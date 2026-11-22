from __future__ import annotations


def build_volume_034_workbook() -> dict:
    def field(name: str, input_type: str, prompt: str, example: str) -> dict:
        return {
            "name": name,
            "type": input_type,
            "prompt": prompt,
            "example": example,
        }

    return {
        "workbook_id": "wb-034-nemt-and-medical-courier-arbitrage",
        "volume_id": "vol-034-nemt-and-medical-courier-arbitrage",
        "title": "NEMT & Medical Courier Dispatch Arbitrage — Operator Companion Workbook",
        "subtitle": (
            "6 Printable Operator Worksheets for Medicaid Standing Orders, "
            "Workers' Compensation Transport, STAT Specimen Routes, Driver "
            "Settlement Controls, Payment Float, and Acquisition-Ready Dispatch Pods"
        ),
        "worksheets": [
            {
                "worksheet_id": "ws-01",
                "number": 1,
                "title": "Arbitrage Deal / Counterparty Underwriting & Spread Qualification",
                "purpose": (
                    "Qualify a healthcare logistics contract before committing dispatch capacity "
                    "or driver settlements. Separate authorized passenger trips from specimen "
                    "deliveries, verify the actual payer and service requirements, and establish "
                    "whether the retained spread survives cancellations, documentation failures, "
                    "backup coverage, and delayed collections."
                ),
                "chapter_ref": "Q1, Q2, Q6",
                "instructions": [
                    (
                        "Choose one named counterparty and one service lane for this sheet. "
                        "Collect its proposed agreement, rate exhibit, authorization workflow, "
                        "payment calendar, and sample documentation requirements before calculating "
                        "spread or discussing a launch date with drivers."
                    ),
                    (
                        "Underwrite the organization that actually owes payment rather than "
                        "the facility requesting transportation. Verify contracting authority, "
                        "provider enrollment requirements, dispute rights, and whether a broker "
                        "can withhold unrelated invoices after a single disputed trip."
                    ),
                    (
                        "Build a representative service basket using completed trips or accepted "
                        "route stops, not requested appointments. Price empty repositioning, "
                        "wheelchair capacity, wait time, failed handoffs, after-hours dispatch, "
                        "and backup assignments explicitly before accepting a blended rate."
                    ),
                    (
                        "Interview at least two qualified carrier businesses about the proposed "
                        "lane. Verify actual operating capacity and settlement expectations, then "
                        "compare their quotes against the service requirements without assuming "
                        "that contractor classification follows from the agreement heading."
                    ),
                    (
                        "Record a proceed, renegotiate, or decline decision supported by documents "
                        "and arithmetic. Assign an owner and resolution date to every unresolved "
                        "condition; do not convert an unverified standing-order forecast into "
                        "committed revenue or immediately spendable cash."
                    ),
                ],
                "fields": [
                    field(
                        "Contracting entity and collectible payment obligation",
                        "textarea",
                        (
                            "Identify the legal buyer, requesting facility, payer intermediary, "
                            "and authorized signer. Explain which entity owes your company money, "
                            "which contract establishes that obligation, and what evidence supports "
                            "its ability to pay."
                        ),
                        (
                            "Illustrative Harbor Access TPA signs the dispatch agreement and owes "
                            "accepted invoices; three dialysis centers only submit schedules. The "
                            "file contains the TPA's W-9, signer authorization, insurance certificate, "
                            "and two vendor references reporting payment within 42 days. A facility "
                            "scheduler's email cannot expand the TPA's contracted payment obligation."
                        ),
                    ),
                    field(
                        "Service lane and authorized demand evidence",
                        "textarea",
                        (
                            "Define geography, passenger assistance level or specimen class, "
                            "operating hours, and recurring demand. Distinguish a planning forecast "
                            "from a written purchase commitment and identify the authorization "
                            "required for each billable service."
                        ),
                        (
                            "The pilot covers ambulatory dialysis transportation within a 22-mile "
                            "service area, weekdays from 05:30 to 18:00. Thirty patients generate "
                            "up to 180 one-way legs weekly at three round trips each. Only "
                            "150 legs currently have valid authorizations; the remaining 30 stay "
                            "outside the committed revenue forecast until verified."
                        ),
                    ),
                    field(
                        "Rate card and retained spread qualification",
                        "textarea",
                        (
                            "Calculate gross billings, carrier settlement, and retained dispatch "
                            "contribution for the service basket. Show approved accessorial charges "
                            "separately and explain whether quoted rates preserve the canonical "
                            "45 percent retained share."
                        ),
                        (
                            "A sample basket contains 100 completed one-way legs billed at $50 "
                            "each, producing $5,000 gross billings. Carrier settlements total "
                            "$2,750, leaving $2,250 retained contribution, exactly 45 percent. "
                            "A separately authorized $20 wait charge with a $15 carrier payment "
                            "retains only 25 percent and must be modeled separately."
                        ),
                    ),
                    field(
                        "Standing-order durability and concentration exposure",
                        "textarea",
                        (
                            "Document standing-order renewal, termination notice, appointment "
                            "variability, and customer concentration. Estimate the contribution "
                            "lost if the largest facility withdraws, and identify a credible "
                            "replacement lane rather than assuming immediate demand substitution."
                        ),
                        (
                            "The TPA provides a 90-day standing-order schedule but may terminate "
                            "on 30 days' notice. Its largest dialysis center supplies $18,000 "
                            "monthly billings and $8,100 retained contribution at 45 percent. "
                            "The replacement pipeline contains two laboratory opportunities, "
                            "but neither enters the forecast before a signed service order exists."
                        ),
                    ),
                    field(
                        "Carrier capacity and operational evidence",
                        "textarea",
                        (
                            "List primary and backup carrier businesses, permitted service "
                            "capabilities, insurance evidence, vehicle availability, and dispatch "
                            "acceptance rules. Separate available vehicles from merely registered "
                            "vehicles and explain how capacity was independently verified."
                        ),
                        (
                            "Carrier A demonstrates four available ambulatory vehicles; Carrier B "
                            "documents two wheelchair-accessible vehicles with current inspections. "
                            "The dispatcher verifies certificates directly with the insurance "
                            "producer and observes one scheduled service demonstration. Two additional "
                            "registered vehicles remain excluded because their drivers are unavailable "
                            "during the dialysis morning peak."
                        ),
                    ),
                    field(
                        "STAT route acceptance and handoff requirements",
                        "textarea",
                        (
                            "Define pickup deadlines, destination acceptance hours, specimen "
                            "classification, packaging responsibility, and temperature instructions. "
                            "Identify who can reject a shipment and who resolves a missed "
                            "handoff without allowing dispatchers to improvise clinical decisions."
                        ),
                        (
                            "The laboratory requests pickup within 30 minutes and delivery within "
                            "90 minutes of acceptance. The laboratory classifies and packages each "
                            "shipment; the courier verifies the external package checklist and "
                            "barcode. A leaking package is refused and escalated to the laboratory "
                            "supervisor, who determines replacement collection and clinical urgency."
                        ),
                    ),
                    field(
                        "Payment terms and disputed invoice boundaries",
                        "textarea",
                        (
                            "Extract the payment clock, clean-invoice definition, submission "
                            "deadline, correction window, offset rights, and collection escalation "
                            "path. Identify whether timing begins at service completion, invoice "
                            "receipt, or acceptance after a separate validation process."
                        ),
                        (
                            "The draft pays Net-45 after acceptance, with acceptance allowed "
                            "five business days after submission. Weekly batching adds up to "
                            "seven calendar days before submission. The counterproposal requires "
                            "itemized disputes within five business days and payment of undisputed "
                            "lines on schedule, preventing one missing trip signature from freezing "
                            "the entire weekly invoice."
                        ),
                    ),
                    field(
                        "Denial and clawback evidence assessment",
                        "textarea",
                        (
                            "Review a sample of historical denials or simulated exceptions. "
                            "Identify missing authorization, unsupported mileage, duplicate "
                            "submission, and absent delivery evidence separately, then assign "
                            "prevention controls and a recoverability estimate supported by documentation."
                        ),
                        (
                            "A 200-leg sample contains six missing authorization references, "
                            "three mileage mismatches, and one duplicate submission. The ten "
                            "affected $50 lines represent $500 of exposure before correction. "
                            "Authorization validation blocks new bookings; GPS review resolves "
                            "mileage exceptions; the duplicate is voided rather than resubmitted "
                            "under a different trip identifier."
                        ),
                    ),
                    field(
                        "Pricing floor and adverse service basket",
                        "textarea",
                        (
                            "Stress the quote with increased carrier rates, canceled appointments, "
                            "and backup usage. Calculate the price needed to retain 45 percent "
                            "after carrier settlement and explain what contract adjustment "
                            "would preserve the service's economics."
                        ),
                        (
                            "If carrier settlement rises from $27.50 to $30 per completed leg, "
                            "a $50 customer rate retains $20, or 40 percent. Preserving "
                            "45 percent requires $30 divided by 0.55, approximately $54.55. "
                            "The proposed exhibit therefore includes a documented rate-review "
                            "mechanism rather than silently assuming the original spread survives."
                        ),
                    ),
                    field(
                        "Underwriting decision and unresolved conditions",
                        "textarea",
                        (
                            "State the commercial decision, evidence supporting it, outstanding "
                            "conditions, accountable owners, and expiration date of the offer. "
                            "Explain which unresolved issues prevent service acceptance and which "
                            "can be monitored after a limited pilot."
                        ),
                        (
                            "Decision: renegotiate the 150-authorized-leg pilot at the current "
                            "$50 rate only if $27.50 carrier settlements remain available. "
                            "The operations lead must verify backup coverage, and the controller "
                            "must remove portfolio-wide invoice offsets. The offer expires in "
                            "14 days; no trips are accepted before the signed rate exhibit "
                            "and service credentials are complete."
                        ),
                    ),
                ],
                "completion_gate": (
                    "The commercial owner and operations lead sign only after the collectible "
                    "payer, authorization process, primary and backup capacity, pricing basket, "
                    "and payment-clock exposure are evidenced. Every unresolved launch-critical "
                    "condition has a named owner and blocks the affected service lane."
                ),
            },
            {
                "worksheet_id": "ws-02",
                "number": 2,
                "title": "Unit Economics, Reserve Float & Working-Capital Calculator",
                "purpose": (
                    "Reconcile the three canonical scenarios without treating driver settlements "
                    "as retained revenue or patient activity as operator sales. Calculate "
                    "collection float, operating cash needs, restricted reserves, and a funded "
                    "volume ceiling before scaling an otherwise profitable dispatch book."
                ),
                "chapter_ref": "Q3, Q4",
                "instructions": [
                    (
                        "Copy the canonical annual gross billings, 45 percent retained share, "
                        "and owner profit into separate columns. Derive carrier settlements "
                        "and residual operating expense algebraically so the worksheet cannot "
                        "silently substitute a different profitability assumption."
                    ),
                    (
                        "Maintain distinct reporting views for customer billings, carrier "
                        "payables, retained contribution, and owner profit. Document the "
                        "contract-specific ASC 606 principal-versus-agent conclusion; the "
                        "scorecard's retained-share presentation does not determine accounting "
                        "treatment for every future agreement."
                    ),
                    (
                        "Use a declared day-count convention when converting annual figures "
                        "into a float requirement. Include service-to-invoice delay and "
                        "acceptance delay when measuring cash exposure, rather than treating "
                        "a nominal Net-45 clause as the complete collection cycle."
                    ),
                    (
                        "Separate reusable working capital from setup spending, operating "
                        "losses, and restricted balances. Count a credit facility only after "
                        "its documents, borrowing conditions, availability, and draw timing "
                        "have been confirmed by the responsible treasury owner."
                    ),
                    (
                        "Stress collections and denial losses before committing additional "
                        "standing orders. When available liquidity cannot support the "
                        "proposed volume, reduce the funded volume ceiling, renegotiate "
                        "settlement timing, or secure additional committed capital before "
                        "accepting the exposure."
                    ),
                ],
                "fields": [
                    field(
                        "Conservative scenario reconciliation",
                        "textarea",
                        (
                            "Reconcile the Conservative scenario from gross billings through "
                            "carrier settlements, retained contribution, operating expense, and "
                            "owner profit. State both gross-billings margin and retained margin "
                            "so the two denominators remain unambiguous."
                        ),
                        (
                            "Conservative annual billings are $250,000. Carrier settlements "
                            "equal $137,500 at 55 percent, leaving $112,500 retained contribution. "
                            "Other operating expense is $82,500, producing $30,000 owner net "
                            "profit. Profit equals 12 percent of gross billings and 26.67 percent "
                            "of retained contribution. The reported core team is 2 FT plus 2 C."
                        ),
                    ),
                    field(
                        "Base scenario reconciliation",
                        "textarea",
                        (
                            "Reconcile the Base scenario using the supplied annual figures "
                            "without adding revenue from patient appointments or laboratory "
                            "testing. Calculate monthly planning amounts from unrounded annual "
                            "values and identify the reported core staffing configuration."
                        ),
                        (
                            "Base annual billings are $925,000; settlements are $508,750; retained "
                            "contribution is $416,250; other expense is $249,750; owner profit "
                            "is $166,500. Gross-billings margin is 18 percent and retained margin "
                            "is 40 percent. Monthly owner profit is $13,875, with a reported "
                            "core team of 2 FT plus 2 C."
                        ),
                    ),
                    field(
                        "Scaled scenario reconciliation",
                        "textarea",
                        (
                            "Reconcile the Scaled Small-Team scenario and disclose the difference "
                            "between core personnel and external carrier capacity. Preserve "
                            "the canonical profit while recording staffing or settlement "
                            "assumptions that would require a separate sensitivity case."
                        ),
                        (
                            "Scaled billings are $1,600,000; settlements are $880,000; retained "
                            "contribution is $720,000; other expense is $336,000; owner profit "
                            "is $384,000. Margins are 24 percent of billings and 53.33 percent "
                            "of retained contribution. The core team is 3 FT plus 3 C; "
                            "external carrier personnel are inventoried separately, not represented "
                            "as six people performing every trip."
                        ),
                    ),
                    field(
                        "Operating expense bridge and planning assumptions",
                        "textarea",
                        (
                            "Bridge the stated $3,500 to $18,000 monthly operating range to "
                            "each scenario's implied total expense. Label any allocation as "
                            "a planning assumption rather than changing the canonical totals "
                            "or hiding omitted labor costs."
                        ),
                        (
                            "Planning allocation only: fixed overhead is $3,500, $12,000, and "
                            "$18,000 monthly for Conservative, Base, and Scaled. Remaining annual "
                            "expense is $40,500, $105,750, and $120,000 respectively. Together "
                            "these reconcile to $82,500, $249,750, and $336,000. The supplied "
                            "monthly range is therefore not presented as each scenario's complete "
                            "all-in expense."
                        ),
                    ),
                    field(
                        "Revenue presentation and settlement accounting",
                        "textarea",
                        (
                            "Describe the contractual control assessment supporting gross or "
                            "net revenue presentation under ASC 606. Preserve the scorecard's "
                            "45 percent retained contribution view while keeping customer "
                            "receivables, settlement liabilities, and recognized revenue distinguishable."
                        ),
                        (
                            "For the Base planning view, $925,000 customer billings less $508,750 "
                            "carrier settlements leaves $416,250 retained contribution. The "
                            "accountant documents the principal-agent assessment under ASC "
                            "606-10-55-36 through 55-40 for each contract. An agent presentation "
                            "recognizes the net fee; a supported principal presentation recognizes "
                            "gross revenue and carrier expense without changing the underlying cash."
                        ),
                    ),
                    field(
                        "Thirty-day and forty-five-day cash float",
                        "textarea",
                        (
                            "Calculate carrier and operating cash needed before collections "
                            "using a 30-day planning month. State whether the interval measures "
                            "actual service-to-cash timing, and include a separate reserve "
                            "without describing internal cash as customer escrow."
                        ),
                        (
                            "Base monthly settlements are $42,395.83 and other expense is "
                            "$20,812.50. Funding 30 days plus a $10,000 reserve requires "
                            "$73,208.33. Funding 45 days requires $63,593.75 settlements plus "
                            "$31,218.75 expense plus $10,000 reserve, totaling $104,812.50. "
                            "Calculations use unrounded annual values; the reserve is internal "
                            "treasury cash, not a customer escrow account."
                        ),
                    ),
                    field(
                        "Collection-delay sensitivity and liquidity response",
                        "textarea",
                        (
                            "Extend the cash-conversion interval to include invoice batching, "
                            "acceptance lag, and slower payment. Calculate the revised funded "
                            "requirement and identify the exact action taken before accepting "
                            "new services beyond available liquidity."
                        ),
                        (
                            "A 60-day service-to-cash stress requires two Base months of "
                            "settlements and expense: $126,416.67, plus the $10,000 reserve, "
                            "totaling $136,416.67. Against $115,000 of confirmed liquidity, "
                            "the shortfall is $21,416.67. New recurring volume pauses until "
                            "collections accelerate, settlement terms change, or additional "
                            "capital is committed and available."
                        ),
                    ),
                    field(
                        "Startup uses and committed capital stack",
                        "textarea",
                        (
                            "Allocate startup cash among setup spending, available working "
                            "capital, and protected reserves. Compare the remaining liquidity "
                            "with the float requirement and distinguish funded resources "
                            "from unsigned credit proposals or expected customer payments."
                        ),
                        (
                            "A $65,000 startup contribution funds $15,000 of setup costs and "
                            "leaves $50,000 cash. A signed, drawable $65,000 working-capital "
                            "line brings available liquidity to $115,000. Against the "
                            "$104,812.50 Base 45-day requirement, headroom is $10,187.50. "
                            "The line exceeds startup equity and is separately disclosed; "
                            "a lender's preliminary term sheet would contribute zero available funding."
                        ),
                    ),
                    field(
                        "Denial loss and reserve replenishment",
                        "textarea",
                        (
                            "Model an incremental unrecoverable denial separately from canonical "
                            "profit. Explain whether carrier settlements remain payable, "
                            "how reserve cash is replenished, and why reserving cash does "
                            "not itself create an additional operating expense."
                        ),
                        (
                            "A new unrecoverable denial equal to 2 percent of Base billings "
                            "is $18,500. If settlements and other expenses remain unchanged "
                            "and this loss was not already budgeted, owner profit falls "
                            "from $166,500 to $148,000. Moving $10,000 into a reserve account "
                            "only reallocates cash; recording the actual loss follows the "
                            "applicable accounting treatment."
                        ),
                    ),
                    field(
                        "Funded volume ceiling and release trigger",
                        "textarea",
                        (
                            "Set the maximum billings supportable by available working capital "
                            "under a declared settlement ratio and collection interval. "
                            "Hold operating cash and reserves aside first, and specify "
                            "what evidence permits the volume ceiling to increase."
                        ),
                        (
                            "With $115,000 liquidity, reserve $10,000 and hold $31,218.75 "
                            "for 45 days of Base operating expense. The remaining $73,781.25 "
                            "funds settlements. Dividing by 0.55 and 1.5 months supports "
                            "$89,431.82 monthly billings under this fixed-expense assumption. "
                            "The controller raises this ceiling only after reviewing actual "
                            "collection timing and incremental staffing costs."
                        ),
                    ),
                ],
                "completion_gate": (
                    "The controller verifies all three canonical reconciliations, approves "
                    "the contract-specific revenue presentation, and confirms drawable cash "
                    "covers the selected service-to-cash stress plus reserve. Proposed "
                    "volume remains below the documented funded ceiling."
                ),
            },
            {
                "worksheet_id": "ws-03",
                "number": 3,
                "title": "End-to-End Execution, Idempotent Ledger & QA Pre-Flight Sheet",
                "purpose": (
                    "Translate a service request into a verified assignment, documented "
                    "completion, collectible invoice, and reconciled carrier payment. Establish "
                    "durable identifiers, controlled state transitions, evidence retention, "
                    "and exception handling so retries, corrections, and dispatch outages "
                    "cannot create duplicate services or unsupported claims."
                ),
                "chapter_ref": "Q7, Q8",
                "instructions": [
                    (
                        "Map the actual workflow from authorization intake through cash "
                        "application before configuring software. Name the owner of each "
                        "transition and specify the evidence required to advance, reverse, "
                        "or cancel a service without losing its history."
                    ),
                    (
                        "Create one durable business identifier for each authorized service "
                        "leg or courier movement. Attach source-system identifiers as "
                        "references, then define idempotency keys for assignment, evidence "
                        "ingestion, invoicing, and settlement rather than relying on timestamps alone."
                    ),
                    (
                        "Separate planned events from observed events in the ledger. "
                        "Preserve appointment times, actual GPS observations, barcode scans, "
                        "and corrections with their provenance; never manufacture a "
                        "missing event simply because the invoice requires a completed field."
                    ),
                    (
                        "Test normal completion, cancellation, duplicate delivery, failed "
                        "handoff, corrected billing, and partial payment in a nonproduction "
                        "environment. Verify both customer receivables and carrier payables "
                        "after each test, including the audit trail left by reversals."
                    ),
                    (
                        "Complete pre-flight checks before each shift and reconcile all "
                        "open exceptions before invoice release. When a safety, packaging, "
                        "authorization, or evidence defect remains unresolved, isolate "
                        "the affected service rather than blocking unrelated valid work."
                    ),
                ],
                "fields": [
                    field(
                        "Intake packet and minimum necessary data",
                        "textarea",
                        (
                            "Define mandatory intake fields for passenger and specimen lanes "
                            "separately. Identify which information dispatch genuinely needs, "
                            "how authorization is verified, and which sensitive details "
                            "should remain outside ordinary notifications and billing summaries."
                        ),
                        (
                            "Passenger intake records service ID, payer authorization, pickup "
                            "and destination, appointment time, mobility needs, and a controlled "
                            "contact channel. Courier intake records package ID, laboratory "
                            "instructions, destination, and deadline. A routine driver notification "
                            "contains a task reference and secure access link, not diagnosis "
                            "text or specimen results copied into an ordinary message."
                        ),
                    ),
                    field(
                        "Canonical service identifier and duplicate detection",
                        "textarea",
                        (
                            "Specify the business key that distinguishes legitimate repeated "
                            "appointments from duplicate requests. Explain how external "
                            "identifiers map to internal service records and how corrections "
                            "preserve identity without creating another payable movement."
                        ),
                        (
                            "Service SVC-004182 represents the outbound leg for authorization "
                            "AUTH-731 on the scheduled service date. The return leg receives "
                            "SVC-004183. Reimporting the same TPA row matches the source ID "
                            "and leg key instead of creating a third service. Changing "
                            "pickup time creates schedule revision 2 while preserving both "
                            "original service identifiers."
                        ),
                    ),
                    field(
                        "Lifecycle states and authorized transitions",
                        "textarea",
                        (
                            "List service states, transition owners, and evidence prerequisites. "
                            "Describe how cancellations, failed pickups, and corrections are "
                            "represented without marking an unperformed service completed "
                            "or deleting information needed for a later payer audit."
                        ),
                        (
                            "The lifecycle is requested, authorized, assigned, accepted, arrived, "
                            "completed, evidence-verified, invoiced, and collected. Dispatch owns "
                            "assignment; the carrier supplies arrival and completion events; "
                            "billing verifies evidence. A patient cancellation enters canceled "
                            "with reason and timestamp. Any contractual cancellation fee uses "
                            "its own charge code and never masquerades as a completed passenger leg."
                        ),
                    ),
                    field(
                        "Atomic ledger posting and retry behavior",
                        "textarea",
                        (
                            "Define how the ledger prevents duplicate financial events "
                            "when callbacks repeat or connections fail. Include uniqueness "
                            "constraints, transaction boundaries, payload comparison, and "
                            "the response to a repeated key carrying conflicting amounts."
                        ),
                        (
                            "The posting key is SVC-004182:carrier-settlement:v1, enforced by "
                            "a database unique constraint. One transaction records the event "
                            "and $27.50 payable; an outbox record schedules notification after "
                            "commit. Repeating the same payload returns the existing result. "
                            "Repeating the key with $30.00 raises a review exception; an "
                            "approved adjustment receives a new linked revision."
                        ),
                    ),
                    field(
                        "GPS verification and disputed mileage",
                        "textarea",
                        (
                            "Record which GPS observations substantiate pickup, drop-off, "
                            "and route distance. Define tolerances, outage handling, and "
                            "manual review requirements while distinguishing estimated "
                            "routing distance from observed evidence used in a claim."
                        ),
                        (
                            "Route planning predicts 12.4 miles; recorded travel is 13.1 miles "
                            "because of a documented road closure. The reviewer attaches "
                            "the GPS track and dispatch note, then applies the payer's "
                            "mileage rule. A missing pickup fix triggers review of permitted "
                            "alternative evidence, not insertion of an invented coordinate "
                            "or automatic substitution of planned mileage."
                        ),
                    ),
                    field(
                        "Barcode custody and specimen exception trail",
                        "textarea",
                        (
                            "Define required custody events, handler identifiers, package "
                            "condition checks, and temperature evidence where specified. "
                            "Describe how a damaged seal, missing scan, or out-of-range "
                            "reading is escalated without retroactively changing the original event."
                        ),
                        (
                            "Package LAB-8821 is scanned at laboratory release, carrier "
                            "acceptance, and receiving-bench handoff, with UTC timestamps "
                            "and handler IDs. A required temperature logger records an "
                            "excursion at 09:42. Dispatch preserves the reading and contacts "
                            "the laboratory supervisor; only the laboratory's designated "
                            "decision-maker determines specimen usability and any recollection requirement."
                        ),
                    ),
                    field(
                        "Invoice or 837P submission eligibility",
                        "textarea",
                        (
                            "Identify the payer-approved submission channel and required "
                            "claim fields. Explain when an 837P is appropriate, how "
                            "authorization and service evidence are matched, and how "
                            "acknowledgments differ from actual adjudication or payment."
                        ),
                        (
                            "The Medicaid intermediary requires its portal roster for this "
                            "contract, so billing does not generate an unsolicited 837P. "
                            "A different enrolled-provider contract uses the payer's 837P "
                            "companion guide, including its required codes and identifiers. "
                            "A 999 or 277CA response updates transmission or claim-status "
                            "tracking where applicable; neither is treated as cash received."
                        ),
                    ),
                    field(
                        "Carrier settlement and cash application",
                        "textarea",
                        (
                            "Describe how accepted service evidence generates a carrier "
                            "payable and how remittances are allocated against customer "
                            "receivables. Keep carrier payment terms independent of customer "
                            "collection unless the signed agreement explicitly provides otherwise."
                        ),
                        (
                            "One hundred accepted $50 legs create $5,000 customer billings "
                            "and $2,750 carrier payables. The customer remits $4,900 and "
                            "identifies two disputed $50 lines. Cash application closes "
                            "98 lines and leaves $100 open with dispute reasons. The "
                            "carrier's agreed settlement date remains unchanged; dispatch "
                            "does not silently deduct the customer dispute from its payment."
                        ),
                    ),
                    field(
                        "Pre-flight test matrix and acceptance evidence",
                        "textarea",
                        (
                            "List executable test cases covering duplicate events, "
                            "cancellations, billing corrections, missing evidence, and "
                            "partial payment. For each case, state expected service "
                            "counts, payable amounts, and the evidence retained by the reviewer."
                        ),
                        (
                            "Test PF-07 submits the same $50 service completion three times. "
                            "Expected output is one completed service, one $50 invoice line, "
                            "and one $27.50 payable. PF-08 cancels before dispatch and expects "
                            "zero completed-service charges. The reviewer stores test payloads, "
                            "ledger extracts, and observed results; any duplicate posting "
                            "blocks production use of that integration."
                        ),
                    ),
                    field(
                        "Outage operation and reconciliation recovery",
                        "textarea",
                        (
                            "Document the controlled fallback during dispatch or network "
                            "failure. Specify temporary identifiers, secure evidence "
                            "capture, escalation channels, and the reconciliation procedure "
                            "that prevents offline services from being invoiced twice after recovery."
                        ),
                        (
                            "During a 40-minute outage, the dispatcher uses an encrypted "
                            "offline roster containing only necessary service details. "
                            "Temporary event OFF-021 references SVC-004182 and records its "
                            "actual completion time. After recovery, reconciliation checks "
                            "existing events before import. The second reviewer confirms "
                            "that five offline completions produce five ledger events, "
                            "not five additional services."
                        ),
                    ),
                ],
                "completion_gate": (
                    "Operations and billing approve the event map, replay tests, evidence "
                    "rules, and outage reconciliation. Duplicate callbacks produce no "
                    "duplicate service, invoice, or settlement, and every released charge "
                    "links to its authorization and actual service evidence."
                ),
            },
            {
                "worksheet_id": "ws-04",
                "number": 4,
                "title": "Statutory, Licensing, Contract Addendum & Compliance Audit",
                "purpose": (
                    "Convert healthcare transport obligations into a lane-specific evidence "
                    "register with accountable owners. Verify Medicaid enrollment, passenger "
                    "transport authority, privacy safeguards, specimen handling, worker "
                    "classification, insurance, and contract allocation before accepting "
                    "services whose legal requirements differ by state, cargo, or payer."
                ),
                "chapter_ref": "Q5, Q9",
                "instructions": [
                    (
                        "Identify the operating states, payer programs, passenger assistance "
                        "levels, and shipment classifications before selecting requirements. "
                        "Use current primary authorities and payer manuals; a generic "
                        "NEMT checklist cannot establish permission to perform every "
                        "transport or specimen service."
                    ),
                    (
                        "Assign each obligation to the contracting entity, carrier, "
                        "laboratory, or dispatch company that actually performs the "
                        "regulated function. Collect supporting evidence and renewal "
                        "dates rather than relying solely on representations in "
                        "a subcontractor agreement."
                    ),
                    (
                        "Review the real working relationship with each contractor "
                        "against applicable federal and state tests. Examine scheduling "
                        "control, rate negotiation, equipment ownership, business "
                        "independence, and integration into operations before treating "
                        "a signed contractor agreement as sufficient."
                    ),
                    (
                        "Translate statutory and payer requirements into operational "
                        "controls that dispatchers can execute. Define what happens "
                        "when credentials expire, a package leaks, a privacy incident "
                        "occurs, or a driver cannot safely perform the assigned assistance."
                    ),
                    (
                        "Draft contract addenda around measurable responsibilities, "
                        "evidence access, incident reporting, payment disputes, and "
                        "service limits. Resolve conflicting clauses before signature, "
                        "and preserve the reviewed contract version alongside "
                        "the requirements and credential register."
                    ),
                ],
                "fields": [
                    field(
                        "Medicaid transportation and enrollment requirements",
                        "textarea",
                        (
                            "Identify the applicable state Medicaid transportation model, "
                            "provider enrollment requirements, and broker credentialing "
                            "conditions. Explain which organization submits claims and "
                            "which service records establish eligibility for payment "
                            "under the selected arrangement."
                        ),
                        (
                            "The register cites 42 CFR 431.53 and 440.170(a) for "
                            "Medicaid transportation requirements and 42 CFR 455.410 "
                            "for applicable provider enrollment. The state manual and "
                            "broker agreement determine this lane's enrollment and "
                            "documentation steps. Dispatch retains enrollment confirmation, "
                            "authorization references, eligible driver records, and required "
                            "trip evidence before releasing the first claim."
                        ),
                    ),
                    field(
                        "Passenger authority and interstate cargo scope",
                        "textarea",
                        (
                            "List state and local passenger-carrier permits, vehicle "
                            "requirements, and any relevant interstate operating authority. "
                            "Evaluate specimen freight brokerage separately from passenger "
                            "dispatch instead of assuming one registration covers "
                            "every business activity."
                        ),
                        (
                            "The launch scope is intrastate ambulatory transport, with "
                            "permit requirements verified against the selected state's "
                            "transportation agency and Medicaid program. A proposed "
                            "interstate specimen lane receives a separate applicability "
                            "review under 49 U.S.C. 13901 and 13904. If property-broker "
                            "registration applies, the file addresses financial security "
                            "under 49 CFR 387.307 before that lane begins."
                        ),
                    ),
                    field(
                        "HIPAA role mapping and business associate agreements",
                        "textarea",
                        (
                            "Map protected health information flows and determine each "
                            "party's role. Identify required business associate and "
                            "subcontractor agreements, permitted uses, access limits, "
                            "and incident obligations without assuming every courier "
                            "relationship has identical privacy treatment."
                        ),
                        (
                            "Dispatch stores identifiable trip schedules for a covered "
                            "provider, so the documented assessment requires a BAA "
                            "under 45 CFR 164.502(e) and 164.504(e). A cloud vendor "
                            "handling that information receives the appropriate subcontractor "
                            "agreement. The team separately assesses a sealed-package courier "
                            "arrangement; any conduit analysis is documented rather than "
                            "automatically extended to the scheduling database."
                        ),
                    ),
                    field(
                        "Security safeguards and breach response",
                        "textarea",
                        (
                            "Translate privacy and security duties into access controls, "
                            "device safeguards, incident ownership, and reporting clocks. "
                            "Distinguish contractual incident notices from statutory "
                            "breach notifications and document who evaluates whether "
                            "an incident meets the applicable definition."
                        ),
                        (
                            "The control register maps risk analysis and safeguards "
                            "to 45 CFR 164.308 and 164.312. A lost dispatch device "
                            "triggers immediate account suspension and a contractual "
                            "24-hour report. The privacy lead assesses breach status "
                            "under 164.402; business-associate notification under 164.410 "
                            "must occur without unreasonable delay and no later than "
                            "60 calendar days after discovery."
                        ),
                    ),
                    field(
                        "Worker classification and owner-operator evidence",
                        "textarea",
                        (
                            "Document the actual contractor relationship under applicable "
                            "labor, tax, and state tests. Explain how essential safety "
                            "and payer requirements differ from managerial control, "
                            "and identify when an employee staffing model is required."
                        ),
                        (
                            "The California review addresses Labor Code sections 2775 "
                            "and 2776, including whether a business-to-business exception "
                            "actually applies and what test follows. Carrier evidence "
                            "includes separate customers, negotiated rates, equipment "
                            "ownership, and independent operations. Dispatch does not "
                            "assume a 1099 form resolves classification; fixed shifts "
                            "and extensive control trigger a documented employment-model review."
                        ),
                    ),
                    field(
                        "Bloodborne pathogen exposure controls",
                        "textarea",
                        (
                            "Assess occupational exposure by role and document applicable "
                            "employee protections, training, equipment, and incident "
                            "response. State who maintains the exposure-control plan "
                            "and what a courier does when a package "
                            "shows leakage or external contamination."
                        ),
                        (
                            "For employees with reasonably anticipated occupational "
                            "exposure, the employer implements 29 CFR 1910.1030, "
                            "including an exposure-control plan, appropriate training, "
                            "protective equipment, and required vaccination and "
                            "post-exposure arrangements. A courier encountering leakage "
                            "isolates the area and contacts the designated responder; "
                            "the courier does not open primary containers or perform "
                            "untrained cleanup."
                        ),
                    ),
                    field(
                        "Specimen classification and transport packaging",
                        "textarea",
                        (
                            "Record the shipper's specimen classification, packaging "
                            "standard, marking requirements, mode of transport, and "
                            "training assessment. Distinguish Category B shipments "
                            "from Category A and exempt specimens before applying "
                            "a standard courier workflow."
                        ),
                        (
                            "The laboratory classifies a qualifying Category B shipment "
                            "under 49 CFR 173.134 and prepares packaging and marks "
                            "under 173.199, including UN3373 where required. Dispatch "
                            "accepts only the reviewed packaging configuration. Category "
                            "A material is excluded from this lane and routed for "
                            "a separate 173.196 assessment; air shipments require "
                            "additional mode-specific review."
                        ),
                    ),
                    field(
                        "Laboratory instructions and specimen acceptance",
                        "textarea",
                        (
                            "Obtain the receiving laboratory's written collection, "
                            "transport, preservation, and rejection instructions. "
                            "Explain how applicable CLIA requirements influence "
                            "handoff evidence without implying that the dispatch "
                            "company makes laboratory testing or clinical acceptance decisions."
                        ),
                        (
                            "For the applicable nonwaived laboratory, the file references "
                            "42 CFR 493.1242 and its written specimen-handling procedures. "
                            "The route profile specifies the laboratory's validated "
                            "temperature range and maximum transit interval. A late "
                            "delivery receives an exception record; the laboratory "
                            "decides whether to accept, reject, or request recollection, "
                            "and dispatch preserves that decision."
                        ),
                    ),
                    field(
                        "Screening insurance and credential renewal",
                        "textarea",
                        (
                            "Specify screening sources, payer-required review intervals, "
                            "insurance verification, and credential-expiration behavior. "
                            "Distinguish statutory duties from additional contract "
                            "requirements and identify the evidence needed to "
                            "resolve a possible exclusion-list match."
                        ),
                        (
                            "The register maps applicable screening obligations under "
                            "42 CFR 455.436 and the payer's monthly exclusion-check "
                            "requirement. Staff review OIG LEIE results and applicable "
                            "state lists, resolving possible matches with reliable "
                            "identifiers. Insurance is verified with the producer. "
                            "Expired required coverage removes the affected carrier "
                            "from assignment until replacement evidence is independently confirmed."
                        ),
                    ),
                    field(
                        "Contract addendum and evidence retention schedule",
                        "textarea",
                        (
                            "Draft concrete clauses covering service limits, records "
                            "access, disputed charges, incident escalation, and retention. "
                            "Identify which retention period applies to each record "
                            "class instead of assigning every operational record "
                            "the same statutory deadline."
                        ),
                        (
                            "The addendum requires authorization references, unaltered "
                            "trip evidence, prompt incident reporting, and payment "
                            "of undisputed lines. The schedule retains HIPAA-required "
                            "policies and related documentation under 45 CFR 164.316(b)(2)(i) "
                            "for six years. Trip and claim records follow the "
                            "applicable state and payer periods, with longer preservation "
                            "when a dispute or legal hold applies."
                        ),
                    ),
                ],
                "completion_gate": (
                    "The responsible operations, privacy, and contract reviewers verify "
                    "lane-specific authority, enrollment, credential evidence, packaging "
                    "responsibilities, worker classification, and signed addenda. Any "
                    "expired credential or unresolved service-scope restriction prevents "
                    "assignment of the affected work."
                ),
            },
            {
                "worksheet_id": "ws-05",
                "number": 5,
                "title": "Automation Pipeline, Acquisition Flywheel & Risk Fallback Tracker",
                "purpose": (
                    "Build a controlled acquisition and automation system that increases "
                    "accepted, collectible service volume rather than raw requests. Connect "
                    "dispatch, evidence, billing, and collections with measurable exception "
                    "handling, then pair every automation dependency with a secure "
                    "fallback and accountable operator."
                ),
                "chapter_ref": "Q6, Q10",
                "instructions": [
                    (
                        "Choose automation only after defining its input, output, "
                        "permissions, and failure behavior. Validate the contracted "
                        "capabilities of RouteGenie or MediRoutes in the selected "
                        "edition rather than assuming every integration, export, "
                        "or routing feature is included."
                    ),
                    (
                        "Build acquisition lists around facilities and intermediaries "
                        "with identifiable route problems. Record the decision-maker, "
                        "service gap, estimated authorized volume, and payment model; "
                        "avoid using patient-level information to enrich prospect "
                        "lists or ordinary marketing systems."
                    ),
                    (
                        "Instrument the path from signed agreement to accepted "
                        "service and collected cash. Track authorization failures, "
                        "assignment rejection, missing scans, invoice rejection, "
                        "and payment delay separately so apparently growing "
                        "booking volume cannot conceal deteriorating economics."
                    ),
                    (
                        "Require every integration to support replay protection, "
                        "bounded retries, alert ownership, and reconciliation. "
                        "Route conflicting events to human review, and test "
                        "the fallback procedure before the first live "
                        "STAT assignment depends on automated delivery."
                    ),
                    (
                        "Prioritize improvements using recovered contribution and "
                        "documented operator time rather than attractive dashboards. "
                        "Reinvest only after evidence quality, service performance, "
                        "and cash collections remain stable across the "
                        "pilot's agreed observation period."
                    ),
                ],
                "fields": [
                    field(
                        "Target account thesis and service trigger",
                        "textarea",
                        (
                            "Define the ideal buyer, service problem, geographic "
                            "density, and observable buying trigger. Explain how "
                            "the opportunity matches available carrier capacity "
                            "and why its payment structure fits the "
                            "current working-capital ceiling."
                        ),
                        (
                            "The target list contains 20 dialysis facilities within "
                            "two adjacent service clusters and ten laboratories "
                            "with scheduled afternoon transfers. Outreach asks "
                            "about missed pickups and backup coverage, not patient "
                            "identities. A qualified opportunity needs recurring "
                            "authorized demand, a named payer, and a payment "
                            "cycle supportable within the $115,000 liquidity plan."
                        ),
                    ),
                    field(
                        "Prospecting funnel and conversion economics",
                        "textarea",
                        (
                            "Specify weekly account outreach, discovery, proposal, "
                            "and signed-pilot targets. Calculate acquisition cost "
                            "from actual sales expense and signed customers, "
                            "then compare that cost with retained "
                            "contribution rather than gross contract value."
                        ),
                        (
                            "A four-week campaign contacts 40 organizations, produces "
                            "12 discovery calls, six qualified proposals, and two "
                            "signed pilots. Sales expense is $3,000, so acquisition "
                            "cost is $1,500 per signed customer. Each pilot forecasts "
                            "$5,000 monthly billings and $2,250 retained contribution; "
                            "contribution payback is approximately 0.67 months before "
                            "incremental overhead, onboarding costs, and collection delay."
                        ),
                    ),
                    field(
                        "Dispatch platform selection and configuration",
                        "textarea",
                        (
                            "Compare RouteGenie and MediRoutes against concrete "
                            "workflow requirements, supported interfaces, access "
                            "controls, and export needs. Record the selected "
                            "configuration and evidence of a successful "
                            "test instead of assuming vendor capabilities."
                        ),
                        (
                            "The pilot evaluation requires recurring-trip import, "
                            "GPS event export, role-based access, and a reviewable "
                            "assignment history. The team requests a vendor "
                            "demonstration using ten synthetic trips and confirms "
                            "which features the quoted edition includes. Selection "
                            "remains conditional on a successful export and "
                            "duplicate-import test, not a sales presentation "
                            "or an undocumented integration promise."
                        ),
                    ),
                    field(
                        "Integration contract and event delivery controls",
                        "textarea",
                        (
                            "Define the source event, destination, schema version, "
                            "authentication method, retry policy, and reconciliation "
                            "key for each connection. Explain how unsupported "
                            "interfaces or missing vendor guarantees affect "
                            "the chosen implementation."
                        ),
                        (
                            "Where a documented vendor interface supports it, "
                            "completion events enter a versioned ingestion endpoint "
                            "using scoped credentials and event IDs. Otherwise, "
                            "a controlled export is reconciled by service ID. "
                            "Retries back off at one, five, and fifteen minutes; "
                            "unresolved events enter a review queue. The operator "
                            "does not invent an undocumented endpoint."
                        ),
                    ),
                    field(
                        "Claims scrubbing and accounts receivable automation",
                        "textarea",
                        (
                            "Define deterministic checks for authorized billing "
                            "channels and aging alerts. Distinguish transmission "
                            "errors, payer rejection, adjudication, and unpaid "
                            "accepted invoices so automation assigns each "
                            "exception to the correct resolution owner."
                        ),
                        (
                            "The scrubber checks authorization, service date, "
                            "required identifiers, duplicate service keys, and "
                            "payer-specific fields before the approved submission. "
                            "AR alerts begin at the contractual due date, "
                            "then escalate seven and fourteen days later. "
                            "A rejected transaction goes to billing correction; "
                            "an accepted but unpaid invoice goes to collections "
                            "with its evidence packet attached."
                        ),
                    ),
                    field(
                        "Specimen scanning automation and alert thresholds",
                        "textarea",
                        (
                            "Define expected barcode events, missing-event timers, "
                            "temperature integration where required, and escalation "
                            "ownership. Explain how an alert reaches a "
                            "human and what evidence confirms that "
                            "the receiving laboratory was contacted."
                        ),
                        (
                            "A STAT pickup accepted at 09:00 must show "
                            "carrier custody by 09:30 under the route contract. "
                            "At 09:20, a missing custody scan alerts dispatch; "
                            "at 09:25, dispatch calls the carrier and laboratory. "
                            "The exception record stores contacts, response times, "
                            "and recovery decisions. A delivered notification alone "
                            "does not prove the specimen reached the laboratory."
                        ),
                    ),
                    field(
                        "Least-privilege access and controlled data exports",
                        "textarea",
                        (
                            "Specify access boundaries for sales, dispatch, "
                            "billing, carriers, and analysts. Identify which "
                            "data can enter external services and how "
                            "permissions, contractual safeguards, and export "
                            "logging are verified before transmission."
                        ),
                        (
                            "Sales sees facility contacts and aggregate lane "
                            "volume, not passenger schedules. Carriers see only "
                            "assigned service details. Billing sees payer "
                            "identifiers and required evidence. Analytics exports "
                            "use service tokens and aggregated metrics where "
                            "possible. A new external service receives sensitive "
                            "data only after documented purpose, access, and "
                            "applicable contractual safeguards are verified."
                        ),
                    ),
                    field(
                        "Risk register and actionable fallback ownership",
                        "textarea",
                        (
                            "Record each high-impact dependency, observable "
                            "failure signal, response deadline, fallback owner, "
                            "and recovery evidence. Include carrier failure, "
                            "platform outage, credential expiry, and delayed "
                            "payer collections rather than limiting "
                            "the register to software problems."
                        ),
                        (
                            "If a primary carrier misses acceptance for a "
                            "STAT request within five minutes, dispatch contacts "
                            "the qualified backup and advises the laboratory "
                            "of the updated estimate. If neither can meet "
                            "the requirement, the service is explicitly "
                            "declined or renegotiated. The log records "
                            "contact attempts and the laboratory's response "
                            "instead of leaving the request silently assigned."
                        ),
                    ),
                    field(
                        "Referral flywheel and healthcare remuneration boundaries",
                        "textarea",
                        (
                            "Design a referral process based on demonstrated "
                            "service quality and aggregate performance evidence. "
                            "Identify who approves incentives or commercial "
                            "arrangements and explain how the process "
                            "avoids paying for patient referrals "
                            "or steering federally reimbursed business."
                        ),
                        (
                            "After 30 verified pilot days, the account "
                            "manager offers an aggregate on-time report "
                            "and requests an introduction to another "
                            "operations manager. No patient list or "
                            "per-patient referral payment changes hands. "
                            "Any proposed remuneration arrangement receives "
                            "review for 42 U.S.C. 1320a-7b(b) and "
                            "applicable state restrictions before an offer "
                            "is made or funds are committed."
                        ),
                    ),
                    field(
                        "Automation return and exception burden",
                        "textarea",
                        (
                            "Calculate the measurable value of an "
                            "automation using operator time, avoided "
                            "duplicate payments, and recovered collectible "
                            "charges. Subtract subscription and maintenance "
                            "costs, and specify when excessive "
                            "exceptions require redesign or rollback."
                        ),
                        (
                            "A reconciliation tool saves 20 monthly "
                            "hours at $30 per hour and prevents "
                            "$300 of documented duplicate settlement "
                            "losses, creating $900 monthly benefit. "
                            "Subscription and maintenance cost $350, "
                            "leaving $550 incremental benefit. If "
                            "exception handling consumes another ten "
                            "hours, benefit falls to $250; the "
                            "owner rechecks actual time logs "
                            "before expanding deployment."
                        ),
                    ),
                ],
                "completion_gate": (
                    "Each live automation has a verified interface, least-privilege "
                    "access, duplicate protection, reconciliation evidence, and tested "
                    "human fallback. Acquisition targets are tied to authorized, "
                    "fundable service volume, and improvement claims use observed "
                    "contribution or labor savings."
                ),
            },
            {
                "worksheet_id": "ws-06",
                "number": 6,
                "title": "30-Day Launch Sprint, Pod KPI Scorecard & Exit-Readiness Ledger",
                "purpose": (
                    "Turn the operating design into a bounded 30-day readiness sprint "
                    "with measurable deliverables, realistic deal timing, and a documented "
                    "handoff. Track service quality, liquidity, owner dependence, and "
                    "transferable records so growth decisions and eventual buyer diligence "
                    "rest on verified operating evidence."
                ),
                "chapter_ref": "Q11, Q12",
                "instructions": [
                    (
                        "Treat the first 30 days as a readiness "
                        "and qualification sprint, not an assumed "
                        "revenue deadline. Preserve the canonical "
                        "two-to-five-month first-deal expectation, and "
                        "separate activities possible before contracting "
                        "from services that require completed "
                        "credentials and signed agreements."
                    ),
                    (
                        "Assign every sprint deliverable to a named "
                        "role with a due date and observable "
                        "acceptance evidence. Limit simultaneous priorities "
                        "so the core pod can complete "
                        "credential review, system tests, and "
                        "customer qualification without relying on "
                        "unrecorded owner overtime."
                    ),
                    (
                        "Publish a weekly scorecard with explicit "
                        "numerators, denominators, observation periods, "
                        "and exclusions. Review service quality "
                        "beside retained contribution and cash "
                        "so increased volume does not hide "
                        "late pickups, unpaid invoices, or "
                        "expanding settlement obligations."
                    ),
                    (
                        "Build the diligence register while operating "
                        "rather than reconstructing it during a "
                        "sale process. Preserve contract versions, "
                        "credential histories, accounting reconciliations, "
                        "incident dispositions, and assignment restrictions "
                        "with controlled access and appropriate "
                        "record-retention rules."
                    ),
                    (
                        "At day 30, compare completed evidence "
                        "with the readiness criteria and "
                        "choose a limited pilot, further "
                        "remediation, or continued prospecting. "
                        "Document the decision without booking "
                        "unsigned pipeline as revenue or "
                        "treating a simulated workflow test "
                        "as a completed customer service."
                    ),
                ],
                "fields": [
                    field(
                        "Days one through seven underwriting deliverables",
                        "textarea",
                        (
                            "Define first-week outcomes for "
                            "counterparty selection, service scope, "
                            "capital planning, and regulatory "
                            "research. State the evidence "
                            "required for completion and "
                            "identify any activity that "
                            "must wait for a signed "
                            "contract or verified credential."
                        ),
                        (
                            "By day 7, the commercial lead "
                            "completes five buyer interviews and "
                            "two draft lane models. Operations "
                            "documents state-specific service requirements "
                            "and verifies two carrier candidates. "
                            "The controller completes all three "
                            "canonical scenario reconciliations and "
                            "a 60-day cash stress. No "
                            "passenger or specimen movement "
                            "is represented as authorized "
                            "merely because these documents exist."
                        ),
                    ),
                    field(
                        "Days eight through fourteen control build",
                        "textarea",
                        (
                            "Specify second-week deliverables for "
                            "contract exhibits, evidence capture, "
                            "ledger design, and privacy "
                            "controls. Identify the reviewer "
                            "for each artifact and "
                            "the test that demonstrates "
                            "the document translates into "
                            "a working operating control."
                        ),
                        (
                            "By day 14, operations drafts "
                            "the service-level exhibit and "
                            "backup escalation tree. Billing "
                            "implements service keys and "
                            "settlement replay tests using "
                            "synthetic records. The privacy "
                            "lead maps data flows and "
                            "required agreements. A reviewer "
                            "must trace one test service "
                            "from intake through a "
                            "$50 invoice and $27.50 payable."
                        ),
                    ),
                    field(
                        "Days fifteen through twenty-one rehearsal",
                        "textarea",
                        (
                            "Plan a realistic rehearsal "
                            "covering normal services and "
                            "exceptions without exposing "
                            "unnecessary patient information. "
                            "Define the expected evidence, "
                            "failure criteria, and remediation "
                            "owner for missed pickups, "
                            "duplicate events, and platform outages."
                        ),
                        (
                            "The rehearsal processes 20 "
                            "synthetic passenger legs and "
                            "five sealed training packages. "
                            "It includes two cancellations, "
                            "three duplicate callbacks, a "
                            "missing custody scan, and "
                            "a 30-minute platform outage. "
                            "Expected results contain no "
                            "duplicate payable and no "
                            "fabricated completion. Each "
                            "defect receives an owner "
                            "and a demonstrated retest "
                            "before live acceptance."
                        ),
                    ),
                    field(
                        "Days twenty-two through thirty decision",
                        "textarea",
                        (
                            "Define the day-30 decision "
                            "packet and distinguish a "
                            "ready operating system from "
                            "a signed customer launch. "
                            "State which evidence permits "
                            "a limited pilot and "
                            "how remaining sales work "
                            "continues beyond the sprint."
                        ),
                        (
                            "The day-30 packet contains "
                            "tested workflows, verified "
                            "carrier credentials, a funded "
                            "volume ceiling, and the "
                            "current contract negotiation log. "
                            "If no agreement is signed, "
                            "the decision is readiness "
                            "complete and prospecting continues. "
                            "The two-to-five-month first-deal "
                            "expectation remains intact. "
                            "Live work begins only "
                            "when the specific lane's "
                            "commercial and operating requirements "
                            "are satisfied."
                        ),
                    ),
                    field(
                        "Core pod staffing and coverage design",
                        "textarea",
                        (
                            "Allocate responsibilities across "
                            "the canonical core staffing "
                            "levels and identify backup "
                            "coverage. Distinguish core "
                            "contractors from external "
                            "carrier businesses, and "
                            "explain how outsourced "
                            "delivery capacity affects "
                            "labor dependence and diligence."
                        ),
                        (
                            "Base staffing assigns two "
                            "full-time roles to operations "
                            "and account/billing management, "
                            "with two contracted support "
                            "roles for qualified overflow "
                            "and bookkeeping. Scaled staffing "
                            "is three full-time plus "
                            "three contracted core roles. "
                            "Carrier businesses remain "
                            "separately tracked within "
                            "settlement economics; the "
                            "staffing label does not "
                            "claim that four or six "
                            "people perform the entire "
                            "transport network's labor."
                        ),
                    ),
                    field(
                        "Service quality KPI definitions and thresholds",
                        "textarea",
                        (
                            "Define on-time pickup, completed "
                            "service, evidence completeness, "
                            "and STAT exception rates "
                            "with explicit denominators. "
                            "Explain cancellations and "
                            "customer-approved rescheduling, "
                            "then identify the "
                            "corrective action triggered "
                            "by each breached threshold."
                        ),
                        (
                            "Of 200 accepted passenger "
                            "legs, ten cancel before "
                            "dispatch and 190 complete. "
                            "Of those completed legs, "
                            "184 meet the agreed "
                            "pickup window: 96.84 percent. "
                            "Evidence is complete for "
                            "188 of 190, or "
                            "98.95 percent. A 98 "
                            "percent pickup target is "
                            "missed, triggering lane "
                            "review rather than "
                            "reclassifying late trips "
                            "as customer cancellations."
                        ),
                    ),
                    field(
                        "Cash and contribution KPI scorecard",
                        "textarea",
                        (
                            "Define retained share, aged "
                            "receivables, settlement coverage, "
                            "and available headroom using "
                            "consistent periods. Show "
                            "actual results beside "
                            "the canonical target "
                            "and explain deviations "
                            "without rewriting the "
                            "original scenario assumptions."
                        ),
                        (
                            "A month produces $77,083.33 "
                            "billings and $42,395.83 "
                            "settlements, approximately matching "
                            "the Base 45 percent "
                            "retained share after rounding. "
                            "Treasury tracks the "
                            "$104,812.50 45-day funding "
                            "requirement against $115,000 "
                            "available liquidity. Actual "
                            "collection aging is shown "
                            "by invoice due date; "
                            "a rising overdue balance "
                            "triggers a revised cash "
                            "forecast before additional "
                            "standing orders are accepted."
                        ),
                    ),
                    field(
                        "Owner independence and handoff rehearsal",
                        "textarea",
                        (
                            "Identify decisions still "
                            "requiring the owner and "
                            "convert recurring ones "
                            "into delegated procedures. "
                            "Test a bounded absence "
                            "with emergency escalation "
                            "available, recording unresolved "
                            "exceptions rather than "
                            "claiming independence from "
                            "a written manual alone."
                        ),
                        (
                            "During a two-day handoff "
                            "rehearsal, the operations "
                            "lead handles scheduling, "
                            "carrier substitutions, and "
                            "routine service exceptions. "
                            "The controller authorizes "
                            "settlements within documented "
                            "limits. Three owner "
                            "interruptions are logged: "
                            "a rate concession, "
                            "a disputed specimen "
                            "handoff, and a credit "
                            "draw. Procedures are "
                            "updated and retested "
                            "before describing the "
                            "business as owner-independent."
                        ),
                    ),
                    field(
                        "Exit-readiness evidence and transfer restrictions",
                        "textarea",
                        (
                            "Inventory records a "
                            "buyer would need "
                            "to verify earnings, "
                            "service quality, contract "
                            "durability, and operational "
                            "transferability. Identify "
                            "assignment restrictions "
                            "and access controls "
                            "before sharing documents "
                            "outside the operating team."
                        ),
                        (
                            "The diligence register "
                            "contains monthly reconciliations, "
                            "customer concentration, signed "
                            "contracts, carrier coverage, "
                            "credential histories, incident "
                            "dispositions, and system "
                            "exports. Two customer "
                            "agreements require written "
                            "assignment consent, so "
                            "their transfer is "
                            "not assumed. Buyer "
                            "materials use redacted "
                            "or aggregate evidence "
                            "first; identifiable health "
                            "information is not "
                            "uploaded to an "
                            "ordinary deal folder."
                        ),
                    ),
                    field(
                        "Day-thirty decision and ninety-day operating mandate",
                        "textarea",
                        (
                            "Record completed deliverables, "
                            "open defects, the "
                            "next operating objective, "
                            "and conditions for "
                            "expansion. Preserve the "
                            "canonical scenario targets "
                            "while distinguishing "
                            "forecast economics from "
                            "verified customer results "
                            "and collected cash."
                        ),
                        (
                            "Decision: continue qualification "
                            "until the first contract "
                            "and carrier coverage "
                            "are fully documented, "
                            "then run a capped "
                            "pilot within available "
                            "float. The next "
                            "90 days prioritize "
                            "collected invoices, verified "
                            "on-time service, and "
                            "repeatable reconciliation. "
                            "The Base $166,500 "
                            "annual owner profit "
                            "remains a scenario "
                            "target, not an "
                            "earned result or "
                            "a substitute for "
                            "observed operating records."
                        ),
                    ),
                ],
                "completion_gate": (
                    "The sprint owner signs a day-30 decision supported by completed "
                    "artifacts and actual test results. Live expansion requires the "
                    "specific lane's credentials, executed agreements, funded float, "
                    "tested fallback, and measurable service performance; unsigned "
                    "pipeline and simulated activity remain separately labeled."
                ),
            },
        ],
    }
