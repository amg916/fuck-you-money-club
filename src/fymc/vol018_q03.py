from __future__ import annotations

CHAPTER_3 = {
    "id": "Q3",
    "chapter_id": "Q3",
    "chapter_number": 3,
    "question_number": 3,
    "slug": "land-flipping-unit-economics-margin-waterfall-working-capital",
    "question_prompt": "What are the real unit economics, gross-to-net margin deductions, scrub/reversal reserves, and working-capital float requirements for land flipping?",
    "kicker": "Q3 / THE BIG MONEY PLAYBOOKS",
    "title": "Unit Economics, Margin Waterfall & Working-Capital Float",
    "subtitle": "Parcel-Level Cost Basis, Escrow Release Timing, Heirs-Property Buyouts, GIS Screening & Title-Insured Cash Conversion",
    "layout_template": "financial_breakdown",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #6, Land Flipping, holds Rank #15 with a 86/100 Money-to-Manpower score. "
        "Its canonical annual owner profits are $24,000 Conservative, $157,250 Base, and "
        "$375,000 Scaled, measured against gross parcel sale proceeds rather than broker "
        "commissions. This chapter maps six operating plays: fractional heir-share acquisition, "
        "vacant-lot spread capture, infill feasibility arbitrage, minor-subdivision execution, "
        "access-defect resolution, and title-curative resale. Only the heir-share identifier "
        "comes from the supplied play mapping; the other five are chapter-specific applications. "
        "A reconciled waterfall separates purchase basis, contractor work, selling costs, "
        "customer acquisition, carrying charges, financing, reserves, and overhead. Cash-cycle "
        "tests expose why attractive accounting spreads can exhaust acquisition capital before "
        "escrow releases sale proceeds."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$200,000",
            "context": "Annual gross parcel sale proceeds; acquisition basis remains a cost.",
            "note": "12% net margin; $24,000 owner profit; 1 FT + 3 C",
        },
        {
            "label": "Base",
            "value": "$850,000",
            "context": "Annual gross parcel sale proceeds; acquisition basis remains a cost.",
            "note": "18.5% net margin; $157,250 owner profit; 1 FT + 3 C",
        },
        {
            "label": "Scaled",
            "value": "$1,500,000",
            "context": "Annual gross parcel sale proceeds; acquisition basis remains a cost.",
            "note": "25% net margin; $375,000 owner profit; 2 FT + 4 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Reconcile Every Parcel Dollar Before Calling the Spread Profit",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Start with closed parcel sales, not asking prices, signed offers, earnest "
                    "money, or the retail value of somebody else's property. The canonical "
                    "Conservative case is $200,000 revenue and $24,000 owner profit; Base is "
                    "$850,000 and $157,250; Scaled is $1,500,000 and $375,000. For a transparent "
                    "cohort reconstruction, assume respectively ten sales averaging $20,000, "
                    "twenty-five averaging $34,000, and thirty averaging $50,000. These deal "
                    "counts and expense allocations are illustrative, while the annual endpoints "
                    "are fixed. Revenue means gross proceeds from parcels the operator owns "
                    "and sells as principal. A broker representing another owner recognizes "
                    "their contractual compensation, not the owner's sale price; that is a "
                    "different business model. In QuickBooks Online or a controlled spreadsheet, "
                    "assign each parcel a permanent project code linked to its APN, purchase "
                    "deed, settlement statements, and disposition record. Keep county and "
                    "jurisdiction fields because APNs are not nationally unique. Reconcile "
                    "the gross contractual price to credits, seller-paid deductions, debt "
                    "payoffs, and actual bank receipts. The settlement wire is cash received, "
                    "not revenue by itself. Track concessions as reductions of price rather "
                    "than quietly preserving an obsolete listing valuation."
                ),
                (
                    "The waterfall below makes acquisition basis the largest deduction and "
                    "keeps every remaining cost visible. Purchase basis consumes $110,000, "
                    "$425,000, and $690,000 across the three cases. Closing and title budgets "
                    "cover allocated acquisition and disposition charges without counting a "
                    "broker commission twice. Contractor delivery includes survey coordination, "
                    "parcel research, field verification, and limited curative work; customer "
                    "acquisition covers list purchases, mail, answering services, and seller "
                    "follow-up. Carrying costs contain property taxes, insurance, and routine "
                    "site obligations; financing contains interest and allocated facility fees, "
                    "never principal repayment. The residual operating contribution before "
                    "overhead is $40,000, $242,250, and $525,000. Subtracting overhead of "
                    "$16,000, $85,000, and $150,000 produces the exact canonical owner profits. "
                    "Per closed parcel, that is $2,400, $6,290, and $12,500. Treat these as "
                    "management-model earnings before the owner's personal income taxes and "
                    "without an additional imputed salary for owner labor. The first "
                    "full-time seat is the working owner; the Scaled overhead budget includes "
                    "the second full-time employee. Contractor counts describe recurring "
                    "relationships, not full-time equivalents. Actual employment costs must "
                    "fit these envelopes or the scenario must be re-underwritten."
                ),
                (
                    "Separate planning reserves from recognized expenses when reconciling "
                    "management results to the books. This model deducts $2,000, $12,750, and "
                    "$30,000 for expected scrubs, valuation corrections, and exceptional "
                    "post-contract losses. Those allowances equal 1%, 1.5%, and 2% of sales. "
                    "Holding the same dollars in a savings account does not itself create "
                    "an accounting expense. Maintain a bridge showing modeled allowance, "
                    "actual losses, remaining exposure, and any permitted accounting provision "
                    "under the entity's reporting method. An earnest-money refund reverses "
                    "a deposit liability when appropriate; it is not automatically negative "
                    "revenue. A failed purchase can leave unrecoverable survey or counsel "
                    "spending even when the deposit returns. Repeatedly marketing land for "
                    "sale can also place property within the dealer-property exclusion in "
                    "26 U.S.C. 1221(a)(1), so do not price the business on assumed capital-gain "
                    "treatment. The stated $3,000–$15,000 monthly operating-budget range is a "
                    "planning reference, not a replacement for this ledger. Separate recurring "
                    "cash commitments from transaction-variable spending, and preserve an "
                    "explicit bridge whenever annual activity pushes total monthly cash "
                    "outflow beyond that range. Report cash profit, modeled profit, and "
                    "taxable income as distinct measures."
                ),
            ],
            "table": {
                "caption": "Reconciled Annual Land-Flipping Waterfall: Fixed Canonical Endpoints and Illustrative Cost Allocations",
                "headers": [
                    "Waterfall line and accounting treatment",
                    "Conservative annual cohort allocation",
                    "Base annual cohort allocation",
                    "Scaled annual cohort allocation",
                ],
                "rows": [
                    [
                        "Gross parcel proceeds recognized from completed principal sales",
                        "$200,000 from ten sales averaging $20,000 each",
                        "$850,000 from twenty-five sales averaging $34,000 each",
                        "$1,500,000 from thirty sales averaging $50,000 each",
                    ],
                    [
                        "Deduct purchase basis assigned to the parcels sold",
                        "$110,000 purchase basis, averaging $11,000 per closed parcel",
                        "$425,000 purchase basis, averaging $17,000 per closed parcel",
                        "$690,000 purchase basis, averaging $23,000 per closed parcel",
                    ],
                    [
                        "Deduct title, escrow, recording, and allocated closing charges",
                        "$10,000 closing charges, averaging $1,000 per completed sale",
                        "$34,000 closing charges, averaging $1,360 per completed sale",
                        "$45,000 closing charges, averaging $1,500 per completed sale",
                    ],
                    [
                        "Deduct contractor delivery labor and parcel-specific technical work",
                        "$8,000 contractor spending, averaging $800 per completed sale",
                        "$25,500 contractor spending, averaging $1,020 per completed sale",
                        "$45,000 contractor spending, averaging $1,500 per completed sale",
                    ],
                    [
                        "Deduct disposition commissions and transaction-linked selling expenses only",
                        "$12,000 disposition spending, modeled at 6% of proceeds",
                        "$51,000 disposition spending, modeled at 6% of proceeds",
                        "$75,000 disposition spending, modeled at 5% of proceeds",
                    ],
                    [
                        "Deduct seller acquisition campaigns and attributable conversion spending",
                        "$8,000 acquisition marketing, averaging $800 per completed sale",
                        "$25,500 acquisition marketing, averaging $1,020 per completed sale",
                        "$30,000 acquisition marketing, averaging $1,000 per completed sale",
                    ],
                    [
                        "Deduct property taxes, insurance, and recurring site obligations",
                        "$6,000 carrying charges, averaging $600 per completed sale",
                        "$17,000 carrying charges, averaging $680 per completed sale",
                        "$30,000 carrying charges, averaging $1,000 per completed sale",
                    ],
                    [
                        "Deduct interest and facility fees without deducting principal",
                        "$4,000 financing charges, averaging $400 per completed sale",
                        "$17,000 financing charges, averaging $680 per completed sale",
                        "$30,000 financing charges, averaging $1,000 per completed sale",
                    ],
                    [
                        "Deduct modeled scrub losses with separate accounting reconciliation",
                        "$2,000 expected losses, equivalent to 1% of proceeds",
                        "$12,750 expected losses, equivalent to 1.5% of proceeds",
                        "$30,000 expected losses, equivalent to 2% of proceeds",
                    ],
                    [
                        "Deduct overhead including applicable staff, systems, and administration",
                        "$16,000 overhead budget after separately allocated transaction expenses",
                        "$85,000 overhead budget after separately allocated transaction expenses",
                        "$150,000 overhead budget including the additional employee seat",
                    ],
                    [
                        "Retain canonical owner profit after all modeled deductions",
                        "$24,000 owner profit, retaining exactly 12% of proceeds",
                        "$157,250 owner profit, retaining exactly 18.5% of proceeds",
                        "$375,000 owner profit, retaining exactly 25% of proceeds",
                    ],
                ],
            },
        },
        {
            "heading": "2. Price Six Operating Plays Against Evidence, Not Imagined Upside",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Use the Base parcel as a common underwriting ruler: $34,000 resale, "
                    "$17,000 purchase basis, $1,360 closing charges, $1,020 contractor delivery, "
                    "$2,040 selling costs, $1,020 acquisition CAC, $680 carrying costs, $680 "
                    "financing, $510 expected losses, and $3,400 allocated overhead leave "
                    "$6,290. Vacant-lot spread capture earns that result only when a legally "
                    "usable parcel actually clears the assumed price. Infill feasibility "
                    "arbitrage replaces superficial price-per-acre comparisons with frontage, "
                    "setbacks, utility availability, lot coverage, and buildable-envelope "
                    "evidence. An extra $2,000 utility verification expense reduces the "
                    "same unit profit to $4,290 unless price or purchase basis changes. "
                    "QGIS can overlay county parcels, FEMA flood mapping, and municipal "
                    "zoning, but map geometry does not establish legal access or authorize "
                    "construction. Obtain the recorded easement and jurisdiction-specific "
                    "development requirements separately. Redfin and Zillow can provide "
                    "listing context; verified deeds and MLS closed-sale records provide "
                    "stronger transaction evidence when available. Save comparable selection "
                    "rules before receiving a seller's counteroffer, so enthusiasm cannot "
                    "silently replace the original underwriting standard. If utility or "
                    "buildability evidence fails, value the parcel for its supported use "
                    "and reprice before committing funds."
                ),
                (
                    "The mandatory TRACK_1 play, fractional_heir_share_partition_forcing, "
                    "requires a different liquidity model from fee-simple lot flipping. "
                    "Suppose a documented 25% tenancy-in-common interest costs $8,000 and "
                    "verified consensual buyout proceeds are $16,000. That $16,000 is the "
                    "operator's sale revenue; the property's hypothetical $100,000 whole-parcel "
                    "value is neither owned inventory nor operator revenue. A simplified "
                    "deal contribution deducts $8,000 basis, $3,000 counsel and title work, "
                    "$1,000 combined holding and financing, and $1,000 closing and selling "
                    "costs, leaving $3,000 before acquisition marketing, reserves, and "
                    "overhead. One additional $4,000 legal engagement makes that contribution "
                    "negative. Confirm the probate chain, ownership fraction, existing "
                    "agreements, liens, and actual applicability of heirs-property statutes "
                    "before purchasing. California's partition provisions, including Code "
                    "of Civil Procedure 874.316 and 874.317 where applicable, establish "
                    "buyout procedures and constraints on partition by sale. A purchased "
                    "minority interest does not promise a forced quick liquidation. Seek "
                    "consensual exits first; use counsel-supervised proceedings only when "
                    "available and economically justified. The fallback is renegotiating "
                    "voluntary exits or retaining the interest, never threatening remedies "
                    "the operator cannot lawfully obtain. Keep this example separate from "
                    "the canonical fee-simple cohort."
                ),
                (
                    "Minor-subdivision execution should be valued as a conditional conversion "
                    "project, not several already-saleable lots. An illustrative $70,000 "
                    "parent tract plus $20,000 engineering, $10,000 municipal charges, "
                    "$10,000 carrying and financing, and $10,000 closing and selling costs "
                    "requires $120,000 before CAC, reserves, or overhead. Three completed "
                    "lots selling for $50,000 each produce $30,000 contribution; only two "
                    "saleable lots produce a $20,000 loss. California Government Code 66424 "
                    "supplies a statutory subdivision definition, while local implementation "
                    "determines the actual review path. Access-defect resolution and "
                    "title-curative resale need equally explicit incremental budgets. Adding "
                    "a $4,000 recorded access solution to the Base parcel leaves $2,290 "
                    "owner profit if every other assumption holds. Adding $2,500 of title "
                    "curative work instead leaves $3,790; adding both leaves a $210 loss. "
                    "Require the title company to identify the proposed insured estate "
                    "and remaining exceptions, rather than treating a commitment as "
                    "completed coverage. Environmental diligence also follows the parcel's "
                    "history: former industrial use can warrant an environmental "
                    "professional and an assessment aligned with 40 CFR Part 312. If "
                    "cost or timing cannot be bounded, preserve the purchase contingency "
                    "or decline the project."
                ),
            ],
            "table": {
                "caption": "Six Play Applications: Incremental Unit Math, Evidence Requirements, and Capital-Preserving Fallbacks",
                "headers": [
                    "Operating play and ownership position",
                    "Illustrative unit contribution or profit calculation",
                    "Evidence required before underwriting the premium",
                    "Fallback when the value thesis breaks",
                ],
                "rows": [
                    [
                        "Vacant-lot spread capture using a principal-owned fee-simple parcel",
                        "$34,000 gross resale less $27,710 deductions leaves $6,290",
                        "Verify closed comparables, recorded access, taxes, and insurability",
                        "Reduce acquisition price or abandon unsupported resale assumptions",
                    ],
                    [
                        "Infill feasibility arbitrage based on documented development capacity",
                        "Additional $2,000 utility investigation reduces owner profit to $4,290",
                        "Obtain utility responses, zoning standards, and buildable-envelope analysis",
                        "Underwrite supported existing use rather than hypothetical construction",
                    ],
                    [
                        "Minor-subdivision execution after jurisdiction-specific parcel creation requirements",
                        "Three $50,000 lots less $120,000 costs leave $30,000 contribution",
                        "Confirm engineering scope, fees, access, utilities, and approval sequence",
                        "Resell the parent tract only at verified achievable pricing",
                    ],
                    [
                        "Access-defect resolution through enforceable, recorded property rights",
                        "Additional $4,000 access cure reduces Base profit to $2,290",
                        "Require executed easement documents and acceptable title treatment",
                        "Reprice as access-constrained land or terminate under contingency",
                    ],
                    [
                        "Title-curative resale after resolving specifically identified ownership defects",
                        "Additional $2,500 curative work reduces Base profit to $3,790",
                        "Collect recorded releases, corrected instruments, and updated title findings",
                        "Stop spending when counsel cannot bound remaining curative work",
                    ],
                    [
                        "fractional_heir_share_partition_forcing: documented fractional acquisition with co-owner protections",
                        "$16,000 buyout less $13,000 direct costs leaves $3,000 contribution",
                        "Verify probate chain, actual ownership fraction, and applicable protections",
                        "Renegotiate voluntary exits or retain without threatening unavailable remedies",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Buy the Evidence Before Buying the Story",
                "body": (
                    "Use small, bounded diligence expenditures to disprove the resale thesis "
                    "before purchase funds become illiquid inventory."
                ),
                "items": [
                    "Ask the title officer to identify the insured access position; compare the answer with recorded easements rather than a visible road.",
                    "Archive comparable-sale searches with dates and exclusion reasons, preventing later cherry-picking of oversized or utility-served lots.",
                    "Quote survey, probate, and access work by deliverable with stop-work limits; a cheap interest can otherwise become an open-ended legal project.",
                    "Offer consensual heir-share exits using documented valuation and counsel-reviewed terms; price an extended holding period into every offer.",
                ],
            },
        },
        {
            "heading": "3. Fund the Inventory Cycle and the Escrow Release Gap Separately",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Land trading is usually inventory-heavy rather than receivables-heavy. "
                    "Distinguish days from acquisition to an unconditional buyer closing, "
                    "days from closing to usable escrow proceeds, and genuine receivable "
                    "days after revenue recognition. For this liquidity illustration, assume "
                    "180 days from acquisition to sale closing and ten additional days "
                    "before funds are usable. The ten-day release assumption is a stress "
                    "input, not a statement that ordinary escrow universally holds money "
                    "that long. Confirm local recording, collected-funds rules, wire cutoffs, "
                    "and transaction-specific holdbacks with the closing agent. At Base "
                    "throughput, twenty-five annual sales times 190 days divided by 365 "
                    "creates 13.01 average capital-funded parcel equivalents. Deploying "
                    "$20,400 upfront per parcel, comprising basis, the full closing budget, "
                    "contractor delivery, and CAC, requires approximately $265,500. Funding "
                    "the entire closing budget early is deliberately conservative even "
                    "though some charges occur at disposition. Average accrued carrying "
                    "and financing costs add approximately $8,800 under a uniform-spend "
                    "assumption. Maintain a deal-level cash schedule because a stalled "
                    "subdivision or disputed heir interest cannot be represented faithfully "
                    "by the same 190-day cycle. Buyer deposits held in trust are not "
                    "available acquisition capital."
                ),
                (
                    "Add three months of Base overhead, $21,250, and a separately earmarked "
                    "$12,750 loss buffer to the approximately $274,300 deployed and accruing "
                    "capital. The resulting steady-state funding target is approximately "
                    "$308,300 before owner distributions or exceptional projects. Using "
                    "the same timing method gives approximately $79,400 Conservative and "
                    "$504,800 Scaled. Conservative upfront deployment is $13,600 per parcel; "
                    "Scaled is $27,000. Average carrying-plus-financing accrual per open "
                    "parcel is $500, $680, and $1,000 respectively. These are gross funding "
                    "requirements before subtracting any committed, drawable financing. "
                    "The Scaled requirement exceeds the supplied $400,000 upper startup "
                    "capital reference, so thirty annual sales at this cycle cannot simply "
                    "be declared self-funded within that range. Stage purchases, shorten "
                    "verified cycle times, recycle retained earnings, or arrange capital "
                    "whose availability and cost are documented. If a lender funds purchase "
                    "basis, subtract the actual advance from equity needed and add its "
                    "repayment to closing cash uses; do not subtract loan principal from "
                    "profit. Recalculate interest if leverage changes, since the fixed "
                    "financing allowance does not authorize unlimited borrowing. Keep owner "
                    "draws subordinate to the forecast cash trough rather than trailing "
                    "accounting profit."
                ),
                (
                    "Measure release delays as a daily capital requirement. A thirty-day "
                    "extension at Base throughput ties up approximately $43,300 more "
                    "capital using $21,080 average funded value per open parcel times "
                    "twenty-five annual sales times thirty divided by 365. That incremental "
                    "funding need is separate from approximately $5,667 of additional "
                    "annual carrying and financing expense if every parcel's original "
                    "180-day holding period extends by thirty days. Do not add the "
                    "entire trapped principal to the income statement. Maintain a rolling "
                    "thirteen-week cash forecast that identifies signed purchase obligations, "
                    "refundable diligence commitments, expected closings, and genuinely "
                    "drawable facilities. Show a second schedule with receipts delayed "
                    "thirty days and exclude disputed proceeds altogether until resolution "
                    "has a documented path. Seller financing requires another model: "
                    "recognized revenue, installment collections, servicing costs, defaults, "
                    "and tax timing can diverge sharply. The canonical cases here assume "
                    "cash dispositions, not a growing note portfolio. Contractors should "
                    "be paid against completed research, survey, or curative milestones, "
                    "but their agreed terms must remain credible; shifting every liquidity "
                    "problem onto a surveyor usually destroys delivery capacity. A funding "
                    "plan is workable only when both the cash amount and payment date "
                    "are supported."
                ),
            ],
            "table": {
                "caption": "Working-Capital Control Sheet: Inventory Days, Escrow Holds, and Available Cash",
                "headers": [
                    "Cash-cycle component and measurement boundary",
                    "Quantified assumption or operational calculation",
                    "Required evidence supporting the cash forecast",
                    "Operator response when timing deteriorates",
                ],
                "rows": [
                    [
                        "Inventory holding period before a completed cash disposition",
                        "Model 180 days from acquisition through sale closing",
                        "Track acquisition wires, listing dates, contracts, and closing records",
                        "Stop new commitments when delayed sales exceed funded capacity",
                    ],
                    [
                        "Escrow release interval before sale proceeds become spendable",
                        "Add ten illustrative days after the sale closing",
                        "Obtain actual escrow release terms and recording dependencies",
                        "Exclude held proceeds from currently available acquisition cash",
                    ],
                    [
                        "Base upfront deployment across the steady-state acquisition pipeline",
                        "$20,400 times twenty-five times 190 divided by 365",
                        "Tie purchase basis and allocated early costs to invoices",
                        "Reduce concurrent acquisitions before exhausting the overhead buffer",
                    ],
                    [
                        "Three scenario funding targets before committed financing offsets",
                        "Approximately $79,400 Conservative, $308,300 Base, and $504,800 Scaled",
                        "Include average accruals, three overhead months, and loss buffers",
                        "Stage Scaled deployment when available capital remains below requirement",
                    ],
                    [
                        "Incremental Base float caused by thirty additional cycle days",
                        "Approximately $43,300 additional funding before exceptional project costs",
                        "Recompute using actual open-parcel values and delayed receipt dates",
                        "Arrange documented liquidity without treating trapped principal as expense",
                    ],
                    [
                        "Available capital after restrictions, commitments, and distributions",
                        "Subtract restricted funds and committed purchases from bank cash",
                        "Reconcile bank balances, trust restrictions, facilities, and scheduled draws",
                        "Suspend discretionary owner distributions before missing contractual obligations",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Build a parcel cash ledger",
                    "action": "Assign dated purchase, diligence, holding, sale, and release events to each parcel.",
                    "detail": "Separate expected amounts from contractual obligations and retain the supporting statement or invoice.",
                },
                {
                    "step": 2,
                    "title": "Reconcile closing proceeds",
                    "action": "Bridge gross sale price to credits, selling deductions, debt repayment, and the bank wire.",
                    "detail": "Recognize principal repayment as a financing cash use rather than a second acquisition expense.",
                },
                {
                    "step": 3,
                    "title": "Project the cash trough",
                    "action": "Refresh thirteen weekly balances with a parallel thirty-day receipt-delay scenario.",
                    "detail": "Include payroll, property obligations, contractor milestones, restricted deposits, and facility availability.",
                },
                {
                    "step": 4,
                    "title": "Set the next acquisition limit",
                    "action": "Approve only purchase commitments supported after overhead and loss buffers remain funded.",
                    "detail": "Record the maximum cash deployment and revisit it whenever a sale slips or a cure expands.",
                },
            ],
        },
        {
            "heading": "4. Stress the Cohort and Stop Losses Before They Consume the Margin",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Stress price, purchase basis, acquisition CAC, and time independently "
                    "before combining them. The table holds annual unit counts constant "
                    "and changes only the stated driver. A 10% resale-price decline reduces "
                    "Conservative owner profit to $5,200, Base to $77,350, and Scaled to "
                    "$232,500 after allowing disposition costs to fall at their modeled "
                    "6%, 6%, and 5% rates. Other dollar budgets, including reserves, remain "
                    "fixed so the stress does not manufacture savings. A 10% purchase-basis "
                    "increase removes $11,000, $42,500, and $69,000 from profit respectively. "
                    "Doubling acquisition CAC leaves $16,000, $131,750, and $345,000. Express "
                    "CAC per closed acquisition, not per mailed name or signed contract: "
                    "a $25,500 campaign that produces fifty contracts but only twenty-five "
                    "completed purchases still costs $1,020 per purchase. Include failed "
                    "campaign spending in the cohort rather than allocating it only to "
                    "parcels that happened to sell. If annual purchases exceed sales, "
                    "separate pipeline investment from the matched sold-parcel analysis. "
                    "Otherwise a growing inventory balance can hide worsening conversion "
                    "economics, while a liquidation year can temporarily make marketing "
                    "efficiency appear better than it really is."
                ),
                (
                    "Define scrub events before launching acquisition campaigns: inaccessible "
                    "parcels, defective ownership chains, unbuildable setbacks, failed utility "
                    "economics, adverse environmental findings, and buyers unable to close. "
                    "For each event, distinguish refundable deposits, recoverable inventory "
                    "value, sunk contractor work, and additional legal obligations. The "
                    "stress table adds one loss beyond the existing annual allowance equal "
                    "to half a typical upfront deployment: $6,800 Conservative, $10,200 "
                    "Base, or $13,500 Scaled. This deliberately changes profit rather than "
                    "merely moving money between bank accounts. Maintain a reserve register "
                    "with parcel identifier, exposure category, estimated loss range, "
                    "responsible operator, and next evidence date. Update estimates when "
                    "title findings or field inspections change the facts. Do not apply "
                    "a generic refund percentage borrowed from ecommerce to land sales. "
                    "Recorded conveyances, escrow deposits, contractual remedies, and "
                    "post-closing claims have different mechanics. CERCLA liability under "
                    "42 U.S.C. 9607 can also overwhelm a small acquisition discount; "
                    "environmental inquiry and applicable defenses require their own "
                    "fact-specific assessment. A routine $510 Base allowance cannot absorb "
                    "an industrial remediation project. Decline exposures whose plausible "
                    "downside exceeds the business's capacity rather than pretending "
                    "diversification makes every parcel acceptable."
                ),
                (
                    "Apply a combined downside before increasing throughput: a 10% price "
                    "decline, 10% purchase-basis increase, and thirty additional holding "
                    "days produce approximately negative $7,467 Conservative profit, "
                    "$29,183 Base profit, and $153,500 Scaled profit. The timing component "
                    "scales the existing carrying-plus-financing budgets by thirty divided "
                    "by 180; it does not assume new financing is automatically available. "
                    "These results show why the Conservative case has little room for "
                    "optimistic access, survey, or resale assumptions. Require an executable "
                    "exit, bounded technical scope, insurable ownership position, and "
                    "funded cash trough before making an acquisition nonrefundable. When "
                    "representing another owner rather than selling owned inventory, review "
                    "the jurisdiction's broker licensing rules; California Business and "
                    "Professions Code 10131 identifies covered brokerage activities, with "
                    "exceptions requiring separate analysis. Keep the operator's principal "
                    "trading ledger distinct from any licensed representation business. "
                    "After each ten completed dispositions, compare actual cost categories "
                    "and release days with underwriting, investigate the largest misses, "
                    "and update offer ceilings. Automation should accelerate parcel "
                    "screening and comparable-sale tracking, not convert missing evidence "
                    "into favorable assumptions. Expand only when realized unit contribution "
                    "and cash recycling both support the next acquisition cohort."
                ),
            ],
            "table": {
                "caption": "One-Driver and Combined Stress Tests: Annual Owner Profit After Explicit Cost Behavior",
                "headers": [
                    "Stress assumption and fixed operating boundary",
                    "Conservative resulting annual owner profit",
                    "Base resulting annual owner profit",
                    "Scaled resulting annual owner profit",
                ],
                "rows": [
                    [
                        "Resale prices decline 10%; disposition percentages remain unchanged",
                        "$5,200 remains after $18,800 net profit erosion",
                        "$77,350 remains after $79,900 net profit erosion",
                        "$232,500 remains after $142,500 net profit erosion",
                    ],
                    [
                        "Purchase basis rises 10%; all other budgets remain unchanged",
                        "$13,000 remains after $11,000 additional acquisition basis",
                        "$114,750 remains after $42,500 additional acquisition basis",
                        "$306,000 remains after $69,000 additional acquisition basis",
                    ],
                    [
                        "Seller acquisition CAC doubles without increasing closed sales",
                        "$16,000 remains after $8,000 additional marketing expense",
                        "$131,750 remains after $25,500 additional marketing expense",
                        "$345,000 remains after $30,000 additional marketing expense",
                    ],
                    [
                        "Every parcel carries thirty days beyond modeled 180 days",
                        "Approximately $22,333 remains after $1,667 additional time costs",
                        "Approximately $151,583 remains after $5,667 additional time costs",
                        "$365,000 remains after $10,000 additional time costs",
                    ],
                    [
                        "One exceptional loss exceeds the already deducted reserve",
                        "$17,200 remains after $6,800 additional realized loss",
                        "$147,050 remains after $10,200 additional realized loss",
                        "$361,500 remains after $13,500 additional realized loss",
                    ],
                    [
                        "Combine lower prices, higher basis, and thirty-day holding extension",
                        "Approximately negative $7,467 results from the combined downside",
                        "Approximately $29,183 remains after the combined downside assumptions",
                        "$153,500 remains after applying the combined downside assumptions",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four Verifications Before Capital Becomes Nonrefundable",
                "body": (
                    "Document each condition at the parcel level and stop the acquisition "
                    "when evidence contradicts the funded underwriting case."
                ),
                "items": [
                    "Verify the conveyed ownership interest, recorded access rights, title exceptions, and counsel-reviewed co-owner protections where fractional interests are involved.",
                    "Verify the resale thesis with closed comparables, zoning requirements, utility evidence, and subdivision costs that match the actual intended use.",
                    "Verify that all contractor quotes, selling deductions, CAC allocations, time costs, and loss allowances reconcile to the required owner-profit hurdle.",
                    "Verify sufficient drawable capital under delayed receipts, preserving overhead and loss buffers without spending restricted buyer deposits.",
                ],
            },
        },
    ],
    "pull_quote": "A parcel spread becomes owner profit only after every deduction is funded and the sale proceeds are spendable.",
    "diagram_id": "diag-03",
    "action_checklist": [
        "Create a parcel-coded waterfall that reconciles gross sale proceeds, acquisition basis, every operating deduction, and the exact canonical scenario endpoints.",
        "Document closed-sale comparables, legal access, title treatment, zoning, utility feasibility, and the supported exit for every acquisition.",
        "Separate fractional-interest revenue from whole-property value and budget consensual exit or counsel-supervised proceedings with explicit spending limits.",
        "Calculate inventory days, escrow release days, average funded parcel exposure, three months of overhead, and an independently tracked loss buffer.",
        "Run price, purchase-basis, CAC, thirty-day delay, exceptional-loss, and combined downside tests before increasing annual throughput.",
        "Refresh the thirteen-week cash forecast weekly and stop discretionary purchases or distributions when delayed receipts breach protected liquidity.",
    ],
    "statutory_citations": [
        {
            "title": "26 U.S.C. 1221(a)(1) — Property excluded from the capital-asset definition",
            "url": "https://www.law.cornell.edu/uscode/text/26/1221",
            "relevance": (
                "Property held primarily for sale to customers in the ordinary course "
                "of business is excluded from capital-asset treatment; repeated flipping "
                "requires classification based on the operator's actual facts."
            ),
        },
        {
            "title": "California Code of Civil Procedure 874.316 — Cotenant buyout procedures",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CCP&sectionNum=874.316.",
            "relevance": (
                "For proceedings within the applicable statutory framework, cotenant "
                "buyout procedures affect fractional-interest exit timing, valuation, "
                "notices, and liquidity assumptions."
            ),
        },
        {
            "title": "California Code of Civil Procedure 874.317 — Partition alternatives",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CCP&sectionNum=874.317.",
            "relevance": (
                "The statutory treatment of partition in kind and partition by sale "
                "prevents underwriting a purchased fractional interest as an automatic "
                "right to immediate whole-property liquidation."
            ),
        },
        {
            "title": "California Government Code 66424 — Subdivision definition",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=GOV&sectionNum=66424.",
            "relevance": (
                "The statutory subdivision definition informs whether proposed parcel "
                "creation enters the subdivision framework; local requirements determine "
                "the project's engineering, review, and timing budget."
            ),
        },
        {
            "title": "40 CFR Part 312 — Standards and Practices for All Appropriate Inquiries",
            "url": "https://www.ecfr.gov/current/title-40/chapter-I/subchapter-J/part-312",
            "relevance": (
                "Environmental inquiry standards can affect diligence scope and timing "
                "for purchasers seeking applicable CERCLA landowner liability protections."
            ),
        },
        {
            "title": "42 U.S.C. 9607 — CERCLA liability and related defenses",
            "url": "https://www.law.cornell.edu/uscode/text/42/9607",
            "relevance": (
                "Potential environmental liability can dwarf parcel acquisition cost; "
                "underwriting must evaluate site history, investigation results, and "
                "the conditions of any claimed protection."
            ),
        },
        {
            "title": "California Business and Professions Code 10131 — Real estate broker activities",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=BPC&sectionNum=10131.",
            "relevance": (
                "Activities performed for others for compensation can fall within "
                "broker licensing rules; distinguish principal-owned parcel sales from "
                "representation services and evaluate applicable exceptions separately."
            ),
        },
    ],
}
