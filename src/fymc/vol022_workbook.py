from __future__ import annotations


def build_volume_022_workbook() -> dict:
    def field(name: str, input_type: str, prompt: str, example: str) -> dict:
        return {"name": name, "type": input_type, "prompt": prompt, "example": example}

    return {
        "workbook_id": "wb-022-medical-equipment-resale",
        "volume_id": "vol-022-medical-equipment-resale",
        "title": "Medical Equipment Resale — Operator Companion Workbook",
        "subtitle": (
            "6 Printable Operator Worksheets for Device Underwriting, Resale Economics, "
            "Biomed QA, Regulatory Mapping, Inventory Automation, and Exit-Ready Operations"
        ),
        "worksheets": [
            {
                "worksheet_id": "ws-01",
                "number": 1,
                "title": "Opportunity, Vertical Underwriting & Counterparty Qualification",
                "purpose": (
                    "Select a serviceable equipment niche before committing acquisition cash. "
                    "Document buyer demand, seller authority, device identity, service access, "
                    "and credible liquidation routes so an attractive purchase price cannot "
                    "conceal unsupported software, encumbered ownership, contamination, or obsolete components."
                ),
                "chapter_ref": "Q1, Q2, Q6",
                "instructions": [
                    (
                        "Choose one initial device family and one buyer segment. Compare diagnostic, "
                        "surgical, veterinary, and aesthetic applications without assuming their "
                        "regulatory obligations are interchangeable. Write the intended use, installation "
                        "requirements, and exclusions before collecting seller quotations."
                    ),
                    (
                        "Build a serial-specific acquisition file using seller invoices, asset registers, "
                        "service records, and photographs. Independently verify the selling entity and "
                        "signatory authority; escalate leases, security interests, disputed ownership, and "
                        "missing identification before proposing any payment."
                    ),
                    (
                        "Obtain demand evidence from actual purchasing conversations and completed "
                        "transactions rather than marketplace asking prices. Separate cash buyers "
                        "from contingent buyers, document accessories included in each comparison, "
                        "and adjust for installation, warranty, and software differences."
                    ),
                    (
                        "Ask a qualified biomedical service provider to price inspection and likely "
                        "repairs before submitting a firm bid. Confirm access to manufacturer procedures, "
                        "calibration equipment, replacement parts, software rights, and an appropriate "
                        "decontamination process for the specific device."
                    ),
                    (
                        "Score the opportunity against downside recovery and working-capital limits, "
                        "not just prospective resale spread. Record a named decision owner, acquisition "
                        "ceiling, evidence expiration date, and explicit rejection conditions that remain "
                        "binding when a seller pressures for speed."
                    ),
                ],
                "fields": [
                    field(
                        "Initial vertical and intended-use boundary",
                        "textarea",
                        "Define the first device family, clinical or veterinary application, buyer profile, and excluded configurations. Explain why your service partners can support this boundary without changing intended use or materially altering device performance.",
                        "Start with two established cart-based ultrasound models for outpatient human diagnostic practices. Exclude therapeutic ultrasound, investigational configurations, unsupported operating systems, and undocumented probes. A regional biomed partner supports both models; veterinary opportunities receive a separate intended-use and service assessment before bidding.",
                    ),
                    field(
                        "Buyer demand and purchasing authority",
                        "textarea",
                        "Record qualified buyer conversations, purchasing authority, budget, timing, and installation constraints. Distinguish demonstrated demand from casual interest, and identify the evidence needed before treating a prospect as a credible inventory exit.",
                        "Interview eight imaging practices and qualify three opportunities: budgets of $24,000, $26,000, and $28,000, each with an identified purchasing manager. Two require delivery within ninety days. Obtain written configuration requests; neither verbal interest nor a marketplace message counts as a purchase commitment.",
                    ),
                    field(
                        "Seller identity and authority evidence",
                        "textarea",
                        "Identify the legal seller, asset owner, authorized signer, payment beneficiary, and any intermediary. Describe independent verification steps and the documents establishing that the proposed seller may transfer this particular equipment.",
                        "The hospital asset register identifies unit US-022-017 as owned equipment. Its procurement director supplies a disposal authorization and original invoice. Confirm authority through the hospital switchboard and match bank beneficiary details to the contracting entity before releasing the proposed $14,000 acquisition payment.",
                    ),
                    field(
                        "Title, leases, and security interests",
                        "textarea",
                        "Document title review, lease status, relevant UCC searches, and any required secured-party release. Explain how counsel will resolve ambiguous ownership rather than treating possession or a seller warranty as sufficient evidence.",
                        "Search the seller's exact legal name in the appropriate filing jurisdiction and investigate a blanket equipment lien. Require a serial-specific release from the secured lender and a bill of sale. UCC Article 9 review remains open until counsel confirms the proposed transfer treatment.",
                    ),
                    field(
                        "Device identity and configuration manifest",
                        "textarea",
                        "Capture manufacturer, model, serial number, available UDI information, software version, accessories, and labeled intended use. Specify how photographs and physical inspection will reconcile discrepancies across invoices, labels, and service records.",
                        "Manifest US-022-017 lists one ultrasound console, two identified probes, software version 6.2, a printer, and a locking cart. Photograph each serial plate and probe connector. Record the UDI when present; older equipment lacking one receives a documented identity review rather than an invented identifier.",
                    ),
                    field(
                        "Comparable sales and achievable price",
                        "textarea",
                        "Select comparable completed sales and normalize their condition, accessories, service coverage, delivery, and software rights. State the achievable equipment resale price separately from customer clinical revenue or any estimated procedure economics.",
                        "Three documented comparable transactions closed at $24,000, $25,500, and $26,000 with similar probes. After adjusting the higher-priced package for additional service coverage, underwrite $25,000 gross equipment proceeds. The buyer's projected patient billings are excluded entirely from operator revenue and acquisition justification.",
                    ),
                    field(
                        "Serviceability and obsolescence horizon",
                        "textarea",
                        "Identify support expiration, critical spare availability, software transfer restrictions, cybersecurity support, and technician access. Establish the minimum supported ownership period and the evidence required to price equipment approaching a support cutoff.",
                        "The service partner confirms probe availability from two documented suppliers and a twelve-month repair agreement. Written manufacturer information shows software support continuing through the planned resale window. Reject the lot if its required license cannot transfer or its only replacement power board lacks traceable sourcing.",
                    ),
                    field(
                        "Decontamination and data exposure screen",
                        "textarea",
                        "Describe likely biological contamination and stored patient information before transport or inspection. Assign responsibility for decontamination evidence, data handling, quarantine location, and specialist escalation when the device cannot safely enter ordinary inventory.",
                        "Treat the ultrasound console as potentially containing patient images until verified otherwise. The seller performs documented surface decontamination using compatible procedures, while authorized technicians handle storage sanitization. Receiving staff place the unit in restricted quarantine; no customer demonstration occurs until both evidence packages are accepted.",
                    ),
                    field(
                        "Downside liquidation and bid ceiling",
                        "textarea",
                        "Calculate an acquisition ceiling from credible resale proceeds, inspection and repair costs, transport, defect provision, and required contribution. Add a separate downside recovery case supported by actual wholesale or parts-channel evidence.",
                        "At $25,000 resale, subtract $2,000 refurbishment, $1,000 freight, $1,000 defect provision, and $7,000 required contribution to set a $14,000 bid ceiling. A documented $15,000 wholesale offer less $1,000 outbound costs returns $14,000 before sunk inspection or repair spending.",
                    ),
                    field(
                        "Opportunity decision and rejection conditions",
                        "textarea",
                        "State the acquisition decision, accountable owner, unresolved evidence, expiry date, and hard rejection conditions. Relate the capital and labor burden to the candidate score rather than presenting equipment trading as passive income.",
                        "Proceed only after title release, probe testing, and license confirmation. The acquisition lead owns a ten-business-day offer window. Candidate #14 ranks #22 of 29 with 64/100: revenue 21, margin 16, team 13, startup 6, and automation 8; capital and labor remain substantial.",
                    ),
                ],
                "completion_gate": (
                    "The acquisition lead and biomed reviewer sign a serial-specific underwriting packet "
                    "containing verified seller authority, supported intended use, comparable sales, service "
                    "access, title resolution, contamination and data controls, and an enforceable bid ceiling."
                ),
            },
            {
                "worksheet_id": "ws-02",
                "number": 2,
                "title": "Unit Economics, Scrub Reserve & Working-Capital Float Calculator",
                "purpose": (
                    "Convert equipment spreads into reconciled owner profit and a dated cash requirement. "
                    "Keep acquisition, refurbishment, freight, data scrubbing, defect exposure, and operating "
                    "overhead visible while distinguishing recognized resale proceeds from deposits, unsold "
                    "inventory, customer procedure revenue, and available cash."
                ),
                "chapter_ref": "Q3, Q4",
                "instructions": [
                    (
                        "Copy the three canonical annual scenarios before adding transaction assumptions. "
                        "Preserve their gross revenue, net margins, owner profit, and staffing exactly. "
                        "Use illustrative unit counts only as a reconciliation bridge, not as "
                        "replacement forecasts or promised production."
                    ),
                    (
                        "Build the landed-cost calculation by serial number. Separate acquisition from "
                        "refurbishment, freight, sanitization labor, and defect provision; document whether "
                        "each amount is paid, accrued, reserved in cash, or included within another "
                        "line to prevent duplicate charges."
                    ),
                    (
                        "Draw the cash timeline from seller payment through buyer collection, including "
                        "inspection delays and acceptance terms. Model simultaneous inventory positions "
                        "rather than relying on average annual margin; a profitable transaction can "
                        "still consume unavailable cash."
                    ),
                    (
                        "Reconcile unit contribution to annual overhead and owner net profit. Treat "
                        "reserve additions, claim utilization, inventory write-downs, and cash ring-fencing "
                        "as distinct management events, then have the bookkeeper map them to the "
                        "applicable accounting treatment."
                    ),
                    (
                        "Stress repair cost, resale price, collection timing, and unsold inventory "
                        "individually before combining adverse changes. Set cash minimums and purchase "
                        "stop rules that preserve the service and warranty obligations already sold "
                        "to existing customers."
                    ),
                ],
                "fields": [
                    field(
                        "Canonical scenario reconciliation",
                        "textarea",
                        "Enter all three annual scenarios with exact revenue, net margin, owner profit, and staffing. Define the revenue basis explicitly so equipment sales are never confused with buyer procedure billings or pass-through principal.",
                        "Conservative: $250,000 gross resale revenue, 10% margin, $25,000 owner net, 2 FT plus 4 contractors. Base: $1,025,000, 16.0%, $164,000, the same staffing. Scaled: $1,800,000, 22%, $396,000, 3 FT plus 5 contractors. Acquisition and refurbishment are expenses within these margins.",
                    ),
                    field(
                        "Base-case unit contribution bridge",
                        "textarea",
                        "Specify sale price and each direct cost for a representative unit, then reconcile contribution to the annual base case. Identify which recurring expenses remain in overhead rather than quietly excluding them from owner profit.",
                        "Sell 41 units at $25,000 for $1,025,000. Per unit, deduct $14,000 acquisition, $2,000 refurbishment, $1,000 freight, and $1,000 defect provision: $7,000 contribution. Annual contribution is $287,000; subtract $123,000 overhead to produce exactly $164,000 owner net and a 16.0% margin.",
                    ),
                    field(
                        "Conservative and scaled cost bridges",
                        "textarea",
                        "Construct illustrative unit-volume and cost bridges for the other canonical cases. Preserve each annual profit and show how differences in equipment mix, sourcing, overhead absorption, and repair burden explain the implied economics.",
                        "Conservative uses 10 units at $25,000, $16,500 direct cost each, and $60,000 overhead: $25,000 net. Scaled uses 60 units at $30,000, $20,800 direct cost each, and $156,000 overhead: $396,000 net. These bridges reflect different sourcing and product mixes, not identical unit economics.",
                    ),
                    field(
                        "Scrub, defect, and warranty provision",
                        "textarea",
                        "Separate routine patient-data sanitization from uncertain repair and warranty exposure. State expected frequency, severity, timing, accounting treatment, and cash protection, making clear when actual claims consume an existing provision rather than create duplicate expenses.",
                        "The $2,000 refurbishment allowance includes $150 authorized data-sanitization labor and $1,850 inspection and service work. The separate $1,000 defect provision represents 20% expected claim frequency times $5,000 average severity. A $600 covered repair consumes the tracked provision; the bookkeeper reconciles expense recognition separately.",
                    ),
                    field(
                        "Transaction cash timeline",
                        "textarea",
                        "List payment and collection dates, deposit assumptions, acceptance conditions, and cash exposure before buyer settlement. Distinguish the date inventory becomes ready for sale from the date customer funds become available for another acquisition.",
                        "Pay $14,000 on day zero, $2,000 refurbishment on day twenty, and $1,000 freight on day thirty-five. Deliver and invoice $25,000 on day thirty-five; collect on day sixty-five. Peak paid exposure is $17,000, or $18,000 including a ring-fenced $1,000 defect buffer.",
                    ),
                    field(
                        "Startup capitalization and inventory slots",
                        "textarea",
                        "Allocate startup cash across acquisition slots, refurbishment, freight, protected defect liquidity, overhead runway, and contingency. Reconcile the total to the stated startup range and avoid counting a cash reserve as both spending and available inventory capital.",
                        "Allocate $180,000 as $112,000 for eight acquisitions, $16,000 refurbishment, $8,000 freight, $8,000 protected defect cash, $30,750 for three months of base overhead, and $5,250 contingency. The total sits within the $75,000–$400,000 startup range; protected amounts cannot fund additional purchases.",
                    ),
                    field(
                        "Inventory turns and collection stress",
                        "textarea",
                        "Translate annual unit demand and cash-cycle duration into concurrent funded inventory positions. Round requirements upward and quantify the additional capital or reduced throughput caused by slower acceptance, delayed parts, or extended buyer payment terms.",
                        "At 41 annual units and a 65-day cash cycle, average funding demand is 7.30 units; eight slots support the steady-state plan. At 80 days, demand becomes 8.99 units, requiring nine slots. Add $18,000 protected liquidity or reduce acquisition pace rather than borrowing warranty cash.",
                    ),
                    field(
                        "Overhead and staffing coverage",
                        "textarea",
                        "Break annual overhead into operating categories and explain how full-time staff and contractors are funded. Distinguish contractor headcount from full-time equivalents, and identify compensation assumptions requiring local validation before using the scenario operationally.",
                        "Base overhead is $123,000: $72,000 combined fixed staff compensation and employer burden, $18,000 storage, $12,000 insurance, $9,000 selling costs, $6,000 systems and bookkeeping, and $6,000 administration. Four contractors receive variable assignments inside direct costs. Monthly overhead is $10,250; validate local compensation before hiring.",
                    ),
                    field(
                        "Price, repair, and inventory stress",
                        "textarea",
                        "Calculate a downside unit case and its annual implications without overwriting the canonical scorecard. State the response when price compression and repair overruns erase contribution, including purchase suspension, repricing, or a supported wholesale exit.",
                        "A $22,500 selling price, $14,000 acquisition, $3,500 refurbishment, $1,000 freight, and $1,500 defect provision leave $2,500 contribution. Across 41 units, $102,500 contribution less $123,000 overhead produces a $20,500 loss. Label this a stress case and suspend purchases until costs or pricing recover.",
                    ),
                    field(
                        "Revenue recognition and cash reconciliation",
                        "textarea",
                        "Define how the ledger distinguishes inventory, deposits, earned equipment revenue, receivables, and collections. Assign responsibility for reconciling the management model to accounting records, particularly when acceptance terms, brokerage arrangements, or returns change the transaction substance.",
                        "A $5,000 advance remains a customer deposit until the applicable recognition criteria are met. A qualifying $25,000 equipment sale creates gross resale revenue, not $30,000. Broker-only fees are tracked separately. Reconcile receivables, deposits, inventory costs, provisions, and bank receipts monthly with the bookkeeper.",
                    ),
                ],
                "completion_gate": (
                    "The operator and bookkeeper verify all three canonical profit calculations, the "
                    "$180,000 capitalization allocation, base overhead, reserve treatment, and dated "
                    "cash-cycle model; no acquisition proceeds if protected service liquidity would be spent."
                ),
            },
            {
                "worksheet_id": "ws-03",
                "number": 3,
                "title": "Execution Ledger & Technical QA Pre-Flight Sheet",
                "purpose": (
                    "Control each unit from collection through buyer acceptance using a serial-level "
                    "ledger and evidence-backed technical release. Separate physical custody, contamination "
                    "status, data sanitization, repairs, calibration, and commercial readiness so no "
                    "unverified device reaches a demonstration, shipment, or clinical installation."
                ),
                "chapter_ref": "Q7, Q8",
                "instructions": [
                    (
                        "Create the inventory record before pickup and attach the signed purchase "
                        "documents, configuration manifest, and condition photographs. Assign separate "
                        "custody and technical owners so movement between warehouse, carrier, and "
                        "service provider never silently changes release status."
                    ),
                    (
                        "Receive every device into a controlled quarantine location. Verify identity, "
                        "accessories, transport condition, contamination documentation, and potential data "
                        "exposure before energizing or connecting it; escalate discrepancies to qualified "
                        "personnel rather than improvising repairs or exploratory access."
                    ),
                    (
                        "Use manufacturer procedures and device-specific acceptance criteria for technical "
                        "inspection. Record instrument identity, calibration status, measured results, "
                        "technician qualifications, and outstanding failures. A generic electrical test "
                        "or clean enclosure does not establish clinical performance."
                    ),
                    (
                        "Keep data sanitization and decontamination as separate evidence streams. Verify "
                        "that each process is compatible with the device and accessories, preserves "
                        "necessary functionality, and supports a signed result without placing patient "
                        "information into ordinary resale records."
                    ),
                    (
                        "Complete independent release review before shipment, then collect delivery, "
                        "installation, and acceptance evidence under the contract. Preserve a complaint "
                        "route and serial-specific warranty history so later failures can be traced "
                        "to inspections, parts, and responsible service providers."
                    ),
                ],
                "fields": [
                    field(
                        "Serial-level custody ledger",
                        "textarea",
                        "Define the inventory identifier, physical location, custodian, status, and movement record. Require event timestamps and supporting documents so ownership, custody, technical release, and customer allocation remain independently traceable throughout the resale process.",
                        "Asset US-022-017 enters the ledger at seller pickup with status Quarantine and location Carrier A. Receiving signs the handoff at Bay Q2 and photographs the transport seal. The service partner later acknowledges custody without changing sale readiness; only the technical release reviewer can authorize that change.",
                    ),
                    field(
                        "Receiving inspection and transit damage",
                        "textarea",
                        "List the receiving checks for identity, accessory count, packaging, visible damage, environmental exposure, and documentation. Explain how staff preserve carrier evidence and prevent a damaged or mismatched shipment from entering available inventory.",
                        "Receiving expects one console, two probes, printer, cart, and power cord. A crushed corner and cracked probe holder trigger photographs before unpacking, carrier notification within contractual deadlines, and a damage hold. The $1,000 freight budget does not justify skipping inspection or accepting hidden damage.",
                    ),
                    field(
                        "Decontamination evidence and handling",
                        "textarea",
                        "Record device-specific cleaning and decontamination evidence, responsible personnel, compatible methods, and receiving restrictions. Distinguish surface treatment from validated reprocessing of patient-contact accessories, and identify items requiring specialist handling or rejection.",
                        "Accept the seller's signed surface-decontamination record only after checking device identity, method, date, and compatibility. A reusable endocavitary probe requires its own applicable reprocessing evidence and specialist assessment. Missing records keep that probe quarantined; an apparently clean exterior does not establish readiness for patient contact.",
                    ),
                    field(
                        "Patient-data sanitization and verification",
                        "textarea",
                        "Identify storage media, authorized handling arrangements, sanitization method selection, verification evidence, and exceptions. Explain how the technician protects device functionality while preventing patient identifiers, images, or network credentials from entering resale demonstrations and inventory attachments.",
                        "The authorized technician inventories internal storage and removable media, follows the device-compatible sanitization procedure, and verifies results using an approved protocol aligned with NIST SP 800-88. Store a serial-linked certificate without patient identifiers. Unverifiable media remain controlled pending an approved replacement or destruction decision.",
                    ),
                    field(
                        "Biomed test plan and acceptance limits",
                        "textarea",
                        "Specify the applicable service procedure, qualified tester, required calibrated instruments, and device-specific pass criteria. Cover functional and safety checks without inventing universal thresholds that could conflict with manufacturer requirements or clinical use.",
                        "The biomed partner follows the current service manual for this exact console and probe combination. Record safety-analyzer identification, calibration due date, image-phantom results, probe integrity findings, and each manual-defined acceptance limit. A failed image-uniformity test blocks release even when the console powers on normally.",
                    ),
                    field(
                        "Repair record and parts traceability",
                        "textarea",
                        "Document each defect, approved corrective action, replacement component, source, labor cost, and verification result. Require review when proposed changes could alter intended use or significantly change performance or safety specifications rather than merely restore them.",
                        "Replace a failed cooling fan with a traceable equivalent permitted by the service procedure: $180 part and $220 labor. Record supplier, part number, technician, and post-repair temperature results. A proposed processor upgrade receives a separate remanufacturing assessment before any work order is approved.",
                    ),
                    field(
                        "Software, network, and accessory release",
                        "textarea",
                        "Verify transferable software rights, licensed functions, credential reset, supported connectivity, and accessory compatibility. Explain how demonstrations remain isolated from patient systems and how missing entitlements or unsupported configurations affect the sale description.",
                        "Confirm that purchased imaging options transfer with US-022-017, remove seller network settings, and establish buyer-controlled credentials at installation. Demonstrate using synthetic test data on an isolated network. Exclude a third-party probe lacking documented compatibility, and revise the accessory manifest before issuing the $25,000 quotation.",
                    ),
                    field(
                        "Technical and commercial release packet",
                        "textarea",
                        "List the evidence required for release and distinguish technical approval from price or payment approval. Identify who may sign, how exceptions are resolved, and which failures automatically prevent listing, demonstration, shipment, or installation.",
                        "The packet contains identity photographs, custody history, title documents, decontamination evidence, sanitization certificate, service report, calibrated-test results, license confirmation, and final accessory manifest. The biomed reviewer signs technical release; the sales lead verifies contractual accuracy. An unresolved safety finding blocks shipment regardless of buyer payment.",
                    ),
                    field(
                        "Delivery, installation, and acceptance",
                        "textarea",
                        "Define transport protection, installer responsibilities, destination checks, buyer training, acceptance testing, and the evidence triggering contractual milestones. Tie timing to the cash model while preserving the buyer's agreed process for documenting delivery or performance defects.",
                        "On day thirty-five, an insured carrier delivers the released console and a qualified installer verifies configuration and agreed tests. The buyer signs a serial-specific acceptance record after successful checks. Payment remains due on day sixty-five under the illustrative terms; damage exceptions are recorded before signatures.",
                    ),
                    field(
                        "Complaints, returns, and service continuity",
                        "textarea",
                        "Set the complaint intake record, immediate containment steps, technical escalation, reportability assessment, and warranty-cost linkage. Explain how a returned device reenters quarantine and how other units are checked for a shared defect or sourcing problem.",
                        "A buyer reports intermittent probe dropout ten days after installation. Open a serial-linked complaint, advise suspension of the affected function pending qualified review, and notify the service partner. A $600 covered repair is tracked against the provision; the reviewer assesses reporting duties according to the operator's role.",
                    ),
                ],
                "completion_gate": (
                    "Every offered unit has a complete custody trail and signed technical release "
                    "supported by device-specific testing, compatible decontamination, verified data "
                    "sanitization, transferable configuration, and documented delivery and complaint procedures."
                ),
            },
            {
                "worksheet_id": "ws-04",
                "number": 4,
                "title": "Statutory, Licensing, Contract & Outreach Audit",
                "purpose": (
                    "Map actual business activities to device, privacy, workplace, state, and commercial "
                    "requirements before expanding the catalog. Translate legal findings into records, "
                    "contract clauses, and assigned operating tasks rather than assuming every used "
                    "device, service intervention, or buyer jurisdiction follows identical rules."
                ),
                "chapter_ref": "Q5, Q9",
                "instructions": [
                    (
                        "Classify the device and the operator's actual role for each transaction, "
                        "including resale, servicing, importation, or remanufacturing. Use current FDA "
                        "sources and qualified regulatory review; do not infer obligations solely "
                        "from marketplace category labels or seller assurances."
                    ),
                    (
                        "Compare planned repair activities with FDA servicing and remanufacturing "
                        "guidance. Escalate changes affecting intended use or significantly changing "
                        "safety or performance specifications, and document the resulting registration, "
                        "quality-system, labeling, and premarket analysis before performing the work."
                    ),
                    (
                        "Map state and local requirements to the warehouse, service activities, "
                        "buyer location, and device type. Give special attention to radiation-producing "
                        "equipment, prescription restrictions, and occupational exposure; keep authority "
                        "citations and verification dates in the operating file."
                    ),
                    (
                        "Review purchase, sale, service, transport, and data-handling agreements as "
                        "a connected chain. Ensure title, representations, inspection rights, acceptance, "
                        "warranty scope, software rights, loss allocation, and record access agree "
                        "with the actual workflow and insurance coverage."
                    ),
                    (
                        "Audit every outreach channel and product claim before campaign activation. "
                        "Use truthful condition descriptions, evidence-backed technical statements, "
                        "applicable commercial-email and calling controls, and suppression records; "
                        "never turn clinical claims or regulatory status into unsupported sales language."
                    ),
                ],
                "fields": [
                    field(
                        "FDA device and operator-role map",
                        "textarea",
                        "Identify device classification, product code, intended use, prescription status, and operator role. Record the authoritative source and determine which establishment, listing, labeling, import, or other requirements actually apply to the proposed activities.",
                        "For the selected human-use ultrasound system, verify classification and product code in FDA records and assess 21 CFR Parts 801 and 807. Document domestic resale separately from importing or manufacturing. Do not advertise establishment registration as FDA approval or assume veterinary labeling resolves a human-use device's obligations.",
                    ),
                    field(
                        "Servicing versus remanufacturing analysis",
                        "textarea",
                        "Describe each planned intervention and compare its effects with FDA's servicing and remanufacturing framework. Assign a reviewer to determine applicable manufacturer obligations, including quality-system requirements, before changes to intended use or significant performance specifications proceed.",
                        "Replacing a failed fan to restore documented specifications enters the servicing analysis; changing output parameters or intended use requires deeper review. Consult FDA's May 2024 remanufacturing guidance. If activities constitute manufacturing subject to the rules, assess registration, listing, premarket duties, and the QMSR under 21 CFR Part 820.",
                    ),
                    field(
                        "State licensing and radiation requirements",
                        "textarea",
                        "Create a jurisdiction-specific list of licenses, registrations, permits, and installation duties for the actual catalog and locations. Distinguish ordinary business registration from device-specific requirements, and identify who verifies changes before entering a new state.",
                        "Begin with non-ionizing ultrasound and exclude X-ray systems from the first catalog. Before adding California radiographic equipment, review California Health and Safety Code sections 114960–115273 and applicable Title 17 radiation rules with the state program. Assign separate verification of equipment registration, installer duties, and local business requirements.",
                    ),
                    field(
                        "HIPAA role and data-handling agreement",
                        "textarea",
                        "Determine whether the transaction involves protected health information and whether the operator acts as a business associate. Define permitted access, agreement requirements, subcontractor controls, incident response, and sanitization evidence without assuming all equipment dealers automatically share one status.",
                        "If the dealer handles stored patient images on behalf of a covered clinic, assess business-associate status under 45 CFR 160.103 and agreement duties under 45 CFR 164.502(e) and 164.504(e). Prefer seller sanitization before transfer; incidental resale possession never authorizes browsing patient records.",
                    ),
                    field(
                        "Workplace exposure and transport controls",
                        "textarea",
                        "Identify employee exposure risks, required training, protective practices, waste handling, and transport restrictions. Connect concrete duties to applicable standards and separate ordinary clean equipment freight from regulated materials requiring specialist classification or handling.",
                        "Assess reasonably anticipated occupational exposure under OSHA's Bloodborne Pathogens Standard, 29 CFR 1910.1030, and chemical communication under 29 CFR 1910.1200. Train receiving staff before handling suspect equipment. Units containing regulated batteries or hazardous materials receive a separate transport assessment under applicable 49 CFR requirements.",
                    ),
                    field(
                        "Purchase contract and title protections",
                        "textarea",
                        "Draft the operative acquisition terms covering identity, ownership, liens, inspection access, condition disclosures, data removal, and remedies. Explain how documentary verification supports contractual promises, particularly when equipment comes through brokers or institutional liquidation channels.",
                        "The purchase schedule identifies US-022-017, both probes, and the $14,000 price. Seller represents authority to transfer and discloses liens, recalls, leases, and known defects. Counsel reviews title and warranty language against the state's enacted UCC sections 2-312 and 2-316; signed promises do not replace lien-release evidence.",
                    ),
                    field(
                        "Sales acceptance and warranty allocation",
                        "textarea",
                        "Specify sold condition, included accessories, acceptance tests, payment milestones, limited warranty scope, exclusions, returns, and service response. Ensure the language matches technical evidence and insurance rather than relying on broad condition labels to resolve every dispute.",
                        "Quote the released configuration at $25,000 with listed probes, installation checks, thirty-day payment terms, and a ninety-day parts-and-labor warranty for identified components. Define misuse exclusions and return authorization clearly. Counsel evaluates the state's UCC sections 2-313 through 2-316 and any limits on disclaimers or remedies.",
                    ),
                    field(
                        "Complaint reporting and recall traceability",
                        "textarea",
                        "Determine reporting, corrections, removals, and recall responsibilities from the operator's actual regulatory role. Define a serial-level customer contact process, retained evidence, escalation deadlines, and who evaluates whether an incident triggers mandatory external action.",
                        "Maintain purchaser, serial, installation, and service contacts for every sale. The regulatory reviewer assesses 21 CFR Part 803 duties for applicable manufacturers, importers, or user facilities and Part 806 duties for applicable manufacturers or importers. Reseller status alone does not establish identical obligations; every serious complaint still receives prompt escalation.",
                    ),
                    field(
                        "Commercial outreach and technical claims",
                        "textarea",
                        "Review email, telephone, messaging, and listing practices against applicable channel rules. Record opt-out handling, claim substantiation, sender identity, and buyer targeting so the campaign sells documented equipment capability rather than unsupported clinical or regulatory assertions.",
                        "Commercial email uses accurate headers, a valid postal address, and working opt-out handling under 15 U.S.C. 7704. Calling and texting receive a separate 47 U.S.C. 227 and 47 CFR 64.1200 review. Listings describe tested configurations and condition, never unsupported FDA endorsement or guaranteed clinical outcomes.",
                    ),
                    field(
                        "Insurance, records, and exception ownership",
                        "textarea",
                        "Record insurance coverage, relevant exclusions, retention responsibilities, renewal dates, and unresolved statutory or contractual issues. Assign each exception an owner and a concrete restriction on buying, servicing, marketing, or shipping affected devices.",
                        "Ask the broker to confirm product-liability, completed-operations, cargo, and cyber coverage for the actual resale and service activities, including contractors. Maintain the serial record under a documented retention schedule. An exclusion for aesthetic lasers keeps lasers outside the catalog until coverage and operational requirements are resolved.",
                    ),
                ],
                "completion_gate": (
                    "The operator records a reviewed role-and-jurisdiction map, applicable authority "
                    "citations, contract versions, insurance evidence, privacy arrangements, outreach "
                    "controls, and named exception owners; affected activities remain restricted until "
                    "their specific requirements are satisfied."
                ),
            },
            {
                "worksheet_id": "ws-05",
                "number": 5,
                "title": "Automation, Growth Flywheel & Risk Fallback Tracker",
                "purpose": (
                    "Automate inventory visibility and service-history retrieval without delegating technical "
                    "judgment to software. Connect verified stock, accurate listings, qualified demand, "
                    "and complaint feedback while defining manual recovery paths for integration failures, "
                    "incorrect records, obsolescence signals, and unsellable inventory."
                ),
                "chapter_ref": "Q6, Q10",
                "instructions": [
                    (
                        "Choose one inventory source of truth and a unique serial-linked asset "
                        "identifier. Define required fields, permitted status transitions, evidence "
                        "locations, and accountable owners before connecting the inventory system "
                        "to accounting, customer management, or public listing tools."
                    ),
                    (
                        "Index service documents using controlled metadata and access permissions. "
                        "Automated extraction may suggest dates, parts, or model references, but "
                        "a qualified reviewer must confirm consequential findings against the "
                        "original report before they affect technical release."
                    ),
                    (
                        "Publish only commercially and technically released inventory. Link every "
                        "public specification, accessory list, condition statement, and warranty "
                        "description to reviewed source records; maintain a rapid withdrawal "
                        "process when a unit is sold, held, or reclassified."
                    ),
                    (
                        "Build outreach around verified buyer needs and serviceable inventory "
                        "rather than bulk message volume. Measure qualified conversations, "
                        "configuration matches, accepted quotations, collections, and referrals "
                        "while recording suppression requests and the cost of acquisition."
                    ),
                    (
                        "Test failures deliberately using synthetic records: duplicate serials, "
                        "stale listings, inaccessible documents, accounting sync errors, and "
                        "unsupported equipment. Assign a manual fallback and recovery owner "
                        "for each incident so automation cannot conceal unsafe or unprofitable work."
                    ),
                ],
                "fields": [
                    field(
                        "Inventory source of truth and state model",
                        "textarea",
                        "Select the inventory system, stable asset key, required fields, and authorized state transitions. Distinguish ownership, location, technical release, listing availability, reservation, sale, and collection so a single status cannot obscure incompatible business facts.",
                        "Use Airtable for serial-linked inventory and QuickBooks Online for accounting, with US-022-017 as the shared asset key. Track custody, technical state, commercial state, and payment state separately. A buyer reservation cannot overwrite a quarantine flag, and payment receipt cannot automatically authorize technical release.",
                    ),
                    field(
                        "Service-history indexing and provenance",
                        "textarea",
                        "Define document categories, naming, extracted metadata, reviewer checks, and original-source links. Explain how indexing improves retrieval while preventing uncertain machine extraction, mismatched serials, or stale manuals from becoming authoritative service instructions.",
                        "Store purchase, decontamination, sanitization, test, repair, and warranty documents in restricted folders linked to the asset record. An OCR workflow proposes service dates and part numbers. The biomed reviewer confirms serial identity and manual revision before accepting indexed results; original signed reports remain the controlling evidence.",
                    ),
                    field(
                        "Integrations and reconciliation controls",
                        "textarea",
                        "Specify the events exchanged among inventory, accounting, customer management, and listing systems. Include duplicate prevention, retry handling, failure alerts, and reconciliation so a dropped or repeated event cannot create fictitious revenue or duplicate inventory.",
                        "A reviewed sale event sends one invoice request to QuickBooks Online using an asset-and-order idempotency key. Retry failures enter an exception queue instead of creating another invoice. Each evening, compare sold assets, invoices, deposits, and collections; the bookkeeper resolves differences before the next management report.",
                    ),
                    field(
                        "Access, backups, and sensitive-data exclusion",
                        "textarea",
                        "Define staff permissions, multifactor authentication, backup recovery, audit access, and prohibited data categories. Keep patient information outside resale tools and explain how contractors receive only the records necessary for their authorized work.",
                        "Sales staff see released specifications and sanitized service summaries, while the biomed contractor receives the assigned asset folder. Enable multifactor authentication and export encrypted weekly backups. Patient images and identifiers never enter the CRM. Test restoration monthly with synthetic asset records and document the recovery result.",
                    ),
                    field(
                        "Verified listing publication workflow",
                        "textarea",
                        "Describe the record checks required before listings publish or update. Connect technical claims, price, accessories, availability, and warranty terms to approved evidence, and specify withdrawal timing when inventory status or safety information changes.",
                        "Publish the $25,000 ultrasound only after technical release, license confirmation, accessory reconciliation, and sales-description review. Show actual photographs without patient identifiers. A hold event immediately queues listing withdrawal, with a fifteen-minute operator check to confirm removal from the website and any external marketplace.",
                    ),
                    field(
                        "Buyer segmentation and lawful outreach cadence",
                        "textarea",
                        "Define buyer segments, evidence of equipment need, contact provenance, channel controls, and a practical follow-up sequence. Measure relevant conversations instead of raw contact counts, and explain how suppression requests propagate across every sending system.",
                        "Build a list of forty outpatient practices from public business sources and document model-fit hypotheses. Send individualized equipment-availability emails through HubSpot with required sender details and opt-out handling. Follow up twice over fourteen days unless suppressed; calling or texting starts only after the separate channel review.",
                    ),
                    field(
                        "Growth funnel and acquisition economics",
                        "textarea",
                        "Set measurable stages from qualified prospect to collected sale and calculate selling cost per completed transaction. Separate pilot targets from canonical annual revenue, and include staff or agency effort rather than treating outreach software as the entire acquisition cost.",
                        "A planning funnel uses 120 researched accounts, 24 conversations, eight qualified configuration requests, four quotations, and two collected sales. A fully allocated $400 campaign cost implies $200 per sale if both close. Across 41 annual sales, $8,200 fits within the base $9,000 selling budget.",
                    ),
                    field(
                        "Service feedback and referral flywheel",
                        "textarea",
                        "Explain how acceptance checks, warranty contacts, and service outcomes improve sourcing, listings, and buyer referrals. Define the evidence required before repeating a supplier purchase or making a quality claim based on earlier transactions.",
                        "Contact each buyer seven and thirty days after acceptance to capture configuration satisfaction and service issues. A probe-failure pattern across two units triggers supplier review and tighter incoming tests. Request introductions only after issues are resolved; publish buyer statements only with permission and without patient information.",
                    ),
                    field(
                        "Obsolescence and unsellable-stock triggers",
                        "textarea",
                        "Set aging, support-life, repair-cost, and demand triggers that force a written disposition decision. Assign owners and price floors, and distinguish a management liquidation decision from the accounting assessment of inventory carrying value.",
                        "At sixty days without a qualified quotation, recheck price and demand. At ninety days, obtain two wholesale bids. A supported $15,000 bid less $1,000 selling freight yields $14,000 cash; against $16,000 acquisition-plus-refurbishment cost, assess a $2,000 shortfall and applicable inventory valuation treatment.",
                    ),
                    field(
                        "Automation failure and manual recovery",
                        "textarea",
                        "List the highest-consequence automation failures, detection method, immediate containment, manual operating method, and recovery test. Require reconciliation before restarting integrations so restored software does not replay stale orders or republish held devices.",
                        "If inventory synchronization fails, freeze automated listings and purchases, export the last verified asset register, and maintain a signed movement log. The operations owner reconciles physical stock and open orders before restart. Replay only reviewed events; a test record must confirm that quarantine still prevents publication.",
                    ),
                ],
                "completion_gate": (
                    "The operator demonstrates one complete synthetic asset flow, duplicate-event "
                    "protection, held-stock withdrawal, suppression propagation, backup restoration, "
                    "and manual recovery; technical release remains a qualified human decision."
                ),
            },
            {
                "worksheet_id": "ws-06",
                "number": 6,
                "title": "30-Day Launch Sprint, Pod KPI Scorecard & Exit-Readiness Ledger",
                "purpose": (
                    "Turn the operating design into a sequenced first-month launch without pretending "
                    "that equipment sourcing and sales close immediately. Assign the small-team pod, "
                    "track evidence and cash discipline, and build transferable records that support "
                    "repeatable operations, lender review, and eventual ownership transition."
                ),
                "chapter_ref": "Q11, Q12",
                "instructions": [
                    (
                        "Plan thirty days of setup, qualification, and controlled pipeline development "
                        "against the canonical three-to-nine-month first-deal horizon. Define completed "
                        "evidence and tested processes as launch outputs; do not manufacture booked "
                        "revenue to make the sprint appear successful."
                    ),
                    (
                        "Assign the two full-time roles and four contractor relationships required "
                        "by the base case. Document responsibilities, availability, compensation "
                        "assumptions, and backup coverage; contractor headcount measures people, "
                        "not a promise of four additional full-time work schedules."
                    ),
                    (
                        "Hold a weekly operating review covering cash, inventory age, technical "
                        "exceptions, buyer demand, claims, and evidence completeness. Compare "
                        "actual results with the model while preserving the canonical scenarios "
                        "as reference cases rather than silently rewriting them."
                    ),
                    (
                        "Authorize acquisition spending only after underwriting and liquidity checks "
                        "are complete. Preserve protected service cash and record the reason "
                        "for every rejected purchase; disciplined avoidance of unsellable inventory "
                        "is a measurable operating result during launch."
                    ),
                    (
                        "Assemble an ownership-transition ledger from the first transaction. "
                        "Separate transferable contracts, licenses, records, and operating knowledge "
                        "from owner-dependent relationships, then test whether another authorized "
                        "operator could reproduce the workflow without undocumented judgment or inaccessible files."
                    ),
                ],
                "fields": [
                    field(
                        "Days 1–7: market and control foundation",
                        "textarea",
                        "Schedule the first week's tangible deliverables, accountable people, and completion evidence. Prioritize niche definition, buyer interviews, entity and insurance review, and operating records before purchasing equipment or committing to an expensive warehouse arrangement.",
                        "By day seven, the commercial lead completes eight buyer interviews and a two-model catalog boundary. The operations lead establishes the asset register, obtains two insurance quotations, and requests service-partner credentials. Deliver a written demand summary and controls checklist; no inventory payment is authorized during this foundation week.",
                    ),
                    field(
                        "Days 8–14: supplier and service qualification",
                        "textarea",
                        "Define the second week's sourcing, title, technical, and contracting work. Identify evidence that makes a seller or service provider usable, and specify which missing documents keep a prospective acquisition outside the funded pipeline.",
                        "Qualify three institutional sellers and two biomed providers. Obtain sample service reports, calibration records, insurance evidence, and written pricing for inspection and sanitization. Review one sample purchase agreement and title-search workflow. A seller lacking serial-specific ownership support remains a prospect, not an approved source for the $14,000 bid.",
                    ),
                    field(
                        "Days 15–21: rehearsals and buyer matching",
                        "textarea",
                        "Plan a controlled rehearsal of receiving, quarantine, documentation, technical review, listing, and accounting using synthetic records. Connect potential equipment configurations to qualified buyers without presenting unowned or unreleased equipment as immediately available inventory.",
                        "Run a synthetic US-TEST-022 asset through quarantine, failed inspection, repair review, release, quotation, invoice, and collection reconciliation. Test a duplicate invoice event and a listing withdrawal. Separately match three buyer requests to seller configurations, labeling availability as conditional until ownership, inspection, and release are complete.",
                    ),
                    field(
                        "Days 22–30: launch review and acquisition readiness",
                        "textarea",
                        "Specify the final week's evidence review, cash authorization, unresolved blockers, and next-month pipeline. Distinguish readiness to pursue a first transaction from a completed deal, respecting the longer expected sourcing and selling cycle.",
                        "At day thirty, present one fully underwritten target, eight qualified inventory slots in the cash model, two contracted service alternatives, and a tested release workflow. Spend only if evidence supports the specific purchase. The expected first deal remains three to nine months; readiness does not become recognized revenue.",
                    ),
                    field(
                        "Pod responsibilities and backup coverage",
                        "textarea",
                        "Assign full-time and contractor responsibilities, escalation authority, documented handoffs, and backup arrangements. Connect staffing to the canonical scenarios and identify any service capacity, compensation, or skill limitations that could constrain actual throughput.",
                        "Base staffing uses two full-time people: commercial lead and operations lead. Four contractors cover biomed service, freight and installation, bookkeeping, and regulatory or contract review. Scaled staffing adds one full-time inventory coordinator and one service contractor, totaling eight people: 3 FT plus 5 contractors.",
                    ),
                    field(
                        "Weekly operating KPI definitions",
                        "textarea",
                        "Define each KPI with numerator, denominator, source record, review frequency, and accountable owner. Include cash and safety-oriented measures alongside sales, and prevent targets from encouraging shipment of incomplete devices or concealment of aging inventory.",
                        "Review released units divided by inspected units, quoted qualified buyers divided by qualified conversations, average acquisition-to-collection days, and assets older than ninety days divided by owned assets. Require 100% serial-level evidence completeness before shipment. The operations lead reports holds separately so inspection failures cannot disappear from the denominator.",
                    ),
                    field(
                        "Canonical performance and variance ledger",
                        "textarea",
                        "Record canonical annual targets alongside actual period performance and explain variances through units, price, costs, and timing. Avoid presenting annual averages as evenly distributed monthly outcomes in a lumpy equipment business.",
                        "Base reference is $1,025,000 annual revenue and $164,000 owner net; arithmetic monthly averages are $85,416.67 and $13,666.67. Scaled reference is $1,800,000 and $396,000; Conservative is $250,000 and $25,000. Review actual collected sales and accrued costs separately instead of expecting identical monthly unit counts.",
                    ),
                    field(
                        "Cash floor, purchase stop, and recovery plan",
                        "textarea",
                        "Set protected liquidity, maximum concurrent exposure, and events that suspend acquisitions. Define who may resume buying and what verified improvement is required, especially when collections slip, service claims rise, or inventory becomes difficult to sell.",
                        "Protect $8,000 defect cash, $30,750 overhead runway, and $5,250 contingency within the $180,000 startup plan. Stop new commitments if the 65-day cash cycle stretches toward eighty days without the additional $18,000 ninth-slot funding. Resume only after collected cash or revised purchase pacing restores coverage.",
                    ),
                    field(
                        "Exit-readiness and transferable evidence",
                        "textarea",
                        "Inventory the records, contracts, systems, service relationships, and permissions a successor would need. Identify transfer restrictions and owner-dependent knowledge, while preserving confidentiality and preventing patient data from entering a buyer diligence package.",
                        "Maintain serial-level inventory valuation, supplier agreements, service contracts, warranty exposure, insurance history, monthly reconciliations, and documented workflows. Flag software and customer contracts requiring transfer consent. A redacted diligence folder contains no patient records; the successor receives authorized operating access only under the agreed transaction and access plan.",
                    ),
                    field(
                        "Day-thirty decision and next ninety days",
                        "textarea",
                        "Record the launch decision, remaining blockers, funded actions, review dates, and criteria for expanding the catalog or team. Keep growth contingent on demonstrated serviceability, demand, collections, and evidence quality rather than enthusiasm or inventory volume.",
                        "Proceed with one supported ultrasound family and the qualified seller pipeline; defer surgical energy devices and aesthetic lasers. Over the next ninety days, pursue the first fully documented acquisition, maintain three qualified buyer opportunities, and verify cash weekly. Expand only after successful acceptance, collection, and observed service performance.",
                    ),
                ],
                "completion_gate": (
                    "At day thirty, both full-time role owners sign the evidence-based launch review, "
                    "confirm funded inventory limits and protected liquidity, assign every remaining "
                    "blocker, and approve a dated ninety-day plan consistent with the three-to-nine-month "
                    "first-deal horizon and canonical staffing."
                ),
            },
        ],
    }
