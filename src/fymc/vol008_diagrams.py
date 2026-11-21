from __future__ import annotations

VOLUME_008_SUBTITLE = (
    "The Complete Playbook for Commercial Lead Generation: "
    "$100,000–$750,000 USD Annually, Starting with a "
    "1 FT + 3 C (4 People) Pod"
)

VOLUME_008_POSITIONING_ALTERNATIVES = [
    {
        "title": "The Accepted-Appointment Revenue Engine",
        "subtitle": (
            "Build commercial lead-generation retainers and accepted-appointment "
            "fees around documented qualification, attribution, and client acceptance."
        ),
        "audience": (
            "Founder-led B2B agencies serving commercial contractors, managed "
            "service providers, and industrial service companies with defined territories."
        ),
        "research_basis": (
            "15 U.S.C. 7704 supplies concrete commercial-email requirements for "
            "sender identity, message content, and opt-out handling. Those obligations "
            "support an auditable outreach workflow; they do not establish demand, "
            "appointment prices, or conversion performance."
        ),
        "sources": [
            "https://www.law.cornell.edu/uscode/text/15/7704",
            "https://www.ftc.gov/business-guidance/resources/"
            "can-spam-act-compliance-guide-business",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Traceable Commercial Call Desk",
        "subtitle": (
            "Sell qualified B2B conversations with documented call eligibility, "
            "routing ownership, acceptance evidence, and replacement rules."
        ),
        "audience": (
            "Small appointment-setting and call-routing teams supporting commercial "
            "service sellers with staffed calendars and measurable response capacity."
        ),
        "research_basis": (
            "47 U.S.C. 227 and 47 CFR 64.1200 distinguish restrictions by call "
            "technology, purpose, destination, and consent. 16 CFR 310.6 describes "
            "qualified exemptions rather than a blanket exemption for every "
            "business-directed call. These sources support channel-specific controls, "
            "not a universal permission to call purchased contacts."
        ),
        "sources": [
            "https://www.law.cornell.edu/uscode/text/47/227",
            "https://www.ecfr.gov/current/title-47/chapter-I/"
            "subchapter-B/part-64/subpart-L/section-64.1200",
            "https://www.ecfr.gov/current/title-16/chapter-I/"
            "subchapter-C/part-310/section-310.6",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Permission-Aware Outbound Operations Pod",
        "subtitle": (
            "Run multi-inbox outreach, CRM routing, suppression, and lead-quality "
            "reporting as one accountable commercial service."
        ),
        "audience": (
            "Experienced sales-operations practitioners building a four-person "
            "service pod for clients with fragmented outreach and CRM ownership."
        ),
        "research_basis": (
            "California Civil Code sections 1798.100, 1798.120, and 1798.140 "
            "address covered-business duties, sale or sharing choices, and scope "
            "definitions. Combined with federal commercial-email rules, they support "
            "purpose tracking, suppression propagation, and documented client roles "
            "where applicable; they do not validate a particular service price."
        ),
        "sources": [
            "https://leginfo.legislature.ca.gov/faces/"
            "codes_displaySection.xhtml?lawCode=CIV&sectionNum=1798.100.",
            "https://leginfo.legislature.ca.gov/faces/"
            "codes_displaySection.xhtml?lawCode=CIV&sectionNum=1798.120.",
            "https://leginfo.legislature.ca.gov/faces/"
            "codes_displaySection.xhtml?lawCode=CIV&sectionNum=1798.140.",
            "https://www.law.cornell.edu/uscode/text/15/7704",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
]


def build_volume_008_diagrams_data() -> list[dict]:
    specs = [
        (
            "diag-01-accepted-lead-workflow",
            "process_flow",
            "Turn Eligible Accounts into Accepted Operator Revenue",
            (
                "Five operating stages connect account selection, outreach, "
                "qualification, routing, and recognized service fees."
            ),
            1,
            "operating_framework",
            (
                "Stage numbers indicate sequence, not conversion volume. Revenue "
                "means retainers and accepted-lead fees; client-funded advertising "
                "pass-through and the client's downstream sales remain excluded."
            ),
            (
                "A lead becomes billable only under the agreed acceptance definition. "
                "Keep eligibility evidence, qualification fields, routing timestamps, "
                "and acceptance outcomes attached to the same CRM record."
            ),
            [
                (
                    "Define the commercial target",
                    "Specify territory, buyer role, and qualifying need.",
                    1.0,
                    (
                        "The founder records service territory, excluded accounts, "
                        "buyer authority, minimum project fit, and duplicate rules "
                        "before sourcing contacts or quoting accepted-lead fees."
                    ),
                ),
                (
                    "Establish contact eligibility",
                    "Check provenance, channel rules, and suppression status.",
                    2.0,
                    (
                        "Record source, collection date, permitted purpose, and "
                        "channel-specific evidence. Reconcile CRM suppression with "
                        "every sending inbox and calling queue before activation."
                    ),
                ),
                (
                    "Run identifiable outreach",
                    "Operate authenticated inboxes with truthful sender identity.",
                    3.0,
                    (
                        "Configure SPF, DKIM, and DMARC on authorized domains. "
                        "Use Google Workspace or Microsoft 365 within provider "
                        "limits; investigate complaints instead of rotating inboxes "
                        "to bypass restrictions."
                    ),
                ),
                (
                    "Qualify and route",
                    "Confirm need, fit, ownership, and appointment availability.",
                    4.0,
                    (
                        "Use HubSpot or Salesforce required fields and Calendly "
                        "availability to verify the buyer's request, assign an "
                        "account owner, and prevent duplicate appointment billing."
                    ),
                ),
                (
                    "Accept, invoice, and learn",
                    "Record acceptance evidence before recognizing lead fees.",
                    5.0,
                    (
                        "Apply the signed acceptance and dispute terms, invoice "
                        "earned retainers and accepted units, and report rejection "
                        "reasons by source. Feed poor-fit patterns back into targeting."
                    ),
                ),
            ],
        ),
        (
            "diag-02-annual-account-to-acceptance-funnel",
            "funnel",
            "One Annual Cohort, Five Nested Conversion Stages",
            (
                "An illustrative 5,000-account cohort produces 60 client-accepted "
                "appointments without counting messages as separate prospects."
            ),
            6,
            "illustrative_model",
            (
                "All stages count distinct accounts from one annual cohort; each "
                "later stage is a subset of the preceding stage. Count at most one "
                "accepted appointment per account. These are planning assumptions, "
                "not observed conversion benchmarks. Sixty accepted appointments "
                "at $1,000 produce $60,000; five annual client retainers at $73,000 "
                "produce $365,000; combined Base revenue is exactly $425,000."
            ),
            (
                "Stage conversions are 40%, 10%, 40%, and 75%; total accepted yield "
                "is 1.2% of screened accounts. Retainers are a separate revenue "
                "component, not an additional prospect-conversion stage."
            ),
            [
                (
                    "Eligible target accounts",
                    "5,000 distinct accounts meet documented screening criteria.",
                    5000.0,
                    (
                        "Deduplicate company domains and legal entities, confirm "
                        "commercial fit, and remove suppressed contacts before "
                        "including an account in the annual eligible cohort."
                    ),
                ),
                (
                    "Accounts reached",
                    "2,000 accounts receive at least one eligible outreach.",
                    2000.0,
                    (
                        "Forty percent of screened accounts receive a delivered "
                        "message through an eligible channel. Multiple contacts, "
                        "inboxes, and follow-ups still count as one reached account."
                    ),
                ),
                (
                    "Positive account responses",
                    "200 accounts express interest in a relevant conversation.",
                    200.0,
                    (
                        "Ten percent of reached accounts provide a positive human "
                        "response. Exclude automatic replies, unsubscribe requests, "
                        "wrong-person referrals without interest, and duplicate threads."
                    ),
                ),
                (
                    "Held qualified appointments",
                    "80 accounts complete conversations meeting the qualification rubric.",
                    80.0,
                    (
                        "Forty percent of positive accounts attend a conversation "
                        "with verified territory, commercial need, and buyer role. "
                        "Exclude cancellations, no-shows, and merely booked meetings."
                    ),
                ),
                (
                    "Client-accepted appointments",
                    "60 accounts produce accepted units worth $60,000 annually.",
                    60.0,
                    (
                        "Clients accept seventy-five percent of held qualified "
                        "appointments under written criteria. Bill $1,000 per "
                        "accepted unit; track the twenty rejected units separately."
                    ),
                ),
            ],
        ),
        (
            "diag-03-base-case-owner-net-waterfall",
            "waterfall",
            "Reconcile $425,000 Revenue to $127,500 Owner Net",
            (
                "Six bars: recognized revenue, four operating-cost deductions, "
                "and a final 30.0% owner-net total."
            ),
            3,
            "illustrative_model",
            (
                "Annual USD. The first and final bars are absolute totals; the "
                "four intervening bars are negative movements. The final bar is "
                "not another additive movement. Cost allocations are illustrative "
                "but reconcile exactly to the canonical Base scenario. The "
                "$57,500 combined software and administration budget averages "
                "$4,791.67 monthly, within the $2,000–$12,000 standing-opex range; "
                "variable delivery and acquisition costs are additional. Owner net "
                "is before personal income taxes and owner distributions; no "
                "separate founder salary is deducted in this allocation."
            ),
            (
                "$425,000 − $150,000 − $90,000 − $24,000 − $33,500 = $127,500. "
                "Canonical annual scenarios remain Conservative $100,000 at 20% "
                "= $20,000; Base $425,000 at 30.0% = $127,500; Scaled $750,000 "
                "at 40% = $300,000. Conservative and Base use 1 FT + 3 C; "
                "Scaled uses 2 FT + 4 C."
            ),
            [
                (
                    "Recognized operator revenue",
                    "Start with $425,000 in earned service revenue.",
                    425000.0,
                    (
                        "Recognize $365,000 of annual retainers plus $60,000 "
                        "of accepted-appointment fees. Exclude client advertising "
                        "pass-through, client contract value, and client sales proceeds."
                    ),
                ),
                (
                    "Delivery labor and fulfillment",
                    "Deduct $150,000 for contracted service delivery capacity.",
                    -150000.0,
                    (
                        "Budget the three contractor seats, appointment handling, "
                        "quality review, and rework inside this delivery envelope. "
                        "The remaining annual contribution becomes $275,000."
                    ),
                ),
                (
                    "Operator-funded acquisition",
                    "Deduct $90,000 for operator-paid acquisition and sourcing.",
                    -90000.0,
                    (
                        "Include direct prospect sourcing and operator-funded "
                        "campaign acquisition expenses, not client-funded advertising "
                        "pass-through. Do not duplicate standing software costs. "
                        "The remaining contribution becomes $185,000."
                    ),
                ),
                (
                    "Software and communications",
                    "Deduct $24,000 for the standing operating stack.",
                    -24000.0,
                    (
                        "Budget CRM, authorized mailboxes, telephony, scheduling, "
                        "and reporting subscriptions at $2,000 monthly. Keep usage "
                        "charges in one cost category. Remaining contribution is $161,000."
                    ),
                ),
                (
                    "Administration and service overhead",
                    "Deduct $33,500 for administration and operating overhead.",
                    -33500.0,
                    (
                        "Cover bookkeeping, insurance, payment processing, contract "
                        "review, and general business administration. This final "
                        "expense deduction leaves exactly $127,500 of annual owner net."
                    ),
                ),
                (
                    "Annual owner net total",
                    "Finish with $127,500, exactly 30.0% of revenue.",
                    127500.0,
                    (
                        "Render this endpoint as an absolute total from zero. "
                        "Annual modeled expenses total $297,500, or 70% of "
                        "recognized operator revenue; the founder occupies the full-time seat."
                    ),
                ),
            ],
        ),
        (
            "diag-04-subniche-accepted-appointment-yields",
            "horizontal_bars",
            "Compare Accepted-Appointment Fee Hypotheses",
            (
                "Five commercial sub-niches use the same unit: operator service "
                "revenue per client-accepted appointment."
            ),
            2,
            "illustrative_model",
            (
                "USD per accepted appointment, excluding retainers and advertising "
                "pass-through. Prices are deliberately illustrative quote hypotheses, "
                "not market averages or incremental revenue to add to the scorecard. "
                "Only the $1,000 hypothesis feeds the Base funnel. ACH and card "
                "describe collection methods; processing expenses belong in costs "
                "and do not change the gross-fee comparison."
            ),
            (
                "Validate each fee against client gross contribution, close rate, "
                "attendance, and replacement burden. A $1,000 appointment at a "
                "20% close rate implies $5,000 in appointment fees per won client "
                "before retainers and the client's own selling costs."
            ),
            [
                (
                    "Commercial HVAC service",
                    "$1,000 accepted appointment fee, collected through ACH invoicing.",
                    1000.0,
                    (
                        "Require an in-territory commercial site, relevant equipment "
                        "scope, and an authorized facilities contact. Reject "
                        "residential requests and emergency calls outside staffed coverage."
                    ),
                ),
                (
                    "Managed IT services",
                    "$900 accepted appointment fee, collected through ACH invoicing.",
                    900.0,
                    (
                        "Verify employee or endpoint range, incumbent-provider "
                        "context, and a business decision-maker. Reject consumer "
                        "device support and accounts below the contracted service minimum."
                    ),
                ),
                (
                    "Industrial equipment maintenance",
                    "$800 accepted appointment fee, collected through ACH invoicing.",
                    800.0,
                    (
                        "Capture equipment category, site location, maintenance "
                        "need, and purchasing responsibility. Reject unsupported "
                        "equipment and work outside the client's field-service territory."
                    ),
                ),
                (
                    "Contract logistics services",
                    "$700 accepted appointment fee, collected through ACH invoicing.",
                    700.0,
                    (
                        "Confirm shipment frequency, lane coverage, cargo category, "
                        "and commercial procurement ownership. Reject one-time "
                        "consumer moves and lanes the client cannot economically serve."
                    ),
                ),
                (
                    "Commercial cleaning contracts",
                    "$600 accepted appointment fee, collected through card invoicing.",
                    600.0,
                    (
                        "Verify facility size, recurring service frequency, access "
                        "requirements, and decision authority. Reject residential "
                        "cleaning and sites below the client's minimum monthly contract."
                    ),
                ),
            ],
        ),
        (
            "diag-05-channel-and-commercial-risk-decisions",
            "decision_tree",
            "Four Pre-Flight Checks Before Contact or Routing",
            (
                "Each check has an explicit proceed condition and an explicit "
                "stop-and-repair branch."
            ),
            5,
            "operating_framework",
            (
                "Numeric values identify check order, not risk scores. Evaluate "
                "each channel separately and document why an unused channel is "
                "disabled. Federal rules are the starting point; applicable state "
                "privacy, calling, and recording requirements also depend on the "
                "parties, locations, technology, and campaign facts."
            ),
            (
                "Proceed only when every applicable check has evidence. Missing "
                "permission, unresolved suppression, unsupported routing, or ambiguous "
                "acceptance criteria sends the affected activity back for repair."
            ),
            [
                (
                    "Commercial-email requirements",
                    "Proceed with truthful identity and functioning opt-out handling.",
                    1.0,
                    (
                        "Apply 15 U.S.C. 7704: accurate header information, "
                        "nondeceptive subjects, required advertising identification "
                        "unless an exception applies, valid physical postal address, "
                        "and a functioning opt-out. Honor opt-outs within ten "
                        "business days; stop affected sends when suppression fails."
                    ),
                ),
                (
                    "Calling and recording requirements",
                    "Proceed only after documenting the specific calling basis.",
                    2.0,
                    (
                        "Check 47 U.S.C. 227, 47 CFR 64.1200, applicable "
                        "16 CFR Part 310 duties, and state calling and recording "
                        "rules. Distinguish live manual calls from automated or "
                        "prerecorded activity and business numbers from personal "
                        "wireless numbers. Disable unsupported dialing or recording."
                    ),
                ),
                (
                    "Privacy and data handling",
                    "Proceed with documented scope, purpose, and rights handling.",
                    3.0,
                    (
                        "Assess California Civil Code 1798.100, 1798.120, and "
                        "1798.140 where applicable, plus other relevant state rules. "
                        "Document client and vendor roles, collection notices, "
                        "retention, access controls, and rights-request ownership. "
                        "Stop transfers that conflict with applicable sale or sharing choices."
                    ),
                ),
                (
                    "Quality and commercial exposure",
                    "Proceed with measurable acceptance and bounded delivery commitments.",
                    4.0,
                    (
                        "Sign territory, qualification, duplicate, acceptance, "
                        "replacement, fee, and dispute terms. Test routing capacity "
                        "and assign a suppression owner. Pause the affected campaign "
                        "when rejection costs, acquisition costs, or churn erase "
                        "its modeled contribution."
                    ),
                ),
            ],
        ),
        (
            "diag-06-four-to-six-person-pod",
            "org_architecture",
            "Four Core Seats, Two Explicit Scale Additions",
            (
                "Conservative and Base: 1 FT + 3 C. "
                "Scaled: 2 FT + 4 C."
            ),
            11,
            "operating_framework",
            (
                "FT means full-time seat; C means contractor seat, not a "
                "full-time-equivalent assertion. Each numeric value represents "
                "one person. The first four seats form the baseline pod; the "
                "final two are scaled-only additions. Do not total all six seats "
                "as Base staffing or assume identical contractor hours."
            ),
            (
                "The founder remains accountable for pricing and delivery economics. "
                "Automation supports consent tracking, CRM routing, and lead-quality "
                "reporting; named people still own exceptions and client acceptance."
            ),
            [
                (
                    "Founder and commercial owner",
                    "Core seat: one full-time owner leads commercial decisions.",
                    1.0,
                    (
                        "Own positioning, sales, contracts, client relationships, "
                        "contribution review, and unresolved delivery issues. "
                        "At scale, delegate routine account operations to the added "
                        "full-time client-success lead."
                    ),
                ),
                (
                    "Data and CRM operator",
                    "Core seat: one contractor owns provenance and routing.",
                    1.0,
                    (
                        "Maintain account deduplication, source records, consent "
                        "evidence where required, suppression propagation, access "
                        "permissions, and HubSpot or Salesforce assignment rules."
                    ),
                ),
                (
                    "Outbound infrastructure operator",
                    "Core seat: one contractor owns authorized outreach operations.",
                    1.0,
                    (
                        "Maintain domain authentication, mailbox configuration, "
                        "provider-limit adherence, message scheduling, bounce review, "
                        "and complaint investigation. Escalate delivery problems "
                        "without bypassing provider restrictions."
                    ),
                ),
                (
                    "Qualification and call-routing operator",
                    "Core seat: one contractor verifies conversations and handoffs.",
                    1.0,
                    (
                        "Review replies, qualify commercial need, confirm calendars, "
                        "route calls, and collect acceptance evidence. Track no-shows "
                        "and rejection causes without billing merely booked appointments."
                    ),
                ),
                (
                    "Client-success lead",
                    "Scaled addition: one full-time employee owns account delivery.",
                    1.0,
                    (
                        "Join only in the six-person configuration. Own client "
                        "reporting, renewal preparation, delivery commitments, "
                        "acceptance disputes, and capacity planning across active accounts."
                    ),
                ),
                (
                    "Quality and reporting analyst",
                    "Scaled addition: one contractor owns independent quality review.",
                    1.0,
                    (
                        "Join only in the six-person configuration. Audit "
                        "qualification records, reconcile accepted units to invoices, "
                        "analyze acquisition cost, and identify sources creating "
                        "excessive replacement work."
                    ),
                ),
            ],
        ),
        (
            "diag-07-startup-capital-allocation",
            "stacked_comparison",
            "Allocate Startup Cash Before Expanding Volume",
            (
                "Four buckets form a $20,000 planning stack, with matched "
                "$5,000 lean and $40,000 expanded allocations."
            ),
            4,
            "illustrative_model",
            (
                "Numeric values are the four segments of one $20,000 startup "
                "budget. The lean and expanded amounts in each stage use the "
                "same 30%, 20%, 30%, and 20% allocation weights and total "
                "$5,000 and $40,000 respectively. These are alternative cash "
                "plans, not three budgets to add together or scorecard revenue "
                "scenarios. Startup cash is not a recurring annual expense total."
            ),
            (
                "Reserve deployment follows evidence, not inbox count. The "
                "$2,000–$12,000 monthly operating range requires a separate cash "
                "forecast, especially because the first deal may take one to four months."
            ),
            [
                (
                    "Infrastructure and operating systems",
                    "Plan $6,000; lean $1,500; expanded $12,000 for infrastructure.",
                    6000.0,
                    (
                        "Allocate thirty percent to CRM setup, authorized domains, "
                        "authenticated mailboxes, scheduling, telephony configuration, "
                        "and initial subscription cash. Record prepaid services "
                        "separately from recurring monthly expense."
                    ),
                ),
                (
                    "Data and qualification development",
                    "Plan $4,000; lean $1,000; expanded $8,000 for qualification.",
                    4000.0,
                    (
                        "Allocate twenty percent to permitted data sourcing, "
                        "account verification, qualification scripts, and small-sample "
                        "quality review. Avoid buying broad lists before validating "
                        "territory fit and contact eligibility."
                    ),
                ),
                (
                    "Pilot delivery and acquisition",
                    "Plan $6,000; lean $1,500; expanded $12,000 for pilots.",
                    6000.0,
                    (
                        "Allocate thirty percent to contractor pilot work and "
                        "operator-funded acquisition tests. Measure held and accepted "
                        "appointments rather than opens or raw booked meetings; "
                        "stop cohorts with unaffordable rejection costs."
                    ),
                ),
                (
                    "Working-capital reserve",
                    "Plan $4,000; lean $1,000; expanded $8,000 as reserve.",
                    4000.0,
                    (
                        "Retain twenty percent for collection delays, replacement "
                        "work, and service continuity. The planning reserve covers "
                        "two months at $2,000 monthly operating spend but only "
                        "one-third of a month at $12,000."
                    ),
                ),
            ],
        ),
        (
            "diag-08-thirty-day-commercial-launch",
            "timeline_roadmap",
            "Build a Measurable Commercial Service in Thirty Days",
            (
                "Four weekly milestones establish scope, infrastructure, pilot "
                "evidence, and a delivery-ready operating review."
            ),
            12,
            "operating_framework",
            (
                "Numeric values are elapsed-day endpoints: 7, 14, 21, and 30. "
                "This sprint builds operating capability; the canonical first-deal "
                "window remains one to four months. Pilot activity uses authorized "
                "resources and eligible contacts, with spend bounded by the "
                "selected $5,000–$40,000 startup cash plan."
            ),
            (
                "Finish day thirty with documented evidence and a clear continue, "
                "repair, or stop decision for each pilot cohort. Do not manufacture "
                "accepted leads, booked revenue, or a signed client to satisfy the calendar."
            ),
            [
                (
                    "Days 1-7",
                    "Choose one niche and write the acceptance contract.",
                    7.0,
                    (
                        "Select territory and buyer profile; interview prospective "
                        "clients; define accepted-appointment criteria, duplicate "
                        "rules, fees, and dispute handling. Produce a channel "
                        "requirements checklist and a cash forecast through the "
                        "four-month first-deal window."
                    ),
                ),
                (
                    "Days 8-14",
                    "Configure systems and test every suppression and routing path.",
                    14.0,
                    (
                        "Authenticate authorized domains, configure CRM fields and "
                        "least-privilege access, and connect scheduling and call "
                        "routing. Use synthetic test records to verify opt-outs, "
                        "duplicate handling, assignment failures, and evidence retention."
                    ),
                ),
                (
                    "Days 15-21",
                    "Run a bounded pilot and inspect qualification evidence.",
                    21.0,
                    (
                        "Activate a small eligible account cohort with explicit "
                        "spend and contact limits. Review delivered accounts, "
                        "positive replies, held appointments, rejection causes, "
                        "and contractor time daily; repair failures before increasing volume."
                    ),
                ),
                (
                    "Days 22-30",
                    "Review unit economics and prepare accountable client delivery.",
                    30.0,
                    (
                        "Reconcile cohort counts, accepted units, invoices when "
                        "earned, and actual costs. Demonstrate the reporting pack, "
                        "assign each exception owner, and pursue a retainer under "
                        "the written scope without treating pipeline value as revenue."
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
