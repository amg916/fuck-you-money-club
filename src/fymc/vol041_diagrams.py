"""Volume 041 diagrams: Buying Group, Commercial Card-Float & Rebate Arbitrage."""

from typing import Any, Dict, List

VOLUME_041_SUBTITLE: str = (
    "Buying-group spreads of 2-5 percent turned into points, $500-$1,000 orders that "
    "survive cancellation, liquidation fees of 5-6 percent netted against rewards, 0% intro "
    "stacks spaced six months apart, Plum 60-day float vs. the 1.5 percent early-pay discount, "
    "Spark and Ink flat-rate engines, Amex financial-review survival, and portal stacks that "
    "only pay when every statement is cleared in full"
)


def build_volume_041_diagrams_data() -> List[Dict[str, Any]]:
    """Return the eight structured diagram dicts for Volume 041."""
    return [
        {
            "diagram_id": "diag-01-buying-group-order-survival",
            "chapter_number": 1,
            "title": "Buying-Group Order Survival Loop",
            "subtitle": "Reserve, buy capped units, ship to the posted address, log the SKU, collect ACH",
            "chart_type": "process_flow",
            "stages": [
                {
                    "step": "01",
                    "label": "Reserve the Deal First",
                    "value": "Step 1",
                    "detail": (
                        "Commit before researching, because reservations hold only a 12 to 24 hour "
                        "window (Lets Get To The Points)."
                    ),
                },
                {
                    "step": "02",
                    "label": "Buy in $500-$1,000 Orders",
                    "value": "Step 2",
                    "detail": (
                        "Keep each checkout between $500 and $1,000 after a $2,000 Target order was "
                        "flagged; pay through PayPal, Apple Pay or Shop Pay with the billing address "
                        "set to the prep center (John Muscarello)."
                    ),
                },
                {
                    "step": "03",
                    "label": "Ship Only to Posted Address",
                    "value": "Step 3",
                    "detail": (
                        "Ignore Discord DMs from 'admins'; impersonators redirected about $20k of goods "
                        "(Geobreeze Travel)."
                    ),
                },
                {
                    "step": "04",
                    "label": "Log the Exact SKU",
                    "value": "Step 4",
                    "detail": (
                        "Wrong color or model means no reimbursement and payout prices can change; do not "
                        "resubmit failed orders while pending charges take 5-7 days (Lets Get To The Points, "
                        "John Muscarello)."
                    ),
                },
                {
                    "step": "05",
                    "label": "Collect ACH and Keep the Points",
                    "value": "Step 5",
                    "detail": (
                        "The spread usually runs 2-5 percent, rarely 10; about $250,000 a year at 4x is "
                        "roughly 1M points (Frequent Miler)."
                    ),
                },
            ],
            "caption": (
                "Members buy household-capped items on their own cards, ship to the group warehouse, "
                "get reimbursed by ACH or check, and keep the rewards."
            ),
            "assumptions_note": (
                "Margins and order sizes are as reported by the named practitioners; never float more "
                "than the bank balance, after an attendee reported losing $60,000 (Geobreeze Travel)."
            ),
            "note": (
                "Sources - Frequent Miler, John Muscarello, Lets Get To The Points, Geobreeze Travel, "
                "Czech It Out Money Hacks."
            ),
        },
        {
            "diagram_id": "diag-02-spark-cash-plus-spend-ladder",
            "chapter_number": 6,
            "title": "Spark Cash Plus Spend Ladder",
            "subtitle": "Where the flat 2 percent charge card pays, from $1M framing down to a single award seat",
            "chart_type": "funnel",
            "stages": [
                {
                    "label": "Every $1 Million Spent",
                    "value": 1000000,
                    "display": "$1,000,000",
                    "conversion": "$20,000 back at 2%",
                    "detail": (
                        "Ryan Maya runs inventory, software and Facebook ads through the card and reports "
                        "over $50,000 in cash back over a few years."
                    ),
                },
                {
                    "label": "Annual Fee Refund Threshold",
                    "value": 150000,
                    "display": "$150,000",
                    "conversion": "$150 fee credited back",
                    "detail": "Capital One credits the annual fee once yearly spend reaches $150,000 (Bytes Media).",
                },
                {
                    "label": "Beats No-Fee 1.5% Cards",
                    "value": 30000,
                    "display": "$30,000",
                    "conversion": "Both net $450",
                    "detail": "Above about $30,000 a year the 2% card minus its fee beats 1.5% no-fee cards (Ask Sebby Business).",
                },
                {
                    "label": "Break-Even on the Fee",
                    "value": 7500,
                    "display": "$7,500",
                    "conversion": "2% covers $150",
                    "detail": "Solved $150 = 2% times spend for the break-even line (Ask Sebby Business).",
                },
                {
                    "label": "Cash Back Shared Into Miles",
                    "value": 1320,
                    "display": "$1,320",
                    "conversion": "132,000 miles, ~$8,500 seat",
                    "detail": (
                        "Spark cash back moved into Capital One miles, then 130,000 Singapore miles for a "
                        "JFK to Singapore saver award (Ask Sebby Business)."
                    ),
                },
            ],
            "caption": (
                "Spark Cash Plus is a no-preset-limit charge card paying a flat 2% that must be cleared "
                "every month; the highest-leverage exit converts cash back into partner miles."
            ),
            "assumptions_note": (
                "Spark products pull all three personal bureaus and report to personal credit, which "
                "affects Chase 5/24 math (Just Money Ish, HowToCredit); a 2.99% late fee applies to unpaid "
                "statement balances (Bytes Media)."
            ),
            "note": "Sources - Ask Sebby Business, Bytes Media, Ryan Maya, Just Money Ish, HowToCredit.",
        },
        {
            "diagram_id": "diag-03-velocity-banking-cycle",
            "chapter_number": 3,
            "title": "Velocity Banking Cycle on a $4,000 Card",
            "subtitle": "Maria's paycheck push and the cash-flow surplus that makes it work",
            "chart_type": "waterfall",
            "bars": [
                {"label": "Card balance before payday", "value": 4000, "display": "$4,000", "kind": "total"},
                {"label": "Paycheck pushed on day one", "value": 3500, "display": "-$3,500", "kind": "deduction"},
                {"label": "Residual balance after push", "value": 500, "display": "$500", "kind": "result"},
                {"label": "Paycheck income for the month", "value": 3500, "display": "$3,500", "kind": "total"},
                {"label": "Living expenses charged back on", "value": 3200, "display": "-$3,200", "kind": "deduction"},
                {"label": "Monthly cash-flow surplus", "value": 300, "display": "$300", "kind": "result"},
            ],
            "caption": (
                "Pushing the paycheck onto the card crushes the average daily balance; the $500 residual "
                "at 19% APR costs about $7.87 over 30 days (Stephen Smith)."
            ),
            "assumptions_note": (
                "The $300 surplus is the arithmetic gap between the $3,500 paycheck and $3,200 of expenses "
                "in the example; velocity pushes only work with positive cash flow, even $100 a month."
            ),
            "note": "Source - Stephen Smith; float discipline echoed by Joey of Amazon FBA and Mogulnomics.",
        },
        {
            "diagram_id": "diag-04-credit-to-cash-cost-ranges",
            "chapter_number": 2,
            "title": "Credit-to-Cash Conversion Costs",
            "subtitle": "Liquidators, invoice routes and balance-transfer checks compared",
            "chart_type": "horizontal_bars",
            "unit": "percent of amount converted",
            "bars": [
                {"label": "Credit card liquidator fee", "min": 5, "max": 6, "typical": 5.5, "display": "5% to 6% (Alex Barajas)"},
                {"label": "Balance-transfer checks", "min": 3, "max": 5, "typical": 4, "display": "3% to 5%"},
                {"label": "Net liquidation cost after rewards", "min": 4, "max": 4, "typical": 4, "display": "About 4% (Naam Wynn)"},
                {"label": "Invoice and PayPal routes", "min": 2, "max": 3, "typical": 2.5, "display": "About 2% to 3%"},
                {"label": "Card rewards netted back", "min": 2, "max": 2, "typical": 2, "display": "2% card rewards (Naam Wynn)"},
            ],
            "caption": (
                "Credit converted to cash only pays when a buyer, exit or repayment plan is locked before "
                "the swipe; Naam Wynn nets 2% rewards against a 6%+ liquidator fee for a real cost near 4%."
            ),
            "assumptions_note": (
                "Typical marks the midpoint where only a range was quoted. Send $100 through any route and "
                "confirm it lands before moving thousands; 1099-K reporting threshold was $5,000 for 2024 "
                "(James Baker CPA)."
            ),
            "note": "Sources - Alex Barajas, Naam Wynn, Geobreeze Travel, James Baker CPA, Frequent Miler.",
        },
        {
            "diagram_id": "diag-05-amex-review-gates",
            "chapter_number": 5,
            "title": "Amex Financial Review Survival Gates",
            "subtitle": "Spend curve, payment-app hygiene, spending-power checks and the 14-day window",
            "chart_type": "decision_tree",
            "nodes": [
                {
                    "gate": "G1",
                    "question": "Is spend ramping on a curve, 5K then 10K then 15K across months?",
                    "pass_next": "G2",
                    "fail_action": (
                        "Slow the ramp and call ahead before any massive purchase; high-velocity spending "
                        "sat behind 65% of reviewed cases (Colin Matthew, Cal Barton)."
                    ),
                },
                {
                    "gate": "G2",
                    "question": "Are PayPal, Cash App, Square and Venmo transfers kept off the Amex?",
                    "pass_next": "G3",
                    "fail_action": "Move family money to Amex Send and Split instead (Cal Barton).",
                },
                {
                    "gate": "G3",
                    "question": "Is check spending power used sparingly, never more than three times a day?",
                    "pass_next": "G4",
                    "fail_action": (
                        "Reserve it for purchases above the six-month average spend (CardRight, Cal Barton)."
                    ),
                },
                {
                    "gate": "G4",
                    "question": "If a review letter lands, are the requested documents sent within 14 days?",
                    "pass_next": "Accounts likely retained; 25 of 28 reported decisions kept some accounts",
                    "fail_action": (
                        "Call the number on the back of the card the same day and transfer out points you "
                        "plan to use before the decision lands (Colin Matthew, AskSebby)."
                    ),
                },
            ],
            "caption": (
                "Reviews freeze every personal and business card plus Membership Rewards until income is "
                "documented; send exactly what is asked, even if the numbers are off."
            ),
            "assumptions_note": (
                "Case counts come from Cal Barton's samples of 20 and 40 cases; 12 of the 25 retained "
                "cases still reported lower limits, fixed limits or closed cards."
            ),
            "note": "Sources - Cal Barton, Colin Matthew, CardRight, RJ Financial, AskSebby.",
        },
        {
            "diagram_id": "diag-06-capital-one-shopping-desk",
            "chapter_number": 11,
            "title": "Targeted-Offer and Transfer Desk",
            "subtitle": "Capital One Shopping offers, the $80 referral, and cents-per-point transfer hurdles",
            "chart_type": "org_architecture",
            "center": {
                "role": "Offer and Transfer Operator",
                "headcount": "Solo operator",
                "focus": (
                    "Browse, log out, return for targeted offers; run Capital One Shopping and Rakuten in "
                    "separate browsers; screenshot every offer and claim after 30 days."
                ),
            },
            "spokes": [
                {
                    "role": "Targeted Offer Hunter",
                    "type": "Portal offers",
                    "kpi": "$45 back on $75 and $160 back on $200; over $500 in three months (Michael Martinez)",
                },
                {
                    "role": "Referral Bonus Runner",
                    "type": "Signup bonus",
                    "kpi": "$80 on a $1 Finish Line donation after a 90-day wait (Nate Bind)",
                },
                {
                    "role": "Transfer Partner Analyst",
                    "type": "Points redemption",
                    "kpi": "2 cents per point hurdle; Grand Hyatt Vail at 2.2 cents (AskSebby)",
                },
                {
                    "role": "Transfer Bonus Watcher",
                    "type": "Promotional bonus",
                    "kpi": "80% Chase-to-IHG bonus lifts 0.6 to 1.08 cents per point (Ben Hedges)",
                },
            ],
            "caption": (
                "The default 0.5 to 2 percent portal rate is noise; the money sits in targeted offers, the "
                "$80 referral, and transfers that clear a cents-per-point hurdle."
            ),
            "assumptions_note": (
                "Payouts land only as gift cards and take one to three months; transfers are not "
                "reversible, so price the award first (Thrive Media, Mark Reese)."
            ),
            "note": "Sources - Michael Martinez, Nate Bind, AskSebby, Ben Hedges, Mark Reese, Twin Finances.",
        },
        {
            "diagram_id": "diag-07-credit-limit-ladders",
            "chapter_number": 4,
            "title": "Reported Credit Limit Ladders",
            "subtitle": "Starting limit to reported peak across four practitioner cases",
            "chart_type": "stacked_comparison",
            "total_range": "$1K to $66K reported across four ladders",
            "buckets": [
                {
                    "label": "Navy Federal limit climb",
                    "low": 10000,
                    "high": 66000,
                    "notes": "Jan 2020 to Feb 2024 in roughly $8K steps, requests spaced 190-195 days (Cal Barton).",
                },
                {
                    "label": "Capital One increase ladder",
                    "low": 1000,
                    "high": 30800,
                    "notes": "Three +$100 bumps, then +$2,500, +$7,000 and +$20K; 6 months called the sweet spot (Cal Barton).",
                },
                {
                    "label": "Navy Federal deposit seasoning",
                    "low": 2000,
                    "high": 18000,
                    "notes": "$250 opening deposit plus $500 biweekly direct deposit preceded the jump (Stephen Smith).",
                },
                {
                    "label": "Chase Sapphire reallocation",
                    "low": 10000,
                    "high": 25000,
                    "notes": "Cutting a Sapphire from $25K to $10K opened room for a $30K Ink Business Preferred (Naam Wynn).",
                },
            ],
            "caption": (
                "Limits follow stated income and heavy, cleanly repaid usage; Chase caps total exposure "
                "near 50% of income and Amex near 35%."
            ),
            "assumptions_note": (
                "Cycle one to three times a month with each charge under 70% of the line; after a denial "
                "wait three months on a soft pull or six on a hard pull (Colin Matthew, Stephen Smith)."
            ),
            "note": "Sources - Cal Barton, Stephen Smith, Naam Wynn, Colin Matthew.",
        },
        {
            "diagram_id": "diag-08-wallet-fee-math-roadmap",
            "chapter_number": 12,
            "title": "Wallet and Premium Fee Math Roadmap",
            "subtitle": "Pay-in-full floor, catch-all core, fee audits and rule-change rebuilds",
            "chart_type": "timeline_roadmap",
            "weeks": [
                {
                    "week": "Week 1",
                    "title": "Pay-in-Full Floor",
                    "deliverable": "Autopay set to clear every statement; every 0% window mapped to a payoff date.",
                    "gate": "Full balance paid before any 0% window closes; 18 to 25 percent APR wipes out rewards (Fat Stacks Academy).",
                },
                {
                    "week": "Week 2",
                    "title": "Catch-All Core Plus Specialists",
                    "deliverable": "A 2x or 2% catch-all wrapped by category cards, close to 3% blended (Rob Berger).",
                    "gate": "Blue Cash Preferred only if supermarket spend tops about $264 a month (Dutcher Capital).",
                },
                {
                    "week": "Week 3",
                    "title": "Premium Fee Audit",
                    "deliverable": "Gold scored at +$199 vs -$85 and Platinum at +$1,000 vs -$715 by credit capture.",
                    "gate": "Count only credits that replace existing spend (Card & Capital, Leo's Travel Hacks).",
                },
                {
                    "week": "Week 4",
                    "title": "Rule-Change Rebuild",
                    "deliverable": "Hotel credit plans rebuilt around the FHR 2-night minimum from January 1, 2027.",
                    "gate": "Gold opened before Platinum because of Amex family language (Ben Hedges, Leo's Travel Hacks).",
                },
            ],
            "caption": (
                "Fee math is a utilization test; Fat Stacks Academy layered a 0% APR float on the Blue "
                "Business Plus for $926.66 profit on $12,282.88 of spend."
            ),
            "assumptions_note": (
                "Week sequencing is an organizing frame; every figure is as reported by the named "
                "practitioner, and the $861.34 figure reflects a 15% tax set-aside."
            ),
            "note": (
                "Sources - Fat Stacks Academy, Rob Berger, Dutcher Capital, Leo's Travel Hacks, "
                "Card & Capital, Ben Hedges."
            ),
        },
    ]


VOLUME_041_POSITIONING_ALTERNATIVES: List[Dict[str, Any]] = [
    {
        "title": "The Float Desk",
        "subtitle": "0% Intro Stacks, Net-60 Charge Cards and the 30-Day Clear",
        "audience": "Online and retail arbitrage sellers financing inventory on business cards",
        "research_basis": (
            "Joey of Amazon FBA runs $277,000 in card credit with almost $142,000 at 0%, Jack McColl "
            "targets Elan's 18-month 0% cards at up to $50,000, Stephen Smith stretches the Plum toward "
            "roughly 90 days, and Jake Broe equates skipping the 1.5% discount to about an 18% APR."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=tKw8SljNcPE&t=637s",
            "https://www.youtube.com/watch?v=c5MGulNCfZ8&t=389s",
            "https://www.youtube.com/watch?v=zOrHXaEEgxk&t=651s",
            "https://www.youtube.com/watch?v=UdDb_X5YHDI&t=407s",
        ],
        "validation_status": "Grounded strictly in Vol. 041 YouTube practitioner transcripts.",
    },
    {
        "title": "Order Survival",
        "subtitle": "Buying Groups and Gift Card Resale at Points-First Margins",
        "audience": "Points earners running near break-even volume for spend and status",
        "research_basis": (
            "Frequent Miler pegs buying-group spreads at 2-5 percent and about $250,000 at 4x as roughly "
            "1M points, John Muscarello keeps orders at $500 to $1,000, Geobreeze Travel reports QCGC "
            "buying Walmart cards at 91.5% and warns never to float more than cash on hand."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=nMlQUH3s8qY&t=2309s",
            "https://www.youtube.com/watch?v=ThO9ard-k8E&t=204s",
            "https://www.youtube.com/watch?v=QTa7eNv00k4&t=1716s",
            "https://www.youtube.com/watch?v=zay5oOKCEls&t=1091s",
        ],
        "validation_status": "Grounded strictly in Vol. 041 YouTube practitioner transcripts.",
    },
    {
        "title": "Review-Proof Rewards",
        "subtitle": "Stacking Portals and Transfers Without Tripping an Amex Shutdown",
        "audience": "High-spend cardholders stacking portals, card offers and transfer partners",
        "research_basis": (
            "Cal Barton finds high-velocity spending behind 65% of financial reviews, Everyday Money "
            "Heroes nets a $200 Nike order to $141.10 across four layers, and AskSebby holds transfers "
            "to a 2 cents per point hurdle."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=0pnnp262mLg&t=727s",
            "https://www.youtube.com/watch?v=3dq0zRBwn8E&t=617s",
            "https://www.youtube.com/watch?v=HbZGYalSsyc&t=1141s",
            "https://www.youtube.com/watch?v=Uvyem-_QFhI&t=540s",
        ],
        "validation_status": "Grounded strictly in Vol. 041 YouTube practitioner transcripts.",
    },
]
