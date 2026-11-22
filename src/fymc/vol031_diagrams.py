from __future__ import annotations

VOLUME_031_SUBTITLE = (
    "The Complete Playbook for Uber & Commercial Fleet Arbitrage: "
    "$180,000–$1,200,000 USD in Annual Gross Billings, "
    "Built Around a 1 FT + 3 C (4 People) Pod"
)

VOLUME_031_POSITIONING_ALTERNATIVES = [
    {
        "title": "Collect the Lease, Control the Fleet",
        "subtitle": (
            "Build recurring driver-lease collections around documented vehicle "
            "eligibility, continuous coverage, and enforceable payment instructions."
        ),
        "audience": (
            "Fleet operators managing investor-owned vehicles who need weekly "
            "collections, driver qualification, and maintenance accountability "
            "without confusing passenger fares with operator revenue."
        ),
        "research_basis": (
            "California Public Utilities Code section 5433 distinguishes "
            "transportation-network insurance periods. The Fair Credit Reporting "
            "Act requires a permissible purpose for consumer reports. Together, "
            "these support an operating model built around coverage-state evidence "
            "and properly authorized driver screening rather than vehicle count alone."
        ),
        "sources": [
            "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PUC&sectionNum=5433.",
            "https://www.law.cornell.edu/uscode/text/15/1681b",
            "https://www.law.cornell.edu/uscode/text/15/1681m",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "Black SUV Shift Economics",
        "subtitle": (
            "Turn licensed commercial vehicle availability into measured shift "
            "contribution through dispatch discipline and downtime control."
        ),
        "audience": (
            "Existing licensed livery and black-car operators evaluating "
            "incremental SUV shifts, airport work, and contractor dispatch capacity."
        ),
        "research_basis": (
            "California Public Utilities Code section 5371 addresses charter-party "
            "carrier authority, while the New York City Taxi and Limousine "
            "Commission publishes separate driver, vehicle, and base licensing "
            "requirements. These are jurisdiction-specific operating systems, "
            "not interchangeable credentials or universal airport permissions."
        ),
        "sources": [
            "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PUC&sectionNum=5371.",
            "https://www.nyc.gov/site/tlc/businesses/for-hire-vehicle-bases.page",
            "https://www.nyc.gov/site/tlc/vehicles/get-a-for-hire-vehicle-license.page",
            "https://www.nyc.gov/site/tlc/drivers/get-a-tlc-drivers-license.page",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "Zero-Owned-Metal Fleet Operations",
        "subtitle": (
            "Coordinate investor vehicles, driver collections, and maintenance "
            "without treating investor assets or passenger fares as operator sales."
        ),
        "audience": (
            "Asset-light fleet managers with vehicle-owner relationships and the "
            "ability to administer contracts, settlements, and service schedules."
        ),
        "research_basis": (
            "UCC Article 2A supplies the model framework for leases of goods; "
            "the enacted state version controls each vehicle arrangement. "
            "Federal odometer rules govern applicable vehicle transfers. "
            "Neither source establishes that a co-hosting arrangement is "
            "asset-light in substance or determines its revenue presentation."
        ),
        "sources": [
            "https://www.law.cornell.edu/ucc/2A",
            "https://www.law.cornell.edu/uscode/text/49/32705",
            "https://www.ecfr.gov/current/title-49/subtitle-B/chapter-V/part-580",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
]


def build_volume_031_diagrams_data() -> list[dict]:
    specs = [
        (
            "diag-01-vehicle-to-settlement-workflow",
            "process_flow",
            "Control the Vehicle-to-Cash Chain",
            "Five operating steps for investor vehicles, qualified drivers, and reconciled collections.",
            1,
            "operating_framework",
            (
                "The asset-light model assumes documented owner authority and "
                "platform acceptance of each vehicle and arrangement. Gross "
                "operator billings mean driver leases, dispatch, and co-hosting "
                "charges; passenger trip GMV and investor vehicle values remain "
                "outside this revenue measure."
            ),
            (
                "A top-of-waterfall lease is a contractual collection priority, "
                "not an automatic platform capability. Use Uber fleet settlement "
                "features only where the account supports the documented split; "
                "otherwise reconcile authorized collections separately."
            ),
            [
                (
                    "Secure vehicle authority",
                    "Document ownership and permitted commercial use before listing",
                    1.0,
                    (
                        "Capture VIN, title or lease authority, lender restrictions, "
                        "owner settlement terms, and responsibility for depreciation. "
                        "Reject vehicles whose financing or insurance excludes "
                        "the intended rental, livery, or rideshare activity."
                    ),
                ),
                (
                    "Qualify driver and operation",
                    "Match driver credentials to vehicle and service jurisdiction",
                    2.0,
                    (
                        "Verify applicable licenses, platform eligibility, MVR "
                        "authorization, inspection dates, airport access, and "
                        "policy endorsements. Treat personal use, app-on waiting, "
                        "accepted trips, and passenger carriage as distinct exposure states."
                    ),
                ),
                (
                    "Execute handover and collection",
                    "Record condition and activate expressly authorized payment instructions",
                    3.0,
                    (
                        "Photograph condition, record odometer and fuel, explain "
                        "deductibles and toll charges, and obtain the required "
                        "payment authorization. Keep refundable security deposits "
                        "in a liability ledger rather than recording them as sales."
                    ),
                ),
                (
                    "Monitor service and exceptions",
                    "Convert telematics exceptions into scheduled human operating decisions",
                    4.0,
                    (
                        "Use OBD-II GPS, diagnostic alerts, and maintenance mileage "
                        "to schedule service. Route collision, overdue-payment, "
                        "and vehicle-location exceptions to a named operator. "
                        "Never remotely interrupt a moving or occupied vehicle."
                    ),
                ),
                (
                    "Close weekly settlements",
                    "Reconcile billed charges, collected cash, and owner distributions",
                    5.0,
                    (
                        "Match Uber settlement exports, authorized ACH receipts, "
                        "toll statements, repair invoices, and owner splits to "
                        "vehicle-level ledgers. Age failed collections separately "
                        "and reconcile retained contribution before calculating profit."
                    ),
                ),
            ],
        ),
        (
            "diag-02-driver-qualification-cohort",
            "funnel",
            "From Driver Inquiry to Settled Vehicle Week",
            "One nested 100-inquiry cohort; every later stage is a subset of the preceding stage.",
            6,
            "illustrative_model",
            (
                "Illustrative counts describe a single prospect cohort, not "
                "verified acquisition performance or annual revenue capacity. "
                "Stage counts are 100, 60, 36, 18, and 12; total conversion is "
                "12%. The first settled week can occur after day 30."
            ),
            (
                "Track unique applicants rather than form submissions. Record "
                "a dated exclusion reason at each transition so insurance "
                "ineligibility, missing credentials, and payment failures do not "
                "disappear inside one blended conversion percentage."
            ),
            [
                (
                    "Inbound inquiries",
                    "100 unique applicants enter the dated source cohort",
                    100.0,
                    (
                        "Deduplicate telephone numbers and applicant records in "
                        "the CRM. Record service area, desired vehicle class, "
                        "work schedule, and acquisition channel before screening."
                    ),
                ),
                (
                    "Operating fit established",
                    "60 applicants meet the initial jurisdiction and schedule criteria",
                    60.0,
                    (
                        "Retain 60% of inquiries after checking intended service, "
                        "license category, platform status, weekly availability, "
                        "and published insurer eligibility requirements."
                    ),
                ),
                (
                    "Documents and screening complete",
                    "36 applicants complete the authorized evidence collection process",
                    36.0,
                    (
                        "Retain 60% of the prior cohort after identity, license, "
                        "MVR, and insurer review. Establish the permissible purpose "
                        "under 15 U.S.C. 1681b before ordering a consumer report."
                    ),
                ),
                (
                    "Vehicle offer accepted",
                    "18 applicants accept documented vehicle and collection terms",
                    18.0,
                    (
                        "Retain 50% of screened applicants after disclosing weekly "
                        "charges, deposits, deductible allocation, mileage terms, "
                        "toll administration, and service downtime procedures."
                    ),
                ),
                (
                    "First settled week completed",
                    "12 drivers complete handover and produce reconciled cleared collections",
                    12.0,
                    (
                        "Retain two-thirds of accepted offers only after coverage "
                        "activation, vehicle inspection, completed handover, and "
                        "cleared first-week collections. An executed contract alone "
                        "does not qualify as a settled vehicle week."
                    ),
                ),
            ],
        ),
        (
            "diag-03-base-case-contribution-waterfall",
            "waterfall",
            "The $690,000 Base-Case Waterfall",
            "$379,500 retained contribution becomes $144,900 owner profit after operator expenses.",
            3,
            "illustrative_model",
            (
                "All amounts are annual USD. Bars 1, 3, and 6 are absolute "
                "totals or subtotals; bars 2, 4, and 5 are signed deductions. "
                "Subtotals must reset the plotted running balance rather than "
                "being added again. The $180,000 and $54,600 expense categories "
                "are illustrative allocations of the canonical $234,600 residual "
                "operator expense requirement, not separately supplied estimates."
            ),
            (
                "$690,000 - $310,500 = $379,500; $379,500 - $180,000 "
                "- $54,600 = $144,900. Owner profit equals 21.0% of gross "
                "billings and 38.18% of retained contribution. Apply the supplied "
                "55% ASC 606 net-presentation convention; actual principal-versus-agent "
                "presentation follows the contracts and control analysis."
            ),
            [
                (
                    "Gross operator billings",
                    "$690,000 annual lease, dispatch, and co-hosting charges",
                    690000.0,
                    (
                        "Opening total: $57,500 average monthly gross billings. "
                        "Exclude underlying passenger fares, vehicle purchase "
                        "values, refundable deposits, and investor capital from "
                        "this operator billing measure."
                    ),
                ),
                (
                    "Owner splits and pass-through costs",
                    "Subtract $310,500 distributed or passed through under contracts",
                    -310500.0,
                    (
                        "Deduction: 45% of gross billings leaves the operator "
                        "under the canonical retained-share model. Reconcile owner "
                        "distributions and pass-through fleet costs individually; "
                        "do not deduct these same costs again below retained contribution."
                    ),
                ),
                (
                    "Retained contribution subtotal",
                    "$379,500 remains under the supplied 55% retained-share convention",
                    379500.0,
                    (
                        "Absolute subtotal: $31,625 average monthly retained "
                        "contribution. This is the supplied net-presentation "
                        "revenue basis, not owner profit and not a separate "
                        "increment added to the running balance."
                    ),
                ),
                (
                    "Recurring operator operating costs",
                    "Subtract $180,000 for the modeled recurring operating cost envelope",
                    -180000.0,
                    (
                        "Deduction: $15,000 monthly covers the modeled operator "
                        "labor, contractor support, software, administration, and "
                        "operator-borne recurring costs. Include only costs "
                        "outside the preceding owner and pass-through deduction."
                    ),
                ),
                (
                    "Depreciation and uninsured collision expense",
                    "Subtract $54,600 in separately modeled operator-borne expense",
                    -54600.0,
                    (
                        "Deduction: $4,550 monthly equivalent represents recognized "
                        "depreciation where the operator bears it and uninsured "
                        "collision expense. Investor-borne depreciation stays with "
                        "the investor; cash transferred into a reserve is not itself expense."
                    ),
                ),
                (
                    "Annual owner profit total",
                    "$144,900 equals 21.0% of gross operator billings",
                    144900.0,
                    (
                        "Closing total: $12,075 monthly equivalent and 38.18% "
                        "of $379,500 retained contribution. Preserve the scorecard "
                        "owner-profit definition; this figure is not a statement "
                        "of after-personal-tax distributions or unrestricted cash."
                    ),
                ),
            ],
        ),
        (
            "diag-04-subniche-retained-yield-bars",
            "horizontal_bars",
            "Compare Retention, Not Passenger Fare Volume",
            "Five illustrative sub-niches measured as retained dollars per $100 of operator billings.",
            2,
            "illustrative_model",
            (
                "Each bar represents $100 of gross operator billings before "
                "operator overhead. Equal billing weights across yields of "
                "$60, $50, $65, $45, and $55 produce the canonical 55% blended "
                "retained share. These are illustrative contract economics, "
                "not observed market yields or separate scorecard forecasts."
            ),
            (
                "Collection rails affect settlement speed, fees, and reversals; "
                "they do not create the underlying yield. Maintain separate "
                "contract, payment-fee, and failed-collection fields. The canonical "
                "scenarios retain 55% regardless of this illustrative niche mix."
            ),
            [
                (
                    "Weekly rideshare driver leases",
                    "$60 retained per $100 billed through authorized ACH collections",
                    60.0,
                    (
                        "Illustrative $40 owner and pass-through allocation "
                        "leaves $60 before operator overhead. Reconcile scheduled "
                        "lease collections to cleared cash; an ACH initiation "
                        "does not establish final payment."
                    ),
                ),
                (
                    "Licensed Black SUV shift dispatch",
                    "$50 retained per $100 billed through reconciled commercial settlements",
                    50.0,
                    (
                        "Illustrative $50 owner and vehicle-service allocation "
                        "leaves $50 before overhead. Measure operator dispatch "
                        "billings rather than all passenger fares; airport waiting "
                        "and empty repositioning can destroy shift contribution."
                    ),
                ),
                (
                    "Investor vehicle co-hosting",
                    "$65 retained per $100 of gross co-hosting billings",
                    65.0,
                    (
                        "Illustrative $35 contractually payable owner and "
                        "pass-through allocation leaves $65. Where the operator "
                        "bills only a management fee in practice, reassess the "
                        "billing denominator instead of importing investor receipts."
                    ),
                ),
                (
                    "Short-duration replacement vehicles",
                    "$45 retained per $100 billed through documented short-term rentals",
                    45.0,
                    (
                        "Illustrative $55 owner and pass-through allocation "
                        "leaves $45 before overhead. Delivery labor, cleaning, "
                        "charge reversals, and idle days require separate tracking; "
                        "deposits remain liabilities until properly applied."
                    ),
                ),
                (
                    "Commercial sedan driver leases",
                    "$55 retained per $100 billed through scheduled business collections",
                    55.0,
                    (
                        "Illustrative $45 owner and pass-through allocation "
                        "matches the canonical blend. Attach toll evidence to "
                        "each permitted charge and distinguish recurring rent "
                        "from reimbursements and separately disclosed administration fees."
                    ),
                ),
            ],
        ),
        (
            "diag-05-preflight-statutory-risk-tree",
            "decision_tree",
            "Four Checks Before Vehicle Release",
            "A sequential decision path: every affirmative result advances; every failed check holds release.",
            5,
            "operating_framework",
            (
                "The four nodes are sequential predicates, not numerical risk "
                "scores. Numeric values indicate reading order. California and "
                "New York City are concrete jurisdiction examples; apply the "
                "actual operating jurisdiction, service category, and airport rules."
            ),
            (
                "Release only after all four evidence sets are complete. "
                "Correct missing authority, coverage, screening, or contract "
                "terms before handover; a platform account does not replace "
                "carrier authority, insurer acceptance, or airport permission."
            ),
            [
                (
                    "Coverage matches every use state",
                    "Yes: advance; no: hold release until endorsements are verified",
                    1.0,
                    (
                        "Map off-app rental use and rideshare Periods 1, 2, "
                        "and 3 to actual policy language and named insureds. "
                        "California Public Utilities Code section 5433 governs "
                        "specified TNC coverage periods; commercial livery use "
                        "needs its own applicable coverage analysis."
                    ),
                ),
                (
                    "Authority matches service and location",
                    "Yes: advance; no: remove the prohibited operating assignment",
                    2.0,
                    (
                        "Check California charter-party authority under Public "
                        "Utilities Code section 5371 where applicable, or NYC "
                        "TLC driver, vehicle, and base requirements for the "
                        "relevant service. Verify airport permissions separately; "
                        "TCP and TLC credentials are not nationwide substitutes."
                    ),
                ),
                (
                    "Screening has a documented lawful basis",
                    "Yes: advance; no: stop report ordering and driver assignment",
                    3.0,
                    (
                        "Establish a permissible consumer-report purpose under "
                        "15 U.S.C. 1681b and protect motor-vehicle information "
                        "under 18 U.S.C. 2721. Use employment-specific disclosure "
                        "and pre-adverse procedures when applicable; apply "
                        "15 U.S.C. 1681m adverse-action notices as required."
                    ),
                ),
                (
                    "Contract and immobilizer controls are safe",
                    "Yes: release vehicle; no: correct terms or disable remote immobilization",
                    4.0,
                    (
                        "Use enacted state UCC Article 2A and applicable "
                        "rental statutes to review lease disclosures, toll fees, "
                        "and remedies. Validate state immobilizer restrictions "
                        "and insurer terms; permit no remote engine shutdown, "
                        "and require verified stationary, unoccupied status plus "
                        "human review for any permitted starter inhibition."
                    ),
                ),
            ],
        ),
        (
            "diag-06-four-to-six-person-pod",
            "org_architecture",
            "Four Seats at Base; Six at Scale",
            "One accountable fleet lead coordinates three contractors before adding two distinct expansion seats.",
            11,
            "operating_framework",
            (
                "FT means full-time seat; C means contractor seat. Conservative "
                "and Base use 1 FT + 3 C, four people total. Scaled uses "
                "2 FT + 4 C, six people total. Each node represents one person; "
                "the last two nodes activate only in the Scaled configuration. "
                "Seat labels do not determine worker classification."
            ),
            (
                "Conservative: $180,000 gross, $99,000 retained, $25,200 profit "
                "at 14% gross margin and 25.45% retained margin. Base: $690,000 "
                "gross, $379,500 retained, $144,900 profit at 21.0% and 38.18%. "
                "Scaled: $1,200,000 gross, $660,000 retained, $336,000 profit "
                "at 28% and 50.91%. Scaled economics require the six-person pod."
            ),
            [
                (
                    "Fleet principal — base FT",
                    "One full-time owner leads contracts, cash, and exception decisions",
                    1.0,
                    (
                        "Own vehicle acceptance, insurer relationships, investor "
                        "terms, weekly contribution review, and incident escalation. "
                        "Approve settlement corrections against source evidence "
                        "rather than allowing dispatch to rewrite owner allocations."
                    ),
                ),
                (
                    "Dispatch coordinator — base contractor",
                    "One contractor coordinates assignments, handovers, and driver communication",
                    1.0,
                    (
                        "Maintain the vehicle availability board, collect signed "
                        "handover records, route platform issues, and confirm "
                        "service interruptions. Escalate coverage and permit "
                        "exceptions instead of assigning around them."
                    ),
                ),
                (
                    "Maintenance coordinator — base contractor",
                    "One contractor schedules inspections, repairs, and downtime recovery",
                    1.0,
                    (
                        "Review OBD-II alerts, mileage intervals, tire condition, "
                        "repair estimates, and return-to-service evidence. Keep "
                        "maintenance availability separate from paid utilization "
                        "so idle vehicles remain visible."
                    ),
                ),
                (
                    "Settlement specialist — base contractor",
                    "One contractor reconciles billing, tolls, and investor statements",
                    1.0,
                    (
                        "Match platform exports, bank receipts, owner splits, "
                        "repair invoices, and toll evidence. Produce aged "
                        "receivables and deposit-liability schedules; the fleet "
                        "principal reviews adjustments and payment releases."
                    ),
                ),
                (
                    "Operations manager — scaled FT",
                    "Add one full-time manager only in the six-person configuration",
                    1.0,
                    (
                        "Take daily dispatch supervision and service recovery "
                        "from the principal. Use documented workload, incident "
                        "response, and contribution capacity to justify the seat "
                        "rather than hiring against gross passenger fare volume."
                    ),
                ),
                (
                    "Claims and onboarding specialist — scaled contractor",
                    "Add one contractor for screening administration and incident documentation",
                    1.0,
                    (
                        "Assemble authorized screening records, renewal evidence, "
                        "collision photographs, insurer submissions, and recovery "
                        "tracking. Keep report access restricted and separate "
                        "claims documentation from settlement payment authority."
                    ),
                ),
            ],
        ),
        (
            "diag-07-startup-capital-allocation",
            "stacked_comparison",
            "Deploy $12,000–$65,000 Without Buying a Fleet",
            "Four capital buckets; the rendered example totals $35,000.",
            4,
            "illustrative_model",
            (
                "Numeric values are USD allocations for one $35,000 startup "
                "stack. Low-envelope allocations total $12,000; high-envelope "
                "allocations total $65,000. Endpoint allocations are coordinated "
                "budgets, not independently selectable cost ranges. This model "
                "assumes investor-supplied vehicles and excludes vehicle acquisitions."
            ),
            (
                "Example: $10,000 + $5,000 + $8,000 + $12,000 = $35,000. "
                "Low envelope: $4,000 + $1,500 + $2,500 + $4,000 = $12,000. "
                "High envelope: $20,000 + $8,000 + $12,000 + $25,000 = $65,000. "
                "Startup cash, refundable deposits, and operating expense are "
                "different ledger categories."
            ),
            [
                (
                    "Insurance and authority funding",
                    "$10,000 example allocation for coverage activation and operating credentials",
                    10000.0,
                    (
                        "Allocate $4,000 in the low envelope and $20,000 in "
                        "the high envelope for required insurance deposits, "
                        "initial premiums, inspections, and applicable authority "
                        "fees. Obtain actual quotes before accepting vehicle commitments."
                    ),
                ),
                (
                    "Telematics and collection infrastructure",
                    "$5,000 example allocation for installed monitoring and billing setup",
                    5000.0,
                    (
                        "Allocate $1,500 low and $8,000 high for OBD-II devices, "
                        "GPS installation, secure account setup, collection "
                        "integration, and settlement templates. Treat later "
                        "subscriptions as operating costs rather than repeatedly "
                        "charging them to startup capital."
                    ),
                ),
                (
                    "Contracts and vehicle onboarding",
                    "$8,000 example allocation for documented vehicle and driver activation",
                    8000.0,
                    (
                        "Allocate $2,500 low and $12,000 high for contract "
                        "drafting, authorized screening, condition documentation, "
                        "initial preparation, and handover logistics. Exclude "
                        "vehicle purchase prices and investor capital contributions."
                    ),
                ),
                (
                    "Liquidity and collision buffer",
                    "$12,000 example allocation retained as operating liquidity",
                    12000.0,
                    (
                        "Allocate $4,000 low and $25,000 high for deductible "
                        "liquidity, collection delays, and service interruptions. "
                        "Keep customer deposits separate. Holding this cash "
                        "does not reduce accounting profit; recognized expenses "
                        "and actual disbursements follow their own timing."
                    ),
                ),
            ],
        ),
        (
            "diag-08-first-thirty-days-roadmap",
            "timeline_roadmap",
            "Build a Controlled Fleet Launch in 30 Days",
            "Four weekly milestones create a launch-ready operation without forcing an early first deal.",
            12,
            "operating_framework",
            (
                "Numeric values are milestone ending days: 7, 14, 21, and 30. "
                "The canonical time to first deal is 1–3 months. The sprint "
                "can finish with qualified prospects and complete documentation "
                "while insurer, licensing, or vehicle activation work continues."
            ),
            (
                "Maintain the supplied $2,500–$15,000 monthly operating-cost "
                "range as a planning envelope, not a universal runway estimate. "
                "Release dates follow completed evidence; acquisition volume "
                "does not override vehicle readiness or insured operating scope."
            ),
            [
                (
                    "Days 1-7",
                    "Define the service jurisdiction and obtain written operating requirements",
                    7.0,
                    (
                        "Choose one launch niche and geography. Obtain insurer "
                        "quotes, identify applicable carrier or TLC authority, "
                        "confirm platform vehicle requirements, and model the "
                        "55% retained share separately from passenger trip GMV. "
                        "Deliver a priced launch worksheet and jurisdiction checklist."
                    ),
                ),
                (
                    "Days 8-14",
                    "Document owner terms and configure auditable collections and ledgers",
                    14.0,
                    (
                        "Review vehicle-owner authority, draft driver terms, "
                        "configure authorized payment collection, and create "
                        "separate deposit, pass-through, and retained-contribution "
                        "accounts. Deliver a sample owner statement that reconciles "
                        "from gross billings to distributable amounts."
                    ),
                ),
                (
                    "Days 15-21",
                    "Run a limited qualification and vehicle-readiness rehearsal",
                    21.0,
                    (
                        "Process a small authorized applicant cohort, inspect "
                        "candidate vehicles, install approved telematics, and "
                        "test maintenance alerts. Rehearse collision reporting, "
                        "failed-payment handling, and stationary starter-inhibition "
                        "controls without deploying an unsafe vehicle."
                    ),
                ),
                (
                    "Days 22-30",
                    "Complete a settlement rehearsal and schedule only ready handovers",
                    30.0,
                    (
                        "Reconcile a labeled test dataset across billing, bank "
                        "receipts, tolls, repairs, and owner splits. Where every "
                        "requirement is complete, conduct a controlled handover; "
                        "otherwise continue the documented 1–3 month first-deal "
                        "plan without recording test collections as revenue."
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
