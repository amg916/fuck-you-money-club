"""Eight SVG diagram grammars, expressed through three editorial systems."""
from __future__ import annotations

import math
import textwrap
import html

from .design_concepts import get_concept, _SVG, _number, _records, _display


_TYPES = {"process_flow", "funnel", "waterfall", "horizontal_bars",
          "decision_tree", "org_architecture", "stacked_comparison", "timeline_roadmap"}


def _label(row, index):
    return row.get("label", row.get("name", row.get("title", f"Item {index + 1}")))


def _value(row):
    value = _number(row.get("numeric_value"))
    return value if value is not None else _number(row.get("value", row.get("amount", row.get("count", row.get("score")))))


def _source(diagram, kind):
    preferred = {"process_flow": "stages", "funnel": "stages", "waterfall": "items",
                 "horizontal_bars": "bars", "decision_tree": "nodes", "org_architecture": "nodes",
                 "stacked_comparison": "rows", "timeline_roadmap": "stages"}.get(kind)
    for key in dict.fromkeys([preferred, "stages", "items", "nodes", "bars", "rows"]):
        rows = _records(diagram.get(key))
        if rows:
            return rows
    return []


def render_diagram_svg(diagram: dict, concept_id: str = "concept_a") -> str:
    t = get_concept(concept_id)
    d = diagram if isinstance(diagram, dict) else {}
    kind = str(d.get("chart_type", "process_flow"))
    title = d.get("title", kind.replace("_", " ").title())
    a, b = concept_id == "concept_a", concept_id == "concept_b"
    s = _SVG(1000, 620, t, title, _display(d))
    # Every original record is accessible in the SVG description; plates are bounded.
    limits = {"process_flow": 8, "funnel": 7, "waterfall": 8, "horizontal_bars": 9,
              "decision_tree": 9, "org_architecture": 9, "stacked_comparison": 6, "timeline_roadmap": 8}
    original = _source(d, kind)
    rows = original[:limits.get(kind, 8)]
    notes = []
    if len(original) > len(rows):
        notes.append(f"Showing {len(rows)} of {len(original)} records; full data in SVG description.")
    if b:
        s.rect(0, 0, 1000, 114, t["cover_bg"])
        s.rect(32, 24, 12, 66, t["accent"])
        s.text(59, 52, title, 29, t["cover_fg"], t["display_font"], width=54, lines=2)
    else:
        s.text(36, 49, title, 28, font=t["display_font"], width=57, lines=2)
        s.line(36, 102, 964, 102, t["accent_secondary"], 1 if a else 2)
    badge = d.get("epistemic_status", d.get("epistemic_badge", d.get("epistemic_tag", "OPERATING FRAMEWORK")))
    s.text(36, 139, badge, 12, font=t["mono_font"], width=110, lines=1)
    if a:
        s.line(154, 162, 154, 512)
        s.text(36, 184, "PLATE", 12, font=t["mono_font"])
        s.text(36, 211, kind.replace("_", " "), 12, width=13, lines=3)
    left, right, top, bottom = (180 if a else 42), 956, 174, 480
    width, height, n = right - left, bottom - top, len(rows)

    def node(x, y, w, h, row, index):
        if b:
            s.rect(x, y, w, h, t["accent"], t["page_fg"], 3, _display(row))
        elif a:
            s.rect(x, y, w, h, t["page_bg"], t["accent_secondary"], 1, _display(row))
            s.line(x + 7, y + 7, x + w - 7, y + 7, t["border"])
        else:
            s.line(x, y + h, x + w, y + h, t["border"])
            s.circle(x + 5, y + 15, 5, t["accent"], tip=_display(row))
        inset = 18 if not (a or b) else 10
        s.text(x + inset, y + 24, _label(row, index), 14, width=max(8, int((w - inset - 8) / 8)), lines=2)
        detail = row.get("description", row.get("detail", row.get("value", row.get("date", ""))))
        s.text(x + inset, y + h - 12, detail, 11, width=max(8, int((w - inset - 8) / 7)), lines=1)

    def arrow(x1, y1, x2, y2):
        s.line(x1, y1, x2, y2, t["page_fg"], 3 if b else 1)
        angle = math.atan2(y2 - y1, x2 - x1)
        points = [(x2, y2)] + [(x2 - 8 * math.cos(angle + delta), y2 - 8 * math.sin(angle + delta)) for delta in (-0.45, 0.45)]
        s.polygon(points, t["page_fg"])

    if kind not in _TYPES:
        s.text(left, 260, "Unsupported chart type: " + kind, 22, width=55, lines=3)
    elif not rows:
        s.text(left, 260, "No data supplied", 25, font=t["display_font"])
        s.text(left, 300, "Provide stages, items, nodes, bars, or rows.", 16)
    elif kind == "process_flow":
        cols = 2 if a else (4 if b else 3)
        levels = math.ceil(n / cols)
        cell_w, cell_h = width / cols, height / levels
        positions = []
        for i, row in enumerate(rows):
            r, c = divmod(i, cols)
            c = cols - 1 - c if r % 2 else c
            x, y = left + c * cell_w, top + r * cell_h
            positions.append((x, y, cell_w - 24, min(88, cell_h - 22)))
        for i in range(n - 1):
            x, y, w, h = positions[i]
            nx, ny, nw, nh = positions[i + 1]
            if y == ny:
                direction = nx > x
                arrow(x + (w if direction else 0), y + h / 2, nx + (0 if direction else nw), ny + nh / 2)
            else:
                arrow(x + w / 2, y + h, nx + nw / 2, ny)
        for i, row in enumerate(rows):
            node(*positions[i], row, i)
    elif kind == "funnel":
        values = [_value(row) for row in rows]
        max_value = max([v for v in values if v is not None and v >= 0] + [1])
        row_h = height / n
        center, max_w = left + width * 0.36, width * 0.65
        for i, row in enumerate(rows):
            val, y = values[i], top + i * row_h
            valid = val is not None and val >= 0
            w = max_w * (val / max_value) if valid else 0
            if b:
                s.rect(left, y, w, row_h - 8, t["accent"], tip=_display(row))
            elif a:
                # Width is constant within a stage: no fictitious next-stage interpolation.
                s.rect(center - w / 2, y, w, row_h - 8, t["callout_bg"], t["accent_secondary"], tip=_display(row))
            else:
                s.line(left, y + row_h / 2, left + max_w, y + row_h / 2)
                if valid:
                    s.circle(left + w, y + row_h / 2, 6, t["accent"], tip=_display(row))
            label = f"{_label(row, i)}: {val:g}" if valid else f"{_label(row, i)}: N/A"
            s.text(left + max_w + 15, y + row_h / 2 + 5, label, 12, width=max(12, int(width * .31 / 7)), lines=2)
        notes.append("Stage widths/positions share a zero baseline; negative counts are unavailable.")
    elif kind == "horizontal_bars":
        vals = [_value(row) for row in rows]
        lo, hi = min([v for v in vals if v is not None] + [0]), max([v for v in vals if v is not None] + [0])
        magnitude = max(abs(lo), abs(hi), 1)
        span = hi / magnitude - lo / magnitude or 1
        start, plot_w = left + 190, width - 275
        scale = lambda v: start + (v / magnitude - lo / magnitude) / span * plot_w
        zero = scale(0)
        s.line(zero, top - 8, zero, bottom, t["border"])
        for i, row in enumerate(rows):
            y, val = top + (i + .5) * height / n, vals[i]
            s.text(left, y + 4, _label(row, i), 13, width=23, lines=2)
            if val is not None:
                end = scale(val)
                if not (a or b):
                    s.line(zero, y, end, y, t["accent_secondary"], 2)
                    s.circle(end, y, 6, t["accent"], t["page_bg"], 2, _display(row))
                else:
                    s.rect(min(zero, end), y - (11 if b else 4), abs(end - zero), 22 if b else 8, t["accent"], tip=_display(row))
            s.text(right, y + 4, "N/A" if val is None else f"{val:g}", 12, anchor="end")
        s.text(start, 502, f"Scale: {lo:g} to {hi:g} {d.get('unit', '')}", 11)
    elif kind == "waterfall":
        intervals, current = [], 0.0
        for row in rows:
            val = _value(row)
            total = (row.get("is_total") or row.get("type") in ("total", "subtotal")
                     or str(row.get("detail", "")).lower().startswith(("opening total", "closing total")))
            end = (val if total else current + val) if val is not None else current
            if not math.isfinite(end):
                val, end = None, current
            intervals.append((0 if total else current, end, val))
            current = end
        low = min([0] + [min(x, y) for x, y, _ in intervals])
        high = max([0] + [max(x, y) for x, y, _ in intervals])
        magnitude = max(abs(low), abs(high), 1)
        span = high / magnitude - low / magnitude or 1
        scale = lambda v: bottom - (v / magnitude - low / magnitude) / span * (height - 32)
        s.line(left, scale(0), right, scale(0), t["muted"])
        step = width / n
        for i, (start, end, val) in enumerate(intervals):
            x, w = left + i * step + 8, step - 18
            y1, y2 = scale(start), scale(end)
            if i:
                s.line(x - 18, scale(intervals[i - 1][1]), x, scale(intervals[i - 1][1]))
            if val is not None:
                if a or b:
                    s.rect(x, min(y1, y2), w, abs(y2 - y1), t["accent"] if b else t["callout_bg"], t["page_fg"] if b else t["accent_secondary"], 2 if b else 1, _display(rows[i]))
                else:
                    s.line(x + w / 2, y1, x + w / 2, y2, t["accent"], 3)
                    s.circle(x + w / 2, y2, 5, t["accent"], tip=_display(rows[i]))
            s.text(x + w / 2, min(y1, y2) - 9, "N/A" if val is None else f"{val:g}", 12, anchor="middle", width=12, lines=1)
            s.text(x + w / 2, 499, _label(rows[i], i), 11, anchor="middle", width=max(7, int(w / 6)), lines=2)
        notes.append("Totals reset the cumulative balance; missing values do not change it.")
    elif kind in ("decision_tree", "org_architecture"):
        cols = 2 if a else 3
        cell_w, cell_h = width / cols, height / math.ceil(n / cols)
        positions = [(left + (i % cols) * cell_w, top + (i // cols) * cell_h) for i in range(n)]
        ids = {str(row.get("id", i)): i for i, row in enumerate(rows)}
        edges = _records(d.get("edges", []))
        edges += [{"source": row.get("parent", row.get("parent_id")), "target": row.get("id", i)} for i, row in enumerate(rows) if row.get("parent", row.get("parent_id")) is not None]
        if not edges:
            notes.append("No relationships supplied; nodes shown as an unconnected register.")
        for edge in edges:
            source, target = ids.get(str(edge.get("source", edge.get("from")))), ids.get(str(edge.get("target", edge.get("to"))))
            if source is None or target is None or source == target:
                notes.append("An invalid or off-plate relationship was omitted.")
                continue
            x1, y1 = positions[source]
            x2, y2 = positions[target]
            arrow(x1 + cell_w - 30, y1 + 36, x2, y2 + 36)
            if edge.get("label"):
                s.text((x1 + x2 + cell_w - 30) / 2, (y1 + y2) / 2 + 28, edge["label"], 10, width=18, lines=1)
        for i, row in enumerate(rows):
            node(*positions[i], cell_w - 30, min(82, cell_h - 16), row, i)
        notes.append("Connectors encode supplied relationships; node positions are schematic.")
    elif kind == "stacked_comparison":
        groups = [_records(row.get("segments", row.get("values", row.get("items", {})))) for row in rows]
        if all(not g for g in groups):
            groups = [[{"label": _label(row, i), "numeric_value": _value(row),
                        "value": row.get("value", _value(row)), "detail": row.get("detail", "")}]
                      for i, row in enumerate(rows)]
        magnitude = max([abs(_value(seg) or 0) for group in groups for seg in group] + [1])
        totals = [sum(max(0, _value(seg) or 0) / magnitude for seg in group) for group in groups]
        maximum = max(totals + [1 / magnitude])
        for i, row in enumerate(rows):
            y, x = top + i * height / n, left + 170
            s.text(left, y + 19, _label(row, i), 12, width=20, lines=2)
            for j, seg in enumerate(groups[i]):
                val = _value(seg)
                if val is None or val < 0:
                    notes.append("Missing/negative segments omitted.")
                    continue
                w = (val / magnitude) / maximum * (width - 180)
                # One ink, outlined segments, and direct labels: no categorical hue ambiguity.
                s.rect(x, y + 2, max(0, w - 2), 26 if b else 12, t["accent"] if b else t["callout_bg"], t["page_fg"], 1, _display(seg))
                x += w
            details = "; ".join(f"{_label(seg, j)}: {_display(seg.get('value', seg.get('amount')))}" for j, seg in enumerate(groups[i]))
            s.text(left + 170, y + (43 if b else 32), details or "No segments supplied", 10, width=105 if not a else 87, lines=1)
        notes.append("Common absolute scale; segment identity is directly labeled, not color-coded.")
    elif kind == "timeline_roadmap":
        vertical = a
        if vertical:
            s.line(left + 8, top, left + 8, bottom, t["accent_secondary"], 1)
        else:
            s.line(left, 317, right, 317, t["page_fg"], 4 if b else 1)
        for i, row in enumerate(rows):
            if vertical:
                x, y = left + 8, top + (i + .5) * height / n
                s.circle(x, y, 5, t["accent"], tip=_display(row))
                s.text(x + 20, y + 4, _label(row, i), 13, width=43, lines=1)
                s.text(right, y + 4, row.get("date", row.get("duration", row.get("value", "Milestone"))), 12, anchor="end", width=26, lines=1)
            else:
                step, x = width / n, left + (i + .5) * width / n
                y = 218 if i % 2 == 0 else 375
                s.line(x, 317, x, y + (43 if i % 2 == 0 else -12), t["border"])
                if b:
                    s.rect(x - 6, 311, 12, 12, t["accent"], t["page_fg"], 2, _display(row))
                else:
                    s.circle(x, 317, 6, t["accent"], t["page_bg"], 2, _display(row))
                s.text(x, y, _label(row, i), 13, anchor="middle", width=max(8, int(step / 7)), lines=2)
                s.text(x, y + 47, row.get("date", row.get("duration", row.get("value", "Milestone"))), 10, anchor="middle", width=max(10, int(step / 6)), lines=2)
        notes.append("Ordinal roadmap: spacing represents sequence, not elapsed time.")
    s.line(36, 535, 964, 535, t["border"], 3 if b else 1)
    footer = "Assumptions: " + _display(d.get("assumptions", d.get("assumptions_note", d.get("caption", "Structured editorial exhibit."))))
    s.text(36, 556, footer, 11, width=133, lines=2)
    s.text(36, 592, " ".join(dict.fromkeys(notes)), 10, width=145, lines=1)
    return s.finish()


def render_all_diagrams_for_concept(diagrams: list[dict], concept_id: str = "concept_a") -> dict[str, str]:
    get_concept(concept_id)
    result = {}
    for i, diagram in enumerate(diagrams):
        key = str(diagram.get("id", diagram.get("diagram_id", f"diagram_{i + 1:02d}")))
        if key in result:
            raise ValueError("Duplicate diagram id: " + key)
        result[key] = render_diagram_svg(diagram, concept_id)
    return result
