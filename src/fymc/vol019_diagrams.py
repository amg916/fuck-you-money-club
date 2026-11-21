from __future__ import annotations

VOLUME_019_SUBTITLE = (
    "The Complete Playbook for Enterprise Software Reselling: "
    "$300,000–$2,500,000 USD in Annual Gross License and Service Billings, "
    "Starting with a 2 FT + 3 C Five-Person Pod"
)

VOLUME_019_POSITIONING_ALTERNATIVES = [
    {
        "title": "The Private-Offer Reseller",
        "subtitle": (
            "Build an authorized enterprise software channel around AWS "
            "Marketplace CPPO, Microsoft CSP, deal registration, and paid implementation."
        ),
        "audience": (
            "Vendor-certified sellers and implementation specialists building a "
            "five-person pod with disciplined vendor commitments and collection terms."
        ),
        "research_basis": (
            "Copyright permissions and export scope create concrete diligence "
            "requirements for software distribution. Marketplace participation, "
            "resale rights, discounts, and settlement mechanics remain contractual "
            "and require verification against current vendor program documents. "
            "The cited statutes establish diligence boundaries rather than "
            "validating demand or specific marketplace program terms."
        ),
        "sources": [
            "https://www.law.cornell.edu/uscode/text/17/106",
            "https://www.law.cornell.edu/uscode/text/17/109",
            (
                "https://www.ecfr.gov/current/title-15/subtitle-B/chapter-VII/"
                "subchapter-C/part-734/section-734.3"
            ),
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Federal Software Procurement Specialist",
        "subtitle": (
            "Package commercial software licenses, defensible quotes, and scoped "
            "deployment services for federal purchasing requirements."
        ),
        "audience": (
            "Experienced public-sector channel sellers pairing procurement "
            "discipline with a small, vendor-authorized delivery bench."
        ),
        "research_basis": (
            "FAR 12.212 addresses commercial computer software licensing, while "
            "FAR 52.212-4 supplies contract terms when incorporated into the award. "
            "FAR 4.1102 establishes registration requirements and exceptions. "
            "These provisions support a procurement-specialist positioning, but "
            "do not establish award probability or customer purchasing volume."
        ),
        "sources": [
            "https://www.acquisition.gov/far/12.212",
            "https://www.acquisition.gov/far/52.212-4",
            "https://www.acquisition.gov/far/4.1102",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Renewal and Implementation Desk",
        "subtitle": (
            "Turn license inventories, renewal calendars, and controlled "
            "implementation scopes into repeatable enterprise account operations."
        ),
        "audience": (
            "Software administrators and account operators serving organizations "
            "that need reliable entitlement records and restricted implementation access."
        ),
        "research_basis": (
            "California Civil Code section 1798.100(d) sets contractual requirements "
            "for specified personal-information disclosures by covered businesses. "
            "16 CFR 314.4(f) addresses service-provider oversight by covered "
            "financial institutions. These requirements support careful access "
            "design and contracting where applicable; neither applies automatically "
            "to every reseller or every customer."
        ),
        "sources": [
            (
                "https://leginfo.legislature.ca.gov/faces/"
                "codes_displaySection.xhtml?sectionNum=1798.100.&lawCode=CIV"
            ),
            (
                "https://www.ecfr.gov/current/title-16/chapter-I/"
                "subchapter-C/part-314/section-314.4"
            ),
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
]


def build_volume_019_diagrams_data() -> list[dict]:
    specs = [
        (
            "diag-01-authorized-resale-workflow",
            "process_flow",
            "From Vendor Authorization to Collected Renewal",
            "Five operating stages for license resale and implementation delivery.",
            1,
            "operating_framework",
            (
                "The scorecard uses gross license resale and service billings, "
                "with vendor costs included in margin. Customer cloud consumption "
                "outside the reseller contract is excluded. For actual reporting, "
                "assess principal-versus-agent treatment separately; a commission-only "
                "arrangement cannot inherit gross resale revenue merely because "
                "the reseller helped arrange the purchase."
            ),
            (
                "Maintain one linked evidence trail across vendor authorization, "
                "registered opportunity, customer order, entitlement delivery, "
                "vendor settlement, and renewal ownership."
            ),
            [
                (
                    "Authorize",
                    "Document program rights before offering licenses",
                    1.0,
                    (
                        "Confirm vendor territory, products, customer eligibility, "
                        "deal-registration rules, and resale rights. Distinguish "
                        "AWS Marketplace CPPO selling authorization from Microsoft "
                        "CSP direct-bill or indirect-reseller responsibilities."
                    ),
                ),
                (
                    "Qualify",
                    "Validate buyer authority and renewal timing",
                    2.0,
                    (
                        "Use Salesforce or HubSpot to record the procurement owner, "
                        "incumbent contract, renewal date, seat inventory, budget "
                        "evidence, and competitive channel position."
                    ),
                ),
                (
                    "Quote",
                    "Lock vendor economics and implementation scope",
                    3.0,
                    (
                        "Generate a versioned quote from current vendor pricing; "
                        "separate license charges, deployment fees, marketplace "
                        "charges, payment dates, and change-order rates."
                    ),
                ),
                (
                    "Deliver",
                    "Reconcile purchased licenses against accepted delivery",
                    4.0,
                    (
                        "Verify customer tenant identifiers, assign entitlements, "
                        "complete the implementation checklist, and capture "
                        "acceptance without retaining unnecessary privileged access."
                    ),
                ),
                (
                    "Collect and renew",
                    "Match settlements and activate renewal alerts",
                    5.0,
                    (
                        "Reconcile customer receipts, marketplace remittances, "
                        "vendor invoices, and credits. Schedule 120-, 90-, and "
                        "60-day renewal alerts with named account ownership."
                    ),
                ),
            ],
        ),
        (
            "diag-02-enterprise-opportunity-funnel",
            "funnel",
            "A Nested Annual Enterprise Sales Cohort",
            "100 target accounts narrow to seven collected customer contracts.",
            6,
            "illustrative_model",
            (
                "Illustrative mature-year cohort, not an observed conversion "
                "benchmark. Each stage is a subset of the preceding stage. "
                "Seven contracts averaging $200,000 in gross license and service "
                "billings produce the $1,400,000 Base-Case revenue. Assume delivery, "
                "billing, and collection occur within the modeled year."
            ),
            (
                "Track conversion and elapsed days separately: the canonical "
                "time to first deal is 3–12 months, so these annual results "
                "are not a first-month sales commitment."
            ),
            [
                (
                    "Target accounts",
                    "100 named enterprise accounts with channel fit",
                    100.0,
                    (
                        "Create a deduplicated account cohort with a compatible "
                        "software estate, supported geography, identifiable buyer, "
                        "and documented renewal or deployment trigger."
                    ),
                ),
                (
                    "Qualified discovery",
                    "40 accounts; 40% of the initial cohort",
                    40.0,
                    (
                        "Confirm a reachable procurement owner, real purchasing "
                        "timeline, vendor eligibility, and a problem that can "
                        "be solved within the pod's delivery capacity."
                    ),
                ),
                (
                    "Validated opportunities",
                    "20 accounts; 50% of qualified discovery",
                    20.0,
                    (
                        "Verify license quantities, budget ownership, technical "
                        "fit, and the applicable deal-registration position "
                        "before investing in detailed solution design."
                    ),
                ),
                (
                    "Executable proposals",
                    "10 accounts; 50% of validated opportunities",
                    10.0,
                    (
                        "Issue customer-specific quotes or private offers with "
                        "confirmed vendor pricing, purchasing route, implementation "
                        "scope, acceptance terms, and collection exposure."
                    ),
                ),
                (
                    "Collected contracts",
                    "7 accounts; 70% of executable proposals",
                    7.0,
                    (
                        "Seven times $200,000 equals $1,400,000 in gross annual "
                        "resale and service billings. Vendor acquisition costs "
                        "remain expenses rather than additional revenue."
                    ),
                ),
            ],
        ),
        (
            "diag-03-base-case-profit-waterfall",
            "waterfall",
            "Base-Case Gross Billings to 14.0% Owner Net",
            "$1,400,000 gross revenue less $1,204,000 costs equals $196,000.",
            3,
            "illustrative_model",
            (
                "Six bars: the first is an opening total, the middle four "
                "are signed deductions, and the last is a closing total rather "
                "than another additive movement. Cost allocations are illustrative; "
                "the canonical revenue, margin, and owner net are fixed. "
                "All operating charges are contained in the four expense buckets; "
                "owner-level personal taxes are outside this model."
            ),
            (
                "Vendor costs consume 70.0% of gross revenue; delivery, staffing, "
                "and overhead consume another 16.0%. The remaining 14.0% is "
                "the canonical $196,000 annual owner net profit."
            ),
            [
                (
                    "Gross revenue",
                    "$1,400,000 annual license resale and service billings",
                    1400000.0,
                    (
                        "Opening total includes only the reseller's modeled "
                        "license and service sales, excluding unrelated customer "
                        "cloud spend and sales taxes collected for remittance."
                    ),
                ),
                (
                    "Vendor acquisition",
                    "Subtract $980,000; 70.0% of gross revenue",
                    -980000.0,
                    (
                        "Illustrative software acquisition and distributor charges "
                        "leave $420,000 before delivery and operating expenses. "
                        "Do not count prospective vendor rebates before earned."
                    ),
                ),
                (
                    "Contract delivery",
                    "Subtract $84,000; 6.0% of gross revenue",
                    -84000.0,
                    (
                        "Three contractor seats share $84,000 in annual engagement "
                        "spend for scoped implementation, license reconciliation, "
                        "and specialist support; seats are not full-time equivalents."
                    ),
                ),
                (
                    "Full-time staffing",
                    "Subtract $98,000; 7.0% of gross revenue",
                    -98000.0,
                    (
                        "Two full-time seats share an illustrative loaded annual "
                        "staffing budget of $98,000. Higher local compensation "
                        "requires additional contribution or reduces owner net."
                    ),
                ),
                (
                    "Operating overhead",
                    "Subtract $42,000; 3.0% of gross revenue",
                    -42000.0,
                    (
                        "Illustrative overhead includes marketplace charges not "
                        "already in vendor costs, CRM, insurance, professional "
                        "services, collection losses, and other operating charges."
                    ),
                ),
                (
                    "Annual owner net",
                    "$196,000 retained; exactly 14.0% net margin",
                    196000.0,
                    (
                        "$1,400,000 minus $980,000 minus $84,000 minus $98,000 "
                        "minus $42,000 equals $196,000. Non-vendor operating costs "
                        "average $18,666.67 monthly, within the canonical range."
                    ),
                ),
            ],
        ),
        (
            "diag-04-channel-contribution-yields",
            "horizontal_bars",
            "Compare Five Channel and Service Offers",
            "Illustrative contribution yields after vendor and direct delivery costs.",
            2,
            "illustrative_model",
            (
                "Bars show contribution as a percentage of each offer's gross "
                "billings, before shared staffing and overhead; they are not "
                "net margins or vendor-published discounts. Each example uses "
                "$100,000 gross billings. These independent examples are not "
                "a weighted portfolio forecast."
            ),
            (
                "Canonical annual outcomes remain Conservative: $300,000 at "
                "8% equals $24,000; Base: $1,400,000 at 14.0% equals $196,000; "
                "Scaled: $2,500,000 at 20% equals $500,000. The first two "
                "use 2 FT + 3 C; Scaled uses 3 FT + 4 C."
            ),
            [
                (
                    "CSP seat renewals",
                    "18% contribution after directly attributable costs",
                    18.0,
                    (
                        "$100,000 gross billings less $82,000 vendor and direct "
                        "support costs leaves $18,000. Verify renewal pricing, "
                        "cancellation windows, and responsibility for unpaid seats."
                    ),
                ),
                (
                    "CPPO license offers",
                    "24% contribution after directly attributable costs",
                    24.0,
                    (
                        "$100,000 gross billings less $76,000 vendor, marketplace, "
                        "and direct execution costs leaves $24,000. Confirm the "
                        "selling authorization and actual settlement calendar."
                    ),
                ),
                (
                    "Security software deployments",
                    "30% contribution after directly attributable costs",
                    30.0,
                    (
                        "$100,000 gross billings less $70,000 license and deployment "
                        "costs leaves $30,000. Price integrations explicitly and "
                        "separate customer acceptance from open-ended remediation."
                    ),
                ),
                (
                    "Data-platform migrations",
                    "35% contribution after directly attributable costs",
                    35.0,
                    (
                        "$100,000 gross billings less $65,000 vendor and migration "
                        "costs leaves $35,000. Meter migration effort and exclude "
                        "customer infrastructure consumption outside the contract."
                    ),
                ),
                (
                    "Workflow application implementations",
                    "42% contribution after directly attributable costs",
                    42.0,
                    (
                        "$100,000 gross billings less $58,000 license and delivery "
                        "costs leaves $42,000. Limit custom connectors, document "
                        "acceptance tests, and charge separately for scope changes."
                    ),
                ),
            ],
        ),
        (
            "diag-05-resale-preflight-decisions",
            "decision_tree",
            "Four Checks Before a Binding Customer Offer",
            "Pass each applicable branch; resolve failures before committing spend.",
            5,
            "operating_framework",
            (
                "Apply checks to the actual product, buyer, geography, procurement "
                "route, and data access. Reseller authorization is a contractual "
                "requirement; statutory duties depend on the transaction. "
                "The numbered stages are sequential decision nodes, not risk scores."
            ),
            (
                "Store the supporting evidence and decision owner with the "
                "opportunity record; a vendor discount alone does not resolve "
                "license rights, procurement duties, data access, or collection risk."
            ),
            [
                (
                    "Distribution rights",
                    "Authorized product, territory, customer, and license use?",
                    1.0,
                    (
                        "Yes: attach current vendor authorization and license "
                        "terms. No: obtain permission or remove the product. "
                        "17 U.S.C. 106 governs exclusive rights; do not assume "
                        "17 U.S.C. 109 authorizes transfers of cloud subscriptions "
                        "or every licensed software arrangement."
                    ),
                ),
                (
                    "Procurement and payment",
                    "Valid purchasing route with financeable collection exposure?",
                    2.0,
                    (
                        "Yes: verify buyer authority, order documents, vendor "
                        "due dates, and cash coverage. No: revise terms or "
                        "decline unfunded exposure. For federal purchases, apply "
                        "FAR 12.212, applicable award clauses such as FAR 52.212-4, "
                        "and FAR 4.1102 registration requirements and exceptions."
                    ),
                ),
                (
                    "Data-processing duties",
                    "Documented access scope and applicable processing terms?",
                    3.0,
                    (
                        "Yes: use least-privilege access and a removal checklist. "
                        "No: complete required contracts before accessing customer "
                        "data. California Civil Code 1798.100(d) applies to "
                        "specified disclosures by covered businesses; 16 CFR "
                        "314.4(f) addresses covered financial institutions' "
                        "service-provider oversight."
                    ),
                ),
                (
                    "Export and channel exposure",
                    "Permitted destination and stable documented vendor economics?",
                    4.0,
                    (
                        "Yes: retain product classification, customer screening "
                        "evidence, quote expiry, and vendor price protection. "
                        "No: resolve restrictions or decline the transaction. "
                        "Assess EAR scope under 15 CFR 734.3 and applicable "
                        "restrictions under parts 744 and 746; escalate applicable "
                        "OFAC restrictions before fulfillment."
                    ),
                ),
            ],
        ),
        (
            "diag-06-five-to-seven-person-pod",
            "org_architecture",
            "Five Core Seats, Two Explicit Scale Additions",
            "Conservative and Base: 2 FT + 3 C; Scaled: 3 FT + 4 C.",
            11,
            "operating_framework",
            (
                "Each stage represents one person, with numeric_value equal to "
                "one seat. The first five seats form the active core pod; the "
                "last two are conditional scale additions. Contractor seats "
                "represent retained people, not full-time labor commitments."
            ),
            (
                "Keep commercial ownership and operational control in the two "
                "core full-time seats. Add the third full-time seat and fourth "
                "contractor only when workload and funded economics support them."
            ),
            [
                (
                    "Channel principal",
                    "Core seat one: full-time commercial owner",
                    1.0,
                    (
                        "Own vendor relationships, deal registration, pricing "
                        "exceptions, strategic accounts, and contribution review. "
                        "Check channel conflict before promising exclusivity."
                    ),
                ),
                (
                    "Revenue operations lead",
                    "Core seat two: full-time operating owner",
                    1.0,
                    (
                        "Own quote generation, CRM hygiene, purchase-order matching, "
                        "license reconciliation, receivables aging, and automated "
                        "renewal alerts tied to verified contract dates."
                    ),
                ),
                (
                    "Implementation architect",
                    "Core seat three: scoped delivery contractor",
                    1.0,
                    (
                        "Translate discovery into a bounded deployment plan, "
                        "estimate integrations, define acceptance tests, and "
                        "prevent unpaid implementation work from absorbing spread."
                    ),
                ),
                (
                    "License operations specialist",
                    "Core seat four: entitlement reconciliation contractor",
                    1.0,
                    (
                        "Match ordered products to customer tenants and active "
                        "seats, investigate vendor invoice discrepancies, and "
                        "produce evidence for renewal quantity decisions."
                    ),
                ),
                (
                    "Technical support specialist",
                    "Core seat five: scheduled support contractor",
                    1.0,
                    (
                        "Handle defined support windows, document recurring "
                        "incidents, escalate product defects to the vendor, "
                        "and keep unsupported customizations outside standard scope."
                    ),
                ),
                (
                    "Expansion account manager",
                    "Scaled addition: third full-time operating seat",
                    1.0,
                    (
                        "Activate for the seven-person model to own expansion "
                        "and renewal negotiations. Measure contribution retained "
                        "and overdue balances, not merely booked contract value."
                    ),
                ),
                (
                    "Migration delivery specialist",
                    "Scaled addition: fourth retained contractor seat",
                    1.0,
                    (
                        "Activate when signed implementation backlog exceeds "
                        "the core delivery bench. Use project-specific statements "
                        "of work and maintain independent acceptance evidence."
                    ),
                ),
            ],
        ),
        (
            "diag-07-startup-capital-allocation",
            "stacked_comparison",
            "Allocate Startup Cash Without Hiding Vendor Float",
            "Four buckets total $75,000 within the $25,000–$150,000 range.",
            4,
            "illustrative_model",
            (
                "numeric_value encodes the $75,000 planning allocation. Matching "
                "low-capital allocations total $25,000 and high-capital allocations "
                "total $150,000, as detailed in each bucket. These are startup "
                "capital envelopes, not the Conservative, Base, and Scaled "
                "annual revenue scenarios."
            ),
            (
                "Startup cash funds timing differences and operating readiness; "
                "it is not revenue. First deals may take 3–12 months, so "
                "recalculate runway against actual spending and vendor terms."
            ),
            [
                (
                    "Vendor settlement float",
                    "$30,000 planning allocation; 40.0% of startup cash",
                    30000.0,
                    (
                        "Low envelope: $10,000; high envelope: $60,000. Cover "
                        "the gap between vendor payment and customer settlement. "
                        "Do not accept orders whose uncovered exposure exceeds "
                        "available cash and confirmed credit capacity."
                    ),
                ),
                (
                    "Operating cash reserve",
                    "$20,000 planning allocation; 26.7% of startup cash",
                    20000.0,
                    (
                        "Low envelope: $7,000; high envelope: $40,000. At the "
                        "canonical $5,000–$25,000 monthly operating range, this "
                        "$20,000 reserve covers 4.0 to 0.8 months before "
                        "receipts, excluding separately allocated vendor float."
                    ),
                ),
                (
                    "Vendor enablement and delivery",
                    "$15,000 planning allocation; 20.0% of startup cash",
                    15000.0,
                    (
                        "Low envelope: $5,000; high envelope: $30,000. Fund "
                        "required certifications, documented demonstration environments, "
                        "deployment runbooks, and limited specialist preparation "
                        "for the chosen product family."
                    ),
                ),
                (
                    "Commercial systems and setup",
                    "$10,000 planning allocation; 13.3% of startup cash",
                    10000.0,
                    (
                        "Low envelope: $3,000; high envelope: $20,000. Establish "
                        "CRM, quote templates, accounting integration, insurance, "
                        "contract review, and focused account research without "
                        "committing to broad paid acquisition."
                    ),
                ),
            ],
        ),
        (
            "diag-08-thirty-day-launch-roadmap",
            "timeline_roadmap",
            "A Thirty-Day Sprint to a Ready Sales Operation",
            "Build evidence, economics, and repeatable execution before scaling outreach.",
            12,
            "operating_framework",
            (
                "Milestones represent Days 1–7, 8–14, 15–21, and 22–30; "
                "numeric_value records each milestone's ending day. This sprint "
                "prepares the operating system and early pipeline. Canonical "
                "time to first deal remains 3–12 months."
            ),
            (
                "Finish the month with a narrow product thesis, reconciled "
                "economics, a tested delivery workflow, and accountable prospect "
                "follow-up rather than an assumed closed sale."
            ),
            [
                (
                    "Days 1–7",
                    "Choose one product family and verify channel access",
                    7.0,
                    (
                        "Select a buyer segment, request vendor authorization, "
                        "map CPPO or CSP participation requirements, identify "
                        "required certifications, and document unresolved eligibility "
                        "items before making customer-facing resale claims."
                    ),
                ),
                (
                    "Days 8–14",
                    "Build quote economics and settlement controls",
                    14.0,
                    (
                        "Create a versioned quote template and vendor-cost ledger. "
                        "Reconcile $1,400,000 gross billings to $196,000 owner "
                        "net in the Base model; stress-test delayed collections "
                        "against the startup cash allocation."
                    ),
                ),
                (
                    "Days 15–21",
                    "Test implementation and automate recurring account work",
                    21.0,
                    (
                        "Use an authorized demonstration tenant to test entitlement "
                        "reconciliation, acceptance evidence, access removal, quote "
                        "generation, and renewal alerts. Obtain contractor scopes "
                        "with explicit effort limits and change-order pricing."
                    ),
                ),
                (
                    "Days 22–30",
                    "Launch targeted discovery and review operating evidence",
                    30.0,
                    (
                        "Research the initial 100-account cohort, begin relevant "
                        "outreach, and record actual stage movement without "
                        "assuming the annual funnel converts this month. Review "
                        "authorization status, cash exposure, delivery readiness, "
                        "and each opportunity's next dated action."
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
