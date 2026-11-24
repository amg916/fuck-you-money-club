"""Volume 037 diagrams for SaaS discount brokerage and GPO arbitrage."""

from typing import Any, Dict, List

__all__ = [
    "VOLUME_037_SUBTITLE",
    "build_volume_037_diagrams_data",
    "VOLUME_037_POSITIONING_ALTERNATIVES",
]


VOLUME_037_SUBTITLE: str = (
    "From Partner Center to Pooled Buying - Indirect CSP Incentive Stacking, "
    "Distributor Margin Wraps, VIPMP Migrations, Brokered UCaaS, GPO Admin Fees, "
    "Contingency Telecom Audits, SaaS Rightsizing and Renewal Defense"
)


def build_volume_037_diagrams_data() -> list[dict]:
    """Return the 8 structured diagram dicts for Volume 037."""
    diagrams: List[Dict[str, Any]] = [
        {
            "diagram_id": "diag-01-microsoft-channel-entry-route",
            "chapter_number": 1,
            "chart_type": "process_flow",
            "title": "Microsoft Channel Entry Route",
            "subtitle": "Partner Center to indirect CSP to Commerce Incentives",
            "caption": (
                "Operators entering the Microsoft channel converge on one route, "
                "ending with a separate Microsoft Commerce Incentives enrollment."
            ),
            "assumptions_note": (
                "Direct bill threshold of $1M trailing revenue reported as raised "
                "from roughly $300,000 effective October. License margin of 8-15% "
                "is before any service bundling."
            ),
            "note": (
                "Attributed to Pax8 APAC, Inside Microsoft AI Cloud Partner Program, "
                "m365 Show and Spyglass MTG."
            ),
            "stages": [
                {
                    "step": "01",
                    "label": "Register Partner Center Account",
                    "value": "Step 1",
                    "detail": (
                        "Create the account and company profile under a domain email "
                        "tied to the primary Entra tenant."
                    ),
                },
                {
                    "step": "02",
                    "label": "Clear Business Verification",
                    "value": "Step 2",
                    "detail": "Pass business verification before attempting to transact.",
                },
                {
                    "step": "03",
                    "label": "Join the AI Cloud Partner Program",
                    "value": "Step 3",
                    "detail": (
                        "Enrollment is free; benefits packages run $345 to $4,730 a "
                        "year. Check the benefits tab before buying another security "
                        "license."
                    ),
                },
                {
                    "step": "04",
                    "label": "Link MPN ID to an Indirect Provider",
                    "value": "Step 4",
                    "detail": (
                        "More than 90% of partners run indirect through Ingram Micro, "
                        "Pax8, TD Synnex or Sherweb, since direct bill demands $1M "
                        "trailing revenue, a designation and paid support."
                    ),
                },
                {
                    "step": "05",
                    "label": "Enroll in Commerce Incentives Separately",
                    "value": "Step 5",
                    "detail": (
                        "A benefits package or designation does not start incentive "
                        "earnings on its own. Lock NCE seat counts and term inside "
                        "the 7-day window."
                    ),
                },
            ],
        },
        {
            "diagram_id": "diag-02-brokered-ucaas-price-ladder",
            "chapter_number": 6,
            "chart_type": "funnel",
            "title": "Brokered UCaaS Price Ladder",
            "subtitle": "Monthly per-seat prices from full contact center down to brokered Zoom Phone",
            "caption": (
                "Contact center quotes span $69 to $149 per agent, while add-ons and "
                "brokered phone seats compress the monthly bill well below list."
            ),
            "assumptions_note": (
                "Values are monthly prices as quoted by practitioners; contact center "
                "is per agent, the Customer Engagement Pack is per supervisor and Zoom "
                "Phone is per user. The broker fee is paid by the provider, not the customer."
            ),
            "note": (
                "Attributed to Mike Smith of AeroCom Inc, with the contact center "
                "range as quoted by UCaaS channel practitioners."
            ),
            "stages": [
                {
                    "label": "Full Contact Center Ceiling",
                    "value": 149,
                    "display": "$149 per agent per month",
                    "conversion": "Top of the $69 to $149 quoted range",
                    "detail": "Analysts still call Zoom Contact Center a 1.0 product.",
                },
                {
                    "label": "Full Contact Center Floor",
                    "value": 69,
                    "display": "$69 per agent per month",
                    "conversion": "Bottom of the $69 to $149 quoted range",
                    "detail": "Features are sliding into the base UCaaS license.",
                },
                {
                    "label": "Customer Engagement Pack Add-On",
                    "value": 20,
                    "display": "$20 per supervisor per month",
                    "conversion": "Positioned against $100+ per agent full licensing",
                    "detail": "Real-time queue analytics sold as a $20-$25 upsell.",
                },
                {
                    "label": "Zoom Phone Unlimited List",
                    "value": 15,
                    "display": "$15 per user per month",
                    "conversion": "List anchor before brokering",
                    "detail": "Most popular Zoom Phone tier.",
                },
                {
                    "label": "Zoom Phone Unlimited Brokered",
                    "value": 10,
                    "display": "Below $10 per user per month",
                    "conversion": "Sometimes $8-$9 against the $15 list",
                    "detail": (
                        "Never let a 100-plus-user buyer go direct; the provider "
                        "pays the broker fee."
                    ),
                },
            ],
        },
        {
            "diagram_id": "diag-03-msp-margin-floor-waterfall",
            "chapter_number": 3,
            "chart_type": "waterfall",
            "title": "MSP Margin Floor Waterfall",
            "subtitle": "Managed support versus security, RMM and non-Microsoft licensing",
            "caption": (
                "The MSP earns its real margin on wrapped services, with a 60% floor "
                "on managed support and a 30% floor on resold security, RMM and "
                "non-Microsoft licensing."
            ),
            "assumptions_note": (
                "Each price is indexed to 100 so the floors read as margin, not "
                "markup; the cost bars are the arithmetic complements of the stated "
                "60% and 30% margin floors."
            ),
            "note": (
                "Attributed to the Pax8 profitability playbook, with IDC's $4.14 of "
                "services per $1 of Microsoft cloud cited by the Pax8 co-founder via "
                "Cloud Software Association."
            ),
            "bars": [
                {
                    "label": "Managed Support Price",
                    "value": 100,
                    "display": "100 (indexed price)",
                    "kind": "total",
                },
                {
                    "label": "Delivery Cost Ceiling",
                    "value": 40,
                    "display": "-40",
                    "kind": "deduction",
                },
                {
                    "label": "Managed Support Margin Floor",
                    "value": 60,
                    "display": "60% margin, best in class",
                    "kind": "result",
                },
                {
                    "label": "Security, RMM and Non-Microsoft Price",
                    "value": 100,
                    "display": "100 (indexed price)",
                    "kind": "total",
                },
                {
                    "label": "Product Cost Ceiling",
                    "value": 70,
                    "display": "-70",
                    "kind": "deduction",
                },
                {
                    "label": "Licensing Margin Floor",
                    "value": 30,
                    "display": "At least 30% margin, not markup",
                    "kind": "result",
                },
            ],
        },
        {
            "diagram_id": "diag-04-microsoft-incentive-rate-bands",
            "chapter_number": 2,
            "chart_type": "horizontal_bars",
            "title": "Microsoft Incentive Rate Bands",
            "subtitle": "Where the FY27 incentive money now sits",
            "unit": "percent",
            "caption": (
                "With the core incentive stripped from Modern Work and Business Apps "
                "in FY27, the money moves to Tier 2 strategic SKUs, the growth "
                "accelerator and tiered Azure growth."
            ),
            "assumptions_note": (
                "Growth margin already includes base margin and is not stacked on "
                "top. Eligibility requires $25K trailing 12-month revenue per location "
                "ID plus a designation, specialization or 25 capability points."
            ),
            "note": (
                "Attributed to Pax8 and Inside Microsoft AI Cloud Partner Program."
            ),
            "bars": [
                {
                    "label": "CSP Growth Accelerator",
                    "min": 7.5,
                    "max": 12.5,
                    "typical": 12.5,
                    "display": "12.5%, up from 7.5%",
                },
                {
                    "label": "Tiered Azure Growth",
                    "min": 7,
                    "max": 12,
                    "typical": 10,
                    "display": "12 / 10 / 7% tiers",
                },
                {
                    "label": "Tier 2 Strategic SKUs",
                    "min": 7,
                    "max": 7,
                    "typical": 7,
                    "display": "7%",
                },
                {
                    "label": "Stacked Ceiling, M365 to Dynamics",
                    "min": 25.75,
                    "max": 34.75,
                    "typical": 26,
                    "display": "25.75% M365, 26% Azure, 34.75% Dynamics",
                },
                {
                    "label": "MCI Payout Split, Co-op to Rebate",
                    "min": 40,
                    "max": 60,
                    "typical": 60,
                    "display": "60% rebate, 40% co-op",
                },
            ],
        },
        {
            "diagram_id": "diag-05-adobe-workspace-buy-gates",
            "chapter_number": 5,
            "chart_type": "decision_tree",
            "title": "Adobe and Workspace Buy Gates",
            "subtitle": "Price the exit and verify the license before chasing a discount",
            "caption": (
                "List price is a negotiable anchor, but cheap seats and retention "
                "offers carry hidden commitments that must clear four gates."
            ),
            "assumptions_note": (
                "Sub-$2 Workspace seats often ride nonprofit, education or legacy "
                "panels that Google is suspending; a cheaper switch can cost $2,800 "
                "more in year one."
            ),
            "note": (
                "Attributed to Tech Meets East, InboxKit and Rook Technology Consulting."
            ),
            "nodes": [
                {
                    "gate": "G1",
                    "question": (
                        "Has Google confirmed the domain sits on an official partner "
                        "license, not a nonprofit, edu or legacy panel?"
                    ),
                    "pass_next": "G2",
                    "fail_action": (
                        "Reject the sub-$2 seats and file Google's support form for a "
                        "phone callback."
                    ),
                },
                {
                    "gate": "G2",
                    "question": (
                        "Is the Adobe annual-paid-monthly exit priced, with half of "
                        "every remaining payment owed on early cancellation?"
                    ),
                    "pass_next": "G3",
                    "fail_action": "Do not sign until the exit fee is priced in.",
                },
                {
                    "gate": "G3",
                    "question": (
                        "Is it confirmed that retention free months do not restart a "
                        "new one-year commitment?"
                    ),
                    "pass_next": "G4",
                    "fail_action": "Decline the free months at the cancellation screen.",
                },
                {
                    "gate": "G4",
                    "question": (
                        "Does the switch case hold across current bill, replacement "
                        "incl. retained items, one-time transition cost and the first "
                        "date old commitments end?"
                    ),
                    "pass_next": "Proceed with the purchase or switch",
                    "fail_action": "Hold the switch and keep the incumbent.",
                },
            ],
        },
        {
            "diagram_id": "diag-06-saas-sales-pod-architecture",
            "chapter_number": 11,
            "chart_type": "org_architecture",
            "title": "SaaS Sales Pod Architecture",
            "subtitle": "Numbers-first pod built around the account executive",
            "caption": (
                "The AE carries a quota near 5x OTE, fed by SDR dialing, a CRO "
                "champion, a procurement gate held on price, and CRM renewal automation."
            ),
            "assumptions_note": (
                "Quota multiples reported range from 5x (SaasRise) to 5.6-6.1x "
                "(QuotaPath), with a Bridge median of 4.6x; 48% of reps hit quota."
            ),
            "note": (
                "Attributed to Sell Better, Caliber, SaasRise, GrowthSpree and "
                "HubSpot Data Analytics by MergeYourData."
            ),
            "center": {
                "role": "Mid-Market Account Executive",
                "headcount": "1 AE per 2 SDRs, never above 2.5 to 1",
                "focus": "Quota at 5x OTE; a $200K median OTE rep brings in about $1M",
            },
            "spokes": [
                {
                    "role": "SDR",
                    "type": "Outbound dialing",
                    "kpi": "40 calls per hour; 200 calls per week for at least 2 meetings",
                },
                {
                    "role": "CRO Champion",
                    "type": "Internal sponsor",
                    "kpi": "Rates the business case very believable in the room",
                },
                {
                    "role": "Procurement",
                    "type": "Buyer gate",
                    "kpi": "Price kept as the final issue; terms only after cash is the last objection",
                },
                {
                    "role": "CRM Automation",
                    "type": "Renewal engine",
                    "kpi": "Workflow fires when renewal date is under 30 days out",
                },
            ],
        },
        {
            "diagram_id": "diag-07-vipmp-volume-level-ladder",
            "chapter_number": 4,
            "chart_type": "stacked_comparison",
            "title": "VIPMP Volume Level Ladder",
            "subtitle": "Four per-end-customer price levels on Adobe VIP Marketplace",
            "total_range": "1 to 100+ units per end customer",
            "caption": (
                "VIP Marketplace keys price to per-customer seat counts, with "
                "auto-renewal on the anniversary date and a 14-day return window."
            ),
            "assumptions_note": (
                "Level 1 starts at a single unit; Level 4 is open-ended above 100 "
                "units. Levels 3 and 4 currently carry the same discount."
            ),
            "note": "Attributed to David Villanueva of TD SYNNEX Spain.",
            "buckets": [
                {
                    "label": "Level 1",
                    "low": 1,
                    "high": 9,
                    "notes": "Up to 9 units; move single-unit customers to auto-renewal",
                },
                {
                    "label": "Level 2",
                    "low": 10,
                    "high": 49,
                    "notes": "First price break",
                },
                {
                    "label": "Level 3",
                    "low": 50,
                    "high": 99,
                    "notes": "Same discount as Level 4 today",
                },
                {
                    "label": "Level 4",
                    "low": 100,
                    "high": 100,
                    "notes": "100 units and above",
                },
            ],
        },
        {
            "diagram_id": "diag-08-hybrid-pricing-rollout-roadmap",
            "chapter_number": 12,
            "chart_type": "timeline_roadmap",
            "title": "Hybrid Pricing Rollout Roadmap",
            "subtitle": "Seat base, metered usage and enforced renewal uplift",
            "caption": (
                "The seat survives as a base fee wrapped in credits, metered overage "
                "and contractual uplifts, with hybrid models posting 105% net revenue "
                "retention."
            ),
            "assumptions_note": (
                "A P90 user can cost five times a P50 user, and AI pulls classical "
                "85% to 95% gross margins toward roughly 50%."
            ),
            "note": (
                "Attributed to The Innovation Attorney, Champion Leadership, "
                "MonetizeNow, Soft Learn Hub and Willingness to Pay."
            ),
            "weeks": [
                {
                    "week": "Week 1",
                    "title": "Model P50 and P90 Cost per User",
                    "deliverable": "Cost model against the price point",
                    "gate": "Hold at least 60% gross margin at P50 users",
                },
                {
                    "week": "Week 2",
                    "title": "Fair-Use Policy and Pilot",
                    "deliverable": "Usage pilot with 5 to 20 customers",
                    "gate": "Fair-use cap in place before opening usage to the full base",
                },
                {
                    "week": "Week 3",
                    "title": "Encode Renewal Uplift",
                    "deliverable": "Fixed or maximum uplift stored on every quote",
                    "gate": "Escalator talks open at 7% within the 3% to 7% range",
                },
                {
                    "week": "Week 4",
                    "title": "Price In Buyer Meter Controls",
                    "deliverable": "Alerts at 80% and 100%, rollover, locked overage and a contractual cap",
                    "gate": "Validated with finance, customer success, sales, product and customers",
                },
            ],
        },
    ]
    return diagrams


VOLUME_037_POSITIONING_ALTERNATIVES: List[Dict[str, Any]] = [
    {
        "title": "The Indirect CSP Margin Engine",
        "subtitle": (
            "Stack Microsoft incentives, wrap services at 30-60% margin, and stop "
            "living on an 8-15% license"
        ),
        "audience": "MSPs and resellers entering or rebuilding a Microsoft and distributor practice",
        "research_basis": (
            "Pax8 APAC on the $1M direct bill threshold, Inside Microsoft AI Cloud "
            "Partner Program on stacked incentives and the 60/40 payout split, Pax8 "
            "on 30% and 60% margin floors, and the Pax8 co-founder citing IDC's $4.14 "
            "of services per $1 of Microsoft cloud."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=Xywyds1IfvM&t=271s",
            "https://www.youtube.com/watch?v=jz1cE7UYBO4&t=948s",
            "https://www.youtube.com/watch?v=jcYTmMdEGPo&t=118s",
            "https://www.youtube.com/watch?v=tsL0gg_Jy9U&t=667s",
            "https://www.youtube.com/watch?v=KcmWalqZBzk&t=114s",
            "https://www.youtube.com/watch?v=phXe8eJoVeo&t=795s",
        ],
        "validation_status": "Grounded strictly in Vol. 037 YouTube practitioner transcripts.",
    },
    {
        "title": "Renewal Defense and Rightsizing",
        "subtitle": (
            "Find the 44% of idle licenses, calendar the notice deadline, and cap "
            "uplifts at 3 to 5%"
        ),
        "audience": "IT, finance and procurement leads buying SaaS without a dedicated sourcing team",
        "research_basis": (
            "SaaS Procurement Insider on 2-4x vendor undercounts and 15-30% shadow IT, "
            "MetrixData 360 on $250K+ yearly reclaim from help desk tickets, Tropic on "
            "60 to 90 day kickoffs and 3 to 5% caps, The Negotiator Guru on 8 in 10 "
            "over-licensed clients, and fynk on roughly 70% auto-renewing contracts."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=udHdwtjP7yM&t=190s",
            "https://www.youtube.com/watch?v=lB5ThkY4hMA&t=1576s",
            "https://www.youtube.com/watch?v=veu6EUBTdBE&t=49s",
            "https://www.youtube.com/watch?v=FESALIJcxS0&t=120s",
            "https://www.youtube.com/watch?v=dOTg4A37x5g&t=38s",
            "https://www.youtube.com/watch?v=QLqtDhk3PoI&t=187s",
        ],
        "validation_status": "Grounded strictly in Vol. 037 YouTube practitioner transcripts.",
    },
    {
        "title": "Pooled Buying, Brokered Seats and Contingency Audits",
        "subtitle": (
            "Let suppliers and providers pay the fee while GPOs, brokers and auditors "
            "pull the discount"
        ),
        "audience": "Operators and owners who want lower unit prices without paying upfront for representation",
        "research_basis": (
            "Eric Bricker on 1.5 to 3 percent supplier-paid GPO admin fees, Una on 18 "
            "to 22 percent food savings, Angelique Beslic on 80 to 90 percent "
            "compliance bands, AeroCom on Zoom Phone below $10 against a $15 list, and "
            "Auditel on a $68,000 monthly bill cut and a $165,000 go-behind credit."
        ),
        "sources": [
            "https://www.youtube.com/watch?v=N0B0bUjLrUE&t=65s",
            "https://www.youtube.com/watch?v=vXeviFgIR1I&t=24s",
            "https://www.youtube.com/watch?v=K2Slgt-y1wo&t=219s",
            "https://www.youtube.com/watch?v=viRtp8k9GAo&t=192s",
            "https://www.youtube.com/watch?v=F00NVfaC6Tk&t=141s",
            "https://www.youtube.com/watch?v=YAHf-FXxBCM&t=95s",
        ],
        "validation_status": "Grounded strictly in Vol. 037 YouTube practitioner transcripts.",
    },
]
