from __future__ import annotations

VOLUME_032_SUBTITLE = (
    "The Complete Playbook for ISO Payment Processing & ATM Arbitrage: "
    "$90,000–$800,000 USD in Annual Retained Revenue, "
    "Built Around a 1 FT + 3 C (4 People) Pod"
)

VOLUME_032_POSITIONING_ALTERNATIVES = [
    {
        "title": "The Residual-First ISO",
        "subtitle": (
            "Build a merchant portfolio around auditable Schedule A spreads, "
            "gateway markups, and durable sponsor relationships."
        ),
        "audience": (
            "Experienced merchant-services sellers operating with one full-time "
            "principal and three specialist contractors."
        ),
        "research_basis": (
            "12 CFR 235.7 addresses debit-network exclusivity and routing restrictions; "
            "15 U.S.C. 1693o-2 separately addresses interchange and payment-network "
            "restrictions. These provisions support a rail-specific operating model, "
            "not a blanket right to surcharge debit transactions. Sponsor agreements "
            "establish residual ownership, deductions, portability, and termination rights."
        ),
        "sources": [
            "https://www.ecfr.gov/current/title-12/chapter-II/subchapter-A/part-235/section-235.7",
            "https://www.law.cornell.edu/uscode/text/15/1693o-2",
        ],
        "validation_status": "Source-informed editorial positioning; not market-tested.",
    },
    {
        "title": "The Exclusive-Venue ATM Portfolio",
        "subtitle": (
            "Turn signed placement rights, dependable cash service, and retained "
            "withdrawal surcharges into a measurable venue portfolio."
        ),
        "audience": (
            "Local venue-network operators able to coordinate contracted maintenance, "
            "sponsor processing, and separately documented vault-cash provision."
        ),
        "research_basis": (
            "12 CFR 1005.16 requires covered ATM fee disclosures and consumer election "
            "before the fee-bearing transfer. 31 CFR 1010.100(ff) defines money-services "
            "business categories; actual services, rather than an ATM label, determine "
            "whether a separate registration analysis is necessary. Neither source "
            "establishes placement profitability or a market conversion rate."
        ),
        "sources": [
            "https://www.ecfr.gov/current/title-12/chapter-X/part-1005/subpart-A/section-1005.16",
            "https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1010/subpart-A/section-1010.100",
            "https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1022/subpart-C/section-1022.380",
        ],
        "validation_status": "Source-informed editorial positioning; not market-tested.",
    },
    {
        "title": "The Price-Integrity Payments Desk",
        "subtitle": (
            "Win suitable merchants through transparent credit pricing, accurate "
            "debit treatment, and disciplined dispute operations."
        ),
        "audience": (
            "Payments operators serving multi-location merchants with documented "
            "pricing configurations and sponsor-approved business categories."
        ),
        "research_basis": (
            "New York General Business Law section 518 requires specific credit-card "
            "price presentation and limits the surcharge to the merchant's charge. "
            "15 U.S.C. 1693o-2 distinguishes statutory discount protections from "
            "other network restrictions. Card-brand surcharge rules remain separate "
            "contractual requirements; state-specific review precedes configuration."
        ),
        "sources": [
            "https://www.nysenate.gov/legislation/laws/GBS/518",
            "https://www.law.cornell.edu/uscode/text/15/1693o-2",
        ],
        "validation_status": "Source-informed editorial positioning; not market-tested.",
    },
]


def build_volume_032_diagrams_data() -> list[dict]:
    specs = [
        (
            "diag-01-retained-residual-workflow",
            "process_flow",
            "From Signed Merchant to Audited Residual",
            "Five operating stages separate payment volume from operator earnings.",
            1,
            "operating_framework",
            (
                "The revenue basis is retained ISO residuals, gateway markups, and "
                "ATM surcharge shares. Merchant settlement funds and ATM vault cash "
                "are excluded. ASC 606 principal-versus-agent assessment follows "
                "the actual contracts; this model uses the specified retained basis."
            ),
            (
                "Own the contract, verify the boarding decision, and reconcile the "
                "retained payment before treating an account as productive."
            ),
            [
                (
                    "Source and qualify",
                    "Verify merchant and venue fit",
                    1.0,
                    (
                        "Capture merchant category, ownership, statements, refund "
                        "patterns, venue traffic, and placement rights in IRIS CRM; "
                        "reject prohibited activity before quoting."
                    ),
                ),
                (
                    "Price the retained spread",
                    "Model Schedule A and venue shares",
                    2.0,
                    (
                        "Calculate residuals after processor deductions and ATM "
                        "venue shares; document gateway markup, minimums, clawbacks, "
                        "reserve exposure, and residual assignment rights."
                    ),
                ),
                (
                    "Submit transparent underwriting",
                    "Sponsor decides acceptance and reserves",
                    3.0,
                    (
                        "Submit accurate ownership, merchant category, websites, "
                        "fulfillment terms, and processing history. Never split "
                        "transactions across MIDs to conceal risk or thresholds."
                    ),
                ),
                (
                    "Activate and monitor",
                    "Test pricing, disclosures, and telemetry",
                    4.0,
                    (
                        "Test debit exclusions and credit-price presentation; "
                        "configure supported Verifi RDR or Ethoca workflows, ATM "
                        "fee election, remote telemetry, and vault-cash alerts."
                    ),
                ),
                (
                    "Audit and retain",
                    "Tie statements to bank receipts",
                    5.0,
                    (
                        "Reconcile IRIS CRM residual imports against Schedule A "
                        "and sponsor statements; investigate missing MIDs, rate "
                        "compression, surcharge deductions, attrition, and cash variances."
                    ),
                ),
            ],
        ),
        (
            "diag-02-merchant-cohort-conversion",
            "funnel",
            "A Nested Merchant Acquisition Cohort",
            "400 prospects become 25 active merchants over an illustrative 120 days.",
            6,
            "illustrative_model",
            (
                "Every stage is a subset of the preceding stage; these are planning "
                "counts, not observed conversion results. First deal timing remains "
                "1–4 months. The separate ATM portfolio is excluded from this funnel."
            ),
            (
                "At steady state, 25 merchants retaining $15,000 annually each "
                "contribute $375,000; ten separately sourced ATM venues retaining "
                "$7,000 each complete the $445,000 Base revenue case."
            ),
            [
                (
                    "Named prospects",
                    "400 merchants; 100% starting cohort",
                    400.0,
                    (
                        "Record identifiable businesses with permitted categories, "
                        "reachable decision-makers, serviceable locations, and an "
                        "explicit reason to reconsider their existing processing arrangement."
                    ),
                ),
                (
                    "Qualified statement audits",
                    "200 merchants; 50% of prior stage",
                    200.0,
                    (
                        "Obtain authorized statements and confirm ownership, "
                        "processing needs, renewal timing, current pricing, and "
                        "risk fit before allocating proposal effort."
                    ),
                ),
                (
                    "Documented proposals",
                    "100 merchants; 50% of prior stage",
                    100.0,
                    (
                        "Present itemized pricing and service terms; calculate "
                        "retained contribution after upstream deductions rather "
                        "than treating interchange or merchant settlement as revenue."
                    ),
                ),
                (
                    "Complete sponsor submissions",
                    "40 merchants; 40% of prior stage",
                    40.0,
                    (
                        "Submit complete applications with genuine business "
                        "activity, required evidence, and disclosed processing history; "
                        "submission does not imply sponsor acceptance."
                    ),
                ),
                (
                    "Active retained accounts",
                    "25 merchants; 62.5% of prior stage",
                    25.0,
                    (
                        "Count only live accounts with reconciled processing. "
                        "Illustrative annual yield is $500,000 monthly merchant "
                        "volume times 12 times a 0.25% retained spread, or $15,000."
                    ),
                ),
            ],
        ),
        (
            "diag-03-base-owner-profit-waterfall",
            "waterfall",
            "Base Case: $445,000 Revenue to $189,125 Owner Profit",
            "Four expense deductions reconcile exactly to a 42.5% annual net margin.",
            3,
            "illustrative_model",
            (
                "USD annually. The first and last bars are absolute totals; the "
                "four intervening bars are negative deltas. Expense allocations "
                "are illustrative and reconcile to the canonical scorecard. "
                "Revenue is already net of upstream retained-share deductions."
            ),
            (
                "$445,000 − $110,000 − $78,000 − $59,875 − $8,000 "
                "= $189,125; $189,125 / $445,000 = 42.5%."
            ),
            [
                (
                    "Retained operator revenue",
                    "$445,000 annual starting total",
                    445000.0,
                    (
                        "Base revenue comprises $375,000 retained merchant and "
                        "gateway income plus $70,000 retained ATM surcharge income. "
                        "Merchant card volume and vault cash contribute zero revenue."
                    ),
                ),
                (
                    "Acquisition commissions",
                    "Subtract $110,000 annual sales expense",
                    -110000.0,
                    (
                        "Pay operator-side referral and sales compensation under "
                        "documented schedules. These costs are distinct from "
                        "processor and venue shares already removed from revenue."
                    ),
                ),
                (
                    "Contract servicing",
                    "Subtract $78,000 annual delivery expense",
                    -78000.0,
                    (
                        "Fund contractor boarding, residual auditing, dispute "
                        "operations, and ATM field-service work; the full-time "
                        "owner's compensation is not deducted again from owner profit."
                    ),
                ),
                (
                    "Fixed operating overhead",
                    "Subtract $59,875 annual overhead expense",
                    -59875.0,
                    (
                        "Budget CRM, telemetry, insurance, equipment leases, "
                        "bookkeeping, and administration. Average fixed overhead "
                        "is $4,989.58 monthly; total expenses also include variable costs."
                    ),
                ),
                (
                    "Loss and remediation expense",
                    "Subtract $8,000 annual risk expense",
                    -8000.0,
                    (
                        "Model operator-borne losses and remediation costs under "
                        "the relevant contracts. Restricted reserve deposits are "
                        "not automatically expenses, and recoverable vault cash is excluded."
                    ),
                ),
                (
                    "Annual owner net profit",
                    "$189,125 ending total; 42.5% margin",
                    189125.0,
                    (
                        "Canonical checks: Conservative $90,000 times 30% equals "
                        "$27,000; Base $445,000 times 42.5% equals $189,125; "
                        "Scaled $800,000 times 55% equals $440,000."
                    ),
                ),
            ],
        ),
        (
            "diag-04-retained-payment-rail-yields",
            "horizontal_bars",
            "Retained Yield by Merchant Segment and Payment Rail",
            "Illustrative operator dollars retained per 1,000 successful payment events.",
            2,
            "illustrative_model",
            (
                "Card examples assume a $50 average ticket. Gateway yield is a "
                "separate component, not an additional merchant cohort. ATM events "
                "are withdrawals, not purchases; differing event economics prevent "
                "direct conclusions about account profitability. Bars are not additive."
            ),
            (
                "Price retained yield after upstream splits, then subtract "
                "operator acquisition, servicing, and loss costs."
            ),
            [
                (
                    "Card-present retail residual",
                    "$120 retained per 1,000 purchases",
                    120.0,
                    (
                        "One thousand $50 purchases produce $50,000 merchant "
                        "volume; a 24-basis-point retained residual produces $120 "
                        "before operator expenses, without assuming debit surcharges."
                    ),
                ),
                (
                    "Restaurant processing residual",
                    "$160 retained per 1,000 purchases",
                    160.0,
                    (
                        "A 32-basis-point retained residual on $50,000 merchant "
                        "volume produces $160; verify tip adjustments, funding "
                        "timing, terminal support, and rate-matching exposure."
                    ),
                ),
                (
                    "Gateway transaction markup",
                    "$90 retained per 1,000 transactions",
                    90.0,
                    (
                        "A $0.09 retained gateway markup produces $90 across "
                        "1,000 transactions; deduct the upstream gateway charge "
                        "before measuring this component and avoid residual double counting."
                    ),
                ),
                (
                    "Sponsor-approved specialty merchant",
                    "$250 retained per 1,000 purchases",
                    250.0,
                    (
                        "A 50-basis-point retained residual on $50,000 merchant "
                        "volume produces $250. Model reserves, disputes, and service "
                        "burden separately; higher yield does not establish higher profit."
                    ),
                ),
                (
                    "Exclusive-venue ATM withdrawals",
                    "$1,750 retained per 1,000 withdrawals",
                    1750.0,
                    (
                        "A $3.00 surcharge less $1.25 combined venue and upstream "
                        "shares retains $1.75 per withdrawal. Four thousand annual "
                        "withdrawals retain $7,000 before operator servicing expenses."
                    ),
                ),
            ],
        ),
        (
            "diag-05-statutory-and-risk-preflight",
            "decision_tree",
            "Four Checks Before Account Activation",
            "Each failed check routes to a specific correction or a stopped submission.",
            5,
            "operating_framework",
            (
                "Numeric values indicate check order, not risk scores. All four "
                "checks must pass for the relevant product; statutes, network "
                "contracts, and sponsor requirements impose distinct obligations."
            ),
            (
                "Document evidence and the decision owner; never use alternate "
                "MIDs or product labels to bypass an adverse underwriting decision."
            ),
            [
                (
                    "Credit and debit pricing",
                    "Pass: configure; fail: reprice and retest",
                    1.0,
                    (
                        "Apply current Visa and Mastercard debit-surcharge prohibitions "
                        "separately from 15 U.S.C. 1693o-2 and 12 CFR 235.7 routing "
                        "rules. For New York, test displayed credit prices and surcharge "
                        "limits against General Business Law section 518."
                    ),
                ),
                (
                    "ATM fee disclosure",
                    "Pass: enable; fail: disable fee-bearing service",
                    2.0,
                    (
                        "Under 12 CFR 1005.16, disclose the fee amount on screen "
                        "or paper before commitment and obtain the consumer's "
                        "election to continue. Preserve test evidence and confirm "
                        "that cancellation avoids the fee."
                    ),
                ),
                (
                    "Service scope and cash custody",
                    "Pass: document scope; fail: stop added services",
                    3.0,
                    (
                        "Analyze actual services under 31 CFR 1010.100(ff); "
                        "withdrawal-only operation does not by itself establish "
                        "money-transmitter status. Added transmission or exchange "
                        "services require separate classification and any applicable "
                        "31 CFR 1022.380 registration work."
                    ),
                ),
                (
                    "Sponsor underwriting and data controls",
                    "Pass: activate; fail: remediate or decline",
                    4.0,
                    (
                        "Verify sponsor acceptance, merchant category, applicable "
                        "MATCH screening, reserves, PCI DSS responsibilities, and "
                        "dispute exposure. Assess 15 U.S.C. 6801 and 16 CFR 314.3 "
                        "where applicable; use Verifi RDR and Ethoca without "
                        "suppressing required sponsor reporting."
                    ),
                ),
            ],
        ),
        (
            "diag-06-four-to-six-person-pod",
            "org_architecture",
            "One Accountable Owner, Three Contract Specialists",
            "The four-person Base pod expands to six people only in the Scaled case.",
            11,
            "operating_framework",
            (
                "FT means full-time and C means contractor; contractor seats are "
                "people, not assumed full-time equivalents. Numeric values show "
                "Base seat occupancy: one for each active seat and zero for each "
                "Scaled-only addition. Sponsor personnel remain outside the pod."
            ),
            (
                "Conservative and Base use 1 FT + 3 C; Scaled uses 2 FT + 4 C. "
                "Automation supports accountable operators rather than removing ownership."
            ),
            [
                (
                    "Owner and sponsor lead",
                    "Base seat: one full-time principal",
                    1.0,
                    (
                        "Own pricing authority, sponsor relationships, placement "
                        "contracts, cash controls, attrition review, and the annual "
                        "owner-profit reconciliation; resolve exceptions raised by contractors."
                    ),
                ),
                (
                    "Merchant acquisition specialist",
                    "Base seat: one sales contractor",
                    1.0,
                    (
                        "Maintain qualified cohorts, collect authorized statements, "
                        "prepare accurate proposals, and negotiate venue introductions "
                        "without promising sponsor acceptance or unsupported savings."
                    ),
                ),
                (
                    "Boarding and residual specialist",
                    "Base seat: one operations contractor",
                    1.0,
                    (
                        "Operate IRIS CRM, reconcile Schedule A residuals, maintain "
                        "boarding evidence, review Verifi RDR and Ethoca outcomes, "
                        "and escalate unresolved disputes or reserve changes."
                    ),
                ),
                (
                    "ATM field-service specialist",
                    "Base seat: one service contractor",
                    1.0,
                    (
                        "Coordinate authorized replenishment, inspect terminals, "
                        "respond to telemetry alarms, and reconcile service tickets "
                        "against cash-custodian records without mixing vault cash and revenue."
                    ),
                ),
                (
                    "Portfolio operations lead",
                    "Scaled addition: one full-time operator",
                    0.0,
                    (
                        "Add ownership of daily exception queues, merchant retention, "
                        "sponsor reporting, and contractor quality when measured "
                        "workload supports the Scaled six-person operating model."
                    ),
                ),
                (
                    "Dispute and support specialist",
                    "Scaled addition: one specialist contractor",
                    0.0,
                    (
                        "Add dedicated case handling, evidence collection, and "
                        "merchant support; the resulting team totals two full-time "
                        "people and four contractors, not six full-time employees."
                    ),
                ),
            ],
        ),
        (
            "diag-07-startup-capital-allocation",
            "stacked_comparison",
            "Allocate Startup Cash Without Counting Vault Cash",
            "Four buckets reconcile to $8,000 lean, $25,000 working, and $45,000 expanded.",
            4,
            "illustrative_model",
            (
                "Numeric values encode the $25,000 working plan. Each value string "
                "also specifies lean and expanded allocations, in that order. "
                "These are alternative budgets, not cumulative spending rounds. "
                "Leased or venue-owned terminals and separately supplied vault cash "
                "are assumed; operator-funded cash inventory needs additional capital."
            ),
            (
                "Lean: $2,000 + $1,500 + $2,500 + $2,000 = $8,000. "
                "Working: $4,500 + $6,000 + $9,000 + $5,500 = $25,000. "
                "Expanded: $8,000 + $10,000 + $18,000 + $9,000 = $45,000."
            ),
            [
                (
                    "Contracting and operating setup",
                    "Lean $2,000; working $4,500; expanded $8,000",
                    4500.0,
                    (
                        "Fund entity setup, insurance deposits, sponsor onboarding, "
                        "and review of residual ownership, termination, venue "
                        "exclusivity, equipment responsibility, and cash-custody agreements."
                    ),
                ),
                (
                    "CRM and terminal deployment",
                    "Lean $1,500; working $6,000; expanded $10,000",
                    6000.0,
                    (
                        "Fund IRIS CRM configuration, residual import testing, "
                        "telemetry setup, terminal lease deposits, connectivity, "
                        "and installation; exclude any assumption of outright fleet purchase."
                    ),
                ),
                (
                    "Acquisition and pilot execution",
                    "Lean $2,500; working $9,000; expanded $18,000",
                    9000.0,
                    (
                        "Fund targeted outreach, site surveys, travel, demonstrations, "
                        "and initial contractor work. Release spending against "
                        "documented cohort progress rather than unverified transaction forecasts."
                    ),
                ),
                (
                    "Liquidity and service buffer",
                    "Lean $2,000; working $5,500; expanded $9,000",
                    5500.0,
                    (
                        "Hold operating cash for service incidents and residual "
                        "payment lags; keep sponsor collateral separately identified. "
                        "At Base fixed overhead, $5,500 covers approximately 1.1 months."
                    ),
                ),
            ],
        ),
        (
            "diag-08-first-thirty-days",
            "timeline_roadmap",
            "The First 30 Days: Build Evidence Before Volume",
            "Four weekly milestones prepare a defensible merchant and ATM pilot.",
            12,
            "operating_framework",
            (
                "Numeric values indicate the final day of each milestone. "
                "The 30-day sprint prepares acquisition and operations; first "
                "deal timing remains 1–4 months, and the funnel spans an "
                "illustrative 120-day cohort rather than this sprint."
            ),
            (
                "Finish the month with reviewed terms, a nested prospect cohort, "
                "tested controls, and a reconciled operating model."
            ),
            [
                (
                    "Days 1-7",
                    "Select sponsor and inspect contract economics",
                    7.0,
                    (
                        "Owner compares Schedule A schedules, residual ownership, "
                        "clawbacks, reserve terms, and supported categories. Deliver "
                        "a written retained-revenue model and an ATM cash-custody plan."
                    ),
                ),
                (
                    "Days 8-14",
                    "Build qualified outreach and site evidence",
                    14.0,
                    (
                        "Sales contractor creates the prospect register, requests "
                        "authorized statements, and surveys suitable venues. Deliver "
                        "stage definitions, pricing worksheets, and documented placement "
                        "requirements without counting unsigned prospects as revenue."
                    ),
                ),
                (
                    "Days 15-21",
                    "Test boarding, pricing, and service controls",
                    21.0,
                    (
                        "Operations contractor configures IRIS CRM and residual "
                        "imports; field specialist tests telemetry and ATM fee "
                        "disclosure. Record debit-pricing tests, dispute escalation "
                        "ownership, and sponsor submission completeness."
                    ),
                ),
                (
                    "Days 22-30",
                    "Submit pilots and reconcile readiness",
                    30.0,
                    (
                        "Submit complete applications and negotiate placement "
                        "terms. If accepted and installed, verify live results; "
                        "otherwise record sponsor dependencies. Reconcile startup "
                        "cash, fixed overhead, and all three canonical profit cases."
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
