from __future__ import annotations

VOLUME_049_SUBTITLE = (
    "The Complete Playbook for Regulated Prediction-Market Terminals and Licensed "
    "iGaming Affiliates: $75,000-$650,000 USD in Annual Operator Revenue, "
    "Starting with a 1 FT + 2 C Pod of 3 People"
)

VOLUME_049_POSITIONING_ALTERNATIVES = [
    {
        "title": "The Non-Custodial Event-Contract Intelligence Terminal",
        "subtitle": (
            "Sell probability normalization, timestamped market comparisons, and "
            "subscription analytics without accepting funds or executing customer orders."
        ),
        "audience": (
            "A technical founder and two contractors building paid analytics for "
            "eligible users of regulated designated contract markets."
        ),
        "research_basis": (
            "7 U.S.C. 1a defines commodity trading advisers, introducing brokers, "
            "and futures commission merchants; 7 U.S.C. 6d addresses intermediary "
            "registration. The publisher exclusion has conditions, including the "
            "incidental-business limitation, and non-custody alone does not settle "
            "registration status. Evaluate personalization, solicitation, compensation, "
            "and order handling before enabling any referral or execution feature. "
            "17 CFR 40.11 also matters when assessing event-contract availability."
        ),
        "sources": [
            "https://www.law.cornell.edu/uscode/text/7/1a",
            "https://www.law.cornell.edu/uscode/text/7/6d",
            "https://www.ecfr.gov/current/title-17/chapter-I/part-40/section-40.11",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The State-Licensed Affiliate Contribution Desk",
        "subtitle": (
            "Turn eligible adult comparison traffic into operator-confirmed CPA "
            "and settled NGR commissions, with deductions visible before acquisition spend."
        ),
        "audience": (
            "An acquisition operator with engineering and editorial contractors "
            "serving licensed sportsbook and iGaming partners in specifically cleared states."
        ),
        "research_basis": (
            "State gaming agencies administer jurisdiction-specific affiliate and "
            "vendor requirements; one state's registration does not authorize another. "
            "Use NJ DGE, PA PGCB, and MI MGCB requirements to build separate partner, "
            "registration, advertising, and reporting records. NJ casino service "
            "industry requirements include N.J.S.A. 5:12-92. Apply material-connection "
            "disclosures under 16 CFR 255.5 alongside age, location, and responsible-gaming controls."
        ),
        "sources": [
            "https://www.nj.gov/oag/ge/",
            "https://gamingcontrolboard.pa.gov/",
            "https://www.michigan.gov/mgcb",
            "https://www.ecfr.gov/current/title-16/chapter-I/subchapter-B/part-255/section-255.5",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "Two Revenue Books, One Small Operating Pod",
        "subtitle": (
            "Combine recurring analytics subscriptions with separately authorized "
            "gaming commissions while keeping contracts, attribution, and deductions distinct."
        ),
        "audience": (
            "A founder seeking the canonical $362,500 annual operator-revenue case "
            "with one full-time seat and two contractor seats."
        ),
        "research_basis": (
            "CFTC intermediary definitions and state gaming requirements govern "
            "different activities. Separate product permissions and revenue ledgers "
            "prevent a software subscription from being treated as authorization for "
            "gaming promotion or compensated futures solicitation. Source-informed "
            "operating controls include activity classification, state-specific vendor "
            "records, disclosed commercial relationships, and settlement-backed commission recognition."
        ),
        "sources": [
            "https://www.law.cornell.edu/uscode/text/7/1a",
            "https://www.law.cornell.edu/uscode/text/7/6d",
            "https://www.nj.gov/oag/ge/",
            "https://gamingcontrolboard.pa.gov/",
            "https://www.michigan.gov/mgcb",
            "https://www.ecfr.gov/current/title-16/chapter-I/subchapter-B/part-255/section-255.5",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
]


def build_volume_049_diagrams_data() -> list[dict]:
    specs = [
        (
            "diag-01-two-ledger-operating-workflow",
            "process_flow",
            "One Pod, Two Separately Authorized Revenue Lanes",
            "Keep regulated-market analytics distinct from state-licensed gaming acquisition.",
            1,
            "operating_framework",
            (
                "The terminal is non-custodial and does not pool capital, accept "
                "customer funds, or submit customer orders. Analytics publishing "
                "does not itself establish an exemption from CTA, IB, or FCM "
                "requirements. Partner access and compensation require documented "
                "permission for the actual activity and jurisdiction."
            ),
            (
                "Build the permission map before the feed adapter; reconcile "
                "subscriptions and gaming commissions through different revenue accounts."
            ),
            [
                (
                    "Classify each activity",
                    "Two distinct permission records",
                    1.0,
                    (
                        "Inventory subscription analytics, personalization, solicitation, "
                        "builder compensation, and gaming links. Apply 7 U.S.C. 1a "
                        "and 6d to the derivatives lane and the applicable state "
                        "vendor rules to the gaming lane; non-custody is necessary "
                        "but does not resolve every registration question."
                    ),
                ),
                (
                    "Normalize permitted feeds",
                    "Timestamp every market observation",
                    2.0,
                    (
                        "Use documented Kalshi, ForecastEx-access, and licensed "
                        "sportsbook interfaces only where available and permitted. "
                        "Record source time, receipt time, fees, contract wording, "
                        "settlement terms, and market identifiers. Measure sub-second "
                        "delivery as a service target rather than assuming every "
                        "source provides a WebSocket feed."
                    ),
                ),
                (
                    "Publish bounded analytics",
                    "Subscriptions without order handling",
                    3.0,
                    (
                        "Normalize implied probabilities and display fee-aware comparisons "
                        "with stale-feed cutoffs. Label positive expected value as "
                        "model-dependent, not riskless arbitrage; incompatible settlement "
                        "terms and execution slippage can reverse the apparent edge. "
                        "Do not add personalized recommendations without reassessing activity classification."
                    ),
                ),
                (
                    "Attribute eligible referrals",
                    "Separate state and partner identifiers",
                    4.0,
                    (
                        "Apply the product's 21+ policy, jurisdiction-specific geofencing, "
                        "partner allowlists, material-connection disclosures, and current "
                        "responsible-gaming helpline disclosures. Sign server-to-server "
                        "events, deduplicate event identifiers, and rely on partner "
                        "confirmation for qualifying deposits rather than browser clicks."
                    ),
                ),
                (
                    "Reconcile earned revenue",
                    "Separate subscriptions, rebates, CPA, and NGR",
                    5.0,
                    (
                        "Match SaaS invoices, expressly permitted builder statements, "
                        "accepted CPA events, and settled NGR reports to bank receipts "
                        "and receivables. Never book trading volume, gambling handle, "
                        "player deposits, or user balances as operator revenue. Block "
                        "unlicensed offshore, unlawful crypto, and unlawful sweepstakes destinations."
                    ),
                ),
            ],
        ),
        (
            "diag-02-eligible-affiliate-cohort",
            "funnel",
            "Annual CPA Cohort: Eligible Traffic to Payable Depositor",
            "Five nested counts describe the affiliate lane only.",
            6,
            "illustrative_model",
            (
                "Illustrative annual unique-visitor cohort underlying the Base-Case "
                "$90,000 CPA revenue allocation. Counts are nested, deduplicated, "
                "and measured within contract-specific attribution windows. Terminal "
                "subscribers and NGR-only partners are outside this funnel. Entry "
                "screening is not a substitute for the operator's age and identity checks."
            ),
            (
                "50,000 eligible visitors produce 100 payable FTD events at $900 "
                "each; a 120-event full-budget planning baseline is reduced by "
                "20 events for seasonal CPA availability before revenue is booked."
            ),
            [
                (
                    "Eligible adult visitor cohort",
                    "50,000 screened unique visitors",
                    50000.0,
                    (
                        "Start with unique visitors passing first-party 21+ screening "
                        "and permitted-location checks. Preserve jurisdiction, campaign, "
                        "and partner eligibility evidence while minimizing personal "
                        "data. Exclude blocked locations and ineligible destinations "
                        "before commercial links become available."
                    ),
                ),
                (
                    "Qualified comparison cohort",
                    "15,000 visitors; 30% of entry cohort",
                    15000.0,
                    (
                        "Count visitors who use a comparison page for an eligible "
                        "licensed partner and see current commercial terms and the "
                        "affiliate disclosure. Remove automated traffic and duplicate "
                        "identities under the documented attribution policy."
                    ),
                ),
                (
                    "Attributed click cohort",
                    "3,000 visitors; 20% of comparison cohort",
                    3000.0,
                    (
                        "Create a signed click identifier and store the state, "
                        "campaign, creative version, and partner offer version. "
                        "A redirect is evidence of a click, not evidence of "
                        "a deposit, account approval, or payable commission."
                    ),
                ),
                (
                    "Partner-confirmed FTD cohort",
                    "300 depositors; 10% of click cohort",
                    300.0,
                    (
                        "Accept first-time-depositor events only from authenticated "
                        "partner reporting after operator checks. Match depositors "
                        "to the originating cohort; deposits still may fail minimum "
                        "amount, attribution-window, campaign-cap, or commission eligibility terms."
                    ),
                ),
                (
                    "Contract-payable CPA cohort",
                    "100 depositors; 33.33% of FTD cohort",
                    100.0,
                    (
                        "Reconcile all 300 events into 100 payable and 200 "
                        "nonpayable outcomes with explicit partner reason codes. "
                        "The 100 accepted events generate $90,000 at $900 each. "
                        "Seasonality is already reflected in this count; do not "
                        "subtract the $18,000 planning reduction again as operating expense."
                    ),
                ),
            ],
        ),
        (
            "diag-03-base-case-profit-bridge",
            "waterfall",
            "Base-Case Operator Revenue to Owner Profit",
            "$362,500 recognized operator revenue less $224,750 operating costs.",
            3,
            "illustrative_model",
            (
                "USD annually. Opening and closing bars are totals; the four "
                "intermediate bars are signed cost changes. Canonical gross revenue "
                "means operator revenue, not customer transaction value. Revenue "
                "includes $210,000 SaaS, $12,500 permitted builder compensation, "
                "$90,000 CPA, and $50,000 settled NGR commissions. The illustrative "
                "cost allocation reconciles exactly to Formula v2.0."
            ),
            (
                "$362,500 - $85,000 - $90,000 - $24,000 - $25,750 = $137,750; "
                "$137,750 / $362,500 = 38.0%. Affiliate contractual deductions "
                "are already reflected in recognized commission revenue."
            ),
            [
                (
                    "Recognized operator revenue",
                    "$362,500 annual opening total",
                    362500.0,
                    (
                        "Book subscriptions and earned software compensation separately "
                        "from affiliate commissions. The $50,000 NGR allocation equals "
                        "$80,000 preliminary contractual commission less $18,000 allocated "
                        "admin and bonus deductions and $12,000 negative carryover. "
                        "Apply ASC 606 principal-versus-agent analysis; no additional "
                        "retained-share multiplier is supplied for this scorecard."
                    ),
                ),
                (
                    "Acquisition and distribution",
                    "-$85,000 annual operating cost",
                    -85000.0,
                    (
                        "Allocate $45,000 to SaaS acquisition, $30,000 to CPA "
                        "acquisition, and $10,000 to NGR acquisition. The CPA cohort "
                        "therefore carries $300 acquisition cost per payable depositor. "
                        "Measure channel contribution after partner adjustments, not "
                        "against headline commission offers."
                    ),
                ),
                (
                    "Contractor delivery capacity",
                    "-$90,000 annual operating cost",
                    -90000.0,
                    (
                        "Budget $54,000 for the engineering contractor and $36,000 "
                        "for the acquisition and editorial contractor. The founder "
                        "is the one full-time seat and receives the residual "
                        "owner-profit measure; no separate founder salary is assumed "
                        "in this illustrative allocation."
                    ),
                ),
                (
                    "Platform and billing infrastructure",
                    "-$24,000 annual operating cost",
                    -24000.0,
                    (
                        "Fund permitted feed access, managed PostgreSQL, cloud delivery, "
                        "monitoring, subscription billing fees, and attribution infrastructure. "
                        "Track stale-feed incidents and webhook replay failures as "
                        "service costs; user trading fees belong in comparison "
                        "analytics rather than operator revenue."
                    ),
                ),
                (
                    "Professional and operating overhead",
                    "-$25,750 annual operating cost",
                    -25750.0,
                    (
                        "Allocate $12,000 to activity classification and state vendor "
                        "work, $6,000 to accounting and insurance, $4,750 to support "
                        "and administrative tools, and $3,000 to refunds and collection "
                        "losses. Refunds are charged here only when not already "
                        "netted from opening revenue."
                    ),
                ),
                (
                    "Owner profit",
                    "$137,750 annual closing total; 38.0%",
                    137750.0,
                    (
                        "Operating costs total $224,750, leaving the canonical "
                        "Base-Case owner profit of $137,750. Fixed delivery, platform, "
                        "and overhead costs average $11,645.83 monthly before "
                        "acquisition; this exceeds the metadata's $10,000 monthly "
                        "upper bound, so that range cannot represent all-in Base-Case costs."
                    ),
                ),
            ],
        ),
        (
            "diag-04-five-monetization-lane-yields",
            "horizontal_bars",
            "Five Revenue Lanes, One Comparable Annual Dollar Unit",
            "Illustrative lane allocations sum to the canonical $362,500 Base Case.",
            2,
            "illustrative_model",
            (
                "Every bar measures annual recognized operator revenue in USD, "
                "not margin, player deposits, or return on wagering capital. "
                "The first two bars are SaaS subscriptions; the third is a "
                "separately assessed software-compensation lane; the final two "
                "are distinct affiliate cohorts with distinct settlement records."
            ),
            (
                "$150,000 + $60,000 + $12,500 + $90,000 + $50,000 = $362,500. "
                "These allocations are an illustrative bridge, not externally "
                "verified partner rates or current program availability."
            ),
            [
                (
                    "Core terminal subscriptions",
                    "$150,000 annual SaaS revenue",
                    150000.0,
                    (
                        "250 average paying subscribers at $50 monthly generate "
                        "$150,000 annually. Average subscribers already incorporate "
                        "churn and replacements. Deliver market comparison, timestamps, "
                        "and fee normalization without account custody or customer "
                        "order submission."
                    ),
                ),
                (
                    "Professional analytics subscriptions",
                    "$60,000 annual SaaS revenue",
                    60000.0,
                    (
                        "50 additional average paying subscribers at $100 monthly "
                        "generate $60,000 annually. Keep these subscribers separate "
                        "from the core tier. Price export capacity, saved analytic "
                        "views, and alert delivery rather than promising trading "
                        "profits or personalized investment outcomes."
                    ),
                ),
                (
                    "Permitted builder compensation",
                    "$12,500 annual software revenue",
                    12500.0,
                    (
                        "Assume 25 contract-defined software-service milestones earning "
                        "$500 each under an expressly permitted arrangement. This "
                        "is a modeling unit, not a claim that any named venue "
                        "offers this program. Do not recognize revenue until terms, "
                        "activity classification, and acceptance evidence support it."
                    ),
                ),
                (
                    "Seasonally adjusted CPA commissions",
                    "$90,000 annual affiliate revenue",
                    90000.0,
                    (
                        "120 potential payable depositors at $900 imply $108,000 "
                        "before a modeled 20-event post-NFL budget reduction. The "
                        "remaining 100 produce $90,000. Subtract the separately budgeted "
                        "$30,000 CPA acquisition cost for $60,000 contribution before "
                        "shared delivery and overhead."
                    ),
                ),
                (
                    "Settled NGR commissions",
                    "$50,000 annual affiliate revenue",
                    50000.0,
                    (
                        "An illustrative $80,000 preliminary commission entitlement, "
                        "not casino-wide gaming revenue, falls to $50,000 after "
                        "$18,000 admin and bonus allocations and $12,000 carryover. "
                        "Subtract $10,000 allocated acquisition cost for $40,000 "
                        "contribution before shared costs; retain partner-level carryover ledgers."
                    ),
                ),
            ],
        ),
        (
            "diag-05-four-preflight-decisions",
            "decision_tree",
            "Four Independent Checks Before Commercial Activation",
            "An unresolved branch disables the affected activity, not the evidence record.",
            5,
            "operating_framework",
            (
                "These are sequential binary checks with pass and stop branches "
                "described in each detail. The US-state affiliate plan does not "
                "extend to Ontario; provincial requirements and partner permissions "
                "need their own assessment. The product adopts 21+ screening "
                "without treating it as a universal derivatives-market age statute."
            ),
            (
                "Non-custody, registration status, eligible destinations, and "
                "settlement economics must each be established independently."
            ),
            [
                (
                    "Activity classification",
                    "Pass to jurisdiction check; otherwise stop affected feature",
                    1.0,
                    (
                        "Under 7 U.S.C. 1a and 6d, assess CTA, IB, and FCM "
                        "status using actual solicitation, compensation, personalization, "
                        "and order-handling behavior. Pass only with a documented "
                        "basis for the permitted scope; otherwise disable the "
                        "feature until required registration or a supported exclusion "
                        "is established. Never accept funds or pool user capital."
                    ),
                ),
                (
                    "Jurisdiction and partner authority",
                    "Pass to audience check; otherwise suppress destination",
                    2.0,
                    (
                        "Verify DCM status and applicable event-contract availability, "
                        "including 17 CFR 40.11. Separately verify the gaming "
                        "operator's state license and required affiliate or vendor "
                        "status with NJ DGE, PA PGCB, MI MGCB, or WV Lottery. "
                        "N.J.S.A. 5:12-92 addresses casino service industry requirements; "
                        "one registration does not create nationwide permission."
                    ),
                ),
                (
                    "Audience and advertising controls",
                    "Pass to economics check; otherwise block referral",
                    3.0,
                    (
                        "Require the product's 21+ screen, eligible geography, "
                        "current offer terms, responsible-gaming helpline disclosures, "
                        "and material-connection disclosure under 16 CFR 255.5. "
                        "Treat uncertain or conflicting location signals as blocked "
                        "until resolved. Do not bypass partner identity, self-exclusion, "
                        "age, or location controls."
                    ),
                ),
                (
                    "Contract and loss exposure",
                    "Activate supported lane; otherwise hold acquisition spend",
                    4.0,
                    (
                        "Read CPA acceptance windows, seasonal caps, NGR deduction "
                        "definitions, negative carryover, payment timing, and clawback "
                        "rights. Require positive modeled contribution after CAC "
                        "and documented adjustments; reconcile authenticated settlement "
                        "events before scaling. Never redirect rejected users to "
                        "unlicensed offshore or unlawful sweepstakes alternatives."
                    ),
                ),
            ],
        ),
        (
            "diag-06-base-and-scaled-pod",
            "org_architecture",
            "Three Base Seats, Two Explicit Scale Additions",
            "Base and Conservative use 1 FT + 2 C; Scaled uses 2 FT + 3 C.",
            11,
            "operating_framework",
            (
                "Each numeric value represents one person. The first three seats "
                "form the Base-Case pod; the final two exist only in the Scaled "
                "scenario. External professional engagements are purchased services, "
                "not additional dedicated operating seats in the canonical team count."
            ),
            (
                "Conservative: $75,000 revenue x 26% = $19,500 owner profit. "
                "Base: $362,500 x 38.0% = $137,750. "
                "Scaled: $650,000 x 50% = $325,000. "
                "The $650,000 scenario requires five people, not the three-person pod."
            ),
            [
                (
                    "Founder and commercial owner",
                    "Base seat 1; one full-time operator",
                    1.0,
                    (
                        "Own partner contracts, state-specific permission records, "
                        "pricing, revenue recognition decisions, and the monthly "
                        "contribution statement. Maintain separate SaaS and affiliate "
                        "ledgers and approve acquisition budgets using settled "
                        "cohorts rather than headline click conversion."
                    ),
                ),
                (
                    "Integration and reliability contractor",
                    "Base seat 2; one engineering contractor",
                    1.0,
                    (
                        "Own feed adapters, market normalization, stale-data controls, "
                        "signed server-to-server attribution, and deployment recovery. "
                        "Use GitHub Actions for tests and PostgreSQL for replay-safe "
                        "event identifiers. Never place customer credentials or "
                        "user funds inside the terminal's operating scope."
                    ),
                ),
                (
                    "Acquisition and editorial contractor",
                    "Base seat 3; one distribution contractor",
                    1.0,
                    (
                        "Own eligible-state content, offer freshness, commercial "
                        "disclosures, campaign cohorts, and seasonal budget pacing. "
                        "Reconcile failed CPA events with partner reason codes and "
                        "maintain a correction queue for expired promotions and "
                        "mismatched settlement terms."
                    ),
                ),
                (
                    "Product and reliability employee",
                    "Scaled seat 4; add one full-time operator",
                    1.0,
                    (
                        "Add this seat only in the five-person Scaled scenario. "
                        "Own release quality, subscription retention, incident response, "
                        "and feed service objectives while the existing engineering "
                        "contractor handles integration depth. Rebuild the cost plan "
                        "within the Scaled $325,000 operating-cost envelope."
                    ),
                ),
                (
                    "Settlement and support contractor",
                    "Scaled seat 5; add one operations contractor",
                    1.0,
                    (
                        "Add this seat only in the Scaled scenario. Own commission "
                        "statement imports, carryover balances, support triage, "
                        "responsible-gaming referral handling, and partner discrepancy "
                        "tickets. Keep discretionary promotional access separate "
                        "from accounting adjustment permissions."
                    ),
                ),
            ],
        ),
        (
            "diag-07-startup-capital-buckets",
            "stacked_comparison",
            "A $24,000 Base Startup Allocation",
            "Four buckets reconcile to $8,000 lean, $24,000 base, and $45,000 expanded.",
            4,
            "illustrative_model",
            (
                "Numeric values encode the $24,000 base startup allocation in "
                "USD. Lean and expanded allocations appear in each stage detail "
                "and sum independently to the canonical range endpoints. Cash "
                "reserves are unspent liquidity, not immediate operating expense; "
                "startup outlays are not added again to the annual profit bridge."
            ),
            (
                "Base: $6,000 + $5,000 + $7,000 + $6,000 = $24,000. "
                "Lean: $2,000 + $2,000 + $2,500 + $1,500 = $8,000. "
                "Expanded: $12,000 + $10,000 + $14,000 + $9,000 = $45,000."
            ),
            [
                (
                    "Activity and vendor setup",
                    "$6,000 base; 25.00% of startup cash",
                    6000.0,
                    (
                        "Lean $2,000; base $6,000; expanded $12,000. Purchase "
                        "activity-classification work, partner-contract analysis, and "
                        "required vendor application preparation. The lean version "
                        "must narrow its permitted launch scope if actual professional "
                        "fees or registration costs exceed this allocation."
                    ),
                ),
                (
                    "Terminal and attribution build",
                    "$5,000 base; 20.83% of startup cash",
                    5000.0,
                    (
                        "Lean $2,000; base $5,000; expanded $10,000. Fund initial "
                        "feed adapters, PostgreSQL event storage, signed webhook "
                        "verification, subscription billing integration, and stale-feed "
                        "tests. Start with a small permitted source set rather "
                        "than assuming universal exchange or sportsbook access."
                    ),
                ),
                (
                    "Content and acquisition experiments",
                    "$7,000 base; 29.17% of startup cash",
                    7000.0,
                    (
                        "Lean $2,500; base $7,000; expanded $14,000. Build "
                        "jurisdiction-specific comparison content and run bounded "
                        "subscription and affiliate acquisition tests. Keep campaign "
                        "budgets separate by lane, and stop spend when accepted-event "
                        "economics fail the documented contribution threshold."
                    ),
                ),
                (
                    "Settlement and operating reserve",
                    "$6,000 base; 25.00% of startup cash",
                    6000.0,
                    (
                        "Lean $1,500; base $6,000; expanded $9,000. Preserve "
                        "liquidity for settlement delays, refunds, partner disputes, "
                        "and unexpected setup costs. At the metadata's $1,500-$10,000 "
                        "monthly outlay range, the base reserve covers 0.6-4.0 "
                        "months, before considering the higher full Base-Case cost structure."
                    ),
                ),
            ],
        ),
        (
            "diag-08-thirty-day-evidence-sprint",
            "timeline_roadmap",
            "Thirty Days to an Instrumented, Permission-Bounded Pilot",
            "Build operating evidence first; first commercial deal remains a 2-6 month assumption.",
            12,
            "operating_framework",
            (
                "Four sequential milestones cover Days 1-30. Numeric values "
                "represent milestone end days, not durations or revenue. The "
                "sprint does not assume that state registrations, venue access, "
                "or partner contracting finish within thirty days."
            ),
            (
                "Finish with tested analytics, replay-safe attribution, separate "
                "revenue books, and a funded next-step plan; activate only the "
                "activities whose permissions and contracts are established."
            ),
            [
                (
                    "Days 1-7",
                    "Define scope and evidence ownership",
                    7.0,
                    (
                        "Choose the initial regulated analytics source and a narrow "
                        "state affiliate footprint. Inventory CTA, IB, FCM, and "
                        "vendor questions against 7 U.S.C. 1a and 6d and agency "
                        "requirements. Draft separate SaaS and affiliate contract "
                        "checklists, cash budgets, and source-access records."
                    ),
                ),
                (
                    "Days 8-14",
                    "Build isolated feed and event paths",
                    14.0,
                    (
                        "Implement timestamped ingestion, settlement-term matching, "
                        "fee normalization, and stale-feed suppression. Build a "
                        "separate server-to-server event path with signature checks, "
                        "idempotent identifiers, and synthetic CPA fixtures. Test "
                        "location uncertainty, blocked destinations, and duplicate "
                        "events without sending real user funds or orders."
                    ),
                ),
                (
                    "Days 15-21",
                    "Exercise eligibility and settlement logic",
                    21.0,
                    (
                        "Test the 21+ product policy, jurisdiction restrictions, "
                        "current offer disclosures, and responsible-gaming contact "
                        "placement. Reconcile sample CPA rejection codes and NGR "
                        "deductions, including partner-specific negative carryover. "
                        "Verify that simulated invoices and commission statements "
                        "never book trading volume or deposits as revenue."
                    ),
                ),
                (
                    "Days 22-30",
                    "Close pilot evidence and next-month budget",
                    30.0,
                    (
                        "Run a small permitted analytics pilot and activate "
                        "affiliate links only where required status and partner "
                        "authority are documented. Reconcile the $362,500 revenue "
                        "bridge and $137,750 owner-profit model, assign incident "
                        "owners, and budget the remaining 2-6 month path to "
                        "the first deal without treating pilot traffic as earned revenue."
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
