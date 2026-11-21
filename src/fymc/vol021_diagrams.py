from __future__ import annotations

VOLUME_021_SUBTITLE = (
    "The Complete Playbook for Automated E-Commerce: "
    "$250,000–$2,000,000 USD Annually with a 2 FT + 3 C "
    "(5 People) Core Pod, Expanding to Seven at Scale"
)

VOLUME_021_POSITIONING_ALTERNATIVES = [
    {
        "title": "The Lean Authorized-Dealer Store",
        "subtitle": (
            "Build a 3PL-backed retail operation around documented supplier "
            "authorization, reliable inventory, and contribution-positive orders."
        ),
        "audience": (
            "Specialist retailers with supplier relationships who want a "
            "five-person core pod rather than an owned warehouse."
        ),
        "research_basis": (
            "Dealer authorization is a commercial sourcing control, not a "
            "substitute for product-safety responsibilities. Under 15 U.S.C. "
            "2064, distributors and retailers can have immediate reporting "
            "duties when specified product-hazard information becomes known. "
            "16 CFR Part 435 establishes shipment-promise, delay-option, and "
            "refund requirements for covered internet orders. These requirements "
            "support lot traceability, credible inventory feeds, and documented "
            "3PL exception handling; they do not establish market demand."
        ),
        "sources": [
            "https://www.law.cornell.edu/uscode/text/15/2064",
            "https://www.ecfr.gov/current/title-16/chapter-I/subchapter-D/part-435",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "Contribution Before Conversion",
        "subtitle": (
            "Underwrite landed cost, fulfillment, payment fees, and acquisition "
            "before increasing advertising spend."
        ),
        "audience": (
            "Performance-oriented operators who can reconcile Shopify orders, "
            "3PL invoices, supplier costs, and advertising cohorts."
        ),
        "research_basis": (
            "19 U.S.C. 1484 assigns entry-information and reasonable-care "
            "responsibilities to importers of record. HTS classification and "
            "applicable duties therefore belong in landed-cost underwriting, "
            "rather than a later bookkeeping adjustment. FTC Act Section 5 "
            "provides the consumer-protection basis for scrutinizing product "
            "claims and promotional representations. Neither source validates "
            "the illustrative acquisition costs or modeled retail margins."
        ),
        "sources": [
            "https://www.law.cornell.edu/uscode/text/19/1484",
            "https://hts.usitc.gov/",
            "https://www.law.cornell.edu/uscode/text/15/45",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "Retention Without Inventory Chaos",
        "subtitle": (
            "Connect replenishment messaging, available-to-promise inventory, "
            "order routing, and returns tracking into one operating loop."
        ),
        "audience": (
            "Lean merchants selling replenishable or accessory products with "
            "documented repeat demand and dependable fulfillment partners."
        ),
        "research_basis": (
            "15 U.S.C. 7704 establishes requirements for commercial email, "
            "including accurate transmission information and honoring opt-out "
            "requests. California Civil Code Sections 1798.100 and 1798.140 "
            "supply privacy obligations and applicability definitions for covered "
            "businesses. These sources inform suppression, data minimization, "
            "and retention workflows; repeat-purchase lift still requires "
            "controlled cohort measurement."
        ),
        "sources": [
            "https://www.law.cornell.edu/uscode/text/15/7704",
            (
                "https://leginfo.legislature.ca.gov/faces/"
                "codes_displaySection.xhtml?sectionNum=1798.100.&lawCode=CIV"
            ),
            (
                "https://leginfo.legislature.ca.gov/faces/"
                "codes_displaySection.xhtml?sectionNum=1798.140.&lawCode=CIV"
            ),
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
]


def build_volume_021_diagrams_data() -> list[dict]:
    specs = [
        (
            "diag-01-authorized-retail-operating-loop",
            "process_flow",
            "Route Orders, Not Unresolved Exceptions",
            "A five-stage operating loop for authorized, 3PL-backed retail.",
            1,
            "operating_framework",
            (
                "Stage numbers indicate sequence, not performance estimates. "
                "The merchant sells its own retail inventory; recognized "
                "revenue is retail sales net of refunds, not supplier sales "
                "or payment-processor settlement volume."
            ),
            (
                "Automate routine routing, inventory alerts, and returns "
                "tracking while assigning named owners to stock discrepancies, "
                "unsafe products, and refund exceptions."
            ),
            [
                (
                    "Authorize suppliers and establish product records",
                    "Step 1: document sourcing and landed cost",
                    1.0,
                    (
                        "Collect dealer terms, supplier invoices, SKU identifiers, "
                        "applicable safety evidence, and landed unit costs. "
                        "Reject undocumented sourcing before publishing listings."
                    ),
                ),
                (
                    "Publish inventory with explicit stock buffers",
                    "Step 2: synchronize available-to-promise inventory",
                    2.0,
                    (
                        "Connect Shopify inventory to the 3PL feed; subtract "
                        "reserved, damaged, and quarantined units. Alert the "
                        "operations lead when feed age exceeds the agreed limit."
                    ),
                ),
                (
                    "Capture payment and route eligible orders",
                    "Step 3: release only fulfillable paid orders",
                    3.0,
                    (
                        "Use idempotent order identifiers and payment-status "
                        "checks before 3PL release. Send address failures, "
                        "suspected fraud, and oversells to an exception queue."
                    ),
                ),
                (
                    "Track delivery and close return exceptions",
                    "Step 4: reconcile shipments, returns, and refunds",
                    4.0,
                    (
                        "Match carrier events to orders, investigate stalled "
                        "shipments, and track return authorizations through "
                        "inspection. Reconcile each refund to the original sale."
                    ),
                ),
                (
                    "Replenish selectively and measure retained demand",
                    "Step 5: refresh purchasing and retention decisions",
                    5.0,
                    (
                        "Use sell-through, lead times, and contribution by SKU "
                        "to replenish inventory. Suppress unavailable products "
                        "and opted-out contacts from Klaviyo replenishment flows."
                    ),
                ),
            ],
        ),
        (
            "diag-02-base-retained-buyer-cohort",
            "funnel",
            "A Nested Cohort That Reconciles to Base Revenue",
            "Annual retained purchases, not clicks multiplied across unrelated cohorts.",
            6,
            "illustrative_model",
            (
                "Illustrative annual cohort: every downstream group is a subset "
                "of the preceding group of distinct visitors. Each retained "
                "buyer places exactly one retained order averaging $75 in "
                "recognized sales after refunds, excluding collected sales tax. "
                "Repeat orders are excluded from this simplified model."
            ),
            (
                "15,000 retained orders × $75 = $1,125,000 annual Base revenue. "
                "The modeled 3% visitor-to-retained-buyer conversion is an "
                "assumption to test, not a traffic benchmark."
            ),
            [
                (
                    "Eligible distinct visitors entering the storefront",
                    "500,000 visitors in the annual starting cohort",
                    500000.0,
                    (
                        "Deduplicate measured visitors using an appropriate "
                        "first-party analytics design. Keep acquisition spend "
                        "separate from attribution claims and record measurement limits."
                    ),
                ),
                (
                    "Visitors reaching an eligible product page",
                    "200,000 visitors; 40% of the preceding cohort",
                    200000.0,
                    (
                        "Count only original-cohort visitors viewing stocked, "
                        "purchasable products. Broken variant links and unavailable "
                        "inventory should be diagnosed before increasing spend."
                    ),
                ),
                (
                    "Product viewers adding an item to cart",
                    "40,000 visitors; 20% of product-page viewers",
                    40000.0,
                    (
                        "Measure distinct cart creators rather than add-to-cart "
                        "events. Investigate unexpected shipping charges and "
                        "unclear product compatibility when this transition weakens."
                    ),
                ),
                (
                    "Cart creators beginning the checkout sequence",
                    "25,000 visitors; 62.5% of cart creators",
                    25000.0,
                    (
                        "Restrict checkout starts to the same cart-creator "
                        "cohort. Segment payment failures and address-validation "
                        "friction without double-counting repeated checkout attempts."
                    ),
                ),
                (
                    "Checkout starters retaining one completed purchase",
                    "15,000 buyers; 60% of checkout starters",
                    15000.0,
                    (
                        "Remove canceled and fully refunded purchases; use "
                        "post-refund recognized order value for remaining buyers. "
                        "This final cohort supplies exactly $1,125,000 annual sales."
                    ),
                ),
            ],
        ),
        (
            "diag-03-base-retail-margin-waterfall",
            "waterfall",
            "From $1,125,000 Retail Sales to $129,375 Owner Net",
            "Six bars reconcile the canonical Base-Case 11.5% net margin.",
            3,
            "illustrative_model",
            (
                "USD per year. The first bar is the opening revenue total, "
                "the next four bars are signed expense changes, and the final "
                "bar is the closing total, not an additional change. Canonical "
                "gross revenue means retail sales net of refunds. Expense "
                "allocations are illustrative and include paid pod labor."
            ),
            (
                "$1,125,000 − $540,000 − $135,000 − $180,000 − $140,625 "
                "= $129,375; $129,375 ÷ $1,125,000 = 11.5%. "
                "Collected sales tax is excluded from revenue."
            ),
            [
                (
                    "Opening total: recognized annual retail sales",
                    "$1,125,000 revenue after refunds; 100% of sales",
                    1125000.0,
                    (
                        "Use Shopify order records and accounting adjustments "
                        "to reconcile net retail sales. Do not deduct refunds "
                        "again or substitute net processor deposits for revenue."
                    ),
                ),
                (
                    "Subtract landed cost of goods sold",
                    "−$540,000 annual expense; 48% of recognized sales",
                    -540000.0,
                    (
                        "Include purchase cost, allocated inbound freight, "
                        "applicable duties, and inventory-loss expense. Unsold "
                        "inventory remains an asset until sold or written down."
                    ),
                ),
                (
                    "Subtract fulfillment, payments, and return handling",
                    "−$135,000 annual expense; 12% of recognized sales",
                    -135000.0,
                    (
                        "Include 3PL storage and handling, outbound shipping, "
                        "payment processing, and reverse logistics. Refund "
                        "principal already reduces opening revenue and is not repeated."
                    ),
                ),
                (
                    "Subtract advertising and variable acquisition spend",
                    "−$180,000 annual expense; 16% of recognized sales",
                    -180000.0,
                    (
                        "Allocate media and directly variable acquisition "
                        "charges here. Retained contribution after these three "
                        "expense bars is $270,000, or 24% of sales."
                    ),
                ),
                (
                    "Subtract labor and remaining operating overhead",
                    "−$140,625 annual expense; 12.5% of recognized sales",
                    -140625.0,
                    (
                        "Budget $96,000 loaded labor for two full-time seats, "
                        "$24,000 for three limited-hour contractors, and $20,625 "
                        "for software, insurance, and remaining overhead. Validate "
                        "local staffing costs; fixed overhead averages $11,718.75 monthly."
                    ),
                ),
                (
                    "Closing total: canonical annual owner net profit",
                    "$129,375 residual profit; 11.5% annual net margin",
                    129375.0,
                    (
                        "This closing bar equals revenue less all four expense "
                        "bars. Paid owner labor, if included in the pod, belongs "
                        "in labor expense; personal tax treatment is not modeled."
                    ),
                ),
            ],
        ),
        (
            "diag-04-subniche-contribution-yields",
            "horizontal_bars",
            "Compare Contribution Yield Before Adding Fixed Overhead",
            "Five illustrative sub-niche and payment-rail combinations.",
            2,
            "illustrative_model",
            (
                "Numeric values are contribution percentages of recognized "
                "retail sales after refunds, not annual net margins. Each "
                "example uses a $100 recognized-sales basis and subtracts "
                "landed goods, fulfillment including return handling, payment "
                "costs, and acquisition. Fixed labor and overhead remain excluded."
            ),
            (
                "These are underwriting examples, not observed category "
                "benchmarks. Payment costs vary by provider, transaction mix, "
                "disputes, and contract; validate the complete order economics."
            ),
            [
                (
                    "Authorized replacement filters through card checkout",
                    "28% contribution; $28 retained per $100 sales",
                    28.0,
                    (
                        "$100 less $42 landed goods, $12 fulfillment, $3 "
                        "payment costs, and $15 acquisition leaves $28. Verify "
                        "compatibility claims and prevent obsolete-model stock accumulation."
                    ),
                ),
                (
                    "Compact repair accessories through card checkout",
                    "24% contribution; $24 retained per $100 sales",
                    24.0,
                    (
                        "$100 less $48 landed goods, $9 fulfillment, $3 "
                        "payment costs, and $16 acquisition leaves $24. This "
                        "cost mix matches Base contribution before fixed overhead."
                    ),
                ),
                (
                    "Bulky organization products through card checkout",
                    "16% contribution; $16 retained per $100 sales",
                    16.0,
                    (
                        "$100 less $45 landed goods, $20 fulfillment, $3 "
                        "payment costs, and $16 acquisition leaves $16. Measure "
                        "dimensional-weight surcharges and damage-driven reverse logistics."
                    ),
                ),
                (
                    "Premium accessories through installment-provider checkout",
                    "22% contribution; $22 retained per $100 sales",
                    22.0,
                    (
                        "$100 less $47 landed goods, $10 fulfillment, $6 "
                        "payment costs, and $15 acquisition leaves $22. Test "
                        "incremental retained purchases rather than assuming financing lifts profit."
                    ),
                ),
                (
                    "Repeat business replenishment through ACH checkout",
                    "36% contribution; $36 retained per $100 sales",
                    36.0,
                    (
                        "$100 less $48 landed goods, $10 fulfillment, $1 "
                        "payment costs, and $5 acquisition leaves $36. Validate "
                        "authorization, settlement timing, return exposure, and repeat demand."
                    ),
                ),
            ],
        ),
        (
            "diag-05-product-and-order-preflight",
            "decision_tree",
            "Four Pre-Flight Checks Before Accepting Orders",
            "Resolve product, customs, tax, and customer-treatment risks.",
            5,
            "operating_framework",
            (
                "Four sequential yes-or-no checks; numeric values indicate "
                "sequence only. A documented pass advances to the next check. "
                "A failed check follows the corrective branch described in "
                "its detail; product category and jurisdiction determine scope."
            ),
            (
                "Use written evidence rather than a single vendor assurance. "
                "After all four checks pass, release only the affected, "
                "documented products and selling destinations."
            ),
            [
                (
                    "Check product safety and supplier traceability",
                    "Check 1: pass documented safety and sourcing requirements",
                    1.0,
                    (
                        "Confirm dealer authorization, applicable testing and "
                        "certificates, and recall screening. Under 15 U.S.C. 2064, "
                        "evaluate immediate reporting duties when hazard information "
                        "arises. Failure routes affected stock to quarantine and review."
                    ),
                ),
                (
                    "Check customs classification and landed import cost",
                    "Check 2: pass importer and duty documentation",
                    2.0,
                    (
                        "Identify the importer of record and verify HTS "
                        "classification, origin, and applicable duties under "
                        "19 U.S.C. 1484. For domestic purchases, retain supplier "
                        "invoices and responsibility records. Failure pauses affected purchasing."
                    ),
                ),
                (
                    "Check sales-tax nexus and collection configuration",
                    "Check 3: pass destination-specific tax setup verification",
                    3.0,
                    (
                        "Review economic and physical nexus, including 3PL-held "
                        "inventory. California Revenue and Taxation Code Section "
                        "6203 illustrates state-specific triggers. Separate marketplace "
                        "collection from direct-store duties; unresolved destinations remain disabled."
                    ),
                ),
                (
                    "Check promises, privacy, and retention messaging",
                    "Check 4: pass customer-facing workflow verification",
                    4.0,
                    (
                        "Test shipping promises and delay handling under 16 CFR "
                        "Part 435, claims under 15 U.S.C. 45, email opt-outs "
                        "under 15 U.S.C. 7704, and applicable California Civil "
                        "Code 1798.100 duties. Failure pauses the affected offer "
                        "or flow until corrected and retested."
                    ),
                ),
            ],
        ),
        (
            "diag-06-core-and-scaled-pod-seats",
            "org_architecture",
            "Five Core Seats, Seven at the Scaled Case",
            "Two full-time operators plus three contractors; add two seats selectively.",
            11,
            "operating_framework",
            (
                "Each numeric value represents one person, not one full-time "
                "equivalent. The first five seats form the Conservative and "
                "Base pod: 2 FT + 3 C. The final two seats expand the Scaled "
                "pod to 3 FT + 4 C. Contractor hours must be budgeted explicitly."
            ),
            (
                "Conservative: $250,000 × 5% = $12,500 owner net. "
                "Base: $1,125,000 × 11.5% = $129,375 owner net. "
                "Scaled: $2,000,000 × 18% = $360,000 owner net. "
                "Scale requires better unit economics, not automation alone."
            ),
            [
                (
                    "Core full-time seat: general manager and merchandising",
                    "Person 1: accountable for purchasing and profit",
                    1.0,
                    (
                        "Own supplier authorization, pricing, purchase commitments, "
                        "and weekly contribution review. Approve reorder quantities "
                        "using lead times, cash availability, and inventory aging."
                    ),
                ),
                (
                    "Core full-time seat: operations and customer experience",
                    "Person 2: accountable for fulfillment and exceptions",
                    1.0,
                    (
                        "Own 3PL service levels, inventory discrepancies, shipment "
                        "delays, and refund resolution. Escalate safety incidents "
                        "and maintain a daily exception backlog with owners."
                    ),
                ),
                (
                    "Core contractor seat: paid acquisition and creative",
                    "Person 3: bounded acquisition and campaign workload",
                    1.0,
                    (
                        "Report contribution by campaign after refunds and "
                        "acquisition costs. Pause deteriorating cohorts and reuse "
                        "approved product evidence when developing advertising claims."
                    ),
                ),
                (
                    "Core contractor seat: automation and retention",
                    "Person 4: bounded integration and messaging workload",
                    1.0,
                    (
                        "Maintain Shopify webhooks, 3PL routing, Klaviyo suppression, "
                        "and return-status synchronization. Test retry behavior "
                        "and duplicate-event handling before publishing workflow changes."
                    ),
                ),
                (
                    "Core contractor seat: bookkeeping and inventory reconciliation",
                    "Person 5: bounded close and reconciliation workload",
                    1.0,
                    (
                        "Reconcile processor settlements, refunds, inventory assets, "
                        "and supplier invoices. Prepare tax-provider handoffs and "
                        "flag unexplained differences before the monthly close."
                    ),
                ),
                (
                    "Scaled full-time addition: inventory and supply planning",
                    "Person 6: added only in the Scaled pod",
                    1.0,
                    (
                        "Take ownership of purchasing forecasts, stock transfers, "
                        "and supplier lead-time variability when these exceed "
                        "the core manager's measured operating capacity."
                    ),
                ),
                (
                    "Scaled contractor addition: customer-support overflow coverage",
                    "Person 7: added only in the Scaled pod",
                    1.0,
                    (
                        "Cover measured ticket peaks and returns administration "
                        "under documented permissions. Keep refund authority, "
                        "product-safety escalation, and customer-data access narrowly assigned."
                    ),
                ),
            ],
        ),
        (
            "diag-07-startup-capital-allocation",
            "stacked_comparison",
            "Allocate Capital Before Funding Advertising Expansion",
            "Four buckets across $30,000, $100,000, and $250,000 startup envelopes.",
            4,
            "illustrative_model",
            (
                "Numeric values encode the $100,000 planning stack in USD. "
                "Each stage also states its $30,000 and $250,000 comparison "
                "allocations. These are startup funding envelopes, not the "
                "Conservative, Base, and Scaled annual revenue scenarios."
            ),
            (
                "Lean: $12,000 + $6,000 + $4,000 + $8,000 = $30,000. "
                "Planning: $40,000 + $20,000 + $15,000 + $25,000 = $100,000. "
                "Expanded: $100,000 + $50,000 + $35,000 + $65,000 = $250,000."
            ),
            [
                (
                    "Opening inventory and supplier purchase commitments",
                    "Lean $12,000; planning $40,000; expanded $100,000",
                    40000.0,
                    (
                        "Fund landed inventory and supplier deposits with "
                        "SKU-level sell-through limits. Keep purchase cash outflow "
                        "separate from cost of goods recognized when products sell."
                    ),
                ),
                (
                    "Acquisition testing and launch creative production",
                    "Lean $6,000; planning $20,000; expanded $50,000",
                    20000.0,
                    (
                        "Release spend in measured cohorts across creative, "
                        "product pages, and paid traffic. Stop additional "
                        "funding when retained-order contribution fails the underwriting target."
                    ),
                ),
                (
                    "Storefront, integrations, and fulfillment onboarding setup",
                    "Lean $4,000; planning $15,000; expanded $35,000",
                    15000.0,
                    (
                        "Budget Shopify configuration, 3PL onboarding, product "
                        "data, routing tests, and returns setup. Separate one-time "
                        "implementation payments from recurring software and service expenses."
                    ),
                ),
                (
                    "Operating liquidity and exception recovery reserve",
                    "Lean $8,000; planning $25,000; expanded $65,000",
                    25000.0,
                    (
                        "Hold cash for settlement delays, replacements, refunds, "
                        "and operating expenses. Against the canonical $4,000–$25,000 "
                        "monthly opex range, the planning reserve alone covers "
                        "approximately 1–6.25 months before replenishment cash needs."
                    ),
                ),
            ],
        ),
        (
            "diag-08-thirty-day-operating-sprint",
            "timeline_roadmap",
            "Thirty Days to a Tested Retail Operating System",
            "Prepare evidence, integrations, and economics before increasing exposure.",
            12,
            "operating_framework",
            (
                "Four milestones cover Days 1–30; numeric values are ending "
                "days. The canonical time to first deal is 2–6 months, so this "
                "sprint establishes readiness rather than assuming revenue "
                "within its first thirty days."
            ),
            (
                "Advance with recorded test results and bounded purchasing. "
                "Unresolved supplier, product-safety, inventory, or margin issues "
                "remain explicit blockers for the affected products or workflows."
            ),
            [
                (
                    "Days 1–7: establish sourcing and unit economics",
                    "Week 1 ends with a documented product shortlist",
                    7.0,
                    (
                        "Obtain dealer terms, sample invoices, applicable safety "
                        "records, and 3PL quotes. Build SKU contribution sheets "
                        "that include duties, shipping, payment costs, returns, "
                        "and explicit acquisition assumptions."
                    ),
                ),
                (
                    "Days 8–14: connect inventory and order routing",
                    "Week 2 ends with repeatable integration test evidence",
                    14.0,
                    (
                        "Configure Shopify and the chosen 3PL integration. Test "
                        "duplicate webhooks, stale inventory, partial shipments, "
                        "payment failures, and address exceptions using test orders "
                        "without uncontrolled customer charges."
                    ),
                ),
                (
                    "Days 15–21: exercise returns and retention workflows",
                    "Week 3 ends with reconciled customer-lifecycle tests",
                    21.0,
                    (
                        "Run return, inspection, refund, delayed-shipment, and "
                        "email opt-out cases. Verify accounting entries and "
                        "suppression behavior; confirm unavailable products cannot "
                        "trigger purchase-focused replenishment messages."
                    ),
                ),
                (
                    "Days 22–30: validate readiness and constrain exposure",
                    "Week 4 ends with a funded operating plan",
                    30.0,
                    (
                        "Review supplier evidence, test results, cash runway, "
                        "and contribution assumptions. If sourcing and readiness "
                        "are complete, authorize a bounded pilot; otherwise "
                        "schedule remediation within the 2–6 month first-deal horizon."
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
