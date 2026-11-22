from __future__ import annotations


def build_volume_035_workbook() -> dict:
    def field(name: str, input_type: str, prompt: str, example: str) -> dict:
        return {"name": name, "type": input_type, "prompt": prompt, "example": example}

    return {
        "workbook_id": "wb-035-subject-to-and-wraparound-note-arbitrage",
        "volume_id": "vol-035-subject-to-and-wraparound-note-arbitrage",
        "title": "Subject-To & Wraparound Note Arbitrage — Operator Companion Workbook",
        "subtitle": (
            "6 Printable Operator Worksheets for Low-Rate Debt Acquisition, "
            "RMLO Buyer Underwriting, Retained Note Spreads, Verified Servicing, "
            "Reserve Protection, and Transfer-Ready Operations"
        ),
        "worksheets": [
            {
                "worksheet_id": "ws-01",
                "number": 1,
                "title": "Arbitrage Deal, Counterparty Underwriting & Spread Qualification",
                "purpose": (
                    "Qualify a subject-to acquisition and proposed wraparound sale before "
                    "committing acquisition cash. Connect verified underlying debt, seller "
                    "authority, buyer repayment capacity, property condition, and acceleration "
                    "exposure to a documented spread decision that survives independent "
                    "title, servicing, and licensed origination review."
                ),
                "chapter_ref": "Q1, Q2, Q6",
                "instructions": [
                    (
                        "Build one evidence folder per property using a stable deal identifier. "
                        "Collect seller-authorized mortgage statements, title evidence, insurance "
                        "declarations, tax records, and repair estimates before entering terms; "
                        "record source dates so stale balances cannot silently drive pricing."
                    ),
                    (
                        "Separate the seller's continuing loan obligation from your acquisition "
                        "of title. Have transaction counsel examine the actual transfer provisions "
                        "and statutory exceptions, then price an acceleration response without "
                        "assuming that timely payments prevent lender enforcement."
                    ),
                    (
                        "Route every proposed owner-occupant wrap buyer through a licensed "
                        "residential mortgage loan originator. Require verified income, obligations, "
                        "credit evidence, and documented repayment analysis before setting final "
                        "terms; seller motivation and buyer cash do not replace underwriting."
                    ),
                    (
                        "Compute interest contribution and cash payment spread separately using "
                        "dated amortization schedules. Identify principal movements, escrow "
                        "collections, acquisition basis, and servicing costs explicitly; a positive "
                        "monthly receipt difference can coexist with weak economics or inadequate "
                        "liquidity."
                    ),
                    (
                        "Approve only a fully evidenced property, seller, buyer, and servicing "
                        "combination. Assign each unresolved defect an owner and resolution date; "
                        "reject transactions requiring hidden transfers, inflated buyer income, "
                        "unsupported valuation, or reserve funding dependent on immediate resale."
                    ),
                ],
                "fields": [
                    field(
                        "Deal identity and title authority",
                        "textarea",
                        "Record the property identifier, vesting, seller authority, existing liens, "
                        "and evidence dates. Explain who independently reconciled the title "
                        "commitment against seller statements and which unresolved interests "
                        "would stop acquisition.",
                        "Deal STW-035-001 covers a $255,000 proposed resale property. The title "
                        "commitment dated June 3 lists one $200,000 mortgage and no junior "
                        "deed of trust. Both vested sellers sign through the title company; "
                        "the closer must clear a recorded judgment before funds move.",
                    ),
                    field(
                        "Underlying debt evidence and payment status",
                        "textarea",
                        "Capture the unpaid principal, contractual rate, remaining term, principal "
                        "and interest payment, escrow amount, arrears, and modification history. "
                        "Distinguish servicer-confirmed figures from seller estimates and identify "
                        "the next payment deadline.",
                        "The authorized servicer statement shows $200,000 principal, 3.00% fixed "
                        "interest, and 360 remaining monthly payments after a documented "
                        "recast. Principal and interest equal approximately $843.21; tax and "
                        "insurance escrow adds $400.00. The account is current, with the "
                        "next $1,243.21 payment due July 1.",
                    ),
                    field(
                        "Seller objective and acquisition consideration",
                        "textarea",
                        "Describe the seller's verified objective, proposed cash consideration, "
                        "existing arrears allocation, and continuing exposure on the underlying "
                        "note. State the communications and documentary evidence required before "
                        "the seller accepts the structure.",
                        "The sellers seek relocation cash rather than a mortgage release. "
                        "The acquisition offers $10,000 equity consideration and identifies "
                        "$5,000 of separately classified transaction costs. Written acknowledgments "
                        "explain that title transfer does not release the sellers from their "
                        "existing loan and that acceleration remains possible.",
                    ),
                    field(
                        "Property condition and valuation support",
                        "textarea",
                        "Document comparable sales, inspection findings, occupancy, repair scope, "
                        "and taxes supporting the proposed resale price. Identify deferred work "
                        "that could impair habitability, insurance placement, borrower affordability, "
                        "or a realistic liquidation exit.",
                        "Three closed comparable sales support a $250,000 to $260,000 range; "
                        "the proposed price is $255,000. An independent inspection identifies "
                        "$6,000 of roof and electrical work. The acquisition budget funds "
                        "those repairs separately, and the licensed contractor must complete "
                        "them before buyer occupancy.",
                    ),
                    field(
                        "Wrap buyer and licensed RMLO file",
                        "textarea",
                        "Identify the buyer's intended occupancy and the licensed RMLO responsible "
                        "for underwriting. Record verified income, employment, obligations, "
                        "credit authorization, available cash, and the location of the documented "
                        "repayment analysis.",
                        "The owner-occupant buyer provides verified monthly gross income "
                        "of $6,500, recurring debt payments of $650, and documented funds "
                        "for a $25,000 down payment. The NMLS-verified RMLO evaluates a "
                        "$1,930.20 projected housing payment, approximately 39.70% total "
                        "debt-to-income, and verified post-closing reserves before recommending terms.",
                    ),
                    field(
                        "Wrap terms and amortization comparison",
                        "textarea",
                        "Enter the sale price, down payment, wrap principal, fixed rate, "
                        "amortization period, payment, and maturity. Compare both amortization "
                        "schedules and explain why scheduled cash spread differs from the "
                        "first month's interest contribution.",
                        "A $255,000 sale less $25,000 down creates a $230,000 wrap at "
                        "7.00% over 360 months, approximately $1,530.20 principal and interest. "
                        "Against $843.21 underlying debt service, cash spread is $686.99. "
                        "First-month interest contribution is $1,341.67 less $500.00, or "
                        "$841.67, before servicing and credit costs.",
                    ),
                    field(
                        "Due-on-sale analysis and acceleration funding",
                        "textarea",
                        "Summarize counsel's review of the underlying transfer clause, applicable "
                        "federal exceptions, and lender communication strategy. Identify an "
                        "executable payoff or sale response, including funding evidence, rather "
                        "than treating lender silence as consent.",
                        "Counsel reviews 12 U.S.C. §1701j-3 and 12 CFR Part 591 against "
                        "the proposed deed transfer. No protected exception is assumed. "
                        "A documented $205,000 payoff funding proposal remains subject to "
                        "fresh underwriting; without executable funding or a supported sale "
                        "exit, the deal cannot advance.",
                    ),
                    field(
                        "Insurance, tax, and servicing feasibility",
                        "textarea",
                        "Confirm that ownership, occupancy, insured interests, property taxes, "
                        "and underlying escrow obligations can be administered accurately. Name "
                        "the licensed third-party servicer and describe how payment verification "
                        "reaches both affected counterparties every month.",
                        "The insurance broker quotes coverage reflecting actual ownership "
                        "and owner occupancy, with lender interests correctly documented. "
                        "The proposed licensed servicer allocates $400 monthly to the "
                        "underlying escrow obligation and supplies payment confirmations. "
                        "The title company verifies current taxes; no duplicate tax reserve "
                        "is charged as revenue.",
                    ),
                    field(
                        "Stress case and concentration limits",
                        "textarea",
                        "Test buyer delinquency, repair overrun, increased escrow, acceleration, "
                        "and a slower property exit. Quantify the cash required under combined "
                        "stress and define portfolio exposure limits that remain workable "
                        "without new acquisitions.",
                        "Six months of underlying payments require $7,459.26 at $1,243.21 "
                        "monthly. Add $12,000 for case-specific enforcement and property "
                        "work, producing $19,459.26 before additional sale costs. A $20,000 "
                        "deal reserve nearly covers that scenario but does not cover "
                        "a $205,000 acceleration payoff; separate funding is necessary.",
                    ),
                    field(
                        "Qualification decision and exception owner",
                        "textarea",
                        "Write an explicit proceed, reprice, or reject decision supported by "
                        "the file. Assign each remaining exception a responsible professional, "
                        "required evidence, deadline, and consequence if the condition cannot "
                        "be resolved.",
                        "Decision: reprice and hold funding. The title company must release "
                        "the judgment, the RMLO must complete repayment analysis, and the "
                        "capital provider must document executable payoff terms. The operator "
                        "will not substitute projected appreciation for those conditions; "
                        "failure by June 14 cancels the proposed acquisition.",
                    ),
                ],
                "completion_gate": (
                    "Proceed only when title authority, current debt, licensed buyer "
                    "underwriting, accurate insurance, servicing feasibility, and an "
                    "executable acceleration response are documented; record the named "
                    "reviewers and retain the rejected-deal rationale when any condition fails."
                ),
            },
            {
                "worksheet_id": "ws-02",
                "number": 2,
                "title": "Unit Economics, Escrow Float & Working-Capital Calculator",
                "purpose": (
                    "Translate contract economics into retained operator revenue, owner "
                    "profit, and usable cash without counting home value, note principal, "
                    "or custodial collections as sales. Reconcile the three canonical "
                    "scenarios while separately funding acquisition outlays, restricted "
                    "escrow, default reserves, and acceleration liquidity."
                ),
                "chapter_ref": "Q3, Q4",
                "instructions": [
                    (
                        "Create separate columns for gross customer cash, principal movements, "
                        "custodial escrow, retained interest contribution, and recognized upfront "
                        "spread. Obtain an accounting policy for each contract form before "
                        "mapping operational cash receipts into the Formula v2.0 scorecard."
                    ),
                    (
                        "Import the underlying and wrap amortization schedules using the same "
                        "payment dates and rounding convention. Reconcile opening principal, "
                        "interest, principal reduction, and ending principal each month; do "
                        "not annualize the first month's margin as an exact forecast."
                    ),
                    (
                        "Treat tax and insurance collections as restricted liabilities until "
                        "properly disbursed. Maintain reserve cash outside the operating "
                        "distribution account, and distinguish cash transfers into reserves "
                        "from recognized expenses, expected credit losses, and subsequent "
                        "actual expenditures."
                    ),
                    (
                        "Reproduce Conservative, Base, and Scaled revenue and profit exactly "
                        "before adding local assumptions. Build a bridge from recurring "
                        "overhead and additional delivery costs to total annual expense, "
                        "keeping debt-service pass-throughs outside recognized operator revenue."
                    ),
                    (
                        "Stress the opening cash budget independently from annual profitability. "
                        "Identify the timing of acquisition funds, buyer receipts, repairs, "
                        "servicing setup, and reserve deposits; prevent distributions whenever "
                        "the unrestricted cash forecast falls below the documented operating floor."
                    ),
                ],
                "fields": [
                    field(
                        "Revenue recognition and retained-share mapping",
                        "textarea",
                        "Define which contractual amounts enter the scorecard and which remain "
                        "principal, liabilities, or pass-throughs. Document the accountant's "
                        "treatment of upfront spreads and interest, including any principal-versus-agent "
                        "assessment relevant to gross billings.",
                        "For this workbook, scorecard revenue means retained upfront spread "
                        "plus retained annual wrap interest contribution. A $255,000 property "
                        "price and $230,000 wrap principal are excluded. The accountant "
                        "assesses ASC 606 only where applicable to customer contracts; "
                        "loan interest and property-sale accounting follow their applicable guidance.",
                    ),
                    field(
                        "Upfront cash bridge and recognized spread",
                        "textarea",
                        "Bridge the buyer's initial receipt to acquisition consideration, "
                        "transaction costs, restricted deposits, and retained cash. Explain "
                        "which amounts the accounting policy recognizes immediately and which "
                        "require deferral or a different classification.",
                        "A $25,000 buyer down payment less $10,000 seller consideration "
                        "and $5,000 acquisition costs leaves $10,000 cash before repairs "
                        "and reserves. That arithmetic alone does not establish recognized "
                        "revenue. The accountant must document any recognized upfront "
                        "spread and prevent the same $5,000 cost from being deducted twice.",
                    ),
                    field(
                        "Monthly interest and principal reconciliation",
                        "textarea",
                        "Calculate one month's borrower interest, underlying interest, both "
                        "principal reductions, and cash spread from actual schedules. Explain "
                        "how principal timing changes liquidity without changing the definition "
                        "of retained interest contribution.",
                        "Month one produces $1,341.67 wrap interest and $500.00 underlying "
                        "interest, leaving $841.67 contribution. Buyer principal is $188.53; "
                        "underlying principal reduction is $343.21. Therefore $841.67 plus "
                        "$188.53 less $343.21 equals $686.99 cash spread, before servicing "
                        "fees, escrow movements, and other operating expenditures.",
                    ),
                    field(
                        "Escrow liability and reserve segregation",
                        "textarea",
                        "Specify the bank accounts, beneficiary ledgers, authorized disbursements, "
                        "and reconciliation cadence for escrow and operating reserves. Quantify "
                        "the amount unavailable for owner distributions and explain how "
                        "shortages are detected.",
                        "Ten buyers each remit $400 of monthly escrow, creating $4,000 "
                        "of collections owed for designated tax and insurance obligations. "
                        "The servicer reconciles individual balances to the custodial account "
                        "and underlying remittances. A separate $20,000 company-funded default "
                        "reserve remains restricted by operating policy, not classified as revenue.",
                    ),
                    field(
                        "Conservative canonical scenario",
                        "textarea",
                        "Reconcile annual recognized operator revenue, net margin, owner net "
                        "profit, and total expense to the Conservative benchmark. Provide "
                        "an illustrative contribution mix and expense bridge without equating "
                        "the benchmark to property transaction volume.",
                        "Conservative revenue is $100,000: illustratively $40,000 recognized "
                        "upfront spreads plus $60,000 retained annual interest contribution. "
                        "Expenses total $72,000, comprising $24,000 recurring overhead and "
                        "$48,000 additional delivery and risk costs. Owner net profit "
                        "is exactly $28,000 at 28%, staffed by 1 FT plus 3 C.",
                    ),
                    field(
                        "Base canonical scenario",
                        "textarea",
                        "Reconcile the Base benchmark using retained operator revenue and "
                        "a complete expense bridge. State the staffing model and explain "
                        "why neither serviced loan balances nor buyer principal collections "
                        "increase the revenue target.",
                        "Base revenue is $475,000: illustratively $175,000 recognized upfront "
                        "spreads plus $300,000 retained annual interest contribution. Annual "
                        "expenses equal $285,000, split between $96,000 recurring overhead "
                        "and $189,000 additional delivery and risk costs. Owner net profit "
                        "is $190,000 at 40.0%, with 1 FT plus 3 C.",
                    ),
                    field(
                        "Scaled canonical scenario",
                        "textarea",
                        "Reconcile the Scaled Small-Team benchmark and identify the required "
                        "staffing and expense discipline. Preserve the canonical profit "
                        "calculation while separating illustrative expense allocations from "
                        "any claim about an individual property's expected performance.",
                        "Scaled revenue is $850,000: illustratively $350,000 recognized "
                        "upfront spreads plus $500,000 retained annual interest contribution. "
                        "Expenses equal $408,000, comprising $144,000 recurring overhead "
                        "and $264,000 additional delivery and risk costs. Owner net profit "
                        "is $442,000 at 52%, supported by 2 FT plus 4 C.",
                    ),
                    field(
                        "Startup cash and funding sequence",
                        "textarea",
                        "Build a dated startup cash schedule within the stated capital "
                        "range, separating operating runway from property-level commitments. "
                        "Identify the highest cumulative cash requirement and which expenses "
                        "must be funded before receiving buyer money.",
                        "A $55,000 opening budget allocates $15,000 to seller consideration "
                        "and acquisition costs, $6,000 to repairs, $20,000 to default "
                        "reserves, $8,000 to two months of operating runway, and $6,000 "
                        "to diligence and setup. This fits the $12,000–$65,000 range "
                        "but excludes a separately funded acceleration payoff.",
                    ),
                    field(
                        "Delinquency carrying cost and liquidity test",
                        "textarea",
                        "Model missed buyer payments without suspending underlying mortgage "
                        "payments. Include servicing, taxes, insurance, property work, and "
                        "case-specific enforcement costs; identify how many months the "
                        "segregated reserve actually supports before additional capital is needed.",
                        "At $1,243.21 underlying payment plus $35 monthly servicing, "
                        "six months cost $7,669.26. Adding $12,000 enforcement and "
                        "property work brings stress usage to $19,669.26, leaving "
                        "$330.74 from a $20,000 reserve. This test excludes acceleration "
                        "payoff and must be expanded for longer state-specific timelines.",
                    ),
                    field(
                        "Distribution policy and accounting close",
                        "textarea",
                        "State the monthly conditions for owner distributions, including "
                        "reconciled custodial balances, current underlying payments, reserve "
                        "minimums, and recognized profit. Specify who resolves differences "
                        "between earnings and cash before any withdrawal.",
                        "The controller releases distributions only after all ten underlying "
                        "payments are verified, escrow reconciles to individual ledgers, "
                        "and the $20,000 reserve floor remains intact. A $12,000 "
                        "accounting profit with only $7,000 unrestricted cash permits "
                        "no more than $7,000 before additional operating runway requirements "
                        "are applied.",
                    ),
                ],
                "completion_gate": (
                    "All three canonical scenarios reconcile exactly: $100,000/$28,000, "
                    "$475,000/$190,000, and $850,000/$442,000 revenue/profit. Principal "
                    "and escrow remain outside operator revenue, expense classifications "
                    "avoid double counting, and the dated cash forecast funds every "
                    "required reserve and closing outlay."
                ),
            },
            {
                "worksheet_id": "ws-03",
                "number": 3,
                "title": "Execution, Idempotent Ledger & QA Pre-Flight",
                "purpose": (
                    "Convert an approved transaction into a repeatable closing and "
                    "servicing process with evidence at every handoff. Establish immutable "
                    "event identifiers, balanced journals, controlled corrections, and "
                    "independent underlying-payment verification so duplicate messages "
                    "or missing receipts cannot distort balances or trigger duplicate transfers."
                ),
                "chapter_ref": "Q7, Q8",
                "instructions": [
                    (
                        "Map the transaction from signed acquisition documents through "
                        "recording, buyer origination, servicing activation, and the first "
                        "verified underlying payment. Give each handoff one accountable owner, "
                        "required evidence, and a stop condition that prevents premature "
                        "fund movement."
                    ),
                    (
                        "Use stable identifiers for properties, loans, counterparties, payment "
                        "events, and journal batches. Enforce uniqueness in the ledger store "
                        "rather than relying on spreadsheet appearance; retries must retrieve "
                        "existing results instead of posting an additional receipt or disbursement."
                    ),
                    (
                        "Preserve original events and correct errors through linked reversals "
                        "and replacement entries. Store amounts as integer cents, timestamps "
                        "with time zones, and source references; never erase a prior "
                        "posting merely because a bank return arrives later."
                    ),
                    (
                        "Run a three-way reconciliation among bank activity, the licensed "
                        "servicer's loan ledger, and the operator's accounting records. "
                        "Verify the underlying lender's receipt separately because a "
                        "successful outbound transfer does not prove correct loan-level "
                        "application."
                    ),
                    (
                        "Complete a rehearsal using duplicate notifications, partial payments, "
                        "returned payments, and delayed statements before activating production "
                        "autopay. Require independent review of the first live cycle and "
                        "record both the actual result and unresolved exceptions."
                    ),
                ],
                "fields": [
                    field(
                        "Closing sequence and evidence handoffs",
                        "textarea",
                        "List each closing dependency in execution order, including title "
                        "clearance, final underwriting, signed documents, funding authorization, "
                        "recording confirmation, and servicing setup. Name the recipient and "
                        "evidence required for each completed handoff.",
                        "The RMLO delivers the final buyer file to the closer; counsel "
                        "confirms the document package; the title company verifies cleared "
                        "funds and recording instructions. Servicing activation follows "
                        "document validation and confirmed closing. The operator retains "
                        "the recorded instrument reference and first-payment schedule under "
                        "deal STW-035-001.",
                    ),
                    field(
                        "Canonical identifiers and source of truth",
                        "textarea",
                        "Define immutable identifiers for the property, underlying loan, wrap "
                        "loan, buyer, servicing account, and payment. Explain how external "
                        "references map to internal records without exposing full account "
                        "numbers in routine dashboards.",
                        "Property P035001 links to underlying loan U035001 and wrap "
                        "loan W035001. The servicer account reference is stored in "
                        "an access-controlled mapping, while dashboards display only the "
                        "final four digits. PostgreSQL holds the canonical relationships; "
                        "Airtable displays workflow status but cannot alter posted loan "
                        "balances.",
                    ),
                    field(
                        "Idempotency key and duplicate handling",
                        "textarea",
                        "Specify the unique event key, database constraint, transaction boundary, "
                        "and retry response for payment intake. Explain how the process "
                        "distinguishes a genuine second payment from a repeated notification "
                        "of the first payment.",
                        "The intake key combines servicer identifier, external payment "
                        "identifier, and event type. A PostgreSQL unique constraint rejects "
                        "a second posting of receipt PAY7842. The handler returns "
                        "the existing journal reference; a separate PAY7843 remains "
                        "eligible even when its amount and date match the first "
                        "payment.",
                    ),
                    field(
                        "Receipt allocation and balanced journals",
                        "textarea",
                        "Describe how one buyer receipt is allocated across interest, "
                        "principal, and escrow according to the contract and accounting "
                        "policy. Show the balancing entry and keep subsequent underlying "
                        "debt service separately traceable.",
                        "For a $1,930.20 receipt, debit cash $1,930.20, credit wrap "
                        "interest $1,341.67, credit note receivable $188.53, and credit "
                        "escrow liability $400.00. Separately allocate the $843.21 "
                        "underlying principal-and-interest payment to $500.00 interest "
                        "and $343.21 principal, with escrow remittance recorded through "
                        "the custodial reconciliation.",
                    ),
                    field(
                        "Returned payment and correction protocol",
                        "textarea",
                        "Define how bank returns, allocation errors, and charge reversals "
                        "affect cash, borrower balances, and downstream tasks. Preserve "
                        "the original transaction and specify review before adding any "
                        "contractual fee or changing delinquency status.",
                        "Receipt PAY7842 for $1,930.20 returns unpaid two banking days "
                        "after posting. A linked reversal restores the receivable and "
                        "escrow balances and removes the cash. The servicer reviews "
                        "permitted fees and borrower notices; the underlying payment "
                        "still proceeds from company reserves rather than being silently "
                        "canceled.",
                    ),
                    field(
                        "Underlying-payment independent verification",
                        "textarea",
                        "Record how the operator confirms that the underlying lender "
                        "received and correctly applied each scheduled payment. Define "
                        "the evidence deadline, escalation owner, and treatment of "
                        "unapplied funds or missing lender confirmation.",
                        "The licensed servicer sends $1,243.21 for the July underlying "
                        "payment. Operations matches its transfer reference to the "
                        "authorized lender statement showing $843.21 principal and "
                        "interest plus $400.00 escrow. Missing confirmation after "
                        "two business days creates an exception; a bank debit alone "
                        "does not close the task.",
                    ),
                    field(
                        "Cash, servicing, and accounting reconciliation",
                        "textarea",
                        "Specify the three records reconciled, acceptable rounding treatment, "
                        "unmatched-item aging, and reviewer independence. Explain how aggregated "
                        "bank deposits are broken into individual loan receipts without "
                        "using unexplained balancing entries.",
                        "A $19,302.00 bank deposit must match ten $1,930.20 loan "
                        "receipts, their allocation journals, and the servicer batch "
                        "report. The bookkeeper prepares the reconciliation; the owner "
                        "reviews it. A missing $1,930.20 item remains in a dated "
                        "exception queue rather than being booked as miscellaneous "
                        "income.",
                    ),
                    field(
                        "Document access and audit evidence",
                        "textarea",
                        "Define access rights, retention ownership, version control, and "
                        "evidence linking for signed documents and borrower records. "
                        "Specify which sensitive information is excluded from operational "
                        "notifications and how access changes are reviewed.",
                        "Signed notes and disclosures reside in an encrypted document "
                        "repository with role-based access and multifactor authentication. "
                        "The acquisition contractor sees property status but not tax "
                        "returns. The audit record stores document version, SHA-256 "
                        "digest, reviewer, and timestamp; weekly access review removes "
                        "departed contractors before further file access.",
                    ),
                    field(
                        "Pre-flight test cases and observed outcomes",
                        "textarea",
                        "List executable tests for duplicates, partial receipts, returns, "
                        "holiday timing, and absent lender confirmation. Record expected "
                        "ledger effects and actual observed results separately so a "
                        "test plan is never mistaken for completed verification.",
                        "Planned case T03 submits PAY7842 twice and expects one "
                        "receipt journal. Planned case T04 returns that receipt "
                        "and expects one linked reversal. Planned case T05 omits "
                        "lender confirmation and expects escalation. These are workbook "
                        "examples, not executed tests; the operator must attach actual "
                        "results before activation.",
                    ),
                    field(
                        "First-cycle acceptance and operational handover",
                        "textarea",
                        "Define the first live cycle's acceptance criteria and handover "
                        "packet. Include borrower payment instructions, escrow allocation, "
                        "underlying receipt, reconciled statements, and named ownership "
                        "of any exception remaining after closing.",
                        "The first-cycle packet contains the $1,930.20 buyer receipt, "
                        "$1,243.21 underlying remittance confirmation, $35 servicing fee, "
                        "and reconciled loan balances. Operations and the bookkeeper "
                        "sign independently. A disputed allocation stays assigned to "
                        "the licensed servicer, and distributions remain suspended until "
                        "the exception is resolved.",
                    ),
                ],
                "completion_gate": (
                    "Activate routine servicing only after signed documents are linked, "
                    "duplicate and reversal tests have recorded passing results, the "
                    "first underlying payment is independently verified, and bank, "
                    "servicer, and accounting balances reconcile with no unexplained difference."
                ),
            },
            {
                "worksheet_id": "ws-04",
                "number": 4,
                "title": "Statutory, Licensing, Contract Addendum & Compliance Audit",
                "purpose": (
                    "Build a transaction-specific legal and operational evidence register "
                    "covering transfer restrictions, origination, repayment analysis, "
                    "disclosures, servicing, privacy, and enforcement. Translate each "
                    "applicable requirement into a document, responsible professional, "
                    "delivery deadline, and retained proof rather than relying on "
                    "general seller-financing assumptions."
                ),
                "chapter_ref": "Q5, Q9",
                "instructions": [
                    (
                        "Determine the property state, buyer occupancy, transaction purpose, "
                        "creditor status, and parties' activities before selecting statutory "
                        "requirements. Have counsel distinguish federal coverage, state "
                        "licensing, and contractual duties; a narrow exemption in one "
                        "category does not resolve the others."
                    ),
                    (
                        "Verify the RMLO and servicing provider through the relevant "
                        "licensing records and confirm their actual scope of engagement. "
                        "Retain dated evidence and require written responsibility for "
                        "underwriting, disclosures, payment administration, and escalation "
                        "rather than relying on marketing descriptions."
                    ),
                    (
                        "Create a delivery calendar from the current law and actual "
                        "transaction facts. Identify required recipients, document versions, "
                        "delivery methods, waiting periods, and proof of receipt; do "
                        "not assume a generic closing checklist satisfies state wraparound "
                        "requirements."
                    ),
                    (
                        "Review buyer-facing and seller-facing contracts together so "
                        "payment duties, acceleration exposure, cure rights, servicing "
                        "access, insurance interests, and payoff procedures are consistent. "
                        "Use transaction counsel's completed instruments rather than "
                        "treating workbook example language as executable loan documents."
                    ),
                    (
                        "Complete a final evidence review before funding and repeat "
                        "the relevant checks after material changes. Preserve reasons "
                        "for adverse credit decisions, borrower communications, and servicing "
                        "exceptions according to a documented retention schedule tied "
                        "to applicable requirements."
                    ),
                ],
                "fields": [
                    field(
                        "Jurisdiction and transaction coverage matrix",
                        "textarea",
                        "Identify property location, occupancy, borrower purpose, creditor "
                        "activity, and governing instruments. Map each fact to the "
                        "federal and state provisions requiring professional review, "
                        "including exceptions that must be established rather than presumed.",
                        "The example property is in Texas, and the buyer will "
                        "occupy it as a principal residence. Counsel evaluates "
                        "Tex. Prop. Code §5.016 and Texas Finance Code Chapter "
                        "159, along with applicable federal consumer-credit provisions. "
                        "The file separately records origination licensing, disclosure "
                        "coverage, and servicing requirements.",
                    ),
                    field(
                        "Transfer restriction and due-on-sale memorandum",
                        "textarea",
                        "Record the underlying contract's transfer language and counsel's "
                        "analysis under federal due-on-sale law. Explain whether a "
                        "specific protected transfer applies and document the practical "
                        "funding response if the lender accelerates.",
                        "The memorandum cites 12 U.S.C. §1701j-3 and 12 CFR "
                        "Part 591, quotes the mortgage transfer clause, and "
                        "finds no established exception for the proposed investor "
                        "acquisition. No trust or entity transfer is described "
                        "as automatic protection. The seller acknowledgment and "
                        "capital plan address continuing acceleration exposure.",
                    ),
                    field(
                        "RMLO licensing and engagement scope",
                        "textarea",
                        "Verify the individual and sponsoring entity responsible for "
                        "origination, including state authority, license status, engagement "
                        "scope, and evidence date. Explain how compensation and "
                        "responsibilities are documented before borrower application work begins.",
                        "Operations checks the RMLO's active Texas authority through "
                        "NMLS Consumer Access and retains the dated result. "
                        "The engagement covers application intake, verified repayment "
                        "analysis, and applicable disclosures. Counsel reviews the "
                        "SAFE Act framework at 12 U.S.C. §§5101–5117 and "
                        "applicable state implementing requirements before origination starts.",
                    ),
                    field(
                        "Ability-to-repay and product review",
                        "textarea",
                        "Identify the documented repayment factors, product terms, and "
                        "applicable creditor obligations. Record any claimed exemption "
                        "with counsel's factual basis while maintaining this operating "
                        "policy's licensed RMLO underwriting for every owner-occupant buyer.",
                        "The RMLO evaluates income, assets, employment, existing obligations, "
                        "mortgage-related costs, credit history, and the proposed payment "
                        "under the applicable 15 U.S.C. §1639c and 12 CFR "
                        "§1026.43 framework. Counsel separately reviews 12 CFR "
                        "§1026.36 seller-financer provisions; those provisions are "
                        "not treated as a blanket repayment-analysis exemption.",
                    ),
                    field(
                        "Texas wrap and existing-lien disclosures",
                        "textarea",
                        "Create a counsel-verified register for existing-lien and wrap "
                        "disclosures, recipients, required content, statutory timing, and "
                        "delivery evidence. Distinguish the property-code requirements "
                        "from the finance-code requirements and record applicability separately.",
                        "The Texas packet separately tracks Tex. Prop. Code "
                        "§5.016 and Texas Finance Code Chapter 159. Counsel "
                        "enters the applicable delivery deadlines and required "
                        "recipients before scheduling closing. The closer retains "
                        "dated versions and delivery proof; signing the deed "
                        "does not substitute for completing required earlier "
                        "disclosure steps.",
                    ),
                    field(
                        "Credit decisions and adverse-action records",
                        "textarea",
                        "Specify authorized credit access, consistent underwriting criteria, "
                        "decision ownership, and applicable notification duties. Identify "
                        "the record retained when an application is declined "
                        "or changed because of credit information or verified affordability.",
                        "The RMLO obtains a permissible purpose and appropriate "
                        "authorization before requesting credit under 15 U.S.C. "
                        "§1681b. If the application is declined, the responsible "
                        "creditor evaluates ECOA and 12 CFR §1002.9 notice "
                        "duties, plus applicable 15 U.S.C. §1681m requirements. "
                        "The file retains actual reasons rather than generic "
                        "rejection language.",
                    ),
                    field(
                        "Servicing, escrow, and borrower information",
                        "textarea",
                        "Document servicing-provider authority, payment allocation rules, "
                        "escrow handling, statement delivery, and borrower error "
                        "channels. Determine which federal servicing provisions apply "
                        "and identify state duties that remain regardless of "
                        "a federal exemption.",
                        "Counsel and the licensed servicer assess 12 U.S.C. "
                        "§2605, 12 CFR §1024.17, and 12 CFR §1026.41 "
                        "for this loan and provider. The contract requires "
                        "monthly underlying-payment evidence and a documented borrower "
                        "inquiry channel. Escrow collections remain separately reconciled "
                        "even when a particular federal provision does not "
                        "apply.",
                    ),
                    field(
                        "Contract addenda and operational covenants",
                        "textarea",
                        "List the counsel-drafted provisions necessary to allocate "
                        "underlying-payment duties, insurance maintenance, information access, "
                        "payoff processing, and default remedies. Identify inconsistencies "
                        "between the wrap note, security instrument, purchase contract, "
                        "and servicing agreement.",
                        "Counsel's drafting instruction states: require monthly evidence "
                        "of underlying payment, authorize appropriate servicing information "
                        "access, specify the payoff calculation method, and "
                        "identify lawful remedies for payment failure. The "
                        "servicing agreement must support those duties operationally. "
                        "A ten-day internal reporting target cannot shorten "
                        "any statutory borrower notice period.",
                    ),
                    field(
                        "Default, foreclosure, and bankruptcy response",
                        "textarea",
                        "Identify the professionals responsible for default notices, "
                        "loss-mitigation review, foreclosure, and bankruptcy monitoring. "
                        "State which actions must stop when new facts "
                        "change the permitted enforcement path and how carrying "
                        "costs remain funded.",
                        "Texas counsel evaluates Tex. Prop. Code §51.002 "
                        "and applicable federal servicing requirements before "
                        "enforcement. A bankruptcy filing triggers immediate "
                        "review of 11 U.S.C. §362 before collection "
                        "activity continues. Operations preserves the $20,000 "
                        "reserve and keeps the underlying loan current; "
                        "no contractor changes locks or pressures occupants "
                        "outside the lawful process.",
                    ),
                    field(
                        "Privacy controls and evidence sign-off",
                        "textarea",
                        "Map borrower information flows, service-provider access, retention "
                        "duties, and incident responsibility. Identify applicable safeguards "
                        "requirements and record the final professional review of "
                        "licenses, disclosures, signed instruments, and delivery evidence "
                        "before funding.",
                        "The reviewer assesses GLBA obligations and 16 CFR "
                        "Part 314 applicability, restricts tax returns to "
                        "the RMLO and authorized reviewers, and requires "
                        "encrypted file exchange. Before funding, counsel "
                        "and operations confirm current licenses, completed "
                        "documents, and delivery evidence. Open disclosure "
                        "defects prevent closing until corrected through "
                        "the required process.",
                    ),
                ],
                "completion_gate": (
                    "Fund only after counsel and the licensed providers have documented "
                    "applicability, completed required underwriting and disclosures, verified "
                    "delivery timing, reconciled contractual duties, and assigned servicing "
                    "and enforcement responsibilities. Reopen the review when parties, "
                    "terms, occupancy, or closing dates materially change."
                ),
            },
            {
                "worksheet_id": "ws-05",
                "number": 5,
                "title": "Automation Pipeline, Acquisition Flywheel & Risk Fallback Tracker",
                "purpose": (
                    "Build a permissioned acquisition and servicing workflow that surfaces "
                    "low-equity opportunities without automating judgment or hiding risk. "
                    "Connect source provenance, seller conversations, qualified referrals, "
                    "licensed underwriting, and payment monitoring to measurable conversion "
                    "stages, exception handling, and tested manual recovery procedures."
                ),
                "chapter_ref": "Q6, Q10",
                "instructions": [
                    (
                        "Start with documented source permissions and defined acquisition "
                        "criteria rather than bulk collection. Label public-record signals "
                        "as leads requiring verification, and suppress contacts when "
                        "ownership, outreach restrictions, or seller preferences prevent "
                        "appropriate follow-up."
                    ),
                    (
                        "Create one pipeline record per property and maintain source "
                        "provenance through every stage. Use deduplication and explicit "
                        "stage criteria so repeated foreclosure records or broker "
                        "referrals do not inflate opportunity counts or generate "
                        "conflicting seller contacts."
                    ),
                    (
                        "Automate reminders, document completeness checks, and reconciliation "
                        "alerts while keeping credit decisions, contract interpretation, "
                        "and fund release with authorized professionals. Record "
                        "the inputs and event history behind every status "
                        "change so exceptions remain explainable."
                    ),
                    (
                        "Measure the acquisition flywheel using verified seller "
                        "conversations, qualified properties, completed RMLO files, "
                        "closed transactions, and performing notes. Include rejected "
                        "deal reasons and servicing quality when evaluating "
                        "channels; inexpensive leads can still create expensive "
                        "portfolio risk."
                    ),
                    (
                        "Maintain manual alternatives for each critical integration "
                        "and test them on a scheduled basis. An "
                        "outage must not cause duplicate payments, missed "
                        "underlying debt service, lost borrower notices, or "
                        "unreviewed changes to credit and closing decisions."
                    ),
                ],
                "fields": [
                    field(
                        "Lead sources and authorized collection",
                        "textarea",
                        "List acquisition sources, permitted use, refresh cadence, "
                        "and verification requirements. Explain how low-equity or "
                        "pre-foreclosure signals become research tasks without treating "
                        "distress as proof of seller willingness or transaction "
                        "suitability.",
                        "The operator reviews 40 county-record notices and "
                        "20 licensed-broker referrals weekly using authorized "
                        "access. Each record retains its source and "
                        "publication date. Staff verify ownership and "
                        "current loan status before discussing terms; "
                        "a foreclosure filing alone neither establishes "
                        "available equity nor authorizes access to "
                        "private mortgage information.",
                    ),
                    field(
                        "Outreach controls and seller communication",
                        "textarea",
                        "Define outreach channels, contact permissions, suppression handling, "
                        "and review of applicable communication rules. Describe "
                        "the seller-facing explanation of subject-to financing, "
                        "continuing liability, and acceleration exposure without "
                        "promising debt release or rescue.",
                        "Before telephone outreach, the campaign owner reviews "
                        "47 U.S.C. §227, 47 CFR §64.1200, "
                        "16 CFR Part 310, and applicable state "
                        "requirements. Suppressed contacts remain excluded. "
                        "The script explains that the seller's "
                        "mortgage stays outstanding and that a "
                        "title transfer can trigger lender action; "
                        "it never promises credit repair.",
                    ),
                    field(
                        "Deduplication and pipeline state machine",
                        "textarea",
                        "Specify property matching keys, permitted stage transitions, "
                        "required evidence, and duplicate resolution. Explain "
                        "how the system preserves multiple referral sources "
                        "while maintaining one accountable owner and one "
                        "current seller-contact plan.",
                        "Normalized parcel identifier plus county forms "
                        "the primary matching key. A second "
                        "broker referral attaches to P035001 rather "
                        "than creating another opportunity. Airtable "
                        "stages are sourced, verified, qualified, "
                        "underwritten, closing, and servicing. Movement "
                        "to qualified requires current debt evidence, "
                        "seller authority, preliminary valuation, and "
                        "a named acquisition owner.",
                    ),
                    field(
                        "Automated document collection and review",
                        "textarea",
                        "Identify documents requested automatically, expiry rules, "
                        "access restrictions, and professional review responsibilities. "
                        "Define what happens when a document is "
                        "missing, inconsistent, unreadable, or older than "
                        "the transaction's evidence policy permits.",
                        "An n8n workflow requests the authorized "
                        "mortgage statement, insurance declarations, and "
                        "tax record after seller permission is "
                        "recorded. A statement older than 30 "
                        "days creates a refresh task. Extracted "
                        "balances remain provisional until reviewed; "
                        "borrower income files route directly "
                        "to the licensed RMLO's secure "
                        "intake process.",
                    ),
                    field(
                        "Acquisition funnel and channel economics",
                        "textarea",
                        "Calculate conversion by documented stage and "
                        "attribute channel spending to qualified opportunities "
                        "and completed transactions. Separate planning assumptions "
                        "from observed results and include the "
                        "time lag between initial contact and "
                        "recognized contribution.",
                        "A planning funnel starts with 120 "
                        "records, 36 verified conversations, 12 "
                        "qualified properties, four complete files, "
                        "and one closing. At $2,400 "
                        "channel spend, planned cost per "
                        "qualified property is $200 and "
                        "cost per closing is $2,400. "
                        "Actual conversion replaces these assumptions "
                        "only after the cohort matures.",
                    ),
                    field(
                        "Licensed-servicer integration and event security",
                        "textarea",
                        "Describe the servicer data exchange, authentication, "
                        "event validation, access scope, and failure "
                        "response. Ensure automation can reconcile approved "
                        "events without independently changing loan terms "
                        "or issuing unrestricted transfers from borrower "
                        "accounts.",
                        "The servicer integration uses scoped credentials "
                        "stored outside workflow text, authenticated "
                        "notifications where supported, and an "
                        "allowlisted event schema. Receipt events "
                        "enter the idempotent ledger queue. "
                        "An unexpected amount or loan "
                        "identifier creates review work; automation "
                        "cannot rewrite the note rate "
                        "or initiate an unapproved borrower "
                        "debit.",
                    ),
                    field(
                        "Monthly tax, insurance, and payment audit",
                        "textarea",
                        "Define recurring checks for underlying payments, "
                        "tax status, insurance continuity, escrow changes, "
                        "and policy renewals. State the evidence "
                        "source, responsible reviewer, and escalation "
                        "timing for each detected discrepancy or "
                        "missing confirmation.",
                        "On the fifth business day, operations "
                        "matches every underlying receipt to "
                        "the lender record and reviews "
                        "escrow changes. Insurance renewals receive "
                        "45-day reminders; taxes receive a "
                        "county-record check before delinquency. "
                        "A premium increase from $1,800 "
                        "to $2,400 annually adds $50 "
                        "monthly to the affordability and "
                        "escrow review.",
                    ),
                    field(
                        "Servicer outage and manual fallback",
                        "textarea",
                        "Write the fallback for unavailable portals, "
                        "failed notifications, delayed remittances, and "
                        "bank interruptions. Specify who verifies "
                        "payment status before manual action "
                        "and how recovery avoids duplicate "
                        "underlying payments or duplicate ledger "
                        "entries.",
                        "If the portal is unavailable before "
                        "the July payment deadline, operations "
                        "calls the servicer through a "
                        "verified contact and checks the "
                        "bank record. An authorized manual "
                        "payment occurs only after duplicate "
                        "risk is resolved. Its reference "
                        "is linked to the original "
                        "obligation so restored automation "
                        "does not pay again.",
                    ),
                    field(
                        "Risk triggers and stop conditions",
                        "textarea",
                        "Define quantitative triggers for acquisition pauses, "
                        "distribution holds, professional escalation, and "
                        "additional reserves. Distinguish temporary system "
                        "faults from borrower distress and "
                        "lender enforcement so each event "
                        "receives the appropriate response.",
                        "Two unverified underlying payments, any "
                        "acceleration notice, or a reserve "
                        "balance below $20,000 pauses new "
                        "commitments. A buyer 15 days "
                        "past due enters the servicer's "
                        "applicable outreach process. An "
                        "acceleration notice goes directly "
                        "to counsel and the capital "
                        "provider; automated marketing never "
                        "resolves an enforcement event.",
                    ),
                    field(
                        "Referral flywheel and continuous improvement",
                        "textarea",
                        "Describe how performing-note evidence, transparent "
                        "seller communication, and documented closing "
                        "quality improve referrals. Assign review "
                        "cadence and channel changes using "
                        "actual results while checking any "
                        "compensation arrangement before making "
                        "referral payments.",
                        "Each quarter, the operator shares "
                        "aggregated payment-verification performance with "
                        "approved broker partners without "
                        "borrower data. A channel with "
                        "eight qualified files and zero "
                        "title-ready transactions is suspended. "
                        "Any proposed paid referral is "
                        "reviewed for applicable 12 U.S.C. "
                        "§2607 restrictions and state "
                        "requirements before compensation is "
                        "offered.",
                    ),
                ],
                "completion_gate": (
                    "Launch automated workflows only after source permissions, suppression "
                    "rules, deduplication, professional decision boundaries, and payment "
                    "fallbacks are documented. Record observed duplicate-event and outage "
                    "test results, and assign every high-risk alert to a named person "
                    "with an evidence-based resolution deadline."
                ),
            },
            {
                "worksheet_id": "ws-06",
                "number": 6,
                "title": "30-Day Launch Sprint, Pod KPI Scorecard & Exit-Readiness Ledger",
                "purpose": (
                    "Turn the first month into an evidence-producing operating sprint "
                    "rather than a forced closing deadline. Assign a small-team "
                    "pod, budget acquisition runway, measure file quality and servicing "
                    "integrity, and assemble transferable note records while preserving "
                    "the canonical annual scorecard and realistic deal timing."
                ),
                "chapter_ref": "Q11, Q12",
                "instructions": [
                    (
                        "Set the first month's objective as a functioning "
                        "acquisition, underwriting, closing, and servicing system. "
                        "Preserve the expected two-to-six-month first-deal horizon; "
                        "do not lower standards or assume immediate "
                        "revenue merely because the launch sprint "
                        "ends after 30 days."
                    ),
                    (
                        "Assign the founder and three contracted "
                        "specialists to explicit responsibilities, then "
                        "document supporting title, insurance, and "
                        "accounting vendors. Distinguish core staffing "
                        "from outside service organizations so "
                        "the team-efficiency claim does not "
                        "hide required professional work."
                    ),
                    (
                        "Budget monthly overhead separately from "
                        "property capital and reserves. Track "
                        "leading indicators during launch and "
                        "recognized revenue after eligible events "
                        "occur; compare annualized performance with "
                        "canonical scenarios only when the "
                        "cohort and timing support the "
                        "comparison."
                    ),
                    (
                        "Build the exit file from the "
                        "first transaction using signed documents, "
                        "recording evidence, servicing histories, "
                        "reconciled balances, and unresolved "
                        "risk disclosures. A potential "
                        "note buyer must be able "
                        "to reconstruct the asset without "
                        "relying on the founder's memory."
                    ),
                    (
                        "Finish day 30 with a written "
                        "continue, repair, or pause decision. "
                        "Record completed work, actual "
                        "test results, missing evidence, "
                        "remaining cash runway, and "
                        "next owners; neither a "
                        "polished dashboard nor a "
                        "full lead list substitutes "
                        "for an executable transaction."
                    ),
                ],
                "fields": [
                    field(
                        "Launch objective and benchmark identity",
                        "textarea",
                        "State the volume's operating thesis, "
                        "scorecard identity, and measurable "
                        "30-day objective. Distinguish the "
                        "ranking and annual scenario "
                        "benchmarks from evidence that "
                        "the current launch has "
                        "actually produced qualified opportunities "
                        "or recognized revenue.",
                        "Volume 035 is Candidate #35, "
                        "pipeline rank #09 of 36, "
                        "with a Money-to-Manpower Score "
                        "of 90/100. Day 30 "
                        "targets one complete practice "
                        "file, verified professional coverage, "
                        "and a tested servicing "
                        "workflow. First-deal planning "
                        "remains two to six "
                        "months; the score does "
                        "not create booked revenue.",
                    ),
                    field(
                        "Days 1–7 professional and capital setup",
                        "textarea",
                        "Assign first-week deliverables for "
                        "counsel, licensed origination, "
                        "servicing, banking, insurance, "
                        "and capital planning. Identify "
                        "the evidence that makes "
                        "each relationship operational "
                        "and the expense owner "
                        "responsible for staying "
                        "within the startup budget.",
                        "By day 7, the founder "
                        "obtains counsel's scope, "
                        "an NMLS-verified RMLO "
                        "engagement, a licensed-servicer "
                        "proposal, and bank-account "
                        "separation instructions. The "
                        "$55,000 startup plan "
                        "reserves $20,000 for "
                        "default carrying costs. "
                        "The capital file "
                        "separately documents the "
                        "requirements for any "
                        "acceleration funding commitment.",
                    ),
                    field(
                        "Days 8–14 acquisition and file rehearsal",
                        "textarea",
                        "Define the second week's "
                        "source validation, outreach, "
                        "qualification, and document "
                        "rehearsal targets. State "
                        "how staff handle "
                        "incomplete evidence and "
                        "which sample transactions "
                        "are educational exercises "
                        "rather than actual "
                        "funded opportunities.",
                        "Days 8–14 target 30 "
                        "verified property records, "
                        "eight appropriate seller "
                        "conversations, and two "
                        "evidence-based preliminary "
                        "screens. Staff rehearse "
                        "STW-035-001 as a "
                        "worked example only. "
                        "A missing lender "
                        "statement prevents "
                        "qualification; the "
                        "team does not "
                        "invent balances "
                        "to meet its "
                        "weekly target.",
                    ),
                    field(
                        "Days 15–21 underwriting and ledger tests",
                        "textarea",
                        "Set third-week deliverables for "
                        "licensed underwriting, disclosure "
                        "planning, amortization review, "
                        "event handling, and "
                        "reconciliation rehearsal. Specify "
                        "the observed evidence "
                        "required to distinguish "
                        "a completed test "
                        "from a planned "
                        "test or vendor "
                        "assurance.",
                        "Days 15–21 produce "
                        "one RMLO-reviewed "
                        "sample affordability "
                        "analysis and five "
                        "ledger test records. "
                        "The duplicate-receipt "
                        "test must leave "
                        "one $1,930.20 "
                        "receipt journal; "
                        "the return test "
                        "must create one "
                        "linked reversal. "
                        "The reviewer "
                        "attaches actual "
                        "outputs and "
                        "records failures "
                        "without labeling "
                        "them completed.",
                    ),
                    field(
                        "Days 22–30 readiness and next-month decision",
                        "textarea",
                        "Define the final week's "
                        "evidence review, remaining "
                        "cash forecast, transaction "
                        "readiness assessment, and "
                        "decision criteria. Identify "
                        "the next month's "
                        "work that can "
                        "continue safely if "
                        "no acquisition "
                        "has reached "
                        "funding readiness.",
                        "On day 30, the "
                        "founder reviews "
                        "professional coverage, "
                        "two qualified "
                        "property files, "
                        "recorded test "
                        "results, and "
                        "a 90-day "
                        "cash forecast. "
                        "With no "
                        "fundable deal, "
                        "the team "
                        "continues verified "
                        "sourcing and "
                        "buyer-file preparation "
                        "within budget. "
                        "It does "
                        "not recognize "
                        "projected spreads "
                        "or force "
                        "a closing.",
                    ),
                    field(
                        "Pod staffing and responsibility boundaries",
                        "textarea",
                        "Map the core staffing "
                        "model to acquisition, "
                        "licensed origination, "
                        "servicing control, "
                        "legal coordination, "
                        "and financial review. "
                        "Identify outside "
                        "vendor services "
                        "and explain "
                        "how their "
                        "costs remain "
                        "visible without "
                        "misstating core "
                        "team size.",
                        "Conservative and Base "
                        "use 1 FT "
                        "founder plus "
                        "3 C: "
                        "acquisition support, "
                        "a licensed "
                        "RMLO engagement, "
                        "and servicing-control "
                        "support. The "
                        "licensed servicing "
                        "company, counsel, "
                        "title company, "
                        "and accounting "
                        "firm remain "
                        "separately costed "
                        "vendors. Scaled "
                        "uses 2 FT "
                        "plus 4 C, "
                        "six core "
                        "people, without "
                        "removing required "
                        "professional services.",
                    ),
                    field(
                        "Pod KPI definitions and review cadence",
                        "textarea",
                        "Define each metric's "
                        "numerator, denominator, "
                        "source, owner, "
                        "and review "
                        "frequency. Balance "
                        "acquisition conversion "
                        "with underlying-payment "
                        "verification, reserve "
                        "adequacy, borrower "
                        "performance, and "
                        "reconciliation quality "
                        "so growth "
                        "cannot conceal "
                        "servicing deterioration.",
                        "Weekly acquisition "
                        "conversion equals "
                        "qualified files "
                        "divided by "
                        "verified conversations: "
                        "12 divided "
                        "by 36 "
                        "equals 33.33%. "
                        "Monthly payment "
                        "verification equals "
                        "confirmed underlying "
                        "receipts divided "
                        "by scheduled "
                        "payments, targeting "
                        "100%. Operations "
                        "also reports "
                        "past-due balances, "
                        "unmatched cash, "
                        "reserve coverage, "
                        "and exceptions "
                        "older than "
                        "two business "
                        "days.",
                    ),
                    field(
                        "Annual scorecard and expense accountability",
                        "textarea",
                        "Record the canonical "
                        "revenue, margin, "
                        "owner profit, "
                        "and staffing "
                        "benchmarks alongside "
                        "actual results. "
                        "Explain recurring "
                        "overhead versus "
                        "additional annual "
                        "delivery costs "
                        "and assign "
                        "variance review "
                        "without treating "
                        "portfolio principal "
                        "as revenue.",
                        "The annual "
                        "scorecard preserves "
                        "$100,000 revenue "
                        "and $28,000 "
                        "profit; $475,000 "
                        "and $190,000; "
                        "$850,000 and "
                        "$442,000. Margins "
                        "remain 28%, "
                        "40.0%, and "
                        "52%. Monthly "
                        "overhead examples "
                        "are $2,000, "
                        "$8,000, and "
                        "$12,000 within "
                        "the stated "
                        "range. Total "
                        "annual expenses "
                        "still reconcile "
                        "to $72,000, "
                        "$285,000, and "
                        "$408,000.",
                    ),
                    field(
                        "Note transfer and exit-readiness evidence",
                        "textarea",
                        "List the asset "
                        "documents, payment "
                        "history, lien "
                        "evidence, custody "
                        "records, and "
                        "transfer restrictions "
                        "required for "
                        "a potential "
                        "note sale. "
                        "Explain how "
                        "counsel verifies "
                        "enforcement rights "
                        "and protects "
                        "borrower information "
                        "during diligence.",
                        "The exit "
                        "folder contains "
                        "the original "
                        "note custody "
                        "record, endorsements, "
                        "recorded security "
                        "instrument, assignments, "
                        "payment history, "
                        "and underlying "
                        "loan status. "
                        "Counsel reviews "
                        "applicable UCC "
                        "§3-301 enforcement "
                        "issues and "
                        "state recording "
                        "requirements. Prospective "
                        "buyers receive "
                        "controlled diligence "
                        "access; underlying "
                        "acceleration exposure "
                        "is disclosed "
                        "rather than "
                        "removed from "
                        "the sale "
                        "narrative.",
                    ),
                    field(
                        "Scale, hold, or exit decision ledger",
                        "textarea",
                        "Write the decision "
                        "rule for "
                        "adding acquisitions, "
                        "holding the "
                        "portfolio, or "
                        "pursuing an "
                        "asset exit. "
                        "Include reserve "
                        "coverage, evidence "
                        "quality, valuation "
                        "haircuts, transaction "
                        "costs, and "
                        "responsibility for "
                        "remaining obligations "
                        "after any "
                        "transfer.",
                        "Scale only "
                        "after three "
                        "consecutive reconciled "
                        "cycles with "
                        "100% underlying-payment "
                        "verification and "
                        "funded reserves. "
                        "For an "
                        "illustrative $230,000 "
                        "wrap balance, "
                        "a 90% "
                        "sale price "
                        "is $207,000; "
                        "a $200,000 "
                        "underlying payoff "
                        "and $5,000 "
                        "costs leave "
                        "$2,000 before "
                        "other adjustments. "
                        "That cash "
                        "is not "
                        "automatically recognized "
                        "profit or "
                        "release from "
                        "all obligations.",
                    ),
                ],
                "completion_gate": (
                    "Close the sprint with a signed decision ledger, assigned core "
                    "and vendor responsibilities, an updated cash runway, actual test "
                    "evidence, and a complete list of unresolved transaction conditions. "
                    "Scale only after the specified servicing history and reserves "
                    "exist; preserve the two-to-six-month first-deal planning horizon."
                ),
            },
        ],
    }
