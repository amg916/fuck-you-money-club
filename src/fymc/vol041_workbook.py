from __future__ import annotations


def build_volume_041_workbook() -> dict:
    def field(name: str, input_type: str, prompt: str, example: str) -> dict:
        return {
            "name": name,
            "type": input_type,
            "prompt": prompt,
            "example": example,
        }

    return {
        "workbook_id": "wb-041-buying-group-card-rebate-and-ticket-allocation-arbitrage",
        "volume_id": "vol-041-buying-group-card-rebate-and-ticket-allocation-arbitrage",
        "title": (
            "Buying Group, Card-Float & Ticket Allocation Arbitrage "
            "— Operator Companion Workbook"
        ),
        "subtitle": (
            "6 Printable Operator Worksheets for Buying-Group Underwriting, "
            "Card-Float Liquidity, Ticket Allocation Execution, Statutory Controls, "
            "Automation Recovery, and Small-Team Launch Economics"
        ),
        "worksheets": [
            {
                "worksheet_id": "ws-01",
                "number": 1,
                "title": (
                    "Arbitrage Deal / Counterparty Underwriting "
                    "& Spread Qualification"
                ),
                "purpose": (
                    "Qualify each buying-group commitment, ticket allocation, or "
                    "corporate-suite mandate before capital moves. Establish who owes "
                    "payment, what creates an enforceable obligation, how inventory "
                    "can be transferred, and whether collectible spread survives "
                    "fees, shipment exceptions, delayed settlement, and event-driven "
                    "price decay."
                ),
                "chapter_ref": "Q1, Q2, Q6",
                "instructions": [
                    (
                        "Open one worksheet for each economic commitment, not each "
                        "marketplace listing. Assign a permanent deal identifier, name "
                        "the beneficial inventory owner, and attach the purchase order "
                        "or allocation agreement before comparing advertised yields "
                        "or requesting available card capacity."
                    ),
                    (
                        "Verify the buying group's contracting entity and receiving "
                        "account through independent channels. Request settlement "
                        "history, reference transactions, receiving procedures, and "
                        "exception terms; begin with a small paid pilot rather than "
                        "treating a familiar chat handle as credit evidence."
                    ),
                    (
                        "Rebuild the spread from actual invoices and collectible "
                        "proceeds. Separate merchandise reimbursement, ticket proceeds, "
                        "card rebates, platform charges, shipment costs, and taxes; "
                        "show both the eligible-rebate case and the zero-rebate case "
                        "before committing inventory or extending unsecured exposure."
                    ),
                    (
                        "Check ticket purchase limits, transfer restrictions, event "
                        "dates, suite guest rules, and seat-license provisions against "
                        "the original documents. Reject acquisition methods involving "
                        "queue circumvention or identity manipulation, and identify "
                        "the lawful liquidation route before entering any allocation."
                    ),
                    (
                        "Stress the deal against delayed ACH, card suspension, "
                        "shipment rejection, and ticket markdowns. Record the operator "
                        "who can stop purchases, the maximum recoverable exposure, "
                        "and the specific evidence required to reopen a paused "
                        "counterparty or inventory category."
                    ),
                ],
                "fields": [
                    field(
                        "Deal identity, economic role, and evidence bundle",
                        "textarea",
                        (
                            "Identify the deal, contracting parties, inventory owner, "
                            "and economic role. Distinguish principal resale from "
                            "agency brokerage, and list the source documents that "
                            "establish quantity, purchase authority, delivery obligations, "
                            "and enforceable payment terms."
                        ),
                        (
                            "BG-041-001 covers 20 authorized electronics units purchased "
                            "for $10,000 against a signed $10,200 wholesale commitment. "
                            "The operator owns merchandise until contractual acceptance. "
                            "The evidence bundle contains the supplier invoice, buying-group "
                            "purchase order, receiving address confirmation, serial-number "
                            "schedule, and written procedure for reporting damaged or "
                            "missing units."
                        ),
                    ),
                    field(
                        "Buying-group credit verification and pilot limit",
                        "textarea",
                        (
                            "Document independently verified entity details, settlement "
                            "references, bank-account confirmation, and the initial "
                            "exposure limit. Explain how paid pilot transactions and "
                            "aging results change the limit without relying on "
                            "unverified community reputation."
                        ),
                        (
                            "The first commitment is limited to $2,000 after checking "
                            "the state entity registry, calling a published business "
                            "number, and obtaining two supplier references. Bank changes "
                            "require callback verification. The limit rises to $5,000 "
                            "only after three accepted shipments settle within five "
                            "business days without unexplained deductions."
                        ),
                    ),
                    field(
                        "Net-3 or Net-5 acceptance clock",
                        "textarea",
                        (
                            "Specify whether the settlement clock begins at delivery, "
                            "inspection, or written acceptance. Record business-day "
                            "conventions, deduction rights, dispute deadlines, and the "
                            "person responsible for escalating unpaid accepted "
                            "merchandise before additional purchases occur."
                        ),
                        (
                            "The purchase order requires acceptance within one business "
                            "day of carrier delivery and payment within three business "
                            "days afterward. On a holiday-free Monday delivery, Tuesday "
                            "acceptance makes Friday the payment deadline. Any deduction "
                            "must identify affected serial numbers and invoice lines; "
                            "unpaid accepted inventory blocks further commitments."
                        ),
                    ),
                    field(
                        "Card eligibility, reward terms, and issuer exposure",
                        "textarea",
                        (
                            "Record the actual commercial-card reward rate, eligible "
                            "merchant categories, exclusions, available capacity, and "
                            "statement obligations. Treat uncapped rewards as a "
                            "documented product feature rather than an assumption, "
                            "and separate available credit from available cash."
                        ),
                        (
                            "The selected card's written terms provide uncapped 2% "
                            "rewards on eligible purchases, producing $200 on a "
                            "$10,000 order. Cash advances and ineligible transactions "
                            "are excluded. The operator retains $10,000 of repayment "
                            "capacity outside the card line and models $0 rewards "
                            "until the issuer posts the credit."
                        ),
                    ),
                    field(
                        "Collectible spread and zero-rebate sensitivity",
                        "textarea",
                        (
                            "Calculate spread using collectible reimbursement, eligible "
                            "rebates, landed basis, shipment charges, and expected "
                            "exception costs. Display the zero-rebate result separately, "
                            "and reject any presentation that labels card borrowing "
                            "or reimbursed purchase principal as profit."
                        ),
                        (
                            "A $10,000 merchandise purchase produces $10,200 reimbursement "
                            "and a conditional $200 rebate. Insured freight costs "
                            "$90 and expected receiving exceptions cost $50. Forecast "
                            "contribution is $260 with rewards and $60 without them. "
                            "The $10,200 reimbursement is a cash receipt, not "
                            "$10,200 of owner earnings."
                        ),
                    ),
                    field(
                        "Ticket acquisition provenance and allocation rights",
                        "textarea",
                        (
                            "Identify the lawful ticket source, account purchase "
                            "limit, transferable rights, and documentary chain. For "
                            "stadium seat licenses, abbreviated SSL, or suites, "
                            "separate the underlying license from individual event "
                            "tickets and corporate hospitality services."
                        ),
                        (
                            "The operator buys eight transferable tickets directly "
                            "within the published eight-ticket account limit and keeps "
                            "the order receipt. A separate suite mandate authorizes "
                            "brokerage for one event only; it does not transfer "
                            "the stadium seat license. Venue confirmation establishes "
                            "delivery timing, permitted guests, and resale restrictions."
                        ),
                    ),
                    field(
                        "Market depth, all-in pricing, and markdown curve",
                        "textarea",
                        (
                            "Use executable comparable sales and current competing "
                            "inventory to set an all-in price. Define scheduled "
                            "markdowns, minimum contribution thresholds, and event "
                            "cutoffs; explain how compulsory charges affect "
                            "customer-facing totals rather than hiding them downstream."
                        ),
                        (
                            "Twenty tickets cost $120 each. The initial customer "
                            "price is $180 each including mandatory charges other "
                            "than separately permitted government charges. Prices fall "
                            "to $165 fourteen days before the event and $145 "
                            "seven days before it. At three days, the inventory "
                            "owner chooses liquidation or documented retention."
                        ),
                    ),
                    field(
                        "Shipment acceptance, insurance, and recovery waterfall",
                        "textarea",
                        (
                            "Map serial tracking, packaging evidence, declared value, "
                            "coverage exclusions, and acceptance proof to each "
                            "shipment. Specify who submits carrier or insurance "
                            "claims, what recovery is actually covered, and "
                            "how disputed receivables remain visible."
                        ),
                        (
                            "A $10,000 shipment receives serial photographs, tamper-evident "
                            "packaging, signature delivery, and confirmed cargo coverage "
                            "subject to a $250 deductible. The operator checks theft "
                            "and unattended-delivery exclusions before dispatch. A loss "
                            "opens an insurer claim and a separate receivable dispute; "
                            "anticipated insurance proceeds never close the unpaid invoice."
                        ),
                    ),
                    field(
                        "Counterparty, issuer, event, and platform concentration",
                        "textarea",
                        (
                            "Set concentration limits using deployable cash and "
                            "stressed exposure, not gross annual throughput. Include "
                            "accepted unpaid goods, unsettled tickets, refund "
                            "obligations, correlated event risk, and dependence on "
                            "one issuer or marketplace settlement channel."
                        ),
                        (
                            "With $40,000 deployable capital, one buying group may "
                            "carry at most $8,000 of accepted unpaid exposure. "
                            "One event may consume $4,000 of ticket basis. "
                            "A $10,000 proposed shipment exceeds the counterparty "
                            "limit and is divided into independently accepted lots; "
                            "card availability does not increase either limit."
                        ),
                    ),
                    field(
                        "Underwriting decision and reopening evidence",
                        "textarea",
                        (
                            "State the authorized deal size, required evidence, "
                            "stop conditions, and accountable operator. Document "
                            "what would justify reopening a rejected opportunity, "
                            "and prohibit retrospective rewriting of the original "
                            "spread assumptions after losses emerge."
                        ),
                        (
                            "The operator authorizes a $2,000 pilot, not the "
                            "requested $10,000 order. Purchases stop after any "
                            "missed contractual payment or unresolved account-name "
                            "mismatch. Reopening requires cleared settlement, a "
                            "documented root cause, and a revised exposure limit. "
                            "The original $260 forecast remains preserved beside "
                            "the pilot's actual contribution."
                        ),
                    ),
                ],
                "completion_gate": (
                    "Advance only when the contracting entity, payment clock, "
                    "inventory rights, eligible-rebate terms, zero-rebate economics, "
                    "and stressed exposure are documented. The accountable operator "
                    "must sign a specific deal limit, with no unresolved payment "
                    "identity mismatch or prohibited acquisition method."
                ),
            },
            {
                "worksheet_id": "ws-02",
                "number": 2,
                "title": (
                    "Unit Economics, Escrow/Reserve Float "
                    "& Working-Capital Calculator"
                ),
                "purpose": (
                    "Translate the canonical scorecard into a cash-safe operating "
                    "model without confusing gross collections, retained spread, "
                    "recognized revenue, owner profit, or available credit. Reconcile "
                    "all three scenarios, calculate dated repayment obligations, "
                    "and isolate restricted customer funds from deployable working capital."
                ),
                "chapter_ref": "Q3, Q4",
                "instructions": [
                    (
                        "Copy the three canonical scenarios exactly before building "
                        "transaction assumptions. Use 35% retained share for scorecard "
                        "comparability, then reconcile actual contracts separately; "
                        "do not force thin merchandise spreads or accounting "
                        "classifications to resemble the blended benchmark."
                    ),
                    (
                        "Build a dated cash schedule from purchase authorization "
                        "through cleared settlement and card repayment. Include "
                        "statement closing dates, issuer due dates, payout delays, "
                        "refund windows, and reserves; available revolving capacity "
                        "must never substitute for a funded repayment plan."
                    ),
                    (
                        "Calculate reward sensitivity at zero, the documented "
                        "eligible rate, and any contractually supported higher rate. "
                        "Exclude double counting between rebates and merchandise "
                        "basis reductions, and show how fees or delayed reward "
                        "posting affect both contribution and liquidity."
                    ),
                    (
                        "Separate unrestricted operating cash, customer money held "
                        "under contractual restrictions, platform reserves, and "
                        "internal liquidity buffers. A reserve transfer changes "
                        "cash availability, not necessarily earnings; record an "
                        "expense only when the relevant accounting recognition "
                        "criteria are satisfied."
                    ),
                    (
                        "Reconcile annual profit to monthly fixed overhead and "
                        "other modeled operating costs. Test counterparty delay "
                        "and issuer interruption together, then size the next "
                        "commitment from the lowest projected unrestricted cash "
                        "balance rather than the highest advertised credit limit."
                    ),
                ],
                "fields": [
                    field(
                        "Canonical Conservative scenario reconciliation",
                        "textarea",
                        (
                            "Enter gross revenue, retained share, retained contribution, "
                            "owner profit, and both margin denominators. Derive "
                            "the remaining cost allowance explicitly, preserving "
                            "the canonical one full-time operator and two "
                            "contractors without treating contractors as free capacity."
                        ),
                        (
                            "Conservative gross revenue is $250,000. Applying 35% "
                            "retained share yields $87,500; the corresponding basis "
                            "bridge is $162,500. Owner net profit is $20,000, "
                            "equal to 8% of gross and 22.86% of retained "
                            "revenue. Remaining modeled costs total $67,500 for "
                            "one full-time operator and two contractors."
                        ),
                    ),
                    field(
                        "Canonical Base scenario reconciliation",
                        "textarea",
                        (
                            "Reproduce the Base scenario using the same "
                            "denominator conventions as the Conservative scenario. "
                            "Show retained contribution, the merchandise and "
                            "ticket basis bridge, total remaining costs, and "
                            "the distinction between owner earnings and gross throughput."
                        ),
                        (
                            "Base gross revenue is $1,025,000 and retained "
                            "revenue is $358,750 at 35%. The basis bridge "
                            "equals $666,250; remaining modeled costs equal "
                            "$215,250. Annual owner net profit is $143,500, "
                            "or 14.0% of gross and 40.0% of retained "
                            "revenue, with one full-time operator and two contractors."
                        ),
                    ),
                    field(
                        "Canonical Scaled Small-Team reconciliation",
                        "textarea",
                        (
                            "Reproduce the scaled economics and identify the "
                            "staffing increase. Calculate retained margin directly "
                            "from retained revenue, and ensure the cost "
                            "bridge reconciles completely without adding a "
                            "second deduction for merchandise or ticket acquisition basis."
                        ),
                        (
                            "Scaled gross revenue is $1,800,000. Retained "
                            "revenue is $630,000, with a $1,170,000 basis "
                            "bridge and $270,000 of remaining modeled costs. "
                            "Owner net profit is $360,000: 20% of gross "
                            "and 57.14% of retained revenue. Staffing expands "
                            "to two full-time operators plus three contractors, "
                            "five people total."
                        ),
                    ),
                    field(
                        "ASC 606 presentation and retained-share bridge",
                        "textarea",
                        (
                            "Document principal-versus-agent conclusions using ASC "
                            "606-10-55-36 through 55-40. Separate the scorecard's "
                            "retained-revenue convention from financial-statement "
                            "presentation, and explain where card rebates, "
                            "sales taxes, and customer reimbursements belong "
                            "under the actual arrangement."
                        ),
                        (
                            "The Base benchmark reports $358,750 of retained "
                            "revenue for comparability, not an automatic booking "
                            "rule. Controlled merchandise may support gross "
                            "presentation; an agency suite placement may support "
                            "commission-only revenue. A $200 purchase rebate "
                            "reduces basis when appropriate and is not also "
                            "credited as a second $200 revenue item."
                        ),
                    ),
                    field(
                        "Transaction economics and reward sensitivity",
                        "textarea",
                        (
                            "Build one transaction from purchase basis through "
                            "collectible contribution. Include freight, marketplace "
                            "fees, reward eligibility, and expected loss "
                            "assumptions; compare the resulting retained share "
                            "with the canonical benchmark without altering "
                            "either number to conceal the difference."
                        ),
                        (
                            "The merchandise example has $10,200 reimbursement, "
                            "$10,000 basis, $90 freight, and $50 expected "
                            "exception cost. Contribution is $60 at zero "
                            "rewards, $260 at 2%, and $460 at 4%, "
                            "but 4% applies only with documented eligibility. "
                            "Its economics do not independently establish "
                            "the portfolio's 35% retained-share benchmark."
                        ),
                    ),
                    field(
                        "Statement calendar and actual float days",
                        "textarea",
                        (
                            "Record transaction posting, statement closing, payment "
                            "due, and cleared receipt dates. Calculate actual "
                            "float from the issuer schedule; identify grace-period "
                            "conditions and distinguish a modeled sixty-day "
                            "window from a contractual entitlement to that duration."
                        ),
                        (
                            "A purchase posts January 2, 2027, the statement "
                            "closes January 31, and payment is due February "
                            "25. Posting-to-due float is 54 calendar days, "
                            "not an assumed sixty. Cleared buying-group proceeds "
                            "arrive January 12. The operator schedules full "
                            "payment February 22 and verifies the card's "
                            "actual grace-period conditions."
                        ),
                    ),
                    field(
                        "Escrow, restricted proceeds, and liquidity reserves",
                        "textarea",
                        (
                            "List balances by ownership, restriction, release "
                            "condition, and banking location. Identify whether "
                            "escrow is genuinely provided by an authorized "
                            "arrangement, and prevent restricted customer deposits "
                            "or refundable suite advances from financing "
                            "unrelated buying-group inventory."
                        ),
                        (
                            "Bank cash totals $40,000, including $6,000 "
                            "of contractually restricted suite deposits and "
                            "a $10,000 internal repayment reserve. Deployable "
                            "cash is therefore $24,000. A separate $3,000 "
                            "platform holdback is excluded from bank cash. "
                            "Moving money into the internal reserve does "
                            "not create an expense or establish an escrow service."
                        ),
                    ),
                    field(
                        "Working-capital overlap and delayed settlement stress",
                        "textarea",
                        (
                            "Model overlapping unpaid purchases by settlement "
                            "cycle, then add refunds and fixed obligations "
                            "falling inside the same stress window. "
                            "Distinguish inventory already funded from incremental "
                            "cash requirements so the model does not "
                            "count one purchase twice."
                        ),
                        (
                            "Three unsettled $8,000 lots create $24,000 "
                            "of funded inventory exposure. A fourth lot "
                            "would require another $8,000 while $4,000 "
                            "of refunds and $3,000 of overhead fall due. "
                            "With $30,000 unrestricted cash before those "
                            "uses, the fourth lot leaves $15,000; already "
                            "funded inventory is not deducted again."
                        ),
                    ),
                    field(
                        "Monthly overhead and annual cost bridge",
                        "textarea",
                        (
                            "Allocate the scenario's remaining costs between "
                            "fixed monthly overhead and other operating "
                            "costs. Keep startup capital separate from "
                            "annual expenses, and state that illustrative "
                            "cost allocations preserve canonical totals "
                            "without claiming observed payroll or loss experience."
                        ),
                        (
                            "Illustrative overhead is $1,500 monthly Conservative, "
                            "$4,500 Base, and $9,000 Scaled. Annual "
                            "overhead is $18,000, $54,000, and $108,000; "
                            "other modeled costs are $49,500, $161,250, "
                            "and $162,000. Together they reconcile to "
                            "$67,500, $215,250, and $270,000. Startup "
                            "capital remains a separate $10,000–$55,000 requirement."
                        ),
                    ),
                    field(
                        "Capital authorization and downside survival decision",
                        "textarea",
                        (
                            "State the maximum next commitment, minimum "
                            "cash floor, and repayment source if rewards "
                            "disappear and ACH arrives late. Include "
                            "issuer shutdown and ticket refunds in "
                            "the same scenario rather than evaluating "
                            "each disruption in isolation."
                        ),
                        (
                            "With $24,000 deployable cash, the operator "
                            "requires an $8,000 cash floor and budgets "
                            "$4,000 for concurrent refunds. The maximum "
                            "new cash-funded commitment is $12,000, subject "
                            "to tighter counterparty limits. If issuer "
                            "capacity disappears, commitments shrink immediately; "
                            "the model does not assume replacement credit "
                            "or advance reward availability."
                        ),
                    ),
                ],
                "completion_gate": (
                    "All three scenarios must reconcile exactly to $20,000, "
                    "$143,500, and $360,000 annual owner net profit. Approve "
                    "new commitments only after documenting actual payment dates, "
                    "accounting presentation, restricted balances, and a funded "
                    "downside case that preserves the chosen cash floor."
                ),
            },
            {
                "worksheet_id": "ws-03",
                "number": 3,
                "title": (
                    "End-to-End Execution, Idempotent Ledger "
                    "& QA Pre-Flight Sheet"
                ),
                "purpose": (
                    "Turn authorized commitments into traceable inventory, settlements, "
                    "and reconciled accounting events. Design repeat-safe identifiers "
                    "and exception handling across buying-group shipments, card "
                    "statements, ticket marketplaces, and refunds so automation "
                    "cannot purchase twice, oversell one seat, or silently erase "
                    "an unpaid obligation."
                ),
                "chapter_ref": "Q7, Q8",
                "instructions": [
                    (
                        "Map each transaction through explicit states from commitment "
                        "to purchase, receipt, acceptance, settlement, and closure. "
                        "Define required evidence and permitted transitions; never "
                        "let a marketplace status update alone establish bank "
                        "settlement or transfer ownership without supporting documents."
                    ),
                    (
                        "Assign immutable identifiers at the earliest controlled "
                        "step and preserve external references separately. Enforce "
                        "uniqueness for purchases, ticket seats, refunds, and "
                        "settlement events so repeated messages return the original "
                        "result rather than create duplicate economic activity."
                    ),
                    (
                        "Configure SkyBox or Automatiq through authorized integrations "
                        "and verify actual account capabilities before enabling "
                        "writes. Start in observation mode, compare proposed "
                        "changes with source inventory, and retain a manual "
                        "listing-freeze procedure for stale or contradictory feeds."
                    ),
                    (
                        "Reconcile purchase orders, carrier evidence, receiving "
                        "acceptance, card postings, platform statements, and bank "
                        "deposits independently. Route discrepancies to named "
                        "owners with aging limits; balancing aggregate cash "
                        "does not excuse missing serial numbers or "
                        "unexplained transaction-level deductions."
                    ),
                    (
                        "Run failure tests before the first live batch. "
                        "Replay duplicate events, interrupt delivery confirmations, "
                        "reverse settlements, and simulate simultaneous ticket sales; "
                        "confirm that inventory remains controlled, financial "
                        "history remains intact, and recovery does not "
                        "require deleting accounting records."
                    ),
                ],
                "fields": [
                    field(
                        "Transaction state machine and permitted transitions",
                        "textarea",
                        (
                            "Define states, transition evidence, responsible owners, "
                            "and timeout handling for merchandise and tickets. "
                            "Separate operational completion from financial closure, "
                            "and require explicit reversal events when "
                            "previously accepted or settled activity changes."
                        ),
                        (
                            "BG-041-001 moves through committed, purchased, shipped, "
                            "delivered, accepted, and settled states. Carrier "
                            "delivery cannot mark it accepted; the buyer's "
                            "receiving record is required. A $10,200 bank "
                            "receipt permits settled status after matching. "
                            "An ACH return creates a settlement-reversed "
                            "event and reopens the receivable without deleting history."
                        ),
                    ),
                    field(
                        "Idempotency key and immutable event identity",
                        "textarea",
                        (
                            "Specify deterministic keys for economic actions "
                            "and separate them from transport delivery "
                            "identifiers. Document uniqueness enforcement, retry "
                            "behavior, and payload conflict handling so "
                            "a repeated callback cannot create another "
                            "purchase, reimbursement, or inventory decrement."
                        ),
                        (
                            "A purchase action uses BG-041-001:PO-778:purchase:v1 "
                            "as its business key. The ledger stores "
                            "that key under a unique constraint and "
                            "returns the original result on replay. "
                            "If the same key arrives with $10,500 "
                            "instead of $10,000, processing stops in "
                            "an exception queue rather than overwriting the first event."
                        ),
                    ),
                    field(
                        "Double-entry postings and clearing-account boundaries",
                        "textarea",
                        (
                            "Describe the postings for acquisition, sale, "
                            "fees, rewards, and settlement under the "
                            "documented accounting policy. Keep inventory "
                            "basis, card liabilities, receivables, and "
                            "clearing balances separate, with reversals "
                            "referencing the original posting identifiers."
                        ),
                        (
                            "For a documented principal transaction, acquisition "
                            "debits inventory $10,000 and credits card "
                            "payable $10,000. Transfer debits receivables "
                            "$10,200 and credits sales $10,200; basis "
                            "moves from inventory to cost of sales. "
                            "Bank settlement clears the receivable. Freight "
                            "and eligible rebates follow separately documented "
                            "postings, never unexplained net adjustments."
                        ),
                    ),
                    field(
                        "Serial, seat, and entitlement uniqueness",
                        "textarea",
                        (
                            "Define the natural identity of merchandise "
                            "units and event entitlements. Explain how "
                            "split lots, seat pairs, suite capacities, "
                            "and partial transfers remain traceable "
                            "without making the same asset independently "
                            "available in multiple sales channels."
                        ),
                        (
                            "Ticket inventory uses event identifier, performance "
                            "time, section, row, seat, and source "
                            "order together. Eight seats become four "
                            "controlled pairs, but each underlying seat "
                            "retains one availability record. A suite "
                            "capacity of twelve admits no thirteenth "
                            "guest entitlement merely because two marketplaces "
                            "carry separate advertisements."
                        ),
                    ),
                    field(
                        "Multi-exchange inventory lock and stale-feed control",
                        "textarea",
                        (
                            "Record the authoritative inventory system, connector "
                            "latency expectations, and oversell prevention "
                            "method. Specify how an accepted sale "
                            "reserves seats immediately and how stale "
                            "connectors trigger listing suspension without "
                            "assuming marketplace updates are atomic."
                        ),
                        (
                            "The operator uses SkyBox as the configured "
                            "inventory authority and tests each enabled "
                            "exchange connector. A confirmed sale reserves "
                            "the pair locally before delisting messages "
                            "are sent. If an exchange acknowledgment "
                            "is missing for 90 seconds, affected "
                            "listings are frozen and reviewed; simultaneous "
                            "sales enter a human resolution queue."
                        ),
                    ),
                    field(
                        "Receiving and shipment three-way reconciliation",
                        "textarea",
                        (
                            "Match purchase-order units, dispatched serials, "
                            "and accepted receiving units. Record "
                            "quantity differences, insured-value evidence, "
                            "and settlement deductions separately so "
                            "a partial acceptance cannot silently "
                            "close the entire shipment or "
                            "misstate outstanding exposure."
                        ),
                        (
                            "The order requires twenty units at $510 "
                            "reimbursement each. Dispatch evidence lists "
                            "twenty serials, while receiving accepts "
                            "nineteen. Accepted reimbursement is $9,690; "
                            "the remaining $510 stays disputed. The "
                            "operator investigates the missing unit using "
                            "packing images and carrier weight, rather "
                            "than treating the reduced payment as full settlement."
                        ),
                    ),
                    field(
                        "Card statement, reward, and bank reconciliation",
                        "textarea",
                        (
                            "Match authorized purchases to posted charges "
                            "and cleared bank payments. Track rewards "
                            "separately by earning period and actual "
                            "posting, and distinguish pending authorizations "
                            "from final liabilities when investigating "
                            "apparent duplicate card activity."
                        ),
                        (
                            "A $10,000 authorization and its later "
                            "$10,000 posted charge represent one "
                            "purchase, not $20,000 of expense. "
                            "The statement payable reconciles to "
                            "$10,000 before other activity. A "
                            "$200 reward posts separately the following "
                            "cycle. Bank payment closes the liability "
                            "only after the bank debit and issuer credit match."
                        ),
                    ),
                    field(
                        "Refund, cancellation, and chargeback reversals",
                        "textarea",
                        (
                            "Define separate workflows for voluntary refunds, "
                            "event cancellation, postponed performances, and "
                            "payment disputes. Preserve original sale "
                            "records, allocate recoveries against the "
                            "correct basis, and prevent duplicate "
                            "customer refunds across platform and "
                            "manual payment channels."
                        ),
                        (
                            "A cancelled event affects four tickets "
                            "sold for $800 with $480 acquisition "
                            "basis. The platform processes the $800 "
                            "customer refund under its terms; the "
                            "operator tracks the separate $480 source "
                            "recovery. A refund identifier prevents "
                            "another manual $800 payment. Unrecovered "
                            "platform charges remain separately visible until resolved."
                        ),
                    ),
                    field(
                        "QA fixture pack and replay results",
                        "textarea",
                        (
                            "List repeatable test cases covering duplicates, "
                            "out-of-order events, missing records, partial "
                            "settlement, and connector failure. Specify "
                            "expected balances and inventory counts "
                            "before declaring automation ready for "
                            "live commitments or unattended "
                            "reconciliation runs."
                        ),
                        (
                            "The test pack sends one purchase event "
                            "three times, delivers acceptance before "
                            "carrier confirmation, and repeats a "
                            "$10,200 settlement callback twice. Expected "
                            "results remain one $10,000 purchase, "
                            "one receivable settlement, and twenty "
                            "inventory units transferred. Any duplicate "
                            "posting fails the release test and "
                            "keeps automated writes disabled."
                        ),
                    ),
                    field(
                        "Daily close evidence and exception ownership",
                        "textarea",
                        (
                            "Define the daily reconciliation deadline, "
                            "required exports, exception aging bands, "
                            "and close owner. Distinguish a fully "
                            "matched close from a provisional "
                            "close, preserving unresolved amounts "
                            "and explicit restrictions on further "
                            "capital deployment."
                        ),
                        (
                            "By 5 p.m., the operator archives "
                            "card postings, bank activity, receiving "
                            "acceptances, ticket inventory, and platform "
                            "settlements. A $510 receiving dispute "
                            "keeps the close provisional and "
                            "reduces that buying group's available "
                            "limit. The contractor owns document "
                            "collection; only the operator can "
                            "close the exception after evidence resolves the balance."
                        ),
                    ),
                ],
                "completion_gate": (
                    "Release live execution only after duplicate replay, partial "
                    "acceptance, settlement reversal, and stale-listing tests produce "
                    "the expected balances and inventory counts. Every unresolved "
                    "exception must have an owner, exposure amount, deadline, "
                    "and documented effect on purchasing capacity."
                ),
            },
            {
                "worksheet_id": "ws-04",
                "number": 4,
                "title": (
                    "Statutory, Licensing, Contract Addendum "
                    "& Compliance Audit"
                ),
                "purpose": (
                    "Convert ticketing statutes, resale licensing, sales-tax "
                    "requirements, and commercial agreements into executable "
                    "operating controls. Record applicable jurisdictions and "
                    "contract versions, distinguish statutory obligations from "
                    "platform conditions, and preserve evidence of lawful "
                    "acquisition, accurate pricing, authorized transfers, and "
                    "clear cancellation remedies."
                ),
                "chapter_ref": "Q5, Q9",
                "instructions": [
                    (
                        "Build the jurisdiction map from event location, customer "
                        "location, business presence, and transaction structure. "
                        "Verify current statutory text and effective dates "
                        "before applying any rule; document the actual "
                        "trigger rather than assuming every state treats "
                        "ticket resale identically."
                    ),
                    (
                        "Translate the federal BOTS Act into acquisition "
                        "restrictions and evidence requirements. Prohibit "
                        "circumvention of ticket limits, queues, or "
                        "access controls, and investigate supplier provenance "
                        "before reselling inventory acquired through channels "
                        "that cannot substantiate lawful purchasing methods."
                    ),
                    (
                        "Audit displayed ticket prices against federal "
                        "and applicable state requirements. Include mandatory "
                        "charges in the required total, identify "
                        "permitted exclusions precisely, and retain screenshots "
                        "showing the customer journey before enabling "
                        "a new sales channel or fee schedule."
                    ),
                    (
                        "Attach transaction-specific contract terms covering "
                        "acceptance, title, risk of loss, payment, "
                        "refunds, transfer rights, and dispute handling. "
                        "Separate terms negotiated with buying groups "
                        "from venue or platform rules the "
                        "operator cannot amend unilaterally."
                    ),
                    (
                        "Assign an owner and evidence location "
                        "for every licensing, tax, insurance, "
                        "and contract requirement. Recheck obligations "
                        "when entering another state or event "
                        "category, and stop only the affected "
                        "activity while correcting a documented "
                        "operating deficiency."
                    ),
                ],
                "fields": [
                    field(
                        "Jurisdiction map and current-source verification",
                        "textarea",
                        (
                            "Identify business locations, event states, "
                            "buyer locations, and sales channels "
                            "that may trigger obligations. Record "
                            "the governing source, verification date, "
                            "applicability analysis, and accountable reviewer "
                            "instead of substituting a generic "
                            "nationwide resale assumption."
                        ),
                        (
                            "The operator plans New York event "
                            "sales and California customer transactions. "
                            "The register assigns New York Arts "
                            "and Cultural Affairs Law Article 25 "
                            "to licensing review and California "
                            "Civil Code section 1770(a)(29) to "
                            "price-display review. Each entry requires "
                            "current official text, territorial analysis, "
                            "and dated evidence before the affected listings publish."
                        ),
                    ),
                    field(
                        "Federal BOTS Act acquisition restrictions",
                        "textarea",
                        (
                            "Translate 15 U.S.C. §45c into "
                            "specific acquisition and resale controls. "
                            "Address circumvention of technical controls "
                            "and applicable knowledge concerning unlawfully "
                            "obtained tickets, with supplier evidence "
                            "and escalation procedures for suspect "
                            "inventory provenance."
                        ),
                        (
                            "The purchasing policy forbids queue bypass, "
                            "CAPTCHA circumvention, and account rotation "
                            "used to defeat posted limits. "
                            "An eight-ticket purchase retains the "
                            "published limit and source receipt. "
                            "A supplier offering 400 restricted "
                            "presale tickets without provenance is "
                            "rejected pending evidence; attractive pricing "
                            "does not override 15 U.S.C. §45c acquisition controls."
                        ),
                    ),
                    field(
                        "Federal and state all-in ticket pricing",
                        "textarea",
                        (
                            "Document how 16 CFR Part 464 "
                            "and applicable state rules affect "
                            "displayed ticket totals and excluded "
                            "charges. Test actual checkout screens, "
                            "price prominence, fee descriptions, and "
                            "final payment disclosures across every "
                            "enabled channel."
                        ),
                        (
                            "A ticket has $160 seller price "
                            "and a mandatory $20 service "
                            "charge. The displayed total is "
                            "$180 before any separately permitted "
                            "government charges, not an initial "
                            "$160 headline. The audit captures "
                            "search, listing, cart, and payment "
                            "screens and checks California Civil "
                            "Code section 1770(a)(29) where applicable."
                        ),
                    ),
                    field(
                        "Reseller licensing, bonds, and platform permissions",
                        "textarea",
                        (
                            "Identify each applicable reseller license "
                            "or bond requirement and distinguish "
                            "it from platform account eligibility. "
                            "Record issued credentials, expiration dates, "
                            "scope limitations, and affected transaction "
                            "types before allowing activity that "
                            "depends on that permission."
                        ),
                        (
                            "For planned New York resale activity, "
                            "the reviewer checks licensing under "
                            "Arts and Cultural Affairs Law "
                            "§25.13 and related Article 25 "
                            "requirements. The launch checklist requires "
                            "the applicable issued license and "
                            "bond evidence before covered sales. "
                            "A marketplace seller account alone "
                            "does not satisfy a separate state licensing obligation."
                        ),
                    ),
                    field(
                        "Sales-tax resale certificates and collection duties",
                        "textarea",
                        (
                            "Separate purchases for resale from "
                            "taxable consumption and distinguish "
                            "marketplace collection from direct-sales "
                            "duties. Identify certificate acceptance, "
                            "nexus, filing, and recordkeeping "
                            "requirements using the applicable "
                            "state's statutes and official "
                            "administrative instructions."
                        ),
                        (
                            "California merchandise purchases use a "
                            "properly completed resale certificate "
                            "when eligible under Revenue and "
                            "Taxation Code §6091 and 18 "
                            "CCR §1668. The operator retains "
                            "seller acceptance and resale evidence. "
                            "A $10,000 resale purchase is "
                            "not treated as tax-free personal "
                            "consumption; direct ticket transactions receive "
                            "their own state and local tax analysis."
                        ),
                    ),
                    field(
                        "Buying-group acceptance and payment addendum",
                        "textarea",
                        (
                            "Draft measurable acceptance, inspection, "
                            "deduction, and payment clauses "
                            "using the applicable state's "
                            "enacted UCC provisions as "
                            "the legal framework. Identify "
                            "which obligations are negotiated "
                            "contract terms rather than "
                            "automatic statutory deadlines."
                        ),
                        (
                            "The addendum states: buyer reports "
                            "serial-specific shortages within one "
                            "business day after delivery and "
                            "pays accepted units within three "
                            "business days after acceptance. "
                            "These are negotiated deadlines, "
                            "reviewed against enacted UCC "
                            "§§2-513, 2-601, and 2-607. "
                            "An unrelated shipment dispute "
                            "does not authorize deductions from this accepted invoice."
                        ),
                    ),
                    field(
                        "Title, risk of loss, and insurance allocation",
                        "textarea",
                        (
                            "Specify when title and risk "
                            "transfer, who insures each "
                            "leg, and which party "
                            "pursues claims. Review the "
                            "applicable state's enacted UCC "
                            "rules and avoid assuming "
                            "that payment timing determines "
                            "risk allocation automatically."
                        ),
                        (
                            "The negotiated shipment clause keeps "
                            "transit risk with the operator "
                            "until signed delivery at the "
                            "approved receiving address, then "
                            "allocates receiving risk to "
                            "the buyer subject to inspection "
                            "terms. The reviewer checks "
                            "enacted UCC §§2-401 and "
                            "2-509. Cargo coverage of "
                            "$10,000 is verified separately from "
                            "carrier declared-value service."
                        ),
                    ),
                    field(
                        "Ticket cancellation, postponement, and transfer clauses",
                        "textarea",
                        (
                            "Specify remedies for cancellation, "
                            "postponement, failed transfer, and "
                            "seat substitution. Align customer "
                            "promises with source rights "
                            "and mandatory rules, including "
                            "refund timing, fee treatment, "
                            "and responsibility when the "
                            "operator cannot recover upstream "
                            "purchase costs."
                        ),
                        (
                            "The customer agreement distinguishes "
                            "cancelled events from rescheduled "
                            "performances and incorporates applicable "
                            "refund requirements. Four cancelled "
                            "tickets sold for $800 "
                            "create a separately tracked "
                            "customer obligation even if "
                            "the $480 upstream recovery "
                            "is delayed. Replacement seats "
                            "require the customer's agreement "
                            "where the contract does not "
                            "authorize equivalent substitution."
                        ),
                    ),
                    field(
                        "SSL and corporate-suite mandate boundaries",
                        "textarea",
                        (
                            "Document the actual rights "
                            "being brokered, venue transfer "
                            "conditions, guest capacity, hospitality "
                            "components, and authority to "
                            "collect money. Separate a "
                            "stadium seat license transfer "
                            "from an event-specific suite "
                            "booking and any associated "
                            "agency commission."
                        ),
                        (
                            "A corporate client authorizes one "
                            "twelve-person suite booking for "
                            "$12,000 plus an expressly "
                            "agreed $1,200 brokerage fee. "
                            "The venue contract controls "
                            "catering, guest credentials, and "
                            "transferability. The operator records "
                            "the $12,000 as client "
                            "funds under the agency "
                            "arrangement, not automatically as "
                            "operator revenue or an SSL acquisition."
                        ),
                    ),
                    field(
                        "Audit evidence, exceptions, and renewal calendar",
                        "textarea",
                        (
                            "Create an evidence register "
                            "linking each obligation to "
                            "its responsible owner, source "
                            "document, renewal date, and "
                            "affected activity. Define how "
                            "missing evidence restricts that "
                            "activity without obscuring unrelated "
                            "transactions that remain properly "
                            "documented and authorized."
                        ),
                        (
                            "The register stores pricing "
                            "screenshots, acquisition receipts, resale "
                            "certificates, insurance schedules, and "
                            "license records under deal "
                            "identifiers. A license renewal "
                            "gets reminders sixty and "
                            "thirty days before expiration. "
                            "Missing renewal evidence suspends "
                            "covered new listings while "
                            "existing customer obligations continue "
                            "to be serviced and recorded."
                        ),
                    ),
                ],
                "completion_gate": (
                    "Covered activity may proceed only when current-source "
                    "verification, applicable licensing, lawful acquisition evidence, "
                    "required price displays, tax treatment, and executed "
                    "transaction terms are recorded. Every exception must specify "
                    "the affected activity, corrective evidence, responsible owner, "
                    "and permitted interim handling of existing obligations."
                ),
            },
            {
                "worksheet_id": "ws-05",
                "number": 5,
                "title": (
                    "Automation Pipeline, Acquisition Flywheel "
                    "& Risk Fallback Tracker"
                ),
                "purpose": (
                    "Automate reconciliation and controlled inventory distribution "
                    "while preserving human authority over capital, exceptions, "
                    "and customer remedies. Build a repeatable acquisition "
                    "flywheel from settled deals and qualified relationships, "
                    "then rehearse fallback operations for issuer interruptions, "
                    "buying-group payment delays, connector outages, and ticket "
                    "price deterioration."
                ),
                "chapter_ref": "Q6, Q10",
                "instructions": [
                    (
                        "Inventory each automation's inputs, permitted actions, "
                        "credentials, and recovery path. Prioritize deal-commit "
                        "matching, card-statement reconciliation, and listing "
                        "synchronization; exclude acquisition automation that "
                        "circumvents ticket controls, and require explicit "
                        "operator authorization before changing exposure "
                        "limits or sending money."
                    ),
                    (
                        "Run new integrations in observation mode "
                        "against a representative historical batch. "
                        "Compare proposed state changes and "
                        "financial postings with operator-reviewed results, "
                        "then enable a small live "
                        "scope only after duplicate handling, "
                        "access controls, and failure alerts "
                        "work as designed."
                    ),
                    (
                        "Build acquisition from vetted counterparties, "
                        "documented allocations, and repeat corporate "
                        "buyers rather than indiscriminate outreach. "
                        "Track qualified conversations, signed mandates, "
                        "settled transactions, and repeat contribution "
                        "so the flywheel rewards collected "
                        "profit instead of inflated lead "
                        "counts or unpaid commitments."
                    ),
                    (
                        "Define circuit breakers for payment "
                        "aging, inventory staleness, reward "
                        "changes, and price decay. "
                        "Every breaker needs a "
                        "clear threshold, accountable owner, "
                        "manual fallback, and reopening "
                        "evidence; alerts without an "
                        "associated operating action merely "
                        "accelerate the delivery of bad news."
                    ),
                    (
                        "Exercise the recovery plan with "
                        "real exports and representative "
                        "transactions. Confirm the pod "
                        "can stop new commitments, "
                        "reconcile existing obligations, communicate "
                        "with customers, and repay "
                        "cards without relying on "
                        "the failed connector, marketplace "
                        "account, or issuer relationship."
                    ),
                ],
                "fields": [
                    field(
                        "Authorized integration map and least-privilege access",
                        "textarea",
                        (
                            "List each system, authorized "
                            "data source, credential owner, "
                            "read or write permission, "
                            "and business purpose. Separate "
                            "reconciliation access from payment "
                            "authority, and identify how "
                            "credentials are revoked when "
                            "a contractor or connector "
                            "no longer requires access."
                        ),
                        (
                            "The buying-group reconciler reads "
                            "approved purchase-order exports and "
                            "bank transactions but cannot "
                            "initiate payments. A configured "
                            "Automatiq connection manages authorized "
                            "ticket listings within its "
                            "documented permissions. Contractors receive "
                            "individual accounts rather than "
                            "shared credentials. Offboarding disables "
                            "access immediately and reviews "
                            "recent listing changes and exception closures."
                        ),
                    ),
                    field(
                        "Deal-commit ingestion and matching rules",
                        "textarea",
                        (
                            "Describe accepted input formats, "
                            "required purchase-order fields, "
                            "validation checks, and matching "
                            "tolerances. Prevent informal messages "
                            "from becoming binding commitments "
                            "without the required evidence, "
                            "and route inconsistent quantities "
                            "or reimbursement amounts to "
                            "an operator-owned exception queue."
                        ),
                        (
                            "An authorized CSV import "
                            "requires deal identifier, buyer "
                            "entity, SKU, quantity, unit "
                            "reimbursement, acceptance terms, and "
                            "document reference. Twenty units "
                            "at $510 must total "
                            "$10,200 exactly. An incoming "
                            "$10,250 total fails validation. "
                            "The system stores the "
                            "original file and proposed "
                            "match but creates no purchase authorization."
                        ),
                    ),
                    field(
                        "Card-float ledger and due-date alerts",
                        "textarea",
                        (
                            "Define the source of "
                            "statement dates, payment amounts, "
                            "reward postings, and bank "
                            "clearance. Establish alert timing "
                            "and payment verification steps "
                            "without treating a scheduled "
                            "payment request as proof "
                            "that the issuer received "
                            "the required funds."
                        ),
                        (
                            "The ledger imports the "
                            "actual $10,000 statement balance "
                            "and February 25 due "
                            "date. Alerts occur ten, "
                            "five, and two calendar "
                            "days before payment is "
                            "due. A February 22 "
                            "payment instruction remains pending "
                            "until bank debit and "
                            "issuer receipt reconcile; a "
                            "missing confirmation triggers direct operator review."
                        ),
                    ),
                    field(
                        "Qualified counterparty and corporate-buyer flywheel",
                        "textarea",
                        (
                            "Define the acquisition sequence "
                            "from qualified introduction through "
                            "paid pilot and repeat "
                            "mandate. Track acquisition effort "
                            "and collected contribution by "
                            "relationship, excluding unsupported commitments "
                            "and pass-through client spending "
                            "from the measure of "
                            "commercial productivity."
                        ),
                        (
                            "Ten vetted introductions produce "
                            "four underwriting calls, two "
                            "paid $2,000 merchandise pilots, "
                            "and one repeat counterparty. "
                            "Separately, three corporate-buyer meetings "
                            "produce one signed suite "
                            "mandate with a $1,200 "
                            "fee. Acquisition reporting counts "
                            "the collectible fee and "
                            "realized merchandise contribution, not "
                            "the client's $12,000 suite budget."
                        ),
                    ),
                    field(
                        "ACH delay and counterparty circuit breaker",
                        "textarea",
                        (
                            "Set aging thresholds from "
                            "contractual due dates rather "
                            "than purchase dates. Define "
                            "purchase suspension, collection escalation, "
                            "exposure reporting, and reopening "
                            "conditions, ensuring that a "
                            "promised payment or screenshot "
                            "does not substitute for "
                            "cleared funds."
                        ),
                        (
                            "A $9,690 accepted receivable "
                            "is due Friday under "
                            "Net-3 terms. If it "
                            "remains unpaid after the "
                            "agreed cutoff, new commitments "
                            "to that buyer stop. "
                            "The operator verifies payment "
                            "status through the bank "
                            "and contacts the buyer. "
                            "Reopening requires cleared funds "
                            "and explanation of the delay, not an ACH screenshot."
                        ),
                    ),
                    field(
                        "Issuer review, reward reduction, and shutdown fallback",
                        "textarea",
                        (
                            "Specify actions when an "
                            "issuer requests documents, changes "
                            "rewards, reduces limits, or "
                            "suspends purchasing. Preserve truthful "
                            "business records, honor repayment "
                            "obligations, and resize commitments "
                            "without misrepresenting transactions or "
                            "attempting to evade the "
                            "issuer's controls."
                        ),
                        (
                            "A card limit falls "
                            "from $30,000 to $5,000 "
                            "while $10,000 remains payable. "
                            "The operator stops card-funded "
                            "purchases, supplies requested invoices "
                            "through the issuer's verified "
                            "channel, and repays from "
                            "reserved cash. Cash-funded deals "
                            "resume only within existing "
                            "counterparty limits and positive "
                            "zero-rebate contribution; alternative accounts are not used to conceal activity."
                        ),
                    ),
                    field(
                        "Event price-decay automation and stop-loss action",
                        "textarea",
                        (
                            "Define event-relative markdown "
                            "dates, observable market inputs, "
                            "minimum pricing authority, and "
                            "human review thresholds. Distinguish "
                            "a planned loss-reduction sale "
                            "from an unauthorized pricing "
                            "error, and include transfer "
                            "deadlines that can make "
                            "inventory unsaleable before event start."
                        ),
                        (
                            "Twenty $120-basis tickets begin "
                            "at $180 each. At "
                            "fourteen days the authorized "
                            "price becomes $165, then "
                            "$145 at seven days. "
                            "With a modeled 10% "
                            "seller fee, $145 produces "
                            "$130.50 per ticket before "
                            "other costs. Any price "
                            "below $135 requires operator "
                            "review, considering actual transfer cutoffs and executable demand."
                        ),
                    ),
                    field(
                        "Connector outage and manual distribution fallback",
                        "textarea",
                        (
                            "Describe how stale inventory "
                            "is detected, affected listings "
                            "are frozen, and authoritative "
                            "records are exported. Specify "
                            "the manual sales sequence "
                            "and reconciliation procedure that "
                            "prevents duplicate allocation while "
                            "a marketplace or POS "
                            "connection remains unavailable."
                        ),
                        (
                            "After a connector exceeds "
                            "the configured freshness limit, "
                            "the operator pauses affected "
                            "listings using available authorized "
                            "controls and exports the "
                            "last verified seat ledger. "
                            "Manual sales use one "
                            "designated channel and reserve "
                            "seats before confirmation. Recovery "
                            "compares every sale and "
                            "delisting acknowledgment before multi-exchange distribution resumes."
                        ),
                    ),
                    field(
                        "Risk alert ownership and response service levels",
                        "textarea",
                        (
                            "Assign each alert category "
                            "a primary owner, backup, "
                            "response window, and immediate "
                            "containment action. Make customer "
                            "delivery failures, overdue card "
                            "payments, and duplicate sales "
                            "distinct from lower-priority reporting "
                            "differences that do not "
                            "change economic exposure."
                        ),
                        (
                            "A suspected duplicate seat "
                            "sale pages the operator "
                            "immediately and freezes that "
                            "event's affected inventory. An "
                            "unmatched $12 platform fee "
                            "enters the next daily "
                            "close queue. A missing "
                            "card payment confirmation two "
                            "days before the due "
                            "date triggers same-day bank "
                            "and issuer verification by the operator, with contractor backup documentation."
                        ),
                    ),
                    field(
                        "Automation acceptance test and rollback evidence",
                        "textarea",
                        (
                            "Define the measured improvement, "
                            "minimum test coverage, live "
                            "pilot boundaries, and rollback "
                            "trigger for each automation. "
                            "Preserve the prior configuration "
                            "and compare cash or "
                            "inventory outcomes rather than "
                            "declaring success solely because "
                            "a scheduled job completed."
                        ),
                        (
                            "A twenty-deal observation batch "
                            "must match all purchase "
                            "orders and bank receipts "
                            "without duplicate postings. The "
                            "first live release handles "
                            "only two $2,000 pilots. "
                            "Any unexplained balance change "
                            "disables writes and restores "
                            "the prior configuration. The "
                            "target is thirty minutes "
                            "saved per daily close with unchanged exception detection."
                        ),
                    ),
                ],
                "completion_gate": (
                    "Enable expanded automation only after the authorized "
                    "integration map, replay tests, measured pilot results, "
                    "and manual fallback rehearsal are complete. Every "
                    "high-severity alert must have an accountable responder "
                    "and a tested containment action that preserves customer "
                    "obligations, inventory integrity, and card repayment capacity."
                ),
            },
            {
                "worksheet_id": "ws-06",
                "number": 6,
                "title": (
                    "30-Day Launch Sprint, Pod KPI Scorecard "
                    "& Exit-Readiness Ledger"
                ),
                "purpose": (
                    "Launch a controlled small-team operation with measurable "
                    "evidence rather than throughput targets detached from "
                    "capital. Assign thirty-day deliverables, reconcile pod "
                    "capacity and canonical economics, and assemble transferable "
                    "records that support a future operating handoff or "
                    "sale without overstating recurring profit or transferable rights."
                ),
                "chapter_ref": "Q11, Q12",
                "instructions": [
                    (
                        "Treat the first thirty days as "
                        "a readiness and pilot sprint, "
                        "not a requirement to force "
                        "a transaction. The canonical first-deal "
                        "window is one to three "
                        "months; unresolved underwriting, licensing, "
                        "or repayment conditions take priority "
                        "over arbitrary launch-date pressure."
                    ),
                    (
                        "Assign deliverables to one full-time "
                        "operator and two contractors, "
                        "with explicit authority boundaries. "
                        "The operator controls commitments "
                        "and cash; contractors support "
                        "document collection, receiving reconciliation, "
                        "and listing operations within "
                        "defined permissions and documented "
                        "exception escalation procedures."
                    ),
                    (
                        "Choose KPI denominators before "
                        "collecting results. Track accepted "
                        "receivable aging, collectible contribution, "
                        "capital occupancy, listing accuracy, "
                        "refund exposure, and operator "
                        "minutes per closed deal; "
                        "gross reimbursements and client "
                        "suite budgets must not "
                        "masquerade as productivity or owner profit."
                    ),
                    (
                        "Review weekly results against "
                        "the canonical scenarios without "
                        "annualizing a single successful "
                        "pilot as recurring earnings. "
                        "Document gaps in verified "
                        "margin, repeat demand, staffing, "
                        "and settlement capacity before "
                        "increasing capital or adopting "
                        "the scaled five-person staffing model."
                    ),
                    (
                        "Build exit-readiness records from "
                        "the first transaction, including "
                        "contract assignability, reconciled cohorts, "
                        "account permissions, and customer "
                        "obligations. A transferable business "
                        "requires evidence that another "
                        "authorized operator can continue "
                        "the process without inheriting "
                        "hidden disputes or relying on personal card privileges."
                    ),
                ],
                "fields": [
                    field(
                        "Days 1–7 underwriting and capital foundation",
                        "textarea",
                        (
                            "Assign first-week deliverables for "
                            "entity verification, card terms, "
                            "banking separation, accounting policy, "
                            "and counterparty screening. Set "
                            "evidence-based completion criteria and "
                            "a startup-capital allocation that "
                            "does not consume cash "
                            "needed for repayments or "
                            "customer remedies."
                        ),
                        (
                            "The launch budget is "
                            "$30,000 within the $10,000–$55,000 "
                            "canonical range. Week one "
                            "allocates $5,000 to setup "
                            "and initial overhead, $10,000 "
                            "to repayment liquidity, $5,000 "
                            "to refund and interruption "
                            "buffer, and $10,000 to "
                            "potential pilots. Two buying "
                            "groups undergo verification; no "
                            "inventory is purchased solely to meet the calendar."
                        ),
                    ),
                    field(
                        "Days 8–14 ledger, terms, and dry-run completion",
                        "textarea",
                        (
                            "Define second-week deliverables for "
                            "contracts, statutory checks, ledger "
                            "configuration, and failure testing. "
                            "Identify which defects prevent "
                            "live commitments and which "
                            "can remain scheduled improvements "
                            "without changing cash safety, "
                            "customer rights, or inventory "
                            "accuracy."
                        ),
                        (
                            "By day fourteen, the "
                            "operator has signed pilot "
                            "purchase terms, verified applicable "
                            "ticket obligations, and replayed "
                            "twenty fixture events. A "
                            "duplicate settlement must create "
                            "zero additional receipts. Missing "
                            "inventory locks block live "
                            "ticket distribution; a cosmetic "
                            "report-layout issue remains scheduled "
                            "because it does not alter balances or operating decisions."
                        ),
                    ),
                    field(
                        "Days 15–21 controlled pilot and receiving proof",
                        "textarea",
                        (
                            "Set pilot size, capital "
                            "limits, purchase authority, and "
                            "evidence requirements for the "
                            "third week. Include an "
                            "alternative readiness deliverable "
                            "when no opportunity qualifies, "
                            "so the sprint never "
                            "rewards buying weak inventory "
                            "to manufacture activity."
                        ),
                        (
                            "The operator may authorize "
                            "one $2,000 merchandise pilot "
                            "after underwriting is complete. "
                            "The contractor records serials, "
                            "insured dispatch, delivery, and "
                            "acceptance. If no counterparty "
                            "qualifies by day twenty-one, "
                            "the team completes two "
                            "additional reference checks and "
                            "a settlement-delay rehearsal instead. "
                            "The one-to-three-month first-deal range remains the planning assumption."
                        ),
                    ),
                    field(
                        "Days 22–30 settlement review and next-cycle decision",
                        "textarea",
                        (
                            "Define the final-week review "
                            "of cleared proceeds, actual "
                            "costs, reward posting, open "
                            "disputes, and operator effort. "
                            "Specify the evidence needed "
                            "to repeat a pilot, "
                            "increase its limit, or "
                            "pause that channel without "
                            "declaring the whole launch successful prematurely."
                        ),
                        (
                            "A $2,000 pilot receives "
                            "$2,040 reimbursement, incurs $18 "
                            "freight and $10 actual "
                            "exception cost, and later "
                            "earns $40 eligible rewards. "
                            "Realized contribution is $12 "
                            "before rewards and $52 "
                            "after posting. The operator "
                            "reviews cleared payment and "
                            "handling time before repeating; "
                            "one profitable pilot does not justify a $10,000 exposure limit."
                        ),
                    ),
                    field(
                        "Pod roles, capacity, and authority boundaries",
                        "textarea",
                        (
                            "Assign the full-time operator "
                            "and contractors to recurring "
                            "work with estimated hours "
                            "and decision rights. Identify "
                            "the conditions requiring additional "
                            "capacity, and reconcile staffing "
                            "changes to the canonical "
                            "one-plus-two and two-plus-three "
                            "team structures."
                        ),
                        (
                            "The Base pod uses "
                            "one full-time operator, a "
                            "receiving contractor for twelve "
                            "hours weekly, and a "
                            "listing contractor for ten. "
                            "Only the operator authorizes "
                            "purchases or changes exposure "
                            "limits. At sustained workload "
                            "beyond documented capacity, the "
                            "scaled plan adds one "
                            "full-time operator and one contractor, producing two plus three."
                        ),
                    ),
                    field(
                        "Weekly KPI definitions and observed pilot scorecard",
                        "textarea",
                        (
                            "Define contribution, settlement timeliness, "
                            "inventory accuracy, capital occupancy, "
                            "and labor productivity with "
                            "explicit denominators. Keep small "
                            "sample sizes visible and "
                            "separate settled results from "
                            "open commitments or estimates "
                            "that could reverse before "
                            "final collection."
                        ),
                        (
                            "Two settled pilots generate "
                            "$104 contribution after posted "
                            "rewards on $4,000 purchase "
                            "basis, or 2.6%. Both "
                            "pay on time, producing "
                            "a two-of-two observed result, "
                            "not established reliability. Total "
                            "operator effort is ninety "
                            "minutes, or forty-five per "
                            "deal. Average capital occupancy "
                            "is eight days, and all forty serials reconcile."
                        ),
                    ),
                    field(
                        "Scenario progress and retained-margin reality check",
                        "textarea",
                        (
                            "Compare verified operating results "
                            "with all three canonical "
                            "annual profit targets. Identify "
                            "whether the actual mix "
                            "supports the 35% retained "
                            "share, and explain any "
                            "gap without substituting annualized "
                            "gross throughput for repeatable "
                            "owner earnings."
                        ),
                        (
                            "Targets remain $20,000 Conservative, "
                            "$143,500 Base, and $360,000 "
                            "Scaled annual owner profit. "
                            "Two pilots with $104 "
                            "contribution do not establish "
                            "any target. Their thin "
                            "merchandise spread requires a "
                            "separate portfolio-mix test; the "
                            "operator cannot simply apply "
                            "35% to pilot reimbursements "
                            "or claim Base earnings from an unverified suite pipeline."
                        ),
                    ),
                    field(
                        "Incident register and capital-release conditions",
                        "textarea",
                        (
                            "Record incidents by root "
                            "cause, affected cash, customer "
                            "impact, and corrective evidence. "
                            "Tie additional capital release "
                            "to resolved operating weaknesses "
                            "and demonstrated settlement behavior "
                            "rather than the passage "
                            "of time or an "
                            "unchanged credit-card limit."
                        ),
                        (
                            "The first pilot records "
                            "a one-day receiving delay "
                            "with $2,040 temporarily unaccepted. "
                            "The operator pauses the "
                            "second shipment, obtains written "
                            "acceptance, and updates the "
                            "receiving contact procedure. Capital "
                            "remains capped at $2,000 "
                            "per pilot until three "
                            "cycles settle within terms "
                            "and the revised process is evidenced in the ledger."
                        ),
                    ),
                    field(
                        "Exit-readiness records and transferability assessment",
                        "textarea",
                        (
                            "List the records another "
                            "authorized operator would need "
                            "to verify earnings and "
                            "continue service. Separate assignable "
                            "contracts from personal card "
                            "relationships, restricted platform accounts, "
                            "and venue licenses requiring "
                            "new approval or direct "
                            "counterparty permission."
                        ),
                        (
                            "The handoff package contains "
                            "monthly reconciliations, transaction cohorts, "
                            "signed buying-group terms, customer "
                            "obligations, inventory records, and "
                            "exception history. Personal commercial-card "
                            "capacity is excluded from "
                            "transferable assets. Each marketplace "
                            "and venue relationship receives "
                            "an assignability review. A "
                            "buyer must establish authorized "
                            "access rather than inherit passwords or assume automatic account transfer."
                        ),
                    ),
                    field(
                        "Thirty-day decision, next milestones, and owner sign-off",
                        "textarea",
                        (
                            "State the actual launch "
                            "status, unresolved work, next "
                            "capital limit, and dated "
                            "milestones. Distinguish verified completion "
                            "from planned activity, and "
                            "require an explicit operator "
                            "decision on continuation, pause, "
                            "or narrowed scope based "
                            "on evidence rather than narrative momentum."
                        ),
                        (
                            "Day thirty status is "
                            "merchandise pilot complete, card "
                            "payment reconciled, and ticket "
                            "distribution still paused pending "
                            "licensing verification. The next "
                            "cycle remains capped at "
                            "$2,000 per qualified pilot. "
                            "Within fourteen additional days, "
                            "the operator will complete "
                            "two counterparty checks and "
                            "the licensing review; no ticket revenue or expanded capacity is reported."
                        ),
                    ),
                ],
                "completion_gate": (
                    "Close the sprint only with an evidence-backed status "
                    "for every deliverable, reconciled pilot balances, named "
                    "incident owners, and an explicit next-cycle capital limit. "
                    "Expansion requires demonstrated capacity and collected "
                    "economics; exit readiness requires verified records and "
                    "documented transfer rights, not projected gross throughput."
                ),
            },
        ],
    }
