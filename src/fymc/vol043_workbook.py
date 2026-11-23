from __future__ import annotations


def build_volume_043_workbook() -> dict:
    def field(name: str, input_type: str, prompt: str, example: str) -> dict:
        return {
            "name": name,
            "type": input_type,
            "prompt": prompt,
            "example": example,
        }

    return {
        "workbook_id": "wb-043-live-event-super-bowl-and-vip-ticket-brokering",
        "volume_id": "vol-043-live-event-super-bowl-and-vip-ticket-brokering",
        "title": "Live-Event, Super Bowl & VIP Ticket Brokering — Operator Companion Workbook",
        "subtitle": (
            "6 Printable Operator Worksheets for Multi-Exchange Ticket Resale, "
            "Luxury-Suite Seat-Splitting, Tentpole Corporate Hospitality, "
            "Settlement Float, Lawful Automation, and Small-Team Execution"
        ),
        "worksheets": [
            {
                "worksheet_id": "ws-01",
                "number": 1,
                "title": "Arbitrage Deal, Counterparty Underwriting & Spread Qualification",
                "purpose": (
                    "Separate exchange resale, suite seat-splitting, and corporate hospitality "
                    "before committing inventory capital. Establish transferable rights, credible "
                    "counterparties, demand evidence, and fully burdened spreads. Convert attractive "
                    "headline prices into documented purchase limits that survive markdowns, "
                    "replacement claims, cancellation exposure, and delayed settlement."
                ),
                "chapter_ref": "Q1, Q2, Q6",
                "instructions": [
                    (
                        "Classify each opportunity into exactly one primary operating lane. Record "
                        "the event, venue, inventory rights, buyer segment, supplier payment dates, "
                        "and expected settlement trigger. Keep any bundled service obligations "
                        "separate from the underlying admission entitlement."
                    ),
                    (
                        "Verify the seller through independently obtained contact information, "
                        "purchase evidence, and the issuer transfer workflow. Compare the contracting "
                        "entity with the receiving bank account. Treat possession of a screenshot "
                        "as insufficient evidence of transferable admission rights."
                    ),
                    (
                        "Build comparable sales from timestamped evidence rather than asking prices "
                        "alone. Normalize section, row, seat adjacency, package contents, delivery "
                        "timing, and buyer fees. Write the observed demand shock that would invalidate "
                        "the proposed purchase price."
                    ),
                    (
                        "Calculate contribution after acquisition, exchange or collection fees, "
                        "unsold inventory, expected claims, settlement carrying cost, and allocated "
                        "execution labor. Label every modeled deduction and prevent the same "
                        "markdown or supplier charge from appearing twice."
                    ),
                    (
                        "Commit only within documented concentration and liquidity limits. Require "
                        "another operator to inspect high-value rights, contract restrictions, and "
                        "cash exposure before payment. Archive the evidence supporting the decision, "
                        "including rejected deals and their specific failure reasons."
                    ),
                ],
                "fields": [
                    field(
                        "Operating lane and settlement profile",
                        "textarea",
                        (
                            "Identify whether this deal involves multi-exchange resale, a divisible "
                            "suite entitlement, or a corporate hospitality package. Describe the "
                            "inventory acquired, capital commitment, customer payment mechanism, "
                            "and event-dependent settlement exposure without combining distinct lanes."
                        ),
                        (
                            "Deal EX-043-001 buys 20 transferable basketball tickets for $6,000 "
                            "and targets $10,000 in gross sales through SkyBox-connected exchanges. "
                            "The supplier receives payment immediately; the modeled exchange "
                            "settlement arrives seven days after the event. Suite and hospitality "
                            "transactions receive separate deal identifiers, contracts, capital "
                            "budgets, and settlement calendars."
                        ),
                    ),
                    field(
                        "Counterparty identity and independent verification",
                        "textarea",
                        (
                            "Document the supplier's contracting entity, independently verified "
                            "contact channel, payment beneficiary, purchase evidence, and dispute "
                            "history. Specify the exact discrepancy that suspends payment and "
                            "identify who resolves that discrepancy before inventory enters circulation."
                        ),
                        (
                            "For EX-043-001, the operator matches the supplier agreement, issuer "
                            "receipt, and bank beneficiary to one incorporated reseller. A callback "
                            "uses the number independently obtained from the reseller's established "
                            "business listing. A last-minute request to pay a personal account "
                            "suspends the $6,000 transfer until the discrepancy is resolved."
                        ),
                    ),
                    field(
                        "Admission rights and transfer restrictions",
                        "textarea",
                        (
                            "Record event identifiers, section and row, seat numbers, transfer "
                            "availability, restricted resale terms, and delivery deadlines. For "
                            "suite or hospitality inventory, identify whether individual admissions "
                            "and promised amenities may actually be sold separately."
                        ),
                        (
                            "Suite SU-043-004 contains 16 admissions, but the venue agreement "
                            "must expressly permit separate guest sales and identify the authorized "
                            "host. Parking, catering, and early entry are recorded as distinct "
                            "rights. If the venue permits invited guests but prohibits commercial "
                            "seat-splitting, the proposed resale structure is rejected before payment."
                        ),
                    ),
                    field(
                        "Comparable demand and evidence quality",
                        "textarea",
                        (
                            "List comparable transactions with observation times, inventory "
                            "attributes, gross buyer prices, and evidence sources. Separate "
                            "completed sales from active listings, then explain the adjustments "
                            "for adjacency, delivery certainty, event timing, and included hospitality services."
                        ),
                        (
                            "The basketball basket uses eight documented sales between $470 "
                            "and $530 per seat for the same section and adjacent rows. "
                            "The model uses $500 per ticket rather than a $650 active "
                            "listing. A starter injury or a 15% decline in comparable "
                            "completed prices triggers immediate re-underwriting of remaining inventory."
                        ),
                    ),
                    field(
                        "Exchange resale spread qualification",
                        "textarea",
                        (
                            "Calculate the exchange lane's expected owner contribution using "
                            "gross sales before seller fees. Include acquisition, fee assumptions, "
                            "inventory slippage, expected event claims, payout carrying cost, "
                            "and execution allocation, with an explicit treatment for forecast markdowns."
                        ),
                        (
                            "Gross sales of $10,000 less $6,000 acquisition produce $4,000 "
                            "retained spread. Deduct $1,000 exchange fees, $300 forecast slippage, "
                            "$200 expected event losses, $60 carrying cost, and $240 execution "
                            "allocation for $2,200 contribution. If actual sales already reflect "
                            "the $300 markdown, remove that forecast deduction during reconciliation."
                        ),
                    ),
                    field(
                        "Suite seat-splitting spread qualification",
                        "textarea",
                        (
                            "Calculate suite economics using the entire suite commitment rather "
                            "than only sold seats. Include seat capacity, contracted amenities, "
                            "collection charges, unsold admissions, event exposure, settlement "
                            "timing, and the labor needed to coordinate guests and venue access."
                        ),
                        (
                            "Sixteen suite admissions at $1,250 create $20,000 modeled gross "
                            "sales against a $12,000 suite acquisition. Deduct $600 collection "
                            "fees, $1,000 slippage, $400 expected event losses, $120 carrying "
                            "cost, and $800 coordination expense. Contribution is $5,080; the "
                            "operator still owes the full suite cost if several admissions remain unsold."
                        ),
                    ),
                    field(
                        "Tentpole hospitality spread qualification",
                        "textarea",
                        (
                            "Define each package component and the rights supporting its sale. "
                            "Calculate contribution after admission and amenity acquisition, "
                            "collections, unsold commitments, supplier failure exposure, delivery "
                            "labor, and longer-dated capital usage associated with corporate buyers."
                        ),
                        (
                            "Ten F1 packages at $5,000 produce $50,000 gross billings. "
                            "Admission and contracted amenities cost $30,000. Collection fees "
                            "of $1,500, slippage of $2,000, event-loss provision of $1,500, "
                            "carrying cost of $400, and delivery expense of $2,200 leave "
                            "$12,400 contribution. No paddock access is advertised without documented rights."
                        ),
                    ),
                    field(
                        "Supplier allotments and playoff-option strips",
                        "textarea",
                        (
                            "Describe sponsor-allotment provenance and any NFL or NBA seat-license "
                            "or playoff-strip conditions. Identify contingent games, purchase "
                            "obligations, refund beneficiaries, transfer limitations, and the "
                            "probability assumptions used to value rights that may never become admissions."
                        ),
                        (
                            "An NBA playoff strip requires $8,000 upfront and provides "
                            "issuer credits for unplayed games under its written terms. "
                            "The operator verifies whether those credits belong to the "
                            "original account holder or the acquiring entity. A sponsor "
                            "allotment is excluded when its agreement restricts commercial resale, regardless of quoted spread."
                        ),
                    ),
                    field(
                        "Concentration limits and stress purchase ceiling",
                        "textarea",
                        (
                            "Set limits by event, issuer, supplier, exchange, and settlement "
                            "week. Recalculate the acquisition ceiling under lower selling "
                            "prices, slower payouts, and replacement claims, then compare peak "
                            "cash exposure with unrestricted working capital rather than bank balance alone."
                        ),
                        (
                            "A $30,000 launch treasury limits one event's acquisition exposure "
                            "to $6,000 and one supplier's exposure to $9,000. For the "
                            "basketball basket, a 20% gross-sales reduction to $8,000 materially "
                            "compresses contribution. The operator refuses an additional $4,000 "
                            "purchase because it would breach the event limit before existing settlement clears."
                        ),
                    ),
                    field(
                        "Investment decision and evidence packet",
                        "textarea",
                        (
                            "Record the purchase decision, maximum payable amount, responsible "
                            "operator, unresolved operational conditions, and evidence locations. "
                            "Specify which new information forces a fresh decision rather "
                            "than allowing an old authorization to cover materially changed inventory."
                        ),
                        (
                            "EX-043-001 is authorized at no more than $6,000 after issuer "
                            "transfer eligibility and beneficiary identity are verified. The "
                            "packet contains the supplier agreement, inventory manifest, comparable "
                            "sales, and stress calculation. Any seat substitution, changed "
                            "beneficiary, transfer restriction, or event-date change requires a new documented purchase decision."
                        ),
                    ),
                ],
                "completion_gate": (
                    "Advance only when each proposed purchase has a verified rights chain, "
                    "lane-specific contribution calculation, independently checked supplier, "
                    "documented cash ceiling, and a named operator accountable for unresolved conditions."
                ),
            },
            {
                "worksheet_id": "ws-02",
                "number": 2,
                "title": "Unit Economics, Reserve Float & Working-Capital Calculator",
                "purpose": (
                    "Reconcile every operating model to the supplied Formula v2.0 scenarios "
                    "while distinguishing gross billings, retained spread, owner profit, and "
                    "available cash. Model settlement delays, customer liabilities, inventory "
                    "commitments, expected losses, and restricted reserves without treating "
                    "borrowed principal or customer deposits as earnings."
                ),
                "chapter_ref": "Q3, Q4",
                "instructions": [
                    (
                        "Enter the three canonical scenarios before building any deal forecast. "
                        "Preserve gross volume, retained share, owner profit, and staffing exactly. "
                        "Treat the detailed expense allocations below as illustrative reconciliation "
                        "assumptions rather than additional supplied scorecard inputs."
                    ),
                    (
                        "Normalize exchange statements to one gross-sales basis and show fees "
                        "once. Separate customer taxes collected for remittance from operator "
                        "revenue. Assess principal-versus-agent presentation from the actual contract "
                        "rather than assuming that a percentage determines accounting treatment."
                    ),
                    (
                        "Build daily cash movements from supplier deposits through final customer "
                        "settlement. Mark contractual release conditions and model actual payout "
                        "delays. Never assume an exchange receivable can fund another purchase "
                        "before the funds become available in the operating account."
                    ),
                    (
                        "Maintain separate schedules for expected economic losses and cash retained "
                        "against potential claims. A transfer into a reserve account does not "
                        "create another expense. Reconcile provisions, actual losses, releases, "
                        "and remaining obligations at each reporting close."
                    ),
                    (
                        "Stress the largest event with lower prices, replacement penalties, "
                        "postponement, and a longer settlement interval. Calculate the funding "
                        "gap without using protected customer funds. Set the next purchasing "
                        "limit from unrestricted liquidity after all near-term obligations."
                    ),
                ],
                "fields": [
                    field(
                        "Gross billings, retained share, and presentation",
                        "textarea",
                        (
                            "Define gross transaction volume, acquisition pass-through, retained "
                            "spread, recognized revenue presentation, and owner profit. Explain "
                            "how exchange net deposits are normalized and where a contract-specific "
                            "ASC 606 principal-versus-agent assessment changes presentation without changing cash economics."
                        ),
                        (
                            "The Base model has $1,010,000 gross billings, $606,000 acquisition "
                            "cost, and $404,000 retained spread at 40%. Under the scorecard's "
                            "net-presentation assumption, retained revenue is $404,000. Actual "
                            "ASC 606 presentation follows the control assessment in ASC "
                            "606-10-55-36 through 55-40; a principal presentation does not create additional economic profit."
                        ),
                    ),
                    field(
                        "Conservative scenario reconciliation",
                        "textarea",
                        (
                            "Reproduce the Conservative scenario exactly, then allocate its "
                            "remaining expense envelope to realistic operating categories. Show "
                            "gross margin basis, retained margin basis, annual owner profit, "
                            "and staffing while preserving the distinction between forecast losses and cash reserves."
                        ),
                        (
                            "Gross billings $220,000 minus acquisition $132,000 leave $88,000. "
                            "Illustrative deductions are fees $17,600, slippage $6,600, event "
                            "losses $4,400, carrying cost $1,400, fixed overhead $21,600, "
                            "and contractor labor $10,000. Total deductions equal $61,600; "
                            "owner profit is $26,400, or 12% gross and 30% retained, with 1 FT plus 2 C."
                        ),
                    ),
                    field(
                        "Base scenario reconciliation",
                        "textarea",
                        (
                            "Reproduce the Base scenario exactly and show every deduction "
                            "between retained spread and owner profit. Confirm that the "
                            "retained net margin and gross net margin use different "
                            "denominators, and identify the operating assumptions needed to achieve the result."
                        ),
                        (
                            "Gross billings $1,010,000 minus acquisition $606,000 leave $404,000. "
                            "Illustrative fees $70,700, slippage $20,200, event losses $15,150, "
                            "carrying cost $6,050, fixed overhead $72,000, and contractor "
                            "labor $28,000 total $212,100. Owner profit is $191,900: "
                            "19% of gross and 47.5% of retained revenue, with 1 FT plus 2 C."
                        ),
                    ),
                    field(
                        "Scaled small-team scenario reconciliation",
                        "textarea",
                        (
                            "Reproduce the Scaled scenario while identifying the labor and "
                            "channel-mix assumptions behind its lower expense burden. Preserve "
                            "the five-person team and show how paid staffing fits the "
                            "operating budget without treating unpaid owner effort as purchased labor."
                        ),
                        (
                            "Gross billings $1,800,000 less acquisition $1,080,000 leave $720,000. "
                            "Illustrative fees $90,000, slippage $18,000, event losses $18,000, "
                            "carrying cost $6,000, fixed operations including nonowner FT "
                            "payroll $96,000, and part-time contractor labor $24,000 total "
                            "$252,000. Owner profit is $468,000, or 26% gross and 65% retained, for 2 FT plus 3 C."
                        ),
                    ),
                    field(
                        "Startup treasury and recurring operating budget",
                        "textarea",
                        (
                            "Allocate startup capital between inventory, unrestricted liquidity, "
                            "operating runway, and claim reserves. Reconcile recurring overhead "
                            "and paid labor to the supplied monthly operating range, "
                            "and state whether owner distributions and personal taxes are excluded from the model."
                        ),
                        (
                            "A $30,000 launch allocation assigns $12,000 to inventory, "
                            "$8,000 to unrestricted liquidity, $6,000 to runway, and "
                            "$4,000 to segregated claim cash. Illustrative monthly overhead "
                            "plus paid labor equals $2,633.33 Conservative, $8,333.33 Base, "
                            "and $10,000 Scaled, within the $1,800–$11,000 range. Owner distributions and personal income taxes are tracked separately."
                        ),
                    ),
                    field(
                        "Exchange settlement and carrying-cost schedule",
                        "textarea",
                        (
                            "Enter acquisition dates, event dates, documented exchange payout "
                            "terms, bank availability, financing rate, and extension stress. "
                            "Calculate carrying cost from actual cash-days outstanding, not "
                            "from the listing date or the date a buyer places an order."
                        ),
                        (
                            "The $6,000 ticket basket is purchased 23 days before the "
                            "event and modeled to settle seven days afterward, creating "
                            "30 funded days. At a hypothetical 12% annual simple rate "
                            "using a 360-day convention, carrying cost is $60. "
                            "Another 21 days of delay adds $42; each exchange's actual agreement controls timing."
                        ),
                    ),
                    field(
                        "Suite and hospitality deposit waterfall",
                        "textarea",
                        (
                            "Map supplier deposits, customer deposits, remaining balances, "
                            "restricted refund money, and service delivery milestones for "
                            "suite and hospitality transactions separately. Identify the "
                            "maximum own-cash requirement under supplier default rather than merely subtracting deposits from purchase cost."
                        ),
                        (
                            "The $50,000 hospitality deal collects $25,000 from customers "
                            "and owes suppliers $18,000 upfront plus $12,000 later. "
                            "If customer deposits remain fully refundable while supplier "
                            "payments are nonrecoverable, the $25,000 stays protected and "
                            "the operator needs separate supplier funding. The deposit does not automatically reduce economic exposure to $5,000."
                        ),
                    ),
                    field(
                        "Expected loss provision and restricted cash",
                        "textarea",
                        (
                            "Separate modeled event-loss expense from cash retained to meet "
                            "claims. Track opening balances, new estimates, realized losses, "
                            "releases, and remaining liabilities, explaining why neither "
                            "segregating cash nor paying an already provided claim creates a second economic deduction."
                        ),
                        (
                            "The Base bridge includes $15,150 of expected event losses. "
                            "Treasury separately retains $20,000 in claim cash because "
                            "liquidity needs can exceed expected losses. A $3,000 "
                            "covered claim consumes provision and cash; it is not "
                            "deducted again from the same forecast. Any revised loss estimate changes the expense bridge once."
                        ),
                    ),
                    field(
                        "Double-sale, postponement, and markdown stress",
                        "textarea",
                        (
                            "Model separate operational shocks rather than hiding all risk "
                            "inside one percentage. Specify the contractual penalty basis, "
                            "replacement cost, event postponement duration, remaining inventory "
                            "markdown, expected recoveries, and incremental carrying cost before calculating the liquidity draw."
                        ),
                        (
                            "A hypothetical marketplace agreement charges a penalty equal "
                            "to 200% of a $1,000 failed order, creating a "
                            "$2,000 penalty before any separately assessed replacement "
                            "charge. Combine that stress with $1,500 inventory markdown "
                            "and $42 extra carrying cost for $3,542 exposure. Actual contract wording determines whether penalties and replacement charges stack."
                        ),
                    ),
                    field(
                        "Purchase capacity and profit-to-cash bridge",
                        "textarea",
                        (
                            "Calculate spendable cash after customer liabilities, restricted "
                            "reserves, supplier balances, operating commitments, and unsettled "
                            "receivables. Reconcile owner profit to cash generated by "
                            "changes in inventory and receivables, and set a purchase limit that preserves required liquidity."
                        ),
                        (
                            "Bank cash of $42,000 less $12,000 customer refund liabilities, "
                            "$8,000 claim cash, $7,000 supplier balances, and $5,000 "
                            "operating commitments leaves $10,000 unrestricted. Preserving a "
                            "$6,000 liquidity floor permits $4,000 of new purchases. "
                            "A separate $9,000 exchange receivable increases neither bank cash nor today's purchase capacity."
                        ),
                    ),
                ],
                "completion_gate": (
                    "Advance only when all three canonical profit totals reconcile exactly, "
                    "each margin has its correct denominator, reserve cash is distinct from "
                    "expense, and the stressed cash calendar supports the proposed purchase limit."
                ),
            },
            {
                "worksheet_id": "ws-03",
                "number": 3,
                "title": "Execution, Idempotent Ledger & QA Pre-Flight Sheet",
                "purpose": (
                    "Translate each approved purchase into a traceable inventory lifecycle "
                    "from acquisition through settlement. Use stable identifiers, atomic holds, "
                    "delivery evidence, and reconciliation controls to prevent duplicate sales, "
                    "repeated transfers, unsupported invoices, and false profit created by "
                    "unmatched exchange deposits or missing liabilities."
                ),
                "chapter_ref": "Q7, Q8",
                "instructions": [
                    (
                        "Assign immutable identifiers to deals, individual admissions, orders, "
                        "transfers, invoices, and settlement lines. Store source-system identifiers "
                        "alongside internal identifiers. Keep customer names out of primary keys "
                        "so corrections do not accidentally create new inventory or duplicate transactions."
                    ),
                    (
                        "Model inventory states explicitly and require an atomic reservation "
                        "before accepting an order. Request delisting across every connected "
                        "exchange immediately. Treat slow or missing acknowledgments as a "
                        "sell-risk condition requiring intervention, not as evidence that inventory disappeared."
                    ),
                    (
                        "Make every external side effect retry-safe through durable operation "
                        "records and source-reference checks. After an ambiguous timeout, inspect "
                        "the provider's status before retrying. A repeated webhook must never "
                        "produce another transfer, invoice, refund, or ledger posting."
                    ),
                    (
                        "Inspect seat identity, adjacency, delivery deadlines, package descriptions, "
                        "pricing, and customer instructions before publication. For corporate "
                        "packages, reconcile the admission manifest with the venue agreement, "
                        "amenity vouchers, and named delivery responsibilities before issuing the final invoice."
                    ),
                    (
                        "Close each event through a three-way match of orders, delivery evidence, "
                        "and settlement lines. Investigate every variance rather than posting "
                        "a balancing plug. Preserve unresolved claims and payout holds in "
                        "the close packet until their actual resolution is documented."
                    ),
                ],
                "fields": [
                    field(
                        "Inventory identity and source manifest",
                        "textarea",
                        (
                            "Define stable deal and admission identifiers, source purchase "
                            "references, event identifiers, seat attributes, acquisition allocation, "
                            "and rights evidence. Describe how corrected venue metadata "
                            "is versioned without duplicating inventory or overwriting the original purchase audit trail."
                        ),
                        (
                            "EX-043-001 contains admissions EX-043-001-001 through EX-043-001-020, "
                            "each allocated $300 acquisition cost. Admission 001 records "
                            "the issuer event identifier, section 112, row 8, "
                            "seat 3, and supplier invoice reference. A corrected "
                            "event start time creates a metadata revision while the admission identifier and original source evidence remain unchanged."
                        ),
                    ),
                    field(
                        "Atomic reservation and cross-channel holds",
                        "textarea",
                        (
                            "Describe the authoritative inventory state machine and compare-and-set "
                            "reservation operation. Record how SkyBox, Automatiq, or Logitix "
                            "connections broadcast holds across StubHub, Vivid Seats, SeatGeek, "
                            "and TickPick, including the response to incomplete synchronization."
                        ),
                        (
                            "An available admission changes atomically to held with order "
                            "ORD-884 as owner of the reservation. Hold requests are "
                            "sent through the verified POS integrations to every active "
                            "channel. If TickPick acknowledgment misses the internal five-second "
                            "target, the operator pauses affected listings and investigates; the target is an internal control, not a platform promise."
                        ),
                    ),
                    field(
                        "Order intake and duplicate-event handling",
                        "textarea",
                        (
                            "Specify the event identity, payload fingerprint, durable receipt "
                            "record, and processing status used for incoming marketplace "
                            "notifications. Distinguish exact duplicates from changed order "
                            "versions, and explain how conflicts are preserved for investigation rather than silently discarded."
                        ),
                        (
                            "The receipt key combines provider name and provider event "
                            "identifier. A second identical notification for ORD-884 returns "
                            "the stored processing outcome without creating another sale. "
                            "A changed payload with the same event identifier is "
                            "quarantined with both fingerprints. A genuine order revision receives its own version and an explicit transition check."
                        ),
                    ),
                    field(
                        "Transfer operation and timeout recovery",
                        "textarea",
                        (
                            "Define the transfer operation key, recipient validation, provider "
                            "reference, delivery evidence, and recovery path after an "
                            "ambiguous response. Explain how an operator determines whether "
                            "a transfer succeeded before issuing another request or changing the buyer's delivery instructions."
                        ),
                        (
                            "Transfer operation TR-884-001 links ORD-884, admission 001, and "
                            "the buyer-confirmed delivery address. If the provider times "
                            "out, the operation remains pending while the operator "
                            "checks the issuer activity record. A successful issuer "
                            "reference closes the existing operation; another request is prohibited until the original transfer state is resolved."
                        ),
                    ),
                    field(
                        "Economic subledger and accounting boundary",
                        "textarea",
                        (
                            "Design separate records for gross order value, inventory "
                            "cost, fees, retained spread, expected losses, and cash "
                            "movements. State how the economic subledger reconciles to "
                            "the general ledger without automatically imposing agent or principal accounting on every contract."
                        ),
                        (
                            "For a $500 admission with $300 acquisition and $50 "
                            "seller fee, the subledger records $500 gross value, "
                            "$300 inventory cost, $200 retained spread, and $150 "
                            "before other costs. The accounting mapping follows the "
                            "contract assessment. The $450 exchange receivable is recorded as a settlement amount, not mistaken for another $450 sale."
                        ),
                    ),
                    field(
                        "Listing and buyer-facing pre-flight inspection",
                        "textarea",
                        (
                            "Record the reviewer, inspection timestamp, actual seats, quantity "
                            "rules, total displayed price, delivery timing, restrictions, "
                            "and package inclusions. Identify which differences between "
                            "the listing and source entitlement require withdrawal before accepting any customer order."
                        ),
                        (
                            "The reviewer confirms two adjacent seats in section 112, "
                            "row 8, with no aisle claim and no included "
                            "parking. The buyer-facing total includes mandatory seller "
                            "charges as required by the applicable pricing rules. "
                            "A listing that promises instant transfer is withdrawn when the issuer will release transfer access only three days before the event."
                        ),
                    ),
                    field(
                        "Suite guest manifest and service delivery",
                        "textarea",
                        (
                            "Define the suite admission roster, host responsibility, guest "
                            "communication timeline, parking allocation, catering cutoff, accessibility "
                            "coordination, and arrival escalation. Separate admission delivery "
                            "from optional service completion so an amenity dispute cannot erase the underlying fulfillment record."
                        ),
                        (
                            "SU-043-004 has 16 admission records, one venue-approved host, "
                            "and four separately numbered parking passes. Catering "
                            "changes close 72 hours before the event under "
                            "the venue contract. The host checks guest entry "
                            "status at arrival; a missing meal voucher creates a service exception rather than falsely marking a delivered admission as undelivered."
                        ),
                    ),
                    field(
                        "Corporate invoice and bundle reconciliation",
                        "textarea",
                        (
                            "Match the corporate purchase order, package components, supplier "
                            "commitments, customer invoice, deposit receipt, and delivery "
                            "evidence. Identify tax and service-charge treatment separately, "
                            "and specify how partial package changes create documented credits instead of informal reductions."
                        ),
                        (
                            "The ten-package F1 invoice totals $50,000 before any "
                            "separately assessed tax outside the scorecard basis. "
                            "A $25,000 deposit and $25,000 balance match the "
                            "purchase order. If one contracted transfer service "
                            "is removed for a $500 credit, a linked credit document reduces the customer balance and the package delivery checklist together."
                        ),
                    ),
                    field(
                        "Settlement matching and variance resolution",
                        "textarea",
                        (
                            "Specify the matching keys for orders, exchange settlement "
                            "lines, bank deposits, fees, adjustments, and reserves. "
                            "Describe the evidence needed to resolve a short "
                            "payment and prevent an unexplained difference from becoming either invented revenue or an unsupported expense."
                        ),
                        (
                            "For $10,000 gross orders and $1,000 seller fees, "
                            "expected settlement is $9,000 before other documented "
                            "adjustments. A bank deposit of $8,800 leaves "
                            "$200 unmatched. If the statement identifies a "
                            "temporary reserve hold, record a receivable classification rather than an expense; if it documents a valid claim, apply the relevant loss treatment."
                        ),
                    ),
                    field(
                        "Event close and evidence retention",
                        "textarea",
                        (
                            "Define event-close criteria, outstanding claims, reserve release "
                            "conditions, access permissions, retention schedules, and the "
                            "person responsible for final reconciliation. Explain how "
                            "late adjustments reopen the relevant event record without altering previously preserved source documents."
                        ),
                        (
                            "EX-043-001 closes operationally after all 20 admissions "
                            "have delivery evidence, but treasury close waits "
                            "for the final settlement and resolution of "
                            "open claims. The packet preserves orders, transfers, "
                            "supplier invoices, and statement matches. A later $100 adjustment posts as a new linked entry with its source notice, leaving the original close evidence intact."
                        ),
                    ),
                ],
                "completion_gate": (
                    "Advance only after a simulated duplicate webhook, transfer timeout, "
                    "cross-channel hold failure, and short settlement each produce one "
                    "traceable outcome without duplicate inventory, duplicate cash postings, or unsupported balancing entries."
                ),
            },
            {
                "worksheet_id": "ws-04",
                "number": 4,
                "title": "Statutory, Licensing, Contract Addendum & Compliance Audit",
                "purpose": (
                    "Convert applicable ticketing requirements into documented operating "
                    "controls. Audit lawful acquisition, reseller licensing, mandatory price "
                    "disclosures, transfer rights, cancellation remedies, and truthful hospitality "
                    "claims. Attach concrete contract terms and jurisdiction-specific evidence "
                    "instead of relying on generic assurances from suppliers or software vendors."
                ),
                "chapter_ref": "Q5, Q9",
                "instructions": [
                    (
                        "Map the business location, event location, buyer jurisdiction, sales "
                        "channel, and transaction structure before applying a rule. Record "
                        "the operative statutory provision and verification date. A license "
                        "or practice accepted in one jurisdiction does not establish permission elsewhere."
                    ),
                    (
                        "Inspect acquisition methods against 15 U.S.C. §45c and issuer terms. "
                        "Permit authorized inventory management and transfer workflows while "
                        "prohibiting queue circumvention, purchase-limit evasion, and acquisition "
                        "from sources whose prohibited procurement method is known or should be known."
                    ),
                    (
                        "Audit all-in pricing at the first displayed offer and again at "
                        "checkout. Use 16 CFR Part 464 for covered live-event ticket "
                        "offers and apply stricter applicable state requirements. Capture "
                        "screenshots showing the actual consumer experience rather than only internal price fields."
                    ),
                    (
                        "Attach written terms for supplier title, transfer timing, cancellations, "
                        "postponements, replacements, refunds, and permitted package descriptions. "
                        "Match customer remedies with upstream recovery wherever possible, "
                        "and price any remaining mismatch as a real economic and liquidity exposure."
                    ),
                    (
                        "Recheck the audit when entering a new state, changing channels, adding "
                        "lodging or transportation, or sourcing sponsor allocations. Preserve "
                        "the evidence and assigned corrective action for every failed "
                        "control; remove affected inventory until the underlying defect is resolved."
                    ),
                ],
                "fields": [
                    field(
                        "Jurisdiction and reseller-license register",
                        "textarea",
                        (
                            "List the jurisdictions implicated by the operator, event, "
                            "buyer, and channel. Record the applicable reseller "
                            "license, renewal date, bond requirement where applicable, "
                            "and evidence owner, using current statutory sections rather than assuming a nationwide ticket-reseller permission."
                        ),
                        (
                            "A New York transaction receives an Article 25 "
                            "review under N.Y. Arts & Cult. Aff. Law, "
                            "including the licensing provisions in §25.13 and "
                            "any applicable exemption. The register records the "
                            "actual license number, renewal evidence, and responsible operator before affected inventory is offered; another state's license is not substituted for that assessment."
                        ),
                    ),
                    field(
                        "BOTS Act acquisition-method control",
                        "textarea",
                        (
                            "Describe how suppliers and employees acquire tickets, "
                            "which automated activities are allowed, and which "
                            "methods are prohibited. Tie the control to "
                            "15 U.S.C. §45c, including the restriction concerning resale of tickets obtained through covered circumvention when the statutory knowledge standard applies."
                        ),
                        (
                            "The supplier attests that the 20-ticket basket "
                            "was acquired without bypassing ticket-issuer security "
                            "measures, access controls, or posted purchase limits. "
                            "The operator reviews provenance and rejects suspicious "
                            "bulk allocations lacking purchase evidence. SkyBox broadcasting and authorized transfer automation manage lawfully acquired inventory; they are not used to evade queues or issuer restrictions."
                        ),
                    ),
                    field(
                        "All-in price display and fee accuracy",
                        "textarea",
                        (
                            "Record the total mandatory price shown when "
                            "a ticket is first offered, the treatment "
                            "of permitted exclusions, and the final payment "
                            "screen. Apply 16 CFR §§464.2–464.3 and applicable state rules to both headline price prominence and truthful fee descriptions."
                        ),
                        (
                            "A direct ticket offer with a $500 base "
                            "amount and a mandatory $75 service charge "
                            "displays $575 as the prominent total rather "
                            "than introducing the charge late in checkout. "
                            "Any permitted excluded government charge is disclosed before payment. The audit also tests New York transactions against applicable Article 25 pricing requirements, including §25.07."
                        ),
                    ),
                    field(
                        "Supplier rights and provenance addendum",
                        "textarea",
                        (
                            "Draft the operating substance of a supplier "
                            "addendum addressing ownership or authority, lawful "
                            "procurement, transferability, accurate descriptions, remedy obligations, "
                            "and records access. Identify the evidence and recovery mechanism supporting each representation instead of relying on an unsupported promise."
                        ),
                        (
                            "Supplier represents authority to transfer the identified "
                            "admissions, discloses all issuer restrictions, and "
                            "provides purchase records on request. Supplier "
                            "must notify Buyer immediately of cancellation "
                            "or transfer impairment. A failed transfer requires the contractually specified replacement or refund; the operator evaluates collectability and payment security before treating that remedy as a recoverable asset."
                        ),
                    ),
                    field(
                        "Cancellation and postponement allocation",
                        "textarea",
                        (
                            "Separate cancellation, postponement, venue relocation, lineup "
                            "changes, and customer cancellation in the "
                            "contract matrix. Identify customer remedies, supplier "
                            "refund eligibility, beneficiary identity, timing, and any mismatch that requires unrestricted liquidity or a dedicated claims reserve."
                        ),
                        (
                            "The suite agreement distinguishes a canceled event "
                            "from a rescheduled event whose admissions "
                            "remain valid. If the customer contract "
                            "requires a $20,000 refund while the "
                            "venue returns only the $12,000 acquisition amount, the $8,000 mismatch is recorded explicitly. Applicable mandatory remedies and marketplace terms take precedence over an incompatible seller-written clause."
                        ),
                    ),
                    field(
                        "Marketplace replacement and penalty terms",
                        "textarea",
                        (
                            "Extract the actual platform terms governing "
                            "double sales, missed delivery, substitutions, "
                            "replacement procurement, penalties, disputes, and "
                            "setoff. State each calculation basis and distinguish a modeled 200% stress assumption from the enforceable terms of the specific marketplace agreement."
                        ),
                        (
                            "The contract register records whether a failed "
                            "$1,000 order can trigger a $2,000 "
                            "penalty, replacement reimbursement, both charges, "
                            "or another formula. It also records "
                            "the dispute deadline and evidence requirements. The operator does not assume every exchange imposes the same 200% charge or that a supplier indemnity immediately restores available cash."
                        ),
                    ),
                    field(
                        "Hospitality rights and affiliation claims",
                        "textarea",
                        (
                            "Verify permission for every advertised hospitality "
                            "component, including suites, lounges, sponsor "
                            "allocations, transport, and special access. "
                            "Review descriptions for misleading official affiliation under 15 U.S.C. §1125(a), and distinguish independently assembled packages from authorized organizer hospitality products."
                        ),
                        (
                            "A Super Bowl package lists verified admission, "
                            "a contracted dinner, and ground transfer "
                            "without describing the operator as an "
                            "official event partner. World Cup, F1, "
                            "Masters, and Final Four inventory receive separate rights checks. Sponsor provenance alone does not establish permission to resell, use organizer branding, or promise restricted-area access."
                        ),
                    ),
                    field(
                        "Seat-license and contingent-game contract audit",
                        "textarea",
                        (
                            "Record the exact stadium seat-license designation, "
                            "transfer agreement, season or playoff purchase "
                            "obligations, contingent-game treatment, and refund "
                            "ownership. Distinguish an SSL or similar seat-license right from a delivered admission and from a freely transferable option contract."
                        ),
                        (
                            "The NFL inventory file separates the seat "
                            "license from each playoff admission and "
                            "records the obligation to buy eligible "
                            "games. An NBA strip specifies how "
                            "unplayed games generate credits. The operator markets only the rights actually transferable under the issuer agreement and does not promise cash refunds where the agreement provides account credit to another holder."
                        ),
                    ),
                    field(
                        "Customer information and payment controls",
                        "textarea",
                        (
                            "Identify the minimum customer information required "
                            "for delivery, who can access it, "
                            "how payment credentials are handled, and "
                            "which statutory breach duties may apply. Keep payment-provider security requirements distinct from ticket-reseller licensing and restrict exports containing guest identity or transfer details."
                        ),
                        (
                            "The suite roster stores guest name, delivery "
                            "address, and necessary arrival instructions, "
                            "but no full card number. A "
                            "hosted payment provider handles card entry. "
                            "Access is limited to the assigned delivery team. The incident checklist evaluates applicable notification requirements, including N.Y. Gen. Bus. Law §899-aa when relevant, using the actual affected information and jurisdiction."
                        ),
                    ),
                    field(
                        "Audit findings and corrective evidence",
                        "textarea",
                        (
                            "Record each failed control, affected inventory, "
                            "customer impact, responsible operator, target "
                            "date, and evidence required to close "
                            "the finding. Explain when a new jurisdiction, bundle component, contract revision, or channel change requires a fresh review before further sales."
                        ),
                        (
                            "Finding AUD-017 identifies a mandatory $75 "
                            "service charge missing from an initial "
                            "direct-sales display. The affected offer "
                            "is removed, the price configuration "
                            "is corrected, and screenshots document the $575 total before republication. Adding hotel rooms later triggers a separate review of applicable travel-selling requirements rather than reusing the ticket-only audit."
                        ),
                    ),
                ],
                "completion_gate": (
                    "Advance only when jurisdictional requirements are documented, affected "
                    "licenses and rights are verified, pricing displays pass inspection, "
                    "and every unresolved contract or statutory defect has removed the "
                    "affected inventory from active sale."
                ),
            },
            {
                "worksheet_id": "ws-05",
                "number": 5,
                "title": "Automation Pipeline, Acquisition Flywheel & Risk Fallback Tracker",
                "purpose": (
                    "Build a small-team operating system around authorized integrations, "
                    "bounded repricing, reliable inventory locks, and measurable acquisition "
                    "channels. Assign manual fallbacks for synchronization failures, demand "
                    "shocks, supplier defects, and transfer outages so automation improves "
                    "throughput without multiplying unsupported commitments or duplicate sales."
                ),
                "chapter_ref": "Q6, Q10",
                "instructions": [
                    (
                        "Select one authoritative inventory source and verify each vendor's "
                        "actual integration coverage. Document account permissions, supported "
                        "operations, connection health, and export availability. Do not "
                        "assume SkyBox, Automatiq, and Logitix provide interchangeable features or identical marketplace behavior."
                    ),
                    (
                        "Define automation boundaries around lawful acquisition and verified "
                        "rights. Use authorized APIs or supported workflows for "
                        "broadcasting, repricing, transfers, and invoice matching. Keep "
                        "issuer purchase limits and access controls intact even when faster acquisition would improve a modeled spread."
                    ),
                    (
                        "Test repricing against completed-sale evidence, event timing, and "
                        "remaining inventory. Set a contribution floor and maximum "
                        "change per interval. Route injury, postponement, playoff "
                        "elimination, or rights changes to explicit review instead of allowing a stale model to keep trading."
                    ),
                    (
                        "Track lead acquisition through qualified inquiry, funded order, "
                        "successful delivery, and repeat purchase. Calculate acquisition "
                        "cost against contribution rather than package billings. "
                        "Separate corporate-account development from exchange demand, because their selling cycles, service requirements, and settlement patterns differ materially."
                    ),
                    (
                        "Rehearse vendor outage and account-compromise responses with a "
                        "small controlled inventory set. Verify delisting, queue "
                        "recovery, reconciliation, and communication procedures. Restore "
                        "automation only after the authoritative inventory state matches every active channel and outstanding transfer operation."
                    ),
                ],
                "fields": [
                    field(
                        "Authoritative POS and integration inventory",
                        "textarea",
                        (
                            "Name the authoritative inventory platform and "
                            "document the supported connections, account "
                            "owners, credential permissions, sync intervals, "
                            "and vendor limitations. Explain which capabilities are verified in the actual subscription rather than inferred from a product name or marketing description."
                        ),
                        (
                            "The launch pod selects SkyBox as the "
                            "inventory authority and verifies its actual "
                            "connections for the intended channels. "
                            "Automatiq or Logitix services are added "
                            "only for documented functions with clear ownership boundaries. One inventory record governs each admission; two independently editable POS catalogs are prohibited because conflicting availability would increase double-sale exposure."
                        ),
                    ),
                    field(
                        "Credential scope and change accountability",
                        "textarea",
                        (
                            "Record authorized integration identities, minimum "
                            "permissions, credential storage, rotation responsibility, "
                            "and change logging. Distinguish production "
                            "access from testing access and define how a suspected credential leak stops selling or transfer activity without losing the underlying reconciliation evidence."
                        ),
                        (
                            "The listing connector can update authorized "
                            "inventory but cannot alter bank payout "
                            "instructions. Transfer access is separately "
                            "assigned and logged. Credentials remain "
                            "outside exported workbooks and customer messages. A suspected compromise disables the affected connection, preserves operation records, and prompts an independently verified review of payout settings before service is restored."
                        ),
                    ),
                    field(
                        "Dynamic drop-curve repricing policy",
                        "textarea",
                        (
                            "Define the event-time price curve, comparable "
                            "sales inputs, inventory thresholds, fee "
                            "assumptions, minimum contribution, and maximum "
                            "change frequency. Explain how the policy reacts when a mathematically profitable price lacks credible demand or would conflict with an existing customer commitment."
                        ),
                        (
                            "A $500 target seat price can decline "
                            "by at most 3% per six-hour "
                            "interval during the final week, "
                            "subject to current comparable sales. "
                            "With $300 acquisition and 10% seller fees, a $380 sale leaves $42 before other costs. The system flags that thin spread for review instead of assuming every price above acquisition is profitable."
                        ),
                    ),
                    field(
                        "Playoff-probability and contingent-rights model",
                        "textarea",
                        (
                            "Describe the probability inputs for contingent "
                            "games, permitted data sources, update "
                            "cadence, refund mechanics, and stress "
                            "bounds. Separate the value of a possible future admission from cash already committed and from any issuer credit that cannot immediately fund another purchase."
                        ),
                        (
                            "A hypothetical playoff right has a 60% "
                            "chance of producing a transferable "
                            "admission worth $800 gross and "
                            "a 40% chance of a "
                            "$300 issuer credit under its contract. Expected gross value is $600 before fees and costs, but the credit's restrictions and timing are modeled separately rather than treating it as immediate cash."
                        ),
                    ),
                    field(
                        "Demand shock and exception triggers",
                        "textarea",
                        (
                            "Set measurable triggers for injuries, rainouts, "
                            "schedule changes, venue restrictions, abnormal "
                            "price moves, and supplier impairment. "
                            "Identify the affected inventory set, first protective action, decision owner, and evidence required before listings or automated repricing resume."
                        ),
                        (
                            "A confirmed event postponement pauses repricing "
                            "and new purchases for that "
                            "event while the operator checks "
                            "issuer and exchange notices. A "
                            "15% completed-price decline over two observation periods triggers re-underwriting. The pod does not label the event canceled or promise refunds solely because a social post reports a possible schedule change."
                        ),
                    ),
                    field(
                        "Corporate acquisition and repeat-account flywheel",
                        "textarea",
                        (
                            "Define the target corporate buyer, lawful "
                            "contact source, offer, qualification questions, "
                            "sales-cycle stages, and repeat-purchase mechanism. "
                            "Measure acquisition expense against delivered contribution, and specify how outreach avoids implying official event affiliation or advertising unsupported premium access."
                        ),
                        (
                            "The pod targets local corporate event "
                            "planners with a documented 16-seat "
                            "suite offer and clear package "
                            "inclusions. A $900 outreach campaign "
                            "produces three qualified inquiries and one delivered booking with $5,080 modeled contribution. Acquisition expense reduces that booking's contribution to $4,180 if the campaign cost is not already allocated in its operating expense."
                        ),
                    ),
                    field(
                        "Supplier development and inventory-quality loop",
                        "textarea",
                        (
                            "Describe how supplier relationships generate "
                            "repeatable lawful inventory rather than "
                            "one-off speculative allocations. Track rights "
                            "verification, delivery success, pricing accuracy, dispute recoveries, and concentration, and explain which performance result changes purchase limits or removes a supplier from future sourcing."
                        ),
                        (
                            "Supplier A delivers 48 of 50 "
                            "admissions on time, creating a "
                            "96% delivery rate and two "
                            "documented exceptions. The pod reduces "
                            "their open-exposure limit from $9,000 to $4,000 until corrective evidence is reviewed. Another supplier with cleaner provenance does not automatically receive the released capacity; their own rights and concentration checks still apply."
                        ),
                    ),
                    field(
                        "Sync-health indicators and manual fallback",
                        "textarea",
                        (
                            "Define inventory-sync latency, stale listing "
                            "count, unacknowledged holds, conflicting orders, "
                            "and queue age. Specify thresholds "
                            "for manual intervention and the exact recovery sequence, recognizing that cross-exchange availability cannot be made perfectly atomic by a local database lock alone."
                        ),
                        (
                            "The dashboard alerts on any sold "
                            "admission still active elsewhere and "
                            "on hold acknowledgments older than "
                            "five seconds. The operator disables "
                            "affected offers through available channel controls, contacts marketplace support when necessary, and checks for competing fills. Recovery requires matching all channel states to the authoritative record before reopening that inventory."
                        ),
                    ),
                    field(
                        "Automated transfer and invoice exception queue",
                        "textarea",
                        (
                            "Define the exception queue for failed "
                            "recipient validation, issuer transfer locks, "
                            "duplicate requests, unmatched corporate deposits, "
                            "and invoice differences. Assign ownership and response times according to event proximity rather than treating all automation failures as equally urgent."
                        ),
                        (
                            "An admission due for delivery within "
                            "four hours receives a 15-minute "
                            "internal response target; a corporate "
                            "invoice variance due next week "
                            "receives a one-business-day target. A $25,000 deposit with an ambiguous reference remains unmatched until verified against the buyer's remittance advice, rather than being automatically attached to the oldest open package invoice."
                        ),
                    ),
                    field(
                        "Outage drill and restoration evidence",
                        "textarea",
                        (
                            "Record the drill scenario, affected vendor, "
                            "paused operations, fallback owner, communication "
                            "method, inventory reconciliation, and restoration "
                            "criteria. Measure recovery time and unresolved exposure, and distinguish a simulated success from evidence that every production channel supports the same fallback capability."
                        ),
                        (
                            "A controlled drill disconnects the POS "
                            "feed for four test listings "
                            "while operators practice supported manual "
                            "withdrawal and state reconciliation. The "
                            "pod records eight minutes to reconcile all four records and one missing acknowledgment. That unresolved channel remains paused; the drill is not marked complete merely because the local inventory screen shows zero availability."
                        ),
                    ),
                ],
                "completion_gate": (
                    "Advance only when authorized integrations are verified, repricing has "
                    "bounded economics, acquisition costs reach the contribution ledger, "
                    "and outage drills demonstrate documented control of every affected "
                    "listing, transfer, and unmatched payment."
                ),
            },
            {
                "worksheet_id": "ws-06",
                "number": 6,
                "title": "30-Day Launch Sprint, Pod KPI Scorecard & Exit-Readiness Ledger",
                "purpose": (
                    "Turn the first month into a controlled validation sequence rather "
                    "than an inventory accumulation contest. Assign pod responsibilities, "
                    "measure delivered contribution and cash conversion, preserve the "
                    "canonical scorecard assumptions, and build transferable operating "
                    "evidence without promising immediate transactions or an unsupported business valuation."
                ),
                "chapter_ref": "Q11, Q12",
                "instructions": [
                    (
                        "Plan the first 30 days around verified rights, connected workflows, "
                        "tested controls, and qualified demand. Respect the supplied "
                        "one-to-three-month time to first deal. A month without "
                        "a funded transaction can still meet its objectives if the documented launch milestones are complete."
                    ),
                    (
                        "Assign one accountable owner for sourcing, inventory, customer "
                        "delivery, treasury, and incident handling. Use the "
                        "Conservative and Base staffing of one full-time "
                        "operator plus two contractors. Schedule explicit coverage rather than assuming contractors provide continuous availability or unpaid standby."
                    ),
                    (
                        "Track contribution, cash availability, delivery accuracy, synchronization "
                        "failures, and repeat customers alongside gross volume. "
                        "Compare results with the correct scenario denominator. "
                        "Do not annualize one successful tentpole event without accounting for seasonality, capacity limits, supplier concentration, and operating expenses."
                    ),
                    (
                        "Increase purchase limits only when reconciled settlement evidence "
                        "supports the decision. Review channel fees, markdowns, "
                        "claims, and carrying costs before changing the "
                        "model. Preserve the original forecast and document revised assumptions instead of rewriting history to make the launch appear on plan."
                    ),
                    (
                        "Prepare an exit-readiness packet with transferable contracts, "
                        "clean inventory records, cohort economics, staffing "
                        "coverage, and unresolved obligations. Separate owner "
                        "profit from distributions and personal effort. Value the operation from defensible evidence rather than applying a multiple to customer billings or acquisition pass-through."
                    ),
                ],
                "fields": [
                    field(
                        "Days 1–7 rights and treasury foundation",
                        "textarea",
                        (
                            "Specify first-week deliverables for business "
                            "scope, jurisdiction review, supplier diligence, "
                            "bank controls, capital allocation, and "
                            "scenario reconciliation. Assign an accountable person and evidence artifact to each deliverable, including the decision to delay purchasing when rights or liquidity remain unresolved."
                        ),
                        (
                            "By day 7, the owner completes "
                            "the three scenario bridges, allocates "
                            "the $30,000 treasury, screens three "
                            "suppliers, and documents the initial "
                            "jurisdiction checklist. Contractor A verifies sample admission records; Contractor B maps settlement statements. No inventory is purchased merely to show activity when supplier authority or the permitted resale structure remains unresolved."
                        ),
                    ),
                    field(
                        "Days 8–14 systems and rehearsal",
                        "textarea",
                        (
                            "Define second-week milestones for POS "
                            "configuration, channel verification, inventory states, "
                            "pricing tests, transfer recovery, and "
                            "settlement matching. Identify the rehearsal evidence required before exposing real inventory to simultaneous marketplace offers or accepting corporate deposits against supplier commitments."
                        ),
                        (
                            "By day 14, the pod demonstrates "
                            "one duplicate-notification test, one "
                            "ambiguous-transfer recovery, one failed "
                            "hold acknowledgment, and one short-payment "
                            "reconciliation using controlled records. Each result includes an operation identifier and responsible reviewer. Live broadcasting remains disabled for any channel whose listing withdrawal or order-state behavior has not been verified."
                        ),
                    ),
                    field(
                        "Days 15–21 qualified demand and controlled pilot",
                        "textarea",
                        (
                            "Set third-week targets for supplier "
                            "offers, qualified corporate inquiries, "
                            "verified comparable sales, and a "
                            "bounded pilot purchase when justified. Tie every numeric target to evidence quality and available capital rather than rewarding raw messages sent or unverified inventory volume."
                        ),
                        (
                            "The pod seeks five documented supplier "
                            "offers and three qualified corporate "
                            "conversations. If EX-043-001 passes "
                            "rights and liquidity checks, the "
                            "pilot is capped at $6,000 acquisition. If no offer qualifies, the week closes with rejection reasons and revised sourcing criteria; the one-to-three-month first-deal window does not require forcing a purchase."
                        ),
                    ),
                    field(
                        "Days 22–30 close, review, and next commitment",
                        "textarea",
                        (
                            "Define the final-week review for "
                            "executed pilots, unresolved claims, "
                            "open receivables, cash runway, "
                            "supplier quality, and next-month priorities. Distinguish operational delivery from final settlement so an event awaiting payout does not appear fully closed or available to fund another purchase."
                        ),
                        (
                            "At day 30, a delivered pilot "
                            "with $9,000 expected exchange "
                            "settlement remains open in treasury "
                            "until the funds clear. "
                            "The owner reviews actual fees and remaining claim exposure before approving another acquisition. If no event has occurred, the report describes verified launch readiness and open pipeline stages rather than inventing realized profit."
                        ),
                    ),
                    field(
                        "Pod roles, labor budget, and coverage",
                        "textarea",
                        (
                            "Assign sourcing, listing control, delivery, "
                            "treasury, and escalation responsibilities "
                            "across the stated team. "
                            "Document contractor hours and event-day availability, then reconcile paid labor with the scenario bridge while acknowledging the owner's active operating role and concentration of decision authority."
                        ),
                        (
                            "Base staffing uses one full-time owner "
                            "for sourcing and treasury, "
                            "Contractor A for inventory "
                            "and transfer support, and "
                            "Contractor B for corporate coordination and reconciliation. The illustrative $28,000 contractor allocation purchases limited scheduled capacity, not two full-time salaries. Scaled staffing adds one paid full-time operator and a third part-time contractor within its stated expense assumptions."
                        ),
                    ),
                    field(
                        "Canonical pod KPI scorecard",
                        "textarea",
                        (
                            "Record canonical score, ranking, component "
                            "scores, gross volume, retained "
                            "revenue, owner profit, staffing, "
                            "and operating measures. Label scorecard metadata separately from measured performance so a high candidate score cannot substitute for verified delivery quality, cash conversion, or realized margins."
                        ),
                        (
                            "Candidate 43 ranks #02 of 43 "
                            "with 95/100: revenue 24, "
                            "margin 25, team efficiency "
                            "20, startup accessibility 13, "
                            "and automation 13. The Base target remains $1,010,000 gross, $404,000 retained, and $191,900 owner profit. Weekly operating measures include on-time delivery, conflicting fills, unacknowledged holds, unrestricted cash, and settlement variance, each reported from actual records."
                        ),
                    ),
                    field(
                        "Contribution cohort and repeat-buyer economics",
                        "textarea",
                        (
                            "Track delivered contribution by operating "
                            "lane, buyer cohort, acquisition "
                            "source, and event season. "
                            "Separate first-order acquisition expense from repeat-service costs, and describe how refunds, late claims, and repeated supplier failures revise cohort profitability after the original sales month."
                        ),
                        (
                            "A corporate cohort delivers two suite "
                            "bookings with $5,080 modeled "
                            "contribution each before a "
                            "separately tracked $900 acquisition "
                            "campaign, leaving $9,260 if that cost was not previously allocated. A later $600 unrecovered claim reduces cohort contribution to $8,660. Gross suite billings of $40,000 are reported separately and never labeled cohort profit."
                        ),
                    ),
                    field(
                        "Capital scaling and stop-purchase triggers",
                        "textarea",
                        (
                            "Define the evidence required to "
                            "increase inventory exposure, add "
                            "another tentpole event, or "
                            "expand staffing. Specify purchase stops for cash shortages, unresolved settlement differences, rights defects, and repeated delivery failures, with explicit restart conditions based on reconciled records."
                        ),
                        (
                            "The initial event acquisition ceiling stays "
                            "at $6,000 until three "
                            "completed events have clean "
                            "settlement matches and no "
                            "unresolved rights defects. Any unrestricted-cash forecast below $6,000 stops new purchases. A $2,000 unexplained exchange shortfall also stops expansion until classified and resolved; booked gross sales alone cannot release either restriction."
                        ),
                    ),
                    field(
                        "Exit-readiness and transferable operating evidence",
                        "textarea",
                        (
                            "List the records a successor "
                            "operator would need to "
                            "reproduce results: assignable contracts, "
                            "rights evidence, supplier concentration, customer cohorts, operating procedures, staff coverage, claims, and settlement history. Identify relationships or platform accounts that require separate consent rather than assuming they transfer automatically."
                        ),
                        (
                            "The exit packet contains 12 months "
                            "of matched event ledgers, "
                            "supplier contracts with assignment "
                            "terms, documented channel-account restrictions, "
                            "customer cohort contribution, and outstanding claim schedules. Personal supplier relationships and owner-only account permissions are marked as transition dependencies. A purchaser receives access only through authorized arrangements, not through shared credentials or an assumption that every marketplace account can be sold."
                        ),
                    ),
                    field(
                        "Owner-profit quality and final operating decision",
                        "textarea",
                        (
                            "Reconcile reported owner profit to "
                            "cash generation, recurring workload, "
                            "replacement staffing, concentration, and "
                            "remaining liabilities. Record whether the next cycle should repeat, expand, or pause, and support that decision with evidence rather than a valuation based on gross package billings."
                        ),
                        (
                            "Base owner profit is $191,900 before "
                            "personal income taxes under "
                            "the supplied model, not "
                            "$1,010,000 of distributable revenue. "
                            "If replacing the owner's operating work would cost an illustrative $80,000 annually, a buyer's adjusted earnings analysis starts at $111,900 before further adjustments. The pod repeats its current scale until cash conversion and coverage justify expansion."
                        ),
                    ),
                ],
                "completion_gate": (
                    "Complete the launch workbook only when all 30-day milestones have "
                    "evidence or explicit unresolved status, the staffing and cash plan "
                    "reconcile to the selected canonical scenario, and the next-cycle "
                    "decision accounts for settlement exposure, owner workload, and transferable operating rights."
                ),
            },
        ],
    }
