"""Volume 043 diagrams: Live-Event, Super Bowl & VIP Ticket Brokering."""

from typing import Any, Dict, List

VOLUME_043_SUBTITLE: str = (
    "Allotment Sourcing, 48-to-72-Hour Resale Timing, PSL Fee Math, Paddock Club "
    "and Suite Hospitality, Ticketmaster and AXS Transfer Custody, BOTS Act Limits "
    "and the 25% Margin Flipping Playbook"
)


def build_volume_043_diagrams_data() -> List[Dict[str, Any]]:
    """Return the 8 structured diagram dicts for Volume 043."""
    return [
        {
            "diagram_id": "diag-01-super-bowl-resale-timing-flow",
            "chapter_number": 1,
            "chart_type": "process_flow",
            "title": "Reading the Super Bowl Resale Curve",
            "subtitle": "From the conference-championship spike to a game-day exit plan",
            "caption": (
                "Five-step buying and exit sequence assembled from street brokers, "
                "StubHub commentary and resale-timing segments."
            ),
            "assumptions_note": (
                "All figures are attributed practitioner claims for specific Super Bowl "
                "years; matchup, fan travel and leftover supply move the curve each season."
            ),
            "note": (
                "Sources: N.F.L Podcast (Aj09Nv4kg04 @ 00:03:31), AP Archive "
                "(NwYrOSq9-5Q @ 00:00:15; NxbqrXeuWTI @ 00:00:38), NBC10 Boston "
                "(-GwKaOFdk_M @ 00:01:24), CBS Boston (hhJFZEqMUpQ @ 00:01:02 and 00:01:16)."
            ),
            "stages": [
                {
                    "step": "01",
                    "label": "Let the conference-championship spike burn off",
                    "value": "Step 1",
                    "detail": (
                        "Watch prices early, wait a few days to a week for the dip, and stay "
                        "out of the final rush when desperation pushes prices back up "
                        "(N.F.L Podcast)."
                    ),
                },
                {
                    "step": "02",
                    "label": "Read the buyer-geography split",
                    "value": "Step 2",
                    "detail": (
                        "A single traveling fan base, like the Philadelphia market, kept "
                        "StubHub sales 30 to 40% ahead of the prior year (AP Archive)."
                    ),
                },
                {
                    "step": "03",
                    "label": "Gauge leftover game-day supply",
                    "value": "Step 3",
                    "detail": (
                        "StubHub said downward movement depends on how much inventory is "
                        "left on game day (AP Archive)."
                    ),
                },
                {
                    "step": "04",
                    "label": "Target the 48 to 72 hour buying window",
                    "value": "Step 4",
                    "detail": (
                        "Prices dip leading up to the game, then pop on game day as "
                        "last-minute purchases hit the market (NBC10 Boston)."
                    ),
                },
                {
                    "step": "05",
                    "label": "Carry an exit plan or bundle a perk",
                    "value": "Step 5",
                    "detail": (
                        "One broker ran a pop-up near NRG Stadium with a tailgate bash for "
                        "buyers; another sat on a backpack of tickets as the average slid "
                        "to just over $4,400 and the low hit $1,900 (CBS Boston)."
                    ),
                },
            ],
        },
        {
            "diagram_id": "diag-02-psl-resale-fee-funnel",
            "chapter_number": 6,
            "chart_type": "funnel",
            "title": "Raiders PSL Resale Fee Funnel",
            "subtitle": "How a $10,000 seat-license sale splits between buyer, seller and marketplace",
            "caption": (
                "A single $10,000 Raiders PSL transaction on the official marketplace, "
                "from buyer all-in cost down to the per-side fee floor."
            ),
            "assumptions_note": (
                "Fee structure is the Raiders' official marketplace FAQ as read by THE "
                "MARKUP FILES; any outstanding PSL loan payoff comes out on top of the "
                "seller net shown."
            ),
            "note": (
                "Source: THE MARKUP FILES (rT4gQkoEVDI @ 00:12:53 and 00:13:14). Offer-route "
                "context: TicketWire (M80btlo7xJc @ 00:01:48) reports $3,000 to $4,000 saved "
                "by making a lowball offer instead of paying asking."
            ),
            "stages": [
                {
                    "label": "Buyer all-in cost",
                    "value": 11200,
                    "display": "$11,200",
                    "conversion": "Starting point",
                    "detail": "Negotiated price plus the 12% buyer fee.",
                },
                {
                    "label": "Negotiated PSL price",
                    "value": 10000,
                    "display": "$10,000",
                    "conversion": "12% buyer fee removed",
                    "detail": "The headline sale price both sides agree on.",
                },
                {
                    "label": "Seller net proceeds",
                    "value": 8800,
                    "display": "$8,800",
                    "conversion": "12% seller fee removed",
                    "detail": "Net before any outstanding loan payoff.",
                },
                {
                    "label": "Combined marketplace fee take",
                    "value": 2400,
                    "display": "Almost $2,400",
                    "conversion": "Both sides combined",
                    "detail": "Total fees on a single $10,000 transaction.",
                },
                {
                    "label": "Per-side fee floor",
                    "value": 250,
                    "display": "$250 minimum",
                    "conversion": "Applies to small sales",
                    "detail": "Minimum fee charged on each side of the trade.",
                },
            ],
        },
        {
            "diagram_id": "diag-03-super-bowl-58-price-ladder-waterfall",
            "chapter_number": 3,
            "chart_type": "waterfall",
            "title": "Super Bowl 58 Price Ladder",
            "subtitle": "From a $12,000 secondary listing down to the recent-years minimum",
            "caption": (
                "Price steps at the record-priced Las Vegas Super Bowl, set against the "
                "roughly $3,000 minimum of recent years that the game tripled."
            ),
            "assumptions_note": (
                "Step sizes are the gaps between the price levels Rhonda Williams cited; "
                "the cheapest band was quoted as a $5,000 to $7,000 range."
            ),
            "note": (
                "Source: Rhonda Williams, Bloomberg Television (zXgujuB9yXw @ 00:01:31). "
                "Suite context: GQ host Clay Skipper quoted $300,000 to $2.5 million "
                "Super Bowl suites at Allegiant Stadium (nT-DpxVmqC0 @ 00:07:04)."
            ),
            "bars": [
                {
                    "label": "Top secondary listing",
                    "value": 12000,
                    "display": "$12,000",
                    "kind": "total",
                },
                {
                    "label": "Step down to game average",
                    "value": 3000,
                    "display": "Over $9,000 average",
                    "kind": "deduction",
                },
                {
                    "label": "Step down to cheapest band top",
                    "value": 2000,
                    "display": "$7,000 cheapest (upper)",
                    "kind": "deduction",
                },
                {
                    "label": "Step down to cheapest band floor",
                    "value": 2000,
                    "display": "$5,000 cheapest (lower)",
                    "kind": "deduction",
                },
                {
                    "label": "Step down to recent-years minimum",
                    "value": 2000,
                    "display": "Roughly $3,000",
                    "kind": "deduction",
                },
                {
                    "label": "Recent-years minimum",
                    "value": 3000,
                    "display": "Roughly $3,000",
                    "kind": "result",
                },
            ],
        },
        {
            "diagram_id": "diag-04-super-bowl-sourcing-price-bands",
            "chapter_number": 2,
            "chart_type": "horizontal_bars",
            "title": "Super Bowl Seat Price Bands by Sourcing Path",
            "subtitle": "Face value, broker cash offers, resale floors and listing ceilings",
            "unit": "USD per ticket",
            "caption": (
                "Reported price bands from face value through the highest listings, "
                "as described by brokers, TickPick coverage and allocation walkthroughs."
            ),
            "assumptions_note": (
                "Face value is reachable only through season-holder raffles, roster "
                "allotments, sponsors or contests; listing ceilings are asks, not completed sales."
            ),
            "note": (
                "Sources: 24H SPORT (pAU7eEVgp1A @ 00:00:40, 00:01:17, 00:03:42), "
                "thumbsuprun (O-Sq4DDGKAY @ 00:04:02 and 00:06:24)."
            ),
            "bars": [
                {
                    "label": "Face value seats",
                    "min": 950,
                    "max": 1250,
                    "typical": 950,
                    "display": "$950 face; players often hold $1,250 seats",
                },
                {
                    "label": "Pre-game party cash offer",
                    "min": 2500,
                    "max": 2500,
                    "typical": 2500,
                    "display": "$2,500 cash from brokers",
                },
                {
                    "label": "Buyer floor near game day",
                    "min": 3200,
                    "max": 3200,
                    "typical": 3200,
                    "display": "Buyers grab seats around $3,200",
                },
                {
                    "label": "Reported resale floors",
                    "min": 3500,
                    "max": 4500,
                    "typical": 4000,
                    "display": "$3,500 to $4,500; about $4,000 on StubHub and TickPick",
                },
                {
                    "label": "Listing ceilings",
                    "min": 16000,
                    "max": 30000,
                    "typical": 16000,
                    "display": "Up to $16,000 on Ticketmaster; up to $30,000 elsewhere",
                },
            ],
        },
        {
            "diagram_id": "diag-05-marquee-event-buy-gates",
            "chapter_number": 5,
            "chart_type": "decision_tree",
            "title": "Marquee Event Buy Gates",
            "subtitle": "Masters, UFC, CFP and tennis purchase checks",
            "caption": (
                "Four gates separating Augusta's official-channel lockbox from the "
                "resale and premium hospitality market around other marquee events."
            ),
            "assumptions_note": (
                "Gate thresholds follow practitioner testimony; stated Masters ballot odds "
                "range from under 1% to 3-5% depending on the source."
            ),
            "note": (
                "Sources: Gameday Guides (LtTBm2wHjoE @ 00:01:03 and 00:01:59), WTHR "
                "(OSa-CK_qebs @ 00:01:13 and 00:02:30), MMALeaked (2vauuB_YXFc @ 00:04:26), "
                "Sports Travel Tom (iKAz6YJRTXI @ 00:01:43)."
            ),
            "nodes": [
                {
                    "gate": "G1",
                    "question": (
                        "If the event is the Masters, is the badge coming through the "
                        "ballot with exactly one application per household?"
                    ),
                    "pass_next": "G2",
                    "fail_action": (
                        "Stop: Augusta voids tickets at the gate with RFID tracking and "
                        "permanently revokes lifetime badges; duplicate household entries "
                        "get both disqualified."
                    ),
                },
                {
                    "gate": "G2",
                    "question": "Is the seller on a verified site, with proof of purchase kept?",
                    "pass_next": "G3",
                    "fail_action": "Refuse the deal and walk away from any seller who rushes you.",
                },
                {
                    "gate": "G3",
                    "question": "Is the price backed by completed sales rather than listed asks?",
                    "pass_next": "G4",
                    "fail_action": (
                        "Wait: 9 times out of 10 prices come down closer to the event, and "
                        "most high asks never sell."
                    ),
                },
                {
                    "gate": "G4",
                    "question": "Has the sightline been checked before paying a premium?",
                    "pass_next": "Buy",
                    "fail_action": (
                        "Skip the seat: a $470 last-section UFC ticket put a metal pillar "
                        "between the buyer and the cage."
                    ),
                },
            ],
        },
        {
            "diagram_id": "diag-06-concert-pricing-desk-architecture",
            "chapter_number": 11,
            "chart_type": "org_architecture",
            "title": "Concert Pricing Desk Architecture",
            "subtitle": "Four controls around the gap between face value and market price",
            "caption": (
                "How a concert buying operation organizes around presale timing, "
                "checkout verification, fee drag and face-value caps."
            ),
            "assumptions_note": (
                "Headcount was not stated by any practitioner; the structure maps to "
                "operator gates, not a staffing plan."
            ),
            "note": (
                "Sources: thumbsuprun (TpXJCfuFf4o @ 00:06:35), Scott Cramer "
                "(kFsH01UthzA @ 00:11:23 and 00:23:58), Why It Costs (tH7bLaJI6ZE @ 00:08:16), "
                "Business Made Simple (VBp4zpS7F3o @ 00:09:17)."
            ),
            "center": {
                "role": "Concert Pricing Desk",
                "headcount": "Not stated by practitioners",
                "focus": (
                    "Run every deal on the all-in number: add every line, divide by face "
                    "value, and compare totals across sites."
                ),
            },
            "spokes": [
                {
                    "role": "Presale Entry",
                    "type": "Access",
                    "kpi": (
                        "First presale wave entered before Official Platinum conversion "
                        "or face-value increases."
                    ),
                },
                {
                    "role": "Checkout Price Verification",
                    "type": "Control",
                    "kpi": (
                        "Final payment screen re-checked; a Shania Twain order at $227 each "
                        "became $291 apiece, a 30% bump."
                    ),
                },
                {
                    "role": "Fee-Drag Underwriting",
                    "type": "Risk",
                    "kpi": (
                        "Secondary fees averaged 31% of listed price in the GAO sample; "
                        "weak demand can leave resale losses."
                    ),
                },
                {
                    "role": "Face-Value Cap Screening",
                    "type": "Compliance",
                    "kpi": (
                        "Tours like Noah Kahan's allow resale only on Ticketmaster at base "
                        "price, so the markup disappears."
                    ),
                },
            ],
        },
        {
            "diagram_id": "diag-07-f1-hospitality-tier-comparison",
            "chapter_number": 4,
            "chart_type": "stacked_comparison",
            "title": "F1 Hospitality Tier Comparison",
            "subtitle": "From a Melbourne Champions Club pass to drive-in Paddock tiers",
            "total_range": "$600 Champions Club to EUR 25,000 drive-in tiers",
            "caption": (
                "Reported price points across F1 premium access, with the Paddock Club "
                "sold as a sponsor-funded corporate room first and retail ticket second."
            ),
            "assumptions_note": (
                "Currencies are mixed as reported (USD and EUR); Pit Stop Lab puts a "
                "Paddock Club seat at up to $15,000 per race weekend."
            ),
            "note": (
                "Sources: Pit Stop Lab (qjr3BHunOxo @ 00:00:00), Kayvan Goes "
                "(2UDtC8EP8GA @ 00:21:38, 00:24:42, 00:30:21), Global Nomads "
                "(ePgxCdmE8o8 @ 00:31:34), Live The Dash (emvC24ZLBWo @ 00:12:30)."
            ),
            "buckets": [
                {
                    "label": "Melbourne Champions Club",
                    "low": 600,
                    "high": 600,
                    "notes": "Entry-level Melbourne hospitality at $600.",
                },
                {
                    "label": "Melbourne Red Bull Pit Lane",
                    "low": 6000,
                    "high": 6000,
                    "notes": "About $6,000 per person bought a run at roughly 40 available seats.",
                },
                {
                    "label": "Paddock Club ticket",
                    "low": 10000,
                    "high": 20000,
                    "notes": (
                        "EUR 10,000 to EUR 20,000; about 30% of guests do not pay, and "
                        "networking scored 1 out of 10 when unassisted."
                    ),
                },
                {
                    "label": "Drive-in tier",
                    "low": 25000,
                    "high": 25000,
                    "notes": (
                        "EUR 25,000 tier; Kayvan Goes said he would not pay EUR 15,000 and "
                        "would pay EUR 200 at most."
                    ),
                },
            ],
        },
        {
            "diagram_id": "diag-08-reseller-four-week-roadmap",
            "chapter_number": 12,
            "chart_type": "timeline_roadmap",
            "title": "Reseller Sourcing and Flipping Roadmap",
            "subtitle": "Event selection, presale stacking, cart checks and sell-through tracking",
            "caption": (
                "A four-week ramp built on the flipper rule of buying where demand "
                "outruns seats, screened against a 25% margin benchmark."
            ),
            "assumptions_note": (
                "Every purchasing account must map to a real, provable person; methods "
                "that beat a seller's purchase limit fall under the BOTS Act at over "
                "$53,000 per violation (Hustle Audit, NOBp14Qcy_8 @ 00:06:47)."
            ),
            "note": (
                "Sources: Ticket Flipping (JwHo6if-9Wo @ 00:09:05; hw92haJDs9Y @ 00:11:21; "
                "NGFBVOXqxpA @ 00:04:09), Emmanuel Ak (RsyNgibgVJY @ 00:24:33; "
                "ETQnblEeP94 @ 00:32:36), 850 Club Credit (p8CMjg4a_CI @ 00:04:17), "
                "The Credit Nerd (JS9sO0Fx9A0 @ 00:02:23)."
            ),
            "weeks": [
                {
                    "week": "Week 1",
                    "title": "Select events where demand outruns seats",
                    "deliverable": (
                        "Shortlist of small-venue, weekend and hometown shows screened with "
                        "Spotify listeners and live inventory counts."
                    ),
                    "gate": "Each event clears a 25% per-ticket margin benchmark.",
                },
                {
                    "week": "Week 2",
                    "title": "Stack every presale",
                    "deliverable": (
                        "Amex, Citi Entertainment and Mastercard presale access mapped; one "
                        "Amex presale turned $150 floor seats into about $390 resales."
                    ),
                    "gate": "Every presale available for the event has been checked.",
                },
                {
                    "week": "Week 3",
                    "title": "Run the cart check",
                    "deliverable": (
                        "StubHub compared while seats sit in the cart; Rush seats at about "
                        "$300 listed near $570."
                    ),
                    "gate": "Resale spread confirmed before payment.",
                },
                {
                    "week": "Week 4",
                    "title": "Track sell-through and stay liquid",
                    "deliverable": (
                        "Remaining tickets divided by capacity daily, watching for held "
                        "inventory that pushes a 500 count back to 700."
                    ),
                    "gate": (
                        "Real daily downtrend, time to receive, list, sell and transfer, "
                        "and no money tied up in dead stock."
                    ),
                },
            ],
        },
    ]


VOLUME_043_POSITIONING_ALTERNATIVES: List[Dict[str, Any]] = [
    {
        "title": "The Super Bowl Resale Desk",
        "subtitle": (
            "Allocation math, face value versus resale, and the 48-to-72-hour buying window"
        ),
        "audience": "Ticket brokers and high-intent fans buying or selling Super Bowl seats",
        "research_basis": (
            "StubHub's average 25% commission, the $950 face value versus $4,950 cheapest "
            "resale gap, the 48 to 72 hour sweet spot, the 58% one-week collapse and the "
            "17.5 percent per-team allocation."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=RGn3Hcnvklg&t=146s",
            "https://www.youtube.com/watch?v=C_QtPWHCo_U&t=118s",
            "https://www.youtube.com/watch?v=-GwKaOFdk_M&t=84s",
            "https://www.youtube.com/watch?v=jQCA_9sgdpM&t=52s",
            "https://www.youtube.com/watch?v=O-Sq4DDGKAY&t=27s",
        ],
        "validation_status": "Grounded strictly in Vol. 043 YouTube practitioner transcripts.",
    },
    {
        "title": "Premium Access Economics",
        "subtitle": "Suites, Paddock Club rooms and seat licenses priced on fees and exits",
        "audience": "Corporate hospitality buyers, PSL holders and premium-seat resellers",
        "research_basis": (
            "$300,000 to $2.5 million Super Bowl suites, the 10% Allegiant PSL transaction "
            "fee, Bills PSL gross proceeds of about $262 million, Paddock Club seats up to "
            "$15,000 and a networking score of 1 out of 10."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=nT-DpxVmqC0&t=424s",
            "https://www.youtube.com/watch?v=o_WpoJl9phM&t=259s",
            "https://www.youtube.com/watch?v=rT4gQkoEVDI&t=100s",
            "https://www.youtube.com/watch?v=qjr3BHunOxo&t=0s",
            "https://www.youtube.com/watch?v=2UDtC8EP8GA&t=1482s",
        ],
        "validation_status": "Grounded strictly in Vol. 043 YouTube practitioner transcripts.",
    },
    {
        "title": "Compliance-First Ticket Flipping",
        "subtitle": "Margin screens, cart checks and transfer custody inside the BOTS Act line",
        "audience": "Independent resellers scaling from side income to a full broker operation",
        "research_basis": (
            "The 25% margin benchmark, the $300 cart versus $570 StubHub spread, Ticketmaster "
            "transfer gating, and BOTS Act penalties above $53,000 per violation with the "
            "show-me-the-human discovery test."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=NOBp14Qcy_8&t=407s",
            "https://www.youtube.com/watch?v=BOIfCHick7o&t=145s",
            "https://www.youtube.com/watch?v=JwHo6if-9Wo&t=545s",
            "https://www.youtube.com/watch?v=RsyNgibgVJY&t=1473s",
            "https://www.youtube.com/watch?v=MP1aH4hgG70&t=95s",
        ],
        "validation_status": "Grounded strictly in Vol. 043 YouTube practitioner transcripts.",
    },
]
