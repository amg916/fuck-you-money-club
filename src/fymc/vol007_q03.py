from __future__ import annotations

CHAPTER_3 = {
    "id": "Q3",
    "chapter_id": "Q3",
    "chapter_number": 3,
    "question_number": 3,
    "slug": "unit-economics-margin-waterfall-working-capital-float",
    "question_prompt": "What are the real unit economics, gross-to-net margin deductions, scrub/reversal reserves, and working-capital float requirements for unclaimed property recovery?",
    "kicker": "Q3 / THE BIG MONEY PLAYBOOKS",
    "title": "Unit Economics, Margin Waterfall & Working-Capital Float",
    "subtitle": "Treasury Finder-Fee Cohorts, Identity Scrubs, Contractor CAC, Settlement Holds, and Cash Conversion Under State Recovery Statutes",
    "layout_template": "financial_breakdown",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #5, Unclaimed Property Recovery, holds Rank #07 with an 85/100 "
        "Money-to-Manpower Score. This chapter translates 12 mapped plays into a "
        "fee-only operating model: client property is never operator revenue. "
        "Conservative, Base, and Scaled cases produce $60,000, $255,000, and "
        "$450,000 recognized annual fees, yielding $15,000, $95,625, and $225,000 "
        "annual owner profit. The waterfall separates identity scrubs, fee reversals, "
        "contractor delivery, acquisition, overhead, and collection expense. Cash "
        "planning then adds treasury processing, payout restrictions, and invoice "
        "DSO rather than treating an accepted claim as spendable cash. Settlement "
        "recovery receives its own eligibility and fee logic; corporate class-action "
        "contingencies cannot be substituted for capped state finder fees."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$60,000",
            "context": "Annual recognized service fees; client property excluded",
            "note": "25% net margin; $15,000 owner profit; 1 FT + 2 C",
        },
        {
            "label": "Base",
            "value": "$255,000",
            "context": "Annual recognized service fees; client property excluded",
            "note": "37.5% net margin; $95,625 owner profit; 1 FT + 2 C",
        },
        {
            "label": "Scaled",
            "value": "$450,000",
            "context": "Annual recognized service fees; client property excluded",
            "note": "50% net margin; $225,000 owner profit; 2 FT + 3 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Define the Fee Unit Before Buying Another Lead",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Start with a claim cohort, not the treasury search result count. "
                    "A cohort contains files admitted during one acquisition period, "
                    "each linked to an owner, property identifier, jurisdiction, "
                    "permitted contract, and documented fee basis. For this illustrative "
                    "bridge, Conservative processes 100 admitted files with $750 average "
                    "potential fees; Base processes 300 at $1,000; Scaled processes "
                    "500 at $1,000. Their initial fee pools are therefore $75,000, "
                    "$300,000, and $500,000. These are prospective contractual economics, "
                    "not booked receivables. If a permitted 10% fee applied throughout, "
                    "the corresponding potential client recoveries would be $750,000, "
                    "$3,000,000, and $5,000,000. Those assets remain client property "
                    "and never enter the operator revenue column. Ten percent is "
                    "a modeling assumption, not a nationwide entitlement. California "
                    "Code of Civil Procedure section 1582 constrains covered recovery "
                    "agreements, while other states impose different conditions. Store "
                    "the applicable rule version alongside each agreement. Exclude "
                    "ineligible contracts before counting a file as monetizable. "
                    "Separate the owner from the payee and the signatory: a corporate "
                    "officer, estate representative, and individual claimant require "
                    "different authority evidence even when names appear similar "
                    "in the public property record."
                ),
                (
                    "Define the economic denominator consistently. The 100, 300, "
                    "and 500 files are admitted files, including files subsequently "
                    "scrubbed or reduced; they are not all successful payouts. "
                    "Conservative loses $10,000 of potential fees to eligibility "
                    "scrubs and $5,000 to fee reductions or reversals, leaving "
                    "$60,000 recognized fees. Base loses $30,000 and $15,000, "
                    "leaving $255,000. Scaled loses $30,000 and $20,000, leaving "
                    "$450,000. Average realized fees per admitted file are consequently "
                    "$600, $850, and $900. Record a reason code for every loss: "
                    "wrong owner, unsupported succession, duplicate filing, contractual "
                    "defect, payout reduction, or uncollectible authorized invoice. "
                    "Do not mechanically label all these events bad debt. A file "
                    "rejected before a fee becomes recognizable is pipeline attrition; "
                    "a later receivable loss has a different accounting treatment. "
                    "QuickBooks or Xero should receive only the amounts supported "
                    "by the recognition policy, with the operational bridge maintained "
                    "in SQLite or a controlled spreadsheet. A weekly reconciliation "
                    "must connect property records, executed agreements, administrator "
                    "notices, invoices, and cash receipts without converting optimistic "
                    "search values into sales. Count reopened files separately so "
                    "a resubmission cannot manufacture apparent acquisition productivity."
                ),
                (
                    "The twelve mapped plays below are chapter-level operating "
                    "buckets, not twelve independently additive revenue forecasts. "
                    "The supplied TRACK_1 play, "
                    "b2b_class_action_contingency_recovery, is economically distinct "
                    "from treasury finder work. Monitor court-approved administrator "
                    "notices for payment-card interchange, freight, auto parts, "
                    "commercial insurance, and SaaS settlements, including large "
                    "corporate antitrust funds. Treat the proposed 85–90% small-business "
                    "nonfiling rate as a sourcing hypothesis until the specific "
                    "administrator supplies defensible participation data. A settlement "
                    "fund's headline size does not establish an individual business's "
                    "allocation. For an illustrative $20,000 verified payout, a "
                    "permitted 30% contingency generates $6,000 potential fees; "
                    "a $600 reduction allowance leaves $5,400. Delivery of $2,400, "
                    "acquisition of $900, systems allocation of $300, and collection "
                    "support of $600 leave $1,200 contribution before shared overhead. "
                    "The proposed 25–33% range is usable only where the contract, "
                    "applicable law, and settlement procedures permit it. Fall back "
                    "to verified operating businesses with primary processor or "
                    "vendor statements and court-approved third-party claim-filing "
                    "riders where required. Never invent transactions, beneficial "
                    "ownership, or purchase history to improve the payout formula. "
                    "Keep this example outside the canonical annual totals unless "
                    "it replaces an explicitly budgeted cohort."
                ),
            ],
            "table": {
                "caption": "Twelve Mapped Recovery Plays: Fee Units, Delivery Budgets, and Failure Fallbacks",
                "headers": [
                    "Mapped play and specific operating scope",
                    "Illustrative permitted fee unit and calculation",
                    "Direct delivery budget and contribution screen",
                    "Failure trigger and concrete operating fallback",
                ],
                "rows": [
                    [
                        "Individual treasury cash claims with verified owner identity",
                        "$5,000 recovered times permitted 10% produces $500 fees",
                        "$150 delivery leaves $350 before acquisition and overhead",
                        "Reject ambiguous identities until address history independently matches",
                    ],
                    [
                        "Corporate uncashed warrants matched to active operating entities",
                        "$12,000 recovered times permitted 10% produces $1,200 fees",
                        "$300 delivery leaves $900 before acquisition and overhead",
                        "Obtain issuer records when warrant payee abbreviations conflict",
                    ],
                    [
                        "Multi-state corporate portfolios consolidated under verified signing authority",
                        "$40,000 recovered times permitted 10% produces $4,000 fees",
                        "$1,200 delivery leaves $2,800 before acquisition and overhead",
                        "Split contracts where state-specific restrictions defeat uniform terms",
                    ],
                    [
                        "Dormant vendor refund checks linked to original invoices",
                        "$8,000 recovered times permitted 10% produces $800 fees",
                        "$200 delivery leaves $600 before acquisition and overhead",
                        "Request original remittance evidence before asserting successor ownership",
                    ],
                    [
                        "Insurance proceeds supported by policy and ownership records",
                        "$15,000 recovered times permitted 10% produces $1,500 fees",
                        "$450 delivery leaves $1,050 before acquisition and overhead",
                        "Pause disputed beneficiary files until claimant authority resolves",
                    ],
                    [
                        "Utility deposit recoveries tied to historical service addresses",
                        "$3,000 recovered times permitted 10% produces $300 fees",
                        "$120 delivery leaves $180 before acquisition and overhead",
                        "Use owner self-service when document costs consume contribution",
                    ],
                    [
                        "Payroll check recoveries supported by employment identity evidence",
                        "$2,000 recovered times permitted 10% produces $200 fees",
                        "$90 delivery leaves $110 before acquisition and overhead",
                        "Avoid paid acquisition where reachable fees cannot cover handling",
                    ],
                    [
                        "Estate property files handled through verified personal representatives",
                        "$25,000 recovered times permitted 10% produces $2,500 fees",
                        "$1,000 delivery leaves $1,500 before acquisition and overhead",
                        "Refer contested succession issues instead of funding litigation",
                    ],
                    [
                        "Merger successor claims supported by transaction document chains",
                        "$60,000 recovered times permitted 10% produces $6,000 fees",
                        "$2,000 delivery leaves $4,000 before acquisition and overhead",
                        "Require assignment schedules when purchase documents exclude assets",
                    ],
                    [
                        "Dissolved corporation recoveries with established surviving claimant rights",
                        "$20,000 recovered times permitted 10% produces $2,000 fees",
                        "$800 delivery leaves $1,200 before acquisition and overhead",
                        "Stop when dissolution prevents a documented authorized claimant",
                    ],
                    [
                        "Repeat corporate property sweeps following previously verified recoveries",
                        "$10,000 recovered times permitted 10% produces $1,000 fees",
                        "$150 delivery leaves $850 before acquisition and overhead",
                        "Refresh authority and search duplicates before reusing historical packets",
                    ],
                    [
                        "b2b_class_action_contingency_recovery: verified corporate settlement claims under TRACK_1",
                        "$20,000 payout times permitted 30% produces $6,000 fees",
                        "$600 reduction and $4,200 costs leave $1,200 contribution",
                        "Use primary statements and court-approved filing riders where required",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Protect the Denominator Before Optimizing the Funnel",
                "body": "Recovery businesses lose margin when search matches masquerade as qualified, collectible files.",
                "items": [
                    "Quote against the documented recoverable amount, not an aggregated search result containing duplicate properties or similarly named owners.",
                    "Ask corporate prospects for one primary processor, vendor, or treasury record before commissioning an expensive historical document search.",
                    "Track client-receipt-to-fee-payment time separately from treasury processing time; faster document work cannot cure an owner's unpaid invoice.",
                    "Reuse a verified corporate authority packet only after checking current officers, successor rights, property identifiers, and jurisdiction-specific requirements.",
                ],
            },
        },
        {
            "heading": "2. Reconcile Every Deduction to the Canonical Owner Profit",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "The annual waterfall below reconciles exactly to the scorecard, "
                    "but its intermediate cost allocations are explicit planning "
                    "assumptions rather than reported operating history. Begin with "
                    "the prospective fee pool, subtract eligibility scrubs, subtract "
                    "fee reductions and reversals, and arrive at recognized service "
                    "revenue. Then deduct delivery labor, acquisition, systems, "
                    "administration, and financing plus collection expense. Conservative "
                    "costs total $45,000, Base $159,375, and Scaled $225,000. "
                    "Subtracting those amounts from $60,000, $255,000, and "
                    "$450,000 yields owner profit of $15,000, $95,625, and "
                    "$225,000, respectively. Dividing profit by recognized revenue "
                    "produces exactly 25%, 37.5%, and 50%. Do not divide profit "
                    "by underlying property recovered or by the unreduced prospective "
                    "fee pool. Likewise, do not deduct the same reversal twice "
                    "through both the fee bridge and an operating expense account. "
                    "Maintain an accounting-policy crosswalk for presentation differences "
                    "without changing the economic total. The scorecard's owner "
                    "profit is treated here as the owner's operating residual "
                    "before personal income taxes; an additional hypothetical owner "
                    "salary has not been silently deducted. Entity-level tax treatment "
                    "and compensation structure require separate budget decisions."
                ),
                (
                    "Delivery labor must purchase completed, auditable work rather "
                    "than contractor availability. Conservative allocates $18,000 "
                    "across 100 admitted files, or $180 each; Base allocates "
                    "$65,000 across 300, or $216.67; Scaled allocates $100,000 "
                    "across 500, or $200. Base's higher unit delivery cost "
                    "represents a harder document mix, not a calculation error. "
                    "Use fixed work packages for identity verification, corporate "
                    "authority assembly, claim preparation, and exception handling, "
                    "with rework ownership written into the engagement. Contractor "
                    "classification follows the actual relationship, not the spreadsheet "
                    "label. The 1 FT + 2 C Conservative and Base structures "
                    "assume the owner is the full-time operator and contractors "
                    "supply variable delivery capacity. Scaled's 2 FT + 3 C "
                    "includes an additional employee whose loaded cost must fit "
                    "inside the delivery and administration allocations. Two contractors "
                    "do not imply two full-time salaries. Model hours and accepted "
                    "deliverables explicitly. At an illustrative $40 blended delivery "
                    "hour, $18,000 buys 450 hours, $65,000 buys 1,625, and "
                    "$100,000 buys 2,500. Any employee benefits, payroll taxes, "
                    "or contractor rework consuming that budget reduce the remaining "
                    "production hours and must appear in capacity planning."
                ),
                (
                    "Acquisition budgets are $6,000, $40,000, and $55,000, "
                    "equivalent to $60, $133.33, and $110 per admitted file. "
                    "These denominators include later scrubs, preventing the marketing "
                    "report from hiding failed files. Count purchased data, mail, "
                    "calling labor, referral payments where permitted, and campaign "
                    "software once, assigning shared subscriptions consistently between "
                    "acquisition and systems. Systems plus administration equal "
                    "$18,000, $38,000, and $50,000 annually, or $1,500, "
                    "$3,166.67, and $4,166.67 monthly. Those fixed-overhead "
                    "assumptions fit the supplied $1,500–$8,000 monthly opex "
                    "planning range; all-in monthly expense is higher once variable "
                    "delivery, acquisition, and collection costs are included. Financing "
                    "and collection budgets of $3,000, $16,375, and $20,000 "
                    "include expected interest, payment charges, and external collection "
                    "support, not an unexplained balancing reserve. Replace each "
                    "component with actual vendor quotes before spending. A prudent "
                    "cash reserve is retained liquidity, not automatically an expense. "
                    "Client distrust increases both CAC and invoice delays, so "
                    "state plainly that owners can claim directly without hiring "
                    "the service. Test plain-language letters against aggressive "
                    "recovery language using admitted-file economics, not response "
                    "rates alone, and retain dated campaign evidence."
                ),
            ],
            "table": {
                "caption": "Annual Fee-Only Waterfall: Exact Conservative, Base, and Scaled Reconciliation",
                "headers": [
                    "Economic line and measurement treatment",
                    "Conservative annual amount and operating interpretation",
                    "Base annual amount and operating interpretation",
                    "Scaled annual amount and operating interpretation",
                ],
                "rows": [
                    [
                        "Prospective fee pool before eligibility and collection adjustments",
                        "$75,000 from 100 admitted files averaging $750 potential fees",
                        "$300,000 from 300 admitted files averaging $1,000 potential fees",
                        "$500,000 from 500 admitted files averaging $1,000 potential fees",
                    ],
                    [
                        "Subtract eligibility scrubs before recognizing any associated revenue",
                        "$10,000 removed for ownership, authority, and eligibility failures",
                        "$30,000 removed for ownership, authority, and eligibility failures",
                        "$30,000 removed for ownership, authority, and eligibility failures",
                    ],
                    [
                        "Subtract fee reductions and reversals without duplicating expenses",
                        "$5,000 removed for reduced payouts and contractual fee losses",
                        "$15,000 removed for reduced payouts and contractual fee losses",
                        "$20,000 removed for reduced payouts and contractual fee losses",
                    ],
                    [
                        "Recognized service revenue excludes all underlying client property",
                        "$60,000 recognized fees equal $600 per admitted file",
                        "$255,000 recognized fees equal $850 per admitted file",
                        "$450,000 recognized fees equal $900 per admitted file",
                    ],
                    [
                        "Deduct delivery labor including contractor work and allocated payroll",
                        "$18,000 delivery spending equals $180 per admitted file",
                        "$65,000 delivery spending equals approximately $216.67 per admitted file",
                        "$100,000 delivery spending equals $200 per admitted file",
                    ],
                    [
                        "Deduct acquisition spending across all admitted cohort files",
                        "$6,000 acquisition spending equals $60 per admitted file",
                        "$40,000 acquisition spending equals approximately $133.33 per admitted file",
                        "$55,000 acquisition spending equals $110 per admitted file",
                    ],
                    [
                        "Deduct systems covering matching, tracking, storage, and accounting",
                        "$6,000 annual systems budget supports controlled small-cohort processing",
                        "$18,000 annual systems budget supports growing multi-jurisdiction processing",
                        "$24,000 annual systems budget supports higher-volume exception tracking",
                    ],
                    [
                        "Deduct administration including insurance and non-delivery support costs",
                        "$12,000 annual administration budget supports owner-led operating infrastructure",
                        "$20,000 annual administration budget supports expanded operating infrastructure",
                        "$26,000 annual administration budget supports five-person operating infrastructure",
                    ],
                    [
                        "Deduct financing, payment charges, and external collection support",
                        "$3,000 expected annual expense requires quoted funding and services",
                        "$16,375 expected annual expense requires quoted funding and services",
                        "$20,000 expected annual expense requires quoted funding and services",
                    ],
                    [
                        "Residual owner profit divided by recognized service revenue",
                        "$15,000 annual owner profit equals exactly 25% net margin",
                        "$95,625 annual owner profit equals exactly 37.5% net margin",
                        "$225,000 annual owner profit equals exactly 50% net margin",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Freeze the cohort register",
                    "action": "Assign immutable file identifiers and acquisition-period tags before calculating economics.",
                    "detail": "Record owner, property, jurisdiction, expected recovery, permitted fee, authority evidence, admission date, and expected payout sequence.",
                },
                {
                    "step": 2,
                    "title": "Resolve every gross-to-net adjustment",
                    "action": "Link each scrub or fee reduction to a reason code and supporting document.",
                    "detail": "Separate pre-recognition pipeline losses from recognized-revenue adjustments and receivable credit losses; prevent duplicate deductions.",
                },
                {
                    "step": 3,
                    "title": "Allocate actual delivery and acquisition costs",
                    "action": "Match contractor invoices, employee allocations, and campaign spending to the cohort.",
                    "detail": "Use admitted files as the common unit denominator and reconcile shared-cost allocations to the general ledger.",
                },
                {
                    "step": 4,
                    "title": "Close profit and cash independently",
                    "action": "Reconcile recognized fees to owner profit, then reconcile receivables to bank receipts.",
                    "detail": "Publish margin, outstanding fee receivables, locked payouts, forecast cash trough, and dated variance explanations each month.",
                },
            ],
        },
        {
            "heading": "3. Fund the Claim Clock and the Invoice Clock Separately",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Cash conversion starts when the operator funds acquisition "
                    "or document work, not when the treasury acknowledges a claim. "
                    "Track four dates: initial cash outlay, complete submission, "
                    "owner receipt of property, and operator receipt of fees. "
                    "Treasury review and settlement distribution delays occur before "
                    "the owner has cash; invoice DSO measures the subsequent "
                    "receivable interval under the contract. A court distribution "
                    "hold, missing indemnity, or returned treasury check can extend "
                    "the first interval without changing DSO at all. For planning, "
                    "Conservative assumes 150 days before owner receipt plus "
                    "30 days to collect fees, Base 120 plus 30, and Scaled "
                    "90 plus 30. These 180-, 150-, and 120-day cash-outlay-to-fee "
                    "intervals are assumptions, not published treasury service commitments. "
                    "An accepted submission is neither a payable invoice nor "
                    "a bankable receivable unless the agreement and applicable "
                    "accounting policy support that conclusion. Record each jurisdiction's "
                    "observed median and slow-tail duration separately. Do not "
                    "finance a slow estate file with the average timing of "
                    "simple corporate cash claims. Review status through official "
                    "portals and administrator correspondence; automation should surface "
                    "exceptions, not repeatedly submit duplicate claims that restart "
                    "manual review or confuse ownership evidence."
                ),
                (
                    "A first-pass float budget multiplies monthly cash operating "
                    "expense by the modeled funding interval. Using annual costs "
                    "divided by twelve gives $3,750 for Conservative, $13,281.25 "
                    "for Base, and $18,750 for Scaled. Six, five, and four "
                    "months of those costs require $22,500, $66,406.25, and "
                    "$75,000 respectively before a contingency cushion. Adding "
                    "15% produces $25,875, $76,367.19, and $86,250. This "
                    "is a conservative steady-spending approximation, not an exact "
                    "receivables formula: some costs occur late, some contractor "
                    "payments can be milestone-based, and mature cohorts generate "
                    "overlapping receipts. Build a weekly cash schedule to locate "
                    "the actual trough before committing funding. The supplied "
                    "$5,000–$35,000 startup capital range can support the illustrated "
                    "Conservative float only toward its upper end and before "
                    "additional launch costs. It does not independently fund the "
                    "illustrated Base or Scaled pipeline. Those cases require "
                    "retained cash, staged starts, or committed external capital. "
                    "Time to first deal of 3–12 months must also be distinguished "
                    "from time to first collected fee. A twelve-month zero-receipt "
                    "ramp at Conservative spending consumes $45,000 before launch "
                    "costs, exceeding the stated startup range."
                ),
                (
                    "Treat client assets as unavailable working capital even when "
                    "a payment arrangement permits some administrative involvement. "
                    "Prefer treasury or administrator payment directly to the "
                    "verified owner, followed by a clearly authorized service "
                    "invoice. Never divert property to cover unrelated payroll. "
                    "For the settlement example, $4,200 of delivery, acquisition, "
                    "systems, and collection spending could precede fee receipt; "
                    "a 270-day distribution interval plus 30-day collection interval "
                    "requires carrying that exposure for roughly ten months. "
                    "Collection support may actually be paid later, so the "
                    "weekly schedule should replace this deliberately conservative "
                    "upper-bound treatment. At an illustrative 12% simple annual "
                    "borrowing rate, carrying $4,200 for ten months costs $420 "
                    "before lender fees, reducing the example's $1,200 contribution "
                    "to $780 if financing was not already allocated. Avoid "
                    "double counting when borrowing costs are inside the annual "
                    "financing line. A lender's advance against a disputed or "
                    "nonassignable claim may be unavailable regardless of expected "
                    "payout. Negotiate contractor milestones around accepted evidence "
                    "packages rather than making payment depend entirely on "
                    "uncontrollable treasury decisions. Release cash cushions only "
                    "after cohort loss experience, aging, and actual receipts "
                    "support the release, not because the profit statement looks strong."
                ),
            ],
            "table": {
                "caption": "Float and Timing Matrix: Cash Requirements Are Separate from Annual Profit",
                "headers": [
                    "Cash planning measurement and explicit modeling convention",
                    "Conservative funding amount and timing implication",
                    "Base funding amount and timing implication",
                    "Scaled funding amount and timing implication",
                ],
                "rows": [
                    [
                        "Monthly all-in cash expense assumes evenly distributed annual spending",
                        "$3,750 monthly spending includes delivery, acquisition, and overhead",
                        "$13,281.25 monthly spending includes delivery, acquisition, and overhead",
                        "$18,750 monthly spending includes delivery, acquisition, and overhead",
                    ],
                    [
                        "Pre-receipt interval includes document work and payout restrictions",
                        "150 modeled days elapse before the owner receives property",
                        "120 modeled days elapse before the owner receives property",
                        "90 modeled days elapse before the owner receives property",
                    ],
                    [
                        "Invoice collection interval begins separately from treasury processing",
                        "30 additional modeled days pass before operator fee collection",
                        "30 additional modeled days pass before operator fee collection",
                        "30 additional modeled days pass before operator fee collection",
                    ],
                    [
                        "Unbuffered float uses thirty-day months for consistent planning",
                        "$22,500 funds six months of modeled cash operating expense",
                        "$66,406.25 funds five months of modeled cash operating expense",
                        "$75,000 funds four months of modeled cash operating expense",
                    ],
                    [
                        "Buffered float adds fifteen percent without booking another expense",
                        "$25,875 total liquidity includes a $3,375 contingency cushion",
                        "$76,367.19 total liquidity includes a $9,960.94 contingency cushion",
                        "$86,250 total liquidity includes an $11,250 contingency cushion",
                    ],
                    [
                        "Additional ninety-day payout delay adds three months of spending",
                        "$11,250 additional liquidity is needed before incremental borrowing costs",
                        "$39,843.75 additional liquidity is needed before incremental borrowing costs",
                        "$56,250 additional liquidity is needed before incremental borrowing costs",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Verify Four Conditions Before Funding the Next Cohort",
                "body": "A profitable forecast cannot authorize an invalid contract or pay contractors during a distribution hold.",
                "items": [
                    "Verify finder registration, contracting restrictions, fee limits, required disclosures, and claimant authority for every jurisdiction represented in the cohort.",
                    "Verify that all modeled recoveries belong to the identified owner and that every settlement claim is supported by primary transaction records.",
                    "Verify committed unrestricted cash covers the weekly projected trough, a ninety-day delay scenario, and separately budgeted launch costs.",
                    "Verify invoice triggers, payment destinations, fee-recognition treatment, reversal handling, and the owner's direct-claim option before outreach or signing.",
                ],
            },
        },
        {
            "heading": "4. Stress the Cohort Before Scaling Matching and Status Automation",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Stress the fee pool, not just the margin percentage. "
                    "A five-percentage-point increase in combined scrub and reversal "
                    "losses removes $3,750 from Conservative revenue, $15,000 "
                    "from Base, and $25,000 from Scaled because the underlying "
                    "prospective pools are $75,000, $300,000, and $500,000. "
                    "Holding costs fixed, owner profits fall to $11,250, "
                    "$80,625, and $200,000. A separate 25% CAC increase "
                    "adds $1,500, $10,000, and $13,750 of cost, leaving "
                    "$13,500, $85,625, and $211,250. A separate 20% delivery "
                    "increase adds $3,600, $13,000, and $20,000, leaving "
                    "$11,400, $82,625, and $205,000. Combined, all three "
                    "shocks leave $6,150, $57,625, and $166,250. These "
                    "are sensitivities around the canonical cases, not replacements "
                    "for their published profits. They deliberately hold throughput "
                    "and other costs constant to expose first-order vulnerability. "
                    "A real downturn can also lower close rates, delay "
                    "collections, and increase borrowing expense simultaneously. Run "
                    "that correlated downside in the weekly cash model rather "
                    "than pretending independent stress columns describe the worst "
                    "possible outcome. Preserve a dated assumption register so "
                    "later performance comparisons cannot rewrite the original "
                    "investment decision or hide deteriorating cohort quality."
                ),
                (
                    "Set acquisition ceilings from contribution after expected "
                    "losses, not from the face value of found property. "
                    "Conservative's $600 realized fee minus $180 delivery leaves "
                    "$420 before CAC, systems, administration, and collection costs. "
                    "Base leaves approximately $633.33 after its $216.67 delivery "
                    "cost; Scaled leaves $700 after $200 delivery. Under the "
                    "allocated annual model, the remaining non-acquisition costs "
                    "per admitted file are $210, $181.25, and $140. Therefore "
                    "the zero-profit acquisition ceilings are $210, approximately "
                    "$452.08, and $560 per admitted file. Those are break-even "
                    "limits, not recommended bids. Current acquisition spending "
                    "leaves the canonical per-file profits of $150, $318.75, "
                    "and $450. If one admitted file requires ten qualified "
                    "responses, Conservative's $60 admitted-file CAC permits only "
                    "$6 per qualified response before additional intake costs. "
                    "Record matching should improve verified admission efficiency, "
                    "while claim-status tracking should reduce manual touches "
                    "and prevent stale packets. Neither automation lever increases "
                    "the lawful fee cap or creates entitlement to property. "
                    "Measure duplicate rate, false-owner matches, contractor minutes, "
                    "missing-document loops, and cash realization by acquisition "
                    "vintage before increasing campaign volume. Stop paid intake "
                    "when incremental files consume contribution or exceed verified "
                    "document-handling capacity."
                ),
                (
                    "Operational controls must preserve both economic evidence "
                    "and claimant trust. California Code of Civil Procedure "
                    "section 1582 addresses covered finder agreements and their "
                    "fee ceiling; New York Abandoned Property Law section 1416 "
                    "addresses recovery agreements, including its 15% compensation "
                    "limit. Florida Statutes section 717.135 specifies requirements "
                    "for covered recovery or purchase agreements, including "
                    "disclosures and compensation provisions. Apply the current "
                    "text to the actual transaction rather than copying a "
                    "national contract template. Federal Rule of Civil Procedure "
                    "23(e) governs settlement approval in covered class actions, "
                    "but the settlement agreement, court orders, and administrator "
                    "instructions determine the operational filing requirements. "
                    "Maintain a restricted evidence repository for identity "
                    "documents and bank information, with role-based access, "
                    "encrypted storage, and documented retention periods. California "
                    "Civil Code section 1798.81.5 supplies a concrete reasonable-security "
                    "requirement for covered personal information. Keep raw identity "
                    "documents out of broad-access Airtable views and campaign "
                    "exports. Publish a monthly operating pack with cohort "
                    "revenue, losses by cause, admitted-file CAC, delivery hours, "
                    "aging, and unrestricted cash. The scaling decision should "
                    "follow collected-fee quality and staffing capacity, not "
                    "the number of attractive treasury records harvested by "
                    "an automated matcher or the headline size of settlement funds."
                ),
            ],
            "table": {
                "caption": "Sensitivity and Break-Even Matrix: Preserve the Published Cases While Testing Their Weak Points",
                "headers": [
                    "Stress test and explicit unchanged assumptions",
                    "Conservative result and specific operating consequence",
                    "Base result and specific operating consequence",
                    "Scaled result and specific operating consequence",
                ],
                "rows": [
                    [
                        "Five percentage points more fee-pool attrition with costs fixed",
                        "$11,250 owner profit remains after $3,750 additional fee losses",
                        "$80,625 owner profit remains after $15,000 additional fee losses",
                        "$200,000 owner profit remains after $25,000 additional fee losses",
                    ],
                    [
                        "Acquisition spending rises twenty-five percent with admitted volume unchanged",
                        "$13,500 owner profit remains after $1,500 additional acquisition expense",
                        "$85,625 owner profit remains after $10,000 additional acquisition expense",
                        "$211,250 owner profit remains after $13,750 additional acquisition expense",
                    ],
                    [
                        "Delivery labor rises twenty percent without improving fee realization",
                        "$11,400 owner profit remains after $3,600 additional delivery expense",
                        "$82,625 owner profit remains after $13,000 additional delivery expense",
                        "$205,000 owner profit remains after $20,000 additional delivery expense",
                    ],
                    [
                        "All three operating shocks occur together before extra financing",
                        "$6,150 owner profit remains after $8,850 combined economic deterioration",
                        "$57,625 owner profit remains after $38,000 combined economic deterioration",
                        "$166,250 owner profit remains after $58,750 combined economic deterioration",
                    ],
                    [
                        "Ninety-day timing shock adds funding needs without immediate fee loss",
                        "$11,250 additional float is required; borrowing expense reduces profit",
                        "$39,843.75 additional float is required; borrowing expense reduces profit",
                        "$56,250 additional float is required; borrowing expense reduces profit",
                    ],
                    [
                        "Zero-profit admitted-file CAC ceiling holds other allocated costs constant",
                        "$210 acquisition ceiling exceeds current $60 CAC by $150",
                        "Approximately $452.08 acquisition ceiling exceeds current CAC by $318.75",
                        "$560 acquisition ceiling exceeds current $110 CAC by $450",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "Found property is a lead, an approved claim is a milestone, and only a collected lawful fee can fund the next cohort.",
    "diagram_id": "diag-03",
    "action_checklist": [
        "Build a fee-only cohort ledger linking every admitted file to owner authority, property identifiers, applicable contract rules, and expected fee timing.",
        "Reconcile prospective fees through scrubs and reversals to exactly $60,000, $255,000, and $450,000 of canonical recognized annual revenue.",
        "Allocate delivery, acquisition, systems, administration, and collection costs to reproduce $15,000, $95,625, and $225,000 annual owner profit.",
        "Construct a weekly cash schedule separating treasury processing, payout restrictions, invoice DSO, launch costs, and unrestricted funding commitments.",
        "Test five-point attrition, twenty-five-percent CAC, twenty-percent labor, and ninety-day payout-delay shocks before expanding paid acquisition.",
        "Verify state finder requirements and settlement-specific filing authority, disclose direct claiming, and protect identity evidence before admitting new files.",
    ],
    "statutory_citations": [
        {
            "title": "California Code of Civil Procedure section 1582 — Recovery agreements",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CCP&sectionNum=1582.",
            "relevance": "Apply the statutory restrictions on covered recovery agreements, including compensation limits and restricted contracting periods, before modeling collectible finder fees.",
        },
        {
            "title": "New York Abandoned Property Law section 1416 — Agreements to locate property",
            "url": "https://www.nysenate.gov/legislation/laws/ABP/1416",
            "relevance": "Check agreement validity, required execution terms, and the 15% compensation limit when projecting New York recovery-service revenue.",
        },
        {
            "title": "Florida Statutes section 717.135 — Recovery or purchase agreements",
            "url": "https://www.flsenate.gov/Laws/Statutes/2025/717.135",
            "relevance": "Review the cited statutory version and subsequent amendments for required disclosures, agreement provisions, and applicable compensation treatment before accepting Florida files.",
        },
        {
            "title": "Federal Rule of Civil Procedure 23(e) — Settlement, voluntary dismissal, or compromise",
            "url": "https://www.law.cornell.edu/rules/frcp/rule_23",
            "relevance": "Distinguish court settlement approval from the claim eligibility, evidence, third-party filing, and distribution requirements established by the settlement documents and court orders.",
        },
        {
            "title": "California Civil Code section 1798.81.5 — Reasonable security for personal information",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1798.81.5",
            "relevance": "Design reasonable security procedures for covered claimant information and address applicable contractual security requirements when sharing evidence with service providers.",
        },
    ],
}
