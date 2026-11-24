"""Volume 021 diagrams: Automated E-Commerce.

Every figure, workflow and threshold below is attributed to a named
practitioner or channel and cited by video ID and timestamp.
"""

from typing import Any, Dict, List

VOLUME_021_SUBTITLE: str = (
    "Authorized-dealer dropshipping on $1,000-plus US brands, supplier accounts "
    "won by persistent outreach, contribution margin before CAC, landed cost "
    "beyond the invoice, a shorter cash cycle, register-first sales tax, "
    "tested 3PLs, scam-proof automation, budgeted returns, AI support with "
    "human refund gates, feed-first Google Shopping, and scaling on CAC payback"
)


def build_volume_021_diagrams_data() -> List[Dict[str, Any]]:
    """Return the eight structured Volume 021 diagram specifications."""
    return [
        {
            "diagram_id": "diag-01-high-ticket-dealer-launch-sequence",
            "chapter_number": 1,
            "chart_type": "process_flow",
            "title": "High-Ticket Authorized-Dealer Launch Sequence",
            "subtitle": "From keyword validation to Google Shopping on $1,000-plus US-brand products",
            "caption": (
                "Authorized-dealer operators list $1,000-plus products from established "
                "US brands, collect payment first, and let the supplier ship. Kenny's "
                "store reached about $207,953 in a month on $4,376.72 of ad spend."
            ),
            "assumptions_note": (
                "Step order follows the research mechanics practitioners describe. "
                "Realistic net margin is 15-20% of gross revenue per Joe Verschoor; "
                "MAP compliance tops out near 90% per built with ali."
            ),
            "note": (
                "Sources: Joe Verschoor [uxvzRhKmdXU @ 00:04:18; 5jY7d_1m1t0 @ 00:06:13], "
                "built with ali [pbk_t9e4Xpo @ 00:11:56; Mf4bZiQ2-Fc @ 00:16:02], "
                "Ecommerce Paradise [EaAeDMJIPLQ @ 00:02:06], Peak Flow Media "
                "[YmrOjrklnxM @ 00:10:02], Asonjf [91zki-xXArY @ 00:37:42]."
            ),
            "stages": [
                {
                    "step": "01",
                    "label": "Validate demand",
                    "value": "Step 1",
                    "detail": (
                        "Check WordStream or Semrush for high search volume plus low "
                        "keyword difficulty; drop anything seasonal or under $1,000."
                    ),
                },
                {
                    "step": "02",
                    "label": "Benchmark online-only dealers",
                    "value": "Step 2",
                    "detail": (
                        "Search 'buy [brand] [product]' in the Shopping tab and rule out "
                        "dealers with physical locations or 'appointment required'."
                    ),
                },
                {
                    "step": "03",
                    "label": "Confirm strict MAP",
                    "value": "Step 3",
                    "detail": (
                        "Compare the identical model and size across sellers; expect "
                        "about 90% compliance at best."
                    ),
                },
                {
                    "step": "04",
                    "label": "Price dispute exposure into margin",
                    "value": "Step 4",
                    "detail": (
                        "Load chargeback, restocking, return-shipping and labor-warranty "
                        "costs into each brand's margin before listing it."
                    ),
                },
                {
                    "step": "05",
                    "label": "Launch on Google Shopping",
                    "value": "Step 5",
                    "detail": (
                        "Bid bottom-of-funnel terms first, such as 'Samsung TV 36 in', "
                        "and push Meta to remarketing."
                    ),
                },
            ],
        },
        {
            "diagram_id": "diag-02-sales-tax-compliance-cycle",
            "chapter_number": 6,
            "chart_type": "funnel",
            "title": "Sales Tax Compliance Cycle",
            "subtitle": "Nexus, register, calculate, sort marketplace sales, then file and remit",
            "caption": (
                "Since the 2018 Wayfair ruling, most states key economic nexus to "
                "$100,000 in sales or 200 transactions, and Avalara and LedgerGurus "
                "both insist on registering before collecting."
            ),
            "assumptions_note": (
                "Funnel widths are ordinal stage positions (5 down to 1), not measured "
                "volumes. Dollar and count figures in each display are the practitioner "
                "numbers; California, New York and Texas set higher thresholds."
            ),
            "note": (
                "Sources: Cherry Bekaert [rUvJ4UwGqiA @ 00:01:00; 00:00:24], Avalara "
                "[EtT3YoVfP0c @ 00:19:36; 00:38:55; QiT660QtcXA @ 00:01:18], "
                "Arthur Glinkin [1Cr_iHc8p4s @ 00:07:44], LedgerGurus "
                "[-DhtTN5_Rh4 @ 00:12:28; 00:13:07]."
            ),
            "stages": [
                {
                    "label": "Nexus test",
                    "value": 5,
                    "display": "$100,000 in sales or 200 transactions",
                    "conversion": "Map every employee, rep, office and Amazon or 3PL inventory location",
                    "detail": "Each of those creates physical nexus on its own (Cherry Bekaert).",
                },
                {
                    "label": "Register before collecting",
                    "value": 4,
                    "display": "Permit issued first",
                    "conversion": "No collection enabled until the permit is in hand",
                    "detail": "Collecting unregistered creates personal officer liability (Avalara).",
                },
                {
                    "label": "Calculate the rate",
                    "value": 3,
                    "display": "13,000 permutations changing monthly",
                    "conversion": "Engine handles rate, rule and boundary changes",
                    "detail": "ZIP 30024 spans three counties (Avalara webinar presenters).",
                },
                {
                    "label": "Sort marketplace and direct sales",
                    "value": 2,
                    "display": "Amazon, Walmart and Etsy collect",
                    "conversion": "Shopify is not a facilitator, so that tax stays with the seller",
                    "detail": "Marketplace-collected sales are already handled (Avalara).",
                },
                {
                    "label": "File and remit",
                    "value": 1,
                    "display": "About $30-35 per TaxJar filing; $40-50 per Avalara return",
                    "conversion": "Approve returns before the platform cutoff",
                    "detail": (
                        "Avalara auto-files after the 11th at 5 PM ET; TaxJar's deadline "
                        "is the 5th (LedgerGurus)."
                    ),
                },
            ],
        },
        {
            "diagram_id": "diag-03-margin-to-cac-waterfall",
            "chapter_number": 3,
            "chart_type": "waterfall",
            "title": "From Per-Order Margin to an Affordable CAC",
            "subtitle": "Two worked examples of contribution margin before and after acquisition cost",
            "caption": (
                "Common Thread Collective turns $53 of fuel profit minus a $20 net "
                "target into a $33 target CAC. Eric Andrews' two-for-one re-run of a "
                "50%-off Black Friday leaves $36 of contribution margin after CAC."
            ),
            "assumptions_note": (
                "Andrews' CAC bar is the gap between his reported $69 contribution "
                "margin per order and $36 after CAC. The 50%-off version produced "
                "only $29 contribution margin per order before CAC."
            ),
            "note": (
                "Sources: Common Thread Collective (as summarized for Chapter Q3), "
                "Eric Andrews [t2H3gJHuw6k @ 00:08:56; 00:07:15; gG33a-ErNRQ @ 00:15:10]."
            ),
            "bars": [
                {"label": "Fuel profit per order (CTC)", "value": 53, "display": "$53", "kind": "total"},
                {"label": "Net profit target (CTC)", "value": -20, "display": "-$20", "kind": "deduction"},
                {"label": "Target CAC (CTC)", "value": 33, "display": "$33", "kind": "result"},
                {"label": "Two-for-one contribution margin (Andrews)", "value": 69, "display": "$69", "kind": "total"},
                {"label": "Acquisition cost per order (Andrews)", "value": -33, "display": "-$33", "kind": "deduction"},
                {"label": "Contribution margin after CAC (Andrews)", "value": 36, "display": "$36", "kind": "result"},
            ],
        },
        {
            "diagram_id": "diag-04-supplier-account-ranges",
            "chapter_number": 2,
            "chart_type": "horizontal_bars",
            "title": "Supplier Account Ranges Practitioners Report",
            "subtitle": "Acceptance, markup, margin floor, quote close rate and MAP compliance",
            "unit": "percent",
            "caption": (
                "Ecommerce Paradise reports 30-50% acceptance when applying to 10-20 "
                "brands at once, while Daniel Boufford pegs distributor markups at "
                "20-50% over brand direct."
            ),
            "assumptions_note": (
                "No practitioner gave a midpoint, so each typical marker sits at the "
                "low end of the quoted range. The quote close rate restates one sale "
                "per twenty quotes as a percentage."
            ),
            "note": (
                "Sources: Ecommerce Paradise [hHXf1_WdANY @ 00:17:39; 00:09:24], "
                "Daniel Boufford [jYFh4ucNZuw @ 00:00:15], Build Assets Online "
                "[ocjVuvj0QJg @ 00:04:14], built with ali [pbk_t9e4Xpo @ 00:21:56]."
            ),
            "bars": [
                {
                    "label": "Acceptance on batch applications",
                    "min": 30,
                    "max": 50,
                    "typical": 30,
                    "display": "30-50% when applying to 10-20 brands",
                },
                {
                    "label": "Distributor markup over brand direct",
                    "min": 20,
                    "max": 50,
                    "typical": 20,
                    "display": "20-50% markup",
                },
                {
                    "label": "Supplier margin walk-away line",
                    "min": 10,
                    "max": 15,
                    "typical": 10,
                    "display": "Reject suppliers under 10-15% margin",
                },
                {
                    "label": "Sale rate on high-ticket quotes",
                    "min": 5,
                    "max": 5,
                    "typical": 5,
                    "display": "About one sale per twenty quotes",
                },
                {
                    "label": "MAP compliance ceiling",
                    "min": 90,
                    "max": 90,
                    "typical": 90,
                    "display": "About 90% compliance at best",
                },
            ],
        },
        {
            "diagram_id": "diag-05-cash-cycle-gates",
            "chapter_number": 5,
            "chart_type": "decision_tree",
            "title": "Cash Conversion Cycle Gates",
            "subtitle": "Inventory days plus sales days minus payable days, checked before cash leaves",
            "caption": (
                "Kurtis Hanni cut a client's cycle from 230 to 45 days, slashing required "
                "cash from $235,000 to $67,000; LedgerGurus typically sees e-commerce "
                "cycles of at least 90 days."
            ),
            "assumptions_note": (
                "Gate order runs from purchasing through exit. The 37.2% figure is One "
                "Minute Finance's annualized cost of letting a 2/10 net 30 discount lapse."
            ),
            "note": (
                "Sources: Kurtis Hanni [0WBeNhRVKHY @ 00:09:32; 00:11:29], One Minute "
                "Finance [7yuWFm95LDw @ 00:07:28], LedgerGurus [F-Y1cubdesE @ 00:06:24], "
                "Brent Freeman - The CBB Group [KSfESWIcDGI @ 00:09:41]."
            ),
            "nodes": [
                {
                    "gate": "G1",
                    "question": "Does cash cover the full cycle before an overseas order with zero payable days?",
                    "pass_next": "G2",
                    "fail_action": (
                        "Hold the order and negotiate billing on arrival; the 230-day client "
                        "needed $235,000 out before a dollar returned."
                    ),
                },
                {
                    "gate": "G2",
                    "question": "Is every 2/10 net 30 early-pay discount being captured?",
                    "pass_next": "G3",
                    "fail_action": (
                        "Pay within 10 days; holding cash 20 extra days costs 37.2% annualized."
                    ),
                },
                {
                    "gate": "G3",
                    "question": "Has net 60 wholesale been modeled for the receivables jump and inventory build?",
                    "pass_next": "G4",
                    "fail_action": (
                        "Model receivables and inventory before signing; revenue can sit "
                        "on the books without the cash."
                    ),
                },
                {
                    "gate": "G4",
                    "question": "Before going to market, is the 12- to 24-month average working capital computed?",
                    "pass_next": "Proceed to sale",
                    "fail_action": (
                        "Compute the average and pull excess capital out, or the buyer "
                        "negotiates to keep it."
                    ),
                },
            ],
        },
        {
            "diagram_id": "diag-06-shopping-feed-ownership",
            "chapter_number": 11,
            "chart_type": "org_architecture",
            "title": "Google Shopping Feed Ownership Map",
            "subtitle": "In Shopping and Performance Max the feed is the targeting",
            "caption": (
                "Operators front-load titles with the converting search term, keep price "
                "and availability identical to the site, never change product IDs, and "
                "segment with custom labels by margin, price bucket and season."
            ),
            "assumptions_note": (
                "Practitioners did not specify team size; roles describe the feed "
                "responsibilities they name, which one operator may hold together."
            ),
            "note": (
                "Sources: Grow My Ads [hY8ZBC3A4uQ @ 00:10:45; 00:13:00], Ecom Chris "
                "[d9kULGtUBD4 @ 00:12:01; XQTEnn-3t0E @ 00:23:16], Max Crakanthorp "
                "[H4yH9xs030Q @ 00:13:46], KeyCommerce [S1NhYxaPnic @ 00:06:21], "
                "Tim Sutton [APb0cOGKROE @ 00:05:06]."
            ),
            "center": {
                "role": "Feed owner",
                "headcount": "Not specified by practitioners",
                "focus": (
                    "Locks product IDs and edits inside the feed app; poorly optimized "
                    "feeds pay 2-3x the CPC (Ecom Chris)."
                ),
            },
            "spokes": [
                {
                    "role": "Title and category editor",
                    "type": "Feed content",
                    "kpi": "10x clicks and impressions on the Home Reserve sofa retitle; 20-30% more sales on a jacket retitle",
                },
                {
                    "role": "Image curator",
                    "type": "Creative assets",
                    "kpi": "2-3x CTR lift from lifestyle images added behind the white-background main",
                },
                {
                    "role": "Price and promotion auditor",
                    "type": "Compliance",
                    "kpi": "Sale price identical to the live site; promotion end time set to 11:59 p.m.",
                },
                {
                    "role": "Custom label segmenter",
                    "type": "Bidding structure",
                    "kpi": "Price buckets from 100 to 10,000 with a 2,000+ label on its own tROAS",
                },
            ],
        },
        {
            "diagram_id": "diag-07-landed-cost-stack",
            "chapter_number": 4,
            "chart_type": "stacked_comparison",
            "title": "Landed Cost Stack Behind a $10 Supplier Price",
            "subtitle": "Goods plus freight, duty and fees divided by units received",
            "total_range": "$12,000 landed on 1,000 units, or $12 per unit versus a $10 supplier price",
            "caption": (
                "Intel by CandiMentor's worked example shows the supplier invoice is only "
                "the starting point; freight, duty and fees add $2,000 across 1,000 units."
            ),
            "assumptions_note": (
                "Low and high are equal because the example reports single figures. "
                "Trade Counsel separately stacks 3.4%, 7.5% and 12.5% into 23.4% duty "
                "on Chinese plastic bins."
            ),
            "note": (
                "Sources: Intel by CandiMentor [CvHvBnjwlJg @ 00:05:57], Trade Counsel "
                "[-WXoF_u08g0 @ 00:01:56], SKUio [DFZ8XDRkuCE @ 00:00:20]."
            ),
            "buckets": [
                {"label": "Product", "low": 10000, "high": 10000, "notes": "Supplier invoice for 1,000 units"},
                {"label": "Freight", "low": 1200, "high": 1200, "notes": "Keep freight separate on the invoice and bill of lading"},
                {"label": "Duty", "low": 500, "high": 500, "notes": "Often arrives weeks later on the broker's bill (SKUio)"},
                {"label": "Fees", "low": 300, "high": 300, "notes": "Broker and handling fees"},
            ],
        },
        {
            "diagram_id": "diag-08-scaling-readiness-roadmap",
            "chapter_number": 12,
            "chart_type": "timeline_roadmap",
            "title": "Scaling Readiness Roadmap",
            "subtitle": "Speed, breakeven math, payback and capacity before more spend",
            "caption": (
                "Operators treat conversion and scaling as one math problem: revenue per "
                "visitor, contribution profit and CAC payback decide whether more traffic "
                "makes money."
            ),
            "assumptions_note": (
                "Week sequencing orders the practitioners' gates; no speaker prescribed "
                "a four-week schedule. Average Shopify conversion is 1 to 3% per "
                "Davie Fogarty Mentors."
            ),
            "note": (
                "Sources: Chase Chappell [daDsoHXE52A @ 00:01:49; 00:23:30], Adam "
                "Callinan [VCXWZQgbKXw @ 00:25:39], Leading Social [KpmUvCBEKK4 @ 00:01:48], "
                "Frankly eCommerce [CCtunt0iWMU @ 00:07:53]."
            ),
            "weeks": [
                {
                    "week": "Week 1",
                    "title": "Fix page speed",
                    "deliverable": "Compress high-resolution images with Tiny Image Optimizer before other CRO work",
                    "gate": "Each 1-second delay costs 7% of conversion (Chase Chappell)",
                },
                {
                    "week": "Week 2",
                    "title": "Set breakeven ROAS by budget",
                    "deliverable": "Breakeven ROAS from fixed costs and variable margin at each planned spend level",
                    "gate": "Runs 22 at $10k spend, 6 at $50k and 4 at $100k (Adam Callinan)",
                },
                {
                    "week": "Week 3",
                    "title": "Check CAC payback",
                    "deliverable": "Payback period measured before raising budgets",
                    "gate": "30 to 60 days; six months or more means financing growth (Leading Social)",
                },
                {
                    "week": "Week 4",
                    "title": "Recover carts and prove capacity",
                    "deliverable": "AI SMS cart recovery plus a separate picker and packer",
                    "gate": "15-30% of carts recovered at 10-15x ROI; two points of verification before surges",
                },
            ],
        },
    ]


VOLUME_021_POSITIONING_ALTERNATIVES: List[Dict[str, Any]] = [
    {
        "title": "The Authorized Dealer",
        "subtitle": "Selling $1,000-plus US brands on Google Shopping without holding stock",
        "audience": "Operators moving from low-ticket dropshipping to branded high-ticket stores",
        "research_basis": (
            "Kenny's store hit about $207,953 in a month on $4,376.72 of ad spend; "
            "Brook Hiddink did about $4.7M in 16 months; Joe Verschoor puts realistic "
            "net at 15-20% of revenue; Ecommerce Paradise reports 30-50% supplier "
            "acceptance on batch applications."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=91zki-xXArY&t=2262s",
            "https://www.youtube.com/watch?v=8V2vAoy6GNA&t=221s",
            "https://www.youtube.com/watch?v=5jY7d_1m1t0&t=373s",
            "https://www.youtube.com/watch?v=hHXf1_WdANY&t=1059s",
        ],
        "validation_status": "Grounded strictly in Vol. 021 YouTube practitioner transcripts.",
    },
    {
        "title": "Margin Before Scale",
        "subtitle": "Contribution margin, landed cost, cash cycle and payback as the scaling gate",
        "audience": "Founders whose revenue grows while cash and profit do not",
        "research_basis": (
            "Eric Andrews holds scaling until contribution margin to CAC exceeds 1; "
            "CandiMentor turns a $10 supplier price into $12 landed; Kurtis Hanni cut a "
            "230-day cycle to 45 days; Leading Social gates spend on 30 to 60 day "
            "payback; Adam Callinan sets breakeven ROAS by budget."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=gG33a-ErNRQ&t=810s",
            "https://www.youtube.com/watch?v=t2H3gJHuw6k&t=536s",
            "https://www.youtube.com/watch?v=CvHvBnjwlJg&t=357s",
            "https://www.youtube.com/watch?v=0WBeNhRVKHY&t=689s",
            "https://www.youtube.com/watch?v=KpmUvCBEKK4&t=108s",
            "https://www.youtube.com/watch?v=VCXWZQgbKXw&t=1539s",
        ],
        "validation_status": "Grounded strictly in Vol. 021 YouTube practitioner transcripts.",
    },
    {
        "title": "The Real Automated Store",
        "subtitle": "Back-office automation that holds up, and the done-for-you schemes that do not",
        "audience": "Store owners weighing 3PLs, tax engines, AI support and automation offers",
        "research_basis": (
            "Smart Capital models about $15.50 self-fulfilled versus about $12 through a "
            "3PL; Cherry Bekaert sets nexus at $100,000 or 200 transactions; Macha prices "
            "Gorgias AI Agent per automated interaction; Dropshipping Deep Dive budgets "
            "around a 19.3% online return rate; NET not GROSS tallies about $77M in "
            "alleged FTC automation-scheme losses."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=8R8um_CLrWI&t=1990s",
            "https://www.youtube.com/watch?v=rUvJ4UwGqiA&t=60s",
            "https://www.youtube.com/watch?v=7Ac3MIM55Yc&t=0s",
            "https://www.youtube.com/watch?v=1L4TNDjsICQ&t=153s",
            "https://www.youtube.com/watch?v=El3a3K2N_sY&t=22s",
        ],
        "validation_status": "Grounded strictly in Vol. 021 YouTube practitioner transcripts.",
    },
]
