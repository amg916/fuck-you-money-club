from __future__ import annotations

VOLUME_016_SUBTITLE = (
    "The Complete Playbook for Probate Real Estate: "
    "$120,000–$900,000 USD in Annual Retained Brokerage Revenue, "
    "Starting with a 2 FT + 3 C Five-Person Pod"
)

VOLUME_016_POSITIONING_ALTERNATIVES = [
    {
        "title": "The Executor's Property Operations Desk",
        "subtitle": (
            "Build an executor concierge brokerage that turns documented authority, "
            "property preparation, and transaction discipline into retained commissions."
        ),
        "audience": (
            "Licensed real estate operators serving personal representatives who need "
            "one accountable coordinator for vendors, listing preparation, and closing."
        ),
        "research_basis": (
            "California Business and Professions Code section 10130 establishes the "
            "licensing requirement for brokerage activity. California Probate Code "
            "sections 10501 and 10580 distinguish authority limits and notice duties "
            "under independent administration. These requirements support a documented "
            "executor workflow, not a promise that every estate can sell immediately."
        ),
        "sources": [
            "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=BPC&sectionNum=10130.",
            "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PROB&sectionNum=10501.",
            "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PROB&sectionNum=10580.",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Probate Attorney's Transaction Partner",
        "subtitle": (
            "Earn repeat introductions through reliable property execution, "
            "clean status reporting, and a referral model without paid steering."
        ),
        "audience": (
            "Broker-led teams building probate-attorney relationships through useful "
            "transaction support rather than purchased settlement-service referrals."
        ),
        "research_basis": (
            "12 U.S.C. section 2607 and 12 CFR section 1024.14 restrict referral "
            "payments and fee splitting within their covered settlement-service scope. "
            "The operating thesis is service-led relationship development: attorneys "
            "handle estate questions, licensed brokers handle brokerage, and each "
            "engagement documents scope, compensation, and client choice."
        ),
        "sources": [
            "https://www.law.cornell.edu/uscode/text/12/2607",
            "https://www.ecfr.gov/current/title-12/chapter-X/part-1024/section-1024.14",
            "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=BPC&sectionNum=10130.",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "Authority-First Probate Property Sales",
        "subtitle": (
            "Specialize in estate property transactions where authority, notices, "
            "conflicts, and court calendars determine the critical path."
        ),
        "audience": (
            "Experienced brokers coordinating with estate counsel and title teams "
            "on court-dependent sales and separately documented acquisition proposals."
        ),
        "research_basis": (
            "California Probate Code section 10501 identifies transactions requiring "
            "court supervision under limited authority; section 10580 addresses notice "
            "of proposed action. Section 9880 restricts personal representatives from "
            "purchasing estate property, subject to statutory exceptions. These "
            "California examples support jurisdiction-specific routing rather than "
            "a nationwide assumption that an executor's signature is sufficient."
        ),
        "sources": [
            "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PROB&sectionNum=10501.",
            "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PROB&sectionNum=10580.",
            "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PROB&sectionNum=9880.",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
]


def build_volume_016_diagrams_data() -> list[dict]:
    specs = [
        (
            "diag-01-authority-to-retained-commission",
            "process_flow",
            "From Probate Signal to Collected Commission",
            "Five operating stages separate estate authority from brokerage execution.",
            1,
            "operating_framework",
            (
                "Use the property's jurisdiction, current court orders, and actual "
                "appointment documents. California statutes illustrate routing rules, "
                "not uniform national procedure. Initial deal timing is 4–18 months."
            ),
            (
                "Docket alerts identify possible work; verified authority permits "
                "the appropriate next step. Recognized operator revenue is retained "
                "brokerage commission after brokerage splits, never property sale value."
            ),
            [
                (
                    "Detect and qualify",
                    "Create one deduplicated estate opportunity record",
                    1.0,
                    (
                        "Use permitted court docket alerts and county property records "
                        "to connect the estate, parcel, representative, and counsel. "
                        "Record source dates; a filing alone does not establish sale intent."
                    ),
                ),
                (
                    "Verify authority",
                    "Document who can authorize each transaction action",
                    2.0,
                    (
                        "Obtain appointment documents, current orders, and counsel's "
                        "sale-path assessment. California Probate Code section 10501 "
                        "requires different treatment for full and limited authority."
                    ),
                ),
                (
                    "Engage and prepare",
                    "Execute brokerage scope and property preparation plan",
                    3.0,
                    (
                        "Confirm licensing, agency relationships, occupancy, insurance, "
                        "access, and vendor budgets. Executor concierge work coordinates "
                        "property tasks without replacing the representative or estate counsel."
                    ),
                ),
                (
                    "Market and transact",
                    "Track offers alongside notices and court dependencies",
                    4.0,
                    (
                        "Use transaction checklists for disclosures, title exceptions, "
                        "notice delivery, objections, and required confirmation. Avoid "
                        "promising possession before occupancy and closing conditions resolve."
                    ),
                ),
                (
                    "Close and reconcile",
                    "Match closing evidence to retained brokerage revenue",
                    5.0,
                    (
                        "Reconcile the closing statement, brokerage split, collection, "
                        "and transaction expenses. Exclude escrow principal, estate "
                        "proceeds, vendor reimbursements, and acquisition resale proceeds "
                        "from this brokerage scorecard."
                    ),
                ),
            ],
        ),
        (
            "diag-02-mature-cohort-conversion",
            "funnel",
            "A Mature Cohort Producing 30 Closings",
            "Nested estate-opportunity counts connect origination to the Base Case.",
            6,
            "illustrative_model",
            (
                "Illustrative mature cohort, not observed conversion data or a first-year "
                "forecast. One record represents one estate-property opportunity. "
                "The 30 eventual closings are assumed to fall within the modeled "
                "revenue year after a sufficient pipeline-development period."
            ),
            (
                "1,000 opportunities yield 30 closings: 3.0% end-to-end conversion. "
                "Thirty closings at $17,000 average retained commission produce "
                "$510,000 Base-Case annual gross operator revenue."
            ),
            [
                (
                    "Recorded opportunities",
                    "1,000 distinct estate-property opportunities enter the cohort",
                    1000.0,
                    (
                        "Deduplicate docket and parcel records before counting. "
                        "Exclude repeated filings, duplicate representatives, and "
                        "unrelated properties from the same opportunity record."
                    ),
                ),
                (
                    "Qualified opportunities",
                    "400 opportunities satisfy documented service-fit criteria",
                    400.0,
                    (
                        "Retain 40% of the starting cohort after checking geography, "
                        "real property ownership, a plausible sale need, and an "
                        "identifiable representative or estate attorney."
                    ),
                ),
                (
                    "Substantive conversations",
                    "120 qualified opportunities produce representative conversations",
                    120.0,
                    (
                        "Convert 30% of qualified opportunities into two-way discussions "
                        "with the representative or authorized counsel. Count completed "
                        "conversations, not unanswered calls or automated messages."
                    ),
                ),
                (
                    "Executed listings",
                    "60 conversations convert into signed brokerage engagements",
                    60.0,
                    (
                        "Convert 50% of engaged opportunities after authority review, "
                        "scope agreement, and property assessment. Signed listings "
                        "remain exposed to disputes, withdrawals, and delayed court dates."
                    ),
                ),
                (
                    "Closed transactions",
                    "30 listings close within the modeled revenue year",
                    30.0,
                    (
                        "Close 50% of signed listings during the modeled period. "
                        "The remaining listings may carry forward or terminate; "
                        "record neither as collected commission."
                    ),
                ),
            ],
        ),
        (
            "diag-03-base-case-profit-bridge",
            "waterfall",
            "The $510,000 to $140,250 Profit Bridge",
            "Four illustrative expense buckets reconcile to a 27.5% net margin.",
            3,
            "illustrative_model",
            (
                "USD per year. First and last bars are absolute totals; middle bars "
                "are signed expense movements. Cost allocations are illustrative, "
                "while revenue, margin, and owner net profit are canonical. "
                "Do not subtract brokerage splits again from retained revenue."
            ),
            (
                "$510,000 − $180,000 − $90,000 − $60,000 − $39,750 = $140,250; "
                "$140,250 / $510,000 = 27.5%. Conservative: $120,000 revenue "
                "and $24,000 profit at 20%. Scaled: $900,000 revenue and "
                "$315,000 profit at 35%."
            ),
            [
                (
                    "Retained gross revenue",
                    "$510,000 annual commissions after brokerage splits",
                    510000.0,
                    (
                        "Opening absolute total. Model 30 completed brokerage "
                        "transactions averaging $17,000 retained commission; underlying "
                        "home prices and estate distributions are excluded."
                    ),
                ),
                (
                    "Full-time personnel",
                    "Subtract $180,000 for two full-time operating seats",
                    -180000.0,
                    (
                        "Illustrative loaded compensation for the broker lead and "
                        "operations lead. Any owner compensation included here is "
                        "an expense distinct from the residual owner net profit."
                    ),
                ),
                (
                    "Contractor delivery",
                    "Subtract $90,000 for three contracted delivery seats",
                    -90000.0,
                    (
                        "Budget field brokerage support, transaction coordination, "
                        "and vendor coordination. Include only operator-paid costs "
                        "not already removed in calculating retained commissions."
                    ),
                ),
                (
                    "Origination and marketing",
                    "Subtract $60,000 for attributable pipeline development",
                    -60000.0,
                    (
                        "Allocate docket access, relationship development, property "
                        "marketing, and targeted outreach. Measure spend against "
                        "collected commissions rather than unsigned pipeline estimates."
                    ),
                ),
                (
                    "Operating overhead",
                    "Subtract $39,750 for remaining operating expenses",
                    -39750.0,
                    (
                        "Illustrative insurance, software, accounting, licensing, "
                        "travel, and administrative expense allocation. Estate-funded "
                        "repairs paid directly to vendors are outside operator revenue."
                    ),
                ),
                (
                    "Annual owner net profit",
                    "$140,250 residual profit at 27.5% net margin",
                    140250.0,
                    (
                        "Closing absolute total, not another additive movement. "
                        "Total modeled expenses are $369,750; this bridge preserves "
                        "the canonical Base-Case annual owner net profit."
                    ),
                ),
            ],
        ),
        (
            "diag-04-retained-commission-by-service-niche",
            "horizontal_bars",
            "Five Service Niches, One Brokerage Revenue Rail",
            "Illustrative retained commission per completed transaction, in USD.",
            2,
            "illustrative_model",
            (
                "These are planning assumptions, not market commission schedules "
                "or evidence that complexity causes higher fees. Compensation is "
                "negotiated for each engagement. Assign each closing to one primary "
                "niche so categories do not overlap."
            ),
            (
                "Six closings in each niche produce 30 total transactions and "
                "6 × ($10,000 + $14,000 + $17,000 + $20,000 + $24,000) = "
                "$510,000 retained revenue. No separate concierge fee or "
                "acquisition spread is included."
            ),
            [
                (
                    "Straightforward local estate",
                    "$10,000 retained commission per completed property sale",
                    10000.0,
                    (
                        "Illustrative six-deal cohort contributes $60,000 annually. "
                        "Prioritize clear access, manageable preparation, and an "
                        "available local representative; still verify sale authority."
                    ),
                ),
                (
                    "Remote executor coordination",
                    "$14,000 retained commission per completed property sale",
                    14000.0,
                    (
                        "Illustrative six-deal cohort contributes $84,000 annually. "
                        "Coordinate access, photographs, vendor scheduling, and concise "
                        "status reports for a representative living elsewhere."
                    ),
                ),
                (
                    "Preparation-intensive vacant home",
                    "$17,000 retained commission per completed property sale",
                    17000.0,
                    (
                        "Illustrative six-deal cohort contributes $102,000 annually. "
                        "Document vacancy coverage, security, utilities, cleanout scope, "
                        "and who authorizes and pays each vendor."
                    ),
                ),
                (
                    "Court-dependent sale",
                    "$20,000 retained commission per completed property sale",
                    20000.0,
                    (
                        "Illustrative six-deal cohort contributes $120,000 annually. "
                        "Coordinate counsel, court calendars, and buyer expectations; "
                        "extra procedural work does not establish a fixed fee entitlement."
                    ),
                ),
                (
                    "Complex property brokerage",
                    "$24,000 retained commission per completed property sale",
                    24000.0,
                    (
                        "Illustrative six-deal cohort contributes $144,000 annually. "
                        "Route title, occupancy, and condition issues to appropriate "
                        "specialists before treating an accepted offer as dependable revenue."
                    ),
                ),
            ],
        ),
        (
            "diag-05-statutory-and-risk-routing",
            "decision_tree",
            "Four Checks Before Committing the Estate",
            "A sequential yes-or-redirect decision path, documented in the transaction file.",
            5,
            "operating_framework",
            (
                "California is the statutory example; replace it with the property's "
                "applicable law and actual court orders. Numeric values indicate "
                "check sequence, not probabilities or a measure of legal sufficiency."
            ),
            (
                "Proceed only along a documented transaction path. Missing authority, "
                "unresolved objections, and conflicting interests change the workflow; "
                "they are not problems that automation can waive."
            ),
            [
                (
                    "Authority and sale route",
                    "Verified authority: continue; missing authority: return to counsel",
                    1.0,
                    (
                        "Inspect appointment documents and current orders. California "
                        "Probate Code section 10501 distinguishes full from limited "
                        "independent-administration authority; limited-authority real "
                        "property sales require the applicable court-supervised route."
                    ),
                ),
                (
                    "Licensing and referral economics",
                    "Permitted role: continue; prohibited compensation: restructure engagement",
                    2.0,
                    (
                        "Confirm brokerage licensing under California Business and "
                        "Professions Code section 10130. Screen covered referral "
                        "arrangements under 12 U.S.C. section 2607 and "
                        "12 CFR section 1024.14; do not pay for prohibited steering."
                    ),
                ),
                (
                    "Notices, objections, and closing readiness",
                    "Requirements satisfied: continue; unresolved conditions: suspend closing commitments",
                    3.0,
                    (
                        "Have counsel identify applicable notice duties under "
                        "California Probate Code section 10580 and the effect of "
                        "any objection. Resolve title exceptions, occupancy, and "
                        "required court action before committing to a closing date."
                    ),
                ),
                (
                    "Conflicts and principal acquisitions",
                    "Independent review completed: proceed; unresolved conflict: separate transaction paths",
                    4.0,
                    (
                        "Document buyer affiliations and agency interests. California "
                        "Probate Code section 9880 restricts representative purchases "
                        "subject to statutory exceptions. Route affiliated acquisitions "
                        "for counsel review; brokerage disclosures alone may be insufficient."
                    ),
                ),
            ],
        ),
        (
            "diag-06-five-to-seven-person-pod",
            "org_architecture",
            "Five Core Seats, Two Conditional Expansion Seats",
            "Conservative and Base: 2 FT + 3 C; Scaled: 3 FT + 4 C.",
            11,
            "operating_framework",
            (
                "Each stage describes one potential person. Numeric values show "
                "Base-Case active headcount: five ones and two zeros. Activate "
                "both expansion seats for the seven-person Scaled configuration. "
                "Estate counsel and title providers are external counterparties."
            ),
            (
                "The five-person pod supports the $120,000 Conservative and "
                "$510,000 Base revenue scenarios. The seven-person pod supports "
                "the $900,000 Scaled scenario; additional seats alone do not "
                "establish demand or commission production."
            ),
            [
                (
                    "Broker lead — FT",
                    "One core full-time owner of brokerage execution",
                    1.0,
                    (
                        "Own agency relationships, listing strategy, negotiations, "
                        "and brokerage supervision. Maintain a weekly exception "
                        "review covering authority, disputes, and stalled transactions."
                    ),
                ),
                (
                    "Operations lead — FT",
                    "One core full-time owner of pipeline control",
                    1.0,
                    (
                        "Maintain docket alerts, CRM records, checklist versions, "
                        "cash forecasts, and reporting. Escalate missing evidence "
                        "rather than marking incomplete statutory tasks as finished."
                    ),
                ),
                (
                    "Field brokerage support — C",
                    "One core contractor handling authorized licensed fieldwork",
                    1.0,
                    (
                        "Provide appropriately licensed showing, inspection-access, "
                        "and market-support services within the brokerage's supervision. "
                        "Confirm worker classification under applicable law."
                    ),
                ),
                (
                    "Transaction coordinator — C",
                    "One core contractor maintaining transaction evidence",
                    1.0,
                    (
                        "Track deadlines, signatures, disclosures, and closing records. "
                        "Administrative coordination does not authorize independent "
                        "brokerage activity or interpretation of disputed estate powers."
                    ),
                ),
                (
                    "Property vendor coordinator — C",
                    "One core contractor organizing property preparation",
                    1.0,
                    (
                        "Schedule authorized cleanouts, security checks, repairs, "
                        "and photography. Keep vendor scopes and estate payment "
                        "responsibility separate from operator commission accounting."
                    ),
                ),
                (
                    "Additional licensed producer — FT",
                    "Zero Base seats; add one Scaled full-time producer",
                    0.0,
                    (
                        "Expand to three full-time people when collected revenue, "
                        "active listings, and response-time pressure support the "
                        "added fixed cost and supervisory workload."
                    ),
                ),
                (
                    "Additional coordination support — C",
                    "Zero Base seats; add one Scaled contractor",
                    0.0,
                    (
                        "Expand to four contractors for greater docket, document, "
                        "and vendor workload. Assign a defined service scope "
                        "instead of creating overlapping ownership of deadlines."
                    ),
                ),
            ],
        ),
        (
            "diag-07-startup-capital-allocation",
            "stacked_comparison",
            "Allocate Capital Before the First Closing",
            "Four buckets compare $15,000, $50,000, and $100,000 startup plans.",
            4,
            "illustrative_model",
            (
                "Numeric values encode the illustrative $50,000 allocation. "
                "Each stage also states its corresponding $15,000 and $100,000 "
                "allocation. These are startup funding plans, not additional "
                "revenue scenarios or assumed annual expense budgets."
            ),
            (
                "Low plan: $4,000 + $5,000 + $3,000 + $3,000 = $15,000. "
                "Middle plan: $12,000 + $16,000 + $10,000 + $12,000 = $50,000. "
                "High plan: $24,000 + $32,000 + $20,000 + $24,000 = $100,000."
            ),
            [
                (
                    "Business readiness and systems",
                    "$12,000 middle-plan allocation for setup and operating systems",
                    12000.0,
                    (
                        "Low: $4,000; middle: $12,000; high: $24,000. Fund "
                        "licensing-related setup, insurance deposits, devices, CRM, "
                        "docket access, document storage, and transaction checklist configuration."
                    ),
                ),
                (
                    "Origination and relationship development",
                    "$16,000 middle-plan allocation for measurable pipeline creation",
                    16000.0,
                    (
                        "Low: $5,000; middle: $16,000; high: $32,000. Fund "
                        "targeted outreach, attorney relationship work, property-market "
                        "materials, and source attribution without purchasing prohibited referrals."
                    ),
                ),
                (
                    "Delivery mobilization",
                    "$10,000 middle-plan allocation for contracted execution capacity",
                    10000.0,
                    (
                        "Low: $3,000; middle: $10,000; high: $20,000. Fund "
                        "contractor onboarding, field coordination, transaction setup, "
                        "and operator-paid listing preparation under documented scopes."
                    ),
                ),
                (
                    "Liquidity reserve",
                    "$12,000 middle-plan allocation for delays and operating continuity",
                    12000.0,
                    (
                        "Low: $3,000; middle: $12,000; high: $24,000. Preserve "
                        "cash for court delays and slow collections. With 4–18 "
                        "months to a first deal, test actual burn before hiring; "
                        "these reserves do not establish complete runway."
                    ),
                ),
            ],
        ),
        (
            "diag-08-thirty-day-launch-sprint",
            "timeline_roadmap",
            "Build Transaction Readiness in Thirty Days",
            "Four weekly milestones create a usable operating system, not instant closings.",
            12,
            "operating_framework",
            (
                "Numeric values indicate milestone end days. The 30-day sprint "
                "builds capability and an initial pipeline; the canonical "
                "4–18-month time to first deal remains the planning horizon."
            ),
            (
                "Finish the month with an authority-aware workflow, traceable "
                "opportunities, rehearsed transaction controls, and a cash-backed "
                "capacity plan. Do not count preparation activity as earned revenue."
            ),
            [
                (
                    "Days 1-7",
                    "Define jurisdiction, brokerage scope, and authority evidence",
                    7.0,
                    (
                        "Select one service geography; confirm licensing and supervision; "
                        "map local sale procedures with counsel. Build intake fields "
                        "for appointment documents, authority limits, notice requirements, "
                        "property occupancy, and source provenance."
                    ),
                ),
                (
                    "Days 8-14",
                    "Configure docket alerts and deduplicated opportunity records",
                    14.0,
                    (
                        "Configure permitted alerts, CRM ownership, and document access. "
                        "Review an initial 25 opportunity records for duplicate parcels, "
                        "incorrect representatives, and unsupported sale assumptions; "
                        "correct the workflow before expanding collection."
                    ),
                ),
                (
                    "Days 15-21",
                    "Rehearse the transaction path and contractor handoffs",
                    21.0,
                    (
                        "Run a synthetic estate sale through authority review, property "
                        "preparation, listing, notices, closing, and commission collection. "
                        "Test a family objection and a delayed hearing; verify that "
                        "both trigger a revised schedule and cash forecast."
                    ),
                ),
                (
                    "Days 22-30",
                    "Launch measured outreach and review economic readiness",
                    30.0,
                    (
                        "Begin targeted representative and attorney outreach using "
                        "applicable channel rules. Review cohort definitions, contractor "
                        "capacity, startup reserve, and retained-commission accounting. "
                        "Publish a weekly dashboard separating conversations, listings, "
                        "closings, collected revenue, and unresolved court dependencies."
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
