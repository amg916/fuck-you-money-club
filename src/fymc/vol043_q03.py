from __future__ import annotations

CHAPTER_3 = {
    "id": "Q3",
    "chapter_id": "Q3",
    "chapter_number": 3,
    "question_number": 3,
    "slug": "unit-economics-margin-waterfall-working-capital-float",
    "question_prompt": "What are the real unit economics, gross-to-net margin deductions, scrub/reversal reserves, and working-capital float requirements for live-event, super bowl & vip ticket brokering?",
    "kicker": "Q3 / THE BIG MONEY PLAYBOOKS",
    "title": "Unit Economics, Margin Waterfall & Working-Capital Float",
    "subtitle": "SkyBox Settlement Cohorts, Suite Seat-Splitting, Hospitality Deposits, ASC 606 Presentation, and BOTS Act Operating Boundaries",
    "layout_template": "financial_breakdown",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #43, ranked #02 of 43 with a 95/100 Money-to-Manpower Score, "
        "turns ticket distribution and hospitality assembly into a settlement-management "
        "business. This chapter maps 12 operator plays across exchange resale, suite "
        "seat-splitting, and tentpole corporate hospitality, then separates acquisition "
        "cost, retained spread, operating deductions, and cash availability. Formula v2.0 "
        "fixes annual owner profit at $26,400 Conservative, $191,900 Base, and $468,000 "
        "Scaled. Those outcomes require $220,000, $1,010,000, and $1,800,000 of gross "
        "volume respectively; the modeled 40% retained shares are $88,000, $404,000, "
        "and $720,000. Cohort waterfalls expose exchange fees, inventory impairments, "
        "reversal losses, contractor labor, acquisition CAC, and financing. Explicit "
        "settlement calendars show why an apparently profitable Super Bowl position "
        "can exhaust available liquidity before the exchange releases payment."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$220,000",
            "context": "Annual gross volume; $88,000 modeled retained revenue at 40%.",
            "note": "12% gross-basis net margin; 30% retained margin; $26,400 annual owner net profit; 1 FT + 2 C.",
        },
        {
            "label": "Base",
            "value": "$1,010,000",
            "context": "Annual gross volume; $404,000 modeled retained revenue at 40%.",
            "note": "19.0% gross-basis net margin; 47.5% retained margin; $191,900 annual owner net profit; 1 FT + 2 C.",
        },
        {
            "label": "Scaled",
            "value": "$1,800,000",
            "context": "Annual gross volume; $720,000 modeled retained revenue at 40%.",
            "note": "26% gross-basis net margin; 65% retained margin; $468,000 annual owner net profit; 2 FT + 3 C.",
        },
    ],
    "sections": [
        {
            "heading": "1. Define the revenue denominator before buying the inventory",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Start every cohort with a documented revenue denominator, not the balance "
                    "displayed in an exchange dashboard. Formula v2.0 supplies $220,000, "
                    "$1,010,000, and $1,800,000 of annual gross volume and a 40% retained "
                    "share after ticket or suite acquisition. This chapter normalizes that "
                    "volume to seller-attributable billings before seller fees, excluding "
                    "taxes collected for government and exchange buyer fees never earned by "
                    "the broker. If an exchange statement reports only a net payout, add "
                    "back its separately identified seller fee before using this waterfall; "
                    "never subtract that fee twice. The resulting retained amounts are "
                    "$88,000, $404,000, and $720,000. ASC 606 principal-versus-agent analysis "
                    "still depends on control of the specified ticket or hospitality service "
                    "before transfer. A 40% spreadsheet assumption does not establish agency "
                    "or automatically determine reported revenue. Maintain the scorecard's "
                    "retained-contribution view alongside the actual accounting presentation, "
                    "with a reconciliation for supplier pass-throughs, recognized commissions, "
                    "and customer liabilities. Do not call underlying event attendance spend, "
                    "corporate travel budgets, or stadium hospitality GMV operator revenue. "
                    "Allocate mixed packages to their distinct promised services and document "
                    "when each obligation is satisfied. This prevents advance deposits from "
                    "inflating both revenue and apparent purchasing capacity."
                ),
                (
                    "Separate three businesses before combining their results. Exchange "
                    "resale buys transferable ticket rights, carries mark-to-market inventory "
                    "risk, and often waits until after the event for settlement. Suite "
                    "seat-splitting commits to a block, then distributes permitted individual "
                    "admissions while sharing catering, host, and minimum-spend obligations. "
                    "Corporate hospitality assembles admissions and specified services under "
                    "customer and supplier contracts with different cancellation clocks. "
                    "For chapter mapping, the 12 operating lanes are multi-exchange drop-curve "
                    "resale; NFL playoff-option strips; NBA playoff-option strips; regular-season "
                    "suite splitting; playoff suite splitting; Super Bowl hospitality; World "
                    "Cup hospitality; F1 hospitality; Masters hospitality; Final Four hospitality; "
                    "authorized sponsor-allotment redistribution; and retained corporate ticket "
                    "sourcing. These are the chapter's operating decomposition, not twelve "
                    "identically funded inventory strategies. A $10,000 resale purchase may "
                    "be entirely prepaid, a $10,000 suite may require staged deposits, and "
                    "a $10,000 sourcing engagement may expose only a commission receivable "
                    "if the customer contracts directly with suppliers. Authenticate allocation "
                    "rights and redistribution permissions before assigning value to any "
                    "sponsor offer. Require event-specific proof for claimed official hospitality "
                    "status. For playoff strips, record which games exist conditionally, who "
                    "receives refunds for unplayed games, and whether those refunds arrive "
                    "before the next supplier payment."
                ),
                (
                    "The required play, multi_exchange_pos_broadcast_drop_curve_arbitrage, "
                    "uses supported, authorized SkyBox or Automatiq integrations, with Logitix "
                    "as another evaluated POS option. Verify actual account and inventory "
                    "eligibility for StubHub, Vivid Seats, SeatGeek, TickPick, GameTime, and "
                    "Ticketmaster Resale rather than assuming universal connectivity. A "
                    "Base-equivalent cohort of twenty fulfilled tickets billed at $505 each "
                    "produces $10,100 gross and carries $6,060 of sold-ticket acquisition "
                    "cost. Deduct $707 seller fees, $252.50 incremental inventory impairment, "
                    "$151.50 expected reversal losses, $360 delivery labor, $180 acquisition "
                    "CAC, $360 allocated overhead, and $110 financing to retain $1,919, "
                    "or $95.95 per fulfilled ticket. The impairment allocation covers separate "
                    "carried inventory losses, not a second charge for markdowns already "
                    "embedded in the $505 realized price. Reprice against net realizable "
                    "proceeds, considering fees and transfer deadlines rather than headline "
                    "asks. Trigger an immediate internal hold when an order arrives and "
                    "verify remote delisting acknowledgments. These controls reduce duplicate "
                    "sales without eliminating race conditions. If synchronization fails, pause "
                    "affected broadcasting, remove residual listings through authorized account "
                    "interfaces, notify exchanges promptly, and resolve obligations through "
                    "permitted equivalent replacements or the required cancellation process."
                ),
            ],
            "table": {
                "caption": "Seven Underwriting Records Separating the Twelve Operating Lanes",
                "headers": [
                    "Operating lane and commercial scope",
                    "Revenue and acquisition measurement",
                    "Capital and settlement exposure",
                    "Required failure response and evidence",
                ],
                "rows": [
                    [
                        "Multi-exchange drop-curve resale through eligible authorized distribution channels.",
                        "Twenty fulfilled tickets generate $10,100 before seller-fee deductions.",
                        "$6,060 sold-ticket basis remains exposed until payout clears.",
                        "Pause affected listings when delisting acknowledgments exceed tested latency.",
                    ],
                    [
                        "NFL and NBA conditional playoff-option ticket strip positions.",
                        "Attribute strip cost across executable games and refundable rights.",
                        "Unplayed-game refunds can arrive after subsequent purchase obligations.",
                        "Reprice surviving games and trace refunds to original purchasers.",
                    ],
                    [
                        "Regular-season and playoff suite seat-splitting with documented permissions.",
                        "Eighteen $500 admissions produce $9,000 against $6,000 suite cost.",
                        "Suite deposits and catering commitments precede individual seat collections.",
                        "Stop individual sales when the venue prohibits seat redistribution.",
                    ],
                    [
                        "Super Bowl and World Cup contracted corporate hospitality.",
                        "Four $5,000 packages yield $20,000 before supplier pass-through costs.",
                        "Supplier deposits may precede customer acceptance and final payment.",
                        "Replace failed components only within documented customer substitution rights.",
                    ],
                    [
                        "F1, Masters, and Final Four event-specific hospitality programs.",
                        "Price admission rights separately from transport and hosted services.",
                        "Different suppliers impose different cancellation dates and payment schedules.",
                        "Verify permitted transfer and access terms for every component.",
                    ],
                    [
                        "Sponsor-allotment redistribution supported by explicit contractual resale authority.",
                        "Recognize only the operator's contracted economics under documented control.",
                        "Late allocation releases concentrate delivery work and replacement exposure.",
                        "Reject unsupported allocations rather than financing promised future access.",
                    ],
                    [
                        "Retained corporate sourcing where customers contract directly with suppliers.",
                        "A $1,000 earned sourcing fee excludes client ticket spending.",
                        "Commission receivables create collection exposure without owned ticket inventory.",
                        "Suspend incremental sourcing when invoices breach agreed credit limits.",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Price the settlement terms as carefully as the seat",
                "body": (
                    "A small headline spread can outperform a larger spread when the "
                    "first position settles sooner and carries enforceable delivery rights."
                ),
                "items": [
                    "Maintain fee schedules by exchange account, inventory category, and contract version; calculate the channel's net bid before moving a listing.",
                    "Record successful remote delisting acknowledgments, not merely outbound POS requests; quarantine inventory when acknowledgment latency exceeds the tested operating threshold.",
                    "Deliver SafeTix inventory through issuer-supported transfer and wallet flows; copied rotating barcodes do not establish successful delivery.",
                    "For playoff strips, maintain a game-by-game refund calendar and use only cleared refunds, rather than expected refunds, to replenish purchasing capacity.",
                ],
            },
        },
        {
            "heading": "2. Reconcile every dollar from gross volume to owner profit",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "The annual waterfall below preserves every canonical Formula v2.0 "
                    "endpoint. Its intermediate expense allocations are explicit underwriting "
                    "assumptions, not additional outputs supplied by the scorecard engine. "
                    "Acquisition consumes 60% of gross volume in each case. Remaining "
                    "deductions total $61,600 Conservative, $212,100 Base, and $252,000 "
                    "Scaled, leaving exactly $26,400, $191,900, and $468,000 of owner "
                    "profit. Gross-basis margins are 12%, 19.0%, and 26%; dividing the "
                    "same profits by retained revenue produces 30%, 47.5%, and 65%. "
                    "Weighted seller fees decline from 8% to 7% to 4% because the "
                    "illustrative mix shifts toward direct suite and hospitality contracts; "
                    "these are portfolio assumptions, not advertised marketplace rates. "
                    "The Scaled case requires evidence for that mix change before adoption. "
                    "Inventory impairment is 3%, 2.5%, and 1% of gross volume; reversal "
                    "expense is 2%, 1.5%, and 0.5%. Smaller loss ratios require better "
                    "contract matching and underwriting, not simply more listings. Actual "
                    "ledger results must replace these allocations monthly while preserving "
                    "the distinction between original underwriting, revised forecast, and "
                    "realized economics. Any variance becomes a named bridge item rather "
                    "than an unexplained adjustment to retained share."
                ),
                (
                    "Labor must include the work that automated broadcasting cannot finish: "
                    "supplier verification, exception handling, customer coordination, transfer "
                    "chasing, invoice reconciliation, and event-day escalation. Conservative "
                    "delivery labor assigns $12,000 across two contractors; Base assigns "
                    "$36,000 across two contractors. Scaled assigns $30,000 across three "
                    "contractors plus $54,000 of fully loaded nonowner employee expense, "
                    "totaling $84,000. Those are annual budgets requiring role-specific "
                    "hours and local pay validation, not asserted market wage schedules. "
                    "The owner supplies the remaining full-time role in each case, so "
                    "owner profit includes compensation for their work rather than profit "
                    "after a separate owner replacement salary. Team counts therefore "
                    "remain 1 FT + 2 C, 1 FT + 2 C, and 2 FT + 3 C. "
                    "Acquisition CAC means customer acquisition expenditure, separate from "
                    "ticket acquisition: outreach, paid lead generation, referral costs, and "
                    "sales effort purchased externally. Combine delivery labor, CAC, and "
                    "fixed overhead to obtain monthly operating budgets of $2,500, $7,500, "
                    "and $11,000. Exchange fees, loss provisions, and financing remain "
                    "separate variable or capital costs. Never describe that monthly operating "
                    "budget as the entire cash requirement for running the brokerage."
                ),
                (
                    "Use product-level waterfalls to test whether the annual blend is "
                    "credible. A suite costs $6,000 for twenty permitted admissions. Selling "
                    "eighteen at $500 generates $9,000; the two empty seats already reduce "
                    "billings from the $10,000 sellout plan. Deduct $180 collection fees, "
                    "$180 reversal provision, $450 fulfillment labor, $150 CAC, $300 "
                    "overhead, and $200 financing, leaving $1,540. Do not subtract another "
                    "$1,000 for those empty seats. Selling only seventeen seats reduces "
                    "profit to $1,060 when fees and reversal provision remain 2% each "
                    "and other costs stay fixed. A fully sold hospitality cohort of four "
                    "$5,000 packages has $12,000 supplier cost, $400 collection fees, "
                    "$600 expected reversal expense, $1,200 delivery labor, $600 CAC, "
                    "$500 overhead, and $500 financing, leaving $4,200. Its 21% margin "
                    "does not establish the portfolio's 26% Scaled margin; other cohorts "
                    "must supply the difference. For either product, document access, hosting, "
                    "transport, and catering obligations independently. Customer deposits remain "
                    "liabilities until the relevant performance occurs. An unused refundable "
                    "supplier deposit remains an asset until recovered or impaired, not an "
                    "instant expense or a second source of earned spread."
                ),
            ],
            "table": {
                "caption": "Formula v2.0 Annual Gross-to-Net Bridge with Explicit Expense Allocations",
                "headers": [
                    "Waterfall line and accounting treatment",
                    "Conservative annual case and allocation",
                    "Base annual case and allocation",
                    "Scaled annual case and allocation",
                ],
                "rows": [
                    [
                        "Gross seller-attributable volume before separately deducted selling expenses.",
                        "$220,000 gross volume establishes the annual underwriting denominator.",
                        "$1,010,000 gross volume establishes the annual underwriting denominator.",
                        "$1,800,000 gross volume establishes the annual underwriting denominator.",
                    ],
                    [
                        "Subtract acquisition basis allocated to sold tickets and services.",
                        "$132,000 acquisition basis consumes 60% of gross volume.",
                        "$606,000 acquisition basis consumes 60% of gross volume.",
                        "$1,080,000 acquisition basis consumes 60% of gross volume.",
                    ],
                    [
                        "Retained contribution subtotal before operating deductions and loss provisions.",
                        "$88,000 retained contribution equals the required 40% share.",
                        "$404,000 retained contribution equals the required 40% share.",
                        "$720,000 retained contribution equals the required 40% share.",
                    ],
                    [
                        "Subtract weighted seller fees and direct payment collection expenses.",
                        "$17,600 expense assumes an 8% blended collection burden.",
                        "$70,700 expense assumes a 7% blended collection burden.",
                        "$72,000 expense assumes a 4% blended collection burden.",
                    ],
                    [
                        "Subtract incremental unsold inventory impairments outside realized selling prices.",
                        "$6,600 expense reserves 3% for incremental inventory losses.",
                        "$25,250 expense reserves 2.5% for incremental inventory losses.",
                        "$18,000 expense reserves 1% for incremental inventory losses.",
                    ],
                    [
                        "Subtract expected unrecovered cancellation, scrub, replacement, and reversal losses.",
                        "$4,400 provision allocates 2% to expected unrecovered losses.",
                        "$15,150 provision allocates 1.5% to expected unrecovered losses.",
                        "$9,000 provision allocates 0.5% to expected unrecovered losses.",
                    ],
                    [
                        "Subtract contractor delivery labor and nonowner employee employment costs.",
                        "$12,000 delivery budget supports the two contractor roles.",
                        "$36,000 delivery budget supports the two contractor roles.",
                        "$84,000 includes $30,000 contractors and $54,000 loaded employment.",
                    ],
                    [
                        "Subtract customer acquisition expenditure without duplicating ticket acquisition basis.",
                        "$6,000 customer acquisition budget supports measured referral and outreach.",
                        "$18,000 customer acquisition budget supports measured referral and outreach.",
                        "$12,000 customer acquisition budget assumes repeat contracted customer demand.",
                    ],
                    [
                        "Subtract fixed software, insurance, accounting, and administrative operating expenses.",
                        "$12,000 fixed expense requires a $1,000 monthly budget.",
                        "$36,000 fixed expense requires a $3,000 monthly budget.",
                        "$36,000 fixed expense requires a $3,000 monthly budget.",
                    ],
                    [
                        "Subtract financing expense while retaining debt principal on balance sheet.",
                        "$3,000 financing expense implies $25,000 average borrowing at 12%.",
                        "$11,000 financing expense implies approximately $91,667 average borrowing at 12%.",
                        "$21,000 financing expense implies $175,000 average borrowing at 12%.",
                    ],
                    [
                        "Owner profit after all listed deductions and before personal taxes.",
                        "$26,400 owner profit equals 12% gross and 30% retained.",
                        "$191,900 owner profit equals 19.0% gross and 47.5% retained.",
                        "$468,000 owner profit equals 26% gross and 65% retained.",
                    ],
                ],
            },
        },
        {
            "heading": "3. Reserve for failed economics, then stress the assumptions",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Maintain separate loss and liquidity ledgers. Expected economic losses "
                    "reduce profit; a cash reserve or processor hold restricts availability "
                    "without automatically creating another expense. Build a reversal register "
                    "for canceled events, postponed events, invalid inventory, rejected delivery, "
                    "customer disputes, and duplicate-sale replacements. For each exposure, "
                    "record gross refund liability, expected supplier recovery, unrecoverable "
                    "fees, replacement cost, and the timing of each movement. A $5,000 "
                    "customer refund with a collectible $4,000 supplier reimbursement creates "
                    "$1,000 expected economic loss before incremental expenses, but may "
                    "require the full $5,000 immediately. A postponement can extend the "
                    "payout lock without producing a refund entitlement; apply the actual "
                    "customer and marketplace terms. For cohort forecasting, estimate loss "
                    "probability multiplied by net loss severity, then add concentration "
                    "stress for correlated event failures. Reconcile provisions to actual "
                    "charges and recoveries, releasing excess amounts only when the "
                    "underlying uncertainty resolves. In financial reporting, classify each "
                    "item according to its substance rather than treating every forecast "
                    "allowance as an interchangeable reserve. Never count both a reduced "
                    "selling price and a separate markdown expense for the same seat. "
                    "Likewise, track supplier recovery rights without assuming disputed "
                    "receivables are usable cash."
                ),
                (
                    "Validate any claimed 200% double-sale replacement penalty against the "
                    "applicable exchange agreement, including its calculation basis, alternatives, "
                    "caps, and additional charges. If a contract actually permits a charge "
                    "equal to 200% of a $500 sale price, the stated charge is $1,000; "
                    "that is not proof that every duplicate costs $1,000 or that the "
                    "charge includes every other liability. Ten such charges would consume "
                    "$10,000 before any separately payable refunds or sourcing costs. "
                    "Retain order timestamps, POS hold timestamps, listing identifiers, "
                    "delisting responses, and issuer transfer acceptance records so the "
                    "operator can reconstruct the failure without speculation. Under "
                    "15 U.S.C. §45c, do not circumvent purchase limits or ticketing security "
                    "measures; automated distribution of legitimately acquired inventory "
                    "is operationally different from prohibited acquisition circumvention. "
                    "SafeTix fulfillment must follow issuer-supported transfer and wallet "
                    "flows rather than copied rotating barcodes. Apply 16 CFR Part 464 "
                    "to covered live-event ticket offers, including required upfront total "
                    "pricing and accurate fee representations. Check New York Arts and "
                    "Cultural Affairs Law Article 25 for applicable reseller obligations. "
                    "These requirements belong in cost and delivery design because a "
                    "nontransferable allocation or incorrectly quoted price can erase an "
                    "otherwise attractive modeled spread."
                ),
                (
                    "Run sensitivities against all three canonical cases using the same "
                    "denominator and clearly stated cost behavior. A two-percentage-point "
                    "increase in seller fees removes $4,400, $20,200, and $36,000 of "
                    "profit respectively. An additional three points of incremental inventory "
                    "loss removes $6,600, $30,300, and $54,000. Raising reversal losses "
                    "one point removes another $2,200, $10,100, and $18,000. Applying "
                    "all three stresses together leaves $13,200, $131,300, and $360,000, "
                    "before any additional settlement financing. A ten-day persistent "
                    "extension in the inventory funding cycle requires approximately "
                    "$3,616, $16,603, and $29,589 more average capital when measured "
                    "against annual sold-ticket acquisition cost. At a 12% annual borrowing "
                    "rate, that adds approximately $434, $1,992, and $3,551 of annual "
                    "interest. This interest is an incremental stress, not a replacement "
                    "for the existing financing line. Test revenue contraction separately: "
                    "if volume falls 10%, acquisition and seller fees flex proportionally "
                    "while all other budget lines stay fixed, resulting profits are "
                    "$19,360, $158,570, and $403,200. Finally, run event-specific cliff "
                    "tests; a portfolio average cannot represent losing the only hospitality "
                    "allocation that supports several prepaid corporate orders."
                ),
            ],
            "table": {
                "caption": "Seven Sensitivity Tests Applied to the Canonical Annual Profit Cases",
                "headers": [
                    "Stress definition and cost behavior",
                    "Conservative resulting annual owner profit",
                    "Base resulting annual owner profit",
                    "Scaled resulting annual owner profit",
                ],
                "rows": [
                    [
                        "Seller-fee burden increases by two percentage points of gross.",
                        "$22,000 remains after deducting $4,400 additional seller fees.",
                        "$171,700 remains after deducting $20,200 additional seller fees.",
                        "$432,000 remains after deducting $36,000 additional seller fees.",
                    ],
                    [
                        "Incremental inventory loss increases by three points of gross.",
                        "$19,800 remains after deducting $6,600 additional inventory losses.",
                        "$161,600 remains after deducting $30,300 additional inventory losses.",
                        "$414,000 remains after deducting $54,000 additional inventory losses.",
                    ],
                    [
                        "Unrecovered reversal losses increase by one point of gross.",
                        "$24,200 remains after deducting $2,200 additional reversal losses.",
                        "$181,800 remains after deducting $10,100 additional reversal losses.",
                        "$450,000 remains after deducting $18,000 additional reversal losses.",
                    ],
                    [
                        "Combine fee, inventory, and reversal stresses without interaction effects.",
                        "$13,200 remains after the combined $13,200 incremental deduction.",
                        "$131,300 remains after the combined $60,600 incremental deduction.",
                        "$360,000 remains after the combined $108,000 incremental deduction.",
                    ],
                    [
                        "Persistent ten-day acquisition funding extension financed at 12% annually.",
                        "$25,966 approximately remains after $434 incremental annual interest.",
                        "$189,908 approximately remains after $1,992 incremental annual interest.",
                        "$464,449 approximately remains after $3,551 incremental annual interest.",
                    ],
                    [
                        "Borrowing rate rises three points on baseline average balances.",
                        "$25,650 remains after $750 interest on $25,000 borrowing.",
                        "$189,150 remains after approximately $2,750 additional borrowing expense.",
                        "$462,750 remains after $5,250 interest on $175,000 borrowing.",
                    ],
                    [
                        "Gross volume contracts 10%; only acquisition and seller fees flex.",
                        "$19,360 remains after losing $7,040 of net contribution.",
                        "$158,570 remains after losing $33,330 of net contribution.",
                        "$403,200 remains after losing $64,800 of net contribution.",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four checks before committing the next event cohort",
                "body": (
                    "Authorize the purchase only when rights, delivery, downside economics, "
                    "and available liquidity are evidenced at the inventory-lot level."
                ),
                "items": [
                    "Verify seller identity, transferable admission rights, suite splitting permission, purchase-limit adherence, and any required reseller licensing before wiring supplier funds.",
                    "Test the actual POS channel connection, internal auto-hold, remote delisting acknowledgment, and issuer-supported transfer path for the inventory type being purchased.",
                    "Reconcile realized-price assumptions, seller fees, incremental inventory losses, reversal provisions, labor, CAC, overhead, and interest to a positive stressed contribution.",
                    "Show sufficient unrestricted cash and committed borrowing for peak supplier payments, customer refund exposure, payout holds, and a documented postponement scenario.",
                ],
            },
        },
        {
            "heading": "4. Fund the payout lock without confusing profit with cash",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Build a dated cash calendar for every inventory lot and consolidate "
                    "it into a rolling thirteen-week forecast. Record supplier deposit, "
                    "supplier balance, customer order, customer collection, event date, "
                    "transfer deadline, exchange release, bank availability, and possible "
                    "refund dates. These dates answer different questions. Customer DSO "
                    "measures collection after the relevant invoice or receivable trigger; "
                    "a marketplace's post-event payout lock is an additional contractual "
                    "restriction and should remain separately visible. Buying at day minus "
                    "sixty and receiving cleared payout at day plus ten creates seventy "
                    "days of inventory funding even if the customer ordered immediately. "
                    "Financing $6,060 for seventy days at 12% costs $139.46 using a "
                    "365-day year. That exceeds the earlier cohort's $110 allocated "
                    "financing by $29.46 and reduces its $1,919 profit to $1,889.54 "
                    "if all other lines remain unchanged. The comparison illustrates why "
                    "portfolio financing allocations must be reconciled to actual cohort "
                    "duration. Enter bank-clearing time and business-day release rules "
                    "explicitly rather than calling every promised payout date available "
                    "cash. For postponed events, extend the inventory lock and recalculate "
                    "interest before initiating another buying cycle, even when the "
                    "original ticket remains valid."
                ),
                (
                    "A useful first approximation for steady-state acquisition float is "
                    "annual acquisition cash cost multiplied by funded days and divided "
                    "by 365, adjusted for supplier credit and genuinely usable customer "
                    "collections. At seventy funded days, the Base sold-ticket basis of "
                    "$606,000 implies $116,219 of acquisition float before unsold inventory, "
                    "payroll, loss coverage, or seasonal concentration. This is a planning "
                    "approximation, not the peak cash forecast. The $10,000–$50,000 startup "
                    "capital range can support a narrow initial book, particularly with "
                    "short settlement cycles or properly matched customer deposits; it "
                    "does not finance unrestricted ownership of the Base or Scaled "
                    "inventory portfolio. Baseline annual interest assumes average funded "
                    "borrowings of $25,000, approximately $91,667, and $175,000 at 12%. "
                    "Equity, supplier terms, and permissible customer funding must cover "
                    "the rest, while committed facilities must accommodate seasonal peaks "
                    "above those averages. A bank line advertised at $150,000 is not "
                    "fully available if borrowing-base exclusions or existing draws consume "
                    "capacity. Keep restricted processor balances, disputed receivables, "
                    "and refundable customer money out of unrestricted liquidity. Calculate "
                    "minimum required cash from the worst cumulative dated deficit plus "
                    "the selected refund shock buffer, not from a percentage of annual profit."
                ),
                (
                    "Corporate hospitality can shorten cash gaps only when customer and "
                    "supplier contracts actually align. On the $20,000 package cohort, "
                    "an illustrative 50% customer deposit collects $10,000 while a 50% "
                    "supplier deposit consumes $6,000. The apparent $4,000 surplus remains "
                    "subject to performance and refund obligations. If the remaining "
                    "$6,000 supplier balance is due before the final $10,000 customer "
                    "collection, the cohort reaches a $2,000 acquisition deficit before "
                    "labor, overhead, and risk coverage. If the customer instead pays "
                    "thirty days after the event, that receivable persists beyond delivery. "
                    "Do not finance unrelated events with refundable deposits while "
                    "ignoring the corresponding refund claim. Set exposure limits by "
                    "event, supplier, exchange, and corporate customer, then stop new "
                    "purchases when the cash calendar breaches the available funding "
                    "envelope. Close each event by matching admissions delivered, exchange "
                    "statements, customer invoices, supplier credits, contractor time, "
                    "and bank receipts. Release reserves according to resolved exposures, "
                    "not because the event date passed. Publish both earned owner profit "
                    "and distributable cash: debt repayment, inventory replenishment, "
                    "restricted reserves, and tax funding can make the second materially "
                    "smaller. This is live-event inventory and service settlement management, "
                    "not the wholesale electronics buying-group economics addressed in Volume 041."
                ),
            ],
            "table": {
                "caption": "Seven Cash Controls for Exchange Resale, Suites, and Corporate Hospitality",
                "headers": [
                    "Cash mechanism requiring separate tracking",
                    "Concrete timing or capital calculation",
                    "Operating record and accountable reconciliation",
                    "Funding response when timing deteriorates",
                ],
                "rows": [
                    [
                        "Exchange inventory purchased before an event and settled afterward.",
                        "$6,060 funded for seventy days costs $139.46 at 12%.",
                        "Match supplier payment dates against cleared exchange bank receipts.",
                        "Reduce new purchases when delayed releases consume committed headroom.",
                    ],
                    [
                        "Steady-state Base acquisition float before additional operating cash needs.",
                        "$606,000 annual acquisition basis times seventy divided by 365 equals $116,219.",
                        "Reconcile the planning estimate against actual dated inventory outflows.",
                        "Add seasonal peaks, unsold inventory, and operating payment obligations.",
                    ],
                    [
                        "Suite contracts with advance deposits and minimum service commitments.",
                        "$6,000 acquisition commitment precedes the eighteen-seat $9,000 collection target.",
                        "Track venue invoices separately from catering and hosting obligations.",
                        "Cut exposure before nonrefundable balances exceed funded customer demand.",
                    ],
                    [
                        "Hospitality customer deposits offset only contractually usable supplier funding.",
                        "$10,000 collected less $6,000 supplier deposit leaves $4,000 temporarily.",
                        "Maintain customer liabilities and cancellation schedules beside bank balances.",
                        "Preserve refund coverage rather than distributing the temporary surplus.",
                    ],
                    [
                        "Hospitality final supplier balance precedes final customer collection.",
                        "$12,000 cumulative supplier payments against $10,000 collections creates $2,000 deficit.",
                        "Schedule final invoice dates and monitor actual corporate payment behavior.",
                        "Arrange committed bridging funds before the supplier balance falls due.",
                    ],
                    [
                        "Cancellation creates a gross refund need before supplier recovery.",
                        "$5,000 immediate refund precedes a collectible $4,000 supplier reimbursement.",
                        "Track the $1,000 economic loss separately from $5,000 liquidity exposure.",
                        "Use the refund buffer and pursue documented supplier recovery rights.",
                    ],
                    [
                        "Post-event receivable persists under negotiated corporate customer payment terms.",
                        "Thirty-day customer terms extend collection beyond completed hospitality delivery.",
                        "Age receivables from the contractual invoice trigger and verify acceptance.",
                        "Stop additional unsecured sourcing when customer exposure exceeds approved limits.",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Create the inventory-lot economics record",
                    "action": "Assign event, supplier, rights, channel, acquisition basis, and contractual delivery identifiers before committing capital.",
                    "detail": "Store gross seller-attributable billings, expected fees, realized-price assumptions, incremental inventory losses, and fulfillment obligations in separate fields.",
                },
                {
                    "step": 2,
                    "title": "Build the dated funding bridge",
                    "action": "Schedule supplier payments, customer collections, exchange holds, bank clearing, and refund exposures for the full cohort.",
                    "detail": "Calculate peak cumulative deficit, available unrestricted cash, remaining committed borrowing, and the financing expense implied by actual funded days.",
                },
                {
                    "step": 3,
                    "title": "Execute delivery with verified inventory locks",
                    "action": "Apply internal POS auto-holds, verify remote delisting, and complete issuer-supported transfer with acceptance evidence.",
                    "detail": "When synchronization fails, pause affected inventory, remove residual listings through authorized interfaces, contact exchanges, and resolve duplicate obligations under the applicable contracts.",
                },
                {
                    "step": 4,
                    "title": "Close the event and release only resolved exposure",
                    "action": "Reconcile supplier invoices, customer billings, exchange deductions, contractor time, recoveries, and cleared bank receipts.",
                    "detail": "Bridge forecast profit to actual owner profit, update loss estimates, and calculate distributable cash after replenishment, debt service, reserves, and tax funding.",
                },
            ],
        },
    ],
    "pull_quote": "A ticket spread becomes owner profit only after the seat is delivered, every deduction is booked, and the settlement cash clears.",
    "diagram_id": "diag-03",
    "action_checklist": [
        "Normalize every exchange statement to seller-attributable gross billings and reconcile the 40% retained-share view without deducting seller fees twice.",
        "Rebuild the Conservative, Base, and Scaled waterfalls to exactly $26,400, $191,900, and $468,000 of annual owner profit.",
        "Separate exchange resale, permitted suite seat-splitting, and corporate hospitality into distinct inventory, delivery, reserve, and settlement cohorts.",
        "Run the seven sensitivity tests, validate contract-specific duplicate-sale remedies, and document the resulting event and counterparty exposure limits.",
        "Build a thirteen-week dated cash forecast that separates customer DSO, post-event payout locks, bank availability, refundable deposits, and committed borrowing.",
        "Test authorized POS holds, cross-channel delisting acknowledgments, and issuer-supported transfers before releasing inventory into multi-exchange distribution.",
    ],
    "statutory_citations": [
        {
            "title": "15 U.S.C. §45c — Unfair and deceptive acts and practices relating to ticket sales",
            "url": "https://www.law.cornell.edu/uscode/text/15/45c",
            "relevance": (
                "Prohibits specified circumvention of ticketing security measures and "
                "purchase controls, and specified sales of tickets obtained through "
                "such violations; authorized POS distribution must remain separate "
                "from prohibited acquisition practices."
            ),
        },
        {
            "title": "16 CFR §464.2 — Unfair or deceptive fees",
            "url": "https://www.ecfr.gov/current/title-16/chapter-I/subchapter-D/part-464/section-464.2",
            "relevance": (
                "Requires covered live-event ticket price offers to disclose total "
                "price and satisfy prominence and final-payment presentation rules; "
                "build mandatory charges into customer-facing pricing as required."
            ),
        },
        {
            "title": "16 CFR §464.3 — Misleading fees",
            "url": "https://www.ecfr.gov/current/title-16/chapter-I/subchapter-D/part-464/section-464.3",
            "relevance": (
                "Prohibits misrepresenting fee purposes and refundability and requires "
                "specified disclosures about excluded charges before payment consent; "
                "align package quotes and cancellation representations with actual terms."
            ),
        },
        {
            "title": "N.Y. Arts and Cultural Affairs Law Article 25 — Tickets to Places of Entertainment",
            "url": "https://www.nysenate.gov/legislation/laws/ACA/A25",
            "relevance": (
                "Provides New York ticket-sale and resale requirements, including "
                "applicable licensing, disclosure, and operating obligations; determine "
                "which provisions govern the seller, transaction, and inventory."
            ),
        },
        {
            "title": "N.Y. Arts and Cultural Affairs Law §25.13 — Licensing of ticket resellers",
            "url": "https://www.nysenate.gov/legislation/laws/ACA/25.13",
            "relevance": (
                "Establishes ticket-reseller licensing requirements and related "
                "conditions; validate applicability and include required operating "
                "costs before underwriting New York resale activity."
            ),
        },
    ],
}
