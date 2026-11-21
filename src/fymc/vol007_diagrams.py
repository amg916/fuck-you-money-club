from __future__ import annotations

VOLUME_007_SUBTITLE = (
    "The Complete Playbook for Unclaimed Property Recovery: "
    "$60,000–$450,000 USD in Annual Service Fees, Starting with a "
    "1 FT + 2 C (3 People) Pod and Scaling to Five"
)

VOLUME_007_POSITIONING_ALTERNATIVES = [
    {
        "title": "The Corporate Lost-Asset Recovery Desk",
        "subtitle": (
            "Recover corporate uncashed warrants and dormant business balances "
            "with documented ownership chains and disciplined service-fee economics."
        ),
        "audience": (
            "Bookkeeping firms, corporate records researchers, and recovery operators "
            "serving controllers with unresolved state-held business assets."
        ),
        "research_basis": (
            "California Code of Civil Procedure sections 1540 and 1582 distinguish "
            "the owner's claim process from compensated recovery agreements. Build "
            "the service around entity continuity, authorized signers, supporting "
            "records, and jurisdiction-specific agreement requirements; never count "
            "the recovered corporate principal as operator revenue."
        ),
        "sources": [
            "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CCP&sectionNum=1540.",
            "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CCP&sectionNum=1582.",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Evidence-First Property Recovery Practice",
        "subtitle": (
            "Win owner trust through verifiable treasury records, transparent "
            "finder agreements, and a clear direct-claim alternative."
        ),
        "audience": (
            "Small research practices that can verify identity carefully and "
            "explain why an owner might purchase assistance instead of filing alone."
        ),
        "research_basis": (
            "New York Abandoned Property Law section 1416 regulates agreements "
            "to locate abandoned property. California Code of Civil Procedure "
            "section 1582 supplies a separate agreement regime. Use state-specific "
            "fee and timing checks rather than exporting one state's contract "
            "nationwide, and disclose that owners can claim directly without "
            "purchasing recovery services."
        ),
        "sources": [
            "https://www.nysenate.gov/legislation/laws/ABP/1416",
            "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CCP&sectionNum=1582.",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Secure Claims Operations Pod",
        "subtitle": (
            "Combine record matching and claim-status tracking with tightly "
            "controlled identity evidence and exception handling."
        ),
        "audience": (
            "Process-oriented founders building a three-person recovery pod "
            "before expanding to a five-person specialist operation."
        ),
        "research_basis": (
            "California Civil Code section 1798.81.5 establishes reasonable-security "
            "requirements for covered businesses handling covered personal "
            "information. Pair its applicability assessment with the ownership "
            "evidence required by California's claim process. Automate candidate "
            "matching and reminders, while retaining human review of identity, "
            "signing authority, disputed ownership, and sensitive-document access."
        ),
        "sources": [
            "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1798.81.5.",
            "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CCP&sectionNum=1540.",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
]


def build_volume_007_diagrams_data() -> list[dict]:
    specs = [
        (
            "diag-01-evidence-to-service-fee",
            "process_flow",
            "From Treasury Record to Recognized Service Fee",
            "Five operating stages separate client assets from operator earnings.",
            1,
            "operating_framework",
            (
                "Use authorized public records and owner-provided evidence. "
                "A matching name is only a lead, not proof of entitlement. "
                "The canonical first-deal planning window is 3–12 months; "
                "filing does not establish a payment date."
            ),
            (
                "State-held principal belongs to the owner. Recognize only "
                "earned service fees under the applicable accounting policy."
            ),
            [
                (
                    "Source eligible records",
                    "Capture the official record and custody dates",
                    1.0,
                    (
                        "Record treasury jurisdiction, property identifier, holder, "
                        "reported owner, and available dates in SQLite. Preserve "
                        "source links and follow the portal's access conditions."
                    ),
                ),
                (
                    "Resolve ownership",
                    "Build an evidence-backed owner identity chain",
                    2.0,
                    (
                        "Compare addresses, entity filings, name changes, and "
                        "signer authority. Escalate mergers, estates, and dissolved "
                        "entities instead of treating fuzzy matches as ownership."
                    ),
                ),
                (
                    "Qualify the engagement",
                    "Check finder rules before compensated recovery work",
                    3.0,
                    (
                        "Document registration requirements, permitted contracting "
                        "dates, fee limits, and required agreement terms. Explain "
                        "the owner's direct-claim option before requesting signature."
                    ),
                ),
                (
                    "Submit and track",
                    "File authorized evidence through the treasury channel",
                    4.0,
                    (
                        "Use the state's accepted claimant or representative "
                        "process. Log receipt identifiers, evidence requests, "
                        "response deadlines, and owner-authorized status checks."
                    ),
                ),
                (
                    "Reconcile and bill",
                    "Separate owner proceeds from earned service fees",
                    5.0,
                    (
                        "Prefer treasury payment directly to the owner. Confirm "
                        "the contractual earning event, invoice the permitted fee, "
                        "and reconcile fee receivables separately from client principal."
                    ),
                ),
            ],
        ),
        (
            "diag-02-mature-cohort-conversion",
            "funnel",
            "A Mature Cohort Producing 75 Paid Cases",
            "Nested case populations support $255,000 in Base-Case service fees.",
            6,
            "illustrative_model",
            (
                "Illustrative mature cohort, not observed conversion performance. "
                "Begin with 1,000 distinct owner-property case IDs; each later "
                "population is a subset of the preceding population. Assume "
                "75 completed, fee-paid cases recognized within one modeled year "
                "at $3,400 average service fees. This is not a 30-day forecast."
            ),
            (
                "1,000 × 40% × 40% × 62.5% × 75% = 75 paid cases; "
                "75 × $3,400 = $255,000 recognized service-fee revenue."
            ),
            [
                (
                    "Screened prospects",
                    "1,000 distinct cases enter the research cohort",
                    1000.0,
                    (
                        "Deduplicate by jurisdiction, property identifier, and "
                        "reported owner. Exclude repeated outreach records rather "
                        "than inflating the top of the funnel."
                    ),
                ),
                (
                    "Evidence-supported matches",
                    "400 cases pass preliminary identity and value screening",
                    400.0,
                    (
                        "Forty percent of screened cases have a supportable "
                        "ownership hypothesis and sufficient expected fees to "
                        "justify additional research; entitlement remains subject to proof."
                    ),
                ),
                (
                    "Lawfully engaged owners",
                    "160 matched cases obtain valid service agreements",
                    160.0,
                    (
                        "Forty percent of matched cases proceed after direct-claim "
                        "disclosure, signer verification, statutory timing checks, "
                        "and acceptance of a permitted fee structure."
                    ),
                ),
                (
                    "Complete claims filed",
                    "100 engaged cases reach accepted submission status",
                    100.0,
                    (
                        "Sixty-two and one-half percent of engagements supply "
                        "the necessary records. Submission acceptance does not "
                        "mean the treasury has approved ownership or payment."
                    ),
                ),
                (
                    "Recovered and fee-paid",
                    "75 filed cases produce recognized and collected fees",
                    75.0,
                    (
                        "Seventy-five percent of filed cases complete within the "
                        "modeled recognition year. Remaining cases stay open, "
                        "withdraw, or fail; do not book their hoped-for fees."
                    ),
                ),
            ],
        ),
        (
            "diag-03-base-service-fee-waterfall",
            "waterfall",
            "Base-Case Revenue to $95,625 Owner Net",
            "Six bars reconcile $255,000 gross fees to a 37.5% net margin.",
            3,
            "illustrative_model",
            (
                "Expense categories are an illustrative allocation, not supplied "
                "scorecard line items. First and last bars are totals; intermediate "
                "negative bars are deductions. Total expenses are $159,375 annually, "
                "or $13,281.25 monthly, exceeding the supplied $1,500–$8,000 monthly "
                "opex band. That band cannot represent all-in Base expenses; only "
                "the modeled $4,000 monthly fixed-overhead component falls inside it."
            ),
            (
                "$255,000 − $48,000 − $66,000 − $25,500 − $19,875 = "
                "$95,625; $95,625 ÷ $255,000 = 37.5%."
            ),
            [
                (
                    "Recognized service fees",
                    "$255,000 annual operator revenue before modeled expenses",
                    255000.0,
                    (
                        "Starting total: 75 paid cases at $3,400 average fees. "
                        "Exclude treasury disbursements belonging to owners and "
                        "exclude unearned fees from unresolved claims."
                    ),
                ),
                (
                    "Fixed operating overhead",
                    "Deduct $48,000 for recurring operating infrastructure",
                    -48000.0,
                    (
                        "Allocate $4,000 monthly to software, insurance, secure "
                        "document handling, bookkeeping, and administration. Remaining "
                        "annual contribution after this deduction is $207,000."
                    ),
                ),
                (
                    "Contract case delivery",
                    "Deduct $66,000 for two contractors' delivery work",
                    -66000.0,
                    (
                        "Budget researcher and claims-administrator capacity at "
                        "$880 per completed case across 75 cases. Remaining "
                        "annual contribution after this deduction is $141,000."
                    ),
                ),
                (
                    "Research and acquisition",
                    "Deduct $25,500 for sourcing and owner engagement",
                    -25500.0,
                    (
                        "Allocate record acquisition, permitted outreach, and "
                        "unsuccessful prospect research at $340 per completed "
                        "case. Remaining annual contribution is $115,500."
                    ),
                ),
                (
                    "Verification and exceptions",
                    "Deduct $19,875 for evidence and exception handling",
                    -19875.0,
                    (
                        "Allocate $265 per completed case to incremental certified "
                        "records, identity checks, and specialist review. Keep these "
                        "charges distinct from contractor delivery and fixed overhead."
                    ),
                ),
                (
                    "Annual owner net profit",
                    "$95,625 ending profit equals 37.5% of service fees",
                    95625.0,
                    (
                        "Ending total uses the canonical owner-net metric. "
                        "Conservative remains $60,000 × 25% = $15,000; "
                        "Scaled remains $450,000 × 50% = $225,000."
                    ),
                ),
            ],
        ),
        (
            "diag-04-paid-case-yield-by-property-rail",
            "horizontal_bars",
            "Illustrative Service-Fee Yield by Property Rail",
            "Compare dollars per completed paid case, not client asset balances.",
            2,
            "illustrative_model",
            (
                "Selected high-value cases only; these are constructed planning "
                "figures, not market averages. Assume 15 paid cases in each of "
                "five mutually exclusive property categories. A hypothetical "
                "permitted 10% fee connects the example balances to fee yields; "
                "actual fee bases, caps, timing, and agreements require state review."
            ),
            (
                "15 × ($5,000 + $4,500 + $3,500 + $2,500 + $1,500) = "
                "$255,000 fees on $2,550,000 owner principal at the assumed rate."
            ),
            [
                (
                    "Corporate government warrants",
                    "$5,000 service fees per completed paid case",
                    5000.0,
                    (
                        "Illustrative $50,000 owner balance at 10%. Confirm that "
                        "the warrant proceeds are actually state-held, then verify "
                        "entity continuity and the officer's signing authority."
                    ),
                ),
                (
                    "Business vendor checks",
                    "$4,500 service fees per completed paid case",
                    4500.0,
                    (
                        "Illustrative $45,000 owner balance at 10%. Reconcile "
                        "supplier names, former addresses, and successor entities; "
                        "exclude government warrants assigned to the preceding category."
                    ),
                ),
                (
                    "Insurance proceeds",
                    "$3,500 service fees per completed paid case",
                    3500.0,
                    (
                        "Illustrative $35,000 owner balance at 10%. Resolve "
                        "policyholder, beneficiary, and estate distinctions before "
                        "requesting documents or representing a claimant's entitlement."
                    ),
                ),
                (
                    "Securities-related cash",
                    "$2,500 service fees per completed paid case",
                    2500.0,
                    (
                        "Illustrative $25,000 recoverable cash balance at 10%. "
                        "Confirm the state's recorded property form; do not price "
                        "fees from a speculative current share-market valuation."
                    ),
                ),
                (
                    "High-value wage balances",
                    "$1,500 service fees per completed paid case",
                    1500.0,
                    (
                        "Illustrative $15,000 owner balance at 10%. Screen "
                        "for consolidated high-value balances; ordinary small "
                        "payroll checks may not support manual recovery economics."
                    ),
                ),
            ],
        ),
        (
            "diag-05-statutory-and-risk-routing",
            "decision_tree",
            "Four Pre-Flight Checks Before Taking a Case",
            "Advance only with documented evidence; route failures explicitly.",
            5,
            "operating_framework",
            (
                "Read sequentially: passing a check advances to the next check. "
                "The numeric field is a check ordinal, not a probability. "
                "Determine the applicable jurisdiction and current statutory text "
                "for each case; California and New York are concrete examples, "
                "not a nationwide substitute."
            ),
            (
                "Registration, contract timing, ownership, and secure handling "
                "must be resolved before a case enters paid delivery."
            ),
            [
                (
                    "Finder status and authority",
                    "Verify required registration and permitted representative activity",
                    1.0,
                    (
                        "Check the treasury's finder requirements and any "
                        "applicable occupational licensing rules. If required "
                        "credentials or owner authorization are absent, pause the "
                        "engagement and identify the specific missing requirement."
                    ),
                ),
                (
                    "Agreement timing and fee",
                    "Test statutory dates, fee limits, and contract terms",
                    2.0,
                    (
                        "For California, examine Code of Civil Procedure section "
                        "1582; for New York, Abandoned Property Law section 1416. "
                        "Document relevant event dates and fee calculations. Route "
                        "premature cases to a dated revisit list; reject prohibited fees."
                    ),
                ),
                (
                    "Ownership and case value",
                    "Verify the claimant and calculate expected contribution",
                    3.0,
                    (
                        "California Code of Civil Procedure section 1540 anchors "
                        "the claim process. Escalate conflicting identities or "
                        "successor rights. Decline cases whose expected lawful fees "
                        "cannot cover research, evidence, delivery, and collection costs."
                    ),
                ),
                (
                    "Privacy and owner understanding",
                    "Protect identity evidence and disclose direct claiming",
                    4.0,
                    (
                        "Assess California Civil Code section 1798.81.5 where "
                        "applicable. Use restricted encrypted storage, multifactor "
                        "authentication, and expiring document links. Explain that "
                        "the owner can claim directly; pause if understanding or "
                        "secure evidence collection remains unresolved."
                    ),
                ),
            ],
        ),
        (
            "diag-06-three-to-five-person-pod",
            "org_architecture",
            "Three Core Seats, Two Scale Seats",
            "Keep accountable ownership explicit as annual service fees grow.",
            11,
            "operating_framework",
            (
                "FT means full-time; C means contractor. Conservative and Base "
                "use one FT plus two C, totaling three people. Scaled uses two "
                "FT plus three C, totaling five people. Each numeric value is "
                "one person; the final two seats belong only to the scaled pod."
            ),
            (
                "Core pod: $60,000 revenue / $15,000 net or $255,000 / $95,625. "
                "Scaled five-person pod: $450,000 revenue / $225,000 net."
            ),
            [
                (
                    "Founder and accountable operator",
                    "Core seat: one full-time operating owner",
                    1.0,
                    (
                        "Own engagement decisions, treasury relationships, fee "
                        "pricing, dispute resolution, and cash reconciliation. "
                        "Review exception queues rather than delegating final "
                        "ownership judgments to an automated matcher."
                    ),
                ),
                (
                    "Records investigator",
                    "Core seat: one contractor researching owner evidence",
                    1.0,
                    (
                        "Maintain source provenance, entity histories, address "
                        "matches, and duplicate controls. Access only assigned "
                        "case records; return ambiguous matches with explicit "
                        "evidence gaps instead of confident guesses."
                    ),
                ),
                (
                    "Claims administrator",
                    "Core seat: one contractor managing submission completeness",
                    1.0,
                    (
                        "Prepare authorized claim packets, track treasury receipts, "
                        "request missing evidence, and maintain aging reports. "
                        "Never convert a status update into an unsupported "
                        "promise about payment timing."
                    ),
                ),
                (
                    "Delivery and queue manager",
                    "Scale addition: one full-time case operations lead",
                    1.0,
                    (
                        "Coordinate researcher capacity, evidence response times, "
                        "handoffs, and receivable follow-up. Add this seat when "
                        "measured backlog and collected-fee economics support "
                        "ongoing payroll, not merely a larger prospect list."
                    ),
                ),
                (
                    "Complex-case specialist",
                    "Scale addition: one contractor reviewing exceptional cases",
                    1.0,
                    (
                        "Handle documented entity succession, estate evidence, "
                        "or jurisdiction-specific specialist work within their "
                        "credentials. Escalate matters requiring licensed counsel "
                        "instead of expanding administrative staff authority."
                    ),
                ),
            ],
        ),
        (
            "diag-07-startup-capital-allocation",
            "stacked_comparison",
            "Allocate Startup Capital Before Scaling Outreach",
            "Four buckets total $20,000 within the $5,000–$35,000 range.",
            4,
            "illustrative_model",
            (
                "Numeric values describe one $20,000 startup allocation. "
                "Details also provide lean and expanded allocations totaling "
                "$5,000 and $35,000 respectively. These are deployment budgets, "
                "not projected revenue or sufficient runway for every case. "
                "Owner living costs are outside these allocations."
            ),
            (
                "Central allocation: $4,000 + $6,000 + $5,000 + $5,000 = "
                "$20,000. A 3–12 month first-deal window requires separate "
                "runway planning against actual recurring and variable costs."
            ),
            [
                (
                    "Jurisdiction and agreement setup",
                    "$4,000 central allocation for lawful engagement setup",
                    4000.0,
                    (
                        "Lean allocation $1,000; expanded allocation $7,000. "
                        "Fund applicable registration, jurisdiction-specific "
                        "agreement drafting, and focused professional review "
                        "before purchasing a large prospect inventory."
                    ),
                ),
                (
                    "Secure records and workflow",
                    "$6,000 central allocation for evidence-handling infrastructure",
                    6000.0,
                    (
                        "Lean allocation $1,500; expanded allocation $10,000. "
                        "Configure Microsoft 365 or Google Workspace access "
                        "controls, encrypted endpoints, backup restoration tests, "
                        "and a minimal claim-status database."
                    ),
                ),
                (
                    "Research and owner acquisition",
                    "$5,000 central allocation for measured prospect development",
                    5000.0,
                    (
                        "Lean allocation $1,000; expanded allocation $8,000. "
                        "Purchase authorized records, obtain certified entity "
                        "documents, and test transparent outreach. Track spend "
                        "per evidence-supported case before increasing volume."
                    ),
                ),
                (
                    "Operating liquidity reserve",
                    "$5,000 central allocation for early cash timing gaps",
                    5000.0,
                    (
                        "Lean allocation $1,500; expanded allocation $10,000. "
                        "At $4,000 monthly fixed overhead, the central reserve "
                        "covers only 1.25 months before variable costs; arrange "
                        "additional runway or reduce the initial cost structure."
                    ),
                ),
            ],
        ),
        (
            "diag-08-thirty-day-launch-sprint",
            "timeline_roadmap",
            "Thirty Days to a Controlled Recovery Operation",
            "Build a qualified pipeline without promising a treasury payout.",
            12,
            "operating_framework",
            (
                "Four weekly milestones establish operating readiness, not "
                "first-deal completion. The canonical first-deal window remains "
                "3–12 months. Pilot counts are workload targets rather than "
                "predicted engagement or collection results."
            ),
            (
                "Finish the month with traceable records, reviewed agreements, "
                "secure evidence handling, and an owner-authorized claim queue."
            ),
            [
                (
                    "Days 1-7",
                    "Select one jurisdiction and document the operating rules",
                    1.0,
                    (
                        "Choose a treasury and two property categories. Capture "
                        "finder requirements, statutory event dates, fee limits, "
                        "claim evidence requirements, and direct-claim instructions. "
                        "Budget fixed overhead and document the funding gap."
                    ),
                ),
                (
                    "Days 8-14",
                    "Configure secure intake and review twenty-five records",
                    2.0,
                    (
                        "Create a SQLite case register with stable identifiers, "
                        "source links, access owners, and next-action dates. "
                        "Test restricted uploads and backups. Manually review "
                        "25 public records to calibrate duplicate and identity rules."
                    ),
                ),
                (
                    "Days 15-21",
                    "Test transparent outreach against ten screened prospects",
                    3.0,
                    (
                        "Where permitted, contact ten evidence-supported prospects "
                        "without implying government affiliation. Explain direct "
                        "claiming, document responses, and execute only agreements "
                        "whose timing, fees, and signer authority have been checked."
                    ),
                ),
                (
                    "Days 22-30",
                    "Prepare eligible packets and inspect the evidence backlog",
                    4.0,
                    (
                        "Submit only complete, authorized claims; otherwise log "
                        "the exact missing evidence and responsible person. "
                        "Review case aging, estimated contribution, and cash "
                        "runway. Schedule weekly treasury-status and receivable reviews."
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
