from __future__ import annotations


def build_volume_012_workbook() -> dict:
    def field(name: str, input_type: str, prompt: str, example: str) -> dict:
        return {
            "name": name,
            "type": input_type,
            "prompt": prompt,
            "example": example,
        }

    return {
        "workbook_id": "wb-012-equipment-brokerage",
        "volume_id": "vol-012-equipment-brokerage",
        "title": "Equipment Brokerage — Operator Companion Workbook",
        "subtitle": (
            "6 Printable Operator Worksheets for Heavy Construction, CNC, Fleet, "
            "and Industrial Equipment: Counterparty Underwriting, Commission Economics, "
            "Lien Clearance, Escrow Settlement, Buyer Matching, and Transferable Operations"
        ),
        "worksheets": [
            {
                "worksheet_id": "ws-01",
                "number": 1,
                "title": "Opportunity Underwriting and Counterparty Qualification",
                "purpose": (
                    "Select an equipment vertical where verified ownership, inspectable condition, "
                    "qualified buyers, and collectible commissions support repeatable brokerage. "
                    "Document the seller, buyer, asset, and transaction evidence before spending "
                    "inspection money or circulating a listing that could create avoidable obligations."
                ),
                "chapter_ref": "Q1, Q2, Q6",
                "instructions": [
                    (
                        "Choose one initial vertical and define its operating geography, typical ticket, "
                        "inspection method, and buyer profile. Compare heavy construction, CNC, fleet, "
                        "and industrial machinery using evidence from completed transactions rather "
                        "than advertised prices alone."
                    ),
                    (
                        "Build separate seller, buyer, and asset records before introducing counterparties. "
                        "Verify business identity through official registries, confirm signatory authority "
                        "through independently obtained contact information, and record exactly which "
                        "documents support each qualification decision."
                    ),
                    (
                        "Establish an ownership and lien investigation plan before treating equipment "
                        "as marketable. Capture serial numbers, debtor names, organization jurisdictions, "
                        "physical locations, title documents where applicable, and any lender or "
                        "lessor identified by the seller."
                    ),
                    (
                        "Evaluate condition with a qualified independent inspector who understands "
                        "the machine class. Separate observed facts, seller representations, missing "
                        "tests, estimated repair costs, and buyer acceptance criteria so sales copy "
                        "cannot silently turn assumptions into promises."
                    ),
                    (
                        "Set an explicit pursue, pause, or decline decision with an accountable "
                        "operator and review date. Advance only when the commission mandate, buyer "
                        "capacity, inspection access, and proposed settlement structure justify "
                        "the next expenditure of time and cash."
                    ),
                ],
                "fields": [
                    field(
                        "Vertical thesis and operating boundary",
                        "textarea",
                        "Define the first equipment niche, geographic reach, expected transaction band, "
                        "and buyer use case. Explain why inspection access, transport availability, "
                        "and repeat purchasing make this segment practical for the starting team.",
                        "Start with used three-axis CNC machining centers priced at $75,000–$250,000 "
                        "within 300 miles of Cleveland. Target job shops replacing aging capacity. "
                        "A local service technician can inspect controls and spindle condition, while "
                        "two insured riggers cover loading. Exclude damaged machines and undocumented "
                        "control retrofits during the first quarter.",
                    ),
                    field(
                        "Seller identity and authority evidence",
                        "textarea",
                        "Record the legal seller, registration jurisdiction, independently verified "
                        "contact, authorized signer, and ownership capacity. Distinguish an owner "
                        "from a dealer, lessee, auction intermediary, or employee offering equipment "
                        "without documented authority.",
                        "Lakefront Machining LLC appears as an active Ohio entity. The operations "
                        "manager supplies an equipment invoice, but the managing member signs the "
                        "brokerage mandate after a callback to the company's published number. "
                        "The asset record retains the registry extract, authority confirmation, "
                        "invoice, and dated verification notes.",
                    ),
                    field(
                        "Buyer capacity and purchasing authority",
                        "textarea",
                        "Describe the buyer's operational need, purchasing authority, funding source, "
                        "decision deadline, and installation readiness. Specify what evidence establishes "
                        "capacity without collecting unnecessary account details or treating a lender "
                        "conversation as committed funding.",
                        "A regional job shop seeks one CNC unit before a new production contract "
                        "starts. Its owner approves a $165,000 delivered budget and provides a "
                        "current lender commitment subject to inspection. The facilities lead confirms "
                        "480-volt service, door clearance, floor capacity, and a scheduled installation "
                        "window before an offer is submitted.",
                    ),
                    field(
                        "Asset identity and provenance register",
                        "textarea",
                        "Capture manufacturer, model, serial number, year, hours, options, location, "
                        "and supporting ownership records. Explain how physical identifiers will "
                        "be matched against invoices, maintenance records, lender collateral descriptions, "
                        "and sale documents.",
                        "The listing covers a 2017 machining center, serial MC170428, showing "
                        "18,420 powered hours. The inspector photographs the identification plate "
                        "and control screen. The purchase invoice and service history use the "
                        "same serial. A separate pallet changer is listed explicitly because "
                        "its ownership and lien status also require verification.",
                    ),
                    field(
                        "Lien search scope and release path",
                        "textarea",
                        "Identify the debtor's correct legal name, organization jurisdiction, relevant "
                        "filing offices, titled-property exceptions, and possible fixture interests. "
                        "Record who interprets search results and how each creditor will authorize "
                        "a sale free of its claim.",
                        "For an Ohio-organized LLC, the reviewer checks Ohio UCC records under "
                        "the verified legal name and investigates prior names and moves. A "
                        "blanket equipment filing triggers a lender payoff request identifying "
                        "MC170428. Any fixture filing or title-based interest receives separate "
                        "review; a seller's invoice alone does not establish clear collateral.",
                    ),
                    field(
                        "Condition evidence and defect exposure",
                        "textarea",
                        "List the mechanical, electrical, control, safety, and operating tests required "
                        "for this asset class. Assign responsibility for interpreting results, "
                        "estimating repairs, documenting limitations, and ensuring listing claims "
                        "remain consistent with the actual evidence.",
                        "The CNC technician performs spindle warm-up, backlash checks, tool "
                        "changes, coolant inspection, and a sample cut under agreed conditions. "
                        "A worn way cover carries a $2,400 repair estimate. The report records "
                        "that unattended production reliability was not tested. The listing "
                        "discloses both the observed defect and the testing boundary.",
                    ),
                    field(
                        "Pricing evidence and sale probability",
                        "textarea",
                        "Build a price range from dated comparable transactions, adjusted for "
                        "condition, options, location, and removal costs. Separate asking prices "
                        "from achieved prices and show how uncertainty affects the seller's "
                        "minimum acceptable proceeds.",
                        "Three documented comparable sales closed at $138,000, $149,000, and "
                        "$156,000 before freight. The subject machine's tooling adds an estimated "
                        "$4,000, while repairs subtract $2,400. The seller approves a $150,000 "
                        "target and a $142,000 minimum equipment price, with commission and "
                        "lender payoff calculated separately in the proceeds statement.",
                    ),
                    field(
                        "Commission mandate and conflict disclosure",
                        "textarea",
                        "State who engages the broker, who pays, what consideration determines "
                        "the fee, when it is earned, and when it is payable. Identify exclusivity, "
                        "protected introductions, and any compensation received from another party.",
                        "The seller signs a 90-day exclusive mandate at 10% of equipment "
                        "consideration, excluding separately stated tax, freight, and installation. "
                        "A $150,000 sale generates a $15,000 commission payable through escrow "
                        "at contractual settlement. Named introduced buyers receive a 60-day "
                        "protection period, and any buyer-paid sourcing fee requires written disclosure.",
                    ),
                    field(
                        "Transaction blockers and stop conditions",
                        "textarea",
                        "Identify circumstances that require pausing or declining the deal rather "
                        "than discounting the risk. Include identity inconsistencies, serial tampering, "
                        "inspection refusal, unsupported title claims, restricted destinations, and "
                        "last-minute payment instruction changes.",
                        "Pause this transaction if the serial plate differs from the invoice, "
                        "the lender will not issue a collateral-specific release arrangement, "
                        "or the seller refuses a powered inspection. Decline payment requests "
                        "to an unrelated beneficiary. A changed escrow instruction requires "
                        "independent callback verification before the transaction can resume.",
                    ),
                    field(
                        "Underwriting decision and next expenditure",
                        "textarea",
                        "Record the pursue, pause, or decline decision with the evidence supporting "
                        "it. Name the accountable operator, authorize a limited next expenditure, "
                        "and define the unresolved conditions that must be cleared before "
                        "buyer commitment.",
                        "Pursue subject to lender payoff confirmation and a satisfactory powered "
                        "inspection. The owner authorizes $1,200 for technical inspection and "
                        "$250 for searches, capped at $1,450 total. No binding delivery date "
                        "is offered until the rigger confirms access. Review the file within "
                        "five business days or suspend further spending.",
                    ),
                ],
                "completion_gate": (
                    "The accountable operator signs a dated underwriting decision supported by "
                    "verified identities, an identified asset, a signed fee mandate, a lien "
                    "investigation plan, and a capped next-step budget; unresolved blockers "
                    "remain visibly assigned rather than treated as completed."
                ),
            },
            {
                "worksheet_id": "ws-02",
                "number": 2,
                "title": "Commission Economics, Defect Reserve, and Working-Capital Float",
                "purpose": (
                    "Translate equipment transactions into broker-only revenue, deal contribution, "
                    "annual owner profit, and cash requirements. Reconcile every planning case "
                    "to the canonical scorecard while separating equipment consideration, escrow "
                    "balances, reimbursed expenses, reserve assumptions, and the operator's actual "
                    "working-capital exposure."
                ),
                "chapter_ref": "Q3, Q4",
                "instructions": [
                    (
                        "Copy the three canonical annual scenarios before building individual deal "
                        "models. Preserve gross commission revenue, net margin, owner net profit, "
                        "and team size exactly; use transaction counts and average tickets only "
                        "as explicit supporting planning assumptions."
                    ),
                    (
                        "Calculate commission from the written fee base, then subtract broker-borne "
                        "deal costs and a documented scrub or defect allowance. Keep buyer-paid "
                        "freight, seller loan payoff, equipment principal, and escrow custody "
                        "outside recognized broker revenue."
                    ),
                    (
                        "Separate recurring monthly overhead from transaction-variable costs so the "
                        "published monthly operating range does not become an incorrect cap on "
                        "total annual expenses. Show each cost category once and identify "
                        "whether it consumes cash before settlement."
                    ),
                    (
                        "Model the time between prospecting expenditure and commission collection, "
                        "including failed inspections and postponed closings. Stress startup liquidity "
                        "against the two-to-nine-month first-deal window rather than assuming "
                        "the first signed mandate produces immediate cash."
                    ),
                    (
                        "Reconcile annual profit and the cash bridge independently. Have the "
                        "bookkeeper review fee recognition, pass-through treatment, reserve accounting, "
                        "and owner compensation conventions before using the worksheet to set "
                        "spending limits or contractor commitments."
                    ),
                ],
                "fields": [
                    field(
                        "Canonical annual scenario reconciliation",
                        "textarea",
                        "Enter the exact Conservative, Base, and Scaled commission revenue, net "
                        "margin, annual owner net profit, and staffing. Show implied annual "
                        "expenses and identify any supporting assumptions that are illustrative "
                        "rather than canonical.",
                        "Conservative: $100,000 revenue minus $75,000 expenses equals $25,000 "
                        "owner net profit at 25%, with 1 FT + 3 C. Base: $450,000 minus "
                        "$292,500 equals $157,500 at 35.0%, with 1 FT + 3 C. Scaled: "
                        "$800,000 minus $440,000 equals $360,000 at 45%, with 2 FT + 4 C.",
                    ),
                    field(
                        "Equipment value to commission bridge",
                        "textarea",
                        "Convert completed deal count, average equipment consideration, and commission "
                        "rate into annual broker revenue. Label underlying equipment value separately "
                        "and specify which taxes, freight charges, or ancillary services the "
                        "commission contract excludes.",
                        "Illustrative bridges use a 10% commission: Conservative closes 10 deals "
                        "at $100,000, producing $1,000,000 equipment value and $100,000 revenue. "
                        "Base closes 30 at $150,000, producing $4,500,000 and $450,000. "
                        "Scaled closes 40 at $200,000, producing $8,000,000 and $800,000. "
                        "Equipment value never enters the broker revenue subtotal.",
                    ),
                    field(
                        "Base deal contribution calculation",
                        "textarea",
                        "Calculate the commission and each broker-funded variable cost for one "
                        "representative Base transaction. Include allocated failed-deal expenditure "
                        "and reserve assumptions, then distinguish deal contribution from annual "
                        "owner profit after recurring overhead.",
                        "A $150,000 sale earns $15,000. Budget $1,200 inspection, $1,100 "
                        "sourcing, $900 deal administration, $850 travel and verification, "
                        "$1,000 allocated failed-deal costs, and $1,500 risk allowance. "
                        "Total variable cost is $6,550, leaving $8,450 contribution. Thirty "
                        "closings produce $253,500 before $96,000 recurring overhead.",
                    ),
                    field(
                        "Scrub and defect allowance policy",
                        "textarea",
                        "Define the budgeting allowance for failed inspections, fee concessions, "
                        "and broker-borne remediation. Specify calculation methods, release criteria, "
                        "and accounting review so a planning reserve is not automatically "
                        "treated as a deductible or recognized expense.",
                        "The Base model allocates $30,000 annually to failed-deal costs and "
                        "$45,000 to risk exposure: $1,000 plus $1,500 per closing across "
                        "30 deals. The bookkeeper records actual costs and separately evaluates "
                        "any accounting provision. Unspent planning allowances are not booked "
                        "as expenses merely to preserve the target margin.",
                    ),
                    field(
                        "Recurring overhead and variable expense bridge",
                        "textarea",
                        "Reconcile annual expenses using monthly recurring overhead and separately "
                        "identified deal-variable spending. Keep the $2,500–$14,000 monthly operating "
                        "range visible without implying that total costs including contractors "
                        "and failed pursuits must fit inside it.",
                        "Planning overhead is $2,500 monthly Conservative, $8,000 Base, and "
                        "$14,000 Scaled: $30,000, $96,000, and $168,000 annually. Add "
                        "variable expense of $45,000, $196,500, and $272,000 respectively. "
                        "Totals reconcile to $75,000, $292,500, and $440,000; this decomposition "
                        "is illustrative, while the scenario totals remain fixed.",
                    ),
                    field(
                        "Startup capital and first-deal runway",
                        "textarea",
                        "Choose startup capitalization within $10,000–$75,000 and budget setup, "
                        "recurring overhead, and pre-close costs. Test both short and extended "
                        "first-deal timing, identifying the spending reduction or additional "
                        "capital needed when cash would otherwise run out.",
                        "Start with $60,000, spend $10,000 on setup, and retain $50,000 "
                        "cash. Six months at $2,500 overhead plus $12,000 pre-close spending "
                        "leaves $23,000. A nine-month case with $18,000 pre-close spending "
                        "leaves $9,500. A $10,000 launch would require a materially smaller "
                        "spend plan or committed additional funding.",
                    ),
                    field(
                        "Working-capital float by settlement stage",
                        "textarea",
                        "Map broker cash paid before a commission becomes collectible, including "
                        "inspection deposits, travel, searches, and contractor advances. Exclude "
                        "customer purchase funds and identify contractual reimbursement rights "
                        "without assuming every failed transaction will repay costs.",
                        "Four active files each require $1,200 inspection and $250 searches, "
                        "creating $5,800 immediate float. Add $2,200 shared travel and "
                        "$5,000 overhead during a two-month delay: exposure reaches $13,000. "
                        "Buyer deposits remain with the independent escrow provider and cannot "
                        "fund this operating shortfall or count as available broker cash.",
                    ),
                    field(
                        "Commission recognition and collection policy",
                        "textarea",
                        "Specify contractual earning conditions, payment instructions, collection "
                        "evidence, and treatment of refundable retainers. Distinguish cash receipt "
                        "from revenue recognition and identify the accounting reviewer responsible "
                        "for applying the business's reporting framework.",
                        "The seller mandate earns the $15,000 fee when its defined sale "
                        "completion conditions are satisfied, with payment directed from escrow. "
                        "A refundable $2,000 engagement deposit remains a liability until its "
                        "conditions change. The bookkeeper checks the signed agreement, completion "
                        "evidence, invoice, and escrow remittance before posting commission revenue.",
                    ),
                    field(
                        "Commission compression and delay stress test",
                        "textarea",
                        "Stress the Base model for a lower fee rate, fewer closings, "
                        "and a longer cash cycle. Keep this sensitivity separate from the "
                        "canonical scenario and calculate the operating response required "
                        "before accepting discounted mandates.",
                        "At 8% on the same $150,000 ticket, commission falls to $12,000. "
                        "Keeping $6,550 variable cost leaves $5,450 contribution. Thirty deals "
                        "less $96,000 overhead produce $67,500, not the canonical $157,500. "
                        "Reject routine discounting unless scope or acquisition costs change, "
                        "and separately fund any settlement delay.",
                    ),
                    field(
                        "Break-even volume and cash decision",
                        "textarea",
                        "Calculate annual contribution break-even and a cash spending threshold "
                        "using explicit assumptions. Record who can authorize incremental deal "
                        "costs, which forecast is being used, and when a missed collection "
                        "date forces a revised plan.",
                        "Base contribution is $8,450 per closing; $96,000 divided by $8,450 "
                        "is 11.36, so 12 comparable closings cover modeled recurring overhead. "
                        "This assumes the variable-cost allocation holds. The owner requires "
                        "a refreshed 13-week cash forecast before spending another $1,500 "
                        "whenever unrestricted cash drops below $20,000.",
                    ),
                ],
                "completion_gate": (
                    "All three annual cases reconcile exactly to canonical revenue and owner "
                    "profit; equipment value and customer funds are excluded from broker revenue; "
                    "the bookkeeper reviews accounting assumptions; and the owner accepts a "
                    "funded cash plan covering delayed settlement and failed pursuits."
                ),
            },
            {
                "worksheet_id": "ws-03",
                "number": 3,
                "title": "Execution, Settlement Ledger, and Technical QA Pre-Flight",
                "purpose": (
                    "Control the transaction from signed mandate through inspection, lien resolution, "
                    "escrow disbursement, and physical handoff. Establish evidence-backed checkpoints "
                    "that prevent mismatched assets, misdirected payments, unresolved collateral "
                    "claims, overstated condition, and premature commission recognition from entering "
                    "a completed deal file."
                ),
                "chapter_ref": "Q7, Q8",
                "instructions": [
                    (
                        "Assign a single transaction identifier and named owner before collecting "
                        "documents. Use the same identifier on the CRM record, inspection report, "
                        "payoff request, purchase agreement, escrow instructions, commission invoice, "
                        "and removal checklist to simplify reconciliation."
                    ),
                    (
                        "Sequence inspection, buyer acceptance, creditor documentation, and escrow "
                        "funding deliberately. Record dependencies rather than running every task "
                        "in parallel; a binding removal appointment must not outrun unresolved "
                        "ownership, safety, or settlement conditions."
                    ),
                    (
                        "Create a source-and-use statement before requesting funds, showing every "
                        "recipient and the basis for each payment. Confirm beneficiary details "
                        "through independently established channels and prohibit staff from "
                        "substituting instructions received only through email."
                    ),
                    (
                        "Conduct technical pre-flight with the inspector, buyer, and removal "
                        "provider using documented acceptance criteria. Identify who disconnects "
                        "utilities, secures moving components, protects controls, loads the asset, "
                        "and carries transport risk under the signed agreement."
                    ),
                    (
                        "Close the file only after evidence supports each ledger entry and "
                        "handoff milestone. Reconcile commission receipts, lender disbursement, "
                        "seller proceeds, release documentation, delivery records, and exceptions; "
                        "assign any surviving post-close obligation a deadline."
                    ),
                ],
                "fields": [
                    field(
                        "Transaction record and document index",
                        "textarea",
                        "Define the transaction identifier, file owner, document naming convention, "
                        "and required evidence set. Explain how superseded agreements and "
                        "inspection revisions remain traceable without exposing obsolete payment "
                        "instructions to staff preparing settlement.",
                        "Use EQ-012-003 for the CNC sale. The transaction coordinator owns "
                        "the index containing mandate, identity checks, serial photographs, "
                        "inspection, purchase agreement, lender payoff, and escrow statement. "
                        "Signed revisions receive dated version labels. Superseded instructions "
                        "are retained read-only outside the active settlement folder.",
                    ),
                    field(
                        "Milestone dependency and responsibility map",
                        "textarea",
                        "List the ordered transaction stages, accountable owner, evidence required "
                        "to advance, and latest acceptable completion date. Identify dependencies "
                        "that prohibit shipment or payment release even when other workstreams "
                        "appear ready.",
                        "Day 1: owner validates mandate and identities. Day 4: technician "
                        "finishes inspection. Day 6: buyer signs acceptance subject to specified "
                        "settlement conditions. Day 8: creditor and escrow documents are "
                        "verified. Day 10: settlement occurs under written instructions. "
                        "Loading remains blocked until the designated release confirmation arrives.",
                    ),
                    field(
                        "Technical acceptance test sheet",
                        "textarea",
                        "Specify equipment-class tests, measurable acceptance criteria, report "
                        "signatures, and permitted exceptions. Distinguish safety observations "
                        "from performance measurements and state how retesting occurs after "
                        "repairs or material changes to the machine.",
                        "The buyer requires repeatable positioning within the agreed test "
                        "tolerance, 20 successful tool changes, a 30-minute spindle run, "
                        "and a sample part meeting its drawing. The technician records "
                        "methods and instrument calibration. The worn way cover is accepted "
                        "in writing; a spindle alarm requires repair and documented retest.",
                    ),
                    field(
                        "Creditor payoff and collateral release packet",
                        "textarea",
                        "Document creditor identity, payoff validity, collateral description, "
                        "release authorization, and filing responsibilities. Explain whether "
                        "the transaction requires a partial release, termination, title lien "
                        "discharge, or another instrument matched to the actual security interest.",
                        "The verified lender quotes $60,000 through the scheduled settlement "
                        "date and identifies serial MC170428. Because its blanket lien "
                        "covers other assets, the packet requires an authorized collateral "
                        "release rather than assuming the entire financing statement terminates. "
                        "Escrow instructions link payment to the lender's documented release "
                        "undertaking and follow-up evidence.",
                    ),
                    field(
                        "Escrow source-and-use settlement statement",
                        "textarea",
                        "Reconcile incoming purchase funds to creditor payoff, broker commission, "
                        "escrow charges, and seller proceeds. State assumptions concerning taxes "
                        "and freight, and identify the independent provider responsible for "
                        "holding and disbursing customer money.",
                        "For an equipment-only settlement of $150,000, the independent escrow "
                        "provider disburses $60,000 to the lender, $15,000 to the broker, "
                        "$500 for its fee, and $74,500 to the seller. Uses total $150,000. "
                        "Any applicable tax and buyer-contracted freight are addressed separately "
                        "and must not silently reduce these allocations.",
                    ),
                    field(
                        "Payment instruction verification record",
                        "textarea",
                        "Record who verified each beneficiary, the independent contact source, "
                        "callback time, and second reviewer. Define the response to account "
                        "changes, mismatched beneficiary names, unexpected urgency, or instructions "
                        "that bypass the established escrow arrangement.",
                        "The coordinator verifies escrow details using the provider number "
                        "established during onboarding; the owner independently reviews the "
                        "beneficiary name and payment reference. An email requesting a new "
                        "account pauses funding. Staff contact the known provider representative "
                        "and preserve the suspicious message rather than forwarding its "
                        "instructions into the settlement packet.",
                    ),
                    field(
                        "Broker ledger and pass-through separation",
                        "textarea",
                        "Describe the entries supporting commission revenue, broker-paid expenses, "
                        "receivables, and cash collection. Keep seller proceeds and lender "
                        "payoffs outside the broker ledger when the broker never holds "
                        "or controls those funds.",
                        "When the contractual earning conditions are satisfied, the bookkeeper "
                        "posts a $15,000 commission receivable and corresponding revenue. "
                        "Escrow remittance clears that receivable into broker cash. Inspection "
                        "and sourcing costs follow their own expense records. The $150,000 "
                        "equipment settlement and $60,000 lender payoff are supporting deal "
                        "data, not broker sales.",
                    ),
                    field(
                        "Rigging, transport, and custody handoff",
                        "textarea",
                        "Assign responsibility for disconnecting, decommissioning, lifting, loading, "
                        "transport, unloading, and installation. Capture insurance evidence, "
                        "site constraints, custody signatures, and contract-specific title and "
                        "risk transfer points without assuming they always coincide.",
                        "An insured rigger disconnects and loads the 12,000-pound machine "
                        "using its approved lifting plan. The carrier confirms cargo limits "
                        "and exclusions before dispatch. Buyer and seller record condition "
                        "photographs at pickup. The purchase agreement separately defines "
                        "title passage, loading responsibility, and transport risk; the bill "
                        "of lading records custody transfer.",
                    ),
                    field(
                        "Exception, dispute, and stop-work log",
                        "textarea",
                        "Capture every unresolved mismatch, its operational consequence, responsible "
                        "party, spending limit, and resolution evidence. Explain who may "
                        "authorize continuation and which defects or documentation gaps require "
                        "fresh buyer acceptance rather than an internal note.",
                        "Before loading, the inspector finds a damaged control pendant that "
                        "was intact during testing. Removal pauses. The seller obtains a "
                        "$1,800 repair quote, and the buyer selects repair plus retest "
                        "instead of a price adjustment. The coordinator updates the "
                        "settlement schedule and retains the signed resolution before dispatch.",
                    ),
                    field(
                        "Post-close reconciliation and evidence retention",
                        "textarea",
                        "Specify the closing checklist, unresolved follow-up items, access "
                        "permissions, and retention schedule. Reconcile actual cash and costs "
                        "to the approved model and identify lessons that should change "
                        "future underwriting or contractor selection.",
                        "Within five business days, the coordinator matches the $15,000 "
                        "receipt to the invoice, confirms lender payment and release evidence, "
                        "and stores delivery acknowledgments. Actual inspection costs exceeded "
                        "budget by $200, reducing contribution accordingly. Contract and tax "
                        "records follow the documented retention schedule; access is limited "
                        "to the transaction team and reviewers.",
                    ),
                ],
                "completion_gate": (
                    "No file is marked completed until asset identity, contractual acceptance, "
                    "settlement arithmetic, verified disbursements, required lien-release evidence, "
                    "and custody records agree; all surviving exceptions have an owner, "
                    "deadline, and documented effect on cash or obligations."
                ),
            },
            {
                "worksheet_id": "ws-04",
                "number": 4,
                "title": "Statutory, Licensing, Contract, and Outreach Compliance Audit",
                "purpose": (
                    "Identify the actual legal duties created by the equipment, jurisdictions, "
                    "transaction role, marketing channel, and destination. Translate licensing, "
                    "secured-transactions, warranty, tax, export, and outreach requirements into "
                    "specific records and operating actions rather than relying on a generic "
                    "broker label."
                ),
                "chapter_ref": "Q5, Q9",
                "instructions": [
                    (
                        "Map where the broker, seller, buyer, equipment, and recipient accounts "
                        "are located, then identify the actual activities performed. Licensing "
                        "and tax obligations depend on those facts; calling the business "
                        "a consultant does not resolve statutory coverage."
                    ),
                    (
                        "Review the enacted state secured-transactions rules and any certificate-of-title "
                        "or fixture exceptions before ordering searches. Distinguish evidence "
                        "of a filing from the underlying security interest, and obtain "
                        "transaction-specific creditor release documentation where required."
                    ),
                    (
                        "Make the purchase agreement and brokerage mandate consistent about "
                        "agency, compensation, condition representations, inspection, acceptance, "
                        "payment, and remedies. Assign a qualified reviewer to resolve "
                        "conflicting terms before marketing language or settlement instructions "
                        "create new obligations."
                    ),
                    (
                        "Evaluate export jurisdiction, classification, destination, end user, and "
                        "end use before accepting international commitments. Run outreach "
                        "requirements by channel and recipient type, and preserve records "
                        "showing that restricted contacts and unsubscribe requests are excluded."
                    ),
                    (
                        "Convert each finding into an owner, required document, completion "
                        "date, and operating restriction. Escalate uncertain statutory application "
                        "to the appropriate specialist while continuing only those activities "
                        "that do not depend on the unresolved determination."
                    ),
                ],
                "fields": [
                    field(
                        "Jurisdiction and transaction role map",
                        "textarea",
                        "Identify the governing locations and whether the business acts "
                        "as broker, consignee, owner-dealer, exporter, or payment intermediary. "
                        "Explain how taking possession, title, customer funds, or resale "
                        "inventory would change the review.",
                        "The initial business introduces Ohio sellers to domestic industrial "
                        "buyers, never takes equipment title, and uses independent escrow. "
                        "A proposed fleet expansion adds titled trucks located in California. "
                        "The owner opens a separate licensing and tax review before "
                        "advertising those vehicles because the existing machinery-broker "
                        "workflow does not establish vehicle authority.",
                    ),
                    field(
                        "Dealer and broker licensing determination",
                        "textarea",
                        "Record the equipment category, statutory definitions, exemptions examined, "
                        "regulator contact, and required license or registration. Avoid "
                        "assuming that industrial machinery, titled vehicles, trailers, and "
                        "construction equipment share identical dealer rules.",
                        "For California motor-vehicle activity, the reviewer examines Vehicle "
                        "Code sections 285 and 11700 and confirms the proposed conduct "
                        "with the DMV licensing unit. A written scope memo separates "
                        "untitled CNC brokerage from vehicle dealing. No covered vehicle "
                        "activity begins until the applicable licensing requirements "
                        "and operating conditions are satisfied.",
                    ),
                    field(
                        "UCC search, priority, and release review",
                        "textarea",
                        "Document the applicable enacted Article 9 provisions, debtor location, "
                        "correct name, and collateral exceptions. State how the reviewer "
                        "will address continuing security interests, authorized disposition, "
                        "termination records, and collateral-specific release documentation.",
                        "The Ohio file references Ohio Rev. Code sections 1309.301, "
                        "1309.307, and 1309.503 for governing-law, debtor-location, and "
                        "name analysis. Sections 1309.315 and 1309.513 inform disposition "
                        "and termination review. The lender's authorized sale and release "
                        "documents address the specific machine; a search result alone "
                        "does not prove freedom from liens.",
                    ),
                    field(
                        "Agency, commission, and contract formation",
                        "textarea",
                        "Specify the represented party, authority limits, commission trigger, "
                        "fee base, payment timing, and dispute process. Review written "
                        "sale requirements under the applicable enactment of UCC Article "
                        "2 and keep broker authority distinct from seller authority.",
                        "The mandate authorizes marketing and introductions but not signing "
                        "the sale agreement for the seller. It states a 10% fee "
                        "on equipment consideration and payment through escrow at defined "
                        "completion. The reviewer checks the state's UCC section 2-201 "
                        "writing requirements and records both parties' signed acceptance "
                        "of the final equipment description.",
                    ),
                    field(
                        "Condition representations and warranty allocation",
                        "textarea",
                        "Identify express statements, descriptions, inspection rights, warranty "
                        "language, and remedies that affect the transaction. Review applicable "
                        "UCC sections 2-312, 2-313, and 2-316, distinguishing title obligations "
                        "from condition disclaimers and avoiding unsupported performance claims.",
                        "The listing says the machine completed the documented sample-cut "
                        "test; it does not promise production output. The agreement "
                        "addresses express descriptions, any applicable implied-warranty "
                        "exclusions, and the buyer's inspection acceptance. A generic "
                        "as-is phrase is not treated as resolving title warranties "
                        "or contradicting specific written performance representations.",
                    ),
                    field(
                        "Sales tax and resale documentation",
                        "textarea",
                        "Assign responsibility for determining taxable consideration, sourcing, "
                        "collection duties, resale or manufacturing exemptions, and document "
                        "retention. Explain how a broker-only model differs from taking "
                        "title or operating a marketplace that controls the sale.",
                        "An Ohio tax specialist reviews Ohio Rev. Code sections 5739.01, "
                        "5739.02, and 5739.03 against the actual transaction. The buyer's "
                        "manufacturing exemption claim is supported with the required "
                        "documentation rather than accepted verbally. The settlement sheet "
                        "identifies who collects any tax and keeps that amount outside "
                        "the broker's commission revenue.",
                    ),
                    field(
                        "Export classification and restricted-party screening",
                        "textarea",
                        "Record export jurisdiction, classification evidence, destination, end "
                        "user, end use, screening results, and license determination. "
                        "Separate EAR99 from license-free assumptions and address sanctions "
                        "and controlled technical information as well as physical equipment.",
                        "Before quoting a CNC unit abroad, the specialist reviews the "
                        "EAR under 15 CFR parts 730–774, including classification under "
                        "part 774 and end-use restrictions under part 744. The file "
                        "also records OFAC screening and destination review. EAR99 status "
                        "does not override prohibited parties, destinations, or end uses.",
                    ),
                    field(
                        "Email and telephone outreach controls",
                        "textarea",
                        "Define permitted outreach channels, recipient sourcing, message content, "
                        "opt-out handling, and suppression checks. Identify the applicable "
                        "commercial-email and calling rules instead of assuming that every "
                        "business contact is exempt from channel-specific restrictions.",
                        "Commercial email follows 15 U.S.C. section 7704: accurate headers, "
                        "nondeceptive subjects, required identification, a valid postal address, "
                        "and a working unsubscribe method. Requests are honored within "
                        "10 business days. Automated calls or texts receive separate "
                        "review under 47 U.S.C. section 227 and 47 CFR section 64.1200 "
                        "before activation.",
                    ),
                    field(
                        "Inspection safety and contractor responsibility",
                        "textarea",
                        "Assign site access, hazardous-energy control, lifting, and equipment "
                        "operation responsibilities to competent parties. Identify applicable "
                        "workplace requirements, contractor insurance evidence, and the procedure "
                        "for refusing demonstrations that lack adequate controls.",
                        "At the seller's facility, the responsible employer coordinates "
                        "hazardous-energy procedures under 29 CFR section 1910.147 where "
                        "applicable. Qualified personnel operate the machine and perform "
                        "electrical work. The broker does not instruct visitors to "
                        "bypass interlocks. The rigger provides its lifting plan and "
                        "insurance evidence before removal work is scheduled.",
                    ),
                    field(
                        "Audit findings and remediation register",
                        "textarea",
                        "Summarize each unresolved requirement with its source, affected "
                        "activity, accountable owner, deadline, and required closure evidence. "
                        "Distinguish a documented specialist determination from an informal "
                        "assumption or a checkbox completed without support.",
                        "Finding L-03: California truck brokerage scope remains under review; "
                        "owner obtains the licensing determination before vehicle listings "
                        "launch. Finding E-02: foreign CNC inquiry lacks end-use details; "
                        "export specialist withholds an international commitment. Finding "
                        "T-01: buyer exemption documentation is incomplete; coordinator "
                        "resolves tax treatment before final settlement figures are approved.",
                    ),
                ],
                "completion_gate": (
                    "Each applicable requirement has a documented determination, evidence owner, "
                    "and completed operating action; unresolved licensing, lien, tax, export, "
                    "or outreach questions restrict the affected activity until the responsible "
                    "specialist supplies a usable resolution."
                ),
            },
            {
                "worksheet_id": "ws-05",
                "number": 5,
                "title": "Automation Pipeline, Buyer Alerts, and Risk Fallback Tracker",
                "purpose": (
                    "Automate inventory matching and buyer alerts without amplifying bad listings, "
                    "restricted outreach, stale availability, or payment fraud. Connect structured "
                    "asset data to qualified demand, preserve human accountability for material "
                    "claims, and measure whether each workflow improves collected commission "
                    "contribution."
                ),
                "chapter_ref": "Q6, Q10",
                "instructions": [
                    (
                        "Define a compact source-of-truth schema before connecting software. "
                        "Use stable identifiers for assets, counterparties, mandates, and "
                        "transactions; require provenance, verification status, and update "
                        "timestamps so matching logic can distinguish evidence from "
                        "seller-entered descriptions."
                    ),
                    (
                        "Configure matching around hard operational constraints before softer "
                        "preferences. Voltage, dimensions, lifting limits, budget, control "
                        "compatibility, and inspection access can disqualify a machine "
                        "even when brand, year, or advertised price appears attractive."
                    ),
                    (
                        "Release buyer alerts only for authorized, current listings and "
                        "eligible recipients. Include material defects and the verification "
                        "date, check suppression records immediately before sending, "
                        "and retain the exact message associated with each "
                        "buyer response."
                    ),
                    (
                        "Build retries, duplicate prevention, access controls, and manual "
                        "fallbacks into each integration. Test failure paths with "
                        "synthetic records rather than live payment instructions, "
                        "and prevent automation from changing settlement beneficiaries "
                        "or declaring collateral released."
                    ),
                    (
                        "Review conversion and contribution by source every week. "
                        "Expand only the channels producing qualified inspections "
                        "and collected fees, and retire automations that create "
                        "duplicate contacts, unsupported claims, wasted inspections, "
                        "or more exception-handling work than they remove."
                    ),
                ],
                "fields": [
                    field(
                        "Source-of-truth inventory schema",
                        "textarea",
                        "Define required asset and counterparty fields, validation rules, "
                        "evidence links, ownership of updates, and stale-record handling. "
                        "Choose a maintainable system that supports export and audit "
                        "history without requiring custom software for the initial workflow.",
                        "Use Airtable for assets and Pipedrive for deals, linked by "
                        "asset_id and transaction_id. Required asset fields include serial, "
                        "seller entity, mandate expiry, location, asking price, inspection "
                        "status, lien-review status, and last verification date. "
                        "Records missing a signed mandate or verified serial remain "
                        "excluded from buyer-alert eligibility.",
                    ),
                    field(
                        "Inventory matching rules and explanation",
                        "textarea",
                        "Specify hard filters, ranking factors, tolerances, and the "
                        "explanation shown to an operator. Prevent the system from "
                        "treating missing technical values as positive matches or "
                        "substituting generated specifications for manufacturer evidence.",
                        "A buyer requires 480-volt power, at least 30 inches of "
                        "X travel, Fanuc-compatible controls, and a $165,000 delivered "
                        "ceiling. The matcher rejects incompatible voltage and flags "
                        "missing travel evidence for review. Remaining candidates rank "
                        "by verified specifications, transport cost, inspection readiness, "
                        "and distance rather than keyword similarity alone.",
                    ),
                    field(
                        "Buyer alert eligibility and message controls",
                        "textarea",
                        "Define recipient eligibility, listing freshness, material disclosure "
                        "requirements, send frequency, and unsubscribe checks. Explain "
                        "who approves the first template and how later changes "
                        "are tested before they reach real buyers.",
                        "A scheduled workflow sends at most two relevant alerts per "
                        "buyer weekly. Each includes equipment price, location, inspection "
                        "date, known defects, and the broker's contact details. "
                        "Listings unverified for seven days pause automatically. "
                        "Suppression checks occur immediately before dispatch, and "
                        "the coordinator reviews the first 20 messages against "
                        "their source records.",
                    ),
                    field(
                        "Listing intake and fraud detection workflow",
                        "textarea",
                        "Describe the checks applied to incoming seller submissions "
                        "before publication. Include identity inconsistencies, reused "
                        "photographs, improbable pricing, serial mismatches, missing "
                        "inspection access, and requests to change payment channels "
                        "outside the normal settlement process.",
                        "A web form creates a draft record, never a public "
                        "listing. The coordinator compares registry details, serial "
                        "photographs, and seller contact information, then requests "
                        "a live walkthrough when evidence conflicts. A $150,000 "
                        "machine offered at $45,000 triggers manual review. "
                        "No automated score can override failed ownership verification "
                        "or a prohibited beneficiary change.",
                    ),
                    field(
                        "Outbound account selection and contact evidence",
                        "textarea",
                        "Identify the target account profile, lawful contact sources, "
                        "relevance criteria, and outreach volume limits. Measure "
                        "qualified conversations rather than raw messages and retain "
                        "enough source information to correct erroneous contacts "
                        "and honor removal requests.",
                        "Build 100 regional job-shop accounts from company websites "
                        "and trade directories with permitted use. Prioritize "
                        "documented machining capacity expansions and relevant equipment "
                        "needs. Contact 15 carefully reviewed accounts per business "
                        "day through approved email practices. Record source URL, "
                        "business relevance, response, and suppression status rather "
                        "than purchasing an unreviewed bulk list.",
                    ),
                    field(
                        "Referral and repeat-buyer growth loop",
                        "textarea",
                        "Design a repeatable referral process involving technicians, "
                        "riggers, lenders, and previous buyers. Define compensation "
                        "disclosures, introduction quality, follow-up timing, and "
                        "how the business avoids incentives that distort condition "
                        "reports or equipment recommendations.",
                        "After a completed installation, the coordinator asks the "
                        "buyer about surplus assets and the next capacity need. "
                        "Two riggers and three service technicians can introduce "
                        "potential sellers, but inspection compensation never depends "
                        "on a clean report. Any referral payment is documented "
                        "and disclosed where required, with collected commission "
                        "as the economic evaluation point.",
                    ),
                    field(
                        "Integration reliability and duplicate prevention",
                        "textarea",
                        "Specify event identifiers, retry behavior, rate limits, "
                        "logging, and reconciliation for connected systems. Explain "
                        "how staff detect partial failures, prevent duplicate "
                        "alerts, and restore accurate records without resending "
                        "messages to the entire list.",
                        "A Make workflow uses asset_id, buyer_id, and listing_version "
                        "as an idempotency key. Failed sends enter a review queue "
                        "after three controlled retries. A daily comparison checks "
                        "eligible matches against delivery logs. If the provider "
                        "times out after accepting a message, staff verify its "
                        "delivery identifier before allowing another send attempt.",
                    ),
                    field(
                        "Access permissions and payment isolation",
                        "textarea",
                        "Assign least-privilege access by role, protect integration "
                        "credentials, and separate marketing data from identity "
                        "and settlement records. Define which actions always "
                        "require independent verification and cannot be delegated "
                        "to a matching or messaging workflow.",
                        "Inspectors upload reports but cannot edit bank details. "
                        "Marketing contractors view approved listing data and "
                        "suppression status, not identity documents or payoff "
                        "letters. Credentials remain in the automation platform's "
                        "managed connection store. Settlement beneficiaries are "
                        "verified outside the alert workflow; no API event "
                        "can mark a lender release complete.",
                    ),
                    field(
                        "Manual fallback and recovery rehearsal",
                        "textarea",
                        "Document the operational fallback for CRM outage, "
                        "messaging failure, corrupted inventory, or unavailable "
                        "automation staff. State restoration priorities, evidence "
                        "requirements, and the process for reconciling manual "
                        "work before scheduled workflows restart.",
                        "If matching fails, the coordinator exports the verified "
                        "inventory and manually reviews the ten highest-priority "
                        "buyer briefs. A dated contact log records every "
                        "message and suppression check. On recovery, staff "
                        "import outcomes, reconcile duplicate keys, and inspect "
                        "the pending queue before reactivating scheduled alerts. "
                        "Settlement continues only through its separate verified process.",
                    ),
                    field(
                        "Channel economics and automation retirement rule",
                        "textarea",
                        "Track source-specific spend, qualified buyers, inspections, "
                        "closings, collected commissions, and manual exception time. "
                        "Set explicit continuation criteria so impressive activity "
                        "counts cannot conceal poor conversion or contribution "
                        "after contractor and inspection costs.",
                        "A quarter's targeted outreach costs $3,000 and generates "
                        "12 qualified conversations, four inspections, and one "
                        "$15,000 collected commission. The source report allocates "
                        "actual transaction costs without counting outreach twice. "
                        "A separate workflow requiring six correction hours "
                        "weekly is paused until duplicate alerts fall below "
                        "one per 100 eligible deliveries.",
                    ),
                ],
                "completion_gate": (
                    "A synthetic end-to-end test demonstrates accurate matching, current "
                    "listing checks, suppression enforcement, duplicate prevention, failure "
                    "logging, and manual recovery; the owner confirms that no automation "
                    "can authorize payment changes, invent specifications, or certify lien release."
                ),
            },
            {
                "worksheet_id": "ws-06",
                "number": 6,
                "title": "30-Day Launch Sprint, Pod KPI Scorecard, and Exit-Readiness Ledger",
                "purpose": (
                    "Launch a focused brokerage operation with measurable evidence, disciplined "
                    "cash use, and clear team ownership. Build a transferable operating "
                    "record from the first month while respecting the two-to-nine-month "
                    "first-deal window and treating annual scorecard outcomes as planning "
                    "cases rather than immediate results."
                ),
                "chapter_ref": "Q11, Q12",
                "instructions": [
                    (
                        "Break the first month into four evidence-producing "
                        "workstreams: operating foundation, verified inventory, "
                        "qualified demand, and execution rehearsal. Assign "
                        "owners and modest budgets, and avoid making a "
                        "closed sale the sole definition of launch success."
                    ),
                    (
                        "Staff the initial pod around the canonical one "
                        "full-time operator and three contractors, with "
                        "clear engagement scopes rather than implied full-time "
                        "availability. Define coverage for technical inspection, "
                        "sourcing, coordination, and escalation before increasing "
                        "active deal volume."
                    ),
                    (
                        "Measure leading indicators and realized economics "
                        "separately each week. Track verified mandates, "
                        "qualified buyer briefs, inspection conversion, days "
                        "to settlement, collected commissions, and actual "
                        "cash exposure using consistent definitions that "
                        "cannot reward duplicate records."
                    ),
                    (
                        "Keep a buyer-ready operating archive from the "
                        "first transaction: transferable contracts, clean "
                        "books, documented workflows, permissioned customer "
                        "records, and concentration analysis. Record "
                        "assignment restrictions and owner dependencies "
                        "instead of assuming every relationship can "
                        "transfer automatically."
                    ),
                    (
                        "At day 30, compare evidence and cash against "
                        "the original plan, then select continue, "
                        "narrow, or pause. Preserve canonical annual "
                        "economics as the reference while revising "
                        "the operating forecast when actual conversion "
                        "or costs differ."
                    ),
                ],
                "fields": [
                    field(
                        "Day 1–7 operating foundation",
                        "textarea",
                        "Define the first week's deliverables, accountable "
                        "owners, budget limits, and evidence of completion. "
                        "Prioritize mandate terms, core systems, independent "
                        "service providers, and role-specific requirements "
                        "before purchasing broad advertising or accepting "
                        "complex transactions.",
                        "By day 7, the owner selects CNC brokerage, "
                        "opens the operating account, configures the "
                        "asset register, and obtains reviewed mandate "
                        "and purchase-document templates. The coordinator "
                        "identifies an independent escrow provider and "
                        "two riggers. Setup spending is capped at "
                        "$10,000, with invoices and deliverables attached "
                        "to the launch ledger.",
                    ),
                    field(
                        "Day 8–14 verified inventory sprint",
                        "textarea",
                        "Set a realistic inventory acquisition target "
                        "and specify the evidence required before "
                        "counting a listing. Assign seller interviews, "
                        "identity checks, serial capture, fee agreements, "
                        "inspection access, and preliminary lien-review "
                        "tasks to named roles.",
                        "Interview ten sellers and seek three signed "
                        "mandates. Count a mandate as verified only "
                        "when authority, serial, location, price range, "
                        "and inspection access are documented. The "
                        "owner reviews every file; the sourcing "
                        "contractor manages follow-up. Limit paid "
                        "inspection commitments to two machines until "
                        "qualified buyer interest supports additional spending.",
                    ),
                    field(
                        "Day 15–21 qualified demand sprint",
                        "textarea",
                        "Define target-account research, outreach cadence, "
                        "buyer-brief requirements, and matching reviews "
                        "for the third week. Distinguish a qualified "
                        "buyer from a casual response and establish "
                        "a capacity limit for simultaneous inspections.",
                        "Research 100 relevant job shops, initiate "
                        "75 reviewed contacts over five business "
                        "days, and seek five complete buyer briefs. "
                        "A qualified brief includes budget, funding "
                        "path, specifications, decision authority, and "
                        "installation timing. The coordinator proposes "
                        "matches; the owner authorizes no more than "
                        "two concurrent paid inspections during launch.",
                    ),
                    field(
                        "Day 22–30 execution rehearsal and review",
                        "textarea",
                        "Plan a complete transaction rehearsal or "
                        "live-file review covering inspection, payoff, "
                        "escrow arithmetic, payment verification, and "
                        "handoff. Record launch success criteria that "
                        "remain useful if no commission has been "
                        "collected by day 30.",
                        "Rehearse the $150,000 CNC settlement using "
                        "synthetic documents: $60,000 lender payoff, "
                        "$15,000 commission, $500 escrow fee, and "
                        "$74,500 seller proceeds. Test a changed "
                        "beneficiary alert and failed inspection. "
                        "Day-30 success means three verified mandates, "
                        "five buyer briefs, and a tested workflow; "
                        "first revenue may still take two to nine months.",
                    ),
                    field(
                        "Pod staffing and responsibility coverage",
                        "textarea",
                        "Map the canonical team to concrete functions, "
                        "engagement terms, availability, and escalation "
                        "responsibilities. Explain how contractor counts "
                        "differ from full-time equivalents and which "
                        "capacity constraints justify moving to the "
                        "Scaled team.",
                        "Conservative and Base use 1 FT owner "
                        "plus 3 C: technical inspector, sourcing "
                        "specialist, and transaction coordinator. "
                        "Contractors work defined scopes rather "
                        "than assumed full-time schedules. Scaled "
                        "uses 2 FT plus 4 C, six people "
                        "total, adding full-time operations coverage "
                        "and contractor capacity only when documented "
                        "workload supports the expanded cost structure.",
                    ),
                    field(
                        "Weekly KPI definitions and evidence sources",
                        "textarea",
                        "Define each metric's numerator, denominator, "
                        "measurement window, source record, and owner. "
                        "Include quality and cash indicators alongside "
                        "pipeline counts so staff cannot improve "
                        "reported performance by entering unverified "
                        "listings or repeatedly contacting the same buyer.",
                        "Week 4 reports three verified mandates "
                        "from ten seller interviews, five qualified "
                        "briefs from 12 substantive buyer conversations, "
                        "and two scheduled inspections. Commission "
                        "collected is $0, reported plainly. "
                        "The coordinator also reports $2,900 "
                        "committed inspection-and-search float, oldest "
                        "unresolved blocker age, and the number "
                        "of listings paused for stale evidence.",
                    ),
                    field(
                        "Annual scorecard and scenario drift",
                        "textarea",
                        "Record the candidate ranking, leverage score, "
                        "component scores, and exact annual scenarios. "
                        "Compare current forecasts separately, explaining "
                        "variance without replacing canonical reference "
                        "values or presenting equipment transaction "
                        "value as recognized brokerage revenue.",
                        "Candidate #11 ranks #12 of 29 with "
                        "81/100: revenue potential 22, margin "
                        "potential 20, team efficiency 18, startup "
                        "accessibility 11, and automation potential "
                        "10. Reference commission revenue and "
                        "owner profit remain $100,000/$25,000, "
                        "$450,000/$157,500, and $800,000/$360,000. "
                        "Forecast changes receive a separate dated "
                        "column explaining deal count, pricing, and cost variance.",
                    ),
                    field(
                        "Concentration and owner-dependency register",
                        "textarea",
                        "Measure revenue concentration, critical-provider "
                        "dependency, and tasks only the owner can "
                        "perform. Define backup coverage and evidence "
                        "needed to reduce fragility without delegating "
                        "specialist judgments or sensitive settlement "
                        "decisions to unqualified staff.",
                        "If one seller produces $180,000 of "
                        "the Base $450,000 commission revenue, "
                        "seller concentration is 40%. Maintain "
                        "a second inspector and rigger, document "
                        "buyer-qualification calls, and train the "
                        "coordinator on file assembly. The owner "
                        "retains commercial exception authority while "
                        "an independently verified backup handles "
                        "urgent document checks during planned absence.",
                    ),
                    field(
                        "Exit-readiness and transferable asset ledger",
                        "textarea",
                        "List the contracts, records, systems, relationships, "
                        "and operating evidence a future purchaser "
                        "could evaluate. Record transfer restrictions, "
                        "data-use limitations, ownership of workflow "
                        "assets, and unresolved disputes instead "
                        "of treating all pipeline value as saleable.",
                        "The ledger contains signed mandates with "
                        "assignment provisions identified, documented "
                        "CRM ownership, contractor intellectual-property "
                        "terms, reconciled commission ledgers, and "
                        "transaction-level contribution history. Buyer "
                        "contact records carry source and suppression "
                        "status. Open claims and contingent fees "
                        "are separately listed. Unclosed equipment "
                        "value is excluded from revenue and "
                        "from any claim of collected earnings.",
                    ),
                    field(
                        "Day-30 capital allocation and continuation decision",
                        "textarea",
                        "Choose continue, narrow, or pause based "
                        "on verified pipeline, cash runway, process "
                        "quality, and unresolved risks. Authorize "
                        "the next month's budget with conditions "
                        "and distinguish the decision from any "
                        "promise of near-term closing.",
                        "Continue CNC brokerage with three verified "
                        "mandates, five buyer briefs, and $45,000 "
                        "unrestricted cash after $15,000 of launch "
                        "outflows from the $60,000 capitalization. "
                        "Authorize $2,500 overhead and $3,000 "
                        "incremental pursuit spending next month. "
                        "Defer fleet expansion until licensing "
                        "review is complete, and refresh the "
                        "13-week cash forecast before every additional inspection commitment.",
                    ),
                ],
                "completion_gate": (
                    "The owner signs the day-30 review with evidence-linked milestones, "
                    "actual cash, canonical scenario references, assigned pod responsibilities, "
                    "documented transfer limitations, and a funded next-month plan; no "
                    "unclosed deal or customer-held funds are represented as earned revenue."
                ),
            },
        ],
    }
