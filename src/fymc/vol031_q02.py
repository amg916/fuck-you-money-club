from __future__ import annotations

CHAPTER_2 = {
    "id": "Q2",
    "chapter_id": "Q2",
    "chapter_number": 2,
    "question_number": 2,
    "slug": "who-pays-fleet-arbitrage-payment-rails",
    "question_prompt": "Who writes the check in uber & commercial fleet arbitrage, what acute financial or statutory pain forces them to pay, and how do funds clear cleanly without circumvention or non-payment?",
    "kicker": "Q2 / THE BIG MONEY PLAYBOOKS",
    "title": "Who Pays, Why They Pay & How the Payment Rail Works",
    "subtitle": "Driver Lease Waterfalls, TLC/TCP Black SUV Dispatch, Investor Co-Hosting, ACH Mandates, and Airport Transfer Settlement",
    "layout_template": "executive_summary",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #31, Uber & Commercial Fleet Arbitrage, ranks #15 of 36 "
        "with an 89/100 Money-to-Manpower Score. Its buyers pay for usable "
        "vehicles, dependable airport capacity, and accountable investor fleet "
        "administration, not abstract access to an app. This chapter maps 10 "
        "operator plays to the person controlling payment, the service evidence "
        "supporting collection, and the fallback when a driver, vehicle, or "
        "payment rail fails. Formula v2.0 annual owner profit is $25,200 "
        "Conservative, $144,900 Base, and $336,000 Scaled. Those results use "
        "$180,000, $690,000, and $1,200,000 gross operator billings, respectively, "
        "with 55% retained contribution after owner splits and pass-through "
        "fleet costs. Separate passenger fares, refundable deposits, investor "
        "principal, and operator fees before designing any settlement waterfall."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$180,000",
            "context": "Annual gross operator billings; $99,000 retained at 55%",
            "note": "14% gross-basis net margin; 25.45% retained-basis net margin; $25,200 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Base",
            "value": "$690,000",
            "context": "Annual gross operator billings; $379,500 retained at 55%",
            "note": "21.0% gross-basis net margin; 38.18% retained-basis net margin; $144,900 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Scaled",
            "value": "$1,200,000",
            "context": "Annual gross operator billings; $660,000 retained at 55%",
            "note": "28% gross-basis net margin; 50.91% retained-basis net margin; $336,000 annual owner net profit; 2 FT + 4 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Identify the economic buyer before offering the vehicle",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "The first check usually comes from a working driver who needs "
                    "an eligible, insured vehicle before the next earning window. "
                    "Their acute pain is lost earning capacity, not vehicle ownership "
                    "as an aspiration. A $450 weekly lease becomes intelligible when "
                    "compared with that driver's documented receipts, fuel, tolls, "
                    "tax provision, and living withdrawals; it does not become "
                    "affordable merely because a salesperson cites busy airport "
                    "queues. Verify recent platform statements supplied through an "
                    "authorized process and separate recurring earnings from temporary "
                    "incentives. Ask who actually owns the payment account and who "
                    "can authorize its debits. A spouse's card, an unrelated "
                    "business account, and a driver's own account create different "
                    "authorization risks. The agreement should identify the vehicle, "
                    "permitted use, weekly billing period, included mileage, damage "
                    "process, and return procedure. A refundable security deposit "
                    "remains a liability until a valid contractual application "
                    "occurs. Keep it outside operating revenue and track it by "
                    "driver. If verified disposable operating cash cannot support "
                    "the recurring charge, reduce the commitment or decline the "
                    "placement rather than turning a collection problem into a "
                    "remote vehicle-control problem."
                ),
                (
                    "The second buyer is an enterprise travel manager, executive "
                    "assistant, hotel transportation desk, or corporate procurement "
                    "team purchasing reliable arrival capacity. The person arranging "
                    "a ride may not control the budget. Establish the contracting "
                    "entity, purchase-order requirement, spending limit, invoice "
                    "recipient, and accounts-payable calendar before dispatch. A "
                    "travel coordinator values an arriving passenger more than a "
                    "beautiful utilization chart; procurement values a supplier "
                    "whose invoice matches an authorized reservation. Price waiting "
                    "time, parking, flight disruption, cancellations, and substitution "
                    "explicitly. For example, twelve independently booked airport "
                    "transfers at $150 produce $1,800 of customer billings, not "
                    "$1,800 of owner profit. Driver compensation, vehicle expense, "
                    "insurance, and any subcontractor settlement still require "
                    "funding. Local authority is a service requirement rather than "
                    "a transferable marketing label: California TCP authority, New "
                    "York City TLC licensing, and airport access permissions address "
                    "different jurisdictions and activities. Corporate clients pay "
                    "to avoid failed pickups and purchasing from an ineligible "
                    "operator. They do not purchase immunity from airport rules. "
                    "When a permit, vehicle qualification, or driver credential "
                    "fails verification, stop assigning that resource and offer "
                    "a separately verified licensed and insured substitute."
                ),
                (
                    "The third buyer is the vehicle investor, whose pain is "
                    "unmonitored downtime, unexplained deductions, and declining "
                    "asset value. Their management agreement authorizes specific "
                    "services and distributions; possession of their vehicle does "
                    "not authorize unrestricted withdrawals from their bank account. "
                    "Specify who approves maintenance, who funds collision "
                    "deductibles, how reserve balances are held, and when statements "
                    "become payable. An investor may accept a $300 monthly management "
                    "fee for documented placement, maintenance coordination, and "
                    "reconciliation, but will challenge an unexplained percentage "
                    "of vaguely defined proceeds. Use a distribution statement that "
                    "opens with collected receipts, lists contractually permitted "
                    "deductions, and ends with the owner's payable balance. The ten "
                    "mapped plays below are chapter-level operating applications "
                    "across the supplied lease, dispatch, and co-hosting edges; "
                    "only the first carries the supplied canonical play identifier. "
                    "Their prices illustrate contracts, not market quotations or "
                    "additional scorecard revenue. Several applications serve the "
                    "same vehicle and must not be counted twice. A toll recovery, "
                    "for example, can settle a receivable without creating fee "
                    "income. Treat each application as a distinct buyer obligation "
                    "with a measurable service, an authorized payment source, and "
                    "a workable fallback."
                ),
            ],
            "table": {
                "caption": "Ten Mapped Operating Plays: Buyer Authority, Unit Economics, and Failure Response",
                "headers": [
                    "Mapped operating play and service boundary",
                    "Payer and specific spending authority",
                    "Illustrative unit math and accounting boundary",
                    "Risk fallback and operational response",
                ],
                "rows": [
                    [
                        "commercial_tlc_tcp_plate_shift_dispatch: commercially registered Black SUV dispatch under locally applicable authority",
                        "Corporate travel buyer authorizes independent bookings; platform settles eligible platform trips",
                        "Two staffed ten-hour shifts yield $700 illustrative daily fares; operator fee basis remains separate",
                        "Remove affected resources; fulfill through independently verified licensed and insured backup operators",
                    ],
                    [
                        "Weekly driver vehicle leasing with documented eligible commercial use",
                        "Named driver authorizes recurring payments from their verified payment account",
                        "Four collected weeks at $450 produce $1,800 gross lease billings",
                        "Pause renewal after failed collection; arrange documented safe voluntary return",
                    ],
                    [
                        "Investor vehicle co-hosting with itemized monthly administration and reporting",
                        "Vehicle owner signs management authority and approves permitted fee deductions",
                        "Six vehicles at $300 monthly produce $1,800 management fee billings",
                        "Suspend new placements when investor maintenance funding or authority lapses",
                    ],
                    [
                        "Dedicated corporate airport transfer blocks sold through independent procurement",
                        "Travel budget holder issues purchase order covering twelve authorized reservations",
                        "Twelve completed transfers at $150 produce $1,800 gross customer billings",
                        "Use verified backup capacity; refund undelivered service under contract terms",
                    ],
                    [
                        "Hotel concierge transfer dispatch through a documented commercial booking agreement",
                        "Hotel purchasing officer authorizes hotel-paid transfers or disclosed guest checkout",
                        "Twenty completed dispatches at $25 produce $500 coordination fee billings",
                        "Require direct authorized checkout when hotel credit exposure exceeds limit",
                    ],
                    [
                        "Black SUV shift scheduling and separately priced fleet dispatch administration",
                        "Fleet principal authorizes schedule administration under signed management service terms",
                        "Forty completed shift assignments at $12 produce $480 administration billings",
                        "Remove unqualified drivers and recalculate charges for unfilled shift assignments",
                    ],
                    [
                        "Eligible replacement vehicle leasing during documented repair-related fleet downtime",
                        "Driver or fleet customer authorizes replacement rental and permitted use",
                        "Five paid replacement days at $85 produce $425 gross billings",
                        "Refund unused days when qualified replacement inventory cannot be delivered",
                    ],
                    [
                        "Toll reconciliation with separately disclosed permitted administration charges",
                        "Driver agreement authorizes actual toll recovery and lawful disclosed fees",
                        "Recover $100 toll cost plus $10 fee; evaluate only fee as revenue",
                        "Reverse duplicate tolls and suspend disputed administration charges pending evidence",
                    ],
                    [
                        "Maintenance coordination for investor-owned vehicles using approved repair budgets",
                        "Investor approves repair estimate and separately contracted coordination service charge",
                        "Four approved service events at $40 produce $160 coordination billings",
                        "Stop vehicle dispatch for safety defects; obtain repair funding separately",
                    ],
                    [
                        "Reserved enterprise transportation capacity funded by a defined service retainer",
                        "Corporate treasury funds retainer against procurement-approved capacity and service terms",
                        "A $2,000 advance offsets ten $200 bookings; never count both twice",
                        "Reconcile unused funds and apply documented cancellation or refund provisions",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Collect against evidence the payer already understands",
                "body": "Align the invoice with the buyer's operating records rather than forcing them to interpret a fleet ledger.",
                "items": [
                    "For driver leases, pair the vehicle identifier and exact lease week with the signed delivery record; do not bury old toll charges inside the next recurring debit.",
                    "For corporate transfers, place the purchase-order number, passenger reference, flight number, and completed pickup timestamp on the same invoice line.",
                    "For investor distributions, show opening reserve, receipts, authorized deductions, additions, and closing reserve before showing the amount payable.",
                    "Test any Uber Fleet Partner payout arrangement with a small live reconciliation before relying on it; feature availability does not establish contractual deduction rights.",
                ],
            },
        },
        {
            "heading": "2. Match the settlement mechanism to the obligation",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Payment rail selection starts with the obligation, not the "
                    "processor's logo. A weekly driver lease benefits from scheduled "
                    "collection and clear authorization; a large investor funding "
                    "transfer benefits from verified bank instructions; a disputed "
                    "asset handover may justify independent escrow. ACH settlement "
                    "does not eliminate returns, and card capture does not eliminate "
                    "chargebacks. Keep separate ledger states for invoiced, initiated, "
                    "processor-settled, bank-reconciled, disputed, and refunded "
                    "transactions. Never release owner distributions merely because "
                    "an online dashboard shows an incoming payment. Establish "
                    "reserve timing from the processor agreement, payment type, "
                    "observed return experience, and promised distribution schedule. "
                    "For recurring debits from consumer accounts, Regulation E "
                    "requires appropriately authenticated authorization and a copy "
                    "to the consumer; variable amounts can trigger advance-notice "
                    "requirements. Business accounts and network rules require "
                    "their own analysis rather than copying consumer language. "
                    "A processor such as Stripe or an ACH provider can transport "
                    "an authorized instruction but cannot manufacture consent or "
                    "validate the underlying lease. Use hosted payment collection "
                    "where available, keep card credentials out of dispatch notes, "
                    "and never ask drivers for platform passwords to make "
                    "collection more convenient."
                ),
                (
                    "A fleet waterfall is a contractual allocation implemented "
                    "through whatever supported payout configuration actually exists. "
                    "Do not sell automatic top-of-waterfall deductions before "
                    "confirming the fleet account's country, product, agreements, "
                    "permissions, and available statement exports. Where a supported "
                    "arrangement permits collection of the operator's charge, "
                    "reconcile the driver's entitlement and every deduction "
                    "explicitly. Where it does not, invoice the driver through "
                    "a separate authorized rail. Platform passenger funds are not "
                    "a general-purpose treasury account for corporate bookings, "
                    "damage assessments, or unrelated investor distributions. "
                    "Likewise, an independently sourced airport transfer belongs "
                    "in its own booking and settlement workflow; never solicit "
                    "a platform passenger to cancel a trip and pay privately. "
                    "Contractual retainers and milestone holds describe when "
                    "money becomes payable, while ACH, wire, and card checkout "
                    "describe how it moves. Escrow describes independent custody "
                    "and release conditions. Factoring changes ownership or "
                    "financing of receivables. Keeping these categories distinct "
                    "prevents a dangerous sales claim that a retainer is "
                    "inherently protected or that a wire-funded invoice is "
                    "immune to fraud. The comparison matrix treats all eight "
                    "requested mechanisms as settlement choices without "
                    "pretending they are technically identical."
                ),
                (
                    "Corporate accounts often demand payment terms longer than "
                    "drivers and backup carriers can finance. If a $10,000 "
                    "approved invoice is factored at an illustrative 3% fee, "
                    "the total proceeds before other charges are $9,700, "
                    "potentially delivered through an initial advance and later "
                    "reserve release. Confirm recourse, dilution, assignment "
                    "restrictions, customer notification, and collection control "
                    "before accepting that liquidity. A disputed pickup can "
                    "remain the fleet's exposure under a recourse agreement. "
                    "Retainers solve a different problem: a $2,000 advance "
                    "funds reserved service but ordinarily remains deferred "
                    "until the contracted performance occurs. Milestone releases "
                    "can fit a multi-day event, with documented daily "
                    "completion controlling each installment. Statutory disbursement "
                    "is not an ordinary fleet revenue channel; it means a "
                    "payment governed by a specific court process or legal "
                    "entitlement, such as a properly established claim "
                    "distribution. Record the actual authority and recipient "
                    "rather than inventing a statutory priority for your lease "
                    "fee. For high-value wires, independently call a previously "
                    "verified contact before changing beneficiary details. A "
                    "convincing email thread is not proof that the investor "
                    "or corporate treasury approved a replacement bank account."
                ),
            ],
            "table": {
                "caption": "Eight Payment and Settlement Mechanisms Compared for Fleet Operations",
                "headers": [
                    "Mechanism and appropriate fleet use",
                    "Authority and evidence required before collection",
                    "Clearing characteristics and principal exposure",
                    "Fee protection and failure response",
                ],
                "rows": [
                    [
                        "Wire transfer for verified investor funding or large corporate settlements",
                        "Authorized treasury contact confirms beneficiary through an independently verified channel",
                        "Bank acceptance does not cure fraud; recall requests offer uncertain recovery",
                        "Match bank credit to invoice and investigate changed instructions before release",
                    ],
                    [
                        "Independent escrow for specifically negotiated asset delivery or disputed handover",
                        "All parties sign release conditions with an appropriately authorized escrow provider",
                        "Provider controls release timing; contested conditions can immobilize operating liquidity",
                        "Define evidence, deadlines, fees, dispute handling, and return of unused funds",
                    ],
                    [
                        "ACH debit for recurring driver leases with valid account authorization",
                        "Account holder authorizes debit terms; retain authentication and required consumer copy",
                        "Settlement remains exposed to applicable returns and unauthorized-payment disputes",
                        "Reconcile returns daily and suspend new exposure rather than repeated blind debits",
                    ],
                    [
                        "Service retainer for reserved enterprise airport capacity and planned bookings",
                        "Budget holder signs service scope, advance amount, application, and refund terms",
                        "Underlying transfer uses another rail; advance normally precedes earned service revenue",
                        "Track unearned balance separately and invoice completed services without duplicate recognition",
                    ],
                    [
                        "Statutory disbursement for an established legally governed claim or distribution",
                        "Obtain actual governing authority, recipient entitlement, and administrator payment instructions",
                        "Timing follows the governing process; ordinary lease charges receive no invented priority",
                        "Exclude speculative proceeds from dispatch cash planning and maintain claim documentation",
                    ],
                    [
                        "Platform checkout for eligible platform trips or processor-hosted independent bookings",
                        "Use each platform's permitted account, transaction type, and customer authorization",
                        "Payout delays, reserves, disputes, and account restrictions can interrupt liquidity",
                        "Keep independent bookings separate and never divert platform-originated trips off platform",
                    ],
                    [
                        "Receivables factoring for accepted corporate invoices with clear assignment rights",
                        "Authorized company officer executes agreement and supplies genuine service acceptance evidence",
                        "Advance differs from final proceeds; recourse and reserve deductions preserve exposure",
                        "Model every financing charge and stop funding invoices with unresolved service disputes",
                    ],
                    [
                        "Milestone holds for multi-day transportation programs with objective completion evidence",
                        "Procurement contract defines milestones, acceptance period, withheld amounts, and release authority",
                        "Money moves through another rail; buyer-controlled holds can extend collection timing",
                        "Use daily manifests and defined objection deadlines to narrow disputed balances",
                    ],
                ],
            },
        },
        {
            "heading": "3. Protect the fee without seizing money or disabling mobility",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Credit screening should predict whether the specific payer "
                    "can satisfy the specific obligation. For a driver, verify "
                    "identity, permitted driving credentials, authorized vehicle "
                    "use, recent earnings, existing lease burdens, and ability "
                    "to fund the first billing period. Obtain motor vehicle "
                    "records through an authorized provider such as SambaSafety "
                    "or another appropriate screening service, with the required "
                    "permissible purpose and authorizations. If a consumer report "
                    "drives a denial or less favorable terms, evaluate applicable "
                    "Fair Credit Reporting Act notice duties rather than "
                    "treating the vendor's score as an unexplained veto. For "
                    "an enterprise, verify legal entity, signer authority, "
                    "procurement enrollment, trade references, disputed invoice "
                    "history, and payment calendar. A genuine company domain "
                    "does not establish that an assistant can bind its "
                    "treasury. For an investor, verify ownership, financing "
                    "restrictions, insurance responsibilities, reserve funding, "
                    "and authority to place the vehicle in commercial service. "
                    "Record a credit limit, review date, and named exception "
                    "owner. Limit exposure using delivered but unpaid service, "
                    "not merely overdue invoices; a customer can exhaust "
                    "credit before the first invoice reaches its due date."
                ),
                (
                    "Fee protection begins with measurable performance and narrow "
                    "deduction rights. Define when a lease week starts, when "
                    "a transfer counts as completed, which party bears a "
                    "no-show, and how disputed tolls or damage are reviewed. "
                    "A fleet cannot establish a damage charge simply by "
                    "calling it an administrative fee. Pair delivery and "
                    "return photographs with inspection timestamps, odometer "
                    "readings, repair estimates, and the contract's allocation "
                    "of responsibility. Keep routine lease collection separate "
                    "from contested assessments where the agreement or law "
                    "requires it. For corporate work, obtain reservation "
                    "acceptance before dispatch and preserve pickup evidence "
                    "without spreading passenger information across uncontrolled "
                    "spreadsheets. UCC Article 9 can matter when receivables "
                    "or other collateral secure an obligation, but a contract "
                    "sentence alone does not establish attachment, perfection, "
                    "or priority; determine the applicable state enactment "
                    "and collateral rules. Avoid assuming a lien exists on "
                    "platform proceeds merely because your company supplied "
                    "the car. If a bankruptcy filing becomes known, escalate "
                    "collection and possession decisions immediately because "
                    "the automatic stay may restrict otherwise available "
                    "remedies. Operational speed cannot repair an invalid "
                    "collection right after money has moved."
                ),
                (
                    "Telematics should reduce uncertainty, not convert a billing "
                    "dispute into a safety incident. Use an authorized OBD-II "
                    "or hardwired system to document mileage, service intervals, "
                    "and permitted location information under a disclosed "
                    "data policy. A starter-interrupt device is not a "
                    "substitute for collection controls. Any contemplated "
                    "intervention requires a lawful contractual basis, "
                    "applicable notices, reliable confirmation that the "
                    "vehicle is parked and unoccupied, and a safe recovery "
                    "procedure; never interrupt propulsion or immobilize "
                    "an occupied or moving vehicle. When payment fails, "
                    "first distinguish bank error, authorization dispute, "
                    "temporary liquidity shortfall, and outright refusal. "
                    "Send an itemized statement, offer a documented cure "
                    "path, stop extending new exposure when permitted, "
                    "and arrange a safe return or qualified recovery "
                    "process. Do not repeatedly debit a revoked mandate "
                    "or hold a driver's unrelated earnings hostage. "
                    "For corporate buyers, preserve undisputed collection "
                    "while investigating a disputed booking. For investors, "
                    "withhold only amounts supported by the management "
                    "agreement and governing rules. The durable deterrent "
                    "to circumvention is reliable dispatch, transparent "
                    "accounting, and enforceable service terms, not "
                    "credential sharing, intimidation, or hidden deductions."
                ),
            ],
            "table": {
                "caption": "Counterparty Credit and Fee Evidence Matrix",
                "headers": [
                    "Counterparty exposure requiring a decision",
                    "Evidence that establishes authority or capacity",
                    "Concrete operating limit or fee protection",
                    "Response when verification or collection fails",
                ],
                "rows": [
                    [
                        "Driver entering a recurring weekly vehicle lease obligation",
                        "Verified identity, eligible credentials, authorized earnings statements, and account mandate",
                        "Collect first agreed period before handover and define maximum unpaid exposure",
                        "Decline placement or shorten commitment when documented affordability remains inadequate",
                    ],
                    [
                        "Corporate travel coordinator requesting transportation on deferred payment terms",
                        "Procurement confirmation, purchase order, authorized signer, and accounts-payable contact details",
                        "Cap delivered unpaid bookings and require replenishment before additional exposure",
                        "Move new independent bookings to authorized prepaid checkout when credit is exhausted",
                    ],
                    [
                        "Investor placing an encumbered vehicle into commercial fleet service",
                        "Ownership documents, permitted commercial use, insurance evidence, and signed management authority",
                        "Fund agreed maintenance reserve and prohibit deductions beyond enumerated contract rights",
                        "Pause placement until ownership authority and essential operating funding are verified",
                    ],
                    [
                        "Backup carrier accepting an airport transfer on short notice",
                        "Current operating authority, coverage confirmation, driver eligibility, and written booking acceptance",
                        "Match customer promise to subcontracted scope and establish documented settlement timing",
                        "Select another verified carrier when credentials or service acceptance cannot be confirmed",
                    ],
                    [
                        "Driver facing an added collision deductible or damage assessment",
                        "Before-and-after inspections, loss evidence, policy terms, and responsibility determination",
                        "Separate disputed assessments from ordinary billing and apply only supported obligations",
                        "Preserve evidence, investigate allocation, and reverse charges unsupported by the record",
                    ],
                    [
                        "Payer requesting replacement bank details during an active settlement cycle",
                        "Independent callback to established contact and documented authorized beneficiary change",
                        "Hold the changed payment instruction while preserving the underlying payable balance",
                        "Escalate suspected impersonation and retain original verified instructions until resolved",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four checks before dispatch or vehicle release",
                "body": "A completed payment instruction cannot compensate for an unauthorized payer, ineligible vehicle, or unsupported deduction.",
                "items": [
                    "Verify the contracting entity, actual signer authority, account-holder authorization, payment amount, and first collection status before accepting recurring exposure.",
                    "Confirm the specific vehicle, driver, operating authority, airport permission, and coverage for every planned use; TLC and TCP credentials are not interchangeable.",
                    "Confirm the written waterfall, reserve ownership, fee basis, and available platform functionality before promising automatic deductions or investor distributions.",
                    "Confirm the backup carrier, incident contact, safe return procedure, and dispute workflow before any occupied trip or driver handover.",
                ],
            },
        },
        {
            "heading": "4. Reconcile the shift economics to retained contribution and cash",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Model commercial_tlc_tcp_plate_shift_dispatch at the vehicle "
                    "level before aggregating the business. Two separately staffed "
                    "ten-hour shifts provide twenty scheduled vehicle hours, "
                    "not permission for one driver to work twenty hours. "
                    "Assume each shift completes four eligible trips averaging "
                    "$87.50 in customer fares: eight trips produce $700 "
                    "daily fare volume. Assume $140 of applicable platform "
                    "or booking charges, $280 of driver compensation, and "
                    "$180 of vehicle, fuel, insurance, and maintenance "
                    "allocations; the illustrative operating remainder is "
                    "$100. These assumptions are a dispatch sensitivity "
                    "test, not the chapter's annual forecast. If your "
                    "contract earns only a $70 dispatch fee while "
                    "another principal sells transportation, record the "
                    "$70 fee basis rather than claiming all $700 "
                    "as operator revenue. Do not add that fee to "
                    "the $100 remainder without establishing whose costs "
                    "and receipts each number represents. Four lost "
                    "trips remove $350 of fares while many costs "
                    "persist. Underwrite normal demand, lawful operating "
                    "hours, airport queue delays, and maintenance downtime "
                    "without guaranteed surge pricing. When coverage or "
                    "authority fails, remove the affected vehicle or "
                    "driver and fulfill accepted work through independently "
                    "verified licensed and insured backup operators."
                ),
                (
                    "The annual scorecard uses a different, expressly defined "
                    "boundary: gross operator lease, dispatch, and co-hosting "
                    "billings multiplied by a 55% retained share. Conservative "
                    "billings of $180,000 leave $99,000 after $81,000 "
                    "of owner splits and pass-through fleet costs. "
                    "Subtracting $73,800 of remaining modeled costs "
                    "produces $25,200 owner net profit. Base billings "
                    "of $690,000 leave $379,500 after $310,500 "
                    "of those deductions; $234,600 of remaining costs "
                    "leaves $144,900. Scaled billings of $1,200,000 "
                    "leave $660,000 after $540,000 of deductions; "
                    "$324,000 of remaining costs leaves $336,000. "
                    "The corresponding gross-basis net margins are "
                    "14%, 21.0%, and 28%; retained-basis margins "
                    "are 25.45%, 38.18%, and 50.91%, rounded "
                    "to two decimals. Remaining costs are residual "
                    "totals required by the supplied model, not "
                    "an invented vendor budget. Do not force "
                    "them into the separate $2,500–$15,000 monthly "
                    "opex planning range or subtract that range "
                    "again. The supplied ASC 606 retained-share "
                    "convention supports this comparison; actual gross "
                    "versus net presentation still depends on the "
                    "principal-agent assessment of each performance "
                    "obligation. Neither passenger fare volume nor "
                    "vehicle purchase funding becomes fee revenue "
                    "simply because it crosses an account you administer."
                ),
                (
                    "Cash control requires a daily bridge from completed "
                    "service to collected funds and a weekly bridge "
                    "from collected funds to distributable balances. "
                    "For every receipt, retain payer, contract, service "
                    "period, vehicle or booking reference, gross "
                    "amount, deductions, processor identifier, and bank "
                    "match. QuickBooks or another suitable ledger "
                    "can track receivables and liabilities, while "
                    "exported platform statements and processor "
                    "reports establish the external evidence. A "
                    "settlement file is not reconciled until its "
                    "net deposit and fees agree with the bank "
                    "and the individual allocations agree with "
                    "the contracts. Keep refundable deposits, unearned "
                    "retainers, owner payables, and claims reserves "
                    "visible rather than sweeping them into "
                    "available operating cash. Conservative and Base "
                    "staffing remain one full-time operator plus "
                    "three contractors; Scaled remains two full-time "
                    "staff plus four contractors. Design exception "
                    "queues around that capacity: failed payments, "
                    "unmatched tolls, expiring coverage, disputed "
                    "damage, and overdue corporate invoices need "
                    "named owners and aging. Automation should "
                    "close matched items and expose exceptions, "
                    "not silently assign contested charges. Before "
                    "distribution, rerun the waterfall using collected "
                    "amounts, preserve required reserves, and "
                    "deliver a statement that lets the driver "
                    "or investor reproduce the calculation independently."
                ),
            ],
            "table": {
                "caption": "Formula v2.0 Annual Reconciliation and Cash Classification",
                "headers": [
                    "Scenario or ledger classification",
                    "Gross billings and retained-share bridge",
                    "Remaining costs and exact owner profit",
                    "Margin basis and staffing interpretation",
                ],
                "rows": [
                    [
                        "Conservative annual case using the supplied Formula v2.0 financial boundary",
                        "$180,000 gross less $81,000 owner splits and pass-through costs equals $99,000 retained",
                        "$99,000 retained less $73,800 remaining modeled costs equals $25,200 owner profit",
                        "14% gross-basis margin; 25.45% retained-basis margin; one full-time operator plus three contractors",
                    ],
                    [
                        "Base annual case using the supplied Formula v2.0 financial boundary",
                        "$690,000 gross less $310,500 owner splits and pass-through costs equals $379,500 retained",
                        "$379,500 retained less $234,600 remaining modeled costs equals $144,900 owner profit",
                        "21.0% gross-basis margin; 38.18% retained-basis margin; one full-time operator plus three contractors",
                    ],
                    [
                        "Scaled annual case using the supplied Formula v2.0 financial boundary",
                        "$1,200,000 gross less $540,000 owner splits and pass-through costs equals $660,000 retained",
                        "$660,000 retained less $324,000 remaining modeled costs equals $336,000 owner profit",
                        "28% gross-basis margin; 50.91% retained-basis margin; two full-time staff plus four contractors",
                    ],
                    [
                        "Custodial and advance balances excluded from earned operating fee totals",
                        "Refundable deposits, unearned retainers, and owner funding require separate balance tracking",
                        "Release or recognize only upon the applicable contractual and accounting event",
                        "Bank balance exceeds spendable cash whenever customers or owners retain valid claims",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Establish payer authority and contract boundaries",
                    "action": "Record the signer, account holder, approved service, fee basis, and maximum exposure.",
                    "detail": "Attach procurement authority or driver authorization, signed terms, vehicle eligibility, and the applicable operating permissions before dispatch or handover.",
                },
                {
                    "step": 2,
                    "title": "Collect through the permitted settlement mechanism",
                    "action": "Issue an itemized invoice or authorized payment instruction linked to the service record.",
                    "detail": "Use supported platform functions only for permitted transactions; separate independent corporate bookings, retainers, refundable deposits, and contested assessments.",
                },
                {
                    "step": 3,
                    "title": "Match performance, processor settlement, and bank movement",
                    "action": "Reconcile booking or lease evidence to the external settlement report and bank entry.",
                    "detail": "Assign failed debits, chargebacks, unmatched tolls, and disputed service to named owners; preserve original evidence and avoid duplicate recovery.",
                },
                {
                    "step": 4,
                    "title": "Apply the waterfall and publish reproducible statements",
                    "action": "Calculate permitted deductions, required reserves, earned fees, and owner or driver payables.",
                    "detail": "Distribute only supported balances under the agreed timing; report gross operator billings, 55% modeled retained contribution, and owner profit as separate measures.",
                },
            ],
        },
    ],
    "pull_quote": "The defensible fee is the one an authorized payer can trace from a completed service to a reconciled bank entry.",
    "diagram_id": "diag-04",
    "action_checklist": [
        "Create separate payer profiles for drivers, corporate buyers, investors, and backup carriers, with signer authority and verified settlement contacts.",
        "Map all ten operating applications to their actual contract and revenue boundary, eliminating duplicate lease, dispatch, retainer, and pass-through recognition.",
        "Test supported fleet payout functionality and one independent collection cycle before promising automatic waterfall deductions.",
        "Verify vehicle, driver, coverage, local livery authority, and airport access for both ten-hour shifts; document a separately verified backup carrier.",
        "Build daily payment exception queues and separate ledgers for refundable deposits, unearned retainers, investor reserves, and owner payables.",
        "Reproduce the $25,200, $144,900, and $336,000 annual owner-profit cases from gross billings, 55% retained contribution, and the exact remaining modeled costs.",
    ],
    "statutory_citations": [
        {
            "title": "12 CFR § 1005.10 — Preauthorized transfers",
            "url": "https://www.ecfr.gov/current/title-12/chapter-X/part-1005/section-1005.10",
            "relevance": "Controls authorization, consumer copies, stop-payment rights, and applicable notices for preauthorized electronic transfers involving covered consumer accounts.",
        },
        {
            "title": "California Public Utilities Code § 5371 — Charter-party carrier authority",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=5371.&lawCode=PUC",
            "relevance": "Establishes the certificate-or-permit requirement for covered charter-party passenger carrier operations; verify the actual authority applicable to the planned service.",
        },
        {
            "title": "California Public Utilities Code § 5433 — Transportation network company insurance",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=5433.&lawCode=PUC",
            "relevance": "Sets coverage requirements across specified transportation network company activity periods; independently contracted livery and app-off operations require their own coverage analysis.",
        },
        {
            "title": "15 U.S.C. § 1681b — Permissible purposes of consumer reports",
            "url": "https://www.law.cornell.edu/uscode/text/15/1681b",
            "relevance": "Requires a valid permissible purpose for obtaining consumer reports; determine the applicable basis before purchasing driver credit or screening reports.",
        },
        {
            "title": "15 U.S.C. § 1681m — Requirements on users of consumer reports",
            "url": "https://www.law.cornell.edu/uscode/text/15/1681m",
            "relevance": "Provides adverse-action notice requirements when covered decisions rely on consumer reports, including identifying the reporting source and relevant consumer rights.",
        },
        {
            "title": "11 U.S.C. § 362 — Automatic stay",
            "url": "https://www.law.cornell.edu/uscode/text/11/362",
            "relevance": "May restrict collection, possession, lien enforcement, and other actions after a bankruptcy filing; escalate affected fleet recovery and deduction decisions before acting.",
        },
    ],
}
