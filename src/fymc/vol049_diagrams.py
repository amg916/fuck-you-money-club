"""Volume 049 diagram data: Regulated Prediction-Market Terminals & Licensed iGaming Affiliates."""

from typing import Dict, List

VOLUME_049_SUBTITLE: str = (
    "Cache the catalog, normalize Kalshi and Polymarket, gate every cross-venue pair on "
    "equivalence and book depth, make markets where retail buys longshots, read the rules "
    "before the first order, and run every affiliate deal through NGR math, FTD-first traffic "
    "and registration checks"
)


def build_volume_049_diagrams_data() -> List[Dict]:
    """Return the eight Volume 049 diagram dicts built from attributed practitioner testimony."""
    return [
        {
            "diagram_id": "diag-01-prediction-market-terminal-wiring",
            "chapter_number": 1,
            "title": "Wiring a Prediction-Market Terminal in Five Steps",
            "subtitle": "From a cached Kalshi catalog to a capped, logged fill-or-kill order",
            "chart_type": "process_flow",
            "stages": [
                {
                    "step": "01",
                    "label": "Cache the Kalshi catalog",
                    "value": "Step 1",
                    "detail": (
                        "Page roughly 30,000 events at 200 per request; the cold load took 193 seconds "
                        "and 1.5 seconds from the Streamlit cache, with an invalidation rule because odds keep moving."
                    ),
                },
                {
                    "step": "02",
                    "label": "Normalize the two venue schemas",
                    "value": "Step 2",
                    "detail": (
                        "Kalshi and Polymarket share almost no IDs, field names or order-book shapes; "
                        "Predictify covers 16 venues through one normalized API, free tier 25,000 credits and 7 days of history."
                    ),
                },
                {
                    "step": "03",
                    "label": "Gate every pair on equivalence",
                    "value": "Step 3",
                    "detail": (
                        "Run each cross-venue pair through the equivalence verdict; a 3-cent gap between "
                        "markets judged not equivalent is not a trade."
                    ),
                },
                {
                    "step": "04",
                    "label": "Make the model read the contract rules",
                    "value": "Step 4",
                    "detail": (
                        "Read the rules or force the LLM to read them; Perplexity structured output works about "
                        "90% of the time, so clean the string before any order call."
                    ),
                },
                {
                    "step": "05",
                    "label": "Dry-run, then fill-or-kill",
                    "value": "Step 5",
                    "detail": (
                        "Keep the $10 cap, read the snapshot, estimate and trade-or-skip reason in the logs, then "
                        "mimic a market order with fill-or-kill plus an aggressive yes price; RSA keys stay in a .env file."
                    ),
                },
            ],
            "caption": (
                "Practitioners wire a split stack: Kalshi for the regulated, KYC'd fiat account and Polymarket "
                "for crypto-native volume, joined by a normalization layer and gated before any live order."
            ),
            "assumptions_note": (
                "Step order is a synthesis of separate practitioner workflows; every figure is as reported by the "
                "named speaker, and settlement lag of about an hour to more than 12 hours after close should be budgeted."
            ),
            "note": (
                "Attributed to Part Time Larry (Ib0BEFKAvn0), OngPredicts (HtGMBJ7ynjs, OEhjqCpa1Uw, kDOrvOpgzjE), "
                "Robot Traders (yYjo1lzNoGI) and Defined (LefzH8sYzRI)."
            ),
        },
        {
            "diagram_id": "diag-02-odds-data-pipe-freshness-funnel",
            "chapter_number": 6,
            "title": "The Odds Data-Pipe Freshness Funnel",
            "subtitle": "Rejecting stale feeds down to a 5-second refresh and a priced cross-book gap",
            "chart_type": "funnel",
            "stages": [
                {
                    "label": "Reject 5-minute delayed feeds",
                    "value": 300,
                    "display": "300 seconds of delay",
                    "conversion": "Baseline to reject",
                    "detail": (
                        "OddsJam dismisses five-minute delayed feeds as useless when lines move on injury news."
                    ),
                },
                {
                    "label": "Demand a 99.9 uptime floor",
                    "value": 99.9,
                    "display": "99.9 uptime",
                    "conversion": "Feed qualifies on availability",
                    "detail": (
                        "OddsJam cites 99.9 uptime alongside sportsbook and market coverage when pitching the API."
                    ),
                },
                {
                    "label": "Cache responses for 30 seconds",
                    "value": 30,
                    "display": "30-second cache and refresh",
                    "conversion": "Dashboard refresh matches the cache",
                    "detail": (
                        "SportsGameOdds caches the events response for 30 seconds; trim oddIDs, pass a bookmakerID, "
                        "keep the key in .env.local on the server and send it in the X-API-Key header."
                    ),
                },
                {
                    "label": "Surface the cross-book gap",
                    "value": 12.5,
                    "display": "12.5% spread between -167 and +300",
                    "conversion": "Gap becomes a locked edge",
                    "detail": (
                        "Brandon of DingerStats flags a Rangers-Angels game where two books priced sides 12.5% apart."
                    ),
                },
                {
                    "label": "Act on a 5-second refresh",
                    "value": 5,
                    "display": "5-second refresh on most markets",
                    "conversion": "Price acted on while still live",
                    "detail": (
                        "OddsJam pushes five-second refresh on most markets so the gap is still there when the bet goes in."
                    ),
                },
            ],
            "caption": (
                "Odds operators agree latency and coverage decide value: reject delayed feeds, cache deliberately, "
                "and only act on gaps priced from fresh lines."
            ),
            "assumptions_note": (
                "Stage values carry their reported units (seconds, uptime, percent spread) and are ordered as a "
                "pipeline, not as a measured conversion ratio between stages."
            ),
            "note": (
                "Attributed to OddsJam (Sports Betting Strategy & Education, ZTKIge6SyQI and Gjuo-nBvRiM) and "
                "SportsGameOdds API (JXdlRbDVFNY, auctQZC3iOE)."
            ),
        },
        {
            "diagram_id": "diag-03-pro-desk-leakage-waterfall",
            "chapter_number": 3,
            "title": "Pro Desk Leakage Stress Test",
            "subtitle": "How cross-book hedging, fee load and a rules miss erode a $100K book",
            "chart_type": "waterfall",
            "bars": [
                {"label": "Up on FanDuel", "value": 100000, "display": "$100K", "kind": "total"},
                {"label": "Down on DraftKings", "value": 20000, "display": "-$20K", "kind": "deduction"},
                {"label": "Net year-end book", "value": 80000, "display": "$80K", "kind": "result"},
                {"label": "One month of order-book fee load", "value": 10000, "display": "-$10K", "kind": "deduction"},
                {"label": "NASCAR pole rules loss", "value": 35000, "display": "-$35K", "kind": "deduction"},
                {"label": "Remaining after leakage", "value": 35000, "display": "$35K", "kind": "result"},
            ],
            "caption": (
                "Pro desks find the edge is structural, with makers earning about +2.5% per trade against takers, "
                "but the gains leak through cross-book exposure, software fees and resolution wording."
            ),
            "assumptions_note": (
                "Composite stress test stacking separately reported figures from different traders; the $80K and $35K "
                "results are arithmetic on those figures, and the $10K is the fee load at about $0.02 per contract on "
                "roughly $5M of monthly volume."
            ),
            "note": (
                "Attributed to SharpMoney (O3v0_n4fZLQ) for the FanDuel and DraftKings hedge, and Inside Prediction "
                "Markets (tM5MKtoBoZ0, ieRL4BXtMGA) for Clay's fee load and Steven's $35K NASCAR loss."
            ),
        },
        {
            "diagram_id": "diag-04-live-trading-latency-ladder",
            "chapter_number": 2,
            "title": "The Live-Trading Latency Ladder",
            "subtitle": "Seconds separating consumer signals from the traders already moving the price",
            "chart_type": "horizontal_bars",
            "unit": "seconds",
            "bars": [
                {"label": "OddsJam odds refresh", "min": 5, "max": 5, "typical": 5, "display": "5 seconds"},
                {"label": "ESPN Gamecast lead over TV", "min": 5, "max": 15, "typical": 10, "display": "5 to 15 seconds"},
                {"label": "Consumer stream delay", "min": 7, "max": 30, "typical": 10, "display": "7, 10 or up to 30 seconds"},
                {"label": "Free feed lag", "min": 15, "max": 30, "typical": 22.5, "display": "15 to 30 seconds"},
                {"label": "Dashboard cache window", "min": 30, "max": 30, "typical": 30, "display": "30 seconds"},
            ],
            "caption": (
                "Latency is the hard ceiling on live cross-venue trading: an ESPN-fed Kalshi bot lost money as Kalshi "
                "moved before the free signal, while pro feeds run near $5,000 a month."
            ),
            "assumptions_note": (
                "Typical values are the midpoint of the stated range where no point estimate was given (Gamecast, free "
                "feed); the consumer stream typical uses the 10-second figure named by the speaker. Refresh and cache "
                "bars come from odds-API practitioners for comparison."
            ),
            "note": (
                "Attributed to Part Time Larry (bA_NUrMJuw4), Whale Slots (QpjzafRRmjQ), OddsJam (ZTKIge6SyQI) and "
                "SportsGameOdds API (JXdlRbDVFNY)."
            ),
        },
        {
            "diagram_id": "diag-05-event-contract-trading-and-listing-gates",
            "chapter_number": 5,
            "title": "Event-Contract Trading and Listing Gates",
            "subtitle": "Four checks before a trade or a listing reaches a registered DCM",
            "chart_type": "decision_tree",
            "nodes": [
                {
                    "gate": "G1",
                    "question": "Is the trade free of information from your job, your campaign or your employer?",
                    "pass_next": "G2",
                    "fail_action": (
                        "Kill the trade; a signed confidentiality agreement turns it into misappropriation and the CFTC will come after you."
                    ),
                },
                {
                    "gate": "G2",
                    "question": "Is the position free of any public misstatement meant to move price?",
                    "pass_next": "G3",
                    "fail_action": (
                        "Stop; pushing misstatements is market manipulation with or without insider-trading liability."
                    ),
                },
                {
                    "gate": "G3",
                    "question": (
                        "For a mention contract, are potential controllers and known insiders identified, with position "
                        "limits, accountability, reporting and surveillance calibrated to them?"
                    ),
                    "pass_next": "G4",
                    "fail_action": "Hold the listing until the insider map and surveillance calibration are done.",
                },
                {
                    "gate": "G4",
                    "question": "Do the terms of any geopolitical contract expressly carve out war pathways?",
                    "pass_next": "List on a registered DCM operating under its 23 core principles.",
                    "fail_action": (
                        "Redraft; under the proposal a facially neutral 'facility remains functional' contract involves war unless carved out."
                    ),
                },
            ],
            "caption": (
                "Insider trading and manipulation rules apply to prediction markets; a teleprompter operator's roughly "
                "50 mention-market trades drew a $65,000 penalty after the up-to-25% cooperation discount."
            ),
            "assumptions_note": (
                "Gate order is a synthesis of separate practitioner guidance; jurisdiction remains contested as Nevada "
                "and Massachusetts sue directly in state court."
            ),
            "note": (
                "Attributed to NEXTPredict (uh3GgMs9ha8, Miller), Profeissor.com Digital Assets, AI & FinTech "
                "(YIkTrxNRVlc, 4Vqws7tSo8E, G-sfCPFFZ5o) and A Lawyer In Finance Explains (MHeX-gRNpCE)."
            ),
        },
        {
            "diagram_id": "diag-06-product-first-affiliate-traffic-team",
            "chapter_number": 11,
            "title": "Product-First Affiliate Traffic Architecture",
            "subtitle": "Owning a product, a tool or an audience instead of renting vanity traffic",
            "chart_type": "org_architecture",
            "center": {
                "role": "Product-first affiliate owner",
                "headcount": "Not reported by practitioners",
                "focus": "Own the product, tool or audience; SEO is where player value is highest",
            },
            "spokes": [
                {
                    "role": "Technical SEO and link lead",
                    "type": "Organic search",
                    "kpi": (
                        "Content confirmed visible to Google before any link is bought; about 7% of links lost per year "
                        "recovered via Majestic and Giga Indexer"
                    ),
                },
                {
                    "role": "AI search lead",
                    "type": "Generative engine visibility",
                    "kpi": (
                        "Bing Webmaster Tools live and cited listicles reverse-engineered; at least two of domain, "
                        "article and anchor relevance"
                    ),
                },
                {
                    "role": "Owned audience lead",
                    "type": "App, email and Telegram capture",
                    "kpi": "20%+ conversion into banner click, subscription or add-to-bet-slip versus well under 1%",
                },
                {
                    "role": "Paid acquisition lead",
                    "type": "PPC and paid social",
                    "kpi": "Optimized to FTDs not sign-ups, bots filtered, no fast scaling while CPC climbs 40 to 80% at peaks",
                },
            ],
            "caption": (
                "Content-only SEO is over; winners pair search with owned audiences and FTD-optimized paid traffic, "
                "with revshare players worth $500 to $2,000 each on 25 to 50% deals."
            ),
            "assumptions_note": (
                "Role split is a synthesis of separate practitioner workflows; no team headcount was reported, and "
                "black-hat tactics remain disputed between practitioners."
            ),
            "note": (
                "Attributed to Big Pond Digital (0_KHkuMmtVQ, jWqa6ck6G3Y), Revpanda Group (OlzqNLFabLI, Xyf6JUN9RFg), "
                "Odys Podcast (ESj1bVRdO2s) and Powerhouse Affiliate (pihR_hy7xRU)."
            ),
        },
        {
            "diagram_id": "diag-07-event-contract-fee-load-by-route",
            "chapter_number": 4,
            "title": "Event-Contract Fee Load by Route",
            "subtitle": "Cents per contract across ForecastEx, Kalshi via IBKR and settlement",
            "chart_type": "stacked_comparison",
            "total_range": "0 to 4 cents per contract depending on venue and exit path",
            "buckets": [
                {
                    "label": "Held to settlement",
                    "low": 0,
                    "high": 0,
                    "notes": "Settlement is fee-free; contracts pay $1 or $0.",
                },
                {
                    "label": "ForecastEx pairing fee",
                    "low": 0.5,
                    "high": 1,
                    "notes": "Yes plus No pairs at $1.01, half a penny per side, with no other exchange, clearing, data or brokerage fees.",
                },
                {
                    "label": "Kalshi via IBKR to settlement",
                    "low": 2,
                    "high": 2,
                    "notes": "$0.01 IBKR plus $0.01 exchange per contract.",
                },
                {
                    "label": "Kalshi via IBKR early exit",
                    "low": 4,
                    "high": 4,
                    "notes": "Exiting early doubles the fees, turning a 48-cent exit into about 46 cents net.",
                },
            ],
            "caption": (
                "Binary contracts priced between roughly 1 and 99 cents read as probability; limit orders only, "
                "because thin books make market orders pay the wide spread on top of the fee."
            ),
            "assumptions_note": (
                "Round-trip fee for an early exit is the doubled figure reported by TC Trading; spread costs in thin "
                "books were described but not quantified, so they are excluded."
            ),
            "note": (
                "Attributed to Interactive Brokers (ceR-weGZSXc), TC Trading (MREcV1sLqwc) and closeuptrading (4_swDdRFYJc)."
            ),
        },
        {
            "diagram_id": "diag-08-cftc-counterparty-and-agent-readiness",
            "chapter_number": 12,
            "title": "Four-Week Counterparty and Agent Readiness Roadmap",
            "subtitle": "Registration, collateral, funding math and agent controls before capital moves",
            "chart_type": "timeline_roadmap",
            "weeks": [
                {
                    "week": "Week 1",
                    "title": "Registration check",
                    "deliverable": "CFTC registration and NFA membership confirmed through NFA BASIC plus enforcement records",
                    "gate": "If either registration is missing, walk away; an RFED must hold at least $20 million",
                },
                {
                    "week": "Week 2",
                    "title": "FCM due diligence",
                    "deliverable": (
                        "Vanguard checklist run on capital levels, top-tier 1.25 securities, audit and seg-compliance "
                        "history and custodian rigor"
                    ),
                    "gate": "Concentration noted with about 10 firms holding 80% of customer funds",
                },
                {
                    "week": "Week 3",
                    "title": "Perpetual funding model",
                    "deliverable": "Each venue's premium math and observation periods modeled, not a headline rate",
                    "gate": "Funding every 8 hours capped near 2%, up to 6% per 24 hours, priced before sizing",
                },
                {
                    "week": "Week 4",
                    "title": "Agent controls and CCO reporting",
                    "deliverable": "Risk controls and audit logs outside the agent harness with hard limits and a kill switch",
                    "gate": "Unredacted home-regulator CCO report or full Reg 3.3 report, never a hybrid",
                },
            ],
            "caption": (
                "The CFTC stack runs on registration and segregation, and with more than 70% of futures trading "
                "automated, the deploying firm is expected to answer for its agents."
            ),
            "assumptions_note": (
                "Weekly cadence is an organizing assumption; the practitioners reported the checks and figures, not "
                "a four-week schedule."
            ),
            "note": (
                "Attributed to Brokerchampion (CIinXD9tbVo), CFTC roundtables (yUqRhv7w9Vs, ZEPjpgVSavY, Ckw1w5mSMIQ, "
                "ec9Mk3slriY) and A Lawyer In Finance Explains (BO0iMB23sU4)."
            ),
        },
    ]


VOLUME_049_POSITIONING_ALTERNATIVES: List[Dict] = [
    {
        "title": "The Event-Contract Desk",
        "subtitle": "Wiring Kalshi and Polymarket, gating cross-venue pairs and making markets where retail buys longshots",
        "audience": "Builders and traders running regulated prediction-market terminals and cross-venue books",
        "research_basis": (
            "Cached 30,000-event Kalshi catalogs, 16-venue normalization, a $7.75 net on a $100 two-leg pair, "
            "5-cent contracts winning 4.18% of the time, and Clay's roughly 10% ROI on about $60M of manual volume."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=HtGMBJ7ynjs&t=231s",
            "https://www.youtube.com/watch?v=Ib0BEFKAvn0&t=887s",
            "https://www.youtube.com/watch?v=lYFPEQllQOw&t=155s",
            "https://www.youtube.com/watch?v=vT0qMNgOkxo&t=336s",
            "https://www.youtube.com/watch?v=tM5MKtoBoZ0&t=1199s",
        ],
        "validation_status": "Grounded strictly in Vol. 049 YouTube practitioner transcripts.",
    },
    {
        "title": "Follow the NGR",
        "subtitle": "Licensed iGaming affiliate deals run through the math before the first click is bought",
        "audience": "Casino and sportsbook affiliates negotiating CPA, revshare and hybrid deals in regulated GEOs",
        "research_basis": (
            "A 35% deal paying an effective 24.5% of GGR, a $400 CPA collapsing to $20 at 5% qualification, "
            "monthly carryover resets, GEO segmentation that saves 90K of a 100K month, and a 20% click-to-FTD "
            "guarantee lifting a German CPA to an effective EUR 1,600."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=WaWQNIAchz0&t=295s",
            "https://www.youtube.com/watch?v=_puyhQJIomQ&t=395s",
            "https://www.youtube.com/watch?v=6jlPOcl5CnI&t=853s",
            "https://www.youtube.com/watch?v=ohEZ5-gHckQ&t=1212s",
            "https://www.youtube.com/watch?v=jWqa6ck6G3Y&t=1260s",
        ],
        "validation_status": "Grounded strictly in Vol. 049 YouTube practitioner transcripts.",
    },
    {
        "title": "Licensed or Walk Away",
        "subtitle": "Registration, rulebooks and insider gates for event contracts and iGaming partners",
        "audience": "Compliance leads, operators and agent builders entering CFTC-regulated and licensed gaming markets",
        "research_basis": (
            "A $65,000 mention-market penalty, 23 DCM core principles, NFA BASIC checks, a $20 million RFED capital "
            "floor, agent kill switches outside the harness, Bulgaria's roughly EUR 6,000 affiliate license, and an "
            "8-page rules document read before the first order."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=uh3GgMs9ha8&t=853s",
            "https://www.youtube.com/watch?v=G-sfCPFFZ5o&t=319s",
            "https://www.youtube.com/watch?v=CIinXD9tbVo&t=370s",
            "https://www.youtube.com/watch?v=Ckw1w5mSMIQ&t=3867s",
            "https://www.youtube.com/watch?v=XUPjmWHBPq4&t=92s",
            "https://www.youtube.com/watch?v=MREcV1sLqwc&t=285s",
        ],
        "validation_status": "Grounded strictly in Vol. 049 YouTube practitioner transcripts.",
    },
]
