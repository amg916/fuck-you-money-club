from __future__ import annotations

VOLUME_023_SUBTITLE = (
    "The Complete Playbook for Mineral Rights: "
    "$30,000–$400,000 USD in Annual Revenue, "
    "Built from a 1 FT + 3 C Pod (4 People)"
)

VOLUME_023_POSITIONING_ALTERNATIVES = [
    {
        "title": "The Title-First Royalty Acquisition Desk",
        "subtitle": (
            "Underwrite producing oil and gas mineral interests through "
            "recorded ownership, lease economics, and reconciled royalty receipts."
        ),
        "audience": (
            "Capital-backed owner-operators building a four-person acquisition "
            "pod around producing mineral interests and nonparticipating royalties."
        ),
        "research_basis": (
            "Texas Property Code Sections 5.021 and 13.001 make conveyance "
            "formalities and recording consequences central diligence questions. "
            "Texas Natural Resources Code Section 91.402 supplies payment timing "
            "rules and specified grounds for withholding proceeds. These sources "
            "support an evidence-led acquisition process, not a valuation shortcut."
        ),
        "sources": [
            "https://statutes.capitol.texas.gov/Docs/PR/htm/PR.5.htm#5.021",
            "https://statutes.capitol.texas.gov/Docs/PR/htm/PR.13.htm#13.001",
            "https://statutes.capitol.texas.gov/Docs/NR/htm/NR.91.htm#91.402",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Pooling-Docket Acquisition Desk",
        "subtitle": (
            "Price acreage before public development milestones resolve, "
            "without treating a pooling application as a producing well."
        ),
        "audience": (
            "Basin-specialist buyers pairing a landman and petroleum engineer "
            "with patient acquisition capital and disciplined docket monitoring."
        ),
        "research_basis": (
            "State commission records establish the applicable pooling process, "
            "case status, and development evidence. Texas Natural Resources Code "
            "Chapter 102 governs a specific statutory pooling mechanism; it is "
            "not interchangeable with Oklahoma Corporation Commission practice. "
            "A filed application, issued order, permit, completed well, and paid "
            "royalty are separate underwriting events."
        ),
        "sources": [
            "https://statutes.capitol.texas.gov/Docs/NR/htm/NR.102.htm",
            "https://oklahoma.gov/occ/divisions/oil-gas.html",
            "https://www.rrc.texas.gov/oil-and-gas/",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Institutional Mineral Exit Desk",
        "subtitle": (
            "Assemble auditable title and production packages, then recognize "
            "rights-sale gains separately from returned acquisition basis."
        ),
        "audience": (
            "Experienced mineral buyers preparing institution-ready assets, "
            "with a six-person expansion reserved for demonstrated deal volume."
        ),
        "research_basis": (
            "15 U.S.C. Section 77b includes fractional undivided interests in "
            "oil, gas, or other mineral rights within the securities definition. "
            "Section 77e establishes registration requirements, subject to "
            "applicable exemptions. 26 U.S.C. Sections 611 and 613A make depletion "
            "treatment a separate asset-specific tax analysis rather than an "
            "automatic deduction from every sale or royalty payment."
        ),
        "sources": [
            "https://www.law.cornell.edu/uscode/text/15/77b",
            "https://www.law.cornell.edu/uscode/text/15/77e",
            "https://www.law.cornell.edu/uscode/text/26/611",
            "https://www.law.cornell.edu/uscode/text/26/613A",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
]


def build_volume_023_diagrams_data() -> list[dict]:
    specs = [
        (
            "diag-01-title-to-cash-workflow",
            "process_flow",
            "Buy the Interest, Verify the Decimal, Reconcile the Cash",
            "Five operating steps from recorded ownership to royalty receipts.",
            1,
            "operating_framework",
            (
                "Scope covers private oil and gas mineral interests and "
                "nonparticipating royalty interests. NMA means net mineral acres; "
                "NPRI means nonparticipating royalty interest. Instruments and "
                "state law control ownership, executive rights, and allocation. "
                "The typical first-deal window is 6–24 months."
            ),
            (
                "A tract description, an operator pay decimal, and a seller's "
                "acreage claim are different evidence objects. Reconcile them "
                "before pricing the interest."
            ),
            [
                (
                    "Define the acquired property interest precisely",
                    "Map tract, instrument, estate, and seller",
                    1.0,
                    (
                        "Record county, legal description, recording references, "
                        "seller vesting, and whether the asset conveys minerals, "
                        "a lease-dependent royalty, or an NPRI. Do not substitute "
                        "surface acreage for the severed mineral estate."
                    ),
                ),
                (
                    "Reconstruct title and calculate economic ownership",
                    "Resolve reservations before accepting ownership decimals",
                    2.0,
                    (
                        "Use county recorder instruments and a landman's run "
                        "sheet to trace conveyances, probate, liens, and "
                        "reservations. Calculate NMA from supported fractional "
                        "mineral ownership; read fixed and floating NPRI language "
                        "before applying any lease royalty multiplier."
                    ),
                ),
                (
                    "Underwrite production and development evidence separately",
                    "Stress price, decline, deductions, and timing",
                    3.0,
                    (
                        "Match operator statements to state well identifiers "
                        "and production records. Model realized commodity prices, "
                        "decline curves, post-production deductions, and downtime. "
                        "Treat undrilled locations and pooling-docket developments "
                        "as contingent cases rather than current royalty cash."
                    ),
                ),
                (
                    "Acquire through documented closing and recordation",
                    "Transfer verified rights with tracked basis",
                    4.0,
                    (
                        "Counsel verifies the conveyance and required releases; "
                        "the landman confirms recording and operator transfer "
                        "requirements. Track purchase basis and transaction costs "
                        "by interest, with cash release tied to documented "
                        "closing conditions."
                    ),
                ),
                (
                    "Reconcile royalties and package realized exits",
                    "Recognize royalties plus gains, excluding returned basis",
                    5.0,
                    (
                        "Use Python csv and sqlite3 to match statements, "
                        "production months, ownership decimals, deductions, and "
                        "bank deposits. Investigate suspense and missing payments; "
                        "for sales, separate returned carrying basis from realized "
                        "rights-trading gains."
                    ),
                ),
            ],
        ),
        (
            "diag-02-nested-acquisition-cohorts",
            "funnel",
            "Turn One Sourcing Cohort into Documented Acquisitions",
            "Five nested cohorts, with explicit denominators and no revenue claims.",
            6,
            "illustrative_model",
            (
                "Illustrative cohort contains 500 distinct seller-interest "
                "packages, deduplicated by owner, tract, and conveyed estate. "
                "Every later stage is a subset of the preceding stage. Counts "
                "are planning assumptions over a 6–24 month acquisition cycle, "
                "not observed conversions or a 30-day closing forecast."
            ),
            (
                "The cohort narrows 500 → 200 → 80 → 20 → 3. "
                "Final conversion is 0.6% of screened packages; acquisition "
                "count alone does not establish annual royalty revenue."
            ),
            [
                (
                    "Screen distinct seller and interest packages",
                    "500 packages enter the documented source cohort",
                    500.0,
                    (
                        "Capture owner contact provenance, county, legal "
                        "description, claimed estate, and asking price. Separate "
                        "duplicate broker listings from distinct interests before "
                        "calculating any downstream conversion rate."
                    ),
                ),
                (
                    "Confirm interest and obtain usable documents",
                    "200 packages qualify; 40% of screened cohort",
                    200.0,
                    (
                        "Obtain seller authority, relevant recorded instruments, "
                        "and permission to review statements when producing. "
                        "Exclude packages whose seller cannot identify the "
                        "conveyed estate or provide a workable document trail."
                    ),
                ),
                (
                    "Pass preliminary title and engineering review",
                    "80 packages survive; 40% of documented cohort",
                    80.0,
                    (
                        "Screen ownership defects, production decline, pricing "
                        "differentials, lease deductions, and development timing. "
                        "Record the specific failure reason for every rejected "
                        "package to improve subsequent sourcing."
                    ),
                ),
                (
                    "Issue supported and conditional purchase offers",
                    "20 packages receive offers; 25% of reviewed cohort",
                    20.0,
                    (
                        "Attach supported ownership math, price sensitivity, "
                        "diligence conditions, and a maximum cash commitment. "
                        "Do not bid contingent drilling upside as though an "
                        "operator has already scheduled first production."
                    ),
                ),
                (
                    "Close and complete recorded ownership transfers",
                    "3 packages close; 15% of offered cohort",
                    3.0,
                    (
                        "Count an acquisition only after executed closing "
                        "documents, required funds movement, and confirmed "
                        "recordation. Track operator pay-status updates "
                        "separately; closing does not establish immediate "
                        "royalty collection."
                    ),
                ),
            ],
        ),
        (
            "diag-03-base-case-owner-profit-waterfall",
            "waterfall",
            "Base Case: $215,000 Revenue to $69,875 Owner Net",
            "Six bars reconcile exactly to a 32.5% annual net margin.",
            3,
            "illustrative_model",
            (
                "USD annually. First and last bars are absolute totals; the "
                "four middle bars are signed deductions. Expense allocations "
                "are illustrative, not additional scorecard inputs. Cash "
                "operating deductions total $120,000, or $10,000 monthly. "
                "The $25,125 depletion allocation is a separate modeled "
                "noncash economic charge against royalty-producing interests, "
                "not a claimed statutory tax deduction. Owner personal taxes "
                "are outside this illustrative bridge."
            ),
            (
                "$215,000 − $54,000 − $42,000 − $24,000 − $25,125 "
                "= $69,875; $69,875 ÷ $215,000 = 32.5%. "
                "Conservative remains $30,000 × 20% = $6,000; "
                "Scaled remains $400,000 × 45% = $180,000."
            ),
            [
                (
                    "Recognized annual royalty and trading revenue",
                    "$215,000 total recognized operator revenue annually",
                    215000.0,
                    (
                        "Illustrative composition: $165,000 royalty receipts "
                        "plus $50,000 realized rights-trading gains. A rights "
                        "sale collecting $250,000 against $200,000 carrying "
                        "basis contributes $50,000, not $250,000, to revenue. "
                        "Underlying operator hydrocarbon sales are excluded."
                    ),
                ),
                (
                    "Pay the three specialist contractor seats",
                    "Subtract $54,000 for the specialist contractor bench",
                    -54000.0,
                    (
                        "Allocate $24,000 to land work, $18,000 to petroleum "
                        "engineering, and $12,000 to mineral and tax counsel. "
                        "These are annual fractional-engagement budgets rather "
                        "than full-time salaries; the owner occupies the "
                        "single full-time seat."
                    ),
                ),
                (
                    "Operate the recurring portfolio monitoring stack",
                    "Subtract $42,000 for recurring portfolio operating costs",
                    -42000.0,
                    (
                        "Budget production data, royalty accounting tools, "
                        "insurance, records storage, travel, and administration. "
                        "Automation handles statement matching and production "
                        "exceptions; ambiguous deductions and ownership changes "
                        "still require review."
                    ),
                ),
                (
                    "Expense distinct diligence and transaction support",
                    "Subtract $24,000 for expensed transaction support services",
                    -24000.0,
                    (
                        "Cover failed-deal diligence, outside title evidence, "
                        "and expensed disposition support beyond contractor "
                        "retainers. Acquisition costs capitalized into carrying "
                        "basis stay outside this deduction and are recovered "
                        "only through the applicable basis calculation."
                    ),
                ),
                (
                    "Charge modeled depletion on retained producing interests",
                    "Subtract $25,125 for modeled annual economic depletion",
                    -25125.0,
                    (
                        "Apply this illustrative allocation only to retained "
                        "royalty-producing assets. Do not deduct the sold "
                        "interest's recovered basis again. Maintain a separate "
                        "tax schedule under 26 U.S.C. Sections 611 and 613A; "
                        "eligibility and limitations depend on the taxpayer "
                        "and property."
                    ),
                ),
                (
                    "Retain the canonical annual owner net profit",
                    "$69,875 owner net at exactly 32.5% margin",
                    69875.0,
                    (
                        "The Base Case uses one full-time owner and three "
                        "contractors, four people total. This profit measure "
                        "is distinct from cash available after new acquisitions, "
                        "debt principal, working-capital changes, and owner "
                        "personal taxes."
                    ),
                ),
            ],
        ),
        (
            "diag-04-producing-interest-gross-receipt-yields",
            "horizontal_bars",
            "Compare Producing Interests on One Capital Denominator",
            "Five illustrative gross royalty receipt yields per $100,000 invested.",
            2,
            "illustrative_model",
            (
                "Each bar measures annual gross royalty cash receipts divided "
                "by $100,000 of acquisition capital. Values are illustrative "
                "underwriting inputs, not market observations, net margins, "
                "total returns, or perpetual yields. Exclude sale proceeds, "
                "rights-trading gains, and unproved drilling upside. No payment "
                "method itself creates additional mineral yield."
            ),
            (
                "Compare identical capital denominators, then stress decline, "
                "commodity prices, deductions, and payment delays. These five "
                "independent examples do not sum to a portfolio forecast."
            ),
            [
                (
                    "Diversified mature oil royalties with electronic payment",
                    "6% gross yield; $6,000 annual royalty receipts",
                    6.0,
                    (
                        "Illustrative multiwell exposure spreads single-well "
                        "downtime but does not remove basin price risk. Match "
                        "ACH deposits to operator remittance identifiers and "
                        "production months before accepting the trailing "
                        "receipt total."
                    ),
                ),
                (
                    "Single-well producing NPRI with confirmed decimal",
                    "8% gross yield; $8,000 annual royalty receipts",
                    8.0,
                    (
                        "Verify whether the NPRI is fixed or floating and "
                        "whether the operator's decimal follows the instrument. "
                        "One well creates concentrated downtime and depletion "
                        "exposure even when recent payments appear stable."
                    ),
                ),
                (
                    "Mature gas royalties exposed to regional basis",
                    "10% gross yield; $10,000 annual royalty receipts",
                    10.0,
                    (
                        "Stress realized gas prices after regional basis "
                        "differentials, gathering, processing, and other "
                        "instrument-permitted deductions. A quoted benchmark "
                        "price cannot substitute for the property's actual "
                        "settlement economics."
                    ),
                ),
                (
                    "New horizontal production with steep initial decline",
                    "12% gross yield; $12,000 annual royalty receipts",
                    12.0,
                    (
                        "Use an explicit twelve-month decline forecast rather "
                        "than multiplying a peak monthly check by twelve. "
                        "Compare forecasts with completion dates, production "
                        "history, and downtime to expose front-loaded receipts."
                    ),
                ),
                (
                    "Concentrated legacy wells requiring statement reconciliation",
                    "14% gross yield; $14,000 annual royalty receipts",
                    14.0,
                    (
                        "A low acquisition price can produce a high modeled "
                        "receipt yield alongside severe cessation and operator "
                        "risk. Paper checks and inconsistent statement formats "
                        "increase reconciliation work, not intrinsic economic "
                        "return."
                    ),
                ),
            ],
        ),
        (
            "diag-05-statutory-and-risk-preflight",
            "decision_tree",
            "Four Checks Before Capital Leaves the Acquisition Account",
            "Proceed only when each applicable question has documented evidence.",
            5,
            "operating_framework",
            (
                "Four sequential binary checks: a supported yes advances; an "
                "unresolved no routes the package to remediation or rejection. "
                "Numeric values indicate check order, not probability. Texas "
                "citations apply to Texas interests; Oklahoma docket practice "
                "requires its own commission records and governing rules."
            ),
            (
                "The decision path separates property ownership, collectible "
                "economics, public development evidence, and capital structure. "
                "Passing one check does not answer the other three."
            ),
            [
                (
                    "Does recorded title support the conveyed interest?",
                    "Yes: advance; no: cure title or reject",
                    1.0,
                    (
                        "Test seller authority, severed estate ownership, "
                        "reservations, probate, liens, and execution formalities. "
                        "For Texas assets, examine Property Code Sections 5.021 "
                        "and 13.001. A recorder index hit alone does not establish "
                        "marketable title or resolve competing interests."
                    ),
                ),
                (
                    "Do lease terms support collectible stressed receipts?",
                    "Yes: advance; no: reprice or reject economics",
                    2.0,
                    (
                        "Read royalty language, deduction provisions, pooling "
                        "authority, and payment history. Texas Natural Resources "
                        "Code Section 91.402 addresses payment timing and "
                        "specified withholding circumstances. Stress commodity "
                        "prices and decline; determine asset-specific tax and "
                        "depletion treatment under 26 U.S.C. Sections 611 and 613A."
                    ),
                ),
                (
                    "Does the docket support the priced development case?",
                    "Yes: advance; no: remove unsupported development value",
                    3.0,
                    (
                        "Verify application status, issued orders, affected "
                        "tracts, election provisions, and deadlines directly "
                        "with the relevant commission. Texas Natural Resources "
                        "Code Chapter 102 does not define Oklahoma pooling "
                        "practice. Do not turn a public filing into assumed "
                        "drilling, completion, or first-payment dates."
                    ),
                ),
                (
                    "Is the funding structure documented before solicitation?",
                    "Yes: authorize closing; no: stop solicitation and remediate",
                    4.0,
                    (
                        "Document owner-funded purchases separately from pooled "
                        "investor offerings. Review 15 U.S.C. Sections 77b and "
                        "77e, any applicable exemption conditions, and relevant "
                        "state securities requirements before soliciting funds. "
                        "A direct-asset label does not settle whether the "
                        "offered arrangement is a security."
                    ),
                ),
            ],
        ),
        (
            "diag-06-four-to-six-person-mineral-pod",
            "org_architecture",
            "One Owner, Three Specialists; Two Seats Added at Scale",
            "Base pod: 1 FT + 3 C. Scaled pod: 2 FT + 4 C.",
            11,
            "operating_framework",
            (
                "Each stage represents one person, not one full-time equivalent. "
                "The first four seats form both Conservative and Base pods. "
                "The final two seats are Scaled-only additions. FT means "
                "full-time; C means contractor. Contractor capacity is "
                "fractional and scheduled against actual transaction workload."
            ),
            (
                "Four people support the $30,000 and $215,000 revenue cases; "
                "six support the $400,000 case. Expansion depends on verified "
                "workload and economics, not headcount as a revenue predictor."
            ),
            [
                (
                    "Owner and acquisition principal leads the base pod",
                    "Base seat one: one full-time acquisition principal",
                    1.0,
                    (
                        "Own sourcing, underwriting decisions, cash allocation, "
                        "offer authority, royalty exception review, and "
                        "institutional buyer relationships. Maintain the "
                        "investment register and distinguish acquisition "
                        "capital from recognized operating revenue."
                    ),
                ),
                (
                    "Contract landman establishes the title evidence trail",
                    "Base seat two: one contract land specialist",
                    1.0,
                    (
                        "Build tract-level run sheets, calculate supported "
                        "ownership fractions, monitor recording, and track "
                        "operator transfer documents. Escalate instrument "
                        "interpretation and contested title issues to counsel "
                        "rather than resolving them through spreadsheet labels."
                    ),
                ),
                (
                    "Contract petroleum engineer challenges production assumptions",
                    "Base seat three: one contract petroleum engineer",
                    1.0,
                    (
                        "Review well-level decline, commodity sensitivities, "
                        "offset evidence, downtime, and development scenarios. "
                        "Keep proved cash-producing exposure separate from "
                        "unfunded drilling inventory and docket-driven "
                        "acquisition hypotheses."
                    ),
                ),
                (
                    "Contract counsel covers mineral and tax structuring",
                    "Base seat four: one qualified contract attorney",
                    1.0,
                    (
                        "Use counsel with demonstrated mineral conveyance and "
                        "tax competence for instrument review, title remedies, "
                        "entity structure, and depletion questions. Securities "
                        "work requires matching expertise before pooled funding; "
                        "if separate specialists become recurring seats, revise "
                        "headcount and costs explicitly."
                    ),
                ),
                (
                    "Royalty operations analyst joins only at scale",
                    "Scaled seat five: one additional full-time analyst",
                    1.0,
                    (
                        "Take over statement ingestion, deposit matching, "
                        "production monitoring, suspense tracking, and exception "
                        "queues. Use Python csv and sqlite3 for reproducible "
                        "reconciliation while preserving original operator "
                        "statements and review history."
                    ),
                ),
                (
                    "Disposition specialist joins only at scale",
                    "Scaled seat six: one additional contract specialist",
                    1.0,
                    (
                        "Assemble buyer data rooms, normalize asset schedules, "
                        "coordinate bids, and track closing deliverables. "
                        "Document asset-sale intermediary authority and any "
                        "jurisdiction-specific licensing requirements before "
                        "accepting the engagement."
                    ),
                ),
            ],
        ),
        (
            "diag-07-startup-capital-allocation-comparison",
            "stacked_comparison",
            "Allocate Acquisition Capital Without Calling It Revenue",
            "Four buckets across $150,000, $600,000, and $2,000,000 startup plans.",
            4,
            "illustrative_model",
            (
                "All amounts are USD. Numeric stage values describe the "
                "$600,000 reference stack; each stage also identifies the "
                "corresponding floor and ceiling allocations. These are "
                "alternative capital plans, not additive funding rounds and "
                "not mappings to the three annual revenue scenarios. Reserves "
                "and acquisition principal are balance-sheet uses, not "
                "recognized royalty or trading revenue."
            ),
            (
                "Floor: $100,000 + $20,000 + $18,000 + $12,000 = $150,000. "
                "Reference: $450,000 + $60,000 + $60,000 + $30,000 = $600,000. "
                "Ceiling: $1,600,000 + $160,000 + $180,000 + $60,000 "
                "= $2,000,000."
            ),
            [
                (
                    "Fund acquired interests and documented purchase basis",
                    "$450,000 reference allocation for mineral acquisition principal",
                    450000.0,
                    (
                        "Floor allocation is $100,000; ceiling allocation is "
                        "$1,600,000. Deploy only against documented asset "
                        "underwriting and closing evidence. Track basis by "
                        "interest so later disposal proceeds do not inflate "
                        "recognized rights-trading gains."
                    ),
                ),
                (
                    "Reserve transaction-specific diligence and closing capital",
                    "$60,000 reference allocation for diligence and closing",
                    60000.0,
                    (
                        "Floor allocation is $20,000; ceiling allocation is "
                        "$160,000. Cover title examination, engineering, "
                        "recording, and instrument preparation. Separate "
                        "capitalized acquisition costs from expensed failed-deal "
                        "work; do not charge the same invoice twice."
                    ),
                ),
                (
                    "Hold operating liquidity against delayed first receipts",
                    "$60,000 reference allocation for protected operating liquidity",
                    60000.0,
                    (
                        "Floor allocation is $18,000; ceiling allocation is "
                        "$180,000. At selected monthly burns of $1,000, $2,500, "
                        "and $7,500 respectively, these fund 18, 24, and 24 "
                        "months. The floor plan needs another $6,000 or "
                        "equivalent reductions if first receipts take 24 months."
                    ),
                ),
                (
                    "Provision startup systems and controlled contingency cash",
                    "$30,000 reference allocation for setup and contingency",
                    30000.0,
                    (
                        "Floor allocation is $12,000; ceiling allocation is "
                        "$60,000. Cover initial data access, secure document "
                        "storage, account setup, and a remaining contingency "
                        "balance. Contingency can extend runway only to the "
                        "extent it remains unspent."
                    ),
                ),
            ],
        ),
        (
            "diag-08-first-thirty-days-execution-roadmap",
            "timeline_roadmap",
            "Build an Investable Acquisition Process in Thirty Days",
            "Four weekly milestones prepare the pipeline, not a promised closing.",
            12,
            "operating_framework",
            (
                "Milestones cover Days 1–7, 8–14, 15–21, and 22–30. Numeric "
                "values mark milestone end days. The canonical first-deal "
                "window remains 6–24 months. A completed sprint produces "
                "traceable research, underwriting, and operating controls; "
                "it does not establish ownership or royalty income."
            ),
            (
                "Finish the month with a narrow acquisition mandate, a "
                "documented evidence trail, tested economics, and a "
                "review-ready offer process."
            ),
            [
                (
                    "Days 1-7: define mandate and evidence standards",
                    "Complete basin scope, capital limits, and record templates",
                    7.0,
                    (
                        "Choose one initial basin and asset type. Establish "
                        "county recorder and state commission access, the "
                        "investment register, and secure document storage. "
                        "Write separate fields for NMA, NPRI terms, lease "
                        "royalty, unit allocation, and operator pay decimal."
                    ),
                ),
                (
                    "Days 8-14: build the first traceable sourcing cohort",
                    "Complete a sourced shortlist with ownership evidence links",
                    14.0,
                    (
                        "Assemble an illustrative 25-package pilot from "
                        "authorized seller outreach and public records. "
                        "Deduplicate interests, collect instrument references, "
                        "and log seller authority. Monitor relevant public "
                        "pooling dockets without equating filings with funded "
                        "development."
                    ),
                ),
                (
                    "Days 15-21: underwrite and challenge candidate economics",
                    "Complete three conditional cases and reproducible reconciliations",
                    21.0,
                    (
                        "For three candidates with sufficient evidence, build "
                        "commodity, decline, deduction, and timing sensitivities. "
                        "Reconcile available royalty statements using Python "
                        "csv and sqlite3. Compare legal ownership math with "
                        "operator decimals and document every unresolved "
                        "difference before setting offer limits."
                    ),
                ),
                (
                    "Days 22-30: prepare offers and operating handoffs",
                    "Complete reviewed offer packs and a funded runway plan",
                    30.0,
                    (
                        "Prepare conditional offers only for supported "
                        "candidates. Assign title remediation, closing "
                        "deliverables, operator transfer tracking, and royalty "
                        "exception ownership. Reconcile acquisition commitments "
                        "with liquidity through the 6–24 month first-deal "
                        "window; retain unresolved candidates in research."
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
