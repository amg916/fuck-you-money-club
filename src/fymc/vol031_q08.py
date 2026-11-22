from __future__ import annotations

CHAPTER_8 = {
    "id": "Q8",
    "chapter_id": "Q8",
    "chapter_number": 8,
    "question_number": 8,
    "slug": "public-records-apis-data-pipelines-operator-tooling",
    "question_prompt": "Which exact public registries, government databases, commercial APIs, enrichment waterfalls, and diagnostic tools give a small uber & commercial fleet arbitrage desk an unfair information edge?",
    "kicker": "Q8 / THE BIG MONEY PLAYBOOKS",
    "title": "Public Records, APIs, Data Pipelines & Operator Tooling",
    "subtitle": (
        "TLC and CPUC Records, NHTSA VIN Intelligence, Authorized Fleet APIs, "
        "Driver Screening, Toll Ledgers, and Evidence-Backed Lease Waterfalls"
    ),
    "layout_template": "resource_directory",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #31, Uber & Commercial Fleet Arbitrage, ranks #15 of 36 with "
        "an 89/100 Money-to-Manpower Score. This directory maps 10 operating plays "
        "across driver leases, Black SUV dispatch, investor co-hosting, permit "
        "verification, VIN screening, coverage continuity, driver monitoring, toll "
        "recovery, maintenance scheduling, and authorized advertising rewards. "
        "Sixteen named sources separate public evidence from permissioned account "
        "data, with access paths, cost structures, freshness controls, and fallback "
        "procedures. Formula v2.0 produces annual owner profits of $25,200, $144,900, "
        "and $336,000 on gross operator billings of $180,000, $690,000, and "
        "$1,200,000. The modeled 55% retained contribution is $99,000, $379,500, "
        "and $660,000 respectively. Build the desk around reconciled identifiers "
        "and settlement evidence, not scraped passenger activity or unsupported "
        "assumptions about platform access."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$180,000",
            "context": (
                "Annual gross driver lease, dispatch, and co-hosting billings; "
                "$99,000 retained contribution at 55%."
            ),
            "note": (
                "14% gross-basis net margin; 25.45% retained net margin; "
                "$25,200 annual owner net profit; 1 FT + 3 C."
            ),
        },
        {
            "label": "Base",
            "value": "$690,000",
            "context": (
                "Annual gross driver lease, dispatch, and co-hosting billings; "
                "$379,500 retained contribution at 55%."
            ),
            "note": (
                "21.0% gross-basis net margin; 38.18% retained net margin; "
                "$144,900 annual owner net profit; 1 FT + 3 C."
            ),
        },
        {
            "label": "Scaled",
            "value": "$1,200,000",
            "context": (
                "Annual gross driver lease, dispatch, and co-hosting billings; "
                "$660,000 retained contribution at 55%."
            ),
            "note": (
                "28% gross-basis net margin; 50.91% retained net margin; "
                "$336,000 annual owner net profit; 2 FT + 4 C."
            ),
        },
    ],
    "sections": [
        {
            "heading": "1. Build an evidence spine before enriching a single vehicle",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Start with three durable entities: vehicle, driver, and operating "
                    "agreement. A vehicle record carries the normalized VIN, plate plus "
                    "issuing jurisdiction, plate effective dates, investor account, "
                    "registration expiry, and permitted service class. A driver record "
                    "carries an internal identifier and separately protected license "
                    "references; a lease record links the parties, service territory, "
                    "billing calendar, and responsibility for tolls, deductibles, and "
                    "downtime. Never join on a driver name alone or treat a plate as "
                    "permanent: plate transfers create false toll allocations and "
                    "misleading permit histories. Store each observation with source "
                    "name, retrieval timestamp, source effective date, raw response "
                    "digest, and the identifier actually queried. Keep the original "
                    "file immutable, then write normalized facts into SQLite for a "
                    "small desk or an existing managed database as volume grows. A "
                    "public listing establishes what that registry publishes, not "
                    "insurance coverage, platform eligibility, ownership, or authority "
                    "to obtain personal records. Under 18 U.S.C. 2721, access to motor "
                    "vehicle personal information requires a permitted purpose; broad "
                    "lead generation is not a substitute. Keep public eligibility "
                    "research separate from permissioned driver screening so an "
                    "analyst cannot accidentally turn a fleet prospect list into a "
                    "personal-data collection campaign."
                ),
                (
                    "Run enrichment from cheapest decisive evidence to expensive "
                    "verification. First validate VIN length and format, decode it "
                    "through NHTSA vPIC, and compare the returned model year and body "
                    "class with the proposed Black SUV service. Next query the "
                    "relevant TLC or CPUC record, preserving its published update "
                    "time rather than assuming that today's download means today's "
                    "status. Then inspect recall evidence and order an NMVTIS report "
                    "through an approved provider when title history could change "
                    "the acquisition or co-hosting decision. NHTSA's public recall "
                    "campaign API is not a VIN-specific repair-completion certificate; "
                    "use the manufacturer or dealer channel for completion evidence. "
                    "NICB VINCheck is a limited screening input, not a complete "
                    "ownership, theft, or damage history. Finish with authorized "
                    "driver records and carrier-issued coverage evidence before "
                    "assigning a revenue shift. For illustration, avoiding one "
                    "$180 title report and inspection bundle on each of five clearly "
                    "ineligible prospects saves $900; that saving is an acquisition "
                    "expense reduction, not additional lease revenue. If sources "
                    "disagree, retain both observations, open an exception, and hold "
                    "the assignment until the issuing authority, owner, or insurer "
                    "resolves the relevant fact in writing."
                ),
                (
                    "The first eight directory entries cover official records and "
                    "low-cost verification. Their cost descriptions identify charging "
                    "structures, not invented vendor quotes; capture the current "
                    "price and permitted use during onboarding. For Socrata, locate "
                    "the named dataset, record its resource identifier, and use its "
                    "Export or API documentation rather than copying an identifier "
                    "from an old blog. Page large responses, select only necessary "
                    "columns, and compare record counts with the published export. "
                    "A zero-row response can mean a bad filter, renamed field, or "
                    "stale identifier; it cannot independently prove that a vehicle "
                    "lacks authority. Check dataset metadata and run a known-valid "
                    "control lookup before escalating an empty result. Cache stable "
                    "VIN decoding, but refresh status-sensitive permit evidence at "
                    "dispatch and after a relevant alert. California TCP authority "
                    "and New York TLC licensing are jurisdiction-specific regimes, "
                    "not interchangeable national credentials. Airport operating "
                    "rights require separate verification with the airport involved. "
                    "If a portal blocks automation, use its permitted manual lookup "
                    "or published download and record the operator's evidence; do "
                    "not bypass challenges or borrow another account. Give every "
                    "fallback an expiry so a saved screenshot never quietly becomes "
                    "permanent operating authority."
                ),
            ],
            "table": {
                "caption": (
                    "Named Source Directory, Entries 1-8: Public Registries and "
                    "Authorized Government Record Channels"
                ),
                "headers": [
                    "Named source and decisive operating question",
                    "Exact access method and evidence captured",
                    "Cost tier and purchasing control",
                    "Refresh latency and freshness treatment",
                    "Rate-limit hygiene and extraction discipline",
                    "Fallback source and operating response",
                ],
                "rows": [
                    [
                        "NYC TLC Active For-Hire Vehicles tests local vehicle licensing status.",
                        "At data.cityofnewyork.us, find the exact dataset title and open its documented Socrata API.",
                        "Public dataset access is free; budget separately for ingestion monitoring.",
                        "Read the published update timestamp; recheck before first assignment and after status alerts.",
                        "Use application tokens where supported, bounded pagination, cached snapshots, and delayed retries.",
                        "Use TLC's official vehicle license lookup and retain dated authority evidence.",
                    ],
                    [
                        "NYC TLC Active For-Hire Drivers tests published driver license status.",
                        "At data.cityofnewyork.us, locate the named dataset and export only required status fields.",
                        "Public dataset access is free; restrict staff access to identifying fields.",
                        "Use source metadata to measure publication lag; check again before assignment.",
                        "Filter narrowly, avoid repeated full downloads, and respect returned throttling instructions.",
                        "Confirm through TLC's official license-status service before releasing a disputed assignment.",
                    ],
                    [
                        "California CPUC Transportation Carrier Lookup tests the proposed carrier's TCP authority.",
                        "Use cpuc.ca.gov transportation pages to open Transportation Carrier Lookup and search the carrier identifier.",
                        "Public carrier lookup is free; authority application and renewal charges are separate.",
                        "Capture the lookup time and displayed status; investigate effective-date differences immediately.",
                        "Use the published search interface; automate only through explicitly supported access.",
                        "Request current CPUC authority documents and resolve discrepancies through the commission.",
                    ],
                    [
                        "NHTSA vPIC VIN decoding tests vehicle identity and advertised configuration.",
                        "GET vpic.nhtsa.dot.gov/api/vehicles/DecodeVinValues/{VIN}?format=json and preserve returned decoding errors.",
                        "Public API access is free; internal development and exception review consume budget.",
                        "Decode at onboarding and after corrected identifiers; retain the source observation date.",
                        "Cache by VIN, serialize bursts, and use documented batch methods when appropriate.",
                        "Compare registration and manufacturer build evidence; unresolved identity differences stop onboarding.",
                    ],
                    [
                        "NHTSA recall campaign data identifies model-level safety campaigns requiring investigation.",
                        "GET api.nhtsa.gov/recalls/recallsByVehicle with make, model, and modelYear query parameters.",
                        "Public campaign lookup is free; dealer inspection or repairs may involve separate costs.",
                        "Poll active fleet models weekly; verify VIN-specific repair status through manufacturer channels.",
                        "Cache make-model-year requests and back off on temporary service or quota errors.",
                        "Use nhtsa.gov/recalls and manufacturer VIN lookup; obtain dealer repair-completion evidence.",
                    ],
                    [
                        "NMVTIS approved consumer providers reveal reported title brands and salvage events.",
                        "Select an approved provider through vehiclehistory.bja.ojp.gov and purchase the VIN report.",
                        "Reports are provider-priced per vehicle or contract; approve charges before ordering.",
                        "Reporting lag varies by submitting entity; inspect event dates before acquisition.",
                        "Use provider-approved purchases or contracted API access; never scrape restricted reports.",
                        "Obtain state title evidence and independent inspection; title conflicts stop vehicle acceptance.",
                    ],
                    [
                        "NICB VINCheck screens limited participating-insurer theft and salvage reporting.",
                        "Use nicb.org/vincheck manually under the published service conditions and permitted purpose.",
                        "The public lookup is free; it does not replace paid title investigation.",
                        "Search during onboarding; treat results as limited coverage with reporting delays.",
                        "Honor displayed search caps; do not rotate addresses or accounts around restrictions.",
                        "Escalate to NMVTIS and authorized ownership documentation before accepting disputed vehicles.",
                    ],
                    [
                        "California DMV Employer Pull Notice supports qualifying employer driver monitoring.",
                        "Enroll through dmv.ca.gov Employer Pull Notice pages and follow authorized driver enrollment procedures.",
                        "DMV enrollment and record fees follow the current schedule and applicable exemptions.",
                        "Use delivered notices and program-scheduled records; do not represent them as instantaneous.",
                        "Follow enrollment, purpose, retention, and delivery rules rather than scraping DMV pages.",
                        "Obtain an authorized current DMV record while preserving required program participation.",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Four ways experienced fleet desks avoid expensive false positives",
                "body": (
                    "Spend verification effort where it changes vehicle acceptance, "
                    "shift assignment, or collectible cash."
                ),
                "items": [
                    (
                        "Store plate assignments as dated intervals; a toll posted "
                        "after a plate transfer belongs to the event-time assignment."
                    ),
                    (
                        "Run a known-valid TLC lookup alongside every ingestion job; "
                        "an empty control result signals a broken feed, not mass suspension."
                    ),
                    (
                        "Separate recall campaign discovery from completed repair "
                        "evidence; request the dealer repair order before closing the exception."
                    ),
                    (
                        "Reject an unsuitable vehicle configuration using cached vPIC "
                        "evidence before purchasing deeper reports or scheduling an inspection."
                    ),
                ],
            },
        },
        {
            "heading": "2. Connect authorized APIs without confusing access with entitlement",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Permissioned integrations begin with an authority register, not "
                    "an API key pasted into a spreadsheet. Record the account owner, "
                    "approved purpose, allowed fleet identifiers, scopes, credential "
                    "custodian, renewal date, and revocation procedure. Uber supplier "
                    "tools expose capabilities according to geography, relationship, "
                    "and account entitlement; do not assume a public endpoint can "
                    "read every driver's earnings or enforce every lease waterfall. "
                    "Use the authorized portal export until the relevant supported "
                    "integration is available. Samsara and Geotab can provide vehicle "
                    "telemetry through contracted interfaces, but location access "
                    "does not confer authority to command hardware. Keep command "
                    "credentials outside the reporting pipeline. Starter-interrupt "
                    "equipment requires a separate documented process addressing "
                    "local restrictions, contract disclosures, stationary-state "
                    "verification, emergency access, and vendor safety controls; "
                    "a billing exception must never directly trigger immobilization. "
                    "Stripe events show payment lifecycle changes, not final earned "
                    "revenue or irrevocable collection. Match processor settlements, "
                    "fees, refunds, and disputes against the bank deposit before "
                    "closing a billing period. The commercial directory below names "
                    "eight channels worth evaluating; none implies that this desk "
                    "already has credentials, a negotiated price, production access, "
                    "or the right to retrieve another operator's records."
                ),
                (
                    "Use an append-only ingestion envelope containing source, "
                    "account identifier, event identifier, event time, receipt time, "
                    "schema version, and raw-object digest. Deduplicate webhooks by "
                    "source account and event identifier, then apply updates through "
                    "an idempotent transaction. Providers can retry messages, deliver "
                    "them late, or deliver a refund before a delayed payment event; "
                    "the current business state must come from a supported object "
                    "lookup or an explicit state transition policy. Poll overlapping "
                    "time windows where a feed supports them, and advance the "
                    "watermark only after the full page set commits. Respect "
                    "Retry-After when supplied; otherwise use bounded exponential "
                    "backoff with jitter and a retry ceiling. Persistent failures "
                    "go to an exception queue instead of spinning indefinitely. "
                    "Preserve raw timestamps and normalize a separate field to UTC, "
                    "retaining local service dates for toll disputes and shift "
                    "billing. Encrypt driver reports separately from telemetry and "
                    "settlement records, and give dispatch only the eligibility "
                    "result needed for assignment. Consumer-report use requires "
                    "a permissible purpose under 15 U.S.C. 1681b; employment-purpose "
                    "reports bring additional disclosure, authorization, and adverse "
                    "action duties when applicable. Calling a driver an independent "
                    "contractor does not settle those questions."
                ),
                (
                    "A small fleet needs a freshness budget for each decision. "
                    "A historical VIN decode can remain useful for months, while "
                    "a device's last GPS fix must carry its actual event time "
                    "before anyone uses it to coordinate a pickup. Establish a "
                    "local operating threshold, such as flagging location samples "
                    "older than fifteen minutes for dispatch review, without "
                    "pretending the vendor promises that latency. Toll charges "
                    "may arrive days after a shift; keep the lease ledger open "
                    "for the contractually stated reconciliation period and retain "
                    "the event-time vehicle assignment. Use Google Ads API reporting "
                    "only for accounts the client has authorized through the "
                    "appropriate manager relationship. Developer-token access and "
                    "OAuth authorization are separate requirements, and neither "
                    "proves card-reward eligibility. Review account quotas in the "
                    "provider console rather than hard-coding folklore about "
                    "requests per minute. Every integration should have a manual "
                    "continuity route: signed export, secure portal download, or "
                    "a documented provider support case. During an outage, label "
                    "stale observations explicitly, stop decisions that require "
                    "fresh evidence, and continue unaffected collections or "
                    "bookkeeping. This preserves useful operations without turning "
                    "a temporary data failure into an unjustified driver rejection "
                    "or an unsafe vehicle assignment."
                ),
            ],
            "table": {
                "caption": (
                    "Named Source Directory, Entries 9-16: Contracted APIs, "
                    "Account Portals, and Permissioned Verification Tools"
                ),
                "headers": [
                    "Named source and decisive operating question",
                    "Exact access method and evidence captured",
                    "Cost tier and purchasing control",
                    "Refresh latency and freshness treatment",
                    "Rate-limit hygiene and extraction discipline",
                    "Fallback source and operating response",
                ],
                "rows": [
                    [
                        "Checkr driver screening supplies ordered reports for authorized eligibility decisions.",
                        "Use dashboard.checkr.com or the documented api.checkr.com interface with approved account credentials.",
                        "Reports and packages are paid; jurisdictional charges and monitoring require current quotations.",
                        "Completion depends on source availability; preserve pending status until the report completes.",
                        "Verify webhook signatures, deduplicate events, and follow account-specific API limits.",
                        "Use the authorized dashboard and provider support; never substitute an unrelated person's record.",
                    ],
                    [
                        "SambaSafety driver monitoring identifies changes within the contracted reporting program.",
                        "Use sambasafety.com customer access and provisioned integration documentation for enrolled drivers.",
                        "Monitoring and record retrieval are contracted services with product-specific pricing.",
                        "Freshness depends on state sources and subscribed products; inspect each record's dates.",
                        "Apply contracted quotas, deduplicate notices, and avoid repeated unnecessary record purchases.",
                        "Order a current authorized state record and resolve monitoring discrepancies with support.",
                    ],
                    [
                        "Uber Supplier Portal supports entitled fleet account reporting and settlement review.",
                        "Use supplier.uber.com and supported exports; request integration access through the account relationship.",
                        "Access and commercial arrangements depend on the fleet relationship and market.",
                        "Use displayed reporting periods and settlement status; exports are not live bank confirmation.",
                        "Use supported exports or approved interfaces; never automate private session endpoints.",
                        "Reconcile account statements with bank deposits and request missing settlement detail.",
                    ],
                    [
                        "Samsara telematics connects contracted vehicle observations to dispatch and maintenance.",
                        "Use developers.samsara.com and api.samsara.com with scoped tokens for authorized fleet assets.",
                        "Hardware, connectivity, software subscriptions, and feature access follow the negotiated contract.",
                        "Device connectivity controls delivery; evaluate event timestamps separately from API receipt times.",
                        "Follow endpoint limits, paginate results, and request only necessary assets and fields.",
                        "Use the authorized dashboard and manual mileage evidence; suspend stale-location dispatch assumptions.",
                    ],
                    [
                        "Geotab MyGeotab supplies permissioned device feeds and vehicle diagnostic observations.",
                        "Use developers.geotab.com MyGeotab API documentation and GetFeed for entitled database entities.",
                        "Hardware and service plans are contracted; reseller terms determine included capabilities.",
                        "Feed arrival depends on device reporting and connectivity; preserve event and receipt times.",
                        "Persist feed version tokens, respect method limits, and retry without duplicating observations.",
                        "Use MyGeotab exports and service records; investigate device silence before drawing conclusions.",
                    ],
                    [
                        "New York E-ZPass statements establish posted toll amounts for account vehicles.",
                        "Use ezpassny.com account access and permitted statement downloads for the operator's account.",
                        "Account, tag, and toll charges follow the issuing authority's current schedule.",
                        "Posting can lag travel; distinguish passage date, posting date, and statement close.",
                        "Use permitted downloads without bypassing login controls; schedule reconciliation around statement availability.",
                        "Request authority transaction detail and compare plate, tag, route, and driver assignment.",
                    ],
                    [
                        "Stripe payment events support lease collection matching and dispute tracking.",
                        "Use docs.stripe.com, api.stripe.com, and signed webhooks scoped to the authorized account.",
                        "Processing, disputes, and optional products carry published or contracted transaction charges.",
                        "Events can retry or arrive out of order; settlement follows payout schedules.",
                        "Use idempotency keys for supported writes, bounded pagination, and documented retry behavior.",
                        "Use Dashboard exports and bank statements; leave unmatched receipts in suspense.",
                    ],
                    [
                        "Google Ads API verifies authorized advertising delivery and account spending.",
                        "Use developers.google.com/google-ads/api with OAuth, developer token, and authorized customer identifiers.",
                        "Advertising spend and operating costs apply; token access does not create reward entitlement.",
                        "Reporting freshness varies by metric; reconcile invoiced spend after billing adjustments.",
                        "Observe developer-token quotas, batch suitable queries, and cache completed reporting periods.",
                        "Use authorized account exports and invoices; switch to client-direct billing when required.",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four pre-flight checks before a vehicle earns its first shift",
                "body": (
                    "Release the assignment only when the evidence covers the "
                    "specific driver, vehicle, service, jurisdiction, and operating time."
                ),
                "items": [
                    (
                        "Match VIN, current plate interval, driver identity, signed "
                        "agreement, and any required TLC, TCP, or airport authority."
                    ),
                    (
                        "Obtain carrier or authorized broker evidence of continuous "
                        "commercial livery or applicable Period 1-2-3 coverage, "
                        "including off-app use and the actual rental arrangement."
                    ),
                    (
                        "Complete authorized driver screening, required report-use "
                        "procedures, and review of unresolved safety or eligibility exceptions."
                    ),
                    (
                        "Test settlement import, toll assignment, location freshness, "
                        "and manual continuity; keep remote hardware commands isolated."
                    ),
                ],
            },
        },
        {
            "heading": "3. Map ten plays to collectible cash and the canonical scorecard",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "The ten chapter mappings are operating workflows, not ten "
                    "additional revenue lines. The first five are driver lease "
                    "waterfalls, Black SUV shift dispatch, investor vehicle "
                    "co-hosting, permit verification, and VIN screening. The next "
                    "section maps coverage continuity, driver monitoring, toll "
                    "recovery, maintenance scheduling, and the specified advertising "
                    "rewards play. Maintain that distinction because one vehicle "
                    "can touch nine workflows while generating only one lease "
                    "invoice. An illustrative vehicle billed at $550 for fifty "
                    "paid weeks produces $27,500 of annual gross lease billings; "
                    "two empty weeks do not become receivables merely because "
                    "a calendar contains fifty-two weeks. At the modeled 55% "
                    "retained share, that example leaves $15,125 before the "
                    "remaining operator expenses. A $600 missed deductible "
                    "reimbursement consumes more than one week's $302.50 retained "
                    "lease contribution. For dispatch, calculate margin on the "
                    "contractual dispatch fee or appropriately classified service "
                    "billings, never on passenger fares the operator neither "
                    "earns nor controls. For co-hosting, use the investor agreement's "
                    "documented waterfall and distinguish owner distributions from "
                    "operator earnings. These examples explain sensitivities; they "
                    "are not a reconstructed fleet count or a replacement for "
                    "the supplied Formula v2.0 scenario totals."
                ),
                (
                    "Reconcile the scorecard through three layers: gross operator "
                    "billings, retained contribution, and owner net profit. "
                    "Conservative billings of $180,000 retain $99,000 at 55%; "
                    "subtract $73,800 of remaining modeled expenses to reach "
                    "$25,200 owner profit. Base billings of $690,000 retain "
                    "$379,500; subtract $234,600 to reach $144,900. Scaled billings "
                    "of $1,200,000 retain $660,000; subtract $324,000 to reach "
                    "$336,000. Gross-basis net margins remain exactly 14%, 21.0%, "
                    "and 28%, while retained-basis margins round to 25.45%, "
                    "38.18%, and 50.91%. Conservative and Base staffing remain "
                    "1 FT plus 3 contractors; Scaled remains 2 FT plus 4 "
                    "contractors. Preserve the model's 55% ASC 606 retained-share "
                    "presentation without treating that percentage as an accounting "
                    "rule for every contract: principal-versus-agent analysis "
                    "depends on the actual promises and control of services. "
                    "The stated $2,500-$15,000 monthly operating expense range "
                    "does not independently explain every annual expense above; "
                    "do not force those measures to match by inventing categories. "
                    "Build an explicit expense bridge when underlying records "
                    "become available. Keep passenger GMV, investor asset value, "
                    "loan balances, deposits, and client advertising pass-throughs "
                    "outside operator revenue unless the applicable contract and "
                    "accounting treatment support recognition."
                ),
                (
                    "Map agency_ad_spend_card_multiplier_rebate_cycling as TRACK_2, "
                    "a separate authorized advertising-payment workflow rather "
                    "than a reason to inflate fleet demand. Its full operating "
                    "concept is Whitelisted Agency Ad-Spend Card-Multiplier Points "
                    "& Volume-Rebate Cycling: only genuine client-authorized spend "
                    "under eligible agency arrangements can qualify. An illustrative "
                    "$20,000 monthly campaign earning a documented 2% cash-equivalent "
                    "reward and a separately stackable 0.5% volume rebate yields "
                    "$500 before costs. Subtract $120 of incremental funding and "
                    "processing costs plus $200 contractually owed to the client; "
                    "the remaining contribution is $180. Confirm whether points "
                    "actually redeem at the assumed value and whether refunds "
                    "reverse both benefits. Do not count the $20,000 client spend "
                    "as fleet revenue, count the same rebate twice, or layer "
                    "this example onto canonical profit without removing existing "
                    "amounts. Match Ads invoices, card statements, rebate settlement "
                    "records, and client terms by billing period. Prohibit "
                    "manufactured spending, circular payments, and campaign "
                    "expansion justified only by rewards. If eligibility changes, "
                    "the client withdraws authority, or costs consume the spread, "
                    "move to client-direct billing or prefunded approved agency "
                    "terms and stop rewards-dependent spending. The fallback "
                    "protects the underlying campaign rather than chasing a "
                    "payment incentive."
                ),
            ],
            "table": {
                "caption": (
                    "Mapped Plays 1-5: Acquisition, Leasing, Dispatch, and "
                    "Co-Hosting Unit Economics"
                ),
                "headers": [
                    "Mapped operating play and evidence chain",
                    "Concrete unit math and ledger treatment",
                    "Failure mode and diagnostic signal",
                    "Risk fallback and required operating response",
                ],
                "rows": [
                    [
                        "Play 1: Driver lease waterfalls link authorized platform statements, contracts, and deposits.",
                        "$550 multiplied by fifty paid weeks equals $27,500 billings and $15,125 modeled retained contribution.",
                        "Missing platform deductions or duplicate invoices overstate collectible cash and expected distributions.",
                        "Use direct contract reconciliation and permitted collection methods; never assume platform deduction priority.",
                    ],
                    [
                        "Play 2: Black SUV shift dispatch links service eligibility, airport rights, and completed bookings.",
                        "Twelve completed shifts at a $40 dispatch fee produce $480 operator fee billings.",
                        "Counting passenger trip value as dispatch revenue inflates yield and hides empty shifts.",
                        "Assign only eligible replacement vehicles and recognize completed contractual fees without invented utilization.",
                    ],
                    [
                        "Play 3: Investor vehicle co-hosting links vehicle acceptance, owner agreements, and monthly waterfalls.",
                        "$4,000 eligible receipts with a contractual 25% fee create $1,000 fee billings before expenses.",
                        "Applying both the contract split and modeled retention to identical costs double-counts deductions.",
                        "Bridge contractual cash flows to scorecard categories once; dispute unclear charges before distribution.",
                    ],
                    [
                        "Play 4: Permit verification links TLC, CPUC, and applicable airport operating evidence.",
                        "Avoiding two unusable $350 shift commitments preserves $700 before any replacement service costs.",
                        "A fresh download containing stale source status creates false confidence about operating authority.",
                        "Confirm current authority with the issuing body or substitute an independently eligible vehicle.",
                    ],
                    [
                        "Play 5: VIN screening links vPIC identity checks, recall evidence, and NMVTIS reports.",
                        "Rejecting five unsuitable prospects before a $180 inspection bundle preserves $900 acquisition expense.",
                        "Model-level recall results cannot establish VIN-specific repair completion or complete title history.",
                        "Obtain manufacturer repair evidence and state title records; reject unresolved identity conflicts.",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Register the account and permitted purpose",
                    "action": (
                        "Record the data owner, approved use, authorized assets, "
                        "credential scope, and revocation contact."
                    ),
                    "detail": (
                        "Separate public registry access from driver-report permissions, "
                        "platform entitlements, and advertising payment authority."
                    ),
                },
                {
                    "step": 2,
                    "title": "Capture evidence before transforming it",
                    "action": (
                        "Save raw exports or responses with source timestamps, "
                        "retrieval timestamps, and SHA-256 digests."
                    ),
                    "detail": (
                        "Maintain immutable originals and effective-dated identity "
                        "links; normalize only into a separate working dataset."
                    ),
                },
                {
                    "step": 3,
                    "title": "Reconcile the decision and the money",
                    "action": (
                        "Join eligible assignments to invoices, settlement events, "
                        "bank deposits, and contractual distributions."
                    ),
                    "detail": (
                        "Quarantine duplicates, stale authority, unmatched tolls, "
                        "and unexplained split differences before closing the period."
                    ),
                },
                {
                    "step": 4,
                    "title": "Publish exceptions with named owners",
                    "action": (
                        "Issue a daily exception report showing affected shifts, "
                        "cash exposure, responsible staff, and resolution deadlines."
                    ),
                    "detail": (
                        "Use documented manual continuity for unaffected operations "
                        "and retain the evidence that closed each exception."
                    ),
                },
            ],
        },
        {
            "heading": "4. Instrument the desk so stale data cannot become a cash leak",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "A useful control panel shows decisions and exposure, not "
                    "just successful HTTP requests. Track source freshness, unmatched "
                    "vehicle identities, unassigned toll amounts, unresolved coverage "
                    "intervals, pending driver reports, settlement differences, and "
                    "vehicle downtime hours. Give each metric a denominator: five "
                    "unmatched tolls out of six is different from five out of "
                    "six thousand. Use Python logging for structured job events, "
                    "sqlite3 for durable local state, hashlib for evidence digests, "
                    "and unittest for parsers and reconciliation rules. Keep "
                    "credentials out of logs and sample payloads. Add tests for "
                    "duplicate webhooks, plate reuse, daylight-saving transitions, "
                    "negative adjustments, partial refunds, canceled shifts, and "
                    "late toll posting. A job should fail visibly if a required "
                    "column disappears or a monetary field changes format; silently "
                    "substituting zero turns a schema change into fabricated "
                    "performance. Compare daily row counts and total amounts "
                    "against historical ranges, but route unusual results to "
                    "review rather than deleting them. For a one-person full-time "
                    "desk supported by contractors, assign one exception owner "
                    "and one backup per feed. Contractors receive only the "
                    "records required for their task, while access revocation "
                    "is part of offboarding rather than an annual cleanup."
                ),
                (
                    "Coverage continuity and driver monitoring deserve independent "
                    "exception queues because a cash ledger cannot prove either. "
                    "For each vehicle, align policy effective intervals with the "
                    "actual service: off-app rental use, app-on waiting, accepted "
                    "trips, passenger transport, and commercial livery assignments. "
                    "California Public Utilities Code section 5433 addresses "
                    "transportation network company insurance, but it does not "
                    "replace the coverage analysis for a TCP livery arrangement "
                    "or an investor-owned vehicle rented to a driver. Ask the "
                    "carrier or authorized broker to resolve exclusions, vehicle "
                    "schedules, driver restrictions, and cancellation notices; a "
                    "certificate alone does not rewrite the policy. Driver "
                    "monitoring likewise needs a defined response to a new "
                    "record, a dispute, and an incomplete report. Where employment "
                    "reporting rules apply, build the required pre-adverse and "
                    "adverse action steps into the case workflow rather than "
                    "letting an automated score terminate access. Apply a "
                    "written retention schedule tied to the relevant purpose "
                    "and dispute obligations. The business objective is timely, "
                    "defensible assignment, not collecting every available "
                    "personal detail. During a coverage or eligibility conflict, "
                    "use a separately verified replacement or pause that "
                    "assignment while continuing unrelated administrative work."
                ),
                (
                    "Close the week with an exception-to-cash bridge. Begin "
                    "with issued billings, subtract credits and reversals, "
                    "separate collected cash from open receivables, then allocate "
                    "investor distributions and pass-through fleet costs once. "
                    "Measure toll recovery against contractually recoverable "
                    "posted charges, not every camera event or provisional "
                    "telematics inference. A $34 toll recovered exactly from "
                    "the responsible driver can settle a receivable without "
                    "creating $34 of retained profit. For maintenance, compare "
                    "actual odometer evidence with the service schedule and "
                    "book repairs into lower-demand windows. Avoiding two "
                    "days of downtime at $550 divided by seven days preserves "
                    "about $157.14 gross lease capacity, not that amount of "
                    "owner profit; apply retention and incremental repair "
                    "costs before claiming a benefit. Track advertising rewards "
                    "only after the issuer and rebate provider settle them, "
                    "with reversals assigned to the original campaign. Review "
                    "the ten mappings monthly and retire feeds that do not "
                    "change a decision, prevent a loss, or accelerate collection. "
                    "Capital remains constrained by the canonical $12,000-$65,000 "
                    "startup range, and first-deal planning remains one to "
                    "three months. Buying more dashboards does not shorten "
                    "vehicle qualification, insurance placement, or a legitimate "
                    "client authorization process."
                ),
            ],
            "table": {
                "caption": (
                    "Mapped Plays 6-10: Safety Evidence, Cost Recovery, "
                    "Maintenance, and Authorized Advertising Rewards"
                ),
                "headers": [
                    "Mapped operating play and evidence chain",
                    "Concrete unit math and ledger treatment",
                    "Failure mode and diagnostic signal",
                    "Risk fallback and required operating response",
                ],
                "rows": [
                    [
                        "Play 6: Coverage continuity links carrier evidence, scheduled vehicles, and actual operating intervals.",
                        "A $300 monthly premium increase across ten vehicles reduces annual contribution by $36,000.",
                        "A policy exclusion or uncovered operating period can overwhelm apparent weekly lease spread.",
                        "Pause affected assignments, obtain written coverage resolution, or use independently covered replacement capacity.",
                    ],
                    [
                        "Play 7: Driver monitoring links authorized state records and contracted screening alerts.",
                        "An illustrative $15 monthly monitoring price across twenty drivers costs $3,600 annually.",
                        "Delayed source updates or identity mismatches can trigger incorrect driver eligibility decisions.",
                        "Verify current records and applicable report-use procedures before acting on disputed information.",
                    ],
                    [
                        "Play 8: Toll recovery links authority transactions to effective-dated plate and driver assignments.",
                        "One hundred recoverable $34 tolls create $3,400 reimbursements, not automatically retained revenue.",
                        "Posting-date allocation charges the wrong driver when vehicles change hands between shifts.",
                        "Use passage-time assignments, contractual disclosures, and authority detail before collecting disputed charges.",
                    ],
                    [
                        "Play 9: Maintenance scheduling links odometer evidence, diagnostic alerts, and completed repair orders.",
                        "Two avoided downtime days at $550 weekly preserve approximately $157.14 gross lease capacity.",
                        "Stale odometers or unresolved diagnostic alerts turn optimistic utilization forecasts into lost shifts.",
                        "Verify mileage manually and substitute qualified capacity while completing documented service work.",
                    ],
                    [
                        (
                            "Play 10: agency_ad_spend_card_multiplier_rebate_cycling "
                            "under TRACK_2 links authorized spend, issuer rewards, and volume rebates."
                        ),
                        "$20,000 spend earns $500 eligible benefits; subtract $120 costs and $200 client share for $180.",
                        "Reward exclusions, reversals, delayed payment, or client pass-through duties can erase the spread.",
                        "Move to client-direct billing or prefunded approved agency terms and stop rewards-dependent spending.",
                    ],
                ],
            },
        },
    ],
    "pull_quote": (
        "An information edge exists only when a dated source changes an "
        "assignment, prevents a loss, or reconciles collectible cash."
    ),
    "diagram_id": "diag-04",
    "action_checklist": [
        (
            "Create effective-dated VIN, plate, driver, investor, and agreement "
            "records before importing any toll or settlement feed."
        ),
        (
            "Register all sixteen directory sources with their current access "
            "terms, costs, update behavior, authorized purpose, and manual fallback."
        ),
        (
            "Build the public-record waterfall from vPIC and licensing checks "
            "through title evidence, authorized driver reports, and carrier confirmation."
        ),
        (
            "Implement idempotent ingestion, raw evidence digests, freshness checks, "
            "schema tests, and a named owner for every unresolved exception."
        ),
        (
            "Reconcile the three canonical cases to 55% retained contribution "
            "and the exact $25,200, $144,900, and $336,000 owner profit totals."
        ),
        (
            "Document client authority, issuer eligibility, rebate stacking, "
            "costs, reversals, and the client-direct fallback before routing advertising spend."
        ),
    ],
    "statutory_citations": [
        {
            "title": (
                "18 U.S.C. 2721 — Prohibition on release and use of certain "
                "personal information from state motor vehicle records"
            ),
            "url": "https://www.law.cornell.edu/uscode/text/18/2721",
            "relevance": (
                "Identify a permitted purpose before obtaining or using protected "
                "motor vehicle record information; public fleet research does not "
                "authorize unrestricted personal-data retrieval."
            ),
        },
        {
            "title": "15 U.S.C. 1681b — Permissible purposes of consumer reports",
            "url": "https://www.law.cornell.edu/uscode/text/15/1681b",
            "relevance": (
                "Establish the permissible purpose for driver reports and apply "
                "employment-purpose disclosure, authorization, and pre-adverse "
                "action requirements where applicable."
            ),
        },
        {
            "title": "15 U.S.C. 1681m — Requirements on users of consumer reports",
            "url": "https://www.law.cornell.edu/uscode/text/15/1681m",
            "relevance": (
                "Build applicable adverse-action notices and consumer reporting "
                "agency identification into report-based eligibility decisions."
            ),
        },
        {
            "title": (
                "California Public Utilities Code section 5433 — "
                "Transportation network company insurance requirements"
            ),
            "url": (
                "https://leginfo.legislature.ca.gov/faces/"
                "codes_displaySection.xhtml?sectionNum=5433.&lawCode=PUC"
            ),
            "relevance": (
                "Map insurance evidence to the relevant app and trip periods "
                "for California TNC operations; separately assess commercial "
                "livery, rental, and investor-owned vehicle arrangements."
            ),
        },
        {
            "title": (
                "California Public Utilities Code section 5371 — "
                "Charter-party carrier operating authority"
            ),
            "url": (
                "https://leginfo.legislature.ca.gov/faces/"
                "codes_displaySection.xhtml?sectionNum=5371.&lawCode=PUC"
            ),
            "relevance": (
                "Verify applicable CPUC authority before assigning California "
                "charter-party service; platform membership does not replace "
                "required carrier authority."
            ),
        },
        {
            "title": (
                "California Vehicle Code section 1808.1 — "
                "Employer driver record information and notification"
            ),
            "url": (
                "https://leginfo.legislature.ca.gov/faces/"
                "codes_displaySection.xhtml?sectionNum=1808.1.&lawCode=VEH"
            ),
            "relevance": (
                "Determine applicable Employer Pull Notice participation and "
                "record obligations for the actual employer, driver, and "
                "vehicle categories involved."
            ),
        },
        {
            "title": (
                "49 U.S.C. 30120 — Remedies for defects and noncompliance"
            ),
            "url": "https://www.law.cornell.edu/uscode/text/49/30120",
            "relevance": (
                "Distinguish recall campaign discovery from documented remedy "
                "completion and retain manufacturer or dealer evidence for "
                "vehicle-specific safety exceptions."
            ),
        },
    ],
}
