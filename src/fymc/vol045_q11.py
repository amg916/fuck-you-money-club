from __future__ import annotations

CHAPTER_11 = {
    "id": "Q11",
    "chapter_id": "Q11",
    "chapter_number": 11,
    "question_number": 11,
    "slug": "pod-architecture-contractor-kpis-exit-valuation",
    "question_prompt": "How do you structure a lean 1 FT + 2 C (3 people) -> 2 FT + 3 C (5 people) pod, enforce weekly scorecards, and build transferable books that command a premium exit multiple (or durable cash cow)?",
    "kicker": "Q11 / THE BIG MONEY PLAYBOOKS",
    "title": "Pod Architecture, Contractor KPIs & Exit Valuation",
    "subtitle": "Three-to-Five-Person IDR Pods, Cash-Verified Contingency Waterfalls, HIPAA Controls, and Transferable Recovery Books",
    "layout_template": "action_checklist",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #45, ranked #09 of 49 with a 94/100 Money-to-Manpower Score, "
        "turns out-of-network recovery into a transferable operating book only when "
        "deadlines, evidence, collections, and ownership survive the founder. This "
        "chapter organizes 12 mapped plays into a three-person pod, then adds two "
        "seats only when measured workload supports them. Canonical annual owner "
        "profits are $33,000 Conservative, $217,150 Base, and $504,000 Scaled; operator "
        "revenue excludes initial payer collections and uncollected awards. Weekly "
        "scorecards connect jurisdiction screening, filing quality, fee exposure, "
        "payer aging, and cash realization. Contractor incentives reward accepted "
        "work rather than speculative awards. Concentration limits, documented "
        "intellectual-property ownership, reproducible cohort ledgers, and founder "
        "replacement costs determine whether the book deserves a stronger exit "
        "valuation or remains a durable cash-producing operation."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$110,000",
            "context": "Annual earned operator contingency revenue; excludes baseline provider collections",
            "note": "30% net margin; $33,000 annual owner net profit; 1 FT + 2 C",
        },
        {
            "label": "Base",
            "value": "$505,000",
            "context": "Annual earned operator contingency revenue; excludes baseline provider collections",
            "note": "43.0% net margin; $217,150 annual owner net profit; 1 FT + 2 C",
        },
        {
            "label": "Scaled",
            "value": "$900,000",
            "context": "Annual earned operator contingency revenue; excludes baseline provider collections",
            "note": "56% net margin; $504,000 annual owner net profit; 2 FT + 3 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Assign Twelve Recovery Plays to Named Seats Before Adding Headcount",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Build the initial pod around one full-time accountable operator and two "
                    "specialist contractors, not three interchangeable claim processors. The "
                    "operator owns provider relationships, jurisdiction exceptions, cash "
                    "reconciliation, and the weekly queue. Contractor A owns intake and "
                    "deadline operations; Contractor B owns evidence assembly, offer support, "
                    "and submission quality. Use this chapter's twelve-play operating map: "
                    "P01 provider qualification, P02 engagement and BAA execution, P03 835 "
                    "ingestion, P04 jurisdiction classification, P05 incremental-recovery "
                    "screening, P06 open negotiation, P07 IDR initiation and entity selection, "
                    "P08 batching and cooling-off control, P09 evidence and offer assembly, "
                    "P10 determination tracking, P11 remittance reconciliation, and P12 "
                    "renewal and book transfer. These are assigned workstreams, not twelve "
                    "additional jobs. The operator retains accountability for every play "
                    "while delegating production through explicit acceptance criteria. "
                    "Federal eligibility under 42 U.S.C. section 300gg-111 depends on the "
                    "service, coverage, and applicable payment regime; an ERISA label alone "
                    "does not establish the correct route. Capture plan funding, service "
                    "location, provider specialty, service category, and applicable state "
                    "payment rules before spending entity fees. Store the classification "
                    "rationale alongside source documents so another reviewer can reproduce "
                    "the decision without interviewing the founder. Escalate unresolved "
                    "jurisdiction questions before filing, rather than rewarding a contractor "
                    "for sending an unsupported case."
                ),
                (
                    "Run the deadline engine as a controlled state machine with an assigned "
                    "owner, backup, timestamp, and delivery evidence for every transition. "
                    "The ordinary federal sequence includes initiating open negotiation "
                    "within the applicable thirty-business-day window after initial payment "
                    "or denial, completing the thirty-business-day negotiation period, and "
                    "initiating IDR within four business days after that period ends. The "
                    "four-day window is not a blanket deadline for every entity-selection "
                    "or batching task. Configure later milestones separately under the "
                    "operative version of 45 CFR section 149.510 and applicable extensions. "
                    "Use PostgreSQL for the event ledger and a private task interface for "
                    "assignments; retain portal confirmations in an access-controlled "
                    "document store. A calendar reminder without acknowledged service is "
                    "not completion evidence. Contractor A prepares notices and verifies "
                    "addresses; Contractor B checks disputed dates and submission "
                    "attachments; the operator resolves exceptions. Record holidays, "
                    "timezone conventions, outages, and corrected inputs in an append-only "
                    "audit history. For P08, explicitly record the parties, item or service "
                    "classification, determination date, and relevant ninety-calendar-day "
                    "cooling-off restriction. Do not pool unrelated provider claims merely "
                    "because a payer name matches. Require an independent batch-eligibility "
                    "check before submission and preserve the rule version applied."
                ),
                (
                    "Move to two full-time seats and three contractors only when accepted "
                    "workload, rather than gross award announcements, exceeds demonstrated "
                    "capacity. The original operator becomes portfolio and commercial lead; "
                    "the second employee becomes production and quality lead. Retain the "
                    "intake contractor and evidence contractor, then add a remittance and "
                    "exception-resolution contractor for P10 and P11. This is five people "
                    "in total, not five employees plus a hidden service bureau. Budget "
                    "specialist consultations separately and disclose their expense without "
                    "representing occasional advice as a permanent production seat. Measure "
                    "touch minutes by play for four weeks, then estimate committed capacity "
                    "after leave, rework, and deadline reserves. An illustrative eighty-percent "
                    "utilization ceiling leaves room for short filing windows and payer "
                    "exceptions; it is an operating target, not a statutory requirement. "
                    "Every critical play needs a trained backup, but a person's backup "
                    "assignment does not create extra capacity. Execute HIPAA business "
                    "associate agreements and applicable subcontractor agreements before "
                    "protected information moves, with role-based access and auditable "
                    "offboarding. Keep provider files inside contracted systems rather than "
                    "personal inboxes. Document a two-week founder-absence exercise before "
                    "expansion: another named person must run the queue, reconcile cash, "
                    "and explain unresolved exceptions from the records alone."
                ),
            ],
            "table": {
                "caption": "Twelve-Play Ownership Matrix for Three-Person and Five-Person IDR Pods",
                "headers": [
                    "Seat or workstream",
                    "Initial three-person ownership",
                    "Scaled five-person ownership",
                    "Required handoff evidence",
                ],
                "rows": [
                    [
                        "P01 and P02 provider qualification and contracting",
                        "Full-time operator signs engagements and verifies provider authority",
                        "Portfolio lead retains commercial ownership and renewal accountability",
                        "Executed agreement, BAA, authorized contacts, and pricing waterfall",
                    ],
                    [
                        "P03 and P04 intake and jurisdiction classification",
                        "Intake contractor prepares records; operator resolves jurisdiction exceptions",
                        "Intake contractor produces classifications; production lead validates exceptions",
                        "Original remittance, plan evidence, state analysis, and reviewer identity",
                    ],
                    [
                        "P05 and P06 recovery screening and negotiation",
                        "Intake contractor models economics and prepares negotiation packages",
                        "Production lead supervises screening thresholds and negotiation delivery",
                        "Baseline amount, expected cost exposure, and delivery confirmation",
                    ],
                    [
                        "P07 and P08 initiation and batch eligibility",
                        "Intake contractor submits only independently checked eligible packages",
                        "Production lead owns deadline exceptions and batch-control accuracy",
                        "Initiation receipt, entity milestones, batch rationale, and restriction dates",
                    ],
                    [
                        "P09 clinical evidence and supported offer assembly",
                        "Evidence contractor prepares briefs; operator approves supported offers",
                        "Evidence contractor prepares briefs; production lead performs quality checks",
                        "Permitted evidence sources, clinical support, calculation version, and signoff",
                    ],
                    [
                        "P10 and P11 determinations and collected remittances",
                        "Operator reconciles cash; evidence contractor maintains determination records",
                        "Remittance contractor traces receipts; portfolio lead resolves disputes",
                        "Determination document, payer reference, bank match, and fee waterfall",
                    ],
                    [
                        "P12 renewals and transferable operating book maintenance",
                        "Operator maintains renewal calendar and reproducible provider histories",
                        "Portfolio lead maintains retention evidence and buyer-ready summaries",
                        "Assignment terms, concentration calculations, cohort exports, and ownership records",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Protect the Thin Pod From Expensive Recovery Friction",
                "body": (
                    "The highest-value efficiencies remove preventable rework without "
                    "weakening jurisdiction, evidence, or cash verification."
                ),
                "items": [
                    "Keep an immutable copy of each original 835 and corrected remittance; payer adjustments can otherwise erase the initial-payment baseline used for contingency calculations.",
                    "Prebuild specialty-specific evidence indexes, but make the reviewer confirm patient-specific acuity and permitted factors before reusing any argument.",
                    "Maintain a separate cooling-off register keyed to the relevant parties and item or service classification; a payer-wide calendar entry is too coarse.",
                    "Assign every determination a remittance owner immediately; a favorable offer selection does not deposit money or establish an earned contingency.",
                ],
            },
        },
        {
            "heading": "2. Pay Contractors for Accepted Work and Publish One Weekly Scorecard",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Contractor compensation should purchase defined outputs without "
                    "encouraging ineligible filings or inflated offers. For planning, use "
                    "illustrative hourly rates of $35 to $55 for intake work and $65 "
                    "to $95 for specialized evidence work, then validate actual proposals "
                    "against the expense envelope. A piece-rate alternative should specify "
                    "exactly what an accepted package contains, how revisions are handled, "
                    "and which disputed tasks remain billable. Pay for properly documented "
                    "ineligibility findings as well as eligible packages; otherwise the "
                    "contractor has an economic reason to suppress bad news. Avoid bonuses "
                    "based solely on award size, portal submissions, or headline prevailing "
                    "rates. A modest quality component can reward timely, accepted work "
                    "and accurate reconciliations, with exclusions for payer delay outside "
                    "the contractor's control. Define a one-business-day acknowledgment "
                    "target, a two-business-day routine defect correction target, and "
                    "same-day escalation for deadlines inside five business days. These "
                    "are internal service targets, not substitutes for statutory clocks. "
                    "Have the reviewer identify the defect category and affected claim "
                    "instead of returning a vague rejection. Specify correction economics "
                    "in the statement of work, and avoid unilateral payment deductions. "
                    "Worker classification follows actual relationships and applicable "
                    "law; a contractor label does not settle employee status."
                ),
                (
                    "Publish the scorecard at the same weekly cutoff using stable "
                    "denominators and claim-level drilldowns. For P03 through P05, show "
                    "complete-intake rate, independently confirmed eligibility rate, and "
                    "screening turnaround. For P06 through P08, show notices served on "
                    "time, initiation deadlines met, rejected submissions, and preventable "
                    "ineligibility dismissals. For P09, show first-pass acceptance, hours "
                    "per accepted brief, and defects by evidence category. For P10 "
                    "and P11, separate favorable determinations, dollars awarded above "
                    "baseline, incremental dollars collected, collection lag, and fees "
                    "actually returned. A prevailing percentage must identify whether its "
                    "denominator is determinations, cases, or dollars; none is a cash "
                    "collection rate. Cohort cash realization divides incremental receipts "
                    "by the corresponding incremental amounts due for the same matured "
                    "cohort, with reversals handled consistently. Do not compare this "
                    "week's deposits with this week's awards. Track the thirty-calendar-day "
                    "payment requirement following the federal determination separately "
                    "from observed payer behavior. Age unpaid balances from their actual "
                    "due dates, assign a collection action, and preserve correspondence. "
                    "A weekly meeting should finish with named corrective owners and "
                    "dates, not a discussion about who was busiest. Repeated eligibility "
                    "defects trigger expanded review before more fees are exposed."
                ),
                (
                    "Use concentration limits to protect both workload continuity and "
                    "saleability. Set an internal ceiling of twenty-five percent for any "
                    "single provider customer and separately for any payer parent group, "
                    "measured on trailing-twelve-month earned operator revenue. Also inspect "
                    "incremental receivables and forecast fee exposure because a payer can "
                    "dominate unpaid awards before dominating collected revenue. Aggregate "
                    "affiliated practices under their controlling relationship and payer "
                    "brands under the economically relevant parent; multiple logos do not "
                    "necessarily diversify risk. A new pod may initially exceed the ceiling. "
                    "Report that breach explicitly, cap additional discretionary exposure, "
                    "and pursue other accounts while preserving existing client duties "
                    "and deadlines. Do not describe a concentrated launch book as diversified. "
                    "Apply the same discipline to contractor dependency: each critical "
                    "play must have an operational backup with tested access. Review "
                    "capacity, concentration, and unresolved defects together each Friday. "
                    "If new business would consume the deadline reserve, delay onboarding "
                    "rather than accept volume the pod cannot service. Revenue growth "
                    "does not justify weak evidence or unexplained fee losses. Retain "
                    "weekly snapshots so a buyer can distinguish genuine improvement "
                    "from a dashboard rewritten immediately before diligence. Compare "
                    "rolling four-week results with the prior period to detect persistent "
                    "drift rather than overreacting to individual case outcomes."
                ),
            ],
            "table": {
                "caption": "Weekly Contractor and Portfolio Scorecard With Reproducible Denominators",
                "headers": [
                    "Metric and accountable owner",
                    "Exact measurement basis",
                    "Internal target or intervention trigger",
                    "Evidence supporting the weekly review",
                ],
                "rows": [
                    [
                        "Intake completeness controlled by the intake contractor",
                        "Complete accepted records divided by all records received",
                        "Investigate every missing document that threatens a deadline",
                        "Required-field report linked to original remittance and engagement",
                    ],
                    [
                        "Jurisdiction accuracy controlled by the accountable reviewing lead",
                        "Confirmed classifications divided by independently checked classified cases",
                        "Expand review after any preventable jurisdiction-based fee forfeiture",
                        "Plan funding evidence, state route rationale, and reviewer notes",
                    ],
                    [
                        "Deadline performance controlled by the assigned calendar owner",
                        "Timely required actions divided by all actions due",
                        "Require complete timeliness and immediately investigate every miss",
                        "Timestamped notices, delivery evidence, portal receipts, and extensions",
                    ],
                    [
                        "Evidence acceptance controlled by the specialist brief contractor",
                        "First-pass accepted briefs divided by all briefs submitted",
                        "Illustrative target above ninety-five percent after initial training",
                        "Reviewer checklist, defect categories, and corrected version history",
                    ],
                    [
                        "Collection realization controlled by the remittance reconciliation owner",
                        "Cohort incremental receipts divided by matched incremental amounts due",
                        "Investigate overdue determinations and deteriorating matured-cohort realization",
                        "Determination amounts, contractual due dates, and matched bank receipts",
                    ],
                    [
                        "Customer and payer concentration controlled by portfolio lead",
                        "Largest related-group revenue divided by trailing annual revenue",
                        "Keep each customer and payer group at twenty-five percent maximum",
                        "Related-party grouping, revenue ledger, receivable aging, and exposure forecast",
                    ],
                    [
                        "Production capacity controlled by the accountable pod operator",
                        "Committed touch hours divided by available productive hours",
                        "Illustrative eighty-percent ceiling preserves deadline and rework reserves",
                        "Time samples, accepted output, absence schedule, and backup assignments",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Freeze the weekly measurement set",
                    "action": "Export the claim ledger, cash matches, deadline queue, and accepted-work register at the agreed cutoff.",
                    "detail": "Retain the export version and calculation definitions so later corrections remain visible rather than silently rewriting history.",
                },
                {
                    "step": 2,
                    "title": "Resolve imminent deadlines before discussing growth",
                    "action": "Inspect every required action due within five business days and confirm its owner, backup, and supporting evidence.",
                    "detail": "Separate genuine legal extensions from internal scheduling changes; retain the source authorizing each extension.",
                },
                {
                    "step": 3,
                    "title": "Trace exceptions to their economic consequences",
                    "action": "Review defects, forfeited fees, overdue awards, and concentration breaches using claim-level records.",
                    "detail": "Assign each corrective action a responsible person, completion date, and measurable acceptance condition.",
                },
                {
                    "step": 4,
                    "title": "Release accepted contractor work and next-week capacity",
                    "action": "Approve invoices against contracted acceptance terms and reserve hours for deadlines, rework, and collections.",
                    "detail": "Authorize additional volume only within measured capacity; archive decisions with the weekly scorecard snapshot.",
                },
            ],
        },
        {
            "heading": "3. Reconcile Cash-Based Fee Waterfalls to Clean Accrual and Cohort Books",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Start every engagement with a written recovery waterfall that separates "
                    "provider money from operator revenue. The initial payer allowed "
                    "payment is the baseline; the QPA may inform that payment but is "
                    "not automatically identical to it. Measure incremental cash against "
                    "the actual documented baseline, including subsequent adjustments "
                    "without double counting. For an illustrative claim, assume $2,000 "
                    "initial payment and $8,000 total payer cash ultimately received. "
                    "Incremental cash is $6,000. If actual non-refundable administrative "
                    "fees are $150, an entity-fee deposit of $600 is returned following "
                    "a prevailing determination, and attributable casework costs are "
                    "$450, the distributable incremental pool is $5,400. At a contracted "
                    "twenty-five-percent contingency, operator revenue is $1,350, not "
                    "$8,000 and not the award amount. The example's fees are assumptions, "
                    "not a current CMS fee schedule. Until the $600 refund actually "
                    "arrives, an unrecovered-fee waterfall produces a $4,800 pool and "
                    "$1,200 fee, followed by a $150 true-up after receipt. Losing "
                    "or ineligible cases retain the applicable forfeited entity-fee "
                    "exposure. Record actual allocations for settlements and other "
                    "procedural outcomes separately. Never assume all deposits return "
                    "or calculate a fee from an uncollected favorable determination."
                ),
                (
                    "The canonical Formula v2.0 scenarios remain fixed: Conservative "
                    "operator revenue of $110,000 less $77,000 expenses yields $33,000 "
                    "owner profit at thirty percent; Base revenue of $505,000 less "
                    "$287,850 yields $217,150 at 43.0 percent; Scaled revenue of $900,000 "
                    "less $396,000 yields $504,000 at fifty-six percent. Conservative "
                    "and Base use one full-time person plus two contractors; Scaled "
                    "uses two full-time people plus three contractors. These revenue "
                    "figures are gross operator fee revenue, not gross medical "
                    "collections. At the illustrative twenty-five-percent share, the "
                    "necessary post-cost incremental pools are $440,000, $2,020,000, "
                    "and $3,600,000 respectively. This sensitivity explains the cases "
                    "without inventing a universal claim count or collection rate. "
                    "Amounts deducted before calculating the share must carry explicit "
                    "funding and reimbursement treatment. If a provider bears casework "
                    "cost through the waterfall, record that reimbursement or settlement "
                    "once; do not silently charge the identical cost again against "
                    "operator profit. Operator-funded unreimbursed casework, contractor "
                    "overhead, technology, and other operating expenses belong in "
                    "the stated expense envelope. The $1,800 to $10,500 monthly "
                    "opex range is not an all-in reconciliation for every scenario; "
                    "annualized stated expense envelopes exceed that range in Base "
                    "and Scaled because the full cost bridge must be shown."
                ),
                (
                    "Maintain separate dates for service, intake, negotiation, initiation, "
                    "determination, payer receipt, fee earning, invoicing, and operator "
                    "collection. The earned contingency condition is incremental payer "
                    "cash actually collected under the engagement, not merely a "
                    "favorable award. When that condition and the applicable revenue "
                    "recognition requirements are satisfied, recognize operator fee "
                    "revenue and a provider receivable even if the provider pays "
                    "the invoice later. Keep potential awards and unearned contingent "
                    "fees in operational schedules rather than booked revenue. Evaluate "
                    "principal-versus-agent presentation under ASC 606 for reimbursed "
                    "costs and pass-through funds; do not label provider collections "
                    "as operator turnover. Separate cash custodial obligations from "
                    "earned revenue and reconcile any handled client funds by provider. "
                    "Create cohorts by intake month, provider, payer group, jurisdiction "
                    "route, and service category. Each cohort should expose submitted "
                    "volume, eligible volume, fee losses, collected uplift, contractor "
                    "cost, and time to cash. Accrue incurred contractor work and "
                    "other expenses in the proper period, estimate collectibility "
                    "of earned receivables, and record reversals transparently. A "
                    "buyer should reconcile ledger totals to invoices, payer remittances, "
                    "and bank records without relying on a founder's spreadsheet "
                    "explanation. Close monthly with a documented review of unmatched "
                    "cash and all outstanding entity-fee deposits."
                ),
            ],
            "table": {
                "caption": "Formula v2.0 Revenue Bridge and Claim-Level Cash Recognition Controls",
                "headers": [
                    "Scenario or accounting object",
                    "Revenue and pool interpretation",
                    "Expense and profit treatment",
                    "Required reconciliation evidence",
                ],
                "rows": [
                    [
                        "Conservative case with one employee and two contractors",
                        "$110,000 operator revenue; illustrative post-cost pool equals $440,000",
                        "$77,000 total expenses; $33,000 profit; thirty percent margin",
                        "Tie earned fees and expenses to the annual ledger",
                    ],
                    [
                        "Base case with one employee and two contractors",
                        "$505,000 operator revenue; illustrative post-cost pool equals $2,020,000",
                        "$287,850 total expenses; $217,150 profit; 43.0 percent margin",
                        "Reconcile provider fee invoices with matched incremental cash receipts",
                    ],
                    [
                        "Scaled case with two employees and three contractors",
                        "$900,000 operator revenue; illustrative post-cost pool equals $3,600,000",
                        "$396,000 total expenses; $504,000 profit; fifty-six percent margin",
                        "Verify five-person staffing costs against accepted work and payroll",
                    ],
                    [
                        "Initial payer payment and subsequent baseline adjustments",
                        "Exclude baseline collections from every operator contingency calculation",
                        "Document adjustments without treating baseline cash as recovered uplift",
                        "Preserve original 835 records and all corrected remittance versions",
                    ],
                    [
                        "Administrative fees and certified entity fee deposits",
                        "Deduct actual unrecovered amounts before applying contracted contingency",
                        "Track deposit refunds separately from operator fee earnings",
                        "Match payment evidence, procedural outcome, refund receipt, and true-up",
                    ],
                    [
                        "Casework funding and reimbursement across the recovery waterfall",
                        "Calculate the share only after stipulated attributable cost deductions",
                        "Assign each cost once under documented funding responsibility",
                        "Link contractor invoices to cost allocations and reimbursement entries",
                    ],
                    [
                        "Earned provider receivables and outstanding contingent recovery schedules",
                        "Recognize earned operator fees separately from uncollected potential awards",
                        "Accrue incurred costs and evaluate earned receivable collectibility",
                        "Reconcile cohort detail, general ledger, bank activity, and invoices",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four Checks Before Exposing Fees or Booking a Contingency",
                "body": (
                    "Use the first three checks before filing and repeat the cash "
                    "check before recognizing or invoicing the earned recovery share."
                ),
                "items": [
                    "Verify the applicable federal or state route using service facts, plan funding evidence, and documented exceptions; do not equate every ERISA plan with federal IDR eligibility.",
                    "Verify notice delivery, business-day calculations, batch eligibility, relevant cooling-off restrictions, and the operative rule version before committing submission fees.",
                    "Verify current administrative and entity charges, losing-case exposure, casework funding, and the signed post-cost contingency waterfall against claim-level expected economics.",
                    "Verify incremental payer cash, the original payment baseline, actual fee refunds, attributable costs, and the resulting operator fee before recording earned revenue.",
                ],
            },
        },
        {
            "heading": "4. Make the Recovery Book Transferable Before Discussing an Exit Multiple",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "A transferable book consists of enforceable relationships, reproducible "
                    "work, clean ownership, and evidence that collections continue "
                    "without the founder. Provider agreements should address assignment, "
                    "change of control, termination, access to records, recovery-tail "
                    "economics, and responsibility for outstanding fees. Obtain required "
                    "permissions before transferring contracts or sensitive records; "
                    "a transaction term sheet does not itself authorize disclosure "
                    "of protected health information. Begin buyer diligence with "
                    "aggregated cohorts and properly de-identified information where "
                    "appropriate, then structure necessary access under applicable "
                    "HIPAA permissions and safeguards. Contractor deliverables need "
                    "signed intellectual-property assignments under 17 U.S.C. section "
                    "204(a) where copyright ownership is transferred. Do not rely "
                    "solely on a broad work-made-for-hire label for independent "
                    "contractor software or templates. Identify preexisting contractor "
                    "tools and secure sufficient transferable licenses for required "
                    "components. Inventory source code, deadline rules, brief templates, "
                    "evidence indexes, and operating manuals in a controlled repository. "
                    "FAIR Health access and other licensed sources require their own "
                    "usage and transfer review; purchased access does not establish "
                    "ownership of the underlying material. Keep credentials outside "
                    "the sale repository. Prove continuity through tested backup "
                    "access, documented renewals, and a named successor for each "
                    "of the twelve plays."
                ),
                (
                    "Value a normalized earnings stream, not the face amount of "
                    "pending determinations. For an owner-operated practice, an "
                    "illustrative two-to-three-times seller discretionary earnings "
                    "range can serve as a sensitivity, provided the earnings "
                    "definition, owner compensation, and required owner labor are "
                    "reconciled. Using Base owner profit of $217,150 as a provisional "
                    "SDE proxy produces $434,300 to $651,450; it becomes a usable "
                    "valuation input only after that bridge is verified. These "
                    "are planning assumptions, not observed transaction comparables. "
                    "An independently managed operation can instead test a "
                    "three-to-five-times normalized EBITDA range. If Scaled owner "
                    "profit of $504,000 excludes a necessary $120,000 replacement "
                    "manager cost, and no other adjustments apply, the normalized "
                    "proxy becomes $384,000 and the enterprise-value sensitivity "
                    "becomes $1,152,000 to $1,920,000. Do not deduct replacement "
                    "cost twice if it is already inside the $396,000 expense "
                    "envelope. Owner profit, SDE, and EBITDA are different "
                    "measures; provide the bridge rather than relabeling them. "
                    "Determine equity proceeds separately after debt, cash "
                    "adjustments, working-capital terms, transaction costs, and "
                    "holdbacks. A higher multiple requires defensible retention, "
                    "limited concentration, stable cohort collections, and "
                    "demonstrably transferable execution. A backlog of unpaid "
                    "awards is not a substitute for those attributes."
                ),
                (
                    "Prepare a rolling diligence package even if the intended "
                    "outcome is a durable cash cow. Include monthly income "
                    "statements, expense bridges, provider and payer concentration, "
                    "cohort collection curves, fee-loss history, contractor "
                    "acceptance records, ownership documents, and the founder-absence "
                    "test. Separate recurring revenue from one-time catch-up "
                    "recoveries and expose provider churn rather than blending "
                    "departed accounts into historical totals. For a sale, define "
                    "which party owns preclosing awards, postclosing receipts, "
                    "refunds, and collection costs. If an earnout is used, "
                    "base it on an auditable measure such as collected operator "
                    "fees from identified transferred cohorts, with agreed "
                    "deductions, collection responsibilities, reporting rights, "
                    "and dispute procedures. An award-based earnout can overpay "
                    "for balances that never convert to cash. For continued "
                    "ownership, reserve cash for payroll, contractor commitments, "
                    "unrecovered fees, and delayed payer remittances before "
                    "distributions. Stress-test the loss of the largest provider "
                    "and a prolonged payment delay from the largest payer "
                    "group. The twenty-five-percent caps limit exposure but "
                    "do not eliminate it. Choose growth only when it improves "
                    "normalized cash generation after replacement labor; "
                    "otherwise preserve the smaller pod. The same disciplined "
                    "records support either decision without manufacturing "
                    "a premium narrative around uncertain collections."
                ),
            ],
            "table": {
                "caption": "Buyer Diligence and Owner Cash-Cow Tests for a Transferable IDR Book",
                "headers": [
                    "Transferability or valuation issue",
                    "Evidence the operator must maintain",
                    "Buyer underwriting or pricing consequence",
                    "Owner action before transaction discussions",
                ],
                "rows": [
                    [
                        "Provider contracts and continuity of authorized recovery work",
                        "Executed agreements with assignment terms and recovery-tail provisions",
                        "Termination exposure weakens confidence in continuing collected fees",
                        "Resolve required permissions and document outstanding case responsibilities",
                    ],
                    [
                        "Contractor intellectual property and reusable operating asset ownership",
                        "Signed assignments plus inventories of licensed preexisting materials",
                        "Unclear ownership can exclude essential assets from the transaction",
                        "Secure transferable rights before presenting templates as owned assets",
                    ],
                    [
                        "Protected information and licensed evidence source transfer restrictions",
                        "Documented access purposes, safeguards, agreements, and license conditions",
                        "Restricted access changes diligence design and postclosing integration",
                        "Prepare aggregated diligence first and authorize necessary access separately",
                    ],
                    [
                        "Provider and payer concentration across related economic groups",
                        "Trailing annual revenue shares and outstanding incremental receivable exposure",
                        "Any group above twenty-five percent requires explicit risk treatment",
                        "Diversify new intake without abandoning existing client deadlines",
                    ],
                    [
                        "Base owner-operated earnings sensitivity using a provisional SDE proxy",
                        "$217,150 owner profit supported by a verified normalization bridge",
                        "Illustrative two-to-three-times range produces $434,300 to $651,450",
                        "Verify owner labor requirements before relying on this proxy",
                    ],
                    [
                        "Scaled managed earnings sensitivity after necessary replacement labor",
                        "$504,000 less assumed $120,000 replacement cost yields $384,000",
                        "Illustrative three-to-five-times range produces $1,152,000 to $1,920,000",
                        "Confirm replacement cost is absent from existing scenario expenses",
                    ],
                    [
                        "Transaction structure versus continued owner cash generation",
                        "Cohort cash evidence, working-capital requirements, and founder-absence results",
                        "Earnout deductions and collection responsibility materially affect realized proceeds",
                        "Compare net sale proceeds with stress-tested distributable owner cash",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "A recovery book earns its multiple when another operator can collect its cash, defend its numbers, and run its deadlines without the founder.",
    "diagram_id": "diag-06",
    "action_checklist": [
        "Assign P01 through P12 to the three-person pod, name trained backups, and document the measured workload that would justify the five-person structure.",
        "Execute engagement, BAA, subcontractor, and intellectual-property documents; record jurisdiction evidence before committing IDR fees.",
        "Publish a weekly scorecard with stable denominators for deadlines, accepted work, eligibility defects, matured-cohort collections, and overdue payer remittances.",
        "Enforce separate twenty-five-percent provider-customer and payer-group concentration ceilings, reporting launch-stage breaches and limiting additional exposure.",
        "Reconcile the canonical $110,000, $505,000, and $900,000 operator revenue cases to post-cost incremental cash and the exact owner-profit expense bridges.",
        "Run a founder-absence test and assemble a transferable diligence book with contract rights, cohort ledgers, replacement-labor normalization, and explicit sale-versus-hold sensitivities.",
    ],
    "statutory_citations": [
        {
            "title": "42 U.S.C. section 300gg-111 — Preventing surprise medical bills",
            "url": "https://www.law.cornell.edu/uscode/text/42/300gg-111",
            "relevance": (
                "Establishes federal surprise-billing protections and the payment "
                "determination framework underlying eligible negotiation and IDR work."
            ),
        },
        {
            "title": "45 CFR section 149.510 — Federal independent dispute resolution process",
            "url": "https://www.ecfr.gov/current/title-45/section-149.510",
            "relevance": (
                "Provides operational requirements for negotiation, initiation, "
                "entity selection, batching, determinations, fees, cooling-off "
                "restrictions, and payment timing; preserve the operative rule "
                "version and applicable extensions for each case."
            ),
        },
        {
            "title": "45 CFR section 149.140 — Methodology for calculating qualifying payment amount",
            "url": "https://www.ecfr.gov/current/title-45/section-149.140",
            "relevance": (
                "Supports QPA analysis while keeping that benchmark distinct "
                "from the actual initial payer payment used in the recovery waterfall."
            ),
        },
        {
            "title": "45 CFR section 164.504(e) — Business associate contracts",
            "url": "https://www.ecfr.gov/current/title-45/section-164.504",
            "relevance": (
                "Defines required business associate contractual protections "
                "and relevant downstream obligations when recovery operations "
                "handle protected health information."
            ),
        },
        {
            "title": "45 CFR section 164.308 — Administrative safeguards",
            "url": "https://www.ecfr.gov/current/title-45/section-164.308",
            "relevance": (
                "Supports security risk management, workforce controls, "
                "contingency planning, and documented access responsibilities "
                "across employee and contractor seats."
            ),
        },
        {
            "title": "17 U.S.C. section 204(a) — Execution of transfers of copyright ownership",
            "url": "https://www.law.cornell.edu/uscode/text/17/204",
            "relevance": (
                "Requires a signed writing for covered copyright transfers, "
                "supporting documented ownership of contractor-created software, "
                "brief templates, and operating materials."
            ),
        },
        {
            "title": "29 U.S.C. section 1144 — ERISA effect on other laws",
            "url": "https://www.law.cornell.edu/uscode/text/29/1144",
            "relevance": (
                "Provides the preemption, insurance-saving, and deemer framework "
                "relevant to distinguishing plan funding and state-law treatment "
                "during jurisdiction screening."
            ),
        },
    ],
}
