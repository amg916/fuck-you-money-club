"""Volume 005 manuscript, 8 vector diagrams, and citation merger for High-Ticket Affiliate Marketing."""
from __future__ import annotations

from copy import deepcopy

from .vol005_q01 import CHAPTER_1
from .vol005_q02 import CHAPTER_2
from .vol005_q03 import CHAPTER_3
from .vol005_q04 import CHAPTER_4
from .vol005_q05 import CHAPTER_5
from .vol005_q06 import CHAPTER_6
from .vol005_q07 import CHAPTER_7
from .vol005_q08 import CHAPTER_8
from .vol005_q09 import CHAPTER_9
from .vol005_q10 import CHAPTER_10
from .vol005_q11 import CHAPTER_11
from .vol005_q12 import CHAPTER_12
from .vol005_workbook import build_volume_005_workbook
from .volume_005_citations import BASELINE_EXPERT_CITATIONS_BY_CHAPTER, CHAPTER_KEYWORDS
from .volume_001_manuscript import compute_manuscript_word_count

ALL_VOLUME_005_CHAPTERS = [
    CHAPTER_1,
    CHAPTER_2,
    CHAPTER_3,
    CHAPTER_4,
    CHAPTER_5,
    CHAPTER_6,
    CHAPTER_7,
    CHAPTER_8,
    CHAPTER_9,
    CHAPTER_10,
    CHAPTER_11,
    CHAPTER_12,
]


def build_volume_005_diagrams_data() -> list[dict]:
    """Return 8 structured vector diagram specifications with explicit units and assumptions."""
    specs = [
        (
            "diag-01-affiliate-funnel-to-commission-loop",
            "process_flow",
            "From commercial buyer intent to settled recurring & CPA commissions",
            "Five-stage high-ticket referral publishing & S2S attribution loop",
            1,
            "operating_framework",
            "Numeric values indicate operating sequence; conversion and scrub rates vary by vertical.",
            "Own the pre-sell comparison calculator, first-party click_id, and email relationship rather than sending cold clicks to raw vendor homepages.",
            [
                ("Intercept BOFU intent", "Step 1", 1.0, "Capture '[Vendor] vs [Vendor]', pricing-calculator, and migration queries across search, YouTube, and AI engines."),
                ("Pre-sell & capture", "Step 2", 2.0, "Run an interactive edge fee/ROI calculator with above-the-fold FTC disclosure and optional checklist email capture."),
                ("Mint S2S click_id", "Step 3", 3.0, "Log GCLID/UTM context in click_ledger and pass unique click_id into 3+ competing high-ticket merchant offers."),
                ("Verify S2S & scrub", "Step 4", 4.0, "Ingest HMAC-signed PartnerStack, Impact, Everflow, or Ringba webhooks and hold a 15% reversal/scrub reserve."),
                ("Compound & re-route", "Step 5", 5.0, "Upload net offline values to ad platforms, stack sequential fintech/SaaS bounties, and cap single merchants at <=25%."),
            ],
        ),
        (
            "diag-02-click-to-commission-funnel",
            "funnel",
            "Bottom-of-funnel comparison traffic to net settled commissions",
            "Illustrative monthly cohort of 10,000 commercial-investigation visitors",
            6,
            "illustrative_model",
            "Invented nested cohort counts illustrating high-intent B2B comparison math; not representative earnings.",
            "Bottom-of-funnel switching and pricing queries convert 5x-10x higher than generic informational listicles.",
            [
                ("BOFU hub visitors", "10,000", 10000.0, "Visitors landing on '[Incumbent] pricing calculator', 'vs', and mid-year migration guides."),
                ("Calculator / table users", "5,800", 5800.0, "Engaged buyers filtering vendor pricing tiers by seat count, state footprint, or transaction volume."),
                ("Outbound merchant clicks", "4,600", 4600.0, "Pre-qualified clicks routed with first-party click_id across Primary, Runner-Up, and Fallback offers."),
                ("Gross S2S conversions", "253", 253.0, "Combined qualified B2B demos, funded fintech accounts, and recurring SaaS subscriptions reported."),
                ("Settled post-scrub payouts", "215", 215.0, "Locked payable conversions after 15% duplicate-CRM, invalid-lead, and 45-day cancellation scrubs."),
            ],
        ),
        (
            "diag-03-epc-to-net-margin-waterfall",
            "waterfall",
            "Gross reported commissions to net owner profit",
            "Illustrative $1,000 gross reported affiliate commission cohort",
            3,
            "illustrative_model",
            "USD per $1,000 gross dashboard commissions; opening and closing bars are totals, middle bars are deductions.",
            "Separate merchant GMV from gross reported commissions, deduct reversals first, and fund media/contractors out of settled Net EPC.",
            [
                ("Gross reported payouts", "$1,000", 1000.0, "Initial CPA bounties, qualified call transfers, and recurring SaaS shares logged before locking."),
                ("Scrubs & clawbacks", "-$150", -150.0, "15% duplicate-CRM leads, <45-day trial cancellations, and refund/chargeback reversals."),
                ("Paid media & co-reg", "-$265", -265.0, "Bounded exact-match comparison search and SparkLoop co-reg spend net of Day-0 recoup."),
                ("Editorial & video pod", "-$210", -210.0, "Two specialized part-time contractors producing substantiated guides, calculators, and YouTube demos."),
                ("Edge, S2S & compliance", "-$77", -77.0, "ClickFlare/Everflow S2S tracking, Ringba routing, SERP/GEO intelligence, and substantiation ops."),
                ("Owner net profit", "$298", 298.0, "35.1% Base-Case net margin on $850 net earned commissions (20% Conservative -> 50% Scaled)."),
            ],
        ),
        (
            "diag-04-attribution-rail-payout-rates",
            "horizontal_bars",
            "Illustrative net commission per conversion across referral rails",
            "Typical post-scrub USD realization per qualified conversion event",
            2,
            "illustrative_model",
            "Illustrative midpoints across B2B/fintech/lead-gen rails; verify live partner contracts independently.",
            "High-ticket B2B SaaS, stacked fintech bounties, and 90-second inbound calls dwarf 1%-4% retail affiliate links.",
            [
                ("Stacked B2B Fintech + SaaS", "$950 / conv", 950.0, "Sequential LLC + business banking + corporate card + payroll software bounties on one new entity."),
                ("B2B SaaS 30% RevShare (12m)", "$640 / conv", 640.0, "12-month realized recurring share on a $210/mo B2B software plan net of logo churn."),
                ("Enterprise Demo + Won CPA", "$525 / conv", 525.0, "Blended PartnerStack / Impact payout combining qualified SQL demo fee plus closed-won bonus."),
                ("Inbound Pay-Per-Call (90s+)", "$135 / call", 135.0, "Ringba/Phonexa qualified commercial insurance, legal, or home-service call lasting >=90 seconds."),
                ("Retail E-Commerce Cookie", "$6 / order", 6.0, "3% commission on a $200 consumer cart exposed to 24-hour cookie expiry and coupon poaching."),
            ],
        ),
        (
            "diag-05-compliance-and-scrub-guardrail-tree",
            "decision_tree",
            "Disclosure, trademark, TCPA & concentration guardrails",
            "Mandatory pre-flight checks before activating traffic on any offer",
            5,
            "operating_framework",
            "Numbers identify sequential operating checks enforced prior to live click routing.",
            "Eliminate retro-clawbacks and account bans by enforcing FTC disclosures, TM+ riders, S2S deduplication, and <=25% merchant caps.",
            [
                ("FTC 255 above fold?", "Check 1", 1.0, "Plain-English material connection notice appears above first CTA on 390px mobile, desktop, and video."),
                ("TM+ or brand negs?", "Check 2", 2.0, "Either signed written TM+ co-bidding addendum on file or account-level partner brand negatives active."),
                ("TCPA / statutory clean?", "Check 3", 3.0, "Zero federal healthcare % kickbacks (42 U.S.C. 1320a-7b); Seller-specific consent + TrustedForm on calls/leads."),
                ("S2S + <=25% cap?", "Check 4", 4.0, "HMAC S2S postback verified with >=2 fallback offers live so no merchant exceeds 25% of portfolio revenue."),
            ],
        ),
        (
            "diag-06-three-person-affiliate-pod",
            "org_architecture",
            "One full-time founder, two specialized contractors",
            "Illustrative 3-person ($325k earned-commission Base Case) pod",
            11,
            "operating_framework",
            "Numeric values are role identifiers; Scaled ($600k earned commissions) scenario expands to 2 FT + 3 C.",
            "Keep fixed payroll near zero by pairing founder deal/attribution ownership with specialized research and video contractors.",
            [
                ("Founder / deal & media lead", "1 FT", 1.0, "Owns merchant underwriting, private CPA bumps, S2S ledger ops, exact-match search caps, and capital float."),
                ("B2B research & hub editor", "1 C", 2.0, "Publishes substantiated comparison calculators, maintains 30-day pricing archives, and optimizes GEO tables."),
                ("YouTube & link-QA specialist", "1 C", 3.0, "Produces 2 screen-recorded product comparisons weekly, manages SparkLoop co-reg, and audits S2S link health."),
            ],
        ),
        (
            "diag-07-startup-media-and-edge-stack",
            "stacked_comparison",
            "Disciplined $20,000 hybrid high-ticket affiliate launch budget",
            "Illustrative allocation across Candidate #24's $5k-$50k startup range",
            4,
            "illustrative_model",
            "USD cash allocation; >=60% stays in liquid Net-60 payout float and working-capital reserve.",
            "Edge comparison hubs cost pennies to host; preserve the majority of launch capital to bridge Net-45/Net-60 commission locking windows.",
            [
                ("Entity, clean domains & IP", "$1,200", 1200.0, "LLC setup, dedicated bank/cards, non-trademark domain diligence, and 17 U.S.C. 204(a) contractor agreements."),
                ("Edge, S2S & SERP/GEO stack", "$1,800", 1800.0, "Three months of Cloudflare Workers/D1, ClickFlare/Everflow S2S tracker, Ringba numbers, and SERP data."),
                ("Bounded BOFU & co-reg tests", "$5,000", 5000.0, "Capped exact-match comparison search tests, SparkLoop co-reg seed budget, and initial video editing."),
                ("Net-60 float & cash reserve", "$12,000", 12000.0, "Segregated working-capital buffer bridging 30-day ad-card billing against 45-to-60-day merchant ACH payouts."),
            ],
        ),
        (
            "diag-08-thirty-day-commission-sprint",
            "timeline_roadmap",
            "Thirty days from partner approval to verified Net EPC run-rate",
            "Four weekly underwriting, S2S build, BOFU launch & Kill/Fix/Scale phases",
            12,
            "operating_framework",
            "Numeric values are milestone end-days; full 3-12 month ramp applies to compounded organic/recurring cohorts.",
            "Validate conversion rate and Net EPC on bottom-of-funnel comparison intent in Month 1 before scaling content headcount.",
            [
                ("Underwrite & approve", "Days 1-7", 7.0, "Approve >=3 competing offers in 1 B2B/fintech vertical, audit clawback/TM+ terms, and map 25 BOFU queries."),
                ("Wire calculator & S2S", "Days 8-14", 14.0, "Ship <1s edge comparison calculator, FTC 255 bar, checklist capture, and synthetic S2S webhook test."),
                ("Launch guides & video", "Days 15-21", 21.0, "Publish 10 substantiated vs/pricing pages, 5 YouTube demos, and run a $300-$500 exact-match search test."),
                ("Reconcile & scale", "Days 22-30", 30.0, "Audit scrub reasons, negotiate a 20%-30% private CPA bump on early volume, and apply Kill/Fix/Scale rules."),
            ],
        ),
    ]
    return [
        dict(
            diagram_id=identifier,
            chart_type=kind,
            title=title,
            subtitle=subtitle,
            chapter_number=chapter,
            epistemic_tag=tag,
            assumptions_note=note,
            caption=caption,
            stages=[
                dict(label=label, value=value, numeric_value=float(number), detail=detail)
                for label, value, number, detail in stages
            ],
        )
        for identifier, kind, title, subtitle, chapter, tag, note, caption, stages in specs
    ]


def build_volume_005_manuscript(abridged_videos: list[dict] | None = None) -> dict:
    """Build isolated Volume 005 chapter records with attributed, sentence-clean commentary."""
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

    chapters = deepcopy(ALL_VOLUME_005_CHAPTERS)
    diagram_ids = {item["diagram_id"][:7]: item["diagram_id"] for item in build_volume_005_diagrams_data()}
    for chapter in chapters:
        chapter.setdefault("id", f"Q{chapter['chapter_number']}")
        chapter.setdefault("chapter_id", f"Q{chapter['chapter_number']}")
        reference = chapter["diagram_id"]
        prefix = reference[:7]
        if prefix not in diagram_ids or (reference != prefix and not reference.startswith(prefix + "-")):
            raise ValueError("Unknown Volume 005 diagram_id: " + str(reference))
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

    _affiliate_allow_re = re.compile(
        r"\b(?:"
        r"affiliate|affiliates|partnerstack|impact\.com|everflow|voluum|clickflare|ringba|phonexa|"
        r"parasitic\s+seo|site\s+reputation\s+abuse|pay[- ]per[- ]call|ping[- ]post|cpa\s+marketing|"
        r"high[- ]ticket\s+affiliate|sparkloop|beehiiv|brand\s+bidding|epc|postback|subid|"
        r"empire\s+flippers|quiet\s+light|chrome\s+extension|afd|rsoc|system1|matched\s+betting|"
        r"ftc\s+disclosure|affiliate\s+marketing|seo\s+affiliate|comparison\s+page|bridge\s+page"
        r")\b",
        re.IGNORECASE,
    )
    _off_domain_deny_re = re.compile(
        r"\b(?:"
        r"genealogy|genealogical|genealogist|ancestry|familysearch|family\s+history|"
        r"birth\s+records|marriage\s+records|death\s+records|cemeteries|obituary|obituaries|"
        r"probate|heir\s+hunting|heirs\s+property|intestate|"
        r"surplus\s+funds|tax\s+sale|tax\s+deed|tax\s+overage|overages|excess\s+proceeds|"
        r"foreclosure|curative\s+title|title\s+search|title\s+problems|distressed\s+properties|"
        r"unclaimed\s+property|state\s+funds|property\s+locator|escheat|escheatment|mineral\s+rights"
        r")\b",
        re.IGNORECASE,
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
            source_corpus = str(video.get("source_corpus") or meta_obj.get("source_corpus") or "").lower()
            if _off_domain_deny_re.search(haystack):
                continue
            if source_corpus != "vol005_high_ticket_affiliate_marketing" and not _affiliate_allow_re.search(haystack):
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
            if large_corpus and _off_domain_deny_re.search(raw_tip_text):
                continue
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
            tokens = set(re.findall(r"[a-z0-9]+", text.lower()))
            scores = []
            for chapter in chapters:
                number = chapter["chapter_number"]
                chapter_tokens = set(re.findall(r"[a-z0-9]+", str(chapter.get("title", "")).lower()))
                chapter_tokens -= {"the", "a", "an", "is", "to", "of", "and", "in", "for", "what", "how", "your", "with", "who", "why", "where"}
                scores.append((len(tokens & (set(CHAPTER_KEYWORDS.get(number, set())) | chapter_tokens)), number))
            best_score = max((score for score, number in scores), default=0)
            targets = (
                {number for score, number in scores if str(number) == explicit}
                if explicit is not None
                else {number for score, number in scores if score == best_score and score > 0}
            )
            label = f"{seconds // 3600:02d}:{seconds % 3600 // 60:02d}:{seconds % 60:02d}"
            url = f"https://www.youtube.com/watch?v={video_id}&t={seconds}s"
            channel_name = str(
                video.get("channel")
                or video.get("channel_title")
                or video.get("author")
                or (video.get("metadata") or {}).get("author")
                or "Independent Practitioner"
            ).strip()
            citation = dict(
                source_type="video_pro_tip",
                video_id=video_id,
                title=str(video.get("title") or (video.get("metadata") or {}).get("title") or video_id),
                channel=channel_name,
                author=channel_name,
                text=text,
                tip=text,
                timestamp=seconds,
                timestamp_seconds=seconds,
                timestamp_label=f"[{label}]",
                url=url,
                markdown=f"[{label}]({url})",
                epistemic_status="attributed_practitioner_claim",
                relevance="Matched source commentary; not independent verification or legal authority.",
            )
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
        "volume_id": "vol-005-high-ticket-affiliate-marketing",
        "volume_number": "005",
        "series_title": "THE BIG MONEY PLAYBOOKS",
        "parent_brand": "THE FUCK YOU MONEY CLUB",
        "tagline": "Big Money. Small Teams. No Bullshit.",
        "title": "HIGH-TICKET AFFILIATE MARKETING",
        "subtitle": "The Complete Playbook for Recurring B2B Software Shares, Stacked Fintech CPA Bounties, S2S Attribution & Scaling a $600k/yr 3-to-5 Person Referral Portfolio",
        "content_architecture_layers": [
            {"layer": 1, "title": "Executive orientation", "description": "Question-led summaries and key metrics establish merchant LTV-to-CAC headroom, reversal-adjusted Net EPC, and working-capital float."},
            {"layer": 2, "title": "Operator-grade analysis", "description": "Detailed sections separate FTC/TCPA/anti-kickback rules, S2S postback architectures, cohort unit models, and practitioner claims."},
            {"layer": 3, "title": "Visual decision support", "description": "Diagrams and tables expose comparison funnels, EPC-to-margin waterfalls, attribution rails, and merchant-concentration guardrails."},
            {"layer": 4, "title": "Execution tools", "description": "SOPs, callouts, chapter checklists, and the 6-worksheet companion workbook turn comparison intent into settled commissions."},
            {"layer": 5, "title": "Source evidence", "description": "Statutory/regulatory citations and attributed timestamped commentary distinguish primary rules from practitioner perspective."},
        ],
        "operator_plays": deepcopy(get_candidate_track_metadata(24)["plays"]),
        "min_expert_youtube_links_per_book": MIN_EXPERT_YOUTUBE_LINKS_PER_BOOK,
        "target_expert_youtube_links_per_book": TARGET_EXPERT_YOUTUBE_LINKS_PER_BOOK,
        "min_expert_youtube_links_per_chapter": MIN_EXPERT_YOUTUBE_LINKS_PER_CHAPTER,
        "expert_youtube_link_count": total_yt_links,
        "positioning_alternatives": [
            {
                "title": "The B2B Comparison & Switching Desk",
                "subtitle": "Intercept bottom-of-funnel pricing, migration, and alternative queries with interactive ROI calculators and 3+ competing SaaS/fintech partners.",
                "audience": "Analytical solo operators and 2-to-5 person editorial engineering pods",
                "research_basis": "Clear above-the-fold FTC 16 CFR Part 255 disclosures and dated vendor fee tables build durable buyer and partner trust.",
                "sources": ["https://www.ecfr.gov/current/title-16/chapter-I/subchapter-B/part-255"],
                "validation_status": "Source-informed editorial positioning; not market-tested.",
            },
            {
                "title": "Server-Side S2S & Co-Registration Arbitrage",
                "subtitle": "Liquidate subscriber acquisition on Day 0 via newsletter co-registration while feeding net offline conversion values back into search algorithms.",
                "audience": "Performance media buyers and newsletter operators engineering predictable Net EPC spreads",
                "research_basis": "First-party click_id ledgers and CAN-SPAM / RFC 8058 hygiene protect attribution accuracy and inbox placement.",
                "sources": ["https://www.law.cornell.edu/uscode/text/15/7704"],
                "validation_status": "Source-informed editorial positioning; not market-tested.",
            },
            {
                "title": "Exit-Ready Referral Media Portfolios",
                "subtitle": "Cap single-merchant concentration at <=25%, pair YouTube + GEO + search traffic, and maintain clean books for 30x-45x monthly profit exits.",
                "audience": "Portfolio builders and micro-PE acquirers targeting transferable digital media cashflow",
                "research_basis": "Written contractor IP assignments under 17 U.S.C. 204(a) and clean non-trademark domains pass institutional brokerage diligence.",
                "sources": ["https://www.law.cornell.edu/uscode/text/17/204"],
                "validation_status": "Source-informed editorial positioning; not market-tested.",
            },
        ],
        "chapters": chapters,
        "chapter_count": len(chapters),
        "total_word_count": total_words,
        "epistemic_note": "Educational and research material only, not legal, tax, accounting, or investment advice. Verify FTC disclosure, telemarketing consent, trademark, and sector-specific referral rules independently.",
    }
