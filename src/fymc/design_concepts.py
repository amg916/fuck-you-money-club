"""Three editorial systems and a self-contained, XML-safe scorecard plate."""
from __future__ import annotations

import copy
import html
import math
import textwrap

from .scorecard_engine import resolve_score_value


CONCEPTS: dict[str, dict] = {
    "concept_a": {
        "id": "concept_a", "concept_id": "concept_a",
        "palette": {
            "cover_bg": "#0B0D11", "cover_fg": "#F5F1E8",
            "page_bg": "#FAF7F0", "page_fg": "#14171F",
            "accent": "#C9A45C", "accent_secondary": "#8C6D32",
        },
        "typography": {
            "display": "Georgia, 'Times New Roman', serif",
            "body": "Arial, Helvetica, sans-serif", "mono": "Courier, monospace",
            "pdf_display": "Times-Bold", "pdf_body": "Times-Roman",
        },
        "name": "Black & Gold Executive", "cover_bg": "#0B0D11",
        "cover_surface": "#141923", "cover_fg": "#F5F1E8",
        "page_bg": "#FAF7F0", "page_fg": "#14171F", "accent": "#C9A45C",
        "accent_secondary": "#8C6D32", "muted": "#6B7280",
        "border": "#D8CEBE", "callout_bg": "#F2ECE0",
        "display_font": "Georgia, 'Times New Roman', serif",
        "body_font": "Arial, Helvetica, sans-serif", "mono_font": "Courier, monospace",
        "pdf_display_font": "Times-Bold", "pdf_body_font": "Times-Roman",
        "pdf_mono_font": "Courier", "grid_columns": 2,
        "grid": "Private-bank marginalia", "cover_composition": "Centered radial crest",
        "chart_grammar": "Fine-line architectural plates",
    },
    "concept_b": {
        "id": "concept_b", "concept_id": "concept_b",
        "palette": {
            "cover_bg": "#09090B", "cover_fg": "#FAF8F2",
            "page_bg": "#FFFFFF", "page_fg": "#09090B",
            "accent": "#FFD400", "accent_secondary": "#E11D48",
        },
        "typography": {
            "display": "'Arial Narrow', Impact, sans-serif",
            "body": "Helvetica, Arial, sans-serif", "mono": "Courier, monospace",
            "pdf_display": "Helvetica-Bold", "pdf_body": "Helvetica",
        },
        "name": "Bold Editorial", "cover_bg": "#09090B",
        "cover_surface": "#18181B", "cover_fg": "#FAF8F2",
        "page_bg": "#FFFFFF", "page_fg": "#09090B", "accent": "#FFD400",
        "accent_secondary": "#E11D48", "muted": "#52525B",
        "border": "#18181B", "callout_bg": "#FFFBEB",
        "display_font": "'Arial Narrow', Impact, sans-serif",
        "body_font": "Helvetica, Arial, sans-serif", "mono_font": "Courier, monospace",
        "pdf_display_font": "Helvetica-Bold", "pdf_body_font": "Helvetica",
        "pdf_mono_font": "Courier-Bold", "grid_columns": 12,
        "grid": "Swiss brutalist magazine", "cover_composition": "Offset typographic slab",
        "chart_grammar": "Bold flat blocks and segmented meters",
    },
    "concept_c": {
        "id": "concept_c", "concept_id": "concept_c",
        "palette": {
            "cover_bg": "#F4EFE6", "cover_fg": "#11382B",
            "page_bg": "#F8F4EC", "page_fg": "#1D2421",
            "accent": "#11382B", "accent_secondary": "#B68D40",
        },
        "typography": {
            "display": "Palatino, Georgia, serif",
            "body": "Optima, Calibri, sans-serif", "mono": "Helvetica, sans-serif",
            "pdf_display": "Times-Bold", "pdf_body": "Times-Roman",
        },
        "name": "Modern Wealth Intelligence", "cover_bg": "#F4EFE6",
        "cover_surface": "#EAE2D3", "cover_fg": "#11382B",
        "page_bg": "#F8F4EC", "page_fg": "#1D2421", "accent": "#11382B",
        "accent_secondary": "#B68D40", "muted": "#5A6560",
        "border": "#CFC6B4", "callout_bg": "#EFE9DC",
        "display_font": "Palatino, Georgia, serif",
        "body_font": "Optima, Calibri, sans-serif", "mono_font": "Helvetica, sans-serif",
        "pdf_display_font": "Times-Bold", "pdf_body_font": "Times-Roman",
        "pdf_mono_font": "Helvetica", "grid_columns": 3,
        "grid": "Tufte analytical dossier", "cover_composition": "Asymmetric research masthead",
        "chart_grammar": "Forest-green dot and bullet scales with brass rules",
    },
}


def get_all_concepts() -> dict[str, dict]:
    return copy.deepcopy(CONCEPTS)


def get_concept(concept_id: str) -> dict:
    if concept_id not in CONCEPTS:
        raise ValueError("Unknown concept: " + str(concept_id))
    return copy.deepcopy(CONCEPTS[concept_id])


def _escape(value) -> str:
    # XML 1.0 excludes control characters, surrogates, and FFFE/FFFF.
    raw = str(value)
    raw = "".join(c for c in raw if c in "\t\n\r" or
                  0x20 <= ord(c) <= 0xD7FF or 0xE000 <= ord(c) <= 0xFFFD or
                  0x10000 <= ord(c) <= 0x10FFFF)
    return html.escape(raw, quote=True)


def _number(value, default=None):
    try:
        result = float(value)
        return result if math.isfinite(result) else default
    except (ValueError, TypeError, OverflowError):
        return default


def _display(value) -> str:
    if value is None:
        return "Not supplied"
    if isinstance(value, dict):
        return "; ".join(str(k).replace("_", " ") + ": " + _display(v)
                         for k, v in value.items())
    if isinstance(value, (list, tuple)):
        return "; ".join(_display(v) for v in value)
    return str(value)


def _records(value) -> list[dict]:
    if isinstance(value, dict):
        return [dict(v, label=v.get("label", str(k).replace("_", " ")))
                if isinstance(v, dict) else {"label": str(k).replace("_", " "), "value": v}
                for k, v in value.items()]
    if isinstance(value, (list, tuple)):
        return [v.copy() if isinstance(v, dict) else {"label": str(v)} for v in value]
    return []


def _finite_geometry(*values):
    try:
        valid = all(math.isfinite(value) for value in values)
    except (TypeError, ValueError, OverflowError):
        valid = False
    if not valid:
        raise ValueError("SVG geometry must be finite")


class _SVG:
    def __init__(self, width, height, theme, title, description=""):
        self.theme = theme
        self.parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img">',
                      f'<title>{_escape(title)}</title><desc>{_escape(description)}</desc>']
        self.rect(0, 0, width, height, theme["page_bg"])

    def rect(self, x, y, width, height, fill, stroke="none", sw=1, tip=None):
        _finite_geometry(x, y, width, height, sw)
        self.parts.append(f'<rect x="{x}" y="{y}" width="{max(0, width)}" height="{max(0, height)}" fill="{_escape(fill)}" stroke="{_escape(stroke)}" stroke-width="{sw}">')
        if tip is not None:
            self.parts.append(f'<title>{_escape(tip)}</title>')
        self.parts.append('</rect>')

    def line(self, x1, y1, x2, y2, color=None, sw=1):
        _finite_geometry(x1, y1, x2, y2, sw)
        self.parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{_escape(color or self.theme["border"])}" stroke-width="{sw}"/>')

    def circle(self, x, y, radius, fill, stroke="none", sw=1, tip=None):
        _finite_geometry(x, y, radius, sw)
        self.parts.append(f'<circle cx="{x}" cy="{y}" r="{radius}" fill="{_escape(fill)}" stroke="{_escape(stroke)}" stroke-width="{sw}">')
        if tip is not None:
            self.parts.append(f'<title>{_escape(tip)}</title>')
        self.parts.append('</circle>')

    def polygon(self, points, fill, stroke="none", sw=1):
        points = list(points)
        _finite_geometry(sw, *(coordinate for point in points for coordinate in point))
        coords = " ".join(f"{x},{y}" for x, y in points)
        self.parts.append(f'<polygon points="{coords}" fill="{_escape(fill)}" stroke="{_escape(stroke)}" stroke-width="{sw}"/>')

    def text(self, x, y, value, size=16, color=None, font=None, anchor="start", width=70, lines=2):
        _finite_geometry(x, y, size, width, lines, size * 1.25)
        raw = _display(value)
        wrapped = textwrap.wrap(raw, width=max(1, int(width))) or [""]
        clipped = wrapped[:lines]
        if len(wrapped) > lines:
            clipped[-1] = clipped[-1].rstrip(".") + "…"
        self.parts.append(f'<text x="{x}" y="{y}" font-family="{_escape(font or self.theme["body_font"])}" font-size="{size}" fill="{_escape(color or self.theme["page_fg"])}" text-anchor="{_escape(anchor)}" style="font-variant-numeric:tabular-nums">')
        self.parts.append(f'<title>{_escape(raw)}</title>')
        for i, chunk in enumerate(clipped):
            self.parts.append(f'<tspan x="{x}" dy="{0 if i == 0 else size * 1.25}">{_escape(chunk)}</tspan>')
        self.parts.append('</text>')

    def finish(self):
        return "".join(self.parts) + '</svg>'


def render_scorecard_svg(scorecard: dict, concept_id: str = "concept_a") -> str:
    t = get_concept(concept_id)
    data = scorecard if isinstance(scorecard, dict) else {}
    a, b = concept_id == "concept_a", concept_id == "concept_b"
    title = "Money-to-Manpower Score"
    s = _SVG(850, 1100, t, title, _display(data))
    s.rect(0, 0, 850, 310, t["cover_bg"])
    s.text(42, 37, t["name"].upper(), 13, t["cover_fg"], t["mono_font"])
    score = resolve_score_value(data, default=None)
    shown = "N/A" if score is None else f"{score:g}"
    if a:
        s.text(42, 82, title, 29, t["cover_fg"], t["display_font"])
        for angle in range(0, 360, 10):
            rad = math.radians(angle)
            s.line(680 + 84 * math.cos(rad), 191 + 84 * math.sin(rad),
                   680 + 96 * math.cos(rad), 191 + 96 * math.sin(rad), t["accent"])
        s.circle(680, 191, 77, "none", t["accent"], 1)
        s.circle(680, 191, 69, "none", t["accent_secondary"], 1)
        s.text(680, 202, shown, 39, t["cover_fg"], t["display_font"], "middle", 8, 1)
        s.text(680, 229, "OF 100", 11, t["cover_fg"], anchor="middle")
        s.text(42, 156, data.get("title", data.get("name", "Executive opportunity assessment")), 24,
               t["cover_fg"], t["display_font"], width=33, lines=3)
        s.text(42, 273, "I / CAPITAL   II / PEOPLE   III / EVIDENCE", 12, t["cover_fg"])
    elif b:
        s.rect(42, 64, 766, 142, t["accent"])
        s.text(59, 110, title, 36, t["page_fg"], t["display_font"], width=34, lines=1)
        s.text(60, 180, shown + " / 100", 53, t["page_fg"], t["display_font"])
        s.text(42, 246, data.get("title", "THE OPERATING LEVERAGE FILE"), 25,
               t["cover_fg"], t["display_font"], width=48)
        s.text(42, 291, "MONEY-TO-MANPOWER INDEX / 0-100", 12, t["cover_fg"], t["mono_font"])
    else:
        s.line(42, 60, 808, 60, t["accent_secondary"], 2)
        s.text(42, 106, title, 32, t["cover_fg"], t["display_font"])
        s.text(42, 181, shown, 62, t["cover_fg"], t["display_font"])
        s.text(42, 213, "Composite / 100", 13, t["page_fg"])
        s.text(310, 158, data.get("title", "Wealth intelligence dossier"), 24,
               t["cover_fg"], t["display_font"], width=33, lines=3)
        s.text(310, 269, "Evidence before inference. Assumptions made explicit.", 13, width=48)
    s.text(42, 344, "01 / FIVE DIMENSIONS", 14, font=t["mono_font"])
    subs = _records(data.get("sub_scores") or data.get("subscores") or data.get("dimensions", {}))
    if not subs and isinstance(data.get("scores"), dict):
        labels = {
            "revenue_potential": "Revenue Potential",
            "profit_margin_potential": "Profit Margin Potential",
            "team_efficiency": "Team Efficiency",
            "startup_accessibility": "Startup Accessibility",
            "automation_potential": "Automation Potential",
        }
        dimension_max = data.get("dimension_max")
        dimension_max = dimension_max if isinstance(dimension_max, dict) else {}
        score_rationale = data.get("score_rationale")
        score_rationale = score_rationale if isinstance(score_rationale, dict) else {}
        subs = [{"label": labels.get(k, k.replace("_", " ").title()),
                 "score": data["scores"][k], "max_score": dimension_max.get(k, 25),
                 "rationale": score_rationale.get(k, "")}
                for k in dict.fromkeys([*labels, *data["scores"]]) if k in data["scores"]]
    defaults = ["Capital efficiency", "Labor leverage", "Margin quality", "Scalability", "Resilience"]
    for i in range(5):
        row = subs[i] if i < len(subs) else {"label": defaults[i]}
        val = _number(row.get("score", row.get("value")))
        maximum = _number(row.get("max_score", row.get("max", 100)), 100)
        ratio = max(0, min(1, val / maximum)) if val is not None and maximum > 0 else None
        y = 382 + i * 43
        s.text(42, y, row.get("label", row.get("name", defaults[i])), 14, width=27, lines=2)
        s.text(795, y, "N/A" if val is None else f"{val:g} / {maximum:g}", 13, anchor="end", width=20, lines=1)
        tip = _display(row)
        if b:
            for j in range(10):
                s.rect(300 + j * 40, y - 16, 36, 20, t["callout_bg"], t["border"], tip=tip)
                fraction = 0 if ratio is None else max(0, min(1, ratio * 10 - j))
                s.rect(300 + j * 40, y - 16, 36 * fraction, 20, t["accent"], tip=tip)
        else:
            s.line(300, y - 5, 700, y - 5, t["border"], 1)
            for tick in range(5):
                s.line(300 + tick * 100, y - 10, 300 + tick * 100, y, t["border"])
            if ratio is not None:
                if a:
                    s.rect(300, y - 9, ratio * 400, 8, t["accent"], tip=tip)
                else:
                    s.circle(300 + ratio * 400, y - 5, 6, t["accent"], t["page_bg"], 2, tip)
    s.text(42, 624, "02 / SCENARIO REGISTER", 14, font=t["mono_font"])
    scenarios = _records(data.get("scenarios", {}))
    for i, label in enumerate(("Downside", "Base case", "Upside")):
        row = scenarios[i] if i < len(scenarios) else {"label": label, "value": None}
        x = 42 + i * 260
        if b:
            s.rect(x, 646, 246, 134, t["callout_bg"], t["border"], 3)
        elif a:
            s.rect(x, 646, 246, 134, "none", t["border"])
        else:
            s.line(x, 646, x + 240, 646, t["accent_secondary"], 2)
        s.text(x + 12, 670, row.get("label", row.get("name", label)), 17, font=t["display_font"], width=22, lines=1)
        if isinstance(data.get("scenarios"), dict) and "annual_gross_revenue_usd" in row:
            details = []
            for key, name, money in (
                ("annual_gross_revenue_usd", "Gross", True),
                ("net_profit_margin_pct", "Margin", False),
                ("annual_owner_net_profit_usd", "Owner Net Profit", True),
                ("total_people", "Team", False),
            ):
                value = _number(row.get(key))
                shown = "Not supplied" if value is None else (f"${value:,.0f}" if money else f"{value:g}")
                if key == "net_profit_margin_pct" and value is not None:
                    shown += "%"
                details.append(f"{name}: {shown}")
            for j, detail in enumerate(details):
                s.text(x + 12, 698 + j * 18, detail, 13, width=27, lines=1)
        else:
            details = {k: v for k, v in row.items() if k not in ("name", "label")}
            s.text(x + 12, 698, _display(details) or "Not supplied", 13, width=27, lines=4)
    s.text(42, 817, "03 / ECONOMICS", 14, font=t["mono_font"])
    s.text(42, 846, _display(data.get("economics")), 14, width=90, lines=3)
    s.text(42, 927, "04 / UNCERTAINTY BAND", 14, font=t["mono_font"])
    band = data.get("uncertainty_bounds")
    if not isinstance(band, (dict, list, tuple)):
        band = data.get("uncertainty_band", data.get("uncertainty", {}))
        if not isinstance(band, (dict, list, tuple)):
            band = data.get("uncertainty", {})
    if isinstance(band, (list, tuple)) and len(band) >= 2:
        band = {"low": band[0], "high": band[1]}
    low = _number(band.get("low", band.get("lower"))) if isinstance(band, dict) else None
    high = _number(band.get("high", band.get("upper"))) if isinstance(band, dict) else None
    s.line(42, 960, 808, 960, t["border"], 2)
    if low is not None and high is not None and 0 <= low <= high <= 100:
        x1, x2 = 42 + low * 7.66, 42 + high * 7.66
        s.rect(x1, 954, x2 - x1, 12, t["accent"], tip=f"Uncertainty: {low:g} to {high:g}")
        s.line(x1, 948, x1, 972, t["page_fg"])
        s.line(x2, 948, x2, 972, t["page_fg"])
        interval = data.get("uncertainty_band")
        interval = interval if isinstance(interval, str) and interval else "interval as supplied"
        s.text(425, 998, f"{low:g}–{high:g} / 100 • {interval}", 13, anchor="middle")
    else:
        s.text(425, 998, "Interval unavailable or invalid; no confidence level inferred", 13, anchor="middle")
    status = data.get("epistemic_status") or (f"Evidence confidence: {data['evidence_confidence']} ({data.get('uncertainty_band', '')})".strip() if data.get("evidence_confidence") else "Weighted 100-point rubric")
    s.text(42, 1033, status, 12, width=95, lines=1)
    footer = _display(data.get("assumptions") or data.get("uncertainty_note") or "Weighted 100-point small-team capital and labor leverage assessment.")
    if len(subs) > 5 or len(scenarios) > 3:
        footer = "Additional records retained in SVG description. " + footer
    s.text(42, 1060, footer, 11, width=110, lines=2)
    return s.finish()
