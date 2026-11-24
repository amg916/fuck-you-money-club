"""Volume 042 diagrams: Cell-Tower, Digital-Billboard & IOS Lease Arbitrage."""

from typing import Dict, List

VOLUME_042_SUBTITLE: str = (
    "Sell the rent stream at 16 to 19 times or strike the ROFR and make buyers bid, "
    "buy the billboard permit instead of the steel and underwrite at 85% fill, "
    "and lease gravel yards, truck stalls and substation-adjacent acres on day-one yield"
)


def build_volume_042_diagrams_data() -> List[Dict]:
    """Return the eight structured diagram dicts for Volume 042."""
    return [
        {
            "diagram_id": "diag-01-cell-lease-buyout-diligence-flow",
            "chapter_number": 1,
            "title": "Cell Tower Lease Buyout Diligence Flow",
            "subtitle": "Five gates before a landlord accepts a lump sum for the rent stream",
            "caption": (
                "Practitioners price a buyout as a multiple of annual rent; tenant mix, "
                "lease language and termination risk decide where the multiple lands."
            ),
            "assumptions_note": (
                "Steps follow the operator gates and pro-tips reported by Tower Genius, "
                "Acquisition Insider and Allworth Financial. The rent-stop window of year "
                "five to eight and the December/January payment split are as stated by "
                "those speakers; no other figures are added."
            ),
            "note": (
                "Sources: Acquisition Insider (MtWLazzJb9Y @ 00:06:24, 00:06:38); "
                "Tower Genius (X75LHgvP1U8 @ 00:02:04, wpxdOZZukBY @ 00:05:12); "
                "Allworth Financial (L5rvTFM0pVg @ 00:06:46)."
            ),
            "chart_type": "process_flow",
            "stages": [
                {
                    "step": "01",
                    "label": "Identify Every Carrier on the Tower",
                    "value": "Step 1",
                    "detail": (
                        "Count every carrier physically on the structure and walk away "
                        "from single-tenant sites (Acquisition Insider)."
                    ),
                },
                {
                    "step": "02",
                    "label": "Name Each Sub-Tenant",
                    "value": "Step 2",
                    "detail": (
                        "Confirm names from meter labels, equipment cabinets and building "
                        "permits; Dish exposure is toxic to buyers (Tower Genius)."
                    ),
                },
                {
                    "step": "03",
                    "label": "Clear ROFR and Consent Language",
                    "value": "Step 3",
                    "detail": (
                        "Read for right of first refusal, confidentiality and "
                        "consent-to-assign before soliciting offers, or a signed LOI can "
                        "put the landlord in default (Tower Genius)."
                    ),
                },
                {
                    "step": "04",
                    "label": "Stress-Test a Rent Stop in Years 5 to 8",
                    "value": "Step 4",
                    "detail": (
                        "Model the rent stopping in year five to eight; if one site cannot "
                        "survive that, buy several or pass (Acquisition Insider)."
                    ),
                },
                {
                    "step": "05",
                    "label": "Shop Bids and Split the Payout",
                    "value": "Step 5",
                    "detail": (
                        "Push the buyer on price and take half in December and half in "
                        "January to spread the tax over two years (Allworth Financial)."
                    ),
                },
            ],
        },
        {
            "diagram_id": "diag-02-static-billboard-cash-flow-funnel",
            "chapter_number": 6,
            "title": "Single Static Billboard Cash-Flow Funnel",
            "subtitle": "From full-calendar rate card to about $7,000 a year of true cash flow",
            "caption": (
                "A two-sided static board at $600 per face per month and 80% occupancy "
                "keeps roughly 60% of occupied revenue after costs, then trades at 8 to "
                "10 times cash flow, or $55,000 to $70,000."
            ),
            "assumptions_note": (
                "Inputs are Acquisition Insider's: $600 per face per month, two faces, "
                "80% occupancy, roughly 40% costs including a 15% to 20% ground lease. "
                "Intermediate dollar values are straight arithmetic on those inputs; the "
                "ground-lease stages show the low and high end of the stated band."
            ),
            "note": "Source: Acquisition Insider (4PyMov-VjoE @ 00:02:07).",
            "chart_type": "funnel",
            "stages": [
                {
                    "label": "Full-Calendar Rate Card",
                    "value": 14400,
                    "display": "$14,400/yr",
                    "conversion": "100%",
                    "detail": "$600 per face per month, two faces, twelve months sold.",
                },
                {
                    "label": "Revenue at 80% Occupancy",
                    "value": 11520,
                    "display": "$11,520/yr",
                    "conversion": "80% of rate card",
                    "detail": "Occupancy assumption used in the single-board model.",
                },
                {
                    "label": "After a 15% Ground Lease",
                    "value": 9792,
                    "display": "$9,792/yr",
                    "conversion": "85% of occupied revenue",
                    "detail": "Low end of the 15% to 20% ground-lease band.",
                },
                {
                    "label": "After a 20% Ground Lease",
                    "value": 9216,
                    "display": "$9,216/yr",
                    "conversion": "80% of occupied revenue",
                    "detail": "High end of the 15% to 20% ground-lease band.",
                },
                {
                    "label": "True Cash Flow After ~40% Costs",
                    "value": 6912,
                    "display": "About $7,000/yr",
                    "conversion": "60% of occupied revenue",
                    "detail": "Trades at 8 to 10 times cash flow, or $55,000 to $70,000.",
                },
            ],
        },
        {
            "diagram_id": "diag-03-ohio-tower-lease-structure-waterfall",
            "chapter_number": 3,
            "title": "What Lease Structure Is Worth: The Ohio Renegotiation",
            "subtitle": "Unwinding over $6,000 a month back to the original $900",
            "caption": (
                "Vertical Consultants' Ohio client went from about $900 to about $2,000 a "
                "month, and the structured lease now pays over $6,000; a rent-only deal "
                "with a 3% escalator would sit near $2,700 to $2,800."
            ),
            "assumptions_note": (
                "Endpoints are Hugh Odum's reported figures. The rent-only subtotal uses "
                "the midpoint of his $2,700 to $2,800 range; deductions are the gaps "
                "between his stated figures. Odum's rule of thumb that $1 of monthly rent "
                "equals roughly $1,000 of lease value frames the stakes of each step."
            ),
            "note": (
                "Source: Vertical Consultants, Hugh Odum (F1m9euwLJAQ @ 00:25:01, "
                "00:19:51, 00:04:23)."
            ),
            "chart_type": "waterfall",
            "bars": [
                {
                    "label": "Structured Lease Eight Years On",
                    "value": 6000,
                    "display": "Over $6,000/mo",
                    "kind": "total",
                },
                {
                    "label": "Remove Tower-Value Participation",
                    "value": 3250,
                    "display": "-$3,200 to -$3,300/mo",
                    "kind": "deduction",
                },
                {
                    "label": "Rent-Only Path With 3% Escalator",
                    "value": 2750,
                    "display": "$2,700 to $2,800/mo",
                    "kind": "total",
                },
                {
                    "label": "Remove Eight Years of 3% Escalation",
                    "value": 750,
                    "display": "-$700 to -$800/mo",
                    "kind": "deduction",
                },
                {
                    "label": "Remove the Renegotiated Base Lift",
                    "value": 1100,
                    "display": "-$1,100/mo",
                    "kind": "deduction",
                },
                {
                    "label": "Original Rent Before Renegotiation",
                    "value": 900,
                    "display": "About $900/mo",
                    "kind": "result",
                },
            ],
        },
        {
            "diagram_id": "diag-04-cell-lease-buyout-multiples",
            "chapter_number": 2,
            "title": "Buyout Multiples of Annual Rent by Source and Tenant",
            "subtitle": "Fine print and carrier identity move the multiple from 5x to 25x",
            "caption": (
                "Easement buyers paid 24-25x for AT&T rent and about 5x for US Cellular "
                "on the same rooftop, while aggregator offers cluster at 8 to 15 times."
            ),
            "assumptions_note": (
                "Ranges are as quoted by each practitioner. Typical values are the "
                "speaker's stated point where one exists (17.5x Tower Genius worked "
                "example, 14x Acquisition Insider discount example); otherwise the "
                "midpoint of the quoted range."
            ),
            "note": (
                "Sources: Tower Genius (pSGbaA0AbTo @ 00:00:32); Acquisition Insider "
                "(MtWLazzJb9Y @ 00:02:09, 00:02:26); Selina Gonzales (x2ZfqDSKoOI @ "
                "00:07:17); James Furlo, Furlo Capital (bk4EnTlbPdA @ 00:11:22)."
            ),
            "chart_type": "horizontal_bars",
            "unit": "x annual rent",
            "bars": [
                {
                    "label": "Aggregator Offer to Shopped Lease",
                    "min": 8,
                    "max": 18,
                    "typical": 14,
                    "display": "8-15x offers; ~18x shopped multi-carrier",
                },
                {
                    "label": "Tower Genius Average to Clean Lease",
                    "min": 16,
                    "max": 19,
                    "typical": 17.5,
                    "display": "16-17.5x average; 19x with 3% escalator, no ROFR",
                },
                {
                    "label": "Ground Lease Buyout Band",
                    "min": 15,
                    "max": 21,
                    "typical": 17.5,
                    "display": "15-20x typical; peak near 21x in 2024",
                },
                {
                    "label": "AT&T Tenant on a Rooftop",
                    "min": 24,
                    "max": 25,
                    "typical": 24.5,
                    "display": "24-25x",
                },
                {
                    "label": "US Cellular Tenant on a Rooftop",
                    "min": 5,
                    "max": 5,
                    "typical": 5,
                    "display": "About 5x",
                },
            ],
        },
        {
            "diagram_id": "diag-05-tower-ownership-go-no-go",
            "chapter_number": 5,
            "title": "Tower Ownership Go/No-Go Gates",
            "subtitle": "The first tenant pays the bills; every tenant after that pays the owner",
            "caption": (
                "One tenant can yield as little as 1% to 3% with paybacks of 34 to 75 "
                "years; a second tenant converts about 90% to 97% of its revenue to profit."
            ),
            "assumptions_note": (
                "Gate thresholds are the practitioners' own: no build without a signed "
                "anchor, underwrite to two signed tenants, match land control to payback, "
                "and stress-test an anchor exit that cuts revenue 60% and profit about 78%."
            ),
            "note": (
                "Sources: Economic Oddities (QdFbgvbJJ-M @ 00:09:49, 00:08:28, 00:10:56); "
                "Holly Lane Radio (RRrHddpY1pU @ 00:24:22, 00:17:58); Mr. Finance "
                "(ku_-0C-ZnV4 @ 00:12:46); Profit Chain (t9bXdQI0jPM @ 00:08:38); "
                "Mr. Money (jQ79QHMZWQE @ 00:08:14)."
            ),
            "chart_type": "decision_tree",
            "nodes": [
                {
                    "gate": "G1",
                    "question": "Is a signed anchor tenant in hand before any steel goes up?",
                    "pass_next": "G2",
                    "fail_action": (
                        "Do not build; a single-tenant tower is a coin flip with a lease "
                        "(Economic Oddities)."
                    ),
                },
                {
                    "gate": "G2",
                    "question": "Does the price work on two signed tenants, not three hoped-for ones?",
                    "pass_next": "G3",
                    "fail_action": (
                        "Re-price; a price built on three future tenants is speculation "
                        "dressed as infrastructure (Holly Lane Radio)."
                    ),
                },
                {
                    "gate": "G3",
                    "question": "Does the ground-lease term cover the payback period?",
                    "pass_next": "G4",
                    "fail_action": (
                        "Extend land control first; an 11-year remaining ground lease "
                        "under a producing tower is live exposure."
                    ),
                },
                {
                    "gate": "G4",
                    "question": "Does the deal survive an anchor exit and a carrier default?",
                    "pass_next": "Proceed to build or acquire",
                    "fail_action": (
                        "Pass; an anchor exit cuts revenue 60% and profit about 78%, and "
                        "Crown's Dish claim exceeds $3.5B with recovery uncertain."
                    ),
                },
            ],
        },
        {
            "diagram_id": "diag-06-truck-parking-yard-operating-model",
            "chapter_number": 11,
            "title": "Self-Managed Truck Parking Yard Operating Model",
            "subtitle": "One operator, automated gates and a marketplace channel",
            "caption": (
                "Operators self-manage yards with Easy Storage, PDK text-to-gate or Rig Hut "
                "app access tied to payment, and Truck Parking Club hosts start on a 70/30 split."
            ),
            "assumptions_note": (
                "Practitioners did not report staff counts; the hub reflects the "
                "self-managed setups they describe. Spoke KPIs are the figures stated by "
                "Ronald Rohde, Truck Parking Media and REtipster's Evan Shelley interview."
            ),
            "note": (
                "Sources: Truck Parking Media (ulBXkeE5I_8 @ 00:02:30, 00:02:13); "
                "Ronald Rohde Law (rPXHwXgqWs8 @ 00:06:59, tonuCLfZrYE @ 00:14:14); "
                "REtipster (Ombo8TjihMk @ 00:12:41)."
            ),
            "chart_type": "org_architecture",
            "center": {
                "role": "Yard Owner-Operator",
                "headcount": "Self-managed through yard software and gate automation",
                "focus": (
                    "By-right zoning, stall rent, and average revenue per space net of "
                    "bad debt, vacancy and late payments"
                ),
            },
            "spokes": [
                {
                    "role": "Inbound Booking Line",
                    "type": "In-house, answer-first",
                    "kpi": (
                        "Caller entered into the system immediately; a 20-minute callback "
                        "lost bookings"
                    ),
                },
                {
                    "role": "Gate and Access Control",
                    "type": "Automation (PDK text-to-gate or Rig Hut app)",
                    "kpi": "Access tied to payment; 30 ft cantilever about $30K installed",
                },
                {
                    "role": "Truck Parking Club Listing",
                    "type": "Marketplace platform",
                    "kpi": "70/30 owner/platform starting split, lower for 5-10 lot operators",
                },
                {
                    "role": "Class A Service Vendors",
                    "type": "Outsourced with markup",
                    "kpi": "Wash billed at $225 against a $200 vendor price; patrol about $5K/mo",
                },
            ],
        },
        {
            "diagram_id": "diag-07-truck-parking-daily-rate-bands",
            "chapter_number": 4,
            "title": "Truck Parking Daily Rates by Market Density",
            "subtitle": "No-ownership parking arbitrage priced per truck per day",
            "caption": (
                "Evan Shealy prices Truck Parking Club lots at $10-$15 rural, $20-$25 "
                "suburban and $30-plus in dense markets, averaging about $20 a day."
            ),
            "assumptions_note": (
                "Bands are Evan Shealy's. The dense-market band has no stated ceiling, so "
                "$30 marks its floor only. Lots must sit on gravel, asphalt millings or "
                "compacted ground, away from active retail and residential."
            ),
            "note": "Source: Ask Flip Man, Evan Shealy (NIYpBpIvXTc @ 00:14:17, 00:07:16).",
            "chart_type": "stacked_comparison",
            "total_range": "$10 to $30-plus per truck per day",
            "buckets": [
                {
                    "label": "Rural Lot",
                    "low": 10,
                    "high": 15,
                    "notes": "Lowest band on the platform.",
                },
                {
                    "label": "Suburban Lot",
                    "low": 20,
                    "high": 25,
                    "notes": "Mid band for suburban locations.",
                },
                {
                    "label": "Dense Metro Lot",
                    "low": 30,
                    "high": 30,
                    "notes": (
                        "$30-plus in LA-Long Beach, Dallas, Chicago, New York-Newark and Orlando."
                    ),
                },
                {
                    "label": "Platform Average",
                    "low": 20,
                    "high": 20,
                    "notes": "About $20 per truck per day across listed lots.",
                },
            ],
        },
        {
            "diagram_id": "diag-08-battery-storage-land-lease-roadmap",
            "chapter_number": 12,
            "title": "Battery Storage Land Lease Screening Roadmap",
            "subtitle": "A grid-proximity play: acreage, terrain, substation capacity, then terms",
            "caption": (
                "LandGate wants 2 to 15 acres next to a substation or under half a mile "
                "away, on leases of 20 to 30 years with upgrade rights."
            ),
            "assumptions_note": (
                "Week labels order the checks; practitioners did not state durations. "
                "Thresholds are LandGate's and Land Owl's; Doxy's free check allows 10 "
                "screenings a day with a $9.99 map."
            ),
            "note": (
                "Sources: LandApp by LandGate (Yes7DTfUfJs @ 00:00:17, 00:00:33, 00:00:51, "
                "00:01:44); Land Owl (yVhfvSQwGRQ @ 00:01:23, 00:02:53)."
            ),
            "chart_type": "timeline_roadmap",
            "weeks": [
                {
                    "week": "Week 1",
                    "title": "Screen the Parcel",
                    "deliverable": (
                        "Shortlist of 2 to 15 acre parcels next to a substation or under "
                        "half a mile away"
                    ),
                    "gate": "Parcel fits acreage and substation distance",
                },
                {
                    "week": "Week 2",
                    "title": "Trust the Map Over the Listing",
                    "deliverable": (
                        "Contour lines and soil survey reviewed; 50 feet of fall on 6 to "
                        "10% slopes flagged as grading cost"
                    ),
                    "gate": "Terrain does not erase the economics",
                },
                {
                    "week": "Week 3",
                    "title": "Confirm Capacity With the Utility",
                    "deliverable": "Utility answer on substation room; zoning confirmed with the county",
                    "gate": "A substation in service still may have no room for you",
                },
                {
                    "week": "Week 4",
                    "title": "Negotiate the Lease",
                    "deliverable": (
                        "20 to 30 year term with periodic upgrade rights, informed by state "
                        "renewable incentives"
                    ),
                    "gate": "Owner knows the incentives before the developer call",
                },
            ],
        },
    ]


VOLUME_042_POSITIONING_ALTERNATIVES: List[Dict] = [
    {
        "title": "Don't Sell Your Cell Tower Rent for Pennies",
        "subtitle": "Strike the ROFR, name every tenant and make buyers bid against each other",
        "audience": "Landowners and building owners collecting cell site rent who are fielding buyout letters",
        "research_basis": (
            "Tower Genius pegs average buyouts at 16 to 17.5 times rent and 19 times for "
            "clean leases; Acquisition Insider sees aggregator offers at 8 to 15 times; a "
            "struck ROFR drew over $200,000 above a best offer; Furlo saw 24-25x for AT&T "
            "versus about 5x for US Cellular."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=pSGbaA0AbTo&t=32s",
            "https://www.youtube.com/watch?v=MtWLazzJb9Y&t=129s",
            "https://www.youtube.com/watch?v=H0Q5FZ_5RWA&t=254s",
            "https://www.youtube.com/watch?v=bk4EnTlbPdA&t=682s",
        ],
        "validation_status": "Grounded strictly in Vol. 042 YouTube practitioner transcripts.",
    },
    {
        "title": "Buy the Permit, Not the Steel",
        "subtitle": "Billboard underwriting at 85% fill, digital conversion math and the debt that kills roll-ups",
        "audience": "Small-business buyers and real estate investors evaluating static and digital billboards",
        "research_basis": (
            "A single static board nets about $7,000 a year and trades at 8 to 10 times "
            "cash flow; Lamar's Sean Reilly cites $3,000 a month static becoming $15,000 "
            "to $18,000 digital for about $200,000; operators underwrite at 85% occupancy; "
            "a 300-board, 75%-debt roll-up went bankrupt in 2021 when leases came back at "
            "double rent."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=4PyMov-VjoE&t=127s",
            "https://www.youtube.com/watch?v=OYv2q23Z36g&t=185s",
            "https://www.youtube.com/watch?v=9d5MJAQGDk8&t=418s",
            "https://www.youtube.com/watch?v=Bb-6A1zEJAc&t=474s",
        ],
        "validation_status": "Grounded strictly in Vol. 042 YouTube practitioner transcripts.",
    },
    {
        "title": "Gravel, Gates and Day-One Yield",
        "subtitle": "Industrial outdoor storage and truck parking yards where zoning and dirt are the deal",
        "audience": "Investors moving from small residential rentals into IOS, truck parking and parking arbitrage",
        "research_basis": (
            "Evan Shealy prices truck parking at $10 to $30-plus per truck per day; Tyler "
            "Cauble's buy box is $300,000-$500,000 an acre and $175-$225 per space; Ron "
            "Rohde lifted stalls from $100 to $215-225; 9606 Capital buys Atlanta at 8.5% "
            "against 7% stabilized; one acre models at about 40 spaces and about $57K NOI."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=NIYpBpIvXTc&t=857s",
            "https://www.youtube.com/watch?v=IRDT0HnPpUc&t=886s",
            "https://www.youtube.com/watch?v=gcg4K6xqYaU&t=264s",
            "https://www.youtube.com/watch?v=LftC_mcL69E&t=894s",
            "https://www.youtube.com/watch?v=q7HQGiIiT_8&t=1170s",
        ],
        "validation_status": "Grounded strictly in Vol. 042 YouTube practitioner transcripts.",
    },
]
