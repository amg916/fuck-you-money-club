from __future__ import annotations


def build_volume_045_workbook() -> dict:
    def field(name: str, input_type: str, prompt: str, example: str) -> dict:
        return {
            "name": name,
            "type": input_type,
            "prompt": prompt,
            "example": example,
        }

    return {
        "workbook_id": "wb-045-no-surprises-act-idr-and-medical-arbitration",
        "volume_id": "vol-045-no-surprises-act-idr-and-medical-arbitration",
        "title": (
            "No Surprises Act (IDR) Medical Arbitration & Out-of-Network Recovery "
            "— Operator Companion Workbook"
        ),
        "subtitle": (
            "6 Printable Operator Worksheets for Federal IDR Eligibility, "
            "Incremental-Cash Contingency Economics, Deadline Control, "
            "Evidence-Ready Arbitration, Recovery Automation, and Small-Team Scaling"
        ),
        "worksheets": [
            {
                "worksheet_id": "ws-01",
                "number": 1,
                "title": "Arbitrage Deal / Counterparty Underwriting & Spread Qualification",
                "purpose": (
                    "Qualify provider engagements before paying dispute fees or promising recovery. "
                    "Separate federal eligibility from state payment remedies, identify the actual "
                    "payer counterparty, establish initial-payment evidence, and test whether "
                    "collectible incremental proceeds justify casework, fee exposure, and the "
                    "operator's contracted contingency share."
                ),
                "chapter_ref": "Q1, Q2, Q6",
                "instructions": [
                    (
                        "Collect a representative, access-controlled sample of remittance records, "
                        "claim submissions, plan documents, facility participation evidence, and "
                        "provider agreements. Assign an internal claim identifier before reviewing "
                        "pricing, and record who supplied each document and when it was received."
                    ),
                    (
                        "Classify funding arrangement, service setting, network status, and applicable "
                        "payment law before estimating arbitration upside. Self-funded ERISA status "
                        "alone does not establish eligibility; examine the covered service, applicable "
                        "state mechanisms, and any state-law election supported by plan evidence."
                    ),
                    (
                        "Build the spread from cash above the payer's documented initial payment, "
                        "not from billed charges, the QPA alone, or the provider's entire account "
                        "balance. Deduct unrecovered dispute fees and attributable casework before "
                        "calculating the contracted operator share."
                    ),
                    (
                        "Underwrite payer behavior with dated collection cohorts rather than published "
                        "offer-selection percentages. Distinguish eligibility dismissals, unfavorable "
                        "determinations, favorable determinations awaiting payment, partial receipts, "
                        "and completed recoveries so the expected cash model preserves each failure "
                        "mode separately."
                    ),
                    (
                        "Authorize a small, documented pilot only after provider authority, jurisdiction, "
                        "deadline feasibility, and reserve funding are established. Keep ambiguous "
                        "claims outside the filing queue, name the person resolving each ambiguity, "
                        "and retain a reasoned rejection record for uneconomic claims."
                    ),
                ],
                "fields": [
                    field(
                        "Provider mandate and service perimeter",
                        "textarea",
                        (
                            "Identify the contracting provider, authorized signatory, participating "
                            "facilities, rendering specialties, and covered service dates. Describe "
                            "exactly which recovery activities the operator may perform and which "
                            "decisions remain with the provider or retained counsel."
                        ),
                        (
                            "Cedar Emergency Physicians authorizes a 60-claim emergency-medicine pilot "
                            "at two named hospitals for January service dates. The practice manager "
                            "supplies remittances; the physician owner approves offers. Authority covers "
                            "record preparation, negotiation administration, and permitted representative "
                            "submissions, but excludes patient collection and settlement outside written "
                            "provider instructions."
                        ),
                    ),
                    field(
                        "Plan funding and jurisdiction evidence",
                        "textarea",
                        (
                            "Record the funding arrangement, governing plan documents, insurer or "
                            "administrator identity, and relevant state payment mechanism. Explain "
                            "why the specific claim enters federal IDR rather than assuming every "
                            "commercial or ERISA-associated claim follows the same pathway."
                        ),
                        (
                            "Claim CED-104 identifies an employer-funded plan administered by a national "
                            "carrier. The summary plan description confirms self-funding; intake checks "
                            "for a relevant state-law election and other applicable payment mechanisms. "
                            "The reviewer records federal-route support under 42 U.S.C. § 300gg-111 "
                            "and 45 CFR § 149.510 before approving preparation."
                        ),
                    ),
                    field(
                        "Protected service and network facts",
                        "textarea",
                        (
                            "Document the service category, emergency status, facility participation, "
                            "provider participation, and any notice-and-consent material relevant to "
                            "coverage. Identify excluded service types or factual gaps that would "
                            "make a federal filing inappropriate despite a low initial payment."
                        ),
                        (
                            "CED-104 concerns emergency physician services at a hospital emergency "
                            "department, with an out-of-network rendering group. Records identify the "
                            "plan, patient encounter, and service category without relying on a generic "
                            "out-of-network flag. A separate ground-ambulance claim is excluded from "
                            "this federal IDR pilot and evaluated under its applicable payment route."
                        ),
                    ),
                    field(
                        "Initial payment, QPA, and patient responsibility",
                        "textarea",
                        (
                            "Separate payer cash, stated QPA, allowed amount, contractual adjustments, "
                            "and patient cost sharing using remittance evidence. Select a consistent "
                            "payer-payment basis for incremental recovery and prevent patient balances "
                            "or QPA figures from masquerading as actual initial receipts."
                        ),
                        (
                            "The ERA reports a $1,500 QPA and $300 patient responsibility; the payer "
                            "initially pays $1,200. The recovery ledger uses $1,200 as the initial "
                            "payer-cash baseline, preserves the $1,500 QPA separately, and excludes "
                            "patient payments from the contingency base. Any later determination is "
                            "normalized to the same payer-payment basis."
                        ),
                    ),
                    field(
                        "Collectible spread hypothesis",
                        "textarea",
                        (
                            "Estimate additional payer cash with a documented collection assumption, "
                            "then deduct unrecovered fees and attributable casework. Show the "
                            "contingency percentage and distinguish a screening estimate from earned "
                            "revenue, which requires actual cleared receipts and contractual entitlement."
                        ),
                        (
                            "The pilot targets $5,700 total payer cash against a $1,200 initial "
                            "payment, yielding $4,500 incremental cash. With an illustrative $115 "
                            "administrative fee, $185 casework cost, and a documented $600 entity-fee "
                            "refund, the distributable base is $4,200. A 25% share produces $1,050 "
                            "operator revenue only after the required receipts clear."
                        ),
                    ),
                    field(
                        "Counterparty payment behavior",
                        "textarea",
                        (
                            "Describe payer performance using completed cohorts with explicit "
                            "denominators, elapsed collection days, partial payments, and aged "
                            "determinations. Keep observed cash realization separate from favorable "
                            "offer selection so a persuasive brief does not become an assumed receipt."
                        ),
                        (
                            "A prior 40-case cohort contains 24 favorable determinations, eight "
                            "unfavorable determinations, four eligibility dismissals, and four pending "
                            "cases. Of the 24 favorable outcomes, 18 have full incremental receipts, "
                            "three have partial receipts, and three remain unpaid. The underwriting "
                            "model reports both 60% favorable outcomes and the separate collection distribution."
                        ),
                    ),
                    field(
                        "Evidence strength and offer support",
                        "textarea",
                        (
                            "List permissible evidence connecting the proposed offer to the actual "
                            "service, including clinical acuity, provider qualifications, and relevant "
                            "contracting history. Explain any benchmark's construction and exclude "
                            "prohibited billed-charge, usual-and-customary, and public-program payment comparisons."
                        ),
                        (
                            "CED-104 uses documented patient acuity, physician experience, the QPA, "
                            "and applicable contracting evidence. A FAIR Health report is screened "
                            "before use; its brand does not make every metric permissible. A "
                            "billed-charge percentile is excluded, while any retained permitted measure "
                            "must have an explained relationship to the service and offer."
                        ),
                    ),
                    field(
                        "Filing-window and cooling-period screen",
                        "textarea",
                        (
                            "Record initial-payment or denial receipt, negotiation initiation, "
                            "negotiation expiration, and federal filing deadline. Check prior "
                            "determinations involving the same parties and service category, and "
                            "separately assess batching eligibility under the rules applicable to the filing."
                        ),
                        (
                            "The calendar stores receipt as business-day zero, requires negotiation "
                            "initiation within the applicable 30-business-day window, then tracks the "
                            "30-business-day negotiation period and following four-business-day IDR "
                            "initiation window. A prior same-party determination triggers a separate "
                            "90-calendar-day suspension check; the reviewer documents treatment of any "
                            "affected subsequent claims and special filing window."
                        ),
                    ),
                    field(
                        "Fee-risk allocation and provider liquidity",
                        "textarea",
                        (
                            "Identify who advances administrative fees, entity deposits, and casework "
                            "costs, and who bears losses after dismissal or an unfavorable outcome. "
                            "Require written reserve funding rather than assuming successful claims "
                            "will immediately finance unsuccessful claims."
                        ),
                        (
                            "For ten separate illustrative disputes, the provider funds $1,150 in "
                            "administrative fees, $6,000 in entity deposits, and $1,850 in casework, "
                            "totaling $9,000. These are planning amounts, not current fee quotes. "
                            "The contract assigns unrecovered costs to the provider reserve and "
                            "prohibits spending one provider's balance on another provider's cases."
                        ),
                    ),
                    field(
                        "Pilot acceptance and rejection decision",
                        "textarea",
                        (
                            "State the minimum evidence, expected collectible contribution, reserve "
                            "coverage, and deadline slack required for acceptance. Name a decision "
                            "owner and record claim-level reasons for rejection, remediation, or "
                            "deferral without replacing statutory eligibility with a profitability score."
                        ),
                        (
                            "The pilot accepts 20 of 60 sampled claims: 15 have supported federal "
                            "eligibility and complete records, while five enter only after missing "
                            "plan evidence is resolved. Twenty-five state-route claims are redirected "
                            "and 15 expired or uneconomic claims are rejected. The owner signs the "
                            "claim list after the $18,000 illustrative reserve is funded."
                        ),
                    ),
                ],
                "completion_gate": (
                    "The provider and intake lead sign the accepted claim list, jurisdiction "
                    "memoranda, initial-payment baselines, deadline records, and funded reserve "
                    "schedule; unresolved eligibility claims remain outside the submission queue."
                ),
            },
            {
                "worksheet_id": "ws-02",
                "number": 2,
                "title": "Unit Economics, Escrow/Reserve Float & Working-Capital Calculator",
                "purpose": (
                    "Translate claim recoveries into earned operator shares without counting "
                    "provider collections as operator revenue. Model fee advances, refund timing, "
                    "casework deductions, loss cohorts, and collection delays, then reconcile annual "
                    "operating profit exactly to the canonical Conservative, Base, and Scaled scorecard."
                ),
                "chapter_ref": "Q3, Q4",
                "instructions": [
                    (
                        "Use separate columns for initial payer cash, additional payer cash, "
                        "administrative fees, entity deposits, entity refunds, and casework costs. "
                        "Keep client-owned reserve balances outside revenue, and do not describe "
                        "ordinary operating cash as escrow without an appropriate arrangement."
                    ),
                    (
                        "Calculate the contingency base as the greater of zero or incremental "
                        "cleared payer cash minus unrecovered dispute fees and contracted casework "
                        "costs. Apply the agreed share afterward, and carry unresolved cost recovery "
                        "according to the written provider agreement."
                    ),
                    (
                        "Use the illustrative fee amounts only to practice the worksheet. Before "
                        "funding an actual dispute, capture the current CMS administrative charge, "
                        "certified entity schedule, batch pricing, refund treatment, and payment "
                        "instructions from authoritative sources applicable to that filing."
                    ),
                    (
                        "Reconcile each provider settlement to bank evidence and distinguish "
                        "operator-paid costs from provider-funded pass-through amounts. A cost "
                        "deducted before the share calculation must not also reduce operator profit "
                        "unless the operator actually bears a separate expense."
                    ),
                    (
                        "Build a rolling 13-week cash forecast with delayed collections, eligibility "
                        "losses, and unreturned entity deposits. Preserve the canonical annual "
                        "scorecard as the comparison baseline while showing your actual operating "
                        "forecast separately whenever observed volumes or costs differ."
                    ),
                ],
                "fields": [
                    field(
                        "Incremental-cash waterfall",
                        "textarea",
                        (
                            "Write the complete receipt-to-share calculation using initial payer "
                            "cash as a separate baseline. Identify fee and casework deductions, "
                            "the zero floor, and the point at which the operator's contractual "
                            "share becomes earned and billable."
                        ),
                        (
                            "Total cleared payer cash is $5,700, including the original $1,200; "
                            "incremental cash is therefore $4,500. Subtract $115 administrative "
                            "expense, $185 provider-funded casework, and zero net entity cost after "
                            "the $600 refund clears. The $4,200 base generates a $1,050 operator "
                            "share and $3,150 residual provider benefit."
                        ),
                    ),
                    field(
                        "Pending refund and settlement true-up",
                        "textarea",
                        (
                            "Show how an unpaid entity-fee refund changes distributable proceeds "
                            "even after a favorable determination. Record provisional deductions, "
                            "refund evidence, subsequent share adjustments, and the party entitled "
                            "to the returned deposit under the signed agreement."
                        ),
                        (
                            "Before the $600 entity refund clears, the same claim has a $3,600 "
                            "base: $4,500 minus $115, $185, and $600. The 25% share is $900. "
                            "After the deposit returns, the base rises to $4,200 and the operator "
                            "earns a $150 true-up, not a second $1,050 fee."
                        ),
                    ),
                    field(
                        "Unfavorable and ineligible case treatment",
                        "textarea",
                        (
                            "Model claims with no incremental collection and explain how fee "
                            "losses affect provider reserves and operator exposure. Treat dismissal "
                            "refunds conservatively unless verified rules and settlement evidence "
                            "support a different result; never book an anticipated refund as cash."
                        ),
                        (
                            "An ineligible dispute produces zero additional payer cash after $115 "
                            "administrative cost, $600 entity cost, and $185 casework. The planning "
                            "model reserves the full $900 as unrecovered and sets the operator "
                            "share to zero. Any documented refund later reduces the actual loss; "
                            "it does not retroactively create payer recovery."
                        ),
                    ),
                    field(
                        "Annual scenario reconciliation",
                        "textarea",
                        (
                            "Enter the canonical annual operator revenue, operating expense, "
                            "net margin, owner net profit, and team for all three scenarios. "
                            "Keep startup capital, provider recovery volume, and client reserve "
                            "balances outside these operator revenue figures."
                        ),
                        (
                            "Conservative: $110,000 revenue minus $77,000 expense equals $33,000 "
                            "profit, a 30% margin, with 1 FT + 2 C. Base: $505,000 minus "
                            "$287,850 equals $217,150, a 43.0% margin, with 1 FT + 2 C. "
                            "Scaled: $900,000 minus $396,000 equals $504,000, a 56% margin, "
                            "with 2 FT + 3 C."
                        ),
                    ),
                    field(
                        "Retained-share revenue presentation",
                        "textarea",
                        (
                            "Define the service promised by the operator and distinguish "
                            "earned contingency consideration from funds belonging to the provider. "
                            "Document the principal-agent assessment under ASC 606 and prevent "
                            "underlying medical collections from inflating reported operator turnover."
                        ),
                        (
                            "At a contracted 25% share, $2,020,000 of aggregate recovery base "
                            "after agreed deductions produces $505,000 of operator revenue. The "
                            "remaining $1,515,000 belongs to providers and is excluded from operator "
                            "sales. The controller documents the actual contract's ASC 606 treatment; "
                            "this scorecard consistently reports earned shares rather than gross provider receipts."
                        ),
                    ),
                    field(
                        "Reserve ownership and segregation",
                        "textarea",
                        (
                            "Describe the account structure, beneficial owner, reconciliation "
                            "frequency, authorized withdrawals, and return process for unused "
                            "provider advances. Specify whether a true escrow or another lawful "
                            "custodial arrangement exists instead of applying an escrow label casually."
                        ),
                        (
                            "Provider A advances $18,000 for 20 individually modeled disputes. "
                            "The subledger tracks $2,300 administrative charges, $12,000 entity "
                            "deposits, and $3,700 casework budget. Daily reconciliation links every "
                            "withdrawal to a claim and invoice. The agreement identifies provider "
                            "ownership, permitted disbursements, and return of unused funds after final reconciliation."
                        ),
                    ),
                    field(
                        "Startup capital and recurring cash burn",
                        "textarea",
                        (
                            "Allocate startup cash between setup expense and operating runway, "
                            "separating it from provider-funded dispute reserves. Reconcile the "
                            "published monthly operating range with annual scenario expenses by "
                            "identifying variable delivery, acquisition, staffing, and management costs."
                        ),
                        (
                            "A $30,000 startup budget allocates $8,000 to setup and leaves "
                            "$22,000 for runway. Recurring overhead of $5,000 monthly consumes "
                            "$60,000 annually; the Base expense total adds $227,850 of variable "
                            "delivery and other operating costs to reach $287,850. The metadata "
                            "ranges remain $10,000–$45,000 startup and $1,800–$10,500 monthly opex."
                        ),
                    ),
                    field(
                        "Collection lag and 13-week liquidity stress",
                        "textarea",
                        (
                            "Forecast the timing of operator receipts separately from provider "
                            "fee advances and entity refunds. Test a full-quarter collection "
                            "delay, identify the minimum operating balance, and name the funding "
                            "response before spending relies on an unpaid determination."
                        ),
                        (
                            "Opening operator cash is $22,000 after setup. Three months at "
                            "$5,000 recurring overhead leave $7,000 if no contingency receipts "
                            "arrive. Provider dispute advances remain segregated and unavailable "
                            "for payroll. The owner caps new discretionary spending at $2,000 "
                            "and defers hiring when the forecasted operating balance falls below $5,000."
                        ),
                    ),
                    field(
                        "Cohort loss carryforward and contribution",
                        "textarea",
                        (
                            "Specify whether the agreement nets costs by claim or across a "
                            "defined provider cohort, and apply that choice consistently. Show "
                            "how losing cases reduce the cohort base without charging the same "
                            "casework expense twice in operator accounts."
                        ),
                        (
                            "Under an expressly cohort-netted contract, 70 successful cases each "
                            "generate a $4,200 base, totaling $294,000. Thirty zero-recovery cases "
                            "each consume $900, reducing the cohort base to $267,000. The 25% "
                            "operator share is $66,750. Without that cohort clause, $73,500 of "
                            "successful-case shares and separate provider losses would require different settlement."
                        ),
                    ),
                    field(
                        "Cash evidence and month-end close",
                        "textarea",
                        (
                            "List the evidence required to recognize earned contingency "
                            "consideration, settle provider balances, and reconcile operating "
                            "profit. Include bank settlement, remittance matching, unresolved "
                            "recoupments, refund status, and a reviewer independent of the initial "
                            "case calculation."
                        ),
                        (
                            "The close packet includes payer EFT trace 4821, the matching 835, "
                            "the $1,200 baseline, $4,500 incremental receipt, $600 cleared entity "
                            "refund, and cost invoices totaling $300. A second reviewer signs "
                            "the $1,050 contingency calculation. An award notice alone supports "
                            "an operational receivable record, not an earned cash-based contingency charge."
                        ),
                    ),
                ],
                "completion_gate": (
                    "All three canonical scenarios reconcile exactly; the controller signs "
                    "the share waterfall, provider reserve reconciliation, cost-allocation "
                    "policy, and 13-week forecast without counting client funds as operator revenue."
                ),
            },
            {
                "worksheet_id": "ws-03",
                "number": 3,
                "title": "End-to-End Execution, Idempotent Ledger & QA Pre-Flight Sheet",
                "purpose": (
                    "Turn an accepted claim into a reproducible execution record from "
                    "initial remittance through negotiation, IDR initiation, determination, "
                    "collection, and settlement. Preserve statutory timing, duplicate protection, "
                    "evidence provenance, and independent quality checks so retries and staff "
                    "handoffs cannot create duplicate filings or unsupported fees."
                ),
                "chapter_ref": "Q7, Q8",
                "instructions": [
                    (
                        "Create one immutable internal claim identity and retain every payer "
                        "identifier as a linked attribute. Parse the 835 into normalized payment "
                        "events, but preserve the source file and distinguish service-line adjustments "
                        "from claim-level denial or eligibility conclusions."
                    ),
                    (
                        "Start timing from documented receipt events, applying the relevant "
                        "business-day definition and holiday calendar. Keep the initial negotiation "
                        "initiation window, negotiation period, and federal IDR initiation window "
                        "as distinct calculations with independent evidence and reviewer confirmation."
                    ),
                    (
                        "Send negotiation and filing notices through the required channels and "
                        "retain delivery evidence. A generated PDF, internal task completion, or "
                        "successful software request does not establish that the correct counterparty "
                        "received a legally sufficient notice on time."
                    ),
                    (
                        "Use a submission outbox with stable idempotency keys and reconcile "
                        "uncertain responses before retrying. Verify batching eligibility and "
                        "cooling-period treatment separately; neither a shared procedure code nor "
                        "a common payer name automatically makes a proposed batch permissible."
                    ),
                    (
                        "Close only after payer cash, entity-fee disposition, casework deductions, "
                        "and provider settlement reconcile. Track post-determination nonpayment "
                        "against the applicable payment deadline, and retain a separate escalation "
                        "record instead of silently treating the selected offer as collected."
                    ),
                ],
                "fields": [
                    field(
                        "Claim identity and source fingerprint",
                        "textarea",
                        (
                            "Define a stable claim key using provider, payer claim control "
                            "number, service line, and service date, with correction handling. "
                            "Record source fingerprints and version relationships so duplicate "
                            "remittance ingestion cannot generate additional recovery inventory."
                        ),
                        (
                            "Internal claim CED-104 links provider P-17, payer control PC-88214, "
                            "service line 2, and the recorded service date. A SHA-256 digest "
                            "identifies the original 835. A corrected remittance becomes event "
                            "version 2 under the same claim, preserving the initial-payment "
                            "history rather than opening a second dispute or resetting deadlines."
                        ),
                    ),
                    field(
                        "835 normalization and adjustment interpretation",
                        "textarea",
                        (
                            "Identify the CLP, SVC, CAS, and payment-trace elements used "
                            "for extraction and describe how CARC and RARC signals enter "
                            "review. Require plan and service evidence before converting a "
                            "payment adjustment into a federal eligibility classification."
                        ),
                        (
                            "The parser extracts $1,200 payer payment and links the service "
                            "adjustment to its CARC and RARC values. A contractual adjustment "
                            "flag creates an intake task, not an automatic IDR filing. The "
                            "reviewer compares the 835 with the submitted claim, plan funding "
                            "evidence, and service setting before accepting CED-104."
                        ),
                    ),
                    field(
                        "Deadline computation and calendar version",
                        "textarea",
                        (
                            "Record receipt evidence, negotiation-start evidence, controlling "
                            "calendar, counting convention, and computed due dates. Require "
                            "an independent recalculation and preserve extensions separately "
                            "from ordinary rules so an exceptional deadline never becomes "
                            "the default for later cases."
                        ),
                        (
                            "Calendar CAL-01 treats Saturdays, Sundays, and federal holidays "
                            "as nonbusiness days for the applicable federal calculation. The "
                            "record separately computes the initial 30-business-day initiation "
                            "limit, the 30-business-day negotiation period, and the next four "
                            "business days for IDR initiation. Two reviewers reconcile actual "
                            "dates against current CMS instructions before release."
                        ),
                    ),
                    field(
                        "Negotiation notice and delivery record",
                        "textarea",
                        (
                            "Describe the notice package, recipient verification, required "
                            "content, transmission method, and delivery proof. State how "
                            "bounces, disputed receipt dates, or changed payer contacts "
                            "are escalated without assuming that an internal send timestamp "
                            "establishes valid service."
                        ),
                        (
                            "The negotiation package identifies the claim, service, proposed "
                            "payment, and authorized representative using the required notice "
                            "format. The operator verifies the payer contact against current "
                            "remittance instructions and retains the sent message, attachments, "
                            "and delivery evidence. A bounce moves the case to urgent review "
                            "that day rather than marking negotiation successfully initiated."
                        ),
                    ),
                    field(
                        "Batch membership and suspension register",
                        "textarea",
                        (
                            "List each proposed batch member, the applicable grouping "
                            "criteria, service-date boundaries, and evidence supporting "
                            "compatibility. Check the same-party cooling restriction "
                            "separately and document the rule version, determination date, "
                            "and any applicable subsequent-claim filing window."
                        ),
                        (
                            "Batch B-12 proposes six claims involving the same provider "
                            "and plan. The reviewer checks the applicable item-or-service "
                            "standard, timing requirements, and current court-affected "
                            "implementation before grouping them. One claim falls under "
                            "a prior same-party 90-calendar-day suspension and is removed "
                            "pending documented treatment under the applicable post-suspension window."
                        ),
                    ),
                    field(
                        "Federal initiation and entity selection checkpoints",
                        "textarea",
                        (
                            "Separate timely federal IDR initiation from later certified "
                            "entity selection, conflict checks, fee payment, and offer "
                            "submission. Record the authoritative instruction for each "
                            "deadline instead of labeling the four-business-day initiation "
                            "period as an entity-selection period."
                        ),
                        (
                            "The case reaches federal initiation on day 2 of the applicable "
                            "four-business-day window, with portal confirmation retained. "
                            "A separate task tracks the generally applicable three-business-day "
                            "joint entity-selection period and any controlling current "
                            "instructions. Entity-selection confirmation then drives the "
                            "offer-submission deadline, generally ten business days, with "
                            "the actual portal notice preserved."
                        ),
                    ),
                    field(
                        "Offer normalization and brief QA",
                        "textarea",
                        (
                            "Specify whether each amount represents total out-of-network "
                            "payment, patient cost sharing, initial payer payment, or "
                            "additional payer payment. Require an arithmetic bridge and "
                            "evidence citations so the brief never compares amounts "
                            "defined on incompatible bases."
                        ),
                        (
                            "The reviewer reconciles a hypothetical $6,300 total payment "
                            "amount with $300 patient cost sharing, producing $6,000 "
                            "payer responsibility. After subtracting the $1,200 initial "
                            "payer payment, additional payer payment would be $4,800. "
                            "If only $4,500 arrives, the ledger records a $300 shortfall "
                            "rather than treating the total determination as cash."
                        ),
                    ),
                    field(
                        "Idempotent submission and uncertain response",
                        "textarea",
                        (
                            "Define the external submission key, payload digest, "
                            "outbox status, retry policy, and reconciliation owner. "
                            "Explain how the system distinguishes confirmed failure "
                            "from uncertain success so a timeout cannot trigger "
                            "duplicate filings, payments, or provider invoices."
                        ),
                        (
                            "Outbox item SUB-104 uses the claim ID, proceeding type, "
                            "and filing version as its stable key. A timeout after "
                            "upload changes status to confirmation-required. The operator "
                            "checks portal history and the confirmation mailbox before "
                            "retrying; an existing confirmation is attached to SUB-104 "
                            "and suppresses another submission or fee instruction."
                        ),
                    ),
                    field(
                        "Determination-to-cash collection tracker",
                        "textarea",
                        (
                            "Track determination receipt, additional amount due, "
                            "applicable payment deadline, payer contact, and actual "
                            "receipts. Separate substantive disputes about the amount "
                            "from payment delay, and identify the documented escalation "
                            "path for an overdue federal determination."
                        ),
                        (
                            "A determination establishes $4,800 additional payer payment, "
                            "with the applicable 30-calendar-day payment deadline recorded. "
                            "Only $4,500 clears, leaving $300 open. The collections owner "
                            "sends a reconciliation request with the determination and "
                            "EFT evidence, then evaluates the appropriate CMS complaint "
                            "or counsel-assisted route if the shortfall remains unresolved."
                        ),
                    ),
                    field(
                        "Append-only settlement and correction trail",
                        "textarea",
                        (
                            "Describe settlement approval, receipt allocation, "
                            "reversal handling, and retention of earlier calculations. "
                            "Require balanced correction events rather than editing "
                            "historical receipts, and state how subsequent payer "
                            "recoupments affect the operator share and provider statement."
                        ),
                        (
                            "Settlement SET-104 records $4,500 incremental cash, $300 "
                            "deductions, a $1,050 share, and $3,150 provider residual. "
                            "A later $400 payer recoupment creates a linked reversal, "
                            "reducing the eligible base by $400 and the 25% share "
                            "by $100. The agreement determines whether that $100 "
                            "is refunded or credited on the next statement."
                        ),
                    ),
                ],
                "completion_gate": (
                    "A second reviewer confirms jurisdiction, calendar math, delivery "
                    "evidence, batch membership, offer normalization, portal confirmation, "
                    "and balanced ledger events; no uncertain submission or unmatched "
                    "receipt may be marked complete."
                ),
            },
            {
                "worksheet_id": "ws-04",
                "number": 4,
                "title": "Statutory, Licensing, Contract Addendum & Compliance Audit",
                "purpose": (
                    "Convert statutory and contractual obligations into evidence-backed "
                    "operating controls. Establish federal jurisdiction, HIPAA responsibilities, "
                    "permitted representation, defensible offer evidence, fee allocation, and "
                    "record retention while preserving state-specific analysis and current "
                    "implementation instructions for every material filing decision."
                ),
                "chapter_ref": "Q5, Q9",
                "instructions": [
                    (
                        "Create a dated authority register covering 42 U.S.C. § 300gg-111, "
                        "45 CFR § 149.510, related plan provisions, applicable state "
                        "surprise-billing rules, and current CMS implementation material. "
                        "Attach the authority supporting the actual service and plan rather "
                        "than relying on a generic reference list."
                    ),
                    (
                        "Execute the business associate agreement before receiving protected "
                        "health information for covered activities. Limit access by role, "
                        "document subcontractor responsibilities, and select storage, messaging, "
                        "and automation services whose contractual terms and safeguards support "
                        "the intended health-information processing."
                    ),
                    (
                        "Review representation authority and state-specific licensing exposure "
                        "before selling services or signing pleadings. Distinguish administrative "
                        "support, permitted authorized representation, collection activity, and "
                        "legal practice, and route activities requiring licensed professionals "
                        "to the appropriate retained resource."
                    ),
                    (
                        "Write the fee addendum around actual incremental payer cash, "
                        "unrecovered dispute fees, casework costs, and refund adjustments. "
                        "Specify reserve ownership, unsuccessful-case treatment, cohort "
                        "netting, termination accounting, and recoupment handling so the "
                        "provider can reproduce every settlement calculation."
                    ),
                    (
                        "Test evidence restrictions and patient-protection controls on a "
                        "sample before launch. Preserve the QPA without treating it as "
                        "a mandatory winning presumption, exclude prohibited comparisons, "
                        "and ensure the operator's recovery process never creates a "
                        "prohibited balance bill to the patient."
                    ),
                ],
                "fields": [
                    field(
                        "Federal authority and current implementation register",
                        "textarea",
                        (
                            "Identify statutory and regulatory provisions governing "
                            "the claim and record the date each operational source "
                            "was checked. Distinguish enacted text, regulations, "
                            "judicially affected provisions, and portal instructions "
                            "instead of treating an old checklist as controlling."
                        ),
                        (
                            "The register anchors eligibility and payment rules to "
                            "42 U.S.C. § 300gg-111 and 45 CFR § 149.510, with "
                            "29 CFR § 2590.716-8 considered for applicable ERISA "
                            "plan provisions. The filing lead attaches current CMS "
                            "guidance and a dated note on court-affected batching "
                            "or offer-evaluation instructions before using the checklist."
                        ),
                    ),
                    field(
                        "State mechanism and ERISA boundary",
                        "textarea",
                        (
                            "Document how the state payment mechanism interacts "
                            "with plan funding, service category, and any applicable "
                            "election. Name the state authority being evaluated "
                            "and explain the claim-specific route without assuming "
                            "all insured or self-funded arrangements behave alike."
                        ),
                        (
                            "For a Texas encounter, the reviewer examines Texas "
                            "Insurance Code Chapter 1467 alongside plan funding "
                            "and service facts. An insured claim within the state "
                            "mechanism is not automatically sent to federal IDR. "
                            "A self-funded claim receives a separate election and "
                            "applicability check, with the supporting plan documents "
                            "attached to the route memorandum."
                        ),
                    ),
                    field(
                        "Business associate agreement and subcontractors",
                        "textarea",
                        (
                            "List the covered entity, business associate, "
                            "subcontractors, permitted uses, incident reporting "
                            "terms, and return-or-destruction obligations. Connect "
                            "each processing service to the required agreement "
                            "and safeguards before any identifiable clinical "
                            "or payment record enters the service."
                        ),
                        (
                            "The provider and operator execute terms addressing "
                            "45 CFR §§ 164.502(e) and 164.504(e). The encrypted "
                            "storage vendor and document-processing subcontractor "
                            "are assessed for downstream business associate duties. "
                            "The agreement requires prompt incident reporting and "
                            "defines termination handling; ordinary consumer upload "
                            "accounts are excluded from the protected-information workflow."
                        ),
                    ),
                    field(
                        "Minimum necessary access and safeguards",
                        "textarea",
                        (
                            "Specify who needs clinical, payment, and identity "
                            "information for each task and how access is "
                            "restricted. Document authentication, encryption, "
                            "audit logging, and periodic access review against "
                            "the relevant HIPAA privacy and security requirements."
                        ),
                        (
                            "The intake contractor can view remittance and plan "
                            "records; the clinical reviewer receives only necessary "
                            "encounter material; the growth contractor receives "
                            "aggregated metrics. MFA, encrypted storage, role-based "
                            "permissions, and audit events support 45 CFR §§ "
                            "164.308, 164.312, and 164.514(d). Access is reviewed "
                            "monthly and removed immediately when an assignment ends."
                        ),
                    ),
                    field(
                        "Representation and licensing scope",
                        "textarea",
                        (
                            "Identify permitted representative activities and "
                            "state-specific licensing questions for collections, "
                            "claims services, and legal representation. State "
                            "which professional makes the determination and "
                            "how the engagement prevents staff from exceeding "
                            "the authority actually granted by the provider."
                        ),
                        (
                            "The engagement authorizes document assembly and "
                            "permitted IDR representation while reserving litigation "
                            "and jurisdiction disputes requiring legal practice "
                            "to retained counsel. Counsel evaluates the operating "
                            "states' collection-agency and unauthorized-practice "
                            "rules, including Texas Government Code § 81.101 "
                            "where relevant. Staff receive a written task boundary "
                            "rather than an assumed nationwide license exemption."
                        ),
                    ),
                    field(
                        "Incremental-cash contingency addendum",
                        "textarea",
                        (
                            "Draft the operative share clause with a "
                            "precise initial-payment baseline, permitted "
                            "deductions, refund treatment, and zero floor. "
                            "Exclude baseline collections, patient payments, "
                            "unpaid determinations, and duplicate charges "
                            "while explaining provider-level cost netting."
                        ),
                        (
                            "Operator compensation equals 25% of cleared incremental "
                            "payer cash above the documented initial payer payment, "
                            "less unrecovered administrative and entity fees and "
                            "agreed attributable casework, floored at zero. Baseline "
                            "payments and patient receipts are excluded. Cohort "
                            "netting applies only to the expressly identified "
                            "provider cohort, with later refunds and recoupments "
                            "reconciled on the next statement."
                        ),
                    ),
                    field(
                        "Fee responsibility and entity refund terms",
                        "textarea",
                        (
                            "State who pays administrative and entity charges, "
                            "when deposits are due, and how actual refunds "
                            "are allocated. Separate the standard prevailing-party "
                            "refund expectation from dismissal, settlement, "
                            "withdrawal, and other disposition rules requiring "
                            "current entity-specific verification."
                        ),
                        (
                            "The provider advances both illustrative charges: "
                            "$115 administrative and $600 entity deposit. The "
                            "administrative charge is modeled as non-refundable. "
                            "A prevailing-party entity refund reduces case cost "
                            "only when documented; losing or ineligible cases "
                            "retain the full deposit loss reserve. Actual dismissal "
                            "or settlement treatment follows verified applicable "
                            "instructions, with no assumed favorable refund."
                        ),
                    ),
                    field(
                        "Offer evidence restrictions and QPA treatment",
                        "textarea",
                        (
                            "Define permitted evidence categories and prohibited "
                            "comparisons for the offer packet. Explain how "
                            "the QPA is considered alongside relevant allowed "
                            "information without imposing a presumption "
                            "unsupported by current governing law or "
                            "double-counting factors already reflected in pricing."
                        ),
                        (
                            "The brief considers the QPA and supported information "
                            "about acuity, training, facility characteristics, "
                            "and good-faith contracting efforts where applicable. "
                            "It excludes billed charges, usual-and-customary "
                            "charge measures, and Medicare or Medicaid rates "
                            "as prohibited comparison inputs. The reviewer "
                            "checks current requirements under 45 CFR § 149.510(c)(4) "
                            "and explains the evidentiary relevance of each exhibit."
                        ),
                    ),
                    field(
                        "Patient protection and referral compensation",
                        "textarea",
                        (
                            "Describe controls preventing prohibited balance "
                            "billing and inappropriate referral-linked "
                            "compensation. Identify patient-cost-sharing "
                            "treatment and the review required before "
                            "marketing payments, fee splits, or referral "
                            "arrangements involving healthcare providers "
                            "are implemented in any operating state."
                        ),
                        (
                            "The workflow never bills the patient for the "
                            "operator's contingency or an IDR shortfall. "
                            "Provider obligations under 42 U.S.C. § 300gg-131 "
                            "and 45 CFR § 149.410 are reflected in account "
                            "instructions. Proposed referral compensation "
                            "receives a fact-specific review of state fee-splitting "
                            "rules and 42 U.S.C. § 1320a-7b(b) where relevant; "
                            "no per-patient commission is launched by default."
                        ),
                    ),
                    field(
                        "Retention, termination, and incident response",
                        "textarea",
                        (
                            "Assign retention periods by record category, "
                            "including HIPAA documentation, contractual "
                            "records, dispute evidence, and litigation "
                            "holds. Define incident escalation and "
                            "termination transfer so deletion automation "
                            "cannot erase records still required by "
                            "law, contract, or an active dispute."
                        ),
                        (
                            "The schedule retains required HIPAA documentation "
                            "for six years under 45 CFR §§ 164.316(b)(2) "
                            "and 164.530(j), while separately assessing medical "
                            "record and dispute retention duties. A suspected "
                            "disclosure triggers the response plan and "
                            "45 CFR § 164.410 assessment. Termination exports "
                            "authorized records, reconciles reserves, revokes access, "
                            "and preserves applicable holds before deletion."
                        ),
                    ),
                ],
                "completion_gate": (
                    "The responsible reviewer signs the authority register, state-route "
                    "analysis, executed BAA, representation scope, fee addendum, evidence "
                    "restrictions, and retention schedule before protected records or "
                    "live disputes enter production."
                ),
            },
            {
                "worksheet_id": "ws-05",
                "number": 5,
                "title": "Automation Pipeline, Acquisition Flywheel & Risk Fallback Tracker",
                "purpose": (
                    "Automate repetitive intake and deadline work without delegating "
                    "jurisdiction, clinical judgment, or cash recognition to unsupported "
                    "predictions. Connect de-identified acquisition evidence to provider "
                    "pilots, monitor error rates, and preserve manual fallbacks for "
                    "portal interruptions, uncertain eligibility, and delayed payer remittance."
                ),
                "chapter_ref": "Q6, Q10",
                "instructions": [
                    (
                        "Map the pipeline from authorized source retrieval through "
                        "835 parsing, eligibility review, deadline scheduling, brief "
                        "assembly, filing, and cash reconciliation. Identify the "
                        "system of record and responsible person for every state "
                        "transition rather than relying on informal inbox ownership."
                    ),
                    (
                        "Evaluate the ERISA and jurisdiction classifier against "
                        "adjudicated examples, including insured plans, state "
                        "elections, excluded services, and incomplete documents. "
                        "Route low-confidence results to review and measure "
                        "false federal classifications separately because they "
                        "can consume non-refundable fees."
                    ),
                    (
                        "Generate briefs from approved evidence templates and "
                        "case-specific facts with exhibit references. Keep "
                        "clinical assertions tied to records, screen benchmark "
                        "content for prohibited measures, and require a named "
                        "reviewer before any offer or factual statement is submitted."
                    ),
                    (
                        "Acquire practices through verifiable operational value "
                        "such as missed-window audits and recovery-ledger "
                        "diagnostics. Use permissioned case studies with "
                        "aggregate results, never raw patient records or "
                        "unqualified favorable-determination statistics presented "
                        "as universal collection performance."
                    ),
                    (
                        "Test manual deadline queues, portal outage procedures, "
                        "backup restoration, and collections escalation before "
                        "increasing volume. Pause only the affected processing "
                        "step, preserve statutory deadlines, and avoid inventing "
                        "an extension or unsupported submission channel when "
                        "a platform becomes unavailable."
                    ),
                ],
                "fields": [
                    field(
                        "Pipeline stages and authoritative records",
                        "textarea",
                        (
                            "Describe each processing stage, its input "
                            "contract, output record, owner, and "
                            "failure state. Identify where immutable "
                            "evidence is stored and how operational "
                            "status is reconciled with external "
                            "portal confirmations and cleared cash."
                        ),
                        (
                            "The pipeline moves through intake, source validation, "
                            "route review, negotiation, initiation, offer preparation, "
                            "determination, collection, and settlement. PostgreSQL "
                            "holds case events; access-controlled object storage "
                            "holds source documents. A filing coordinator owns "
                            "portal reconciliation, while a separate collections "
                            "owner matches EFT traces. Neither a parser success "
                            "nor a task completion alone advances legal status."
                        ),
                    ),
                    field(
                        "835 extraction accuracy and exception queue",
                        "textarea",
                        (
                            "Set field-level extraction tests for payment "
                            "amounts, control numbers, service lines, "
                            "adjustments, and payer identifiers. Define "
                            "tolerances and exception handling for "
                            "reversals, corrected remittances, and "
                            "unmatched deposits before records enter "
                            "economic calculations or deadline workflows."
                        ),
                        (
                            "A 200-remittance validation set requires exact "
                            "agreement on payer payment and claim control "
                            "number for every automatically accepted record. "
                            "Three unmatched EFT traces and two corrected "
                            "claims enter the exception queue. The parser "
                            "does not infer missing cash; the reviewer "
                            "resolves each source discrepancy and records "
                            "the correction before recalculating the recovery base."
                        ),
                    ),
                    field(
                        "ERISA classifier and jurisdiction error budget",
                        "textarea",
                        (
                            "Specify classifier features, prohibited "
                            "shortcuts, reviewed labels, and escalation "
                            "thresholds. Measure false federal routing "
                            "directly, and require documentary support "
                            "for funding arrangement and state-rule "
                            "applicability rather than inferring eligibility "
                            "from a carrier logo or adjustment code."
                        ),
                        (
                            "The classifier uses plan documents, funding "
                            "statements, service setting, and verified state "
                            "mechanism evidence. In 100 reviewed cases it "
                            "proposes 72 federal routes, but two prove "
                            "incorrect, a 2.8% false-route share of those "
                            "proposals. Automatic routing remains disabled; "
                            "a reviewer resolves both errors and retrains "
                            "the decision rules before the next evaluation."
                        ),
                    ),
                    field(
                        "Deadline engine tests and alert ownership",
                        "textarea",
                        (
                            "Define calendar fixtures, boundary tests, "
                            "time-zone handling, extension records, "
                            "and alert escalation. Test negotiation "
                            "initiation, negotiation expiration, federal "
                            "initiation, cooling periods, and post-determination "
                            "payment separately so a single "
                            "date helper cannot silently misclassify all deadlines."
                        ),
                        (
                            "Python unittest fixtures cover federal holidays, "
                            "Friday receipt, leap day, and year-end "
                            "transitions. Alerts fire five and two "
                            "business days before negotiation-related "
                            "deadlines, with immediate owner escalation "
                            "inside the final day. The 90-day suspension "
                            "and 30-day payment obligation use their "
                            "applicable calendar-day logic rather than "
                            "reusing the business-day counter."
                        ),
                    ),
                    field(
                        "Evidence assembler and benchmark controls",
                        "textarea",
                        (
                            "Describe how the brief builder "
                            "extracts facts, links exhibits, "
                            "normalizes payment amounts, and "
                            "screens benchmark material. Require "
                            "human verification of clinical "
                            "acuity and provider qualifications "
                            "and record the licensed source "
                            "of every retained pricing reference."
                        ),
                        (
                            "The assembler populates a standard offer "
                            "packet from approved facts and exhibit "
                            "IDs, leaving no unsupported clinical "
                            "assertion for submission. A reviewer "
                            "checks acuity against the encounter "
                            "record and inspects FAIR Health "
                            "metric definitions. Charge-based material "
                            "is excluded; any permissible retained "
                            "benchmark includes source rights, methodology, "
                            "and a case-specific relevance explanation."
                        ),
                    ),
                    field(
                        "Provider acquisition offer and funnel economics",
                        "textarea",
                        (
                            "Define the target practice, outreach "
                            "message, diagnostic deliverable, and "
                            "conversion denominator. Calculate "
                            "acquisition cost from actual spend "
                            "and signed providers, and distinguish "
                            "a signed pilot from collectible "
                            "claims or recognized operator revenue."
                        ),
                        (
                            "The target is an independent emergency "
                            "physician group with usable 835 exports "
                            "and documented out-of-network inventory. "
                            "A $4,800 campaign reaches 80 practices, "
                            "produces 12 discovery calls, four "
                            "diagnostic reviews, and two signed "
                            "pilots. Acquisition cost is $2,400 "
                            "per signed provider; neither signature "
                            "creates revenue before incremental recovery "
                            "and earned compensation."
                        ),
                    ),
                    field(
                        "Proof package and permissioned case study",
                        "textarea",
                        (
                            "Choose outcome measures that "
                            "communicate operational value "
                            "without exposing patient information "
                            "or equating favorable decisions "
                            "with collected money. Record "
                            "provider publication permission, "
                            "aggregation method, observation period, "
                            "and limitations caused by "
                            "pending cases or incomplete collections."
                        ),
                        (
                            "The provider-approved case study reports "
                            "40 submitted disputes, 24 favorable "
                            "determinations, 18 fully collected "
                            "favorable cases, three partially "
                            "collected favorable cases, and three "
                            "unpaid favorable cases at the "
                            "measurement date. It omits patient "
                            "identifiers and claim-level clinical "
                            "details. Publication occurs only after "
                            "permission and privacy review of "
                            "the actual aggregate presentation."
                        ),
                    ),
                    field(
                        "Portal outage and manual continuity procedure",
                        "textarea",
                        (
                            "Specify the outage evidence, "
                            "manual task queue, support "
                            "contact, and authority needed "
                            "for alternative filing or "
                            "deadline relief. Explain how "
                            "staff preserve proof and "
                            "avoid assuming that downtime "
                            "automatically extends a statutory "
                            "or regulatory deadline."
                        ),
                        (
                            "When the portal becomes unavailable "
                            "two business days before initiation "
                            "expires, the coordinator records "
                            "timestamps, screenshots, and support "
                            "ticket details, then escalates "
                            "immediately. Staff use only "
                            "currently authorized alternative "
                            "procedures or documented relief. "
                            "The manual queue preserves "
                            "claim priority and evidence; "
                            "it never marks an unsent "
                            "filing complete."
                        ),
                    ),
                    field(
                        "Delayed-remittance fallback and cash throttling",
                        "textarea",
                        (
                            "Define aged-recovery buckets, "
                            "collection ownership, documentation "
                            "requirements, and volume limits "
                            "when payer cash lags. "
                            "Separate provider reserve sufficiency "
                            "from operator runway and "
                            "describe the escalation path "
                            "for determinations that remain "
                            "unpaid after the applicable deadline."
                        ),
                        (
                            "The dashboard separates amounts "
                            "due within 30 days, overdue "
                            "by 1–30 days, and overdue "
                            "by more than 30 days, "
                            "measured against the applicable "
                            "due date. If operator cash "
                            "falls below $5,000, discretionary "
                            "acquisition pauses. Collections "
                            "staff assemble determination, "
                            "notice, and remittance evidence "
                            "for payer escalation and "
                            "the appropriate enforcement channel."
                        ),
                    ),
                    field(
                        "Change control and measurable automation benefit",
                        "textarea",
                        (
                            "Record the baseline labor "
                            "time, proposed automated step, "
                            "test population, error measures, "
                            "and rollback owner. Require "
                            "an observable improvement without "
                            "increased deadline or eligibility "
                            "errors, and keep production "
                            "access separate from experimental "
                            "processing environments."
                        ),
                        (
                            "A brief-assembly change reduces "
                            "median preparation time from "
                            "90 to 55 minutes across "
                            "20 reviewed cases, saving "
                            "700 minutes, or 11 hours "
                            "40 minutes. Every offer "
                            "still receives review. One "
                            "incorrect exhibit link triggers "
                            "rollback to the prior "
                            "template until corrected; "
                            "the release record preserves "
                            "both the benefit measurement "
                            "and defect evidence."
                        ),
                    ),
                ],
                "completion_gate": (
                    "The automation owner demonstrates tested calendar logic, reviewed "
                    "jurisdiction classifications, source-linked briefs, duplicate suppression, "
                    "and a manual continuity drill; acquisition material uses authorized "
                    "aggregate evidence and distinguishes decisions from collections."
                ),
            },
            {
                "worksheet_id": "ws-06",
                "number": 6,
                "title": "30-Day Launch Sprint, Pod KPI Scorecard & Exit-Readiness Ledger",
                "purpose": (
                    "Launch a controlled provider pilot within 30 days while "
                    "respecting longer statutory and collection cycles. Assign "
                    "small-team ownership, track eligible inventory and collected "
                    "contribution, reconcile canonical targets, and build transferable "
                    "records that support management continuity, diligence, and "
                    "eventual ownership transition without overstating pipeline value."
                ),
                "chapter_ref": "Q11, Q12",
                "instructions": [
                    (
                        "Treat the first month as a setup and qualified-pipeline "
                        "sprint, not a promise of completed arbitration cash. "
                        "The published time to first deal is one to four "
                        "months, and newly initiated negotiation commonly extends "
                        "beyond a 30-calendar-day launch plan."
                    ),
                    (
                        "Assign a full-time operator and two contractors to "
                        "distinct intake, evidence, deadline, and reconciliation "
                        "responsibilities. Document backup coverage for every "
                        "time-sensitive task and preserve independent checking "
                        "even when one person owns several routine operating functions."
                    ),
                    (
                        "Measure eligible inventory, timely notices, dismissal "
                        "reasons, favorable determinations, cleared incremental "
                        "cash, and earned operator shares as separate metrics. "
                        "Use dated cohorts and denominators so growing "
                        "submission volume cannot conceal collection delays "
                        "or worsening eligibility accuracy."
                    ),
                    (
                        "Compare the actual forecast with the canonical "
                        "Conservative, Base, and Scaled cases without rewriting "
                        "their economics. Scale only after observed delivery "
                        "capacity, reserve funding, quality, and collection "
                        "performance support the next workload; headcount "
                        "alone does not create recoverable inventory."
                    ),
                    (
                        "Build the exit-readiness ledger from reproducible "
                        "records, assignable contracts, protected-information "
                        "controls, and reconciled earnings. Distinguish earned "
                        "receivables from unpaid determinations and speculative "
                        "pipeline, and restrict diligence access until "
                        "appropriate agreements and data-minimization "
                        "arrangements are established."
                    ),
                ],
                "fields": [
                    field(
                        "Days 1–7 operating foundation",
                        "textarea",
                        (
                            "Specify first-week deliverables, "
                            "owners, dependencies, and "
                            "acceptance evidence for "
                            "contracts, security, banking, "
                            "source records, and "
                            "jurisdiction review. Identify "
                            "which activities can "
                            "proceed before protected "
                            "information arrives and "
                            "which require executed agreements."
                        ),
                        (
                            "By day 3, the owner completes "
                            "the service agreement and "
                            "incremental-cash addendum. By "
                            "day 5, the BAA, role "
                            "permissions, and reserve "
                            "accounting are active. By "
                            "day 7, intake receives "
                            "60 authorized sample claims "
                            "and records their initial "
                            "payment evidence. No production "
                            "clinical record enters an "
                            "unapproved service during setup."
                        ),
                    ),
                    field(
                        "Days 8–14 underwriting and calendar validation",
                        "textarea",
                        (
                            "Define the second-week "
                            "claim-screening target, "
                            "document requirements, "
                            "calendar tests, and "
                            "reviewer sign-offs. "
                            "Separate accepted cases "
                            "from unresolved cases "
                            "and identify how "
                            "missing evidence is "
                            "obtained without allowing "
                            "a filing deadline to lapse."
                        ),
                        (
                            "The intake contractor screens "
                            "60 claims and proposes "
                            "20 pilot candidates. The "
                            "operator confirms 15 and "
                            "holds five for plan "
                            "documentation. A second "
                            "reviewer recalculates every "
                            "candidate deadline and "
                            "checks the holiday calendar. "
                            "Cases already near expiry "
                            "receive same-day attention "
                            "rather than waiting for "
                            "the weekly launch meeting."
                        ),
                    ),
                    field(
                        "Days 15–21 negotiation and evidence preparation",
                        "textarea",
                        (
                            "Set the authorized "
                            "negotiation workload, "
                            "notice verification "
                            "standard, evidence "
                            "assembly target, "
                            "and fee-funding "
                            "check. Distinguish "
                            "preparation from "
                            "federal initiation "
                            "and preserve the "
                            "full required "
                            "negotiation period "
                            "for each accepted claim."
                        ),
                        (
                            "The coordinator sends 15 "
                            "timely negotiation notices "
                            "with recipient and delivery "
                            "evidence. Clinical review "
                            "completes eight draft "
                            "evidence packets, while "
                            "the provider funds the "
                            "agreed reserve. No case "
                            "enters IDR merely because "
                            "the launch sprint reaches "
                            "day 21; its own negotiation "
                            "expiration and eligibility "
                            "control the next action."
                        ),
                    ),
                    field(
                        "Days 22–30 rehearsal and first operating review",
                        "textarea",
                        (
                            "Describe end-of-month "
                            "deliverables that "
                            "demonstrate readiness "
                            "without inventing "
                            "completed recoveries. "
                            "Include a submission "
                            "rehearsal, ledger "
                            "reconciliation, outage "
                            "drill, provider "
                            "report, and "
                            "next-month calendar "
                            "for proceedings "
                            "still within negotiation."
                        ),
                        (
                            "By day 30, the team "
                            "rehearses one synthetic "
                            "filing, reconciles the "
                            "provider reserve, tests "
                            "the portal-outage checklist, "
                            "and issues a status "
                            "report covering all "
                            "20 candidates. Fifteen "
                            "negotiations remain tracked "
                            "on their actual clocks; "
                            "the report records zero "
                            "earned contingency revenue "
                            "unless qualifying incremental "
                            "cash has actually cleared."
                        ),
                    ),
                    field(
                        "Pod roles, capacity, and backup ownership",
                        "textarea",
                        (
                            "Assign primary and "
                            "backup responsibility "
                            "for eligibility, "
                            "deadlines, clinical "
                            "evidence, submission, "
                            "collections, and "
                            "settlement review. "
                            "State weekly "
                            "capacity assumptions "
                            "and show how "
                            "independent review "
                            "survives absences "
                            "within the specified "
                            "small-team configurations."
                        ),
                        (
                            "The Base pod uses 1 "
                            "FT operator plus 2 "
                            "contractors: one handles "
                            "intake and calendars, "
                            "the other evidence "
                            "preparation and second "
                            "checks. The operator "
                            "owns filing and "
                            "collections, with trained "
                            "backup coverage. The "
                            "Scaled pod adds one "
                            "FT case manager and "
                            "one contractor, reaching "
                            "2 FT + 3 C, "
                            "or five people."
                        ),
                    ),
                    field(
                        "Weekly KPI definitions and thresholds",
                        "textarea",
                        (
                            "Define each KPI "
                            "numerator, denominator, "
                            "measurement period, "
                            "owner, and action "
                            "threshold. Include "
                            "deadline adherence, "
                            "eligibility loss, "
                            "cash realization, "
                            "cycle time, "
                            "and earned "
                            "contribution without "
                            "combining materially "
                            "different populations "
                            "into one success percentage."
                        ),
                        (
                            "The weekly scorecard shows "
                            "15 of 15 notices "
                            "timely, 20 of 60 "
                            "sample claims accepted, "
                            "and five candidates "
                            "initially requiring "
                            "additional plan evidence. "
                            "Later cohorts separately "
                            "report favorable outcomes "
                            "and cleared incremental "
                            "cash divided by additional "
                            "payer amounts due. "
                            "Any missed statutory "
                            "deadline triggers immediate "
                            "incident review, regardless "
                            "of revenue performance."
                        ),
                    ),
                    field(
                        "Canonical scorecard and growth decision",
                        "textarea",
                        (
                            "Record the volume's "
                            "ranking, score "
                            "components, canonical "
                            "annual cases, "
                            "and actual "
                            "forecast variance. "
                            "Explain which "
                            "observed operational "
                            "conditions justify "
                            "moving between "
                            "staffing levels "
                            "without presenting "
                            "the model's "
                            "profit targets "
                            "as already earned."
                        ),
                        (
                            "Volume 045 ranks #09 "
                            "of 49 with 94/100: "
                            "24 revenue, 24 margin, "
                            "20 team efficiency, "
                            "13 startup accessibility, "
                            "and 13 automation. "
                            "Canonical revenue/profit "
                            "pairs remain "
                            "$110,000/$33,000, "
                            "$505,000/$217,150, "
                            "and $900,000/$504,000. "
                            "The growth decision "
                            "uses actual eligible "
                            "inventory, collection "
                            "lags, funded reserves, "
                            "and reviewed capacity, "
                            "not the score alone."
                        ),
                    ),
                    field(
                        "Risk register and stop-spend triggers",
                        "textarea",
                        (
                            "List the "
                            "highest-impact "
                            "failure modes, "
                            "leading indicators, "
                            "loss exposure, "
                            "owners, and "
                            "specific fallback "
                            "actions. Include "
                            "ineligible filings, "
                            "same-party cooling "
                            "errors, delayed "
                            "remittance, "
                            "privacy incidents, "
                            "and insufficient "
                            "operator working "
                            "capital rather "
                            "than one generic "
                            "risk category."
                        ),
                        (
                            "Two eligibility dismissals "
                            "in the first ten "
                            "filings stop new "
                            "fee commitments for "
                            "route revalidation. "
                            "A detected cooling "
                            "conflict removes the "
                            "affected claim from "
                            "the proposed batch. "
                            "Operator cash below "
                            "$5,000 pauses discretionary "
                            "acquisition, while overdue "
                            "payer amounts enter "
                            "the documented collections "
                            "escalation queue. Each "
                            "trigger names an owner "
                            "and a restart test."
                        ),
                    ),
                    field(
                        "Transferable contracts and diligence evidence",
                        "textarea",
                        (
                            "Identify contract "
                            "assignment provisions, "
                            "termination rights, "
                            "concentration exposure, "
                            "data-access conditions, "
                            "staff dependencies, "
                            "and source-system "
                            "documentation needed "
                            "for continuity. "
                            "Design diligence "
                            "around minimized "
                            "information first "
                            "and obtain "
                            "the required "
                            "permissions before "
                            "external disclosure."
                        ),
                        (
                            "The diligence index "
                            "contains executed "
                            "provider agreements, "
                            "assignment clauses, "
                            "aggregate cohort "
                            "reports, SOP versions, "
                            "and reconciled "
                            "earnings schedules. "
                            "A buyer initially "
                            "receives provider-coded "
                            "summaries rather than "
                            "clinical files. "
                            "Required provider "
                            "permissions and "
                            "appropriate confidentiality "
                            "and health-information "
                            "arrangements precede "
                            "expanded access; "
                            "the operator records "
                            "who accessed each "
                            "authorized document."
                        ),
                    ),
                    field(
                        "Exit-quality earnings and handoff ledger",
                        "textarea",
                        (
                            "Reconcile reported "
                            "earnings to "
                            "earned operator "
                            "shares, cleared "
                            "cash, expenses, "
                            "reserve liabilities, "
                            "refunds, and "
                            "recoupments. "
                            "Separate collected "
                            "value from "
                            "unpaid determinations "
                            "and speculative "
                            "inventory, then "
                            "define the "
                            "handoff evidence "
                            "needed for "
                            "another operator "
                            "to reproduce "
                            "the close."
                        ),
                        (
                            "The Base diligence "
                            "bridge starts with "
                            "$505,000 earned "
                            "operator revenue "
                            "and $287,850 "
                            "operating expense, "
                            "yielding $217,150 "
                            "owner net profit. "
                            "Provider reserves "
                            "remain liabilities, "
                            "and unpaid awards "
                            "are disclosed "
                            "separately rather "
                            "than added to "
                            "revenue. The "
                            "successor receives "
                            "case-level receipt "
                            "links, cost "
                            "allocations, calendar "
                            "ownership, and "
                            "signed reconciliation "
                            "records."
                        ),
                    ),
                ],
                "completion_gate": (
                    "The owner signs the 30-day deliverable register, role coverage, "
                    "KPI definitions, risk responses, canonical reconciliation, and "
                    "handoff index. Launch completion means a controlled operating "
                    "system and documented pipeline, not assumed awards or uncollected revenue."
                ),
            },
        ],
    }
