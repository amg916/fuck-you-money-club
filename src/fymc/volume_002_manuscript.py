from __future__ import annotations

from copy import deepcopy

from .vol002_q01_02 import CHAPTERS_1_TO_2
from .vol002_q03_04 import CHAPTERS_3_TO_4
from .vol002_q05_06 import CHAPTERS_5_TO_6
from .volume_002_chapters_b import CHAPTERS_7_TO_12, build_volume_002_workbook
from .volume_002_citations import BASELINE_EXPERT_CITATIONS_BY_CHAPTER, CHAPTER_KEYWORDS
from .volume_001_manuscript import compute_manuscript_word_count


CHAPTERS_1_TO_6 = CHAPTERS_1_TO_2 + CHAPTERS_3_TO_4 + CHAPTERS_5_TO_6


def build_volume_002_diagrams_data() -> list[dict]:
    """Return fresh renderer-neutral data with explicit units and assumptions."""
    specs = [
        ("diag-01-end-to-end-workflow", "process_flow", "From sale record to reconciled recovery", "Separate tax-sale and foreclosure procedures", 1,
         "operating_framework", "Numeric values indicate sequence, not duration or probability of recovery.",
         "A posted surplus is an investigation starting point; verify custody, priority and entitlement before estimating a claimant's proceeds.", [
             ("Identify sale", "Step 1", 1.0, "Record parcel, case number, sale date and whether the sale was tax-related or mortgage foreclosure."),
             ("Verify funds", "Step 2", 2.0, "Reconcile the sale accounting with the current custodian ledger; exclude paid, transferred or duplicated balances."),
             ("Resolve priority", "Step 3", 3.0, "Trace title, lien claims and the claimant's identity; refer disputed ranking and entitlement to counsel."),
             ("Document authority", "Step 4", 4.0, "Check deadlines and permitted compensation; assemble the signed engagement and evidence of representative authority."),
             ("Submit and reconcile", "Step 5", 5.0, "Use the custodian or court procedure, track objections and reconcile distribution against collected fees.")]),
        ("diag-02-deal-funnel", "funnel", "Screen for recoverable value, not list size", "Illustrative cohort of 200 sale records", 6,
         "illustrative_model", "Invented nested cohort counts; no observed conversion rate or collection forecast is implied.",
         "Keep a reason code for every rejected record and distinguish an engaged claimant from an actual cash collection.", [
             ("Sale records", "200", 200.0, "Deduplicated case and parcel records from one defined acquisition period."),
             ("Balance verified", "80", 80.0, "Custodian confirmation supports a still-held balance rather than a stale auction-list amount."),
             ("Net claim plausible", "32", 32.0, "Preliminary lien and deadline screening leaves a potentially economic claimant share."),
             ("Claimants engaged", "8", 8.0, "Eligible claimants choose assistance after receiving a clear scope and fee calculation."),
             ("Fees collected", "3", 3.0, "Resolved cases with cleared business receipts; pending matters remain outside this count.")]),
        ("diag-03-fee-waterfall", "waterfall", "Collected fee to case contribution", "Keep the claimant distribution separate", 3,
         "illustrative_model", "USD; opening and closing bars are totals, intervening bars are signed deductions. Assume a permitted 10% fee on a $50,000 claimant recovery.",
         "$5,000 collected less $600 records, $900 professional review and $1,000 acquisition allocation leaves $2,500 before overhead, owner compensation and tax.", [
             ("Collected fee", "$5,000", 5000.0, "Opening total; assumes lawful compensation and actual receipt, not an unsigned prospective fee."),
             ("Evidence costs", "-$600", -600.0, "Certified deeds, docket copies, identity documents and research labor paid by the business."),
             ("Professional review", "-$900", -900.0, "Illustrative business-paid review cost; not a statutory deduction from claimant proceeds."),
             ("Acquisition allocation", "-$1,000", -1000.0, "Includes outreach and screening expense for unsuccessful records in the same cohort."),
             ("Case contribution", "$2,500", 2500.0, "Closing total, not another movement; deduct fixed overhead before describing owner profit.")]),
        ("diag-04-jurisdiction-fee-caps", "horizontal_bars", "Test fee sensitivity before choosing a market", "Hypothetical ceilings, not a state-law comparison", 2,
         "illustrative_model", "Percent of a $50,000 claimant recovery. A-D are fictional jurisdictions; these values assert no actual statutory cap.",
         "A percentage ceiling alone does not establish an enforceable agreement; claim type, timing, permitted services and the compensation base also matter.", [
             ("Hypothetical A", "5% / $2,500", 5.0, "Assumed ceiling only; verify the governing sale procedure and any waiting period."),
             ("Hypothetical B", "10% / $5,000", 10.0, "Assumed ceiling, not a recommendation to charge the maximum."),
             ("Hypothetical C", "15% / $7,500", 15.0, "Assumed ceiling; reimbursed expenses may count toward allowed compensation."),
             ("Hypothetical D", "20% / $10,000", 20.0, "Assumed ceiling; legal representation and assignment restrictions remain separate questions.")]),
        ("diag-05-lien-priority-tree", "decision_tree", "Resolve priority before pricing a claim", "A triage tree, not an automatic payout formula", 7,
         "operating_framework", "Numbers identify nodes; branch directions are in the details. Applicable law and court orders control entitlement and ranking.",
         "Do not subtract every recorded lien mechanically: verify the sale type, lien status, priority, filed claims and the distribution procedure.", [
             ("Funds still held?", "Node 1", 1.0, "Yes: continue to node 2. No: locate the transfer or distribution record before further acquisition spending."),
             ("Claimant authority proven?", "Node 2", 2.0, "Yes: continue to node 3. No: obtain identity, title or estate authority documents; do not assume a relative can sign."),
             ("Competing claims resolved?", "Node 3", 3.0, "Yes: continue to node 4. No: send the docket, title chain and lien instruments for professional priority analysis."),
             ("Economic remainder?", "Node 4", 4.0, "Positive documented remainder: prepare the permitted claim. Zero or uncertain remainder: close or hold with a recorded reason.")]),
        ("diag-06-small-team-org", "org_architecture", "Two full-time operators, two contract specialists", "Illustrative base-team allocation", 9,
         "operating_framework", "Numeric values are role identifiers, not employee counts or pay. The owner and coordinator are full-time; research and counsel are contract roles.",
         "The owner manages case economics; the coordinator manages records and communication. Contract specialists retain responsibility for their assigned work.", [
             ("Owner / case lead", "1 FT", 1.0, "Owns market selection, budgets, engagements and cash reconciliation; supervises coordinator and research deliverables."),
             ("Records / client coordinator", "1 FT", 2.0, "Reports to owner; maintains custodian confirmations, deadline calendars and claimant document requests."),
             ("Title / records researcher", "1 C", 3.0, "Delivers sourced title and docket packets to the case lead; flags contradictions without deciding disputed entitlement."),
             ("Independent counsel", "1 C", 4.0, "Provides separately scoped professional review or representation; sales targets do not determine legal conclusions.")]),
        ("diag-07-startup-budget-stack", "stacked_comparison", "Fund the work before the first distribution", "Illustrative $10,000 business cash stack", 4,
         "illustrative_model", "USD; four additive components total $10,000 for one pilot scenario. Owner living expenses, income tax and ongoing salaries are excluded; obtain local quotes.",
         "The cash reserve is unspent liquidity, not a fee expense. A startup allowance does not fund a two-person payroll indefinitely.", [
             ("Setup and review", "$2,500", 2500.0, "Formation, initial engagement review and insurance allowance; actual costs depend on services and jurisdiction."),
             ("Tools and records", "$1,000", 1000.0, "Initial secure case system, records access and communication tools for a bounded pilot."),
             ("Pilot case work", "$1,500", 1500.0, "Certified documents, postage and contract research across successful and rejected cases."),
             ("Uncommitted reserve", "$5,000", 5000.0, "Liquidity for delays and rework; keep separate from projected receivables and claimant funds.")]),
        ("diag-08-30-day-roadmap", "timeline_roadmap", "Thirty days to a reviewable recovery operation", "Readiness milestones, not a payout schedule", 12,
         "operating_framework", "Numeric values are milestone end-days. Ranges are operating targets, not statutory filing periods or expected collection dates.",
         "The month should end with documented cases, actual spending and a decision on the next cohort; a pending distribution is not collected revenue.", [
             ("Select one lane", "Days 1-7", 7.0, "Choose one county and sale type; identify the custodian, claim procedure, compensation rules and deadlines."),
             ("Build the case desk", "Days 8-14", 14.0, "Configure record provenance, duplicate checks, engagement documents, case budgets and a deadline calendar."),
             ("Screen a pilot cohort", "Days 15-21", 21.0, "Verify balances, trace ownership and record rejection reasons before committing to expensive evidence work."),
             ("Review and iterate", "Days 22-30", 30.0, "Review evidence completeness, professional-review needs and cash runway; resize the next cohort using measured costs.")]),
    ]
    return [dict(diagram_id=identifier, chart_type=kind, title=title, subtitle=subtitle,
                 chapter_number=chapter, epistemic_tag=tag, assumptions_note=note, caption=caption,
                 stages=[dict(label=label, value=value, numeric_value=float(number), detail=detail)
                         for label, value, number, detail in stages])
            for identifier, kind, title, subtitle, chapter, tag, note, caption, stages in specs]


def build_volume_002_manuscript(abridged_videos: list[dict] | None = None) -> dict:
    """Build isolated chapter records with attributed, timestamped commentary."""
    import math
    import re
    from urllib.parse import parse_qs, urlparse
    from . import (
        MIN_EXPERT_YOUTUBE_LINKS_PER_BOOK,
        TARGET_EXPERT_YOUTUBE_LINKS_PER_BOOK,
        MIN_EXPERT_YOUTUBE_LINKS_PER_CHAPTER,
        count_manuscript_youtube_links,
    )
    from .scorecard_engine import get_candidate_track_metadata

    chapters = deepcopy(CHAPTERS_1_TO_6 + CHAPTERS_7_TO_12)
    diagram_ids = {item["diagram_id"][:7]: item["diagram_id"]
                   for item in build_volume_002_diagrams_data()}
    for chapter in chapters:
        chapter.setdefault("id", f"Q{chapter['chapter_number']}")
        chapter.setdefault("chapter_id", f"Q{chapter['chapter_number']}")
        reference = chapter["diagram_id"]
        prefix = reference[:7]
        if prefix not in diagram_ids or (reference != prefix and not reference.startswith(prefix + "-")):
            raise ValueError("Unknown Volume 002 diagram_id: " + str(reference))
        chapter["diagram_id"] = diagram_ids[prefix]
        chapter["source_citations"] = []

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

    _surplus_signals = (
        "surplus", "overage", "excess proceeds", "excess funds", "tax sale", "tax deed",
        "foreclosure", "hennepin", "tyler", "unclaimed", "escheat", "curative title",
        "skip trac", "overages", "state funds",
    )
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

    valid_videos = [video for video in (abridged_videos or []) if isinstance(video, dict)]
    large_corpus = len(valid_videos) > 20
    for video in valid_videos:
        if large_corpus:
            meta_obj = video.get("metadata") or {}
            haystack = " ".join(
                str(x or "")
                for x in (
                    video.get("title"),
                    video.get("channel"),
                    video.get("channel_title"),
                    video.get("author"),
                    meta_obj.get("title"),
                    meta_obj.get("channel_title"),
                    meta_obj.get("author"),
                )
            ).lower()
            if not any(sig in haystack for sig in _surplus_signals):
                continue
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
                scores.append((len(tokens & (set(CHAPTER_KEYWORDS.get(number, set())) | chapter_tokens)), number))
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
                            text=text, tip=text, timestamp=seconds, timestamp_seconds=seconds,
                            timestamp_label=f"[{label}]", url=url, markdown=f"[{label}]({url})",
                            epistemic_status="attributed_practitioner_claim",
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
        baseline = BASELINE_EXPERT_CITATIONS_BY_CHAPTER.get(number, [])
        baseline_prepared = []
        for base_cit in baseline:
            cloned = deepcopy(base_cit)
            if cloned.get("author") and not cloned.get("channel"):
                cloned["channel"] = cloned["author"]
            polished_base = polish_excerpt(str(cloned.get("text") or cloned.get("tip") or ""))
            if polished_base:
                cloned["text"] = polished_base
                cloned["tip"] = polished_base
            baseline_prepared.append(cloned)
        base_urls = {item.get("url") for item in baseline_prepared}
        non_base = [item for item in existing if item.get("url") not in base_urls]
        merged = baseline_prepared + non_base
        if cap_per_chapter is not None and len(merged) > cap_per_chapter:
            chapter["source_citations"] = baseline_prepared + non_base[: max(0, cap_per_chapter - len(baseline_prepared))]
        else:
            chapter["source_citations"] = merged

    total_words = compute_manuscript_word_count(chapters)
    total_yt_links = count_manuscript_youtube_links(chapters)
    return {
        "volume_id": "vol-002-surplus-funds-recovery", "volume_number": "002",
        "series_title": "THE BIG MONEY PLAYBOOKS", "parent_brand": "THE FUCK YOU MONEY CLUB",
        "tagline": "Big Money. Small Teams. No Bullshit.", "title": "SURPLUS FUNDS RECOVERY",
        "subtitle": "The Complete Playbook for Tax-Sale Overages, Foreclosure Excess Proceeds & Building a Contingent Recovery Firm",
        "content_architecture_layers": [
            {"layer": 1, "title": "Executive orientation", "description": "Question-led summaries and key metrics establish the opportunity, economics and operating constraints."},
            {"layer": 2, "title": "Operator-grade analysis", "description": "Detailed sections separate statutory facts, operating frameworks, hypothetical models and practitioner claims."},
            {"layer": 3, "title": "Visual decision support", "description": "Diagrams and tables expose process sequence, lien-priority questions, costs and collection assumptions."},
            {"layer": 4, "title": "Execution tools", "description": "SOPs, callouts, chapter checklists and the companion workbook translate evidence into repeatable case work."},
            {"layer": 5, "title": "Source evidence", "description": "Statutory citations and attributed timestamped commentary distinguish primary authority from practitioner perspective."},
        ],
        "operator_plays": deepcopy(get_candidate_track_metadata(2)["plays"]),
        "min_expert_youtube_links_per_book": MIN_EXPERT_YOUTUBE_LINKS_PER_BOOK,
        "target_expert_youtube_links_per_book": TARGET_EXPERT_YOUTUBE_LINKS_PER_BOOK,
        "min_expert_youtube_links_per_chapter": MIN_EXPERT_YOUTUBE_LINKS_PER_CHAPTER,
        "expert_youtube_link_count": total_yt_links,
        "positioning_alternatives": [
            {"title": "The Surplus Recovery Operator", "subtitle": "Turn sale records into documented claimant recoveries.",
             "audience": "Small teams building a focused tax-sale surplus practice",
             "research_basis": "California Revenue and Taxation Code section 4675 illustrates a defined excess-proceeds claim procedure with priority and timing requirements.",
             "sources": ["https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=4675."],
             "validation_status": "Source-informed editorial positioning; not market-tested."},
            {"title": "Beyond the Auction Balance", "subtitle": "Understand entitlement before counting a fee.",
             "audience": "Operators screening foreclosure excess-proceeds opportunities",
             "research_basis": "Florida section 45.032 distinguishes surplus funds and their distribution, supporting a workflow built around ownership, subordinate interests and case records.",
             "sources": ["https://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0000-0099/0045/Sections/0045.032.html"],
             "validation_status": "Source-informed editorial positioning; not market-tested."},
            {"title": "The Contingent Recovery Desk", "subtitle": "Build a small-team practice around evidence, priority and collected cash.",
             "audience": "Researchers and service-business owners evaluating contingent recovery work",
             "research_basis": "Florida section 45.033 addresses surplus rights and transfers; the distinction between a service engagement and an assignment informs scope and document design.",
             "sources": ["https://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0000-0099/0045/Sections/0045.033.html"],
             "validation_status": "Source-informed editorial positioning; not market-tested."},
        ],
        "epistemic_framework": [
            {"tier": 1, "tag": "statutory_fact", "label": "Primary legal authority", "standard": "Read current cited law, local procedure and case orders; one jurisdiction's surplus process does not establish another's deadlines or entitlement rules."},
            {"tier": 2, "tag": "attributed_practitioner_claim", "label": "Attributed source commentary", "standard": "Timestamped commentary identifies a source's statement; it does not independently verify legal conclusions, conversion rates or earnings."},
            {"tier": 3, "tag": "operating_framework", "label": "Editorial operating guidance", "standard": "Workflows and case-screening methods require local adaptation and pilot measurement; they are not observed industry benchmarks."},
            {"tier": 4, "tag": "illustrative_model", "label": "Explicit hypothetical", "standard": "Invented budgets, fee ceilings and funnel counts explain mechanics rather than actual market performance or statutory limits."},
        ],
        "total_word_count": total_words, "chapter_count": len(chapters), "chapters": chapters,
    }
