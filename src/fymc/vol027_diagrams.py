"""Volume 027 diagram data for Business Acquisition, drawn from practitioner testimony."""

from __future__ import annotations

VOLUME_027_SUBTITLE: str = (
    "Buy Cash Flow, Not Hope: Source Belly to Belly, Pay 2.5-4.5x Earnings, "
    "Clear SBA 7(a) at 1.25x DSCR, Prove Every Add-Back With a QoE, Lock the "
    "Working Capital Peg, and Stabilize Before You Accelerate"
)


def build_volume_027_diagrams_data() -> list[dict]:
    """Return the eight Volume 027 diagram dicts, built fresh on every call."""
    return [
        {
            "diagram_id": "diag-01-eta-buy-side-process",
            "chapter_number": 1,
            "title": "The Buy-Instead-of-Build Process",
            "subtitle": "From belly-to-belly sourcing to a six-month change freeze",
            "chart_type": "process_flow",
            "stages": [
                {
                    "step": "01",
                    "label": "Source Belly to Belly",
                    "value": "Step 1",
                    "detail": (
                        "Work brokers, trade-show lists and direct outreach in one geography; "
                        "Ruback says belly-to-belly sales beat national email campaigns, and a "
                        "Houston searcher never had lunch alone."
                    ),
                },
                {
                    "step": "02",
                    "label": "Screen Near 4x Cash Flow",
                    "value": "Step 2",
                    "detail": (
                        "Screen at about 4x cash flow and stay away from anything too asset or "
                        "capital intensive (Chicago Booth); map revenue by referral source."
                    ),
                },
                {
                    "step": "03",
                    "label": "Open at 2.5x, Concede Up to Half a Turn",
                    "value": "Step 3",
                    "detail": (
                        "Searcher Antonio opens at 2.5x; Ruback gives a quarter or half turn to "
                        "preserve goodwill, because if the deal is good at 3, it is still good."
                    ),
                },
                {
                    "step": "04",
                    "label": "LOI, 60-Day Diligence, QoE",
                    "value": "Step 4",
                    "detail": (
                        "Close on an LOI, 60 days of diligence and a QoE; reconcile 36 months of "
                        "bank statements and kill or reprice any target with two sets of books."
                    ),
                },
                {
                    "step": "05",
                    "label": "Fund, Then Freeze for Six Months",
                    "value": "Step 5",
                    "detail": (
                        "Fund with SBA 7(a) debt up to $5M, a seller note and $100-150K of "
                        "working capital; freeze personnel changes for six months post-close."
                    ),
                },
            ],
            "caption": (
                "The street mechanics of entrepreneurship through acquisition, from sourcing "
                "and screening through price, diligence, funding and the post-close freeze."
            ),
            "assumptions_note": (
                "Every multiple, dollar figure and time window is quoted from Q1 practitioners; "
                "the 4x screen and 2.5x opening offer are practitioner rules, not market averages."
            ),
            "note": (
                "Attributed to HBS Rock Center for Entrepreneurship (oJcm3Bn-lXE at 00:46:43 and "
                "00:57:40), The University of Chicago Booth School of Business (60ZOJolZwOo), "
                "Technically News (nOnsMlkLh10 at 00:58:06 and 01:08:24) and The Wall Street "
                "Skinny (MpeYmBDptXs at 00:44:27)."
            ),
        },
        {
            "diagram_id": "diag-02-sba-seller-note-capital-stack",
            "chapter_number": 6,
            "title": "The 90/5/5 Capital Stack",
            "subtitle": "How the purchase price narrows to the buyer's own cash",
            "chart_type": "funnel",
            "stages": [
                {
                    "label": "Purchase Price",
                    "value": 100,
                    "display": "100% of price",
                    "conversion": "Baseline",
                    "detail": "The full price the capital stack has to cover.",
                },
                {
                    "label": "SBA 7(a) Loan",
                    "value": 90,
                    "display": "90% of price",
                    "conversion": "90% financed by the SBA loan",
                    "detail": (
                        "Keira Hamilton calls the 90% SBA loan the base of the most common structure."
                    ),
                },
                {
                    "label": "Required Equity Injection",
                    "value": 10,
                    "display": "10% of price",
                    "conversion": "10% injection on a change of ownership",
                    "detail": (
                        "The 10% injection on an initial acquisition cannot be reduced."
                    ),
                },
                {
                    "label": "Seller Note on Full Standby",
                    "value": 5,
                    "display": "5% of price",
                    "conversion": "No more than 50% of the required injection",
                    "detail": (
                        "Counts toward equity only on full standby for the life of the loan; "
                        "never call it a 10-year note (JackQuisitions)."
                    ),
                },
                {
                    "label": "Buyer Cash",
                    "value": 5,
                    "display": "5% of price",
                    "conversion": "Remaining half of the injection",
                    "detail": (
                        "The buyer's own cash; a full 10% seller note shows up mostly for insiders "
                        "or deep industry operators."
                    ),
                },
            ],
            "caption": (
                "The street baseline of a 90% SBA loan, 5% buyer cash and a 5% seller note, "
                "with the seller note capped at half of the required injection."
            ),
            "assumptions_note": (
                "Values are percentages of purchase price as testified; combined SBA and seller "
                "note payments must still clear 1.25x debt service coverage (Josh Kim)."
            ),
            "note": (
                "Attributed to Keira Hamilton (7RAyVC1b9Pg at 00:01:27), Allan Peterson on "
                "JackQuisitions (I6M8wAaqm5s at 00:22:18), Loan To Launch (OSZgayF9jHw at "
                "00:03:06) and Josh Kim (W3nhTnkKZcU at 00:04:29)."
            ),
        },
        {
            "diagram_id": "diag-03-search-to-purchase-waterfall",
            "chapter_number": 3,
            "title": "200 Companies to One Purchase",
            "subtitle": "Pete Seligman's sourcing funnel before buying SRO",
            "chart_type": "waterfall",
            "bars": [
                {
                    "label": "Companies Screened",
                    "value": 200,
                    "display": "200 companies",
                    "kind": "total",
                },
                {
                    "label": "Dropped Before an IM",
                    "value": -150,
                    "display": "-150 (50 IMs remain)",
                    "kind": "deduction",
                },
                {
                    "label": "Dropped Before a Conversation",
                    "value": -30,
                    "display": "-30 (20 conversations remain)",
                    "kind": "deduction",
                },
                {
                    "label": "Dropped Before an Offer",
                    "value": -15,
                    "display": "-15 (5 offers remain)",
                    "kind": "deduction",
                },
                {
                    "label": "Offers Not Won",
                    "value": -4,
                    "display": "-4 (1 purchase remains)",
                    "kind": "deduction",
                },
                {
                    "label": "Company Purchased",
                    "value": 1,
                    "display": "1 purchase",
                    "kind": "result",
                },
            ],
            "caption": (
                "Search is a numbers game: about 200 companies became 50 IMs, 20 conversations, "
                "5 offers and 1 purchase, worked through online and offline brokers."
            ),
            "assumptions_note": (
                "Deductions are the differences between Seligman's stated stage counts; the "
                "funnel is one searcher's history, not an industry average."
            ),
            "note": (
                "Attributed to Pete Seligman on David Nazeem Aboud (_exEOi-Wxuk at 00:15:24 and "
                "00:15:42), with the numbers-game framing from Before You Buy or Sell a Business "
                "Podcast (Hh83Lc7sWf4 at 00:22:15)."
            ),
        },
        {
            "diagram_id": "diag-04-multiple-arbitrage-ladder",
            "chapter_number": 2,
            "title": "The Multiple Arbitrage Ladder",
            "subtitle": "Where small-company buyers pay versus where value gets marked",
            "chart_type": "horizontal_bars",
            "unit": "x earnings",
            "bars": [
                {
                    "label": "Opening Offer With Concession",
                    "min": 2.5,
                    "max": 3.0,
                    "typical": 3.0,
                    "display": "Open 2.5x, concede to 3x",
                },
                {
                    "label": "Main Street Earnings Multiple",
                    "min": 2.5,
                    "max": 4.5,
                    "typical": 4.0,
                    "display": "2.5-4.5x, screened near 4x",
                },
                {
                    "label": "Roll-Up Add-On Purchase",
                    "min": 4.0,
                    "max": 5.0,
                    "typical": 4.5,
                    "display": "Buy at 4-5x",
                },
                {
                    "label": "Roll-Up Exit Target",
                    "min": 7.0,
                    "max": 7.5,
                    "typical": 7.25,
                    "display": "Exit at 7-7.5x",
                },
                {
                    "label": "Public Company Multiple",
                    "min": 19.0,
                    "max": 28.0,
                    "typical": 23.5,
                    "display": "19-28x",
                },
            ],
            "caption": (
                "Main Street businesses trade at 2.5-4.5x earnings against 19-28x for public "
                "companies, and Deibel's roll-up model buys at 4-5x to target 7-7.5x exits."
            ),
            "assumptions_note": (
                "Typical marks the testified anchor where one exists (3x from Ruback, about 4x "
                "from the Q1 screen); where only a range was testified, typical is the "
                "arithmetic midpoint of that range, not a separate claim."
            ),
            "note": (
                "Attributed to Walker Deibel on Jake & Gino (xpFa8hcRy_k at 00:17:02), Walker "
                "Deibel on roll-ups (fFDPLnXTi0o) and HBS Rock Center for Entrepreneurship "
                "(oJcm3Bn-lXE at 00:57:40)."
            ),
        },
        {
            "diagram_id": "diag-05-sba-acquisition-gates",
            "chapter_number": 5,
            "title": "Four Gates Under SOP 50 10 8.1",
            "subtitle": "Historical cash flow sets the ceiling on acquisition debt",
            "chart_type": "decision_tree",
            "nodes": [
                {
                    "gate": "G1",
                    "question": (
                        "Do supported historical earnings cover debt service at 1.25x or better?"
                    ),
                    "pass_next": "G2",
                    "fail_action": (
                        "Reprice or walk; $700K claimed that shrinks to $550K against $500K of "
                        "debt service is 1.10x and fails the floor."
                    ),
                },
                {
                    "gate": "G2",
                    "question": (
                        "If the price net of appraised owner-occupied real estate is $3M or more, "
                        "is a lender-commissioned or vendor-reviewed QoE in hand?"
                    ),
                    "pass_next": "G3",
                    "fail_action": (
                        "Order the QoE with the lender as the client; quotes run $5,000 to $30,000."
                    ),
                },
                {
                    "gate": "G3",
                    "question": (
                        "Is the 10% injection seasoned for two full bank statement cycles, with "
                        "any HELOC paired to an outside repayment source?"
                    ),
                    "pass_next": "G4",
                    "fail_action": (
                        "Season the cash first, or pair borrowed money with outside income such "
                        "as a spouse's W-2."
                    ),
                },
                {
                    "gate": "G4",
                    "question": (
                        "Will the seller sign a full-standby note with no principal or interest "
                        "for the life of the loan, covering no more than half the injection?"
                    ),
                    "pass_next": (
                        "Close; on a $1.15M project that is $57,500 of buyer cash plus a $57,500 "
                        "standby note."
                    ),
                    "fail_action": (
                        "Fund the full 10% injection in buyer cash; the old zero-cash structure "
                        "is gone."
                    ),
                },
            ],
            "caption": (
                "Lenders, brokers and CPAs agree the DSCR floor, the $3M QoE trigger, injection "
                "seasoning and seller standby terms now decide whether an SBA deal closes."
            ),
            "assumptions_note": (
                "Gates follow the practitioner examples quoted; how the $3M trigger is measured "
                "and whether a buyer QoE can be reused remain disputed among practitioners."
            ),
            "note": (
                "Attributed to Pioneer Capital Advisory LLC (WF2-6ODNQms at 00:06:24 and "
                "00:32:42), Lion Business Advisors (orHTcAJcuAM at 00:07:05 and 00:15:11), "
                "SBA Ray (9Sl18GknuZE at 00:04:31) and Exit Ready Valuation (Tt3Ae9PDn8A at "
                "00:00:54 and 00:01:15)."
            ),
        },
        {
            "diagram_id": "diag-06-asset-deal-protection-architecture",
            "chapter_number": 11,
            "title": "Asset Deal Buyer Protection Architecture",
            "subtitle": "Indemnity, set-off, escrow and allocation around the buyer entity",
            "chart_type": "org_architecture",
            "center": {
                "role": "Buyer Entity (Asset Purchaser)",
                "headcount": "1 acquiring entity, formed to sign the NDAs and LOI, assigned to NewCo at close",
                "focus": (
                    "Buy assets for liability protection and a stepped-up basis; almost all Main "
                    "Street and lower middle market deals close as asset sales."
                ),
            },
            "spokes": [
                {
                    "role": "Selling Shareholders",
                    "type": "Personal indemnitors",
                    "kpi": (
                        "Every selling shareholder signs; indemnity cap 10-15%, deductible "
                        "0.5-1%, survival 12-18 months the norm."
                    ),
                },
                {
                    "role": "Seller Note",
                    "type": "Set-off source",
                    "kpi": (
                        "Sized at 10-15% to match the indemnity cap; never used to set off a "
                        "working-capital adjustment."
                    ),
                },
                {
                    "role": "Escrow or Holdback",
                    "type": "Held-back purchase price",
                    "kpi": (
                        "89% of lower middle market deals carry an escrow, median 10%; SMB "
                        "escrows likely under 5%."
                    ),
                },
                {
                    "role": "Form 8594 Allocation",
                    "type": "Matching tax filing",
                    "kpi": (
                        "A $1M intangible amortizes over 15 years; buyer and seller returns "
                        "must match."
                    ),
                },
            ],
            "caption": (
                "Sellers want stock for capital-gains treatment, buyers want assets, and SMB "
                "buyer protection runs on personal indemnity, set-off, escrow and a matched "
                "allocation."
            ),
            "assumptions_note": (
                "Market terms are SMB Law Group's report across roughly 130+ deals and the "
                "Aquiem study; practitioners disagree on whether reps carry value without a "
                "note to offset."
            ),
            "note": (
                "Attributed to SMB Law Group LLP (iNOj__jXGpE at 00:11:52, 00:26:54 and "
                "00:43:34), Walker Deibel (NM-ZwBNBHQE at 00:02:06), Tax Hack Accounting Group "
                "(Wd1__Z4Nz6k at 00:02:32) and Teach Me! Personal Finance (G0f0r8tYMnk at "
                "00:05:35)."
            ),
        },
        {
            "diagram_id": "diag-07-sourcing-workload-benchmarks",
            "chapter_number": 4,
            "title": "Sourcing Workload Benchmarks",
            "subtitle": "What a consistent on- and off-market deal funnel looks like",
            "chart_type": "stacked_comparison",
            "total_range": "10-20 minutes a day feeding 50-100 reviewed deals and 30-50 NDAs",
            "buckets": [
                {
                    "label": "Deals Reviewed",
                    "low": 50,
                    "high": 100,
                    "notes": "Codie Sanchez's review target across listings and off-market targets.",
                },
                {
                    "label": "NDAs Signed",
                    "low": 30,
                    "high": 50,
                    "notes": "LOIs go out on about 20%; reject anything under a 15% margin first.",
                },
                {
                    "label": "Qualified Seller Meetings per Month",
                    "low": 5,
                    "high": 10,
                    "notes": (
                        "CGS Partners search fund, Illinois and Indiana specialty distribution "
                        "and HVAC, via calls, LinkedIn and email."
                    ),
                },
                {
                    "label": "Daily Minutes on the Funnel",
                    "low": 10,
                    "high": 20,
                    "notes": "Worked consistently rather than in bursts.",
                },
            ],
            "caption": (
                "Practitioner benchmarks for the reviewing, NDA and meeting volume behind a "
                "sourcing engine that reaches owners before anyone else does."
            ),
            "assumptions_note": (
                "Buckets carry different units (deals, NDAs, meetings per month, minutes per "
                "day) and are compared side by side, not summed."
            ),
            "note": (
                "Attributed to Codie Sanchez (3mtS8rOAqoM at 00:42:09 and 01:13:51) and Marco "
                "Palmero (iPMw4FjbyRQ at 00:02:48)."
            ),
        },
        {
            "diagram_id": "diag-08-first-30-days-controls",
            "chapter_number": 12,
            "title": "The First Four Weeks After Close",
            "subtitle": "Stabilize cash, people and controls before accelerating",
            "chart_type": "timeline_roadmap",
            "weeks": [
                {
                    "week": "Week 1",
                    "title": "Employees First, Then Customers",
                    "deliverable": (
                        "Last bank reconciliation for every account, the age of the oldest "
                        "suspense item, and what the local controller would fix first."
                    ),
                    "gate": "Employees told before customers, and no market blackout.",
                },
                {
                    "week": "Week 2",
                    "title": "13-Week Cash Forecast Live",
                    "deliverable": (
                        "Forecast updated weekly against actuals with every gap explained in writing."
                    ),
                    "gate": "Red flag at a gap above 10% for two consecutive weeks.",
                },
                {
                    "week": "Week 3",
                    "title": "Dual Signatures by Day 15",
                    "deliverable": (
                        "Every bank account on dual signatures; the person who approves a payment "
                        "never sends it."
                    ),
                    "gate": (
                        "Lead flow watched; going dark cut it 40% within 3 weeks in the Jen case."
                    ),
                },
                {
                    "week": "Week 4",
                    "title": "Tribal Knowledge and Access Control",
                    "deliverable": (
                        "Recorded 1 to 2 hour staff sessions converted into SOPs and FAQs; every "
                        "temporary access given an owner, scope, expiry and removal action."
                    ),
                    "gate": "Day 30 Control Memo in hand before any acceleration.",
                },
            ],
            "caption": (
                "Operators converge on one rule for the first 100 days: do not break the "
                "business, and prove cash visibility and controls in the first month."
            ),
            "assumptions_note": (
                "Week placement follows the testified deadlines (forecast within 2 weeks, dual "
                "signatures by Day 15, Day 30 Control Memo); practitioners split on how fast "
                "hard decisions should follow."
            ),
            "note": (
                "Attributed to Lighthouse Capital (OwAOc9xgv9U at 00:00:51 and 00:01:07), Neo "
                "Expertise (4kQ8R30J5q4 at 00:02:14), Strategy Leaders Inc. (OeJwN9bz5dE at "
                "00:12:31), Patrick O'Connell - M&A Transaction Services (6AT45jrM2CU at "
                "00:23:24) and Bridgeyard (wjVsYwI5G_E at 00:01:58)."
            ),
        },
    ]


VOLUME_027_POSITIONING_ALTERNATIVES: list[dict] = [
    {
        "title": "Buy the Cash Flow",
        "subtitle": (
            "Why practitioners pay 2.5-4.5x for a running business instead of building one "
            "from zero"
        ),
        "audience": (
            "Career switchers, MBA students and first-time buyers weighing a startup against "
            "an acquisition"
        ),
        "research_basis": (
            "Q1-Q3 testimony: 98% acquisition-entrepreneur success versus about 10% for "
            "startups, a 2% SBA default rate versus 20% first-year startup failure, and "
            "small-firm multiples at a half to a third of private equity."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=c1OtHjDpymM&t=457s",
            "https://www.youtube.com/watch?v=xpFa8hcRy_k&t=293s",
            "https://www.youtube.com/watch?v=YXFpxJrIjD0&t=513s",
            "https://www.youtube.com/watch?v=oJcm3Bn-lXE&t=3460s",
            "https://www.youtube.com/watch?v=_exEOi-Wxuk&t=924s",
        ],
        "validation_status": "Grounded strictly in Vol. 027 YouTube practitioner transcripts.",
    },
    {
        "title": "The Financing Story That Survives Diligence",
        "subtitle": (
            "SBA 7(a), the 1.25x floor, and the 90/5/5 stack with a full-standby seller note"
        ),
        "audience": (
            "Self-funded searchers and SBA borrowers structuring a first Main Street acquisition"
        ),
        "research_basis": (
            "Q5-Q6 testimony: DSCR at 1.25x on historical financials, a mandatory QoE at a $3M "
            "business purchase price, $57,500 of buyer cash on a $1M deal, and seller notes "
            "capped at half the injection on full standby."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=WF2-6ODNQms&t=384s",
            "https://www.youtube.com/watch?v=Tt3Ae9PDn8A&t=54s",
            "https://www.youtube.com/watch?v=I6M8wAaqm5s&t=1338s",
            "https://www.youtube.com/watch?v=7RAyVC1b9Pg&t=87s",
        ],
        "validation_status": "Grounded strictly in Vol. 027 YouTube practitioner transcripts.",
    },
    {
        "title": "Prove It, Peg It, Protect It",
        "subtitle": (
            "Quality of earnings, the working capital peg, and the first 100 days after close"
        ),
        "audience": (
            "Buyers under LOI and new owners moving from diligence into integration"
        ),
        "research_basis": (
            "Q8-Q12 testimony: about half of QoEs come back clean and 20-25% kill the deal, a "
            "$2.3M normalization gap worth $23M at 10x, a $900K peg that cost a seller a net "
            "$100K, escrow terms for SMB deals, and a 13-week cash forecast live within two weeks."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=g_fy5eeJpHE&t=1669s",
            "https://www.youtube.com/watch?v=zQE4R-z6Yww&t=197s",
            "https://www.youtube.com/watch?v=ob7Q-yxAsNs&t=85s",
            "https://www.youtube.com/watch?v=iNOj__jXGpE&t=1614s",
            "https://www.youtube.com/watch?v=OwAOc9xgv9U&t=51s",
            "https://www.youtube.com/watch?v=fFDPLnXTi0o&t=382s",
        ],
        "validation_status": "Grounded strictly in Vol. 027 YouTube practitioner transcripts.",
    },
]
