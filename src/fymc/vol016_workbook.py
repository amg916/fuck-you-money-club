from __future__ import annotations


def build_volume_016_workbook() -> dict:
    def field(name: str, input_type: str, prompt: str, example: str) -> dict:
        return {
            "name": name,
            "type": input_type,
            "prompt": prompt,
            "example": example,
        }

    return {
        "workbook_id": "wb-016-probate-real-estate",
        "volume_id": "vol-016-probate-real-estate",
        "title": "Probate Real Estate — Operator Companion Workbook",
        "subtitle": (
            "6 Printable Operator Worksheets for Probate Deal Qualification, "
            "Retained-Commission Economics, Executor Concierge Delivery, Court-Sale "
            "Controls, Attorney Referral Systems, and Small-Team Operating Readiness"
        ),
        "worksheets": [
            {
                "worksheet_id": "ws-01",
                "number": 1,
                "title": "Opportunity Underwriting and Fiduciary Counterparty Qualification",
                "purpose": (
                    "Select probate brokerage opportunities that fit the team's license, "
                    "court experience, cash runway, and service capacity. Separate an "
                    "estate's property value from brokerage revenue, establish who can "
                    "instruct the broker, and expose title, authority, occupancy, and "
                    "family conflicts before committing substantial work."
                ),
                "chapter_ref": "Q1, Q2, Q6",
                "instructions": [
                    (
                        "Choose one initial county and one service lane. Record the "
                        "applicable probate court, supervising broker, property profile, and "
                        "expected appointment-to-closing interval. Treat acquisitions and "
                        "executor concierge work as separately contracted activities rather "
                        "than automatic extensions of a brokerage listing."
                    ),
                    (
                        "Obtain the appointment documents and relevant orders from the "
                        "authorized representative or court record. Have estate counsel "
                        "identify the representative's powers, restrictions, and required "
                        "sale procedure. Do not treat a relative's possession of keys "
                        "as authority to list."
                    ),
                    (
                        "Build a counterparty map covering the representative, estate "
                        "attorney, beneficiaries, occupants, lender, title officer, and "
                        "prospective buyers. Distinguish decision authority from consultation "
                        "preferences, and document the permitted recipients of confidential "
                        "pricing, offer, and estate information."
                    ),
                    (
                        "Underwrite property condition, liens, occupancy, access, insurance, "
                        "and carrying costs before projecting commission timing. Use a "
                        "dated comparative market analysis and scenario ranges. Track "
                        "potential family objections as procedural and scheduling risks, "
                        "not as presumed authority to veto."
                    ),
                    (
                        "Conclude with a written pursuit decision and assigned next "
                        "action. Reject opportunities requiring unlicensed representation, "
                        "undisclosed self-dealing, unsupported authority, or cash advances "
                        "outside policy. Keep unresolved documents visible with owners "
                        "and dates rather than replacing them with optimistic assumptions."
                    ),
                ],
                "fields": [
                    field(
                        "Initial county and service lane",
                        "textarea",
                        (
                            "Define the initial geographic market, court, property segment, "
                            "licensed activity, and concierge boundaries. Explain why the "
                            "team can serve this lane without depending on unfamiliar "
                            "procedures or speculative acquisition profits."
                        ),
                        (
                            "Start with Sacramento County single-family probate listings "
                            "priced from $450,000 to $800,000. The California supervising "
                            "broker handles representation; the coordinator schedules "
                            "estate-authorized vendors. Purchases by the operator require "
                            "a separate conflict review and purchase file, and contribute "
                            "nothing to the brokerage scorecard forecast."
                        ),
                    ),
                    field(
                        "Candidate fit and leverage thesis",
                        "textarea",
                        (
                            "Record the candidate's canonical rank, score components, and "
                            "operating constraints. Identify the specific repetitive tasks "
                            "that automation can remove while preserving licensed judgment "
                            "and representative control over consequential decisions."
                        ),
                        (
                            "Candidate #9, Probate Real Estate, ranks #26 of 29 with "
                            "80/100: revenue potential 23, margin potential 20, team efficiency 16, startup accessibility 10, and automation potential 11. "
                            "Docket alerts and transaction checklists support the "
                            "High-Leverage Operator Play; they do not replace court "
                            "interpretation or negotiations."
                        ),
                    ),
                    field(
                        "Representative identity and documented authority",
                        "textarea",
                        (
                            "Identify the appointed representative, appointment date, "
                            "current letters, relevant restrictions, and counsel's procedure "
                            "assessment. Specify what evidence must exist before the "
                            "broker accepts instructions, access permissions, or a listing agreement."
                        ),
                        (
                            "Case PR-2026-0412 names Jordan Lee as personal representative. "
                            "The file contains current Letters of Administration and "
                            "the appointment order; counsel confirms full IAEA authority "
                            "and checks for restrictions. Jordan signs the listing only "
                            "after the broker verifies identity and matches the signing capacity."
                        ),
                    ),
                    field(
                        "Counterparty communication and dispute map",
                        "textarea",
                        (
                            "Map who instructs the broker, who receives updates, and "
                            "who may object through the applicable procedure. Record "
                            "actual disputes and communication permissions without assuming "
                            "every beneficiary controls pricing or contract execution."
                        ),
                        (
                            "Jordan instructs the broker; estate counsel receives legal "
                            "questions; three beneficiaries receive an authorized Friday "
                            "status summary. One beneficiary disputes the proposed cleanout "
                            "budget. The broker records the concern and routes it to "
                            "Jordan and counsel rather than collecting informal beneficiary signatures."
                        ),
                    ),
                    field(
                        "Property condition and access underwriting",
                        "textarea",
                        (
                            "Describe occupancy, utilities, security, insurance, deferred "
                            "maintenance, and inspection access. Separate observed facts "
                            "from estimates, identify qualified vendors, and assign the "
                            "representative responsibility for authorizing estate expenditures."
                        ),
                        (
                            "The $625,000 target property is vacant with active utilities "
                            "and a leaking garage roof. Jordan authorizes a $450 "
                            "inspection and obtains vacant-property coverage confirmation. "
                            "The coordinator logs lockbox access; no belongings leave "
                            "the house until the representative gives written disposition instructions."
                        ),
                    ),
                    field(
                        "Title debt and estate proceeds bridge",
                        "textarea",
                        (
                            "List preliminary liens, payoff estimates, taxes, selling "
                            "costs, and title exceptions. Calculate illustrative estate "
                            "proceeds separately from brokerage receipts, identifying "
                            "items that require updated demands or title clearance before closing."
                        ),
                        (
                            "At a $625,000 sale, subtract a $210,000 mortgage, $12,000 "
                            "tax lien, $18,750 negotiated listing-side commission, and "
                            "$14,250 other estimated selling costs: provisional estate "
                            "proceeds equal $370,000. The operator retains $15,000 after "
                            "the assumed brokerage split; payoff interest and final settlement charges remain subject to reconciliation."
                        ),
                    ),
                    field(
                        "Sale route and court timing",
                        "textarea",
                        (
                            "Identify whether the proposed transaction uses independent "
                            "administration or a court-supervised sale route. Record "
                            "counsel's required notices, objection handling, hearing "
                            "dependencies, and timing assumptions rather than promising a fixed closing date."
                        ),
                        (
                            "Counsel selects a full-authority IAEA sale subject to "
                            "the applicable notice process under California Probate "
                            "Code sections 10580–10589. The planning calendar allows "
                            "notice time plus a 30-day buyer escrow. An objection "
                            "moves the file to counsel's revised procedure before any closing commitment."
                        ),
                    ),
                    field(
                        "Pricing evidence and downside sensitivity",
                        "textarea",
                        (
                            "Document comparable sales, condition adjustments, valuation "
                            "date, and the effect of a lower sale price on retained "
                            "commission. State the negotiated rate and split explicitly; "
                            "never present either as an industry requirement."
                        ),
                        (
                            "Three adjusted comparable sales support $600,000 to "
                            "$650,000, with $625,000 used for planning. At an illustrative "
                            "negotiated 3% listing-side rate and 80% retention, operator "
                            "revenue is $15,000. A 10% price reduction produces $562,500 "
                            "of sale value and $13,500 of retained commission."
                        ),
                    ),
                    field(
                        "Acquisition and concierge conflict screen",
                        "textarea",
                        (
                            "Identify operator ownership interests, proposed purchases, "
                            "vendor relationships, and concierge compensation. Describe "
                            "how conflicts are disclosed and evaluated before proceeding, "
                            "including alternatives that preserve independent representation and estate decision-making."
                        ),
                        (
                            "An affiliated acquisition entity offers $540,000 while "
                            "the listing analysis supports $625,000 before condition "
                            "adjustments. The broker discloses ownership, stops using "
                            "confidential seller leverage in acquisition negotiations, "
                            "and asks counsel to assess the conflict and proposed procedure. "
                            "The forecast excludes acquisition resale gains."
                        ),
                    ),
                    field(
                        "Pursuit decision and resource ceiling",
                        "textarea",
                        (
                            "State pursue, defer, or decline with evidence-based reasons, "
                            "an initial labor budget, cash exposure limit, and next "
                            "review date. Tie the decision to authority, economics, "
                            "property readiness, and realistic closing dependencies."
                        ),
                        (
                            "Pursue after authority verification, preliminary title "
                            "review, and signed representation documents. Limit "
                            "pre-listing work to 12 staff hours and $600 of brokerage "
                            "spending; estate vendors invoice the estate directly. "
                            "Review in seven days if access or insurance remains unresolved "
                            "and defer marketing until those issues are cleared."
                        ),
                    ),
                ],
                "completion_gate": (
                    "The supervising broker records a pursuit decision supported by "
                    "verified signing authority, a documented sale route, preliminary "
                    "property and title findings, a retained-commission estimate, and "
                    "named owners for every unresolved condition."
                ),
            },
            {
                "worksheet_id": "ws-02",
                "number": 2,
                "title": "Retained-Commission Economics, Defect Reserve, and Cash Float",
                "purpose": (
                    "Reconcile the canonical revenue and owner-profit scenarios to "
                    "retained brokerage commissions. Build a case-level cost bridge, "
                    "an explicit failed-file allowance, and a cash timing plan that "
                    "keeps estate money separate while exposing the funding gap "
                    "created by delayed probate closings."
                ),
                "chapter_ref": "Q3, Q4",
                "instructions": [
                    (
                        "Enter all three canonical scenarios unchanged before adding "
                        "local assumptions. Show sale value, gross listing-side commission, "
                        "brokerage split, retained operator revenue, total costs, and "
                        "owner net profit as separate quantities. Do not substitute "
                        "property appreciation or acquisition proceeds for commissions."
                    ),
                    (
                        "Use negotiated commission and retention assumptions solely "
                        "to construct a transparent unit model. Match annual retained "
                        "revenue through closed-file counts, and distinguish realized "
                        "closings from signed listings, pending escrows, and probability-weighted "
                        "pipeline values that have not yet earned revenue."
                    ),
                    (
                        "Allocate recurring overhead, people costs, direct case costs, "
                        "and failed-file allowances without counting any item twice. "
                        "Explain which costs sit inside the monthly operating envelope "
                        "and which require additional cash. Reconcile the complete "
                        "annual expense total to the canonical margin."
                    ),
                    (
                        "Forecast cash by expected receipt and payment date rather "
                        "than by annual averages alone. Stress a court delay and "
                        "a reduced sale price separately. Never use estate deposits, "
                        "trust funds, or vendor reimbursements to conceal the brokerage's "
                        "own working-capital shortfall."
                    ),
                    (
                        "Set numerical hiring and spending conditions based on "
                        "available unrestricted cash, committed funding, and documented "
                        "costs. Keep launch capital separate from the mature team's "
                        "annual economics, and show what happens when the first "
                        "commission arrives near the far end of the timing range."
                    ),
                ],
                "fields": [
                    field(
                        "Canonical scenario reconciliation",
                        "textarea",
                        (
                            "Write the three annual revenue, margin, owner-profit, "
                            "expense, and staffing combinations. Verify revenue multiplied "
                            "by margin equals owner profit, and revenue less profit "
                            "equals the complete implied expense envelope."
                        ),
                        (
                            "Conservative: $120,000 revenue, 20% margin, $24,000 profit, "
                            "$96,000 costs, 2 FT + 3 C. Base: $510,000 revenue, "
                            "27.5% margin, $140,250 profit, $369,750 costs, 2 FT + "
                            "3 C. Scaled: $900,000 revenue, 35% margin, $315,000 "
                            "profit, $585,000 costs, 3 FT + 4 C."
                        ),
                    ),
                    field(
                        "Sale value to retained commission bridge",
                        "textarea",
                        (
                            "Calculate a representative closing from property sale "
                            "value through negotiated listing-side commission and "
                            "brokerage retention. Identify the recipient of each amount "
                            "and the distinct recognition event for operator revenue."
                        ),
                        (
                            "A $625,000 closing at an illustrative negotiated 3% "
                            "listing-side commission generates $18,750 before the "
                            "brokerage split. At 80% operator retention, $15,000 "
                            "reaches the operator and $3,750 remains with the "
                            "brokerage. Record the retained amount under the accountant's "
                            "earned-revenue policy, not when the listing is signed."
                        ),
                    ),
                    field(
                        "Annual closing count and property throughput",
                        "textarea",
                        (
                            "Convert each scenario into an illustrative count of "
                            "completed transactions. Reconcile aggregate property "
                            "throughput separately from retained revenue, using explicit "
                            "average prices, negotiated commission assumptions, and brokerage retention percentages."
                        ),
                        (
                            "Conservative uses 10 closings at $500,000, producing "
                            "$5,000,000 property throughput and $120,000 retained "
                            "revenue at 3% commission and 80% retention. Base uses "
                            "34 closings at $625,000: $21,250,000 throughput and "
                            "$510,000 revenue. Scaled uses 60 identical units: "
                            "$37,500,000 throughput and $900,000 revenue."
                        ),
                    ),
                    field(
                        "Base expense architecture and unit margin",
                        "textarea",
                        (
                            "Build an illustrative expense schedule that sums exactly "
                            "to the base expense envelope. Identify personnel, recurring "
                            "overhead, case spending, and expected losses, then calculate "
                            "fully allocated cost and profit per closing."
                        ),
                        (
                            "Budget $108,000 recurring overhead, $216,000 people "
                            "costs, $32,250 direct case spending, and $13,500 "
                            "expected failed-file losses: total $369,750. People "
                            "costs comprise $156,000 for two full-time roles and "
                            "$60,000 across three contractors. Across 34 closings, "
                            "cost is $10,875 and owner profit is $4,125 each."
                        ),
                    ),
                    field(
                        "Scrub defects and failed-file allowance",
                        "textarea",
                        (
                            "Define the events that consume the loss allowance, "
                            "including duplicate leads, authority defects, abandoned "
                            "listings, and unrecovered case spending. Separate an "
                            "internal budgeting allowance from actual accounting treatment and restricted cash."
                        ),
                        (
                            "Allocate the $13,500 management allowance as $3,000 "
                            "for docket and identity rework, $4,500 for unrecovered "
                            "inspection or marketing commitments, and $6,000 for "
                            "abandoned-file labor. Review actual losses monthly. Moving "
                            "$13,500 into a reserve account creates no second expense; "
                            "the accountant controls recorded expense recognition."
                        ),
                    ),
                    field(
                        "Startup capital and first-deal runway",
                        "textarea",
                        (
                            "Place the launch plan within the canonical startup "
                            "capital and first-deal ranges. Separate one-time setup "
                            "from liquid runway and show the consequence of a "
                            "late first closing without assuming the mature team already exists."
                        ),
                        (
                            "Canonical startup capital is $15,000–$100,000 and "
                            "time to first deal is 4–18 months. A $90,000 "
                            "launch budget spends $15,000 on setup and leaves "
                            "$75,000 liquid. A staged $6,000 monthly burn lasts "
                            "12.5 months; reaching month 18 requires another "
                            "$33,000 or documented reductions before committing."
                        ),
                    ),
                    field(
                        "Monthly operating envelope and mature float",
                        "textarea",
                        (
                            "Explain how the quoted monthly operating range maps "
                            "to this budget. Calculate mature-team cash requirements "
                            "using all relevant costs rather than treating recurring "
                            "overhead as the entire expense base."
                        ),
                        (
                            "The canonical monthly opex range is $3,000–$18,000. "
                            "For this worksheet, $9,000 is recurring non-personnel "
                            "overhead, with $18,000 monthly people costs shown "
                            "separately. Fixed cash demand is therefore $27,000 "
                            "monthly, and 90 days requires $81,000 before direct "
                            "case costs. This scope assumption must accompany the budget."
                        ),
                    ),
                    field(
                        "Court-delay and price stress",
                        "textarea",
                        (
                            "Stress delayed receipts and reduced sale prices without "
                            "altering the canonical scenario labels. Quantify cash "
                            "timing effects separately from profit effects, and state "
                            "which cost assumptions remain fixed in the sensitivity."
                        ),
                        (
                            "Moving two $15,000 commissions beyond the quarter "
                            "creates a $30,000 receipt shortfall without automatically "
                            "destroying lifetime revenue. Separately, a 10% price "
                            "decline across 34 base closings reduces retained revenue "
                            "to $459,000. Holding modeled costs at $369,750 leaves "
                            "$89,250 profit; this is a sensitivity, not the canonical base."
                        ),
                    ),
                    field(
                        "Break-even volume and contribution logic",
                        "textarea",
                        (
                            "Separate fixed annual costs from variable case costs "
                            "and expected losses. Calculate contribution per completed "
                            "closing and the whole-number closing count required "
                            "to cover fixed costs under the stated assumptions."
                        ),
                        (
                            "Treat $324,000 of overhead and people costs as fixed. "
                            "Allocate $45,750 of case spending and expected losses "
                            "across 34 closings, or approximately $1,345.59 each. "
                            "At $15,000 retained revenue, contribution is approximately "
                            "$13,654.41. Fixed-cost break-even is 23.73 closings, "
                            "rounded upward to 24 completed transactions."
                        ),
                    ),
                    field(
                        "Cash ownership and funding decision",
                        "textarea",
                        (
                            "Identify unrestricted brokerage cash, estate funds, "
                            "trust deposits, proposed borrowing, and the next spending "
                            "decision. Specify evidence required before treating "
                            "future receipts or a credit facility as available working capital."
                        ),
                        (
                            "The operator has $62,000 unrestricted cash against "
                            "an $81,000 fixed-cost float target, leaving a "
                            "$19,000 gap before case spending. A proposed $25,000 "
                            "credit line counts only after execution and availability "
                            "verification. Buyer earnest money remains with the "
                            "authorized holder and cannot fund payroll or marketing."
                        ),
                    ),
                ],
                "completion_gate": (
                    "All canonical scenarios reconcile exactly; the base cost schedule "
                    "totals $369,750; property throughput never appears as operator "
                    "revenue; and the owner records a funded cash plan or specific "
                    "spending reductions for the identified runway shortfall."
                ),
            },
            {
                "worksheet_id": "ws-03",
                "number": 3,
                "title": "Execution Ledger and Transaction QA Pre-Flight",
                "purpose": (
                    "Turn a qualified probate opportunity into a controlled transaction "
                    "file. Assign evidence, owners, and deadlines from intake through "
                    "closing, preserve a clear commission ledger, and test the "
                    "technical controls that prevent stale authority, premature marketing, "
                    "misdirected funds, and incomplete handoffs."
                ),
                "chapter_ref": "Q7, Q8",
                "instructions": [
                    (
                        "Create a unique case identifier before importing documents "
                        "or assigning tasks. Use the same identifier in the CRM, "
                        "document folder, transaction checklist, and accounting reference. "
                        "Keep sensitive identity and estate documents outside broadly "
                        "shared prospecting views and marketing exports."
                    ),
                    (
                        "Define each transaction state by evidence rather than "
                        "elapsed time. A signed listing does not prove authority "
                        "remains current, a hearing date does not prove confirmation, "
                        "and an accepted offer does not establish that required "
                        "notices or objections have been resolved."
                    ),
                    (
                        "Assign one accountable owner for every deadline and "
                        "one backup for absences. Record the source of each date "
                        "and counsel's procedural instructions. Treat software reminders "
                        "as operational aids, while preserving the underlying order, "
                        "notice, contract, or verified court entry."
                    ),
                    (
                        "Reconcile the draft settlement statement to negotiated "
                        "compensation, the brokerage split, and authorized credits. "
                        "Verify payment instructions through a trusted independent "
                        "channel. Keep estate distributions, buyer deposits, and "
                        "operator receipts in separate ledger categories with explicit ownership."
                    ),
                    (
                        "Run a pre-closing review and a post-closing exception "
                        "review. Test document access, duplicate prevention, deadline "
                        "calculation, and receipt matching. Record failed checks "
                        "with corrective actions and retest results rather than "
                        "marking the entire file complete because funds were received."
                    ),
                ],
                "fields": [
                    field(
                        "Case identity and source register",
                        "textarea",
                        (
                            "Define the identifiers and source metadata needed to "
                            "connect court records, property records, contacts, and "
                            "transaction documents. Explain how duplicate estates "
                            "and multiple properties belonging to one estate remain distinguishable."
                        ),
                        (
                            "Use estate ID EST-0412 and property ID EST-0412-P01. "
                            "Store the court case number, county, parcel number, "
                            "source URL, and retrieval timestamp. A second property "
                            "becomes P02 rather than a second estate. Match new "
                            "imports on county plus case number before creating another representative contact."
                        ),
                    ),
                    field(
                        "Evidence-based transaction states",
                        "textarea",
                        (
                            "List the operational states and documentary requirements "
                            "for moving between them. Include a suspended state "
                            "for authority changes, objections, access failures, "
                            "or contract issues that require review before further execution."
                        ),
                        (
                            "States are prospect, authority review, engaged, preparation, "
                            "active listing, under contract, closing ready, closed, "
                            "and suspended. Engaged requires verified authority and "
                            "executed representation documents. Closing ready requires "
                            "counsel's procedure confirmation, title clearance, and "
                            "escrow readiness. A new authority restriction moves "
                            "the file to suspended immediately."
                        ),
                    ),
                    field(
                        "Document custody and access matrix",
                        "textarea",
                        (
                            "Specify where originals and working copies are stored, "
                            "which roles can access sensitive material, and how "
                            "version history is preserved. Define a narrow "
                            "document-sharing procedure for vendors and external counterparties."
                        ),
                        (
                            "Google Drive contains a restricted estate folder "
                            "with separate authority, title, offers, and closing "
                            "subfolders. The coordinator can manage checklists but "
                            "cannot export identity documents. A cleanout vendor "
                            "receives only the property address, access window, "
                            "scope, and representative authorization through a limited-access folder."
                        ),
                    ),
                    field(
                        "Deadline ledger and calendar validation",
                        "textarea",
                        (
                            "Record each deadline's triggering event, source "
                            "document, calculation method, owner, and backup. "
                            "Explain how the team checks weekends, holidays, "
                            "service rules, and amended orders before relying on a software date."
                        ),
                        (
                            "The notice task records the notice document, "
                            "counsel-approved service date, applicable objection "
                            "period, and calculated earliest action date. The "
                            "coordinator enters reminders seven and two days "
                            "before review; the broker checks counsel's instructions. "
                            "An amended order replaces the operative deadline while preserving the original audit entry."
                        ),
                    ),
                    field(
                        "Vendor authorization and reimbursement ledger",
                        "textarea",
                        (
                            "Document vendor scope, approving party, spending "
                            "ceiling, invoice recipient, and completion evidence. "
                            "Separate estate expenses from brokerage expenses "
                            "and identify any reimbursement agreement before the operator advances funds."
                        ),
                        (
                            "Jordan authorizes a $2,800 cleanout contract payable "
                            "directly by the estate. The vendor supplies insurance "
                            "evidence, before-and-after photographs, and an itemized "
                            "invoice. The brokerage separately spends $450 on "
                            "photography as its own marketing cost. Neither "
                            "amount is added to retained commission revenue."
                        ),
                    ),
                    field(
                        "Offer comparison and decision evidence",
                        "textarea",
                        (
                            "Compare offers using net proceeds, funding evidence, "
                            "contingencies, closing dependencies, and required court "
                            "procedure. Record the representative's decision "
                            "without allowing automated scoring to accept or reject a binding offer."
                        ),
                        (
                            "Offer A is $625,000 with a 17-day inspection "
                            "contingency and verified financing. Offer B is "
                            "$610,000 cash with a seven-day inspection period. "
                            "The broker prepares a net sheet for each and "
                            "explains procedural dependencies. Jordan chooses "
                            "A in writing after reviewing the documented tradeoffs."
                        ),
                    ),
                    field(
                        "Closing commission and receipt reconciliation",
                        "textarea",
                        (
                            "Tie the signed compensation terms to the settlement "
                            "statement, brokerage disbursement, bank receipt, "
                            "and accounting entry. Describe how credits, "
                            "changed terms, or payment discrepancies remain visible until resolved."
                        ),
                        (
                            "The closing statement shows $18,750 listing-side "
                            "commission. The brokerage retains $3,750 and "
                            "remits $15,000 to the operator. The coordinator "
                            "matches the disbursement statement and bank "
                            "receipt to EST-0412-P01; the bookkeeper records "
                            "$15,000 retained revenue. A $250 discrepancy "
                            "creates an exception, not an automatic revenue adjustment."
                        ),
                    ),
                    field(
                        "Payment instruction verification control",
                        "textarea",
                        (
                            "Define the independent verification procedure "
                            "for changed payment instructions, including "
                            "trusted contact sources, permitted communication "
                            "channels, and stop conditions. Preserve proof "
                            "of verification without exposing full account details in the CRM."
                        ),
                        (
                            "An email requests a new escrow account two "
                            "days before closing. The coordinator pauses "
                            "the request and calls escrow using the "
                            "number from the previously verified engagement "
                            "record, not the email. The file records "
                            "the verifier, callback time, and outcome; "
                            "account details remain in the restricted closing folder."
                        ),
                    ),
                    field(
                        "Technical pre-flight test cases",
                        "textarea",
                        (
                            "Write concrete tests for duplicate records, "
                            "missing authority, expired links, date changes, "
                            "and reconciliation errors. Specify expected "
                            "behavior and evidence so the team can "
                            "repeat the tests after an automation change."
                        ),
                        (
                            "Test five synthetic files: a repeated docket "
                            "event creates no duplicate task; missing "
                            "letters prevent engagement status; a vendor "
                            "cannot open identity documents; a changed "
                            "hearing date preserves history; and a "
                            "$14,750 receipt against $15,000 expected "
                            "creates a $250 exception. Save screenshots "
                            "and the test-run date."
                        ),
                    ),
                    field(
                        "Closing handoff and retained evidence",
                        "textarea",
                        (
                            "Define the final deliverables, retention owner, "
                            "open-item review, and post-closing follow-up. "
                            "Identify what the broker may retain "
                            "and what should be removed from marketing "
                            "systems while preserving required transaction records."
                        ),
                        (
                            "Within five business days, archive the "
                            "executed agreement, authority evidence, required "
                            "notices, settlement statement, commission "
                            "reconciliation, and communications supporting "
                            "material decisions. The broker applies "
                            "California Business and Professions Code "
                            "section 10148 and any longer applicable "
                            "hold. Remove unnecessary identity attachments "
                            "from the prospecting CRM and confirm outstanding invoices."
                        ),
                    ),
                ],
                "completion_gate": (
                    "The broker and coordinator complete the evidence checklist, "
                    "resolve or formally assign every exception, demonstrate the "
                    "five technical tests, and reconcile expected commission to "
                    "the closing documents and actual bank receipt."
                ),
            },
            {
                "worksheet_id": "ws-04",
                "number": 4,
                "title": "Statutory, Licensing, Contract, and Outreach Audit",
                "purpose": (
                    "Translate applicable licensing, fiduciary, sale-procedure, "
                    "advertising, and outreach requirements into evidence the team "
                    "can actually inspect. Use California as the worked jurisdiction, "
                    "then replace its authorities when operating elsewhere instead "
                    "of carrying one state's probate workflow into another court."
                ),
                "chapter_ref": "Q5, Q9",
                "instructions": [
                    (
                        "Identify the property jurisdiction and the court "
                        "administering the estate before selecting statutes "
                        "or forms. Have qualified local counsel confirm "
                        "the sale route and material procedural requirements. "
                        "Record citations, verification dates, and the "
                        "transaction facts that make each requirement applicable."
                    ),
                    (
                        "Verify the supervising broker's license and "
                        "each worker's permitted activity. Review "
                        "representation, agency disclosures, compensation "
                        "terms, vendor agreements, and acquisition "
                        "conflicts before engagement. Administrative "
                        "support must not drift into negotiation "
                        "or other activity requiring a real estate license."
                    ),
                    (
                        "Build separate procedures for independent "
                        "administration and court-supervised sales. "
                        "Document required notices, objections, "
                        "appraisal conditions, confirmation, and "
                        "overbid mechanics where applicable. "
                        "A CRM status label cannot establish "
                        "that statutory prerequisites have been satisfied."
                    ),
                    (
                        "Audit attorney relationships and settlement-service "
                        "referrals for prohibited compensation. "
                        "Review outreach channels independently: "
                        "postal mail, live calls, texts, "
                        "automated calls, and commercial email "
                        "have different requirements. Public "
                        "court information does not create blanket permission to contact someone."
                    ),
                    (
                        "Convert every material issue into "
                        "a correction with an owner "
                        "and evidence deadline. Suspend "
                        "the affected activity when authority, "
                        "licensing, required procedure, or "
                        "contact permission is missing. "
                        "Preserve lawful work on other "
                        "parts of the file while the issue is resolved."
                    ),
                ],
                "fields": [
                    field(
                        "Jurisdiction and controlling procedure",
                        "textarea",
                        (
                            "Identify the property location, "
                            "probate court, administration type, "
                            "and applicable procedural sources. "
                            "State how the team verifies "
                            "current local rules and distinguishes "
                            "a general checklist from counsel's case-specific instructions."
                        ),
                        (
                            "The property and probate proceeding "
                            "are in Sacramento County, California. "
                            "Counsel checks the appointment order, "
                            "California Probate Code, and current "
                            "Sacramento Superior Court probate "
                            "rules. A property later identified "
                            "in Nevada receives a separate "
                            "jurisdiction review rather than inheriting "
                            "California notice and sale assumptions."
                        ),
                    ),
                    field(
                        "Broker licensing and worker scope",
                        "textarea",
                        (
                            "Record license verification evidence "
                            "and each role's permitted work. "
                            "Identify who negotiates, signs "
                            "brokerage documents, supervises "
                            "advertising, and handles administrative "
                            "tasks, citing the relevant licensing restriction for the worked jurisdiction."
                        ),
                        (
                            "California Business and Professions "
                            "Code section 10130 requires "
                            "licensure for covered brokerage "
                            "activity. The broker verifies "
                            "active DRE status before assignment. "
                            "The unlicensed coordinator schedules "
                            "inspections and assembles documents "
                            "but does not negotiate price "
                            "or compensation. Compensation arrangements "
                            "are checked against section 10137."
                        ),
                    ),
                    field(
                        "Representative authority and fiduciary conflicts",
                        "textarea",
                        (
                            "Document the representative's powers, "
                            "restrictions, and potential interests "
                            "in the buyer or vendors. "
                            "Identify facts requiring counsel's "
                            "review before a purchase, "
                            "advance, or related-party arrangement proceeds."
                        ),
                        (
                            "The representative proposes selling "
                            "to a company they own. "
                            "Counsel evaluates California Probate "
                            "Code sections 9880–9885 and "
                            "the specific facts before "
                            "any commitment. The broker "
                            "records ownership and alternative "
                            "marketing evidence. A relationship "
                            "disclosure alone is not treated "
                            "as permission for a restricted transaction."
                        ),
                    ),
                    field(
                        "IAEA notice and objection evidence",
                        "textarea",
                        (
                            "For an independent-administration sale, "
                            "record authority scope, required "
                            "notice recipients, service evidence, "
                            "objection handling, and any "
                            "applicable waiver. Avoid assuming "
                            "that full authority eliminates procedural notice or court involvement."
                        ),
                        (
                            "Counsel confirms full authority "
                            "and applies California Probate "
                            "Code sections 10580–10589. The "
                            "file contains the Notice "
                            "of Proposed Action, recipient "
                            "list, service evidence, and "
                            "counsel's timing calculation, including "
                            "the applicable minimum notice "
                            "period. A timely objection "
                            "halts the independent-action path "
                            "pending counsel's instructions."
                        ),
                    ),
                    field(
                        "Court-confirmed sale and overbid calculation",
                        "textarea",
                        (
                            "For a sale requiring confirmation, "
                            "record appraisal requirements, "
                            "accepted price, hearing terms, "
                            "and the statutory overbid "
                            "calculation. Explain that "
                            "meeting a numeric threshold "
                            "does not itself secure court confirmation."
                        ),
                        (
                            "For the applicable private "
                            "sale, California Probate Code "
                            "section 10309 requires at "
                            "least 90% of appraised "
                            "value, using an appraisal "
                            "within one year. A "
                            "$500,000 accepted bid has "
                            "a $525,500 initial statutory "
                            "overbid under section 10311: "
                            "$1,000 on the first "
                            "$10,000 plus $24,500 on the remainder."
                        ),
                    ),
                    field(
                        "Agency disclosures and negotiated compensation",
                        "textarea",
                        (
                            "Identify required agency disclosures, "
                            "the client's signing capacity, "
                            "compensation terms, and any "
                            "dual-agency issue. Specify "
                            "how the broker confirms "
                            "the applicable documents and "
                            "does not imply a mandatory commission rate."
                        ),
                        (
                            "The California file uses "
                            "applicable agency disclosures "
                            "under Civil Code sections "
                            "2079.14–2079.17. The listing "
                            "states an expressly negotiated "
                            "3% listing-side commission "
                            "and identifies the representative's "
                            "estate capacity. Any dual "
                            "agency receives the required "
                            "disclosure and consent, with "
                            "Business and Professions Code section 10176(d) reviewed."
                        ),
                    ),
                    field(
                        "Attorney referrals and settlement-service payments",
                        "textarea",
                        (
                            "Describe every benefit exchanged "
                            "with referral sources, "
                            "including fees, gifts, "
                            "shared marketing, and "
                            "free services. Identify "
                            "the transaction types "
                            "requiring RESPA review and "
                            "preserve evidence of genuine services rather than disguised referrals."
                        ),
                        (
                            "The attorney relationship plan "
                            "pays $0 for referrals. "
                            "For transactions involving "
                            "federally related mortgage "
                            "loans, review 12 U.S.C. "
                            "section 2607 and 12 "
                            "CFR section 1024.14. "
                            "A proposed $500 payment "
                            "per referred closing is "
                            "rejected. Genuine shared "
                            "educational expenses require separate "
                            "review of services, allocation, and other applicable rules."
                        ),
                    ),
                    field(
                        "Calls texts and email channel controls",
                        "textarea",
                        (
                            "Specify the outreach channel, "
                            "recipient category, suppression "
                            "checks, and any required "
                            "permission. Distinguish "
                            "manual business outreach "
                            "from consumer telemarketing "
                            "and automated messaging, "
                            "with a documented process for honoring stop requests."
                        ),
                        (
                            "Do not cold-text representatives "
                            "from docket records. "
                            "Consumer calling procedures "
                            "address 47 U.S.C. "
                            "section 227, 47 "
                            "CFR section 64.1200, "
                            "and applicable 16 "
                            "CFR section 310.4 "
                            "requirements, including registry "
                            "screening. Commercial email "
                            "follows 15 U.S.C. "
                            "section 7704, including accurate "
                            "headers, postal identification, and timely opt-out handling."
                        ),
                    ),
                    field(
                        "Fair housing and property advertising",
                        "textarea",
                        (
                            "Review listing copy, "
                            "audience selection, "
                            "offer handling, and "
                            "lead segmentation "
                            "for prohibited "
                            "discrimination or "
                            "misleading claims. "
                            "Define objective property "
                            "and service criteria that "
                            "replace protected-characteristic proxies in marketing decisions."
                        ),
                        (
                            "The broker reviews "
                            "advertising under 42 "
                            "U.S.C. section 3604 "
                            "and California Government "
                            "Code section 12955. "
                            "Copy describes three "
                            "bedrooms, step-free entry, "
                            "and inspection access "
                            "rather than preferred "
                            "occupants. Audience selection "
                            "uses service geography "
                            "and property needs, "
                            "not protected traits "
                            "or inferred family characteristics."
                        ),
                    ),
                    field(
                        "Data handling retention and correction register",
                        "textarea",
                        (
                            "Record data categories, "
                            "access controls, "
                            "retention rules, "
                            "privacy-law applicability, "
                            "and corrective actions. "
                            "Identify which public "
                            "record details are "
                            "unnecessary for outreach "
                            "and should never enter a marketing export."
                        ),
                        (
                            "Export only the "
                            "minimum lawful contact "
                            "and property fields; "
                            "exclude identity documents, "
                            "account numbers, and "
                            "beneficiary medical details. "
                            "Assess California Civil "
                            "Code section 1798.100 "
                            "et seq. applicability "
                            "and section 1798.81.5 "
                            "security duties. The "
                            "broker owns retention "
                            "review and corrects "
                            "an overbroad vendor "
                            "folder before restoring access."
                        ),
                    ),
                ],
                "completion_gate": (
                    "The supervising broker and appropriate local counsel have "
                    "resolved the applicable authority, sale-procedure, licensing, "
                    "contract, referral-payment, and outreach issues; evidence is "
                    "linked to the file, and unresolved activities remain suspended."
                ),
            },
            {
                "worksheet_id": "ws-05",
                "number": 5,
                "title": "Automation Pipeline, Attorney Flywheel, and Risk Fallbacks",
                "purpose": (
                    "Build a repeatable referral and execution system without "
                    "turning court records into indiscriminate outreach. Combine "
                    "authorized docket monitoring, structured qualification, useful "
                    "attorney relationships, and transaction checklists with "
                    "traceable data handling, measured conversion, and practical "
                    "fallbacks for automation failures and disrupted sale timelines."
                ),
                "chapter_ref": "Q6, Q10",
                "instructions": [
                    (
                        "List authorized information sources "
                        "and their access conditions "
                        "before configuring ingestion. "
                        "Prefer court-provided alerts "
                        "or permitted licensed feeds. "
                        "Record freshness, source "
                        "identifiers, and retrieval "
                        "errors so the CRM "
                        "can distinguish new evidence "
                        "from stale or duplicated records."
                    ),
                    (
                        "Automate collection, "
                        "deduplication, reminders, "
                        "and checklist preparation "
                        "before automating outreach. "
                        "Require qualified review "
                        "for authority interpretation, "
                        "procedural dates, pricing, "
                        "offer decisions, and "
                        "contractual commitments. "
                        "Test with synthetic "
                        "records before enabling any live workflow."
                    ),
                    (
                        "Build the attorney "
                        "flywheel around useful "
                        "estate-property work: "
                        "valuation explanations, "
                        "sale-route checklists, "
                        "vendor coordination, "
                        "and concise authorized "
                        "updates. Measure relationships "
                        "through qualified introductions "
                        "and completed service, "
                        "not payments or benefits contingent on referral volume."
                    ),
                    (
                        "Use a source-level "
                        "funnel with explicit "
                        "denominators and "
                        "conversion windows. "
                        "Separate newly created "
                        "opportunities from "
                        "prior-period closings. "
                        "Show acquisition cost "
                        "alongside staff capacity "
                        "and cash timing so "
                        "growth does not conceal an overloaded transaction pod."
                    ),
                    (
                        "Assign fallback owners "
                        "for unavailable feeds, "
                        "court postponements, "
                        "family disputes, "
                        "weak demand, "
                        "and vendor outages. "
                        "Define the operational "
                        "trigger and immediate "
                        "response for each. "
                        "An automation failure "
                        "must reduce convenience, not remove control over deadlines or client funds."
                    ),
                ],
                "fields": [
                    field(
                        "Authorized docket source and freshness",
                        "textarea",
                        (
                            "Identify the source, "
                            "permitted access "
                            "method, refresh "
                            "cadence, and "
                            "freshness threshold. "
                            "Specify how "
                            "the team verifies "
                            "a docket event "
                            "before using it "
                            "to alter a transaction deadline or contact status."
                        ),
                        (
                            "Use court-provided "
                            "notifications where "
                            "available or a "
                            "licensed feed permitting "
                            "the intended use. "
                            "Refresh each business "
                            "morning and flag "
                            "records older than "
                            "48 hours. A "
                            "new hearing event "
                            "creates a review "
                            "task; the coordinator "
                            "checks the underlying "
                            "entry before changing the operative calendar."
                        ),
                    ),
                    field(
                        "CRM schema and deduplication rules",
                        "textarea",
                        (
                            "Define the "
                            "minimum record "
                            "schema, stable "
                            "identifiers, merge "
                            "rules, and "
                            "suppression links. "
                            "Explain how "
                            "the workflow "
                            "handles repeated "
                            "events without "
                            "duplicating outreach, "
                            "erasing provenance, or merging different people who share a name."
                        ),
                        (
                            "Airtable stores "
                            "county, case "
                            "number, estate "
                            "ID, parcel "
                            "number, event "
                            "ID, source "
                            "timestamp, owner, "
                            "and review "
                            "status. County "
                            "plus case "
                            "number identifies "
                            "the estate; "
                            "contact merges "
                            "require additional "
                            "identity evidence. "
                            "A normalized "
                            "contact key "
                            "links suppression preferences across all campaigns."
                        ),
                    ),
                    field(
                        "Automation boundaries and review ownership",
                        "textarea",
                        (
                            "List tasks "
                            "the system "
                            "may perform "
                            "automatically and "
                            "decisions reserved "
                            "for a "
                            "qualified person. "
                            "Specify the "
                            "owner and "
                            "required evidence "
                            "for each "
                            "consequential status change or external communication."
                        ),
                        (
                            "A Python "
                            "job imports "
                            "permitted docket "
                            "events and "
                            "creates draft "
                            "tasks. It "
                            "cannot mark "
                            "authority verified, "
                            "send consumer "
                            "texts, accept "
                            "offers, or "
                            "release payment "
                            "instructions. The "
                            "broker confirms "
                            "representation status; "
                            "counsel supplies "
                            "procedure guidance; "
                            "the coordinator sends only reviewed, authorized updates."
                        ),
                    ),
                    field(
                        "Attorney relationship value proposition",
                        "textarea",
                        (
                            "Define a "
                            "specific service "
                            "promise for "
                            "probate attorneys, "
                            "the deliverables "
                            "supporting it, "
                            "and the "
                            "relationship cadence. "
                            "Exclude referral-contingent "
                            "payments and "
                            "avoid promising "
                            "legal conclusions or a closing date outside the broker's control."
                        ),
                        (
                            "Offer a "
                            "two-business-day property "
                            "intake response, "
                            "a documented "
                            "pricing analysis, "
                            "and an "
                            "authorized weekly "
                            "sale-status summary. "
                            "Meet eight "
                            "probate attorneys "
                            "during the "
                            "first quarter "
                            "to explain "
                            "the process. "
                            "Referrals earn "
                            "no payment; "
                            "service quality "
                            "and reliable "
                            "file updates create the reason to introduce another estate."
                        ),
                    ),
                    field(
                        "Outbound cadence and suppression handling",
                        "textarea",
                        (
                            "Describe the "
                            "initial audience, "
                            "message content, "
                            "follow-up limit, "
                            "and stop "
                            "conditions. "
                            "Make the "
                            "channel-specific "
                            "requirements visible "
                            "and state "
                            "how opt-outs "
                            "propagate before another employee or tool sends a message."
                        ),
                        (
                            "Send individually "
                            "reviewed commercial "
                            "emails to "
                            "20 relevant "
                            "probate-law firms "
                            "with a "
                            "clear service "
                            "description, postal "
                            "address, and "
                            "opt-out method. "
                            "Permit one "
                            "follow-up after "
                            "ten business "
                            "days. A "
                            "stop request "
                            "updates the "
                            "central suppression "
                            "list immediately "
                            "and is checked before every later campaign."
                        ),
                    ),
                    field(
                        "Base funnel and conversion assumptions",
                        "textarea",
                        (
                            "Construct an "
                            "illustrative annual "
                            "funnel that "
                            "reaches the "
                            "base closing "
                            "count. "
                            "Identify the "
                            "conversion denominator "
                            "at each "
                            "stage and "
                            "state whether "
                            "the model describes a mature pipeline or a newly launched business."
                        ),
                        (
                            "A mature "
                            "pipeline produces "
                            "200 qualified "
                            "introductions, 100 "
                            "consultations, 50 "
                            "signed listings, "
                            "and 34 "
                            "closings annually. "
                            "Stage conversions "
                            "are 50%, "
                            "50%, and "
                            "68%; overall "
                            "introduction-to-close conversion "
                            "is 17%. "
                            "At $15,000 "
                            "retained per "
                            "closing, revenue "
                            "is $510,000. "
                            "A new launch should not expect this annual output immediately."
                        ),
                    ),
                    field(
                        "Attribution cost and acquisition payback",
                        "textarea",
                        (
                            "Define source "
                            "attribution, direct "
                            "channel spending, "
                            "labor allocation, "
                            "and completed-deal "
                            "measurement. "
                            "Calculate a "
                            "transparent acquisition "
                            "cost without "
                            "claiming that "
                            "retained commission "
                            "equals contribution or adding existing expenses a second time."
                        ),
                        (
                            "Tag each "
                            "introduction with "
                            "its originating "
                            "relationship and "
                            "first-contact date. "
                            "An illustrative "
                            "$24,000 annual "
                            "outreach allocation "
                            "supporting 34 "
                            "closings equals "
                            "$705.88 per "
                            "closing before "
                            "separately allocated "
                            "labor. The "
                            "$24,000 already "
                            "sits inside "
                            "$108,000 overhead; "
                            "do not add it again when reconciling base profit."
                        ),
                    ),
                    field(
                        "Court delay and family dispute fallback",
                        "textarea",
                        (
                            "Specify the "
                            "trigger, owner, "
                            "communication plan, "
                            "and cash "
                            "response for "
                            "a postponed "
                            "hearing or "
                            "material family "
                            "dispute. "
                            "Identify what "
                            "work stops "
                            "and what property-protection tasks continue under valid authorization."
                        ),
                        (
                            "A hearing "
                            "moves by "
                            "60 days "
                            "while a "
                            "beneficiary challenges "
                            "the sale. "
                            "The coordinator "
                            "moves the "
                            "expected $15,000 "
                            "receipt out "
                            "of the "
                            "current cash "
                            "forecast. Counsel "
                            "directs the "
                            "procedural response; "
                            "the broker "
                            "pauses unsupported "
                            "closing promises. "
                            "Authorized insurance, "
                            "security, and maintenance tasks continue with weekly updates."
                        ),
                    ),
                    field(
                        "Housing-cycle response and capacity threshold",
                        "textarea",
                        (
                            "Define measurable "
                            "market and "
                            "capacity triggers "
                            "for adjusting "
                            "pricing advice, "
                            "spending, or "
                            "intake volume. "
                            "Preserve representative "
                            "control over "
                            "sale decisions "
                            "and avoid "
                            "treating increased leads as proof that the team can close more transactions."
                        ),
                        (
                            "If median "
                            "listing age "
                            "exceeds 60 "
                            "days or "
                            "showings fall "
                            "below two "
                            "weekly for "
                            "three weeks, "
                            "the broker "
                            "updates comparables "
                            "and presents "
                            "options to "
                            "the representative. "
                            "At more "
                            "than 12 "
                            "active files "
                            "per coordinator, "
                            "new intake "
                            "slows until "
                            "the broker verifies workload and funds additional capacity."
                        ),
                    ),
                    field(
                        "Failure monitoring and manual recovery",
                        "textarea",
                        (
                            "Document the "
                            "automation health "
                            "signals, alert "
                            "recipient, recovery "
                            "method, and "
                            "replay controls. "
                            "Specify how "
                            "the team "
                            "continues deadline "
                            "review during "
                            "an outage "
                            "without creating duplicate tasks or unauthorized communications."
                        ),
                        (
                            "A missing "
                            "daily heartbeat "
                            "by 10:00 "
                            "a.m. alerts "
                            "the coordinator. "
                            "They review "
                            "the authorized "
                            "court source "
                            "and the "
                            "exported active-file "
                            "deadline list "
                            "manually. Recovery "
                            "replays events "
                            "using stable "
                            "event IDs, "
                            "creates no "
                            "duplicate tasks, "
                            "and requires "
                            "a spot-check "
                            "of five files before scheduled processing resumes."
                        ),
                    ),
                ],
                "completion_gate": (
                    "The pipeline has authorized sources, tested duplicate protection, "
                    "central suppression handling, assigned review responsibilities, "
                    "a base funnel that reconciles to 34 closings, and a demonstrated "
                    "manual recovery path for docket and checklist outages."
                ),
            },
            {
                "worksheet_id": "ws-06",
                "number": 6,
                "title": "30-Day Launch Sprint, Pod Scorecard, and Exit-Readiness Ledger",
                "purpose": (
                    "Launch the operating system in 30 days without confusing "
                    "setup progress with earned commissions. Define accountable "
                    "roles, staged spending, measurable service quality, and "
                    "transferable records that support a durable small-team "
                    "brokerage while respecting the longer probate deal cycle."
                ),
                "chapter_ref": "Q11, Q12",
                "instructions": [
                    (
                        "Break the first "
                        "month into four "
                        "work packages "
                        "with named owners "
                        "and inspectable "
                        "deliverables. Prioritize "
                        "licensing, authority "
                        "review, cash "
                        "planning, and "
                        "file controls "
                        "before expanding "
                        "outreach. Treat "
                        "30 days as an operating-system launch, not a promised closing deadline."
                    ),
                    (
                        "Assign work by "
                        "licensed responsibility "
                        "and actual "
                        "capacity. Use "
                        "the canonical "
                        "staffing models "
                        "as scenario "
                        "references, but "
                        "stage hiring "
                        "against funded "
                        "runway and "
                        "case demand. "
                        "A contractor "
                        "label does not replace a worker-classification review or proper supervision."
                    ),
                    (
                        "Publish a weekly "
                        "scorecard containing "
                        "lead quality, "
                        "authority readiness, "
                        "file aging, "
                        "service reliability, "
                        "cash coverage, "
                        "and realized "
                        "retained revenue. "
                        "Give every "
                        "metric an "
                        "owner, denominator, "
                        "measurement period, and trigger that changes a specific operating decision."
                    ),
                    (
                        "Separate launch "
                        "acceptance tests "
                        "from mature "
                        "economic targets. "
                        "Demonstrate the "
                        "workflow on "
                        "synthetic records "
                        "and then "
                        "review authorized "
                        "live cases. "
                        "Record missed "
                        "deliverables honestly "
                        "and carry unresolved "
                        "items into the next sprint with assigned dates and resources."
                    ),
                    (
                        "Build transferability "
                        "from the "
                        "first month: "
                        "clean records, "
                        "documented processes, "
                        "reconciled receipts, "
                        "permission-aware data "
                        "exports, and "
                        "a second "
                        "person able "
                        "to operate "
                        "critical checklists. "
                        "Do not assume "
                        "client contracts, licenses, or referral relationships transfer automatically in a sale."
                    ),
                ],
                "fields": [
                    field(
                        "Days 1–7 foundation package",
                        "textarea",
                        (
                            "Assign the "
                            "first week's "
                            "jurisdiction, licensing, "
                            "authority, budget, "
                            "and workflow "
                            "deliverables. "
                            "Give each "
                            "item an "
                            "owner and "
                            "objective acceptance "
                            "evidence, including "
                            "the conditions that prevent premature marketing or spending."
                        ),
                        (
                            "By day "
                            "7, the "
                            "broker verifies "
                            "DRE status, "
                            "selects Sacramento "
                            "County, and "
                            "reviews the "
                            "representation packet. "
                            "The coordinator "
                            "creates the "
                            "case template "
                            "and access "
                            "matrix. The "
                            "owner approves "
                            "the $90,000 "
                            "launch plan "
                            "and identifies "
                            "the month-18 "
                            "cash gap. "
                            "No live listing begins without documented authority."
                        ),
                    ),
                    field(
                        "Days 8–14 workflow and testing package",
                        "textarea",
                        (
                            "Specify the "
                            "second week's "
                            "system configuration, "
                            "synthetic cases, "
                            "reconciliation tests, "
                            "and recovery "
                            "exercise. "
                            "Define what "
                            "must pass "
                            "before staff "
                            "use the "
                            "workflow for live confidential documents or external communications."
                        ),
                        (
                            "By day "
                            "14, create "
                            "five synthetic "
                            "cases and "
                            "run duplicate, "
                            "authority, access, "
                            "deadline-change, and "
                            "receipt-mismatch tests. "
                            "Disable the "
                            "docket importer "
                            "for one "
                            "exercise and "
                            "complete manual "
                            "review. The "
                            "broker checks "
                            "results; failed "
                            "permissions tests "
                            "block live "
                            "document uploads until corrected and retested."
                        ),
                    ),
                    field(
                        "Days 15–21 relationship and intake package",
                        "textarea",
                        (
                            "Define the "
                            "third week's "
                            "target audience, "
                            "reviewed outreach, "
                            "meeting goals, "
                            "and intake "
                            "quality checks. "
                            "Separate controllable "
                            "activity targets "
                            "from introductions "
                            "or engagements "
                            "that depend on independent counterparties choosing to respond."
                        ),
                        (
                            "Prepare 20 "
                            "reviewed law-firm "
                            "contacts, send "
                            "permitted individualized "
                            "messages, and "
                            "seek four "
                            "introductory meetings. "
                            "Actual meetings "
                            "are reported "
                            "separately from "
                            "invitations. For "
                            "each authorized "
                            "estate introduction, "
                            "the broker "
                            "reviews authority "
                            "and property "
                            "fit before "
                            "the coordinator "
                            "creates a live transaction file."
                        ),
                    ),
                    field(
                        "Days 22–30 launch acceptance package",
                        "textarea",
                        (
                            "Define the "
                            "final week's "
                            "evidence review, "
                            "cash check, "
                            "service rehearsal, "
                            "and next-month "
                            "decision. "
                            "Make launch "
                            "completion independent "
                            "of whether "
                            "a commission "
                            "has arrived, while keeping uncompleted deliverables visible."
                        ),
                        (
                            "By day "
                            "30, the "
                            "broker reviews "
                            "all active "
                            "files, the "
                            "owner refreshes "
                            "runway, and "
                            "the coordinator "
                            "rehearses the "
                            "Friday client "
                            "update. Accept "
                            "launch only "
                            "when critical "
                            "controls pass. "
                            "Record $0 "
                            "earned commission "
                            "if no "
                            "closing occurred; "
                            "the canonical "
                            "first-deal expectation remains 4–18 months."
                        ),
                    ),
                    field(
                        "Pod roles and staffing progression",
                        "textarea",
                        (
                            "Assign the "
                            "full-time and "
                            "contractor responsibilities "
                            "for the "
                            "canonical scenarios. "
                            "Explain how "
                            "the launch "
                            "stages capacity "
                            "and how "
                            "additional roles "
                            "are authorized "
                            "without assuming unpaid labor or automatic worker-classification outcomes."
                        ),
                        (
                            "Conservative and "
                            "base reference "
                            "2 FT "
                            "+ 3 C: "
                            "licensed lead, "
                            "transaction coordinator, "
                            "and three "
                            "specialist contractors. "
                            "Scaled uses "
                            "3 FT "
                            "+ 4 C, "
                            "seven people "
                            "total, adding "
                            "licensed capacity "
                            "and another "
                            "specialist. Launch "
                            "starts lean; "
                            "hiring requires "
                            "funded costs, "
                            "scope clarity, and applicable classification review."
                        ),
                    ),
                    field(
                        "Weekly leading-indicator scorecard",
                        "textarea",
                        (
                            "Specify leading "
                            "metrics with "
                            "targets, denominators, "
                            "owners, and "
                            "corrective actions. "
                            "Prioritize qualified "
                            "intake, evidence "
                            "readiness, service "
                            "timeliness, and "
                            "capacity rather "
                            "than raw "
                            "contact counts or unsourced claims about pipeline value."
                        ),
                        (
                            "The coordinator "
                            "reports qualified "
                            "introductions, consultations "
                            "held, authority-ready "
                            "files divided "
                            "by engaged "
                            "files, and "
                            "on-time updates "
                            "divided by "
                            "updates due. "
                            "Target 100% "
                            "authority readiness "
                            "and at "
                            "least 95% "
                            "timely updates. "
                            "Two missed "
                            "updates trigger "
                            "a workload "
                            "review before "
                            "additional intake is assigned."
                        ),
                    ),
                    field(
                        "Monthly realized-results scorecard",
                        "textarea",
                        (
                            "Define the "
                            "monthly revenue, "
                            "cost, profit, "
                            "cash, and "
                            "closing metrics. "
                            "Tie them "
                            "to actual "
                            "ledger evidence "
                            "and show "
                            "canonical annual "
                            "comparisons without "
                            "treating a monthly average as a predictable receipt schedule."
                        ),
                        (
                            "Base annual "
                            "targets are "
                            "34 closings, "
                            "$510,000 retained "
                            "revenue, $369,750 "
                            "costs, and "
                            "$140,250 owner "
                            "profit. Arithmetic "
                            "monthly averages "
                            "are $42,500 "
                            "revenue, $30,812.50 "
                            "costs, and "
                            "$11,687.50 profit. "
                            "The dashboard "
                            "shows actual "
                            "receipts and "
                            "earned revenue "
                            "separately because probate closings do not arrive evenly."
                        ),
                    ),
                    field(
                        "Thirty-day stop continue or adjust decision",
                        "textarea",
                        (
                            "State the "
                            "specific conditions "
                            "for continuing, "
                            "reducing spend, "
                            "changing the "
                            "service lane, "
                            "or pausing "
                            "new intake. "
                            "Use evidence "
                            "from runway, "
                            "qualified demand, "
                            "execution quality, and unresolved authority or licensing issues."
                        ),
                        (
                            "Continue the "
                            "county pilot "
                            "when controls "
                            "pass, outreach "
                            "produces relevant "
                            "conversations, and "
                            "the next "
                            "90 days "
                            "of committed "
                            "spending are "
                            "funded. Reduce "
                            "discretionary spend "
                            "if runway "
                            "falls below "
                            "six months "
                            "before reliable "
                            "receipts exist. "
                            "Pause affected "
                            "engagements immediately for unresolved authority or licensing defects."
                        ),
                    ),
                    field(
                        "Exit-readiness evidence and transfer restrictions",
                        "textarea",
                        (
                            "List the "
                            "records a "
                            "prospective successor "
                            "would need "
                            "to verify "
                            "earnings, workflow, "
                            "and client "
                            "obligations. "
                            "Identify restrictions "
                            "on contract "
                            "assignment, data "
                            "sharing, licensing, and referral continuity before preparing any external diligence package."
                        ),
                        (
                            "Maintain 24 "
                            "months of "
                            "reconciled retained-commission "
                            "records when "
                            "available, source "
                            "attribution, documented "
                            "procedures, vendor "
                            "terms, and "
                            "an exception "
                            "log. A "
                            "successor receives "
                            "redacted summaries "
                            "first. Counsel "
                            "reviews assignment "
                            "and confidentiality "
                            "terms; the "
                            "broker confirms "
                            "licensing requirements. "
                            "No valuation "
                            "assumes that estate listings or attorney relationships transfer automatically."
                        ),
                    ),
                    field(
                        "Key-person coverage and improvement ledger",
                        "textarea",
                        (
                            "Identify critical "
                            "tasks dependent "
                            "on one "
                            "person, name "
                            "a qualified "
                            "backup, and "
                            "schedule a "
                            "coverage exercise. "
                            "Record improvement "
                            "items with "
                            "evidence, owners, "
                            "and dates so transferability improves through tested operations rather than documentation alone."
                        ),
                        (
                            "The broker "
                            "is the "
                            "only current "
                            "negotiator, so "
                            "qualified licensed "
                            "coverage must "
                            "be arranged "
                            "before absence. "
                            "The coordinator "
                            "trains a "
                            "permitted backup "
                            "on deadline "
                            "review and "
                            "document permissions. "
                            "A two-day "
                            "coverage exercise "
                            "tests five "
                            "active-file tasks; "
                            "any missed "
                            "reminder receives "
                            "an owner, correction date, and repeat test."
                        ),
                    ),
                ],
                "completion_gate": (
                    "The 30-day deliverables are evidenced, critical controls have "
                    "passed their tests, the next spending period is funded or "
                    "reduced to available resources, scorecard ownership is assigned, "
                    "and the exit-readiness ledger distinguishes verified records "
                    "from future evidence still to be accumulated."
                ),
            },
        ],
    }
