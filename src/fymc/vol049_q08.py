from __future__ import annotations

CHAPTER_8 = {
    "id": "Q8",
    "chapter_id": "Q8",
    "chapter_number": 8,
    "question_number": 8,
    "slug": "public-records-apis-data-pipelines-operator-tooling",
    "question_prompt": "Which exact public registries, government databases, commercial APIs, enrichment waterfalls, and diagnostic tools give a small regulated prediction-market terminals & licensed igaming affiliates desk an unfair information edge?",
    "kicker": "Q8 / THE BIG MONEY PLAYBOOKS",
    "title": "Public Records, APIs, Data Pipelines & Operator Tooling",
    "subtitle": "CFTC and NFA Records, State Gaming Registers, Permissioned Market Feeds, and Auditable CPA/NGR Attribution",
    "layout_template": "resource_directory",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #49, Regulated Prediction-Market Terminals & Licensed iGaming "
        "Affiliates, ranks #18 of 49 with a 91/100 score. This chapter maps 12 "
        "operator plays onto an eighteen-source directory spanning CFTC records, "
        "state gaming registers, permissioned market feeds, attribution systems, "
        "and diagnostic tools. The edge comes from matching contract rules, "
        "license scope, quote freshness, and payable commission evidence before "
        "publishing a comparison or buying traffic. Keep subscription and permitted "
        "builder revenue separate from licensed affiliate CPA and NGR earnings. "
        "The scorecard produces annual owner profits of $19,500 Conservative, "
        "$137,750 Base, and $325,000 Scaled. Build source provenance, replayable "
        "events, and deduction-aware settlement first; add faster alerts only "
        "where access rights and measured retention justify their cost."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$75,000",
            "context": "Annual operator revenue; excludes customer deposits and trading volume",
            "note": "26% net margin; $19,500 annual owner net profit; 1 FT + 2 C",
        },
        {
            "label": "Base",
            "value": "$362,500",
            "context": "Annual operator revenue; affiliate commissions measured after contractual deductions",
            "note": "38.0% net margin; $137,750 annual owner net profit; 1 FT + 2 C",
        },
        {
            "label": "Scaled",
            "value": "$650,000",
            "context": "Annual operator revenue; excludes sportsbook handle and merchant proceeds",
            "note": "50% net margin; $325,000 annual owner net profit; 2 FT + 3 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Establish the legal entity, product, territory, and permission graph",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Start with a permission graph, not a list of attractive odds. "
                    "Represent every destination as a legal entity, consumer brand, "
                    "approved domain, product class, territory, registration category, "
                    "effective date, and evidence URL. The CFTC designated contract "
                    "market list establishes exchange status; NFA BASIC helps check "
                    "registrant identities and disciplinary history. Neither establishes "
                    "that your particular referral arrangement is permitted. Read the "
                    "exchange agreement and compare actual conduct with the introducing "
                    "broker and futures commission merchant definitions in 7 U.S.C. "
                    "1a and 17 CFR 1.3. Never accept customer funds, pool capital, "
                    "collect brokerage credentials, or transmit orders through an "
                    "analytics product without separately resolving the applicable "
                    "registration framework. A paid publisher also needs a documented "
                    "assessment of commodity trading adviser rules; a publication "
                    "label alone does not settle the question. Assign one evidence "
                    "owner and one backup for each destination. Capture the official "
                    "page, retrieval time, effective date, and a SHA-256 digest. "
                    "A dated screenshot supports a review trail but cannot replace "
                    "the operative order or license record. Recheck before activating "
                    "a destination and whenever an official notice changes its scope."
                ),
                (
                    "Build a separate state gaming graph because a CFTC exchange "
                    "record says nothing about sportsbook affiliate permissions. "
                    "Consult New Jersey DGE, Pennsylvania PGCB, Michigan MGCB, and "
                    "West Virginia Lottery records for the operator, approved brand, "
                    "and relevant supplier or vendor treatment. Determine your own "
                    "registration obligations from the compensation arrangement and "
                    "activities rather than assuming every publisher uses one category. "
                    "For Ontario, reconcile AGCO registration with iGaming Ontario's "
                    "operator directory; Ontario is a separate jurisdiction, not an "
                    "extension of a United States license. This chapter adopts a "
                    "21+ affiliate publishing floor even where the local minimum "
                    "differs, including Ontario's 19+ threshold. Apply destination "
                    "eligibility before presenting outbound promotional links, and "
                    "use jurisdiction-specific responsible-gaming resources. IP location "
                    "is an imperfect publishing filter, not a replacement for the "
                    "operator's regulated identity and location checks. Do not route "
                    "United States readers to unlicensed offshore or crypto venues "
                    "or unlawful sweepstakes casinos. If a register is inaccessible, "
                    "preserve the last verified record for investigation, suppress "
                    "affected acquisition links, and request current written evidence "
                    "from the operator rather than treating silence as continued "
                    "authorization. Record who restored the destination and why."
                ),
                (
                    "The first nine directory entries are public evidence sources, "
                    "not promised machine interfaces. Their no-charge access does not "
                    "include engineering labor, bulk redistribution rights, or a "
                    "service-level commitment. Use an official download when offered; "
                    "otherwise conduct a modest scheduled page check consistent with "
                    "published access conditions. Daily retrieval is an internal "
                    "target for registers, while live launch decisions require a "
                    "fresh check of the relevant record. Store publication time "
                    "separately from retrieval time because a newly fetched page can "
                    "still contain an old decision. Use conditional requests where "
                    "supported, one outstanding request per host, bounded retries, "
                    "and a circuit breaker after repeated failures. Treat an empty "
                    "parser result as an incident, not proof that every license "
                    "disappeared. Route structural changes to a human evidence queue. "
                    "An enrichment waterfall should move from official entity record "
                    "to official approved domain, then executed partner agreement, "
                    "then internal campaign identifier. Reject fuzzy brand matches "
                    "that join unrelated subsidiaries. This sequence prevents a "
                    "cheap directory shortcut from creating expensive misdirected "
                    "traffic. The practical output is a versioned destination manifest "
                    "that both the publishing system and attribution service can "
                    "read without independently interpreting license scope."
                ),
            ],
            "table": {
                "caption": "Official Evidence Directory, Entries 1–9: Access, Cadence, and Failure Recovery",
                "headers": [
                    "Named source and exact entry point",
                    "Access method and cost tier",
                    "Refresh target and request hygiene",
                    "Fallback evidence and operator use",
                ],
                "rows": [
                    [
                        "CFTC Trading Organizations at cftc.gov; navigate Industry Oversight, Trading Organizations, Designated Contract Markets.",
                        "Open official organization pages manually or through permitted retrieval; public access carries no subscription charge.",
                        "Check relevant records daily and before launch; serialize requests and honor published access restrictions.",
                        "Inspect the underlying CFTC designation order and exchange rulebook; suspend destinations with unresolved entity mismatches.",
                    ],
                    [
                        "NFA BASIC at basic.nfa.futures.org; search the exact legal entity and available NFA identifier.",
                        "Use the public browser search without bypassing interactive controls; basic record access is free.",
                        "Review during onboarding and weekly thereafter; use human searches when automation permission is absent.",
                        "Request the entity's registration details and verify against official records; do not substitute a marketing biography.",
                    ],
                    [
                        "New Jersey Division of Gaming Enforcement at nj.gov/oag/ge; open internet gaming and vendor information.",
                        "Read official operator, platform, and vendor materials; public pages and posted documents require no subscription.",
                        "Check daily before New Jersey acquisition campaigns; cache documents and avoid repeated full-site retrieval.",
                        "Use DGE orders and direct regulator clarification; compare approved domains against the executed affiliate agreement.",
                    ],
                    [
                        "Pennsylvania Gaming Control Board at gamingcontrolboard.pa.gov; inspect interactive gaming and sports wagering license materials.",
                        "Use official license pages, public meeting records, and downloads; public evidence access is free.",
                        "Review daily and after board decisions; fetch changed documents rather than replaying every archived request.",
                        "Consult the operative board order and operator contact; withhold Pennsylvania links while scope remains unresolved.",
                    ],
                    [
                        "Michigan Gaming Control Board at michigan.gov/mgcb; open internet gaming and internet sports betting resources.",
                        "Read authorized operator and provider information through official pages; public retrieval has no subscription fee.",
                        "Check daily during active Michigan campaigns; use conditional retrieval and bounded retries where supported.",
                        "Review MGCB notices and the relevant authorization record; pause links when brand-to-license mapping conflicts.",
                    ],
                    [
                        "West Virginia Lottery at wvlottery.com; inspect sports wagering, interactive wagering, and licensing resources.",
                        "Use official public pages and published documents; request clarification when the needed vendor detail is absent.",
                        "Check weekly plus immediately before campaign activation; limit polling because public pages offer no latency commitment.",
                        "Obtain current written status from the Lottery or operator; retain the response beside the destination record.",
                    ],
                    [
                        "Alcohol and Gaming Commission of Ontario at agco.ca; follow iGaming Ontario market registration resources.",
                        "Use official public information and available registry search; public browsing requires no commercial data subscription.",
                        "Review Ontario destinations daily; respect search controls and avoid automated enumeration of registry records.",
                        "Confirm the exact registrant and registration scope directly; AGCO evidence does not replace operator agreement checks.",
                    ],
                    [
                        "iGaming Ontario at igamingontario.ca; open the official directory of regulated operators and gaming sites.",
                        "Read the public operator directory and linked approved sites; access is free through an ordinary browser.",
                        "Compare domains daily and before publishing Ontario promotions; save changed records with retrieval timestamps.",
                        "Cross-check AGCO registration and current operator correspondence; remove links when the approved domain cannot be reconciled.",
                    ],
                    [
                        "eCFR at ecfr.gov and Federal Register at federalregister.gov; retrieve cited sections, rules, and effective dates.",
                        "Use official browser pages or documented public interfaces; access is free subject to published usage terms.",
                        "Monitor relevant notices daily; paginate incrementally, cache responses, and obey each interface's published limits.",
                        "Compare the official published rule and historical effective version; flag proposals separately from operative requirements.",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Verify four independent permissions before publishing an earning link",
                "body": (
                    "A valid operator record is only one component. The destination, "
                    "your activity, the data rights, and the payable campaign must all match."
                ),
                "items": [
                    "Match legal entity, approved domain, product, territory, and current status to dated primary evidence before enabling a destination.",
                    "Document publisher, CTA, IB, and FCM boundary analysis for actual features and compensation; block custody, pooling, and unresolved order-routing features.",
                    "Confirm affiliate registration requirements, 21+ publishing controls, territory filtering, responsible-gaming text, and permitted promotional language for each campaign.",
                    "Verify display and redistribution rights, signed commercial terms, payable event definitions, reversal windows, and support contacts before assigning revenue expectations.",
                ],
            },
        },
        {
            "heading": "2. Acquire permissioned feeds and normalize contracts before measuring speed",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Separate discovery, quotation, and settlement into different "
                    "pipelines. Kalshi documents market-data interfaces, including "
                    "WebSocket access, but current authentication, account tiers, "
                    "subscription limits, and redistribution terms must be verified "
                    "in its official documentation and agreement. ForecastEx access "
                    "may come through Interactive Brokers or another authorized "
                    "distribution arrangement; do not invent a public ForecastEx "
                    "WebSocket endpoint or assume a brokerage account permits "
                    "commercial display. A commercial sportsbook feed such as "
                    "Sportradar or The Odds API can accelerate coverage, yet feed "
                    "availability does not establish affiliate permission or execution "
                    "availability. Store provider identifier, venue identifier, "
                    "contract identifier, source event time, receipt time, sequence "
                    "number when supplied, and rights classification on every "
                    "normalized record. Design for at-least-once delivery and deduplicate "
                    "by stable identifiers rather than arrival order. The next nine "
                    "directory entries distinguish public documentation from paid "
                    "entitlements and self-hosted software. Their stated refresh "
                    "cadences are operating targets, not vendor promises. Obtain "
                    "written quotes for commercial access instead of embedding "
                    "transient list prices into the business model. Keep a cheaper "
                    "read-only fallback, but never silently replace a licensed "
                    "real-time stream with scraped consumer screens."
                ),
                (
                    "Cross-venue normalization is a contract interpretation problem "
                    "before it is a probability calculation. Two election contracts "
                    "can reference different certification authorities, deadlines, "
                    "recount treatment, cancellation rules, or payout conditions. "
                    "Sportsbook prices introduce overtime rules, pushes, voided "
                    "legs, stake limits, and location-dependent availability. Attach "
                    "a versioned settlement-rule fingerprint to each comparison "
                    "pair and require an exact reviewed mapping before calling "
                    "prices comparable. For an illustrative binary contract bought "
                    "at $0.54 with an estimated $0.02 transaction cost, a research "
                    "probability of 0.60 produces expected profit of $0.04 per "
                    "contract before slippage and model error. That is analytics "
                    "output, not operator revenue or an executable riskless spread. "
                    "A sportsbook decimal price of 1.90 implies approximately "
                    "52.63% before removing the bookmaker margin; it does not "
                    "directly equal a clean probability estimate. Show displayed "
                    "size, applicable fee assumptions, rule differences, and source "
                    "timestamps alongside every comparison. If either quote is "
                    "stale or a rule mapping changes, suppress the positive-edge "
                    "badge and retain a historical chart. This fallback protects "
                    "subscriber trust without manufacturing certainty from mismatched "
                    "contracts or unavailable liquidity."
                ),
                (
                    "Instrument the feed path before marketing sub-second alerts. "
                    "Measure provider event time to receipt, receipt to normalization, "
                    "and normalization to rendered alert separately; clock skew can "
                    "otherwise make a slow system appear fast. An illustrative "
                    "internal budget of 300 milliseconds for transport, 200 for "
                    "normalization, and 300 for delivery totals 800 milliseconds "
                    "only where the source genuinely supplies timely events. "
                    "Polling every five seconds cannot support that claim. Apply "
                    "token buckets per credential and endpoint, honor Retry-After, "
                    "and reconnect with capped exponential backoff plus jitter. "
                    "After a disconnect, recover from a documented snapshot and "
                    "resume sequence only where the provider supports that method. "
                    "Otherwise mark the interval incomplete and rebuild current "
                    "state without claiming tick-perfect history. Use PostgreSQL "
                    "for normalized facts, append-only object storage for permitted "
                    "raw payloads, and Prometheus with Grafana for lag and gap "
                    "metrics. Store secrets outside logs and redact partner click "
                    "identifiers from broad dashboards. Diagnostic bundles should "
                    "contain schema versions, request identifiers, and sanitized "
                    "samples, not customer credentials. When the source fails, "
                    "degrade visibly to delayed research and stop time-sensitive "
                    "notifications until freshness and sequence checks recover."
                ),
            ],
            "table": {
                "caption": "Technical Directory, Entries 10–18: Commercial Entitlements, Data Interfaces, and Diagnostic Tools",
                "headers": [
                    "Named source and exact entry point",
                    "Access method and cost tier",
                    "Latency target and rate-limit hygiene",
                    "Fallback source and recovery behavior",
                ],
                "rows": [
                    [
                        "Kalshi official API documentation at docs.kalshi.com; inspect market data, authentication, WebSocket, and rate-limit sections.",
                        "Use documented REST and streaming interfaces under current entitlements; verify commercial display rights and any negotiated charges.",
                        "Target sub-second processing only for supported live streams; obey account-specific limits and resynchronize after connection gaps.",
                        "Use permitted REST snapshots with delayed labels; stop actionable alerts when source freshness cannot be established.",
                    ],
                    [
                        "ForecastEx at forecastex.com and Interactive Brokers documentation at interactivebrokers.com/campus; identify authorized market-data access.",
                        "Obtain approved broker or distributor access; account, market-data, and commercial rights costs depend on the executed arrangement.",
                        "Measure the actual entitled interface cadence; obey broker pacing restrictions rather than assuming exchange-native streaming access.",
                        "Use official contract specifications and permitted delayed information; remove live comparisons when authorized quotations are unavailable.",
                    ],
                    [
                        "Sportradar developer portal at developer.sportradar.com; select the licensed odds product and documented coverage package.",
                        "Request trial access where offered, then a production quote; commercial redistribution rights require explicit contractual coverage.",
                        "Use product-specific push or polling cadence; respect purchased request allowances and handle quota exhaustion without repeated retries.",
                        "Switch only to another licensed feed with equivalent mappings; otherwise display delayed research without current-price claims.",
                    ],
                    [
                        "The Odds API documentation at the-odds-api.com; inspect supported sports, markets, regions, and quota accounting.",
                        "Use a documented API key and current plan; trial or entry access and paid tiers have changing allowances.",
                        "Poll within purchased credits and returned usage indicators; align cadence with the provider's actual market update interval.",
                        "Use a separately licensed backup source or cached historical prices; mark missing markets rather than inventing coverage.",
                    ],
                    [
                        "Executed affiliate partner portal and its S2S specification; obtain the exact hostname from the signed operator agreement.",
                        "Access operator-issued credentials and documented callbacks; portal access is contractual, while tracking integration consumes staff time.",
                        "Process callbacks immediately and reconcile daily exports; enforce signatures, replay protection, deduplication, and partner-specific retry limits.",
                        "Use signed settlement exports and partner case references; keep disputed events outside collected commission totals.",
                    ],
                    [
                        "MaxMind GeoIP documentation at dev.maxmind.com; evaluate GeoLite2 and GeoIP2 database or service access.",
                        "Use licensed local databases or a paid service; free GeoLite2 access still requires applicable account and license terms.",
                        "Refresh databases on the vendor's published schedule; cache local lookups and limit paid requests by campaign need.",
                        "Suppress restricted acquisition links when location confidence is insufficient; operator-side regulated geolocation remains a separate requirement.",
                    ],
                    [
                        "PostgreSQL at postgresql.org/docs; use SQL, constraints, transaction logs, and supported backup procedures.",
                        "Self-host the open-source database or purchase managed hosting; software license cost is separate from storage and operations.",
                        "Commit normalized events promptly and batch reports; bound connection pools and test recovery against measured ingestion volume.",
                        "Replay permitted immutable payloads into a restored instance; preserve idempotency keys to prevent duplicated commission claims.",
                    ],
                    [
                        "Prometheus at prometheus.io/docs and Grafana at grafana.com/docs; configure metrics collection and service dashboards.",
                        "Self-host available open-source editions or buy hosted plans; budget compute, retention, and alert delivery separately.",
                        "Scrape internal metrics every fifteen seconds as an initial target; control label cardinality and alert on stale collection.",
                        "Use structured application logs and direct health probes; do not infer healthy feeds from a silent dashboard.",
                    ],
                    [
                        "mitmproxy at docs.mitmproxy.org and curl at curl.se/docs; inspect authorized integration traffic and HTTP behavior.",
                        "Use open-source tools on your own test clients; capture only traffic and accounts explicitly authorized for inspection.",
                        "Run targeted diagnostic sessions rather than continuous broad capture; honor endpoint limits and redact credentials before sharing evidence.",
                        "Reproduce failures with sanitized request fixtures and provider request identifiers; never intercept unrelated customer sessions.",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Four techniques that prevent attractive dashboards from hiding weak evidence",
                "body": (
                    "The highest-value optimizations make a disputed number explainable "
                    "without asking the founder to reconstruct an entire session."
                ),
                "items": [
                    "Hash settlement-rule text and alert on changes; identical event names can conceal incompatible payout definitions.",
                    "Keep source timestamps beside receipt timestamps; provider-side batching can defeat an otherwise fast alert engine.",
                    "Attach the partner's original event identifier to every payable FTD; duplicate callbacks must never create duplicate receivables.",
                    "Separate stale-price suppression from historical-chart availability; subscribers can retain useful research while live alerts remain disabled.",
                ],
            },
        },
        {
            "heading": "3. Turn verified evidence into comparison content and measurable subscriber value",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "The chapter's twelve mapped plays connect evidence acquisition "
                    "to revenue, with six infrastructure plays below and six "
                    "commercial plays in the final matrix. The required "
                    "competitor_intent_comparison_hijacking play belongs to TRACK_2: "
                    "build useful pages for '[Competitor] pricing', '[Competitor] "
                    "cancel', and '[Competitor] vs [Offer]' queries. Treat the name "
                    "as an internal acquisition label, not permission to impersonate "
                    "a competitor or interfere with cancellation. Publish text-only "
                    "brand references, timestamped public pricing citations, honest "
                    "feature matrices, and direct links to the competitor's own "
                    "cancellation instructions. Nominative fair use is context-dependent; "
                    "keep references necessary, accurate, and free of implied "
                    "endorsement. Do not copy logos, fabricate affiliations, or "
                    "describe a paid placement as an independent ranking. Disclose "
                    "material affiliate relationships clearly near relevant recommendations "
                    "under 16 CFR 255.5. If a fee cannot be verified, remove "
                    "that calculation and show the source-check date instead. "
                    "Programmatic publishing should require a complete evidence "
                    "record for each claim, not merely a template and a keyword. "
                    "A broken source should automatically retire affected factual "
                    "claims while preserving genuinely useful explanatory material "
                    "that remains supported."
                ),
                (
                    "Use the proposed 10–18% conversion range as a test hypothesis "
                    "for qualified comparison visitors, not an assumed sitewide "
                    "result. At 1,000 qualified visits, a 10% paid conversion "
                    "produces 100 subscribers; 18% produces 180. At an illustrative "
                    "$40 monthly subscription, those cohorts create $4,000 or "
                    "$7,200 of first-month billed subscription value before refunds, "
                    "payment costs, churn, and tax treatment. With $6 variable "
                    "service cost per paid subscriber, first-month contribution "
                    "before acquisition and shared overhead is $3,400 or $6,120. "
                    "If traffic costs $2,500, the remaining amounts are $900 "
                    "and $3,620. These cohort examples are not additional scorecard "
                    "revenue and cannot be annualized without retention evidence. "
                    "Measure completed paid starts separately from free account "
                    "creation, then reconcile paid starts against processor "
                    "settlements. Segment direct SaaS buyers from sportsbook "
                    "affiliate referrals so one click does not receive two "
                    "incompatible revenue assumptions. A cancellation guide can "
                    "convert by solving an urgent user problem, but it must "
                    "never obstruct the original cancellation. When paid traffic "
                    "misses its contribution threshold, stop buying that segment "
                    "and retain the evidence-backed organic page."
                ),
                (
                    "Design calculators around reproducible inputs rather than "
                    "persuasive output. A fee calculator should expose contract "
                    "quantity, quoted price, applicable fee schedule, subscription "
                    "charge, and the timestamp of every external assumption. "
                    "Retain a calculation version so support can reproduce what "
                    "a reader saw. An enrichment waterfall for comparison content "
                    "starts with the venue's official rulebook and pricing page, "
                    "then a permissioned market feed, then an executed partner "
                    "schedule, and finally an editor-confirmed exception. Do not "
                    "enrich individual readers with purchased gambling propensity "
                    "or vulnerability indicators. Use campaign-level attribution "
                    "and the minimum identifiers required for reconciliation. "
                    "For migration guides, accept only customer-authorized exports "
                    "and document which watchlists or research settings can "
                    "actually move; never request brokerage passwords. Subscription "
                    "retention should be earned through reliable alerts, transparent "
                    "methodology, and fast defect resolution. At 400 active "
                    "subscribers, reducing monthly voluntary churn from 5% to "
                    "4% retains four additional subscribers for that month, "
                    "worth $160 in billed value at $40 each before costs. "
                    "That unit math supports a small reliability project, not "
                    "an unlimited engineering budget. If retention does not "
                    "improve, revert the experiment and examine cohort-specific "
                    "failure reports."
                ),
            ],
            "table": {
                "caption": "Mapped Plays 1–6: Evidence and Market-Data Infrastructure",
                "headers": [
                    "Mapped implementation play",
                    "Concrete evidence-to-product workflow",
                    "Illustrative unit math and decision",
                    "Risk trigger and operating fallback",
                ],
                "rows": [
                    [
                        "Play 1, registry_change_monitoring, maintains the versioned approved-destination manifest.",
                        "Compare official entity and domain evidence against current campaign destinations before each activation.",
                        "Checking twenty destinations for three minutes each requires sixty minutes per review cycle.",
                        "A changed license scope suppresses affected links until a documented review resolves the discrepancy.",
                    ],
                    [
                        "Play 2, contract_rule_diffing, detects settlement changes before comparison claims persist.",
                        "Hash retrieved rule text and route material differences to an editor with source evidence.",
                        "Reviewing ten flagged mappings for six minutes each consumes one hour of specialist attention.",
                        "A material rule mismatch removes the comparison pair while preserving separately labeled historical charts.",
                    ],
                    [
                        "Play 3, licensed_destination_verification, separates territory eligibility from commercial preference.",
                        "Join approved domains to executed partner agreements and territory-specific promotional requirements.",
                        "Four territories multiplied by five approved brands creates twenty destination records requiring explicit ownership.",
                        "Missing domain evidence disables outbound promotion rather than substituting an offshore or unlicensed destination.",
                    ],
                    [
                        "Play 4, cross_venue_probability_normalization, compares reviewed contract definitions rather than similar event names.",
                        "Normalize payout conditions, market prices, fees, and quoted size before displaying probability differences.",
                        "A 0.60 estimate less 0.54 price and 0.02 costs yields 0.04 expected dollars per contract.",
                        "Different settlement conditions or missing fee inputs remove the positive-edge badge pending revalidation.",
                    ],
                    [
                        "Play 5, stale_quote_suppression, enforces source freshness before sending paid alerts.",
                        "Measure event age and sequence integrity independently from application uptime and subscriber delivery success.",
                        "An 800-millisecond internal budget combines 300 transport, 200 processing, and 300 delivery milliseconds.",
                        "Polling-only sources or stream gaps switch the product to explicitly delayed research without live alerts.",
                    ],
                    [
                        "Play 6, net_fee_calculator, makes displayed comparisons independently reproducible by subscribers.",
                        "Version fee schedules and record quantity, quote time, subscription assumptions, and applicable transaction charges.",
                        "Ten contracts priced at 0.54 plus 0.02 each require an illustrative total outlay of $5.60.",
                        "An inaccessible pricing source removes the affected calculation until current fee evidence is restored.",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Capture and classify primary evidence",
                    "action": "Create a source record with entity, territory, URL, retrieval time, effective date, rights category, and content digest.",
                    "detail": "Assign a named owner and review cadence; distinguish proposed rules, operative requirements, commercial terms, and measured observations.",
                },
                {
                    "step": 2,
                    "title": "Normalize with replayable identifiers",
                    "action": "Join contract identifiers and partner campaign identifiers through reviewed mappings rather than fuzzy brand text.",
                    "detail": "Preserve source event identifiers, schema versions, and permitted raw payloads so duplicates and corrections can be replayed safely.",
                },
                {
                    "step": 3,
                    "title": "Publish only supported comparisons",
                    "action": "Check source freshness, settlement equivalence, fee versions, territory eligibility, and adjacent affiliate disclosures before rendering.",
                    "detail": "Suppress affected claims or links when checks fail; retain clearly labeled historical material that still has adequate evidence.",
                },
                {
                    "step": 4,
                    "title": "Reconcile value and retire weak experiments",
                    "action": "Compare paid subscriber settlements and approved partner commissions against campaign costs and source operating costs.",
                    "detail": "Record reversal windows, collection status, churn, and off-season performance; stop spend when collected contribution misses the documented threshold.",
                },
            ],
        },
        {
            "heading": "4. Reconcile attribution, deductions, and seasonality to the exact scorecard",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Keep three ledgers: subscriptions, permitted builder arrangements, "
                    "and licensed gaming affiliates. The first records your SaaS "
                    "service revenue; the second records only contractually earned "
                    "software or referral consideration after boundary review; "
                    "the third records payable CPA and NGR commissions after "
                    "contractual adjustments. Under an ASC 606 principal-versus-agent "
                    "assessment, an affiliate generally reports its earned "
                    "commission rather than customer deposits, sportsbook handle, "
                    "or the operator's gaming revenue. Where retained_share "
                    "applies to pass-through billings, multiply by that share "
                    "once; never apply another haircut to a commission already "
                    "reported net. An illustrative Base bridge is 400 average "
                    "paid subscribers times $40 times twelve months, or $192,000, "
                    "plus $20,500 of permitted builder consideration and $150,000 "
                    "of net affiliate commissions, totaling $362,500. The affiliate "
                    "component can comprise 1,000 finally approved CPA events "
                    "at $120, yielding $120,000, plus $30,000 of NGR commissions "
                    "from a separate eligible cohort. An NGR example starts "
                    "with $200,000 gaming revenue, subtracts $50,000 contractual "
                    "deductions, applies a 25% share to $150,000, and subtracts "
                    "$7,500 carried losses from $37,500. The resulting $30,000 "
                    "is operator affiliate revenue, not $200,000."
                ),
                (
                    "The Base scorecard allows $224,750 of total annual operating "
                    "costs because $362,500 less $137,750 equals $224,750. An "
                    "illustrative allocation is $60,000 acquisition, $74,000 staffed "
                    "engineering and editorial work, $24,000 hosting and feeds, "
                    "$21,750 verification and support, and $45,000 other operating "
                    "costs, including remaining staff and administration. These "
                    "amounts sum exactly to the allowed cost envelope; owner "
                    "distributions are not an additional operating deduction. "
                    "Deduct NGR bonuses and administration charges in the "
                    "commission bridge, not again in overhead. The Conservative "
                    "case remains $75,000 revenue less $55,500 costs, producing "
                    "$19,500 at 26%. The Scaled case remains $650,000 less "
                    "$325,000, producing $325,000 at 50%; Base remains 38.0%. "
                    "Keep teams at 1 FT + 2 C for Conservative and Base, "
                    "and 2 FT + 3 C for Scaled. Model sportsbook seasonality "
                    "monthly without changing these annual totals silently. "
                    "For example, four off-season months losing twenty payable "
                    "FTDs each at $120 reduce expected CPA revenue by $9,600 "
                    "unless other earned revenue replaces it. Treat that as "
                    "a downside forecast variance, reduce marginal acquisition "
                    "spend, and preserve the canonical scenario as the comparison "
                    "baseline rather than pretending the gap disappeared."
                ),
                (
                    "S2S attribution needs a state machine, not a counter that "
                    "increments whenever a callback arrives. Record click accepted, "
                    "registration reported, first deposit reported, eligibility "
                    "reviewed, commission approved, commission reversed, and cash "
                    "collected as separate events. The operator determines the "
                    "payable FTD under its contract, including age, territory, "
                    "duplicate-account, minimum-deposit, and promotional conditions. "
                    "Your publishing filter does not certify those conditions. "
                    "Verify callback signatures, enforce timestamp windows, "
                    "deduplicate partner event identifiers, and reconcile daily "
                    "against exports. Reconcile monthly against settlement "
                    "statements and bank receipts. Track negative carryover "
                    "by partner and contractual cohort; do not spread it "
                    "across unrelated partners to flatter performance. For "
                    "a campaign costing $6,000 that produces eighty approved "
                    "FTDs at $120, gross commission is $9,600 and contribution "
                    "before shared costs is $3,600. Ten later reversals reduce "
                    "those figures to $8,400 and $2,400. Maintain a reserve "
                    "policy based on observed reversal timing and payment "
                    "disputes. Pause spend when collected contribution falls "
                    "below the acquisition threshold, when a partner reduces "
                    "its CPA budget, or when evidence cannot support attribution. "
                    "The final dashboard should explain every dollar from source "
                    "event to collected cash."
                ),
            ],
            "table": {
                "caption": "Mapped Plays 7–12: Conversion, Retention, Attribution, and Net Commission Protection",
                "headers": [
                    "Mapped commercial play",
                    "Exact operating implementation",
                    "Illustrative unit math and decision",
                    "Risk fallback and evidence requirement",
                ],
                "rows": [
                    [
                        "Play 7, competitor_intent_comparison_hijacking, applies the TRACK_2 comparison-content acquisition method.",
                        "Publish text-only pricing, cancellation, and alternative pages with timestamped official citations and clear relationship disclosures.",
                        "One thousand qualified visits at 10–18% paid conversion produce 100–180 subscribers before churn and refunds.",
                        "Rely strictly on necessary nominative references; remove unsupported claims and avoid logos, spoofing, or implied endorsement.",
                    ],
                    [
                        "Play 8, permissioned_migration_guides, converts research friction into a documented subscriber onboarding workflow.",
                        "Import only customer-authorized watchlists or research settings, and link directly to genuine cancellation instructions.",
                        "Saving fifteen minutes across forty migrations returns ten customer hours while keeping credential handling outside scope.",
                        "When export rights or compatibility fail, offer a manual checklist instead of requesting brokerage passwords.",
                    ],
                    [
                        "Play 9, subscription_cohort_retention, ties reliability improvements to measured subscriber contribution.",
                        "Compare churn, alert defects, support contacts, and settled subscription receipts across explicitly defined cohorts.",
                        "Reducing monthly churn from 5% to 4% across 400 subscribers retains four accounts worth $160 billed.",
                        "Stop expanding the experiment when measured retention does not improve; inspect actual defect reports before rebuilding.",
                    ],
                    [
                        "Play 10, geofenced_s2s_ftd_reconciliation, separates location filtering from operator-confirmed payable conversions.",
                        "Join signed callbacks, approved destination records, partner exports, reversal events, and collected settlement receipts.",
                        "Eighty approved FTDs at $120 yield $9,600; subtracting $6,000 acquisition leaves $3,600 before shared costs.",
                        "Ten reversed events reduce contribution to $2,400; pause campaigns when collected results breach the acquisition threshold.",
                    ],
                    [
                        "Play 11, ngr_deduction_audit, reconstructs payable share after contractually specified reductions and carryover.",
                        "Reconcile gaming revenue, bonuses, administration charges, share percentage, historical losses, and current settlement adjustments.",
                        "A $150,000 adjusted basis at 25% yields $37,500; subtracting $7,500 carryover leaves $30,000 payable.",
                        "Dispute unsupported deduction lines with statement evidence; keep contested amounts outside collected commission reporting.",
                    ],
                    [
                        "Play 12, seasonality_budget_reallocation, protects contribution when sportsbook acquisition budgets contract after peak seasons.",
                        "Forecast payable events monthly and move acquisition only toward channels with observed positive collected contribution.",
                        "Losing twenty monthly FTDs for four months at $120 creates a $9,600 annual revenue shortfall.",
                        "Reduce marginal spend and publish the downside variance; never fill missing revenue with customer handle or deposits.",
                    ],
                ],
            },
        },
    ],
    "pull_quote": (
        "The information edge is the shortest auditable path from an official "
        "permission and a fresh quote to a collected dollar."
    ),
    "diagram_id": "diag-04",
    "action_checklist": [
        "Build the destination manifest from CFTC, NFA, and applicable gaming records; attach entity, domain, territory, effective date, evidence URL, and review owner.",
        "Document publisher, CTA, IB, and FCM boundaries for the actual product and compensation; keep custody, pooled capital, and unresolved order transmission outside the service.",
        "Obtain feed entitlements and display rights, then instrument source age, processing latency, sequence gaps, endpoint quotas, and visible degraded-mode behavior.",
        "Publish one evidence-backed comparison cluster with text-only brand references, live fee assumptions, direct cancellation instructions, and adjacent affiliate disclosures.",
        "Implement signed S2S event ingestion and reconcile approved FTDs, NGR deductions, negative carryover, reversals, and cash receipts without duplicate commission recognition.",
        "Reconcile the exact $75,000, $362,500, and $650,000 revenue cases to $19,500, $137,750, and $325,000 owner profits; track seasonality as an explicit forecast variance.",
    ],
    "statutory_citations": [
        {
            "title": "7 U.S.C. 1a — Commodity Exchange Act definitions",
            "url": "https://www.law.cornell.edu/uscode/text/7/1a",
            "relevance": (
                "Defines commodity trading adviser, introducing broker, futures "
                "commission merchant, and other relevant categories; assess actual "
                "services and compensation rather than relying on a publisher label."
            ),
        },
        {
            "title": "17 CFR 1.3 — Definitions",
            "url": "https://www.ecfr.gov/current/title-17/chapter-I/part-1/section-1.3",
            "relevance": (
                "Supports activity-based review of intermediary status and the "
                "distinction between analytics publishing, solicitation, order "
                "handling, and customer-fund activity."
            ),
        },
        {
            "title": "17 CFR 4.14 — Exemption from registration as a commodity trading adviser",
            "url": "https://www.ecfr.gov/current/title-17/chapter-I/part-4/section-4.14",
            "relevance": (
                "Provides specific exemption conditions requiring fact-sensitive "
                "review; a non-custodial dashboard is not automatically outside "
                "all adviser registration requirements."
            ),
        },
        {
            "title": "17 CFR 38.251 — General requirements for prevention of market disruption",
            "url": "https://www.ecfr.gov/current/title-17/chapter-I/part-38/subpart-E/section-38.251",
            "relevance": (
                "Addresses designated contract market risk controls and market "
                "disruption safeguards; supports monitoring exchange notices "
                "without mischaracterizing exchange duties as affiliate permission."
            ),
        },
        {
            "title": "16 CFR 255.5 — Disclosure of material connections",
            "url": "https://www.ecfr.gov/current/title-16/chapter-I/subchapter-B/part-255/section-255.5",
            "relevance": (
                "Explains disclosure expectations for material connections in "
                "endorsements; place clear affiliate relationship disclosures "
                "where readers evaluate recommendations."
            ),
        },
        {
            "title": "15 U.S.C. 1125 — False designations of origin and false descriptions",
            "url": "https://www.law.cornell.edu/uscode/text/15/1125",
            "relevance": (
                "Provides the statutory context for avoiding misleading "
                "affiliation and false comparative claims; necessary text-only "
                "brand references still require context-sensitive review."
            ),
        },
        {
            "title": "18 U.S.C. 1084 — Transmission of wagering information",
            "url": "https://www.law.cornell.edu/uscode/text/18/1084",
            "relevance": (
                "Relevant to assessing sports-wagering communications and "
                "interstate activity; do not infer that an affiliate agreement "
                "authorizes accepting or transmitting customer wagers."
            ),
        },
    ],
}
