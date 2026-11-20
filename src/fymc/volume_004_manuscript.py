"""Volume 004 manuscript, 8 vector diagrams, and citation merger for AI-Powered Micro SaaS."""
from __future__ import annotations

from copy import deepcopy

from .vol004_q01 import CHAPTER_1
from .vol004_q02 import CHAPTER_2
from .vol004_q03 import CHAPTER_3
from .vol004_q04 import CHAPTER_4
from .vol004_q05 import CHAPTER_5
from .vol004_q06 import CHAPTER_6
from .vol004_q07 import CHAPTER_7
from .vol004_q08 import CHAPTER_8
from .vol004_q09 import CHAPTER_9
from .vol004_q10 import CHAPTER_10
from .vol004_q11 import CHAPTER_11
from .vol004_q12 import CHAPTER_12
from .vol004_workbook import build_volume_004_workbook
from .volume_004_citations import BASELINE_EXPERT_CITATIONS_BY_CHAPTER, CHAPTER_KEYWORDS
from .volume_001_manuscript import compute_manuscript_word_count

ALL_VOLUME_004_CHAPTERS = [
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


def build_volume_004_diagrams_data() -> list[dict]:
    """Return 8 structured vector diagram specifications with explicit units and assumptions."""
    specs = [
        (
            "diag-01-micro-saas-wedge-workflow",
            "process_flow",
            "From B2B pain signal to sticky recurring MRR",
            "Five-stage vertical AI micro-SaaS execution loop",
            1,
            "operating_framework",
            "Numeric values indicate engineering and GTM sequence, not guaranteed retention.",
            "Anchor the software around a system-of-work bottleneck and proprietary context rather than an exposed single-prompt wrapper.",
            [
                ("Isolate B2B wedge", "Step 1", 1.0, "Mine technographic churn, G2 1-star complaints, and compliance defects; secure paid pilot LOIs first."),
                ("Ingest domain context", "Step 2", 2.0, "Normalize public registries or tenant documents behind Postgres Row-Level Security and pgvector."),
                ("Route & cache tokens", "Step 3", 3.0, "Dispatch 85% routine tasks to small models, 15% synthesis to frontier models, with semantic caching."),
                ("Deliver <5m value", "Step 4", 4.0, "Ship a pre-loaded diagnostic artifact or workflow copilot output in the user's first session."),
                ("Expand NRR", "Step 5", 5.0, "Compound revenue via metered workflow credits, team seats, embedded VCC rails, and smart dunning."),
            ],
        ),
        (
            "diag-02-scanner-to-mrr-funnel",
            "funnel",
            "Diagnostic scanner outbound to retained B2B logos",
            "Illustrative cohort of 1,000 scanned B2B domains",
            6,
            "illustrative_model",
            "Invented nested cohort counts illustrating outbound/PLG conversion math; actual rates vary by vertical.",
            "Automated compliance, technographic, and migration scanners convert cold outbound into concrete product demos.",
            [
                ("Domains scanned", "1,000", 1000.0, "Automated WCAG, SSL, DNS technographic, or incumbent-pricing scans across qualified B2B domains."),
                ("Verified defect hits", "340", 340.0, "Prospects with a documented compliance gap, renewal window, or broken workflow."),
                ("Interactive trials", "68", 68.0, "Decision-makers inspecting their pre-populated diagnostic workspace or calculator."),
                ("Paying MRR logos", "19", 19.0, "Self-serve or founder-assisted conversions onto a $149-$299/mo hybrid subscription."),
                ("Expanded annual logos", "11", 11.0, "Accounts upgrading to annual prepay, extra seats, or higher metered credit tiers."),
            ],
        ),
        (
            "diag-03-mrr-to-net-margin-waterfall",
            "waterfall",
            "Monthly ARPU to net owner operating margin",
            "Illustrative $150/mo B2B account on unsubsidized compute",
            3,
            "illustrative_model",
            "USD per $150 monthly subscription receipt; opening and closing bars are totals, middle bars are deductions.",
            "Even after startup cloud credits expire, model routing and semantic caching preserve >80% SaaS gross margin and 30%-45% net margin.",
            [
                ("Monthly ARPU", "$150.00", 150.0, "Hybrid $99 base workspace plus $51 average metered workflow and seat expansion."),
                ("LLM & vector compute", "-$14.50", -14.5, "Unsubsidized tiered model inference, embeddings, and managed Postgres/queue allocation."),
                ("Billing & tax rail", "-$7.50", -7.5, "Stripe Billing + Tax or Merchant-of-Record processing and failed-card retry overhead."),
                ("Churn & refund drag", "-$9.00", -9.0, "Amortized involuntary/voluntary churn and prorated ROSCA cancellation credits."),
                ("Contractor & GTM pod", "-$51.50", -51.5, "Allocated part-time engineering, support automation, and acquisition spend at scale."),
                ("Owner net contribution", "$67.50", 67.5, "45% scaled small-team owner margin before personal income taxes and R&D tax timing."),
            ],
        ),
        (
            "diag-04-billing-rail-take-rates",
            "horizontal_bars",
            "Effective take-rate across SaaS billing architectures",
            "Illustrative % fee on a $150/mo B2B subscription",
            2,
            "illustrative_model",
            "Percent of a $150 SaaS charge; excludes state CPA filing fees if managing multi-jurisdiction sales tax directly.",
            "Match the billing rail to buyer geography: MoR eliminates global VAT filings early, while Stripe Billing + ACH optimizes high-ACV B2B.",
            [
                ("Stripe ACH / Wire", "0.8% / $1.20", 0.8, "Capped ACH debit ideal for $1,500-$5,000 annual B2B prepay invoices."),
                ("Stripe Card + Tax", "3.6% / $5.40", 3.6, "2.9% + $0.30 card processing plus ~0.5% Stripe Tax calculation; seller remits state/VAT returns."),
                ("MoR (Paddle / LS)", "5.3% / $8.00", 5.3, "5% + $0.50 Merchant-of-Record fee absorbing global SaaS VAT, US Wayfair nexus, and chargebacks."),
                ("App Store In-App", "30.0% / $45.00", 30.0, "Default mobile store cut (15% Small Business tier) avoided via Web2App external web checkout."),
            ],
        ),
        (
            "diag-05-token-and-churn-guardrail-tree",
            "decision_tree",
            "Inference cost, security & involuntary-churn guardrails",
            "Mandatory production checks before opening public signups",
            5,
            "operating_framework",
            "Numbers identify engineering gates; enforce in middleware before any upstream LLM call.",
            "Prevent weekend token-bill blowups and cross-tenant leaks through hard Redis budgets, RLS isolation, ZDR endpoints, and smart dunning.",
            [
                ("Tenant RLS & cap?", "Node 1", 1.0, "Enforce Postgres tenant_id RLS and hard daily/monthly Redis token ceilings before inference."),
                ("Cache or small model?", "Node 2", 2.0, "Serve repeat queries from cache and route structured extraction to low-cost models first."),
                ("ZDR & eval pass?", "Node 3", 3.0, "Call Zero-Data-Retention enterprise endpoints and block deploys that regress golden evals."),
                ("Smart dunning live?", "Node 4", 4.0, "Run card-updater, pre-expiry alerts, and multi-day retry cadences to cut involuntary churn."),
            ],
        ),
        (
            "diag-06-three-person-saas-pod",
            "org_architecture",
            "One full-time founder, two specialized contractors",
            "Illustrative 3-person ($375k ARR Base Case) SaaS pod",
            11,
            "operating_framework",
            "Numeric values are role identifiers; Scaled ($700k ARR) scenario expands to 2 FT + 3 C.",
            "Keep headcount ultra-lean by automating CI evals, onboarding, and Tier-1 docs deflection before hiring full-time staff.",
            [
                ("Founder / product lead", "1 FT", 1.0, "Owns customer discovery, core architecture, pricing, enterprise trust, and capital allocation."),
                ("Full-stack & eval dev", "1 C", 2.0, "Maintains connectors, RLS migrations, golden-dataset evals, and companion extension releases."),
                ("Growth & CS specialist", "1 C", 3.0, "Runs diagnostic-scanner outbound, comparison calculators, onboarding calls, and churn-save reviews."),
            ],
        ),
        (
            "diag-07-startup-runway-stack",
            "stacked_comparison",
            "Disciplined $15,000 bootstrapped AI micro-SaaS budget",
            "Illustrative launch stack paired with cloud/LLM credit grants",
            4,
            "illustrative_model",
            "USD cash outlay; excludes non-cash AWS/GCP/Azure/LLM startup credits that subsidize early compute.",
            "Cloud credit grants subsidize inference COGS, not founder runway; keep >=50% of cash in liquid reserve until MRR covers fixed opex.",
            [
                ("Entity, IP & DPA setup", "$1,500", 1500.0, "LLC/C-corp formation, banking, contractor IP assignment templates, and baseline privacy/DPA docs."),
                ("Core infra & telemetry", "$1,500", 1500.0, "Domains, managed Postgres/auth/observability tiers, and golden-eval testing harness."),
                ("Scanner & GTM pilots", "$4,000", 4000.0, "Technographic/WCAG scanner infra, comparison-page assets, and bounded paid-search intent tests."),
                ("Liquid runway reserve", "$8,000", 8000.0, "Untouched cash buffer protecting against slow B2B sales cycles and credit-grant expiration."),
            ],
        ),
        (
            "diag-08-thirty-day-mvp-roadmap",
            "timeline_roadmap",
            "Thirty days from buyer interviews to first 10 MRR logos",
            "Four weekly validation, multi-tenant build, outbound & retention gates",
            12,
            "operating_framework",
            "Numeric values are milestone end-days; full 2-9 month ramp applies to stabilized recurring cohorts.",
            "Never spend three months coding in isolation: validate paid pilot commitments in Week 1 and ship a metered multi-tenant wedge by Day 14.",
            [
                ("Validate & pre-sell", "Days 1-7", 7.0, "Mine G2/technographic pain, interview 15 buyers, demo clickable scan, and lock >=3 paid pilot LOIs."),
                ("Ship metered MVP", "Days 8-14", 14.0, "Deploy Postgres RLS, ZDR model router, Redis token caps, semantic cache, and Stripe hybrid billing."),
                ("Launch scanner GTM", "Days 15-21", 21.0, "Activate pilot logos in <5 minutes, run WCAG/churn-scanner outbound, and publish vs-incumbent pages."),
                ("Audit NRR & scale", "Days 22-30", 30.0, "Audit unsubsidized token margin per tenant, enable smart dunning, and apply Day-30 Kill/Scale rules."),
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


def build_volume_004_manuscript(abridged_videos: list[dict] | None = None) -> dict:
    """Build isolated Volume 004 chapter records with attributed, sentence-clean commentary."""
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

    chapters = deepcopy(ALL_VOLUME_004_CHAPTERS)
    diagram_ids = {item["diagram_id"][:7]: item["diagram_id"] for item in build_volume_004_diagrams_data()}
    for chapter in chapters:
        chapter.setdefault("id", f"Q{chapter['chapter_number']}")
        chapter.setdefault("chapter_id", f"Q{chapter['chapter_number']}")
        reference = chapter["diagram_id"]
        prefix = reference[:7]
        if prefix not in diagram_ids or (reference != prefix and not reference.startswith(prefix + "-")):
            raise ValueError("Unknown Volume 004 diagram_id: " + str(reference))
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

    _saas_signals = (
        "saas", "micro saas", "micro-saas", "software", "mrr", "arr", "churn",
        "stripe", "paddle", "token", "llm", "rag", "openai", "anthropic",
        "cloud", "aws", "serverless", "postgres", "chrome extension", "onboarding",
        "plg", "pricing", "subscription", "b2b", "startup", "founder", "bootstrap",
        "api", "webhook", "dunning", "soc 2", "gdpr", "geo",
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
            if not any(sig in haystack for sig in _saas_signals):
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
        "volume_id": "vol-004-ai-powered-micro-saas",
        "volume_number": "004",
        "series_title": "THE BIG MONEY PLAYBOOKS",
        "parent_brand": "THE FUCK YOU MONEY CLUB",
        "tagline": "Big Money. Small Teams. No Bullshit.",
        "title": "AI-POWERED MICRO SAAS",
        "subtitle": "The Complete Playbook for Vertical B2B Wedges, Token Metering, Cloud-Credit Stacks & Scaling a $700k ARR 3-to-5 Person Software Firm",
        "content_architecture_layers": [
            {"layer": 1, "title": "Executive orientation", "description": "Question-led summaries and key metrics establish B2B wedge selection, ARPU, churn, and inference margins."},
            {"layer": 2, "title": "Operator-grade analysis", "description": "Detailed sections separate statutory billing/privacy duties, multi-tenant architectures, unit-economics models, and founder claims."},
            {"layer": 3, "title": "Visual decision support", "description": "Diagrams and tables expose model routing, scanner funnels, MRR contribution waterfalls, and token/churn guardrails."},
            {"layer": 4, "title": "Execution tools", "description": "SOPs, callouts, chapter checklists, and the 6-worksheet companion workbook turn architecture into repeatable MRR."},
            {"layer": 5, "title": "Source evidence", "description": "Statutory/regulatory citations and attributed timestamped commentary distinguish primary rules from practitioner perspective."},
        ],
        "operator_plays": deepcopy(get_candidate_track_metadata(22)["plays"]),
        "min_expert_youtube_links_per_book": MIN_EXPERT_YOUTUBE_LINKS_PER_BOOK,
        "target_expert_youtube_links_per_book": TARGET_EXPERT_YOUTUBE_LINKS_PER_BOOK,
        "min_expert_youtube_links_per_chapter": MIN_EXPERT_YOUTUBE_LINKS_PER_CHAPTER,
        "expert_youtube_link_count": total_yt_links,
        "positioning_alternatives": [
            {
                "title": "The Vertical B2B AI Wedge",
                "subtitle": "Own the workflow bottleneck and domain dataset instead of building a disposable prompt wrapper.",
                "audience": "Technical solo founders and 2-to-5 person B2B SaaS pods",
                "research_basis": "Multi-tenant Row-Level Security, tiered model routing, and semantic caching sustain >80% SaaS gross margins.",
                "sources": ["https://www.nist.gov/itl/ai-risk-management-framework"],
                "validation_status": "Source-informed editorial positioning; not market-tested.",
            },
            {
                "title": "Metered Inference & Zero-Idle Cloud Stacks",
                "subtitle": "Pair hybrid seat-plus-credit billing with cloud grants and multi-provider API routers.",
                "audience": "Bootstrapped software operators engineering profitable day-one unit economics",
                "research_basis": "FTC ROSCA governs transparent recurring SaaS billing and cancellation parity alongside Wayfair digital-tax nexus.",
                "sources": ["https://www.law.cornell.edu/uscode/text/15/8403"],
                "validation_status": "Source-informed editorial positioning; not market-tested.",
            },
            {
                "title": "Diagnostic Scanners & Micro-Extension Rollups",
                "subtitle": "Acquire B2B logos via automated compliance/churn scanners, comparison calculators, and browser extensions.",
                "audience": "PLG engineers and micro-PE operators building 4x-6x ARR exit-ready software assets",
                "research_basis": "Written IP assignments under 17 U.S.C. 204(a) and GDPR Art. 28 DPAs pass buyer and enterprise security diligence.",
                "sources": ["https://www.law.cornell.edu/uscode/text/17/204"],
                "validation_status": "Source-informed editorial positioning; not market-tested.",
            },
        ],
        "chapters": chapters,
        "chapter_count": len(chapters),
        "total_word_count": total_words,
        "epistemic_note": "Educational and research material only, not legal, tax, accounting, security, or investment advice. Verify data-protection, billing, and tax obligations independently.",
    }
