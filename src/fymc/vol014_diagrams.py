"""Volume 014 diagrams: Specialty Finance Brokerage."""

from typing import Any, Dict, List

VOLUME_014_SUBTITLE: str = (
    "Score the File, Match the One Lender Whose Credit Box Fits, and Get Paid at Funding: "
    "Points and Packaging Deposits, Dealer-Channel Equipment Deals, Lifetime Factoring "
    "Residuals, SBA and DSCR Underwriting Math, MCA Takeout Ladders, and Capital-Stack Placement"
)


def build_volume_014_diagrams_data() -> List[Dict[str, Any]]:
    """Return the eight structured diagram dicts for Volume 014."""
    return [
        {
            "diagram_id": "diag-01-broker-deal-path",
            "chapter_number": 1,
            "chart_type": "process_flow",
            "title": "From Qualified File to Funded Commission",
            "subtitle": "The five-step commercial broker path practitioners describe",
            "caption": (
                "The broker lends no money, scores and packages the file, places it with the "
                "lender whose credit box fits, and is paid only when the deal funds."
            ),
            "assumptions_note": (
                "Step order combines operator gates from separate speakers. The $30,000 figure "
                "is Shane Walton's worked example of a $2 million loan at 1.5 points."
            ),
            "note": (
                "Sources are John Neufer, CFM (Commercial Financing Mastery) with Sua Truong, "
                "and Shane Walton of the Commercial Loan Broker Institute."
            ),
            "stages": [
                {
                    "step": "01",
                    "label": "Score the file before quoting points",
                    "value": "Step 1",
                    "detail": (
                        "Neufer weighs deal size, deal type, borrower constraints and time "
                        "pressure, sets the hair clause up front, and targets $5,000 to "
                        "$10,000 per deal."
                    ),
                },
                {
                    "step": "02",
                    "label": "Confirm lender appetite this week",
                    "value": "Step 2",
                    "detail": (
                        "Truong calls bank commercial managers on Monday or Tuesday to ask "
                        "where the money is going, because portfolios fill up by asset type."
                    ),
                },
                {
                    "step": "03",
                    "label": "Take a packaging deposit",
                    "value": "Step 3",
                    "detail": (
                        "Walton takes a deposit as small as $250 with a 45-day LOI refund "
                        "clause before the heavy lifting begins."
                    ),
                },
                {
                    "step": "04",
                    "label": "Place with the lender that fits",
                    "value": "Step 4",
                    "detail": (
                        "Most clients are a best fit for just one, two or three lenders, so "
                        "the file goes where the credit box matches."
                    ),
                },
                {
                    "step": "05",
                    "label": "Collect points when the deal funds",
                    "value": "Step 5",
                    "detail": (
                        "Funded amount times points, with most products paying 1% to 6%. "
                        "A $2 million loan at 1.5 points pays $30,000."
                    ),
                },
            ],
        },
        {
            "diagram_id": "diag-02-factoring-invoice-funnel",
            "chapter_number": 6,
            "chart_type": "funnel",
            "title": "What an Invoice Turns Into on Day One",
            "subtitle": "Advance and discount levels as a percent of invoice face value",
            "caption": (
                "A B2B invoice for delivered work is sold to a factor, which advances most of "
                "the face value immediately and charges a discount per batch."
            ),
            "assumptions_note": (
                "All values are percent of invoice face value. Advance levels come from Joe "
                "Camberato and Ian Johnson; discount levels come from CPA Financial Exchange "
                "Group and are quoted per batch, never annualized."
            ),
            "note": (
                "Sources are Joe Camberato, Ian Johnson, CPA Financial Exchange Group, and "
                "Universal Funding Corporation."
            ),
            "stages": [
                {
                    "label": "Invoice face value",
                    "value": 100,
                    "display": "100% of invoice",
                    "conversion": "Invoice sent to the customer and to the factor",
                    "detail": (
                        "Underwriting rests on the account debtor's credit rating, not the "
                        "client's, per Ian Johnson."
                    ),
                },
                {
                    "label": "Day-one advance ceiling",
                    "value": 90,
                    "display": "Up to 90%",
                    "conversion": "Paid immediately on invoicing",
                    "detail": "Camberato quotes advances of 80 to 90 percent on day one.",
                },
                {
                    "label": "Modeled advance",
                    "value": 80,
                    "display": "80%",
                    "conversion": "Johnson's worksheet advance",
                    "detail": (
                        "Johnson models an 80 percent advance plus a typical 1 percent "
                        "administration fee."
                    ),
                },
                {
                    "label": "Industry-average discount ceiling",
                    "value": 4.5,
                    "display": "Up to 4.5% per batch",
                    "conversion": "Industry average 3% to 4.5%",
                    "detail": "Per batch of receivables purchased, not annualized.",
                },
                {
                    "label": "Typical first-30-day discount",
                    "value": 3,
                    "display": "3% first 30 days",
                    "conversion": "Plus 1% for each additional period",
                    "detail": (
                        "Referral brokers earn 20 percent for the life of the deal through "
                        "Universal Funding Corporation."
                    ),
                },
            ],
        },
        {
            "diagram_id": "diag-03-licensing-exposure-waterfall",
            "chapter_number": 3,
            "chart_type": "waterfall",
            "title": "The Same $25,000, Licensed Versus Unlicensed",
            "subtitle": "California licensing cost against securities rescission exposure",
            "caption": (
                "Meeting California's commercial finance license costs a fee of $500 to $1,000 "
                "against a $25,000 net-worth floor, while selling another sponsor's security "
                "without a license can turn a $25,000 fee into a $1 million judgment."
            ),
            "assumptions_note": (
                "Two separate scenarios sit side by side. Bars one to three use Funder Intel's "
                "California figures at the high end of the fee range; bars four to six use "
                "Trowbridge Law Group's rescission example. Result bars are plain arithmetic."
            ),
            "note": "Sources are Funder Intel and Trowbridge Law Group.",
            "bars": [
                {
                    "label": "California net-worth floor",
                    "value": 25000,
                    "display": "$25,000",
                    "kind": "total",
                },
                {
                    "label": "License fee at the high end",
                    "value": -1000,
                    "display": "-$1,000 (range $500 to $1,000)",
                    "kind": "deduction",
                },
                {
                    "label": "Net worth after the license fee",
                    "value": 24000,
                    "display": "$24,000",
                    "kind": "result",
                },
                {
                    "label": "Fee for selling a $1M raise unlicensed",
                    "value": 25000,
                    "display": "$25,000",
                    "kind": "total",
                },
                {
                    "label": "Rescission judgment",
                    "value": -1000000,
                    "display": "-$1,000,000",
                    "kind": "deduction",
                },
                {
                    "label": "Net exposure after rescission",
                    "value": -975000,
                    "display": "-$975,000",
                    "kind": "result",
                },
            ],
        },
        {
            "diagram_id": "diag-04-broker-point-ranges",
            "chapter_number": 2,
            "chart_type": "horizontal_bars",
            "title": "Broker Point Ranges by Product",
            "subtitle": "Stated ranges and worked examples from practitioners",
            "unit": "broker points (% of funded amount)",
            "caption": (
                "Points vary sharply by product, from a single point on USDA B&I loans to "
                "double-digit points on some equipment deals."
            ),
            "assumptions_note": (
                "Typical values are the worked examples each speaker gave. The Equipment "
                "Finance Academy bar borrows Walton's $500k equipment example at 4% as its "
                "typical marker."
            ),
            "note": (
                "Sources are Shane Walton of the Commercial Loan Broker Institute, Eric "
                "Johnson of North Avenue Capital via Commercial Capital Training Group, Josh "
                "Feinberg of Leads For Locals, and Equipment Finance Academy."
            ),
            "bars": [
                {
                    "label": "Most financing products (Walton)",
                    "min": 1,
                    "max": 6,
                    "typical": 1.5,
                    "display": "1% to 6%, outliers to 15%; $2M at 1.5 points pays $30,000",
                },
                {
                    "label": "Broker point range (Walton)",
                    "min": 1,
                    "max": 10,
                    "typical": 1,
                    "display": "1 to 10 points; $2M at 1% pays $20,000",
                },
                {
                    "label": "USDA B&I loans (Johnson)",
                    "min": 1,
                    "max": 2,
                    "typical": 1,
                    "display": "Lender charges 2, usually passes 1; 1 point on $4-5M = $70,000-$80,000",
                },
                {
                    "label": "Equipment deals (Feinberg)",
                    "min": 3,
                    "max": 15,
                    "typical": 7.5,
                    "display": "3 to 15 points, 7.5-8% average across 10 years",
                },
                {
                    "label": "Equipment deals (Equipment Finance Academy)",
                    "min": 1,
                    "max": 5,
                    "typical": 4,
                    "display": "1% to 5%, $2,000 to $5,000 per deal",
                },
            ],
        },
        {
            "diagram_id": "diag-05-equipment-approval-gates",
            "chapter_number": 5,
            "chart_type": "decision_tree",
            "title": "Four Gates Before an Equipment File Goes Out",
            "subtitle": "Collateral, vendor, credit, and payment checks",
            "caption": (
                "The machine secures its own deal, so the asset, the vendor, the borrower's "
                "credit and the payment math each get screened before submission."
            ),
            "assumptions_note": (
                "Gate order is an operating sequence assembled from separate practitioners; "
                "thresholds are as each speaker stated them."
            ),
            "note": (
                "Sources are ION Capital - Loan Broker University, The Banking Podcast, ROK "
                "Financial with Ryan Vehey, Joe Camberato, and BizMoney Explained."
            ),
            "nodes": [
                {
                    "gate": "G1",
                    "question": (
                        "Can the lender resell every listed asset, with no existing UCC "
                        "filing on the equipment?"
                    ),
                    "pass_next": "G2",
                    "fail_action": (
                        "Stop; lenders will not take second position on an asset and want "
                        "recent units they can resell."
                    ),
                },
                {
                    "gate": "G2",
                    "question": "Are the seller and the invoice price verified as a real vendor sale?",
                    "pass_next": "G3",
                    "fail_action": (
                        "Fix before submission; underwriters catch the friend-down-the-street "
                        "invoice every time."
                    ),
                },
                {
                    "gate": "G3",
                    "question": (
                        "Does credit fit the program, such as 620-plus for application-only "
                        "leases to about $150,000, or 700-plus with comparable past debt for "
                        "startups?"
                    ),
                    "pass_next": "G4",
                    "fail_action": (
                        "Screen out very high revolving utilization, active collections and "
                        "auction-house purchases; push files under 50 percent utilization."
                    ),
                },
                {
                    "gate": "G4",
                    "question": (
                        "Does the payment survive weak demand, where $900 of incremental cash "
                        "against a $1,500 payment leaves a $600 monthly shortfall?"
                    ),
                    "pass_next": "Submit to the matched lender",
                    "fail_action": "Restructure the term or walk away.",
                },
            ],
        },
        {
            "diagram_id": "diag-06-dscr-underwriting-desk",
            "chapter_number": 11,
            "chart_type": "org_architecture",
            "title": "Who Sets the Bar on a DSCR or CRE File",
            "subtitle": "The broker at the center of four underwriting tests",
            "caption": (
                "DSCR is the gatekeeper metric, but the bar moves with the lender, the "
                "appraiser's rent schedule, and the debt-yield test."
            ),
            "assumptions_note": (
                "Spokes group practitioners by the test they apply; thresholds are quoted "
                "as stated and differ by asset class and lender."
            ),
            "note": (
                "Sources are SEI Mortgage - Ryan Marks, Real Estate Finance Academy with "
                "Trevor Calton, Brandon Turner, Academy For Commercial Lending, and Tactica RES."
            ),
            "center": {
                "role": "Commercial and DSCR loan broker",
                "headcount": "Broker of record",
                "focus": (
                    "Run DSCR at the broker's rent and at market rent, check debt yield, and "
                    "back into the maximum loan before offering."
                ),
            },
            "spokes": [
                {
                    "role": "Small-balance DSCR lender",
                    "type": "One-to-four and five-plus unit rentals (Ryan Marks)",
                    "kpi": (
                        "600 credit floor on one-to-four; 680 credit, 25% down, 6 months "
                        "reserves and 1.0 DSCR once past four units"
                    ),
                },
                {
                    "role": "Commercial underwriter",
                    "type": "NOI-based sizing (Trevor Calton)",
                    "kpi": "$100,000 NOI over 1.25x caps debt service at $80,000 a year",
                },
                {
                    "role": "Appraiser rent schedule",
                    "type": "Market rent the lender actually uses (Brandon Turner)",
                    "kpi": "$11 per unit separated 1.19 from a 1.2 target on his duplex",
                },
                {
                    "role": "Debt-yield test",
                    "type": "Refinance survivability (Academy For Commercial Lending, Tactica RES)",
                    "kpi": (
                        "Paid CMBS sat at 13.3% to 14.4% versus sub-10% failures; one deal "
                        "needed 60% LTV to clear a 10.5% bar"
                    ),
                },
            ],
        },
        {
            "diagram_id": "diag-07-equipment-lead-source-yield",
            "chapter_number": 4,
            "chart_type": "stacked_comparison",
            "title": "Funding Yield by Equipment Lead Source",
            "subtitle": "Percent of applications or leads that fund or close",
            "total_range": "Near 0% to 50% funded or closed, depending on the source",
            "caption": (
                "Dealer partnerships fund a far larger share of applications than bought "
                "leads or broad ad campaigns."
            ),
            "assumptions_note": (
                "Percentages are converted directly from stated ratios. The dealer figure is "
                "4-5 of 10; the shared-lead high end is one deal on 20 leads; the ad-campaign "
                "figure is the 'not even .01' Cheathem quoted."
            ),
            "note": (
                "Sources are Jermane Cheathem via Credit Suite, Josh Feinberg of Leads For "
                "Locals, and Equipment Finance Academy."
            ),
            "buckets": [
                {
                    "label": "Dealer partnerships",
                    "low": 40,
                    "high": 50,
                    "notes": "4-5 funded out of 10 weekly dealer applications (Cheathem)",
                },
                {
                    "label": "Exclusive bought leads",
                    "low": 3,
                    "high": 5,
                    "notes": "$50 per lead, 30-lead minimum at $1,500 a month (Feinberg)",
                },
                {
                    "label": "Shared bought leads",
                    "low": 0,
                    "high": 5,
                    "notes": "$40-80 per lead; $800 for 20 leads might close one deal",
                },
                {
                    "label": "Broad ad campaign",
                    "low": 0,
                    "high": 0.01,
                    "notes": "100 applications a day funded 'not even .01' (Cheathem's partner)",
                },
            ],
        },
        {
            "diagram_id": "diag-08-capital-stack-roadmap",
            "chapter_number": 12,
            "chart_type": "timeline_roadmap",
            "title": "Layering the Stack From Cheapest Money to Risk Capital",
            "subtitle": "Senior debt, bridge, tax credits, and litigation funding",
            "caption": (
                "Cheapest senior money goes in first; expensive risk capital is rented only "
                "where the gap demands it."
            ),
            "assumptions_note": (
                "The week-by-week sequence is an organizing order, not a timeline any speaker "
                "prescribed; every rate, price and ratio is as stated by the cited source."
            ),
            "note": (
                "Sources are Break Into CRE, Jeremiah Boucher of Patriot Holdings, Jason Prince "
                "via Tax Alpha Insider, and Statera Capital via The National Law Review."
            ),
            "weeks": [
                {
                    "week": "Week 1",
                    "title": "Map the capital stack",
                    "deliverable": (
                        "Senior debt at 50-65% of cost, with mezzanine and preferred equity "
                        "priced at 15-20% all-in (Break Into CRE)"
                    ),
                    "gate": "Senior capacity sized before any risk capital is sought",
                },
                {
                    "week": "Week 2",
                    "title": "Price the bridge loan",
                    "deliverable": (
                        "7-12% rate, 65-80% LTV, 1% up to 3-4% origination, close in 5-60 "
                        "days, with capex funding and a 12-month interest reserve requested"
                    ),
                    "gate": "Exit mapped and default provisions redlined by an attorney",
                },
                {
                    "week": "Week 3",
                    "title": "Place transferable tax credits",
                    "deliverable": (
                        "About 85 cents on the dollar, about 92 cents with insurance, parent "
                        "guarantees and Big-4 memos, about 80 cents for risk-takers"
                    ),
                    "gate": (
                        "Prevailing wage and apprenticeship records verified before paying "
                        "above the 80-cent tier"
                    ),
                },
                {
                    "week": "Week 4",
                    "title": "Approach litigation funders",
                    "deliverable": (
                        "Targeted pitch aiming at 2-4x returns, with realistic case value "
                        "near 10x the commitment"
                    ),
                    "gate": (
                        "NDA, budget, timeline and case outline in hand; only 3-5% of cases "
                        "are accepted"
                    ),
                },
            ],
        },
    ]


VOLUME_014_POSITIONING_ALTERNATIVES: List[Dict[str, Any]] = [
    {
        "title": "Paid at Funding",
        "subtitle": (
            "Points, Packaging Deposits, and Capital-Stack Math for the Commercial Loan Broker"
        ),
        "audience": (
            "New and residential-side brokers moving into commercial files who want to price "
            "points and stack repeat financing events per client"
        ),
        "research_basis": (
            "Walton's 1% to 6% fee range and $30,000 on a $2 million loan at 1.5 points, "
            "Neufer's $5,000 to $10,000 per-deal target and hair clause, and Walton's "
            "investor property paying three times through acquisition, rehab and permanent "
            "financing."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=3V8HTzwHS90&t=218s",
            "https://www.youtube.com/watch?v=v3GnrXphwvM&t=250s",
            "https://www.youtube.com/watch?v=uqs40-CCDSc&t=638s",
            "https://www.youtube.com/watch?v=7OHPVFeEmD4&t=637s",
        ],
        "validation_status": "Grounded strictly in Vol. 014 YouTube practitioner transcripts.",
    },
    {
        "title": "The Residual Broker",
        "subtitle": "Dealer-Channel Equipment Deals and Lifetime Factoring Commissions",
        "audience": (
            "Brokers, CPAs and consultants seeking recurring income from equipment vendors "
            "and B2B clients waiting 30, 60 or 90 days on invoices"
        ),
        "research_basis": (
            "Cheathem's 4-5 of 10 dealer applications funding, Feinberg's 7.5-8% average "
            "equipment points, Universal Funding's 20 percent lifetime referral commission, "
            "and Walton's 10% to 15% factoring residual on monthly factor fees."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=L2-ax8GoKVw&t=964s",
            "https://www.youtube.com/watch?v=Oq4y-D6sylo&t=1007s",
            "https://www.youtube.com/watch?v=3PlJmybrzHs&t=86s",
            "https://www.youtube.com/watch?v=3V8HTzwHS90&t=458s",
        ],
        "validation_status": "Grounded strictly in Vol. 014 YouTube practitioner transcripts.",
    },
    {
        "title": "Underwrite Before You Submit",
        "subtitle": "DSCR, Debt Yield, SBA Packaging, and MCA Debt Schedules That Lenders Fund",
        "audience": (
            "Brokers handling real estate, SBA acquisition, and stacked-MCA files who need "
            "packages that land in a lender's A bucket"
        ),
        "research_basis": (
            "Turner's run-DSCR-twice rule at the broker's rent and market rent, Academy For "
            "Commercial Lending's debt-yield split of 13.3% to 14.4% versus sub-10%, Siegel's "
            "written debt schedule from funder contracts, and the A-B-C lender bucket "
            "described at the Commercial Loan Broker Institute."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=-W2ThDxeu-o&t=928s",
            "https://www.youtube.com/watch?v=NHfs2vBPCys&t=186s",
            "https://www.youtube.com/watch?v=w-ETPb-Trek&t=236s",
            "https://www.youtube.com/watch?v=8-4I4VOIIqg&t=3124s",
        ],
        "validation_status": "Grounded strictly in Vol. 014 YouTube practitioner transcripts.",
    },
]
