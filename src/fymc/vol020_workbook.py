from __future__ import annotations


def build_volume_020_workbook() -> dict:
    def field(name: str, input_type: str, prompt: str, example: str) -> dict:
        return {
            "name": name,
            "type": input_type,
            "prompt": prompt,
            "example": example,
        }

    return {
        "workbook_id": "wb-020-government-contract-brokering",
        "volume_id": "vol-020-government-contract-brokering",
        "title": "Government Contract Brokering — Operator Companion Workbook",
        "subtitle": (
            "6 Printable Operator Worksheets for Federal and Municipal Bid Desks, "
            "Prime/Subcontractor Qualification, Service-Fee Economics, FAR Review, "
            "Submission Controls, and Small-Team Launch Execution"
        ),
        "worksheets": [
            {
                "worksheet_id": "ws-01",
                "number": 1,
                "title": "Opportunity Underwriting and Counterparty Qualification",
                "purpose": (
                    "Select a procurement vertical where documented delivery capability, "
                    "lawful fee arrangements, and accessible buying channels support a "
                    "repeatable bid desk. Separate advisory revenue from customer contract "
                    "value, qualify every delivery counterparty, and reject opportunities "
                    "whose eligibility or execution assumptions cannot survive examination."
                ),
                "chapter_ref": "Q1, Q2, Q6",
                "instructions": [
                    (
                        "Choose one federal buying pattern and one municipal comparison "
                        "rather than searching every commodity. Record solicitation sources, "
                        "purchasing frequency, incumbent evidence, and delivery geography. Treat "
                        "every worked example below as a synthetic planning case, not a "
                        "verified live opportunity."
                    ),
                    (
                        "Define whether the operator supplies proposal services, performs as "
                        "a prime, or undertakes a genuine subcontract work package. Map who "
                        "contracts with the agency, who controls performance, and who bears "
                        "defect costs before assigning any revenue."
                    ),
                    (
                        "Collect counterparty evidence directly from authoritative records "
                        "and authorized customer documents. Check entity identity, SAM.gov "
                        "status where applicable, exclusions, ownership representations, "
                        "insurance, references, capacity, and working capital; record the "
                        "reviewer and the actual date of each check."
                    ),
                    (
                        "Score opportunities using written eligibility, capability, economics, "
                        "timing, and integrity criteria. Distinguish a failed mandatory "
                        "requirement from an unattractive commercial score. Do not let a "
                        "large advertised ceiling compensate for missing qualifications "
                        "or an unsupported teaming structure."
                    ),
                    (
                        "Approve only a defined discovery or delivery engagement with a "
                        "named client payer and documented scope. Archive rejection reasons "
                        "alongside accepted opportunities so the next sourcing cycle improves "
                        "without repeatedly evaluating the same unsuitable agencies, "
                        "suppliers, or contract vehicles."
                    ),
                ],
                "fields": [
                    field(
                        "Vertical and buying-pattern thesis",
                        "textarea",
                        "Describe the service category, buyer population, purchasing cadence, "
                        "geographic boundary, and evidence supporting repeat demand. Identify "
                        "which work the bid desk can evaluate competently and which technical "
                        "requirements require an independent specialist before pursuit.",
                        "The initial desk supports facilities-maintenance proposal preparation "
                        "for small contractors serving two nearby federal installations and "
                        "three municipalities. The research target is 24 relevant notices "
                        "per quarter. Electrical design, hazardous-material remediation, and "
                        "bonded construction remain outside scope until qualified specialists "
                        "can evaluate those requirements and delivery partners.",
                    ),
                    field(
                        "Opportunity identity and source provenance",
                        "textarea",
                        "Record the authoritative notice identifier, source URL, agency, "
                        "contracting contact, publication date, amendment history, question "
                        "deadline, and submission deadline with time zone. Explain how staff "
                        "will distinguish authoritative solicitation instructions from "
                        "aggregator summaries and preliminary market research.",
                        "Training record FED-FAC-001 represents a synthetic facilities "
                        "solicitation. The live register would store its SAM.gov notice URL, "
                        "download timestamp, and amendment identifiers. The internal example "
                        "deadline is December 18 at 2:00 p.m. Eastern; the desk schedules "
                        "a final authoritative-source refresh 24 hours before submission.",
                    ),
                    field(
                        "Operator role and recognized revenue boundary",
                        "textarea",
                        "Specify the operator's contracting role, actual deliverables, client "
                        "payer, fee basis, and recognition evidence. Separate advisory fees "
                        "from agency award value, supplier invoices, customer receipts, and "
                        "other amounts the operator does not earn through its own performance.",
                        "The contractor purchases a $20,000 fixed-fee capture and proposal "
                        "engagement covering four accepted deliverables. Its contemplated "
                        "$800,000 agency contract is customer contract value, not desk "
                        "revenue. The desk neither invoices the agency nor takes title to "
                        "supplies; revenue follows completed service obligations under the "
                        "engagement's accounting policy.",
                    ),
                    field(
                        "Offeror eligibility and registration evidence",
                        "textarea",
                        "Identify the actual offeror and list applicable registration, "
                        "size, socioeconomic, vehicle-access, and solicitation eligibility "
                        "requirements. Record supporting documents and verification dates; "
                        "distinguish the offeror's responsibilities from those of an advisory "
                        "firm that merely prepares authorized proposal materials.",
                        "The facilities contractor, not the proposal desk, is the prospective "
                        "prime. Its file includes current SAM.gov registration evidence, "
                        "UEI, exclusion-search results, and a size analysis under the "
                        "solicitation's assigned NAICS code. The client signs representations "
                        "after review; desk staff do not infer eligibility from a "
                        "supplier's marketing badge.",
                    ),
                    field(
                        "Counterparty capability and financial strength",
                        "textarea",
                        "Document relevant past performance, references, staffing availability, "
                        "insurance limits, financial resources, and delivery dependencies. "
                        "Identify who verified each claim and what evidence would invalidate "
                        "the qualification decision before proposal submission or "
                        "subcontract execution.",
                        "A proposed janitorial subcontractor supplies three comparable "
                        "references, a current $2 million liability certificate, and a "
                        "staffing roster supporting two shifts. Its forecast shows $90,000 "
                        "available cash against $60,000 initial payroll and supplies. "
                        "The desk requests insurer confirmation and reference calls before "
                        "using those claims in the proposal.",
                    ),
                    field(
                        "Prime and subcontractor responsibility map",
                        "textarea",
                        "Allocate proposal ownership, agency communication, technical "
                        "performance, staffing supervision, inspection, invoicing, and "
                        "remediation between participants. Identify the actual work each "
                        "party contributes and flag structures that depend on merely "
                        "routing funds through an eligible entity.",
                        "The prime supervises site personnel, owns the quality plan, invoices "
                        "the agency, and resolves performance defects. The subcontractor "
                        "performs the documented evening-cleaning package. The desk prepares "
                        "proposal artifacts for a fixed fee. No participant describes "
                        "introductions, invoice routing, or borrowed certifications as "
                        "substantive contract performance.",
                    ),
                    field(
                        "Opportunity score and mandatory rejection rules",
                        "textarea",
                        "Set weighted commercial criteria separately from mandatory eligibility "
                        "tests. Record evidence behind each score, the minimum pursuit "
                        "threshold, the reviewer, and explicit rejection conditions that "
                        "cannot be offset by estimated award size or relationship enthusiasm.",
                        "The score allocates 25 points to capability, 20 to buyer fit, "
                        "20 to economics, 20 to timing, and 15 to evidence quality. "
                        "A 78-point opportunity clears the 75-point pursuit threshold. "
                        "Missing mandatory certification, unavailable key personnel, "
                        "improper information access, or an impossible submission schedule "
                        "still requires rejection.",
                    ),
                    field(
                        "Competitive position and addressable award value",
                        "textarea",
                        "Summarize incumbent performance, buyer priorities, likely competition, "
                        "and the client's specific differentiator. Distinguish an estimated "
                        "task value from an indefinite-delivery ceiling and describe how "
                        "uncertainty affects pursuit effort rather than inflating service "
                        "revenue projections.",
                        "A vehicle advertises a $10 million aggregate ceiling, but the "
                        "client can credibly service one anticipated $250,000 task order. "
                        "Its differentiator is a staffed local response team with measured "
                        "two-hour dispatch capability. The desk budgets 30 discovery hours "
                        "and does not book either amount as its own revenue.",
                    ),
                    field(
                        "Fee structure and relationship integrity screen",
                        "textarea",
                        "Describe all compensation, referrals, marketing representatives, "
                        "government relationships, and proposed payment triggers. Identify "
                        "whether contingent-fee, procurement-integrity, gratuity, kickback, "
                        "or local lobbying rules require specialist review before any "
                        "commitment, introduction, or proposal work begins.",
                        "The engagement charges $5,000 for each of four documented service "
                        "milestones, regardless of award outcome. A proposed introduction "
                        "payment tied to winning is removed pending review of FAR "
                        "Subpart 3.4 and applicable clauses. Fixed pricing does not "
                        "excuse improper influence, undisclosed conflicts, or "
                        "restricted-information handling.",
                    ),
                    field(
                        "Underwriting decision and next evidence request",
                        "textarea",
                        "Write the pursue, pause, or reject decision with a named owner, "
                        "authorized spending limit, unresolved evidence requests, and "
                        "expiration date. State what must change before a paused "
                        "opportunity can consume proposal-production capacity or client funds.",
                        "The desk authorizes a $1,500 discovery phase, capped at 12 labor "
                        "hours, while the client confirms supervisor availability and "
                        "vehicle access. Proposal production remains paused until those "
                        "documents arrive. The capture lead reviews the file in five "
                        "business days and closes it if eligibility cannot be established.",
                    ),
                ],
                "completion_gate": (
                    "The capture lead and delivery lead sign a dated pursue decision only "
                    "after mandatory eligibility evidence, the client payer, actual work "
                    "allocation, fee structure, and a capped next-step budget are documented."
                ),
            },
            {
                "worksheet_id": "ws-02",
                "number": 2,
                "title": "Service-Fee Economics, Defect Reserve, and Working-Capital Float",
                "purpose": (
                    "Translate the canonical scenarios into recognized service-fee revenue, "
                    "explicit cost budgets, and collection-sensitive cash forecasts. Price "
                    "actual delivery work, quantify proposal defects and supplier exposure, "
                    "and expose staffing affordability problems without substituting "
                    "customer awards or borrowed funds for earned operator revenue."
                ),
                "chapter_ref": "Q3, Q4",
                "instructions": [
                    (
                        "Enter all three canonical scenarios without changing their revenue, "
                        "margin, profit, or staffing figures. Treat them as comparison "
                        "benchmarks rather than verified wage budgets. Build any normalized "
                        "compensation sensitivity separately and label its differences "
                        "from the canonical case."
                    ),
                    (
                        "Create a service-contract volume bridge using completed engagements "
                        "and earned fees. Exclude customer award value, government purchase "
                        "orders payable to clients, and refundable deposits from recognized "
                        "desk revenue. Reconcile cash collections separately from "
                        "performance-based revenue recognition."
                    ),
                    (
                        "Price delivery labor, specialist reviews, software, insurance, "
                        "proposal corrections, collection losses, and subcontract support. "
                        "Explain which costs sit inside recurring core overhead and which "
                        "vary with delivery volume so the monthly overhead range is "
                        "not mistaken for total operating expense."
                    ),
                    (
                        "Build a weekly cash forecast using actual client payment terms, "
                        "deposit treatment, payable dates, and disputed-invoice assumptions. "
                        "Measure the largest cumulative funding deficit, then add a "
                        "documented contingency buffer rather than assuming government "
                        "payment rules protect advisory invoices."
                    ),
                    (
                        "Stress award losses, slower collections, rework, and supplier "
                        "replacement independently before combining them. Record the "
                        "funding response and stop-work authority. Reject any price or "
                        "staffing plan that only works by concealing unpaid labor or "
                        "counting client contract principal as desk revenue."
                    ),
                ],
                "fields": [
                    field(
                        "Canonical scenario reconciliation",
                        "textarea",
                        "Record annual recognized service revenue, net margin, owner net "
                        "profit, implied total expenses, and staffing for Conservative, "
                        "Base, and Scaled cases. Show the arithmetic explicitly and "
                        "retain the canonical values even when additional sensitivities "
                        "reveal operating constraints.",
                        "Conservative: $120,000 revenue less $102,000 expenses equals "
                        "$18,000 owner net profit, or 15%, with 2 FT plus 3 C. "
                        "Base: $560,000 less $434,000 equals $126,000, or 22.5%, "
                        "with 2 FT plus 3 C. Scaled: $1,000,000 less $700,000 "
                        "equals $300,000, or 30%, with 3 FT plus 4 C.",
                    ),
                    field(
                        "Engagement volume and earned-fee bridge",
                        "textarea",
                        "Construct an annual engagement-count and average-fee bridge for "
                        "each canonical revenue case. State the completion and acceptance "
                        "assumptions, identify partial-year work separately, and explain "
                        "why agency awards or supplier sales do not enter this "
                        "service-revenue calculation.",
                        "Conservative assumes 10 completed engagements at $12,000, producing "
                        "$120,000. Base assumes 28 at $20,000, producing $560,000. "
                        "Scaled assumes 40 at $25,000, producing $1,000,000. These "
                        "are earned proposal-service fees, not award commissions. "
                        "Unsigned proposals, incomplete milestones, client contract ceilings, "
                        "and unearned advance payments do not increase these totals.",
                    ),
                    field(
                        "Core overhead and delivery-cost bridge",
                        "textarea",
                        "Reconcile recurring core overhead and delivery-related expenses to "
                        "each scenario's total cost budget. Define the accounting boundary "
                        "for the stated $5,000 to $25,000 monthly operating range and "
                        "prevent double counting of payroll, contractors, reserves, and tools.",
                        "The planning bridge assigns Conservative $60,000 core overhead "
                        "plus $42,000 delivery costs; Base $180,000 plus $254,000; "
                        "Scaled $300,000 plus $400,000. Core overhead therefore runs "
                        "$5,000, $15,000, and $25,000 monthly. Total costs are higher "
                        "because delivery expenses remain separate; each bridge matches "
                        "the canonical implied expense budget exactly.",
                    ),
                    field(
                        "Staffing affordability and compensation sensitivity",
                        "textarea",
                        "Test whether the canonical headcount can be funded at credible "
                        "compensation and utilization levels. Distinguish full-time "
                        "employees, contractor headcount, owner labor, and contractor "
                        "hours. Show any funding gap without silently altering "
                        "canonical owner profit or staffing.",
                        "Conservative's $102,000 total expense budget cannot cover two "
                        "employees costing $65,000 each plus three contractors, tools, "
                        "and insurance. Employee cost alone exceeds that budget by "
                        "$28,000. Preserve the canonical $18,000 result as the benchmark, "
                        "but mark deployment blocked until a fully costed staffing "
                        "sensitivity identifies a funded operating plan.",
                    ),
                    field(
                        "Engagement contribution and delivery-hour budget",
                        "textarea",
                        "Calculate earned fee less variable delivery labor, specialist "
                        "review, rework allowance, and direct software costs for one "
                        "engagement. State planned hours, loaded rates, and contribution "
                        "before allocated overhead; do not label contribution "
                        "as annual owner profit.",
                        "A $20,000 engagement budgets 100 contractor hours at $60, "
                        "$1,500 specialist review, $500 direct tools, and $1,000 "
                        "rework allowance. Total variable cost is $9,000; contribution "
                        "is $11,000, or 55%. Across 28 engagements, $252,000 "
                        "variable cost leaves $2,000 within Base's $254,000 "
                        "delivery-cost pool for additional shared delivery expense.",
                    ),
                    field(
                        "Scrub defects and management reserve",
                        "textarea",
                        "Define recoverable proposal defects, expected correction costs, "
                        "client credits, and escalation thresholds. Separate a management "
                        "cash reserve from an accounting accrual and state where "
                        "expected rework is already included so the scenario "
                        "does not count it twice.",
                        "Base includes $28,000 expected rework inside delivery expense: "
                        "28 engagements multiplied by $1,000. A separate $12,000 "
                        "restricted management cash buffer supports unusually concentrated "
                        "corrections and is not automatically another expense. Each "
                        "incident records omitted requirement, responsible reviewer, "
                        "repair hours, credit decision, and whether an accounting "
                        "adjustment is supported.",
                    ),
                    field(
                        "Invoice schedule and revenue-recognition evidence",
                        "textarea",
                        "Map invoices, cash receipt dates, deliverable acceptance, disputes, "
                        "and earned-revenue evidence. State how advances and incomplete "
                        "work are tracked, identify the client debtor, and avoid "
                        "assuming that payment to the prime automatically "
                        "settles the desk's invoices.",
                        "A $20,000 engagement invoices a $5,000 advance and three "
                        "subsequent $5,000 milestones. The advance remains unearned "
                        "until the first defined service obligation is satisfied. "
                        "Acceptance records support each earned amount. The private "
                        "contractor owes the desk under its service agreement, "
                        "independently of when the government pays that contractor.",
                    ),
                    field(
                        "Startup capital and weekly float requirement",
                        "textarea",
                        "Set starting capital within the canonical startup range and "
                        "forecast weekly collections, payroll, contractor payments, "
                        "fixed overhead, and setup costs. Calculate peak cumulative "
                        "cash deficit and remaining buffer, keeping borrowing "
                        "proceeds separate from revenue.",
                        "The launch uses $120,000 starting capital, within the "
                        "$25,000 to $150,000 range. Setup consumes $18,000. "
                        "A ten-week forecast contains $70,000 outflows and $25,000 "
                        "collections, leaving $57,000 cash: $120,000 less $18,000 "
                        "less $45,000. Reserving $20,000 for contingencies leaves "
                        "$37,000 available above that buffer.",
                    ),
                    field(
                        "Collection delay and supplier-failure stress",
                        "textarea",
                        "Quantify cash effects from delayed invoices and failed delivery "
                        "partners separately from profit effects. State the assumed "
                        "delay, replacement cost, recoverability, expense classification, "
                        "and authority to pause additional work before liquidity "
                        "falls below the operating buffer.",
                        "If $20,000 of planned ten-week collections slips beyond "
                        "the forecast, ending cash falls from $57,000 to $37,000. "
                        "An unrecoverable $8,000 replacement-specialist charge reduces "
                        "cash to $29,000 and reduces profit if outside budget. "
                        "The payment delay alone changes timing, not earned "
                        "revenue, unless collectability evidence requires adjustment.",
                    ),
                    field(
                        "Economic decision and funding commitments",
                        "textarea",
                        "State the accepted pricing floor, capital source, collection "
                        "assumptions, budget owner, and conditions for adding capacity. "
                        "Identify which scenario is being pursued and distinguish "
                        "an annual steady-state model from first-year timing "
                        "and cash availability.",
                        "Management pursues Base as a steady-state target, not a "
                        "promise of first-year collections. The expected first-deal "
                        "window remains 6 to 18 months. Pricing below $20,000 "
                        "requires a revised hour budget. Additional contractor hours "
                        "require signed client scope and a forecast retaining "
                        "at least $20,000 unrestricted operating cash.",
                    ),
                ],
                "completion_gate": (
                    "The finance owner reconciles all three canonical scenarios, verifies "
                    "that only earned service fees enter revenue, documents the Conservative "
                    "staffing affordability gap, and signs a weekly cash forecast with "
                    "funded reserves and explicit stop-work thresholds."
                ),
            },
            {
                "worksheet_id": "ws-03",
                "number": 3,
                "title": "Execution Ledger and Technical QA Pre-Flight",
                "purpose": (
                    "Turn each qualified opportunity into a controlled production record "
                    "from intake through collection. Preserve amendment lineage, "
                    "requirement traceability, authorized representations, submission "
                    "receipts, and service acceptance so a second operator can reconstruct "
                    "what happened without relying on email memory or verbal assurances."
                ),
                "chapter_ref": "Q7, Q8",
                "instructions": [
                    (
                        "Open one engagement record before production starts. Link the "
                        "signed scope, client authority, solicitation snapshot, deadline, "
                        "delivery budget, and responsible staff. Use consistent identifiers "
                        "across the bid calendar, document repository, time records, "
                        "invoice register, and defect log."
                    ),
                    (
                        "Translate every mandatory solicitation instruction into a "
                        "requirement matrix with source page, response location, evidence, "
                        "owner, and review state. Review amendments against that matrix "
                        "rather than assuming the original downloaded package remains "
                        "sufficient for a timely submission."
                    ),
                    (
                        "Separate drafting, technical validation, pricing review, client "
                        "certification, and submission authority. Require the actual "
                        "offeror to approve representations and binding commitments. "
                        "A proposal-services contract does not itself authorize the "
                        "desk to certify eligibility or bind its client."
                    ),
                    (
                        "Run content, arithmetic, accessibility, file-format, and portal "
                        "checks against the actual solicitation instructions. Preserve "
                        "test evidence and corrections. Use an internal deadline that "
                        "leaves time for recovery without assuming the agency "
                        "will accept a late proposal."
                    ),
                    (
                        "Close the engagement only after recording receipt evidence, "
                        "client acceptance, earned fees, outstanding invoices, and "
                        "remaining obligations. Capture award outcomes separately from "
                        "service completion so an unsuccessful client bid does "
                        "not erase completed delivery history or distort conversion metrics."
                    ),
                ],
                "fields": [
                    field(
                        "Engagement record and document architecture",
                        "textarea",
                        "Define the engagement identifier, repository structure, record "
                        "owners, access groups, and cross-system keys. Describe how "
                        "source documents, working drafts, signed approvals, submission "
                        "packages, and financial records remain distinguishable "
                        "throughout the delivery lifecycle.",
                        "ENG-020-014 links the service agreement, opportunity record, "
                        "requirements matrix, labor ledger, and invoice series. "
                        "SharePoint separates source snapshots, drafts, approved "
                        "release files, and receipts. Only the release manager "
                        "can modify the final-package folder; client viewers "
                        "receive access to their engagement rather than the "
                        "desk's entire customer repository.",
                    ),
                    field(
                        "Solicitation baseline and amendment ledger",
                        "textarea",
                        "Record each source download, amendment identifier, retrieval "
                        "timestamp, content hash, reviewer, and resulting change. "
                        "Specify who checks authoritative sources and how altered "
                        "deadlines, quantities, clauses, or response formats "
                        "propagate to production tasks.",
                        "The baseline archive contains the solicitation PDF and "
                        "attachments with SHA-256 hashes. Amendment 0002 changes "
                        "the staffing schedule and requires acknowledgment. The "
                        "coordinator logs both changes, assigns the staffing "
                        "revision to the technical writer, and adds amendment "
                        "acknowledgment to the final checklist before releasing "
                        "the next proposal version.",
                    ),
                    field(
                        "Requirement traceability and evidence matrix",
                        "textarea",
                        "Specify how every mandatory instruction connects to a "
                        "response section, supporting evidence, accountable owner, "
                        "and independent check. Include page limits, forms, "
                        "pricing schedules, representations, attachment names, "
                        "and submission methods rather than tracking narrative "
                        "requirements alone.",
                        "Requirement R-017 cites Section L, paragraph 4, and "
                        "requires three comparable projects within five years. "
                        "The matrix points to Technical Volume pages 8 through "
                        "10 and three reference letters. A separate R-018 "
                        "tracks the 20-page limit; the reviewer confirms "
                        "appendices are treated exactly as the solicitation directs.",
                    ),
                    field(
                        "Production schedule and responsibility assignment",
                        "textarea",
                        "Set a backward schedule from the official deadline with "
                        "named owners for discovery, drafting, pricing, technical "
                        "review, client authorization, and upload. Quantify slack "
                        "and state escalation rules when dependencies "
                        "threaten the internal completion date.",
                        "For a Friday 2:00 p.m. Eastern deadline, technical "
                        "content freezes Tuesday noon, pricing Wednesday noon, "
                        "and client authorization Thursday 10:00 a.m. The "
                        "release target is Thursday 2:00 p.m. A missing "
                        "client signature at Thursday noon triggers immediate "
                        "escalation; staff cannot fabricate authorization "
                        "to preserve the schedule.",
                    ),
                    field(
                        "Price schedule and numerical QA",
                        "textarea",
                        "Describe independent checks for quantities, unit prices, "
                        "extensions, option periods, rounding, and consistency "
                        "between narrative staffing and price schedules. Separate "
                        "the client's proposed agency price from the "
                        "desk's service invoice and expense budget.",
                        "The client's schedule includes 12 monthly units at "
                        "$18,500, totaling $222,000 for the base period. "
                        "The reviewer recalculates every extension and confirms "
                        "option-year totals use their own stated prices. "
                        "The desk's $20,000 proposal fee appears only in "
                        "its client engagement ledger, not as operator "
                        "revenue of $222,000.",
                    ),
                    field(
                        "File package and portal pre-flight",
                        "textarea",
                        "List required formats, filenames, size limits, signature "
                        "requirements, redaction checks, malware scanning, and "
                        "portal credentials. Describe a safe rehearsal using "
                        "authorized accounts and record how final files "
                        "are distinguished from obsolete drafts.",
                        "The release checklist requires searchable PDF files, "
                        "the buyer's specified volume names, visible signatures "
                        "where required, and no tracked changes. A reviewer "
                        "opens each exported file and checks page counts. "
                        "The authorized submitter verifies portal access "
                        "two days early and confirms final package "
                        "hashes against the release manifest.",
                    ),
                    field(
                        "Client representations and submission authority",
                        "textarea",
                        "Identify the person authorized to bind the offeror, "
                        "the representations requiring their review, and "
                        "the desk's delegated submission permissions. Record "
                        "written approval of final content and prohibit "
                        "silent substitutions after that approval.",
                        "The client's managing officer approves pricing, "
                        "certifications, and the final technical volume "
                        "through a dated authorization email linked to "
                        "the release manifest. The desk may upload "
                        "the approved package but cannot change personnel "
                        "commitments or sign size representations. Any "
                        "substantive correction requires renewed "
                        "client authorization before release.",
                    ),
                    field(
                        "Submission receipt and incident recovery",
                        "textarea",
                        "Record submission timestamp, portal confirmation, file "
                        "list, submitter, and receipt location. Define "
                        "recovery actions for outages or rejected files "
                        "using solicitation-authorized channels, and "
                        "document late-submission risk without presuming "
                        "an exception will apply.",
                        "The training receipt records Thursday 1:42 p.m. "
                        "Eastern and lists three accepted files with "
                        "their hashes. If the portal rejects a file, "
                        "the submitter captures the error and promptly "
                        "contacts the designated contracting channel. "
                        "An alternate email submission is used only "
                        "if authorized; an outage screenshot alone "
                        "does not establish timely receipt.",
                    ),
                    field(
                        "Service ledger and invoice reconciliation",
                        "textarea",
                        "Connect time entries, contractor bills, milestone "
                        "acceptance, recognized revenue, invoices, and "
                        "collections for the engagement. Explain how "
                        "staff resolve mismatches and preserve the "
                        "difference between cash received and "
                        "services actually earned.",
                        "ENG-020-014 records $20,000 earned fees, $9,000 "
                        "direct delivery cost, $15,000 collected, and "
                        "$5,000 accounts receivable after final acceptance. "
                        "A $600 contractor invoice is already inside "
                        "the $9,000 cost total. The bookkeeper checks "
                        "that it was not also posted through "
                        "a duplicate card transaction before closing "
                        "the monthly ledger.",
                    ),
                    field(
                        "Defect closure and after-action record",
                        "textarea",
                        "Define defect severity, corrective owner, root "
                        "cause, client notification, cost impact, and "
                        "verification evidence. Separate proposal quality "
                        "from award outcome and specify how "
                        "lessons update templates without exposing "
                        "another customer's confidential materials.",
                        "A missing amendment acknowledgment is classified "
                        "as a critical pre-submission defect and "
                        "corrected before upload. The incident consumes "
                        "four hours at $60, or $240, against "
                        "the rework budget. The template gains "
                        "an amendment ledger checkpoint, but the "
                        "client's technical narrative is excluded "
                        "from reusable training examples.",
                    ),
                ],
                "completion_gate": (
                    "An independent reviewer signs the requirement matrix, numerical checks, "
                    "release manifest, client authorization, and receipt record; the finance "
                    "owner reconciles earned fees, delivery costs, collections, and unresolved "
                    "defects before engagement closure."
                ),
            },
            {
                "worksheet_id": "ws-04",
                "number": 4,
                "title": "Statutory, Contract, Licensing, and Outreach Audit",
                "purpose": (
                    "Identify the rules actually governing each federal or municipal "
                    "engagement and translate them into concrete operating controls. "
                    "Review compensation, information handling, teaming, eligibility, "
                    "licensing, communications, and contract clauses before staff "
                    "make representations, exchange sensitive material, or commit "
                    "the client to performance."
                ),
                "chapter_ref": "Q5, Q9",
                "instructions": [
                    (
                        "Build a jurisdiction and clause register from the actual "
                        "solicitation, incorporated provisions, proposed agreements, "
                        "and official procurement code. Federal rules do not "
                        "automatically replace municipal requirements, and a "
                        "general clause checklist does not establish which "
                        "terms govern a particular engagement."
                    ),
                    (
                        "Examine how every participant is paid and what "
                        "they actually do. Escalate award-linked compensation, "
                        "gifts, referral arrangements, former-official involvement, "
                        "and access to restricted information before "
                        "contact or contracting activity proceeds; document "
                        "the specific rule and proposed corrective action."
                    ),
                    (
                        "Review prime and subcontract structures against "
                        "applicable performance, size, socioeconomic, "
                        "nonmanufacturer, and excessive-pass-through requirements. "
                        "Collect evidence of real managerial and "
                        "technical contribution rather than treating "
                        "certifications or invoice routing as sufficient "
                        "support for an eligible arrangement."
                    ),
                    (
                        "Map outreach, data storage, and security "
                        "requirements to the actual communication channel "
                        "and information classification. Use only "
                        "authorized accounts and approved repositories. "
                        "Check solicitation-specific restrictions before "
                        "sending agency contacts marketing messages "
                        "or uploading client material into external services."
                    ),
                    (
                        "Write remediation actions with responsible "
                        "owners, evidence requirements, and deadlines. "
                        "A specialist's review should resolve "
                        "a defined question, not substitute "
                        "for collecting underlying facts. Keep "
                        "unresolved structural issues visible and "
                        "pause affected work until "
                        "the documented resolution supports proceeding."
                    ),
                ],
                "fields": [
                    field(
                        "Jurisdiction and applicable-clause register",
                        "textarea",
                        "Identify the purchasing jurisdiction, contract "
                        "type, solicitation provisions, incorporated "
                        "clauses, and subcontract flowdowns. Record "
                        "the authoritative text and effective "
                        "version, distinguishing mandatory obligations "
                        "from terms that apply only "
                        "when included or triggered.",
                        "The federal file records FAR provisions "
                        "actually incorporated by the solicitation "
                        "and separately reviews proposed subcontract "
                        "flowdowns. The municipal file records "
                        "the city's purchasing rules and "
                        "solicitation instructions. For a New "
                        "York City pursuit, the reviewer "
                        "checks applicable Procurement Policy "
                        "Board rules and Administrative Code "
                        "Section 6-129 requirements rather "
                        "than importing federal assumptions.",
                    ),
                    field(
                        "Contingent-fee and selling-agency analysis",
                        "textarea",
                        "Document all fees, award-linked triggers, "
                        "referral payments, and intermediary duties. "
                        "Review FAR Subpart 3.4 and "
                        "FAR 52.203-5 when applicable, "
                        "including the defined bona fide "
                        "employee or agency exception "
                        "rather than assuming every "
                        "commission is permissible.",
                        "A proposed 3% award-success fee "
                        "on an $800,000 contract would "
                        "create $24,000 contingent compensation. "
                        "The desk suspends that arrangement "
                        "for fact-specific review and "
                        "instead proposes separately priced, "
                        "documented service milestones. A "
                        "fixed fee is not a "
                        "safe harbor for improper "
                        "influence; actual conduct and "
                        "applicable contractual restrictions "
                        "remain part of the analysis.",
                    ),
                    field(
                        "Procurement integrity and restricted information",
                        "textarea",
                        "Assess access to bid, proposal, "
                        "source-selection, and other restricted "
                        "procurement information under 41 "
                        "U.S.C. Sections 2101 through "
                        "2107 and FAR 3.104. "
                        "Record former-official relationships, "
                        "information provenance, access "
                        "restrictions, and escalation procedures.",
                        "A contact offers an unreleased "
                        "competitor pricing spreadsheet. The "
                        "desk stops review, restricts "
                        "access, preserves an incident "
                        "record, and obtains counsel "
                        "direction on notification and "
                        "handling. The pursuit model "
                        "continues using public notices "
                        "and authorized client materials; "
                        "the offered spreadsheet is "
                        "excluded from pricing, strategy, "
                        "and automated research inputs.",
                    ),
                    field(
                        "Kickbacks, gifts, conflicts, and referral controls",
                        "textarea",
                        "Identify payments or benefits involving "
                        "prime personnel, subcontractors, agency "
                        "staff, referral sources, and "
                        "related parties. Review 41 "
                        "U.S.C. Sections 8701 through "
                        "8707, applicable FAR provisions, "
                        "and local ethics rules "
                        "against the actual relationship.",
                        "A supplier proposes a $2,000 "
                        "personal referral payment to "
                        "the prime's purchasing manager "
                        "for subcontract selection. The "
                        "desk rejects the arrangement "
                        "and records the incident "
                        "for review. Legitimate subcontract "
                        "pricing must describe delivered "
                        "work and flow through "
                        "authorized company accounts, not "
                        "concealed benefits to "
                        "procurement decision-makers.",
                    ),
                    field(
                        "Set-aside performance and nonmanufacturer review",
                        "textarea",
                        "Evaluate the solicitation's eligibility "
                        "requirements and actual performance "
                        "allocation under 13 CFR "
                        "125.6, applicable FAR 52.219-14 "
                        "terms, and 13 CFR "
                        "121.406 for covered supply "
                        "arrangements. Identify similarly "
                        "situated entities and "
                        "applicable calculation exclusions.",
                        "For a covered services award "
                        "with a simplified $400,000 "
                        "payment base and no "
                        "applicable exclusions, a plan "
                        "to pay $240,000 to "
                        "non-similarly situated subcontractors "
                        "exceeds the 50% limit. "
                        "The prime revises genuine "
                        "performance allocation before "
                        "offering. A supply pursuit "
                        "requires a separate nonmanufacturer "
                        "analysis rather than recycling "
                        "the services calculation.",
                    ),
                    field(
                        "Pass-through value and teaming agreement terms",
                        "textarea",
                        "Describe each party's substantive "
                        "contribution, subcontract percentage, "
                        "management responsibilities, and "
                        "pricing support. Review FAR "
                        "52.215-22 and 52.215-23 "
                        "when applicable, plus teaming "
                        "terms for exclusivity, confidentiality, "
                        "workshare, termination, and "
                        "award-dependent obligations.",
                        "The prime expects to subcontract "
                        "75% of total performance "
                        "cost. Where FAR 52.215-22 "
                        "applies, it supplies the "
                        "required explanation of added "
                        "value rather than treating "
                        "70% as a universal "
                        "prohibition. Its evidence covers "
                        "program management, integration, "
                        "quality oversight, and risk "
                        "ownership; unexplained invoice "
                        "routing does not establish "
                        "that value.",
                    ),
                    field(
                        "Licensing, bonding, insurance, and registrations",
                        "textarea",
                        "Identify licenses, permits, bonds, "
                        "insurance, business registrations, "
                        "and lobbying registrations "
                        "triggered by actual work "
                        "and jurisdiction. Assign "
                        "each requirement to the "
                        "responsible entity and verify "
                        "coverage dates, limits, "
                        "endorsements, and renewal ownership.",
                        "The desk performs proposal "
                        "services and does not "
                        "claim its client’s electrical "
                        "contractor license. A municipal "
                        "installation pursuit requires "
                        "the performing contractor's "
                        "applicable trade license and "
                        "the solicitation's bond "
                        "evidence. The register "
                        "identifies the issuing "
                        "authority, license number, "
                        "expiration date, and reviewer "
                        "before any licensed capability "
                        "appears in proposal text.",
                    ),
                    field(
                        "Truthful certifications and invoice support",
                        "textarea",
                        "List certifications, performance claims, "
                        "cost representations, and invoice "
                        "statements requiring evidence. "
                        "Address False Claims Act "
                        "exposure under 31 U.S.C. "
                        "Sections 3729 through "
                        "3733 and define review "
                        "controls preventing fabricated "
                        "or recklessly unsupported submissions.",
                        "A draft claims five completed "
                        "agency projects, but records "
                        "support only three projects "
                        "and two unrelated commercial "
                        "jobs. The writer corrects "
                        "the narrative and obtains "
                        "client approval. Service invoices "
                        "attach milestone acceptance "
                        "and actual scope references; "
                        "staff cannot relabel unperformed "
                        "tasks as delivered merely "
                        "to accelerate cash collection.",
                    ),
                    field(
                        "Information security and external-service restrictions",
                        "textarea",
                        "Classify solicitation and client "
                        "information, identify contractual "
                        "security requirements, and "
                        "record approved storage, "
                        "sharing, incident handling, "
                        "and retention controls. "
                        "Review FAR 52.204-21 "
                        "and applicable defense "
                        "requirements only where "
                        "the information and clauses "
                        "make them relevant.",
                        "Public notices may enter "
                        "the research queue, while "
                        "client pricing stays in "
                        "a restricted repository with "
                        "multifactor authentication and "
                        "access logs. If a "
                        "defense subcontract carries "
                        "DFARS 252.204-7012 and "
                        "covered information, the "
                        "security owner evaluates "
                        "the applicable NIST SP "
                        "800-171 requirements before "
                        "acceptance. External drafting "
                        "services receive no "
                        "restricted client content.",
                    ),
                    field(
                        "Outreach restrictions and remediation sign-off",
                        "textarea",
                        "Document lawful prospecting channels, "
                        "agency communication restrictions, "
                        "opt-out processing, and "
                        "specialist review actions. "
                        "Address 15 U.S.C. "
                        "Section 7704 for "
                        "commercial email and "
                        "47 U.S.C. Section "
                        "227 where telephone "
                        "or text practices "
                        "trigger its requirements.",
                        "The desk sends targeted "
                        "business email with accurate "
                        "sender identity, a postal "
                        "address, and a working "
                        "opt-out process honoring "
                        "requests within ten "
                        "business days. Automated "
                        "calling remains disabled "
                        "pending channel-specific review. "
                        "Solicitation questions use "
                        "only the designated "
                        "contracting channel; the "
                        "audit owner records "
                        "evidence closing each "
                        "communication-related remediation item.",
                    ),
                ],
                "completion_gate": (
                    "The responsible specialist and operating owner resolve every "
                    "material compensation, eligibility, information, licensing, "
                    "contract, and outreach issue in writing; unresolved prohibited "
                    "structures remain excluded from the pursuit and delivery pipeline."
                ),
            },
            {
                "worksheet_id": "ws-05",
                "number": 5,
                "title": "Automation, Growth Flywheel, and Risk Fallback Tracker",
                "purpose": (
                    "Automate public-notice intake, bid calendars, and requirement "
                    "checklists while preserving source evidence and human "
                    "accountability. Build a narrow, measurable acquisition system "
                    "for qualified service clients, with explicit fallbacks "
                    "for missed notices, calendar errors, supplier failures, "
                    "security incidents, and payment delays."
                ),
                "chapter_ref": "Q6, Q10",
                "instructions": [
                    (
                        "Define the manual process before automating "
                        "it. Identify authoritative inputs, expected "
                        "outputs, accountable owners, and evidence "
                        "needed to detect failure. Use "
                        "public data and client-authorized "
                        "resources only; automation credentials "
                        "do not expand contractual "
                        "authority or information access."
                    ),
                    (
                        "Configure solicitation alerts around a "
                        "single vertical, geography, and "
                        "capability profile. Track duplicate "
                        "notices, amendments, cancellations, and "
                        "source freshness. Test filtering "
                        "against a manually reviewed "
                        "sample so a narrow "
                        "search does not silently "
                        "discard qualified opportunities."
                    ),
                    (
                        "Route deadlines and extracted "
                        "requirements into a review "
                        "queue rather than directly "
                        "making binding commitments. "
                        "Require a second person "
                        "to verify critical dates, "
                        "time zones, representations, "
                        "and pricing instructions "
                        "against the authoritative "
                        "solicitation before production "
                        "or submission depends "
                        "on those values."
                    ),
                    (
                        "Build growth around documented "
                        "client fit, useful procurement "
                        "insights, and repeat "
                        "delivery quality. Separate "
                        "prospecting consent and "
                        "channel requirements from "
                        "agency procurement communications. "
                        "Measure signed service "
                        "engagements and collected "
                        "fees rather than "
                        "celebrating unqualified contact "
                        "volume or advertised "
                        "award ceilings."
                    ),
                    (
                        "Assign a fallback owner "
                        "and recovery target "
                        "for every critical "
                        "automation. Rehearse source "
                        "outages, missed amendments, "
                        "staff absence, failed "
                        "suppliers, and overdue "
                        "invoices using synthetic "
                        "records. Preserve incident "
                        "evidence and update "
                        "the operating checklist "
                        "after each recovery exercise."
                    ),
                ],
                "fields": [
                    field(
                        "Authorized source inventory and intake schedule",
                        "textarea",
                        "List public procurement sources, "
                        "authorized APIs or "
                        "exports, access owners, "
                        "refresh schedules, usage "
                        "limits, and source "
                        "retention requirements. "
                        "Describe how the "
                        "desk handles unavailable "
                        "sources without assuming "
                        "silence means no "
                        "new opportunities exist.",
                        "SAM.gov saved searches "
                        "and permitted API "
                        "access support federal "
                        "intake; municipal portals "
                        "use their available "
                        "alerts or authorized "
                        "exports. The coordinator "
                        "reviews intake each "
                        "business morning and "
                        "logs refresh failures. "
                        "An unavailable feed "
                        "creates a manual "
                        "portal-check task rather "
                        "than an empty "
                        "report claiming the "
                        "market contains zero "
                        "relevant notices.",
                    ),
                    field(
                        "Filtering, deduplication, and amendment logic",
                        "textarea",
                        "Define matching criteria, "
                        "stable record keys, "
                        "duplicate handling, "
                        "amendment linkage, "
                        "cancellation treatment, "
                        "and false-negative "
                        "testing. Include "
                        "a review path "
                        "for records whose "
                        "classification or "
                        "delivery requirements "
                        "cannot be determined "
                        "reliably by automation.",
                        "The filter combines "
                        "target NAICS categories, "
                        "facilities keywords, "
                        "delivery location, "
                        "and response window. "
                        "Notice identifier plus "
                        "source distinguishes records; "
                        "amendments attach to "
                        "the original opportunity. "
                        "A weekly sample "
                        "of 20 rejected "
                        "notices tests exclusions. "
                        "If two are "
                        "actually relevant, the "
                        "owner revises the "
                        "rule and reprocesses "
                        "the affected intake period.",
                    ),
                    field(
                        "Bid-calendar synchronization and deadline controls",
                        "textarea",
                        "Specify the source "
                        "of deadline truth, "
                        "time-zone handling, "
                        "calendar synchronization, "
                        "review responsibilities, "
                        "reminders, and "
                        "change notifications. "
                        "Define how staff "
                        "recover when an "
                        "amendment changes "
                        "a deadline after "
                        "internal production "
                        "tasks have "
                        "already been assigned.",
                        "The opportunity register "
                        "stores the agency's "
                        "deadline text and "
                        "an independently checked "
                        "UTC conversion. Outlook "
                        "receives the official "
                        "deadline plus internal "
                        "checkpoints at 72 "
                        "and 24 hours. "
                        "A changed source "
                        "date requires coordinator "
                        "verification, calendar updates, "
                        "and explicit acknowledgment "
                        "from the writer "
                        "and release manager "
                        "before old reminders "
                        "are retired.",
                    ),
                    field(
                        "Checklist extraction and human verification",
                        "textarea",
                        "Describe which requirements "
                        "automation may extract, "
                        "how source citations "
                        "are retained, and "
                        "which decisions remain "
                        "with qualified reviewers. "
                        "Define sampling, "
                        "error severity, "
                        "version control, "
                        "and handling "
                        "of low-confidence "
                        "or conflicting "
                        "extracted instructions.",
                        "A local parser "
                        "suggests page limits, "
                        "required forms, and "
                        "attachment names while "
                        "retaining page references. "
                        "The reviewer compares "
                        "every mandatory requirement "
                        "with the solicitation. "
                        "A conflict between "
                        "an attachment and "
                        "amendment becomes a "
                        "question for the "
                        "authorized contracting channel; "
                        "the parser cannot "
                        "choose a convenient "
                        "interpretation and mark "
                        "the requirement resolved.",
                    ),
                    field(
                        "Client profile and outbound message evidence",
                        "textarea",
                        "Define the ideal "
                        "client's delivery "
                        "capability, size, "
                        "geography, purchasing "
                        "authority, and "
                        "procurement readiness. "
                        "Specify evidence "
                        "supporting personalized "
                        "outreach and "
                        "prohibit claims "
                        "of guaranteed "
                        "awards, privileged "
                        "agency access, "
                        "or unsupported "
                        "certification eligibility.",
                        "The desk targets "
                        "established facilities "
                        "contractors with "
                        "documented supervisors, "
                        "commercial references, "
                        "and capacity "
                        "for public "
                        "work. Outreach "
                        "references one "
                        "publicly posted "
                        "buying pattern "
                        "and offers "
                        "a fixed-scope "
                        "readiness review. "
                        "The message "
                        "does not "
                        "claim influence "
                        "over selection "
                        "or state "
                        "that hiring "
                        "the desk "
                        "will secure "
                        "an agency award.",
                    ),
                    field(
                        "Growth funnel and acquisition-cost ledger",
                        "textarea",
                        "Track targeted contacts, "
                        "qualified conversations, "
                        "diagnostics, proposals, "
                        "signed engagements, "
                        "earned fees, "
                        "and acquisition "
                        "cost by "
                        "cohort. Separate "
                        "pipeline estimates "
                        "from recognized "
                        "revenue and "
                        "show the "
                        "time lag "
                        "between outreach "
                        "and actual "
                        "client conversion.",
                        "A planning cohort "
                        "of 100 "
                        "targeted contacts "
                        "produces 20 "
                        "conversations, eight "
                        "diagnostics, four "
                        "service proposals, "
                        "and two "
                        "signed engagements. "
                        "With $3,000 "
                        "acquisition spending, "
                        "cost per "
                        "signed client "
                        "is $1,500. "
                        "Two $20,000 "
                        "contracts represent "
                        "$40,000 contracted "
                        "fees, but "
                        "revenue follows "
                        "delivered obligations, "
                        "not signature "
                        "or outreach activity.",
                    ),
                    field(
                        "Retention, referrals, and reusable knowledge",
                        "textarea",
                        "Design a repeat "
                        "engagement and "
                        "referral process "
                        "based on "
                        "documented service "
                        "quality. Identify "
                        "reusable public "
                        "research and "
                        "generic templates, "
                        "while excluding "
                        "customer confidential "
                        "content, improper "
                        "referral compensation, "
                        "and unsupported "
                        "award attribution.",
                        "After accepted "
                        "delivery, the "
                        "account lead "
                        "offers a "
                        "$2,000 monthly "
                        "monitoring service "
                        "with defined "
                        "notice reviews "
                        "and calendar "
                        "maintenance. These "
                        "fees require "
                        "a separate "
                        "revenue bridge "
                        "before inclusion "
                        "in a "
                        "scenario. Reusable "
                        "assets contain "
                        "public-source research "
                        "and blank "
                        "checklists, never "
                        "another client's "
                        "pricing or "
                        "technical approach.",
                    ),
                    field(
                        "Access control, audit events, and data minimization",
                        "textarea",
                        "Identify service "
                        "accounts, least-privilege "
                        "permissions, credential "
                        "storage, logging, "
                        "retention, and "
                        "access revocation. "
                        "Specify which "
                        "data may "
                        "enter each "
                        "automation and "
                        "how operators "
                        "detect unauthorized "
                        "exports or "
                        "accidental cross-client "
                        "document access.",
                        "The alert "
                        "integration reads "
                        "public notices "
                        "and writes "
                        "only to "
                        "the intake "
                        "queue. It "
                        "cannot access "
                        "client proposal "
                        "folders or "
                        "submit bids. "
                        "Credentials reside "
                        "in an "
                        "approved password "
                        "manager; access "
                        "reviews occur "
                        "monthly. A "
                        "departing contractor's "
                        "account is "
                        "disabled immediately "
                        "and active "
                        "sharing links "
                        "are reviewed "
                        "for continued need.",
                    ),
                    field(
                        "Risk triggers and manual fallback ownership",
                        "textarea",
                        "Assign measurable "
                        "triggers and "
                        "fallback actions "
                        "for source "
                        "outages, missed "
                        "amendments, unavailable "
                        "staff, supplier "
                        "failure, and "
                        "payment delays. "
                        "Record who "
                        "may pause "
                        "work, spend "
                        "contingency funds, "
                        "notify clients, "
                        "and restore "
                        "normal operations.",
                        "A source "
                        "refresh older "
                        "than 24 "
                        "hours triggers "
                        "manual review. "
                        "An overdue "
                        "client invoice "
                        "at day "
                        "15 triggers "
                        "account-lead escalation "
                        "and discretionary "
                        "work suspension "
                        "under the "
                        "agreement. A "
                        "failed reviewer "
                        "activates the "
                        "qualified backup, "
                        "with replacement "
                        "spending capped "
                        "at $2,000 "
                        "until the "
                        "delivery lead "
                        "authorizes more.",
                    ),
                    field(
                        "Automation acceptance test and recovery drill",
                        "textarea",
                        "Define a "
                        "synthetic test "
                        "set, expected "
                        "outputs, failure "
                        "criteria, reviewer "
                        "sign-off, and "
                        "recovery-time target. "
                        "Record actual "
                        "test results "
                        "rather than "
                        "assuming configured "
                        "alerts, exports, "
                        "or calendar "
                        "rules operate "
                        "correctly in "
                        "production.",
                        "The drill "
                        "uses ten "
                        "synthetic notices: "
                        "six relevant, "
                        "two duplicates, "
                        "one cancellation, "
                        "and one "
                        "deadline amendment. "
                        "Acceptance requires "
                        "correct linkage "
                        "and no "
                        "missed critical "
                        "change. The "
                        "owner then "
                        "disables the "
                        "feed and "
                        "demonstrates manual "
                        "intake within "
                        "four hours. "
                        "This is "
                        "a planned "
                        "test case; "
                        "results remain "
                        "to be "
                        "recorded after "
                        "execution.",
                    ),
                ],
                "completion_gate": (
                    "The automation owner records successful synthetic tests and a "
                    "manual recovery drill; the growth owner verifies prospecting "
                    "controls, cohort economics, authorized data use, and named "
                    "fallback coverage before production reliance."
                ),
            },
            {
                "worksheet_id": "ws-06",
                "number": 6,
                "title": "30-Day Launch, Pod KPI Scorecard, and Exit-Readiness Ledger",
                "purpose": (
                    "Launch a disciplined procurement-services desk without confusing "
                    "thirty days of setup with the canonical six-to-eighteen-month "
                    "first-deal window. Establish accountable pod roles, evidence-based "
                    "performance measures, capital milestones, transferable records, "
                    "and a realistic continuation decision grounded in "
                    "service economics and operating capacity."
                ),
                "chapter_ref": "Q11, Q12",
                "instructions": [
                    (
                        "Define the thirty-day deliverable "
                        "as a functioning, tested "
                        "service operation with "
                        "qualified pipeline evidence. "
                        "Do not require an "
                        "agency award or "
                        "pretend early prospecting "
                        "activity is recognized "
                        "revenue. Preserve the "
                        "canonical first-deal timing "
                        "when planning cash runway "
                        "and owner commitments."
                    ),
                    (
                        "Allocate weekly work "
                        "to named pod "
                        "roles and specialists. "
                        "Identify actual available "
                        "hours, funded compensation, "
                        "backup coverage, and "
                        "decision rights. Compare "
                        "the practical staffing "
                        "plan with the "
                        "canonical two-full-time, "
                        "three-contractor benchmark "
                        "rather than concealing "
                        "a shortfall through "
                        "unpriced owner labor."
                    ),
                    (
                        "Set launch spending "
                        "limits and measurable "
                        "weekly outputs before "
                        "purchasing software or "
                        "hiring delivery capacity. "
                        "Track evidence produced, "
                        "not just tasks "
                        "marked complete. Review "
                        "runway after each "
                        "week using actual "
                        "cash movements and "
                        "updated collection assumptions."
                    ),
                    (
                        "Maintain a pod "
                        "scorecard covering "
                        "qualification accuracy, "
                        "submission quality, "
                        "delivery hours, "
                        "rework, collections, "
                        "client concentration, "
                        "and qualified "
                        "pipeline. Assign "
                        "every metric "
                        "a denominator, "
                        "measurement window, "
                        "data source, "
                        "and corrective "
                        "owner so "
                        "the dashboard "
                        "supports decisions "
                        "rather than "
                        "decorative reporting."
                    ),
                    (
                        "Create transferable "
                        "operating records "
                        "from the "
                        "first engagement. "
                        "Separate client "
                        "confidentiality, contract "
                        "assignment, government "
                        "novation, security "
                        "access, and "
                        "owner knowledge "
                        "dependencies. At "
                        "day thirty, "
                        "make a "
                        "documented continue, "
                        "narrow, or "
                        "pause decision "
                        "using evidence "
                        "and funded "
                        "next-period commitments."
                    ),
                ],
                "fields": [
                    field(
                        "Launch thesis and canonical positioning",
                        "textarea",
                        "State the "
                        "selected vertical, "
                        "operator role, "
                        "initial service, "
                        "capital commitment, "
                        "and canonical "
                        "positioning. Record "
                        "the score "
                        "and component "
                        "scores accurately, "
                        "while separating "
                        "the series "
                        "ranking from "
                        "your own "
                        "opportunity-level "
                        "pursuit criteria.",
                        "Volume 020 "
                        "covers Candidate "
                        "#4, Government "
                        "Contract Brokering, "
                        "ranked #20 "
                        "of 29. "
                        "Its 70/100 "
                        "score comprises "
                        "22 revenue, "
                        "16 margin, "
                        "14 team "
                        "efficiency, eight "
                        "startup accessibility, "
                        "and ten "
                        "automation points. "
                        "The launch "
                        "positions a "
                        "facilities bid "
                        "desk as "
                        "a Disciplined "
                        "Specialist Play "
                        "with $120,000 "
                        "committed starting capital.",
                    ),
                    field(
                        "Days 1 through 7: foundation sprint",
                        "textarea",
                        "List first-week "
                        "deliverables, accountable "
                        "owners, spending "
                        "limits, and "
                        "evidence of "
                        "completion. Prioritize "
                        "vertical selection, "
                        "service boundaries, "
                        "contract terms, "
                        "source inventory, "
                        "budget controls, "
                        "and secure "
                        "document handling "
                        "before broad "
                        "prospecting or "
                        "client production.",
                        "Week one "
                        "allocates $4,000 "
                        "to specialist "
                        "contract review "
                        "and essential "
                        "setup. The "
                        "capture lead "
                        "documents one "
                        "vertical thesis "
                        "and ten "
                        "sample opportunities; "
                        "the operations "
                        "lead configures "
                        "restricted folders "
                        "and the "
                        "cash forecast. "
                        "Completion evidence "
                        "includes the "
                        "reviewed service "
                        "scope, source "
                        "register, access "
                        "test, and "
                        "signed spending limit.",
                    ),
                    field(
                        "Days 8 through 14: qualification sprint",
                        "textarea",
                        "Define second-week "
                        "research, counterparty "
                        "qualification, pricing, "
                        "and outreach "
                        "outputs. Include "
                        "quality checks "
                        "and spending "
                        "limits, and "
                        "state which "
                        "evidence must "
                        "exist before "
                        "a prospect "
                        "can be "
                        "counted as "
                        "a qualified "
                        "service opportunity.",
                        "Week two "
                        "reviews 20 "
                        "notices, qualifies "
                        "six contractor "
                        "prospects, and "
                        "conducts three "
                        "readiness conversations. "
                        "A qualified "
                        "prospect needs "
                        "demonstrated delivery "
                        "capability, an "
                        "authorized buyer, "
                        "a defined "
                        "procurement problem, "
                        "and a "
                        "plausible fee "
                        "budget. Additional "
                        "spending is "
                        "capped at "
                        "$3,000; unverified "
                        "contact lists "
                        "do not "
                        "satisfy the target.",
                    ),
                    field(
                        "Days 15 through 21: delivery rehearsal",
                        "textarea",
                        "Specify a "
                        "complete rehearsal "
                        "covering intake, "
                        "requirement extraction, "
                        "pricing review, "
                        "client authorization, "
                        "package preparation, "
                        "ledger entries, "
                        "and recovery. "
                        "Use synthetic "
                        "or authorized "
                        "materials and "
                        "record actual "
                        "defects, hours, "
                        "and corrective "
                        "actions before "
                        "accepting production deadlines.",
                        "Week three "
                        "runs a "
                        "synthetic $20,000 "
                        "engagement through "
                        "the complete "
                        "workflow without "
                        "submitting to "
                        "an agency. "
                        "The team "
                        "budgets 16 "
                        "rehearsal hours "
                        "and tests "
                        "one amendment "
                        "plus one "
                        "portal-outage scenario. "
                        "The expected "
                        "deliverables are "
                        "a signed "
                        "review record, "
                        "defect log, "
                        "reconciled sample "
                        "ledger, and "
                        "updated checklist.",
                    ),
                    field(
                        "Days 22 through 30: launch decision",
                        "textarea",
                        "Define final-week "
                        "commercial outputs, "
                        "operating evidence, "
                        "cash review, "
                        "and the "
                        "day-thirty decision. "
                        "Separate signed "
                        "engagements from "
                        "proposals and "
                        "qualified pipeline, "
                        "and identify "
                        "the funded "
                        "next step "
                        "if no "
                        "client has "
                        "yet purchased.",
                        "The day-thirty "
                        "review targets "
                        "two tailored "
                        "service proposals "
                        "and a "
                        "tested operating "
                        "system, not "
                        "a guaranteed "
                        "award. If "
                        "neither proposal "
                        "is signed, "
                        "recognized service "
                        "revenue remains "
                        "zero. Management "
                        "continues only "
                        "with verified "
                        "buyer interest, "
                        "a revised "
                        "90-day cash "
                        "forecast, and "
                        "funding consistent "
                        "with the "
                        "6-to-18-month first-deal window.",
                    ),
                    field(
                        "Pod roles, capacity, and backup coverage",
                        "textarea",
                        "Allocate capture, "
                        "production, specialist "
                        "review, finance, "
                        "and release "
                        "responsibilities across "
                        "the pod. "
                        "State available "
                        "hours and "
                        "loaded costs, "
                        "identify conflicts "
                        "between production "
                        "and independent "
                        "review, and "
                        "document backup "
                        "authority for "
                        "critical absences.",
                        "The Base "
                        "benchmark uses "
                        "two full-time "
                        "roles and "
                        "three contractors: "
                        "capture lead, "
                        "operations lead, "
                        "proposal writer, "
                        "pricing reviewer, "
                        "and procurement "
                        "specialist. Contractor "
                        "headcount does "
                        "not imply "
                        "full-time availability. "
                        "A proposal "
                        "writer cannot "
                        "independently approve "
                        "their own "
                        "release; the "
                        "operations lead "
                        "maintains funded "
                        "backup review "
                        "hours in "
                        "the engagement budget.",
                    ),
                    field(
                        "Weekly pod KPI scorecard",
                        "textarea",
                        "Define each "
                        "KPI's numerator, "
                        "denominator, target, "
                        "measurement period, "
                        "data source, "
                        "and action "
                        "owner. Include "
                        "qualification, timeliness, "
                        "critical defects, "
                        "rework cost, "
                        "delivery utilization, "
                        "collections, and "
                        "concentration rather "
                        "than relying "
                        "only on "
                        "bid volume.",
                        "The weekly "
                        "scorecard targets "
                        "100% verified "
                        "deadlines, zero "
                        "critical release "
                        "defects, and "
                        "rework within "
                        "the $1,000 "
                        "per-engagement budget. "
                        "Collections reporting "
                        "shows overdue "
                        "receivables divided "
                        "by total "
                        "receivables. For "
                        "four completed "
                        "engagements, $3,200 "
                        "rework averages "
                        "$800 each; "
                        "the delivery "
                        "lead investigates "
                        "any individual "
                        "case exceeding "
                        "its approved allowance.",
                    ),
                    field(
                        "Scale decision and capacity economics",
                        "textarea",
                        "Set evidence-based "
                        "conditions for "
                        "moving toward "
                        "the Scaled "
                        "scenario. Reconcile "
                        "engagement volume, "
                        "average fee, "
                        "expense ceiling, "
                        "headcount, cash "
                        "availability, and "
                        "service quality "
                        "before adding "
                        "permanent capacity "
                        "or promising "
                        "more concurrent "
                        "proposal deadlines.",
                        "Scaled requires "
                        "40 completed "
                        "engagements at "
                        "$25,000, yielding "
                        "$1,000,000 revenue, "
                        "$700,000 expenses, "
                        "and $300,000 "
                        "owner net "
                        "profit at "
                        "30%. Staffing "
                        "is three "
                        "full-time people "
                        "plus four "
                        "contractors, seven "
                        "people total. "
                        "Management requires "
                        "funded delivery "
                        "hours and "
                        "sustained quality "
                        "before hiring; "
                        "signed demand "
                        "alone does "
                        "not establish "
                        "collection capacity.",
                    ),
                    field(
                        "Exit-readiness and transferability ledger",
                        "textarea",
                        "Inventory transferable "
                        "processes, contracts, "
                        "data rights, "
                        "financial records, "
                        "customer relationships, "
                        "security obligations, "
                        "and key-person "
                        "dependencies. Distinguish "
                        "private service "
                        "contract assignment "
                        "from transfer "
                        "of an "
                        "actual government "
                        "contract, and "
                        "identify required "
                        "consents or "
                        "specialist review.",
                        "The desk "
                        "maintains monthly "
                        "fee ledgers, "
                        "signed service "
                        "agreements, documented "
                        "procedures, and "
                        "client-specific access "
                        "records. A "
                        "sale review "
                        "checks assignment "
                        "restrictions and "
                        "confidentiality permissions. "
                        "If the "
                        "business holds "
                        "government prime "
                        "contracts, FAR "
                        "Subpart 42.12 "
                        "and 41 "
                        "U.S.C. Section "
                        "6305 receive "
                        "separate analysis; "
                        "a private "
                        "asset sale "
                        "does not "
                        "automatically transfer "
                        "those government obligations.",
                    ),
                    field(
                        "Owner decision, runway, and next review",
                        "textarea",
                        "Write the "
                        "continue, narrow, "
                        "or pause "
                        "decision using "
                        "actual cash, "
                        "qualified demand, "
                        "delivery readiness, "
                        "staffing affordability, "
                        "and unresolved "
                        "risks. Name "
                        "the accountable "
                        "owner, next "
                        "review date, "
                        "spending authority, "
                        "and evidence "
                        "that would "
                        "reverse the decision.",
                        "The owner "
                        "continues the "
                        "facilities niche "
                        "for another "
                        "30 days "
                        "with a "
                        "$10,000 spending "
                        "cap, provided "
                        "cash remains "
                        "above the "
                        "approved buffer "
                        "and qualified "
                        "conversations continue. "
                        "The desk "
                        "pauses expansion "
                        "if staffing "
                        "cannot be "
                        "funded or "
                        "mandatory review "
                        "coverage fails. "
                        "The next "
                        "review compares "
                        "actual cash "
                        "and signed "
                        "scope against "
                        "the updated forecast.",
                    ),
                ],
                "completion_gate": (
                    "The owner signs the thirty-day decision only after reviewing "
                    "actual launch evidence, funded staffing, canonical scenario "
                    "reconciliation, runway through the expected first-deal window, "
                    "pod quality metrics, and the transferability ledger."
                ),
            },
        ],
    }
