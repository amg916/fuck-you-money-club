from __future__ import annotations

CHAPTER_12 = {
    "id": "Q12",
    "chapter_id": "Q12",
    "chapter_number": 12,
    "question_number": 12,
    "slug": "first-30-day-launch-sprint-kill-fix-scale",
    "question_prompt": "What is the exact Day-1-to-Day-30 execution schedule for launching iso payment processing & atm arbitrage, and what quantitative thresholds govern Kill, Fix, or Scale decisions at Day 30/60/90?",
    "kicker": "Q12 / THE BIG MONEY PLAYBOOKS",
    "title": "The First 30-Day Launch Sprint & Kill / Fix / Scale Gates",
    "subtitle": "A Four-Person ISO and ATM Launch: Schedule A Economics, IRIS CRM Evidence, Reg E Screens, and Day-30/60/90 Capital Decisions",
    "layout_template": "thirty_day_plan",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #32, ISO Payment Processing & ATM Arbitrage, holds Rank #02 of 36 "
        "with a 94/100 Money-to-Manpower Score. This sprint translates its 12 mapped "
        "plays into a controlled launch for one full-time operator and three contractors: "
        "prove sponsor access, document retained spreads, board approved merchants, and "
        "validate exclusive ATM locations before expanding. The canonical annual owner "
        "profit cases are $27,000 Conservative, $189,125 Base, and $440,000 Scaled; none "
        "is a first-month target. Days 1–30 establish evidence, with a $6,000 operating "
        "cash-deployment ceiling and separate vault cash. Day-30/60/90 decisions distinguish "
        "fatal sponsorship or authorization failures from repairable conversion problems "
        "and genuinely repeatable contribution. Scale follows reconciled economics, not "
        "merchant settlement volume, signed applications, or optimistic ATM footfall."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$90,000",
            "context": "Annual retained operator revenue; excludes merchant settlements and ATM vault cash",
            "note": "30% net margin; $27,000 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Base",
            "value": "$445,000",
            "context": "Annual retained operator revenue; excludes merchant settlements and ATM vault cash",
            "note": "42.5% net margin; $189,125 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Scaled",
            "value": "$800,000",
            "context": "Annual retained operator revenue; excludes merchant settlements and ATM vault cash",
            "note": "55% net margin; $440,000 annual owner net profit; 2 FT + 4 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Days 1–7: Establish Sponsor Access, Twelve Play IDs, and a Cash Boundary",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Start Day 1 by making the twelve plays explicit workstreams rather than twelve "
                    "simultaneous launches. This chapter's operating map is P01 wholesale Schedule A "
                    "negotiation; P02 interchange-plus merchant acquisition; P03 gateway markup attachment; "
                    "P04 permitted credit-card surcharge deployment; P05 genuine dual-pricing deployment; "
                    "P06 sponsor-approved higher-risk MID placement; P07 residual audit recovery; P08 "
                    "retention and repricing; P09 Verifi RDR or Ethoca dispute deflection; P10 exclusive "
                    "ATM venue acquisition; P11 ATM surcharge yield management; and P12 telemetry and "
                    "vault-cash control. These are operating labels for the twelve mapped plays, not "
                    "twelve independent revenue forecasts. Activate P01, P02, P03, P07, P10, and P12 "
                    "first; the remaining plays require an eligible merchant, actual dispute exposure, "
                    "a renewal opportunity, or measured ATM traffic. Assign the full-time operator "
                    "forty weekly hours across selling, sponsor coordination, and decisions. Contractor "
                    "one receives eight hours for boarding and evidence control; contractor two receives "
                    "six for integrations and terminal configuration; contractor three receives six for "
                    "ATM field service and cash-provider coordination. That sixty-hour weekly pod must "
                    "also handle support. Reserve twelve of those hours for exceptions, and stop adding "
                    "installations whenever unresolved incidents consume that reserve. No contractor "
                    "receives unrestricted merchant banking access."
                ),
                (
                    "Use Days 2–4 to replace attractive sales language with enforceable economics. "
                    "Request the sponsor or upstream ISO agreement, current Schedule A, residual "
                    "ownership and vesting language, termination treatment, reserve rights, clawbacks, "
                    "and the actual underwriting checklist. Confirm who registers the business with "
                    "each relevant card network and what activities the agreement authorizes. An "
                    "unsigned reseller arrangement is not permission to present as a registered ISO. "
                    "For each merchant quote, separate interchange and network assessments from "
                    "processor costs, the merchant-facing markup, and the retained operator share. "
                    "For each ATM proposal, identify terminal ownership, vault-cash ownership, venue "
                    "commission, switch fees, replenishment costs, and servicing responsibility. "
                    "P06 does not authorize splitting one business across unrelated MIDs to escape "
                    "monitoring; submit the true business model and beneficial owners through the "
                    "sponsor's process. Document MATCH screening responsibility and the sponsor's "
                    "current dispute thresholds without inventing a universal safe percentage. "
                    "P04 and P05 require separate pricing designs: debit restrictions under 15 "
                    "U.S.C. 1693o-2 do not create a general permission to surcharge debit cards. "
                    "Require the processor's supported tender logic and jurisdiction-specific price "
                    "presentation before either play reaches a live terminal. Keep rejected "
                    "configurations as regression-test cases for every subsequent software update."
                ),
                (
                    "On Days 5–7, freeze the launch budget and evidence architecture. The illustrative "
                    "capital package is $20,000 of unrestricted operating cash plus $5,000 of separately "
                    "controlled vault cash, a $25,000 startup within the canonical $8,000–$45,000 "
                    "range. Cap Days 1–30 operating cash deployment at $6,000: $2,000 equipment and "
                    "installation, $1,000 sponsor and software setup, $1,800 contractor work, $600 "
                    "travel and prospecting, and $600 contingency. Unused categories remain unspent; "
                    "a contingency allocation is not a purchasing instruction. Limit Days 31–60 "
                    "and 61–90 to another $4,000 each, preserving $6,000 operating liquidity before "
                    "receipts. This cash schedule includes equipment purchases and therefore differs "
                    "from recurring expense recognition. Vault principal never funds payroll, and "
                    "merchant settlement balances never enter the operator's budget. Configure IRIS "
                    "CRM with play ID, sponsor, consented contact source, underwriting status, "
                    "quoted economics, and next evidence date. Store sensitive boarding documents "
                    "only in the sponsor-approved intake system; use CRM references rather than "
                    "copies of identity records. Create a separate ATM ledger linking terminal "
                    "identifier, venue contract, dispenser balance, settlement receivable, and "
                    "cash-service ticket. Export weekly evidence before changing any pricing or "
                    "residual assumptions."
                ),
            ],
            "table": {
                "caption": "Days 1–7: Named Owners, Play Coverage, and Verifiable Launch Artifacts",
                "headers": [
                    "Execution day and assigned operating owner",
                    "Specific work tied to mapped plays",
                    "Required artifact before the next action",
                    "Quantitative boundary or explicit stop condition",
                ],
                "rows": [
                    [
                        "Day 1: full-time operator assigns all twelve workstreams",
                        "Map P01 through P12 into one prioritized backlog",
                        "Publish ownership, weekly hours, and dependent sponsor decisions",
                        "Limit planned work to forty-eight hours plus twelve reserved",
                    ],
                    [
                        "Day 2: operator and boarding contractor examine sponsorship",
                        "Validate P01 permissions and P06 permitted merchant categories",
                        "Retain executed terms or a documented contract deficiency list",
                        "Stop live selling representations that exceed written sponsor authority",
                    ],
                    [
                        "Day 3: operator constructs merchant spread comparison worksheets",
                        "Model P02 processing and P03 gateway retained shares",
                        "Produce three sample quotes with every pass-through separated",
                        "Reject quotes whose retained spread cannot be independently reproduced",
                    ],
                    [
                        "Day 4: integration contractor reviews tender configuration options",
                        "Test eligibility conditions for P04 and P05 pricing",
                        "Record supported debit exclusions and displayed price treatment",
                        "Require zero debit surcharges in every proposed surcharge configuration",
                    ],
                    [
                        "Day 5: field contractor evaluates initial ATM operating partners",
                        "Price P10 placement and P12 cash-service responsibilities",
                        "Obtain written equipment, cash custody, and servicing quotations",
                        "Keep vault principal segregated from all operating spending commitments",
                    ],
                    [
                        "Day 6: boarding contractor configures the evidence workflow",
                        "Connect P07 audit fields and P08 renewal reminders",
                        "Create CRM records referencing approved document storage locations",
                        "Allow no sensitive identity attachments in ordinary prospect records",
                    ],
                    [
                        "Day 7: operator signs the first weekly resource review",
                        "Sequence active plays against sponsor and installation dependencies",
                        "Publish the cash forecast and unresolved exception register",
                        "Keep first-month operating cash deployment at or below $6,000",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four Pre-Flight Conditions Before Any Live Payment or Withdrawal",
                "body": "Hold the affected installation until its evidence is complete; continue unrelated prospect research within the existing budget.",
                "items": [
                    "Verify executed sponsor authority, required network registration status, approved merchant category, and named underwriting contact before accepting a live merchant.",
                    "Reproduce the quoted retained residual from Schedule A, including gateway charges, reserve treatment, clawbacks, and residual termination provisions.",
                    "Test credit, debit, refund, and displayed-price behavior against applicable network rules and state requirements; release no surcharge configuration with debit leakage.",
                    "Verify the ATM venue agreement, controlled cash custody, insurance scope, switch activation, and the 12 CFR 1005.16 fee screen with affirmative consumer continuation.",
                ],
            },
        },
        {
            "heading": "2. Days 8–14: Build a Qualified Pipeline and Prove Installation Readiness",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Days 8–10 are a narrow acquisition sprint, not a mass solicitation exercise. "
                    "Select one merchant vertical the sponsor accepts and one ATM venue archetype "
                    "with observable cash demand. Build thirty named merchant prospects and ten "
                    "venue prospects using public business information and introductions. A qualified "
                    "merchant has an authorized decision-maker, an eligible business model, a "
                    "documented pricing problem, and willingness to provide a current statement "
                    "through the approved channel. A qualified venue has a decision-maker, viable "
                    "power and communications, an accessible placement position, and evidence of "
                    "cash demand beyond an owner's estimate. Target ten completed merchant discovery "
                    "conversations and four venue walkthroughs by Day 14; these are internal workload "
                    "targets, not expected close rates. Use P02 and P03 as the default offer, "
                    "presenting P04 or P05 only when the merchant's operating environment supports "
                    "them. Capture the current effective processing cost, transaction count, average "
                    "ticket, card mix, and recurring gateway charges. Do not compare an interchange-plus "
                    "quote against a blended headline rate while ignoring per-item costs. For venues, "
                    "record operating hours, nearby competing ATMs, existing cash-back options, "
                    "seasonality, and physical access constraints. Photograph the proposed equipment "
                    "position only with venue permission and exclude customers."
                ),
                (
                    "Days 11–12 convert interest into complete, truthful submissions. The boarding "
                    "contractor checks the sponsor's required identity, ownership, bank-account, "
                    "website, refund-policy, and fulfillment evidence, while the operator resolves "
                    "commercial questions. Submit three complete merchant files by Day 14 if the "
                    "qualified pipeline supports them; never manufacture completeness to meet the "
                    "target. Record the sponsor's receipt timestamp and distinguish submitted, "
                    "accepted for review, approved, installed, and first funded transaction. A "
                    "merchant is not activated merely because IRIS CRM shows a signed application. "
                    "Higher-risk placement under P06 stays inactive unless the sponsor expressly "
                    "accepts that actual business model, descriptor, settlement structure, and "
                    "reserve terms. For P09, ask whether Verifi RDR or Ethoca integration is "
                    "available through the processor and determine account eligibility, event "
                    "pricing, duplicate-event handling, and refund authority. Do not assume every "
                    "alert prevents a dispute or that automation removes chargeback exposure. "
                    "Configure refund limits and reconcile processor outcomes before expanding "
                    "automation. The contractor may collect missing records but cannot edit "
                    "merchant facts to satisfy underwriting. Escalate inconsistencies to the "
                    "sponsor, record the response, and close the opportunity when the business "
                    "cannot substantiate its activities. Protecting the upstream relationship "
                    "outweighs one attractive residual."
                ),
                (
                    "Days 13–14 establish ATM site economics and deployment readiness without "
                    "ordering equipment for an unproven location. Obtain two written venue "
                    "proposals covering exclusivity, term, commission calculation, access, power, "
                    "network availability, early termination, equipment removal, and responsibility "
                    "for damage. Exclusivity must identify its actual scope; a vague promise "
                    "does not prevent competing cash-back or another terminal elsewhere on the "
                    "property. Build a downside transaction estimate from observed demand and "
                    "comparable evidence, then obtain the cash provider's service frequency and "
                    "minimum charge. Test the ATM fee-disclosure flow required by 12 CFR "
                    "1005.16: disclose the fee on screen or paper before commitment and "
                    "obtain the consumer's election to continue. Do not substitute an exterior "
                    "sticker for the required transaction-stage disclosure. Evaluate P12 alerts "
                    "for low cash, offline status, dispenser errors, and tamper events, with "
                    "named responders and after-hours contact coverage. FinCEN treatment depends "
                    "on actual activities under 31 CFR 1010.100(ff); a conventional withdrawal "
                    "ATM is not automatically an MSB solely because it dispenses cash. Expanded "
                    "transfer or exchange services require a fresh activity assessment. The "
                    "operator closes Week 2 with a documented readiness decision, not a "
                    "ceremonial installation deadline."
                ),
            ],
            "table": {
                "caption": "Days 8–14: Merchant Discovery, Truthful Boarding, and Exclusive Venue Evidence",
                "headers": [
                    "Daily responsibility within the four-person pod",
                    "Concrete acquisition or preparation activity performed",
                    "Evidence retained in the controlled operating record",
                    "Target that determines the next practical move",
                ],
                "rows": [
                    [
                        "Day 8: operator selects one merchant vertical",
                        "Build thirty named prospects accepted by sponsor criteria",
                        "Record decision-maker route and observed processing pain point",
                        "Exclude every category outside written sponsor acceptance parameters",
                    ],
                    [
                        "Day 9: operator conducts first merchant discovery calls",
                        "Compare current statements against P02 and P03 economics",
                        "Retain permissioned statement references and reproducible comparison worksheets",
                        "Complete five substantive conversations before revising the pitch",
                    ],
                    [
                        "Day 10: field contractor inspects candidate venue locations",
                        "Examine P10 access and P12 cash-service feasibility",
                        "Record demand observations, competing machines, and placement constraints",
                        "Complete two walkthroughs without committing to equipment purchases",
                    ],
                    [
                        "Day 11: boarding contractor assembles sponsor submission packets",
                        "Check ownership, operating model, settlement account, and fulfillment",
                        "Produce complete-file checklists with merchant-confirmed factual information",
                        "Submit no file containing unresolved material identity inconsistencies",
                    ],
                    [
                        "Day 12: integration contractor reviews processor automation options",
                        "Scope P03 gateway and P09 dispute-event handling",
                        "Document integration eligibility, charges, refund limits, and reconciliation",
                        "Enable no automated refund without written merchant authorization",
                    ],
                    [
                        "Day 13: operator negotiates venue-specific ATM contract terms",
                        "Price exclusivity, revenue sharing, access, and removal rights",
                        "Obtain two written venue proposals with clear obligations",
                        "Reject locations lacking safe service access or defined custody",
                    ],
                    [
                        "Day 14: operator reviews merchant and venue pipeline evidence",
                        "Finish ten merchant conversations and four venue walkthroughs",
                        "Target three complete submissions and two written venue proposals",
                        "Classify missed targets by documented cause before allocating more hours",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Four Tactics That Preserve Residuals and Avoid Expensive Installations",
                "body": "Use contract detail and transaction evidence to improve the pilot before adding prospect volume.",
                "items": [
                    "Ask for an anonymized sample residual statement before signing Schedule A; locate every fee code and confirm whether gateway revenue shares use a different calculation.",
                    "Ask merchants about their latest repricing notice and unresolved support incident; a documented switching reason is stronger qualification than a generic savings promise.",
                    "Count venue cash requests during more than one operating period; weekend-only observations can materially overstate weekday withdrawal demand.",
                    "Negotiate ATM removal access and commission calculation together; exclusivity has little value when a weak location traps equipment behind an uncooperative counterparty.",
                ],
            },
        },
        {
            "heading": "3. Days 15–21: Activate Only Approved Accounts and Reconcile Every Dollar",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Days 15–17 run controlled activation only where external approvals and "
                    "contracts are complete. Candidate #32 has a canonical one-to-four-month "
                    "time to first deal, so a ready pipeline without a live account "
                    "can still be a valid first-month outcome. Do not force a transaction "
                    "through an unapproved MID to make the calendar look successful. For "
                    "each approved merchant, the integration contractor verifies descriptor, "
                    "terminal identifiers, authorized tender types, refund behavior, receipt "
                    "content, and funding instructions using the processor's supported test "
                    "procedures. Test P04 and P05 separately; a cash-discount label does not "
                    "repair an incorrectly implemented surcharge. Confirm the relevant state "
                    "rule, including New York General Business Law section 518 where "
                    "applicable, against the displayed total price. The operator owns the "
                    "commercial explanation, while the boarding contractor retains evidence "
                    "of merchant training and support contacts. For an approved ATM location, "
                    "the field contractor records installation, safe access, communications, "
                    "fee-screen behavior, and opening cash count with the cash custodian. "
                    "Perform controlled withdrawal and reversal checks through the approved "
                    "switch process. Do not store PIN data or full card credentials in "
                    "tickets. Any cash discrepancy, misleading fee display, or misdirected "
                    "settlement suspends that installation until corrected."
                ),
                (
                    "Days 18–19 separate pilot contribution from the annual scorecard. Consider "
                    "an illustrative merchant processing $10,000 monthly with a retained "
                    "twenty-basis-point spread: $10,000 multiplied by 0.002 produces $20, "
                    "and an $8 retained gateway markup produces $28 operator revenue. "
                    "With $3 incremental servicing cost, monthly contribution is $25; "
                    "$150 acquisition spending therefore requires six months of stable "
                    "contribution to recover. Merchant card sales are not operator revenue. "
                    "For an illustrative agency-style ATM contract, 200 monthly withdrawals "
                    "at $3.50 produce $700 customer surcharges. If the contract analysis "
                    "supports excluding $175 of venue entitlement and $100 of processor "
                    "entitlement from operator revenue, retained revenue is $425. Deduct "
                    "$120 cash servicing and $30 maintenance to obtain $275 location "
                    "contribution before shared overhead. Actual gross-versus-net presentation "
                    "requires the ASC 606 principal-agent assessment; do not net every "
                    "cost simply because cash passes through a settlement account. Label "
                    "these unit examples as planning assumptions until statements validate "
                    "them. P07 compares expected entitlements with processor reports, while "
                    "P11 tests whether surcharge changes improve contribution without "
                    "destroying withdrawals. Count completed, settled withdrawals rather "
                    "than balance inquiries, reversals, or attempted transactions."
                ),
                (
                    "Days 20–21 reconcile the scorecard and operating dashboard without "
                    "pretending that pilot receipts establish an annual run rate. Formula "
                    "v2.0 uses $90,000 retained annual operator revenue at a 30% net "
                    "margin for $27,000 owner profit, leaving $63,000 annual costs. "
                    "The Base case is $445,000 at 42.5%, producing $189,125 "
                    "profit and $255,875 costs. The Scaled case is $800,000 at "
                    "55%, producing $440,000 profit and $360,000 costs. Although "
                    "the canonical scorecard labels its revenue field gross revenue, "
                    "its specified basis here is retained ISO residuals, gateway "
                    "markups, and ATM surcharges, not merchant settlements or vault "
                    "principal. Preserve that basis in every comparison. Conservative "
                    "and Base use one full-time operator plus three contractors; "
                    "Scaled uses two full-time staff plus four contractors. Do not "
                    "attribute the Scaled result to the launch pod. The canonical "
                    "$1,500–$10,000 monthly operating range is a startup planning "
                    "reference, not a ceiling on every annual scenario's total costs. "
                    "Keep launch cash deployment, recurring expenses, direct costs, "
                    "and capital purchases in separate columns. Track accrued "
                    "residuals separately from cash received because processor "
                    "payment timing can leave profitable-looking growth unable to "
                    "pay next month's contractor invoices."
                ),
            ],
            "table": {
                "caption": "Days 15–21: Controlled Activation, Retained-Revenue Math, and Residual Evidence",
                "headers": [
                    "Daily execution owner and operating focus",
                    "Specific transaction or accounting work required",
                    "Evidence supporting the reported operating result",
                    "Exception threshold and required containment response",
                ],
                "rows": [
                    [
                        "Day 15: boarding contractor confirms each activation prerequisite",
                        "Match sponsor decisions to merchant identity and requested configuration",
                        "Retain approval reference, permitted category, and funding instructions",
                        "Hold every account lacking explicit permission for live processing",
                    ],
                    [
                        "Day 16: integration contractor performs supported merchant testing",
                        "Verify tender logic, receipts, descriptor, refunds, and gateway behavior",
                        "Store redacted test results and merchant training confirmation",
                        "Permit zero debit surcharge errors or misdirected settlement instructions",
                    ],
                    [
                        "Day 17: field contractor installs only fully ready locations",
                        "Test ATM communications, fee disclosure, withdrawal, and reversal handling",
                        "Record custodian count, terminal identifiers, and switch test evidence",
                        "Suspend dispensing after any unexplained physical cash discrepancy",
                    ],
                    [
                        "Day 18: operator reviews merchant-level retained contribution math",
                        "Calculate $28 revenue less $3 incremental servicing cost",
                        "Record $25 contribution and six-month recovery on $150 acquisition",
                        "Treat assumed volume as provisional until actual statements arrive",
                    ],
                    [
                        "Day 19: operator and field contractor examine ATM economics",
                        "Separate $700 surcharge collections from $425 retained revenue",
                        "Record $275 contribution after $150 direct operating costs",
                        "Apply this net presentation only when contract analysis supports it",
                    ],
                    [
                        "Day 20: boarding contractor reconciles processor entitlement evidence",
                        "Compare P07 expected residuals with available processor reporting",
                        "Track accrued amounts, received cash, and unresolved fee differences",
                        "Escalate unexplained variance above one percent or twenty-five dollars",
                    ],
                    [
                        "Day 21: operator reviews workload and annual-case comparability",
                        "Separate startup cash, direct expenses, overhead, and capital purchases",
                        "Reconcile all three scorecard revenue and profit pairs exactly",
                        "Stop expansion when exception work exhausts twelve reserved weekly hours",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Freeze the entitlement snapshot",
                    "action": "Export the effective Schedule A, merchant pricing, gateway terms, and ATM venue shares.",
                    "detail": "Attach effective dates and identifiers so later price changes cannot rewrite the original expected residual.",
                },
                {
                    "step": 2,
                    "title": "Match activity to settlement evidence",
                    "action": "Join merchant and terminal identifiers to processor reports, ATM switch records, and cash receipts.",
                    "detail": "Separate refunds, reversals, chargebacks, reserves, and settlement timing differences before calculating revenue.",
                },
                {
                    "step": 3,
                    "title": "Recalculate retained revenue and direct contribution",
                    "action": "Apply the documented presentation basis and subtract actual incremental servicing costs.",
                    "detail": "Investigate any unexplained difference exceeding either one percent of expected revenue or $25 for the account and period.",
                },
                {
                    "step": 4,
                    "title": "Close exceptions and authorize the next cohort",
                    "action": "Assign each discrepancy an owner, processor ticket, due date, and cash exposure.",
                    "detail": "Reconcile physical ATM cash independently; monetary tolerances for residual reviews never excuse an unexplained cash shortage.",
                },
            ],
        },
        {
            "heading": "4. Days 22–30 and Day-60/90 Reviews: Kill Broken Routes, Fix Bottlenecks, Scale Evidence",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Days 22–24 turn observations into a renewal and exception system. "
                    "The operator interviews every activated merchant and venue decision-maker, "
                    "logging unresolved funding, pricing, receipt, and service issues. P08 "
                    "captures the actual reason an account might leave; do not answer "
                    "every complaint with a permanent price concession. The boarding "
                    "contractor reconciles available settlement evidence, and the integration "
                    "contractor reviews P09 outcomes for duplicate alerts or unintended "
                    "refunds. Days 25–27 rehearse a terminal outage, a low-cash alert, "
                    "and a missing residual line using test notifications rather than "
                    "disrupting customers. Specify who acknowledges each alert and who "
                    "may dispatch service or change configuration. Target acknowledgment "
                    "within thirty minutes during contracted coverage and document "
                    "after-hours arrangements separately. Days 28–29 produce the decision "
                    "packet: cash spent and committed, qualified pipeline, sponsor "
                    "status, live accounts, first funding evidence, direct contribution, "
                    "support hours, and unresolved incidents. Report cohort denominators "
                    "alongside conversion and attrition percentages. One lost account "
                    "out of five is twenty percent, but that observation does not "
                    "establish a mature annual attrition rate. Day 30 is a resource "
                    "decision, not a demand that an external underwriting queue conform "
                    "to the operator's calendar. Preserve source evidence for the "
                    "next two reviews."
                ),
                (
                    "Apply the decision matrix in precedence order: Kill conditions "
                    "override Fix, and every Scale condition must hold together. "
                    "Kill means stop the affected route, account, or location, "
                    "cancel avoidable future spending, and execute contractual "
                    "closure; it does not mean abandon merchant support or "
                    "cash reconciliation. Kill immediately for fabricated boarding "
                    "information, unauthorized processing, unresolved diversion of "
                    "settlement funds, or an operating model the sponsor rejects. "
                    "A cash custody incident freezes the affected ATM pending "
                    "investigation rather than triggering an unexplained write-off. "
                    "Fix means a named defect, a measurable repair, a maximum "
                    "fourteen-day window, and no expansion spending on that "
                    "defect's route. At Day 30, Scale authorizes only another "
                    "bounded acquisition cohort: ten qualified merchant prospects, "
                    "three complete sponsor submissions, two written venue "
                    "proposals, reproducible unit economics, and spending within "
                    "$6,000. It does not require a live deal or authorize "
                    "speculative machine inventory. At Day 60, require five "
                    "funded merchants, one operating ATM, a reconciled settlement "
                    "cycle for each live route, positive direct contribution, "
                    "and merchant acquisition payback no longer than nine "
                    "months. These are management-selected thresholds, not "
                    "network standards. Sponsor-specific risk limits remain "
                    "independent operating constraints."
                ),
                (
                    "At Day 90, authorize a larger cohort only after ten "
                    "funded merchants and two live ATMs have produced at "
                    "least two reconciled settlement cycles per route, including "
                    "a complete residual period for merchants. Require positive "
                    "contribution for every location, merchant acquisition "
                    "payback within nine months, ATM installed-capital payback "
                    "within eighteen months, and positive aggregate contribution "
                    "in both latest completed months. Measure ATM payback "
                    "against equipment, installation, and acquisition spending; "
                    "report recoverable vault principal separately and still "
                    "charge its actual funding cost. Require at least ninety "
                    "percent merchant retention among accounts active sixty "
                    "days earlier, with the cohort count displayed. Smaller "
                    "or younger cohorts remain in Fix for insufficient "
                    "evidence rather than receiving a fabricated retention "
                    "score. Increase the next acquisition cohort by no more "
                    "than twenty-five percent, rounded down, and keep total "
                    "Day-90 operating cash deployment within $14,000 unless "
                    "a separately documented capital decision changes the "
                    "plan. Do not hire toward the six-person Scaled team "
                    "until observed support demand and collected contribution "
                    "can carry the added cost. If no deal has closed "
                    "because a credible sponsor process remains within the "
                    "stated one-to-four-month window, extend a capped validation "
                    "period; do not call that Scale."
                ),
            ],
            "table": {
                "caption": "Days 22–30 Execution and Quantitative Day-30/60/90 Kill, Fix, and Scale Decisions",
                "headers": [
                    "Execution date or explicit decision classification",
                    "Measurable condition with the relevant evidence",
                    "Required operator response and bounded resource allocation",
                    "Proof needed before the decision can change",
                ],
                "rows": [
                    [
                        "Day 22: operator interviews every activated account owner",
                        "Collect actual funding, pricing, and support complaints directly",
                        "Assign P08 retention tasks without automatic permanent discounting",
                        "Record owner-confirmed resolution or an explicit pending service action",
                    ],
                    [
                        "Day 23: boarding contractor closes available settlement exceptions",
                        "Compare receipts with expected residual and ATM entitlement calculations",
                        "Open processor tickets for each material unexplained revenue difference",
                        "Retain corrected statements or documented timing explanations with dates",
                    ],
                    [
                        "Day 24: integration contractor audits dispute automation outcomes",
                        "Review P09 duplicate events, refund authority, and processor status",
                        "Pause problematic rules while preserving manual customer support",
                        "Demonstrate correct event treatment before restoring automated refund behavior",
                    ],
                    [
                        "Day 25: integration contractor rehearses terminal outage handling",
                        "Send test alerts without interrupting actual merchant transactions",
                        "Measure acknowledgment against thirty-minute contracted-coverage service target",
                        "Record named responder, escalation path, and successful test closure",
                    ],
                    [
                        "Day 26: field contractor rehearses vault-cash alert handling",
                        "Test low-cash notices against custodian availability and service windows",
                        "Correct alert thresholds without moving money through operating accounts",
                        "Retain notification evidence and the authorized replenishment response plan",
                    ],
                    [
                        "Day 27: boarding contractor rehearses missing residual recovery",
                        "Trace a sample missing line through contracts and reports",
                        "Produce one complete P07 evidence package for processor review",
                        "Demonstrate reproducible entitlement math and a named recovery owner",
                    ],
                    [
                        "Day 28: operator prepares the cash and capacity packet",
                        "Include paid spending, outstanding commitments, and reserved support hours",
                        "Freeze discretionary purchases pending the scheduled Day-30 decision",
                        "Show first-month cash deployment within the authorized $6,000 ceiling",
                    ],
                    [
                        "Day 29: operator challenges pipeline and contribution assumptions",
                        "Separate submissions, approvals, live accounts, and funded transactions",
                        "Remove unsupported revenue claims from the resource decision packet",
                        "Attach source documents and cohort denominators to every reported metric",
                    ],
                    [
                        "Day 30: operator records the applicable decision explicitly",
                        "Apply Kill precedence before considering Fix or bounded Scale",
                        "Publish responsible owners and the next evidence review date",
                        "Retain the decision packet for Day-60 and Day-90 comparison",
                    ],
                    [
                        "Day 30 Kill: stop a structurally invalid operating route",
                        "Sponsor rejects the actual model or material information is fabricated",
                        "Cancel avoidable route spending while preserving contractual servicing duties",
                        "Require a genuinely valid authorized route before reconsidering deployment",
                    ],
                    [
                        "Day 30 Fix: repair readiness without forcing premature activation",
                        "Fewer than three complete submissions or two written venue proposals",
                        "Assign fourteen-day repairs and keep total spending within $6,000",
                        "Show completed files, executable proposals, or documented external review timing",
                    ],
                    [
                        "Day 30 Scale: authorize only a bounded second prospect cohort",
                        "Ten qualified prospects, three submissions, two proposals, and reproducible economics",
                        "Allow at most ten additional merchant prospects and two venue proposals",
                        "Confirm sponsor authority, no critical incidents, and intact operating liquidity",
                    ],
                    [
                        "Day 60 Kill: close routes that cannot produce viable contribution",
                        "Documented best executable terms still produce nonpositive direct contribution",
                        "Stop acquisition for that route and remove avoidable fixed commitments",
                        "Require new executable terms demonstrating positive contribution before reopening",
                    ],
                    [
                        "Day 60 Fix: repair conversion, evidence, or route economics",
                        "Fewer than five funded merchants or one operating ATM",
                        "Use fourteen-day corrective actions within the cumulative $10,000 ceiling",
                        "Document sponsor progress, reconciled receipts, and a credible activation date",
                    ],
                    [
                        "Day 60 Scale: increase acquisition only after initial reconciliation",
                        "Five funded merchants, one ATM, and positive direct route contribution",
                        "Add at most five merchant prospects and one contracted location",
                        "Show one reconciled cycle, merchant payback within nine months, and no critical incidents",
                    ],
                    [
                        "Day 90 Kill: exit persistently uneconomic routes after repairs",
                        "Two completed monthly periods remain nonpositive after documented corrective action",
                        "Stop new exposure and execute contract-specific servicing or removal plans",
                        "Require credible executable economics rather than speculative future transaction growth",
                    ],
                    [
                        "Day 90 Fix: preserve capital while evidence remains insufficient",
                        "Scale evidence fails, but sponsor timing or specific repairs remain credible",
                        "Hold expansion and document any extension within remaining authorized cash",
                        "Show dated sponsor milestones, resolved defects, and a revised evidence deadline",
                    ],
                    [
                        "Day 90 Scale: expand only proven merchant and ATM cohorts",
                        "Ten funded merchants, two ATMs, and two positive completed months",
                        "Increase next acquisition cohort by at most twenty-five percent",
                        "Require two reconciled cycles, merchant payback within nine months, ATM payback within eighteen months, ninety percent eligible-cohort retention, positive contribution at every location, no critical incidents, and spending within $14,000",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "Scale the reconciled retained dollar, not the signed application, the settlement balance, or the machine count.",
    "diagram_id": "diag-08",
    "action_checklist": [
        "Assign P01–P12 to the one-full-time, three-contractor pod, reserving twelve of sixty weekly hours for exceptions and support.",
        "Obtain sponsor authority, current Schedule A, underwriting criteria, residual rights, and documented rules for each proposed pricing configuration.",
        "Create separate operating and vault-cash controls, cap first-month operating deployment at $6,000, and preserve the planned $6,000 Day-90 operating reserve.",
        "Complete thirty named merchant prospects, ten venue prospects, ten merchant conversations, four venue walkthroughs, and evidence-backed submission targets.",
        "Test every approved merchant configuration and ATM fee screen, then reconcile retained revenue, cash custody, direct contribution, and processor payment timing.",
        "Record Day-30/60/90 Kill, Fix, or Scale decisions using the specified evidence, payback limits, spending ceilings, and fourteen-day repair windows.",
    ],
    "statutory_citations": [
        {
            "title": "12 CFR 1005.16 — Disclosures at automated teller machines",
            "url": "https://www.ecfr.gov/current/title-12/chapter-X/part-1005/section-1005.16",
            "relevance": (
                "An ATM operator imposing a covered fee must provide the required amount "
                "disclosure on screen or paper before commitment and obtain the consumer's "
                "election to continue; include this in installation testing."
            ),
        },
        {
            "title": "15 U.S.C. 1693o-2 — Reasonable fees and rules for payment card transactions",
            "url": "https://www.law.cornell.edu/uscode/text/15/1693o-2",
            "relevance": (
                "Provides the statutory framework for debit interchange and payment-card "
                "network restrictions, including specified discount protections; do not "
                "misread those protections as blanket authorization for debit surcharges."
            ),
        },
        {
            "title": "12 CFR 235.7 — Limitations on payment card restrictions",
            "url": "https://www.ecfr.gov/current/title-12/chapter-II/subchapter-A/part-235/section-235.7",
            "relevance": (
                "Addresses debit network exclusivity and routing restrictions; terminal "
                "and processor choices must preserve applicable merchant routing rights."
            ),
        },
        {
            "title": "31 CFR 1010.100(ff) — Money services business definitions",
            "url": "https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1010/section-1010.100",
            "relevance": (
                "Assess the operator's actual activities against the MSB definitions, "
                "especially before adding transfers or exchange services beyond "
                "conventional ATM withdrawals."
            ),
        },
        {
            "title": "New York General Business Law section 518 — Credit card surcharge pricing",
            "url": "https://www.nysenate.gov/legislation/laws/GBS/518",
            "relevance": (
                "For applicable New York transactions, evaluate the current surcharge "
                "limit and total-price posting requirements before configuring merchant "
                "signage, menus, receipts, or terminal pricing."
            ),
        },
    ],
}
