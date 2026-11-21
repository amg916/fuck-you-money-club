from __future__ import annotations

CHAPTER_2 = {
    "id": "Q2",
    "chapter_id": "Q2",
    "chapter_number": 2,
    "question_number": 2,
    "slug": "who-pays-why-they-pay-and-payment-rails",
    "question_prompt": "Who writes the check in enterprise software reselling, what acute financial or statutory pain forces them to pay, and how do funds clear cleanly without circumvention or non-payment?",
    "kicker": "Q2 / THE BIG MONEY PLAYBOOKS",
    "title": "Who Pays, Why They Pay & How the Payment Rail Works",
    "subtitle": "CFO Budget Authority, AWS CPPO and Microsoft CSP Economics, SEC Filing Triggers, FAR Payment Rules, and Collectible Implementation Spreads",
    "layout_template": "executive_summary",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #23, Enterprise Software Reselling, ranks #19 with a 72/100 "
        "Money-to-Manpower Score. This chapter maps nine operator plays: SEC filing "
        "triggers, deal registration, renewal rescue, license reconciliation, AWS CPPO, "
        "Microsoft CSP, implementation milestones, procurement consolidation, and "
        "receivables protection. Buyers pay to preserve operating continuity, eliminate "
        "wasted entitlements, simplify procurement, and satisfy specific contractual or "
        "statutory duties. Payment comes from authorized enterprise budgets, not merely "
        "an enthusiastic technical sponsor. Canonical annual owner profits are $24,000 "
        "Conservative, $196,000 Base, and $500,000 Scaled, on gross license resale and "
        "service billings with vendor costs inside margin. The operator's discipline "
        "is matching authorization, license delivery, acceptance evidence, and collection "
        "timing before assuming an irreversible vendor obligation."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$300,000",
            "context": "Annual gross license resale and service billings; vendor costs included in margin",
            "note": "8% net margin; $24,000 annual owner net profit; 2 FT + 3 C",
        },
        {
            "label": "Base",
            "value": "$1,400,000",
            "context": "Annual gross license resale and service billings; vendor costs included in margin",
            "note": "14.0% net margin; $196,000 annual owner net profit; 2 FT + 3 C",
        },
        {
            "label": "Scaled",
            "value": "$2,500,000",
            "context": "Annual gross license resale and service billings; vendor costs included in margin",
            "note": "20% net margin; $500,000 annual owner net profit; 3 FT + 4 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Identify the budget owner and sell against a dated operating loss",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "The enterprise writes the check, but four different people usually determine "
                    "whether it happens. The CIO or application owner defines the technical outcome; "
                    "the CFO or delegated budget holder authorizes expenditure; procurement negotiates "
                    "the commercial instrument; accounts payable releases an approved liability. A "
                    "security lead may have veto power without spending authority. Map those roles "
                    "before issuing a binding quote, including the legal buying entity, budget code, "
                    "purchase order threshold, authorized signatory, and receiving contact. Ask which "
                    "dated loss the purchase prevents: an expiring identity subscription, an unsupported "
                    "ERP release, duplicate licenses after acquisition, or a migration that otherwise "
                    "requires expensive parallel systems. A $120,000 renewal protecting a system with "
                    "$20,000 weekly disruption exposure has a different decision clock from optional "
                    "analytics. Quantify that exposure with the buyer rather than presenting invented "
                    "savings. Statutory pressure is specific, not universal: a HIPAA business associate "
                    "arrangement under 45 CFR 164.504(e) can require contractual safeguards where the "
                    "implementation involves protected health information. It does not prescribe a "
                    "particular software brand. Sell the documented control and implementation work; "
                    "never imply that a reseller invoice alone satisfies the underlying duty. Record "
                    "whose acceptance permits payment and who substitutes when that person is absent."
                ),
                (
                    "The mapped play sec_edgar_8k_vendor_trigger_arbitrage turns public disclosures into "
                    "timely, evidence-based discovery, not automatic purchasing intent. Monitor SEC "
                    "EDGAR current-filings RSS and available JSON submission records for Form 8-K "
                    "Item 5.02 executive changes, Item 1.01 material agreements, and Item 2.01 completed "
                    "acquisitions. Track Form D filings separately for exempt offering activity; the "
                    "reported amount sold is not proof of unrestricted cash available for software. "
                    "Persist accession number, issuer identifier, filing time, event category, and a "
                    "short commercial hypothesis. An acquisition may create duplicate identity tenants; "
                    "a new CFO may question renewal sprawl. Route a relevant public filing to a "
                    "human-reviewed, sub-hour outreach queue during staffed hours, avoiding sensitive "
                    "personal assumptions. Illustratively, 40 researched events producing eight qualified "
                    "conversations and two $25,000 projects yield $50,000 billings. At $18,000 delivery "
                    "cost per project, contribution is $14,000 before outreach expense and overhead. "
                    "Those are planning assumptions, not measured conversion rates. Enforce a "
                    "five-request-per-second token bucket with an identifying User-Agent, caching, "
                    "and slower retries when requested. For historical lookbacks, mirror available "
                    "SEC nightly bulk ZIP archives rather than repeatedly retrieving individual "
                    "records. Missing event data sends the lead to manual research, not fabricated "
                    "personalization or duplicate automated messages."
                ),
                (
                    "The remaining eight mapped plays are chapter operating mappings, each tied to "
                    "a payer and a measurable spread. Deal registration on $100,000 license billings "
                    "against $82,000 vendor cost leaves $18,000 before other expenses; if protection "
                    "expires, requote instead of assuming exclusivity. Renewal rescue at $60,000 less "
                    "$54,000 acquisition cost leaves $6,000, but an unconfirmed cancellation window "
                    "requires written vendor clarification. License reconciliation charges $6,000 for "
                    "documenting 100 removable seats at $30 monthly, supporting $36,000 annualized "
                    "buyer savings only when contract terms permit removal. AWS CPPO on $100,000 "
                    "billings with $85,000 wholesale cost and an assumed $2,000 applicable marketplace "
                    "charge leaves $13,000; substitute actual fee terms before quoting. Microsoft CSP "
                    "billings of $36,000 against $31,680 distributor cost leave $4,320 before support. "
                    "Implementation milestones produce $12,000 contribution on $30,000 fees and "
                    "$18,000 delivery cost. Procurement consolidation earns a separately contracted "
                    "$9,000 service fee against $4,000 administration cost. Receivables protection "
                    "preserves cash through deposits, limits, or selective funding; a $1,500 funding "
                    "charge reduces a $10,000 deal contribution to $8,500. None of these deal spreads "
                    "equals annual owner profit. Where authority, eligibility, or acceptance fails, "
                    "pause the affected commitment while preserving separately authorized discovery work."
                ),
            ],
            "table": {
                "caption": "Nine Mapped Plays: Economic Buyer, Collectible Deliverable, and Failure Fallback",
                "headers": [
                    "Mapped play and operating scope",
                    "Budget owner and acute buying pain",
                    "Billable evidence and unit economics",
                    "Failure fallback before committing supplier cash",
                ],
                "rows": [
                    [
                        "sec_edgar_8k_vendor_trigger_arbitrage: public filing signals for timely executive discovery",
                        "New finance or technology leadership confronting acquisition integration costs",
                        "Two accepted projects generate $50,000 billings against $36,000 delivery",
                        "Throttle SEC retrieval and mirror available nightly historical archives",
                    ],
                    [
                        "Deal registration protection for qualified enterprise license opportunities",
                        "Procurement director seeking accountable pricing and an authorized supplier",
                        "Registered $100,000 transaction less $82,000 vendor acquisition cost",
                        "Obtain registration extension or rebuild pricing before quote acceptance",
                    ],
                    [
                        "Renewal rescue for subscriptions approaching contractual notice deadlines",
                        "Application owner preventing entitlement interruption during budget negotiations",
                        "Verified $60,000 renewal less $54,000 supplier purchase obligation",
                        "Confirm cancellation rights before promising any renewal cost reduction",
                    ],
                    [
                        "License reconciliation for provably removable duplicate enterprise seats",
                        "Finance controller reducing documented waste without breaking employee access",
                        "Charge $6,000 against contractually realizable $36,000 annualized savings",
                        "Separate usage findings from savings blocked by commitment terms",
                    ],
                    [
                        "AWS CPPO execution for eligible channel partner private offers",
                        "Cloud budget owner preferring consolidated eligible marketplace purchasing",
                        "$100,000 less $85,000 wholesale and assumed $2,000 platform charges",
                        "Reprice using actual offer eligibility and marketplace fee allocation",
                    ],
                    [
                        "Microsoft CSP management for supported enterprise subscription estates",
                        "IT director requiring subscription administration and accountable support ownership",
                        "$36,000 annual billings less $31,680 distributor acquisition costs",
                        "Require advance funding when customer terms exceed distributor credit",
                    ],
                    [
                        "Implementation milestones for bounded migration and integration deliverables",
                        "Transformation sponsor needing verified functionality by a dated cutover",
                        "$30,000 accepted service fees less $18,000 direct delivery costs",
                        "Split disputed deliverables and collect accepted undisputed milestone amounts",
                    ],
                    [
                        "Procurement consolidation through separately contracted subscription administration services",
                        "Procurement leader reducing fragmented invoices and recurring renewal coordination",
                        "$9,000 service fee less $4,000 attributable administration costs",
                        "Exclude unassigned licenses and suppliers outside documented service scope",
                    ],
                    [
                        "Receivables protection through deposits credit limits and selective funding",
                        "Reseller treasury protecting supplier payments against customer collection delays",
                        "$10,000 contribution becomes $8,500 after $1,500 funding expense",
                        "Shorten terms or decline unfunded incremental customer credit exposure",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Win the buying event without confusing influence with authority",
                "body": (
                    "Veteran operators make the commercial evidence portable across the "
                    "sponsor, procurement desk, receiving team, and payable ledger."
                ),
                "items": [
                    "Save the EDGAR accession and specific event excerpt in CRM; connect the event to one verifiable software problem rather than sending a generic executive-change pitch.",
                    "Ask procurement for its supplier onboarding checklist before the final quote; an approved technical evaluation does not create an active payable vendor record.",
                    "Calendar deal-registration expiry, customer notice deadlines, and distributor commitment dates separately; the earliest irreversible obligation drives funding decisions.",
                    "Have the buyer's cloud billing owner validate the exact purchasing account and private-offer eligibility before promising marketplace consolidation or commitment consumption.",
                ],
            },
        },
        {
            "heading": "2. Choose the settlement structure before accepting the vendor obligation",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Separate the payment rail from the commercial funding structure. Wire and ACH "
                    "move money; escrow, retainers, factoring, and milestone holds allocate timing "
                    "or counterparty risk. Marketplace checkout combines contractual routing with a "
                    "platform collection process. Statutory disbursement describes a governed payment "
                    "process, not an independent bank network. Start every deal with a funds-flow "
                    "schedule naming customer, reseller, software publisher, distributor, marketplace, "
                    "and any financing provider. Show who invoices whom, who owes tax, who advances "
                    "supplier cost, when entitlement activates, and what evidence releases funds. A "
                    "customer purchase order is an instruction under its procurement process, not "
                    "cash or a bank undertaking. For a $120,000 annual license with $102,000 supplier "
                    "cost, supplier terms of net fifteen and buyer terms of net sixty create a "
                    "forty-five-day financing gap if both invoices start together. A $60,000 advance "
                    "still leaves $42,000 of supplier cost temporarily unfunded, before taxes and "
                    "operating costs. Reserve that liquidity or negotiate aligned terms. Confirm "
                    "beneficiary changes through an independently sourced telephone number, require "
                    "dual release for outbound wires, and retain the verification record. Invoice "
                    "bank instructions alone are inadequate protection against compromised email "
                    "threads, especially when a genuine purchase order gives fraudulent instructions "
                    "an appearance of legitimacy."
                ),
                (
                    "For AWS channel partner private offers, confirm the selling authorization, "
                    "buyer account, eligible product, offer duration, wholesale economics, and "
                    "disbursement treatment in the actual marketplace records. Do not assume the "
                    "buyer accepting an offer causes immediate cash settlement to the reseller. "
                    "Reconcile acceptance, invoice, customer collection, adjustments, and payout "
                    "as separate events. A $100,000 offer may carry channel economics very different "
                    "from the cash deposited after publisher allocations, fees, taxes, and credits. "
                    "Microsoft CSP is another specific channel structure, not a synonym for every "
                    "Microsoft marketplace private offer. Under an indirect arrangement, the "
                    "distributor relationship can leave the reseller owing subscription charges "
                    "before the enterprise customer pays. New Commerce Experience cancellation "
                    "windows and term commitments must be checked for the particular subscription "
                    "and current program rules; monthly billing does not automatically create "
                    "monthly cancellation rights. Where a buyer wants escrow, obtain written release "
                    "criteria that match license provisioning and vendor payment deadlines. Otherwise "
                    "money can sit safely with an escrow agent while the reseller defaults on an "
                    "unconditional supplier invoice. A cash retainer for support also needs a clear "
                    "drawdown ledger and replenishment rule; calling it a retainer does not explain "
                    "whether it buys availability, prepays hours, or remains refundable."
                ),
                (
                    "Government buyers require a different collection map. Under applicable federal "
                    "contract clauses, a proper invoice, satisfactory performance, and receiving "
                    "documentation drive payment timing; FAR 32.905 and FAR 52.232-25 provide concrete "
                    "requirements and due-date mechanics. The Prompt Payment Act, including "
                    "31 U.S.C. 3902, addresses interest on qualifying late payments, but it does "
                    "not supply working capital while acceptance or invoice defects remain unresolved. "
                    "Identify the contracting officer, authorized receiving official, designated "
                    "billing office, and required invoice submission system. A program manager's "
                    "enthusiasm cannot substitute for contractual authority. For commercial accounts, "
                    "ACH debit requires appropriate authorization and creates return exposure; ACH "
                    "credit shifts initiation to the buyer but still needs reliable remittance "
                    "matching. Wires reduce some collection delays without eliminating fraud or "
                    "recall issues. Factoring converts eligible invoices into earlier liquidity, "
                    "subject to assignment rights, dilution reserves, recourse, and concentration "
                    "limits. On a $100,000 invoice, an illustrative 85% advance produces $85,000 "
                    "initial cash; a $3,000 fee leaves $12,000 reserve release if the customer pays "
                    "in full and there are no other deductions. That $3,000 is expense, not a "
                    "reduction in customer purchasing volume. Compare all structures using net "
                    "cash dates, enforceable release conditions, and the maximum exposed supplier balance."
                ),
            ],
            "table": {
                "caption": "Eight Payment and Settlement Structures Compared by Authority, Finality, and Failure Mode",
                "headers": [
                    "Rail or settlement structure",
                    "Who authorizes and releases customer funds",
                    "Timing and economic treatment to model",
                    "Control against loss or payment delay",
                ],
                "rows": [
                    [
                        "Bank wire for verified enterprise invoice settlement",
                        "Customer treasury releases funds through authorized banking signers",
                        "Track actual bank receipt rather than emailed transfer confirmations",
                        "Independently verify beneficiaries and investigate mismatched originating customer names",
                    ],
                    [
                        "Escrow account with contractually defined release conditions",
                        "Named escrow agent releases funds under agreed documentary instructions",
                        "Supplier obligations may mature before escrow conditions permit release",
                        "Align provisioning evidence with release tests and dispute deadlines",
                    ],
                    [
                        "ACH credit or expressly authorized commercial ACH debit",
                        "Customer treasury initiates credit or authorizes permitted debit collection",
                        "Model processing windows and returns separately from invoice due dates",
                        "Preserve authorization records and reconcile returns before expanding exposure",
                    ],
                    [
                        "Cash retainer supporting defined recurring services or hours",
                        "Customer budget holder approves deposit under signed service terms",
                        "Maintain advance balance separately from earned service revenue recognition",
                        "Define drawdowns replenishment deadlines refund rights and service suspension",
                    ],
                    [
                        "Statutory disbursement through applicable government contract payment processes",
                        "Authorized agency offices validate invoices and evidence satisfactory performance",
                        "Payment timing depends on governing clauses and proper invoice receipt",
                        "Use correct contract identifiers receiving reports and designated submission systems",
                    ],
                    [
                        "Platform checkout for eligible cloud marketplace private offers",
                        "Authorized buyer account accepts offer under applicable platform permissions",
                        "Acceptance collection allocation and reseller payout remain distinct events",
                        "Reconcile offer identifiers settlement reports fees credits and adjustments",
                    ],
                    [
                        "Factoring eligible receivables under an executed funding agreement",
                        "Factor advances cash after validating assignability debtor and invoice",
                        "Deduct funding fees reserves and recourse exposure from contribution",
                        "Confirm assignment restrictions dispute status and customer notification requirements",
                    ],
                    [
                        "Milestone holds against objectively testable implementation delivery stages",
                        "Designated customer acceptor authorizes release following documented milestone completion",
                        "Retained amounts remain exposed until specified release conditions occur",
                        "Define test scripts review periods cure procedures and partial payment",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Draw the legal and cash counterparties",
                    "action": "Record every invoicing entity, recipient account, supplier obligation, and contractual payer.",
                    "detail": "Attach the customer purchase order, reseller authorization, distributor terms, and marketplace offer identifiers to one transaction record.",
                },
                {
                    "step": 2,
                    "title": "Calculate the peak funding deficit",
                    "action": "Schedule customer deposits, supplier payments, taxes, platform settlements, and expected collections by date.",
                    "detail": "Stress collections by an additional thirty days and require committed liquidity for the resulting maximum cumulative cash shortfall.",
                },
                {
                    "step": 3,
                    "title": "Bind acceptance to release evidence",
                    "action": "Specify license provisioning records or implementation tests that make the invoice payable.",
                    "detail": "Name the authorized acceptor and substitute, define the review period, and separate undisputed charges from contested work.",
                },
                {
                    "step": 4,
                    "title": "Reconcile receipt before closing the transaction",
                    "action": "Match bank or platform settlement to invoice lines, taxes, credits, fees, and retained balances.",
                    "detail": "Escalate unmatched deductions and keep supplier liabilities visible even when the customer invoice shows a partial payment.",
                },
            ],
        },
        {
            "heading": "3. Protect the fee with authorization, evidence, and counterparty credit limits",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Fee protection starts with a valid right to sell, not a sweeping "
                    "noncircumvention paragraph. Verify reseller authorization for the product, geography, "
                    "customer segment, and channel route; save the publisher or distributor evidence "
                    "with its expiry date. Register the opportunity where the program permits and "
                    "document named account, scope, renewal ownership, protected pricing, and any "
                    "conditions that remove protection. A registration may protect a discount "
                    "without preventing the publisher from selling directly. Put discovery and "
                    "implementation fees in a signed statement of work so useful labor is not "
                    "contingent on winning the license order. For example, a $4,000 assessment with "
                    "$2,000 delivery cost contributes $2,000 even when the buyer later chooses a "
                    "different license channel, provided the assessment is independently contracted "
                    "and delivered. Define treatment of that fee if a later project includes a "
                    "credit, preventing double counting. Narrow any noncircumvention provision to "
                    "identified introductions, a reasonable period, and a defined economic remedy "
                    "reviewed for enforceability. Do not use it to obstruct a customer's existing "
                    "publisher relationship. Where the channel agreement prohibits particular "
                    "markups, assignments, or subcontracting, redesign the service scope rather "
                    "than concealing compensation in an inaccurate invoice description. Make "
                    "renewal handover duties explicit before the first subscription starts."
                ),
                (
                    "Credit screening measures the legal customer's ability and willingness to pay, "
                    "not the prestige of its logo. Confirm entity registration, purchasing address, "
                    "tax documentation where required, and whether the purchase order issuer matches "
                    "the contracting party. A subsidiary is not its parent; a brand name does "
                    "not create a parent guarantee. Use commercial bureau reports, customer-authorized "
                    "trade references, filed accounts, and public insolvency records as complementary "
                    "evidence. For public issuers, compare cash, operating cash flow, debt maturities, "
                    "and going-concern disclosures with the proposed obligation. For private issuers, "
                    "a Form D filing is an event signal, not a substitute for current liquidity "
                    "evidence. Establish a credit limit covering unpaid invoices plus committed "
                    "supplier charges that cannot be canceled, less genuinely available deposits. "
                    "A customer with $40,000 unpaid invoices and a new $70,000 irreversible supplier "
                    "commitment creates $110,000 exposure before an applicable $30,000 deposit reduces "
                    "it to $80,000. Do not subtract expected marketplace payouts that are already "
                    "pledged or unresolved. Reassess limits after repeated short payments, ownership "
                    "changes, invoice disputes, or material deterioration. A profitable order that "
                    "exceeds available liquidity should move to advance payment, a smaller phase, "
                    "or a separately approved credit facility rather than automatic fulfillment."
                ),
                (
                    "Disputes become expensive when the record proves activity but not acceptance. "
                    "Create an evidence packet containing executed terms, approved quote, purchase "
                    "order, vendor order confirmation, tenant or entitlement identifiers, delivery "
                    "notice, acceptance tests, and invoice submission receipt. Do not include "
                    "administrator passwords or unnecessary production data. For implementation, "
                    "define a test such as fifty pilot identities authenticating through the agreed "
                    "provider with documented rollback, instead of an ambiguous promise that "
                    "integration will be satisfactory. Route scope changes to priced change orders "
                    "before performing extra work. If $8,000 of a $30,000 milestone is disputed, "
                    "the agreement should support collection of the $22,000 undisputed portion "
                    "rather than freezing the entire project. Suspension rights need notice, "
                    "contractual authority, and product-specific feasibility; a reseller should not "
                    "disable critical access merely because an internal receivables report is "
                    "overdue. For public receivables, assignment can trigger federal requirements "
                    "including 31 U.S.C. 3727 and FAR Subpart 32.8, so obtain specialist review "
                    "before promising collateral to a factor. State-enacted UCC Article 9 may "
                    "govern security interests in commercial receivables, but perfection does "
                    "not repair a defective invoice or eliminate the customer's valid contractual "
                    "defenses. Preserve the operational record that makes the receivable worth financing."
                ),
            ],
            "table": {
                "caption": "Counterparty Credit and Collection Evidence: Six Checks Before Irreversible Commitment",
                "headers": [
                    "Credit or authority test",
                    "Evidence the operator must actually collect",
                    "Specific failure that threatens collectible revenue",
                    "Action that reduces the exposed balance",
                ],
                "rows": [
                    [
                        "Confirm the exact contracting customer legal entity",
                        "Match registry record signed agreement and purchase order issuer",
                        "Well-known parent branding masks an undercapitalized purchasing subsidiary",
                        "Obtain enforceable additional support or collect sufficient advance funds",
                    ],
                    [
                        "Verify delegated spending and invoice acceptance authority",
                        "Obtain procurement routing and named authorized acceptance personnel",
                        "Technical sponsor orders work outside their actual spending delegation",
                        "Wait for valid execution before placing irreversible supplier orders",
                    ],
                    [
                        "Evaluate current liquidity beyond financing announcement headlines",
                        "Review available accounts cash flow references and bureau information",
                        "Reported capital raising obscures restricted cash or severe obligations",
                        "Reduce unsecured terms and separate implementation into funded stages",
                    ],
                    [
                        "Measure total exposure including uncancelable future supplier charges",
                        "Combine receivables aging committed orders deposits and credit utilization",
                        "Unbilled annual commitments remain invisible in the aging report",
                        "Set customer limits using committed exposure rather than invoices alone",
                    ],
                    [
                        "Validate acceptance and invoice submission evidence before collection",
                        "Retain entitlement delivery tests acceptance records and submission receipts",
                        "Customer rejects invoices because receiving records never reached procurement",
                        "Repair documentary defects and pursue undisputed amounts without delay",
                    ],
                    [
                        "Examine assignment restrictions before funding an outstanding invoice",
                        "Review customer contract channel terms and applicable assignment requirements",
                        "Factor advances against receivables subject to unresolved assignment defects",
                        "Use another liquidity source until assignment requirements are satisfied",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four pre-flight checks before the reseller becomes the lender",
                "body": (
                    "Release an irreversible supplier order only when the transaction "
                    "record answers all four questions with current evidence."
                ),
                "items": [
                    "Authorization: Confirm current reseller rights, protected pricing validity, eligible customer account, and an executed order from the actual purchasing entity.",
                    "Liquidity: Calculate peak committed exposure, verify available deposits and credit capacity, and stress the collection date by thirty additional days.",
                    "Acceptance: Name the customer's authorized acceptor, objective delivery evidence, review deadline, and treatment of undisputed invoice lines.",
                    "Settlement: Verify beneficiary details independently and document the actual rail, marketplace payout rules, escrow release terms, or government invoicing requirements.",
                ],
            },
        },
        {
            "heading": "4. Reconcile recognized revenue, supplier cost, and cash into the canonical cases",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Use the scorecard exactly: Conservative is $300,000 gross revenue, 8% net "
                    "margin, and $24,000 annual owner net profit with two full-time people and "
                    "three contractors. Base is $1,400,000 gross revenue, 14.0% net margin, and "
                    "$196,000 owner net profit with the same headcount. Scaled is $2,500,000 "
                    "gross revenue, 20% net margin, and $500,000 owner net profit with three "
                    "full-time people and four contractors. The implied total annual cost envelopes "
                    "are $276,000, $1,204,000, and $2,000,000 respectively. Those envelopes include "
                    "vendor acquisition costs and all other costs assumed by the scorecard; they "
                    "are not spare overhead budgets. As one arithmetic bridge, ten $30,000 "
                    "transactions, twenty $70,000 transactions, and twenty-five $100,000 transactions "
                    "produce the respective revenue totals. These transaction mixes illustrate "
                    "scale, not a claim that every license carries identical economics. Contractor "
                    "counts do not imply full-year utilization, so price delivery hours explicitly. "
                    "The stated $5,000 to $25,000 monthly operating expense range is contextual, "
                    "not an extra deduction after these net profits. Likewise, $25,000 to $150,000 "
                    "startup capital is funding capacity, not revenue. With three to twelve "
                    "months to a first deal, cash runway and supplier-credit headroom must be "
                    "planned separately from the annual profit target."
                ),
                (
                    "The canonical revenue basis is gross license resale and service billings, "
                    "with vendor costs included in margin. Preserve that basis for these scenarios, "
                    "but assess principal-versus-agent treatment for actual financial reporting "
                    "under the applicable accounting framework and contract facts. If a channel "
                    "transaction is only an agency commission, do not inflate revenue with the "
                    "customer's full software purchase. A $100,000 underlying order generating "
                    "a $12,000 agency commission contributes $12,000 revenue before related expenses, "
                    "not $100,000 gross reseller revenue. Conversely, a qualifying principal resale "
                    "at $100,000 with $85,000 vendor cost starts with $15,000 gross spread before "
                    "marketplace fees, delivery, support, selling expense, and overhead. Taxes "
                    "collected for a government, escrow principal held for another party, and "
                    "customer cloud spending outside the reseller's sale are not additional "
                    "operator revenue. Advance cash for an undelivered service is not automatically "
                    "earned revenue. Reconcile each transaction across quote, order, invoice, "
                    "entitlement, supplier bill, bank receipt, and platform settlement using stable "
                    "identifiers. Where platform cash is net of supplier allocations, retain the "
                    "supporting gross-to-net bridge rather than treating the bank deposit as the "
                    "entire economic record. Review credits and cancellation adjustments in the "
                    "same ledger so late reversals cannot silently overstate the month's margin."
                ),
                (
                    "Build the control cadence around the three automation levers: renewal alerts, "
                    "quote generation, and license reconciliation. Renewal alerts should join notice "
                    "deadlines, customer purchase order status, supplier commitment dates, and credit "
                    "limits, not merely send reminders thirty days before expiration. Quote "
                    "generation should pull valid distributor pricing, current authorization, "
                    "currency, tax treatment, payment terms, and service scope into a versioned "
                    "document. License reconciliation should compare purchased entitlements, assigned "
                    "seats, active usage, and contractually available reductions while preserving "
                    "administrator review before changing access. Each week, reconcile marketplace "
                    "settlement exceptions, aging balances, unaccepted milestones, registration "
                    "expiries, and projected supplier payments. At the Base run rate, $1,400,000 "
                    "divided by 365 is approximately $3,836 daily billings; thirty additional "
                    "collection days can tie up about $115,068 if sales are evenly distributed "
                    "and entirely on credit. That is a working-capital sensitivity, not an "
                    "automatic profit loss. A $14,000 credit loss equals one percent of Base "
                    "revenue and would reduce the modeled $196,000 profit to $182,000 unless "
                    "offset elsewhere. Preserve the canonical target while showing that stress "
                    "case separately. Scaling means increasing collected contribution per accountable "
                    "person, not adding unmanaged subscription commitments that make the revenue "
                    "dashboard look larger while treasury runs out of cash."
                ),
            ],
            "table": {
                "caption": "Six Revenue-to-Cash Controls That Preserve the Canonical Profit Cases",
                "headers": [
                    "Ledger or operating control",
                    "Concrete arithmetic or transaction evidence required",
                    "Failure mode that distorts owner economics",
                    "Operator response and durable record",
                ],
                "rows": [
                    [
                        "Conservative annual gross resale and service billing reconciliation",
                        "$300,000 revenue less $276,000 total costs equals $24,000 profit",
                        "Adding supplier costs after net margin double counts expenses",
                        "Maintain one complete cost bridge supporting the eight-percent margin",
                    ],
                    [
                        "Base annual gross resale and service billing reconciliation",
                        "$1,400,000 revenue less $1,204,000 total costs equals $196,000 profit",
                        "Treating gross license spread as owner profit omits operating costs",
                        "Reconcile delivery support selling and overhead within the cost envelope",
                    ],
                    [
                        "Scaled annual gross resale and service billing reconciliation",
                        "$2,500,000 revenue less $2,000,000 total costs equals $500,000 profit",
                        "Assuming more headcount automatically supports the twenty-percent net margin",
                        "Validate workload pricing and contribution for three employees four contractors",
                    ],
                    [
                        "Principal and agent transaction classification before revenue posting",
                        "Separate $100,000 underlying purchase from a $12,000 agency commission",
                        "Counting customer purchasing volume as operator revenue inflates reported scale",
                        "Retain contract analysis and apply the appropriate accounting presentation",
                    ],
                    [
                        "Marketplace gross-to-net settlement reconciliation for every private offer",
                        "Match invoice supplier allocations charges taxes credits and cash settlement",
                        "Booking only bank deposits loses supplier costs and adjustment visibility",
                        "Archive offer identifiers settlement exports and resolved exception evidence",
                    ],
                    [
                        "Working-capital stress monitoring alongside actual credit loss reporting",
                        "Thirty extra Base collection days tie up approximately $115,068",
                        "Confusing delayed cash with expense obscures actual funding requirements",
                        "Forecast liquidity separately and expense actual losses under applicable policy",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "A software order becomes a business only when authority, entitlement, acceptance, and collected cash agree.",
    "diagram_id": "diag-04",
    "action_checklist": [
        "Map the legal buyer, budget holder, procurement signer, receiving official, and payable contact for the next three opportunities.",
        "Build an EDGAR trigger queue with accession-level deduplication, five-request-per-second throttling, human-reviewed outreach, and available nightly bulk archive lookbacks.",
        "Document current reseller authorization, deal-registration expiry, distributor costs, cancellation exposure, and account eligibility before issuing each binding quote.",
        "Create a dated funds-flow schedule comparing supplier commitments with deposits, platform payouts, escrow releases, and customer credit limits.",
        "Attach objective implementation tests, named acceptance authority, invoice submission requirements, and undisputed-payment treatment to every statement of work.",
        "Reconcile gross billings, vendor costs, platform adjustments, cash receipts, and total expenses to the $24,000, $196,000, and $500,000 canonical annual profit cases.",
    ],
    "statutory_citations": [
        {
            "title": "17 CFR 249.308 — Form 8-K for current reports",
            "url": "https://www.ecfr.gov/current/title-17/chapter-II/part-249/section-249.308",
            "relevance": (
                "Establishes Form 8-K as the current-report form; use the official "
                "form instructions to classify executive changes, agreements, and acquisitions."
            ),
        },
        {
            "title": "SEC Form 8-K — Items 1.01, 2.01, and 5.02",
            "url": "https://www.sec.gov/files/form8-k.pdf",
            "relevance": (
                "Provides the primary filing instructions for material agreements, "
                "completed acquisitions or dispositions, and specified leadership changes."
            ),
        },
        {
            "title": "17 CFR 230.503 — Filing of notice of sales",
            "url": "https://www.ecfr.gov/current/title-17/chapter-II/part-230/section-230.503",
            "relevance": (
                "Governs Form D notice filing for specified exempt offerings; reported "
                "offering activity supports research but does not establish customer liquidity."
            ),
        },
        {
            "title": "45 CFR 164.504(e) — Business associate contracts",
            "url": "https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-E/section-164.504",
            "relevance": (
                "Defines business associate contract requirements relevant when authorized "
                "implementation services involve protected health information."
            ),
        },
        {
            "title": "FAR 32.905 — Payment documentation and process",
            "url": "https://www.acquisition.gov/far/32.905",
            "relevance": (
                "Specifies federal payment documentation and proper invoice requirements "
                "that operators must incorporate into their collection evidence."
            ),
        },
        {
            "title": "FAR 52.232-25 — Prompt Payment",
            "url": "https://www.acquisition.gov/far/52.232-25",
            "relevance": (
                "Provides payment due-date and related mechanics when this clause "
                "applies to the federal customer contract."
            ),
        },
        {
            "title": "31 U.S.C. 3902 — Interest penalties",
            "url": "https://www.law.cornell.edu/uscode/text/31/3902",
            "relevance": (
                "Addresses interest penalties for qualifying late federal payments; "
                "interest rights do not replace invoice accuracy or working capital."
            ),
        },
        {
            "title": "31 U.S.C. 3727 — Assignments of claims",
            "url": "https://www.law.cornell.edu/uscode/text/31/3727",
            "relevance": (
                "Restricts assignments of claims against the United States and provides "
                "specified exceptions relevant to financing federal receivables."
            ),
        },
        {
            "title": "FAR Subpart 32.8 — Assignment of Claims",
            "url": "https://www.acquisition.gov/far/subpart-32.8",
            "relevance": (
                "Provides federal contract requirements for qualifying assignments, "
                "including procedures that must be checked before receivables funding."
            ),
        },
    ],
}
