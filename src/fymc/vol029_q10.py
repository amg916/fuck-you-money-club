from __future__ import annotations

CHAPTER_10 = {
    "id": "Q10",
    "chapter_id": "Q10",
    "chapter_number": 10,
    "question_number": 10,
    "slug": "automation-ai-leverage-scalable-distribution-flywheels",
    "question_prompt": "How does a 2 FT + 2 C (4 people) insurance restoration team automate 70%+ of repetitive research, qualification, fulfillment, and traffic/deal acquisition while keeping human-in-the-loop QA?",
    "kicker": "Q10 / THE BIG MONEY PLAYBOOKS",
    "title": "Automation, AI Leverage & Scalable Distribution Flywheels",
    "subtitle": "Python Webhooks, IICRC Drying Evidence, Xactimate Supplements, Job-Cost Ledgers, and UPPA-Safe Referral Loops",
    "layout_template": "case_study_walkthrough",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #15, Insurance Restoration, ranks #13 with a Money-to-Manpower "
        "Score of 87/100 because trucks, drying equipment, skilled crews, and "
        "receivables remain stubbornly physical. This chapter maps five operator "
        "plays: emergency water mitigation, fire and smoke restoration, mold "
        "remediation, storm reconstruction, and documented rebuild closeout with "
        "collections. A 2 FT + 2 C pod automates dispatch preparation, evidence "
        "indexing, estimate research, cost reconciliation, and referral follow-up "
        "while people retain safety, scope, pricing, and customer decisions. "
        "Canonical annual owner profit remains $40,000 Conservative, $195,000 "
        "Base, and $450,000 Scaled; the Scaled case requires 3 FT + 3 C. "
        "The operating target is 70%+ straight-through completion of defined "
        "repetitive tasks, measured separately from labor savings and consequential review."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$500,000",
            "context": "Annual gross restoration billings; subcontractor and material costs included in margin",
            "note": "8% net margin; $40,000 annual owner net profit; 2 FT + 2 C",
        },
        {
            "label": "Base",
            "value": "$1,500,000",
            "context": "Annual gross restoration billings; subcontractor and material costs included in margin",
            "note": "13.0% net margin; $195,000 annual owner net profit; 2 FT + 2 C",
        },
        {
            "label": "Scaled",
            "value": "$2,500,000",
            "context": "Annual gross restoration billings; subcontractor and material costs included in margin",
            "note": "18% net margin; $450,000 annual owner net profit; 3 FT + 3 C, totaling 6 people",
        },
    ],
    "sections": [
        {
            "heading": "1. Allocate the five plays before automating the four-person pod",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Treat the five mapped plays as operating lanes rather than five "
                    "separate businesses: emergency water mitigation, fire and smoke "
                    "restoration, mold remediation, storm reconstruction, and documented "
                    "rebuild closeout with collections. This chapter uses those five "
                    "lanes to organize Candidate #15's property-restoration workflow. "
                    "Assign the five full-time seats to an owner-estimator, dispatcher, "
                    "field supervisor, restoration technician, and job-cost administrator. "
                    "Allocate the six contractor relationships across surge drying labor, "
                    "contents cleaning, demolition, carpentry, electrical work, and "
                    "specialist remediation, checking local licensing and actual "
                    "availability before dispatch. A contractor relationship is not a "
                    "promise of an available crew. The dispatcher owns response coverage; "
                    "the supervisor owns site safety and readings; the estimator owns "
                    "scope and price; the administrator owns purchase orders and "
                    "receivables. Automation may prepare each person's queue, but cannot "
                    "create additional licensed capacity. Build separate availability "
                    "fields for people, vehicles, air movers, dehumidifiers, and "
                    "containment equipment. A storm alert must not silently overbook "
                    "machines already committed to drying jobs. Track each lane's "
                    "accepted work, pending inspections, equipment-days, and cash "
                    "commitments in one daily capacity board. Reserve an explicit "
                    "after-hours escalation rotation instead of assuming the owner "
                    "will absorb every exception."
                ),
                (
                    "Start with a task census, not a claim that software replaces "
                    "seventy percent of restoration labor. Define one eligible task "
                    "as a bounded administrative operation with recorded inputs, an "
                    "acceptance test, and one completion event. Examples include "
                    "normalizing an address, checking a service radius, matching a "
                    "photo to a room, retrieving an approved estimating reference, "
                    "or matching a receipt to a purchase order. Exclude demolition, "
                    "drying judgment, hazard assessment, estimate approval, coverage "
                    "discussion, and contractual commitments from automatic completion. "
                    "Over two weeks, label attempts by play, role, duration, exception "
                    "reason, and downstream correction. Freeze that denominator before "
                    "reporting the automation rate; splitting one photo task into "
                    "twenty tiny events would manufacture progress. Use a seventy "
                    "percent target only for the eligible queue. Report mandatory "
                    "human reviews and total administrative minutes beside it. A "
                    "successful automatic match that later causes an invoice correction "
                    "must be reclassified in the quality report. Review a rotating "
                    "sample from every play, including quiet mold jobs and overnight "
                    "water calls. Otherwise, the dashboard rewards easy daytime "
                    "traffic while hiding the work most likely to damage customer "
                    "trust or consume scarce field capacity."
                ),
                (
                    "Implement the control plane with a Python webhook receiver, a "
                    "durable event table, a worker queue, and a reviewer inbox. Use "
                    "documented vendor APIs or permitted exports from tools such as "
                    "Encircle, CompanyCam, Xactimate, and QuickBooks Online; confirm "
                    "account entitlements instead of assuming each product exposes "
                    "every desired operation. Assign an internal job identifier "
                    "before attaching claim references. Store event identifier, "
                    "provider identifier, received time, payload hash, schema version, "
                    "job identifier, attempt count, and processing state. In a small "
                    "single-host prototype, Python's sqlite3 can enforce a unique "
                    "event key and commit state changes transactionally. Production "
                    "hosting must match concurrency, backup, and recovery requirements. "
                    "Validate webhook signatures with hmac.compare_digest where the "
                    "provider specifies HMAC verification; reject stale deliveries "
                    "using the provider's documented timestamp rules. Acknowledge "
                    "only after durable receipt, then process asynchronously. Keep "
                    "customer addresses, access codes, policy records, and interior "
                    "photos out of general diagnostic logs. Give workers narrowly "
                    "scoped service credentials, and record which human authorized "
                    "each outward-facing estimate or message. The system of record "
                    "remains the job file and accounting ledger, not an LLM "
                    "conversation or an automation vendor's transient execution history."
                ),
            ],
            "table": {
                "caption": "Five Restoration Plays and the Shared Pod Control Plane",
                "headers": [
                    "Operating lane and accountable human owner",
                    "Bounded automation with a recorded completion test",
                    "Human decision that remains outside automatic execution",
                    "Evidence required before the work advances",
                ],
                "rows": [
                    [
                        "Emergency water mitigation belongs to dispatcher and field supervisor",
                        "Prepare routing suggestions using available crews and equipment inventory",
                        "Supervisor assesses electrical hazards, contamination, and safe access conditions",
                        "Dispatch packet contains authorization, contact confirmation, and equipment reservation",
                    ],
                    [
                        "Fire and smoke restoration belongs to estimator and contents specialist",
                        "Index room photographs and draft contents inventory reconciliation exceptions",
                        "Qualified staff decide cleaning methods and item disposition recommendations",
                        "Room inventory preserves original photographs and customer disposition instructions",
                    ],
                    [
                        "Mold remediation belongs to supervisor and appropriately licensed specialists",
                        "Organize containment records, daily logs, and assessment document references",
                        "Qualified personnel determine remediation scope and applicable assessment separation",
                        "Job packet documents credentials, containment plan, and required verification",
                    ],
                    [
                        "Storm reconstruction belongs to estimator and scheduled trade contractors",
                        "Retrieve permit requirements and prepare measured scope comparison packets",
                        "Estimator approves quantities while authorized personnel approve contract commitments",
                        "Packet links measurements, permit status, subcontractor capacity, and signed scope",
                    ],
                    [
                        "Documented rebuild closeout and collections belong to job-cost administrator",
                        "Match invoices, completion evidence, payments, and customer balance reminders",
                        "Authorized staff resolve disputed charges without negotiating insurance coverage",
                        "Ledger distinguishes customer obligations, insurer payments, and disputed invoices",
                    ],
                    [
                        "Shared control plane belongs to owner with administrator backup",
                        "Deduplicate incoming events and route exceptions into named work queues",
                        "Owner assigns response coverage and reviews recurring automation failures",
                        "Audit trail preserves event origin, reviewer identity, and final disposition",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Verify four conditions before enabling automatic task completion",
                "body": (
                    "Enable one bounded workflow at a time; each condition must have "
                    "a named owner and retained test evidence."
                ),
                "items": [
                    "Confirm contractor and remediation credentials for the actual jurisdiction, and separate restoration scope work from activities requiring a public-adjuster license.",
                    "Replay duplicate and out-of-order webhook fixtures; verify exactly one internal task result and no duplicate customer message or equipment booking.",
                    "Test that missing moisture readings, unresolved hazards, and unreviewed supplement drafts stop at the assigned human review queue.",
                    "Restore a backup job file and demonstrate manual dispatch, paper field documentation, and later reconciliation before relying on the live pipeline.",
                ],
            },
        },
        {
            "heading": "2. Turn field evidence into reviewable dispatch, drying, and supplement packets",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "For water mitigation, the intake webhook should create a "
                    "provisional job, normalize the service address, check the service "
                    "area, and request a dispatcher decision. Ask about active water, "
                    "occupant access, visible electrical involvement, and immediate "
                    "contact availability without turning a chatbot into a remote "
                    "safety inspector. Potential electrical or structural danger "
                    "routes to a person and the appropriate emergency response "
                    "instructions, not an autonomous technician booking. After human "
                    "acceptance, the scheduler reserves a crew and equipment against "
                    "the same job identifier. Mobile uploads enter an evidence "
                    "pipeline that preserves originals, computes SHA-256 hashes "
                    "with hashlib, records capture and receipt times separately, "
                    "and attaches room and material tags. Optical character "
                    "recognition can draft meter values, but a technician confirms "
                    "instrument identity, units, location, and readings. Capture "
                    "temperature, relative humidity, material moisture, equipment "
                    "placement, and daily changes using the adopted IICRC S500 "
                    "documentation approach. Psychrometric calculations may flag "
                    "inconsistencies; they cannot manufacture missing measurements. "
                    "A plausible-looking drying curve assembled from guessed values "
                    "is worse than a visible gap. Route gaps to the supervisor "
                    "before drafting the daily customer update or deciding whether "
                    "equipment can be removed from site."
                ),
                (
                    "Use an LLM as a constrained drafting component between "
                    "deterministic checks, never as the authoritative evidence "
                    "store. Send only the minimum job material needed for the "
                    "task, with an approved retention arrangement and restricted "
                    "access. Require structured output containing job identifier, "
                    "source identifiers, extracted facts, proposed text, and "
                    "explicit exception codes. Python's json module can parse "
                    "the response; separate validation must enforce required "
                    "keys, permitted values, numeric ranges, and source existence. "
                    "Treat text inside photographs, emails, and uploaded reports "
                    "as evidence, not instructions capable of changing worker "
                    "permissions. For Xactimate supplements, retrieve the "
                    "authorized estimate export and applicable price-list "
                    "reference, then compare measured quantities, documented "
                    "equipment-days, demolition limits, and missing line-item "
                    "support. Do not let a model invent a line-item code, "
                    "inflate quantities, or infer coverage from a policy heading. "
                    "The estimator reviews a side-by-side packet showing original "
                    "scope, proposed change, evidence links, and arithmetic. "
                    "Restoration staff can explain their work and charges "
                    "within applicable rules; insurance claim representation "
                    "may require separate public-adjuster licensing. In Texas, "
                    "Insurance Code Section 4102.051 supplies a concrete licensing "
                    "boundary that the communication workflow must respect."
                ),
                (
                    "Build failure recovery into each state transition. Use "
                    "received, validated, drafted, awaiting_review, released, "
                    "and failed as explicit states rather than interpreting "
                    "a missing error message as success. Store the prompt "
                    "version, model identifier, evidence manifest, and accepted "
                    "output with each draft. Retry transient timeouts with "
                    "bounded exponential backoff and jitter; stop retrying "
                    "invalid credentials, malformed payloads, or prohibited "
                    "operations until a person resolves the cause. Move "
                    "exhausted jobs into an exception queue with a deadline "
                    "and accountable owner. An uncertain outbound delivery "
                    "requires reconciliation against the provider's message "
                    "record before another send. For offline fieldwork, retain "
                    "encrypted device records or controlled paper forms with "
                    "job and room identifiers, then reconcile timestamps "
                    "after connectivity returns. Never relabel upload time "
                    "as measurement time. For fire, mold, and storm work, "
                    "hazard exceptions remain visible alongside production "
                    "tasks: suspect asbestos disturbance invokes applicable "
                    "29 CFR 1926.1101 controls, and covered lead renovation "
                    "work follows 40 CFR 745.85. These conditions cannot "
                    "be cleared by a fluent summary. Review restored records "
                    "against the original site log before releasing an "
                    "estimate, drying report, or completion packet."
                ),
            ],
            "table": {
                "caption": "Evidence Pipeline Failure Modes and Human Recovery Actions",
                "headers": [
                    "Incoming event and expected evidence provenance",
                    "Deterministic check before accepting the proposed output",
                    "Named human review responsibility and consequential decision",
                    "Recovery procedure when the automated path fails",
                ],
                "rows": [
                    [
                        "Intake webhook contains customer contact and reported loss location",
                        "Verify signature, deduplicate event, and validate service address fields",
                        "Dispatcher confirms access arrangements and accepts the proposed response",
                        "Telephone the customer and record dispatch manually during integration outages",
                    ],
                    [
                        "Mobile photograph includes original file and assigned room identifier",
                        "Hash original bytes and reject cross-job attachment identifier mismatches",
                        "Field supervisor resolves ambiguous rooms and missing context photographs",
                        "Preserve unassigned files separately until the uploader confirms placement",
                    ],
                    [
                        "Meter reading includes instrument identity, units, and measurement location",
                        "Check valid numeric ranges without replacing missing field observations",
                        "Technician confirms extracted values before any drying interpretation occurs",
                        "Request a fresh measurement and preserve the original disputed entry",
                    ],
                    [
                        "Daily drying packet references readings and equipment placement history",
                        "Reconcile equipment-days against placement records and documented removal events",
                        "Supervisor decides continued drying requirements and equipment removal timing",
                        "Hold the report and contact field staff about conflicting records",
                    ],
                    [
                        "Supplement draft links estimate revision and supporting source documents",
                        "Recalculate quantities and verify every cited evidence identifier exists",
                        "Estimator approves construction scope, pricing, and customer-facing factual statements",
                        "Return unsupported line items for measurement rather than speculative expansion",
                    ],
                    [
                        "Completion packet contains signed scope and recorded work completion",
                        "Check attachment access and verify recipients against the job record",
                        "Administrator reviews balances while owner handles disputed completion assertions",
                        "Suspend automatic delivery and reconcile missing signatures with responsible staff",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Make the evidence cheaper to defend than to reconstruct",
                "body": (
                    "Veteran restoration teams design capture routines around the "
                    "questions an estimator, customer, or adjuster will ask later."
                ),
                "items": [
                    "Photograph the meter display together with room and material context, then retain a separate wide shot so an extracted number cannot drift between rooms.",
                    "Record each dehumidifier's placement and removal against its asset identifier; reconcile billed equipment-days before the supplement reaches the estimator.",
                    "Keep demolition boundary photographs before surfaces disappear, because a polished closeout album cannot recreate concealed conditions after reconstruction.",
                    "Version estimate exports and annotate changed quantities against source evidence; send reviewers the difference packet rather than another unmarked full estimate.",
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Receive and preserve the source event",
                    "action": "Validate origin and persist the event before acknowledging receipt.",
                    "detail": "Record the unique event key, payload hash, job identifier, and provider timestamp without exposing access codes in logs.",
                },
                {
                    "step": 2,
                    "title": "Validate facts before requesting a draft",
                    "action": "Check source ownership, required fields, units, and evidence completeness.",
                    "detail": "Route missing measurements or conflicting job identifiers to the supervisor instead of asking the model to fill gaps.",
                },
                {
                    "step": 3,
                    "title": "Review consequential outputs with linked evidence",
                    "action": "Present the draft, arithmetic, source links, and exceptions to the accountable person.",
                    "detail": "Require explicit review for dispatch acceptance, safety decisions, scope changes, supplement release, and disputed balance communications.",
                },
                {
                    "step": 4,
                    "title": "Release once and reconcile the result",
                    "action": "Record authorization, send through the approved channel, and verify delivery state.",
                    "detail": "Use provider idempotency support where available; reconcile uncertain outcomes before retrying and preserve the final released version.",
                },
            ],
        },
        {
            "heading": "3. Price every automated run and reconcile the canonical owner-profit cases",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Keep the scorecard intact while testing automation economics. "
                    "Conservative gross restoration billings are $500,000 at an "
                    "8% net margin, producing $40,000 annual owner net profit "
                    "with 2 FT + 2 C. Base billings are $1,500,000 at "
                    "13.0%, producing $195,000 with the same four-person "
                    "configuration. Scaled billings are $2,500,000 at 18%, "
                    "producing $450,000 with 3 FT + 3 C, thirteen people "
                    "rather than eleven. Corresponding total annual costs are "
                    "$460,000, $1,305,000, and $2,050,000. Subcontractor "
                    "and material costs already sit inside those margins. "
                    "Do not subtract them again or treat an insurer's "
                    "entire claim valuation as restoration revenue. As an "
                    "illustrative volume bridge only, an average $10,000 "
                    "recognized restoration invoice implies 50, 150, or "
                    "250 completed jobs respectively; actual mix will "
                    "vary sharply between mitigation and reconstruction. "
                    "Automation spending must fit within each case's "
                    "total cost envelope or be offset by measured "
                    "savings to preserve the stated profit. The "
                    "$18,000–$75,000 startup capital range and "
                    "$4,000–$20,000 monthly operating expense range "
                    "are planning inputs, not substitutes for a full "
                    "annual job-cost reconciliation. Equipment purchases "
                    "and collection delays also require a separate cash "
                    "schedule rather than optimistic margin arithmetic."
                ),
                (
                    "Use an illustrative batch of 1,000 eligible administrative "
                    "tasks to make the seventy percent target auditable. "
                    "Suppose 740 finish automatically and pass their "
                    "acceptance tests, while 260 require human review. "
                    "That is 74% straight-through completion, subject "
                    "to later correction findings. Assume each attempted "
                    "run consumes $0.025 of model inference, $0.006 "
                    "of orchestration, $0.009 of storage and transfer, "
                    "and $0.010 of monitoring allocation: $0.050 "
                    "per attempt, or $50 for the batch. These "
                    "are budgeting assumptions, not vendor quotations, "
                    "and exclude fixed implementation and subscription "
                    "charges. At three minutes per review and a "
                    "$40 hourly loaded rate, the 260 reviews "
                    "cost $520, making direct processing expense "
                    "$570, or $0.57 per attempted task. A "
                    "four-minute manual baseline would consume "
                    "66.67 hours. Thirteen review hours, five "
                    "exception-handling hours, and three maintenance "
                    "hours leave 21 hours of work, a 68.5% "
                    "time reduction rather than 74%. Cost those "
                    "additional eight hours at the same assumed "
                    "rate and the batch reaches $890 before "
                    "fixed charges. Count mandatory consequential "
                    "reviews wherever they occur; do not hide "
                    "them outside the labor ledger to improve "
                    "the automation headline."
                ),
                (
                    "Connect job-cost tracking to purchase orders, receipts, "
                    "time entries, equipment-days, subcontractor invoices, "
                    "and signed change orders using the internal job "
                    "identifier. QuickBooks Online can hold accounting "
                    "transactions while the operational board holds "
                    "field status, but one system must own each "
                    "editable fact. Use Python's decimal.Decimal for "
                    "money calculations, with explicit rounding rules, "
                    "rather than binary floating-point totals. Match "
                    "receipts deterministically on supplier, amount, "
                    "date window, and purchase-order reference before "
                    "asking a model to suggest an ambiguous match. "
                    "The administrator resolves exceptions and "
                    "reviews proposed postings; never let text "
                    "extraction create an unrestricted payment. "
                    "Track committed cost separately from posted "
                    "cost so an unbilled subcontractor does not "
                    "make a storm job appear unusually profitable. "
                    "Maintain customer receivables separately from "
                    "expected insurer disbursements, deposits, and "
                    "deductible obligations. For Texas projects "
                    "within Insurance Code Chapter 707, encode "
                    "the deductible requirement into reviewed "
                    "contract and collection workflows; do not "
                    "automate prohibited deductible waivers. "
                    "Trigger collection reminders from verified "
                    "contract balances, not model interpretations "
                    "of policy coverage. Escalate disputed scope "
                    "and payment allocation to the owner with "
                    "a complete evidence packet before any "
                    "new customer-facing assertion is released."
                ),
            ],
            "table": {
                "caption": "Canonical Economics and Illustrative Automation Cost Controls",
                "headers": [
                    "Scenario or operating measurement being evaluated",
                    "Revenue basis or explicitly bounded cost assumption",
                    "Reconciled result with the complete calculation context",
                    "Operator interpretation and required review discipline",
                ],
                "rows": [
                    [
                        "Conservative case retains five full-time staff and six contractors",
                        "Annual gross restoration billings equal the canonical $500,000 amount",
                        "Eight percent net margin produces $40,000 annual owner profit",
                        "Keep all annual costs within $460,000 to preserve this case",
                    ],
                    [
                        "Base case retains five full-time staff and six contractors",
                        "Annual gross restoration billings equal the canonical $1,500,000 amount",
                        "Thirteen percent net margin produces $195,000 annual owner profit",
                        "Reconcile labor, materials, subcontractors, and overhead within $1,305,000 annually",
                    ],
                    [
                        "Scaled case requires six full-time staff and seven contractors",
                        "Annual gross restoration billings equal the canonical $2,500,000 amount",
                        "Eighteen percent net margin produces $450,000 annual owner profit",
                        "Thirteen people support this case with $2,050,000 total annual costs",
                    ],
                    [
                        "Illustrative eligible batch contains one thousand attempted administrative tasks",
                        "Per-attempt variable infrastructure and model allocation totals five cents",
                        "One thousand attempts create fifty dollars of assumed machine expense",
                        "Add retries and fixed subscriptions before comparing actual operating budgets",
                    ],
                    [
                        "Illustrative human review queue contains two hundred sixty task exceptions",
                        "Three minutes each at forty dollars hourly creates $520 expense",
                        "Machine expense plus initial human review equals $570 per batch",
                        "Separate additional exception handling and maintenance from initial review cost",
                    ],
                    [
                        "Illustrative full batch labor includes review, exceptions, and routine maintenance",
                        "Twenty-one labor hours cost $840 at the assumed loaded rate",
                        "Adding fifty dollars machine expense produces $890 before fixed charges",
                        "Report 68.5% time reduction separately from 74% straight-through task completion",
                    ],
                ],
            },
        },
        {
            "heading": "4. Build evidence-led distribution loops that never outrun field capacity",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Build programmatic acquisition around verified operating "
                    "facts, not thousands of interchangeable disaster pages. "
                    "For each genuinely served municipality, maintain "
                    "response hours, available services, relevant permit "
                    "links, travel limits, and a reviewed contact route. "
                    "Python can assemble draft pages from approved "
                    "structured records, while a person verifies local "
                    "claims before publication. A useful water page "
                    "explains the intake sequence and drying "
                    "documentation; a fire page explains contents "
                    "inventory; a mold page explains assessment "
                    "and remediation roles; a storm page explains "
                    "temporary protection and reconstruction scheduling. "
                    "The fifth play contributes a closeout guide "
                    "covering documented scope, completion records, "
                    "and customer balances without promising coverage. "
                    "Index only pages with distinct local value. "
                    "Use Google Business Profile and Search Console "
                    "to observe discovery and demand, keeping "
                    "service areas and opening hours accurate. "
                    "Tie conversion events to qualified appointments "
                    "and completed jobs rather than raw form "
                    "submissions. When available equipment-days or "
                    "inspection slots fall below the dispatcher's "
                    "reserve, pause affected campaigns and show "
                    "honest availability. Software-generated demand "
                    "that cannot be served increases cancellations, "
                    "overtime, and reputation damage rather than "
                    "creating a scalable distribution advantage."
                ),
                (
                    "Create the referral loop from a reviewed closeout "
                    "packet: concise work summary, approved before-and-after "
                    "images, equipment history where useful, completion "
                    "confirmation, and a clear service contact. Obtain "
                    "customer authorization before publishing identifiable "
                    "property images or sharing a case study outside "
                    "the job's intended recipients. Offer a customer "
                    "a clean public link they may choose to "
                    "share; never expose a private claim portal "
                    "as the share destination. Ask for honest "
                    "feedback consistently, rather than soliciting "
                    "reviews only from customers predicted to be "
                    "happy. Avoid fabricated testimonials and "
                    "incentives conditioned on positive sentiment; "
                    "16 CFR Part 465 supplies concrete review "
                    "and testimonial restrictions. For outbound "
                    "growth, prioritize plumbers, property managers, "
                    "and facility operators within the service "
                    "area, using documented business contact "
                    "sources and individually relevant messages. "
                    "Commercial email workflows must implement "
                    "15 U.S.C. 7704 requirements, including "
                    "accurate routing information, required "
                    "identification, a valid postal address, "
                    "and functioning opt-out handling. Preserve "
                    "suppression lists across every campaign "
                    "tool. Automated calls and texts require "
                    "channel-specific review under applicable "
                    "47 U.S.C. 227 rules before activation; "
                    "a purchased contact list does not "
                    "establish the required permission."
                ),
                (
                    "Run distribution as a closed loop from source "
                    "to accepted inspection, signed scope, recognized "
                    "billings, collected cash, and resulting referral. "
                    "Store first-touch and partner identifiers "
                    "without overwriting them when a customer "
                    "returns through another channel. Report "
                    "qualified acquisition cost and collected "
                    "gross margin by play, alongside cancellation "
                    "rate and response time. A plumber referral "
                    "that converts into properly documented water "
                    "work may outperform cheap storm clicks "
                    "that consume estimator visits without "
                    "signed scopes. Feed those results into "
                    "weekly budget changes reviewed by the "
                    "owner, not autonomous bidding based "
                    "only on lead counts. Cap message "
                    "frequency, apply suppression immediately, "
                    "and inspect customer-facing drafts for "
                    "coverage promises, invented availability, "
                    "and unsupported drying claims. During "
                    "a storm surge, switch the dispatcher "
                    "to a simplified intake queue with "
                    "manual prioritization and prewritten "
                    "status updates. If an integration "
                    "fails, stop new automated releases "
                    "while preserving received inquiries "
                    "for telephone follow-up. Review the "
                    "five plays together each week: "
                    "which evidence reduced disputes, "
                    "which handoff delayed cash, which "
                    "referral produced profitable work, "
                    "and which exception consumed human "
                    "capacity. Scale the proven loop "
                    "only when the pod can absorb "
                    "the resulting physical work."
                ),
            ],
            "table": {
                "caption": "Distribution Flywheels Linked to Capacity, Evidence, and Collected Results",
                "headers": [
                    "Distribution loop and specific restoration entry point",
                    "Automated preparation using approved operating source records",
                    "Human release decision and customer protection requirement",
                    "Measurement that closes the loop without vanity reporting",
                ],
                "rows": [
                    [
                        "Local water mitigation pages connect nearby customers to dispatch",
                        "Generate drafts from verified service areas and response schedules",
                        "Dispatcher confirms current capacity before response claims become public",
                        "Measure accepted inspections and completed water jobs by originating page",
                    ],
                    [
                        "Fire restoration case studies explain contents documentation and cleaning",
                        "Assemble proposed image sequences from authorized closeout evidence records",
                        "Customer authorization and estimator review precede external case-study publication",
                        "Attribute qualified contents inquiries and collected project margin to publication",
                    ],
                    [
                        "Mold education pages explain assessment roles and remediation workflow",
                        "Prepare service explanations from approved credentials and jurisdiction records",
                        "Qualified reviewer verifies role separation and avoids unsupported health claims",
                        "Track appropriate assessments booked rather than undifferentiated educational page traffic",
                    ],
                    [
                        "Storm reconstruction outreach connects property managers with available inspections",
                        "Match documented business contacts to genuine service coverage and capacity",
                        "Owner reviews messages while dispatcher confirms inspection slots remain available",
                        "Compare signed reconstruction scopes against acquisition cost and estimator hours",
                    ],
                    [
                        "Closeout referral links let satisfied customers voluntarily share public material",
                        "Prepare shareable summaries without private claim records or identifying images",
                        "Administrator verifies customer authorization and requests honest feedback consistently",
                        "Connect referred jobs to completed work and collected gross margin",
                    ],
                    [
                        "Partner email follow-up keeps plumbers informed about actual service availability",
                        "Draft relevant updates and apply the shared opt-out suppression list",
                        "Owner reviews commercial messaging and checks partner relationship restrictions",
                        "Measure qualified partner introductions, response reliability, and resulting collected balances",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "Automate the evidence trail and the next safe handoff, never the judgment that makes a restoration job defensible.",
    "diagram_id": "diag-02",
    "action_checklist": [
        "Map the five restoration plays to the five full-time seats and six contractor relationships, then publish daily crew, equipment, and inspection capacity.",
        "Freeze a two-week eligible-task baseline with task identifiers, duration, correction counts, mandatory reviews, and explicit exclusions for physical work and consequential decisions.",
        "Build signed webhook intake, durable event storage, evidence hashing, structured draft validation, and a reviewer inbox; test duplicates, outages, and uncertain outbound delivery.",
        "Pilot photo indexing and receipt matching before supplement drafting, and require source-linked human review for scope, safety, customer commitments, and disputed balances.",
        "Reconcile automation expense inside the canonical $460,000, $1,305,000, and $2,050,000 annual cost envelopes, while tracking cash commitments and collections separately.",
        "Launch one verified local page and one reviewed referral workflow per appropriate play, then scale only against qualified jobs, collected results, and available field capacity.",
    ],
    "statutory_citations": [
        {
            "title": "Texas Insurance Code Section 4102.051 — Public Insurance Adjuster License Required",
            "url": "https://statutes.capitol.texas.gov/Docs/IN/htm/IN.4102.htm#4102.051",
            "relevance": "Separate contractor scope documentation from activities that constitute public adjusting; route claim-representation requests according to applicable licensing requirements.",
        },
        {
            "title": "Texas Insurance Code Section 707.002 — Payment of Deductible",
            "url": "https://statutes.capitol.texas.gov/Docs/IN/htm/IN.707.htm#707.002",
            "relevance": "For covered Texas property policies and work, incorporate the deductible payment requirement and prohibited waiver practices into reviewed contracting and collection workflows.",
        },
        {
            "title": "29 CFR 1926.1101 — Asbestos in Construction",
            "url": "https://www.ecfr.gov/current/title-29/section-1926.1101",
            "relevance": "Route applicable asbestos disturbance work to qualified personnel and required exposure-control procedures rather than clearing hazardous conditions through automated summaries.",
        },
        {
            "title": "40 CFR 745.85 — Work Practice Standards",
            "url": "https://www.ecfr.gov/current/title-40/section-745.85",
            "relevance": "Apply required work practices when restoration includes covered renovation in target housing or child-occupied facilities, including applicable containment and cleaning requirements.",
        },
        {
            "title": "15 U.S.C. 7704 — Requirements for Transmission of Messages",
            "url": "https://www.law.cornell.edu/uscode/text/15/7704",
            "relevance": "Build commercial email workflows with accurate headers, required identification and address information, functioning opt-out processing, and maintained suppression records.",
        },
        {
            "title": "47 U.S.C. 227 — Restrictions on Use of Telephone Equipment",
            "url": "https://www.law.cornell.edu/uscode/text/47/227",
            "relevance": "Review automated calling and texting programs for applicable consent and other restrictions before activation; retain the supporting permission and revocation records.",
        },
        {
            "title": "16 CFR Part 465 — Rule on the Use of Consumer Reviews and Testimonials",
            "url": "https://www.ecfr.gov/current/title-16/chapter-I/subchapter-D/part-465",
            "relevance": "Prevent fake reviews, sentiment-conditioned review incentives, and prohibited review suppression in automated reputation and referral workflows.",
        },
    ],
}
