from __future__ import annotations

VOLUME_024_SUBTITLE = (
    "The Complete Playbook for Tax Lien Investing: "
    "$15,000–$180,000 USD in Annual Realized Revenue, "
    "a 1 FT + 2 C Core Pod (3 People), and a 5-Person Scale Model"
)

VOLUME_024_POSITIONING_ALTERNATIVES = [
    {
        "title": "Buy the Lien, Price the Wait",
        "subtitle": (
            "Build a certificate portfolio around auction bid-down math, "
            "redemption timing, and realized interest rather than advertised rates."
        ),
        "audience": (
            "Capital-backed owner-operators deploying $100,000–$1,500,000 USD "
            "with a full-time principal and contracted title and legal specialists."
        ),
        "research_basis": (
            "Florida Statutes sections 197.432 and 197.472 and Arizona Revised "
            "Statutes sections 42-18114 and 42-18153 establish distinct auction "
            "and redemption mechanics. Compare actual bid rates, eligible "
            "interest bases, redemption dates, and unrecovered transaction costs; "
            "do not treat a statutory ceiling as the portfolio's earned yield."
        ),
        "sources": [
            "https://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0100-0199/0197/Sections/0197.432.html",
            "https://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0100-0199/0197/Sections/0197.472.html",
            "https://www.azleg.gov/ars/42/18114.htm",
            "https://www.azleg.gov/ars/42/18153.htm",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Three-Person Redemption Desk",
        "subtitle": (
            "Run auction screening and redemption tracking with one full-time "
            "principal, one title contractor, and one local counsel contractor."
        ),
        "audience": (
            "Small investment partnerships that need disciplined parcel records, "
            "cash reconciliation, and statutory calendars before expanding headcount."
        ),
        "research_basis": (
            "Florida Statutes section 197.502 and Arizona Revised Statutes "
            "section 42-18201 distinguish certificate ownership from later "
            "enforcement procedures. A parcel-level calendar, documented title "
            "review, and counsel-owned notices support the core pod; automation "
            "organizes evidence but does not establish title or clear a stay "
            "under 11 U.S.C. section 362."
        ),
        "sources": [
            "https://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0100-0199/0197/Sections/0197.502.html",
            "https://www.azleg.gov/ars/42/18201.htm",
            "https://www.law.cornell.edu/uscode/text/11/362",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "Redemption First, Equity Intact",
        "subtitle": (
            "Separate certificate interest, redeemable-deed premiums, and property "
            "disposition gains while engineering lawful surplus handling after Tyler."
        ),
        "audience": (
            "Experienced property investors comparing certificate purchases with "
            "redeemable deeds and budgeting for title defects and delayed exits."
        ),
        "research_basis": (
            "Texas Tax Code section 34.21 supplies property-specific redemption "
            "periods and payment formulas rather than ordinary certificate "
            "interest. Tyler v. Hennepin County, 598 U.S. 631 (2023), addresses "
            "government retention of value beyond the tax debt; it does not "
            "create one nationwide private-investor foreclosure procedure. "
            "Federal tax liens also require analysis under 26 U.S.C. section 7425."
        ),
        "sources": [
            "https://statutes.capitol.texas.gov/Docs/TX/htm/TX.34.htm#34.21",
            "https://www.law.cornell.edu/supremecourt/text/21-166",
            "https://www.law.cornell.edu/uscode/text/26/7425",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
]


def build_volume_024_diagrams_data() -> list[dict]:
    specs = [
        (
            "diag-01-certificate-to-realized-cash",
            "process_flow",
            "From County Inventory to Realized Cash",
            "Five operating steps keep invested principal separate from earnings.",
            1,
            "operating_framework",
            (
                "Applies to statutory certificates and separately classified "
                "redeemable deeds. County procedures control execution. The "
                "canonical time to first deal is 6–36 months; completing research "
                "or registering for an auction does not establish an earned return."
            ),
            (
                "Track each parcel from original county record through bank "
                "settlement. Returned principal replenishes investment capital; "
                "only realized interest, penalties, and disposition gains enter "
                "the revenue scorecard."
            ),
            [
                (
                    "Source official inventory",
                    "County records before auction marketing",
                    1,
                    (
                        "Download the county treasurer or tax collector sale "
                        "file, preserve its publication date, and cross-check "
                        "parcel identifiers against assessor GIS and recorder "
                        "records. Record whether the asset is a certificate or "
                        "a redeemable deed."
                    ),
                ),
                (
                    "Underwrite parcel and procedure",
                    "Title, access, value, and statutory clock",
                    2,
                    (
                        "Have the title contractor review recorded interests, "
                        "access, parcel usability, and competing taxes. Local "
                        "counsel maps redemption and enforcement requirements; "
                        "PACER checks support bankruptcy review under 11 U.S.C. "
                        "section 362."
                    ),
                ),
                (
                    "Price and acquire",
                    "Bid ceiling includes trapped-cash exposure",
                    3,
                    (
                        "Model the actual interest-bearing base, auction premium, "
                        "fees, subsequent taxes, and collection delay. Apply the "
                        "auction's bid-down or premium rules rather than bidding "
                        "from a headline statutory rate."
                    ),
                ),
                (
                    "Service and reconcile",
                    "Track redemption without counting accruals",
                    4,
                    (
                        "Use a SQLite parcel register and scheduled calendar "
                        "alerts for receipts, statutory dates, and subsequent "
                        "tax decisions. Match county statements to bank activity "
                        "and flag overdue events for human review."
                    ),
                ),
                (
                    "Redeem or resolve",
                    "Separate principal, earnings, costs, and surplus",
                    5,
                    (
                        "Post returned principal to the investment ledger and "
                        "realized earnings to revenue. Route nonredemption "
                        "through counsel-led enforcement or loss resolution; "
                        "a property transfer alone is not a realized disposition "
                        "gain, and restricted surplus is not operator revenue."
                    ),
                ),
            ],
        ),
        (
            "diag-02-auction-underwriting-cohort",
            "funnel",
            "A Narrowing Auction Cohort",
            "One acquisition cohort, five nested stages, and explicit rejection.",
            6,
            "illustrative_model",
            (
                "Illustrative counts represent the same candidate pool, not "
                "historical conversion evidence. Every later stage is a subset "
                "of the preceding stage. Twenty acquisitions at an average "
                "$37,500 all-in basis use the $750,000 acquisition bucket in "
                "the $1,000,000 capital illustration; this is not a 30-day target."
            ),
            (
                "Screening automation reduces manual review volume. It does not "
                "turn title exceptions into clean assets or convert acquired "
                "certificates into certain redemptions."
            ),
            [
                (
                    "Published sale candidates",
                    "1,000 entries form the starting cohort",
                    1000,
                    (
                        "Import 1,000 county sale entries into one dated cohort. "
                        "Retain withdrawn and duplicate entries as excluded "
                        "records so the original denominator remains auditable."
                    ),
                ),
                (
                    "Desktop-qualified parcels",
                    "300 remain; 30% of starting entries",
                    300,
                    (
                        "Retain 300 candidates after removing duplicates, "
                        "withdrawals, unusable parcel fragments, inaccessible "
                        "land, and assets outside the selected county strategy."
                    ),
                ),
                (
                    "Title-reviewed candidates",
                    "120 remain; 40% of desktop-qualified parcels",
                    120,
                    (
                        "Advance 120 of the 300 desktop survivors after recorded "
                        "interest review, bankruptcy checks, and counsel's "
                        "identification of the applicable redemption procedure."
                    ),
                ),
                (
                    "Price-qualified bid plans",
                    "40 remain; one-third of reviewed candidates",
                    40,
                    (
                        "Approve internal bid plans for 40 of the 120 reviewed "
                        "candidates after modeling premiums, taxes, duration, "
                        "loss exposure, and portfolio concentration limits."
                    ),
                ),
                (
                    "Funded acquisitions",
                    "20 acquired; 50% of price-qualified plans",
                    20,
                    (
                        "Acquire 20 of the 40 planned bids without exceeding "
                        "individual price ceilings. The resulting 2% overall "
                        "conversion measures purchase selection, not redemption "
                        "probability or future investment profitability."
                    ),
                ),
            ],
        ),
        (
            "diag-03-base-case-owner-profit",
            "waterfall",
            "Base Case: $97,500 Revenue to 42.5% Owner Net",
            "Opening gross revenue, four deductions, and one closing total.",
            3,
            "illustrative_model",
            (
                "Canonical annual revenue and margin are fixed; expense "
                "categories are an illustrative allocation of their difference. "
                "The first bar is the opening total, the middle four are signed "
                "deltas, and the sixth is the closing total, not another delta. "
                "Recurring overhead plus contractors equals $36,000 annually "
                "or $3,000 monthly, inside the $500–$4,000 monthly opex range. "
                "Deal-specific costs and realized capital losses are separate."
            ),
            (
                "$97,500 - $24,000 - $12,000 - $10,500 - $9,562.50 "
                "= $41,437.50, exactly 42.5% of revenue and displayed as "
                "$41,438 annual owner net profit. The owner works the core "
                "full-time seat; no additional owner salary is deducted. "
                "Returned principal never enters the opening revenue bar."
            ),
            [
                (
                    "Realized operator revenue",
                    "$97,500 annual gross; principal receipts excluded",
                    97500,
                    (
                        "Opening total contains realized interest, penalties, "
                        "and positive disposition gains. Gross property sale "
                        "proceeds and recovered certificate basis are not "
                        "recognized as revenue in this operator scorecard."
                    ),
                ),
                (
                    "Recurring operating overhead",
                    "Subtract $24,000 annual recurring operating overhead",
                    -24000,
                    (
                        "Allocate $2,000 monthly to portfolio administration, "
                        "data access, insurance, bookkeeping, secure records, "
                        "and servicing systems; contractor retainers are "
                        "separately shown in the next deduction."
                    ),
                ),
                (
                    "Two contracted core seats",
                    "Subtract $12,000 annual contractor retainer expense",
                    -12000,
                    (
                        "Budget $6,000 annually for title review retainers and "
                        "$6,000 for local counsel retainers. These are limited "
                        "service budgets, not full-time salaries; exceptional "
                        "matter charges belong in deal-specific expenses."
                    ),
                ),
                (
                    "Deal-specific execution costs",
                    "Subtract $10,500 in nonrecurring transaction costs",
                    -10500,
                    (
                        "Allocate auction charges, targeted parcel inspections, "
                        "recording expenses, incremental notices, and exceptional "
                        "legal work here. Exclude costs already deducted when "
                        "calculating a disposition gain to prevent double counting."
                    ),
                ),
                (
                    "Realized capital losses",
                    "Subtract $9,562.50 of unrecovered investment basis",
                    -9562.50,
                    (
                        "Recognize documented unrecovered basis from resolved "
                        "loss positions. Do not expense every principal purchase "
                        "or treat principal repayment as income; a cash reserve "
                        "transfer alone does not establish a realized loss."
                    ),
                ),
                (
                    "Annual owner net profit",
                    "$41,437.50 exact; $41,438 rounded annual owner net",
                    41437.50,
                    (
                        "Closing total equals $97,500 multiplied by 42.5%. "
                        "This is owner operating profit before personal income "
                        "tax, with no leverage or separate owner salary modeled."
                    ),
                ),
            ],
        ),
        (
            "diag-04-realized-cash-yield-mechanics",
            "horizontal_bars",
            "Five Investment Bases, Five Cash-Yield Outcomes",
            "Compare realized cash divided by invested cash, not headline rates.",
            2,
            "illustrative_model",
            (
                "All bars are independent transaction illustrations, not "
                "portfolio forecasts or components of the canonical revenue "
                "scenarios. Numeric values are realized cash-yield percentages "
                "before expenses and taxes. Certificate examples assume one "
                "year outstanding; the Texas example is one redemption event "
                "within its applicable 180-day period and is not annualized."
            ),
            (
                "The investment denominator matters as much as the rate. "
                "Certificate interest, auction premiums, and redeemable-deed "
                "payments follow different rules; verify the applicable statute "
                "and county settlement calculation before committing funds."
            ),
            [
                (
                    "Florida certificate at 6%",
                    "6.0% cash yield on $10,000 invested",
                    6.0,
                    (
                        "Assume a $10,000 certificate acquired at a 6% auction "
                        "rate and redeemed after one year: $600 realized "
                        "interest divided by $10,000 invested. Apply Florida "
                        "Statutes sections 197.432 and 197.472, including "
                        "redemption-specific calculation rules."
                    ),
                ),
                (
                    "Arizona certificate at 8%",
                    "8.0% cash yield on $10,000 invested",
                    8.0,
                    (
                        "Assume a $10,000 interest-bearing certificate at an "
                        "8% bid rate for one year: $800 divided by $10,000. "
                        "Arizona Revised Statutes sections 42-18114 and "
                        "42-18153 govern bid rates and redemption amounts; "
                        "actual statutory month counting controls settlement."
                    ),
                ),
                (
                    "New Jersey certificate at 4%",
                    "4.0% interest-only yield before separate redemption charges",
                    4.0,
                    (
                        "Assume a $10,000 certificate bought without a premium "
                        "at 4% and redeemed after one year. Interest alone "
                        "contributes $400; separately analyze additional "
                        "redemption amounts under N.J.S.A. 54:5-32 and "
                        "54:5-61 rather than adding them to the bid rate."
                    ),
                ),
                (
                    "New Jersey premium-funded certificate",
                    "2.0% interest-only yield on $20,000 committed",
                    2.0,
                    (
                        "Assume the same $10,000 certificate at 4% requires "
                        "a separate $10,000 auction premium. Its $400 interest "
                        "divided by $20,000 committed yields 2%; premium "
                        "return, forfeiture, and holding rules require separate "
                        "review under N.J.S.A. 54:5-33."
                    ),
                ),
                (
                    "Texas nonhomestead redeemable deed",
                    "25.0% event yield; no annualized comparison implied",
                    25.0,
                    (
                        "Assume a qualifying nonhomestead, nonagricultural "
                        "property under Texas Tax Code section 34.21(e), "
                        "with $10,000 total qualifying expenditure and timely "
                        "redemption. A 25% premium produces $2,500; this "
                        "is a statutory redemption payment, not annual interest."
                    ),
                ),
            ],
        ),
        (
            "diag-05-statutory-risk-preflight",
            "decision_tree",
            "Four Checks Before Capital Moves",
            "Every failed branch stops the bid or the proposed enforcement step.",
            5,
            "operating_framework",
            (
                "Read these as ordered checks: passing advances to the next "
                "check; failing produces the stated stop action. Numeric values "
                "are layout weights, not probabilities. Re-run relevant checks "
                "before enforcement because bankruptcy, title, and statutory "
                "facts can change after purchase."
            ),
            (
                "Local auction eligibility, rate limits, notice procedures, "
                "and redemption rights control the investment. A successful "
                "auction bid does not resolve title defects or authorize "
                "retaining another party's protected surplus."
            ),
            [
                (
                    "Eligibility and auction mechanics",
                    "Pass documented authority; otherwise do not bid",
                    1,
                    (
                        "Verify bidder registration, deposits, payment deadlines, "
                        "asset type, and rate or premium rules against the "
                        "current county packet and governing statute. If any "
                        "material rule is unresolved, remove the parcel from "
                        "the live bid list."
                    ),
                ),
                (
                    "Title, stays, and federal interests",
                    "Pass counsel review; otherwise suspend affected action",
                    1,
                    (
                        "Review recorded liens, ownership, access, and bankruptcy "
                        "status. Counsel evaluates 11 U.S.C. section 362 and "
                        "federal lien notice or redemption issues under "
                        "26 U.S.C. section 7425; a recorder search alone "
                        "does not establish that enforcement may proceed."
                    ),
                ),
                (
                    "Redemption, notice, and surplus",
                    "Pass lawful procedure; otherwise redesign the exit",
                    1,
                    (
                        "Map the jurisdiction's redemption period, required "
                        "notices, foreclosure procedure, and surplus distribution. "
                        "Apply Tyler v. Hennepin County, 598 U.S. 631 (2023), "
                        "to the relevant government-taking issue without "
                        "assuming identical rules for every private certificate."
                    ),
                ),
                (
                    "Loss capacity and bid economics",
                    "Pass funded downside; otherwise reduce bid or reject",
                    1,
                    (
                        "Stress delayed redemption, unusable collateral, "
                        "subsequent taxes, counsel expense, and capital loss. "
                        "Reject positions whose loss exposure or cash demands "
                        "exceed funded reserves; a large statutory rate cannot "
                        "repair defective collateral or an excessive premium."
                    ),
                ),
            ],
        ),
        (
            "diag-06-core-and-scaled-pod",
            "org_architecture",
            "Three Core Seats, Five at Scale",
            "The principal owns capital decisions; specialists own defined work.",
            11,
            "operating_framework",
            (
                "FT means full-time and C means contractor. Conservative and "
                "Base use 1 FT + 2 C, totaling three people. Scaled uses "
                "2 FT + 3 C, totaling five people. The principal remains the "
                "investment decision owner in both structures."
            ),
            (
                "Canonical annual outcomes: Conservative $15,000 gross at 30% "
                "margin yields $4,500 owner net; Base $97,500 gross at 42.5% "
                "yields $41,438 rounded owner net; Scaled $180,000 gross at "
                "55% yields $99,000 owner net. All gross figures exclude "
                "returned principal, and the scaled result uses five people."
            ),
            [
                (
                    "Principal investor",
                    "Core seat one: full-time capital decision owner",
                    1,
                    (
                        "Sets county coverage, concentration limits, bid ceilings, "
                        "reserve policy, and acquisition decisions. Reviews "
                        "cash reconciliation and maintains the distinction "
                        "between invested basis, recovered principal, realized "
                        "revenue, and owner profit."
                    ),
                ),
                (
                    "Title and parcel reviewer",
                    "Core seat two: contracted title research specialist",
                    1,
                    (
                        "Reports recorded interests, legal-description mismatches, "
                        "access issues, parcel fragmentation, and unresolved "
                        "exceptions. Delivers dated evidence packets rather "
                        "than treating assessor records as proof of clear title."
                    ),
                ),
                (
                    "Local enforcement counsel",
                    "Core seat three: contracted jurisdiction-specific counsel",
                    1,
                    (
                        "Owns legal interpretation, notice sequencing, stay "
                        "analysis, federal lien issues, enforcement filings, "
                        "and surplus treatment. Distinguishes ordinary retainer "
                        "work from separately budgeted litigation."
                    ),
                ),
                (
                    "Portfolio operations lead",
                    "Scaled seat four: second full-time operating seat",
                    1,
                    (
                        "Added only in the five-person model. Maintains the "
                        "SQLite portfolio register, redemption calendar, "
                        "bank matching, document versioning, and overdue "
                        "exception queue; the principal retains capital authority."
                    ),
                ),
                (
                    "Auction and field analyst",
                    "Scaled seat five: third contracted specialist seat",
                    1,
                    (
                        "Added only in the five-person model. Cleans auction "
                        "files, verifies property conditions, collects local "
                        "sale evidence, and documents inspection exceptions "
                        "without substituting desktop estimates for title review."
                    ),
                ),
            ],
        ),
        (
            "diag-07-startup-capital-allocation",
            "stacked_comparison",
            "Capital Is Inventory and Runway, Not Revenue",
            "Four buckets allocate a $1,000,000 startup illustration.",
            4,
            "illustrative_model",
            (
                "Numeric values are dollar allocations totaling $1,000,000, "
                "within the canonical $100,000–$1,500,000 startup range. "
                "Allocation shares are 75%, 10%, 10%, and 5%. Endpoint "
                "comparisons apply those shares mechanically, not as forecasts. "
                "Capital allocation alone does not generate the canonical "
                "Conservative, Base, or Scaled revenue outcomes."
            ),
            (
                "The $750,000 acquisition bucket matches the illustrative "
                "twenty-position funnel. The $50,000 operating reserve covers "
                "about 16.7 months of the Base illustration's $3,000 recurring "
                "monthly spend, not the entire possible 36-month deal timeline."
            ),
            [
                (
                    "Acquisition principal and premiums",
                    "$750,000 allocated; 75% of startup capital",
                    750000,
                    (
                        "Fund certificate principal or deed purchase basis "
                        "and any required premium without counting purchases "
                        "as revenue. At $100,000 total capital this bucket "
                        "is $75,000; at $1,500,000 it is $1,125,000."
                    ),
                ),
                (
                    "Parcel diligence and enforcement reserve",
                    "$100,000 allocated; 10% of startup capital",
                    100000,
                    (
                        "Hold cash for inspections, title work, recording, "
                        "notices, and exceptional enforcement matters. Reserve "
                        "funding is not an immediate expense. Endpoint "
                        "allocations are $10,000 and $150,000 respectively."
                    ),
                ),
                (
                    "Liquidity and subsequent-tax reserve",
                    "$100,000 allocated; 10% of startup capital",
                    100000,
                    (
                        "Preserve uncommitted liquidity for delayed redemptions "
                        "and underwritten subsequent-tax decisions. Do not "
                        "assume every additional tax payment earns interest "
                        "or preserves priority. Endpoint allocations are "
                        "$10,000 and $150,000 respectively."
                    ),
                ),
                (
                    "Operating cash runway",
                    "$50,000 allocated; 5% of startup capital",
                    50000,
                    (
                        "Fund recurring administration and contractor retainers "
                        "while investment cash remains tied up. Endpoint "
                        "allocations are $5,000 and $75,000; at the lower "
                        "endpoint, size spend and commitments to available "
                        "runway rather than assuming Base-case overhead fits."
                    ),
                ),
            ],
        ),
        (
            "diag-08-first-thirty-days",
            "timeline_roadmap",
            "Thirty Days to a Documented Investment Process",
            "Build the operating system before expecting investment proceeds.",
            12,
            "operating_framework",
            (
                "Four consecutive work periods cover Days 1–30. Numeric "
                "values are each period's ending day, not revenue or deal "
                "counts. The canonical first-deal window remains 6–36 months; "
                "the sprint produces diligence and operating artifacts rather "
                "than promising an acquisition, redemption, or foreclosure."
            ),
            (
                "A completed sprint leaves a traceable county rulebook, tested "
                "parcel records, conservative bid worksheets, and a funded "
                "cash plan. An unsuitable auction remains a valid reason "
                "to finish the month without deploying acquisition capital."
            ),
            [
                (
                    "Days 1-7",
                    "Choose one jurisdiction and document its rules",
                    7,
                    (
                        "Select one county and asset type. Archive its official "
                        "auction packet, registration instructions, payment "
                        "requirements, redemption statute, and enforcement "
                        "procedure. Ask local counsel to identify notice, "
                        "bankruptcy, federal lien, and surplus issues."
                    ),
                ),
                (
                    "Days 8-14",
                    "Build and test the parcel evidence register",
                    14,
                    (
                        "Create a SQLite register keyed by county and parcel "
                        "identifier. Import one published sale file, retain "
                        "source dates, and manually audit twenty records "
                        "against assessor GIS, recorder documents, and counsel's "
                        "title-review requirements."
                    ),
                ),
                (
                    "Days 15-21",
                    "Model bids, reserves, and delayed cash recovery",
                    21,
                    (
                        "Create spreadsheet bid worksheets separating principal, "
                        "premiums, interest-bearing amounts, fees, and taxes. "
                        "Stress redemption at 6, 18, and 36 months where "
                        "legally relevant, plus capital loss; test reserve "
                        "adequacy without assuming immediate owner distributions."
                    ),
                ),
                (
                    "Days 22-30",
                    "Rehearse execution and verify cash classifications",
                    30,
                    (
                        "Run a mock auction against documented bid ceilings, "
                        "test redemption alerts, and reconcile sample receipts "
                        "into principal and earnings. Confirm contractor scope, "
                        "payment procedures, and record retention; fund a real "
                        "purchase only when its specific checks pass."
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
