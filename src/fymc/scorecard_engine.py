"""Editorial scorecards; economics are illustrative USD planning assumptions.

Confidence and production stages are supplied editorial classifications, not
claims that this module has verified sources or reviewed a research corpus.
Ranges describe operating businesses, not guaranteed startup outcomes. A new
operator can earn nothing or lose capital. Scores are judgment-based, not
investment advice; uncertainty bands are not statistical confidence intervals.
"""

from __future__ import annotations

from copy import deepcopy
from math import isfinite
import re

SCORE_KEYS = ("money_to_manpower_score", "total_score", "composite_score", "score")
_SCORE_STRING_RE = re.compile(r"^\s*([+-]?\d+(?:\.\d+)?)\s*(?:/\s*100)?\s*$")


def resolve_score_value(scorecard: dict | None, default: float | None = None) -> float | None:
    """Resolve the numeric composite score deterministically without truthiness traps."""
    if not isinstance(scorecard, dict):
        return default
    for key in SCORE_KEYS:
        if key not in scorecard:
            continue
        raw = scorecard[key]
        if raw is None or isinstance(raw, bool):
            continue
        if isinstance(raw, (int, float)):
            try:
                as_float = float(raw)
            except (ValueError, OverflowError):
                continue
            if isfinite(as_float):
                return int(raw) if isinstance(raw, int) else (int(as_float) if as_float.is_integer() else as_float)
            continue
        if isinstance(raw, str):
            match = _SCORE_STRING_RE.match(raw)
            if match:
                try:
                    parsed = float(match.group(1))
                except (ValueError, OverflowError):
                    continue
                if isfinite(parsed):
                    return int(parsed) if parsed.is_integer() else parsed
    return default

SCORE_DIMENSIONS = {
    "revenue_potential": 25,
    "profit_margin_potential": 25,
    "team_efficiency": 20,
    "startup_accessibility": 15,
    "automation_potential": 15,
}
DIMENSION_LABELS = {
    "revenue_potential": "Revenue Potential",
    "profit_margin_potential": "Profit Margin Potential",
    "team_efficiency": "Team Efficiency",
    "startup_accessibility": "Startup Accessibility",
    "automation_potential": "Automation Potential",
}
_CONFIDENCE_BANDS = {
    "High": "±3 pts",
    "Moderate": "±6 pts",
    "Preliminary — Uncertainty Range": "±10 pts",
}

TRACK_DEFINITIONS = {
    "track_1": {
        "id": "track_1",
        "code": "TRACK 01",
        "name": "Asymmetric & Data-Arbitrage Plays",
        "short_label": "Track 1 · Asymmetric & Data Arbitrage",
        "summary": (
            "100% legal, high-edge operator models built on public-record and API "
            "intelligence, public Telegram channel/deal-room signal scraping, expired "
            "domain/traffic arbitrage, programmatic SEO, and distressed asset recovery "
            "where small automated teams exploit data latency and fragmented registries."
        ),
    },
    "track_2": {
        "id": "track_2",
        "code": "TRACK 02",
        "name": "Grey-Zone Growth & Traffic Arbitrage",
        "short_label": "Track 2 · Grey-Zone Growth & Traffic Arbitrage",
        "summary": (
            "Aggressive, high-velocity acquisition mechanics—parasitic SEO, high-velocity "
            "affiliate funnels, trigger-based DM outbound systems, SERP Navboost CTR "
            "engineering, viral distribution loops, and paid-to-organic media arbitrage—"
            "paired with forensic teardowns of naive blackhat traps and explicit platform-policy fallbacks."
        ),
    },
}

PLAY_DEFINITIONS = {
    "public_record_api_intelligence": {
        "id": "public_record_api_intelligence",
        "track_id": "track_1",
        "name": "Public-Record & API Intelligence",
        "mechanism": (
            "Ingest fragmented county dockets, probate registries, unclaimed property ledgers, "
            "and public APIs to surface uncontested claims or high-intent B2B triggers before "
            "manual competitors."
        ),
        "inputs": ["Court & probate dockets", "State controller ledgers", "Public licensing & entity APIs"],
        "workflow": [
            "Poll and normalize county/state record releases on an automated cadence",
            "Cross-match entity/kinship/lien records and filter by minimum net fee threshold",
            "Route verified dossiers into compliant outreach and claim execution",
        ],
        "metrics": ["Cost per verified lead", "Docket-to-contact latency (hours)", "Net recovery / conversion rate"],
        "platform_risks": [
            {
                "failure_mode": "Portal rate-limiting or CAPTCHA gating",
                "trigger": "High-frequency automated polling against county or agency web portals",
                "impact": "Delayed lead ingestion or temporary IP block on target registry",
                "detection_metric": "HTTP 429/403 rate and daily record ingestion delta",
                "fallback": "Switch to scheduled bulk FOIA/public-record exports, official data feeds, and low-frequency cached queues",
            },
        ],
    },
    "expired_domain_traffic_arbitrage": {
        "id": "expired_domain_traffic_arbitrage",
        "track_id": "track_1",
        "name": "Expired Authority Domain (.gov/.edu/Media) Rebuilds & Traffic Arbitrage",
        "mechanism": (
            "Acquire dropped or auctioned domains carrying clean historical backlinks from .gov, .edu, "
            "major media, and trade publications, then rebuild strict topical-continuity authority hubs "
            "and monetize via high-payout lead routing and affiliate offers."
        ),
        "inputs": ["Registrar drop lists & closeout auctions", "Historical archive snapshots (.gov/.edu/editorial link equity)", "Backlink & anchor-text profiles"],
        "workflow": [
            "Screen auction and drop feeds for non-trademarked domains with clean editorial/.gov/.edu backlinks",
            "Verify clean indexing history and absence of toxic spam penalties",
            "Restore strict topical continuity with the historical archive theme and route qualified traffic to high-margin lead/affiliate offers",
        ],
        "inputs_note": "Strictly excludes trademarked terms or deceptive brand impersonation.",
        "metrics": ["Acquisition cost vs. 6-month traffic value", "Indexation retention %", "RPM / revenue per visitor"],
        "platform_risks": [
            {
                "failure_mode": "Search engine expired-domain abuse classification / deindexing",
                "trigger": "Abrupt topical pivot (e.g., defunct civic site to unrelated casino/loan spam) or thin auto-generated content",
                "impact": "Loss of historical ranking authority and organic search impressions",
                "detection_metric": "Indexed page ratio and non-brand impression trend in Search Console",
                "fallback": "Keep strict topical continuity with historical archive theme and capture first-party email opt-ins on entry",
            },
        ],
    },
    "programmatic_seo": {
        "id": "programmatic_seo",
        "track_id": "track_1",
        "name": "Programmatic SEO",
        "mechanism": (
            "Combine structured proprietary datasets (pricing benchmarks, local regulations, "
            "provider directories, calculator matrices) with high-utility page templates to capture "
            "thousands of long-tail commercial-intent queries."
        ),
        "inputs": ["Normalized proprietary dataset", "Long-tail intent taxonomy", "Interactive calculator / comparison templates"],
        "workflow": [
            "Assemble verifiable structured data rows with unique per-entity attributes",
            "Render fast, high-utility comparison and calculator pages with zero duplicate boilerplate",
            "Monetize high-intent visitors via B2B lead routing, SaaS signups, or high-ticket referrals",
        ],
        "metrics": ["Indexed-to-submitted sitemap ratio", "Organic conversions per 1,000 pages", "Customer acquisition cost (CAC)"],
        "platform_risks": [
            {
                "failure_mode": "Scaled content / thin-page deindexing during core search updates",
                "trigger": "Publishing near-identical template pages without unique underlying data value",
                "impact": "Crawl-budget throttling or sitewide organic traffic drop",
                "detection_metric": "'Crawled - currently not indexed' count and average time-on-page",
                "fallback": "Enforce minimum data-density gates per URL, prune zero-impression pages, and funnel traffic into owned tools/newsletters",
            },
        ],
    },
    "distressed_asset_recovery": {
        "id": "distressed_asset_recovery",
        "track_id": "track_1",
        "name": "Distressed Asset Recovery",
        "mechanism": (
            "Locate mispriced, orphaned, or administratively stranded assets—tax-sale overages, "
            "unclaimed state funds, dormant judgments, government surplus lots, or distressed "
            "micro-businesses—and capture a contingent recovery fee or acquisition spread."
        ),
        "inputs": ["Tax-sale excess proceeds ledgers", "Unclaimed property & judgment dockets", "Surplus auction manifests"],
        "workflow": [
            "Audit statutory fee caps, claim windows, and chain-of-title encumbrances",
            "Execute skip-tracing or asset inspection to confirm net realizable value",
            "Lock in contingent recovery agreements or below-intrinsic buyouts",
        ],
        "metrics": ["Gross spread / contingent fee per case", "Claim approval rate", "Days from filing to disbursement"],
        "platform_risks": [
            {
                "failure_mode": "Statutory fee-cap compression or administrative hold",
                "trigger": "Jurisdiction updates finder fee limits, waiting periods, or filing documentation rules",
                "impact": "Reduced net fee margin or extended cash conversion cycle",
                "detection_metric": "County/state rejection notice rate and days-to-payout variance",
                "fallback": "Diversify across multi-state dockets and use attorney-backed filing partnerships where required",
            },
        ],
    },
    "parasitic_seo": {
        "id": "parasitic_seo",
        "track_id": "track_2",
        "name": "Parasitic SEO & High-DR Subfolder Leasing",
        "mechanism": (
            "Publish deeply researched commercial comparisons, calculators, and buyer guides on "
            "high-authority third-party trade publications, leased DR 80+ '/guides/' subfolders, "
            "and community domains to rank #1–#3 for competitive buyer keywords within 48 hours."
        ),
        "inputs": ["High-DR niche trade publications & leased subfolders", "High-CPC buyer-intent keyword clusters", "Conversion-tested quiz & comparison bridge modules"],
        "workflow": [
            "Partner with topically relevant high-DR trade publications or authority platforms that index rapidly for commercial queries",
            "Deploy substantive, data-backed comparison and calculator placements with tracked referral CTAs",
            "Siphon third-party placement traffic immediately into owned quiz/calculator bridge pages and first-party email/SMS lists",
        ],
        "metrics": ["Time-to-top-3 ranking (days)", "Click-through rate to owned bridge page", "Net commission per placement"],
        "platform_risks": [
            {
                "failure_mode": "Host removal or Google Site Reputation Abuse manual/algorithmic demotion",
                "trigger": "Leasing subfolders on generic news sites for unrelated coupon/casino topics or host moderation of outbound links",
                "impact": "Sudden removal or ranking drop of hosted placement URLs",
                "detection_metric": "HTTP status/canonical monitor on hosted URLs and SERP rank tracker alerts",
                "fallback": "Partner strictly with topically aligned trade publications and treat hosted placements as top-of-funnel feeders into owned email/SMS lists",
            },
        ],
    },
    "high_velocity_affiliate_funnels": {
        "id": "high_velocity_affiliate_funnels",
        "track_id": "track_2",
        "name": "High-Velocity Affiliate Funnels",
        "mechanism": (
            "Pair rapid-deployment pre-sell bridge pages, comparison quizzes, and automated follow-up "
            "sequences with high-ticket recurring or CPA offers to maximize earnings per click (EPC)."
        ),
        "inputs": ["High-ticket / recurring merchant offers", "Pre-sell quiz & comparison bridge funnels", "Server-side conversion tracking"],
        "workflow": [
            "Route intent-matched traffic to a fast pre-qualification bridge page rather than raw merchant links",
            "Capture lead opt-in before handoff so non-converting clicks enter automated follow-up sequences",
            "Split-test offer routing dynamically by EPC and reversal rate",
        ],
        "metrics": ["Earnings per click (EPC)", "Bridge-page opt-in rate", "Net payout after reversals/clawbacks"],
        "platform_risks": [
            {
                "failure_mode": "Affiliate commission cuts, clawbacks, or attribution loss",
                "trigger": "Merchant changes payout terms, cookie windows expire, or ad platforms reject bridge pages",
                "impact": "Margin compression or retroactive commission reversals",
                "detection_metric": "EPC drop >15% or reversal/refund rate exceeding historical baseline",
                "fallback": "Maintain multi-merchant offer rotation on owned bridge links and monetize captured email leads directly",
            },
        ],
    },
    "viral_distribution_loops": {
        "id": "viral_distribution_loops",
        "track_id": "track_2",
        "name": "Viral Distribution Loops",
        "mechanism": (
            "Engineer shareable interactive outputs, programmatic short-form media variants, and "
            "incentivized referral unlocks so every user action or content batch seeds organic distribution."
        ),
        "inputs": ["Interactive tool / template assets", "Short-form distribution accounts", "Referral milestone unlock mechanics"],
        "workflow": [
            "Embed native watermark/attribution or referral-unlock hooks into user-generated outputs",
            "Syndicate high-retention hooks across short-form and community feeds pointing to a central capture hub",
            "Convert viral spikes into durable product sales, SaaS trials, or subscriber cohorts",
        ],
        "metrics": ["Viral K-factor / share rate", "Organic impressions per asset batch", "Visitor-to-owned-subscriber conversion %"],
        "platform_risks": [
            {
                "failure_mode": "Algorithmic reach throttling or account shadow-limiting",
                "trigger": "Social platforms penalize repetitive template formats or aggressive outbound link prompts",
                "impact": "Sharp decay in organic feed impressions and click-through volume",
                "detection_metric": "Non-follower reach ratio and outbound link CTR per post",
                "fallback": "Rotate native creative formats, avoid spammy engagement bait, and convert viewers into owned email/SMS channels",
            },
        ],
    },
    "paid_to_organic_media_arbitrage": {
        "id": "paid_to_organic_media_arbitrage",
        "track_id": "track_2",
        "name": "Paid-to-Organic Media Arbitrage",
        "mechanism": (
            "Acquire underpriced clicks from secondary ad networks, newsletter sponsorships, and "
            "long-tail search queries, then monetize the spread via higher-yield B2B lead sales, "
            "high-ticket affiliate payouts, and organic retargeting loops."
        ),
        "inputs": ["Low-CPC ad & sponsorship inventory", "High-RPM / high-CPL monetization endpoints", "Cohort ROAS & LTV attribution ledger"],
        "workflow": [
            "Buy targeted traffic where CPC is priced below the realized first-session + 30-day email value",
            "Segment incoming visitors via instant qualification prompts to route high-value leads to premium buyers",
            "Recycle organic search and newsletter return visits at zero marginal media cost",
        ],
        "metrics": ["Day-1 vs. Day-30 ROAS spread", "Realized RPM minus effective CPC", "Lead acceptance rate"],
        "platform_risks": [
            {
                "failure_mode": "Traffic-cost spikes, ad-account restrictions, or attribution blind spots",
                "trigger": "Auction CPC inflation, ad-network creative disapprovals, or browser tracking restrictions",
                "impact": "Negative front-end arbitrage spread and wasted ad spend",
                "detection_metric": "Hourly CPC-to-EPC ratio and server-side conversion match rate",
                "fallback": "Enforce automated spend circuit-breakers when spread narrows and rely on first-party newsletter monetization",
            },
        ],
    },
    "telegram_channel_signal_scraping": {
        "id": "telegram_channel_signal_scraping",
        "track_id": "track_1",
        "name": "Telegram Channel & Deal-Room Signal Scraping",
        "mechanism": (
            "Ingest public Telegram channel broadcasts, OTC deal rooms, wholesale distress feeds, "
            "and niche community message streams in real time to extract high-intent buyer/seller "
            "triggers before they hit public search—while avoiding naive member-list scraping traps."
        ),
        "inputs": [
            "Public Telegram channel & group broadcast streams",
            "Keyword & entity-regex signal filters",
            "Inbound utility-bot & deal-desk capture endpoints",
        ],
        "workflow": [
            "Monitor public channel message history and live broadcast streams for high-intent deal keywords (buying, distressed lot, urgent allocation, broker needed)",
            "Score and deduplicate message authors and deal metadata against minimum ticket thresholds without scraping hidden member rosters",
            "Route verified deal signals to an operator desk or deploy a pinned niche utility bot (alert/calculator/directory) that converts channel readers into inbound leads",
        ],
        "metrics": [
            "Signal-to-response latency (seconds)",
            "Qualified deal triggers per 1,000 messages",
            "Inbound bot opt-in & close rate",
        ],
        "platform_risks": [
            {
                "failure_mode": "MTProto session ban (UserDeactivatedBanError) or FloodWaitError throttling",
                "trigger": "Aggressive GetParticipantsRequest calls on hidden member lists or high-frequency polling from VoIP virtual SIMs",
                "impact": "Immediate termination of listener sessions and loss of real-time channel feed ingestion",
                "detection_metric": "Telegram FloodWaitError seconds per hour and session disconnect rate",
                "fallback": "Restrict ingestion to passive read-only public broadcast listeners and capture prospects inbound via official Bot API utility bots",
            },
        ],
    },
    "high_velocity_dm_outbound_systems": {
        "id": "high_velocity_dm_outbound_systems",
        "track_id": "track_2",
        "name": "High-Velocity DM Outbound & Trigger Funnels",
        "mechanism": (
            "Replace blind cold mass-DM blasts (which die to PeerFloodError and silent Message Request "
            "graveyards) with high-velocity comment-to-DM triggers, hand-raiser reaction hooks, and "
            "multi-inbox warm signal routing."
        ),
        "inputs": [
            "Short-form / community trigger posts ('Comment KEYWORD')",
            "Signal-verified prospect handles",
            "Automated DM qualification & booking bridge",
        ],
        "workflow": [
            "Publish high-curiosity teardown or resource posts where prospects comment a trigger keyword or react to unlock a playbook or calculator",
            "Deliver instant automated DM replies to warm hand-raisers (bypassing cold-DM filters because the user initiated interaction) or send contextual 1-to-1 DMs referencing an active public request",
            "Qualify budget and timeline inside a 3-message DM micro-funnel and transition immediately to a booked call, checkout link, or owned SMS/email list",
        ],
        "metrics": [
            "Trigger-comment to DM delivery rate",
            "DM reply-to-qualified-conversation %",
            "Revenue per 100 DM threads",
        ],
        "platform_risks": [
            {
                "failure_mode": "PeerFloodError, shadow-filtering into 'Hidden Requests', or link-domain blacklisting",
                "trigger": "Sending identical unsolicited cold DMs with raw external URLs across freshly registered or SIM-farmed accounts",
                "impact": "Near-0% inbox placement, outbound DM block, or permanent account suspension",
                "detection_metric": "Seen/reply ratio below 10% and outbound PeerFloodError / action-block frequency",
                "fallback": "Require user-initiated trigger action (comment/reaction/inbound message) before automated DM dispatch and send external links only after the prospect replies",
            },
        ],
    },
    "serp_signal_navboost_engineering": {
        "id": "serp_signal_navboost_engineering",
        "track_id": "track_2",
        "name": "SERP Signal & Navboost CTR Engineering",
        "mechanism": (
            "Target Google's Navboost and Glue click-log re-ranking systems (goodClicks vs. badClicks "
            "and lastLongestClicks) not with synthetic proxy click-bots—which get squashed by Chrome "
            "session/entropy filters—but by engineering real-human Branded Search Seeding and high-dwell interactive pages."
        ),
        "inputs": [
            "Search Console #3-#10 high-impression query targets",
            "Short-form / newsletter Branded Search Seeding prompts",
            "Above-the-fold interactive calculator / lookup tools",
        ],
        "workflow": [
            "Identify commercial queries ranking positions #3-#10 where beating the expected positional CTR curve triggers Navboost promotion",
            "Seed real human search demand via social videos, communities, and newsletters instructing users to Google '[Target Keyword] + [Brand]' instead of clicking a direct URL",
            "Capture the click onto an interactive calculator or live database table so the user spends 3+ minutes on-page and terminates their search session without pogo-sticking (lastLongestClick)",
        ],
        "metrics": [
            "Positional CTR delta vs. SERP baseline",
            "Search Console branded + target keyword impression growth",
            "Average engaged dwell time & lastLongestClick retention",
        ],
        "platform_risks": [
            {
                "failure_mode": "Navboost click squashing or Search Console spam-classifier demotion",
                "trigger": "Using headless browsers, 4G/residential proxy rotators, or automated click farms lacking real signed-in Chrome profile entropy",
                "impact": "Zero ranking lift (phantom impressions purged from Search Console) or algorithmic ranking demotion",
                "detection_metric": "Divergence between Search Console reported clicks and verified human tool interactions",
                "fallback": "Never use synthetic proxy click-bots; drive 100% real human Chrome searchers via Branded Search Seeding and optimize title/snippet hooks for organic CTR",
            },
        ],
    },
    "public_filing_trigger_mail_arbitrage": {
        "id": "public_filing_trigger_mail_arbitrage",
        "track_id": "track_1",
        "name": "New-LLC & Recorded-Deed Trigger-Mail Arbitrage",
        "mechanism": (
            "Ingest daily Secretary of State new-LLC filings and County Recorder new-deed/mortgage "
            "recordings to trigger programmatic direct mail via API—replacing illegal government-lookalike "
            "poster/deed invoices (which violate 39 U.S.C. § 3001 and state deed-solicitation laws) with "
            "high-LTV recurring workplace compliance subscriptions, property-tax appeal contingency offers, "
            "and exclusive new-mover/B2B lead monetization."
        ),
        "inputs": [
            "Daily Secretary of State new-entity (LLC/Corp) bulk feeds",
            "County Recorder grant/warranty deed & mortgage recording dockets",
            "Programmatic print-and-mail API (Lob / PostGrid) + QR intake bridge",
        ],
        "workflow": [
            "Pull daily new-LLC formations (filtering for employer/commercial NAICS or multi-member filings) and newly recorded residential deeds with purchase price and loan metadata",
            "Dispatch transparent, non-governmental trigger mailers within 24–48 hours of filing with personalized QR codes pre-populating entity or parcel data",
            "Monetize new LLCs via recurring annual labor-poster/registered-agent compliance memberships and B2B partner referrals; monetize new deeds via contingency property-tax appeal filings or high-ticket homeowner lead sales",
        ],
        "metrics": [
            "Filing-to-mailbox latency (hours)",
            "QR scan & intake conversion % per 1,000 mailers",
            "Annualized LTV / net revenue per mailed piece",
        ],
        "platform_risks": [
            {
                "failure_mode": "USPS 39 U.S.C. § 3001(h)-(i) mail-stop order, State AG UDAP enforcement, or payment-processor freeze",
                "trigger": "Styling mailers as fake government penalty notices, invoices, or charging $89-$195 solely for a $3 public deed copy without statutory disclaimers",
                "impact": "Civil restitution penalties, merchant account termination, and 30%+ chargeback rates",
                "detection_metric": "Refund/chargeback ratio >1% and customer support inquiries mistaking the mailer for a government agency",
                "fallback": "Use unambiguous private commercial branding, never mimic government seals or citation numbers, and sell genuine value-add subscriptions (annual compliance updates, tax-assessment appeals, or B2B services)",
            },
        ],
    },
    "newly_registered_domain_trigger_arbitrage": {
        "id": "newly_registered_domain_trigger_arbitrage",
        "track_id": "track_1",
        "name": "Newly Registered Domain (NRD) & DNS-Diagnostic Trigger Arbitrage",
        "mechanism": (
            "Ingest daily ICANN CZDS Newly Registered Domain (NRD) zone diffs and .us unredacted RDAP "
            "feeds, cross-match domain tokens against Secretary of State LLC filings to resolve physical "
            "mailing addresses despite WHOIS privacy, and run automated 72-hour DNS/HTTP probes (0 Google "
            "indexed pages, missing sitemap.xml, missing SPF/DMARC) to trigger personalized diagnostic mailers."
        ),
        "inputs": [
            "ICANN CZDS daily zone-file diffs & unredacted .us RDAP feeds",
            "30-day Secretary of State LLC/Corp & USPTO entity cross-match index",
            "Automated 72-hour DNS (SPF/DKIM/DMARC) & HTTP (sitemap.xml / Google index) scanner",
        ],
        "workflow": [
            "Cross-match daily NRD registrations against new SOS LLC filings and .us RDAP records to resolve founder name and street address",
            "Probe each resolved domain at 72 hours for unindexed status, missing sitemap.xml/robots.txt, and unconfigured SPF/DMARC email authentication",
            "Dispatch a personalized diagnostic scorecard mailer with a QR code offering a $149 1-click Search Console + IndexNow + DNS/DMARC launch fix, recurring local SEO retainers, and high-CPA SaaS/hosting referrals",
        ],
        "metrics": [
            "NRD-to-physical-address resolution rate (%)",
            "QR diagnostic scan & $149 tripwire conversion %",
            "Upsell rate to recurring SEO/AI agency retainers + affiliate EPC",
        ],
        "platform_risks": [
            {
                "failure_mode": "39 U.S.C. § 3001(h)-(i) deceptive invoice enforcement, registrar abuse complaints, or WHOIS redaction blind spots",
                "trigger": "Sending fake 'Domain Registry / Google Activation' bills or scraping RDAP endpoints above rate limits",
                "impact": "USPS mail-stop orders, merchant processor termination, or RDAP IP rate-limiting",
                "detection_metric": "Customer confusion inquiries, chargeback ratio >1%, and RDAP HTTP 429 response rate",
                "fallback": "Use ICANN CZDS bulk zone files + SOS LLC cross-matching instead of high-frequency WHOIS scraping, and present mailers strictly as a private technical diagnostic audit with real DNS/sitemap fixes",
            },
        ],
    },
    "identity_graph_pixel_arbitrage": {
        "id": "identity_graph_pixel_arbitrage",
        "track_id": "track_2",
        "name": "Identity-Graph Pixel & Search-Intent Deanonymization",
        "mechanism": (
            "Deploy first-party CNAME identity-resolution pixels and pre-click search/bidstream intent "
            "feeds (syncing visitor IP/device hashes against publisher co-op SHA-256 rainbow tables and "
            "property/B2B graphs) to resolve 35–55% of anonymous bouncing search visitors into verified "
            "names, emails, LinkedIn profiles, and physical home addresses."
        ),
        "inputs": [
            "First-party CNAME identity-resolution pixel & Google Ads ValueTrack ({keyword}) URL tags",
            "Publisher co-op SHA-256 HEM spine + County Assessor / B2B LinkedIn enrichment graph",
            "Automated physical postcard API (Lob / PostGrid), B2B Slack routing, & Custom Audience sync",
        ],
        "workflow": [
            "Geo-fence pixel execution at the CDN edge (US-only, excluding EU/UK GDPR traffic) and capture exact referring search keywords via ValueTrack parameters",
            "Resolve anonymous bouncing visitors against the identity spine within 200ms to append homeowner address, work email, and LinkedIn URL",
            "Route resolved B2B executives to instant Slack/LinkedIn warm outreach, trigger physical next-day postcards to resolved homeowner addresses, and sync SHA-256 hashes into Meta/Google Custom Audiences",
        ],
        "metrics": [
            "Anonymous visitor-to-identity match rate (35–55% target)",
            "Cost per resolved identity ($0.10–$0.25) vs. net recovered revenue per 1,000 bounces",
            "Postcard & B2B LinkedIn intercept conversion rate (%)",
        ],
        "platform_risks": [
            {
                "failure_mode": "Primary email domain blacklisting (>0.3% spam complaint rate) or California CIPA / state privacy demand letters",
                "trigger": "Blasting cold consumer Gmail addresses from primary brand domains saying 'we saw you on our site' or firing third-party pixels without geo-fencing/consent notice",
                "impact": "Google Workspace / ESP domain suspension or statutory privacy settlement costs",
                "detection_metric": "Postmaster Tools spam rate >0.1%, bounce rate >2%, and edge geo-fence block verification",
                "fallback": "Never cold-email unconsented consumer Gmail addresses from primary domains; monetize consumer matches strictly via CAN-SPAM-exempt physical trigger mail and SHA-256 ad-audience sync, and enforce US-only edge geo-gating",
            },
        ],
    },
    "competitor_intent_comparison_hijacking": {
        "id": "competitor_intent_comparison_hijacking",
        "track_id": "track_2",
        "name": "Programmatic 'Alternative To / Pricing / Cancel' Intent Hijacking",
        "mechanism": (
            "Generate programmatic nominative-fair-use comparison matrices, live fee calculators, and "
            "migration guides targeting bottom-of-funnel '[Competitor] pricing', '[Competitor] cancel', "
            "and '[Competitor] vs [Offer]' queries to intercept buyers with 10–18% conversion rates."
        ),
        "inputs": [
            "Competitor pricing tiers, hidden-fee schedules, & cancellation friction data",
            "Bottom-of-funnel '[Brand] pricing / alternative / vs' keyword taxonomy",
            "Interactive side-by-side TCO (Total Cost of Ownership) switching calculator",
        ],
        "workflow": [
            "Ingest verified public pricing, contract lock-in terms, and fee schedules across 100+ incumbent providers in the target vertical",
            "Publish objective, factual side-by-side comparison matrices and switching calculators under nominative fair use",
            "Offer a 1-click migration concierge or instant savings quote that routes high-intent switchers into owned SaaS, agency, or high-ticket affiliate offers",
        ],
        "metrics": [
            "Bottom-of-funnel visitor-to-lead conversion % (10–18% target)",
            "Earnings per click (EPC) on switching-intent queries",
            "Organic top-3 SERP share across '[Competitor] pricing/alternative' clusters",
        ],
        "platform_risks": [
            {
                "failure_mode": "UDRP trademark complaint, DMCA notice, or false-advertising cease-and-desist",
                "trigger": "Impersonating competitor login pages, using trademarked logos deceptively, or publishing fabricated competitor pricing",
                "impact": "Page takedown demand or affiliate partner account review",
                "detection_metric": "Quarterly pricing fact-check audit log and legal/compliance inbox alerts",
                "fallback": "Rely strictly on nominative fair use (text-only brand names, timestamped public pricing citations, and zero logo spoofing)",
            },
        ],
    },
    "social_to_search_ping_post_arbitrage": {
        "id": "social_to_search_ping_post_arbitrage",
        "track_id": "track_2",
        "name": "Social-to-Search Ad Feed & Ping-Post Lead Arbitrage",
        "mechanism": (
            "Buy $0.05–$0.12 curiosity clicks on Meta, TikTok, NewsBreak, and native ad networks and "
            "route them through a 4-question qualification bridge—replacing fragile $1.50 RSOC/AFD "
            "search-feed clicks with direct $45–$180 Ping-Post lead auctions."
        ),
        "inputs": [
            "Low-CPC social/native ad hooks ($0.05–$0.12 CPC)",
            "Fast 4-question conditional qualification quiz + TCPA consent capture",
            "Real-time Ping-Post lead distribution engine (Boberdoo / Leadspedia / Phonexa) + RSOC downsell feed",
        ],
        "workflow": [
            "Acquire low-cost social and native clicks using compliant consumer-benefit hooks (tax appeals, solar rebates, insurance audits, surplus claims)",
            "Pre-qualify zip code, homeowner/business status, and urgency inside a zero-friction 4-step quiz bridge",
            "Auction verified exclusive leads in real time via Ping-Post for $45–$180/lead and monetize non-qualifying traffic via compliant secondary search/affiliate offers",
        ],
        "metrics": [
            "Effective media cost per qualified lead (CPL) vs. Ping-Post auction payout",
            "Ping-to-Post acceptance rate (%) and sub-500ms auction response time",
            "Net arbitrage margin after ad spend and buyer returns",
        ],
        "platform_risks": [
            {
                "failure_mode": "Ad-account ban, RSOC/AFD feed termination, or TCPA consent challenge",
                "trigger": "Using fake 'government stimulus' ad bait, forcing accidental ad clicks, or selling leads without one-to-one TCPA consent logs",
                "impact": "Ad account suspension, feed clawbacks, or buyer lead rejections",
                "detection_metric": "Ad disapproval rate, buyer return rate >5%, and TrustedForm/Jornaya certificate match rate (100% required)",
                "fallback": "Enforce 100% factual ad hooks, log cryptographic TrustedForm/Jornaya session certificates on every form submit, and diversify across 5+ direct lead buyers",
            },
        ],
    },
    "chrome_extension_contextual_arbitrage": {
        "id": "chrome_extension_contextual_arbitrage",
        "track_id": "track_2",
        "name": "Chrome Extension & Micro-Tool Contextual Deal/Fee Arbitrage",
        "mechanism": (
            "Acquire or launch free high-utility Chrome extensions and browser calculators (50,000+ users) "
            "that surface visible, opt-in savings, fee-cap, or vendor comparisons at the exact moment a "
            "user views a target docket, SaaS checkout, or supplier portal—without blackhat cookie stuffing."
        ),
        "inputs": [
            "Chrome Web Store utility extension (docket helper, fee calculator, B2B price checker)",
            "Manifest V3 declarative URL/DOM contextual trigger rules",
            "Opt-in comparison drawer with high-payout affiliate and lead-gen endpoints",
        ],
        "workflow": [
            "Grow or acquire a niche Manifest V3 Chrome extension solving a recurring daily workflow (e.g., parcel lookup, e-commerce fee calculator, freight rate check)",
            "Detect when the user visits a high-intent commercial URL and display a clean, non-intrusive opt-in badge ('3 lower-fee providers available for this state/item')",
            "Credit affiliate or lead bounty only when the user explicitly clicks the comparison prompt",
        ],
        "metrics": [
            "Weekly active extension users (WAU) & uninstall rate (<2%/mo)",
            "Contextual prompt CTR (%) and monthly revenue per 1,000 active users",
            "Customer acquisition cost ($0 organic CWS search + micro-acquisitions)",
        ],
        "platform_risks": [
            {
                "failure_mode": "Chrome Web Store removal or affiliate network termination for cookie stuffing",
                "trigger": "Firing hidden background iframes/tabs to overwrite affiliate cookies without explicit user click or requesting excessive host permissions",
                "impact": "Immediate Chrome Web Store delisting and forfeiture of unpaid affiliate commissions",
                "detection_metric": "CWS policy warning alerts and 100% user-initiated click-event attestation per affiliate redirect",
                "fallback": "Never auto-fire background affiliate links; use narrow activeTab/declarativeContent permissions and require an explicit user click on every offer",
            },
        ],
    },
    "rank_and_rent_pay_per_call_routing": {
        "id": "rank_and_rent_pay_per_call_routing",
        "track_id": "track_2",
        "name": "Rank-and-Rent Digital Real Estate & Pay-Per-Call Routing",
        "mechanism": (
            "Build and rank local high-ticket service hubs (foundation repair, water restoration, probate "
            "liquidation, commercial roofing) wired to dynamic call-tracking switches (Ringba / Twilio) "
            "that auto-bill local operators $75–$300 per inbound call lasting over 90 seconds."
        ),
        "inputs": [
            "City + high-ticket emergency/specialty service domain portfolio",
            "Ringba / Twilio dynamic number insertion (DNI) & IVR duration billing switch",
            "Co-verified local contractor partner agreements with card-on-file auto-recharge",
        ],
        "workflow": [
            "Launch fast programmatic local service pages and cost calculators for high-ticket, high-urgency verticals ($5,000+ average job ticket)",
            "Partner with a licensed brick-and-mortar operator in each city for legitimate Google Business Profile co-verification while retaining ownership of the domain and tracking numbers",
            "Route inbound prospect calls through Ringba with a 90-second duration threshold, automatically charging the partner's card on file per qualified call",
        ],
        "metrics": [
            "Inbound calls per site per month & % of calls >90 seconds",
            "Revenue per qualified call ($75–$300) and contractor retention rate",
            "Portfolio gross margin (80–90% once ranked)",
        ],
        "platform_risks": [
            {
                "failure_mode": "Google Business Profile suspension or contractor payment default",
                "trigger": "Registering fake Google Maps pins at UPS stores/virtual offices or delivering calls before collecting prepaid credit balances",
                "impact": "Loss of Map Pack call volume or uncollected call receivables",
                "detection_metric": "Organic-vs-Maps call split and prepaid Stripe wallet balance per partner",
                "fallback": "Anchor traffic in organic city/calculator pages (immune to GBP suspension), co-verify Maps only with real partner physical addresses, and enforce prepaid auto-refill call wallets",
            },
        ],
    },
    "ego_bait_directory_badge_arbitrage": {
        "id": "ego_bait_directory_badge_arbitrage",
        "track_id": "track_1",
        "name": "Industry Award & Verified Directory 'Ego-Bait' Badge Arbitrage",
        "mechanism": (
            "Publish data-scored state and city rankings ('Top 15 Verified Specialists in [City]') and "
            "issue free embeddable 'Top Rated' winner badges to ranked firms—earning hundreds of free "
            "high-DR backlinks when firms post the badge on their own sites, while upselling $299–$799/mo "
            "Featured #1 Lead-Capture placements."
        ),
        "inputs": [
            "Public state licensing, inspection, & review dataset for 500+ firms per vertical",
            "Transparent algorithmic scoring rubric + auto-generated SVG 'Verified Top 10%' embed badges",
            "Self-serve $299–$799/mo Featured Placement & exclusive lead-routing checkout",
        ],
        "workflow": [
            "Score all licensed operators in a high-ticket vertical using objective public records (years licensed, zero disciplinary actions, review velocity)",
            "Notify top-scoring firms with their free embeddable HTML/SVG '2026 Top-Scored Provider' badge (driving natural dofollow backlinks back to your directory)",
            "Convert 5–10% of shortlisted firms into $299–$799/mo Featured Top-Spot subscribers who receive priority inbound quote requests",
        ],
        "metrics": [
            "Badge embed rate (% of notified firms linking back to directory)",
            "Domain Rating (DR) growth and organic city-ranking velocity",
            "Monthly recurring revenue (MRR) from Featured Profile subscriptions",
        ],
        "platform_risks": [
            {
                "failure_mode": "FTC endorsement/ranking disclosure scrutiny or Google widget-link spam filtering",
                "trigger": "Manipulating objective scores solely for pay-to-play without 'Sponsored' labels or stuffing keyword-anchor links inside badge HTML",
                "impact": "Loss of editorial credibility or discounting of badge backlinks",
                "detection_metric": "Anchor-text naturalness ratio and clear visual separation of 'Sponsored Featured Partner' vs. algorithmic score",
                "fallback": "Keep the underlying algorithmic score 100% objective and immutable, clearly label paid top-spot placements as 'Sponsored / Featured', and use clean branded anchor text in badge embeds",
            },
        ],
    },
    "b2b_class_action_contingency_recovery": {
        "id": "b2b_class_action_contingency_recovery",
        "track_id": "track_1",
        "name": "B2B Class-Action & Antitrust Settlement Contingency Recovery",
        "mechanism": (
            "Monitor multibillion-dollar corporate antitrust and commercial class-action settlement funds "
            "(payment-card interchange, freight, auto parts, commercial insurance, SaaS) where 85–90% of "
            "eligible small businesses never file, and recover verified payouts on a 25–33% contingency fee."
        ),
        "inputs": [
            "Active federal B2B class-action settlement docket calendar & claims-administrator portals",
            "B2B merchant-processing, fleet, & vendor spend intake pipeline",
            "Contingency claim-preparation & court-authorized third-party filing agreements",
        ],
        "workflow": [
            "Track open and upcoming commercial class-action settlements with verified court-appointed claims administrators and $50M–$5B+ settlement pools",
            "Sign zero-upfront-cost (25–33% contingency) authorization agreements with operating restaurants, medical practices, retailers, and fleets",
            "Extract historical merchant statements or vendor invoices, submit audited claim packages to the settlement administrator, and reconcile fee splits upon disbursement",
        ],
        "metrics": [
            "Average gross settlement recovery per enrolled business ($5,000–$150,000+)",
            "Claim acceptance rate by court-appointed administrator (%)",
            "Net contingency fee per operator hour invested",
        ],
        "platform_risks": [
            {
                "failure_mode": "Claim rejection, administrator audit hold, or court cap on third-party filer fees",
                "trigger": "Submitting unsubstantiated spend estimates, missing court bar dates, or failing to include required third-party filer disclosures",
                "impact": "Delayed payout disbursement or court-mandated fee reduction",
                "detection_metric": "Deficiency-notice rate (<2% target) and 100% court-approved disclosure compliance",
                "fallback": "File strictly for verified operating businesses with primary processor/vendor statements and use court-approved third-party claim-filing riders",
            },
        ],
    },
    "arizona_abs_mass_tort_cocounsel": {
        "id": "arizona_abs_mass_tort_cocounsel",
        "track_id": "track_1",
        "name": "Arizona ABS Law-Firm Ownership & Survivor/Mass-Tort Co-Counsel Arbitrage",
        "mechanism": (
            "Leverage Arizona Supreme Court Rule 31.1(c) and ACJA § 7-209 (which abolished ABA Rule 5.4 "
            "in Arizona via Alternative Business Structure [ABS] licensing) so non-lawyer acquisition "
            "operators can legally own an Arizona law firm, acquire inbound institutional sexual assault "
            "survivor claims (juvenile detention facilities, rideshare MDLs, clergy/boarding-school/medical "
            "lookback windows) and catastrophic mass torts, and participate in lawful co-counsel contingency "
            "fee splits ($50k–$400k+ per settled case) instead of capped flat marketing fees."
        ),
        "inputs": [
            "Arizona Supreme Court ABS license + designated Compliance Lawyer (ACJA § 7-209)",
            "Trauma-informed inbound acquisition funnels for state sexual-assault lookback windows & federal MDLs",
            "24/7 HIPAA-compliant survivor intake, facility/ride-receipt verification, & national trial co-counsel network",
        ],
        "workflow": [
            "Form or partner with a licensed Arizona ABS law firm with an appointed Arizona-bar Compliance Lawyer to legally bridge digital acquisition and legal representation",
            "Run empathetic, 100% inbound survivor-advocacy campaigns across open statutory lookback windows (juvenile detention centers, Uber/Lyft rideshare MDL 3084, institutional/youth-facility abuse)",
            "Execute trauma-informed intake, verify facility/detention/rideshare records, and co-counsel with specialized trial litigators under Rule 1.5(e) joint-responsibility agreements to share in back-end settlement fees",
        ],
        "metrics": [
            "Cost per signed & record-verified survivor retainer ($1,200–$3,500 media cost)",
            "Facility/rideshare corroboration pass rate (%) & zero-fraud docket quality",
            "Realized co-counsel contingency fee per settled case ($50,000–$400,000+ vs. $3k lead sale)",
        ],
        "platform_risks": [
            {
                "failure_mode": "Cross-jurisdictional Rule 5.4 fee-splitting challenges, MDL claimant-fraud rejections, or 24–48 month settlement lockup",
                "trigger": "Splitting fees in non-ABS jurisdictions without genuine legal services/joint responsibility by ABS attorneys, accepting unverified lead-brokered retainers, or undercapitalizing multi-year MDL hold times",
                "impact": "Disallowance of co-counsel fee division in restrictive states, court dismissal of uncorroborated claims, or working-capital exhaustion before settlement payout",
                "detection_metric": "100% primary-record corroboration rate (detention/medical/ride logs) and state-by-state Rule 1.5(e)/5.4 ethics opinion sign-off",
                "fallback": "Ensure licensed ABS attorneys perform substantive legal intake/case-work or pair with an MSO (Management Services Organization) structure in restrictive states, enforce strict primary-document verification before filing, and blend fast-settling single-event injury cases with multi-year institutional dockets",
            },
        ],
    },
}

CANDIDATE_PLAY_MAP: dict[int, tuple[str, ...]] = {
    1: ("public_record_api_intelligence",),
    2: ("public_record_api_intelligence", "distressed_asset_recovery"),
    4: ("public_record_api_intelligence", "ego_bait_directory_badge_arbitrage"),
    5: ("public_record_api_intelligence", "distressed_asset_recovery", "b2b_class_action_contingency_recovery"),
    8: (
        "public_record_api_intelligence",
        "distressed_asset_recovery",
        "b2b_class_action_contingency_recovery",
        "arizona_abs_mass_tort_cocounsel",
    ),
    9: (
        "public_record_api_intelligence",
        "public_filing_trigger_mail_arbitrage",
        "rank_and_rent_pay_per_call_routing",
        "identity_graph_pixel_arbitrage",
    ),
    11: ("telegram_channel_signal_scraping", "ego_bait_directory_badge_arbitrage"),
    12: ("public_filing_trigger_mail_arbitrage", "ego_bait_directory_badge_arbitrage"),
    13: ("distressed_asset_recovery",),
    15: ("rank_and_rent_pay_per_call_routing",),
    16: ("expired_domain_traffic_arbitrage", "newly_registered_domain_trigger_arbitrage"),
    17: ("distressed_asset_recovery",),
    18: (
        "public_record_api_intelligence",
        "public_filing_trigger_mail_arbitrage",
        "newly_registered_domain_trigger_arbitrage",
        "telegram_channel_signal_scraping",
        "programmatic_seo",
        "ego_bait_directory_badge_arbitrage",
        "arizona_abs_mass_tort_cocounsel",
        "rank_and_rent_pay_per_call_routing",
        "social_to_search_ping_post_arbitrage",
        "high_velocity_dm_outbound_systems",
        "identity_graph_pixel_arbitrage",
        "paid_to_organic_media_arbitrage",
    ),
    20: (
        "public_filing_trigger_mail_arbitrage",
        "b2b_class_action_contingency_recovery",
        "arizona_abs_mass_tort_cocounsel",
        "identity_graph_pixel_arbitrage",
    ),
    21: (
        "public_filing_trigger_mail_arbitrage",
        "arizona_abs_mass_tort_cocounsel",
        "telegram_channel_signal_scraping",
        "rank_and_rent_pay_per_call_routing",
        "social_to_search_ping_post_arbitrage",
        "high_velocity_dm_outbound_systems",
        "identity_graph_pixel_arbitrage",
    ),
    22: (
        "public_record_api_intelligence",
        "competitor_intent_comparison_hijacking",
        "chrome_extension_contextual_arbitrage",
        "viral_distribution_loops",
        "identity_graph_pixel_arbitrage",
    ),
    24: (
        "parasitic_seo",
        "competitor_intent_comparison_hijacking",
        "high_velocity_affiliate_funnels",
        "social_to_search_ping_post_arbitrage",
        "chrome_extension_contextual_arbitrage",
        "high_velocity_dm_outbound_systems",
        "serp_signal_navboost_engineering",
        "identity_graph_pixel_arbitrage",
        "paid_to_organic_media_arbitrage",
    ),
    25: (
        "expired_domain_traffic_arbitrage",
        "newly_registered_domain_trigger_arbitrage",
        "programmatic_seo",
        "ego_bait_directory_badge_arbitrage",
        "parasitic_seo",
        "competitor_intent_comparison_hijacking",
        "rank_and_rent_pay_per_call_routing",
        "serp_signal_navboost_engineering",
        "identity_graph_pixel_arbitrage",
        "paid_to_organic_media_arbitrage",
    ),
    26: (
        "arizona_abs_mass_tort_cocounsel",
        "telegram_channel_signal_scraping",
        "ego_bait_directory_badge_arbitrage",
        "high_velocity_dm_outbound_systems",
        "identity_graph_pixel_arbitrage",
    ),
    27: (
        "public_filing_trigger_mail_arbitrage",
        "chrome_extension_contextual_arbitrage",
        "viral_distribution_loops",
        "high_velocity_dm_outbound_systems",
        "identity_graph_pixel_arbitrage",
    ),
    28: (
        "chrome_extension_contextual_arbitrage",
        "viral_distribution_loops",
        "identity_graph_pixel_arbitrage",
    ),
    29: (
        "newly_registered_domain_trigger_arbitrage",
        "telegram_channel_signal_scraping",
        "competitor_intent_comparison_hijacking",
        "high_velocity_dm_outbound_systems",
        "identity_graph_pixel_arbitrage",
    ),
}


def get_candidate_track_metadata(candidate_number: object) -> dict:
    """Return detached ``track_ids``, ``track_labels``, ``plays``, and ``platform_risks`` for ``candidate_number``."""
    num: int | None = None
    if not isinstance(candidate_number, bool) and isinstance(candidate_number, int):
        num = candidate_number
    play_ids = CANDIDATE_PLAY_MAP.get(num, ()) if num is not None else ()
    plays = [deepcopy(PLAY_DEFINITIONS[pid]) for pid in play_ids if pid in PLAY_DEFINITIONS]
    track_ids: list[str] = []
    for play in plays:
        tid = play.get("track_id")
        if isinstance(tid, str) and tid in TRACK_DEFINITIONS and tid not in track_ids:
            track_ids.append(tid)
    track_labels = [TRACK_DEFINITIONS[tid]["name"] for tid in track_ids]
    platform_risks = [
        deepcopy({**risk, "play_id": play["id"], "play_name": play["name"], "track_id": play["track_id"]})
        for play in plays
        for risk in play.get("platform_risks", [])
        if isinstance(risk, dict)
    ]
    return {
        "track_ids": track_ids,
        "track_labels": track_labels,
        "plays": plays,
        "platform_risks": platform_risks,
    }


def compute_scorecard(spec: dict) -> dict:
    """Validate weighted subscores and return a detached, normalized scorecard."""
    if not isinstance(spec, dict):
        raise ValueError("spec must be a dictionary")
    scores = spec.get("scores")
    if not isinstance(scores, dict) or set(scores) != set(SCORE_DIMENSIONS):
        raise ValueError("scores must contain exactly the five score dimensions")
    for key, maximum in SCORE_DIMENSIONS.items():
        value = scores[key]
        if (isinstance(value, bool) or not isinstance(value, (int, float))
                or not 0 <= value <= maximum or not isfinite(value)):
            raise ValueError(f"{key} must be a finite number between 0 and {maximum}")
    confidence = spec.get("evidence_confidence")
    if not isinstance(confidence, str) or confidence not in _CONFIDENCE_BANDS:
        raise ValueError("invalid evidence_confidence")
    total = sum(scores.values())
    uncertainty_band = _CONFIDENCE_BANDS[confidence]
    band_delta = int(uncertainty_band.removeprefix("±").split()[0])
    if total >= 85:
        tier = "Elite Small-Team Cash Machine"
    elif total >= 75:
        tier = "High-Leverage Operator Play"
    elif total >= 65:
        tier = "Disciplined Specialist Play"
    else:
        tier = "Capital / Labor Intensive"
    track_meta = get_candidate_track_metadata(spec.get("candidate_number"))
    raw_track_ids = spec.get("track_ids")
    raw_plays = spec.get("plays")
    raw_platform_risks = spec.get("platform_risks")
    track_ids = (
        [str(t) for t in raw_track_ids if isinstance(t, str) and t in TRACK_DEFINITIONS]
        if isinstance(raw_track_ids, list)
        else track_meta["track_ids"]
    )
    track_labels = [TRACK_DEFINITIONS[tid]["name"] for tid in track_ids if tid in TRACK_DEFINITIONS]
    plays = (
        [deepcopy(p) for p in raw_plays if isinstance(p, dict)]
        if isinstance(raw_plays, list)
        else track_meta["plays"]
    )
    platform_risks = (
        [deepcopy(r) for r in raw_platform_risks if isinstance(r, dict)]
        if isinstance(raw_platform_risks, list)
        else track_meta["platform_risks"]
    )
    result = {
        "candidate_number": spec.get("candidate_number"),
        "slug": spec.get("slug", ""),
        "title": spec.get("title", ""),
        "category": spec.get("category", ""),
        "production_stage": spec.get("production_stage", "candidate_scored"),
        "scores": dict(scores),
        "dimension_max": dict(SCORE_DIMENSIONS),
        "total_score": total,
        "tier_label": tier,
        "evidence_confidence": confidence,
        "uncertainty_band": uncertainty_band,
        "uncertainty_bounds": {
            "low": max(0, total - band_delta),
            "high": min(100, total + band_delta),
        },
        "uncertainty_note": spec.get("uncertainty_note", (
            "Editorial sensitivity band, not a statistical interval. Confidence "
            "is a supplied classification; independent source review is required."
        )),
        "score_rationale": spec.get("score_rationale", {}),
        "economics": spec.get("economics", {}),
        "scenarios": spec.get("scenarios", {}),
        "automation_levers": spec.get("automation_levers", []),
        "key_risks": spec.get("key_risks", []),
        "regulatory_notes": spec.get("regulatory_notes", []),
        "track_ids": track_ids,
        "track_labels": track_labels,
        "plays": plays,
        "platform_risks": platform_risks,
    }
    return deepcopy(result)


def get_flagship_scorecard() -> dict:
    """Return candidate 1 irrespective of its eventual pipeline ranking."""
    return compute_scorecard(next(
        spec for spec in _CANDIDATE_SPECS if spec["candidate_number"] == 1
    ))


def _money_range(values: tuple) -> str:
    return f"${values[0]:,.0f}–${values[1]:,.0f} USD"


def _candidate(number, title, category, points, gross, margins, capital, opex,
               timing, team, rationale, levers, risks, regulations,
               revenue_basis="Recognized service fees, not client asset value",
               confidence="Moderate") -> dict:
    """Build a uniform schema from explicit, candidate-specific assumptions.

    Gross revenue is annual. Margins already include non-owner labor and all
    operating expenses; monthly opex is an indicative fixed/semi-fixed budget,
    not an additional deduction. Inventory, pass-through and financing capital
    are separate from fixed opex. Owner profit assumes sole ownership, before
    personal taxes, debt principal and reinvestment, with no owner salary charged.
    """
    scores = dict(zip(SCORE_DIMENSIONS, points))
    ft, contractors = team
    staffing = {
        "full_time_including_owner": ft,
        "contractors": contractors,
        "total_people": ft + contractors,
    }
    scenarios = {}
    for name, revenue, margin, extra in (
        ("conservative", gross[0], margins[0], 0),
        ("base_case", sum(gross) / 2, sum(margins) / 2, 0),
        ("scaled_small_team", gross[1], margins[1], 2),
    ):
        scenarios[name] = {
            "annual_gross_revenue_usd": revenue,
            "net_profit_margin_pct": margin,
            "annual_owner_net_profit_usd": round(revenue * margin / 100),
            "full_time_including_owner": ft + (1 if extra else 0),
            "contractors": contractors + (1 if extra else 0),
            "total_people": ft + contractors + extra,
            "assumption": (
                "Illustrative established-operation run rate, not first-year "
                "earnings. Margin includes operating costs and non-owner labor; "
                "owner labor is not separately compensated. Scale requires "
                "additional demand, working capital and delivery capacity."
            ),
        }
    confidence = "High" if number in {1, 2, 5, 9} else confidence
    stage = ("flagship_in_design_review" if number == 1 else
             "research_corpus_ready" if number in {2, 5, 9} else "candidate_scored")
    return {
        "candidate_number": number,
        "slug": title.lower().replace(" ", "-"),
        "title": title,
        "category": category,
        "production_stage": stage,
        "scores": scores,
        "evidence_confidence": confidence,
        "score_rationale": {
            key: f"{DIMENSION_LABELS[key]}: {score}/{SCORE_DIMENSIONS[key]}. {rationale}"
            for key, score in scores.items()
        },
        "economics": {
            "gross_revenue_range": _money_range(gross) + " annually",
            "net_profit_margin_range": f"{margins[0]}–{margins[1]}%",
            "owner_net_profit_potential": _money_range((
                gross[0] * margins[0] / 100, gross[1] * margins[1] / 100,
            )) + " annually, before personal taxes and reinvestment",
            "startup_capital_range": _money_range(capital),
            "monthly_opex_range": _money_range(opex),
            "time_to_first_deal": timing,
            "typical_team_size": staffing,
            "includes_contractors_note": (
                "Headcount includes the working owner and recurring contractors "
                "as people, not FTE equivalents. Contractors may be part-time. "
                "Scaled scenario adds one employee and one contractor; external "
                "vendor workforces are not counted as internal team members."
            ),
            "revenue_basis": revenue_basis,
            "cost_basis": (
                "Annual net margins include operating expenses and non-owner "
                "labor; monthly opex is fixed/semi-fixed overhead only. No owner "
                "salary is deducted. Capital needs may grow beyond startup range."
            ),
            "estimate_status": "Illustrative assumptions; not verified earnings data",
        },
        "scenarios": scenarios,
        "automation_levers": levers,
        "key_risks": risks,
        "regulatory_notes": regulations,
    }


_CANDIDATE_SPECS = [
    _candidate(1, "Heir Hunting", "Estate research", (22, 23, 18, 12, 12),
        (80000, 600000), (25, 50), (10000, 50000), (2000, 10000), "6–24 months", (1, 3),
        "Contingent fees support lean research teams, but estate delays defer cash.",
        ["Public-record alerts", "Genealogy case tracking", "Document indexing"],
        ["Unsuccessful research", "Contested kinship", "Long collection cycles"],
        ["Check heir-finder fee restrictions and solicitation rules by jurisdiction.",
         "Do not provide legal representation without appropriate authorization."]),
    _candidate(2, "Surplus Funds Recovery", "Recovery services", (22, 22, 18, 12, 12),
        (100000, 750000), (25, 45), (10000, 60000), (2500, 14000), "3–18 months", (2, 2),
        "Fee-based recovery has low inventory needs but uneven claim conversion.",
        ["Auction-result monitoring", "Claim deadlines", "Document checklists"],
        ["Competing claims", "Denied claims", "Fee compression"],
        ["Surplus recovery fee caps, assignment validity and waiting periods vary.",
         "Court filings may require licensed counsel."]),
    _candidate(3, "Tax Lien Investing", "Asset investing", (17, 15, 17, 5, 8),
        (15000, 180000), (30, 55), (100000, 1500000), (500, 4000), "6–36 months", (1, 2),
        "Lean administration cannot offset capital lockup and adverse property selection.",
        ["Auction screening", "Redemption tracking"],
        ["Nonredeeming liens", "Title defects", "Capital loss"],
        ["Auction eligibility, interest limits and foreclosure procedures are local."],
        revenue_basis="Realized interest, penalties and disposition gains; excludes returned principal"),
    _candidate(4, "Government Contract Brokering", "Procurement services", (22, 16, 14, 8, 10),
        (120000, 1000000), (15, 30), (25000, 150000), (5000, 25000), "6–18 months", (2, 3),
        "Large awards do not translate to large fees; compliance and sales require labor.",
        ["Solicitation alerts", "Bid calendars", "Compliance checklists"],
        ["Award uncertainty", "Payment delays", "Supplier failure"],
        ["Review contingent-fee restrictions, procurement integrity and anti-kickback rules.",
         "Pass-through restrictions and set-aside rules can prohibit proposed structures."]),
    _candidate(5, "Unclaimed Property Recovery", "Recovery services", (20, 22, 18, 13, 12),
        (60000, 450000), (25, 50), (5000, 35000), (1500, 8000), "3–12 months", (1, 2),
        "Low-capital research scales moderately; free state claims constrain pricing.",
        ["Record matching", "Claim status tracking"],
        ["Identity mismatch", "Low claim values", "Customer distrust"],
        ["Check finder registration, fee caps, waiting periods and privacy obligations.",
         "Disclose the owner's ability to claim directly without a recovery service."]),
    _candidate(6, "Land Flipping", "Real estate trading", (21, 18, 17, 6, 10),
        (200000, 1500000), (12, 25), (50000, 400000), (3000, 15000), "3–12 months", (1, 3),
        "Small teams can trade parcels, but inventory capital and due diligence limit access.",
        ["Parcel screening", "Comparable-sale tracking"],
        ["Illiquidity", "No legal access", "Environmental constraints"],
        ["Review zoning, title, disclosures and broker licensing when representing others."],
        revenue_basis="Gross parcel sale proceeds; acquisition costs included in net margin"),
    _candidate(7, "Mineral Rights", "Resource assets", (20, 17, 16, 3, 7),
        (30000, 400000), (20, 45), (150000, 2000000), (1000, 12000), "6–24 months", (1, 3),
        "Specialist title work and substantial capital outweigh passive-income appeal.",
        ["Royalty reconciliation", "Production monitoring"],
        ["Commodity prices", "Depletion", "Title disputes"],
        ["Review severed mineral title, leases, tax obligations and securities rules if pooling funds."],
        revenue_basis="Royalty receipts and realized rights-trading gains, excluding returned basis"),
    _candidate(8, "Judgment Recovery", "Recovery services", (20, 21, 16, 10, 10),
        (60000, 500000), (20, 40), (10000, 75000), (2000, 12000), "6–24 months", (1, 3),
        "Contingent collections can be efficient but many judgments are uncollectible.",
        ["Court deadline tracking", "Payment reconciliation"],
        ["Insolvent debtors", "Bankruptcy stays", "Enforcement costs"],
        ["Check collection licensing, consumer-debt rules, exemptions and lawful data access."]),
    _candidate(9, "Probate Real Estate", "Real estate services", (23, 18, 16, 9, 10),
        (120000, 900000), (20, 35), (15000, 100000), (3000, 18000), "4–18 months", (2, 3),
        "Modeled as licensed brokerage rather than capital-heavy property acquisition.",
        ["Docket alerts", "Transaction checklists"],
        ["Court delays", "Family disputes", "Housing-market cycles"],
        ["Real estate licensing, fiduciary duties and court-sale approvals may apply."],
        revenue_basis="Retained brokerage commissions after brokerage splits, not home sale values"),
    _candidate(10, "Commercial Cleaning Contracts", "Facility services", (21, 12, 6, 11, 6),
        (250000, 1200000), (8, 16), (15000, 90000), (4000, 18000), "1–4 months", (5, 4),
        "Recurring contracts are attractive, but delivery headcount grows with revenue.",
        ["Scheduling", "Inspection logs", "Billing"],
        ["Labor turnover", "Underpriced contracts", "Customer concentration"],
        ["Observe wage laws, worker classification, chemical safety and insurance requirements."],
        revenue_basis="Cleaning contract revenue; scalable only with more paid crew hours"),
    _candidate(11, "Equipment Brokerage", "Industrial brokerage", (22, 20, 18, 11, 10),
        (100000, 800000), (25, 45), (10000, 75000), (2500, 14000), "2–9 months", (1, 3),
        "Fee-only brokerage avoids inventory, while inspections and deal sourcing remain manual.",
        ["Inventory matching", "Buyer alerts"],
        ["Equipment defects", "Fraud", "Lumpy commissions"],
        ["Check dealer licensing, lien releases, warranties and export controls."],
        revenue_basis="Broker commissions only; excludes equipment transaction value"),
    _candidate(12, "Freight Brokerage", "Logistics", (23, 10, 10, 7, 12),
        (1000000, 5000000), (3, 8), (50000, 250000), (6000, 30000), "2–6 months", (3, 2),
        "Large billings conceal carrier costs, thin net margins and intensive exception handling.",
        ["Load matching", "Shipment tracking", "Invoice reconciliation"],
        ["Carrier fraud", "Claims", "Shipper nonpayment"],
        ["US property brokers generally need FMCSA authority and $75,000 bond or trust security.",
         "Verify current financial-responsibility and carrier-vetting requirements."],
        revenue_basis="Gross shipper billings including carrier costs; accounting presentation can differ"),
    _candidate(13, "Business Acquisition", "Operating business ownership", (24, 16, 7, 2, 8),
        (750000, 3000000), (8, 18), (200000, 1000000), (15000, 70000), "6–18 months", (7, 3),
        "Existing cash flow requires purchase capital, retained staff and debt-service discipline.",
        ["Financial reporting", "Back-office workflows"],
        ["Hidden liabilities", "Customer attrition", "Leverage"],
        ["Review employment, tax, licenses, lender covenants and transaction disclosures."],
        revenue_basis="Acquired business sales; margin after interest, before principal repayments"),
    _candidate(14, "Medical Equipment Resale", "Equipment trading", (21, 16, 13, 6, 8),
        (250000, 1800000), (10, 22), (75000, 400000), (5000, 22000), "3–9 months", (2, 4),
        "Specialist refurbishment, inventory and traceability reduce lean-team economics.",
        ["Inventory tracking", "Service-history indexing"],
        ["Device liability", "Obsolescence", "Unsellable inventory"],
        ["Check device-specific FDA obligations, servicing versus remanufacturing and state licensing.",
         "Sanitize stored patient data and verify decontamination procedures."],
        revenue_basis="Gross equipment resale proceeds; acquisition and refurbishment included in margin"),
    _candidate(15, "Insurance Restoration", "Property restoration", (24, 13, 5, 5, 7),
        (500000, 2500000), (8, 18), (75000, 350000), (10000, 45000), "1–6 months", (5, 6),
        "High ticket sizes require field crews, working capital and demanding project oversight.",
        ["Dispatch", "Photo documentation", "Job-cost tracking"],
        ["Claim disputes", "Cash-flow gaps", "Safety incidents"],
        ["Check contractor and remediation licensing; public adjusting may require a separate license.",
         "Do not promise insurer coverage or waive deductibles unlawfully."],
        revenue_basis="Gross restoration billings; subcontractor and material costs included in margin"),
]
_CANDIDATE_SPECS.extend([
    _candidate(16, "Domain Investing", "Digital asset trading", (17, 18, 19, 9, 11),
        (20000, 300000), (15, 40), (10000, 150000), (500, 5000), "3–24 months", (1, 1),
        "Lean portfolios can produce high-margin sales, but low sell-through ties up capital.",
        ["Renewal tracking", "Comparable-sale monitoring", "Inbound inquiry routing"],
        ["Illiquid inventory", "Renewal costs", "Trademark disputes"],
        ["Review trademark conflicts, domain dispute policies and anti-cybersquatting laws."],
        revenue_basis="Gross domain sale proceeds; acquisition and renewal costs included in margin"),
    _candidate(17, "Government Surplus Auctions", "Surplus asset trading", (20, 14, 12, 8, 8),
        (150000, 1000000), (8, 20), (25000, 200000), (3000, 15000), "1–6 months", (2, 3),
        "Discounted lots offer resale spreads, but transport, storage and defects consume margin.",
        ["Auction alerts", "Bid-limit worksheets", "Inventory tracking"],
        ["As-is defects", "Removal deadlines", "Unsold inventory"],
        ["Check auction eligibility, resale permits, title transfer and restricted-item rules."],
        revenue_basis="Gross resale proceeds; purchase, transport and refurbishment included in margin"),
    _candidate(18, "Commercial Lead Generation", "B2B marketing services", (21, 21, 18, 12, 13),
        (100000, 750000), (20, 40), (5000, 40000), (2000, 12000), "1–4 months", (1, 3),
        "Recurring prospecting fees support lean delivery, but qualification and retention need oversight.",
        ["Consent tracking", "CRM routing", "Lead-quality reporting"],
        ["Poor lead quality", "Client churn", "Rising acquisition costs"],
        ["Observe applicable privacy, email marketing, telemarketing and opt-out requirements."],
        revenue_basis="Retainers and accepted-lead fees; excludes client-funded advertising pass-through"),
    _candidate(19, "Intellectual Property Licensing", "Licensing services", (22, 23, 18, 6, 10),
        (50000, 800000), (25, 60), (25000, 250000), (2000, 15000), "6–24 months", (1, 3),
        "Reusable rights can earn royalties, but defensible IP and licensee adoption are costly to establish.",
        ["Royalty reporting", "License renewal alerts", "Contract obligation tracking"],
        ["Unproven demand", "Infringement disputes", "Licensee underreporting"],
        ["Verify chain of title, permitted uses, territorial rights and competition-law constraints."],
        revenue_basis="License fees and royalties; excludes licensees' underlying product sales",
        confidence="Preliminary — Uncertainty Range"),
    _candidate(20, "Specialty Finance Brokerage", "Finance intermediary services", (23, 21, 17, 8, 10),
        (120000, 1000000), (25, 45), (20000, 100000), (4000, 18000), "3–9 months", (2, 2),
        "Fee-only placement avoids lending capital, but underwriting coordination and licensing constrain scale.",
        ["Application checklists", "Lender matching", "Renewal tracking"],
        ["Failed closings", "Lender concentration", "Commission clawbacks"],
        ["Check loan-broker licensing, fee disclosures, fair-lending and data-security duties.",
         "Securities placements may require separate broker-dealer registration."],
        revenue_basis="Retained origination or referral fees only; excludes loan principal"),
    _candidate(21, "Million-Dollar Lead Generation", "Enterprise demand generation", (24, 21, 16, 9, 12),
        (150000, 1200000), (20, 40), (15000, 100000), (4000, 20000), "3–12 months", (2, 3),
        "Targets buyers of million-dollar contracts, not guaranteed million-dollar lead fees or earnings.",
        ["Account qualification", "CRM attribution", "Meeting scheduling"],
        ["Long sales cycles", "Attribution disputes", "Customer concentration"],
        ["Check privacy, outreach consent and sector-specific referral or contingent-fee restrictions."],
        revenue_basis="Retainers and qualified-opportunity fees; excludes client contract values",
        confidence="Preliminary — Uncertainty Range"),
    _candidate(22, "AI-Powered Micro SaaS", "Subscription software", (22, 22, 19, 11, 14),
        (50000, 700000), (15, 45), (10000, 100000), (2000, 15000), "2–9 months", (1, 2),
        "Narrow software products support lean recurring revenue, but inference costs and churn limit margins.",
        ["Subscription billing", "Usage metering", "Onboarding workflows"],
        ["Weak product-market fit", "Model-provider dependency", "Security incidents"],
        ["Review data privacy, model and content licenses, subscription terms and sector obligations.",
         "Validate consequential outputs and avoid unsupported accuracy claims."],
        revenue_basis="Subscription and usage fees; hosting, model usage and support included in margin",
        confidence="Preliminary — Uncertainty Range"),
    _candidate(23, "Enterprise Software Reselling", "Software channel sales", (23, 14, 15, 9, 11),
        (300000, 2500000), (8, 20), (25000, 150000), (5000, 25000), "3–12 months", (2, 3),
        "Large license billings mask vendor costs; renewals help but enterprise sales need specialist labor.",
        ["Renewal alerts", "Quote generation", "License reconciliation"],
        ["Vendor policy changes", "Slow collections", "Channel competition"],
        ["Verify reseller authorization, license terms, procurement requirements and data-processing duties."],
        revenue_basis="Gross license resale and service billings; vendor costs included in margin"),
    _candidate(24, "High-Ticket Affiliate Marketing", "Referral publishing", (21, 22, 19, 12, 13),
        (50000, 600000), (20, 50), (5000, 50000), (1500, 12000), "3–12 months", (1, 2),
        "Commission income avoids fulfillment, but traffic costs and merchant dependence create volatility.",
        ["Link validation", "Conversion reporting", "Content scheduling"],
        ["Commission cuts", "Refund clawbacks", "Traffic loss"],
        ["Clearly disclose affiliate relationships and substantiate advertising and earnings claims.",
         "Check sector-specific restrictions on paid referrals."],
        revenue_basis="Earned affiliate commissions net of reversals; excludes referred purchase values"),
    _candidate(25, "Building an SEO Empire", "Search-driven publishing", (22, 21, 17, 10, 12),
        (80000, 900000), (20, 45), (15000, 120000), (3000, 20000), "6–24 months", (2, 4),
        "A site portfolio can monetize recurring traffic, but editorial quality and search volatility require investment.",
        ["Technical site audits", "Content refresh queues", "Revenue reporting"],
        ["Ranking losses", "Slow audience growth", "Revenue concentration"],
        ["Respect copyright, advertising disclosures, privacy requirements and search platform policies."],
        revenue_basis="Advertising, affiliate and sponsorship revenue; excludes referred merchant sales"),
    _candidate(26, "High-Ticket Brokerage", "Specialist transaction services", (23, 22, 18, 10, 9),
        (100000, 1000000), (25, 50), (15000, 100000), (3000, 18000), "3–12 months", (1, 3),
        "Large specialist transactions can yield substantial commissions, but closing frequency is uneven.",
        ["Buyer-seller matching", "Deal milestone tracking", "Document checklists"],
        ["Failed closings", "Misrepresentation claims", "Lumpy cash flow"],
        ["Confirm asset-specific brokerage licenses, agency disclosures and client-fund handling rules."],
        revenue_basis="Retained transaction commissions only; excludes underlying asset values"),
    _candidate(27, "Digital Product Empire", "Digital education and tools", (22, 23, 19, 12, 14),
        (50000, 800000), (20, 55), (5000, 60000), (1500, 15000), "1–6 months", (1, 3),
        "Reusable products have low delivery costs, but audience building, refunds and updates absorb profit.",
        ["Digital fulfillment", "Customer onboarding", "Sales-tax reporting"],
        ["Weak demand", "Piracy", "Paid acquisition losses"],
        ["Verify content rights, consumer refund rules, digital sales taxes and truthful marketing."],
        revenue_basis="Digital product sales net of refunds; acquisition, platform and support costs included in margin"),
    _candidate(28, "Automated E-Commerce", "Online retail", (23, 13, 14, 8, 12),
        (250000, 2000000), (5, 18), (30000, 250000), (4000, 25000), "2–6 months", (2, 3),
        "Automation reduces routine order work, not inventory exposure, returns or supplier oversight.",
        ["Order routing", "Inventory alerts", "Returns tracking"],
        ["Ad-cost inflation", "Stockouts", "Product liability"],
        ["Check product safety, import duties, sales taxes, privacy and consumer protection requirements."],
        revenue_basis="Retail sales net of refunds; goods, fulfillment and advertising included in margin"),
    _candidate(29, "Productized AI Agencies", "Technology implementation services", (23, 21, 17, 12, 13),
        (100000, 1000000), (20, 40), (5000, 60000), (2500, 18000), "1–4 months", (2, 3),
        "Standardized implementations improve repeatability, but integration exceptions and human review remain costly.",
        ["Client intake workflows", "Deployment checklists", "Usage and quality monitoring"],
        ["Scope creep", "Unreliable outputs", "Client data exposure"],
        ["Obtain authorization for client-system access and define data-processing and IP terms.",
         "Maintain human review for consequential decisions and substantiate performance claims."],
        revenue_basis="Implementation fees and support retainers; excludes client revenue attributed to automation",
        confidence="Preliminary — Uncertainty Range"),
])


def build_29_candidate_pipeline() -> list[dict]:
    """Return all 29 normalized scorecards ranked by score, then candidate number."""
    from . import (
        MIN_EXPERT_YOUTUBE_LINKS_PER_BOOK,
        TARGET_EXPERT_YOUTUBE_LINKS_PER_BOOK,
        MIN_EXPERT_YOUTUBE_LINKS_PER_CHAPTER,
    )
    pipeline = [compute_scorecard(spec) for spec in _CANDIDATE_SPECS]
    pipeline.sort(key=lambda card: (-card["total_score"], card["candidate_number"]))
    for rank, card in enumerate(pipeline, start=1):
        card["rank"] = rank
        card["min_expert_youtube_links"] = MIN_EXPERT_YOUTUBE_LINKS_PER_BOOK
        card["target_expert_youtube_links"] = TARGET_EXPERT_YOUTUBE_LINKS_PER_BOOK
        card["min_expert_youtube_links_per_chapter"] = MIN_EXPERT_YOUTUBE_LINKS_PER_CHAPTER
    return pipeline
