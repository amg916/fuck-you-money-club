from __future__ import annotations


def build_volume_028_workbook() -> dict:
    def field(name: str, input_type: str, prompt: str, example: str) -> dict:
        return {
            "name": name,
            "type": input_type,
            "prompt": prompt,
            "example": example,
        }

    return {
        "workbook_id": "wb-028-commercial-cleaning-contracts",
        "volume_id": "vol-028-commercial-cleaning-contracts",
        "title": "Commercial Cleaning Contracts — Operator Companion Workbook",
        "subtitle": (
            "6 Printable Operator Worksheets for Recurring Commercial and Medical "
            "Janitorial Contracts: Production-Rate Bidding, Crew Economics, Chemical "
            "Safety, Supervisor Pods, Working Capital, and Transferable Contract Value"
        ),
        "worksheets": [
            {
                "worksheet_id": "ws-01",
                "number": 1,
                "title": "Opportunity, Vertical Underwriting and Counterparty Qualification",
                "purpose": (
                    "Select recurring cleaning opportunities that fit verified crew capacity, "
                    "payment resources, and site-specific safety requirements. Convert a "
                    "walkthrough into measurable scope, distinguish commercial offices from "
                    "medical environments, and qualify the actual purchasing entity before "
                    "committing a price or mobilization date."
                ),
                "chapter_ref": "Q1, Q2, Q6",
                "instructions": [
                    (
                        "Choose one service territory and one initial facility segment. "
                        "Measure driving time during the actual evening shift, identify "
                        "supervisor coverage, and exclude sites whose access restrictions "
                        "or specialist procedures exceed the team's documented capability."
                    ),
                    (
                        "Conduct a room-by-room walkthrough with the facilities contact. "
                        "Record cleanable area, flooring, fixture counts, waste streams, "
                        "occupancy, cleaning frequencies, and access windows; building "
                        "marketing area alone cannot support a defensible labor estimate."
                    ),
                    (
                        "Translate observed tasks into paid minutes using licensed ISSA "
                        "reference material and your own timed trials. Record the reference "
                        "edition and conditions, then add setup, travel, interruptions, "
                        "and supervision rather than hiding them inside productivity assumptions."
                    ),
                    (
                        "Verify the contracting entity, signer authority, invoice destination, "
                        "purchase-order requirements, and payment history through authorized "
                        "business references. Obtain written confirmation of scope ownership "
                        "when a property manager purchases services for a separate building owner."
                    ),
                    (
                        "Compare the opportunity against concentration limits and the "
                        "canonical portfolio scenarios. Keep contract revenue separate from "
                        "client property value or medical collections, and reject attractive "
                        "headline pricing when staffing, credit, or scope assumptions remain unsupported."
                    ),
                ],
                "fields": [
                    field(
                        "Target vertical and territory",
                        "textarea",
                        (
                            "Define the facility category, practical service radius, purchasing "
                            "role, and excluded work. Explain why available supervisors, "
                            "equipment, and training can support this segment without relying "
                            "on future hires."
                        ),
                        (
                            "Target professional offices within a 25-minute evening drive "
                            "of the equipment depot. Pursue facilities managers controlling "
                            "10,000 to 40,000 cleanable square feet. Exclude operating rooms, "
                            "hazardous spill response, and exterior high-access windows. "
                            "One supervisor can inspect two nearby sites during a scheduled "
                            "four-hour coverage window."
                        ),
                    ),
                    field(
                        "Measured facility scope",
                        "textarea",
                        (
                            "Record cleanable square footage by surface, restroom fixtures, "
                            "touchpoints, occupancy, and service frequency. Identify areas "
                            "excluded from routine cleaning and state who verified the "
                            "measurements during the walkthrough."
                        ),
                        (
                            "The facilities manager verified 20,000 cleanable square feet: "
                            "12,000 carpet, 6,000 resilient flooring, and 2,000 restroom "
                            "and breakroom surfaces. Service occurs five nights weekly, "
                            "using a 260-visit annual planning assumption. The scope includes "
                            "12 restroom fixtures and excludes tenant storage rooms, "
                            "exterior glass, and periodic floor restoration."
                        ),
                    ),
                    field(
                        "Medical environment boundary",
                        "textarea",
                        (
                            "Identify whether the site contains patient-care areas, blood "
                            "exposure tasks, sharps, isolation rooms, or protected records. "
                            "Separate ordinary janitorial duties from procedures requiring "
                            "additional training, equipment, and explicit contractual responsibility."
                        ),
                        (
                            "A proposed outpatient clinic includes six examination rooms "
                            "and a reception area. Clinic staff retain sharps handling "
                            "and instrument processing. Before pricing examination-room "
                            "cleaning, the supervisor documents exposure tasks, disinfectant "
                            "requirements, and the clinic's written protocol. The office "
                            "bid remains separate until those additional labor minutes "
                            "and controls are measured."
                        ),
                    ),
                    field(
                        "Production-rate evidence",
                        "textarea",
                        (
                            "Document task quantities, measured production rates, equipment "
                            "assumptions, and source dates. Use ISSA material as a starting "
                            "reference, then explain adjustments supported by observed "
                            "furniture density, soil load, and access conditions."
                        ),
                        (
                            "A timed trial assigns 1.50 hours to carpet care, 1.00 "
                            "to hard floors, 1.00 to restrooms, and 0.50 to waste "
                            "and touchpoints per visit. Total direct cleaning is 4.00 "
                            "hours. Record the licensed ISSA reference edition separately; "
                            "these are site trial results, not universal published rates."
                        ),
                    ),
                    field(
                        "Counterparty and signer authority",
                        "textarea",
                        (
                            "Identify the legal purchaser, service beneficiary, authorized "
                            "signer, and accounts-payable contact. Describe the evidence "
                            "connecting the signer to the purchaser and resolve whether "
                            "a property manager acts as agent."
                        ),
                        (
                            "Example purchaser Harbor Office Holdings LLC owns the serviced "
                            "building. Its property manager signs only after providing "
                            "written agency authority naming that entity. Accounts payable "
                            "confirms the invoice email and purchase-order number. The "
                            "contract identifies Harbor as payment obligor rather than "
                            "assuming the management company's brand establishes credit."
                        ),
                    ),
                    field(
                        "Payment terms and credit exposure",
                        "textarea",
                        (
                            "Specify invoice timing, contractual due dates, dispute procedures, "
                            "reference checks, and maximum unpaid exposure. Connect the "
                            "payment cycle to payroll funding rather than treating booked "
                            "revenue as immediately available cash."
                        ),
                        (
                            "The proposal bills $4,000 monthly in arrears with payment "
                            "due 30 days after a valid invoice. Two authorized trade "
                            "references report payments within 35 days. Finance models "
                            "roughly 60 days from initial service to first cash and "
                            "requires $10,200 of dedicated operating coverage before mobilization."
                        ),
                    ),
                    field(
                        "Access and service continuity",
                        "textarea",
                        (
                            "List permitted service windows, badge issuance, alarm procedures, "
                            "storage rights, water access, and after-hours contacts. Assign "
                            "responsibility for lost access and explain how downtime "
                            "changes the labor estimate or service calendar."
                        ),
                        (
                            "Cleaning runs from 6:00 p.m. to 10:00 p.m., Monday "
                            "through Friday. The customer provides two named badges, "
                            "a locked chemical cabinet, and a working janitor sink. "
                            "If access fails, the crew calls the facilities contact "
                            "and records waiting time; rescheduling and charge treatment "
                            "follow the signed access clause."
                        ),
                    ),
                    field(
                        "Scope exclusions and change triggers",
                        "textarea",
                        (
                            "State included outcomes and measurable triggers for repricing. "
                            "Address increased occupancy, added square footage, unusual soil, "
                            "periodic services, and emergency requests so supervisors can "
                            "distinguish defects from newly requested work."
                        ),
                        (
                            "The $4,000 monthly scope covers the measured office and "
                            "listed tasks. Carpet extraction, floor stripping, construction "
                            "dust, and emergency spills require separate written pricing. "
                            "An added 2,000 square feet triggers a new task-time "
                            "study. Occupancy changes prompt review when documented "
                            "service minutes increase for two consecutive weeks."
                        ),
                    ),
                    field(
                        "Concentration and renewal exposure",
                        "textarea",
                        (
                            "Calculate the proposed customer's share of recognized annual "
                            "revenue and identify correlated building ownership or management "
                            "relationships. Record renewal dates and a concrete mitigation "
                            "when several contracts could terminate together."
                        ),
                        (
                            "A $48,000 annual contract represents 6.62% of the "
                            "$725,000 Base revenue benchmark. Three buildings under "
                            "the same payment obligor would total $144,000, or "
                            "19.86%. Management reviews shared ownership before adding "
                            "a fourth building and schedules prospecting outside that "
                            "group rather than treating each address as independent diversification."
                        ),
                    ),
                    field(
                        "Opportunity decision and scorecard anchor",
                        "textarea",
                        (
                            "Record the pursuit decision, evidence still required, and "
                            "named decision owner. Anchor expectations to the candidate's "
                            "actual rank, score, revenue basis, and staffing dependence "
                            "instead of presenting cleaning as passive income."
                        ),
                        (
                            "Proceed to a paid site trial, subject to verified access "
                            "and funding. Commercial Cleaning Contracts is Candidate "
                            "#10, pipeline rank #23 of 29, with a 82/100 "
                            "Money-to-Manpower Score. Its component scores are 21, "
                            "12, 6, 11, and 6 respectively; growth requires "
                            "additional paid crew hours, not software alone."
                        ),
                    ),
                ],
                "completion_gate": (
                    "The operations lead and finance owner sign the measured scope, "
                    "counterparty record, capacity estimate, and cash requirement. Do not "
                    "issue a binding start date while purchasing authority, medical-task "
                    "boundaries, access, or payroll coverage remains unresolved."
                ),
            },
            {
                "worksheet_id": "ws-02",
                "number": 2,
                "title": "Unit Economics, Rework Reserve and Working-Capital Float",
                "purpose": (
                    "Build an auditable contract contribution model from paid hours, "
                    "not square footage alone. Quantify rework, collections timing, "
                    "and overhead allocations while preserving the canonical Conservative, "
                    "Base, and Scaled portfolio outcomes as benchmarks requiring a "
                    "separate executable staffing and cost plan."
                ),
                "chapter_ref": "Q3, Q4",
                "instructions": [
                    (
                        "Enter annual service visits before calculating monthly averages. "
                        "Use the actual contract calendar for live bids, including "
                        "holidays and shutdowns; the worked example uses 260 visits "
                        "solely to keep its annual labor reconciliation explicit."
                    ),
                    (
                        "Build loaded labor from wages, employer taxes, insurance, "
                        "benefits, and paid nonproductive time. Do not count travel "
                        "or setup twice when those hours already appear as separate "
                        "lines in the paid-time schedule."
                    ),
                    (
                        "Separate direct cleaning, mobilization, supervision, consumables, "
                        "equipment, administration, and expected defect cost. Reconcile "
                        "annual totals first, then divide by twelve so rounded monthly "
                        "figures do not create unexplained annual differences."
                    ),
                    (
                        "Calculate working capital from the timing of actual cash "
                        "outflows and collections. Stress a delayed first payment, "
                        "a disputed invoice, and a payroll cycle arriving before "
                        "receivables clear; revenue recognition does not fund wages."
                    ),
                    (
                        "Compare the contract illustration with all three canonical "
                        "scenarios without rewriting their published numbers. Label "
                        "contribution separately from owner net profit, and flag "
                        "any wage or capacity assumption that makes a benchmark "
                        "unattainable under the proposed staffing plan."
                    ),
                ],
                "fields": [
                    field(
                        "Canonical scenario reconciliation",
                        "textarea",
                        (
                            "Enter annual recognized cleaning revenue, net margin, owner "
                            "net profit, implied total cost, and team composition for "
                            "every canonical scenario. Preserve the published values "
                            "even when operational feasibility requires further investigation."
                        ),
                        (
                            "Conservative: $250,000 revenue, 8% margin, $20,000 owner "
                            "net, $230,000 implied cost, 1 FT + 3 C. Base: "
                            "$725,000, 12.0%, $87,000, $638,000, 1 FT + 3 C. "
                            "Scaled: $1,200,000, 16%, $192,000, $1,008,000, "
                            "2 FT + 4 C, totaling 6 people. These are portfolio benchmarks."
                        ),
                    ),
                    field(
                        "Direct cleaning labor",
                        "textarea",
                        (
                            "Calculate direct annual hours from visits and task time, "
                            "then apply a documented loaded hourly cost. Identify "
                            "what the burden includes and reserve separate lines "
                            "for paid activities outside direct cleaning."
                        ),
                        (
                            "The office requires 260 visits multiplied by 4.00 "
                            "direct hours, equaling 1,040 annual hours. A $20 "
                            "wage plus an illustrative 25% employer burden produces "
                            "$25 per paid hour. Direct cleaning therefore costs "
                            "$26,000 annually, or $2,166.67 monthly after rounding. "
                            "Local payroll and insurance quotes must replace the illustrative burden."
                        ),
                    ),
                    field(
                        "Mobilization and supervision costs",
                        "textarea",
                        (
                            "Price intersite travel, setup, teardown, required meetings, "
                            "and supervisor coverage. State whether each quantity is "
                            "measured per visit or per month and distinguish payroll "
                            "cost from any separate vehicle expense."
                        ),
                        (
                            "Allow 0.80 additional paid hours per visit for setup "
                            "and allocated intersite travel: 208 annual hours at "
                            "$25 cost $5,200. Supervisor inspection allocation is "
                            "$2,400 annually. Combined cost is $7,600, or "
                            "$633.33 monthly. Vehicle expense, if incurred, must "
                            "be priced separately rather than assumed inside the hourly wage."
                        ),
                    ),
                    field(
                        "Nonlabor cost schedule",
                        "textarea",
                        (
                            "Enter consumables, equipment ownership or rental, insurance "
                            "allocation, and administration. Identify customer-provided supplies "
                            "and explain how replacement equipment is funded without "
                            "counting both purchase cash and depreciation as operating expense."
                        ),
                        (
                            "Annual operating allocations are $1,800 for chemicals "
                            "and consumables, $1,200 for equipment usage, and "
                            "$3,000 for insurance and administration. Their combined "
                            "$6,000 equals $500 monthly. Customer restroom paper "
                            "is excluded and purchased directly by the customer. "
                            "Equipment purchase cash is tracked separately in the startup budget."
                        ),
                    ),
                    field(
                        "Scrub and defect reserve",
                        "textarea",
                        (
                            "Estimate expected callback hours and materials from defect "
                            "frequency and correction time. Treat planned periodic floor "
                            "work separately, and explain how actual corrections consume "
                            "the management reserve without duplicating expense."
                        ),
                        (
                            "Budget 48 annual callback hours at $25, creating "
                            "a $1,200 management rework allowance, or $100 "
                            "monthly. That supports twelve four-hour corrections. "
                            "Routine floor restoration remains separately priced. Actual "
                            "callback payroll is tagged to the defect code and "
                            "compared with the allowance; accounting records actual "
                            "expense rather than a second automatic payroll charge."
                        ),
                    ),
                    field(
                        "Price and contribution bridge",
                        "textarea",
                        (
                            "Reconcile annual contract revenue to direct and allocated "
                            "costs, contribution, and any further portfolio overhead. "
                            "Show both dollars and percentages, making clear which "
                            "profit measure the selling team may quote."
                        ),
                        (
                            "Annual price is $48,000. Costs total $26,000 + "
                            "$5,200 + $2,400 + $1,800 + $1,200 + "
                            "$3,000 + $1,200 = $40,800. Contribution is "
                            "$7,200, or 15%. An illustrative additional $1,440 "
                            "portfolio allocation leaves $5,760, or 12%; this "
                            "single-contract illustration does not establish the Base portfolio result."
                        ),
                    ),
                    field(
                        "Working-capital float calculation",
                        "textarea",
                        (
                            "Model the interval from first service to collected payment "
                            "and identify cash outflows within that interval. Add "
                            "a specific disruption buffer, distinguishing required funding "
                            "from receivables balance and accounting profit."
                        ),
                        (
                            "Monthly operating cost is $3,400. Monthly arrears "
                            "billing with net-30 terms can put first cash roughly "
                            "60 days after service starts. Planning coverage is "
                            "two months of cost, $6,800, plus one $3,400 "
                            "buffer, totaling $10,200. Approximately $8,000 of "
                            "earned or invoiced exposure is revenue exposure, not the funding calculation."
                        ),
                    ),
                    field(
                        "Startup cash and expense boundaries",
                        "textarea",
                        (
                            "Allocate startup resources across equipment, deposits, onboarding, "
                            "and payroll float. Explain how the stated monthly "
                            "operating range relates to launch scale rather than "
                            "mistaking it for every mature portfolio expense."
                        ),
                        (
                            "A $35,000 launch budget allocates $10,000 equipment, "
                            "$3,000 insurance deposits, $2,000 onboarding, and "
                            "$20,000 float. It sits within the $10,000–$50,000 "
                            "startup range. The $3,000–$14,000 monthly operating "
                            "range describes a planning envelope; Base implied "
                            "all-in annual cost is $638,000, averaging $53,166.67 monthly."
                        ),
                    ),
                    field(
                        "Labor sensitivity and feasibility exception",
                        "textarea",
                        (
                            "Stress wage increases, productivity slippage, and the "
                            "canonical team labels against the available cost budget. "
                            "Document infeasibility explicitly rather than concealing it "
                            "through unpaid owner work or misclassified labor."
                        ),
                        (
                            "A 10% increase in the $25 loaded rate adds "
                            "$3,120 across 1,248 direct and mobilization hours. "
                            "Separately, five full-time employees at 2,080 hours "
                            "and $25 loaded cost require $260,000 before "
                            "contractors. That exceeds Conservative's $230,000 total "
                            "cost benchmark; the benchmark remains unchanged, but this staffing-cost interpretation fails."
                        ),
                    ),
                    field(
                        "Repricing and cash intervention",
                        "textarea",
                        (
                            "Define numeric triggers for repricing, collection escalation, "
                            "and suspension review. Name the responsible role and "
                            "specify how contractual notice requirements prevent an "
                            "improvised service interruption during a payment dispute."
                        ),
                        (
                            "Review pricing when paid hours exceed bid hours "
                            "by 10% for four weeks. Finance contacts accounts "
                            "payable five days after the due date and escalates "
                            "at fifteen days. At thirty overdue days, the "
                            "owner reviews contractual notice and cure provisions "
                            "before changing service, while preserving the next two payroll cycles."
                        ),
                    ),
                ],
                "completion_gate": (
                    "Finance verifies the $40,800 contract cost bridge, $7,200 "
                    "contribution, and $10,200 funding model. Portfolio planning must "
                    "retain all canonical figures and separately resolve any staffing "
                    "feasibility exception before those benchmarks become an operating budget."
                ),
            },
            {
                "worksheet_id": "ws-03",
                "number": 3,
                "title": "Execution, Service Ledger and Technical QA Pre-Flight",
                "purpose": (
                    "Translate the signed scope into repeatable shifts, controlled "
                    "chemical use, traceable time records, and invoice-ready evidence. "
                    "Give supervisors a practical inspection routine that detects "
                    "missed work early while protecting customer access information "
                    "and separating approved extras from routine service."
                ),
                "chapter_ref": "Q7, Q8",
                "instructions": [
                    (
                        "Create one service specification for each site and version "
                        "it whenever scope changes. Link tasks to rooms, frequencies, "
                        "estimated minutes, and acceptance evidence so cleaners do "
                        "not have to interpret a sales proposal during a shift."
                    ),
                    (
                        "Verify badges, keys, alarm instructions, emergency contacts, "
                        "storage, equipment condition, and chemical documentation before "
                        "the first visit. Conduct a supervised dry run and "
                        "record any access delay as an operational defect requiring ownership."
                    ),
                    (
                        "Use individual time records with site and task codes. "
                        "Capture required paid activities and preserve corrections "
                        "with reviewer identity; a schedule is an expectation, "
                        "whereas the payroll ledger must reflect actual compensable work."
                    ),
                    (
                        "Inspect observable outcomes using a fixed sampling plan "
                        "and documented severity rules. Record room identifiers "
                        "instead of sensitive customer content, and connect each "
                        "failed item to correction time, responsible staff, and follow-up verification."
                    ),
                    (
                        "Reconcile service completion, authorized extras, payroll, supply "
                        "usage, and billing each week. Investigate mismatches before "
                        "month-end invoicing so missing evidence does not turn "
                        "a completed service into a preventable collection dispute."
                    ),
                ],
                "fields": [
                    field(
                        "Versioned service specification",
                        "textarea",
                        (
                            "List task frequencies, area identifiers, estimated minutes, "
                            "and acceptance criteria. Record the effective version "
                            "and customer acknowledgment so an old checklist cannot "
                            "silently override a newly signed scope."
                        ),
                        (
                            "Specification HARBOR-03 takes effect on the first "
                            "service date. Restrooms receive fixture cleaning, "
                            "touchpoint treatment, restocking from customer supplies, "
                            "and floor care each visit. Carpet spotting is "
                            "daily; full extraction is excluded. The customer "
                            "acknowledges the specification and a 240-minute direct "
                            "cleaning estimate before the supervisor publishes shift assignments."
                        ),
                    ),
                    field(
                        "Shift and route construction",
                        "textarea",
                        (
                            "Convert site labor into named assignments, route order, "
                            "supervision windows, and backup coverage. Distinguish elapsed "
                            "shift duration from total labor hours when multiple "
                            "cleaners work simultaneously on the same site."
                        ),
                        (
                            "Two cleaners each receive 2.00 direct hours and "
                            "0.40 allocated setup or travel hours per visit. "
                            "Combined paid time is 4.80 hours, although the "
                            "paired assignment occupies roughly 2.40 elapsed hours. "
                            "The supervisor checks the site on Tuesday and "
                            "Friday within the separately budgeted inspection allocation."
                        ),
                    ),
                    field(
                        "Access custody and emergency contacts",
                        "textarea",
                        (
                            "Define badge and key custody, authorized access recipients, "
                            "loss reporting, and emergency escalation. Keep secrets "
                            "out of printable worksheets and explain how access "
                            "is revoked when personnel leave the assignment."
                        ),
                        (
                            "Badge A17 is assigned to the shift lead and "
                            "badge A18 to the second cleaner. The worksheet "
                            "records custody but no alarm code. Codes stay "
                            "in a restricted password manager. Lost badges "
                            "are reported immediately to building security; departing "
                            "staff return access items before their assignment is closed."
                        ),
                    ),
                    field(
                        "Chemical and equipment pre-flight",
                        "textarea",
                        (
                            "Record product identity, label instructions, safety data "
                            "sheet access, dilution method, equipment checks, and "
                            "required protective equipment. State who confirms that "
                            "the chosen product is suitable for the actual surface."
                        ),
                        (
                            "The supervisor confirms the selected EPA-registered "
                            "disinfectant label permits the intended surface and "
                            "requires five minutes of wet contact in this "
                            "example. Staff verify dilution, maintain wetness for "
                            "that interval, and inspect vacuum cords before "
                            "use. The actual purchased product label controls; "
                            "five minutes is not assumed for every disinfectant."
                        ),
                    ),
                    field(
                        "Timekeeping and payroll evidence",
                        "textarea",
                        (
                            "Specify individual time entry, location attribution, correction "
                            "review, and retention responsibilities. Include between-site "
                            "travel and required meetings where compensable, and "
                            "prohibit deleting work merely because a budget was exceeded."
                        ),
                        (
                            "Cleaner 014 records 2.00 direct hours, 0.25 "
                            "setup hours, and 0.15 intersite travel hours "
                            "for the assignment. A missed clock-out is "
                            "corrected using their written account and supervisor "
                            "review. The original entry remains visible in "
                            "the audit history; the customer billing budget "
                            "does not cap earned payroll."
                        ),
                    ),
                    field(
                        "Inspection sampling and defect severity",
                        "textarea",
                        (
                            "Set an inspection sample, pass calculation, severity "
                            "definitions, and corrective deadlines. Explain which "
                            "failures require immediate response regardless of the "
                            "overall score and avoid substituting appearance checks "
                            "for infection-control evidence."
                        ),
                        (
                            "Inspect twenty scored items per visit sample. "
                            "Nineteen passes produce 95%, but a blocked "
                            "exit or unsecured chemical container requires immediate "
                            "correction even at that score. A visibly "
                            "missed waste bin receives next-shift correction. "
                            "Visual inspection confirms observed cleaning outcomes; "
                            "it does not establish microbial reduction or replace required contact-time records."
                        ),
                    ),
                    field(
                        "Service event ledger",
                        "textarea",
                        (
                            "Define the minimum record linking a scheduled visit "
                            "to actual work, inspection, and billing. Include "
                            "unique identifiers, timestamps, exception status, and "
                            "review ownership without collecting unnecessary customer information."
                        ),
                        (
                            "Event HARBOR-2026-1201 stores site ID, scheduled "
                            "date, two worker IDs, 4.80 paid hours, "
                            "checklist version HARBOR-03, inspection score, and "
                            "supervisor review time. Its status changes from "
                            "scheduled to completed to verified. A linked "
                            "exception records one supply shortage without copying "
                            "customer documents or placing alarm details in the ledger."
                        ),
                    ),
                    field(
                        "Extra work authorization",
                        "textarea",
                        (
                            "Describe how requested work outside scope becomes "
                            "an authorized service item. Capture the requester, "
                            "price, labor estimate, timing, and evidence that "
                            "the requester can bind the paying customer."
                        ),
                        (
                            "The facilities manager requests a separately scheduled "
                            "carpet extraction for $650. The change record "
                            "states six labor hours, $75 materials and "
                            "equipment allocation, the service area, and the "
                            "authorized purchaser's acceptance. The crew performs "
                            "the work only after scheduling confirmation, and "
                            "billing uses a separate line rather than changing recurring revenue."
                        ),
                    ),
                    field(
                        "Weekly ledger reconciliation",
                        "textarea",
                        (
                            "Reconcile visits, paid hours, supply issues, corrections, "
                            "and authorized extras against the bid. Name "
                            "the reviewer and explain how exceptions move "
                            "to payroll correction, operating review, or customer billing."
                        ),
                        (
                            "Five visits should produce 24.00 paid direct "
                            "and mobilization hours. The ledger shows 25.50, "
                            "including a documented 1.50-hour callback costing "
                            "$37.50 at the loaded rate. Payroll retains "
                            "all hours. Operations tags the callback against "
                            "the rework allowance, while billing retains the "
                            "agreed monthly price because the correction is contractor-caused."
                        ),
                    ),
                    field(
                        "Invoice readiness and evidence package",
                        "textarea",
                        (
                            "Specify the records needed to issue a correct "
                            "invoice and resolve a dispute. Check contract "
                            "entity, purchase order, service period, authorized "
                            "extras, applicable tax treatment, and customer delivery requirements."
                        ),
                        (
                            "The monthly package contains the $4,000 recurring "
                            "charge, service dates, purchase order H-441, "
                            "and the approved $650 extraction line. It "
                            "references completion records without attaching worker "
                            "personal data. Finance verifies jurisdiction-specific tax "
                            "treatment and sends the invoice to the confirmed "
                            "accounts-payable address, recording delivery and the contractual due date."
                        ),
                    ),
                ],
                "completion_gate": (
                    "The supervisor completes a dry run and verifies access, "
                    "equipment, task timing, and exception handling. Finance traces "
                    "one sample visit through timekeeping, inspection, and invoicing, "
                    "with every mismatch assigned a correction owner and deadline."
                ),
            },
            {
                "worksheet_id": "ws-04",
                "number": 4,
                "title": "Statutory, Licensing, Contract and Outreach Audit",
                "purpose": (
                    "Turn wage, classification, chemical, insurance, and outreach "
                    "requirements into specific operating evidence. Identify which "
                    "rules actually apply to each location and contract, assign "
                    "owners for unresolved requirements, and prevent a generic "
                    "subcontract agreement from substituting for lawful workforce design."
                ),
                "chapter_ref": "Q5, Q9",
                "instructions": [
                    (
                        "Build a jurisdiction map for every serviced location, "
                        "not just the company mailing address. Verify business "
                        "registration, tax treatment, wage floors, paid-leave rules, "
                        "and specialized licensing using current official sources "
                        "before assigning responsibility or quoting labor."
                    ),
                    (
                        "Classify each worker relationship from actual operating "
                        "facts. Review control, independence, equipment, customers, "
                        "and applicable federal and state tests; a contractor "
                        "label, invoice, or certificate of insurance does "
                        "not independently settle employment status."
                    ),
                    (
                        "Translate the chemical inventory and exposure assessment "
                        "into training, protective equipment, labeling, and emergency "
                        "procedures. Medical sites require task-specific evaluation "
                        "rather than a blanket assumption that every cleaner "
                        "has identical exposure or privacy obligations."
                    ),
                    (
                        "Review customer and subcontract terms together so "
                        "service promises, insurance endorsements, incident reporting, "
                        "and termination rights align. Identify federal service "
                        "contract clauses separately because wage determinations "
                        "can materially change a seemingly ordinary janitorial bid."
                    ),
                    (
                        "Audit prospecting channels before scaling outreach. "
                        "Document sender identity, suppression handling, telephone "
                        "technology, and data sources, then retain evidence "
                        "showing why a particular campaign satisfies the "
                        "rules applicable to its recipients and communication method."
                    ),
                ],
                "fields": [
                    field(
                        "Jurisdiction and registration register",
                        "textarea",
                        (
                            "List the service address, governing state and municipality, "
                            "required registrations, and responsible verifier. Include "
                            "service-tax treatment and specialist work restrictions, "
                            "using dated official findings rather than broad assumptions."
                        ),
                        (
                            "Before opening a California service territory, the "
                            "operations owner checks state registration, the "
                            "city's business-license requirements, and janitorial "
                            "employer registration under California Labor Code "
                            "sections 1420–1434. The register stores source "
                            "links, review dates, renewal deadlines, and applicability "
                            "findings. Tax treatment is separately verified for "
                            "the precise services and billing jurisdiction."
                        ),
                    ),
                    field(
                        "Minimum wage, overtime and paid time",
                        "textarea",
                        (
                            "Identify applicable wage floors, overtime calculations, "
                            "compensable travel, and required payroll records. "
                            "Aggregate each employee's work across customer "
                            "sites and include additional state requirements "
                            "where they provide broader protection."
                        ),
                        (
                            "Under 29 U.S.C. sections 206 and 207, "
                            "apply covered wage and overtime requirements. "
                            "An employee working 38 hours at one "
                            "site and 6 at another has 44 "
                            "hours, not two separate short weeks. Review "
                            "29 CFR 785.38 for workday travel and "
                            "29 CFR 516.2 for required records."
                        ),
                    ),
                    field(
                        "Worker classification evidence",
                        "textarea",
                        (
                            "Record the facts supporting employee or independent "
                            "business treatment under each applicable test. "
                            "Identify conflicting evidence, the review owner, "
                            "and required changes before using a subcontract "
                            "structure in the labor budget."
                        ),
                        (
                            "A cleaner working the company's fixed route, "
                            "using its supplies, and receiving detailed daily "
                            "direction is budgeted as W-2 labor pending "
                            "review. Federal tax analysis considers 26 U.S.C. "
                            "3121(d)(2). California analysis also examines Labor "
                            "Code 2775 and any applicable 2776 exception; "
                            "a business-to-business agreement alone does not establish eligibility."
                        ),
                    ),
                    field(
                        "Subcontractor operating file",
                        "textarea",
                        (
                            "Define the documents and ongoing checks required "
                            "for a genuine subcontract business. Address "
                            "staffing responsibility, payroll obligations, insurance, "
                            "scope, audit rights, and any client consent "
                            "required before subcontracted work begins."
                        ),
                        (
                            "The subcontract file contains entity verification, "
                            "tax documentation, signed scope, insurance evidence, "
                            "and confirmation of who employs the assigned "
                            "crew. The customer contract expressly permits "
                            "the arrangement. California Labor Code 2810.3 "
                            "is reviewed where applicable to shared liability. "
                            "The scorecard's C headcount is a planning "
                            "label, not evidence that any individual is lawfully classified."
                        ),
                    ),
                    field(
                        "Hazard communication and chemical controls",
                        "textarea",
                        (
                            "Map the chemical inventory to labels, safety "
                            "data sheets, employee training, protective equipment, "
                            "and dilution controls. Identify the specific "
                            "standard and the records demonstrating that "
                            "assigned workers understand the hazards."
                        ),
                        (
                            "The employer maintains its hazard communication "
                            "program under 29 CFR 1910.1200, including "
                            "container labeling, accessible safety data sheets, "
                            "and required training. PPE selection follows "
                            "the task assessment under 29 CFR 1910.132. "
                            "Disinfectant use follows the EPA label; "
                            "7 U.S.C. 136j(a)(2)(G) addresses use inconsistent "
                            "with pesticide labeling, subject to statutory exceptions."
                        ),
                    ),
                    field(
                        "Bloodborne exposure and medical privacy",
                        "textarea",
                        (
                            "Determine whether assigned duties create occupational "
                            "bloodborne exposure and whether services involve "
                            "protected health information beyond incidental contact. "
                            "Document the resulting controls without treating "
                            "every medical cleaning contract as identical."
                        ),
                        (
                            "Where occupational exposure exists, apply 29 "
                            "CFR 1910.1030, including an exposure control "
                            "plan, required training, and hepatitis B "
                            "vaccination availability within ten working days "
                            "of initial assignment, subject to specified "
                            "exceptions. Janitorial incidental contact does not "
                            "automatically create a HIPAA business associate; "
                            "evaluate actual functions under 45 CFR 160.103."
                        ),
                    ),
                    field(
                        "Insurance and incident allocation",
                        "textarea",
                        (
                            "Record required coverage, limits, endorsements, exclusions, "
                            "deductibles, and renewal dates. Distinguish customer "
                            "contract requirements from statutory obligations and "
                            "confirm that medical tasks, vehicle use, "
                            "and subcontracting fit the actual policy wording."
                        ),
                        (
                            "The customer requests $1 million per occurrence "
                            "and $2 million aggregate general liability, "
                            "plus workers' compensation as required by "
                            "the operating state. The broker verifies "
                            "the actual additional-insured endorsement rather "
                            "than relying only on a certificate. "
                            "The supervisor reports property damage immediately "
                            "and preserves facts without promising uninsured reimbursement."
                        ),
                    ),
                    field(
                        "Contract remedies and public procurement",
                        "textarea",
                        (
                            "Review scope, payment, indemnity, cure rights, "
                            "termination, assignment, and public-contract obligations. "
                            "Identify any applicable wage determination "
                            "before bidding and document who confirms "
                            "that contract terms match the modeled costs."
                        ),
                        (
                            "The private office agreement provides written "
                            "defect notice and a defined correction "
                            "period before termination for remediable service "
                            "failures. A separate covered federal service "
                            "solicitation exceeding $2,500 requires review "
                            "under 41 U.S.C. 6701–6707 and FAR "
                            "52.222-41, including applicable wage and fringe "
                            "requirements; ordinary private-office labor assumptions cannot simply carry over."
                        ),
                    ),
                    field(
                        "Email, calling and suppression controls",
                        "textarea",
                        (
                            "Identify each outreach channel, recipient source, "
                            "sender disclosures, opt-out process, and calling "
                            "technology. Record applicable federal and "
                            "state rules, including circumstances where "
                            "business recipients still receive statutory protection."
                        ),
                        (
                            "Commercial email follows 15 U.S.C. 7704 "
                            "with accurate headers, nondeceptive subjects, "
                            "required identification, a valid postal address, "
                            "and an effective opt-out honored within "
                            "ten business days. Calling and texting "
                            "receive separate review under 47 U.S.C. "
                            "227 and applicable state rules; a "
                            "business contact is not a universal exemption."
                        ),
                    ),
                    field(
                        "Evidence ownership and remediation",
                        "textarea",
                        (
                            "Assign every requirement an owner, evidence "
                            "location, review date, and correction deadline. "
                            "Explain which unresolved conditions prevent "
                            "staff assignment or service commencement "
                            "and how completion is independently checked."
                        ),
                        (
                            "The operations owner controls chemical training "
                            "records, payroll controls wage configuration, "
                            "and finance tracks insurance renewals. A "
                            "missing product safety data sheet prevents "
                            "use of that product until corrected. "
                            "The supervisor verifies the replacement record "
                            "and worker instruction before resuming the "
                            "task, while unaffected contracted cleaning continues with suitable approved materials."
                        ),
                    ),
                ],
                "completion_gate": (
                    "The responsible owners verify current jurisdictional requirements, "
                    "worker treatment, wage settings, insurance evidence, and task-specific "
                    "safety controls. Unresolved medical exposure, unlawful pay practices, "
                    "or unauthorized subcontracting must be corrected before the affected "
                    "assignment begins."
                ),
            },
            {
                "worksheet_id": "ws-05",
                "number": 5,
                "title": "Automation, Growth Flywheel and Risk Fallback Tracker",
                "purpose": (
                    "Automate scheduling, inspection records, and billing without "
                    "concealing the labor required to fulfill contracts. Build "
                    "a measurable local sales process, connect qualified opportunities "
                    "to available crew capacity, and maintain workable fallbacks "
                    "for software outages, absences, collection delays, and customer loss."
                ),
                "chapter_ref": "Q6, Q10",
                "instructions": [
                    (
                        "Choose a small operating stack with clear system "
                        "ownership. Define which application holds customer "
                        "records, schedules, time, inspections, and invoices, "
                        "then use stable identifiers to prevent duplicate "
                        "sites or mismatched records across integrations."
                    ),
                    (
                        "Automate routine transfers only after the manual "
                        "process reconciles. Validate incoming fields, keep "
                        "a retry log, and route exceptions to "
                        "a named person; a failed integration must "
                        "not silently skip payroll or issue duplicate invoices."
                    ),
                    (
                        "Measure outbound activity through qualified walkthroughs "
                        "and signed recurring revenue, not email volume "
                        "alone. Match each prospect segment to proof "
                        "of service capability and exclude contacts that "
                        "have opted out or fall outside the territory."
                    ),
                    (
                        "Tie every proposed start date to verified "
                        "staffing, training, equipment, and cash coverage. "
                        "Automation can reduce coordination effort, but "
                        "the portfolio still needs paid cleaning hours "
                        "and supervisor capacity for each additional contracted visit."
                    ),
                    (
                        "Rehearse the fallback for an absent cleaner, "
                        "failed timekeeping application, delayed customer payment, "
                        "and lost anchor account. Record the response "
                        "owner, activation threshold, recovery evidence, and "
                        "cost instead of assuming software availability guarantees service continuity."
                    ),
                ],
                "fields": [
                    field(
                        "System map and record ownership",
                        "textarea",
                        (
                            "Name the tools used for prospecting, scheduling, "
                            "timekeeping, inspection, and accounting. Assign "
                            "the authoritative owner of each data "
                            "element and define stable identifiers "
                            "that survive customer or site name changes."
                        ),
                        (
                            "HubSpot holds prospect activity, Jobber holds "
                            "service schedules, an approved timekeeping "
                            "system records actual hours, and QuickBooks "
                            "Online holds invoices and payments. Site "
                            "ID SITE-028-001 appears in every system. "
                            "The operations administrator owns site identity; "
                            "finance owns customer billing identity and "
                            "does not let a marketing import overwrite payment terms."
                        ),
                    ),
                    field(
                        "Schedule publication and exception handling",
                        "textarea",
                        (
                            "Define how recurring work becomes crew assignments "
                            "and how access changes, holidays, absences, "
                            "and overtime conflicts are detected. "
                            "Specify who resolves exceptions before "
                            "workers receive the final schedule."
                        ),
                        (
                            "The scheduler creates five weekly visits "
                            "from the signed service calendar. A "
                            "validation step checks badges, training "
                            "status, availability, and projected weekly "
                            "hours before publication. A sixth visit "
                            "requested for a holiday event enters "
                            "an exception queue; the supervisor obtains "
                            "scope and price confirmation rather than allowing automatic unpaid schedule expansion."
                        ),
                    ),
                    field(
                        "Inspection capture and privacy controls",
                        "textarea",
                        (
                            "Describe the mobile inspection form, required "
                            "fields, acceptable photographs, permissions, and "
                            "retention process. Minimize captured information "
                            "and ensure supervisors can document "
                            "defects without recording customer records "
                            "or private occupant activity."
                        ),
                        (
                            "A Microsoft Forms inspection captures site "
                            "ID, room code, twenty scored items, "
                            "severity, and correction owner. Photos "
                            "show the affected surface only; screens, "
                            "patient names, and documents stay outside "
                            "the frame. Access is limited to "
                            "assigned operations staff, and the retention "
                            "schedule follows contractual needs and documented recordkeeping requirements."
                        ),
                    ),
                    field(
                        "Billing automation and duplicate prevention",
                        "textarea",
                        (
                            "Specify the verified event that permits "
                            "invoice creation, the unique billing "
                            "key, validation checks, and retry "
                            "behavior. Separate recurring charges from "
                            "extras and prevent automation from "
                            "converting unreviewed requests into billed revenue."
                        ),
                        (
                            "The billing key combines customer ID, "
                            "contract ID, service month, and charge "
                            "type. A verified monthly service "
                            "summary prepares one $4,000 draft "
                            "invoice. Retrying the workflow finds "
                            "the same key instead of creating "
                            "another charge. The $650 extraction "
                            "requires its own accepted change record and completion evidence before inclusion."
                        ),
                    ),
                    field(
                        "Prospect list and outreach sequence",
                        "textarea",
                        (
                            "Define a narrow prospect segment, permitted "
                            "contact sources, useful message content, "
                            "follow-up timing, and suppression handling. "
                            "Make the offer specific to "
                            "facility operating problems rather than "
                            "promising unsupported savings or service outcomes."
                        ),
                        (
                            "Build a list of forty nearby "
                            "professional offices using public business "
                            "directories and customer referrals. Offer "
                            "a walkthrough focused on missed-task "
                            "patterns and measurable frequencies. Send "
                            "one relevant introduction and one "
                            "follow-up after seven business days. "
                            "Check suppression before each send and record the recipient's response without buying indiscriminate lists."
                        ),
                    ),
                    field(
                        "Sales funnel and acquisition economics",
                        "textarea",
                        (
                            "Calculate movement from targeted accounts "
                            "to conversations, walkthroughs, proposals, and "
                            "wins. Include sales labor and "
                            "travel in acquisition cost, and "
                            "compare that cost with contribution "
                            "rather than gross contract revenue."
                        ),
                        (
                            "Forty targeted accounts yield eight conversations, "
                            "four walkthroughs, two proposals, and "
                            "one $48,000 annual contract in "
                            "this planning example. Acquisition spending "
                            "is $1,200 including sales labor "
                            "and travel. At $600 monthly "
                            "contract contribution, simple acquisition payback "
                            "is two months of contribution, separate from collection timing and mobilization cash."
                        ),
                    ),
                    field(
                        "Renewal and referral flywheel",
                        "textarea",
                        (
                            "Define the recurring customer review, "
                            "evidence presented, renewal timing, and "
                            "referral request. Link growth to "
                            "documented service quality while avoiding "
                            "incentives that cause supervisors to "
                            "hide complaints or manipulate inspection scores."
                        ),
                        (
                            "Each month, the account lead reviews "
                            "completed visits, inspection scores, callbacks, "
                            "and agreed changes with the "
                            "facilities manager. Renewal discussion begins "
                            "ninety days before expiry. After "
                            "two consecutive months with resolved "
                            "defects and timely reporting, request "
                            "one introduction to a nearby building manager; referral credit never depends on suppressing complaints."
                        ),
                    ),
                    field(
                        "Absence and turnover fallback",
                        "textarea",
                        (
                            "Set absence thresholds, relief coverage, "
                            "training requirements, customer communication, and "
                            "incremental cost. Ensure the response "
                            "does not depend on off-clock "
                            "labor or untrained temporary staff "
                            "performing medical or chemical tasks."
                        ),
                        (
                            "A cleaner reports absence two hours "
                            "before service. The scheduler contacts "
                            "a trained relief employee with "
                            "current site access and checks "
                            "their weekly hours. Two added "
                            "hours at a $30 loaded "
                            "rate cost $60. If coverage "
                            "cannot satisfy the contracted window, the supervisor contacts the customer and documents the agreed recovery plan."
                        ),
                    ),
                    field(
                        "Software outage and recovery drill",
                        "textarea",
                        (
                            "Describe offline scheduling, time capture, "
                            "access to safety information, and "
                            "later reconciliation. Name the recovery "
                            "owner and explain how backfilled "
                            "records are distinguished from original "
                            "entries without losing actual paid time."
                        ),
                        (
                            "During a four-hour application outage, "
                            "the shift lead uses the "
                            "printed route sheet and individual "
                            "time forms. Safety data sheets "
                            "remain accessible in the site "
                            "binder. The administrator imports records "
                            "the next morning with an "
                            "outage tag, checks duplicates, and obtains supervisor confirmation before payroll export and invoice preparation resume."
                        ),
                    ),
                    field(
                        "Capacity-aware growth and risk triggers",
                        "textarea",
                        (
                            "Set measurable limits for contracted "
                            "hours, customer concentration, receivable aging, "
                            "and supervisor load. Explain the "
                            "specific response when a limit "
                            "is crossed and keep hiring "
                            "decisions connected to collected cash."
                        ),
                        (
                            "Pause new start-date commitments when "
                            "next month's assigned hours exceed "
                            "90% of verified available capacity. "
                            "Review any payment obligor exceeding "
                            "20% of annual revenue and "
                            "any invoice thirty days overdue. "
                            "The owner prioritizes collections, recruits "
                            "trained relief capacity, or delays starts; sending more proposals is not a remedy for an understaffed route."
                        ),
                    ),
                ],
                "completion_gate": (
                    "Operations demonstrates one schedule-to-inspection-to-invoice cycle, "
                    "a duplicate-safe retry, and an offline recovery. Sales may "
                    "commit additional starts only when named staffing, required "
                    "training, supervisor coverage, and working capital support the "
                    "new service obligations."
                ),
            },
            {
                "worksheet_id": "ws-06",
                "number": 6,
                "title": "30-Day Launch, Supervisor Pod KPIs and Exit Readiness",
                "purpose": (
                    "Organize the first thirty days around evidence, "
                    "paid capacity, and cash protection rather than "
                    "an arbitrary sales deadline. Establish supervisor "
                    "pod metrics and a transferable operating record "
                    "that supports renewal, delegation, and eventual "
                    "buyer review without overstating earnings or contract durability."
                ),
                "chapter_ref": "Q11, Q12",
                "instructions": [
                    (
                        "Set thirty-day deliverables that remain useful "
                        "even if the first contract closes "
                        "later. The expected first-deal window "
                        "is one to four months, so "
                        "track completed underwriting and operating "
                        "readiness separately from signed revenue."
                    ),
                    (
                        "Assign a named owner and dated "
                        "evidence requirement to each weekly "
                        "milestone. Release spending in relation "
                        "to verified opportunities and required "
                        "readiness, preserving payroll float instead "
                        "of buying a full equipment fleet before scope is known."
                    ),
                    (
                        "Construct each supervisor pod from "
                        "actual paid hours, travel geography, "
                        "inspection duties, relief availability, and "
                        "training coverage. A headcount label "
                        "does not establish productive capacity, "
                        "and contractor availability must be evidenced rather than assumed."
                    ),
                    (
                        "Review quality, labor variance, safety, "
                        "collections, and concentration together each "
                        "week. Investigate deteriorating leading indicators "
                        "before they become lost contracts, "
                        "and preserve reported defects rather "
                        "than rewarding a superficially perfect dashboard."
                    ),
                    (
                        "Maintain buyer-ready records from the "
                        "first signed contract: service scope, "
                        "renewal rights, assignment terms, payroll "
                        "support, equipment ownership, and reconciled "
                        "earnings. Separate documented transferable operations "
                        "from relationships or unpaid owner work that disappear after a sale."
                    ),
                ],
                "fields": [
                    field(
                        "Days 1–7: underwriting and setup",
                        "textarea",
                        (
                            "Identify first-week deliverables, accountable roles, "
                            "spending limits, and evidence of "
                            "completion. Prioritize jurisdictional checks, "
                            "target selection, insurance quotations, "
                            "and a realistic cash plan "
                            "before promising a service launch."
                        ),
                        (
                            "By day seven, the owner "
                            "selects a 25-minute service territory, "
                            "qualifies forty target offices, and "
                            "obtains payroll and insurance estimates. "
                            "Finance builds the $35,000 startup "
                            "allocation and preserves $20,000 "
                            "for float. Operations completes the "
                            "jurisdiction register and records three authorized walkthrough appointments without counting them as contracted revenue."
                        ),
                    ),
                    field(
                        "Days 8–14: walkthroughs and price proof",
                        "textarea",
                        (
                            "Set second-week targets for measured "
                            "scope, task timing, counterparty checks, "
                            "and proposal preparation. Specify which "
                            "assumptions require direct observation "
                            "and what evidence prevents an "
                            "unsupported low bid from being released."
                        ),
                        (
                            "By day fourteen, operations measures "
                            "three sites and performs one "
                            "authorized timing trial. Finance reconciles "
                            "the office illustration to $48,000 "
                            "annual price and $40,800 cost. "
                            "The owner verifies purchasing authority "
                            "and payment routing before issuing "
                            "two proposals. Any unmeasured medical task remains outside those prices until its procedure and labor requirement are established."
                        ),
                    ),
                    field(
                        "Days 15–21: workforce and operating rehearsal",
                        "textarea",
                        (
                            "Define hiring or subcontract review, "
                            "training, access preparation, and systems "
                            "testing for the third week. "
                            "Keep contingent staffing plans explicit "
                            "and avoid treating candidate interest "
                            "as confirmed available cleaning capacity."
                        ),
                        (
                            "By day twenty-one, the supervisor "
                            "checks two employee candidates, completes "
                            "required onboarding for confirmed assignments, "
                            "and rehearses the 4.80-hour paid "
                            "visit plan. The administrator tests "
                            "time capture and a draft "
                            "invoice using a training record. "
                            "No worker receives unsupervised chemical duties before task-specific instruction, and no unsigned customer is marked active."
                        ),
                    ),
                    field(
                        "Days 22–30: launch or readiness checkpoint",
                        "textarea",
                        (
                            "State fourth-week actions for both "
                            "a signed contract and a "
                            "still-open sales process. Define "
                            "launch evidence, first inspection, "
                            "cash verification, and the next "
                            "decision without forcing revenue into an artificial deadline."
                        ),
                        (
                            "If the contract is signed, "
                            "verify access and $10,200 operating "
                            "coverage, conduct the first supervised "
                            "visit, and review the first "
                            "five service events. If negotiations "
                            "continue, preserve cash and schedule "
                            "the next decision meeting. A "
                            "day-thirty readiness result is acceptable within the one-to-four-month first-deal planning window; an unsigned proposal remains pipeline."
                        ),
                    ),
                    field(
                        "Supervisor pod capacity model",
                        "textarea",
                        (
                            "Translate the canonical team label "
                            "into explicit employee roles, paid "
                            "hours, productive fractions, and "
                            "contractor commitments. Test required "
                            "service hours against available capacity "
                            "and expose any gap before approving growth."
                        ),
                        (
                            "For Base's 5 FT + "
                            "4 C, illustrate four cleaners "
                            "at 2,080 hours and 80% "
                            "direct productivity: 6,656 hours. "
                            "One supervisor adds 520 direct "
                            "hours. Four independently reviewed contractor "
                            "commitments at 1,040 hours and "
                            "80% productivity add 3,328, totaling 10,504 direct hours. Contractor hours are assumptions requiring written availability, not promised capacity."
                        ),
                    ),
                    field(
                        "Revenue capacity and service-mix bridge",
                        "textarea",
                        (
                            "Compare revenue per productive hour "
                            "with the contract model and "
                            "portfolio target. Identify required "
                            "changes in price, task productivity, "
                            "service mix, or staffing without "
                            "silently changing the canonical revenue or team figures."
                        ),
                        (
                            "The office model earns $48,000 "
                            "over 1,040 direct hours, or "
                            "$46.15 per hour. Base revenue "
                            "of $725,000 would require approximately "
                            "15,708 direct hours at that "
                            "unrounded rate, exceeding illustrative capacity "
                            "by 5,204 hours. At 10,504 "
                            "hours, required revenue averages $69.02 per hour. Validate a different service mix or capacity plan before treating Base as executable."
                        ),
                    ),
                    field(
                        "Weekly pod KPI scorecard",
                        "textarea",
                        (
                            "Define a small set of "
                            "quality, labor, coverage, cash, "
                            "and safety metrics with calculation "
                            "rules, thresholds, and owners. "
                            "Use paired measures so cost "
                            "improvements cannot conceal missed work or unpaid time."
                        ),
                        (
                            "The weekly review tracks completed "
                            "visits divided by scheduled visits, "
                            "inspection passes divided by sampled "
                            "items, actual versus budgeted paid "
                            "hours, callback cost, and overdue "
                            "receivables. Targets are 100% visit "
                            "coverage, at least 95% inspection "
                            "passes, and no unexplained unpaid hours. Safety-critical defects trigger immediate response regardless of aggregate performance."
                        ),
                    ),
                    field(
                        "Owner role and earnings normalization",
                        "textarea",
                        (
                            "Document the owner's recurring tasks, "
                            "hours, compensation treatment, and "
                            "replacement cost. Reconcile recorded "
                            "earnings to a transferable operating "
                            "model without adding back expenses "
                            "that a successor would still incur."
                        ),
                        (
                            "The owner performs fifteen weekly "
                            "hours of sales and dispatch. "
                            "At an illustrative $35 loaded "
                            "replacement rate for 52 weeks, "
                            "that role costs $27,300 annually. "
                            "If it is absent from "
                            "the underlying cost model, a "
                            "buyer-style sensitivity reduces $87,000 Base owner net to $59,700. The canonical $87,000 remains unchanged and is clearly distinguished from this sensitivity."
                        ),
                    ),
                    field(
                        "Transferability and contract ledger",
                        "textarea",
                        (
                            "List executed contracts, renewal dates, "
                            "termination rights, assignment conditions, "
                            "customer concentration, and supporting "
                            "service records. Identify customer "
                            "consents or equipment ownership "
                            "evidence needed for a potential transfer of operations."
                        ),
                        (
                            "The contract ledger records Harbor's "
                            "$48,000 annual recurring revenue, "
                            "signed scope, renewal date, "
                            "termination provisions, and assignment "
                            "language. If assignment requires "
                            "customer consent, the owner records "
                            "that dependency rather than labeling "
                            "the revenue automatically transferable. Equipment serial numbers, purchase records, maintenance history, and any lender interests are maintained in a separate asset register."
                        ),
                    ),
                    field(
                        "Scale decision and exit-readiness review",
                        "textarea",
                        (
                            "State the next ninety-day decision, "
                            "required evidence, capital limits, "
                            "and unresolved risks. Preserve "
                            "the Scaled benchmark while "
                            "requiring proof that additional "
                            "crew hours, supervision, collections, and documentation support expansion."
                        ),
                        (
                            "The next review requires three "
                            "months of reconciled contract results, "
                            "documented relief coverage, and "
                            "adequate cash before adding sites. "
                            "Scaled remains $1,200,000 revenue, "
                            "16% margin, $192,000 owner net, "
                            "and 2 FT + 4 C. "
                            "The owner must substantiate the $1,008,000 cost envelope and eleven-person capacity; scheduling software alone does not establish either result."
                        ),
                    ),
                ],
                "completion_gate": (
                    "The owner signs a thirty-day evidence ledger, a funded "
                    "ninety-day plan, and a pod capacity reconciliation. Exit "
                    "readiness requires traceable earnings, documented owner replacement "
                    "work, accessible service records, and an explicit register of "
                    "contract-transfer conditions and unresolved operating risks."
                ),
            },
        ],
    }
