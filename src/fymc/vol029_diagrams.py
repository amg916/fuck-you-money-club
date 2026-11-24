"""Volume 029 diagrams for Insurance Restoration, built from practitioner testimony."""

from typing import Any, Dict, List

VOLUME_029_SUBTITLE: str = (
    "Remove It Physically, Prove It on the Meter, Price It Line by Line, Collect It Clean: "
    "S500/S520 Field Mechanics, Mitigation Billing, Xactimate Repricing, Roof Supplements, "
    "Adjuster and TPA Negotiation, Plumber Referrals, LSA Launches, AOB Risk, Legal Deductibles "
    "and Storm Crew Margins from the Operators Who Run Them"
)


def build_volume_029_diagrams_data() -> list[dict]:
    diagrams: List[Dict[str, Any]] = [
        {
            "diagram_id": "diag-01-s500-s520-containment-to-closeout",
            "chapter_number": 1,
            "title": "Working to the Standard, From Classification to Closeout",
            "subtitle": "The S500 and S520 field sequence practitioners describe on the job",
            "chart_type": "process_flow",
            "stages": [
                {
                    "step": "01",
                    "label": "Classify Category and Condition",
                    "value": "Step 1",
                    "detail": (
                        "Judge mold jobs by Conditions 1, 2 and 3 rather than visible square footage. "
                        "Water that originates from beyond the trap is category three (TheIICRC)."
                    ),
                },
                {
                    "step": "02",
                    "label": "Seal and Prove Containment",
                    "value": "Step 2",
                    "detail": (
                        "6 mil fire-retardant poly, then hold -5 pascals on a manometer before any "
                        "demolition or air movers start (Balanced Building Biology)."
                    ),
                },
                {
                    "step": "03",
                    "label": "Remove Physically Under HEPA",
                    "value": "Step 3",
                    "detail": (
                        "Physical removal, never fogging or bleach, which is essentially a masking agent. "
                        "HEPA captures 99.97% at 0.3 microns and runs about $153 per filter "
                        "(Phill McGurk, Balanced Building Biology, APPALeadership)."
                    ),
                },
                {
                    "step": "04",
                    "label": "Extract, Then Set Air Movers",
                    "value": "Step 4",
                    "detail": (
                        "Pull water off the top and from underneath before drying mats go down. "
                        "Darren Floyd's worked example puts 12 to 16 air movers on a 750 sq ft loss, "
                        "and negative air is never drawn from a crawlspace "
                        "(Restoration Technical Institute, APPALeadership)."
                    ),
                },
                {
                    "step": "05",
                    "label": "Close on Same-Meter Readings",
                    "value": "Step 5",
                    "detail": (
                        "Take moisture readings every 5 ft with the same meter used daily, and close on "
                        "monitored readings, never fan-days (Coach8, Andrew Melrose)."
                    ),
                },
            ],
            "caption": (
                "Containment must hold -5 Pa before work begins, and the file closes only on readings "
                "from the same meter used throughout the project."
            ),
            "assumptions_note": (
                "Step order follows the operator gates stated by Balanced Building Biology and Coach8. "
                "Air mover counts reflect Darren Floyd's 750 sq ft example, not a universal ratio."
            ),
            "note": (
                "Attributed to Balanced Building Biology, Phill McGurk, APPALeadership (Darren Floyd), "
                "Restoration Technical Institute, TheIICRC, Coach8 and Andrew Melrose."
            ),
        },
        {
            "diagram_id": "diag-02-tpa-program-squeeze",
            "chapter_number": 6,
            "title": "The TPA Program Squeeze",
            "subtitle": "How program work narrows a contractor's pricing control",
            "chart_type": "funnel",
            "stages": [
                {
                    "label": "Claims Routed Through TPAs",
                    "value": 80,
                    "display": "Upwards of 80% of claims",
                    "conversion": "Entry point, very few adjusters still work for insurers",
                    "detail": (
                        "The DYOJO host puts the TPA share at upwards of 80% of claims, and Jon Schoen "
                        "says very few adjusters still work directly for carriers."
                    ),
                },
                {
                    "label": "Carriers Bundled per Program",
                    "value": 40,
                    "display": "30 to 40 carriers",
                    "conversion": "Each carrier requires separate approval",
                    "detail": (
                        "Programs such as Contractor Connection bundle 30 to 40 carriers, and the "
                        "contractor must be approved by each one separately."
                    ),
                },
                {
                    "label": "Markup Surrendered at Entry",
                    "value": 20,
                    "display": "20% over the standard list",
                    "conversion": "Preset, discounted list that cannot be changed",
                    "detail": (
                        "Outside programs Jon Schoen marks the standard price list up 20%. Inside a "
                        "program the list is preset and discounted with no markup."
                    ),
                },
                {
                    "label": "Program Fee Charged",
                    "value": 10,
                    "display": "5% to 10% of the work",
                    "conversion": "Fee paid by the contractor to do program work",
                    "detail": (
                        "Schoen reports that TPAs charge the contractor 5 to 10 percent in order to do "
                        "the work, on top of the preset price list."
                    ),
                },
                {
                    "label": "Drying Capped at 3 Days",
                    "value": 3,
                    "display": "3-day drying cap",
                    "conversion": "Cap credited with $20M in claimed savings",
                    "detail": (
                        "Contractor Connection won Nationwide back from Alacrity by capping drying at "
                        "3 days and claiming $20M in savings (Jon Schoen)."
                    ),
                },
            ],
            "caption": (
                "Program work trades chasing for control, yet David Smith says a program can hand over "
                "a $250,000 fire nobody had to chase."
            ),
            "assumptions_note": (
                "Stage values carry mixed units (percent of claims, carrier count, percent of price, "
                "days) and are plotted as reported figures, not conversion rates. The 30 to 40 carrier "
                "range is plotted at its upper bound and the 5 to 10% fee at its upper bound."
            ),
            "note": (
                "Attributed to Water Damage Restoration Coach Jon Schoen and The DYOJO, including "
                "Oregon mitigation owner David Smith. Brian Close counters that guaranteed work is not "
                "always profitable."
            ),
        },
        {
            "diagram_id": "diag-03-mini-split-repricing-gap",
            "chapter_number": 3,
            "title": "The May 2026 Mini-Split Repricing Gap",
            "subtitle": "What an estimate left on the April price list gives up",
            "chart_type": "waterfall",
            "bars": [
                {
                    "label": "Four-Zone Unit, May 2026 Price",
                    "value": 13000,
                    "display": "$13,000",
                    "kind": "total",
                },
                {
                    "label": "Gap Versus April List",
                    "value": 6200,
                    "display": "-$6,200",
                    "kind": "deduction",
                },
                {
                    "label": "Four-Zone Unit, April Price",
                    "value": 6800,
                    "display": "$6,800",
                    "kind": "result",
                },
                {
                    "label": "One-Zone Unit, May 2026 Price",
                    "value": 4200,
                    "display": "$4,200",
                    "kind": "total",
                },
                {
                    "label": "Gap Versus April Price",
                    "value": 2700,
                    "display": "-$2,700",
                    "kind": "deduction",
                },
                {
                    "label": "One-Zone Unit, April Price",
                    "value": 1500,
                    "display": "$1,500",
                    "kind": "result",
                },
            ],
            "caption": (
                "Labor yields cut about 85% kept April mini-split pricing unprofitable. Reprice after "
                "every macro load and every monthly price list update before sending."
            ),
            "assumptions_note": (
                "Gap bars are the arithmetic difference between the April and May 2026 unit prices "
                "reported by Actionable. Two separate unit chains are shown side by side."
            ),
            "note": (
                "Attributed to Actionable for the mini-split prices, Claim Daddy for the repricing gate, "
                "and Overhead And Profit for a separate $2,688.91 repricing gain on an open estimate."
            ),
        },
        {
            "diagram_id": "diag-04-mitigation-billing-floors",
            "chapter_number": 2,
            "title": "Mitigation Billing Floors Per Visit and Per Job",
            "subtitle": "Shane O'Dazier's street numbers for getting paid on water work",
            "chart_type": "horizontal_bars",
            "unit": "USD",
            "bars": [
                {
                    "label": "Initial Response Charge",
                    "min": 285,
                    "max": 285,
                    "typical": 285,
                    "display": "$285 initial response",
                },
                {
                    "label": "Minimum Per Truck Roll",
                    "min": 400,
                    "max": 500,
                    "typical": 400,
                    "display": "At least $400-$500 every time the truck rolls",
                },
                {
                    "label": "Truck Mount Uplift Per Job",
                    "min": 300,
                    "max": 400,
                    "typical": 300,
                    "display": "$300-$400 added by billing $189-$289 per committed hour",
                },
                {
                    "label": "Monitoring Trip Lump Charge",
                    "min": 150,
                    "max": 489,
                    "typical": 489,
                    "display": "$489 per trip vs roughly $150 billed hourly",
                },
                {
                    "label": "Small Cash-Pay Job Floor",
                    "min": 800,
                    "max": 2000,
                    "typical": 2000,
                    "display": "$800-$1,000 in trips before work, so priced at $2,000",
                },
            ],
            "caption": (
                "Change your pricing, never your scope. A $489 assess-and-reposition trip sat on a "
                "$7,300 invoice that was paid in full."
            ),
            "assumptions_note": (
                "Where a range was stated, the typical marker sits on the stated floor or the "
                "practitioner's own chosen price. No midpoints were calculated."
            ),
            "note": (
                "Attributed to Shane O'Dazier of RestorationProfits. ReconSmart Solutions pushes back "
                "that documentation, never a target dollar figure, drives the estimate."
            ),
        },
        {
            "diagram_id": "diag-05-negotiation-table-gates",
            "chapter_number": 5,
            "title": "The Negotiation Table Decision Gates",
            "subtitle": "Questions contractors clear before conceding a dollar to an adjuster",
            "chart_type": "decision_tree",
            "nodes": [
                {
                    "gate": "G1",
                    "question": "Is the adjuster's extra demand a requirement rather than a recommendation?",
                    "pass_next": "Ask what the requirement is based on, then move to G2",
                    "fail_action": (
                        "Decline it plainly, as Chris Zimmerman puts it, I don't need this, and "
                        "therefore I won't be doing it"
                    ),
                },
                {
                    "gate": "G2",
                    "question": "Is the discussion limited to scope and pricing, not coverage?",
                    "pass_next": "Move to G3",
                    "fail_action": (
                        "Stop; coverage negotiation needs a license, and in Texas section 4102.163 "
                        "voids power-of-attorney workarounds (Avner Gat, Daly and Black)"
                    ),
                },
                {
                    "gate": "G3",
                    "question": "Has the carrier estimate been read for squares, tear-off quantities and unit errors?",
                    "pass_next": "Move to G4",
                    "fail_action": (
                        "Rebuild the baseline first; catch errors like 24.48 SF entered for 2,448 SF, "
                        "since a weak estimate creates a weak starting point (claimhelpme)"
                    ),
                },
                {
                    "gate": "G4",
                    "question": "Is the requested reduction 10% or less on a 3 to 4 minute question-list call?",
                    "pass_next": (
                        "Accept and collect; no claim is closed until all repairs are made and paid "
                        "for (Chad Michael)"
                    ),
                    "fail_action": (
                        "Refuse reductions over 10% and collect the undisputed amount "
                        "(Shane O'Dazier)"
                    ),
                },
            ],
            "caption": (
                "Frontline paid about $40,000 against an almost $75,000 bid, so the first carrier "
                "number is a baseline to attack, not accept."
            ),
            "assumptions_note": (
                "Gate order is a sequencing of separate practitioner rules. The 10% ceiling is Shane "
                "O'Dazier's, and the trade-code switch from DMO reached about 40% approval for Chad Michael."
            ),
            "note": (
                "Attributed to Chris Zimmerman, Daly and Black P.C., Avner Gat Inc., claimhelpme, "
                "Builder's Perspective Public Adjusting, Shane O'Dazier and Chad Michael."
            ),
        },
        {
            "diagram_id": "diag-06-deductible-and-claim-check-parties",
            "chapter_number": 11,
            "title": "Who Touches the Deductible and the Claim Check",
            "subtitle": "The parties a contractor coordinates to get paid legally",
            "chart_type": "org_architecture",
            "center": {
                "role": "Restoration or Roofing Contractor",
                "headcount": "Not stated by the speakers",
                "focus": (
                    "Collect the deductible from the homeowner and never bill the carrier a number "
                    "the client was never charged, which Chad Michael calls a felony in every state"
                ),
            },
            "spokes": [
                {
                    "role": "Homeowner",
                    "type": "Deductible payer",
                    "kpi": "2% on a $500,000 dwelling is $10,000, owed on a $12,000 loss or a total loss (Anne Pullen)",
                },
                {
                    "role": "Carrier",
                    "type": "Insurer",
                    "kpi": "Withholds the deductible from the payout; subrogation refunded it in about 6 months (Collision Crash Course)",
                },
                {
                    "role": "Mortgage Loss Draft Department",
                    "type": "Lender",
                    "kpi": "Under $10,000 endorsed with no holdback; over $10,000 goes to inspection (Richard Levisee)",
                },
                {
                    "role": "Assignment Counsel",
                    "type": "Legal",
                    "kpi": "Confirm a true assignment, not a direction to pay, signed by every named insured (Butler Legal)",
                },
            ],
            "caption": (
                "A roofer who waives or eats the deductible is usually inflating the estimate or "
                "cutting roof quality."
            ),
            "assumptions_note": (
                "Legal deductible coverage per Chad Michael means mining ACV-only other-structures "
                "money or subcontracting trades back to the owner. The lender threshold is from one "
                "sample mortgage package."
            ),
            "note": (
                "Attributed to Anne Pullen, Restoration Roofing, Collision Crash Course, Richard Levisee, "
                "Butler Legal, Integrity Roofing and Painting and Chad Michael."
            ),
        },
        {
            "diagram_id": "diag-07-roof-supplement-value-bands",
            "chapter_number": 4,
            "title": "Roof Supplement Value Bands",
            "subtitle": "Reported supplement sizes from advertised average to single-spot O&P",
            "chart_type": "stacked_comparison",
            "total_range": (
                "$2,500 to $7,000 per approved supplement (Roof Sales Mastery), with a single file "
                "lifted about $26,000 (Estimate Mastery)"
            ),
            "buckets": [
                {
                    "label": "Advertised Average Supplement",
                    "low": 2500,
                    "high": 2500,
                    "notes": "Roof Sales Mastery's advertised figure",
                },
                {
                    "label": "Real Average Supplement",
                    "low": 4000,
                    "high": 4500,
                    "notes": "Roof Sales Mastery's figure across contractors trained since 2014",
                },
                {
                    "label": "Top User Average",
                    "low": 5000,
                    "high": 7000,
                    "notes": "Some Roof Sales Mastery users using the 100-plus item master list",
                },
                {
                    "label": "O&P Riding on One Closet Spot",
                    "low": 5400,
                    "high": 5600,
                    "notes": "Chad Michael's $28,000 job where a single interior water spot unlocked O&P",
                },
            ],
            "caption": (
                "Estimate Mastery took a $21,027 RCV file to $47,192 RCV with O&P, while American Roof "
                "Supplements aims for the most accurate, supportable estimate at $150 per supplement."
            ),
            "assumptions_note": (
                "Bands are each practitioner's own reported figures and are not drawn from a common "
                "sample of claims."
            ),
            "note": (
                "Attributed to Roof Sales Mastery, Chad Michael, Estimate Mastery and American Roof "
                "Supplements."
            ),
        },
        {
            "diagram_id": "diag-08-storm-roof-claim-roadmap",
            "chapter_number": 12,
            "title": "Storm Roof Claim Roadmap",
            "subtitle": "From policy read to paid crew, evidence first",
            "chart_type": "timeline_roadmap",
            "weeks": [
                {
                    "week": "Week 1",
                    "title": "Read the Policy Before Promising",
                    "deliverable": (
                        "PPRC confirmed, any 400R ACV roof endorsement flagged, prior roof payments "
                        "found; client emails their own agent on O&L, ACV versus RCV and cosmetic "
                        "exclusions"
                    ),
                    "gate": "No promise made until the policy is read (Adjuster TV, Chad Michael)",
                },
                {
                    "week": "Week 2",
                    "title": "Inspect and Photograph Every Elevation",
                    "deliverable": (
                        "About 30-50 roof photos and 90-120 total, every elevation in the same order; "
                        "test square never on the contractor's square, counting stopped at 10 hits"
                    ),
                    "gate": "Proof that replacement beats repair is in hand (Chris Zimmerman)",
                },
                {
                    "week": "Week 3",
                    "title": "Write and Self-Check the Estimate",
                    "deliverable": (
                        "Macro-built estimate with 10 to 15 percent waste; Haag-based worksheet at "
                        "$24.80 per shingle against $368.78 per square for repair versus replace"
                    ),
                    "gate": (
                        "Print-preview self-check passed and scope sits at $250-$450 per square, "
                        "not $190 (Adjuster TV, Adam Bensman)"
                    ),
                },
                {
                    "week": "Week 4",
                    "title": "Price on Margin and Build",
                    "deliverable": (
                        "Price at cost divided by 0.65, so a $10,000 cost job is $15,384 rather than "
                        "$13,500 at 1.35 markup; 54 percent markup is only 35 percent margin"
                    ),
                    "gate": (
                        "Sub workers comp and GL verified, agreement locked before the first nail, "
                        "never 3 unpaid jobs carried (Digital Roofing Innovations, Roofing Insights)"
                    ),
                },
            ],
            "caption": (
                "The evidence wins the roof, and margin-based pricing keeps the crew profitable once "
                "the claim is approved."
            ),
            "assumptions_note": (
                "Week buckets are a sequencing device; practitioners did not assign calendar durations "
                "to these steps."
            ),
            "note": (
                "Attributed to Adjuster TV (Matt), Chris Zimmerman, Chad Michael, Claim Daddy, "
                "The STRONG Roofer with Adam Bensman, RoofCoach, ProLine, Digital Roofing Innovations "
                "and Roofing Insights."
            ),
        },
    ]
    return diagrams


VOLUME_029_POSITIONING_ALTERNATIVES: List[Dict[str, Any]] = [
    {
        "title": "The Mitigation Profit Playbook",
        "subtitle": (
            "Truck-Roll Floors, Plumber Referral Trees and 70% Margins for Water Damage Owners"
        ),
        "audience": "Water mitigation owners and startup restoration operators",
        "research_basis": (
            "Shane O'Dazier's $400-$500 per truck roll floor and half-day roundup billing worth "
            "$30,000-$40,000 a year, his 4:1 free dry-out guardrail, and Albi's 70%+ emergency "
            "mitigation gross margins."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=72Qh6dRR94U&t=127s",
            "https://www.youtube.com/watch?v=roHp-ZzbYvs&t=469s",
            "https://www.youtube.com/watch?v=D4BavFC6d1E&t=720s",
            "https://www.youtube.com/watch?v=3PlUwHvZkxE&t=192s",
        ],
        "validation_status": "Grounded strictly in Vol. 029 YouTube practitioner transcripts.",
    },
    {
        "title": "Prove It Line by Line",
        "subtitle": (
            "Xactimate Repricing, Click-for-Detail Catches and Roof Supplements That Hold Up"
        ),
        "audience": "Estimators, roofing contractors and in-house supplementers",
        "research_basis": (
            "Estimate Mastery's $21,027 to $47,192 RCV file and $225 window line, Chad Michael's "
            "40%+ supplement increases, Actionable's May 2026 mini-split repricing, and American "
            "Roof Supplements' accuracy-first flat-fee model."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=q6R8Iom5Uz8&t=1144s",
            "https://www.youtube.com/watch?v=bVX2IRINNSM&t=3416s",
            "https://www.youtube.com/watch?v=s4xCprLX1Yw&t=1113s",
            "https://www.youtube.com/watch?v=WNR0K0ubIoI&t=66s",
            "https://www.youtube.com/watch?v=HpoMhPz1KfU&t=623s",
        ],
        "validation_status": "Grounded strictly in Vol. 029 YouTube practitioner transcripts.",
    },
    {
        "title": "By the Book and On the Record",
        "subtitle": (
            "Standard-of-Care Drying, Defensible Documentation and Clean Claim Checks"
        ),
        "audience": "Restoration project managers, technicians and compliance-minded owners",
        "research_basis": (
            "Balanced Building Biology's -5 Pa containment gate, Coach8's same-meter closeout rule, "
            "TheIICRC's warning that skipping the standard loses in front of a jury, Encircle's "
            "written humidity readings, The DYOJO's documentation mandate, and Chad Michael's "
            "line against billing a number the client was never charged."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=YdUmzaa5wO0&t=167s",
            "https://www.youtube.com/watch?v=7gZTdFWoHgs&t=2235s",
            "https://www.youtube.com/watch?v=JOiWfXdUwjM&t=893s",
            "https://www.youtube.com/watch?v=33iGNdZ6fyE&t=7137s",
            "https://www.youtube.com/watch?v=onSDIprTeAU&t=2881s",
            "https://www.youtube.com/watch?v=DmesIP8hcak&t=1932s",
        ],
        "validation_status": "Grounded strictly in Vol. 029 YouTube practitioner transcripts.",
    },
]
