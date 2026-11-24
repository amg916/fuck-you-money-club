"""Volume 013 diagrams for Intellectual Property Licensing.

Every figure, workflow and attribution below is drawn from named practitioner
testimony collected for Chapters Q1-Q12.
"""

from typing import Any, Dict, List

VOLUME_013_SUBTITLE: str = (
    "Keep Title, Rent the Rights: Perceived Ownership on a $65 Provisional, "
    "5% Royalty Anchors, 20-30 Company Outreach, Half-Projection Minimum "
    "Guarantees, Claim-Charted Portfolios, Audit Clauses and AI-Data Deletion Terms"
)


def build_volume_013_diagrams_data() -> List[Dict[str, Any]]:
    """Return the eight structured diagram dicts for Volume 013."""
    return [
        {
            "diagram_id": "diag-01-licensing-model-fork",
            "chapter_number": 1,
            "chart_type": "process_flow",
            "title": "Make It, Sell It, or License It",
            "subtitle": "The five-step fork practitioners walk before pitching a single licensee",
            "caption": (
                "Licensing wins the consensus for inventors who want the licensee's money, "
                "staff and shelf space; inventRightTV contrasts an instant 20,000-store "
                "footprint with at least $250,000 floated to venture alone."
            ),
            "assumptions_note": (
                "Step order follows the operator gates cited for Chapter Q1. Royalty bands "
                "are attributed claims (2 to 10% of wholesale per Patent Question, 3 to 5% "
                "and up to 10% per Patent pc, 5 to 20% per UpCounsel) and vary by industry."
            ),
            "note": (
                "Attributed to The Sourcing Gals, Patent Question, inventRightTV, UpCounsel, "
                "Patent pc, Licensing Consulting Group, Kauffman FoundersSchool and "
                "Michigan Engineering."
            ),
            "stages": [
                {
                    "step": "01",
                    "label": "Lock a protectable element",
                    "value": "Step 1",
                    "detail": (
                        "The Sourcing Gals refuse further deal conversations until the "
                        "technology is protected."
                    ),
                },
                {
                    "step": "02",
                    "label": "Weigh venturing against licensing",
                    "value": "Step 2",
                    "detail": (
                        "Venturing meant floating at least $250,000 with retailers paying "
                        "in 60 to 90 days (inventRightTV); Patent Question bars manufacturing "
                        "without demand, margins, a sales channel and operating ability."
                    ),
                },
                {
                    "step": "03",
                    "label": "Pitch as a product developer",
                    "value": "Step 3",
                    "detail": (
                        "Polished brochures, formal letters and prototypes; brokers paid on "
                        "commission only and vetted through the United Inventors Association "
                        "and Better Business Bureau (UpCounsel)."
                    ),
                },
                {
                    "step": "04",
                    "label": "Choose exclusivity and markets",
                    "value": "Step 4",
                    "detail": (
                        "Pick an exclusive partner carefully or demand non-exclusive where "
                        "you hold market power (Patent pc); license human and pet markets at "
                        "once (Licensing Consulting Group)."
                    ),
                },
                {
                    "step": "05",
                    "label": "Set minimums, then price",
                    "value": "Step 5",
                    "detail": (
                        "No license without annual minimums (Michigan Engineering); price "
                        "comes last and is capped by the licensee's next best alternative "
                        "(Kauffman FoundersSchool)."
                    ),
                },
            ],
        },
        {
            "diagram_id": "diag-02-tech-transfer-odds-funnel",
            "chapter_number": 6,
            "chart_type": "funnel",
            "title": "University Tech Transfer Odds Narrow Fast",
            "subtitle": "From office economics to the rare million-dollar invention",
            "caption": (
                "Nelsen calls tech transfer a lottery where only a dozen US offices make "
                "money at any time; Salk's director says two or three inventions drive "
                "80-90% of revenue."
            ),
            "assumptions_note": (
                "Each stage is a separately reported percentage with its own population "
                "(offices, research dollars, or disclosed inventions). Stages are ordered "
                "by size to show narrowing odds, not as one cohort passing through."
            ),
            "note": (
                "Attributed to Columbia TechVentures (Herschwitz), the MIT Technology "
                "Licensing Office (Millar-Nicholson) and OSU Center for Clinical and "
                "Translational Science."
            ),
            "stages": [
                {
                    "label": "Offices losing money gross",
                    "value": 84,
                    "display": "84% of US university offices",
                    "conversion": "Starting odds for a typical office",
                    "detail": (
                        "Herschwitz's figure, contrasted with Columbia sitting in the top "
                        "2-3 earners for 20 years."
                    ),
                },
                {
                    "label": "Offices covering operating costs",
                    "value": 14,
                    "display": "14% of US offices",
                    "conversion": "Few offices break even on operations",
                    "detail": "Offices like the MIT TLO rarely cover their costs.",
                },
                {
                    "label": "Licensing return per research $1",
                    "value": 4,
                    "display": "4 cents per $1 of research funding",
                    "conversion": "$58B revenue across AUTM surveys, 1991 to 2022",
                    "detail": (
                        "Millar-Nicholson's math on 30 years of AUTM survey results "
                        "against university research funding."
                    ),
                },
                {
                    "label": "Stanford disclosures reaching $1M",
                    "value": 0.8,
                    "display": "0.8% of disclosed inventions",
                    "conversion": "Best-in-class benchmark",
                    "detail": "Success defined as at least $1M in cumulative revenue.",
                },
                {
                    "label": "Ohio State disclosures reaching $1M",
                    "value": 0.1,
                    "display": "0.1% of all inventions ever disclosed",
                    "conversion": "The home-run tail",
                    "detail": (
                        "Provisionals go in before publication at $1,200-$1,500; "
                        "non-provisionals cost $15-30K."
                    ),
                },
            ],
        },
        {
            "diagram_id": "diag-03-royalty-rate-ladder",
            "chapter_number": 3,
            "chart_type": "waterfall",
            "title": "How an Inventor Royalty Rate Steps Down",
            "subtitle": "From Disney-level brand rates to the high-volume consumable floor",
            "caption": (
                "Stephen Key and Andrew Krauss see about 5% most often, seven or eight when "
                "CAD, testing or tooling is done, over 10% only for Disney-level brands, and "
                "toward three for high-volume consumables."
            ),
            "assumptions_note": (
                "Over 10% is plotted at 10 and seven-or-eight at 8; step sizes are the "
                "differences between the rates Key and Krauss reported. UpCounsel's 3 to 6% "
                "of gross sales sits inside the same band."
            ),
            "note": (
                "Attributed to inventRightTV (Stephen Key and Andrew Krauss), with the 3 to "
                "6% band from UpCounsel."
            ),
            "bars": [
                {
                    "label": "Disney-level brand rate",
                    "value": 10,
                    "display": "Over 10%",
                    "kind": "total",
                },
                {
                    "label": "No Disney-level brand pull",
                    "value": -2,
                    "display": "Down to 7-8%",
                    "kind": "deduction",
                },
                {
                    "label": "No CAD, testing or tooling",
                    "value": -3,
                    "display": "Down to about 5%",
                    "kind": "deduction",
                },
                {
                    "label": "Most common average rate",
                    "value": 5,
                    "display": "About 5%",
                    "kind": "result",
                },
                {
                    "label": "High-volume consumable",
                    "value": -2,
                    "display": "Drops toward 3%",
                    "kind": "deduction",
                },
                {
                    "label": "Consumable floor",
                    "value": 3,
                    "display": "About 3%",
                    "kind": "result",
                },
            ],
        },
        {
            "diagram_id": "diag-04-protection-cost-stack",
            "chapter_number": 2,
            "chart_type": "horizontal_bars",
            "title": "What Protection Costs Before Licensing",
            "subtitle": "From a $65 provisional to full attorney-drafted applications",
            "unit": "USD",
            "caption": (
                "inventRightTV reports 99% of its students over 15 years licensed without a "
                "patent, buying perceived ownership with a $65 micro entity provisional and "
                "pushing the licensee to fund the non-provisional."
            ),
            "assumptions_note": (
                "Single quoted fees are plotted with min, max and typical equal. For the "
                "nonprovisional and attorney ranges no typical figure was given, so the "
                "typical marker sits at the low end of the quoted range."
            ),
            "note": (
                "Attributed to USPTOvideo for the fee tiers and attorney range, and "
                "inventRightTV for the $65 micro entity rate (income under $150k a year)."
            ),
            "bars": [
                {
                    "label": "Provisional fee, micro entity",
                    "min": 65,
                    "max": 65,
                    "typical": 65,
                    "display": "$65",
                },
                {
                    "label": "Provisional fee, middle tier",
                    "min": 130,
                    "max": 130,
                    "typical": 130,
                    "display": "$130",
                },
                {
                    "label": "Provisional fee, top tier",
                    "min": 325,
                    "max": 325,
                    "typical": 325,
                    "display": "$325",
                },
                {
                    "label": "Nonprovisional filing fees",
                    "min": 400,
                    "max": 2000,
                    "typical": 400,
                    "display": "$400 to $2,000",
                },
                {
                    "label": "Attorney fees for an application",
                    "min": 6000,
                    "max": 18000,
                    "typical": 6000,
                    "display": "About $6,000 to $18,000",
                },
            ],
        },
        {
            "diagram_id": "diag-05-license-clause-gates",
            "chapter_number": 5,
            "chart_type": "decision_tree",
            "title": "Four Gates Before the Definitive License Closes",
            "subtitle": "Scope, performance, indexation and reversion checks",
            "caption": (
                "Operators lock the commercial skeleton in a short term sheet, then fight "
                "over scope, money and exit triggers; royalties typically land at 3 to 7% "
                "with 5% as the anchor."
            ),
            "assumptions_note": (
                "Term sheets are treated as non-binding except for exclusivity, no-shop and "
                "confidentiality. Industry royalty bands run 0.1 to 25% per UpCounsel, so "
                "the 5% anchor moves with category, leverage and market proof."
            ),
            "note": (
                "Attributed to Ayers Law TV (Andrew M. Ayers), J.D. Houvener of Bold Patents "
                "Law Firm, Bao Tran, BaxterIPAttorneys, a Boardgame Publisher and Licensing "
                "Basics (Ryan Stewart)."
            ),
            "nodes": [
                {
                    "gate": "G1",
                    "question": "Does the grant language state exclusive, sole or non-exclusive?",
                    "pass_next": "G2",
                    "fail_action": (
                        "Rewrite the grant; discovering a non-exclusive license later leaves "
                        "no way to stop a competitor."
                    ),
                },
                {
                    "gate": "G2",
                    "question": "Does every exclusive grant carry a performance clause?",
                    "pass_next": "G3",
                    "fail_action": (
                        "Add an explicit right to terminate on a missed milestone, separate "
                        "from good-faith renegotiation."
                    ),
                },
                {
                    "gate": "G3",
                    "question": "Is every per-unit or foreign-currency royalty indexed?",
                    "pass_next": "G4",
                    "fail_action": (
                        "Provide for proper indexation, since a fixed foreign-currency "
                        "royalty can lose badly."
                    ),
                },
                {
                    "gate": "G4",
                    "question": (
                        "Are reversion triggers written for bankruptcy, ceasing to operate "
                        "and out-of-print status?"
                    ),
                    "pass_next": "Close the definitive license",
                    "fail_action": "Hold the closing until automatic reversion triggers are in.",
                },
            ],
        },
        {
            "diagram_id": "diag-06-sync-catalog-architecture",
            "chapter_number": 11,
            "chart_type": "org_architecture",
            "title": "Who Takes a Cut of a Sync Placement",
            "subtitle": "Routes from a compounding catalog to the buyer",
            "caption": (
                "Michael Elsner models a climb from roughly $2,000 in year one to "
                "$75,000-$100,000 by year five as 20 songs a year multiply into stems, "
                "instrumentals and edits."
            ),
            "assumptions_note": (
                "Cut sizes are practitioner estimates and depend on the route chosen; "
                "operators split on exclusivity and on pitching supervisors directly."
            ),
            "note": (
                "Attributed to Elite Music Coaching (Michael Elsner), Randy McGravey Music, "
                "ClintMusic and Majeston."
            ),
            "center": {
                "role": "Catalog-building composer",
                "headcount": "Solo creator writing 20 songs a year",
                "focus": (
                    "48 kHz, 24-bit WAVs, clean 8- or 16-bar edit points, sting outros, "
                    "no samples, deep metadata"
                ),
            },
            "spokes": [
                {
                    "role": "Licensing agency",
                    "type": "Fee-split agent",
                    "kpi": "Takes 25-50% of the sync fee",
                },
                {
                    "role": "Music library",
                    "type": "Catalog holder",
                    "kpi": (
                        "Most keep the fee and publishing; confirm a composer share of sync "
                        "fees before signing"
                    ),
                },
                {
                    "role": "Major sub-publisher",
                    "type": "Off-the-top distributor",
                    "kpi": "About 25% off the top; $375 each to library and composer on $1,000",
                },
                {
                    "role": "Music supervisor",
                    "type": "Placement buyer",
                    "kpi": "Searches mood tags; one library track drew 57 placements",
                },
            ],
        },
        {
            "diagram_id": "diag-07-pitch-royalty-buckets",
            "chapter_number": 4,
            "chart_type": "stacked_comparison",
            "title": "Royalty Rates Licensees Actually Offer",
            "subtitle": "Where a pitched consumer product lands on wholesale",
            "total_range": "2.5% to 10% of wholesale",
            "caption": (
                "Stephen Key estimates 20 to 30 companies per deal, with success at six to "
                "seven follow-ups spaced every five days; the royalty a pitch lands depends "
                "on the channel and the licensee."
            ),
            "assumptions_note": (
                "Bucket edges are the rates named by Mark Reyland and Andrew Krauss; Reyland "
                "cites the National Royalty Guide average. Single-point figures are plotted "
                "with equal low and high."
            ),
            "note": "Attributed to Mark Reyland and inventRightTV (Andrew Krauss, Stephen Key).",
            "buckets": [
                {
                    "label": "As Seen On TV deals",
                    "low": 2.5,
                    "high": 2.5,
                    "notes": "Reyland puts these deals near 2.5 percent.",
                },
                {
                    "label": "Companies holding firm",
                    "low": 5,
                    "high": 5,
                    "notes": "Krauss says many companies still hold at 5 percent.",
                },
                {
                    "label": "Most deals done",
                    "low": 6,
                    "high": 6,
                    "notes": "Reyland reports most of his deals near 6 percent.",
                },
                {
                    "label": "Guide average to ceiling",
                    "low": 8,
                    "high": 10,
                    "notes": "8 percent National Royalty Guide average; 10 percent ceiling.",
                },
            ],
        },
        {
            "diagram_id": "diag-08-ai-data-license-roadmap",
            "chapter_number": 12,
            "chart_type": "timeline_roadmap",
            "title": "Licensing Operational Records to AI Labs",
            "subtitle": "License copies, never the asset, and name every category",
            "caption": (
                "Jason Varner quotes $100K to $3M-plus payouts for anonymized operational "
                "records, and micro1 reports two to three weeks from owner interest to a "
                "completed license with payout around 60 days out."
            ),
            "assumptions_note": (
                "Week labels sequence the reported steps; the only durations practitioners "
                "gave are 2-3 weeks to completion and payout around 60 days out. Payouts "
                "are driven by exclusivity."
            ),
            "note": (
                "Attributed to Jason Varner, micro1, Archive Trove, OneHourProfessor and "
                "Mayer Brown."
            ),
            "weeks": [
                {
                    "week": "Week 1",
                    "title": "Inventory operational records",
                    "deliverable": (
                        "IT tickets first, since each holds a problem, an action and a fix, "
                        "plus Slack exports"
                    ),
                    "gate": (
                        "Pricing records treated as exposed even after names are removed"
                    ),
                },
                {
                    "week": "Week 2",
                    "title": "Name every category in the contract",
                    "deliverable": (
                        "Records, outputs, embeddings and models named, with exclusivity "
                        "decided against selling to multiple labs"
                    ),
                    "gate": (
                        "Deletion clause reaches labels, caches, backups and checkpoints "
                        "and decides the trained model's fate"
                    ),
                },
                {
                    "week": "Week 3",
                    "title": "Close the license",
                    "deliverable": (
                        "Completed license inside the 2-3 week window micro1 reports"
                    ),
                    "gate": (
                        "Retention, copies and models after termination settled before export"
                    ),
                },
                {
                    "week": "Week 4",
                    "title": "Track payout and model access",
                    "deliverable": "Payout expected around 60 days out",
                    "gate": (
                        "Diligence, regulator access and audit access locked for every "
                        "model version"
                    ),
                },
            ],
        },
    ]


VOLUME_013_POSITIONING_ALTERNATIVES: List[Dict[str, Any]] = [
    {
        "title": "Rent the Rights",
        "subtitle": (
            "Perceived ownership, a 5% royalty anchor and 20-30 company outreach for "
            "inventors who license instead of manufacture"
        ),
        "audience": "Independent inventors and product developers weighing licensing against venturing",
        "research_basis": (
            "inventRightTV's 99% of students licensing without a patent, $65 micro entity "
            "provisionals, the 7/5/1 tiered royalty, Key and Krauss's 5% average, the "
            "$250,000 venturing float, and the 20 to 30 companies a deal can take."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=CS31715RNQk&t=312s",
            "https://www.youtube.com/watch?v=5pNsi_2H-J4&t=278s",
            "https://www.youtube.com/watch?v=IMLF0c7wOQI&t=51s",
            "https://www.youtube.com/watch?v=E5dH32uMqOY&t=305s",
        ],
        "validation_status": "Grounded strictly in Vol. 013 YouTube practitioner transcripts.",
    },
    {
        "title": "Lease the Brand, Keep the Catalog",
        "subtitle": (
            "Half-projection minimum guarantees, 8% to 12% brand royalties and compounding "
            "sync catalogs"
        ),
        "audience": "Brand owners, licensees and creators licensing music, art and knowledge products",
        "research_basis": (
            "Daymond John's 2% to 15% band with 8% to 12% typical, Stu Seltzer's rule of "
            "guaranteeing half the licensee's own projection, Michael Elsner's year-five "
            "$75,000-$100,000 catalog model, and Randy McGravey's 25% sub-publisher cut."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=knoob7eUS6Y&t=634s",
            "https://www.youtube.com/watch?v=qx___lyJ5yQ&t=270s",
            "https://www.youtube.com/watch?v=D6XhETdysBM&t=584s",
            "https://www.youtube.com/watch?v=iF_Z6ikfzMo&t=671s",
        ],
        "validation_status": "Grounded strictly in Vol. 013 YouTube practitioner transcripts.",
    },
    {
        "title": "Make Licensed IP Pay",
        "subtitle": (
            "Claim-charted portfolios, royalty audits that recover 5 to 20 times their cost, "
            "and AI-data deals with deletion clauses that hold"
        ),
        "audience": "IP owners, licensing executives and companies monetizing portfolios, royalty streams and operational records",
        "research_basis": (
            "Funders passing on 19 of every 20 portfolios, up to 89% of audited licensees "
            "underreporting, Julie Tate finding errors about 75% of the time, $100K to "
            "$3M-plus AI-data payouts, and deletion clauses that must reach labels, caches, "
            "backups and checkpoints."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=pyi_x9MFGjs&t=1422s",
            "https://www.youtube.com/watch?v=9Fku-QlhyHc&t=308s",
            "https://www.youtube.com/watch?v=NrMiKZwGTD4&t=2756s",
            "https://www.youtube.com/watch?v=nKuxu_x-s6o&t=104s",
            "https://www.youtube.com/watch?v=y5YpFZxHpYE&t=137s",
        ],
        "validation_status": "Grounded strictly in Vol. 013 YouTube practitioner transcripts.",
    },
]
