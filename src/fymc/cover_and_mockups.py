"""Standalone SVG cover art and merchandising mockups; no external assets."""
from __future__ import annotations

import html
import re
import textwrap

from .scorecard_engine import resolve_score_value


MOCKUP_SPECS = [
    {"asset_id": "01_front_cover", "label": "Front cover", "width": 600, "height": 900},
    {"asset_id": "02_paperback_wrap", "label": "Paperback wrap", "width": 1320, "height": 960},
    {"asset_id": "03_hardcover_concept", "label": "Hardcover concept", "width": 1500, "height": 1100},
    {"asset_id": "04_ebook_cover", "label": "Ebook cover", "width": 1600, "height": 2400},
    {"asset_id": "05_3d_hardcover_mockup", "label": "3D hardcover", "width": 1400, "height": 1200},
    {"asset_id": "06_paperback_mockup", "label": "Paperback", "width": 1400, "height": 1100},
    {"asset_id": "07_ereader_mockup", "label": "E-reader", "width": 1200, "height": 1200},
    {"asset_id": "08_phone_tablet_mockup", "label": "Phone and tablet", "width": 1600, "height": 1200},
    {"asset_id": "09_series_collection_mockup", "label": "Volumes 001–005", "width": 2000, "height": 1100},
    {"asset_id": "10_social_promo_pack", "label": "Social promo pack", "width": 2400, "height": 1400},
]
_CONCEPTS = {
    "concept_a": ("#101113", "#C7A66B", "#F7F1E6"),
    "concept_b": ("#131313", "#FFD400", "#FFFFFF"),
    "concept_c": ("#F4EFE6", "#11382B", "#11382B"),
}


def _e(value):
    return html.escape(str(value), quote=True)


def _copy(value, limit=180):
    """Keep arbitrary metadata XML-safe and reserve full branding for the footer."""
    value = " ".join(str(value).split())
    value = "".join(c for c in value if 32 <= ord(c) <= 0xD7FF
                    or 0xE000 <= ord(c) <= 0xFFFD or 0x10000 <= ord(c) <= 0x10FFFF)
    for pattern in (r"The Fuck You Money Club", r"FYMC Publishing", r"fuck"):
        value = re.sub(pattern, "FYMC", value, flags=re.IGNORECASE)
    return value.replace(chr(0x2122), "").replace(chr(0x00AE), "")[:limit]


def _text(x, y, value, size=20, fill="#FFFFFF", weight=400, anchor="start", width=None):
    value = str(value)
    fitting = ""
    if width is not None and len(value) * size * 0.59 > width:
        fitting = f' textLength="{_e(width)}" lengthAdjust="spacingAndGlyphs"'
    return (f'<text x="{_e(x)}" y="{_e(y)}" fill="{_e(fill)}" '
            f'font-family="Arial, Helvetica, sans-serif" font-size="{_e(size)}" '
            f'font-weight="{_e(weight)}" text-anchor="{_e(anchor)}"{fitting}>'
            f'{_e(value)}</text>')


def _rect(x, y, w, h, fill, radius=0, stroke="none", sw=1):
    return (f'<rect x="{_e(x)}" y="{_e(y)}" width="{_e(w)}" height="{_e(h)}" '
            f'rx="{_e(radius)}" fill="{_e(fill)}" stroke="{_e(stroke)}" '
            f'stroke-width="{_e(sw)}"/>')


def _path(d, fill="none", stroke="none", sw=1):
    return f'<path d="{_e(d)}" fill="{_e(fill)}" stroke="{_e(stroke)}" stroke-width="{_e(sw)}"/>'


def _group(content, transform, extra=""):
    return f'<g transform="{_e(transform)}" {extra}>{content}</g>'


def _lines(x, y, value, width, size, fill, leading=None, count=4):
    rows = textwrap.wrap(_copy(value), width=width, max_lines=count, placeholder="…")
    return "".join(_text(x, y + i * (leading or size * 1.35), row, size, fill)
                   for i, row in enumerate(rows))


def _meta(meta):
    meta = dict(meta or {})
    raw = meta.get("volume_number", meta.get("volume", 1))
    try:
        number = f'{max(1, min(999, int(raw))):03d}'
    except (ValueError, TypeError, OverflowError):
        number = "001"
    return {
        "number": number,
        "title": _copy(meta.get("title", "Build wealth. Buy back your time."), 100),
        "subtitle": _copy(meta.get("subtitle", "Practical systems for capital, leverage and independence.")),
        "author": _copy(meta.get("author", "FYMC"), 60),
        "description": _copy(meta.get("description", "A field guide to turning income into enduring assets, repeatable systems and greater independence."), 600),
    }


def _footer(meta, clean, include_full_colophon, ink, x=300, y=840):
    publisher = ("FYMC Publishing" if clean else "The Fuck You Money Club") if include_full_colophon else "FYMC"
    return (_text(x, y - 27, meta["author"], 14, ink, anchor="middle", width=440)
            + _text(x, y, publisher, 17, ink, anchor="middle", width=470))


def _score_display(score: dict | None) -> tuple[str, str]:
    """Return `(total_str, sub_str)` using canonical scorecard values without inventing sub-scores."""
    numeric = resolve_score_value(score, default=87)
    total_str = _copy(f"{numeric:g} / 100" if numeric is not None else "87 / 100", 40)
    dims = score.get("scores") if isinstance(score, dict) and isinstance(score.get("scores"), dict) else None
    keys = (
        ("revenue_potential", "REV", 25),
        ("profit_margin_potential", "MGN", 25),
        ("team_efficiency", "TEAM", 20),
        ("startup_accessibility", "START", 15),
        ("automation_potential", "AUTO", 15),
    )
    if dims and all(
        isinstance(dims.get(k), (int, float)) and not isinstance(dims.get(k), bool)
        for k, _, _ in keys
    ):
        sub_str = " / ".join(f"{abbr} {dims[k]:g}/{cap}" for k, abbr, cap in keys)
    else:
        sub_str = ""
    return total_str, sub_str


def _concept_a(meta, score, clean, include_full_colophon):
    bg, gold, white = _CONCEPTS["concept_a"]
    total_str, sub_str = _score_display(score)
    out = _rect(0, 0, 600, 900, bg)
    out += _rect(24, 24, 552, 852, "none", stroke=gold, sw=2)
    out += _rect(33, 33, 534, 834, "none", stroke=gold, sw=0.7)
    out += _path("M300 74 L346 96 L340 153 Q325 180 300 191 Q275 180 260 153 L254 96 Z", "none", gold, 2)
    out += _path("M300 84 L336 102 L331 149 Q320 169 300 180 Q280 169 269 149 L264 102 Z", "none", gold, 0.8)
    out += _text(300, 139, "FYMC", 22, gold, 700, "middle")
    out += _text(300, 235, "THE EXECUTIVE SERIES / VOL. " + meta["number"], 14, gold, 700, "middle")
    for y, word, size in ((325, "THE BIG", 62), (416, "MONEY", 89), (502, "PLAYBOOKS", 62)):
        out += _text(300, y, word, size, white, 800, "middle", 490)
    out += _path("M110 540 H490 M175 548 H425", stroke=gold, sw=1)
    out += _text(300, 592, meta["title"], 23, gold, 600, "middle", 460)
    out += _lines(85, 636, meta["subtitle"], 46, 17, white, count=2)
    out += _rect(95, 708, 410, 66 if sub_str else 48, "#17191D", radius=4, stroke=gold, sw=1.2)
    out += _text(300, 736, "MONEY-TO-MANPOWER SCORE: " + total_str, 15, gold, 700, "middle", 386)
    if sub_str:
        out += _text(300, 760, sub_str, 11, white, 600, "middle", 386)
    return out + _footer(meta, clean, include_full_colophon, gold)


def _concept_b(meta, score, clean, include_full_colophon):
    bg, yellow, white = _CONCEPTS["concept_b"]
    total_str, sub_str = _score_display(score)
    out = _rect(0, 0, 600, 900, bg)
    out += _text(38, 56, "FYMC / VOL. " + meta["number"], 15, white, 700)
    out += _rect(368, 30, 198, 36, yellow, radius=3)
    out += _text(467, 54, "SCORE " + total_str, 16, bg, 900, "middle", 184)
    out += _path("M38 80 H562", stroke=white, sw=2)
    for y, word, size in ((182, "THE BIG", 86), (290, "MONEY", 108), (384, "PLAYBOOKS", 75)):
        out += _text(32, y, word, size, white, 900, width=534)
    out += _path("M0 492 L600 396 L600 546 L0 642 Z", yellow)
    band = _text(35, 528, "CAPITAL / LEVERAGE / FREEDOM", 27, bg, 900, width=530)
    out += _group(band, "rotate(-9.3 35 528)")
    out += _text(38, 680, meta["title"], 23, white, 700, width=524)
    out += _lines(38, 714, meta["subtitle"], 52, 15, white, count=2)
    out += _rect(38, 758, 524, 52 if sub_str else 36, "#1E1E22", radius=3, stroke=yellow, sw=1.5)
    out += _text(52, 780, "MONEY-TO-MANPOWER SCORE: " + total_str, 14, yellow, 800, width=496)
    if sub_str:
        out += _text(52, 800, sub_str, 11, white, 700, width=496)
    return out + _footer(meta, clean, include_full_colophon, white, y=858)


def _concept_c(meta, score, clean, include_full_colophon):
    vellum, green, ink = _CONCEPTS["concept_c"]
    total_str, sub_str = _score_display(score)
    out = _rect(0, 0, 600, 900, vellum)
    out += _path("M27 0 V900 M34 0 V900", stroke="#D5CCBD", sw=1)
    out += _text(60, 55, "WEALTH INTELLIGENCE / VOL. " + meta["number"], 15, ink, 700)
    out += _path("M60 76 H554", stroke=green)
    out += _path("M48 116 H327 L352 141 H564 V568 H48 Z", green)
    out += _text(72, 166, "FYMC / STRATEGY DOSSIER", 14, vellum, 700)
    for y, word, size in ((258, "THE BIG", 65), (350, "MONEY", 90), (435, "PLAYBOOKS", 60)):
        out += _text(72, y, word, size, vellum, 800, width=468)
    out += _text(72, 511, meta["title"], 20, vellum, 600, width=460)
    out += _rect(64, 594, 484, 182, "#D9D1C3", radius=2)
    out += _rect(58, 588, 484, 182, "#FFFCF5", radius=2, stroke="#BDB5A6")
    out += _text(76, 617, "ANALYTICAL INDEX / " + meta["number"], 13, ink, 700)
    out += _path("M76 630 H524 M76 711 H524", stroke="#D5CCBD")
    out += _text(76, 656, "Money-to-Manpower Score", 18, ink, 700, width=430)
    out += _text(76, 694, total_str, 27, ink, 700, width=420)
    label = score.get("label") or score.get("tier_label") or "CAPITAL EFFICIENCY / OPERATOR INDEPENDENCE"
    out += _text(76, 735, _copy(label, 75), 12, ink, width=430)
    if sub_str:
        out += _text(76, 756, sub_str, 11, ink, 700, width=430)
    return out + _footer(meta, clean, include_full_colophon, ink, y=852)


_BUILDERS = {"concept_a": _concept_a, "concept_b": _concept_b, "concept_c": _concept_c}


def _front(concept, meta, score, clean, include_full_colophon=True):
    return _BUILDERS[concept](meta, score, clean, include_full_colophon)


def _placed_cover(concept, meta, score, clean, x, y, w, h, include_full_colophon=True):
    content = _front(concept, meta, score, clean, include_full_colophon)
    return (f'<svg x="{_e(x)}" y="{_e(y)}" width="{_e(w)}" height="{_e(h)}" '
            f'viewBox="0 0 600 900" preserveAspectRatio="xMidYMid meet">{content}</svg>')


def _back(concept, meta, score=None):
    bg, accent, ink = _CONCEPTS[concept]
    total_str, sub_str = _score_display(score)
    out = _rect(0, 0, 600, 900, bg)
    out += _text(55, 100, "OWN YOUR NEXT CHAPTER.", 29, ink, 800, width=490)
    out += _path("M55 132 H545", stroke=accent, sw=2)
    out += _lines(55, 198, meta["description"], 42, 21, ink, count=9)
    out += _lines(55, 520, "Build assets. Design systems. Protect your time.", 33, 24, ink, count=2)
    panel_bg = "#FFFCF5" if concept == "concept_c" else "#1A1B1F"
    out += _rect(55, 620, 490, 86 if sub_str else 58, panel_bg, radius=4, stroke=accent, sw=1.4)
    out += _text(75, 654, "MONEY-TO-MANPOWER SCORE: " + total_str, 17, accent if concept != "concept_c" else ink, 800, width=450)
    if sub_str:
        out += _text(75, 684, sub_str, 12, ink, 700, width=450)
    out += _text(55, 770, "FYMC / VOL. " + meta["number"], 17, ink, 700)
    out += _rect(355, 798, 190, 62, "#FFFFFF")
    out += _text(450, 833, "ISBN AREA RESERVED", 11, "#333333", anchor="middle")
    return out


def _spine(concept, meta, width, height):
    bg, accent, ink = _CONCEPTS[concept]
    out = _rect(0, 0, width, height, bg)
    out += _path(f'M4 0 V{height} M{width - 4} 0 V{height}', stroke=accent, sw=0.7)
    label = _text(0, 0, "THE BIG MONEY PLAYBOOKS / " + meta["number"] + " / FYMC", 17, ink, 700, "middle", height - 100)
    return out + _group(label, f'translate({width / 2} {height / 2}) rotate(90)')


def _asset_01(concept, meta, score, clean):
    return _front(concept, meta, score, clean)


def _asset_02(concept, meta, score, clean):
    out = _rect(0, 0, 1320, 960, "#DEDAD1")
    out += _group(_back(concept, meta, score), "translate(30 30)")
    out += _group(_spine(concept, meta, 60, 900), "translate(630 30)")
    out += _placed_cover(concept, meta, score, clean, 690, 30, 600, 900)
    out += _text(660, 951, "CONCEPT WRAP / SPINE AND BLEED REQUIRE PRINTER SPECIFICATIONS", 12, "#333333", anchor="middle")
    return out


def _asset_03(concept, meta, score, clean):
    out = _rect(0, 0, 1500, 1100, "#DEDAD1")
    out += _text(70, 70, "HARDCOVER / CASE DESIGN STUDY", 25, "#262626", 700)
    out += _rect(60, 125, 630, 930, "#262626", radius=8)
    out += _group(_back(concept, meta, score), "translate(75 140)")
    out += _rect(760, 125, 650, 930, "#262626", radius=8)
    out += _group(_spine(concept, meta, 35, 900), "translate(775 140)")
    out += _placed_cover(concept, meta, score, clean, 810, 140, 585, 900)
    return out


def _asset_04(concept, meta, score, clean):
    return _placed_cover(concept, meta, score, clean, 0, 0, 1600, 2400)


def _defs():
    return '''<defs>
      <linearGradient id="stage" x2="0.25" y2="1">
        <stop stop-color="#F5F2EC"/><stop offset="1" stop-color="#CEC8BC"/>
      </linearGradient>
      <linearGradient id="pages" x2="1" y2="0">
        <stop stop-color="#AAA69C"/><stop offset="0.22" stop-color="#FFFDF5"/>
        <stop offset="0.8" stop-color="#E4DFD3"/><stop offset="1" stop-color="#BAB4A6"/>
      </linearGradient>
      <linearGradient id="foil" x2="1" y2="0.3">
        <stop stop-color="#FFFFFF" stop-opacity="0.18"/>
        <stop offset="0.3" stop-color="#FFFFFF" stop-opacity="0"/>
        <stop offset="1" stop-color="#000000" stop-opacity="0.2"/>
      </linearGradient>
      <linearGradient id="metal" x2="1" y2="1">
        <stop stop-color="#797D80"/><stop offset="0.35" stop-color="#272A2D"/>
        <stop offset="0.72" stop-color="#090B0C"/><stop offset="1" stop-color="#63676A"/>
      </linearGradient>
      <linearGradient id="glass" x2="1" y2="1">
        <stop stop-color="#FFFFFF" stop-opacity="0.14"/>
        <stop offset="0.48" stop-color="#FFFFFF" stop-opacity="0"/>
      </linearGradient>
      <filter id="shadow" x="-50%" y="-100%" width="200%" height="300%">
        <feGaussianBlur stdDeviation="15"/>
      </filter>
    </defs>'''


def _stage(width, height, label):
    return (_rect(0, 0, width, height, "url(#stage)")
            + _text(60, 65, label, 20, "#343A38", 700)
            + _path(f'M0 {height - 130} H{width}', stroke="#C4BEB2"))


def _shadow(cx, cy, rx, ry):
    return (f'<ellipse cx="{_e(cx)}" cy="{_e(cy)}" rx="{_e(rx)}" ry="{_e(ry)}" '
            'fill="#24231F" opacity="0.26" filter="url(#shadow)"/>')


def _book(concept, meta, score, clean, paperback=False, full=True):
    """Affine front/spine planes with a visible fore-edge and page strata."""
    depth = 22 if paperback else 48
    out = _path(f'M70 115 L{70 + depth} 85 L{610 + depth} 145 L610 175 Z', "url(#pages)")
    out += _path(f'M610 175 L{610 + depth} 145 L{610 + depth} 937 L610 967 Z', "url(#pages)")
    for i in range(4, depth, 4):
        out += _path(f'M{610 + i} {175 - i * 30 / depth} V{967 - i * 30 / depth}', stroke="#BEB8AA", sw=0.6)
        out += _path(f'M{70 + i} {115 - i * 30 / depth} L{610 + i} {175 - i * 30 / depth}', stroke="#D0C9BC", sw=0.6)
    if not paperback:
        out += _path(f'M{70 + depth} 82 L{615 + depth} 142 V940 L610 973 V175 L70 115 Z', "none", "#242723", 5)
    out += _group(_spine(concept, meta, 42, 900), "matrix(1 -0.36 0 0.88 28 130)")
    out += _group(_front(concept, meta, score, clean, full), "matrix(0.9 0.1 0 0.88 70 115)")
    out += _path("M70 115 L610 175 V967 L70 907 Z", "url(#foil)")
    out += _path("M78 117 V906", stroke="#FFFFFF", sw=0.7)
    out += _path("M70 115 V907", stroke="#000000", sw=2)
    if paperback:
        out += _path("M72 905 Q345 952 610 967", stroke="#EEE8DB", sw=3)
    return out


def _asset_05(concept, meta, score, clean):
    out = _stage(1400, 1200, "THE BIG MONEY PLAYBOOKS / HARDCOVER")
    out += _shadow(716, 1080, 350, 40)
    out += _group(_book(concept, meta, score, clean), "translate(340 50)")
    out += _text(70, 1148, "FYMC / VOL. " + meta["number"] + " / CASEBOUND EDITION", 17, "#343A38", 700)
    return out


def _asset_06(concept, meta, score, clean):
    out = _stage(1400, 1100, "THE BIG MONEY PLAYBOOKS / PAPERBACK")
    out += _shadow(750, 974, 410, 38)
    # A second, back-facing copy provides context without repeating the colophon.
    out += _path("M820 336 L1200 408 L1187 967 L807 895 Z", "url(#pages)")
    out += _group(_back(concept, meta), "matrix(0.62 0.12 -0.014 0.62 820 330)")
    out += _path("M820 330 L1192 402 L1179 960 L807 888 Z", "url(#foil)")
    out += _group(_book(concept, meta, score, clean, paperback=True), "translate(265 30) scale(0.92)")
    out += _text(70, 1050, "FYMC / FLEXIBLE COVER / PORTABLE FIELD EDITION", 17, "#343A38", 700)
    return out


def _device(concept, meta, score, clean, x, y, w, kind="tablet", full=True):
    phone = kind == "phone"
    ereader = kind == "ereader"
    h = w * (2.02 if phone else 1.44)
    radius = w * (0.13 if phone else 0.065)
    bezel = w * (0.055 if phone else 0.07)
    out = _shadow(x + w / 2, y + h + 12, w * 0.48, 18)
    out += _rect(x - 3, y + h * 0.23, 5, h * 0.12, "#65686B", 2)
    out += _rect(x + w - 2, y + h * 0.18, 5, h * 0.075, "#65686B", 2)
    out += _rect(x, y, w, h, "url(#metal)", radius, "#85888B", 2)
    out += _rect(x + 5, y + 5, w - 10, h - 10, "#111315", radius - 4)
    sx, sy, sw, sh = x + bezel, y + bezel, w - 2 * bezel, h - 2 * bezel
    out += _rect(sx, sy, sw, sh, "#F7F5ED", radius / 3)
    out += _text(x + w / 2, sy + 23, "FYMC READER / LIBRARY", max(10, w * 0.021), "#333936", 700, "middle", sw - 20)
    ch = min(sh - (110 if phone else 85), (sw - 20) * 1.5)
    cw = ch / 1.5
    cx, cy = x + (w - cw) / 2, sy + (sh - ch) / 2
    out += _placed_cover(concept, meta, score, clean, cx, cy, cw, ch, full)
    out += _text(x + w / 2, sy + sh - 22, "VOL. " + meta["number"] + " / OPEN BOOK", max(10, w * 0.02), "#333936", 600, "middle", sw - 20)
    if phone:
        out += _rect(x + w * 0.32, y + 13, w * 0.36, 12, "#070809", 6)
        out += _rect(x + w * 0.36, y + h - 14, w * 0.28, 4, "#909397", 2)
    else:
        out += f'<circle cx="{_e(x + w / 2)}" cy="{_e(y + bezel / 2)}" r="3" fill="#4C5660"/>'
    if ereader:
        out += _text(x + w / 2, y + h - 12, "E-READER / COLOR DISPLAY", 10, "#BFC2C1", anchor="middle")
    out += _rect(x + 6, y + 6, w - 12, h - 12, "url(#glass)", radius - 4)
    return out


def _asset_07(concept, meta, score, clean):
    out = _stage(1200, 1200, "THE BIG MONEY PLAYBOOKS / DIGITAL LIBRARY")
    out += _device(concept, meta, score, clean, 285, 135, 630, "ereader")
    out += _text(600, 1125, "YOUR NEXT CHAPTER. ALWAYS WITH YOU.", 20, "#343A38", 700, "middle")
    return out


def _asset_08(concept, meta, score, clean):
    out = _stage(1600, 1200, "THE BIG MONEY PLAYBOOKS / READ ANYWHERE")
    out += _device(concept, meta, score, clean, 255, 140, 650, "tablet")
    out += _device(concept, meta, score, clean, 1000, 352, 330, "phone", full=False)
    out += _text(800, 1144, "ONE LIBRARY / EVERY SCREEN", 21, "#343A38", 700, "middle")
    return out


def _asset_09(concept, meta, score, clean):
    out = _stage(2000, 1100, "THE BIG MONEY PLAYBOOKS / THE FIVE-VOLUME COLLECTION")
    out += _rect(55, 921, 1890, 19, "#A59E91", 3)
    out += _shadow(1000, 970, 840, 35)
    for i in range(5):
        volume = dict(meta, number=f'{i + 1:03d}')
        x = 70 + i * 375
        out += _shadow(x + 180, 918, 172, 15)
        out += _group(_book(concept, volume, score, clean, full=(i == 0)), f'translate({x} 380) scale(0.55)')
        out += _text(x + 185, 990, "VOL. " + volume["number"], 22, "#343A38", 700, "middle")
    out += _text(1000, 215, "BUILD A LIBRARY OF LEVERAGE.", 48, "#222A26", 800, "middle")
    out += _text(1000, 274, "FIVE VOLUMES / ONE INDEPENDENT MINDSET", 22, "#343A38", 600, "middle")
    return out


def _asset_10(concept, meta, score, clean):
    bg, accent, ink = _CONCEPTS[concept]
    out = _rect(0, 0, 2400, 1400, "#DEDAD1")
    out += _text(55, 65, "FYMC / SOCIAL PROMO PACK / THREE FORMAT STUDIES", 24, "#343A38", 700)
    # Square, 9:16 story and 1.91:1 landscape panels; only the square is fully branded.
    out += _rect(50, 165, 760, 760, bg)
    out += _text(92, 221, "BUILD WEALTH. BUY BACK TIME.", 25, ink, 800, width=675)
    out += _placed_cover(concept, meta, score, clean, 265, 265, 330, 495)
    out += _rect(226, 818, 408, 58, accent, 4)
    button_ink = "#F4EFE6" if concept == "concept_c" else "#101113"
    out += _text(430, 855, "EXPLORE VOL. " + meta["number"], 22, button_ink, 700, "middle")
    out += _rect(850, 165, 540, 960, bg)
    out += _text(1120, 236, "YOUR NEXT", 40, ink, 800, "middle")
    out += _text(1120, 287, "POWER MOVE.", 40, ink, 800, "middle")
    out += _group(_book(concept, meta, score, clean, full=False), "translate(900 285) scale(0.6)")
    out += _text(1120, 970, "THE BIG MONEY PLAYBOOKS", 23, ink, 800, "middle", 480)
    out += _text(1120, 1043, "FYMC / START READING", 20, ink, 700, "middle")
    out += _rect(1430, 165, 920, 482, bg)
    out += _placed_cover(concept, meta, score, clean, 1470, 201, 260, 390, False)
    out += _text(1780, 280, "THE BIG MONEY", 33, ink, 800, width=520)
    out += _text(1780, 329, "PLAYBOOKS", 44, ink, 800, width=520)
    out += _lines(1780, 394, meta["title"], 29, 22, ink, count=3)
    out += _text(1780, 570, "FYMC / EXPLORE THE SERIES", 19, ink, 700, width=520)
    for x, y, label in ((50, 974, "01 / SQUARE / 1:1"), (850, 1174, "02 / STORY / 9:16"), (1430, 696, "03 / LANDSCAPE / 1.91:1")):
        out += _text(x, y, label, 19, "#343A38", 700)
    out += _text(55, 1320, "LAYOUT CONTACT SHEET / VECTOR ART / EXPORT EACH PANEL FOR ITS CHANNEL", 20, "#343A38", 600)
    return out


_ASSETS = dict(zip((spec["asset_id"] for spec in MOCKUP_SPECS), (
    _asset_01, _asset_02, _asset_03, _asset_04, _asset_05,
    _asset_06, _asset_07, _asset_08, _asset_09, _asset_10,
)))


def render_cover_or_mockup_svg(
    concept_id: str, asset_id: str, volume_meta: dict | None = None,
    scorecard: dict | None = None, marketplace_clean: bool = False,
) -> str:
    """Render a self-contained SVG. Wrap dimensions are concepts, not print templates.

    Metadata keys: volume_number (or volume), title, subtitle, author, description.
    Scorecard keys: money_to_manpower_score, total_score (or score), label (or
    tier_label). Missing scores default to 87 / 100. Secondary faces use FYMC
    rather than the full colophon.
    """
    if concept_id not in _BUILDERS:
        raise ValueError(f'Unknown concept_id: {concept_id!r}; choose {tuple(_BUILDERS)}')
    if asset_id not in _ASSETS:
        raise ValueError(f'Unknown asset_id: {asset_id!r}; choose {tuple(_ASSETS)}')
    spec = next(item for item in MOCKUP_SPECS if item["asset_id"] == asset_id)
    width, height = spec["width"], spec["height"]
    content = _ASSETS[asset_id](concept_id, _meta(volume_meta), dict(scorecard or {}), marketplace_clean)
    title = "THE BIG MONEY PLAYBOOKS / " + spec["label"]
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
            f'viewBox="0 0 {width} {height}" role="img" aria-labelledby="art-title art-desc">'
            f'<title id="art-title">{_e(title)}</title>'
            '<desc id="art-desc">Original vector cover concept and presentation artwork. '
            'Mockups illustrate proposed formats, not manufactured products.</desc>'
            + _defs() + content + '</svg>')


def render_all_concept_mockups(
    concept_id: str, volume_meta: dict | None = None, scorecard: dict | None = None,
    marketplace_clean: bool = False,
) -> dict[str, str]:
    """Return all ten deliverables, keyed by their exact asset identifiers."""
    return {spec["asset_id"]: render_cover_or_mockup_svg(
        concept_id, spec["asset_id"], volume_meta, scorecard, marketplace_clean,
    ) for spec in MOCKUP_SPECS}

