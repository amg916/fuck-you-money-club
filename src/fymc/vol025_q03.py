from __future__ import annotations

CHAPTER_3 = {
    "id": "Q3",
    "chapter_id": "Q3",
    "chapter_number": 3,
    "question_number": 3,
    "slug": "freight-brokerage-unit-economics-margin-waterfall-working-capital",
    "question_prompt": "What are the real unit economics, gross-to-net margin deductions, scrub/reversal reserves, and working-capital float requirements for freight brokerage?",
    "kicker": "Q3 / THE BIG MONEY PLAYBOOKS",
    "title": "Unit Economics, Margin Waterfall & Working-Capital Float",
    "subtitle": "Shipper Receivables, Carrier Payables, Highway/RMIS Controls, BMC-84/BMC-85 Security, and Recovery-Fee Economics",
    "layout_template": "financial_breakdown",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #12, Freight Brokerage, ranks #25 with a Money-to-Manpower Score "
        "of 62/100 because spread is earned load by load while cash leaves before "
        "shippers pay. The canonical annual owner profits are $30,000 Conservative, "
        "$165,000 Base, and $400,000 Scaled on $1 million, $3 million, and $5 million "
        "of gross shipper billings. This chapter maps eight operating plays: niche-lane "
        "procurement, detention collection, carrier verification, quick-pay pricing, "
        "shipper credit control, invoice reconciliation, contingency auditing, and "
        "float treasury. It separates carrier pass-through, employee and contractor "
        "labor, acquisition expense, reversals, and financing. Explicit DSO and "
        "carrier-payment assumptions expose why a profitable brokerage can exhaust "
        "its cash before its next growth milestone."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$1,000,000",
            "context": "Annual gross shipper billings including carrier costs",
            "note": "3% net margin; $30,000 annual owner net profit; 3 FT + 2 C",
        },
        {
            "label": "Base",
            "value": "$3,000,000",
            "context": "Annual gross shipper billings including carrier costs",
            "note": "5.5% net margin; $165,000 annual owner net profit; 3 FT + 2 C",
        },
        {
            "label": "Scaled",
            "value": "$5,000,000",
            "context": "Annual gross shipper billings including carrier costs",
            "note": "8% net margin; $400,000 annual owner net profit; 4 FT + 3 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Reconcile every load from shipper billing to owner profit",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Begin with the scorecard's measurement boundary: revenue means gross "
                    "shipper billings including purchased transportation, not the broker's "
                    "retained spread. Actual financial statements require a separate "
                    "principal-versus-agent assessment; a net presentation changes the "
                    "revenue denominator without manufacturing additional cash or profit. "
                    "The illustrative annual cohorts contain 500, 1,500, and 2,500 delivered "
                    "loads, each averaging $2,000 billed. Carrier purchases average $1,500, "
                    "$1,600, and $1,560 per load, producing gross spreads of $500, $400, "
                    "and $440. Those differences represent different customer and lane "
                    "mixes, not a promise that procurement improves automatically with "
                    "size. Conservative deliberately assumes a concentrated, higher-spread "
                    "niche whose small volume absorbs fixed labor poorly. Base broadens "
                    "the book at a thinner spread; Scaled gains density and purchasing "
                    "discipline. Preserve separate load identifiers for original tenders, "
                    "rebooks, accessorial amendments, carrier settlements, and shipper "
                    "credits. Otherwise, a canceled booking can leave phantom revenue "
                    "while a replacement carrier creates a second payable. The waterfall "
                    "below is an explicit cost allocation constructed to reconcile the "
                    "canonical outcomes, rather than additional scorecard data or vendor "
                    "pricing. Its owner-profit residual follows all listed business "
                    "expenses; personal taxes and owner distributions sit outside this "
                    "operating model."
                ),
                (
                    "Labor must remain visible even when an owner dispatches after "
                    "hours. Annual loaded employee budgets are $150,000, $240,000, and "
                    "$360,000 for three, three, and four full-time positions respectively. "
                    "These imply average loaded costs of $50,000, $80,000, and $90,000; "
                    "validate local wages, payroll taxes, benefits, and the owner's "
                    "working-role compensation before accepting them. Contractor delivery "
                    "support adds $24,000, $48,000, and $84,000, equivalent to 800, "
                    "1,600, and 2,800 purchased hours at an illustrative $30 hourly "
                    "rate. The two, two, and three contractors are fractional resources, "
                    "not additional full-time equivalents. Assign their hours to "
                    "check-calls, appointment recovery, document collection, and invoice "
                    "exceptions. Contractor expense per delivered load is consequently "
                    "$48, $32, and $33.60. Keep commissions inside the stated labor "
                    "buckets or disclose a replacement allocation; quietly adding "
                    "commissions later breaks the reconciliation. Employee and contractor "
                    "classification depends on the actual relationship, not the "
                    "spreadsheet label. If the Conservative employee budget proves "
                    "$30,000 too low, its entire annual owner profit disappears. Track "
                    "after-hours coverage and exception minutes alongside shipment "
                    "count so nominal automation savings do not merely become "
                    "unpaid owner labor."
                ),
                (
                    "Acquisition expense is $12,000, $36,000, and $60,000, supporting "
                    "six, eighteen, and thirty newly acquired shipper accounts at "
                    "$2,000 incremental CAC each. These are acquisition counts, not "
                    "an assumption that every load comes from a new account. For "
                    "a new Base account contributing twenty loads, gross spread "
                    "is $8,000; subtracting $640 of contractor support and $400 "
                    "of expected losses leaves $6,960 before allocated employee, "
                    "platform, financing, and other costs. That contribution covers "
                    "the $2,000 incremental acquisition outlay after roughly six "
                    "comparable loads, but collection timing still controls cash "
                    "payback. A fully loaded CAC report should add attributed "
                    "employee selling time while eliminating the corresponding "
                    "double count from payroll when reconciling totals. Keep "
                    "software and integration costs at $12,000, $24,000, and "
                    "$42,000; loss provisions at $10,000, $30,000, and $50,000; "
                    "financing at $6,000, $24,000, and $40,000; and other overhead "
                    "at $6,000, $33,000, and $64,000. These deductions produce "
                    "exact owner profits of $30,000, $165,000, and $400,000. "
                    "Divide by delivered loads to obtain $60, $110, and $160 "
                    "of owner profit, rather than mistaking the much larger "
                    "gross spread for distributable earnings."
                ),
            ],
            "table": {
                "caption": "Annual Cohort Waterfall: Explicit Allocations Reconciled to All Three Canonical Cases",
                "headers": [
                    "Waterfall line and operator accounting treatment",
                    "Conservative annual cohort with 500 delivered loads",
                    "Base annual cohort with 1,500 delivered loads",
                    "Scaled annual cohort with 2,500 delivered loads",
                ],
                "rows": [
                    [
                        "Start with gross shipper invoices before purchased transportation",
                        "$1,000,000 billed across five hundred completed customer shipments",
                        "$3,000,000 billed across fifteen hundred completed customer shipments",
                        "$5,000,000 billed across twenty-five hundred completed customer shipments",
                    ],
                    [
                        "Deduct contracted carrier linehaul and carrier accessorial purchases",
                        "$750,000 deducted for verified carrier transportation and accessorials",
                        "$2,400,000 deducted for verified carrier transportation and accessorials",
                        "$3,900,000 deducted for verified carrier transportation and accessorials",
                    ],
                    [
                        "Retain gross spread before brokerage operating expense deductions",
                        "$250,000 retained spread equals twenty-five percent of gross billings",
                        "$600,000 retained spread equals twenty percent of gross billings",
                        "$1,100,000 retained spread equals twenty-two percent of gross billings",
                    ],
                    [
                        "Deduct loaded employee compensation including working-owner role compensation",
                        "$150,000 allocated across three full-time operating team positions",
                        "$240,000 allocated across three full-time operating team positions",
                        "$360,000 allocated across four full-time operating team positions",
                    ],
                    [
                        "Deduct fractional contractor delivery support and exception handling",
                        "$24,000 purchases eight hundred contractor hours across two people",
                        "$48,000 purchases sixteen hundred contractor hours across two people",
                        "$84,000 purchases twenty-eight hundred contractor hours across three people",
                    ],
                    [
                        "Deduct incremental shipper acquisition spending without duplicating payroll",
                        "$12,000 supports six acquired accounts at $2,000 incremental CAC",
                        "$36,000 supports eighteen acquired accounts at $2,000 incremental CAC",
                        "$60,000 supports thirty acquired accounts at $2,000 incremental CAC",
                    ],
                    [
                        "Deduct transportation software subscriptions and recurring integration support",
                        "$12,000 funds transportation systems and recurring data integration support",
                        "$24,000 funds transportation systems and recurring data integration support",
                        "$42,000 funds transportation systems and recurring data integration support",
                    ],
                    [
                        "Deduct modeled credit losses and unrecovered settlement adjustments",
                        "$10,000 provisions one percent of annual gross shipper billings",
                        "$30,000 provisions one percent of annual gross shipper billings",
                        "$50,000 provisions one percent of annual gross shipper billings",
                    ],
                    [
                        "Deduct financing interest and fees under explicit borrowing assumptions",
                        "$6,000 annual financing budget requires validation against lender terms",
                        "$24,000 annual financing budget requires validation against lender terms",
                        "$40,000 annual financing budget requires validation against lender terms",
                    ],
                    [
                        "Deduct remaining insurance administration and other operating overhead",
                        "$6,000 remaining overhead must fit actual insurance and administration",
                        "$33,000 remaining overhead must fit actual insurance and administration",
                        "$64,000 remaining overhead must fit actual insurance and administration",
                    ],
                    [
                        "Retain canonical annual owner profit after every listed deduction",
                        "$30,000 owner profit equals three percent of gross billings",
                        "$165,000 owner profit equals 5.5 percent of gross billings",
                        "$400,000 owner profit equals eight percent of gross billings",
                    ],
                ],
            },
        },
        {
            "heading": "2. Scrub invoices, reserve reversals, and price eight operating plays",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Treat scrub as the process that converts an operational event "
                    "into an enforceable, supported invoice, not as a mysterious "
                    "percentage withheld from every shipment. Match the shipper "
                    "tender, signed rate confirmation, delivery evidence, carrier "
                    "invoice, and authorized accessorial record before billing. "
                    "For detention, capture arrival, release, appointment, free "
                    "time, and the applicable contractual rate. Four hours on "
                    "site with two free hours at $75 per compensable hour "
                    "supports $150, not $300. If the broker owes the carrier "
                    "$100, retained incremental spread is $50 before collection "
                    "and handling expense. Never assume tracking pings alone "
                    "prove the customer's detention obligation. The annual "
                    "one-percent loss provision can be analytically divided "
                    "into 0.50% shipper credit loss, 0.30% unsupported billing "
                    "or credit adjustments, and 0.20% unrecovered carrier "
                    "settlement or claims-related costs. Base therefore assigns "
                    "$15,000, $9,000, and $6,000 to those categories. Financial "
                    "reporting must classify revenue reductions separately from "
                    "credit expense where appropriate; this management waterfall "
                    "combines them only to expose economic leakage. Reconcile "
                    "opening reserve plus current provision less utilized "
                    "amounts to closing reserve. A posted credit must not "
                    "also become a second loss when the invoice finally closes."
                ),
                (
                    "The supplied canonical play is freight_detention_audit_contingency, "
                    "covering automated parcel, LTL freight, and tariff overcharge "
                    "contingency auditing under TRACK_1. The remaining seven labels "
                    "in the matrix are chapter-local operating mappings, not "
                    "additional asserted catalog identifiers. Obtain shipper-authorized, "
                    "read-only UPS, FedEx, and LTL billing feeds through supported "
                    "APIs, EDI delivery, or controlled exports. Obtain CBP Form "
                    "7501 entry summaries from the authorized importer or its "
                    "customs service provider; do not assume a universal public "
                    "API exposes entry records. Reconcile invoice lines to "
                    "negotiated tariffs, dimensions, weights, service commitments, "
                    "and actual delivery events. A $25,000 realized recovery "
                    "at a 40% contingency produces $10,000 of operator fee "
                    "revenue, not $25,000 and certainly not the underlying "
                    "freight spend. Deduct $2,000 specialist labor, $1,000 "
                    "acquisition, $500 data handling, and a $1,000 reversal "
                    "reserve to obtain $5,500 contribution before allocated "
                    "fixed overhead. The 35–50% fee range produces $8,750–$12,500 "
                    "revenue on that same recovery. These are illustrative "
                    "sidecar economics, excluded from the canonical brokerage "
                    "totals unless an explicit offsetting allocation incorporates "
                    "them. Require account-level proof that collected benefits "
                    "belong to the contracted customer."
                ),
                (
                    "Refund eligibility and drawback eligibility require different "
                    "evidence. Parcel service guarantees may be suspended or "
                    "contractually waived; LTL classifications depend on the "
                    "shipment and governing tariff. When service-refund claims "
                    "fail, pivot toward duplicate charges, dimensional-weight "
                    "errors, LTL freight-class corrections, and contract-rate "
                    "benchmarking recoveries. Target defensible billing errors "
                    "where service-guarantee waivers do not control the claim, "
                    "while still checking billing-dispute deadlines and "
                    "contractual limitations. Duty drawback under 19 U.S.C. "
                    "1313 requires a qualifying statutory pathway and "
                    "supporting import, export, or destruction records; Form "
                    "7501 alone establishes no refund entitlement. Route "
                    "regulated customs business through appropriately licensed "
                    "or otherwise authorized participants under 19 U.S.C. "
                    "1641 and 19 CFR 111.2. Contract contingency fees against "
                    "actually realized refunds or usable credits and define "
                    "clawback treatment. A ninety-day recovery cycle can "
                    "require the $3,500 of delivery, acquisition, and data "
                    "spending before any fee arrives; the additional $1,000 "
                    "reserve is retained protection, not immediate vendor "
                    "spend. Use carrier identity controls from Highway or "
                    "RMIS alongside independent FMCSA checks and verified "
                    "bank-change callbacks. A clean platform status does "
                    "not establish who actually collected the shipment or "
                    "who controls the remittance account."
                ),
            ],
            "table": {
                "caption": "Eight Mapped Operating Plays: Unit Math, Evidence, and Risk Fallbacks",
                "headers": [
                    "Mapped operating play and defined commercial boundary",
                    "Concrete unit economics for the operator",
                    "Evidence required before counting the economic benefit",
                    "Failure mode and practical fallback operating response",
                ],
                "rows": [
                    [
                        "Niche-lane procurement uses repeat demand rather than speculative capacity",
                        "A $2,000 invoice less $1,600 carrier purchase yields $400",
                        "Retain matched tender, accepted carrier rate, and delivery evidence",
                        "If spot prices rise, reprice future tenders or decline coverage",
                    ],
                    [
                        "Detention collection converts documented waiting time into supported accessorials",
                        "Collect $150 detention, pay $100 carrier, retain $50 spread",
                        "Preserve appointment, arrival, release, free-time allowance, and authorization records",
                        "If authorization fails, remove unsupported revenue and repair customer terms",
                    ],
                    [
                        "Carrier verification protects purchased transportation from impersonation and diversion",
                        "A $12 incremental review costs 0.6% of $2,000 billing",
                        "Cross-check Highway or RMIS with authority, identity, and bank ownership",
                        "When identity conflicts persist, use a separately verified replacement carrier",
                    ],
                    [
                        "Quick-pay pricing exchanges earlier carrier cash for an agreed discount",
                        "Two percent of a $1,600 settlement equals $32 discount",
                        "Record carrier election, actual settlement timing, and lender funding cost",
                        "Reject discounts below financing cost plus fraud and administration exposure",
                    ],
                    [
                        "Shipper credit control limits concentration before receivables become stranded",
                        "An $80,000 receivable ceiling supports forty unpaid $2,000 invoices",
                        "Aggregate delivered unbilled loads, receivables, disputes, and pending tenders",
                        "Require prepayment or reduce new exposure when limits are exhausted",
                    ],
                    [
                        "Invoice reconciliation prevents duplicate settlement and unsupported shipper billing",
                        "Preventing one duplicate $1,600 payment preserves sixteen $100 contributions",
                        "Match load identifier, carrier invoice number, amount, and payment trace",
                        "Quarantine conflicting invoices for review without delaying unrelated valid obligations",
                    ],
                    [
                        "freight_detention_audit_contingency: Automated Parcel, LTL Freight & Tariff Overcharge Contingency Auditing — TRACK_1",
                        "$25,000 recovered at forty percent generates $10,000 operator fee",
                        "Retain authorized billing feeds, applicable tariffs, entry records, and receipts",
                        "Pivot to dimensional, duplicate-charge, class, and contract-rate recovery rules",
                    ],
                    [
                        "Float treasury aligns invoice collectability with promised carrier payment dates",
                        "Base carrier funding gap equals $2,400,000 times thirty divided by 365",
                        "Maintain invoice-level collection forecasts and settlement-date carrier payable schedules",
                        "Use committed eligible funding or constrain tenders before liquidity fails",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Protect the spread before celebrating the shipment",
                "body": (
                    "Small operational exceptions become material when they repeat across "
                    "an entire shipper cohort; instrument the repeatable failure first."
                ),
                "items": [
                    "Export detention events weekly with appointment and release evidence; bill only compensable hours under the customer's actual terms.",
                    "Require an independently sourced callback for carrier bank changes; an emailed voided check is supporting evidence, not identity verification.",
                    "Age audit recoveries from documented customer realization, not from the date an analyst first flags an apparent overcharge.",
                    "Code every credit by original load and root cause so sales concessions, document failures, and shipper insolvency remain distinguishable.",
                ],
            },
        },
        {
            "heading": "3. Fund the collection gap without treating security as spendable cash",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Model working capital with a daily convention before quoting "
                    "a growth target. Assume uniform annual activity over 365 "
                    "days, shipper DSO of 45, 45, and 50 days, and "
                    "effective carrier payment timing of 15, 15, and 14 "
                    "days after delivery. DSO here includes delivery-to-invoice "
                    "delay; operational dashboards should separately show that "
                    "delay and invoice-to-cash aging. Carrier payment timing "
                    "must likewise reflect actual settlement, not contractual "
                    "terms that the business routinely overrides. The "
                    "carrier-cost bridge equals annual carrier purchases "
                    "divided by 365, multiplied by DSO less payment days. "
                    "It is approximately $61,644 Conservative, $197,260 Base, "
                    "and $384,658 Scaled. This bridge answers how much "
                    "purchased transportation is funded between carrier "
                    "settlement and corresponding customer collection; it "
                    "does not include every business cash requirement. "
                    "A document-related payout lock is a specific, "
                    "contractually supported settlement condition, not an "
                    "unlimited financing option. Track invoice receipt, "
                    "proof-of-delivery completeness, exception resolution, "
                    "and due date independently. Valid carrier obligations "
                    "remain obligations even when the shipper disputes "
                    "its own invoice. Repeatedly stretching carriers can "
                    "remove trusted capacity precisely when a growing "
                    "brokerage needs reliable service and stronger "
                    "procurement leverage."
                ),
                (
                    "A complementary balance-sheet measure is gross receivables "
                    "less carrier payables. Multiply shipper billings by "
                    "DSO over 365, then subtract carrier purchases times "
                    "payment days over 365. The resulting trading working "
                    "capital is approximately $92,466, $271,233, and $535,342. "
                    "It exceeds the carrier-cost bridge because billed "
                    "spread is also awaiting collection. These are "
                    "alternative views of the same operating cycle; "
                    "never add the two totals. For a planning cushion, "
                    "add fourteen days of noncarrier cash operating "
                    "expense, excluding the noncash loss provision. "
                    "Annual cash expenses on that definition are "
                    "$210,000, $405,000, and $650,000, producing cushions "
                    "of roughly $8,055, $15,534, and $24,932. Trading "
                    "working capital plus those cushions is therefore "
                    "about $100,521, $286,767, and $560,274. Round "
                    "illustrative accessible-liquidity targets upward to "
                    "$110,000, $320,000, and $610,000 before separately "
                    "assessing concentrated defaults, seasonality, or "
                    "restricted security. These targets are planning "
                    "choices, not lender commitments. Build a thirteen-week "
                    "cash schedule to capture actual invoice batches, "
                    "payroll dates, tax payments, deposits, and facility "
                    "draws; steady-state averages can hide a severe "
                    "Friday settlement shortfall. Undrawn facilities "
                    "count only to the extent their borrowing conditions "
                    "are actually satisfied."
                ),
                (
                    "The $50,000–$250,000 startup capital range does not "
                    "automatically fund the Base or Scaled receivables "
                    "book. A $250,000 cash contribution falls $70,000 "
                    "short of the illustrative Base liquidity target "
                    "before restricted collateral or formation spending. "
                    "FMCSA property-broker authority and financial "
                    "responsibility are separate requirements under "
                    "49 U.S.C. 13904 and 13906 and 49 CFR "
                    "387.307. The $75,000 BMC-84 surety bond or "
                    "BMC-85 trust security amount is neither automatic "
                    "credit availability nor necessarily a $75,000 "
                    "expense. Bond premium is expense; required "
                    "collateral consumes liquidity; trust assets "
                    "cannot simultaneously fund carrier payroll-like "
                    "settlement runs. Verify current instrument, "
                    "provider, replenishment, and authority-status "
                    "requirements before operating. Compare a bank "
                    "receivables line with factoring using advance "
                    "rate, eligible collateral, concentration limits, "
                    "recourse, reserve release, minimum fees, and "
                    "notification requirements. At an 85% advance, "
                    "Base gross receivables of about $369,863 "
                    "produce at most $314,384 before exclusions "
                    "and facility limits. That is below the "
                    "$320,000 planning target even when every "
                    "invoice qualifies. A recourse factor accelerates "
                    "cash without necessarily transferring shipper "
                    "default risk. Keep financing budgets provisional "
                    "until actual balances, rate tiers, and fee "
                    "schedules reproduce them."
                ),
            ],
            "table": {
                "caption": "Daily Float Model: Separate Carrier Funding, Trading Working Capital, and Accessible Liquidity",
                "headers": [
                    "Funding measure and calculation boundary",
                    "Conservative funding assumptions and resulting dollars",
                    "Base funding assumptions and resulting dollars",
                    "Scaled funding assumptions and resulting dollars",
                ],
                "rows": [
                    [
                        "Set delivery-to-cash days and actual carrier settlement days",
                        "Forty-five collection days less fifteen settlement days creates thirty days",
                        "Forty-five collection days less fifteen settlement days creates thirty days",
                        "Fifty collection days less fourteen settlement days creates thirty-six days",
                    ],
                    [
                        "Calculate carrier purchases exposed during the collection gap",
                        "$750,000 divided by 365 times thirty equals approximately $61,644",
                        "$2,400,000 divided by 365 times thirty equals approximately $197,260",
                        "$3,900,000 divided by 365 times thirty-six equals approximately $384,658",
                    ],
                    [
                        "Calculate gross receivables before credit exclusions or lender haircuts",
                        "$1,000,000 times forty-five divided by 365 equals approximately $123,288",
                        "$3,000,000 times forty-five divided by 365 equals approximately $369,863",
                        "$5,000,000 times fifty divided by 365 equals approximately $684,932",
                    ],
                    [
                        "Subtract carrier payables to calculate trading working capital",
                        "$123,288 receivables less $30,822 carrier payables leaves approximately $92,466",
                        "$369,863 receivables less $98,630 carrier payables leaves approximately $271,233",
                        "$684,932 receivables less $149,589 carrier payables leaves approximately $535,342",
                    ],
                    [
                        "Add fourteen days of noncarrier cash operating expense",
                        "$210,000 annual cash expense creates approximately $8,055 additional cushion",
                        "$405,000 annual cash expense creates approximately $15,534 additional cushion",
                        "$650,000 annual cash expense creates approximately $24,932 additional cushion",
                    ],
                    [
                        "Set rounded accessible-liquidity targets excluding restricted financial security",
                        "$110,000 planning target exceeds approximately $100,521 modeled requirement",
                        "$320,000 planning target exceeds approximately $286,767 modeled requirement",
                        "$610,000 planning target exceeds approximately $560,274 modeled requirement",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Verify four funding conditions before increasing accepted loads",
                "body": (
                    "Authorize additional shipment exposure only when the shipment-level "
                    "records and the treasury schedule support the promised settlements."
                ),
                "items": [
                    "Reconcile delivery-to-invoice delay and invoice-to-cash aging to the assumed DSO; investigate excluded disputes and delivered unbilled shipments.",
                    "Confirm carrier due dates and quick-pay elections against available cash, rather than assuming every carrier accepts the modeled payment interval.",
                    "Verify current FMCSA authority and $75,000 financial-security support; exclude restricted trust assets and pledged collateral from usable liquidity.",
                    "Recalculate lender availability after debtor concentration, aging, disputes, reserves, and recourse exposure; fund the remaining gap before accepting more tenders.",
                ],
            },
        },
        {
            "heading": "4. Stress the cohort and turn exceptions into a weekly cash SOP",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Stress purchase cost and collection quality independently "
                    "before combining them. A two-percentage-point increase "
                    "in carrier cost as a share of gross billings "
                    "removes $20,000, $60,000, and $100,000 from annual "
                    "profit when customer pricing stays unchanged. "
                    "Owner profit falls to $10,000, $105,000, and "
                    "$300,000. An additional one-percentage-point loss "
                    "provision removes another $10,000, $30,000, and "
                    "$50,000. Together those operating shocks leave "
                    "$0, $75,000, and $250,000 before any financing "
                    "effect. Do not label a two-point revenue "
                    "deduction as a two-percent carrier-price increase: "
                    "the denominators differ. On Base carrier purchases "
                    "of $2.4 million, a literal two-percent purchase "
                    "increase is $48,000, whereas two points of "
                    "$3 million billings is $60,000. Use both "
                    "views during bid review and state the "
                    "chosen denominator in the customer cohort "
                    "report. Concentration produces a different "
                    "shock: a single $50,000 unrecovered shipper "
                    "balance exceeds Conservative annual profit "
                    "before any offsetting reserve release. Model "
                    "such events against existing provisions so "
                    "the same expected loss is not charged "
                    "twice. Future volume can be repriced; "
                    "completed shipments need a collections and "
                    "settlement plan rather than optimistic "
                    "replacement bookings."
                ),
                (
                    "Extend DSO by fifteen days without changing "
                    "carrier payment behavior. Additional gross "
                    "receivables become approximately $41,096, "
                    "$123,288, and $205,479. If a lender funds "
                    "the entire incremental balance at an "
                    "illustrative 12% annual rate and the "
                    "extension persists throughout a full year, "
                    "incremental annual interest is $4,932, "
                    "$14,795, and $24,658. A temporary delay "
                    "requires interest based on actual duration, "
                    "not this sustained annualization. Funding "
                    "availability is a separate question: an "
                    "aging invoice may lose eligibility just "
                    "when cash is needed most. Combining "
                    "the carrier-cost shock, extra losses, "
                    "and sustained collection delay produces "
                    "approximately negative $4,932, positive "
                    "$60,205, and positive $225,342 in annual "
                    "owner profit. Compare that with replacing "
                    "the entire original financing budget "
                    "with a simple 2% fee on every "
                    "gross invoice. Annual fees would be "
                    "$20,000, $60,000, and $100,000, yielding "
                    "profits of $16,000, $129,000, and "
                    "$340,000 after removing the old "
                    "financing expense first. This fee-only "
                    "comparison excludes additional interest "
                    "and service charges; actual proposals "
                    "must be modeled from their complete "
                    "schedules. Never add a replacement "
                    "financing fee while retaining an "
                    "expense it explicitly replaces."
                ),
                (
                    "Run the operating review from one immutable "
                    "weekly shipment extract, then reconcile it "
                    "to accounting and bank activity. Segment "
                    "by shipper, lane, equipment, salesperson, "
                    "carrier, invoice month, and exception "
                    "reason. A Base load yielding $400 "
                    "spread but requiring five extra contractor "
                    "hours at $30 consumes $150 before "
                    "employee escalation or credit loss. "
                    "If that pattern repeats across one "
                    "hundred loads, $15,000 of contribution "
                    "vanishes even though headline gross "
                    "margin appears healthy. Separate these "
                    "exceptions from normal delivery support "
                    "to determine whether the modeled "
                    "$48,000 contractor budget still holds. "
                    "Use TMS event timestamps, accounting "
                    "payment traces, and bank reconciliation "
                    "rather than salesperson estimates. "
                    "Maintain the transaction records required "
                    "by 49 CFR 371.3, including compensation "
                    "and freight-charge information, and "
                    "preserve applicable access rights. "
                    "Assign each exception an owner, "
                    "evidence requirement, recovery amount, "
                    "and next action date. Escalate "
                    "unresolved identity conflicts separately "
                    "from ordinary missing paperwork. "
                    "Finish each review with a signed "
                    "cash forecast that states which "
                    "customer exposure can grow, which "
                    "needs prepayment, and which should "
                    "stop receiving new tenders. Profit "
                    "is usable only when the corresponding "
                    "cash survives collection, settlement, "
                    "and correction."
                ),
            ],
            "table": {
                "caption": "Annual Sensitivity Tests: Hold All Unmentioned Inputs Constant",
                "headers": [
                    "Explicit stress definition and accounting treatment",
                    "Conservative annual owner-profit result or funding change",
                    "Base annual owner-profit result or funding change",
                    "Scaled annual owner-profit result or funding change",
                ],
                "rows": [
                    [
                        "Baseline uses the exact canonical revenue and profit cases",
                        "$30,000 annual owner profit before any additional modeled stress",
                        "$165,000 annual owner profit before any additional modeled stress",
                        "$400,000 annual owner profit before any additional modeled stress",
                    ],
                    [
                        "Carrier cost increases by two percentage points of gross billings",
                        "$10,000 profit remains after subtracting $20,000 additional carrier expense",
                        "$105,000 profit remains after subtracting $60,000 additional carrier expense",
                        "$300,000 profit remains after subtracting $100,000 additional carrier expense",
                    ],
                    [
                        "Loss provision increases alone by one percentage point of billings",
                        "$20,000 profit remains after subtracting $10,000 additional expected losses",
                        "$135,000 profit remains after subtracting $30,000 additional expected losses",
                        "$350,000 profit remains after subtracting $50,000 additional expected losses",
                    ],
                    [
                        "DSO extends fifteen days with sustained twelve-percent incremental borrowing",
                        "Approximately $41,096 additional funding creates $4,932 annual incremental interest",
                        "Approximately $123,288 additional funding creates $14,795 annual incremental interest",
                        "Approximately $205,479 additional funding creates $24,658 annual incremental interest",
                    ],
                    [
                        "Combine two-point carrier shock, one-point losses, and extended DSO",
                        "Approximately negative $4,932 annual owner profit after all three shocks",
                        "Approximately positive $60,205 annual owner profit after all three shocks",
                        "Approximately positive $225,342 annual owner profit after all three shocks",
                    ],
                    [
                        "Replace original financing expense with two-percent gross-invoice fee only",
                        "$16,000 profit equals $30,000 plus $6,000 less $20,000 fees",
                        "$129,000 profit equals $165,000 plus $24,000 less $60,000 fees",
                        "$340,000 profit equals $400,000 plus $40,000 less $100,000 fees",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Freeze and reconcile the delivered-load cohort",
                    "action": "Export the prior week's deliveries, amendments, invoices, credits, and settlements into a versioned reconciliation workbook.",
                    "detail": "Tie shipment counts and gross billings to the TMS and ledger; retain separate identifiers for canceled loads, replacement tenders, and disputed accessorials.",
                },
                {
                    "step": 2,
                    "title": "Rebuild the contribution and reserve waterfall",
                    "action": "Allocate purchased transportation, contractor time, acquisition spending, and expected loss adjustments to the correct shipper cohort.",
                    "detail": "Reconcile reserve opening balance, new provision, utilization, and closing balance; remove duplicate charges between revenue credits, loss expense, and actual write-offs.",
                },
                {
                    "step": 3,
                    "title": "Refresh thirteen-week settlement and collection liquidity",
                    "action": "Update expected receipt dates, carrier due dates, payroll, lender availability, and restricted security balances.",
                    "detail": "Run fifteen-day DSO deterioration and concentrated-customer default cases; exclude ineligible invoices and unavailable collateral from the funding sources column.",
                },
                {
                    "step": 4,
                    "title": "Assign corrective actions before accepting incremental exposure",
                    "action": "Set customer-level prepayment requirements, revised tender limits, repricing actions, and exception-resolution owners.",
                    "detail": "Record dollar exposure, evidence still required, next review date, and settlement responsibility; verify completion against subsequent bank and shipment records.",
                },
            ],
        },
    ],
    "pull_quote": "A freight spread is only spendable after the shipper pays, the carrier clears, and the exceptions stop reversing.",
    "diagram_id": "diag-03",
    "action_checklist": [
        "Reconcile the $1 million, $3 million, and $5 million gross-billing cohorts to exactly $30,000, $165,000, and $400,000 annual owner profit.",
        "Validate employee compensation and fractional contractor hours against actual coverage requirements, including the owner's working role and after-hours exceptions.",
        "Create load-linked reserve categories for credit loss, unsupported billing, and unrecovered settlement exposure without duplicating posted credits or write-offs.",
        "Build a thirteen-week cash forecast using actual delivery-to-cash timing, carrier due dates, lender eligibility, and separately restricted financial security.",
        "Pilot freight_detention_audit_contingency with authorized billing records, collection-based contingency fees, documented reversals, and qualified customs participants where required.",
        "Run the two-point carrier-cost, one-point loss, and fifteen-day DSO stresses before increasing shipper credit limits or accepting materially more volume.",
    ],
    "statutory_citations": [
        {
            "title": "49 U.S.C. 13904 — Registration of brokers",
            "url": "https://www.law.cornell.edu/uscode/text/49/13904",
            "relevance": "Establishes the federal broker-registration framework that must be addressed before operating the property-brokerage business.",
        },
        {
            "title": "49 U.S.C. 13906(b) — Broker financial security",
            "url": "https://www.law.cornell.edu/uscode/text/49/13906",
            "relevance": "Provides the statutory broker financial-security framework, including the $75,000 amount relevant to restricted capital and liquidity planning.",
        },
        {
            "title": "49 CFR 387.307 — Property-broker surety bond or trust fund",
            "url": "https://www.ecfr.gov/current/title-49/section-387.307",
            "relevance": "Governs broker financial responsibility and the BMC-84/BMC-85 framework; verify current security maintenance requirements separately from operating cash availability.",
        },
        {
            "title": "49 CFR 371.3 — Records to be kept by brokers",
            "url": "https://www.ecfr.gov/current/title-49/section-371.3",
            "relevance": "Requires transaction records covering brokerage activity, compensation, and freight-charge information, with retention and transaction-party access provisions.",
        },
        {
            "title": "19 U.S.C. 1313 — Drawback and refunds",
            "url": "https://www.law.cornell.edu/uscode/text/19/1313",
            "relevance": "Defines statutory drawback pathways; an entry summary alone does not establish eligibility for the contingency audit's proposed customs recovery.",
        },
        {
            "title": "19 U.S.C. 1641 — Customs brokers",
            "url": "https://www.law.cornell.edu/uscode/text/19/1641",
            "relevance": "Defines customs business and the licensing framework relevant when audit work moves beyond analytics into regulated customs representation.",
        },
        {
            "title": "19 CFR 111.2 — License and permit requirements",
            "url": "https://www.ecfr.gov/current/title-19/section-111.2",
            "relevance": "Identifies licensing and permit requirements and applicable exceptions for customs business; structure drawback execution around the participant's actual authority.",
        },
    ],
}
