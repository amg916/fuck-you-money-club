from __future__ import annotations


def build_volume_044_workbook() -> dict:
    def field(name: str, input_type: str, prompt: str, example: str) -> dict:
        return {
            "name": name,
            "type": input_type,
            "prompt": prompt,
            "example": example,
        }

    return {
        "workbook_id": "wb-044-customs-duty-drawback-and-tariff-refund-recovery",
        "volume_id": "vol-044-customs-duty-drawback-and-tariff-refund-recovery",
        "title": "Customs Duty Drawback, Tariff Refund & Antitrust Claim Recovery — Operator Companion Workbook",
        "subtitle": (
            "6 Printable Operator Worksheets for Three-Lane Recovery Underwriting, "
            "Contingency Economics, Customs Filing Controls, Settlement Claim Evidence, "
            "Automation Resilience, and Small-Team Launch Execution"
        ),
        "worksheets": [
            {
                "worksheet_id": "ws-01",
                "number": 1,
                "title": "Arbitrage Deal / Counterparty Underwriting & Spread Qualification",
                "purpose": (
                    "Qualify recovery opportunities before purchasing records or committing specialist hours. "
                    "Separate drawback, tariff correction or protest, and settled antitrust claims into "
                    "independent eligibility decisions, then establish claimant authority, collectible amounts, "
                    "evidence quality, fee economics, and a documented reason to proceed."
                ),
                "chapter_ref": "Q1, Q2, Q6",
                "instructions": [
                    (
                        "Open one opportunity record per claimant, recovery lane, and underlying claim population. "
                        "Use manifest intelligence only for prospecting, obtain claimant-authorized source records, "
                        "and name the person responsible for confirming ownership before estimating any collectible recovery."
                    ),
                    (
                        "Have the licensed customs broker or trade counsel classify the customs route before "
                        "quoting fees. Distinguish unused merchandise drawback from entry correction and protest; "
                        "a matching tariff number alone never establishes a valid claim."
                    ),
                    (
                        "For settlement opportunities, read the operative class definition, allocation plan, "
                        "administrator instructions, and court orders. Record the actual claims deadline and "
                        "distribution conditions rather than treating an announced settlement fund as immediately collectible money."
                    ),
                    (
                        "Price each lane against its own documentation burden, specialist charges, bond exposure, "
                        "and payment delay. Quote contingency fees only on contractually defined realized recovery, "
                        "and exclude importer principal, merchant sales, and settlement pool size from operator revenue."
                    ),
                    (
                        "Resolve duplicate representation, missing export evidence, adverse duty treatment, and "
                        "deadline uncertainty before accepting the engagement. Preserve rejected opportunities with "
                        "specific reasons so acquisition automation cannot repeatedly revive an economically or legally defective claim population."
                    ),
                ],
                "fields": [
                    field(
                        "Claimant identity and recovery ownership",
                        "textarea",
                        "Identify the legal claimant, operating entities, importer identifiers, signing authority, "
                        "and any transfer affecting recovery rights. Explain how documentary ownership will be "
                        "established independently of the prospecting database or salesperson's representation.",
                        "Example: Harbor Components LLC supplies its W-9, importer number, corporate resolution, "
                        "and acquisition agreement. The agreement retained pre-closing customs refunds with the seller, "
                        "so the first engagement covers only post-closing imports. The chief operating officer signs "
                        "for the LLC; a separate seller authorization would be required before pursuing the older "
                        "entry population or quoting fees against it.",
                    ),
                    field(
                        "Three-lane opportunity segmentation",
                        "textarea",
                        "Split the opportunity into drawback, tariff correction or protest, and settled antitrust "
                        "recovery. Assign separate claim populations, evidence packages, expected amounts, and accountable "
                        "specialists so one lane cannot borrow another lane's eligibility.",
                        "Example: Case HC-044 contains $100,000 of potentially eligible drawback duties, a separate "
                        "$40,000 classification overpayment, and an illustrative $20,000 settlement distribution estimate. "
                        "The same $40,000 duty component is excluded from the drawback population. A licensed broker "
                        "owns customs analysis, while a settlement specialist checks the court-approved claim process. "
                        "Three child records retain distinct deadlines and recovery calculations.",
                    ),
                    field(
                        "Drawback statutory eligibility screen",
                        "textarea",
                        "Document the applicable 19 U.S.C. § 1313 provision, import and export dates, merchandise "
                        "condition, duty components, and tracing method. Have the broker identify exclusions and "
                        "substitution restrictions before accepting the proposed collectible base.",
                        "Example: The broker screens unused merchandise under § 1313(j)(1), linking imported parts "
                        "to actual exported units through serial numbers and warehouse movements. From $112,000 "
                        "of paid duties, $12,000 of antidumping duties is excluded under § 1313(v). "
                        "The remaining $100,000 supports a preliminary $99,000 recovery at 99%, subject to "
                        "complete evidence, timely filing, and any additional applicable restrictions.",
                    ),
                    field(
                        "Tariff correction and protest route",
                        "textarea",
                        "Identify the entry decision being corrected, liquidation status, available administrative "
                        "route, and controlling deadline. Distinguish an ACE Post-Summary Correction from a protest "
                        "under 19 U.S.C. § 1514 and document the broker's route selection.",
                        "Example: An entry accepted January 15 has a classification error supported by a technical "
                        "datasheet and invoice. The broker checks current ACE eligibility, the general 300-day PSC "
                        "limit, and the requirement to precede scheduled liquidation by at least 15 days. "
                        "If liquidation has occurred, counsel separately evaluates a protest within 180 days of "
                        "the relevant protestable decision; PSC timing is not extended by that period.",
                    ),
                    field(
                        "Settlement class and collectible distribution",
                        "textarea",
                        "Record the exact settlement class, covered purchase period, exclusions, allocation formula, "
                        "and administrator evidence rules. Distinguish qualifying purchases from projected distributions "
                        "and identify any unresolved condition preventing a reliable cash estimate.",
                        "Example: An illustrative court-approved industrial-components settlement covers direct purchases "
                        "during its defined six-year period. Harbor documents $2,000,000 of qualifying purchases, "
                        "but the allocation model supports only a provisional $20,000 distribution. The specialist "
                        "checks affiliate exclusions, releases, and previous claim submissions. Purchase volume remains "
                        "an allocation input; neither that volume nor the entire settlement fund becomes operator revenue.",
                    ),
                    field(
                        "Evidence coverage and acquisition cost",
                        "textarea",
                        "Inventory the records already available and price the work needed to close material gaps. "
                        "Assign coverage percentages to claim value rather than document counts, and identify which "
                        "missing evidence would defeat recovery entirely.",
                        "Example: ACE entry summaries cover 100% of proposed import duties, while export BOL, "
                        "AES references where required, and warehouse records support 82% of proposed drawback value. "
                        "Recovering archived shipment records costs $1,400 within a $3,600 documentation budget. "
                        "The unsupported 18% stays outside the filing population until the broker accepts tracing "
                        "evidence; ten extra invoices cannot substitute for missing export proof.",
                    ),
                    field(
                        "Contingency rate and earned fee trigger",
                        "textarea",
                        "Specify the fee rate, cash receipt trigger, treatment of partial recoveries, and allocation "
                        "of reversals. Identify who invoices the claimant and whether external specialist costs are "
                        "operator expenses or separately authorized client charges.",
                        "Example: Drawback carries a 30% contingency on realized eligible refunds, tariff correction "
                        "carries 25%, and settlement recovery carries 30%. A $99,000 drawback receipt earns a "
                        "$29,700 fee under the example agreement. An approved but unpaid claim earns no invoice "
                        "under this contract. Broker and documentation charges are operator expenses already included "
                        "in underwriting, rather than surprise deductions from the claimant's retained recovery.",
                    ),
                    field(
                        "Counterparty and specialist diligence",
                        "textarea",
                        "Assess claimant responsiveness, broker credentials, counsel scope, administrator authenticity, "
                        "and payment instructions. Capture independently verified contact channels and conflicts, "
                        "including any existing representative claiming fees on the same underlying recovery rights.",
                        "Example: The operations lead verifies the broker's license and permit status through "
                        "official records, confirms the engagement directly, and receives professional coverage details. "
                        "Harbor identifies an incumbent broker but no existing drawback engagement. The settlement "
                        "portal is reached from the court-authorized administrator website, not an emailed payment "
                        "link. Any bank-account change requires a callback using a previously verified telephone number.",
                    ),
                    field(
                        "Lane-specific timing and bond exposure",
                        "textarea",
                        "Estimate evidence preparation, submission, review, and payment intervals separately for each "
                        "lane. State whether accelerated drawback payment is requested, what surety security is "
                        "required, and which assumptions could materially lengthen cash conversion.",
                        "Example: Budget 30–90 days for drawback evidence assembly and an illustrative 6–18 months "
                        "for payment without acceleration. A broker-approved accelerated-payment route might shorten "
                        "post-acceptance timing to 60–120 days, but requires authorization and adequate bond capacity. "
                        "Tariff refunds use a 3–12-plus-month planning range without assuming a drawback bond. "
                        "Settlement distributions use 6–24-plus months and no CBP bond.",
                    ),
                    field(
                        "Underwriting decision and rejection reason",
                        "textarea",
                        "Record the accepted claim ceiling, expected fee, direct costs, evidence conditions, and "
                        "named reviewer. Explain why the opportunity exceeds the required contribution threshold "
                        "without relying on accelerated payment or unsupported settlement estimates.",
                        "Example: Accept the documented $100,000 drawback duty base for further broker review, "
                        "supporting a preliminary $99,000 refund and $29,700 operator fee. Budget $7,900 direct "
                        "costs, leaving $21,800 before fixed overhead. Hold the separate tariff and settlement "
                        "opportunities pending their own eligibility decisions. Reject any additional duties whose "
                        "statutory treatment or export tracing remains unresolved rather than inflating the sales pipeline.",
                    ),
                ],
                "completion_gate": (
                    "The operator and responsible specialist sign three separate eligibility decisions, "
                    "reconcile all overlapping duty components, verify claimant authority, and approve only "
                    "documented collectible bases with explicit cost and timing assumptions."
                ),
            },
            {
                "worksheet_id": "ws-02",
                "number": 2,
                "title": "Unit Economics, Escrow/Reserve Float & Working-Capital Calculator",
                "purpose": (
                    "Translate recoveries into earned contingency revenue without counting claimant principal. "
                    "Reconcile deal-level costs, operating reserves, payment timing, and surety collateral with "
                    "the canonical annual scorecard, while distinguishing unrestricted operator cash from "
                    "restricted funds, receivables, and refundable client money."
                ),
                "chapter_ref": "Q3, Q4",
                "instructions": [
                    (
                        "Calculate each lane independently using realized recovery multiplied by its contracted "
                        "contingency rate. Show eligible duties, correction refunds, and settlement distributions "
                        "as claimant amounts; never combine underlying purchases or refund principal with earned operator revenue."
                    ),
                    (
                        "Separate direct claim expenses, fixed overhead, reserve transfers, and surety collateral. "
                        "A cash reserve reduces immediately deployable liquidity but does not automatically create "
                        "an expense, while collateral remains restricted until the surety contract permits release."
                    ),
                    (
                        "Use the canonical Conservative, Base, and Scaled annual figures exactly. Reconcile "
                        "annual expense totals to those figures, explaining how quoted monthly operating overhead "
                        "differs from variable broker, documentation, contractor, and acquisition costs included in total expenses."
                    ),
                    (
                        "Build a monthly cash schedule from actual expected collection dates rather than signed "
                        "contract value. Stress delayed customs payment and delayed settlement distributions together, "
                        "then identify the maximum funding deficit before paying owner distributions or expanding acquisition."
                    ),
                    (
                        "Send claimant recoveries directly to the authorized claimant account wherever the payment "
                        "process permits. If an actual escrow arrangement is required, document the independent "
                        "custodian, permitted disbursements, and reconciliation controls instead of treating client money as float."
                    ),
                ],
                "fields": [
                    field(
                        "Drawback deal contribution calculation",
                        "textarea",
                        "Calculate eligible paid duties, statutory recovery percentage, realized refund, contracted "
                        "fee, direct costs, and pre-overhead contribution. Explain every deduction and keep the "
                        "claimant's retained recovery separate from the operator's fee revenue.",
                        "Example: $100,000 eligible duties × 99% produces a $99,000 realized refund. At 30%, "
                        "operator revenue is $29,700 and the claimant retains $69,300 before its own expenses. "
                        "Documentation costs $3,600, broker services $2,200, illustrative bond premium $1,200, "
                        "and acquisition $900. Total direct cost is $7,900; contribution is $21,800 before "
                        "fixed overhead. The premium is a quote assumption, not a statutory price.",
                    ),
                    field(
                        "Tariff refund deal contribution calculation",
                        "textarea",
                        "Calculate the overpayment actually recovered through the selected correction or protest "
                        "route, the contingency fee, specialist costs, and contribution. Do not apply drawback's "
                        "99% convention or accelerated-payment bond assumptions to this lane.",
                        "Example: A supported classification correction produces a $40,000 refund, excluding interest "
                        "from the contracted fee base. The 25% fee equals $10,000; Harbor retains $30,000. "
                        "Broker or counsel work costs $1,800, records preparation $900, and acquisition $600. "
                        "Direct cost totals $3,300, leaving $6,700 before fixed overhead. No separate accelerated "
                        "drawback bond is budgeted merely because the payment originates with CBP.",
                    ),
                    field(
                        "Settlement recovery deal contribution calculation",
                        "textarea",
                        "Use the claimant's actual settlement distribution rather than qualifying purchases or "
                        "the advertised pool. Calculate the earned contingency, claim preparation cost, specialist "
                        "expense, and contribution while identifying allocation or timing uncertainty.",
                        "Example: A $20,000 realized distribution on $2,000,000 of qualifying purchases generates "
                        "$6,000 revenue at 30%; the claimant retains $14,000. Documentation costs $800, "
                        "specialist review $500, and acquisition $300. The $1,600 direct cost leaves $4,400 "
                        "before fixed overhead. A preliminary administrator estimate remains a forecast until paid "
                        "under this contract, and this lane carries no CBP surety-bond requirement.",
                    ),
                    field(
                        "Reserve policy and distributable cash",
                        "textarea",
                        "Define fee-funded reserves for corrections, reversals, and servicing obligations. Show "
                        "reserve balances separately from expenses and claimant funds, then calculate deployable "
                        "cash after actual costs and reserve transfers for each worked deal.",
                        "Example: Reserve 15% of the $29,700 drawback fee, or $4,455, leaving $17,345 "
                        "after $7,900 direct costs. Reserve 10% of the $10,000 tariff fee, leaving $5,700 "
                        "after $3,300 costs. Reserve 10% of the $6,000 settlement fee, leaving $3,800 "
                        "after $1,600 costs. Combined contribution is $32,900; combined reserves are $6,055 "
                        "and deployable cash is $26,845 before overhead.",
                    ),
                    field(
                        "Conservative annual scorecard bridge",
                        "textarea",
                        "Reproduce the Conservative Formula v2.0 outcome and supply a lane mix that exactly "
                        "reconciles earned revenue. Calculate total expenses and explain the staffing notation "
                        "without converting contractor engagements into additional full-time employees.",
                        "Example: Drawback recoveries of $200,000 at 30% yield $60,000; tariff refunds of "
                        "$80,000 at 25% yield $20,000; settlement distributions of $100,000 at 30% yield "
                        "$30,000. Revenue totals $110,000. Expenses are $74,800, leaving $35,200 annual "
                        "owner net profit at 32%. Staffing is 1 FT + 3 C: one full-time operator "
                        "with three contracted specialists, not four full-time salaries.",
                    ),
                    field(
                        "Base annual scorecard bridge",
                        "textarea",
                        "Reproduce the Base Formula v2.0 outcome with an exact lane-level fee bridge. "
                        "Distinguish annual total expenses from recurring overhead and retain the canonical "
                        "profit amount, margin, and staffing configuration without rounding away differences.",
                        "Example: $900,000 drawback recoveries at 30% produce $270,000; $500,000 tariff refunds "
                        "at 25% produce $125,000; $400,000 settlement distributions at 30% produce $120,000. "
                        "The $1,800,000 claimant recovery base generates $515,000 revenue. Expenses of $283,250 "
                        "leave $231,750 owner net profit at 45.0%. One illustrative cost split is $60,000 "
                        "annual fixed overhead plus $223,250 variable delivery costs, using 1 FT + 3 C.",
                    ),
                    field(
                        "Scaled annual scorecard bridge",
                        "textarea",
                        "Reproduce the Scaled Small-Team Formula v2.0 outcome and reconcile lane recoveries, "
                        "fee revenue, expenses, and owner profit. State the six-person team composition and "
                        "avoid representing the increased margin as automatic.",
                        "Example: $1,600,000 drawback recoveries at 30% yield $480,000; $800,000 tariff refunds "
                        "at 25% yield $200,000; $800,000 settlement distributions at 30% yield $240,000. "
                        "Revenue totals $920,000, expenses total $386,400, and annual owner net profit is "
                        "$533,600 at 58%. Staffing is 2 FT + 4 C, six people. Achieving that "
                        "cost structure requires documented throughput and fewer manual rework hours.",
                    ),
                    field(
                        "Working-capital runway and collection stress",
                        "textarea",
                        "Schedule startup spending, monthly fixed overhead, claim-specific outlays, and fee collections "
                        "by month. Calculate the lowest unrestricted cash balance under delayed payment, "
                        "excluding reserve cash, claimant money, and undrawn financing from available liquidity.",
                        "Example: Start with $35,000, spend $8,000 on setup, and pay $3,000 monthly fixed "
                        "overhead for four months. One drawback, tariff, and settlement package consume $12,800 "
                        "combined direct costs. Before any collections, unrestricted cash falls to $2,200. "
                        "Two more months without receipts create a $3,800 deficit. Pause new paid preparation "
                        "and arrange committed funding before that deficit, rather than borrowing against claimant refunds.",
                    ),
                    field(
                        "Surety collateral and escrow segregation",
                        "textarea",
                        "Document the actual bond quote, premium, collateral requirement, release conditions, and "
                        "custodian of any restricted funds. Separate ordinary import bonds from accelerated "
                        "drawback security and describe how client receipts avoid the operating account.",
                        "Example: A surety quotes $1,200 annual premium and $10,000 cash collateral for the "
                        "illustrative accelerated drawback arrangement, subject to underwriting. The premium is already "
                        "included in direct costs; collateral is additional restricted liquidity, not another expense. "
                        "Adding collateral to the previous runway example deepens the pre-collection shortfall to "
                        "$7,800. Refunds go to Harbor directly; this engagement creates no operator-controlled client escrow.",
                    ),
                    field(
                        "Revenue recognition and retained-share reconciliation",
                        "textarea",
                        "Define the accounting unit, earned fee trigger, principal-versus-agent assessment, and "
                        "treatment of subcontractors. If a partner retains part of a fee, reconcile "
                        "recognized operator revenue explicitly instead of silently changing canonical revenue definitions.",
                        "Example: In these scenarios the contracted recovery service earns the full stated fee "
                        "and pays broker subcontractors as expenses; no additional retained-share factor reduces "
                        "$515,000 Base revenue. The accountant documents the ASC 606 assessment, including "
                        "variable consideration. If a different arrangement makes the operator an agent entitled "
                        "to 70% of a $10,000 service fee, operator revenue is $7,000, requiring a "
                        "separate bridge rather than reuse of the canonical totals.",
                    ),
                ],
                "completion_gate": (
                    "All three annual scenarios reconcile exactly; deal contribution, reserve transfers, "
                    "restricted collateral, and claimant principal occupy separate ledger categories. "
                    "The operator approves a funded cash plan that survives the documented collection delay."
                ),
            },
            {
                "worksheet_id": "ws-03",
                "number": 3,
                "title": "End-to-End Execution, Idempotent Ledger & QA Pre-Flight Sheet",
                "purpose": (
                    "Build a reproducible claim production system from authorized intake through final receipt. "
                    "Use immutable source evidence, component-level recovery allocation, specialist review, "
                    "idempotent submission controls, and cash reconciliation to prevent duplicate claims, "
                    "unsupported tariff matches, missed deadlines, and premature contingency invoices."
                ),
                "chapter_ref": "Q7, Q8",
                "instructions": [
                    (
                        "Create a claim identifier before collecting documents, then attach every source file "
                        "to its authorized claimant and recovery lane. Store original files unchanged, record "
                        "checksums, and use versioned derived records for extraction, normalization, and corrections."
                    ),
                    (
                        "Reconcile merchandise quantity, duty components, and ownership before creating a draft "
                        "drawback claim. Route substitution questions to the broker; an automated eight-digit "
                        "HTS match is only a candidate link and cannot replace the applicable statutory tests."
                    ),
                    (
                        "Check liquidation events, correction windows, protest deadlines, and settlement deadlines "
                        "against authoritative records. Maintain independent calendar verification and assign a backup "
                        "owner so missing email or a stalled data feed cannot silently expire a claim."
                    ),
                    (
                        "Transmit formal customs filings only through the engaged licensed broker or trade "
                        "counsel under the required authority. Preserve submission payloads, acknowledgments, rejection "
                        "messages, and accepted revisions before changing any ledger status to submitted or accepted."
                    ),
                    (
                        "Reconcile actual recovery receipts before invoicing the contingency fee under the engagement. "
                        "Match reversals to the original claim and fee, retain the complete audit chain, "
                        "and test duplicate suppression with a repeated source file and repeated payment notification."
                    ),
                ],
                "fields": [
                    field(
                        "Claim state machine and responsible owner",
                        "textarea",
                        "Define allowed claim states, required evidence for each transition, and the person "
                        "authorized to change status. Separate internal preparation from external acceptance, "
                        "payment, fee collection, and final archival so progress metrics remain truthful.",
                        "Example: HC-044-D moves through authorized, evidence complete, specialist reviewed, submitted, "
                        "acknowledged, paid, fee collected, and archived. The analyst can complete evidence preparation "
                        "but cannot mark a CBP filing accepted. The broker supplies the acknowledgment identifier. "
                        "A rejected transmission returns to correction required with its error message preserved; "
                        "it does not count toward submitted production or expected collected revenue.",
                    ),
                    field(
                        "Source manifest and evidence custody",
                        "textarea",
                        "List required source systems, export permissions, file formats, checksums, and retention "
                        "owners. Explain how originals remain distinguishable from cleaned spreadsheets and how "
                        "a reviewer can reproduce every material amount from retained evidence.",
                        "Example: The manifest records ACE Form 7501 exports, commercial invoices, warehouse movement "
                        "files, export BOL, and applicable AES records. Each original receives a SHA-256 checksum "
                        "and read-only object version. The analyst's normalized CSV records the source filename "
                        "and row reference for each amount. A corrected invoice becomes a new version with "
                        "an explanation; the earlier invoice remains available for audit reconstruction.",
                    ),
                    field(
                        "Drawback matching and substitution review",
                        "textarea",
                        "Describe the matching keys, quantity controls, condition evidence, and treatment of "
                        "substitution candidates. Identify limitations under 19 U.S.C. § 1313(j)(2), "
                        "including classification restrictions and any applicable lesser-of calculation.",
                        "Example: The matcher proposes links using importer, eight-digit HTS, quantity, date, and "
                        "SKU mappings. The broker rejects a substitution candidate where the applicable classification "
                        "restriction prevents the proposed treatment. Another candidate requires review of the "
                        "lesser-of amount before valuation. Neither receives the automatic $99,000 example refund; "
                        "only individually validated duty components enter the claim calculation and export allocation ledger.",
                    ),
                    field(
                        "Component-level anti-duplication allocation",
                        "textarea",
                        "Specify how each entry line, duty component, quantity, and export allocation is "
                        "reserved against competing recoveries. Explain how corrections, partial refunds, and "
                        "amendments update eligibility without allowing the same overpayment to be collected twice.",
                        "Example: Entry line E100-03 has $10,000 ordinary duty and a proposed $2,000 "
                        "classification reduction. The tariff case reserves the disputed $2,000 component. The "
                        "drawback calculation uses only the broker-approved remaining eligible amount after considering "
                        "the correction's effect. When the $2,000 refund posts, an allocation event updates "
                        "the line basis and triggers specialist review of every related draft or existing claim.",
                    ),
                    field(
                        "Deadline engine and independent verification",
                        "textarea",
                        "Record the event that starts each statutory or administrative clock, the calculated "
                        "deadline, and the authoritative source. Include escalation intervals and distinguish "
                        "ordinary liquidation, extension, suspension, and potential deemed-liquidation issues.",
                        "Example: The calendar stores actual import dates for drawback and separately checks "
                        "export timing and complete-claim filing under § 1313. Protest reminders use the "
                        "verified protestable decision date and § 1514's applicable 180-day period. The broker "
                        "reviews 19 U.S.C. § 1504 events instead of assuming an unchanged liquidation schedule. "
                        "Settlement reminders use the operative court order, with 30-, 14-, and 3-day escalations.",
                    ),
                    field(
                        "Idempotency key and revision protocol",
                        "textarea",
                        "Define stable identifiers for claim creation, submission attempts, revisions, and payments. "
                        "Explain the database uniqueness rule and reconciliation process that prevent retries "
                        "from creating duplicate external claims or duplicate internal fee invoices.",
                        "Example: The internal key combines claimant ID, lane, claim population hash, and revision "
                        "number. A database uniqueness constraint blocks duplicate accepted creation requests. Transmission "
                        "attempts have separate IDs, while the broker's external reference links all acknowledgments. "
                        "A timeout first triggers status reconciliation with the filing channel; it never "
                        "automatically generates a new claim. A revision preserves its predecessor and changed-component list.",
                    ),
                    field(
                        "Settlement claim package and submission receipt",
                        "textarea",
                        "Document the purchase-ledger transformation, class-period filters, exclusion checks, filer "
                        "disclosures, claimant certification, and submission evidence. Identify which statements "
                        "require claimant confirmation rather than inference from imported accounts-payable records.",
                        "Example: The settlement package filters $2,300,000 total vendor purchases to $2,000,000 "
                        "within the defined products and class period, excluding $300,000 of unrelated purchases. "
                        "The claimant confirms affiliate status and prior submissions. The packet includes the "
                        "required third-party filer disclosure and direct-filing information. An administrator receipt, "
                        "timestamp, and payload checksum are stored before the claim is marked submitted.",
                    ),
                    field(
                        "QA exception thresholds and pre-flight sample",
                        "textarea",
                        "Specify the exact checks required before submission, including monetary reconciliation, "
                        "date logic, documentary coverage, signatures, and duplicate detection. Separate "
                        "blocking defects from reviewable extraction exceptions and name the final reviewer.",
                        "Example: All claimed dollars require accepted source support, all authorizations must be "
                        "current, and allocated quantities cannot exceed documented imports or exports. Any one-cent "
                        "unexplained reconciliation difference blocks release until resolved or documented as an "
                        "approved rounding rule. The broker checks every material eligibility exception and a "
                        "risk-based sample of otherwise clean lines; sampling never excuses missing evidence "
                        "for the remaining claimed population.",
                    ),
                    field(
                        "Receipt, invoice, and reversal reconciliation",
                        "textarea",
                        "Map payment evidence to the claim, earned fee invoice, bank settlement, and reserve "
                        "entry. Define how partial recoveries and later clawbacks affect the claimant balance, "
                        "operator revenue, and servicing obligations without erasing original records.",
                        "Example: CBP pays $49,500 against half the approved example recovery. Harbor supplies "
                        "the receipt, and the operator invoices $14,850 at 30%, not the full $29,700 "
                        "forecast. A later $5,000 recovery reversal triggers a linked $1,500 fee adjustment "
                        "under the contract's reversal clause. The original receipt remains unchanged; offsetting "
                        "events preserve the sequence and identify whether a refund or credit was issued.",
                    ),
                    field(
                        "Audit replay and closure package",
                        "textarea",
                        "Define the archive contents and demonstrate that a reviewer can reconstruct eligibility, "
                        "amounts, submissions, payments, and fee calculations without the original analyst. "
                        "Include retention dates, access restrictions, and unresolved post-payment obligations.",
                        "Example: The closure package contains engagement authority, broker POA confirmation, original "
                        "evidence, calculation versions, specialist decisions, submission receipts, payment records, and "
                        "fee invoices. A second analyst rebuilds the $99,000 recovery and $29,700 fee from "
                        "the archive. Retention follows 19 CFR Part 190 and other applicable requirements, "
                        "including holds. A paid claim remains open for identified audit or reversal obligations "
                        "until the responsible specialist clears closure.",
                    ),
                ],
                "completion_gate": (
                    "A reviewer reproduces one claim per lane from source evidence, verifies every "
                    "deadline, and demonstrates that duplicate files, submission retries, and repeated "
                    "payment events cannot create additional claims or fee invoices."
                ),
            },
            {
                "worksheet_id": "ws-04",
                "number": 4,
                "title": "Statutory, Licensing, Contract Addendum & Compliance Audit",
                "purpose": (
                    "Convert statutory restrictions and engagement terms into operational evidence requirements. "
                    "Establish authorized customs representation, defensible drawback and protest routes, "
                    "court-specific settlement disclosures, record retention, and clear contingency mechanics "
                    "before the team handles sensitive records or initiates formal submissions."
                ),
                "chapter_ref": "Q5, Q9",
                "instructions": [
                    (
                        "Assign customs eligibility and formal filing decisions to the engaged licensed broker "
                        "or trade counsel. Verify the permitted scope of each role and obtain required "
                        "powers of attorney directly through the authorized professional's documented engagement process."
                    ),
                    (
                        "Build an eligibility memorandum for each duty component rather than relying on a "
                        "generic tariff label. Review antidumping, countervailing, Section 232, Section 301, "
                        "and other special measures against the operative statute, proclamation, exclusion, and current agency instructions."
                    ),
                    (
                        "Write the contingency addendum around realized cash, fee calculation, direct expenses, "
                        "partial recoveries, reversals, and termination. Identify who controls filings and who "
                        "receives refunds, keeping the operator's service agreement separate from customs representation authority."
                    ),
                    (
                        "For each settlement, preserve the controlling orders and administrator requirements governing "
                        "third-party assistance, certification, compensation, and payment directions. Tell claimants "
                        "they may file directly at zero cost and avoid suggesting affiliation with the court or administrator."
                    ),
                    (
                        "Audit retention, access, deletion, and dispute handling against the actual records "
                        "and contracts in use. Freeze deletion when litigation, agency examination, or "
                        "a preservation duty applies, and record remediation owners for every material exception."
                    ),
                ],
                "fields": [
                    field(
                        "Customs representation and POA evidence",
                        "textarea",
                        "Identify the licensed customs broker or trade counsel, authority documents, authorized "
                        "signers, and filing scope. Explain how the operator avoids conducting regulated "
                        "customs business outside the permitted role under 19 CFR Part 111.",
                        "Example: Harbor engages a verified licensed broker for drawback and PSC preparation "
                        "and execution, with trade counsel retained for contested legal issues. The broker "
                        "obtains a valid Customs Power of Attorney directly from Harbor and verifies signer "
                        "authority. The operator collects authorized records and coordinates tasks but does not "
                        "use the broker's credentials, sign customs declarations, or independently make formal "
                        "classification representations to CBP.",
                    ),
                    field(
                        "Drawback provision and five-year clocks",
                        "textarea",
                        "Cite the precise drawback provision and document all applicable import, export, "
                        "destruction, and filing clocks. Distinguish unused merchandise requirements from "
                        "manufacturing drawback rules and explain the complete-claim evidence required before expiry.",
                        "Example: The example uses § 1313(j)(1) unused merchandise treatment, not a manufacturing "
                        "theory. The broker validates the relevant five-year export period and the complete "
                        "claim requirement under § 1313(r)(1) and 19 CFR § 190.51. An internal "
                        "deadline is set 90 days before the verified statutory limit. A missing export "
                        "record is escalated immediately; a draft spreadsheet is not treated as a complete filing.",
                    ),
                    field(
                        "Excluded duties and special tariff treatment",
                        "textarea",
                        "List every duty component and the authority supporting inclusion or exclusion. "
                        "Address special tariff measures individually, including current product coverage "
                        "and effective dates, instead of assuming all additional duties share one drawback treatment.",
                        "Example: The broker excludes $12,000 antidumping duties under 19 U.S.C. § 1313(v), "
                        "which also addresses countervailing duties. A separate Section 232 component is tested "
                        "against the applicable proclamation's drawback restriction and excluded where barred. "
                        "Section 301 duties receive a separate eligibility review rather than automatic exclusion "
                        "or inclusion. The memo records entry dates, tariff components, authorities, and the "
                        "resulting $100,000 eligible example base.",
                    ),
                    field(
                        "PSC, protest, and contested decision controls",
                        "textarea",
                        "Document which administrative path applies to each entry and which issues it can "
                        "address. Include liquidation monitoring, standing, filing authority, and escalation "
                        "to counsel where a protest cannot resolve the underlying legal question.",
                        "Example: The broker uses PSC only while the entry and timing remain eligible under "
                        "current ACE rules. After a protestable liquidation decision, counsel evaluates § 1514 "
                        "and 19 CFR Part 174, including the applicable 180-day deadline. A challenge "
                        "to an underlying governmental measure is not automatically labeled a routine classification "
                        "protest. Counsel identifies jurisdiction and remedy before the operator promises that a "
                        "particular administrative filing can preserve recovery.",
                    ),
                    field(
                        "Accelerated drawback and surety responsibilities",
                        "textarea",
                        "Identify accelerated-payment authorization, bond terms, collateral, audit obligations, "
                        "and repayment exposure. State who bears premium and indemnity costs and "
                        "what operational changes apply if the surety reduces capacity or CBP withholds payment.",
                        "Example: The broker evaluates accelerated payment under 19 CFR § 190.92 and obtains "
                        "the actual required security terms. Harbor reviews any indemnity obligation directly "
                        "with the surety and counsel. The operator budgets a quoted $1,200 premium but "
                        "does not promise access to accelerated funds. If authorization or capacity is "
                        "unavailable, the claim follows the ordinary timing assumption and the cash forecast "
                        "removes accelerated receipts.",
                    ),
                    field(
                        "Settlement authority and third-party filer disclosure",
                        "textarea",
                        "Identify the operative court order, administrator instructions, class definition, "
                        "and third-party filer requirements. Record the exact claimant disclosure "
                        "and confirm whether representation, assignments, fee deductions, or payment redirection are restricted.",
                        "Example: For an illustrative settlement approved under Federal Rule of Civil Procedure "
                        "23(e), the engagement states: 'You may submit your claim directly to the settlement "
                        "administrator at zero cost. Our optional preparation service charges 30% of your "
                        "realized distribution.' The specialist adds every court-required third-party disclosure, "
                        "checks whether paid assistance is permitted, and removes any payment-redirection term "
                        "that conflicts with the operative order.",
                    ),
                    field(
                        "Claim certification and litigation boundaries",
                        "textarea",
                        "Identify who certifies claim facts, who resolves legal interpretation, and whether "
                        "the work concerns an existing settlement or new litigation. Distinguish "
                        "settlement claim deadlines from substantive antitrust limitation periods and litigation rights.",
                        "Example: Harbor certifies qualifying purchases and affiliate status after reviewing the "
                        "prepared schedule. The operator does not sign factual declarations on Harbor's behalf "
                        "without express permitted authority. Counsel explains that 15 U.S.C. § 15b's "
                        "four-year limitation framework for damages actions is distinct from a settlement's "
                        "court-ordered claim deadline. The engagement covers an existing settlement claim, not "
                        "commencement or funding of a new antitrust lawsuit.",
                    ),
                    field(
                        "Contingency, termination, and reversal addendum",
                        "textarea",
                        "Draft concrete commercial terms defining the recovery base, earned fee event, "
                        "expenses, refunds, termination, and duplicate-representation handling. Make the "
                        "client's obligations measurable without charging for unsupported projected recoveries.",
                        "Example: 'The drawback fee is 30% of eligible refund principal actually received for "
                        "the scheduled claim population; interest is excluded. No upfront service fee applies. "
                        "The operator bears listed preparation expenses. A repayment reduces the corresponding "
                        "fee proportionately. After termination, fees apply only to documented scheduled work "
                        "that produces recovery under the agreed tail period; duplicate representative fees "
                        "require written resolution before filing.'",
                    ),
                    field(
                        "Record retention and restricted access",
                        "textarea",
                        "Set retention periods by record category, governing authority, contractual need, "
                        "and preservation duties. Specify access permissions, secure transfer methods, "
                        "and the controls preventing premature deletion of customs, financial, or settlement evidence.",
                        "Example: The broker maps drawback records to 19 CFR Part 190, including applicable "
                        "retention requirements measured from payment, and checks other relevant Part 163 duties. "
                        "The team does not start every clock at intake. Customs records are restricted "
                        "to assigned analysts and the broker; settlement purchase records have a separate "
                        "access group. A documented litigation hold suspends scheduled deletion and records "
                        "the responsible counsel and affected files.",
                    ),
                    field(
                        "Audit exceptions and remediation evidence",
                        "textarea",
                        "Record each material exception, affected claims, responsible owner, corrective action, "
                        "and verification evidence. Prioritize defects that threaten filing authority, "
                        "eligibility, deadlines, claimant funds, or the truthfulness of signed submissions.",
                        "Example: The audit finds one expired internal signer authorization, two missing export "
                        "documents, and a settlement disclosure using an obsolete administrator address. All "
                        "affected submissions pause. Harbor refreshes signer evidence, the warehouse supplies "
                        "traceable export records, and the specialist verifies the current administrator contact "
                        "against the court materials. A second reviewer records closure dates and supporting "
                        "files before the claims return to the submission queue.",
                    ),
                ],
                "completion_gate": (
                    "The responsible broker or counsel confirms customs authority and route selection; "
                    "the settlement specialist verifies controlling orders and disclosures. Every material "
                    "contract, eligibility, retention, and certification exception has documented resolution."
                ),
            },
            {
                "worksheet_id": "ws-05",
                "number": 5,
                "title": "Automation Pipeline, Acquisition Flywheel & Risk Fallback Tracker",
                "purpose": (
                    "Automate evidence preparation and prospect qualification without delegating eligibility "
                    "decisions to unverified matches. Connect acquisition signals to authorized records, "
                    "measure exception costs, and maintain tested fallback procedures for missing exports, "
                    "portal outages, bond constraints, deadline changes, and delayed settlement distributions."
                ),
                "chapter_ref": "Q6, Q10",
                "instructions": [
                    (
                        "Use ImportGenius or Panjiva to identify plausible import activity, not to establish "
                        "paid duties or ownership. Obtain permission before connecting claimant records, and "
                        "keep prospecting observations separate from evidence used in a formal customs claim."
                    ),
                    (
                        "Automate extraction, normalization, duplicate detection, and exception routing before "
                        "automating external actions. Require deterministic calculations and source links "
                        "for every monetary value, and preserve a manual review path for uncertain document interpretation."
                    ),
                    (
                        "Track acquisition efficiency using signed authorized engagements, accepted evidence "
                        "packages, and collected fees rather than raw leads. Attribute contractor rework "
                        "and failed claim preparation to the originating channel so misleading volume does not hide poor economics."
                    ),
                    (
                        "Set stop conditions for broken data feeds, missing export trace, expiring "
                        "deadlines, constrained surety capacity, and changed settlement instructions. "
                        "Assign a fallback owner and a tested alternative process for each condition before increasing throughput."
                    ),
                    (
                        "Use approved client references and carefully scoped case studies to grow referrals. "
                        "Do not publish importer records, merchant purchase details, or recovery amounts "
                        "without explicit permission, and keep outcome examples tied to their documented factual populations."
                    ),
                ],
                "fields": [
                    field(
                        "Manifest intelligence to authorized intake",
                        "textarea",
                        "Define prospect filters, data licensing limits, outreach qualification, and the "
                        "handoff to claimant-authorized ACE records. Explain which facts manifest "
                        "intelligence can support and which must be verified from primary customs evidence.",
                        "Example: Panjiva identifies 60 import-active manufacturers with apparent outbound activity. "
                        "Outreach asks whether they retain import and export records rather than asserting "
                        "refund entitlement. Twelve respond, six authorize a preliminary records review, and "
                        "three provide usable ACE summaries. Manifest quantities remain prospecting signals; "
                        "paid duties, importer identity, merchandise condition, and actual export linkage come "
                        "from authorized records before any claim value enters underwriting.",
                    ),
                    field(
                        "Extraction schema and source confidence",
                        "textarea",
                        "Specify normalized fields, deterministic validations, document confidence thresholds, "
                        "and exception routing. Make low-confidence amounts and dates reviewable "
                        "without allowing extraction confidence to substitute for statutory eligibility or source authenticity.",
                        "Example: The parser extracts entry number, line, import date, ten-digit tariff "
                        "classification, duty components, quantity, unit, and invoice reference. A derived "
                        "eight-digit key supports candidate matching. Amounts are calculated with decimal "
                        "arithmetic, not binary floating-point approximations. Any unclear date, negative quantity, "
                        "or mismatch against the source total enters manual review; a high extraction score "
                        "still does not establish drawback eligibility.",
                    ),
                    field(
                        "Export BOL and HTS reconciliation automation",
                        "textarea",
                        "Describe the linkage logic connecting entry records, inventory movements, export "
                        "documents, and substitution candidates. Record unit conversions and reviewer "
                        "decisions so an automated match remains reproducible when product descriptions differ.",
                        "Example: The pipeline converts 100 cartons containing 20 units each into 2,000 units "
                        "using the retained packing specification. It proposes an export match against "
                        "the warehouse shipment and BOL, then checks dates and allocated quantities. "
                        "A same-eight-digit HTS substitution candidate is routed to the broker for "
                        "restriction and value testing. The system records the conversion rule and "
                        "review outcome instead of silently treating similar descriptions as identical merchandise.",
                    ),
                    field(
                        "Accounts-payable settlement claim packager",
                        "textarea",
                        "Define vendor normalization, class-period filtering, product qualification, credit "
                        "memo treatment, and duplicate detection for settlement purchase records. "
                        "Explain how the packager preserves administrator-specific requirements rather than applying one generic allocation template.",
                        "Example: The packager maps vendor aliases to legal sellers, excludes transactions outside "
                        "the settlement period, and nets $50,000 of credit memos against $2,050,000 "
                        "otherwise eligible purchases. The resulting $2,000,000 schedule links every line "
                        "to an invoice or accepted alternative record. Administrator-specific columns and "
                        "certification questions are versioned separately. The projected $20,000 distribution "
                        "remains an estimate, not a fixed percentage promised to the claimant.",
                    ),
                    field(
                        "Acquisition funnel and cohort economics",
                        "textarea",
                        "Measure conversion from targeted account to authorization, usable evidence, filed "
                        "claim, and collected fee. Attribute cash acquisition spend and preparation "
                        "labor to cohorts, while separating early engagement conversion from eventual cash realization.",
                        "Example: A $900 drawback acquisition cohort produces 30 targeted accounts, six qualified "
                        "conversations, two authorized reviews, and one accepted engagement. Acquisition cost "
                        "per engagement is $900, not $150 per conversation. The eventual example fee "
                        "is $29,700 only if the modeled recovery is realized. Monthly reporting keeps "
                        "that cohort's uncollected forecast separate from cash fees and includes any "
                        "abandoned-review labor in channel profitability.",
                    ),
                    field(
                        "Specialist capacity and exception cost",
                        "textarea",
                        "Quantify clean-package throughput, exception frequency, review time, and contracted "
                        "specialist capacity. Identify the bottleneck that limits additional acquisition "
                        "and calculate the economic effect of improving source quality instead of adding indiscriminate leads.",
                        "Example: One analyst prepares eight clean packages monthly, but each missing-export "
                        "exception consumes four extra hours. At a $75 contractor rate, ten exceptions "
                        "cost $3,000 and 40 hours. A $600 archive-retrieval improvement eliminating six "
                        "exceptions saves $1,800 of labor, producing $1,200 net savings for that cohort. "
                        "The broker's available review slots remain the final throughput constraint even "
                        "after extraction becomes faster.",
                    ),
                    field(
                        "Portal outage and submission fallback",
                        "textarea",
                        "Document the response to unavailable customs or administrator systems, including "
                        "deadline escalation, authorized alternative channels, and receipt verification. "
                        "Prevent retries from creating duplicate claims or treating an internal queue timestamp as an external filing.",
                        "Example: An administrator portal fails five days before the claim deadline. The "
                        "specialist captures the error, contacts the published administrator support channel, "
                        "and checks the operative instructions for an authorized alternative. The team "
                        "uses an alternate method only if permitted and preserves delivery evidence. "
                        "A queued browser submission is not recorded as filed; restoration triggers "
                        "receipt reconciliation before any retry or replacement transmission.",
                    ),
                    field(
                        "Bond, export-trace, and payment-delay fallback",
                        "textarea",
                        "Specify separate fallback actions for insufficient surety capacity, missing "
                        "export documentation, and delayed distribution. Quantify how each changes "
                        "claim scope, cash timing, preparation spending, and the next review date.",
                        "Example: If collateral rises by $10,000, the operator removes accelerated receipts "
                        "from the cash plan and asks the broker to assess ordinary processing. "
                        "If export evidence remains missing for 18% of value, that population stays "
                        "outside the supported claim calculation. If settlement payment slips six months, "
                        "no fee invoice is issued; new acquisition spending pauses when unrestricted "
                        "runway would fall below two months of committed costs.",
                    ),
                    field(
                        "Referral loop and publication permissions",
                        "textarea",
                        "Define the referral trigger, permitted case-study detail, client permission "
                        "record, and channel attribution. Keep outreach claims tied to "
                        "verified outcomes and distinguish optional paid services from direct settlement filing options.",
                        "Example: After a fee is collected and the claimant confirms satisfaction, the operator "
                        "requests an introduction to one peer controller. Written permission allows an "
                        "anonymized case study reporting a $99,000 drawback receipt and 30% service fee, "
                        "but excludes entry numbers, supplier names, and shipment details. Settlement "
                        "outreach states the claimant may file directly at zero cost and identifies "
                        "the operator as an independent optional service provider.",
                    ),
                    field(
                        "Automation monitoring and rollback test",
                        "textarea",
                        "List production checks, failure thresholds, deployment rollback steps, and "
                        "human escalation ownership. Test whether a changed rule, corrupted "
                        "document, repeated event, or stale deadline source can alter accepted claim amounts without detection.",
                        "Example: A weekly replay feeds 20 archived packages through the current matcher. "
                        "Any unexplained change in eligible duty totals stops deployment. A duplicate "
                        "payment event must create zero extra invoices, and a corrupted source "
                        "checksum must trigger quarantine. The prior rule version remains deployable; "
                        "the operations lead owns rollback while the broker approves changes affecting "
                        "customs eligibility, duty treatment, or formal filing output.",
                    ),
                ],
                "completion_gate": (
                    "One authorized package per lane completes a supervised pipeline test; exception "
                    "costs and acquisition attribution are visible. Portal failure, duplicate events, "
                    "missing evidence, and reduced bond capacity each have a tested owner-led fallback."
                ),
            },
            {
                "worksheet_id": "ws-06",
                "number": 6,
                "title": "30-Day Launch Sprint, Pod KPI Scorecard & Exit-Readiness Ledger",
                "purpose": (
                    "Launch a disciplined recovery operation without confusing early engagements with "
                    "collected fees. Allocate the small-team pod, stage the first thirty days, "
                    "monitor evidence and cash performance, and assemble transferable operating records "
                    "that support later diligence without overstating backlog or recovery certainty."
                ),
                "chapter_ref": "Q11, Q12",
                "instructions": [
                    (
                        "Plan the first thirty days around specialist readiness, authorized intake, "
                        "evidence quality, and a complete sample workflow. Treat the one-to-three-month "
                        "first-deal range as an engagement target, not a promise that customs or settlement cash arrives immediately."
                    ),
                    (
                        "Assign one accountable owner to each lane and control function, including "
                        "backup coverage for deadlines. Use the canonical team configurations when "
                        "modeling annual outcomes, while documenting actual contractor scope, capacity, billing terms, and conflicts."
                    ),
                    (
                        "Review pod metrics weekly using consistent denominators and source evidence. "
                        "Track accepted evidence packages, approaching deadlines, claim rework, cash "
                        "runway, and collected fee revenue separately so a larger forecast cannot conceal execution or liquidity deterioration."
                    ),
                    (
                        "Create an exit-readiness ledger as operations begin rather than reconstructing "
                        "records later. Preserve assignability restrictions, claimant permissions, specialist "
                        "relationships, revenue reconciliation, open audit exposure, and access-control evidence in a restricted diligence structure."
                    ),
                    (
                        "At day thirty, compare actual readiness against the written milestones and "
                        "funding plan. Expand only the lanes with supported eligibility, reliable "
                        "delivery capacity, and funded waiting periods; record deferred work explicitly instead of manufacturing progress from speculative recoveries."
                    ),
                ],
                "fields": [
                    field(
                        "Days 1–7 specialist and authority foundation",
                        "textarea",
                        "Define the first week's deliverables, owners, costs, and evidence of "
                        "completion. Prioritize licensed customs capacity, settlement expertise, engagement "
                        "terms, secure intake, and a funded initial operating plan before purchasing broad prospect lists.",
                        "Example: By day 7, the founder confirms one licensed broker, one trade-counsel "
                        "contact, and one settlement specialist. The team approves the three-lane "
                        "intake form, contingency addendum, and direct-filing disclosure template. An "
                        "$8,000 setup budget covers scoped professional work, secure document storage, "
                        "and initial data access. Completion requires executed service arrangements "
                        "and tested access, not merely introductory calls or unsigned proposals.",
                    ),
                    field(
                        "Days 8–14 acquisition and authorized records",
                        "textarea",
                        "Set a targeted outreach cohort, qualification questions, authorization target, "
                        "and source-record acceptance standard. Define what counts as a "
                        "qualified engagement while keeping unsupported duty estimates outside the collectible recovery forecast.",
                        "Example: Contact 30 import-active manufacturers and 20 businesses fitting one verified "
                        "settlement class. Target six substantive conversations and three authorized "
                        "record reviews, not a guaranteed number of claims. For each customs "
                        "prospect, request entry summaries and export evidence before pricing. "
                        "For each settlement prospect, verify the class period and direct-filing "
                        "option. The founder records responses, authorization dates, and reasons "
                        "for declining unsuitable opportunities.",
                    ),
                    field(
                        "Days 15–21 production pilot and controls",
                        "textarea",
                        "Define the supervised pilot, required records, reviewer responsibilities, "
                        "and test cases for each lane. Distinguish a completed "
                        "internal package from a real external submission and avoid manufacturing filings solely to satisfy sprint milestones.",
                        "Example: Prepare one authorized drawback package, one tariff-route assessment, and one "
                        "settlement eligibility package if suitable prospects exist. Otherwise use "
                        "clearly labeled synthetic records for the missing lane's workflow test. "
                        "Run duplicate-file, missing-export, stale-deadline, and payment-reversal tests. "
                        "The broker signs the customs assessment; the settlement specialist "
                        "checks the controlling instructions. No synthetic package is submitted "
                        "to CBP or a settlement administrator.",
                    ),
                    field(
                        "Days 22–30 readiness decision and next sprint",
                        "textarea",
                        "List the final readiness evidence, remaining blockers, responsible owners, "
                        "and next-month priorities. Use actual completion status and "
                        "funding needs rather than converting pipeline estimates into revenue or declaring all lanes operational prematurely.",
                        "Example: Day 30 closes with two signed engagements, one broker-reviewed drawback "
                        "package, and a settlement workflow tested on synthetic records. "
                        "Collected fee revenue remains $0 because no recovery has arrived. "
                        "The next sprint pursues missing export records, verifies tariff "
                        "route timing, and secures one suitable settlement claimant. The "
                        "founder defers paid acquisition expansion until the cash plan "
                        "covers the documented preparation and waiting-period commitments.",
                    ),
                    field(
                        "Pod roster and canonical staffing",
                        "textarea",
                        "Assign accountable people to acquisition, evidence, licensed filing, settlement "
                        "review, and accounting. Reconcile the roster with canonical "
                        "staffing and state contractor availability, backup arrangements, and which tasks remain with the full-time operator.",
                        "Example: Conservative and Base use 1 FT + 3 C: the founder owns sales, "
                        "cash, and case coordination; contracted roles cover broker filing, "
                        "evidence engineering, and settlement or trade specialist support under "
                        "defined scopes. Scaled uses 2 FT + 4 C, six people, "
                        "adding a full-time operations lead and a fourth contracted role. "
                        "Counsel availability and accounting support are scoped explicitly within "
                        "the actual cost plan rather than assumed free.",
                    ),
                    field(
                        "Weekly operating KPI scorecard",
                        "textarea",
                        "Define each KPI, numerator, denominator, reporting interval, source, and "
                        "intervention threshold. Include evidence completeness, deadline exposure, "
                        "rework, collection timing, and fee cash without merging forecasts with completed production or collections.",
                        "Example: Week 4 shows three authorized reviews, two signed engagements, and one "
                        "broker-reviewed package. Value-weighted export support is 82%; material "
                        "unresolved deadlines within 30 days number zero. Two of "
                        "ten reviewed records require correction, producing a 20% record "
                        "rework rate. Collected fees are $0, and unrestricted runway "
                        "is calculated from committed spending. Any approaching unsupported "
                        "filing deadline receives same-day specialist escalation.",
                    ),
                    field(
                        "Capital allocation and economic checkpoint",
                        "textarea",
                        "Compare actual launch spending, monthly overhead, direct claim commitments, "
                        "and restricted cash with the canonical startup and "
                        "operating ranges. Explain any funding gap and distinguish first signed deal timing from first collected fee timing.",
                        "Example: Available launch capital is $35,000 within the $8,000–$35,000 range, and "
                        "fixed overhead is $3,000 monthly within the $1,500–$9,500 "
                        "range. The four-month worked plan leaves $2,200 before "
                        "collections, excluding additional collateral. A first engagement in "
                        "months 1–3 does not solve that cash constraint. The "
                        "operator defers acceleration requiring $10,000 collateral unless "
                        "separate committed liquidity funds it.",
                    ),
                    field(
                        "Revenue quality and transferable backlog",
                        "textarea",
                        "Separate collected fees, earned receivables, conditional forecasts, and speculative "
                        "opportunities. Record claim stage, reversal exposure, transfer "
                        "restrictions, and supporting evidence so a reviewer can assess revenue quality without treating claimant principal as business sales.",
                        "Example: The diligence ledger shows $29,700 collected drawback fees, $10,000 tariff "
                        "fees earned after a documented refund but awaiting client "
                        "payment, and $6,000 conditional settlement fees awaiting distribution. "
                        "These are three different categories, not $45,700 collected "
                        "revenue. Underlying claimant recoveries remain separate. Each "
                        "engagement records assignability terms, required client permissions, "
                        "open servicing duties, and the source documents supporting "
                        "its stated accounting treatment.",
                    ),
                    field(
                        "Exit-readiness evidence and relationship transfer",
                        "textarea",
                        "Inventory operating procedures, client contracts, specialist dependencies, licenses, "
                        "data permissions, and system access that affect "
                        "transferability. Identify what a purchaser could receive contractually and what requires new client authority or professional arrangements.",
                        "Example: The restricted diligence index contains redacted contracts, monthly fee "
                        "reconciliations, procedure versions, security records, and specialist "
                        "capacity agreements. Client customs records are not released "
                        "merely because a buyer signs a general interest letter. "
                        "Broker licenses, portal credentials, and Customs Powers of "
                        "Attorney are not treated as freely transferable assets. "
                        "Counsel maps required consents and replacement arrangements "
                        "before any proposed transaction changes access or representation.",
                    ),
                    field(
                        "Thirty-day decision and scorecard reconciliation",
                        "textarea",
                        "Record the launch decision, deferred lanes, next funding action, and "
                        "canonical annual targets. Confirm the difference between "
                        "a modeled operating outcome and measured performance, preserving the exact profit, margin, staffing, and ranking metadata.",
                        "Example: Continue the supported drawback pilot, defer paid settlement acquisition until "
                        "one real class-qualified claimant is verified, and fund "
                        "the next evidence cycle before expanding. Volume 044 "
                        "remains pipeline rank #03 with Money-to-Manpower Score "
                        "95/100: revenue 25, margin 24, efficiency 19, accessibility "
                        "14, automation 13. Canonical annual owner profit targets "
                        "remain $35,200 Conservative, $231,750 Base, and $533,600 "
                        "Scaled; none is reported as achieved launch performance.",
                    ),
                ],
                "completion_gate": (
                    "The founder signs the thirty-day evidence ledger, reconciles actual cash and "
                    "claim status, and approves only funded next-sprint commitments. Canonical annual "
                    "targets remain distinct from measured results, with transfer restrictions and "
                    "unfinished lane work explicitly recorded."
                ),
            },
        ],
    }
