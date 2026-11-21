from __future__ import annotations

VOLUME_014_SUBTITLE = (
    "The Complete Playbook for $120,000–$1,000,000 USD in Annual Retained "
    "Brokerage Fees: Build a 2 FT + 2 C Pod, Scale to Six People"
)

VOLUME_014_POSITIONING_ALTERNATIVES = [
    {
        "title": "The Equipment and Receivables Placement Desk",
        "subtitle": (
            "Build a four-person commercial finance brokerage around collateral "
            "evidence, lender-fit rules, and retained placement fees."
        ),
        "audience": (
            "Commercial lending operators and equipment-industry specialists "
            "serving established businesses with documented assets or receivables."
        ),
        "research_basis": (
            "UCC Article 9 supplies the framework for security interests and "
            "perfection. A brokerage can organize collateral schedules, lien-search "
            "requests, and lender submissions without treating financed principal "
            "as its revenue. State licensing analysis remains transaction-specific."
        ),
        "sources": [
            "https://www.law.cornell.edu/ucc/9/9-203",
            "https://www.law.cornell.edu/ucc/9/9-310",
            "https://www.law.cornell.edu/ucc/9/9-315",
            (
                "https://leginfo.legislature.ca.gov/faces/"
                "codes_displaySection.xhtml?lawCode=FIN&sectionNum=22100."
            ),
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The SBA Application-to-Closing Desk",
        "subtitle": (
            "Turn complete borrower files, documented agent compensation, "
            "and disciplined lender coordination into a repeatable placement service."
        ),
        "audience": (
            "Experienced commercial credit operators coordinating SBA applications "
            "with participating lenders and borrowers who can document repayment capacity."
        ),
        "research_basis": (
            "13 CFR 103.5 governs agent compensation and required disclosure "
            "for covered SBA assistance. SBA Form 159 operationalizes fee "
            "disclosure where required. The lender, rather than the brokerage, "
            "makes credit decisions and determines program eligibility."
        ),
        "sources": [
            "https://www.ecfr.gov/current/title-13/chapter-I/part-103/section-103.5",
            (
                "https://www.sba.gov/document/"
                "sba-form-159-fee-disclosure-compensation-agreement"
            ),
            "https://www.ecfr.gov/current/title-13/chapter-I/part-120",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Lender-Matrix Specialty Debt Desk",
        "subtitle": (
            "Place equipment, receivables, and bridge debt through an evidence-led "
            "lender matrix while controlling concentration and commission reversals."
        ),
        "audience": (
            "Commercial finance relationship managers building a small brokerage "
            "with multiple lender relationships and strong credit-file discipline."
        ),
        "research_basis": (
            "ECOA and Regulation B shape covered credit practices; the FTC "
            "Safeguards Rule imposes security duties on covered financial "
            "institutions. Securities-based fundraising requires a separate "
            "registration analysis under Exchange Act Section 15(a), rather "
            "than automatic treatment as ordinary loan brokerage."
        ),
        "sources": [
            "https://www.law.cornell.edu/uscode/text/15/1691",
            "https://www.ecfr.gov/current/title-12/chapter-X/part-1002",
            "https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-314",
            "https://www.law.cornell.edu/uscode/text/15/78o",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
]


def build_volume_014_diagrams_data() -> list[dict]:
    specs = [
        (
            "diag-01-placement-workflow",
            "process_flow",
            "From Borrower File to Retained Brokerage Fee",
            "Five operating stages; loan principal never enters brokerage revenue.",
            1,
            "operating_framework",
            (
                "The brokerage arranges commercial financing rather than funding "
                "loans. Revenue consists only of retained origination or referral "
                "fees earned under the applicable agreement. First-deal planning "
                "remains 3–9 months; stage numbers indicate sequence, not duration."
            ),
            (
                "A signed term sheet is neither a closing nor earned cash. "
                "Track failed closings and commission-reversal exposure separately."
            ),
            [
                (
                    "Qualify the mandate",
                    "1 | Scope and eligibility",
                    1.0,
                    (
                        "Record borrower jurisdiction, business purpose, financing "
                        "amount, collateral, and requested timing in HubSpot. "
                        "Confirm the brokerage can perform the proposed activity "
                        "before accepting a fee-bearing engagement."
                    ),
                ),
                (
                    "Assemble the credit file",
                    "2 | Evidence and permissions",
                    2.0,
                    (
                        "Collect financial statements, bank records, debt schedules, "
                        "equipment invoices or receivables aging, and authorized "
                        "contact details. Use a restricted document portal rather "
                        "than forwarding borrower files through shared inboxes."
                    ),
                ),
                (
                    "Match the lender matrix",
                    "3 | Credit fit before submission",
                    3.0,
                    (
                        "Filter Airtable lender records by geography, ticket size, "
                        "industry, collateral, leverage, and lender-defined coverage "
                        "requirements. Record each decline reason and permission "
                        "to share the file with each selected lender."
                    ),
                ),
                (
                    "Coordinate credit and closing",
                    "4 | Conditions and fee evidence",
                    4.0,
                    (
                        "Maintain a closing-condition checklist and reconcile "
                        "borrower-facing fees with lender agreements. The lender "
                        "owns underwriting and funding; the broker verifies "
                        "compensation terms, payor identity, and reversal triggers."
                    ),
                ),
                (
                    "Reconcile and service",
                    "5 | Retained fees and renewals",
                    5.0,
                    (
                        "Match the earned-fee record to the lender settlement "
                        "statement and bank receipt. Separate contingent amounts, "
                        "track clawback windows, and schedule renewal outreach "
                        "without representing loan principal as operator sales."
                    ),
                ),
            ],
        ),
        (
            "diag-02-annual-placement-funnel",
            "funnel",
            "Forty Funded Placements Support the Base Case",
            "One annual borrower cohort; every downstream count is a subset.",
            6,
            "illustrative_model",
            (
                "Illustrative steady-state annual cohort, not a first-month "
                "forecast. Count each financing opportunity once and exclude "
                "duplicate lender submissions. Forty funded, fee-retaining "
                "placements at $14,000 average retained compensation produce "
                "$560,000 operator gross revenue."
            ),
            (
                "Stage conversion rates are 60.0%, 50.0%, 53.3%, and 62.5%; "
                "overall conversion is 10.0%. The $14,000 fee is a modeled "
                "average, not a market quotation."
            ),
            [
                (
                    "Permissioned opportunities",
                    "400 annual opportunities",
                    400.0,
                    (
                        "Source documented borrower introductions through "
                        "accountants, equipment dealers, and existing relationships. "
                        "Deduplicate financing requests before measuring acquisition "
                        "cost or assigning the relationship manager."
                    ),
                ),
                (
                    "Qualified financing requests",
                    "240 | 60.0% of prior stage",
                    240.0,
                    (
                        "Retain borrowers whose business purpose, geography, "
                        "financing size, and timing fit the desk's permitted scope "
                        "and at least one current lender appetite."
                    ),
                ),
                (
                    "Complete lender-ready files",
                    "120 | 50.0% of prior stage",
                    120.0,
                    (
                        "Require current financial evidence, a reconciled debt "
                        "schedule, appropriate collateral documentation, and "
                        "authorized distribution before counting a file as complete."
                    ),
                ),
                (
                    "Accepted conditional terms",
                    "64 | 53.3% of prior stage",
                    64.0,
                    (
                        "Count borrower-accepted lender terms with remaining "
                        "closing conditions logged. Do not recognize brokerage "
                        "fees merely because an indicative offer was issued."
                    ),
                ),
                (
                    "Funded and fee-retaining placements",
                    "40 | 62.5% of prior stage",
                    40.0,
                    (
                        "Reconcile 40 placements times $14,000 to $560,000 "
                        "retained annual fee revenue. Exclude failed closings "
                        "and amounts reversed or unearned; maintain a separate "
                        "contingent-compensation exposure register."
                    ),
                ),
            ],
        ),
        (
            "diag-03-base-case-profit-waterfall",
            "waterfall",
            "$560,000 Retained Fees to $196,000 Owner Net",
            "Four expense deductions reconcile exactly to a 35.0% net margin.",
            3,
            "illustrative_model",
            (
                "All values are annual USD. First and last bars are totals; "
                "the four intervening bars are negative expense movements. "
                "Cost allocations are illustrative, while revenue, profit, "
                "and margin match the canonical Base Case. The published "
                "$4,000–$18,000 monthly operating range is not an all-in "
                "annual expense ceiling: this model requires $364,000 total "
                "annual expenses, averaging $30,333.33 monthly. Do not infer "
                "that the published range funds every modeled expense."
            ),
            (
                "$560,000 − $156,000 − $60,000 − $84,000 − $64,000 = "
                "$196,000; $196,000 / $560,000 = 35.0%. Retained fees "
                "exclude loan principal and already reflect fee reversals "
                "for the modeled cohort."
            ),
            [
                (
                    "Retained brokerage revenue",
                    "$560,000 gross operator revenue",
                    560000.0,
                    (
                        "Opening total equals retained origination and referral "
                        "fees across 40 funded placements. Borrower loan proceeds "
                        "and lender-funded principal remain outside this revenue bar."
                    ),
                ),
                (
                    "Pod delivery compensation",
                    "−$156,000 annual expense",
                    -156000.0,
                    (
                        "Illustrative compensation and employment-cost envelope "
                        "for two full-time seats and two part-time contractor "
                        "seats. Validate local hiring costs and owner compensation "
                        "treatment before adopting this staffing budget."
                    ),
                ),
                (
                    "Recurring operating infrastructure",
                    "−$60,000 annual expense",
                    -60000.0,
                    (
                        "Budget $5,000 monthly for CRM, secure document handling, "
                        "insurance, accounting, office services, and baseline "
                        "professional support. Keep transaction-dependent costs "
                        "outside this recurring infrastructure subtotal."
                    ),
                ),
                (
                    "Acquisition and relationship development",
                    "−$84,000 annual expense",
                    -84000.0,
                    (
                        "Allocate $2,100 per funded placement across 40 outcomes "
                        "for industry outreach, events, content, and relationship "
                        "development. Any compensated referral requires a separate "
                        "activity, licensing, and fee-permissibility assessment."
                    ),
                ),
                (
                    "Transaction and exception handling",
                    "−$64,000 annual expense",
                    -64000.0,
                    (
                        "Allocate $1,600 per funded outcome across the whole "
                        "pipeline for specialized file review, transaction counsel, "
                        "verification, and failed-file work. Exclude costs already "
                        "charged to staffing, infrastructure, or acquisition."
                    ),
                ),
                (
                    "Annual owner net profit",
                    "$196,000 | 35.0% net margin",
                    196000.0,
                    (
                        "Closing total matches the canonical Base Case after "
                        "all four expense deductions. Treat this bar as the "
                        "resulting total rather than an additional positive "
                        "movement in the waterfall."
                    ),
                ),
            ],
        ),
        (
            "diag-04-specialty-placement-fee-yields",
            "horizontal_bars",
            "Compare Retained Fees, Not Financed Principal",
            "Illustrative retained USD per $1,000,000 funded placement.",
            2,
            "illustrative_model",
            (
                "Each bar uses an identical illustrative $1,000,000 financed "
                "amount. Values are retained brokerage fees, not lender yields "
                "or quoted market rates. Eight placements in each of five "
                "categories produce 40 closings, $40,000,000 underlying principal, "
                "and $560,000 operator revenue. Fees require transaction-specific "
                "permissibility, agreement, disclosure, and retention."
            ),
            (
                "Eight times ($15,000 + $10,000 + $10,000 + $20,000 + "
                "$15,000) equals $560,000. The equal-weight average is "
                "$14,000 retained fees per funded placement."
            ),
            [
                (
                    "Equipment acquisition debt",
                    "$15,000 retained | 1.50%",
                    15000.0,
                    (
                        "Model eight placements producing $120,000 retained "
                        "fees. Verify equipment invoices, asset identification, "
                        "useful life, advance rate, and lien position before "
                        "sending the collateral package to lenders."
                    ),
                ),
                (
                    "Receivables-backed facilities",
                    "$10,000 retained | 1.00%",
                    10000.0,
                    (
                        "Model eight placements producing $80,000 retained "
                        "fees. Review dilution, debtor concentration, eligibility "
                        "exclusions, and borrowing-base reporting; model no "
                        "recurring residual compensation unless contractually earned."
                    ),
                ),
                (
                    "SBA-backed business loans",
                    "$10,000 retained | 1.00%",
                    10000.0,
                    (
                        "Model eight placements producing $80,000 retained "
                        "fees. This percentage is an arithmetic assumption, "
                        "not an authorized tariff; apply 13 CFR 103.5, "
                        "current program requirements, and Form 159 where required."
                    ),
                ),
                (
                    "Commercial bridge debt",
                    "$20,000 retained | 2.00%",
                    20000.0,
                    (
                        "Model eight placements producing $160,000 retained "
                        "fees. Verify repayment exit, maturity, collateral "
                        "valuation, and extension terms; resolve real-estate "
                        "broker licensing requirements when collateral triggers them."
                    ),
                ),
                (
                    "Purchase-order working capital",
                    "$15,000 retained | 1.50%",
                    15000.0,
                    (
                        "Model eight placements producing $120,000 retained "
                        "fees. Confirm purchase-order authenticity, supplier "
                        "performance, customer acceptance conditions, and control "
                        "of proceeds before selecting an appropriate funding structure."
                    ),
                ),
            ],
        ),
        (
            "diag-05-statutory-risk-preflight",
            "decision_tree",
            "Four Checks Before a Live Financing Submission",
            "Advance on documented fit; unresolved branches stop the affected activity.",
            5,
            "operating_framework",
            (
                "These are sequential checks, not a universal licensing "
                "determination. Jurisdiction, collateral, product, compensation, "
                "and the broker's actual conduct control applicability. "
                "Numeric values identify check order rather than risk scores."
            ),
            (
                "Keep the legal-scope record beside the lender matrix. "
                "A lender relationship does not itself authorize brokerage "
                "activity, fee collection, or securities placement."
            ),
            [
                (
                    "Activity and licensing",
                    "1 | Proceed or resolve scope",
                    1.0,
                    (
                        "Map borrower, broker, and collateral jurisdictions. "
                        "California Financial Code Section 22100 requires "
                        "licensing for covered finance-lender or broker activity, "
                        "subject to applicable exceptions and scope. Analyze "
                        "real-estate brokerage separately. Securities activity "
                        "requires analysis under 15 U.S.C. 78o(a)(1); stop "
                        "that activity until the required registration path is resolved."
                    ),
                ),
                (
                    "Compensation and disclosure",
                    "2 | Document or revise fees",
                    2.0,
                    (
                        "Identify each payor, service, fee amount, earning event, "
                        "and clawback trigger before engagement. For covered "
                        "SBA agent services, apply 13 CFR 103.5 and required "
                        "Form 159 disclosures. Assess state commercial-financing "
                        "disclosure duties by role and product; revise unsupported "
                        "or impermissible compensation arrangements before proceeding."
                    ),
                ),
                (
                    "Fair lending and file security",
                    "3 | Evidence or remediate controls",
                    3.0,
                    (
                        "Use documented credit-fit criteria under ECOA, "
                        "15 U.S.C. 1691, and Regulation B, 12 CFR part 1002. "
                        "Determine creditor status and allocate notice duties "
                        "without erasing statutory responsibility. For covered "
                        "institutions, implement 16 CFR part 314 safeguards; "
                        "use MFA, restricted access, and documented data handling."
                    ),
                ),
                (
                    "Collateral and closing exposure",
                    "4 | Submit or reduce exposure",
                    4.0,
                    (
                        "Confirm who verifies attachment and perfection under "
                        "UCC 9-203 and 9-310, including applicable exceptions. "
                        "Check lender concentration, closing conditions, and "
                        "commission reversal terms. Use an internal 35% "
                        "single-lender retained-revenue review threshold; excess "
                        "concentration triggers diversification planning, not a claimed statute."
                    ),
                ),
            ],
        ),
        (
            "diag-06-four-to-six-person-pod",
            "org_architecture",
            "Four Core Seats, Two Scale Seats",
            "Base and Conservative: 2 FT + 2 C; Scaled: 3 FT + 3 C.",
            11,
            "operating_framework",
            (
                "Each stage represents one person; contractor seats are "
                "part-time engagements, not full-time equivalents. Numeric "
                "values represent one person each. First four seats form "
                "the core pod; final two are scale additions. Compensation "
                "is scenario-specific and must be tested against actual hiring costs."
            ),
            (
                "Conservative: $120,000 revenue and $30,000 owner net at 25%. "
                "Base: $560,000 and $196,000 at 35%. Scaled: $1,000,000 "
                "and $450,000 at 45%; the scaled scenario uses six people."
            ),
            [
                (
                    "Principal and relationship lead",
                    "Core seat | 1 FT",
                    1.0,
                    (
                        "Own borrower qualification, lender relationships, "
                        "engagement terms, concentration reviews, and fee disputes. "
                        "The owner occupies this operating seat rather than "
                        "appearing as an uncounted fifth core team member."
                    ),
                ),
                (
                    "Credit operations lead",
                    "Core seat | 1 FT",
                    1.0,
                    (
                        "Own application checklists, lender-matrix freshness, "
                        "submission quality, closing conditions, and CRM accuracy. "
                        "Use Airtable and HubSpot automation to surface missing "
                        "documents without automating lender credit decisions."
                    ),
                ),
                (
                    "File analysis specialist",
                    "Core seat | 1 C",
                    1.0,
                    (
                        "Reconcile financial statements, receivables aging, "
                        "equipment schedules, and borrower debt. Work from "
                        "restricted assignments and escalate unexplained balance "
                        "differences before the operations lead releases submissions."
                    ),
                ),
                (
                    "Transaction controls specialist",
                    "Core seat | 1 C",
                    1.0,
                    (
                        "Maintain fee evidence, renewal tracking, access reviews, "
                        "and exception records. Coordinate outside counsel on "
                        "licensing or securities questions without representing "
                        "this contractor as a substitute for required expertise."
                    ),
                ),
                (
                    "Additional relationship manager",
                    "Scale addition | 1 FT",
                    1.0,
                    (
                        "Expand qualified borrower coverage and lender depth "
                        "when sustained pipeline demand supports a third "
                        "full-time seat. Measure funded retained fees and "
                        "closing quality rather than raw submission volume."
                    ),
                ),
                (
                    "Closing and renewal coordinator",
                    "Scale addition | 1 C",
                    1.0,
                    (
                        "Absorb closing-condition follow-up, settlement matching, "
                        "and renewal scheduling at scaled throughput. Add "
                        "capacity only after the core pod demonstrates reliable "
                        "fee collection and bounded exception backlogs."
                    ),
                ),
            ],
        ),
        (
            "diag-07-startup-capital-allocation",
            "stacked_comparison",
            "Allocate Startup Cash Before Chasing Closings",
            "Four buckets across $20,000, $60,000, and $100,000 launch budgets.",
            4,
            "illustrative_model",
            (
                "Numeric values are middle-budget USD components and sum to "
                "$60,000. Each stage's value and detail also specify lean "
                "and upper-budget components; those columns sum to $20,000 "
                "and $100,000. These are capital plans, not revenue scenarios. "
                "Launch spending and reserve balances must not be counted twice."
            ),
            (
                "The middle plan allocates $12,000 + $8,000 + $10,000 + "
                "$30,000 = $60,000. A reserve cannot erase the 3–9 month "
                "first-deal interval or fund unlimited failed-closing work."
            ),
            [
                (
                    "Licensing and professional setup",
                    "Lean $4,000 | Middle $12,000 | Upper $20,000",
                    12000.0,
                    (
                        "Fund jurisdiction-specific licensing analysis, filings "
                        "where required, engagement drafting, insurance setup, "
                        "and compensation review. Restrict launch geography "
                        "when available capital cannot support the required scope."
                    ),
                ),
                (
                    "Secure operating infrastructure",
                    "Lean $3,000 | Middle $8,000 | Upper $12,000",
                    8000.0,
                    (
                        "Configure HubSpot, Airtable, Microsoft 365, secure "
                        "document access, MFA, and backup procedures. Distinguish "
                        "implementation spending and prepaid subscriptions from "
                        "later monthly operating expenses."
                    ),
                ),
                (
                    "Lender and referral development",
                    "Lean $3,000 | Middle $10,000 | Upper $18,000",
                    10000.0,
                    (
                        "Build lender coverage, attend targeted industry events, "
                        "and develop borrower education materials. Validate "
                        "permitted referral arrangements before paying anyone "
                        "for financing introductions or transaction outcomes."
                    ),
                ),
                (
                    "Uncommitted operating reserve",
                    "Lean $10,000 | Middle $30,000 | Upper $50,000",
                    30000.0,
                    (
                        "Preserve cash for collection delays and failed files. "
                        "The middle reserve covers 7.5 months at $4,000 "
                        "monthly cash burn but only 1.67 months at $18,000; "
                        "nine months at $18,000 requires $162,000 before setup costs."
                    ),
                ),
            ],
        ),
        (
            "diag-08-first-thirty-days",
            "timeline_roadmap",
            "Thirty Days to an Evidence-Ready Brokerage Desk",
            "Build scope, systems, lender fit, and pipeline discipline before forecasting fees.",
            12,
            "operating_framework",
            (
                "Four milestones cover Days 1–30 inclusively. Numeric values "
                "are milestone end days. This sprint prepares operations; "
                "the canonical first-deal expectation remains 3–9 months. "
                "Any unresolved licensing requirement prevents affected live activity."
            ),
            (
                "Finish the month with a functioning lender matrix, tested "
                "application checklist, renewal fields, and a funded runway "
                "plan rather than an invented first-month closing target."
            ),
            [
                (
                    "Define the permitted desk",
                    "Days 1–7 | Scope and economics",
                    7.0,
                    (
                        "Choose two initial financing products and launch "
                        "jurisdictions. Document licensing and fee requirements, "
                        "assign the four core seats, and reconcile the "
                        "$120,000, $560,000, and $1,000,000 retained-fee scenarios "
                        "to their respective margins and team sizes."
                    ),
                ),
                (
                    "Build the evidence system",
                    "Days 8–14 | Checklists and security",
                    14.0,
                    (
                        "Configure HubSpot stages, Airtable lender fields, "
                        "document permissions, MFA, and missing-file reminders. "
                        "Test three synthetic borrower files covering equipment, "
                        "receivables, and bridge use cases; resolve access "
                        "and arithmetic defects before loading live records."
                    ),
                ),
                (
                    "Validate lender fit",
                    "Days 15–21 | Coverage and terms",
                    21.0,
                    (
                        "Research eight candidate lenders and obtain documented "
                        "appetite confirmation from at least four. Record "
                        "ticket size, geography, collateral, exclusions, fee "
                        "terms, clawbacks, and contacts. Keep unconfirmed lenders "
                        "outside automated matching recommendations."
                    ),
                ),
                (
                    "Run the controlled pipeline",
                    "Days 22–30 | Outreach and operating review",
                    30.0,
                    (
                        "After required permissions are in place, conduct "
                        "ten qualified referral conversations and request "
                        "three complete borrower packages. Treat these as "
                        "activity targets, not promised conversions. Review "
                        "cash runway, concentration, file defects, and next-month ownership."
                    ),
                ),
            ],
        ),
    ]
    return [
        dict(
            diagram_id=identifier,
            chart_type=kind,
            title=title,
            subtitle=subtitle,
            chapter_number=chapter,
            epistemic_tag=tag,
            assumptions_note=note,
            caption=caption,
            stages=[
                dict(
                    label=label,
                    value=value,
                    numeric_value=float(number),
                    detail=detail,
                )
                for label, value, number, detail in stages
            ],
        )
        for (
            identifier,
            kind,
            title,
            subtitle,
            chapter,
            tag,
            note,
            caption,
            stages,
        ) in specs
    ]
