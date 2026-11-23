from __future__ import annotations

VOLUME_042_SUBTITLE = (
    "The Complete Playbook for Cell-Tower, Digital-Billboard & IOS Lease "
    "Arbitrage: $120,000–$950,000 USD in Annual Operator Revenue, "
    "Starting with a 1 FT + 3 C Pod (4 People); Six People at Scale"
)

VOLUME_042_POSITIONING_ALTERNATIVES = [
    {
        "title": "The Telecom Rights Spread Desk",
        "subtitle": (
            "Build a parcel-to-closing engine for tower and rooftop rights, "
            "pricing transferable cash flows rather than institutional purchase principal."
        ),
        "audience": (
            "Principal investors and infrastructure acquisition operators who can "
            "underwrite lease rights, title exceptions, lender consent, and buyer demand."
        ),
        "research_basis": (
            "47 CFR 17.4 establishes registration requirements for covered antenna "
            "structures; the FCC Antenna Structure Registration search supports initial "
            "prospecting but does not establish ownership or transferable lease rights. "
            "47 U.S.C. 332(c)(7) preserves specified local siting authority subject "
            "to federal limitations. California Business and Professions Code "
            "10130 and 10131 illustrate why transaction capacity and brokerage "
            "activities require state-specific review. Neither registration nor "
            "these statutes establishes a buyer's purchase multiple."
        ),
        "sources": [
            "https://www.ecfr.gov/current/title-47/section-17.4",
            "https://wireless2.fcc.gov/UlsApp/AsrSearch/asrRegistrationSearch.jsp",
            "https://www.law.cornell.edu/uscode/text/47/332",
            "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=BPC&sectionNum=10130.",
            "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=BPC&sectionNum=10131.",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Permitted Billboard Assignment Desk",
        "subtitle": (
            "Turn highway parcel screening, sign entitlement diligence, and "
            "assignable ground control into documented assignment-fee opportunities."
        ),
        "audience": (
            "Land-rights acquisition teams serving outdoor-advertising operators "
            "with verified demand for legally usable digital-sign locations."
        ),
        "research_basis": (
            "23 U.S.C. 131 provides the federal highway-advertising control "
            "framework. 23 CFR 750.705 and 750.706 address effective control "
            "and state criteria. Federal coverage, applicable state agreements, "
            "state DOT rules, and local ordinances must be checked together; "
            "traffic counts alone establish neither permit eligibility nor "
            "digital conversion rights. Assignment value also depends on "
            "permit transfer procedures and the ground lease's consent language."
        ),
        "sources": [
            "https://www.law.cornell.edu/uscode/text/23/131",
            "https://www.ecfr.gov/current/title-23/section-750.705",
            "https://www.ecfr.gov/current/title-23/section-750.706",
            "https://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvthwy.cfm",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Zero-Building Fleet Yard Spread",
        "subtitle": (
            "Control usable industrial outdoor storage, contract fleet demand, "
            "and retain the master-lease spread with metered access and billing."
        ),
        "audience": (
            "Small industrial-property operating teams with fleet relationships "
            "and capacity to supervise site diligence, lease obligations, and collections."
        ),
        "research_basis": (
            "40 CFR 312.20 and 312.21 establish elements of all appropriate "
            "inquiries and environmental-professional inquiry requirements. "
            "Use a qualified professional to scope Phase I work and any "
            "transaction-specific liability-protection requirements. "
            "40 CFR 122.26 supplies the federal industrial stormwater framework; "
            "coverage depends on actual activities, exposure, and the applicable "
            "permitting authority. Neither a Phase I report nor a triple-net "
            "lease substitutes for permitted heavy-vehicle use."
        ),
        "sources": [
            "https://www.ecfr.gov/current/title-40/section-312.20",
            "https://www.ecfr.gov/current/title-40/section-312.21",
            "https://www.ecfr.gov/current/title-40/section-122.26",
            "https://www.epa.gov/brownfields/brownfields-all-appropriate-inquiries",
            "https://www.epa.gov/npdes/stormwater-discharges-industrial-activities",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
]


def build_volume_042_diagrams_data() -> list[dict]:
    specs = [
        (
            "diag-01-parcel-to-retained-spread",
            "process_flow",
            "Control Rights Before Selling the Spread",
            "Five operating steps from a mapped parcel to collected operator revenue",
            1,
            "operating_framework",
            (
                "This workflow serves telecom rights, billboard assignments, and "
                "industrial outdoor storage. First-deal planning remains 2–6 months. "
                "The scorecard counts earned spreads and fees, excluding institutional "
                "purchase principal and tenant gross billings."
            ),
            (
                "A mapped opportunity becomes inventory only after rights, "
                "consents, permitted use, and an executable exit are documented."
            ),
            [
                (
                    "Map eligible parcels",
                    "FCC ASR + DOT AADT",
                    1.0,
                    (
                        "Join FCC ASR records, state DOT annual average daily "
                        "traffic layers, and assessor parcels in QGIS. Verify "
                        "rooftop candidates separately because ASR is not a "
                        "complete inventory of telecom installations."
                    ),
                ),
                (
                    "Establish transferable control",
                    "Title + options + consents",
                    2.0,
                    (
                        "Review recorded instruments, lease amendments, assignment "
                        "limits, mortgage priority, and access rights. Use "
                        "diligence-contingent control documents and identify required "
                        "lender subordination, nondisturbance, and attornment agreements."
                    ),
                ),
                (
                    "Underwrite the actual spread",
                    "Cash-flow NPV + buyer bids",
                    3.0,
                    (
                        "Model escalators, termination, restoration, and collection "
                        "risk in a spreadsheet. Test a 16×–22× telecom buyer "
                        "multiple only as an illustrative sensitivity on buyer-accepted "
                        "annual contractual rent; obtain written bids before relying "
                        "on an exit value."
                    ),
                ),
                (
                    "Clear site-specific execution risks",
                    "Permits + environmental + access",
                    4.0,
                    (
                        "Confirm sign spacing and digital operation permissions, "
                        "telecom access and utility easements, or IOS heavy-axle "
                        "use and stormwater obligations. Commission Phase I work "
                        "before executing an IOS master lease."
                    ),
                ),
                (
                    "Close and reconcile collections",
                    "Settlement ledger + yard billing",
                    5.0,
                    (
                        "Match settlement statements to earned assignment or buyout "
                        "spreads. For IOS, reconcile contracted tenant receipts, "
                        "master rent, and directly allocated property obligations "
                        "before measuring retained spread; link RFID access to "
                        "the authorized tenant roster."
                    ),
                ),
            ],
        ),
        (
            "diag-02-annual-parcel-cohort-funnel",
            "funnel",
            "One Cohort, Seventeen Monetized Opportunities",
            "Annual illustrative funnel supporting the Base operator-revenue mix",
            6,
            "illustrative_model",
            (
                "The same 400 unique parcel opportunities flow through every "
                "stage; each stage is a subset of the preceding stage. "
                "Conversions are planning assumptions, not observed performance. "
                "The cohort represents a mature annual operating period, not "
                "a promise to close within the first 30 days."
            ),
            (
                "Seventeen outcomes comprise four telecom spread transactions, "
                "five billboard assignments, and eight IOS activations. The "
                "IOS revenue mix assumes twelve billed months per activated yard."
            ),
            [
                (
                    "Mapped opportunities",
                    "400 unique parcel records",
                    400.0,
                    (
                        "Deduplicate by parcel and proposed rights package before "
                        "counting. Capture source date, owner contact route, "
                        "traffic or telecom evidence, and the proposed use."
                    ),
                ),
                (
                    "Desktop-qualified opportunities",
                    "200 parcels; 50% of mapped",
                    200.0,
                    (
                        "Remove incompatible zoning, unsuitable access, obvious "
                        "sign-spacing conflicts, and absent buyer demand. Retain "
                        "a recorded reason for every exclusion."
                    ),
                ),
                (
                    "Owner-engaged opportunities",
                    "80 parcels; 40% of qualified",
                    80.0,
                    (
                        "Confirm the owner's identity and transaction interest, "
                        "obtain relevant leases, and establish a credible route "
                        "to inspect title and site conditions."
                    ),
                ),
                (
                    "Controlled diligence opportunities",
                    "24 parcels; 30% of engaged",
                    24.0,
                    (
                        "Secure documented diligence access and conditional control "
                        "where appropriate. Obtain preliminary counterparty economics "
                        "before ordering expensive reports or committing deposits."
                    ),
                ),
                (
                    "Monetized opportunities",
                    "17 parcels; 70.83% of controlled",
                    17.0,
                    (
                        "Close four telecom transactions and five billboard "
                        "assignments; activate eight leased yards. Overall cohort "
                        "conversion is 4.25%, with annual IOS revenue dependent "
                        "on full-year occupancy and payment."
                    ),
                ),
            ],
        ),
        (
            "diag-03-base-owner-profit-waterfall",
            "waterfall",
            "$535,000 Operator Revenue to $214,000 Owner Profit",
            "Six bars reconcile the Base scenario to a 40.0% net margin",
            3,
            "illustrative_model",
            (
                "Formula v2.0 Base totals are canonical; the four expense "
                "allocations are illustrative. The first bar is the opening "
                "total, middle bars are signed deductions, and the final bar "
                "is the ending total rather than another additive movement. "
                "Operator revenue already excludes acquisition principal, "
                "tenant gross billings, and IOS property costs used to compute "
                "retained lease spreads."
            ),
            (
                "$535,000 − $90,000 − $75,000 − $60,000 − $96,000 = "
                "$214,000; $214,000 / $535,000 = 40.0%. The $96,000 "
                "recurring-overhead allocation equals $8,000 monthly; other "
                "deductions are variable transaction expenses."
            ),
            [
                (
                    "Gross operator revenue",
                    "$535,000 opening total",
                    535000.0,
                    (
                        "Combine $260,000 telecom buyout spreads, $95,000 billboard "
                        "assignment fees, and $180,000 retained IOS spreads. "
                        "These are operator-level economics, not the underlying "
                        "property or easement transaction values."
                    ),
                ),
                (
                    "Origination and closing support",
                    "−$90,000 variable expense",
                    -90000.0,
                    (
                        "Allocate transaction-specific sourcing and closing support "
                        "only after verifying the permitted compensation structure. "
                        "Do not duplicate contractor costs assigned to recurring overhead."
                    ),
                ),
                (
                    "Title, legal, and consent execution",
                    "−$75,000 variable expense",
                    -75000.0,
                    (
                        "Budget title work, instrument drafting, lender negotiations, "
                        "recording coordination, and failed-deal legal costs outside "
                        "the already calculated acquisition spread."
                    ),
                ),
                (
                    "Site and permit diligence",
                    "−$60,000 variable expense",
                    -60000.0,
                    (
                        "Allocate surveys, Phase I reports, zoning verification, "
                        "engineering checks, and permit diligence. Include abandoned "
                        "opportunity costs rather than charging only completed deals."
                    ),
                ),
                (
                    "Recurring operating overhead",
                    "−$96,000 annual overhead",
                    -96000.0,
                    (
                        "Reserve $8,000 monthly for contracted administration, "
                        "software, insurance, accounting, travel, and routine "
                        "operating support, with no duplication of variable expenses."
                    ),
                ),
                (
                    "Annual owner net profit",
                    "$214,000 ending total",
                    214000.0,
                    (
                        "The canonical Base result is owner profit after "
                        "$321,000 modeled operating expenses. Personal taxes, "
                        "owner distributions, and financing principal movements "
                        "are not additional operating-expense bars."
                    ),
                ),
            ],
        ),
        (
            "diag-04-five-operator-revenue-rails",
            "horizontal_bars",
            "Five Revenue Rails, One $535,000 Base",
            "Illustrative annual dollar yield by sub-niche, not asset investment returns",
            2,
            "illustrative_model",
            (
                "Bar values are annual operator-revenue contributions in USD, "
                "not percentage yields or underlying asset prices. Deal counts "
                "and unit spreads are illustrative allocations of the canonical "
                "Base total. The eight IOS yards each contribute twelve months "
                "of retained spread in this mature-year model."
            ),
            (
                "Scenario anchors remain Conservative $120,000 revenue at 28% "
                "for $33,600 owner profit; Base $535,000 at 40.0% for "
                "$214,000; Scaled $950,000 at 52% for $494,000. "
                "Conservative and Base use four people; Scaled uses six."
            ),
            [
                (
                    "Ground-tower easement spreads",
                    "2 transactions × $75,000",
                    150000.0,
                    (
                        "Retain $150,000 after the modeled acquisition consideration "
                        "embedded in each buyout spread, before the waterfall's "
                        "separate operating expenses. Collect through documented "
                        "settlement disbursements rather than counting buyer principal."
                    ),
                ),
                (
                    "Rooftop telecom rights spreads",
                    "2 transactions × $55,000",
                    110000.0,
                    (
                        "Retain $110,000 from transferable rooftop rights. "
                        "Price roof replacement access, relocation provisions, "
                        "building lender consent, and operator termination rights "
                        "before accepting the acquisition obligation."
                    ),
                ),
                (
                    "Digital-billboard assignments",
                    "5 assignments × $19,000",
                    95000.0,
                    (
                        "Earn $95,000 in documented assignment fees for "
                        "usable ground-control packages. Verify permit transfer "
                        "procedures and lease consent separately; traffic volume "
                        "does not establish transferable sign rights."
                    ),
                ),
                (
                    "Fleet drop-yard master leases",
                    "4 yards × $25,000 annually",
                    100000.0,
                    (
                        "Retain $100,000 after master rent and directly allocated "
                        "property obligations. Bill fleet tenants through "
                        "authorized ACH instructions and reconcile settled receipts "
                        "against contract schedules and access records."
                    ),
                ),
                (
                    "Equipment-storage master leases",
                    "4 yards × $20,000 annually",
                    80000.0,
                    (
                        "Retain $80,000 after master rent and directly allocated "
                        "property obligations. Monitor permitted storage categories, "
                        "surface damage, delinquency, and exposure to uninsured "
                        "tenant equipment losses."
                    ),
                ),
            ],
        ),
        (
            "diag-05-rights-statutes-and-site-checks",
            "decision_tree",
            "Four Checks Before Irreversible Exposure",
            "Proceed on documented evidence; resolve defects or reject the parcel",
            5,
            "operating_framework",
            (
                "These four sequential checks apply according to transaction "
                "type and jurisdiction. A failed check routes the opportunity "
                "to documented remediation or rejection, not automatic execution. "
                "Cited provisions establish specific requirements or frameworks; "
                "they do not replace parcel-level determinations."
            ),
            (
                "Capital follows confirmed capacity, priority, permitted use, "
                "and site condition. A favorable exit multiple cannot repair "
                "an unassignable right or prohibited yard operation."
            ),
            [
                (
                    "Capacity and licensed activity",
                    "Proceed if transaction role is verified",
                    1.0,
                    (
                        "Map principal activity, options, referrals, and services "
                        "performed for others against the applicable state rules. "
                        "California Business and Professions Code 10130 and "
                        "10131 illustrate the licensing boundary; do not assume "
                        "every option assignment qualifies for an exemption."
                    ),
                ),
                (
                    "Priority and required consents",
                    "Proceed if enforceable rights survive",
                    2.0,
                    (
                        "Inspect title, mortgage priority, termination clauses, "
                        "assignment restrictions, and access easements. Obtain "
                        "required lender and lessor consents and negotiate "
                        "an effective SNDA where needed; the SNDA requirement "
                        "depends on documents and risk, not a universal statute."
                    ),
                ),
                (
                    "Sign and telecom permissions",
                    "Proceed if the proposed use is permitted",
                    3.0,
                    (
                        "For covered highway signs, apply 23 U.S.C. 131, "
                        "23 CFR 750.705–750.706, state DOT spacing criteria, "
                        "and local digital-sign rules. For telecom, check "
                        "47 CFR 17.4 applicability and local siting requirements "
                        "within 47 U.S.C. 332(c)(7)."
                    ),
                ),
                (
                    "IOS environmental and axle suitability",
                    "Proceed if site obligations are costed",
                    4.0,
                    (
                        "Before executing the master lease, obtain Phase I "
                        "screening and verify heavy-vehicle zoning, turning paths, "
                        "surface capacity, drainage, and fire access. Scope "
                        "40 CFR Part 312 when applicable and assess industrial "
                        "stormwater coverage under 40 CFR 122.26."
                    ),
                ),
            ],
        ),
        (
            "diag-06-four-person-pod-six-person-scale",
            "org_architecture",
            "Four Core Seats; Two Additions at Scale",
            "Conservative and Base use 1 FT + 3 C; Scaled uses 2 FT + 4 C",
            11,
            "operating_framework",
            (
                "FT denotes a full-time operator and C denotes a contracted "
                "seat. The first four seats form the four-person pod; the "
                "last two activate only in the six-person Scaled scenario. "
                "Specialist reports are purchased services, not additional "
                "standing pod seats."
            ),
            (
                "Keep signing authority and cash exposure with the principal. "
                "Automate evidence assembly and recurring billing, while "
                "retaining human review of rights and exceptions."
            ),
            [
                (
                    "Principal and acquisition lead",
                    "Core seat 1; full-time operator",
                    1.0,
                    (
                        "Own pricing, capital commitments, counterparty selection, "
                        "and final execution. Approve acquisition assumptions "
                        "against written demand and review the operator-revenue "
                        "bridge before signing."
                    ),
                ),
                (
                    "Rights and transaction counsel",
                    "Core seat 2; contracted specialist",
                    1.0,
                    (
                        "Review licensed-activity questions, title exceptions, "
                        "assignment language, lender consent, and SNDA terms. "
                        "Maintain a document checklist tied to each parcel."
                    ),
                ),
                (
                    "GIS and site diligence coordinator",
                    "Core seat 3; contracted specialist",
                    1.0,
                    (
                        "Maintain QGIS parcel screening and coordinate "
                        "surveys, environmental professionals, zoning confirmation, "
                        "and DOT permit checks without substituting desktop "
                        "screening for required field work."
                    ),
                ),
                (
                    "Billing and transaction operations",
                    "Core seat 4; contracted specialist",
                    1.0,
                    (
                        "Reconcile settlement statements, tenant invoices, "
                        "master-rent schedules, insurance evidence, and access "
                        "permissions. Escalate collection exceptions rather "
                        "than automatically changing contractual rights."
                    ),
                ),
                (
                    "Portfolio operating lead",
                    "Scaled addition; second full-time operator",
                    1.0,
                    (
                        "Take daily responsibility for active yards, renewal "
                        "calendars, tenant exceptions, and vendor performance "
                        "so the principal can maintain acquisition discipline."
                    ),
                ),
                (
                    "Dedicated sourcing coordinator",
                    "Scaled addition; fourth contracted specialist",
                    1.0,
                    (
                        "Expand owner contact coverage and buyer matching "
                        "using approved transaction roles and compensation "
                        "structures. Preserve parcel-level attribution and "
                        "prevent duplicate acquisition outreach."
                    ),
                ),
            ],
        ),
        (
            "diag-07-startup-capital-four-buckets",
            "stacked_comparison",
            "Deploy $12,000–$60,000 Without Buying the Whole Asset",
            "Four startup buckets shown at a $36,000 planning allocation",
            4,
            "illustrative_model",
            (
                "Numeric values show the $36,000 planning allocation. "
                "Matched lean allocations total $12,000; matched expanded "
                "allocations total $60,000. These budgets fund diligence, "
                "conditional control, and runway, not full easement purchases "
                "or major yard construction. Capital deployment is not "
                "automatically a current-period operating expense."
            ),
            (
                "The lean budget depends on low deposits, staged reports, "
                "and limited cash burn. First-deal timing is 2–6 months "
                "and monthly operating expense planning is $2,000–$12,000; "
                "the startup range does not cover every timing and burn combination."
            ),
            [
                (
                    "Rights and transaction setup",
                    "$8,000 planning allocation",
                    8000.0,
                    (
                        "Lean $3,000; expanded $12,000. Fund entity-specific "
                        "contracts, title review, licensing analysis, consent "
                        "planning, and documented control instruments before "
                        "committing to acquisition obligations."
                    ),
                ),
                (
                    "Site and permit investigation",
                    "$10,000 planning allocation",
                    10000.0,
                    (
                        "Lean $3,000; expanded $16,000. Stage Phase I work, "
                        "surveys, drainage review, sign eligibility checks, "
                        "and heavy-vehicle use verification by parcel priority."
                    ),
                ),
                (
                    "Conditional control and deposits",
                    "$12,000 planning allocation",
                    12000.0,
                    (
                        "Lean $4,000; expanded $22,000. Reserve cash for "
                        "negotiated options, refundable deposits where available, "
                        "and initial yard security deposits; track refund "
                        "conditions and expiry dates separately."
                    ),
                ),
                (
                    "Systems and working reserve",
                    "$6,000 planning allocation",
                    6000.0,
                    (
                        "Lean $2,000; expanded $10,000. Fund GIS hosting, "
                        "document storage, billing setup, insurance activation, "
                        "and operating liquidity. Stress-test slower closings "
                        "before treating this reserve as sufficient runway."
                    ),
                ),
            ],
        ),
        (
            "diag-08-thirty-day-evidence-sprint",
            "timeline_roadmap",
            "Thirty Days to a Defensible Acquisition Pipeline",
            "Four weekly milestones produce evidence, not an assumed first closing",
            12,
            "operating_framework",
            (
                "The first sprint establishes a working acquisition system. "
                "A first completed deal remains a 2–6 month planning horizon. "
                "Weekly activity targets are illustrative and separate from "
                "the mature annual cohort used in the funnel."
            ),
            (
                "End the month with priced, documented opportunities and "
                "explicit unresolved conditions; do not accelerate execution "
                "by skipping lender, permit, or environmental work."
            ),
            [
                (
                    "Days 1-7",
                    "Choose one market and map 50 parcels",
                    7.0,
                    (
                        "Select a primary revenue rail and buyer profile. "
                        "Load FCC ASR or state DOT AADT layers into QGIS, "
                        "verify local use criteria, and create parcel records "
                        "with source dates and ownership evidence."
                    ),
                ),
                (
                    "Days 8-14",
                    "Screen 20 parcels and seek 10 owner conversations",
                    14.0,
                    (
                        "Prioritize transferable rights and demonstrated buyer "
                        "demand. Request leases and amendments, document "
                        "owner authority, and record exclusion reasons without "
                        "treating outreach targets as achieved conversions."
                    ),
                ),
                (
                    "Days 15-21",
                    "Price three candidates and assemble diligence scopes",
                    21.0,
                    (
                        "Model downside rent and termination assumptions, "
                        "request buyer indications, identify lender requirements, "
                        "and obtain title, Phase I, survey, or permit "
                        "work proposals appropriate to each candidate."
                    ),
                ),
                (
                    "Days 22-30",
                    "Advance one conditional control package",
                    30.0,
                    (
                        "Negotiate a diligence-contingent option or equivalent "
                        "control structure, assign consent owners, and schedule "
                        "specialist work. Test settlement and billing ledgers "
                        "using synthetic entries; execute no IOS master lease "
                        "before environmental and heavy-axle checks."
                    ),
                ),
            ],
        ),
    ]
    return [
        dict(
            diagram_id=identifier,
            chart_type=kind,
            title=title,
            subtitle=subtitle,
            chapter_number=chapter,
            epistemic_tag=tag,
            assumptions_note=note,
            caption=caption,
            stages=[
                dict(
                    label=label,
                    value=value,
                    numeric_value=float(number),
                    detail=detail,
                )
                for label, value, number, detail in stages
            ],
        )
        for (
            identifier,
            kind,
            title,
            subtitle,
            chapter,
            tag,
            note,
            caption,
            stages,
        ) in specs
    ]
