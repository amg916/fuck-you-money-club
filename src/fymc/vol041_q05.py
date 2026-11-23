from __future__ import annotations

CHAPTER_5 = {
    "id": "Q5",
    "chapter_id": "Q5",
    "chapter_number": 5,
    "question_number": 5,
    "slug": "beginner-traps-clawbacks-asymmetric-failure-modes",
    "question_prompt": "What kills 80% of newcomers in buying group, card-float & ticket allocation arbitrage, and what forensic metrics detect margin leaks, regulatory landmines, or platform bans before they wipe out capital?",
    "kicker": "Q5 / THE BIG MONEY PLAYBOOKS",
    "title": "Beginner Traps, Clawbacks & Asymmetric Failure Modes",
    "subtitle": "Buying-Group ACH Aging, Issuer Reviews, Ticket Decay, BOTS Act Controls, and ASC 606 Spread Reconciliation",
    "layout_template": "expert_insights",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #41, Rank #09 of 42, scores 93/100 across a volume with 11 mapped plays, "
        "but its attractive manpower ratio conceals concentrated settlement, credit, and inventory risks. "
        "The canonical annual owner profits are $20,000 Conservative, $143,500 Base, and $360,000 Scaled; "
        "gross transaction proceeds are not interchangeable with retained operator revenue. This chapter "
        "dismantles reimbursement delays, rebate reversals, issuer shutdowns, shipment defects, duplicate "
        "ticket sales, event cancellations, and misleading corporate-credit shortcuts. It provides loss "
        "budgets, account-level telemetry, lawful acquisition controls, and a financing fallback for "
        "aged_shelf_corp_tradeline_credit_stacking. The question's 80% figure is a framing device, not an "
        "established failure statistic. Survival comes from matching each purchase to enforceable economics "
        "and funding every obligation without depending on tomorrow's buyer."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$250,000",
            "context": "Annual gross proceeds; $87,500 retained revenue at 35%.",
            "note": "8% gross-basis net margin; $20,000 annual owner profit; 22.86% retained margin; 1 FT + 2 C.",
        },
        {
            "label": "Base",
            "value": "$1,025,000",
            "context": "Annual gross proceeds; $358,750 retained revenue at 35%.",
            "note": "14.0% gross-basis net margin; $143,500 annual owner profit; 40.0% retained margin; 1 FT + 2 C.",
        },
        {
            "label": "Scaled",
            "value": "$1,800,000",
            "context": "Annual gross proceeds; $630,000 retained revenue at 35%.",
            "note": "20% gross-basis net margin; $360,000 annual owner profit; 57.14% retained margin; 2 FT + 3 C.",
        },
    ],
    "sections": [
        {
            "heading": "1. Separate economic spread from cash that belongs to the next settlement",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "The first fatal trap is booking reimbursement principal as spendable profit. Formula v2.0 "
                    "uses $250,000, $1,025,000, and $1,800,000 of annual gross proceeds, with a 35% retained "
                    "share of $87,500, $358,750, and $630,000. Subtracting owner profits of $20,000, $143,500, "
                    "and $360,000 leaves modeled operating and loss burdens of $67,500, $215,250, and $270,000 "
                    "after merchandise and ticket basis. Those residuals are reconciliation totals, not permission "
                    "to force every expense into monthly overhead. Gross-basis margins remain 8%, 14.0%, and "
                    "20%; retained margins are 22.86%, 40.0%, and 57.14%. Maintain both denominators on every "
                    "dashboard. The scorecard's ASC 606 net presentation is a modeling convention that must be "
                    "checked against actual principal-versus-agent facts for each contract. An operator controlling "
                    "inventory may have a different accounting presentation without changing cash economics. Never "
                    "apply the 35% portfolio assumption blindly to an individual purchase order. Record purchase "
                    "basis, expected reimbursement, earned rebate, freight, insurance, platform fees, defect reserve, "
                    "and settlement date separately. Otherwise a profitable-looking buying-group shipment can "
                    "consume the cash required to settle an unrelated ticket cancellation. Reconcile modeled "
                    "profit to bank movement through receivables, inventory, payables, and card balances rather "
                    "than treating a temporarily swollen checking account as distributable earnings."
                ),
                (
                    "The second and third traps are confusing a buying-group commitment with cleared money "
                    "and confusing delivery with acceptance. A Net-3 or Net-5 term is incomplete until the "
                    "contract defines business days, the acceptance trigger, inspection rights, and permitted "
                    "deductions. Consider an illustrative $10,000 purchase with a $10,100 reimbursement and a "
                    "$200 earned rebate. After $80 freight, $30 insurance, and a $40 defect reserve, expected "
                    "contribution is $150. A $250 condition deduction changes that to a $100 loss before "
                    "financing. Capture the commitment identifier before ordering and link merchant invoice, "
                    "serial numbers, carrier acceptance, warehouse receipt, inspection result, and remittance. "
                    "Do not accept a warehouse scan as evidence that the contractual inspection period has "
                    "expired. A payment arriving from an unexpected entity requires reconciliation with the "
                    "contracting counterparty, not automatic release of another shipment. Set an internal warning "
                    "at one business day beyond the agreed payment deadline and suspend new commitments at "
                    "three business days overdue until an authorized operator resolves the exception. These "
                    "are proposed house limits, not industry statistics. Extend no additional exposure merely "
                    "because a group posts attractive new deals while earlier accepted units remain unpaid."
                ),
                (
                    "The fourth trap is treating a shipping label's declared value as comprehensive insurance. "
                    "Carrier liability, purchased cargo coverage, excluded commodities, signature requirements, "
                    "and claim deadlines are separate contractual facts. Photograph packaging and serial numbers "
                    "before sealing, retain weight records, and verify that the named insured and claim beneficiary "
                    "match the party bearing transit risk. A $12,000 electronics carton with only $1,000 recoverable "
                    "coverage exposes $11,000 before any deductible; buying-group reimbursement does not erase "
                    "that gap. Track disputed dollars as a share of retained contribution, not simply shipment "
                    "value. A $600 dispute consumes four $150 clean-order contributions, which is a more useful "
                    "management signal than a small percentage of gross throughput. Aggregate exposure across "
                    "related buying groups sharing beneficial ownership, warehouses, or payment accounts. Use "
                    "a provisional ceiling of 20% of deployable cash per correlated counterparty cluster and "
                    "require cleared settlement before exceeding it. A low-capital operator should shrink lots "
                    "instead of assuming diversification exists because five websites have different branding. "
                    "Keep one shipment-sized liquidity buffer outside the next purchase cycle. Insured losses "
                    "can still create a cash crisis because documentation disputes and claim processing usually "
                    "do not follow the card statement calendar."
                ),
            ],
            "table": {
                "caption": "Buying-Group Margin-Leak and Settlement Exception Matrix",
                "headers": [
                    "Failure mechanism",
                    "Forensic evidence",
                    "Proposed intervention threshold",
                    "Required operator response",
                ],
                "rows": [
                    [
                        "Reimbursement principal gets mistaken for distributable operating profit",
                        "Compare bank receipts against matched purchase basis and liabilities",
                        "Any proposed distribution depends on unsettled reimbursement principal",
                        "Rebuild the cash bridge before releasing owner distributions",
                    ],
                    [
                        "Acceptance terms silently extend the advertised settlement cycle",
                        "Retain inspection windows and actual warehouse acceptance timestamps",
                        "First business day beyond the contractual payment deadline",
                        "Escalate reconciliation and suspend expansion of counterparty exposure",
                    ],
                    [
                        "Condition deductions erase thin merchandise and rebate spreads",
                        "Match serial photographs with rejection codes and deduction notices",
                        "Single deduction exceeds the shipment's entire expected contribution",
                        "Contest with evidence and reprice future defect reserves",
                    ],
                    [
                        "Correlated buying groups create disguised single debtor concentration",
                        "Compare contracting entities, ownership records, warehouses, and remitters",
                        "Cluster exposure exceeds twenty percent of deployable cash",
                        "Reduce open lots until cleared payments restore capacity",
                    ],
                    [
                        "Transit recovery falls below the replacement cash obligation",
                        "Inspect commodity exclusions, deductibles, beneficiary terms, and signatures",
                        "Recoverable coverage falls below the accepted shipment risk",
                        "Change coverage or reduce shipment value before dispatch",
                    ],
                    [
                        "Late claims destroy otherwise valid recovery rights permanently",
                        "Calendar carrier notice deadlines beside delivery exception evidence",
                        "Any damaged shipment lacks a documented claim owner",
                        "Assign responsibility immediately and preserve every required document",
                    ],
                    [
                        "Profit reporting hides inventory growth and unpaid card obligations",
                        "Reconcile contribution reports to inventory, receivables, and card balances",
                        "Reported earnings rise while unrestricted operating cash declines",
                        "Freeze distributions and explain each working capital movement",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Four controls that preserve thin spreads",
                "body": "Veteran operators protect evidence and liquidity before chasing another rebate point.",
                "items": [
                    "Attach the buying-group commitment and acceptance clock to each serial-number record before merchandise leaves your control.",
                    "Calculate how many clean-order contributions each deduction consumes; investigate losses exceeding two contributions even when gross-volume percentages look small.",
                    "Group counterparties by shared payment accounts and warehouses, then apply one exposure ceiling to the entire related cluster.",
                    "Ask the cargo insurer to identify the exact commodity coverage and claim beneficiary in writing before sending the first high-value carton.",
                ],
            },
        },
        {
            "heading": "2. Stress the card calendar and reject fictitious corporate-credit advantages",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "The fifth trap is treating a 60-day float ledger as a promise of 60 interest-free "
                    "days on every purchase. Available time depends on posting date, statement close, contractual "
                    "due date, and continued grace-period eligibility. A purchase just before closing can have "
                    "far less runway than one just afterward. Build the calendar from issuer statements rather "
                    "than marketing language. An illustrative $20,000 eligible purchase earning 2% produces "
                    "$400 before any spread or expenses. Thirty days of financing at a 24% annual rate "
                    "costs approximately $394.52 using a 365-day simple-interest approximation, leaving $5.48 "
                    "before shipping or defects. Actual issuer calculations may differ. Treat uncapped 2%–4% "
                    "commercial rewards as product-specific eligibility assumptions, not universal terms. Verify "
                    "category exclusions, spend caps, cash-equivalent treatment, promotional expirations, and "
                    "clawback provisions in the current agreement. Report rewards in three states: estimated, "
                    "posted, and available for redemption. Only the final state belongs in the immediate "
                    "liquidity forecast, and even redeemed rewards may remain subject to contractual reversal. "
                    "If interest begins accruing or a rebate is disputed, stop extending the affected strategy "
                    "until purchase-level contribution remains positive without the disputed benefit. Do not "
                    "solve that warning by opening another card."
                ),
                (
                    "The mapped play aged_shelf_corp_tradeline_credit_stacking requires a sharper distinction "
                    "than its name suggests. Reinstating an older entity can restore its state status where "
                    "permitted, but incorporation age is not evidence of revenue, payment performance, or "
                    "continuous operations. Genuine facilities are underwritten against accurately disclosed "
                    "ownership, activity, financial statements, guarantees, and repayment capacity. Do not "
                    "present purchased tradelines as the applicant's own operating achievements or conceal "
                    "related applications and existing obligations when asked. Compare an illustrative $30,000 "
                    "draw under a genuine 0%-APR purchase promotion with a transparent 12% term facility. "
                    "If the full principal remains outstanding for six months, simplified interest on the "
                    "term facility is $1,800, excluding fees and amortization effects. A $900 entity package "
                    "plus $1,200 placement charge already costs $2,100 before reinstatement expenses, so the "
                    "aged-company route is not automatically cheaper even if an issuer actually grants the "
                    "promotion. Classify those charges as financing acquisition costs, not merchandise basis. "
                    "If approval depends on inaccurate history or repayment depends on another future "
                    "application, halt applications, correct disclosures, and use a transparent term facility "
                    "or reduce financed spending. Preserve the underwriting record so later issuer questions "
                    "can be answered with consistent documents rather than improvised explanations."
                ),
                (
                    "The sixth and seventh traps are paying one facility with uncertain proceeds and "
                    "responding to issuer scrutiny by obscuring activity. An issuer review can freeze available "
                    "credit while every existing balance remains payable. Maintain a thirteen-week cash forecast "
                    "with card due dates, buying-group acceptance delays, ticket payout holds, refunds, and "
                    "tax liabilities. Define due-date coverage as unrestricted cash plus receipts actually "
                    "cleared before the payment deadline, divided by contractual payments due over the next "
                    "fourteen days. Exclude unused limits and expected rewards. Under an illustrative house "
                    "policy, coverage below 1.25 triggers reduced purchasing; below 1.00 stops new financed "
                    "orders and initiates an orderly cash recovery plan. Stress one major buying group paying "
                    "ten business days late while the largest issuer supplies no additional capacity. Keep "
                    "invoices, shipping evidence, beneficial-owner records, and bank statements consistent "
                    "with applications. Never fabricate sales, circulate payments to imitate demand, or create "
                    "replacement accounts to defeat a suspension. Commercial-purpose credit is generally "
                    "outside many consumer Regulation Z protections under 12 CFR 1026.3(a), making the actual "
                    "agreement especially important. Diversify genuine facilities only when aggregate repayment "
                    "capacity supports them; five limits drawing on the same receivable are one economic risk."
                ),
            ],
            "table": {
                "caption": "Issuer, Promotion, and Working-Capital Circuit-Breaker Matrix",
                "headers": [
                    "Credit trap",
                    "Required measurement",
                    "Illustrative warning condition",
                    "Financing fallback",
                ],
                "rows": [
                    [
                        "Statement timing creates less float than purchasing assumes",
                        "Calculate days between actual posting and contractual payment deadline",
                        "Expected reimbursement lands after the applicable payment deadline",
                        "Delay purchase or fund repayment with existing unrestricted cash",
                    ],
                    [
                        "Accrued interest consumes the entire eligible rebate yield",
                        "Compare transaction interest and fees against earned reward dollars",
                        "Financing expense exhausts contribution before freight and defects",
                        "Stop revolving exposure and recalculate economics without rewards",
                    ],
                    [
                        "Promotional eligibility excludes the intended commercial transaction type",
                        "Read current offer terms alongside transaction classification records",
                        "Written eligibility cannot support the modeled promotional treatment",
                        "Use ordinary contract pricing or reject the purchase",
                    ],
                    [
                        "Entity age gets substituted for genuine operating history",
                        "Reconcile application statements with formation and operating records",
                        "Any claimed trading history exceeds supported business activity",
                        "Halt applications, correct disclosures, and reduce financed spending",
                    ],
                    [
                        "Placement fees exceed realistic promotional financing savings available",
                        "Compare all acquisition charges with equivalent transparent borrowing costs",
                        "Entity and placement charges exceed documented financing savings",
                        "Choose a transparent term facility with affordable repayment",
                    ],
                    [
                        "Issuer review removes capacity needed for tomorrow's purchases",
                        "Stress available credit at zero while preserving existing obligations",
                        "Cash forecast requires fresh borrowing to meet scheduled payments",
                        "Suspend commitments and collect existing receivables before restarting",
                    ],
                    [
                        "Shared receivables support several apparently independent card limits",
                        "Aggregate every facility against the same cleared repayment resources",
                        "Fourteen day due-date coverage falls below one times",
                        "Stop financed orders and execute documented cash recovery",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Verify repayment before the next purchase",
                "body": "A purchase proceeds only when all four checks have documentary support.",
                "items": [
                    "Confirm the issuer's actual statement dates, eligible transaction category, promotion expiry, and applicable reward reversal terms.",
                    "Match entity history, ownership, revenue, guarantees, and outstanding obligations to the disclosures used in the credit application.",
                    "Demonstrate at least 1.25 times fourteen-day due-date coverage using unrestricted cash and already-cleared receipts.",
                    "Show that a ten-business-day buying-group delay and loss of the largest unused card line do not prevent contractual repayment.",
                ],
            },
        },
        {
            "heading": "3. Price ticket decay and make acquisition rights auditable",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "The eighth trap is valuing tickets at asking prices instead of executable net proceeds. "
                    "Secondary inventory has a deadline, and the final unsold seat can become worthless "
                    "even when yesterday's listings appeared profitable. For an illustrative $200 ticket, "
                    "$10 acquisition expense, $5 transfer expense, and a 15% seller fee, break-even resale "
                    "price is $215 divided by 0.85, or $252.94. A $240 sale returns $204 after the seller "
                    "fee and loses $11 against the $215 basis. Use actual settlement schedules because "
                    "fee structures differ by exchange and contract. SkyBox or Automatiq can centralize "
                    "inventory and repricing where supported, but software does not establish transferability "
                    "or guarantee synchronization. Measure comparable completed transactions when available, "
                    "the cheapest genuinely comparable listing, inventory depth, and days until the event. "
                    "An illustrative markdown plan reviews positions at twenty-one, fourteen, seven, and "
                    "two days before the event, with purchase suspension whenever expected liquidation "
                    "loss exceeds the allocated event budget. Treat a stop-loss as an instruction to "
                    "seek execution without assuring an exit price. Review venue, section, row, restrictions, "
                    "and delivery timing before trusting a superficially comparable listing."
                ),
                (
                    "The ninth and tenth traps are duplicate sales and inventory that cannot be delivered "
                    "as advertised. A synchronization delay across exchanges can sell the same seat twice; "
                    "replacement-ticket charges, contractual penalties, and account restrictions can exceed "
                    "the original spread. Maintain one authoritative inventory identifier per transferable "
                    "entitlement, not merely per listing. Lock that entitlement when an order is accepted "
                    "and retain downstream delisting acknowledgments. An illustrative internal target is "
                    "confirmation within sixty seconds; if an integration cannot reliably meet the chosen "
                    "target, use single-exchange listing for scarce inventory rather than promise impossible "
                    "control. Test transfer availability before listing and monitor delayed-delivery windows "
                    "separately from ordinary inventory. Stadium seat licenses, often abbreviated SSLs, "
                    "and corporate-suite allocations are contract rights, not automatically interchangeable "
                    "tickets. Identify assignment restrictions, annual purchase obligations, renewal dates, "
                    "suite-host duties, and whether amenities transfer with the seat. A suite costing "
                    "$12,000 for twenty seats requires $600 per seat before any selling costs; selling "
                    "sixteen seats at $650 produces $10,400 and a $1,600 shortfall before fees. Where "
                    "permitted, broker confirmed demand without taking speculative title, documenting the "
                    "commission and delivery responsibilities explicitly. Otherwise shrink the allocation "
                    "rather than disguising unsold capacity as a marketing expense."
                ),
                (
                    "The eleventh trap is treating technical access as permission to circumvent ticket "
                    "purchase controls. The federal BOTS Act, 15 U.S.C. §45c, prohibits specified circumvention "
                    "of security measures, access controls, or technological controls enforcing posted ticket "
                    "limits or purchase-order rules; it also restricts trafficking in tickets obtained through "
                    "covered violations. Do not use queue or CAPTCHA bypass software, deceptive identity "
                    "multiplication, or proxy-based concealment to defeat purchase limits. Platform contracts "
                    "can prohibit additional conduct beyond the statute, and a successful checkout proves "
                    "neither contractual permission nor clean provenance. Retain acquisition receipts and "
                    "seller attestations, investigate suspicious volumes, and reject inventory whose lawful "
                    "acquisition cannot be supported. For covered live-event ticket offers, 16 CFR Part 464 "
                    "requires upfront total-price presentation including mandatory fees, subject to its "
                    "specified treatment of government charges and shipping. Build price displays from "
                    "the actual rule rather than adding mandatory service charges late in checkout. Apply "
                    "relevant state resale, licensing, disclosure, and tax requirements by jurisdiction; "
                    "New York Arts and Cultural Affairs Law §25.07 provides concrete ticket-pricing rules. "
                    "When rights or sourcing fail review, cancel the acquisition before taking payment "
                    "from a downstream buyer. Never reopen a banned account through concealed ownership."
                ),
            ],
            "table": {
                "caption": "Ticket Allocation, Transfer Rights, and Lawful Acquisition Matrix",
                "headers": [
                    "Inventory failure",
                    "Evidence and unit economics",
                    "Proposed warning threshold",
                    "Immediate containment response",
                ],
                "rows": [
                    [
                        "Asking prices conceal negative executable ticket resale margins",
                        "Subtract actual seller fees from comparable achievable proceeds",
                        "Expected proceeds fall below basis and required delivery costs",
                        "Mark down deliberately or stop buying additional event exposure",
                    ],
                    [
                        "Event concentration converts small markdowns into capital impairment",
                        "Aggregate all seats and suites by correlated event exposure",
                        "Liquidation stress exceeds the event's written loss budget",
                        "Reduce positions before adding inventory for related performances",
                    ],
                    [
                        "Exchange synchronization sells one transferable entitlement multiple times",
                        "Record entitlement locks and every downstream delisting acknowledgment",
                        "Acknowledgment misses the documented internal synchronization time target",
                        "Disable additional channels until inventory reconciliation is complete",
                    ],
                    [
                        "Delayed transfers make advertised delivery dates impossible to meet",
                        "Verify release dates against actual customer delivery promises",
                        "Transfer availability extends beyond the promised delivery deadline",
                        "Correct listings and arrange an authorized customer resolution",
                    ],
                    [
                        "Suite economics depend on selling every allocated seat",
                        "Compare contracted suite cost with conservative net sold seats",
                        "Confirmed net demand cannot cover the allocation obligation",
                        "Broker permitted rights or reduce the committed allocation",
                    ],
                    [
                        "Acquisition shortcuts defeat enforced purchase limits or controls",
                        "Retain receipts, source attestations, limits, and acquisition account records",
                        "Source evidence indicates prohibited circumvention or deceptive acquisition",
                        "Reject inventory and stop the implicated sourcing relationship",
                    ],
                    [
                        "Late mandatory fees misstate the initially displayed ticket price",
                        "Audit customer price displays against applicable total-price requirements",
                        "Mandatory service charges appear only after initial price display",
                        "Correct pricing logic before accepting additional affected orders",
                    ],
                ],
            },
        },
        {
            "heading": "4. Run one exception ledger for clawbacks, taxes, refunds, and shutdown recovery",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "The twelfth trap is releasing reserves when a transaction is merely paid rather "
                    "than economically closed. A ticket payout can precede a cancellation claim, and a "
                    "merchant return can reverse a card reward after the reward funded another purchase. "
                    "Create an exception ledger linking every order to refund rights, dispute windows, "
                    "reward reversal terms, and the party contractually responsible for replacement. For "
                    "an illustrative $300 ticket sale with a $45 seller fee and $210 acquisition basis, "
                    "initial contribution is $45. If cancellation requires a $300 customer refund while "
                    "the marketplace retains its $45 fee and the supplier returns only $210, final "
                    "loss is $45, a $90 deterioration from the original forecast. Different contracts "
                    "change that result; model the actual cash legs instead of assuming symmetric refunds. "
                    "Track exposure by event and marketplace because one cancellation can affect many "
                    "orders simultaneously. A reserve equal to average historical refunds is inadequate "
                    "for a portfolio dominated by one event. Hold enough accessible liquidity for the "
                    "largest explicitly chosen cancellation stress and disclose any remaining funding "
                    "gap internally. Do not count supplier recovery until the contractual right and "
                    "expected payment timing have both been evaluated."
                ),
                (
                    "The thirteenth trap is treating resale documentation as a blanket tax exemption. "
                    "For California merchandise purchases, Regulation 1668 governs resale certificates; "
                    "the documentation must fit a genuine resale transaction and applicable requirements. "
                    "An item diverted to business use can create tax consequences even when originally "
                    "purchased for resale. Maintain jurisdiction, certificate, seller acceptance, transaction "
                    "purpose, and subsequent disposition together. Marketplace tax collection does not "
                    "automatically resolve taxes or obligations on off-platform activity, suite arrangements, "
                    "or wholesale merchandise. Separate collected tax from revenue and unrestricted cash. "
                    "In an illustrative transaction where an 8% tax applies to a $1,000 taxable base, "
                    "the $80 collected is a liability, not spread; actual rates and taxable bases vary. "
                    "Reconcile marketplace tax reports to orders and investigate differences before funds "
                    "are distributed. At Base scale, a recurring $500 monthly leak removes $6,000, or "
                    "about 4.18% of canonical $143,500 annual owner profit. Use that profit denominator "
                    "to prioritize repairs. Assign each exception an owner, supporting evidence, dollar "
                    "exposure, deadline, and next action. Without these fields, a colorful dashboard "
                    "becomes a queue of losses that nobody is responsible for collecting or stopping."
                ),
                (
                    "The final trap is automating throughput before automating reconciliation and shutdown. "
                    "Use a daily three-way match among commitments or orders, delivery or acceptance "
                    "evidence, and bank or marketplace settlement. Add a fourth comparison for issuer "
                    "rewards and deductions wherever rewards form part of the original margin. Set "
                    "illustrative alerts for any unmatched settlement older than one business day, any "
                    "negative-contribution order, and aggregate unresolved losses above 10% of the month's "
                    "planned retained contribution. A single verified duplicate sale, prohibited sourcing "
                    "incident, or unexplained ownership discrepancy warrants immediate isolation regardless "
                    "of dollar size. Keep buying-group, issuer, marketplace, and event concentrations visible "
                    "together so diversification is assessed economically rather than by account count. "
                    "A one-owner team with two contractors needs named reconciliation and fulfillment "
                    "backups, not three people editing the same spreadsheet without permissions. The "
                    "Scaled case adds a second full-time operator and three contractors but does not "
                    "remove the need for separation of duties. Restart an interrupted lane only after "
                    "the cause is corrected, outstanding customers are handled, cash coverage is restored, "
                    "and a small authorized test settles cleanly. Preserve appeal evidence and communicate "
                    "through approved account channels; account replacement is not a recovery strategy."
                ),
            ],
            "table": {
                "caption": "Clawback, Tax, and Restart Exception Ownership Matrix",
                "headers": [
                    "Latent liability",
                    "Daily forensic check",
                    "Proposed escalation condition",
                    "Closure evidence",
                ],
                "rows": [
                    [
                        "Cancellation refunds exceed immediately recoverable supplier purchase basis",
                        "Model customer refunds, retained fees, and supplier recovery timing",
                        "Largest chosen event stress exceeds accessible refund liquidity",
                        "Document funded refunds and reconcile remaining supplier recovery",
                    ],
                    [
                        "Returned merchandise reverses rewards already treated as operating income",
                        "Match issuer adjustment records to returned purchase transaction identifiers",
                        "Reward reversal makes the original order contribution negative",
                        "Post revised economics and recover eligible contractual reimbursements",
                    ],
                    [
                        "Resale certificates fail to match actual merchandise disposition",
                        "Compare certificate scope with buyer status and item disposition",
                        "Goods enter business use without a documented tax review",
                        "Correct transaction treatment and retain supporting disposition records",
                    ],
                    [
                        "Collected taxes are spent as unrestricted purchasing capital",
                        "Reconcile tax liabilities separately from revenue and cash reserves",
                        "Available reserved cash falls below recorded tax obligations",
                        "Restore reserved funds and reconcile jurisdiction reporting amounts",
                    ],
                    [
                        "Unowned deductions remain unresolved until recovery deadlines expire",
                        "Require owner, deadline, evidence, and next action per exception",
                        "Any recoverable deduction lacks an accountable assigned operator",
                        "Record recovery or authorized writeoff with supporting evidence",
                    ],
                    [
                        "Unmatched settlements hide duplicate deductions and missing payments",
                        "Match commitments, acceptance records, settlement deposits, and reward adjustments",
                        "Unmatched settlement remains open beyond one business day",
                        "Resolve transaction linkage and document all remaining differences",
                    ],
                    [
                        "Premature restart repeats the incident across larger inventory volumes",
                        "Verify corrected cause, funded obligations, and clean test settlement",
                        "Any customer obligation or root cause remains unresolved",
                        "Resume only the repaired authorized lane at reduced exposure",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Isolate the affected exposure",
                    "action": "Stop new commitments in the implicated counterparty, issuer, event, or exchange lane.",
                    "detail": "Preserve outstanding delivery obligations and freeze only the activity creating additional risk; do not indiscriminately cancel customer orders.",
                },
                {
                    "step": 2,
                    "title": "Reconstruct the contractual cash waterfall",
                    "action": "Match original terms, invoices, fulfillment evidence, fees, rewards, deductions, and settlement records.",
                    "detail": "Calculate the loss and payment calendar without assuming a successful appeal, fresh borrowing, or immediate insurance recovery.",
                },
                {
                    "step": 3,
                    "title": "Fund obligations and pursue supported recovery",
                    "action": "Allocate unrestricted cash to due payments, refunds, taxes, and required delivery remedies.",
                    "detail": "Submit documented claims within contractual deadlines and use the issuer's or marketplace's authorized review process.",
                },
                {
                    "step": 4,
                    "title": "Restart with a small observable transaction",
                    "action": "Verify the repaired control and complete one authorized transaction through final reconciliation.",
                    "detail": "Restore exposure incrementally only after settlement, reward treatment, customer delivery, and due-date coverage match the revised model.",
                },
            ],
        },
    ],
    "pull_quote": "A spread is not yours until the delivery holds, the cash clears, and the clawback can be funded.",
    "diagram_id": "diag-05",
    "action_checklist": [
        "Reconcile all three canonical cases using gross proceeds, 35% retained revenue, retained margins, and exact annual owner profits.",
        "Build a commitment-to-settlement register linking buying-group terms, serial evidence, acceptance timestamps, insurance, deductions, and bank receipts.",
        "Calculate fourteen-day due-date coverage and stress a ten-business-day reimbursement delay with no additional capacity from the largest issuer.",
        "Audit aged_shelf_corp_tradeline_credit_stacking disclosures and compare all acquisition charges against a transparent term facility before applying.",
        "Verify ticket acquisition provenance, transfer rights, all-in price displays, event loss budgets, and multi-exchange delisting acknowledgments.",
        "Assign every refund, tax difference, reward reversal, and platform restriction an owner, cash reserve, evidence packet, and restart condition.",
    ],
    "statutory_citations": [
        {
            "title": "15 U.S.C. §45c — Better Online Ticket Sales Act",
            "url": "https://www.law.cornell.edu/uscode/text/15/45c",
            "relevance": "Prohibits covered circumvention of ticket purchase controls and specified trafficking in tickets obtained through covered violations; supports acquisition provenance and sourcing controls.",
        },
        {
            "title": "16 CFR Part 464 — Rule on Unfair or Deceptive Fees",
            "url": "https://www.ecfr.gov/current/title-16/chapter-I/subchapter-D/part-464",
            "relevance": "Establishes total-price and related disclosure requirements for covered live-event ticket offers, including treatment of mandatory charges.",
        },
        {
            "title": "12 CFR 1026.3(a) — Business, Commercial, Agricultural, or Organizational Credit",
            "url": "https://www.consumerfinance.gov/rules-policy/regulations/1026/3/",
            "relevance": "Identifies business-purpose and organizational credit exemptions from Regulation Z, making accurate purpose classification and review of commercial credit agreements essential.",
        },
        {
            "title": "New York Arts and Cultural Affairs Law §25.07 — Ticket Pricing",
            "url": "https://www.nysenate.gov/legislation/laws/ACA/25.07",
            "relevance": "Provides state ticket-pricing and disclosure requirements that must be incorporated into applicable ticket offers and transaction records.",
        },
        {
            "title": "California Code of Regulations, Title 18, §1668 — Sales for Resale",
            "url": "https://www.cdtfa.ca.gov/lawguides/vol1/sutr/1668.html",
            "relevance": "Sets requirements governing sales for resale and resale certificates; supports transaction-level documentation rather than blanket exemption assumptions.",
        },
    ],
}
