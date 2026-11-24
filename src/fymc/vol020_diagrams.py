"""Volume 020 diagrams for Government Contract Brokering."""

from typing import Any, Dict, List

VOLUME_020_SUBTITLE: str = (
    "Three Quotes, a 7-25% Markup, and the 50% Line: Middleman Primes, "
    "DIBBS Parts Brokering, FPDS Price Intelligence, Set-Aside Outreach, "
    "and Funding the 30-Day Payment Gap"
)


def build_volume_020_diagrams_data() -> List[Dict[str, Any]]:
    return [
        {
            "diagram_id": "diag-01-middleman-bid-workflow",
            "chapter_number": 1,
            "title": "The Middleman Bid Workflow",
            "subtitle": "From set-aside filter to priced submission, as Kizzy Parks teaches it",
            "caption": (
                "Kizzy Parks rates a priced VA waste-removal small business set-aside at 50% to 55% "
                "win odds for a couple hours of monthly oversight, worth $500 to $2,000 a month to "
                "the prime. GovClose counters that middlemen write 20 to 50 proposals per win."
            ),
            "assumptions_note": (
                "Attorney Steve places the limitations-on-subcontracting exemption at the $350,000 "
                "simplified acquisition threshold for plain small business set-asides, while Humam "
                "cites roughly $250,000. A 100% pass-through on 8(a), HUBZone or SDVOSB set-asides "
                "crosses the legal line. GovCon TechLab floated $30,000 when an agency paid months late."
            ),
            "note": (
                "Sources - Kizzy Parks (kejmg4Gzuuc, 386MNSeLv9E, 2GThNGqMOJQ, R-2hdJLvKUM), "
                "Dr. Wes Fisher (7NhHddZW0kE), J. White - The Federal Code (LWdgQS6TyHg), "
                "GovCon TechLab (uYFWvLCSDgA), GovCon Empire with Derrick Green 'Theo' (h72zKiJRBe4), "
                "GovClose | DoD Contract Academy (GSss1UvHnQg)."
            ),
            "chart_type": "process_flow",
            "stages": [
                {
                    "step": "01",
                    "label": "Filter Small Business Set-Asides",
                    "value": "Step 1",
                    "detail": (
                        "Filter SAM for small business set-asides and open every attachment, because "
                        "Parks calls it a game of reading. Check whether 52.219-14 is checked on the "
                        "solicitation (Dr. Wes Fisher)."
                    ),
                },
                {
                    "step": "02",
                    "label": "Pull the Prior Contract Amount",
                    "value": "Step 2",
                    "detail": (
                        "Get the prior award from the point of contact, USA Spending or FPDS so a "
                        "$120,000 bid never lands against a $40,000 history (Kizzy Parks)."
                    ),
                },
                {
                    "step": "03",
                    "label": "Collect Three Vendor Quotes",
                    "value": "Step 3",
                    "detail": (
                        "Three price quotes before opening a Word document. Quote big players such as "
                        "WM or Republic, not small rivals who will bid the job themselves (Kizzy Parks). "
                        "Line up a backup sub at the same price (J. White, citing Stephanie)."
                    ),
                },
                {
                    "step": "04",
                    "label": "Lock Pay-After-Paid Terms",
                    "value": "Step 4",
                    "detail": (
                        "Ask the vendor whether paying after you have been paid is okay and write a "
                        "stop-work clause into the service agreement (Kizzy Parks). Prove 60 to 90 days "
                        "of float through a line of credit or cash reserve (GovCon TechLab)."
                    ),
                },
                {
                    "step": "05",
                    "label": "Mark Up and Document Management",
                    "value": "Step 5",
                    "detail": (
                        "Add a 20% to 100% markup (Kizzy Parks), then document oversight with an org "
                        "chart, defined roles and Gantt charts, because if the paperwork is not right, "
                        "it did not happen (Derrick Green 'Theo')."
                    ),
                },
            ],
        },
        {
            "diagram_id": "diag-02-recompete-pricing-funnel",
            "chapter_number": 6,
            "title": "Recompete Pricing Funnel",
            "subtitle": "Sizing the pipeline, then recovering the real incumbent number from FPDS",
            "caption": (
                "Neil McDonnell sizes recompete pipeline at $25-100M of opportunities for every $5M of "
                "revenue targeted. Fox Wade recovered $1,686,566.88 over three years from modification 0 "
                "of a DHS NAICS 541611 incumbent, where the latest action alone showed 348k."
            ),
            "assumptions_note": (
                "Stages 1-3 restate McDonnell's pipeline rule and stages 4-5 restate one Fox Wade "
                "recompete, so the values are not a single continuous conversion path. Kizzy Parks "
                "assumed an Army award was at least $250K and it came in around $35K, so the POC is "
                "asked for incumbent, contract number and value every time."
            ),
            "note": (
                "Sources - Neil McDonnell (17foq325L5w), Fox Wade (Z2ZeI5rayvk), "
                "Kizzy Parks (L0SM3XAM3IE), FedAccess (GrYP5KyxBho)."
            ),
            "chart_type": "funnel",
            "stages": [
                {
                    "label": "Pipeline Ceiling",
                    "value": 100000000,
                    "display": "$100M",
                    "conversion": "Top of the $25-100M band per $5M targeted",
                    "detail": (
                        "McDonnell pulls recompetes from FPDS and saves each search by URL, because "
                        "the query lives in the URL."
                    ),
                },
                {
                    "label": "Pipeline Floor",
                    "value": 25000000,
                    "display": "$25M",
                    "conversion": "Bottom of the band per $5M targeted",
                    "detail": "McDonnell's floor, with 2027 revenue to be won in 2026.",
                },
                {
                    "label": "Revenue Target",
                    "value": 5000000,
                    "display": "$5M",
                    "conversion": "Revenue the pipeline must convert into",
                    "detail": "The revenue unit McDonnell's pipeline multiple is anchored to.",
                },
                {
                    "label": "Incumbent Base Award Recovered",
                    "value": 1686566.88,
                    "display": "$1,686,566.88",
                    "conversion": "Modification 0 over three years",
                    "detail": (
                        "Fox Wade sorted FPDS by date signed and pulled modification 0 of the DHS "
                        "incumbent, then pulled the old solicitation because scope can grow from "
                        "2 people to 10 (FedAccess)."
                    ),
                },
                {
                    "label": "Latest-Action Trap",
                    "value": 348000,
                    "display": "$348K",
                    "conversion": "Latest action alone",
                    "detail": (
                        "The number a pricer sees by skipping modification 0, which Fox Wade warns "
                        "distorts the recompete price."
                    ),
                },
            ],
        },
        {
            "diagram_id": "diag-03-fpds-simplified-award-filter",
            "chapter_number": 3,
            "title": "FPDS Simplified-Award Filter",
            "subtitle": "Humam's filter chain from 86 million records to 535 pricing comparables",
            "caption": (
                "SamSearch reports 65% of simplified acquisition contracts went to small businesses "
                "versus 26% of traditional contract spending. Humam uses the FPDS action obligation on "
                "comparable simplified awards as the pricing benchmark before quoting."
            ),
            "assumptions_note": (
                "Deduction bars are the arithmetic gaps between Humam's three reported counts. The year "
                "of the March 1 date-signed filter was not stated. Kizzy Parks' Coast Guard award shows "
                "the payoff scale, $1,300 a month profit on $14,000 a month split across 10 vendors."
            ),
            "note": (
                "Sources - GovCon with Humam (IEV3HAgB8jA), SamSearch - AI for Government Contracting "
                "(e7wypJIJZpw), Kizzy Parks (Ac9lYLwR6QQ)."
            ),
            "chart_type": "waterfall",
            "bars": [
                {
                    "label": "FPDS Records at $20K Obligation",
                    "value": 86000000,
                    "display": "86 million",
                    "kind": "total",
                },
                {
                    "label": "Simplified Procedures + Date Signed",
                    "value": -85970000,
                    "display": "Cut to 30,000",
                    "kind": "deduction",
                },
                {
                    "label": "Simplified Award Pool",
                    "value": 30000,
                    "display": "30,000",
                    "kind": "total",
                },
                {
                    "label": "Keyword 'cleaning'",
                    "value": -29465,
                    "display": "Cut to 535",
                    "kind": "deduction",
                },
                {
                    "label": "Cleaning Comparables",
                    "value": 535,
                    "display": "535",
                    "kind": "total",
                },
                {
                    "label": "Pricing Benchmark Set",
                    "value": 535,
                    "display": "535 awards to price against",
                    "kind": "result",
                },
            ],
        },
        {
            "diagram_id": "diag-04-registration-clock",
            "chapter_number": 2,
            "title": "The Registration Clock",
            "subtitle": "How long each step of the SAM and CAGE stack takes, per practitioners",
            "caption": (
                "Kizzy Parks pulled a UEI roughly 3 minutes into the entity validation flow. The CAGE "
                "code is assigned by DLA at no charge after submission and is never bought "
                "(FedOpp, Eric Coffie)."
            ),
            "assumptions_note": (
                "Where a speaker gave only a range, the typical value marks the earliest point given, "
                "since no midpoint was testified. Three weeks is shown as 21 days. HUBZone requires the "
                "office and 35% of employee home addresses inside a zone (Nick Waters GovCon), against "
                "government-wide HUBZone spend of 0.44% (Squared Compass)."
            ),
            "note": (
                "Sources - Neil McDonnell (QIEmDXcWhSE), SEMSCIO (rRWCLLWqrV0), Kizzy Parks "
                "(FWfV2m3K4jY, eIFlVzfusWo), FedOpp (2Bp78kNCVGI)."
            ),
            "chart_type": "horizontal_bars",
            "unit": "days",
            "bars": [
                {
                    "label": "CAGE Assignment by DLA",
                    "min": 3,
                    "max": 21,
                    "typical": 3,
                    "display": "3 days to 3 weeks (Neil McDonnell)",
                },
                {
                    "label": "CAGE After IRS Verification",
                    "min": 7,
                    "max": 14,
                    "typical": 7,
                    "display": "About a week or two (SEMSCIO)",
                },
                {
                    "label": "DLA Follow-Up Response Window",
                    "min": 3,
                    "max": 3,
                    "typical": 3,
                    "display": "3 business days (Kizzy Parks)",
                },
                {
                    "label": "Registration Login Cadence",
                    "min": 7,
                    "max": 7,
                    "typical": 7,
                    "display": "At least weekly, since zero reminder emails arrive (Kizzy Parks)",
                },
                {
                    "label": "SAM Renewal Cycle",
                    "min": 365,
                    "max": 365,
                    "typical": 365,
                    "display": "Every 365 days (FedOpp)",
                },
            ],
        },
        {
            "diagram_id": "diag-05-set-aside-sled-bid-gates",
            "chapter_number": 5,
            "title": "Set-Aside and SLED Bid Gates",
            "subtitle": "Four checks before spending time on a certification or a bid",
            "caption": (
                "Neil McDonnell counts 11,152 FY2023 SDVOSB set-aside awards against 5,413,622 total new "
                "contract actions (WOSB 2,845, HUBZone 1,534, 8(a) 872), and reports that 20-30 "
                "sources-sought responses yield 5-10 RFP responses."
            ),
            "assumptions_note": (
                "SLED figures come from separate speakers. Texas SmartBuy drops from 20,000 pages to 27 "
                "with status set to posted (SamSearch), and Foley Equipment estimates cooperative "
                "purchasing at about 20-30% of US purchases."
            ),
            "note": (
                "Sources - GovKidMethod (nRXCetmIWUs, xXM1cyLQ_jY), D'S Construction (yxjYYFbCa5E), "
                "Government Contracting Strategist & Host (iTD46ZpHbdI), GovClose | DoD Contract Academy "
                "(Qij-5QQmwc8), Neil McDonnell (4poj2n7iLrs)."
            ),
            "chart_type": "decision_tree",
            "nodes": [
                {
                    "gate": "G1",
                    "question": (
                        "Does the SAM set-aside filter on your NAICS code show enough set-aside "
                        "volume to justify a certification?"
                    ),
                    "pass_next": "G2",
                    "fail_action": (
                        "Hold off on the certification, because the SBA is not going to be bringing "
                        "you contracts (GovKidMethod)."
                    ),
                },
                {
                    "gate": "G2",
                    "question": "Is there a mandatory pre-bid meeting, and can you attend it?",
                    "pass_next": "G3",
                    "fail_action": "Skip the bid, because missing it means you cannot submit (D'S Construction).",
                },
                {
                    "gate": "G3",
                    "question": "Have you pulled the bid tabs and the last award letter?",
                    "pass_next": "G4",
                    "fail_action": (
                        "Pull them and price against history instead of guessing "
                        "(Government Contracting Strategist & Host)."
                    ),
                },
                {
                    "gate": "G4",
                    "question": "Did your questions go in at the sources-sought or RFI stage?",
                    "pass_next": "Bid, and keep flooding sources sought with a 10-20 firm team (Neil McDonnell)",
                    "fail_action": (
                        "Target the next sources-sought notice, since contracting officers avoid "
                        "one-on-one questions once a solicitation drops (GovClose)."
                    ),
                },
            ],
        },
        {
            "diagram_id": "diag-06-dibbs-broker-architecture",
            "chapter_number": 11,
            "title": "DIBBS Parts Broker Architecture",
            "subtitle": "One narrow FSC lane, quoted every day",
            "caption": (
                "DVN reports DLA posts 2,000 to 3,000 solicitations a day, and the active DIBBS vendor "
                "pool shrank to about 8,500 from roughly 15,000 before the pandemic. Roughly 99% of "
                "awards go to the cheapest bid."
            ),
            "assumptions_note": (
                "Spokes are functions, not hires, and may all sit with one owner-operator. No headcount "
                "was testified. Tooling ranges from FedOpp browser-built batch files to DVN's DLA BUS "
                "catalog uploads and Gov Scraper at $100 a month."
            ),
            "note": (
                "Sources - Tris10 @ MeND (v4ulUMKE5xA, JE_OOJ3NAVk), Secureframe with Tristan Thomas "
                "(v7nJCLRc0uo), The DLA Vendor Network (DVN) with Ki Hendris (jjX9klCZFKI, MyfmHjDF9HI), "
                "Loocey DLA & GovCon (LzmJyrGyMBw), FedOpp (bTs2wy13K1c)."
            ),
            "chart_type": "org_architecture",
            "center": {
                "role": "DIBBS Broker",
                "headcount": "Owner-operator in a 3 to 5 FSC lane",
                "focus": "Quote every day, because bid count tracks award count (Tris10 @ MeND)",
            },
            "spokes": [
                {
                    "role": "RFQ Screener",
                    "type": "Solicitation intake",
                    "kpi": (
                        "Read the full solicitation, filter Approved Sources is null, and reject "
                        "parts from non-qualifying countries such as China or Afghanistan"
                    ),
                },
                {
                    "role": "Supplier Sourcer",
                    "type": "Supply side",
                    "kpi": (
                        "Map every NSN to the manufacturer part number with nsn-now, then call "
                        "instead of email"
                    ),
                },
                {
                    "role": "Pricer",
                    "type": "Margin control",
                    "kpi": (
                        "10-15% margin anchored to procurement history, since asking 20-30% gets "
                        "underbid (Tristan Thomas)"
                    ),
                },
                {
                    "role": "Invoicing and Cash",
                    "type": "Collections",
                    "kpi": (
                        "Net 30 terms with the government paying in 23 to 25 days on average, "
                        "and My Invoice checked every Friday"
                    ),
                },
            ],
        },
        {
            "diagram_id": "diag-07-winning-markup-bands",
            "chapter_number": 4,
            "title": "Winning Markup Bands",
            "subtitle": "Where first wins and nine-figure bids were actually priced",
            "caption": (
                "Dr. Wes Fisher compresses execution into five days, listing 15-20 opportunities and "
                "getting a quote within 48 hours. Derek James says bids 10-20 are in the money."
            ),
            "assumptions_note": (
                "Each bucket is one practitioner's reported band, not a market survey. Kizzy Parks warns "
                "the hard part is funding, as with a $155,000 outlay for $10,000 in profit, and that "
                "upfront-cash, weird or overseas bids can sit outside the 7-25% band."
            ),
            "note": (
                "Sources - Kizzy Parks (etvo2gL7_Cs, AHQVro9N9HM, RrDUfb8vNms, WR8VA1o3VMU), "
                "with David Packouz and James Walk as reported by Parks."
            ),
            "chart_type": "stacked_comparison",
            "total_range": "7% to 25% markup, the contracting officer's middle band",
            "buckets": [
                {
                    "label": "Contracting Officer Middle Band",
                    "low": 7,
                    "high": 25,
                    "notes": "A contracting officer told Kizzy Parks newcomers bid either too low or too high.",
                },
                {
                    "label": "Gravel Sweet Spot",
                    "low": 10,
                    "high": 13,
                    "notes": "The same contracting officer's band for gravel bids.",
                },
                {
                    "label": "Packouz Munitions Margin",
                    "low": 10,
                    "high": 20,
                    "notes": "Bid just under $300M and came in $52M under the next bidder, while majors bid around $500M.",
                },
                {
                    "label": "James Walk VA Parts",
                    "low": 15,
                    "high": 15,
                    "notes": "About $42K of VA Dallas cooling-tower parts, won under LPTA without being the lowest bidder.",
                },
            ],
        },
        {
            "diagram_id": "diag-08-funding-and-payment-roadmap",
            "chapter_number": 12,
            "title": "Funding the Gap and Getting Paid",
            "subtitle": "From financing choice to a proper invoice that starts the payment clock",
            "caption": (
                "A contractor typically works about 30 days, invoices, then waits roughly another 30. "
                "Debra Smith calls 3% to 5% a fair factoring fee, flags anything over 5%, and cites "
                "RTS Financial at 2.5%."
            ),
            "assumptions_note": (
                "The four-week sequencing is an organizing frame and no practitioner testified to a "
                "weekly schedule. Progress payments run 80% for large and 95% for small businesses, "
                "and performance-based payments reach up to 90% of contract value (Acquisition Pro Tips)."
            ),
            "note": (
                "Sources - Debra Smith (NusotbSsCa4), Business Cash Now with Chris Curtin (4V1zq5q3VuQ), "
                "Mobilization Capital (oOQSsJO94kM), Acquisition Pro Tips (WXCymE9NjBg, cdachjXPX3k), "
                "Tris10 @ MeND (weLOISkZc5k, yXqp5I7wQK0)."
            ),
            "chart_type": "timeline_roadmap",
            "weeks": [
                {
                    "week": "Week 1",
                    "title": "Pick the Funding Tool",
                    "deliverable": (
                        "Factoring for services and credit cards for products (Debra Smith), or a "
                        "mobilization lender against a signed contract or Notice to Proceed"
                    ),
                    "gate": (
                        "Margin covers the fee, since 5% to 7% low-bid margins leave nothing for "
                        "financing (Business Cash Now)"
                    ),
                },
                {
                    "week": "Week 2",
                    "title": "Lock the Supplier",
                    "deliverable": "Supplier terms in hand with agency name and POC kept confidential",
                    "gate": "A sub demanding the agency name and POC before the PO is a signal to walk (Debra Smith)",
                },
                {
                    "week": "Week 3",
                    "title": "Ship and Invoice in WAWF",
                    "deliverable": (
                        "Combo for supplies or Invoice 2-in-1 for services, a Z on the final shipment, "
                        "and photos plus carrier proof of delivery"
                    ),
                    "gate": "Ship-to DoDAAC is not the admin DoDAAC (Acquisition Pro Tips)",
                },
                {
                    "week": "Week 4",
                    "title": "Chase the Payment",
                    "deliverable": (
                        "My Invoice opened every Friday, and rejected invoices copied with only the "
                        "failed field fixed"
                    ),
                    "gate": (
                        "A proper invoice starts the 30-day prompt payment clock, with late interest "
                        "quoted at 4.6%"
                    ),
                },
            ],
        },
    ]


VOLUME_020_POSITIONING_ALTERNATIVES: List[Dict[str, Any]] = [
    {
        "title": "The Middleman Prime",
        "subtitle": "Three Quotes, a Real Markup, and the Line Between Brokering and Fraud",
        "audience": "New small business owners who want to prime set-asides by managing qualified subs",
        "research_basis": (
            "Kizzy Parks' three-quote workflow and 50% to 55% win-odds estimate, attorney Steve's "
            "$350,000 limitations-on-subcontracting exemption, GovCon TechLab's $30,000 float, and "
            "PilieroMazza's 50% services cap with a 47-49% buffer."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=kejmg4Gzuuc&t=601s",
            "https://www.youtube.com/watch?v=R-2hdJLvKUM&t=1250s",
            "https://www.youtube.com/watch?v=uYFWvLCSDgA&t=447s",
            "https://www.youtube.com/watch?v=i9prjadeAyM&t=757s",
        ],
        "validation_status": "Grounded strictly in Vol. 020 YouTube practitioner transcripts.",
    },
    {
        "title": "The DIBBS Parts Broker",
        "subtitle": "Quote Every Day in a Narrow FSC Lane at 10-15% Margin",
        "audience": "Operators who want high-volume DLA parts brokering without a factory",
        "research_basis": (
            "DVN's 2,000-3,000 daily solicitations and shrinking vendor pool, Tristan Thomas' 10-15% "
            "margin sweet spot, Tris10's bid-count-to-award correlation, and WAWF payment mechanics "
            "from Acquisition Pro Tips."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=jjX9klCZFKI&t=1213s",
            "https://www.youtube.com/watch?v=v7nJCLRc0uo&t=2283s",
            "https://www.youtube.com/watch?v=v4ulUMKE5xA&t=955s",
            "https://www.youtube.com/watch?v=WXCymE9NjBg&t=437s",
        ],
        "validation_status": "Grounded strictly in Vol. 020 YouTube practitioner transcripts.",
    },
    {
        "title": "Price to Win, Fund to Deliver",
        "subtitle": "FPDS History, the 7-25% Band, and Cash That Survives the Payment Gap",
        "audience": "Bidders losing on price or winning awards they cannot afford to perform",
        "research_basis": (
            "The contracting officer's 7-25% middle band reported by Kizzy Parks, Solvability's 1.5 "
            "wrap rate and 8-15% G&A norm, Fox Wade's modification 0 recovery, and Debra Smith's 3% "
            "to 5% factoring rule."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=etvo2gL7_Cs&t=143s",
            "https://www.youtube.com/watch?v=lOumu-Dk0Jw&t=2451s",
            "https://www.youtube.com/watch?v=Z2ZeI5rayvk&t=170s",
            "https://www.youtube.com/watch?v=NusotbSsCa4&t=176s",
        ],
        "validation_status": "Grounded strictly in Vol. 020 YouTube practitioner transcripts.",
    },
]
