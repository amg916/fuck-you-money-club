from __future__ import annotations

VOLUME_034_SUBTITLE = (
    "The Complete Playbook for NEMT & Medical Courier Dispatch Arbitrage: "
    "$250,000–$1,600,000 USD in Annual Gross Billings with a "
    "2 FT + 2 C (4 People) Core Pod, Scaling to Six"
)

VOLUME_034_POSITIONING_ALTERNATIVES = [
    {
        "title": "The Standing-Order Dispatch Desk",
        "subtitle": (
            "Build recurring NEMT dispatch around authorized Medicaid and "
            "workers'-comp trips, verified performance, and disciplined collections."
        ),
        "audience": (
            "Healthcare logistics operators coordinating credentialed transport "
            "providers without purchasing a vehicle fleet."
        ),
        "research_basis": (
            "42 CFR 431.53 addresses Medicaid transportation assurance; "
            "42 CFR 440.170(a) addresses transportation services. These provisions "
            "support the service context, not automatic broker enrollment or "
            "payment. State Medicaid manuals, broker contracts, and workers'-comp "
            "payer agreements determine authorization, documentation, and rates."
        ),
        "sources": [
            "https://www.law.cornell.edu/cfr/text/42/431.53",
            "https://www.law.cornell.edu/cfr/text/42/440.170",
            "https://www.law.cornell.edu/uscode/text/42/1396a",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Barcode-to-Bench Courier Desk",
        "subtitle": (
            "Coordinate recurring laboratory routes and contracted STAT coverage "
            "with barcode custody events, validated packaging, and exception ownership."
        ),
        "audience": (
            "Courier dispatch teams serving laboratories, collection sites, and "
            "clinical networks through qualified owner-operator capacity."
        ),
        "research_basis": (
            "42 CFR 493.1242 requires laboratory specimen-handling procedures; "
            "49 CFR 173.199 governs applicable Category B infectious-substance "
            "shipments. OSHA exposure controls and HIPAA business-associate "
            "requirements depend on actual work and information handling. "
            "CLIA duties belong to the laboratory; courier service alone does "
            "not establish a laboratory certification requirement."
        ),
        "sources": [
            "https://www.law.cornell.edu/cfr/text/42/493.1242",
            "https://www.law.cornell.edu/cfr/text/49/173.199",
            "https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.1030",
            "https://www.law.cornell.edu/cfr/text/45/164.504",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Asset-Light Healthcare Logistics Pod",
        "subtitle": (
            "Separate driver settlements, retained dispatch contribution, and "
            "owner profit while scaling a four-person desk to six."
        ),
        "audience": (
            "Owner-led brokerage teams combining NEMT standing orders and "
            "laboratory courier contracts with outsourced transport capacity."
        ),
        "research_basis": (
            "29 U.S.C. 203 and applicable state labor tests require classification "
            "based on actual relationships rather than contract labels. California "
            "Labor Code section 2775 illustrates state-specific constraints. "
            "HIPAA business-associate provisions shape dispatch data handling; "
            "these sources do not establish commercial yields or market demand."
        ),
        "sources": [
            "https://www.law.cornell.edu/uscode/text/29/203",
            "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=2775.&lawCode=LAB",
            "https://www.law.cornell.edu/cfr/text/45/164.502",
            "https://www.law.cornell.edu/cfr/text/45/164.504",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
]


def build_volume_034_diagrams_data() -> list[dict]:
    specs = [
        (
            "diag-01-order-to-cash-dispatch",
            "process_flow",
            "One Order, One Evidence Trail, One Settlement",
            "Separate passenger transport and specimen handling within one dispatch desk.",
            1,
            "operating_framework",
            (
                "The pod coordinates contracted providers rather than owning a fleet. "
                "Passenger trips and specimen movements require separate service "
                "rules, escalation procedures, and evidence packets."
            ),
            (
                "Close each assignment only after reconciling authorization, "
                "performance evidence, payer billing, and provider settlement."
            ),
            [
                (
                    "Validate the contracted order",
                    "Confirm payer, service scope, authorization, and collection terms",
                    1.0,
                    (
                        "For NEMT, verify member eligibility, authorized transport "
                        "level, destination, and standing-order validity. For courier "
                        "work, verify specimen class, receiving hours, packaging "
                        "responsibility, and contracted pickup deadline."
                    ),
                ),
                (
                    "Match qualified transport capacity",
                    "Assign an eligible provider with documented backup coverage",
                    2.0,
                    (
                        "Check driver credentials, vehicle suitability, insurance, "
                        "service-area limits, and exclusions. A signed owner-operator "
                        "agreement does not resolve worker classification."
                    ),
                ),
                (
                    "Dispatch and capture service events",
                    "Record timestamped pickup, movement, delivery, and exceptions",
                    3.0,
                    (
                        "Use RouteGenie or MediRoutes for configured NEMT GPS events. "
                        "Use barcode custody records for specimens; escalate missed "
                        "STAT pickups to the named laboratory contact immediately."
                    ),
                ),
                (
                    "Build the payer evidence packet",
                    "Reconcile ordered service against completed service before billing",
                    4.0,
                    (
                        "Scrub 837P claims only where the payer requires that format; "
                        "otherwise submit the contracted broker file or courier "
                        "invoice. Attach required trip verification or custody evidence."
                    ),
                ),
                (
                    "Collect, settle, and reconcile",
                    "Track receivables separately from provider payment obligations",
                    5.0,
                    (
                        "Forecast Medicaid broker Net-30/45 collection exposure "
                        "against settlement dates. Under the canonical model, "
                        "55% of gross billings funds drivers and 45% remains "
                        "before pod costs and owner profit."
                    ),
                ),
            ],
        ),
        (
            "diag-02-qualified-account-conversion",
            "funnel",
            "Convert a Defined Account Cohort",
            "One hundred target accounts narrow to five signed service accounts.",
            6,
            "illustrative_model",
            (
                "Illustrative counts follow one account cohort across a complete "
                "sales cycle; they are not observed conversion benchmarks. Every "
                "later stage is a subset of the preceding stage. First-deal "
                "planning remains 2–5 months, not one sprint."
            ),
            (
                "Count accounts consistently: route reviews, proposals, and awards "
                "refer to the same original account list."
            ),
            [
                (
                    "Mapped target accounts",
                    "100 accounts with named purchasing or transport contacts",
                    100.0,
                    (
                        "Build a deduplicated list of Medicaid transport brokers, "
                        "workers'-comp administrators, laboratories, and collection "
                        "networks within the service territory."
                    ),
                ),
                (
                    "Qualified service fit",
                    "60 accounts pass territory, service, and payer screening",
                    60.0,
                    (
                        "Retain 60% of the original cohort after confirming "
                        "outsourcing demand, procurement access, credentialing "
                        "requirements, and feasible payment terms."
                    ),
                ),
                (
                    "Documented route discovery",
                    "30 accounts share usable service and exception requirements",
                    30.0,
                    (
                        "Advance 50% of qualified accounts after receiving trip "
                        "windows, route density, transport levels, specimen needs, "
                        "or other service-specific workload evidence."
                    ),
                ),
                (
                    "Costed proposals delivered",
                    "15 accounts receive capacity-backed pricing and service terms",
                    15.0,
                    (
                        "Advance 50% of discovery accounts after pricing driver "
                        "settlements, deadhead, standby coverage, failed pickups, "
                        "and collection timing."
                    ),
                ),
                (
                    "Signed service accounts",
                    "5 accounts execute scoped contracts with operating contacts",
                    5.0,
                    (
                        "Convert one-third of proposals and 5% of the original "
                        "cohort. Signing does not equal dispatch readiness, recognized "
                        "revenue, or collected cash."
                    ),
                ),
            ],
        ),
        (
            "diag-03-base-case-billings-to-profit",
            "waterfall",
            "Base Case: $925,000 Gross to $166,500 Owner Profit",
            "Six bars distinguish billings, retained contribution, costs, and profit.",
            3,
            "illustrative_model",
            (
                "Annual USD. Opening, retained subtotal, and closing bars are "
                "absolute totals; negative bars are deductions. Retained share "
                "is 45%. The two pod-cost allocations are illustrative splits "
                "of the canonical $249,750 residual operating cost."
            ),
            (
                "$925,000 − $508,750 = $416,250 retained; $416,250 − $120,000 "
                "− $129,750 = $166,500 profit. Profit is 18.0% of gross "
                "billings and 40.0% of retained revenue."
            ),
            [
                (
                    "Opening gross contracted billings",
                    "$925,000 annual customer billings before driver settlements",
                    925000.0,
                    (
                        "Opening total: NEMT brokerage and medical courier "
                        "service billings, excluding underlying healthcare "
                        "charges and any unrelated client transaction volume."
                    ),
                ),
                (
                    "Deduct external driver settlements",
                    "−$508,750 paid to contracted transport delivery providers",
                    -508750.0,
                    (
                        "Deduction: 55% of gross billings compensates the external "
                        "transport network. These providers are separate from "
                        "the four-person administrative and dispatch pod."
                    ),
                ),
                (
                    "Retained dispatch revenue subtotal",
                    "$416,250 retained under the canonical 45% share",
                    416250.0,
                    (
                        "Absolute subtotal, not another inflow. This model uses "
                        "the specified ASC 606 agent presentation; actual net "
                        "presentation requires a contract-specific principal-agent "
                        "assessment and is not established by the percentage alone."
                    ),
                ),
                (
                    "Deduct full-time pod seat costs",
                    "−$120,000 allocated to two full-time operating seats",
                    -120000.0,
                    (
                        "Deduction: illustrative combined compensation and "
                        "employment burden for the two full-time seats. If the "
                        "owner fills a seat, keep seat compensation distinct "
                        "from the residual owner-profit line."
                    ),
                ),
                (
                    "Deduct remaining pod operating costs",
                    "−$129,750 covers contractor seats and other operating expenses",
                    -129750.0,
                    (
                        "Deduction: illustrative aggregate for two contractor "
                        "seats, dispatch software, insurance, billing support, "
                        "credentialing, administration, and service exceptions. "
                        "Do not deduct driver settlements a second time."
                    ),
                ),
                (
                    "Closing annual owner net profit",
                    "$166,500 equals 18.0% gross and 40.0% retained margin",
                    166500.0,
                    (
                        "Closing total: canonical Base-Case annual owner profit. "
                        "Working-capital funding is a cash requirement rather "
                        "than an additional expense automatically deducted here."
                    ),
                ),
            ],
        ),
        (
            "diag-04-service-rail-retained-yields",
            "horizontal_bars",
            "Compare Retained Dollars per Completed Assignment",
            "Five service examples use the same 45% retained-share assumption.",
            2,
            "illustrative_model",
            (
                "Synthetic pricing examples, not fee schedules or market quotes. "
                "Each bar measures USD retained before pod overhead for one "
                "completed one-way trip or one defined courier run. Assignment "
                "duration and mileage differ, so bars do not rank hourly returns."
            ),
            (
                "Apply the contracted unit definition before comparing yield; "
                "a courier run and a passenger trip are not interchangeable units."
            ),
            [
                (
                    "Medicaid broker ambulatory trip",
                    "$31.50 retained from a $70 completed one-way trip",
                    31.5,
                    (
                        "$70 gross less $38.50 driver settlement leaves $31.50. "
                        "Use broker authorization and trip-log rules; disputed "
                        "eligibility or missing GPS evidence can erase collection."
                    ),
                ),
                (
                    "Medicaid broker wheelchair trip",
                    "$54 retained from a $120 completed one-way trip",
                    54.0,
                    (
                        "$120 gross less $66 driver settlement leaves $54. "
                        "Verify vehicle equipment, securement capability, passenger "
                        "assistance requirements, and the authorized transport level."
                    ),
                ),
                (
                    "Workers'-comp administrator trip",
                    "$45 retained from a $100 completed one-way trip",
                    45.0,
                    (
                        "$100 gross less $55 driver settlement leaves $45. "
                        "Confirm administrator authorization and contracted wait-time "
                        "rules rather than importing Medicaid billing assumptions."
                    ),
                ),
                (
                    "Scheduled laboratory courier run",
                    "$40.50 retained from a $90 defined collection run",
                    40.5,
                    (
                        "$90 gross less $49.50 driver settlement leaves $40.50. "
                        "Specify included stops, receiving cutoffs, packaging "
                        "responsibility, and custody-event evidence in the route scope."
                    ),
                ),
                (
                    "Contracted STAT specimen run",
                    "$81 retained from a $180 defined urgent run",
                    81.0,
                    (
                        "$180 gross less $99 driver settlement leaves $81. "
                        "Price backup availability and deadline exposure; higher "
                        "dollars per run do not establish better utilization."
                    ),
                ),
            ],
        ),
        (
            "diag-05-preflight-statutory-risk-checks",
            "decision_tree",
            "Four Checks Before Accepting a Live Assignment",
            "A failed applicable check routes the order to remediation, not dispatch.",
            5,
            "operating_framework",
            (
                "Apply checks in sequence to the actual service. Passenger-only "
                "work does not inherit specimen-shipping requirements. Document "
                "why a conditional requirement does or does not apply."
            ),
            (
                "Proceed only when the assigned provider, information workflow, "
                "service evidence, and handling method support the contracted work."
            ),
            [
                (
                    "Payer and provider eligibility",
                    "Yes: continue; no: obtain required credentials and authorization",
                    1.0,
                    (
                        "For Medicaid work, verify state and broker enrollment, "
                        "driver and vehicle requirements, exclusions screening, "
                        "and trip authorization under applicable program rules. "
                        "42 CFR 431.53 and 440.170(a) establish context, not "
                        "universal broker payment eligibility."
                    ),
                ),
                (
                    "Worker status and insured capacity",
                    "Yes: continue; no: redesign staffing or replace capacity",
                    2.0,
                    (
                        "Evaluate actual control and applicable labor tests under "
                        "29 U.S.C. 203 and state law, including California Labor "
                        "Code section 2775 where relevant. Verify commercial "
                        "coverage for the assigned service; a 1099 label or "
                        "insurance certificate alone does not resolve exposure."
                    ),
                ),
                (
                    "Protected information handling",
                    "Yes: continue; no: repair access controls and required agreements",
                    3.0,
                    (
                        "Determine business-associate status under 45 CFR 160.103; "
                        "execute required agreements under 164.502(e) and 164.504(e). "
                        "Restrict dispatch access to necessary information. A "
                        "courier conduit analysis does not automatically extend "
                        "to a platform storing protected health information."
                    ),
                ),
                (
                    "Specimen classification and exposure controls",
                    "Yes: release; no: correct packaging or select qualified service",
                    4.0,
                    (
                        "For specimen work, confirm classification before applying "
                        "49 CFR 173.199 Category B packaging and marking rules; "
                        "Category A material needs a different workflow. Apply "
                        "29 CFR 1910.1030 to covered employee exposure and follow "
                        "laboratory handling instructions under 42 CFR 493.1242."
                    ),
                ),
            ],
        ),
        (
            "diag-06-four-to-six-person-pod",
            "org_architecture",
            "Four Core Seats, Six at Scaled Volume",
            "Two full-time and two contractor seats expand to three of each.",
            11,
            "operating_framework",
            (
                "Each bar represents one distinct pod seat; the final two seats "
                "activate only in the Scaled scenario. External drivers are "
                "delivery capacity outside the pod count. Contractor designation "
                "requires a supportable relationship under applicable law."
            ),
            (
                "Base capacity is not round-the-clock staffing. Sell only coverage "
                "windows supported by the roster and documented backup arrangements."
            ),
            [
                (
                    "Core FT: owner and account lead",
                    "One full-time seat owns contracts, capacity, and cash",
                    1.0,
                    (
                        "Approve pricing, review receivable aging, maintain payer "
                        "relationships, and own escalation decisions. Separate "
                        "operating seat compensation from residual owner profit."
                    ),
                ),
                (
                    "Core FT: dispatch operations lead",
                    "One full-time seat owns live routing and service evidence",
                    1.0,
                    (
                        "Manage RouteGenie or MediRoutes workflows, provider "
                        "availability, missed pickups, and shift handoffs. "
                        "Protect specimen and passenger workflows from accidental mixing."
                    ),
                ),
                (
                    "Core C: claims and collections specialist",
                    "One contractor seat owns billing quality and receivable follow-up",
                    1.0,
                    (
                        "Validate required 837P fields or broker invoice files, "
                        "resolve denials, reconcile remittances, and escalate "
                        "Net-30/45 slippage before settlement cash becomes constrained."
                    ),
                ),
                (
                    "Core C: credential and quality specialist",
                    "One contractor seat owns provider records and evidence sampling",
                    1.0,
                    (
                        "Track credential expiration, insurance evidence, trip-log "
                        "completeness, and barcode custody exceptions. Structure "
                        "the engagement around a lawful service relationship."
                    ),
                ),
                (
                    "Scaled FT: second operations dispatcher",
                    "One additional full-time seat extends supported coverage windows",
                    1.0,
                    (
                        "Add this seat for the canonical three-FT configuration "
                        "as concurrent assignments and recovery workload exceed "
                        "the documented capacity of the core operations lead."
                    ),
                ),
                (
                    "Scaled C: route onboarding specialist",
                    "One additional contractor seat implements newly awarded service routes",
                    1.0,
                    (
                        "Add this seat for the canonical three-contractor "
                        "configuration; document stop instructions, provider "
                        "readiness, laboratory contacts, and route acceptance evidence."
                    ),
                ),
            ],
        ),
        (
            "diag-07-startup-capital-allocation",
            "stacked_comparison",
            "Allocate Startup Capital Without Buying a Fleet",
            "Four buckets total $40,000 within the $15,000–$65,000 range.",
            4,
            "illustrative_model",
            (
                "Numeric values show a $40,000 planning case. Corresponding lean "
                "allocations total $15,000 and expanded allocations total $65,000. "
                "These are funding envelopes, not automatically deductible expenses "
                "or proof of sufficient payment float."
            ),
            (
                "At Base-Case driver settlements of $508,750 annually, smooth "
                "30-day exposure is approximately $41,815 and 45-day exposure "
                "is $62,723 before offsets from actual settlement terms."
            ),
            [
                (
                    "Provider readiness and insurance setup",
                    "$12,000 planning allocation for service-ready provider onboarding",
                    12000.0,
                    (
                        "Lean allocation $3,000; expanded allocation $18,000. "
                        "Fund coverage deposits, credential checks, contract "
                        "setup, and provider onboarding rather than vehicle purchases."
                    ),
                ),
                (
                    "Dispatch and evidence infrastructure",
                    "$8,000 planning allocation for configured operational tooling",
                    8000.0,
                    (
                        "Lean allocation $2,000; expanded allocation $12,000. "
                        "Fund dispatch configuration, barcode equipment, access "
                        "controls, billing integration, and event-record retention."
                    ),
                ),
                (
                    "Commercial setup and pilot preparation",
                    "$9,000 planning allocation for contracting and service preparation",
                    9000.0,
                    (
                        "Lean allocation $3,000; expanded allocation $15,000. "
                        "Fund scoped route discovery, staff preparation, dry runs, "
                        "payer setup, and account acquisition before live volume."
                    ),
                ),
                (
                    "Settlement cash and exception reserve",
                    "$11,000 planning allocation held for timing and recovery exposure",
                    11000.0,
                    (
                        "Lean allocation $7,000; expanded allocation $20,000. "
                        "Size final liquidity from daily settlements and collection "
                        "lags. This reserve alone cannot fund Base-Case 30-day "
                        "driver exposure; stage volume or secure additional liquidity."
                    ),
                ),
            ],
        ),
        (
            "diag-08-thirty-day-launch-sprint",
            "timeline_roadmap",
            "Thirty Days to an Evidence-Ready Operating Desk",
            "Four weekly milestones prepare the business for a 2–5 month sales cycle.",
            12,
            "operating_framework",
            (
                "This sprint establishes readiness, not a promised first award. "
                "Use synthetic or properly authorized test records; do not "
                "dispatch paid passenger or specimen work before applicable "
                "credentials, agreements, and service requirements are satisfied."
            ),
            (
                "Preserve the canonical annual cases: Conservative $250,000 gross "
                "and $30,000 profit; Base $925,000 and $166,500; Scaled $1,600,000 "
                "and $384,000. The sprint does not forecast those results."
            ),
            [
                (
                    "Days 1-7: define the service boundary",
                    "Complete territory, payer, provider, and service requirement maps",
                    7.0,
                    (
                        "Choose initial NEMT transport levels and courier specimen "
                        "classes. Document enrollment requirements, insurance "
                        "coverage, labor classification, pickup windows, and "
                        "accountable exception contacts."
                    ),
                ),
                (
                    "Days 8-14: configure the evidence path",
                    "Demonstrate order intake through dispatch, custody, and billing records",
                    14.0,
                    (
                        "Configure dispatch roles, GPS events, barcode custody "
                        "records, required information agreements, and payer-specific "
                        "billing outputs. Test missing authorization and missed "
                        "pickup cases with controlled records."
                    ),
                ),
                (
                    "Days 15-21: validate capacity and unit economics",
                    "Finish provider-backed route quotes and settlement timing models",
                    21.0,
                    (
                        "Model 45% retained share: Conservative $112,500 retained "
                        "with $30,000 profit at 26.67%; Base $416,250 retained "
                        "with $166,500 profit at 40.0%; Scaled $720,000 retained "
                        "with $384,000 profit at 53.33%. Gross margins remain "
                        "12%, 18.0%, and 24%, respectively."
                    ),
                ),
                (
                    "Days 22-30: rehearse and pursue scoped awards",
                    "Complete exception drills, account proposals, and operating handoffs",
                    30.0,
                    (
                        "Rehearse driver absence, disputed trip evidence, missed "
                        "STAT pickup, and late remittance. Assign the four core "
                        "seats and define when the two Scaled seats are needed. "
                        "Submit proposals without treating unsigned pipeline as revenue."
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
        for identifier, kind, title, subtitle, chapter, tag, note, caption, stages in specs
    ]
