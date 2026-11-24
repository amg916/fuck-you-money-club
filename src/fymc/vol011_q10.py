from __future__ import annotations

CHAPTER_10 = {'id': 'Q10',
 'chapter_id': 'Q10',
 'chapter_number': 10,
 'question_number': 10,
 'slug': 'vol011-q10-business-valuation-earnings-multiples-deal-structure',
 'question_prompt': 'Which earnings measure and multiple should I use to evaluate a business, and how do '
                    'SaaS characteristics and financing terms affect the proposed transaction?',
 'kicker': 'Q10 / THE BIG MONEY PLAYBOOKS',
 'title': 'Business Valuation: Earnings, Multiples, and Deal Structure',
 'subtitle': 'SDE, EBIT, EBITDA, add-backs, net profit versus cash flow, e-commerce valuations, SaaS '
             'valuation levers and exit planning, SBA financing, seller notes, earnouts, and rollovers',
 'layout_template': 'expert_commentary',
 'reading_time_minutes': 15,
 'executive_summary': 'Brokers, lower-middle-market advisors, SaaS specialists and a valuation professor '
                      'converge on one formula: normalized earnings times a risk-adjusted multiple. Under '
                      "roughly $500K-$1M of earnings, buyers price Seller's Discretionary Earnings (SDE) "
                      'at about 2-4x; above that, adjusted EBITDA takes over and multiples climb with '
                      'size, from 3-5x at $500K-$1M EBITDA to 6-10x at $5-10M and 12x-plus above $10M. '
                      'Owner dependence, customer concentration, trend, recurring revenue and clean books '
                      'move the multiple. Lenders cap price through SBA 7(a) rules: tax returns as source '
                      'of truth, 10% buyer injection, DSCR floors of 1.25 versus a stated 1.5 lender '
                      'appetite. Sharp splits remain on personal add-backs such as vehicles and phones, on '
                      'juicing trailing earnings before a sale, and on whether headline price or cash at '
                      'closing defines the real deal.',
 'key_metrics': [{'label': 'Main Street SDE Multiple Range',
                  'metric': 'Main Street SDE Multiple Range',
                  'value': '2-3.5x SDE',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Shep Campbell's working range for owner-operated businesses, set from comps "
                             'and industry datasets; EBITDA multiples run higher because of lower owner '
                             'risk.',
                  'source': 'Deal Street - Small to Lower Middle Market M&A ([ggUaT-lHV0A @ 00:04:13])'},
                 {'label': 'Lower-Middle-Market EBITDA Multiple at $1-3M EBITDA',
                  'metric': 'Lower-Middle-Market EBITDA Multiple at $1-3M EBITDA',
                  'value': 'Historically 4-7x, lately 5-8x, revised to 5-9x',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Arthur Petropoulos's band for companies bought by PE platforms and search "
                             'funds, including independent and fundless sponsors.',
                  'source': 'Arthur Petropoulos ([D58oCe_7BBM @ 00:04:36])'},
                 {'label': 'SBA 7(a) Minimum DSCR',
                  'metric': 'SBA 7(a) Minimum DSCR',
                  'value': '1.25 (previously 1.2), effective Oct 1, 2026',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Floor for acquisition loans; projections no longer count toward DSCR and '
                             '$3M-plus deals require an independent QoE report.',
                  'source': 'Deal Street - Small to Lower Middle Market M&A ([a5Z--B3Uhrg @ 00:03:08])'},
                 {'label': 'Add-Back Leverage at a 4x Multiple',
                  'metric': 'Add-Back Leverage at a 4x Multiple',
                  'value': '$50K add-back = $200K of price',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "David Newell's illustration of how a single disputed add-back swings SaaS "
                             'sale price when SDE is multiplied at 4x.',
                  'source': 'Quiet Light Brokerage ([oJsHo5vaDus @ 00:12:36])'}],
 'sections': [{'heading': 'Section 1: The Practitioner Consensus',
               'paragraphs': ['Main Street brokers and lower-middle-market advisors start from the same '
                              'arithmetic: normalized earnings times a multiple, with risk deciding where '
                              'the multiple lands. Shep Campbell of Deal Street, who values businesses '
                              'every week, frames value as earnings, multiple and risk, and insists buyers '
                              'purchase cash flow rather than revenue, warning that a $5M break-even '
                              'company can be worth less than a profitable $1M one [ggUaT-lHV0A @ '
                              '00:01:08]. Campbell puts it bluntly: cash flow services debt and pays the '
                              'owner [ggUaT-lHV0A @ 00:01:34]. Quiet Light Brokerage repeats the formula '
                              "for online sellers, stating that a business's value is based on a multiple "
                              'of its earnings and that buyers treat SDE as their baseline for estimating '
                              'return on investment [R4jvbLHhCBg @ 00:00:26]. Ryan C. Winter reduces it to '
                              'earnings times multiple, $300K at 3x for roughly $900K [tPnDBaB9oPU @ '
                              '00:01:02], and warns operators off revenue rules of thumb entirely '
                              '[tPnDBaB9oPU @ 00:03:58]. Campbell backs that warning with a scar: a '
                              'listing priced at 3x revenue, $15M on $5M of sales and roughly 10x cash '
                              'flow, never sold [ggUaT-lHV0A @ 00:09:04]. Price conversations therefore '
                              'open on documented profit, never on top-line volume, years in business, '
                              "debts the seller owes or the seller's retirement number.",
                              'Practitioners also agree on which earnings number to multiply, and the '
                              'switch turns on whether the buyer is buying a job or a managed company. '
                              'Keira Hamilton notes that SDE and EBITDA both add back interest, taxes, '
                              'depreciation, amortization, one-time items and discretionary spending, '
                              'while SDE alone also adds back owner salary [1dJeO4qEAhU @ 00:00:20]. Peter '
                              "Nola labels SDE 'return to a working owner,' its New Zealand name "
                              "[RoGz5NZF96I @ 00:00:38], and calls EBITDA 'managed profit' calculated "
                              'after owner pay [RoGz5NZF96I @ 00:01:39], the standard in M&A for medium, '
                              'large and capital-intensive firms [RoGz5NZF96I @ 00:03:16]. David C Barnett '
                              'draws the line near $500K: SDE for owner-operated firms below it at about '
                              '2-2.2x and lower for service firms, EBITDA above it [Va5USDqv3-A @ '
                              '00:03:34], and EBIT or EBITDA minus capex for capital-intensive operators '
                              'like trucking [Va5USDqv3-A @ 00:04:46]. Brett Cenkus places the salary '
                              "add-back mainly around $1-2M deals, where buyers 'buy themselves a job,' "
                              'while at roughly $20M management is retained and no salary comes back '
                              '[y4u_MuL4xhw @ 00:05:11]. The size cutoff floats from adviser to adviser, '
                              "but the logic holds: once a paid manager runs the business, the owner's "
                              'paycheck stops counting as discretionary earnings and the buyer prices a '
                              'managed cash stream.',
                              'On what moves the multiple, the risk lists line up almost item for item. '
                              'Campbell names owner dependence, customer concentration around 30-40%, '
                              'recurring revenue, trend, clean books, industry and size, and warns that '
                              "'the more a business depends on the owner at listing time, the more it will "
                              "depend on the owner at closing time' [ggUaT-lHV0A @ 00:06:46]. Winter's "
                              'list is nearly identical, flagging a single client at 50% of revenue as a '
                              'red flag alongside owner dependence, trend, clean books and team '
                              '[tPnDBaB9oPU @ 00:02:49]. Arthur Petropoulos explains why bigger companies '
                              'earn bigger multiples: less key-person risk and a broader buyer pool, a '
                              "dynamic labeled 'EBITDA expansion' that drives roll-ups, summed up as 'same "
                              "work, different deals' [brFD1fFAYhQ @ 00:01:12]. On the SaaS side, David "
                              'Newell of Quiet Light, who has sold 75-plus businesses including Drip, '
                              'names key-man risk as mistake number one: document the code, hand it to a '
                              'trusted developer or CTO, and step out quickly, the way Rob Walling brought '
                              'in Derek as CTO and left the code after about six months [oJsHo5vaDus @ '
                              '00:04:39]. Every one of these levers is about transferability. A buyer pays '
                              'up for earnings that survive the seller walking out the door, and discounts '
                              'every dollar that leaves with the founder.'],
               'table': {'caption': 'Where practitioners line up on earnings, multiples and risk',
                         'headers': ['Consensus Point',
                                     'What Practitioners Teach',
                                     'Operator Implication',
                                     'Expert Source'],
                         'rows': [['Buyers buy cash flow, never top-line revenue',
                                   'Value rests on earnings, multiple and risk; a $5M break-even firm can '
                                   'trail a profitable $1M one',
                                   'Lead every pricing conversation with documented, normalized profit '
                                   'figures',
                                   'Deal Street - Small to Lower Middle Market M&A ([ggUaT-lHV0A @ '
                                   '00:01:08])'],
                                  ['Value equals normalized earnings times a multiple',
                                   '$300K of earnings at 3x lands at roughly $900K of value',
                                   'Ignore revenue rules of thumb when setting any asking price',
                                   'Ryan C. Winter, Business Broker ([tPnDBaB9oPU @ 00:01:02])'],
                                  ['SDE adds owner salary on top of EBITDA add-backs',
                                   'Both add back interest, taxes, depreciation, amortization, one-time '
                                   'and discretionary items; SDE adds salary',
                                   'Use SDE for owner-run firms and EBITDA for managed ones',
                                   'Keira Hamilton ([1dJeO4qEAhU @ 00:00:20])'],
                                  ['The earnings metric switches with size and capital intensity',
                                   'SDE under roughly $500K, EBITDA above, EBITDA minus capex for '
                                   'trucking-type firms',
                                   'Match the earnings measure to the buyer universe before quoting '
                                   'multiples',
                                   'David C Barnett Small Business and Deal Making SMB ([Va5USDqv3-A @ '
                                   '00:03:34])'],
                                  ['The salary add-back fades as companies scale up',
                                   'Buyers at $1-2M buy themselves a job; at roughly $20M management stays '
                                   'on',
                                   'Stop adding back owner pay once a paid manager is required',
                                   'Brett Cenkus ([y4u_MuL4xhw @ 00:05:11])'],
                                  ['Owner dependence is the top multiple killer',
                                   'Dependence on the owner at listing time carries straight through to '
                                   'closing time',
                                   'Build a team and documented systems before going to market',
                                   'Deal Street - Small to Lower Middle Market M&A ([ggUaT-lHV0A @ '
                                   '00:06:46])'],
                                  ['Size earns multiple expansion across the market',
                                   'Larger EBITDA brings less key-person risk and a broader buyer pool, '
                                   'fueling roll-ups',
                                   'Grow or combine earnings to climb into a higher multiple band',
                                   'Arthur Petropoulos ([brFD1fFAYhQ @ 00:01:12])']]}},
              {'heading': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ["The SDE build follows a repeatable sequence. Quiet Light's method strips "
                              'non-cash expenses like amortization and depreciation plus taxes and '
                              "interest, then owner benefits such as salary and home office, 'because how "
                              "much you pay yourself is entirely up to you,' then true one-time expenses "
                              'like building an app, then situational adjustments [R4jvbLHhCBg @ '
                              '00:01:14]. Nate Lind starts at the top line: gross sales minus chargebacks '
                              'and refunds, COGS, SG&A and non-operating income such as PPP or EIDL money '
                              'and lawsuit settlements [yaZZzBKh86I @ 00:01:39]. Lind then allows '
                              'depreciation, interest and amortization, one-time website retrofits, the '
                              '2021 freight-cost delta and recruiter fees as add-backs [yaZZzBKh86I @ '
                              '00:04:01]. Tyler Jeffcoat of Seller Accountant runs trailing-twelve-month '
                              'SDE off an accrual-basis P&L, walking $1M in sales, $340K gross profit and '
                              "$100K operating profit to $185K of SDE [jkHzL8ya984 @ 00:06:26]. Jeffcoat's "
                              'filter: unused rent, owner salary and a VA come back; core tools like a '
                              "Skubana ERP and core contractors stay in, because 'you win every ad back "
                              "battle that you don't have to have' [jkHzL8ya984 @ 00:05:06]. Brent Freeman "
                              'of the CBB Group shows the stack on a real P&L: $924K plus $15K interest, '
                              '$40K depreciation and $210K owner comp yields $1.189M of SDE [pzqh4R8Hppk @ '
                              '00:04:53].',
                              'With normalized earnings locked in, the multiple grid is remarkably well '
                              'mapped. Campbell runs Main Street SDE at 2-3.5x off comps and industry '
                              'datasets, stacking $150K net, $100K owner pay and $50K add-backs into $300K '
                              'of SDE that lands near $825K at about 2.75x, while nudging the multiple to '
                              '3.25x adds $150K [ggUaT-lHV0A @ 00:05:06]. Keira Hamilton quotes a typical '
                              '3-5x, with $500K of SDE at 4x producing $2M [1dJeO4qEAhU @ 00:01:28]. '
                              'Petropoulos, whose Hillview Partners serves $1M-$20M EBITDA companies, maps '
                              'the institutional ladder: $500K-$1M of EBITDA at 3-5x, $1-3M revised up to '
                              '5-9x, $3-5M at 6-9x with many $3M companies trading at 7-8x, $5-10M at '
                              '6-10x, and above $10M at 12x, with 15x and 20x printed in frothy markets '
                              '[D58oCe_7BBM @ 00:04:07]. The arbitrage math explains PE appetite: buy ten '
                              '$1M-EBITDA companies at 6x for $60M, then sell the combined $10M of EBITDA '
                              'at 10x for $100M [D58oCe_7BBM @ 00:08:00]. Newell values sub-$1M-ARR SaaS '
                              'on SDE at 3-5x, so a $500K-ARR product throwing off $200K of profit prices '
                              'at $600K-$1M [oJsHo5vaDus @ 00:10:22]. With the median near 4x [oJsHo5vaDus '
                              '@ 00:13:41], every $50K of add-backs is worth $200K of price, which is why '
                              'the add-back fight matters so much [oJsHo5vaDus @ 00:12:36].',
                              "The financing desk then decides whether the price survives. Deal Street's "
                              'financing breakdown sets SBA 7(a) loans at up to $5M covering as much as '
                              '90% of goodwill, a buyer injection of at least 10% that cannot be borrowed '
                              '[a5Z--B3Uhrg @ 00:02:23], a 1.25 minimum DSCR as of October 1, 2026, no '
                              'projections counted toward DSCR, and an independent QoE on deals of '
                              '$3M-plus [a5Z--B3Uhrg @ 00:03:08]. Campbell defines DSCR as cash flow plus '
                              'owner salary divided by annual debt service, warning that if the price is '
                              "so high that cash flow can't comfortably support the debt, the deal won't "
                              "get financed [ggUaT-lHV0A @ 00:12:46]. Freeman's live structure: $3M price, "
                              '15% or $450K down, a $2.55M SBA loan over 10 years at 8.5% for $31,616 a '
                              'month, producing 2.25:1 coverage with $150K of owner comp and 1.92:1 on a '
                              'modified basis that charges a 20% return on the down payment, $7,500 a '
                              'month [pzqh4R8Hppk @ 00:12:28]. Seller notes fill the gap at 10-20% of '
                              'price over 3-7 years, often amortized over 10-plus years with a 3-5 year '
                              "balloon [a5Z--B3Uhrg @ 00:05:13]; a note funding the buyer's down payment "
                              "sits on full standby for the SBA loan's life [a5Z--B3Uhrg @ 00:06:31] and "
                              'can cover at most half that injection [a5Z--B3Uhrg @ 00:07:20].'],
               'table': {'caption': 'Street numbers for building earnings, setting multiples and financing '
                                    'the deal',
                         'headers': ['Mechanic', 'Exact Numbers Stated', 'Execution Note', 'Expert Source'],
                         'rows': [['Owner-operator SDE build and Main Street multiple',
                                   '$150K net + $100K owner pay + $50K add-backs = $300K SDE at 2-3.5x',
                                   'Moving the multiple from 2.75x to 3.25x adds $150K of price',
                                   'Deal Street - Small to Lower Middle Market M&A ([ggUaT-lHV0A @ '
                                   '00:05:06])'],
                                  ['E-commerce trailing-twelve-month SDE on accrual books',
                                   '$1M sales, $100K operating profit, $185K SDE, 2-4x with deals north of '
                                   '4x',
                                   'Leave core tools and core contractors in; add back a VA and unused '
                                   'rent',
                                   'Seller Accountant ([jkHzL8ya984 @ 00:06:26])'],
                                  ['Lower-middle-market EBITDA ladder by company size',
                                   '$500K-$1M at 3-5x, $1-3M at 5-9x, $5-10M at 6-10x, above $10M at 12x',
                                   'Many $3M EBITDA companies trade at 7-8x in practice',
                                   'Arthur Petropoulos ([D58oCe_7BBM @ 00:04:07])'],
                                  ['Sub-$1M ARR SaaS priced on SDE multiples',
                                   '$500K ARR with $200K profit at 3-5x equals $600K-$1M of value',
                                   'A $50K add-back difference at 4x moves price by $200K',
                                   'Quiet Light Brokerage ([oJsHo5vaDus @ 00:10:22])'],
                                  ['SBA 7(a) guardrails for acquisition loans',
                                   'Up to $5M, 90% of goodwill, 10% unborrowed injection, 1.25 DSCR '
                                   'minimum',
                                   'Projections no longer count toward DSCR; $3M-plus deals need an '
                                   'independent QoE',
                                   'Deal Street - Small to Lower Middle Market M&A ([a5Z--B3Uhrg @ '
                                   '00:02:23])'],
                                  ['Debt service coverage on a $3M acquisition',
                                   '$2.55M SBA loan at 8.5% over 10 years, $31,616 monthly, 2.25:1 DSCR',
                                   'Modified DSCR charging 20% on the $450K down payment drops to 1.92:1',
                                   'Brent Freeman  - The CBB Group ([pzqh4R8Hppk @ 00:12:28])'],
                                  ['Seller note sizing and amortization structure',
                                   '10-20% of price over 3-7 years, or 10-plus year amortization with 3-5 '
                                   'year balloon',
                                   'Notes funding the down payment go on full standby for the SBA term',
                                   'Deal Street - Small to Lower Middle Market M&A ([a5Z--B3Uhrg @ '
                                   '00:05:13])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Add-back and structure moves the brokers actually run',
                           'body': 'Small, documented adjustments compound through the multiple, and deal '
                                   'structure decides what the seller actually banks.',
                           'items': ['Apply a confirmed hosting cut retroactively: dropping from $8K to '
                                     '$4K a month credits $4K x 10 months, or $40K, to trailing earnings, '
                                     'and a one-time $10-15K website overhaul can be added back [Quiet '
                                     'Light Brokerage — oJsHo5vaDus @ 00:48:11].',
                                     'Pull PPP or EIDL money and lawsuit settlements out as non-operating '
                                     'income, then add back recruiter fees and the 2021 freight-cost delta '
                                     'as one-time items [Nate Lind - Business Broker and Beyond — '
                                     'yaZZzBKh86I @ 00:01:39].',
                                     'Shop lenders to the add-back schedule: SBA lenders vary in whether '
                                     'owner salary and depreciation come back in full, in part or not at '
                                     'all, so match the lender to the add-backs [Keira Hamilton — '
                                     '1dJeO4qEAhU @ 00:02:40].',
                                     'Use the seller-note trick of the trade: amortize over 10-plus years '
                                     'with a balloon at year 3-5 that usually gets refinanced [Deal Street '
                                     '- Small to Lower Middle Market M&A — a5Z--B3Uhrg @ 00:05:13].']},
               'sop_steps': [{'step': 1,
                              'title': 'Rebuild trailing earnings',
                              'action': 'Reconstruct trailing-twelve-month earnings on an accrual-basis '
                                        'P&L before touching add-backs.',
                              'detail': 'Start from gross sales, subtract chargebacks, refunds, COGS and '
                                        'SG&A, and strip non-operating income such as PPP/EIDL money and '
                                        'lawsuit settlements [Nate Lind - Business Broker and Beyond — '
                                        'yaZZzBKh86I @ 00:01:39]; run the result on TTM accrual books '
                                        '[Seller Accountant — jkHzL8ya984 @ 00:06:26].'},
                             {'step': 2,
                              'title': 'Layer defensible add-backs',
                              'action': 'Add back non-cash items, owner benefits, true one-time spend and '
                                        'situational adjustments only where documented.',
                              'detail': 'Follow the four-step SDE sequence of non-cash items, owner '
                                        'benefits, one-time expenses and situational adjustments [Quiet '
                                        'Light Brokerage — R4jvbLHhCBg @ 00:01:14]; expect lenders to '
                                        'reject meals, travel, car and entertainment and accept medical '
                                        'insurance only if documented [Brent Freeman  - The CBB Group — '
                                        'pzqh4R8Hppk @ 00:05:58].'},
                             {'step': 3,
                              'title': 'Pick the earnings measure and multiple band',
                              'action': 'Choose SDE, EBITDA or EBITDA minus capex by size and capital '
                                        'intensity, then place the business in its band.',
                              'detail': 'Use SDE below roughly $500K and EBITDA above it, with EBITDA '
                                        'minus capex for trucking-type firms [David C Barnett Small '
                                        'Business and Deal Making SMB — Va5USDqv3-A @ 00:03:34]; place '
                                        'EBITDA companies on the 3-5x to 12x size ladder [Arthur '
                                        'Petropoulos — D58oCe_7BBM @ 00:04:07].'},
                             {'step': 4,
                              'title': 'Stress-test price against the lender',
                              'action': 'Run DSCR on the proposed SBA structure before the number goes to '
                                        'market.',
                              'detail': 'Compute DSCR as cash flow plus owner salary over annual debt '
                                        'service against the 1.25 minimum [Deal Street - Small to Lower '
                                        'Middle Market M&A — ggUaT-lHV0A @ 00:11:50]; model the full '
                                        'structure the way Freeman did, a $3M price at 2.25:1 standard and '
                                        '1.92:1 modified coverage [Brent Freeman  - The CBB Group — '
                                        'pzqh4R8Hppk @ 00:12:28].'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The add-back fight is where brokers split hardest, and the split moves real '
                              'dollars. Shep Campbell at Deal Street adds back W-2 owner salary and '
                              "payroll taxes plus life insurance and family members' phones, vehicles and "
                              "health plans, yet refuses to add back the owner's personal vehicle, phone "
                              'or health insurance [ggUaT-lHV0A @ 00:02:25]. Ryan C. Winter runs the '
                              'opposite playbook: salary, interest, taxes, depreciation, one-time items '
                              'and the personal vehicle, phone and travel all go back in, and Winter '
                              'reports SDE often lands 40 to 50 percent above tax-return profit '
                              '[tPnDBaB9oPU @ 00:01:56]. Brent Freeman of the CBB Group says that inflated '
                              'number dies at the bank, because lenders treat tax returns as the source of '
                              'truth and refuse meals, travel, car and entertainment add-backs, accepting '
                              'medical insurance only when documented [pzqh4R8Hppk @ 00:05:58]. Nate Lind '
                              'splits the difference: travel, meals, personal auto and phone are generally '
                              'accepted, but SBA lenders rule on them case by case [yaZZzBKh86I @ '
                              '00:03:14]. The operator read: the aggressive schedule wins the listing '
                              'conversation, the conservative schedule wins the financing conversation, so '
                              'build both versions before quoting a seller any number at all.',
                              'Practitioners also disagree on where SDE stops and EBITDA starts, and on '
                              'which multiple belongs to each. David C Barnett uses SDE for owner-operated '
                              'firms under roughly $500K at about 2 to 2.2 times, lower for service firms, '
                              'switches to EBITDA above $500K, and moves capital-intensive operators like '
                              'trucking to EBIT or EBITDA minus capex [Va5USDqv3-A @ 00:03:34]. Brent '
                              'Freeman puts the switch at about $1M and above, noting the EBITDA multiple '
                              'is always higher [pzqh4R8Hppk @ 00:11:00]. Brett Cenkus ties the '
                              'owner-salary add-back to the $1 to 2M band, where buyers buy themselves a '
                              'job, and drops it near $20M because management stays on [y4u_MuL4xhw @ '
                              '00:05:11]. SaaS breaks the pattern entirely: David Newell at Quiet Light '
                              'values sub-$1M ARR deals on SDE, but over $1M ARR private equity and '
                              'strategic buyers price on revenue and will accept thin EBITDA if the '
                              'founder is out of the code, churn stays under 4 percent a month, and growth '
                              'runs 30 to 50 percent a year [oJsHo5vaDus @ 00:08:13]. Pick the earnings '
                              'metric first, because it decides which multiple band a seller is even '
                              'allowed to argue for, and which buyer pool will show up to the table.',
                              'Financing thresholds and pre-sale earnings tuning are the third fault line. '
                              'Deal Street states the SBA 7(a) minimum DSCR moved from 1.2 to 1.25, with '
                              'projections no longer allowed toward the ratio [a5Z--B3Uhrg @ 00:03:35]. '
                              'Brent Freeman says lenders want at least 1.5 in this interest rate '
                              'environment, and runs a modified DSCR that credits the buyer a 20 percent '
                              'return on the down payment, $7,500 a month, which drags a 2.25:1 deal down '
                              'to 1.92:1 [pzqh4R8Hppk @ 00:12:28]. On juicing the trailing twelve months, '
                              'the 2025 Quiet Light panel split live: Tom is very anti, while John '
                              'Hanstock says it depends, arguing that switching AWS to reserved pricing '
                              'and showing three months of savings can justify applying them across the '
                              'trailing 12 months [In6A5W0WFdY @ 00:34:26]. David Newell goes further, '
                              'applying a hosting cut from $8K to $4K a month retroactively, $4K times 10 '
                              'months, for a $40K adjustment, and treating a one-time $10 to 15K website '
                              'overhaul as an add-back [oJsHo5vaDus @ 00:48:11]. The split playbook: '
                              'underwrite to the 1.5 cushion and clean books when the deal needs bank '
                              'money, and save retroactive savings adjustments for the buyer who can '
                              "actually pay for them without a lender's sign-off."],
               'table': {'caption': 'Contested valuation calls: two playbooks side by side',
                         'headers': ['Contested Question', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [["Should the owner's personal perks count as add-backs?",
                                   'Campbell refuses personal vehicle, phone and health insurance but adds '
                                   'life insurance and family plans',
                                   'Winter adds back personal vehicle, phone and travel, lifting SDE 40 to '
                                   '50 percent over tax profit',
                                   'Deal Street - Small to Lower Middle Market M&A ([ggUaT-lHV0A @ '
                                   '00:02:25]); Ryan C. Winter, Business Broker ([tPnDBaB9oPU @ '
                                   '00:01:56])'],
                                  ['How much add-back tolerance does the lender give?',
                                   'Freeman: lenders disallow meals, travel, car and entertainment; '
                                   'medical only if documented',
                                   'Lind: travel, meals, auto and phone generally accepted, but SBA '
                                   'lenders decide case by case',
                                   'Brent Freeman  - The CBB Group ([pzqh4R8Hppk @ 00:05:58]); Nate Lind - '
                                   'Business Broker and Beyond ([yaZZzBKh86I @ 00:03:14])'],
                                  ['What debt service coverage ratio clears the bank?',
                                   'Deal Street: SBA minimum DSCR is 1.25, up from 1.2, with projections '
                                   'disallowed',
                                   'Freeman: lenders want at least 1.5 now; modified DSCR credits 20 '
                                   'percent down-payment return',
                                   'Deal Street - Small to Lower Middle Market M&A ([a5Z--B3Uhrg @ '
                                   '00:03:35]); Brent Freeman  - The CBB Group ([pzqh4R8Hppk @ 00:12:28])'],
                                  ['Where does SDE give way to EBITDA pricing?',
                                   'Barnett switches to EBITDA above roughly $500K and uses EBITDA minus '
                                   'capex for trucking',
                                   'Freeman switches at about $1M and up, where the EBITDA multiple is '
                                   'always higher',
                                   'David C Barnett Small Business and Deal Making SMB ([Va5USDqv3-A @ '
                                   '00:03:34]); Brent Freeman  - The CBB Group ([pzqh4R8Hppk @ 00:11:00])'],
                                  ['Should SaaS be priced on profit or on revenue?',
                                   'Newell: under $1M ARR is SDE-based at 3 to 5 times, median about 4 '
                                   'times',
                                   'Over $1M ARR goes revenue-based; niche high-retention SaaS quoted at 3 '
                                   'to 5 times revenue',
                                   'Quiet Light Brokerage ([oJsHo5vaDus @ 00:08:13]); Quiet Light '
                                   'Brokerage ([In6A5W0WFdY @ 00:29:51])'],
                                  ['Is it fair to juice trailing earnings before listing?',
                                   'Tom on the 2025 Quiet Light panel is very anti any juicing of earnings',
                                   'Hanstock says it depends: three months of AWS reserved savings can be '
                                   'applied to TTM',
                                   'Quiet Light Brokerage ([In6A5W0WFdY @ 00:33:55]); Quiet Light '
                                   'Brokerage ([In6A5W0WFdY @ 00:34:26])'],
                                  ['What counts as a cheap EBITDA multiple to buy?',
                                   'The PE and LBO rule of thumb calls anything under 6 times EBITDA cheap',
                                   'Damodaran uses the 20th percentile or first quartile, recalculated '
                                   'every single year instead',
                                   'Aswath Damodaran ([xI-KTlxfNDU @ 00:03:55]); Aswath Damodaran '
                                   '([xI-KTlxfNDU @ 00:05:03])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The most expensive failures start at the listing price. Shep Campbell at '
                              'Deal Street once listed a business at 3 times revenue, $15M on $5M of '
                              'revenue, roughly 10 times cash flow, and it never sold; the same broker '
                              'names selling into a downturn as mistake number two and warns that '
                              'add-back-everything schedules raise red flags with buyers [ggUaT-lHV0A @ '
                              '00:09:04]. Ryan C. Winter bans revenue rules of thumb outright and treats '
                              'one client at 50 percent of revenue as a red flag that drags the multiple '
                              'down [tPnDBaB9oPU @ 00:03:58]. Aswath Damodaran shows why cheap-looking '
                              'multiples trap buyers: the private equity rule that under 6 times EBITDA is '
                              'cheap would have flagged about 10,000 of roughly 40,000 global companies in '
                              '2013 and half of all companies in 2009, so the fix is the 20th percentile '
                              'or first quartile recalculated each year [xI-KTlxfNDU @ 00:04:12]. '
                              "Damodaran's Ryder System case, at 2.91 times, looked cheap but carried the "
                              'oldest fleet in the sector and would need debt to replace it [xI-KTlxfNDU @ '
                              '00:11:07]. The economics check is mismatch-hunting: a low multiple sitting '
                              'on old assets, high taxes or heavy reinvestment needs is usually priced '
                              'correctly, not a bargain waiting for a sharp buyer.',
                              'The second cluster of losses happens between handshake and funding. Brent '
                              'Freeman warns that a broker ends up selling the transaction three times, to '
                              'the buyer, the lender and the appraiser, and that lenders underwrite off '
                              'tax returns, so add-backs that cannot survive that review die at the bank; '
                              "Freeman's protection is a clawback through seller-note forgiveness if "
                              'add-backs prove false [pzqh4R8Hppk @ 00:07:41]. Deal Street adds the hard '
                              "SBA mechanics: a seller note funding the buyer's down payment goes on full "
                              'standby, with no payments or interest for the life of the SBA loan, and the '
                              'SBA will not finance earnouts at all [a5Z--B3Uhrg @ 00:06:31]. Keira '
                              'Hamilton reports SBA lenders vary on whether owner salary and depreciation '
                              'get added back in full, in part or not at all, so the lender has to match '
                              "the add-back schedule [1dJeO4qEAhU @ 00:02:40]. Deal Street's two-offer "
                              'comparison is the economics check: Offer A at $1.2M cash, a $500K note and '
                              'a $500K earnout loses to Offer B at $1.7M cash and a $200K note, which puts '
                              "$500K more in the seller's pocket on day one [a5Z--B3Uhrg @ 00:13:04]. "
                              'Price the structure, not the headline.',
                              'SaaS and concentration traps destroy value quietly. David Newell at Quiet '
                              'Light ranks key-man risk as mistake number one, calls lifetime plans '
                              'suicidal after one surfaced within 24 hours of due diligence, and lists '
                              'heavy discounting and halting development for more than 3 to 6 months as '
                              'value destroyers; the timing fix is to avoid selling exhausted or '
                              'mid-rebuild and aim for about six months after a major release [oJsHo5vaDus '
                              '@ 00:39:54]. On the 2025 Quiet Light panel, Tom walked away from a '
                              "custom-data contract worth about half a team member's salary because "
                              'one-off revenue is not worth anything to buyers, and flags COGS at 20 '
                              'percent as a possible misclassification signal against a target near 5 '
                              "percent [In6A5W0WFdY @ 00:17:52]. David C Barnett's concentration case, 60 "
                              'percent of revenue from four clients, gets handled with seller notes '
                              'subject to offset rather than a blunt price cut [Va5USDqv3-A @ 00:13:35]. '
                              'Brett Cenkus goes harder: a business living on two customers may be '
                              'unsellable or sold only at a discount [y4u_MuL4xhw @ 00:10:18]. Clean these '
                              'up before listing, because diligence finds them anyway.'],
               'table': {'caption': 'Firsthand traps and the economics check that catches each one',
                         'headers': ['Trap',
                                     'What Practitioners Reported',
                                     'Economics Check',
                                     'Expert Source'],
                         'rows': [['Listing the business on a revenue multiple',
                                   'Listed at 3 times revenue, $15M on $5M, roughly 10 times cash flow, '
                                   'and never sold',
                                   'Price off cash flow; Main Street SDE multiples quoted at 2 to 3.5 '
                                   'times',
                                   'Deal Street - Small to Lower Middle Market M&A ([ggUaT-lHV0A @ '
                                   '00:09:04])'],
                                  ['Fighting for weak add-backs in diligence',
                                   'Core tools like Skubana and core contractors are not add-backs; a VA '
                                   'and unused rent are',
                                   "You win every add back battle that you don't have to have",
                                   'Seller Accountant ([jkHzL8ya984 @ 00:05:06])'],
                                  ['Add-backs that collapse at the lender',
                                   'Lenders use tax returns as the source of truth and refuse meals, '
                                   'travel, car, entertainment',
                                   'Claw back through seller-note forgiveness if add-backs later prove '
                                   'false',
                                   'Brent Freeman  - The CBB Group ([pzqh4R8Hppk @ 00:07:41])'],
                                  ['Falling for the bigger headline offer',
                                   'Offer A: $1.2M cash, $500K note, $500K earnout versus Offer B: $1.7M '
                                   'cash, $200K note',
                                   "Offer B puts $500K more in the seller's pocket on day one",
                                   'Deal Street - Small to Lower Middle Market M&A ([a5Z--B3Uhrg @ '
                                   '00:13:04])'],
                                  ['Counting earnout dollars at full face value',
                                   'The SBA will not finance earnouts; a contingent seller note is the '
                                   'workaround',
                                   'Value every earnout dollar at a steep discount to cash at closing',
                                   'Deal Street - Small to Lower Middle Market M&A ([a5Z--B3Uhrg @ '
                                   '00:11:09])'],
                                  ['Lifetime plans and key-man risk in SaaS',
                                   'A lifetime plan surfaced within 24 hours of due diligence; called '
                                   'suicidal for value',
                                   'Get the founder out of the code and halt no development beyond 3 to 6 '
                                   'months',
                                   'Quiet Light Brokerage ([oJsHo5vaDus @ 00:39:54])'],
                                  ['Buying a cheap multiple that is a value trap',
                                   "Ryder System at 2.91 times looked cheap but had the sector's oldest "
                                   'fleet',
                                   'Check tax rate, reinvestment, return on capital and asset age for a '
                                   'mismatch',
                                   'Aswath Damodaran ([xI-KTlxfNDU @ 00:11:07])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Four checks before a number goes in front of a seller or buyer',
                           'body': 'Each gate below comes from a loss, a dead listing or a diligence '
                                   'blowup the practitioners reported. Clear all four before quoting price '
                                   'or signing a structure.',
                           'items': ['Refuse to list on a revenue multiple; a 3 times revenue listing at '
                                     'roughly 10 times cash flow never sold [Deal Street - Small to Lower '
                                     'Middle Market M&A — ggUaT-lHV0A @ 00:09:04].',
                                     "Run DSCR at the lender's current floor, at least 1.5 in this rate "
                                     'environment, and again with a 20 percent down-payment return before '
                                     'listing [Brent Freeman  - The CBB Group — pzqh4R8Hppk @ 00:12:28].',
                                     'Match the SBA lender to the add-back schedule, since lenders differ '
                                     'on owner salary and depreciation in full, in part or not at all '
                                     '[Keira Hamilton — 1dJeO4qEAhU @ 00:02:40].',
                                     'Kill lifetime plans, heavy discounting and founder dependence in the '
                                     'code before diligence opens, because they surface within 24 hours '
                                     '[Quiet Light Brokerage — oJsHo5vaDus @ 00:39:54].']}}],
 'pull_quote': '"Do not fall in love with the headline price." Deal Street - Small to Lower Middle Market '
               'M&A (a5Z--B3Uhrg @ 00:15:02).',
 'diagram_id': 'diag-02',
 'action_checklist': ['Build SDE from trailing-twelve-month figures on an accrual-basis P&L, not '
                      'cash-basis books [Seller Accountant — jkHzL8ya984 @ 00:06:26].',
                      'Strip non-operating income such as PPP and EIDL money and lawsuit settlements '
                      'before adding anything back [Nate Lind - Business Broker and Beyond — yaZZzBKh86I @ '
                      '00:01:39].',
                      'Pull comparables matched on industry, geography and revenue range from '
                      'bizbuysell.com, then add real estate and equipment and subtract assumed liabilities '
                      '[Brett Cenkus — y4u_MuL4xhw @ 00:06:24].',
                      'Cross-check the SDE multiple against EBITDA net of a fair wage: $150K SDE at 2 '
                      'times can equal 5 to 6 times EBITDA [David C Barnett Small Business and Deal Making '
                      'SMB — Va5USDqv3-A @ 00:09:56].',
                      'Structure seller notes at 10 to 20 percent of price, amortized over 10-plus years '
                      'with a 3 to 5 year balloon, backed by credit check, personal guarantee and security '
                      'interest [Deal Street - Small to Lower Middle Market M&A — a5Z--B3Uhrg @ 00:05:13].',
                      'Map the EBITDA band to its buyer pool and multiple, $1 to 3M at 5 to 9 times, and '
                      'pitch PE platforms and search funds accordingly [Arthur Petropoulos — D58oCe_7BBM @ '
                      '00:04:36].'],
 'statutory_citations': [{'title': 'Deal Street - Small to Lower Middle Market M&A — How Business Sales '
                                   'Get Financed (Cash, SBA Loans, Seller Notes, Earnouts & Rollovers) '
                                   '[00:13:04]',
                          'url': 'https://www.youtube.com/watch?v=a5Z--B3Uhrg&t=784s',
                          'relevance': 'Primary practitioner testimony on comparing cash-at-close, seller '
                                       'notes and earnouts across competing offers.'},
                         {'title': 'Brent Freeman  - The CBB Group — Net Profit is not Cash Flow - EBITDA '
                                   'or SDE!  Buying a Business and SBA. [00:12:28]',
                          'url': 'https://www.youtube.com/watch?v=pzqh4R8Hppk&t=748s',
                          'relevance': 'Primary practitioner testimony on SBA deal math, DSCR thresholds '
                                       'and modified DSCR.'},
                         {'title': 'Deal Street - Small to Lower Middle Market M&A — How Much Is My '
                                   'Business Really Worth? (How Buyers, Lenders & Brokers Value Small '
                                   'Businesses) [00:09:04]',
                          'url': 'https://www.youtube.com/watch?v=ggUaT-lHV0A&t=544s',
                          'relevance': 'Primary practitioner testimony on owner pricing myths and a '
                                       'revenue-multiple listing that never sold.'},
                         {'title': 'Quiet Light Brokerage — 3 Big Levers to Maximize SaaS Business '
                                   'Valuation with David Newell [00:39:54]',
                          'url': 'https://www.youtube.com/watch?v=oJsHo5vaDus&t=2394s',
                          'relevance': 'Primary practitioner testimony on SaaS value destroyers surfaced '
                                       'in due diligence.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'ggUaT-lHV0A',
                       'title': 'How Much Is My Business Really Worth? (How Buyers, Lenders & Brokers '
                                'Value Small Businesses)',
                       'channel': 'Deal Street - Small to Lower Middle Market M&A',
                       'author': 'Deal Street - Small to Lower Middle Market M&A',
                       'text': 'Value rests on earnings, multiple and risk, and buyers buy cash flow, not '
                               'revenue.',
                       'tip': 'Value rests on earnings, multiple and risk, and buyers buy cash flow, not '
                              'revenue.',
                       'timestamp': 68,
                       'timestamp_seconds': 68,
                       'timestamp_label': '[00:01:08]',
                       'url': 'https://www.youtube.com/watch?v=ggUaT-lHV0A&t=68s',
                       'markdown': '[00:01:08](https://www.youtube.com/watch?v=ggUaT-lHV0A&t=68s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'oJsHo5vaDus',
                       'title': '3 Big Levers to Maximize SaaS Business Valuation with David Newell',
                       'channel': 'Quiet Light Brokerage',
                       'author': 'Quiet Light Brokerage',
                       'text': 'Lifetime plans are suicidal for a SaaS valuation, and one surfaced within '
                               '24 hours of due diligence.',
                       'tip': 'Lifetime plans are suicidal for a SaaS valuation, and one surfaced within '
                              '24 hours of due diligence.',
                       'timestamp': 2394,
                       'timestamp_seconds': 2394,
                       'timestamp_label': '[00:39:54]',
                       'url': 'https://www.youtube.com/watch?v=oJsHo5vaDus&t=2394s',
                       'markdown': '[00:39:54](https://www.youtube.com/watch?v=oJsHo5vaDus&t=2394s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'jkHzL8ya984',
                       'title': 'Valuing Your E-Commerce Business: SDE, Add-backs, and Multiples',
                       'channel': 'Seller Accountant',
                       'author': 'Seller Accountant',
                       'text': "You win every add back battle that you don't have to have.",
                       'tip': "You win every add back battle that you don't have to have.",
                       'timestamp': 306,
                       'timestamp_seconds': 306,
                       'timestamp_label': '[00:05:06]',
                       'url': 'https://www.youtube.com/watch?v=jkHzL8ya984&t=306s',
                       'markdown': '[00:05:06](https://www.youtube.com/watch?v=jkHzL8ya984&t=306s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'brFD1fFAYhQ',
                       'title': 'EBITDA Multiples and Valuation Ranges: How Companies are Valued',
                       'channel': 'Arthur Petropoulos',
                       'author': 'Arthur Petropoulos',
                       'text': 'Companies with $400K to $1M of EBITDA trade at 4 to 6 times, and $1 to 2M '
                               'of EBITDA trades at 5 to 8 times.',
                       'tip': 'Companies with $400K to $1M of EBITDA trade at 4 to 6 times, and $1 to 2M '
                              'of EBITDA trades at 5 to 8 times.',
                       'timestamp': 199,
                       'timestamp_seconds': 199,
                       'timestamp_label': '[00:03:19]',
                       'url': 'https://www.youtube.com/watch?v=brFD1fFAYhQ&t=199s',
                       'markdown': '[00:03:19](https://www.youtube.com/watch?v=brFD1fFAYhQ&t=199s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '1dJeO4qEAhU',
                       'title': "What is Seller's Discretionary Earnings (SDE)? And Why Does it Matter?",
                       'channel': 'Keira Hamilton',
                       'author': 'Keira Hamilton',
                       'text': 'SBA lenders vary on whether they add back owner salary and depreciation in '
                               'full, in part or not at all, so match the lender to the add-backs.',
                       'tip': 'SBA lenders vary on whether they add back owner salary and depreciation in '
                              'full, in part or not at all, so match the lender to the add-backs.',
                       'timestamp': 160,
                       'timestamp_seconds': 160,
                       'timestamp_label': '[00:02:40]',
                       'url': 'https://www.youtube.com/watch?v=1dJeO4qEAhU&t=160s',
                       'markdown': '[00:02:40](https://www.youtube.com/watch?v=1dJeO4qEAhU&t=160s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Va5USDqv3-A',
                       'title': 'What Number Do I Multiply? SDE, EBIT, EBITDA?',
                       'channel': 'David C Barnett Small Business and Deal Making SMB',
                       'author': 'David C Barnett Small Business and Deal Making SMB',
                       'text': 'Valuation is not like engineering; the methods are a toolkit.',
                       'tip': 'Valuation is not like engineering; the methods are a toolkit.',
                       'timestamp': 84,
                       'timestamp_seconds': 84,
                       'timestamp_label': '[00:01:24]',
                       'url': 'https://www.youtube.com/watch?v=Va5USDqv3-A&t=84s',
                       'markdown': '[00:01:24](https://www.youtube.com/watch?v=Va5USDqv3-A&t=84s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'RoGz5NZF96I',
                       'title': 'SDE v EBITDA.  Essential for Accurate Business Valuation.',
                       'channel': 'Peter Nola',
                       'author': 'Peter Nola',
                       'text': 'A bakery with $100K of profit, a $50K owner salary and a $10K car produces '
                               '$160K of SDE.',
                       'tip': 'A bakery with $100K of profit, a $50K owner salary and a $10K car produces '
                              '$160K of SDE.',
                       'timestamp': 76,
                       'timestamp_seconds': 76,
                       'timestamp_label': '[00:01:16]',
                       'url': 'https://www.youtube.com/watch?v=RoGz5NZF96I&t=76s',
                       'markdown': '[00:01:16](https://www.youtube.com/watch?v=RoGz5NZF96I&t=76s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'pzqh4R8Hppk',
                       'title': 'Net Profit is not Cash Flow - EBITDA or SDE!  Buying a Business and SBA.',
                       'channel': 'Brent Freeman  - The CBB Group',
                       'author': 'Brent Freeman  - The CBB Group',
                       'text': 'Lenders use tax returns as the source of truth, and you end up selling the '
                               'transaction three times.',
                       'tip': 'Lenders use tax returns as the source of truth, and you end up selling the '
                              'transaction three times.',
                       'timestamp': 358,
                       'timestamp_seconds': 358,
                       'timestamp_label': '[00:05:58]',
                       'url': 'https://www.youtube.com/watch?v=pzqh4R8Hppk&t=358s',
                       'markdown': '[00:05:58](https://www.youtube.com/watch?v=pzqh4R8Hppk&t=358s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'tPnDBaB9oPU',
                       'title': 'How to Value a Business: SDE, Multiples & Add-Backs',
                       'channel': 'Ryan C. Winter, Business Broker',
                       'author': 'Ryan C. Winter, Business Broker',
                       'text': 'Do not use revenue rules of thumb to value a business.',
                       'tip': 'Do not use revenue rules of thumb to value a business.',
                       'timestamp': 238,
                       'timestamp_seconds': 238,
                       'timestamp_label': '[00:03:58]',
                       'url': 'https://www.youtube.com/watch?v=tPnDBaB9oPU&t=238s',
                       'markdown': '[00:03:58](https://www.youtube.com/watch?v=tPnDBaB9oPU&t=238s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'yaZZzBKh86I',
                       'title': "Business Valuation - Part 5 - How to Calculate Seller's Discretionary "
                                'Earnings',
                       'channel': 'Nate Lind - Business Broker and Beyond',
                       'author': 'Nate Lind - Business Broker and Beyond',
                       'text': 'Travel, meals, personal auto and phone are generally accepted add-backs, '
                               'but SBA lenders treat them case by case.',
                       'tip': 'Travel, meals, personal auto and phone are generally accepted add-backs, '
                              'but SBA lenders treat them case by case.',
                       'timestamp': 194,
                       'timestamp_seconds': 194,
                       'timestamp_label': '[00:03:14]',
                       'url': 'https://www.youtube.com/watch?v=yaZZzBKh86I&t=194s',
                       'markdown': '[00:03:14](https://www.youtube.com/watch?v=yaZZzBKh86I&t=194s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'xI-KTlxfNDU',
                       'title': 'Session 16: Other Earnings Multiples',
                       'channel': 'Aswath Damodaran',
                       'author': 'Aswath Damodaran',
                       'text': "Again, what you're looking for is a mismatch.",
                       'tip': "Again, what you're looking for is a mismatch.",
                       'timestamp': 605,
                       'timestamp_seconds': 605,
                       'timestamp_label': '[00:10:05]',
                       'url': 'https://www.youtube.com/watch?v=xI-KTlxfNDU&t=605s',
                       'markdown': '[00:10:05](https://www.youtube.com/watch?v=xI-KTlxfNDU&t=605s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'R4jvbLHhCBg',
                       'title': 'What Is Seller’s Discretionary Earnings or SDE (and How to Calculate It)',
                       'channel': 'Quiet Light Brokerage',
                       'author': 'Quiet Light Brokerage',
                       'text': "You see, your business's value is based on a multiple of your earnings.",
                       'tip': "You see, your business's value is based on a multiple of your earnings.",
                       'timestamp': 26,
                       'timestamp_seconds': 26,
                       'timestamp_label': '[00:00:26]',
                       'url': 'https://www.youtube.com/watch?v=R4jvbLHhCBg&t=26s',
                       'markdown': '[00:00:26](https://www.youtube.com/watch?v=R4jvbLHhCBg&t=26s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'D58oCe_7BBM',
                       'title': 'The EBITDA Multiple Valuation Spectrum all Acquirers Use',
                       'channel': 'Arthur Petropoulos',
                       'author': 'Arthur Petropoulos',
                       'text': 'That is the magic words for enhancing value.',
                       'tip': 'That is the magic words for enhancing value.',
                       'timestamp': 816,
                       'timestamp_seconds': 816,
                       'timestamp_label': '[00:13:36]',
                       'url': 'https://www.youtube.com/watch?v=D58oCe_7BBM&t=816s',
                       'markdown': '[00:13:36](https://www.youtube.com/watch?v=D58oCe_7BBM&t=816s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'y4u_MuL4xhw',
                       'title': 'How To Value a Business for Sale (Mergers and Acquisitions)',
                       'channel': 'Brett Cenkus',
                       'author': 'Brett Cenkus',
                       'text': 'At this market level comparable transaction analysis reigned supreme over '
                               'DCF and public comparables.',
                       'tip': 'At this market level comparable transaction analysis reigned supreme over '
                              'DCF and public comparables.',
                       'timestamp': 106,
                       'timestamp_seconds': 106,
                       'timestamp_label': '[00:01:46]',
                       'url': 'https://www.youtube.com/watch?v=y4u_MuL4xhw&t=106s',
                       'markdown': '[00:01:46](https://www.youtube.com/watch?v=y4u_MuL4xhw&t=106s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'a5Z--B3Uhrg',
                       'title': 'How Business Sales Get Financed (Cash, SBA Loans, Seller Notes, Earnouts '
                                '& Rollovers)',
                       'channel': 'Deal Street - Small to Lower Middle Market M&A',
                       'author': 'Deal Street - Small to Lower Middle Market M&A',
                       'text': 'A seller note is a loan.',
                       'tip': 'A seller note is a loan.',
                       'timestamp': 487,
                       'timestamp_seconds': 487,
                       'timestamp_label': '[00:08:07]',
                       'url': 'https://www.youtube.com/watch?v=a5Z--B3Uhrg&t=487s',
                       'markdown': '[00:08:07](https://www.youtube.com/watch?v=a5Z--B3Uhrg&t=487s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'a5Z--B3Uhrg',
                       'title': 'How Business Sales Get Financed (Cash, SBA Loans, Seller Notes, Earnouts '
                                '& Rollovers)',
                       'channel': 'Deal Street - Small to Lower Middle Market M&A',
                       'author': 'Deal Street - Small to Lower Middle Market M&A',
                       'text': 'Do not fall in love with the headline price.',
                       'tip': 'Do not fall in love with the headline price.',
                       'timestamp': 902,
                       'timestamp_seconds': 902,
                       'timestamp_label': '[00:15:02]',
                       'url': 'https://www.youtube.com/watch?v=a5Z--B3Uhrg&t=902s',
                       'markdown': '[00:15:02](https://www.youtube.com/watch?v=a5Z--B3Uhrg&t=902s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'In6A5W0WFdY',
                       'title': 'The State of SaaS in 2025: Multiples, Growth Strategies, Valuations, & '
                                'Exit Planning',
                       'channel': 'Quiet Light Brokerage',
                       'author': 'Quiet Light Brokerage',
                       'text': 'One-off custom revenue is not worth anything to buyers, so a contract '
                               "worth about half a team member's salary was dropped.",
                       'tip': 'One-off custom revenue is not worth anything to buyers, so a contract worth '
                              "about half a team member's salary was dropped.",
                       'timestamp': 1072,
                       'timestamp_seconds': 1072,
                       'timestamp_label': '[00:17:52]',
                       'url': 'https://www.youtube.com/watch?v=In6A5W0WFdY&t=1072s',
                       'markdown': '[00:17:52](https://www.youtube.com/watch?v=In6A5W0WFdY&t=1072s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'}]}
