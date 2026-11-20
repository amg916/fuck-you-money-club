CHAPTER_2 = {
    "id": "Q2", "chapter_id": "Q2", "chapter_number": 2, "question_number": 2,
    "slug": "who-pays-billing-rails-and-embedded-fintech",
    "question_prompt": "Who pays, why do they pay, and which payment rails preserve owner profit?",
    "kicker": "Q2 / THE BIG MONEY PLAYBOOKS",
    "title": "Who Pays, Why They Pay & Embedded Fintech Monetization",
    "subtitle": "Departmental Card Budgets vs. Enterprise Procurement, Annual Prepay Cashflow, Merchant-of-Record vs. Stripe & Embedded VCC Interchange",
    "layout_template": "executive_summary", "reading_time_minutes": 14,
    "executive_summary": "Sell a measurable departmental outcome before adding payment revenue. A corporate card can fund a narrow workflow at $99-$499 monthly; cheap prosumers require volume, while enterprise contracts consume sales time and security resources. Choose billing infrastructure by total operating cost, not headline processing fees. Annual prepayment can fund acquisition, but its cash includes future service obligations. Embedded vendor payments add revenue only when suppliers accept cards and the platform actually receives a contractual share. Model subscription billings, inference and hosting costs, payment contribution, labor, and owner profit separately. Money moving through your software is not automatically your revenue.",
    "key_metrics": [
        {"label": "Departmental price", "value": "$99-$499/mo", "context": "Corporate-card workflow", "note": "Buyer limits vary."},
        {"label": "Annual incentive", "value": "10 monthly payments", "context": "Twelve months delivered", "note": "16.7% discount."},
        {"label": "VCC hypothesis", "value": "140-195 bps", "context": "Contract-dependent gross economics", "note": "Not guaranteed platform revenue."},
    ],
    "sections": [
        {
            "heading": "1. Sell to the budget owner, not the largest audience",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                "A departmental buyer pays to remove a recurring queue: invoice exceptions, missed renewals, or document review that blocks revenue. Price the finished workflow at $99-$499 monthly and identify whose corporate card carries the charge. This range can sit below CFO procurement friction, but no universal spending exemption exists. Ask about purchasing limits, data access, and vendor registration during discovery. Demonstrate one completed job using realistic inputs, then measure hours saved against the buyer's existing process. A $299 product that reliably saves ten hours has a clearer purchase argument than an unlimited assistant with no defined output. Capture the budget owner, daily user, renewal date, and measurable success threshold in the account record before celebrating the sale. Those fields explain retention better than signup counts.",
                "The $5 monthly prosumer looks easy to acquire because the purchase decision is small. The economics become difficult when a single support exchange costs more than several months of revenue. At an illustrative $30 loaded hourly support cost, ten minutes consumes the entire monthly bill before payment fees, inference, hosting, refunds, or acquisition. Low prices also attract intermittent usage: customers subscribe for one task and leave. Do not assume a large audience cures this structure. Test repeat use across several billing periods and track support minutes per paying account. If the workflow genuinely belongs to consumers, constrain expensive usage and automate recovery from common failures. Otherwise, package the same capability around a business deadline that supports a higher price and accountable renewal conversation.",
                "An enterprise buyer offering $25,000 or more annually changes the operating model rather than merely increasing revenue per account. A six-month sales cycle involving SOC 2 evidence, security review, procurement, and contract negotiation is a planning scenario, not a mandatory duration or universal certification rule. Count founder selling time and engineering requests against the deal before treating its value as available cash. A small operator can run out of runway while a promising contract waits for a signature. Keep enterprise features separate from the departmental product unless several qualified buyers need them. Request a paid pilot with a defined result and decision date where feasible. Compare cash collected per sales hour across segments; a signed annual commitment does not pay expenses until collection actually occurs."
            ],
            "table": {
                "caption": "Forensic buyer and billing traps",
                "headers": ["Naive Trap", "Detection Metric", "Durable Operator Fallback"],
                "rows": [
                    ["Cheap users mean cheap growth", "Support cost per account", "Price a recurring business outcome"],
                    ["Enterprise pipeline equals cash", "Days to collected payment", "Paid, bounded pilot"],
                    ["Prepay equals profit", "Unserved subscription months", "Reserve delivery cash"],
                    ["Payment volume equals revenue", "Net settled partner share", "Separate settlement ledger"]
                ]
            }
        },
        {
            "heading": "2. Buy the billing responsibilities you actually need",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                "Stripe Billing plus Stripe Tax gives a direct seller subscription tooling and tax calculation capabilities, with available registration and filing services depending on product coverage and configuration. It does not automatically make Stripe the merchant of record for that arrangement. Map who registers, collects, files, remits, refunds, and answers tax notices before comparing prices. Paddle and Lemon Squeezy offer merchant-of-record models for eligible products and supported transactions, typically taking seller-facing responsibility for transaction taxes within their contractual scope. They do not erase your own income taxes, payroll duties, or obligations outside those sales. Compare the complete contract: permitted products, geographic coverage, payout timing, reserves, chargebacks, subscription migration, and customer invoice identity. A lower fee is meaningless if the provider cannot support your specific business model.",
                "Wayfair removed the physical-presence requirement that previously constrained state sales-tax collection duties; it did not declare every SaaS transaction taxable everywhere. State economic-nexus thresholds, taxable product definitions, exemptions, and sourcing rules still matter. Global VAT brings a different jurisdictional map, especially for customer location and business status. Maintain a country and state sales ledger with product classification and customer evidence rather than treating a tax percentage as a complete operating system. Under a merchant-of-record contract, verify which transactions the provider sells and which obligations remain yours. Under direct billing, assign responsibility for registrations and returns explicitly. Review new territories before material sales accumulate. This is a cost allocation decision as much as a tax decision: administrative hours belong in the comparison beside processing and subscription fees.",
                "Run a representative month through both billing models using actual ticket sizes, currencies, refunds, and annual purchases. Separate payment processing, subscription software, tax services, foreign exchange, dispute charges, and internal administration. A merchant-of-record premium may purchase valuable operating capacity for one founder; a mature domestic business may prefer direct control. Do not compare a bundled rate with an unbundled card rate and call the difference pure savings. Test lifecycle behavior as well: a refund must update entitlements correctly, duplicate webhooks must not create duplicate credits, and a failed renewal must enter a recoverable state. Store provider identifiers alongside internal account identifiers so migration remains possible. Export invoices and reconcile payouts monthly. The durable rail is the one whose economics and operational responsibilities remain visible when something fails."
            ]
        },
        {
            "heading": "3. Use annual cash without spending tomorrow's delivery budget",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                "Two months free means charging ten monthly payments for twelve months of service, a 16.7% discount against monthly billing. At $299 monthly, the annual invoice is $2,990 rather than $3,588. Assume illustrative collection costs of 4%, acquisition spending of $600, and inference plus hosting of $35 monthly. Collection leaves $2,870.40; after acquisition and reserving $420 for twelve months of technical delivery, $1,850.40 remains before support, payroll, overhead, refunds, and taxes. That remainder is not owner profit. Annual prepayment creates a negative working-capital pattern when customers pay before delivery costs fall due. It can finance acquisition from customer cash, but only when collection timing, refund exposure, and future service costs support the schedule. A prepaid customer is still owed eleven more months after the first month closes.",
                "Build the cash schedule by acquisition cohort rather than averaging the whole company. Record invoice date, cleared payout date, acquisition cash paid, expected service usage, support allowance, and renewal month. Separate collected cash from revenue earned over the service period; annual prepayment changes cash timing without making twelve months of service immediately delivered. Stress the reserve with twice the expected inference usage and a delayed provider payout. If the business must spend next year's renewal money to serve this year's subscribers, the apparent financing benefit conceals a funding gap. Maintain liquidity for contractual refunds and disputed payments separately from projected growth spending. The useful question is not whether annual customers pay more today, but whether each cohort can fund its remaining promises without requiring another cohort to arrive.",
                "Offer annual billing after the customer sees repeat value, not as camouflage for weak monthly retention. Compare annual renewal behavior with monthly cohorts at equivalent customer ages, and count cancellations even when access continues until the prepaid term ends. Show the total annual charge, renewal timing, and cancellation process clearly at purchase. For online consumer negative-option transactions, 15 U.S.C. section 8403 requires material disclosures before billing information is obtained, express informed consent before charging, and simple mechanisms to stop recurring charges. A business workflow should also make renewal expectations easy to understand, while applicable duties depend on the transaction. Track collected annual cash, remaining delivery obligations, and earned subscription revenue as distinct measures. Avoid rewarding a sales channel merely because it produces a large first invoice followed by expensive refunds."
            ],
            "sop_steps": [
                {"step": 1, "title": "Quote", "action": "Display the annual total.", "detail": "State renewal timing and discount against monthly billing."},
                {"step": 2, "title": "Collect", "action": "Wait for cleared settlement.", "detail": "Record fees, reserves, and payout timing."},
                {"step": 3, "title": "Reserve", "action": "Fund twelve months of delivery.", "detail": "Stress inference, support, and refund assumptions."},
                {"step": 4, "title": "Deploy", "action": "Release only surplus acquisition cash.", "detail": "Reconcile cohort obligations each month."}
            ]
        },
        {
            "heading": "4. Monetize legitimate payment activity, not hidden routing",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                "The b2b_commercial_vcc_interchange_rebate_arbitrage play embeds accounts-payable invoice approval and vendor settlement inside vertical B2B software. Treat 140-195 basis points as a commercial VCC economics hypothesis requiring a written partner offer, not an automatic platform yield. Interchange generally flows to issuers; software earns only the negotiated rebate or revenue share after contractual deductions. Regulation II, 12 CFR Part 235, addresses debit-card interchange and routing; it does not establish a commercial credit-card rebate entitlement. Model eligible settled card spend, supplier acceptance, issuer economics, partner share, reversals, and payment operations separately. A vendor declining cards produces no card revenue, however large its invoice. Keep ACH or another agreed settlement method available. The product earns trust by closing invoices accurately, not by forcing every supplier onto a more expensive rail.",
                "Consider $1 million of monthly invoice opportunities with 40% supplier card acceptance. At an illustrative 170 basis points on $400,000 settled eligible spend, the gross economics pool is $6,800. If the platform contract allocates 50% of that pool to the software business, its revenue is $3,400 before support, reversals, partner charges, or fraud losses assigned by contract. These assumptions are arithmetic, not a market quote. Invoice principal remains settlement volume and never becomes subscription revenue. Confirm who funds the transaction, holds customer funds, underwrites credit, and handles disputes; a software integration does not itself confer those capabilities. Use a partner-provided card token, amount limit, supplier restriction where supported, and expiration. Reconcile invoice, authorization, capture, settlement, and cancellation states before recognizing the share as earned revenue.",
                "The high_risk_payfac_iso_mid_cascading_arbitrage play is best framed here as payment-orchestration and multi-MID routing analytics software for complex merchants. Sell visibility into authorized merchant accounts, processor availability, decline categories, reconciliation gaps, and total acceptance costs. Routing must remain within acquiring agreements and accurate merchant identities; never conceal prohibited activity or send blocked transactions through unrelated accounts. Retry only where network rules and processor guidance permit it, and distinguish technical failures from hard declines. Use idempotency keys and a shared payment state so a timeout cannot trigger two captures through different processors. Attribute revenue lift to settled transactions after refunds and chargebacks, not raw authorization gains. Charge for analytical value or a clearly contracted service fee rather than assuming the software owns processor economics simply because it recommends a route."
            ],
            "callout": {
                "kind": "OPERATOR GATE", "title": "Count only contracted, settled economics",
                "body": "Subscription revenue and payment contribution need separate ledgers.",
                "items": ["Obtain the partner's share formula and exclusions.", "Measure supplier acceptance on actual invoices.", "Exclude invoice principal from company revenue.", "Prevent duplicate captures across processors."]
            }
        },
        {
            "heading": "5. Keep distribution savings separate from owner profit",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                "The web2app_quiz_subscription_billing_bypass play acquires mobile SaaS customers through a useful web onboarding quiz, then collects subscription payment through Stripe or Paddle where platform rules and local requirements permit that journey. The quiz should identify a relevant workflow and lead to an honest product recommendation, not manufacture urgency. A claim of retaining 94% or more assumes total web collection costs at or below 6%; it excludes acquisition, refunds, tax amounts collected for authorities, and delivery costs. The familiar 70% App Store comparison assumes a 30% commission, which is not universal across programs, subscription tenure, regions, or transaction types. Verify the applicable rules before using either number. Web billing changes the collection channel, not the obligation to deliver the mobile experience or provide a functional cancellation path.",
                "At a $20 tax-exclusive subscription, an illustrative 6% web collection cost leaves $18.80 before delivery, while a 30% store commission leaves $14.00. The $4.80 difference is collection contribution, not extra net owner profit. Web acquisition can erase it through lower conversion, additional advertising expense, or customer support needed to connect purchases with app access. Measure the same audience across the full funnel: quiz start, completed checkout, successful account linking, first useful result, refund, and retained paid month. Preserve entitlements across devices with authenticated account mapping rather than trusting an email string supplied by a browser. Validate billing events server-side, deduplicate webhook deliveries, and revoke access according to the actual subscription state. Compare contribution per acquired customer over a consistent horizon instead of promoting the highest checkout retention percentage.",
                "The annual scenarios below are operating targets, not forecasts. Gross means tax-exclusive subscription billings before operating costs; the steady-state illustration assumes billings approximate earned revenue and ignores material deferred-revenue movements. Net owner profit here is the residual before owner income tax, after the listed operating expenses, with founder compensation coming from that residual rather than an additional salary. FT denotes full-time operators and C denotes scoped contractors, not three salaried employees in the smallest case. Conservative economics cannot fund market salaries for that headcount; the founder supplies the full-time work and contractors receive limited project budgets. In scaled operations, paid employee wages must fit inside nontechnical expenses. Embedded payment contribution is excluded from all three cases until validated separately. If founder labor is valued at a market wage, economic profit falls accordingly."
            ],
            "table": {
                "caption": "Illustrative annual subscription economics; dollars, before owner income tax",
                "headers": ["Scenario", "Gross subscription billings", "Inference / hosting COGS", "Other operating expenses", "Net owner profit", "Net margin", "Staffing"],
                "rows": [
                    ["Conservative", "$50,000", "$10,000", "$32,500", "$7,500", "15%", "1 FT + 2 C"],
                    ["Base", "$375,000", "$56,250", "$206,250", "$112,500", "30%", "1 FT + 2 C"],
                    ["Scaled", "$700,000", "$84,000", "$301,000", "$315,000", "45%", "2 FT + 3 C"]
                ]
            }
        },
    ],
    "pull_quote": "The customer pays for a finished workflow; your profit depends on what remains after delivering it, collecting payment, and supporting the next renewal.",
    "diagram_id": "diag-04-billing-rail-take-rates",
    "action_checklist": [
        "Interview five departmental budget owners about purchasing limits.",
        "Measure support minutes and inference cost per paid account.",
        "Price a representative month on direct and MoR rails.",
        "Build a twelve-month prepaid delivery cash schedule.",
        "Obtain written VCC revenue-share and supplier acceptance terms.",
        "Reconcile subscriptions, settlements, and owner labor separately."
    ],
    "statutory_citations": [
        {"title": "South Dakota v. Wayfair, 585 U.S. 162 (2018)", "url": "https://www.supremecourt.gov/opinions/17pdf/17-494_j4el.pdf", "relevance": "Physical presence is not required for sales-tax nexus."},
        {"title": "12 CFR Part 235", "url": "https://www.ecfr.gov/current/title-12/chapter-II/subchapter-A/part-235", "relevance": "Regulation II governs debit interchange and routing, not a commercial credit rebate entitlement."},
        {"title": "15 U.S.C. section 8403", "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title15-section8403&num=0&edition=prelim", "relevance": "Online negative-option sales require material disclosures, informed consent, and simple cancellation mechanisms."}
    ]
}
