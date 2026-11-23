from __future__ import annotations

VOLUME_048_SUBTITLE = (
    "The Complete Playbook for Forensic Whistleblower Analytics: "
    "$95,000–$880,000 USD Annual Operator Revenue, "
    "a 1 FT + 2 C Core Pod (3 People), and a 5-Person Scaled Team"
)

VOLUME_048_POSITIONING_ALTERNATIVES = [
    {
        "title": "The Retainer-First Relator Intelligence Desk",
        "subtitle": (
            "Sell evidence-grade forensic analytics to relator counsel; "
            "keep contingent recoveries outside operating cash budgets."
        ),
        "audience": (
            "Healthcare analysts and forensic accountants serving plaintiff law "
            "firms through scoped, paid litigation-support engagements."
        ),
        "research_basis": (
            "CMS utilization and Open Payments datasets support anomaly discovery, "
            "not proof of a false claim. Counsel must assess the public-disclosure "
            "bar under 31 U.S.C. § 3730(e)(4), original-source eligibility, and "
            "Rule 9(b) particularity before developing a filing strategy. "
            "Commercial retainers compensate documented services rather than "
            "purchasing a relator position or a percentage of counsel fees."
        ),
        "sources": [
            "https://data.cms.gov/",
            "https://openpaymentsdata.cms.gov/",
            "https://www.law.cornell.edu/uscode/text/31/3730",
            "https://www.law.cornell.edu/rules/frcp/rule_9",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Securities and Tax Evidence Laboratory",
        "subtitle": (
            "Build counsel-directed SEC and IRS evidence packages while "
            "funding the team through recurring analytical service contracts."
        ),
        "audience": (
            "Securities-data specialists and tax forensic practitioners with "
            "lawful records access and established counsel relationships."
        ),
        "research_basis": (
            "SEC awards generally range from 10%–30% of qualifying monetary "
            "sanctions collected when the covered action exceeds $1 million, "
            "subject to eligibility and procedural requirements. IRS mandatory "
            "awards generally range from 15%–30% of collected proceeds under "
            "26 U.S.C. § 7623(b), subject to its thresholds and exceptions. "
            "Public-record analysis alone does not establish award eligibility; "
            "counsel evaluates original information, exclusions, and timing."
        ),
        "sources": [
            "https://www.law.cornell.edu/uscode/text/15/78u-6",
            "https://www.law.cornell.edu/cfr/text/17/240.21F-4",
            "https://www.sec.gov/whistleblower",
            "https://www.law.cornell.edu/uscode/text/26/7623",
            "https://www.irs.gov/compliance/whistleblower-office",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Procurement and Customs Claim Reconstruction Studio",
        "subtitle": (
            "Convert lawful procurement and shipment signals into "
            "traceable, counsel-tested claim reconstruction."
        ),
        "audience": (
            "Procurement investigators and customs-data analysts selling "
            "fixed-scope research and recurring support to relator law firms."
        ),
        "research_basis": (
            "SAM.gov records, authorized shipment datasets, and primary-source "
            "corroboration can identify mismatches worth investigating. "
            "A pricing anomaly or shipment discrepancy does not itself establish "
            "FCA falsity, materiality, scienter, or a qualifying payment claim. "
            "Counsel tests 31 U.S.C. § 3729 elements and public-disclosure "
            "constraints before any sealed complaint."
        ),
        "sources": [
            "https://sam.gov/",
            "https://www.cbp.gov/trade",
            "https://www.law.cornell.edu/uscode/text/31/3729",
            "https://www.law.cornell.edu/uscode/text/31/3730",
            "https://www.law.cornell.edu/rules/frcp/rule_9",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
]


def build_volume_048_diagrams_data() -> list[dict]:
    specs = [
        (
            "diag-01-evidence-to-paid-support",
            "process_flow",
            "Build Evidence, Sell Support, Separate Award Exposure",
            "Five operating stages from lawful public signals to paid counsel work",
            1,
            "operating_framework",
            (
                "Public anomalies are research leads rather than established "
                "violations. Retainers pay for defined analytical services. "
                "An analyst does not acquire statutory claimant eligibility "
                "merely by preparing a dossier for someone else."
            ),
            (
                "Use Python sqlite3, hashlib, and csv for reproducible research; "
                "preserve source provenance before transforming records. "
                "Only licensed relator counsel files an FCA complaint under "
                "31 U.S.C. § 3730(b)(2). Route SEC Form TCR and IRS Form 211 "
                "submissions through counsel as an operating requirement."
            ),
            [
                (
                    "Acquire Lawful Records",
                    "Step 1: document source and access authority",
                    1.0,
                    (
                        "Collect CMS Part B/D, Open Payments, SAM.gov, and "
                        "lawfully obtained import-manifest records. Record "
                        "publication dates, source URLs, permitted uses, and "
                        "SHA-256 hashes; exclude improperly acquired records."
                    ),
                ),
                (
                    "Rank Explainable Signals",
                    "Step 2: normalize before scoring anomalies",
                    2.0,
                    (
                        "Normalize specialties, geography, utilization, coding "
                        "changes, contract modifications, and shipment units. "
                        "Use peer-adjusted comparisons and negative controls; "
                        "an outlier without context is not a fraud conclusion."
                    ),
                ),
                (
                    "Corroborate Claim Elements",
                    "Step 3: tie allegations to primary evidence",
                    3.0,
                    (
                        "Build a claim ledger linking dates, actors, amounts, "
                        "government payment requests, and supporting records. "
                        "Track FOIA provenance and disclosure history; public "
                        "FOIA material can affect public-disclosure analysis."
                    ),
                ),
                (
                    "Contract Counsel Support",
                    "Step 4: bill defined forensic deliverables",
                    4.0,
                    (
                        "Use paid scopes for reproducible notebooks, claim "
                        "reconstruction, exhibits, and ongoing analytical "
                        "support. Invoice service milestones independently "
                        "of litigation outcomes and preserve conflict checks."
                    ),
                ),
                (
                    "Segregate Contingent Outcomes",
                    "Step 5: restrict sealed materials and award ledgers",
                    5.0,
                    (
                        "Counsel controls filing, service, court orders, and "
                        "permitted disclosure. Maintain least-privilege matter "
                        "workspaces. Carry potential awards at zero in operating "
                        "cash budgets until actual eligible proceeds arrive."
                    ),
                ),
            ],
        ),
        (
            "diag-02-nested-retainer-conversion",
            "funnel",
            "A Screening Funnel, Not an Award Forecast",
            "Nested illustrative cohorts end in paid firm-matter engagements",
            6,
            "illustrative_model",
            (
                "Synthetic mature-year cohort, not measured conversion history. "
                "All stages count distinct firm-matter opportunities, each "
                "anchored to an initial signal; later stages are subsets of "
                "earlier stages. Five engagements belong to five separate firms. "
                "No conversion stage represents an agency recovery probability."
            ),
            (
                "Sequential conversion is 18.0%, 33.3%, 30.0%, and 27.8%; "
                "overall conversion is 0.5%. Annual engagement fees of "
                "$60,000, $75,000, $90,000, $112,500, and $150,000 total "
                "$487,500. This is a mature annual service model, not a "
                "30-day sales promise; first deal timing is 4–12 months."
            ),
            [
                (
                    "Screened Opportunities",
                    "1,000 distinct signal-linked firm-matter opportunities",
                    1000.0,
                    (
                        "Deduplicate related entities and repeated anomalies "
                        "before counting opportunities. Record one candidate "
                        "firm and one traceable matter hypothesis per entry."
                    ),
                ),
                (
                    "Corroborated Opportunities",
                    "180 retained; 18.0% of initial cohort",
                    180.0,
                    (
                        "Retain only opportunities with independent corroboration "
                        "and a plausible payment, securities, or tax nexus. "
                        "Reject stale identifiers and ordinary coding variation."
                    ),
                ),
                (
                    "Counsel-Screened Opportunities",
                    "60 retained; 33.3% of preceding cohort",
                    60.0,
                    (
                        "Counsel assesses conflicts, public disclosure, source "
                        "eligibility, and evidence specificity. This screen "
                        "does not establish liability or entitlement to payment."
                    ),
                ),
                (
                    "Scoped Support Proposals",
                    "18 retained; 30.0% of preceding cohort",
                    18.0,
                    (
                        "Prepare priced analytical scopes with acceptance "
                        "criteria, lawful access boundaries, named deliverables, "
                        "payment schedules, and segregated matter permissions."
                    ),
                ),
                (
                    "Paid Retainer Engagements",
                    "5 retained; 27.8% of preceding cohort",
                    5.0,
                    (
                        "Execute five distinct annual service engagements. "
                        "Track invoices and collections separately from "
                        "contingent filings; no award proceeds fund payroll."
                    ),
                ),
            ],
        ),
        (
            "diag-03-base-case-owner-profit",
            "waterfall",
            "Base Case: $487,500 Revenue to $219,375 Owner Profit",
            "Six bars reconcile the canonical 45.0% annual net margin",
            3,
            "illustrative_model",
            (
                "Formula v2.0 scenario totals are fixed; expense categories "
                "below are an illustrative reconciliation rather than supplied "
                "historical accounts. Base revenue is entirely earned B2B "
                "service fees, with $0 contingent awards. Positive endpoints "
                "are totals; the four negative bars are expense movements. "
                "Do not add the final total to the preceding movements."
            ),
            (
                "Conservative: $95,000 revenue less $64,600 costs equals "
                "$30,400 owner profit at 32%, with 1 FT + 2 C. "
                "Base: $487,500 less $268,125 equals $219,375 at 45.0%, "
                "with 1 FT + 2 C. Scaled: $880,000 less $369,600 equals "
                "$510,400 at 58%, with 2 FT + 3 C. All three scenarios "
                "can be modeled with zero award receipts. Government "
                "recoveries, sanctions, tax proceeds, and client funds "
                "are not operator revenue."
            ),
            [
                (
                    "Recognized Service Revenue",
                    "$487,500 annual earned operator service revenue",
                    487500.0,
                    (
                        "Five annual engagements supply the opening total. "
                        "Recognize services as earned and track cash collection "
                        "separately. Exclude agency recoveries and uncollected "
                        "claims; recognize only the operator's eligible retained "
                        "portion of any separately realized award."
                    ),
                ),
                (
                    "Delivery Labor",
                    "Subtract $165,000 annual delivery labor expense",
                    -165000.0,
                    (
                        "Illustrative allocation covers contracted analytical "
                        "delivery and non-owner delivery support. Residual "
                        "owner profit is owner compensation, not an additional "
                        "salary deduction; remaining contribution is $322,500."
                    ),
                ),
                (
                    "Evidence Infrastructure",
                    "Subtract $36,000 annual data and tooling expense",
                    -36000.0,
                    (
                        "Budget licensed datasets, secure matter storage, "
                        "reproducible processing, backup retention, and source "
                        "retrieval. Record subscription rights by project; "
                        "remaining contribution is $286,500."
                    ),
                ),
                (
                    "Specialist Matter Support",
                    "Subtract $42,000 annual specialist support expense",
                    -42000.0,
                    (
                        "Budget business-side specialist consultation and "
                        "external technical validation. Do not imply that "
                        "this purchases representation for every relator; "
                        "remaining contribution is $244,500."
                    ),
                ),
                (
                    "Operating Overhead",
                    "Subtract $25,125 annual operating overhead expense",
                    -25125.0,
                    (
                        "Allocate insurance, bookkeeping, secure communications, "
                        "business development, and administration. Total "
                        "deductions reach $268,125, leaving $219,375."
                    ),
                ),
                (
                    "Annual Owner Profit",
                    "$219,375 residual; exactly 45.0% net margin",
                    219375.0,
                    (
                        "Closing total equals $487,500 minus $268,125. "
                        "Non-delivery operating categories total $103,125 "
                        "annually, or $8,593.75 monthly, within the stated "
                        "$1,500–$9,500 operating range; total costs including "
                        "delivery labor average $22,343.75 monthly."
                    ),
                ),
            ],
        ),
        (
            "diag-04-service-rail-yield",
            "horizontal_bars",
            "Five Paid Research Niches Fund the Base Case",
            "Illustrative annual service-fee yield per distinct firm engagement",
            2,
            "illustrative_model",
            (
                "Bars represent annual operator service revenue in USD, not "
                "statutory award percentages, expected recoveries, or empirical "
                "market prices. Each niche contributes one distinct engagement "
                "to the five-engagement Base model; total revenue is $487,500."
            ),
            (
                "Price around reproducible evidence work and counsel demand. "
                "A payment rail determines the research problem, not automatic "
                "award eligibility. Invoice support services independently of "
                "whether counsel files a complaint or an agency takes action."
            ),
            [
                (
                    "CMS Part B/D Support",
                    "$60,000 annually; $5,000 monthly service equivalent",
                    60000.0,
                    (
                        "Reconcile provider identifiers, billing periods, "
                        "specialty cohorts, and payment records. Aggregate "
                        "utilization anomalies require claim-level corroboration "
                        "before supporting a particularized FCA allegation."
                    ),
                ),
                (
                    "Open Payments Corroboration",
                    "$75,000 annually; $6,250 monthly service equivalent",
                    75000.0,
                    (
                        "Resolve manufacturer, recipient, and payment identities "
                        "against relevant utilization records. A disclosed "
                        "payment does not itself prove an unlawful inducement "
                        "or a resulting false reimbursement claim."
                    ),
                ),
                (
                    "Procurement and Customs",
                    "$90,000 annually; $7,500 monthly service equivalent",
                    90000.0,
                    (
                        "Link procurement representations and authorized "
                        "shipment evidence to specific contracts or entries. "
                        "Test alternative explanations including amendments, "
                        "valuation methods, timing, and entity mismatches."
                    ),
                ),
                (
                    "SEC Evidence Analytics",
                    "$112,500 annually; $9,375 monthly service equivalent",
                    112500.0,
                    (
                        "Provide issuer-event reconstruction and original-analysis "
                        "support. Counsel evaluates 15 U.S.C. § 78u-6 and "
                        "17 CFR § 240.21F-4; SEC award percentages generally "
                        "run 10%–30%, not the FCA intervention schedule."
                    ),
                ),
                (
                    "IRS Evidence Analytics",
                    "$150,000 annually; $12,500 monthly service equivalent",
                    150000.0,
                    (
                        "Reconcile lawful records to tax periods and asserted "
                        "underpayments. Counsel tests 26 U.S.C. § 7623(b), "
                        "including amounts exceeding $2 million and, for "
                        "individual taxpayers, gross income exceeding $200,000 "
                        "in a qualifying taxable year."
                    ),
                ),
            ],
        ),
        (
            "diag-05-statutory-and-recovery-tree",
            "decision_tree",
            "Four Checks Before a Filing Strategy",
            "Separate source eligibility, claim detail, procedure, and recovery risk",
            5,
            "operating_framework",
            (
                "The renderer presents four sequential decision nodes; each "
                "detail states its proceed or stop branch. Numerical recovery "
                "parameters are sensitivity assumptions, not observed DOJ "
                "intervention or Granston-era dismissal rates. Agency and "
                "court outcomes require matter-specific assessment."
            ),
            (
                "FCA shares generally run 15%–25% after government intervention "
                "and 25%–30% without intervention, subject to statutory "
                "exceptions and reductions. SEC and CFTC generally use "
                "10%–30%; IRS § 7623(b) generally uses 15%–30%. "
                "No common 15%–30% rate should be applied across programs. "
                "Annual operating cash includes zero pending award value."
            ),
            [
                (
                    "Source Eligibility",
                    "Check 1: proceed only with defensible eligibility",
                    1.0,
                    (
                        "For FCA matters, counsel tests 31 U.S.C. "
                        "§ 3730(e)(4), qualifying public disclosures, and "
                        "original-source requirements; public-data mining "
                        "alone does not bypass the bar. If unresolved, stop "
                        "filing preparation and resolve the issue. Separately "
                        "test SEC or IRS eligibility under its own rules."
                    ),
                ),
                (
                    "Claim Particularity",
                    "Check 2: proceed with adequately supported allegations",
                    2.0,
                    (
                        "Counsel tests Rule 9(b), applicable circuit standards, "
                        "and 31 U.S.C. § 3729 elements. Build representative "
                        "claim links where required: who, what, when, where, "
                        "amount, payment request, and evidence. If specificity "
                        "fails, obtain lawful corroboration or stop."
                    ),
                ),
                (
                    "Seal and Submission Control",
                    "Check 3: proceed only through controlled counsel procedure",
                    3.0,
                    (
                        "FCA complaints remain sealed for at least 60 days "
                        "under § 3730(b)(2), with court-authorized extensions. "
                        "Do not serve the defendant before court direction. "
                        "Seal breaches can cause sanctions or dismissal, but "
                        "dismissal is not automatic. Restrict access; route "
                        "SEC TCR and IRS 211 separately through counsel."
                    ),
                ),
                (
                    "Zero-Recovery Stress Test",
                    "Check 4: fund operations without pending recoveries",
                    4.0,
                    (
                        "Illustrative FCA sensitivity uses intervention "
                        "i=20%, non-intervention=80%, dismissal conditional "
                        "on non-intervention d=25%, and positive collection "
                        "probabilities of 60% after intervention and 20% "
                        "after non-intervention survival. Collection "
                        "probability is i*0.60+(1-i)*(1-d)*0.20=24%; "
                        "zero collection is 76%. A severe case with both "
                        "collection probabilities at zero yields zero recovery. "
                        "Model government dismissal, including Granston-policy "
                        "risk, under § 3730(c)(2)(A); non-intervention itself "
                        "is not dismissal. Exclude all pending amounts from "
                        "operating cash regardless of modeled probability."
                    ),
                ),
            ],
        ),
        (
            "diag-06-core-and-scaled-pod",
            "org_architecture",
            "Three Core People, Five at Scale",
            "Core 1 FT + 2 C becomes 2 FT + 3 C without counting client counsel",
            11,
            "operating_framework",
            (
                "FT denotes a full-time seat; C denotes a contractor seat, "
                "not a full-time equivalent. Numeric value is one person per "
                "seat. The first three seats form the core pod; the final "
                "two activate only in the Scaled scenario. Client counsel "
                "is an external relationship, not an uncounted pod employee."
            ),
            (
                "Core staffing supports the $95,000 Conservative and $487,500 "
                "Base revenue scenarios. Five-person staffing supports the "
                "$880,000 Scaled scenario. Access follows assigned matters "
                "rather than seniority; client counsel retains filing and "
                "legal-strategy responsibility."
            ),
            [
                (
                    "Core Owner Operator",
                    "Core seat 1; one full-time operator",
                    1.0,
                    (
                        "Own client acquisition, engagement scope, billing, "
                        "delivery acceptance, and cash reserves. Separate "
                        "service invoices from contingent-award tracking and "
                        "escalate legal questions to retained counsel."
                    ),
                ),
                (
                    "Core Data Engineer",
                    "Core seat 2; one contracted engineer",
                    1.0,
                    (
                        "Build lawful ingestion, identifier resolution, "
                        "versioned transformations, hashing, and reproducible "
                        "anomaly rankings. Maintain source-to-exhibit lineage "
                        "and restrict access to assigned client matters."
                    ),
                ),
                (
                    "Core Forensic Analyst",
                    "Core seat 3; one contracted analyst",
                    1.0,
                    (
                        "Corroborate anomalies, maintain claim ledgers, test "
                        "benign explanations, and prepare evidence indexes. "
                        "Track conflicting facts rather than excluding "
                        "records that weaken the working hypothesis."
                    ),
                ),
                (
                    "Scaled Delivery Lead",
                    "Scaled seat 4; second full-time operator",
                    1.0,
                    (
                        "Coordinate parallel engagements, document acceptance "
                        "criteria, monitor service capacity, and audit source "
                        "lineage. Activate only when contracted service "
                        "revenue supports recurring delivery commitments."
                    ),
                ),
                (
                    "Scaled Specialist Analyst",
                    "Scaled seat 5; third contracted specialist",
                    1.0,
                    (
                        "Add healthcare coding, securities, customs, or tax "
                        "expertise against defined paid scopes. Limit "
                        "specialist access to relevant records and record "
                        "technical assumptions in each delivered exhibit."
                    ),
                ),
            ],
        ),
        (
            "diag-07-startup-capital-allocation",
            "stacked_comparison",
            "Allocate $30,000 Before Expanding the Pod",
            "Four capital buckets inside the $10,000–$45,000 startup range",
            4,
            "illustrative_model",
            (
                "Numeric values represent a $30,000 central startup plan. "
                "Each detail supplies matching lean and expanded allocations: "
                "lean totals $10,000; expanded totals $45,000. Startup capital "
                "is not additional recognized revenue or an automatic annual "
                "expense. Reserve balances become expenses only when spent "
                "on qualifying operating costs."
            ),
            (
                "Central allocation is $8,000 + $7,000 + $5,000 + $10,000 "
                "= $30,000. Monthly operating needs span $1,500–$9,500; "
                "a $10,000 cash reserve covers only about 1.1–6.7 months "
                "before delivery labor and other excluded commitments. "
                "With first deals taking 4–12 months, stage spending and "
                "secure additional runway rather than anticipating awards."
            ),
            [
                (
                    "Lawful Evidence Access",
                    "$8,000 central allocation; 26.7% of capital",
                    8000.0,
                    (
                        "Lean allocation is $2,000; expanded allocation is "
                        "$12,000. Purchase necessary dataset rights, limited "
                        "source retrieval, and targeted corroboration rather "
                        "than broad subscriptions without paid demand."
                    ),
                ),
                (
                    "Secure Research Environment",
                    "$7,000 central allocation; 23.3% of capital",
                    7000.0,
                    (
                        "Lean allocation is $2,000; expanded allocation is "
                        "$10,000. Fund encrypted endpoints, matter-level "
                        "permissions, backups, reproducible processing, and "
                        "access logging before sensitive materials arrive."
                    ),
                ),
                (
                    "Engagement and Quality Setup",
                    "$5,000 central allocation; 16.7% of capital",
                    5000.0,
                    (
                        "Lean allocation is $2,000; expanded allocation is "
                        "$8,000. Fund engagement documentation, initial "
                        "insurance costs, external technical checks, and "
                        "counsel-directed handling procedures for sensitive work."
                    ),
                ),
                (
                    "Uncommitted Cash Reserve",
                    "$10,000 central allocation; 33.3% of capital",
                    10000.0,
                    (
                        "Lean allocation is $4,000; expanded allocation is "
                        "$15,000. Keep liquidity available for delayed "
                        "collections and essential operating costs; do not "
                        "treat sealed matters as cash collateral."
                    ),
                ),
            ],
        ),
        (
            "diag-08-thirty-day-operating-sprint",
            "timeline_roadmap",
            "Thirty Days to a Counsel-Ready Research Operation",
            "Build a defensible paid-support capability, not a rushed complaint",
            12,
            "operating_framework",
            (
                "Numeric values are milestone end days. This sprint establishes "
                "operating readiness; it does not shorten the 4–12 month "
                "first-deal window or the illustrative 2–5+ year award horizon. "
                "FCA investigations may remain under extended seal for years; "
                "SEC and IRS submissions do not use the FCA complaint-seal "
                "procedure."
            ),
            (
                "Exit the sprint with one reproducible research package, "
                "a counsel-reviewed service scope, and a collection-aware "
                "cash plan. Recurring support revenue funds operations. "
                "Model every pending award as zero cash and stress a "
                "permanent zero-recovery outcome before adding fixed costs."
            ),
            [
                (
                    "Days 1–7",
                    "Milestone 1: establish scope and source controls",
                    7.0,
                    (
                        "Choose one niche and define a lawful data inventory. "
                        "Create source hashes, access permissions, entity "
                        "resolution rules, and a register of disclosure "
                        "dates. Draft specific analytical service deliverables."
                    ),
                ),
                (
                    "Days 8–14",
                    "Milestone 2: reproduce and challenge one signal",
                    14.0,
                    (
                        "Build a small SQLite evidence store and deterministic "
                        "transforms. Test one anomaly against matched peers "
                        "and benign explanations. Preserve failed hypotheses "
                        "and document missing claim-level evidence."
                    ),
                ),
                (
                    "Days 15–21",
                    "Milestone 3: obtain counsel-directed evidence assessment",
                    21.0,
                    (
                        "Arrange confidential counsel assessment of conflicts, "
                        "public disclosure, eligibility, particularity, and "
                        "handling restrictions. Define paid support scope; "
                        "do not circulate sealed or restricted material "
                        "as a marketing sample."
                    ),
                ),
                (
                    "Days 22–30",
                    "Milestone 4: prepare delivery and cash controls",
                    30.0,
                    (
                        "Finalize exhibit lineage, acceptance criteria, "
                        "invoice milestones, and access logs. Build a "
                        "13-week cash forecast with zero award receipts "
                        "and delayed retainer collections. Scale outreach "
                        "using sanitized methods demonstrations, not allegations."
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
