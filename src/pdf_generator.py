#!/usr/bin/env python3
"""Dependency-free PDF 1.4 writer for ProTip / Agent Operational Reports.

Only the Python standard library is used: Type1 base-14 fonts, ASCII transliteration,
word wrapping, a dark navy cover banner with telemetry boxes and `Page X of Y` footers.
"""
from __future__ import annotations

import re
from datetime import datetime, timezone

PAGE_W, PAGE_H, MARGIN = 612.0, 792.0, 54.0
BODY_W = PAGE_W - 2 * MARGIN
NAVY, NAVY_SOFT, ACCENT = (0.055, 0.094, 0.21), (0.12, 0.19, 0.38), (0.09, 0.42, 0.78)
INK, GREY, WHITE = (0.10, 0.12, 0.16), (0.45, 0.48, 0.55), (1.0, 1.0, 1.0)
PALE, TIP_BG, RULE = (0.70, 0.77, 0.91), (0.93, 0.96, 1.0), (0.85, 0.87, 0.90)
FONT_IDS = {"body": "F1", "bold": "F2", "mono": "F3"}
HEADINGS = {1: (16.5, 15.0), 2: (14.0, 14.0), 3: (11.5, 10.0), 4: (10.5, 8.0)}
FLOOR_Y = MARGIN + 36

_SUBS = (("—", " - "), ("–", "-"), ("−", "-"), ("…", "..."), (" ", " "),
         ("‘", "'"), ("’", "'"), ("“", '"'), ("”", '"'), ("•", "* "),
         ("·", " - "), ("§", "Sec. "), ("→", "->"), ("✓", "v"), ("×", "x"))
_NARROW = set("iljtfIr.,;:'`|!()[]{}- ")
_WIDE = set("MWmw@%")


def ascii_text(value) -> str:
    """Transliterate arbitrary text to printable ASCII (PDF WinAnsi-safe)."""
    text = str("" if value is None else value)
    for bad, good in _SUBS:
        text = text.replace(bad, good)
    return "".join(c if 32 <= ord(c) < 127 else ("\n" if c == "\n" else " " if c in "\t\r" else "?")
                   for c in text)


def _esc(text: str) -> str:
    return text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


# Base-14 AFM advance widths, ASCII 32..126, in thousandths of an em.
_WIDTHS = {
    'body': dict(zip(map(chr, range(32, 127)), (
        278,278,355,556,556,889,667,191,333,333,389,584,278,333,278,278,
        *([556]*10),278,278,584,584,584,556,1015,
        667,667,722,722,667,611,778,722,278,500,667,556,833,722,778,667,778,722,667,611,722,667,944,667,667,611,
        278,278,278,469,556,333,
        556,556,500,556,556,278,556,556,222,222,500,222,833,556,556,556,556,333,500,278,556,500,722,500,500,500,
        334,260,334,584))),
    'bold': dict(zip(map(chr, range(32, 127)), (
        278,333,474,556,556,889,722,238,333,333,389,584,278,333,278,278,
        *([556]*10),333,333,584,584,584,611,975,
        722,722,722,722,667,611,778,722,278,556,722,611,833,722,778,667,778,722,667,611,722,667,944,667,667,611,
        333,278,333,584,556,333,
        556,611,556,611,556,333,611,611,278,278,556,278,889,611,611,611,611,389,556,333,611,556,778,556,556,500,
        389,280,389,584)))
}


def text_width(text: str, size: float, mono: bool = False, font='body') -> float:
    font = {'F1': 'body', 'F2': 'bold', 'F3': 'mono'}.get(font, font)
    if mono or font == 'mono':
        return size * 0.6 * len(text)
    return size * sum(_WIDTHS[font].get(c, 1000) for c in text) / 1000


def wrap(text: str, size: float, width: float, mono: bool = False, font='body') -> list[str]:
    font = {'F1': 'body', 'F2': 'bold', 'F3': 'mono'}.get(font, font)
    mono = mono or font == 'mono'
    text = ascii_text(text)
    if not mono:
        text = ' '.join(text.split())
    limit = width * 0.99
    lines = []
    for source in text.split('\n'):
        start, pos, last_space, used = 0, 0, -1, 0.0
        while pos < len(source):
            char = source[pos]
            advance = size * (0.6 if mono else _WIDTHS[font].get(char, 1000) / 1000)
            if used + advance > limit and pos > start:
                end = last_space if not mono and last_space > start else pos
                lines.append(source[start:end])
                start = end + 1 if end == last_space and not mono else end
                pos, last_space, used = start, -1, 0.0
                continue
            used += advance
            if char == ' ':
                last_space = pos
            pos += 1
        lines.append(source[start:])
    return lines or ['']


def _rect(x, y, w, h, color) -> str:
    return (f"{color[0]:.3f} {color[1]:.3f} {color[2]:.3f} rg "
            f"{x:.2f} {y:.2f} {max(w, 0.1):.2f} {max(h, 0.1):.2f} re f")


def _text(x, y, body, font="body", size=10.5, color=INK) -> str:
    return (f"{color[0]:.3f} {color[1]:.3f} {color[2]:.3f} rg BT /{FONT_IDS[font]} {size:.2f} Tf "
            f"1 0 0 1 {x:.2f} {y:.2f} Tm ({_esc(body)}) Tj ET")


def _item(text, font="body", size=10.5, indent=0.0, before=0.0, after=3.0, color=INK, bg=None) -> dict:
    return {"text": text, "font": font, "size": size, "indent": indent,
            "before": before, "after": after, "color": color, "bg": bg}


def _inline(text: str) -> str:
    out = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", ascii_text(text))
    out = re.sub(r"\[([^\]]*)\]\(([^)]*)\)", r"\1 (\2)", out)
    out = out.replace("**", "").replace("`", "").replace("~~", "")
    return re.sub(r"(?<!\w)_([^_]+)_(?!\w)", r"\1", out).strip()


def _as_list(value) -> list:
    if value is None:
        return []
    return list(value) if isinstance(value, (list, tuple)) else [value]


def _norm_telemetry(telemetry) -> list[tuple[str, str]]:
    out = []
    for entry in _as_list(telemetry)[:4]:
        if isinstance(entry, dict):
            label = next((entry[k] for k in ("label", "name", "key") if k in entry), "")
            value = next((entry[k] for k in ("value", "count", "total") if k in entry), "")
        elif isinstance(entry, (list, tuple)) and len(entry) >= 2:
            label, value = entry[0], entry[1]
        else:
            label, _, value = ascii_text(entry).partition(":")
            if not value:
                label, value = "", label
        out.append((ascii_text(label).strip(), ascii_text(value).strip()))
    return out


def _blocks_to_items(blocks) -> list[dict]:
    items = []
    for block in _as_list(blocks):
        block = {"heading": block} if isinstance(block, str) else dict(block or {})
        heading = block.get("heading") or block.get("title")
        if heading:
            level = max(1, min(4, int(block.get("level") or 2)))
            size, before = HEADINGS[level]
            items.append(_item(_inline(heading), "bold", size, 0.0, before, 4.0,
                               NAVY if level <= 2 else ACCENT))
        for para in _as_list(block.get("body") or block.get("text") or block.get("paragraphs")):
            items.append(_item(_inline(para), "body", 10.5, 0.0, 1.0, 4.0))
        for bullet in _as_list(block.get("bullets")):
            items.append(_item("- " + _inline(bullet), "body", 10.5, 12.0, 0.0, 1.5))
        for tip in _as_list(block.get("pro_tips")):
            items.append(_item("ProTip: " + _inline(tip), "bold", 10.0, 18.0, 6.0, 6.0,
                               NAVY_SOFT, TIP_BG))
        for code in _as_list(block.get("code")):
            items.append(_item(ascii_text(code), "mono", 8.6, 12.0, 0.0, 1.0, (0.2, 0.24, 0.3)))
    return items


def _layout(items, first_top, next_top) -> list[list[dict]]:
    pages, page, y = [], [], first_top
    for item in items:
        mono = item["font"] == "mono"
        lines = wrap(item["text"], item["size"], BODY_W - item["indent"], mono, item['font'])
        lead = item["size"] * 1.34
        y -= item["before"]
        for line in lines:
            if y - lead < FLOOR_Y:
                pages.append(page)
                page, y = [], next_top
            y -= lead
            page.append({"x": MARGIN + item["indent"], "y": y, "text": line, "lead": lead,
                         "font": item["font"], "size": item["size"],
                         "color": item["color"], "bg": item["bg"]})
        y -= item["after"]
    pages.append(page)
    return pages


def _banner(title, subtitle, telemetry, height) -> list[str]:
    ops = [_rect(0, PAGE_H - height, PAGE_W, height, NAVY),
           _rect(0, PAGE_H - height, PAGE_W, 5, ACCENT)]
    y = PAGE_H - 46
    for line in wrap(title, 22, BODY_W, font='bold'):
        ops.append(_text(MARGIN, y, line, "bold", 22, WHITE))
        y -= 26
    for line in wrap(subtitle, 10.5, BODY_W)[:2] if subtitle else []:
        ops.append(_text(MARGIN, y, line, "body", 10.5, PALE))
        y -= 14
    if telemetry:
        count = len(telemetry)
        width = (BODY_W - 10.0 * (count - 1)) / count
        box_y = PAGE_H - height + 14
        for i, (label, value) in enumerate(telemetry):
            x = MARGIN + i * (width + 10.0)
            ops.append(_rect(x, box_y, width, 46, NAVY_SOFT))
            ops.append(_rect(x, box_y, width, 2.5, ACCENT))
            ops.append(_text(x + 10, box_y + 26, value[:16], "bold", 15, WHITE))
            ops.append(_text(x + 10, box_y + 11, label.upper()[:22], "body", 7.5, PALE))
    return ops


def _content(atoms, page_no, total, banner) -> str:
    ops = list(banner or [])
    for atom in atoms:
        if atom["bg"]:
            width = MARGIN + BODY_W - atom["x"] + 12
            ops.append(_rect(atom["x"] - 12, atom["y"] - 4.5, width, atom["lead"] + 1, atom["bg"]))
            ops.append(_rect(atom["x"] - 12, atom["y"] - 4.5, 3, atom["lead"] + 1, ACCENT))
        ops.append(_text(atom["x"], atom["y"], atom["text"], atom["font"], atom["size"], atom["color"]))
    footer = f"Page {page_no} of {total}"
    ops.append(_rect(MARGIN, 58, BODY_W, 0.7, RULE))
    ops.append(_text((PAGE_W - text_width(footer, 9)) / 2, 42, footer, "body", 9, GREY))
    return "\n".join(ops)


def _assemble(streams, title) -> bytes:
    pages = len(streams)
    fonts = 3 + 2 * pages
    objects = [b"<< /Type /Catalog /Pages 2 0 R >>",
               ("<< /Type /Pages /Count %d /Kids [%s] >>"
                % (pages, " ".join(f"{3 + i} 0 R" for i in range(pages)))).encode("latin-1")]
    for i in range(pages):
        objects.append((f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {PAGE_W:.0f} {PAGE_H:.0f}] "
                        f"/Resources << /Font << /F1 {fonts} 0 R /F2 {fonts + 1} 0 R "
                        f"/F3 {fonts + 2} 0 R >> >> /Contents {3 + pages + i} 0 R >>").encode("latin-1"))
    for stream in streams:
        data = stream.encode("latin-1", "replace")
        objects.append(f"<< /Length {len(data)} >>\nstream\n".encode("latin-1") + data + b"\nendstream")
    for base in ("Helvetica", "Helvetica-Bold", "Courier"):
        objects.append((f"<< /Type /Font /Subtype /Type1 /BaseFont /{base} "
                        f"/Encoding /WinAnsiEncoding >>").encode("latin-1"))
    created = datetime.now(timezone.utc).strftime("D:%Y%m%d%H%M%SZ")
    objects.append((f"<< /Title ({_esc(title)}) /Producer (ProTip Abridger PDF writer) "
                    f"/CreationDate ({created}) >>").encode('latin-1'))
    info_id = len(objects)
    buf, offsets = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n"), []
    for number, body in enumerate(objects, 1):
        offsets.append(len(buf))
        buf += f"{number} 0 obj\n".encode("latin-1") + body + b"\nendobj\n"
    start = len(buf)
    buf += f"xref\n0 {len(objects) + 1}\n".encode("latin-1") + b"0000000000 65535 f \n"
    for offset in offsets:
        buf += f"{offset:010d} 00000 n \n".encode("latin-1")
    buf += (f"trailer\n<< /Size {len(objects) + 1} /Root 1 0 R /Info {info_id} 0 R >>\n"
            f"startxref\n{start}\n%%EOF\n").encode("latin-1")
    return bytes(buf)


def render_pdf_bytes(title: str, subtitle: str = "", telemetry: list | None = None,
                     sections: list | None = None) -> bytes:
    """Render a paginated PDF 1.4 document and return its raw bytes."""
    title = ascii_text(title).strip() or "Agent Operational Report"
    subtitle = ascii_text(subtitle).strip()
    tele = _norm_telemetry(telemetry)
    height = 112.0 + (62.0 if tele else 0.0) + (14.0 if subtitle else 0.0)
    height += max(0, len(wrap(title, 22, BODY_W, font='bold')) - 2) * 26
    pages = _layout(_blocks_to_items(sections), PAGE_H - height - 26, PAGE_H - MARGIN)
    banner = _banner(title, subtitle, tele, height)
    return _assemble([_content(atoms, i + 1, len(pages), banner if i == 0 else None)
                      for i, atoms in enumerate(pages)], title)


def _markdown_blocks(markdown_text: str) -> list[dict]:
    blocks, para, code, fenced = [], [], [], False

    def flush():
        if para:
            blocks.append({"body": [" ".join(para)]})
            del para[:]

    for raw in ascii_text(markdown_text).splitlines():
        line = raw.rstrip()
        if line.strip().startswith("```"):
            flush()
            fenced = not fenced
            if not fenced and code:
                blocks.append({"code": list(code)})
                del code[:]
            continue
        if fenced:
            code.append(line)
            continue
        stripped = line.strip()
        if not stripped:
            flush()
            continue
        head = re.match(r"(#{1,6})\s+(.*)", stripped)
        if head:
            flush()
            blocks.append({"heading": head.group(2), "level": len(head.group(1))})
            continue
        if stripped.startswith("|"):
            flush()
            blocks.append({"code": [line]})
            continue
        tip = re.match(r"(?:\d+\.|[-*>])?\s*\*\*\[(.+?)\]\*\*\s*(.*)", stripped)
        if tip or stripped.lower().startswith("protip"):
            flush()
            blocks.append({"pro_tips": [f"[{tip.group(1)}] {tip.group(2)}" if tip else stripped]})
            continue
        bullet = re.match(r"[-*+]\s+(.*)", stripped) or re.match(r"(?:>)\s+(.*)", stripped)
        if bullet:
            flush()
            blocks.append({"bullets": [bullet.group(1)]})
            continue
        numbered = re.match(r"(\d+)\.\s+(.*)", stripped)
        if numbered:
            flush()
            blocks.append({"bullets": [f"{numbered.group(1)}. {numbered.group(2)}"]})
            continue
        para.append(stripped)
    flush()
    if code:
        blocks.append({"code": code})
    return blocks


def markdown_to_pdf_bytes(markdown_text: str, title: str = "Agent Operational Report",
                          subtitle: str = "", telemetry: list | None = None) -> bytes:
    """Convert report markdown into a paginated PDF, promoting the leading H1/lede."""
    blocks = _markdown_blocks(markdown_text or "")
    if blocks and blocks[0].get("level") == 1 and blocks[0].get("heading"):
        heading = _inline(blocks.pop(0)["heading"])
        if not str(title).strip() or str(title).strip() == "Agent Operational Report":
            title = heading
    if not subtitle and blocks and blocks[0].get("body"):
        lede = _inline(blocks[0]["body"][0])
        if 0 < len(lede) <= 160:
            subtitle = lede
            blocks.pop(0)
    return render_pdf_bytes(title, subtitle, telemetry, blocks)


def _jpeg_dimensions(data):
    import struct
    if not (isinstance(data, (bytes, bytearray)) and len(data) >= 4
            and data.startswith(b'\xff\xd8\xff') and data.endswith(b'\xff\xd9')):
        raise ValueError('JPEG has no supported frame header')
    pos = 2
    while pos + 4 <= len(data) - 2:
        if data[pos] != 255:
            break
        marker = data[pos + 1]
        length = struct.unpack('>H', data[pos + 2:pos + 4])[0]
        if length < 2 or pos + 2 + length > len(data) - 2:
            break
        if marker in (0xc0, 0xc1, 0xc2):
            if length < 8 or pos + 10 > len(data) - 2:
                break
            components = data[pos + 9]
            if components not in (1, 3, 4) or length != 8 + 3 * components:
                break
            height, width = struct.unpack('>HH', data[pos + 5:pos + 9])
            if width > 0 and height > 0:
                return width, height
            break
        pos += 2 + length
    raise ValueError('JPEG has no supported frame header')


def render_ebook_pdf_bytes(ebook: dict, mode: str = '8.5x11') -> bytes:
    """Independent illustrated layout; legacy report dimensions are never mutated."""
    import base64
    if mode not in {'8.5x11', '6x9', 'workbook'}:
        raise ValueError('invalid ebook PDF mode')
    width, height = (432, 648) if mode == '6x9' else (612, 792)
    pages = []
    page = None
    y = 0

    def new_page():
        nonlocal page, y
        number = len(pages) + 1
        left = (58 if number % 2 else 40) if mode == '6x9' else 48
        page = {'ops': [], 'links': [], 'images': [], 'left': left}
        pages.append(page)
        y = height - 48

    def paragraph(value, size=10, bold=False, url=None, color=INK, max_lines=None):
        nonlocal y
        lines = []
        for source in str(value).splitlines() or ['']:
            lines.extend(wrap(source, size, width - (98 if mode == '6x9' else 96), font='bold' if bold else 'body'))
        if max_lines is not None:
            lines = lines[:max_lines]
        for line in lines:
            if y < 65 + size:
                new_page()
            page['ops'].append(_text(page['left'], y, line, 'bold' if bold else 'body', size, color))
            if url and str(url).startswith(('https://', 'http://')):
                page['links'].append((page['left'], y-3, width-40, y+size, url))
            y -= size * 1.4
        y -= 7

    new_page()
    page['ops'] += [_rect(0, 0, width, height, NAVY), _rect(0, height*.22, width, 110, ACCENT),
                    _rect(18, 0, 10, height, NAVY_SOFT)]
    y = height - 75
    paragraph('APEX FIELD INTELLIGENCE PRESS', 10, True, color=PALE)
    paragraph(ebook['title'], 23 if mode == '6x9' else 28, True, color=WHITE, max_lines=5)
    paragraph(ebook['subtitle'], 11, color=WHITE, max_lines=3)
    paragraph('PRINTABLE WORKBOOK EDITION' if mode == 'workbook' else ebook['book_spec']['edition'], 12, True, color=PALE)
    for label, value in ebook['telemetry'].items():
        paragraph(f'{label.replace("_", " ").upper()}: {value}', 10, True, color=WHITE)
    new_page()
    paragraph('Table of Contents', 22, True)
    for chapter in ebook['chapters']:
        paragraph(chapter['title'], 12, True)
    paragraph('Source directory & publication notes', 12, True)
    paragraph(ebook['publication_notice'], 10)
    for chapter in ebook['chapters']:
        new_page()
        paragraph(chapter['title'], 17, True)
        for p in chapter['paragraphs']:
            paragraph(p)
        for section in chapter['sections']:
            paragraph(section['heading'], 12, True)
            for p in section['paragraphs']:
                paragraph(p)
            paragraph('Review video source', url=section['source_url'], color=ACCENT)
        for tip in chapter['pro_tips']:
            paragraph('ProTip: ' + str(tip.get('tip', '')), 10, True)
            paragraph(tip.get('timestamp', 'Source'), url=tip['timestamp_url'], color=ACCENT)
        for reference in chapter['statutes'] + chapter['portals']:
            paragraph(reference['name'] + ' | ' + reference['status'], 9,
                      url=reference.get('url') or reference['source_url'])
        for item in chapter['checklist']:
            paragraph('[ ] ' + item)
            if mode == 'workbook':
                paragraph('Finding: ________________________________________\nSource / date: ___________________________________\nNext action: _____________________________________', 10)
        for eid in chapter['exhibits']:
            exhibit = next(e for e in ebook['exhibits'] if e['exhibit_id'] == eid)
            new_page()
            paragraph(exhibit['figure_label'], 14, True)
            paragraph(exhibit['video_title'], 11)
            image_width = width - (98 if mode == '6x9' else 96)
            data = base64.b64decode(exhibit['jpeg_base64'])
            iw, ih = _jpeg_dimensions(data)
            image_height = min(200, image_width * ih / iw)
            image_width = image_height * iw / ih
            y -= image_height
            name = 'Im' + str(len(page['images']) + 1)
            page['images'].append((name, data, iw, ih))
            page['ops'].append(f'q {image_width:.2f} 0 0 {image_height:.2f} {page["left"]} {y:.2f} cm /{name} Do Q')
            y -= 20
            paragraph(exhibit['image_provenance'], 8)
            paragraph(exhibit['caption'], 9)
            paragraph(exhibit['timestamp'] + ' — watch source', 10, url=exhibit['url'], color=ACCENT)
            if y < 160:
                new_page()
            matrix = exhibit['qr_matrix']
            cell = 2.2
            x, bottom = page['left'], y - (len(matrix)+8)*cell
            page['ops'].append(_rect(x, bottom, (len(matrix)+8)*cell, (len(matrix)+8)*cell, WHITE))
            for row, values in enumerate(matrix):
                for col, value in enumerate(values):
                    if value:
                        page['ops'].append(_rect(x+(col+4)*cell, bottom+(len(matrix)-row+3)*cell, cell, cell, (0, 0, 0)))
            page['links'].append((x, bottom, x+(len(matrix)+8)*cell, y, exhibit['url']))
            y = bottom - 20
    new_page()
    paragraph('Source directory & publication notes', 17, True)
    paragraph(ebook['publication_notice'])
    for source in ebook['sources']:
        paragraph(source['title'] + ' — ' + source['author'], 11, True, source['url'])
        paragraph(source['url'], 8, url=source['url'])
    objects = [b'', b'']
    def add(data):
        objects.append(data.encode('latin-1', 'replace') if isinstance(data, str) else data)
        return len(objects)
    font1 = add('<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>')
    font2 = add('<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >>')
    kids = []
    for number, p in enumerate(pages, 1):
        p['ops'].append(_text(p['left'], 28, f'Page {number} of {len(pages)}', size=9, color=GREY))
        image_refs = []
        for name, data, iw, ih in p['images']:
            ref = add((f'<< /Type /XObject /Subtype /Image /Width {iw} /Height {ih} /ColorSpace /DeviceRGB /BitsPerComponent 8 /Filter /DCTDecode /Length {len(data)} >>\nstream\n').encode() + data + b'\nendstream')
            image_refs.append(f'/{name} {ref} 0 R')
        links = []
        for x1, y1, x2, y2, url in p['links']:
            ref = add(f'<< /Type /Annot /Subtype /Link /Rect [{x1} {y1} {x2} {y2}] /Border [0 0 0] /A << /Type /Action /S /URI /URI ({_esc(ascii_text(url))}) >> >>')
            links.append(f'{ref} 0 R')
        data = '\n'.join(p['ops']).encode('latin-1', 'replace')
        stream = add(f'<< /Length {len(data)} >>\nstream\n'.encode() + data + b'\nendstream')
        kids.append(add(f'<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {width} {height}] /Resources << /Font << /F1 {font1} 0 R /F2 {font2} 0 R >> /XObject << {" ".join(image_refs)} >> >> /Annots [{" ".join(links)}] /Contents {stream} 0 R >>'))
    objects[0] = b'<< /Type /Catalog /Pages 2 0 R >>'
    objects[1] = f'<< /Type /Pages /Count {len(kids)} /Kids [{" ".join(str(k)+" 0 R" for k in kids)}] >>'.encode()
    buffer = bytearray(b'%PDF-1.4\n%\xe2\xe3\xcf\xd3\n')
    offsets = [0]
    for i, obj in enumerate(objects, 1):
        offsets.append(len(buffer))
        buffer += f'{i} 0 obj\n'.encode() + obj + b'\nendobj\n'
    start = len(buffer)
    buffer += f'xref\n0 {len(objects)+1}\n0000000000 65535 f \n'.encode()
    for offset in offsets[1:]:
        buffer += f'{offset:010d} 00000 n \n'.encode()
    buffer += f'trailer\n<< /Size {len(objects)+1} /Root 1 0 R >>\nstartxref\n{start}\n%%EOF\n'.encode()
    return bytes(buffer)


if __name__ == "__main__":  # pragma: no cover - smoke check
    import sys
    sys.stdout.buffer.write(markdown_to_pdf_bytes("# Demo\n\n_Sample_\n\n- one\n- two\n"))
