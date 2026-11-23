from __future__ import annotations

VOLUME_038_SUBTITLE = (
    "The Complete Playbook for Contingent Corporate Bill-Audit & Tax-Credit "
    "Recovery: $110,000-$900,000 USD in Annual Operator Revenue, "
    "a 1 FT + 3 C (4 People) Core Pod, and a Six-Person Scaled Model"
)

VOLUME_038_POSITIONING_ALTERNATIVES = [
    {
        "title": "The Corporate Overpayment Recovery Desk",
        "subtitle": (
            "Recover documented parcel, utility, waste, and telecom overpayments "
            "through authorized invoice audits and contract-permitted "
            "25%-50% recovery shares."
        ),
        "audience": (
            "Procurement analysts and expense-audit operators serving "
            "multi-location employers with recurring, reconcilable vendor bills."
        ),
        "research_basis": (
            "Invoice-level evidence, written authority, and enforceable fee "
            "terms support a repeatable recovery service. Electronic agreements "
            "have a federal statutory framework under 15 U.S.C. 7001, but "
            "signature validity does not establish refund eligibility. Carrier "
            "service guarantees, contractual waivers, filing windows, utility "
            "tariffs, and municipal refund procedures must be checked separately."
        ),
        "sources": [
            "https://www.law.cornell.edu/uscode/text/15/7001",
            "https://www.eia.gov/tools/faqs/faq.php?id=97&t=3",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Evidence-First Property Assessment Desk",
        "subtitle": (
            "Build assessment-appeal files from valuation evidence and pursue "
            "licensed, deadline-controlled recovery engagements."
        ),
        "audience": (
            "Property-tax consultants and commercial-property analysts with "
            "jurisdiction-specific credentials and access to valuation records."
        ),
        "research_basis": (
            "Texas Occupations Code Chapter 1152 establishes property-tax "
            "consultant registration requirements and exemptions. Texas Tax "
            "Code Sections 41.41 and 41.44 identify protest rights and filing "
            "requirements. These authorities support a Texas-specific operating "
            "design, not an assumption that other states use identical rules."
        ),
        "sources": [
            "https://statutes.capitol.texas.gov/Docs/OC/htm/OC.1152.htm",
            "https://statutes.capitol.texas.gov/Docs/TX/htm/TX.41.htm",
            "https://www.tdlr.texas.gov/ptc/ptc.htm",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Employer Credit Documentation Desk",
        "subtitle": (
            "Connect ATS intake, Form 8850 timing, state certification, and "
            "substantiated employer-credit files using separately scoped fees."
        ),
        "audience": (
            "Employer-service operators working with qualified tax practitioners "
            "and employers whose hiring records support credit eligibility."
        ),
        "research_basis": (
            "26 U.S.C. 51(d)(13) establishes WOTC certification and prescreening "
            "requirements, including the applicable 28-day submission deadline. "
            "Section 51(c)(4) makes hire-date statutory authorization a separate "
            "check. Treasury Circular 230, 31 CFR 10.27, requires a "
            "matter-specific fee review; an expense-recovery percentage must "
            "not automatically become a federal tax-credit fee."
        ),
        "sources": [
            "https://www.law.cornell.edu/uscode/text/26/51",
            "https://www.irs.gov/forms-pubs/about-form-8850",
            "https://www.ecfr.gov/current/title-31/subtitle-A/part-10/section-10.27",
            "https://www.law.cornell.edu/uscode/text/26/7216",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
]


def build_volume_038_diagrams_data() -> list[dict]:
    specs = [
        (
            "diag-01-authorized-recovery-workflow",
            "process_flow",
            "From Signed Authority to Earned Recovery Fees",
            "Five evidence-controlled stages for expense and tax-credit work",
            1,
            "operating_framework",
            (
                "Expense-recovery shares of 25%-50% apply only where permitted "
                "and contractually agreed. Federal tax work receives a separate "
                "scope and fee review. Client refunds, vendor bills, property "
                "values, and tax credits are not operator revenue."
            ),
            (
                "Preserve the original evidence before proposing corrections. "
                "A refund request is neither an issued refund nor an earned fee."
            ),
            [
                (
                    "Authorize and preserve",
                    "Signed authority plus immutable baseline",
                    1.0,
                    (
                        "Obtain a signed Letter of Authorization and fee "
                        "agreement before disclosing tariff or refund findings. "
                        "Snapshot invoices, payment records, carrier contracts, "
                        "meter identifiers, assessment notices, and relevant "
                        "employment records with timestamps and file hashes."
                    ),
                ),
                (
                    "Extract and normalize",
                    "One traceable ledger per client",
                    2.0,
                    (
                        "Import FedEx and UPS EDI exports or permitted API "
                        "records; use OCR for utility tariffs and cooling-tower "
                        "meter evidence. Normalize account, invoice, service "
                        "date, charge code, and payment status while retaining "
                        "links to original documents."
                    ),
                ),
                (
                    "Validate entitlement",
                    "Documented rule and recoverable amount",
                    3.0,
                    (
                        "Check service-guarantee waivers, tariff effective "
                        "dates, appeal deadlines, duplicate claims, and prior "
                        "credits. For WOTC, verify statutory hire-date coverage, "
                        "prescreening, certification timing, and substantiation "
                        "before including a case in the recoverable pipeline."
                    ),
                ),
                (
                    "Submit through authorized channels",
                    "Accepted submission with receipt evidence",
                    4.0,
                    (
                        "Use carrier-supported claim routes, utility refund "
                        "procedures, licensed property-tax representation, or "
                        "state workforce agency channels as applicable. Store "
                        "submission identifiers and response deadlines; route "
                        "rejections to a documented exception queue."
                    ),
                ),
                (
                    "Reconcile and earn",
                    "Verified benefit matched to contract",
                    5.0,
                    (
                        "Match issued refunds or realized savings to bank, "
                        "vendor-credit, or billing evidence. Recognize only "
                        "earned operator fees under the contract. For 36-month "
                        "shared-savings arrangements, reconcile each period "
                        "against a volume-adjusted baseline rather than booking "
                        "all future savings immediately."
                    ),
                ),
            ],
        ),
        (
            "diag-02-nested-annual-recovery-cohort",
            "funnel",
            "A Nested Cohort Behind the Base Revenue Target",
            "250 screened prospects become 25 earned-and-collected engagements",
            6,
            "illustrative_model",
            (
                "Illustrative mature annual cohort, not measured conversion "
                "performance or a first-month forecast. Every downstream group "
                "is a subset of the preceding group. Twenty-five engagements "
                "at $20,200 average annual earned operator fees reconcile to "
                "$505,000 Base revenue; the average is a modeling input."
            ),
            (
                "Stage conversions are 40.0%, 60.0%, 66.7%, and 62.5%; overall "
                "conversion is 10.0%. Pending cases remain outside the final "
                "earned-and-collected cohort."
            ),
            [
                (
                    "Screened corporate prospects",
                    "250 organizations with auditable recurring spend",
                    250.0,
                    (
                        "Identify organizations with accessible invoice "
                        "history, a responsible account owner, and a plausible "
                        "recovery lane. Exclude accounts already bound by "
                        "conflicting recovery engagements before outreach."
                    ),
                ),
                (
                    "Authorized client engagements",
                    "100 signed engagements from those prospects",
                    100.0,
                    (
                        "Forty percent of screened prospects execute authority "
                        "and scope documents and provide baseline records. "
                        "A verbal expression of interest does not count "
                        "as an authorized engagement."
                    ),
                ),
                (
                    "Evidence-qualified recovery cases",
                    "60 engagements with documented eligible opportunities",
                    60.0,
                    (
                        "Sixty percent of authorized engagements survive "
                        "contract, deadline, statutory, and evidence checks. "
                        "Remove duplicate recoveries, unsupported estimates, "
                        "and claims barred by applicable waivers."
                    ),
                ),
                (
                    "Accepted recovery submissions",
                    "40 engagements reach accepted filing channels",
                    40.0,
                    (
                        "Two-thirds of qualified engagements obtain submission "
                        "receipts or accepted processing records. Count client "
                        "engagements consistently rather than inflating this "
                        "stage with multiple invoices from one client."
                    ),
                ),
                (
                    "Earned and collected engagements",
                    "25 engagements generate $505,000 operator revenue",
                    25.0,
                    (
                        "Twenty-five engagements meet earning conditions and "
                        "collection assumptions within the modeled year. "
                        "$505,000 divided by 25 equals $20,200 per engagement; "
                        "this is operator fee revenue, not client recovery "
                        "principal or total underlying vendor expenditure."
                    ),
                ),
            ],
        ),
        (
            "diag-03-base-owner-profit-waterfall",
            "waterfall",
            "Base Revenue to $217,150 Owner Profit",
            "$505,000 less $287,850 modeled expenses equals a 43.0% net margin",
            3,
            "illustrative_model",
            (
                "Formula v2.0 Base revenue, margin, and owner profit are "
                "canonical. The four expense allocations are illustrative "
                "because the supplied scorecard does not itemize costs. "
                "First and last bars are totals; the intervening bars are "
                "negative changes. Gross means gross operator fee revenue, "
                "not gross client refund receipts."
            ),
            (
                "Reconciliation: $505,000 - $145,000 - $40,850 - $60,000 "
                "- $42,000 = $217,150; $217,150 / $505,000 = 43.0%. "
                "Conservative remains $110,000 at 30% = $33,000; Scaled "
                "remains $900,000 at 56% = $504,000."
            ),
            [
                (
                    "Earned operator fee revenue",
                    "$505,000 annual Base revenue",
                    505000.0,
                    (
                        "Include earned contingency shares, earned portions "
                        "of 36-month shared-savings agreements, and completed "
                        "WOTC processing fees. Apply ASC 606 principal-agent "
                        "analysis to the actual arrangement; client benefits "
                        "are never automatically operator billings."
                    ),
                ),
                (
                    "Pod delivery labor",
                    "Subtract $145,000 allocated annual labor",
                    -145000.0,
                    (
                        "Illustratively allocate $145,000 to employee "
                        "compensation and contractor delivery across the "
                        "1 FT plus 3 C pod. The resulting owner-profit figure "
                        "is the residual after this modeled labor charge, "
                        "not a separate estimate of owner compensation."
                    ),
                ),
                (
                    "Variable case execution",
                    "Subtract $40,850 case-linked operating costs",
                    -40850.0,
                    (
                        "Illustratively allocate case-specific records, "
                        "permitted filing charges, incremental extraction "
                        "services, and recovery processing costs here. "
                        "Exclude contractor labor already charged to the "
                        "preceding bar to prevent double counting."
                    ),
                ),
                (
                    "Commercial and administrative overhead",
                    "Subtract $60,000 annual commercial overhead",
                    -60000.0,
                    (
                        "Illustratively allocate acquisition, insurance, "
                        "bookkeeping, and general administration to a "
                        "$5,000 monthly fixed-cost budget. Track acquisition "
                        "cost per signed engagement rather than per "
                        "unqualified lead."
                    ),
                ),
                (
                    "Platform and secure operations",
                    "Subtract $42,000 annual platform overhead",
                    -42000.0,
                    (
                        "Illustratively allocate $3,500 monthly to OCR, "
                        "permitted integrations, secure storage, access "
                        "management, and monitoring. Combined fixed overhead "
                        "is $8,500 monthly, within the stated $1,500-$9,500 "
                        "range; this allocation excludes the delivery and "
                        "variable costs shown separately."
                    ),
                ),
                (
                    "Annual owner net profit",
                    "$217,150 retained annual operating residual",
                    217150.0,
                    (
                        "The endpoint is a total, not another additive "
                        "movement. Total modeled expenses are $287,850, "
                        "leaving exactly 43.0% of Base operator revenue. "
                        "Owner-level personal taxes and distribution timing "
                        "are outside this supplied scenario."
                    ),
                ),
            ],
        ),
        (
            "diag-04-recovery-lane-fee-yields",
            "horizontal_bars",
            "Five Recovery Lanes and Their Operator Fee Math",
            "Illustrative contract yields, not measured niche performance",
            2,
            "illustrative_model",
            (
                "The first four bars each assume $100,000 of independently "
                "verified, realized client recovery and a permitted expense "
                "contingency rate. The fifth assumes 120 completed WOTC "
                "administrative packages at a fixed $250 fee. Denominators "
                "differ deliberately; bars are fee-dollar examples, not a "
                "ranking of expected return or a Base revenue decomposition."
            ),
            (
                "Parcel $50,000; utility $35,000; waste and telecom $30,000; "
                "property assessment $25,000; WOTC processing $30,000. "
                "Client recoveries and tax-credit amounts remain outside "
                "operator revenue."
            ),
            [
                (
                    "Parcel service and billing recoveries",
                    "$100,000 realized recovery multiplied by 50%",
                    50000.0,
                    (
                        "Earn $50,000 only where the signed agreement supports "
                        "a 50% share and the carrier accepts the underlying "
                        "claim. Check FedEx or UPS guarantee availability, "
                        "waivers, eligible services, submission windows, and "
                        "API terms before automation."
                    ),
                ),
                (
                    "Commercial utility tariff recoveries",
                    "$100,000 realized recovery multiplied by 35%",
                    35000.0,
                    (
                        "Earn $35,000 on documented recoveries from applicable "
                        "rate classifications, meter errors, or eligible "
                        "sewer deductions. Match cooling-tower meter evidence "
                        "to local rules and distinguish slow refund issuance "
                        "from an approved adjustment."
                    ),
                ),
                (
                    "Waste and telecom billing recoveries",
                    "$100,000 realized recovery multiplied by 30%",
                    30000.0,
                    (
                        "Earn $30,000 from supported duplicate charges, "
                        "disconnected services, or contractual rate errors. "
                        "Separate refunded historical charges from future "
                        "savings, and prevent the same correction from "
                        "generating two overlapping fee claims."
                    ),
                ),
                (
                    "Property assessment recoveries",
                    "$100,000 realized recovery multiplied by 25%",
                    25000.0,
                    (
                        "Earn $25,000 only under a permitted engagement "
                        "handled by appropriately credentialed personnel. "
                        "Track protest and payment deadlines independently; "
                        "a reduced assessment does not itself establish "
                        "a received cash refund."
                    ),
                ),
                (
                    "WOTC administrative processing",
                    "120 completed packages multiplied by $250",
                    30000.0,
                    (
                        "Earn $30,000 from separately scoped administrative "
                        "deliverables, not a percentage of federal tax "
                        "credits. Verify hire-date statutory coverage and "
                        "Form 8850 timing. Fixed pricing does not remove "
                        "practitioner, privacy, or substantiation requirements."
                    ),
                ),
            ],
        ),
        (
            "diag-05-statutory-and-contract-preflight",
            "decision_tree",
            "Four Checks Before a Recovery Submission",
            "Each failed check routes to remediation or a declined claim",
            5,
            "operating_framework",
            (
                "Apply every relevant branch to the engagement; branches "
                "describe operating checks, not a probability model. "
                "Federal tax fee rules, state representation rules, and "
                "private carrier terms address different obligations."
            ),
            (
                "Submit only after authority, contractual eligibility, "
                "tax scope, and jurisdictional credentials are resolved. "
                "Preserve the evidence supporting each decision."
            ),
            [
                (
                    "Authority and permitted information use",
                    "Proceed with documented authority and valid access",
                    1.0,
                    (
                        "Require signed authority, baseline invoice snapshots, "
                        "and least-privilege access. Where tax-return preparer "
                        "information rules apply, evaluate 26 U.S.C. 7216 and "
                        "26 CFR 301.7216-3; a generic Letter of Authorization "
                        "does not replace any required disclosure or use "
                        "consent. Otherwise obtain missing permissions first."
                    ),
                ),
                (
                    "Carrier and vendor recovery entitlement",
                    "Proceed only for eligible timely claims",
                    2.0,
                    (
                        "Inspect actual carrier guarantee waivers, service "
                        "exclusions, filing deadlines, prior credits, and "
                        "authorized API use. For utilities, retain the "
                        "controlling tariff and effective date. If entitlement "
                        "fails, remove the claim rather than bypassing a "
                        "carrier restriction or manufacturing a billing error."
                    ),
                ),
                (
                    "Federal tax scope and substantiation",
                    "Proceed with supported eligibility and permitted fees",
                    3.0,
                    (
                        "Have a qualified practitioner assess 31 CFR 10.27 "
                        "as applicable to the specific service, including "
                        "exceptions and relevant judicial limitations. "
                        "For WOTC, verify 26 U.S.C. 51(c)(4) hire-date coverage "
                        "and 51(d)(13) certification requirements; where "
                        "prescreening applies, complete it by the offer date "
                        "and submit within 28 days after work begins."
                    ),
                ),
                (
                    "State credentials and appeal calendar",
                    "Proceed through properly credentialed representation",
                    4.0,
                    (
                        "Check state property-tax consultant rules, permissible "
                        "fee terms, and local appeal procedures. In Texas, "
                        "review Occupations Code Chapter 1152 and Tax Code "
                        "41.44, including applicable exceptions and actual "
                        "notice dates. If credentials or deadlines fail, "
                        "refer appropriately or decline the affected matter."
                    ),
                ),
            ],
        ),
        (
            "diag-06-core-and-scaled-pod",
            "org_architecture",
            "Four Core Seats, Six at Scaled Throughput",
            "Base 1 FT + 3 C; Scaled 2 FT + 4 C",
            11,
            "operating_framework",
            (
                "Numeric values show the four Base seats, one per role. "
                "The Scaled model adds one full-time operations seat and "
                "one contract audit seat. Contractor counts describe people, "
                "not full-time equivalents or unlimited specialist capacity."
            ),
            (
                "Conservative and Base use four people; Scaled uses six. "
                "Credential-sensitive work stays with personnel qualified "
                "for that jurisdiction and service."
            ),
            [
                (
                    "Owner and client operations",
                    "Base one FT; Scaled two FT",
                    1.0,
                    (
                        "The owner controls sales, authority documents, "
                        "pricing, cash collection, and client reporting. "
                        "At Scaled volume, add a full-time operations lead "
                        "for queue ownership and reconciliation; retain "
                        "separate review of fee calculations and receipts."
                    ),
                ),
                (
                    "Parcel and invoice audit delivery",
                    "Base one contractor; Scaled two contractors",
                    1.0,
                    (
                        "Audit analysts reconcile EDI and permitted API "
                        "records, preserve invoice lineage, test duplicates, "
                        "and prepare supported claims. The second Scaled "
                        "analyst increases throughput without sharing "
                        "client credentials or bypassing rate limits."
                    ),
                ),
                (
                    "Utility and property specialist",
                    "One contractor in both operating scenarios",
                    1.0,
                    (
                        "A vetted specialist owns tariff interpretation, "
                        "meter evidence, and property-assessment analysis "
                        "within their demonstrated qualifications. Accept "
                        "representation work only where this seat holds "
                        "required credentials; otherwise narrow that "
                        "engagement rather than inventing coverage."
                    ),
                ),
                (
                    "Tax-credit documentation specialist",
                    "One contractor in both operating scenarios",
                    1.0,
                    (
                        "A qualified specialist controls WOTC prescreening "
                        "timing, state certification evidence, secure records, "
                        "and coordination with the employer's tax preparer. "
                        "Separate administrative processing from tax-return "
                        "services and maintain the required fee review."
                    ),
                ),
            ],
        ),
        (
            "diag-07-startup-capital-allocation",
            "stacked_comparison",
            "Four Buckets Inside the Startup Capital Range",
            "$6,000 lean launch; $20,000 reference launch; $35,000 expanded launch",
            4,
            "illustrative_model",
            (
                "Numeric values represent the $20,000 reference launch. "
                "The same 30%, 25%, 25%, and 20% allocations produce the "
                "$6,000 and $35,000 endpoints. Startup allocations are "
                "illustrative, exclude client recovery principal, and "
                "do not establish that every jurisdiction or software "
                "contract fits the lean budget."
            ),
            (
                "Lean allocations total $1,800 + $1,500 + $1,500 + $1,200 "
                "= $6,000. Reference allocations total $20,000. Expanded "
                "allocations total $10,500 + $8,750 + $8,750 + $7,000 "
                "= $35,000."
            ),
            [
                (
                    "Secure tooling and integrations",
                    "$6,000 reference; $1,800 lean; $10,500 expanded",
                    6000.0,
                    (
                        "Allocate 30% to initial OCR configuration, encrypted "
                        "document storage, password management, access "
                        "controls, and permitted carrier integrations. "
                        "Prefer supported exports before paying to automate "
                        "an unvalidated claim lane."
                    ),
                ),
                (
                    "Credentials and engagement design",
                    "$5,000 reference; $1,500 lean; $8,750 expanded",
                    5000.0,
                    (
                        "Allocate 25% to required registrations, initial "
                        "professional review, engagement documents, "
                        "insurance setup, and jurisdiction-specific scope "
                        "design. If local requirements exceed this bucket, "
                        "reduce launch geography or increase funded capital."
                    ),
                ),
                (
                    "Prospecting and pilot onboarding",
                    "$5,000 reference; $1,500 lean; $8,750 expanded",
                    5000.0,
                    (
                        "Allocate 25% to targeted account research, direct "
                        "outreach, client intake, and initial evidence "
                        "normalization. Measure signed, document-ready "
                        "engagements rather than purchased contact volume "
                        "or unverified recovery estimates."
                    ),
                ),
                (
                    "Liquidity and collection buffer",
                    "$4,000 reference; $1,200 lean; $7,000 expanded",
                    4000.0,
                    (
                        "Allocate 20% to delayed collections and operating "
                        "variance. The reference $4,000 covers about "
                        "2.7 months at $1,500 monthly overhead or 0.4 months "
                        "at $9,500; it does not fund the full pod or "
                        "automatically cover the 1-4 month first-deal window."
                    ),
                ),
            ],
        ),
        (
            "diag-08-thirty-day-launch-sprint",
            "timeline_roadmap",
            "A Thirty-Day Evidence-to-Submission Sprint",
            "Build an authorized pilot before expanding claim volume",
            12,
            "operating_framework",
            (
                "Milestones are operator-controlled launch deliverables, "
                "not promised refund dates. The canonical time to first "
                "deal is 1-4 months; municipal refunds, assessment appeals, "
                "and tax-credit certification can take longer than this "
                "sprint."
            ),
            (
                "Finish the month with traceable pilot evidence, tested "
                "fee math, and a documented submission or a specific "
                "remediation plan; do not substitute projected recoveries "
                "for collected revenue."
            ),
            [
                (
                    "Days 1-7",
                    "Define one lane and secure the workspace",
                    7.0,
                    (
                        "Choose one customer profile and recovery lane. "
                        "Review applicable contract terms, tax-service scope, "
                        "or state credentials; prepare authority and fee "
                        "documents. Configure encrypted storage, individual "
                        "accounts, access logging, and a deadline register."
                    ),
                ),
                (
                    "Days 8-14",
                    "Secure a pilot and preserve baseline evidence",
                    14.0,
                    (
                        "Conduct targeted outreach and seek one authorized "
                        "pilot. After signature, obtain invoice and payment "
                        "records and preserve their original versions. "
                        "If no pilot signs, continue acquisition and test "
                        "the workflow with synthetic records without "
                        "claiming client access or recoveries."
                    ),
                ),
                (
                    "Days 15-21",
                    "Validate exceptions and calculate the fee basis",
                    21.0,
                    (
                        "Reconcile extracted records against source "
                        "documents, remove duplicates, test eligibility, "
                        "and calculate supported claim amounts. Review "
                        "waivers, tariff periods, credentials, or WOTC "
                        "timing as applicable. Have a second qualified "
                        "reviewer inspect material exceptions."
                    ),
                ),
                (
                    "Days 22-30",
                    "Submit supported claims and establish reconciliation",
                    30.0,
                    (
                        "Submit only authorized, eligible pilot matters and "
                        "store acceptance receipts. If evidence remains "
                        "incomplete, issue a dated remediation list instead. "
                        "Build refund-to-invoice matching, aging reports, "
                        "shared-savings baseline checks, and a fee ledger "
                        "that separates pending value from earned revenue."
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
