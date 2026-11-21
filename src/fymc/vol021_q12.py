from __future__ import annotations

CHAPTER_12 = {
    "id": "Q12",
    "chapter_id": "Q12",
    "chapter_number": 12,
    "question_number": 12,
    "slug": "first-thirty-day-launch-sprint-kill-fix-scale",
    "question_prompt": "What is the exact Day-1-to-Day-30 execution schedule for launching automated e-commerce, and what quantitative thresholds govern Kill, Fix, or Scale decisions at Day 30/60/90?",
    "kicker": "Q12 / THE BIG MONEY PLAYBOOKS",
    "title": "The First 30-Day Launch Sprint & Kill / Fix / Scale Gates",
    "subtitle": "A Five-Person Shopify and 3PL Sprint: Contribution Underwriting, Dealer Authorization, FTC Shipping Rules, and Evidence-Based Capital Release",
    "layout_template": "thirty_day_plan",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #28, Automated E-Commerce, ranks #21 with a 70/100 "
        "Money-to-Manpower Score. This sprint turns 18 mapped plays into an "
        "accountable launch system for two full-time operators and three "
        "contractors. Days 1–30 establish authorized supply, landed economics, "
        "tested fulfillment, measured acquisition, and automated retention; they "
        "do not compress the stated two-to-six-month first-deal horizon into a "
        "sales promise. Use a $35,000 first-month cash ceiling only against "
        "$60,000 of committed funding, then release further capital against "
        "mature contribution and service evidence. Canonical annual owner "
        "profits remain $12,500 Conservative, $129,375 Base, and $360,000 Scaled. "
        "Day 30/60/90 decisions separate weak economics from insufficient "
        "evidence, with explicit stop conditions for unsafe products, "
        "unauthorized supply, and uncontrolled cash exposure."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$250,000",
            "context": "Annual retail sales net of refunds; goods, fulfillment, and advertising included in margin",
            "note": "5% net margin; $12,500 annual owner net profit; 2 FT + 3 C",
        },
        {
            "label": "Base",
            "value": "$1,125,000",
            "context": "Annual retail sales net of refunds; goods, fulfillment, and advertising included in margin",
            "note": "11.5% net margin; $129,375 annual owner net profit; 2 FT + 3 C",
        },
        {
            "label": "Scaled",
            "value": "$2,000,000",
            "context": "Annual retail sales net of refunds; goods, fulfillment, and advertising included in margin",
            "note": "18% net margin; $360,000 annual owner net profit; 3 FT + 4 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Days 1–7: Underwrite the Assortment Before Committing Inventory",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Day 1 establishes the operating boundary: one domestic market, "
                    "one storefront, one contracted 3PL, and three to five initial "
                    "SKUs from authorized suppliers. Candidate #28 has 18 mapped "
                    "plays; use the following chapter-local execution labels to "
                    "make that coverage actionable without treating them as "
                    "separate businesses. P01 selects the niche; P02 verifies "
                    "dealer authorization; P03 checks product safety; P04 calculates "
                    "landed cost; P05 underwrites contribution; P06 builds product "
                    "pages; P07 configures checkout and tax; P08 integrates the "
                    "3PL; P09 routes orders; P10 monitors inventory; P11 handles "
                    "delivery exceptions; P12 tracks returns; P13 tests paid "
                    "acquisition; P14 captures permissioned email; P15 runs "
                    "retention; P16 reconciles settlements; P17 controls cash; "
                    "and P18 makes portfolio decisions. Assign the commercial "
                    "lead P01–P07, P13, P17, and P18, and the operations lead "
                    "P08–P12, P14–P16. These are the two full-time seats. Three "
                    "contractors provide storefront and tracking implementation, "
                    "creative and lifecycle production, and bookkeeping with "
                    "tax coordination. The 3PL is a contracted service, not "
                    "an invisible internal employee. Keep one shared exception "
                    "queue so contractor handoffs cannot become orphaned work. "
                    "Record a primary owner and backup for every play before "
                    "accepting supplier terms."
                ),
                (
                    "Days 2–4 turn supplier enthusiasm into documentary evidence. "
                    "Obtain a signed authorization identifying permitted channels, "
                    "territories, warranty handling, image rights, and termination "
                    "terms; a distributor invoice alone does not establish every "
                    "resale permission. Match product identifiers to applicable "
                    "test reports and certificates under 15 U.S.C. 2063 and "
                    "16 CFR Part 1110 where certification is required. Avoid "
                    "children's products, ingestibles, batteries, and medical "
                    "claims in this initial assortment unless the team already "
                    "has category-specific expertise and documentation. Record "
                    "lot identifiers and a recall contact, and establish how "
                    "the operator will assess reporting duties under 15 U.S.C. "
                    "2064(b). For imports, identify the importer of record, "
                    "classification, origin, customs value, duties, and broker "
                    "before approving landed cost; 19 U.S.C. 1484 places entry "
                    "responsibilities on the importer. Confirm insurance coverage "
                    "against the actual category, rather than assuming a general "
                    "policy covers every product. On Day 4, obtain a written "
                    "3PL rate card covering receiving, storage, pick fees, "
                    "packaging, dimensional weight, returns, and minimum charges. "
                    "Model the most expensive common shipping zone, not merely "
                    "the warehouse's neighboring ZIP codes. Reject suppliers "
                    "whose lead times or evidence cannot support the published "
                    "customer promise."
                ),
                (
                    "Days 5–7 establish a cash envelope before placing the "
                    "opening purchase order. This illustrative sprint requires "
                    "$60,000 of committed funding, within the candidate's "
                    "$30,000–$250,000 startup range, and caps first-month cash "
                    "commitments at $35,000: $16,000 inventory and inbound freight, "
                    "$12,000 loaded payroll and contractor work, $3,000 advertising, "
                    "$2,000 systems and setup, and $2,000 contingency. The "
                    "noninventory envelope is therefore $19,000, inside the "
                    "stated $4,000–$25,000 monthly operating range, although actual "
                    "accounting classification follows the underlying expense. "
                    "Keep the remaining $25,000 uncommitted; customer receipts "
                    "do not automatically enlarge spending authority. Inventory "
                    "purchases consume cash immediately but become cost of goods "
                    "as units sell, subject to impairment. Obtain real staffing "
                    "quotes: the labor allowance is an assumption, not evidence "
                    "that every market can supply five people at that cost. "
                    "If loaded staffing exceeds it, revise funding and scope "
                    "before purchase, rather than hiding unpaid owner labor "
                    "inside profit. Stage the inventory commitment with the "
                    "supplier and include cancellation exposure in the cash "
                    "ledger. An operator starting with only $30,000 should "
                    "complete validation and negotiate smaller orders instead "
                    "of attempting this entire funded configuration."
                ),
            ],
            "table": {
                "caption": "Days 1–7: Accountable Underwriting and Purchasing Deliverables",
                "headers": [
                    "Execution day and mapped operating plays",
                    "Accountable owner and concrete assigned work",
                    "Required artifact before the next dependency",
                    "Acceptance test and immediate failure response",
                ],
                "rows": [
                    [
                        "Day 1: Define P01, P17, and P18",
                        "Commercial lead selects one market and initial assortment",
                        "Signed scope sheet names owners for all eighteen plays",
                        "Reject additional channels until first assortment passes underwriting",
                    ],
                    [
                        "Day 2: Establish P02 authorized supply evidence",
                        "Commercial lead requests channel rights and supplier references",
                        "Authorization file matches supplier identity and offered products",
                        "Exclude any SKU with unresolved channel permission restrictions",
                    ],
                    [
                        "Day 3: Complete P03 product safety screening",
                        "Operations lead checks certificates, lots, and recall contacts",
                        "SKU evidence register links applicable certificates and insurance",
                        "Hold purchasing when required safety evidence remains absent",
                    ],
                    [
                        "Day 4: Price P04 landed fulfillment exposure",
                        "Operations lead obtains broker and warehouse written quotations",
                        "Landed cost workbook includes duties and dimensional shipping",
                        "Reprice products whose expensive shipping zones erase contribution",
                    ],
                    [
                        "Day 5: Underwrite P05 contribution by SKU",
                        "Commercial lead models refunds, acquisition, and variable costs",
                        "Versioned unit model separates contribution from owner profit",
                        "Reject products with negative contribution before advertising costs",
                    ],
                    [
                        "Day 6: Fund P17 commitments and staffing",
                        "Commercial lead reconciles committed funding with contractor quotations",
                        "Cash ledger reserves twenty-five thousand dollars outside sprint",
                        "Reduce initial scope if staffing exceeds funded cash capacity",
                    ],
                    [
                        "Day 7: Release staged purchasing through P18",
                        "Both full-time leads review purchase and cancellation exposure",
                        "Signed purchase schedule records quantities and delivery milestones",
                        "Release only inventory supported by accepted product evidence",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four Checks Before the First Irreversible Purchase",
                "body": "Each check needs dated evidence and a named full-time owner; a contractor's verbal assurance is insufficient.",
                "items": [
                    "Match every opening SKU to supplier identity, channel authorization, applicable product certificates, and lot-level traceability.",
                    "Include duties, inbound freight, packaging, dimensional shipping, payment charges, and return handling in the signed unit model.",
                    "Verify $60,000 committed funding, the $35,000 sprint ceiling, and the separate $25,000 reserve before releasing inventory funds.",
                    "Price both full-time seats and all three contractor scopes using actual commitments, with no unrecorded labor subsidy.",
                ],
            },
        },
        {
            "heading": "2. Days 8–14: Prove Checkout, Routing, and Exception Recovery",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Days 8–10 build a narrow transaction path rather than "
                    "a decorative storefront. Use Shopify for catalog and "
                    "checkout, the contracted 3PL's supported connector for "
                    "fulfillment, and QuickBooks Online or Xero for the "
                    "accounting destination; select one accounting system, not "
                    "both. The implementation contractor creates a staging "
                    "checklist while the commercial lead owns prices, product "
                    "claims, shipping promises, and customer-facing policies. "
                    "For every SKU, publish dimensions, compatibility limits, "
                    "warranty route, and realistic dispatch timing. Under "
                    "16 CFR Part 435, maintain a reasonable basis for the "
                    "stated shipping time; if shipment cannot occur as "
                    "promised, follow the applicable delay-notice, cancellation, "
                    "consent, and refund requirements. Do not let a template "
                    "promise same-day shipment when the warehouse cutoff "
                    "makes that impossible. P07 includes determining registration "
                    "obligations from physical presence, inventory location, "
                    "and each destination state's economic nexus rules. "
                    "A tax calculation app does not perform every registration "
                    "or filing duty. The bookkeeping contractor produces a "
                    "jurisdiction worksheet and the commercial lead resolves "
                    "required registrations before affected sales begin. "
                    "Restrict collection of customer data to operational needs, "
                    "configure role-based access, and document the privacy "
                    "requests workflow applicable to the actual business."
                ),
                (
                    "Days 11–12 attack the integration's failure paths. Send "
                    "one normal order, one duplicate event, one cancellation, "
                    "one partial allocation, one address correction, and one "
                    "refund through controlled tests. Shopify webhooks may "
                    "arrive more than once; use the order identifier and "
                    "fulfillment operation as an idempotency key so a retry "
                    "cannot create a second shipment. Authenticate incoming "
                    "events, minimize stored customer fields, and place failed "
                    "messages into a visible retry queue with an assigned "
                    "owner. Distinguish financial authorization, capture, warehouse "
                    "acceptance, label creation, carrier acceptance, and delivery. "
                    "A purchased label is not proof that the parcel entered "
                    "the carrier network. The operations lead reconciles "
                    "available inventory against allocated orders and warehouse "
                    "counts twice daily during launch. Set the reorder point "
                    "from expected daily demand multiplied by replenishment "
                    "lead time, then add explicit safety stock; for two "
                    "units daily, fourteen days of lead time, and ten "
                    "buffer units, the alert triggers at thirty-eight units. "
                    "Keep safety stock separate from sellable stock when "
                    "publishing availability. Never enable uncontrolled backorders "
                    "to conceal a connector delay. Record each test's "
                    "expected state, observed state, timestamp, and recovery "
                    "owner so another person can reproduce the result."
                ),
                (
                    "Days 13–14 prove the customer and accounting loops "
                    "before paid traffic arrives. The operations lead "
                    "creates return reason codes, photographs condition "
                    "standards, and defines who decides restock, refurbish, "
                    "supplier credit, or disposal. P12 must connect a "
                    "return authorization to the original order, physical "
                    "receipt, refund, and inventory adjustment; an email "
                    "thread alone is not a returns ledger. Configure "
                    "Klaviyo or an equivalent lifecycle system for separately "
                    "identified transactional and commercial messages. Under "
                    "15 U.S.C. 7704, commercial email needs accurate routing "
                    "information, appropriate identification, a valid postal "
                    "address, and a functioning opt-out honored within the "
                    "statutory period. Suppress unsubscribed recipients from "
                    "promotional flows while retaining necessary order service "
                    "communications with correctly limited content. The creative "
                    "contractor prepares first-purchase education and replenishment "
                    "messages only where product usage supports them. The "
                    "bookkeeping contractor then reconciles three controlled "
                    "orders across storefront, payment processor, warehouse, "
                    "and accounting records, including fees and one refund. "
                    "Require zero unexplained order-level differences before "
                    "publishing acquisition campaigns. Test orders remain "
                    "excluded from customer conversion and contribution reports. "
                    "Finish the week with a recorded handoff showing how "
                    "either full-time operator can pause ads, disable a "
                    "SKU, and locate a delayed shipment."
                ),
            ],
            "table": {
                "caption": "Days 8–14: Storefront, Warehouse, and Settlement Acceptance Tests",
                "headers": [
                    "Execution day and mapped operating plays",
                    "Accountable owner and concrete assigned work",
                    "Required artifact before accepting live traffic",
                    "Acceptance test and immediate failure response",
                ],
                "rows": [
                    [
                        "Day 8: Build P06 product page evidence",
                        "Commercial lead and implementation contractor publish accurate specifications",
                        "Product pages disclose compatibility, shipping timing, and warranty",
                        "Remove claims unsupported by supplier documentation or testing",
                    ],
                    [
                        "Day 9: Configure P07 checkout and taxation",
                        "Bookkeeping contractor maps nexus while commercial lead resolves registrations",
                        "Jurisdiction worksheet records inventory locations and registration decisions",
                        "Restrict affected destinations until required collection setup works",
                    ],
                    [
                        "Day 10: Connect P08 warehouse fulfillment records",
                        "Operations lead validates warehouse SKU mapping and cutoff",
                        "Connector mapping links storefront variants to warehouse identifiers",
                        "Block unmapped variants rather than accepting unfulfillable orders",
                    ],
                    [
                        "Day 11: Challenge P09 routing with duplicate events",
                        "Implementation contractor tests retries with operations lead observing",
                        "Event log proves duplicate messages create one shipment",
                        "Disable automatic routing if duplicate fulfillment remains possible",
                    ],
                    [
                        "Day 12: Exercise P10 and P11 exceptions",
                        "Operations lead tests stock alerts and delayed parcels",
                        "Exception queue names owners and next customer actions",
                        "Suppress unavailable inventory and correct misleading shipment promises",
                    ],
                    [
                        "Day 13: Connect P12, P14, and P15",
                        "Creative contractor builds lifecycle flows with suppression checks",
                        "Return workflow and commercial email suppression tests pass",
                        "Keep promotional automation disabled until opt-outs propagate correctly",
                    ],
                    [
                        "Day 14: Reconcile P16 controlled transaction evidence",
                        "Bookkeeping contractor ties orders, fees, refunds, and settlements",
                        "Three controlled orders reconcile across all transaction systems",
                        "Exclude test activity and resolve every unexplained difference",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Create a controlled order",
                    "action": "Place a clearly tagged test purchase using the storefront's supported testing method.",
                    "detail": "Record order identifier, expected tax, shipping charge, inventory allocation, and payment state; exclude the transaction from live performance cohorts.",
                },
                {
                    "step": 2,
                    "title": "Replay the fulfillment event",
                    "action": "Submit the same authorized test event twice through the integration test path.",
                    "detail": "Confirm one warehouse order and one inventory allocation; retain the idempotency record and both processing outcomes.",
                },
                {
                    "step": 3,
                    "title": "Exercise cancellation and recovery",
                    "action": "Cancel a separate unshipped test order and simulate a delayed-carrier exception.",
                    "detail": "Verify warehouse cancellation acknowledgment, inventory restoration, assigned customer follow-up, and any required shipping-delay notice.",
                },
                {
                    "step": 4,
                    "title": "Close the transaction ledger",
                    "action": "Trace a refund through processor reporting and the accounting destination.",
                    "detail": "Explain fees, timing differences, and inventory movements; obtain both full-time operators' sign-off before enabling paid acquisition.",
                },
            ],
        },
        {
            "heading": "3. Days 15–21: Buy Measured Evidence Without Buying Uncontrolled Losses",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Days 15–17 release a small acquisition experiment only "
                    "after stock is available and acceptance tests pass. "
                    "The commercial lead selects one paid channel, either "
                    "Google Shopping for existing search demand or Meta "
                    "for demonstrable visual differentiation, rather than "
                    "splitting a small budget across both. Start at "
                    "$100 daily for three days, with the full sprint's "
                    "paid-media commitment capped at $3,000. The creative "
                    "contractor supplies two materially different messages "
                    "for the same qualified audience and landing page; "
                    "changing audience, offer, and page simultaneously makes "
                    "diagnosis ambiguous. Tag campaigns consistently and "
                    "join acquisition source to order identifiers in "
                    "the storefront export. Platform-reported return on "
                    "ad spend remains a diagnostic, not recognized "
                    "revenue or profit. Reconcile attributed purchases "
                    "against paid customer orders and separate existing "
                    "customers from new customers. Calculate acquisition "
                    "cost as channel spend divided by attributable "
                    "new customers, reporting attribution limitations "
                    "explicitly. If there are no customers, report "
                    "spend and zero conversions rather than fabricating "
                    "a cost ratio. Pause a creative after $150 "
                    "without a purchase, inspect the funnel, and "
                    "resume only with a documented correction. This "
                    "is a spend-control rule, not statistical proof "
                    "that the product cannot sell."
                ),
                (
                    "Day 18 replaces attractive dashboard ratios with "
                    "order-level contribution. In the illustrative unit "
                    "model, $110 of merchandise charges less $10 "
                    "of expected refunds produces $100 of net retail "
                    "sales, excluding sales tax. Subtract $40 landed "
                    "product cost, $12 outbound fulfillment and shipping, "
                    "$3 payment fees, and $3 return handling to "
                    "produce $42 of contribution before acquisition, "
                    "called CM1. Subtract $25 acquisition cost to "
                    "produce $17 CM2, or 17% of net sales. "
                    "Return handling is a separate expense, not "
                    "a second deduction of the refunded selling "
                    "price. Replace estimates with actual cohort "
                    "results as returns mature, including inventory "
                    "recovery and nonrecoverable fees. CM2 still "
                    "excludes fixed payroll, software, insurance, and "
                    "other overhead; it is not owner profit. "
                    "At the canonical Base revenue of $1,125,000, "
                    "a hypothetical 17% blended CM2 would yield "
                    "$191,250 before fixed expenses. Reaching the "
                    "canonical $129,375 owner profit would then "
                    "leave only $61,875 for those expenses, a "
                    "tight constraint that must be tested against "
                    "actual staffing. If fixed costs exceed it, "
                    "the model needs better blended contribution, "
                    "not relabeling of payroll. The Scaled 18% "
                    "net margin likewise requires contribution above "
                    "18% whenever fixed costs remain positive."
                ),
                (
                    "Days 19–21 test whether automation reduces work "
                    "without concealing service debt. Inspect every "
                    "late dispatch, stock discrepancy, refund request, "
                    "and delivery exception daily. Measure dispatch "
                    "performance against the published promise using "
                    "orders whose dispatch deadline has elapsed; "
                    "exclude neither difficult destinations nor "
                    "cancelled warehouse mistakes merely to improve "
                    "the rate. Track order accuracy from verified "
                    "picks and customer reports, and keep the "
                    "denominator visible. P15 can test post-purchase "
                    "education and a relevant accessory offer, "
                    "but projected repeat purchases never rescue "
                    "a losing first-order acquisition case. Measure "
                    "repeat contribution only after the repeat "
                    "order settles and its return exposure is "
                    "provisioned. Limit the launch queue to five "
                    "open noncritical exceptions per full-time "
                    "operator and require an initial response "
                    "within one business day. If unresolved work "
                    "exceeds that capacity for two consecutive "
                    "days, pause acquisition expansion and repair "
                    "the dominant failure. Stop paid traffic "
                    "immediately when cumulative observed CM2 "
                    "loss, including refund provisions, reaches "
                    "$750. This acquisition-loss limit sits "
                    "inside, not above, the $3,000 media "
                    "envelope. Neither limit replaces the "
                    "$35,000 total cash ceiling, and favorable "
                    "processor settlements do not authorize "
                    "automatic replenishment spending."
                ),
            ],
            "table": {
                "caption": "Days 15–21: Acquisition, Contribution, and Operator-Capacity Experiments",
                "headers": [
                    "Execution day and mapped operating plays",
                    "Accountable owner and bounded commercial experiment",
                    "Evidence captured with an explicit denominator",
                    "Quantitative stop rule or required corrective action",
                ],
                "rows": [
                    [
                        "Day 15: Start P13 bounded paid acquisition",
                        "Commercial lead releases one hundred dollars daily maximum",
                        "Campaign ledger records spend and attributable new customers",
                        "Keep total sprint media commitments below three thousand",
                    ],
                    [
                        "Day 16: Compare P06 and P13 messages",
                        "Creative contractor changes message while holding audience stable",
                        "Experiment sheet records sessions, purchases, and customer counts",
                        "Pause individual creative after one hundred fifty unconverted dollars",
                    ],
                    [
                        "Day 17: Audit P13 attribution against orders",
                        "Commercial lead joins campaign records to storefront transactions",
                        "Order export separates new customers from existing customers",
                        "Remove test orders and investigate duplicate purchase events",
                    ],
                    [
                        "Day 18: Recalculate P05 and P16 contribution",
                        "Bookkeeping contractor replaces estimated fees with settlement evidence",
                        "Contribution ledger distinguishes net sales, CM1, and CM2",
                        "Stop paid traffic at seven hundred fifty contribution loss",
                    ],
                    [
                        "Day 19: Inspect P10 and P11 fulfillment",
                        "Operations lead reviews every elapsed dispatch deadline",
                        "Service ledger counts eligible orders and missed promises",
                        "Pause expansion when preventable fulfillment failures remain unresolved",
                    ],
                    [
                        "Day 20: Measure P12 and P15 outcomes",
                        "Operations lead and creative contractor inspect returns together",
                        "Cohort report records refund provisions and settled repeat orders",
                        "Exclude projected lifetime value from first-order profitability decisions",
                    ],
                    [
                        "Day 21: Review P17 and P18 capacity",
                        "Both full-time leads count open exceptions and commitments",
                        "Workload board records queue size and response age",
                        "Stop expansion after two days above ten combined exceptions",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Four Ways Experienced Operators Preserve the Experiment",
                "body": "Protect the quality of the evidence before trying to improve the reported conversion rate.",
                "items": [
                    "Ask the 3PL for parcel-level billed dimensions; one oversized carton can destroy the margin that an average shipping quote suggests.",
                    "Keep a separate SKU ledger for returns awaiting inspection so damaged goods cannot silently reappear as available inventory.",
                    "Use an order-level acquisition export alongside platform attribution; duplicate purchase events often look like sudden marketing improvement.",
                    "Negotiate staged supplier releases with written cancellation terms before seeking a lower unit price tied to an oversized opening order.",
                ],
            },
        },
        {
            "heading": "4. Days 22–30 and Day 60/90: Separate Kill, Fix, and Scale Decisions",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Days 22–30 turn the launch into a repeatable "
                    "decision packet. A mature order has passed "
                    "the disclosed return window plus seven days, "
                    "with a minimum observation period of thirty "
                    "days after delivery; maintain additional reserves "
                    "for later disputes and warranty exposure. "
                    "The thresholds below are operating choices "
                    "for this experiment, not scorecard forecasts. "
                    "A fresh store will usually lack mature "
                    "orders on Day 30, and the candidate's "
                    "two-to-six-month first-deal horizon makes a "
                    "pre-revenue checkpoint entirely plausible. Classify "
                    "that condition as Fix: continue bounded "
                    "validation or wait for evidence, without "
                    "calling missing data product failure. For "
                    "each checkpoint, examine the latest ninety "
                    "days of mature orders and require at "
                    "least 100 at Day 30, 200 at "
                    "Day 60, or 300 at Day 90 "
                    "before granting Scale. Require at least "
                    "fifty mature orders within any SKU "
                    "and acquisition segment proposed for expansion. "
                    "Pool only operationally comparable orders, "
                    "and disclose concentration in a single "
                    "product or campaign. These counts are "
                    "minimum evidence floors, not statistical "
                    "certainty. Add a stress calculation with "
                    "acquisition cost increased 20% and net "
                    "sales reduced 5%, holding other unit "
                    "costs constant; stressed CM2 must remain "
                    "positive."
                ),
                (
                    "Apply decisions in a fixed precedence order. "
                    "First, Kill means stop the affected SKU, "
                    "supplier, campaign, or automation path immediately "
                    "for missing required safety evidence, revoked "
                    "authorization, an unresolved serious safety "
                    "signal, or a committed-cash breach. Assess "
                    "reporting and customer remediation separately; "
                    "stopping ads does not resolve an existing "
                    "product hazard. Next, once the evidence "
                    "floor is met, kill an economic test "
                    "when mature CM2 is zero or negative "
                    "after two documented corrective experiments, "
                    "each observed through cohort maturity. "
                    "Before those experiments mature, Fix applies "
                    "and spending remains paused or separately "
                    "bounded. Scale requires mature CM2 of "
                    "at least 8%, 12%, and 15% at "
                    "Days 30, 60, and 90 respectively, "
                    "on-time dispatch of at least 98%, "
                    "verified order accuracy of at least "
                    "99%, unit return rate no greater "
                    "than 8%, and positive stressed CM2. "
                    "Use the same mature cohort for return "
                    "rates and contribution; report counts "
                    "beside percentages. All other outcomes "
                    "are Fix with one owner, one "
                    "specific hypothesis, and a seven-day "
                    "implementation deadline. Reaching that "
                    "deadline proves execution only; it "
                    "does not accelerate the return window. "
                    "Stop the whole venture only when "
                    "the constraint is systemic or "
                    "remaining capital cannot fund a "
                    "credible bounded repair."
                ),
                (
                    "Scale releases controlled increments, not a "
                    "new annual revenue claim. Require unrestricted "
                    "cash to cover at least ninety days "
                    "of committed fixed cash costs plus "
                    "separately reserved taxes, refunds, and "
                    "supplier payables. This reserve test is "
                    "stricter than the initial $25,000 buffer "
                    "and may block expansion until additional "
                    "funding or retained contribution exists. "
                    "With all tests passed, increase paid "
                    "spend no more than 20% per seven "
                    "days and order no more than six "
                    "weeks of forecast demand, adjusted "
                    "for actual lead time. Obtain a "
                    "new dated cash budget for Days "
                    "31–60 and 61–90; the original sprint "
                    "ceiling never silently renews. Keep "
                    "the two-full-time, three-contractor pod "
                    "until sustained workload and contribution "
                    "fund another seat. The canonical "
                    "Scaled configuration is three full-time "
                    "people plus four contractors, seven "
                    "people total, not an unsupported "
                    "five-person staffing promise. Preserve "
                    "the annual scorecard exactly: $250,000 "
                    "net-of-refund retail revenue at 5% "
                    "produces $12,500 owner profit; "
                    "$1,125,000 at 11.5% produces "
                    "$129,375; $2,000,000 at 18% "
                    "produces $360,000. These are complete "
                    "annual scenarios after goods, fulfillment, "
                    "advertising, and operating costs, not "
                    "thirty-day run rates. Archive the "
                    "Day 30 packet with signed decisions, "
                    "evidence links, unresolved assumptions, "
                    "and the next checkpoint date."
                ),
            ],
            "table": {
                "caption": "Days 22–30 Execution Calendar and Day 30/60/90 Decision Thresholds",
                "headers": [
                    "Execution day or dated decision checkpoint",
                    "Required work and explicitly accountable owner",
                    "Evidence threshold or measurable completed deliverable",
                    "Resulting action and controlled capital treatment",
                ],
                "rows": [
                    [
                        "Day 22: Audit P02 and P03 evidence",
                        "Commercial lead rechecks authorization and safety document changes",
                        "Every active SKU retains required evidence and traceability",
                        "Suspend affected listings immediately when required evidence fails",
                    ],
                    [
                        "Day 23: Reconcile P04 and P05 costs",
                        "Bookkeeping contractor compares warehouse invoices with quoted rates",
                        "Actual shipping, storage, fees, and adjustments explain contribution",
                        "Correct pricing or packaging before expanding affected orders",
                    ],
                    [
                        "Day 24: Stress P08 through P11 resilience",
                        "Operations lead rehearses connector failure and manual recovery",
                        "Controlled outage produces no duplicate or lost fulfillment",
                        "Keep acquisition flat until recovery steps are reproducible",
                    ],
                    [
                        "Day 25: Inspect P12 through P15 cohorts",
                        "Operations lead distinguishes mature returns from provisional results",
                        "Cohort ledger shows delivered dates and return-window maturity",
                        "Do not count immature orders toward Scale evidence",
                    ],
                    [
                        "Day 26: Close P16 settlement reconciliation",
                        "Bookkeeping contractor resolves processor and storefront timing differences",
                        "Every material difference has documented cause and resolution",
                        "Hold expansion while unexplained settlement discrepancies remain open",
                    ],
                    [
                        "Day 27: Test P17 downside cash survival",
                        "Commercial lead forecasts commitments under lower sales receipts",
                        "Ledger includes supplier payables, tax reserves, and refunds",
                        "Stop new commitments that would exceed available funding",
                    ],
                    [
                        "Day 28: Assign P18 Kill or Fix experiments",
                        "Both full-time leads classify each SKU and campaign",
                        "Decision sheet records economic evidence and two repair histories",
                        "Pause losing segments while bounded corrective work proceeds",
                    ],
                    [
                        "Day 29: Prepare P18 conditional expansion packet",
                        "Commercial lead drafts next budget without committing expenditure",
                        "Packet includes contribution stress and ninety-day reserve calculation",
                        "Release no additional capital merely because budget exists",
                    ],
                    [
                        "Day 30: Sign the complete eighteen-play review",
                        "Both full-time leads certify evidence and unresolved assumptions",
                        "Archived packet assigns every exception and checkpoint date",
                        "Continue only activities consistent with the signed decision",
                    ],
                    [
                        "Day 30 checkpoint: Apply ordered Kill, Fix, Scale rules",
                        "Kill hard failures; otherwise assess mature evidence first",
                        "Scale requires 100 mature orders and at least 8% CM2",
                        "Missing maturity means Fix; all shared Scale tests apply",
                    ],
                    [
                        "Day 60 checkpoint: Retest economics and repair maturity",
                        "Kill nonpositive mature CM2 after two completed repairs",
                        "Scale requires 200 mature orders and at least 12% CM2",
                        "Intermediate outcomes remain Fix with renewed bounded cash authorization",
                    ],
                    [
                        "Day 90 checkpoint: Validate durable small-team operating capacity",
                        "Kill systemic unfundable economics; preserve independently healthy segments",
                        "Scale requires 300 mature orders and at least 15% CM2",
                        "Increase spend at most 20% weekly after shared tests",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "Automate the repeatable transaction, measure the expensive exception, and scale only the contribution that survives both.",
    "diagram_id": "diag-08",
    "action_checklist": [
        "Assign all eighteen execution plays across two full-time owners and three scoped contractors, with a backup owner for every exception queue.",
        "Complete SKU-level authorization, applicable safety evidence, landed-cost underwriting, and staged purchase terms before releasing inventory funds.",
        "Fund the illustrative $60,000 configuration, enforce the $35,000 first-month commitment ceiling, and preserve the separate $25,000 initial reserve.",
        "Pass checkout, duplicate-event, cancellation, inventory, return, email-suppression, and settlement tests before enabling paid acquisition.",
        "Report mature CM2 separately from owner profit, enforce the $3,000 media ceiling and $750 contribution-loss stop, and retain order-level evidence.",
        "Sign Day 30/60/90 Kill, Fix, or Scale decisions using maturity floors, service thresholds, downside contribution, and the ninety-day cash-reserve test.",
    ],
    "statutory_citations": [
        {
            "title": "16 CFR Part 435 — Mail, Internet, or Telephone Order Merchandise Rule",
            "url": "https://www.ecfr.gov/current/title-16/chapter-I/subchapter-D/part-435",
            "relevance": "Maintain a reasonable basis for shipping promises and implement applicable delay notices, cancellation options, consent procedures, and prompt refunds.",
        },
        {
            "title": "15 U.S.C. 2063 — Product Certification and Labeling",
            "url": "https://www.law.cornell.edu/uscode/text/15/2063",
            "relevance": "Identify applicable certification and testing requirements before listing regulated consumer products and preserve SKU-linked supporting evidence.",
        },
        {
            "title": "16 CFR Part 1110 — Certificates of Compliance",
            "url": "https://www.ecfr.gov/current/title-16/chapter-II/subchapter-B/part-1110",
            "relevance": "Determine the responsible certifying party and required certificate content for covered products, including the operator's role when importing.",
        },
        {
            "title": "15 U.S.C. 2064(b) — Reporting of Substantial Product Hazards",
            "url": "https://www.law.cornell.edu/uscode/text/15/2064",
            "relevance": "Establish escalation procedures for information that may trigger immediate reporting obligations for manufacturers, distributors, or retailers.",
        },
        {
            "title": "19 U.S.C. 1484 — Entry of Merchandise",
            "url": "https://www.law.cornell.edu/uscode/text/19/1484",
            "relevance": "Assign importer-of-record responsibility and exercise reasonable care over entry information, classification, value, and applicable duties.",
        },
        {
            "title": "15 U.S.C. 7704 — Requirements for Commercial Electronic Mail",
            "url": "https://www.law.cornell.edu/uscode/text/15/7704",
            "relevance": "Configure commercial messages with accurate identifying information, a valid postal address, functioning opt-out mechanisms, and timely suppression.",
        },
        {
            "title": "15 U.S.C. 45 — Unfair or Deceptive Acts or Practices",
            "url": "https://www.law.cornell.edu/uscode/text/15/45",
            "relevance": "Substantiate product and advertising claims and keep stated shipping, warranty, refund, and data-handling practices consistent with actual operations.",
        },
    ],
}
