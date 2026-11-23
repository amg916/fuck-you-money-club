from __future__ import annotations


def build_volume_040_workbook() -> dict:
    def field(name: str, input_type: str, prompt: str, example: str) -> dict:
        return {
            "name": name,
            "type": input_type,
            "prompt": prompt,
            "example": example,
        }

    return {
        "workbook_id": "wb-040-self-funded-erisa-pbm-and-workers-comp-arbitrage",
        "volume_id": "vol-040-self-funded-erisa-pbm-and-workers-comp-arbitrage",
        "title": "Self-Funded Health, PBM & Workers' Comp Arbitrage — Operator Companion Workbook",
        "subtitle": (
            "6 Printable Operator Worksheets for ERISA Prospect Underwriting, "
            "Retained-Fee Economics, Stop-Loss and PBM Execution, Workers' Comp "
            "Recovery Controls, Licensed Delivery, and a Transferable Small-Team Practice"
        ),
        "worksheets": [
            {
                "worksheet_id": "ws-01",
                "number": 1,
                "title": "Arbitrage Deal / Counterparty Underwriting & Spread Qualification",
                "purpose": (
                    "Separate a defensible employer benefit improvement from an attractive "
                    "sales illustration. Underwrite the employer, plan, carrier, PBM, and "
                    "rating jurisdiction before proposing a transition. Establish which "
                    "savings are measurable, which fees the operator retains, and which "
                    "dependencies could prevent collection."
                ),
                "chapter_ref": "Q1, Q2, Q6",
                "instructions": [
                    (
                        "Start with the employer's legal identity, plan year, covered employee "
                        "count, current funding arrangement, and authorized decision maker. "
                        "Use public Form 5500 material for prospecting, then obtain employer "
                        "authorization before requesting nonpublic contracts or participant information."
                    ),
                    (
                        "Build separate health, pharmacy, and Workers' Comp opportunity "
                        "records. Assign each its own baseline, evidence period, billing "
                        "basis, and recovery deadline so projected employer savings cannot "
                        "be mistaken for operator revenue or counted across overlapping services."
                    ),
                    (
                        "Request binding stop-loss terms, underlying plan documents, PBM "
                        "definitions, and the applicable rating bureau worksheet. Treat "
                        "illustrative quotes and public filings as leads rather than "
                        "evidence that a carrier, administrator, or employer has accepted an obligation."
                    ),
                    (
                        "Normalize every comparison for enrollment, benefit design, claims "
                        "period, rebates, administrative charges, and coverage exclusions. "
                        "Identify excluded costs explicitly, particularly participant balance "
                        "bills, specialty pharmacy substitutions, claim run-out, and individual stop-loss lasers."
                    ),
                    (
                        "Approve pursuit only after documenting authority, measurable value, "
                        "collectible compensation, licensed delivery capacity, and a credible "
                        "fallback. Assign an owner and dated evidence request to each "
                        "unresolved dependency rather than concealing uncertainty inside a savings percentage."
                    ),
                ],
                "fields": [
                    field(
                        "Employer identity, plan scope, and authorized sponsor",
                        "textarea",
                        (
                            "Record the employer entity, controlled-group questions, plan "
                            "number, funding status, plan year, covered employees, covered "
                            "lives, and sponsor representative. Explain which signed "
                            "authorization permits each requested dataset and vendor conversation."
                        ),
                        (
                            "Harbor Components LLC sponsors calendar-year plan 501 with "
                            "350 covered employees and 612 covered lives. The CFO signs "
                            "a benefits review engagement and authorizes contract requests. "
                            "The 350 employees establish the proposed PEPM billing base; "
                            "612 lives inform claims analysis but do not multiply advisory fees."
                        ),
                    ),
                    field(
                        "Renewal intelligence and incumbent position",
                        "textarea",
                        (
                            "Identify the renewal date, public filing source, incumbent "
                            "broker relationship, cancellation notice requirements, and "
                            "procurement calendar. Distinguish historical Schedule A or C "
                            "information from current arrangements verified directly with the employer."
                        ),
                        (
                            "A DOL EFAST2 filing identifies a prior carrier relationship "
                            "and December plan-year end. The employer confirms a January "
                            "renewal and September market review. Its current agreement "
                            "requires 60 days' termination notice. Schedule C amounts "
                            "remain historical evidence, not proof of this year's broker compensation."
                        ),
                    ),
                    field(
                        "Health baseline and comparable exposure",
                        "textarea",
                        (
                            "Specify the paid and incurred claim periods, enrollment "
                            "denominator, benefit design, administrative fees, and "
                            "large-claim adjustments. Identify the reconciliations needed "
                            "before comparing an insured renewal against self-funded or captive alternatives."
                        ),
                        (
                            "The employer reports $3,600,000 annual health spend, including "
                            "medical and pharmacy costs, carrier charges, and administration. "
                            "The analyst obtains 24 months of monthly enrollment and "
                            "claims summaries. A proposed $180,000 reduction remains an "
                            "employer projection, with trend, benefit changes, and run-out shown separately."
                        ),
                    ),
                    field(
                        "Stop-loss counterparty and laser qualification",
                        "textarea",
                        (
                            "Capture carrier identity, specific and aggregate attachments, "
                            "contract basis, exclusions, disclosure duties, reimbursement "
                            "timing, and named claimant lasers. Compare the binding wording "
                            "with the plan's obligations rather than relying on a quote summary."
                        ),
                        (
                            "A proposal offers $100,000 specific coverage with one "
                            "$250,000 claimant laser and a 125% aggregate attachment. "
                            "The additional $150,000 laser exposure is modeled separately. "
                            "The sponsor requests a firm aggregate schedule, reimbursement "
                            "requirements, and contract wording before treating the quote as executable protection."
                        ),
                    ),
                    field(
                        "PBM spread and rebate opportunity",
                        "textarea",
                        (
                            "Define the claim sample, ingredient-cost benchmark, dispensing "
                            "fees, specialty exclusions, rebate ownership, and reconciliation "
                            "period. Explain how NADAC comparisons will distinguish a "
                            "screening signal from contractually recoverable dollars and achievable future savings."
                        ),
                        (
                            "A 10,000-claim generic sample totals $420,000 in ingredient "
                            "charges against $370,000 using date-matched NADAC observations. "
                            "Adding $15,000 modeled dispensing fees produces a $35,000 "
                            "screening difference. Specialty products, missing benchmark observations, "
                            "rebates, and member cost sharing require separate treatment before presenting savings."
                        ),
                    ),
                    field(
                        "Workers' Comp jurisdiction and E-Mod evidence",
                        "textarea",
                        (
                            "Identify each state's rating authority, policy period, "
                            "experience worksheet, payroll classifications, ownership "
                            "history, and loss valuation date. Record the specific "
                            "correction mechanism and filing deadline rather than assuming every state uses NCCI."
                        ),
                        (
                            "An Indiana employer supplies an NCCI worksheet showing "
                            "a 1.18 modification. A supported correction models 1.06 "
                            "on $240,000 of premium subject to modification, implying "
                            "$28,800 before other rating factors. The carrier must "
                            "issue an endorsed calculation before a refund amount becomes collectible."
                        ),
                    ),
                    field(
                        "Contractual compensation and retained spread",
                        "textarea",
                        (
                            "List advisory fees, direct and indirect commissions, recovery "
                            "splits, referral obligations, and payment triggers. Reconcile "
                            "each amount to retained operator consideration, excluding "
                            "employer claim accounts, insurance premiums, and recoveries owed to the employer."
                        ),
                        (
                            "The annual base portfolio contains $315,000 retained advisory "
                            "fees, $140,000 retained stop-loss and TPA commissions, and "
                            "$80,000 earned recovery fees. Advisory fees equal 350 "
                            "covered employees times $75 times 12 months. Employer "
                            "premiums and claim funding remain outside the $535,000 operator revenue total."
                        ),
                    ),
                    field(
                        "Vendor solvency, service, and dispute exposure",
                        "textarea",
                        (
                            "Assess each counterparty's operating authority, carrier "
                            "backing where relevant, service references, termination "
                            "rights, data access, auditability, and dispute process. "
                            "Record the evidence source and the commercial consequence of a failed obligation."
                        ),
                        (
                            "The stop-loss carrier's state authority is verified through "
                            "the insurance department. The TPA supplies two comparable "
                            "employer references, a specimen service agreement, and a "
                            "claims export specification. A proposed 90-day export delay "
                            "is rejected because it would obstruct transition reconciliation and independent claim review."
                        ),
                    ),
                    field(
                        "Employer savings bridge and downside case",
                        "textarea",
                        (
                            "Bridge baseline employer cost to proposed cost using "
                            "separately labeled benefit, utilization, price, fee, and "
                            "risk changes. Stress the principal adverse assumptions "
                            "without using operator margin as evidence of employer value."
                        ),
                        (
                            "A $180,000 gross employer improvement less $70,000 incremental "
                            "service costs and $40,000 transition costs yields $70,000 "
                            "modeled first-year benefit. A further $150,000 uncovered "
                            "laser exposure turns that case into an $80,000 adverse "
                            "outcome. The sponsor considers alternate coverage before accepting retained risk."
                        ),
                    ),
                    field(
                        "Pursuit decision and evidence conditions",
                        "textarea",
                        (
                            "Write the pursue, defer, or decline decision with "
                            "documented reasons, required evidence, accountable owners, "
                            "and dates. Separate a commercial pursuit decision from "
                            "authority to bind insurance, move funds, or transmit participant records."
                        ),
                        (
                            "Pursue the PBM review and defer the funding transition. "
                            "The analyst must reconcile rebates by day 8; the "
                            "licensed producer must obtain firm laser terms by day "
                            "12. No carrier binding, participant transfer, or employer "
                            "fund movement is authorized by this internal pursuit decision."
                        ),
                    ),
                ],
                "completion_gate": (
                    "The principal and licensed service lead sign a dated opportunity "
                    "record containing a reconciled baseline, retained-fee schedule, "
                    "counterparty evidence, jurisdiction map, and assigned resolution "
                    "dates for every material underwriting dependency."
                ),
            },
            {
                "worksheet_id": "ws-02",
                "number": 2,
                "title": "Unit Economics, Escrow/Reserve Float & Working-Capital Calculator",
                "purpose": (
                    "Reconcile the canonical portfolio scenarios to retained operator "
                    "revenue, annual expense, and owner net profit. Separate revenue "
                    "recognition from cash collection, distinguish operating reserves "
                    "from employer claim funds, and size working capital for commission "
                    "delays, refund disputes, and implementation spending."
                ),
                "chapter_ref": "Q3, Q4",
                "instructions": [
                    (
                        "Copy the three canonical scenarios without changing their "
                        "revenue, margin, profit, or team assumptions. Explain that "
                        "the scorecard's gross revenue label refers to retained "
                        "operator revenue here, not employer premiums, plan assets, or underlying medical spend."
                    ),
                    (
                        "Build each scenario from covered employee months, retained "
                        "advisory rates, retained commissions, and earned recovery "
                        "fees. Treat the component mixes as workbook assumptions "
                        "that reconcile to the fixed scenario totals, not additional facts supplied by the scorecard."
                    ),
                    (
                        "Apply principal-versus-agent analysis to every compensation "
                        "stream and document the accounting policy. For this "
                        "scorecard, use the retained contribution basis consistently; "
                        "do not deduct upstream sharing arrangements a second time after revenue has already been reduced."
                    ),
                    (
                        "Prepare a weekly cash forecast that separates issued invoices, "
                        "recognized consideration, unrestricted receipts, restricted amounts, "
                        "and expenses. Exclude employer claim funding from available "
                        "working capital even if a vendor dashboard displays those balances alongside operator commissions."
                    ),
                    (
                        "Stress collections and dispute exposure before committing "
                        "the startup budget. Show monthly recurring overhead "
                        "separately from total delivery costs, and make owner "
                        "draws subordinate to the chosen cash floor rather than to an uncollected revenue forecast."
                    ),
                ],
                "fields": [
                    field(
                        "Conservative retained-revenue scenario",
                        "textarea",
                        (
                            "Reproduce conservative revenue, margin, owner net profit, "
                            "expense, and staffing exactly. Construct an explicit "
                            "illustrative fee mix that adds to the canonical "
                            "revenue without including employer premiums or claim funds."
                        ),
                        (
                            "Conservative revenue is $120,000: 100 employees times $60 "
                            "PEPM times 12 equals $72,000, plus $30,000 retained "
                            "commissions and $18,000 earned recovery fees. Expenses "
                            "are $81,600, leaving $38,400 at 32% margin. Staffing "
                            "is 1 full-time principal plus 3 contractors, not four full-time equivalents."
                        ),
                    ),
                    field(
                        "Base-case retained-revenue scenario",
                        "textarea",
                        (
                            "Reproduce base revenue, margin, owner net profit, "
                            "expense, and staffing exactly. State whether enrolled "
                            "employees or covered lives drive the advisory "
                            "calculation, and identify the recognition condition for contingent fees."
                        ),
                        (
                            "Base revenue is $535,000: 350 employees times $75 "
                            "PEPM times 12 equals $315,000, plus $140,000 retained "
                            "commissions and $80,000 earned recovery fees. Expenses "
                            "are $294,250, leaving $240,750 at 45.0% margin. Staffing "
                            "is 1 full-time principal plus 3 contractors with defined delivery capacity."
                        ),
                    ),
                    field(
                        "Scaled small-team retained-revenue scenario",
                        "textarea",
                        (
                            "Reproduce scaled revenue, margin, owner net profit, "
                            "expense, and headcount exactly. Explain how increased "
                            "covered enrollment and retained ancillary compensation "
                            "produce the revenue total without counting premium volume as sales."
                        ),
                        (
                            "Scaled revenue is $950,000: 800 employees times $65 "
                            "PEPM times 12 equals $624,000, plus $226,000 retained "
                            "commissions and $100,000 earned recovery fees. Expenses "
                            "are $399,000, leaving $551,000 at 58% margin. Staffing "
                            "is 2 full-time personnel plus 4 contractors, totaling six people."
                        ),
                    ),
                    field(
                        "ASC 606 retained-share bridge",
                        "textarea",
                        (
                            "Document gross contractual consideration, pass-through shares, "
                            "retained_share, performance obligations, and collection "
                            "timing. Explain the actual principal-versus-agent conclusion "
                            "separately from the scorecard presentation, especially when statutory accounts require a different gross presentation."
                        ),
                        (
                            "A commission stream has $200,000 gross contractual consideration "
                            "and a $60,000 upstream share. With retained_share equal "
                            "to 0.70, the scorecard includes $140,000. A documented "
                            "ASC 606 assessment supports net presentation for this "
                            "example; delayed receipt of $20,000 changes cash timing, not the retained-share multiplication."
                        ),
                    ),
                    field(
                        "Annual cost bridge and monthly overhead",
                        "textarea",
                        (
                            "Reconcile annual scenario expense to recurring overhead "
                            "and other delivery costs. Keep the stated monthly "
                            "opex range visible without falsely equating that "
                            "range to all annual costs required to earn the scenario revenue."
                        ),
                        (
                            "The base expense bridge allocates $72,000 to recurring "
                            "overhead, or $6,000 monthly within the $2,000–$11,000 "
                            "range. Other delivery, acquisition, and project costs "
                            "total $222,250. Combined expense is $294,250. The "
                            "$6,000 overhead line is a subset, not the full monthly economic cost."
                        ),
                    ),
                    field(
                        "Startup capital and delayed-collection stress",
                        "textarea",
                        (
                            "Specify one-time setup spending, unrestricted opening "
                            "cash, monthly burn, expected first collection, and "
                            "stress duration. Compare required funding with the "
                            "$8,000–$45,000 startup range and the 2–5 month first-deal expectation."
                        ),
                        (
                            "At the high end, $8,000 setup plus three months "
                            "of $11,000 burn plus a $4,000 incident cushion "
                            "requires $45,000. Five months at that burn would "
                            "require $67,000. The operator therefore reduces burn, "
                            "secures permissible deposits, or adds capital rather than assuming the startup range covers every delay."
                        ),
                    ),
                    field(
                        "Employer funds, escrow, and operating reserve separation",
                        "textarea",
                        (
                            "Identify every account, beneficial owner, permitted "
                            "use, transfer authority, and reconciliation owner. "
                            "Distinguish employer claim reserves, insurer premium "
                            "payments, and disputed recoveries from unrestricted operator cash available for payroll or acquisitions."
                        ),
                        (
                            "The employer maintains a $300,000 claim account under "
                            "its own authorized funding arrangement. The operator "
                            "holds $28,000 unrestricted business cash and has no "
                            "claim-account withdrawal rights. A $12,000 disputed "
                            "recovery stays with its contractual holder; neither external balance extends the operator's measured runway."
                        ),
                    ),
                    field(
                        "Recovery fee recognition and reversal exposure",
                        "textarea",
                        (
                            "Record the recovery amount, split, evidence of "
                            "carrier acceptance, employer receipt, invoice trigger, "
                            "and reversal terms. Apply variable-consideration "
                            "constraints before recognizing a disputed fee, and distinguish a billing milestone from a recognition conclusion."
                        ),
                        (
                            "The carrier confirms a $100,000 premium correction and "
                            "the employer receives the refund. A 20% engagement "
                            "fee produces $20,000, subject to the documented "
                            "recognition assessment. A separate proposed $60,000 "
                            "correction remains disputed; its potential $12,000 fee stays outside recognized revenue and unrestricted cash."
                        ),
                    ),
                    field(
                        "Receivable aging and portfolio cash floor",
                        "textarea",
                        (
                            "List receivables by counterparty, contractual due date, "
                            "dispute status, and expected collection week. "
                            "Calculate unrestricted runway from cash and "
                            "committed burn, excluding unsigned renewals, unearned contingencies, and employer-controlled balances from the calculation."
                        ),
                        (
                            "Unrestricted cash is $28,000 and committed monthly "
                            "overhead is $6,000, giving 4.67 months before "
                            "other outlays. Receivables include $18,000 due in "
                            "15 days and $12,000 disputed. A $12,000 cash "
                            "floor leaves $16,000 deployable; neither receivable is treated as already collected."
                        ),
                    ),
                    field(
                        "Break-even and owner distribution policy",
                        "textarea",
                        (
                            "State the contribution assumptions used for marginal "
                            "break-even, then reconcile them with the full "
                            "portfolio result. Define who authorizes distributions "
                            "and which cash, tax, dispute, and delivery obligations must be funded first."
                        ),
                        (
                            "At an illustrative 70% marginal contribution rate, "
                            "$6,000 monthly fixed overhead requires $8,571.43 "
                            "monthly retained revenue. This planning ratio does "
                            "not replace the base annual 45% margin. The "
                            "principal reviews distributions monthly only after the $12,000 cash floor, committed invoices, and tax reserve remain funded."
                        ),
                    ),
                ],
                "completion_gate": (
                    "All three revenue-minus-expense calculations equal the canonical "
                    "owner profit figures; retained-share calculations contain no "
                    "double deduction; and the weekly cash forecast excludes every "
                    "employer-controlled balance while funding the selected downside duration."
                ),
            },
            {
                "worksheet_id": "ws-03",
                "number": 3,
                "title": "End-to-End Execution, Idempotent Ledger & QA Pre-Flight Sheet",
                "purpose": (
                    "Turn signed authority into a reproducible delivery sequence "
                    "without duplicate invoices, unsupported savings, or participant "
                    "data leakage. Define source records, stable identifiers, "
                    "reconciliation checkpoints, release evidence, and correction "
                    "procedures across health transitions, PBM repricing, and Workers' Comp recoveries."
                ),
                "chapter_ref": "Q7, Q8",
                "instructions": [
                    (
                        "Map each engagement from signed scope through intake, "
                        "analysis, proposal, accepted terms, implementation, billing, "
                        "and collection. Attach an owner and evidence artifact "
                        "to each transition so a completed task means an observable outcome rather than a checked box."
                    ),
                    (
                        "Create stable engagement, source-file, claim, adjustment, and "
                        "invoice identifiers before importing records. Use explicit "
                        "versioning for corrected records and database uniqueness "
                        "constraints for economic events so retrying a job cannot create another fee or recovery entry."
                    ),
                    (
                        "Reconcile source counts and money totals before applying "
                        "pricing logic. Keep paid claims, reversals, adjustments, "
                        "rebates, and fees in distinct record types; "
                        "a negative transaction is not automatically an error, and an apparent duplicate may be a legitimate correction."
                    ),
                    (
                        "Require independent review of coverage wording, repricing "
                        "assumptions, rating corrections, and billing calculations. "
                        "The reviewer must reproduce material totals from "
                        "source evidence rather than merely confirming that the analyst's final spreadsheet looks internally consistent."
                    ),
                    (
                        "Release only the contracted deliverable to authorized "
                        "recipients and preserve a compact evidence package. "
                        "Record actual vendor acceptance, employer acknowledgment, "
                        "and cash receipt separately; internal completion does not establish that an external counterparty performed its obligation."
                    ),
                ],
                "fields": [
                    field(
                        "Engagement state machine and handoff owners",
                        "textarea",
                        (
                            "Define allowed engagement states, transition evidence, "
                            "responsible roles, and blocked-state behavior. "
                            "Specify which actions require sponsor authority "
                            "or a licensed producer, and prevent an analyst status change from creating external authority."
                        ),
                        (
                            "ENG-040-017 advances from signed to intake-complete after "
                            "contract and enrollment checks, then to analyzed after "
                            "independent reconciliation. Only the licensed producer "
                            "records carrier binding evidence. The billing specialist "
                            "opens invoicing after the contractual milestone; an analyst cannot bind coverage by marking analysis complete."
                        ),
                    ),
                    field(
                        "Source manifest and protected intake",
                        "textarea",
                        (
                            "List each source file's sender, authorization, receipt "
                            "time, cryptographic digest, record count, monetary "
                            "control total, and retention class. Define "
                            "how malformed files and excess participant identifiers are isolated before analysts receive access."
                        ),
                        (
                            "A monthly pharmacy extract arrives through an encrypted "
                            "portal with 10,080 transactions and a $424,200 "
                            "net control total. The intake service records "
                            "a SHA-256 digest and restricts the original "
                            "to the review team. Names and addresses are removed from the pricing copy when unnecessary."
                        ),
                    ),
                    field(
                        "Idempotency keys and duplicate-event handling",
                        "textarea",
                        (
                            "Specify a stable economic-event key, storage "
                            "uniqueness rule, retry behavior, and corrected-record "
                            "policy. Explain why file names and "
                            "arrival timestamps alone cannot identify an obligation or prevent duplicate posting across repeated vendor exports."
                        ),
                        (
                            "A PBM event key combines engagement, vendor transaction "
                            "identifier, transaction type, and version. SQLite enforces "
                            "a UNIQUE constraint on those columns. Reimporting "
                            "the same version changes no ledger balances. "
                            "A corrected version supersedes the earlier analysis and creates a linked adjustment rather than silently overwriting history."
                        ),
                    ),
                    field(
                        "PBM claim, reversal, and rebate reconciliation",
                        "textarea",
                        (
                            "Describe transaction classification, original-to-reversal matching, "
                            "benchmark dates, quantity normalization, and rebate "
                            "allocation. State which exceptions block a "
                            "savings calculation and how the reviewer reconciles transaction totals to vendor settlement reports."
                        ),
                        (
                            "The extract contains 10,000 paid transactions totaling "
                            "$430,000 and 80 reversals totaling negative $5,800, "
                            "for $424,200 net. Each reversal links to "
                            "its original transaction. Rebate receivables remain "
                            "separate until the contract period is reconciled, preventing a credit from being counted as both lower claim cost and rebate income."
                        ),
                    ),
                    field(
                        "Stop-loss implementation and coverage continuity",
                        "textarea",
                        (
                            "Record the binding evidence, plan-document alignment, "
                            "eligibility transmission, contract basis, terminal "
                            "liability arrangements, and reimbursement workflow. "
                            "Identify who verifies that old-period claims and new-period claims have a defined funding and coverage path."
                        ),
                        (
                            "The implementation checklist records the signed binder, "
                            "accepted eligibility roster, $100,000 specific attachment, "
                            "and $250,000 laser. A 12/15 proposal is "
                            "checked against actual contract definitions. Prior "
                            "incurred claims receive a separate run-out schedule; the team does not assume the new contract automatically covers them."
                        ),
                    ),
                    field(
                        "Workers' Comp correction evidence chain",
                        "textarea",
                        (
                            "Identify the disputed classification, payroll or "
                            "loss record, source authority, requested correction, "
                            "bureau response, and carrier endorsement. "
                            "Require dated evidence linking the underlying error to a revised modification and actual premium consequence."
                        ),
                        (
                            "The employer supplies payroll records supporting a "
                            "classification correction and a carrier loss-run "
                            "letter confirming one closed claim's revised "
                            "value. The analyst logs submission and "
                            "bureau response dates. The file reaches collectible status only after the carrier issues the endorsed premium calculation and contractual recovery conditions are satisfied."
                        ),
                    ),
                    field(
                        "Retained-fee ledger and settlement entries",
                        "textarea",
                        (
                            "Define ledger accounts for receivables, cash, "
                            "retained revenue, external shares, and "
                            "adjustments. Specify how accounting presentation "
                            "is reconciled to the scorecard, and require settlement references connecting each receipt to an existing obligation."
                        ),
                        (
                            "A $20,000 earned recovery fee creates one "
                            "receivable and one revenue event under the "
                            "adopted policy. A later $15,000 receipt "
                            "reduces that receivable to $5,000; it "
                            "does not create another $15,000 of revenue. Bank reference and invoice identifier remain linked in the settlement record."
                        ),
                    ),
                    field(
                        "Independent QA and release tolerances",
                        "textarea",
                        (
                            "Set reproducible checks for record counts, "
                            "currency precision, enrollment months, contract "
                            "terms, and recipient authorization. Distinguish "
                            "permitted rounding from unexplained differences, and document the reviewer who can withhold an unsupported deliverable."
                        ),
                        (
                            "The reviewer reproduces 350 times $75 as "
                            "$26,250 monthly advisory fees and confirms "
                            "the current enrollment definition. Source-to-ledger "
                            "totals must reconcile to the cent "
                            "after documented rounding rules. An unexplained $240 difference blocks release until the missing adjustment is identified and recorded."
                        ),
                    ),
                    field(
                        "Corrections, rollback, and customer notification",
                        "textarea",
                        (
                            "Describe how an incorrect analysis, invoice, "
                            "or exported file is withdrawn and "
                            "replaced without erasing history. Identify "
                            "notification responsibility, external acceptance checks, and the conditions requiring participant incident assessment or contractual escalation."
                        ),
                        (
                            "A mistaken invoice bills 360 rather than "
                            "350 employees at $75 PEPM. The "
                            "billing specialist issues a linked $750 "
                            "credit and sends the corrected statement "
                            "to the employer's authorized contact. The original remains auditable, and the delivery log records acknowledgment rather than assuming an email was read."
                        ),
                    ),
                    field(
                        "Evidence package and closeout reconciliation",
                        "textarea",
                        (
                            "List the minimum closeout artifacts, access "
                            "roles, retention basis, and unresolved "
                            "balances. Separate durable decision evidence "
                            "from unnecessary participant-level copies, and state which open items prevent engagement closure despite a delivered presentation."
                        ),
                        (
                            "Closeout contains the engagement, compensation disclosure, "
                            "source manifest, reproducible calculation, reviewer "
                            "sign-off, carrier endorsement, invoice, and "
                            "receipt reference. The remaining $5,000 "
                            "receivable keeps collection open while delivery is complete. Participant-level working files follow the documented retention schedule instead of being copied into every project folder."
                        ),
                    ),
                ],
                "completion_gate": (
                    "A second operator reproduces the material totals, a repeated "
                    "import creates zero additional economic events, every outward "
                    "action has recorded authority, and the evidence package "
                    "reconciles delivery status, invoices, adjustments, and collected cash."
                ),
            },
            {
                "worksheet_id": "ws-04",
                "number": 4,
                "title": "Statutory, Licensing, Contract Addendum & Compliance Audit",
                "purpose": (
                    "Convert statutory duties and contract dependencies into "
                    "testable operating requirements. Map producer and administrator "
                    "authority by state, disclose compensation before covered "
                    "engagements, protect health information, and preserve enforceable "
                    "rights around stop-loss coverage, PBM accounting, rating corrections, and reference-based pricing."
                ),
                "chapter_ref": "Q5, Q9",
                "instructions": [
                    (
                        "Create a jurisdiction map based on employer locations, "
                        "insured risks, solicitation activity, and performed "
                        "services. Verify individual and business-entity "
                        "authority with the relevant insurance department before treating a contractor's license as authority for the whole practice."
                    ),
                    (
                        "Identify the actual service role before applying "
                        "ERISA, HIPAA, or state administrator requirements. "
                        "A brokerage engagement does not automatically "
                        "make every activity fiduciary, and a consulting title does not remove licensing requirements when the underlying activity is regulated."
                    ),
                    (
                        "Attach direct and indirect compensation schedules to "
                        "covered engagements before execution, renewal, or "
                        "extension within the statutory timing framework. "
                        "Describe payment sources, formulas, offsets, and termination compensation clearly enough for the responsible plan fiduciary to evaluate reasonableness."
                    ),
                    (
                        "Review contract provisions against the actual operating "
                        "workflow, including data access, audit rights, "
                        "reimbursement duties, dispute escalation, and "
                        "termination assistance. Reject wording that promises transparency while withholding the transaction-level evidence needed to verify the promise."
                    ),
                    (
                        "Record the exact rule source, effective date, "
                        "reviewer, and corrective action for each "
                        "finding. Use current state and "
                        "rating-bureau requirements for recovery work; neither an ERISA label nor a national vendor contract substitutes for jurisdiction-specific analysis."
                    ),
                ],
                "fields": [
                    field(
                        "Producer license and appointment matrix",
                        "textarea",
                        (
                            "Record individual and agency licenses, relevant "
                            "Life and Health and Property and "
                            "Casualty authority, carrier appointments where "
                            "required, renewal dates, and responsible personnel for every state implicated by the proposed services."
                        ),
                        (
                            "The practice verifies Texas Life and Health "
                            "authority under Texas Insurance Code Chapter "
                            "4054 and Property and Casualty authority "
                            "under Chapter 4051, plus business-entity "
                            "and applicable appointment requirements. A spreadsheet links each verification to the named producer and permitted activity; an inactive credential blocks that activity."
                        ),
                    ),
                    field(
                        "TPA scope and stop-loss placement authority",
                        "textarea",
                        (
                            "Describe whether the operator administers claims, "
                            "collects premiums, handles plan assets, "
                            "or only advises and places "
                            "coverage. Test administrator licensing and exemptions separately from producer authority using the actual service scope and jurisdiction."
                        ),
                        (
                            "The Texas engagement excludes claims adjudication, "
                            "premium collection, and discretionary claim "
                            "payments. The service lead reviews "
                            "Texas Insurance Code Chapter 4151 "
                            "for administrator requirements and exemptions before adding services. Stop-loss placement also receives a line-of-authority and product review rather than assuming a health license resolves every issue."
                        ),
                    ),
                    field(
                        "ERISA compensation disclosure evidence",
                        "textarea",
                        (
                            "Identify covered brokerage or consulting services, "
                            "expected compensation, direct and indirect "
                            "payment sources, recipient, and delivery "
                            "date. Apply ERISA Section 408(b)(2)(B) to covered group health arrangements rather than automatically extending it to every Workers' Comp engagement."
                        ),
                        (
                            "For a covered group health engagement expecting "
                            "at least $1,000 compensation, the practice "
                            "provides disclosures reasonably in advance "
                            "under 29 U.S.C. 1108(b)(2)(B). The "
                            "schedule identifies $75 PEPM advisory fees, carrier-paid commissions, referral payments, formulas, and termination amounts, with dated evidence of delivery to the responsible plan fiduciary."
                        ),
                    ),
                    field(
                        "Plan fiduciary role and employer decision record",
                        "textarea",
                        (
                            "Identify who exercises discretion over plan "
                            "administration, assets, and vendor selection. "
                            "Document service limitations and sponsor "
                            "decisions against ERISA's functional fiduciary framework, without assuming that a contract label overrides the activities actually performed."
                        ),
                        (
                            "Under 29 U.S.C. 1002(21)(A), functional discretion "
                            "can establish fiduciary status. The "
                            "employer's committee documents vendor selection "
                            "under 29 U.S.C. 1104(a), comparing "
                            "coverage, compensation, and service quality. The operator provides analysis but receives no discretionary claim-payment authority; any later expansion triggers a fresh role assessment."
                        ),
                    ),
                    field(
                        "HIPAA role, minimum necessary access, and incidents",
                        "textarea",
                        (
                            "Map covered-entity and business-associate relationships, "
                            "permitted uses, subcontractors, security "
                            "responsibilities, and incident reporting. "
                            "Specify when a business associate agreement is required and how analytical access is limited to the information needed for the task."
                        ),
                        (
                            "When acting as a business associate, the "
                            "practice executes terms addressing 45 CFR "
                            "164.504(e), applies relevant minimum-necessary "
                            "requirements under 45 CFR 164.502(b), "
                            "and uses safeguards under 45 CFR 164.308 and 164.312. Suspected exposure enters the documented assessment process, including applicable notification duties under 45 CFR 164.410."
                        ),
                    ),
                    field(
                        "Stop-loss, run-out, and captive addendum",
                        "textarea",
                        (
                            "Specify attachment definitions, claimant lasers, "
                            "eligibility, exclusions, reimbursement documents, "
                            "advance funding, termination liability, "
                            "and captive assessments where relevant. State which party funds a claim before reimbursement and how contract conflicts are resolved."
                        ),
                        (
                            "The addendum schedules $100,000 specific attachment, "
                            "the identified $250,000 laser, and "
                            "the signed aggregate calculation. It "
                            "assigns employer funding responsibility until "
                            "reimbursement and lists claim submission deadlines. A captive proposal separately discloses collateral, additional assessments, and exit obligations rather than treating membership contributions as ordinary operator revenue."
                        ),
                    ),
                    field(
                        "PBM rebate ownership and gag-clause review",
                        "textarea",
                        (
                            "Define rebates, administrative fees, affiliate "
                            "remuneration, audit rights, data "
                            "access, and settlement timing. "
                            "Evaluate contractual restrictions under applicable gag-clause provisions and distinguish an operator's assistance from the plan or issuer's attestation responsibility."
                        ),
                        (
                            "The PBM addendum assigns defined manufacturer "
                            "remuneration to the plan, itemizes "
                            "retained fees, and permits authorized "
                            "audit access. Review addresses 29 "
                            "U.S.C. 1185m, 42 U.S.C. 300gg-119, and 26 U.S.C. 9824. The plan tracks its annual attestation responsibility and documents vendor support without assuming a signature resolves every restriction."
                        ),
                    ),
                    field(
                        "Workers' Comp correction authority and fee terms",
                        "textarea",
                        (
                            "Identify the state's rating rules, correction "
                            "window, licensed activities, employer "
                            "authorization, and permitted contingent "
                            "compensation. Check separate adjuster or consultant requirements where implicated, and distinguish employer premium recovery from representation on an employee's injury claim."
                        ),
                        (
                            "For California exposure, the operator uses "
                            "WCIRB materials rather than NCCI "
                            "rules and reviews California Insurance "
                            "Code Sections 11750 and following "
                            "with the applicable rating plan. The engagement limits work to authorized employer premium analysis and a permitted 20% received-refund fee; it excludes handling an employee's benefit claim."
                        ),
                    ),
                    field(
                        "Reference-based pricing and participant defense",
                        "textarea",
                        (
                            "Describe reference-based pricing methodology, provider "
                            "acceptance, participant communications, balance-bill "
                            "support, appeal rights, and "
                            "funded defense arrangements. Separate plan payment methodology from statutory surprise-billing protections and identify cases where protection does not apply."
                        ),
                        (
                            "A proposed reference-based pricing arrangement includes "
                            "a written balance-bill assistance protocol "
                            "and funded access to qualified "
                            "counsel. Review distinguishes applicable protections "
                            "under 42 U.S.C. 300gg-111 and 300gg-131 from unrelated bills. A Medicare multiple alone does not establish provider acceptance or eliminate participant disputes."
                        ),
                    ),
                    field(
                        "Audit findings, contract precedence, and corrective action",
                        "textarea",
                        (
                            "Record each finding's rule source, affected "
                            "contract, severity, owner, remedy, "
                            "and verification evidence. Identify "
                            "which document controls when the sales proposal, service agreement, plan document, and insurance contract describe different obligations."
                        ),
                        (
                            "Finding C-07 identifies a proposal promising "
                            "full rebate pass-through while the "
                            "PBM agreement excludes affiliate receipts. "
                            "The contract lead requests a "
                            "defined remuneration amendment and independent review. The employer receives the unresolved difference in writing, and no savings calculation assumes the amendment is effective before execution."
                        ),
                    ),
                ],
                "completion_gate": (
                    "The service lead verifies current activity-specific authority, "
                    "required compensation disclosures, executed data-use terms, "
                    "and material coverage addenda. Every remaining finding has "
                    "a documented operating restriction, named owner, and dated resolution requirement."
                ),
            },
            {
                "worksheet_id": "ws-05",
                "number": 5,
                "title": "Automation Pipeline, Acquisition Flywheel & Risk Fallback Tracker",
                "purpose": (
                    "Build a small-team acquisition and delivery system that "
                    "automates repeatable evidence handling without automating "
                    "unsupported decisions. Track source provenance, renewal timing, "
                    "repricing quality, bureau-specific logic, and human review "
                    "capacity while preserving a manual fallback for every critical dependency."
                ),
                "chapter_ref": "Q6, Q10",
                "instructions": [
                    (
                        "Use public employer filings to prioritize outreach, "
                        "not to infer current benefit terms "
                        "or acquire participant records. Respect "
                        "source access conditions, cache retrieved material, and preserve filing dates so prospect scores do not silently rely on stale arrangements."
                    ),
                    (
                        "Version the NADAC reference series, PBM "
                        "contract rules, and rating-bureau inputs "
                        "used by each calculation. A "
                        "reproducible result must identify its source period and exclusions, including products without a valid benchmark and states outside the selected bureau."
                    ),
                    (
                        "Measure automation by reconciled work completed "
                        "per reviewer hour rather than "
                        "by files downloaded. Separate "
                        "technical processing success from commercial validity; a perfectly parsed contract can still contain an unacceptable exclusion or an unenforceable savings assumption."
                    ),
                    (
                        "Keep outreach, analytics, and billing stores "
                        "separated by purpose and access "
                        "role. Public prospect records "
                        "belong in the CRM, while participant-level claims require restricted handling; copying medical details into a sales note creates unnecessary exposure without improving qualification."
                    ),
                    (
                        "For each automated stage, define a "
                        "failure signal, stop condition, "
                        "manual procedure, owner, and "
                        "recovery target. Reconcile the backlog before restarting a failed job so resumed processing does not duplicate outreach, imports, correction submissions, or invoices."
                    ),
                ],
                "fields": [
                    field(
                        "Form 5500 prospect acquisition manifest",
                        "textarea",
                        (
                            "Specify public sources, permitted retrieval "
                            "method, filing identifiers, employer "
                            "matching logic, and refresh "
                            "cadence. Document absent schedules as evidence limitations without inventing insurance arrangements or treating every plan as subject to identical filing requirements."
                        ),
                        (
                            "The weekly job reads public DOL "
                            "Form 5500 datasets and records "
                            "employer EIN, plan number, filing "
                            "year, and source reference. It "
                            "links Schedule A and C only when present and applicable. A missing schedule prompts employer verification, not an invented carrier, commission figure, or funding classification."
                        ),
                    ),
                    field(
                        "Renewal scoring and outreach eligibility",
                        "textarea",
                        (
                            "Define the scoring features, evidence "
                            "age limits, contact verification, "
                            "suppression logic, and reviewer "
                            "role. Ensure scoring supports relevant outreach without implying that public benefit filings establish interest, authority, or permission to access private plan information."
                        ),
                        (
                            "A prospect earns 30 points for "
                            "a verified renewal within 180 "
                            "days, 25 for suitable employee "
                            "count, and 20 for a "
                            "documented service mismatch. The operator suppresses opted-out contacts and checks business-email requirements under 15 U.S.C. 7704. A high score creates a review task, not automatic enrollment."
                        ),
                    ),
                    field(
                        "NADAC reference ingestion and normalization",
                        "textarea",
                        (
                            "Record the CMS reference release, "
                            "effective dates, NDC normalization, "
                            "unit definitions, and unmatched "
                            "product treatment. Prevent the engine from presenting a retail acquisition benchmark as a universal PBM contract price or a complete specialty-drug benchmark."
                        ),
                        (
                            "The repricing job preserves each CMS "
                            "NADAC release and matches claim "
                            "service dates to effective observations. "
                            "It checks NDC format and "
                            "quantity units before multiplication. Of 10,000 generic claims, 430 lack defensible matches and enter an exception queue rather than receiving zero benchmark cost or an estimated savings credit."
                        ),
                    ),
                    field(
                        "PBM pricing engine and reproducibility tests",
                        "textarea",
                        (
                            "Define contract-specific ingredient, dispensing, "
                            "rebate, and specialty logic "
                            "with test fixtures. State "
                            "how the engine proves arithmetic accuracy while keeping benchmark comparisons separate from contractual recoveries and enrollment-adjusted forward savings projections."
                        ),
                        (
                            "Python decimal arithmetic prices a fixture "
                            "of 30 units at $1.20 "
                            "plus a $1.50 dispensing fee "
                            "as $37.50. The test suite "
                            "checks reversals, unit changes, and effective-date boundaries. A benchmark difference is labeled analytical opportunity until the contract and claim evidence establish an enforceable recovery."
                        ),
                    ),
                    field(
                        "E-Mod analyzer and jurisdiction-specific rules",
                        "textarea",
                        (
                            "Identify the bureau, experience period, "
                            "valuation dates, payroll classes, "
                            "loss inputs, and authorized "
                            "reference materials. Define which computations the tool can reproduce and which require bureau confirmation or carrier endorsement before presenting a refund."
                        ),
                        (
                            "The analyzer stores the employer's actual "
                            "NCCI worksheet and licensed reference "
                            "inputs for the applicable period. "
                            "It flags a mismatch between "
                            "submitted and supported payroll rather than inventing rating factors. California files route to a WCIRB workflow; no universal NCCI formula is applied across every jurisdiction."
                        ),
                    ),
                    field(
                        "CRM boundaries and role-based permissions",
                        "textarea",
                        (
                            "Specify which attributes enter the "
                            "CRM, which remain in "
                            "restricted analysis storage, and "
                            "which roles can export information. Define account removal, multifactor authentication, access review, and logging responsibilities for employees and contractors."
                        ),
                        (
                            "The CRM stores company contacts, renewal "
                            "dates, employee-count bands, and opportunity "
                            "stage. Participant names, diagnoses, and "
                            "claim identifiers remain in restricted "
                            "storage. The principal reviews access monthly, requires multifactor authentication, and removes a departing analyst's account immediately while retaining an auditable record of the authorized work."
                        ),
                    ),
                    field(
                        "Acquisition flywheel and conversion economics",
                        "textarea",
                        (
                            "Measure prospect-to-meeting, meeting-to-review, and "
                            "review-to-engagement conversion with "
                            "dated cohorts. Calculate acquisition "
                            "cost from actual spend and signed engagements, keeping pipeline estimates separate from earned revenue and recognizing the 2–5 month first-deal cycle."
                        ),
                        (
                            "A cohort of 120 verified employers "
                            "produces 24 meetings, 8 authorized "
                            "reviews, and 2 signed engagements "
                            "over three months. With $6,000 "
                            "attributable acquisition spending, cost is $3,000 per signed engagement. The cohort supports pipeline planning; it does not create recognized fees before contractual service and recognition conditions are met."
                        ),
                    ),
                    field(
                        "Automation observability and exception budget",
                        "textarea",
                        (
                            "Define success metrics for accepted "
                            "records, reconciled totals, exception "
                            "age, reviewer hours, and "
                            "unauthorized-access alerts. Set thresholds that stop unreliable output rather than rewarding high throughput when source quality or contract interpretation has deteriorated."
                        ),
                        (
                            "A batch passes only when source "
                            "counts and settlement totals reconcile. "
                            "Unmatched benchmark claims above 5% "
                            "trigger analyst review; any unexplained "
                            "money difference blocks release. A dashboard tracks exceptions older than two business days and reviewer hours per completed employer analysis, not merely the number of imported files."
                        ),
                    ),
                    field(
                        "Vendor outage and manual fallback tracker",
                        "textarea",
                        (
                            "List critical dependencies, outage indicators, "
                            "manual substitutes, recovery targets, "
                            "and data reconciliation steps. "
                            "Distinguish a temporary processing pause from loss of coverage or a statutory deadline, and assign escalation to the role able to resolve each consequence."
                        ),
                        (
                            "If the PBM portal fails, intake "
                            "pauses and the analyst requests "
                            "an authorized encrypted export through "
                            "the named vendor contact. The "
                            "service target is one business day for status confirmation. After recovery, source digests and transaction identifiers are checked before import so the alternate delivery cannot duplicate economic events."
                        ),
                    ),
                    field(
                        "Incumbent defense and concentration fallback",
                        "textarea",
                        (
                            "Identify renewal obstruction, missing broker "
                            "authority, carrier concentration, and "
                            "key-person dependencies. Define "
                            "commercial fallback services that remain authorized and valuable without claiming leverage over a carrier, employer, or incumbent relationship the operator does not control."
                        ),
                        (
                            "When the incumbent retains placement, the "
                            "operator offers a separately authorized "
                            "PBM contract review instead of "
                            "promising a carrier change. No "
                            "single commission payer should dominate the planning case without a documented stress test. A second licensed producer maintains continuity if the principal becomes unavailable during the renewal window."
                        ),
                    ),
                ],
                "completion_gate": (
                    "Each production automation has versioned inputs, a reproducible "
                    "test, reconciliation thresholds, an assigned reviewer, and a "
                    "manual fallback. Outreach metrics use dated cohorts, and no "
                    "pipeline value, benchmark difference, or unendorsed correction is posted as earned revenue."
                ),
            },
            {
                "worksheet_id": "ws-06",
                "number": 6,
                "title": "30-Day Launch Sprint, Pod KPI Scorecard & Exit-Readiness Ledger",
                "purpose": (
                    "Translate the operating model into a realistic first "
                    "month and a measurable small-team practice. Assign "
                    "licensed responsibilities, set collection-aware performance targets, "
                    "and preserve transferable evidence of recurring revenue, "
                    "client rights, vendor dependencies, and delivery quality without assuming immediate deal closure."
                ),
                "chapter_ref": "Q11, Q12",
                "instructions": [
                    (
                        "Treat the first 30 days as "
                        "a setup and evidence-building sprint, "
                        "not a promise of closing "
                        "inside one month. Preserve the canonical 2–5 month first-deal expectation while setting immediate milestones for authority, contracts, intake, outreach, and analytical readiness."
                    ),
                    (
                        "Assign named responsibilities across the principal "
                        "and contractors, including license-dependent actions, "
                        "source reconciliation, accounting, and "
                        "contract review. Contractor count measures people, not full-time equivalents; document available hours and backup coverage before assuming the pod can absorb a new employer."
                    ),
                    (
                        "Use a scorecard that pairs activity "
                        "with evidence quality and collection "
                        "outcomes. Meetings, analyses, and "
                        "proposals are leading indicators; earned retained revenue, unrestricted receipts, corrections, and unresolved obligations determine whether the practice is actually producing durable owner profit."
                    ),
                    (
                        "Build exit readiness from the first "
                        "engagement through assignable contracts, "
                        "documented producer relationships, source "
                        "provenance, and clean revenue classification. Do not copy participant records into a broad buyer folder or assume a purchaser automatically inherits licenses and carrier appointments."
                    ),
                    (
                        "At day 30, reconcile completed tasks "
                        "against artifacts and remaining "
                        "dependencies. Continue only the "
                        "services supported by current authority, cash, and delivery capacity; revise the next sprint explicitly rather than silently changing the canonical scenario targets or hiding incomplete work."
                    ),
                ],
                "fields": [
                    field(
                        "Days 1–7 authority, scope, and capital",
                        "textarea",
                        (
                            "List the first week's deliverables "
                            "for licenses, business scope, "
                            "insurance, contracts, bank separation, "
                            "and startup funding. Assign an owner and objective acceptance evidence to each task, including items that cannot be completed within the week."
                        ),
                        (
                            "By day 7, the principal verifies "
                            "existing licenses, documents pending state "
                            "extensions, approves the engagement template, "
                            "and sets a $28,000 opening "
                            "cash balance. The team spends no more than $4,000 of the setup budget. Work requiring pending authority remains outside the active service scope until verification is complete."
                        ),
                    ),
                    field(
                        "Days 8–14 intake and analytical rehearsal",
                        "textarea",
                        (
                            "Define the second week's intake, "
                            "ledger, repricing, and recovery "
                            "workflow tests. Specify synthetic "
                            "or properly authorized source material, reviewer responsibility, pass criteria, and the remediation path for failed arithmetic, access, or duplicate-event checks."
                        ),
                        (
                            "By day 14, the analyst processes "
                            "a synthetic 200-transaction pharmacy fixture, "
                            "reconciles its control total, and "
                            "reimports it without additional ledger "
                            "events. A reviewer verifies the $37.50 pricing fixture and one linked reversal. No real participant file is used merely to demonstrate the intake software."
                        ),
                    ),
                    field(
                        "Days 15–21 targeted acquisition sprint",
                        "textarea",
                        (
                            "Set a bounded prospect cohort, "
                            "contact verification process, outreach "
                            "budget, meeting target, and "
                            "documented qualification standard. Separate permission to discuss an employer's needs from authority to collect claims, obtain carrier quotes, or represent the employer."
                        ),
                        (
                            "The principal selects 40 verified employers "
                            "with renewals within 180 days "
                            "and budgets $1,000 for outreach "
                            "and meeting preparation. The target "
                            "is eight conversations and three scoped review opportunities. A signed engagement and appropriate authorization precede nonpublic contract requests; meeting acceptance alone provides neither."
                        ),
                    ),
                    field(
                        "Days 22–30 proposal readiness and cash review",
                        "textarea",
                        (
                            "Specify the final week's deliverables "
                            "for proposal quality, compensation "
                            "disclosure, counterparty readiness, and "
                            "cash runway. State what counts as completed preparation when no employer has yet signed, consistent with the expected first-deal timing."
                        ),
                        (
                            "By day 30, the pod completes "
                            "two evidence-backed proposal drafts, a "
                            "reviewed compensation schedule, and a "
                            "13-week cash forecast. If no "
                            "engagement is signed, revenue remains zero. The principal reports proposal readiness and remaining dependencies accurately while maintaining the 2–5 month expected time to first deal."
                        ),
                    ),
                    field(
                        "Pod responsibility, contractor capacity, and backups",
                        "textarea",
                        (
                            "Assign each regulated, analytical, commercial, "
                            "and accounting responsibility to "
                            "a qualified person. Record "
                            "contractor hours, review dependencies, backup coverage, and the workload threshold requiring deferred intake or the scaled six-person configuration."
                        ),
                        (
                            "The base pod has one full-time "
                            "principal and three contractors: an "
                            "analyst at 50 hours monthly, "
                            "a licensed service specialist at "
                            "30, and an accounting coordinator at 12. External counsel is engaged for defined matters. Scaled staffing is two full-time personnel and four contractors, with capacity validated before accepting additional implementations."
                        ),
                    ),
                    field(
                        "Weekly KPI scorecard and evidence thresholds",
                        "textarea",
                        (
                            "Define leading, delivery, cash, and "
                            "quality indicators with denominators, "
                            "measurement periods, and accountable "
                            "owners. Include exceptions and aging so a high proposal count cannot obscure duplicate billing, incomplete disclosures, or deteriorating collections."
                        ),
                        (
                            "The weekly scorecard records 12 verified "
                            "prospects, four meetings, two authorized "
                            "reviews, and one independently checked "
                            "analysis. Quality targets are zero "
                            "duplicate economic events and 100% required disclosure delivery before covered engagement execution. Cash reporting shows unrestricted balance, overdue receivables, and the next four weeks' committed payments."
                        ),
                    ),
                    field(
                        "Canonical performance and owner-profit bridge",
                        "textarea",
                        (
                            "Present actual retained revenue, expense, "
                            "and owner profit beside "
                            "the fixed annual scenarios. "
                            "Label the measurement period and distinguish an annualized run rate from earned annual results, preserving the scorecard's team and margin assumptions."
                        ),
                        (
                            "The annual reference remains $120,000 revenue "
                            "and $38,400 profit conservative, $535,000 "
                            "and $240,750 base, and $950,000 "
                            "and $551,000 scaled. If month "
                            "four earns $26,250 advisory revenue, report that month's result separately. Multiplying it by 12 is an advisory run rate, not proof of the full base portfolio."
                        ),
                    ),
                    field(
                        "Renewal retention and recurring-revenue quality",
                        "textarea",
                        (
                            "Measure contracted employee months, cancellation "
                            "rights, commission persistency, client "
                            "concentration, and contingent-fee "
                            "dependence. Distinguish recurring contractual economics from one-time recoveries and forecasts, and document the evidence supporting each classification in a buyer-ready revenue schedule."
                        ),
                        (
                            "The base mix contains $315,000 advisory "
                            "fees, $140,000 retained commissions, and "
                            "$80,000 recovery fees. Advisory and "
                            "commission streams require contract and "
                            "persistency review before being labeled recurring. The $80,000 recovery component is separately identified as contingent, preventing a buyer from treating all $535,000 as durable subscription revenue."
                        ),
                    ),
                    field(
                        "Exit-readiness ledger and controlled diligence",
                        "textarea",
                        (
                            "List contracts, assignment provisions, carrier "
                            "relationships, license dependencies, accounting "
                            "policies, operating procedures, and "
                            "data-transfer restrictions needed for a transaction. Define staged buyer access that supports diligence without disclosing unnecessary participant information or implying automatic regulatory transfer."
                        ),
                        (
                            "The diligence index contains redacted engagements, "
                            "compensation schedules, monthly retained-revenue "
                            "bridges, renewal calendars, and process "
                            "tests. Counsel reviews assignment and "
                            "change-of-control provisions. Buyer access starts with aggregated records; participant-level access requires a separate justified process. Producer licenses and carrier appointments receive their own continuity plan rather than being listed as automatically transferable assets."
                        ),
                    ),
                    field(
                        "Day-30 decision, next sprint, and unresolved obligations",
                        "textarea",
                        (
                            "Record completed artifacts, missed milestones, "
                            "cash remaining, unresolved authority "
                            "issues, and the next "
                            "30-day priorities. State explicitly whether to continue, narrow authorized activity, defer spending, or stop a service based on observable capacity and evidence."
                        ),
                        (
                            "Day 30 ends with $22,000 unrestricted "
                            "cash, two reviewed proposals, one "
                            "pending state extension, and no "
                            "collected fees. The principal continues "
                            "authorized consulting, defers placement in the pending state, and limits next-month overhead to $6,000. The next sprint prioritizes signed scope, verified source records, and collection timing rather than declaring launch revenue prematurely."
                        ),
                    ),
                ],
                "completion_gate": (
                    "The principal signs the day-30 artifact register, staffing "
                    "and license map, current cash forecast, and next-sprint "
                    "priorities. The KPI ledger distinguishes preparation, signed "
                    "work, recognized retained revenue, and collected cash, while "
                    "the exit index contains no unnecessary participant-level disclosures."
                ),
            },
        ],
    }
