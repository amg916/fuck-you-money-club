from __future__ import annotations

VOLUME_036_SUBTITLE = (
    "The Complete Playbook for GPU Compute & Telecom Capacity Arbitrage: "
    "$150,000–$1,200,000 USD in Annual Gross Billings, "
    "Built Around a 1 FT + 2 C Pod (3 People), Scaling to 5"
)

VOLUME_036_POSITIONING_ALTERNATIVES = [
    {
        "title": "The Reserved-to-On-Demand Compute Desk",
        "subtitle": (
            "Turn authorized H100, H200, and B200 capacity reservations into "
            "metered GPU-hour products with prepaid balances and enforceable limits."
        ),
        "audience": (
            "Infrastructure operators who can negotiate resale rights, isolate "
            "customer workloads, and manage utilization against fixed supplier commits."
        ),
        "research_basis": (
            "Positioning centers on capacity control rather than hardware ownership. "
            "Export classification, destination, end-user, and end-use screening "
            "must follow the current EAR where applicable; GPU model names alone "
            "do not resolve transaction eligibility. NIST SP 800-190 supplies "
            "container-security considerations, not proof of tenant isolation."
        ),
        "sources": [
            "https://www.ecfr.gov/current/title-15/subtitle-B/chapter-VII/subchapter-C/part-742",
            "https://www.ecfr.gov/current/title-15/subtitle-B/chapter-VII/subchapter-C/part-744",
            "https://csrc.nist.gov/pubs/sp/800/190/final",
        ],
        "validation_status": "Source-informed editorial positioning; not market-tested.",
    },
    {
        "title": "The Prepaid Inference Routing Desk",
        "subtitle": (
            "Sell measured inference outcomes while routing eligible requests "
            "across providers by effective cost, latency, and retention terms."
        ),
        "audience": (
            "API operators serving repeat inference buyers who need predictable "
            "spend controls, documented service limits, and verifiable data handling."
        ),
        "research_basis": (
            "LiteLLM and vLLM support the operating concept, while the cited "
            "materials ground advertising accuracy and access-control practices. "
            "Under 15 U.S.C. 45, unsupported security or retention representations "
            "create concrete exposure. NIST SP 800-53 provides control patterns; "
            "neither source establishes achievable routing savings."
        ),
        "sources": [
            "https://www.law.cornell.edu/uscode/text/15/45",
            "https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final",
        ],
        "validation_status": "Source-informed editorial positioning; not market-tested.",
    },
    {
        "title": "The Screened Wholesale Telecom Desk",
        "subtitle": (
            "Broker authorized SIP, registered business messaging, and documented "
            "IPv4 capacity without letting abuse consume the wholesale spread."
        ),
        "audience": (
            "Telecom operators with carrier relationships, traceback procedures, "
            "numbering controls, and the ability to classify their actual service role."
        ),
        "research_basis": (
            "47 CFR 64.6301 and 64.6305 establish role-dependent caller "
            "authentication and robocall-mitigation requirements. 47 CFR 54.711 "
            "addresses contributor reporting, and 47 U.S.C. 227 governs covered "
            "calling and messaging conduct. TCR registration is a carrier-ecosystem "
            "requirement, distinct from statutory permission to contact recipients."
        ),
        "sources": [
            "https://www.law.cornell.edu/cfr/text/47/64.6301",
            "https://www.law.cornell.edu/cfr/text/47/64.6305",
            "https://www.law.cornell.edu/cfr/text/47/54.711",
            "https://www.law.cornell.edu/uscode/text/47/227",
        ],
        "validation_status": "Source-informed editorial positioning; not market-tested.",
    },
]


def build_volume_036_diagrams_data() -> list[dict]:
    specs = [
        (
            "diag-01-reserved-capacity-to-collected-cash",
            "process_flow",
            "Broker Capacity Without Losing Control of Consumption",
            "Five operating stages connect supplier rights to reconciled customer usage.",
            1,
            "operating_framework",
            (
                "The operator resells only contractually authorized capacity. "
                "Prepayment controls credit exposure but does not eliminate "
                "chargebacks, supplier commits, or service-credit obligations."
            ),
            (
                "Keep gross customer billings, upstream supplier charges, and "
                "retained contribution in separate ledger accounts. A customer's "
                "wallet deposit is not earned service revenue before delivery."
            ),
            [
                (
                    "Secure supply rights",
                    "Document capacity, resale rights, and supplier limits",
                    1.0,
                    (
                        "Negotiate GPU reservation windows, carrier termination rates, "
                        "IPv4 lease authority, cancellation terms, and measurable SLAs. "
                        "Track minimum commits separately from consumed units."
                    ),
                ),
                (
                    "Screen and fund",
                    "Identify buyers before activating prepaid consumption limits",
                    2.0,
                    (
                        "Verify business identity and intended workloads, enforce "
                        "the AUP, and fund a Stripe-backed internal credit ledger. "
                        "Reject abusive mining, spoofing, and unauthorized calling."
                    ),
                ),
                (
                    "Route and isolate",
                    "Allocate eligible workloads within explicit spend ceilings",
                    3.0,
                    (
                        "Use LiteLLM or vLLM for supported inference paths and "
                        "least-cost routing for eligible SIP routes. Apply tenant "
                        "isolation, destination restrictions, and tested failover limits."
                    ),
                ),
                (
                    "Meter and reconcile",
                    "Match customer usage with independent supplier records",
                    4.0,
                    (
                        "Combine request-level token records, scheduler allocation "
                        "intervals, DCGM health telemetry, and carrier call-detail "
                        "records. DCGM utilization alone is not a billing ledger."
                    ),
                ),
                (
                    "Collect and rebalance",
                    "Recognize delivered service and reset exposure daily",
                    5.0,
                    (
                        "Debit wallets idempotently, recognize delivered units, "
                        "reconcile supplier invoices, and stop consumption at limits. "
                        "Reprice expiring GPU reservations before generation-driven "
                        "price compression erases their spread."
                    ),
                ),
            ],
        ),
        (
            "diag-02-qualified-buyer-cohort",
            "funnel",
            "One Cohort, Five Observable Conversion Steps",
            "Track qualified demand before increasing noncancelable capacity.",
            6,
            "illustrative_model",
            (
                "Illustrative 90-day acquisition cohort, not a revenue forecast. "
                "Every stage is a subset of the preceding stage; all counts "
                "represent buyer organizations rather than contacts or API keys."
            ),
            (
                "The cohort narrows 200 → 80 → 40 → 20 → 10. Sequential conversion "
                "is 40%, 50%, 50%, and 50%; overall conversion is 5%. "
                "Ten repeat buyers do not by themselves establish $675,000 billings."
            ),
            [
                (
                    "Documented prospects",
                    "200 organizations with observable recurring capacity needs",
                    200.0,
                    (
                        "Build a named account list from permitted research and "
                        "existing relationships. Record workload type, buyer role, "
                        "current supplier arrangement, and likely purchasing window."
                    ),
                ),
                (
                    "Qualified demand",
                    "80 organizations with budget and technical fit",
                    80.0,
                    (
                        "Forty percent of the original cohort confirms budget, "
                        "eligible destinations, expected usage, and acceptable "
                        "retention terms during a documented discovery conversation."
                    ),
                ),
                (
                    "Validated economics",
                    "40 organizations pass workload and spread checks",
                    40.0,
                    (
                        "Half of qualified organizations supplies an authorized "
                        "benchmark or traffic sample. Compare effective unit costs, "
                        "p95 latency, retry burden, and minimum-commit exposure."
                    ),
                ),
                (
                    "Funded pilots",
                    "20 organizations prepay bounded production pilot balances",
                    20.0,
                    (
                        "Half of validated organizations accepts the service terms "
                        "and funds a capped pilot. Record wallet liability separately "
                        "from recognized revenue and enforce hard usage limits."
                    ),
                ),
                (
                    "Repeat consumption",
                    "10 organizations complete a second paid cycle",
                    10.0,
                    (
                        "Half of funded pilots consumes delivered service and "
                        "purchases another cycle. Expand commitments only against "
                        "observed repeat demand and customer concentration limits."
                    ),
                ),
            ],
        ),
        (
            "diag-03-base-case-gross-to-owner-profit",
            "waterfall",
            "Base Case: $675,000 Billings to $189,000 Owner Profit",
            "Separate upstream pass-through economics from retained operating performance.",
            3,
            "illustrative_model",
            (
                "Annual USD; canonical retained_share is 0.65. The $168,000 "
                "operating-cost and $81,750 variable-cost allocations are illustrative "
                "components of the required $249,750 post-upstream cost total. "
                "Bars 1, 3, and 6 are absolute totals; bars 2, 4, and 5 "
                "are signed movements. Never add the retained subtotal twice."
            ),
            (
                "$675,000 − $236,250 = $438,750 retained contribution; "
                "$438,750 − $168,000 − $81,750 = $189,000 owner profit. "
                "Profit is 28.0% of gross billings and 43.08% of retained "
                "contribution. The scorecard's ASC 606 net presentation assumes "
                "an agent arrangement; assess principal-versus-agent status "
                "separately for each promised service."
            ),
            [
                (
                    "Gross customer billings",
                    "$675,000 annual delivered compute and telecom billings",
                    675000.0,
                    (
                        "Opening total equals $56,250 monthly on an annualized "
                        "basis. These are operator customer billings, not customers' "
                        "underlying commerce, token resale proceeds, or enterprise revenue."
                    ),
                ),
                (
                    "Upstream capacity cost",
                    "Subtract $236,250 for upstream capacity and termination",
                    -236250.0,
                    (
                        "Thirty-five percent of gross billings goes to supplier "
                        "capacity and carrier termination, including the modeled "
                        "effect of commits. Do not deduct these charges again below."
                    ),
                ),
                (
                    "Retained contribution",
                    "$438,750 remains after the upstream supplier deduction",
                    438750.0,
                    (
                        "Subtotal equals 65% of gross billings and $36,562.50 "
                        "monthly. Use this denominator for the retained-margin "
                        "view; it is not the owner's take-home profit."
                    ),
                ),
                (
                    "Recurring operating costs",
                    "Subtract $168,000 for recurring pod and platform operations",
                    -168000.0,
                    (
                        "Illustrative expense envelope equals $14,000 monthly, "
                        "the canonical range ceiling. Allocate it to contractor "
                        "support, observability, administration, and recurring tooling."
                    ),
                ),
                (
                    "Variable operating costs",
                    "Subtract $81,750 for variable fulfillment and collection costs",
                    -81750.0,
                    (
                        "Illustrative annual allocation covers processing fees, "
                        "chargeback losses, service credits, and non-upstream variable "
                        "support. Keep these outside the recurring monthly envelope "
                        "and avoid duplicating supplier capacity charges."
                    ),
                ),
                (
                    "Annual owner profit",
                    "$189,000 remains after all modeled operating deductions",
                    189000.0,
                    (
                        "Closing total equals $15,750 monthly on an annualized "
                        "basis. Preserve the canonical owner-profit convention; "
                        "personal taxes and an additional imputed owner salary "
                        "are not separately modeled."
                    ),
                ),
            ],
        ),
        (
            "diag-04-subniche-retained-yield",
            "horizontal_bars",
            "Compare Retained Yield Before Operating Costs",
            "Five illustrative product spreads reconcile to the 65% retained-share anchor.",
            2,
            "illustrative_model",
            (
                "Numeric values are retained-contribution percentages, not owner "
                "profit margins or observed market quotes. Assigning $135,000 "
                "annual gross billings to each of five niches creates an "
                "illustrative equal-weight Base mix totaling $675,000."
            ),
            (
                "Retained contributions total $91,800 + $83,700 + $101,250 + "
                "$74,250 + $87,750 = $438,750. The weighted retained yield is "
                "65%; payment-processing and other operating costs remain below "
                "this measure. Actual product mixes require fresh supplier quotes."
            ),
            [
                (
                    "H100 and H200 reservations",
                    "68% retained yield on authorized GPU-hour resale",
                    68.0,
                    (
                        "At $135,000 gross billings, upstream cost is $43,200 "
                        "and retained contribution is $91,800. Prefer prepaid "
                        "business balances; idle reserved hours still consume cash."
                    ),
                ),
                (
                    "B200 capacity windows",
                    "62% retained yield on bounded accelerated-compute windows",
                    62.0,
                    (
                        "At $135,000 gross billings, upstream cost is $51,300 "
                        "and retained contribution is $83,700. Match customer "
                        "reservation terms to supply; benchmark before promising throughput."
                    ),
                ),
                (
                    "Multi-provider inference",
                    "75% retained yield on normalized delivered inference",
                    75.0,
                    (
                        "At $135,000 gross billings, upstream cost is $33,750 "
                        "and retained contribution is $101,250. Meter input, output, "
                        "cache, and retries separately before debiting prepaid credits."
                    ),
                ),
                (
                    "SIP and business messaging",
                    "55% retained yield after carrier and messaging charges",
                    55.0,
                    (
                        "At $135,000 gross billings, upstream cost is $60,750 "
                        "and retained contribution is $74,250. Include carrier "
                        "surcharges and registration costs consistently; restrict "
                        "high-cost destinations and abnormal traffic."
                    ),
                ),
                (
                    "Authorized IPv4 leasing",
                    "65% retained yield on documented address-capacity leases",
                    65.0,
                    (
                        "At $135,000 gross billings, upstream cost is $47,250 "
                        "and retained contribution is $87,750. Verify lease authority, "
                        "routing authorization, abuse history, and return conditions "
                        "before accepting customer funds."
                    ),
                ),
            ],
        ),
        (
            "diag-05-preflight-service-eligibility",
            "decision_tree",
            "Four Pre-Flight Checks Before Customer Traffic",
            "Each service follows every applicable branch; unresolved checks block that service.",
            5,
            "operating_framework",
            (
                "Numeric values indicate check order, not risk probabilities. "
                "Evaluate the operator's actual role, destination, service, and "
                "contract terms. Telecom requirements do not automatically apply "
                "to a compute-only product."
            ),
            (
                "A pass permits movement to the next applicable check. A failed "
                "check sends the affected service back for remediation, not "
                "around the control. Recheck changed customers, destinations, "
                "providers, and product capabilities."
            ),
            [
                (
                    "Capacity and workload rights",
                    "Pass only with authorized supply and screened workloads",
                    1.0,
                    (
                        "Verify resale rights and EAR applicability under "
                        "15 CFR parts 742 and 744, including relevant end-user "
                        "and end-use restrictions. Test tenant isolation and "
                        "upstream retention settings; otherwise withhold the "
                        "affected workload or zero-retention offering."
                    ),
                ),
                (
                    "Voice provider obligations",
                    "Pass only after role-specific authentication and mitigation checks",
                    2.0,
                    (
                        "Map the service role to 47 CFR 64.6301 and 64.6305 "
                        "for applicable STIR/SHAKEN, Robocall Mitigation Database "
                        "certification, and traffic-acceptance duties. Verify supplier "
                        "status and traceback procedures; unresolved requirements "
                        "block voice activation."
                    ),
                ),
                (
                    "Messaging and calling use",
                    "Pass only with documented lawful traffic and carrier registration",
                    3.0,
                    (
                        "Apply 47 U.S.C. 227 and 47 CFR 64.1200 to covered "
                        "traffic, including applicable permission, revocation, and "
                        "calling restrictions. Complete carrier-required 10DLC TCR "
                        "brand and campaign registration; registration alone does "
                        "not establish permission to message."
                    ),
                ),
                (
                    "Reporting and exposure",
                    "Pass only after reporting classification and funding controls",
                    4.0,
                    (
                        "Classify telecom contribution and reporting duties under "
                        "47 CFR 54.706 and 54.711 using current FCC Form 499-A "
                        "instructions; contribution exemptions do not automatically "
                        "remove filing duties. Confirm prepaid limits, refund rules, "
                        "chargeback reserves, and emergency traffic shutoff ownership."
                    ),
                ),
            ],
        ),
        (
            "diag-06-three-to-five-person-pod",
            "org_architecture",
            "Three Seats Launch; Five Seats Support the Scaled Case",
            "Keep commercial authority, platform execution, and telecom operations explicit.",
            11,
            "operating_framework",
            (
                "Each numeric value represents one person, not one full-time "
                "equivalent. Conservative and Base use 1 FT + 2 C; Scaled uses "
                "2 FT + 3 C. The last two seats are additions, not initial hires."
            ),
            (
                "Conservative: $150,000 gross, $97,500 retained, $27,000 owner "
                "profit; margins 18% gross and 27.69% retained. Base: $675,000 "
                "gross, $438,750 retained, $189,000 profit; margins 28.0% and "
                "43.08%. Scaled: $1,200,000 gross, $780,000 retained, $456,000 "
                "profit; margins 38% and 58.46%. Retained share stays 65%."
            ),
            [
                (
                    "Owner and commercial lead",
                    "Initial full-time seat owns commitments and customer economics",
                    1.0,
                    (
                        "Set pricing floors, negotiate supplier rights, maintain "
                        "cash forecasts, and resolve customer concentration exposure. "
                        "Authorize commitment increases only after reviewing "
                        "utilization, churn, and available operating cash."
                    ),
                ),
                (
                    "Platform engineering contractor",
                    "Initial contractor owns routing, isolation, and usage integrity",
                    1.0,
                    (
                        "Maintain LiteLLM or vLLM, tenant controls, DCGM collection, "
                        "idempotent wallet debits, and usage reconciliation. Publish "
                        "tested incident runbooks and instrument supplier-cost drift."
                    ),
                ),
                (
                    "Telecom operations contractor",
                    "Initial contractor owns carrier provisioning and traffic exceptions",
                    1.0,
                    (
                        "Maintain SIP least-cost routes, carrier limits, 10DLC "
                        "provisioning records, traceback responses, and applicable "
                        "filing calendars. Escalate suspicious traffic immediately "
                        "rather than waiting for monthly settlement."
                    ),
                ),
                (
                    "Customer operations specialist",
                    "Scaled addition supplies the second full-time operating seat",
                    1.0,
                    (
                        "Own onboarding, support queues, renewal preparation, and "
                        "service-credit evidence. Add this seat when measured "
                        "support load threatens response targets and retained "
                        "contribution can support the recurring expense."
                    ),
                ),
                (
                    "Security and reconciliation contractor",
                    "Scaled addition supplies the third contracted specialist seat",
                    1.0,
                    (
                        "Independently sample access controls, supplier invoices, "
                        "wallet balances, and abuse investigations. Separate "
                        "reconciliation review from the person changing rates "
                        "or issuing customer credits."
                    ),
                ),
            ],
        ),
        (
            "diag-07-startup-capital-allocation",
            "stacked_comparison",
            "Allocate $10,000–$60,000 Before Expanding Commitments",
            "Four buckets illustrate a $30,000 working launch budget.",
            4,
            "illustrative_model",
            (
                "Numeric values show the $30,000 reference allocation in USD. "
                "Each stage also gives low-capital and upper-capital allocations; "
                "the three complete budgets total $10,000, $30,000, and $60,000. "
                "These are capital envelopes, not annual expense forecasts."
            ),
            (
                "Low budget: $4,000 + $2,500 + $2,000 + $1,500 = $10,000. "
                "Reference budget: $12,000 + $8,000 + $6,000 + $4,000 = $30,000. "
                "Upper budget: $24,000 + $16,000 + $12,000 + $8,000 = $60,000. "
                "Customer prepaid balances remain service obligations, not free capital."
            ),
            [
                (
                    "Supplier deposits and first capacity",
                    "$12,000 reference allocation for bounded upstream supply access",
                    12000.0,
                    (
                        "Allocate $4,000 at the low budget and $24,000 at the "
                        "upper budget. Favor cancellable pilot capacity; record "
                        "refundable deposits separately from consumed services and "
                        "do not treat the deposit as recurring profit expense."
                    ),
                ),
                (
                    "Settlement and loss reserve",
                    "$8,000 reference allocation for timing gaps and service losses",
                    8000.0,
                    (
                        "Allocate $2,500 at the low budget and $16,000 at the "
                        "upper budget. Cover supplier settlement timing, refunds, "
                        "and chargeback exposure with operator cash rather than "
                        "assuming card-funded wallets cannot reverse."
                    ),
                ),
                (
                    "Metering and tenant controls",
                    "$6,000 reference allocation for instrumentation and containment work",
                    6000.0,
                    (
                        "Allocate $2,000 at the low budget and $12,000 at the "
                        "upper budget. Implement wallet reconciliation, scoped "
                        "credentials, routing limits, workload isolation tests, "
                        "and retention verification before raising usage ceilings."
                    ),
                ),
                (
                    "Onboarding and operating setup",
                    "$4,000 reference allocation for qualified pilots and service setup",
                    4000.0,
                    (
                        "Allocate $1,500 at the low budget and $8,000 at the "
                        "upper budget. Fund supplier diligence, applicable registrations, "
                        "contract review, and narrowly targeted pilot acquisition. "
                        "Release spending against completed operating evidence."
                    ),
                ),
            ],
        ),
        (
            "diag-08-thirty-day-launch-sprint",
            "timeline_roadmap",
            "Build the Evidence for a First Deal in 30 Days",
            "Four weekly milestones prepare a controlled commercial launch.",
            12,
            "operating_framework",
            (
                "Numeric values are milestone end days. The canonical time to "
                "first deal remains 1–4 months; this sprint establishes readiness "
                "and can finish before the first paid customer arrives."
            ),
            (
                "Sequence supply validation, metering, buyer qualification, and "
                "bounded activation. Do not convert an unfinished test, pending "
                "registration, or unsigned supplier offer into a completed launch claim."
            ),
            [
                (
                    "Days 1-7",
                    "Select one wedge and verify supplier economics",
                    7.0,
                    (
                        "Choose one GPU, inference, or telecom product. Obtain "
                        "written resale terms and comparable supplier quotes, "
                        "classify applicable service duties, and model utilization "
                        "break-even without treating prepaid deposits as revenue."
                    ),
                ),
                (
                    "Days 8-14",
                    "Build the wallet, meter, and controlled shutdown path",
                    14.0,
                    (
                        "Connect a Stripe test flow to an internal credit ledger. "
                        "Replay duplicate events, supplier outages, and exhausted "
                        "balances; test tenant isolation and retention settings "
                        "before enabling customer production credentials."
                    ),
                ),
                (
                    "Days 15-21",
                    "Qualify buyers and prove a bounded service benchmark",
                    21.0,
                    (
                        "Conduct discovery with named buyers and benchmark "
                        "authorized workloads or traffic. Complete applicable "
                        "carrier provisioning and registrations, document service "
                        "limits, and reject pilots whose effective unit economics "
                        "fail the price floor."
                    ),
                ),
                (
                    "Days 22-30",
                    "Run an eligible pilot or finish readiness evidence",
                    30.0,
                    (
                        "If contracts, funding, and applicable service requirements "
                        "are complete, activate a capped pilot and reconcile daily. "
                        "Otherwise finish test evidence and buyer follow-up without "
                        "buying speculative capacity or claiming a completed deal."
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
                dict(label=label, value=value, numeric_value=float(number), detail=detail)
                for label, value, number, detail in stages
            ],
        )
        for identifier, kind, title, subtitle, chapter, tag, note, caption, stages in specs
    ]
