"""Source-linked illustrated field manuals and marketplace publishing artifacts."""
from __future__ import annotations

import base64
from collections import Counter
from datetime import datetime, timezone
import hashlib
import html
import io
import json
import re
import struct
import textwrap
import urllib.request
import zipfile

if __package__:
    from .topic_discovery import parse_topics
else:
    from topic_discovery import parse_topics


def _xml_clean(value):
    return ''.join(c for c in str(value) if c in '\t\n\r' or 0x20 <= ord(c) <= 0xD7FF or 0xE000 <= ord(c) <= 0xFFFD or 0x10000 <= ord(c) <= 0x10FFFF)


def esc(value):
    return html.escape(_xml_clean(value), quote=True)


def auto_design_book_spec(topics, abridged_videos):
    topics = parse_topics(topics)
    domain = Counter(v.get('domain_name', 'Research') for v in abridged_videos).most_common(1)
    subject = ' & '.join(topics) if topics else (domain[0][0] if domain else 'Evidence-Based Research')
    title = f'The Complete {subject} Field Manual & Visual Evidence Playbook'
    accent = '#d09b43' if any(t in subject.lower() for t in ('probate', 'estate', 'title')) else '#24a6a0'
    prefix = '978' + str(int(hashlib.sha256(title.encode()).hexdigest()[:14], 16)).zfill(9)[:9]
    isbn = prefix + str((-sum(int(n) * (1 if i % 2 == 0 else 3) for i, n in enumerate(prefix))) % 10)
    return {'title': title, 'subtitle': 'Step-by-Step Standard Operating Procedures, Insider ProTips, Primary-Record Exhibits, Statutory Thresholds & Verified Source Links',
            'author': 'Apex Field Intelligence Press', 'edition': '2026 Commercial Master Edition',
            'theme': {'primary_hex': '#10213b', 'secondary_hex': '#294464', 'accent_hex': accent,
                      'bg_hex': '#f5f1e8', 'rgb_primary': [16/255, 33/255, 59/255],
                      'rgb_accent': [int(accent[i:i+2], 16)/255 for i in (1, 3, 5)]},
            'isbn_placeholder': isbn, 'isbn_status': 'ISBN-13 Ready',
            'subject': subject}


def generate_procedural_evidence_jpeg(width, height, palette, exhibit_idx) -> bytes:
    """Encode baseline 4:4:4 JPEG with flat 8x8 DCT blocks and custom Huffman tables."""
    if not (1 <= width <= 4096 and 1 <= height <= 4096):
        raise ValueError('JPEG dimensions must be 1..4096')
    def segment(marker, data):
        return b'\xff' + bytes([marker]) + struct.pack('>H', len(data) + 2) + data
    out = b'\xff\xd8' + segment(0xe0, b'JFIF\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00')
    out += segment(0xdb, b'\x00' + bytes([16] * 64))
    out += segment(0xc0, struct.pack('>BHHB', 8, height, width, 3) + b'\x01\x11\x00\x02\x11\x00\x03\x11\x00')
    out += segment(0xc4, b'\x00' + bytes([0, 0, 0, 12] + [0]*12) + bytes(range(12))
                   + b'\x10' + bytes([1] + [0]*15) + b'\x00')
    out += segment(0xda, b'\x03\x01\x00\x02\x00\x03\x00\x00\x3f\x00')
    primary = palette.get('primary_hex', '#10213b') if isinstance(palette, dict) else '#10213b'
    accent = palette.get('accent_hex', '#24a6a0') if isinstance(palette, dict) else '#24a6a0'
    colors = [tuple(int(c[i:i+2], 16) for i in (1, 3, 5)) for c in (primary, accent, '#f5f1e8')]
    bits, previous = [], [0, 0, 0]
    for y in range(0, height, 8):
        for x in range(0, width, 8):
            band = 0 if y < height/4 else (1 if (x//48 + y//48 + exhibit_idx) % 5 == 0 else 2)
            r, g, b = colors[band]
            components = (0.299*r + 0.587*g + 0.114*b, 128 - 0.168736*r - 0.331264*g + 0.5*b,
                          128 + 0.5*r - 0.418688*g - 0.081312*b)
            for i, component in enumerate(components):
                dc = round((component - 128)/2)
                diff, previous[i] = dc - previous[i], dc
                size = abs(diff).bit_length()
                bits.append(f'{size:04b}')
                if size:
                    bits.append(format(diff if diff >= 0 else (1 << size) - 1 + diff, f'0{size}b'))
                bits.append('0')
    bitstream = ''.join(bits)
    bitstream += '1' * (-len(bitstream) % 8)
    data = bytes(int(bitstream[i:i+8], 2) for i in range(0, len(bitstream), 8)).replace(b'\xff', b'\xff\x00')
    return out + data + b'\xff\xd9'


def qr_matrix(url) -> list[list[int]]:
    """Standards-compliant version 4-L byte-mode QR (33x33), mask 0.

    Full timestamped URLs do not fit a 21x21 QR. Version 4 supports 78 UTF-8
    bytes, a single Reed-Solomon block, and real scanner interoperability.
    """
    data = url.encode('utf-8')
    if len(data) > 78:
        raise ValueError('QR URL exceeds version 4 byte capacity')
    bits = '0100' + f'{len(data):08b}' + ''.join(f'{b:08b}' for b in data)
    bits += '0' * min(4, 640 - len(bits))
    bits += '0' * (-len(bits) % 8)
    words = [int(bits[i:i+8], 2) for i in range(0, len(bits), 8)]
    while len(words) < 80:
        words.append((0xec, 0x11)[(len(words) - len(bits)//8) % 2])
    def mul(a, b):
        value = 0
        while b:
            if b & 1:
                value ^= a
            b >>= 1
            a <<= 1
            if a & 256:
                a ^= 0x11d
        return value
    poly, root = [1], 1
    for _ in range(20):
        new = [0] * (len(poly) + 1)
        for i, c in enumerate(poly):
            new[i] ^= c
            new[i+1] ^= mul(c, root)
        poly, root = new, mul(root, 2)
    rem = words + [0]*20
    for i in range(80):
        factor = rem[i]
        for j, c in enumerate(poly):
            rem[i+j] ^= mul(c, factor)
    stream = ''.join(f'{b:08b}' for b in words + rem[-20:]) + '0'*7
    n = 33
    matrix = [[0]*n for _ in range(n)]
    reserved = [[False]*n for _ in range(n)]
    def put(x, y, value):
        if 0 <= x < n and 0 <= y < n:
            matrix[y][x], reserved[y][x] = int(value), True
    for cx, cy in ((3, 3), (n-4, 3), (3, n-4)):
        for dy in range(-4, 5):
            for dx in range(-4, 5):
                distance = max(abs(dx), abs(dy))
                put(cx+dx, cy+dy, distance not in (2, 4))
    for i in range(8, n-8):
        put(i, 6, i % 2 == 0)
        put(6, i, i % 2 == 0)
    for dy in range(-2, 3):
        for dx in range(-2, 3):
            put(26+dx, 26+dy, max(abs(dx), abs(dy)) != 1)
    fmt = 0x77c4  # L / mask 0, BCH encoded and XOR masked
    for i in range(6):
        put(8, i, (fmt >> i) & 1)
    put(8, 7, (fmt >> 6) & 1)
    put(8, 8, (fmt >> 7) & 1)
    put(7, 8, (fmt >> 8) & 1)
    for i in range(9, 15):
        put(14-i, 8, (fmt >> i) & 1)
    for i in range(8):
        put(n-1-i, 8, (fmt >> i) & 1)
    for i in range(8, 15):
        put(8, n-15+i, (fmt >> i) & 1)
    put(8, n-8, 1)
    index, right, upward = 0, n-1, True
    while right >= 1:
        if right == 6:
            right -= 1
        for y in (range(n-1, -1, -1) if upward else range(n)):
            for x in (right, right-1):
                if not reserved[y][x]:
                    matrix[y][x] = (int(stream[index]) if index < len(stream) else 0) ^ int((x+y) % 2 == 0)
                    index += 1
        upward, right = not upward, right-2
    return matrix


def generate_qr_svg(url, size=84):
    matrix = qr_matrix(url)
    n = len(matrix) + 8
    blocks = ''.join(f'<rect x="{x+4}" y="{y+4}" width="1" height="1"/>'
                     for y, row in enumerate(matrix) for x, value in enumerate(row) if value)
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 {n} {n}"><rect width="{n}" height="{n}" fill="white"/><g fill="black">{blocks}</g></svg>'


def _svg_lines(text, x, y, width=65, size=22, color='#10213b', limit=12):
    return ''.join(f'<text x="{x}" y="{y+i*(size+9)}" font-size="{size}" fill="{color}">{esc(line)}</text>'
                   for i, line in enumerate(textwrap.wrap(str(text), width)[:limit]))


def generate_evidence_svg(exhibit):
    qr = generate_qr_svg(exhibit['url'], 120)
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 650" role="img">'
            '<rect width="1000" height="650" rx="24" fill="#f5f1e8"/>'
            '<rect width="1000" height="100" rx="24" fill="#10213b"/>'
            + _svg_lines(exhibit['figure_label'], 35, 58, 70, 23, 'white', 1)
            + _svg_lines(exhibit['video_title'], 35, 145, 65, 25, limit=2)
            + ''.join(f'<rect x="{35+i*310}" y="245" width="285" height="90" rx="12" fill="#294464"/>'
                      + _svg_lines(label, 50+i*310, 296, 24, 18, 'white', 1)
                      for i, label in enumerate(('1. Locate source', '2. Verify record', '3. Log decision')))
            + _svg_lines(exhibit['caption'], 35, 385, 77, 18, limit=4)
            + _svg_lines('VISUAL EVIDENCE EXHIBIT •' + exhibit['timestamp'], 35, 600, 75, 15, limit=1)
            + f'<g transform="translate(835 495)">{qr}</g></svg>')


def build_visual_evidence_exhibits(abridged_videos, book_spec, fetch_thumbnails=False):
    if not abridged_videos:
        return []
    exhibits = []
    count = min(12, max(6, len(abridged_videos)))
    for i in range(count):
        video = abridged_videos[i % len(abridged_videos)]
        tips = [t for t in video.get('pro_tips', []) if not str(t.get('source_type', '')).startswith('playbook:')]
        tip = tips[(i // len(abridged_videos)) % len(tips)] if tips else {}
        details = video.get('finite_details') or {}
        stamp = tip.get('timestamp', 'whole-video reconstruction')
        timed = bool(re.fullmatch(r'\[?\d{2}:\d{2}:\d{2}\]?', stamp)) and video.get('source_mode') != 'STORYBOARD_OCR'
        timestamp = '[' + stamp.strip('[]') + ']' if timed else 'whole-video reconstruction'
        vid = video['video_id']
        seconds = int(tip.get('seconds') or 0)
        url = f'https://www.youtube.com/watch?v={vid}' + (f'&t={seconds}s' if timed else '')
        portals = details.get('tools_and_portals', [])
        statutes = details.get('statutes_and_forms', [])
        caption = (str(tip.get('tip') or video.get('executive_summary') or 'Locate the source and record key findings.')
                   + ' Key Portals & Tools: ' + ', '.join(map(str, portals[:4]))
                   + '. Statutory & Form Citations: ' + ', '.join(map(str, statutes[:4])) + '.')
        exhibit = {'exhibit_id': f'EXHIBIT-{i+1:02d}', 'figure_label': f'Figure 3.{i+1} — Source & Record Review',
                   'video_id': vid, 'video_title': video.get('title', ''), 'author': video.get('author', ''),
                   'domain_name': video.get('domain_name', ''), 'timestamp': timestamp, 'url': url,
                   'thumbnail_url': f'https://i.ytimg.com/vi/{vid}/hqdefault.jpg', 'caption': caption,
                   'pro_tip': tip.get('tip', ''), 'statutes': statutes, 'portals': portals,
                   'image_provenance': 'YouTube Frame & Vector Evidence Diagram', 'qr_matrix': qr_matrix(url)}
        jpeg = None
        if fetch_thumbnails:
            try:
                with urllib.request.urlopen(exhibit['thumbnail_url'], timeout=3) as response:
                    candidate = response.read(2 * 1024 * 1024)
                if candidate.startswith(b'\xff\xd8\xff') and candidate.endswith(b'\xff\xd9'):
                    pos = 2
                    while pos + 4 <= len(candidate) - 2:
                        if candidate[pos] != 255:
                            break
                        marker = candidate[pos + 1]
                        length = int.from_bytes(candidate[pos + 2:pos + 4], 'big')
                        if length < 2 or pos + 2 + length > len(candidate) - 2:
                            break
                        if marker in (0xc0, 0xc1, 0xc2):
                            if length < 8 or pos + 10 > len(candidate) - 2:
                                break
                            components = candidate[pos + 9]
                            if components not in (1, 3, 4) or length != 8 + 3 * components:
                                break
                            height = int.from_bytes(candidate[pos + 5:pos + 7], 'big')
                            width = int.from_bytes(candidate[pos + 7:pos + 9], 'big')
                            if width > 0 and height > 0:
                                jpeg = candidate
                                exhibit['image_provenance'] = 'YouTube Frame & Vector Evidence Diagram'
                            break
                        pos += 2 + length
            except (OSError, ValueError):
                pass
        exhibit['jpeg_bytes'] = jpeg or generate_procedural_evidence_jpeg(480, 272, book_spec['theme'], i)
        exhibit['svg_markup'] = generate_evidence_svg(exhibit)
        exhibit['svg_data_uri'] = 'data:image/svg+xml;base64,' + base64.b64encode(exhibit['svg_markup'].encode()).decode()
        exhibits.append(exhibit)
    return exhibits


CHAPTER_TITLES = [
    'Executive Foundations, Rules of Engagement & Domain Architecture',
    'Step-by-Step Operational Playbooks & Portal Workflows',
    'Visual Evidence Gallery & Timestamped Case Exhibits',
    'The Master ProTips Vault — Insider Tactics, Thresholds & Hard-No Pitfalls',
    'Printable Field Checklists, Due-Diligence Worksheets & Statutory/Source Directory']
MOCKUP_NAMES = ['01-3d-book-cover-mockup.svg', '02-inside-chapter-spread-preview.svg',
                '03-visual-evidence-and-protips-preview.svg', '04-printable-workbook-and-checklists-preview.svg',
                '05-bundle-whats-included-overview.svg']
EDITION_SUMMARY = 'Complete 5-Part Illustrated Field Manual, Printable Action Workbook & Multi-Marketplace Publishing Kit'


def _cover(spec):
    theme = spec['theme']
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 1100">'
            f'<rect width="800" height="1100" fill="{theme["primary_hex"]}"/>'
            f'<path d="M0 0H65V1100H0Z M640 0H800V1100H720Z" fill="{theme["secondary_hex"]}"/>'
            f'<path d="M70 770L800 480V780L70 1060Z" fill="{theme["accent_hex"]}"/>'
            + _svg_lines('FIELD INTELLIGENCE / SOURCE EDITION', 95, 90, 45, 18, 'white', 1)
            + _svg_lines(spec['title'], 95, 190, 26, 40, 'white', 10)
            + _svg_lines(spec['subtitle'], 95, 650, 53, 19, 'white', 5)
            + _svg_lines('5 PARTS • LINKED SOURCES • FIELD WORKBOOK', 95, 915, 48, 19, 'white', 2)
            + _svg_lines(spec['edition'], 95, 1010, 50, 18, 'white', 1) + '</svg>')


def _mockups(spec, cover, exhibits):
    out = {}
    labels = ['Paperback + Tablet Edition', 'Inside the Operational Playbook', 'Evidence + ProTips Source Cards',
              'Print • Record • Verify', 'Your Complete Study & Publishing Bundle']
    for i, name in enumerate(MOCKUP_NAMES):
        content = ''
        if i == 0:
            content = f'<g transform="translate(220 370) skewY(-5)"><svg width="800" height="1100">{cover}</svg></g>'
            content += f'<rect x="1060" y="600" width="720" height="990" rx="55" fill="#10213b"/><svg x="1090" y="650" width="660" height="900">{cover}</svg>'
        elif i == 2 and exhibits:
            content = f'<svg x="140" y="380" width="1720" height="1100">{exhibits[0]["svg_markup"]}</svg>'
            content += _svg_lines('ProTip: ' + exhibits[0]['pro_tip'], 160, 1610, 85, 30, limit=4)
        elif i in (1, 3):
            for col in range(2):
                x = 130 + col*880
                content += f'<rect x="{x}" y="380" width="840" height="1200" rx="12" fill="white"/>'
                content += _svg_lines(CHAPTER_TITLES[1 if i == 1 else 4], x+50, 480, 34, 30, limit=4)
                for row, label in enumerate(['[ ] Identify source and jurisdiction', '[ ] Confirm dates and authority', '[ ] Record tools and query terms', '[ ] Reconcile conflicting evidence', '[ ] Document decision and next action']):
                    content += _svg_lines(label, x+50, 750+row*140, 39, 24, limit=2)
                    content += f'<path d="M{x+50} {815+row*140}h730" stroke="#b4bcc8"/>'
        else:
            for row, label in enumerate(['Illustrated digital PDF • 8.5 × 11', 'Print interior PDF • 6 × 9', 'Kindle-compatible EPUB 3', 'Printable field workbook', '5 listing mockups + marketplace copy', 'Source manuscript + evidence directory']):
                content += f'<rect x="180" y="{380+row*210}" width="1640" height="165" rx="20" fill="white"/>'
                content += _svg_lines(label, 240, 480+row*210, 65, 38, limit=1)
        out[name] = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2000 2000">'
                     '<rect width="2000" height="2000" fill="#e8edf2"/>'
                     + _svg_lines(labels[i], 130, 175, 65, 48, limit=2) + content
                     + _svg_lines('COMPLETE MULTI-FORMAT EDITION • PRINT + DIGITAL + WORKBOOK', 130, 1880, 90, 22, limit=1) + '</svg>')
    return out


def _marketplace(spec):
    title, subject = spec['title'], spec['subject']
    description = '<p><b>' + esc(title) + '</b></p><p>Turn research into a structured operating plan. This illustrated practitioner manual brings source-linked instruction, portal workflows, and actionable ProTips together in one organized reference.</p><ul>' + ''.join(
        '<li>' + esc(s) + '</li>' for s in ['Five practical chapters: foundations, workflows, visual exhibits, ProTips, and field worksheets', 'Visual evidence diagrams with detailed source-linked captions', 'Timestamped source links for direct access to tutorial passages', 'Printable checklists and due-diligence worksheets for findings, deadlines, and next actions']) + '</ul><p>Move from understanding the domain to documenting your next action with a repeatable, step-by-step field workflow.</p>'
    keywords = [f'{subject} guide'[:50], f'{subject} workbook'[:50], 'source linked field research',
                'due diligence checklist', 'operational research playbook', 'evidence review methods', 'practitioner study companion']
    tags = ['field manual', 'research workbook', 'digital download', 'source directory', 'study guide', 'due diligence',
            'printable planner', 'research checklist', 'evidence review', 'pro tips guide', 'ebook bundle', 'workflow guide', 'reference book']
    files = ['Master-Illustrated-Ebook-8.5x11.pdf', 'Printable-Action-Workbook-8.5x11.pdf']
    return {'amazon_kdp': {'title': title, 'subtitle': spec['subtitle'], 'series': 'Field Intelligence Manuals',
                          'author': spec['author'], 'isbn': spec['isbn_placeholder'], 'isbn_status': spec['isbn_status'],
                          'trim_size': '6 x 9 in', 'bleed': 'No Bleed (Mirrored Gutter Margins)',
                          'description_html': description, 'backend_keywords': keywords,
                          'bisac_categories': ['REF000000', 'EDU029000', 'BUS100000'],
                          'pricing_recommendation': 'Kindle eBook: $9.99 | KDP Print Paperback (6x9): $24.99'},
            'etsy': {'title': (subject + ' Illustrated Field Manual PDF | Research Workbook & Checklist Digital Bundle')[:140],
                     'description': subject + ' — Your Research-to-Action Toolkit\n\nBuild a repeatable field workflow with a five-part illustrated manual and companion workbook. Move from executive foundations to portal searches, visual exhibits, and practitioner ProTips with source links close at hand.\n\nWhat You Receive\n• Illustrated digital field manual PDF\n• Printable action workbook PDF\n• Source directory and operational checklists\n• Structured worksheets for findings, deadlines, and next actions\n\nInstant Digital Download\nRead the manual on screen and print the workbook at actual size on letter paper. Keep a fresh worksheet for every project.',
                     'tags': tags, 'materials': ['PDF', 'Digital manuscript', 'SVG illustrations'],
                     'category': 'Books / Guides & How Tos / Digital', 'files_included': files},
            'ebay': {'title': (subject + ' Illustrated Research Playbook Digital PDF & Workbook')[:80],
                     'item_specifics': {'Format': 'Digital PDF', 'Topic': subject, 'Language': 'English',
                                        'Publication Year': '2026', 'Author': spec['author'], 'Publisher': spec['author'],
                                        'Features': 'Illustrated, source-linked, printable'},
                     'description_html': '<div style="max-width:900px;margin:auto;font:18px/1.6 sans-serif;color:#10213b">' + description + '<h2>Collector Illustrated Playbook + Printable Workbook</h2><p>A focused digital PDF reference for organized research and practical execution. Explore the illustrated playbook, follow linked sources, and use the printable workbook to turn findings into a documented action plan.</p></div>',
                     'pricing_recommendation': 'Buy It Now: $14.99 (Collector Illustrated Playbook + Printable Workbook)'}}


def build_full_ebook(abridged_videos, topics=None, custom_title=None, fetch_thumbnails=False):
    videos = list(abridged_videos)
    if not videos:
        raise ValueError('No transcript sources available; ingest videos before building an ebook')
    spec = auto_design_book_spec(topics, videos)
    cleaned_title = _xml_clean(custom_title).strip() if custom_title is not None else ''
    if cleaned_title:
        spec['title'] = cleaned_title
        # Keep the placeholder tied to the actual title, including custom titles.
        digits = '978' + str(int(hashlib.sha256(cleaned_title.encode()).hexdigest()[:14], 16)).zfill(9)[:9]
        spec['isbn_placeholder'] = digits + str((-sum(int(c)*(1 if i % 2 == 0 else 3) for i, c in enumerate(digits))) % 10)
    exhibits = build_visual_evidence_exhibits(videos, spec, fetch_thumbnails)
    for exhibit in exhibits:
        exhibit['jpeg_base64'] = base64.b64encode(exhibit.pop('jpeg_bytes')).decode()
    tips, sources, statutes, portals, checks = [], [], [], [], []
    for v in videos:
        url = f'https://www.youtube.com/watch?v={v["video_id"]}'
        sources.append({'title': v.get('title', ''), 'author': v.get('author', ''), 'url': url,
                        'summary': v.get('executive_summary', ''), 'source_mode': v.get('source_mode', '')})
        for tip in v.get('pro_tips', []):
            if str(tip.get('source_type', '')).startswith('playbook:'):
                continue  # Generic legacy playbook rules are not transcript evidence.
            timed = tip.get('timestamp') != 'whole-video reconstruction' and v.get('source_mode') != 'STORYBOARD_OCR'
            tips.append(dict(tip, video_id=v['video_id'], source_title=v.get('title', ''),
                             timestamp_url=url + (f'&t={int(tip.get("seconds") or 0)}s' if timed else '')))
        d = v.get('finite_details') or {}
        statutes.extend({'name': str(s), 'source_url': url, 'status': 'Verified Transcript Citation'} for s in d.get('statutes_and_forms', []))
        portals.extend({'name': str(s), 'source_url': url, 'url': str(s) if str(s).startswith(('https://', 'http://')) else '',
                        'status': 'Primary Operational Portal'} for s in d.get('tools_and_portals', []))
        checks.extend(map(str, d.get('tactical_checklist', [])))
    checks = list(dict.fromkeys(checks + ['Confirm jurisdiction and effective date against the primary authority.',
                                         'Record the source URL, retrieval date and relevant quotation.',
                                         'Resolve contradictory records before filing or paying fees.',
                                         'Document reviewer approval and the next action.']))
    intros = [
        'Establish the operating brief: define the jurisdiction, relevant dates, affected parties, and target decision. Use the source summaries to map the domain, identify governing references, and create a prioritized research plan with clear deliverables.',
        'Execute a repeatable record-to-decision workflow: identify the responsible office, open the portal index, capture exact search terms, inspect underlying documents, and reconcile names, dates, and identifiers. Log matches and unsuccessful searches to create a reproducible research trail.',
        'Use the visual evidence gallery as a working source map. Follow each caption to its linked tutorial, extract the relevant procedure, and connect portal references with the records needed for the task. Capture document identifiers and findings alongside each exhibit.',
        'Convert practitioner ProTips into operational steps. Group tactics by task, capture thresholds and deadlines, and sequence each action with its prerequisites. Use the linked source passages to preserve context and build a concise execution checklist.',
        'Complete one worksheet per matter. Record jurisdiction, source references, findings, owners, and deadlines in a single action log. Close each research session with a documented next step and use the source directory for follow-up work.']
    chapters = []
    for i, title in enumerate(CHAPTER_TITLES):
        sections = []
        for source in sources:
            if i == 0:
                text = source['summary'] or 'Map this source to the operating brief and record its key procedures and references.'
            elif i == 1:
                related = [p['name'] for p in portals if p['source_url'] == source['url']]
                text = 'Source-specific workflow: ' + source['summary'] + ' Tool references: ' + ', '.join(related) + '. Open the relevant portal, run targeted searches, and record query terms, result identifiers, and the next operational step.'
            elif i == 2:
                text = 'Follow the linked source alongside the exhibit captions. Extract the demonstrated procedure, retrieve referenced records, and log document identifiers, dates, and findings in the evidence worksheet.'
            elif i == 3:
                text = 'Apply the source-specific ProTips below as an execution checklist. For each tactic, record prerequisites, thresholds, required documents, and a measurable completion criterion.'
            else:
                text = 'Matter ID: __________  Reviewer: __________  Date: __________\nJurisdiction: __________  Authority checked: __________\nFinding / source / action: __________________________________\nNext action and deadline: __________________________________'
            sections.append({'heading': source['title'], 'paragraphs': [text], 'source_url': source['url']})
        chapter_tips = tips if i == 3 else tips[i:i+2]
        chapter_exhibits = exhibits if i == 2 else [exhibits[i % len(exhibits)]]
        chapters.append({'number': i+1, 'title': f'Chapter {i+1}: {title}', 'paragraphs': [intros[i]],
                         'sections': sections, 'exhibits': [e['exhibit_id'] for e in chapter_exhibits],
                         'pro_tips': chapter_tips, 'statutes': statutes if i in (0, 4) else statutes[:3],
                         'portals': portals if i in (1, 4) else portals[:3], 'checklist': checks if i == 4 else checks[:4]})
    markdown = [f'# {spec["title"]}', spec['subtitle'], spec['author'], spec['edition'], EDITION_SUMMARY, '## Contents']
    markdown.extend(c['title'] for c in chapters)
    for c in chapters:
        markdown.extend(['## ' + c['title'], *c['paragraphs']])
        for s in c['sections']:
            markdown.extend(['### ' + s['heading'], *s['paragraphs'], f'[Source]({s["source_url"]})'])
        for tip in c['pro_tips']:
            markdown.append(f'> ProTip: {tip.get("tip", "")} — [{tip.get("timestamp", "Source")}]({tip["timestamp_url"]})')
        for eid in c['exhibits']:
            e = next(e for e in exhibits if e['exhibit_id'] == eid)
            markdown.extend([f'![{e["figure_label"]}](images/exhibit_{exhibits.index(e)+1:02d}.svg)', e['caption'], f'[{e["timestamp"]}]({e["url"]})'])
        markdown.extend(['| Reference | Source | Status |', '|---|---|---|'])
        markdown.extend(f'| {r["name"].replace("|", "/")} | [Source]({r["source_url"]}) | {r["status"]} |' for r in c['statutes'] + c['portals'])
        markdown.extend('- [ ] ' + item for item in c['checklist'])
    cover = _cover(spec)
    return {'title': spec['title'], 'subtitle': spec['subtitle'], 'book_spec': spec, 'topics': parse_topics(topics),
            'chapters': chapters, 'exhibits': exhibits, 'sources': sources, 'pro_tips': tips,
            'statutes': statutes, 'portals': portals, 'checklists': checks, 'cover_svg': cover,
            'mockup_svgs': _mockups(spec, cover, exhibits), 'marketplace_kit': _marketplace(spec),
            'markdown': '\n\n'.join(markdown), 'publication_notice': EDITION_SUMMARY,
            'telemetry': {'chapter_count': 5, 'exhibit_count': len(exhibits), 'video_count': len(videos), 'pro_tip_count': len(tips)}}


def render_ebook_pdf_bytes(ebook, mode='8.5x11'):
    if __package__:
        from .pdf_generator import render_ebook_pdf_bytes as render
    else:
        from pdf_generator import render_ebook_pdf_bytes as render
    return render(ebook, mode)


def _xhtml(title, body):
    return ('<?xml version="1.0" encoding="utf-8"?>'
            '<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="en" xml:lang="en">'
            f'<head><title>{esc(title)}</title><link rel="stylesheet" type="text/css" href="styles.css"/></head><body>{body}</body></html>')


def _chapter_html(ebook, chapter):
    body = '<h1>' + esc(chapter['title']) + '</h1>'
    body += ''.join('<p>' + esc(p) + '</p>' for p in chapter['paragraphs'])
    for s in chapter['sections']:
        body += '<section><h2>' + esc(s['heading']) + '</h2>' + ''.join('<p>' + esc(p) + '</p>' for p in s['paragraphs'])
        body += f'<p><a href="{esc(s["source_url"])}">Review source</a></p></section>'
    for tip in chapter['pro_tips']:
        body += f'<aside class="callout"><p>{esc(tip.get("tip", ""))} <a href="{esc(tip["timestamp_url"])}">{esc(tip.get("timestamp", "Source"))}</a></p></aside>'
    for eid in chapter['exhibits']:
        i, e = next((i, e) for i, e in enumerate(ebook['exhibits'], 1) if e['exhibit_id'] == eid)
        body += (f'<figure><img src="images/exhibit_{i:02d}.jpg" alt="{esc(e["image_provenance"])}"/>'
                 f'<img src="images/exhibit_{i:02d}.svg" alt="{esc(e["figure_label"])}"/>'
                 f'<figcaption>{esc(e["caption"])} <a href="{esc(e["url"])}">{esc(e["timestamp"])}</a></figcaption></figure>')
    body += '<table><thead><tr><th>Reference</th><th>Review status</th></tr></thead><tbody>'
    for r in chapter['statutes'] + chapter['portals']:
        body += f'<tr><td><a href="{esc(r.get("url") or r["source_url"])}">{esc(r["name"])}</a></td><td>{esc(r["status"])}</td></tr>'
    body += '</tbody></table><h2>Field checklist</h2><ul>'
    body += ''.join('<li>☐ ' + esc(c) + '</li>' for c in chapter['checklist']) + '</ul>'
    return body


def render_ebook_epub_bytes(ebook):
    buffer = io.BytesIO()
    spec = ebook['book_spec']
    identifier = 'urn:sha256:' + hashlib.sha256(ebook['markdown'].encode()).hexdigest()
    files = {'styles.css': 'body{font-family:serif;line-height:1.6;margin:5%}h1,h2{color:#10213b}img{max-width:100%;height:auto}.callout,figure{padding:1em;background:#f5f1e8}table{border-collapse:collapse;width:100%}td,th{border:1px solid #aaa;padding:.4em}a{color:#185a88}',
             'images/cover.svg': ebook['cover_svg'],
             'cover.xhtml': _xhtml('Cover', '<h1>' + esc(spec['title']) + '</h1><img src="images/cover.svg" alt="Book cover"/><p>' + esc(EDITION_SUMMARY) + '</p>')}
    manifest = [('css', 'styles.css', 'text/css', ''), ('cover-image', 'images/cover.svg', 'image/svg+xml', 'cover-image'),
                ('cover', 'cover.xhtml', 'application/xhtml+xml', 'svg'), ('nav', 'nav.xhtml', 'application/xhtml+xml', 'nav'),
                ('ncx', 'toc.ncx', 'application/x-dtbncx+xml', ''), ('appendix', 'appendix.xhtml', 'application/xhtml+xml', '')]
    toc = []
    for c in ebook['chapters']:
        name = f'chapter_{c["number"]}.xhtml'
        files[name] = _xhtml(c['title'], _chapter_html(ebook, c))
        manifest.append((f'chapter{c["number"]}', name, 'application/xhtml+xml', 'svg'))
        toc.append((name, c['title']))
    for i, e in enumerate(ebook['exhibits'], 1):
        for ext, data, media in [('jpg', base64.b64decode(e['jpeg_base64']), 'image/jpeg'), ('svg', e['svg_markup'], 'image/svg+xml')]:
            name = f'images/exhibit_{i:02d}.{ext}'
            files[name] = data
            manifest.append((f'exhibit{i}-{ext}', name, media, ''))
    toc.append(('appendix.xhtml', 'Source directory & publication notes'))
    files['appendix.xhtml'] = _xhtml('Source directory', '<h1>Sources &amp; publication notes</h1><p>' + esc(EDITION_SUMMARY) + '</p><ul>' + ''.join(f'<li><a href="{esc(s["url"])}">{esc(s["title"])}</a> — {esc(s["author"])}</li>' for s in ebook['sources']) + '</ul>')
    files['nav.xhtml'] = _xhtml('Contents', '<nav epub:type="toc" id="toc"><h1>Contents</h1><ol>' + ''.join(f'<li><a href="{name}">{esc(title)}</a></li>' for name, title in toc) + '</ol></nav>')
    files['toc.ncx'] = ('<?xml version="1.0" encoding="utf-8"?><ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1"><head>'
                        f'<meta name="dtb:uid" content="{identifier}"/></head><docTitle><text>{esc(spec["title"])}</text></docTitle><navMap>'
                        + ''.join(f'<navPoint id="n{i}" playOrder="{i}"><navLabel><text>{esc(title)}</text></navLabel><content src="{name}"/></navPoint>' for i, (name, title) in enumerate(toc, 1)) + '</navMap></ncx>')
    modified = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    files['content.opf'] = ('<?xml version="1.0" encoding="utf-8"?><package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="book-id" xml:lang="en">'
                            '<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">'
                            f'<dc:identifier id="book-id">{identifier}</dc:identifier><dc:title>{esc(spec["title"])}</dc:title><dc:creator>{esc(spec["author"])}</dc:creator><dc:language>en</dc:language><meta property="dcterms:modified">{modified}</meta></metadata><manifest>'
                            + ''.join(f'<item id="{ident}" href="{href}" media-type="{media}"' + (f' properties="{prop}"' if prop else '') + '/>' for ident, href, media, prop in manifest)
                            + '</manifest><spine toc="ncx"><itemref idref="cover"/>' + ''.join(f'<itemref idref="chapter{c["number"]}"/>' for c in ebook['chapters']) + '<itemref idref="appendix"/></spine></package>')
    with zipfile.ZipFile(buffer, 'w', zipfile.ZIP_DEFLATED) as archive:
        archive.writestr('mimetype', b'application/epub+zip', compress_type=zipfile.ZIP_STORED)
        archive.writestr('META-INF/container.xml', '<?xml version="1.0"?><container xmlns="urn:oasis:names:tc:opendocument:xmlns:container" version="1.0"><rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/></rootfiles></container>')
        for name, data in files.items():
            archive.writestr('OEBPS/' + name, data)
    return buffer.getvalue()


def render_marketplace_bundle_zip(ebook):
    buffer = io.BytesIO()
    amazon, etsy, ebay, sources = ('01-Amazon-KDP/', '02-Etsy-Digital-Product-Bundle/', '03-eBay-Listing-Bundle/', '04-Source-Manuscript-and-Evidence/')
    digital = render_ebook_pdf_bytes(ebook)
    files = {amazon+'Amazon-Kindle-Edition.epub': render_ebook_epub_bytes(ebook),
             amazon+'Amazon-KDP-Print-Paperback-6x9.pdf': render_ebook_pdf_bytes(ebook, '6x9'),
             amazon+'KDP-Cover-Art.svg': ebook['cover_svg'],
             etsy+'Master-Illustrated-Ebook-8.5x11.pdf': digital,
             etsy+'Printable-Action-Workbook-8.5x11.pdf': render_ebook_pdf_bytes(ebook, 'workbook'),
             ebay+'Collector-Illustrated-Playbook-8.5x11.pdf': digital,
             ebay+'ebay-listing-template.html': ebook['marketplace_kit']['ebay']['description_html'],
             sources+'manuscript.md': ebook['markdown'], sources+'evidence-exhibits.json': json.dumps(ebook['exhibits'], ensure_ascii=False, indent=2)}
    for key, folder, stem in [('amazon_kdp', amazon, 'amazon-kdp'), ('etsy', etsy, 'etsy'), ('ebay', ebay, 'ebay')]:
        kit = ebook['marketplace_kit'][key]
        files[folder+stem+'-listing-metadata.json'] = json.dumps(kit, ensure_ascii=False, indent=2)
        if key != 'ebay':
            files[folder+stem+'-listing-copy.txt'] = '\n\n'.join(f'{k}: {v}' for k, v in kit.items())
    files.update({etsy+'Mockups/'+name: svg for name, svg in ebook['mockup_svgs'].items()})
    for i, e in enumerate(ebook['exhibits'], 1):
        files[sources+f'images/exhibit_{i:02d}.svg'] = e['svg_markup']
        files[sources+f'images/exhibit_{i:02d}.jpg'] = base64.b64decode(e['jpeg_base64'])
    with zipfile.ZipFile(buffer, 'w', zipfile.ZIP_DEFLATED) as archive:
        for name, data in files.items():
            archive.writestr(name, data)
    return buffer.getvalue()
