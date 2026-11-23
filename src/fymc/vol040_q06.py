from __future__ import annotations

CHAPTER_6 = {
    "id": "Q6",
    "chapter_id": "Q6",
    "chapter_number": 6,
    "question_number": 6,
    "slug": "sourcing-demand-mining-and-landing-first-deals",
    "question_prompt": "Where do high-margin deals, clients, or undervalued assets hide in self-funded health, pbm & workers' comp arbitrage, and what repeatable outbound/inbound sourcing system lands the first 3-to-10 wins (2–5 months)?",
    "kicker": "Q6 / THE BIG MONEY PLAYBOOKS",
    "title": "Sourcing, Demand Mining & Landing Your First Deals",
    "subtitle": "Form 5500 Renewal Signals, SEC EDGAR Executive Triggers, NADAC Repricing, and NCCI E-Mod Recovery Mandates",
    "layout_template": "step_by_step_sop",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #40 ranks #08 of 42 with a 93/100 Money-to-Manpower Score because "
        "employer benefit friction creates several monetizable entry points without owning "
        "claim risk. This chapter maps 11 sourcing plays into one evidence-led acquisition "
        "system: public filings identify timing, authorized records establish recoverability, "
        "and narrowly priced mandates convert interest into retained fees. Target the first "
        "3-to-10 signed wins over 2–5 months using renewal calendars, executive changes, "
        "PBM contract mismatches, and workers' compensation corrections. Canonical annual "
        "owner profit is $38,400 Conservative, $240,750 Base, and $551,000 Scaled. Those "
        "outcomes use retained operator revenue, never employer premiums or claim funds. "
        "The operating advantage is disciplined qualification, documented compensation, "
        "and outreach tied to a verifiable event rather than speculative savings."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$120,000",
            "context": "Annual retained operator revenue; employer premiums and claim funds excluded",
            "note": "32% net margin; $38,400 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Base",
            "value": "$535,000",
            "context": "Annual retained operator revenue; advisory fees, commissions, and recovery splits",
            "note": "45.0% net margin; $240,750 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Scaled",
            "value": "$950,000",
            "context": "Annual retained operator revenue; excludes underlying employer spending",
            "note": "58% net margin; $551,000 annual owner net profit; 2 FT + 4 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Mine renewal windows and executive events before buying broad lead lists",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Build the first account universe around employers with roughly 200–2,000 "
                    "covered employees, an identifiable benefits decision maker, and enough "
                    "time before renewal to evaluate alternatives. Treat this band as an "
                    "initial targeting hypothesis, not a universal underwriting threshold. "
                    "Download Department of Labor Form 5500 datasets through EFAST2 resources; "
                    "join employer EIN, plan number, filing year, participant counts, and "
                    "Schedule A contract periods into a dated account record. Separate health "
                    "contracts from dental, vision, disability, and life coverage before "
                    "assigning a renewal hypothesis. Schedule A insurance periods do not "
                    "automatically establish a self-funded medical renewal, and Schedule C "
                    "reporting is not a complete broker compensation ledger. Public filings "
                    "can lag operating reality, amended filings can replace earlier values, "
                    "and exemptions leave some employers outside this universe. Verify timing "
                    "on the first conversation. An illustrative batch of 120 employers might "
                    "yield 36 apparently relevant renewal windows and 12 verified dates; "
                    "these are planning assumptions, not published conversion rates. Store "
                    "source URL, retrieval date, evidence excerpt, and confidence separately "
                    "from inferred need. Never turn a participant count into enrolled "
                    "employees without checking the definition. The first sellable deliverable "
                    "is a renewal evidence brief, not an unsolicited proposal claiming that "
                    "a captive or self-funded plan will save money."
                ),
                (
                    "Implement sec_edgar_8k_vendor_trigger_arbitrage as a timing layer over "
                    "that employer universe. Poll SEC EDGAR current-filing RSS feeds and "
                    "documented JSON endpoints where available; resolve the accession, issuer "
                    "identity, filing type, and event text rather than relying on keyword "
                    "headlines. Form D reports exempt offerings, but the amount offered is "
                    "not cash received; distinguish it from the reported amount sold. "
                    "Route Form 8-K Item 5.02 departures or appointments, Item 1.01 material "
                    "agreements, and Item 2.01 acquisition closings into separate queues. "
                    "None proves benefit dissatisfaction. Require an employer match and a "
                    "plausible operating consequence, such as acquired workforces or a new "
                    "CFO inheriting renewal decisions. Use an identifying User-Agent, a "
                    "token bucket capped at five requests per second across workers, "
                    "deduplication by accession, and backoff on throttling. Each night, "
                    "mirror available SEC bulk ZIP archives for historical lookbacks; "
                    "use daily indexes and accession retrieval where no corresponding ZIP "
                    "exists. Do not assume every feed has a nightly archive. A batch of "
                    "40 events producing eight relevant accounts and two conversations "
                    "is an explicit test case. Aim for human-reviewed, sub-hour executive "
                    "outreach after ingestion, before slower commercial databases refresh; "
                    "measure actual latency rather than promising universal speed."
                ),
                (
                    "Map the chapter's 11 sourcing plays to distinct buying reasons: EDGAR "
                    "executive triggers, Form 5500 renewal targeting, Schedule A/C compensation "
                    "discovery, acquisition census reconciliation, NADAC benchmark repricing, "
                    "PBM rebate reconciliation, stop-loss renewal comparison, TPA service "
                    "unbundling, NCCI E-Mod correction, payroll classification review, and "
                    "partner-led diagnostic demand. The matrix starts the first seven; "
                    "the next section completes the map. Keep the outreach consequence "
                    "specific. A new CFO receives a dated renewal-risk brief; an acquired "
                    "business receives a census and contract inventory; an employer with "
                    "a transparent PBM already receives no spread accusation. For compensation "
                    "discovery, 600 covered employees at $4 PEPM creates $28,800 annual "
                    "advisory fees only after enrollment, scope, and payment terms are "
                    "confirmed. An acquisition census engagement priced at 800 employees "
                    "times $3 PEPM also produces $28,800 annually, but do not stack both "
                    "fees for identical work. A $500,000 stop-loss premium with a contractual "
                    "3% commission produces $15,000 gross commission before any contractual "
                    "sharing. Neither premium nor alleged employer savings becomes operator "
                    "revenue. Where evidence is weak, offer a fixed-scope inventory instead "
                    "of an outcome fee. Preserve a written reason to abandon each play "
                    "when the incumbent arrangement already meets the employer's needs."
                ),
            ],
            "table": {
                "caption": "First Seven Mapped Plays: Public Signals, Unit Economics, and Practical Fallbacks",
                "headers": [
                    "Mapped sourcing play and observable entry signal",
                    "Evidence request that establishes commercial fit",
                    "Illustrative unit economics and revenue boundary",
                    "Failure mode and concrete fallback action",
                ],
                "rows": [
                    [
                        "EDGAR executive triggers through sec_edgar_8k_vendor_trigger_arbitrage and relevant employer events",
                        "Confirm accession details, employer identity, executive role, and renewal responsibility",
                        "Forty reviewed events yield eight qualified accounts and two conversations",
                        "Throttle at five requests per second; mirror available bulk archives nightly",
                    ],
                    [
                        "Form 5500 renewal targeting using dated health contract information",
                        "Verify twelve renewal dates from thirty-six hypotheses across 120 employers",
                        "Two mandates at $4,000 each produce $8,000 diagnostic fees",
                        "Missing filings shift research toward employer websites and authorized introductions",
                    ],
                    [
                        "Schedule A/C compensation discovery using reported service relationships",
                        "Request current agreements and complete direct and indirect compensation disclosures",
                        "Six hundred employees times $4 PEPM produces $28,800 annually",
                        "Incomplete public schedules require contract review rather than undisclosed-fee accusations",
                    ],
                    [
                        "Acquisition census reconciliation following a verified operating business combination",
                        "Obtain authorized counts, coverage classes, duplicate vendors, and renewal calendars",
                        "Eight hundred employees times $3 PEPM produces $28,800 annually",
                        "Unsettled integration plans support a fixed inventory instead of replacement",
                    ],
                    [
                        "NADAC benchmark repricing where contract terms permit meaningful drug comparisons",
                        "Obtain NDC, quantity, service date, channel, fees, and eligibility fields",
                        "Twelve thousand normalized fills times $2 difference suggests $24,000 exposure",
                        "Benchmark mismatch requires channel segmentation before presenting any savings estimate",
                    ],
                    [
                        "PBM rebate reconciliation against executed guarantees and eligible utilization",
                        "Request rebate schedules, exclusions, remittances, guarantees, and settlement timing",
                        "A $100,000 collected recovery times 20% yields $20,000 fees",
                        "Disputed definitions favor a paid reconciliation with no collection assumption",
                    ],
                    [
                        "Stop-loss renewal comparison triggered by attachment changes or laser notices",
                        "Obtain binding terms, exclusions, run-out provisions, disclosures, and claim history",
                        "A $500,000 premium times 3% produces $15,000 gross commission",
                        "Unacceptable lasers favor incumbent negotiation rather than a forced transition",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Win the timing advantage without manufacturing a savings story",
                "body": (
                    "Experienced operators sell a verifiable next step while preserving the "
                    "employer's existing service continuity."
                ),
                "items": [
                    "Compare amended Form 5500 filings before outreach; a revised Schedule A can invalidate the renewal date in a purchased lead list.",
                    "Link every EDGAR event to an actual employer operating unit; investment vehicles and special-purpose issuers often produce irrelevant alerts.",
                    "Keep the PBM contract definition beside each rebate calculation; an attractive benchmark cannot override excluded utilization or settlement language.",
                    "Ask for the current E-Mod worksheet and state bureau identity first; NCCI procedures do not govern every state's rating system.",
                ],
            },
        },
        {
            "heading": "2. Qualify recoverable economics before requesting sensitive records",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Use a 100-point qualification scorecard with six explicit components: "
                    "renewal or correction timing worth 20 points, verified economic exposure "
                    "worth 25, access to a budget owner worth 15, accessible contract "
                    "evidence worth 15, licensed delivery capacity worth 15, and workable "
                    "payment terms worth 10. Define full, partial, and zero credit in "
                    "the CRM rather than letting enthusiasm determine the score. Full "
                    "timing credit means a confirmed review window and enough implementation "
                    "time; a rumored renewal earns five points at most. Economic exposure "
                    "requires a defensible fee basis after delivery cost, not a large "
                    "premium alone. Work accounts scoring at least 75 immediately, nurture "
                    "60–74 with a dated document request, and close lower scores unless "
                    "new evidence changes the inputs. Hard stops override the total: no "
                    "authorized decision maker, missing required producer authority, or "
                    "pressure to conceal compensation. Maintain separate health and workers' "
                    "compensation tracks because the same employer can qualify for one "
                    "and fail the other. An expiring health renewal may be unsuitable "
                    "for transition while a documented payroll correction remains actionable. "
                    "Ask initially for aggregate counts, renewal dates, contract summaries, "
                    "and redacted worksheets. These establish fit without sending individual "
                    "claim information through a prospecting platform."
                ),
                (
                    "Treat the PBM wedge as a reconciliation problem before treating it "
                    "as a replacement sale. Normalize National Drug Codes, package units, "
                    "quantities, dispense dates, retail versus mail channels, and specialty "
                    "exclusions before comparing claims with CMS NADAC files. NADAC "
                    "benchmarks pharmacy acquisition costs for covered survey populations; "
                    "it is neither a universal contract price nor proof of unlawful "
                    "spread. An illustrative 12,000 eligible fills with a $2 modeled "
                    "difference creates $24,000 of employer exposure before dispensing "
                    "fees, rebates, administrative charges, and implementation costs. A "
                    "$4,000 diagnostic fee is operator revenue if earned; the $24,000 "
                    "is not. For rebate reconciliation, a verified $100,000 recovery "
                    "with a permitted 20% collection fee yields $20,000 only under "
                    "the executed scope and recognition terms. Check licensing and "
                    "conflicts before offering contingency pricing. Complete a business "
                    "associate agreement when the service relationship requires one, "
                    "restrict access by role, encrypt transfers, and define deletion "
                    "dates. A confidentiality agreement alone does not authorize every "
                    "disclosure. Use the minimum necessary information where that HIPAA "
                    "standard applies. If usable records cannot be released, deliver a "
                    "contract-definition audit using redacted examples and postpone claims "
                    "repricing. Keep all patient-level information outside outbound CRM "
                    "notes, demonstration spreadsheets, and email sequences."
                ),
                (
                    "Complete the remaining plays with independent evidence paths. TPA "
                    "service unbundling might support 400 employees at $5 PEPM, or "
                    "$24,000 annual advisory fees, only when the employer buys genuinely "
                    "separate work and disclosed compensation avoids hidden overlap. NCCI "
                    "E-Mod correction starts with the applicable worksheet, payroll periods, "
                    "loss runs, valuation dates, and carrier reporting history; changes "
                    "must follow the governing bureau's rules. A modeled $60,000 premium "
                    "refund and 25% permitted collection split yields $15,000, but no "
                    "receivable should be assumed from an analyst's estimate. Payroll "
                    "classification review examines actual duties and state rules rather "
                    "than searching for the cheapest code. A separate $40,000 collected "
                    "correction at 20% produces $8,000; exclude amounts already counted "
                    "in the E-Mod engagement. Partner-led demand comes from payroll "
                    "firms, benefits counsel, accountants, and licensed brokers with "
                    "noncompeting specialties. Ten partner conversations yielding three "
                    "introductions and one paid mandate is a testable planning ratio. "
                    "Do not pay insurance-related referral compensation before checking "
                    "the relevant state's licensing and payment restrictions. Where "
                    "contingency fees, referrals, or delegated administration create "
                    "unresolved authority issues, use a properly licensed delivery "
                    "partner or limit the engagement to an authorized fixed-fee analytical "
                    "scope without negotiating coverage or handling claims."
                ),
            ],
            "table": {
                "caption": "Remaining Four Plays and Three Qualification Controls That Protect Delivery Margin",
                "headers": [
                    "Mapped play or qualification control under review",
                    "Specific evidence needed before accepting the opportunity",
                    "Commercial threshold or illustrative unit calculation",
                    "Required fallback when the evidence fails",
                ],
                "rows": [
                    [
                        "TPA service unbundling based on duplicated or unmet operating work",
                        "Compare executed administrative agreements against actual employer service requirements",
                        "Four hundred employees times $5 PEPM produces $24,000 annually",
                        "Retain useful incumbent functions and price only genuinely separate services",
                    ],
                    [
                        "NCCI E-Mod correction using verified rating and loss reporting errors",
                        "Reconcile bureau worksheets, carrier loss runs, payroll periods, and valuations",
                        "A $60,000 collected refund times 25% produces $15,000 fees",
                        "Use the applicable state bureau process when NCCI does not govern",
                    ],
                    [
                        "Payroll classification review based on actual duties and auditable records",
                        "Match job descriptions, time records, classifications, and state allocation rules",
                        "A separate $40,000 collected correction times 20% produces $8,000",
                        "Exclude overlapping E-Mod recoveries and reject unsupported code substitution",
                    ],
                    [
                        "Partner-led diagnostic demand through complementary professional service relationships",
                        "Confirm employer permission, relevant expertise, conflicts, and referral payment rules",
                        "Ten partner conversations produce three introductions and one illustrative mandate",
                        "Use unpaid introductions when compensation authority has not been established",
                    ],
                    [
                        "Timing and economic exposure together determine forty-five possible points",
                        "Verify review deadlines and an evidence-backed fee basis after delivery costs",
                        "Twenty timing points plus twenty-five economic points anchor account priority",
                        "Nurture weak evidence until a dated operating event improves fit",
                    ],
                    [
                        "Buyer access and usable records together determine thirty possible points",
                        "Identify the signer and document authorized access to necessary records",
                        "Fifteen authority points plus fifteen evidence points support practical execution",
                        "Offer redacted contract analysis instead of demanding identifiable claim records",
                    ],
                    [
                        "Licensed capacity and workable payment terms determine twenty-five possible points",
                        "Verify state authority, contractor availability, collection terms, and compensation disclosure",
                        "Fifteen capacity points plus ten payment points complete the scorecard",
                        "Stop prohibited activity regardless of an otherwise attractive account score",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four pre-flight checks before a mandate becomes delivery work",
                "body": (
                    "Record the reviewer, evidence, and verification date for each check; "
                    "an account score never substitutes for these requirements."
                ),
                "items": [
                    "Verify active Life & Health or Property & Casualty producer authority for the relevant state and activity, plus any applicable TPA or consultant requirements.",
                    "Deliver applicable ERISA §408(b)(2)(B) direct and indirect compensation disclosures reasonably before the arrangement, renewal, or extension.",
                    "Confirm the employer's authorized signer, permitted records access, required business associate arrangements, and secure transfer method before receiving claim files.",
                    "For a coverage transition, compare specific and aggregate attachment points, lasers, exclusions, contract basis, run-out protection, and any RBP balance-bill defense obligations.",
                ],
            },
        },
        {
            "heading": "3. Run a measured outreach cadence that sells the smallest useful mandate",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Design outbound around one observed event, one bounded hypothesis, "
                    "and one low-friction request. For a verified acquisition, write: "
                    "'Your Item 2.01 filing describes the completed acquisition. If "
                    "the acquired workforce has separate benefit renewal dates, a "
                    "contract inventory can identify duplicated administration before "
                    "renewal. Would a twenty-minute scope call be useful?' Do not "
                    "claim knowledge of employee health, incumbent misconduct, or "
                    "undisclosed contract terms. On day zero, send a short business "
                    "email with the source link; on day two, place a manually "
                    "dialed business call; on day five, offer a one-page evidence "
                    "brief; on day nine, make a contextual LinkedIn connection request; "
                    "on day fourteen, close the sequence with a clear opt-out. "
                    "A sub-hour EDGAR alert deserves faster initial review, not "
                    "more aggressive follow-ups. Apply CAN-SPAM identification, accurate "
                    "headers, a valid postal address, and a functioning opt-out to "
                    "commercial email. Honor suppression centrally across contractors. "
                    "Avoid automated texts and prerecorded calls without reviewing "
                    "the applicable TCPA requirements and state rules. Track reply "
                    "quality rather than email opens, which are distorted by privacy "
                    "features and scanners. One useful response is worth more than "
                    "hundreds of unverified impressions. Keep the cadence at account "
                    "level so three contacts do not receive simultaneous copies."
                ),
                (
                    "Use a cohort funnel to distinguish insufficient demand from poor "
                    "execution. An illustrative first campaign begins with 300 raw "
                    "employer records, qualifies 180 against evidence and timing, "
                    "reaches 150 through valid contact paths, generates 30 positive "
                    "replies, books 18 discovery calls, secures ten authorized "
                    "diagnostics, and closes four paid mandates. That means 60% "
                    "raw-to-qualified, 83.3% qualified-to-reached, 20% reached-to-positive, "
                    "60% positive-to-discovery, 55.6% discovery-to-diagnostic, and 40% "
                    "diagnostic-to-mandate conversion. Overall raw-to-mandate conversion "
                    "is 1.33%. These are starting hypotheses, not industry benchmarks. "
                    "If half as many reached accounts respond positively and downstream "
                    "ratios hold, expect roughly two mandates, subject to small-sample "
                    "variation. Run weekly cohorts and display counts beside percentages. "
                    "A signed mandate counts as a win only when scope, price, "
                    "authority, and payment terms are executed; free calls and broker "
                    "appointments without billable scope do not count. At $1,800 "
                    "campaign cash cost and 36 owner hours valued internally at "
                    "$100, fully loaded acquisition cost is $5,400 divided by four, "
                    "or $1,350 per mandate. Four $4,000 diagnostics produce $16,000 "
                    "revenue before delivery costs, not annual recurring revenue. "
                    "Record both first-cash date and sales-cycle duration, because "
                    "signed work with delayed collections can exhaust a small "
                    "operator's working capital."
                ),
                (
                    "Support outbound with narrow inbound assets that reveal buying "
                    "intent without collecting health records. Publish a Form 5500 "
                    "renewal-date verification worksheet, a PBM rebate-definition "
                    "checklist, and an E-Mod evidence-request guide. Each should "
                    "offer a concrete diagnostic deliverable and identify the "
                    "required source documents. Use a simple website, a scheduling "
                    "tool, and HubSpot or a controlled spreadsheet for account "
                    "tracking; no stack purchase compensates for an unclear offer. "
                    "Host a twenty-minute session with a payroll firm on reconciling "
                    "job duties to audit records, then invite employers to request "
                    "a scoped review. Ten attendees requesting three follow-ups "
                    "and one paid diagnostic provide a measurable local experiment. "
                    "Keep referral economics separate from education and check "
                    "state restrictions before sharing insurance-related compensation. "
                    "Weeks one and two establish licenses, sources, assets, and "
                    "the first account cohort; weeks three through six test "
                    "messaging and deliver initial diagnostics; weeks seven "
                    "through twelve convert evidence into paid mandates; weeks "
                    "thirteen through twenty repeat only productive channels. "
                    "The objective is three to ten signed wins within two "
                    "to five months, with narrower scopes for the first "
                    "engagements. If delivery capacity is constrained, delay "
                    "new start dates openly instead of selling a savings "
                    "implementation the team cannot support."
                ),
            ],
            "table": {
                "caption": "Seven-Stage Acquisition Funnel with Explicit Denominators and Operator Responses",
                "headers": [
                    "Pipeline stage and illustrative cohort population",
                    "Conversion definition with the correct denominator",
                    "Evidence required before advancing the account",
                    "Operator action when progression falls below plan",
                ],
                "rows": [
                    [
                        "Raw employer universe contains three hundred distinct employer records",
                        "Starting denominator is three hundred deduplicated employers, not contact names",
                        "Store employer identity, source date, likely segment, and evidence link",
                        "Remove investment vehicles, duplicate subsidiaries, and unsupported employer identity matches",
                    ],
                    [
                        "Qualified universe contains one hundred eighty evidence-screened employer accounts",
                        "One hundred eighty divided by three hundred equals sixty percent",
                        "Verify relevant timing, economic hypothesis, and a plausible delivery path",
                        "Narrow the segment before purchasing additional broad contact lists",
                    ],
                    [
                        "Reached cohort contains one hundred fifty valid account contact paths",
                        "One hundred fifty divided by one hundred eighty equals 83.3%",
                        "Confirm valid delivery or completed contact without ignoring suppression requests",
                        "Repair contact quality and stop sequences on invalid addresses",
                    ],
                    [
                        "Positive replies contain thirty employers acknowledging a relevant operating issue",
                        "Thirty divided by one hundred fifty equals twenty percent",
                        "Record the stated issue and permission for a useful next step",
                        "Replace generic savings language with a verified event and bounded hypothesis",
                    ],
                    [
                        "Discovery meetings contain eighteen completed conversations with relevant employer stakeholders",
                        "Eighteen divided by thirty equals sixty percent of positive replies",
                        "Confirm authority, timing, economic scope, and a feasible evidence request",
                        "Shorten scheduling delays and clarify the proposed meeting deliverable",
                    ],
                    [
                        "Authorized diagnostics contain ten employers accepting a defined evidence review",
                        "Ten divided by eighteen equals 55.6% of completed discovery meetings",
                        "Document record permissions, scope boundaries, and any diagnostic payment terms",
                        "Reduce the initial record burden and offer redacted contract analysis",
                    ],
                    [
                        "Paid mandates contain four executed engagements with explicit commercial terms",
                        "Four divided by ten equals forty percent of authorized diagnostics",
                        "Require signed scope, fee basis, authorized signer, and collection schedule",
                        "Review objections and proof quality before discounting the delivery price",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Build and date the evidence queue",
                    "action": "Load the first 300 employer records and deduplicate by employer identity.",
                    "detail": "Attach Form 5500 or EDGAR evidence, verify public-source dates, and assign a specific sourcing play.",
                },
                {
                    "step": 2,
                    "title": "Score before sequencing",
                    "action": "Apply the six-part qualification score and separate immediate work from nurture.",
                    "detail": "Confirm licensing scope and contact suppression before releasing a human-reviewed message.",
                },
                {
                    "step": 3,
                    "title": "Sell a bounded evidence deliverable",
                    "action": "Use the fourteen-day cadence to book discovery and propose a defined diagnostic.",
                    "detail": "Specify required records, access controls, price, completion date, and the employer's decision after delivery.",
                },
                {
                    "step": 4,
                    "title": "Convert and inspect the cohort",
                    "action": "Execute paid mandates and review stage counts, delivery cost, and collections weekly.",
                    "detail": "Keep paid diagnostics, recurring advisory revenue, commissions, and contingent collections in separate ledger categories.",
                },
            ],
        },
        {
            "heading": "4. Resolve objections, protect the mandate, and reconcile retained revenue",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Handle incumbent resistance by separating evidence collection "
                    "from replacement authority. When the employer says the "
                    "broker already performs this work, ask for the relevant "
                    "deliverable and compare scope, timing, and compensation "
                    "without attacking the incumbent. Offer a joint review "
                    "or withdraw duplicated work. When the objection is "
                    "disruption, propose a renewal inventory or retrospective "
                    "reconciliation that leaves coverage unchanged. When the "
                    "employer demands guaranteed savings, define a paid "
                    "diagnostic with explicit assumptions and a decision "
                    "threshold rather than promising a result before seeing "
                    "contracts. For 'send your best rate,' explain that "
                    "premiums alone omit attachment points, lasers, exclusions, "
                    "contract basis, and run-out coverage. Stop-loss pricing "
                    "can look attractive while transferring materially more "
                    "risk to the employer. Reference-based pricing requires "
                    "specific consideration of provider access, balance-bill "
                    "support, and the contractual defense arrangement; it "
                    "is not simply a lower reimbursement percentage. If "
                    "the buyer refuses necessary evidence, narrow the "
                    "deliverable to what can be supported. Never request "
                    "a broker-of-record change merely to obtain a "
                    "conversation. Document the employer's decision criteria "
                    "before preparing alternatives so the proposal answers "
                    "a real buying question. A preserved relationship "
                    "with a useful future renewal date can be worth "
                    "more than an unsupported immediate sale."
                ),
                (
                    "Make the first mandate small enough to deliver "
                    "well and specific enough to enforce economically. "
                    "Define the employer entities, covered period, records "
                    "required, analytical method, exclusions, deliverables, "
                    "fee basis, termination terms, and correction process. "
                    "For recovery work, distinguish a modeled error, a "
                    "carrier-approved adjustment, a posted credit, and "
                    "cash actually received; define which event earns "
                    "the fee and how reversals are handled. Do not "
                    "let the operator receive premiums or claim funds "
                    "merely because the engagement involves insurance. "
                    "For covered group health brokerage or consulting "
                    "arrangements reasonably expecting at least $1,000 "
                    "in direct or indirect compensation, apply ERISA "
                    "§408(b)(2)(B) disclosure requirements, including "
                    "services, applicable fiduciary statements, compensation "
                    "sources, and payment manner. Deliver the disclosures "
                    "reasonably before entering, extending, or renewing "
                    "the arrangement, subject to the statute's specific "
                    "rules. Verify state requirements independently; an "
                    "ERISA plan does not erase producer or TPA "
                    "obligations. A $4,000 diagnostic with $1,200 "
                    "contractor cost and eight owner hours budgeted "
                    "at $100 has $2,000 contribution after those "
                    "delivery inputs, before acquisition and overhead. "
                    "If the fully loaded acquisition allocation is "
                    "$1,350, only $650 remains on that initial "
                    "engagement. Expand recurring work only when the "
                    "client receives a distinct ongoing service."
                ),
                (
                    "Reconcile the acquisition plan to the supplied "
                    "Formula v2.0 scorecard instead of inflating a "
                    "small pipeline into an annual result. Conservative "
                    "revenue of $120,000 less $81,600 total cost "
                    "produces $38,400 owner net profit at 32%; "
                    "Base revenue of $535,000 less $294,250 produces "
                    "$240,750 at 45.0%; Scaled revenue of $950,000 "
                    "less $399,000 produces $551,000 at 58%. "
                    "Conservative and Base use one full-time operator "
                    "plus three contractors; Scaled uses two full-time "
                    "people plus four contractors. The scorecard's "
                    "gross-revenue label refers here to retained "
                    "operator fees and commissions, not underlying "
                    "employer spending. Apply the ASC 606 principal-versus-agent "
                    "assessment to each arrangement; do not mechanically "
                    "net every subcontractor payment. Where the operator "
                    "acts as agent and retains 70% of $100,000 "
                    "fee billings, recognized retained revenue is "
                    "$70,000, with the other $30,000 excluded from "
                    "that revenue basis. Do not subtract the "
                    "$30,000 again as an operating cost. Employer "
                    "premiums, claim funds, and recovered principal "
                    "remain outside operator revenue. The startup "
                    "range is $8,000–$45,000 and monthly operating "
                    "range is $2,000–$11,000; neither replaces the "
                    "annual scenarios' all-in costs. Track actual "
                    "delivery labor, acquisition expense, insurance, "
                    "systems, and collection delays before increasing "
                    "outbound volume."
                ),
            ],
            "table": {
                "caption": "Objection Responses and Canonical Revenue Controls for the First Signed Mandates",
                "headers": [
                    "Buyer objection or operating control requiring resolution",
                    "Concrete response supported by the available evidence",
                    "Commercial action and measurable decision boundary",
                    "Failure fallback that preserves employer continuity",
                ],
                "rows": [
                    [
                        "The incumbent broker says this analysis is already included",
                        "Request the existing deliverable and compare its scope and completion date",
                        "Sell only a distinct gap with separately disclosed compensation",
                        "Conduct a joint review or withdraw genuinely duplicated advisory work",
                    ],
                    [
                        "The employer wants savings promised before releasing contract records",
                        "Explain which assumptions require contracts, enrollment, and normalized claim evidence",
                        "Offer a $4,000 diagnostic with explicit deliverables and decision criteria",
                        "Limit the work to supported evidence instead of inventing outcomes",
                    ],
                    [
                        "The employer fears disruption from changing coverage or administration",
                        "Separate retrospective reconciliation from prospective changes in vendors or coverage",
                        "Begin with a contract inventory that leaves current coverage unchanged",
                        "Defer implementation until required terms and service continuity are established",
                    ],
                    [
                        "The buyer compares stop-loss offers using quoted premium alone",
                        "Compare specific and aggregate attachment points, lasers, exclusions, and run-out",
                        "Advance only an option whose total risk allocation the employer understands",
                        "Negotiate incumbent terms when cheaper alternatives shift unacceptable claim exposure",
                    ],
                    [
                        "Conservative annual retained revenue must reconcile to the supplied scorecard",
                        "$120,000 revenue less $81,600 total costs produces $38,400 owner profit",
                        "The 32% margin supports one full-time operator and three contractors",
                        "Reduce unsupported acquisition spending rather than counting premiums as revenue",
                    ],
                    [
                        "Base annual retained revenue must reconcile to the supplied scorecard",
                        "$535,000 revenue less $294,250 total costs produces $240,750 owner profit",
                        "The 45.0% margin supports one full-time operator and three contractors",
                        "Reprice delivery scope if actual labor consumes the planned contribution",
                    ],
                    [
                        "Scaled annual retained revenue must reconcile to the supplied scorecard",
                        "$950,000 revenue less $399,000 total costs produces $551,000 owner profit",
                        "The 58% margin supports two full-time people and four contractors",
                        "Pause new starts when delivery capacity cannot support contracted service",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "The best first deal is a verified timing advantage converted into a paid, bounded evidence mandate.",
    "diagram_id": "diag-02",
    "action_checklist": [
        "Build a dated 300-employer universe from Form 5500 records and relevant EDGAR events, retaining source links and separating verified facts from hypotheses.",
        "Configure EDGAR accession deduplication, an identifying User-Agent, five-request-per-second token-bucket limits, backoff, and nightly mirroring of available historical archives.",
        "Apply the 100-point qualification score, verify state licensing scope, and assign each priority account one specific play rather than a bundle of speculative savings claims.",
        "Launch the fourteen-day account-level cadence with accurate business email identification, centralized suppression, manual calling, and a bounded diagnostic offer.",
        "Execute the first paid mandates with authorized records access, applicable compensation disclosures, secure transfer procedures, explicit fee triggers, and separate delivery scopes.",
        "Review weekly funnel counts, first-cash dates, acquisition cost, delivery contribution, and retained revenue against the exact Conservative, Base, and Scaled scorecard totals.",
    ],
    "statutory_citations": [
        {
            "title": "29 U.S.C. §1108(b)(2)(B) — Group health brokerage and consulting compensation disclosures",
            "url": "https://www.law.cornell.edu/uscode/text/29/1108",
            "relevance": "Defines covered service-provider arrangements, the compensation threshold, required disclosures, and timing requirements for covered group health plan services.",
        },
        {
            "title": "29 U.S.C. §1023 — Annual reports",
            "url": "https://www.law.cornell.edu/uscode/text/29/1023",
            "relevance": "Provides the annual-report framework underlying Form 5500 sourcing; public filing information must still be checked against current employer contracts.",
        },
        {
            "title": "45 CFR §164.502 — Uses and disclosures of protected health information",
            "url": "https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-E/section-164.502",
            "relevance": "Establishes permitted-use and disclosure requirements, including the minimum necessary standard where applicable to claim-record analysis.",
        },
        {
            "title": "45 CFR §164.504(e) — Business associate arrangements",
            "url": "https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-E/section-164.504",
            "relevance": "Specifies required contractual safeguards when the operator's role constitutes a business associate relationship.",
        },
        {
            "title": "15 U.S.C. §7704 — Requirements for commercial electronic mail",
            "url": "https://www.law.cornell.edu/uscode/text/15/7704",
            "relevance": "Supports accurate sender information, nondeceptive commercial messages, required identification and address information, and effective opt-out handling.",
        },
        {
            "title": "47 U.S.C. §227 — Restrictions on telephone equipment and certain calls",
            "url": "https://www.law.cornell.edu/uscode/text/47/227",
            "relevance": "Requires channel-specific review before using automated dialing, prerecorded calls, or text outreach; state requirements may impose additional restrictions.",
        },
        {
            "title": "17 CFR §230.503 — Filing of notice of sales",
            "url": "https://www.ecfr.gov/current/title-17/chapter-II/part-230/section-230.503",
            "relevance": "Establishes Form D notice requirements for specified Regulation D offerings; offering notices are timing signals rather than proof of available employer cash.",
        },
        {
            "title": "17 CFR §249.308 — Form 8-K current reports",
            "url": "https://www.ecfr.gov/current/title-17/chapter-II/part-249/section-249.308",
            "relevance": "Identifies the Form 8-K current-report framework used to source executive-change, material-agreement, and acquisition-completion triggers.",
        },
        {
            "title": "Texas Insurance Code §4001.051 — License required",
            "url": "https://statutes.capitol.texas.gov/Docs/IN/htm/IN.4001.htm#4001.051",
            "relevance": "Provides a concrete state licensing reference for regulated insurance activity in Texas; verify the relevant jurisdiction and activity before solicitation or negotiation.",
        },
    ],
}
