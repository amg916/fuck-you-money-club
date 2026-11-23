from __future__ import annotations


def build_volume_047_workbook() -> dict:
    def field(name: str, input_type: str, prompt: str, example: str) -> dict:
        return {
            "name": name,
            "type": input_type,
            "prompt": prompt,
            "example": example,
        }

    return {
        "workbook_id": "wb-047-ai-data-center-powered-land-and-bess-optioning",
        "volume_id": "vol-047-ai-data-center-powered-land-and-bess-optioning",
        "title": (
            "AI Data-Center Powered Land, Substation Headroom & BESS Site "
            "Optioning — Operator Companion Workbook"
        ),
        "subtitle": (
            "6 Printable Operator Worksheets for Utility-Validated Powered Land, "
            "Separate BESS Parcel Underwriting, Assignable Options, Reserve "
            "Discipline, Evidence-Controlled Execution, and Small-Team Launch"
        ),
        "worksheets": [
            {
                "worksheet_id": "ws-01",
                "number": 1,
                "title": "Arbitrage Deal / Counterparty Underwriting & Spread Qualification",
                "purpose": (
                    "Separate attractive map coordinates from transferable, economically "
                    "defensible site control. Establish counterparty authority, utility "
                    "evidence, land-use feasibility, and buyer demand before pricing an "
                    "option assignment. Underwrite standalone storage parcels separately "
                    "from data-center campuses, with explicit rejection and expiration costs."
                ),
                "chapter_ref": "Q1, Q2, Q6",
                "instructions": [
                    (
                        "Create one opportunity record per parcel, use case, and proposed "
                        "utility service configuration. Preserve source dates and document "
                        "identifiers; do not combine storage export rights, campus import "
                        "requests, or neighboring ownership into a single capacity claim."
                    ),
                    (
                        "Classify each power assertion by evidence strength: geographic "
                        "screen, utility discussion, completed study, executed agreement, "
                        "or satisfied service conditions. Record the study scope and "
                        "limitations before assigning any MW-dependent premium to the option."
                    ),
                    (
                        "Contact the owner, utility representative, and prospective buyer "
                        "through independently verified channels. Confirm signing authority, "
                        "commercial objectives, funding capacity, and decision deadlines; "
                        "retain written responses rather than relying on an intermediary's "
                        "summary of another party's commitments."
                    ),
                    (
                        "Run separate physical screens for storage and computing. Test "
                        "BESS setbacks, access, drainage, and fire response; test campus "
                        "fiber diversity, cooling strategy, water availability, noise, and "
                        "phasing. Record which constraint can independently terminate underwriting."
                    ),
                    (
                        "Price the assignable interest after deducting expected option "
                        "burn, documented upgrade exposure, specialist costs, and time "
                        "risk. Set a maximum cash-at-risk amount and a dated rejection "
                        "decision before negotiating a longer diligence period."
                    ),
                ],
                "fields": [
                    field(
                        "Parcel identity, use case, and ownership chain",
                        "textarea",
                        (
                            "Identify the parcel, legal owner, controlling entity, acreage, "
                            "proposed use, and ownership evidence. Explain whether adjacent "
                            "land is essential and identify any missing access or easement "
                            "interest that prevents independent development."
                        ),
                        (
                            "Opportunity TX-BESS-014 covers an illustrative 12-acre storage "
                            "parcel owned by Cedar Parcel LLC. The title commitment matches "
                            "the proposed option grantor; a manager resolution establishes "
                            "signing authority. A separate recorded access easement is "
                            "required across the southern tract before any buyer receives "
                            "an executable assignment package."
                        ),
                    ),
                    field(
                        "Utility evidence and deliverable capacity classification",
                        "textarea",
                        (
                            "Record utility-authored capacity findings, service voltage, "
                            "study date, operating assumptions, remaining conditions, and "
                            "the responsible utility contact. Distinguish requested MW from "
                            "documented deliverable MW and identify the evidence required "
                            "before increasing valuation."
                        ),
                        (
                            "The campus requests 40 MW at 138 kV. An illustrative completed "
                            "utility study supports a conditional 20 MW first phase after "
                            "specified upgrades, with service targeted for October 2029. "
                            "Underwriting uses only that conditional 20 MW tranche; the "
                            "remaining 20 MW receives zero capacity premium pending further study."
                        ),
                    ),
                    field(
                        "Network-upgrade exposure and restudy sensitivity",
                        "textarea",
                        (
                            "List allocated network upgrades, estimate class, contingency, "
                            "deposit deadlines, cost responsibility, and restudy triggers. "
                            "Calculate the economic effect of an adverse revision and "
                            "identify the contractual right that limits the operator's "
                            "exposure before assignment."
                        ),
                        (
                            "The utility's preliminary allocation is $2.4 million, funded "
                            "by the acquiring developer rather than the originator. A "
                            "40% restudy increase adds $960,000. The buyer's $3 million "
                            "investment threshold would be exceeded, so the option permits "
                            "termination before the next $7,500 extension becomes payable."
                        ),
                    ),
                    field(
                        "Standalone BESS parcel qualification",
                        "textarea",
                        (
                            "Underwrite the storage parcel independently using acreage, "
                            "import and export limits, duration, fire access, setbacks, "
                            "drainage, noise, and emergency planning. State which technical "
                            "findings are preliminary and which require qualified engineering "
                            "or utility confirmation."
                        ),
                        (
                            "A 12-acre parcel is screened for 20 MW / 80 MWh storage, "
                            "representing four hours of discharge duration. Engineering "
                            "must validate usable acreage after drainage and setbacks. "
                            "The utility must separately establish charging import and "
                            "discharging export capability; an export queue position does "
                            "not establish either service entitlement."
                        ),
                    ),
                    field(
                        "AI campus fiber, cooling, and zoning qualification",
                        "textarea",
                        (
                            "Document campus-specific power phasing, carrier routes, cooling "
                            "requirements, water sources, wastewater arrangements, zoning, "
                            "and noise limits. Identify physical dependencies that prevent "
                            "a storage-qualified parcel from being marketed as a "
                            "development-ready computing campus."
                        ),
                        (
                            "The illustrative 80-acre campus needs a 20 MW initial phase "
                            "and two physically diverse carrier entrances. Carrier letters "
                            "currently show both routes using one bridge. An air-cooled "
                            "design reduces process-water demand, but civil engineering "
                            "must still confirm domestic supply, stormwater capacity, and "
                            "permitted equipment-noise limits."
                        ),
                    ),
                    field(
                        "Option duration, assignability, and seller authority",
                        "textarea",
                        (
                            "Summarize the proposed option term, extension mechanics, "
                            "assignment permissions, notice procedure, title obligations, "
                            "and signature authority. Identify utility or zoning conditions "
                            "that permit exit without creating an obligation to purchase "
                            "the underlying property."
                        ),
                        (
                            "The proposed principal-held option runs 18 months, with a "
                            "$7,000 initial fee and two three-month extensions at $3,500 "
                            "each. Assignment to a qualified project entity requires "
                            "notice rather than discretionary seller consent. Utility "
                            "and zoning termination rights are stated expressly, with "
                            "fees remaining nonrefundable unless otherwise negotiated."
                        ),
                    ),
                    field(
                        "Developer counterparty and purchase authority",
                        "textarea",
                        (
                            "Identify the buyer's investment mandate, authorized decision "
                            "maker, capital source, diligence sequence, and comparable "
                            "execution history. Establish evidence of ability to fund "
                            "assignment consideration separately from ability to finance "
                            "the eventual construction project."
                        ),
                        (
                            "The developer seeks 10–25-acre storage sites and delegates "
                            "site-control purchases below $150,000 to an investment "
                            "committee. Request its written mandate, authorized signatory "
                            "list, and evidence supporting the $95,000 assignment payment. "
                            "A construction financing discussion alone does not establish "
                            "cash available for the option acquisition."
                        ),
                    ),
                    field(
                        "Assignment spread and buyer residual economics",
                        "textarea",
                        (
                            "Calculate assignment consideration less acquisition fees, "
                            "site diligence, closing expenses, and allocated failed-site "
                            "burn. Show the buyer's remaining development costs separately "
                            "and state why the proposed spread survives documented "
                            "utility and schedule limitations."
                        ),
                        (
                            "A $95,000 assignment produces $62,000 before shared overhead "
                            "after $7,000 option acquisition, $12,000 successful-site "
                            "diligence, $8,000 closing services, and $6,000 allocated "
                            "expired-site fees. The buyer separately funds land purchase "
                            "and utility upgrades; neither amount becomes operator "
                            "revenue or inflates the assignment spread."
                        ),
                    ),
                    field(
                        "Fatal-flaw evidence and rejection thresholds",
                        "textarea",
                        (
                            "List independently decisive rejection conditions, evidence "
                            "owners, maximum investigation spend, and decision deadlines. "
                            "Include current land-use restrictions, unresolved title "
                            "defects, utility timing, environmental constraints, and "
                            "counterparty behavior that invalidates the original underwriting."
                        ),
                        (
                            "Reject the campus if an enacted data-center moratorium "
                            "covers the parcel, if utility service moves beyond the "
                            "buyer's December 2029 deadline, or if no diverse carrier "
                            "route is commercially available. Limit pre-option screening "
                            "to $1,200 and preserve the dated ordinance, utility "
                            "response, and carrier route evidence."
                        ),
                    ),
                    field(
                        "Investment decision and permitted marketing language",
                        "textarea",
                        (
                            "Record the decision, permitted claims, unresolved conditions, "
                            "cash-at-risk ceiling, and next evidence milestone. Specify "
                            "exactly how the buyer package describes capacity so "
                            "commercial enthusiasm cannot convert conditional findings "
                            "into unconditional service representations."
                        ),
                        (
                            "Proceed only to a $7,000 contingent option after title "
                            "and authority checks. Buyer materials state: Utility study "
                            "supports a conditional 20 MW phase, subject to listed "
                            "upgrades and service conditions. Materials exclude the "
                            "unstudied expansion request and show October 2029 as "
                            "a conditional target rather than an assured energization date."
                        ),
                    ),
                ],
                "completion_gate": (
                    "The principal signs only after parcel identity, seller authority, "
                    "separate use-case screening, utility evidence classification, "
                    "buyer qualification, maximum fee burn, and assignment economics "
                    "are documented. Any unresolved fatal flaw keeps the opportunity "
                    "in screening rather than funded site control."
                ),
            },
            {
                "worksheet_id": "ws-02",
                "number": 2,
                "title": "Unit Economics, Escrow/Reserve Float & Working-Capital Calculator",
                "purpose": (
                    "Reconcile opportunity-level spreads with the canonical annual "
                    "scorecard while protecting cash during long utility diligence "
                    "cycles. Separate recognized operator fees, restricted deposits, "
                    "land consideration, and construction capital. Budget failed "
                    "options explicitly and expose funding gaps before commitments "
                    "consume available reserves."
                ),
                "chapter_ref": "Q3, Q4",
                "instructions": [
                    (
                        "Copy all three canonical scenarios without changing revenue, "
                        "margin, owner profit, or team size. Build any transaction mix "
                        "as a transparent illustrative bridge to those totals, not as "
                        "a replacement forecast disguised as the published scorecard."
                    ),
                    (
                        "Define the operator's promised service or transferred interest "
                        "for every fee. Separate payment timing from recognition timing "
                        "and identify pass-through amounts. Recognize development carry "
                        "only when the applicable accounting conditions support the "
                        "reported realized amount."
                    ),
                    (
                        "Prepare a dated cash schedule covering deposits, option "
                        "extensions, recurring expenses, diligence invoices, and expected "
                        "closings. Treat escrow and refundable security as unavailable "
                        "operating cash until released; do not count forecast assignments "
                        "as current liquidity."
                    ),
                    (
                        "Allocate unsuccessful-site fees to an explicit annual loss "
                        "budget and retain successful-site costs in their own category. "
                        "Use mutually exclusive classifications so option acquisition, "
                        "specialist invoices, and closing charges are never deducted "
                        "twice in contribution calculations."
                    ),
                    (
                        "Stress the plan for six months without receipts, a delayed "
                        "milestone, and a failed utility study. Identify the exact "
                        "funding shortfall and a documented response before increasing "
                        "burn; an uncommitted investor conversation does not close "
                        "a cash deficit."
                    ),
                ],
                "fields": [
                    field(
                        "Canonical Conservative scenario reconciliation",
                        "textarea",
                        (
                            "Enter the Conservative revenue, margin, annual owner profit, "
                            "implied total costs, and staffing. Show the arithmetic and "
                            "distinguish annual recognized fee revenue from underlying "
                            "property values, requested power capacity, and project "
                            "construction budgets."
                        ),
                        (
                            "Conservative revenue is $110,000 with a 30% margin and "
                            "$33,000 annual owner net profit. Implied annual costs are "
                            "$77,000 because $110,000 minus $33,000 equals $77,000. "
                            "Staffing remains 1 FT + 3 C. Land purchase consideration "
                            "and developer-funded construction spending are excluded "
                            "from these operator totals."
                        ),
                    ),
                    field(
                        "Canonical Base scenario revenue bridge",
                        "textarea",
                        (
                            "Reconcile the Base scenario to a clearly labeled "
                            "illustrative transaction mix. Identify assignment fees, "
                            "separately earned origination milestones, and realized carry "
                            "without counting the same contractual payment in more "
                            "than one revenue category."
                        ),
                        (
                            "Base revenue equals three $95,000 assignments, four "
                            "separate $40,000 origination milestones, and $60,000 "
                            "realized development carry: $285,000 + $160,000 + "
                            "$60,000 = $505,000. Each milestone concerns a distinct "
                            "earned obligation and is not embedded in an assignment "
                            "price. A 42.0% margin produces $212,100 owner profit "
                            "with 1 FT + 3 C."
                        ),
                    ),
                    field(
                        "Canonical Scaled Small-Team scenario reconciliation",
                        "textarea",
                        (
                            "Record the Scaled revenue, margin, annual owner profit, "
                            "implied costs, and six-person team. Explain which operational "
                            "improvements would support the scenario without treating "
                            "larger project capital requirements as additional "
                            "operator revenue or unrestricted liquidity."
                        ),
                        (
                            "Scaled Small-Team revenue is $900,000 at a 54% margin, "
                            "producing $486,000 annual owner net profit and $414,000 "
                            "implied costs. Staffing is 2 FT + 4 C, six people "
                            "total. Reusable diligence packages and stronger buyer "
                            "coverage support throughput; utility deposits and "
                            "construction capital remain outside operator revenue."
                        ),
                    ),
                    field(
                        "Base annual cost ledger and classification boundaries",
                        "textarea",
                        (
                            "Allocate Base costs into mutually exclusive categories "
                            "that reconcile exactly to the canonical profit. State "
                            "which expenses include recurring operations, successful "
                            "site control, failed options, external closing support, "
                            "and separately contracted project specialists."
                        ),
                        (
                            "Base costs total $292,900: recurring operations $100,800, "
                            "successful option acquisition and diligence $72,000, "
                            "expired option fees $36,000, external closing services "
                            "$42,000, and project specialists $42,100. Recurring "
                            "operations average $8,400 monthly. Specialist invoices "
                            "exclude work already charged to successful diligence "
                            "or closing, preserving $505,000 minus $292,900 "
                            "= $212,100."
                        ),
                    ),
                    field(
                        "Startup capital allocation and usable liquidity",
                        "textarea",
                        (
                            "Allocate startup cash among option fees, diligence, "
                            "refundable escrow, setup expenses, and unrestricted reserve. "
                            "Distinguish initial cash deployment from annual expense "
                            "recognition and identify which startup items already "
                            "belong inside the annual operating model."
                        ),
                        (
                            "A $40,000 startup pool allocates $14,000 to option "
                            "fees, $10,000 to diligence, $6,000 to refundable escrow, "
                            "$2,000 to setup, and $8,000 to unrestricted reserve. "
                            "The allocation totals $40,000. Paid expenses enter "
                            "their corresponding annual cost categories once; "
                            "refundable escrow remains an asset until released "
                            "or validly forfeited."
                        ),
                    ),
                    field(
                        "Escrow controls and release evidence",
                        "textarea",
                        (
                            "Identify the holder, account reference, beneficial owner, "
                            "release conditions, reconciliation frequency, and permitted "
                            "uses of each deposit. Explain how the operating cash "
                            "report excludes restricted funds even when the "
                            "operator expects eventual reimbursement."
                        ),
                        (
                            "The $6,000 refundable diligence deposit is held by "
                            "the named title company's escrow department under "
                            "written instructions. Release requires the specified "
                            "termination notice or closing documents. The controller "
                            "reconciles the escrow statement monthly, records the "
                            "balance separately, and never uses it to cover "
                            "the $8,400 recurring monthly operating budget."
                        ),
                    ),
                    field(
                        "Failed-option burn and surviving-deal contribution",
                        "textarea",
                        (
                            "Budget nonrefundable fees lost on utility or zoning "
                            "failures independently from successful site costs. Show "
                            "how unsuccessful opportunities affect portfolio contribution "
                            "and establish a spending threshold that stops "
                            "repeated extensions on deteriorating projects."
                        ),
                        (
                            "The Base plan reserves $36,000 for expired options, "
                            "illustratively six failures at $6,000 each. One "
                            "$95,000 assignment carries a $6,000 analytical loss "
                            "allocation in its spread worksheet, but the annual "
                            "ledger books the actual $36,000 only once. No "
                            "extension proceeds after a documented fatal utility "
                            "or zoning result."
                        ),
                    ),
                    field(
                        "Six-month no-receipts runway and funding deficit",
                        "textarea",
                        (
                            "Calculate unrestricted cash needed to sustain the "
                            "selected burn rate without closings while preserving "
                            "a minimum reserve. Exclude escrow and forecast fees, "
                            "then state whether the startup allocation actually "
                            "finances the proposed operating pace."
                        ),
                        (
                            "After initial deployment, unrestricted cash is $8,000. "
                            "Six months at the Base $8,400 monthly burn requires "
                            "$50,400; preserving an $8,000 floor requires $58,400 "
                            "available cash. The deficit is therefore $50,400. "
                            "The $40,000 startup plan cannot support that pace "
                            "without additional committed funding, lower spending, "
                            "or actual collected receipts."
                        ),
                    ),
                    field(
                        "Revenue recognition, retained economics, and pass-throughs",
                        "textarea",
                        (
                            "Define gross operator fee revenue and any net "
                            "presentation required by the actual principal-agent "
                            "assessment under ASC 606. Identify earned versus "
                            "contingent amounts and exclude land price, utility "
                            "deposits, and reimbursable project capital from "
                            "unsupported revenue claims."
                        ),
                        (
                            "The illustrative $95,000 assignment fee is operator "
                            "consideration; the developer's $1.8 million land "
                            "purchase is separate. No retained_share assumption "
                            "is supplied for this volume, so none is invented. "
                            "Accounting reviews the transaction's substance and "
                            "applicable guidance; a projected $60,000 carry remains "
                            "outside recognized totals until realization and "
                            "recognition conditions are satisfied."
                        ),
                    ),
                    field(
                        "Milestone sensitivity and cash commitment decision",
                        "textarea",
                        (
                            "Model a missed milestone and an adverse utility "
                            "outcome separately from the canonical scorecard. State "
                            "the resulting revenue and profit change under "
                            "explicit cost assumptions, then identify which cash "
                            "commitments should stop before reserves are breached."
                        ),
                        (
                            "If one $40,000 milestone is never earned and Base "
                            "costs remain $292,900, the sensitivity produces "
                            "$465,000 revenue and $172,100 profit. This is a "
                            "downside case, not the canonical Base result. "
                            "Pause additional options and extension payments "
                            "when the rolling cash forecast falls below "
                            "the funded $8,000 minimum reserve."
                        ),
                    ),
                ],
                "completion_gate": (
                    "All three canonical scenarios reconcile exactly; Base expense "
                    "categories total $292,900 without duplication. Escrow, purchase "
                    "price, and project capital are excluded from usable operating "
                    "cash. Any six-month funding deficit has a documented spending "
                    "reduction or committed funding response before further obligations."
                ),
            },
            {
                "worksheet_id": "ws-03",
                "number": 3,
                "title": "End-to-End Execution, Idempotent Ledger & QA Pre-Flight Sheet",
                "purpose": (
                    "Convert site origination into a reproducible evidence and "
                    "transaction process. Preserve document lineage, prevent duplicate "
                    "payments, reconcile signed obligations, and test buyer packages "
                    "before release. Keep parcel rights, utility conditions, revenue "
                    "events, and cash movements traceable through assignment "
                    "and post-closing obligations."
                ),
                "chapter_ref": "Q7, Q8",
                "instructions": [
                    (
                        "Define the lifecycle from raw lead through rejected, "
                        "optioned, studied, marketed, assigned, and archived states. "
                        "Attach entry requirements and an accountable owner to "
                        "each transition; never let a marketing label silently "
                        "upgrade the underlying utility evidence."
                    ),
                    (
                        "Assign stable identifiers to opportunities, parcels, "
                        "contracts, invoices, and payment events. Store the "
                        "original source separately from normalized records. "
                        "Use deterministic duplicate detection so repeated "
                        "imports update evidence rather than create extra "
                        "revenue, fees, or obligations."
                    ),
                    (
                        "Build an execution checklist covering title, access, "
                        "environmental screening, utility correspondence, zoning, "
                        "option notices, and assignment conditions. Sequence "
                        "nonrefundable payments after the relevant evidence "
                        "review whenever the negotiated contract permits "
                        "that ordering without forfeiting rights."
                    ),
                    (
                        "Reconcile the cash ledger to bank and escrow "
                        "statements before releasing a buyer package or "
                        "making a payment. Distinguish authorized commitments, "
                        "paid expenses, refundable deposits, earned receivables, "
                        "and contingent fees in separate ledger "
                        "states and reports."
                    ),
                    (
                        "Perform a second-person pre-flight check on the "
                        "commercial package and closing instructions. Resolve "
                        "capacity wording, document dates, signature authority, "
                        "wire verification, and incomplete obligations before "
                        "release; record the reviewer, evidence version, "
                        "and disposition of every exception."
                    ),
                ],
                "fields": [
                    field(
                        "Lifecycle states and evidence-based transitions",
                        "textarea",
                        (
                            "Define the opportunity states, required transition "
                            "evidence, responsible role, and allowed reversals. "
                            "Explain how a negative study, expired option, "
                            "or changed ordinance moves the project out "
                            "of an active marketing or execution state."
                        ),
                        (
                            "TX-BESS-014 moves from screened to optioned only "
                            "after countersignature and verified payment. It "
                            "moves to utility-reviewed after the dated study "
                            "is indexed, not after a queue submission. "
                            "A failed export assessment returns the record "
                            "to rejected, freezes extension reminders, and "
                            "withdraws the corresponding buyer package "
                            "from active distribution."
                        ),
                    ),
                    field(
                        "Stable identifiers and duplicate prevention key",
                        "textarea",
                        (
                            "Specify persistent keys for parcels, option "
                            "agreements, invoices, and cash events. Define "
                            "how amended documents relate to originals "
                            "and how the system distinguishes a repeated "
                            "delivery from a genuinely new "
                            "contractual obligation."
                        ),
                        (
                            "Use opportunity TX-BESS-014, contract OPT-014-v1, "
                            "and event OPT-014-INITIAL-FEE as distinct identifiers. "
                            "The $7,000 initial fee has one economic-event "
                            "key regardless of repeated invoice uploads. "
                            "Amendment OPT-014-v2 references v1 and creates "
                            "a new extension obligation only when its "
                            "signed terms actually authorize an "
                            "additional payment."
                        ),
                    ),
                    field(
                        "Source provenance and document integrity manifest",
                        "textarea",
                        (
                            "Record document origin, retrieval date, issuer, "
                            "effective date, revision, integrity hash, and "
                            "scope limitations. Explain which source controls "
                            "when a sales presentation conflicts with "
                            "a utility study, executed agreement, "
                            "or official land record."
                        ),
                        (
                            "The manifest links the utility-issued PDF, "
                            "its SHA-256 digest, study revision 3, and "
                            "the project identifier to the 20 MW "
                            "conditional campus tranche. A broker's slide "
                            "claiming 40 MW is retained as correspondence "
                            "but cannot overwrite the utility finding. "
                            "The discrepancy receives a named reviewer "
                            "and a corrected package revision."
                        ),
                    ),
                    field(
                        "Critical-path sequence and payment dependencies",
                        "textarea",
                        (
                            "List the next execution tasks, dependencies, "
                            "deadlines, and payment consequences. Distinguish "
                            "commercial target dates from contractual notice "
                            "deadlines and utility-controlled schedules, especially "
                            "where a missed date causes "
                            "irreversible option-fee burn."
                        ),
                        (
                            "Complete title review by day 7, obtain "
                            "the zoning response by day 12, and "
                            "submit the utility information request by "
                            "day 15. The option notice deadline is "
                            "day 45 under the illustrative agreement. "
                            "Send termination by the prescribed method "
                            "before that deadline if evidence cannot "
                            "support the next $3,500 extension."
                        ),
                    ),
                    field(
                        "Idempotent payment state and retry handling",
                        "textarea",
                        (
                            "Define payment authorization, submission, confirmation, "
                            "failure, and reconciliation states. Specify how "
                            "a timeout is investigated before retrying "
                            "and how the ledger prevents duplicate "
                            "wire instructions from creating "
                            "duplicate cash disbursements."
                        ),
                        (
                            "Payment OPT-014-INITIAL-FEE enters submitted "
                            "after the $7,000 wire request is "
                            "acknowledged. A portal timeout leaves the "
                            "event awaiting confirmation rather than failed. "
                            "The coordinator checks the bank reference "
                            "and title-company receipt before any retry. "
                            "A database uniqueness constraint blocks "
                            "a second posted disbursement for "
                            "the same economic-event key."
                        ),
                    ),
                    field(
                        "Cash, escrow, receivable, and commitment reconciliation",
                        "textarea",
                        (
                            "Reconcile each financial event to external "
                            "evidence and classify its accounting and "
                            "cash status separately. Explain how unpaid "
                            "milestones, restricted escrow, future extensions, "
                            "and collected assignment fees appear "
                            "without inflating available funds."
                        ),
                        (
                            "The ledger shows $6,000 restricted escrow "
                            "supported by the holder's statement, a "
                            "$3,500 future extension commitment, and "
                            "a $40,000 milestone receivable only after "
                            "its earning condition is documented. "
                            "Available cash includes neither escrow "
                            "nor the unpaid receivable. The bank "
                            "deposit and settlement statement support "
                            "the collected $95,000 assignment."
                        ),
                    ),
                    field(
                        "Buyer package technical and commercial pre-flight",
                        "textarea",
                        (
                            "List the required package components and "
                            "test every headline against its supporting "
                            "document. Include capacity limitations, estimated "
                            "upgrade costs, energization assumptions, option "
                            "expiry, assignability, parcel access, and "
                            "unresolved physical or "
                            "land-use constraints."
                        ),
                        (
                            "Package revision 5 contains the option "
                            "abstract, title exceptions, 20 MW "
                            "conditional utility study, $2.4 million "
                            "preliminary upgrade allocation, and October "
                            "2029 target. The reviewer removes "
                            "an unsupported 40 MW headline and "
                            "adds the shared-bridge fiber constraint. "
                            "The package index identifies every "
                            "remaining condition beside its "
                            "source document."
                        ),
                    ),
                    field(
                        "Closing funds verification and assignment delivery",
                        "textarea",
                        (
                            "Document closing prerequisites, independently "
                            "verified payment instructions, executed assignment "
                            "delivery, seller notices, and post-closing "
                            "recording responsibilities. State how changed "
                            "wire details or an incomplete "
                            "signature package stop "
                            "funds release."
                        ),
                        (
                            "Before the $95,000 assignment closes, "
                            "the coordinator confirms title-company "
                            "wire details using a previously "
                            "verified telephone number. Closing "
                            "requires the signed assignment, required "
                            "seller notice, buyer acceptance of "
                            "remaining utility conditions, and the "
                            "settlement statement. An emailed bank "
                            "change stops payment until independent "
                            "verification and documented authorization "
                            "are complete."
                        ),
                    ),
                    field(
                        "Exception repair and immutable correction trail",
                        "textarea",
                        (
                            "Describe how errors are detected, "
                            "assigned, corrected, and communicated. Preserve "
                            "original entries and document why "
                            "the correction occurred, including whether "
                            "previous recipients need replacement "
                            "materials or financial "
                            "records require reversal."
                        ),
                        (
                            "A duplicated $3,500 extension invoice "
                            "is flagged by contract and "
                            "milestone matching. The duplicate "
                            "record is marked void with "
                            "a reason and reviewer identity; "
                            "the original remains intact. If "
                            "a buyer received an outdated "
                            "utility summary, send the corrected "
                            "revision directly and record "
                            "receipt rather than silently "
                            "replacing the stored file."
                        ),
                    ),
                    field(
                        "Post-closing obligations and operational acceptance",
                        "textarea",
                        (
                            "Identify obligations surviving assignment, "
                            "their owners, due dates, evidence "
                            "requirements, and financial consequences. "
                            "Separate completed transfers from "
                            "ongoing milestone services, contingent "
                            "carry interests, and unresolved "
                            "escrow or "
                            "recording matters."
                        ),
                        (
                            "After assignment, the operator "
                            "must deliver the final utility "
                            "correspondence archive within five "
                            "business days and confirm seller "
                            "notice delivery. A separately "
                            "contracted $40,000 milestone remains "
                            "contingent on its specified "
                            "deliverable. The closing checklist "
                            "does not mark that payment "
                            "earned merely because the "
                            "$95,000 assignment proceeds "
                            "have arrived."
                        ),
                    ),
                ],
                "completion_gate": (
                    "A reviewer other than the preparer verifies the current "
                    "package, unique financial-event keys, reconciled bank and "
                    "escrow balances, authorized signatures, independently checked "
                    "wire instructions, and surviving obligations. No unresolved "
                    "capacity misstatement or duplicate payment event remains "
                    "in the release package."
                ),
            },
            {
                "worksheet_id": "ws-04",
                "number": 4,
                "title": "Statutory, Licensing, Contract Addendum & Compliance Audit",
                "purpose": (
                    "Translate jurisdiction-specific requirements into evidence, "
                    "contract terms, and operating responsibilities. Distinguish "
                    "principal trading from brokerage, load service from "
                    "generation interconnection, and screening from permitting. "
                    "Identify objective legal triggers without implying that "
                    "site control alone establishes utility service "
                    "or development permission."
                ),
                "chapter_ref": "Q5, Q9",
                "instructions": [
                    (
                        "Identify the state, county, municipality, "
                        "utility territory, and applicable market "
                        "before selecting requirements. Retrieve current "
                        "primary authorities and adopted local "
                        "codes; record effective dates rather "
                        "than assuming a neighboring jurisdiction "
                        "uses the same rules "
                        "or exemptions."
                    ),
                    (
                        "Have transaction counsel classify the "
                        "actual conduct and compensation structure "
                        "under state real-estate licensing law. "
                        "Document the operator's genuine option "
                        "interest or engage a properly "
                        "licensed broker where required; "
                        "contract labels alone do "
                        "not establish "
                        "an exemption."
                    ),
                    (
                        "Separate federal transmission and "
                        "interconnection requirements from utility "
                        "retail-load procedures and state "
                        "siting rules. Identify the governing "
                        "tariff and service agreement "
                        "for each project; a "
                        "storage market participation rule "
                        "does not allocate physical "
                        "substation "
                        "headroom."
                    ),
                    (
                        "Translate diligence findings into "
                        "specific option and assignment "
                        "clauses covering access, testing, "
                        "notice, extensions, assignment, title "
                        "cure, utility uncertainty, and "
                        "termination. Negotiate obligations "
                        "against actual evidence and "
                        "deadlines instead of relying "
                        "on broad commercial "
                        "assurances."
                    ),
                    (
                        "Maintain a requirement register "
                        "with citation, applicability rationale, "
                        "responsible specialist, evidence, and "
                        "next action. Recheck municipal "
                        "moratoriums, code amendments, and "
                        "utility tariff changes before "
                        "extensions or buyer-package release; "
                        "retain the dated source "
                        "supporting each "
                        "decision."
                    ),
                ],
                "fields": [
                    field(
                        "Principal interest and brokerage licensing analysis",
                        "textarea",
                        (
                            "Describe what the operator "
                            "owns, whose interests they "
                            "represent, and how compensation "
                            "is earned. Identify state "
                            "licensing provisions and the "
                            "facts counsel must resolve "
                            "before owner solicitation, "
                            "marketing, or "
                            "assignment."
                        ),
                        (
                            "For an illustrative Texas "
                            "transaction, counsel reviews Tex. "
                            "Occ. Code §§ 1101.002, "
                            "1101.0045, and 1101.351. "
                            "The operator holds an "
                            "executed option and discloses "
                            "the nature of that "
                            "interest. If actual activities "
                            "constitute brokerage outside "
                            "applicable exceptions, a "
                            "licensed broker performs "
                            "that work under a "
                            "written engagement."
                        ),
                    ),
                    field(
                        "Utility jurisdiction, tariffs, and interconnection pathway",
                        "textarea",
                        (
                            "Identify whether the project "
                            "needs retail load service, "
                            "generation interconnection, storage import "
                            "and export arrangements, or "
                            "multiple pathways. Cite relevant "
                            "jurisdictional authority while "
                            "recording the actual "
                            "utility tariff "
                            "and process."
                        ),
                        (
                            "The federal jurisdiction review "
                            "starts with 16 U.S.C. "
                            "§ 824(b)(1), with tariff "
                            "issues assessed under §§ "
                            "824d and 824e where "
                            "applicable. FERC Order No. "
                            "2023 concerns generator "
                            "interconnection reforms, not "
                            "automatic campus load "
                            "entitlement. The utility "
                            "must identify the "
                            "specific service pathway "
                            "and governing agreements."
                        ),
                    ),
                    field(
                        "Storage market rules versus physical service rights",
                        "textarea",
                        (
                            "Identify applicable storage "
                            "participation rules, market "
                            "operator procedures, and "
                            "utility service requirements. "
                            "Explain which approvals "
                            "address market access "
                            "and which establish "
                            "physical charging, export, "
                            "protection, or "
                            "operating conditions."
                        ),
                        (
                            "FERC Order No. 841 "
                            "and 18 CFR "
                            "§ 35.28(g)(9) address "
                            "electric storage participation "
                            "in covered organized "
                            "wholesale markets. They "
                            "do not grant a "
                            "12-acre parcel 20 MW "
                            "of charging or "
                            "export capacity. The "
                            "project still requires "
                            "the applicable utility "
                            "studies, agreements, "
                            "protection settings, and "
                            "operating restrictions."
                        ),
                    ),
                    field(
                        "Zoning authority, moratorium, and land-use evidence",
                        "textarea",
                        (
                            "Record the current "
                            "zoning designation, permitted "
                            "use classification, special "
                            "approvals, moratorium status, "
                            "and hearing requirements. "
                            "Identify the governing "
                            "local text and "
                            "distinguish staff interpretation "
                            "from an enacted "
                            "ordinance or "
                            "issued permit."
                        ),
                        (
                            "For a Texas municipal "
                            "site, Tex. Loc. "
                            "Gov't Code § 211.003 "
                            "provides relevant zoning "
                            "authority, while the "
                            "adopted ordinance determines "
                            "parcel-specific use rules. "
                            "Record the current "
                            "district, storage classification, "
                            "setbacks, and hearing "
                            "schedule. A staff "
                            "email cannot override "
                            "an enacted BESS "
                            "moratorium covering "
                            "the property."
                        ),
                    ),
                    field(
                        "Wetlands, floodplain, and environmental review triggers",
                        "textarea",
                        (
                            "Identify environmental screening "
                            "sources, fieldwork needs, "
                            "permit triggers, and "
                            "federal involvement. Separate "
                            "mapped indicators from "
                            "jurisdictional determinations and "
                            "explain which findings "
                            "require redesign, agency "
                            "consultation, additional "
                            "studies, or "
                            "termination."
                        ),
                        (
                            "A National Wetlands "
                            "Inventory overlay triggers "
                            "field review rather "
                            "than a definitive "
                            "jurisdiction finding. Proposed "
                            "discharges into covered "
                            "waters may require "
                            "authorization under Clean "
                            "Water Act § 404, "
                            "33 U.S.C. § 1344, "
                            "and 33 CFR "
                            "Parts 323 and "
                            "328. FEMA mapping "
                            "informs separate local "
                            "floodplain and "
                            "drainage review."
                        ),
                    ),
                    field(
                        "Species, cultural resources, and federal nexus",
                        "textarea",
                        (
                            "Record potential protected "
                            "species, cultural-resource concerns, "
                            "federal permits, and "
                            "funding connections. Identify "
                            "the distinct statutory "
                            "triggers and responsible "
                            "specialists without assuming "
                            "every private option "
                            "requires the same "
                            "federal review "
                            "process."
                        ),
                        (
                            "A potential federal "
                            "wetlands permit prompts "
                            "review of Endangered "
                            "Species Act consultation "
                            "under 16 U.S.C. "
                            "§ 1536 and "
                            "historic-preservation review "
                            "under 54 U.S.C. "
                            "§ 306108 where "
                            "applicable. Separately assess "
                            "prohibited take under "
                            "16 U.S.C. § 1538. "
                            "Specialists define survey "
                            "scope before the "
                            "next nonrefundable "
                            "option extension."
                        ),
                    ),
                    field(
                        "BESS fire code, emergency access, and adopted standards",
                        "textarea",
                        (
                            "Identify the locally "
                            "adopted fire-code edition, "
                            "storage provisions, applicable "
                            "standards, emergency-access requirements, "
                            "and reviewing authority. "
                            "Distinguish enforceable adopted "
                            "requirements from engineering "
                            "references and manufacturer "
                            "test documentation "
                            "used during "
                            "design review."
                        ),
                        (
                            "The fire official "
                            "confirms the jurisdiction's "
                            "adopted International Fire "
                            "Code edition and "
                            "applicable energy-storage provisions, "
                            "including Section 1207 "
                            "where adopted. Engineering "
                            "checks NFPA 855 "
                            "applicability and UL "
                            "9540A test documentation. "
                            "The 12-acre layout "
                            "reserves verified emergency "
                            "access and separation "
                            "distances before "
                            "usable acreage "
                            "is marketed."
                        ),
                    ),
                    field(
                        "Title, mineral rights, access, and recorded notice",
                        "textarea",
                        (
                            "Document title exceptions, "
                            "surface-use conflicts, mineral "
                            "rights, legal access, "
                            "easements, and recording "
                            "strategy. Identify which "
                            "rights must be "
                            "cured or subordinated "
                            "and whether recording "
                            "a memorandum is "
                            "permitted and "
                            "commercially appropriate."
                        ),
                        (
                            "The title commitment "
                            "reveals a mineral "
                            "reservation and a "
                            "pipeline easement crossing "
                            "the proposed battery "
                            "pad. Counsel evaluates "
                            "surface protections and "
                            "a revised layout. "
                            "The option expressly "
                            "addresses any permitted "
                            "memorandum recording and "
                            "release on termination. "
                            "An equitable option "
                            "interest does not "
                            "erase prior liens "
                            "or access "
                            "defects."
                        ),
                    ),
                    field(
                        "Utility contingency and assignment contract addendum",
                        "textarea",
                        (
                            "Draft the commercial "
                            "instructions for clauses "
                            "covering evidence standards, "
                            "utility timing, cost "
                            "ceilings, assignment, notices, "
                            "and termination. State "
                            "which amounts remain "
                            "nonrefundable and who "
                            "bears deposits or "
                            "upgrade obligations "
                            "after transfer."
                        ),
                        (
                            "Proposed business terms "
                            "permit termination before "
                            "the next extension "
                            "if the utility "
                            "cannot support the "
                            "specified 20 MW "
                            "phase by the "
                            "buyer's deadline or "
                            "allocated upgrades exceed "
                            "$3 million. The "
                            "$7,000 initial fee "
                            "remains nonrefundable. "
                            "Assignment transfers only "
                            "the rights actually "
                            "held; utility agreement "
                            "transfer requirements "
                            "remain separately "
                            "applicable."
                        ),
                    ),
                    field(
                        "Requirement register and dated audit sign-off",
                        "textarea",
                        (
                            "List each applicable "
                            "requirement with its "
                            "citation, source date, "
                            "reviewer, evidence, unresolved "
                            "action, and next "
                            "review event. Define "
                            "which changes require "
                            "updated underwriting or "
                            "withdrawal of "
                            "previous buyer "
                            "materials."
                        ),
                        (
                            "The register assigns "
                            "licensing analysis to "
                            "transaction counsel, utility "
                            "tariff review to "
                            "the power consultant, "
                            "and fire-code confirmation "
                            "to the engineer. "
                            "Recheck all three "
                            "before the $3,500 "
                            "extension. A new "
                            "municipal storage restriction "
                            "immediately pauses marketing "
                            "and triggers a "
                            "documented option "
                            "termination or "
                            "redesign decision."
                        ),
                    ),
                ],
                "completion_gate": (
                    "Qualified reviewers resolve jurisdiction, licensing treatment, "
                    "actual utility pathway, current land-use restrictions, environmental "
                    "triggers, adopted fire requirements, and title exceptions. The "
                    "signed option reflects negotiated assignment and termination "
                    "rights, and every capacity statement preserves the utility's "
                    "documented conditions."
                ),
            },
            {
                "worksheet_id": "ws-05",
                "number": 5,
                "title": "Automation Pipeline, Acquisition Flywheel & Risk Fallback Tracker",
                "purpose": (
                    "Automate repeatable screening and evidence handling without "
                    "automating unsupported power claims or irreversible commitments. "
                    "Connect parcel discovery, utility research, developer demand, "
                    "and disciplined follow-up. Track stale sources, concentration, "
                    "failed-site learning, and manual fallbacks so software "
                    "increases throughput without increasing option-fee losses."
                ),
                "chapter_ref": "Q6, Q10",
                "instructions": [
                    (
                        "Define authoritative sources and "
                        "permitted retrieval methods before "
                        "building ingestion. Record update "
                        "cadence, geographic coverage, and "
                        "field definitions. Treat public "
                        "queue entries and hosting-capacity "
                        "maps as screening inputs "
                        "rather than contracts for "
                        "deliverable "
                        "power."
                    ),
                    (
                        "Separate automated ranking from "
                        "human investment decisions. Let "
                        "software flag distance, acreage, "
                        "flood exposure, deadlines, and "
                        "document gaps; require named "
                        "reviewers to interpret utility "
                        "conditions, approve cash commitments, "
                        "and authorize outward-facing "
                        "commercial "
                        "claims."
                    ),
                    (
                        "Build a source-to-decision trail "
                        "for every scored feature "
                        "and derived conclusion. Store "
                        "retrieval timestamps and data "
                        "versions so a changed "
                        "utility map, parcel boundary, "
                        "or municipal ordinance can "
                        "invalidate affected opportunity "
                        "records "
                        "automatically."
                    ),
                    (
                        "Design acquisition around specific "
                        "developer mandates and owner "
                        "situations rather than undifferentiated "
                        "lead volume. Feed rejection "
                        "reasons back into screening "
                        "weights while maintaining separate "
                        "cohorts for BESS parcels "
                        "and AI campus "
                        "development "
                        "requirements."
                    ),
                    (
                        "Test failure handling before "
                        "expanding automation. Simulate missing "
                        "feeds, duplicate imports, stale "
                        "study summaries, changed payment "
                        "instructions, and overdue options. "
                        "Assign a manual fallback "
                        "and recovery deadline to "
                        "each event that "
                        "could consume "
                        "cash."
                    ),
                ],
                "fields": [
                    field(
                        "Source inventory and ingestion schedule",
                        "textarea",
                        (
                            "List parcel, transmission, "
                            "queue, hosting-capacity, flood, "
                            "wetland, zoning, and "
                            "fiber sources. Define "
                            "retrieval permission, update "
                            "cadence, coverage limitations, "
                            "and the source "
                            "owner responsible for "
                            "resolving conflicting "
                            "or stale "
                            "records."
                        ),
                        (
                            "Use county GIS "
                            "for parcel geometry, "
                            "the relevant ISO "
                            "portal for queue "
                            "status, utility publications "
                            "for available screening "
                            "layers, FEMA for "
                            "flood mapping, and "
                            "USFWS for wetland "
                            "indicators. Refresh queue "
                            "records weekly where "
                            "permitted and ordinances "
                            "before commitments. "
                            "Carrier route confirmation "
                            "requires direct provider "
                            "evidence, not a "
                            "crowdsourced line "
                            "alone."
                        ),
                    ),
                    field(
                        "GIS ranking and voltage-corridor feature definitions",
                        "textarea",
                        (
                            "Define spatial ranking "
                            "features, distance methods, "
                            "coordinate reference systems, "
                            "and exclusions. Explain "
                            "how the 69kV–345kV "
                            "screen identifies research "
                            "candidates without converting "
                            "line proximity or "
                            "substation location "
                            "into an "
                            "available-MW estimate."
                        ),
                        (
                            "QGIS ranks a "
                            "12-acre storage parcel "
                            "0.8 miles from "
                            "a 138 kV "
                            "substation using an "
                            "appropriate projected coordinate "
                            "system. The score "
                            "means attractive for "
                            "utility inquiry only. "
                            "No MW premium "
                            "is assigned from "
                            "distance. Crossing rights, "
                            "protection design, queue "
                            "interactions, and utility "
                            "study results remain "
                            "separate unresolved "
                            "features."
                        ),
                    ),
                    field(
                        "Separate BESS and AI campus scoring models",
                        "textarea",
                        (
                            "Specify distinct feature "
                            "sets and rejection "
                            "rules for storage "
                            "and computing. Identify "
                            "shared evidence that "
                            "can be reused "
                            "and critical constraints "
                            "that must never "
                            "be inherited "
                            "between the "
                            "two models."
                        ),
                        (
                            "The BESS model "
                            "screens 5–25-acre parcels "
                            "for access, setbacks, "
                            "drainage, import capability, "
                            "and export pathway. "
                            "The campus model "
                            "adds phased load "
                            "service, diverse dark-fiber "
                            "routes, cooling resources, "
                            "and local computing-use "
                            "rules. A strong "
                            "storage score does "
                            "not transfer the "
                            "parcel into the "
                            "campus shortlist "
                            "without those "
                            "additional findings."
                        ),
                    ),
                    field(
                        "Automation confidence and human verification rules",
                        "textarea",
                        (
                            "Define which extracted "
                            "facts software may "
                            "populate, which require "
                            "review, and which "
                            "actions remain manual. "
                            "Specify confidence thresholds "
                            "and evidence requirements "
                            "for utility numbers, "
                            "contract dates, "
                            "and monetary "
                            "obligations."
                        ),
                        (
                            "Document extraction proposes "
                            "the 20 MW "
                            "study figure, $2.4 "
                            "million upgrade estimate, "
                            "and October 2029 "
                            "target. A reviewer "
                            "checks the original "
                            "pages and conditions "
                            "before acceptance. Software "
                            "may schedule reminders, "
                            "but it cannot "
                            "sign the option, "
                            "send a wire, "
                            "or publish a "
                            "capacity claim "
                            "without authorized "
                            "human action."
                        ),
                    ),
                    field(
                        "Developer mandate library and buyer matching",
                        "textarea",
                        (
                            "Record each developer's "
                            "acreage, utility territory, "
                            "MW range, timing, "
                            "capital readiness, and "
                            "technical exclusions. Explain "
                            "how matching uses "
                            "documented site attributes "
                            "rather than optimistic "
                            "future upgrades "
                            "or unsupported "
                            "capacity assumptions."
                        ),
                        (
                            "Buyer B-07 seeks "
                            "10–25-acre storage parcels "
                            "with a credible "
                            "20 MW export "
                            "pathway and utility "
                            "timing within its "
                            "investment window. Buyer "
                            "D-03 requires 20 MW "
                            "initial campus service "
                            "and diverse fiber. "
                            "The shared-bridge campus "
                            "fails D-03 matching "
                            "until carrier evidence "
                            "establishes genuine "
                            "route diversity."
                        ),
                    ),
                    field(
                        "Owner acquisition sequence and contact economics",
                        "textarea",
                        (
                            "Define targeted owner "
                            "outreach, verified contact "
                            "sources, follow-up intervals, "
                            "response tracking, and "
                            "cost per qualified "
                            "conversation. Preserve clear "
                            "principal-interest disclosures and "
                            "avoid claiming buyer "
                            "or utility "
                            "commitments that "
                            "do not "
                            "exist."
                        ),
                        (
                            "A pilot reviews "
                            "100 parcels, identifies "
                            "30 owners matching "
                            "current buyer mandates, "
                            "and sends 20 "
                            "individualized letters after "
                            "ownership checks. Four "
                            "qualified conversations from "
                            "$400 direct outreach "
                            "cost equal $100 "
                            "per qualified conversation. "
                            "The letter describes "
                            "an interest in "
                            "negotiating an option, "
                            "not an existing "
                            "utility allocation "
                            "or committed "
                            "sale."
                        ),
                    ),
                    field(
                        "Evidence freshness and invalidation policy",
                        "textarea",
                        (
                            "Set review intervals "
                            "for each source "
                            "class and define "
                            "events that invalidate "
                            "a prior conclusion. "
                            "Explain how stale "
                            "records affect ranking, "
                            "marketing eligibility, option "
                            "extensions, and "
                            "buyer follow-up "
                            "tasks."
                        ),
                        (
                            "Queue and ordinance "
                            "checks run before "
                            "every extension and "
                            "buyer-package release. A "
                            "new utility restudy "
                            "notice marks the "
                            "20 MW capacity "
                            "summary for revalidation "
                            "and pauses affected "
                            "outreach. The system "
                            "keeps the earlier "
                            "study for history "
                            "but removes it "
                            "from the current "
                            "evidence set "
                            "until a "
                            "reviewer resolves "
                            "the change."
                        ),
                    ),
                    field(
                        "Pipeline fallbacks and outage response",
                        "textarea",
                        (
                            "Describe the manual "
                            "fallback for unavailable "
                            "feeds, corrupted geometry, "
                            "document extraction failures, "
                            "and missed reminders. "
                            "Assign an owner "
                            "and recovery deadline "
                            "while preserving contractual "
                            "notice dates "
                            "and preventing "
                            "unreviewed spending."
                        ),
                        (
                            "If the utility "
                            "portal fails for "
                            "48 hours, the "
                            "coordinator contacts the "
                            "known utility representative "
                            "and records the "
                            "response. A separate "
                            "calendar retains the "
                            "option notice deadline. "
                            "No extension is "
                            "paid merely because "
                            "the feed is "
                            "unavailable; the principal "
                            "decides using current "
                            "evidence, contractual "
                            "rights, and "
                            "remaining reserve."
                        ),
                    ),
                    field(
                        "Concentration limits and correlated failure tracker",
                        "textarea",
                        (
                            "Measure exposure by "
                            "utility, substation, municipality, "
                            "developer, and option "
                            "expiry month. Define "
                            "a cash-based concentration "
                            "limit and explain "
                            "how shared upgrades "
                            "or zoning actions "
                            "can cause "
                            "several opportunities "
                            "to fail "
                            "together."
                        ),
                        (
                            "Three options near "
                            "one substation each "
                            "require $7,000, creating "
                            "$21,000 correlated acquisition "
                            "exposure before diligence. "
                            "Against $40,000 startup "
                            "capital, that concentration "
                            "is 52.5%. The "
                            "pilot caps initial "
                            "option fees in "
                            "one substation area "
                            "at $14,000 and "
                            "requires a separate "
                            "utility territory "
                            "before adding "
                            "another correlated "
                            "commitment."
                        ),
                    ),
                    field(
                        "Learning loop and automation investment return",
                        "textarea",
                        (
                            "Record rejection reasons, "
                            "hours saved, verification "
                            "errors, software costs, "
                            "and changes in "
                            "option-fee losses. Define "
                            "the evidence required "
                            "to keep an "
                            "automation feature rather "
                            "than rewarding "
                            "lead volume "
                            "without economic "
                            "benefit."
                        ),
                        (
                            "A zoning-change monitor "
                            "costs $180 monthly "
                            "and saves six "
                            "review hours valued "
                            "internally at $50 "
                            "per hour, yielding "
                            "$120 monthly net "
                            "time value. Record "
                            "avoided $3,500 extensions "
                            "separately and only "
                            "when documented. Do "
                            "not count the "
                            "same saved labor "
                            "again as additional "
                            "cash profit in "
                            "the canonical "
                            "scorecard."
                        ),
                    ),
                ],
                "completion_gate": (
                    "Every automated score has traceable inputs, separate BESS "
                    "and campus logic, current evidence status, and a manual "
                    "fallback. Payment, contract execution, and external capacity "
                    "claims remain controlled actions. The pilot demonstrates "
                    "measured time savings or loss reduction without increasing "
                    "unreviewed cash exposure."
                ),
            },
            {
                "worksheet_id": "ws-06",
                "number": 6,
                "title": "30-Day Launch Sprint, Pod KPI Scorecard & Exit-Readiness Ledger",
                "purpose": (
                    "Launch a small-team origination operation with measurable "
                    "evidence production, controlled spending, and realistic closing "
                    "expectations. Connect the first thirty days to the "
                    "two-to-six-month first-deal window, canonical staffing, and "
                    "transfer-ready records. Measure decision quality and collected "
                    "economics rather than speculative project value."
                ),
                "chapter_ref": "Q11, Q12",
                "instructions": [
                    (
                        "Set a thirty-day launch "
                        "objective around qualified "
                        "opportunities, verified utility "
                        "pathways, and executable "
                        "processes rather than "
                        "promised closings. The "
                        "canonical first-deal window "
                        "is two to six "
                        "months, so fund "
                        "the selected operating "
                        "pace "
                        "accordingly."
                    ),
                    (
                        "Assign one accountable "
                        "owner for every "
                        "deliverable and clarify "
                        "contractor scopes. Use "
                        "the Conservative and "
                        "Base staffing structure "
                        "of one full-time "
                        "operator plus three "
                        "contractors before designing "
                        "the two-full-time, "
                        "four-contractor scaled "
                        "pod "
                        "structure."
                    ),
                    (
                        "Track both leading "
                        "indicators and cash "
                        "outcomes. Separate screened "
                        "parcels, qualified conversations, "
                        "utility responses, signed "
                        "options, assignments, and "
                        "collected fees; none "
                        "of these stages "
                        "can substitute "
                        "for another in "
                        "the performance "
                        "scorecard."
                    ),
                    (
                        "Run a weekly "
                        "cash and evidence "
                        "review that examines "
                        "reserve coverage, upcoming "
                        "notices, failed-option burn, "
                        "buyer concentration, and "
                        "unresolved technical findings. "
                        "Document stop, continue, "
                        "or revise decisions "
                        "before the "
                        "next nonrefundable "
                        "commitment becomes "
                        "due."
                    ),
                    (
                        "Maintain an exit-ready "
                        "ledger from the "
                        "first option rather "
                        "than reconstructing history "
                        "during a sale. "
                        "Preserve transfer restrictions, "
                        "source evidence, accounting "
                        "support, surviving obligations, "
                        "and access permissions "
                        "so another operator "
                        "can evaluate "
                        "the business "
                        "accurately."
                    ),
                ],
                "fields": [
                    field(
                        "Day 1–7 market selection and operating setup",
                        "textarea",
                        (
                            "Choose a narrow "
                            "initial geography, utility "
                            "territory, buyer mandate, "
                            "and use case. "
                            "List setup deliverables, "
                            "responsible people, spending "
                            "limits, and the "
                            "minimum evidence needed "
                            "before beginning "
                            "owner outreach "
                            "or option "
                            "negotiation."
                        ),
                        (
                            "During week one, "
                            "select one utility "
                            "territory and prioritize "
                            "5–25-acre BESS sites. "
                            "Interview three developers, "
                            "retain transaction counsel, "
                            "configure the evidence "
                            "register, and verify "
                            "the title-company contact. "
                            "Limit setup spending "
                            "to the planned "
                            "$2,000. Do not "
                            "broaden into campus "
                            "origination until fiber, "
                            "cooling, and load-service "
                            "review capacity "
                            "is available."
                        ),
                    ),
                    field(
                        "Day 8–14 sourcing and preliminary qualification",
                        "textarea",
                        (
                            "Set a parcel-screening "
                            "target, owner-contact target, "
                            "and buyer-feedback target. "
                            "Identify the expected "
                            "output of each "
                            "activity and distinguish "
                            "research-qualified prospects from "
                            "sites with documented "
                            "utility capacity "
                            "or executed "
                            "control."
                        ),
                        (
                            "By day 14, "
                            "screen 100 parcels, "
                            "identify 30 mandate-aligned "
                            "owners, send 20 "
                            "targeted letters, and "
                            "hold four qualified "
                            "conversations. Produce ten "
                            "desktop summaries and "
                            "three utility inquiry "
                            "packages. These targets "
                            "measure research throughput; "
                            "none establishes deliverable "
                            "MW, a signed "
                            "option, or "
                            "recognized fee "
                            "revenue."
                        ),
                    ),
                    field(
                        "Day 15–21 diligence and conditional site control",
                        "textarea",
                        (
                            "Define the evidence "
                            "required before negotiating "
                            "or funding an "
                            "option. Assign utility, "
                            "title, zoning, access, "
                            "and engineering tasks "
                            "while preserving the "
                            "startup allocation and "
                            "the right "
                            "to reject "
                            "an unsuitable "
                            "parcel."
                        ),
                        (
                            "Advance two shortlisted "
                            "parcels to title "
                            "and zoning checks "
                            "and seek written "
                            "utility process guidance. "
                            "The $14,000 initial "
                            "option budget permits "
                            "two $7,000 fees "
                            "only after authority "
                            "and fatal-flaw review. "
                            "If utility evidence "
                            "remains inadequate, negotiate "
                            "a later funding "
                            "date or decline "
                            "the option "
                            "rather than "
                            "spending to "
                            "meet a "
                            "calendar target."
                        ),
                    ),
                    field(
                        "Day 22–30 package testing and launch decision",
                        "textarea",
                        (
                            "Specify the buyer-package "
                            "test, operational rehearsal, "
                            "reserve review, and "
                            "day-thirty decision. Explain "
                            "how the team "
                            "will proceed when "
                            "studies remain incomplete "
                            "without converting the "
                            "launch milestone "
                            "into a "
                            "forced closing "
                            "deadline."
                        ),
                        (
                            "By day 30, "
                            "complete one reviewed "
                            "sample package, test "
                            "duplicate-payment prevention, and "
                            "reconcile escrow. Obtain "
                            "feedback from three "
                            "mandate-matched developers. If "
                            "utility findings remain "
                            "pending, label the "
                            "opportunity accordingly and "
                            "retain the two-to-six-month "
                            "first-deal assumption. Continue "
                            "only at a "
                            "burn rate supported "
                            "by actual "
                            "unrestricted cash "
                            "and committed "
                            "funding."
                        ),
                    ),
                    field(
                        "Pod role charter and contractor capacity",
                        "textarea",
                        (
                            "Allocate sourcing, utility "
                            "analysis, GIS, transaction "
                            "documentation, bookkeeping, and "
                            "review responsibilities across "
                            "the canonical team. "
                            "Identify outsourced specialist "
                            "work, scope boundaries, "
                            "and capacity limits "
                            "that trigger "
                            "a staffing "
                            "change."
                        ),
                        (
                            "The Base pod "
                            "uses 1 FT "
                            "principal and 3 C: "
                            "a GIS researcher, "
                            "a power consultant, "
                            "and transaction counsel. "
                            "The principal owns "
                            "cash and buyer "
                            "decisions; outside title "
                            "and bookkeeping services "
                            "are scoped vendors. "
                            "Scaled staffing becomes "
                            "2 FT + "
                            "4 C, six "
                            "people, without relabeling "
                            "construction crews "
                            "as operator "
                            "headcount."
                        ),
                    ),
                    field(
                        "Leading indicators and conversion denominator definitions",
                        "textarea",
                        (
                            "Define each KPI "
                            "with numerator, denominator, "
                            "time window, evidence "
                            "source, and accountable "
                            "owner. Separate initial "
                            "screening, utility-validated underwriting, "
                            "option control, buyer "
                            "acceptance, and closing "
                            "so conversion "
                            "figures remain "
                            "interpretable."
                        ),
                        (
                            "Four qualified owner "
                            "conversations from 20 "
                            "targeted letters produce "
                            "a 20% conversation "
                            "rate. Two executed "
                            "options from four "
                            "qualified conversations produce "
                            "a 50% option "
                            "conversion rate if "
                            "both actually sign. "
                            "Report utility-study completion "
                            "separately. A submitted "
                            "request cannot be "
                            "counted as "
                            "utility validation "
                            "or added "
                            "to documented "
                            "MW."
                        ),
                    ),
                    field(
                        "Cash KPIs, option burn, and canonical performance",
                        "textarea",
                        (
                            "Track collected fees, "
                            "recognized revenue, reserve "
                            "coverage, expired option "
                            "fees, and owner "
                            "profit against the "
                            "canonical scenarios. Explain "
                            "which measures are "
                            "annual targets and "
                            "which are "
                            "current cash "
                            "facts requiring "
                            "immediate action."
                        ),
                        (
                            "The Base annual "
                            "reference remains $505,000 "
                            "revenue, $212,100 owner "
                            "profit, and 42.0% "
                            "margin. The expired-option "
                            "budget is $36,000. "
                            "At launch, report "
                            "actual collected revenue "
                            "as $0 until "
                            "a receipt occurs; "
                            "do not divide "
                            "the annual target "
                            "into assumed monthly "
                            "cash. Show the "
                            "$8,000 unrestricted "
                            "reserve beside "
                            "the funded "
                            "burn plan."
                        ),
                    ),
                    field(
                        "Weekly risk review and stop-spend decisions",
                        "textarea",
                        (
                            "Define the weekly "
                            "review agenda, decision "
                            "owners, escalation triggers, "
                            "and documented responses. "
                            "Include correlated utility "
                            "risk, municipal restrictions, "
                            "buyer withdrawal, expiring "
                            "options, and reserve "
                            "erosion before "
                            "authorizing additional "
                            "cash commitments."
                        ),
                        (
                            "Every Friday, review "
                            "the next 45 "
                            "days of notices "
                            "and cash obligations. "
                            "A restudy pushing "
                            "upgrades from $2.4 "
                            "million to $3.36 "
                            "million exceeds the "
                            "buyer's $3 million "
                            "limit. Pause the "
                            "$3,500 extension, obtain "
                            "the buyer's updated "
                            "decision, and exercise "
                            "the negotiated exit "
                            "right before "
                            "the notice "
                            "deadline if "
                            "economics fail."
                        ),
                    ),
                    field(
                        "Exit-readiness evidence and transferability ledger",
                        "textarea",
                        (
                            "Inventory contracts, option "
                            "rights, assignments, financial "
                            "records, utility evidence, "
                            "buyer mandates, operating "
                            "procedures, and access "
                            "permissions. Identify which "
                            "assets transfer freely "
                            "and which require "
                            "counterparty consent, "
                            "new engagement, "
                            "or restricted "
                            "disclosure."
                        ),
                        (
                            "The ledger lists "
                            "each option's expiry, "
                            "assignment clause, remaining "
                            "fees, title status, "
                            "and utility-study conditions. "
                            "A buyer of "
                            "the origination business "
                            "receives financial support "
                            "for the $95,000 "
                            "assignment, not unrestricted "
                            "access to confidential "
                            "developer records. Review "
                            "utility agreement transfer "
                            "conditions and "
                            "consultant reliance "
                            "rights before "
                            "promising transferable "
                            "project evidence."
                        ),
                    ),
                    field(
                        "Day-thirty decision and next-quarter operating mandate",
                        "textarea",
                        (
                            "Record the launch "
                            "decision, funded spending "
                            "ceiling, highest-priority evidence "
                            "gaps, next-quarter objectives, "
                            "and conditions for "
                            "scaling. Distinguish the "
                            "published candidate score "
                            "from demonstrated operating "
                            "results and "
                            "state what "
                            "must improve "
                            "before expansion."
                        ),
                        (
                            "Candidate #47 carries "
                            "a 92/100 Money-to-Manpower "
                            "Score and pipeline "
                            "rank #15 of "
                            "49; these are "
                            "selection metadata, not "
                            "collected earnings. The "
                            "day-thirty decision authorizes "
                            "only funded activity, "
                            "prioritizes utility responses "
                            "and qualified buyer "
                            "feedback, and defers "
                            "the scaled pod "
                            "until repeatable closings, "
                            "documented margins, "
                            "and adequate "
                            "working capital "
                            "are demonstrated."
                        ),
                    ),
                ],
                "completion_gate": (
                    "The principal records a day-thirty continue, revise, or "
                    "stop decision supported by actual cash, current evidence, "
                    "assigned roles, and dated next actions. KPI denominators "
                    "are auditable, canonical scenario totals remain unchanged, "
                    "and the transferability ledger distinguishes owned rights "
                    "from conditional or restricted project information."
                ),
            },
        ],
    }
