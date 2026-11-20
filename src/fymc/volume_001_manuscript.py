from __future__ import annotations

from copy import deepcopy
from .scorecard_engine import get_candidate_track_metadata
from .vol001_q01_02 import CHAPTERS_1_TO_2
from .vol001_q03_04 import CHAPTERS_3_TO_4
from .vol001_q05_06 import CHAPTERS_5_TO_6
from .volume_001_chapters_b import CHAPTERS_7_TO_12, build_volume_001_workbook


def build_volume_001_diagrams_data() -> list[dict]:
    """Return fresh, renderer-neutral data; examples are not market benchmarks."""
    specs = [
        ("diag-01-end-to-end-workflow", "process_flow", "From lead to documented recovery", "Five gates, not a promise of payment", 1,
         "operating_framework", "Ordinal numeric values indicate sequence, not elapsed time or success probability.",
         "Identify the legal lane before researching relatives or offering a recovery contract.", [
             ("Classify", "Gate 1", 1.0, "Separate probate, custodial unclaimed property and sale surplus."),
             ("Qualify", "Gate 2", 2.0, "Verify the record, claimant eligibility, deadlines and likely net value."),
             ("Prove", "Gate 3", 3.0, "Build a sourced relationship chain and resolve contradictory records."),
             ("Authorize", "Gate 4", 4.0, "Obtain lawful consent and locally reviewed contractual authority."),
             ("Resolve", "Gate 5", 5.0, "Submit through the authorized channel and reconcile actual distributions.")]),
        ("diag-02-deal-funnel", "funnel", "A qualification funnel worth measuring", "Illustrative cohort of 100 records", 6,
         "illustrative_model", "Invented nested cohort; these counts are not observed conversion rates or a forecast.",
         "Measure why records leave each gate; signed clients and completed distributions are different outcomes.", [
             ("Records screened", "100", 100.0, "Deduplicated records with identifiable custodians or case numbers."),
             ("Plausible net value", "30", 30.0, "Illustrative survivors after preliminary eligibility and liability checks."),
             ("Evidence feasible", "12", 12.0, "A credible document path exists within a defined research budget."),
             ("Authorized clients", "4", 4.0, "Eligible claimants choose assistance under lawful agreements."),
             ("Paid resolutions", "2", 2.0, "Actual collected fees, potentially many months after intake.")]),
        ("diag-03-fee-waterfall", "waterfall", "What remains of a collected fee", "Business contribution, not the estate distribution", 3,
         "illustrative_model", "USD; first and last bars are totals, middle bars are signed deductions. Assumed lawful fee is $6,000 on $60,000 recovered.",
         "A $6,000 fee less $1,200 records, $800 review and $1,000 allocated acquisition leaves $3,000 before overhead, owner pay and tax.", [
             ("Collected fee", "$6,000", 6000.0, "Opening total: a hypothetical 10% fee, only if lawful for this claim."),
             ("Records and research", "-$1,200", -1200.0, "Direct evidence costs, including paid research labor."),
             ("Professional review", "-$800", -800.0, "Business-paid review; not an asserted statutory charge."),
             ("Acquisition allocation", "-$1,000", -1000.0, "Allocated costs include unsuccessful leads, not just this winner."),
             ("Contribution", "$3,000", 3000.0, "Closing total, not an additional movement and not owner net profit.")]),
        ("diag-04-jurisdiction-fee-caps", "horizontal_bars", "Fee-cap sensitivity before choosing a market", "Hypothetical legal ceilings, not a state-law comparison", 2,
         "illustrative_model", "Percent of a $40,000 recovery. A-D are hypothetical jurisdictions; no bar states an actual legal limit. Replace only after current legal review.",
         "Identical recoveries can support different maximum fees; timing restrictions can make an agreement unavailable regardless of percentage.", [
             ("Hypothetical A", "5% / $2,000", 5.0, "Assumed ceiling only; agreement eligibility still requires review."),
             ("Hypothetical B", "10% / $4,000", 10.0, "Assumed ceiling, not a recommendation to charge the maximum."),
             ("Hypothetical C", "15% / $6,000", 15.0, "Assumed ceiling; the allowable compensation base may differ."),
             ("Hypothetical D", "20% / $8,000", 20.0, "Assumed ceiling; expense reimbursement can also be regulated.")]),
        ("diag-05-kinship-decision-tree", "decision_tree", "Build proof before naming an heir", "A research triage tree, not a distribution formula", 7,
         "operating_framework", "Numeric values identify nodes. Edges are stated in detail; local law decides succession, representation and shares.",
         "Relationship evidence supports legal analysis; it does not replace a court's finding of entitlement.", [
             ("Governing instrument?", "Node 1", 1.0, "Valid will or trust: follow counsel's instrument analysis; otherwise continue to node 2."),
             ("Spouse or descendants?", "Node 2", 2.0, "Yes: document and refer for allocation; no: continue to node 3. Spousal rights may coexist with descendants."),
             ("Parents or collateral kin?", "Node 3", 3.0, "Yes: prove each link and refer for statutory priority; no or uncertain: continue to node 4."),
             ("Evidence unresolved?", "Node 4", 4.0, "Stop distribution assumptions; obtain missing records and counsel's direction on further classes or escheat.")]),
        ("diag-06-small-team-org", "org_architecture", "Separate research, review and client care", "Roles may be fractional; authority must remain distinct", 9,
         "operating_framework", "Numeric values are role identifiers, not headcounts, hierarchy ranks or compensation.",
         "The owner coordinates researchers and client care; independent licensed advisers retain professional judgment.", [
             ("Owner / case lead", "Role 1", 1.0, "Accountable for intake gates, budgets and secure case access."),
             ("Research specialist", "Role 2", 2.0, "Reports case evidence to the lead; does not decide legal entitlement."),
             ("Client coordinator", "Role 3", 3.0, "Reports to the lead; tracks consent, requests and plain-language updates."),
             ("Independent counsel", "Role 4", 4.0, "Advises within a separate engagement; not controlled by a research sales target.")]),
        ("diag-07-startup-budget-stack", "stacked_comparison", "A lean pilot's startup cash stack", "Compare cost composition, not promised earnings", 4,
         "illustrative_model", "USD; one scenario with four additive components totaling $5,000. This is not a vendor quote or paired market comparison; living expenses are excluded.",
         "Keep a reserve for failed cases and delays; a cheap subscription does not make the business fully funded.", [
             ("Setup and review", "$1,500", 1500.0, "Illustrative formation, contract review and insurance allowance; obtain actual quotes."),
             ("Research tools", "$600", 600.0, "Illustrative three-month subscriptions and basic secure working tools."),
             ("Pilot case costs", "$900", 900.0, "Illustrative records, postage and limited paid research."),
             ("Business reserve", "$2,000", 2000.0, "Uncommitted buffer; owner living costs and taxes require a separate plan.")]),
        ("diag-08-30-day-roadmap", "timeline_roadmap", "Thirty days to a controlled pilot", "Readiness milestones, not a collection deadline", 12,
         "operating_framework", "Numeric values are milestone end-days; ranges are calendar targets, not statutory deadlines.",
         "The first month should produce a reviewable process and documented cases, not an unsupported income promise.", [
             ("Choose the lane", "Days 1-7", 7.0, "Select one jurisdiction, custodian and claim type; get legal gates reviewed."),
             ("Build the controls", "Days 8-14", 14.0, "Set record provenance, privacy, case budgets and written stop rules."),
             ("Run a small cohort", "Days 15-21", 21.0, "Screen a bounded batch and build evidence only for qualified leads."),
             ("Review and decide", "Days 22-30", 30.0, "Audit economics and compliance; continue, redesign or stop the pilot.")]),
    ]
    return [dict(diagram_id=identifier, chart_type=kind, title=title, subtitle=subtitle,
                 chapter_number=chapter, epistemic_tag=tag, assumptions_note=note, caption=caption,
                 stages=[dict(label=label, value=value, numeric_value=float(number), detail=detail)
                         for label, value, number, detail in stages])
            for identifier, kind, title, subtitle, chapter, tag, note, caption, stages in specs]


CHAPTERS_1_TO_6 = CHAPTERS_1_TO_2 + CHAPTERS_3_TO_4 + CHAPTERS_5_TO_6


def compute_manuscript_word_count(chapters: list[dict] | None) -> int:
    """Compute prose word count across chapter content, excluding IDs and URLs."""
    import re

    def prose_words(value):
        if isinstance(value, str):
            return len(re.findall(r"\b[\w]+(?:['-][\w]+)*\b", value))
        if isinstance(value, (list, tuple)):
            return sum(prose_words(item) for item in value)
        if isinstance(value, dict):
            excluded = {"id", "chapter_id", "slug", "diagram_id", "layout_template", "epistemic_status",
                        "source_type", "url", "video_id", "timestamp_label", "markdown"}
            return sum(prose_words(item) for key, item in value.items() if key not in excluded)
        return 0

    return sum(
        prose_words({key: chapter.get(key) for key in (
            "title", "subtitle", "executive_summary", "key_metrics", "sections", "pull_quote",
            "action_checklist", "statutory_citations", "source_citations")})
        for chapter in (chapters or []) if isinstance(chapter, dict)
    )


def build_volume_001_manuscript(abridged_videos: list[dict] | None = None) -> dict:
    """Build an isolated manuscript with matched, attributed video references.

    Video commentary is not statutory authority. Untimed or unmatchable tips are
    omitted rather than assigned invented timestamps or unrelated chapter claims.
    """
    import math
    import re
    from urllib.parse import parse_qs, urlparse
    from . import (
        MIN_EXPERT_YOUTUBE_LINKS_PER_BOOK,
        TARGET_EXPERT_YOUTUBE_LINKS_PER_BOOK,
        MIN_EXPERT_YOUTUBE_LINKS_PER_CHAPTER,
        count_manuscript_youtube_links,
    )
    from .volume_001_citations import (
        BASELINE_EXPERT_CITATIONS_BY_CHAPTER,
        CHAPTER_KEYWORDS,
    )

    chapters = deepcopy(CHAPTERS_1_TO_6 + CHAPTERS_7_TO_12)
    for ch in chapters:
        ch.setdefault("id", f"Q{ch['chapter_number']}")
        ch.setdefault("chapter_id", f"Q{ch['chapter_number']}")
    keywords = CHAPTER_KEYWORDS

    def seconds_of(value):
        if value is None or isinstance(value, bool):
            return None
        try:
            if isinstance(value, str) and ":" in value:
                parts = value.strip().strip("[]").split(":")
                if len(parts) not in (2, 3):
                    return None
                parts = [float(part) for part in parts]
                if any(not math.isfinite(part) or part < 0 for part in parts):
                    return None
                if any(part >= 60 for part in parts[1:]):
                    return None
                seconds = sum(part * 60 ** index for index, part in enumerate(reversed(parts)))
            else:
                seconds = float(value)
            return int(seconds) if math.isfinite(seconds) and seconds >= 0 else None
        except (ValueError, TypeError, OverflowError):
            return None

    for chapter in chapters:
        chapter["source_citations"] = []
    _dangling_tail = {
        "a", "about", "after", "although", "am", "an", "and", "any", "are", "as", "at",
        "be", "because", "been", "before", "being", "between", "both", "but", "by", "can",
        "could", "did", "do", "does", "doing", "during", "each", "either", "for", "from",
        "get", "getting", "go", "going", "had", "has", "have", "having", "he", "her", "his",
        "how", "i", "i'll", "i'm", "i've", "if", "in", "into", "is", "it", "it's", "its",
        "just", "like", "make", "many", "may", "might", "more", "most", "much", "must", "my",
        "need", "no", "nor", "not", "of", "on", "onto", "or", "other", "our", "over", "put",
        "really", "same", "say", "saying", "see", "she", "should", "since", "so", "some",
        "still", "such", "than", "that", "that's", "the", "their", "them", "then", "there",
        "these", "they", "they're", "this", "those", "though", "through", "to", "too",
        "under", "unless", "until", "up", "upon", "very", "want", "was", "we", "we'll",
        "we're", "were", "what", "when", "where", "whether", "which", "while", "who", "whom",
        "whose", "why", "will", "with", "within", "without", "would", "you", "you'll",
        "you're", "your",
    }

    def polish_excerpt(raw_text: str) -> str:
        cleaned = re.sub(r"\s+", " ", str(raw_text or "")).strip()
        if not cleaned:
            return ""
        if (
            "|" not in cleaned
            and not re.search(r"\b\d+:\d{2}(?::\d{2})?(?:\.\d+)?\s*S\d+\b", cleaned)
            and re.search(r'[.!?]["\')\]]*$', cleaned)
        ):
            return cleaned
        cleaned = re.sub(r"\b\d+:\d{2}(?::\d{2})?(?:\.\d+)?\s*S\d+\b", "", cleaned).strip()
        if "|" in cleaned:
            parts = [p.strip() for p in cleaned.split("|") if p.strip()]
            cleaned = parts[0] if parts and len(parts[0]) >= 50 else ". ".join(parts)
        was_char_clipped = len(raw_text or "") in range(215, 226) or len(raw_text or "") >= 455
        if was_char_clipped and not re.search(r'[.!?]["\')\]]*$', cleaned):
            # Drop potentially mid-word clipped final token before sentence/clause trim
            cleaned = re.sub(r"\s+\S+$", "", cleaned).strip()
        matches = list(re.finditer(r'[.!?]["\')\]]*(?=\s|$)', cleaned))
        if matches and matches[-1].end() >= 55:
            cleaned = cleaned[: matches[-1].end()].strip()
        if not re.search(r'[.!?]["\')\]]*$', cleaned):
            tokens_list = cleaned.split()
            while len(tokens_list) > 6:
                last_word = re.sub(r"^[^A-Za-z0-9']+|[^A-Za-z0-9']+$", "", tokens_list[-1]).lower()
                if not last_word or (not any(ch.isdigit() for ch in last_word) and (last_word in _dangling_tail or len(last_word) <= 1)):
                    tokens_list.pop()
                else:
                    break
            cleaned = " ".join(tokens_list).rstrip(",;:- ")
            if cleaned and cleaned[-1] not in ".!?":
                cleaned += "."
        if cleaned and cleaned[0].isalpha() and cleaned[0].islower():
            cleaned = cleaned[0].upper() + cleaned[1:]
        return cleaned

    valid_videos = [v for v in (abridged_videos or []) if isinstance(v, dict)]
    large_corpus = len(valid_videos) > 20
    for video in valid_videos:
        video_id = str(video.get("video_id") or "")
        if not re.fullmatch(r"[A-Za-z0-9_-]{11}", video_id):
            try:
                parsed = urlparse(str(video.get("url") or video.get("video_url") or ""))
                host = (parsed.hostname or "").lower()
                if host in {"youtube.com", "www.youtube.com", "m.youtube.com"}:
                    video_id = parse_qs(parsed.query).get("v", [""])[0]
                    if not video_id and parsed.path.startswith(("/shorts/", "/embed/", "/live/")):
                        video_id = parsed.path.split("/")[2]
                elif host == "youtu.be":
                    video_id = parsed.path.strip("/").split("/")[0]
            except ValueError:
                continue
        if not re.fullmatch(r"[A-Za-z0-9_-]{11}", video_id):
            continue
        tips = []
        for key in ("pro_tips", "tips", "key_points"):
            items = video.get(key)
            if isinstance(items, list):
                tips.extend(items)
        for tip in tips:
            if not isinstance(tip, dict):
                continue
            raw_tip_text = str(tip.get("text") or tip.get("tip") or tip.get("summary") or "").strip()
            text = polish_excerpt(raw_tip_text) if large_corpus else raw_tip_text
            seconds = None
            for key in ("timestamp", "start", "start_seconds", "timestamp_seconds"):
                seconds = seconds_of(tip.get(key))
                if seconds is not None:
                    break
            if not text or seconds is None:
                continue
            explicit = tip.get("chapter_number", tip.get("question_number"))
            if explicit is not None:
                explicit = str(explicit).upper().removeprefix("Q")
            tokens = set(re.findall(r"[a-z]+", text.lower()))
            scores = []
            for chapter in chapters:
                number = chapter["chapter_number"]
                chapter_tokens = set(re.findall(r"[a-z]+", str(chapter.get("title", "")).lower()))
                chapter_tokens -= {"the", "a", "an", "is", "to", "of", "and", "in", "for", "what", "how", "your", "with", "who", "why", "where"}
                scores.append((len(tokens & (keywords.get(number, set()) | chapter_tokens)), number))
            best_score = max((score for score, number in scores), default=0)
            targets = ({number for score, number in scores if str(number) == explicit}
                       if explicit is not None else {number for score, number in scores if score == best_score and score > 0})
            label = f"{seconds // 3600:02d}:{seconds % 3600 // 60:02d}:{seconds % 60:02d}"
            url = f"https://www.youtube.com/watch?v={video_id}&t={seconds}s"
            channel_name = str(
                video.get("channel")
                or video.get("channel_title")
                or video.get("author")
                or (video.get("metadata") or {}).get("author")
                or "Independent Practitioner"
            ).strip()
            citation = dict(source_type="video_pro_tip", video_id=video_id,
                            title=str(video.get("title") or (video.get("metadata") or {}).get("title") or video_id),
                            channel=channel_name,
                            author=channel_name,
                            text=text, tip=text,
                            timestamp=seconds, timestamp_seconds=seconds, timestamp_label=f"[{label}]",
                            url=url, markdown=f"[{label}]({url})", epistemic_status="attributed_practitioner_claim",
                            relevance="Matched source commentary; not independent verification or legal authority.")
            for chapter in chapters:
                if chapter["chapter_number"] in targets:
                    existing = chapter["source_citations"]
                    if not any(item["url"] == url and item["text"] == text for item in existing):
                        existing.append(deepcopy(citation))

    cap_per_chapter = 18 if large_corpus else None
    for chapter in chapters:
        number = chapter["chapter_number"]
        existing = chapter["source_citations"]
        for base_cit in BASELINE_EXPERT_CITATIONS_BY_CHAPTER.get(number, []):
            cloned = deepcopy(base_cit)
            if cloned.get("author") and not cloned.get("channel"):
                cloned["channel"] = cloned["author"]
            polished_base = polish_excerpt(str(cloned.get("text") or cloned.get("tip") or ""))
            if polished_base:
                cloned["text"] = polished_base
                cloned["tip"] = polished_base
            if not any(
                item.get("url") == cloned.get("url") and item.get("text") == cloned.get("text")
                for item in existing
            ):
                existing.append(cloned)
        if cap_per_chapter is not None and len(existing) > cap_per_chapter:
            # Retain baseline 15 plus top custom matches up to cap_per_chapter
            base_urls = {c.get("url") for c in BASELINE_EXPERT_CITATIONS_BY_CHAPTER.get(number, [])}
            baseline_items = [item for item in existing if item.get("url") in base_urls and item.get("relevance") != "Matched source commentary; not independent verification or legal authority."]
            if len(baseline_items) < len(base_urls):
                seen_b = {item.get("url") for item in baseline_items}
                for item in existing:
                    if item.get("url") in base_urls and item.get("url") not in seen_b:
                        seen_b.add(item.get("url"))
                        baseline_items.append(item)
            extra_items = [item for item in existing if item.get("url") not in base_urls]
            chapter["source_citations"] = baseline_items + extra_items[: max(0, cap_per_chapter - len(baseline_items))]

    total_words = compute_manuscript_word_count(chapters)
    total_yt_links = count_manuscript_youtube_links(chapters)
    return {
        "volume_id": "vol-001-heir-hunting", "volume_number": "001",
        "series_title": "THE BIG MONEY PLAYBOOKS", "parent_brand": "THE FUCK YOU MONEY CLUB",
        "tagline": "Big Money. Small Teams. No Bullshit.", "title": "HEIR HUNTING",
        "subtitle": "The Complete Playbook for Finding Missing Heirs, Researching Unclaimed Estates & Building a Probate Research Business",
        "min_expert_youtube_links_per_book": MIN_EXPERT_YOUTUBE_LINKS_PER_BOOK,
        "target_expert_youtube_links_per_book": TARGET_EXPERT_YOUTUBE_LINKS_PER_BOOK,
        "min_expert_youtube_links_per_chapter": MIN_EXPERT_YOUTUBE_LINKS_PER_CHAPTER,
        "expert_youtube_link_count": total_yt_links,
        "content_architecture_layers": [
            "Executive Summary",
            "Deep-Dive Analysis",
            "Visual Frameworks",
            "Operator Action Checklists",
            "Sources & Expert Insights",
        ],
        "operator_plays": get_candidate_track_metadata(1)["plays"],
        "positioning_alternatives": [
            {"title": "The Probate Research Operator", "subtitle": "Build documented kinship cases, not inheritance promises.",
             "audience": "Researchers building a narrow probate service", "research_basis": "State-law succession makes evidence and jurisdictional scope central to a defensible service.",
             "sources": ["https://www.law.cornell.edu/wex/intestacy"], "validation_status": "Source-informed editorial positioning; not market-tested."},
            {"title": "Evidence Before Inheritance", "subtitle": "A risk-first guide to finding heirs and screening estates.",
             "audience": "Operators who need stronger liability and solvency triage", "research_basis": "Federal Medicaid recovery provisions demonstrate why gross estate value cannot stand in for distributable value.",
             "sources": ["https://www.law.cornell.edu/uscode/text/42/1396p"], "validation_status": "Source-informed editorial positioning; not market-tested."},
            {"title": "The Missing-Heir Research Desk", "subtitle": "A small-team workflow from public records to reviewable proof.",
             "audience": "Genealogists developing a professional research workflow", "research_basis": "Intestacy identifies heirs under state law; positioning around sourced relationship research avoids promising a legal distribution result.",
             "sources": ["https://www.law.cornell.edu/wex/intestacy"], "validation_status": "Source-informed editorial positioning; not market-tested."},
        ],
        "epistemic_framework": [
            {"tier": 1, "tag": "statutory_fact", "label": "Primary legal authority", "standard": "Read the cited current law and applicable state implementation; citations are not individualized legal advice. California links are reference pointers, not certification of current text."},
            {"tier": 2, "tag": "attributed_practitioner_claim", "label": "Attributed source commentary", "standard": "Timestamped pro-tips identify who said what; they do not establish consensus or verify a legal or earnings claim."},
            {"tier": 3, "tag": "operating_framework", "label": "Editorial operating guidance", "standard": "Recommended controls and workflows require local adaptation and pilot validation; they are not measured industry norms."},
            {"tier": 4, "tag": "illustrative_model", "label": "Explicit hypothetical", "standard": "Invented budgets, conversion counts and fee examples explain mechanics, not actual market performance, legal ceilings or guaranteed results."},
        ],
        "total_word_count": total_words, "chapter_count": len(chapters), "chapters": chapters,
    }
