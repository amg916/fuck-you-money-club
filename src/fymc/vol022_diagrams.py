"""Volume 022 diagrams: Medical Equipment Resale.

Every workflow, threshold and figure below is drawn from the Vol. 022
practitioner testimony digest (Chapters Q1-Q12) and attributed to the
named speaker or channel.
"""

from typing import Dict, List

VOLUME_022_SUBTITLE: str = (
    "Buy Hospital Surplus, Biomed-Check Every Unit, Resell or Rerent It: "
    "Medicare Rentals, Cross-Border Refurbishing, Third-Party Service, "
    "Bench Safety Testing, QMSR and 510(k) Readiness, Helium-Safe Imaging "
    "Resale, Sterile-Processing Buyers, and Referral-Driven Device Sales"
)


def build_volume_022_diagrams_data() -> List[Dict]:
    """Return the 8 structured diagram dicts for Volume 022."""
    return [
        {
            "diagram_id": "diag-01-surplus-to-resale-engine",
            "chapter_number": 1,
            "chart_type": "process_flow",
            "title": "The Surplus-to-Resale Engine",
            "subtitle": "Buy surplus cheap, verify it, document it, then resell or rerent",
            "caption": (
                "Operators converge on one loop. Centurion moves about 6,000 pieces "
                "a month and turns its entire inventory every 5 weeks, while the "
                "Earn Your Leisure founder rerents returned units on 13-month "
                "Medicare rentals."
            ),
            "assumptions_note": (
                "Step order follows the operator gates and quotes attributed below; "
                "no throughput or margin figures beyond those stated by the speakers "
                "are implied."
            ),
            "note": (
                "Attributed to Centurion Service Group (A TRIMEDX Company), Bill "
                "Whittemore, Jon Sheppard Sells, Used Medical Equipment, and Earn "
                "Your Leisure."
            ),
            "stages": [
                {
                    "step": "01",
                    "label": "Source hospital surplus and trade-ins",
                    "value": "Step 1",
                    "detail": (
                        "Centurion represents well over 1,000 hospitals, surgery "
                        "centers and manufacturers and moves about 6,000 pieces a month."
                    ),
                },
                {
                    "step": "02",
                    "label": "Recheck with a biomed team",
                    "value": "Step 2",
                    "detail": (
                        "Bill Whittemore: never ship on a power-on check alone; "
                        "recheck with biomed or sell it explicitly as is."
                    ),
                },
                {
                    "step": "03",
                    "label": "Write condition limits into the listing",
                    "value": "Step 3",
                    "detail": (
                        "Jon Sheppard Sells: add condition limits and clear pictures "
                        "before the listing goes live, because returns still hit sellers."
                    ),
                },
                {
                    "step": "04",
                    "label": "Display patient-ready inventory",
                    "value": "Step 4",
                    "detail": (
                        "Used Medical Equipment puts biomed certified, patient-ready "
                        "equipment on display so doctors can see what is available."
                    ),
                },
                {
                    "step": "05",
                    "label": "Resell or rerent the unit",
                    "value": "Step 5",
                    "detail": (
                        "Earn Your Leisure bills a 13-month rental for most equipment, "
                        "picks it up when no longer needed, and rerents the same item."
                    ),
                },
            ],
        },
        {
            "diagram_id": "diag-02-pathway-clock-vs-calendar",
            "chapter_number": 6,
            "chart_type": "funnel",
            "title": "Pathway Clock vs. Calendar",
            "subtitle": "FDA review-clock targets against elapsed days in practice",
            "caption": (
                "leanRAQA's pathway table shows the FDA clock understating real "
                "elapsed time on every route, with the 510(k) at a 90-day clock "
                "but about 200 days in practice."
            ),
            "assumptions_note": (
                "Elapsed-day values are approximate figures from the leanRAQA pathway "
                "table; the PMA 180-day clock is cited in the conversion text rather "
                "than plotted as its own stage."
            ),
            "note": (
                "Attributed to leanRAQA, with hold-letter and fee guidance from "
                "Prime Path Medtech and Registrar Corp."
            ),
            "stages": [
                {
                    "label": "PMA elapsed in practice",
                    "value": 800,
                    "display": "~800 days",
                    "conversion": "vs 180-day FDA clock",
                    "detail": "leanRAQA puts PMA at about 800 actual days; only PMA devices are 'approved.'",
                },
                {
                    "label": "De Novo elapsed in practice",
                    "value": 400,
                    "display": "~400 days",
                    "conversion": "vs 120-day FDA clock",
                    "detail": "leanRAQA warns that words like 'novel' push a predicate comparison toward De Novo.",
                },
                {
                    "label": "510(k) elapsed in practice",
                    "value": 200,
                    "display": "~200 days",
                    "conversion": "vs 90-day FDA clock",
                    "detail": "The 510(k) is the dominant route; Registrar Corp quotes a $24,335 standard FY2025 fee.",
                },
                {
                    "label": "De Novo on the FDA clock",
                    "value": 120,
                    "display": "120 days",
                    "conversion": "Clock target; ~400 days actual",
                    "detail": "Lock the exact three-letter product code before filing to avoid an RTA refusal.",
                },
                {
                    "label": "510(k) on the FDA clock",
                    "value": 90,
                    "display": "90 days",
                    "conversion": "Clock target; ~200 days actual",
                    "detail": "Prime Path Medtech: an unpaid user fee triggers a hold letter before review starts.",
                },
            ],
        },
        {
            "diagram_id": "diag-03-dental-service-rate-ladder",
            "chapter_number": 3,
            "chart_type": "waterfall",
            "title": "Dental Service Rate Ladder",
            "subtitle": "Bright Idea Dental Repair rate card, from after-hours call to launch rate",
            "caption": (
                "Jason of Bright Idea Dental Repair launched at $150 an hour, now bills "
                "$175 regular and $225 after hours, plus $75 travel beyond 30 minutes, "
                "invoiced on labor, parts, travel and shipping lines."
            ),
            "assumptions_note": (
                "The opening bar adds the reported $225 after-hours rate and $75 travel "
                "line; step-downs are the differences between reported rates. Parts and "
                "shipping lines are excluded because no figures were given."
            ),
            "note": "Attributed to Jason of Bright Idea Dental Repair on the Better Biomed Channel.",
            "bars": [
                {"label": "After-hours hour plus travel", "value": 300, "display": "$225 + $75 travel", "kind": "total"},
                {"label": "Travel fee beyond 30 minutes", "value": 75, "display": "-$75", "kind": "deduction"},
                {"label": "After-hours premium", "value": 50, "display": "-$50", "kind": "deduction"},
                {"label": "Regular hourly labor rate", "value": 175, "display": "$175/hr", "kind": "result"},
                {"label": "Gap back to launch pricing", "value": 25, "display": "-$25", "kind": "deduction"},
                {"label": "Launch hourly labor rate", "value": 150, "display": "$150/hr", "kind": "result"},
            ],
        },
        {
            "diagram_id": "diag-04-used-vs-oem-parts-pricing",
            "chapter_number": 2,
            "chart_type": "horizontal_bars",
            "title": "Used Gear vs. OEM Pricing",
            "subtitle": "What a hospital biomed paid on eBay against OEM quotes and trade credit",
            "unit": "USD",
            "caption": (
                "Better Biomed Channel documents $200-$300 eBay buys replacing "
                "$1,200-$2,200 OEM parts and repairs, and a camera-head trade-in loop "
                "that saved $10,000-plus."
            ),
            "assumptions_note": (
                "Where the speaker gave a range, the typical marker sits at the range "
                "midpoint; single reported prices use the same value for min, max and typical."
            ),
            "note": "Attributed to the Better Biomed Channel; Storz trade credit as described by the same speaker.",
            "bars": [
                {"label": "Used part bought on eBay", "min": 200, "max": 300, "typical": 250, "display": "$200-$300"},
                {"label": "Used camera-head box on eBay", "min": 800, "max": 800, "typical": 800, "display": "~$800"},
                {"label": "OEM part or repair quote", "min": 1200, "max": 2200, "typical": 1700, "display": "$1,200-$2,200"},
                {"label": "Whole used tower on eBay", "min": 2500, "max": 2500, "typical": 2500, "display": "$2,500"},
                {"label": "Storz trade credit per head", "min": 2500, "max": 2500, "typical": 2500, "display": "$2,500 credit"},
            ],
        },
        {
            "diagram_id": "diag-05-qmsr-inspection-readiness",
            "chapter_number": 5,
            "chart_type": "decision_tree",
            "title": "QMSR Inspection-Readiness Gates",
            "subtitle": "Four checks before the February 2, 2026 hard switch bites",
            "caption": (
                "The QMSR incorporates ISO 13485:2016 by reference, makes risk the "
                "thread investigators pull, and opens management review and audit "
                "records to inspection."
            ),
            "assumptions_note": (
                "Gate sequence reflects the operator gates attributed below; an ISO or "
                "MDSAP certificate does not exempt a firm from any gate."
            ),
            "note": (
                "Attributed to AMORIT EDUCATION, Regulatory Compliance Associates, "
                "Matrix One, Medmarc, and Greenlight Guru."
            ),
            "nodes": [
                {
                    "gate": "G1",
                    "question": "Is the quality system already built on ISO 13485:2016?",
                    "pass_next": "G2",
                    "fail_action": "Re-baseline now; firms complying only with Part 820 face significant change.",
                },
                {
                    "gate": "G2",
                    "question": "Does the risk management file reflect the latest complaint trends?",
                    "pass_next": "G3",
                    "fail_action": "Update it before the visit; Matrix One says the risk file steers the inspection.",
                },
                {
                    "gate": "G3",
                    "question": "Are procedures free of 'do not show to FDA' language and fewer-CAPA objectives?",
                    "pass_next": "G4",
                    "fail_action": "Sweep and rewrite; management review and audit records are now reviewable.",
                },
                {
                    "gate": "G4",
                    "question": "Is every automated label check backed by a statistically significant human sample?",
                    "pass_next": "Ready for a CP 7382.850 inspection",
                    "fail_action": "Add the human sample, as Henry of Greenlight Guru insists.",
                },
            ],
        },
        {
            "diagram_id": "diag-06-sterile-processing-buying-center",
            "chapter_number": 11,
            "chart_type": "org_architecture",
            "title": "Sterile Processing as the Buying Center",
            "subtitle": "Who buys around Central Sterile in ASC, veterinary and dental clinics",
            "caption": (
                "Henry Schein Medical pitches autoclaves, instrument washers, sinks and "
                "cassettes as the room ASC owners overlook, while surgeons cut total knee "
                "trays from five to two."
            ),
            "assumptions_note": (
                "No staffing counts were reported, so headcount is described "
                "qualitatively; spoke KPIs are the figures each practitioner stated."
            ),
            "note": (
                "Attributed to Henry Schein Medical, the American Association of Hip and "
                "Knee Surgeons (Drs. Ballard and Pickering), PEER at TAMU, and Nuronus."
            ),
            "center": {
                "role": "Central Sterile processing",
                "headcount": "Shared processing room serving every surgical team",
                "focus": "Autoclaves, instrument washers, processing sinks, prep-and-pack, cassettes",
            },
            "spokes": [
                {
                    "role": "ASC owner",
                    "type": "Capital buyer",
                    "kpi": "Bundles sterilizers, washers, sinks and cassettes from one vendor",
                },
                {
                    "role": "Orthopedic surgeon",
                    "type": "Cost champion",
                    "kpi": "Knee trays 5 to 2; $750 saved per case vs ~$8,400 Medicare knee",
                },
                {
                    "role": "Veterinary surgical team",
                    "type": "Consumables buyer",
                    "kpi": "Triple-wrapped packs rewashed and resterilized every 6 months",
                },
                {
                    "role": "Dental practice",
                    "type": "Compliance buyer",
                    "kpi": "$4,000-8,000 initial; $500-1,500 per month retainer",
                },
            ],
        },
        {
            "diagram_id": "diag-07-bench-readings-vs-limits",
            "chapter_number": 4,
            "chart_type": "stacked_comparison",
            "title": "Bench Readings vs. Pass Limits",
            "subtitle": "Measured values against thresholds on the electrical safety sequence",
            "total_range": "Measured reading (low) against pass or fail threshold (high), per test",
            "caption": (
                "Prove the analyzer first, then run mains, protective earth, leakage "
                "and insulation in a fixed sequence; Josh Herzka's R Series defib passed "
                "both leakage checks with wide margin."
            ),
            "assumptions_note": (
                "Each bucket carries its own unit as stated in the notes; buckets are "
                "compared within a test, not across tests."
            ),
            "note": (
                "Attributed to Josh Herzka of ReNew Biomedical on the Better Biomed "
                "Channel, and to AbishkarTECH on the Fluke ESA620."
            ),
            "buckets": [
                {
                    "label": "Earth leakage, R Series defib",
                    "low": 129,
                    "high": 500,
                    "notes": "Microamps; 129 measured under normal conditions vs an under-500 limit.",
                },
                {
                    "label": "Applied-part leakage, single fault",
                    "low": 6.5,
                    "high": 50,
                    "notes": "Microamps; 6.5 measured vs a limit of 50.",
                },
                {
                    "label": "Mains check on a no-ground fault",
                    "low": 32,
                    "high": 53,
                    "notes": "Neutral-to-earth 32 and live-to-earth 53 vs an expected figure under five.",
                },
                {
                    "label": "Insulation resistance",
                    "low": 2,
                    "high": 100,
                    "notes": "Megohms; below 2 fails, 1.5 fails, OL over the 100 megohm range is good.",
                },
            ],
        },
        {
            "diagram_id": "diag-08-breaking-into-device-sales",
            "chapter_number": 12,
            "chart_type": "timeline_roadmap",
            "title": "Breaking Into Device Sales",
            "subtitle": "A referral-first sprint from profile cleanup to a capital pipeline",
            "caption": (
                "Valente says almost all roles come from referrals and fewer than 1% of "
                "applicants break in; Licata's capital funnel runs 30 accounts for 1 to "
                "2 purchase orders."
            ),
            "assumptions_note": (
                "The four-week sequencing organizes the practitioners' tactics; the "
                "speakers did not prescribe a calendar."
            ),
            "note": (
                "Attributed to Vincent Valente (Break Into Medical Device Sales), Jacob "
                "(New to Medical Device Sales), Med Sales With Matt, and Joe Licata."
            ),
            "weeks": [
                {
                    "week": "Week 1",
                    "title": "Clean up the profile",
                    "deliverable": "Open to work badge removed and AI dashes stripped from outreach text",
                    "gate": "Hiring managers no longer read desperation into the profile",
                },
                {
                    "week": "Week 2",
                    "title": "Work the referral web",
                    "deliverable": "No-note LinkedIn requests and sub-100-word messages to reps",
                    "gate": "Referral conversations booked, held to a 70/30 listening ratio",
                },
                {
                    "week": "Week 3",
                    "title": "Run the interview gauntlet",
                    "deliverable": "Prepared for 4 to 8 rounds against 200 to 400 applicants per role",
                    "gate": "Interview even if relocating; multiple offers trigger bidding wars",
                },
                {
                    "week": "Week 4",
                    "title": "Map the capital pipeline",
                    "deliverable": "30 accounts targeted for 1 to 2 purchase orders over 1 to 5 years",
                    "gate": "Never inflate pipeline progress reported to managers",
                },
            ],
        },
    ]


VOLUME_022_POSITIONING_ALTERNATIVES: List[Dict] = [
    {
        "title": "Verified, Not Wiped Down",
        "subtitle": "Buying hospital surplus and reselling or rerenting it with biomed proof",
        "audience": "Garage-to-showroom refurbishers, surplus buyers, and DME rental founders",
        "research_basis": (
            "Bill Whittemore's $100M+ over 32 years and warning against power-on-only "
            "shipping; Centurion's 6,000 pieces a month and 5-week inventory turn; Earn "
            "Your Leisure's 13-month Medicare rentals; Better Biomed Channel's eBay buys "
            "against OEM quotes; Block Imaging's HIPAA removal and pre-ship QA demands."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=zLW0PtGvqQE&t=725s",
            "https://www.youtube.com/watch?v=dUZz08G_Dzc&t=36s",
            "https://www.youtube.com/watch?v=hQY0qIkQ-xY&t=506s",
            "https://www.youtube.com/watch?v=sgJKIx288kY&t=938s",
            "https://www.youtube.com/watch?v=xvO7-DA6X2w&t=97s",
        ],
        "validation_status": "Grounded strictly in Vol. 022 YouTube practitioner transcripts.",
    },
    {
        "title": "The Third-Party Equipment Lane",
        "subtitle": "Service shops, remanufactured parts, and helium-safe imaging resale",
        "audience": "Independent biomed servicers and imaging equipment resellers",
        "research_basis": (
            "Jason's Bright Idea Dental Repair rate card and PM memberships; Block "
            "Imaging's $20 to $30 per liter helium on ~2,000-liter magnets; FGI's rule "
            "never to quench a magnet bound for the secondhand market."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=YXLWY7VHfxM&t=2136s",
            "https://www.youtube.com/watch?v=_-e12TPIFxw&t=179s",
            "https://www.youtube.com/watch?v=HPAddrORIJU&t=2089s",
        ],
        "validation_status": "Grounded strictly in Vol. 022 YouTube practitioner transcripts.",
    },
    {
        "title": "Sell Into Central Sterile and the Capital Committee",
        "subtitle": "Clinic buyers, line-item ROI, and referral-driven device sales careers",
        "audience": "Equipment reps and sales hires targeting ASC, veterinary, and dental clinics",
        "research_basis": (
            "Henry Schein Medical's Central Sterile pitch; Drs. Ballard and Pickering's "
            "$750 per case savings against a ~$8,400 Medicare knee; Valente's referral-first "
            "hiring reality; Licata's 30 accounts for 1 to 2 purchase orders."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=VMonxNBLqE4&t=323s",
            "https://www.youtube.com/watch?v=AQIyPCz9bJM&t=1587s",
            "https://www.youtube.com/watch?v=-KxAlnmN4IY&t=1107s",
            "https://www.youtube.com/watch?v=KsMhJhbA73k&t=2262s",
        ],
        "validation_status": "Grounded strictly in Vol. 022 YouTube practitioner transcripts.",
    },
]
