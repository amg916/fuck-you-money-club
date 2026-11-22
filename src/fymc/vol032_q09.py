from __future__ import annotations

CHAPTER_9 = {
    "id": "Q9",
    "chapter_id": "Q9",
    "chapter_number": 9,
    "question_number": 9,
    "slug": "contracts-statutory-guardrails-licensing-outreach-scripts",
    "question_prompt": "Which federal/state statutes, licensing boundaries, contract clauses, and compliant outreach scripts govern iso payment processing & atm arbitrage?",
    "kicker": "Q9 / THE BIG MONEY PLAYBOOKS",
    "title": "Contracts, Statutory Guardrails, Licensing & Outreach Scripts",
    "subtitle": "Sponsor-Bank Schedule A Rights, Regulation E ATM Screens, State Surcharge Boundaries, and Disclosed Fintech Referral Economics",
    "layout_template": "legal_compliance_notes",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #32, ISO Payment Processing & ATM Arbitrage, holds Rank #02 of 36 "
        "with a Money-to-Manpower Score of 94/100. Across the volume's 12 mapped plays, "
        "durable earnings depend on enforceable residual rights, accurate merchant pricing, "
        "sponsor-approved underwriting, and disciplined ATM operations. This chapter develops "
        "the supplied fintech co-registration play alongside the contract and statutory "
        "controls supporting ISO and venue portfolios. Canonical annual owner profits are "
        "$27,000 Conservative, $189,125 Base, and $440,000 Scaled. Those results arise from "
        "retained operator revenue, never merchant settlement volume or ATM vault cash. "
        "Use the matrices, discovery scripts, and four-step operating procedure to assign "
        "licensing responsibilities, document fee triggers, preserve transfer rights, and "
        "reject revenue that depends on misleading enrollment or undisclosed debit surcharges."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$90,000",
            "context": "Annual retained ISO residual, gateway markup, and ATM surcharge revenue",
            "note": "30% net margin; $27,000 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Base",
            "value": "$445,000",
            "context": "Annual retained ISO residual, gateway markup, and ATM surcharge revenue",
            "note": "42.5% net margin; $189,125 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Scaled",
            "value": "$800,000",
            "context": "Annual retained ISO residual, gateway markup, and ATM surcharge revenue",
            "note": "55% net margin; $440,000 annual owner net profit; 2 FT + 4 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Draw the Funds-Flow Boundary Before Signing the First Merchant",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Begin with a funds-flow diagram, not a salesperson's description of an ISO. "
                    "Identify the merchant, acquiring bank, processor, gateway, independent sales "
                    "organization, ATM owner, vault-cash provider, and settlement account owner. "
                    "An operator that introduces merchants and receives contractual residuals "
                    "occupies a different perimeter from one accepting customer money and "
                    "forwarding it elsewhere. Under 31 CFR 1010.100(ff), money-transmitter status "
                    "turns on actual activity and applicable exclusions, not the words used in "
                    "a sales agreement. The payment-processor exclusion has specific conditions "
                    "involving goods or services, a clearance and settlement system, and an "
                    "agreement with the seller or creditor; an ISO label alone proves nothing. "
                    "Keep merchant settlement directly between the acquiring arrangement and "
                    "the merchant's designated account. Do not route proceeds through an "
                    "ordinary operating account to simplify reconciliation. A software-only "
                    "gateway may raise different questions from a wallet holding customer "
                    "balances, while state money-transmission definitions and exemptions require "
                    "separate analysis. Obtain the sponsor's written allocation of underwriting, "
                    "monitoring, settlement, reserves, and complaints. Record whether registration "
                    "is with a card network, a federal agency, or a state regulator; these "
                    "are distinct requirements rather than interchangeable badges."
                ),
                (
                    "For a conventional withdrawal ATM, distinguish access to an existing bank "
                    "account from accepting value for transmission. FinCEN guidance FIN-2007-G006 "
                    "explains why the described limited-service ATM activity does not itself "
                    "make the owner a money services business. That conclusion is activity-specific: "
                    "cash deposits, crypto conversion, remittances, or stored-value loading change "
                    "the analysis. Separately, 12 CFR 1005.16 requires an ATM operator imposing "
                    "a covered fee to disclose that a fee will be imposed and its amount "
                    "on screen or paper before the consumer commits, then obtain the consumer's "
                    "election to continue. Federal law no longer requires the former exterior "
                    "fee placard, although contracts or local requirements may add signage. "
                    "Test the actual terminal sequence after every software or surcharge change; "
                    "a photograph of the cabinet cannot establish screen compliance. Keep test "
                    "receipts, firmware identifiers, deployment timestamps, and a documented "
                    "cancel path. Regulation E error-resolution responsibilities under 12 CFR "
                    "1005.11 generally sit with the account-holding institution, but your "
                    "contracts must route retrieval records and complaints promptly. A cash "
                    "dispense reversal, partial dispense, or journal gap should create a "
                    "service ticket before anyone treats the transaction as collectible revenue."
                ),
                (
                    "Treat sponsor-bank underwriting standards as operating obligations even "
                    "where they exceed statutory minimums. The bank's customer identification "
                    "and due-diligence duties under 31 CFR 1020.220 and 1010.230 do not "
                    "automatically become identical direct duties of every referral agent; "
                    "the sponsor agreement determines which collection and verification work "
                    "the ISO performs. Use the sponsor's current checklist because exemptions "
                    "and administrative relief can change required beneficial-owner collection. "
                    "For high-risk MID orchestration, obtain written approval for the actual "
                    "products, websites, owners, fulfillment model, and expected transaction "
                    "patterns. Separate approved business lines only for genuine operating "
                    "reasons, never to conceal common ownership, evade monitoring, or distribute "
                    "prohibited transactions. Mastercard MATCH screening is a network process, "
                    "not a state license, and an unfavorable result requires sponsor-directed "
                    "review rather than identity substitution. OFAC screening, PCI DSS duties, "
                    "and bank risk policies likewise have different legal and contractual "
                    "sources. Record each source, responsible party, evidence requirement, and "
                    "renewal interval in IRIS CRM. If the sponsor declines an activity, stop "
                    "boarding that activity and offer an accurately described permitted alternative. "
                    "Do not promise approval, unrestricted processing, or protection from reserves "
                    "before underwriting is complete."
                ),
            ],
            "table": {
                "caption": "Funds-Flow, Licensing, and Sponsor Responsibility Allocation Matrix",
                "headers": [
                    "Activity and controlling operating boundary",
                    "Primary authority or governing contract source",
                    "Evidence retained before accepting the activity",
                    "Fallback when the boundary is crossed",
                ],
                "rows": [
                    [
                        "Merchant introduction without accepting or forwarding merchant settlement proceeds",
                        "31 CFR 1010.100(ff) definitions plus applicable state transmission statutes",
                        "Signed flow diagram showing direct merchant settlement and residual payment",
                        "Keep settlement with the acquirer while obtaining activity-specific perimeter review",
                    ],
                    [
                        "Payment processing claimed within the federal money-transmitter exclusion conditions",
                        "31 CFR 1010.100(ff)(5)(ii)(B) establishes conditional payment-processor exclusion requirements",
                        "Seller agreement and settlement-system description supporting every applicable exclusion element",
                        "Suspend the expanded service until federal and state treatment is resolved",
                    ],
                    [
                        "Conventional ATM withdrawals accessing customers' existing bank deposit accounts",
                        "FinCEN FIN-2007-G006 addresses the limited ATM activity it describes",
                        "Terminal feature inventory confirming no remittance or stored-value loading functions",
                        "Disable additional features until their separate licensing treatment is established",
                    ],
                    [
                        "ATM surcharge disclosure before the consumer elects to complete withdrawal",
                        "12 CFR 1005.16 governs covered operator fee notice and election",
                        "Timestamped screen sequence showing fee amount and working cancellation path",
                        "Disable surcharge collection or withdraw service until disclosure functions correctly",
                    ],
                    [
                        "Sponsor-directed collection of merchant identity and beneficial ownership records",
                        "31 CFR 1020.220 and 1010.230 inform applicable bank collection duties",
                        "Sponsor checklist version and securely retained merchant verification audit trail",
                        "Request corrected documentation instead of inventing owners or substituting identities",
                    ],
                    [
                        "High-risk merchant boarding under the actual approved business model",
                        "Sponsor underwriting agreement and current Mastercard MATCH participation requirements",
                        "Written category approval linking websites and owners to submitted application",
                        "Decline prohibited activity rather than routing transactions through another merchant",
                    ],
                    [
                        "Merchant settlement complaints and ATM retrieval requests requiring coordinated response",
                        "12 CFR 1005.11 governs covered account institution error-resolution responsibilities",
                        "Contractual response deadlines and complete electronic journal retrieval contact roster",
                        "Escalate promptly to the responsible institution without promising claim outcomes",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four Verifications Before Any Merchant or Terminal Goes Live",
                "body": (
                    "Assign an evidence owner to each check. A sales promise, vendor badge, "
                    "or unsigned application cannot substitute for the underlying record."
                ),
                "items": [
                    "Approve the actual funds-flow diagram with the sponsor, identifying every account owner and documenting the state licensing analysis for any custody or transmission function.",
                    "Match the merchant's owners, websites, product categories, and fulfillment practices to the sponsor's written underwriting approval before enabling production credentials.",
                    "Complete a credit, debit, prepaid, refund, and cancellation test suite for pricing; separately capture the ATM fee screen and consumer continuation sequence.",
                    "Execute the Schedule A, merchant authorization, venue agreement, and data-access terms with named signatories and a dated evidence package in IRIS CRM.",
                ],
            },
        },
        {
            "heading": "2. Contract for Collectible Residuals, Transferable Rights, and Bounded Losses",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Read Schedule A as a calculation specification. Define eligible merchant "
                    "accounts, interchange and network assessments, processor buy rates, gateway "
                    "charges, minimums, chargeback costs, reserve adjustments, and the residual "
                    "split. State whether each percentage applies to merchant volume, gross "
                    "markup, or a specified contribution pool. For illustration, $100,000 in "
                    "monthly merchant card volume multiplied by a 0.40% contractual spread "
                    "creates a $400 pool; a 70% ISO share produces $280 before any "
                    "separately authorized adjustments. The $100,000 is not operator revenue. "
                    "Require merchant-level statements with stable identifiers and enough fields "
                    "to reproduce the calculation, including negative adjustments and their "
                    "original transaction periods. Use IRIS CRM to compare expected residuals "
                    "against remittances, but retain processor exports independently. Specify "
                    "when earned amounts become payable, how long either party may dispute "
                    "calculations, and whether the processor can alter buy rates unilaterally. "
                    "An economically attractive spread is fragile if a general amendment "
                    "clause can erase it without notice. Negotiate prospective notice, a "
                    "documented objection mechanism, and defined treatment of existing merchants. "
                    "For gateway markups, identify who provides the underlying service and "
                    "who bears delivery obligations; that principal-versus-agent analysis matters "
                    "when determining the operator's recognized revenue."
                ),
                (
                    "Protect the asset after termination. Define residual vesting, survival, "
                    "merchant attrition treatment, reassignment, sale rights, successor servicing, "
                    "and the narrow circumstances permitting forfeiture. An anti-circumvention "
                    "clause should cover identified introductions and a reasonable attribution "
                    "period, not claim every business in a region forever. Require a "
                    "cure process for remediable breaches, while allowing immediate action "
                    "for fraud or prohibited processing. Address liability caps, indemnity "
                    "scope, exclusions, defense control, insurance, and dispute resolution "
                    "together: a nominal cap offers little protection if every operational "
                    "error falls into an unlimited exception. For ATM venues, specify "
                    "exclusive placement boundaries, operating hours, electrical and network "
                    "access, relocation rights, servicing access, theft allocation, cash ownership, "
                    "and end-of-term removal. A $3.50 surcharge across 300 completed monthly "
                    "withdrawals creates $1,050 in surcharge receipts. If the venue receives "
                    "$0.75 per completed withdrawal, its $225 allocation leaves $825 before "
                    "processor, connectivity, cash-service, and other expenses; describe this "
                    "contract waterfall before deciding the accounting presentation. Vault cash "
                    "remains a separate balance-sheet asset or provider obligation. If equipment "
                    "or receivables secure an advance, identify collateral precisely and check "
                    "the relevant state's UCC Article 9 attachment, perfection, and priority rules."
                ),
                (
                    "Preserve the canonical scorecard without smuggling client throughput into "
                    "the top line. Formula v2.0 uses $90,000, $445,000, and $800,000 of "
                    "annual retained operator revenue, despite the scorecard's gross-revenue "
                    "label. These amounts already reflect the specified retained-share basis "
                    "for ISO residuals, gateway markups, and ATM surcharges; do not apply "
                    "another blanket residual split. At 30%, 42.5%, and 55% margins, owner "
                    "net profits are exactly $27,000, $189,125, and $440,000. Corresponding "
                    "annual operating costs are $63,000, $255,875, and $360,000. Teams remain "
                    "1 FT plus 3 contractors for Conservative and Base, and 2 FT plus "
                    "4 contractors for Scaled. ASC 606 principal-versus-agent conclusions depend "
                    "on control of each specified service, not simply on which party issues "
                    "an invoice. Reconcile contractual gross billings, pass-through allocations, "
                    "recognized retained revenue, and operating expense in separate ledger "
                    "columns. The stated $1,500–$10,000 monthly opex range is a planning "
                    "reference, not a replacement for these scenario-implied total costs. "
                    "Explain cost categories and stage differences rather than forcing a "
                    "false reconciliation. Bounty cohorts are separate unit illustrations "
                    "unless explicitly incorporated into a revised scorecard; adding their "
                    "receipts to the canonical totals would change the supplied scenarios."
                ),
            ],
            "table": {
                "caption": "Residual Purchase, Merchant Service, and ATM Venue Contract Clause Checklist",
                "headers": [
                    "Clause and precise economic purpose",
                    "Minimum substantive drafting instruction",
                    "Evidence supporting contract administration",
                    "Negotiation fallback preserving operating control",
                ],
                "rows": [
                    [
                        "Scope defines permitted merchant services and authorized venue activities",
                        "List products and territories with explicit exclusions for unsupported services",
                        "Maintain signed schedules connecting each service to its responsible provider",
                        "Restrict launch scope to services the sponsor has expressly accepted",
                    ],
                    [
                        "Fee trigger determines when residuals and bounties become earned",
                        "Specify completed events and adjustment windows with reproducible calculation fields",
                        "Archive settlement reports and attribution records supporting every invoiced amount",
                        "Use monthly verified settlements rather than untestable lifetime revenue promises",
                    ],
                    [
                        "Residual survival preserves earned portfolio economics following ordinary termination",
                        "Separate termination rights from vested residual ownership and transfer permissions",
                        "Retain merchant identifiers and signed amendments documenting each vesting milestone",
                        "Price restricted transfer rights into acquisition value before purchasing accounts",
                    ],
                    [
                        "Anti-circumvention protects named introductions without capturing unrelated market relationships",
                        "Define introduced accounts and reasonable duration with existing relationship exceptions",
                        "Log dated introductions and acknowledge preexisting accounts before outreach begins",
                        "Use an agreed referral tail instead of an unlimited restriction",
                    ],
                    [
                        "Liability caps allocate loss without hiding unlimited contractual exceptions",
                        "Define aggregate limits and targeted exclusions with balanced defense procedures",
                        "Match insurance schedules and incident records to each assumed exposure",
                        "Reject uncapped ordinary service errors or narrow the covered work",
                    ],
                    [
                        "Dispute resolution creates a workable path for residual calculation disagreements",
                        "Set audit rights and escalation periods before specified court or arbitration",
                        "Keep reproducible monthly calculations and written notices of disputed adjustments",
                        "Separate undisputed payments from contested amounts while reviewing source evidence",
                    ],
                    [
                        "IP and data ownership preserve access without claiming unrestricted customer data",
                        "Distinguish software ownership from limited data rights and export obligations",
                        "Maintain access logs and deletion schedules with documented subcontractor permissions",
                        "Require portable merchant metadata while leaving sensitive payment credentials tokenized",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Buy the Payment Waterfall, Not the Sales Deck",
                "body": (
                    "Veteran operators preserve evidence at the same granularity as the fee "
                    "formula. Rights that cannot be reconciled or transferred deserve a lower price."
                ),
                "items": [
                    "Request three actual residual statements and reconstruct ten merchant calculations before accepting Schedule A; include one refund-heavy merchant and one account with negative adjustments.",
                    "Put a successor-servicing and residual-survival clause beside the termination clause, then test what happens if the original salesperson leaves or the ISO entity is sold.",
                    "Write venue commissions against completed, surcharge-bearing withdrawals, explicitly addressing reversals and fee-free transactions before promising the venue a monthly minimum.",
                    "Export merchant identifiers, venue contacts, fee-screen evidence, and residual audit fields monthly; never depend on continued vendor portal access after a contract dispute.",
                ],
            },
        },
        {
            "heading": "3. Engineer State Pricing Rules and Optional Fintech Enrollment",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Build pricing by transaction type and merchant location, not by a "
                    "national sales slogan. A surcharge adds an amount because the customer "
                    "uses an eligible credit card; a genuine cash discount reduces a "
                    "clearly disclosed ordinary price. Calling an added checkout fee a "
                    "discount does not change its mechanics. Visa and Mastercard rules "
                    "prohibit surcharging their debit and prepaid transactions, including "
                    "debit processed without a PIN. Maintain current acquirer-approved "
                    "network caps, notice requirements, receipt fields, and eligible products "
                    "as versioned configuration rather than hard-coded assumptions. Durbin's "
                    "framework in 15 U.S.C. 1693o-2 and Regulation II addresses debit "
                    "interchange, routing, and related network restrictions; it does not "
                    "create universal permission for consumer debit surcharges. New York "
                    "General Business Law 518 requires disclosure of the total credit-card "
                    "price and restricts the surcharge relative to merchant cost. Massachusetts "
                    "General Laws chapter 140D, section 28A prohibits seller credit-card "
                    "surcharges while allowing qualifying discounts. California's surcharge "
                    "statute has important litigation history, so do not treat its printed "
                    "text as a complete enforcement answer. When a location's treatment "
                    "is unresolved, retain ordinary disclosed pricing without a surcharge "
                    "until the applicable state rule and sponsor policy are documented."
                ),
                (
                    "Sector differences can overwhelm a nominally attractive processing spread. "
                    "Recurring subscriptions require a documented authorization path, cancellation "
                    "mechanism, and accurate refund policy; online negative-option offers also "
                    "implicate the Restore Online Shoppers' Confidence Act, 15 U.S.C. 8403. "
                    "Travel, delayed delivery, advance ticket sales, and high-ticket services "
                    "create fulfillment exposure that underwriting may address through reserves "
                    "or delayed funding. Treat sponsor-approved merchant category coding as "
                    "a description of reality, not a way to obtain cheaper risk treatment. "
                    "Verifi RDR and Ethoca integrations can reduce dispute handling, but "
                    "configure refund authority and duplicate-credit protection before enabling "
                    "automated responses. A resolved alert does not erase deceptive sales "
                    "or fix an undisclosed recurring charge. For interstate portfolios, "
                    "record each physical location, checkout channel, customer-facing price "
                    "display, and refund workflow. Test restaurants for tips and split "
                    "tenders, unattended terminals for screen limitations, and ecommerce "
                    "checkouts for debit recognition before the final price appears. If "
                    "the gateway cannot reliably classify a card, do not surcharge that "
                    "transaction. Ask the sponsor which state and network requirements "
                    "apply to the actual arrangement; retain the answer with the deployment "
                    "record. Escalate inconsistent vendor guidance instead of letting each "
                    "sales contractor improvise a different interpretation."
                ),
                (
                    "For free_llc_fintech_bounty_stacking, define the offer as a $0-service-fee "
                    "formation concierge: the founder pays mandatory state filing fees, "
                    "while banking, corporate card, payroll, bookkeeping, and merchant referrals "
                    "remain separately explained choices. The proposed 'Required Business "
                    "Infrastructure Checklist' must distinguish actual statutory requirements "
                    "from optional commercial recommendations; a referred account is not "
                    "legally required merely because it pays a bounty. Disclose material "
                    "referral relationships under the FTC endorsement framework and obtain "
                    "separate authorization before sharing application data. Corporate cards "
                    "remain subject to issuer underwriting, and payroll suitability depends "
                    "on actual employees rather than bounty size. An illustrative ten-founder "
                    "cohort averaging $1,000 in earned CPA awards produces $10,000, within "
                    "the supplied $600–$1,800+ potential per formation. A modeled 15% reversal "
                    "allowance leaves $8,500; $3,000 of attributable acquisition and servicing "
                    "cost leaves $5,500 of cohort contribution, not canonical annual owner "
                    "profit. Prequalify founders for genuine 30-day operating revenue intent, "
                    "without manufacturing activity. If free operating-agreement and bookkeeping "
                    "templates depend on verified bank funding, disclose that separate promotional "
                    "condition upfront and offer an alternative without account enrollment. "
                    "Use minimal verification, not bank passwords, and never withhold purchased "
                    "filing work or required entity documents to force optional referrals."
                ),
            ],
            "table": {
                "caption": "State Pricing, Sector Exposure, and Fintech Bounty Control Matrix",
                "headers": [
                    "Market or workflow requiring separate treatment",
                    "Concrete rule or commercial boundary",
                    "Implementation evidence the operator must retain",
                    "Revenue-preserving fallback without misleading customers",
                ],
                "rows": [
                    [
                        "Visa and Mastercard debit or prepaid cards presented at checkout",
                        "Network rules prohibit surcharges even when debit uses signature processing",
                        "Card classification tests and receipts proving zero debit surcharge assessment",
                        "Use ordinary published pricing when card type cannot be verified",
                    ],
                    [
                        "New York merchant displays and credit-card totals before customer commitment",
                        "General Business Law 518 requires total credit price disclosure and limits",
                        "Menu photographs and checkout captures matching the actual charged total",
                        "Publish clear complete prices rather than adding an unexpected checkout percentage",
                    ],
                    [
                        "Massachusetts seller pricing for credit purchases and genuine cash discounts",
                        "Chapter 140D section 28A prohibits surcharges while permitting qualifying discounts",
                        "Ordinary price displays and discount logic reviewed against the statutory text",
                        "Keep one ordinary price until a qualifying discount design is verified",
                    ],
                    [
                        "California pricing deployment where surcharge text and litigation history interact",
                        "Civil Code 1748.1 requires analysis alongside controlling decisions and current rules",
                        "Dated state analysis and acquirer confirmation for the proposed customer display",
                        "Avoid surcharging while unresolved enforcement and presentation questions are addressed",
                    ],
                    [
                        "Online recurring subscriptions with automatic charges after introductory promotional periods",
                        "15 U.S.C. 8403 requires disclosure and consent plus simple cancellation mechanisms",
                        "Enrollment records and cancellation tests linked to the actual offer version",
                        "Offer a clearly priced one-time purchase while recurring enrollment is repaired",
                    ],
                    [
                        "Optional fintech account referrals embedded in a formation concierge workflow",
                        "FTC Act section 5 and endorsement guidance address deceptive material omissions",
                        "Prominent referral disclosure and separate permissions for each transmitted application",
                        "Offer formation service without claiming optional accounts are legally required",
                    ],
                    [
                        "Promotional templates released after verified funding of an eligible referred account",
                        "Upfront offer terms must explain conditions without overriding promised formation work",
                        "Minimal funding confirmation and sponsor terms defining eligible bounty attribution",
                        "Provide an alternative without enrollment and reject manufactured qualifying activity",
                    ],
                ],
            },
        },
        {
            "heading": "4. Use Verbatim Discovery Scripts and Preserve the Evidence Behind Every Claim",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Open merchant conversations with permission and a bounded claim: 'We "
                    "compare your current statement against a written processing proposal. "
                    "With a redacted statement and your card mix, we can identify "
                    "specific fee differences; we cannot quote your actual savings before "
                    "that review. May I send the comparison checklist?' Follow with "
                    "discovery rather than a surcharge pitch: 'Which states do you sell "
                    "in, what share is debit, do you bill subscriptions, and how "
                    "long after payment do customers receive the product?' Ask for "
                    "masked statements through a secure upload, never full card numbers "
                    "in email. For an ATM venue, use: 'We would propose a defined "
                    "placement area, service responsibilities, and a commission per completed "
                    "surcharge-bearing withdrawal. May we review foot traffic, access hours, "
                    "existing exclusivity, and electrical availability before estimating transactions?' "
                    "Do not convert foot traffic into guaranteed withdrawals. Commercial email "
                    "must follow CAN-SPAM requirements under 15 U.S.C. 7704, including accurate "
                    "headers, nondeceptive subjects, required identification, a valid postal "
                    "address, and a working opt-out honored within the statutory period. "
                    "Business recipients are not a blanket exemption. Keep a suppression "
                    "list shared with authorized sending vendors so an exported lead "
                    "file cannot silently revive an unsubscribed address."
                ),
                (
                    "Use a separate formation disclosure before collecting referral applications: "
                    "'Our formation service fee is $0; you pay the mandatory state "
                    "filing fee. We may receive compensation if you choose eligible "
                    "partner services. Bank, card, payroll, bookkeeping, and processing offers "
                    "are optional, have separate terms, and may require qualification. "
                    "Would you like the formation-only path or the optional referral "
                    "checklist?' Then ask: 'What will the business sell during its "
                    "first 30 operating days, when do you expect the first customer "
                    "payment, and will you actually employ anyone?' This screens fit "
                    "without instructing applicants to fabricate revenue. If a founder "
                    "requests templates, say: 'The promotional template bundle requires "
                    "verified funding of an eligible referred account; the separate "
                    "terms explain the amount and timing. You can choose an alternative "
                    "without opening that account, and your formation documents are "
                    "unaffected.' State the actual funding amount and alternative before "
                    "acceptance. For telephone outreach, evaluate 47 U.S.C. 227, 47 CFR "
                    "64.1200, applicable Telemarketing Sales Rule provisions, and state calling "
                    "laws against the number type, dialing technology, message, and permission "
                    "record. Do not assume that a business purpose permits prerecorded "
                    "calls or marketing texts to a wireless number. Honor internal "
                    "do-not-call requests immediately."
                ),
                (
                    "Make post-sale evidence collection part of the same workflow as "
                    "prospecting. Each accepted proposal should reference its statement analysis, "
                    "pricing version, state review, sponsor approval, executed agreement, and "
                    "first settlement reconciliation. Record call permissions and disclosure "
                    "versions without retaining unnecessary personal data; call recording "
                    "itself requires review of applicable state permission rules. Restrict "
                    "contractor access by role, prohibit local exports of payment credentials, "
                    "and use processor tokens for operational references. Remote ATM telemetry "
                    "should alert on cash levels, communications loss, dispenser faults, "
                    "and unexplained transaction reversals, with an assigned escalation owner. "
                    "Review bounty reversals, merchant attrition, negative residual adjustments, "
                    "and unresolved disputes monthly. If a disclosure defect appears, "
                    "pause the affected campaign or pricing feature, preserve records, "
                    "correct customer-facing materials, and route remediation through the "
                    "responsible provider. Do not erase logs to make conversion metrics "
                    "look cleaner. Close the loop with a measured recovery plan: "
                    "retest the affected terminal or checkout, confirm corrected enrollment "
                    "language, and reconcile any resulting credits. The operator's advantage "
                    "is a repeatable, documented service that survives an audit, staff "
                    "turnover, or portfolio sale. Favor fewer correctly boarded accounts "
                    "over a larger pipeline whose fees, permissions, or residual rights "
                    "cannot be demonstrated."
                ),
            ],
            "table": {
                "caption": "Verbatim Outreach and Discovery Scripts with Evidence-Based Follow-Through",
                "headers": [
                    "Conversation and specific intended operating outcome",
                    "Exact words available for operator use",
                    "Evidence required before the next action",
                    "Fallback when the prospect declines participation",
                ],
                "rows": [
                    [
                        "Initial merchant email requesting permission for a statement-based cost comparison",
                        "'May I send a checklist for a written comparison using your redacted processing statement?'",
                        "Approved email identity and postal address with working unsubscribe functionality",
                        "Honor the opt-out and suppress future campaigns through every sending vendor",
                    ],
                    [
                        "Discovery identifies transaction mix before proposing any merchant pricing changes",
                        "'Which states do you sell in, and what share of your transactions uses debit?'",
                        "Merchant location list and statement evidence supporting the reported card mix",
                        "Offer a standard pricing review without introducing an unverified surcharge program",
                    ],
                    [
                        "Savings discussion prevents unsupported claims from entering the signed merchant proposal",
                        "'We will show the assumptions and fees; actual savings depend on your transaction mix.'",
                        "Reproducible statement comparison including monthly fees and relevant termination costs",
                        "Leave current processing unchanged when documented savings do not justify switching",
                    ],
                    [
                        "ATM venue introduction establishes placement feasibility before projecting transaction volume",
                        "'May we review access hours, existing exclusivity, and service responsibilities before estimating withdrawals?'",
                        "Venue authorization and existing agreement review with a documented placement survey",
                        "Decline conflicting placement rights or propose a later contract renewal discussion",
                    ],
                    [
                        "Formation concierge introduction separates the service offer from optional paid referrals",
                        "'Our service fee is $0; state filing fees apply, and partner account offers are optional.'",
                        "Written state fee disclosure and referral compensation explanation before data sharing",
                        "Provide the formation-only path without pressure to enroll in partner services",
                    ],
                    [
                        "Founder qualification tests genuine operating intent without manufacturing bounty eligibility",
                        "'What will the business sell during its first 30 operating days, and will anyone be employed?'",
                        "Founder-provided business description and actual service needs recorded with permission",
                        "Exclude unsuitable payroll or card offers rather than submitting speculative applications",
                    ],
                    [
                        "Template promotion disclosure explains funding conditions before any optional account enrollment",
                        "'The template promotion has a funding condition; your formation documents do not depend on participation.'",
                        "Exact funding terms and alternative access route delivered before promotional acceptance",
                        "Offer the alternative and never withhold already promised formation deliverables",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Classify the activity and permitted outreach channel",
                    "action": "Create the funds-flow map and record the merchant, venue, or founder's actual operating facts.",
                    "detail": (
                        "Identify applicable states, transaction types, account custody, sponsor duties, "
                        "and outreach permissions. Assign unresolved transmission or calling questions "
                        "to a named reviewer before using the affected activity or channel."
                    ),
                },
                {
                    "step": 2,
                    "title": "Execute the economic and data-rights documents",
                    "action": "Sign the relevant Schedule A, venue terms, referral disclosures, and narrowly scoped data permissions.",
                    "detail": (
                        "Document fee triggers, deductions, residual survival, ownership boundaries, "
                        "liability allocation, dispute procedures, and export rights. Store the "
                        "executed version alongside a reproducible unit-economics worksheet."
                    ),
                },
                {
                    "step": 3,
                    "title": "Test the actual customer-facing implementation",
                    "action": "Run transaction and enrollment tests against the deployed screen, receipt, checkout, and script versions.",
                    "detail": (
                        "Include debit, prepaid, credit, refund, cancellation, ATM fee election, "
                        "and formation-only enrollment paths. Disable any affected feature that "
                        "fails, retain evidence, and repeat the test after correction."
                    ),
                },
                {
                    "step": 4,
                    "title": "Reconcile earned revenue and ongoing exceptions",
                    "action": "Match the first settlement and each monthly residual or bounty statement to its contractual calculation.",
                    "detail": (
                        "Track reversals, credits, attrition, opt-outs, terminal faults, and unresolved "
                        "disputes. Keep customer throughput and vault cash outside operator revenue, "
                        "and compare actual retained earnings against the unchanged canonical cases."
                    ),
                },
            ],
        },
    ],
    "pull_quote": "A payment portfolio is worth the residuals you can reconcile and the rights you can enforce.",
    "diagram_id": "diag-05",
    "action_checklist": [
        "Draw separate merchant, ATM, and fintech referral funds-flow maps; identify custody, settlement ownership, and the federal and state activity boundaries for each.",
        "Reconstruct a Schedule A residual calculation and an ATM venue waterfall from source statements, preserving retained revenue separately from merchant volume and vault cash.",
        "Negotiate fee triggers, residual survival, assignment, anti-circumvention, liability allocation, dispute procedures, and usable data exports before committing acquisition capital.",
        "Build a location-specific pricing register and test credit, debit, prepaid, refunds, and ATM fee disclosures against current sponsor requirements and applicable state law.",
        "Deploy the formation-only enrollment path, referral compensation disclosures, exact promotional funding terms, and minimally intrusive bounty verification without forced account registration.",
        "Load the approved outreach scripts, suppression records, four-step SOP, and monthly exception review into IRIS CRM with named owners and independently retained evidence.",
    ],
    "statutory_citations": [
        {
            "title": "31 CFR 1010.100(ff)(5) — Money transmitter definition and payment-processor exclusion",
            "url": "https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1010/section-1010.100",
            "relevance": "Classify actual acceptance and transmission activity; test each condition of the federal payment-processor exclusion separately from state licensing.",
        },
        {
            "title": "12 CFR 1005.16 — Disclosures at automated teller machines",
            "url": "https://www.ecfr.gov/current/title-12/chapter-X/part-1005/section-1005.16",
            "relevance": "Implement covered ATM fee notice, amount disclosure, and consumer election before completing the withdrawal.",
        },
        {
            "title": "12 CFR 1005.11 — Procedures for resolving errors",
            "url": "https://www.ecfr.gov/current/title-12/chapter-X/part-1005/section-1005.11",
            "relevance": "Allocate supporting journal retrieval and complaint routing without confusing the ATM contractor with the account institution responsible for covered error resolution.",
        },
        {
            "title": "31 CFR 1020.220 — Customer identification programs for banks",
            "url": "https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1020/section-1020.220",
            "relevance": "Understand the sponsor bank's identification framework and document the collection work assigned contractually to the ISO.",
        },
        {
            "title": "31 CFR 1010.230 — Beneficial ownership requirements for legal entity customers",
            "url": "https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1010/section-1010.230",
            "relevance": "Use current sponsor instructions reflecting applicable coverage, exclusions, and relief when collecting ownership information.",
        },
        {
            "title": "15 U.S.C. 1693o-2 — Reasonable fees and rules for payment card transactions",
            "url": "https://www.law.cornell.edu/uscode/text/15/1693o-2",
            "relevance": "Distinguish statutory debit interchange, routing, and discount provisions from network restrictions on consumer surcharges.",
        },
        {
            "title": "12 CFR 235.7 — Limitations on payment card network restrictions",
            "url": "https://www.ecfr.gov/current/title-12/chapter-II/subchapter-A/part-235/section-235.7",
            "relevance": "Evaluate debit network exclusivity and routing requirements without presenting them as permission to surcharge debit transactions.",
        },
        {
            "title": "New York General Business Law 518 — Credit card surcharge pricing",
            "url": "https://www.nysenate.gov/legislation/laws/GBS/518",
            "relevance": "Configure total credit-card price disclosure and surcharge limits for covered New York merchant transactions.",
        },
        {
            "title": "Massachusetts General Laws chapter 140D, section 28A — Credit card surcharges and discounts",
            "url": "https://malegislature.gov/Laws/GeneralLaws/PartI/TitleXX/Chapter140D/Section28A",
            "relevance": "Separate prohibited seller surcharges from discounts meeting the statutory conditions.",
        },
        {
            "title": "California Civil Code 1748.1 — Credit card surcharge statutory text",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1748.1",
            "relevance": "Identify the statutory starting point while separately reviewing controlling litigation and current enforceability before California deployment.",
        },
        {
            "title": "15 U.S.C. 8403 — Negative option marketing on the Internet",
            "url": "https://www.law.cornell.edu/uscode/text/15/8403",
            "relevance": "Require material offer disclosure, express informed consent, and simple cancellation mechanisms for covered online negative-option transactions.",
        },
        {
            "title": "15 U.S.C. 45 — Unfair or deceptive acts or practices",
            "url": "https://www.law.cornell.edu/uscode/text/15/45",
            "relevance": "Support accurate formation offers, substantiated merchant savings claims, and disclosure of material referral relationships.",
        },
        {
            "title": "16 CFR 255.5 — Disclosure of material connections in endorsements",
            "url": "https://www.ecfr.gov/current/title-16/chapter-I/subchapter-B/part-255/section-255.5",
            "relevance": "Apply FTC interpretive guidance to material referral compensation when recommendations function as endorsements.",
        },
        {
            "title": "15 U.S.C. 7704 — Requirements for commercial electronic mail",
            "url": "https://www.law.cornell.edu/uscode/text/15/7704",
            "relevance": "Implement accurate commercial email identification, postal address disclosures, functioning opt-outs, and timely suppression.",
        },
        {
            "title": "47 U.S.C. 227 — Restrictions on telephone equipment and telephone solicitations",
            "url": "https://www.law.cornell.edu/uscode/text/47/227",
            "relevance": "Assess calling and texting practices by number type, technology, message content, and required permission rather than relying on a business-purpose label.",
        },
        {
            "title": "47 CFR 64.1200 — Telephone solicitation and calling restrictions",
            "url": "https://www.ecfr.gov/current/title-47/chapter-I/subchapter-B/part-64/subpart-L/section-64.1200",
            "relevance": "Implement applicable calling permissions, internal suppression procedures, and restrictions governing automated or prerecorded outreach.",
        },
        {
            "title": "16 CFR Part 310 — Telemarketing Sales Rule",
            "url": "https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-310",
            "relevance": "Determine which telemarketing provisions cover the proposed campaign, including applicable business-to-business misrepresentation restrictions.",
        },
        {
            "title": "FinCEN FIN-2007-G006 — Application of the definition of money services business to ATM owners and operators",
            "url": "https://www.fincen.gov/resources/statutes-regulations/guidance/application-definition-money-services-business-owners-and",
            "relevance": "Use the agency's activity-specific interpretation for conventional ATM withdrawals without extending it to remittance, deposit, or conversion services.",
        },
    ],
}
