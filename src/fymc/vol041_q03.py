from __future__ import annotations

CHAPTER_3 = {
    "id": "Q3",
    "chapter_id": "Q3",
    "chapter_number": 3,
    "question_number": 3,
    "slug": "unit-economics-margin-waterfall-working-capital-float",
    "question_prompt": "What are the real unit economics, gross-to-net margin deductions, scrub/reversal reserves, and working-capital float requirements for buying group, card-float & ticket allocation arbitrage?",
    "kicker": "Q3 / THE BIG MONEY PLAYBOOKS",
    "title": "Unit Economics, Margin Waterfall & Working-Capital Float",
    "subtitle": "Purchase-Order Spreads, VCC Rebate Scrubs, Ticket Payout Locks, ASC 606 Presentation, and Statement-Date Liquidity",
    "layout_template": "financial_breakdown",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #41, Rank #09 of 42, scores 93/100 across 11 mapped plays, but its economics depend on collecting spread before settlement obligations become cash demands. "
        "The canonical Conservative, Base, and Scaled cases produce $20,000, $143,500, and $360,000 annual owner profit from $250,000, $1,025,000, and $1,800,000 gross throughput. "
        "A 35% retained share converts those amounts into $87,500, $358,750, and $630,000 retained revenue. "
        "This chapter reconciles the complete waterfall, separates inventory principal from VCC commission revenue, and prices contractor labor, acquisition, reversals, and financing. "
        "It also translates buying-group ACH delays, event payout locks, and issuer interruptions into dated liquidity requirements. "
        "The operating rule is simple: neither an advertised rebate nor an unsold ticket pays a card statement."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$250,000",
            "context": "Annual gross throughput; $87,500 retained revenue at 35%.",
            "note": "8% gross-basis margin; $20,000 annual owner profit; 22.86% retained margin; 1 FT + 2 C.",
        },
        {
            "label": "Base",
            "value": "$1,025,000",
            "context": "Annual gross throughput; $358,750 retained revenue at 35%.",
            "note": "14.0% gross-basis margin; $143,500 annual owner profit; 40.0% retained margin; 1 FT + 2 C.",
        },
        {
            "label": "Scaled",
            "value": "$1,800,000",
            "context": "Annual gross throughput; $630,000 retained revenue at 35%.",
            "note": "20% gross-basis margin; $360,000 annual owner profit; 57.14% retained margin; 2 FT + 3 C.",
        },
    ],
    "sections": [
        {
            "heading": "1. Reconcile gross throughput to retained spread before underwriting a purchase",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Start with three ledgers rather than one sales dashboard: transaction principal, earned spread, and unrestricted cash. "
                    "The canonical scorecard labels $250,000, $1,025,000, and $1,800,000 as gross revenue, covering buying-group reimbursements, earned card rebates, and ticket resale proceeds. "
                    "For this chapter, call that measure gross throughput so nobody mistakes pass-through merchandise basis for spendable earnings. "
                    "Apply the supplied 35% retained share once: retained revenue becomes $87,500, $358,750, and $630,000, while merchandise and face-value ticket basis becomes $162,500, $666,250, and $1,170,000. "
                    "Owner profit divided by retained revenue produces 22.86%, 40.0%, and 57.14%; dividing by gross throughput produces the canonical 8%, 14.0%, and 20%. "
                    "These are different denominators, not competing forecasts. "
                    "ASC 606 principal-versus-agent presentation depends on control before transfer, not a universal percentage election. "
                    "Use 35% as the supplied economic retention convention; determine statutory reporting presentation contract by contract with the accounting team. "
                    "A principal seller may report gross sales and cost of sales, while an agent may report its commission. "
                    "Do not force both arrangements into identical journal entries merely because the management scorecard combines their economics. "
                    "Keep customer invoice principal out of VCC commission revenue altogether, and retain a reconciliation from each settlement report to the management measure."
                ),
                (
                    "Build the Base case from 205 illustrative completed cohorts averaging $5,000 gross throughput each. "
                    "A cohort is a settled purchase-order batch or ticket allocation batch, not necessarily one customer or one seat. "
                    "Its $3,250 landed basis leaves $1,750 retained spread. "
                    "Deduct $150 acquisition, $300 contractor delivery, $292.68 allocated fixed overhead, $150 transaction and fulfillment expense, $100 expected scrub and reversal loss, and $57.32 funding expense. "
                    "The resulting $700 owner contribution multiplied by 205 produces $143,500. "
                    "Annual amounts control rounding: overhead is exactly $60,000 and funding exactly $11,750. "
                    "For Conservative, use 50 cohorts at $5,000, producing $1,750 retained spread and $400 owner contribution per cohort. "
                    "For Scaled, use 300 cohorts at $6,000, producing $2,100 retained spread and $1,200 owner contribution. "
                    "These cohort constructions reconcile the supplied outcomes; they are allocation assumptions rather than observed conversion rates. "
                    "Attach every cohort to its purchase authorization, seller invoice, shipping acceptance, marketplace settlement, and issuer statement. "
                    "The canonical 11 mapped plays belong in one consolidated ledger, but each needs its own principal, fee, and cash-timing fields. "
                    "A purchase that appears profitable only after assigning another cohort's rebate is a rejected purchase, not a diversification benefit."
                ),
                (
                    "Do not present the portfolio's 35% retention as the typical spread on a committed wholesale electronics order. "
                    "A buying-group purchase costing $10,000 and reimbursing $10,150 produces only $150 merchandise spread. "
                    "An eligible 2% earned purchase rebate adds $200, making gross throughput $10,350 and retained spread $350 before shipping, labor, funding, and reversals. "
                    "After $60 insured shipping, $45 contractor handling, $30 acquisition allocation, $40 expected loss, and $25 funding expense, that order contributes $150 before fixed overhead. "
                    "Its realized retention is approximately 3.38%, far below the canonical blended assumption. "
                    "Reaching 35% therefore requires a materially richer verified mix of ticket spreads, allocation commissions, or service fees; it cannot be created by relabeling reimbursements. "
                    "A $1,000 face-value ticket resold for $1,400 retains $400 before a hypothetical 12% marketplace fee of $168 and $35 delivery labor, leaving $197 before acquisition, reserves, funding, and overhead. "
                    "The marketplace percentage must come from the actual seller agreement. "
                    "SkyBox or Automatiq can synchronize inventory and prices, but neither converts an asking price into collected proceeds. "
                    "Reject the aggregate underwriting if signed economics do not support the blended retention, and rebuild the forecast from the real channel mix before committing capital."
                ),
            ],
            "table": {
                "caption": "Canonical Formula v2.0 Annual Gross-to-Net Reconciliation",
                "headers": [
                    "Economic line and measurement discipline",
                    "Conservative annual case and operating interpretation",
                    "Base annual case and operating interpretation",
                    "Scaled annual case and operating interpretation",
                ],
                "rows": [
                    [
                        "Gross throughput before removing merchandise and ticket basis",
                        "$250,000 combining reimbursements, earned rebates, and resale proceeds",
                        "$1,025,000 combining reimbursements, earned rebates, and resale proceeds",
                        "$1,800,000 combining reimbursements, earned rebates, and resale proceeds",
                    ],
                    [
                        "Landed merchandise and face-value basis equals sixty-five percent",
                        "$162,500 removed before calculating retained operating revenue",
                        "$666,250 removed before calculating retained operating revenue",
                        "$1,170,000 removed before calculating retained operating revenue",
                    ],
                    [
                        "Retained revenue equals the supplied thirty-five percent share",
                        "$87,500 retained before contractor, acquisition, and operating deductions",
                        "$358,750 retained before contractor, acquisition, and operating deductions",
                        "$630,000 retained before contractor, acquisition, and operating deductions",
                    ],
                    [
                        "Fixed overhead allocated once across completed transaction cohorts",
                        "$18,000 annually, equivalent to $1,500 monthly fixed overhead",
                        "$60,000 annually, equivalent to $5,000 monthly fixed overhead",
                        "$84,000 annually, equivalent to $7,000 monthly fixed overhead",
                    ],
                    [
                        "Variable deductions include acquisition, contractors, fees, losses, funding",
                        "$49,500 combined variable deductions beyond the landed basis",
                        "$155,250 combined variable deductions beyond the landed basis",
                        "$186,000 combined variable deductions beyond the landed basis",
                    ],
                    [
                        "Annual owner profit after all modeled operating deductions",
                        "$20,000 owner profit, representing eight percent gross-basis margin",
                        "$143,500 owner profit, representing fourteen percent gross-basis margin",
                        "$360,000 owner profit, representing twenty percent gross-basis margin",
                    ],
                    [
                        "Retained margin and team configuration use separate denominators",
                        "22.86% retained margin with one full-time operator, two contractors",
                        "40.0% retained margin with one full-time operator, two contractors",
                        "57.14% retained margin with two full-time operators, three contractors",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Protect the spread that survives settlement",
                "body": "Price the completed cash cycle, not the advertised purchase discount or speculative resale listing.",
                "items": [
                    "Export issuer rebate adjustments by original transaction identifier; charge a clawback to its originating cohort rather than hiding it in the current month's purchases.",
                    "Negotiate buying-group acceptance timestamps and rejection windows in writing; a Net-3 promise without a defined acceptance event cannot support a reliable cash forecast.",
                    "Record marketplace fees separately from ticket face value; compare actual net settlements against SkyBox or Automatiq exports before increasing allocation size.",
                    "Model card shutdown with zero new charging capacity and zero unposted rebates; keep the cash needed for already-posted statements outside inventory purchasing balances.",
                ],
            },
        },
        {
            "heading": "2. Price contractor delivery, acquisition, and the VCC rebate waterfall",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Treat contractor delivery as a measured production input, not miscellaneous overhead that disappears when volume scales. "
                    "The Conservative allocation is 12 hours per cohort at $30, or $360; Base and Scaled use ten hours at $30, or $300. "
                    "Annual contractor budgets are consequently $18,000, $61,500, and $90,000, covering 600, 2,050, and 3,000 hours. "
                    "Divide those hours across two, two, and three contractors, respectively, and reserve operator attention for underwriting exceptions, reconciliation, and counterparty collections. "
                    "The team labels describe staffing structure, not five full-time salaries at scale. "
                    "Fixed overhead includes systems, bookkeeping, insurance, and any employed support compensation within the stated envelope; owner compensation comes from owner profit. "
                    "If actual payroll cannot fit, the canonical case needs revision rather than an invisible labor subsidy. "
                    "Allocate $150 acquisition cost to each completed cohort: $7,500, $30,750, and $45,000 annually. "
                    "This is acquisition expense per completion, not necessarily customer CAC. "
                    "Calculate customer CAC separately as acquisition spending divided by newly activated counterparties, then track repeat cohorts to avoid charging each repeat transaction a fictional new-customer cost. "
                    "Charge failed outreach, canceled commitments, and unsuccessful onboarding to acquisition expense even when no shipment or ticket transfer occurs. "
                    "That denominator discipline prevents a polished sales dashboard from overstating repeatable contribution."
                ),
                (
                    "The mapped play b2b_commercial_vcc_interchange_rebate_arbitrage embeds automated AP and vendor settlement into freight brokerage, construction, medical supply, property management, or media-agency workflows. "
                    "Its economic principal is third-party invoice volume, not operator sales. "
                    "For $100,000 of eligible settled supplier payments, a contractually retained 160-basis-point rebate produces $1,600 revenue. "
                    "Deduct illustrative provider expense of $250, servicing labor of $180, acquisition allocation of $120, reversal provision of $150, and funding expense of $100; contribution becomes $800 before fixed overhead. "
                    "Confirm whether the quoted yield is already net of provider charges before deducting them again. "
                    "The specified 140–195 basis-point range implies $1.4 million–$1.95 million on $100 million eligible annual payments, but that separate scale illustration is not added to this volume's canonical scenarios. "
                    "No operator receives the entire merchant interchange merely by issuing a virtual card. "
                    "A sponsor, issuer, processor, or program agreement determines eligibility, revenue sharing, adjustments, and payment timing. "
                    "Create single-use Visa or Mastercard commercial VCCs only for authorized invoices and approved suppliers. "
                    "Transmit authentic Level-3 line-item invoice metadata at creation where supported; metadata does not compel vendor acceptance or ensure a particular rebate. "
                    "Measure accepted, settled, rebate-eligible volume instead of displaying all uploaded AP invoices as monetized throughput."
                ),
                (
                    "For card-averse vendors, offer dynamic early-pay ACH discounts only through an agreed settlement arrangement. "
                    "On a $100,000 invoice, a 1.5%–2% discount for payment on day ten instead of day thirty saves the buyer $1,500–$2,000. "
                    "A separately contracted 20% share of that saving yields $300–$400 operator revenue; the remaining saving belongs to the buyer. "
                    "If the operator advances the full principal for twenty days at 12% annual funding cost, interest alone is approximately $657.53, exceeding that fee. "
                    "The fallback therefore needs buyer-funded settlement, a separately priced funding facility, or a smaller advance exposure. "
                    "Do not count the same discount simultaneously as buyer savings, merchant rebate, and operator revenue. "
                    "Focus VCC acquisition on fragmented long-tail vendors that explicitly accept the payment method, then retain ACH for suppliers whose acceptance economics fail. "
                    "Keep these AP settlement rebates separate from the purchasing business's advertised 2%–4% commercial card rewards. "
                    "A reward is usable in underwriting only after checking caps, category exclusions, returned-purchase treatment, fees, and contractual business-use restrictions. "
                    "For an illustrative $10,000 eligible purchase, 2% yields $200 and 4% yields $400; losing one percentage point removes $100. "
                    "Never manufacture transactions or misclassify invoices to restore that difference. "
                    "Use a lower purchase price, a lower service cost, or decline the transaction."
                ),
            ],
            "table": {
                "caption": "Annual Expense Allocations That Exactly Reconcile Owner Profit",
                "headers": [
                    "Expense line and allocation boundary",
                    "Conservative expense and measurable operating driver",
                    "Base expense and measurable operating driver",
                    "Scaled expense and measurable operating driver",
                ],
                "rows": [
                    [
                        "Acquisition expense allocated across completed purchase or allocation cohorts",
                        "$7,500 equals fifty completed cohorts at $150 each",
                        "$30,750 equals 205 completed cohorts at $150 each",
                        "$45,000 equals 300 completed cohorts at $150 each",
                    ],
                    [
                        "Contractor delivery labor measured through logged productive hours",
                        "$18,000 equals 600 delivery hours at $30 hourly",
                        "$61,500 equals 2,050 delivery hours at $30 hourly",
                        "$90,000 equals 3,000 delivery hours at $30 hourly",
                    ],
                    [
                        "Fixed overhead includes systems, administration, and budgeted support",
                        "$18,000 annual allocation requires $1,500 monthly cash coverage",
                        "$60,000 annual allocation requires $5,000 monthly cash coverage",
                        "$84,000 annual allocation requires $7,000 monthly cash coverage",
                    ],
                    [
                        "Transaction and fulfillment expense excludes already counted inventory basis",
                        "$10,000 covers payment fees, shipping, and fulfillment exceptions",
                        "$30,750 covers payment fees, shipping, and fulfillment exceptions",
                        "$27,000 covers payment fees, shipping, and fulfillment exceptions",
                    ],
                    [
                        "Expected scrub and reversal losses reduce current cohort contribution",
                        "$10,000 provision equals four percent of gross throughput",
                        "$20,500 provision equals two percent of gross throughput",
                        "$18,000 provision equals one percent of gross throughput",
                    ],
                    [
                        "Funding expense includes contracted interest and facility carrying charges",
                        "$4,000 annual funding budget requires dated borrowing reconciliation",
                        "$11,750 annual funding budget requires dated borrowing reconciliation",
                        "$6,000 annual funding budget requires dated borrowing reconciliation",
                    ],
                    [
                        "Total deductions bridge retained revenue to annual owner profit",
                        "$67,500 deducted from $87,500 leaves $20,000 owner profit",
                        "$215,250 deducted from $358,750 leaves $143,500 owner profit",
                        "$270,000 deducted from $630,000 leaves $360,000 owner profit",
                    ],
                ],
            },
        },
        {
            "heading": "3. Convert settlement promises into a dated working-capital requirement",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Build the float model from actual purchase dates, statement closing dates, due dates, and unrestricted settlement dates. "
                    "The named 60-day card-statement float ledger is a tracking horizon, not a promise of sixty interest-free days on every charge. "
                    "A purchase shortly before statement closing receives less runway than one shortly afterward, and revolving balances can change grace-period economics. "
                    "For an explicit blended illustration, assume purchase-to-cash cycles of 48, 42, and 36 days against thirty days of payment runway. "
                    "These cycles include shipping, acceptance, receivable collection, event waiting periods, and payout locks; they are broader than invoice DSO alone. "
                    "The uncovered gaps are eighteen, twelve, and six days. "
                    "Multiply each gap by annual landed basis divided by 365, producing approximately $8,014, $21,904, and $19,233 of average inventory-basis funding need. "
                    "This proxy excludes fee timing and acquisition outflows, which the daily cash calendar must add. "
                    "It also assumes evenly distributed purchases, making it unsuitable as the sole authorization limit for event-heavy inventory. "
                    "A concentrated ticket allocation can consume months of average purchases in one afternoon. "
                    "Record every known statement payment and event payout individually, then calculate the maximum cumulative cash deficit rather than relying exclusively on annual turnover ratios."
                ),
                (
                    "Add explicit liquidity layers without pretending that every layer is another expense. "
                    "For Conservative, Base, and Scaled, hold illustrative reversal cash buffers of $4,000, $12,000, and $18,000, plus one month of fixed overhead at $1,500, $5,000, and $7,000. "
                    "Add incremental peak-batch cushions of $10,000, $20,000, and $30,000 only for concentration exceeding the average funding proxy. "
                    "The resulting planning liquidity is $23,514, $58,904, and $74,233. "
                    "The stated $10,000–$55,000 startup range therefore does not automatically fund every modeled operating state: Base exceeds its upper end by $3,904 and Scaled by $19,233. "
                    "Retained earnings or a committed external facility must bridge those differences before purchases increase. "
                    "Cash held against reversals is a balance-sheet liquidity allocation; expected losses are already included in the earnings waterfall. "
                    "Do not subtract the buffer again when calculating profit. "
                    "Likewise, drawing a credit facility creates cash and debt, not revenue, and repaying principal is distinct from interest expense. "
                    "An unused card limit is not unrestricted cash available to satisfy another card statement. "
                    "Validate borrowing permissions, advance availability, and settlement restrictions before counting any facility as a source of working capital. "
                    "Remove uncommitted financing immediately from the downside cash forecast."
                ),
                (
                    "Separate buying-group DSO from ticket payout locks because their failure modes require different interventions. "
                    "A vetted Net-3 or Net-5 buying group should have a documented trigger, such as warehouse acceptance, followed by an expected ACH initiation and bank-availability date. "
                    "Weekends, disputed serial numbers, rejected packaging, and shipment loss can extend the purchase-to-cash cycle beyond the invoice term. "
                    "Insure high-value shipments with the correct declared value and preserve carrier acceptance evidence, while checking exclusions and claim-payment timing. "
                    "Ticket marketplaces may hold proceeds until after the event or longer during disputes; selling inventory today does not necessarily release cash today. "
                    "SSL rights, corporate suites, and allocation brokerage additionally require documented transfer rights, included amenities, and counterparty payment conditions. "
                    "Do not treat a revocable allocation email as transferable inventory. "
                    "Set markdown checkpoints against event dates, using a pre-agreed contribution floor and cash-release objective rather than waiting for face-value recovery. "
                    "If a card issuer starts a review, stop new commitments that depend on that line, continue reconciling existing obligations, and preserve statement-payment cash. "
                    "If a buying-group ACH misses its expected availability date, suspend incremental exposure to that counterparty and move only uncommitted orders to another vetted group. "
                    "Diversification works before default exposure accumulates, not after."
                ),
            ],
            "table": {
                "caption": "Illustrative Float and Liquidity Bridge Using Landed Basis",
                "headers": [
                    "Timing or liquidity component and calculation rule",
                    "Conservative cash-cycle assumption and resulting requirement",
                    "Base cash-cycle assumption and resulting requirement",
                    "Scaled cash-cycle assumption and resulting requirement",
                ],
                "rows": [
                    [
                        "Purchase-to-unrestricted-cash cycle includes receivable and event settlement delays",
                        "48 days from purchase until unrestricted cash becomes available",
                        "42 days from purchase until unrestricted cash becomes available",
                        "36 days from purchase until unrestricted cash becomes available",
                    ],
                    [
                        "Illustrative payment runway must be replaced with statement dates",
                        "Thirty days assumed before the purchase obligation requires payment",
                        "Thirty days assumed before the purchase obligation requires payment",
                        "Thirty days assumed before the purchase obligation requires payment",
                    ],
                    [
                        "Uncovered funding gap equals cash cycle minus payment runway",
                        "Eighteen uncovered days require funding beyond assumed card runway",
                        "Twelve uncovered days require funding beyond assumed card runway",
                        "Six uncovered days require funding beyond assumed card runway",
                    ],
                    [
                        "Average basis funding equals annual basis times gap divided by 365",
                        "$8,014 rounded funding need against $162,500 annual landed basis",
                        "$21,904 rounded funding need against $666,250 annual landed basis",
                        "$19,233 rounded funding need against $1,170,000 annual landed basis",
                    ],
                    [
                        "Reversal cash buffer plus one month of fixed overhead",
                        "$5,500 combines $4,000 reversal cash and $1,500 fixed overhead",
                        "$17,000 combines $12,000 reversal cash and $5,000 fixed overhead",
                        "$25,000 combines $18,000 reversal cash and $7,000 fixed overhead",
                    ],
                    [
                        "Incremental peak-batch cushion covers concentration beyond average basis funding",
                        "$10,000 additional liquidity reserved for concentrated purchase commitments",
                        "$20,000 additional liquidity reserved for concentrated purchase commitments",
                        "$30,000 additional liquidity reserved for concentrated purchase commitments",
                    ],
                    [
                        "Total planning liquidity excludes uncommitted financing and unrealized rebates",
                        "$23,514 total planning liquidity before additional calendar-specific cash demands",
                        "$58,904 total planning liquidity before additional calendar-specific cash demands",
                        "$74,233 total planning liquidity before additional calendar-specific cash demands",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Create the dated obligation register",
                    "action": "Link every cohort to purchase, acceptance, statement, event, and payout dates.",
                    "detail": "Use issuer exports and actual marketplace settlement terms; distinguish invoice DSO from the complete purchase-to-cash cycle.",
                },
                {
                    "step": 2,
                    "title": "Calculate the daily cash deficit",
                    "action": "Project each cash inflow and outflow over the next sixty days.",
                    "detail": "Include already committed purchases, contractor payments, refunds, fixed overhead, facility interest, and statement principal without counting debt draws as revenue.",
                },
                {
                    "step": 3,
                    "title": "Apply collection and issuer interruptions",
                    "action": "Delay buying-group collections fifteen days and remove new card availability.",
                    "detail": "Keep existing statement obligations unchanged; exclude unposted rebates and any facility whose availability is not contractually committed.",
                },
                {
                    "step": 4,
                    "title": "Set purchase limits from available liquidity",
                    "action": "Authorize only commitments that preserve statement-payment cash under the downside calendar.",
                    "detail": "Escalate counterparty delays, reduce ticket positions, or secure documented funding before increasing exposure; retain the reviewed forecast with the purchase decision.",
                },
            ],
        },
        {
            "heading": "4. Stress the spread, reserve reversals, and enforce executable fallbacks",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Maintain separate reserve schedules for merchandise rejection, card-rebate scrub, ticket cancellation, delivery disputes, and counterparty nonpayment. "
                    "A scrub is the removal of an expected rebate or payable spread after eligibility review; a reversal returns a previously booked amount or unwinds a settlement. "
                    "Book only contractually supportable earned rebates, age unsettled balances, and true up estimates against issuer reports. "
                    "The annual expected-loss allocations are $10,000, $20,500, and $18,000, equivalent to 4%, 2%, and 1% of canonical gross throughput. "
                    "Their decline with scale is an underwriting assumption requiring evidence from acceptance quality, vendor diversification, and resolved claims, not an automatic benefit of becoming larger. "
                    "For tickets, evaluate cancellation refunds alongside recoverable purchase basis rather than assuming every gross refund is an equal net loss. "
                    "For insured shipments, recognize that a potential insurance recovery can arrive after the card statement and can be disputed. "
                    "Track gross exposure, expected recovery, expected net loss, and expected payment date independently. "
                    "Use realized cohort vintages to revise the provision, preserving a record of original estimates and subsequent adjustments. "
                    "A reserve release belongs to the period and cohort supported by evidence; it should never become a convenient plug used to meet a target margin."
                ),
                (
                    "Run sensitivities against the same canonical baseline rather than changing the denominator halfway through the stress test. "
                    "An additional two percentage points of net loss on gross throughput removes $5,000, $20,500, and $36,000, leaving owner profit of $15,000, $123,000, and $324,000. "
                    "A 20% contractor-cost increase removes $3,600, $12,300, and $18,000. "
                    "Together those two shocks leave $11,400, $110,700, and $306,000. "
                    "Separately, assume tickets represent 20% of gross throughput and realized ticket prices fall 2%, with basis and other costs held constant. "
                    "That removes $1,000, $4,100, and $7,200; actual fee reductions could soften the impact, but this test gives no credit for them. "
                    "A fifteen-day collection delay increases the average basis funding proxy by approximately $6,678, $27,380, and $48,082 without directly changing accounting profit. "
                    "Additional financing interest would reduce profit according to the actual facility balance and duration. "
                    "These shocks are independent illustrations unless expressly combined. "
                    "Do not add a full ticket cancellation loss to a price-decay stress on the same seat without defining mutually exclusive outcomes. "
                    "Similarly, losing a rebate already excluded from the baseline is not a second incremental expense. "
                    "Stress testing should expose cash fragility, not inflate losses through duplicate counting."
                ),
                (
                    "Turn each modeled downside into a purchase rule that can be executed by the small team. "
                    "The BOTS Act, 15 U.S.C. §45c, prohibits specified circumvention of online ticket controls and certain sales of tickets obtained through that conduct. "
                    "Use no queue or CAPTCHA bypass software, and preserve acquisition records supporting lawful sourcing. "
                    "For covered ticket offers, 16 CFR Part 464 governs total-price disclosure and specified fee representations; map seller listings and marketplace presentations to the applicable requirements. "
                    "New York Arts and Cultural Affairs Law §25.07 adds jurisdiction-specific ticket pricing requirements, while state resale-certificate rules govern qualifying inventory purchases. "
                    "California Revenue and Taxation Code §6091 places the burden of establishing a sale for resale on the seller unless the prescribed certificate conditions are met. "
                    "Collect tax separately from earned spread and reconcile marketplace collection responsibilities before comparing channel margins. "
                    "For SSL and suite allocations, verify the actual license or venue contract permits the intended transfer and resale. "
                    "Decline unsupported rights rather than assigning them optimistic liquidation value. "
                    "The final release decision combines positive stressed contribution, documented transferability, available settlement liquidity, and a named fallback buyer or markdown schedule. "
                    "If one fails, reduce the position, renegotiate the purchase basis, or leave the allocation with its current holder."
                ),
            ],
            "table": {
                "caption": "Independent Sensitivity Tests and One Explicit Combined Downside",
                "headers": [
                    "Stress definition and denominator held constant",
                    "Conservative change and resulting operating interpretation",
                    "Base change and resulting operating interpretation",
                    "Scaled change and resulting operating interpretation",
                ],
                "rows": [
                    [
                        "Baseline owner profit before applying any incremental stress",
                        "$20,000 annual owner profit under the canonical operating assumptions",
                        "$143,500 annual owner profit under the canonical operating assumptions",
                        "$360,000 annual owner profit under the canonical operating assumptions",
                    ],
                    [
                        "Additional net loss equals two percent of gross throughput",
                        "$5,000 additional loss leaves $15,000 annual owner profit",
                        "$20,500 additional loss leaves $123,000 annual owner profit",
                        "$36,000 additional loss leaves $324,000 annual owner profit",
                    ],
                    [
                        "Contractor delivery expense increases twenty percent without throughput growth",
                        "$3,600 additional labor expense leaves $16,400 owner profit",
                        "$12,300 additional labor expense leaves $131,200 owner profit",
                        "$18,000 additional labor expense leaves $342,000 owner profit",
                    ],
                    [
                        "Combine only the incremental loss and contractor expense shocks",
                        "$8,600 combined expense increase leaves $11,400 owner profit",
                        "$32,800 combined expense increase leaves $110,700 owner profit",
                        "$54,000 combined expense increase leaves $306,000 owner profit",
                    ],
                    [
                        "Ticket prices decline two percent on twenty-percent ticket mix",
                        "$1,000 proceeds reduction leaves $19,000 annual owner profit",
                        "$4,100 proceeds reduction leaves $139,400 annual owner profit",
                        "$7,200 proceeds reduction leaves $352,800 annual owner profit",
                    ],
                    [
                        "Collection cycle extends fifteen days against unchanged payment dates",
                        "$6,678 additional basis funding required before incremental financing interest",
                        "$27,380 additional basis funding required before incremental financing interest",
                        "$48,082 additional basis funding required before incremental financing interest",
                    ],
                    [
                        "Purchase rebate falls fifty basis points on fully eligible basis",
                        "$812.50 lost rebate leaves $19,187.50 annual owner profit",
                        "$3,331.25 lost rebate leaves $140,168.75 annual owner profit",
                        "$5,850 lost rebate leaves $354,150 annual owner profit",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four checks before releasing purchase capital",
                "body": "A positive headline spread is insufficient when eligibility, ownership, settlement, or downside liquidity remains unresolved.",
                "items": [
                    "Verify signed buying-group acceptance terms, merchandise condition requirements, ACH timing, and insured shipment coverage before relying on the reimbursement.",
                    "Verify issuer reward eligibility and VCC revenue-sharing terms; separate customer invoice principal from operator fees and test zero unposted rebate availability.",
                    "Verify lawful ticket acquisition, transferable SSL or suite rights, seller fee schedules, payout-lock terms, and applicable total-price presentation requirements.",
                    "Verify the daily cash forecast survives a fifteen-day collection delay and no new card capacity while preserving cash for already-posted statement obligations.",
                ],
            },
        },
    ],
    "pull_quote": "A spread becomes owner profit only after basis, reversals, labor, and the cash calendar have all been paid.",
    "diagram_id": "diag-03",
    "action_checklist": [
        "Reconcile each cohort from gross throughput through the 35% retained-share convention to actual channel-level owner contribution.",
        "Separate VCC invoice principal, earned program rebates, buyer discount savings, and operator service fees into distinct ledger accounts.",
        "Replace illustrative contractor hours, acquisition allocations, and fee percentages with signed rates and completed-cohort evidence.",
        "Build a sixty-day cash calendar using actual statement dates, buying-group acceptance terms, event dates, and unrestricted payout dates.",
        "Fund reversal liquidity and concentrated purchase cushions without deducting those cash allocations twice from owner profit.",
        "Apply the specified downside tests, document lawful sourcing and transfer rights, and set counterparty limits and pre-event markdown instructions.",
    ],
    "statutory_citations": [
        {
            "title": "15 U.S.C. §45c — Unfair and deceptive acts and practices relating to ticket sales",
            "url": "https://www.law.cornell.edu/uscode/text/15/45c",
            "relevance": "Prohibits specified circumvention of ticket purchase controls and covered resale of tickets obtained through that conduct; supports acquisition-record and sourcing controls.",
        },
        {
            "title": "16 CFR Part 464 — Rule on Unfair or Deceptive Fees",
            "url": "https://www.ecfr.gov/current/title-16/chapter-I/subchapter-D/part-464",
            "relevance": "Establishes total-price disclosure and fee-representation requirements for covered live-event ticket offers; affects displayed prices and channel margin comparisons.",
        },
        {
            "title": "New York Arts and Cultural Affairs Law §25.07 — Ticket prices",
            "url": "https://www.nysenate.gov/legislation/laws/ACA/25.07",
            "relevance": "Provides ticket-pricing and disclosure requirements relevant to covered New York transactions; review actual listing and checkout presentations against the statutory scope.",
        },
        {
            "title": "California Revenue and Taxation Code §6091 — Presumption of taxable retail sales and resale certificates",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=6091.",
            "relevance": "Addresses the seller's burden to establish a sale for resale and the role of qualifying resale certificates; supports inventory tax-basis documentation.",
        },
    ],
}
