from __future__ import annotations

VOLUME_047_SUBTITLE = (
    "The Complete Playbook for AI Powered-Land, Substation Headroom & BESS "
    "Site Optioning: $110,000–$900,000 USD in Annual Operator Revenue, "
    "Built Around a 1 FT + 3 C (4 People) Pod"
)

VOLUME_047_POSITIONING_ALTERNATIVES = [
    {
        "title": "Utility-Evidenced Powered-Land Origination",
        "subtitle": (
            "Package assignable land interests around documented deliverable "
            "MW, bounded upgrade exposure, and credible energization schedules."
        ),
        "audience": (
            "Principal option holders and licensed development brokers serving "
            "modular and hyperscale AI data-center developers."
        ),
        "research_basis": (
            "16 U.S.C. 824 and 18 CFR 35.28 establish relevant federal electric "
            "rate and transmission frameworks; neither substitutes for a "
            "utility's site-specific load-service determination. California "
            "Business and Professions Code sections 10130 and 10131 illustrate "
            "why transaction role and compensation require state-specific "
            "licensure analysis. Screen 69kV–345kV corridors, then obtain written "
            "utility evidence before pricing capacity-dependent assignment fees."
        ),
        "sources": [
            "https://www.law.cornell.edu/uscode/text/16/824",
            "https://www.ecfr.gov/current/title-18/chapter-I/subchapter-C/part-35/section-35.28",
            "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=BPC&sectionNum=10130.",
            "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=BPC&sectionNum=10131.",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "Small-Footprint BESS Option Assembly",
        "subtitle": (
            "Control 5–25 acre storage parcels with diligence-contingent "
            "12–24 month options and explicit expiration-loss reserves."
        ),
        "audience": (
            "Small origination pods supplying standalone battery-storage "
            "developers with transferable site control and organized diligence."
        ),
        "research_basis": (
            "18 CFR 35.28 supplies the applicable federal interconnection "
            "framework where jurisdictional; the relevant tariff determines "
            "the actual study path. Clean Water Act section 404, 33 U.S.C. "
            "1344, addresses permits for covered discharges of dredged or "
            "fill material. Keep storage injection, charging demand, local "
            "fire access, and conditional-use requirements separate from "
            "AI campus load, fiber, cooling, and water requirements."
        ),
        "sources": [
            "https://www.ecfr.gov/current/title-18/chapter-I/subchapter-C/part-35/section-35.28",
            "https://www.law.cornell.edu/uscode/text/33/1344",
            "https://www.fema.gov/flood-maps",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "Evidence-to-Assignment Development Desk",
        "subtitle": (
            "Turn dated utility studies, clean option rights, and verified "
            "land-use pathways into milestone-based operator receipts."
        ),
        "audience": (
            "A four-person principal-led pod coordinating utility engineers, "
            "land-use specialists, and transaction counsel for developer buyers."
        ),
        "research_basis": (
            "California Business and Professions Code sections 10130 and 10131 "
            "distinguish licensable real-estate activity by transaction role; "
            "a principal label alone does not resolve the analysis. Federal "
            "interconnection requirements and Clean Water Act permitting "
            "provide separate diligence tracks. Use a dated evidence register "
            "to distinguish screening indications, preliminary studies, binding "
            "service commitments, and unresolved development conditions."
        ),
        "sources": [
            "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=BPC&sectionNum=10130.",
            "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=BPC&sectionNum=10131.",
            "https://www.law.cornell.edu/uscode/text/33/1344",
            "https://www.ecfr.gov/current/title-18/chapter-I/subchapter-C/part-35/section-35.28",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
]


def build_volume_047_diagrams_data() -> list[dict]:
    specs = [
        (
            "diag-01-evidence-backed-option-workflow",
            "process_flow",
            "From Corridor Signal to Assignable Site Interest",
            "Sell documented development progress, not apparent electrical proximity.",
            1,
            "operating_framework",
            (
                "Sequence numbers indicate work order rather than capacity or "
                "conversion probability. Typical first-deal timing is 2–6 "
                "months; utility studies can extend it. Maintain separate "
                "standalone BESS and AI campus underwriting templates."
            ),
            (
                "An attractive map intersection becomes a priced option only "
                "after power, land rights, upgrade exposure, and timing have "
                "survived documented diligence."
            ),
            [
                (
                    "Screen distinct site classes",
                    "Separate storage parcels from AI campus candidates",
                    1,
                    (
                        "Use QGIS, utility GIS, FEMA maps, and USFWS wetland "
                        "mapping to screen 69kV–345kV corridors. Track 5–25 acre "
                        "standalone BESS parcels separately from campuses "
                        "requiring fiber, water, larger footprints, and load service."
                    ),
                ),
                (
                    "Obtain utility evidence",
                    "Request dated capacity and service-path documentation",
                    2,
                    (
                        "Record requested load, injection and charging profiles, "
                        "study status, contingencies, deliverable MW, upgrade "
                        "allocation, and energization range. A substation pin "
                        "or raw queue filing establishes neither available "
                        "headroom nor a service commitment."
                    ),
                ),
                (
                    "Secure contingent site control",
                    "Negotiate transferable 12–24 month option rights",
                    3,
                    (
                        "Have counsel verify ownership, title exceptions, "
                        "mineral rights, easements, assignment permission, "
                        "extension pricing, and utility or zoning exit rights. "
                        "Document any recorded memorandum and distinguish "
                        "nonrefundable fees from refundable escrow deposits."
                    ),
                ),
                (
                    "Price documented development risk",
                    "Underwrite deliverable MW against remaining exposure",
                    4,
                    (
                        "Illustratively, 20 utility-documented MW at a negotiated "
                        "$5,000 per-MW milestone yields $100,000 before direct "
                        "costs. Price restudy exposure, energization delay, "
                        "expiration losses, and buyer conditions separately; "
                        "unvalidated MW supports no capacity-based value."
                    ),
                ),
                (
                    "Assign and reconcile receipts",
                    "Close eligible transfers with an evidence ledger",
                    5,
                    (
                        "Deliver the executed option chain, dated study package, "
                        "land-use findings, and contractual milestone evidence. "
                        "Recognize earned assignment fees, origination payments, "
                        "and realized carry without counting land price, "
                        "developer capex, deposits, or unrealized carry."
                    ),
                ),
            ],
        ),
        (
            "diag-02-nested-site-conversion-cohorts",
            "funnel",
            "One Cohort, Five Evidence Filters",
            "Every surviving site remains a subset of the original 120 parcels.",
            6,
            "illustrative_model",
            (
                "Illustrative mature annual cohort, not observed conversion "
                "performance or a 30-day sales forecast. Counts are sites, "
                "not MW. Track BESS and AI campus subcohorts separately even "
                "when reporting this combined funnel."
            ),
            (
                "Only three of 120 screened sites reach paid transfer or "
                "milestone status; rejected and expired sites still consume cash."
            ),
            [
                (
                    "Mapped candidate parcels",
                    "120 parcels entered with distinct asset classifications",
                    120,
                    (
                        "Capture parcel identifiers, ownership, corridor "
                        "distance, source dates, zoning district, and preliminary "
                        "hazards. Deduplicate adjoining tracts before assigning "
                        "one site identifier to a potential transaction."
                    ),
                ),
                (
                    "Fatal-flaw screen survivors",
                    "48 parcels survive the first desktop screen",
                    48,
                    (
                        "Forty percent of the original cohort survives access, "
                        "flood, wetland, mineral, and apparent zoning checks. "
                        "Mapped overlays are screening evidence rather than "
                        "jurisdictional determinations or final permits."
                    ),
                ),
                (
                    "Documented utility-path candidates",
                    "18 sites retain an actionable utility pathway",
                    18,
                    (
                        "Thirty-seven and one-half percent of the previous "
                        "stage receives sufficiently specific utility responses "
                        "to justify further diligence. Preliminary responses "
                        "remain explicitly conditional and do not establish "
                        "guaranteed deliverable capacity."
                    ),
                ),
                (
                    "Controlled diligence positions",
                    "Six sites secure assignable contingent option interests",
                    6,
                    (
                        "One-third of utility-path candidates reaches signed "
                        "site control. Apply option-fee caps and expiration "
                        "dates; the illustrative annual loss budget includes "
                        "three unsuccessful positions costing $16,000 each."
                    ),
                ),
                (
                    "Paid assignment or milestone sites",
                    "Three sites generate realized operator fee events",
                    3,
                    (
                        "Half of controlled positions produces paid events, "
                        "equal to 2.5 percent of the initial cohort. Multiple "
                        "distinct earned fee events may occur at one site; "
                        "never count the same contractual consideration twice."
                    ),
                ),
            ],
        ),
        (
            "diag-03-base-owner-profit-bridge",
            "waterfall",
            "Base-Case Revenue to Owner Profit",
            "$505,000 operator revenue less $292,900 costs equals $212,100.",
            3,
            "illustrative_model",
            (
                "USD annually. First and final bars are totals; the four "
                "intermediate bars are signed expense movements. Expense "
                "allocation is illustrative; canonical scenario totals are "
                "fixed. Conservative is $110,000 revenue at 30% margin, "
                "producing $33,000 profit with 1 FT + 3 C. Base is $505,000 "
                "at 42.0%, producing $212,100 with the same pod. Scaled is "
                "$900,000 at 54%, producing $486,000 with 2 FT + 4 C."
            ),
            (
                "505,000 − 132,000 − 80,000 − 48,000 − 32,900 = 212,100; "
                "212,100 / 505,000 = 42.0%. Underlying land purchases and "
                "developer construction spending never enter operator revenue."
            ),
            [
                (
                    "Recognized operator revenue",
                    "$505,000 annual earned fees and realized carry",
                    505000,
                    (
                        "Include only earned option assignments, per-MW "
                        "origination milestones, and realized development carry. "
                        "Where ASC 606 applies, assess principal versus agent "
                        "presentation; exclude third-party pass-through billings "
                        "when only the retained fee is operator revenue."
                    ),
                ),
                (
                    "Recurring pod operating expense",
                    "−$132,000 annual recurring delivery and overhead costs",
                    -132000,
                    (
                        "$11,000 monthly covers recurring contractor retainers, "
                        "software, insurance, administration, and sourcing. This "
                        "is the upper end of the canonical $1,800–$11,000 "
                        "monthly operating range; exclude the separate "
                        "project-specific charges below."
                    ),
                ),
                (
                    "Direct site diligence expense",
                    "−$80,000 project-specific technical and land diligence",
                    -80000,
                    (
                        "Allocate $36,000 to utility engineering and study "
                        "support, $24,000 to environmental and survey work, "
                        "and $20,000 to land-use and title investigation. "
                        "These expenses exclude recurring pod retainers."
                    ),
                ),
                (
                    "Expired option fee expense",
                    "−$48,000 recognized losses from unsuccessful site control",
                    -48000,
                    (
                        "Three failed positions at $16,000 each absorb "
                        "nonrefundable option and extension fees after utility "
                        "or zoning failure. Do not treat refundable deposits "
                        "as losses or capitalize expired rights indefinitely."
                    ),
                ),
                (
                    "Closed transaction expense",
                    "−$32,900 incremental closing and assignment delivery costs",
                    -32900,
                    (
                        "Allocate $18,000 to incremental transaction counsel, "
                        "$9,000 to licensed brokerage services where required, "
                        "and $5,900 to escrow, recording, and buyer-package "
                        "delivery. Exclude costs already charged to diligence."
                    ),
                ),
                (
                    "Annual owner net profit",
                    "$212,100 retained annual owner operating profit total",
                    212100,
                    (
                        "Final subtotal, not another upward movement. The "
                        "canonical model does not separately specify owner "
                        "salary or personal income taxes; do not describe "
                        "this amount as after-tax take-home cash."
                    ),
                ),
            ],
        ),
        (
            "diag-04-fee-rail-revenue-contribution",
            "horizontal_bars",
            "Five Fee Rails, One Base Revenue Total",
            "Compare annual earned dollar contributions rather than asset values.",
            2,
            "illustrative_model",
            (
                "Illustrative negotiated fee mix totaling $505,000. Bars "
                "measure annual recognized operator dollars, not market "
                "benchmarks, investment returns, or capacity commitments. "
                "The five fee events may span three successful sites."
            ),
            (
                "A payment rail earns its place only when its rights, "
                "milestone evidence, and payment trigger are separately documented."
            ),
            [
                (
                    "AI campus option assignment",
                    "$150,000 from one completed campus option assignment",
                    150000,
                    (
                        "One transferable principal-held option earns a "
                        "$150,000 assignment fee after buyer acceptance. "
                        "Verify campus zoning, carrier-confirmed dark-fiber "
                        "routes, cooling and water feasibility, and utility "
                        "service conditions; exclude the parcel purchase price."
                    ),
                ),
                (
                    "Standalone BESS option assignment",
                    "$125,000 from one completed storage parcel assignment",
                    125000,
                    (
                        "One assignable 5–25 acre storage parcel interest "
                        "earns $125,000. Document injection and charging "
                        "limitations, fire access, setbacks, interconnection "
                        "conditions, and transfer rights independently of "
                        "any nearby data-center development."
                    ),
                ),
                (
                    "Utility-evidenced MW milestone",
                    "$100,000 from twenty documented MW at $5,000",
                    100000,
                    (
                        "Twenty utility-documented deliverable MW multiplied "
                        "by a negotiated $5,000 milestone rate yields "
                        "$100,000 only upon the contractual earning event. "
                        "Attach upgrade exposure, study conditions, and "
                        "energization assumptions to the capacity statement."
                    ),
                ),
                (
                    "Development readiness milestone",
                    "$80,000 from one separately earned readiness payment",
                    80000,
                    (
                        "One $80,000 contractual milestone requires specified "
                        "land-use findings, access rights, and accepted "
                        "technical deliverables. A signed option or preliminary "
                        "queue entry alone does not satisfy that event."
                    ),
                ),
                (
                    "Realized development carry",
                    "$50,000 from one settled development carry distribution",
                    50000,
                    (
                        "Include $50,000 only after the carry crystallizes "
                        "under the applicable arrangement. Exclude speculative "
                        "future project appreciation, unearned promote value, "
                        "and consideration already included in another fee rail."
                    ),
                ),
            ],
        ),
        (
            "diag-05-preflight-rights-power-and-land",
            "decision_tree",
            "Four Checks Before Irreversible Option Spend",
            "Any failed check redirects the site to remediation or rejection.",
            5,
            "operating_framework",
            (
                "Four ordered decision nodes, each with a pass and stop "
                "outcome described in its detail. Federal and California "
                "citations identify concrete requirements; determine the "
                "actual state, local jurisdiction, utility tariff, and "
                "project-specific applicability for every parcel."
            ),
            (
                "Principal rights, utility evidence, land-use feasibility, "
                "and bounded downside must agree before pricing the assignment."
            ),
            [
                (
                    "Verify transaction role and rights",
                    "Proceed only with valid rights and role analysis",
                    1,
                    (
                        "Check California Business and Professions Code "
                        "sections 10130 and 10131 where applicable, or the "
                        "site state's corresponding statutes. Pass with a "
                        "valid principal option interest and supported "
                        "licensure analysis, or licensed broker participation; "
                        "stop if unlicensed activity or transfer defects remain."
                    ),
                ),
                (
                    "Validate utility service evidence",
                    "Proceed only with documented power and upgrade exposure",
                    2,
                    (
                        "Apply the relevant tariff and, where applicable, "
                        "18 CFR 35.28. Separate load-service requests from "
                        "storage interconnection requests. Pass when documented "
                        "MW, restudy exposure, upgrade responsibility, and "
                        "timing support the deal; stop when the thesis "
                        "depends only on line proximity or an unstudied filing."
                    ),
                ),
                (
                    "Resolve land-use and environmental barriers",
                    "Proceed only with a viable parcel-specific entitlement path",
                    3,
                    (
                        "Check adopted zoning text, active municipal "
                        "moratoriums, fire requirements, title, and mineral "
                        "rights. Evaluate Clean Water Act section 404 under "
                        "33 U.S.C. 1344 for covered discharges. Pass with "
                        "a documented path and priced conditions; stop for "
                        "prohibited use or an unresolved fatal site constraint."
                    ),
                ),
                (
                    "Bound expiration and delivery losses",
                    "Proceed only when downside fits available committed cash",
                    4,
                    (
                        "Stress delayed energization, network-upgrade restudy, "
                        "option expiration, buyer withdrawal, and extension "
                        "pricing. Confirm AI fiber and water requirements "
                        "separately from BESS needs. Pass within written "
                        "spending limits; renegotiate or reject uncapped "
                        "upgrade exposure and unaffordable option-fee burn."
                    ),
                ),
            ],
        ),
        (
            "diag-06-four-to-six-person-origination-pod",
            "org_architecture",
            "Four Core People, Two Explicit Scale Additions",
            "Base staffing is 1 FT + 3 C; scaled staffing is 2 FT + 4 C.",
            11,
            "operating_framework",
            (
                "Each stage represents one distinct person in the six-person "
                "scaled pod. The first four seats form the Conservative "
                "and Base pod; the final two are incremental scaled seats. "
                "C means contractor, not a full-time-equivalent commitment. "
                "External laboratories, survey firms, and escrow providers "
                "are purchased vendors rather than hidden pod employees."
            ),
            (
                "The principal owns underwriting and negotiations while "
                "specialists maintain independent technical and rights evidence."
            ),
            [
                (
                    "Principal and commercial lead",
                    "One full-time core owner leads transaction decisions",
                    1,
                    (
                        "Own sourcing priorities, option negotiation, developer "
                        "relationships, exposure limits, revenue recognition "
                        "coordination, and closing decisions. Keep purchase "
                        "price and construction budgets outside operator "
                        "fee reporting."
                    ),
                ),
                (
                    "GIS and land research specialist",
                    "One core contractor maintains parcel evidence quality",
                    1,
                    (
                        "Maintain QGIS parcel layers, FEMA overlays, wetland "
                        "screening, zoning citations, ownership records, and "
                        "source timestamps. Escalate conflicting records "
                        "instead of allowing automated screening to imply "
                        "verified capacity or final permitting."
                    ),
                ),
                (
                    "Utility and storage engineer",
                    "One core contractor validates technical power assumptions",
                    1,
                    (
                        "Interpret utility correspondence, study scope, "
                        "deliverable MW, charging profiles, upgrade allocation, "
                        "restudy sensitivity, and energization dependencies. "
                        "Distinguish preliminary technical estimates from "
                        "executed service commitments."
                    ),
                ),
                (
                    "Real-estate transaction counsel",
                    "One core contractor structures rights and transfer evidence",
                    1,
                    (
                        "Review principal status, applicable brokerage statutes, "
                        "title, option contingencies, assignment restrictions, "
                        "mineral protections, expiration notices, and closing "
                        "deliverables. Coordinate licensed brokerage services "
                        "where the transaction requires them."
                    ),
                ),
                (
                    "Development operations manager",
                    "One additional full-time person joins only at scale",
                    1,
                    (
                        "Own milestone calendars, buyer diligence requests, "
                        "study-document versioning, contractor schedules, and "
                        "receipt reconciliation. Add this seat for the "
                        "$900,000 scenario rather than silently increasing "
                        "the four-person Base workload."
                    ),
                ),
                (
                    "Land-use and environmental specialist",
                    "One additional contractor joins the scaled delivery pod",
                    1,
                    (
                        "Coordinate parcel-specific zoning, environmental "
                        "investigation, local fire access, water constraints, "
                        "and entitlement dependencies. The core pod buys "
                        "limited site-specific services before this recurring "
                        "scaled seat becomes justified."
                    ),
                ),
            ],
        ),
        (
            "diag-07-startup-capital-allocation",
            "stacked_comparison",
            "Preserve Runway Before Expanding Option Exposure",
            "Four buckets total a $30,000 startup plan inside the $10,000–$50,000 range.",
            4,
            "illustrative_model",
            (
                "Numeric values encode the $30,000 reference allocation. "
                "Each detail also supplies lean and expanded allocations "
                "totaling $10,000 and $50,000 respectively. These are "
                "starting cash envelopes, not annual expenses or funding "
                "for land acquisition, construction, or major utility deposits."
            ),
            (
                "Do not spend the entire startup reserve on option premiums; "
                "a 2–6 month first-deal cycle requires explicit runway planning."
            ),
            [
                (
                    "Parcel intelligence and sourcing",
                    "$4,500 reference allocation for targeted evidence gathering",
                    4500,
                    (
                        "Lean $1,500; reference $4,500; expanded $7,500. "
                        "Fund parcel records, targeted outreach, GIS support, "
                        "and corridor verification. Prioritize public utility "
                        "and county sources before purchasing broad datasets "
                        "that cannot establish site-specific power availability."
                    ),
                ),
                (
                    "Rights and initial diligence",
                    "$7,500 reference allocation for essential specialist investigation",
                    7500,
                    (
                        "Lean $2,500; reference $7,500; expanded $12,500. "
                        "Fund initial counsel, title research, utility "
                        "consultation, and land-use investigation. Full "
                        "interconnection studies and extensive fieldwork need "
                        "separately committed funding beyond this initial envelope."
                    ),
                ),
                (
                    "Contingent option fee exposure",
                    "$6,000 reference allocation for tightly limited site control",
                    6000,
                    (
                        "Lean $2,000; reference $6,000; expanded $10,000. "
                        "Cap initial nonrefundable fees and negotiate staged "
                        "payments with diligence exits. This startup exposure "
                        "is separate from the mature Base annual $48,000 "
                        "expired-option expense allowance."
                    ),
                ),
                (
                    "Operating runway reserve",
                    "$12,000 reference allocation for preserved operating liquidity",
                    12000,
                    (
                        "Lean $4,000; reference $12,000; expanded $20,000. "
                        "At $1,800 monthly overhead, $12,000 covers about "
                        "6.7 months; at $11,000 it covers about 1.1 months. "
                        "Reduce burn or secure additional committed capital "
                        "before adopting the Base cost structure."
                    ),
                ),
            ],
        ),
        (
            "diag-08-thirty-day-evidence-sprint",
            "timeline_roadmap",
            "Thirty Days to an Evidence-Based Option Decision",
            "Build a disciplined pipeline without pretending studies finish in one month.",
            12,
            "operating_framework",
            (
                "Numeric values are milestone ending days. Activity counts "
                "are operating targets, not utility response commitments "
                "or closing forecasts. The canonical first-deal window "
                "remains 2–6 months, subject to site and study dependencies."
            ),
            (
                "Finish the sprint with documented proceed, revise, or reject "
                "decisions and a funded next step, rather than unsupported MW claims."
            ),
            [
                (
                    "Days 1-7",
                    "Define two site theses and assemble forty candidates",
                    7,
                    (
                        "Create separate BESS and AI campus score sheets, "
                        "a QGIS evidence register, utility contact records, "
                        "and jurisdiction-specific zoning checklists. Record "
                        "69kV–345kV corridor signals without labeling "
                        "unstudied substations as available capacity."
                    ),
                ),
                (
                    "Days 8-14",
                    "Screen twelve priority parcels and initiate utility inquiries",
                    14,
                    (
                        "Investigate ownership, access, wetlands, flood "
                        "exposure, mineral rights, and municipal moratoriums. "
                        "Send site-specific load or storage profiles to "
                        "utilities; log unanswered requests as unresolved "
                        "dependencies rather than favorable technical findings."
                    ),
                ),
                (
                    "Days 15-21",
                    "Negotiate three contingent option structures with capped exposure",
                    21,
                    (
                        "Seek 12–24 month assignable terms, staged fees, "
                        "study access, extension pricing, and defined "
                        "diligence exits. Obtain carrier route evidence "
                        "for AI candidates and storage-specific charging "
                        "and fire-access findings for BESS candidates."
                    ),
                ),
                (
                    "Days 22-30",
                    "Prepare two buyer packages and decide next commitments",
                    30,
                    (
                        "Compile dated utility evidence, unresolved conditions, "
                        "upgrade sensitivity, energization ranges, option "
                        "rights, and expiration budgets. Authorize only "
                        "affordable next steps; defer capacity-based pricing "
                        "when utility documentation remains insufficient."
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
