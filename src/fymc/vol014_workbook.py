from __future__ import annotations


def build_volume_014_workbook() -> dict:
    def field(name: str, input_type: str, prompt: str, example: str) -> dict:
        return {
            "name": name,
            "type": input_type,
            "prompt": prompt,
            "example": example,
        }

    return {
        "workbook_id": "wb-014-specialty-finance-brokerage",
        "volume_id": "vol-014-specialty-finance-brokerage",
        "title": "Specialty Finance Brokerage — Operator Companion Workbook",
        "subtitle": (
            "6 Printable Operator Worksheets for Commercial Deal Underwriting, "
            "Retained-Fee Economics, Lender Execution, Licensing Controls, "
            "Automation, and Small-Team Launch Readiness"
        ),
        "worksheets": [
            {
                "worksheet_id": "ws-01",
                "number": 1,
                "title": "Opportunity, Deal Underwriting & Counterparty Qualification",
                "purpose": (
                    "Select a commercially viable financing niche before spending money "
                    "on applications or lender introductions. Document borrower quality, "
                    "collateral evidence, lender appetite, intermediary authority, and "
                    "repayment capacity so each proposed placement has a defensible "
                    "economic purpose and an identifiable execution path."
                ),
                "chapter_ref": "Q1, Q2, Q6",
                "instructions": [
                    (
                        "Choose one initial commercial financing vertical and define its "
                        "borrower profile, ticket range, collateral, geography, and repayment "
                        "source. Separate equipment, receivables, SBA, and bridge opportunities "
                        "because their documentation, licensing analysis, lender appetite, "
                        "and closing dependencies differ materially."
                    ),
                    (
                        "Collect borrower documents through a restricted portal, then reconcile "
                        "identity, ownership, bank activity, liabilities, and requested proceeds. "
                        "Record the source date and reviewer for every material fact rather "
                        "than copying unverified statements into a lender submission."
                    ),
                    (
                        "Build the lender matrix from current written criteria and conversations "
                        "with authorized lender representatives. Include excluded industries, "
                        "minimum coverage, lien expectations, geographic limits, pricing "
                        "mechanics, and broker compensation rules before assigning a deal."
                    ),
                    (
                        "Stress the actual repayment source using a documented downside case. "
                        "For receivables, inspect dilution and customer concentration; for "
                        "equipment, inspect useful life and liquidation support; for bridge "
                        "financing, test the exit independently of optimistic appreciation."
                    ),
                    (
                        "Approve a qualified opportunity only after the borrower, proposed "
                        "lender, and broker relationship pass the documented checks. Assign "
                        "a named owner to each unresolved condition and prevent automated "
                        "routing from bypassing missing evidence or geographic restrictions."
                    ),
                ],
                "fields": [
                    field(
                        "Initial vertical and commercial use",
                        "textarea",
                        (
                            "Define the first borrower segment, financing product, ticket size, "
                            "eligible states, and specific use of proceeds. Explain why "
                            "repeatable documentation and accessible lenders make this segment "
                            "appropriate for the initial operating team."
                        ),
                        (
                            "Start with established packaging manufacturers seeking $300,000 "
                            "to $900,000 equipment loans in states cleared by the licensing "
                            "review. Require three operating years, identifiable production "
                            "equipment, and vendor invoices. Exclude household purchases, "
                            "speculative inventory, and transactions requiring securities placement."
                        ),
                    ),
                    field(
                        "Borrower identity and authority",
                        "textarea",
                        (
                            "List the entity records, ownership information, signing authority, "
                            "and account ownership evidence required for intake. Identify "
                            "who verifies discrepancies and distinguish broker verification "
                            "from the lender's separate customer identification obligations."
                        ),
                        (
                            "For Harbor Packaging LLC, obtain formation records, a current "
                            "registry extract, the operating agreement, and a borrowing "
                            "resolution naming the authorized signer. Reconcile two owners "
                            "holding 60% and 40%. Match the disbursement account to the "
                            "entity and escalate any third-party payment request."
                        ),
                    ),
                    field(
                        "Sources, uses, and borrower contribution",
                        "textarea",
                        (
                            "Reconcile the requested loan, borrower cash, vendor invoices, "
                            "closing costs, and other funding sources. Specify whether fees "
                            "are financed or separately paid and prevent the same borrower "
                            "contribution from appearing twice."
                        ),
                        (
                            "Equipment costs $600,000, installation costs $25,000, and "
                            "documented closing charges total $5,000, producing $630,000 "
                            "of uses. A $500,000 loan plus $130,000 borrower cash balances "
                            "the schedule. The lender separately pays the broker's $10,000 "
                            "fee; it is excluded from borrower-funded uses."
                        ),
                    ),
                    field(
                        "Repayment capacity and downside case",
                        "textarea",
                        (
                            "Calculate debt service coverage using normalized operating "
                            "cash flow and all required debt payments. Explain adjustments, "
                            "exclude unsupported addbacks, and record the downside case "
                            "that would invalidate the current lender match."
                        ),
                        (
                            "Verified annual cash available for debt service is $240,000. "
                            "Existing payments of $60,000 plus proposed payments of "
                            "$120,000 produce 1.33 times coverage. A 15% cash-flow "
                            "reduction leaves $204,000 and 1.13 times coverage, below "
                            "the selected lender's documented 1.25 minimum."
                        ),
                    ),
                    field(
                        "Collateral, liens, and valuation evidence",
                        "textarea",
                        (
                            "Identify collateral ownership, existing liens, valuation source, "
                            "inspection requirements, and expected lien priority. Explain "
                            "which lender or closing professional resolves filings and "
                            "releases before funds move to the seller."
                        ),
                        (
                            "The proposed collateral consists of two serial-numbered presses "
                            "priced at $600,000. An existing blanket lien requires a "
                            "documented release or subordination acceptable to the new "
                            "lender. Order the relevant UCC search and obtain written "
                            "closing instructions; a vendor invoice alone proves neither priority nor value."
                        ),
                    ),
                    field(
                        "Receivables eligibility and dilution",
                        "textarea",
                        (
                            "For receivables financing, reconcile aging, disputes, credit "
                            "memos, related-party balances, and customer concentration. "
                            "Show the borrowing-base calculation separately from the "
                            "broker's fee and identify any lender-specific eligibility adjustments."
                        ),
                        (
                            "An illustrative ledger has $800,000 in receivables. Remove "
                            "$100,000 aged beyond the lender limit and $50,000 of "
                            "disputed invoices, leaving $650,000 eligible. An 80% advance "
                            "produces $520,000 before other reserves. A 45% customer "
                            "concentration requires a separate haircut under the selected lender's policy."
                        ),
                    ),
                    field(
                        "Lender matrix and documented appetite",
                        "textarea",
                        (
                            "Record each candidate lender's product, state coverage, ticket "
                            "range, coverage threshold, collateral rules, decision authority, "
                            "and compensation terms. Date the evidence and define how "
                            "stale criteria are removed from active matching."
                        ),
                        (
                            "Equipment Lender A accepts $250,000 to $1,000,000 requests, "
                            "requires 1.25 times coverage, and pays a contracted 2% "
                            "origination fee after funding. Receivables Lender B accepts "
                            "eligible B2B invoices but excludes construction retainage. "
                            "Reconfirm both profiles every 30 days and before presenting unusual collateral."
                        ),
                    ),
                    field(
                        "Counterparty qualification and concentration",
                        "textarea",
                        (
                            "Verify lender identity, funding authority, references, payment "
                            "history, and broker-contract terms. Set concentration limits "
                            "using retained fees and pipeline exposure rather than merely "
                            "counting lenders with signed introduction agreements."
                        ),
                        (
                            "Three verified lenders generated retained fees of $60,000, "
                            "$40,000, and $20,000 over the trailing year. The first "
                            "represents 50% of $120,000, exceeding the internal 40% "
                            "target. Qualify two alternatives, check references, and avoid "
                            "promising borrower access to uncommitted funding."
                        ),
                    ),
                    field(
                        "Product boundary and specialist escalation",
                        "textarea",
                        (
                            "Identify characteristics that move a transaction outside the "
                            "chosen product lane. Specify escalation for SBA eligibility, "
                            "consumer-purpose ambiguity, securities features, real-estate "
                            "licensing questions, and bridge exits dependent on uncommitted refinancing."
                        ),
                        (
                            "A borrower requests a $750,000 bridge loan against commercial "
                            "property with repayment from an unsigned refinance proposal. "
                            "Require a documented fallback sale analysis and specialist "
                            "review of state brokerage requirements. Decline to market "
                            "fractional investor interests through the ordinary commercial-loan workflow."
                        ),
                    ),
                    field(
                        "Qualification decision and evidence owner",
                        "textarea",
                        (
                            "State the disposition, supporting evidence, unresolved conditions, "
                            "responsible reviewer, and next decision date. Distinguish internal "
                            "qualification from lender credit approval and make borrower "
                            "communications reflect that distinction accurately."
                        ),
                        (
                            "Disposition: qualified for lender discussion, not committed "
                            "funding. The analyst has verified invoices, ownership, and "
                            "bank statements. The principal must resolve the blanket "
                            "lien and downside coverage concern within five business "
                            "days. No term sheet is represented as a binding credit commitment."
                        ),
                    ),
                ],
                "completion_gate": (
                    "Advance only when all ten qualification records identify evidence "
                    "and an owner, at least two suitable lenders have current criteria, "
                    "sources equal uses, and unresolved restrictions prevent submission "
                    "until the responsible reviewer documents resolution."
                ),
            },
            {
                "worksheet_id": "ws-02",
                "number": 2,
                "title": "Unit Economics, Defect Reserve & Working-Capital Float",
                "purpose": (
                    "Translate funded placements into retained broker fees, then reconcile "
                    "those fees to the three canonical operating scenarios. Quantify "
                    "failed-closing expense, contractual clawbacks, collection delays, "
                    "and cash runway without treating loan principal, unused credit "
                    "commitments, or cash reserve transfers as operator earnings."
                ),
                "chapter_ref": "Q3, Q4",
                "instructions": [
                    (
                        "Start every calculation with the fee the brokerage is entitled "
                        "to retain under an executed agreement. Display borrower principal "
                        "in a separate operational column, and distinguish earned fees, "
                        "unearned contingent amounts, cash receipts, and potential repayments."
                    ),
                    (
                        "Reproduce Conservative, Base, and Scaled revenue, margin, owner "
                        "profit, and staffing exactly. Treat the illustrative deal counts "
                        "and fee rates below as ways to explain those totals, not "
                        "as additional forecasts supplied by the canonical scorecard."
                    ),
                    (
                        "Separate core monthly overhead from incremental production "
                        "expense, contractor delivery, partner compensation, and expected "
                        "loss expense. Explain why total annual expenses can exceed "
                        "twelve times the stated monthly operating range without "
                        "changing the canonical profit figures."
                    ),
                    (
                        "Build a cohort reserve from observed defects, failed closings, "
                        "refund rights, and contractual repayment windows. Distinguish "
                        "management cash earmarks from accounting expenses so a "
                        "transfer into a reserve bank account never creates a second deduction."
                    ),
                    (
                        "Stress collection timing, funded volume, and lender concentration "
                        "before committing additional payroll or marketing. Calculate "
                        "cash available after restricted amounts and unpaid obligations, "
                        "then assign a concrete spending response to each downside threshold."
                    ),
                ],
                "fields": [
                    field(
                        "Retained fee and principal separation",
                        "textarea",
                        (
                            "Document the contractual fee rate, fee base, responsible payer, "
                            "earning event, and any external share. Show placement volume "
                            "only as an operating measure and calculate retained revenue "
                            "without adding principal."
                        ),
                        (
                            "A $1,000,000 funded equipment loan carries a lender-paid "
                            "2% broker fee, producing $20,000 retained revenue when "
                            "the contractual earning conditions are met. The brokerage "
                            "has no partner split on this deal. The $1,000,000 "
                            "principal belongs in placement reporting, never in brokerage revenue."
                        ),
                    ),
                    field(
                        "Conservative scenario reconciliation",
                        "textarea",
                        (
                            "Reconcile annual revenue, total expense, net margin, owner "
                            "profit, and team size to the Conservative case. Supply "
                            "an illustrative funded-deal count and retained fee that "
                            "multiply exactly to canonical revenue."
                        ),
                        (
                            "Twelve funded placements at $10,000 retained fees produce "
                            "$120,000 revenue. Expenses of $90,000 leave $30,000 annual "
                            "owner net profit and a 25% net margin. Staffing remains "
                            "2 full-time people plus 2 contractors; contractor counts "
                            "do not imply full-time hours or equal compensation."
                        ),
                    ),
                    field(
                        "Base scenario reconciliation",
                        "textarea",
                        (
                            "Reconcile the Base case using exact revenue and profit "
                            "figures. Separate funded placement volume from retained "
                            "fees, and explain the average monthly fee production "
                            "needed without assuming closings arrive evenly."
                        ),
                        (
                            "Twenty-eight placements at $20,000 retained fees produce "
                            "$560,000 annual revenue. Expenses of $364,000 leave "
                            "$196,000 owner net profit, exactly 35.0%. The team is "
                            "2 full-time people plus 2 contractors. Average monthly "
                            "revenue is $46,666.67, although actual collections follow uneven closing dates."
                        ),
                    ),
                    field(
                        "Scaled small-team scenario reconciliation",
                        "textarea",
                        (
                            "Reconcile the Scaled case with the six-person staffing "
                            "ceiling. Identify the illustrative average retained fee "
                            "and deal count, and calculate expenses from canonical "
                            "revenue less canonical owner profit."
                        ),
                        (
                            "Forty placements at $25,000 retained fees produce "
                            "$1,000,000 revenue. Annual expenses of $550,000 leave "
                            "$450,000 owner net profit and a 45% margin. Staffing "
                            "is 3 full-time people plus 3 contractors, six people "
                            "total. Illustrative $1,250,000 loans at 2% explain each fee."
                        ),
                    ),
                    field(
                        "Expense bridge and monthly operating range",
                        "textarea",
                        (
                            "Allocate each scenario's expense total among core overhead, "
                            "incremental delivery costs, and expected loss expense. "
                            "Keep core monthly overhead within the supplied range "
                            "and document which costs sit outside that run rate."
                        ),
                        (
                            "Conservative expenses are $48,000 core, $30,000 delivery, "
                            "and $12,000 expected losses. Base expenses are $144,000, "
                            "$192,000, and $28,000. Scaled expenses are $216,000, "
                            "$284,000, and $50,000. Core monthly overhead is respectively "
                            "$4,000, $12,000, and $18,000; these illustrative allocations preserve all canonical totals."
                        ),
                    ),
                    field(
                        "Scrub defects and failed-closing cost",
                        "textarea",
                        (
                            "Calculate application preparation cost per funded placement "
                            "using completed and failed files. Define preventable "
                            "defects, assign remediation ownership, and place failed-file "
                            "labor inside the existing expense bridge rather than adding it twice."
                        ),
                        (
                            "Forty files enter full packaging, but only 28 fund, "
                            "a 70% conversion rate. At $600 packaging cost per "
                            "file, total packaging expense is $24,000, or $857.14 "
                            "per funded deal. The $7,200 spent on twelve failed "
                            "files is already included in Base delivery expense."
                        ),
                    ),
                    field(
                        "Clawback exposure and reserve mechanics",
                        "textarea",
                        (
                            "Record repayment triggers, exposure windows, probability "
                            "assumptions, expected loss, and cash earmarks. Explain "
                            "how the accountant distinguishes contingent fee recognition, "
                            "refund liabilities, and separate liquidity reserves under "
                            "the brokerage's accounting policy."
                        ),
                        (
                            "A $20,000 collected fee has a contractual 90-day "
                            "early-default repayment provision. An illustrative 5% "
                            "full-clawback probability implies $1,000 expected loss. "
                            "Across 28 comparable placements, $28,000 matches the "
                            "Base loss assumption. Earmarking $28,000 cash is a liquidity "
                            "action, not another $28,000 expense."
                        ),
                    ),
                    field(
                        "Startup funding and runway",
                        "textarea",
                        (
                            "Allocate startup cash across setup expenses and available "
                            "working capital. Compare runway with the supplied first-deal "
                            "timeline, include contractor obligations, and identify the "
                            "funding gap before accepting a launch budget."
                        ),
                        (
                            "A $60,000 launch budget allocates $12,000 to licensing "
                            "and counsel, $8,000 to systems, $10,000 to insurance "
                            "and initial acquisition, and $30,000 to working capital. "
                            "At $12,000 core monthly spend, runway is only 2.5 "
                            "months before variable costs, shorter than the 3–9 month first-deal range."
                        ),
                    ),
                    field(
                        "Collection lag and cash trough",
                        "textarea",
                        (
                            "Model the days between funding, fee entitlement, invoicing, "
                            "and cleared collection. Calculate the cash trough using "
                            "actual obligations and exclude pending invoices from "
                            "spendable cash until payment clears."
                        ),
                        (
                            "Starting unrestricted cash is $30,000. Over a 45-day "
                            "collection delay, core overhead consumes $18,000 and "
                            "scheduled contractor payments consume $8,000, leaving "
                            "$4,000. Two earned $20,000 invoices remain receivables "
                            "until collected; their $40,000 face value cannot finance today's payroll."
                        ),
                    ),
                    field(
                        "Break-even, sensitivity, and response",
                        "textarea",
                        (
                            "Calculate contribution per closing, break-even funded "
                            "volume, and a practical downside response. Reconcile "
                            "the chosen variable-cost assumption to the Base expense "
                            "bridge instead of inventing a conflicting margin model."
                        ),
                        (
                            "Base variable delivery and expected losses total "
                            "$220,000, or $7,857.14 per closing. Contribution is "
                            "$12,142.86 against $144,000 fixed overhead, requiring "
                            "twelve whole closings to break even. At twenty closings, "
                            "modeled profit falls to about $98,857; pause new recurring "
                            "spend if unrestricted cash falls below $24,000."
                        ),
                    ),
                ],
                "completion_gate": (
                    "Sign off only when the three cases reconcile to $30,000, "
                    "$196,000, and $450,000 annual owner net profit, principal is "
                    "excluded from revenue, cash transfers are not double-counted, "
                    "and a dated funding plan covers the modeled cash trough."
                ),
            },
            {
                "worksheet_id": "ws-03",
                "number": 3,
                "title": "Execution, Fee Ledger & Technical QA Pre-Flight",
                "purpose": (
                    "Turn a qualified request into an auditable placement workflow "
                    "with controlled documents, traceable lender submissions, and "
                    "reconciled fee records. Establish technical checks that prevent "
                    "duplicate applications, altered payment instructions, unsupported "
                    "revenue entries, and silent failures between the CRM, portal, "
                    "accounting system, and lender communications."
                ),
                "chapter_ref": "Q7, Q8",
                "instructions": [
                    (
                        "Assign a permanent deal identifier before requesting sensitive "
                        "documents. Use that identifier across the CRM, portal, lender "
                        "submission log, contract folder, and accounting records so "
                        "reviewers can trace every status change without relying on filenames."
                    ),
                    (
                        "Define entry and exit criteria for each execution stage, "
                        "including the person responsible for borrower updates. Require "
                        "evidence of actual lender receipt, decision conditions, and "
                        "funding confirmation rather than treating an outgoing email as successful execution."
                    ),
                    (
                        "Validate documents for completeness, consistency, date coverage, "
                        "and authorization before submission. Compare bank activity with "
                        "reported revenue and debt payments, and escalate discrepancies "
                        "through a documented process instead of modifying borrower "
                        "records to improve apparent qualification."
                    ),
                    (
                        "Reconcile the contractual earning event to invoice creation "
                        "and cash receipt. Keep receivables, contingent compensation, "
                        "refund exposure, and principal placement statistics distinct "
                        "so the accounting export cannot inflate retained-fee revenue."
                    ),
                    (
                        "Run duplicate-event, access-control, reconciliation, and recovery "
                        "tests before enabling production integrations. Record actual "
                        "test results and unresolved defects, and maintain a manual "
                        "processing path that preserves the same evidence and authorization requirements."
                    ),
                ],
                "fields": [
                    field(
                        "Deal identifier and controlled record",
                        "textarea",
                        (
                            "Specify the unique identifier format, system of record, "
                            "required fields, and document ownership. Describe how "
                            "duplicate borrower submissions are detected without merging "
                            "unrelated facilities or exposing one client's records to another."
                        ),
                        (
                            "Create deal identifier SF-2026-0142 in HubSpot and "
                            "mirror it in the restricted document folder and "
                            "QuickBooks invoice reference. Match possible duplicates "
                            "using entity identifier, product, and request date. "
                            "A second facility receives a new identifier linked "
                            "to the same verified borrower record."
                        ),
                    ),
                    field(
                        "Stage transitions and accountable owners",
                        "textarea",
                        (
                            "Define the ordered execution stages, required evidence, "
                            "responsible owner, and time target for each transition. "
                            "Prevent automatic progression when the necessary borrower "
                            "authorization or lender response is absent."
                        ),
                        (
                            "Stages are intake, verified package, lender review, "
                            "conditional offer, closing preparation, funded, and "
                            "fee collected. The analyst owns packaging within "
                            "three business days of complete intake. Only a "
                            "recorded lender response permits conditional-offer status; "
                            "only confirmed disbursement permits funded status."
                        ),
                    ),
                    field(
                        "Document completeness and discrepancy log",
                        "textarea",
                        (
                            "List required documents by product and define checks "
                            "for missing periods, inconsistent balances, altered "
                            "files, and unsigned authorities. Record the discrepancy "
                            "resolution without overwriting the original borrower submission."
                        ),
                        (
                            "The equipment checklist requires three bank statements, "
                            "two annual tax returns, interim statements, a debt "
                            "schedule, and vendor invoices. A $22,000 monthly debit "
                            "missing from the debt schedule triggers clarification. "
                            "Preserve the original schedule and attach the borrower's "
                            "corrected version with reviewer and receipt dates."
                        ),
                    ),
                    field(
                        "Submission authority and recipient controls",
                        "textarea",
                        (
                            "Record borrower authorization, approved recipients, "
                            "submission scope, secure delivery method, and confirmation "
                            "of receipt. Limit document sharing to the particular "
                            "placement purpose and remove recipients when the lender relationship ends."
                        ),
                        (
                            "The borrower authorizes submission to Equipment Lenders "
                            "A and C for the specified $500,000 request. Send "
                            "time-limited portal invitations to verified business "
                            "addresses, not public links. Log lender receipt and "
                            "disable access after withdrawal under the retention "
                            "schedule, preserving the submission audit record."
                        ),
                    ),
                    field(
                        "Term sheet and closing condition comparison",
                        "textarea",
                        (
                            "Compare proposed terms with approved borrower instructions "
                            "and the lender's closing checklist. Identify changes "
                            "in proceeds, payment structure, guarantees, collateral, "
                            "fees, and conditions that require renewed borrower acknowledgment."
                        ),
                        (
                            "The initial proposal offered $500,000 over sixty "
                            "months; final documents offer $475,000 and require "
                            "an additional guarantor. The broker highlights the "
                            "$25,000 proceeds reduction and revised obligations "
                            "before signing. The borrower must update the sources "
                            "and uses schedule rather than assume the original terms survived."
                        ),
                    ),
                    field(
                        "Funding confirmation and payment verification",
                        "textarea",
                        (
                            "Define acceptable proof of funding and the independent "
                            "verification process for payment instructions. State "
                            "who may approve changes and keep borrower principal "
                            "outside brokerage-controlled accounts unless a separately reviewed arrangement permits custody."
                        ),
                        (
                            "Obtain lender confirmation that $500,000 was disbursed "
                            "to the verified equipment vendor. Confirm any changed "
                            "bank details through a callback to an independently "
                            "stored number and require a second reviewer. The "
                            "broker receives only its contracted $10,000 fee, "
                            "not the borrower's financing proceeds."
                        ),
                    ),
                    field(
                        "Fee ledger and accounting treatment",
                        "textarea",
                        (
                            "Design ledger fields for earning date, payer, retained "
                            "amount, invoice, collection, repayment exposure, and "
                            "accounting reference. Explain how bookkeeping follows "
                            "the adopted revenue policy rather than a CRM status label."
                        ),
                        (
                            "For an earned $20,000 fee, record the contract "
                            "reference, funding evidence, invoice INV-0142, and "
                            "collection due date. Under the approved accrual "
                            "policy, debit receivables and credit fee revenue "
                            "when recognition criteria are satisfied. Collection "
                            "clears receivables; any refund estimate receives separate accountant review."
                        ),
                    ),
                    field(
                        "Integration idempotency and validation",
                        "textarea",
                        (
                            "Specify event identifiers, required payload fields, "
                            "validation rules, retry handling, and duplicate protection. "
                            "Define how failed events become visible to an "
                            "operator before an invoice or borrower notification is repeated."
                        ),
                        (
                            "Use the pair SF-2026-0142 and fee-earned-v1 as "
                            "the invoice idempotency key. Reject events lacking "
                            "contract reference, currency, or earning evidence. "
                            "Replay the same event three times in testing "
                            "and require one invoice. Route failed attempts "
                            "to a monitored exception queue with an assigned reviewer."
                        ),
                    ),
                    field(
                        "Access, retention, and recovery test",
                        "textarea",
                        (
                            "Define role-based access, multifactor authentication, "
                            "retention ownership, backup protection, and restoration "
                            "testing. Describe how contractors lose access promptly "
                            "and how restored records preserve the original audit trail."
                        ),
                        (
                            "The analyst accesses assigned files; the bookkeeper "
                            "accesses fee evidence rather than full borrower "
                            "tax records. Require multifactor authentication and "
                            "disable departing contractor accounts the same day. "
                            "Restore a sample deal into an isolated workspace "
                            "quarterly and verify document hashes, permissions, and ledger links."
                        ),
                    ),
                    field(
                        "Pre-flight acceptance and exception resolution",
                        "textarea",
                        (
                            "Record concrete test cases, expected results, actual "
                            "outcomes, and accountable defect owners. Define which "
                            "failures stop automated processing and which permit "
                            "documented manual handling without weakening evidence requirements."
                        ),
                        (
                            "Before activation, test a duplicate invoice event, "
                            "expired portal link, unauthorized export, missing "
                            "funding confirmation, and failed accounting connection. "
                            "Expected results are no duplicate billing, denied "
                            "access, and visible exceptions. If the accounting "
                            "test fails, keep invoicing manual until reconciliation passes."
                        ),
                    ),
                ],
                "completion_gate": (
                    "Release the workflow only after five documented pre-flight tests "
                    "pass, a sample deal reconciles from contract through collection, "
                    "principal never enters fee revenue, and a second reviewer confirms "
                    "payment-change controls and restricted document access."
                ),
            },
            {
                "worksheet_id": "ws-04",
                "number": 4,
                "title": "Statutory, Licensing, Contract & Outreach Audit",
                "purpose": (
                    "Map the brokerage's actual activities to jurisdiction-specific "
                    "licensing, disclosure, fair-lending, privacy, outreach, and "
                    "contract requirements. Convert that analysis into evidence-backed "
                    "operating restrictions, with separate review for SBA compensation, "
                    "consumer-report access, mortgage-related activity, and transactions "
                    "that could involve securities rather than ordinary commercial debt."
                ),
                "chapter_ref": "Q5, Q9",
                "instructions": [
                    (
                        "Inventory where the brokerage, borrower, collateral, lender, "
                        "and outreach recipients are located. Analyze the activities "
                        "actually performed in each jurisdiction rather than assuming "
                        "a commercial-purpose label or the lender's license automatically "
                        "covers the intermediary."
                    ),
                    (
                        "Maintain a dated requirements register with statutory "
                        "citations, applicability reasoning, evidence, and renewal "
                        "owners. Check exemptions against their specific conditions, "
                        "and restrict activity when a required license, filing, "
                        "disclosure, or contractual permission has not been established."
                    ),
                    (
                        "Review borrower and lender contracts together so compensation, "
                        "refund rights, exclusivity, representations, data sharing, "
                        "and dispute provisions remain consistent. Explain all "
                        "material fee arrangements before the borrower incurs "
                        "the obligation or accepts the covered offer."
                    ),
                    (
                        "Translate fair-lending and security duties into operational "
                        "controls covering intake, matching, communications, access, "
                        "and records. Assign responsibility for notices and "
                        "retention based on the parties' actual roles rather "
                        "than copying a lender's policy without examining applicability."
                    ),
                    (
                        "Test outreach and product boundaries before starting "
                        "campaigns or accepting referrals. Verify suppression "
                        "handling, contact channels, securities indicators, and "
                        "SBA-specific documentation, then retain evidence showing "
                        "why each selected process is permitted for the proposed activity."
                    ),
                ],
                "fields": [
                    field(
                        "Jurisdiction and licensing applicability map",
                        "textarea",
                        (
                            "Identify relevant jurisdictions, activity descriptions, "
                            "license categories, exemption conditions, and evidence "
                            "owners. Include a concrete statutory reference and "
                            "explain why lender authorization alone does not "
                            "resolve the brokerage's obligations."
                        ),
                        (
                            "For California activity, analyze the California "
                            "Financing Law, including Financial Code sections "
                            "22004 and 22100, and document whether the proposed "
                            "brokerage activity requires licensing or satisfies "
                            "an exemption. Verify lender status separately. "
                            "Restrict California submissions until the written applicability "
                            "analysis and required authorization are complete."
                        ),
                    ),
                    field(
                        "Commercial financing disclosures",
                        "textarea",
                        (
                            "Identify covered commercial financing offers, transaction "
                            "thresholds, responsible providers, broker delivery duties, "
                            "and required timing. Record the applicable state "
                            "rules rather than assuming one national disclosure "
                            "template covers every product."
                        ),
                        (
                            "Review California Financial Code sections 22800–22805 "
                            "and New York Financial Services Law sections "
                            "801–811 with 23 NYCRR Part 600. For each covered "
                            "offer, identify the responsible provider and any "
                            "broker delivery obligations. Preserve the actual "
                            "disclosure version and evidence of delivery before required acceptance."
                        ),
                    ),
                    field(
                        "ECOA, matching rules, and notices",
                        "textarea",
                        (
                            "Map the brokerage's role under ECOA and Regulation "
                            "B, including nondiscrimination, discouragement, decision "
                            "participation, notices, and recordkeeping. Specify "
                            "who owns each applicable duty and test lender "
                            "matching for prohibited criteria."
                        ),
                        (
                            "Review 15 U.S.C. 1691 and 12 CFR Part 1002, "
                            "including sections 1002.2(l), 1002.4, 1002.9, "
                            "and 1002.12. A referral-only role differs from "
                            "credit-decision participation. Exclude protected "
                            "characteristics from matching, identify the party "
                            "responsible for applicable notices, and document the business-credit retention rule."
                        ),
                    ),
                    field(
                        "Consumer reports and guarantor permissions",
                        "textarea",
                        (
                            "Identify whether any owner or guarantor consumer "
                            "report is accessed, the permissible purpose, "
                            "authorization evidence, access restrictions, and "
                            "notice responsibilities. Distinguish business "
                            "entity credit information from individual consumer-report data."
                        ),
                        (
                            "Before requesting an owner's consumer report, "
                            "document a permissible purpose under 15 U.S.C. "
                            "1681b and the provider's required authorization "
                            "process. Limit access to the assigned reviewer. "
                            "If report information contributes to an adverse "
                            "decision, determine applicable duties under 15 U.S.C. 1681m "
                            "and allocate responsibility explicitly."
                        ),
                    ),
                    field(
                        "Information security and incident duties",
                        "textarea",
                        (
                            "Determine applicable financial-information safeguards, "
                            "privacy obligations, service-provider controls, "
                            "and incident notifications. Record coverage analysis "
                            "and implement concrete security measures rather "
                            "than treating a portal vendor's marketing claims "
                            "as proof of compliance."
                        ),
                        (
                            "Assess coverage under 15 U.S.C. 6801–6809 and "
                            "16 CFR Part 314, including any limited exceptions "
                            "and applicable FTC notification duties. Maintain "
                            "a written security program, multifactor authentication, "
                            "encryption, vendor oversight, and incident procedures. "
                            "Separately evaluate affected residents' state breach-notification requirements "
                            "using actual incident facts."
                        ),
                    ),
                    field(
                        "Broker compensation and contract alignment",
                        "textarea",
                        (
                            "Record payer identity, retained compensation, earning "
                            "conditions, cancellation treatment, clawback triggers, "
                            "and fee disclosure timing. Compare borrower and "
                            "lender agreements for inconsistent statements "
                            "about independence, exclusivity, and compensation."
                        ),
                        (
                            "The lender agreement pays 2% of funded principal "
                            "within fifteen business days after the earning "
                            "conditions are satisfied. The borrower engagement "
                            "discloses lender-paid compensation and no borrower "
                            "success fee. A ninety-day repayment provision "
                            "identifies covered events, calculation method, notice procedure, "
                            "and dispute rights."
                        ),
                    ),
                    field(
                        "SBA agent compensation and eligibility",
                        "textarea",
                        (
                            "For SBA placements, identify agent services, "
                            "compensation source, required disclosures, eligibility "
                            "review, and lender responsibilities. Use current "
                            "program instructions and avoid representing "
                            "ordinary lender interest as SBA authorization."
                        ),
                        (
                            "For a proposed $750,000 SBA 7(a) placement, "
                            "review 13 CFR Part 103, 13 CFR 120.221, "
                            "current SBA Form 159 instructions, and the "
                            "applicable SBA operating procedures. Describe "
                            "each compensated service and payer, check "
                            "current fee restrictions, and have the lender "
                            "confirm required agent documentation before closing."
                        ),
                    ),
                    field(
                        "Email, telephone, and text outreach",
                        "textarea",
                        (
                            "Document outreach channels, audience sourcing, "
                            "message claims, suppression controls, and "
                            "applicable federal and state restrictions. "
                            "Do not treat a business contact label "
                            "as universal permission for automated calls "
                            "or marketing texts."
                        ),
                        (
                            "Commercial email follows 15 U.S.C. 7704: "
                            "accurate headers, appropriate identification, "
                            "a valid postal address, and functioning opt-out "
                            "processing within ten business days. Review "
                            "47 U.S.C. 227 and 47 CFR 64.1200 before "
                            "calls or texts, including technology, number "
                            "type, permission requirements, and state restrictions."
                        ),
                    ),
                    field(
                        "Securities and mortgage activity boundary",
                        "textarea",
                        (
                            "Identify proposed activities that require "
                            "separate securities or mortgage analysis. "
                            "Record transaction structure, compensation "
                            "basis, collateral, borrower purpose, and "
                            "the restriction imposed while a qualified "
                            "reviewer determines the applicable registration requirements."
                        ),
                        (
                            "A sponsor asks the broker to sell fractional "
                            "interests in a debt pool for transaction-based "
                            "compensation. Suspend that activity and review "
                            "15 U.S.C. 78o(a) and the instrument's securities "
                            "status. Separately assess mortgage requirements "
                            "for real-estate-secured placements; commercial purpose "
                            "does not eliminate every state licensing obligation."
                        ),
                    ),
                    field(
                        "Requirements evidence and renewal calendar",
                        "textarea",
                        (
                            "Create an auditable register linking each "
                            "applicable requirement to evidence, operating "
                            "restriction, reviewer, renewal date, and "
                            "affected workflow. Define how legal changes "
                            "and expired authorizations reach the people "
                            "responsible for submissions and outreach."
                        ),
                        (
                            "The register links each approved state "
                            "to its analysis, license evidence where "
                            "required, contract version, and disclosure "
                            "procedure. Assign a principal and outside "
                            "counsel reviewer. Set reminders sixty and "
                            "thirty days before renewal, and disable "
                            "new affected-state submissions if required authority expires."
                        ),
                    ),
                ],
                "completion_gate": (
                    "Proceed only when each active jurisdiction and product has "
                    "a documented applicability decision, required authorizations "
                    "are current, fee and outreach documents are approved for "
                    "their actual use, and securities or mortgage exceptions "
                    "have an assigned specialist and an enforced activity restriction."
                ),
            },
            {
                "worksheet_id": "ws-05",
                "number": 5,
                "title": "Automation, Growth Flywheel & Risk Fallback Tracker",
                "purpose": (
                    "Build a repeatable acquisition and servicing system around "
                    "application checklists, evidence-based lender matching, and "
                    "renewal tracking. Measure funded economics rather than "
                    "message volume, while preserving borrower choice, controlling "
                    "lender concentration, and providing manual alternatives when "
                    "data, integrations, counterparties, or automated recommendations fail."
                ),
                "chapter_ref": "Q6, Q10",
                "instructions": [
                    (
                        "Select automation only after documenting the manual "
                        "decision and evidence requirements. Prioritize checklist "
                        "completion, lender eligibility filtering, and renewal "
                        "reminders because these reduce repetitive work without "
                        "delegating credit approval or legal interpretation "
                        "to an unreviewed software rule."
                    ),
                    (
                        "Build a referral and outbound funnel with explicit "
                        "stage definitions and denominators. Measure qualified "
                        "applications, complete packages, funded placements, "
                        "retained fees, and acquisition cost so booked "
                        "meetings cannot conceal poor borrower fit or "
                        "persistent closing failures."
                    ),
                    (
                        "Use named system owners and versioned matching "
                        "criteria. Capture why lenders were included "
                        "or excluded, review stale profiles, and "
                        "require human review for borderline cases "
                        "rather than allowing automation to fabricate "
                        "missing financial information or imply guaranteed approval."
                    ),
                    (
                        "Track concentration using both realized retained "
                        "fees and upcoming closing exposure. Maintain "
                        "qualified alternatives for important products, "
                        "and define the borrower communication, rerouting "
                        "authorization, and cash response triggered by "
                        "a lender pause or commission dispute."
                    ),
                    (
                        "Review growth experiments and automation exceptions "
                        "weekly using an evidence log. Expand only "
                        "when marginal acquisition economics, document "
                        "quality, staff capacity, and cash collection "
                        "remain acceptable; stop channels that create "
                        "complaints, unsuitable applications, or unmanageable sensitive-data exposure."
                    ),
                ],
                "fields": [
                    field(
                        "Ideal customer and acquisition proposition",
                        "textarea",
                        (
                            "Define the borrower profile, observable "
                            "trigger event, financing need, acquisition "
                            "channel, and evidence-backed service promise. "
                            "Exclude claims of certain approval, "
                            "universal lender coverage, or pricing "
                            "that cannot be supported for the target segment."
                        ),
                        (
                            "Target packaging manufacturers adding a "
                            "production line within six months and "
                            "seeking $300,000 to $900,000 equipment "
                            "financing. Lead with organized documentation "
                            "and comparison of suitable lender "
                            "structures. Promise a completeness review "
                            "within two business days, not a funding "
                            "decision or a fixed interest rate."
                        ),
                    ),
                    field(
                        "Referral partner qualification and economics",
                        "textarea",
                        (
                            "Identify referral sources, permitted "
                            "activities, compensation conditions, "
                            "borrower disclosures, and lead-quality "
                            "standards. Confirm whether partner "
                            "conduct creates licensing or agent "
                            "issues before exchanging applications "
                            "or paying transaction-linked compensation."
                        ),
                        (
                            "Recruit three equipment dealers and "
                            "two accountants for introductions. "
                            "Initially use uncompensated referrals "
                            "with borrower-authorized contact sharing. "
                            "If a compensated arrangement is "
                            "proposed, review applicable licensing "
                            "and disclosure rules first, then "
                            "document the fee and include it "
                            "in delivery expense rather than hiding "
                            "it inside principal."
                        ),
                    ),
                    field(
                        "Funnel mathematics and stage definitions",
                        "textarea",
                        (
                            "Calculate a complete funnel using "
                            "one consistent cohort and time "
                            "window. Define each stage, show "
                            "conversion rates, and reconcile "
                            "funded deal counts to the "
                            "illustrative Base retained-fee model."
                        ),
                        (
                            "An annual planning cohort contains "
                            "400 eligible contacts, 100 "
                            "substantive conversations, 60 "
                            "applications, 40 complete packages, "
                            "and 28 funded deals. Stage "
                            "conversions are 25%, 60%, "
                            "66.67%, and 70%. At $20,000 "
                            "retained per funding, the final "
                            "stage produces the canonical $560,000 "
                            "Base revenue."
                        ),
                    ),
                    field(
                        "Application checklist automation",
                        "textarea",
                        (
                            "Specify checklist triggers, product-specific "
                            "requirements, reminder cadence, exception "
                            "handling, and human review. "
                            "Explain how the automation "
                            "detects missing evidence without "
                            "inventing document contents or "
                            "repeatedly requesting already accepted files."
                        ),
                        (
                            "A HubSpot stage change creates "
                            "the equipment checklist in the "
                            "secure portal. Reminder tasks "
                            "run after three and seven "
                            "business days for missing items "
                            "only. The analyst reviews mismatched "
                            "statement periods. Once a file "
                            "is accepted, its status suppresses "
                            "further reminders unless a documented "
                            "refresh requirement applies."
                        ),
                    ),
                    field(
                        "Lender matching rules and explainability",
                        "textarea",
                        (
                            "Define hard eligibility filters, "
                            "ranking factors, evidence freshness, "
                            "and reviewer overrides. Keep "
                            "compensation separate from suitability "
                            "and record the reason "
                            "for each recommendation so "
                            "borrower interests are visible in the process."
                        ),
                        (
                            "Filter first by authorized geography, "
                            "product, $500,000 ticket size, "
                            "industry, collateral, and required "
                            "coverage. Rank surviving lenders "
                            "by structure fit and documented "
                            "execution performance. Do not "
                            "rank solely by broker fee. "
                            "An override requires the principal's "
                            "written reason and a current lender "
                            "confirmation of the exception."
                        ),
                    ),
                    field(
                        "Renewal tracking and borrower service",
                        "textarea",
                        (
                            "Define renewal, maturity, covenant, "
                            "and document-refresh dates "
                            "with accountable owners. Explain "
                            "how reminders improve borrower "
                            "service without treating "
                            "uncommitted refinancing or "
                            "future fees as recognized revenue."
                        ),
                        (
                            "For a receivables facility renewing "
                            "on September 30, schedule "
                            "borrower contact 120 days "
                            "earlier and updated aging "
                            "collection 90 days earlier. "
                            "Review concentration and renewal "
                            "terms sixty days before maturity. "
                            "Any potential renewal fee stays "
                            "in forecast reporting until the "
                            "contractual earning conditions are satisfied."
                        ),
                    ),
                    field(
                        "Acquisition cost and experiment budget",
                        "textarea",
                        (
                            "Calculate acquisition cost using "
                            "attributable spending and funded "
                            "cohort results. Distinguish "
                            "early leading indicators "
                            "from mature economics and "
                            "set a spending threshold "
                            "consistent with the existing expense model."
                        ),
                        (
                            "A mature campaign costs $18,000 "
                            "and produces six funded "
                            "placements, yielding $3,000 "
                            "acquisition cost per funding. "
                            "At $20,000 retained fees, "
                            "gross retained fees before "
                            "other costs are $120,000. "
                            "Include campaign spending within "
                            "Base delivery expense; cap the "
                            "next unproven test at $2,000."
                        ),
                    ),
                    field(
                        "Lender concentration and interruption fallback",
                        "textarea",
                        (
                            "Measure concentration by trailing "
                            "retained revenue and expected "
                            "pipeline fees. Define an "
                            "interruption trigger, alternative "
                            "lenders, borrower permissions, "
                            "and the cash-management "
                            "response if the largest counterparty stops funding."
                        ),
                        (
                            "Lender A represents $224,000 "
                            "of $560,000 Base revenue, "
                            "or 40%, and six "
                            "pending files carrying $120,000 "
                            "potential fees. A funding "
                            "pause triggers alternative-lender "
                            "review within two business "
                            "days, renewed borrower authorization "
                            "before redistribution, and suspension "
                            "of discretionary acquisition spend "
                            "until collection exposure is reassessed."
                        ),
                    ),
                    field(
                        "Integration failure and manual fallback",
                        "textarea",
                        (
                            "List critical integration dependencies, "
                            "failure signals, response owners, "
                            "manual procedures, and "
                            "reconciliation requirements. Ensure "
                            "fallback handling preserves "
                            "recipient restrictions and "
                            "avoids duplicate lender submissions or invoices."
                        ),
                        (
                            "If the CRM-to-portal connection "
                            "fails for thirty minutes, "
                            "the operations owner opens "
                            "a controlled exception register. "
                            "Staff create portal tasks "
                            "manually using existing deal "
                            "identifiers. On restoration, "
                            "compare event identifiers and "
                            "task records before replaying "
                            "messages; never resend sensitive "
                            "attachments through ordinary email "
                            "to bypass the outage."
                        ),
                    ),
                    field(
                        "Weekly learning loop and stop criteria",
                        "textarea",
                        (
                            "Define the weekly review "
                            "agenda, experiment evidence, "
                            "complaint tracking, defect "
                            "thresholds, and improvement "
                            "ownership. Specify which "
                            "findings stop an "
                            "acquisition channel or require changes before additional spend."
                        ),
                        (
                            "Every Friday, review contact "
                            "quality, application completion, "
                            "funding conversion, collection "
                            "lag, complaints, and exceptions. "
                            "Pause a channel if "
                            "more than 20% of "
                            "its last twenty applications "
                            "misstate the permitted use "
                            "of funds. Assign one "
                            "corrective experiment and review "
                            "the next twenty applications "
                            "before restoring the previous budget."
                        ),
                    ),
                ],
                "completion_gate": (
                    "Activate growth automation only after the funnel reconciles, "
                    "matching explanations are recorded, suppression and duplicate "
                    "controls pass testing, renewal forecasts remain outside earned "
                    "revenue, and a named owner has rehearsed the largest-lender "
                    "and integration-outage fallback procedures."
                ),
            },
            {
                "worksheet_id": "ws-06",
                "number": 6,
                "title": "30-Day Launch, Pod KPI Scorecard & Exit-Readiness Ledger",
                "purpose": (
                    "Translate the operating design into a thirty-day launch "
                    "sequence with accountable owners, measured capacity, and "
                    "cash-aware milestones. Preserve clean contracts, financial "
                    "records, and counterparty evidence from the start so "
                    "the brokerage can support disciplined growth, continuity "
                    "planning, and a later diligence process."
                ),
                "chapter_ref": "Q11, Q12",
                "instructions": [
                    (
                        "Treat the first thirty days as a readiness "
                        "and pipeline-building sprint, not a promise "
                        "of funded revenue. The supplied first-deal "
                        "range is three to nine months, so "
                        "sequence spending against available capital "
                        "and verified execution progress."
                    ),
                    (
                        "Assign each launch deliverable to one "
                        "accountable person and identify any "
                        "specialist dependency. Preserve the Base "
                        "team design of two full-time people "
                        "and two contractors, while checking "
                        "actual workload and employment classification "
                        "rather than assuming headcount alone proves capacity."
                    ),
                    (
                        "Review a compact weekly scorecard "
                        "covering qualified demand, complete "
                        "packages, funding conversion, retained "
                        "fees, collection lag, defects, "
                        "concentration, and cash. Define "
                        "each denominator and owner so "
                        "metric changes represent operating "
                        "facts rather than shifting definitions."
                    ),
                    (
                        "Build the diligence ledger alongside "
                        "ordinary operations. Preserve executed "
                        "contracts, license evidence, fee "
                        "reconciliations, clawback cohorts, "
                        "security records, and assignment "
                        "restrictions without exposing borrower "
                        "records to prospective counterparties "
                        "before appropriate authorization and controlled access."
                    ),
                    (
                        "At the end of the sprint, "
                        "compare completed evidence with "
                        "the plan and make a "
                        "documented proceed, remediate, "
                        "or pause decision. List "
                        "unfinished work explicitly, maintain "
                        "cash discipline, and separate "
                        "readiness accomplishments from transactions "
                        "that have actually funded."
                    ),
                ],
                "fields": [
                    field(
                        "Launch charter and canonical positioning",
                        "textarea",
                        (
                            "State the candidate, pipeline "
                            "rank, leverage score, "
                            "capital range, operating "
                            "range, and first-deal "
                            "timeline. Explain how "
                            "these inputs shape "
                            "the launch rather than treating the score as earned performance."
                        ),
                        (
                            "Volume 014 covers Candidate "
                            "#20, Specialty Finance Brokerage, "
                            "ranked #14 of 29 "
                            "with a 79/100 Money-to-Manpower "
                            "Score: 23 revenue, 21 "
                            "margin, 17 team efficiency, "
                            "8 accessibility, and 10 "
                            "automation. Plan around $20,000–$100,000 "
                            "startup capital, $4,000–$18,000 "
                            "monthly core operations, and "
                            "three to nine months "
                            "to the first deal."
                        ),
                    ),
                    field(
                        "Days 1–7: scope, authority, and evidence",
                        "textarea",
                        (
                            "Define the first week's "
                            "deliverables, accountable owners, "
                            "budget limits, and "
                            "dependencies. Prioritize product "
                            "scope, jurisdiction analysis, "
                            "contract review, and "
                            "secure intake before purchasing broad acquisition capacity."
                        ),
                        (
                            "The principal selects equipment "
                            "finance for established packaging "
                            "manufacturers, commissions the "
                            "initial jurisdiction review, "
                            "and approves draft engagements. "
                            "The analyst configures restricted "
                            "intake and the lender "
                            "matrix. Cap first-week "
                            "committed setup spending at "
                            "$6,000 within the broader "
                            "$60,000 launch allocation "
                            "and record each signed obligation."
                        ),
                    ),
                    field(
                        "Days 8–14: counterparties and dry runs",
                        "textarea",
                        (
                            "Specify lender qualification, "
                            "workflow tests, sample "
                            "documentation, and training "
                            "deliverables for the "
                            "second week. Use "
                            "synthetic test files "
                            "rather than distributing real borrower information without authorization."
                        ),
                        (
                            "Qualify three equipment lenders "
                            "using verified contacts, "
                            "written appetite, and "
                            "broker agreements. Run "
                            "two clearly labeled "
                            "synthetic applications through "
                            "checklist and matching "
                            "tests without submitting "
                            "them as real credit "
                            "requests. Complete duplicate-invoice, "
                            "access-denial, and backup-restoration "
                            "tests before enabling "
                            "live borrower intake."
                        ),
                    ),
                    field(
                        "Days 15–21: controlled acquisition pilot",
                        "textarea",
                        (
                            "Define the pilot audience, "
                            "channel, contact limits, "
                            "spending cap, success "
                            "criteria, and stop "
                            "conditions. Measure early "
                            "pipeline quality without "
                            "claiming that conversations or applications already represent funded revenue."
                        ),
                        (
                            "Contact forty verified business "
                            "prospects and hold "
                            "five referral-partner conversations "
                            "through reviewed channels. "
                            "Cap pilot spending "
                            "at $2,000 within "
                            "the initial acquisition "
                            "allocation. Target ten "
                            "substantive borrower conversations "
                            "and four eligible "
                            "applications; record zero "
                            "earned fees until actual "
                            "contractual earning conditions "
                            "have been satisfied."
                        ),
                    ),
                    field(
                        "Days 22–30: execution rehearsal and review",
                        "textarea",
                        (
                            "List final sprint "
                            "deliverables, evidence owners, "
                            "cash review, and "
                            "unresolved work. Distinguish "
                            "completed readiness tests "
                            "from live underwriting "
                            "outcomes and define the next operating period's spending permission."
                        ),
                        (
                            "Complete two authorized lender "
                            "submissions if borrower "
                            "files qualify, reconcile "
                            "the cash ledger, "
                            "and rehearse the "
                            "largest-lender interruption "
                            "scenario. If licensing "
                            "work remains open, "
                            "continue internal preparation "
                            "but restrict affected "
                            "submissions. Approve the "
                            "next month's spending "
                            "only after reviewing "
                            "remaining runway and "
                            "documented obligations."
                        ),
                    ),
                    field(
                        "Pod responsibilities and capacity calculation",
                        "textarea",
                        (
                            "Allocate responsibilities across "
                            "full-time and contractor "
                            "roles, estimate hours "
                            "per file, and "
                            "identify bottlenecks. Compare "
                            "capacity with the "
                            "Base funnel while preserving separation of duties for sensitive changes."
                        ),
                        (
                            "The principal owns lender "
                            "relationships and exceptions; "
                            "the analyst owns "
                            "packaging and borrower "
                            "updates. Two contractors "
                            "cover bookkeeping and "
                            "specialist file support. "
                            "Forty annual packages "
                            "at eighteen analyst "
                            "hours require 720 "
                            "hours, before follow-up "
                            "and renewals. Payment-detail "
                            "changes still require "
                            "two independent reviewers."
                        ),
                    ),
                    field(
                        "Weekly KPI scorecard and escalation",
                        "textarea",
                        (
                            "Define target metrics, "
                            "formulas, data sources, "
                            "owners, and escalation "
                            "thresholds. Separate mature "
                            "annual planning assumptions "
                            "from early sprint "
                            "observations so small samples do not create false operating certainty."
                        ),
                        (
                            "Track complete packages divided "
                            "by applications, funded "
                            "deals divided by "
                            "mature completed packages, "
                            "retained fees, median "
                            "collection days, defect "
                            "rate, and unrestricted "
                            "cash. Base planning "
                            "uses 28 fundings "
                            "from forty packages. "
                            "Escalate collection delays "
                            "beyond thirty days "
                            "past contractual due "
                            "dates and any "
                            "unresolved identity discrepancy."
                        ),
                    ),
                    field(
                        "Owner-profit bridge and distribution discipline",
                        "textarea",
                        (
                            "Connect the canonical "
                            "profit cases to "
                            "the management ledger "
                            "and cash distribution "
                            "policy. Separate accounting "
                            "profit from collectible "
                            "cash and retain funding for obligations, loss exposure, and continued operations."
                        ),
                        (
                            "The annual reference cases "
                            "remain $120,000 revenue "
                            "and $30,000 profit; "
                            "$560,000 and $196,000; "
                            "and $1,000,000 and "
                            "$450,000. These are "
                            "not monthly draw "
                            "budgets. If Base "
                            "profit accrues while "
                            "$40,000 remains uncollected, "
                            "review receivables, unpaid "
                            "expenses, repayment exposure, "
                            "and required working "
                            "capital before authorizing "
                            "an owner distribution."
                        ),
                    ),
                    field(
                        "Exit-readiness and transferable evidence",
                        "textarea",
                        (
                            "List diligence records "
                            "that demonstrate earnings "
                            "quality, counterparty durability, "
                            "operating independence, and "
                            "transfer restrictions. Explain "
                            "how a prospective "
                            "buyer receives staged access without unnecessary disclosure of borrower documents."
                        ),
                        (
                            "Maintain monthly fee reconciliations, "
                            "funding cohorts, clawback "
                            "history, lender concentration, "
                            "executed contracts, license "
                            "records, and procedure "
                            "versions. Index assignment "
                            "and change-of-control "
                            "clauses because lender "
                            "agreements and licenses "
                            "may require separate "
                            "action. Begin diligence "
                            "with aggregated metrics "
                            "and redacted samples "
                            "in a restricted "
                            "data room."
                        ),
                    ),
                    field(
                        "Day-30 decision and next-period commitments",
                        "textarea",
                        (
                            "Record the proceed, "
                            "remediate, or pause "
                            "decision with evidence, "
                            "cash available, unresolved "
                            "risks, accountable owners, "
                            "and dated next "
                            "actions. Avoid declaring completion for work that remains untested or dependent on another party."
                        ),
                        (
                            "Decision: remediate before expanding. "
                            "Three lender profiles "
                            "are verified and "
                            "two workflow rehearsals "
                            "passed, but one "
                            "state review remains "
                            "open. Unrestricted cash "
                            "is $26,000 against "
                            "$12,000 monthly core "
                            "spend. The principal "
                            "resolves the state "
                            "question within ten "
                            "business days; acquisition "
                            "stays capped and "
                            "no funded revenue "
                            "is reported."
                        ),
                    ),
                ],
                "completion_gate": (
                    "Close the sprint only after every milestone has an evidenced "
                    "status, the pod accepts its responsibilities, the scorecard "
                    "uses stable definitions, cash reconciles to the ledger, and "
                    "the day-30 decision explicitly identifies unfinished work, "
                    "funding needs, and restrictions on further activity."
                ),
            },
        ],
    }
