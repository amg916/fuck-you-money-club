"""Structural publication gates; visual/press approval remains an owner gate."""
from __future__ import annotations

import io
from pathlib import Path
import re
import xml.etree.ElementTree as ET
import zipfile

from . import (
    MIN_EXPERT_YOUTUBE_LINKS_PER_BOOK,
    MIN_EXPERT_YOUTUBE_LINKS_PER_CHAPTER,
    parse_expert_youtube_deep_link,
)
from .design_concepts import CONCEPTS, render_scorecard_svg
from .diagrams_engine import render_all_diagrams_for_concept
from .cover_and_mockups import render_all_concept_mockups
from .interior_templates import INTERIOR_TEMPLATES, render_interior_page_html
from .exporters import render_fymc_pdf_bytes, render_fymc_epub_bytes, _svg_assets, _unpack_state


_FORBIDDEN = (chr(0x2122), chr(0x00AE), 'undefined', 'NaN', 'i.ytimg.com')


def _result(issues, **details):
    return {'passed': not issues, 'valid': not issues, 'issues': issues, **details}


_ALLOWED_SVG_TAGS = {
    'svg', 'g', 'defs', 'style', 'title', 'desc', 'metadata',
    'lineargradient', 'radialgradient', 'stop', 'clippath', 'mask', 'pattern',
    'filter', 'fegaussianblur', 'fedropshadow', 'feoffset', 'femerge', 'femergenode',
    'fecolormatrix', 'feblend', 'fecomposite', 'feflood',
    'rect', 'circle', 'ellipse', 'line', 'polyline', 'polygon', 'path',
    'text', 'tspan', 'use', 'symbol', 'marker',
}


def _unescape_css(value: str) -> str:
    prev = None
    while prev != value:
        prev = value
        value = re.sub(r'/\*.*?\*/', '', value, flags=re.S)
    value = re.sub(r'\\\r?\n', '', value)

    def _repl(match):
        hex_part = match.group(1)
        if hex_part:
            codepoint = int(hex_part, 16)
            return chr(codepoint) if 0 < codepoint <= 0x10FFFF else '\uFFFD'
        return match.group(2)

    un = re.sub(r'\\(?:([0-9a-fA-F]{1,6})\s?|(.))', _repl, value)
    prev = None
    while prev != un:
        prev = un
        un = re.sub(r'/\*.*?\*/', '', un, flags=re.S)
    return un


def _has_external_css_resource(value: str) -> bool:
    for candidate in (value, _unescape_css(value)):
        if re.search(r'@\s*(?:import|font-face|namespace|charset)', candidate, re.I):
            return True
        if re.search(r'(?:javascript|vbscript|data|file|http|https|ftp|ws|wss|blob|filesystem|about|chrome)\s*:', candidate, re.I):
            return True
        if re.search(r'(?:^|[\s(\'",:])//[^\s\'")]+', candidate):
            return True
        if re.search(r'(?:-[a-z]+-)?(?:image-set|cross-fade|image-rect|element|canvas)\s*\(', candidate, re.I):
            return True
        if re.search(r'(?:^|[^a-zA-Z0-9_-])(?:image|src|paint|expression|alpha-mask)\s*\(', candidate, re.I):
            return True
        if re.search(r'(?:-moz-binding|behavior)\s*:', candidate, re.I):
            return True
        total_urls = len(re.findall(r'url\s*\(', candidate, re.I))
        if total_urls:
            safe_urls = len(re.findall(r'url\s*\(\s*([\'"]?)#[^\s\'"()\\<>]+\1\s*\)', candidate, re.I))
            if safe_urls != total_urls:
                return True
    return False


def validate_svg_asset(svg_text: str, asset_name: str, check_cover_profanity: bool = False) -> dict:
    issues = []
    for token in _FORBIDDEN:
        if token in svg_text:
            issues.append(f'{asset_name}: prohibited token {ascii(token)}')
    if re.search(r'<\?\s*(?!xml(?:\s|\?>))', svg_text, re.I):
        issues.append(f'{asset_name}: prohibited XML processing instruction')
    if re.search(r'<!\s*(?:DOCTYPE|ENTITY)\b', svg_text, re.I):
        issues.append(f'{asset_name}: prohibited XML DTD/entity declaration')
    try:
        root = ET.fromstring(svg_text)
        if root.tag != '{http://www.w3.org/2000/svg}svg':
            issues.append(f'{asset_name}: missing SVG root/namespace')
        values = re.split(r'[\s,]+', root.get('viewBox', '').strip())
        try:
            numbers = [float(value) for value in values]
            if len(numbers) != 4 or any(n != n or abs(n) == float('inf') for n in numbers) or min(numbers[2:]) <= 0:
                raise ValueError('invalid geometry')
        except ValueError:
            issues.append(f'{asset_name}: invalid or missing viewBox')
        for node in root.iter():
            if not node.tag.startswith('{http://www.w3.org/2000/svg}'):
                issues.append(f'{asset_name}: non-SVG namespace element {node.tag}')
            tag = node.tag.rsplit('}', 1)[-1]
            tag_low = tag.lower()
            if tag_low not in _ALLOWED_SVG_TAGS:
                issues.append(f'{asset_name}: non-original or active SVG element {tag}')
            if tag_low == 'style' and len(node) > 0:
                issues.append(f'{asset_name}: child elements inside style')
            for name, value in node.attrib.items():
                local = name.rsplit('}', 1)[-1].split(':')[-1]
                local_low = local.lower()
                if local_low == 'base':
                    issues.append(f'{asset_name}: prohibited xml:base or base attribute')
                if _has_external_css_resource(value):
                    issues.append(f'{asset_name}: external CSS resource')
                if local_low in {'x', 'y', 'x1', 'y1', 'x2', 'y2', 'cx', 'cy', 'r', 'rx', 'ry', 'width', 'height', 'points', 'd'}:
                    if re.search(r'(?<![a-z])[-+]?(?:nan|inf(?:inity)?)(?![a-z])', value, re.I):
                        issues.append(f'{asset_name}: non-finite geometry {local}')
                if (
                    local_low.startswith('on')
                    or local_low in {'to', 'from', 'values', 'by', 'attributename', 'attributetype'}
                    or (local_low in {'href', 'src'} and not re.fullmatch(r'#[A-Za-z0-9_.\-:\u0080-\uFFFF]+', value.strip()))
                    or re.search(r'(?:javascript|vbscript|data|file)\s*:', value, re.I)
                ):
                    issues.append(f'{asset_name}: active or external SVG resource')
            for text_chunk in (node.text, node.tail, ''.join(node.itertext()) if tag_low == 'style' else None):
                if text_chunk and _has_external_css_resource(text_chunk):
                    issues.append(f'{asset_name}: external CSS resource')
    except (ET.ParseError, ValueError) as exc:
        issues.append(f'{asset_name}: malformed SVG: {exc}')
    if check_cover_profanity:
        if svg_text.upper().count('FUCK') > 1:
            issues.append(f'{asset_name}: more than one profanity occurrence')
        if 'THE BIG MONEY PLAYBOOKS' not in svg_text.upper():
            issues.append(f'{asset_name}: missing dominant series brand')
    return _result(issues, asset_name=asset_name)


def validate_pdf_bytes(pdf_bytes: bytes, expected_mode: str = 'digital_pdf') -> dict:
    issues = []
    if expected_mode not in {'digital_pdf', 'print_6x9_pdf', 'workbook_pdf'}:
        issues.append('Unknown PDF mode')
    if not pdf_bytes.startswith(b'%PDF-1.4'):
        issues.append('Missing PDF 1.4 header')
    if not pdf_bytes.rstrip().endswith(b'%%EOF'):
        issues.append('Missing PDF EOF marker')
    text = pdf_bytes.decode('latin-1')
    pages = re.findall(rb'\b\d+\s+0\s+obj\s*(<<\s*/Type\s*/Page\b.*?>>)\s*endobj', pdf_bytes, re.S)
    page_count = len(pages)
    minimum = 7 if expected_mode == 'workbook_pdf' else 16
    if page_count < minimum:
        issues.append(f'Expected at least {minimum} pages, found {page_count}')
    tree = re.search(rb'/Type\s*/Pages\s*/Count\s+(\d+)', pdf_bytes)
    if not tree or int(tree.group(1)) != page_count:
        issues.append('Page tree count does not match page objects')
    expected_box = [0, 0, 450, 666] if expected_mode == 'print_6x9_pdf' else [0, 0, 612, 792]
    for index, page in enumerate(pages, 1):
        for key, expected in [('MediaBox', expected_box)] + ([('TrimBox', [9, 9, 441, 657])] if expected_mode == 'print_6x9_pdf' else []):
            match = re.search(rb'/' + key.encode() + rb'\s*\[([^]]+)\]', page)
            try:
                actual = [float(v) for v in match.group(1).split()] if match else []
            except ValueError:
                actual = []
            if actual != expected:
                issues.append(f'Page {index}: incorrect /{key}')
        if f'Page {index} of {page_count}'.encode() not in pdf_bytes:
            issues.append(f'Page {index}: missing page-number footer')
    for symbol in (chr(0x2122), chr(0x00AE)):
        if symbol.encode('utf-8') in pdf_bytes or symbol.encode('utf-16-be') in pdf_bytes:
            issues.append('Prohibited symbol in PDF')
    if pdf_bytes.upper().count(b'FUCK') > 1:
        issues.append('PDF contains more than one profanity occurrence')
    start = re.search(rb'startxref\s+(\d+)\s+%%EOF\s*$', pdf_bytes)
    if not start or pdf_bytes[int(start.group(1)):int(start.group(1)) + 4] != b'xref':
        issues.append('Invalid cross-reference offset')
    else:
        offset = int(start.group(1))
        lines = pdf_bytes[offset:].splitlines()
        try:
            first, count = map(int, lines[1].split())
            if first != 0 or lines[2] != b'0000000000 65535 f ':
                raise ValueError('invalid free object')
            for obj in range(1, count):
                position = int(lines[obj + 2].split()[0])
                if not pdf_bytes[position:].startswith(f'{obj} 0 obj\n'.encode()):
                    raise ValueError(f'object {obj} offset mismatch')
        except (IndexError, ValueError) as exc:
            issues.append(f'Invalid cross-reference table: {exc}')
    yt_uris = set()
    obj_map = {
        int(m.group(1)): m.group(2)
        for m in re.finditer(rb'\b(\d+)\s+0\s+obj\s*(.*?)\s*endobj', pdf_bytes, re.S)
    }
    for page in pages:
        annots_m = re.search(rb'/Annots\s*\[([^\]]*)\]', page)
        if not annots_m:
            continue
        for ref_num in re.findall(rb'(\d+)\s+0\s+R\b', annots_m.group(1)):
            annot_obj = obj_map.get(int(ref_num), b'')
            if not (
                re.search(rb'/Type\s*/Annot\b', annot_obj)
                and re.search(rb'/Subtype\s*/Link\b', annot_obj)
            ):
                continue
            rect_m = re.search(rb'/Rect\s*\[([^\]]+)\]', annot_obj)
            if not rect_m:
                continue
            try:
                rx1, ry1, rx2, ry2 = [float(v) for v in rect_m.group(1).split()]
            except ValueError:
                continue
            if not (rx2 > rx1 and ry2 > ry1):
                continue
            uri_m = re.search(rb'/S\s*/URI\b[^>]*/URI\s*\(([^)]+)\)', annot_obj, re.S)
            if not uri_m:
                continue
            parsed_yt = parse_expert_youtube_deep_link(uri_m.group(1).decode('latin-1', 'ignore'))
            if parsed_yt is not None:
                yt_uris.add(parsed_yt)
    return _result(issues, page_count=page_count, expected_mode=expected_mode,
                   youtube_link_count=len(yt_uris),
                   validation_scope='Uncompressed PDF 1.4 preview structure; not a general PDF parser')


def _resolve(base, href):
    parts = base.split('/')[:-1]
    href = href.split('#', 1)[0]
    if not href:
        return base
    if href.startswith('/') or ':' in href or '\\' in href:
        raise ValueError('Absolute or external package reference')
    for part in href.split('/'):
        if part == '..':
            if not parts:
                raise ValueError('Package reference escapes archive')
            parts.pop()
        elif part not in {'', '.'}:
            parts.append(part)
    return '/'.join(parts)


def validate_epub_bytes(epub_bytes: bytes) -> dict:
    issues, xml_count = [], 0
    try:
        with zipfile.ZipFile(io.BytesIO(epub_bytes)) as archive:
            infos = archive.infolist()
            names = archive.namelist()
            if not infos or infos[0].filename != 'mimetype' or infos[0].compress_type != zipfile.ZIP_STORED:
                issues.append('mimetype must be the first entry and ZIP_STORED')
            if archive.read('mimetype') != b'application/epub+zip':
                issues.append('Invalid mimetype payload')
            if len(names) != len(set(names)):
                issues.append('Duplicate ZIP entries')
            required = {'META-INF/container.xml', 'OEBPS/content.opf', 'OEBPS/nav.xhtml', 'OEBPS/toc.ncx', 'OEBPS/styles.css',
                        'OEBPS/cover.xhtml', 'OEBPS/scorecard.xhtml', 'OEBPS/appendix.xhtml', 'OEBPS/images/cover.svg', 'OEBPS/images/scorecard.svg'}
            required.update(f'OEBPS/chapter_{n:02d}.xhtml' for n in range(1, 13))
            required.update(f'OEBPS/images/diag_{n:02d}.svg' for n in range(1, 9))
            issues.extend('Missing EPUB entry: ' + name for name in sorted(required - set(names)))
            roots = {}
            for name in names:
                if name.startswith('/') or '..' in name.split('/'):
                    issues.append('Unsafe archive path: ' + name)
                if name.lower().startswith('oebps/images/') and name.lower().endswith(('.jpg', '.jpeg')):
                    issues.append('Third-party raster image prohibited: ' + name)
                data = archive.read(name)
                if any(token.encode() in data for token in _FORBIDDEN):
                    issues.append('Prohibited content: ' + name)
                if name.endswith(('.xml', '.opf', '.ncx', '.xhtml', '.svg')):
                    try:
                        roots[name] = ET.fromstring(data)
                        xml_count += 1
                    except ET.ParseError as exc:
                        issues.append(f'{name}: invalid XML: {exc}')
                if name.endswith('.svg'):
                    issues.extend(validate_svg_asset(data.decode('utf-8'), name, name.endswith('/cover.svg'))['issues'])
            container = roots.get('META-INF/container.xml')
            if container is not None:
                locations = [n.get('full-path') for n in container.iter() if n.tag.endswith('}rootfile')]
                if 'OEBPS/content.opf' not in locations:
                    issues.append('Container does not resolve to the OPF')
            opf = roots.get('OEBPS/content.opf')
            ns = {'o': 'http://www.idpf.org/2007/opf'}
            if opf is not None:
                if opf.get('version') != '3.0':
                    issues.append('OPF must declare EPUB 3.0')
                items = opf.findall('o:manifest/o:item', ns)
                ids, hrefs = set(), set()
                nav_items = []
                for item in items:
                    item_id = item.get('id')
                    if not item_id or item_id in ids:
                        issues.append('Missing or duplicate manifest id')
                    ids.add(item_id)
                    target = _resolve('OEBPS/content.opf', item.get('href', ''))
                    hrefs.add(target)
                    if target not in names:
                        issues.append('Unresolved manifest href: ' + target)
                    if 'nav' in item.get('properties', '').split():
                        nav_items.append(target)
                if nav_items != ['OEBPS/nav.xhtml']:
                    issues.append('Manifest must identify exactly one navigation document')
                for ref in opf.findall('o:spine/o:itemref', ns):
                    if ref.get('idref') not in ids:
                        issues.append('Unresolved spine idref')
                for name in names:
                    if name.startswith('OEBPS/') and name != 'OEBPS/content.opf' and name not in hrefs:
                        issues.append('Resource absent from manifest: ' + name)
            yt_hrefs = set()
            for name, root in roots.items():
                if not name.endswith(('.xhtml', '.ncx')):
                    continue
                for node in root.iter():
                    for attr in ('src', 'href'):
                        target = node.get(attr)
                        if target and not re.match(r'^(?:https?:|mailto:)', target):
                            if _resolve(name, target) not in names:
                                issues.append(f'{name}: unresolved resource {target}')
                        elif (
                            attr == 'href'
                            and target
                            and name.endswith('.xhtml')
                            and node.tag.rsplit('}', 1)[-1] == 'a'
                            and ''.join(node.itertext()).strip()
                        ):
                            parsed_yt = parse_expert_youtube_deep_link(target)
                            if parsed_yt is not None:
                                yt_hrefs.add(parsed_yt)
    except (zipfile.BadZipFile, KeyError, ValueError, UnicodeError, RuntimeError, OSError) as exc:
        issues.append('EPUB validation failed: ' + str(exc))
        yt_hrefs = set()
    return _result(issues, checked_xml_count=xml_count,
                   youtube_link_count=len(yt_hrefs),
                   validation_scope='Structural checks only; external EPUBCheck and reader proofing still required')


def validate_manuscript_youtube_links(
    manuscript: dict,
    min_per_book: int = MIN_EXPERT_YOUTUBE_LINKS_PER_BOOK,
    min_per_chapter: int = MIN_EXPERT_YOUTUBE_LINKS_PER_CHAPTER,
) -> dict:
    """Validate that a book manuscript meets the expert YouTube deep-link floor."""
    issues: list[str] = []
    chapters = manuscript.get('chapters') if isinstance(manuscript, dict) else []
    if not isinstance(chapters, list) or len(chapters) != 12:
        issues.append(f'Expected 12 chapters for YouTube link floor check, got {len(chapters) if isinstance(chapters, list) else 0}')
        return _result(
            issues,
            min_required_per_book=min_per_book,
            min_required_per_chapter=min_per_chapter,
            total_links=0,
            unique_links=0,
            per_chapter_counts={},
        )

    unique_keys: set[tuple[str, int]] = set()
    total_valid_links = 0
    per_chapter_counts: dict[str, int] = {}

    for idx, ch in enumerate(chapters, start=1):
        ch_num = ch.get('chapter_number', idx) if isinstance(ch, dict) else idx
        cites = (ch.get('source_citations') or []) if isinstance(ch, dict) else []
        if not isinstance(cites, list):
            cites = []
        ch_valid = 0
        ch_seen: set[tuple[str, int]] = set()
        for cite in cites:
            if not isinstance(cite, dict):
                continue
            parsed = parse_expert_youtube_deep_link(cite.get('url'))
            if parsed is None:
                continue
            vid, t_val = parsed
            if cite.get('video_id') not in (None, '', vid):
                continue
            ts = cite.get('timestamp_seconds', cite.get('timestamp'))
            if ts is not None and (isinstance(ts, bool) or not isinstance(ts, int) or ts != t_val):
                continue
            if parsed not in ch_seen:
                ch_seen.add(parsed)
                ch_valid += 1
            unique_keys.add(parsed)
            total_valid_links += 1
        per_chapter_counts[f'Q{ch_num}'] = ch_valid
        if ch_valid < min_per_chapter:
            issues.append(
                f'Chapter Q{ch_num}: has {ch_valid} expert YouTube deep links, below minimum {min_per_chapter}'
            )

    unique_count = len(unique_keys)
    if unique_count < min_per_book:
        issues.append(
            f'Book total unique expert YouTube deep links is {unique_count}, below minimum floor of {min_per_book}'
        )

    return _result(
        issues,
        min_required_per_book=min_per_book,
        min_required_per_chapter=min_per_chapter,
        total_links=total_valid_links,
        unique_links=unique_count,
        per_chapter_counts=per_chapter_counts,
    )


def run_full_qa_suite(root_dir: Path, state: dict) -> dict:
    """Run in memory; do not overwrite previews while validating."""
    metadata, manuscript, workbook, diagrams, scorecard, approved = _unpack_state(state)
    issues, exports, svg_count, template_count = [], {}, 0, 0
    yt_report = validate_manuscript_youtube_links(manuscript)
    issues.extend(yt_report['issues'])
    concepts = ('concept_a', 'concept_b', 'concept_c')
    templates = list(INTERIOR_TEMPLATES) if isinstance(INTERIOR_TEMPLATES, dict) else [t.get('id', t.get('template_id')) if isinstance(t, dict) else t for t in INTERIOR_TEMPLATES]
    for concept_id in concepts:
        try:
            diagram_assets = _svg_assets(render_all_diagrams_for_concept(diagrams, concept_id))
            mockups = _svg_assets(render_all_concept_mockups(concept_id, metadata, scorecard))
            assets = {'scorecard': render_scorecard_svg(scorecard, concept_id)}
            assets.update({'diagram/' + k: v for k, v in diagram_assets.items()})
            assets.update({'mockup/' + k: v for k, v in mockups.items()})
            if len(assets) != 19:
                issues.append(f'{concept_id}: expected 19 SVGs, got {len(assets)}')
            for name, svg in assets.items():
                svg_count += 1
                issues.extend(validate_svg_asset(svg, concept_id + '/' + name,
                                                 check_cover_profanity=name.startswith('mockup/'))['issues'])
        except Exception as exc:
            issues.append(f'{concept_id}: SVG rendering failed: {type(exc).__name__}: {exc}')
        for template_id in templates:
            template_count += 1
            try:
                markup = render_interior_page_html(template_id, concept_id, manuscript, scorecard, diagrams)
                if not isinstance(markup, str) or not markup.strip():
                    raise ValueError('Empty HTML render')
                if not re.search(r'<(?:html|article|section|div)\b', markup, re.I):
                    raise ValueError('Missing HTML content root')
                if any(token in markup for token in _FORBIDDEN):
                    raise ValueError('Prohibited token in HTML')
                if re.search(r'<script\b|\bon\w+\s*=|javascript:', markup, re.I):
                    raise ValueError('Active content in interior template')
            except Exception as exc:
                issues.append(f'{concept_id}/{template_id}: template failed: {type(exc).__name__}: {exc}')
        exports[concept_id] = {}
        for mode in ('digital_pdf', 'print_6x9_pdf', 'workbook_pdf', 'epub'):
            try:
                report = validate_epub_bytes(render_fymc_epub_bytes(state, concept_id)) if mode == 'epub' else validate_pdf_bytes(render_fymc_pdf_bytes(state, concept_id, mode), mode)
                if report.get('youtube_link_count', 0) < MIN_EXPERT_YOUTUBE_LINKS_PER_BOOK:
                    report['issues'].append(
                        f'Exported clickable YouTube deep links ({report.get("youtube_link_count", 0)}) below minimum floor of {MIN_EXPERT_YOUTUBE_LINKS_PER_BOOK}'
                    )
                    report['passed'] = False
            except Exception as exc:
                report = _result([f'{type(exc).__name__}: {exc}'])
            exports[concept_id][mode] = report
            issues.extend(f'{concept_id}/{mode}: {issue}' for issue in report['issues'])
    if svg_count != 57:
        issues.append(f'Expected 57 SVG checks, completed {svg_count}')
    if template_count != 42:
        issues.append(f'Expected 42 template renders, attempted {template_count}')
    exports_yt_ok = all(
        r.get('youtube_link_count', 0) >= MIN_EXPERT_YOUTUBE_LINKS_PER_BOOK
        for modes in exports.values() for r in modes.values()
    )
    gates = {'svg_count': svg_count == 57, 'template_count': template_count == 42,
             'exports_pass': all(r['passed'] for modes in exports.values() for r in modes.values()),
             'youtube_links_floor': yt_report['passed'] and exports_yt_ok,
             'owner_design_approved': approved in concepts,
             'visual_proofing': 'not_performed', 'epubcheck': 'not_performed', 'press_preflight': 'not_performed'}
    return {'overall_pass': not issues, 'checked_svg_count': svg_count,
            'checked_template_renders': template_count, 'concept_exports': exports,
            'youtube_links_report': yt_report,
            'gates': gates, 'issues': issues, 'scope': 'automated preview QA, not release authorization'}
