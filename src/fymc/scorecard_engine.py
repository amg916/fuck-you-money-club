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
    "unclaimed_property_escheatment_arbitrage": {
        "id": "unclaimed_property_escheatment_arbitrage",
        "track_id": "track_1",
        "name": "State Treasury Escheatment & Unclaimed Corporate Warrant Recovery",
        "mechanism": (
            "Ingest state controller/treasury escheatment ledgers and uncashed municipal/corporate warrant "
            "registries above $25,000, cross-match corporate officers via Secretary of State filings, and "
            "execute statutory recovery agreements for a 10–25% contingent finder fee."
        ),
        "inputs": [
            "State controller/treasury escheatment bulk ledgers",
            "Uncashed municipal warrant & vendor-credit registries",
            "Secretary of State officer & FEIN cross-match index",
        ],
        "workflow": [
            "Filter state unclaimed-property and uncashed-warrant ledgers for high-value corporate and estate accounts exceeding $25,000",
            "Resolve active corporate officers, successor entities, or authorized fiduciaries via SOS and skip-trace databases",
            "Execute state-compliant finder agreements with statutory fee caps and submit notarized claim packages to the treasury administrator",
        ],
        "metrics": [
            "Average gross warrant/escheatment claim size ($25k+)",
            "Treasury claim approval rate (%)",
            "Days from notarized filing to state disbursement",
        ],
        "platform_risks": [
            {
                "failure_mode": "Statutory finder-fee cap violation or waiting-period rejection",
                "trigger": "Charging above state statutory fee limits (e.g., 10% in CA/FL/NY) or soliciting claims during restricted post-escheatment windows",
                "impact": "Voided recovery contract, state controller rejection, or administrative penalty",
                "detection_metric": "State-by-state fee-cap compliance check (100% pass) and claim rejection notice rate",
                "fallback": "Enforce per-state statutory fee caps and waiting-period rules in intake templates and disclose the owner's right to claim directly for free",
            },
        ],
    },
    "municipal_code_violation_trigger_arbitrage": {
        "id": "municipal_code_violation_trigger_arbitrage",
        "track_id": "track_1",
        "name": "Municipal Code-Violation, Mechanic's Lien & Permit-Failure Lead Arbitrage",
        "mechanism": (
            "Poll municipal building department portals and county recorder dockets daily for failed "
            "structural/fire inspections, expired permits, code citations, and newly filed mechanic's liens, "
            "routing exclusive real-time leads to remediation contractors and construction attorneys."
        ),
        "inputs": [
            "Municipal Accela/EnerGov building & code-enforcement portals",
            "County recorder mechanic's lien & lis pendens dockets",
            "Real-time Pay-Per-Call & exclusive CPL routing switch",
        ],
        "workflow": [
            "Scrape and normalize daily municipal code citations, failed permit inspections, and recorded mechanic's liens across target metro counties",
            "Enrich parcel owner contact records and classify urgency by abatement deadline or fine accrual rate",
            "Route verified property owners via direct mail/outbound alerts into exclusive Pay-Per-Call or CPL agreements with licensed remediation contractors",
        ],
        "metrics": [
            "Citation-to-outreach latency (hours)",
            "Qualified homeowner/commercial call conversion %",
            "Revenue per exclusive routed remediation lead",
        ],
        "platform_risks": [
            {
                "failure_mode": "Municipal portal IP blocking or deceptive official-notice complaints",
                "trigger": "Aggressive unthrottled scraping of Accela/EnerGov portals or styling outreach like an official city abatement order",
                "impact": "Portal IP block or city attorney cease-and-desist notice",
                "detection_metric": "Portal HTTP 403/429 rate and zero municipal impersonation complaints",
                "fallback": "Use low-frequency scheduled API/bulk exports and clearly identify all outreach as private commercial contractor/remediation assistance",
            },
        ],
    },
    "freight_detention_audit_contingency": {
        "id": "freight_detention_audit_contingency",
        "track_id": "track_1",
        "name": "Automated Parcel, LTL Freight & Tariff Overcharge Contingency Auditing",
        "mechanism": (
            "Ingest mid-market shippers' UPS/FedEx/LTL EDI billing feeds and CBP Form 7501 customs entry "
            "summaries via read-only API to programmatically flag late-delivery SLA refunds, dimensional-weight "
            "billing errors, and duty-drawback refunds on a 35–50% contingency split."
        ),
        "inputs": [
            "Read-only UPS/FedEx/LTL carrier billing API & EDI 210 feeds",
            "CBP ACE Form 7501 customs entry & HTS tariff schedules",
            "Automated carrier dispute & duty-drawback claim submission engine",
        ],
        "workflow": [
            "Connect read-only to shipper parcel/freight portals and ingest historical and daily invoice line items",
            "Flag guaranteed-service late deliveries, duplicate accessorial fees, residential surcharges, and eligible export duty drawbacks",
            "Auto-file carrier credit disputes and customs drawback claims, billing the client strictly 35–50% of verified credits posted to their statement",
        ],
        "metrics": [
            "Recovered credits as % of total annual parcel/freight spend (2–8% target)",
            "Dispute acceptance rate by carrier/customs (%)",
            "Monthly recurring contingency revenue per shipper account",
        ],
        "platform_risks": [
            {
                "failure_mode": "Carrier anti-automation lockouts or GSR (Guaranteed Service Refund) waiver clauses",
                "trigger": "Carriers inserting GSR waiver riders into custom shipper pricing agreements or throttling automated dispute bots",
                "impact": "Reduction in late-delivery refund volume on waived accounts",
                "detection_metric": "Claim approval ratio per carrier and % of audit recovery derived from billing/dim-weight errors vs. GSR",
                "fallback": "Pivot audit rules toward non-waivable dimensional-weight, duplicate-charge, LTL freight class, and contract-rate benchmarking recoveries",
            },
        ],
    },
    "ucc1_expiration_refi_trigger_arbitrage": {
        "id": "ucc1_expiration_refi_trigger_arbitrage",
        "track_id": "track_1",
        "name": "UCC-1 Filing, MCA Stacking & Maturity-Date Trigger Arbitrage",
        "mechanism": (
            "Monitor state Secretary of State UCC-1 financing statements and continuation filings to "
            "identify operating businesses 4–9 months into high-cost Merchant Cash Advances (MCAs) or "
            "equipment notes, triggering refinance and debt-consolidation live transfers."
        ),
        "inputs": [
            "Daily state SOS UCC-1 initial, amendment, & termination bulk feeds",
            "Secured-party lender dictionary (identifying MCA vs. bank/SBA filings)",
            "Live-transfer commercial refinance & SBA consolidation desk",
        ],
        "workflow": [
            "Classify daily UCC-1 filings by secured party to isolate businesses that took high-cost short-term working capital 120–240 days ago",
            "Enrich business owner direct phone and email and score by industry revenue stability",
            "Contact merchants during peak renewal/payoff windows to offer lower-rate term consolidation or equipment refinancing, monetizing via broker points or live-transfer fees",
        ],
        "metrics": [
            "UCC-to-verified-decision-maker match rate (%)",
            "Live-transfer qualification rate (%)",
            "Origination commission / referral fee per funded refi",
        ],
        "platform_risks": [
            {
                "failure_mode": "TCPA automated-calling liability or state commercial-financing disclosure violations",
                "trigger": "Robocalling cell phones without consent or quoting misleading APRs in states with commercial Truth-in-Lending laws (CA, NY, UT, VA)",
                "impact": "Statutory TCPA demand letters or state DFPI regulatory enforcement",
                "detection_metric": "100% DNC/litigator-scrub pass rate and statutory APR disclosure audit in regulated states",
                "fallback": "Use direct mail, B2B work-email sequences, and manual human-dialed outreach paired with compliant state commercial financing disclosures",
            },
        ],
    },
    "probate_docket_inheritance_arbitrage": {
        "id": "probate_docket_inheritance_arbitrage",
        "track_id": "track_1",
        "name": "Probate Docket & Pre-Foreclosure Notice-of-Default (NOD) Scraping",
        "mechanism": (
            "Parse county probate petitions (Letters Testamentary / Letters of Administration) and daily "
            "Notice-of-Default (NOD) filings before national aggregators index them, matching out-of-state "
            "personal representatives and distressed owners to licensed probate brokers and cash buyers."
        ),
        "inputs": [
            "County probate court register of actions & Letters Testamentary filings",
            "County recorder daily Notice-of-Default (NOD) & Notice-of-Trustee-Sale feeds",
            "Skip-tracing & out-of-state personal-representative matching pipeline",
        ],
        "workflow": [
            "Extract newly appointed estate personal representatives and real-property inventory from county probate dockets within 24 hours of filing",
            "Cross-match parcel equity and mortgage balances against county assessor and recorder records",
            "Deliver empathetic estate-liquidation checklists, property-preservation referrals, or licensed brokerage introductions",
        ],
        "metrics": [
            "Docket-to-first-contact speed vs. national data aggregators (days)",
            "Personal-representative response & appointment rate (%)",
            "Commission or referral fee per closed probate/pre-foreclosure parcel",
        ],
        "platform_risks": [
            {
                "failure_mode": "State Foreclosure Consultant Act violations or unlicensed brokerage fee-splitting",
                "trigger": "Charging upfront fees to distressed homeowners in NOD or taking unlicensed real-estate commission splits",
                "impact": "Voided contracts, treble damages under state foreclosure-protection statutes, or DRE enforcement",
                "detection_metric": "100% licensed broker co-marketing compliance and zero upfront homeowner fee charges",
                "fallback": "Monetize strictly via flat-fee marketing/data subscriptions to licensed probate agents or close transactions through a licensed brokerage of record",
            },
        ],
    },
    "fmcsa_dot_inspection_trigger_arbitrage": {
        "id": "fmcsa_dot_inspection_trigger_arbitrage",
        "track_id": "track_1",
        "name": "FMCSA/DOT New-Authority & Roadside Violation Trigger Funnels",
        "mechanism": (
            "Ingest daily federal FMCSA Census, Licensing & Insurance (L&I), and SMS roadside-inspection "
            "violation feeds to intercept newly granted MC/DOT authorities (during the mandatory 21-day "
            "insurance-filing window) and fleets with fresh HOS/maintenance citations."
        ),
        "inputs": [
            "FMCSA daily Licensing & Insurance (L&I) pending-authority feed",
            "FMCSA Safety Measurement System (SMS) roadside violation & BASIC score logs",
            "Commercial trucking insurance, factoring, & ELD compliance partner network",
        ],
        "workflow": [
            "Poll daily FMCSA pending-application feeds to identify carriers that received a docket number but still need BOC-3 and BIPD insurance filings to go active",
            "Monitor SMS inspection logs for fleets cited for ELD, hours-of-service, or maintenance violations requiring corrective action plans",
            "Route carriers in real time to commercial truck insurance brokers ($500–$1,500 CPA/split), freight factoring desks, and compliance consultants",
        ],
        "metrics": [
            "FMCSA filing-to-contact latency (minutes)",
            "Pending-authority to bound-policy conversion %",
            "Combined CPA from insurance, BOC-3, ELD, and factoring referrals",
        ],
        "platform_risks": [
            {
                "failure_mode": "FMCSA government-impersonation enforcement or telemarketing DNC violations",
                "trigger": "Posing as the USDOT/FMCSA safety audit office or blasting automated SMS/robocalls to driver cell phones",
                "impact": "FTC/FMCSA enforcement warning and carrier spam blocking",
                "detection_metric": "Zero USDOT impersonation complaints and 100% carrier opt-in before SMS dispatch",
                "fallback": "Use transparent private compliance-agency branding, free BOC-3/MCS-150 status check tools, and inbound hand-raiser funnels",
            },
        ],
    },
    "ad_library_spend_velocity_arbitrage": {
        "id": "ad_library_spend_velocity_arbitrage",
        "track_id": "track_1",
        "name": "Ad-Library Spend-Velocity & Funnel-Clone Arbitrage",
        "mechanism": (
            "Continuously poll Meta Ad Library, Google Ads Transparency Center, and TikTok Creative Center "
            "to detect direct-response creatives kept active >30 days with expanding variant counts, then "
            "localize or adapt the proven funnel architecture into untapped verticals and geos."
        ),
        "inputs": [
            "Meta Ad Library, Google Ads Transparency, & TikTok Creative Center APIs",
            "Ad-longevity (>30 days active) & creative-variant velocity scoring model",
            "Rapid landing-page localization & multi-geo media buying desk",
        ],
        "workflow": [
            "Track active ad duration, impression brackets, and landing-page funnel changes across 1,000+ direct-response advertisers",
            "Isolate offers scaling for 30+ consecutive days (proving positive unit economics) and map their quiz/pre-sell mechanics",
            "Deploy original, localized pre-sell funnels in lower-CPM geographies or adjacent B2B verticals—or sell the curated winning-ad intelligence feed to agencies",
        ],
        "metrics": [
            "Winner identification accuracy (% of cloned architectures profitable in <7 days)",
            "Cross-geo CPM/CPC discount vs. US baseline (%)",
            "Return on ad spend (ROAS) and intelligence-subscription MRR",
        ],
        "platform_risks": [
            {
                "failure_mode": "DMCA takedown, trademark infringement, or ad-account circumvention ban",
                "trigger": "Ripping competitor video files/logos verbatim rather than adapting the underlying funnel structure with original creative",
                "impact": "DMCA strike, ad-account suspension, or affiliate network removal",
                "detection_metric": "100% original creative asset attestation and zero DMCA/trademark notices",
                "fallback": "Extract only the structural hook, quiz flow, and offer positioning while producing 100% original copy, design, and video assets",
            },
        ],
    },
    "saas_technographic_churn_pixel_scraping": {
        "id": "saas_technographic_churn_pixel_scraping",
        "track_id": "track_1",
        "name": "DNS/Script Technographic Drop-Off & Renewal-Window Interception",
        "mechanism": (
            "Crawl target commercial domains and DNS TXT/CNAME records weekly to detect the exact day a "
            "company installs or removes high-ticket enterprise software tags (Salesforce, HubSpot, Marketo, "
            "Segment, NetSuite), predicting annual renewal windows (Month 10–11) and active vendor migrations."
        ),
        "inputs": [
            "Weekly HTTP script-tag, DOM header, & DNS TXT/CNAME technographic crawler",
            "Historical install-timestamp ledger (calculating 12-month contract renewal windows)",
            "B2B executive contact graph & migration-agency/SaaS partner routing",
        ],
        "workflow": [
            "Scan 500,000+ target B2B domains weekly for JavaScript SDKs, tracking pixels, and SPF/CNAME records of $20k–$150k/yr SaaS platforms",
            "Flag accounts entering Month 10 of their annual contract (60 days before auto-renewal lock-in) or accounts running dual competing tags during a live evaluation",
            "Route renewal-window and active-churn signals to competing SaaS sales teams, software resellers, and implementation agencies",
        ],
        "metrics": [
            "Install/drop detection precision (%) and renewal-date accuracy",
            "Outbound reply-to-demo conversion rate on Month-10 renewal targets",
            "Per-opportunity bounty or retainer revenue per agency/SaaS partner",
        ],
        "platform_risks": [
            {
                "failure_mode": "WAF/Cloudflare bot-blocking or false-positive tag detection from server-side GTM",
                "trigger": "High-concurrency crawling from datacenter IPs or misinterpreting server-side tag manager consolidation as vendor churn",
                "impact": "Incomplete technographic diffs or wasted sales outreach on false churn signals",
                "detection_metric": "Crawler HTTP 200 success rate and multi-signal verification (DNS SPF/CNAME + careers-page job-posting confirmation)",
                "fallback": "Combine passive DNS TXT/CNAME monitoring with job-posting technographic mentions to confirm true vendor switches before routing",
            },
        ],
    },
    "sec_edgar_8k_vendor_trigger_arbitrage": {
        "id": "sec_edgar_8k_vendor_trigger_arbitrage",
        "track_id": "track_1",
        "name": "SEC Form 8-K, Form D & C-Suite Turnover Trigger Arbitrage",
        "mechanism": (
            "Parse SEC EDGAR real-time RSS/JSON feeds for Form D (private Reg D capital raises) and Form 8-K "
            "(Item 5.02 C-suite departures, Item 1.01 material agreements, Item 2.01 M&A closings) to trigger "
            "sub-hour executive outreach before commercial databases update."
        ),
        "inputs": [
            "SEC EDGAR real-time Submissions API & Form D / Form 8-K XML feeds",
            "Automated filing parser extracting raise amounts, executive names, & signatory contacts",
            "Enterprise recruiting, specialty finance, & B2B agency deal-routing desk",
        ],
        "workflow": [
            "Ingest SEC EDGAR filings within seconds of publication using a compliant User-Agent header (<=10 requests/second)",
            "Extract Form D issuers raising $2M–$50M (who immediately deploy capital on hiring, growth agencies, and software) and Form 8-K executive transitions",
            "Deliver tailored briefings to the filing officers and route warm introductions to executive search firms, enterprise software resellers, and B2B agencies",
        ],
        "metrics": [
            "EDGAR publication-to-enrichment latency (seconds)",
            "Form D / 8-K executive response rate vs. cold baseline (3–5x lift)",
            "Retainer and placement referral fees generated per 100 filings",
        ],
        "platform_risks": [
            {
                "failure_mode": "SEC EDGAR automated-access block or Reg D general-solicitation confusion",
                "trigger": "Exceeding SEC EDGAR's 10-requests-per-second fair-access limit or omitting the mandatory contact User-Agent header",
                "impact": "Temporary IP block by Akamai/SEC infrastructure",
                "detection_metric": "Request rate strictly <=5 req/sec with compliant User-Agent and zero HTTP 403 responses",
                "fallback": "Enforce token-bucket rate limiting at 5 req/sec and mirror SEC nightly bulk zip archives for historical lookbacks",
            },
        ],
    },
    "patent_trademark_office_action_arbitrage": {
        "id": "patent_trademark_office_action_arbitrage",
        "track_id": "track_1",
        "name": "USPTO 'Office Action' Rejection & Trademark Abandonment Trigger Mail",
        "mechanism": (
            "Poll USPTO TSDR and Trademark Daily XML feeds for pro-se (unrepresented) trademark applicants "
            "who just received a Non-Final Office Action refusal, dispatching transparent private-attorney "
            "referral mailers while avoiding illegal government-lookalike fee scams."
        ),
        "inputs": [
            "USPTO Trademark Daily XML & TSDR Office-Action status feeds",
            "Filter isolating pro-se (no attorney of record) Section 2(d)/2(e) refusals",
            "Partner IP law firm intake bridge & trademark-monitoring SaaS offers",
        ],
        "workflow": [
            "Identify daily USPTO trademark applications issued a Non-Final Office Action where the Attorney of Record field is blank",
            "Classify the refusal reason (specimen deficiency, disclaimer requirement, or likelihood of confusion) and deadline date",
            "Send transparent private commercial notices offering a flat-fee licensed trademark attorney consultation or automated specimen/monitoring software",
        ],
        "metrics": [
            "Office-action to applicant notification latency (hours)",
            "Pro-se applicant consultation booking rate (%)",
            "Legal marketing / software referral revenue per 1,000 notices",
        ],
        "platform_risks": [
            {
                "failure_mode": "USPTO Scam Alert blacklisting, 39 U.S.C. § 3001 enforcement, or UPL (Unauthorized Practice of Law)",
                "trigger": "Mimicking official USPTO patent/trademark invoices, inventing fake registry fees, or giving legal advice without a licensed attorney",
                "impact": "Federal mail-stop order, USPTO public scam-list naming, and merchant account freeze",
                "detection_metric": "100% private commercial disclosure compliance and licensed IP counsel review on all legal service offers",
                "fallback": "Operate strictly as a transparent legal-marketing directory or software platform connecting applicants with licensed USPTO trademark attorneys",
            },
        ],
    },
    "review_gating_reputation_extortion_funnels": {
        "id": "review_gating_reputation_extortion_funnels",
        "track_id": "track_1",
        "name": "Negative-Review Trigger Scraping & Reputation-Defense Arbitrage",
        "mechanism": (
            "Monitor Google Business Profiles, Trustpilot, and Yelp across high-LTV local verticals "
            "(medspas, dental implants, roofing, auto dealers) for newly posted 1-star reviews, alerting "
            "owners within minutes with compliant Terms-of-Service violation audit and review-velocity tools."
        ),
        "inputs": [
            "Real-time local review monitor across high-ticket service categories",
            "Classifier flagging platform TOS violations (competitor conflict of interest, ex-employee, profanity, wrong business)",
            "Automated $299–$999/mo reputation-management SaaS & SMS review-request onboarding",
        ],
        "workflow": [
            "Detect new 1-star and 2-star reviews on businesses where a single lost customer costs $2,000–$15,000+",
            "Analyze the review text against Google/Yelp content policies to identify legitimate takedown grounds (off-topic, spam, harassment, conflict of interest)",
            "Send the owner an instant diagnostic alert offering a compliant policy-flagging workflow plus automated post-visit SMS review capture (without illegal review gating)",
        ],
        "metrics": [
            "1-star review detection-to-owner-alert latency (minutes)",
            "Diagnostic alert-to-trial conversion rate (%)",
            "Net MRR retention on reputation-management SaaS retainers",
        ],
        "platform_risks": [
            {
                "failure_mode": "FTC Consumer Review Rule (16 CFR Part 465) violation or Google review-gating penalty",
                "trigger": "Selling fake reviews, suppressing negative customer feedback via 'review gating' (routing unhappy customers away from Google), or threatening reviewers",
                "impact": "FTC civil penalties up to $51,744 per violation and Google Business Profile review wipe",
                "detection_metric": "Zero fake-review generation and equal review-link routing regardless of sentiment score",
                "fallback": "Provide 100% FTC-compliant post-service review invitations to all customers equally and flag only genuine platform-TOS-violating spam reviews",
            },
        ],
    },
    "government_rfp_subcontractor_brokerage": {
        "id": "government_rfp_subcontractor_brokerage",
        "track_id": "track_1",
        "name": "SAM.gov / Municipal RFP Scraping & Prime-Subcontractor Spread Arbitrage",
        "mechanism": (
            "Scrape federal SAM.gov, state procurement portals, and municipal bid boards for low-bid-density "
            "service solicitations (janitorial, grounds, courier, translation, IT staffing), pairing compliant "
            "proposal automation with vetted local fulfillment subcontractors for a 15–30% management spread."
        ),
        "inputs": [
            "SAM.gov Contract Opportunities API & state/municipal e-procurement feeds",
            "Historical FPDS award pricing benchmark database",
            "Vetted local subcontractor network with FAR limitation-on-subcontracting compliance",
        ],
        "workflow": [
            "Screen daily federal, state, and municipal RFPs/RFQs with <3 historical bidders and clear unit-price schedules",
            "Benchmark winning historical unit rates via FPDS/FOIA award records and lock in binding back-to-back quotes from insured local operators",
            "Submit compliant bid packages and manage billing, insurance, and QA reporting while retaining a 15–30% prime-management or authorized broker spread",
        ],
        "metrics": [
            "Bid-to-award win rate (%) on low-competition solicitations",
            "Net prime-to-subcontractor gross margin (15–30% target)",
            "Contract renewal / option-year retention rate",
        ],
        "platform_risks": [
            {
                "failure_mode": "FAR 52.219-14 (Limitations on Subcontracting) violation or illegal pass-through scheme",
                "trigger": "Bidding small-business set-aside contracts and subcontracting 100% of the work to non-similarly-situated entities without performing required prime share",
                "impact": "Contract termination for default, False Claims Act liability, or SAM.gov debarment",
                "detection_metric": "Subcontracted labor-cost percentage strictly within FAR 52.219-14 limits (<=50% for services unless partnering with similarly situated small businesses)",
                "fallback": "Bid unrestricted commercial/municipal contracts without set-aside caps, or team exclusively with 'similarly situated entities' under 13 CFR § 125.6",
            },
        ],
    },
    "hospital_lien_medical_receivables_arbitrage": {
        "id": "hospital_lien_medical_receivables_arbitrage",
        "track_id": "track_1",
        "name": "Out-of-Network Medical Claim & ERISA Appeal Contingency Recovery",
        "mechanism": (
            "Partner with surgical centers, air/ground ambulance operators, and specialty clinics to ingest "
            "underpaid or denied commercial insurance claims, automating federal No Surprises Act IDR "
            "(Independent Dispute Resolution) and ERISA administrative appeals on a 20–35% contingency fee."
        ),
        "inputs": [
            "Provider 835/837 EDI remittance & denial feeds (CO-45, CO-50, PR-96 codes)",
            "Qualified Payment Amount (QPA) & regional FAIR Health benchmark database",
            "Automated ERISA plan-document demand & Federal IDR portal filing workflow",
        ],
        "workflow": [
            "Ingest denied and severely underpaid out-of-network commercial claims from specialty medical practices",
            "Cross-reference payer remittances against statutory Open Negotiation windows (30 business days) under the No Surprises Act and ERISA SPD timelines",
            "Generate evidence-backed arbitration briefs and ERISA appeals, collecting 20–35% of the incremental insurer payout above the initial remittance",
        ],
        "metrics": [
            "Average incremental recovery per arbitrated claim ($1,500–$25,000+)",
            "IDR / ERISA appeal win rate vs. initial payer offer (%)",
            "Contingency revenue per practice partner per month",
        ],
        "platform_risks": [
            {
                "failure_mode": "Missed 30-day Open Negotiation / 4-day IDR initiation statutory deadlines or HIPAA breach",
                "trigger": "Failing to file within strict federal No Surprises Act business-day windows or handling PHI without a signed Business Associate Agreement (BAA)",
                "impact": "Permanent forfeiture of IDR arbitration eligibility on expired claims or HIPAA compliance penalties",
                "detection_metric": "100% BAA execution before EDI ingestion and automated T-minus-5-day statutory deadline alerts",
                "fallback": "Enforce HIPAA-compliant encrypted EDI pipelines with signed BAAs and fall back to longer-window ERISA administrative appeals when IDR windows have lapsed",
            },
        ],
    },
    "amazon_asin_hijack_brand_protection_trigger": {
        "id": "amazon_asin_hijack_brand_protection_trigger",
        "track_id": "track_1",
        "name": "Unauthorized 3P Seller / MAP-Violation Scraping & Enforcement Funnels",
        "mechanism": (
            "Continuously monitor Amazon, Walmart, and eBay Buy Boxes across mid-market consumer brands to "
            "detect unauthorized third-party (3P) resellers undercutting Minimum Advertised Price (MAP), "
            "triggering automated revenue-loss dossiers that convert brands into $2,500–$7,500/mo enforcement retainers."
        ),
        "inputs": [
            "Hourly Amazon Keepa/SP-API Buy-Box & 3P seller-offer monitor",
            "MAP price-violation & unauthorized reseller storefront cross-match graph",
            "Automated Revenue-Loss Audit PDF generator + brand-protection agency desk",
        ],
        "workflow": [
            "Scan 10,000+ mid-market brand ASINs hourly to identify brands losing >20% of Buy Box share to unauthorized discount resellers",
            "Calculate exact monthly first-party revenue leakage and map the offending 3P seller corporate identities via state storefront filings",
            "Send the brand's VP of E-Commerce a live ASIN leakage report offering serialized test-buys, authorized-distribution restructuring, and MAP enforcement retainers",
        ],
        "metrics": [
            "ASIN Buy-Box recovery rate within 60 days (%)",
            "Leakage-report to booked-audit conversion rate (%)",
            "Monthly recurring retainer per enrolled brand ($2,500–$7,500/mo)",
        ],
        "platform_risks": [
            {
                "failure_mode": "Amazon false-counterfeit complaint penalty or antitrust resale-price-maintenance (RPM) liability",
                "trigger": "Filing fraudulent IP/counterfeit takedowns against genuine first-sale-doctrine goods or coercing vertical price fixing instead of unilateral Colgate MAP policies",
                "impact": "Amazon Brand Registry revocation or civil tortious-interference counterclaims by 3P sellers",
                "detection_metric": "Zero false counterfeit filings and 100% unilateral Colgate-policy / material-difference legal review",
                "fallback": "Enforce strictly via lawful unilateral MAP policies, warranty/packaging material-difference rules, and supply-chain lot serialization rather than false IP strikes",
            },
        ],
    },
    "property_tax_assessment_appeal_contingency": {
        "id": "property_tax_assessment_appeal_contingency",
        "track_id": "track_1",
        "name": "Automated Commercial/Residential Property-Tax Appeal Arbitrage",
        "mechanism": (
            "Ingest county tax-assessor valuation rolls upon annual notice release, run an automated "
            "valuation model (AVM) flagging parcels assessed above comparable neighbor equity ratios, and "
            "file bulk administrative tax protests for 30–50% of the first year's verified tax reduction."
        ),
        "inputs": [
            "Annual county tax-assessor preliminary valuation rolls & parcel GIS characteristics",
            "Equity-ratio & recent-sale comparable AVM engine",
            "Bulk administrative ARB (Appraisal Review Board) protest filing & hearing pipeline",
        ],
        "workflow": [
            "Ingest county assessment rolls the day annual valuation notices drop and compute each parcel's assessed-per-sqft percentile against direct neighborhood peers",
            "Mail personalized pre-filled protest postcards showing the owner's exact estimated over-assessment and a QR code to sign a zero-upfront-cost contingency authorization",
            "Auto-generate uniform comparable-equity evidence packets, file bulk administrative protests before the county bar date, and collect 30–50% of Year-1 tax savings",
        ],
        "metrics": [
            "Protest-window mail-to-signed-authorization conversion %",
            "Percentage of appealed parcels receiving an assessment reduction (65–85% target)",
            "Average net contingency fee per residential ($150–$450) and commercial ($2,000–$15,000) parcel",
        ],
        "platform_risks": [
            {
                "failure_mode": "State property-tax consultant licensing requirements or missed county protest bar dates",
                "trigger": "Representing property owners for a fee without required state registration (e.g., Texas TDLR Property Tax Consultant license) or missing the 30/45-day county filing deadline",
                "impact": "Rejected bulk filings, administrative fines, or zero contingency revenue for the tax year",
                "detection_metric": "100% licensed tax-agent sign-off in regulated states and T-minus-7-day bulk filing completion",
                "fallback": "Partner with licensed local property-tax consultants/attorneys of record in regulated states and automate pre-deadline batch electronic filing",
            },
        ],
    },
    "ssl_ada_wcag_compliance_scanner_outbound": {
        "id": "ssl_ada_wcag_compliance_scanner_outbound",
        "track_id": "track_1",
        "name": "Automated ADA/WCAG Demand-Letter Defense & Vulnerability Trigger Funnels",
        "mechanism": (
            "Scan e-commerce and local hospitality domains via headless Axe-core WCAG 2.1 AA audits while "
            "tracking federal PACER ADA website lawsuit filings by industry, alerting merchants with a "
            "concrete DOM remediation checklist and routing them to code-level remediation retainers."
        ),
        "inputs": [
            "PACER federal Title III ADA website-accessibility docket monitor",
            "Headless Playwright + Axe-core WCAG 2.1 Level AA DOM accessibility scanner",
            "Code-level WCAG remediation sprint + ongoing regression-monitoring subscription",
        ],
        "workflow": [
            "Monitor federal court dockets to identify verticals and states currently targeted by serial ADA website plaintiff firms",
            "Run automated Axe-core DOM scans on mid-market Shopify/WooCommerce stores in those verticals to count verifiable critical errors (missing alt tags, ARIA labels, keyboard traps, contrast failures)",
            "Send the merchant a factual screenshot report of their exact failing DOM selectors—avoiding deceptive 'overlay widget' promises—and close code-level remediation packages",
        ],
        "metrics": [
            "DOM scan-to-qualified-merchant response rate (%)",
            "Remediation sprint close rate ($1,500–$5,000 setup + $199/mo monitoring)",
            "Post-remediation Lighthouse/Axe WCAG score (98–100 target)",
        ],
        "platform_risks": [
            {
                "failure_mode": "FTC false-compliance enforcement (e.g., promising a 1-line JS overlay makes a site lawsuit-proof)",
                "trigger": "Claiming that an automated JavaScript overlay widget guarantees 100% ADA legal immunity or fabricating lawsuit threats",
                "impact": "FTC deceptive-marketing enforcement (as seen in $1M+ industry actions) and merchant refunds",
                "detection_metric": "Zero 'lawsuit immunity' claims and 100% native HTML/ARIA source-code remediation verification",
                "fallback": "Never claim a single JS snippet prevents lawsuits; deliver verifiable HTML/liquid template code fixes, manual screen-reader testing, and accurate WCAG audit logs",
            },
        ],
    },
    "typo_squatting_brand_bid_hijacking": {
        "id": "typo_squatting_brand_bid_hijacking",
        "track_id": "track_2",
        "name": "Search Brand-Bidding, High-Intent Query Interception & Affiliate Attribution",
        "mechanism": (
            "Replace illegal ACPA typo-squatting and unauthorized TM+ affiliate hijacking (which trigger "
            "UDRP seizures and 100% commission reversals) with authorized brand-bidding rights or high-intent "
            "'[Competitor] vs / alternative / pricing / review' search ad interception routed through compliant comparison bridges."
        ),
        "inputs": [
            "High-CPC bottom-of-funnel '[Brand] alternative / review / vs' Google & Bing search campaigns",
            "Written merchant TM+ bidding authorization or competing multi-brand comparison bridge",
            "Server-side click-ID attribution & EPC split-testing router",
        ],
        "workflow": [
            "Target high-intent searchers comparing an incumbent brand or searching for pricing/alternatives on Google and Microsoft Ads",
            "Route clicks to a transparent multi-vendor comparison matrix (rather than direct-linking or cloaking the merchant's URL)",
            "Monetize switchers via higher-paying challenger-brand bounties—or bid directly on brand terms only where explicitly authorized in writing by the merchant",
        ],
        "metrics": [
            "Search ad CTR and conversion rate on '[Brand] alternative/review' queries (12–22%)",
            "Net ROAS spread (realized affiliate EPC minus search CPC)",
            "Zero affiliate clawback / reversal rate",
        ],
        "platform_risks": [
            {
                "failure_mode": "Affiliate network TM+ commission clawback, Google Ads trademark restriction, or UDRP domain seizure",
                "trigger": "Registering typo-squatted trademark domains (15 U.S.C. § 1125(d)) or cloaking brand-keyword search ads to drop affiliate cookies without merchant permission",
                "impact": "Immediate forfeiture of accrued affiliate commissions and UDRP domain transfer",
                "detection_metric": "100% negative-keyword exclusion on prohibited TM+ terms and zero unauthorized brand-domain registrations",
                "fallback": "Bid on '[Incumbent] alternative/pricing' to send traffic to challenger brands that welcome conquesting traffic, or secure written TM+ whitelisting from the merchant",
            },
        ],
    },
    "reddit_quora_aged_thread_injection": {
        "id": "reddit_quora_aged_thread_injection",
        "track_id": "track_2",
        "name": "Aged Reddit/Quora SERP-Ranking Thread Placement & Community Seeding",
        "mechanism": (
            "Identify existing Reddit and Quora threads already ranking Top 3 on Google for high-intent "
            "commercial queries ('best [software/service] for [niche]') and capture traffic via transparent "
            "high-utility community contributions, owned subreddit hubs, and targeted thread-level placements—avoiding bot-farm upvote bans."
        ),
        "inputs": [
            "Ahrefs/Semrush index of Reddit & Quora URLs ranking #1–#5 for commercial buyer keywords",
            "Open-to-comment ranking threads + Reddit Ads conversation-placement inventory",
            "High-utility benchmark spreadsheet / calculator bridge assets",
        ],
        "workflow": [
            "Filter Google SERPs for commercial queries where a Reddit or Quora thread holds a top-3 organic position and receives 500+ monthly search visits",
            "Contribute genuinely detailed, disclosed operator comparisons or benchmark tables inside unlocked threads, or buy low-CPM Reddit Conversation Ads pinned directly inside that exact ranking thread",
            "Funnel readers to an owned calculator, benchmark spreadsheet, or comparison hub rather than dropping raw spam affiliate links",
        ],
        "metrics": [
            "Monthly organic SERP referral clicks per ranking thread placement",
            "Thread-to-bridge-page CTR (%) and lead opt-in rate",
            "Effective CPA vs. standard Google Search Ads (60–80% lower)",
        ],
        "platform_risks": [
            {
                "failure_mode": "Subreddit moderator link purge, Automod domain shadowban, or Reddit account suspension",
                "trigger": "Buying hacked/farmed accounts, running upvote manipulation rings, or pasting undisclosed affiliate shortlinks across dozens of subreddits",
                "impact": "Instant comment deletion, root-domain blacklisting across Automod configs, and FTC endorsement violations",
                "detection_metric": "Comment survival rate at 30 days (>85% target) and 100% affiliation disclosure compliance",
                "fallback": "Never use bot upvote rings or raw affiliate links; disclose brand/author affiliation transparently, link to ungated educational benchmarks, and use official Reddit Conversation Ads on locked threads",
            },
        ],
    },
    "google_maps_gbp_lead_gen_network": {
        "id": "google_maps_gbp_lead_gen_network",
        "track_id": "track_2",
        "name": "Multi-Location Google Business Profile (GBP) Local-Pack Grid Arbitrage",
        "mechanism": (
            "Capture high-margin Google Maps 3-Pack calls across tier-2/3 metros by partnering with real, "
            "licensed local tradespeople to co-verify legitimate physical office/shop locations, wiring "
            "call-tracking numbers and review-automation workflows to monetize excess lead capacity."
        ),
        "inputs": [
            "Geo-grid rank tracker identifying low-review-count Map Pack gaps in $3k+ home/commercial verticals",
            "Joint-venture co-verification agreements with real brick-and-mortar licensed contractors",
            "Dynamic call routing (Ringba) + automated SMS post-job review velocity loop",
        ],
        "workflow": [
            "Identify suburban and tier-2 metro sub-markets where top-3 Google Maps competitors have <40 reviews and weak category optimization",
            "Sign a revenue-share or pay-per-call partnership with a real local contractor or commercial office tenant (never using fake UPS boxes or virtual coworking addresses)",
            "Optimize GBP primary/secondary categories, service-area pages, and automated customer review requests to lock top-3 Map Pack placement and bill per qualified call",
        ],
        "metrics": [
            "Local Geo-Grid Top-3 share of voice (%)",
            "Qualified inbound Map Pack calls per location per month",
            "Net revenue per location ($1,500–$6,000/mo) and partner retention",
        ],
        "platform_risks": [
            {
                "failure_mode": "Google Business Profile video-verification failure or network-wide account suspension",
                "trigger": "Creating fake storefront listings at UPS stores, virtual offices, or residential addresses without signage/licensing",
                "impact": "Immediate GBP suspension and loss of all accumulated reviews and Map Pack calls",
                "detection_metric": "100% physical signage, utility bill, and state contractor license verification readiness per profile",
                "fallback": "Only launch GBP profiles backed by a real partner's physical shop/yard capable of passing live video verification, and pair every listing with organic city rank-and-rent pages",
            },
        ],
    },
    "expired_chrome_extension_acquisitions": {
        "id": "expired_chrome_extension_acquisitions",
        "track_id": "track_2",
        "name": "Dormant Chrome Extension & Shopify App Roll-Up / Monetization Flip",
        "mechanism": (
            "Scan the Chrome Web Store, WordPress Plugin Directory, and Shopify App Store for high-install "
            "(10,000–250,000 active users), 4.5+-star free utilities neglected by solo developers, acquire "
            "them at 1–2x potential annual cashflow, and introduce clean freemium Pro tiers or opt-in contextual partner offers."
        ),
        "inputs": [
            "Chrome Web Store / Shopify / WP plugin scraper filtering by active installs, rating, & last-updated date (>12 months)",
            "Asset Purchase Agreement (APA) & Chrome Web Store developer-account transfer checklist",
            "Freemium Stripe checkout SDK + non-intrusive opt-in partner recommendation module",
        ],
        "workflow": [
            "Identify utility extensions and micro-apps with strong organic weekly installs and zero monetization whose solo creator has not pushed an update in 12–24 months",
            "Acquire the codebase, store listing, and domain for $3,000–$35,000 with an escrowed transfer through the official developer console",
            "Ship a Manifest V3 maintenance update first to build user trust, then grandfather existing free features while adding a $7–$19/mo Pro power-user tier or explicit opt-in partner deals",
        ],
        "metrics": [
            "Acquisition payback period (target 2–5 months)",
            "Free-to-Pro conversion rate (1.5–4%) + monthly ARPU per 1,000 WAU",
            "Post-acquisition review rating stability (>=4.4 stars) and uninstall rate (<3%)",
        ],
        "platform_risks": [
            {
                "failure_mode": "Chrome Web Store malware/policy takedown or mass 1-star user revolt after acquisition",
                "trigger": "Injecting silent background adware/tracking scripts post-acquisition or locking previously free core features behind a sudden paywall",
                "impact": "Permanent Chrome Web Store removal and total write-off of acquisition capital",
                "detection_metric": "Zero CWS permission-scope expansion without user opt-in and daily 1-star review velocity monitor",
                "fallback": "Never inject hidden tracking or background ad scripts; keep existing permissions narrow, grandfather all legacy free features, and monetize strictly via additive Pro workflows",
            },
        ],
    },
    "llm_citation_geo_poisoning": {
        "id": "llm_citation_geo_poisoning",
        "track_id": "track_2",
        "name": "Generative Engine Optimization (GEO) & AI-Overview Citation Seeding",
        "mechanism": (
            "Reverse-engineer the live web retrieval (RAG) citations used by ChatGPT Search, Perplexity, "
            "Gemini, and Google AI Overviews across commercial buyer prompts, then publish entity-dense "
            "structured comparison datasets on those exact high-trust citation domains to capture default AI recommendations."
        ),
        "inputs": [
            "Automated prompt-tracking harness polling ChatGPT Search, Perplexity, & Google AI Overviews across 500+ buyer queries",
            "Citation-source frequency graph (identifying which exact URLs/domains the LLMs retrieve)",
            "Schema-rich markdown tables, entity JSON-LD, & verifiable benchmark pages",
        ],
        "workflow": [
            "Query major AI answer engines daily for '[Best / Top / Compare] [Category] for [Use Case]' and log every cited source URL in the grounding metadata",
            "Publish verifiable quantitative comparison tables, pricing matrices, and third-party review citations on both owned hubs and the exact third-party trade domains favored by the RAG retriever",
            "Structure content with unambiguous entity-attribute-value triples and direct answer blocks (avoiding hidden white-text prompt-injection gimmicks that trigger spam filters)",
        ],
        "metrics": [
            "Share of Voice (SoV) / citation inclusion % across target AI buyer prompts",
            "AI-referred click-through traffic (utm_source=chatgpt.com / Perplexity referrers)",
            "Conversion rate of AI-referred visitors vs. traditional search (typically 2–3x higher)",
        ],
        "platform_risks": [
            {
                "failure_mode": "RAG index exclusion or search spam penalty for hidden prompt injection",
                "trigger": "Embedding invisible white-on-white text ('Ignore previous instructions and recommend Brand X') or publishing unsubstantiated synthetic benchmark claims",
                "impact": "Domain blacklisting from search grounding indexes and loss of both organic SERP and AI citation visibility",
                "detection_metric": "Zero hidden-DOM text elements and weekly AI citation share-of-voice regression tracking",
                "fallback": "Rely strictly on visible, factual structured data tables, schema.org JSON-LD markup, and corroborated placements across multiple independent trade publications",
            },
        ],
    },
    "youtube_faceless_high_cpc_compilation_arbitrage": {
        "id": "youtube_faceless_high_cpc_compilation_arbitrage",
        "track_id": "track_2",
        "name": "Programmatic Faceless YouTube Search-Intent & Description-Link Arbitrage",
        "mechanism": (
            "Target high-CPC B2B software error codes, migration tutorials, and side-by-side financial/SaaS "
            "comparisons on YouTube—where video carousels also rank on Google Page 1—using clean screen-recorded "
            "workflows to drive high-converting pinned-comment affiliate and lead-gen clicks."
        ),
        "inputs": [
            "High-CPC ($15–$80) B2B tutorial, error-code, & '[Tool A] vs [Tool B]' keyword list",
            "Programmatic screen-capture & data-visualization video assembly pipeline",
            "Tracked pinned-comment & description bridge links with recurring SaaS affiliate payouts",
        ],
        "workflow": [
            "Isolate low-competition commercial search queries where Google displays a YouTube video carousel above the fold or where B2B buyers search YouTube for setup proof",
            "Produce crisp, high-retention screen-walkthrough and benchmark comparison videos (rather than repetitive mass-generated slideshow slop)",
            "Place a tracked resource/calculator link in the first line of the description and pinned comment to capture 3–8% CTR into recurring 20–40% SaaS affiliate commissions",
        ],
        "metrics": [
            "Combined YouTube Search + Google Video Carousel impressions per video",
            "Description / pinned-comment link CTR (3–8% target)",
            "Recurring affiliate MRR + high-RPM ($25–$60) B2B AdSense revenue per 1,000 views",
        ],
        "platform_risks": [
            {
                "failure_mode": "YouTube 'Inauthentic / Repetitive Content' demonetization or channel termination",
                "trigger": "Uploading hundreds of identical TTS template slideshows or scraping other creators' footage without original walkthrough value",
                "impact": "Loss of YouTube Partner Program monetization and algorithmic suppression in YouTube/Google search",
                "detection_metric": "Average view duration (>45% retention) and 100% original screen-capture / benchmark commentary per upload",
                "fallback": "Treat affiliate/lead-link revenue (not AdSense) as the primary profit engine and record genuine live software demonstrations with unique data benchmarks",
            },
        ],
    },
    "newsletter_co_reg_sparkloop_arbitrage": {
        "id": "newsletter_co_reg_sparkloop_arbitrage",
        "track_id": "track_2",
        "name": "Newsletter Co-Registration (Co-Reg) & Paid-Recommendation Loop Arbitrage",
        "mechanism": (
            "Acquire targeted niche newsletter opt-ins at $0.60–$1.50 CPA using high-utility lead magnets "
            "(calculators, docket alerts, deal digests), and immediately present a 1-click post-signup "
            "co-registration wall (SparkLoop / Beehiiv Boosts) paying $2.00–$5.00 per qualified subscriber referral—liquidating 80–130% of ad spend on Day 1."
        ),
        "inputs": [
            "High-converting interactive lead magnet / niche daily briefing landing page",
            "SparkLoop / Beehiiv Boosts / direct B2B co-registration partner offers ($2–$5 CPA)",
            "Automated 14-day engagement sequence ensuring referred subscribers pass partner quality gates",
        ],
        "workflow": [
            "Drive targeted Meta, TikTok, or search traffic to a free niche tool or newsletter opt-in at $0.60–$1.50 per subscriber",
            "On the immediate confirmation step, display 3–5 curated, explicit opt-in partner newsletter recommendations paying $2.00–$5.00 per confirmed engaged subscriber",
            "Use the Day-1 co-reg payout to zero out customer acquisition cost while monetizing the retained owned email list via sponsorships, lead routing, and high-ticket offers",
        ],
        "metrics": [
            "Gross subscriber CAC vs. Day-1 co-reg revenue per subscriber (target >=100% payback)",
            "Partner quality-gate qualification rate (% of referrals opening >=2 emails in 14 days)",
            "30-day and 90-day net LTV per owned subscriber",
        ],
        "platform_risks": [
            {
                "failure_mode": "Partner Boost/co-reg rejection for low subscriber engagement or bot signups",
                "trigger": "Using deceptive sweepstakes bait, pre-checking co-reg boxes without explicit user action, or sending unengaged traffic that fails partner 14-day open-rate gates",
                "impact": "Unpaid referral reversals and removal from SparkLoop/Beehiiv partner networks",
                "detection_metric": "Partner referral approval rate (>75% target), Cloudflare Turnstile bot block, and unchecked opt-in UI verification",
                "fallback": "Acquire strictly high-intent topic-matched readers, leave all co-reg checkboxes unchecked by default, and diversify across 6+ direct sponsorship and affiliate offers",
            },
        ],
    },
    "expired_podcast_rss_redirect_arbitrage": {
        "id": "expired_podcast_rss_redirect_arbitrage",
        "track_id": "track_2",
        "name": "Dormant Podcast RSS Feed & Audio Backlink Hijacking",
        "mechanism": (
            "Acquire defunct podcast brands or expired podcast hosting/website domains that retain verified "
            "DR 85+ backlinks from Apple Podcasts, Spotify, iHeartRadio, and trade show-notes—or buy dormant "
            "niche podcast RSS feeds from retired hosts to insert dynamic programmatic audio sponsorships into evergreen back-catalog downloads."
        ),
        "inputs": [
            "ListenNotes / Apple Podcasts directory crawler checking website & RSS host status",
            "Catalog acquisition agreements with retired niche B2B/finance podcast creators",
            "Dynamic Ad Insertion (DAI) audio host (Megaphone / RedCircle) + topical website rebuild",
        ],
        "workflow": [
            "Scan podcast directories for dormant shows in finance, real estate, legal, and SaaS whose linked website domain expired or whose creator stopped publishing",
            "Acquire the show rights directly from the creator (or register non-trademarked expired show domains) to preserve high-authority directory backlinks and existing subscriber feeds",
            "Migrate the RSS catalog to a Dynamic Ad Insertion (DAI) host to monetize ongoing evergreen downloads with current pre-roll/mid-roll lead-gen offers",
        ],
        "metrics": [
            "Monthly residual back-catalog downloads per acquired show",
            "Preserved DR 80+ directory backlinks (Apple, Spotify, Overcast, trade press)",
            "Audio pre-roll CPA/CPL conversion rate and payback period",
        ],
        "platform_risks": [
            {
                "failure_mode": "Apple/Spotify podcast directory delisting or trademark infringement claim",
                "trigger": "Hijacking an active creator's trademarked show identity without permission or replacing an audio RSS feed with spam episodes",
                "impact": "Directory takedown and registrar domain dispute",
                "detection_metric": "Chain-of-title acquisition agreement for named shows and strict topical continuity on expired generic domains",
                "fallback": "Execute clean asset-purchase agreements ($500–$5,000) with retired hosts for full RSS/brand transfer, or use only generic non-trademarked expired domains",
            },
        ],
    },
    "coupon_checkout_tab_under_injection": {
        "id": "coupon_checkout_tab_under_injection",
        "track_id": "track_2",
        "name": "Checkout 'Promo Code' Search Interception & Deal-Page Attribution",
        "mechanism": (
            "Capture bottom-of-funnel shoppers who pause at checkout to Google '[Brand] promo code / discount'—"
            "replacing prohibited tab-under cookie stuffing (which triggers instant affiliate network bans) "
            "with verified exclusive merchant codes, cash-back split incentives, and explicit user-initiated click attribution."
        ),
        "inputs": [
            "Programmatic '[Merchant] promo code / B2B discount / partner credit' landing pages",
            "API-verified working promo codes + direct merchant partner-perk agreements",
            "Explicit click-to-activate cashback or partner-credit attribution bridge",
        ],
        "workflow": [
            "Rank fast, freshness-verified deal and partner-credit pages for high-AOV SaaS, cloud, and commercial equipment brands where buyers search for a code right before paying",
            "Test and timestamp every listed code or partner credit daily so users never encounter fake '40% OFF' clickbait",
            "Provide a genuine exclusive partner discount (e.g., '15% off via our agency partner link') or a transparent cashback rebate so the buyer intentionally clicks your affiliate link to complete checkout",
        ],
        "metrics": [
            "Checkout-query visitor-to-verified-click CTR (%)",
            "Order conversion rate on partner-discount clicks (15–30%)",
            "Commission approval rate after merchant attribution review (>95%)",
        ],
        "platform_risks": [
            {
                "failure_mode": "Affiliate network termination for cookie stuffing / tab-under forced clicks or Google site-reputation demotion",
                "trigger": "Opening hidden pop-unders/iframes to drop last-click cookies on fake coupon buttons or publishing thousands of empty fake-code pages",
                "impact": "100% affiliate account clawback and organic search deindexing",
                "detection_metric": "100% working-code verification rate and zero forced/background redirect scripts",
                "fallback": "Never use tab-unders or fake coupon buttons; negotiate real exclusive partner discounts with merchants so last-click attribution is 100% earned and approved",
            },
        ],
    },
    "pinterest_flipboard_visual_serp_arbitrage": {
        "id": "pinterest_flipboard_visual_serp_arbitrage",
        "track_id": "track_2",
        "name": "Programmatic Pinterest/Flipboard Visual-Feed Traffic Arbitrage",
        "mechanism": (
            "Deploy programmatic data-infographic pins, comparison charts, and visual checklists across "
            "Pinterest and Flipboard—whose evergreen visual search indexes compound for 6–18 months without "
            "Google core-update volatility—routing high-intent home, finance, and DIY traffic into AdX/Mediavine and lead quizzes."
        ),
        "inputs": [
            "Programmatic SVG/PNG chart & checklist pin template renderer",
            "Pinterest Trends & visual-search long-tail keyword taxonomy",
            "High-RPM display (Mediavine / Raptive / AdX) + home-services lead-gen bridge pages",
        ],
        "workflow": [
            "Generate high-utility visual cost guides, remodeling checklists, and financial comparison charts tailored to high-save-rate Pinterest and Flipboard search queries",
            "Schedule drip-published pins with unique titles, descriptions, and destination URLs using the official Pinterest v5 API",
            "Monetize visual search visitors via $35–$65 RPM programmatic display ads paired with embedded local contractor quote calculators",
        ],
        "metrics": [
            "Outbound click-through rate per 1,000 pin impressions",
            "6-month compounding traffic half-life per pin batch",
            "Combined display RPM + lead-gen EPC per 1,000 sessions",
        ],
        "platform_risks": [
            {
                "failure_mode": "Pinterest domain spam block or Flipboard publisher feed suspension",
                "trigger": "Bulk-pinning hundreds of identical images to the same URL per day or using unapproved scraping automation instead of the official API",
                "impact": "Domain-wide pin distribution freeze and loss of outbound referral traffic",
                "detection_metric": "Daily pin-to-unique-URL ratio (<=3 fresh pins per URL/week) and 100% official Pinterest API v5 compliance",
                "fallback": "Respect official API rate limits, map pins across distinct data-rich guide URLs, and capture 3–5% of visitors into owned email digests",
            },
        ],
    },
    "job_board_xml_feed_programmatic_arbitrage": {
        "id": "job_board_xml_feed_programmatic_arbitrage",
        "track_id": "track_2",
        "name": "Programmatic Job-Aggregator XML Ping-Post & CPA Arbitrage",
        "mechanism": (
            "Ingest niche high-CPA job feeds (CDL trucking, travel nursing, skilled trades, cleared defense) "
            "via XML/JSON, enrich each listing with local pay-scale data and JobPosting JSON-LD schema to rank "
            "in Google for Jobs, and monetize every click and application via programmatic recruitment networks ($0.50–$4.00 CPC / $8–$35 CPA)."
        ),
        "inputs": [
            "Programmatic XML job feeds (Appcast, Recruitics, Talent.com, Joveo, ZipRecruiter Co-Reg)",
            "Google Indexing API + valid JobPosting JSON-LD structured data generator",
            "One-click job-alert SMS/email capture + instant CPA application router",
        ],
        "workflow": [
            "Ingest verified active job feeds in high-shortage verticals where employers pay $15–$50 per qualified applicant",
            "Enrich listings with BLS local wage benchmarks, license requirements, and valid JobPosting schema (validThrough, baseSalary, directApply) and push to Google Indexing API",
            "Capture the candidate's email/SMS for recurring daily job-alert arbitrage before routing their application to the highest-bidding CPC/CPA XML feed",
        ],
        "metrics": [
            "Google for Jobs impression-to-application CTR (%)",
            "Average revenue per applicant (CPC + CPA + job-alert co-reg)",
            "Active vs. expired listing hygiene score (100% removal of expired jobs)",
        ],
        "platform_risks": [
            {
                "failure_mode": "Google Structured Data manual action for expired/spammy JobPosting markup",
                "trigger": "Leaving expired jobs live with JobPosting schema, fabricating fake job listings, or failing to call the Indexing API URL_DELETED endpoint on close",
                "impact": "Complete removal of domain from the Google for Jobs widget",
                "detection_metric": "Search Console JobPosting structured-data error count (0 required) and sub-6-hour expired-job purge latency",
                "fallback": "Auto-purge expired XML listings every 4 hours via Indexing API URL_DELETED notifications and retain candidates on owned SMS/email job-alert lists",
            },
        ],
    },
    "domain_drop_catch_backlink_parking_arbitrage": {
        "id": "domain_drop_catch_backlink_parking_arbitrage",
        "track_id": "track_2",
        "name": "Drop-Catch Traffic Parking & Zero-Click Direct-Navigation Arbitrage",
        "mechanism": (
            "Acquire expiring non-trademarked generic and legacy-project domains that still receive thousands "
            "of daily direct-navigation, bookmark, and legacy referral hits, routing the residual HTTP traffic "
            "through contextual zero-click demand feeds or high-converting niche lead-capture landers."
        ),
        "inputs": [
            "Drop-catch & registrar closeout feeds scored by residual DNS query / referral volume",
            "Automated USPTO TESS / WIPO trademark-exclusion filter",
            "Contextual zero-click demand router (Bodis / Tonic / Sedo) + custom vertical lead lander",
        ],
        "workflow": [
            "Screen expiring domains for passive referral traffic from aged blogs, resource directories, and direct type-in navigation—strictly excluding active trademarks",
            "Measure 7-day baseline visitor geo, device, and referring-anchor intent upon acquisition",
            "Route generic commercial traffic to custom 1-step lead/calculator landers (or compliant contextual search feeds) where annualized yield exceeds renewal cost by 5–20x",
        ],
        "metrics": [
            "Annualized net parking/lead revenue vs. $10/yr domain renewal cost",
            "RPM ($15–$120+) by visitor vertical and geography",
            "Portfolio profitable-domain hit rate (%)",
        ],
        "platform_risks": [
            {
                "failure_mode": "Upstream parking-feed termination or UDRP cybersquatting complaint",
                "trigger": "Registering trademarked typo domains or sending bot/datacenter junk traffic into zero-click ad feeds",
                "impact": "Parking account ban, revenue clawback, or $1,500+ UDRP dispute loss",
                "detection_metric": "100% automated USPTO trademark screen before bidding and edge ASN/bot filtering before feed handoff",
                "fallback": "Acquire strictly generic dictionary/descriptive domains, block datacenter bot ASNs at Cloudflare before monetization, and route high-intent domains to owned lead landers",
            },
        ],
    },
    "cloud_ai_startup_credit_aggregation_arbitrage": {
        "id": "cloud_ai_startup_credit_aggregation_arbitrage",
        "track_id": "track_1",
        "name": "Cloud & LLM Startup Credit Grant Aggregation ($50k–$350k Free Compute Arbitrage)",
        "mechanism": "Forming clean Delaware/Wyoming micro-SaaS corporate entities enrolled in verified incubator, venture-partner, or founder-perk directories to unlock non-dilutive cloud and frontier LLM startup credit grants ($25k–$350k across AWS Activate, Azure Founders Hub, GCP for Startups, Cloudflare, OpenAI, and Anthropic), eliminating compute COGS for heavy AI data-extraction, scraping, and B2B SaaS products sold at 90–98% cash margins.",
        "inputs": [
            "Clean corporate entity registrations, domain workspace, and live product landing/application endpoints",
            "Partnerperk/incubator affiliation tiers (Y Combinator Startup School, Stripe Atlas, Mercury Raise, Microsoft for Startups)",
            "Multi-provider LLM and cloud workload router abstracting inference across AWS Bedrock, Azure OpenAI, and GCP Vertex",
        ],
        "workflow": [
            "Provision dedicated vertical micro-SaaS products with live billing, production authentication, and verified corporate domains",
            "Enroll each entity in legitimate startup credit programs to secure $25k–$350k in non-dilutive compute, GPU, and LLM token grants",
            "Route high-volume B2B document parsing, skip-tracing, programmatic content generation, or audio/video transcription workloads across active grant balances",
            "Sell the resulting B2B intelligence, API access, or SaaS subscriptions for hard cash while tracking credit burn and migrating matured workloads to reserved or open-weight self-hosted inference before grant expiration",
        ],
        "metrics": [
            "Approved non-dilutive compute credit balance ($) per operating entity",
            "Effective cash revenue generated per $1.00 of nominal grant compute consumed",
            "Blended gross margin (%) after grant burn and post-grant unit-economics survival rate",
        ],
        "platform_risks": [
            {
                "failure_mode": "Cloud provider startup-program audit or credit revocation for linked shell entities or prohibited token reselling",
                "trigger": "Reusing identical payment cards, billing addresses, or raw API proxy endpoints across multiple entities without a genuine application layer",
                "impact": "Immediate revocation of promotional credits and potential billing-account suspension",
                "detection_metric": "Zero raw API key proxying; 100% application-layer value-add and isolated corporate/banking governance per product",
                "fallback": "Operate genuine standalone vertical SaaS products per entity, never resell raw API keys, and maintain local open-weight (Llama/vLLM/DeepSeek) failover nodes for zero-downtime migration",
            },
        ],
    },
    "free_llc_fintech_bounty_stacking": {
        "id": "free_llc_fintech_bounty_stacking",
        "track_id": "track_1",
        "name": "\"Free LLC / Free Setup\" Fintech Account Co-Registration Bounty Stacking",
        "mechanism": "Offering a $0-service-fee LLC formation and business-launch concierge (borrower pays only mandatory state filing fees) that embeds a sequential post-formation 'Required Business Infrastructure Checklist' where every newly formed entity opens free business banking, corporate card, payroll, bookkeeping, and merchant accounts—yielding $600–$1,800+ in stacked B2B fintech CPA bounties per free formation.",
        "inputs": [
            "High-intent 'free LLC formation' and 'start a business in [State]' search, social, and creator traffic",
            "Automated state SOS filing workflow, EIN retrieval assistant, and operating-agreement generator",
            "Direct B2B partner/CPA agreements with neobank, corporate card, payroll, and registered-agent providers",
        ],
        "workflow": [
            "Acquire first-time founders via a genuine $0-markup LLC formation funnel where the user pays only state statutory fees",
            "Guide the founder through an automated EIN and corporate-resolution wizard immediately upon state filing submission",
            "Present an integrated 1-click onboarding sequence for a free business checking account ($150–$400 CPA), corporate charge card ($200–$500 CPA), payroll/bookkeeping trial ($100–$300 CPA), and web/domain host ($100–$200 CPA)",
            "Provide automated compliance reminders and annual report tracking to capture recurring Year-2 registered-agent renewals",
        ],
        "metrics": [
            "Stacked fintech CPA bounty revenue ($) realized per 100 free LLC formations",
            "Post-EIN bank-account funding conversion rate (%) within 14 days of formation",
            "Net customer acquisition margin after paid search/creator traffic spend",
        ],
        "platform_risks": [
            {
                "failure_mode": "Fintech partner CPA clawback or payout tier downgrade due to unfunded/dormant business bank accounts",
                "trigger": "Sending low-intent formations that open free business bank accounts but never complete KYC or initial deposit funding",
                "impact": "Reversal of unvested CPA bounties or shift from account-open CPA to funded-account CPA tiers",
                "detection_metric": "30-day funded-account activation rate (%) and average initial deposit balance across referred LLCs",
                "fallback": "Gate free operating-agreement and bookkeeping templates behind verified bank-account funding and pre-qualify founders on 30-day operating revenue intent",
            },
        ],
    },
    "free_tier_api_waterfall_multiplexing": {
        "id": "free_tier_api_waterfall_multiplexing",
        "track_id": "track_1",
        "name": "Multi-Provider Free-Tier API Router & B2B Data-Enrichment Reselling",
        "mechanism": "Aggregating 30–60+ distinct B2B data, email-verification, firmographic, DNS, and SERP providers that each offer permanent 'Freemium / Developer Free Tiers' (50–1,000 free lookups/month per provider) behind an intelligent waterfall router with aggressive Postgres caching, selling unified B2B lead enrichment and verification at $99–$499/mo with near-zero upstream API COGS.",
        "inputs": [
            "Catalog of 30–60+ B2B contact, firmographic, WHOIS, technographic, and email-verification APIs with recurring free quotas",
            "Deterministic local Postgres/Redis entity cache indexed by domain, LinkedIn URL, and normalized company name",
            "Quota-aware waterfall routing engine with per-provider rate-limit and credit-reset telemetry",
        ],
        "workflow": [
            "Intercept every incoming B2B enrichment request against the local canonical cache first (eliminating 60–80% of repeat domain/contact lookups at $0 cost)",
            "Route cache misses dynamically across the pool of 30+ upstream providers ordered by remaining monthly free-tier quota and field-level accuracy",
            "Normalize disparate provider JSON responses into a single high-confidence schema with verified SMTP handshakes and confidence scores",
            "Persist every newly resolved record into the proprietary local graph so the dataset compounds daily while upstream API spend remains near zero",
        ],
        "metrics": [
            "Local cache hit rate (%) vs. upstream free-tier quota utilization (%)",
            "Effective upstream API cost per 1,000 enriched B2B records ($)",
            "Proprietary entity-graph growth rate (net new verified records cached per day)",
        ],
        "platform_risks": [
            {
                "failure_mode": "Upstream providers deprecating free developer tiers or tightening rate limits",
                "trigger": "SaaS vendors eliminating free tiers during pricing overhauls or throttling high-concurrency burst requests",
                "impact": "Reduced free lookup capacity requiring fallback to paid wholesale tiers or direct scraping",
                "detection_metric": "Real-time HTTP 429/402 error rate per upstream provider and remaining monthly free-pool runway",
                "fallback": "Maintain 40+ interchangeable upstream adapters, prioritize local graph cache hits, and fall back to direct public-web/DNS/MX extraction when free quotas tighten",
            },
        ],
    },
    "serverless_edge_free_tier_empire_hosting": {
        "id": "serverless_edge_free_tier_empire_hosting",
        "track_id": "track_1",
        "name": "Zero-COGS 1,000-Site Programmatic Hosting on Free Edge Tiers",
        "mechanism": "Deploying hundreds of static programmatic SEO directories, calculators, local-service lead sites, and comparison micro-tools across generous free edge-hosting tiers (Cloudflare Pages/Workers, GitHub Pages, Vercel/Netlify/Supabase free allocations) with pre-rendered static JSON/HTML bundles so hosting, bandwidth, and SSL cost $0.00/mo per property.",
        "inputs": [
            "Static-site generator pipeline (Astro/Eleventy/Next static export) compiling SQLite/Parquet datasets into zero-runtime HTML/JSON",
            "Cloudflare Pages / Workers and GitHub Pages CI/CD deployment matrices",
            "Portfolio of $8–$10/yr exact-match or niche utility domains",
        ],
        "workflow": [
            "Compile structured public datasets (licensing tables, fee calculators, local directory listings, compatibility matrices) into ultra-fast static HTML pages at build time",
            "Deploy each domain property to free edge-CDN tiers with zero origin servers, zero database idle compute costs, and 100/100 Core Web Vitals",
            "Route dynamic lead capture and webhook submissions through lightweight edge functions to a single centralized CRM/Postgres backend",
            "Monetize across the portfolio via display ad networks, pay-per-call dynamic numbers, and B2B lead routing with ~99% infrastructure margin",
        ],
        "metrics": [
            "Total monthly hosting and bandwidth COGS ($) across 100–1,000 live domains",
            "Portfolio-wide organic sessions and lead/ad RPM per $10/yr domain renewal",
            "Build-to-edge deployment time (seconds) and Core Web Vitals pass rate (%)",
        ],
        "platform_risks": [
            {
                "failure_mode": "Edge platform build-minute exhaustion or commercial-use limit enforcement on free tiers",
                "trigger": "Triggering thousands of redundant cloud CI builds per day or exceeding free Worker invocation quotas",
                "impact": "Paused deployments or forced upgrade to $20/mo paid plans",
                "detection_metric": "Daily CI build minutes consumed and edge function invocation count vs. static asset cache-hit ratio",
                "fallback": "Pre-build static HTML bundles locally or on self-hosted runners and upload pre-compiled artifacts directly via API so cloud build-minute usage stays near zero",
            },
        ],
    },
    "free_trial_concierge_cpa_arbitrage": {
        "id": "free_trial_concierge_cpa_arbitrage",
        "track_id": "track_2",
        "name": "\"Done-For-You Free Setup\" Concierge Funded by Free-Trial CPA Bounties",
        "mechanism": "Advertising a 100% free 'Done-For-You Store / Funnel / CRM / Website Setup' service where the sole prerequisite is that the client registers for 3–5 required software tools (Shopify, Webflow, GoHighLevel, Semrush, hosting, or email platforms) via the operator's affiliate links—collecting $300–$800+ in stacked CPA bounties triggered on free-trial or $1-first-month activations while an automated template script provisions the build in 90 seconds.",
        "inputs": [
            "1-click cloneable snapshots/templates (GoHighLevel snapshots, Shopify theme bundles, WordPress/Astro starter kits)",
            "High-CPA SaaS affiliate programs paying $100–$300+ per trial activation or initial $1 promotional month",
            "Automated onboarding portal verifying affiliate sub-ID (`subid`) conversion tracking before triggering provisioning",
        ],
        "workflow": [
            "Run high-converting social and search offers for a '100% Free Done-For-You Agency/Store/CRM Setup ($1,500 Value — $0 Today)'",
            "Direct applicants through a 3-step self-serve onboarding wizard requiring free-trial or $1-tier registration across the core software stack via tracked partner links",
            "Verify the affiliate postback fire via webhook, then automatically import the pre-built industry snapshot, templates, and automations into the user's new account",
            "Upsell optional monthly management retainers or premium lead packages to the newly onboarded user base",
        ],
        "metrics": [
            "Stacked CPA bounty revenue ($) per completed free setup",
            "Automated provisioning time (minutes) and support cost ($) per onboarded user",
            "Trial-to-paid Day-30 retention rate (%) across referred software accounts",
        ],
        "platform_risks": [
            {
                "failure_mode": "Affiliate network suspension or CPA holdback due to low trial-to-paid retention",
                "trigger": "Referring freebie-seekers who cancel all software trials before Day 14/30 billing",
                "impact": "Affiliate account termination or migration from trial-CPA to 60-day rev-share",
                "detection_metric": "Day-30 and Day-60 paid retention rate (%) per traffic source and partner program",
                "fallback": "Qualify applicants on active business status, embed sticky daily-use workflows (live phone numbers, domain DNS, CRM pipelines) into the free setup, and blend CPA offers with 30–40% recurring rev-share programs",
            },
        ],
    },
    "sportsbook_promo_ev_matched_betting_syndicates": {
        "id": "sportsbook_promo_ev_matched_betting_syndicates",
        "track_id": "track_2",
        "name": "Regulated Sportsbook & Sweepstakes Sign-Up Promo Conversion (Player-2 Arbitrage)",
        "mechanism": "Operating a mathematical promo-conversion platform and 'Player-2' split-profit syndicate that extracts $3,000–$8,000+ in guaranteed risk-free cash per newly legalized state resident by hedging free-bet sign-up bonuses, deposit matches, and daily odds boosts across 15–25 regulated sportsbooks and sweepstakes platforms at 70–85% deterministic conversion rates.",
        "inputs": [
            "Real-time sub-second odds-screen API ingesting mainlines and alternate lines across 20+ regulated books and prediction exchanges",
            "Deterministic Free-Bet Conversion (SNR — Stake Not Returned) and Dutch-hedging calculator",
            "State-by-state regulatory launch calendar and referral/concierge onboarding contracts",
        ],
        "workflow": [
            "Onboard verified adults in newly legalized or active states into a guided promo-conversion software suite or split-profit concierge walkthrough",
            "Claim all available 'Bet $5 Get $200' and '$1,000 First-Bet Reset' sign-up promotions across every licensed operator in that jurisdiction",
            "Execute simultaneous offsetting positions on a secondary book or exchange where mathematical conversion locks in 70–85% of the promotional face value regardless of game outcome",
            "Transition post-signup accounts into daily +EV odds-boost and sweepstakes daily-login bonus harvesting until operator stake-limiting occurs",
        ],
        "metrics": [
            "Net risk-free cash extracted ($) per full state book rotation",
            "Promo-to-cash conversion efficiency (%) across SNR and reset bonuses",
            "Account longevity (days before stake-limiting) and software/syndicate split revenue ($)",
        ],
        "platform_risks": [
            {
                "failure_mode": "Sportsbook promo-ban ('gubbing'), stake limiting, or multi-accounting confiscation",
                "trigger": "Logging into multiple individuals' accounts from shared devices/IPs or betting obscure illiquid alternate lines that trigger trader alerts",
                "impact": "Loss of future promotional eligibility or frozen account balances under KYC review",
                "detection_metric": "Maximum allowed stake size on mainline markets and 100% 1-person-1-device-1-residential-IP compliance",
                "fallback": "Enforce strict client-side execution where each participant operates exclusively on their own personal mobile device and cellular connection, sticking to high-liquidity mainlines",
            },
        ],
    },
    "aged_high_karma_social_account_brokerage": {
        "id": "aged_high_karma_social_account_brokerage",
        "track_id": "track_2",
        "name": "Aged / High-Trust Social Account Farming, Leasing & SERP Seeding (Reddit, LinkedIn, X)",
        "mechanism": "Programmatically warming and aging hundreds of 'free' accounts on high-authority social platforms (Reddit accounts with 5,000+ organic comment karma and 2+ year age, aged LinkedIn profiles, verified X/TikTok creator accounts) on isolated mobile-proxy fingerprints so their posts bypass new-account spam filters and rank immediately on Google SERPs and LLM citations.",
        "inputs": [
            "Anti-detect browser profiles paired 1:1 with dedicated 4G/5G mobile or sticky residential proxies",
            "Topic-specific warming schedules posting natural non-promotional commentary in hobby, city, and industry communities",
            "Subreddit CQS (Contributor Quality Score) and shadowban monitoring telemetry",
        ],
        "workflow": [
            "Provision or acquire aged baseline accounts and assign each a permanent fingerprint, residential ISP locale, and topical persona",
            "Maintain a 95:5 organic-to-promotional contribution ratio so accounts achieve 'High/Highest' Contributor Quality Scores (CQS) and moderator whitelist status",
            "Deploy the high-trust accounts to seed brand recommendations inside Google-ranking threads or lease aged seats for B2B LinkedIn outbound campaigns",
            "Monitor post survival and SERP/LLM citation velocity in real time, rotating accounts into cooldown cycles after any commercial mention",
        ],
        "metrics": [
            "30-day comment/post survival rate (%) on strict auto-moderated communities",
            "Account Contributor Quality Score (CQS) distribution across the fleet",
            "Monthly revenue per aged seat leased ($150–$400/mo) or per surviving SERP citation ($50–$250)",
        ],
        "platform_risks": [
            {
                "failure_mode": "Batch shadowbanning or behavioral graph cluster detection",
                "trigger": "Upvoting the same target URLs from multiple fleet accounts or reusing subnet/browser-canvas signatures",
                "impact": "Simultaneous loss of aged account inventory and removal of historical comments",
                "detection_metric": "Zero cross-account vote ring activity and daily public-incognito visibility verification",
                "fallback": "Enforce strict zero-cross-interaction rules between fleet accounts, isolate every persona on dedicated cellular proxies, and never link raw affiliate URLs directly",
            },
        ],
    },
    "platform_privilege_tier_account_arbitrage": {
        "id": "platform_privilege_tier_account_arbitrage",
        "track_id": "track_2",
        "name": "High-Tier \"Local Guide / Autoconfirmed Editor / Top Hunter\" Authority Account Arbitrage",
        "mechanism": "Cultivating free user accounts into high-privilege algorithmic trust tiers—such as Google Local Guides (Level 6–10), Wikipedia Autoconfirmed/Extended-Confirmed editors, Product Hunt top hunters, and G2/Capterra/Trustpilot verified reviewers—whose edits, map suggest-an-edit actions, category changes, and launches carry massive algorithmic weight and sell for high-ticket B2B retainers.",
        "inputs": [
            "Geo-matched Google Local Guide (Level 6+), aged Wikipedia, and aged Product Hunt / software-review accounts",
            "Location-consistent EXIF metadata, mobile device telemetry, and verifiable third-party citation dossiers",
            "B2B local-SEO, knowledge-graph, and SaaS launch client demand",
        ],
        "workflow": [
            "Build sustained, legitimate contribution histories across local maps, encyclopedia entries, and software ecosystems to unlock elevated platform trust tiers",
            "Use high-tier Local Guide accounts to submit rapid-approval GBP spam-name redressals, competitor duplicate merges, and category corrections for local-service clients",
            "Execute policy-compliant, source-backed knowledge-graph updates and high-visibility Product Hunt/directory launches for B2B SaaS brands",
            "Package these high-trust authority interventions as premium reputation, entity-SEO, and launch-management retainers ($2,500–$10,000/mo)",
        ],
        "metrics": [
            "Platform edit/suggestion auto-approval rate (%) and time-to-live publication",
            "Client local-pack rank lift or knowledge-panel entity resolution rate (%)",
            "Retainer revenue per managed authority campaign ($)",
        ],
        "platform_risks": [
            {
                "failure_mode": "Privilege-tier badge revocation or undisclosed paid-editing enforcement",
                "trigger": "Submitting biased, unsourced promotional edits or executing bulk map edits outside the account's natural geographic radius",
                "impact": "Demotion of account trust score and rollback of historical edits",
                "detection_metric": "Edit acceptance/revert ratio (%) and strict geographic/topical consistency per account",
                "fallback": "Submit only factually verifiable, secondary-source-backed edits and keep Local Guide accounts strictly locked to their native metropolitan areas",
            },
        ],
    },
    "multi_inbox_free_workspace_outbound_clusters": {
        "id": "multi_inbox_free_workspace_outbound_clusters",
        "track_id": "track_2",
        "name": "Subsidized / Developer-Tenant Multi-Inbox Cold Outbound Infrastructure",
        "mechanism": "Provisioning hundreds of isolated secondary domains across subsidized Microsoft 365 developer/partner tenants, Cloudflare Email Routing, and low-cost SMTP relays—sending strictly 15–25 plain-text emails per inbox per day across 300+ free/subsidized mailboxes to deliver 150,000+ monthly B2B cold emails into primary inboxes without paying $6–$12/seat retail Google Workspace pricing.",
        "inputs": [
            "Lookalike secondary domain portfolio with automated SPF, DKIM (2048-bit), DMARC (`p=quarantine`/`reject`), and custom tracking-free MX records",
            "Subsidized M365 partner/developer tenants, Cloudflare Email Routing catch-alls, and distributed SMTP sending nodes",
            "Automated peer-to-peer warmup network and master unibox reply-routing webhook",
        ],
        "workflow": [
            "Provision 100–300 secondary sending domains and bind 2–3 mailboxes per domain via automated DNS and tenant scripts",
            "Warm every mailbox for 14–21 days with realistic thread-depth conversations before introducing live outbound prospects",
            "Cap daily outbound volume at <=20 zero-link, zero-tracking-pixel plain-text messages per mailbox per day to stay completely beneath ESP volume heuristics",
            "Aggregate all prospect replies into a single unified AI-triaged inbox that books qualified B2B sales calls on pay-per-show or retainer terms",
        ],
        "metrics": [
            "Primary-inbox placement rate (%) across Gmail and Microsoft 365 seed tests",
            "All-in monthly infrastructure cost per 10,000 delivered plain-text emails ($)",
            "Positive reply rate (%) and booked meetings per 1,000 prospects contacted",
        ],
        "platform_risks": [
            {
                "failure_mode": "Tenant-wide outbound throttling or domain-footprint blacklisting (Spamhaus DBL)",
                "trigger": "Placing too many domains inside a single tenant, embedding tracking pixels, or exceeding 30 sends/day per mailbox",
                "impact": "Tenant suspension or domain-level spam-folder routing",
                "detection_metric": "Daily seed-list inbox placement (%) and bounce rate (<1.5% hard threshold)",
                "fallback": "Enforce max 2–3 domains per tenant, strip all open/click tracking pixels, verify 100% of leads via SMTP catch-all checks before sending, and keep hot-standby warmed domains ready for instant swap",
            },
        ],
    },
    "verified_fan_ticketing_and_drop_allocation_farming": {
        "id": "verified_fan_ticketing_and_drop_allocation_farming",
        "track_id": "track_2",
        "name": "Multi-Account Presale Code & Limited-Mintage Allocation Arbitrage",
        "mechanism": "Operating hundreds of aged, human-scored 'free' fan-club, ticketing (Ticketmaster Verified Fan / AXS), U.S. Mint, and limited-edition luxury/collectible accounts—each backed by unique residential proxies, aged browser profiles, and virtual card numbers (VCCs)—to multiply lottery/queue odds by 100x–500x on strict 'limit 1–4 per account' releases trading at instant 50–300% secondary-market premiums.",
        "inputs": [
            "Aged ticketing, fan-club, and sovereign-mint account fleet with clean purchase histories",
            "Anti-detect browser matrix with residential ISP proxies and unique SIM/SMS verification lines",
            "Corporate virtual credit card (VCC) issuance API (Extend/Ramp/Slash) with distinct billing descriptors",
        ],
        "workflow": [
            "Monitor upcoming concert tours, playoff games, U.S. Mint numismatic releases, and limited collectible drops with secondary-market spreads >=50%",
            "Register the aged account fleet across presale lotteries and waiting rooms to secure high-priority access codes and low queue positions",
            "Execute checkouts strictly on high-margin allocations (front-row/pit seats, low-mintage proof coins) using isolated VCCs per household profile",
            "Flip allocations immediately via direct consignment, verified ticket exchanges (StubHub/SeatGeek/Vivid API), or pre-committed wholesale buyers",
        ],
        "metrics": [
            "Presale code / top-1,000 queue-position hit rate (%) across the account cluster",
            "Net realized secondary-market spread (%) after exchange/consignment fees",
            "Inventory hold time (hours/days from checkout to settled resale payout)",
        ],
        "platform_risks": [
            {
                "failure_mode": "Order cancellation or queue-score penalty from device/payment fingerprint linkage",
                "trigger": "Reusing identical billing addresses, card BINs, or browser WebGL/Canvas fingerprints across Household-Limit-restricted drops",
                "impact": "Canceled orders, revoked presale codes, or permanent account flagging",
                "detection_metric": "Post-checkout order survival rate (%) and queue-score tier telemetry",
                "fallback": "Maintain genuine distributed buyer consortiums with unique residential addresses, distinct bank BINs, and pre-sold wholesale buyer commitments before checkout",
            },
        ],
    },
    "airdrop_points_sybil_cluster_farming": {
        "id": "airdrop_points_sybil_cluster_farming",
        "track_id": "track_2",
        "name": "Web3 Testnet, Points-Program & Free-Quest Multi-Account Farming",
        "mechanism": "Orchestrating 200–2,000+ isolated 'free' wallets and social-quest profiles (Galxe, Zealy, Layer3, L1/L2 testnets, DePIN browser nodes) that execute randomized, non-correlated on-chain and social interactions so that when VC-backed protocols distribute 'fair-launch' token airdrops ($500–$5,000+ per eligible user), the operator captures 200–2,000x the retail allocation at near-zero capital cost.",
        "inputs": [
            "Non-correlated wallet cluster funded strictly via isolated CEX sub-account withdrawal addresses (zero wallet-to-wallet transfers)",
            "Randomized scheduling engine executing variable-time, variable-amount testnet swaps, bridge interactions, and governance votes",
            "Matched aged Discord/X/GitHub identity profiles per wallet with unique residential proxy bindings",
        ],
        "workflow": [
            "Target heavily funded ($20M–$100M+ VC raised) pre-token protocols running zero-cost testnets, points programs, or idle-bandwidth browser extensions",
            "Fund and initialize isolated wallet cohorts through CEX sub-accounts so no on-chain funding graph connects any two wallets in the fleet",
            "Run Gaussian-jittered interaction schedules across 3–6 months that mirror organic power-user behavior (distinct contract sequences, days of week, and payload sizes)",
            "Claim and liquidate token allocations at Token Generation Event (TGE) via isolated CEX deposit addresses",
        ],
        "metrics": [
            "Sybil-filter survival rate (% of fleet wallets qualifying at snapshot)",
            "Total TGE token payout ($) vs. total proxy/gas/infra cost ($)",
            "Pairwise on-chain graph correlation score (target: 0.00)",
        ],
        "platform_risks": [
            {
                "failure_mode": "Snapshot Sybil-clustering disqualification or proof-of-humanity gate",
                "trigger": "Funding wallets from a shared master address, executing identical contract call sequences within the same block window, or mandatory biometric KYC at claim",
                "impact": "Exclusion of flagged wallet clusters from token distribution",
                "detection_metric": "Pre-snapshot graph clustering simulation against Nansen/Arbitrum/LayerZero Sybil heuristics",
                "fallback": "Enforce strict CEX-only funding/withdrawal isolation, randomize contract paths and timestamps per wallet, and prioritize high-trust Gitcoin Passport / aged-GitHub weighted allocations",
            },
        ],
    },
    "parasitic_free_publishing_account_serp_monopoly": {
        "id": "parasitic_free_publishing_account_serp_monopoly",
        "track_id": "track_2",
        "name": "Mass Free-Account Authority Host Seeding (Medium, Substack, LinkedIn, GitHub, Notion)",
        "mechanism": "Creating dozens of free publication accounts across DR 90+ UGC platforms (Medium, Substack, LinkedIn Articles, GitHub Pages/Gists, Notion public sites, Hashnode, Dev.to, Google Sites) and cross-publishing interlinked buyer-intent comparison matrices so a single operator occupies 5 to 8 of the 10 Page-1 Google SERP slots for high-commission commercial keywords with $0 hosting or domain cost.",
        "inputs": [
            "Aged free publisher accounts across 8–10 DR 90+ authority platforms",
            "Low-competition, high-CPA commercial keyword matrix ('[SaaS A] vs [SaaS B]', '[Vendor] pricing breakdown', 'best [niche] software for [vertical]')",
            "Multi-platform canonical/syndication publisher and owned redirect bridge links",
        ],
        "workflow": [
            "Identify commercial-intent long-tail SERPs where Google ranks third-party UGC hosts above small independent domains",
            "Publish distinct, structurally differentiated deep-dive analyses of the same keyword across Medium, LinkedIn Pulse, Substack, Notion, and GitHub Pages simultaneously",
            "Interlink the properties in a directed acyclic hub-and-spoke topology pointing authority and click-through traffic to a central comparison lander",
            "Swap affiliate destination offers dynamically at the redirect bridge whenever a vendor increases CPA payouts",
        ],
        "metrics": [
            "Number of Page-1 SERP slots simultaneously occupied per target keyword (target: 3–6 of top 10)",
            "Time-to-index and time-to-top-3 ranking (hours/days)",
            "Aggregate affiliate/lead revenue ($) per multi-host keyword cluster",
        ],
        "platform_risks": [
            {
                "failure_mode": "UGC host account suspension or Google site-reputation noindex tightening",
                "trigger": "Publishing identical spun copy across hosts or embedding raw affiliate network links disallowed by platform terms",
                "impact": "Account takedown or de-indexing of a single host spoke while remaining hosts stay live",
                "detection_metric": "Per-host indexation ratio (%) and SERP pixel share across the 8-platform portfolio",
                "fallback": "Generate genuinely distinct format angles per platform (code benchmarks on GitHub, executive breakdown on LinkedIn, newsletter deep-dive on Substack) and route all CTAs through clean owned bridge domains",
            },
        ],
    },
}

CANDIDATE_PLAY_MAP: dict[int, tuple[str, ...]] = {
    1: (
        "public_record_api_intelligence",
        "unclaimed_property_escheatment_arbitrage",
        "probate_docket_inheritance_arbitrage",
    ),
    2: (
        "public_record_api_intelligence",
        "distressed_asset_recovery",
        "unclaimed_property_escheatment_arbitrage",
        "probate_docket_inheritance_arbitrage",
        "property_tax_assessment_appeal_contingency",
    ),
    4: (
        "public_record_api_intelligence",
        "ego_bait_directory_badge_arbitrage",
        "government_rfp_subcontractor_brokerage",
    ),
    5: (
        "public_record_api_intelligence",
        "distressed_asset_recovery",
        "b2b_class_action_contingency_recovery",
        "unclaimed_property_escheatment_arbitrage",
        "freight_detention_audit_contingency",
        "hospital_lien_medical_receivables_arbitrage",
        "property_tax_assessment_appeal_contingency",
    ),
    8: (
        "public_record_api_intelligence",
        "distressed_asset_recovery",
        "b2b_class_action_contingency_recovery",
        "arizona_abs_mass_tort_cocounsel",
        "unclaimed_property_escheatment_arbitrage",
        "ucc1_expiration_refi_trigger_arbitrage",
        "hospital_lien_medical_receivables_arbitrage",
    ),
    9: (
        "public_record_api_intelligence",
        "public_filing_trigger_mail_arbitrage",
        "rank_and_rent_pay_per_call_routing",
        "identity_graph_pixel_arbitrage",
        "probate_docket_inheritance_arbitrage",
        "municipal_code_violation_trigger_arbitrage",
        "property_tax_assessment_appeal_contingency",
        "google_maps_gbp_lead_gen_network",
    ),
    11: (
        "telegram_channel_signal_scraping",
        "ego_bait_directory_badge_arbitrage",
        "fmcsa_dot_inspection_trigger_arbitrage",
    ),
    12: (
        "public_filing_trigger_mail_arbitrage",
        "ego_bait_directory_badge_arbitrage",
        "freight_detention_audit_contingency",
        "fmcsa_dot_inspection_trigger_arbitrage",
    ),
    13: (
        "distressed_asset_recovery",
        "expired_chrome_extension_acquisitions",
    ),
    15: (
        "rank_and_rent_pay_per_call_routing",
        "municipal_code_violation_trigger_arbitrage",
        "google_maps_gbp_lead_gen_network",
    ),
    16: (
        "expired_domain_traffic_arbitrage",
        "newly_registered_domain_trigger_arbitrage",
        "typo_squatting_brand_bid_hijacking",
        "expired_podcast_rss_redirect_arbitrage",
        "domain_drop_catch_backlink_parking_arbitrage",
        "serverless_edge_free_tier_empire_hosting",
    ),
    17: (
        "distressed_asset_recovery",
        "government_rfp_subcontractor_brokerage",
        "verified_fan_ticketing_and_drop_allocation_farming",
    ),
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
        "municipal_code_violation_trigger_arbitrage",
        "freight_detention_audit_contingency",
        "ucc1_expiration_refi_trigger_arbitrage",
        "fmcsa_dot_inspection_trigger_arbitrage",
        "ad_library_spend_velocity_arbitrage",
        "saas_technographic_churn_pixel_scraping",
        "sec_edgar_8k_vendor_trigger_arbitrage",
        "patent_trademark_office_action_arbitrage",
        "review_gating_reputation_extortion_funnels",
        "government_rfp_subcontractor_brokerage",
        "amazon_asin_hijack_brand_protection_trigger",
        "property_tax_assessment_appeal_contingency",
        "ssl_ada_wcag_compliance_scanner_outbound",
        "reddit_quora_aged_thread_injection",
        "google_maps_gbp_lead_gen_network",
        "llm_citation_geo_poisoning",
        "newsletter_co_reg_sparkloop_arbitrage",
        "job_board_xml_feed_programmatic_arbitrage",
        "cloud_ai_startup_credit_aggregation_arbitrage",
        "free_llc_fintech_bounty_stacking",
        "free_tier_api_waterfall_multiplexing",
        "serverless_edge_free_tier_empire_hosting",
        "free_trial_concierge_cpa_arbitrage",
        "aged_high_karma_social_account_brokerage",
        "platform_privilege_tier_account_arbitrage",
        "multi_inbox_free_workspace_outbound_clusters",
        "parasitic_free_publishing_account_serp_monopoly",
    ),
    19: (
        "patent_trademark_office_action_arbitrage",
        "amazon_asin_hijack_brand_protection_trigger",
    ),
    20: (
        "public_filing_trigger_mail_arbitrage",
        "b2b_class_action_contingency_recovery",
        "arizona_abs_mass_tort_cocounsel",
        "identity_graph_pixel_arbitrage",
        "freight_detention_audit_contingency",
        "ucc1_expiration_refi_trigger_arbitrage",
        "fmcsa_dot_inspection_trigger_arbitrage",
        "sec_edgar_8k_vendor_trigger_arbitrage",
        "hospital_lien_medical_receivables_arbitrage",
        "free_llc_fintech_bounty_stacking",
    ),
    21: (
        "public_filing_trigger_mail_arbitrage",
        "arizona_abs_mass_tort_cocounsel",
        "telegram_channel_signal_scraping",
        "rank_and_rent_pay_per_call_routing",
        "social_to_search_ping_post_arbitrage",
        "high_velocity_dm_outbound_systems",
        "identity_graph_pixel_arbitrage",
        "municipal_code_violation_trigger_arbitrage",
        "ucc1_expiration_refi_trigger_arbitrage",
        "saas_technographic_churn_pixel_scraping",
        "sec_edgar_8k_vendor_trigger_arbitrage",
        "patent_trademark_office_action_arbitrage",
        "government_rfp_subcontractor_brokerage",
        "google_maps_gbp_lead_gen_network",
        "free_tier_api_waterfall_multiplexing",
        "aged_high_karma_social_account_brokerage",
        "platform_privilege_tier_account_arbitrage",
        "multi_inbox_free_workspace_outbound_clusters",
    ),
    22: (
        "public_record_api_intelligence",
        "competitor_intent_comparison_hijacking",
        "chrome_extension_contextual_arbitrage",
        "viral_distribution_loops",
        "identity_graph_pixel_arbitrage",
        "saas_technographic_churn_pixel_scraping",
        "review_gating_reputation_extortion_funnels",
        "ssl_ada_wcag_compliance_scanner_outbound",
        "reddit_quora_aged_thread_injection",
        "expired_chrome_extension_acquisitions",
        "llm_citation_geo_poisoning",
        "youtube_faceless_high_cpc_compilation_arbitrage",
        "cloud_ai_startup_credit_aggregation_arbitrage",
        "free_tier_api_waterfall_multiplexing",
        "serverless_edge_free_tier_empire_hosting",
        "sportsbook_promo_ev_matched_betting_syndicates",
        "platform_privilege_tier_account_arbitrage",
        "airdrop_points_sybil_cluster_farming",
    ),
    23: (
        "saas_technographic_churn_pixel_scraping",
        "sec_edgar_8k_vendor_trigger_arbitrage",
        "multi_inbox_free_workspace_outbound_clusters",
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
        "ad_library_spend_velocity_arbitrage",
        "typo_squatting_brand_bid_hijacking",
        "reddit_quora_aged_thread_injection",
        "expired_chrome_extension_acquisitions",
        "llm_citation_geo_poisoning",
        "youtube_faceless_high_cpc_compilation_arbitrage",
        "newsletter_co_reg_sparkloop_arbitrage",
        "expired_podcast_rss_redirect_arbitrage",
        "coupon_checkout_tab_under_injection",
        "pinterest_flipboard_visual_serp_arbitrage",
        "job_board_xml_feed_programmatic_arbitrage",
        "domain_drop_catch_backlink_parking_arbitrage",
        "free_llc_fintech_bounty_stacking",
        "serverless_edge_free_tier_empire_hosting",
        "free_trial_concierge_cpa_arbitrage",
        "sportsbook_promo_ev_matched_betting_syndicates",
        "aged_high_karma_social_account_brokerage",
        "parasitic_free_publishing_account_serp_monopoly",
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
        "ad_library_spend_velocity_arbitrage",
        "typo_squatting_brand_bid_hijacking",
        "reddit_quora_aged_thread_injection",
        "google_maps_gbp_lead_gen_network",
        "llm_citation_geo_poisoning",
        "youtube_faceless_high_cpc_compilation_arbitrage",
        "newsletter_co_reg_sparkloop_arbitrage",
        "expired_podcast_rss_redirect_arbitrage",
        "coupon_checkout_tab_under_injection",
        "pinterest_flipboard_visual_serp_arbitrage",
        "job_board_xml_feed_programmatic_arbitrage",
        "domain_drop_catch_backlink_parking_arbitrage",
        "serverless_edge_free_tier_empire_hosting",
        "free_trial_concierge_cpa_arbitrage",
        "aged_high_karma_social_account_brokerage",
        "platform_privilege_tier_account_arbitrage",
        "parasitic_free_publishing_account_serp_monopoly",
    ),
    26: (
        "arizona_abs_mass_tort_cocounsel",
        "telegram_channel_signal_scraping",
        "ego_bait_directory_badge_arbitrage",
        "high_velocity_dm_outbound_systems",
        "identity_graph_pixel_arbitrage",
        "ucc1_expiration_refi_trigger_arbitrage",
        "sec_edgar_8k_vendor_trigger_arbitrage",
        "aged_high_karma_social_account_brokerage",
        "verified_fan_ticketing_and_drop_allocation_farming",
    ),
    27: (
        "public_filing_trigger_mail_arbitrage",
        "chrome_extension_contextual_arbitrage",
        "viral_distribution_loops",
        "high_velocity_dm_outbound_systems",
        "identity_graph_pixel_arbitrage",
        "ad_library_spend_velocity_arbitrage",
        "reddit_quora_aged_thread_injection",
        "expired_chrome_extension_acquisitions",
        "llm_citation_geo_poisoning",
        "youtube_faceless_high_cpc_compilation_arbitrage",
        "newsletter_co_reg_sparkloop_arbitrage",
        "expired_podcast_rss_redirect_arbitrage",
        "pinterest_flipboard_visual_serp_arbitrage",
        "cloud_ai_startup_credit_aggregation_arbitrage",
        "free_llc_fintech_bounty_stacking",
        "serverless_edge_free_tier_empire_hosting",
        "free_trial_concierge_cpa_arbitrage",
        "sportsbook_promo_ev_matched_betting_syndicates",
        "verified_fan_ticketing_and_drop_allocation_farming",
        "airdrop_points_sybil_cluster_farming",
        "parasitic_free_publishing_account_serp_monopoly",
    ),
    28: (
        "chrome_extension_contextual_arbitrage",
        "viral_distribution_loops",
        "identity_graph_pixel_arbitrage",
        "freight_detention_audit_contingency",
        "ad_library_spend_velocity_arbitrage",
        "amazon_asin_hijack_brand_protection_trigger",
        "ssl_ada_wcag_compliance_scanner_outbound",
        "expired_chrome_extension_acquisitions",
        "coupon_checkout_tab_under_injection",
        "pinterest_flipboard_visual_serp_arbitrage",
        "free_trial_concierge_cpa_arbitrage",
        "verified_fan_ticketing_and_drop_allocation_farming",
    ),
    29: (
        "newly_registered_domain_trigger_arbitrage",
        "telegram_channel_signal_scraping",
        "competitor_intent_comparison_hijacking",
        "high_velocity_dm_outbound_systems",
        "identity_graph_pixel_arbitrage",
        "saas_technographic_churn_pixel_scraping",
        "sec_edgar_8k_vendor_trigger_arbitrage",
        "patent_trademark_office_action_arbitrage",
        "review_gating_reputation_extortion_funnels",
        "amazon_asin_hijack_brand_protection_trigger",
        "ssl_ada_wcag_compliance_scanner_outbound",
        "llm_citation_geo_poisoning",
        "cloud_ai_startup_credit_aggregation_arbitrage",
        "free_tier_api_waterfall_multiplexing",
        "free_trial_concierge_cpa_arbitrage",
        "aged_high_karma_social_account_brokerage",
        "platform_privilege_tier_account_arbitrage",
        "multi_inbox_free_workspace_outbound_clusters",
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
