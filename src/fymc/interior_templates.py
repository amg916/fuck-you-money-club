"""Editorial interior plates; sibling modules own concept and SVG rendering."""
from __future__ import annotations

import html
import re

from .brand_and_catalog import _normalize_section
from .design_concepts import get_concept, render_scorecard_svg
from .diagrams_engine import render_diagram_svg
from .scorecard_engine import resolve_score_value


INTERIOR_TEMPLATES = [
    {"template_id": "chapter_opener", "label": "01. Chapter Opening Spread", "default_chapter": 1},
    {"template_id": "executive_summary", "label": "02. Executive Summary Brief", "default_chapter": 2},
    {"template_id": "opportunity_overview", "label": "03. Opportunity Overview", "default_chapter": 1},
    {"template_id": "step_by_step_sop", "label": "04. Step-by-Step Operator SOP", "default_chapter": 6},
    {"template_id": "expert_insights", "label": "05. Corroborated Expert Insights", "default_chapter": 5},
    {"template_id": "financial_breakdown", "label": "06. Financial & Unit-Economics Breakdown", "default_chapter": 3},
    {"template_id": "case_study_walkthrough", "label": "07. Illustrative Case Study Walkthrough", "default_chapter": 10},
    {"template_id": "comparison_table", "label": "08. Structured Comparison Matrix", "default_chapter": 4},
    {"template_id": "research_exhibit", "label": "09. Research Exhibit & Data Plate", "default_chapter": 7},
    {"template_id": "legal_compliance_notes", "label": "10. Statutory & Jurisdictional Notes", "default_chapter": 9},
    {"template_id": "resource_directory", "label": "11. Public Records & Tool Directory", "default_chapter": 8},
    {"template_id": "action_checklist", "label": "12. Operator Action Checklist", "default_chapter": 11},
    {"template_id": "thirty_day_plan", "label": "13. 30-Day Implementation Plan", "default_chapter": 12},
    {"template_id": "scorecard_page", "label": "14. Money-to-Manpower Scorecard Plate", "default_chapter": 1},
]


def _text(value):
    if value is None:
        return ""
    if isinstance(value, dict):
        return "; ".join(str(k).replace("_", " ") + ": " + _text(v) for k, v in value.items())
    if isinstance(value, (list, tuple)):
        return "; ".join(_text(v) for v in value)
    return str(value)


def _e(value):
    return html.escape(_text(value), quote=True)


def _items(value):
    if value is None or value == "":
        return []
    if isinstance(value, (list, tuple)):
        return list(value)
    return [value]


def _p(value, fallback="Not supplied in the manuscript."):
    return "<p>" + _e(value if value is not None and value != "" else fallback) + "</p>"


def _list(value, ordered=False):
    tag = "ol" if ordered else "ul"
    entries = _items(value)
    if not entries:
        return '<p class="missing">No entries supplied.</p>'
    return "<" + tag + ">" + "".join("<li>" + _e(v) + "</li>" for v in entries) + "</" + tag + ">"


def _card(title, body, cls=""):
    return '<section class="card ' + _e(cls) + '"><h2>' + _e(title) + "</h2>" + body + "</section>"


def _field(chapter, manuscript, key, default=None):
    return chapter.get(key, manuscript.get(key, default))


def _link(value):
    url = _text(value).strip()
    if url.lower().startswith(("https://", "http://")):
        return '<a href="' + _e(url) + '">' + _e(url) + "</a>"
    return _e(value)


def _table(headers, rows, caption, link_columns=()):
    head = "".join('<th scope="col">' + _e(h) + "</th>" for h in headers)
    body = "".join("<tr>" + "".join("<td>" + (_link(v) if i in link_columns else _e(v)) + "</td>" for i, v in enumerate(row)) + "</tr>" for row in rows)
    if not body:
        body = '<tr><td colspan="' + str(len(headers)) + '">No data supplied.</td></tr>'
    return '<div class="table-wrap"><table><caption>' + _e(caption) + "</caption><thead><tr>" + head + "</tr></thead><tbody>" + body + "</tbody></table></div>"


def _rows(value, keys):
    rows = []
    for item in _items(value):
        if isinstance(item, dict):
            lower = {str(key).lower(): key for key in item}
            normalized = {re.sub(r"[^a-z0-9]+", "_", str(key).lower()).strip("_"): key for key in item}
            cells = []
            for k in keys:
                name = str(k)
                actual = k if k in item else lower.get(name.lower())
                if actual is None:
                    actual = normalized.get(re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_"))
                cells.append(item[actual] if actual is not None else "Not supplied")
            rows.append(cells)
        elif isinstance(item, (list, tuple)):
            rows.append((list(item) + ["Not supplied"] * len(keys))[:len(keys)])
        else:
            rows.append([item] + ["Not supplied"] * (len(keys) - 1))
    return rows


def _paragraphs(value):
    return "".join(_p(item) for item in _items(value))


def _sections(c):
    return _items(c.get("sections", []))


def _metrics(value):
    entries = []
    for item in _items(value):
        if isinstance(item, dict):
            label = _text(item.get("label", ""))
            text = (label + ": " if label else "") + _text(item.get("value", ""))
            context = item.get("context") or item.get("note")
            if context:
                text += " — " + _text(context)
            entries.append(text)
        else:
            entries.append(item)
    return _list(entries)


def _sop_entries(section):
    value = (section.get("sop_steps") or section.get("sops") or
             section.get("sop") or section.get("procedures"))
    entries = []
    for item in _items(value):
        if isinstance(item, dict) and "steps" in item:
            entries.extend(_items(item["steps"]))
        else:
            entries.append(item)
    return entries


def _step_body(item):
    return (_paragraphs(item.get("action") or item.get("description"))
            + _paragraphs(item.get("detail")))


def _steps(value):
    entries = []
    for item in _items(value):
        if isinstance(item, dict):
            body = ("<strong>" + _e(item["title"]) + "</strong>" if item.get("title") else "")
            body += _step_body(item)
            body += _paragraphs(item.get("acceptance_criteria"))
        else:
            body = _e(item)
        entries.append("<li>" + body + "</li>")
    return "<ol>" + "".join(entries) + "</ol>" if entries else ""


def _section_table(table, caption="Chapter data"):
    raw_rows = _items(table.get("rows"))
    headers = table.get("headers") or table.get("columns") or table.get("header")
    if not headers:
        dict_keys = []
        max_cols = 0
        for row in raw_rows:
            if isinstance(row, dict):
                for key in row:
                    if key not in dict_keys:
                        dict_keys.append(key)
            elif isinstance(row, (list, tuple)):
                max_cols = max(max_cols, len(row))
        if dict_keys:
            headers = [str(k) for k in dict_keys]
        elif max_cols > 2:
            headers = [f"Column {i}" for i in range(1, max_cols + 1)]
        else:
            headers = ["Item", "Value"]
    headers = [str(h) for h in headers]
    keys = table.get("keys") or headers
    return _table(headers, _rows(raw_rows, keys), table.get("caption") or table.get("title") or caption)


def _section_html(section, include_table=True, include_steps=True):
    section = _normalize_section(section)
    if not isinstance(section, dict):
        return _p(section)
    body = "<h3>" + _e(section.get("heading", "Chapter section")) + "</h3>"
    if section.get("epistemic_status"):
        body += '<p class="muted">' + _e(_text(section["epistemic_status"]).replace("_", " ")) + "</p>"
    body += _paragraphs(section.get("paragraphs"))
    if section.get("bullets"):
        body += _list(section["bullets"])
    if include_table:
        for table in section.get("tables", []):
            if isinstance(table, dict):
                body += _section_table(table, section.get("heading", "Chapter data"))
    if include_steps:
        body += _steps(_sop_entries(section))
    for callout in section.get("callouts", []):
        if isinstance(callout, dict):
            content = ("<h3>" + _e(callout["title"]) + "</h3>" if callout.get("title") else "")
            content += _paragraphs(callout.get("body", callout.get("text", callout.get("content"))))
            if callout.get("items"):
                content += _list(callout["items"])
        else:
            content = _paragraphs(callout)
        body += '<aside class="aside">' + content + "</aside>"
    return body


def _section_cards(c, include_tables=True, include_steps=True, skip_first_table=False):
    skipped = False
    cards = []
    for section in _sections(c):
        norm = _normalize_section(section)
        if isinstance(norm, dict) and include_tables and skip_first_table and not skipped:
            dict_tables = [t for t in norm.get("tables", []) if isinstance(t, dict)]
            if dict_tables:
                trimmed = dict(norm)
                remaining = dict_tables[1:]
                if remaining:
                    trimmed["tables"] = remaining
                else:
                    trimmed.pop("tables", None)
                skipped = True
                cards.append('<section class="card wide">' + _section_html(trimmed, include_tables, include_steps) + "</section>")
                continue
        cards.append('<section class="card wide">' + _section_html(section, include_tables, include_steps) + "</section>")
    return "".join(cards)


def _first_table(c):
    for section in _sections(c):
        section = _normalize_section(section)
        if isinstance(section, dict):
            for table in section.get("tables", []):
                if isinstance(table, dict):
                    return _section_table(table, section.get("heading", "Chapter data"))
    return ""


def _quote(value):
    if not value:
        return ""
    if isinstance(value, dict):
        body = _paragraphs(value.get("quote", value.get("text")))
        attribution = value.get("author", value.get("attribution"))
        if attribution:
            body += "<cite>" + _e(attribution) + "</cite>"
    else:
        body = _paragraphs(value)
    return "<blockquote>" + body + "</blockquote>"


def _citation_body(item):
    if not isinstance(item, dict):
        return _link(item)
    body = ""
    locator = item.get("timestamp_label") or item.get("timestamp") or item.get("locator") or item.get("page")
    if locator:
        body += '<span class="muted">' + _e(locator) + "</span> "
    title = (item.get("title") or item.get("video_title") or item.get("name")
             or item.get("label") or item.get("statute") or item.get("authority"))
    if title:
        body += "<strong>" + _e(title) + "</strong>"
    seen_notes = []
    for key in ("tip", "relevance", "text", "note", "summary", "quote", "excerpt", "description"):
        val = item.get(key)
        if val not in (None, "") and val not in seen_notes:
            seen_notes.append(val)
            body += _paragraphs(val)
    url = item.get("url") or item.get("link") or item.get("video_url") or item.get("source_url")
    if url:
        body += "<p>" + _link(url) + "</p>"
    return body


def _citations(value):
    entries = _items(value)
    return "<ul>" + "".join("<li>" + _citation_body(item) + "</li>" for item in entries) + "</ul>" if entries else _list([])


def _chapter_citations(c, m):
    combined = []
    for key in ("statutory_citations", "source_citations", "citations"):
        combined.extend(_items(_field(c, m, key)))
    return combined


def _checklist(value):
    entries = _items(value)
    return '<ul class="checklist">' + "".join('<li><span class="checkbox" aria-hidden="true"></span><span>' + _e(item) + "</span></li>" for item in entries) + "</ul>" if entries else _p(None)


def _chapter(manuscript, number):
    chapters = manuscript.get("chapters", [])
    if isinstance(chapters, dict):
        value = chapters.get(str(number), chapters.get(number, {}))
        return value if isinstance(value, dict) else {"body": value}
    for index, value in enumerate(_items(chapters), 1):
        if isinstance(value, dict) and str(value.get("chapter_number", value.get("number", index))) == str(number):
            return value
    return {}


_BASE_CSS = """
*{box-sizing:border-box}body{margin:0;background:#e8e8e5;color:var(--ink);font-family:var(--body)}
.reader{padding:32px;max-width:1600px;margin:auto}.spread{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:24px;align-items:start}
.sheet{position:relative;background:var(--paper);box-shadow:0 5px 24px #0002;min-width:0}
.trim{padding:38px;min-height:850px;position:relative}.running-head,.folio{display:flex;justify-content:space-between;gap:16px;font:11px/1.5 system-ui;letter-spacing:.08em;text-transform:uppercase}
.running-head{border-bottom:1px solid var(--rule);padding-bottom:12px}.folio{border-top:1px solid var(--rule);padding-top:12px;margin-top:28px}
.page-title{font-family:var(--heading);font-size:clamp(26px,3vw,42px);line-height:1.08;margin:18px 0 24px;overflow-wrap:anywhere}
.kicker{font:700 11px/1.5 system-ui;letter-spacing:.12em;text-transform:uppercase;margin-top:20px}
.layout{display:grid;gap:20px;align-items:start}.layout>*{min-width:0}.card{border-top:1px solid var(--rule);padding-top:12px;break-inside:avoid}
h2{font-family:var(--heading);font-size:18px;line-height:1.2;margin:0 0 10px}h3{font-size:14px;margin:12px 0 6px}
p,li,td,th{font-size:13px;line-height:1.6;overflow-wrap:anywhere}p{margin:0 0 12px;white-space:pre-line}ul,ol{padding-left:20px;margin:0}li+li{margin-top:8px}
.wide,.hero,.table-wrap,.plate{grid-column:1/-1}.hero{padding:24px 0;border-bottom:3px solid var(--rule)}
.chapter-numeral{font:700 70px/1 var(--heading);margin-bottom:14px}.deck{font-size:20px;line-height:1.4}
.aside{font-size:12px;border-left:3px solid var(--accent);padding-left:12px}.missing,.muted{color:#555}
.table-wrap{overflow-x:auto}table{border-collapse:collapse;width:100%;text-align:left}caption{text-align:left;font-weight:700;padding:8px 0}
th,td{padding:9px 7px;border-bottom:1px solid var(--rule);vertical-align:top}td{white-space:pre-line}th{background:var(--wash);font-weight:700}
blockquote{margin:0;padding:14px;border-left:3px solid var(--accent)}blockquote p{font-size:17px}cite{font:12px/1.5 var(--body)}
.step{display:grid;grid-template-columns:34px 1fr;gap:12px;margin:14px 0;break-inside:avoid}.step-number{font:700 24px/1 var(--heading)}
figure{margin:0;break-inside:avoid}figcaption{font:12px/1.5 var(--body);margin:10px 0}svg{max-width:100%;height:auto;display:block}
a{color:inherit;text-decoration:underline;text-underline-offset:3px}.checklist{list-style:none;padding:0}.checklist li{display:flex;gap:10px;border-bottom:1px solid var(--rule);padding:9px 0}
.checkbox{flex:0 0 13px;height:13px;border:1px solid currentColor;margin-top:4px}.timeline{list-style:none;padding:0}.timeline>li{border-left:3px solid var(--accent);padding:0 0 16px 16px;break-inside:avoid}
.evidence-register{margin-top:24px}.guide{display:none;pointer-events:none;position:absolute;z-index:2}.guide-label{position:absolute;font:8px/1 system-ui;background:white;color:black;padding:2px}
.tablet .spread{display:block;max-width:740px;margin:auto}.tablet .trim{min-height:0}.tablet .continuation{margin-top:30px}
.print .reader{padding:20px}.print .spread{display:block}.print .sheet{width:6in;min-height:9in;margin:0 auto 20px}
.print .trim{width:6in;min-height:9in;padding:.5in .5in .5in .75in}.print .verso .trim{padding-left:.5in;padding-right:.75in}
.print .page-title{font-size:26px}.print p,.print li,.print td,.print th{font-size:10pt}.print .layout{gap:12px}
.print.guides .sheet{width:6.25in;min-height:9.25in;padding:.125in}.guides .guide{display:block}
.guide.bleed{inset:0;border:1px dashed #555}.guide.trim-guide{inset:.125in;border:1px dashed #111}
.guide.gutter{top:.625in;bottom:.625in;left:.875in;border-left:1px dotted #111}.verso .guide.gutter{left:auto;right:.875in}
.guide.crop{inset:0;background:linear-gradient(#111,#111) .125in 0/1px .09in no-repeat,linear-gradient(#111,#111) 0 .125in/.09in 1px no-repeat,linear-gradient(#111,#111) calc(100% - .125in) 0/1px .09in no-repeat,linear-gradient(#111,#111) 100% .125in/.09in 1px no-repeat,linear-gradient(#111,#111) .125in 100%/1px .09in no-repeat,linear-gradient(#111,#111) 0 calc(100% - .125in)/.09in 1px no-repeat,linear-gradient(#111,#111) calc(100% - .125in) 100%/1px .09in no-repeat,linear-gradient(#111,#111) 100% calc(100% - .125in)/.09in 1px no-repeat}
@media(max-width:850px){.reader{padding:12px}.spread{grid-template-columns:1fr}.trim{padding:24px;min-height:0}}
@media(max-width:520px){body:not(.print) .layout{grid-template-columns:1fr}body:not(.print) .layout>*{grid-column:1/-1}.page-title{font-size:28px}}
@media print{body{background:white}.reader,.print .reader{padding:0;max-width:none}.spread{display:block}.sheet,.print .sheet{box-shadow:none;margin:0;break-after:page}.sheet:last-child{break-after:auto}.table-wrap{overflow:visible}thead{display:table-header-group}a{text-decoration:none}*{print-color-adjust:exact}}
"""


def _concept_css(concept_id):
    """Different grid systems, not merely different accent colors."""
    styles = {
        "concept_a": """
:root{--ink:#171612;--paper:#fffdf7;--accent:#82671c;--rule:#a48c49;--wash:#f1ecdc;--body:Georgia,serif;--heading:Georgia,serif}
.layout{grid-template-columns:minmax(0,3fr) minmax(0,1fr);column-gap:24px}
.layout>.card{grid-column:1}.layout>.aside{grid-column:2}.layout>.wide{grid-column:1/-1}
.running-head{background:#171612;color:#fffdf7;padding:12px;border-bottom:3px solid #a48c49}.hero{border-bottom-color:#82671c}
""",
        "concept_b": """
:root{--ink:#111;--paper:#fff;--accent:#111;--rule:#111;--wash:#eee;--body:Arial,sans-serif;--heading:Arial,sans-serif}
.layout{grid-template-columns:repeat(12,minmax(0,1fr));gap:16px}
.layout>.card{grid-column:span 6}.layout>.aside{grid-column:span 4}.layout>.wide,.layout>.hero,.layout>.plate,.layout>.table-wrap{grid-column:1/-1}
.card{border-top:3px solid #111}.page-title{font-weight:900;letter-spacing:-.045em;text-transform:uppercase}.hero{border-bottom-width:8px}.chapter-numeral{font-size:96px}
""",
        "concept_c": """
:root{--ink:#202a2d;--paper:#fbfcfa;--accent:#3e6264;--rule:#a5b4b3;--wash:#edf2f0;--body:Georgia,serif;--heading:Arial,sans-serif}
.layout{grid-template-columns:repeat(3,minmax(0,1fr));gap:18px}
.layout>.card{grid-column:span 2}.layout>.aside{grid-column:span 1}.layout>.wide,.layout>.hero,.layout>.plate,.layout>.table-wrap{grid-column:1/-1}
.running-head{font-family:monospace}.card{border-top-width:1px}.page-title{font-weight:500;letter-spacing:-.02em}.aside{font-family:Arial,sans-serif}.deck{font-size:18px}
""",
    }
    if concept_id not in styles:
        raise ValueError("Unknown concept_id: " + str(concept_id))
    return _BASE_CSS + styles[concept_id]


def _chapter_opener(c, m, number):
    hero = '<section class="hero"><div class="chapter-numeral">' + f"{number:02d}" + '</div><p class="deck">' + _e(_field(c, m, "subtitle", "Chapter orientation")) + "</p></section>"
    brief = _field(c, m, "executive_summary") or _field(c, m, "summary") or _field(c, m, "body")
    metrics = _field(c, m, "key_metrics")
    headings = [section.get("heading", "Chapter section") if isinstance(section, dict) else section for section in _sections(c)]
    return hero + _card("The brief", _paragraphs(brief)) + _card("Key metrics", _metrics(metrics) if metrics else _list(_field(c, m, "learning_objectives")), "aside") + _card("Chapter sections", _list(headings, True) + _quote(_field(c, m, "pull_quote")), "wide")


def _executive_summary(c, m, number):
    body = _card("Executive brief", _paragraphs(_field(c, m, "executive_summary") or _field(c, m, "summary")), "hero")
    findings = _field(c, m, "key_takeaways")
    body += _card("Key findings", _list(findings)) if findings is not None else _section_cards(c)
    decision = _field(c, m, "decision")
    body += _card("Decision required", _paragraphs(decision), "aside") if decision is not None else _card("Key metrics", _metrics(_field(c, m, "key_metrics")), "aside")
    return body + _card("Recommended next moves", _list(_field(c, m, "recommendations", _field(c, m, "action_checklist")), True), "wide")


def _opportunity_overview(c, m, number):
    body = _card("Opportunity thesis", _paragraphs(_field(c, m, "opportunity", _field(c, m, "executive_summary") or _field(c, m, "summary"))), "hero")
    demand = _field(c, m, "demand_signals")
    body += _card("Demand and evidence", _list(demand)) if demand is not None else _section_cards(c)
    body += _card("Qualification gate", _list(_field(c, m, "qualification_criteria", _field(c, m, "action_checklist"))), "aside")
    access = _field(c, m, "access_path")
    if access is not None:
        body += _card("Access path", _paragraphs(access))
    risks = _field(c, m, "risks")
    body += _card("Constraints", _list(risks), "aside") if risks is not None else _card("Key metrics", _metrics(_field(c, m, "key_metrics")), "aside")
    return body


def _step_by_step_sop(c, m, number):
    sequence_steps = _field(c, m, "steps")
    if sequence_steps is None:
        sequence_steps = c.get("sop_steps")
    if sequence_steps is None:
        sequence = "".join("<h3>" + _e(section.get("heading", "Execution stage")) + "</h3>" + _steps(_sop_entries(section)) for section in _sections(c) if isinstance(section, dict) and _sop_entries(section))
        return _card("Execution sequence", sequence or _p(None), "wide") + _card("Inputs & prerequisites", _list(_field(c, m, "prerequisites", _field(c, m, "action_checklist")))) + _card("Stop / escalate", _list(_field(c, m, "stop_conditions", _field(c, m, "action_checklist"))), "aside") + _section_cards(c, include_steps=False)
    steps = []
    for index, item in enumerate(_items(sequence_steps), 1):
        item = item if isinstance(item, dict) else {"action": item}
        text = "<h3>" + _e(item.get("title", "Step " + str(index))) + "</h3>" + _step_body(item)
        text += _p(item.get("acceptance_criteria"), "Acceptance criteria not supplied.")
        steps.append('<div class="step"><span class="step-number">' + str(index) + "</span><div>" + text + "</div></div>")
    return _card("Execution sequence", "".join(steps) or _p(None), "wide") + _card("Inputs & prerequisites", _list(_field(c, m, "prerequisites"))) + _card("Stop / escalate", _list(_field(c, m, "stop_conditions")), "aside")


def _expert_insights(c, m, number):
    if _field(c, m, "expert_insights") is None:
        return _card("Expert perspective", _quote(_field(c, m, "pull_quote")), "hero") + _section_cards(c) + _card("Source citations", _citations(_field(c, m, "source_citations")), "wide")
    panels = []
    for item in _items(_field(c, m, "expert_insights")):
        item = item if isinstance(item, dict) else {"insight": item}
        quote = item.get("quote")
        body = "<blockquote>" + _p(quote) + "<cite>" + _e(item.get("expert", item.get("author", "Attribution not supplied"))) + "</cite></blockquote>" if quote else _p(item.get("insight"))
        body += "<h3>Corroborating evidence</h3>" + _citations(item.get("sources"))
        body += _paragraphs(item.get("corroboration"))
        panels.append(_card(item.get("title", "Expert observation"), body))
    return "".join(panels) or _card("Expert observations", _p(None))


def _financial_breakdown(c, m, number):
    if _field(c, m, "financials") is None:
        return _first_table(c) + _section_cards(c, skip_first_table=True) + _card("Key metrics", _metrics(_field(c, m, "key_metrics")), "aside")
    rows = _rows(_field(c, m, "financials"), ["item", "amount", "basis", "source"])
    return _table(["Line item", "Amount / unit", "Assumption basis", "Source"], rows, "Unit-economics ledger — supplied values") + _card("Model assumptions", _list(_field(c, m, "financial_assumptions"))) + _card("Sensitivity", _p(_field(c, m, "sensitivity")), "aside") + _card("Interpretation", _p(_field(c, m, "financial_summary")), "wide")


def _case_study_walkthrough(c, m, number):
    if _field(c, m, "case_study") is None:
        return _card("Case study brief", _paragraphs(_field(c, m, "executive_summary") or _field(c, m, "summary")), "hero") + _section_cards(c) + _card("Action checklist", _checklist(_field(c, m, "action_checklist")), "wide")
    case = _field(c, m, "case_study", {})
    case = case if isinstance(case, dict) else {"summary": case}
    return _card("Illustrative case", _p(case.get("summary")), "hero") + _card("Starting position", _p(case.get("starting_position"))) + _card("Constraints", _list(case.get("constraints")), "aside") + _card("Decision trail", _list(case.get("steps"), True), "wide") + _card("Outcome & lessons", _p(case.get("outcome")) + _list(case.get("lessons"))) + _card("Evidence limits", _p(case.get("limitations")), "aside")


def _comparison_table(c, m, number):
    if _field(c, m, "comparison") is None:
        return _first_table(c) + _section_cards(c, skip_first_table=True) + _card("Key metrics", _metrics(_field(c, m, "key_metrics")), "aside")
    comparison = _field(c, m, "comparison", {})
    if not isinstance(comparison, dict):
        comparison = {"rows": comparison}
    headers = comparison.get("headers", ["Criterion", "Option A", "Option B", "Evidence"])
    if not isinstance(headers, (list, tuple)) or not headers:
        headers = ["Criterion", "Option A", "Option B", "Evidence"]
    keys = comparison.get("keys", ["criterion", "option_a", "option_b", "evidence"])
    if not isinstance(keys, (list, tuple)) or len(keys) != len(headers):
        keys = [str(h) for h in headers]
    return _table(headers, _rows(comparison.get("rows"), keys), comparison.get("caption", "Structured comparison matrix")) + _card("Decision rule", _p(comparison.get("decision_rule")), "wide")


def _research_exhibit(c, m, number, diagrams, concept_id):
    plates = []
    for index, diagram in enumerate(diagrams, 1):
        if not isinstance(diagram, dict):
            raise TypeError("Every diagram must be a dict")
        svg = render_diagram_svg(diagram, concept_id)
        title = diagram.get("title", "Research exhibit " + str(index))
        caption = diagram.get("caption") or diagram.get("subtitle") or diagram.get("source", "Structured data plate")
        plates.append('<figure class="plate" aria-label="' + _e(title) + '">' + svg + "<figcaption>" + _e(title) + " — " + _e(caption) + "</figcaption></figure>")
        description = _paragraphs(diagram.get("description") or diagram.get("assumptions_note"))
        stages = []
        for stage in _items(diagram.get("stages")):
            if isinstance(stage, dict):
                text = _text(stage.get("label", ""))
                if stage.get("value") is not None:
                    text += " (" + _text(stage["value"]) + ")"
                if stage.get("detail"):
                    text += " — " + _text(stage["detail"])
                stages.append(text)
            else:
                stages.append(stage)
        data = stages or diagram.get("data", diagram.get("nodes"))
        if data:
            description += _list(data)
        plates.append(_card("Exhibit description / accessible data", description, "wide"))
    body = "".join(plates) or _card("Research plate", _p(None, "No diagrams supplied."), "wide")
    method = _paragraphs(_field(c, m, "research_method"))
    if _field(c, m, "research_limitations"):
        method += _list(_field(c, m, "research_limitations"))
    return body + (_card("Method & limitations", method, "wide") if method else "") + _section_cards(c)


def _legal_compliance_notes(c, m, number):
    notes = _field(c, m, "legal_notes")
    body = _card("Jurisdiction controls", _paragraphs(_field(c, m, "executive_summary") or _field(c, m, "summary")), "hero")
    if notes is None:
        body += _table(["Authority", "Relevance", "Source"], _rows(_field(c, m, "statutory_citations", []), ["title", "relevance", "url"]), "Statutory verification register", link_columns=(2,)) + _section_cards(c)
    else:
        body += _table(["Jurisdiction", "Requirement", "Authority", "Checked on"], _rows(notes, ["jurisdiction", "requirement", "authority", "verified_date"]), "Statutory verification register")
    if _field(c, m, "legal_escalations") is not None:
        body += _card("Escalation points", _list(_field(c, m, "legal_escalations")), "wide")
    return body


def _resource_directory(c, m, number):
    if _field(c, m, "resources") is None:
        cards = []
        for item in _chapter_citations(c, m):
            if isinstance(item, dict):
                details = {key: value for key, value in item.items() if key not in {"title", "name"}}
                cards.append(_card(item.get("title", item.get("name", "Resource")), _citation_body(details)))
            else:
                cards.append(_card("Resource", _citation_body(item)))
        return "".join(cards) + _section_cards(c) or _card("Public records & tools", _p(None), "wide")
    cards = []
    for item in _items(_field(c, m, "resources")):
        item = item if isinstance(item, dict) else {"name": item}
        url = _text(item.get("url", "")).strip()
        link = '<p><a href="' + _e(url) + '">' + _e(url) + "</a></p>" if url.lower().startswith(("https://", "http://")) else _p(url, "URL not supplied.")
        body = _p(item.get("purpose", item.get("description"))) + link
        body += "<h3>Coverage / access</h3>" + _p(item.get("coverage")) + _p(item.get("access"))
        cards.append(_card(item.get("name", "Resource"), body))
    return "".join(cards) or _card("Public records & tools", _p(None), "wide")


def _action_checklist(c, m, number):
    entries = _field(c, m, "checklist", _field(c, m, "action_items", _field(c, m, "action_checklist")))
    evidence = _field(c, m, "completion_evidence")
    benchmarks = _list(evidence) if evidence is not None else _metrics(_field(c, m, "key_metrics"))
    return _card("Operator completion record", _checklist(entries), "wide") + _card("Completion evidence", benchmarks) + _card("Sign-off", _p(_field(c, m, "signoff"), "Owner: __________________\nDate: __________________"), "aside")


def _thirty_day_plan(c, m, number):
    if _field(c, m, "thirty_day_plan") is None:
        stages = "".join("<li>" + _section_html(section) + "</li>" for section in _sections(c))
        body = _card("30-day implementation sequence", '<ol class="timeline">' + stages + "</ol>", "wide")
        body += _card("Action checklist", _checklist(_field(c, m, "action_checklist")), "wide")
        if _field(c, m, "dependencies") is not None:
            body += _card("Dependencies", _list(_field(c, m, "dependencies")))
        if _field(c, m, "review_cadence") is not None:
            body += _card("Review cadence", _paragraphs(_field(c, m, "review_cadence")), "aside")
        return body
    plan = _items(_field(c, m, "thirty_day_plan"))
    stages = []
    for index, item in enumerate(plan, 1):
        item = item if isinstance(item, dict) else {"actions": item}
        stages.append("<li><h3>" + _e(item.get("days", item.get("period", "Stage " + str(index)))) + "</h3>" + _list(item.get("actions")) + "<h3>Deliverable / gate</h3>" + _p(item.get("deliverable")) + _p(item.get("gate")) + "</li>")
    body = '<ol class="timeline">' + "".join(stages) + "</ol>" if stages else _p(None, "No implementation schedule supplied. Assign actions and gates for days 1–30 before execution.")
    return _card("30-day implementation sequence", body, "wide") + _card("Dependencies", _list(_field(c, m, "dependencies"))) + _card("Review cadence", _p(_field(c, m, "review_cadence")), "aside")


def _assessment(value):
    if isinstance(value, dict):
        if "low" in value or "lower" in value:
            low = value.get("low", value.get("lower"))
            high = value.get("high", value.get("upper"))
            return _text(low) + "–" + _text(high)
        return "\n".join(str(key).replace("_", " ").capitalize() + ": " + _assessment(item) for key, item in value.items())
    if isinstance(value, (list, tuple)):
        return "\n".join(_assessment(item) for item in value)
    return _text(value)


def _dimension_summary(scorecard):
    dimensions = scorecard.get("dimensions", scorecard.get("scores", scorecard.get("sub_scores", scorecard.get("subscores", {}))))
    records = dimensions.items() if isinstance(dimensions, dict) else enumerate(_items(dimensions), 1)
    maxima = scorecard.get("dimension_max", {})
    lines = []
    for name, item in records:
        label = str(name).replace("_", " ").title()
        maximum = maxima.get(name) if isinstance(maxima, dict) else None
        if isinstance(item, dict):
            label = item.get("label", item.get("name", label))
            score = item.get("score", item.get("value"))
            maximum = item.get("max_score", item.get("max", maximum))
        else:
            score = item
        line = _text(label) + ": " + _text(score)
        if maximum is not None:
            line += " / " + _text(maximum)
        lines.append(line)
    return "\n".join(lines)


def _scorecard_page(c, m, number, scorecard, concept_id):
    svg = render_scorecard_svg(scorecard, concept_id)
    plate = '<figure class="plate" aria-label="Money-to-Manpower Score">' + svg + '<figcaption>Money-to-Manpower Score — assessment overview.</figcaption></figure>'
    confidence = _assessment(scorecard.get("evidence_confidence", scorecard.get("confidence")))
    band = _assessment(scorecard.get("uncertainty_band", scorecard.get("uncertainty")))
    bounds = _assessment(scorecard.get("uncertainty_bounds"))
    resolved_score = resolve_score_value(scorecard, default=None)
    data = [
        ["Total Score", resolved_score],
        ["Tier", scorecard.get("tier_label", scorecard.get("tier"))],
        ["Confidence & Uncertainty Band", " · ".join(value for value in (confidence, band, bounds) if value)],
        ["Dimensions", _dimension_summary(scorecard)],
        ["Scenarios", _assessment(scorecard.get("scenarios"))],
    ]
    body = plate + _table(["Field", "Supplied assessment"], data, "Accessible scorecard data")
    method = _paragraphs(scorecard.get("methodology")) + _paragraphs(scorecard.get("limitations")) + _paragraphs(scorecard.get("uncertainty_note"))
    if method:
        body += _card("Scoring method & uncertainty", method, "wide")
    if scorecard.get("key_risks"):
        body += _card("Key risks", _list(scorecard["key_risks"]), "wide")
    return body


_RENDERERS = {
    "chapter_opener": _chapter_opener,
    "executive_summary": _executive_summary,
    "opportunity_overview": _opportunity_overview,
    "step_by_step_sop": _step_by_step_sop,
    "expert_insights": _expert_insights,
    "financial_breakdown": _financial_breakdown,
    "case_study_walkthrough": _case_study_walkthrough,
    "comparison_table": _comparison_table,
    "legal_compliance_notes": _legal_compliance_notes,
    "resource_directory": _resource_directory,
    "action_checklist": _action_checklist,
    "thirty_day_plan": _thirty_day_plan,
}


def _guides():
    return '<div aria-hidden="true"><div class="guide bleed"><span class="guide-label">BLEED · 0.125 in</span></div><div class="guide trim-guide"><span class="guide-label" style="right:0;bottom:0">TRIM · 6 × 9 in</span></div><div class="guide gutter"><span class="guide-label">GUTTER · 0.75 in</span></div><div class="guide crop"></div></div>'


def _sheet(content, title, book_title, label, number, side, guides=False):
    head = '<header class="running-head"><span>' + _e(book_title) + '</span><span>Chapter ' + _e(number) + "</span></header>"
    foot = '<footer class="folio"><span>' + _e(label) + '</span><span>' + _e(side) + "</span></footer>"
    heading = '<h1 class="page-title">' + _e(title) + "</h1>" if side == "recto" else '<h2 class="page-title">' + _e(title) + "</h2>"
    return '<article class="sheet ' + side + '">' + (_guides() if guides else "") + '<div class="trim">' + head + heading + content + foot + "</div></article>"


def render_interior_page_html(
    template_id: str,
    concept_id: str,
    manuscript: dict,
    scorecard: dict,
    diagrams: list[dict],
    chapter_number: int | None = None,
    viewport_mode: str = "desktop",
    show_print_guides: bool = False,
) -> str:
    """Render an editorial proof, not a paginated production PDF.

    Manuscript fields may live at book or chapter level; chapter fields win.
    SVG siblings are trusted renderers with (data, concept_id) signatures.
    Desktop uses facing content/evidence leaves; tablet uses one continuous
    reader page. Print uses mirrored 6-by-9-inch minimum-height proof sheets.
    Overset content flows without clipping and needs production pagination.
    """
    if isinstance(template_id, dict):
        template_id = template_id.get("template_id", template_id.get("id", ""))
    metadata = next((t for t in INTERIOR_TEMPLATES if t["template_id"] == template_id), None)
    if metadata is None:
        raise ValueError("Unknown template_id: " + str(template_id))
    if viewport_mode not in {"desktop", "tablet", "print"}:
        raise ValueError("Unknown viewport_mode: " + str(viewport_mode))
    if not isinstance(manuscript, dict) or not isinstance(scorecard, dict):
        raise TypeError("manuscript and scorecard must be dicts")
    if not isinstance(diagrams, list):
        raise TypeError("diagrams must be a list")
    number = metadata["default_chapter"] if chapter_number is None else chapter_number
    if isinstance(number, bool) or not isinstance(number, int) or number < 1:
        raise ValueError("chapter_number must be a positive integer")
    css = _concept_css(concept_id)
    concept = get_concept(concept_id)
    concept_name = concept.get("name", concept.get("label", concept_id)) if isinstance(concept, dict) else concept_id
    chapter = _chapter(manuscript, number)
    title = chapter.get("title") or metadata["label"].split(". ", 1)[1]
    book_title = manuscript.get("title", "Editorial field manual")
    if template_id == "research_exhibit":
        body = _research_exhibit(chapter, manuscript, number, diagrams, concept_id)
    elif template_id == "scorecard_page":
        body = _scorecard_page(chapter, manuscript, number, scorecard, concept_id)
    else:
        body = _RENDERERS[template_id](chapter, manuscript, number)
    label = metadata["label"]
    content = '<div class="kicker">' + _e(label) + '</div><div class="layout">' + body + "</div>"
    sources = _field(chapter, manuscript, "sources")
    evidence = _card("Source register", _citations(sources if sources is not None else _chapter_citations(chapter, manuscript)), "wide")
    notes = _field(chapter, manuscript, "editorial_notes")
    evidence += _card("Key metrics & callouts", _paragraphs(notes) if notes is not None else _metrics(_field(chapter, manuscript, "key_metrics")), "wide")
    metadata_text = f'Template: {template_id} · Reading time: {chapter.get("reading_time_minutes", 4)} min'
    evidence += _card("Editorial metadata", _p(_field(chapter, manuscript, "verification_status"), metadata_text), "wide")
    evidence = '<div class="layout evidence-register">' + evidence + "</div>"
    guides = viewport_mode == "print" and show_print_guides
    if viewport_mode == "tablet":
        content += '<section class="continuation"><h2>Evidence & notes</h2>' + evidence + "</section>"
    sheets = _sheet(content, title, book_title, label, number, "recto", guides)
    if viewport_mode != "tablet":
        sheets += _sheet(evidence, "Evidence & notes", book_title, label, number, "verso", guides)
    page_size = "6.25in 9.25in" if guides else "6in 9in"
    css += "\n@page{size:" + page_size + ";margin:0}"
    classes = viewport_mode + (" guides" if guides else "") + " " + concept_id
    document = '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>' + _e(title) + " — " + _e(book_title) + "</title><style>" + css + '</style></head><body class="' + classes + '"><main class="reader" aria-label="' + _e(concept_name) + '"><div class="spread">' + sheets + "</div></main></body></html>"
    return document.replace("Money-to-Manpower Score" + chr(0x2122), "Money-to-Manpower Score").replace("Money-to-Manpower Score" + chr(0x00AE), "Money-to-Manpower Score")
