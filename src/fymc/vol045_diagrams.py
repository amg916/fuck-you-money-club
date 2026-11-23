from __future__ import annotations

VOLUME_045_SUBTITLE = (
    "The Complete Playbook for No Surprises Act Recovery: "
    "$110,000–$900,000 USD in Annual Earned Fees, "
    "a 1 FT + 2 C Launch Pod, and Five-Person Scale"
)

VOLUME_045_POSITIONING_ALTERNATIVES = [
    {
        "title": "The Incremental-Cash Recovery Desk",
        "subtitle": (
            "Build a three-person physician recovery operation that earns its "
            "contingency share only after additional payer cash clears."
        ),
        "audience": (
            "Physician billing operators and revenue-cycle founders serving "
            "out-of-network emergency medicine, anesthesia, and diagnostic groups."
        ),
        "research_basis": (
            "Federal payment-dispute procedures create a defined recovery workflow, "
            "but an award and a bank deposit are different events. Position the "
            "service around claim-level collection reconciliation, verified "
            "incremental receipts, and a contractually defined fee base after "
            "unrecovered administrative fees, entity fees, and casework costs."
        ),
        "sources": [
            "https://www.law.cornell.edu/uscode/text/42/300gg-111",
            "https://www.ecfr.gov/current/title-45/section-149.510",
            "https://www.cms.gov/nosurprises",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Jurisdiction-First IDR Specialist",
        "subtitle": (
            "Reject the wrong payment rail before spending on an arbitration "
            "submission, then preserve every eligible federal deadline."
        ),
        "audience": (
            "Independent revenue-cycle teams handling mixed self-funded employer "
            "plans, fully insured plans, and state-regulated provider disputes."
        ),
        "research_basis": (
            "Applicable state law, All-Payer Model Agreements, plan funding, and "
            "service circumstances affect the payment route. ERISA status alone "
            "does not establish federal IDR eligibility. A documented routing "
            "decision reduces wasted entity fees and missed negotiation windows."
        ),
        "sources": [
            "https://www.ecfr.gov/current/title-45/section-149.30",
            "https://www.ecfr.gov/current/title-45/section-149.510",
            "https://www.law.cornell.edu/uscode/text/29/1144",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Evidence-to-Remittance Arbitration Pod",
        "subtitle": (
            "Turn eligible clinical evidence into disciplined offers, then turn "
            "determinations into reconciled incremental receipts."
        ),
        "audience": (
            "Clinical documentation specialists and billing founders building a "
            "small authorized provider-representation service."
        ),
        "research_basis": (
            "42 U.S.C. § 300gg-111(c)(5) identifies permitted considerations and "
            "prohibited payment benchmarks. Evidence assembly should connect "
            "acuity, complexity, and relevant contracting facts to each offer; "
            "collection operations should separately track determination dates, "
            "payment obligations, fee refunds, and actual remittances."
        ),
        "sources": [
            "https://www.law.cornell.edu/uscode/text/42/300gg-111",
            "https://www.ecfr.gov/current/title-45/section-149.510",
            "https://www.ecfr.gov/current/title-45/section-164.504",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
]


def build_volume_045_diagrams_data() -> list[dict]:
    specs = [
        (
            "diag-01-incremental-cash-workflow",
            "process_flow",
            "From Remittance Exception to Earned Contingency",
            "Five operating steps; provider recoveries never become operator revenue.",
            1,
            "operating_framework",
            (
                "Operate under provider authorization and HIPAA Business Associate "
                "Agreements where required by 45 CFR § 164.504(e). The initial "
                "payment is an actual remittance; QPA is a separate statutory "
                "benchmark and must not be substituted for the cash baseline. "
                "Apply current CMS instructions and controlling rules to each "
                "filing rather than hardcoding fee schedules or batching criteria."
            ),
            (
                "Separate eligibility, deadline preservation, evidence, collection, "
                "and revenue recognition. No award amount enters the earned-fee "
                "ledger before the relevant incremental cash is collected."
            ),
            [
                (
                    "Reconcile the baseline",
                    "835 plus bank match",
                    1.0,
                    (
                        "Ingest authorized 835 ERA records, CARC/RARC codes, claim "
                        "identifiers, initial allowed amounts, and payment dates. "
                        "Match payer cash to the claim and preserve the reported "
                        "QPA separately; denial codes alone do not establish an "
                        "underpayment or federal eligibility."
                    ),
                ),
                (
                    "Select the payment rail",
                    "Federal, state, or other",
                    2.0,
                    (
                        "Verify service setting, network status, coverage, plan "
                        "funding, applicable state law, and any All-Payer Model "
                        "Agreement. Route eligible federal disputes under "
                        "42 U.S.C. § 300gg-111 and 45 CFR § 149.510; segregate "
                        "state-process cases before incurring federal filing costs."
                    ),
                ),
                (
                    "Preserve the deadlines",
                    "30 business days + 4",
                    3.0,
                    (
                        "Track receipt of initial payment or denial, the separate "
                        "30-business-day period to start open negotiation, and "
                        "the 30-business-day negotiation period. If unresolved, "
                        "track the four-business-day IDR initiation window after "
                        "negotiation ends; initiation is distinct from entity "
                        "selection and later offer submission."
                    ),
                ),
                (
                    "Build the offer packet",
                    "Supported offer and evidence",
                    4.0,
                    (
                        "Use QPA, relevant clinical acuity, case complexity, and "
                        "permitted contracting evidence. Licensed FAIR Health "
                        "material requires field-level screening; do not submit "
                        "usual-and-customary charges, billed charges, or public "
                        "payer rates as prohibited benchmarks under "
                        "42 U.S.C. § 300gg-111(c)(5)(D)."
                    ),
                ),
                (
                    "Collect and allocate",
                    "Cash before contingency",
                    5.0,
                    (
                        "Reconcile additional payer receipts and confirmed entity "
                        "fee refunds. Fee base equals incremental cash above the "
                        "initial payer payment, less unrecovered CMS administrative "
                        "fees, entity fees, and agreed casework costs, floored at "
                        "zero. Multiply that base by the contracted share; keep "
                        "provider-owned cash out of operator revenue."
                    ),
                ),
            ],
        ),
        (
            "diag-02-nested-dispute-cash-cohort",
            "funnel",
            "A Favorable Determination Is Not Collected Cash",
            "One fixed referral cohort, five nested counts, one observation date.",
            6,
            "illustrative_model",
            (
                "Illustrative cohort counts, not observed performance or the "
                "canonical annual revenue model. Every stage is a subset of the "
                "preceding stage. Negotiated settlements leave this arbitration "
                "funnel and enter a separate collection ledger. Unpaid awards "
                "remain receivables or disputed items, not earned contingency "
                "revenue under this cash-conditioned model."
            ),
            (
                "The example has 420 favorable determinations but only 280 cases "
                "with incremental cash received: a 66.7% paid share of favorable "
                "cases and a 28.0% referral-to-cash conversion."
            ),
            [
                (
                    "Referred claims",
                    "1,000 source claims",
                    1000.0,
                    (
                        "Freeze a dated intake cohort with unique claim identifiers, "
                        "provider authority, payer remittance records, and bank "
                        "reconciliation links; count each dispute unit once."
                    ),
                ),
                (
                    "Federal-eligible claims",
                    "700 of 1,000; 70.0%",
                    700.0,
                    (
                        "Document federal eligibility and usable records for 700 "
                        "claims. Exclude the other 300 from this cohort's federal "
                        "filing path because routing or documentation requirements "
                        "were not satisfied."
                    ),
                ),
                (
                    "Timely initiated disputes",
                    "560 of 700; 80.0%",
                    560.0,
                    (
                        "Carry 560 unresolved, timely initiated disputes forward "
                        "after open negotiation. The remaining 140 include "
                        "settlements and operational exits; track their outcomes "
                        "separately rather than labeling them arbitration losses."
                    ),
                ),
                (
                    "Favorable determinations",
                    "420 of 560; 75.0%",
                    420.0,
                    (
                        "Record 420 favorable determinations by the observation "
                        "date. Split the other 140 among pending, adverse, and "
                        "dismissed cases in the case ledger; do not treat every "
                        "non-favorable observation as a final merits loss."
                    ),
                ),
                (
                    "Incremental cash received",
                    "280 of 420; 66.7%",
                    280.0,
                    (
                        "Match incremental receipts for 280 favorable cases to "
                        "bank activity. The other 140 favorable cases have no "
                        "matched incremental cash at this cutoff. Partial receipts "
                        "support fees only on their actual net collected amount."
                    ),
                ),
            ],
        ),
        (
            "diag-03-base-case-earned-fee-waterfall",
            "waterfall",
            "$505,000 Earned Fees to $217,150 Owner Profit",
            "Six bars reconcile the canonical Base-Case 43.0% net margin.",
            3,
            "illustrative_model",
            (
                "Canonical endpoints are $505,000 annual operator revenue and "
                "$217,150 owner profit. Cost splits and the supporting recovery "
                "pool are illustrative engineering assumptions. Example fee base: "
                "$2,200,000 incremental provider cash collected minus $80,000 "
                "unrecovered administrative/entity fees minus $100,000 provider-borne "
                "casework costs equals $2,020,000; a 25% retained share produces "
                "$505,000 earned operator revenue. Those two provider-borne "
                "deductions are outside the operator expense bars and must not "
                "be deducted twice. No baseline provider collections are included."
            ),
            (
                "$505,000 − $156,000 − $30,000 − $36,000 − $65,850 = $217,150. "
                "Owner profit divided by earned operator revenue equals 43.0%. "
                "The first and last bars are totals; the four middle bars are "
                "negative changes, not additional revenue."
            ),
            [
                (
                    "Earned operator revenue",
                    "$505,000 annual fee revenue",
                    505000.0,
                    (
                        "Recognize the operator's earned 25% share of the "
                        "$2,020,000 net incremental collection pool. Where the "
                        "operator is an agent under ASC 606, exclude provider "
                        "proceeds and pass-through recoveries from recognized "
                        "revenue; document the principal-versus-agent assessment."
                    ),
                ),
                (
                    "Variable delivery labor",
                    "−$156,000 annual expense",
                    -156000.0,
                    (
                        "Illustrative operator-funded contractor delivery labor "
                        "and specialist support, separate from provider-borne "
                        "casework already deducted in the fee-base calculation. "
                        "Owner distributions are not a second labor deduction."
                    ),
                ),
                (
                    "Systems and protected storage",
                    "−$30,000 annual expense",
                    -30000.0,
                    (
                        "Budget $2,500 monthly for contracted secure infrastructure, "
                        "835 ingestion, access logging, deadline automation, and "
                        "licensed evidence tools. Verify business-associate terms "
                        "before any service receives protected health information."
                    ),
                ),
                (
                    "Core operating overhead",
                    "−$36,000 annual expense",
                    -36000.0,
                    (
                        "Budget $3,000 monthly for insurance, accounting, workspace, "
                        "and routine administration. Combined with systems, "
                        "$5,500 monthly fixed overhead sits within the supplied "
                        "$1,800–$10,500 core operating budget range."
                    ),
                ),
                (
                    "Acquisition and variable support",
                    "−$65,850 annual expense",
                    -65850.0,
                    (
                        "Allocate illustrative non-fixed acquisition, provider "
                        "onboarding, and transaction support costs. Total operator "
                        "expenses are $287,850 annually; the monthly core budget "
                        "range does not represent all-in expenses including "
                        "variable delivery and acquisition."
                    ),
                ),
                (
                    "Owner net profit",
                    "$217,150 at 43.0%",
                    217150.0,
                    (
                        "Canonical Base-Case annual residual for the 1 FT + 2 C "
                        "pod. Preserve the scorecard's owner-profit definition; "
                        "do not silently recast this figure as a provider recovery "
                        "amount, salary figure, or award-value margin."
                    ),
                ),
            ],
        ),
        (
            "diag-04-specialty-collected-yield",
            "horizontal_bars",
            "Compare Cash Yield, Not Headline Awards",
            "Illustrative earned fees per referred claim on eligible federal rails.",
            2,
            "illustrative_model",
            (
                "Each bar uses an independent ten-referral cohort, including "
                "referrals producing zero cash, and a hypothetical 25% retained "
                "share. Net recovery pools already exclude initial payer "
                "collections, unrecovered administrative/entity fees, and agreed "
                "casework costs. These are comparison assumptions, not specialty "
                "benchmarks, expected returns, or a weighted bridge to annual "
                "scorecard revenue. Operator overhead remains to be deducted."
            ),
            (
                "Normalize collections to all referred claims so rejected claims, "
                "losses, and unpaid awards reduce yield. Specialty labels do not "
                "establish jurisdiction or eligibility."
            ),
            [
                (
                    "Emergency physician",
                    "$150 earned per referral",
                    150.0,
                    (
                        "A $6,000 net incremental cash pool across ten referrals "
                        "produces $1,500 operator fees at 25%. Screen emergency "
                        "service circumstances, payer coverage, and the applicable "
                        "state or federal payment route before filing."
                    ),
                ),
                (
                    "Facility anesthesia",
                    "$200 earned per referral",
                    200.0,
                    (
                        "An $8,000 net incremental cash pool across ten referrals "
                        "produces $2,000 operator fees at 25%. Verify the "
                        "participating-facility context and applicable ancillary "
                        "service protections rather than relying on the specialty "
                        "code alone."
                    ),
                ),
                (
                    "Facility radiology",
                    "$100 earned per referral",
                    100.0,
                    (
                        "A $4,000 net incremental cash pool across ten referrals "
                        "produces $1,000 operator fees at 25%. Separate professional "
                        "and technical components, validate service identifiers, "
                        "and prevent duplicate recovery across component claims."
                    ),
                ),
                (
                    "Facility pathology",
                    "$80 earned per referral",
                    80.0,
                    (
                        "A $3,200 net incremental cash pool across ten referrals "
                        "produces $800 operator fees at 25%. Validate covered "
                        "facility-linked services and permitted batching criteria; "
                        "similar specialty labels do not make every claim batchable."
                    ),
                ),
                (
                    "Covered air ambulance",
                    "$600 earned per referral",
                    600.0,
                    (
                        "A $24,000 net incremental cash pool across ten referrals "
                        "produces $6,000 operator fees at 25%. Apply the distinct "
                        "air-ambulance requirements in 45 CFR § 149.520 and "
                        "42 U.S.C. § 300gg-112; exclude ground ambulance claims "
                        "from this federal comparison."
                    ),
                ),
            ],
        ),
        (
            "diag-05-statutory-risk-decision-tree",
            "decision_tree",
            "Four Checks Before Federal Filing",
            "Explicit stop, reroute, and proceed outcomes preserve fees and deadlines.",
            5,
            "operating_framework",
            (
                "Evaluate the checks in sequence for each proposed dispute or "
                "batch. Statutory anchors include 42 U.S.C. § 300gg-111, "
                "45 CFR §§ 149.30 and 149.510, and HIPAA business-associate "
                "requirements in 45 CFR § 164.504(e). Verify current CMS "
                "operational guidance and applicable court orders when configuring "
                "deadline, fee, and batching rules."
            ),
            (
                "A missing fact is a work item, not permission to file. Every "
                "negative branch must identify the responsible person, next action, "
                "and remaining deadline."
            ),
            [
                (
                    "Authority and protected records",
                    "Complete → check two",
                    1.0,
                    (
                        "Yes: retain provider representation authority, required "
                        "BAA terms, access controls, and relevant records. No: stop "
                        "protected-data ingestion and filing until authority and "
                        "handling arrangements are established; use de-identified "
                        "samples for system testing."
                    ),
                ),
                (
                    "Federal payment jurisdiction",
                    "Eligible → check three",
                    2.0,
                    (
                        "Yes: document covered service circumstances and why "
                        "federal IDR applies. No: route to the applicable state "
                        "process, contractual appeal, or other supported channel. "
                        "Do not equate self-funded ERISA status with automatic "
                        "eligibility or fully insured status with automatic exclusion."
                    ),
                ),
                (
                    "Timing and batch validity",
                    "Valid → check four",
                    3.0,
                    (
                        "Yes: retain negotiation notices, business-day calculations, "
                        "timely initiation evidence, and current batch criteria. "
                        "No: remove incompatible claims or stop the filing. Apply "
                        "the 90-calendar-day same-party, same-or-similar-item "
                        "cooling-off restriction and its applicable post-period "
                        "initiation window; never reset clocks through relabeling."
                    ),
                ),
                (
                    "Evidence and collection economics",
                    "Positive → authorized filing",
                    4.0,
                    (
                        "Proceed only with a supportable offer and a positive "
                        "risk-adjusted net collection estimate. Budget CMS "
                        "administrative fees as non-refundable and losing or "
                        "ineligible cases as unrecovered entity-fee exposure. "
                        "Credit prevailing-party entity refunds only when confirmed; "
                        "apply dismissal-specific rules rather than presuming a "
                        "refund. Otherwise renegotiate, correct, or decline."
                    ),
                ),
            ],
        ),
        (
            "diag-06-three-to-five-person-pod",
            "org_architecture",
            "Three People Launch; Five People Scale",
            "Clear ownership separates filing execution from cash reconciliation.",
            11,
            "operating_framework",
            (
                "Canonical Conservative: $110,000 revenue × 30% = $33,000 owner "
                "profit with 1 FT + 2 C. Canonical Base-Case: $505,000 × 43.0% = "
                "$217,150 with the same three-person structure. Canonical Scaled: "
                "$900,000 × 56% = $504,000 with 2 FT + 3 C. Revenue means earned "
                "operator contingency, not provider collections. Seats four and "
                "five are additions only in the Scaled configuration."
            ),
            (
                "FT means full-time seat; C means contractor seat, not assumed "
                "full-time capacity. Assign a named backup for every deadline "
                "and keep evidence decisions separate from receipt confirmation."
            ),
            [
                (
                    "Owner and recovery lead",
                    "Launch: 1 FT",
                    1.0,
                    (
                        "Own provider contracts, jurisdiction exceptions, offer "
                        "authority, fee-base definitions, and operating economics. "
                        "Maintain the exception queue and engage appropriately "
                        "qualified specialists when a matter exceeds the team's "
                        "authorized scope."
                    ),
                ),
                (
                    "Claims and deadline analyst",
                    "Launch: 1 C",
                    1.0,
                    (
                        "Parse 835 records, verify initial remittances, maintain "
                        "business-day calendars, preserve negotiation delivery "
                        "evidence, and prepare eligible batches. Escalate missing "
                        "plan documentation before filing costs are committed."
                    ),
                ),
                (
                    "Clinical evidence specialist",
                    "Launch: 1 C",
                    1.0,
                    (
                        "Connect chart-supported acuity and complexity to permitted "
                        "offer factors, redact unnecessary information, and inspect "
                        "licensed data extracts for prohibited benchmarks. The "
                        "owner checks submission authority and final packet quality."
                    ),
                ),
                (
                    "Operations and collections lead",
                    "Scale addition: 1 FT",
                    1.0,
                    (
                        "Take ownership of capacity planning, payer payment "
                        "follow-up, determination-date tracking, and cash "
                        "reconciliation. Monitor the applicable 30-calendar-day "
                        "payment obligation after determination separately from "
                        "actual collection performance."
                    ),
                ),
                (
                    "Remittance quality specialist",
                    "Scale addition: 1 C",
                    1.0,
                    (
                        "Independently match bank receipts, corrected remittances, "
                        "entity refunds, and provider allocations. Sample earned "
                        "contingency calculations for duplicate collections, "
                        "baseline-payment leakage, and double-counted case costs."
                    ),
                ),
            ],
        ),
        (
            "diag-07-startup-capital-allocation",
            "stacked_comparison",
            "Allocate $25,000 Without Confusing Reserves with Expense",
            "Four capital buckets within the $10,000–$45,000 startup range.",
            4,
            "illustrative_model",
            (
                "Illustrative startup allocation totals $25,000, within the "
                "canonical $10,000–$45,000 range. Shares are 26%, 22%, 32%, and "
                "20%. Capital allocations are not automatically current-period "
                "expenses. First-deal timing is 1–4 months; first cash collection "
                "can occur later, so maintain a dated liquidity forecast."
            ),
            (
                "$6,500 + $5,500 + $8,000 + $5,000 = $25,000. Release filing "
                "liquidity only for screened cases with documented fee ownership "
                "and reimbursement treatment."
            ),
            [
                (
                    "Secure intake infrastructure",
                    "$6,500; 26% of capital",
                    6500.0,
                    (
                        "Fund encrypted storage setup, role-based access, audit "
                        "logging, 835 parser validation, and backup restoration "
                        "testing. Use synthetic or de-identified fixtures until "
                        "contracts and required business-associate arrangements "
                        "cover the production data path."
                    ),
                ),
                (
                    "Contracts and operating setup",
                    "$5,500; 22% of capital",
                    5500.0,
                    (
                        "Fund provider engagement terms, BAA preparation, "
                        "representation scope, insurance deposits, and accounting "
                        "design. Specify the incremental-cash baseline, cost "
                        "deductions, refund allocation, retained share, and handling "
                        "of provider-owned money."
                    ),
                ),
                (
                    "Case-fee liquidity reserve",
                    "$8,000; 32% of capital",
                    8000.0,
                    (
                        "Reserve cash for authorized administrative and entity "
                        "fee outlays where the provider contract assigns funding "
                        "responsibility. Track advances, reimbursements, losses, "
                        "and actual refunds separately; a refundable deposit "
                        "is not earned operator revenue."
                    ),
                ),
                (
                    "Acquisition and runway reserve",
                    "$5,000; 20% of capital",
                    5000.0,
                    (
                        "Fund targeted provider outreach, pilot onboarding, and "
                        "a limited operating buffer. At the illustrative $5,500 "
                        "monthly fixed overhead, this bucket alone covers less "
                        "than one month; use staged spending, provider-funded "
                        "fees, or additional capital before expanding."
                    ),
                ),
            ],
        ),
        (
            "diag-08-thirty-day-launch-roadmap",
            "timeline_roadmap",
            "Thirty Days to a Controlled Recovery Pipeline",
            "Build a working operation without compressing statutory calendars.",
            12,
            "operating_framework",
            (
                "Sprint days are calendar-day project milestones; statutory "
                "business-day and calendar-day clocks remain separate. The "
                "canonical first-deal horizon is 1–4 months, and this sprint "
                "does not assume a completed award, payer deposit, or earned "
                "contingency within 30 days."
            ),
            (
                "End the month with authorized intake, defensible routing, tested "
                "timers, and claim-level economics. Advance individual cases "
                "only when their actual statutory and operational conditions hold."
            ),
            [
                (
                    "Days 1-7",
                    "Authority and data foundation",
                    7.0,
                    (
                        "Execute provider engagement and required BAA documents; "
                        "define the incremental-cash fee formula and fee ownership. "
                        "Configure least-privilege access and reconcile a sample "
                        "835 to bank receipts. Deliver an intake checklist and "
                        "a tested initial-payment ledger."
                    ),
                ),
                (
                    "Days 8-14",
                    "Routing and clock validation",
                    14.0,
                    (
                        "Classify a pilot cohort using plan documents, service "
                        "facts, and state-law applicability. Test holiday handling, "
                        "30-business-day negotiation calculations, four-business-day "
                        "initiation windows, and cooling-off restrictions. Deliver "
                        "a dated routing record for every pilot claim."
                    ),
                ),
                (
                    "Days 15-21",
                    "Evidence and negotiation execution",
                    21.0,
                    (
                        "Start eligible open negotiations within their actual "
                        "deadlines, retain delivery evidence, and prepare supported "
                        "offers. Test packet generation with clinical source links "
                        "and prohibited-benchmark checks. Older eligible matters "
                        "may advance only if their own clocks permit."
                    ),
                ),
                (
                    "Days 22-30",
                    "Cash controls and capacity decision",
                    30.0,
                    (
                        "Reconcile pilot status, fee exposure, available liquidity, "
                        "and contractor capacity. Test contingency calculations "
                        "against partial collections, losses, and confirmed "
                        "refunds. Deliver a cash forecast and next-month case "
                        "schedule; record pending negotiations without fabricating "
                        "awards or collections."
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
