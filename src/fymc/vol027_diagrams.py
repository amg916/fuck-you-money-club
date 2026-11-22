from __future__ import annotations

VOLUME_027_SUBTITLE: str = (
    "The Complete Playbook for Buying Cash-Flowing Businesses: "
    "$750,000–$3,000,000 USD in Annual Acquired-Business Sales, "
    "a 7 FT + 3 C (10-Person) Core Pod, and Disciplined Debt"
)

VOLUME_027_POSITIONING_ALTERNATIVES: list[dict] = [
    {
        "title": "Buy the Earnings, Audit the Cash",
        "subtitle": (
            "An ETA operator's playbook for QoE, customer retention, "
            "working-capital terms, and cash-flowing SMB ownership."
        ),
        "audience": (
            "First-time acquisition entrepreneurs and small holding-company "
            "operators evaluating established businesses with recurring customers."
        ),
        "research_basis": (
            "26 U.S.C. § 1060 establishes purchase-price allocation requirements "
            "for applicable asset acquisitions; UCC § 9-315 addresses continuing "
            "security interests in collateral and proceeds. These rules support "
            "separate workstreams for earnings verification, asset allocation, "
            "lien searches, and closing releases. They do not establish market demand."
        ),
        "sources": [
            "https://www.law.cornell.edu/uscode/text/26/1060",
            "https://www.irs.gov/forms-pubs/about-form-8594",
            "https://www.law.cornell.edu/ucc/9/9-315",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "Debt That Leaves Room to Operate",
        "subtitle": (
            "Structure SBA debt, seller notes, and working capital around "
            "verified collections rather than seller-adjusted optimism."
        ),
        "audience": (
            "Buyer-operators using acquisition debt who need explicit repayment "
            "models, lender covenant monitoring, and downside liquidity planning."
        ),
        "research_basis": (
            "13 CFR §§ 120.110, 120.150, and 120.160 address SBA business "
            "eligibility, lending criteria, and loan conditions. The operating "
            "framework separates those requirements from transaction-specific "
            "lender terms and requires current program guidance for seller-note "
            "standby treatment and equity-injection eligibility."
        ),
        "sources": [
            "https://www.ecfr.gov/current/title-13/section-120.110",
            "https://www.ecfr.gov/current/title-13/section-120.150",
            "https://www.ecfr.gov/current/title-13/section-120.160",
            "https://www.sba.gov/funding-programs/loans/7a-loans",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The First 100 Days of Ownership",
        "subtitle": (
            "Protect customers, stabilize payroll, and install reporting "
            "before expanding a newly acquired service business."
        ),
        "audience": (
            "Micro-PE sponsors and hands-on general managers integrating "
            "labor-intensive businesses with a ten-to-twelve-person operating pod."
        ),
        "research_basis": (
            "29 U.S.C. § 207 supplies federal overtime requirements for covered "
            "nonexempt employees; 29 U.S.C. §§ 2101–2102 define federal WARN "
            "coverage and notice duties. Coverage depends on the acquired "
            "enterprise and transaction facts, not merely the acquisition pod's "
            "headcount. These sources inform workforce diligence and transition planning."
        ),
        "sources": [
            "https://www.law.cornell.edu/uscode/text/29/207",
            "https://www.law.cornell.edu/uscode/text/29/2101",
            "https://www.law.cornell.edu/uscode/text/29/2102",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
]


def build_volume_027_diagrams_data() -> list[dict]:
    specs = [
        (
            "diag-01-acquisition-to-operating-control",
            "process_flow",
            "Buy Verified Earnings; Then Protect Them",
            "Five linked workstreams from acquisition thesis to the first 100 days.",
            1,
            "operating_framework",
            (
                "First-deal timing is 6–18 months. The 100-day operating plan "
                "starts after closing, not after initial outreach. Recognized "
                "revenue is acquired-business sales, not purchase price, borrowed "
                "principal, seller proceeds, or transaction volume."
            ),
            (
                "Advance only with the evidence named in each stage; keep the "
                "customer-retention plan connected to the purchase agreement."
            ),
            [
                (
                    "Define the buy box",
                    "Owner: acquisition lead",
                    1.0,
                    (
                        "Specify geography, transferable licenses, customer "
                        "concentration limits, operator replacement cost, and "
                        "a $200,000–$1,000,000 buyer-capital envelope."
                    ),
                ),
                (
                    "Verify earnings",
                    "Owner: QoE and tax contractor",
                    2.0,
                    (
                        "Tie QuickBooks exports to bank deposits, tax returns, "
                        "receivables aging, payroll, and customer contracts; "
                        "remove unsupported add-backs and identify maintenance capex."
                    ),
                ),
                (
                    "Structure the purchase",
                    "Owner: acquisition lead and counsel",
                    3.0,
                    (
                        "Model lender debt and seller notes separately; define "
                        "working-capital delivery, asset allocation, lien releases, "
                        "representations, indemnities, and required contract transfers."
                    ),
                ),
                (
                    "Transfer operating control",
                    "Owner: general manager",
                    4.0,
                    (
                        "Reconcile closing funds, verify insurance and license "
                        "continuity, transfer authorized bank access, and test "
                        "payroll and customer billing before retiring seller access."
                    ),
                ),
                (
                    "Run the 100-day plan",
                    "Owner: general manager and controller",
                    5.0,
                    (
                        "Track weekly collections, customer retention, backlog, "
                        "service defects, and covenant headroom; automate reporting "
                        "only after ledger ownership and exception handling work."
                    ),
                ),
            ],
        ),
        (
            "diag-02-single-cohort-sourcing-funnel",
            "funnel",
            "One Cohort, Five Evidence Filters",
            "An illustrative 120-target search cohort narrows to two signed LOIs.",
            6,
            "illustrative_model",
            (
                "Counts describe one hypothetical cohort observed through a "
                "common cutoff, not monthly throughput or an industry benchmark. "
                "Each stage is a subset of the preceding stage. A signed LOI "
                "does not establish a completed acquisition."
            ),
            (
                "Stage conversions are 40%, 50%, 33.33%, and 25%; cumulative "
                "target-to-LOI conversion is 2 / 120 = 1.67%."
            ),
            [
                (
                    "Qualified targets",
                    "120 businesses fit the buy box",
                    120.0,
                    (
                        "Deduplicate broker and direct-owner leads in Airtable; "
                        "record business identity, geography, sector, and a "
                        "specific reason the ownership model fits."
                    ),
                ),
                (
                    "Owner conversations",
                    "48 of 120 targets; 40% conversion",
                    48.0,
                    (
                        "Confirm seller authority, transition intentions, expected "
                        "timing, and willingness to provide operating records "
                        "before requesting confidential customer-level material."
                    ),
                ),
                (
                    "Usable data rooms",
                    "24 of 48 conversations; 50% conversion",
                    24.0,
                    (
                        "Execute confidentiality terms and obtain sufficient "
                        "ledger, payroll, tax, and receivables records to compare "
                        "the seller narrative with recorded operating activity."
                    ),
                ),
                (
                    "Diligence-ready candidates",
                    "8 of 24 data rooms; 33.33% conversion",
                    8.0,
                    (
                        "Complete preliminary earnings normalization, concentration "
                        "review, and debt-service stress testing; reserve full "
                        "third-party QoE expenditure for the selected transaction."
                    ),
                ),
                (
                    "Signed LOIs",
                    "2 of 8 candidates; 25% conversion",
                    2.0,
                    (
                        "Negotiate price mechanics, exclusivity, diligence access, "
                        "and closing conditions sequentially where capacity demands; "
                        "neither LOI is counted as revenue or a closed deal."
                    ),
                ),
            ],
        ),
        (
            "diag-03-base-case-earnings-waterfall",
            "waterfall",
            "From $1,875,000 Sales to $243,750 Owner Net",
            "Six bars reconcile the Base-Case 13.0% annual net margin.",
            3,
            "illustrative_model",
            (
                "Canonical annual outcomes: Conservative $750,000 sales at 8% "
                "equals $60,000 owner net; Base $1,875,000 at 13.0% equals "
                "$243,750; Scaled $3,000,000 at 18% equals $540,000. Expense "
                "allocations below are illustrative, not additional scorecard "
                "inputs. Net is after interest and before principal repayments; "
                "no separate owner-level income-tax calculation is supplied."
            ),
            (
                "Render sales as the opening total, four negative expense "
                "movements, and owner net as the closing total: $1,875,000 "
                "− $900,000 − $450,000 − $187,500 − $93,750 = $243,750. "
                "Do not add the closing total as another movement."
            ),
            [
                (
                    "Acquired-business sales",
                    "$1,875,000 annual recognized revenue",
                    1875000.0,
                    (
                        "Use earned sales from the operating company; exclude "
                        "acquisition debt proceeds, equity contributions, sales "
                        "tax collected for remittance, and purchase consideration."
                    ),
                ),
                (
                    "Direct fulfillment costs",
                    "Subtract $900,000 annual direct costs",
                    -900000.0,
                    (
                        "Allocate materials, outside fulfillment, and other direct "
                        "costs here; exclude pod payroll already assigned below. "
                        "The remaining gross profit is $975,000."
                    ),
                ),
                (
                    "Recurring pod labor",
                    "Subtract $450,000 annual labor expense",
                    -450000.0,
                    (
                        "Illustrative loaded labor and recurring contractor "
                        "expense averages $37,500 monthly across the core pod; "
                        "validate local wages, benefits, and contractor scope."
                    ),
                ),
                (
                    "Other operating expense",
                    "Subtract $187,500 annual operating expense",
                    -187500.0,
                    (
                        "Budget $15,625 monthly for occupancy, insurance, software, "
                        "and remaining operating charges. Together with pod labor, "
                        "recurring overhead is $53,125 monthly, excluding direct costs."
                    ),
                ),
                (
                    "Interest expense",
                    "Subtract $93,750 annual interest expense",
                    -93750.0,
                    (
                        "Interest averages $7,812.50 monthly in this allocation. "
                        "Debt principal is not an earnings expense; model its "
                        "cash requirement separately using actual amortization schedules."
                    ),
                ),
                (
                    "Annual owner net profit",
                    "$243,750 closing total; 13.0% margin",
                    243750.0,
                    (
                        "Divide $243,750 by $1,875,000 to recover 13.0%. "
                        "Then separately bridge earnings to available cash for "
                        "principal, working-capital changes, capex, and distributions."
                    ),
                ),
            ],
        ),
        (
            "diag-04-subniche-collection-yields",
            "horizontal_bars",
            "Collection Yield by Acquisition Sub-Niche",
            "Illustrative dollars banked within 30 days per $100 invoiced.",
            2,
            "illustrative_model",
            (
                "Five independent underwriting examples use hypothetical collection "
                "assumptions, not observed sector averages. Numeric values are "
                "percentages of an invoice cohort collected within 30 days. "
                "Collections are measured before payment-processing fees; slower "
                "collection does not automatically mean bad debt."
            ),
            (
                "Compare cash conversion rather than mistaking payment-rail "
                "receipts for incremental sales or owner profit. Replace every "
                "assumption with target-specific invoice and bank evidence."
            ),
            [
                (
                    "Managed IT services",
                    "$95 banked per $100 invoiced",
                    95.0,
                    (
                        "Illustrative recurring ACH cohort: verify debit "
                        "authorizations, return histories, disputed service credits, "
                        "and whether customer contracts survive the ownership change."
                    ),
                ),
                (
                    "Commercial cleaning",
                    "$90 banked per $100 invoiced",
                    90.0,
                    (
                        "Illustrative ACH and check cohort: inspect customer "
                        "payment runs, site acceptance requirements, invoice "
                        "disputes, and payroll funded before customer collection."
                    ),
                ),
                (
                    "Equipment maintenance",
                    "$85 banked per $100 invoiced",
                    85.0,
                    (
                        "Illustrative card and ACH cohort: reconcile signed "
                        "service tickets, parts charges, processor deductions, "
                        "refund exposure, and commercial-account credit terms."
                    ),
                ),
                (
                    "Specialty distribution",
                    "$80 banked per $100 invoiced",
                    80.0,
                    (
                        "Illustrative trade-credit cohort: test delivery evidence, "
                        "returns, deductions, inventory funding, and customer "
                        "credit limits rather than relying on invoice totals."
                    ),
                ),
                (
                    "Commercial field services",
                    "$75 banked per $100 invoiced",
                    75.0,
                    (
                        "Illustrative milestone-billing cohort: identify retainage, "
                        "purchase-order mismatches, disputed completion certificates, "
                        "and collection delays hidden inside reported receivables."
                    ),
                ),
            ],
        ),
        (
            "diag-05-preflight-statutory-risk-tree",
            "decision_tree",
            "Four Checks Before Committing Closing Funds",
            "Each affirmative branch advances; unresolved evidence returns to diligence.",
            5,
            "operating_framework",
            (
                "Apply jurisdiction-specific employment, tax, licensing, and "
                "secured-transactions rules to the actual deal structure. SBA "
                "requirements apply when using the relevant program; lender "
                "covenants and disclosure obligations depend on executed terms."
            ),
            (
                "Treat the four nodes as sequential decisions. An unresolved "
                "branch requires a documented cure, revised economics, or "
                "withdrawal before funds are committed."
            ),
            [
                (
                    "Can title transfer cleanly?",
                    "Yes: advance; unresolved: obtain releases",
                    1.0,
                    (
                        "Search applicable UCC filing offices and inspect liens "
                        "outside that system. UCC § 9-315 generally preserves "
                        "security interests after disposition unless an exception "
                        "applies; obtain secured-party releases and payoff evidence."
                    ),
                ),
                (
                    "Are tax terms executable?",
                    "Yes: advance; unresolved: revise closing terms",
                    2.0,
                    (
                        "For applicable asset acquisitions, align allocation and "
                        "Form 8594 reporting under 26 U.S.C. § 1060. Review "
                        "state successor-tax exposure, payroll remittances, "
                        "clearance requirements, and tax-related indemnity support."
                    ),
                ),
                (
                    "Can people and licenses continue?",
                    "Yes: advance; unresolved: cure continuity risks",
                    3.0,
                    (
                        "Test overtime exposure under 29 U.S.C. § 207, "
                        "applicable WARN duties under §§ 2101–2102, state "
                        "employment rules, and license transfer restrictions. "
                        "Obtain required consents and verify customer assignment terms."
                    ),
                ),
                (
                    "Does the debt structure survive stress?",
                    "Yes: proceed; unresolved: resize or withdraw",
                    4.0,
                    (
                        "For SBA transactions, review 13 CFR §§ 120.110, "
                        "120.150, and 120.160 plus current program requirements. "
                        "Disclose seller notes and side agreements; stress "
                        "principal, interest, customer loss, and covenant headroom."
                    ),
                ),
            ],
        ),
        (
            "diag-06-ten-to-twelve-person-pod",
            "org_architecture",
            "Ten Core Seats; Two Explicit Scale Additions",
            "Base and Conservative: 7 FT + 3 C. Scaled: 8 FT + 4 C.",
            11,
            "operating_framework",
            (
                "Each numeric value represents one person. The first ten seats "
                "form the core pod; the final two activate only in the Scaled "
                "case. Contractors are people, not full-time-equivalent claims. "
                "Roles are an illustrative combined ownership-and-operation "
                "roster, not ten extra hires above an acquired workforce."
            ),
            (
                "The acquisition lead owns capital allocation; the general "
                "manager directs operations. Specialist contractors support "
                "defined workstreams without replacing management accountability."
            ),
            [
                (
                    "Acquisition lead",
                    "Core FT 1 of 7",
                    1.0,
                    (
                        "Own purchase discipline, lender relationships, "
                        "investment decisions, seller negotiations, and the "
                        "weekly review of liquidity and customer concentration."
                    ),
                ),
                (
                    "General manager",
                    "Core FT 2 of 7",
                    1.0,
                    (
                        "Own the operating result, customer retention, staffing "
                        "priorities, service recovery, and execution of the "
                        "post-close 100-day integration plan."
                    ),
                ),
                (
                    "Operations lead",
                    "Core FT 3 of 7",
                    1.0,
                    (
                        "Control scheduling, vendor commitments, capacity "
                        "allocation, backlog aging, and daily escalation of "
                        "delivery constraints to the general manager."
                    ),
                ),
                (
                    "Service lead",
                    "Core FT 4 of 7",
                    1.0,
                    (
                        "Set delivery standards, supervise job execution, "
                        "review defects, and preserve customer-specific operating "
                        "knowledge that could leave with the seller."
                    ),
                ),
                (
                    "Delivery specialist",
                    "Core FT 5 of 7",
                    1.0,
                    (
                        "Perform customer work, capture completion evidence, "
                        "record materials and hours, and flag scope changes "
                        "before they become unbilled service."
                    ),
                ),
                (
                    "Account and retention lead",
                    "Core FT 6 of 7",
                    1.0,
                    (
                        "Own renewals, customer transition calls, dispute "
                        "resolution, concentration monitoring, and early "
                        "escalation of threatened account departures."
                    ),
                ),
                (
                    "Controller and reporting lead",
                    "Core FT 7 of 7",
                    1.0,
                    (
                        "Own QuickBooks reconciliations, the cash forecast, "
                        "receivables follow-up, covenant calculations, and "
                        "automated management reporting with reviewed exceptions."
                    ),
                ),
                (
                    "Transaction counsel",
                    "Core contractor 1 of 3",
                    1.0,
                    (
                        "Review transaction disclosures, purchase terms, lien "
                        "releases, license transfers, employment issues, and "
                        "post-close claims within a defined engagement."
                    ),
                ),
                (
                    "QoE and tax specialist",
                    "Core contractor 2 of 3",
                    1.0,
                    (
                        "Normalize earnings, test working capital, evaluate "
                        "tax allocation, and reconcile diligence findings "
                        "with the opening operating-company records."
                    ),
                ),
                (
                    "Systems and workflow specialist",
                    "Core contractor 3 of 3",
                    1.0,
                    (
                        "Configure Microsoft 365 access, accounting integrations, "
                        "backups, and back-office workflows; document recovery "
                        "procedures and test exception ownership."
                    ),
                ),
                (
                    "Capacity supervisor",
                    "Scaled addition: FT 8 of 8",
                    1.0,
                    (
                        "Add only in the twelve-person Scaled configuration "
                        "to supervise higher throughput, absorb scheduling "
                        "complexity, and prevent service-quality erosion."
                    ),
                ),
                (
                    "Integration coach",
                    "Scaled addition: contractor 4 of 4",
                    1.0,
                    (
                        "Add time-bounded process coaching and integration "
                        "support in the Scaled configuration; transfer "
                        "documented routines to the permanent operating leads."
                    ),
                ),
            ],
        ),
        (
            "diag-07-buyer-capital-allocation",
            "stacked_comparison",
            "Allocate Buyer Capital Before Negotiating Price",
            "Four buckets divide an illustrative $600,000 startup-capital plan.",
            4,
            "illustrative_model",
            (
                "The canonical buyer-capital range is $200,000–$1,000,000. "
                "The $600,000 illustration allocates 40%, 10%, 30%, and 20%. "
                "Boundary allocations use the same illustrative weights, not "
                "claims that every transaction is feasible at either boundary."
            ),
            (
                "Numeric values are USD and sum to $600,000. Detail text "
                "provides comparable $200,000 and $1,000,000 allocations. "
                "Buyer capital is neither recognized sales nor total enterprise value."
            ),
            [
                (
                    "Purchase equity contribution",
                    "$240,000; 40% of buyer capital",
                    240000.0,
                    (
                        "Allocate $80,000 at the lower boundary and $400,000 "
                        "at the upper boundary. Size debt separately; confirm "
                        "lender equity requirements and seller-note treatment "
                        "before treating any note as qualifying injection."
                    ),
                ),
                (
                    "Diligence and closing costs",
                    "$60,000; 10% of buyer capital",
                    60000.0,
                    (
                        "Allocate $20,000 at the lower boundary and $100,000 "
                        "at the upper boundary for QoE, counsel, tax work, "
                        "searches, and transaction expenses. Separate one-time "
                        "engagement charges from recurring contractor expense."
                    ),
                ),
                (
                    "Opening working-capital reserve",
                    "$180,000; 30% of buyer capital",
                    180000.0,
                    (
                        "Allocate $60,000 at the lower boundary and $300,000 "
                        "at the upper boundary. Fund collection gaps and "
                        "seasonality after reconciling seller-delivered working "
                        "capital to the negotiated closing adjustment."
                    ),
                ),
                (
                    "Integration and contingency liquidity",
                    "$120,000; 20% of buyer capital",
                    120000.0,
                    (
                        "Allocate $40,000 at the lower boundary and $200,000 "
                        "at the upper boundary for migration, retention, and "
                        "repair contingencies. Cash released for one purpose "
                        "cannot simultaneously remain available for another."
                    ),
                ),
            ],
        ),
        (
            "diag-08-first-thirty-days-search-sprint",
            "timeline_roadmap",
            "Thirty Days to a Decision-Ready Acquisition Search",
            "Build an evidence pipeline without pretending the first deal closes in a month.",
            12,
            "operating_framework",
            (
                "This is a pre-acquisition launch sprint. First-deal timing "
                "remains 6–18 months; the 100-day turnaround starts after "
                "closing. Numeric values are milestone endpoint days."
            ),
            (
                "Complete one inspectable operating artifact each week. "
                "A missing seller document becomes a tracked diligence issue, "
                "not an invented input to the debt model."
            ),
            [
                (
                    "Days 1-7",
                    "Deliver the buy box and capital plan",
                    7.0,
                    (
                        "Assign the acquisition lead; document sector exclusions, "
                        "buyer liquidity, operator capacity, and concentration "
                        "limits. Build the four-bucket capital worksheet and "
                        "identify lender and specialist interview targets."
                    ),
                ),
                (
                    "Days 8-14",
                    "Deliver the tracked sourcing cohort",
                    14.0,
                    (
                        "Configure Airtable stages and deduplication; begin "
                        "broker and owner outreach. Record response evidence, "
                        "confidentiality terms, seller authority, and requested "
                        "records without treating the illustrative funnel as a quota."
                    ),
                ),
                (
                    "Days 15-21",
                    "Deliver the first evidence-backed screening memo",
                    21.0,
                    (
                        "For a responsive target, reconcile available statements "
                        "to deposits, review customer concentration, and build "
                        "an interest-and-principal schedule. If records are "
                        "insufficient, issue a precise evidence request instead."
                    ),
                ),
                (
                    "Days 22-30",
                    "Deliver the pursue, revise, or reject decision",
                    30.0,
                    (
                        "Review the four pre-flight checks, document downside "
                        "liquidity, and price unresolved liabilities. Prepare "
                        "LOI terms only for a supported candidate; otherwise "
                        "revise the search and preserve diligence capital."
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
