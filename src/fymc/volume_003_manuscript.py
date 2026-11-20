"""Volume 003 manuscript, 8 vector diagrams, and citation merger for Digital Product Empire."""
from __future__ import annotations

from copy import deepcopy

from .vol003_q01 import CHAPTER_1
from .vol003_q02 import CHAPTER_2
from .vol003_q03 import CHAPTER_3
from .vol003_q04 import CHAPTER_4
from .vol003_q05 import CHAPTER_5
from .vol003_q06 import CHAPTER_6
from .vol003_q07 import CHAPTER_7
from .vol003_q08 import CHAPTER_8
from .vol003_q09 import CHAPTER_9
from .vol003_q10 import CHAPTER_10
from .vol003_q11 import CHAPTER_11
from .vol003_q12 import CHAPTER_12
from .vol003_workbook import build_volume_003_workbook
from .volume_003_citations import BASELINE_EXPERT_CITATIONS_BY_CHAPTER, CHAPTER_KEYWORDS
from .volume_001_manuscript import compute_manuscript_word_count

ALL_VOLUME_003_CHAPTERS = [
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


def build_volume_003_diagrams_data() -> list[dict]:
    """Return 8 structured vector diagram specifications with explicit units and assumptions."""
    specs = [
        (
            "diag-01-value-ladder-workflow",
            "process_flow",
            "From pain signal to recurring portfolio cashflow",
            "Five-stage digital product value ladder",
            1,
            "operating_framework",
            "Numeric values indicate operating sequence, not guaranteed conversion rates.",
            "Validate willingness to pay before full asset production, then compound LTV via order bumps, 1-click upsells, and recurring updates.",
            [
                ("Validate pain", "Step 1", 1.0, "Mine Ad Libraries, search queries, and Reddit threads; pre-sell or smoke-test before full build."),
                ("Ship core SKU", "Step 2", 2.0, "Package a modular template, toolkit, or micro-course that delivers a measurable win in 15 minutes."),
                ("Expand basket", "Step 3", 3.0, "Attach a contextual $19-$29 order bump and a 1-click post-purchase implementation upsell."),
                ("Automate onboarding", "Step 4", 4.0, "Deliver license tokens, Visa CE 3.0 receipts, and a 5-part activation sequence to cut refunds."),
                ("Ascend LTV", "Step 5", 5.0, "Convert proven buyers into annual data feeds, paid communities, or quarterly template drops."),
            ],
        ),
        (
            "diag-02-demand-validation-funnel",
            "funnel",
            "Self-liquidating acquisition to backend ascension",
            "Illustrative cohort of 1,000 targeted visitors",
            6,
            "illustrative_model",
            "Invented nested cohort counts illustrating funnel math; actual conversion varies by traffic source and offer.",
            "Newsletter co-registration and front-end order bumps offset acquisition spend so backend community and bundle sales become high-margin profit.",
            [
                ("Targeted clicks", "1,000", 1000.0, "High-intent visitors from YouTube tutorials, Reddit SERP threads, GEO citations, or paid tests."),
                ("Lead-magnet opt-ins", "380", 380.0, "38% opt-in to a free calculator or lite template with optional paid newsletter co-registration."),
                ("Core SKU buyers", "34", 34.0, "3.4% front-end conversion on a $49 operational toolkit or template system."),
                ("Bump & upsell buyers", "13", 13.0, "38% order-bump attachment and 14% 1-click post-purchase bundle upgrades."),
                ("Annual subscribers", "5", 5.0, "Ascended members on a $290-$490/yr update feed or operator community."),
            ],
        ),
        (
            "diag-03-slo-contribution-waterfall",
            "waterfall",
            "Gross checkout receipts to net contribution margin",
            "Illustrative $100 blended basket on Merchant-of-Record rails",
            3,
            "illustrative_model",
            "USD per $100 gross checkout basket; opening and closing bars are totals, middle bars are deductions.",
            "$100 gross receipts less $5.50 MoR processing, $4.00 refund reserve, $12.00 affiliate/support allocation, and $23.50 media spend leaves $55.00 contribution.",
            [
                ("Gross basket", "$100.00", 100.0, "Combined front-end SKU, order bump, and post-purchase upsell receipts excluding pass-through VAT."),
                ("MoR & payment fee", "-$5.50", -5.5, "Merchant-of-Record 5% + $0.50 fee handling global VAT/sales-tax remittance and fraud screening."),
                ("Refunds & disputes", "-$4.00", -4.0, "4% combined refund and dispute allowance under clear click-to-cancel terms."),
                ("Support & affiliates", "-$12.00", -12.0, "Blended affiliate payout share and Tier-1 support/fulfillment automation cost."),
                ("Net ad spend", "-$23.50", -23.5, "Paid media outlay net of Day-1 SparkLoop / co-registration lead-magnet liquidation."),
                ("Contribution margin", "$55.00", 55.0, "Closing contribution before fixed studio opex, contractor retainers, and owner taxes."),
            ],
        ),
        (
            "diag-04-mor-vs-direct-fee-bars",
            "horizontal_bars",
            "Effective take-rate across checkout & distribution rails",
            "Illustrative % platform & payment fee on a $100 digital order",
            2,
            "illustrative_model",
            "Percent of a $100 digital sale; excludes optional paid discovery boosts and state registration overhead.",
            "Direct Stripe has the lowest card fee but leaves global VAT/Wayfair nexus compliance on the seller; MoR platforms absorb tax liability for ~2% more.",
            [
                ("Direct Stripe + Tax", "3.7% / $3.70", 3.7, "2.9% + $0.30 card fee plus ~0.5% Stripe Tax; seller still owns state/VAT registrations."),
                ("MoR (Paddle / LS)", "5.5% / $5.50", 5.5, "5% + $0.50 Merchant-of-Record fee; MoR acts as legal seller and remits global VAT/sales tax."),
                ("Gumroad Direct", "10.5% / $10.50", 10.5, "10% + $0.50 direct-link fee; simple starter rail but expensive above $10k/mo volume."),
                ("App Store In-App", "30.0% / $30.00", 30.0, "Standard 30% mobile store commission (15% Small Business Program) vs Web2App external web checkout."),
            ],
        ),
        (
            "diag-05-piracy-refund-triage-tree",
            "decision_tree",
            "Checkout compliance, chargeback & piracy defense tree",
            "Operational triage before scaling paid traffic",
            5,
            "operating_framework",
            "Numbers identify decision nodes; keep dispute ratio well below the 0.75% card-network threshold.",
            "Prevent friendly-fraud chargebacks and group-buy leaks structurally through MoR tax handling, CE 3.0 logs, 1-click refunds, and fingerprinted files.",
            [
                ("Global tax covered?", "Node 1", 1.0, "Yes via MoR or registered tax engine: advance to Node 2. No: route international/nexus checkout to MoR."),
                ("CE 3.0 telemetry?", "Node 2", 2.0, "Log IP, device, timestamp, license activation, and download events to win friendly-fraud representments."),
                ("Dispute rate <0.4%?", "Node 3", 3.0, "Yes: scale traffic. Elevated: enable self-serve 1-click refunds/cancellations so unhappy buyers refund instead of disputing."),
                ("Canary watermark?", "Node 4", 4.0, "Embed buyer-specific canary hashes and automate 17 U.S.C. 512(c) DMCA notices on leaked repos."),
            ],
        ),
        (
            "diag-06-four-person-empire-org",
            "org_architecture",
            "One full-time architect, three specialized contractors",
            "Illustrative 4-person ($425k-$800k/yr) portfolio pod",
            11,
            "operating_framework",
            "Numeric values are role identifiers, not FTE salaries. All contractor work requires signed IP assignment.",
            "Keep headcount lean by automating fulfillment, tax, and Tier-1 FAQ triage while focusing human talent on SKU quality and creative velocity.",
            [
                ("Owner / product architect", "1 FT", 1.0, "Owns market selection, offer positioning, pricing, funnel math, and capital allocation."),
                ("Product & UI builder", "1 C", 2.0, "Builds modular Notion/Sheets/Figma systems, calculators, and micro-extension updates under written IP assignment."),
                ("Video & ad editor", "1 C", 3.0, "Produces faceless YouTube tutorials, VSL hooks, and weekly Meta/TikTok creative variants."),
                ("Ops & affiliate lead", "1 C", 4.0, "Manages Tier-2 customer tickets, refund QA, DMCA sweeps, and affiliate/newsletter partner payouts."),
            ],
        ),
        (
            "diag-07-zero-cogs-startup-stack",
            "stacked_comparison",
            "Disciplined $10,000 digital product launch allocation",
            "Illustrative pilot budget with 50% untouched cash reserve",
            4,
            "illustrative_model",
            "USD; four additive components total $10,000 for a multi-SKU launch scenario. Serverless hosting and startup credits keep fixed tech COGS near zero.",
            "Never sink $10,000 into unvalidated course production; cap initial build + legal setup and preserve liquidity for post-validation traffic scaling.",
            [
                ("Entity & IP setup", "$1,200", 1200.0, "LLC formation, business banking, domain portfolio, and contractor work-made-for-hire / IP templates."),
                ("Design & tooling", "$1,300", 1300.0, "Screen-recording gear, analytics, email engine, and modular design assets not covered by free tiers."),
                ("Validation ad tests", "$2,500", 2500.0, "Bounded 72-hour pre-sale smoke tests and SLO creative experiments with strict kill gates."),
                ("Operating reserve", "$5,000", 5000.0, "Untouched liquidity buffer for scaling proven ROAS winners and covering payout timing."),
            ],
        ),
        (
            "diag-08-thirty-day-launch-roadmap",
            "timeline_roadmap",
            "Thirty days from pain signal to cash-flowing SKU",
            "Four weekly validation, build, launch & optimization gates",
            12,
            "operating_framework",
            "Numeric values are milestone end-days. Advance to paid scaling only after front-end unit economics clear target thresholds.",
            "Ship a focused v1.0 painkiller in 14 days, validate real checkout conversion in Week 3, and lock onboarding + affiliate leverage by Day 30.",
            [
                ("Mine & pre-sell", "Days 1-7", 7.0, "Audit Ad Libraries and Reddit threads, wire MoR pre-sale lander, and confirm real buyer conversion."),
                ("Build & wire SKU", "Days 8-14", 14.0, "Assemble modular v1.0 product, order bump, 1-click upsell, CE 3.0 webhooks, and 5-email onboarding."),
                ("Launch & liquidate", "Days 15-21", 21.0, "Publish YouTube/Reddit/DM triggers, activate newsletter co-reg, and run $50/day SLO split tests."),
                ("Audit & scale", "Days 22-30", 30.0, "Reconcile net contribution margin, cut refund friction, onboard affiliates, and scale winning hooks."),
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


def build_volume_003_manuscript(abridged_videos: list[dict] | None = None) -> dict:
    """Build isolated Volume 003 chapter records with attributed, sentence-clean commentary."""
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

    chapters = deepcopy(ALL_VOLUME_003_CHAPTERS)
    diagram_ids = {item["diagram_id"][:7]: item["diagram_id"] for item in build_volume_003_diagrams_data()}
    for chapter in chapters:
        chapter.setdefault("id", f"Q{chapter['chapter_number']}")
        chapter.setdefault("chapter_id", f"Q{chapter['chapter_number']}")
        reference = chapter["diagram_id"]
        prefix = reference[:7]
        if prefix not in diagram_ids or (reference != prefix and not reference.startswith(prefix + "-")):
            raise ValueError("Unknown Volume 003 diagram_id: " + str(reference))
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

    _digital_signals = (
        "digital product", "digital products", "notion", "gumroad", "lemon squeezy",
        "paddle", "stripe", "sales tax", "vat", "merchant of record", "upsell",
        "order bump", "funnel", "course", "community", "skool", "newsletter",
        "beehiiv", "sparkloop", "chrome extension", "faceless", "manychat",
        "chargeback", "piracy", "dmca", "pricing", "template", "ebook", "saas",
        "creator", "monetiz", "affiliate", "pinterest", "reddit", "web2app", "geo",
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
            if not any(sig in haystack for sig in _digital_signals):
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
        "volume_id": "vol-003-digital-product-empire",
        "volume_number": "003",
        "series_title": "THE BIG MONEY PLAYBOOKS",
        "parent_brand": "THE FUCK YOU MONEY CLUB",
        "tagline": "Big Money. Small Teams. No Bullshit.",
        "title": "DIGITAL PRODUCT EMPIRE",
        "subtitle": "The Complete Playbook for High-Margin Templates, Self-Liquidating Funnels, Merchant-of-Record Checkout & Scaling an $800k/yr 4-Person Catalog",
        "content_architecture_layers": [
            {"layer": 1, "title": "Executive orientation", "description": "Question-led summaries and key metrics establish product-ladder economics, take-rates, and operating constraints."},
            {"layer": 2, "title": "Operator-grade analysis", "description": "Detailed sections separate statutory tax/billing rules, operating frameworks, hypothetical SLO models, and practitioner claims."},
            {"layer": 3, "title": "Visual decision support", "description": "Diagrams and tables expose value ladders, checkout take-rates, SLO contribution margins, and chargeback/piracy triage."},
            {"layer": 4, "title": "Execution tools", "description": "SOPs, callouts, chapter checklists, and the 6-worksheet companion workbook translate strategy into repeatable SKU launches."},
            {"layer": 5, "title": "Source evidence", "description": "Statutory/regulatory citations and attributed timestamped commentary distinguish primary rules from creator perspective."},
        ],
        "operator_plays": deepcopy(get_candidate_track_metadata(27)["plays"]),
        "min_expert_youtube_links_per_book": MIN_EXPERT_YOUTUBE_LINKS_PER_BOOK,
        "target_expert_youtube_links_per_book": TARGET_EXPERT_YOUTUBE_LINKS_PER_BOOK,
        "min_expert_youtube_links_per_chapter": MIN_EXPERT_YOUTUBE_LINKS_PER_CHAPTER,
        "expert_youtube_link_count": total_yt_links,
        "positioning_alternatives": [
            {
                "title": "The Zero-COGS Catalog Architect",
                "subtitle": "Build modular B2B templates and calculators that compound without headcount bloat.",
                "audience": "Solo operators and 2-to-4 person teams building high-margin B2B digital toolkits",
                "research_basis": "Merchant-of-Record checkout and serverless hosting eliminate physical COGS and automate multi-jurisdiction digital tax remittance.",
                "sources": ["https://supreme.justia.com/cases/federal/us/585/162/"],
                "validation_status": "Source-informed editorial positioning; not market-tested.",
            },
            {
                "title": "Self-Liquidating Funnel Systems",
                "subtitle": "Liquidate Day-1 acquisition spend with order bumps, co-registration, and 1-click upsells.",
                "audience": "Performance marketers and newsletter operators monetizing paid and organic funnels",
                "research_basis": "FTC ROSCA and Endorsement Guides govern transparent recurring billing, upsell consent, and affiliate substantiation.",
                "sources": ["https://www.law.cornell.edu/uscode/text/15/8403"],
                "validation_status": "Source-informed editorial positioning; not market-tested.",
            },
            {
                "title": "The Multi-SKU Operator Pod",
                "subtitle": "Combine evergreen YouTube, GEO citations, and micro-extensions into a durable digital portfolio.",
                "audience": "Creators and micro-PE buyers rolling up utility extensions, newsletters, and digital libraries",
                "research_basis": "Written work-made-for-hire / IP assignment agreements under 17 U.S.C. 101 and 204(a) secure clean chain of title across contractor-built SKUs.",
                "sources": ["https://www.law.cornell.edu/uscode/text/17/204"],
                "validation_status": "Source-informed editorial positioning; not market-tested.",
            },
        ],
        "chapters": chapters,
        "chapter_count": len(chapters),
        "total_word_count": total_words,
        "epistemic_note": "Educational and research material only, not legal, tax, accounting, or investment advice. Verify tax nexus, billing disclosures, and platform policies independently.",
    }
