from __future__ import annotations

VOLUME_009_SUBTITLE = (
    "The Complete Playbook for $150,000–$1,200,000 USD Annually in "
    "Enterprise Lead Generation: A 2 FT + 3 C (5-Person) Core Pod, "
    "Scaling to Seven"
)

VOLUME_009_POSITIONING_ALTERNATIVES = [
    {
        "title": "The Enterprise Opportunity Engine",
        "subtitle": (
            "Build an account-based demand-generation pod that earns retainers "
            "and accepted-opportunity fees without counting client contract values."
        ),
        "audience": (
            "Experienced enterprise sellers and boutique agency operators serving "
            "software vendors with complex buying committees and long sales cycles."
        ),
        "research_basis": (
            "Positioning emphasizes buyer relevance, documented outreach rules, "
            "and auditable opportunity acceptance. Commercial email requirements "
            "under 15 U.S.C. 7704 inform sender identification, suppression, and "
            "opt-out operations. These sources establish operating constraints, "
            "not evidence of demand, conversion rates, or achievable earnings."
        ),
        "sources": [
            "https://www.law.cornell.edu/uscode/text/15/7704",
            "https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The ABM Signal-to-Meeting Desk",
        "subtitle": (
            "Turn permissioned account signals into qualified enterprise "
            "conversations through disciplined CRM attribution and scheduling."
        ),
        "audience": (
            "Revenue-operations specialists and demand-generation leaders who "
            "can connect account research, outreach execution, and sales acceptance."
        ),
        "research_basis": (
            "Positioning centers on contact provenance, purpose-limited processing, "
            "and channel-specific outreach controls. California Civil Code "
            "1798.100 and 1798.140 inform covered-business obligations and "
            "applicability analysis; 47 U.S.C. 227 and 47 CFR 64.1200 inform "
            "telephone and text-message controls. Applicability depends on the "
            "actual data, parties, channel, technology, and jurisdiction."
        ),
        "sources": [
            "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1798.100.&lawCode=CIV",
            "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1798.140.&lawCode=CIV",
            "https://www.law.cornell.edu/uscode/text/47/227",
            "https://www.ecfr.gov/current/title-47/section-64.1200",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The High-ACV Origination Studio",
        "subtitle": (
            "Build a specialist enterprise pipeline business with explicit "
            "acceptance evidence, payment triggers, and sector-specific fee rules."
        ),
        "audience": (
            "Domain experts originating enterprise opportunities for a small "
            "portfolio of clients rather than selling undifferentiated contact lists."
        ),
        "research_basis": (
            "Positioning treats fee architecture as a sector-specific design "
            "decision. The federal healthcare anti-kickback statute, RESPA "
            "referral restrictions, and FAR contingent-fee provisions demonstrate "
            "why one referral-payment template cannot serve every vertical. "
            "Flat fees also require substantive review; renaming compensation "
            "does not remove a prohibited referral arrangement."
        ),
        "sources": [
            "https://www.law.cornell.edu/uscode/text/42/1320a-7b",
            "https://www.law.cornell.edu/uscode/text/12/2607",
            "https://www.ecfr.gov/current/title-48/section-3.402",
            "https://www.ecfr.gov/current/title-48/section-52.203-5",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
]


def build_volume_009_diagrams_data() -> list[dict]:
    specs = [
        (
            "diag-01-enterprise-opportunity-workflow",
            "process_flow",
            "From Account Signal to Earned Operator Revenue",
            "Five operating stages connect research, outreach, acceptance, and billing.",
            1,
            "operating_framework",
            (
                "Sequence numbers indicate workflow order, not conversion rates. "
                "The operator earns retainers and qualified-opportunity fees; "
                "client pipeline amounts and signed contract values remain outside "
                "operator revenue. Salesforce, HubSpot, and Calendly are example "
                "tools rather than required vendors."
            ),
            (
                "Every invoice traces to delivered service or a documented "
                "acceptance event, not an inflated client pipeline valuation."
            ),
            [
                (
                    "Define the commercial unit",
                    "Document scope, fee trigger, exclusions, and account ownership.",
                    1.0,
                    (
                        "Specify the ideal customer profile, named-account territory, "
                        "retainer deliverables, qualification rubric, attribution "
                        "window, duplicate rules, and dispute timetable before outreach."
                    ),
                ),
                (
                    "Qualify account signals",
                    "Attach source evidence and timestamps to each target account.",
                    2.0,
                    (
                        "Combine public filings, client-supplied account history, "
                        "and permitted data sources. Record company identity, "
                        "business trigger, buying role, provenance, and suppression status."
                    ),
                ),
                (
                    "Orchestrate relevant outreach",
                    "Coordinate account messaging, channel controls, and meeting availability.",
                    3.0,
                    (
                        "Use HubSpot or Salesforce to manage contact ownership and "
                        "suppression. Automate scheduling through Calendly only after "
                        "checking timezone, seller capacity, and account-routing rules."
                    ),
                ),
                (
                    "Secure opportunity acceptance",
                    "Obtain client confirmation against the written qualification rubric.",
                    4.0,
                    (
                        "Capture the attended conversation, relevant buying role, "
                        "documented business problem, agreed next step, and client "
                        "acceptance timestamp. A booked calendar slot alone does "
                        "not satisfy the illustrated qualified-opportunity standard."
                    ),
                ),
                (
                    "Recognize and reconcile fees",
                    "Match earned retainers and accepted opportunities to invoice lines.",
                    5.0,
                    (
                        "Reconcile the CRM acceptance ledger with invoices, credits, "
                        "and collections. Resolve duplicate claims before billing; "
                        "record advance payments separately until the contracted "
                        "service has been delivered."
                    ),
                ),
            ],
        ),
        (
            "diag-02-nested-enterprise-account-cohort",
            "funnel",
            "A Single Cohort, Five Observable Outcomes",
            "Track client-account pairs instead of mixing contacts, meetings, and deals.",
            6,
            "illustrative_model",
            (
                "Illustrative annual cohort across nine operator clients, followed "
                "through a full observation window. Each unit is one unique "
                "client-account pair, and each later stage is a subset of the "
                "preceding stage. Count at most one qualifying opportunity and "
                "one downstream win per pair. Counts are planning assumptions, "
                "not measured benchmarks. Downstream customer wins may occur "
                "after the opportunity-fee recognition period."
            ),
            (
                "Base revenue bridge: nine clients paying $60,000 in earned annual "
                "retainers produce $540,000; 90 accepted opportunities at $1,500 "
                "produce $135,000; total operator revenue is $675,000."
            ),
            [
                (
                    "Eligible target pairs",
                    "2,400 client-account pairs enter the defined annual cohort.",
                    2400.0,
                    (
                        "Create stable client-account identifiers, verify account "
                        "fit, and exclude suppression records and existing "
                        "opportunities barred by the attribution agreement."
                    ),
                ),
                (
                    "Meaningfully engaged pairs",
                    "600 pairs engage; 25.0% of eligible target pairs.",
                    600.0,
                    (
                        "Require a substantive response or documented buying "
                        "interaction. Email delivery, tracking-pixel activity, "
                        "and bot-generated clicks do not qualify as engagement."
                    ),
                ),
                (
                    "Attended discovery pairs",
                    "180 pairs attend discovery; 30.0% of engaged pairs.",
                    180.0,
                    (
                        "Require an attended session with a relevant buying role. "
                        "Reschedules and repeated meetings retain the same pair "
                        "identifier and do not increase the cohort count."
                    ),
                ),
                (
                    "Accepted opportunity pairs",
                    "90 pairs qualify; 50.0% of attended discovery pairs.",
                    90.0,
                    (
                        "Client acceptance must satisfy the contracted rubric and "
                        "attribution rules. These 90 billable events support the "
                        "$135,000 opportunity-fee component of the Base illustration."
                    ),
                ),
                (
                    "Client contract wins",
                    "18 pairs become customers; 20.0% of accepted opportunities.",
                    18.0,
                    (
                        "Record downstream wins to evaluate delivery quality. "
                        "The resulting customer contract values belong to clients "
                        "and contribute zero additional operator revenue in this model."
                    ),
                ),
            ],
        ),
        (
            "diag-03-base-revenue-to-owner-net",
            "waterfall",
            "The $675,000 Base Revenue-to-Net Bridge",
            "Four expense deductions leave $202,500, exactly 30.0% of revenue.",
            3,
            "illustrative_model",
            (
                "USD annual amounts. The first and final bars are absolute totals; "
                "the four intervening bars are signed expense changes. Expense "
                "categories are illustrative allocations, not supplied scorecard "
                "line items. Canonical Base costs total $472,500, or $39,375 per "
                "month, so the supplied $4,000–$20,000 monthly opex range cannot "
                "describe fully loaded Base expenses. This illustration assigns "
                "$5,625 monthly to operating overhead and separately budgets "
                "payroll, contractors, and direct delivery; that classification "
                "is an explicit modeling assumption."
            ),
            (
                "$675,000 − $180,000 − $135,000 − $90,000 − $67,500 = "
                "$202,500. Canonical annual revenue, margin, and owner net: "
                "Conservative $150,000 / 20% / $30,000; Base $675,000 / 30.0% / "
                "$202,500; Scaled $1,200,000 / 40% / $480,000. Conservative and "
                "Base use five people; Scaled uses seven."
            ),
            [
                (
                    "Recognized operator revenue",
                    "$675,000 earned from retainers and accepted-opportunity fees.",
                    675000.0,
                    (
                        "Opening absolute total: $540,000 of earned retainers "
                        "plus $135,000 of accepted-opportunity fees. Exclude "
                        "client contract values and unearned customer deposits."
                    ),
                ),
                (
                    "Full-time personnel",
                    "Subtract $180,000 for the two full-time operator seats.",
                    -180000.0,
                    (
                        "Illustrative loaded annual personnel budget for the "
                        "operator lead and account director, including budgeted "
                        "founder pay where applicable. Running balance: $495,000."
                    ),
                ),
                (
                    "Contract specialist delivery",
                    "Subtract $135,000 for three contracted specialist seats.",
                    -135000.0,
                    (
                        "Allocate contracted research, campaign production, and CRM "
                        "operations costs to the core pod. Contract scope and "
                        "worker classification require separate review. Running "
                        "balance: $360,000."
                    ),
                ),
                (
                    "Direct campaign delivery",
                    "Subtract $90,000 for operator-funded campaign delivery inputs.",
                    -90000.0,
                    (
                        "Budget incremental campaign data, client-specific production, "
                        "and other direct delivery inputs without duplicating "
                        "contractor costs. Client-funded pass-through spend is "
                        "excluded from this illustration. Running balance: $270,000."
                    ),
                ),
                (
                    "Operating overhead",
                    "Subtract $67,500 for shared operating and administrative costs.",
                    -67500.0,
                    (
                        "Budget shared CRM subscriptions, accounting, insurance, "
                        "security administration, and payment processing separately "
                        "from direct campaign inputs. Monthly equivalent: $5,625. "
                        "Running balance: $202,500."
                    ),
                ),
                (
                    "Annual owner net profit",
                    "$202,500 remaining equals the canonical 30.0% Base margin.",
                    202500.0,
                    (
                        "Closing absolute total, not another positive cash-flow "
                        "increment. Divide $202,500 by $675,000 to obtain 30.0%; "
                        "do not add budgeted founder pay back into this metric."
                    ),
                ),
            ],
        ),
        (
            "diag-04-qualified-opportunity-fee-yields",
            "horizontal_bars",
            "Compare Contracted Fee Yield, Not Client Deal Size",
            "Five illustrative enterprise sub-niches priced per accepted opportunity.",
            2,
            "illustrative_model",
            (
                "Numeric values are illustrative USD operator fees per accepted "
                "opportunity, excluding retainers and before delivery expense. "
                "They are neither market quotations nor profit estimates. "
                "The five bars are alternative pricing hypotheses, not a "
                "portfolio mix to be added together. The Base illustration "
                "uses only the $1,500 fee assumption. ACH and wire describe "
                "collection methods, not permission to pay referral fees."
            ),
            (
                "Test fee yield against delivery cost, acceptance rate, collection "
                "delay, and dispute frequency before choosing a sub-niche."
            ),
            [
                (
                    "Workforce software",
                    "$900 per accepted enterprise workforce-software opportunity.",
                    900.0,
                    (
                        "Illustrative ACH collection against a verified acceptance "
                        "record. Qualify organization size, operating footprint, "
                        "buying role, and a defined workforce-platform initiative."
                    ),
                ),
                (
                    "Logistics software",
                    "$1,200 per accepted enterprise logistics-software opportunity.",
                    1200.0,
                    (
                        "Illustrative ACH collection for software demand generation, "
                        "not freight brokerage. Qualify shipment scale, integration "
                        "requirements, operations ownership, and an active evaluation."
                    ),
                ),
                (
                    "Industrial software",
                    "$1,500 per accepted enterprise industrial-software opportunity.",
                    1500.0,
                    (
                        "Base fee assumption: 90 accepted opportunities generate "
                        "$135,000. Qualify facility context, technical owner, "
                        "integration constraints, and a documented evaluation step."
                    ),
                ),
                (
                    "Cybersecurity platforms",
                    "$1,800 per accepted enterprise cybersecurity-platform opportunity.",
                    1800.0,
                    (
                        "Illustrative wire collection after documented acceptance. "
                        "Qualify security ownership, deployment context, procurement "
                        "path, and relevant need without collecting sensitive "
                        "system access details."
                    ),
                ),
                (
                    "Enterprise data platforms",
                    "$2,100 per accepted enterprise data-platform opportunity.",
                    2100.0,
                    (
                        "Illustrative wire collection against a fixed-fee invoice. "
                        "Qualify architecture fit, data-platform ownership, migration "
                        "trigger, and a credible next evaluation step; exclude "
                        "any percentage of the client's contract value."
                    ),
                ),
            ],
        ),
        (
            "diag-05-preflight-statutory-risk-decisions",
            "decision_tree",
            "Four Pre-Flight Decisions Before Outreach",
            "Proceed on documented facts; remediate or exclude unsupported activities.",
            5,
            "operating_framework",
            (
                "Numeric values indicate ordered decision nodes, not legal-risk "
                "scores. Each node has an explicit proceed branch and a "
                "remediation branch. Apply the cited federal rules together "
                "with relevant state requirements, contract terms, and the "
                "actual channel and sector. A business audience does not "
                "automatically remove privacy or outreach obligations."
            ),
            (
                "A data license, an email address, or a flat-fee label alone "
                "does not establish that the proposed activity is permitted."
            ),
            [
                (
                    "Privacy and provenance",
                    "Proceed with documented permitted use; otherwise quarantine records.",
                    1.0,
                    (
                        "Evaluate California Civil Code 1798.100 and 1798.140 "
                        "where applicable, including covered-business status, "
                        "collection notices, purposes, and data relationships. "
                        "Proceed when sourcing and use are supported; otherwise "
                        "exclude the records until deficiencies are resolved."
                    ),
                ),
                (
                    "Commercial email controls",
                    "Proceed with compliant sender controls; otherwise repair campaign setup.",
                    2.0,
                    (
                        "Apply 15 U.S.C. 7704 to commercial email, including "
                        "accurate headers, nondeceptive subjects, required "
                        "identification, a valid postal address, and an opt-out "
                        "mechanism. Honor opt-outs within ten business days. "
                        "Proceed after checks pass; otherwise pause affected sends."
                    ),
                ),
                (
                    "Telephone and text permissions",
                    "Proceed with channel-specific evidence; otherwise disable affected outreach.",
                    3.0,
                    (
                        "Evaluate 47 U.S.C. 227 and 47 CFR 64.1200 against "
                        "number type, dialing technology, artificial or prerecorded "
                        "voice use, purpose, consent requirements, calling times, "
                        "and do-not-call duties. Proceed only for supported uses; "
                        "otherwise remove calls or texts from the sequence."
                    ),
                ),
                (
                    "Sector and fee restrictions",
                    "Proceed with permitted compensation; otherwise exclude or redesign scope.",
                    4.0,
                    (
                        "Screen healthcare referrals under 42 U.S.C. 1320a-7b(b), "
                        "covered settlement-service referrals under 12 U.S.C. 2607, "
                        "and federal procurement compensation under FAR 3.402 "
                        "and 52.203-5 where applicable. Proceed only with supported "
                        "fee terms and written attribution rules; otherwise "
                        "exclude the activity or obtain a reviewed alternative."
                    ),
                ),
            ],
        ),
        (
            "diag-06-five-to-seven-person-pod",
            "org_architecture",
            "The Five-Person Core and Seven-Person Expansion",
            "Two full-time seats plus three contractors; add one of each at scale.",
            11,
            "operating_framework",
            (
                "FT means full-time; C means contractor. Numeric values show "
                "Base seat occupancy: five occupied seats and two expansion "
                "seats at zero. Conservative and Base use 2 FT + 3 C; Scaled "
                "uses 3 FT + 4 C. Contractor seats represent people, not "
                "full-time equivalents. Role design is illustrative; contractor "
                "status depends on the actual working relationship."
            ),
            (
                "The account director owns client acceptance; the CRM specialist "
                "maintains evidence; the operator lead resolves pricing, capacity, "
                "and customer-concentration decisions."
            ),
            [
                (
                    "Operator lead",
                    "Core FT seat: own sales, pricing, capacity, and cash.",
                    1.0,
                    (
                        "Maintain the agency sales pipeline, approve commercial "
                        "terms, review client concentration monthly, and compare "
                        "collections with payroll and contractor commitments."
                    ),
                ),
                (
                    "Account director",
                    "Core FT seat: own client outcomes and acceptance quality.",
                    1.0,
                    (
                        "Translate client strategy into account plans, run delivery "
                        "reviews, secure opportunity acceptance, and resolve scope "
                        "issues before they become attribution disputes."
                    ),
                ),
                (
                    "Account research specialist",
                    "Core C seat: own target research and signal qualification.",
                    1.0,
                    (
                        "Produce sourced account briefs, maintain identity matching, "
                        "check suppression records, and flag weak buying signals "
                        "before campaign production consumes delivery capacity."
                    ),
                ),
                (
                    "Campaign production specialist",
                    "Core C seat: own messaging assets and outreach preparation.",
                    1.0,
                    (
                        "Develop account-relevant messaging, prepare channel-specific "
                        "campaign assets, inspect suppression settings, and route "
                        "substantive replies into the client-account record."
                    ),
                ),
                (
                    "CRM and attribution specialist",
                    "Core C seat: own scheduling, acceptance evidence, and reconciliation.",
                    1.0,
                    (
                        "Configure Salesforce or HubSpot workflows, connect Calendly "
                        "routing, preserve source timestamps, deduplicate events, "
                        "and reconcile accepted opportunities with invoice lines."
                    ),
                ),
                (
                    "Client success manager",
                    "Expansion FT seat: activate for the seven-person Scaled pod.",
                    0.0,
                    (
                        "Add one full-time person to absorb onboarding, reporting, "
                        "and renewal coordination when measured account workload "
                        "exceeds the core account director's sustainable capacity."
                    ),
                ),
                (
                    "Research and production support",
                    "Expansion C seat: activate for the seven-person Scaled pod.",
                    0.0,
                    (
                        "Add one contracted specialist for the demonstrated research "
                        "or production bottleneck. Preserve qualification standards "
                        "rather than increasing volume through weaker acceptance criteria."
                    ),
                ),
            ],
        ),
        (
            "diag-07-startup-capital-allocation",
            "stacked_comparison",
            "Allocate Startup Cash Before Expanding Delivery",
            "Four buckets sum to a $60,000 illustrative launch budget.",
            4,
            "illustrative_model",
            (
                "Numeric values are USD allocations in the $60,000 central "
                "illustration, inside the canonical $15,000–$100,000 startup "
                "range. Allocation shares are 20%, 30%, 20%, and 30%. Applying "
                "the same shares to the two endpoints produces complete "
                "$15,000 and $100,000 comparison budgets. These are cash "
                "allocations, not annual expenses or recognized revenue."
            ),
            (
                "First-deal timing remains 3–12 months. The $18,000 reserve "
                "covers 4.5 months at $4,000 monthly cash burn or 0.9 months "
                "at $20,000; it does not fund a fully staffed Base pod."
            ),
            [
                (
                    "Formation and operating setup",
                    "$12,000 central allocation; 20% of total startup capital.",
                    12000.0,
                    (
                        "Fund entity setup, contract drafting, initial insurance, "
                        "security configuration, and bookkeeping implementation. "
                        "At the $15,000 and $100,000 endpoints, allocate "
                        "$3,000 and $20,000 respectively."
                    ),
                ),
                (
                    "CRM and research infrastructure",
                    "$18,000 central allocation; 30% of total startup capital.",
                    18000.0,
                    (
                        "Fund scoped CRM implementation, licensed research inputs, "
                        "scheduling integration, and initial attribution reporting. "
                        "At the $15,000 and $100,000 endpoints, allocate "
                        "$4,500 and $30,000 respectively."
                    ),
                ),
                (
                    "Pilot production and proof",
                    "$12,000 central allocation; 20% of total startup capital.",
                    12000.0,
                    (
                        "Fund limited specialist assignments, account briefs, "
                        "messaging assets, and acceptance-ledger testing for "
                        "a narrow pilot. At the $15,000 and $100,000 endpoints, "
                        "allocate $3,000 and $20,000 respectively."
                    ),
                ),
                (
                    "Uncommitted cash reserve",
                    "$18,000 central allocation; 30% of total startup capital.",
                    18000.0,
                    (
                        "Retain liquid cash for collection delays and essential "
                        "operating commitments. At the $15,000 and $100,000 "
                        "endpoints, allocate $4,500 and $30,000 respectively. "
                        "Reduce commitments or secure more runway if the "
                        "sales-cycle forecast exceeds available cash."
                    ),
                ),
            ],
        ),
        (
            "diag-08-thirty-day-launch-sprint",
            "timeline_roadmap",
            "Thirty Days to an Instrumented Pilot",
            "Build operating evidence now; allow 3–12 months for the first deal.",
            12,
            "operating_framework",
            (
                "Numeric values mark milestone end days: 7, 14, 21, and 30. "
                "The sprint establishes a functioning pilot and decision evidence, "
                "not a promised signed client or enterprise contract. Outreach "
                "requires the relevant checks to be completed and, when acting "
                "for a client, documented client authorization."
            ),
            (
                "Finish with traceable account records, tested acceptance logic, "
                "a reconciled pilot ledger, and a cash-backed continuation decision."
            ),
            [
                (
                    "Days 1-7",
                    "Select one sub-niche and define the billable opportunity.",
                    7.0,
                    (
                        "Interview prospective buyers, document the ideal customer "
                        "profile, define retainer deliverables and acceptance "
                        "criteria, review sector restrictions, and build a cash "
                        "forecast around the 3–12 month first-deal range."
                    ),
                ),
                (
                    "Days 8-14",
                    "Configure the CRM, provenance records, and suppression workflows.",
                    14.0,
                    (
                        "Implement client-account identifiers, source timestamps, "
                        "contact restrictions, acceptance fields, and invoice "
                        "references. Test scheduling, duplicate detection, opt-out "
                        "handling, and access controls using clearly labeled test records."
                    ),
                ),
                (
                    "Days 15-21",
                    "Run a narrow pilot with documented outreach authority.",
                    21.0,
                    (
                        "Launch a capacity-limited account cohort only after "
                        "pre-flight checks. If no client is signed, test the "
                        "agency's own acquisition workflow instead of claiming "
                        "client delivery. Record replies, attended meetings, "
                        "labor hours, and actual cash spend."
                    ),
                ),
                (
                    "Days 22-30",
                    "Audit cohort evidence and decide the next funded iteration.",
                    30.0,
                    (
                        "Review acceptance failures, duplicate claims, response "
                        "quality, collection terms, and client concentration "
                        "exposure. Reconcile any earned fees with the ledger, "
                        "update the cash forecast, and expand only when workload "
                        "and available runway support the added commitments."
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
