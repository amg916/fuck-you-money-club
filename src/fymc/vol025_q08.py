from __future__ import annotations

CHAPTER_8 = {
    "id": "Q8",
    "chapter_id": "Q8",
    "chapter_number": 8,
    "question_number": 8,
    "slug": "public-records-apis-data-pipelines-operator-tooling",
    "question_prompt": "Which exact public registries, government databases, commercial APIs, enrichment waterfalls, and diagnostic tools give a small freight brokerage desk an unfair information edge?",
    "kicker": "Q8 / THE BIG MONEY PLAYBOOKS",
    "title": "Public Records, APIs, Data Pipelines & Operator Tooling",
    "subtitle": "FMCSA Authority Checks, Highway and RMIS Identity Controls, Contracted Freight APIs, and Carrier-Payable Settlement Economics",
    "layout_template": "resource_directory",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #12, Freight Brokerage, ranks #25 with a Money-to-Manpower Score of "
        "62/100. Its information edge comes from eight mapped operating plays: authority "
        "verification, carrier identity defense, shipper credit screening, lane pricing "
        "and matching, shipment exception tracking, invoice reconciliation, cash-float "
        "control, and commercial virtual-card settlement rebates. This directory connects "
        "FMCSA records, Highway, RMIS, contracted market feeds, tracking providers, and "
        "issuer settlement files to specific desk decisions. Canonical annual owner "
        "profits remain $30,000 Conservative, $165,000 Base, and $400,000 Scaled. Gross "
        "shipper billings include carrier costs; payable throughput and card purchase "
        "volume are separate measures. Buy evidence that changes a decision, preserve "
        "its timestamp, and keep a documented fallback when a feed fails."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$1,000,000",
            "context": "Annual gross shipper billings including carrier costs; presentation can differ",
            "note": "3% net margin; $30,000 annual owner net profit; 3 FT + 2 C",
        },
        {
            "label": "Base",
            "value": "$3,000,000",
            "context": "Annual gross shipper billings including carrier costs; presentation can differ",
            "note": "5.5% net margin; $165,000 annual owner net profit; 3 FT + 2 C",
        },
        {
            "label": "Scaled",
            "value": "$5,000,000",
            "context": "Annual gross shipper billings including carrier costs; presentation can differ",
            "note": "8% net margin; $400,000 annual owner net profit; 4 FT + 3 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Build an evidence directory before buying another freight dashboard",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Start with the decision, not the subscription. A niche property brokerage "
                    "needs eight linked operating plays: authority verification, carrier identity "
                    "defense, shipper credit screening, lane pricing and matching, shipment "
                    "exception tracking, invoice reconciliation, cash-float control, and "
                    "commercial virtual-card settlement rebates. These are this chapter's "
                    "workflow mappings, not additional scored candidates. Give each play an "
                    "owner, an input contract, an evidence lifetime, and a manual fallback. "
                    "FMCSA registration under 49 U.S.C. 13904 and security under 49 U.S.C. "
                    "13906 are operating prerequisites, not data products. Confirm the "
                    "brokerage's own authority and the generally required $75,000 bond or "
                    "trust arrangement before tendering freight. For each carrier, distinguish "
                    "a USDOT identity record from active operating authority and applicable "
                    "insurance filings. A company snapshot does not establish that the person "
                    "answering an email controls the listed carrier. Likewise, a state entity "
                    "registration establishes a corporate filing, not payment capacity. "
                    "Preserve these distinctions in the data model so a polished dashboard "
                    "cannot turn incomplete evidence into a favorable decision. Store source "
                    "URLs, retrieval times, source effective dates, and the operator's reason "
                    "for accepting or rejecting the counterparty."
                ),
                (
                    "Use a free-first enrichment waterfall: resolve legal identity through "
                    "SAFER and state records, establish authority through Licensing and "
                    "Insurance, then buy Highway or RMIS evidence where identity or onboarding "
                    "risk justifies the expense. Query commercial services only after "
                    "deduplicating USDOT and docket identifiers; ten duplicate records should "
                    "not consume ten paid lookups. Keep shipper research separate from carrier "
                    "research, because a shipper may have no motor-carrier registration. "
                    "Match its contract entity, billing address, state filing, accounts-payable "
                    "contact, and trade references before extending terms. PACER can surface "
                    "bankruptcy proceedings, while UCC searches can reveal recorded security "
                    "interests; neither substitutes for a credit decision. The directory below "
                    "states access channels and cost models rather than invented subscription "
                    "prices. Commercial API access is frequently separately licensed from "
                    "browser access. Refresh intervals are proposed desk retrieval targets, "
                    "not promises about upstream publication. Capture each provider's actual "
                    "updated timestamp and reject silent assumptions that today's download "
                    "contains today's events. Where documentation supplies no numeric request "
                    "quota, obtain the contractual limit instead of guessing. A free public "
                    "page is not permission to automate unrestricted collection."
                ),
                (
                    "Separate source freshness, retrieval freshness, and decision freshness. "
                    "A shipment webhook received now may describe a position measured forty "
                    "minutes earlier; a registry downloaded overnight may incorporate an "
                    "older filing. Keep all three times alongside the raw response digest. "
                    "For authority-sensitive dispatch decisions, refresh the authoritative "
                    "record near tender and repeat when identity, insurance, or payment "
                    "instructions change. For slower research feeds, schedule daily imports "
                    "only where permitted and retain the source's own publication schedule. "
                    "An inexpensive control is a daily exception report showing stale "
                    "authority evidence, missing tracking events, and unresolved payable "
                    "changes. If sixty carriers each need two checks, that is 120 checks; "
                    "batch or cache stable identity fields while refreshing decision-critical "
                    "status separately. Never rotate accounts to defeat a provider's limits. "
                    "Honor Retry-After responses, use exponential backoff with jitter, and "
                    "route exhausted retries to a human queue. During an outage, use the "
                    "named official portal or previously verified contact path, recording "
                    "what could and could not be confirmed. Unresolved identity or authority "
                    "blocks a new tender; an unavailable lane-price feed merely changes "
                    "the pricing method. Different failures deserve different fallbacks."
                ),
            ],
            "table": {
                "caption": "Eighteen Named Sources: Access, Cost Model, Desk Refresh Targets, and Safe Fallbacks",
                "headers": [
                    "Named source and decision served",
                    "Exact access method and cost model",
                    "Refresh target and upstream latency treatment",
                    "Request hygiene and practical fallback evidence",
                ],
                "rows": [
                    [
                        "FMCSA SAFER Company Snapshot for carrier identity resolution",
                        "Use safer.fmcsa.dot.gov Company Snapshot search; public browser access is free",
                        "Retrieve at onboarding and changed identity; preserve displayed source dates",
                        "Use manual searches without bulk scraping; cross-check official census identifiers",
                    ],
                    [
                        "FMCSA Licensing and Insurance for authority and filing status",
                        "Use li-public.fmcsa.dot.gov carrier search; public browser access is free",
                        "Check near tender and material changes; record filing effective dates",
                        "Avoid assuming a public API exists; resolve outages before new tender",
                    ],
                    [
                        "FMCSA QCMobile API for structured carrier information retrieval",
                        "Request a webKey through mobile.fmcsa.dot.gov/QCDevsite; government developer access is free",
                        "Query permitted endpoints at onboarding; distinguish retrieval from source updates",
                        "Follow current key quotas and response codes; fall back to SAFER",
                    ],
                    [
                        "FMCSA Company Census File for bulk identity deduplication",
                        "Locate Company Census File at data.transportation.gov; public downloads are free",
                        "Import newly published releases; retain release date and dataset metadata",
                        "Prefer published downloads over repeated queries; reconcile exceptions through SAFER",
                    ],
                    [
                        "FMCSA Safety Measurement System for available safety context",
                        "Use ai.fmcsa.dot.gov/SMS public search; public portions require no subscription",
                        "Follow published monthly cycles; retain measurement period with each observation",
                        "Respect restricted fields and access rules; examine available inspection context",
                    ],
                    [
                        "State Secretary of State registries for contracting entity verification",
                        "Use the incorporation state's official business search; certified records may cost",
                        "Check onboarding and entity changes; filing publication delays vary by state",
                        "Search legal names and entity numbers; obtain official copies when disputed",
                    ],
                    [
                        "State UCC filing offices for recorded secured-creditor research",
                        "Order debtor-name searches through official filing portals; state fees vary",
                        "Refresh before material credit increases; record search cutoff and jurisdiction",
                        "Follow state search logic; request certified searches for consequential decisions",
                    ],
                    [
                        "PACER Case Locator and court dockets for bankruptcy research",
                        "Use pcl.uscourts.gov and court CM/ECF links; published PACER fees apply",
                        "Check before substantial unsecured exposure; confirm current docket entries",
                        "Observe account terms and billing controls; verify matches with court records",
                    ],
                    [
                        "National Weather Service API for route disruption alerts",
                        "Use api.weather.gov/alerts/active with documented filters; government API access is free",
                        "Poll operational areas every fifteen minutes; retain alert issuance and expiry",
                        "Send an identifying User-Agent and cache; consult weather.gov during failures",
                    ],
                    [
                        "Highway carrier identity platform for impersonation risk investigation",
                        "Purchase access through highway.com; integration rights and pricing require quotation",
                        "Evaluate onboarding and change events; confirm contracted monitoring delivery latency",
                        "Use contracted endpoints only; independently call previously verified carrier contacts",
                    ],
                    [
                        "RMIS carrier onboarding services for document and monitoring workflows",
                        "Request brokerage onboarding services through rmis.com; service packages require quotation",
                        "Process contracted alerts and renewal events; verify document effective dates",
                        "Follow integration agreement limits; validate disputed coverage with the issuing agent",
                    ],
                    [
                        "DAT market products for lane pricing and capacity discovery",
                        "Use dat.com licensed products; API and redistribution rights require agreement",
                        "Refresh active lane decisions within entitlement; preserve observation window and geography",
                        "Cache permitted results without credential sharing; obtain direct carrier quotes",
                    ],
                    [
                        "Truckstop load-board and rate products for independent market comparison",
                        "Use truckstop.com subscriptions; developer access requires the applicable commercial agreement",
                        "Retrieve active-lane evidence as permitted; record quote age and equipment scope",
                        "Respect package quotas and reuse restrictions; compare verified carrier bids",
                    ],
                    [
                        "project44 shipment visibility services for exception-driven tracking operations",
                        "Contract through project44.com; authenticated API and webhook access depend on scope",
                        "Consume shipment events continuously; measure event age against receipt time",
                        "Validate documented authentication and deduplicate events; call dispatch during tracking gaps",
                    ],
                    [
                        "Descartes MacroPoint tracking services for carrier location and milestones",
                        "Contract through macropoint.com; integration access and shipment charges require quotation",
                        "Consume contracted event feeds; monitor actual update cadence per shipment",
                        "Observe provider request limits and tracking permissions; use verified dispatch updates",
                    ],
                    [
                        "Google Maps Routes API for route duration comparison",
                        "Use routes.googleapis.com/directions/v2:computeRoutes with credentials; metered pricing and quotas apply",
                        "Request at planning and material disruption; preserve departure time assumptions",
                        "Set budget limits and respect storage terms; verify truck routing separately",
                    ],
                    [
                        "QuickBooks Online Accounting API for invoice and payment reconciliation",
                        "Use developer.intuit.com OAuth applications; accounting subscription and platform terms apply",
                        "Combine supported webhooks with reconciliation pulls; allow for posting delays",
                        "Honor throttling and entity versions; reconcile against exported ledger reports",
                    ],
                    [
                        "WEX accounts-payable services for virtual-card and settlement evidence",
                        "Request AP services through wexinc.com; portal and integration terms are negotiated",
                        "Import settlement and rebate statements when posted; distinguish authorization from settlement",
                        "Use contracted exports or APIs; reconcile exceptions against bank settlement records",
                    ],
                ],
            },
        },
        {
            "heading": "2. Turn registry evidence into carrier-fraud and shipper-credit decisions",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Build a carrier identity graph around USDOT number, docket number, "
                    "legal name, dispatch contacts, insurance evidence, equipment expectations, "
                    "and independently verified payment instructions. Do not key the graph "
                    "on email alone: an impersonator can reproduce a logo, certificate, "
                    "and rate confirmation without controlling a truck. Highway and RMIS "
                    "can contribute signals and documents, but the brokerage still needs "
                    "an explicit decision trail. When dispatch introduces a new domain or "
                    "bank account, call a previously verified number rather than the number "
                    "inside the change request. Ask the pickup facility to compare the "
                    "arriving tractor identification and carrier representation with the "
                    "tendered arrangement, escalating discrepancies before release. A leased "
                    "tractor or different marking can have a legitimate explanation, so "
                    "investigate rather than automatically accuse. Verify insurance with "
                    "the issuing agent through an independently sourced channel, including "
                    "relevant cargo exclusions and policy dates. An uploaded certificate "
                    "alone does not resolve coverage. Keep identity review distinct from "
                    "safety selection: available inspection data, equipment suitability, "
                    "cargo characteristics, and service history answer different questions. "
                    "No single vendor score should collapse these judgments into one "
                    "unexplained green indicator."
                ),
                (
                    "For shipper credit, establish which entity owes the invoice and "
                    "whether the purchase order, transportation agreement, and accounts-payable "
                    "instructions identify that same obligor. State filings help resolve "
                    "names; UCC filings identify recorded interests under the relevant "
                    "jurisdiction's Article 9 system; bankruptcy dockets identify proceedings "
                    "and orders requiring further review. A lien is not proof of distress, "
                    "and a clean search is not proof of solvency. Combine public records "
                    "with directly verified trade references, payment behavior, disputes, "
                    "and a written exposure limit. Suppose a shipper requests ten $2,000 "
                    "loads weekly on forty-five-day terms. Steady outstanding billings "
                    "approach $128,571, using $20,000 times 45 divided by seven, before "
                    "seasonality or disputes. That exceeds many new desks' usable cash "
                    "even if the lane earns an attractive spread. Begin with fewer loads, "
                    "a deposit, shorter terms, or a funded receivables arrangement whose "
                    "recourse terms the owner understands. Track legal-entity exposure "
                    "across sales representatives so splitting accounts cannot bypass "
                    "the limit. Preserve adverse evidence with exact entity matches; "
                    "similar names and stale addresses create expensive false positives "
                    "in both underwriting and collections."
                ),
                (
                    "Use evidence quality to prioritize labor. At the Base team's three "
                    "full-time staff and two contractors, reviewing every routine shipment "
                    "from scratch wastes capacity, but waiving review for a familiar "
                    "display name invites impersonation. Classify exceptions by consequence: "
                    "changed bank instructions, inconsistent identity, and authority "
                    "problems interrupt tender or payment; missing optional enrichment "
                    "does not. An illustrative queue of forty weekly reviews at twelve "
                    "minutes each consumes eight hours. Reducing twenty-five low-risk "
                    "duplicates to two-minute confirmations saves 250 minutes while "
                    "preserving fifteen full investigations. Measure the actual result "
                    "rather than treating saved minutes as eliminated salaries. For "
                    "double-brokering defense, connect the booked carrier, pickup evidence, "
                    "tracking participant, delivery paperwork, and payable recipient. "
                    "A mismatch should produce a named investigation, not an automated "
                    "payment to whichever inbox submits the first invoice. Retain a "
                    "controlled broker transaction record under 49 CFR 371.3 for the "
                    "required three years, including applicable compensation and "
                    "freight-charge information. Address transaction-party review rights "
                    "through a controlled retrieval process. Longer preservation may "
                    "be needed for disputes, litigation holds, or other applicable "
                    "record obligations; do not let a routine deletion job destroy "
                    "an active claim file."
                ),
            ],
            "table": {
                "caption": "Four Consequential Verification Decisions and Their Evidence Fallbacks",
                "headers": [
                    "Trigger requiring a concrete desk decision",
                    "Evidence bundle and independent verification method",
                    "Unit economics or operational exposure measure",
                    "Fallback when the evidence cannot resolve risk",
                ],
                "rows": [
                    [
                        "Dispatch requests a newly substituted carrier email domain",
                        "Compare identity graph and independently call the previously verified carrier",
                        "One unresolved substitution can expose the entire cargo movement",
                        "Hold the new tender and source another fully verified carrier",
                    ],
                    [
                        "Carrier requests changed bank details immediately before payment",
                        "Authenticate the request separately and compare approved payable beneficiary records",
                        "A $12,000 misdirected payment consumes eight $1,500 load spreads",
                        "Keep the existing payment hold until independent verification resolves ownership",
                    ],
                    [
                        "Shipper requests ten weekly loads on forty-five-day payment terms",
                        "Match contract entity and obtain references plus current receivables aging",
                        "$20,000 weekly billings imply approximately $128,571 steady outstanding exposure",
                        "Reduce accepted volume or require deposits before exposure exceeds capacity",
                    ],
                    [
                        "Pickup identity differs from the carrier named on tender",
                        "Collect facility observations and verify any legitimate equipment leasing arrangement",
                        "Delay costs must be weighed against full shipment loss exposure",
                        "Prevent cargo release until a named operator resolves the discrepancy",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four checks before freight or money leaves your control",
                "body": (
                    "Assign each check to a named operator and retain the evidence used "
                    "for that shipment or payment decision."
                ),
                "items": [
                    "Confirm applicable carrier authority through FMCSA evidence close to tender; distinguish the USDOT record from operating authority.",
                    "Resolve dispatch identity and pickup discrepancies through independently verified contacts before authorizing cargo release.",
                    "Confirm the shipper's contracting entity and remaining credit capacity before accepting another load on terms.",
                    "Verify changed payment instructions outside the requesting message thread and separate beneficiary changes from payment release.",
                ],
            },
        },
        {
            "heading": "3. Engineer a small, auditable pipeline that survives stale feeds",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Implement four layers: permitted raw evidence, normalized entities, "
                    "decision events, and accounting postings. A small desk can begin "
                    "with a managed relational database, encrypted object storage, and "
                    "scheduled jobs rather than a streaming platform. Use USDOT and "
                    "docket identifiers as separate fields, retaining original text "
                    "and normalized values; docket prefixes matter. Map each shipment "
                    "to its shipper entity, booked carrier, equipment requirement, "
                    "rate confirmation, tracking reference, invoice, and payable. Every "
                    "import needs source identifier, effective timestamp, retrieval "
                    "timestamp, parser version, and content digest. Preserve raw material "
                    "only to the extent the license and retention obligations allow. "
                    "Idempotency keys should combine the provider's event identifier "
                    "with its account or shipment scope, preventing retried webhooks "
                    "from creating duplicate milestones or payments. Quarantine schema "
                    "changes instead of silently dropping fields. For example, if "
                    "an authority status changes from a documented enumeration to "
                    "an unrecognized value, require review rather than mapping it "
                    "to active. Keep provider credentials in a secret store, give "
                    "contractors role-limited access, and isolate payment capabilities "
                    "from research access. A dispatcher should not acquire beneficiary "
                    "editing powers merely because both features share a dashboard."
                ),
                (
                    "Instrument the workflow at the points where stale information "
                    "becomes money. Track request success rate, throttled requests, "
                    "source age, webhook event age, duplicate-event suppression, "
                    "unmatched invoices, and reconciliation backlog. Use OpenTelemetry "
                    "for traces where supported, Prometheus-compatible counters for "
                    "pipeline health, and structured logs with shipment identifiers "
                    "instead of full bank details. These are optional infrastructure "
                    "choices, not prerequisites for opening a brokerage. A basic "
                    "dashboard and an owned exception queue can serve the same "
                    "decisions at lower operating cost. Set alerts from contractual "
                    "service requirements and observed behavior: a critical pickup "
                    "may warrant investigation after a thirty-minute tracking gap, "
                    "while a nightly ledger import can wait until its documented "
                    "completion window. Route weather alerts against shipment corridors "
                    "and confirm truck-specific restrictions separately; general road "
                    "directions do not establish legal truck routing. For pricing, "
                    "retain DAT or Truckstop observation dates, equipment classes, "
                    "and lane definitions, then compare live verified carrier bids. "
                    "If a feed is unavailable, price from documented quotes and "
                    "recent completed loads rather than presenting an old market "
                    "estimate as a current executable rate."
                ),
                (
                    "Reconciliation should join the shipment, approved rate, delivery "
                    "evidence, accessorial authorization, carrier invoice, shipper "
                    "invoice, and settlement event. A delivery timestamp alone does "
                    "not prove that a detention charge was agreed. Maintain "
                    "separate disputed and undisputed amounts so one questioned "
                    "accessorial does not obscure the entire payable. At 3,000 "
                    "annual loads, cutting routine reconciliation from ten minutes "
                    "to four releases 18,000 minutes, or 300 hours annually. "
                    "At an illustrative $35 loaded hourly cost, the capacity "
                    "value is $10,500; recognize actual savings only when spending "
                    "or staffing changes. Keep the canonical Base owner profit "
                    "at $165,000 unless the complete scenario is rebuilt. For "
                    "load matching, score verified equipment fit, service history, "
                    "geography, and current availability before price; a cheap "
                    "unverified carrier is not usable capacity. At five candidate "
                    "calls reduced to three across 3,000 loads, two minutes "
                    "per avoided call represents 200 annual hours. Avoid double "
                    "counting those hours with onboarding or reconciliation savings. "
                    "Test each automation against anonymized or synthetic records "
                    "covering duplicate events, changed identifiers, partial payments, "
                    "reversed settlements, and missing delivery evidence before it "
                    "can alter live operational state."
                ),
            ],
            "table": {
                "caption": "Four Pipeline Diagnostics That Connect Data Defects to Desk Actions",
                "headers": [
                    "Diagnostic and concrete measurement to retain",
                    "Failure pattern that requires operator attention",
                    "Controlled automated response before human intervention",
                    "Recovery evidence required before normal processing resumes",
                ],
                "rows": [
                    [
                        "Source age measured separately from local retrieval age",
                        "Fresh download contains authority evidence older than the decision window",
                        "Mark evidence stale and prevent new automated tender decisions",
                        "Store a fresh authoritative check or a documented resolved investigation",
                    ],
                    [
                        "Webhook event identity and shipment-scoped duplicate counter",
                        "Repeated tracking delivery attempts create duplicated shipment milestone events",
                        "Apply idempotency keys and acknowledge already processed valid events",
                        "Replay retained permitted events and verify one resulting milestone",
                    ],
                    [
                        "Invoice match rate across rates, delivery, and accessorial approvals",
                        "Carrier invoice contains detention charges without matching written authorization",
                        "Separate disputed amounts and route the discrepancy to operations",
                        "Attach documented resolution and reconcile the resulting authorized payable",
                    ],
                    [
                        "Settlement match rate across issuer files and bank postings",
                        "Authorized virtual-card purchase never settles or later reverses",
                        "Keep authorization separate from completed payment and rebate recognition",
                        "Match final settlement identifiers and adjust any reversed rebate accrual",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Register the source contract",
                    "action": "Document access rights, authenticated endpoints, permitted storage, and quota rules.",
                    "detail": "Assign an owner and a fallback before the first production request.",
                },
                {
                    "step": 2,
                    "title": "Normalize without discarding evidence",
                    "action": "Store source and retrieval times, stable identifiers, parser version, and digest.",
                    "detail": "Quarantine schema surprises and preserve licensed evidence needed for reconstruction.",
                },
                {
                    "step": 3,
                    "title": "Replay consequential failure cases",
                    "action": "Test duplicate events, stale authority, changed beneficiaries, and reversed settlements.",
                    "detail": "Require repeatable results with no duplicated tenders, invoices, or payment instructions.",
                },
                {
                    "step": 4,
                    "title": "Reconcile and assign exceptions daily",
                    "action": "Join operational events to ledger entries and assign unresolved items.",
                    "detail": "Record resolution evidence, elapsed time, and the operator responsible for closure.",
                },
            ],
        },
        {
            "heading": "4. Monetize settlement carefully and keep float separate from profit",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "The mapped play b2b_commercial_vcc_interchange_rebate_arbitrage embeds "
                    "automated accounts payable and rapid vendor settlement into a "
                    "freight desk's existing invoice workflow. The platform issues "
                    "single-use commercial virtual cards through a contracted issuer "
                    "and earns a negotiated share of eligible settled purchase "
                    "volume. The cited 140–195 basis points means 1.40%–1.95%, "
                    "not the entire interchange charge and not a universal "
                    "available rebate. Establish who receives the rebate, which "
                    "transactions qualify, when reversals apply, and whether program "
                    "fees reduce the share. Consider the Base scenario's illustrative "
                    "3,000 loads at $1,000 shipper billing each: $3,000,000 "
                    "gross billings less $2,550,000 carrier costs yields $450,000 "
                    "gross spread. Another $285,000 of operating costs produces "
                    "the canonical $165,000 owner profit. If willing carriers "
                    "accept cards on 20% of those payables, eligible volume "
                    "is $510,000 and gross contracted rebate potential is "
                    "$7,140–$9,945 before program costs and adjustments. That "
                    "volume is carrier settlement throughput, not additional "
                    "brokerage revenue. Do not add the rebate to the "
                    "scorecard while leaving its costs and accounting treatment "
                    "unexamined. Treat it as a separately reconciled sensitivity "
                    "until an approved operating budget incorporates the actual "
                    "net contribution."
                ),
                (
                    "Make acceptance voluntary and specific to the carrier. A "
                    "$10,000 card payment with a 2.5% illustrative acceptance "
                    "cost imposes $250 on the recipient while a 1.40%–1.95% "
                    "rebate returns only $140–$195 to the program beneficiary. "
                    "That mismatch can destroy a valuable capacity relationship "
                    "if hidden inside claims of free settlement. Automatically "
                    "supply accurate Level-3 invoice and line-item metadata "
                    "through issuer-supported fields where the transaction qualifies; "
                    "do not invent tax amounts or assume enhanced data "
                    "eliminates acceptance costs. For card-averse carriers, offer "
                    "an explicit early-pay ACH alternative when economics support "
                    "it. On a $10,000 invoice otherwise due in thirty "
                    "days, a 1.5%–2% discount paid on day ten costs "
                    "the carrier $150–$200 for twenty days of acceleration. "
                    "The simple annualized cost on cash received is approximately "
                    "27.8%–37.2%, making transparent comparison essential. Focus on "
                    "fragmented long-tail vendors that value faster cash, but "
                    "retain ordinary ACH for those that decline. Never describe "
                    "credit as free float: issuer due dates, reserves, "
                    "limits, and settlement failures remain the brokerage's "
                    "operating constraints. A declined card requires a verified "
                    "replacement payment path, not another unreviewed beneficiary."
                ),
                (
                    "Model float independently from margin. Using the Base "
                    "illustration's $2,550,000 annual carrier costs and a "
                    "twenty-five-day gap between carrier payment and shipper "
                    "collection, the cost-funded bridge is about $174,658: "
                    "$2,550,000 divided by 365, multiplied by twenty-five. "
                    "This is a simplified working-capital estimate, excluding "
                    "overhead, reserves, taxes, bad debt, and uneven weekly "
                    "volume. It is not recognized revenue or an issuer "
                    "credit commitment. Update a thirteen-week cash forecast "
                    "from open receivables, committed carrier payables, available "
                    "cash, and documented funding availability. Stress a "
                    "large shipper paying fifteen days late and remove "
                    "uncollected disputes from spendable cash. Preserve all "
                    "three scorecard cases: $1,000,000 at 3% yields "
                    "$30,000; $3,000,000 at 5.5% yields $165,000; "
                    "$5,000,000 at 8% yields $400,000. The Scaled "
                    "team is four full-time staff plus three contractors, "
                    "not a solo operation. Gross billings include carrier "
                    "costs; principal-versus-agent accounting presentation requires "
                    "a separate assessment. Purchase tools within the stated "
                    "$6,000–$30,000 monthly operating range and $50,000–$250,000 "
                    "startup capital range, testing actual affordability. A "
                    "rebate opportunity must never override carrier verification, "
                    "shipper credit limits, or the cash required to "
                    "finish already accepted freight."
                ),
            ],
            "table": {
                "caption": "Settlement and Float Math Without Inflating the Canonical Scorecard",
                "headers": [
                    "Economic case and exact measurement basis",
                    "Calculation with clearly separated economic components",
                    "Recognition boundary and actual operating constraint",
                    "Risk fallback when the proposed method fails",
                ],
                "rows": [
                    [
                        "Base freight illustration using gross shipper billings",
                        "$3,000,000 billings minus $2,550,000 carriers minus $285,000 operations equals $165,000",
                        "Canonical owner profit remains 5.5% of gross shipper billings",
                        "Reprice freight or reduce commitments when actual costs exceed budget",
                    ],
                    [
                        "Virtual-card sensitivity covering twenty percent of Base carrier payables",
                        "$510,000 eligible settled volume times 1.40%–1.95% equals $7,140–$9,945",
                        "Gross rebate sensitivity excludes fees, reversals, and contractual sharing",
                        "Use verified ACH when carriers decline or issuer capacity disappears",
                    ],
                    [
                        "Early-pay alternative on one ten-thousand-dollar carrier invoice",
                        "Day-ten payment with 1.5%–2% discount transfers $9,850–$9,800",
                        "Twenty-day acceleration costs approximately 27.8%–37.2% simple annualized on proceeds",
                        "Offer ordinary agreed ACH terms when the carrier rejects acceleration",
                    ],
                    [
                        "Base cost-funded float bridge across twenty-five calendar days",
                        "$2,550,000 annual carrier costs divided by 365 times 25 equals $174,658",
                        "Working-capital estimate excludes overhead, disputes, reserves, and seasonal concentration",
                        "Reduce exposure or secure documented funding before accepting additional commitments",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Protect capacity relationships while extracting settlement value",
                "body": (
                    "The strongest desk measures verified savings and settled cash, "
                    "not dashboard activity or advertised rebate ceilings."
                ),
                "items": [
                    "Ask carriers about card acceptance during onboarding, then preserve their chosen payment method instead of renegotiating under delivery pressure.",
                    "Keep a previously verified dispatch contact outside the current email thread; impersonation investigations depend on an independent callback path.",
                    "Reconcile rebates from settled issuer statements, including reversals, rather than multiplying authorized card volume by the headline rate.",
                    "Run a weekly cash forecast that excludes disputed receivables and separately identifies carrier commitments already accepted by operations.",
                ],
            },
        },
    ],
    "pull_quote": "A freight desk's information edge is evidence that changes a tender, a credit limit, or a payment before cash leaves.",
    "diagram_id": "diag-04",
    "action_checklist": [
        "Create an eighteen-source register with access rights, cost owners, source timestamps, request limits, and documented outage fallbacks.",
        "Link each carrier's USDOT and docket identifiers to independently verified dispatch contacts, insurance evidence, and approved payment instructions.",
        "Set shipper-level exposure limits using contracting entities, verified references, receivables aging, and a thirteen-week cash forecast.",
        "Implement idempotent shipment and accounting imports with stale-evidence alerts, schema quarantine, and daily exception ownership.",
        "Pilot voluntary virtual-card settlement on verified eligible payables, reconciling actual rebates, fees, reversals, and carrier acceptance costs.",
        "Preserve the $30,000, $165,000, and $400,000 canonical owner-profit cases while reporting automation savings and settlement sensitivities separately.",
    ],
    "statutory_citations": [
        {
            "title": "49 U.S.C. 13904 — Registration of brokers",
            "url": "https://www.law.cornell.edu/uscode/text/49/13904",
            "relevance": (
                "Establishes the broker registration framework that the desk must "
                "distinguish from a carrier's USDOT identity record."
            ),
        },
        {
            "title": "49 U.S.C. 13906 — Security requirements",
            "url": "https://www.law.cornell.edu/uscode/text/49/13906",
            "relevance": (
                "Provides the statutory basis for property-broker security, including "
                "the $75,000 amount; verify the applicable bond or trust arrangement."
            ),
        },
        {
            "title": "49 CFR 387.307 — Property brokers: surety bond or trust fund",
            "url": "https://www.ecfr.gov/current/title-49/section-387.307",
            "relevance": (
                "Defines operative broker security requirements and related procedures; "
                "review the current text when establishing and maintaining coverage."
            ),
        },
        {
            "title": "49 CFR 371.3 — Records to be kept by brokers",
            "url": "https://www.ecfr.gov/current/title-49/section-371.3",
            "relevance": (
                "Requires specified transaction records, three-year retention, and "
                "transaction-party review access; informs evidence storage and retrieval."
            ),
        },
        {
            "title": "49 CFR 371.2 — Definitions",
            "url": "https://www.ecfr.gov/current/title-49/section-371.2",
            "relevance": (
                "Distinguishes brokerage activity and related roles, helping operators "
                "classify the actual service rather than relying on marketing labels."
            ),
        },
        {
            "title": "Delaware Code, Title 6, Section 9-502 — Contents of financing statement",
            "url": "https://delcode.delaware.gov/title6/c009/sc05/index.html#9-502",
            "relevance": (
                "Provides a concrete enacted UCC Article 9 filing rule; use the "
                "applicable debtor jurisdiction and official search procedures when "
                "researching recorded secured-creditor interests."
            ),
        },
    ],
}
