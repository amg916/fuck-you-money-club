from __future__ import annotations

CHAPTER_3 = {'id': 'Q3',
 'chapter_id': 'Q3',
 'chapter_number': 3,
 'question_number': 3,
 'slug': 'unit-economics-and-contribution-margin',
 'question_prompt': 'How much profit does each order really make after product, fulfillment, payment, and '
                    'ad costs, and how should those numbers guide decisions?',
 'kicker': 'Q3 / THE BIG MONEY PLAYBOOKS',
 'title': 'Unit Economics and Contribution Margin',
 'subtitle': 'Gross vs. contribution margin, CM1–CM3 and where marketing costs sit (OPEX vs. CM3), '
             'contribution-margin-to-CAC ratios, lifecycle benchmarks from idea to exit, tracking and '
             'reporting CM, and the 50%-off vs. BOGO case that lost $500K',
 'layout_template': 'financial_analysis',
 'reading_time_minutes': 15,
 'executive_summary': 'Accountants, agency operators and finance coaches converge on one spine: '
                      'contribution margin is net revenue minus every cost that moves with an order, '
                      'including product, fulfillment, payment fees and, for most, marketing, and it caps '
                      'both operating margin and the CAC you can afford. Eric Andrews targets a '
                      'contribution-margin-to-CAC ratio above 1 and break-even or better on the first '
                      'order; Common Thread Collective turns $53 of fuel profit minus a $20 net target '
                      'into a $33 target CAC; Mark Builds Brands targets 60 percent gross margin and a 1.3 '
                      'break-even ROAS. Street-tested levers include two-for-one offers instead of 50 '
                      'percent off and pushing ad spend into the highest-margin SKU. Disagreements center '
                      'on whether marketing belongs inside contribution margin, how to classify agency and '
                      'creative fees, and whether to scale on lifetime value.',
 'key_metrics': [{'label': 'Contribution Margin to CAC Ratio Target',
                  'metric': 'Contribution Margin to CAC Ratio Target',
                  'value': 'Better than 1.0 on the first order (1.5 in the idea-phase plan, 2.1 at late '
                           'stage in the optimal scenario)',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Eric Andrews' lifecycle benchmarks for an apparel brand moving from idea to "
                             'late stage, where the optimal business always breaks even or better on the '
                             'first order',
                  'source': 'Eric Andrews ([gG33a-ErNRQ @ 00:13:30])'},
                 {'label': 'Break-Even Revenue Point',
                  'metric': 'Break-Even Revenue Point',
                  'value': '$1,000,000 ($300,000 fixed costs divided by a 30% contribution margin ratio)',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Stephen's worked example of using the contribution margin ratio and fixed "
                             'costs to find the revenue at which profit starts',
                  'source': 'LedgerGurus: Ecommerce Accounting Experts ([e5r7-KT6mQ0 @ 00:02:28])'},
                 {'label': 'Target Gross Margin and Break-Even ROAS',
                  'metric': 'Target Gross Margin and Break-Even ROAS',
                  'value': '60% gross margin KPI; 1.3 personal break-even ROAS target (1.84 called tough '
                           'to scale)',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Mark's unit economics calculator KPIs for scaling a new product on paid ads",
                  'source': 'Mark Builds Brands Highlights ([eTADhJ3N_oo @ 00:03:21])'},
                 {'label': 'BOGO vs 50% Off Contribution Margin',
                  'metric': 'BOGO vs 50% Off Contribution Margin',
                  'value': '$69 vs $29 contribution margin per order; $36 contribution margin after CAC on '
                           'two-for-one',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Black Friday case study of a brand that lost $500,000 running 50% off '
                             'sitewide, re-run as a two-for-one offer',
                  'source': 'Eric Andrews ([t2H3gJHuw6k @ 00:08:56])'}],
 'sections': [{'heading': '1. The Practitioner Consensus: Contribution Margin Is the Ceiling on Everything',
               'paragraphs': ['Every operator here builds the same spine: contribution margin is what '
                              'survives after the costs that move with each order. Stephen at LedgerGurus '
                              'defines it as revenue minus variable costs, with COGS, fulfillment and '
                              'shipping, payment processor fees and advertising sitting on the variable '
                              'side, while payroll, software, rent and non-advertising marketing sit in '
                              'fixed [e5r7-KT6mQ0 @ 00:01:14]. Abir, a DTC accountant, frames it '
                              'identically as the money left over after variable expenses that then covers '
                              'fixed expenses, and walks a pogo-stick store from $100,000 revenue down to '
                              '$33,000 of contribution margin after discounts, product, shipping, merchant '
                              'fees and $30,000 of ads [lrF2Uey1-uU @ 00:03:43]. Common Thread Collective '
                              'defines it as net revenue minus payment processor fee, pick-pack, '
                              'fulfillment, cost of goods and ad spend [b4ddPmPdQcY @ 00:00:00], and Chan '
                              'at Bloom Analytics spells out the formula as net revenue minus variable '
                              'costs minus marketing costs, with net revenue meaning sales after discounts '
                              'and refunds [mWL3C_COYk8 @ 00:00:36]. Both accountants add a reality check: '
                              'costs are rarely perfectly fixed or variable, and fixed costs climb in step '
                              "functions as the business grows. Stephen's hard rule follows directly: "
                              'operating margin can never exceed contribution margin, and a contribution '
                              'margin at or below zero means a broken business that must raise prices or '
                              'cut costs fast.',
                              'The second point of agreement is that margin must be split into layers '
                              'instead of one blended COGS bucket. Eric Andrews defines gross margin as '
                              'revenue minus product cost, so a $100 item that costs $20 to make and land '
                              'in the warehouse runs about 80 percent; contribution margin then also backs '
                              "out fulfillment to the customer's door, and post-marketing contribution "
                              'margin, the lowest layer, asks whether you made money after all marketing '
                              '[Zh6xNyWZVs4 @ 00:01:10]. Valentin Kuznetcov runs the same ladder with '
                              'numbered labels: product profit is CM1, gross profit after cost of delivery '
                              'is CM2, and profit contribution after the costs that incur revenue is CM3, '
                              'with everything below that treated as OPEX [LmlQ8JEPflQ @ 00:04:57]. Chan '
                              'at Bloom turns the ladder into a waterfall on a $10,000 month: $3,500 '
                              'product leaves 65 percent, $1,500 fulfillment leaves 50 percent, $2,000 '
                              'marketing leaves a 30 percent contribution margin [mWL3C_COYk8 @ 00:02:33]. '
                              "Chan's diagnostic: a weak first layer is a pricing or sourcing problem ads "
                              'will not fix, a big fulfillment bite points to a low free-shipping '
                              'threshold or heavy cheap products, and a healthy gross profit with a thin '
                              'contribution margin means acquisition cost is the problem [mWL3C_COYk8 @ '
                              '00:03:14].',
                              'The third consensus is that contribution margin per order is the ceiling on '
                              'what you can pay to acquire a customer. Eric Andrews shows $64 of '
                              'contribution margin per unit against a $42 CAC, a '
                              'contribution-margin-to-CAC ratio of about 1.5, and argues that being '
                              'profitable on the first order makes every repeat order close to pure profit '
                              'because little or no marketing attaches to it [LKEn47f67vQ @ 00:01:31]. In '
                              'his lifecycle benchmarks the goal of most businesses is at the very least '
                              'break-even on the first order, with the exception being brands whose '
                              'customers buy five, ten or fifteen times [gG33a-ErNRQ @ 00:04:53]. Common '
                              'Thread Collective calls the same number fuel profit: with 53 points of '
                              'margin left on a $100 boot, you could spend up to $52 to acquire a customer '
                              "and still net one dollar [gCo34Jl1RkQ @ 00:07:25]. Patrick O'Driscoll of "
                              'TVG lands in the same place from the agency side, saying most smaller '
                              'brands are better off keeping new customer acquisition cost below AOV from '
                              'day one and not scaling spend until contribution margin is healthy, even '
                              'though the fastest scaling happens on lifetime value [vI_Np8RQikw @ '
                              '00:12:23]. The shared rule: know the per-order margin before you touch the '
                              'ad budget.'],
               'table': {'caption': 'Where the practitioners agree on contribution margin fundamentals',
                         'headers': ['Consensus Principle',
                                     'Operator Detail From the Speaker',
                                     'Expert Source'],
                         'rows': [['Contribution margin equals revenue minus every variable cost tied to '
                                   'each order',
                                   'COGS, fulfillment and shipping, payment processor fees and advertising '
                                   'all sit on the variable side',
                                   'LedgerGurus: Ecommerce Accounting Experts ([e5r7-KT6mQ0 @ 00:00:26])'],
                                  ['Operating margin can never exceed the contribution margin ratio of the '
                                   'business',
                                   'A 30 percent contribution margin caps operating margin at 30 percent, '
                                   'and zero or below means a broken business',
                                   'LedgerGurus: Ecommerce Accounting Experts ([e5r7-KT6mQ0 @ 00:02:00])'],
                                  ['Break gross margin, contribution margin and post-marketing margin into '
                                   'separate layers',
                                   'Product cost and fulfillment are backed out separately so each one can '
                                   'be evaluated independently',
                                   'Eric Andrews Clips ([Zh6xNyWZVs4 @ 00:01:29])'],
                                  ['Contribution margin per order sets the hard ceiling on customer '
                                   'acquisition cost',
                                   'With $83 of contribution margin on a $175 order, CAC should be $83 or '
                                   'less',
                                   'Eric Andrews ([gG33a-ErNRQ @ 00:06:53])'],
                                  ['Aim to break even or better on the very first customer order',
                                   'Many customers buy only once, so first-order economics must work '
                                   'unless lifetime orders run very high',
                                   'Eric Andrews ([gG33a-ErNRQ @ 00:04:16])'],
                                  ['Track unit economics by SKU instead of treating every product as '
                                   'identical',
                                   'Treating every SKU as producing the same net outcome is one of the '
                                   'number one drainers of money',
                                   'Common Thread Collective ([gCo34Jl1RkQ @ 00:08:57])'],
                                  ['Do not scale ad spend until contribution margin is in a healthy spot',
                                   'First levers are raising prices, cutting cost of goods via suppliers '
                                   'or shipping, and lowering acquisition costs',
                                   "Patrick O'Driscoll | E-Commerce Growth Marketer ([vI_Np8RQikw @ "
                                   '00:11:11])']]}},
              {'heading': '2. Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['Eric Andrews builds per-order unit economics with plain division: total '
                              'revenue over total orders gives a $232 AOV, product COGS over orders gives '
                              '$62, fulfillment over orders gives $71, leaving $99 of contribution margin '
                              'per order; when months bounce around he runs a trailing average, which '
                              'lands at $238, $64, $74 and roughly $100 [tj2W9oEqeQo @ 00:00:56]. In his '
                              'fuller case study, gross revenue takes product sales and taxes collected, '
                              'then discounts and returns come out and shipping income goes back in to '
                              'reach net revenue, about $134 per order [8xfPvprL5qE @ 00:07:34]. COGS '
                              'covers product cost, import freight, duties and taxes at 29 and 27 percent '
                              'of revenue; fulfillment covers pick and pack, packing materials, other 3PL '
                              'charges, shipping to customer and merchant fees, about $31 and $35 per '
                              'order, leaving $64 of contribution margin, a little under 50 percent '
                              '[8xfPvprL5qE @ 00:10:18]. Marketing then eats 31 to 36 percent of revenue, '
                              '$42 and $48 per order, so post-marketing contribution is only $22 and $12; '
                              'opex of about $8 per order leaves operating income around 11 and 5 percent. '
                              'Matt Byrne of Day One Advisory warns that once multiple stock orders carry '
                              'different landed costs per unit, tracking in Excel becomes death by '
                              'spreadsheet, so landed cost belongs in an inventory system [sR1NjOCbwOA @ '
                              '00:09:49].',
                              "Common Thread Collective's fuel-profit math is the cleanest street build. "
                              'Start at a $100 retail price, subtract $20 paid to the manufacturer, about '
                              '$1 per unit for the 3PL to break bulk and shelve, roughly $2 in payment '
                              'processing, about $1 pick fee, $10 to ship a heavy item, and $15 for a 15 '
                              'percent return rate, landing at $53 of fuel profit [gCo34Jl1RkQ @ '
                              '00:06:19]. Then set a net target per order: fuel profit of $53 minus a $20 '
                              'net target gives a $33 target CAC, which becomes the rule for building the '
                              'ad account and thinking about bid caps [gCo34Jl1RkQ @ 00:08:06]. Mark of '
                              'Mark Builds Brands wires the same logic into a calculator: product price, '
                              'COGS from AliExpress or CJ Dropshipping, US shipping, and payment '
                              'processing at a standard 2.7 percent plus 30 cents per order [eTADhJ3N_oo @ '
                              '00:02:47]. His KPIs are a 60 percent gross margin, a break-even ROAS where '
                              '1.84 is tough to scale and his personal target is 1.3, and a 20 percent '
                              'profit margin; his sample store showed a 1.67 ROAS against that 1.84 '
                              'break-even, meaning a 3 percent margin and $613 of profit [eTADhJ3N_oo @ '
                              '00:04:57]. His two product-selection rules are a $20 gross margin minimum '
                              'and pricing at 3x cost of goods.',
                              "Eric Andrews' Black Friday case shows the mechanics of promo math. "
                              'Baseline: 1.75 percent conversion, $75 CAC, $124 net AOV, $21 product COGS, '
                              '$19 fulfillment, $84 contribution margin and only $9 after CAC [t2H3gJHuw6k '
                              '@ 00:02:33]. At 50 percent off, CAC can drop to $33, but most buyers take '
                              'one unit, gross order value falls to $68, product and fulfillment costs '
                              'barely move, and contribution margin of $29 sits below the $33 CAC, so '
                              'every customer loses money [t2H3gJHuw6k @ 00:05:13]. Switch to two-for-one '
                              'with no refunds and the customer pays $135, product COGS doubles to $42, '
                              'shipping rises only marginally, and contribution margin jumps to $69 with '
                              '$36 left after CAC; on 20,000 orders he puts that at three-quarters of a '
                              'million dollars [t2H3gJHuw6k @ 00:09:35]. Abir runs the ad-spend version: '
                              '$250,000 of spend at 4x ROAS with 30 percent COGS throws off $450,000 of '
                              'contribution and $150,000 profit against $300,000 fixed costs; when ROAS '
                              'slides to 3x the business drops to a $25,000 loss, cutting spend to '
                              '$150,000 to restore 4x deepens it to $30,000, while raising spend to '
                              '$350,000 at 3x yields an $85,000 profit [lrF2Uey1-uU @ 00:08:08]. He adds '
                              'that break-even in that model sits around a 2.6 or 2.7 ROAS.'],
               'table': {'caption': 'Exact per-order numbers and levers taught by the practitioners',
                         'headers': ['Line Item or Lever',
                                     'Exact Number Taught',
                                     'How the Speaker Uses It',
                                     'Expert Source'],
                         'rows': [['Payment processing fees charged on every single order',
                                   'Standard 2.7 percent plus 30 cents per transaction',
                                   'Auto-calculated per order inside the unit economics calculator',
                                   'Mark Builds Brands Highlights ([eTADhJ3N_oo @ 00:02:47])'],
                                  ['Stacked merchant fees for smaller retailers using multiple processors',
                                   'Often around 5 to 6 percent once everything is added up',
                                   'Check the combined total of third-party merchant plus Shopify fees, '
                                   'not one line',
                                   'Matt Byrne ([sR1NjOCbwOA @ 00:11:22])'],
                                  ['Fuel profit converted into a target customer acquisition cost',
                                   '$53 fuel profit minus a $20 net target equals a $33 CAC',
                                   'Sets the rule for building the ad account and thinking about bid caps',
                                   'Common Thread Collective ([gCo34Jl1RkQ @ 00:08:06])'],
                                  ['Break-even revenue calculated from fixed costs and contribution ratio',
                                   '$2,400 fixed costs divided by 30 percent equals $8,000 per month',
                                   'Every dollar sold past $8,000 adds 30 cents of profit to the business',
                                   'Bloom Analytics ([mWL3C_COYk8 @ 00:04:14])'],
                                  ['Black Friday two-for-one offer versus a 50 percent sitewide discount',
                                   '$69 versus $29 contribution margin per order on identical CAC lift',
                                   'Gift extra product because an additional unit only costs the brand $21',
                                   'Eric Andrews ([t2H3gJHuw6k @ 00:08:36])'],
                                  ['Discount capacity tested on a single lower-margin SKU',
                                   '20 percent off loses money; 15 percent leaves a very small profit',
                                   'Run net price after discount through COGS and cost per acquisition '
                                   'before promoting',
                                   'Matt Byrne ([sR1NjOCbwOA @ 00:19:13])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Margin Leaks the Operators Plug First',
                           'body': 'Small per-order line items decide whether a brand profits at scale. '
                                   'These are the tactical adjustments the speakers apply directly in '
                                   'their models and dashboards.',
                           'items': ['Give marketing its own line: use ad spend alone when you calculate '
                                     'ROAS, but use full marketing costs, including influencer and '
                                     'affiliate payouts, agency fees and email and SMS tools, for '
                                     'contribution margin [Bloom Analytics — mWL3C_COYk8 @ 00:01:53].',
                                     'Audit total processing cost, not the headline rate: running another '
                                     'merchant on top of Shopify means paying both sets of fees, which can '
                                     'add up to 5 or 6 percent for smaller retailers [Matt Byrne — '
                                     'sR1NjOCbwOA @ 00:11:22].',
                                     'During any promo, do not offer refunds or returns, so the net order '
                                     'value holds above a straight 50 percent haircut, landing near 55 '
                                     'percent of normal net AOV [Eric Andrews — t2H3gJHuw6k @ 00:04:37].',
                                     'Layer hidden costs into the daily contribution calculation as a '
                                     'percentage of sales (royalties, revenue shares), a dollar figure per '
                                     'order such as a $2 pick fee, or a monthly cost such as agency or '
                                     'influencer fees [Common Thread Collective — b4ddPmPdQcY @ '
                                     '00:04:08].']},
               'sop_steps': [{'step': 1,
                              'title': 'Build Net Revenue Per Order',
                              'action': 'Start from gross revenue, back out discounts and returns, add '
                                        'shipping income, and divide by orders to get net AOV.',
                              'detail': 'Eric Andrews puts product sales and taxes collected into gross '
                                        'revenue, subtracts discounts and returns, adds shipping charges '
                                        'as revenue, and lands at about $134 of net revenue per order '
                                        '[Eric Andrews — 8xfPvprL5qE @ 00:07:02].'},
                             {'step': 2,
                              'title': 'Split Product COGS From Fulfillment COGS',
                              'action': 'Price landed cost (product, freight, duties, insurance) '
                                        'separately from pick and pack, packaging, last-mile shipping and '
                                        'merchant fees.',
                              'detail': 'Matt Byrne pulls landed cost from an inventory system, 3PL '
                                        'packing costs from the 3PL invoice, merchant fees from Shopify, '
                                        'PayPal or Afterpay, and shipping from the carrier, using a '
                                        'weighted average for city versus regional deliveries [Matt Byrne '
                                        '— sR1NjOCbwOA @ 00:12:21].'},
                             {'step': 3,
                              'title': 'Convert Fuel Profit Into a Target CAC',
                              'action': 'Subtract all per-unit costs and the return rate from price, then '
                                        'subtract your desired net profit per order to set the CAC '
                                        'ceiling.',
                              'detail': 'Common Thread Collective nets a $100 boot to $53 of fuel profit, '
                                        'subtracts a $20 net target, and runs the ad account against a $33 '
                                        'target CAC [Common Thread Collective — gCo34Jl1RkQ @ 00:08:06].'},
                             {'step': 4,
                              'title': 'Set Daily Contribution Targets and Track Against Them',
                              'action': 'Build a bottoms-up forecast to the P&L level, load daily revenue, '
                                        'spend and contribution targets, and review actuals every day.',
                              'detail': 'Common Thread Collective sets an expectation for every dollar '
                                        'earned, spent and contributed each day of the month, then reads '
                                        'contribution margin against target as the primary driving metric '
                                        '[Common Thread Collective — b4ddPmPdQcY @ 00:01:16].'}]},
              {'heading': 'Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The first fight is about definitions: does marketing sit inside '
                              'contribution margin or below it? Eric Andrews defines contribution margin '
                              'as revenue minus product cost minus fulfillment. He then carves out a '
                              'separate post-marketing contribution margin, which he calls the lowest and '
                              'most important profit view [8xfPvprL5qE @ 00:02:14]. Chan at Bloom '
                              'Analytics rejects that split outright. Chan points out that most formulas '
                              'leave marketing out, and once marketing is gone the number is not '
                              'contribution margin anymore, it is gross profit [mWL3C_COYk8 @ 00:00:00]. '
                              'Common Thread Collective sides with Bloom. It defines contribution margin '
                              'as net revenue minus payment processing, pick-pack, fulfillment, cost of '
                              'goods, and ad spend [b4ddPmPdQcY @ 00:00:00]. Valentin Kuznetcov settles '
                              'the naming war by stacking three layers: product profit as CM1, gross '
                              'profit as CM2, and profit contribution as CM3, where every cost that brings '
                              'in revenue lives. Everything after that is OPEX [LmlQ8JEPflQ @ 00:04:36]. '
                              'For an operator, the point is not which label wins. Every team in the '
                              'business has to use the same ladder. Andrews himself warns that people say '
                              'gross margin when they mean contribution margin and vice versa. Each brand '
                              'has to define the terms by how it actually runs and then measure them as '
                              'separate ideas [Zh6xNyWZVs4 @ 00:00:20].',
                              'The second split is over which marketing dollars belong in the variable '
                              'layer. Bloom puts ad spend, influencer and affiliate payouts, agency fees, '
                              'and email and SMS tools straight into marketing costs inside contribution '
                              'margin [mWL3C_COYk8 @ 00:01:14]. Abir, CFO, takes a middle line. Agency '
                              'fees count as variable only if they scale with ad spend or revenue, and '
                              'influencer costs depend on how the deal is structured [lrF2Uey1-uU @ '
                              '00:03:05]. Kuznetcov goes the other way and argues that what a cost does '
                              'matters more than whether it scales. A fixed-retainer paid media agency is '
                              '100% OPEX. Even a performance-based agency goes to OPEX, because swapping '
                              'it for a retainer shop is just deal structure and does not change what the '
                              'cost is [LmlQ8JEPflQ @ 00:13:21]. His one exception is an agency that '
                              'explicitly charges per acquisition, such as 15% of new-customer profit '
                              'contribution. He treats that as a premium on nCAC. He also puts email and '
                              'SMS send fees into CM3, while Klaviyo-style platform fees and CRM software '
                              'sit in OPEX. He puts most creative and content in OPEX too, because a '
                              "creative can run for days or for years. Common Thread's Statlas setup lets "
                              'operators add agency or influencer fees as a monthly fixed cost, a '
                              'percentage of sales, or a per-order dollar figure [b4ddPmPdQcY @ 00:04:08].',
                              'The sharpest strategic disagreement is how much first-order loss a brand '
                              'can carry. Eric Andrews calls first-order profitability the ideal, because '
                              'every repeat order then lands as nearly pure profit with little or no '
                              'marketing attached [LKEn47f67vQ @ 00:01:31]. His benchmark work softens '
                              'that position. A brand whose customers buy 5, 10, or 15 times can afford to '
                              'lose more on the first order. A contribution-margin-to-CAC ratio under one '
                              'is survivable only with heavy repeat buyers, never with one-time buyers '
                              '[gG33a-ErNRQ @ 00:05:10]. Common Thread runs Bamboo Earth at first-order '
                              'break-even, meaning zero contribution, so every repeat order is pure '
                              "incremental contribution [b4ddPmPdQcY @ 00:02:46]. Patrick O'Driscoll "
                              'agrees that scaling on lifetime value is the fastest way to grow. He adds '
                              'that it needs significant cash reserves and a deep grasp of repeat purchase '
                              'rates, and that most smaller brands should keep nCAC below AOV from day one '
                              '[vI_Np8RQikw @ 00:12:23]. Practitioners also split on spend. Mark warns '
                              'that CAC climbs at every step from $100 a day to $100,000 a day. StoreHero, '
                              'on the other hand, watched a brand raise spend 260%, take a 56% drop in '
                              'MER, and still grow contribution margin 18%.'],
               'table': {'caption': 'Side-by-side playbooks where named practitioners split on '
                                    'contribution margin decisions',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Where marketing sits in the margin stack',
                                   'Contribution margin is revenue minus product cost minus fulfillment, '
                                   'with post-marketing margin tracked separately',
                                   'Strip marketing out and the number is not contribution margin, it is '
                                   'just gross profit',
                                   'Eric Andrews ([8xfPvprL5qE @ 00:02:14]); Bloom Analytics ([mWL3C_COYk8 '
                                   '@ 00:00:00])'],
                                  ['How to book paid media agency fees',
                                   'Treat agency fees as variable costs when they scale with ad spend or '
                                   'revenue',
                                   'Book them as OPEX whether retainer or performance based, unless the '
                                   'agency explicitly charges per acquisition',
                                   'Abir, CFO ([lrF2Uey1-uU @ 00:03:05]); Valentin Kuznetcov ([LmlQ8JEPflQ '
                                   '@ 00:13:21])'],
                                  ['How much loss a first order can carry',
                                   'Black Friday buyers retain badly, so every brand should make money on '
                                   'the first order',
                                   'Brands whose customers buy 5, 10, or 15 times can lose more upfront '
                                   'and recover it later',
                                   'Eric Andrews ([t2H3gJHuw6k @ 00:02:56]); Eric Andrews ([gG33a-ErNRQ @ '
                                   '00:05:10])'],
                                  ['Scaling when nCAC is higher than AOV',
                                   'Most smaller brands should keep new customer acquisition cost below '
                                   'AOV from day one',
                                   'The fastest way to scale is betting on LTV, backed by cash reserves '
                                   'and repeat-rate data',
                                   "Patrick O'Driscoll | E-Commerce Growth Marketer ([vI_Np8RQikw @ "
                                   '00:12:23])'],
                                  ['What to do when ROAS falls on Meta',
                                   'The usual owner reflex is to cut ad spend until the 4x ROAS target '
                                   'comes back',
                                   'Turn spend up instead, since break-even holds down to about 2.6 or 2.7 '
                                   'ROAS',
                                   'Abir, CFO ([lrF2Uey1-uU @ 00:07:01]); Abir, CFO ([lrF2Uey1-uU @ '
                                   '00:08:21])'],
                                  ['Minimum gross margin before spending on ads',
                                   'Target a 60% gross margin, at least $20 gross margin per unit, and a '
                                   '3x COGS price',
                                   'A product at 70 to 75 percent gross margin counts as a healthy margin',
                                   'Mark Builds Brands Highlights ([eTADhJ3N_oo @ 00:05:30]); Eric Andrews '
                                   '([8xfPvprL5qE @ 00:08:52])'],
                                  ['How granular contribution tracking should be',
                                   'Start at business and channel level, because SKU tracking is very time '
                                   'consuming',
                                   'Treating every SKU as the same net outcome is a top drain on money in '
                                   'your pocket',
                                   'LedgerGurus: Ecommerce Accounting Experts ([e5r7-KT6mQ0 @ 00:03:11]); '
                                   'Common Thread Collective ([gCo34Jl1RkQ @ 00:08:40])']]}},
              {'heading': 'Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The most expensive trap anyone reported is the sitewide percentage '
                              'discount. Eric Andrews knew a brand that ran 50% off every Black Friday and '
                              'lost $500,000 the last time it did [t2H3gJHuw6k @ 00:00:00]. The mechanics '
                              'are brutal. Baseline economics were $124 net AOV, $21 product COGS, $19 '
                              'fulfillment, $84 contribution margin, and only $9 left after a $75 CAC. At '
                              'half off, the conversion lift pushed CAC down to $33. But net order value '
                              'fell to about 55% of normal while product and fulfillment costs stayed the '
                              'same. That left $29 of contribution margin and a loss on every customer. '
                              'Switching to buy-one-get-one gave the shopper the same perceived value, '
                              'since the extra unit cost the brand only $21. Contribution margin rose to '
                              '$69 and CM minus CAC to $36, worth roughly three quarters of a million '
                              'dollars on 20,000 orders [t2H3gJHuw6k @ 00:09:35]. Matt Byrne hit the same '
                              'ceiling on everyday promos. A flat 20% discount on a $100 SKU makes it lose '
                              'money, 15% leaves very little, and that product could really only afford '
                              'about 5% [sR1NjOCbwOA @ 00:19:33]. Bloom Analytics adds the rule underneath '
                              'both cases: with negative contribution margin, more sales make things worse '
                              '[mWL3C_COYk8 @ 00:04:14].',
                              'The second failure pattern is scaling spend into economics that never '
                              "worked. Mark's own calculator example shows a 1.67 estimated ROAS that "
                              'looks fine until you compare it with a 1.84 break-even ROAS. The result is '
                              'negative net profit per order and a 3% profit margin against a 20% KPI '
                              '[eTADhJ3N_oo @ 00:04:57]. He warns that CAC rises at every step up in daily '
                              'spend, so a brand that is not very profitable at $1K to $10K a day has no '
                              'shot at scale. Eric Andrews models the venture-funded version. CAC climbs '
                              'from $68 to $79 to $123 to $149 while the team raises a $20 million round '
                              'and keeps pouring money into marketing. It ends at a 0.58 '
                              'contribution-margin-to-CAC ratio, losing money on every customer '
                              '[gG33a-ErNRQ @ 00:15:47]. Abir, CFO, shows the opposite panic. When Meta '
                              'slips from 4x to 3x ROAS on $250,000 of spend, a $150,000 profit becomes a '
                              '$25,000 loss. Cutting spend to $150,000 to get back to 4x makes the loss '
                              'worse, at $30,000 [lrF2Uey1-uU @ 00:07:17]. His fix was raising spend to '
                              '$350,000, which got the business back to an $85,000 profit. StoreHero calls '
                              'both mistakes waste: overspending for topline revenue, and leaving cash in '
                              'the bank idle when the unit economics are staring you in the face '
                              '[xJXlWITRM7I @ 00:23:59].',
                              'The quietest losses come from bad data. Matt Byrne has seen businesses keep '
                              'selling SKUs whose gross margin leaves no room for ads. Contribution margin '
                              'on those SKUs goes negative, while profitable SKUs fund the loss and hide '
                              'it inside a P&L that looks profitable overall [sR1NjOCbwOA @ 00:15:26]. He '
                              'also warns that landed costs tracked in Excel break down once several '
                              'purchase orders carry different per-unit costs, which ends in death by '
                              'spreadsheet. Stacked merchant and Shopify fees can reach 5 or 6% for '
                              "smaller retailers. Bloom Analytics points out that Shopify's built-in "
                              'profit reports subtract product cost and stop there, so shipping, payment '
                              'fees, and ad spend never reach the number [mWL3C_COYk8 @ 00:04:36]. '
                              'Valentin Kuznetcov flags two costs of misclassification. Dumping variable '
                              'promotion costs into OPEX inflates OPEX against benchmarks and hides broken '
                              'growth economics. Miscategorized costs can also lead a brand to overpay its '
                              'growth team on performance compensation [LmlQ8JEPflQ @ 00:03:02]. Common '
                              "Thread's daily reporting shows why single-number goals mislead. Sales and "
                              'spend ran about 8% above target and MER sat on target, yet contribution '
                              'margin landed almost 60% over expectation. Repeat cohorts outperformed '
                              'while new customer acquisition ran about 10% behind [b4ddPmPdQcY @ '
                              '00:05:11].'],
               'table': {'caption': 'Firsthand losses and modeled blow-ups with the economics check that '
                                    'catches each one',
                         'headers': ['Failure Mode', 'What Happened', 'Economics Check', 'Expert Source'],
                         'rows': [['Running 50% off sitewide on Black Friday',
                                   'The brand lost $500,000 the last time it ran the half-off promo',
                                   'Contribution margin of $29 against a $33 CAC means losing money on '
                                   'each customer',
                                   'Eric Andrews ([t2H3gJHuw6k @ 00:05:13])'],
                                  ['Cutting ad spend to chase a ROAS target',
                                   'Cutting spend to $150K got back to 4x ROAS, but the loss grew to $30K',
                                   'Measure contribution margin dollars against fixed costs, not ROAS '
                                   'alone',
                                   'Abir, CFO ([lrF2Uey1-uU @ 00:07:17])'],
                                  ['Scaling with a CM to CAC ratio below one',
                                   'A funded brand pushed CAC to $149 while lifetime orders stayed at 1.8',
                                   'An LTV to CAC ratio of one leaves no money to cover OPEX',
                                   'Eric Andrews ([gG33a-ErNRQ @ 00:16:44])'],
                                  ['Hidden SKUs with negative contribution margin',
                                   'Profitable SKUs quietly paid for ad spend on products that were losing '
                                   'money',
                                   'Calculate contribution margin per SKU before deciding where ad budget '
                                   'goes',
                                   'Matt Byrne ([sR1NjOCbwOA @ 00:15:42])'],
                                  ["Trusting Shopify's built-in profit reports",
                                   'The built-in reports subtract product costs and then stop calculating',
                                   'Add shipping, payment fees, and ad spend before reading any profit '
                                   'number',
                                   'Bloom Analytics ([mWL3C_COYk8 @ 00:04:36])'],
                                  ['Weak front-end margins before scaling spend',
                                   'A 1.67 estimated ROAS looked acceptable against a 1.84 break-even ROAS',
                                   'Hold a 60% gross margin and at least $20 gross margin per unit',
                                   'Mark Builds Brands Highlights ([eTADhJ3N_oo @ 00:04:57])'],
                                  ['Cash flow squeeze while scaling inventory and ads',
                                   'Clients cut marketing, agencies, and staff when cash got tight, which '
                                   'slowed growth',
                                   'Track cash conversion cycle, inventory turnover, burn rate, and '
                                   'operating cash flow',
                                   "Patrick O'Driscoll | E-Commerce Growth Marketer ([vI_Np8RQikw @ "
                                   '00:09:20])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Stop-Checks Before Spend Goes Up or a Promo Ships',
                           'body': 'Four stop-checks drawn from losses these operators took or modeled. '
                                   'Run every one before raising budget, launching a discount, or cutting '
                                   'spend.',
                           'items': ['Do not scale while the first-order contribution margin to CAC ratio '
                                     'is below one on a product people buy once. Andrews says that '
                                     'business should not be scaling until it fixes its unit economics '
                                     '[Eric Andrews — gG33a-ErNRQ @ 00:15:10].',
                                     'Before launch, model every Black Friday promo both as percent-off '
                                     'and as two-for-one. Kill any version where contribution margin minus '
                                     'CAC goes negative [Eric Andrews — t2H3gJHuw6k @ 00:05:34].',
                                     'If contribution margin is 0% or less, stop and fix pricing, COGS, or '
                                     'cost of sales right away, because the business is broken '
                                     '[LedgerGurus: Ecommerce Accounting Experts — e5r7-KT6mQ0 @ '
                                     '00:02:14].',
                                     'Before cutting spend on a ROAS dip, recalculate contribution margin '
                                     'dollars against fixed costs at both lower and higher spend levels '
                                     '[Abir, CFO — lrF2Uey1-uU @ 00:07:31].']}}],
 'pull_quote': '"If your unit economics work, your business works. If your unit economics don\'t work, '
               'your business will never work." — Eric Andrews (t2H3gJHuw6k @ 00:10:14).',
 'diagram_id': 'diag-03',
 'action_checklist': ['Rebuild the P&L into product profit, gross profit, and profit contribution layers, '
                      'with paid media and affiliate commission inside CM3 [Valentin Kuznetcov — '
                      'LmlQ8JEPflQ @ 00:04:57].',
                      'Calculate per-order AOV, product COGS, and fulfillment by dividing each monthly '
                      'total by total orders, and use a trailing average of a couple of months when the '
                      'numbers bounce around [Eric Andrews Clips — tj2W9oEqeQo @ 00:01:33].',
                      'Set target CAC as fuel profit minus net target, so $53 minus $20 gives a $33 CAC, '
                      'and calculate it separately for each SKU [Common Thread Collective — gCo34Jl1RkQ @ '
                      '00:08:06].',
                      'Find break-even revenue by dividing fixed costs by the contribution margin ratio, '
                      'so $2,400 divided by 30% equals $8,000 a month [Bloom Analytics — mWL3C_COYk8 @ '
                      '00:04:14].',
                      'Calculate blended nCAC as total marketing spend divided by new customers only, '
                      "leaving returning customers out of the denominator [Patrick O'Driscoll | E-Commerce "
                      'Growth Marketer — vI_Np8RQikw @ 00:10:35].',
                      'Set a daily contribution margin target from a bottoms-up forecast and review '
                      'actuals against it every day [Common Thread Collective — b4ddPmPdQcY @ 00:00:45].'],
 'statutory_citations': [{'title': 'Eric Andrews — 50% Off vs. BOGO: Unit Economics Case Study (How We '
                                   'Lost $500K) [00:00:00]',
                          'url': 'https://www.youtube.com/watch?v=t2H3gJHuw6k&t=0s',
                          'relevance': 'Primary practitioner testimony on the $500,000 Black Friday promo '
                                       'loss and the buy-one-get-one contribution margin fix.'},
                         {'title': 'Abir, CFO — How to Calculate eCommerce Contribution Margins (DTC '
                                   'Accountant Explains) [00:06:29]',
                          'url': 'https://www.youtube.com/watch?v=lrF2Uey1-uU&t=389s',
                          'relevance': 'Primary practitioner testimony on why cutting ad spend to recover '
                                       'ROAS deepened losses while raising spend restored profit.'},
                         {'title': 'Valentin Kuznetcov — Ecommerce Marketing Costs Explained: What Goes '
                                   'Into OPEX vs CM3? [00:04:57]',
                          'url': 'https://www.youtube.com/watch?v=LmlQ8JEPflQ&t=297s',
                          'relevance': 'Primary practitioner testimony on sorting marketing costs into CM3 '
                                       'or OPEX by the nature of the cost.'},
                         {'title': 'Eric Andrews — Unit Economics Benchmarks for eCommerce | From Idea to '
                                   'Exit [00:15:10]',
                          'url': 'https://www.youtube.com/watch?v=gG33a-ErNRQ&t=910s',
                          'relevance': 'Primary practitioner testimony on contribution margin to CAC '
                                       'benchmarks and the funded scale-up that loses money on every '
                                       'customer.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'e5r7-KT6mQ0',
                       'title': 'Ecommerce Contribution Margin Explained',
                       'channel': 'LedgerGurus: Ecommerce Accounting Experts',
                       'author': 'LedgerGurus: Ecommerce Accounting Experts',
                       'text': 'If you have a contribution margin of 0% or less, you have a broken '
                               'business. Your fundamental pricing and variable costs must change.',
                       'tip': 'If you have a contribution margin of 0% or less, you have a broken '
                              'business. Your fundamental pricing and variable costs must change.',
                       'timestamp': 134,
                       'timestamp_seconds': 134,
                       'timestamp_label': '[00:02:14]',
                       'url': 'https://www.youtube.com/watch?v=e5r7-KT6mQ0&t=134s',
                       'markdown': '[00:02:14](https://www.youtube.com/watch?v=e5r7-KT6mQ0&t=134s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'LKEn47f67vQ',
                       'title': 'Contribution Margin: CAC Ratio for eCommerce | Unit Economics',
                       'channel': 'Eric Andrews Clips',
                       'author': 'Eric Andrews Clips',
                       'text': "If you're profitable on the first order then all of the subsequent orders "
                               'that a customer makes when they return will be pure profit because '
                               "there'll generally be little or no marketing associated with them.",
                       'tip': "If you're profitable on the first order then all of the subsequent orders "
                              "that a customer makes when they return will be pure profit because there'll "
                              'generally be little or no marketing associated with them.',
                       'timestamp': 91,
                       'timestamp_seconds': 91,
                       'timestamp_label': '[00:01:31]',
                       'url': 'https://www.youtube.com/watch?v=LKEn47f67vQ&t=91s',
                       'markdown': '[00:01:31](https://www.youtube.com/watch?v=LKEn47f67vQ&t=91s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '8xfPvprL5qE',
                       'title': 'How to Calculate eCommerce Contribution Margins',
                       'channel': 'Eric Andrews',
                       'author': 'Eric Andrews',
                       'text': 'The key to success with these businesses is optimizing the unit economics; '
                               'if you can negotiate or eliminate any individual expense and knock a '
                               'couple dollars out that might be the difference between an extra five '
                               'dollars per order.',
                       'tip': 'The key to success with these businesses is optimizing the unit economics; '
                              'if you can negotiate or eliminate any individual expense and knock a couple '
                              'dollars out that might be the difference between an extra five dollars per '
                              'order.',
                       'timestamp': 773,
                       'timestamp_seconds': 773,
                       'timestamp_label': '[00:12:53]',
                       'url': 'https://www.youtube.com/watch?v=8xfPvprL5qE&t=773s',
                       'markdown': '[00:12:53](https://www.youtube.com/watch?v=8xfPvprL5qE&t=773s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'tj2W9oEqeQo',
                       'title': 'Master Contribution Margins for eCommerce',
                       'channel': 'Eric Andrews Clips',
                       'author': 'Eric Andrews Clips',
                       'text': "It's good to sometimes just do a trailing average of a couple months, "
                               'especially if the numbers bounce around a lot.',
                       'tip': "It's good to sometimes just do a trailing average of a couple months, "
                              'especially if the numbers bounce around a lot.',
                       'timestamp': 93,
                       'timestamp_seconds': 93,
                       'timestamp_label': '[00:01:33]',
                       'url': 'https://www.youtube.com/watch?v=tj2W9oEqeQo&t=93s',
                       'markdown': '[00:01:33](https://www.youtube.com/watch?v=tj2W9oEqeQo&t=93s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'eTADhJ3N_oo',
                       'title': 'unit economics for ecom explained (boring as hell, but prints $$$)',
                       'channel': 'Mark Builds Brands Highlights',
                       'author': 'Mark Builds Brands Highlights',
                       'text': "Your CAC is only going to go up, so if you're not super profitable at "
                               "these low levels of spend, then no shot that you're going to be profitable "
                               'as you try to scale more.',
                       'tip': "Your CAC is only going to go up, so if you're not super profitable at these "
                              "low levels of spend, then no shot that you're going to be profitable as you "
                              'try to scale more.',
                       'timestamp': 405,
                       'timestamp_seconds': 405,
                       'timestamp_label': '[00:06:45]',
                       'url': 'https://www.youtube.com/watch?v=eTADhJ3N_oo&t=405s',
                       'markdown': '[00:06:45](https://www.youtube.com/watch?v=eTADhJ3N_oo&t=405s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'gG33a-ErNRQ',
                       'title': 'Unit Economics Benchmarks for eCommerce | From Idea to Exit',
                       'channel': 'Eric Andrews',
                       'author': 'Eric Andrews',
                       'text': 'Our contribution margin to CAC ratio is less than one and our LTV to CAC '
                               'ratio is less than one, and so this business should not be scaling until '
                               'it can fix its unit economics.',
                       'tip': 'Our contribution margin to CAC ratio is less than one and our LTV to CAC '
                              'ratio is less than one, and so this business should not be scaling until it '
                              'can fix its unit economics.',
                       'timestamp': 910,
                       'timestamp_seconds': 910,
                       'timestamp_label': '[00:15:10]',
                       'url': 'https://www.youtube.com/watch?v=gG33a-ErNRQ&t=910s',
                       'markdown': '[00:15:10](https://www.youtube.com/watch?v=gG33a-ErNRQ&t=910s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 't2H3gJHuw6k',
                       'title': '50% Off vs. BOGO: Unit Economics Case Study (How We Lost $500K)',
                       'channel': 'Eric Andrews',
                       'author': 'Eric Andrews',
                       'text': 'I used to know an e-commerce brand that ran a 50% off sitewide discount '
                               'every Black Friday. And the last time they ran it, they lost $500,000.',
                       'tip': 'I used to know an e-commerce brand that ran a 50% off sitewide discount '
                              'every Black Friday. And the last time they ran it, they lost $500,000.',
                       'timestamp': 0,
                       'timestamp_seconds': 0,
                       'timestamp_label': '[00:00:00]',
                       'url': 'https://www.youtube.com/watch?v=t2H3gJHuw6k&t=0s',
                       'markdown': '[00:00:00](https://www.youtube.com/watch?v=t2H3gJHuw6k&t=0s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 't2H3gJHuw6k',
                       'title': '50% Off vs. BOGO: Unit Economics Case Study (How We Lost $500K)',
                       'channel': 'Eric Andrews',
                       'author': 'Eric Andrews',
                       'text': 'When you offer the customer two for one, you are able to give them $135, '
                               "but the difference is that you don't lose half your revenue. An extra unit "
                               'only costs you $21.',
                       'tip': 'When you offer the customer two for one, you are able to give them $135, '
                              "but the difference is that you don't lose half your revenue. An extra unit "
                              'only costs you $21.',
                       'timestamp': 435,
                       'timestamp_seconds': 435,
                       'timestamp_label': '[00:07:15]',
                       'url': 'https://www.youtube.com/watch?v=t2H3gJHuw6k&t=435s',
                       'markdown': '[00:07:15](https://www.youtube.com/watch?v=t2H3gJHuw6k&t=435s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'LmlQ8JEPflQ',
                       'title': 'Ecommerce Marketing Costs Explained: What Goes Into OPEX vs CM3?',
                       'channel': 'Valentin Kuznetcov',
                       'author': 'Valentin Kuznetcov',
                       'text': 'Direct marketing is costs incurred to promote or advertise your product, '
                               'whereas OPEX is costs that build systems and elevate the organization.',
                       'tip': 'Direct marketing is costs incurred to promote or advertise your product, '
                              'whereas OPEX is costs that build systems and elevate the organization.',
                       'timestamp': 338,
                       'timestamp_seconds': 338,
                       'timestamp_label': '[00:05:38]',
                       'url': 'https://www.youtube.com/watch?v=LmlQ8JEPflQ&t=338s',
                       'markdown': '[00:05:38](https://www.youtube.com/watch?v=LmlQ8JEPflQ&t=338s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Zh6xNyWZVs4',
                       'title': 'Gross margin vs. contribution margin for eCommerce | Eric Andrews clips',
                       'channel': 'Eric Andrews Clips',
                       'author': 'Eric Andrews Clips',
                       'text': 'Often people say gross margin when they mean contribution margin and vice '
                               "versa, so it's important to define them according to how you're running "
                               'your business and then measure them as unique ideas.',
                       'tip': 'Often people say gross margin when they mean contribution margin and vice '
                              "versa, so it's important to define them according to how you're running "
                              'your business and then measure them as unique ideas.',
                       'timestamp': 20,
                       'timestamp_seconds': 20,
                       'timestamp_label': '[00:00:20]',
                       'url': 'https://www.youtube.com/watch?v=Zh6xNyWZVs4&t=20s',
                       'markdown': '[00:00:20](https://www.youtube.com/watch?v=Zh6xNyWZVs4&t=20s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'vI_Np8RQikw',
                       'title': 'The E-Commerce Profit Framework (Used by 7–8 Figure Brands)',
                       'channel': "Patrick O'Driscoll | E-Commerce Growth Marketer",
                       'author': "Patrick O'Driscoll | E-Commerce Growth Marketer",
                       'text': "This is called scaling on lifetime value: if you're scaling where your new "
                               "customer acquisition is higher than your AOV, then you're betting that a "
                               'customer will make a second or third purchase to become profitable.',
                       'tip': "This is called scaling on lifetime value: if you're scaling where your new "
                              "customer acquisition is higher than your AOV, then you're betting that a "
                              'customer will make a second or third purchase to become profitable.',
                       'timestamp': 718,
                       'timestamp_seconds': 718,
                       'timestamp_label': '[00:11:58]',
                       'url': 'https://www.youtube.com/watch?v=vI_Np8RQikw&t=718s',
                       'markdown': '[00:11:58](https://www.youtube.com/watch?v=vI_Np8RQikw&t=718s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'mWL3C_COYk8',
                       'title': 'How to Calculate Contribution Margin (Formula + Shopify Example)',
                       'channel': 'Bloom Analytics',
                       'author': 'Bloom Analytics',
                       'text': 'Most contribution margin formulas do not include your marketing costs. '
                               'Take marketing out and that number is not your contribution margin '
                               "anymore. It's your gross profit.",
                       'tip': 'Most contribution margin formulas do not include your marketing costs. Take '
                              "marketing out and that number is not your contribution margin anymore. It's "
                              'your gross profit.',
                       'timestamp': 0,
                       'timestamp_seconds': 0,
                       'timestamp_label': '[00:00:00]',
                       'url': 'https://www.youtube.com/watch?v=mWL3C_COYk8&t=0s',
                       'markdown': '[00:00:00](https://www.youtube.com/watch?v=mWL3C_COYk8&t=0s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'xJXlWITRM7I',
                       'title': 'Contribution Margin Explained (with Examples)',
                       'channel': 'StoreHero',
                       'author': 'StoreHero',
                       'text': 'As long as your increase in ad spend is yielding extra contribution '
                               "margin, that's a positive and you should continue to spend.",
                       'tip': 'As long as your increase in ad spend is yielding extra contribution margin, '
                              "that's a positive and you should continue to spend.",
                       'timestamp': 1207,
                       'timestamp_seconds': 1207,
                       'timestamp_label': '[00:20:07]',
                       'url': 'https://www.youtube.com/watch?v=xJXlWITRM7I&t=1207s',
                       'markdown': '[00:20:07](https://www.youtube.com/watch?v=xJXlWITRM7I&t=1207s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'sR1NjOCbwOA',
                       'title': 'Understanding Unit Economics in Ecommerce',
                       'channel': 'Matt Byrne',
                       'author': 'Matt Byrne',
                       'text': "I've seen businesses where their gross profit margin is so low it doesn't "
                               'leave any capacity behind to spend money on ads and therefore the '
                               'contribution margin is negative, but they continue to sell it.',
                       'tip': "I've seen businesses where their gross profit margin is so low it doesn't "
                              'leave any capacity behind to spend money on ads and therefore the '
                              'contribution margin is negative, but they continue to sell it.',
                       'timestamp': 926,
                       'timestamp_seconds': 926,
                       'timestamp_label': '[00:15:26]',
                       'url': 'https://www.youtube.com/watch?v=sR1NjOCbwOA&t=926s',
                       'markdown': '[00:15:26](https://www.youtube.com/watch?v=sR1NjOCbwOA&t=926s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'lrF2Uey1-uU',
                       'title': 'How to Calculate eCommerce Contribution Margins (DTC Accountant Explains)',
                       'channel': 'Abir, CFO',
                       'author': 'Abir, CFO',
                       'text': "Just because you reduced ad spend to improve your ROAS doesn't necessarily "
                               "mean that your business is doing better; you have to make sure that you're "
                               'generating enough contribution margin to cover your fixed expenses.',
                       'tip': "Just because you reduced ad spend to improve your ROAS doesn't necessarily "
                              "mean that your business is doing better; you have to make sure that you're "
                              'generating enough contribution margin to cover your fixed expenses.',
                       'timestamp': 451,
                       'timestamp_seconds': 451,
                       'timestamp_label': '[00:07:31]',
                       'url': 'https://www.youtube.com/watch?v=lrF2Uey1-uU&t=451s',
                       'markdown': '[00:07:31](https://www.youtube.com/watch?v=lrF2Uey1-uU&t=451s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'gCo34Jl1RkQ',
                       'title': 'Unit Economics of Ecommerce Growth',
                       'channel': 'Common Thread Collective',
                       'author': 'Common Thread Collective',
                       'text': 'The amount of people that I see running a Facebook ad account where they '
                               'treat every SKU as if they produce the same net outcome is one of the '
                               'number one drainers of money in your pocket.',
                       'tip': 'The amount of people that I see running a Facebook ad account where they '
                              'treat every SKU as if they produce the same net outcome is one of the '
                              'number one drainers of money in your pocket.',
                       'timestamp': 537,
                       'timestamp_seconds': 537,
                       'timestamp_label': '[00:08:57]',
                       'url': 'https://www.youtube.com/watch?v=gCo34Jl1RkQ&t=537s',
                       'markdown': '[00:08:57](https://www.youtube.com/watch?v=gCo34Jl1RkQ&t=537s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'b4ddPmPdQcY',
                       'title': 'How to Track, Measure, and Report Contribution Margin',
                       'channel': 'Common Thread Collective',
                       'author': 'Common Thread Collective',
                       'text': 'You can never just have one revenue goal or one spend goal or even an MER '
                               'goal; you have to look at all of these things together to really '
                               'understand how your business is getting to where it is.',
                       'tip': 'You can never just have one revenue goal or one spend goal or even an MER '
                              'goal; you have to look at all of these things together to really understand '
                              'how your business is getting to where it is.',
                       'timestamp': 344,
                       'timestamp_seconds': 344,
                       'timestamp_label': '[00:05:44]',
                       'url': 'https://www.youtube.com/watch?v=b4ddPmPdQcY&t=344s',
                       'markdown': '[00:05:44](https://www.youtube.com/watch?v=b4ddPmPdQcY&t=344s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'}]}
