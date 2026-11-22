from __future__ import annotations

VOLUME_026_SUBTITLE = (
    "The Complete Playbook for $150,000–$1,000,000 USD in Annual Government "
    "Surplus Resale: Start with 2 FT + 3 C (5 People), Scale to 7"
)

VOLUME_026_POSITIONING_ALTERNATIVES = [
    {
        "title": "The Removal-Ready Surplus Operator",
        "subtitle": (
            "Turn federal and municipal surplus into collected B2B resale "
            "proceeds through disciplined bidding, scheduled removal, and "
            "documented asset condition."
        ),
        "audience": (
            "A two-full-time, three-contractor operating pod with "
            "$15,000–$80,000 in startup capital, dependable freight access, "
            "and practical experience inspecting commercial equipment."
        ),
        "research_basis": (
            "40 U.S.C. 545 and 41 CFR Part 102-38 establish the federal "
            "surplus-sale framework. Individual auction terms determine "
            "inspection access, payment obligations, and removal deadlines. "
            "The positioning emphasizes execution risk rather than assumed "
            "auction discounts; municipal sales require separate review "
            "of the seller's authority and published terms."
        ),
        "sources": [
            "https://www.law.cornell.edu/uscode/text/40/545",
            (
                "https://www.ecfr.gov/current/title-41/subtitle-C/"
                "chapter-102/subchapter-B/part-102-38"
            ),
            "https://gsaauctions.gov/",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Title-Ready Fleet Remarketer",
        "subtitle": (
            "Build a repeatable vehicle-and-trailer resale operation around "
            "VIN verification, SF-97 documentation, repair ceilings, and "
            "qualified business buyers."
        ),
        "audience": (
            "Fleet-service operators and equipment resellers with towing "
            "capacity, title-processing experience, and sufficient liquidity "
            "to carry vehicles through repair and registration delays."
        ),
        "research_basis": (
            "Federal disposal rules provide the sale framework, while state "
            "vehicle law controls dealer licensing and title-transfer duties. "
            "California Vehicle Code sections 11700 and 5900 illustrate "
            "separate licensing and transfer-notice requirements. An SF-97 "
            "supports an application for state title; it is not itself a "
            "state-issued title or proof of roadworthiness."
        ),
        "sources": [
            (
                "https://www.ecfr.gov/current/title-41/subtitle-C/"
                "chapter-102/subchapter-B/part-102-38"
            ),
            (
                "https://leginfo.legislature.ca.gov/faces/"
                "codes_displaySection.xhtml?sectionNum=11700.&lawCode=VEH"
            ),
            (
                "https://leginfo.legislature.ca.gov/faces/"
                "codes_displaySection.xhtml?sectionNum=5900.&lawCode=VEH"
            ),
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Buyer-Led Industrial Surplus Desk",
        "subtitle": (
            "Source unrestricted shop equipment and commercial fixtures "
            "against documented B2B demand, with landed-cost bid ceilings "
            "and explicit disposition plans."
        ),
        "audience": (
            "Industrial distributors, maintenance-service businesses, and "
            "small warehouse operators that already know local business "
            "buyers and can test equipment before remarketing."
        ),
        "research_basis": (
            "The federal sales framework supports disciplined asset "
            "selection, but surplus status does not remove export controls "
            "or contractual restrictions. 15 CFR 736.2 and 22 CFR 121.1 "
            "provide relevant export-control references. California Revenue "
            "and Taxation Code section 6071 supplies a concrete example "
            "of a state seller-permit requirement."
        ),
        "sources": [
            "https://www.law.cornell.edu/uscode/text/40/545",
            "https://www.law.cornell.edu/cfr/text/15/736.2",
            "https://www.law.cornell.edu/cfr/text/22/121.1",
            (
                "https://leginfo.legislature.ca.gov/faces/"
                "codes_displaySection.xhtml?sectionNum=6071.&lawCode=RTC"
            ),
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
]


def build_volume_026_diagrams_data() -> list[dict]:
    specs = [
        (
            "diag-01-surplus-to-collected-resale",
            "process_flow",
            "Buy the Exit Before You Buy the Lot",
            "Five operating stages from auction discovery to collected resale",
            1,
            "operating_framework",
            (
                "GSA Auctions, GovPlanet, GovDeals, and Public Surplus are "
                "discovery channels, not interchangeable sellers or uniform "
                "contract regimes. Verify the actual seller, governing sale "
                "terms, and asset restrictions for every lot. Revenue means "
                "the operator's gross resale proceeds, not auction-platform "
                "transaction volume."
            ),
            (
                "A low hammer price creates no profit until removal, "
                "condition, documentation, and buyer payment are resolved."
            ),
            [
                (
                    "Source qualified lots",
                    "Alerts plus buyer demand",
                    1.0,
                    (
                        "Configure auction alerts by equipment class, pickup "
                        "radius, closing date, and seller. Match each candidate "
                        "to recent resale evidence and named prospective "
                        "business buyers before requesting inspection."
                    ),
                ),
                (
                    "Inspect and price",
                    "Evidence-backed bid ceiling",
                    2.0,
                    (
                        "Record serial numbers, condition, title documents, "
                        "loading constraints, and removal deadlines. Set the "
                        "hammer ceiling from expected collected resale less "
                        "fees, freight, repairs, labor, carrying costs, "
                        "overhead allocation, and required profit."
                    ),
                ),
                (
                    "Bid and settle",
                    "Commit within funded limits",
                    3.0,
                    (
                        "Use a versioned bid-limit worksheet; reserve cash "
                        "for the full invoice and removal plan before bidding. "
                        "Validate payment instructions through the auction "
                        "account and seller contact details before sending "
                        "a bank payment."
                    ),
                ),
                (
                    "Remove and prepare",
                    "Document custody and condition",
                    4.0,
                    (
                        "Book the carrier within the contractual pickup "
                        "window. Photograph condition at release and receipt, "
                        "attach costs to the inventory record, and stop "
                        "repairs when the remaining resale contribution "
                        "falls below the approved floor."
                    ),
                ),
                (
                    "Remarket and collect",
                    "Close the asset-level ledger",
                    5.0,
                    (
                        "Publish tested specifications and disclosed defects, "
                        "execute the applicable title or bill-of-sale transfer, "
                        "verify payment receipt rather than screenshots, and "
                        "reconcile proceeds, direct costs, and inventory age."
                    ),
                ),
            ],
        ),
        (
            "diag-02-qualified-lot-conversion",
            "funnel",
            "Track One Cohort from Alert to Cash",
            "A nested 200-lot cohort with six completed resale collections",
            6,
            "illustrative_model",
            (
                "Illustrative 120-day observation window, not a forecast of "
                "market conversion rates or a promise of first-month sales. "
                "Every stage is a subset of the preceding stage; count each "
                "lot once. The canonical time to first deal remains "
                "1–6 months."
            ),
            (
                "The two awarded but uncollected lots remain inventory or "
                "unsettled dispositions; they do not become collected resale "
                "proceeds merely because an auction was won."
            ),
            [
                (
                    "Unique alerted lots",
                    "200 lots enter review",
                    200.0,
                    (
                        "Deduplicate reposted listings and capture seller, "
                        "asset class, location, closing date, and pickup "
                        "window. This is the complete cohort denominator."
                    ),
                ),
                (
                    "Desk-qualified lots",
                    "80 lots; 40% of alerts",
                    80.0,
                    (
                        "Retain only lots within the operating radius, capital "
                        "limit, permitted asset categories, and documented "
                        "buyer demand. Exclude inaccessible removal sites "
                        "and unresolved ownership restrictions."
                    ),
                ),
                (
                    "Inspection-cleared lots",
                    "24 lots; 30% of qualified",
                    24.0,
                    (
                        "Complete condition verification, document review, "
                        "transport quotations, and repair estimates. These "
                        "24 lots receive evidence-backed bid ceilings; "
                        "inspection expense also includes unsuccessful bids."
                    ),
                ),
                (
                    "Awarded and paid lots",
                    "8 lots; 33.3% of cleared",
                    8.0,
                    (
                        "Win eight lots without exceeding their ceilings "
                        "and settle their purchase invoices. Reject price "
                        "chasing; the other sixteen cleared lots consume "
                        "inspection effort but no acquisition principal."
                    ),
                ),
                (
                    "Resold and collected lots",
                    "6 lots; 75% of awarded",
                    6.0,
                    (
                        "Collect resale proceeds on six of the eight acquired "
                        "lots within the observation window. Overall "
                        "alert-to-collection conversion is 3%; track the "
                        "remaining two lots through inventory aging."
                    ),
                ),
            ],
        ),
        (
            "diag-03-base-case-profit-waterfall",
            "waterfall",
            "$575,000 Resale Proceeds Become $80,500 Owner Net",
            "Six bars reconcile the canonical Base-Case 14.0% net margin",
            3,
            "illustrative_model",
            (
                "USD per year. Opening and closing bars are totals; the four "
                "intermediate bars are negative cost movements. The scorecard "
                "fixes revenue and owner net, while the cost-category split "
                "is an illustrative operating budget. Direct handling and "
                "repair labor belong in their respective direct-cost "
                "categories; remaining operating labor belongs in overhead."
            ),
            (
                "$575,000 - $345,000 - $46,000 - $46,000 - $57,500 = "
                "$80,500; $80,500 / $575,000 = 14.0%. Sales tax collected "
                "for remittance is excluded from resale revenue."
            ),
            [
                (
                    "Gross resale proceeds",
                    "$575,000 opening total",
                    575000.0,
                    (
                        "Canonical Base-Case annual operator revenue from "
                        "owned surplus inventory resales. This is neither "
                        "client asset value nor a marketplace's aggregate "
                        "transaction volume."
                    ),
                ),
                (
                    "Inventory acquisition",
                    "-$345,000; 60% of revenue",
                    -345000.0,
                    (
                        "Allocate purchase prices, buyer premiums, and "
                        "nonrecoverable acquisition taxes to units sold. "
                        "Recoverable taxes are excluded; unsold inventory "
                        "remains a separate working-capital exposure."
                    ),
                ),
                (
                    "Transport and handling",
                    "-$46,000; 8% of revenue",
                    -46000.0,
                    (
                        "Include loading, rigging, carrier charges, fuel "
                        "surcharges, direct handling labor, and delivery "
                        "costs associated with completed resales. Missed "
                        "pickup windows can exhaust this entire allowance."
                    ),
                ),
                (
                    "Inspection and refurbishment",
                    "-$46,000; 8% of revenue",
                    -46000.0,
                    (
                        "Budget inspection effort, parts, testing, cleaning, "
                        "and repair-contractor labor. Include inspections "
                        "that produce no winning bid and avoid counting "
                        "the same labor again in overhead."
                    ),
                ),
                (
                    "Operating overhead",
                    "-$57,500; 10% of revenue",
                    -57500.0,
                    (
                        "Allocate remaining operating labor, storage, "
                        "insurance, software, selling and payment fees, "
                        "administration, and operating-loss allowances. "
                        "The monthly equivalent is $4,791.67, within the "
                        "canonical $3,000–$15,000 monthly opex range."
                    ),
                ),
                (
                    "Annual owner net profit",
                    "$80,500 closing total; 14.0%",
                    80500.0,
                    (
                        "Canonical Base-Case residual after the four expense "
                        "categories for a 2 FT + 3 C core pod (5 people). "
                        "External vendor and trade sub-crews are charged to "
                        "direct subcontractor/COGS pass-through within the "
                        "applicable direct-cost categories, not counted in "
                        "internal pod headcount. Owner distributions do not "
                        "create an additional expense below this closing total."
                    ),
                ),
            ],
        ),
        (
            "diag-04-sub-niche-direct-contribution",
            "horizontal_bars",
            "Compare Sub-Niches on the Same Cost Boundary",
            "Illustrative contribution before operating overhead, not net margin",
            2,
            "illustrative_model",
            (
                "Each bar assumes $10,000 of realized resale revenue. "
                "Direct costs include acquisition, transport, handling, "
                "inspection, and refurbishment; operating overhead, including "
                "selling and payment fees, is excluded. These percentages "
                "are planning hypotheses, not measured auction yields. "
                "An equal-revenue mix averages 24% direct contribution, "
                "matching the Base-Case before its 10% overhead allocation."
            ),
            (
                "A larger spread can conceal slower turnover, expensive "
                "removal, or unsold inventory. Validate each hypothesis "
                "with completed transactions before increasing bid limits."
            ),
            [
                (
                    "Office furniture bundles",
                    "16% direct contribution",
                    16.0,
                    (
                        "$10,000 resale less $8,400 direct cost leaves "
                        "$1,600 before overhead. Require confirmed loading "
                        "access and buyer measurements; bulky low-value "
                        "pieces can turn storage into the dominant cost."
                    ),
                ),
                (
                    "Commercial kitchen equipment",
                    "20% direct contribution",
                    20.0,
                    (
                        "$10,000 resale less $8,000 direct cost leaves "
                        "$2,000 before overhead. Verify power, gas, "
                        "refrigeration condition, and installation requirements; "
                        "unverified functionality can overwhelm repair limits."
                    ),
                ),
                (
                    "Fleet vehicles and trailers",
                    "24% direct contribution",
                    24.0,
                    (
                        "$10,000 resale less $7,600 direct cost leaves "
                        "$2,400 before overhead. Match VINs to sale "
                        "documents and confirm the state title pathway "
                        "before allowing transport or repair spending."
                    ),
                ),
                (
                    "Grounds-maintenance equipment",
                    "28% direct contribution",
                    28.0,
                    (
                        "$10,000 resale less $7,200 direct cost leaves "
                        "$2,800 before overhead. Inspect hydraulic systems, "
                        "hour meters, attachments, and seasonal demand; "
                        "missing proprietary components can erase the spread."
                    ),
                ),
                (
                    "Industrial shop equipment",
                    "32% direct contribution",
                    32.0,
                    (
                        "$10,000 resale less $6,800 direct cost leaves "
                        "$3,200 before overhead. Confirm rigging access, "
                        "three-phase power requirements, guarding condition, "
                        "and a credible buyer before bidding."
                    ),
                ),
            ],
        ),
        (
            "diag-05-pre-bid-statutory-risk-tree",
            "decision_tree",
            "Four Checks Before an Irrevocable Bid",
            "Proceed only when every branch has documented supporting evidence",
            5,
            "operating_framework",
            (
                "Read the four nodes sequentially: a documented pass moves "
                "to the next node; an unresolved issue stops the bid. "
                "Federal sale rules do not automatically govern municipal "
                "sales. California citations illustrate state-specific "
                "requirements and must be replaced or supplemented for "
                "the actual operating jurisdiction."
            ),
            (
                "Auction access, title evidence, restricted-property rules, "
                "and removal economics are separate checks; clearing one "
                "does not resolve the others."
            ),
            [
                (
                    "Seller authority and eligibility",
                    "Pass: eligible; stop: unresolved terms",
                    1.0,
                    (
                        "For federal lots, review 40 U.S.C. 545, 41 CFR "
                        "Part 102-38, and the specific sale terms. For "
                        "municipal lots, verify the seller's authority and "
                        "local conditions. Record bidder eligibility, "
                        "deposit requirements, payment deadlines, and "
                        "authorized purchasing identity."
                    ),
                ),
                (
                    "Ownership and title pathway",
                    "Pass: transferable; stop: document mismatch",
                    2.0,
                    (
                        "Match VIN or serial number to the sale record. "
                        "For federal vehicles, establish whether SF-97 or "
                        "another title document will be delivered and "
                        "whether the state accepts that pathway. Review "
                        "applicable dealer licensing and transfer duties, "
                        "including California Vehicle Code sections "
                        "11700 and 5900 when operating there."
                    ),
                ),
                (
                    "Restricted property and DEMIL",
                    "Pass: permitted; stop: unresolved restriction",
                    3.0,
                    (
                        "Review the listing's demilitarization instructions, "
                        "end-use terms, and controlled-property conditions. "
                        "Exclude lots whose obligations exceed documented "
                        "capability or authorization. Evaluate export "
                        "restrictions separately under 15 CFR 736.2 and "
                        "22 CFR 121.1 where applicable; an SF-97 does not "
                        "waive those restrictions."
                    ),
                ),
                (
                    "Permits, removal, and cash capacity",
                    "Pass: funded plan; stop: uncovered obligation",
                    4.0,
                    (
                        "Confirm applicable seller permits, resale-certificate "
                        "treatment, and tax collection obligations; California "
                        "Revenue and Taxation Code section 6071 is one "
                        "state example. Require carrier availability, site "
                        "access, insurance, repair limits, and sufficient "
                        "cash through the contractual removal deadline."
                    ),
                ),
            ],
        ),
        (
            "diag-06-five-to-seven-person-pod",
            "org_architecture",
            "Five Core Seats, Two Explicit Scale Additions",
            "Base: 2 FT + 3 C; scaled operation: 3 FT + 4 C",
            11,
            "operating_framework",
            (
                "FT means full-time and C means contractor. The first five "
                "seats form the Conservative and Base-Case pod; the final "
                "two seats are additions for the Scaled Small-Team "
                "scenario. Contractor headcount does not imply full-time "
                "hours, and seat descriptions do not set compensation."
            ),
            (
                "Conservative: $150,000 revenue × 8% = $12,000 owner net "
                "with five people. Base: $575,000 × 14% = $80,500 with "
                "five. Scaled: $1,000,000 × 20% = $200,000 with seven. "
                "All revenue is gross operator resale proceeds."
            ),
            [
                (
                    "FT 1: commercial owner",
                    "Core seat; bid and cash authority",
                    1.0,
                    (
                        "Own buyer demand, final bid ceilings, funding "
                        "allocation, seller exceptions, and inventory "
                        "markdown decisions. Review cash committed by "
                        "pickup deadline before authorizing another purchase."
                    ),
                ),
                (
                    "FT 2: inventory and remarketing lead",
                    "Core seat; asset-to-sale execution",
                    1.0,
                    (
                        "Maintain asset records, photograph condition, "
                        "coordinate preparation, publish listings, qualify "
                        "buyers, and verify fulfillment. Reconcile serial "
                        "numbers across receipt, repair, and sale documents."
                    ),
                ),
                (
                    "C 1: transport and rigging specialist",
                    "Core seat; removal execution",
                    1.0,
                    (
                        "Quote loading and freight before bidding, reserve "
                        "pickup capacity, document custody, and deliver "
                        "within site restrictions. Escalate missing forklifts, "
                        "access constraints, and loading damage immediately."
                    ),
                ),
                (
                    "C 2: inspection and repair technician",
                    "Core seat; condition and repair control",
                    1.0,
                    (
                        "Perform asset-class inspections, produce defect "
                        "estimates, execute bounded repairs, and record "
                        "test results. Seek a revised commercial decision "
                        "before exceeding the authorized repair ceiling."
                    ),
                ),
                (
                    "C 3: title and bookkeeping specialist",
                    "Core seat; documents and reconciliation",
                    1.0,
                    (
                        "Track title submissions, resale documentation, "
                        "tax records, purchase invoices, and bank receipts. "
                        "Separate tax liabilities, inventory cash, direct "
                        "costs, and overhead in the asset-level ledger."
                    ),
                ),
                (
                    "FT 3: operations lead",
                    "Scaled addition; sixth person",
                    1.0,
                    (
                        "Add dedicated scheduling, yard control, carrier "
                        "coordination, and cycle-time ownership when concurrent "
                        "lots exceed the core team's capacity. The "
                        "commercial owner retains final bid authority."
                    ),
                ),
                (
                    "C 4: field inspection specialist",
                    "Scaled addition; seventh person",
                    1.0,
                    (
                        "Expand inspection coverage without substituting "
                        "listing photographs for condition evidence. Use "
                        "standard test sheets and return inspection findings "
                        "before the bid worksheet is finalized."
                    ),
                ),
            ],
        ),
        (
            "diag-07-startup-capital-45000-reference",
            "stacked_comparison",
            "Protect Removal Cash in a $45,000 Startup Plan",
            "Four buckets: $15,000 lean, $45,000 reference, $80,000 expanded",
            4,
            "illustrative_model",
            (
                "Numeric values show the $45,000 central/reference startup "
                "budget in USD, within the canonical $15,000–$80,000 range. "
                "Each stage also provides its allocation at the $15,000 "
                "lean minimum and $80,000 expanded maximum. The allocation "
                "percentages are illustrative and sum to 100% at every "
                "capital level. Startup deployment is not annual revenue "
                "or annual expense."
            ),
            (
                "Lean: $9,000 + $2,250 + $1,500 + $2,250 = $15,000. "
                "Reference: $27,000 + $6,750 + $4,500 + $6,750 = $45,000. "
                "Expanded: $48,000 + $12,000 + $8,000 + $12,000 = $80,000."
            ),
            [
                (
                    "Acquisition working capital",
                    "60%; $27,000 reference allocation",
                    27000.0,
                    (
                        "Allocate $9,000 in the $15,000 lean plan, $27,000 "
                        "in the $45,000 reference plan, and $48,000 in the "
                        "$80,000 expanded plan. Cover hammer prices, premiums, "
                        "and acquisition cash obligations while limiting "
                        "concentration in any single lot or buyer segment."
                    ),
                ),
                (
                    "Removal and repair float",
                    "15%; $6,750 reference allocation",
                    6750.0,
                    (
                        "Allocate $2,250 in the $15,000 lean plan, $6,750 "
                        "in the $45,000 reference plan, and $12,000 in the "
                        "$80,000 expanded plan. Ring-fence loading, freight, "
                        "inspection, testing, and bounded repair payments "
                        "that fall due before resale collections."
                    ),
                ),
                (
                    "Facilities and operating setup",
                    "10%; $4,500 reference allocation",
                    4500.0,
                    (
                        "Allocate $1,500 in the $15,000 lean plan, $4,500 "
                        "in the $45,000 reference plan, and $8,000 in the "
                        "$80,000 expanded plan. Fund appropriately scaled "
                        "storage deposits, insurance setup, safety equipment, "
                        "inventory controls, and required business registrations."
                    ),
                ),
                (
                    "Liquidity and holding reserve",
                    "15%; $6,750 reference allocation",
                    6750.0,
                    (
                        "Allocate $2,250 in the $15,000 lean plan, $6,750 "
                        "in the $45,000 reference plan, and $12,000 in the "
                        "$80,000 expanded plan. Preserve cash for delayed "
                        "collections, additional storage, and operating "
                        "disruptions; calculate runway from actual monthly "
                        "burn rather than assuming six months are funded."
                    ),
                ),
            ],
        ),
        (
            "diag-08-thirty-day-launch-sprint",
            "timeline_roadmap",
            "Thirty Days to an Evidence-Backed Buying Operation",
            "Launch controls and buyer coverage before forcing a first purchase",
            12,
            "operating_framework",
            (
                "Milestones describe controllable setup work, not required "
                "sales outcomes. Canonical time to first deal is 1–6 months. "
                "If no lot passes the documented bid criteria, complete "
                "the sprint with a qualified watchlist and retained cash."
            ),
            (
                "Auction alerts, bid-limit worksheets, and inventory "
                "tracking support the operator; none replaces inspection, "
                "title verification, removal capacity, or buyer demand."
            ),
            [
                (
                    "Days 1-7",
                    "Define scope and operating constraints",
                    7.0,
                    (
                        "Choose two initial asset classes and a pickup "
                        "radius. Review seller terms and applicable permits, "
                        "create a restricted-property exclusion list, and "
                        "obtain storage, insurance, and carrier quotations. "
                        "Deliver a written buying mandate and capital budget."
                    ),
                ),
                (
                    "Days 8-14",
                    "Build buyer evidence and unit economics",
                    14.0,
                    (
                        "Interview ten prospective business buyers and "
                        "document specifications, delivery constraints, and "
                        "payment practices. Configure GSA Auctions, GovPlanet, "
                        "GovDeals, and Public Surplus alerts. Price five "
                        "candidate lots using resale evidence and complete "
                        "landed-cost bid worksheets."
                    ),
                ),
                (
                    "Days 15-21",
                    "Validate condition and removal execution",
                    21.0,
                    (
                        "Arrange inspections for up to three qualified "
                        "lots when access is available. Resolve title "
                        "documents, obtain written freight estimates, assign "
                        "pod responsibilities, and test inventory records. "
                        "Bid only when the four pre-flight checks pass."
                    ),
                ),
                (
                    "Days 22-30",
                    "Execute conditionally and review the cohort",
                    30.0,
                    (
                        "If awarded a qualifying lot, settle and remove "
                        "it on the seller's timetable, record actual "
                        "condition, and begin buyer outreach. Otherwise "
                        "continue qualification. Review cash commitments, "
                        "inspection losses, inventory aging, and expected "
                        "versus actual landed costs."
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
                    numeric_value=float(numeric_value),
                    detail=detail,
                )
                for label, value, numeric_value, detail in stages
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
