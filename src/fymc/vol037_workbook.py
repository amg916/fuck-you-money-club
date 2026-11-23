from __future__ import annotations


def build_volume_037_workbook() -> dict:
    def field(name: str, input_type: str, prompt: str, example: str) -> dict:
        return {
            "name": name,
            "type": input_type,
            "prompt": prompt,
            "example": example,
        }

    return {
        "workbook_id": "wb-037-saas-discount-and-gpo-arbitrage",
        "volume_id": "vol-037-saas-discount-and-gpo-arbitrage",
        "title": "SaaS Discount Brokerage & GPO Arbitrage — Operator Companion Workbook",
        "subtitle": (
            "6 Printable Operator Worksheets for Authorized SaaS Brokerage, "
            "Partner Attribution, GPO Rebates, Shared-Savings Audits, "
            "Reserve-Safe Execution, and Transferable Small-Team Operations"
        ),
        "worksheets": [
            {
                "worksheet_id": "ws-01",
                "number": 1,
                "title": "Arbitrage Deal / Counterparty Underwriting & Spread Qualification",
                "purpose": (
                    "Qualify an authorized software discount opportunity before promising "
                    "savings or accepting payment. Establish the actual customer, licensed "
                    "tenant, distribution route, renewal deadline, collectible retained "
                    "spread, and downside exposure. Reject opportunities that depend on "
                    "unapproved pooling, speculative rebates, or unsupported partner status."
                ),
                "chapter_ref": "Q1, Q2, Q6",
                "instructions": [
                    (
                        "Open one opportunity record per customer contracting entity and "
                        "renewal cohort. Attach customer-provided invoices, subscription "
                        "exports, and written research permission. Keep distinct tenants "
                        "separate even when a common parent owns several operating companies."
                    ),
                    (
                        "Verify the proposed route with the relevant distributor or "
                        "master agent before quoting. Separate purchase authorization, "
                        "partner attribution, delegated administration, and subscription "
                        "transfer rights; a CPOR association alone does not establish "
                        "every permission required for fulfillment."
                    ),
                    (
                        "Normalize each incumbent invoice to comparable seats, editions, "
                        "terms, support, and taxes. Establish a documented baseline rather "
                        "than comparing an annual negotiated price with an inflated "
                        "monthly list price or a materially different product."
                    ),
                    (
                        "Request dated evidence for customer credit quality and supplier "
                        "settlement terms. Price the complete annual commitment exposure, "
                        "not just the next monthly installment. Treat delayed rebates "
                        "and disputed commissions as separate collection risks."
                    ),
                    (
                        "Write a specific accept, revise, or reject decision with an "
                        "accountable owner and expiration date. Advance only when the "
                        "authorized route, enforceable customer obligations, collectible "
                        "spread, and required prefunding all survive a documented downside case."
                    ),
                ],
                "fields": [
                    field(
                        "Customer entity, tenant, and authority",
                        "textarea",
                        (
                            "Identify the contracting entity, tenant identifiers, billing "
                            "contact, and individual authorized to approve procurement. "
                            "Explain how the collected evidence connects the customer "
                            "agreement to each subscription without crossing tenant boundaries."
                        ),
                        (
                            "Harbor Design LLC supplies its incorporation record, current "
                            "Microsoft invoice, and tenant export covering 120 licensed "
                            "employees. Its procurement director signs the purchasing "
                            "mandate. The affiliate operating 35 additional seats remains "
                            "outside this opportunity until it executes a separate agreement."
                        ),
                    ),
                    field(
                        "Authorized distribution and attribution route",
                        "textarea",
                        (
                            "Record the vendor program, distributor, relationship evidence, "
                            "and precise transaction permissions. Distinguish attribution "
                            "from reseller authority and administrative access; identify "
                            "the written source governing any proposed subscription or partner change."
                        ),
                        (
                            "The proposed Microsoft route uses the brokerage's active "
                            "Pax8 reseller relationship and the customer's accepted "
                            "purchasing relationship. Operations verifies applicable CSP "
                            "transfer eligibility separately. Any CPOR claim is handled "
                            "only where the relevant program supports it; delegated "
                            "administration receives separate scoped authorization."
                        ),
                    ),
                    field(
                        "Renewal cliff and cancellation evidence",
                        "textarea",
                        (
                            "Capture subscription renewal dates, commitment duration, "
                            "billing cadence, notice requirements, and the authoritative "
                            "source for change windows. Assign an owner to confirm "
                            "current program rules before representing any cancellation right."
                        ),
                        (
                            "The 120-seat cohort renews on September 1 under an annual "
                            "commitment with monthly billing. Operations saves the current "
                            "distributor terms and portal deadline evidence on August 5. "
                            "An internal August 20 decision deadline leaves time for "
                            "customer funding and supplier confirmation."
                        ),
                    ),
                    field(
                        "Comparable spend baseline",
                        "textarea",
                        (
                            "Build the baseline from actual recurring charges and "
                            "equivalent entitlements. Separate taxes, implementation work, "
                            "temporary credits, unused seats, and true product changes "
                            "so every claimed saving has an identifiable economic source."
                        ),
                        (
                            "The verified cohort contains 120 seats priced at $20 per "
                            "seat monthly, producing $28,800 annual subscription charges "
                            "before tax. A separate $1,200 migration invoice is excluded. "
                            "The comparison retains the same edition, annual commitment, "
                            "support scope, and seat count throughout the quote."
                        ),
                    ),
                    field(
                        "Retained spread qualification",
                        "textarea",
                        (
                            "Calculate customer billings, supplier entitlement, retained "
                            "spread, and effective retained_share for the proposed route. "
                            "Identify contractual adjustments and distinguish economic "
                            "spread calculations from the separate ASC 606 presentation assessment."
                        ),
                        (
                            "For this illustrative quote, annual customer billings equal "
                            "$28,800 and the distributor entitlement equals $26,496. "
                            "Retained spread is $2,304, with retained_share of 8%. "
                            "The agency assessment supports recording only that retained "
                            "amount as operator revenue; customer subscription spend "
                            "does not become brokerage revenue."
                        ),
                    ),
                    field(
                        "Counterparty payment capacity",
                        "textarea",
                        (
                            "Summarize objective payment evidence, authorized references, "
                            "payment method, and unresolved disputes. Quantify annual "
                            "supplier exposure if customer collections stop, and specify "
                            "which funding evidence must exist before a commitment is placed."
                        ),
                        (
                            "Harbor supplies twelve months of timely incumbent payments "
                            "and two trade references under written permission. The "
                            "brokerage still requires $28,800 annual prefunding before "
                            "placing the order. A stored payment method alone cannot "
                            "cover the $26,496 supplier obligation if later collections fail."
                        ),
                    ),
                    field(
                        "GPO membership and rebate eligibility",
                        "textarea",
                        (
                            "Document the member agreement, eligible products, volume "
                            "bracket, measurement period, exclusions, rebate recipient, "
                            "and settlement lag. Explain whether aggregation changes "
                            "commercial pricing only or also changes any licensed usage rights."
                        ),
                        (
                            "A signed illustrative GPO schedule pays a 5% administrative "
                            "rebate on $1,600,000 of eligible annual member purchases, "
                            "yielding $80,000 before operating costs. Members retain "
                            "separate tenants and licenses. Returns reduce eligible "
                            "volume, and settlement occurs quarterly after the supplier "
                            "validates the membership roster."
                        ),
                    ),
                    field(
                        "Master-agent residual rights",
                        "textarea",
                        (
                            "Identify the master-agent agreement, eligible recurring "
                            "billing base, commission percentage, activation condition, "
                            "payment lag, and clawback period. Determine whether residual "
                            "rights survive account reassignment, termination, or a sale of the brokerage."
                        ),
                        (
                            "An illustrative Telarus channel schedule credits 5% on "
                            "$5,000 monthly eligible UCaaS charges per activated customer. "
                            "Forty continuously active accounts produce $120,000 annual "
                            "residuals. The reviewer verifies exclusions, termination "
                            "language, and assignment restrictions rather than treating "
                            "the modeled percentage as a published program rate."
                        ),
                    ),
                    field(
                        "Shared-savings baseline and fee claim",
                        "textarea",
                        (
                            "State the baseline methodology, measurement period, fee "
                            "percentage, validation process, and treatment of supplier "
                            "rebates. Exclude reductions caused by unrelated workforce "
                            "changes unless the agreement explicitly includes that service."
                        ),
                        (
                            "A comparable annual renewal falls from $240,000 to $200,000 "
                            "without changing seats or entitlements. Verified savings "
                            "equal $40,000. A signed 30% success-fee clause produces "
                            "$12,000 operator revenue and $28,000 customer benefit after "
                            "the fee, with supplier-funded credits separately disclosed "
                            "and excluded from duplicate claims."
                        ),
                    ),
                    field(
                        "Decision, exception, and downside owner",
                        "textarea",
                        (
                            "Write the underwriting decision and quantify its failure "
                            "threshold. Name the person responsible for each unresolved "
                            "condition, establish a quote expiration, and specify the "
                            "evidence that would require rejection rather than repricing."
                        ),
                        (
                            "Accept Harbor only after cleared prefunding and confirmed "
                            "supplier terms by August 20. If supplier cost rises to "
                            "$27,360, retained spread falls to $1,440, or 5%. "
                            "The deal owner must reprice or reject; combining unrelated "
                            "customers into one tenant is never an acceptable remedy."
                        ),
                    ),
                ],
                "completion_gate": (
                    "The deal owner and operations reviewer sign the dated evidence "
                    "packet. Customer authority, supplier route, renewal deadline, "
                    "collectible retained spread, and full commitment funding must "
                    "be documented; any unresolved licensing boundary stops placement."
                ),
            },
            {
                "worksheet_id": "ws-02",
                "number": 2,
                "title": "Unit Economics, Escrow/Reserve Float & Working-Capital Calculator",
                "purpose": (
                    "Convert channel activity into recognized operator revenue, owner "
                    "profit, and cash requirements without counting customer software "
                    "spend as earnings. Reconcile the three canonical scenarios, "
                    "calculate settlement timing and reserve coverage, and distinguish "
                    "ordinary operating reserves from genuinely restricted escrow funds."
                ),
                "chapter_ref": "Q3, Q4",
                "instructions": [
                    (
                        "Create separate schedules for customer subscription billings, "
                        "supplier entitlements, operator revenue, operating costs, and "
                        "cash movements. Apply retained_share only to the applicable "
                        "spread-bearing billings, then add independently earned residuals, "
                        "administrative rebates, and shared-savings fees."
                    ),
                    (
                        "Copy the Conservative, Base, and Scaled scorecard totals "
                        "exactly before building supporting transaction assumptions. "
                        "Treat the supplied gross revenue label as operator revenue "
                        "on the stated net-retained basis, never as underlying member purchases."
                    ),
                    (
                        "Prepare a thirteen-week cash forecast using actual contractual "
                        "payment dates. Show rebate lags, commission disputes, customer "
                        "prefunding, supplier commitments, and processor holds separately; "
                        "annual profit does not establish the cash available for next "
                        "week's supplier debit."
                    ),
                    (
                        "Identify the legal holder and withdrawal conditions for "
                        "each reserve or escrow balance. Do not describe an ordinary "
                        "brokerage bank account as escrow. Document how customer "
                        "refund obligations and remaining annual commitments constrain "
                        "apparently available cash."
                    ),
                    (
                        "Stress the model for tier compression, delayed collections, "
                        "credit defaults, and lost renewals. Keep the canonical "
                        "scorecard unchanged, report stress cases alongside it, and "
                        "define the cash threshold that suspends additional commitments "
                        "before funding becomes insufficient."
                    ),
                ],
                "fields": [
                    field(
                        "Revenue basis and retained_share bridge",
                        "textarea",
                        (
                            "Define each revenue stream and the applicable recognition "
                            "basis. Show the equation connecting underlying billings "
                            "to retained contribution, with separate treatment for "
                            "supplier liabilities, taxes, and fees earned outside the resale spread."
                        ),
                        (
                            "For agency-classified wholesale activity, $2,500,000 annual "
                            "customer billings multiplied by retained_share of 0.08 "
                            "produce $200,000 operator revenue. Supplier entitlement "
                            "equals $2,300,000. Add $120,000 residuals, $80,000 GPO "
                            "administrative rebates, and $100,000 earned audit fees "
                            "to reach $500,000 total operator revenue."
                        ),
                    ),
                    field(
                        "Conservative canonical reconciliation",
                        "textarea",
                        (
                            "Reconcile the Conservative revenue, net margin, owner "
                            "profit, and implied total costs. Preserve the specified "
                            "staffing model, and explain how illustrative stream "
                            "allocations support rather than replace the canonical annual totals."
                        ),
                        (
                            "Conservative operator revenue is $100,000, comprising an "
                            "illustrative $40,000 spread, $24,000 residuals, $16,000 "
                            "rebates, and $20,000 audit fees. At 32% net margin, "
                            "annual owner net profit is $32,000 and implied costs "
                            "are $68,000. Staffing remains one full-time operator "
                            "plus three contractors."
                        ),
                    ),
                    field(
                        "Base canonical reconciliation",
                        "textarea",
                        (
                            "Reconcile the Base revenue streams, total costs, net "
                            "margin, and annual owner profit. Explain the treatment "
                            "of supplier pass-through amounts so the same subscription "
                            "spend cannot inflate both reported revenue and operating expense."
                        ),
                        (
                            "Base operator revenue equals $500,000 and total modeled "
                            "costs equal $275,000, leaving $225,000 annual owner net "
                            "profit at 45.0%. The team is one full-time operator "
                            "plus three contractors. The $2,300,000 wholesale supplier "
                            "entitlement is excluded from both agency revenue and "
                            "these modeled operating costs."
                        ),
                    ),
                    field(
                        "Scaled canonical reconciliation",
                        "textarea",
                        (
                            "Record the Scaled revenue, margin, owner profit, total "
                            "costs, and six-person staffing structure. Identify a "
                            "consistent illustrative stream mix without silently "
                            "changing the canonical margin to accommodate a different operating design."
                        ),
                        (
                            "Scaled operator revenue is $900,000: $360,000 spread, "
                            "$216,000 residuals, $144,000 rebates, and $180,000 audit "
                            "fees. Costs equal $378,000, producing $522,000 annual "
                            "owner net profit at 58%. Staffing is two full-time "
                            "people plus four contractors, six people in total."
                        ),
                    ),
                    field(
                        "Operating expense scope and cost bridge",
                        "textarea",
                        (
                            "Separate the quoted monthly operating expense range "
                            "from total scenario costs. State which direct delivery, "
                            "acquisition, contractor, reserve, and support expenses "
                            "sit outside the selected overhead subtotal, avoiding duplicate expense recognition."
                        ),
                        (
                            "The published monthly opex range is $1,500–$9,500. "
                            "For an illustrative Base bridge, select $5,000 monthly "
                            "overhead, or $60,000 annually, plus $120,000 delivery "
                            "labor, $55,000 acquisition, and $40,000 other direct "
                            "costs and modeled losses. These nonoverlapping categories "
                            "sum to the required $275,000."
                        ),
                    ),
                    field(
                        "Annual commitment funding calculator",
                        "textarea",
                        (
                            "Calculate customer prefunding, total supplier commitment, "
                            "unencumbered spread, and any remaining exposure. Distinguish "
                            "payment authorization from cleared funds, and show how "
                            "a customer default changes exposure when installments were mistakenly allowed."
                        ),
                        (
                            "Harbor prepays $28,800 against a $26,496 annual supplier "
                            "commitment, leaving $2,304 spread before costs and reserves. "
                            "With monthly supplier installments of $2,208, default "
                            "after three paid months would otherwise leave $19,872 "
                            "of supplier exposure. Full annual prefunding prevents "
                            "that installment-funded mismatch."
                        ),
                    ),
                    field(
                        "Reserve ownership and escrow classification",
                        "textarea",
                        (
                            "Identify each balance's owner, bank arrangement, permitted "
                            "uses, release triggers, and accounting classification. "
                            "Explain whether the funds are a brokerage reserve, "
                            "customer liability, or separately administered escrow under an executed agreement."
                        ),
                        (
                            "The brokerage keeps a $12,000 operating risk reserve "
                            "in a dedicated account owned by the brokerage. It "
                            "is not escrow. A separate customer deposit ledger "
                            "tracks $28,800 received for Harbor; supplier funding "
                            "and any refund rights remain encumbrances until the "
                            "applicable contractual obligations are satisfied."
                        ),
                    ),
                    field(
                        "Settlement lag and thirteen-week cash need",
                        "textarea",
                        (
                            "Map cash receipts and disbursements by week using "
                            "contractual settlement dates. Calculate peak cumulative "
                            "deficit without borrowing customer subscription funds, "
                            "and specify the available capital supporting that deficit and the protected reserve."
                        ),
                        (
                            "A launch begins with $25,000 capital, within the "
                            "$5,000–$30,000 startup range. Three months of $5,000 "
                            "cash operating costs consume $15,000 before a $20,000 "
                            "rebate arrives in week thirteen. Peak deficit is "
                            "$15,000; a $5,000 protected reserve leaves $5,000 "
                            "additional cash headroom."
                        ),
                    ),
                    field(
                        "Shared-savings and commission collection math",
                        "textarea",
                        (
                            "Calculate fee entitlement, invoice date, expected cash "
                            "date, dispute exposure, and collection cost for contingent "
                            "revenue. Keep measured savings, customer benefit, earned "
                            "fees, and cash receipts in distinct columns of the supporting schedule."
                        ),
                        (
                            "Ten comparable renewal audits each validate $40,000 "
                            "savings. At the contractual 25% fee, each earns "
                            "$10,000 and total earned fees equal $100,000. "
                            "If two invoices remain unpaid, cash receipts are "
                            "$80,000 and receivables are $20,000; the $400,000 "
                            "customer savings pool is never operator revenue."
                        ),
                    ),
                    field(
                        "Tier compression and liquidity stress",
                        "textarea",
                        (
                            "Model a specific adverse change without altering the "
                            "canonical reference case. Quantify revenue loss, revised "
                            "profit, collection delay, and cash response; identify "
                            "the minimum unrestricted balance required before accepting further annual commitments."
                        ),
                        (
                            "Reducing the Base wholesale retained_share from 8% "
                            "to 6% on $2,500,000 billings removes $50,000 revenue. "
                            "With costs unchanged at $275,000, stress-case profit "
                            "becomes $175,000 on $450,000 revenue. Pause new "
                            "unfunded commitments whenever unrestricted cash would "
                            "fall below the separately approved $12,000 reserve."
                        ),
                    ),
                ],
                "completion_gate": (
                    "The reviewer independently recomputes $32,000, $225,000, and "
                    "$522,000 annual owner net profit from the canonical scenarios. "
                    "Every cash forecast excludes encumbered customer money from "
                    "available working capital and identifies funding for the peak deficit."
                ),
            },
            {
                "worksheet_id": "ws-03",
                "number": 3,
                "title": "End-to-End Execution, Idempotent Ledger & QA Pre-Flight Sheet",
                "purpose": (
                    "Turn an approved opportunity into a traceable order, license "
                    "record, supplier payable, and collectible operator fee. Prevent "
                    "duplicate commitments through idempotent processing, verify tenant "
                    "boundaries, reconcile settlement evidence, and define safe recovery "
                    "when a distributor response or billing event is ambiguous."
                ),
                "chapter_ref": "Q7, Q8",
                "instructions": [
                    (
                        "Assign a stable internal deal identifier before collecting "
                        "documents or creating orders. Link customer, tenant, supplier, "
                        "subscription, and contract records through explicit identifiers "
                        "rather than email subjects, editable company names, or "
                        "spreadsheet row positions."
                    ),
                    (
                        "Define separate order, payment, entitlement, and recognition "
                        "states. Require evidence for each transition and retain "
                        "the original event payload. An accepted payment does "
                        "not prove provisioning, and provisioning does not independently "
                        "prove that a commission was earned."
                    ),
                    (
                        "Use a database uniqueness constraint for local event "
                        "processing and supplier idempotency features where supported. "
                        "After an ambiguous timeout, query supplier status before "
                        "retrying a commitment; local deduplication cannot reverse "
                        "an order already accepted upstream."
                    ),
                    (
                        "Run a preflight comparison against the signed quote "
                        "before submitting any order. Check tenant, product, "
                        "quantity, term, funding, support scope, and applicable "
                        "program permissions. Have a second reviewer inspect "
                        "high-exposure annual commitments."
                    ),
                    (
                        "Reconcile orders, entitlements, supplier statements, customer "
                        "balances, and operator earnings daily during launch. "
                        "Route mismatches to a documented exception queue and "
                        "preserve reversible actions where available; never use "
                        "license deletion as an improvised billing correction."
                    ),
                ],
                "fields": [
                    field(
                        "Deal identifiers and system of record",
                        "textarea",
                        (
                            "Specify stable identifiers for the deal, customer entity, "
                            "tenant, subscription cohort, and supplier account. Name "
                            "the authoritative system for each attribute and describe "
                            "how amendments remain linked without rewriting original evidence."
                        ),
                        (
                            "Deal D037-001 links customer C-014, tenant T-014, "
                            "cohort R-2026-09, and distributor account P-008. "
                            "PostgreSQL stores operational identifiers; the signed "
                            "contract repository stores commercial authority. Amendment "
                            "A-002 references D037-001 and preserves A-001, allowing "
                            "reviewers to reconstruct the original 120-seat purchase "
                            "and later authorized changes."
                        ),
                    ),
                    field(
                        "Order state transitions",
                        "textarea",
                        (
                            "Define the allowed order states, transition evidence, "
                            "responsible role, and forbidden shortcuts. Separate "
                            "commercial acceptance from supplier submission, activation, "
                            "settlement, and revenue recognition so operational status cannot silently create earnings."
                        ),
                        (
                            "D037-001 progresses through drafted, reviewed, funded, "
                            "submitted, confirmed, and reconciled. The funded state "
                            "requires bank evidence; confirmed requires a supplier "
                            "order identifier and matching entitlement export. An "
                            "HTTP timeout leaves the order submitted with an "
                            "exception flag, never automatically confirmed or resubmitted."
                        ),
                    ),
                    field(
                        "Idempotency key and uniqueness control",
                        "textarea",
                        (
                            "Describe the canonical business key, payload version, "
                            "database constraint, and retry behavior for each "
                            "commitment-creating operation. State how the process "
                            "handles supplier endpoints that provide no native idempotency support."
                        ),
                        (
                            "The local order key combines D037-001, T-014, "
                            "R-2026-09, and quote version 3. A unique database "
                            "constraint admits one active placement intent. A "
                            "transactional outbox tracks delivery. When supplier "
                            "idempotency is unavailable, ambiguous results enter "
                            "manual reconciliation before any operator can authorize "
                            "a replacement submission."
                        ),
                    ),
                    field(
                        "Webhook authenticity and replay handling",
                        "textarea",
                        (
                            "Record the provider's supported authentication method, "
                            "event identifier, timestamp checks, replay protection, "
                            "and payload retention. Explain how duplicate delivery "
                            "or out-of-order events affect state without assuming all providers expose identical controls."
                        ),
                        (
                            "For a provider offering signed webhooks, the receiver "
                            "checks its documented signature and timestamp rules "
                            "before storing the event. Event E-441 has a unique "
                            "provider-event key. Three duplicate deliveries produce "
                            "one ledger transition, while an older pending event "
                            "cannot overwrite the later confirmed order state."
                        ),
                    ),
                    field(
                        "Tenant and entitlement preflight",
                        "textarea",
                        (
                            "List the exact comparisons required before placement "
                            "and after activation. Include tenant identity, edition, "
                            "seat quantity, commitment term, support responsibility, "
                            "and permitted transfer route, with an explicit prohibition on unauthorized cross-customer pooling."
                        ),
                        (
                            "The reviewer matches T-014, 120 seats, the quoted "
                            "edition, annual commitment, and $28,800 customer charge "
                            "against the signed order. The post-activation export "
                            "must show the same tenant and quantity. A proposed "
                            "move into the broker's tenant fails preflight even "
                            "if it appears to improve pricing."
                        ),
                    ),
                    field(
                        "Agency ledger posting and recognition",
                        "textarea",
                        (
                            "Describe the debit and credit sequence for customer "
                            "receipts, supplier obligations, deferred fees, and "
                            "earned operator revenue. Tie recognition timing to "
                            "the documented performance obligation rather than automatically recognizing the full retained spread at collection."
                        ),
                        (
                            "For this agency-classified arrangement, receipt debits "
                            "cash $28,800 and credits a clearing liability $28,800. "
                            "Allocation debits clearing $28,800, credits supplier "
                            "payable $26,496, and credits deferred operator fees "
                            "$2,304. The assessed stand-ready service recognizes "
                            "$192 monthly for twelve months by releasing deferred fees."
                        ),
                    ),
                    field(
                        "Daily three-way reconciliation",
                        "textarea",
                        (
                            "Define the comparison between accepted orders, live "
                            "entitlements, and supplier billing, then connect the "
                            "result to customer balances and operator earnings. "
                            "Specify materiality thresholds and ownership for every unmatched item."
                        ),
                        (
                            "The daily job compares 120 ordered seats with 120 "
                            "active entitlements and a $2,208 monthly supplier "
                            "installment. A statement showing 125 seats creates "
                            "a five-seat exception, not an automatic customer "
                            "invoice. Operations investigates that day and keeps "
                            "the unmatched charge outside the approved settlement batch."
                        ),
                    ),
                    field(
                        "Timeout and partial-failure recovery",
                        "textarea",
                        (
                            "Write the recovery sequence for an uncertain order "
                            "response or partial provisioning event. Identify "
                            "read-only checks, customer communication, supplier "
                            "escalation, and the evidence required before any irreversible remedial action is attempted."
                        ),
                        (
                            "A distributor request times out after submission. "
                            "Operations searches by the client reference and "
                            "retrieves supplier order S-778 showing 120 seats "
                            "pending activation. The worker links S-778 to "
                            "D037-001 instead of submitting again, informs Harbor "
                            "of the delay, and schedules a status check in "
                            "thirty minutes."
                        ),
                    ),
                    field(
                        "Credit, refund, and clawback correction",
                        "textarea",
                        (
                            "Define how supplier credits, customer refunds, and "
                            "commission reversals enter the ledger without "
                            "deleting original entries. Specify linkage, reviewer "
                            "approval, period treatment, and reconciliation against the next supplier or master-agent statement."
                        ),
                        (
                            "A $300 residual clawback references original earning "
                            "E-190 and supplier adjustment C-021. Accounting "
                            "records a separate $300 reduction to commission "
                            "revenue or the applicable estimate, then reconciles "
                            "the reduced remittance. The original earning stays "
                            "visible, and the customer receives no unrelated "
                            "subscription change."
                        ),
                    ),
                    field(
                        "Evidence packet and QA sign-off",
                        "textarea",
                        (
                            "List the evidence required to close execution, "
                            "including contract version, funding proof, supplier "
                            "confirmation, entitlement export, recognition schedule, "
                            "and exception resolution. Assign an independent reviewer and record their dated decision."
                        ),
                        (
                            "Packet D037-001 contains signed quote version 3, "
                            "cleared bank receipt, supplier order S-778, the "
                            "120-seat entitlement export, and the twelve-month "
                            "$192 recognition schedule. A second reviewer "
                            "signs the checklist after resolving the five-seat "
                            "statement discrepancy; the erroneous supplier charge "
                            "remains linked to its credit."
                        ),
                    ),
                ],
                "completion_gate": (
                    "A duplicate-event replay creates no extra order or ledger "
                    "posting, an ambiguous-timeout test triggers reconciliation "
                    "rather than blind resubmission, and the reviewer matches "
                    "the signed quote to funding, entitlements, supplier billing, "
                    "and the recognition schedule."
                ),
            },
            {
                "worksheet_id": "ws-04",
                "number": 4,
                "title": "Statutory, Licensing, Contract Addendum & Compliance Audit",
                "purpose": (
                    "Translate licensing, outreach, payment, and accounting obligations "
                    "into evidence-backed operating requirements. Establish authorized "
                    "program participation, bounded delegated access, enforceable "
                    "commercial terms, and accurate revenue presentation while "
                    "preventing tenant pooling, misleading savings claims, and "
                    "uncontrolled use of customer procurement information."
                ),
                "chapter_ref": "Q5, Q9",
                "instructions": [
                    (
                        "Collect the actual agreements governing the selected "
                        "vendor route and record their effective dates. Separate "
                        "Microsoft CSP purchasing, applicable CPOR attribution, "
                        "Adobe VIP Marketplace membership, and Zoom channel "
                        "permissions instead of treating them as interchangeable "
                        "transfer mechanisms."
                    ),
                    (
                        "Map each outbound channel to the relevant federal "
                        "and state requirements before activation. Document "
                        "recipient type, dialing technology, consent evidence "
                        "where required, suppression procedures, and substantiation "
                        "of every savings claim used by callers or messages."
                    ),
                    (
                        "Draft addenda that define baseline calculations, fee "
                        "entitlement, payment timing, annual commitment liability, "
                        "and access boundaries. Use objective acceptance evidence "
                        "and explicit adjustment rules so disputes do not "
                        "depend on informal sales promises."
                    ),
                    (
                        "Have the accounting owner document the ASC 606 "
                        "principal-versus-agent assessment for each specified "
                        "service. Evaluate control and performance obligations "
                        "rather than assuming every channel contract shares "
                        "the same revenue presentation or recognition schedule."
                    ),
                    (
                        "Maintain a dated control register with evidence "
                        "locations, responsible people, review frequency, and "
                        "remediation deadlines. Recheck affected controls when "
                        "vendor terms, outreach technology, payment methods, "
                        "customer jurisdictions, or the brokerage's service "
                        "scope changes materially."
                    ),
                ],
                "fields": [
                    field(
                        "Vendor program and license boundary register",
                        "textarea",
                        (
                            "Record the agreement governing each licensed activity "
                            "and explain the authority it grants. Identify "
                            "separate requirements for purchasing, attribution, "
                            "transfer, delegation, and end-user use so commercial discounting cannot expand licensed access."
                        ),
                        (
                            "The register links Microsoft purchasing to the "
                            "active CSP distribution agreement, Adobe orders "
                            "to the customer's VIP Marketplace route, and Zoom "
                            "residuals to the applicable Zoom Up or TSD "
                            "agreement. It records CPOR only for supported "
                            "attribution activity and prohibits unauthorized "
                            "seat-sharing between unrelated customer tenants."
                        ),
                    ),
                    field(
                        "Annual commitment and prefunding addendum",
                        "textarea",
                        (
                            "Draft concrete terms covering commitment duration, "
                            "billing cadence, customer funding, supplier change "
                            "windows, and refund handling. State who bears "
                            "remaining supplier obligations and prevent sales language from implying monthly cancellation of annual commitments."
                        ),
                        (
                            "The addendum states: Customer funds $28,800 before "
                            "placement of the twelve-month 120-seat order. "
                            "Monthly supplier billing does not shorten the "
                            "annual commitment. Reductions and cancellations "
                            "follow the attached current supplier rules. "
                            "Refunds reflect actual recoverable supplier "
                            "credits and the separately stated earned "
                            "service-fee treatment."
                        ),
                    ),
                    field(
                        "TCPA and telephone outreach controls",
                        "textarea",
                        (
                            "Map telephone activity to 47 U.S.C. § 227 and "
                            "47 CFR § 64.1200, including recipient numbers, "
                            "technology, consent requirements, calling restrictions, "
                            "and suppression evidence. Include applicable state rules rather than assuming business targeting creates a blanket exemption."
                        ),
                        (
                            "The pilot uses manually placed live calls to "
                            "verified business office numbers during recipient "
                            "business hours. It excludes automated texts, "
                            "prerecorded messages, and artificial-voice calls. "
                            "The owner reviews mobile-number and state-law "
                            "exposure before expansion, logs required permission, "
                            "and suppresses an opted-out number before the "
                            "next dialing batch."
                        ),
                    ),
                    field(
                        "FTC TSR and claims substantiation",
                        "textarea",
                        (
                            "Review 16 CFR Part 310 and FTC Act "
                            "15 U.S.C. § 45 against the proposed sales "
                            "process. Explain applicable B2B limits, prohibited "
                            "misrepresentations, recordkeeping duties, and the evidence supporting stated affiliations and savings."
                        ),
                        (
                            "The script says the brokerage will evaluate "
                            "documented renewal savings, not that Microsoft "
                            "appointed it to audit the prospect. The control "
                            "owner checks the TSR's current B2B scope, including "
                            "prohibitions on material misrepresentations, and "
                            "retains substantiation and records required for "
                            "the actual campaign and its applicable retention period."
                        ),
                    ),
                    field(
                        "Commercial email and suppression procedure",
                        "textarea",
                        (
                            "Apply CAN-SPAM, 15 U.S.C. § 7704, to "
                            "commercial email content and suppression handling. "
                            "Specify truthful routing information, subject lines, "
                            "advertising identification where required, postal address, opt-out functionality, and responsibility for outside senders."
                        ),
                        (
                            "A renewal-audit email uses the brokerage's real "
                            "sender identity, a factual subject, its postal "
                            "address, and a working unsubscribe link. The "
                            "system processes opt-outs immediately, within "
                            "the statutory ten-business-day limit, keeps the "
                            "mechanism available for thirty days after sending, "
                            "and prevents an agency from reimporting suppressed contacts."
                        ),
                    ),
                    field(
                        "Shared-savings and rebate disclosure clauses",
                        "textarea",
                        (
                            "Write the fee calculation, validation rights, "
                            "measurement boundaries, adjustment process, and "
                            "disclosure of supplier-paid compensation. Explain "
                            "how the agreement prevents duplicate charges when shared savings and channel remuneration touch the same renewal."
                        ),
                        (
                            "The clause defines comparable savings as verified "
                            "baseline cost minus executed renewal cost, "
                            "excluding taxes and unrelated seat reductions. "
                            "A 30% fee applies to $40,000 validated savings, "
                            "producing $12,000. The schedule discloses supplier "
                            "compensation and credits overlapping remuneration "
                            "against the audit fee where the signed "
                            "agreement requires that treatment."
                        ),
                    ),
                    field(
                        "ASC 606 principal-versus-agent memorandum",
                        "textarea",
                        (
                            "Document the specified services, control assessment, "
                            "performance obligations, variable consideration, and "
                            "recognition timing under ASC 606. Reference "
                            "ASC 606-10-55-36 through 55-40 for principal-versus-agent analysis and distinguish contractual economics from presentation conclusions."
                        ),
                        (
                            "The memorandum concludes that the modeled wholesale "
                            "arrangement is agency-classified and presents "
                            "$2,304 retained fees rather than $28,800 subscription "
                            "billings. It separately assesses the stand-ready "
                            "service period and rebate uncertainty. If an "
                            "actual arrangement establishes control before "
                            "transfer, accounting reassesses presentation instead "
                            "of forcing the portfolio assumption."
                        ),
                    ),
                    field(
                        "Payment authorization and account controls",
                        "textarea",
                        (
                            "Identify ACH or card authorization evidence, "
                            "processor rules, account classification, payment "
                            "reversibility, and funding-release controls. "
                            "Distinguish business-account requirements from consumer protections, and explain why an authorization alone does not eliminate collection risk."
                        ),
                        (
                            "Harbor signs a business ACH authorization through "
                            "the processor, which applies the relevant Nacha "
                            "requirements and its own underwriting rules. "
                            "The reviewer checks UCC Article 4A applicability "
                            "for covered transfers and does not assume "
                            "consumer Regulation E, 12 CFR Part 1005, "
                            "governs the business account."
                        ),
                    ),
                    field(
                        "Customer information and delegated access",
                        "textarea",
                        (
                            "Define the minimum procurement information and "
                            "administrative permissions required, retention "
                            "periods, deletion procedures, and access reviewers. "
                            "Assess applicable privacy duties, including California Civil Code § 1798.100 et seq. where its scope requirements are met."
                        ),
                        (
                            "The audit collects invoices, SKU counts, renewal "
                            "dates, and authorized contacts, but no mailbox "
                            "content. A scoped GDAP relationship is used "
                            "only when the service requires administration. "
                            "Access expires after the engagement, procurement "
                            "files follow the documented retention schedule, "
                            "and the quarterly reviewer removes inactive "
                            "contractor accounts."
                        ),
                    ),
                    field(
                        "GPO competition boundaries and audit remediation",
                        "textarea",
                        (
                            "Specify lawful purchasing coordination boundaries, "
                            "member information restrictions, and remediation "
                            "owners. Assess Sherman Act concerns under "
                            "15 U.S.C. § 1 when sharing competitively sensitive information or coordinating purchasing behavior beyond the signed program."
                        ),
                        (
                            "Members submit eligible purchase totals to the "
                            "GPO administrator, not competitors' future "
                            "selling prices, wages, or customer strategies. "
                            "The administrator distributes aggregated bracket "
                            "results only. A discovered cross-member pricing "
                            "spreadsheet is access-restricted immediately, "
                            "preserved for review, and removed from routine "
                            "distribution before the next quarterly rebate "
                            "calculation."
                        ),
                    ),
                ],
                "completion_gate": (
                    "The responsible reviewer signs the vendor-authority register, "
                    "outreach controls, payment addendum, compensation disclosures, "
                    "access register, and ASC 606 memorandum. Every unresolved "
                    "finding has an owner and deadline; activities affected by "
                    "missing authority or required permission remain inactive."
                ),
            },
            {
                "worksheet_id": "ws-05",
                "number": 5,
                "title": "Automation Pipeline, Acquisition Flywheel & Risk Fallback Tracker",
                "purpose": (
                    "Build a measurable acquisition and fulfillment pipeline using "
                    "permitted technographic research, verified renewal evidence, "
                    "authorized distributor integrations, and auditable pricing "
                    "logic. Connect every automation to an accountable operator, "
                    "detect economic deterioration early, and preserve a manual "
                    "fallback that cannot duplicate commitments."
                ),
                "chapter_ref": "Q6, Q10",
                "instructions": [
                    (
                        "Define the ideal customer using observable procurement "
                        "conditions rather than speculative company profiling. "
                        "Use public DNS and customer-authorized evidence "
                        "as research inputs, then verify actual products, "
                        "seat counts, and renewal dates directly before "
                        "claiming an opportunity."
                    ),
                    (
                        "Instrument the pipeline from researched account "
                        "through accepted audit, signed engagement, funded "
                        "order, and collected fee. Distinguish observed "
                        "conversion from planning assumptions and exclude "
                        "customer software spend when calculating acquisition "
                        "payback or channel productivity."
                    ),
                    (
                        "Connect only approved accounts and documented "
                        "interfaces for Pax8, Ingram, Telarus, or other "
                        "selected providers. Separate read-only imports "
                        "from commitment-creating actions, and preserve "
                        "manual evidence capture when a provider lacks "
                        "the required API capability."
                    ),
                    (
                        "Version benchmark inputs, supplier floors, "
                        "shared-savings calculations, and exception rules. "
                        "Recompute the customer proposal when any "
                        "material assumption changes, and require a "
                        "reviewed quote version before automation can "
                        "place or amend a paid subscription."
                    ),
                    (
                        "Set thresholds for integration failures, rebate "
                        "compression, defaults, and licensing anomalies. "
                        "Document the safe fallback and recovery owner "
                        "for each condition; restoring throughput is "
                        "secondary to preventing duplicate orders, "
                        "unsupported claims, or unauthorized tenant changes."
                    ),
                ],
                "fields": [
                    field(
                        "Ideal customer and renewal trigger definition",
                        "textarea",
                        (
                            "Define customer size, product mix, renewal horizon, "
                            "purchase authority, and minimum collectible opportunity. "
                            "Identify the evidence required to qualify each "
                            "condition so lead scoring does not mistake a public technology signal for purchasing intent."
                        ),
                        (
                            "The first segment is independently operated "
                            "design firms with 75–250 paid collaboration "
                            "seats and a renewal inside 120 days. A "
                            "qualified opportunity needs an authorized "
                            "procurement contact, current invoice, comparable "
                            "product scope, and at least $2,000 projected "
                            "annual retained contribution before direct "
                            "delivery costs."
                        ),
                    ),
                    field(
                        "DNS, MX, and SPF signal boundaries",
                        "textarea",
                        (
                            "Specify the public signals collected, rate "
                            "limits, provenance, and permitted interpretation. "
                            "Explain which commercial facts those signals "
                            "cannot establish, and define the customer-confirmation "
                            "step before using them in a quote or savings estimate."
                        ),
                        (
                            "A rate-limited DNS lookup records MX and "
                            "SPF observations with collection dates. A "
                            "Microsoft-associated mail route suggests a "
                            "research hypothesis but proves neither paid "
                            "seat count nor renewal timing. The researcher "
                            "requests an authorized invoice before entering "
                            "120 seats or a September renewal into "
                            "the pricing engine."
                        ),
                    ),
                    field(
                        "Acquisition funnel and cohort conversion",
                        "textarea",
                        (
                            "State the funnel stages, observation window, "
                            "conversion assumptions, and qualification criteria. "
                            "Keep the denominator consistent and identify "
                            "which outcomes are measured versus modeled so a promising small sample is not presented as established performance."
                        ),
                        (
                            "A modeled monthly cohort contains 200 "
                            "researched accounts, 40 qualified conversations, "
                            "12 accepted audits, and four signed deals. "
                            "That implies 20%, 30%, and 33.3% successive "
                            "conversion rates. The tracker labels these "
                            "as planning assumptions until completed "
                            "cohorts supply actual outcomes and elapsed "
                            "sales-cycle evidence."
                        ),
                    ),
                    field(
                        "Acquisition cost and contribution payback",
                        "textarea",
                        (
                            "Calculate acquisition cost using the relevant "
                            "channel expense and signed-customer denominator. "
                            "Then compute payback from collected retained "
                            "contribution after direct service cost, not from subscription billings, estimated savings, or unpaid contingent fees."
                        ),
                        (
                            "A cohort costs $2,400 in outreach labor "
                            "and tools and signs four customers, giving "
                            "$600 acquisition cost per customer. Each "
                            "customer contributes $200 monthly retained "
                            "revenue less $50 direct service cost. "
                            "Monthly contribution is $150, producing "
                            "four-month simple payback before fixed "
                            "overhead and collection delays."
                        ),
                    ),
                    field(
                        "Distributor and master-agent integration map",
                        "textarea",
                        (
                            "List each provider, authorized account, "
                            "supported interface, imported objects, "
                            "write permissions, and reconciliation owner. "
                            "Distinguish CPOR, CSP, VIP, and commission workflows rather than assuming a common endpoint can execute all partner changes."
                        ),
                        (
                            "Pax8 order and billing records enter "
                            "through the brokerage's authorized interface; "
                            "Ingram records follow its supported account "
                            "export or API. Telarus commission statements "
                            "are reconciled separately. CPOR attribution "
                            "and Adobe VIP changes use their applicable "
                            "program workflows, with manual evidence "
                            "capture wherever the selected account "
                            "lacks automation support."
                        ),
                    ),
                    field(
                        "Benchmark floor and quote version control",
                        "textarea",
                        (
                            "Define the benchmark's comparable dimensions, "
                            "source permissions, age limit, supplier "
                            "floor, and minimum spread. Specify "
                            "how quote versions are invalidated when costs or entitlements change and prevent cross-customer confidential pricing from leaking."
                        ),
                        (
                            "Quote version 3 compares identical "
                            "edition, term, region, support, and "
                            "120-seat quantity. The supplier floor "
                            "is $18.40 per seat monthly and "
                            "the customer price is $20. A "
                            "new floor of $19 invalidates the "
                            "quote, reduces annual spread to "
                            "$1,440, and requires a fresh "
                            "underwriting decision."
                        ),
                    ),
                    field(
                        "Shared-savings audit engine controls",
                        "textarea",
                        (
                            "Specify baseline inputs, normalization rules, "
                            "fee percentage, rounding, customer verification, "
                            "and exception handling. Ensure the "
                            "engine isolates negotiation savings from quantity changes and reconciles overlapping rebates before generating an invoice."
                        ),
                        (
                            "The engine normalizes a $240,000 "
                            "baseline to unchanged seats and "
                            "features, then compares the signed "
                            "$200,000 renewal. Savings equal "
                            "$40,000 and a 30% fee equals "
                            "$12,000. A concurrent 10% seat "
                            "reduction routes the case to "
                            "manual recalculation instead of "
                            "inflating the negotiation claim."
                        ),
                    ),
                    field(
                        "Risk thresholds and fallback actions",
                        "textarea",
                        (
                            "Assign measurable triggers for spread "
                            "compression, overdue remittances, default "
                            "exposure, and tenant anomalies. "
                            "Document the person responsible, immediate containment action, required customer communication, and evidence needed to resume the affected workflow."
                        ),
                        (
                            "A wholesale spread below 6%, "
                            "a residual remittance thirty days "
                            "past its contractual due date, "
                            "or any cross-customer tenant "
                            "proposal creates an exception. "
                            "The operations owner stops "
                            "affected placements, reconciles "
                            "supplier evidence, and preserves "
                            "existing authorized services while "
                            "the deal owner resolves pricing "
                            "or collection exposure."
                        ),
                    ),
                    field(
                        "Secret storage, job access, and audit trail",
                        "textarea",
                        (
                            "Identify where integration secrets "
                            "are stored, which jobs can "
                            "retrieve them, and how access "
                            "is reviewed. Record rotation, redaction, and incident steps without placing credentials or customer-sensitive payloads in printable operational worksheets."
                        ),
                        (
                            "An encrypted secret manager holds "
                            "provider credentials; the nightly "
                            "billing importer receives read-only "
                            "access where supported. Production "
                            "logs record event identifiers "
                            "and status, not tokens or "
                            "full invoices. A quarterly "
                            "review removes inactive contractors, "
                            "and suspected exposure triggers "
                            "credential revocation, rotation, "
                            "and scoped access-history review."
                        ),
                    ),
                    field(
                        "Referral flywheel and manual recovery drill",
                        "textarea",
                        (
                            "Describe the permission-based referral "
                            "request, measured outcome, and "
                            "fallback drill supporting reliable "
                            "delivery. Identify what evidence can be shared externally and how operators reconcile manual work before automated processing resumes."
                        ),
                        (
                            "After the customer verifies "
                            "$28,000 net benefit, the "
                            "account owner requests permission "
                            "for an anonymized case study "
                            "and one referral introduction. "
                            "During a two-hour integration "
                            "outage drill, operators import "
                            "approved statements manually and "
                            "mark event keys; recovery "
                            "replays create zero duplicate "
                            "earnings or orders."
                        ),
                    ),
                ],
                "completion_gate": (
                    "The pipeline identifies evidence-backed opportunities, reports "
                    "contribution-based acquisition payback, and demonstrates one "
                    "successful manual recovery without duplicate orders. All "
                    "provider permissions, benchmark versions, suppression rules, "
                    "and risk fallback owners are recorded before production use."
                ),
            },
            {
                "worksheet_id": "ws-06",
                "number": 6,
                "title": "30-Day Launch Sprint, Pod KPI Scorecard & Exit-Readiness Ledger",
                "purpose": (
                    "Translate the model into a thirty-day evidence-building launch "
                    "and a repeatable small-team operating cadence. Assign "
                    "accountability, protect startup capital, measure retained "
                    "earnings and cash separately, and assemble transferable "
                    "contracts and records without treating projected revenue "
                    "as an achieved run rate."
                ),
                "chapter_ref": "Q11, Q12",
                "instructions": [
                    (
                        "Organize the first thirty days "
                        "around verified deliverables rather "
                        "than a promised close date. "
                        "The stated time to first "
                        "deal is one to three "
                        "months, so an unfinished sales "
                        "cycle at day thirty requires "
                        "evidence review, not invented revenue."
                    ),
                    (
                        "Assign one accountable owner to "
                        "each sales, procurement, operations, "
                        "accounting, and technical control. "
                        "Use contractors for bounded "
                        "work packages with documented "
                        "handoffs; preserve independent review "
                        "of high-exposure commitments even "
                        "when the full-time pod is small."
                    ),
                    (
                        "Set weekly targets for qualified "
                        "opportunities, verified savings, funded "
                        "orders, collected retained revenue, "
                        "renewal retention, and exception "
                        "age. Separate leading activity "
                        "indicators from earned revenue "
                        "and cash so pipeline optimism "
                        "cannot mask deteriorating economics."
                    ),
                    (
                        "Reconcile the pod dashboard to "
                        "the canonical scenarios and "
                        "current ledger every month. "
                        "Track headcount, contractor scope, "
                        "total costs, reserve sufficiency, "
                        "and concentration alongside margin; "
                        "a high percentage margin alone "
                        "does not establish a transferable business."
                    ),
                    (
                        "Build the exit-readiness record "
                        "from executed agreements and "
                        "reconciled evidence throughout launch. "
                        "Verify assignment rights, residual "
                        "survival, customer permissions, and "
                        "supplier relationships before treating "
                        "recurring commissions as transferable "
                        "assets in a buyer discussion."
                    ),
                ],
                "fields": [
                    field(
                        "Days 1–7 authority and evidence sprint",
                        "textarea",
                        (
                            "Define the first week's completed "
                            "deliverables, named roles, budget, "
                            "and acceptance evidence. Prioritize "
                            "authorized distribution access, customer engagement documents, ledger structure, and sourcing criteria before committing spending to broad acquisition."
                        ),
                        (
                            "The full-time operator confirms "
                            "one authorized supplier route "
                            "and signs off the engagement "
                            "template. The accounting contractor "
                            "documents the revenue policy; "
                            "the systems contractor creates "
                            "the event ledger. Week-one "
                            "spending is capped at $2,000, "
                            "and ten candidate accounts "
                            "receive evidence-based research "
                            "records rather than automated quotes."
                        ),
                    ),
                    field(
                        "Days 8–14 discovery and audit sprint",
                        "textarea",
                        (
                            "Set discovery and audit targets "
                            "with specific evidence requirements, "
                            "outreach permissions, and reviewer "
                            "capacity. Define what makes an audit accepted and prevent incomplete invoices or unverified renewal dates from entering the qualified pipeline."
                        ),
                        (
                            "The operator targets ten "
                            "qualified conversations and three "
                            "accepted audits during week "
                            "two. Each accepted audit "
                            "requires written customer authority, "
                            "a current invoice, comparable "
                            "SKU details, and a renewal "
                            "date. The procurement contractor "
                            "reviews all three baselines "
                            "before any savings percentage "
                            "is shared."
                        ),
                    ),
                    field(
                        "Days 15–21 quote and execution rehearsal",
                        "textarea",
                        (
                            "Specify reviewed proposal outputs, "
                            "funding requirements, supplier checks, "
                            "and failure simulations for "
                            "week three. State which actions use test records and which require a real signed customer order and cleared payment."
                        ),
                        (
                            "Two reviewed proposals show "
                            "baseline, supplier floor, retained "
                            "spread, and customer benefit. "
                            "The systems contractor rehearses "
                            "duplicate-event and timeout handling "
                            "with test records. No live "
                            "annual subscription is placed "
                            "without an executed order "
                            "and cleared prefunding, even "
                            "if the prospect verbally "
                            "accepts the quotation."
                        ),
                    ),
                    field(
                        "Days 22–30 launch review and cash decision",
                        "textarea",
                        (
                            "Define the final launch review, "
                            "evidence packet, remaining cash "
                            "test, and next-month decision. "
                            "Distinguish a signed engagement, funded placement, earned fee, and collected revenue so unfinished work is reported at its actual stage."
                        ),
                        (
                            "Day thirty shows three "
                            "accepted audits, two issued "
                            "quotes, and one signed "
                            "engagement awaiting prefunding. "
                            "Recognized and collected revenue "
                            "remain $0. With $18,000 "
                            "unrestricted cash after $7,000 "
                            "launch spending, the operator "
                            "continues the one-to-three-month "
                            "sales cycle and schedules "
                            "weekly funding reviews."
                        ),
                    ),
                    field(
                        "Pod roles, capacity, and review coverage",
                        "textarea",
                        (
                            "Map the canonical staffing "
                            "structure to concrete responsibilities "
                            "and weekly capacity. Identify "
                            "the independent reviewer for commitments and accounting exceptions, and define the capacity signal that justifies adding the second full-time operator."
                        ),
                        (
                            "The Base pod has one "
                            "full-time commercial operator and "
                            "three contractors covering procurement, "
                            "accounting, and systems. Each "
                            "contractor receives a bounded "
                            "work queue and named "
                            "handoff. The Scaled design "
                            "adds a full-time operations "
                            "lead and a fourth contractor, "
                            "creating the required six-person "
                            "team without removing independent "
                            "commitment review."
                        ),
                    ),
                    field(
                        "Weekly KPI definitions and denominators",
                        "textarea",
                        (
                            "Define each KPI's numerator, "
                            "denominator, measurement window, "
                            "data source, and owner. "
                            "Include customer concentration, renewal retention, exception age, and contribution-based acquisition payback alongside sales activity and collected retained revenue."
                        ),
                        (
                            "The dashboard reports four "
                            "signed deals from twelve "
                            "accepted audits, or 33.3% "
                            "audit conversion. Thirty-eight "
                            "of forty eligible renewals "
                            "retain service, or 95% "
                            "logo retention. Largest-customer "
                            "share is $60,000 divided "
                            "by $500,000 retained revenue, "
                            "or 12%; any exception "
                            "older than two business "
                            "days receives an owner review."
                        ),
                    ),
                    field(
                        "Canonical scorecard and scale decision",
                        "textarea",
                        (
                            "Record the volume rank, "
                            "Money-to-Manpower score, component "
                            "scores, and scenario targets. "
                            "Explain which operating evidence supports expansion without treating the editorial score or a projected annualized month as proof of achieved profit."
                        ),
                        (
                            "Volume 037 is pipeline "
                            "rank #04 of 37 with "
                            "a 94/100 score: revenue "
                            "24, margin 24, team "
                            "efficiency 19, accessibility "
                            "14, and automation 13. "
                            "Annual owner profit targets "
                            "remain $32,000 Conservative, "
                            "$225,000 Base, and $522,000 "
                            "Scaled. Expansion requires "
                            "reconciled collections, supported "
                            "capacity, and funded commitment "
                            "exposure."
                        ),
                    ),
                    field(
                        "Concentration and recurring earnings quality",
                        "textarea",
                        (
                            "Measure customer, supplier, and "
                            "program concentration using retained "
                            "revenue rather than customer "
                            "subscription spend. Separate durable recurring earnings from contingent audit fees and identify the largest contractual or rebate dependency requiring mitigation."
                        ),
                        (
                            "In the Base illustration, "
                            "$200,000 spread plus $120,000 "
                            "residuals represents $320,000, "
                            "or 64% of operator "
                            "revenue, before assessing "
                            "contract durability. GPO "
                            "rebates contribute 16% and "
                            "audit fees 20%. If "
                            "one supplier supports all "
                            "wholesale spread, that "
                            "supplier represents 40% "
                            "of operator revenue and "
                            "requires explicit compression monitoring."
                        ),
                    ),
                    field(
                        "Exit-readiness contracts and evidence ledger",
                        "textarea",
                        (
                            "List the records needed "
                            "to verify earnings quality, "
                            "customer authority, residual "
                            "ownership, and transfer restrictions. Assign a custodian and refresh interval, and specify which materials require customer permission before external buyer access."
                        ),
                        (
                            "The monthly record set "
                            "includes reconciled revenue "
                            "schedules, supplier statements, "
                            "customer contracts, rebate "
                            "calculations, and twelve-month "
                            "renewal cohorts. Each master-agent "
                            "agreement has an assignment "
                            "and residual-survival summary. "
                            "Buyer access uses redacted "
                            "copies under authorized "
                            "sharing arrangements; customer "
                            "tenant credentials never "
                            "enter the diligence room."
                        ),
                    ),
                    field(
                        "Stop, repair, expand, and handoff decision",
                        "textarea",
                        (
                            "Write a measurable operating "
                            "decision with the accountable "
                            "owner, supporting evidence, "
                            "review date, and required corrective actions. Include a handoff test proving another authorized operator can reconcile a deal without relying on undocumented founder knowledge."
                        ),
                        (
                            "Continue the pilot while "
                            "unrestricted cash exceeds "
                            "the $12,000 reserve and "
                            "all annual orders remain "
                            "fully funded. Repair any "
                            "unmatched supplier statement "
                            "before expansion. An authorized "
                            "backup operator must reconstruct "
                            "D037-001 from contract through "
                            "the $2,304 retained-fee "
                            "schedule within sixty minutes "
                            "using documented records alone."
                        ),
                    ),
                ],
                "completion_gate": (
                    "The operator signs the thirty-day review with actual stage "
                    "counts, cash balances, unresolved issues, and the next "
                    "decision date. Scenario targets reconcile exactly, the "
                    "pod has named review coverage, and an authorized backup "
                    "successfully reconstructs one complete deal from preserved evidence."
                ),
            },
        ],
    }
