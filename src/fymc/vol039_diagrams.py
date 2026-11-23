from __future__ import annotations

VOLUME_039_SUBTITLE = (
    "The Complete Playbook for Inbound Pay-Per-Call & RTB Ping-Post Arbitrage: "
    "$200,000–$1,500,000 USD in Annual Gross Settlements, "
    "Starting with a 1 FT + 2 C (3 People) Pod"
)

VOLUME_039_POSITIONING_ALTERNATIVES = [
    {
        "title": "The Collectible Call Exchange",
        "subtitle": (
            "Build a three-person inbound exchange around buyer acceptance, "
            "auditable call qualification, and cash collected before traffic expansion."
        ),
        "audience": (
            "Paid-search operators and affiliate managers building an authorized "
            "Ringba or Retreaver exchange with directly contracted buyers."
        ),
        "research_basis": (
            "47 CFR 64.1200 distinguishes regulated outbound communications from "
            "other call activity; 16 CFR 310.4 supplies applicable telemarketing "
            "restrictions. Preserve the distinction between consumer-initiated "
            "inbound calls, transfers, and later outbound contact. Buyer-specific "
            "consent evidence is an operating control, not proof of a universal "
            "FCC one-seller requirement."
        ),
        "sources": [
            "https://www.ecfr.gov/current/title-47/section-64.1200",
            "https://www.ecfr.gov/current/title-16/section-310.4",
            "https://www.law.cornell.edu/uscode/text/47/227",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Medicare Call Evidence Desk",
        "subtitle": (
            "Route Medicare inquiries with permission provenance, recorded "
            "marketing calls, documented appointment timing, and buyer-level reconciliation."
        ),
        "audience": (
            "Experienced insurance lead operators serving contracted Medicare "
            "organizations and their third-party marketing organizations."
        ),
        "research_basis": (
            "42 CFR 422.2264 and 423.2264 govern beneficiary contact and appointment "
            "practices, including the applicable 48-hour scope-of-appointment rule "
            "and exceptions. Sections 422.2274 and 423.2274 address TPMO oversight, "
            "call recording, and beneficiary-information sharing. Do not treat "
            "every unscheduled inbound inquiry as a scheduled appointment."
        ),
        "sources": [
            "https://www.ecfr.gov/current/title-42/section-422.2264",
            "https://www.ecfr.gov/current/title-42/section-423.2264",
            "https://www.ecfr.gov/current/title-42/section-422.2274",
            "https://www.ecfr.gov/current/title-42/section-423.2274",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Emergency-Service Routing Desk",
        "subtitle": (
            "Auction verified local-service inquiries against live dispatch "
            "capacity, geographic fit, and collectible per-call prices."
        ),
        "audience": (
            "Local-service media buyers serving plumbing, HVAC, and restoration "
            "contractors through fixed-price, documented inbound-call agreements."
        ),
        "research_basis": (
            "15 U.S.C. 45 supports truthful advertising and accurate representations "
            "of provider identity. Applicable outbound follow-up remains subject "
            "to 47 CFR 64.1200. California Penal Code section 632 illustrates why "
            "recording design must account for state confidentiality requirements "
            "rather than assuming a single nationwide recording standard."
        ),
        "sources": [
            "https://www.law.cornell.edu/uscode/text/15/45",
            "https://www.ecfr.gov/current/title-47/section-64.1200",
            (
                "https://leginfo.legislature.ca.gov/faces/"
                "codes_displaySection.xhtml?sectionNum=632.&lawCode=PEN"
            ),
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
]


def build_volume_039_diagrams_data() -> list[dict]:
    specs = [
        (
            "diag-01-inbound-auction-to-collected-cash",
            "process_flow",
            "One inquiry, one auditable settlement",
            "Separate routing speed from qualification evidence and cash collection.",
            1,
            "operating_framework",
            (
                "Illustrative operating sequence for directly contracted publishers "
                "and buyers. Ringba or Retreaver timeout settings are tested against "
                "actual buyer response times; sub-second bidding is an engineering "
                "target, not an asserted service level. A 90–120 second threshold "
                "is a negotiated billing condition, never evidence of lawful contact."
            ),
            (
                "Preserve a shared call identifier from source click through buyer "
                "payment; a winning bid alone does not establish collectible revenue."
            ),
            [
                (
                    "Capture source and permission",
                    "Bind click, caller, disclosure, and intended recipient",
                    1.0,
                    (
                        "Persist source campaign, landing-page version, timestamp, "
                        "recipient identity, and TrustedForm or Jornaya evidence "
                        "where applicable. A certificate records evidence; it does "
                        "not independently establish valid permission."
                    ),
                ),
                (
                    "Validate inquiry and eligibility",
                    "Check geography, duplication, contact rules, and capacity",
                    2.0,
                    (
                        "Confirm service intent, buyer coverage, business hours, "
                        "and duplicate-call lookback. For regulated outbound "
                        "follow-up, apply current suppression and permission rules. "
                        "A commercial litigation-risk list never substitutes for "
                        "National or entity-specific DNC controls."
                    ),
                ),
                (
                    "Ping eligible contracted buyers",
                    "Auction minimal attributes against live caps",
                    3.0,
                    (
                        "Send only contractually permitted routing attributes. "
                        "Apply Ringba or Retreaver bid timeouts, geographic filters, "
                        "capacity limits, and a fallback route; avoid broadcasting "
                        "the caller's identity to every bidder."
                    ),
                ),
                (
                    "Post and qualify the connection",
                    "Connect once and measure contracted connected seconds",
                    4.0,
                    (
                        "Select the eligible bid, connect the caller, and measure "
                        "the buyer-agreed 90–120 second buffer using the agreed "
                        "clock. Distinguish ringing, hold time, and agent-connected "
                        "time; review transcript classifications before billing."
                    ),
                ),
                (
                    "Reconcile and collect",
                    "Resolve scrubs before increasing publisher exposure",
                    5.0,
                    (
                        "Match disposition, duration, duplicate status, invoice, "
                        "and bank receipt by call identifier. Keep publisher caps "
                        "tight until actual net-7 buyer collections are verified; "
                        "send S2S value corrections when accepted calls reverse."
                    ),
                ),
            ],
        ),
        (
            "diag-02-nested-cohort-settlement-funnel",
            "funnel",
            "From paid visits to settled calls",
            "A single annual cohort produces the Base-Case $850,000 gross settlement model.",
            6,
            "illustrative_model",
            (
                "All five stages belong to the same illustrative annual cohort. "
                "Each later stage is a subset of the prior stage, with one counted "
                "call per qualifying visit. The 3,400 final calls average $250 "
                "in gross billable settlements; these rates are model inputs, "
                "not measured campaign results."
            ),
            (
                "100,000 visits × 10% × 50% × 80% × 85% = 3,400 settled calls. "
                "Gross settlements equal $850,000; the 55% retained share equals "
                "$467,500 before remaining modeled costs."
            ),
            [
                (
                    "Tracked paid visits",
                    "100,000 visits enter the same annual cohort",
                    100000.0,
                    (
                        "Count attributed landing-page visits after traffic-quality "
                        "filtering. Use a stable campaign identifier and defined "
                        "attribution window; do not mix impressions or repeat "
                        "telephone attempts into this visit count."
                    ),
                ),
                (
                    "Visits initiating calls",
                    "10,000 call starts; 10% of tracked visits",
                    10000.0,
                    (
                        "Count the first tracked call initiation associated with "
                        "each converting visit. A telephone-link click without an "
                        "actual call start does not enter this stage."
                    ),
                ),
                (
                    "Unique eligible inquiries",
                    "5,000 inquiries; 50% of call starts",
                    5000.0,
                    (
                        "Remove duplicates, wrong-service inquiries, out-of-area "
                        "callers, and inquiries lacking required routing permission. "
                        "Preserve exclusion reasons so source quality can be "
                        "reconciled with publisher invoices."
                    ),
                ),
                (
                    "Buyer-qualified connections",
                    "4,000 connections; 80% of eligible inquiries",
                    4000.0,
                    (
                        "Require buyer connection, contracted intent, and the "
                        "specified 90–120 second buffer. An AI transcript label "
                        "supports review but does not override buyer acceptance "
                        "terms or the actual call clock."
                    ),
                ),
                (
                    "Settled billable calls",
                    "3,400 calls; 85% of qualified connections",
                    3400.0,
                    (
                        "Exclude 600 rejected or reversed connections before "
                        "applying the $250 settlement average. The resulting "
                        "$850,000 is exchange settlement volume, not the value "
                        "of policies, repairs, legal matters, or client purchases."
                    ),
                ),
            ],
        ),
        (
            "diag-03-base-case-owner-profit-waterfall",
            "waterfall",
            "$850,000 gross settlements to $199,750 owner profit",
            "Six bars reconcile the 55% retained share and 23.5% gross-basis net margin.",
            3,
            "illustrative_model",
            (
                "The first and last bars are absolute totals; the four intermediate "
                "bars are signed deductions. Only the $382,500 acquisition deduction "
                "is fixed by the canonical 55% retained share; the remaining "
                "$267,750 is allocated illustratively. This model treats the quoted "
                "$2,500–$14,000 monthly opex band as recurring pod and platform "
                "overhead, with variable fulfillment separately funded. All-in "
                "post-acquisition costs average $22,312.50 monthly. If the quoted "
                "opex band were intended to include every such cost, it would not "
                "reconcile to the canonical Base Case."
            ),
            (
                "$850,000 − $382,500 − $99,750 − $108,000 − $60,000 = "
                "$199,750. Retained revenue is $467,500; owner profit is 23.5% "
                "of gross settlements and 42.73% of retained revenue. The 55% "
                "presentation is the supplied ASC 606 modeling convention; actual "
                "principal-versus-agent presentation depends on contract facts."
            ),
            [
                (
                    "Gross billable settlements",
                    "$850,000 annual exchange settlement total",
                    850000.0,
                    (
                        "Opening absolute total equals 3,400 settled calls at "
                        "$250 each. Keep this gross settlement basis separate "
                        "from the $467,500 retained-revenue presentation and from "
                        "any downstream buyer transaction value."
                    ),
                ),
                (
                    "Publisher and media acquisition",
                    "Subtract $382,500; retain $467,500 before other costs",
                    -382500.0,
                    (
                        "Publisher payouts plus click-to-call media consume 45% "
                        "of gross settlements. Attribute each acquisition cost "
                        "once; publisher-funded traffic must not also be charged "
                        "as directly purchased media."
                    ),
                ),
                (
                    "Variable call fulfillment",
                    "Subtract $99,750 in incremental transaction costs",
                    -99750.0,
                    (
                        "Illustrative allocation covers usage-based telephony, "
                        "metered evidence retrieval, outsourced call audits, and "
                        "transaction handling. Exclude acquisition spending and "
                        "fixed subscriptions already represented in other bars."
                    ),
                ),
                (
                    "Pod labor and contractors",
                    "Subtract $108,000 for one employee and two contractors",
                    -108000.0,
                    (
                        "Annual illustrative labor budget equals $9,000 monthly. "
                        "Treat the full-time seat as paid operating labor; owner "
                        "profit is the residual after this budget, not a substitute "
                        "for recording labor expense."
                    ),
                ),
                (
                    "Fixed platform and administration",
                    "Subtract $60,000 in annual recurring overhead",
                    -60000.0,
                    (
                        "Budget $5,000 monthly for fixed software commitments, "
                        "accounting, insurance, and administration. Combined with "
                        "labor, recurring overhead reaches $14,000 monthly; variable "
                        "fulfillment remains a separate waterfall deduction."
                    ),
                ),
                (
                    "Annual owner net profit",
                    "$199,750 residual after all four modeled deductions",
                    199750.0,
                    (
                        "Closing absolute total is the canonical Base Case. "
                        "Conservative remains $200,000 gross, $110,000 retained, "
                        "and $30,000 profit at 15% gross margin and 27.27% retained "
                        "margin. Scaled remains $1,500,000 gross, $825,000 retained, "
                        "and $480,000 profit at 32% and 58.18%, respectively."
                    ),
                ),
            ],
        ),
        (
            "diag-04-subniche-retained-yield-comparison",
            "horizontal_bars",
            "Compare retained dollars per settled call",
            "Five illustrative sub-niche yields use the same 55% retained-share assumption.",
            2,
            "illustrative_model",
            (
                "Bar lengths measure retained dollars per settled call before "
                "fulfillment, pod labor, and fixed overhead. Gross call prices are "
                "illustrative contract inputs, not observed market quotes. These "
                "alternatives are not an additive portfolio and do not alter the "
                "Base-Case blended $250 gross settlement assumption."
            ),
            (
                "Higher nominal yield can conceal longer collection cycles, "
                "tighter statutory restrictions, or worse rejection rates. Compare "
                "realized contribution per acquired inquiry before reallocating spend."
            ),
            [
                (
                    "Emergency plumbing dispatch",
                    "$110 retained from a $200 settled call",
                    110.0,
                    (
                        "$200 × 55% = $110 before remaining costs. Require live "
                        "service-area coverage, a working dispatch endpoint, and "
                        "documented buyer acceptance; an unanswered emergency "
                        "transfer cannot be counted as a completed job."
                    ),
                ),
                (
                    "Personal insurance inquiry",
                    "$137.50 retained from a $250 settled call",
                    137.5,
                    (
                        "$250 × 55% = $137.50 before remaining costs. Match "
                        "state and product eligibility to the licensed buyer; "
                        "record recipient-specific permission where required and "
                        "reject duplicates under the signed lookback window."
                    ),
                ),
                (
                    "Commercial insurance inquiry",
                    "$165 retained from a $300 settled call",
                    165.0,
                    (
                        "$300 × 55% = $165 before remaining costs. Capture "
                        "business class and coverage intent without collecting "
                        "unnecessary sensitive information; reconcile buyer staffing "
                        "hours and acceptance criteria before buying traffic."
                    ),
                ),
                (
                    "Water-restoration dispatch",
                    "$192.50 retained from a $350 settled call",
                    192.5,
                    (
                        "$350 × 55% = $192.50 before remaining costs. Verify "
                        "incident location, actual dispatch availability, and "
                        "service intent; do not equate the call price with "
                        "restoration contract value or insurance proceeds."
                    ),
                ),
                (
                    "Permitted legal advertising inquiry",
                    "$220 retained from a $400 settled call",
                    220.0,
                    (
                        "$400 × 55% = $220 before remaining costs. Activate "
                        "only where the precise advertising arrangement is permitted "
                        "under applicable state rules; check California Rules of "
                        "Professional Conduct 7.2 and Business and Professions "
                        "Code sections 6151–6153 for relevant California activity. "
                        "A fixed call price alone does not establish permissibility."
                    ),
                ),
            ],
        ),
        (
            "diag-05-preflight-contact-and-counterparty-tree",
            "decision_tree",
            "Four checks before traffic is purchased",
            "Pass each check in sequence; a failed branch stops the affected route.",
            5,
            "operating_framework",
            (
                "Numeric values encode ordered check positions, not risk scores. "
                "The FCC's 2023 one-to-one consent amendment was vacated in "
                "Insurance Marketing Coalition Ltd. v. FCC, 127 F.4th 303 "
                "(11th Cir. 2025); do not present it as an operative universal "
                "FCC mandate. Recipient-specific evidence remains a useful "
                "contractual control. Confirm current rule text and controlling "
                "decisions before activating a jurisdiction or product."
            ),
            (
                "Pass proceeds to the next check; failure disables the relevant "
                "campaign or recipient until the specified defect is corrected. "
                "Commercial risk checks supplement statutory requirements."
            ),
            [
                (
                    "Contact method and permission",
                    "Pass to Medicare scope; fail to contact redesign",
                    1.0,
                    (
                        "Classify consumer-initiated inbound activity, transfers, "
                        "and outbound follow-up separately under 47 U.S.C. 227, "
                        "47 CFR 64.1200, and applicable 16 CFR Part 310 provisions. "
                        "Apply written-consent requirements where triggered. "
                        "Refresh DNC suppression as required, including the "
                        "applicable 31-day National Registry update interval, "
                        "and check entity-specific suppression before outbound contact."
                    ),
                ),
                (
                    "Medicare marketing requirements",
                    "Pass to state restrictions; fail to appointment repair",
                    2.0,
                    (
                        "For Medicare activity, apply 42 CFR 422.2264 and "
                        "423.2264 scope-of-appointment timing, including the "
                        "48-hour rule and its actual exceptions. Apply TPMO "
                        "marketing, sales, and enrollment call-recording rules "
                        "under 422.2274 and 423.2274, plus applicable individual "
                        "TPMO information-sharing permission requirements. "
                        "Non-Medicare routes proceed without importing these rules."
                    ),
                ),
                (
                    "State recording and legal advertising",
                    "Pass to buyer risk; fail to route exclusion",
                    3.0,
                    (
                        "Map caller and recipient jurisdictions before recording; "
                        "California Penal Code section 632 addresses confidential "
                        "communications. For legal inquiries, examine applicable "
                        "state advertising, solicitation, referral-payment, and "
                        "runner restrictions, including California Business and "
                        "Professions Code sections 6151–6153 when relevant. "
                        "Exclude arrangements that fail the governing rules."
                    ),
                ),
                (
                    "Buyer collectability and acquisition risk",
                    "Pass to capped traffic; fail to funding repair",
                    4.0,
                    (
                        "Document the connected-time clock, rejection reasons, "
                        "dispute window, credit exposure, and actual net-7 "
                        "collections. Set CPC and publisher exposure limits from "
                        "realized contribution, not headline bids. At Base Case, "
                        "a 10% acquisition-cost increase with everything else "
                        "fixed removes $38,250 and reduces profit to $161,500."
                    ),
                ),
            ],
        ),
        (
            "diag-06-three-to-five-person-operating-pod",
            "org_architecture",
            "Three core seats, two scaled additions",
            "Base pod is 1 FT + 2 C; scaled pod is 2 FT + 3 C.",
            11,
            "operating_framework",
            (
                "Each numeric value represents one person in the five-person "
                "scaled configuration, not one full-time equivalent. The first "
                "three seats form the Conservative and Base pods. The final two "
                "seats are scaled additions; contractor hours are scoped separately."
            ),
            (
                "Automation handles routing, evidence indexing, and S2S corrections. "
                "Named people still own spend limits, buyer disputes, recording "
                "exceptions, and bank reconciliation."
            ),
            [
                (
                    "Exchange operator — core full-time",
                    "Own buyers, cash exposure, and daily contribution",
                    1.0,
                    (
                        "Own signed buyer terms, Ringba or Retreaver routing "
                        "configuration, publisher caps, and daily cash exposure. "
                        "Reconcile settled-call contribution with invoices before "
                        "increasing media budgets or buyer credit limits."
                    ),
                ),
                (
                    "Acquisition specialist — core contractor",
                    "Own search campaigns, landing pages, and source controls",
                    1.0,
                    (
                        "Manage Google Ads search terms, geographic targeting, "
                        "negative keywords, landing-page versions, and S2S "
                        "conversion corrections. Diagnose CPC spikes using settled "
                        "cohorts rather than optimizing toward raw call starts."
                    ),
                ),
                (
                    "Evidence and reconciliation specialist — core contractor",
                    "Own call audits, evidence retrieval, and dispute packets",
                    1.0,
                    (
                        "Sample AI transcript dispositions, retrieve TrustedForm "
                        "or Jornaya evidence where used, and reconcile duration "
                        "scrubs. Assemble timestamped dispute packets and match "
                        "buyer receipts to the settlement ledger."
                    ),
                ),
                (
                    "Buyer operations manager — scaled full-time",
                    "Add live capacity management and counterparty coverage",
                    1.0,
                    (
                        "Add this second full-time seat in the five-person scaled "
                        "configuration. Maintain buyer schedules, backup routes, "
                        "concentration limits, and collections follow-up while "
                        "the operator retains portfolio-level spend authority."
                    ),
                ),
                (
                    "Automation engineer — scaled contractor",
                    "Add routing tests, event reliability, and audit exports",
                    1.0,
                    (
                        "Add this third contractor in the scaled configuration. "
                        "Test bid timeouts, webhook retries, idempotent postbacks, "
                        "access controls, and evidence exports; prevent duplicate "
                        "billing when asynchronous events arrive out of order."
                    ),
                ),
            ],
        ),
        (
            "diag-07-startup-capital-allocation",
            "stacked_comparison",
            "Allocate startup cash before buying volume",
            "Four buckets total $8,000 lean, $30,000 working, or $45,000 expanded.",
            4,
            "illustrative_model",
            (
                "Numeric values display the $30,000 working plan. Each detail "
                "also states its lean and expanded allocations. Lean allocations "
                "sum to $8,000; expanded allocations sum to $45,000. These are "
                "startup cash allocations, not annual expense deductions or "
                "additional revenue."
            ),
            (
                "Do not count an unspent reserve as an expense. Release test "
                "capital in small cohorts, and resize settlement float using "
                "observed buyer collections rather than invoice due dates alone."
            ),
            [
                (
                    "Routing and evidence setup",
                    "$3,500 working allocation for initial systems",
                    3500.0,
                    (
                        "Lean $1,000; working $3,500; expanded $5,000. Fund "
                        "telephone numbers, initial Ringba or Retreaver configuration, "
                        "evidence integration, landing-page instrumentation, and "
                        "test-call fixtures before connecting paid traffic."
                    ),
                ),
                (
                    "Contracts and operating setup",
                    "$4,500 working allocation for documented counterparties",
                    4500.0,
                    (
                        "Lean $1,000; working $4,500; expanded $7,000. Fund "
                        "buyer and publisher contract work, jurisdiction-specific "
                        "advertising review, accounting setup, recording procedures, "
                        "and written acceptance and dispute definitions."
                    ),
                ),
                (
                    "Controlled acquisition experiments",
                    "$14,000 working allocation for measured traffic cohorts",
                    14000.0,
                    (
                        "Lean $4,000; working $14,000; expanded $21,000. Release "
                        "media or publisher test spending in capped increments. "
                        "Stop a source when realized contribution or evidence "
                        "quality breaches its documented operating threshold."
                    ),
                ),
                (
                    "Settlement float and contingency",
                    "$8,000 working allocation for timing and reversals",
                    8000.0,
                    (
                        "Lean $2,000; working $8,000; expanded $12,000. Reserve "
                        "cash for prepaid acquisition, buyer payment delays, and "
                        "reversals. Base acquisition averages about $1,047.95 "
                        "daily; seven days consumes about $7,335.62 before "
                        "other obligations, making an $8,000 reserve tight."
                    ),
                ),
            ],
        ),
        (
            "diag-08-thirty-day-controlled-launch",
            "timeline_roadmap",
            "Thirty days to an instrumented operating pilot",
            "Four milestones prepare the exchange; first-deal planning remains one to three months.",
            12,
            "operating_framework",
            (
                "Numeric values mark milestone end days. This sprint establishes "
                "buyer terms, tested routing, capped experiments, and reconciliation. "
                "It does not assume a buyer payment or profitable campaign will "
                "arrive within the first 30 days."
            ),
            (
                "Increase exposure only after the evidence, contribution, and "
                "collection record supports it. Carry unfinished buyer contracting "
                "or collection work into the stated one-to-three-month deal window."
            ),
            [
                (
                    "Days 1-7",
                    "Define one niche and executable buyer terms",
                    7.0,
                    (
                        "Choose one jurisdiction and service category. Document "
                        "call price, connected-time definition, duplicate window, "
                        "rejection reasons, payment timing, and recording duties. "
                        "Complete the four pre-flight checks and assign a named "
                        "owner to each operating control."
                    ),
                ),
                (
                    "Days 8-14",
                    "Prove routing and evidence with authorized test calls",
                    14.0,
                    (
                        "Configure Ringba or Retreaver buyer caps and fallback "
                        "paths. Test no-bid, timeout, disconnect, duplicate-event, "
                        "and webhook-retry cases. Verify evidence retrieval and "
                        "recording access without sending test conversions into "
                        "production bid optimization."
                    ),
                ),
                (
                    "Days 15-21",
                    "Run capped cohorts and inspect every disputed call",
                    21.0,
                    (
                        "Release a limited acquisition tranche after buyer "
                        "contracting is complete. Compare source cost, connected "
                        "duration, buyer acceptance, and evidence completeness. "
                        "Reconcile S2S values to accepted calls; pause faulty "
                        "routes rather than padding call duration."
                    ),
                ),
                (
                    "Days 22-30",
                    "Close the first reconciliation and set the next exposure cap",
                    30.0,
                    (
                        "Match call records, buyer statements, publisher invoices, "
                        "and any received payments. Separate billed amounts from "
                        "cash collected. If net-7 collectability remains unproven, "
                        "retain pilot caps and extend observation instead of "
                        "treating an unpaid invoice as validated demand."
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
