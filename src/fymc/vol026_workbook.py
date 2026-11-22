from __future__ import annotations


def build_volume_026_workbook() -> dict:
    def field(name: str, input_type: str, prompt: str, example: str) -> dict:
        return {"name": name, "type": input_type, "prompt": prompt, "example": example}

    return {
        "workbook_id": "wb-026-government-surplus-auctions",
        "volume_id": "vol-026-government-surplus-auctions",
        "title": "Government Surplus Auctions — Operator Companion Workbook",
        "subtitle": (
            "6 Printable Operator Worksheets for GSA and Municipal Lot Underwriting, "
            "Bid Ceilings, Removal Logistics, SF-97 and DEMIL Review, B2B Remarketing, "
            "and Small-Team Capital Discipline"
        ),
        "worksheets": [
            {
                "worksheet_id": "ws-01",
                "number": 1,
                "title": "Opportunity, Lot Underwriting and Counterparty Qualification",
                "purpose": (
                    "Select surplus categories where inspection access, removal capacity, "
                    "transfer documents, and reachable business buyers support a defensible "
                    "resale thesis. Separate the auction platform from the actual seller, "
                    "qualify every critical counterparty, and reject attractive headline "
                    "prices that conceal custody, restriction, or liquidation problems."
                ),
                "chapter_ref": "Q1, Q2, Q6",
                "instructions": [
                    (
                        "Choose one starting asset category and one service radius. Compare "
                        "GSA Auctions, GovPlanet, GovDeals, and Public Surplus listings without "
                        "assuming identical seller authority, buyer eligibility, premiums, "
                        "inspection rights, or pickup support across platforms."
                    ),
                    (
                        "Preserve the complete listing, amendments, photographs, lot identifier, "
                        "seller contact, and sale conditions before estimating value. Contact "
                        "the listed custodian through a verified channel to resolve missing "
                        "serial numbers, access limits, or conflicting descriptions."
                    ),
                    (
                        "Obtain recent completed-sale evidence and at least three direct buyer "
                        "conversations. Distinguish achieved prices from asking prices, and "
                        "subtract delivery, testing, warranty, and sales-channel differences "
                        "before treating another seller's transaction as a usable comparable."
                    ),
                    (
                        "Inspect the assets personally or appoint a documented local inspector. "
                        "Describe the exact tests permitted, record every untested subsystem, "
                        "and price the uncertainty instead of treating silence in an auction "
                        "description as evidence of working condition."
                    ),
                    (
                        "Decide whether to pursue, inspect further, or reject the lot using "
                        "written criteria. A low acquisition price does not offset missing "
                        "transfer evidence, prohibited end use, unavailable loading equipment, "
                        "or a removal schedule the operating team cannot meet."
                    ),
                ],
                "fields": [
                    field(
                        "Category thesis and operating boundary",
                        "textarea",
                        (
                            "Define the first resale category, typical buyer, geographic radius, "
                            "maximum lot size, and exclusions. Explain why this narrow operating "
                            "boundary gives the team a measurable inspection or distribution advantage."
                        ),
                        (
                            "Start with commercial steel tool cabinets within 150 road miles "
                            "of Sacramento. Target independent repair shops buying two to four "
                            "units. Limit the first purchase to ten cabinets and exclude powered "
                            "lifts, compressed-gas equipment, weapons, and assets requiring "
                            "unresolved vehicle-title or controlled-item determinations."
                        ),
                    ),
                    field(
                        "Listing identity and actual selling party",
                        "textarea",
                        (
                            "Record the platform, lot identifier, legal seller, custodian, "
                            "physical location, and source of sale authority. Explain how the "
                            "team verified that payment and removal instructions belong to this transaction."
                        ),
                        (
                            "Internal opportunity GA-026-001 covers ten municipal tool cabinets "
                            "listed through GovDeals by a city fleet department. The analyst "
                            "matches the listing contact to the city's published directory, "
                            "confirms the yard address by telephone, and saves the listing "
                            "and seller-specific conditions in the deal folder."
                        ),
                    ),
                    field(
                        "Auction eligibility and account readiness",
                        "textarea",
                        (
                            "Identify account registration, deposit, identity, entity, residency, "
                            "or end-use requirements stated for this sale. Separate ordinary "
                            "account activation from lot-specific eligibility and document who checked each requirement."
                        ),
                        (
                            "The purchasing LLC uses its own approved buyer account and "
                            "documented bank account. The analyst confirms no special end-user "
                            "qualification is stated for these cabinets. A second reviewer "
                            "checks the current lot terms before bidding; a GovPlanet account "
                            "alone would not establish eligibility for restricted property."
                        ),
                    ),
                    field(
                        "Completed-sale comparable set",
                        "textarea",
                        (
                            "List achieved prices for closely matched assets with dates, "
                            "condition, quantity, and delivery terms. State every adjustment "
                            "used to convert those observations into a conservative resale estimate for this lot."
                        ),
                        (
                            "Three completed local transactions support $1,850, $2,050, and "
                            "$2,200 per cabinet. The highest included delivery worth $200 "
                            "per unit. After adjusting for missing keys and mixed cosmetics, "
                            "the model uses $2,000 each, producing $20,000 gross resale "
                            "proceeds for ten cabinets before customer sales tax."
                        ),
                    ),
                    field(
                        "Buyer demand and reachable purchasing authority",
                        "textarea",
                        (
                            "Describe specific potential buyers, their intended use, quantity, "
                            "budget, decision-maker role, and purchase timing. Distinguish "
                            "documented interest from signed orders, deposits, and merely encouraging conversations before assigning demand confidence."
                        ),
                        (
                            "Shop A requests a quote for four cabinets at $2,000 each, "
                            "Shop B can use three within thirty days, and Shop C will "
                            "inspect two after cleaning. These nine units represent interest, "
                            "not booked revenue. No buyer commitment enters the cash forecast "
                            "until its payment terms are documented."
                        ),
                    ),
                    field(
                        "Inspection evidence and untested conditions",
                        "textarea",
                        (
                            "Record inspection date, inspector, sample coverage, permitted "
                            "tests, defects, and inaccessible components. Explain how photographs, "
                            "serial records, measurements, and test limitations support the purchase decision without overstating verified operating condition."
                        ),
                        (
                            "The inspector checks all ten cabinet frames, opens every accessible "
                            "drawer, and records dimensions and serial plates. Two locks need "
                            "replacement and one drawer binds. No powered equipment is included. "
                            "The report allocates $1,000 to planned refurbishment and separately "
                            "earmarks $600 for defects discovered after collection."
                        ),
                    ),
                    field(
                        "Removal feasibility and loading responsibility",
                        "textarea",
                        (
                            "Translate the listing's collection conditions into equipment, "
                            "labor, appointment, insurance, and transport requirements. Name "
                            "the party responsible for loading and identify the latest safe collection date before contractual removal expires."
                        ),
                        (
                            "The hypothetical sale requires collection within ten calendar days "
                            "after award and provides no loading assistance. A carrier quotes "
                            "$1,200 transport and a local operator quotes $300 unloading. "
                            "Pickup is booked for day six, leaving four days for disruption; "
                            "forklift capacity and cabinet dimensions are confirmed before bidding."
                        ),
                    ),
                    field(
                        "Transfer evidence and restricted-property screen",
                        "textarea",
                        (
                            "Identify the documents needed to establish a transferable interest "
                            "and any restrictions on use, resale, export, or destruction. "
                            "Explain why the selected asset category does or does not require vehicle-specific documentation."
                        ),
                        (
                            "Cabinets require the paid invoice, lot description, release "
                            "authorization, and matching custody record; SF-97 is irrelevant "
                            "to this nonvehicle lot. For a later federal vehicle, the team "
                            "would confirm promised SF-97 availability and state title requirements. "
                            "Any DEMIL condition receives a separate written disposition review."
                        ),
                    ),
                    field(
                        "Counterparty qualification and fraud controls",
                        "textarea",
                        (
                            "Evaluate the seller contact, inspector, carrier, refurbisher, "
                            "and likely buyer using evidence appropriate to each role. "
                            "Record payment-channel verification, insurance scope, service capacity, references, and conflicts that could distort recommendations."
                        ),
                        (
                            "The carrier supplies its legal entity name, current cargo coverage, "
                            "and equipment description. The operator checks applicable FMCSA "
                            "records and confirms the yard appointment directly. A changed "
                            "wire instruction is paused until independently verified using "
                            "the previously validated seller telephone number, never the number "
                            "inside the change request."
                        ),
                    ),
                    field(
                        "Pursuit decision and rejection triggers",
                        "textarea",
                        (
                            "Write a concise investment decision identifying the evidence "
                            "supporting pursuit, the remaining conditions, and nonnegotiable "
                            "rejection triggers. Assign an accountable reviewer and expiration time so stale assumptions cannot authorize a later bid."
                        ),
                        (
                            "Pursue only after the inspector's report, carrier reservation, "
                            "and seller release terms are saved. Reject if loading becomes "
                            "buyer-provided without available equipment, serial counts differ, "
                            "or the bid exceeds $9,700. The operations lead signs the "
                            "decision twenty-four hours before close and rechecks any listing amendment."
                        ),
                    ),
                ],
                "completion_gate": (
                    "The purchasing lead and operations lead confirm verified seller identity, "
                    "documented buyer evidence, complete inspection limits, an executable removal "
                    "plan, and a written bid ceiling. Unresolved transfer or item restrictions "
                    "keep the lot out of the bidding queue."
                ),
            },
            {
                "worksheet_id": "ws-02",
                "number": 2,
                "title": "Unit Economics, Defect Reserve and Working-Capital Float",
                "purpose": (
                    "Convert an auction opportunity into a cash-backed bid ceiling using "
                    "gross resale proceeds, buyer premiums, transport, refurbishment, defect "
                    "exposure, and allocated operating costs. Reconcile illustrative lot "
                    "returns with the three canonical annual scenarios while keeping "
                    "inventory investment, tax collections, and recognized revenue distinct."
                ),
                "chapter_ref": "Q3, Q4",
                "instructions": [
                    (
                        "Model expected resale proceeds from units actually expected to sell "
                        "and exclude customer sales tax from revenue. List the hammer price, "
                        "premium, purchase tax treatment, logistics, repair work, channel "
                        "fees, and operating-cost allocation as separate inputs."
                    ),
                    (
                        "Build a defect allowance from inspection findings and explicitly "
                        "untested components. Show planned repairs separately from uncertain "
                        "failures, then describe how unused cash reserves differ from actual "
                        "expenses and from any accounting valuation adjustment."
                    ),
                    (
                        "Calculate the maximum bid algebraically from the target contribution "
                        "after all modeled costs. Apply premium and purchase-tax formulas "
                        "to the correct base, round downward to a valid bidding increment, "
                        "and prohibit unsupported last-minute ceiling increases."
                    ),
                    (
                        "Map every cash payment and buyer receipt onto a dated timeline. "
                        "Include deposits, payment deadlines, refurbishment, recurring costs, "
                        "and a late-sale case so the team can see peak funding demand "
                        "rather than relying on projected accounting profit."
                    ),
                    (
                        "Reconcile annual proceeds, total costs, margin, owner net profit, "
                        "and staffing to the supplied scorecard. Treat an attractive individual "
                        "lot as an underwriting example, not evidence that the whole "
                        "portfolio automatically earns the same margin."
                    ),
                ],
                "fields": [
                    field(
                        "Canonical annual scenario reconciliation",
                        "textarea",
                        (
                            "Copy the three annual scenarios exactly and derive each total "
                            "cost budget. State the revenue basis, staffing, and distinction "
                            "between owner net profit and acquisition capital committed to unsold inventory."
                        ),
                        (
                            "Conservative: $150,000 proceeds less $138,000 costs equals $12,000 "
                            "owner net at 8%, with 2 FT + 3 C. Base: $575,000 less "
                            "$494,500 equals $80,500 at 14%, with 2 FT + 3 C. "
                            "Scaled: $1,000,000 less $800,000 equals $200,000 at 20%, "
                            "with 3 FT + 4 C, seven people."
                        ),
                    ),
                    field(
                        "Resale proceeds and channel assumptions",
                        "textarea",
                        (
                            "Calculate expected gross resale proceeds by unit count and "
                            "realistic achieved price. Identify delivery charges, returns, "
                            "discounts, channel fees, and tax collections so each item receives consistent treatment throughout the model."
                        ),
                        (
                            "Ten cabinets at $2,000 each produce $20,000 gross resale "
                            "proceeds, excluding sales tax. Buyers collect from the warehouse, "
                            "so no delivery revenue is modeled. Selling costs are $800, "
                            "or 4% of proceeds. If the operator collects customer tax, "
                            "that cash enters a tax liability account rather than sales."
                        ),
                    ),
                    field(
                        "Acquisition cost and purchase-tax treatment",
                        "textarea",
                        (
                            "Enter hammer price, buyer premium, taxable purchase base, "
                            "applicable purchase tax, and auction charges. Support any resale "
                            "exemption with accepted documentation instead of assuming every government seller or platform handles taxes identically."
                        ),
                        (
                            "The example uses a $9,000 hammer price and a hypothetical "
                            "10% premium, producing $9,900 acquisition cost. Purchase tax is "
                            "$0 only because the seller accepts the valid resale documentation "
                            "for this transaction. If acceptance changes, the analyst recalculates "
                            "the bid ceiling before submitting a bid."
                        ),
                    ),
                    field(
                        "Transport, refurbishment and full lot cost",
                        "textarea",
                        (
                            "Build the complete modeled cost bridge from acquisition to "
                            "collected resale proceeds. Separate variable services, storage, "
                            "defect allowance, sales expenses, and allocated recurring overhead, and explain where contractor charges are already included."
                        ),
                        (
                            "Costs are $9,000 purchase, $900 premium, $1,200 transport, "
                            "$300 unloading, $1,000 refurbishment, $600 defect allowance, "
                            "$400 incremental storage, $800 selling, and $1,000 overhead "
                            "allocation. Total modeled cost is $15,200; $20,000 proceeds "
                            "less $15,200 yields $4,800, or 24%. Contractor work "
                            "is included in the quoted service lines."
                        ),
                    ),
                    field(
                        "Defect reserve and downside sensitivity",
                        "textarea",
                        (
                            "Document the defect allowance, loss drivers, adverse resale "
                            "price, and additional repair exposure. Distinguish cash earmarked "
                            "for uncertainty from a booked expense, and calculate both a stressed profit and a loss case."
                        ),
                        (
                            "Earmark $600 for uncertain defects; record actual spending under "
                            "the accounting policy rather than expensing the earmark automatically. "
                            "At $17,000 proceeds and $800 additional repairs beyond the "
                            "original model, total cost becomes $16,000 and profit $1,000, "
                            "a 5.88% margin. At $15,000 proceeds, the same cost creates "
                            "a $1,000 loss."
                        ),
                    ),
                    field(
                        "Maximum bid and premium formula",
                        "textarea",
                        (
                            "Solve for the hammer-price ceiling using target margin, "
                            "nonacquisition costs, premium rate, and applicable tax mechanics. "
                            "Show the arithmetic and the permitted bidding increment, then record the enforceable rounded ceiling."
                        ),
                        (
                            "A 20% target margin permits $16,000 total cost on $20,000 "
                            "proceeds. Nonacquisition costs equal $5,300. With a 10% premium "
                            "and accepted purchase-tax exemption, maximum hammer price is "
                            "($16,000 - $5,300) / 1.10 = $9,727.27. Round down "
                            "to $9,700 when valid increments are $100; never round upward."
                        ),
                    ),
                    field(
                        "Peak cash exposure and collection timeline",
                        "textarea",
                        (
                            "List dated outflows, expected collections, unrestricted cash, "
                            "and minimum operating liquidity. Show whether expense allocations "
                            "represent new payments and include earmarked reserves when assessing how much cash remains available for another purchase."
                        ),
                        (
                            "Pay $9,900 on day two, $1,500 logistics on day six, "
                            "$1,000 repairs by day twelve, and $400 storage before sale. "
                            "Earmark another $600 for defects and $1,000 for the lot's "
                            "overhead share: funding capacity required is $14,400. The $800 "
                            "selling cost is paid from collected proceeds, assuming the "
                            "channel does not require advance payment."
                        ),
                    ),
                    field(
                        "Startup capital and recurring cost envelope",
                        "textarea",
                        (
                            "Allocate starting cash among inventory, services, reserves, "
                            "facilities, and operating liquidity. Compare the plan with "
                            "the canonical capital and monthly cost ranges, and distinguish annual budget allocations from cash already committed at launch."
                        ),
                        (
                            "Use $75,000 within the $15,000-$80,000 startup range: "
                            "$30,000 acquisition capacity, $8,000 logistics, $6,000 repairs, "
                            "$6,000 defects, $10,000 facilities and tools, and $15,000 "
                            "operating liquidity. Recurring costs of $10,000 monthly fit "
                            "the $3,000-$15,000 range. The operating reserve covers only "
                            "1.5 months, so early commitments must remain deliberately limited."
                        ),
                    ),
                    field(
                        "Base-case annual cost bridge",
                        "textarea",
                        (
                            "Allocate the Base scenario's exact total cost across a "
                            "credible annual operating plan. Explain differences between "
                            "the portfolio and sample lot, and prevent recurring payroll, facility costs, and contractor services from being counted twice."
                        ),
                        (
                            "Base costs total $494,500: purchases $300,000, premiums "
                            "$30,000, transport $18,000, repairs $12,000, defect costs "
                            "$6,000, selling $8,500, and recurring overhead $120,000. "
                            "The overhead includes employee compensation and base facility "
                            "costs; contractors sit in service lines. Direct B2B sales "
                            "reduce annual selling costs below the example lot's 4% assumption."
                        ),
                    ),
                    field(
                        "Inventory turn and capital-release decision",
                        "textarea",
                        (
                            "Define inventory cost, carrying period, recovery alternatives, "
                            "and cash-release triggers. Calculate throughput using cost "
                            "rather than resale proceeds, and explain how slow-moving goods can remain profitable on paper while preventing the next purchase."
                        ),
                        (
                            "The cabinet lot has $13,400 of modeled presale cost and "
                            "defect capacity before selling fees and overhead. With $40,200 "
                            "dedicated to comparable presale commitments, only three such "
                            "lots fit simultaneously. Review unsold units on day thirty, "
                            "reprice on day forty-five, and seek a documented wholesale "
                            "exit on day sixty."
                        ),
                    ),
                ],
                "completion_gate": (
                    "The reviewer reproduces the $15,200 lot cost, $4,800 modeled profit, "
                    "$9,700 rounded ceiling, and all three annual scenario totals. Cash "
                    "availability covers payment, removal, reserve commitments, and recurring "
                    "costs without relying on unsigned buyer interest."
                ),
            },
            {
                "worksheet_id": "ws-03",
                "number": 3,
                "title": "Execution, Inventory Ledger and Technical QA Pre-Flight",
                "purpose": (
                    "Create a traceable operating chain from auction award through payment, "
                    "release, transport, inspection, repair, listing, and collected resale. "
                    "Use asset-level records and reconciled cash entries to prevent missed "
                    "removal deadlines, duplicate inventory, unsupported condition claims, "
                    "and premature recognition of proceeds from uncompleted transactions."
                ),
                "chapter_ref": "Q7, Q8",
                "instructions": [
                    (
                        "Assign one owner to every handoff and record the required evidence "
                        "before the next step begins. Match award documents, invoices, "
                        "payment confirmation, release instructions, and physical asset identifiers "
                        "rather than relying on an auction account's status alone."
                    ),
                    (
                        "Create the asset ledger before collection and confirm quantities "
                        "during loading. Photograph distinguishing marks and damage, record "
                        "custody changes, and keep the transport receipt separate from any "
                        "claim that mechanical or electrical condition has been verified."
                    ),
                    (
                        "Use a category-specific inspection checklist at receiving. Quarantine "
                        "unsafe or restricted items, document repair decisions and parts, "
                        "and require retesting before changing an asset's condition classification "
                        "or publishing a statement that it is ready for service."
                    ),
                    (
                        "Reconcile the inventory subledger, expense records, payment records, "
                        "and buyer invoices weekly. Preserve a clear distinction between "
                        "cash outflow, inventory cost, cost of goods sold, reserve planning, "
                        "sales tax liabilities, and earned resale proceeds."
                    ),
                    (
                        "Close each lot with collected funds, delivery or pickup evidence, "
                        "resolved exceptions, and a realized margin review. Compare the "
                        "actual result with the original bid model and update future "
                        "assumptions without overwriting the original underwriting record."
                    ),
                ],
                "fields": [
                    field(
                        "Award package and source-of-truth record",
                        "textarea",
                        (
                            "Identify the authoritative documents for the purchase and "
                            "their storage location. Record lot identity, final price, "
                            "amendments, seller terms, and the person responsible for resolving discrepancies before payment or collection instructions are executed."
                        ),
                        (
                            "Deal GA-026-001 contains the saved listing, final award notice, "
                            "$9,900 seller invoice, accepted resale documentation, and "
                            "removal conditions. The analyst names files with the deal "
                            "identifier and capture date. A mismatch between the invoice "
                            "quantity and ten listed cabinets is resolved with the seller "
                            "before the payment is released."
                        ),
                    ),
                    field(
                        "Payment verification and release authorization",
                        "textarea",
                        (
                            "Document payment deadline, approved payment channel, confirmation "
                            "reference, release recipient, and seller acknowledgment. Explain "
                            "how the team detects changed bank details and prevents a carrier from arriving without an effective release document."
                        ),
                        (
                            "The operator pays $9,900 through the platform's verified "
                            "channel on day two and saves the receipt. The seller "
                            "confirms cleared payment and authorizes the named carrier "
                            "for day-six pickup. The dispatcher supplies the release "
                            "reference and driver identification requirements, then confirms "
                            "the yard has the same appointment."
                        ),
                    ),
                    field(
                        "Removal schedule and contingency dispatch",
                        "textarea",
                        (
                            "Set the contractual removal deadline, scheduled appointment, "
                            "loading resources, travel buffer, and fallback carrier. Record "
                            "the escalation owner and the evidence needed for any seller-approved extension rather than assuming extensions are routinely available."
                        ),
                        (
                            "The contract permits ten calendar days; primary collection "
                            "is day six. The dispatcher reconfirms on day four and "
                            "holds a day-eight backup carrier quote. If the primary "
                            "truck fails, operations activates the backup immediately. "
                            "Any extension must be written by the authorized seller; "
                            "a voicemail request does not change the deadline."
                        ),
                    ),
                    field(
                        "Asset identity and custody manifest",
                        "textarea",
                        (
                            "Specify the identifiers, quantities, photographs, and signatures "
                            "captured at each custody transfer. Explain how items lacking "
                            "serial plates receive internal identifiers without falsely representing those identifiers as manufacturer or government asset numbers."
                        ),
                        (
                            "Assign CAB-001 through CAB-010 as internal inventory IDs. "
                            "Record manufacturer serials where present and photograph each "
                            "cabinet's front, back, drawers, and damage. The driver and "
                            "yard custodian confirm ten loaded units; receiving confirms "
                            "the same ten IDs. Missing serial plates are described "
                            "explicitly, not replaced with invented manufacturer numbers."
                        ),
                    ),
                    field(
                        "Receiving inspection and safe-use hold",
                        "textarea",
                        (
                            "Define receiving tests, acceptance criteria, inspection owner, "
                            "and the process for holding unsafe equipment. Keep transport "
                            "damage, preexisting defects, and untested functions separate so repair priorities and possible claims remain supportable."
                        ),
                        (
                            "Receiving checks cabinet stability, drawer retention, sharp "
                            "edges, locks, and caster attachment. CAB-004 remains off "
                            "the sales floor because its drawer stop is missing. "
                            "The technician labels the condition, photographs the defect, "
                            "and logs the repair estimate. A dent already visible "
                            "in auction photographs is not presented as carrier damage."
                        ),
                    ),
                    field(
                        "Refurbishment work order and retest",
                        "textarea",
                        (
                            "Record authorized repair scope, labor, parts, spending limit, "
                            "and completion tests. Explain who may approve additional "
                            "work and how the original defect description remains visible after the asset passes its final inspection."
                        ),
                        (
                            "Work order WO-026-01 authorizes $1,000 across ten cabinets "
                            "for cleaning, two locks, drawer alignment, and minor hardware. "
                            "Additional spending above $100 per unit requires operations "
                            "review against recovery value. CAB-004 returns to saleable "
                            "status only after the replacement stop is installed and "
                            "the technician documents a successful drawer-retention test."
                        ),
                    ),
                    field(
                        "Inventory cost and accounting classification",
                        "textarea",
                        (
                            "Define the bookkeeping treatment for acquisition, freight, "
                            "repairs, storage, selling costs, and overhead under the "
                            "operator's accounting policy. Explain how the planning reserve is tracked without automatically creating an unsupported expense or duplicate cost."
                        ),
                        (
                            "The bookkeeper records the $9,900 purchase and allocates "
                            "qualifying direct acquisition costs across ten asset IDs "
                            "under the adopted policy. Selling costs and recurring "
                            "overhead remain separately identifiable. The $600 defect "
                            "earmark stays in the cash-planning register until actual "
                            "costs or a supportable valuation adjustment require accounting entries."
                        ),
                    ),
                    field(
                        "Listing evidence and condition claims",
                        "textarea",
                        (
                            "Specify the photographs, measurements, test results, included "
                            "accessories, and excluded services needed before publication. "
                            "Require each condition statement to link to evidence and explain how an unresolved defect changes the listing and expected price."
                        ),
                        (
                            "CAB-004's listing states dimensions, drawer count, installed "
                            "replacement stop, cosmetic dents, and buyer pickup terms. "
                            "It includes current photographs and the completed inspection "
                            "record. The listing does not claim factory refurbishment, "
                            "load capacity beyond documented evidence, or manufacturer "
                            "warranty coverage. Any included key is counted and photographed."
                        ),
                    ),
                    field(
                        "Buyer invoice, collection and revenue event",
                        "textarea",
                        (
                            "Record buyer identity, price, tax treatment, payment terms, "
                            "delivery obligation, and the event used for revenue "
                            "recognition under the accounting policy. Explain how customer deposits and overdue invoices appear separately from completed cash sales."
                        ),
                        (
                            "Shop A buys four cabinets for $8,000 before applicable "
                            "sales tax and pays before pickup. The team records "
                            "any early payment as a customer deposit until the "
                            "contractual transfer event under its accounting policy. "
                            "The signed pickup receipt identifies all four assets, "
                            "and the invoice separates collected tax from resale proceeds."
                        ),
                    ),
                    field(
                        "Lot closeout and actual-versus-model review",
                        "textarea",
                        (
                            "Reconcile final units sold, collected proceeds, remaining "
                            "inventory, actual costs, reserve use, and recognized margin. "
                            "Identify each variance from underwriting and assign a specific correction to future bidding, inspection, pricing, or logistics assumptions."
                        ),
                        (
                            "All ten cabinets sell for $20,000. Actual defects cost "
                            "$400 instead of the modeled $600, while every other "
                            "modeled cost holds. Comparable fully allocated cost becomes "
                            "$15,000 and profit $5,000, or 25%. The closeout releases "
                            "$200 of unused reserve capacity and preserves the original "
                            "$4,800 underwriting result for comparison."
                        ),
                    ),
                ],
                "completion_gate": (
                    "Every acquired asset has a complete custody trail, inspection status, "
                    "cost record, and disposition. Award, payment, release, inventory, "
                    "buyer receipts, and bank records reconcile, and no unresolved safety "
                    "hold is represented as a sale-ready item."
                ),
            },
            {
                "worksheet_id": "ws-04",
                "number": 4,
                "title": "Statutory, Licensing, Contract and Outreach Audit",
                "purpose": (
                    "Identify the actual rules attached to the seller, asset, location, "
                    "transport movement, resale channel, and destination. Translate federal "
                    "surplus procedures, state resale requirements, vehicle documents, "
                    "restricted-property conditions, and outreach duties into specific "
                    "evidence requirements without treating every auction as the same transaction."
                ),
                "chapter_ref": "Q5, Q9",
                "instructions": [
                    (
                        "Classify the seller and sale program before selecting governing "
                        "rules. Federal personal-property sales, municipal disposals, and "
                        "private marketplace transactions can follow different authorities; "
                        "the platform's brand does not determine the legal status of every lot."
                    ),
                    (
                        "Read the complete sale contract and preserve applicable amendments. "
                        "Extract inspection limits, payment deadlines, removal obligations, "
                        "default remedies, transfer documents, taxes, and restricted uses "
                        "into a checklist with an accountable reviewer for each material obligation."
                    ),
                    (
                        "Check state and local requirements where the business operates "
                        "and where goods will be delivered. Match permits, resale "
                        "certificates, vehicle-dealer rules, and tax collection duties "
                        "to the actual activity rather than copying another state's checklist."
                    ),
                    (
                        "Escalate vehicles, controlled items, hazardous materials, data-bearing "
                        "devices, and export transactions to the appropriate specialist "
                        "before commitment. Document a lawful disposition route and "
                        "required evidence instead of assuming a low purchase price resolves restrictions."
                    ),
                    (
                        "Review buyer outreach and resale representations alongside the "
                        "physical transaction. Maintain accurate sender identity, suppression "
                        "records, substantiated condition claims, and clear delivery terms; "
                        "retain the evidence supporting every regulated or contract-sensitive decision."
                    ),
                ],
                "fields": [
                    field(
                        "Seller authority and governing sale framework",
                        "textarea",
                        (
                            "Identify the seller's authority and the applicable sale "
                            "framework with concrete citations where relevant. Explain "
                            "which rules govern this transaction and why unrelated federal procurement clauses should not be imported automatically."
                        ),
                        (
                            "For a federal personal-property sale, review 40 U.S.C. "
                            "545 and 41 CFR Part 102-38 together with the actual "
                            "sale terms. For the municipal cabinet lot, record the "
                            "city's disposal authority and seller conditions instead. "
                            "FAR clauses from government purchasing contracts do not "
                            "automatically govern every government surplus sale."
                        ),
                    ),
                    field(
                        "Business registration and resale-tax evidence",
                        "textarea",
                        (
                            "Record the operating entity, seller permit, resale "
                            "documentation, collection duties, and jurisdiction-specific "
                            "source. Explain how the operator verifies acceptance by the auction seller and prevents a resale exemption from covering business-use purchases."
                        ),
                        (
                            "A California reseller checks Revenue and Taxation Code "
                            "6066 for permit requirements and 6091 for the presumption "
                            "that gross receipts are taxable unless the contrary "
                            "is established. The team supplies valid resale evidence "
                            "for inventory cabinets, but separately evaluates a cabinet "
                            "retained for its own warehouse rather than resold."
                        ),
                    ),
                    field(
                        "Sale contract, inspection limits and remedies",
                        "textarea",
                        (
                            "Extract the exact contractual allocation of condition risk, "
                            "inspection rights, payment timing, removal duties, and "
                            "available remedies. Explain how the operator preserves evidence and avoids assuming ordinary retail return rights apply to auction purchases."
                        ),
                        (
                            "The example contract sells the cabinets as-is, requires "
                            "payment within its stated period, and requires removal "
                            "within ten calendar days. The file records any description-error "
                            "procedure separately from ordinary defects. Under applicable "
                            "state enactments, review UCC 2-316 for warranty exclusions "
                            "and UCC 2-328 for auction-specific sale mechanics."
                        ),
                    ),
                    field(
                        "Federal vehicle SF-97 and state title route",
                        "textarea",
                        (
                            "For vehicle opportunities, identify the seller-promised "
                            "ownership evidence, VIN match, state application requirements, "
                            "and resale restrictions. Explain the distinction between a federal transfer certificate and a state-issued title before valuing a vehicle as road-ready inventory."
                        ),
                        (
                            "A later GSA vehicle opportunity proceeds only after the "
                            "seller confirms the documents it will provide. SF-97, "
                            "when provided, supports an application for a state title; "
                            "it is not itself that title. The operator checks the "
                            "VIN, destination DMV requirements, and any dealer-license "
                            "obligation before pricing the vehicle for retail resale."
                        ),
                    ),
                    field(
                        "DEMIL conditions and controlled-item disposition",
                        "textarea",
                        (
                            "Record any DEMIL code, end-use condition, mutilation "
                            "requirement, controlled-item designation, and required "
                            "certificate. Explain who interprets the applicable sale instructions and how completion evidence is retained before any resale or alternate disposition."
                        ),
                        (
                            "If a GovPlanet listing carries a DEMIL condition, the "
                            "team obtains the exact lot instructions and supporting "
                            "classification rather than relying on a generic code "
                            "summary. Where applicable, review DoD Manual 4160.28 "
                            "and the contract's required process. No restricted item "
                            "is advertised for intact resale while its permitted "
                            "disposition remains unresolved."
                        ),
                    ),
                    field(
                        "Export classification and destination controls",
                        "textarea",
                        (
                            "Identify whether export activity is contemplated and "
                            "document jurisdiction, classification, destination, end "
                            "user, and authorization requirements. Explain why an auction release or DEMIL determination does not independently establish permission to export the property."
                        ),
                        (
                            "The cabinet pilot remains domestic, with no export "
                            "service offered. For later equipment exports, screen "
                            "EAR scope under 15 CFR 734.3, restrictions under "
                            "15 CFR 736.2, and the Commerce Control List in "
                            "Part 774, Supplement No. 1. Potential defense articles "
                            "require separate review under 22 CFR 121.1 and 123.1."
                        ),
                    ),
                    field(
                        "Transport authority, securement and insurance",
                        "textarea",
                        (
                            "Identify the shipment's vehicle class, route, cargo "
                            "characteristics, carrier role, and applicable transport "
                            "requirements. Record insurance verification and securement responsibilities without treating a certificate of insurance as proof that every loss is covered."
                        ),
                        (
                            "Operations checks whether the planned interstate movement "
                            "falls under applicable FMCSA requirements and verifies "
                            "the carrier's current status. Securement is evaluated "
                            "against applicable 49 CFR Part 393, including 393.100. "
                            "The ten cabinets are restrained against movement, loading "
                            "responsibility is explicit, and cargo coverage exclusions "
                            "are reviewed before dispatch."
                        ),
                    ),
                    field(
                        "Environmental handling and embedded data",
                        "textarea",
                        (
                            "Screen assets for refrigerants, batteries, oils, "
                            "hazardous components, and stored information. Identify "
                            "the applicable handling route, qualified service provider, and evidence required before resale, recycling, repair, or destruction creates an irreversible exposure."
                        ),
                        (
                            "The cabinet lot contains no powered devices or known "
                            "fluid systems after inspection. A later refrigeration "
                            "lot would require review of 40 CFR 82.154 before "
                            "service or disposal. Batteries may trigger 40 CFR "
                            "Part 273 requirements depending on waste type and "
                            "activity. Data-bearing equipment receives documented "
                            "sanitization using applicable NIST SP 800-88 guidance."
                        ),
                    ),
                    field(
                        "B2B outreach and commercial representations",
                        "textarea",
                        (
                            "Document the outreach channel, audience source, sender "
                            "identity, opt-out process, and claims review. Identify "
                            "the rules relevant to the selected channel and explain how suppression and condition evidence remain linked to outbound campaigns."
                        ),
                        (
                            "Commercial email to repair shops follows 15 U.S.C. "
                            "7704: accurate routing information, nondeceptive subjects, "
                            "required identification and postal address, and a working "
                            "opt-out honored within ten business days. The team "
                            "screens its suppression list before every send and "
                            "avoids automated promotional calls or texts without "
                            "a separate channel-specific review."
                        ),
                    ),
                    field(
                        "Contractual obligations and evidence retention",
                        "textarea",
                        (
                            "Create an obligation register covering purchase, transport, "
                            "repair, buyer delivery, taxes, and special restrictions. "
                            "Assign each record an owner and retention rule tied to applicable requirements, while keeping unresolved obligations visible after physical delivery."
                        ),
                        (
                            "The register links the auction invoice, release, carrier "
                            "receipt, accepted resale certificate, work orders, buyer "
                            "invoice, and signed pickup record. The bookkeeper sets "
                            "retention periods using applicable tax and contract "
                            "requirements. A vehicle file cannot close merely because "
                            "the vehicle left the yard if promised transfer "
                            "documents are still outstanding."
                        ),
                    ),
                ],
                "completion_gate": (
                    "The responsible reviewers document the applicable sale authority, tax "
                    "treatment, contract obligations, transport requirements, and outreach "
                    "controls. Vehicles, restricted goods, exports, and regulated waste "
                    "remain excluded until their specific documentation and disposition "
                    "requirements are resolved."
                ),
            },
            {
                "worksheet_id": "ws-05",
                "number": 5,
                "title": "Automation Pipeline, B2B Growth and Risk Fallback Tracker",
                "purpose": (
                    "Automate discovery, bid calculations, inventory status, and buyer "
                    "follow-up while preserving source evidence and accountable purchasing "
                    "decisions. Build a repeatable B2B resale loop, monitor stale data "
                    "and workflow failures, and maintain manual recovery paths for "
                    "auction deadlines, asset custody, and customer commitments."
                ),
                "chapter_ref": "Q6, Q10",
                "instructions": [
                    (
                        "Begin with platform-provided alerts, saved searches, and permitted "
                        "data access. Define category, geography, price, and removal filters "
                        "before adding software, and never assume a marketplace permits "
                        "automated extraction or bidding merely because its pages are public."
                    ),
                    (
                        "Keep acquisition screening, bid calculation, and bid submission "
                        "as distinct steps. Validate source fields and formula inputs, "
                        "highlight changed sale terms, and require an accountable operator "
                        "to confirm the current ceiling before making a purchase commitment."
                    ),
                    (
                        "Connect each asset's inspection, cost, location, listing, and "
                        "buyer status through a stable identifier. Use restricted write "
                        "access, change history, duplicate checks, and exception alerts "
                        "so automation cannot quietly create conflicting quantities or missing assets."
                    ),
                    (
                        "Build outbound around specific stock that solves a buyer's "
                        "operating need. Track qualified conversations, quotes, paid orders, "
                        "repeat purchases, and collected margin instead of optimizing "
                        "message volume or treating an email reply as realized demand."
                    ),
                    (
                        "Test fallback procedures for expired credentials, missed alerts, "
                        "incorrect premiums, pickup disruption, duplicate sales, and "
                        "suppression failures. Record recovery owners, response times, "
                        "and evidence that the manual process can preserve the transaction "
                        "when integrations stop working."
                    ),
                ],
                "fields": [
                    field(
                        "Auction discovery and alert configuration",
                        "textarea",
                        (
                            "Specify the platforms, permitted alert methods, search "
                            "terms, geographic filters, and review cadence. Identify "
                            "how seller-specific restrictions enter the screening record and how the operator handles incomplete or delayed platform notifications."
                        ),
                        (
                            "Create saved searches for tool cabinets on GSA Auctions, "
                            "GovDeals, and Public Surplus, plus relevant GovPlanet "
                            "categories where available. Route platform emails into "
                            "a dedicated mailbox and review them at 08:00 each "
                            "weekday. A weekly manual platform check measures missed "
                            "opportunities without assuming the alert feed is complete."
                        ),
                    ),
                    field(
                        "Normalized opportunity record and source freshness",
                        "textarea",
                        (
                            "Define required opportunity fields, source timestamps, "
                            "duplicate keys, and freshness limits. Explain how "
                            "the workflow handles amended descriptions, changed closing times, buyer premiums, and absent removal details without silently inventing replacement values."
                        ),
                        (
                            "Airtable stores platform, seller, lot ID, close time "
                            "with time zone, location, premium, removal deadline, "
                            "and saved-source reference. The duplicate key combines "
                            "platform, seller, and lot ID. If removal terms are "
                            "absent, the record stays in a research queue; the "
                            "system never substitutes the previous seller's ten-day window."
                        ),
                    ),
                    field(
                        "Bid worksheet automation and formula tests",
                        "textarea",
                        (
                            "Describe the calculator's inputs, formulas, validation "
                            "rules, version record, and human confirmation step. "
                            "Include test cases that reveal incorrect premium handling, tax assumptions, missing expenses, or rounding above the permitted maximum hammer price."
                        ),
                        (
                            "Google Sheets calculates ceiling = (proceeds times "
                            "(1 - target margin) - other costs) / (1 + premium) "
                            "for the tax-exempt example. A locked test case must "
                            "return $9,727.27 before downward rounding to $9,700. "
                            "Missing premium or tax treatment blocks calculation; "
                            "only the purchasing lead submits the confirmed bid."
                        ),
                    ),
                    field(
                        "Inventory tracking and status transitions",
                        "textarea",
                        (
                            "Define asset identifiers, allowed status changes, "
                            "location fields, supporting evidence, and edit permissions. "
                            "Explain how receiving, repair, listing, reservation, and sale events update quantities without allowing two channels to sell the same physical asset."
                        ),
                        (
                            "CAB-001 progresses through awarded, collected, received, "
                            "repair, sale-ready, reserved, and sold. Airtable requires "
                            "a receiving photo before sale-ready status and a "
                            "buyer reference before reservation. The operations lead "
                            "controls status changes; a daily exception view lists "
                            "assets advertised on two channels without synchronized "
                            "availability or a single accountable owner."
                        ),
                    ),
                    field(
                        "Buyer segments and offer construction",
                        "textarea",
                        (
                            "Define buyer segments by operating need, purchase "
                            "quantity, delivery constraints, and purchasing cycle. "
                            "Write a concrete offer using verified inventory evidence, and explain how the team avoids implying scarce stock or condition claims it cannot substantiate."
                        ),
                        (
                            "Segment independent repair shops needing secure tool "
                            "storage, vocational workshops buying matched sets, "
                            "and industrial resellers purchasing whole lots. Send "
                            "Shop A an offer for four inspected cabinets at "
                            "$8,000 before applicable tax, with dimensions, current "
                            "photos, and pickup windows. State reservation expiry "
                            "only when the inventory system enforces that expiry."
                        ),
                    ),
                    field(
                        "Outbound sequence and suppression workflow",
                        "textarea",
                        (
                            "Set the contact source, message sequence, follow-up "
                            "limits, suppression checks, and reply ownership. "
                            "Explain how the team records opt-outs across tools and pauses campaigns when a synchronization failure could cause unwanted repeat contact."
                        ),
                        (
                            "HubSpot holds forty relevant local business contacts "
                            "with documented source notes. Send one stock-specific "
                            "email and at most one follow-up seven business "
                            "days later unless the buyer engages. Synchronize "
                            "opt-outs before each batch; if synchronization fails, "
                            "pause sending and manually reconcile the suppression "
                            "list rather than relying on last week's export."
                        ),
                    ),
                    field(
                        "Growth funnel and collected-margin metrics",
                        "textarea",
                        (
                            "Define each funnel stage with an observable event "
                            "and denominator. Calculate conversion using a bounded "
                            "cohort, distinguish leads from paid buyers, and connect acquisition effort to collected gross resale proceeds and lot-level realized margin."
                        ),
                        (
                            "A forty-contact cohort produces twelve replies, six "
                            "qualified buyers, four quotes, and two paid orders. "
                            "Contact-to-paid conversion is 2 / 40 = 5%; "
                            "quote-to-paid conversion is 2 / 4 = 50%. "
                            "The two orders total $10,000 before tax. Margin "
                            "is reported only after allocating the actual asset "
                            "costs and selling expenses."
                        ),
                    ),
                    field(
                        "Operational exception alerts and response owners",
                        "textarea",
                        (
                            "List high-impact exceptions, alert thresholds, delivery "
                            "channels, response deadlines, and accountable owners. "
                            "Explain how an unresolved alert escalates and how the team verifies that notification delivery itself remains functional during important auction and removal windows."
                        ),
                        (
                            "Alert operations seventy-two hours before removal "
                            "expires if collection is unconfirmed. Alert purchasing "
                            "when the premium changes or source terms are older "
                            "than the last listing amendment. A daily test message "
                            "checks the shared mailbox. An unanswered urgent alert "
                            "escalates by telephone after thirty minutes during "
                            "staffed operating hours."
                        ),
                    ),
                    field(
                        "Manual fallback and recovery rehearsal",
                        "textarea",
                        (
                            "Describe the offline records, backup contacts, manual "
                            "calculations, and recovery sequence available during "
                            "software failure. Include a timed rehearsal and explain how changes made during the outage are reconciled without overwriting valid later records."
                        ),
                        (
                            "Export the active lot register and pickup schedule "
                            "daily to an access-controlled local folder. During "
                            "a simulated Airtable outage, operations locates the "
                            "seller release and carrier contact within five "
                            "minutes, then logs two custody updates on paper. "
                            "After recovery, the owner enters both updates with "
                            "their original event times and checks for duplicates."
                        ),
                    ),
                    field(
                        "Automation value and capacity boundary",
                        "textarea",
                        (
                            "Estimate hours saved, recurring software costs, "
                            "error reduction, and remaining physical labor. "
                            "Explain which tasks cannot be automated safely and how measured throughput affects staffing without overstating the candidate's overall automation or margin potential."
                        ),
                        (
                            "Alerts, calculators, and inventory views save six "
                            "administrative hours weekly, valued at $30 per "
                            "hour: $180 weekly before software costs. Inspection, "
                            "loading, repair, and title resolution remain physical "
                            "or specialist work. The candidate retains its "
                            "79/100 Money-to-Manpower score; automation does not "
                            "convert a high-leverage, system-disciplined operation "
                            "into a passive business."
                        ),
                    ),
                ],
                "completion_gate": (
                    "The team demonstrates one complete alert-to-record workflow, a tested "
                    "bid calculator, asset-level status controls, synchronized buyer "
                    "suppression, and a successful outage rehearsal. Automation cannot "
                    "submit an unreviewed bid or publish an unsupported asset condition."
                ),
            },
            {
                "worksheet_id": "ws-06",
                "number": 6,
                "title": "30-Day Launch Sprint, Pod Scorecard and Exit-Readiness Ledger",
                "purpose": (
                    "Turn the operating design into a thirty-day evidence-building sprint "
                    "with named responsibilities, bounded capital exposure, and measurable "
                    "commercial progress. Track the canonical scorecard, maintain realistic "
                    "first-deal timing, and assemble transferable records that support "
                    "continued operation, controlled liquidation, or an eventual business sale."
                ),
                "chapter_ref": "Q11, Q12",
                "instructions": [
                    (
                        "Set the first thirty days as an execution and evidence milestone, "
                        "not a promise of completed resale. The canonical first-deal "
                        "window is one to six months, so track readiness and qualified "
                        "opportunities even when disciplined bidding produces no purchase."
                    ),
                    (
                        "Assign the Base pod's two full-time roles and three contractor "
                        "roles to named responsibilities. Define coverage for inspection, "
                        "bidding, removal, bookkeeping, repair, and sales, then describe "
                        "how the Scaled pod expands without silently hiding additional labor."
                    ),
                    (
                        "Break the sprint into weekly deliverables with evidence, owners, "
                        "and spending limits. Complete entity, account, tax, inspection, "
                        "carrier, buyer, and inventory foundations before treating an "
                        "auction win as operational progress or committing the majority "
                        "of available capital."
                    ),
                    (
                        "Review cash, inventory age, removal performance, defect variance, "
                        "collected proceeds, and fully allocated margin every week. "
                        "Use the exact annual scorecard for strategic comparison while "
                        "keeping short-period results distinct from a validated annual run rate."
                    ),
                    (
                        "Maintain an exit-readiness ledger from the first purchase. "
                        "Preserve asset ownership evidence, customer terms, supplier "
                        "records, transferable procedures, and unresolved liabilities; "
                        "test a controlled inventory liquidation before assuming the "
                        "business could be sold without owner involvement."
                    ),
                ],
                "fields": [
                    field(
                        "Canonical position and investment thesis",
                        "textarea",
                        (
                            "Record the candidate identity, pipeline rank, overall "
                            "score, component scores, and operating classification. "
                            "Explain how these fixed reference values shape the launch plan without turning the score into a forecast of actual investment returns."
                        ),
                        (
                            "Candidate #17, Government Surplus Auctions, ranks #29 "
                            "of 29 and scores 79/100, classified High-Leverage Operator Play. Components are revenue potential 21, margin potential 21, team efficiency 15, startup accessibility 12, and automation potential 10. The launch "
                            "therefore prioritizes capital recovery, inspection quality, "
                            "and executable removal rather than aggressive lot count."
                        ),
                    ),
                    field(
                        "Pod roster and accountable role coverage",
                        "textarea",
                        (
                            "Assign the full-time and contractor roles required "
                            "by the canonical scenario. Identify responsibilities, "
                            "backup coverage, cost placement, and the additional roles needed at scale without counting occasional outside assistance as invisible operating capacity."
                        ),
                        (
                            "Base uses 2 FT: a purchasing-and-sales lead and an "
                            "operations-and-inventory lead. Its 3 C are a "
                            "transport provider, repair specialist, and bookkeeper. "
                            "Scaled uses 3 FT + 4 C by adding a full-time "
                            "warehouse operator and contract inspection capacity. "
                            "Employee costs sit in overhead; contracted services "
                            "remain in their designated cost lines."
                        ),
                    ),
                    field(
                        "Days one through seven foundation sprint",
                        "textarea",
                        (
                            "Specify the first week's deliverables, owners, "
                            "evidence, and spending limits. Cover account readiness, "
                            "resale documentation, asset-category selection, buyer discovery, and service-provider qualification before the team submits any binding auction commitment."
                        ),
                        (
                            "By day seven, purchasing completes three platform "
                            "account applications, validates resale documentation, "
                            "and interviews ten local shops. Operations qualifies "
                            "two carriers and one repair specialist, then creates "
                            "the cabinet inspection checklist. Limit research "
                            "and setup spending to $1,500 from the facilities "
                            "and tools allocation; no auction commitment is required."
                        ),
                    ),
                    field(
                        "Days eight through fourteen underwriting sprint",
                        "textarea",
                        (
                            "Define the second week's opportunity funnel, "
                            "inspection targets, comparable evidence, and bid "
                            "worksheet outputs. Explain how the team records rejected opportunities and why a completed underwriting file can be valuable even when no bid is placed."
                        ),
                        (
                            "Screen twenty listings, call five custodians, and "
                            "inspect two suitable lots. Produce two complete "
                            "bid worksheets with buyer evidence and transport "
                            "quotes. Reject one lot because loading access "
                            "conflicts with the carrier's equipment. For the "
                            "cabinet example, publish the $9,700 ceiling and "
                            "document why the team will not exceed it."
                        ),
                    ),
                    field(
                        "Days fifteen through twenty-one execution sprint",
                        "textarea",
                        (
                            "Specify the third week's actions if a suitable "
                            "lot is won and the alternative actions if "
                            "none clears underwriting. Include payment, removal, receiving, and cash controls while avoiding pressure to buy merely to satisfy a calendar target."
                        ),
                        (
                            "If awarded at $9,000, pay the verified $9,900 "
                            "invoice, collect on day six after award, and "
                            "register ten assets at receiving. Preserve $14,400 "
                            "of modeled funding capacity for the lot. If "
                            "bidding exceeds $9,700, record a disciplined loss "
                            "of the auction and inspect the next qualified "
                            "opportunity rather than increasing the ceiling."
                        ),
                    ),
                    field(
                        "Days twenty-two through thirty commercial sprint",
                        "textarea",
                        (
                            "Define the final week's resale, follow-up, closeout, "
                            "and review deliverables. Distinguish paid orders "
                            "from quotes and interest, and explain what completion means when the first transaction remains within the canonical one-to-six-month deal window."
                        ),
                        (
                            "Publish only inspection-supported listings, contact "
                            "forty relevant businesses, and issue written quotes "
                            "to qualified buyers. If inventory is ready, seek "
                            "two prepaid orders without promising that outcome. "
                            "Day-thirty completion means reconciled records, a "
                            "working buyer process, and reviewed cash exposure. "
                            "A still-open first deal remains consistent with "
                            "the one-to-six-month timing range."
                        ),
                    ),
                    field(
                        "Weekly KPI definitions and action thresholds",
                        "textarea",
                        (
                            "Define a compact scorecard with precise numerators, "
                            "denominators, timing, and action thresholds. Include "
                            "cash availability, inventory age, removal reliability, defect variance, buyer conversion, collected proceeds, and fully allocated lot profitability rather than relying on auction wins."
                        ),
                        (
                            "Track completed pickups before deadline divided "
                            "by pickups due, targeting 100%; units unsold over "
                            "forty-five days divided by units held; actual "
                            "defect costs against the $600 allowance; and "
                            "paid buyers divided by contacted buyers. Pause "
                            "new purchases if committed cash would leave less "
                            "than $10,000 of unrestricted operating liquidity "
                            "after scheduled obligations."
                        ),
                    ),
                    field(
                        "Annual scenario bridge and scale decision",
                        "textarea",
                        (
                            "Compare actual results with the three canonical "
                            "annual cases without annualizing a short launch "
                            "period as established performance. State the evidence needed to increase commitments and preserve exact proceeds, owner net profit, margin, and staffing references."
                        ),
                        (
                            "Annual reference points remain $150,000 proceeds "
                            "and $12,000 net at 8%; $575,000 and $80,500 at "
                            "14%; and $1,000,000 and $200,000 at 20%. "
                            "Conservative and Base use 2 FT + 3 C; Scaled "
                            "uses 3 FT + 4 C. Require three completed "
                            "inventory cycles, reliable collections, and verified "
                            "capacity before expanding commitments toward the next case."
                        ),
                    ),
                    field(
                        "Transferable operating records and buyer diligence",
                        "textarea",
                        (
                            "List the records an incoming operator or business "
                            "buyer would need to verify earnings, assets, "
                            "obligations, and repeatability. Identify personal dependencies, account-transfer restrictions, and missing documents that would reduce transferability even when recent sales appear attractive."
                        ),
                        (
                            "The diligence folder contains asset-level purchase "
                            "and sale records, bank reconciliations, tax filings, "
                            "inventory counts, carrier agreements, repair history, "
                            "customer terms, and written procedures. Auction "
                            "accounts and contracts are reviewed for transfer "
                            "restrictions instead of presumed assignable. A "
                            "documented backup performs one weekly operating "
                            "review so the business does not depend entirely "
                            "on the purchasing lead's memory."
                        ),
                    ),
                    field(
                        "Controlled liquidation and stop-loss ledger",
                        "textarea",
                        (
                            "Define the conditions that stop new buying, "
                            "trigger inventory markdowns, or begin a controlled "
                            "wind-down. Record liquidation bids, remaining liabilities, document obligations, and decision ownership so capital recovery is measured after costs rather than by headline sale proceeds."
                        ),
                        (
                            "At day sixty, three unsold cabinets receive a "
                            "wholesale offer of $3,900 against $4,020 of "
                            "allocated modeled presale cost, before selling "
                            "and overhead allocations. The lead evaluates "
                            "the $120 shortfall plus exit costs against "
                            "continued storage and delayed recovery. A wind-down "
                            "plan settles taxes, customer obligations, transport "
                            "bills, and document delivery before distributing residual cash."
                        ),
                    ),
                ],
                "completion_gate": (
                    "The pod completes all thirty-day evidence deliverables, reconciles "
                    "cash and inventory, records its exact staffing and annual scenario "
                    "references, and demonstrates a usable liquidation plan. Continued "
                    "buying requires current liquidity, resolved critical exceptions, "
                    "and a documented capacity-based commitment limit."
                ),
            },
        ],
    }
