from __future__ import annotations

VOLUME_028_SUBTITLE: str = (
    "The Complete Playbook for Commercial Cleaning Contracts: "
    "$250,000–$1,200,000 USD in Annual Contract Revenue, "
    "from a 5 FT + 4 C (9 People) Pod to an 11-Person Team"
)

VOLUME_028_POSITIONING_ALTERNATIVES: list[dict] = [
    {
        "title": "The Recurring Office Cleaning Contract Engine",
        "subtitle": (
            "Turn measured building scopes into profitable recurring routes "
            "with paid crew hours, inspection evidence, and disciplined billing."
        ),
        "audience": (
            "Local janitorial operators building dense office routes with "
            "five full-time employees and four genuine independent service providers."
        ),
        "research_basis": (
            "Federal minimum-wage, overtime, and time-record requirements make "
            "paid labor hours the core bidding input. Use task-specific ISSA "
            "production rates as estimating references, then replace assumptions "
            "with timed site observations. The cited statutes establish labor "
            "requirements, not achievable production rates or buyer demand."
        ),
        "sources": [
            "https://www.law.cornell.edu/uscode/text/29/206",
            "https://www.law.cornell.edu/uscode/text/29/207",
            "https://www.ecfr.gov/current/title-29/subtitle-B/chapter-V/subchapter-A/part-516",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Medical Office Cleaning Evidence System",
        "subtitle": (
            "Sell documented cleaning scopes, correct disinfectant use, "
            "and exposure-aware crews to outpatient facility buyers."
        ),
        "audience": (
            "Established commercial cleaners entering outpatient offices with "
            "trained supervisors, documented chemical handling, and bounded service scopes."
        ),
        "research_basis": (
            "OSHA Hazard Communication requirements govern covered workplace "
            "chemical hazards. The Bloodborne Pathogens standard applies where "
            "occupational exposure exists. Federal pesticide law prohibits "
            "registered-product use inconsistent with labeling, subject to statutory "
            "exceptions. These requirements support an evidence-led operating "
            "system; they do not establish a medical-cleaning price premium."
        ),
        "sources": [
            "https://www.ecfr.gov/current/title-29/subtitle-B/chapter-XVII/part-1910/section-1910.1200",
            "https://www.ecfr.gov/current/title-29/subtitle-B/chapter-XVII/part-1910/section-1910.1030",
            "https://www.law.cornell.edu/uscode/text/7/136j",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Supervisor-Pod Cleaning Business",
        "subtitle": (
            "Build a nine-person operating pod with explicit labor status, "
            "measured route capacity, and a controlled eleven-person expansion."
        ),
        "audience": (
            "Owner-operators replacing informal labor arrangements with documented "
            "employee roles, independently operated subcontract services, and accountable supervision."
        ),
        "research_basis": (
            "Employee status requires examination of the actual relationship. "
            "26 U.S.C. 3121(d)(2) addresses common-law employee status for "
            "employment taxes; 29 U.S.C. 203 supplies FLSA definitions. "
            "California Labor Code section 2775 establishes an ABC framework "
            "subject to statutory exceptions. A subcontract agreement alone "
            "does not resolve every applicable classification test."
        ),
        "sources": [
            "https://www.law.cornell.edu/uscode/text/26/3121",
            "https://www.law.cornell.edu/uscode/text/29/203",
            "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=2775.&lawCode=LAB",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
]


def build_volume_028_diagrams_data() -> list[dict]:
    specs = [
        (
            "diag-01-measured-scope-to-renewal",
            "process_flow",
            "Sell a Measured Scope, Then Prove Delivery",
            "Five operating stages for recurring commercial and medical janitorial contracts.",
            1,
            "operating_framework",
            (
                "Recognized operator revenue is earned cleaning contract revenue. "
                "Customer building value, tenant sales, and proposed contract value "
                "are excluded. Higher revenue requires additional paid productive "
                "crew hours, higher realized pricing, or both."
            ),
            (
                "The workflow connects the bid estimate to actual paid hours, "
                "documented service quality, invoicing, and renewal pricing."
            ),
            [
                (
                    "Qualify the route",
                    "Confirm buyer, location, frequency, and payment terms",
                    1.0,
                    (
                        "Record the facility manager, purchasing authority, building "
                        "address, service windows, invoice requirements, and travel "
                        "time from existing stops. Flag customer concentration "
                        "before adding a large account."
                    ),
                ),
                (
                    "Measure the scope",
                    "Inventory cleanable area and task-level service frequencies",
                    2.0,
                    (
                        "Walk the site with the buyer; count restrooms, fixtures, "
                        "floor types, touchpoints, waste stations, and restricted "
                        "rooms. Distinguish usable cleanable area from leased area "
                        "and separate periodic floor work from nightly service."
                    ),
                ),
                (
                    "Price paid capacity",
                    "Convert observed production into fully loaded labor costs",
                    3.0,
                    (
                        "Estimate area tasks as square feet divided by task-specific "
                        "ISSA production-rate references. Add fixture tasks, setup, "
                        "paid travel, inspections, breaks where required, and rework. "
                        "Validate with a timed pilot and include payroll burden, "
                        "overtime, supplies, overhead, and target profit."
                    ),
                ),
                (
                    "Mobilize and inspect",
                    "Assign qualified labor and capture completed-task evidence",
                    4.0,
                    (
                        "Use Swept or a comparable scheduling and inspection system "
                        "to assign employee work, record exceptions, and track "
                        "corrective actions. Independently operated subcontractors "
                        "deliver contracted outcomes under their own lawful methods."
                    ),
                ),
                (
                    "Bill and renew",
                    "Reconcile accepted services, collection timing, and account margin",
                    5.0,
                    (
                        "Issue QuickBooks invoices against contracted service periods "
                        "and approved extras. Compare actual hours with the bid "
                        "weekly; correct scope creep, repeated callbacks, and slow "
                        "payment before the next renewal."
                    ),
                ),
            ],
        ),
        (
            "diag-02-local-account-conversion-cohort",
            "funnel",
            "One Prospect Cohort, Five Measurable Conversions",
            "Illustrative account counts; every downstream account belongs to the original cohort.",
            6,
            "illustrative_model",
            (
                "Follow 200 unique local accounts for up to 120 days, consistent "
                "with a one-to-four-month first-deal planning range. Counts are "
                "illustrative, not market benchmarks or annual revenue projections. "
                "Referred or newly discovered accounts enter separate cohorts."
            ),
            (
                "The cohort narrows from 200 researched accounts to five activated "
                "contracts: 2.5% overall conversion without mixing leads and locations."
            ),
            [
                (
                    "Researched accounts",
                    "200 unique accounts matching the service territory",
                    200.0,
                    (
                        "Deduplicate legal buyers and document facility type, route "
                        "distance, estimated cleaning frequency, and a reachable "
                        "purchasing contact before counting an account."
                    ),
                ),
                (
                    "Qualified conversations",
                    "80 accounts with confirmed need and purchasing access",
                    80.0,
                    (
                        "Forty percent of the original accounts confirm a relevant "
                        "service need, a buyer contact, and a plausible buying "
                        "window. Email opens and unanswered calls do not qualify."
                    ),
                ),
                (
                    "Completed walkthroughs",
                    "40 accounts with measured sites and service requirements",
                    40.0,
                    (
                        "Fifty percent of qualified conversations produce a completed "
                        "site inspection with task inventory, access conditions, "
                        "existing service problems, and invoice requirements."
                    ),
                ),
                (
                    "Delivered proposals",
                    "20 accounts receive costed and capacity-checked proposals",
                    20.0,
                    (
                        "Fifty percent of walkthrough accounts receive priced scopes "
                        "after labor-hour costing and route review. Decline work "
                        "that cannot cover required wages and delivery costs."
                    ),
                ),
                (
                    "Activated contracts",
                    "Five accounts sign and begin accepted service",
                    5.0,
                    (
                        "Twenty-five percent of proposed accounts sign and start "
                        "service within the observation window. Track deposits, "
                        "earned revenue, invoiced receivables, and cash collections "
                        "separately."
                    ),
                ),
            ],
        ),
        (
            "diag-03-base-case-revenue-to-owner-net",
            "waterfall",
            "$725,000 Contract Revenue to $87,000 Owner Net",
            "Six bars reconcile the Base-Case annual operating result to a 12.0% net margin.",
            3,
            "illustrative_model",
            (
                "USD per year. The first and last bars are absolute totals; "
                "the four middle bars are negative movements. Intermediate "
                "balances are $290,000, $246,500, $166,750, and $87,000. "
                "Cost categories are an illustrative allocation, not additional "
                "canonical scorecard inputs. Owner net is the operating residual "
                "before owner-specific income taxes."
            ),
            (
                "$725,000 minus $435,000 minus $43,500 minus $79,750 minus "
                "$79,750 equals $87,000. Costs total $638,000, or 88.0% "
                "of revenue; owner net equals 12.0%. The stated $4,000–$18,000 "
                "monthly opex range cannot serve as an all-in cost ceiling "
                "for this scenario; its coverage must be reconciled before bidding."
            ),
            [
                (
                    "Earned contract revenue",
                    "$725,000 annual cleaning service revenue; opening total",
                    725000.0,
                    (
                        "Use the canonical Base-Case gross revenue for completed "
                        "cleaning services. Exclude sales taxes collected for "
                        "remittance and customer business turnover."
                    ),
                ),
                (
                    "Direct service labor",
                    "Subtract $435,000 for paid delivery labor and burden",
                    -435000.0,
                    (
                        "Allocate 60.0% of revenue to field employee wages, employer "
                        "payroll charges, field workers' compensation, paid travel, "
                        "overtime, callbacks, and legitimate subcontract service "
                        "invoices. Remaining balance: $290,000."
                    ),
                ),
                (
                    "Supplies and equipment",
                    "Subtract $43,500 for chemicals, consumables, and equipment",
                    -43500.0,
                    (
                        "Allocate 6.0% of revenue to cleaning chemicals, liners, "
                        "microfiber replacement, equipment rental or depreciation, "
                        "and repairs. Keep equipment purchase cash flows separate "
                        "from annual expense recognition. Remaining balance: $246,500."
                    ),
                ),
                (
                    "Supervision and operations",
                    "Subtract $79,750 for oversight and shared operating costs",
                    -79750.0,
                    (
                        "Allocate 11.0% of revenue to supervisor compensation and "
                        "burden, management work, vehicles, storage, general liability, "
                        "and inspection systems. Assign each payroll hour once; "
                        "exclude field labor already charged above. Remaining "
                        "balance: $166,750."
                    ),
                ),
                (
                    "Selling and administration",
                    "Subtract $79,750 for acquisition, billing, and administration",
                    -79750.0,
                    (
                        "Allocate 11.0% of revenue to estimating, account sales, "
                        "administrative compensation and burden, accounting, payment "
                        "fees, bad-debt expense, and other operating expenses. "
                        "Include compensation for owner work where applicable "
                        "before calculating residual profit. Remaining balance: $87,000."
                    ),
                ),
                (
                    "Annual owner net",
                    "$87,000 residual owner profit; closing total at 12.0%",
                    87000.0,
                    (
                        "Render this bar from zero, not as another positive "
                        "movement. Preserve the other canonical scenarios: "
                        "$250,000 at 8.0% yields $20,000; $1,200,000 at "
                        "16.0% yields $192,000."
                    ),
                ),
            ],
        ),
        (
            "diag-04-sub-niche-contribution-per-paid-hour",
            "horizontal_bars",
            "Compare Contribution per Paid Service Hour",
            "Five illustrative sub-niche bids after direct delivery costs, before shared overhead.",
            2,
            "illustrative_model",
            (
                "All values are USD contribution per paid service hour, not "
                "net margin percentages or published market rates. Revenue "
                "equivalent equals contract revenue divided by all attributable "
                "paid service hours. Direct cost includes loaded field labor, "
                "routine consumables, and service-specific equipment. Shared "
                "supervision, sales, administration, and owner net remain outside "
                "these bars."
            ),
            (
                "Rank measured account economics rather than building labels. "
                "Extra dwell time, access delays, overtime, and rework can "
                "erase a nominal medical or industrial price premium."
            ),
            [
                (
                    "Outpatient medical offices",
                    "$14 contribution from $52 revenue less $38 direct cost",
                    14.0,
                    (
                        "Model label contact times, isolation-area restrictions, "
                        "PPE, and exposure-related training in paid hours. "
                        "Do not price regulated waste handling into an ordinary "
                        "janitorial scope without the required operating capability."
                    ),
                ),
                (
                    "Light industrial offices",
                    "$12 contribution from $48 revenue less $36 direct cost",
                    12.0,
                    (
                        "Limit the modeled scope to offices and agreed common "
                        "areas. Separately quote production-floor work, machinery "
                        "proximity, unusual soils, and site-specific safety training."
                    ),
                ),
                (
                    "Professional office suites",
                    "$11 contribution from $44 revenue less $33 direct cost",
                    11.0,
                    (
                        "Cluster nearby suites to reduce paid travel. Measure "
                        "desk density, restroom fixtures, alarm procedures, elevator "
                        "delays, and tenant-requested extras rather than bidding "
                        "from square footage alone."
                    ),
                ),
                (
                    "Multitenant common areas",
                    "$11 contribution from $46 revenue less $35 direct cost",
                    11.0,
                    (
                        "Specify lobby appearance standards, restroom replenishment, "
                        "public access windows, and weekend attendance. Separate "
                        "tenant-private cleaning from property-manager common-area "
                        "obligations to prevent unpaid scope expansion."
                    ),
                ),
                (
                    "Private education facilities",
                    "$8 contribution from $40 revenue less $32 direct cost",
                    8.0,
                    (
                        "Price restroom intensity, event resets, safeguarding-related "
                        "access procedures, and academic calendar changes. Quote "
                        "summer floor restoration separately and confirm whether "
                        "monthly billing continues through closures."
                    ),
                ),
            ],
        ),
        (
            "diag-05-preflight-labor-chemical-and-contract-checks",
            "decision_tree",
            "Four Checks Before Assigning a Crew",
            "Each failed check routes to a specific correction before the affected work starts.",
            5,
            "operating_framework",
            (
                "Read nodes in order. Each numeric value is a sequence index, "
                "not a risk score or probability. Apply federal requirements "
                "alongside applicable state and local rules. Insurance limits "
                "depend on jurisdiction, policy terms, and the buyer's contract."
            ),
            (
                "A signed cleaning agreement does not cure underpaid labor, "
                "misclassification, unsafe chemical use, or uninsured scope."
            ),
            [
                (
                    "Wages and paid time",
                    "Pass to classification; otherwise recost and correct payroll",
                    1.0,
                    (
                        "Apply 29 U.S.C. 206 and 207 to covered workers, "
                        "including overtime for covered nonexempt employees. "
                        "Keep required records under 29 CFR Part 516 and "
                        "evaluate compensable time under 29 CFR Part 785. "
                        "Capture intersite travel and setup; apply higher "
                        "applicable state or local wage requirements."
                    ),
                ),
                (
                    "Actual worker relationship",
                    "Pass to chemical review; otherwise redesign or employ",
                    2.0,
                    (
                        "Evaluate actual control and economic facts under applicable "
                        "FLSA, tax, and state tests, including 26 U.S.C. "
                        "3121(d)(2) and California Labor Code section 2775 "
                        "where relevant. A 1099 form, LLC, or insurance "
                        "certificate alone does not establish independent status."
                    ),
                ),
                (
                    "Chemical and exposure controls",
                    "Pass to contract review; otherwise train and correct methods",
                    3.0,
                    (
                        "Implement applicable 29 CFR 1910.1200 labeling, safety "
                        "data sheets, written program, and training requirements. "
                        "Follow disinfectant labeling under 7 U.S.C. 136j. "
                        "Where occupational exposure exists, implement 29 CFR "
                        "1910.1030 controls; do not assign untrained workers "
                        "to sharps or blood cleanup."
                    ),
                ),
                (
                    "Insured and bounded scope",
                    "Start covered work only after resolving identified coverage gaps",
                    4.0,
                    (
                        "Confirm required workers' compensation and buyer-specified "
                        "liability coverage with the broker. Review exclusions, "
                        "endorsements, key loss, property damage, and medical-site "
                        "activities. Attach service frequencies, inspection standards, "
                        "change-order pricing, payment terms, and termination rights "
                        "to the signed agreement."
                    ),
                ),
            ],
        ),
        (
            "diag-06-nine-seat-pod-with-two-seat-expansion",
            "org_architecture",
            "Nine Active Seats, Two Explicit Expansion Seats",
            "Base: 5 FT + 4 C. Scaled: 6 FT + 5 C.",
            11,
            "operating_framework",
            (
                "Numeric values indicate Base-Case active seats: nine ones "
                "and two zeros. Activate both zero-valued seats only in "
                "the Scaled scenario. FT denotes full-time employee seats; "
                "C denotes one-person independent service-provider seats, "
                "subject to applicable classification tests. Headcount is "
                "not a full-time-equivalent measure."
            ),
            (
                "Conservative: $250,000 revenue and $20,000 owner net with "
                "nine people. Base: $725,000 revenue and $87,000 owner net "
                "with nine people. Scaled: $1,200,000 revenue and $192,000 "
                "owner net with eleven people. These are separate operating "
                "scenarios, not proof that two hires alone produce the revenue "
                "increase. Validate paid hours, utilization, pricing, and route "
                "capacity before accepting added work."
            ),
            [
                (
                    "FT 1: pod supervisor",
                    "One active employee owning delivery quality and coverage",
                    1.0,
                    (
                        "Own employee scheduling, site mobilization, inspection "
                        "review, supply readiness, and absence coverage. Maintain "
                        "a weekly bid-hours-versus-actual-hours report for each account."
                    ),
                ),
                (
                    "FT 2: working lead",
                    "One active employee leading the primary recurring route",
                    1.0,
                    (
                        "Perform cleaning while coaching employee task sequencing, "
                        "checking lockup procedures, and documenting exceptions. "
                        "Record supervisory and field time separately for costing."
                    ),
                ),
                (
                    "FT 3: route cleaner",
                    "One active employee serving measured recurring office scopes",
                    1.0,
                    (
                        "Execute assigned office cleaning tasks and record actual "
                        "service time. Escalate access delays, excess waste, "
                        "missing consumables, and out-of-scope requests immediately."
                    ),
                ),
                (
                    "FT 4: route cleaner",
                    "One active employee serving trained medical-office scopes",
                    1.0,
                    (
                        "Follow site-specific task lists, product labeling, and "
                        "required exposure controls. Log missed rooms and corrective "
                        "actions without capturing patient records in inspection photographs."
                    ),
                ),
                (
                    "FT 5: account operations",
                    "One active employee owning estimates, billing, and renewals",
                    1.0,
                    (
                        "Maintain the prospect cohort, proposal costing, customer "
                        "purchase-order details, invoice follow-up, and renewal "
                        "calendar. If the owner fills this seat, include "
                        "their work compensation before residual owner net."
                    ),
                ),
                (
                    "C 1: floor-care provider",
                    "One active independent provider delivering bounded floor projects",
                    1.0,
                    (
                        "Contract for defined floor-care outcomes with an independently "
                        "operated provider using appropriate equipment and methods. "
                        "Verify insurance, competence, scheduling interfaces, and "
                        "classification under the actual working arrangement."
                    ),
                ),
                (
                    "C 2: carpet-care provider",
                    "One active independent provider delivering scheduled extraction projects",
                    1.0,
                    (
                        "Purchase scoped carpet extraction outcomes with documented "
                        "drying requirements, access windows, and property protection. "
                        "Do not disguise an employee cleaner's regular controlled "
                        "shift as a specialist subcontract."
                    ),
                ),
                (
                    "C 3: interior-glass provider",
                    "One active independent provider delivering scoped glass services",
                    1.0,
                    (
                        "Define reachable interior-glass surfaces, frequency, and "
                        "acceptance evidence. Exclude elevated-access work unless "
                        "the provider has suitable equipment, training, insurance, "
                        "and an expressly priced scope."
                    ),
                ),
                (
                    "C 4: project-cleaning provider",
                    "One active independent provider delivering separate periodic projects",
                    1.0,
                    (
                        "Use independently priced deep-cleaning projects with bounded "
                        "deliverables rather than employee-style fill-in shifts. "
                        "For controlled shift coverage, use an appropriate employee "
                        "arrangement and revise the staffing plan."
                    ),
                ),
                (
                    "FT 6: scaled route cleaner",
                    "Zero Base seats; activate one employee for Scaled capacity",
                    0.0,
                    (
                        "Add this sixth employee only against measured recurring "
                        "paid-hour demand and adequate collection funding. Recalculate "
                        "supervisor coverage and overtime exposure before expanding "
                        "the route."
                    ),
                ),
                (
                    "C 5: scaled specialist provider",
                    "Zero Base seats; activate one independent provider when justified",
                    0.0,
                    (
                        "Add a fifth genuine provider for separately scoped "
                        "specialist demand. The illustrated headcount assumes each "
                        "provider is one person; count additional people explicitly "
                        "if a subcontract business deploys a larger crew."
                    ),
                ),
            ],
        ),
        (
            "diag-07-startup-cash-allocation",
            "stacked_comparison",
            "Allocate Launch Cash Before Buying Capacity",
            "Four buckets reconcile lean, reference, and expanded startup budgets.",
            4,
            "illustrative_model",
            (
                "Numeric values encode the $45,000 reference stack only. "
                "The value text supplies comparable $15,000 lean and "
                "$90,000 expanded stacks in the same bucket order. "
                "These are startup cash allocations, not annual expenses "
                "or revenue scenarios. Do not stack all three budgets together."
            ),
            (
                "Lean: $4,500 + $2,000 + $1,000 + $7,500 = $15,000. "
                "Reference: $12,000 + $5,000 + $3,000 + $25,000 = $45,000. "
                "Expanded: $22,000 + $10,000 + $6,000 + $52,000 = $90,000. "
                "A lean launch uses existing transport and staged hiring; "
                "none of these budgets proves runway for nine simultaneous starts."
            ),
            [
                (
                    "Equipment and initial supplies",
                    "Lean $4,500; reference $12,000; expanded $22,000 equipment cash",
                    12000.0,
                    (
                        "Fund commercial vacuums, carts, microfiber systems, PPE, "
                        "dispensers, and initial chemicals. Rent infrequent specialty "
                        "machines until contracted utilization supports ownership. "
                        "Avoid duplicating client-provided equipment in the budget."
                    ),
                ),
                (
                    "Setup and coverage deposits",
                    "Lean $2,000; reference $5,000; expanded $10,000 setup cash",
                    5000.0,
                    (
                        "Reserve cash for registration, required local licensing, "
                        "insurance deposits, contract preparation, and initial safety "
                        "training. Replace estimates with jurisdiction-specific fees "
                        "and written broker quotations before committing funds."
                    ),
                ),
                (
                    "Acquisition and operating systems",
                    "Lean $1,000; reference $3,000; expanded $6,000 acquisition cash",
                    3000.0,
                    (
                        "Fund a focused website, local prospect research, walkthrough "
                        "travel, estimating setup, Swept onboarding, and QuickBooks "
                        "configuration. Limit subscription seats and advertising "
                        "commitments until the first route converts."
                    ),
                ),
                (
                    "Payroll and collection buffer",
                    "Lean $7,500; reference $25,000; expanded $52,000 liquidity",
                    25000.0,
                    (
                        "Hold unspent cash for wages, payroll charges, subcontract "
                        "invoices, and collection delays. At Base-Case direct labor "
                        "of $435,000 yearly, $25,000 covers about three weeks "
                        "of direct labor alone; stage mobilization and model "
                        "all other cash outflows separately."
                    ),
                ),
            ],
        ),
        (
            "diag-08-first-thirty-days-execution",
            "timeline_roadmap",
            "Thirty Days to a Measured, Bid-Ready Operation",
            "Four weekly milestones establish demand evidence, delivery economics, and launch readiness.",
            12,
            "operating_framework",
            (
                "Numeric values are milestone end days: 7, 14, 21, and 30. "
                "A first signed deal may take one to four months. "
                "The sprint builds a qualified pipeline and costed delivery "
                "system; service starts only when an actual customer contract "
                "and ready capacity support them."
            ),
            (
                "Use evidence at each milestone: named accounts, measured "
                "walkthroughs, reconciled bids, and a funded mobilization plan. "
                "Scheduling, inspection logs, and billing reduce administration "
                "but do not replace paid cleaning hours."
            ),
            [
                (
                    "Days 1-7",
                    "Choose the territory and establish costed operating boundaries",
                    7.0,
                    (
                        "Select one dense office or outpatient cluster, research "
                        "40 named buyer accounts, obtain insurance quotations, "
                        "and document applicable wage and classification rules. "
                        "Build the first loaded hourly-cost worksheet and "
                        "choose the startup cash envelope."
                    ),
                ),
                (
                    "Days 8-14",
                    "Conduct walkthroughs and test task-level production assumptions",
                    14.0,
                    (
                        "Target three completed walkthroughs where buyers agree "
                        "to participate. Record cleanable area, fixtures, access, "
                        "and frequencies; perform an authorized timed pilot. "
                        "Use ISSA references only as initial estimates and "
                        "retain observed paid-hour evidence."
                    ),
                ),
                (
                    "Days 15-21",
                    "Issue reconciled proposals and verify deliverable labor capacity",
                    21.0,
                    (
                        "Target two complete proposals supported by measured scopes. "
                        "Test overtime, route travel, supplies, payment delays, "
                        "and customer concentration. Confirm employee availability "
                        "and separately scoped provider capability without "
                        "committing unfunded payroll."
                    ),
                ),
                (
                    "Days 22-30",
                    "Prepare mobilization and continue documented buyer follow-up",
                    30.0,
                    (
                        "Configure scheduling, inspection forms, invoice templates, "
                        "chemical records, and site-access controls. If a contract "
                        "is signed, confirm coverage and training before service. "
                        "Otherwise continue the same prospect cohort into months "
                        "two through four without recording proposed sales as revenue."
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
