"""Dependency-free, inspectable publishing previews; not production press proofs."""
from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import html
import io
import json
import os
from pathlib import Path
import re
import shutil
import tempfile
from uuid import uuid4
import xml.etree.ElementTree as ET
import zipfile

from . import PARENT_BRAND, BOOK_SERIES, BRAND_TAGLINE, RATING_SYSTEM_NAME
from .design_concepts import CONCEPTS, get_concept, render_scorecard_svg
from .diagrams_engine import render_all_diagrams_for_concept, render_diagram_svg
from .cover_and_mockups import render_all_concept_mockups, render_cover_or_mockup_svg
from .interior_templates import INTERIOR_TEMPLATES, render_interior_page_html
from .brand_and_catalog import (
    DEFAULT_DIAGRAM_IDS,
    _fsync_dir,
    _normalize_section,
    _recover_export_journals,
    _root_lock,
    _strip_xml_controls,
)


def _unpack_state(state: dict) -> tuple[dict, dict, dict, list[dict], dict, str | None]:
    """Normalize loaded publishing state and standalone preview state."""
    vol = state.get('volume') if isinstance(state.get('volume'), dict) else {}
    metadata = vol.get('metadata') or state.get('metadata') or {
        'volume_number': '001', 'title': 'HEIR HUNTING', 'subtitle': 'The Complete Playbook'}
    manuscript = vol.get('manuscript') or state.get('manuscript') or {}
    workbook = vol.get('workbook') or state.get('workbook') or {}
    scorecard = vol.get('scorecard') or state.get('scorecard') or {}
    raw_diags = vol.get('diagrams_data') if 'diagrams_data' in vol else state.get('diagrams_data', [])
    diagrams = raw_diags.get('diagrams', []) if isinstance(raw_diags, dict) else (list(raw_diags) if isinstance(raw_diags, list) else [])
    approved = None
    return metadata, manuscript, workbook, diagrams, scorecard, approved


def _ascii(value):
    replacements = {'‘': "'", '’': "'", '“': '"', '”': '"',
                    '–': '-', '—': ' - ', '…': '...', '•': '*',
                    ' ': ' ', chr(0x2122): '', chr(0x00AE): '', 'é': 'e',
                    'è': 'e', 'à': 'a', 'ö': 'o', 'ü': 'u',
                    'ñ': 'n', 'ç': 'c', 'ß': 'ss', '£': 'GBP '}
    text = _strip_xml_controls(str(value))
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text.encode('ascii', 'replace').decode('ascii')


def _text(value):
    if value is None:
        return ''
    if isinstance(value, dict):
        return '\n'.join(str(k).replace('_', ' ').title() + ': ' + _text(v) for k, v in value.items())
    if isinstance(value, (list, tuple)):
        return '\n'.join(_text(v) for v in value)
    return str(value)


# Adobe AFM advances for ASCII 32..126, in thousandths of an em.
_AFM = {
    'Helvetica': '278 278 355 556 556 889 667 191 333 333 389 584 278 333 278 278 556 556 556 556 556 556 556 556 556 556 278 278 584 584 584 556 1015 667 667 722 722 667 611 778 722 278 500 667 556 833 722 778 667 778 722 667 611 722 667 944 667 667 611 278 278 278 469 556 333 556 556 500 556 556 278 556 556 222 222 500 222 833 556 556 556 556 333 500 278 556 500 722 500 500 500 334 260 334 584',
    'Helvetica-Bold': '278 333 474 556 556 889 722 238 333 333 389 584 278 333 278 278 556 556 556 556 556 556 556 556 556 556 333 333 584 584 584 611 975 722 722 722 722 667 611 778 722 278 556 722 611 833 722 778 667 778 722 667 611 722 667 944 667 667 611 333 278 333 584 556 333 556 611 556 611 556 333 611 611 278 278 556 278 889 611 611 611 611 389 556 333 611 556 778 556 556 500 389 280 389 584',
    'Times-Roman': '250 333 408 500 500 833 778 180 333 333 500 564 250 333 250 278 500 500 500 500 500 500 500 500 500 500 278 278 564 564 564 444 921 722 667 667 722 611 556 722 722 333 389 722 611 889 722 722 556 722 667 556 611 722 722 944 722 722 611 333 278 333 469 500 333 444 500 444 500 444 333 500 500 278 278 500 278 778 500 500 500 500 333 389 278 500 500 722 500 500 444 480 200 480 541',
    'Times-Bold': '250 333 555 500 500 1000 833 278 333 333 500 570 250 333 250 278 500 500 500 500 500 500 500 500 500 500 333 333 570 570 570 500 930 722 667 722 722 667 611 778 778 389 500 778 667 944 722 778 611 778 722 556 667 722 722 1000 722 722 667 333 278 333 581 500 333 500 556 444 556 444 333 500 556 278 333 556 278 833 556 500 556 556 444 389 333 556 500 722 500 500 444 394 220 394 520',
}
_AFM = {k: tuple(map(int, v.split())) for k, v in _AFM.items()}


def _width(text, font, size):
    return sum(600 if font.startswith('Courier') else _AFM[font][ord(c) - 32]
               for c in _ascii(text) if 32 <= ord(c) <= 126) * size / 1000


def _wrap_with_links(text, font, size, width):
    width = max(float(width), 1e-4)
    rows = []
    for paragraph in _ascii(text).splitlines() or ['']:
        line = ''
        line_links = []
        for raw_word in paragraph.split():
            word_urls = []
            for m in re.finditer(r'https?://[^\s()<>]+', raw_word, re.IGNORECASE):
                uri = m.group(0).rstrip('.,;]')
                if uri:
                    word_urls.append((m.start(), m.start() + len(uri), uri))
            word = raw_word
            offset = 0
            if line and _width(line + ' ' + word, font, size) > width:
                rows.append((line, line_links))
                line, line_links = '', []
            while word and _width(word, font, size) > width:
                cut = 1
                while cut < len(word) and _width(word[:cut + 1], font, size) <= width:
                    cut += 1
                if line:
                    rows.append((line, line_links))
                    line, line_links = '', []
                frag = word[:cut]
                frag_links = []
                for u_start, u_end, uri in word_urls:
                    ov_s = max(offset, u_start)
                    ov_e = min(offset + cut, u_end)
                    if ov_e > ov_s:
                        frag_links.append((ov_s - offset, ov_e - offset, uri))
                rows.append((frag, frag_links))
                word = word[cut:]
                offset += cut
            if word:
                prefix_len = (len(line) + 1) if line else 0
                line = (line + ' ' + word) if line else word
                for u_start, u_end, uri in word_urls:
                    ov_s = max(offset, u_start)
                    ov_e = min(offset + len(word), u_end)
                    if ov_e > ov_s:
                        line_links.append((prefix_len + (ov_s - offset), prefix_len + (ov_e - offset), uri))
        rows.append((line, line_links))
    return rows


def _wrap(text, font, size, width):
    return [line for line, _ in _wrap_with_links(text, font, size, width)]


def _aligned_row_cells(row, headers, keys=None):
    if not isinstance(row, dict):
        return list(row) if isinstance(row, (list, tuple)) else [row]
    columns = keys or headers
    if not columns:
        return list(row.values())
    lower = {str(key).lower(): key for key in row}
    normalized = {re.sub(r'[^a-z0-9]+', '_', str(key).lower()).strip('_'): key for key in row}
    cells, matched = [], False
    for column in columns:
        name = str(column)
        key = column if column in row else lower.get(name.lower())
        if key is None:
            key = normalized.get(re.sub(r'[^a-z0-9]+', '_', name.lower()).strip('_'))
        matched = matched or key is not None
        cells.append(row[key] if key is not None else '')
    return cells if matched else list(row.values())


class _PDF:
    def __init__(self, concept_id, mode):
        get_concept(concept_id)
        self.print_mode = mode == 'print_6x9_pdf'
        self.w, self.h = (450, 666) if self.print_mode else (612, 792)
        self.fonts = {'concept_a': ('Times-Bold', 'Times-Roman', 'Courier'),
                      'concept_b': ('Helvetica-Bold', 'Helvetica', 'Courier-Bold'),
                      'concept_c': ('Times-Bold', 'Times-Roman', 'Helvetica')}[concept_id]
        self.accent = {'concept_a': '.18 .27 .22', 'concept_b': '.13 .25 .40',
                       'concept_c': '.40 .22 .17'}[concept_id]
        self.pages, self.annots, self.toc = [], [], []

    def new(self, title=''):
        self.pages.append([])
        self.annots.append([])
        self.left = (63 if len(self.pages) % 2 else 45) if self.print_mode else 54
        self.right = (45 if len(self.pages) % 2 else 63) if self.print_mode else 54
        self.usable = self.w - self.left - self.right
        self.y = self.h - 76
        self.title = title
        if len(self.pages) > 1:
            self.draw(str(BOOK_SERIES), self.left, self.h - 37, 8, 2)
            self.line(self.left, self.h - 45, self.w - self.right, self.h - 45)

    def emit(self, command):
        self.pages[-1].append(command)

    def draw(self, text, x, y, size=10, font=1):
        safe = ''.join(c for c in _ascii(text) if 32 <= ord(c) <= 126)
        safe = safe.replace('\\', '\\\\').replace('(', '\\(').replace(')', '\\)')
        size_tok = f'{size:.4f}'.rstrip('0').rstrip('.') if isinstance(size, float) else str(size)
        self.emit(f'BT /F{font} {size_tok} Tf 1 0 0 1 {x:.2f} {y:.2f} Tm ({safe}) Tj ET')

    def line(self, x, y, x2, y2):
        self.emit(f'0.6 w {x:.2f} {y:.2f} m {x2:.2f} {y2:.2f} l S')

    def box(self, x, y, w, h, fill=False):
        self.emit(f'q {self.accent if fill else "0 0 0"} {"rg" if fill else "RG"} '
                  f'{x:.2f} {y:.2f} {w:.2f} {h:.2f} re {"f" if fill else "S"} Q')

    def need(self, height):
        if self.y - height < 54:
            self.new(self.title)

    def paragraph(self, value, size=10.5, font=1, boxed=False):
        raw_text = _text(value)
        for line, line_links in _wrap_with_links(raw_text, self.fonts[font], size, self.usable - (16 if boxed else 0)):
            self.need(size * 1.45)
            text_x = self.left + (8 if boxed else 0)
            if boxed:
                self.box(self.left, self.y - 4, self.usable, size * 1.45)
            self.draw(line, text_x, self.y, size, font)
            if self.annots and line_links:
                for s_idx, e_idx, uri in line_links:
                    x1 = text_x + _width(line[:s_idx], self.fonts[font], size)
                    x2 = max(x1 + 4.0, text_x + _width(line[:e_idx], self.fonts[font], size))
                    self.annots[-1].append((x1, self.y - 2, x2, self.y + size, uri))
            self.y -= size * 1.45
        self.y -= 7

    def heading(self, title):
        self.need(45)
        self.paragraph(title, 17, 0)

    def table(self, value):
        if not isinstance(value, dict):
            self.paragraph(value, boxed=True)
            return
        caption = value.get('caption') if value.get('caption') not in (None, '') else value.get('title')
        if caption not in (None, ''):
            self.paragraph(_text(caption), 10, 0)
        rows = list(value.get('rows', []))
        headers = value.get('headers') or value.get('columns') or value.get('header') or []
        if not headers:
            dict_keys = []
            for r in rows:
                if isinstance(r, dict):
                    for k in r:
                        if k not in dict_keys:
                            dict_keys.append(k)
            if dict_keys:
                headers = [str(k) for k in dict_keys]
        if headers:
            rows = [headers] + rows
        for row in rows:
            cells = _aligned_row_cells(row, headers, value.get('keys'))
            cw = self.usable / max(1, len(cells))
            pad = min(6.0, cw * 0.12)
            inner_w = max(1e-4, cw - 2.0 * pad)
            cell_size = 9 if inner_w >= 9.0 * 1.02 else max(1e-4, int((inner_w / 1.03) * 10000) / 10000)
            wrapped = [_wrap(_text(c), self.fonts[1], cell_size, inner_w) for c in cells]
            for index in range(max((len(c) for c in wrapped), default=0)):
                self.need(16)
                for col, lines in enumerate(wrapped):
                    self.box(self.left + col * cw, self.y - 5, cw, 16)
                    self.draw(lines[index] if index < len(lines) else '', self.left + col * cw + pad, self.y, cell_size)
                self.y -= 16
        self.y -= 8

    def finish(self):
        total = len(self.pages)
        for number in range(total):
            label = f'Page {number + 1} of {total}'
            x = (self.w - _width(label, self.fonts[2], 8)) / 2
            self.pages[number].append(f'BT /F2 8 Tf {x:.2f} 30 Td ({label}) Tj ET')
        objects = [b'<< /Type /Catalog /Pages 2 0 R >>', b'']
        objects += [f'<< /Type /Font /Subtype /Type1 /BaseFont /{f} /Encoding /WinAnsiEncoding >>'.encode() for f in self.fonts]
        kids = []
        for page_idx, commands in enumerate(self.pages):
            page_annots = self.annots[page_idx] if page_idx < len(self.annots) else []
            annot_refs = []
            for x1, y1, x2, y2, uri in page_annots:
                safe_uri = ''.join(c for c in _ascii(uri) if 32 <= ord(c) <= 126)
                safe_uri = safe_uri.replace('\\', '\\\\').replace('(', '\\(').replace(')', '\\)')
                annot_id = len(objects) + 1
                annot_refs.append(f'{annot_id} 0 R')
                objects.append(
                    f'<< /Type /Annot /Subtype /Link /Rect [{x1:.2f} {y1:.2f} {x2:.2f} {y2:.2f}] '
                    f'/Border [0 0 0] /A << /S /URI /URI ({safe_uri}) >> >>'.encode()
                )
            page_id = len(objects) + 1
            kids.append(f'{page_id} 0 R')
            trim = ' /TrimBox [9 9 441 657]' if self.print_mode else ''
            annots_clause = f' /Annots [{" ".join(annot_refs)}]' if annot_refs else ''
            objects.append((f'<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {self.w} {self.h}]'
                            f'{trim}{annots_clause} /Resources << /Font << /F0 3 0 R /F1 4 0 R /F2 5 0 R >> >> '
                            f'/Contents {page_id + 1} 0 R >>').encode())
            stream = '\n'.join(commands).encode('ascii')
            objects.append(f'<< /Length {len(stream)} >>\nstream\n'.encode() + stream + b'\nendstream')
        objects[1] = f'<< /Type /Pages /Count {total} /Kids [{" ".join(kids)}] >>'.encode()
        out, offsets = bytearray(b'%PDF-1.4\n%\xe2\xe3\xcf\xd3\n'), [0]
        for index, obj in enumerate(objects, 1):
            offsets.append(len(out))
            out.extend(f'{index} 0 obj\n'.encode() + obj + b'\nendobj\n')
        start = len(out)
        out.extend(f'xref\n0 {len(offsets)}\n0000000000 65535 f \n'.encode())
        for offset in offsets[1:]:
            out.extend(f'{offset:010d} 00000 n \n'.encode())
        out.extend(f'trailer\n<< /Size {len(offsets)} /Root 1 0 R >>\nstartxref\n{start}\n%%EOF\n'.encode())
        return bytes(out)


def _records(state, group, key, count):
    records = state.get(group, {}).get(key, [])
    records = list(records.values()) if isinstance(records, dict) else list(records)
    if len(records) != count:
        raise ValueError(f'{group}.{key} must contain exactly {count} records')
    return [r if isinstance(r, dict) else {'body': r} for r in records]


def render_fymc_pdf_bytes(state: dict, concept_id: str = 'concept_a', fmt: str = 'digital_pdf') -> bytes:
    if fmt not in {'digital_pdf', 'print_6x9_pdf', 'workbook_pdf'}:
        raise ValueError('Unsupported PDF format: ' + fmt)
    metadata, manuscript, workbook_data, diagrams, scorecard, approved = _unpack_state(state)
    workbook = fmt == 'workbook_pdf'
    records = _records({'manuscript': manuscript, 'workbook': workbook_data},
                       'workbook' if workbook else 'manuscript',
                       'worksheets' if workbook else 'chapters', 6 if workbook else 12)
    pdf = _PDF(concept_id, fmt)
    pdf.new('Cover')
    pdf.box(pdf.left, 130, pdf.usable, 160, True)
    for n in range(6):
        x = pdf.left + 15 + n * (pdf.usable - 30) / 6
        pdf.emit('q 1 1 1 RG')
        pdf.line(x, 145, x, 155 + n * 21)
        pdf.emit('Q')
    pdf.paragraph(BOOK_SERIES, 30, 0)
    pdf.paragraph(metadata.get('title', 'HEIR HUNTING'), 23, 0)
    pdf.paragraph('VOLUME ' + str(metadata.get('volume_number', '001')), 12, 2)
    pdf.paragraph('OPERATOR WORKBOOK' if workbook else metadata.get('subtitle', 'The Complete Playbook'), 12)
    pdf.draw('THE FUCK YOU MONEY CLUB', pdf.left, 85, 8, 2)
    if not workbook:
        pdf.new('Title / Contents')
        pdf.heading(f"{metadata.get('title', 'HEIR HUNTING')} - VOLUME {metadata.get('volume_number', '001')}")
        if approved is None:
            pdf.paragraph('CONCEPT PREVIEW EDITION - AWAITING OWNER DESIGN APPROVAL', 10, 2, True)
        toc_page = len(pdf.pages) - 1
        pdf.new('Scorecard')
        pdf.heading('Money-to-Manpower Scorecard')
        pdf.paragraph(RATING_SYSTEM_NAME, 11, 2)
        scores = scorecard.get('scores')
        metrics = scores or scorecard.get('metrics', {})
        factors = [('Revenue potential', 25), ('Profit margin potential', 25),
                   ('Team efficiency', 20), ('Startup accessibility', 15),
                   ('Automation potential', 15)] if scores else [
                       (label, 100) for label in ['Capital efficiency', 'Operator workload',
                                                'Speed to cash', 'Scalability', 'Risk control']]
        for label, maximum in factors:
            raw = metrics.get(label, metrics.get(label.lower().replace(' ', '_'))) if isinstance(metrics, dict) else None
            assessed = isinstance(raw, (int, float)) and raw == raw and abs(raw) != float('inf')
            val = max(0, min(maximum, float(raw))) if assessed else 0
            pdf.paragraph(label + (f' - {val:g}/{maximum}' if assessed else ' - not assessed'))
            pdf.box(pdf.left, pdf.y - 14, pdf.usable, 12)
            pdf.box(pdf.left, pdf.y - 14, pdf.usable * val / maximum, 12, True)
            pdf.y -= 35
        pdf.heading('Three operating scenarios')
        pdf.paragraph(scorecard.get('scenarios', ['Solo operator: validate one lead before scaling.', 'Small team: separate research and outreach.', 'Scaled operation: audit quality and cash conversion.']) if isinstance(scorecard, dict) else '')
    for index, record in enumerate(records, 1):
        title = str(record.get('title', record.get('name', f'{"Worksheet" if workbook else "Chapter"} {index}')))
        pdf.new(title)
        pdf.toc.append((title, len(pdf.pages)))
        pdf.heading(f'{index:02d} / {title}')
        pdf.paragraph(record.get('executive_summary', record.get('summary', 'Executive summary not supplied.')), boxed=True)
        for key, value in record.items():
            if key in {'title', 'name', 'executive_summary', 'summary', 'action_checklist', 'checklist',
                       'source_citations', 'statutory_citations', 'citations', 'sources', 'diagram', 'diagram_id'}:
                continue
            pdf.heading(key.replace('_', ' ').title())
            if key == 'sections':
                for section in value:
                    section = _normalize_section(section)
                    if not isinstance(section, dict):
                        pdf.paragraph(section)
                        continue
                    for field, content in section.items():
                        if field == 'tables':
                            for table in content:
                                pdf.table(table)
                        elif field == 'bullets':
                            for bullet in (content if isinstance(content, list) else [content]):
                                pdf.paragraph('* ' + _text(bullet))
                        else:
                            pdf.paragraph(content)
            elif key in ('tables', 'table'):
                for table in value if isinstance(value, list) else [value]:
                    pdf.table(table)
            else:
                pdf.paragraph(value)
        pdf.heading('Operator checklist')
        for item in record.get('action_checklist') or record.get('checklist') or ['Review assumptions', 'Record next action']:
            pdf.paragraph('[ ] ' + _text(item))
        if workbook:
            pdf.heading('Write-in workspace')
            pdf.need(150)
            pdf.box(pdf.left, pdf.y - 140, pdf.usable, 140)
            for offset in range(20, 140, 20):
                pdf.line(pdf.left + 8, pdf.y - offset, pdf.w - pdf.right - 8, pdf.y - offset)
            pdf.y -= 155
        else:
            pdf.heading('Exhibit - operating sequence')
            pdf.paragraph(record.get('diagram', record.get('diagram_id', 'Chapter workflow')), boxed=True)
            diagram_id = record.get('diagram_id')
            diagram = next((d for d in diagrams if diagram_id is not None
                            and diagram_id in (d.get('diagram_id'), d.get('id'))), {})
            stages = (diagram.get('stages') or [
                {'label': label, 'value': ''} for label in ['RESEARCH', 'VERIFY', 'ACT']])[:5]
            cell_width = pdf.usable / len(stages)
            labels = [_wrap(_text(stage.get('label', '')), pdf.fonts[2], 8, cell_width - 18)
                      + _wrap(_text(stage.get('value', '')), pdf.fonts[2], 8, cell_width - 18)
                      for stage in stages]
            height = max(32, max(len(lines) for lines in labels) * 11 + 12)
            pdf.need(height + 20)
            for step, lines in enumerate(labels):
                x = pdf.left + step * cell_width
                pdf.box(x, pdf.y - height, cell_width - 8, height)
                for line_index, line in enumerate(lines):
                    pdf.draw(line, x + 5, pdf.y - 14 - line_index * 11, 8, 2)
                if step < len(stages) - 1:
                    pdf.line(x + cell_width - 8, pdf.y - height / 2,
                             x + cell_width, pdf.y - height / 2)
            pdf.y -= height + 20
        combined_citations = []
        for ckey in ('statutory_citations', 'source_citations', 'citations', 'sources'):
            cval = record.get(ckey)
            if cval:
                combined_citations.extend(cval if isinstance(cval, (list, tuple)) else [cval])
        pdf.paragraph('Statutory & source citations', 10, 0)
        pdf.paragraph(combined_citations or 'No source timestamps supplied; verify before publication.', 9)
    if workbook and isinstance(manuscript.get('chapters'), list) and manuscript['chapters']:
        pdf.new('Expert YouTube Reference Index')
        pdf.heading('Expert YouTube Deep-Link Reference Index')
        for ch_idx, ch in enumerate(manuscript['chapters'], 1):
            if isinstance(ch, dict) and ch.get('source_citations'):
                pdf.paragraph(f"Chapter {ch_idx:02d}: {ch.get('title', '')}", 10, 0)
                pdf.paragraph(ch.get('source_citations'), 8.5)
    if not workbook:
        pdf.new('Appendix')
        pdf.heading('Appendix / source and operating notes')
        pdf.paragraph(manuscript.get('appendix', state.get('sources', 'Owner review required before publication.')))
        # Fill the reserved TOC without creating pages or changing chapter numbers.
        saved_pages = pdf.pages
        pdf.pages = [saved_pages[toc_page]]
        toc_left = 45 if pdf.print_mode else 54
        toc_width = pdf.w - (108 if pdf.print_mode else 108)
        size = 10.0
        while True:
            lines = [line for title, page in pdf.toc
                     for line in _wrap(f'{page:02d}  {title}', pdf.fonts[1], size, toc_width)]
            if len(lines) * size * 1.5 <= pdf.h - 250:
                break
            size *= 0.9
        y = pdf.h - 195
        for line in lines:
            pdf.draw(line, toc_left, y, size)
            y -= size * 1.5
        pdf.pages = saved_pages
    return pdf.finish()


def _svg_assets(rendered):
    """Normalize named SVG collections without importing sibling internals."""
    if isinstance(rendered, dict):
        result = {}
        for name, value in rendered.items():
            if isinstance(value, str) and '<svg' in value:
                result[str(name)] = value
            elif isinstance(value, dict) and isinstance(value.get('svg'), str):
                result[str(name)] = value['svg']
        return result
    result = {}
    for index, value in enumerate(rendered):
        if isinstance(value, str):
            result[str(index + 1)] = value
        elif isinstance(value, dict) and isinstance(value.get('svg'), str):
            result[str(value.get('id', value.get('name', index + 1)))] = value['svg']
    return result


def _original_svg(svg):
    root = ET.fromstring(svg)
    if root.tag != '{http://www.w3.org/2000/svg}svg' or not root.get('viewBox'):
        raise ValueError('SVG requires an SVG namespace and viewBox')
    if any(token in svg for token in (chr(0x2122), chr(0x00AE), 'i.ytimg.com', 'undefined', 'NaN')):
        raise ValueError('Invalid or prohibited SVG content')
    for node in root.iter():
        if node.tag.rsplit('}', 1)[-1] in {'image', 'script', 'foreignObject'}:
            raise ValueError('Only original static vector artwork is allowed')
        for name, value in node.attrib.items():
            if name.rsplit('}', 1)[-1] == 'href' and not value.startswith('#'):
                raise ValueError('External SVG resources are not allowed')
    return svg


def _epub_art(state, concept_id):
    metadata, manuscript, workbook, diagrams, scorecard, approved = _unpack_state(state)
    diagram_assets = _svg_assets(render_all_diagrams_for_concept(diagrams, concept_id))
    mockups = _svg_assets(render_all_concept_mockups(concept_id, metadata, scorecard))
    if len(diagram_assets) != 8:
        raise ValueError('Expected eight original concept diagrams')
    cover_keys = [key for key in mockups if 'cover' in key.lower() and 'back' not in key.lower()]
    if not cover_keys:
        raise ValueError('Concept mockups must include a named cover SVG')
    cover_keys.sort(key=lambda key: ('front' not in key.lower(), len(key), key))
    art = {'cover.svg': mockups[cover_keys[0]], 'scorecard.svg': render_scorecard_svg(scorecard, concept_id)}
    for index, (_, svg) in enumerate(sorted(diagram_assets.items()), 1):
        art[f'diag_{index:02d}.svg'] = svg
    return {name: _original_svg(svg) for name, svg in art.items()}


def _escape(value):
    value = _strip_xml_controls(str(value))
    return html.escape(value.replace(chr(0x2122), '').replace(chr(0x00AE), ''), quote=True)


def _xhtml(title, body):
    return ('<?xml version="1.0" encoding="utf-8"?>\n'
            '<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="en" xml:lang="en">'
            '<head><title>' + _escape(title) + '</title><link rel="stylesheet" type="text/css" href="styles.css"/></head>'
            '<body>' + body + '</body></html>')


def _markup(value):
    if isinstance(value, dict):
        if 'rows' in value:
            caption_raw = value.get('caption') if value.get('caption') not in (None, '') else value.get('title')
            cap = '<caption>' + _escape(caption_raw) + '</caption>' if caption_raw not in (None, '') else ''
            raw_rows = list(value['rows'])
            headers = value.get('headers') or value.get('columns') or value.get('header') or []
            if not headers:
                dict_keys = []
                for r in raw_rows:
                    if isinstance(r, dict):
                        for k in r:
                            if k not in dict_keys:
                                dict_keys.append(k)
                if dict_keys:
                    headers = [str(k) for k in dict_keys]
            head = '<thead><tr>' + ''.join('<th scope="col">' + _escape(c) + '</th>' for c in headers) + '</tr></thead>' if headers else ''
            rows = []
            for row in raw_rows:
                cells = _aligned_row_cells(row, headers, value.get('keys'))
                rows.append('<tr>' + ''.join('<td>' + _markup(c) + '</td>' for c in cells) + '</tr>')
            return '<table>' + cap + head + '<tbody>' + ''.join(rows) + '</tbody></table>'
        return '<dl>' + ''.join('<dt>' + _escape(str(k).replace('_', ' ').title()) + '</dt><dd>' + _markup(v) + '</dd>' for k, v in value.items()) + '</dl>'
    if isinstance(value, (list, tuple)):
        return '<ul>' + ''.join('<li>' + _markup(item) + '</li>' for item in value) + '</ul>'
    if value is None:
        return ''
    out_lines = []
    for line in str(value).splitlines():
        stripped = line.strip()
        if re.fullmatch(r'https?://[^\s<>"\']+', stripped, re.IGNORECASE):
            esc_url = _escape(stripped)
            out_lines.append('<p><a href="' + esc_url + '">' + esc_url + '</a></p>')
        else:
            out_lines.append('<p>' + _escape(line) + '</p>')
    return ''.join(out_lines)


def render_fymc_epub_bytes(state: dict, concept_id: str = 'concept_a', _art=None) -> bytes:
    get_concept(concept_id)
    metadata, manuscript, workbook, diagrams, scorecard, approved = _unpack_state(state)
    chapters = _records({'manuscript': manuscript}, 'manuscript', 'chapters', 12)
    art = _epub_art(state, concept_id) if _art is None else _art
    diagram_keys = sorted(str(diagram.get('id', diagram.get('diagram_id', f'diagram_{i + 1:02d}')))
                          for i, diagram in enumerate(diagrams))
    diagram_map: dict[str, int] = {}
    for i, key in enumerate(diagram_keys, 1):
        diagram_map[key] = i
        diagram_map[DEFAULT_DIAGRAM_IDS[i - 1]] = i
        for prefix in ('diag', 'diagram'):
            for separator in ('_', '-'):
                diagram_map[f'{prefix}{separator}{i:02d}'] = i
                diagram_map[f'{prefix}{separator}{i}'] = i
    title = f"{BOOK_SERIES}: {metadata.get('title', 'HEIR HUNTING')}, Volume {metadata.get('volume_number', '001')}"
    digest = hashlib.sha256(json.dumps(state, sort_keys=True, default=str).encode()).hexdigest()
    identifier = 'urn:sha256:' + hashlib.sha256((concept_id + digest).encode()).hexdigest()
    pages = [('cover.xhtml', 'Cover', '<h1>' + _escape(title) + '</h1><img src="images/cover.svg" alt="Original concept cover"/>')]
    if approved is None:
        pages[0] = (pages[0][0], pages[0][1], pages[0][2] + '<p>CONCEPT PREVIEW EDITION - AWAITING OWNER DESIGN APPROVAL</p>')
    pages.append(('scorecard.xhtml', 'Money-to-Manpower Scorecard', '<h1>Money-to-Manpower Scorecard</h1><img src="images/scorecard.svg" alt="Five-factor Money-to-Manpower Scorecard and three operating scenarios"/>' + _markup(scorecard)))
    for index, chapter in enumerate(chapters, 1):
        heading = str(chapter.get('title', f'Chapter {index}'))
        body = '<h1>' + _escape(heading) + '</h1>'
        for key, value in chapter.items():
            if key not in {'title', 'diagram_id'}:
                if key == 'sections' and isinstance(value, list):
                    value = [_normalize_section(section) for section in value]
                body += '<section><h2>' + _escape(key.replace('_', ' ').title()) + '</h2>' + _markup(value) + '</section>'
        raw_diagram = chapter.get('diagram_id')
        if raw_diagram is None or raw_diagram == '':
            number = (index - 1) % 8 + 1
        else:
            number = diagram_map.get(str(raw_diagram), 0)
        if not 1 <= number <= 8:
            raise ValueError('Chapter diagram reference must identify diagram 01 through 08')
        body += f'<figure><img src="images/diag_{number:02d}.svg" alt="Chapter {index} operating diagram"/><figcaption>Exhibit {index}: operating diagram</figcaption></figure>'
        pages.append((f'chapter_{index:02d}.xhtml', heading, body))
    appendix = manuscript.get('appendix', state.get('sources', 'Review all sources before publication.'))
    pages.append(('appendix.xhtml', 'Appendix', '<h1>Appendix</h1>' + _markup(appendix)))
    links = ''.join('<li><a href="' + name + '">' + _escape(label) + '</a></li>' for name, label, _ in pages)
    nav = _xhtml('Contents', '<nav epub:type="toc" id="toc"><h1>Contents</h1><ol>' + links + '</ol></nav>')
    ncx = ('<?xml version="1.0" encoding="utf-8"?><ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1" xml:lang="en">'
           '<head><meta name="dtb:uid" content="' + identifier + '"/><meta name="dtb:depth" content="1"/><meta name="dtb:totalPageCount" content="0"/><meta name="dtb:maxPageNumber" content="0"/></head><docTitle><text>' + _escape(title) + '</text></docTitle><navMap>')
    for index, (name, label, _) in enumerate(pages, 1):
        ncx += f'<navPoint id="n{index}" playOrder="{index}"><navLabel><text>{_escape(label)}</text></navLabel><content src="{name}"/></navPoint>'
    ncx += '</navMap></ncx>'
    manifest = '<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/><item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/><item id="css" href="styles.css" media-type="text/css"/>'
    spine = ''
    for index, (name, _, _) in enumerate(pages):
        manifest += f'<item id="p{index}" href="{name}" media-type="application/xhtml+xml"/>'
        spine += f'<itemref idref="p{index}"/>'
    for index, name in enumerate(art):
        prop = ' properties="cover-image"' if name == 'cover.svg' else ''
        manifest += f'<item id="art{index}" href="images/{name}" media-type="image/svg+xml"{prop}/>'
    modified = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    opf = ('<?xml version="1.0" encoding="utf-8"?><package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="book-id" xml:lang="en">'
           '<metadata xmlns:dc="http://purl.org/dc/elements/1.1/"><dc:identifier id="book-id">' + identifier + '</dc:identifier><dc:title>' + _escape(title) + '</dc:title><dc:language>en</dc:language><dc:creator>' + _escape(PARENT_BRAND) + '</dc:creator><meta property="dcterms:modified">' + modified + '</meta></metadata><manifest>' + manifest + '</manifest><spine toc="ncx">' + spine + '</spine></package>')
    files = {'META-INF/container.xml': '<?xml version="1.0"?><container xmlns="urn:oasis:names:tc:opendocument:xmlns:container" version="1.0"><rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/></rootfiles></container>',
             'OEBPS/content.opf': opf, 'OEBPS/nav.xhtml': nav, 'OEBPS/toc.ncx': ncx,
             'OEBPS/styles.css': 'body{font-family:serif;line-height:1.5;margin:5%;color:#171717;background:#fff}h1,h2{line-height:1.2}img{max-width:100%;height:auto}table{border-collapse:collapse;width:100%}td,th{border:1px solid #555;padding:.4em;overflow-wrap:anywhere}dt{font-weight:bold}figure{margin:1em 0}a{color:#164574}'}
    files.update({'OEBPS/' + name: _xhtml(label, body) for name, label, body in pages})
    files.update({'OEBPS/images/' + name: svg for name, svg in art.items()})
    output = io.BytesIO()
    with zipfile.ZipFile(output, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr('mimetype', b'application/epub+zip', compress_type=zipfile.ZIP_STORED)
        for name, content in files.items():
            if name.endswith(('.xml', '.opf', '.ncx', '.xhtml', '.svg')):
                ET.fromstring(content)
            archive.writestr(name, content.encode('utf-8'))
    return output.getvalue()


def _package_files(state, concept_id):
    metadata, manuscript, workbook, diagrams, scorecard, approved = _unpack_state(state)
    files = {fmt + '.pdf': render_fymc_pdf_bytes(state, concept_id, fmt)
             for fmt in ('digital_pdf', 'print_6x9_pdf', 'workbook_pdf')}
    art = _epub_art(state, concept_id)
    files['book.epub'] = render_fymc_epub_bytes(state, concept_id, _art=art)
    for name, svg in art.items():
        files['art/' + name] = svg.encode('utf-8')
    manifest = {'concept_id': concept_id, 'approved': approved == concept_id,
                'preview_only': True, 'files': {name: {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()} for name, data in files.items()}}
    files['manifest.json'] = json.dumps(manifest, indent=2).encode('utf-8')
    return files


def _zip_files(files):
    output = io.BytesIO()
    with zipfile.ZipFile(output, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
        for name, content in files.items():
            archive.writestr(name, content)
    return output.getvalue()


def render_fymc_bundle_zip_bytes(state: dict, concept_id: str = 'concept_a') -> bytes:
    return _zip_files(_package_files(state, concept_id))


def _write_durable_file(path: Path, data: bytes) -> None:
    fd = os.open(str(path), os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)
    with os.fdopen(fd, 'wb') as stream:
        stream.write(data)
        stream.flush()
        os.fsync(stream.fileno())


def _write_export_journal(previews_dir: Path, journal_path: Path, concept_id: str, payload: dict) -> None:
    serialized = json.dumps(payload, indent=2, ensure_ascii=False, allow_nan=False) + '\n'
    tmp_path = None
    try:
        with tempfile.NamedTemporaryFile(
            mode='w', encoding='utf-8', dir=str(previews_dir),
            prefix=f'.export_journal_{concept_id}.tmp.', suffix='.json', delete=False,
        ) as tmp:
            tmp_path = Path(tmp.name)
            tmp.write(serialized)
            tmp.flush()
            os.fsync(tmp.fileno())
        os.replace(tmp_path, journal_path)
        _fsync_dir(previews_dir)
    finally:
        if tmp_path is not None:
            tmp_path.unlink(missing_ok=True)


def export_concept_package(root_dir: Path, state: dict, concept_id: str = 'concept_a') -> dict:
    if concept_id not in {'concept_a', 'concept_b', 'concept_c'}:
        raise ValueError('Unknown concept id')
    root = Path(root_dir).resolve()
    directory = root / 'publishing' / 'previews' / concept_id
    if os.path.commonpath([str(root), str(directory.resolve())]) != str(root):
        raise ValueError('Preview directory escapes the project root')
    files = _package_files(state, concept_id)
    files['bundle.zip'] = _zip_files(files)
    with _root_lock(root):
        previews_dir = directory.parent
        previews_dir.mkdir(parents=True, exist_ok=True)
        _recover_export_journals(root)
        if os.path.commonpath([str(root), str(directory.resolve())]) != str(root):
            raise ValueError('Preview directory escapes the project root')
        stage_dir = Path(tempfile.mkdtemp(prefix=concept_id + '.stage.', dir=str(previews_dir)))
        backup = directory.with_name(concept_id + '.prev.' + uuid4().hex)
        journal_path = previews_dir / f'.export_journal_{concept_id}.json'
        try:
            staged_dirs = {stage_dir}
            for name, data in files.items():
                path = stage_dir / name
                if not path.resolve().is_relative_to(stage_dir.resolve()):
                    raise ValueError('Preview target escapes staging directory')
                path.parent.mkdir(parents=True, exist_ok=True)
                parent = path.parent
                while parent != stage_dir and stage_dir in parent.parents:
                    staged_dirs.add(parent)
                    parent = parent.parent
                _write_durable_file(path, data)
            for dpath in sorted(staged_dirs, key=lambda p: len(p.parts), reverse=True):
                _fsync_dir(dpath)
            _fsync_dir(previews_dir)
            had_existing = directory.exists()
            _write_export_journal(previews_dir, journal_path, concept_id, {
                'concept_id': concept_id,
                'target': directory.name,
                'stage': stage_dir.name,
                'backup': backup.name,
                'had_existing': had_existing,
                'expected_files': sorted(files.keys()),
            })
            if had_existing:
                os.replace(directory, backup)
                _fsync_dir(previews_dir)
            try:
                os.replace(stage_dir, directory)
                _fsync_dir(previews_dir)
            except OSError:
                if backup.exists():
                    if directory.exists() or directory.is_symlink():
                        if directory.is_dir() and not directory.is_symlink():
                            shutil.rmtree(directory)
                        else:
                            directory.unlink(missing_ok=True)
                    os.replace(backup, directory)
                elif not had_existing and (directory.exists() or directory.is_symlink()):
                    if directory.is_dir() and not directory.is_symlink():
                        shutil.rmtree(directory)
                    else:
                        directory.unlink(missing_ok=True)
                journal_path.unlink(missing_ok=True)
                try:
                    _fsync_dir(previews_dir)
                except OSError:
                    pass
                raise
            journal_path.unlink(missing_ok=True)
            _fsync_dir(previews_dir)
            if backup.exists():
                shutil.rmtree(backup)
                _fsync_dir(previews_dir)
        finally:
            if stage_dir.exists():
                shutil.rmtree(stage_dir)
                _fsync_dir(previews_dir)
        return {'concept_id': concept_id, 'output_dir': str(directory),
                'files': {name: str(directory / name) for name in files}, 'preview_only': True}

