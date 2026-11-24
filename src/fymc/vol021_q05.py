from __future__ import annotations

CHAPTER_5 = {'id': 'Q5',
 'chapter_id': 'Q5',
 'chapter_number': 5,
 'question_number': 5,
 'slug': 'cash-conversion-cycle-working-capital',
 'question_prompt': 'Why is my business profitable but short on cash, and how does working capital affect '
                    'the price when the business is sold?',
 'kicker': 'Q5 / THE BIG MONEY PLAYBOOKS',
 'title': 'Cash Conversion Cycle and Working Capital',
 'subtitle': 'DIO + DSO − DPO, inventory estimates, why profit and cash diverge in e-commerce, shortening '
             'the cycle, and working-capital pegs, seasonal normalization, and purchase-price adjustments '
             'in a business sale',
 'layout_template': 'case_study',
 'reading_time_minutes': 15,
 'executive_summary': 'Practitioners converge on one formula: inventory days plus sales days minus payable '
                      'days, the number of days cash sits locked between paying suppliers and collecting '
                      'from customers. LedgerGurus typically sees e-commerce cycles of at least 90 days, '
                      'with some brands carrying 180 to 240 days of inventory, while Dell, Costco, Procter '
                      '& Gamble, and Amazon run near-zero or negative cycles. The street mechanics convert '
                      'days into dollars: InstructorTom prices a 65-day cycle at 59 million dollars of '
                      'working capital and about 4 million a year in interest, and Kurtis Hanni cut a '
                      "client's cycle from 230 to 45 days, slashing required cash from 235,000 to 67,000 "
                      'dollars. Speakers split on how far to stretch payables, on whether the metric moves '
                      'valuation, and on how to set the working capital peg when a business is sold.',
 'key_metrics': [{'label': 'Client cash conversion cycle after supplier and collection fixes',
                  'metric': 'Client cash conversion cycle after supplier and collection fixes',
                  'value': '230 days cut to 45 days; cash required cut from $235,000 to $67,000',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Bison CFO client importing inventory: shipping cut from 185 to 15 days, '
                             'supplier billed only on arrival, cash positive moved to month two.',
                  'source': 'Kurtis Hanni ([0WBeNhRVKHY @ 00:11:29])'},
                 {'label': 'Typical e-commerce cash conversion cycle observed',
                  'metric': 'Typical e-commerce cash conversion cycle observed',
                  'value': 'At least 90 days; some brands hold 180 to 240 days of inventory',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'What the LedgerGurus team reports seeing across e-commerce clients, '
                             'especially those with slow supply chains or wholesale terms.',
                  'source': 'LedgerGurus: Ecommerce Accounting Experts ([F-Y1cubdesE @ 00:04:57])'},
                 {'label': 'Annualized cost of skipping a 2/10 net 30 discount',
                  'metric': 'Annualized cost of skipping a 2/10 net 30 discount',
                  'value': '37.2%',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Letting a 2 percent 10-day discount lapse to hold cash 20 extra days, framed '
                             'as an expensive way to finance the business.',
                  'source': 'One Minute Finance ([7yuWFm95LDw @ 00:07:11])'},
                 {'label': 'Working capital tied up by a 65-day cycle',
                  'metric': 'Working capital tied up by a 65-day cycle',
                  'value': '$59 million of working capital; about $4 million a year in interest at 7%',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Average daily cost of goods sold multiplied by 65 cycle days, then '
                             'multiplied by a 7 percent cost of debt.',
                  'source': 'InstructorTom ([Ju1MGgf9RUw @ 00:03:32])'}],
 'sections': [{'title': 'The Practitioner Consensus: Days Are Dollars Locked in the Loop',
               'paragraphs': ['Every speaker runs the same three-gear math: days inventory outstanding '
                              'plus days sales outstanding minus days payable outstanding. Invoice Finance '
                              'News frames it as the speed at which cash turns into inventory and back '
                              'into cash through sales, with a worked case of 40 + 30 - 40 = 30 days '
                              '[Ooq0PnAEf5s @ 00:01:20]. Laurence Gartside gives the same formula and the '
                              'operator translation: turn inventory fast, get paid fast, and pay suppliers '
                              'as late as possible, assuming no interest is being charged; his shoe shop '
                              'runs 5 + 15 - 12 = 8 days [z3z_GomovEI @ 00:03:02]. Mergers & Inquisitions '
                              'lays out the identical structure as average inventory over cost of goods '
                              'sold, average receivables over revenue, and average payables over cost of '
                              'goods sold, each multiplied by days in the period, landing a 45 + 30 - 40 = '
                              '35-day example [rNjMWAOJHwM @ 00:02:22]. Luke Kermode adds the cleanest '
                              'timeline view: the cycle runs from the day cash leaves for suppliers to the '
                              'day cash lands from customers, while the operating cycle is just inventory '
                              'days plus sales days before supplier credit is netted out [1gBvyu9ADGo @ '
                              '00:01:48]. The shared verdict is blunt: shorter is better, and longer means '
                              'cash is trapped and the operation is running inefficiently.',
                              'The second point of agreement is that profit and cash are separate '
                              'scoreboards. LedgerGurus opens with the e-commerce owner asking where the '
                              'cash went despite profits, and calls the cycle a cash survival metric: '
                              'every store pre-funds growth by buying inventory before it sells, paying '
                              'suppliers before customers pay, and waiting on Shopify, Amazon, and '
                              'wholesale payouts [F-Y1cubdesE @ 00:00:30]. The same team stresses that the '
                              'number never appears on the profit and loss or the balance sheet; it is '
                              'calculated from both, which is exactly why accrual books can show profit '
                              'with no cash in the bank [F-Y1cubdesE @ 00:05:28]. One Minute Finance '
                              'answers its own question of whether a highly profitable company can go '
                              'broke with a resounding yes, describing cash frozen in warehouse stock and '
                              'then stuck again in unpaid invoices, while sales growth absorbs more '
                              'receivables and inventory and opens a funding gap [7yuWFm95LDw @ 00:01:10]. '
                              'Marketing Business Network walks a single batch of lamps through the loop: '
                              'supplier paid on day thirty, customer cash on day sixty, a thirty-day hole '
                              'the business funds itself, and a reminder that wages, rent, and taxes still '
                              'need a separate cash forecast [C5Ut79jWwHA @ 00:02:33].',
                              'Practitioners also agree the raw number means little until it is '
                              'benchmarked against the right peer set. Invoice Finance News warns that '
                              'comparing an aircraft builder with a car maker is useless and that the '
                              'comparison has to stay inside one sector [Ooq0PnAEf5s @ 00:02:01]. '
                              "WallStreetMojo's Dheeraj Vaidya runs Colgate at 36.35 days in 2017 creeping "
                              "to 45.51 days in 2020, then sets it beside Procter & Gamble's negative "
                              'cycle and an Amazon figure he puts around minus 24 to 25 days, insisting '
                              'the read only works against the industry [Sw24t4Xzk0I @ 00:15:13]. '
                              'LedgerGurus uses Dell as the negative-cycle model, where the customer pays '
                              'before the build starts, and Costco as the near-zero model, selling stock '
                              'in as little as 10 days against 30-day supplier terms [F-Y1cubdesE @ '
                              '00:04:36]. Mergers & Inquisitions pulls Target and Costco filings and finds '
                              'both under five days with negative years, which it attributes to large '
                              'retailers holding significant pricing and market power [rNjMWAOJHwM @ '
                              '00:06:04]. The consensus warning for small sellers is direct: LedgerGurus '
                              'calls the Dell and Costco structures brilliant but very hard to pull off, '
                              'requiring scale, deep supplier relationships, and fast customer payment, '
                              'conditions most small e-commerce operators simply do not have yet.'],
               'table': {'caption': 'Where the practitioners line up on the cash conversion cycle',
                         'headers': ['Consensus Point',
                                     'What the Practitioner Says',
                                     'Operator Read',
                                     'Expert Source'],
                         'rows': [['Core formula is inventory days plus sales days minus payable days',
                                   'Inventory and receivable days add trapped time; payable days subtract '
                                   'it as supplier financing',
                                   'Build every cash review around these three levers, not revenue alone',
                                   'Invoice Finance News ([Ooq0PnAEf5s @ 00:01:20])'],
                                  ['A shorter cycle signals efficient operations and cash management',
                                   'A short cycle indicates an efficient supply chain, efficient '
                                   'operations, and good cash flow management',
                                   'Recalculate the cycle at each month end and push the number down',
                                   'Laurence Gartside ([z3z_GomovEI @ 00:00:45])'],
                                  ['Profitable stores can still run completely out of cash',
                                   'Accrual books show profit while cash sits somewhere between the '
                                   'factory and the customer',
                                   'Read the cycle alongside the profit and loss before placing any '
                                   'inventory order',
                                   'LedgerGurus: Ecommerce Accounting Experts ([F-Y1cubdesE @ 00:05:28])'],
                                  ['Sales growth itself widens the funding gap that must be financed',
                                   'Growth absorbs receivables and inventory, creating a short-term '
                                   'financing requirement or a cash surplus',
                                   'Model the cash gap before adding a new sales channel or scaling volume',
                                   'One Minute Finance ([7yuWFm95LDw @ 00:02:14])'],
                                  ['Benchmark the number only against peers in the same industry',
                                   "Colgate's rising cycle is judged against Procter & Gamble's negative "
                                   'cycle, not in isolation',
                                   'Pull peer cycles from your own category before judging whether yours '
                                   'is good',
                                   'WallStreetMojo ([Sw24t4Xzk0I @ 00:15:52])'],
                                  ['Negative cycles exist and represent the ideal business model',
                                   'Dell collects from the customer before building; Costco sells in about '
                                   '10 days on 30-day terms',
                                   'Treat a negative cycle as the target structure, knowing it demands '
                                   'real scale',
                                   'LedgerGurus: Ecommerce Accounting Experts ([F-Y1cubdesE @ 00:04:36])'],
                                  ['The cycle works as a leading warning signal for trouble',
                                   'Changes appear in the cycle before the owner feels anything when the '
                                   'economy turns',
                                   'Chart the last one to three years on a spreadsheet to catch drift '
                                   'early',
                                   'Kurtis Hanni ([0WBeNhRVKHY @ 00:13:06])']]}},
              {'title': 'Exact Street Mechanics, Tools & Numbers: Calculating and Shrinking the Gap',
               'paragraphs': ['The mechanics start with getting the denominators right. LedgerGurus '
                              'computes inventory days as average inventory divided by cost of goods sold '
                              'times 365, and sales days as receivables divided by revenue times 365, then '
                              'maps the e-commerce reality: Shopify typically pays out in two business '
                              'days, Amazon every two weeks, and wholesale on 30, 60, or 90-day terms, so '
                              'the moment wholesale is added, cash pressure jumps [F-Y1cubdesE @ '
                              '00:02:26]. Understanding Accounting insists receivables be matched to '
                              'credit sales only; in its Sound Decision case, using credit sales yields 40 '
                              'collection days, while stuffing in 109,500 dollars of cash sales drops the '
                              'computed result to about 34.29 days without any customer paying faster '
                              '[OoegPOU-YCE @ 00:18:55]. The same instructor shows that swapping cost of '
                              'goods sold in for actual credit purchases while inventory is rising pushes '
                              'payment days from 28 to 29.65, overstating supplier credit and making the '
                              'cycle look shorter than it is [GtIbksKcl3Q @ 01:06:52]. Mergers & '
                              'Inquisitions adds period discipline: use 90 days on quarterly figures and '
                              '365 or 366 on full years, and in Excel subtract the two period dates '
                              'instead of hard-coding the day count, after averaging beginning and ending '
                              'balances for each account [rNjMWAOJHwM @ 00:04:03].',
                              'The sharpest operators convert days into a dollar bill. InstructorTom takes '
                              'a 65-day cycle (100 inventory days plus 15 receivable days minus 50 payable '
                              'days), multiplies it by average daily spend on cost of goods sold over 365, '
                              'and lands at 59 million dollars of working capital; at a 7 percent cost of '
                              'debt, that is roughly 4 million dollars a year in interest alone '
                              '[Ju1MGgf9RUw @ 00:03:32]. Tying the model to those inputs, he shows cutting '
                              'inventory days from 100 to 50 lifting the modeled share price from 28.85 to '
                              '30.63, with stretching payables to 80 days and getting customers to pay at '
                              "order driving it higher still [Ju1MGgf9RUw @ 00:05:39]. Kurtis Hanni's "
                              'Bison CFO engagement is the street version: an importer waited 185 days '
                              'from order to warehouse plus 15 days to sell, ran 30 receivable days, and '
                              'paid suppliers on commitment, a 230-day cycle that required 235,000 dollars '
                              'out before a dollar returned [0WBeNhRVKHY @ 00:09:07]. A different sourcing '
                              'arrangement cut transit to 15 days, the supplier billed only on arrival, '
                              'and the cycle collapsed to 45 days, dropping the cash needed from 235,000 '
                              'to 67,000 dollars and turning cash positive in month two [0WBeNhRVKHY @ '
                              '00:11:29].',
                              'The lever menu is consistent across speakers. LedgerGurus prescribes '
                              'improving the cycle without a single extra sale: negotiate better supplier '
                              'terms, tap manufacturer lending programs, layer multiple payment terms, '
                              'even accept a slightly higher unit price in exchange for longer terms, '
                              'clear out inventory sitting on shelves, and tighten reorder points '
                              '[F-Y1cubdesE @ 00:06:37]. One Minute Finance attacks inventory days with '
                              'just-in-time buying, AI demand forecasting to prevent overstocking, lean '
                              'production, and ABC analysis to prioritize the most valuable items, then '
                              'attacks receivables the way GE Healthcare did by overhauling its '
                              'order-to-cash process, plus e-invoicing, automated payment reminders, and '
                              'early-payment discounts [7yuWFm95LDw @ 00:06:04]. Invoice Finance News '
                              'points to factoring to pull receivable cash forward, and to invoice '
                              'discounting schemes where a factor pays the supplier immediately while the '
                              'buyer gets longer to settle, lengthening payable days while the supplier '
                              "still gets paid up front [Ooq0PnAEf5s @ 00:03:51]. Kurtis Hanni's "
                              'collection fix was procedural: more frequent follow-up and forcing '
                              'customers without credit terms to pay immediately, which took receivable '
                              'days from about 35 to 20 over six months and cut bad debt from '
                              'short-relationship buyers [0WBeNhRVKHY @ 00:10:51]. None of these moves '
                              'requires opening a new sales channel.'],
               'table': {'caption': 'Calculations, levers, and the exact numbers practitioners reported',
                         'headers': ['Calculation or Lever',
                                     'Exact Mechanic Taught',
                                     'Number Reported',
                                     'Expert Source'],
                         'rows': [['Days inventory outstanding from average stock',
                                   'Average inventory divided by cost of goods sold, multiplied by days in '
                                   'the period',
                                   "John's pharmacy: $100,000 opening, $200,000 closing, $150,000 average "
                                   'inventory',
                                   'One Minute Finance ([7yuWFm95LDw @ 00:03:44])'],
                                  ['Days sales outstanding by sales channel',
                                   'Receivables divided by revenue times 365; channel payout speed drives '
                                   'the result',
                                   'Shopify about two business days, Amazon every two weeks, wholesale 30 '
                                   'to 90 days',
                                   'LedgerGurus: Ecommerce Accounting Experts ([F-Y1cubdesE @ 00:02:26])'],
                                  ['Days payable built on purchases, not sales',
                                   'Purchases equal cost of goods sold plus ending inventory minus '
                                   'beginning inventory',
                                   'Worked case: 45,000 purchases, payables turnover 3.0, full cycle '
                                   '130.79 days',
                                   'WallStreetMojo ([Sw24t4Xzk0I @ 00:11:18])'],
                                  ['Working capital requirement expressed in dollars',
                                   'Daily cost of goods sold times cycle days, then multiplied by the cost '
                                   'of debt',
                                   '65 days equals $59 million; a 7 percent rate costs about $4 million '
                                   'yearly',
                                   'InstructorTom ([Ju1MGgf9RUw @ 00:03:32])'],
                                  ['Supplier sourcing and pay-on-arrival terms',
                                   'Switch sourcing to cut transit time and pay only when goods reach the '
                                   'warehouse',
                                   'Cycle 230 to 45 days; cash needed $235,000 down to $67,000',
                                   'Kurtis Hanni ([0WBeNhRVKHY @ 00:11:29])'],
                                  ['Skipping a supplier early-payment discount to hold cash',
                                   'Paying at 30 days instead of taking 2 percent for paying within 10 '
                                   'days',
                                   'Annualized cost of passing on the discount reaches 37.2 percent',
                                   'One Minute Finance ([7yuWFm95LDw @ 00:07:11])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Cash-Unlocking Moves Practitioners Actually Use',
                           'body': 'Small structural tweaks to terms, billing triggers, and spreadsheet '
                                   'hygiene move the cycle more than chasing new revenue.',
                           'items': ['Price-for-terms swap: accept a slightly higher unit price and '
                                     'slightly lower profitability in exchange for longer supplier terms '
                                     'that shorten the cash conversion cycle [LedgerGurus: Ecommerce '
                                     'Accounting Experts — F-Y1cubdesE @ 00:06:37].',
                                     "Get billed on arrival, not on order: the client's new supplier did "
                                     'not require payment until goods reached the warehouse and were '
                                     'sellable, handing back 15 days of credit [Kurtis Hanni — 0WBeNhRVKHY '
                                     '@ 00:11:08].',
                                     'Watch the allowance effect: a larger allowance for credit losses '
                                     'shrinks net receivables and shortens calculated collection days even '
                                     'though no customer paid faster [Understanding Accounting — '
                                     'GtIbksKcl3Q @ 00:57:03].',
                                     'Stop hard-coding days: subtract the period-end dates in Excel to get '
                                     'the exact day count and anchor the cells so the formula copies '
                                     'cleanly down the sheet [Mergers & Inquisitions / Breaking Into Wall '
                                     'Street — rNjMWAOJHwM @ 00:05:07].']},
               'sop_steps': [{'step': 1,
                              'title': 'Pull the five rows and average them',
                              'action': 'Isolate sales, cost of goods sold, receivables, inventory, and '
                                        'payables, then average beginning and ending balances.',
                              'detail': 'InstructorTom hides every other row so only these five remain '
                                        'before calculating [InstructorTom — Ju1MGgf9RUw @ 00:00:00]; '
                                        'Mergers & Inquisitions averages receivables, inventory, and '
                                        'payables for each period before computing days [Mergers & '
                                        'Inquisitions / Breaking Into Wall Street — rNjMWAOJHwM @ '
                                        '00:04:19].'},
                             {'step': 2,
                              'title': 'Match every balance to its own flow',
                              'action': 'Compute collection days on credit sales, inventory days on cost '
                                        'of goods sold, and payment days on credit purchases.',
                              'detail': 'Compare net receivables with net credit sales per day, inventory '
                                        'cost with cost of goods sold per day, and payables with credit '
                                        'inventory purchases per day; a common denominator mixes different '
                                        'transactions [Understanding Accounting — OoegPOU-YCE @ '
                                        '00:16:45].'},
                             {'step': 3,
                              'title': 'Convert cycle days into dollars and interest',
                              'action': 'Multiply average daily cost of goods sold by cycle days, then '
                                        'apply your cost of debt.',
                              'detail': 'A 65-day cycle on this method equals $59 million of working '
                                        'capital, and at 7 percent it costs about $4 million a year in '
                                        'interest [InstructorTom — Ju1MGgf9RUw @ 00:03:03].'},
                             {'step': 4,
                              'title': 'Attack the worst lever and recheck in 90 days',
                              'action': 'Pick the weakest of the three components, brainstorm options, '
                                        'implement one or two, and remeasure after 90 days.',
                              'detail': 'Pick whichever component is worst and work terms with vendors and '
                                        'customers [Kurtis Hanni — 0WBeNhRVKHY @ 00:13:06]; then in 90 '
                                        'days report back, see what improved, and keep iterating toward a '
                                        '45-day or even negative cycle [Kurtis Hanni — 0WBeNhRVKHY @ '
                                        '00:13:42].'}]},
              {'heading': 'Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The sharpest split is over how hard to lean on suppliers. Laurence Gartside '
                              'states the textbook operator stance flat out: turn inventory fast, get paid '
                              'fast, and pay suppliers as late as possible, so long as no interest is '
                              'being charged on the delay [z3z_GomovEI @ 00:03:02]. InstructorTom models '
                              'the upside in a spreadsheet, showing that dragging feet to 80 payable days '
                              'instead of 50 pushes the equity value per share higher, then concedes that '
                              'if payable days grow too big the business will incur supplier penalties, '
                              'while paying fast enough can unlock supplier promotions [Ju1MGgf9RUw @ '
                              '00:05:58]. One Minute Finance attacks the stretch on pure cost: letting a 2 '
                              'percent discount for paying in 10 days lapse to hold cash 20 extra days on '
                              'a 30-day bill carries an annualized cost of 37.2 percent, and the channel '
                              'quotes the line that maximizing DPO is not inherently optimal because '
                              'delays can tighten future terms or threaten continuity of supply '
                              '[7yuWFm95LDw @ 00:07:11]. Invoice Finance News adds the reputational hit: a '
                              'big buyer that bullies smaller suppliers into long delays gets known as a '
                              'slow payer and can scare suppliers off, and the alternative it pitches is '
                              'an early payment scheme where a factoring company pays the supplier '
                              'immediately while the buyer still gets a longer period to settle '
                              '[Ooq0PnAEf5s @ 00:03:33].',
                              'Practitioners also split on whether the cycle moves valuation at all. '
                              'InstructorTom wires inventory, receivable, and payable days into a pro '
                              'forma model and argues an acquirer who can run the supply chain more '
                              'efficiently, cutting inventory days from 100 to 50, lifts the share price '
                              'from 28.85 to 30.63 [Ju1MGgf9RUw @ 00:05:39]. Mergers & Inquisitions pushes '
                              'back hard: the cycle is rarely used directly in financial models, Costco '
                              'trading near 1.2x revenue against roughly 0.7x for Target cannot plausibly '
                              'be explained by cash conversion numbers sitting under five days for both, '
                              'and the gap is driven by growth, margins, and competition instead, though '
                              'the channel concedes the metric earns its keep for startups, small '
                              'inventory businesses, and distressed companies heading for a cash crunch '
                              '[rNjMWAOJHwM @ 00:06:19]. The measurement itself is contested. LedgerGurus '
                              'computes payables days off cost of goods sold and receivables days off '
                              'total revenue [F-Y1cubdesE @ 00:02:09], while Understanding Accounting '
                              'insists payables be matched to credit purchases and receivables to credit '
                              'sales, showing the cost-of-goods proxy inflates payment days to 29.65 '
                              'versus 28 when inventory is growing, which makes the cycle look shorter '
                              'than it really is [GtIbksKcl3Q @ 01:06:52].',
                              'Whether a negative cycle is a realistic target splits the room. LedgerGurus '
                              'treats Dell and Costco as brilliant but very hard to pull off: Costco sells '
                              'inventory in as little as 10 days while paying on 30-day terms, and the '
                              'firm says it typically sees cycles of at least 90 days [F-Y1cubdesE @ '
                              '00:04:57]. Kurtis Hanni goes the other way and challenges owners to collect '
                              'before any outflow happens, calling that a business that can grow with no '
                              'stress beyond fulfilling the promise [0WBeNhRVKHY @ 00:14:05]. On the deal '
                              'side, the split is how to set the working capital peg. A Simple Model shows '
                              'a Texas pool float seller where a 12-month average of 4.4 million dollars '
                              'badly undershoots a June peak of 21.5 million, so the target lands between '
                              'the active-month average of 10.5 million and the peak-month average of '
                              'roughly 15 million, because a buyer with no adjustment would simply take '
                              'control in June [8qsUvwoLJHw @ 00:04:38]. Brent Freeman rejects a fixed '
                              'dollar target for growing or declining companies and tells buyers to '
                              'structure the adjustment off a working capital ratio, citing an 18- to '
                              '24-month average that closed at a negotiated 1.80 to one [KSfESWIcDGI @ '
                              '00:11:03].'],
               'table': {'caption': 'Competing playbooks on the cash conversion cycle and the working '
                                    'capital peg',
                         'headers': ['Dispute', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Supplier payment timing and how far to stretch',
                                   'Pay suppliers as late as possible whenever no interest is charged on '
                                   'the delay',
                                   'Capture early payment discounts because lapsing 2/10 net 30 costs 37.2 '
                                   'percent annualized',
                                   'Laurence Gartside ([z3z_GomovEI @ 00:03:02]); One Minute Finance '
                                   '([7yuWFm95LDw @ 00:07:28])'],
                                  ['Whether the cycle actually moves valuation',
                                   'Model inventory days cut from 100 to 50 lifting share price from 28.85 '
                                   'to 30.63',
                                   'Rarely used in models; Costco 1.2x versus Target 0.7x revenue is not '
                                   'explained by the cycle',
                                   'InstructorTom ([Ju1MGgf9RUw @ 00:05:39]); Mergers & Inquisitions / '
                                   'Breaking Into Wall Street ([rNjMWAOJHwM @ 00:06:19])'],
                                  ['Denominator for payables days calculation',
                                   'Average accounts payable divided by cost of goods sold times days in '
                                   'the period',
                                   'Match payables to credit purchases; the cost proxy overstates days at '
                                   '29.65 versus 28',
                                   'Kurtis Hanni ([0WBeNhRVKHY @ 00:05:40]); Understanding Accounting '
                                   '([GtIbksKcl3Q @ 01:06:52])'],
                                  ['Denominator for receivables days calculation',
                                   'Accounts receivable divided by total revenue times the 365-day period',
                                   'Use credit sales only, since cash sales never create receivables and '
                                   'shorten the result',
                                   'LedgerGurus: Ecommerce Accounting Experts ([F-Y1cubdesE @ 00:02:09]); '
                                   'WallStreetMojo ([Sw24t4Xzk0I @ 00:05:28])'],
                                  ['Chasing a negative cash conversion cycle',
                                   'Dell and Costco models are brilliant but very hard for small '
                                   'e-commerce sellers',
                                   'Challenge owners to collect customer money before any outflow ever '
                                   'happens',
                                   'LedgerGurus: Ecommerce Accounting Experts ([F-Y1cubdesE @ 00:04:57]); '
                                   'Kurtis Hanni ([0WBeNhRVKHY @ 00:14:05])'],
                                  ['Fixing slow customer collections and high DSO',
                                   'Use a factoring company that releases cash quickly back into the cycle',
                                   'Revamp order to cash with e-invoicing, automated reminders, and early '
                                   'payment discounts',
                                   'Invoice Finance News ([Ooq0PnAEf5s @ 00:03:33]); One Minute Finance '
                                   '([7yuWFm95LDw @ 00:06:04])'],
                                  ['Basis for the working capital peg in a sale',
                                   'Seasonal sellers peg between active-month and peak-month averages of '
                                   '10.5 to 15 million',
                                   'Use a working capital ratio instead of a dollar target when sales grow '
                                   'or decline',
                                   'A Simple Model ([8qsUvwoLJHw @ 00:04:38]); Brent Freeman  - The CBB '
                                   'Group ([KSfESWIcDGI @ 00:11:03])']]}},
              {'heading': 'Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ["The most expensive firsthand case comes from Kurtis Hanni's Bison CFO "
                              'engagement. The client was taking 200 days from ordering inventory to '
                              'selling it, 185 of them on a boat from overseas, with receivables stuck '
                              'above 30 days and zero payable days because the supplier demanded payment '
                              'at commitment [0WBeNhRVKHY @ 00:07:14]. That stacked into a 230-day cash '
                              'conversion cycle, roughly 11 months to get cash flow positive on a first '
                              'order, and 235,000 dollars paid out before a single dollar came back '
                              '[0WBeNhRVKHY @ 00:09:07]. The owner kept getting hit with tax payments and '
                              'felt like they were drowning inside a growing business that was eating all '
                              'its cash. The fix was a supplier conversation: a different route cut '
                              'shipping from 185 to 15 days, the new supplier did not demand payment until '
                              'goods landed in the warehouse, and follow-up systems pulled receivables '
                              'from about 35 days to 20 over six months, landing the cycle at 45 days and '
                              'the cash requirement at 67,000 dollars [0WBeNhRVKHY @ 00:11:29]. '
                              'LedgerGurus reports the same trap across its client base, regularly seeing '
                              'brands holding 180 to 240 days of inventory and warning that accrual books '
                              'can show profits while the cash sits somewhere between the factory and the '
                              'customer [F-Y1cubdesE @ 00:05:12].',
                              'Growth itself is the trap several practitioners keep hitting. LedgerGurus '
                              'watches owners sign a big wholesaler on net 60 terms, book a huge purchase '
                              'order as revenue, and then sit without the cash while also pre-building a '
                              'pile of inventory to push into that channel [F-Y1cubdesE @ 00:06:05]. A '
                              "Simple Model's pool float seller made 10 million dollars of profit yet "
                              'nearly ran out of cash funding inventory and receivables ahead of summer, '
                              'and states that had sales spiked more abruptly the 15 million dollar '
                              'starting balance would have been insufficient, because strong growth can '
                              'bankrupt a company with positive net working capital [8qsUvwoLJHw @ '
                              '00:01:47]. Understanding Accounting flags how the ratios themselves '
                              'mislead: a bigger allowance for credit losses shortens computed collection '
                              'days without any customer paying faster, beginning-and-ending averages can '
                              'miss a seasonal peak entirely, and payroll, rent, debt service, and taxes '
                              'sit outside the cycle [GtIbksKcl3Q @ 00:57:03]. InstructorTom puts a price '
                              'on carrying a long cycle: 65 days of average daily spend works out to 59 '
                              'million dollars of working capital, and at a 7 percent cost of debt that is '
                              '4 million dollars a year in interest alone, before counting what else that '
                              'capital could have done [Ju1MGgf9RUw @ 00:03:50].',
                              'In a business sale, the working capital line is where sellers lose money '
                              'after the price is agreed. Enterprise Industry Network says sellers get '
                              'into trouble when they assume all cash stays with them or underestimate '
                              'normal operating needs, with aggressive collections timing, delayed '
                              'payables, and inventory swings as the usual culprits, and warns that '
                              'waiting until late-stage diligence leaves the seller negotiating from a '
                              'weaker position [axmEedpIF1E @ 00:01:40]. Brent Freeman shows the mechanics '
                              'bite dollar for dollar: against a 5 million dollar target, a closing '
                              'balance of 4.9 million cuts the 2 million dollar seller note by 100,000 '
                              'dollars, while a seller who leaves a 3 to 1 ratio of excess capital in the '
                              'company invites the buyer to negotiate keeping it [KSfESWIcDGI @ 00:08:36]. '
                              'The countermove taught for sellers is to pull excess capital out, lend it '
                              'back from a separate entity with a UCC filing, and recast the balance sheet '
                              'near a 1.5 to 1.7 ratio. On the buy side, a buyer who takes over '
                              'insufficient working capital ends up injecting cash on top of the purchase '
                              'price. A Simple Model adds the exclusion fight: buyers commonly strip '
                              'receivables aged 90 days or more, cutting a 10 million dollar balance to '
                              '8.3 million in its example, and refuse to pay for obsolete inventory or '
                              "payables that are the seller's obligation [DbHq5BHo_XA @ 00:02:38]."],
               'table': {'caption': 'Firsthand cash traps, the numbers behind them, and the corrections '
                                    'practitioners applied',
                         'headers': ['Failure Mode',
                                     'Firsthand Numbers',
                                     'Correction Taught',
                                     'Expert Source'],
                         'rows': [['Overseas inventory with 185-day shipping and zero payable days',
                                   '230-day cycle and 235,000 dollars paid out before the first dollar '
                                   'came back',
                                   'New supplier route, 15-day shipping, pay on arrival, cycle cut to 45 '
                                   'days',
                                   'Kurtis Hanni ([0WBeNhRVKHY @ 00:09:07])'],
                                  ['Adding a wholesale channel on net 60 terms',
                                   'Revenue booked on a huge purchase order while cash and extra inventory '
                                   'stay locked',
                                   'Negotiate supplier terms, clear inventory that is not selling, tighten '
                                   'reorder points',
                                   'LedgerGurus: Ecommerce Accounting Experts ([F-Y1cubdesE @ 00:06:05])'],
                                  ['Seasonal ramp funding inventory ahead of summer sales',
                                   '10 million dollars of profit yet nearly ran out of a 15 million dollar '
                                   'starting balance',
                                   'Size liquidity and the peg off active-month and peak-month averages, '
                                   'not twelve months',
                                   'A Simple Model ([8qsUvwoLJHw @ 00:01:47])'],
                                  ['Ignoring the carrying cost of a long cycle',
                                   '59 million dollars of working capital at 7 percent costs 4 million '
                                   'dollars every year',
                                   'Convert cycle days into dollars of daily spend, then price each supply '
                                   'chain improvement',
                                   'InstructorTom ([Ju1MGgf9RUw @ 00:03:50])'],
                                  ['Cycle drifting upward at a distressed or growing company',
                                   'Cycle rising from 25 to 63 days left cash from operations at 59 versus '
                                   '75',
                                   'Track the cycle trend to flag when a loan or capital raise is coming',
                                   'Mergers & Inquisitions / Breaking Into Wall Street ([rNjMWAOJHwM @ '
                                   '00:09:07])'],
                                  ['Closing short of the agreed working capital target',
                                   '4.9 million against a 5 million target cut the seller note by 100,000 '
                                   'dollars',
                                   'Calculate the 12- to 24-month average early and strip excess capital '
                                   'before market',
                                   'Brent Freeman  - The CBB Group ([KSfESWIcDGI @ 00:08:36])'],
                                  ['Celebrating a shorter cycle without checking the cause',
                                   'Fewer inventory days may mean stockouts and more payment days may mean '
                                   'overdue bills',
                                   'Inspect customer terms, inventory availability, and supplier payment '
                                   'records before judging',
                                   'Understanding Accounting ([OoegPOU-YCE @ 00:28:29])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Cash Gates Before You Order, Expand, or Sell',
                           'body': 'Every item below is a trap a practitioner either lived through with a '
                                   'client or priced out in a model. Clear each gate before committing '
                                   'cash to inventory, a new channel, or a closing balance sheet.',
                           'items': ['Before signing net 60 wholesale terms, model the receivables jump '
                                     'and the extra inventory build the channel demands [LedgerGurus: '
                                     'Ecommerce Accounting Experts — F-Y1cubdesE @ 00:06:24].',
                                     'Do not place an overseas order with zero payable days until cash '
                                     'covers the full cycle; the 230-day client needed 235,000 dollars out '
                                     'before a dollar returned [Kurtis Hanni — 0WBeNhRVKHY @ 00:09:32].',
                                     'Never let a 2 percent 10-day discount lapse just to hold cash 20 '
                                     'more days, because the annualized cost runs 37.2 percent [One Minute '
                                     'Finance — 7yuWFm95LDw @ 00:07:28].',
                                     'Before going to market, compute the 12- to 24-month average working '
                                     'capital and pull excess capital out, or the buyer negotiates to keep '
                                     'it [Brent Freeman  - The CBB Group — KSfESWIcDGI @ 00:09:41].']}}],
 'pull_quote': "Businesses don't always fail because they're unprofitable, but they definitely fail "
               "because they don't have enough cash. — LedgerGurus: Ecommerce Accounting Experts "
               '(F-Y1cubdesE @ 00:07:52).',
 'diagram_id': 'diag-05',
 'action_checklist': ['Calculate your cash conversion cycle from income statement and balance sheet '
                      'averages, then chart it across the last one to three years to catch shifts before '
                      'you feel them (Kurtis Hanni, 0WBeNhRVKHY @ 00:12:48).',
                      'Pick the worst of inventory, receivable, and payable days, brainstorm term changes '
                      'with vendors and customers, and report back on the result in 90 days (Kurtis Hanni, '
                      '0WBeNhRVKHY @ 00:13:26).',
                      'Negotiate better supplier terms, including accepting a slightly higher unit price '
                      'in exchange for payment terms that shorten the cycle (LedgerGurus: Ecommerce '
                      'Accounting Experts, F-Y1cubdesE @ 00:06:37).',
                      'Clear inventory that is not selling and tighten reorder points to free cash without '
                      'adding ad channels or sales channels (LedgerGurus: Ecommerce Accounting Experts, '
                      'F-Y1cubdesE @ 00:06:56).',
                      'Convert cycle days into dollars by multiplying average daily cost of goods sold by '
                      'the cycle, then apply your cost of debt to price the carry (InstructorTom, '
                      'Ju1MGgf9RUw @ 00:03:03).',
                      'Cut receivables days with e-invoicing, automated payment reminders, and strategic '
                      'early payment discounts aimed at past-due accounts (One Minute Finance, 7yuWFm95LDw '
                      '@ 00:06:04).'],
 'statutory_citations': [{'title': 'Kurtis Hanni — You’re Not Broke, Your Cash Is Just Stuck (Cash '
                                   'Conversion Cycle Explained) [00:08:45]',
                          'url': 'https://www.youtube.com/watch?v=0WBeNhRVKHY&t=525s',
                          'relevance': 'Primary practitioner testimony on a 230-day client cycle cut to 45 '
                                       'days and the cash outlay it required.'},
                         {'title': 'LedgerGurus: Ecommerce Accounting Experts — Cash Conversion Cycle: The '
                                   'Metric EVERY Ecommerce Owner Should Understand [00:06:05]',
                          'url': 'https://www.youtube.com/watch?v=F-Y1cubdesE&t=365s',
                          'relevance': 'Primary practitioner testimony on wholesale net 60 terms trapping '
                                       'e-commerce cash.'},
                         {'title': 'A Simple Model — The Working Capital Peg for a Seasonal Business '
                                   '[00:01:47]',
                          'url': 'https://www.youtube.com/watch?v=8qsUvwoLJHw&t=107s',
                          'relevance': 'Primary practitioner testimony on seasonal growth nearly '
                                       'exhausting cash and setting a peak-based peg.'},
                         {'title': 'Brent Freeman  - The CBB Group — Working Capital Adjustment in a '
                                   'Business Sale. How it Can Change the Final Purchase Price! [00:08:36]',
                          'url': 'https://www.youtube.com/watch?v=KSfESWIcDGI&t=516s',
                          'relevance': 'Primary practitioner testimony on dollar-for-dollar seller note '
                                       'adjustments at closing.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'Ooq0PnAEf5s',
                       'title': 'What is the Cash Conversion Cycle?',
                       'channel': 'Invoice Finance News',
                       'author': 'Invoice Finance News',
                       'text': 'A company that has managed to negotiate payment terms with suppliers so '
                               'that they have a high DPO might create a low or even negative CCC score, '
                               'however that company might gain a reputation in its sector for being slow '
                               'payers, thus causing reputational damage.',
                       'tip': 'A company that has managed to negotiate payment terms with suppliers so '
                              'that they have a high DPO might create a low or even negative CCC score, '
                              'however that company might gain a reputation in its sector for being slow '
                              'payers, thus causing reputational damage.',
                       'timestamp': 142,
                       'timestamp_seconds': 142,
                       'timestamp_label': '[00:02:22]',
                       'url': 'https://www.youtube.com/watch?v=Ooq0PnAEf5s&t=142s',
                       'markdown': '[00:02:22](https://www.youtube.com/watch?v=Ooq0PnAEf5s&t=142s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Ju1MGgf9RUw',
                       'title': 'Video   Cash Conversion Cycle',
                       'channel': 'InstructorTom',
                       'author': 'InstructorTom',
                       'text': "If I'm carrying an average balance of fifty nine million dollars at an "
                               "annual cost of seven percent, it's gonna cost me four million dollars a "
                               'year just to pay the interest on that working capital.',
                       'tip': "If I'm carrying an average balance of fifty nine million dollars at an "
                              "annual cost of seven percent, it's gonna cost me four million dollars a "
                              'year just to pay the interest on that working capital.',
                       'timestamp': 230,
                       'timestamp_seconds': 230,
                       'timestamp_label': '[00:03:50]',
                       'url': 'https://www.youtube.com/watch?v=Ju1MGgf9RUw&t=230s',
                       'markdown': '[00:03:50](https://www.youtube.com/watch?v=Ju1MGgf9RUw&t=230s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'OoegPOU-YCE',
                       'title': 'Inventory Estimates and the Cash Conversion Cycle | ACC 300 Lecture 20',
                       'channel': 'Understanding Accounting',
                       'author': 'Understanding Accounting',
                       'text': 'Faster collection may reflect tighter customer credit. Fewer inventory '
                               'days may reflect faster sales or stockouts. More payment days may reflect '
                               'longer agreed terms or overdue bills.',
                       'tip': 'Faster collection may reflect tighter customer credit. Fewer inventory days '
                              'may reflect faster sales or stockouts. More payment days may reflect longer '
                              'agreed terms or overdue bills.',
                       'timestamp': 1709,
                       'timestamp_seconds': 1709,
                       'timestamp_label': '[00:28:29]',
                       'url': 'https://www.youtube.com/watch?v=OoegPOU-YCE&t=1709s',
                       'markdown': '[00:28:29](https://www.youtube.com/watch?v=OoegPOU-YCE&t=1709s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'z3z_GomovEI',
                       'title': 'The Cash Conversion Cycle formula and how to use it',
                       'channel': 'Laurence Gartside',
                       'author': 'Laurence Gartside',
                       'text': 'For a better shorter cash conversion cycle we want to turn over inventory '
                               'quickly, have few credit sales, get paid quickly and pay our suppliers as '
                               "late as possible, assuming we're not paying interest.",
                       'tip': 'For a better shorter cash conversion cycle we want to turn over inventory '
                              'quickly, have few credit sales, get paid quickly and pay our suppliers as '
                              "late as possible, assuming we're not paying interest.",
                       'timestamp': 182,
                       'timestamp_seconds': 182,
                       'timestamp_label': '[00:03:02]',
                       'url': 'https://www.youtube.com/watch?v=z3z_GomovEI&t=182s',
                       'markdown': '[00:03:02](https://www.youtube.com/watch?v=z3z_GomovEI&t=182s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'GtIbksKcl3Q',
                       'title': 'Inventory Estimates and the Cash Conversion Cycle | ACC 300 Chapter 18 '
                                'Reading',
                       'channel': 'Understanding Accounting',
                       'author': 'Understanding Accounting',
                       'text': 'Using cost of goods sold as a proxy would instead produce 29.65 days. '
                               'Inventory increased, so cost of goods sold is smaller than purchases here. '
                               'The smaller denominator overstates payment days and makes the calculated '
                               'cash conversion cycle shorter.',
                       'tip': 'Using cost of goods sold as a proxy would instead produce 29.65 days. '
                              'Inventory increased, so cost of goods sold is smaller than purchases here. '
                              'The smaller denominator overstates payment days and makes the calculated '
                              'cash conversion cycle shorter.',
                       'timestamp': 4012,
                       'timestamp_seconds': 4012,
                       'timestamp_label': '[01:06:52]',
                       'url': 'https://www.youtube.com/watch?v=GtIbksKcl3Q&t=4012s',
                       'markdown': '[01:06:52](https://www.youtube.com/watch?v=GtIbksKcl3Q&t=4012s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '7yuWFm95LDw',
                       'title': 'The Cash Conversion Cycle (CCC) Explained | Formula, Working Capital & '
                                'Cash Flow Mastery',
                       'channel': 'One Minute Finance',
                       'author': 'One Minute Finance',
                       'text': 'If you let that discount lapse just so you can hold onto your cash for 20 '
                               'extra days, the annualized cost of that decision is a staggering 37.2%.',
                       'tip': 'If you let that discount lapse just so you can hold onto your cash for 20 '
                              'extra days, the annualized cost of that decision is a staggering 37.2%.',
                       'timestamp': 448,
                       'timestamp_seconds': 448,
                       'timestamp_label': '[00:07:28]',
                       'url': 'https://www.youtube.com/watch?v=7yuWFm95LDw&t=448s',
                       'markdown': '[00:07:28](https://www.youtube.com/watch?v=7yuWFm95LDw&t=448s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'F-Y1cubdesE',
                       'title': 'Cash Conversion Cycle: The Metric EVERY Ecommerce Owner Should Understand',
                       'channel': 'LedgerGurus: Ecommerce Accounting Experts',
                       'author': 'LedgerGurus: Ecommerce Accounting Experts',
                       'text': "Businesses don't always fail because they're unprofitable, but they "
                               "definitely fail because they don't have enough cash.",
                       'tip': "Businesses don't always fail because they're unprofitable, but they "
                              "definitely fail because they don't have enough cash.",
                       'timestamp': 472,
                       'timestamp_seconds': 472,
                       'timestamp_label': '[00:07:52]',
                       'url': 'https://www.youtube.com/watch?v=F-Y1cubdesE&t=472s',
                       'markdown': '[00:07:52](https://www.youtube.com/watch?v=F-Y1cubdesE&t=472s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'F-Y1cubdesE',
                       'title': 'Cash Conversion Cycle: The Metric EVERY Ecommerce Owner Should Understand',
                       'channel': 'LedgerGurus: Ecommerce Accounting Experts',
                       'author': 'LedgerGurus: Ecommerce Accounting Experts',
                       'text': 'They sign a new relationship with a big wholesaler, they have net 60 day '
                               'terms, and the days sales outstanding can grow tremendously; you can show '
                               "revenue on the books, but you don't have the cash from selling that "
                               'inventory.',
                       'tip': 'They sign a new relationship with a big wholesaler, they have net 60 day '
                              'terms, and the days sales outstanding can grow tremendously; you can show '
                              "revenue on the books, but you don't have the cash from selling that "
                              'inventory.',
                       'timestamp': 365,
                       'timestamp_seconds': 365,
                       'timestamp_label': '[00:06:05]',
                       'url': 'https://www.youtube.com/watch?v=F-Y1cubdesE&t=365s',
                       'markdown': '[00:06:05](https://www.youtube.com/watch?v=F-Y1cubdesE&t=365s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Sw24t4Xzk0I',
                       'title': 'Cash Conversion Cycle - Meaning, Formula, Calculation & Interpretations',
                       'channel': 'WallStreetMojo',
                       'author': 'WallStreetMojo',
                       'text': 'Other examples where negative cash conversion cycle could be like Amazon; '
                               "if you look at Amazon's cash conversion cycle, it's around minus 24, 25 "
                               'days.',
                       'tip': 'Other examples where negative cash conversion cycle could be like Amazon; '
                              "if you look at Amazon's cash conversion cycle, it's around minus 24, 25 "
                              'days.',
                       'timestamp': 952,
                       'timestamp_seconds': 952,
                       'timestamp_label': '[00:15:52]',
                       'url': 'https://www.youtube.com/watch?v=Sw24t4Xzk0I&t=952s',
                       'markdown': '[00:15:52](https://www.youtube.com/watch?v=Sw24t4Xzk0I&t=952s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'C5Ut79jWwHA',
                       'title': 'What is the Cash Conversion Cycle?',
                       'channel': 'Marketing Business Network',
                       'author': 'Marketing Business Network',
                       'text': 'Longer supplier terms can also help, if the supplier agrees to them. '
                               'Simply paying late is different from negotiating more time. Missed '
                               'deadlines may damage relationships or bring charges.',
                       'tip': 'Longer supplier terms can also help, if the supplier agrees to them. Simply '
                              'paying late is different from negotiating more time. Missed deadlines may '
                              'damage relationships or bring charges.',
                       'timestamp': 115,
                       'timestamp_seconds': 115,
                       'timestamp_label': '[00:01:55]',
                       'url': 'https://www.youtube.com/watch?v=C5Ut79jWwHA&t=115s',
                       'markdown': '[00:01:55](https://www.youtube.com/watch?v=C5Ut79jWwHA&t=115s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '0WBeNhRVKHY',
                       'title': 'You’re Not Broke, Your Cash Is Just Stuck (Cash Conversion Cycle '
                                'Explained)',
                       'channel': 'Kurtis Hanni',
                       'author': 'Kurtis Hanni',
                       'text': 'They were able to take their cash conversion cycle from 230 days to 45 '
                               'days, which meant that their cash positive happened in month two, meaning '
                               'they can start investing that money back in inventory.',
                       'tip': 'They were able to take their cash conversion cycle from 230 days to 45 '
                              'days, which meant that their cash positive happened in month two, meaning '
                              'they can start investing that money back in inventory.',
                       'timestamp': 689,
                       'timestamp_seconds': 689,
                       'timestamp_label': '[00:11:29]',
                       'url': 'https://www.youtube.com/watch?v=0WBeNhRVKHY&t=689s',
                       'markdown': '[00:11:29](https://www.youtube.com/watch?v=0WBeNhRVKHY&t=689s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '1gBvyu9ADGo',
                       'title': 'Cash Conversion Cycle Explained | CFA Level 1 Corporate Issuers',
                       'channel': 'Luke Kermode, CFA',
                       'author': 'Luke Kermode, CFA',
                       'text': 'A short cash conversion cycle is seen as a positive sign for a company and '
                               'it indicates that the company is converting its cash investment in '
                               'inventory into cash inflow from sales quickly and is operating '
                               'efficiently.',
                       'tip': 'A short cash conversion cycle is seen as a positive sign for a company and '
                              'it indicates that the company is converting its cash investment in '
                              'inventory into cash inflow from sales quickly and is operating efficiently.',
                       'timestamp': 433,
                       'timestamp_seconds': 433,
                       'timestamp_label': '[00:07:13]',
                       'url': 'https://www.youtube.com/watch?v=1gBvyu9ADGo&t=433s',
                       'markdown': '[00:07:13](https://www.youtube.com/watch?v=1gBvyu9ADGo&t=433s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'rNjMWAOJHwM',
                       'title': 'The Cash Conversion Cycle (CCC): The King of the Cash Flow Statement?',
                       'channel': 'Mergers & Inquisitions / Breaking Into Wall Street',
                       'author': 'Mergers & Inquisitions / Breaking Into Wall Street',
                       'text': 'These companies often find it harder to collect from customers and they '
                               'may sometimes get squeezed by suppliers who impose tougher payment terms '
                               'because of the financial state of the companies.',
                       'tip': 'These companies often find it harder to collect from customers and they may '
                              'sometimes get squeezed by suppliers who impose tougher payment terms '
                              'because of the financial state of the companies.',
                       'timestamp': 532,
                       'timestamp_seconds': 532,
                       'timestamp_label': '[00:08:52]',
                       'url': 'https://www.youtube.com/watch?v=rNjMWAOJHwM&t=532s',
                       'markdown': '[00:08:52](https://www.youtube.com/watch?v=rNjMWAOJHwM&t=532s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'DbHq5BHo_XA',
                       'title': 'The Definition of Working Capital in the Working Capital Peg',
                       'channel': 'A Simple Model',
                       'author': 'A Simple Model',
                       'text': 'A buyer may want to omit all accounts receivable balances aged 90 days or '
                               'more to avoid the risk that those customers do not end up paying, because '
                               "that's cash that the buyer may not receive once the transaction closes, so "
                               'why pay for it.',
                       'tip': 'A buyer may want to omit all accounts receivable balances aged 90 days or '
                              'more to avoid the risk that those customers do not end up paying, because '
                              "that's cash that the buyer may not receive once the transaction closes, so "
                              'why pay for it.',
                       'timestamp': 127,
                       'timestamp_seconds': 127,
                       'timestamp_label': '[00:02:07]',
                       'url': 'https://www.youtube.com/watch?v=DbHq5BHo_XA&t=127s',
                       'markdown': '[00:02:07](https://www.youtube.com/watch?v=DbHq5BHo_XA&t=127s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'axmEedpIF1E',
                       'title': 'Working Capital Adjustments in a Business Sale | EIN Business Brokers | '
                                'Enterprise Industry Network',
                       'channel': 'Enterprise Industry Network',
                       'author': 'Enterprise Industry Network',
                       'text': 'If you wait until late stage diligence to understand working capital, you '
                               'are already negotiating from a weaker position.',
                       'tip': 'If you wait until late stage diligence to understand working capital, you '
                              'are already negotiating from a weaker position.',
                       'timestamp': 141,
                       'timestamp_seconds': 141,
                       'timestamp_label': '[00:02:21]',
                       'url': 'https://www.youtube.com/watch?v=axmEedpIF1E&t=141s',
                       'markdown': '[00:02:21](https://www.youtube.com/watch?v=axmEedpIF1E&t=141s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '8qsUvwoLJHw',
                       'title': 'The Working Capital Peg for a Seasonal Business',
                       'channel': 'A Simple Model',
                       'author': 'A Simple Model',
                       'text': 'Had sales spiked more abruptly, the 15 million cash balance that the '
                               "company started the season with would have been insufficient; it's a "
                               'little counterintuitive, but strong growth can bankrupt a company with '
                               'positive net working capital.',
                       'tip': 'Had sales spiked more abruptly, the 15 million cash balance that the '
                              "company started the season with would have been insufficient; it's a little "
                              'counterintuitive, but strong growth can bankrupt a company with positive '
                              'net working capital.',
                       'timestamp': 107,
                       'timestamp_seconds': 107,
                       'timestamp_label': '[00:01:47]',
                       'url': 'https://www.youtube.com/watch?v=8qsUvwoLJHw&t=107s',
                       'markdown': '[00:01:47](https://www.youtube.com/watch?v=8qsUvwoLJHw&t=107s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'KSfESWIcDGI',
                       'title': 'Working Capital Adjustment in a Business Sale. How it Can Change the '
                                'Final Purchase Price!',
                       'channel': 'Brent Freeman  - The CBB Group',
                       'author': 'Brent Freeman  - The CBB Group',
                       'text': "If you purchase a business with insufficient working capital, you're going "
                               'to end up injecting cash on top of your purchase price to satisfy that '
                               'requirement and keep the business running.',
                       'tip': "If you purchase a business with insufficient working capital, you're going "
                              'to end up injecting cash on top of your purchase price to satisfy that '
                              'requirement and keep the business running.',
                       'timestamp': 362,
                       'timestamp_seconds': 362,
                       'timestamp_label': '[00:06:02]',
                       'url': 'https://www.youtube.com/watch?v=KSfESWIcDGI&t=362s',
                       'markdown': '[00:06:02](https://www.youtube.com/watch?v=KSfESWIcDGI&t=362s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'}]}
