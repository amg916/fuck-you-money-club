from __future__ import annotations

CHAPTER_10 = {
    "id": "Q10",
    "chapter_id": "Q10",
    "chapter_number": 10,
    "question_number": 10,
    "slug": "freight-brokerage-automation-ai-scalable-distribution",
    "question_prompt": "How does a 3 FT + 2 C (5 people) freight brokerage team automate 70%+ of repetitive research, qualification, fulfillment, and traffic/deal acquisition while keeping human-in-the-loop QA?",
    "kicker": "Q10 / THE BIG MONEY PLAYBOOKS",
    "title": "Automation, AI Leverage & Scalable Distribution Flywheels",
    "subtitle": "Python Event Queues, Highway/RMIS Identity Checks, FMCSA Authority Controls, and Cash-Aware Freight Growth",
    "layout_template": "case_study_walkthrough",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #12, Freight Brokerage, ranks #25 with a Money-to-Manpower Score of "
        "62/100 because automation cannot erase carrier exposure, working-capital demands, "
        "or service accountability. This chapter maps eight operator plays: lane research, "
        "shipper qualification, carrier verification, load matching, shipment tracking, "
        "invoice reconciliation, targeted outbound, and lane-content referrals. A 3 FT + "
        "2 C pod routes routine evidence through Python workers while people retain "
        "pricing, identity exceptions, credit, claims, and payment decisions. The canonical "
        "annual owner-profit cases remain $30,000 Conservative, $165,000 Base, and $400,000 "
        "Scaled; gross shipper billings include carrier costs. Measure 70%+ automation "
        "against a fixed repetitive-work baseline, price every run including review "
        "labor, and expand distribution only when delivery reliability and cash headroom "
        "support the next shipper."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$1,000,000",
            "context": "Annual gross shipper billings, including carrier costs",
            "note": "3% net margin; $30,000 annual owner net profit; 3 FT + 2 C",
        },
        {
            "label": "Base",
            "value": "$3,000,000",
            "context": "Annual gross shipper billings, including carrier costs",
            "note": "5.5% net margin; $165,000 annual owner net profit; 3 FT + 2 C",
        },
        {
            "label": "Scaled",
            "value": "$5,000,000",
            "context": "Annual gross shipper billings, including carrier costs",
            "note": "8% net margin; $400,000 annual owner net profit; 4 FT + 3 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Assign eight plays to an evidence-first, five-person operating pod",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Start with a responsibility map rather than a chatbot subscription. "
                    "Candidate #12's eight mapped operator plays are organized here as lane "
                    "research, shipper qualification, carrier verification, load matching, "
                    "shipment tracking, invoice reconciliation, targeted outbound, and "
                    "lane-content referrals. These are operating labels for this chapter, "
                    "not eight independent businesses. Assign the first full-time operator "
                    "to shipper sales and credit coordination, the second to carrier "
                    "procurement and dispatch, and the third to billing, collections, and "
                    "exception ownership. One contractor maintains integrations and observability; "
                    "the other performs scheduled document and tracking support. Contractors "
                    "receive task-scoped access, not shared administrator credentials or "
                    "unrestricted banking permissions. Each play must produce a durable "
                    "artifact: a sourced lane brief, qualified account, verified carrier "
                    "packet, ranked match, milestone history, reconciled invoice, attributed "
                    "conversation, or referral record. Those artifacts feed the next play "
                    "through stable shipment and account identifiers. The pod stays small "
                    "because information moves without rekeying, not because responsibility "
                    "disappears. Maintain named primary and backup owners for every exception "
                    "queue, with coverage windows visible in the TMS. If nobody owns an "
                    "exception during an overnight pickup, automation has merely hidden "
                    "an unstaffed service promise."
                ),
                (
                    "Build the integration spine around the brokerage's TMS, such as "
                    "Rose Rocket or Tai where contracted APIs support the required actions. "
                    "A Python webhook receiver authenticates the provider's documented "
                    "signature, checks timestamp freshness where supported, and stores the "
                    "original event before returning success. Use hashlib and hmac for "
                    "applicable signature schemes, json for strict payload parsing, and "
                    "sqlite3 for a bounded single-host pilot queue; move concurrent production "
                    "workloads to a managed durable queue when operational requirements "
                    "exceed that design. An event record carries provider_event_id, shipment_id, "
                    "event_type, schema_version, received_at, source_reference, and processing_state. "
                    "Enforce a unique provider/event key and a separate business-action key "
                    "so redelivery cannot create another tender or payment instruction. "
                    "Workers write proposed changes to an outbox; a narrowly authorized "
                    "dispatcher applies approved actions. Keep external calls outside database "
                    "transactions and reconcile uncertain acknowledgments before retrying. "
                    "Treat attached documents and extracted text as untrusted data: an LLM "
                    "cannot follow instructions embedded in a rate confirmation or change "
                    "its own tool permissions. Store model version, prompt version, extracted "
                    "fields, and evidence locations with each proposal. This makes later "
                    "disputes explainable without allowing a language model to become the "
                    "system of record."
                ),
                (
                    "Define the 70% objective before selecting vendors. Sample two weeks "
                    "of repetitive research, qualification, fulfillment administration, and "
                    "acquisition work, recording task counts and median human handling "
                    "minutes. Freeze that task catalog for each measurement period so "
                    "automation cannot improve its apparent score by excluding difficult "
                    "loads. An illustrative weekly baseline contains 100 research tasks "
                    "at four minutes, 100 qualification tasks at six minutes, 200 fulfillment "
                    "tasks at six minutes, and 100 acquisition tasks at four minutes: "
                    "2,600 minutes total. If the corresponding residual handling, review, "
                    "and allocated maintenance times are 100, 180, 350, and 150 minutes, "
                    "the reduction is exactly 70%, or 1,820 minutes recovered. This is "
                    "a handling-time result, not proof that 70% of decisions are autonomous "
                    "or that payroll falls by 70%. Track straight-through completion, "
                    "review minutes, escaped errors, reopened exceptions, and service failures "
                    "separately. Count contractor repair time and manual spreadsheet rescues "
                    "against the automation result. Review a random sample of successful "
                    "runs as well as every material exception. Preserve broker transaction "
                    "records required by 49 CFR 371.3, including compensation and relevant "
                    "freight-charge records, for three years; choose additional retention "
                    "periods according to contracts and other applicable duties."
                ),
            ],
            "table": {
                "caption": "Eight Mapped Plays: Evidence Products, Human Ownership, and Release Conditions",
                "headers": [
                    "Mapped operator play and practical scope",
                    "Automation artifact produced for downstream use",
                    "Human owner and consequential decision retained",
                    "Release condition before downstream work proceeds",
                ],
                "rows": [
                    [
                        "Play one: research recurring lanes within the chosen niche",
                        "Source-linked lane briefs summarize equipment, seasonality, and facilities",
                        "Sales operator confirms fit against actual service coverage",
                        "Publish only briefs with dated sources and defensible assumptions",
                    ],
                    [
                        "Play two: qualify shippers before promising available capacity",
                        "Account packets combine contact evidence and credit-review inputs",
                        "Sales operator owns account acceptance and credit coordination",
                        "Release quoting only within documented account exposure limits",
                    ],
                    [
                        "Play three: verify carriers before any tender commitment",
                        "Highway or RMIS evidence joins official authority checks",
                        "Procurement operator resolves identity conflicts through independent callbacks",
                        "Release only after identity and required coverage checks",
                    ],
                    [
                        "Play four: match loads against verified carrier capacity",
                        "Ranked candidates expose equipment, timing, price, and exclusions",
                        "Procurement operator approves carrier selection and final rate",
                        "Tender only after refreshed eligibility and capacity confirmation",
                    ],
                    [
                        "Play five: track shipments and manage milestone exceptions",
                        "Timestamped milestones distinguish fresh telemetry from stale estimates",
                        "Dispatch owner handles missed appointments and material deviations",
                        "Send routine updates only from attributable current evidence",
                    ],
                    [
                        "Play six: reconcile invoices against contracted shipment evidence",
                        "Variance packets link confirmations, delivery documents, and invoice lines",
                        "Billing operator authorizes payable changes and cash release",
                        "Release payment only after identity and reconciliation controls",
                    ],
                    [
                        "Play seven: acquire accounts through targeted outbound sequences",
                        "Evidence-based drafts connect relevant lanes to shipper needs",
                        "Sales operator approves claims, recipients, and sequence limits",
                        "Send only after suppression checks and content review",
                    ],
                    [
                        "Play eight: compound lane content and customer referrals",
                        "Approved service evidence becomes useful pages and referral links",
                        "Sales operator approves publication and customer attribution permissions",
                        "Publish only supported claims without confidential shipment details",
                    ],
                ],
            },
        },
        {
            "heading": "2. Automate matching and tracking without automating carrier trust",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Load matching begins with deterministic eligibility, followed by ranking. "
                    "Normalize origin and destination geography, pickup and delivery windows, "
                    "equipment, commodity, weight, temperature requirements, and shipper-specific "
                    "restrictions into typed fields. Reject missing hard constraints rather "
                    "than asking a model to invent them. Query contracted DAT or "
                    "Truckstop services only through permitted access methods; feed candidates "
                    "through Highway or RMIS evidence and the brokerage's own carrier "
                    "history. Confirm official authority and relevant filings through FMCSA "
                    "sources, while recognizing that a valid USDOT or MC number alone "
                    "does not establish the identity of the person offering the truck. "
                    "Rank eligible carriers using quoted buy rate, historical punctuality, "
                    "equipment fit, geographic relevance, and evidence freshness. An LLM "
                    "may summarize why three candidates fit, but the explanation must "
                    "cite stored inputs and cannot reverse a hard exclusion. The procurement "
                    "operator confirms capacity, identity continuity, and commercial terms "
                    "before tendering. Recheck material signals at tender time because "
                    "yesterday's verified packet may no longer describe today's contact, "
                    "authority status, or payment destination. Log both rejected and selected "
                    "candidates so post-loss reviews can reconstruct what was visible when "
                    "the decision was made."
                ),
                (
                    "Double-brokering defense requires binding the carrier identity to the "
                    "actual pickup, not merely collecting more documents. Compare the "
                    "tender contact, established phone channel, email domain, dispatch "
                    "instructions, named carrier, and payment beneficiary. Independently call "
                    "a previously established number when a contact or bank account "
                    "changes; never use only the number supplied in the change request. "
                    "Ask the shipper's pickup team to record the arriving carrier identity "
                    "and report discrepancies before releasing freight under the agreed "
                    "operating procedure. A photo, insurance certificate, or portal screenshot "
                    "is supporting evidence, not self-authenticating proof. Verify insurance "
                    "through independently established channels and distinguish required "
                    "filings from contractual cargo coverage and commodity exclusions. "
                    "Place conflicting identities, unexplained reassignments, and urgent "
                    "payment changes into a held state with a named resolver. U.S. "
                    "property brokers generally require FMCSA registration under 49 U.S.C. "
                    "13904 and $75,000 bond or trust security under 49 CFR 387.307; "
                    "verify current rules, accepted instruments, and filing status before "
                    "operating. That security does not establish a carrier's cargo coverage "
                    "or fund the brokerage's ordinary carrier-pay cycle. Keep identity "
                    "controls independent from sales urgency and from the model's confidence "
                    "language, which measures neither authority nor honesty."
                ),
                (
                    "Shipment tracking uses the same event spine but different decision "
                    "rights. Accept supported project44, FourKites, carrier API, or contracted "
                    "tracking feeds, and label each milestone with observed_at, received_at, "
                    "source, location precision, and freshness. Distinguish an observed arrival "
                    "from a predicted arrival and a driver's message from independent "
                    "location evidence. Compute lateness against appointment windows with "
                    "explicit time zones; preserve the original timestamp and normalize "
                    "processing to UTC. An LLM can turn verified milestones into concise "
                    "shipper updates, but it cannot convert an estimate into a delivered "
                    "status or declare cargo undamaged. Suppress automatic reassurance when "
                    "telemetry becomes stale, route diversions appear, or facility evidence "
                    "conflicts. Route those cases to dispatch with the last reliable event "
                    "and a recommended next contact. Use bounded retries with jitter for "
                    "transient outages, then move failed events to a dead-letter queue "
                    "with an alert and manual recovery instructions. During a tracking "
                    "provider outage, switch to scheduled carrier check calls and shipper "
                    "appointment confirmation, marking updates as manually sourced. After "
                    "restoration, replay events in shipment sequence without duplicating "
                    "notifications. Test this fallback before selling continuous visibility "
                    "to accounts whose appointment penalties make silence expensive."
                ),
            ],
            "table": {
                "caption": "Carrier and Tracking Failure Modes: Detection, Containment, and Recovery",
                "headers": [
                    "Failure pattern observed during shipment execution",
                    "Evidence that triggers a controlled exception",
                    "Immediate containment action assigned to humans",
                    "Recovery evidence required before normal processing",
                ],
                "rows": [
                    [
                        "A known carrier requests an urgent beneficiary change",
                        "Payment details differ from the previously verified master",
                        "Billing freezes the change and procurement contacts established dispatch",
                        "Independent confirmation and dual review document the authorized beneficiary",
                    ],
                    [
                        "Pickup personnel report a different arriving carrier identity",
                        "Facility records conflict with the approved tender identity",
                        "Dispatch requests a pickup hold under agreed facility procedures",
                        "Documented identity resolution precedes any revised release instruction",
                    ],
                    [
                        "A matching worker receives an incomplete equipment requirement",
                        "Required equipment field fails deterministic shipment schema validation",
                        "Procurement asks the shipper for the missing constraint",
                        "Corrected shipment requirements support a fresh eligible-carrier ranking",
                    ],
                    [
                        "Tracking provider returns stale positions during active transit",
                        "Observed timestamps exceed the lane-specific freshness operating threshold",
                        "Dispatch initiates carrier check calls and labels manual updates",
                        "Fresh attributable events reconcile with manually collected milestone history",
                    ],
                    [
                        "Provider redelivery repeats an already processed shipment milestone",
                        "Stored provider identifier matches an existing successful event",
                        "Worker records duplicate receipt without sending another notification",
                        "Existing business-action record confirms the intended notification outcome",
                    ],
                    [
                        "A delivery estimate conflicts with actual facility evidence",
                        "Predicted arrival disagrees with signed or confirmed receiving information",
                        "Dispatch suppresses reassurance and contacts the receiving facility",
                        "Resolved appointment status replaces the estimate with attributable evidence",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Make fraud expensive before making dispatch fast",
                "body": (
                    "Experienced operators preserve independent evidence channels and make "
                    "exception ownership visible before increasing load volume."
                ),
                "items": [
                    "Store verified callback numbers separately from incoming documents; a forged packet must not replace the channel used to authenticate itself.",
                    "Refresh carrier eligibility immediately before tendering, especially after contact, ownership, authority, or payment changes.",
                    "Give pickup facilities a short discrepancy script naming the expected carrier and the dispatch number for resolving mismatches.",
                    "Measure check-call workload by lane and tracking provider; apparently cheap visibility becomes costly when operators repeatedly repair stale feeds.",
                ],
            },
        },
        {
            "heading": "3. Reconcile money, meter automation, and protect the carrier-pay float",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Invoice reconciliation should compare evidence, not merely extract "
                    "invoice totals. Ingest the shipper agreement, carrier rate confirmation, "
                    "bill of lading, proof of delivery, accessorial approvals, carrier "
                    "invoice, and shipper invoice into a shipment-linked document register. "
                    "Use OCR where necessary, then require extracted amounts, dates, "
                    "reference numbers, and line items to point back to document pages. "
                    "Python decimal arithmetic handles money; binary floating-point "
                    "rounding must not decide a payable variance. Match base freight "
                    "against the signed confirmation, accessorials against required "
                    "supporting evidence, and delivery status against attributable receipt "
                    "information. A missing signature, disputed detention period, duplicate "
                    "invoice number, or changed beneficiary creates a review task rather "
                    "than an automatic payment. LLM output can draft the discrepancy "
                    "message but cannot amend the agreed rate or release cash. Keep "
                    "claims in a separate case record linked to the shipment. The "
                    "Carmack framework in 49 U.S.C. 14706 addresses covered carrier "
                    "liability; do not mechanically assign every cargo loss to the "
                    "broker or assume contract labels settle the broker's role. Where "
                    "49 CFR Part 370 applies, capture written claim particulars and "
                    "supporting evidence instead of treating a delivery exception note "
                    "as a complete claim."
                ),
                (
                    "Price an automated run as a complete operating event. An illustrative "
                    "LLM extraction consumes 6,000 input tokens at $2 per million and "
                    "1,000 output tokens at $8 per million, producing $0.020 in model "
                    "cost. Add $0.015 for OCR, $0.005 for queue and storage operations, "
                    "and $0.010 in allocated provider expense: $0.050 before human review. "
                    "These are budgeting assumptions, not vendor quotations; replace them "
                    "with contracted rates and actual invoice allocations. If 10% of "
                    "runs require four minutes of review at a loaded $30 hourly "
                    "rate, average review cost is $0.200 per run and combined cost "
                    "is $0.250. At 2,000 monthly runs, that is $500 and roughly "
                    "13.3 review hours. Reserve another $100 monthly for engineering "
                    "maintenance, making the planning total $600, or $0.300 per run. "
                    "Meter retries, failed calls, and document pages rather than counting "
                    "only successful responses. Allocate fixed TMS and verification "
                    "subscriptions separately unless the provider allocation already "
                    "includes them. Compare the full workload cost with measured manual "
                    "handling time and escaped-error losses. Cheap tokens do not rescue "
                    "a workflow that doubles disputes or consumes a senior operator's "
                    "afternoon correcting unsupported extraction results."
                ),
                (
                    "Keep automation economics separate from the canonical brokerage "
                    "scorecard. Conservative gross shipper billings are $1,000,000 at "
                    "3% net margin, producing $30,000 owner net profit with 3 FT + "
                    "2 C. Base is $3,000,000 at 5.5%, producing $165,000 with the "
                    "same pod. Scaled is $5,000,000 at 8%, producing $400,000 with "
                    "4 FT + 3 C, seven people rather than five. These billings "
                    "include carrier costs; they are not all retained brokerage fees, "
                    "and accounting presentation can differ. For an illustrative Base "
                    "bridge, 1,200 loads billed at $2,500 generate $3,000,000; carrier "
                    "purchases of $2,150 per load total $2,580,000. The resulting "
                    "$420,000 spread less $255,000 of other costs leaves exactly "
                    "$165,000. Include automation inside those costs, not as an extra "
                    "unreconciled profit claim. If carriers are paid at day 21 and "
                    "shippers pay at day 45, a steady-state 24-day carrier-cost gap "
                    "requires about $169,644 using $2,580,000 divided by 365 times "
                    "24. This excludes seasonality and loss reserves. Track cash "
                    "headroom, receivable aging, and shipper concentration before accepting "
                    "additional freight; faster booking can otherwise accelerate a "
                    "liquidity shortage while the income statement still looks profitable."
                ),
            ],
            "table": {
                "caption": "Illustrative Base Economics and Cash Controls Reconciled to the Canonical Scorecard",
                "headers": [
                    "Economic component and explicit calculation basis",
                    "Illustrative amount with substantive operating interpretation",
                    "Measurement source and responsible operating owner",
                    "Control preventing misleading profit or cash conclusions",
                ],
                "rows": [
                    [
                        "Annual gross billings equal twelve hundred loads times $2,500",
                        "$3,000,000 includes purchased transportation rather than retained fees",
                        "Billing owner reconciles shipper invoices with shipment records",
                        "Report carrier purchases separately from the brokerage's retained spread",
                    ],
                    [
                        "Carrier purchases equal twelve hundred loads times $2,150",
                        "$2,580,000 represents transportation purchases supporting those shipper billings",
                        "Procurement and billing reconcile accepted confirmations against payables",
                        "Investigate accessorial variances before treating forecast spread as earned",
                    ],
                    [
                        "Gross spread subtracts carrier purchases from shipper billings",
                        "$420,000 remains before payroll, systems, losses, and other costs",
                        "Billing owner maintains a shipment-level realized spread report",
                        "Keep spread terminology distinct from annual owner net profit",
                    ],
                    [
                        "Other costs consume the remaining reconciled operating expense envelope",
                        "$255,000 includes automation and all other modeled operating costs",
                        "Owner reconciles the expense ledger to the scenario bridge",
                        "Revise assumptions if staffing and losses exceed this envelope",
                    ],
                    [
                        "Base owner profit subtracts other costs from gross spread",
                        "$165,000 exactly equals the canonical 5.5% net margin",
                        "Owner reviews closed-period results rather than booking projections",
                        "Do not add modeled automation savings twice to profit",
                    ],
                    [
                        "Carrier funding gap uses annual purchases and twenty-four days",
                        "About $169,644 funds the illustrative steady-state timing mismatch",
                        "Billing owner maintains a weekly dated cash forecast",
                        "Add stress reserves for late payers and seasonal peaks",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four pre-flight checks before increasing automated throughput",
                "body": (
                    "Keep consequential actions held until the assigned operator records "
                    "the following evidence in the shipment or account record."
                ),
                "items": [
                    "Verify current FMCSA broker authority, required $75,000 security, and applicable filing status through official records before accepting brokerage work.",
                    "Confirm carrier identity continuity, required coverage, tender terms, and independently verified payment details before releasing shipment instructions or money.",
                    "Reconcile the shipment's commercial documents and resolve material amount, delivery, or duplicate-invoice exceptions before authorizing payment.",
                    "Confirm shipper credit capacity and stressed carrier-pay cash headroom before allowing an acquisition sequence to create additional accepted load volume.",
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Register immutable source evidence",
                    "action": "Attach original documents and provider events to stable shipment identifiers.",
                    "detail": "Record receipt time, source reference, document digest, and access scope before extracting or transforming fields.",
                },
                {
                    "step": 2,
                    "title": "Validate proposed operational changes",
                    "action": "Run deterministic schema, identity, arithmetic, and duplicate checks before routing proposals.",
                    "detail": "Separate missing evidence from contradictory evidence, and give each exception a named owner and resolution deadline.",
                },
                {
                    "step": 3,
                    "title": "Authorize consequential execution",
                    "action": "Require the responsible operator to approve tender, credit, disputed charges, and payment decisions.",
                    "detail": "Store the reviewer, evidence version, approved values, and business-action identifier before the dispatcher applies the action.",
                },
                {
                    "step": 4,
                    "title": "Reconcile results and rehearse recovery",
                    "action": "Confirm downstream acknowledgments, sample completed runs, and replay a controlled failed event.",
                    "detail": "Verify that retries do not duplicate tenders, notifications, invoices, or payment instructions and that manual fallback remains usable.",
                },
            ],
        },
        {
            "heading": "4. Compound niche distribution only as fast as verified service capacity",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Programmatic distribution starts with service knowledge the brokerage "
                    "can actually defend. Turn approved lane briefs into useful pages "
                    "covering equipment fit, appointment preparation, seasonal constraints, "
                    "and document requirements for the chosen niche. Generate structured "
                    "drafts from a controlled template and source register, not thousands "
                    "of interchangeable city pages. Python can assemble static HTML, "
                    "validate internal links, and produce sitemap entries; an LLM can "
                    "compress operator notes into readable explanations. A human verifies "
                    "every material service claim and removes customer names, negotiated "
                    "rates, facility vulnerabilities, and shipment identifiers unless "
                    "publication is explicitly authorized. Publish original observations "
                    "with measurement periods and sample sizes, and separate historical "
                    "performance from future commitments. Attribute visits through first-party "
                    "campaign parameters and connect qualified inquiries to account and "
                    "shipment identifiers in the CRM. The loop is specific: a useful "
                    "lane page attracts an inquiry, a qualified account produces completed "
                    "loads, verified service results improve the page, and that evidence "
                    "supports the next relevant inquiry. Measure contribution from collected "
                    "business, not page count or search impressions. If a lane lacks "
                    "reliable capacity, pause its acquisition page rather than allowing "
                    "marketing to sell coverage the procurement operator cannot consistently "
                    "deliver."
                ),
                (
                    "Targeted outbound should reuse the same lane evidence rather than "
                    "inventing a second research department. Build a small account universe "
                    "from permitted company sources, trade directories, and existing "
                    "customer referrals. Capture why each company plausibly fits the "
                    "niche, who owns the relationship, and when the source was checked. "
                    "An LLM drafts a short, specific message about an observable "
                    "shipping need; it must not fabricate a conversation, customer "
                    "endorsement, available truck, or confidential shipping schedule. "
                    "The sales operator approves batches, monitors replies, and removes "
                    "irrelevant accounts. For U.S. commercial email, implement the "
                    "requirements of 15 U.S.C. 7704, including accurate routing information, "
                    "nondeceptive subject lines, required sender information, and a working "
                    "opt-out process honoring requests within ten business days. Apply "
                    "suppression before every send, including contractor campaigns. Keep "
                    "automated calls and texts outside this pipeline unless a separately "
                    "reviewed process addresses applicable requirements. Make referrals "
                    "easy through a shipper-approved introduction link after successful "
                    "service, not by exposing live shipment tracking publicly. The viral "
                    "mechanism is a useful introduction between relevant operators, not "
                    "an incentive to broadcast sensitive load details. Record referral "
                    "source, qualified opportunities, collected spread, and support burden "
                    "so apparent growth can be evaluated against actual contribution."
                ),
                (
                    "Scale through controlled cohorts with explicit stop conditions. "
                    "Run a small lane and shipper cohort in shadow mode, comparing "
                    "proposed matches, status updates, and invoice outcomes with operator "
                    "decisions before enabling routine writes. Release low-consequence "
                    "actions first, such as internal research packets and verified "
                    "milestone drafts, then expand only after measured quality holds. "
                    "Set workflow-specific limits for escaped errors, stale events, "
                    "exception age, and review minutes; a changed model or provider "
                    "schema returns the affected workflow to shadow comparison. Keep "
                    "a versioned prompt and rule registry, a rollback switch, and "
                    "a daily reconciliation of received events against completed actions. "
                    "The integration contractor owns repairs, but the full-time process "
                    "owner decides whether service can continue manually. Review "
                    "acquisition and operations together each week: qualified inquiries, "
                    "accepted loads, on-time milestones, realized spread, cash collections, "
                    "and unresolved claims belong on one scorecard. Do not extrapolate "
                    "the five-person Base pod indefinitely. The canonical Scaled case "
                    "explicitly adds one full-time operator and one contractor, reaching "
                    "4 FT + 3 C. Add that capacity when coverage and exception "
                    "loads require it, not after service failures force emergency hiring. "
                    "A distribution flywheel compounds only when each new account "
                    "strengthens evidence, margin quality, and operating resilience."
                ),
            ],
            "table": {
                "caption": "Distribution Flywheel Controls: Useful Evidence, Measurable Conversion, and Stop Conditions",
                "headers": [
                    "Distribution asset or recurring acquisition mechanism",
                    "Evidence required before external publication or sending",
                    "Commercial measure tied to actual operating results",
                    "Stop condition and practical human recovery action",
                ],
                "rows": [
                    [
                        "Niche lane pages explain realistic equipment and appointment requirements",
                        "Procurement validates coverage claims against current service capability",
                        "Track qualified inquiries that become collected profitable shipments",
                        "Pause promotion when reliable capacity or service coverage deteriorates",
                    ],
                    [
                        "Targeted email batches connect observed needs with relevant services",
                        "Sales verifies source relevance and current suppression status",
                        "Track reply quality, accepted accounts, and collected contribution",
                        "Stop sequences when objections reveal poor targeting or unsupported claims",
                    ],
                    [
                        "Customer introduction links simplify relevant peer referrals after delivery",
                        "Account owner confirms permission and removes sensitive shipment information",
                        "Measure referred account quality and subsequent support burden",
                        "Withdraw public material if attribution permission changes or details leak",
                    ],
                    [
                        "Service case studies summarize verified outcomes within a defined period",
                        "Operator checks sample size, exclusions, and customer publication authorization",
                        "Connect assisted opportunities to realized spread after collection",
                        "Revise claims when newer results no longer support positioning",
                    ],
                    [
                        "CRM follow-up tasks reactivate accounts with suitable recurring lanes",
                        "Sales checks relationship ownership, credit status, and lane readiness",
                        "Measure repeat loads alongside concentration and overdue receivables",
                        "Hold new commitments when account exposure exceeds documented limits",
                    ],
                    [
                        "Weekly cohort reviews coordinate marketing pace with operational capacity",
                        "Owners reconcile event completion, exception age, and cash forecasts",
                        "Track collected contribution per combined operating and acquisition hour",
                        "Reduce acquisition volume before backlog or funding pressure harms service",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "Automate the evidence trail, keep judgment accountable, and let collected freight profit set the speed of growth.",
    "diagram_id": "diag-02",
    "action_checklist": [
        "Assign all eight mapped plays to the 3 FT + 2 C pod, with named exception owners, backups, and documented coverage windows.",
        "Baseline repetitive task minutes for two weeks and measure residual review, maintenance, and rework against the same fixed task catalog.",
        "Implement authenticated event ingestion, idempotent business-action keys, an approval-backed outbox, and a tested dead-letter recovery procedure.",
        "Refresh carrier identity and eligibility before tendering; independently verify contact or beneficiary changes and coordinate pickup discrepancy handling.",
        "Reconcile invoice evidence with decimal arithmetic and maintain a dated carrier-pay cash forecast that includes delayed shipper collections.",
        "Publish reviewed lane evidence and run suppression-checked outbound cohorts only while service quality, credit exposure, and cash headroom remain acceptable.",
    ],
    "statutory_citations": [
        {
            "title": "49 U.S.C. 13904 — Registration of brokers",
            "url": "https://www.law.cornell.edu/uscode/text/49/13904",
            "relevance": "Establishes the federal registration framework for brokers; verify applicable authority before conducting covered brokerage operations.",
        },
        {
            "title": "49 CFR 387.307 — Property broker and freight forwarder financial security",
            "url": "https://www.ecfr.gov/current/title-49/subtitle-B/chapter-III/subchapter-B/part-387/subpart-C/section-387.307",
            "relevance": "Provides the $75,000 property-broker bond or trust security requirement and related conditions; confirm current filings and instrument requirements.",
        },
        {
            "title": "49 CFR 371.3 — Records to be kept by brokers",
            "url": "https://www.ecfr.gov/current/title-49/subtitle-B/chapter-III/subchapter-B/part-371/section-371.3",
            "relevance": "Requires specified transaction records, three-year preservation, and access rights for parties to brokered transactions; design evidence storage accordingly.",
        },
        {
            "title": "49 U.S.C. 14706 — Liability of carriers under receipts and bills of lading",
            "url": "https://www.law.cornell.edu/uscode/text/49/14706",
            "relevance": "Supplies the carrier cargo-liability framework for covered transportation; preserve shipment evidence and assess actual roles rather than assuming broker liability.",
        },
        {
            "title": "49 CFR 370.3 — Filing of claims",
            "url": "https://www.ecfr.gov/current/title-49/subtitle-B/chapter-III/subchapter-B/part-370/section-370.3",
            "relevance": "Defines minimum claim-filing particulars for covered claims and distinguishes supporting shipment notations from a sufficient written claim.",
        },
        {
            "title": "15 U.S.C. 7704 — Requirements for transmission of messages",
            "url": "https://www.law.cornell.edu/uscode/text/15/7704",
            "relevance": "Governs U.S. commercial email practices, including routing accuracy, subject lines, required disclosures, opt-out mechanisms, and timely suppression.",
        },
    ],
}
