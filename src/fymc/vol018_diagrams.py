"""Volume 018 diagrams: Land Flipping.

Every figure below is an attributed practitioner claim drawn from the
Vol. 018 YouTube practitioner testimony digest (Chapters Q1-Q12).
"""

from typing import Any, Dict, List

VOLUME_018_SUBTITLE: str = (
    "Buy Deep, Scrub Hard, Sell on Terms: Practitioner Playbooks for Priced "
    "Mail and Texting, Per-Acre Comping, Perc and Access Checks, Subdivides "
    "and Double Closes, Seller Financing, and RV and Energy Land Plays"
)


def build_volume_018_diagrams_data() -> List[Dict[str, Any]]:
    """Return the 8 structured diagram dicts for Volume 018."""
    return [
        {
            "diagram_id": "diag-01-land-flip-core-process",
            "chapter_number": 1,
            "chart_type": "process_flow",
            "title": "The Land Flip Acquisition Loop",
            "subtitle": "From liquid county to verified contract in five operator steps",
            "caption": (
                "Land flippers pick counties with real sales velocity, scrub out "
                "unbuildable parcels, price off per-acre comps, lead with texting, "
                "and verify access, septic, and funding before money goes hard."
            ),
            "assumptions_note": (
                "Step order consolidates the workflows described by the cited "
                "practitioners; every threshold shown is an attributed practitioner "
                "claim, not a universal market rule."
            ),
            "note": (
                "Attributed to Thomas | Land Flipping (ZfyoS572Kbk), Landon Bleau via "
                "REtipster (Uaqe67xWZN0), Seth Williams of REtipster, Clayton Hepler "
                "via DealMachine Podcast (HE45qWS8txg), and Ron Apke via Real Estate "
                "Pros Show (Z_ZynszdCFo)."
            ),
            "stages": [
                {
                    "step": "01",
                    "label": "Pick Liquid Counties",
                    "value": "Step 1",
                    "detail": (
                        "Thomas pulls lists only in counties with at least 200 land "
                        "sales a year and fewer active listings than sold listings; "
                        "lists under 1,000 texts get bundled with neighboring counties."
                    ),
                },
                {
                    "step": "02",
                    "label": "Scrub Unbuildable Parcels",
                    "value": "Step 2",
                    "detail": (
                        "Strip the 40% to 50% of parcels carrying wetlands, flood, "
                        "slope, or bad access before any offer is built."
                    ),
                },
                {
                    "step": "03",
                    "label": "Price Off Median Per-Acre Comps",
                    "value": "Step 3",
                    "detail": (
                        "Build offers from median price per acre minus agent, closing, "
                        "and lender costs; Seth Williams teaches buying at 5% to 30% of "
                        "value while Clayton Hepler offers 50% to 55%."
                    ),
                },
                {
                    "step": "04",
                    "label": "Text First, Mail Second",
                    "value": "Step 4",
                    "detail": (
                        "Landon Bleau reports about 9x return on ad spend for texting "
                        "versus about 3x for mail; cutting texts to about 100 characters "
                        "lifted reply rates from 13%-15% to nearly 20%."
                    ),
                },
                {
                    "step": "05",
                    "label": "Verify Access, Septic, and Funding",
                    "value": "Step 5",
                    "detail": (
                        "Confirm legal deeded access, verify soil and septic (Thomas paid "
                        "about $600 per test and now has the buyer verify in inspection), "
                        "line up funding, and amend closing by 30 to 45 days rather than "
                        "let earnest money go hard on an unsold deal."
                    ),
                },
            ],
        },
        {
            "diagram_id": "diag-02-septic-cost-funnel",
            "chapter_number": 6,
            "chart_type": "funnel",
            "title": "What the Soil Decides: Septic Cost Funnel",
            "subtitle": "Upper-bound cost of each system tier down to the perc test that sorts them",
            "caption": (
                "A perc test costing at most $1,500 is the gate that decides whether "
                "a parcel needs a conventional system or an alternative system that can "
                "run to $60,000, which is why practitioners test first and buy second."
            ),
            "assumptions_note": (
                "Each stage value is the upper end of the cost range reported by the "
                "cited practitioners; the display field shows the full reported range. "
                "Stages narrow by reported cost, not by parcel counts."
            ),
            "note": (
                "Attributed to Jack Bosch (nVJMPjUWdZw), Florida Land Facts "
                "(zWTn3NY8wqc), Seth Williams of REtipster (yp6qPMTkjgE), the Apke "
                "Brothers (j3-xqUjgb7k), and Groundwork (dSAQlt9llvM)."
            ),
            "stages": [
                {
                    "label": "Alternative Systems (Mound, ATU, Drip)",
                    "value": 60000,
                    "display": "$15,000-$60,000",
                    "conversion": "Triggered when soil fails a conventional design",
                    "detail": (
                        "Mounds, treatment units, and drip systems run roughly $15,000 "
                        "to $60,000 per land and septic practitioners."
                    ),
                },
                {
                    "label": "Bosch Deal-Killer Tier",
                    "value": 50000,
                    "display": "$30,000-$50,000",
                    "conversion": "Kills a $5,000 lot meant for a $30,000 mobile home",
                    "detail": (
                        "Jack Bosch prices the system the soil demands against the end "
                        "buyer's build budget before committing."
                    ),
                },
                {
                    "label": "Conventional System",
                    "value": 20000,
                    "display": "$5,000-$20,000",
                    "conversion": "Default path when the perc passes",
                    "detail": "Conventional systems run roughly $5,000 to $20,000.",
                },
                {
                    "label": "Florida Conventional Install",
                    "value": 15000,
                    "display": "$10,000-$15,000",
                    "conversion": "Often more than an $8,000 lot",
                    "detail": (
                        "Florida Land Facts cites $3,600 to $12,500 nationally, with "
                        "Florida installs usually landing at $10,000 to $15,000."
                    ),
                },
                {
                    "label": "County Perc Test",
                    "value": 1500,
                    "display": "$150-$1,500",
                    "conversion": "Run inside due diligence, never after closing",
                    "detail": (
                        "Seth Williams reports county health departments typically "
                        "charge $150 to $1,500; the Apke Brothers cap standard diligence "
                        "at 48 hours."
                    ),
                },
            ],
        },
        {
            "diagram_id": "diag-03-texts-per-contract-ladder",
            "chapter_number": 3,
            "chart_type": "waterfall",
            "title": "Texts Per Contract: The Skill Ladder",
            "subtitle": "How reported texting volume per contract falls as operator skill rises",
            "caption": (
                "Reported texts per contract range from 250,000 at the top of Clay "
                "Hepler's logs down to 5,000 for a skilled Apke Brothers texter; each "
                "step down is the gap to the next cited benchmark."
            ),
            "assumptions_note": (
                "Total and result bars are reported benchmarks; each deduction is the "
                "arithmetic gap between two adjacent reported benchmarks, not a "
                "separately reported figure."
            ),
            "note": (
                "Attributed to Clay Hepler, Michael Bull (PMSn1EaZ42Y), and the Apke "
                "Brothers (Ls2lelB6ImM) as summarized in practitioner testimony on "
                "texting acquisition."
            ),
            "bars": [
                {
                    "label": "Hepler Upper Texting Range",
                    "value": 250000,
                    "display": "250,000 texts per contract",
                    "kind": "total",
                },
                {
                    "label": "Bull Unskilled Ceiling",
                    "value": -210000,
                    "display": "-210,000 (down to 40,000 texts)",
                    "kind": "deduction",
                },
                {
                    "label": "Apke Beginner Benchmark",
                    "value": -20000,
                    "display": "-20,000 (down to 20,000 texts)",
                    "kind": "deduction",
                },
                {
                    "label": "Bull Skilled Benchmark",
                    "value": -10000,
                    "display": "-10,000 (down to 10,000 texts)",
                    "kind": "deduction",
                },
                {
                    "label": "Apke Skilled Texter",
                    "value": -5000,
                    "display": "-5,000 (down to 5,000 texts)",
                    "kind": "deduction",
                },
                {
                    "label": "Skilled Texts Per Contract",
                    "value": 5000,
                    "display": "5,000 texts per contract",
                    "kind": "result",
                },
            ],
        },
        {
            "diagram_id": "diag-04-mail-roas-bands",
            "chapter_number": 2,
            "chart_type": "horizontal_bars",
            "title": "Direct Mail Return on Ad Spend Bands",
            "subtitle": "Reported ROAS ranges for land mail campaigns and blended benchmarks",
            "caption": (
                "Blind-offer mail ranges from 8x to 10x for new members to about 23x "
                "for a standout campaign, while Landon Bleau's mail runs about 3x "
                "against his texting."
            ),
            "assumptions_note": (
                "Min and max are the reported band edges; where a range was reported, "
                "the typical value marks the band midpoint rather than a separately "
                "reported figure. Single-point claims use the same value for all three."
            ),
            "note": (
                "Attributed to Sumner Healey (R4icAmTE4WI), Landon Bleau via REtipster "
                "(Uaqe67xWZN0), and Clayton Hepler via DealMachine Podcast "
                "(HE45qWS8txg)."
            ),
            "unit": "x return on ad spend",
            "bars": [
                {
                    "label": "Landon Bleau Mail",
                    "min": 3,
                    "max": 3,
                    "typical": 3,
                    "display": "About 3x",
                },
                {
                    "label": "Hepler Blended Benchmark",
                    "min": 5,
                    "max": 10,
                    "typical": 7.5,
                    "display": "5x-10x",
                },
                {
                    "label": "Healey New Members",
                    "min": 8,
                    "max": 10,
                    "typical": 9,
                    "display": "8x-10x",
                },
                {
                    "label": "Healey Seasoned Members",
                    "min": 10,
                    "max": 20,
                    "typical": 15,
                    "display": "10x-20x",
                },
                {
                    "label": "Anthony Blind-Offer Campaign",
                    "min": 23,
                    "max": 23,
                    "typical": 23,
                    "display": "About 23x (14,000 letters, over $200K netted)",
                },
            ],
        },
        {
            "diagram_id": "diag-05-comping-gates",
            "chapter_number": 5,
            "chart_type": "decision_tree",
            "title": "Four Gates Before a Land Offer",
            "subtitle": "Sold comps, site layers, disclosure status, and the max-buy cap",
            "caption": (
                "Operators value vacant land off sold, land-only comps, pull wetland and "
                "flood layers, haircut list prices in non-disclosure states, and walk "
                "when the number will not clear the cap."
            ),
            "assumptions_note": (
                "Gate order consolidates the comping practices of the cited "
                "practitioners; discount bands and caps are their reported rules of "
                "thumb, not appraisal standards."
            ),
            "note": (
                "Attributed to Seth Williams of REtipster (rYCHQ59jzhY), Alex Reese of "
                "Acrewell Land Company (TbH_4hSsYHU), Sumner Advanced (8pB5HoHJ4Bk), "
                "Cool Wholesaling (3x8J7AdyCEw), Brent Bowers, and the Apke Brothers "
                "(bIqgihxHoo8)."
            ),
            "nodes": [
                {
                    "gate": "G1",
                    "question": (
                        "Are the comps sold, land-only, in a tight size band, and inside "
                        "a six-to-twelve-month window?"
                    ),
                    "pass_next": "G2",
                    "fail_action": (
                        "Drop actives and outliers that do not line up with the sold "
                        "list before averaging per-acre values."
                    ),
                },
                {
                    "gate": "G2",
                    "question": "Have wetlands, flood zone, and soil layers been pulled?",
                    "pass_next": "G3",
                    "fail_action": (
                        "Pull them first; a lot about 40 percent wet sold at $20,000 "
                        "after an $85,000 ask."
                    ),
                },
                {
                    "gate": "G3",
                    "question": "Is the sold price disclosed in this state?",
                    "pass_next": "G4",
                    "fail_action": (
                        "Haircut last list price by days on market (0-15% at 1-90 days, "
                        "20-30% at 3-6 months, 35-50% at 6-12 months), drop listings "
                        "older than a year, and check land.com sold listings."
                    ),
                },
                {
                    "gate": "G4",
                    "question": (
                        "Does the offer clear the max-buy cap (e.g. $35,000 max on 8 "
                        "Fairmont acres worth $40,000 retail)?"
                    ),
                    "pass_next": "Send the offer",
                    "fail_action": (
                        "Walk away; on subdivides, call the county on minimum lot rules "
                        "before modeling any split."
                    ),
                },
            ],
        },
        {
            "diagram_id": "diag-06-terms-seller-architecture",
            "chapter_number": 11,
            "chart_type": "org_architecture",
            "title": "The Terms-Sale Land Operation",
            "subtitle": "Buyers as the asset, notes as the cash engine",
            "caption": (
                "Abhi runs roughly 80% of sales on terms, so buyer acquisition, payoff "
                "nudges, compliance, and listing media orbit the note book rather than "
                "a one-time cash sale."
            ),
            "assumptions_note": (
                "Spoke roles group practices reported by the cited practitioners; team "
                "headcount was not reported in testimony."
            ),
            "note": (
                "Attributed to Abhi of Gokce Capital via REtipster (HpkNhY7WclQ), Seth "
                "Williams of REtipster (m1GoTr9J5TM), William Bronchick (ZGvGq-_10yA), "
                "and Wyman Gentry (ItWPpkhNHto)."
            ),
            "center": {
                "role": "Terms-Sale Land Operator (Abhi, Gokce Capital)",
                "headcount": "Not reported in testimony",
                "focus": (
                    "80% terms / 20% cash across nearly 800 land deals since 2018; buy "
                    "around $10K, sell around $20K with 10% down and about $500 a month."
                ),
            },
            "spokes": [
                {
                    "role": "Buyer Acquisition",
                    "type": "Marketing",
                    "kpi": "Cost per lead up from about $5 to $800-$1,200",
                },
                {
                    "role": "Early-Payoff Cashback",
                    "type": "In-house team",
                    "kpi": (
                        "5% back within 6 months, 2.5% within 12; about 10% of borrowers "
                        "take it; reminders in months 4-5 and 9-11"
                    ),
                },
                {
                    "role": "Seller-Finance Compliance",
                    "type": "Advisory",
                    "kpi": (
                        "Owner-occupant deals counted per person against RMLO thresholds "
                        "(Texas 5, Colorado 3, California 0); no-build-before-payoff clause"
                    ),
                },
                {
                    "role": "Drone Listing Media",
                    "type": "Contractor",
                    "kpi": "$125 for 5 photos, $225 for 10; Part 107 certified",
                },
            ],
        },
        {
            "diagram_id": "diag-07-list-size-by-pull",
            "chapter_number": 4,
            "chart_type": "stacked_comparison",
            "title": "How Filter Stacking Shrinks a Land List",
            "subtitle": "Reported record counts from raw county pull to tagged small-town export",
            "caption": (
                "Stacking public-record filters cut 82,328 Lehigh Acres lots to 1,250, "
                "while priced and tagged exports land in the hundreds or dozens before "
                "a dollar goes to mail."
            ),
            "assumptions_note": (
                "Each bucket is a separate reported pull from a different operator and "
                "market; buckets are compared side by side, not summed."
            ),
            "note": (
                "Attributed to PropStream testimony on Lehigh Acres, Max Edson of PRYCD "
                "(7jGQIvwqBwc), and Seth Williams of REtipster (oJpqcR4iFy8)."
            ),
            "total_range": "20 to 82,328 records per pull",
            "buckets": [
                {
                    "label": "Lehigh Acres Raw Lots",
                    "low": 82328,
                    "high": 82328,
                    "notes": "Unfiltered lot count before the PropStream filter stack.",
                },
                {
                    "label": "Lehigh Acres After Filter Stack",
                    "low": 1250,
                    "high": 1250,
                    "notes": (
                        "Raw land isolated by setting improvement value to zero plus "
                        "stacked owner filters."
                    ),
                },
                {
                    "label": "PRYCD Priced List",
                    "low": 300,
                    "high": 300,
                    "notes": "300 records for $24 with offer price at a 25% default slider.",
                },
                {
                    "label": "Small-Town Tagged Export",
                    "low": 20,
                    "high": 40,
                    "notes": "Apply tags, switch to Less Map, and export about 20 to 40 properties.",
                },
            ],
        },
        {
            "diagram_id": "diag-08-alt-use-roadmap",
            "chapter_number": 12,
            "chart_type": "timeline_roadmap",
            "title": "Repositioning Land Into RV and Energy Uses",
            "subtitle": "Zoning, layout, lease terms, and cap-rate underwriting in sequence",
            "caption": (
                "Operators clear zoning first, model site conversion, underwrite only "
                "lease payments on energy deals, and buy RV parks at high caps they can "
                "push lower with occupancy."
            ),
            "assumptions_note": (
                "Week labels sequence the reported operator gates for planning only; no "
                "practitioner reported a four-week timeline."
            ),
            "note": (
                "Attributed to Heather Blankenship (FY9TF9ZkLwk), The Owner's Math "
                "(xjNh4eemKCs), Dan of LandApp by LandGate (Uaymin1wo40), and Dr. Jeff "
                "Anzalone (tZwHEMuaXiQ, 5o06VeN0Gak)."
            ),
            "weeks": [
                {
                    "week": "Week 1",
                    "title": "Clear Zoning and Permitting",
                    "deliverable": "Written zoning and permit path for the intended use",
                    "gate": (
                        "No build until cleared; one Blankenship student was shut down "
                        "for 6-plus months on glamping units."
                    ),
                },
                {
                    "week": "Week 2",
                    "title": "Model Site Conversion",
                    "deliverable": "Layout showing usable share of the parcel",
                    "gate": (
                        "55 to 65% usable on a good layout versus 40% on a poor one; the "
                        "same 5-acre build swings from about 12% to about 1% cash-on-cash."
                    ),
                },
                {
                    "week": "Week 3",
                    "title": "Underwrite the Energy Lease",
                    "deliverable": "Lease model on payments only, matched to optioned acreage",
                    "gate": (
                        "Solar at $300-$2,000 per acre per year with a 2% escalator after "
                        "a 4-5 year option; storage sites bought at $30,000 per acre."
                    ),
                },
                {
                    "week": "Week 4",
                    "title": "Underwrite the RV Park Cap Rate",
                    "deliverable": "Entry cap and occupancy demand plan",
                    "gate": (
                        "Buy at 9-11+ caps versus 3-4 on apartments; Anzalone lifted a "
                        "200-site park from 50% to 90% by targeting a nearby employer."
                    ),
                },
            ],
        },
    ]


VOLUME_018_POSITIONING_ALTERNATIVES: List[Dict[str, Any]] = [
    {
        "title": "The Land Deal Machine",
        "subtitle": "Priced Mail, Short Texts, and the Unit Economics Behind Every Vacant-Land Contract",
        "audience": (
            "Operators building outbound acquisition for vacant land who want "
            "per-deal mail, texting, and return-on-ad-spend benchmarks."
        ),
        "research_basis": (
            "Apke Brothers model 1 deal per 2,500 mailers at about $1,500 marketing "
            "and $18,500 net; Sumner Healey reports 8x-23x ROAS; Landon Bleau reports "
            "about 9x texting versus 3x mail; Michael Bull benchmarks about 10,000 texts "
            "per contract if skilled; Clayton Hepler cites about $25K average profit."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=U4C3AVYK9M4&t=63s",
            "https://www.youtube.com/watch?v=R4icAmTE4WI&t=289s",
            "https://www.youtube.com/watch?v=Uaqe67xWZN0&t=2335s",
            "https://www.youtube.com/watch?v=PMSn1EaZ42Y&t=361s",
            "https://www.youtube.com/watch?v=HE45qWS8txg&t=578s",
        ],
        "validation_status": "Grounded strictly in Vol. 018 YouTube practitioner transcripts.",
    },
    {
        "title": "Manufactured Margin",
        "subtitle": "Subdivides, Paper Splits, and Unlocking Landlocked Acreage",
        "audience": (
            "Land investors moving past discount buying toward splitting acreage and "
            "fixing access to create value."
        ),
        "research_basis": (
            "Clay Hepler netted $235K on 80 Minnesota acres in under six months; Jon "
            "Jasniak turned 79 Texas acres into $818K of seller-financed notes; Jack "
            "Bosch cuts landlocked value at least in half and cites a $500 neighbor "
            "easement; the Apke Brothers would pay 70-80% of retail for frontage and "
            "sold 4 of 7 Tate County parcels at about $62,000 average."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=o_c7zC-iYqE&t=95s",
            "https://www.youtube.com/watch?v=N5LpbcKdDVE&t=259s",
            "https://www.youtube.com/watch?v=tfERI-RnheU&t=347s",
            "https://www.youtube.com/watch?v=5p6zCt25Tyw&t=68s",
            "https://www.youtube.com/watch?v=bIqgihxHoo8&t=367s",
        ],
        "validation_status": "Grounded strictly in Vol. 018 YouTube practitioner transcripts.",
    },
    {
        "title": "Land That Pays Monthly",
        "subtitle": "Seller-Financed Notes, Solar and Storage Leases, and RV Park Cap-Rate Plays",
        "audience": (
            "Land owners and flippers seeking recurring income from terms sales, "
            "energy leases, and RV hospitality."
        ),
        "research_basis": (
            "Abhi sells about 80% on terms with 5% and 2.5% early-payoff cashbacks; "
            "Seth Williams and William Bronchick map seller-finance compliance on vacant "
            "land; LandGate's Dan prices solar at $300-$2,000 per acre per year and "
            "storage sites at $30,000 per acre; The Owner's Math shows a 12% versus 1% "
            "RV storage swing; Dr. Jeff Anzalone buys RV parks at 9-11+ caps."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=HpkNhY7WclQ&t=579s",
            "https://www.youtube.com/watch?v=HpkNhY7WclQ&t=677s",
            "https://www.youtube.com/watch?v=m1GoTr9J5TM&t=1056s",
            "https://www.youtube.com/watch?v=ZGvGq-_10yA&t=505s",
            "https://www.youtube.com/watch?v=Uaymin1wo40&t=213s",
            "https://www.youtube.com/watch?v=xjNh4eemKCs&t=1093s",
            "https://www.youtube.com/watch?v=tZwHEMuaXiQ&t=185s",
        ],
        "validation_status": "Grounded strictly in Vol. 018 YouTube practitioner transcripts.",
    },
]
