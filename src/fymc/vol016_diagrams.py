"""Volume 016: Probate Real Estate - diagram data and positioning alternatives."""

VOLUME_016_SUBTITLE: str = (
    "Letters before listings, overbid-ready court confirmations, step-up appraisals, "
    "Medicaid claim checks, call-first probate pipelines, attorney referral runways, "
    "and pre-completion wholesale contracts"
)


def build_volume_016_diagrams_data() -> list[dict]:
    return [
        {
            "diagram_id": "diag-01-filing-to-letters-roadmap",
            "chapter_number": 1,
            "chart_type": "process_flow",
            "title": "From Filing to Certified Letters",
            "subtitle": "The court sequence that must finish before any estate property is listed",
            "caption": (
                "Nothing moves on an estate property until the court issues letters; the letters "
                "date is the date the property can be listed."
            ),
            "assumptions_note": (
                "Timing figures are attributed practitioner claims. SwiftProbate cites 2 to 6 weeks "
                "for letters in straightforward cases and several months for busy courts or contested "
                "cases; California timelines run longer."
            ),
            "note": (
                "Sequence per SwiftProbate, RLS Law Corporation, California Probate Real Estate Made "
                "Simple, and NOVA Real Estate Solutions."
            ),
            "stages": [
                {
                    "step": "01",
                    "label": "File in the county of domicile",
                    "value": "Step 1",
                    "detail": (
                        "Original will, certified death certificate, petition and fee; request full "
                        "IAEA authority at filing to avoid repeat court approvals."
                    ),
                },
                {
                    "step": "02",
                    "label": "Notify every heir and publish",
                    "value": "Step 2",
                    "detail": (
                        "List every heir and relative, including disinherited ones; the DE121 notice is "
                        "mailed by a non-party with proof filed."
                    ),
                },
                {
                    "step": "03",
                    "label": "Clear the hearing",
                    "value": "Step 3",
                    "detail": (
                        "An omitted heir is the most common avoidable mistake, and the judge will "
                        "continue the hearing."
                    ),
                },
                {
                    "step": "04",
                    "label": "Pull certified letters",
                    "value": "Step 4",
                    "detail": (
                        "Order at least 5 to 10 certified copies; some institutions refuse letters more "
                        "than sixty to ninety days old."
                    ),
                },
                {
                    "step": "05",
                    "label": "Open the estate account under its EIN",
                    "value": "Step 5",
                    "detail": (
                        "Estate money runs only through this account, and debts are paid in statutory "
                        "priority order to avoid personal liability."
                    ),
                },
            ],
        },
        {
            "diagram_id": "diag-02-probate-lead-funnel",
            "chapter_number": 6,
            "chart_type": "funnel",
            "title": "What 100 Probate Leads Become",
            "subtitle": "Per-100-lead figures reported by probate listing specialists",
            "caption": (
                "Probate inventory does not care about rates, but it rewards volume and follow-up; "
                "three touches do not do it."
            ),
            "assumptions_note": (
                "Stages combine per-100-lead figures from different speakers and are not a single "
                "tracked cohort. Carolynn Castillo reports 20 to 40 leads a week per county."
            ),
            "note": (
                "Figures from Probate Mastery (Bruce Hill) and Carolynn Castillo; the must-sell share "
                "is the Probate Mastery 10 to 15 percent estimate."
            ),
            "stages": [
                {
                    "label": "Raw probate leads",
                    "value": 100,
                    "display": "100 leads",
                    "conversion": "Baseline",
                    "detail": "Most counties produce 20 to 40 leads a week, about 1 to 2 hours of calling.",
                },
                {
                    "label": "Leads with real estate",
                    "value": 70,
                    "display": "About 70",
                    "conversion": "About 70% carry real estate",
                    "detail": "Bruce Hill counts about 70 of 100 raw leads holding real estate.",
                },
                {
                    "label": "Live conversations, call-first",
                    "value": 50,
                    "display": "About 50",
                    "conversion": "About 50 per 100 leads",
                    "detail": "Roughly $400 of ISA cost versus $900 for 600 mailers.",
                },
                {
                    "label": "Estates that have to sell",
                    "value": 10,
                    "display": "About 10",
                    "conversion": "10 to 15% of leads",
                    "detail": "Probate Mastery estimates 10 to 15 of every 100 leads have to go.",
                },
                {
                    "label": "Closed deals",
                    "value": 1.5,
                    "display": "About 1.5",
                    "conversion": "About 1.5 per 100 raw leads",
                    "detail": "20 to 25% of pipeline reaches an appointment and about 15 to 20% close.",
                },
            ],
        },
        {
            "diagram_id": "diag-03-step-up-and-confirmation-floor",
            "chapter_number": 3,
            "chart_type": "waterfall",
            "title": "Step-Up Basis and the 90% Floor on an $800,000 House",
            "subtitle": "Two reported calculations an heir runs before setting the asking price",
            "caption": (
                "A professional date-of-death appraisal erased a projected capital gains bill, and the "
                "referee value sets the lowest price a court will confirm."
            ),
            "assumptions_note": (
                "The first three bars follow a Ventura County sale where the CPA had estimated roughly "
                "$180,000 in tax; the last three apply the 90% referee-value floor to the same figure."
            ),
            "note": (
                "Step-up math per Tricia Garcia Real Estate; 90% court-confirmation floor per Matt "
                "McGilvray."
            ),
            "bars": [
                {"label": "Sale price", "value": 800000, "display": "$800,000", "kind": "total"},
                {
                    "label": "Date-of-death basis",
                    "value": -800000,
                    "display": "-$800,000",
                    "kind": "deduction",
                },
                {"label": "Taxable gain", "value": 0, "display": "$0", "kind": "result"},
                {"label": "Referee appraisal", "value": 800000, "display": "$800,000", "kind": "total"},
                {
                    "label": "Allowed discount below appraisal",
                    "value": -80000,
                    "display": "-10% (-$80,000)",
                    "kind": "deduction",
                },
                {
                    "label": "Court-confirmation minimum",
                    "value": 720000,
                    "display": "$720,000",
                    "kind": "result",
                },
            ],
        },
        {
            "diagram_id": "diag-04-overbid-dollar-ranges",
            "chapter_number": 2,
            "chart_type": "horizontal_bars",
            "title": "Courtroom Overbid Dollars",
            "subtitle": "Statutory opening bids and observed overbid amounts in Los Angeles and Las Vegas",
            "unit": "USD",
            "caption": (
                "Limited authority sales must survive a confirmation hearing that doubles as a live "
                "auction; 1 in 6 Los Angeles confirmations drew an overbid."
            ),
            "assumptions_note": (
                "Where a single figure was reported, min, max and typical are equal. For Las Vegas the "
                "typical value is set to the lower reported overbid because no midpoint was reported."
            ),
            "note": (
                "Los Angeles figures per Bill Gross, the LA Probate Expert; opening bid formula per "
                "Win-Win Realtors TV; Las Vegas calendar per Mario Joyner."
            ),
            "bars": [
                {
                    "label": "LA expected value per estate",
                    "min": 8000,
                    "max": 8000,
                    "typical": 8000,
                    "display": "About $8,000 (1 in 6 chance of roughly $48,000)",
                },
                {
                    "label": "Las Vegas February 10 overbid amounts",
                    "min": 15000,
                    "max": 19000,
                    "typical": 15000,
                    "display": "About $15,000 and $19,000 (2 of 10 confirmations)",
                },
                {
                    "label": "Statutory opening overbid on a $500,000 contract",
                    "min": 25500,
                    "max": 25500,
                    "typical": 25500,
                    "display": "$525,500 opening bid (10% of first $10,000 plus 5% of balance)",
                },
                {
                    "label": "LA median overbid, all sales",
                    "min": 47500,
                    "max": 47500,
                    "typical": 47500,
                    "display": "$47,500 (6.7% over accepted offer)",
                },
                {
                    "label": "LA median overbid, properties over $1 million",
                    "min": 322000,
                    "max": 322000,
                    "typical": 322000,
                    "display": "$322,000",
                },
            ],
        },
        {
            "diagram_id": "diag-05-cleanout-gate-tree",
            "chapter_number": 5,
            "chart_type": "decision_tree",
            "title": "Cleanout Gates Before Anything Leaves the House",
            "subtitle": "Secure, authorize, document and search before disposal",
            "caption": (
                "Throw nothing away until a professional has looked; the market decides the value of "
                "the items, not the memories."
            ),
            "assumptions_note": (
                "Gate order follows the shared sequence of probate realtors, haulers, liquidators and "
                "preservation contractors. Fee and return figures are attributed practitioner claims."
            ),
            "note": (
                "Gates per JunkRemovalWeb, Gyd Path, Local Probate Help, Cesar Espinoza, Illinois "
                "Probate Solutions, BizMove, At Home with Jody, Smile Abroad, and JM Junk Removers."
            ),
            "nodes": [
                {
                    "gate": "G1",
                    "question": "Has the person with legal authority signed before a single item is loaded?",
                    "pass_next": "G2",
                    "fail_action": (
                        "Stop. Nobody loads a truck until that person signs; where two heirs inherit, "
                        "get both signatures."
                    ),
                },
                {
                    "gate": "G2",
                    "question": "Is every room, garage, shed and closet photographed or on video?",
                    "pass_next": "G3",
                    "fail_action": "Shoot the preliminary inventory before any contents move.",
                },
                {
                    "gate": "G3",
                    "question": "Have books, coat pockets, high shelves, tins and shoeboxes been searched?",
                    "pass_next": "G4",
                    "fail_action": (
                        "Run the one-pass search; one hoarder-home sort turned up $5,000 in jewelry and "
                        "nearly $30,000 in cash."
                    ),
                },
                {
                    "gate": "G4",
                    "question": "Has a professional looked at valuable or unique items?",
                    "pass_next": (
                        "Choose the sale route: DIY ($400 in expenses turned into well over $10,000) or "
                        "a company (base minimum plus 25-50% or more), then quote cleanout as load "
                        "price plus labor."
                    ),
                    "fail_action": "Hire an appraiser for valuable or unique items before disposal.",
                },
            ],
        },
        {
            "diagram_id": "diag-06-probate-wholesale-architecture",
            "chapter_number": 11,
            "chart_type": "org_architecture",
            "title": "The Pre-Completion Probate Wholesale Setup",
            "subtitle": "One operator, fresh filings, and the parties that make the contract close",
            "caption": (
                "Reach the personal representative within 30 days of filing and contract before "
                "probate completes; Flip With Rick reports an average near $47,000 per probate deal."
            ),
            "assumptions_note": (
                "Team size was not reported. Practitioners split on attorneys: Flip With Rick bypasses "
                "them as billable-hour blockers, while Al Nicoletti treats them as closing partners."
            ),
            "note": (
                "Structure per Flip With Rick, Rick Ginn, and Michael Franke; Rick Ginn pegs probate "
                "spreads at 3 to 3.5 times a normal assignment."
            ),
            "center": {
                "role": "Probate wholesaler",
                "headcount": "Not reported",
                "focus": (
                    "Warm calls at 80/20 or 90/10 listening, no price on the first call, and a "
                    "price-deposit-terms anchor locked with the PR."
                ),
            },
            "spokes": [
                {
                    "role": "Personal representative",
                    "type": "Seller",
                    "kpi": (
                        "Letters of administration confirmed; contract re-papered with a new date after "
                        "they issue; EMD of at least $500."
                    ),
                },
                {
                    "role": "Courthouse or XLeads list pull",
                    "type": "Lead source",
                    "kpi": "Filings from the last 30 days only, never older than 90.",
                },
                {
                    "role": "Cash buyer",
                    "type": "Exit",
                    "kpi": (
                        "May pay $10,000 more for a faster close; $50 to $75 rekey plus lockbox lets "
                        "buyers tour without an out-of-state PR."
                    ),
                },
                {
                    "role": "Title company and real estate attorney",
                    "type": "Closing partner",
                    "kpi": (
                        "Sale process verified in order through the state probate court site, the title "
                        "company, then the attorney."
                    ),
                },
            ],
        },
        {
            "diagram_id": "diag-07-medicaid-home-equity-caps",
            "chapter_number": 4,
            "chart_type": "stacked_comparison",
            "title": "Long-Term Care Medicaid Home Equity Caps",
            "subtitle": "Current limits versus the flat cap starting January 1, 2028",
            "total_range": "$752,000 to $1.13 million",
            "caption": (
                "Home equity must sit under the limit to qualify for long-term care Medicaid unless a "
                "spouse or a minor or disabled child lives there."
            ),
            "assumptions_note": (
                "The 2028 cap is reported at $1 million with no inflation increases; DC's limit drops "
                "under it. Each bucket is a single reported figure, so low and high are equal."
            ),
            "note": "Caps reported by Marc Cormier.",
            "buckets": [
                {
                    "label": "Maryland today",
                    "low": 752000,
                    "high": 752000,
                    "notes": "$752,000 current limit.",
                },
                {
                    "label": "Virginia today",
                    "low": 752000,
                    "high": 752000,
                    "notes": "$752,000 current limit; a broader-estate recovery state.",
                },
                {
                    "label": "DC today",
                    "low": 1130000,
                    "high": 1130000,
                    "notes": "$1.13 million current limit, which falls under the 2028 cap.",
                },
                {
                    "label": "All three from January 1, 2028",
                    "low": 1000000,
                    "high": 1000000,
                    "notes": "$1 million with no inflation increases.",
                },
            ],
        },
        {
            "diagram_id": "diag-08-senior-transition-roadmap",
            "chapter_number": 12,
            "chart_type": "timeline_roadmap",
            "title": "Senior Transition Sale Roadmap",
            "subtitle": "Authority first, then the house, then the capital",
            "caption": (
                "Sheri Coleman reports as short as 6 weeks from family meeting to closing once a power "
                "of attorney and a single family contact are in place."
            ),
            "assumptions_note": (
                "The four weeks are a sequencing frame, not a reported duration; actual timing depends "
                "on asking price and finding the right buyer."
            ),
            "note": (
                "Sequence per Florida Realtors YouTube, Dale Corpus, The Cobb Home Team, Ariana Jay, "
                "Brett Chotkevys, Serg Lupescu, and Unit Math."
            ),
            "weeks": [
                {
                    "week": "Week 1",
                    "title": "Lock legal authority",
                    "deliverable": "Power of attorney or the senior signing, plus one designated family contact.",
                    "gate": "No senior listing without both.",
                },
                {
                    "week": "Week 2",
                    "title": "Payoff and pricing",
                    "deliverable": (
                        "Reverse mortgage balance confirmed, since it is paid off at closing; family "
                        "educated on current market conditions."
                    ),
                    "gate": "No overpriced list that stalls and frustrates the family.",
                },
                {
                    "week": "Week 3",
                    "title": "Fund the care",
                    "deliverable": (
                        "Bay Area assisted living or memory care at $5,000 to $12,000-plus per month, "
                        "often funded by the home sale."
                    ),
                    "gate": "Two years of private pay saved, with financial and medical POA and a will or trust.",
                },
                {
                    "week": "Week 4",
                    "title": "Redeploy capital",
                    "deliverable": (
                        "Residential assisted living targets $3,000 to $10,000 per client per month; a "
                        "$240 rough site plan clears zoning questions."
                    ),
                    "gate": "Zoning confirmed for the exact address and debt service coverage near 1.2.",
                },
            ],
        },
    ]


VOLUME_016_POSITIONING_ALTERNATIVES: list[dict] = [
    {
        "title": "Letters First, Listings Second",
        "subtitle": "The probate listing agent's playbook from courthouse lead to court confirmation",
        "audience": "Real estate agents building a probate listing practice",
        "research_basis": (
            "RLS Law Corporation ties listing dates to letters, Bill Gross tracked 1 in 6 Los Angeles "
            "confirmations overbid at a $47,500 median, Carolynn Castillo reports 20 to 40 leads a week "
            "per county, and a 15-year probate attorney puts real estate in 80 to 90 percent of probates."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=lNaVAVnUZTE&t=805s",
            "https://www.youtube.com/watch?v=ih5FQvZZVck&t=232s",
            "https://www.youtube.com/watch?v=RR9l10XmnC4&t=972s",
            "https://www.youtube.com/watch?v=tHKQUQ1PDts&t=1237s",
        ],
        "validation_status": "Grounded strictly in Vol. 016 YouTube practitioner transcripts.",
    },
    {
        "title": "The Inherited House Decision Guide",
        "subtitle": "Step-up appraisals, vacancy protection, Medicaid claims and the 90% floor",
        "audience": "Executors, personal representatives and heirs holding an inherited home",
        "research_basis": (
            "Tricia Garcia took a projected $180,000 capital gains bill to zero with a date-of-death "
            "appraisal, Stephanie Burt prices six months of indecision at $3,000 to $6,000, Matt "
            "McGilvray sets the court floor at 90% of referee value, and Marc Cormier says to know the "
            "Medicaid claim before pricing."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=qNeCeQehzRg&t=195s",
            "https://www.youtube.com/watch?v=6xUa7KjeSSY&t=263s",
            "https://www.youtube.com/watch?v=fi8ZbbtnVgM&t=153s",
            "https://www.youtube.com/watch?v=t0-A8dVrr1o&t=241s",
        ],
        "validation_status": "Grounded strictly in Vol. 016 YouTube practitioner transcripts.",
    },
    {
        "title": "Fresh Filings, Fast Contracts",
        "subtitle": "Call-first probate acquisition and pre-completion wholesale deals",
        "audience": "Investors and wholesalers buying probate property",
        "research_basis": (
            "Flip With Rick reports about $47,000 average probate profit and pulls only filings from "
            "the last 30 days, Rick Ginn pegs probate spreads at 3 to 3.5 times a normal assignment, "
            "and Bruce Hill's call-first math yields about 50 conversations per 100 leads."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=4-UlN2iP-_c&t=1188s",
            "https://www.youtube.com/watch?v=WU_DwL7k5ZE&t=3450s",
            "https://www.youtube.com/watch?v=e3YN7RJaj6U&t=3575s",
            "https://www.youtube.com/watch?v=y1TInRM-Flc&t=43s",
        ],
        "validation_status": "Grounded strictly in Vol. 016 YouTube practitioner transcripts.",
    },
]
