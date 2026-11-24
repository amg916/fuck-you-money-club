from __future__ import annotations

VOLUME_025_SUBTITLE: str = (
    "Niche into steel, lumber and machinery, post the $75,000 bond at a negotiated premium, "
    "win five great shippers with relentless touches, price from the truck up, lock accessorials "
    "into the rate con, and fence out double brokers before the cargo goes dark"
)


def build_volume_025_diagrams_data() -> list[dict]:
    return [
        {
            "diagram_id": "diag-01-launch-roadmap",
            "chapter_number": 1,
            "title": "Five-Step Brokerage Launch Roadmap",
            "subtitle": "From niche selection to a funded float, per Matt Krause and The Finance Pro",
            "chart_type": "process_flow",
            "caption": (
                "Krause launches on hard freight, files authority for roughly $2,500 to $4,500 all-in, "
                "runs a stack near $300 a month, and funds the float before booking volume."
            ),
            "assumptions_note": (
                "Dollar figures are attributed practitioner claims. Startup cost excludes training. "
                "The $40,000 float assumes 10 loads a week, as Krause frames it."
            ),
            "note": (
                "Sources - Matt Krause (afV63okbAMs, bP4Dnpd58PE) and The Finance Pro (29d2gRCN8Ng)."
            ),
            "stages": [
                {
                    "step": "01",
                    "label": "Pick a hard-freight niche",
                    "value": "Step 1",
                    "detail": (
                        "Chase steel, lumber and machinery, which Krause calls 1/4 of the work for the "
                        "same money. Satellite recon shows white rectangles for lumber, gray cylinders "
                        "for steel coils and yellow shapes for machinery."
                    ),
                },
                {
                    "step": "02",
                    "label": "File authority and bond",
                    "value": "Step 2",
                    "detail": (
                        "The $300 FMCSA fee, BMC-84 premium, BOC-3, $46 UCR, LLC and contingent cargo "
                        "run about $2,500 to $3,500, or $3,500 to $4,500 with weaker credit."
                    ),
                },
                {
                    "step": "03",
                    "label": "Stand up the tech stack",
                    "value": "Step 3",
                    "detail": (
                        "Load board ~$150, vetting tool $50-$100, TMS ~$25 or free, phone $30. "
                        "Total ~$300 a month, covered by one $400-margin load."
                    ),
                },
                {
                    "step": "04",
                    "label": "Build the prospect list",
                    "value": "Step 4",
                    "detail": (
                        "Look for 3+ dock doors with trailers and a careers page posting logistics "
                        "openings, then star 50 prospects before dialing. Who is on the list matters "
                        "more than how many."
                    ),
                },
                {
                    "step": "05",
                    "label": "Fund the float",
                    "value": "Step 5",
                    "detail": (
                        "At 10 loads a week a new desk is $40,000 out of pocket by week four. With $10K "
                        "of monthly overhead at $200 per load, break-even is 50 loads a month."
                    ),
                },
            ],
        },
        {
            "diagram_id": "diag-02-cold-call-funnel",
            "chapter_number": 6,
            "title": "From Dials to a Recurring Account",
            "subtitle": "Touch volume and the test-load conversion, per Dennis Brown and Matt Krause",
            "chart_type": "funnel",
            "caption": (
                "Phone-built brokers win on volume and follow-up. One 'we don't use brokers' prospect "
                "became a $150 test load and roughly $20,000 a year in profit."
            ),
            "assumptions_note": (
                "Stages mix units (monthly touches, daily calls, touches per close, loads), so stage "
                "values show order of magnitude, not a single cohort conversion rate."
            ),
            "note": (
                "Sources - Matt Krause (NF0itNMuQvY, r0gf3CDabxw) and FreightBrokers with Dennis Brown "
                "(BCLv7SfCxIo, kc6-g1EZ0Fk, knW5LzcUJIw)."
            ),
            "stages": [
                {
                    "label": "Monthly touches per yes",
                    "value": 300,
                    "display": "~300 touches/month",
                    "conversion": "About one shipper yes per ~300 monthly touches (Krause)",
                    "detail": "Krause runs 10-20 nightly touches after burning out at 100 a day.",
                },
                {
                    "label": "Daily dial floor",
                    "value": 50,
                    "display": "50 calls/day",
                    "conversion": "Brown's minimum; brokers who stop prospecting stop growing",
                    "detail": (
                        "Retire 'did I catch you at a bad time' - Gong figures put it under 1%, about "
                        "40% worse than average."
                    ),
                },
                {
                    "label": "Touches to close",
                    "value": 12,
                    "display": "8-12 touches",
                    "conversion": "6-8 is reasonable; it never closes on the first call",
                    "detail": "Follow-up across phone, email, LinkedIn and face-to-face carries the deal.",
                },
                {
                    "label": "Test load booked",
                    "value": 1,
                    "display": "$150 gross profit",
                    "conversion": "A 'we don't use brokers' prospect won with one test load",
                    "detail": "Take three of five loads you can cover rather than committing to five and covering three.",
                },
                {
                    "label": "Recurring account",
                    "value": 1,
                    "display": "~$20,000/year",
                    "conversion": "Over $100,000 across 5+ years from that single pet food shipper",
                    "detail": (
                        "Send the handover email the moment the carrier is confirmed, with carrier, "
                        "pickup time, driver and the driver's direct number."
                    ),
                },
            ],
        },
        {
            "diagram_id": "diag-03-bond-premium-ladder",
            "chapter_number": 3,
            "title": "The BMC-84 Premium Ladder",
            "subtitle": "Annual premium on a $75,000 bond, from sub-600 credit to the best market rate",
            "chart_type": "waterfall",
            "caption": (
                "Brokers pay a credit-driven percentage, not $75,000 in cash. Quotes run from $8,000 to "
                "$10,000 for sub-600 scores down to $975 at a 1.3% rate."
            ),
            "assumptions_note": (
                "Each step lands on a reported premium. Step sizes are the arithmetic gaps between those "
                "reported quotes, not separate practitioner figures."
            ),
            "note": (
                "Sources - Surety Bonds Direct (tkM7CbVBoC0), Brandon Scott (lzC0i5OReRU), Brandon Manney "
                "The Mentor (BKciSMvLpD8) and Freight Broker TV (wSNSmdThc6A)."
            ),
            "bars": [
                {
                    "label": "Sub-600 credit quote",
                    "value": 10000,
                    "display": "$8,000-$10,000/yr (upper end)",
                    "kind": "total",
                },
                {
                    "label": "Poor credit at 4.6%",
                    "value": 6550,
                    "display": "Down to $3,450/yr",
                    "kind": "deduction",
                },
                {
                    "label": "Scott's accepted first quote",
                    "value": 450,
                    "display": "Down to $3,000/yr",
                    "kind": "deduction",
                },
                {
                    "label": "Renegotiated at term end",
                    "value": 1500,
                    "display": "Down to $1,500/yr",
                    "kind": "deduction",
                },
                {
                    "label": "Best market rate at 1.3%",
                    "value": 525,
                    "display": "Down to $975/yr",
                    "kind": "deduction",
                },
                {
                    "label": "Strong-credit premium",
                    "value": 975,
                    "display": "$975/yr on $75,000",
                    "kind": "result",
                },
            ],
        },
        {
            "diagram_id": "diag-04-authority-cost-ranges",
            "chapter_number": 2,
            "title": "What Broker Authority Actually Costs",
            "subtitle": "Reported cost ranges for filing, process agent, UCR, bond premium and all-in launch",
            "chart_type": "horizontal_bars",
            "unit": "USD",
            "caption": (
                "Authority is $300 per type, but the bond premium swings from $900 to $9,000 on owner "
                "credit and dominates the all-in launch bill."
            ),
            "assumptions_note": (
                "The 'typical' marker is a practitioner-named anchor where one exists (Scott's $3,000 "
                "quote, Krause's $3,500 band edge); otherwise it is the upper end of the reported range."
            ),
            "note": (
                "Sources - The Broker Intellect (5TtQ4-VoZuI), Truckers Authority (jyVHYDl8PgQ), "
                "Matt Krause (afV63okbAMs, hhT4X32MspU) and Brandon Scott (lzC0i5OReRU)."
            ),
            "bars": [
                {
                    "label": "Application fee per authority",
                    "min": 300,
                    "max": 300,
                    "typical": 300,
                    "display": "$300 per authority type; $0 paid means only a DOT number",
                },
                {
                    "label": "UCR filing",
                    "min": 46,
                    "max": 46,
                    "typical": 46,
                    "display": "$46",
                },
                {
                    "label": "Process agent (BOC-3)",
                    "min": 20,
                    "max": 100,
                    "typical": 100,
                    "display": "$20-$100; must cover every operating state",
                },
                {
                    "label": "BMC-84 bond premium",
                    "min": 900,
                    "max": 9000,
                    "typical": 3000,
                    "display": "$900-$9,000 by owner credit",
                },
                {
                    "label": "All-in authority launch",
                    "min": 2500,
                    "max": 4500,
                    "typical": 3500,
                    "display": "$2,500-$3,500; up to $4,500 with weaker credit",
                },
            ],
        },
        {
            "diagram_id": "diag-05-shipper-qualification-gates",
            "chapter_number": 5,
            "title": "Four Gates Before a Shipper Earns More Freight",
            "subtitle": "Vetting, margin floor, payment terms and pipeline discipline, per Dennis Brown",
            "chart_type": "decision_tree",
            "caption": (
                "Brown's startup rules - vet every party, hold a $100 floor, state 30-day terms, and keep "
                "90%+ of time on prospecting - protect cash while 5-10 shippers build a six-figure book."
            ),
            "assumptions_note": (
                "Gate order is an editorial sequence. Each threshold is quoted from FreightBrokers "
                "sessions led by Dennis Brown."
            ),
            "note": (
                "Source - FreightBrokers with Dennis Brown (UhCy0ncTrTI, j9lUdJynzFA, dciVQpw-BWM, "
                "kc6-g1EZ0Fk)."
            ),
            "nodes": [
                {
                    "gate": "G1",
                    "question": "Has due diligence cleared the shipper, the carrier and the driver?",
                    "pass_next": "G2",
                    "fail_action": "Hold the tender until all three checks are complete.",
                },
                {
                    "gate": "G2",
                    "question": "Does the load clear $100 gross while targeting 10-15% margin?",
                    "pass_next": "G3",
                    "fail_action": (
                        "After the deliberate break-even first load, drop shippers below $100 gross."
                    ),
                },
                {
                    "gate": "G3",
                    "question": "Were 30-day terms stated upfront and AP called after the first load?",
                    "pass_next": "G4",
                    "fail_action": "Trigger a credit hold at 60 days unpaid.",
                },
                {
                    "gate": "G4",
                    "question": "Is 90% or more of time still spent prospecting as loads arrive?",
                    "pass_next": "Grow toward 5-10 active small-to-midsize shippers.",
                    "fail_action": "Rebuild the pipeline; the business dies when prospecting stops.",
                },
            ],
        },
        {
            "diagram_id": "diag-06-fraud-defense-desk",
            "chapter_number": 11,
            "title": "The Double-Brokering Defense Desk",
            "subtitle": "Four controls that treat freight fraud as identity theft",
            "chart_type": "org_architecture",
            "caption": (
                "Double brokering cost an estimated $2 to $3 billion in 2024, and a $75,000 bond paid "
                "Convoy carriers under 10 cents on the dollar. Defense is verification, not insurance."
            ),
            "assumptions_note": (
                "No practitioner reported desk staffing levels, so headcount is left unspecified. "
                "Spokes are controls, not mandated roles."
            ),
            "note": (
                "Sources - Double Broker Bounty Hunter (J96nZa6x_Ek, 3dI5z6SHDPc, 3WxrmhqpsyY), Highway "
                "(b-vDBH9GpuA, sKKld4Wdyqg), Overdrive with Hank Seaton (jnoJihiGSEA) and Freight 360 "
                "(uGu6NcZkt28)."
            ),
            "center": {
                "role": "Carrier Vetting and Fraud Desk",
                "headcount": "Not reported by practitioners",
                "focus": "Confirm who is actually hauling before any pickup number leaves the building.",
            },
            "spokes": [
                {
                    "role": "Association Insights Screen",
                    "type": "Vetting platform (Highway)",
                    "kpi": (
                        "Flag shared addresses, phones and equipment; 10+ trucks claimed from a "
                        "residential area; 16 trucks with no inspections in 24 months."
                    ),
                },
                {
                    "role": "Rate Anomaly Check",
                    "type": "Pricing trigger (Double Broker Bounty Hunter)",
                    "kpi": "Dig at 20% above or below market; 30% above is most likely a scam.",
                },
                {
                    "role": "Credential and PIN Hygiene",
                    "type": "Account security",
                    "kpi": (
                        "DOT PIN reset since the March 2023 breach; never authenticate a load board "
                        "login from an emailed link."
                    ),
                },
                {
                    "role": "Pickup Proof and BOL Control",
                    "type": "Dispatch protocol (Overdrive, Freight 360)",
                    "kpi": (
                        "Authorized carrier name on every bill of lading, a gap on two-thirds to "
                        "three-quarters of shipments; stacked pickup photo requests."
                    ),
                },
            ],
        },
        {
            "diagram_id": "diag-07-agent-split-ranges",
            "chapter_number": 4,
            "title": "Freight Agent Commission Splits",
            "subtitle": "Share of margin, never of gross, by agent tenure and book",
            "chart_type": "stacked_comparison",
            "total_range": "40%-70% of load margin",
            "caption": (
                "On a $300 margin at a 60% split the agent keeps $180 and the brokerage $120. The broker "
                "carries authority, bond, back office and credit risk."
            ),
            "assumptions_note": (
                "Percentages apply to margin only. Ask what comes out before and after the split - load "
                "board, software, insurance - since the headline rate is not take-home."
            ),
            "note": (
                "Sources - Matt Krause (hhT4X32MspU) and FreightBrokers with Connor Harutyunyan of ALG "
                "(jgNUpO0VPws)."
            ),
            "buckets": [
                {
                    "label": "Low-paying brokerages",
                    "low": 40,
                    "high": 40,
                    "notes": "Some brokerages pay 40%.",
                },
                {
                    "label": "New agents",
                    "low": 50,
                    "high": 50,
                    "notes": "New agents typically start near 50%.",
                },
                {
                    "label": "Agents bringing shippers or volume",
                    "low": 60,
                    "high": 70,
                    "notes": "Tenured, high-volume agents reach 60 to 70%.",
                },
                {
                    "label": "Veteran ALG agent",
                    "low": 67,
                    "high": 67,
                    "notes": "Connor Harutyunyan reports about 67% of profit.",
                },
            ],
        },
        {
            "diagram_id": "diag-08-claims-readiness-roadmap",
            "chapter_number": 12,
            "title": "Four-Week Cargo Claims Readiness Plan",
            "subtitle": "Evidence, coverage proof, high-value protocol and claim filing",
            "chart_type": "timeline_roadmap",
            "caption": (
                "Brokers sit outside Carmack and contingent cargo only matches what the carrier carries; "
                "Peerless saw one $17,000 contingent payout in 45 years. Documents win claims."
            ),
            "assumptions_note": (
                "The weekly sequence is an editorial rollout. Clocks, tracker prices and payout figures "
                "are attributed practitioner claims."
            ),
            "note": (
                "Sources - Freight 360 (qTcDOmwZMjI), LOGISTICS RISK EXPERT by Cassandra Gaines "
                "(Ig6sI3O1a14), CargoRex with Jared Palmer (xQYjaYAvyms) and Cargo Rant (NxIispBOkz8)."
            ),
            "weeks": [
                {
                    "week": "Week 1",
                    "title": "Build the claim file first",
                    "deliverable": (
                        "Standing folder per load with bill of lading, commercial invoice, packing list, "
                        "photos and every carrier email."
                    ),
                    "gate": "No load closes without its evidence file started.",
                },
                {
                    "week": "Week 2",
                    "title": "Prove coverage in writing",
                    "deliverable": (
                        "Certificates pulled through Highway, RMIS or AssureAssist as holder; carrier's "
                        "insurance agent emails confirmation that the commodity is not excluded."
                    ),
                    "gate": "A carrier's verbal yes does not count.",
                },
                {
                    "week": "Week 3",
                    "title": "Lock the high-value protocol",
                    "deliverable": (
                        "High-value loads go only to relationship carriers, never a load board, with a "
                        "covert tracker now about $15 instead of $750."
                    ),
                    "gate": "Theft response begins inside the 24 to 48 hour window.",
                },
                {
                    "week": "Week 4",
                    "title": "Standardize claim filing",
                    "deliverable": (
                        "Formal written claim with a dollar amount and commercial invoice, tracked "
                        "against the 30-day acknowledgment and 120-day disposition clocks."
                    ),
                    "gate": "Check contracts for a specific nine-month limit before accepting 'too old'.",
                },
            ],
        },
    ]


VOLUME_025_POSITIONING_ALTERNATIVES: list[dict] = [
    {
        "title": "The Hard-Freight Spread",
        "subtitle": "Launch a brokerage on steel, lumber and machinery for a few thousand dollars and a funded float",
        "audience": "First-time owners weighing authority, bond and startup cash",
        "research_basis": (
            "Matt Krause prices authority at $2,500 to $4,500 and a stack near $300 a month, chases "
            "hard freight as 1/4 of the work, and warns of a $40,000 float by week four; Brandon Scott "
            "halved a $3,000 bond premium at renewal."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=afV63okbAMs&t=470s",
            "https://www.youtube.com/watch?v=bP4Dnpd58PE&t=390s",
            "https://www.youtube.com/watch?v=bP4Dnpd58PE&t=1899s",
            "https://www.youtube.com/watch?v=VD-td9ERDAU&t=123s",
            "https://www.youtube.com/watch?v=lzC0i5OReRU&t=318s",
        ],
        "validation_status": "Grounded strictly in Vol. 025 YouTube practitioner transcripts.",
    },
    {
        "title": "Five Great Shippers",
        "subtitle": "Touch counts, scripts and test loads that turn cold dials into six-figure books",
        "audience": "New brokers and agents stuck before their first recurring account",
        "research_basis": (
            "Dennis Brown says 5-10 shippers produce six figures and closes take 8-12 touches; Krause "
            "counts about 300 touches per yes; a $150 test load grew to about $20,000 a year."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=kc6-g1EZ0Fk&t=425s",
            "https://www.youtube.com/watch?v=kc6-g1EZ0Fk&t=2158s",
            "https://www.youtube.com/watch?v=NF0itNMuQvY&t=141s",
            "https://www.youtube.com/watch?v=r0gf3CDabxw&t=559s",
            "https://www.youtube.com/watch?v=knW5LzcUJIw&t=285s",
        ],
        "validation_status": "Grounded strictly in Vol. 025 YouTube practitioner transcripts.",
    },
    {
        "title": "Broker Without the Burn",
        "subtitle": "Fraud vetting, bond floors and claim files that keep one bad load from ending the business",
        "audience": "Operating brokers exposed to double brokering, cargo theft and claims",
        "research_basis": (
            "Double Broker Bounty Hunter sizes losses at $2 to $3 billion and digs at 20% off market; "
            "ThinkFreight reports the 7-day replenishment rule; Freight 360 cites one $17,000 contingent "
            "payout in 45 years; Gaines sets the 30 and 120 day claim clocks."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=J96nZa6x_Ek&t=619s",
            "https://www.youtube.com/watch?v=3dI5z6SHDPc&t=859s",
            "https://www.youtube.com/watch?v=s-qzw5ZxjmU&t=101s",
            "https://www.youtube.com/watch?v=jnoJihiGSEA&t=1528s",
            "https://www.youtube.com/watch?v=qTcDOmwZMjI&t=867s",
            "https://www.youtube.com/watch?v=Ig6sI3O1a14&t=311s",
        ],
        "validation_status": "Grounded strictly in Vol. 025 YouTube practitioner transcripts.",
    },
]
