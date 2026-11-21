from __future__ import annotations

VOLUME_015_SUBTITLE = (
    "The Complete Playbook for Judgment Recovery: "
    "$60,000–$500,000 USD in Annual Service Fees, "
    "from a 1 FT + 3 C (4 People) Pod to a Six-Person Team"
)

VOLUME_015_POSITIONING_ALTERNATIVES = [
    {
        "title": "The Commercial Judgment Recovery Desk",
        "subtitle": (
            "Build a four-person recovery pod around enforceable judgments, "
            "documented authority, lawful asset research, and counsel-led execution."
        ),
        "audience": (
            "Commercial recovery operators serving business creditors with entered "
            "money judgments and sufficient records to establish enforcement authority."
        ),
        "research_basis": (
            "Federal Rule of Civil Procedure 69 generally ties federal judgment "
            "execution to state procedure unless a federal statute applies. "
            "California Code of Civil Procedure section 683.020 illustrates why "
            "judgment age and applicable renewal rules belong in initial screening. "
            "A docket entry alone does not establish collectability."
        ),
        "sources": [
            "https://www.law.cornell.edu/rules/frcp/rule_69",
            "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CCP&sectionNum=683.020.",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "Priority Before Pursuit",
        "subtitle": (
            "Choose commercial enforcement files by reachable equity, competing "
            "claims, bankruptcy status, and the cost of the next lawful step."
        ),
        "audience": (
            "Attorney-supported recovery teams handling commercial judgments "
            "against businesses or guarantors with identifiable assets."
        ),
        "research_basis": (
            "11 U.S.C. section 362 establishes the automatic stay framework; "
            "11 U.S.C. section 522 addresses bankruptcy exemptions. UCC section "
            "9-317 supplies a model priority rule involving security interests "
            "and lien creditors, subject to its exceptions and state enactment. "
            "These authorities support asset-specific screening rather than "
            "equating judgment principal with realizable cash."
        ),
        "sources": [
            "https://www.law.cornell.edu/uscode/text/11/362",
            "https://www.law.cornell.edu/uscode/text/11/522",
            "https://www.law.cornell.edu/ucc/9/9-317",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Recovery Fee Ledger",
        "subtitle": (
            "Turn collected judgment payments into traceable creditor remittances, "
            "earned service fees, and reconciled operator economics."
        ),
        "audience": (
            "Small recovery firms and creditor-service teams that need reliable "
            "payment allocation, deadline ownership, and commercial-file classification."
        ),
        "research_basis": (
            "15 U.S.C. section 1692a defines covered debt by its primarily personal, "
            "family, or household purpose; commercial labeling alone is insufficient. "
            "12 CFR section 1006.38 supplies validation requirements where Regulation F "
            "applies. 15 U.S.C. section 1681b limits consumer-report access to permissible "
            "purposes. These rules support documented classification and controlled "
            "research, while fee recognition follows the actual service agreement "
            "and applicable accounting treatment."
        ),
        "sources": [
            "https://www.law.cornell.edu/uscode/text/15/1692a",
            "https://www.ecfr.gov/current/title-12/chapter-X/part-1006/section-1006.38",
            "https://www.law.cornell.edu/uscode/text/15/1681b",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
]


def build_volume_015_diagrams_data() -> list[dict]:
    specs = [
        (
            "diag-01-commercial-judgment-workflow",
            "process_flow",
            "From Entered Judgment to Earned Service Fee",
            "Five controlled handoffs separate enforcement authority from collected cash.",
            1,
            "operating_framework",
            (
                "Designed for commercial post-judgment recovery. State procedure, "
                "licensing, representation requirements, and the service agreement "
                "determine permitted activity. Assignment does not automatically "
                "authorize a nonlawyer to represent another party."
            ),
            (
                "Court deadlines and payment reconciliation can be automated; "
                "legal conclusions and enforcement selections remain assigned "
                "to qualified people."
            ),
            [
                (
                    "Screen the docket",
                    "Confirm entry, parties, balance, age, and enforceability before outreach",
                    1.0,
                    (
                        "Use PACER for federal matters and the relevant state court "
                        "portal for state judgments. Obtain the judgment and subsequent "
                        "orders; record appeals, stays, service issues, payments, "
                        "and renewal deadlines with source-document links."
                    ),
                ),
                (
                    "Establish lawful authority",
                    "Document creditor instructions, assignment scope, and counsel responsibilities",
                    2.0,
                    (
                        "Verify the creditor and any assignment chain. Execute a "
                        "service agreement defining fees, expense responsibility, "
                        "remittance timing, and termination. Confirm required licenses "
                        "and use counsel for reserved legal work."
                    ),
                ),
                (
                    "Map reachable equity",
                    "Identify assets, competing liens, exemptions, and current bankruptcy exposure",
                    3.0,
                    (
                        "Search authorized court, recorder, and Secretary of State "
                        "records. Distinguish ownership from possession, subtract "
                        "senior claims, and record data provenance. Do not purchase "
                        "a consumer report without a documented permissible purpose."
                    ),
                ),
                (
                    "Select the recovery route",
                    "Compare voluntary payment against counsel-directed execution costs and timing",
                    4.0,
                    (
                        "Prepare an asset-specific cost estimate and settlement "
                        "authority limits. Federal Rule of Civil Procedure 69 "
                        "generally uses state execution procedure. Calendar each "
                        "required notice, writ, service event, and response deadline."
                    ),
                ),
                (
                    "Reconcile and remit",
                    "Allocate cleared receipts, earned fees, expenses, and creditor remittances",
                    5.0,
                    (
                        "Match bank transactions to the matter ledger, investigate "
                        "returns, and follow applicable client-fund handling rules. "
                        "Recognize only earned operator service fees as revenue; "
                        "track satisfaction filings and remaining balances."
                    ),
                ),
            ],
        ),
        (
            "diag-02-mature-commercial-recovery-funnel",
            "funnel",
            "A Mature Cohort Supporting the Base Case",
            "Five nested stages connect screening discipline to $280,000 in annual service fees.",
            6,
            "illustrative_model",
            (
                "Illustrative mature annual cohort, not an observed conversion "
                "benchmark or a launch-year forecast. Counts are nested: "
                "500 >= 200 >= 100 >= 40 >= 20. Each stage is a subset of "
                "the preceding stage. First-deal planning remains 6–24 months."
            ),
            (
                "Twenty collecting matters averaging $14,000 in earned fees "
                "produce $280,000 recognized revenue. At an assumed 25% fee, "
                "$1,120,000 collected for creditors underlies that revenue."
            ),
            [
                (
                    "Screened judgment records",
                    "500 commercial judgment records receive initial document-based screening",
                    500.0,
                    (
                        "Starting cohort equals 100% of screened records. Record "
                        "court identifiers, judgment dates, creditor authority, "
                        "balances, and review dates without treating face value "
                        "as operator revenue."
                    ),
                ),
                (
                    "Qualified commercial files",
                    "200 records satisfy documented authority, scope, and enforceability criteria",
                    200.0,
                    (
                        "Forty percent of screened records survive initial review. "
                        "Exclude files with unresolved authority, expired enforcement "
                        "rights, unaddressed stays, or activity outside permitted scope."
                    ),
                ),
                (
                    "Creditor engagements",
                    "100 qualified files become signed, document-complete creditor engagements",
                    100.0,
                    (
                        "Fifty percent of qualified files convert to engagements. "
                        "Each has fee terms, expense limits, communications authority, "
                        "and a defined attorney role where required."
                    ),
                ),
                (
                    "Actionable asset cases",
                    "40 engaged files support economically justified, lawful recovery action",
                    40.0,
                    (
                        "Forty percent of engagements show a reachable asset or "
                        "credible voluntary-payment route after priority, exemption, "
                        "bankruptcy, and cost review."
                    ),
                ),
                (
                    "Collecting matters",
                    "20 actionable matters generate cleared receipts and earned service fees",
                    20.0,
                    (
                        "Fifty percent of actionable cases collect within the "
                        "modeled annual measurement window: 4% of initial records. "
                        "Average collections of $56,000 per collecting matter "
                        "at 25% yield $14,000 in recognized fees."
                    ),
                ),
            ],
        ),
        (
            "diag-03-base-case-fee-to-owner-profit",
            "waterfall",
            "Base Case: $280,000 Fees to $84,000 Owner Net",
            "Four expense deductions reconcile exactly to a 30.0% annual net margin.",
            3,
            "illustrative_model",
            (
                "Annual USD. First and last bars are absolute totals; intervening "
                "bars are signed deductions. Expense allocation is illustrative; "
                "the canonical totals are $280,000 revenue, $196,000 expenses, "
                "and $84,000 owner net. Owner labor is supported by the residual "
                "rather than a second salary deduction."
            ),
            (
                "$280,000 - $100,000 - $48,000 - $24,000 - $24,000 = $84,000; "
                "$84,000 / $280,000 = 30.0%. Client principal and creditor "
                "remittances never enter the revenue bar."
            ),
            [
                (
                    "Recognized service fees",
                    "Annual earned operator fee revenue totals exactly $280,000",
                    280000.0,
                    (
                        "Opening total equals the canonical Base-Case revenue. "
                        "Illustrative collections of $1,120,000 at a 25% service "
                        "fee generate $280,000; the remaining creditor allocation "
                        "is not operator revenue or an operator expense."
                    ),
                ),
                (
                    "Contract delivery labor",
                    "Deduct $100,000 for nonowner research and recovery-administration delivery",
                    -100000.0,
                    (
                        "Illustrative file-linked contractor expense covers research "
                        "and administrative delivery, excluding separately budgeted "
                        "outside counsel. Remaining contribution equals $180,000."
                    ),
                ),
                (
                    "Counsel and enforcement",
                    "Deduct $48,000 for operator-borne legal work and execution expenses",
                    -48000.0,
                    (
                        "Include only costs contractually borne by the operator. "
                        "Do not duplicate creditor-funded advances as operator "
                        "expenses. Remaining contribution equals $132,000."
                    ),
                ),
                (
                    "Research and systems",
                    "Deduct $24,000 for lawful data, docket monitoring, and reconciliation systems",
                    -24000.0,
                    (
                        "Illustrative recurring allocation equals $2,000 monthly. "
                        "Maintain access permissions, source records, matter-level "
                        "audit trails, and deadline alerts. Remaining contribution "
                        "equals $108,000."
                    ),
                ),
                (
                    "Operating overhead",
                    "Deduct $24,000 for insurance, bookkeeping, administration, and business overhead",
                    -24000.0,
                    (
                        "Illustrative recurring allocation equals $2,000 monthly. "
                        "Combined recurring systems and overhead equal $4,000 "
                        "monthly, inside the $2,000–$12,000 planning range. "
                        "File-linked delivery and enforcement costs remain additional."
                    ),
                ),
                (
                    "Annual owner net",
                    "Closing annual owner net profit equals exactly $84,000",
                    84000.0,
                    (
                        "Closing total is not another cash inflow. The four-person "
                        "Base pod is 1 FT + 3 C. Canonical comparison: Conservative "
                        "$60,000 at 20% yields $12,000 with 1 FT + 3 C; "
                        "Scaled $500,000 at 40% yields $200,000 with 2 FT + 4 C."
                    ),
                ),
            ],
        ),
        (
            "diag-04-commercial-subniche-fee-yields",
            "horizontal_bars",
            "Five Commercial File Types, One Common Collection Base",
            "Compare illustrative service-fee yield per $100,000 actually recovered.",
            2,
            "illustrative_model",
            (
                "All five bars assume $100,000 in cleared recoveries and show "
                "gross operator fee yield before expenses. Rates are editorial "
                "pricing hypotheses, not observed market rates or recovery "
                "probabilities. Bars are alternatives, not additive revenue."
            ),
            (
                "Use a common recovered-dollar denominator to compare pricing. "
                "Neither the debtor's asset value nor the judgment balance "
                "establishes earned revenue."
            ),
            [
                (
                    "Document-complete supplier judgments",
                    "$100,000 recovered at 20% produces $20,000 service-fee revenue",
                    20000.0,
                    (
                        "Assume an entered trade-credit judgment and voluntary "
                        "payment using bank-supported business ACH or wire transfer. "
                        "Confirm payment authority, return exposure, and ledger "
                        "allocation; a convenient rail does not improve lien priority."
                    ),
                ),
                (
                    "Equipment lease deficiency judgments",
                    "$100,000 recovered at 25% produces $25,000 service-fee revenue",
                    25000.0,
                    (
                        "Assume a valid commercial deficiency judgment after "
                        "credited disposition proceeds. Counsel reviews remaining "
                        "liability and secured claims before selecting a recovery "
                        "route; prevent double recovery."
                    ),
                ),
                (
                    "Commercial premises rent judgments",
                    "$100,000 recovered at 25% produces $25,000 service-fee revenue",
                    25000.0,
                    (
                        "Confirm the named tenant entity, judgment scope, credited "
                        "deposits, and any adjudicated guarantor liability. Separate "
                        "commercial obligations from household-purpose debts and "
                        "verify assets belong to an actual judgment debtor."
                    ),
                ),
                (
                    "Adjudicated business guarantor obligations",
                    "$100,000 recovered at 30% produces $30,000 service-fee revenue",
                    30000.0,
                    (
                        "Assume judgment already reaches the guarantor. Classify "
                        "the underlying obligation by purpose, not the person's "
                        "name; counsel evaluates ownership, exemptions, and "
                        "available execution procedure."
                    ),
                ),
                (
                    "Lien-constrained commercial judgments",
                    "$100,000 recovered at 35% produces $35,000 service-fee revenue",
                    35000.0,
                    (
                        "Higher assumed pricing reflects more intensive priority "
                        "and asset analysis, not superior collectability. Senior "
                        "claims can eliminate reachable equity; decline further "
                        "spend when incremental recovery economics fail."
                    ),
                ),
            ],
        ),
        (
            "diag-05-preflight-authority-and-recoverability",
            "decision_tree",
            "Four Checks Before Enforcement Spend",
            "Proceed only on documented facts; route unresolved issues to the responsible specialist.",
            5,
            "operating_framework",
            (
                "Read nodes in order. A supported answer advances to the next "
                "check; an unresolved or adverse answer follows the stated "
                "hold, referral, or decline path. These are jurisdiction-specific "
                "reviews, not universal procedural instructions."
            ),
            (
                "A valid judgment can still be uneconomic or temporarily "
                "unenforceable. Verify authority, lawful scope, bankruptcy "
                "constraints, and net reachable value before spending."
            ),
            [
                (
                    "Authority and judgment life",
                    "Proceed with verified enforcement rights; otherwise hold for counsel review",
                    1.0,
                    (
                        "Match creditor identity, assignment documents, judgment "
                        "terms, payments, appeal status, and renewal deadlines. "
                        "California CCP section 683.020 illustrates the ten-year "
                        "enforcement limit absent applicable renewal or exception. "
                        "Federal Rule 69 generally points execution to state procedure."
                    ),
                ),
                (
                    "Licensing, debt purpose, and data",
                    "Proceed within authorized scope; otherwise suspend affected research or contact",
                    2.0,
                    (
                        "Check applicable state and local collection licensing "
                        "even for commercial files. Apply the purpose-based debt "
                        "definition in 15 U.S.C. section 1692a and Regulation F "
                        "where covered. Document any consumer-report permissible "
                        "purpose under 15 U.S.C. section 1681b; judgment status "
                        "alone does not supply one."
                    ),
                ),
                (
                    "Bankruptcy and protected property",
                    "Proceed only with resolved stay exposure and an asset-specific exemption analysis",
                    3.0,
                    (
                        "Refresh bankruptcy screening before enforcement. A "
                        "potentially applicable 11 U.S.C. section 362 stay stops "
                        "affected action pending counsel's determination or court "
                        "relief. Review discharge effects under section 524, "
                        "bankruptcy exemptions under section 522, and applicable "
                        "state execution exemptions."
                    ),
                ),
                (
                    "Priority and incremental economics",
                    "Proceed on positive expected contribution; otherwise defer or decline spending",
                    4.0,
                    (
                        "Verify liens, perfection, timing, ownership, and likely "
                        "sale or collection costs. State-enacted UCC section 9-317 "
                        "may affect lien-creditor priority. An illustrative 40% "
                        "chance of collecting $50,000 at a 25% fee produces "
                        "$5,000 expected fees; subtracting $6,000 incremental "
                        "operator costs produces a $1,000 expected loss."
                    ),
                ),
            ],
        ),
        (
            "diag-06-four-to-six-person-recovery-pod",
            "org_architecture",
            "A Four-Person Base Pod, Expanded to Six",
            "One owner, three contractors, and two clearly triggered expansion seats.",
            11,
            "operating_framework",
            (
                "Each node represents one person, not one full-time equivalent. "
                "Conservative and Base activate the first four seats: 1 FT + 3 C. "
                "Scaled activates all six: 2 FT + 4 C. Contractor hours and "
                "assignments vary with authorized workload."
            ),
            (
                "The owner coordinates economics and client delivery; retained "
                "counsel controls legal work within the agreed representation. "
                "Separate payment preparation from release wherever feasible."
            ),
            [
                (
                    "Owner and portfolio lead",
                    "One full-time owner leads intake, pricing, prioritization, and client accountability",
                    1.0,
                    (
                        "Active in every scenario. Own engagement terms, spending "
                        "limits, fee forecasts, and exception resolution. Review "
                        "prepared remittances against bank evidence and matter "
                        "ledgers; owner net is the scenario's residual profit."
                    ),
                ),
                (
                    "Lawful research contractor",
                    "One contractor documents assets, docket facts, ownership, and competing claims",
                    1.0,
                    (
                        "Active in every scenario. Use permitted public records "
                        "and authorized databases, preserve source links, flag "
                        "stale evidence, and escalate ambiguous identity matches. "
                        "Do not select legal remedies or exceed data permissions."
                    ),
                ),
                (
                    "Retained enforcement attorney",
                    "One contractor handles legal analysis, filings, and court-facing enforcement work",
                    1.0,
                    (
                        "Active in every scenario, subject to the actual engagement "
                        "and required jurisdictional qualifications. Determine the "
                        "client and representation scope, evaluate stays and "
                        "exemptions, and perform reserved legal work independently."
                    ),
                ),
                (
                    "Case and payment administrator",
                    "One contractor maintains deadlines, document completeness, and receipt reconciliation",
                    1.0,
                    (
                        "Active in every scenario. Maintain a shared matter "
                        "register, monitor court notices, reconcile bank receipts, "
                        "prepare creditor statements, and escalate missed events. "
                        "Do not independently release funds that they prepared."
                    ),
                ),
                (
                    "Scaled operations lead",
                    "One additional full-time employee coordinates the expanded active-file workload",
                    1.0,
                    (
                        "Activate only in the Scaled six-person model. Own "
                        "capacity planning, document handoffs, aging reviews, "
                        "and operational quality checks while the owner retains "
                        "pricing and portfolio accountability."
                    ),
                ),
                (
                    "Scaled data and quality contractor",
                    "One additional contractor tests automation and independently reviews matter records",
                    1.0,
                    (
                        "Activate only in the Scaled six-person model. Test "
                        "deadline calculations against court rules, inspect "
                        "duplicate payments and access logs, and sample lien "
                        "evidence without replacing attorney review."
                    ),
                ),
            ],
        ),
        (
            "diag-07-startup-capital-allocation",
            "stacked_comparison",
            "Allocate Startup Cash Before Expanding the File Book",
            "Four buckets support $10,000, $30,000, and $75,000 illustrative capital plans.",
            4,
            "illustrative_model",
            (
                "Numeric values encode the $30,000 central planning stack. "
                "Bucket details also provide the $10,000 and $75,000 alternatives. "
                "Capital plans are separate from the canonical operating scenarios; "
                "startup cash is not recognized revenue or automatic annual expense."
            ),
            (
                "Central allocation: $6,000 + $9,000 + $12,000 + $3,000 = $30,000. "
                "Alternative stacks total exactly $10,000 and $75,000. "
                "A 6–24 month first-deal window requires separate runway planning."
            ),
            [
                (
                    "Formation and operating readiness",
                    "Reserve $6,000 centrally for licensing review, insurance, and engagement infrastructure",
                    6000.0,
                    (
                        "Allocate $2,000 in the $10,000 plan and $15,000 in the "
                        "$75,000 plan: 20% throughout. Budget jurisdiction-specific "
                        "license and bond costs where required, insurance, entity "
                        "setup, and counsel-reviewed service documents."
                    ),
                ),
                (
                    "Research and workflow systems",
                    "Reserve $9,000 centrally for lawful data access and dependable case systems",
                    9000.0,
                    (
                        "Allocate $3,000 in the $10,000 plan and $22,500 in the "
                        "$75,000 plan: 30% throughout. Fund authorized record "
                        "retrieval, docket tracking, secure document storage, "
                        "access controls, and payment-ledger setup."
                    ),
                ),
                (
                    "Enforcement working cash",
                    "Reserve $12,000 centrally for approved operator-borne file costs and delivery",
                    12000.0,
                    (
                        "Allocate $4,000 in the $10,000 plan and $30,000 in the "
                        "$75,000 plan: 40% throughout. Release cash against "
                        "matter-level budgets for counsel, filing, service, "
                        "and contractor delivery. Track creditor advances separately."
                    ),
                ),
                (
                    "Liquidity and error reserve",
                    "Reserve $3,000 centrally for payment interruptions, corrections, and operating contingencies",
                    3000.0,
                    (
                        "Allocate $1,000 in the $10,000 plan and $7,500 in the "
                        "$75,000 plan: 10% throughout. This is not full launch "
                        "runway: 6 months at $2,000 monthly consumes $12,000, "
                        "while 24 months at $12,000 consumes $288,000."
                    ),
                ),
            ],
        ),
        (
            "diag-08-thirty-day-commercial-recovery-launch",
            "timeline_roadmap",
            "Thirty Days to an Auditable Recovery Operation",
            "Four weekly milestones establish readiness without assuming first-month collections.",
            12,
            "operating_framework",
            (
                "The sprint establishes operating capability, not a collection "
                "deadline. Canonical time to first deal remains 6–24 months. "
                "Training files and synthetic payment records stay separate "
                "from authorized live matters."
            ),
            (
                "Finish the month with documented scope, a screened file queue, "
                "tested controls, and a funded operating plan. Do not book "
                "judgment principal, prospective recoveries, or unsigned fees as revenue."
            ),
            [
                (
                    "Days 1-7",
                    "Define jurisdiction, commercial scope, representation roles, and operating economics",
                    7.0,
                    (
                        "Select one initial jurisdiction and commercial file type. "
                        "Document licensing research, counsel responsibilities, "
                        "lawful data sources, fee terms, and expense ownership. "
                        "Load canonical revenue, margin, and staffing scenarios "
                        "into a spreadsheet without changing their totals."
                    ),
                ),
                (
                    "Days 8-14",
                    "Build the source-linked screening register and test deadline ownership",
                    14.0,
                    (
                        "Review 25 lawfully accessible judgment records as an "
                        "internal process sample, not a sales forecast. Capture "
                        "entry dates, balances, authority evidence, relevant "
                        "orders, and review decisions. Have counsel verify "
                        "jurisdiction-specific deadline logic."
                    ),
                ),
                (
                    "Days 15-21",
                    "Exercise bankruptcy checks, priority review, and payment-allocation controls",
                    21.0,
                    (
                        "Run five training cases through the four pre-flight "
                        "checks. Test synthetic partial payments, duplicate "
                        "receipts, reversals, creditor advances, and fee splits. "
                        "Confirm that deadline alerts reach a named owner and "
                        "that system failures produce visible exceptions."
                    ),
                ),
                (
                    "Days 22-30",
                    "Launch bounded creditor outreach and review readiness, capacity, and runway",
                    30.0,
                    (
                        "Contact an initial list of ten prospective commercial "
                        "creditor organizations using permitted business channels. "
                        "Accept live work only within established authority and "
                        "capacity. Review cash runway, contractor commitments, "
                        "record completeness, and unresolved legal questions "
                        "before committing matter-specific expenditure."
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
