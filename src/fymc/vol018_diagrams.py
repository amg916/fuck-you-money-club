from __future__ import annotations

VOLUME_018_SUBTITLE = (
    "The Complete Playbook for $200,000–$1,500,000 USD in Annual Land Sales: "
    "Launch with 1 FT + 3 C (4 People), Scale to 2 FT + 4 C"
)

VOLUME_018_POSITIONING_ALTERNATIVES = [
    {
        "title": "Access First, Acquisition Second",
        "subtitle": (
            "Build a vacant-land trading operation around documented legal access, "
            "parcel-level GIS screening, and title-insured dispositions."
        ),
        "audience": (
            "Owner-operators buying rural vacant parcels with a four-person pod "
            "and enough working capital to hold inventory through slow exits."
        ),
        "research_basis": (
            "USGS mapping and FEMA flood mapping support desktop screening, "
            "but neither establishes ownership, legal access, or buildability. "
            "42 U.S.C. § 9601(35) and 40 CFR Part 312 describe environmental "
            "inquiry requirements relevant to certain CERCLA liability protections. "
            "This positioning centers documented evidence before acquisition; "
            "the cited sources establish requirements and screening resources, "
            "not customer demand or achievable investment returns."
        ),
        "sources": [
            "https://www.usgs.gov/programs/national-geospatial-program/national-map",
            "https://msc.fema.gov/portal/home",
            "https://www.law.cornell.edu/uscode/text/42/9601",
            "https://www.ecfr.gov/current/title-40/chapter-I/subchapter-J/part-312",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "Infill Without Entitlement Guesswork",
        "subtitle": (
            "Trade vacant infill parcels and approved minor subdivisions using "
            "written zoning findings, utility evidence, and verified legal lots."
        ),
        "audience": (
            "Experienced real-estate operators working in one county or metro "
            "where planning records, utility providers, and comparable sales "
            "can be checked before earnest money becomes exposed."
        ),
        "research_basis": (
            "California Government Code §§ 66424 and 66428 illustrate why "
            "division of land and parcel-map requirements require specific "
            "jurisdictional analysis. California Business and Professions Code "
            "§ 11010 establishes notice requirements for covered subdivided-land "
            "offerings, subject to applicable exemptions. These California "
            "examples support a jurisdiction-specific operating method rather "
            "than a nationwide assumption that small splits are exempt."
        ),
        "sources": [
            (
                "https://leginfo.legislature.ca.gov/faces/"
                "codes_displaySection.xhtml?lawCode=GOV&sectionNum=66424."
            ),
            (
                "https://leginfo.legislature.ca.gov/faces/"
                "codes_displaySection.xhtml?lawCode=GOV&sectionNum=66428."
            ),
            (
                "https://leginfo.legislature.ca.gov/faces/"
                "codes_displaySection.xhtml?lawCode=BPC&sectionNum=11010."
            ),
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Four-Person Land Trading Desk",
        "subtitle": (
            "Separate principal trading, licensed representation, title work, "
            "and parcel diligence while controlling inventory cash exposure."
        ),
        "audience": (
            "Capitalized specialists running one full-time owner and three "
            "contract seats, with expansion tied to completed sales rather "
            "than the number of parcels under contract."
        ),
        "research_basis": (
            "California Business and Professions Code §§ 10130–10131 illustrate "
            "licensing boundaries for compensated real-estate activities "
            "performed for others. CERCLA owner-liability provisions under "
            "42 U.S.C. § 9607 support assigning environmental diligence before "
            "taking title. These sources inform role boundaries and acquisition "
            "controls; the four-person staffing model and revenue scenarios "
            "remain supplied operating assumptions."
        ),
        "sources": [
            (
                "https://leginfo.legislature.ca.gov/faces/"
                "codes_displaySection.xhtml?lawCode=BPC&sectionNum=10130."
            ),
            (
                "https://leginfo.legislature.ca.gov/faces/"
                "codes_displaySection.xhtml?lawCode=BPC&sectionNum=10131."
            ),
            "https://www.law.cornell.edu/uscode/text/42/9607",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
]


def build_volume_018_diagrams_data() -> list[dict]:
    specs = [
        (
            "diag-01-evidence-to-title-insured-exit",
            "process_flow",
            "Buy the Evidence Before Buying the Parcel",
            "Five operating stages for vacant land, infill, and minor subdivisions",
            1,
            "operating_framework",
            (
                "The operator trades owned inventory as principal. Annual revenue "
                "means gross parcel sale proceeds, with acquisition costs included "
                "in the net-margin calculation. Desktop GIS results are screening "
                "evidence, not proof of access, boundaries, or development rights."
            ),
            (
                "Keep one parcel evidence packet from initial screening through "
                "recorded acquisition and insured disposition; unresolved fatal "
                "defects stop the purchase before capital becomes trapped."
            ),
            [
                (
                    "Screen the parcel",
                    "GIS and comparable sales",
                    1.0,
                    (
                        "Join county assessor records to QGIS parcel layers, FEMA "
                        "flood mapping, terrain, and recorded comparable sales. "
                        "Flag landlocked geometry, steep slopes, suspect lot lines, "
                        "and asking prices unsupported by completed transactions."
                    ),
                ),
                (
                    "Verify the rights",
                    "Access, title, and use",
                    1.0,
                    (
                        "Obtain the title commitment and exception documents; "
                        "verify deeded access, easement scope, legal-lot status, "
                        "zoning, utility availability, and environmental history. "
                        "A visible road or neighboring house proves neither "
                        "legal access nor permission to build."
                    ),
                ),
                (
                    "Price and contract",
                    "Exit value less every cost",
                    1.0,
                    (
                        "Set the acquisition ceiling from defensible resale value "
                        "less acquisition expense, diligence, selling expense, "
                        "carry, and target profit. Preserve inspection rights "
                        "and tie deposits to explicit termination dates."
                    ),
                ),
                (
                    "Close and prepare",
                    "Insured acquisition and evidence",
                    1.0,
                    (
                        "Use a title or escrow provider to resolve closing "
                        "requirements and record the deed. Complete only scoped "
                        "survey, access, cleanup, or subdivision work supported "
                        "by permits, written estimates, and the resale thesis."
                    ),
                ),
                (
                    "Sell and reconcile",
                    "Recorded exit and released cash",
                    1.0,
                    (
                        "Publish substantiated parcel facts through suitable land "
                        "channels or a licensed broker, close with title insurance, "
                        "and reconcile settlement proceeds against parcel costs. "
                        "Track days held, realized margin, and cash released."
                    ),
                ),
            ],
        ),
        (
            "diag-02-annual-parcel-cohort-conversion",
            "funnel",
            "From 10,000 Screened Parcels to 17 Completed Exits",
            "One nested annual cohort supporting the mature Base-Case model",
            6,
            "illustrative_model",
            (
                "Each stage is a subset of the preceding stage and counts unique "
                "parcel opportunities, not emails, owner contacts, or repeat offers. "
                "This illustrative mature-year cohort assumes its 17 acquisitions "
                "also resell within the modeled year at $50,000 each. Actual "
                "acquisition and disposition cohorts can cross reporting years."
            ),
            (
                "17 completed parcel sales × $50,000 = $850,000 gross annual "
                "revenue. This is a steady-state illustration, not a first-month "
                "closing target; time to first deal remains 3–9 months."
            ),
            [
                (
                    "Parcels screened",
                    "10,000 unique opportunities",
                    10000,
                    (
                        "Deduplicate assessor parcel identifiers and remove "
                        "public land, incompatible parcel sizes, and obvious "
                        "geographic mismatches. This starting population supplies "
                        "the denominator for the complete conversion funnel."
                    ),
                ),
                (
                    "Desktop-qualified parcels",
                    "2,000 parcels; 20% advance",
                    2000,
                    (
                        "Retain parcels with plausible access, usable terrain, "
                        "supporting sale comparables, and an identifiable owner. "
                        "Desktop qualification does not replace title review "
                        "or establish environmental suitability."
                    ),
                ),
                (
                    "Seller-engaged parcels",
                    "400 parcels; 20% advance",
                    400,
                    (
                        "Count an opportunity only after the owner or authorized "
                        "representative responds substantively about that parcel. "
                        "Record price expectations, ownership authority, timing, "
                        "and disclosed property issues before preparing terms."
                    ),
                ),
                (
                    "Written offers issued",
                    "100 parcels; 25% advance",
                    100,
                    (
                        "Issue written offers only where preliminary economics "
                        "survive transaction expenses and holding costs. Maintain "
                        "one cohort entry per parcel even when price or "
                        "inspection terms are revised."
                    ),
                ),
                (
                    "Acquired and resold",
                    "17 parcels; 17% advance",
                    17,
                    (
                        "Complete diligence, insured acquisition, and subsequent "
                        "sale for 17 parcels: 0.17% of the original cohort. "
                        "Count gross completed-sale proceeds rather than pending "
                        "contracts, listing prices, or unrealized appreciation."
                    ),
                ),
            ],
        ),
        (
            "diag-03-base-case-owner-profit-waterfall",
            "waterfall",
            "$850,000 Gross Sales to $157,250 Owner Net",
            "Six bars reconcile exactly to the Base-Case 18.5% net margin",
            3,
            "illustrative_model",
            (
                "USD per mature operating year. The first bar opens the balance, "
                "the next four bars are signed deductions, and the sixth bar "
                "is the closing total rather than another additive movement. "
                "Cost allocations are illustrative; gross revenue, margin, and "
                "owner net match the supplied scorecard. Owner net is the modeled "
                "business residual before personal income tax; no separate "
                "owner salary is deducted in this illustration."
            ),
            (
                "$850,000 − $510,000 − $42,500 − $55,250 − $85,000 = "
                "$157,250; $157,250 ÷ $850,000 = 18.5%. Acquisition cost is "
                "an expense in this bridge, not an amount omitted from revenue."
            ),
            [
                (
                    "Gross parcel sales",
                    "$850,000 opening balance",
                    850000,
                    (
                        "Recognize the model's gross completed parcel sale "
                        "proceeds: 17 exits averaging $50,000. This principal "
                        "trading model does not substitute broker commissions "
                        "or third-party transaction volume for operator revenue."
                    ),
                ),
                (
                    "Parcel acquisition basis",
                    "−$510,000; 60.0% of sales",
                    -510000,
                    (
                        "Allocate $30,000 average purchase price to each of "
                        "17 sold parcels. Match inventory basis to completed "
                        "sales; cash spent on parcels still held at year-end "
                        "is not automatically a current-year sale expense."
                    ),
                ),
                (
                    "Diligence and preparation",
                    "−$42,500; 5.0% of sales",
                    -42500,
                    (
                        "Allow $2,500 per sold parcel for survey work, "
                        "environmental screening, zoning verification, and limited "
                        "site preparation. Specialist investigations or major "
                        "entitlements require a separate acquisition budget."
                    ),
                ),
                (
                    "Closing and selling",
                    "−$55,250; 6.5% of sales",
                    -55250,
                    (
                        "Allow $3,250 per sold parcel for allocated acquisition "
                        "and disposition settlement charges, title costs, "
                        "transaction-linked marketing, and applicable brokerage. "
                        "Exclude these items from overhead to prevent double counting."
                    ),
                ),
                (
                    "Carry and operating expense",
                    "−$85,000; 10.0% of sales",
                    -85000,
                    (
                        "Combine $25,000 annual parcel carry and financing "
                        "expense with $60,000 recurring operating expense. "
                        "The latter equals $5,000 monthly for contract capacity, "
                        "screening systems, outreach, and administration."
                    ),
                ),
                (
                    "Annual owner net",
                    "$157,250 closing total",
                    157250,
                    (
                        "The final residual is 18.5% of gross sales after "
                        "all four modeled expense groups. Render this bar "
                        "from zero as the ending total, not as an "
                        "additional increase to the running balance."
                    ),
                ),
            ],
        ),
        (
            "diag-04-parcel-strategy-spread-yields",
            "horizontal_bars",
            "Compare Acquisition-Spread Yields, Not Listing Hype",
            "Five independent parcel examples with the same $50,000 sale price",
            2,
            "illustrative_model",
            (
                "Each numeric value is gross acquisition spread as a percentage "
                "of sale price: (sale price − purchase price) ÷ sale price. "
                "These illustrative yields exclude diligence, preparation, closing, "
                "selling, carry, and overhead; they are neither net margins nor "
                "annualized returns. Examples are independent alternatives, "
                "not a weighted portfolio or observed market ranking."
            ),
            (
                "A wide acquisition spread can disappear through access repairs, "
                "utility extensions, septic failure, or delayed approvals. "
                "The 40% example matches the Base-Case spread before its "
                "remaining 21.5 percentage points of modeled expenses."
            ),
            [
                (
                    "Accessible rural acreage",
                    "40% gross spread",
                    40,
                    (
                        "$50,000 resale less $30,000 purchase leaves $20,000 "
                        "before other costs. Verify recorded access and actual "
                        "road condition; a cheap landlocked parcel does not "
                        "become attractive through a larger spreadsheet spread."
                    ),
                ),
                (
                    "Utility-served infill lot",
                    "35% gross spread",
                    35,
                    (
                        "$50,000 resale less $32,500 purchase leaves $17,500 "
                        "before other costs. Confirm connection capacity, tap "
                        "fees, setbacks, and legal-lot status; a utility line "
                        "near the boundary is insufficient evidence."
                    ),
                ),
                (
                    "Septic-dependent homesite",
                    "30% gross spread",
                    30,
                    (
                        "$50,000 resale less $35,000 purchase leaves $15,000 "
                        "before other costs. Obtain the local authority's "
                        "required soil and wastewater findings before representing "
                        "the parcel as suitable for residential construction."
                    ),
                ),
                (
                    "Approved minor-split lot",
                    "25% gross spread",
                    25,
                    (
                        "$50,000 resale less $37,500 allocated purchase basis "
                        "leaves $12,500 before other costs. This example assumes "
                        "an approved, legally created lot; unresolved split "
                        "applications require separate timing and expense scenarios."
                    ),
                ),
                (
                    "Recreational-use parcel",
                    "20% gross spread",
                    20,
                    (
                        "$50,000 resale less $40,000 purchase leaves $10,000 "
                        "before other costs. Verify lawful recreational uses, "
                        "seasonal access, and restrictions; narrow buyer demand "
                        "can make even modest carrying costs decisive."
                    ),
                ),
            ],
        ),
        (
            "diag-05-acquisition-statutory-risk-decisions",
            "decision_tree",
            "Four Questions Before Acquisition Cash Leaves Escrow",
            "Proceed on evidence; cure or reject material unresolved defects",
            5,
            "operating_framework",
            (
                "Read the four nodes sequentially. An affirmative, documented "
                "finding advances to the next node; an adverse or incomplete "
                "finding routes to a documented cure or rejection before closing. "
                "Federal environmental rules and California statutory examples "
                "serve different purposes; apply the actual property's state "
                "and local requirements rather than exporting California rules."
            ),
            (
                "Title insurance, a clean-looking map, and a low purchase price "
                "answer different questions. None independently establishes "
                "legal access, permitted use, environmental suitability, "
                "or authority to represent another seller."
            ),
            [
                (
                    "Title and access",
                    "Document rights or stop",
                    1.0,
                    (
                        "Review vesting, liens, taxes, recorded easements, "
                        "surveys, and commitment exceptions with the title "
                        "provider and counsel. Require access rights adequate "
                        "for the intended use; cure defects before closing "
                        "or reject the parcel rather than assume coverage."
                    ),
                ),
                (
                    "Zoning and legal division",
                    "Confirm the lawful parcel",
                    1.0,
                    (
                        "Obtain jurisdiction-specific findings on legal-lot "
                        "status, setbacks, minimum area, and proposed division. "
                        "For California examples, review Government Code "
                        "§§ 66424 and 66428 and applicable local ordinances; "
                        "an assessor parcel identifier alone proves no split approval."
                    ),
                ),
                (
                    "Environmental constraints",
                    "Investigate before taking title",
                    1.0,
                    (
                        "Evaluate contamination under 42 U.S.C. § 9607 and "
                        "applicable inquiry requirements under 40 CFR Part 312. "
                        "Check flood exposure and potential jurisdictional waters; "
                        "discharges of dredged or fill material may require "
                        "authorization under 33 U.S.C. § 1344."
                    ),
                ),
                (
                    "Representation and disclosures",
                    "Verify role and offering rules",
                    1.0,
                    (
                        "Distinguish owned-inventory sales from compensated "
                        "representation of others. California examples include "
                        "Business and Professions Code §§ 10130–10131 for "
                        "licensing and § 11010 for covered subdivided-land "
                        "offerings. Verify exemptions, required reports, and "
                        "property-specific disclosures before solicitation or sale."
                    ),
                ),
            ],
        ),
        (
            "diag-06-four-person-land-trading-pod",
            "org_architecture",
            "One Accountable Owner, Three Contract Specialists",
            "Base pod: 1 FT + 3 C; scaled pod: 2 FT + 4 C",
            11,
            "operating_framework",
            (
                "The four displayed seats are people in the Conservative and "
                "Base-Case pod; C means contractor, not full-time equivalent. "
                "The scaled six-person pod adds one full-time operations lead "
                "and one contract field coordinator. Title, escrow, survey, "
                "environmental, and legal firms are transaction vendors outside "
                "this pod headcount; applicable fees remain in modeled expenses."
            ),
            (
                "The owner controls capital allocation and final purchase terms. "
                "Specialists supply parcel evidence and transaction execution; "
                "automation accelerates screening without deciding title, "
                "access, zoning, or environmental conclusions."
            ),
            [
                (
                    "Owner and investment lead",
                    "1 full-time seat",
                    1,
                    (
                        "Own acquisition ceilings, liquidity limits, offer terms, "
                        "and exit decisions. Review held inventory weekly, "
                        "reconcile parcel-level profit after settlement, and "
                        "retain accountability when adding the scaled operations lead."
                    ),
                ),
                (
                    "GIS and comparable-sales analyst",
                    "1 contract seat",
                    1,
                    (
                        "Maintain QGIS screening layers, assessor extracts, "
                        "recorded-sale comparisons, and evidence timestamps. "
                        "Automate duplicate detection and comparable-sale tracking; "
                        "escalate mismatched boundaries, unsupported access, "
                        "and stale valuations to the owner."
                    ),
                ),
                (
                    "Transaction coordinator",
                    "1 contract seat",
                    1,
                    (
                        "Track inspection deadlines, title requirements, vendor "
                        "deliverables, escrow documents, and settlement reconciliations. "
                        "Route title opinions to counsel and coverage questions "
                        "to the insurer; coordination does not confer authority "
                        "to provide regulated professional services."
                    ),
                ),
                (
                    "Licensed disposition specialist",
                    "1 contract seat",
                    1,
                    (
                        "Use an appropriately licensed professional where "
                        "representation requires it. Manage substantiated listings, "
                        "buyer qualification, feedback, and closing coordination. "
                        "At scaled volume, the added field coordinator handles "
                        "site visits and vendor scheduling rather than brokerage."
                    ),
                ),
            ],
        ),
        (
            "diag-07-forty-five-thousand-dollar-startup-stack",
            "stacked_comparison",
            "Allocate a $45,000 Reference Budget Before the First Offer",
            "Four capital buckets: $15,000 lean, $45,000 reference, $75,000 expanded",
            4,
            "illustrative_model",
            (
                "Numeric values represent the $45,000 central startup plan "
                "inside the canonical $15,000–$75,000 USD capital range. "
                "Each bucket also states its lean and expanded allocations; "
                "these are alternative budgets, not additive funding sources. "
                "Values are capital allocations, not annual expenses or recognized "
                "revenue. Acquisition capital remains inventory until disposition; "
                "unused reserves remain cash. Startup parcel prices must fit "
                "available cash rather than assume the mature Base-Case purchase "
                "price. Recycling sale proceeds is required to support annual "
                "purchases above the initial inventory bucket."
            ),
            (
                "Lean: $6,000 + $1,500 + $1,500 + $6,000 = $15,000. "
                "Reference: $24,000 + $4,500 + $1,500 + $15,000 = $45,000. "
                "Expanded: $42,000 + $7,500 + $3,000 + $22,500 = $75,000. "
                "The reference operating reserve covers three months at $5,000 "
                "monthly, not the entire 3–9 month first-deal window under "
                "every timing outcome."
            ),
            [
                (
                    "Parcel purchase capital",
                    "Lean $6,000; reference $24,000; expanded $42,000",
                    24000,
                    (
                        "Allocate $6,000 in the $15,000 lean plan, $24,000 in "
                        "the $45,000 reference plan, or $42,000 in the $75,000 "
                        "expanded plan to purchase prices and deposits credited "
                        "against those prices. The reference bucket cannot fund "
                        "the mature Base-Case $30,000 average purchase outright; "
                        "target lower-priced inventory without consuming reserves. "
                        "Do not count pending sales as available acquisition cash."
                    ),
                ),
                (
                    "Diligence and preparation",
                    "Lean $1,500; reference $4,500; expanded $7,500",
                    4500,
                    (
                        "Allocate $1,500 in the $15,000 lean plan, $4,500 in "
                        "the $45,000 reference plan, or $7,500 in the $75,000 "
                        "expanded plan to surveys, environmental work, land-use "
                        "verification, and narrowly scoped preparation. Track "
                        "failed-deal investigation costs separately from successful "
                        "parcel basis, and stop spending when a fatal defect "
                        "emerges. Reject or separately fund scopes exceeding "
                        "the available diligence allocation."
                    ),
                ),
                (
                    "Closing and carrying liquidity",
                    "Lean $1,500; reference $1,500; expanded $3,000",
                    1500,
                    (
                        "Allocate $1,500 in the $15,000 lean plan, $1,500 in "
                        "the $45,000 reference plan, or $3,000 in the $75,000 "
                        "expanded plan to settlement charges, property taxes, "
                        "insurance, and parcel-specific carrying bills before "
                        "sales replenish cash. Confirm transaction-specific costs "
                        "before committing capital. Do not also allocate this "
                        "same cash to recurring contractor or software invoices."
                    ),
                ),
                (
                    "Operating runway",
                    "Lean $6,000; reference $15,000; expanded $22,500",
                    15000,
                    (
                        "Allocate $6,000 in the $15,000 lean plan, $15,000 in "
                        "the $45,000 reference plan, or $22,500 in the $75,000 "
                        "expanded plan to recurring operations. Lean runway is "
                        "two months at $3,000 monthly; reference and expanded "
                        "runway are three and 4.5 months at $5,000 monthly. "
                        "The canonical monthly range is $3,000–$15,000, and time "
                        "to first deal is 3–9 months; resale cash may arrive later. "
                        "These reserves do not guarantee funding through exit. "
                        "Close any projected cash shortfall before committing "
                        "to purchases by reducing spending or securing funding."
                    ),
                ),
            ],
        ),
        (
            "diag-08-thirty-day-land-desk-launch",
            "timeline_roadmap",
            "Build the Acquisition System in 30 Days",
            "Four weekly deliverables; first-deal timing remains 3–9 months",
            12,
            "operating_framework",
            (
                "Numeric values are cumulative milestone days: 7, 14, 21, and 30. "
                "This sprint establishes operating readiness and a measured "
                "pipeline, not a promised closing. Canonical annual scenarios "
                "are Conservative: $200,000 gross × 12% = $24,000 owner net "
                "with 1 FT + 3 C; Base-Case: $850,000 gross × 18.5% = "
                "$157,250 owner net with 1 FT + 3 C; Scaled Small-Team: "
                "$1,500,000 gross × 25% = $375,000 owner net with 2 FT + 4 C."
            ),
            (
                "Advance by completed evidence and funded obligations. "
                "Illiquidity, absent legal access, and environmental constraints "
                "can defeat attractive headline spreads before the first resale."
            ),
            [
                (
                    "Days 1-7",
                    "Select market and capital limits",
                    7,
                    (
                        "Choose one county and parcel thesis, assemble recorded "
                        "sale comparables, and document zoning and subdivision "
                        "contacts. Set maximum cash exposure per parcel, "
                        "minimum operating runway, and the four startup "
                        "capital allocations before soliciting sellers."
                    ),
                ),
                (
                    "Days 8-14",
                    "Build the screening evidence chain",
                    14,
                    (
                        "Configure QGIS parcel layers, assessor-record imports, "
                        "comparable-sale tracking, and a parcel evidence checklist. "
                        "Screen an initial 250 unique parcels and manually "
                        "inspect 25 records for mapping, ownership, and "
                        "sale-comparison errors before increasing throughput."
                    ),
                ),
                (
                    "Days 15-21",
                    "Test outreach and transaction support",
                    21,
                    (
                        "Contact a measured subset of qualified owners and "
                        "record parcel-level responses rather than message "
                        "counts. Obtain title-provider terms, survey quotes, "
                        "and specialist availability; prepare written offer "
                        "forms and jurisdiction-specific disclosure checklists."
                    ),
                ),
                (
                    "Days 22-30",
                    "Review offers and funded runway",
                    30,
                    (
                        "Underwrite responsive opportunities, issue only offers "
                        "supported by evidence, and schedule inspection deadlines. "
                        "Reconcile funnel counts, committed cash, remaining runway, "
                        "and open defects; carry incomplete investigations "
                        "forward without treating unsigned or unclosed deals "
                        "as revenue."
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
