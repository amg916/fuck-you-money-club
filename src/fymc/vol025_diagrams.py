from __future__ import annotations

VOLUME_025_SUBTITLE: str = (
    "The Complete Playbook for $1,000,000–$5,000,000 USD in Annual Gross "
    "Shipper Billings: Build a 3 FT + 2 C (5 People) Freight Brokerage Pod "
    "and Scale to Seven"
)

VOLUME_025_POSITIONING_ALTERNATIVES: list[dict] = [
    {
        "title": "The Verified-Carrier Freight Brokerage",
        "subtitle": (
            "Build a niche property brokerage around verified carrier identity, "
            "controlled load tendering, and documented shipment handoffs."
        ),
        "audience": (
            "Experienced freight operators building a five-person brokerage "
            "serving repeat domestic commercial shippers."
        ),
        "research_basis": (
            "49 U.S.C. 13904 establishes broker registration requirements; "
            "49 CFR 371.2 defines brokerage roles. FMCSA registration and "
            "carrier records support identity checks, while Highway or RMIS "
            "can supplement direct verification. Platform signals alone do "
            "not establish carrier identity or authorize subcontracting."
        ),
        "sources": [
            "https://www.law.cornell.edu/uscode/text/49/13904",
            "https://www.ecfr.gov/current/title-49/section-371.2",
            "https://www.fmcsa.dot.gov/registration/broker-registration",
            "https://safer.fmcsa.dot.gov/",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Freight Float Control Desk",
        "subtitle": (
            "Separate shipper billings, carrier obligations, brokerage spread, "
            "and collectible cash before accepting another load."
        ),
        "audience": (
            "Brokerage founders managing shipper credit exposure and carrier "
            "payment commitments with $50,000–$250,000 USD in startup capital."
        ),
        "research_basis": (
            "49 U.S.C. 13906(b) and 49 CFR 387.307 establish property-broker "
            "security requirements. Broker transaction records under "
            "49 CFR 371.3 support reconciliation of freight charges and "
            "brokerage compensation. These requirements inform a cash-control "
            "positioning rather than evidence of customer demand."
        ),
        "sources": [
            "https://www.law.cornell.edu/uscode/text/49/13906",
            "https://www.ecfr.gov/current/title-49/section-387.307",
            "https://www.ecfr.gov/current/title-49/section-371.3",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Repeat-Lane Brokerage Pod",
        "subtitle": (
            "Turn a narrow shipper segment into repeat lanes through disciplined "
            "quoting, carrier coverage, tracking, and invoice reconciliation."
        ),
        "audience": (
            "Commercial freight sellers and carrier-operations leads combining "
            "three full-time seats with two specialist contractors."
        ),
        "research_basis": (
            "49 CFR 371.3 provides a transaction-record foundation for repeat "
            "loads. 49 U.S.C. 14706 addresses covered carrier cargo liability, "
            "and 49 CFR Part 370 addresses covered carrier claim processing. "
            "The operating design distinguishes broker coordination from "
            "carrier obligations and prices service complexity explicitly."
        ),
        "sources": [
            "https://www.ecfr.gov/current/title-49/section-371.3",
            "https://www.law.cornell.edu/uscode/text/49/14706",
            "https://www.ecfr.gov/current/title-49/part-370",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
]


def build_volume_025_diagrams_data() -> list[dict]:
    specs = [
        (
            "diag-01-verified-load-workflow",
            "process_flow",
            "One Load, Five Controlled Handoffs",
            "Move from a credit-cleared shipper order to reconciled cash.",
            1,
            "operating_framework",
            (
                "Applies to an authorized domestic property brokerage. Stage "
                "values indicate sequence, not load volume or conversion rates."
            ),
            (
                "Automate load matching, tracking, and invoice reconciliation; "
                "assign a named owner to identity, service, and payment exceptions."
            ),
            [
                (
                    "Qualify shipper and lane",
                    "Confirm credit before accepting the order",
                    1.0,
                    (
                        "Record commodity, equipment, declared cargo value, "
                        "pickup windows, accessorial terms, and shipper credit "
                        "limit in the TMS before committing capacity."
                    ),
                ),
                (
                    "Quote and reserve exposure",
                    "Price carrier cost and service burden",
                    2.0,
                    (
                        "Set the shipper rate against a documented carrier buy "
                        "rate; reserve credit exposure for the entire invoice, "
                        "not merely the expected brokerage spread."
                    ),
                ),
                (
                    "Verify and tender carrier",
                    "Match authority, identity, driver, and equipment",
                    3.0,
                    (
                        "Cross-check FMCSA records with Highway or RMIS, call a "
                        "previously verified carrier contact, verify insurance "
                        "with the issuer, and investigate identity mismatches "
                        "before issuing the rate confirmation."
                    ),
                ),
                (
                    "Track and resolve exceptions",
                    "Monitor pickup, transit, delivery, and evidence",
                    4.0,
                    (
                        "Use TMS tracking events and exception alerts; confirm "
                        "unexpected tractor, driver, or destination changes "
                        "through trusted contacts and retain delivery evidence."
                    ),
                ),
                (
                    "Reconcile and settle obligations",
                    "Match documents before releasing carrier payment",
                    5.0,
                    (
                        "Match rate confirmation, proof of delivery, carrier "
                        "invoice, and approved accessorials. Bill the shipper, "
                        "pay under agreed terms, and retain required broker "
                        "transaction records for three years under 49 CFR 371.3."
                    ),
                ),
            ],
        ),
        (
            "diag-02-repeat-shipper-cohort-funnel",
            "funnel",
            "From Named Accounts to Repeat Shippers",
            "Track one acquisition cohort through five nested account states.",
            6,
            "illustrative_model",
            (
                "Illustrative 180-day cohort of 200 distinct shipper accounts; "
                "each later stage is a subset of the prior stage. Counts are "
                "planning assumptions, not measured benchmarks or load counts. "
                "The canonical first-deal planning range remains 2–6 months."
            ),
            (
                "200 targeted accounts produce 10 repeat shippers in this "
                "illustration: 5% end-to-end conversion, with no implied revenue "
                "until actual load frequency and invoice values are established."
            ),
            [
                (
                    "Named target accounts",
                    "200 lane-matched commercial shipper accounts",
                    200.0,
                    (
                        "Select accounts with recurring lanes, compatible "
                        "equipment requirements, reachable transportation buyers, "
                        "and an identifiable entity responsible for payment."
                    ),
                ),
                (
                    "Qualified buyer conversations",
                    "80 accounts; 40% of targeted accounts",
                    80.0,
                    (
                        "Document shipment cadence, incumbent service gaps, "
                        "procurement process, payment terms, and an accessible "
                        "buyer with authority to sponsor a trial."
                    ),
                ),
                (
                    "Documented quoting opportunities",
                    "40 accounts; 50% of qualified conversations",
                    40.0,
                    (
                        "Receive actual origin, destination, commodity, weight, "
                        "equipment, and timing requirements; exclude speculative "
                        "rate checks without a credible shipment opportunity."
                    ),
                ),
                (
                    "Completed first-load customers",
                    "20 accounts; 50% of quoting opportunities",
                    20.0,
                    (
                        "Count only customers with a delivered first shipment "
                        "and an issued invoice; a signed agreement without a "
                        "completed load does not enter this stage."
                    ),
                ),
                (
                    "Repeat-load customers",
                    "10 accounts; 50% of first-load customers",
                    10.0,
                    (
                        "Require a second completed shipment within the cohort "
                        "window and no overdue undisputed invoice before treating "
                        "the account as an active repeat relationship."
                    ),
                ),
            ],
        ),
        (
            "diag-03-base-case-billings-to-owner-net",
            "waterfall",
            "$3,000,000 Billings to $165,000 Owner Net",
            "Six bars reconcile the canonical Base-Case 5.5% net margin.",
            3,
            "illustrative_model",
            (
                "USD per year. Opening and closing bars are totals; intervening "
                "bars are signed deductions. Carrier cost and expense splits "
                "are illustrative allocations; the $3,000,000 billings, "
                "$165,000 owner net, and 5.5% margin are canonical. Owner net "
                "is the scorecard residual, not a modeled personal tax outcome."
            ),
            (
                "$3,000,000 - $2,550,000 - $180,000 - $45,000 - $60,000 "
                "= $165,000. Carrier costs leave $450,000 in brokerage gross "
                "profit; $285,000 annual operating expense equals $23,750 "
                "monthly. Gross shipper billings are the scorecard basis, "
                "not automatically recognized operator revenue under an "
                "agent accounting presentation."
            ),
            [
                (
                    "Gross shipper billings",
                    "$3,000,000 opening total; includes carrier costs",
                    3000000.0,
                    (
                        "Record the full annual shipper invoice amount as the "
                        "scorecard denominator. This figure includes money "
                        "owed to carriers and is not retained brokerage income."
                    ),
                ),
                (
                    "Purchased carrier transportation",
                    "Subtract $2,550,000; retain $450,000 gross profit",
                    -2550000.0,
                    (
                        "Illustrative carrier purchases consume 85% of billings, "
                        "leaving a 15% brokerage gross margin before staffing, "
                        "systems, credit losses, and other operating expenses."
                    ),
                ),
                (
                    "Pod labor and contractor expense",
                    "Subtract $180,000 in annual staffing expense",
                    -180000.0,
                    (
                        "Illustrative combined payroll, payroll burden, and "
                        "contractor spending for the three-full-time, "
                        "two-contractor pod; reconcile actual owner compensation "
                        "and local labor costs without counting distributions twice."
                    ),
                ),
                (
                    "Systems and operating services",
                    "Subtract $45,000 in annual systems expense",
                    -45000.0,
                    (
                        "Illustrative allowance for TMS, load-board access, "
                        "Highway or RMIS verification, shipment visibility, "
                        "communications, and invoice-reconciliation services; "
                        "obtain actual vendor quotes before commitment."
                    ),
                ),
                (
                    "Other overhead and loss expense",
                    "Subtract $60,000 in annual residual expense",
                    -60000.0,
                    (
                        "Illustrative combined allowance for insurance, security "
                        "arrangement costs, administration, acquisition spending, "
                        "credit losses, claims expense, and funding charges. "
                        "Restricted trust principal is not an operating expense."
                    ),
                ),
                (
                    "Annual owner net profit",
                    "$165,000 closing total; 5.5% of billings",
                    165000.0,
                    (
                        "Reconcile to the canonical Base Case exactly. The "
                        "Conservative case is $1,000,000 at 3% for $30,000; "
                        "the Scaled case is $5,000,000 at 8% for $400,000."
                    ),
                ),
            ],
        ),
        (
            "diag-04-niche-gross-spread-yields",
            "horizontal_bars",
            "Compare Niche Gross Spread, Not Headline Billings",
            "Five illustrative lane archetypes use the same $2,000 shipper invoice.",
            2,
            "illustrative_model",
            (
                "Numeric values are brokerage gross-margin percentages: "
                "(shipper invoice minus carrier purchase) divided by shipper "
                "invoice. These are hypothetical quoting comparisons, not "
                "market yield estimates or net-profit forecasts. Payment terms "
                "and accessorial treatment are held constant."
            ),
            (
                "A wider spread can compensate for harder coverage, cargo "
                "exposure, or after-hours labor. Compare contribution after "
                "service costs rather than treating the highest bar as the "
                "best niche."
            ),
            [
                (
                    "Predictable dry-van replenishment",
                    "12% gross margin; $240 retained spread",
                    12.0,
                    (
                        "$2,000 shipper invoice less $1,760 carrier purchase "
                        "leaves $240 before overhead. Repeat appointments can "
                        "reduce touch time, while competitive bids compress spread."
                    ),
                ),
                (
                    "Regional industrial replacement parts",
                    "14% gross margin; $280 retained spread",
                    14.0,
                    (
                        "$2,000 shipper invoice less $1,720 carrier purchase "
                        "leaves $280 before overhead. Confirm receiving hours "
                        "and accessorial recovery before accepting urgent orders."
                    ),
                ),
                (
                    "Scheduled packaged-goods truckload",
                    "15% gross margin; $300 retained spread",
                    15.0,
                    (
                        "$2,000 shipper invoice less $1,700 carrier purchase "
                        "leaves $300 before overhead. This illustrative spread "
                        "matches the Base waterfall's carrier-cost assumption."
                    ),
                ),
                (
                    "Appointment-sensitive refrigerated freight",
                    "17% gross margin; $340 retained spread",
                    17.0,
                    (
                        "$2,000 shipper invoice less $1,660 carrier purchase "
                        "leaves $340 before overhead. Verify temperature "
                        "instructions, equipment suitability, and relevant cargo "
                        "coverage before tender."
                    ),
                ),
                (
                    "Time-critical manufacturing recovery",
                    "18% gross margin; $360 retained spread",
                    18.0,
                    (
                        "$2,000 shipper invoice less $1,640 carrier purchase "
                        "leaves $360 before overhead. Price after-hours "
                        "coordination and recovery capacity rather than assuming "
                        "urgency creates free margin."
                    ),
                ),
            ],
        ),
        (
            "diag-05-broker-preflight-decision-tree",
            "decision_tree",
            "Four Checks Before a Load Moves",
            "Advance on documented evidence; route failed checks to remediation.",
            5,
            "operating_framework",
            (
                "Numeric values indicate check order, not risk scores. Apply "
                "current federal requirements and shipment-specific obligations. "
                "Software verification supplements, rather than replaces, "
                "document review and trusted-contact confirmation."
            ),
            (
                "The sequence separates broker authority, carrier identity, "
                "cash exposure, and cargo risk. Passing one check does not "
                "resolve failures in another."
            ),
            [
                (
                    "Broker authority and required security",
                    "Pass to identity; otherwise suspend booking",
                    1.0,
                    (
                        "Confirm active FMCSA property-broker authority, required "
                        "process-agent designation, and $75,000 BMC-84 bond or "
                        "BMC-85 trust security under 49 U.S.C. 13904, "
                        "13906(b), and 49 CFR 387.307. Verify current provider "
                        "eligibility and security status; a pending filing "
                        "does not authorize brokerage operations."
                    ),
                ),
                (
                    "Carrier identity and operating eligibility",
                    "Pass to credit; otherwise investigate mismatches",
                    2.0,
                    (
                        "Check applicable carrier authority and insurance "
                        "filings through FMCSA, supplement with Highway or "
                        "RMIS, and confirm dispatch through a trusted number. "
                        "Independently verify cargo coverage and bank changes; "
                        "resolve substituted identities or unauthorized "
                        "re-brokering before release."
                    ),
                ),
                (
                    "Shipper credit and payment float",
                    "Pass to cargo; otherwise change exposure",
                    3.0,
                    (
                        "At Base carrier purchases of $2,550,000 annually, a "
                        "20-day collection-versus-payment gap requires about "
                        "$139,726 using annual carrier cost divided by 365. "
                        "If available cash cannot cover modeled obligations, "
                        "obtain a deposit, change agreed terms, or reduce volume."
                    ),
                ),
                (
                    "Cargo terms and claims readiness",
                    "Pass to tender; otherwise resolve coverage",
                    4.0,
                    (
                        "Match commodity, value, exclusions, handling instructions, "
                        "and contract obligations to verified coverage. "
                        "49 U.S.C. 14706 addresses covered carrier cargo "
                        "liability; broker exposure also depends on conduct "
                        "and contract. Preserve claim evidence and track "
                        "applicable deadlines under 49 CFR Part 370."
                    ),
                ),
            ],
        ),
        (
            "diag-06-five-to-seven-person-pod",
            "org_architecture",
            "Five Core Seats, Two Scale Seats",
            "Base: 3 FT + 2 C. Scaled: 4 FT + 3 C.",
            11,
            "operating_framework",
            (
                "Each numeric value represents one person, not full-time "
                "equivalent capacity. The first five seats form the "
                "Conservative and Base pod; the final two are Scaled-only "
                "additions. Contractor status requires a fact-specific "
                "classification assessment, not merely a seat label."
            ),
            (
                "Conservative: $1,000,000 billings and $30,000 owner net with "
                "five people. Base: $3,000,000 and $165,000 with five. Scaled: "
                "$5,000,000 and $400,000 with seven. The $180,000 Base labor "
                "allocation is illustrative and must be tested against actual "
                "staffing costs and workload."
            ),
            [
                (
                    "Founder and commercial lead",
                    "Core seat one; full-time commercial owner",
                    1.0,
                    (
                        "Own shipper acquisition, pricing limits, customer "
                        "concentration, and cash planning. Approve unusual "
                        "credit exposure without also controlling every "
                        "payment-master change."
                    ),
                ),
                (
                    "Carrier procurement and verification lead",
                    "Core seat two; full-time carrier owner",
                    1.0,
                    (
                        "Source capacity, verify carrier identity, negotiate "
                        "buy rates, and document coverage decisions. Escalate "
                        "identity conflicts independently of sales pressure."
                    ),
                ),
                (
                    "Shipment operations and service lead",
                    "Core seat three; full-time execution owner",
                    1.0,
                    (
                        "Run pickup and delivery execution, monitor tracking "
                        "exceptions, collect proof of delivery, and maintain "
                        "shipper updates and claims evidence."
                    ),
                ),
                (
                    "Billing and reconciliation specialist",
                    "Core seat four; contracted accounting support",
                    1.0,
                    (
                        "Match invoices to load records, reconcile carrier "
                        "payables, monitor receivables aging, and flag "
                        "duplicate invoices. Separate payment preparation "
                        "from final release."
                    ),
                ),
                (
                    "After-hours tracking specialist",
                    "Core seat five; contracted coverage support",
                    1.0,
                    (
                        "Cover agreed monitoring windows, escalate missed "
                        "milestones, and preserve event logs. One contractor "
                        "does not provide continuous round-the-clock staffing."
                    ),
                ),
                (
                    "Additional account operations manager",
                    "Scaled seat six; added full-time capacity",
                    1.0,
                    (
                        "Add only in the seven-person configuration to own "
                        "repeat-account execution and absorb measured service "
                        "load without weakening carrier or credit controls."
                    ),
                ),
                (
                    "Additional coverage and exception specialist",
                    "Scaled seat seven; added contracted capacity",
                    1.0,
                    (
                        "Expand defined coverage windows and document exception "
                        "resolution during peak demand. Track contracted hours "
                        "against incremental load contribution and service results."
                    ),
                ),
            ],
        ),
        (
            "diag-07-startup-capital-allocation",
            "stacked_comparison",
            "Allocate a $150,000 Startup Capital Plan",
            "Four cash buckets inside the canonical $50,000–$250,000 range.",
            4,
            "illustrative_model",
            (
                "USD allocations total $150,000. This illustration uses a "
                "fully funded $75,000 BMC-85 trust rather than a BMC-84 bond. "
                "Verify eligible trustee, assets, and current requirements. "
                "Trust principal remains restricted and cannot also fund "
                "carrier payments."
            ),
            (
                "$75,000 + $45,000 + $20,000 + $10,000 = $150,000. A bond-based "
                "plan uses quoted premiums and any required collateral instead "
                "of assuming $75,000 cash funding. Neither arrangement removes "
                "the need to fund shipper-to-carrier timing gaps."
            ),
            [
                (
                    "Restricted broker trust security",
                    "$75,000 allocated; 50% of startup capital",
                    75000.0,
                    (
                        "Fund the illustrated BMC-85 security arrangement "
                        "separately from operating cash. Track provider charges "
                        "and any replenishment obligations without treating "
                        "restricted principal as available working capital."
                    ),
                ),
                (
                    "Carrier payment working capital",
                    "$45,000 allocated; 30% of startup capital",
                    45000.0,
                    (
                        "At a 20-day gap and 85% carrier-cost ratio, this "
                        "supports roughly $966,176 annualized billings before "
                        "buffers. Base throughput needs about $139,726 for "
                        "that gap, so shorten terms or secure additional funding."
                    ),
                ),
                (
                    "Launch operating runway",
                    "$20,000 allocated; about 13.3% of capital",
                    20000.0,
                    (
                        "Fund lean pre-revenue operations and initial staffing. "
                        "At $6,000 monthly burn this lasts about 3.3 months, "
                        "shorter than the six-month first-deal planning boundary; "
                        "phase hiring or raise the runway allocation."
                    ),
                ),
                (
                    "Setup systems and administration",
                    "$10,000 allocated; about 6.7% of capital",
                    10000.0,
                    (
                        "Budget registration work, process-agent services, "
                        "contract preparation, TMS configuration, verification "
                        "onboarding, and accounting setup. Separate one-time "
                        "charges from recurring monthly operating expense."
                    ),
                ),
            ],
        ),
        (
            "diag-08-first-thirty-days-roadmap",
            "timeline_roadmap",
            "Thirty Days to an Evidence-Ready Brokerage",
            "Prepare the operating system without forcing premature live loads.",
            12,
            "operating_framework",
            (
                "Numeric values are milestone end days: 7, 14, 21, and 30. "
                "This sprint prepares launch readiness; it does not replace "
                "the canonical 2–6 month time-to-first-deal planning range "
                "or accelerate external authority processing."
            ),
            (
                "Finish the month with a documented niche, tracked authority "
                "work, tested verification procedures, and a cash-limited "
                "pipeline. Live brokerage begins only when required authority "
                "and operating prerequisites are satisfied."
            ),
            [
                (
                    "Days 1-7",
                    "Define niche, economics, and authority work",
                    7.0,
                    (
                        "Choose equipment and lane boundaries, identify 50 "
                        "target shippers, document the three canonical "
                        "scorecard scenarios, obtain security quotes, and "
                        "prepare required registration and process-agent work."
                    ),
                ),
                (
                    "Days 8-14",
                    "Configure verification and transaction records",
                    14.0,
                    (
                        "Configure the TMS, Highway or RMIS workflow, trusted "
                        "callback procedure, carrier document checklist, and "
                        "49 CFR 371.3 record retention. Test identity and "
                        "bank-change exceptions using synthetic records."
                    ),
                ),
                (
                    "Days 15-21",
                    "Test quoting, credit, and cash timing",
                    21.0,
                    (
                        "Conduct shipper discovery, assemble carrier coverage "
                        "options, and model sample quotes without representing "
                        "pending authority as active. Stress-test payment gaps "
                        "and set account exposure limits against available cash."
                    ),
                ),
                (
                    "Days 22-30",
                    "Rehearse shipment execution and reconciliation",
                    30.0,
                    (
                        "Run a synthetic tender-to-settlement exercise, assign "
                        "the five core seats, test tracking alerts and duplicate "
                        "invoice detection, and review authority status. Keep "
                        "live loads paused while required prerequisites remain open."
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
