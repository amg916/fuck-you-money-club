from __future__ import annotations

VOLUME_037_SUBTITLE = (
    "The Complete Playbook for SaaS Discount Brokerage & GPO Arbitrage: "
    "$100,000–$900,000 USD in Annual Retained Revenue; "
    "Start with 1 FT + 3 C (4 People), Scale to 6"
)

VOLUME_037_POSITIONING_ALTERNATIVES = [
    {
        "title": "The Authorized SaaS Renewal Desk",
        "subtitle": (
            "Build recurring retained spreads through authorized Microsoft CSP, "
            "Adobe VIP Marketplace, and vendor-specific partner relationships."
        ),
        "audience": (
            "An owner-led procurement brokerage with three contractors covering "
            "licensing operations, renewal analysis, and collections."
        ),
        "research_basis": (
            "Distinguish vendor authorization from revenue presentation. Vendor "
            "agreements determine transfer rights; ASC 606 principal-versus-agent "
            "analysis determines gross or net presentation. The cited SEC rule "
            "establishes the GAAP framework for applicable SEC financial statements, "
            "not a universal filing obligation for private brokerages. The model "
            "counts retained operator consideration rather than client subscription spend."
        ),
        "sources": [
            "https://www.law.cornell.edu/cfr/text/17/210.4-01",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Evergreen UCaaS Residual Pod",
        "subtitle": (
            "Turn documented business renewal opportunities into contracted "
            "Telarus or Avant master-agent residuals without carrying subscription principal."
        ),
        "audience": (
            "Business communications advisers who can document customer authority, "
            "manage carrier installations, and reconcile monthly residual statements."
        ),
        "research_basis": (
            "Outreach design must distinguish business solicitation from calls or "
            "texts subject to TCPA restrictions. The FTC TSR business-call exemption "
            "does not remove specified prohibitions on deceptive representations. "
            "These rules support evidence-based prospecting, not an assumed right "
            "to automate calls to every business contact."
        ),
        "sources": [
            "https://www.law.cornell.edu/uscode/text/47/227",
            "https://www.law.cornell.edu/cfr/text/16/310.3",
            "https://www.law.cornell.edu/cfr/text/16/310.6",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Private GPO Savings Bureau",
        "subtitle": (
            "Combine contracted administrative rebates with separately earned "
            "25%–35% renewal shared-savings fees and auditable member economics."
        ),
        "audience": (
            "Vertical procurement specialists serving independent businesses with "
            "comparable software needs and separately authorized purchasing decisions."
        ),
        "research_basis": (
            "Sherman Act Section 1 makes purchasing-group structure and competitor "
            "coordination material operating questions. Use written member mandates, "
            "restricted access to sensitive information, and documented rebate "
            "allocation; group purchasing is not blanket permission to coordinate "
            "members' downstream prices or exclude competing suppliers."
        ),
        "sources": [
            "https://www.law.cornell.edu/uscode/text/15/1",
            "https://www.law.cornell.edu/uscode/text/15/2",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
]


def build_volume_037_diagrams_data() -> list[dict]:
    specs = [
        (
            "diag-01-authorized-renewal-workflow",
            "process_flow",
            "From Renewal Signal to Retained Contribution",
            "Five operating steps separate customer subscription spend from earned brokerage revenue.",
            1,
            "operating_framework",
            (
                "The operator has customer permission and current vendor agreements. "
                "Microsoft CPOR attribution is not interchangeable with CSP resale "
                "authority; Adobe VIP Marketplace and Zoom partner routes have "
                "their own eligibility and transfer requirements."
            ),
            (
                "Track one opportunity identifier across discovery, authorization, "
                "quote, activation, and settlement. No stage authorizes cross-customer "
                "seat pooling or converts client subscription spend into operator revenue."
            ),
            [
                (
                    "Detect a renewal trigger",
                    "Permissioned account research",
                    1.0,
                    (
                        "Use public DNS, MX, and SPF signals to prioritize research; "
                        "confirm actual products, seat counts, and renewal dates from "
                        "customer-provided contracts rather than inferring license eligibility."
                    ),
                ),
                (
                    "Verify the authorized route",
                    "Customer mandate and vendor eligibility",
                    2.0,
                    (
                        "Record customer authority and the applicable Microsoft CSP, "
                        "CPOR, Adobe VIP Marketplace, Zoom Up, or master-agent agreement. "
                        "Check transfer windows, tenant boundaries, and existing commitments."
                    ),
                ),
                (
                    "Price the retained economics",
                    "Comparable scope and measurable savings",
                    3.0,
                    (
                        "Normalize term, seats, taxes, support, and service levels. "
                        "Separate vendor-funded spreads from member rebates and "
                        "25%–35% shared-savings fees; disclose any combined compensation."
                    ),
                ),
                (
                    "Activate and reconcile billing",
                    "Authorized changes with funded exposure",
                    4.0,
                    (
                        "Complete vendor-approved changes and reconcile Pax8, Ingram, "
                        "or Telarus records where supported. Fund annual NCE exposure "
                        "before commitment; monthly auto-debit alone does not cover it."
                    ),
                ),
                (
                    "Recognize and monitor earnings",
                    "Earned consideration with clawback tracking",
                    5.0,
                    (
                        "Reconcile partner statements, customer acceptance, rebate "
                        "conditions, and residual receipts. Apply ASC 606 contract "
                        "analysis and maintain separate ledgers for client pass-through "
                        "amounts, operator earnings, and potential reversals."
                    ),
                ),
            ],
        ),
        (
            "diag-02-renewal-cohort-funnel",
            "funnel",
            "A Nested Annual Cohort Supporting the Base Case",
            "200 permissioned opportunities narrow to 10 activated portfolio accounts.",
            6,
            "illustrative_model",
            (
                "Illustrative annual acquisition cohort, not measured conversion data. "
                "Each stage is a subset of the preceding stage. Ten portfolio accounts "
                "each contribute $50,000 in annual recognized retained revenue after "
                "full activation; partial-year activation produces less revenue."
            ),
            (
                "Stage conversions are 50%, 50%, 50%, and 40%; overall conversion "
                "is 5%. Ten accounts multiplied by $50,000 equals the $500,000 "
                "Base-Case annual revenue target. First-deal timing remains 1–3 months."
            ),
            [
                (
                    "Permissioned opportunities",
                    "200 accounts with documented renewal windows",
                    200.0,
                    (
                        "Count distinct prospective portfolio accounts with an identified "
                        "buyer, a documented contact basis, and a contract renewal window; "
                        "exclude scraped contact lists without qualification."
                    ),
                ),
                (
                    "Evidence-complete accounts",
                    "100 accounts with usable contract evidence",
                    100.0,
                    (
                        "Half the original cohort supplies invoices, product identifiers, "
                        "seat counts, commitment dates, and procurement authority sufficient "
                        "to calculate a comparable incumbent baseline."
                    ),
                ),
                (
                    "Eligible economic cases",
                    "50 accounts with authorized positive economics",
                    50.0,
                    (
                        "Half the evidence-complete accounts passes vendor eligibility, "
                        "minimum retained contribution, and funding checks after migration "
                        "costs, concessions, and expected clawbacks."
                    ),
                ),
                (
                    "Signed mandates",
                    "25 accounts with executed commercial terms",
                    25.0,
                    (
                        "Half the eligible accounts executes a mandate defining "
                        "compensation, savings measurement, rebate ownership, customer "
                        "responsibilities, and the permitted licensing route."
                    ),
                ),
                (
                    "Activated earning accounts",
                    "10 accounts earning $50,000 annually each",
                    10.0,
                    (
                        "Forty percent of signed accounts completes activation and "
                        "begins earning contracted consideration. Treat $500,000 as "
                        "full-year recognized revenue only when service timing supports it."
                    ),
                ),
            ],
        ),
        (
            "diag-03-base-case-profit-waterfall",
            "waterfall",
            "Base-Case Revenue to $225,000 Owner Profit",
            "$500,000 retained operator revenue less $275,000 operating costs yields 45.0%.",
            3,
            "illustrative_model",
            (
                "Six bars contain an opening total, four signed deductions, and a "
                "closing total; the final bar is not another increment. Cost allocations "
                "are illustrative because only scenario totals are canonical. Opening "
                "gross revenue is gross within the operator income statement but already "
                "net of client subscription pass-through under the specified agency model."
            ),
            (
                "$500,000 − $120,000 − $75,000 − $50,000 − $30,000 = $225,000; "
                "$225,000 / $500,000 = 45.0%. Conservative is $100,000 revenue, "
                "$68,000 costs, and $32,000 profit at 32%. Scaled is $900,000 revenue, "
                "$378,000 costs, and $522,000 profit at 58%. The supplied monthly opex "
                "range of $1,500–$9,500 is not a ceiling on all-in annual scenario costs."
            ),
            [
                (
                    "Recognized retained revenue",
                    "$500,000 opening operator revenue total",
                    500000.0,
                    (
                        "Count earned partner spreads, master-agent residuals, GPO "
                        "administrative rebates, and shared-savings fees. Exclude client "
                        "software subscription principal and avoid applying a second "
                        "retained-share reduction to this already-retained revenue."
                    ),
                ),
                (
                    "Contractor delivery",
                    "−$120,000 annual delivery labor allocation",
                    -120000.0,
                    (
                        "Allocate licensing operations, savings verification, and "
                        "reconciliation work across the three contractor seats. "
                        "This modeled deduction leaves $380,000 before remaining costs."
                    ),
                ),
                (
                    "Acquisition and channel servicing",
                    "−$75,000 annual variable commercial costs",
                    -75000.0,
                    (
                        "Budget qualified outreach, referral compensation, account "
                        "onboarding, and partner-servicing costs without duplicating "
                        "deductions already embedded in retained partner spreads."
                    ),
                ),
                (
                    "Systems and professional operations",
                    "−$50,000 annual infrastructure operating allocation",
                    -50000.0,
                    (
                        "Cover CRM, document storage, reconciliation tooling, bookkeeping, "
                        "contract review, insurance, and operating administration. "
                        "The modeled running balance becomes $255,000."
                    ),
                ),
                (
                    "Credit and service-loss expense",
                    "−$30,000 annual modeled loss allocation",
                    -30000.0,
                    (
                        "Model unrecovered customer exposure and service remediation "
                        "as expenses. Revenue reversals already netted from the opening "
                        "total must not also appear in this deduction."
                    ),
                ),
                (
                    "Owner net profit",
                    "$225,000 closing profit at 45.0%",
                    225000.0,
                    (
                        "This is the canonical annual owner-profit endpoint, not "
                        "another source of revenue. Personal taxes, financing choices, "
                        "and owner distributions are not separately modeled."
                    ),
                ),
            ],
        ),
        (
            "diag-04-retained-yield-by-commercial-rail",
            "horizontal_bars",
            "Compare Retained Yield on a Common Spend Denominator",
            "Five illustrative commercial rails measured against $100,000 of eligible annual client spend.",
            2,
            "illustrative_model",
            (
                "Numeric values are modeled retained revenue dollars, not published "
                "vendor rates or profit margins. Use comparable annual scope and "
                "exclude taxes. Rails are alternatives unless executed agreements "
                "expressly permit combined compensation without duplicate billing."
            ),
            (
                "The spend denominator belongs to the customer. At a modeled 8% "
                "retained yield, $6,250,000 of eligible spend would produce $500,000 "
                "operator revenue; it would not create $6,250,000 of operator revenue."
            ),
            [
                (
                    "Microsoft CSP retained spread",
                    "$8,000 retained from $100,000 eligible spend",
                    8000.0,
                    (
                        "Assume an 8% retained spread after upstream shares. Confirm "
                        "current CSP economics and NCE commitment exposure; CPOR "
                        "attribution alone does not establish a resale discount."
                    ),
                ),
                (
                    "Adobe VIP Marketplace spread",
                    "$10,000 retained from $100,000 eligible spend",
                    10000.0,
                    (
                        "Assume a 10% retained spread under an authorized reseller "
                        "arrangement. Validate customer eligibility, volume brackets, "
                        "term alignment, and distributor deductions before quoting."
                    ),
                ),
                (
                    "Zoom or UCaaS residual",
                    "$6,000 retained from $100,000 eligible spend",
                    6000.0,
                    (
                        "Assume a 6% annual retained residual after master-agent "
                        "shares. Reconcile Telarus or Avant statements and account "
                        "for installation delays, cancellations, and contracted chargebacks."
                    ),
                ),
                (
                    "Private GPO administrative rebate",
                    "$4,000 retained from $100,000 eligible spend",
                    4000.0,
                    (
                        "Assume a 4% earned administrative rebate after member "
                        "allocations. Confirm the purchasing bracket, qualifying spend, "
                        "payment timing, and which party owns each rebate component."
                    ),
                ),
                (
                    "Renewal shared-savings fee",
                    "$6,000 retained from $20,000 verified savings",
                    6000.0,
                    (
                        "Reduce a comparable $100,000 baseline to $80,000 and earn "
                        "30% of the $20,000 verified reduction. The contracted "
                        "25%–35% fee range would produce $5,000–$7,000."
                    ),
                ),
            ],
        ),
        (
            "diag-05-statutory-and-exposure-decision-tree",
            "decision_tree",
            "Four Checks Before a Binding Commitment",
            "Proceed only when authority, funding, outreach, and purchasing-group structure are documented.",
            5,
            "operating_framework",
            (
                "These are sequential yes-or-no operating checks. Contractual licensing "
                "requirements and the internal credit policy are distinct from statutory "
                "duties. A failed check routes the account to the stated corrective "
                "action rather than silently advancing to execution."
            ),
            (
                "Keep the supporting contract, funds evidence, outreach basis, and "
                "member mandate with the opportunity record. Statutes do not grant "
                "vendor transfer rights, and a customer signature does not eliminate "
                "annual vendor commitment exposure."
            ),
            [
                (
                    "Authorized licensing route?",
                    "Yes proceed; no obtain valid authority",
                    1.0,
                    (
                        "Verify the customer mandate and applicable CSP, CPOR, VIP "
                        "Marketplace, Zoom, or GPO agreement. Reject unauthorized "
                        "cross-tenant seat pooling; use the vendor-approved transfer "
                        "process or retain the existing arrangement."
                    ),
                ),
                (
                    "Annual exposure fully covered?",
                    "Yes proceed; no defer the commitment",
                    2.0,
                    (
                        "Require cleared customer funding covering the committed NCE "
                        "exposure and monitor ACH return or card dispute risk. "
                        "Recurring debit authorization is a collection mechanism, "
                        "not proof of irrevocable annual funding."
                    ),
                ),
                (
                    "Outreach route permitted?",
                    "Yes proceed; no redesign the contact method",
                    3.0,
                    (
                        "Apply 47 U.S.C. 227 and applicable FCC rules to calls and "
                        "texts. Under 16 CFR 310.3 and 310.6(b)(7), do not treat "
                        "business solicitation as exempt from specified deception "
                        "prohibitions; assess relevant state calling requirements."
                    ),
                ),
                (
                    "GPO conduct independently defensible?",
                    "Yes execute; no obtain structure-specific review",
                    4.0,
                    (
                        "Assess competitor coordination under 15 U.S.C. 1. Preserve "
                        "independent member purchasing decisions, restrict competitively "
                        "sensitive information, document rebate ownership, and exclude "
                        "downstream price coordination from the member arrangement."
                    ),
                ),
            ],
        ),
        (
            "diag-06-four-to-six-person-pod",
            "org_architecture",
            "Four Core Seats, Two Explicit Scaling Additions",
            "Conservative and Base use 1 FT + 3 C; Scaled uses 2 FT + 4 C.",
            11,
            "operating_framework",
            (
                "FT means full-time and C means contractor. Numeric values indicate "
                "baseline seat occupancy: four active seats and two inactive expansion "
                "seats. Activate both expansion seats to reach the six-person Scaled pod."
            ),
            (
                "The four-person pod supports the canonical $100,000 Conservative "
                "and $500,000 Base revenue cases. The six-person pod corresponds "
                "to $900,000 Scaled revenue; headcount alone does not establish demand."
            ),
            [
                (
                    "Owner and commercial lead",
                    "One full-time core seat owns economics",
                    1.0,
                    (
                        "Own vendor relationships, pricing, customer commitments, "
                        "concentration limits, and cash exposure. Review exception "
                        "reports instead of manually rebuilding every partner statement."
                    ),
                ),
                (
                    "Licensing operations specialist",
                    "One contractor core seat owns activation",
                    1.0,
                    (
                        "Validate tenant boundaries, transfer eligibility, product "
                        "identifiers, commitment dates, and distributor records. "
                        "Maintain evidence for every customer-authorized license change."
                    ),
                ),
                (
                    "Savings and procurement analyst",
                    "One contractor core seat owns measurement",
                    1.0,
                    (
                        "Build comparable incumbent baselines, test price floors, "
                        "calculate contingent fees, and distinguish seat reductions "
                        "from genuine like-for-like procurement savings."
                    ),
                ),
                (
                    "Billing and collections specialist",
                    "One contractor core seat owns reconciliation",
                    1.0,
                    (
                        "Match customer receipts, distributor charges, residual "
                        "statements, and rebate settlements. Escalate funding gaps "
                        "before a new annual vendor commitment is created."
                    ),
                ),
                (
                    "Scaled operations manager",
                    "Add one full-time seat when scaling",
                    0.0,
                    (
                        "Join the existing owner to create two full-time seats. "
                        "Own delivery capacity, workflow exceptions, contractor "
                        "coordination, and renewal-service continuity."
                    ),
                ),
                (
                    "Scaled portfolio analyst",
                    "Add one contractor seat when scaling",
                    0.0,
                    (
                        "Join the three core contractors to create four contractor "
                        "seats. Expand renewal monitoring, rebate verification, "
                        "and independent checks on shared-savings calculations."
                    ),
                ),
            ],
        ),
        (
            "diag-07-startup-capital-allocation",
            "stacked_comparison",
            "Four Buckets Across a $5,000–$30,000 Launch",
            "Lean, working, and expanded launch budgets total $5,000, $15,000, and $30,000.",
            4,
            "illustrative_model",
            (
                "Numeric values show the $15,000 working-budget allocation. Each "
                "stage also states lean and expanded amounts for comparison. These "
                "are startup allocations, not annual operating expenses or canonical "
                "revenue scenarios; no bucket finances customer subscription principal."
            ),
            (
                "The working allocation is $4,500 + $3,000 + $4,500 + $3,000 = "
                "$15,000. Monthly opex remains the supplied $1,500–$9,500 planning "
                "range. Protect runway through the 1–3 month first-deal window "
                "without using customer-designated funds for brokerage expenses."
            ),
            [
                (
                    "Partner and contract setup",
                    "Lean $1,500; working $4,500; expanded $9,000",
                    4500.0,
                    (
                        "Allocate 30% to agreement review, customer mandates, "
                        "bookkeeping setup, partner onboarding work, and insurance "
                        "setup. Vendor-specific deposits require separate verification."
                    ),
                ),
                (
                    "Systems and reconciliation",
                    "Lean $1,000; working $3,000; expanded $6,000",
                    3000.0,
                    (
                        "Allocate 20% to CRM configuration, access-controlled document "
                        "storage, statement imports, renewal tracking, and audit-ready "
                        "reconciliation templates before purchasing custom integrations."
                    ),
                ),
                (
                    "Evidence-led acquisition",
                    "Lean $1,500; working $4,500; expanded $9,000",
                    4500.0,
                    (
                        "Allocate 30% to vertical prospect research, buyer interviews, "
                        "permissioned outreach, and initial contract audits. Measure "
                        "qualified opportunities rather than purchased contact volume."
                    ),
                ),
                (
                    "Brokerage liquidity reserve",
                    "Lean $1,000; working $3,000; expanded $6,000",
                    3000.0,
                    (
                        "Allocate 20% to brokerage timing gaps and operating "
                        "contingencies. Keep this reserve distinct from customer "
                        "prefunding and increase runway if sales or settlement takes longer."
                    ),
                ),
            ],
        ),
        (
            "diag-08-thirty-day-launch-roadmap",
            "timeline_roadmap",
            "A 30-Day Sprint to an Execution-Ready Brokerage",
            "Build evidence and operating readiness before forecasting collected residuals.",
            12,
            "operating_framework",
            (
                "The four milestones span Days 1–30. Activities use authorized "
                "project resources and customer-provided records. Partner onboarding, "
                "renewal timing, and vendor activation can extend beyond this sprint; "
                "the canonical first-deal range is 1–3 months."
            ),
            (
                "Finish the sprint with a defined niche, verified economics, "
                "executable documents, and a reconciled pilot or documented activation "
                "schedule. Do not label quoted savings, unsigned rebates, or future "
                "residuals as recognized revenue."
            ),
            [
                (
                    "Days 1-7",
                    "Choose one niche and verify partner routes",
                    1.0,
                    (
                        "Select a repeatable buyer segment, obtain current partner "
                        "terms, define excluded license arrangements, and build a "
                        "retained-revenue worksheet separating subscription principal "
                        "from operator consideration."
                    ),
                ),
                (
                    "Days 8-14",
                    "Collect evidence and test comparable economics",
                    2.0,
                    (
                        "Request permissioned renewal contracts, normalize product "
                        "scope, test vendor price floors, and calculate prospective "
                        "shared-savings fees. Document why each candidate passes "
                        "or fails the four pre-commitment checks."
                    ),
                ),
                (
                    "Days 15-21",
                    "Execute mandates and establish funded readiness",
                    3.0,
                    (
                        "Finalize compensation terms, member rebate allocation, "
                        "customer authority, and permitted transfer steps. Verify "
                        "funding before annual commitments and configure distributor "
                        "or master-agent statement reconciliation."
                    ),
                ),
                (
                    "Days 22-30",
                    "Reconcile a pilot and schedule remaining activation",
                    4.0,
                    (
                        "Complete one authorized pilot when vendor timing permits, "
                        "or record the dated activation dependency. Reconcile earned "
                        "consideration, inspect exception handling, and compare "
                        "forecast contribution with the Base-Case cost structure."
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
