from __future__ import annotations

VOLUME_013_SUBTITLE: str = (
    "The Complete Playbook for $50,000–$800,000 USD in Annual IP Licensing "
    "Revenue: Launch with 1 FT + 3 C (4 People), Scale to 6 People"
)

VOLUME_013_POSITIONING_ALTERNATIVES: list[dict] = [
    {
        "title": "The Patent Licensing Deal Desk",
        "subtitle": (
            "Convert documented patent rights into field-of-use licenses, "
            "minimum guarantees, and auditable royalty schedules."
        ),
        "audience": (
            "Patent owners and authorized licensing operators with documented "
            "assignments, technical evidence, and access to prospective manufacturers."
        ),
        "research_basis": (
            "35 U.S.C. 261 addresses patent ownership and assignments; "
            "35 U.S.C. 154 defines patent rights and statutory term. "
            "These provisions support an operating sequence that checks ownership, "
            "remaining term, territory, and licensed claims before pricing rights. "
            "They do not establish buyer demand or a commercially achievable royalty."
        ),
        "sources": [
            "https://www.law.cornell.edu/uscode/text/35/261",
            "https://www.law.cornell.edu/uscode/text/35/154",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Brand Royalty Operating System",
        "subtitle": (
            "Build controlled brand licenses with product approvals, minimum "
            "guarantees, territory schedules, and reconciled royalty statements."
        ),
        "audience": (
            "Trademark owners and authorized brand operators licensing defined "
            "product categories to manufacturers with inspectable sales records."
        ),
        "research_basis": (
            "15 U.S.C. 1055 addresses controlled use by related companies, "
            "while 15 U.S.C. 1127 supplies relevant definitions. "
            "16 CFR 436.1 supplies franchise definitions requiring a separate "
            "classification check when brand rights accompany operating assistance "
            "or control and required payments."
        ),
        "sources": [
            "https://www.law.cornell.edu/uscode/text/15/1055",
            "https://www.law.cornell.edu/uscode/text/15/1127",
            "https://www.ecfr.gov/current/title-16/chapter-I/subchapter-D/part-436/section-436.1",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Catalog and Dataset Rights Desk",
        "subtitle": (
            "Package cleared catalogs and controlled datasets into permitted-use "
            "licenses with renewal calendars and reproducible usage evidence."
        ),
        "audience": (
            "Catalog owners, publishers, and dataset operators with documented "
            "provenance, contributor agreements, and enforceable access controls."
        ),
        "research_basis": (
            "17 U.S.C. 102 distinguishes protected expression from excluded "
            "ideas and methods; 17 U.S.C. 103 limits compilation protection "
            "to qualifying contributions rather than underlying material. "
            "17 U.S.C. 204 addresses transfers of copyright ownership. "
            "18 U.S.C. 1839 defines trade secrets, including reasonable secrecy "
            "measures. Dataset licensing therefore requires a rights-specific "
            "analysis rather than an assumption that every collected fact is owned."
        ),
        "sources": [
            "https://www.law.cornell.edu/uscode/text/17/102",
            "https://www.law.cornell.edu/uscode/text/17/103",
            "https://www.law.cornell.edu/uscode/text/17/204",
            "https://www.law.cornell.edu/uscode/text/18/1839",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
]


def build_volume_013_diagrams_data() -> list[dict]:
    specs = [
        (
            "diag-01-rights-to-royalties",
            "process_flow",
            "Turn Controlled Rights into Collectible Royalties",
            "Five evidence-backed handoffs from asset intake to renewal.",
            1,
            "operating_framework",
            (
                "Stages show operating sequence, not elapsed months or conversion "
                "rates. First-deal planning remains 4–14 months. Recognized revenue "
                "consists of operator license fees and royalties, excluding "
                "licensees' underlying product sales."
            ),
            (
                "Every handoff produces an inspectable record; a signed license "
                "does not replace usage evidence or a reconciled royalty statement."
            ),
            [
                (
                    "Establish ownership",
                    "Signed rights dossier and exception register",
                    1,
                    (
                        "Collect assignments, contributor agreements, registration "
                        "records, encumbrances, and sublicensing authority. Apply "
                        "35 U.S.C. 261 and 17 U.S.C. 204 to relevant transfers."
                    ),
                ),
                (
                    "Define licensed scope",
                    "Asset schedule and permitted-use boundaries",
                    2,
                    (
                        "Specify patent claims, brand categories, catalog assets, "
                        "or dataset fields; record territory, term, exclusivity, "
                        "derivative uses, and prohibited redistribution."
                    ),
                ),
                (
                    "Validate buyer economics",
                    "Named buyer and measurable commercial use",
                    3,
                    (
                        "Interview the licensee's product owner, identify a "
                        "budget owner, and test whether the rights solve a "
                        "specific product, distribution, or research constraint."
                    ),
                ),
                (
                    "Execute measurable terms",
                    "Royalty schedule and enforceable reporting obligations",
                    4,
                    (
                        "Document royalty base, permitted deductions, minimum "
                        "guarantees, payment dates, audit access, cure periods, "
                        "quality controls, and termination consequences."
                    ),
                ),
                (
                    "Reconcile and renew",
                    "Matched usage, statements, invoices, and receipts",
                    5,
                    (
                        "Join licensee reports to invoice records in SQLite; "
                        "schedule renewal alerts and exception reviews. Investigate "
                        "missing territories, unexplained deductions, and late reports."
                    ),
                ),
            ],
        ),
        (
            "diag-02-qualified-licensee-cohorts",
            "funnel",
            "A Nested Licensee Development Funnel",
            "One 200-account cohort; five progressively narrower evidence states.",
            6,
            "illustrative_model",
            (
                "Illustrative account counts across a 6–24-month development "
                "window, not a measured benchmark or a 30-day closing promise. "
                "Every later cohort is a subset of the preceding cohort. "
                "These counts do not derive the canonical annual revenue scenarios."
            ),
            (
                "Sequential conversion is 40%, 40%, 37.5%, and 41.67%; "
                "five executed licensees represent 2.5% of the original cohort."
            ),
            [
                (
                    "Screened accounts",
                    "200 accounts with relevant commercial applications",
                    200,
                    (
                        "Each account has an identified product category, "
                        "operating territory, and plausible use for the controlled rights."
                    ),
                ),
                (
                    "Confirmed use cases",
                    "80 accounts with documented buyer interest",
                    80,
                    (
                        "Eighty of 200 accounts confirm a specific application "
                        "and identify a contact responsible for evaluating the rights."
                    ),
                ),
                (
                    "Diligence participants",
                    "32 accounts exchanging technical and rights evidence",
                    32,
                    (
                        "Thirty-two of 80 accounts review the rights package "
                        "and supply enough product information to assess licensing fit."
                    ),
                ),
                (
                    "Negotiated term sheets",
                    "12 accounts negotiating scope and economics",
                    12,
                    (
                        "Twelve of 32 accounts negotiate permitted uses, "
                        "minimum guarantees, royalty bases, and reporting capabilities."
                    ),
                ),
                (
                    "Executed licensees",
                    "5 accounts with signed reporting obligations",
                    5,
                    (
                        "Five of 12 negotiating accounts execute agreements. "
                        "Track invoicing, collection, and revenue recognition separately."
                    ),
                ),
            ],
        ),
        (
            "diag-03-base-case-profit-bridge",
            "waterfall",
            "The $425,000 Base-Case Profit Bridge",
            "Four cost deductions reconcile to $180,625 owner net profit.",
            3,
            "illustrative_model",
            (
                "Annual USD. Opening and closing bars are absolute totals; "
                "intermediate bars are signed deductions. The cost allocation "
                "is illustrative, while revenue, profit, and margin are canonical. "
                "This example assumes the operator controls sublicensed rights "
                "and recognizes the associated fees gross; agency pass-through "
                "receipts are excluded. Recurring personnel and administration "
                "total $10,000 monthly; rights participation and transaction-specific "
                "legal and audit expenses are additional variable costs."
            ),
            (
                "$425,000 - $96,000 - $24,000 - $85,000 - $39,375 "
                "= $180,625. Total modeled costs are $244,375; "
                "$180,625 / $425,000 = 42.5%."
            ),
            [
                (
                    "Recognized license revenue",
                    "$425,000 annual operator fees and royalties",
                    425000,
                    (
                        "Opening total includes recognized license fees and "
                        "royalties only, never the licensees' product-sales base."
                    ),
                ),
                (
                    "Personnel and delivery",
                    "Deduct $96,000 for recurring pod work",
                    -96000,
                    (
                        "Illustrative annual allowance for operator delivery "
                        "and recurring contractor retainers; exclude distributions "
                        "of the closing owner profit."
                    ),
                ),
                (
                    "Systems and administration",
                    "Deduct $24,000 for recurring operating infrastructure",
                    -24000,
                    (
                        "Fund reporting tools, insurance, bookkeeping, secure "
                        "document storage, and administration without duplicating personnel costs."
                    ),
                ),
                (
                    "Rights-holder participation",
                    "Deduct $85,000 in contractual rights payments",
                    -85000,
                    (
                        "Illustrative 20% participation on recognized revenue "
                        "under controlled sublicensing arrangements; replace this "
                        "allocation when the actual rights structure differs."
                    ),
                ),
                (
                    "Deal-specific legal and audits",
                    "Deduct $39,375 for variable specialist services",
                    -39375,
                    (
                        "Expense transaction-specific drafting, rights investigation, "
                        "and royalty examinations separately from recurring retainers; "
                        "this bar is not an unspent cash reserve."
                    ),
                ),
                (
                    "Annual owner net profit",
                    "$180,625 retained at 42.5% modeled margin",
                    180625,
                    (
                        "Closing total equals revenue less all four modeled "
                        "cost categories and matches the canonical Base-Case result."
                    ),
                ),
            ],
        ),
        (
            "diag-04-license-structure-yields",
            "horizontal_bars",
            "Compare Annual License Receipts by Rights Package",
            "Five illustrative agreement-level yields, all expressed in USD.",
            2,
            "illustrative_model",
            (
                "Bars show hypothetical annual operator fees for one agreement, "
                "not market royalty benchmarks, profit, or additive portfolio "
                "revenue. Assume a full licensed year, earned fees, and collection "
                "without withholding or payment charges. Minimum guarantees are "
                "creditable against royalties rather than added to them."
            ),
            (
                "Compare license economics on one annual fee basis; "
                "the licensee's sales remain a royalty calculation input only."
            ),
            [
                (
                    "Patent field-of-use license",
                    "$20,000 annual royalty from defined product sales",
                    20000,
                    (
                        "Illustrative 2% royalty on $1,000,000 of contract-defined "
                        "net product sales; recognize $20,000, not the sales base. "
                        "Collect against quarterly statements."
                    ),
                ),
                (
                    "Brand category license",
                    "$30,000 annual minimum exceeds calculated royalties",
                    30000,
                    (
                        "Illustrative greater of a $30,000 minimum or 4% "
                        "of $600,000 net sales. The $24,000 royalty is covered "
                        "by the minimum, not added to it."
                    ),
                ),
                (
                    "Cleared catalog license",
                    "$15,000 annual fee for scheduled catalog assets",
                    15000,
                    (
                        "Illustrative 100 cleared assets at $150 each for "
                        "one annual use scope; additional media or territories "
                        "require a separately priced amendment."
                    ),
                ),
                (
                    "Controlled dataset license",
                    "$25,000 annual fee for bounded dataset access",
                    25000,
                    (
                        "Illustrative five business units at $5,000 annually "
                        "with permitted-use and redistribution limits; access logs "
                        "support scope reconciliation rather than ownership claims."
                    ),
                ),
                (
                    "Bundled technology package",
                    "$50,000 annual fee across two licensed facilities",
                    50000,
                    (
                        "Illustrative two facilities at $25,000 annually for "
                        "scheduled patent and know-how rights; define included "
                        "support so service effort does not consume the margin."
                    ),
                ),
            ],
        ),
        (
            "diag-05-preflight-rights-and-risk",
            "decision_tree",
            "Four Pre-Flight Decisions Before Commercial Commitment",
            "Proceed on documented evidence; remediate the specific failed check.",
            5,
            "operating_framework",
            (
                "Numeric values identify ordered decision nodes, not risk "
                "probabilities. Each node states its pass and remediation branches. "
                "Apply statutes to the actual rights, transaction, and territory; "
                "the checks are not interchangeable across asset classes."
            ),
            (
                "Resolve title, scope, commercial restrictions, and evidence "
                "access before promising an exclusive or unrestricted license."
            ),
            [
                (
                    "Can the operator grant these rights?",
                    "Pass documented title; otherwise repair ownership evidence",
                    1,
                    (
                        "Review assignments, liens, joint ownership, and sublicensing "
                        "authority under 35 U.S.C. 261 or 17 U.S.C. 204 as "
                        "applicable. If authority is supported, continue; otherwise "
                        "obtain the missing grant or exclude the affected asset."
                    ),
                ),
                (
                    "Does the proposed use fit the rights?",
                    "Pass supported scope; otherwise narrow the licensed grant",
                    2,
                    (
                        "Check territory, duration, patent status, third-party "
                        "material, and permitted data uses. Apply 17 U.S.C. "
                        "102–103 to expression and compilations and 18 U.S.C. "
                        "1839 to claimed trade secrets. Proceed only with supported scope."
                    ),
                ),
                (
                    "Are commercial restrictions defensible?",
                    "Pass reviewed terms; otherwise revise restrictive provisions",
                    3,
                    (
                        "Review exclusivity, tying, and resale restrictions under "
                        "15 U.S.C. 1 without assuming exclusivity is inherently "
                        "unlawful. For brand arrangements, assess 16 CFR 436.1 "
                        "and applicable state franchise rules; resolve classification "
                        "and required disclosures before execution."
                    ),
                ),
                (
                    "Can performance and misuse be detected?",
                    "Pass inspectable controls; otherwise redesign monitoring terms",
                    4,
                    (
                        "Require royalty records, audit access, retention periods, "
                        "and enforceable remedies. For trademarks, document quality "
                        "control relevant to 15 U.S.C. 1055 and 1127. "
                        "If evidence cannot be inspected, revise terms or decline."
                    ),
                ),
            ],
        ),
        (
            "diag-06-four-to-six-person-pod",
            "org_architecture",
            "A Four-Person Core with Two Explicit Scale Seats",
            "Base: 1 FT + 3 C. Scaled: 2 FT + 4 C.",
            11,
            "operating_framework",
            (
                "FT denotes a full-time seat; C denotes a contractor person, "
                "not a full-time equivalent. Each node represents one person. "
                "Conservative: $50,000 annual revenue, 25% margin, $12,500 "
                "owner net, 1 FT + 3 C. Base: $425,000 annual revenue, "
                "42.5% margin, $180,625 owner net, 1 FT + 3 C. "
                "Scaled: $800,000 annual revenue, 60% margin, $480,000 "
                "owner net, 2 FT + 4 C. Revenue excludes licensee product sales."
            ),
            (
                "Seats one through four form the core pod; seats five "
                "and six are additions for the Scaled Small-Team scenario."
            ),
            [
                (
                    "Licensing principal",
                    "Core full-time seat owning commercial decisions",
                    1,
                    (
                        "Own buyer development, pricing, rights strategy, and "
                        "renewal negotiation. Resolve exceptions across the "
                        "contractor workstreams and retain responsibility for commitments."
                    ),
                ),
                (
                    "IP transaction counsel",
                    "Core contractor seat owning rights documentation",
                    1,
                    (
                        "Review chain of title, draft scoped grants, assess "
                        "statutory issues, and manage disputes. Separate recurring "
                        "retainer work from separately billed transaction services."
                    ),
                ),
                (
                    "Royalty reporting specialist",
                    "Core contractor seat owning statements and collections",
                    1,
                    (
                        "Reconcile licensee reports, inspect deductions, issue "
                        "invoices, and escalate missing receipts. Maintain auditable "
                        "links between contract terms and reported royalty calculations."
                    ),
                ),
                (
                    "Technical rights analyst",
                    "Core contractor seat owning asset-use evidence",
                    1,
                    (
                        "Map claims, catalog provenance, dataset permissions, "
                        "and licensee use evidence. Maintain the rights inventory "
                        "and support counsel without making unsupported ownership assertions."
                    ),
                ),
                (
                    "Licensee success manager",
                    "Scaled additional full-time seat owning account execution",
                    1,
                    (
                        "Add at the six-person scenario to own onboarding, "
                        "obligation tracking, renewal alerts, and routine account "
                        "coordination while the principal concentrates on negotiations."
                    ),
                ),
                (
                    "Royalty audit examiner",
                    "Scaled additional contractor seat owning exception examinations",
                    1,
                    (
                        "Add targeted examinations of source sales records "
                        "and usage logs; avoid auditing their own reporting work "
                        "and route disputed findings through counsel."
                    ),
                ),
            ],
        ),
        (
            "diag-07-forty-thousand-startup-capital-buckets",
            "stacked_comparison",
            "Allocate a $40,000 Reference Startup Budget Across Four Buckets",
            "Compare lean $12,000, reference $40,000, and expanded $75,000 plans.",
            4,
            "illustrative_model",
            (
                "Numeric values are USD allocations for the illustrative "
                "$40,000 reference plan within the $12,000–$75,000 startup "
                "capital range, not annual expenses or canonical revenue. "
                "The same 35% / 25% / 20% / 20% split produces the lean "
                "$12,000 and expanded $75,000 comparisons stated in the details. "
                "Startup capital does not establish runway: recurring monthly "
                "opex is $2,000–$12,000 and first-deal timing is 4–14 months."
            ),
            (
                "Reference: $14,000 + $10,000 + $8,000 + $8,000 = $40,000. "
                "Lean: $4,200 + $3,000 + $2,400 + $2,400 = $12,000. "
                "Expanded: $26,250 + $18,750 + $15,000 + $15,000 = $75,000. "
                "The reference liquidity bucket covers 0.8 months at $10,000 "
                "recurring monthly opex, so separately fund the remaining "
                "development period and variable costs."
            ),
            [
                (
                    "Rights diligence and contracting",
                    "$14,000 reference plan allocation for defensible grants",
                    14000,
                    (
                        "Allocate 35% to title investigation, asset schedules, "
                        "and contract drafting: $4,200 in the lean $12,000 plan, "
                        "$14,000 in the reference $40,000 plan, and $26,250 "
                        "in the expanded $75,000 plan."
                    ),
                ),
                (
                    "Buyer validation and packaging",
                    "$10,000 reference plan allocation for commercial evidence",
                    10000,
                    (
                        "Allocate 25% to technical demonstrations, buyer interviews, "
                        "and scoped licensing materials: $3,000 in the lean "
                        "$12,000 plan, $10,000 in the reference $40,000 plan, "
                        "and $18,750 in the expanded $75,000 plan."
                    ),
                ),
                (
                    "Reporting and obligation systems",
                    "$8,000 reference plan allocation for inspectable operations",
                    8000,
                    (
                        "Allocate 20% to report templates, controlled document "
                        "storage, SQLite reconciliation, and renewal scheduling: "
                        "$2,400 in the lean $12,000 plan, $8,000 in the reference "
                        "$40,000 plan, and $15,000 in the expanded $75,000 plan."
                    ),
                ),
                (
                    "Uncommitted operating liquidity",
                    "$8,000 reference plan allocation for cash continuity",
                    8000,
                    (
                        "Hold 20% as cash rather than recording an immediate "
                        "expense: $2,400 in the lean $12,000 plan, $8,000 in "
                        "the reference $40,000 plan, and $15,000 in the expanded "
                        "$75,000 plan. Do not treat this reserve as acquisition "
                        "funding twice."
                    ),
                ),
            ],
        ),
        (
            "diag-08-thirty-day-evidence-sprint",
            "timeline_roadmap",
            "The First 30 Days Build Evidence, Not Assumed Royalty Income",
            "Four weekly milestones prepare a disciplined licensing pipeline.",
            12,
            "operating_framework",
            (
                "Numeric values are milestone ending days. Deliverables are "
                "30-day operating targets, not executed-license forecasts. "
                "First-deal planning remains 4–14 months; the sprint does "
                "not change the canonical revenue or staffing scenarios."
            ),
            (
                "Finish the month with a rights dossier, tested use cases, "
                "a draft term structure, and a working reporting rehearsal."
            ),
            [
                (
                    "Days 1-7",
                    "Complete one asset dossier and rights-exception register",
                    7,
                    (
                        "Inventory ownership documents, licensed territories, "
                        "asset identifiers, and existing grants. Assign every "
                        "unresolved title or permission question to counsel."
                    ),
                ),
                (
                    "Days 8-14",
                    "Screen twenty accounts and seek five buyer interviews",
                    14,
                    (
                        "Rank accounts by concrete use case and ability to "
                        "report usage. Record actual interview outcomes; unanswered "
                        "outreach does not count as validated demand."
                    ),
                ),
                (
                    "Days 15-21",
                    "Draft one scoped offer and royalty calculation schedule",
                    21,
                    (
                        "Define minimum guarantees, royalty deductions, permitted "
                        "uses, audit rights, and quality controls. Run the four "
                        "pre-flight checks before circulating commercial commitments."
                    ),
                ),
                (
                    "Days 22-30",
                    "Rehearse reporting and establish the next development cycle",
                    30,
                    (
                        "Load synthetic royalty records into SQLite, reconcile "
                        "one sample invoice, and test renewal reminders. Review "
                        "buyer evidence and cash runway before further spending."
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
