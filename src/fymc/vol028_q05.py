from __future__ import annotations

CHAPTER_5 = {'id': 'Q5',
 'chapter_id': 'Q5',
 'chapter_number': 5,
 'question_number': 5,
 'slug': 'worked-bids-and-pricing-calculators',
 'question_prompt': 'How do I run real numbers on a specific building, and which calculators and '
                    'worksheets help me price it without losing money?',
 'kicker': 'Q5 / THE BIG MONEY PLAYBOOKS',
 'title': 'Worked Bids and Pricing Calculators',
 'subtitle': '2,400, 3,500, 10,000, 20,000 and 30,000 sq ft worked examples, first-office bid worksheets, '
             'Janibid, BizAlmighty, Google Sheets and CleanFirst calculators, house-cleaning math, and '
             'cash flow and margin expensing',
 'layout_template': 'case_study',
 'reading_time_minutes': 15,
 'executive_summary': 'Every operator here prices commercial cleaning from labor hours, not square '
                      'footage. The method is consistent: walk the building, then convert footage and '
                      'fixture counts into hours using production rates of 2,500 to 4,000 square feet an '
                      'hour and about 3 minutes per fixture. Load the wage with a 25% payroll burden or '
                      'itemized liabilities, and add supplies, equipment, and overhead. Then divide by one '
                      'minus the target margin and multiply by 4.33 weeks. Worked bids run from a 2,400 '
                      'square foot office at $325 a month to a 30,000 square foot building at $5,165. The '
                      'disagreements are over margin and minimums. Commercial Cleaning CEO scales margin '
                      'from 45% down to 35% as weekly hours rise, and Clean Proposals demands at least '
                      '30%. Solo Business Systems marks up 25% on cost, and Channel Zero Marketing sets a '
                      '$65 floor on small visits regardless of what the hourly math says.',
 'key_metrics': [{'label': 'True Hourly Cost of a $15 Cleaner',
                  'metric': 'True Hourly Cost of a $15 Cleaner',
                  'value': '$17.71 per hour',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Matt's calculator stacks payroll liabilities (state and federal "
                             'unemployment, FICA, workers comp) on a $15 wage; the result drives every '
                             'later step of the bid.',
                  'source': 'Commercial Cleaning CEO ([IMbK5m7qbY0 @ 00:04:42])'},
                 {'label': 'Margin Collapse From One Extra Worker Hour',
                  'metric': 'Margin Collapse From One Extra Worker Hour',
                  'value': '25% falls to about 13.4%',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'On a 20,000 square foot, three-visit-a-week model priced at $2,800, going '
                             'from five to six worker hours per visit raises cost to $2,425 and leaves '
                             'only $375 of profit.',
                  'source': 'Bid & Profit Lab ([T-l3Df3Iino @ 00:04:10])'},
                 {'label': 'Annual Revenue Lost Using 4 Weeks Instead of 4.33',
                  'metric': 'Annual Revenue Lost Using 4 Weeks Instead of 4.33',
                  'value': 'About $516 per year',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'A $65, twice-weekly visit prices at $520 a month using 4 weeks versus $563 '
                             'using 4.33, which amounts to practically a free month for the client.',
                  'source': 'Channel Zero Marketing ([Ey7iPjW1uZQ @ 00:13:44])'},
                 {'label': '10,000 Sq Ft Five-Night Office Bid',
                  'metric': '10,000 Sq Ft Five-Night Office Bid',
                  'value': '$2,650 cost / 0.75 = about $3,530, rounded to roughly $3,600 per month',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'The cost covers 86.6 labor hours at a $22.50 loaded rate, plus $225 '
                             'supplies, $125 equipment wear, and $350 overhead, priced for a 25% margin.',
                  'source': 'Janitorial Empire ([PmZvMyhPjCM @ 00:03:49])'}],
 'sections': [{'heading': 'The Practitioner Consensus',
               'paragraphs': ['Every operator who builds bids for a living starts from the same anchor: '
                              'labor hours, not square footage. Matt of Commercial Cleaning CEO scaled a '
                              'company past a million dollars a year in under five years. Matt says flat '
                              'rates like 20 or 25 cents a square foot are not the safest or most accurate '
                              'route, because markets pay different wages and facilities carry different '
                              'densities of desks, toilets, and offices [IMbK5m7qbY0 @ 00:01:50]. Scott at '
                              'Channel Zero Marketing had Claude AI scrape 1,900 posts from cleaning '
                              'communities. One 3,500 square foot office drew answers from $750 to $3,000 '
                              'a month for the same building. The verdict: labor hours set the price, and '
                              'square footage alone cannot [Ey7iPjW1uZQ @ 00:04:06]. The Janitorial Store '
                              'goes further. Per-square-foot math only behaves on buildings of 10,000 '
                              'square feet or more cleaned five days a week, or once you have tracked your '
                              'own locations long enough to set your own price points [Cf4hKGN0mXg @ '
                              '00:02:06]. Solo Business Systems calls a published per-foot figure a '
                              'comparison tool, nothing more. Multiplying a 5 to 20 cent rate across their '
                              '5,000 square foot benchmark produces a fantasy number of $250 to $1,000 per '
                              'visit [hf0U17FyA58 @ 00:06:53].',
                              'The second point of agreement is that the wage on the job ad is not your '
                              'cost. Commercial Cleaning CEO builds true hourly cost from the average '
                              'market starting pay plus 10% to attract better people, then stacks payroll '
                              'liabilities on top. Payroll liabilities, per Matt, cover payroll taxes, '
                              'state and federal unemployment insurance, and workers comp. In Asheville, '
                              '$13 became $14.30, and roughly 14.1% in liabilities brought it to $16.32 an '
                              'hour [598Td1ks52Y @ 00:05:44]. Janitorial Empire calls stopping at the wage '
                              'the first major mistake. Their bid loads an $18 cleaner with a 25% burden '
                              'to reach $22.50 per true hour [PmZvMyhPjCM @ 00:01:49]. Bid & Profit Lab '
                              'applies the same 25% burden to a $20 wage for a $25 loaded rate. They add '
                              'that if you clean the account yourself, leaving your own labor out makes '
                              'the job look more profitable than it is [T-l3Df3Iino @ 00:02:54]. Clean '
                              'Proposals turns the principle into a slogan: bid like the company you want '
                              'to be, never like the company you are. That means payroll taxes, insurance, '
                              'and overhead go into every proposal even when the owner holds the mop. '
                              'Inspectors, trainers, turnover cost, front-line custodians paid well with '
                              'adequate cleaning times, and a cell phone line belong there too '
                              '[0OZkOVSBE1c @ 00:00:15].',
                              'Third, price equals cost divided by one minus the target margin, and a '
                              'month is 4.33 weeks. Bid & Profit Lab shows why the division matters. '
                              'Dividing $2,100 of cost by 0.75 gives $2,800 and a true 25% margin. Adding '
                              '25% on top of cost yields $2,625 and only a 20% margin, because markup is '
                              'measured against cost and margin against revenue [T-l3Df3Iino @ 00:03:15]. '
                              'Janitorial Empire repeats the warning in their 10,000 square foot bid, '
                              'dividing $2,650 by 0.75 instead of stacking 25% on top [PmZvMyhPjCM @ '
                              '00:03:30]. On frequency, Channel Zero Marketing insists on 4.33 rather than '
                              '4, because two months a year carry an extra week. On a $65 visit twice '
                              'weekly, 4 weeks gives $520 a month against $563 at 4.33, which hands back '
                              'roughly $516 a year [Ey7iPjW1uZQ @ 00:13:44]. Commercial Cleaning CEO uses '
                              'the same multiplier, or the equivalent of multiplying by 52 weeks and '
                              'dividing by 12 months [598Td1ks52Y @ 00:09:35]. All of these operators also '
                              'refuse to quote blind: no walkthrough, no fixture count, no floor type, no '
                              'bid. Scott says flatly that without square footage, density, fixture '
                              'counts, floor type, and pictures, there is nothing to build a bid on.'],
               'table': {'caption': 'Consensus pricing rules shared across the practitioners who publish '
                                    'worked bids',
                         'headers': ['Consensus Rule',
                                     'What Practitioners Actually Do',
                                     'Why It Protects the Bid',
                                     'Expert Source'],
                         'rows': [['Price from labor hours, never from square footage alone',
                                   'Count desks, toilets, sinks, and glass faces to infer cleaning time',
                                   'Markets and facility densities differ, so flat cents-per-foot rates '
                                   'misprice buildings',
                                   'Commercial Cleaning CEO ([IMbK5m7qbY0 @ 00:01:50])'],
                                  ['Load the wage with payroll burden before any pricing',
                                   'Multiply an $18 wage by a 25% burden for $22.50 true cost',
                                   'Stopping at the hourly wage is the first major bidding mistake',
                                   'Janitorial Empire ([PmZvMyhPjCM @ 00:01:49])'],
                                  ['Divide total cost by one minus the target margin',
                                   'Divide $2,100 monthly cost by 0.75 to reach a $2,800 price',
                                   'Adding 25% to cost only produces a 20% margin on revenue',
                                   'Bid & Profit Lab ([T-l3Df3Iino @ 00:03:33])'],
                                  ['Use 4.33 weeks per month, never a flat four weeks',
                                   'Multiply per-visit price by visits per week, then by 4.33',
                                   'Using four weeks forfeits about $516 a year on a $563 account',
                                   'Channel Zero Marketing ([Ey7iPjW1uZQ @ 00:13:44])'],
                                  ['Walk every building before writing a single number down',
                                   'Measure cleanable footage, count fixtures, log floors, and confirm '
                                   'access and consumables',
                                   'Bidding from the parking lot means pricing a building you never saw',
                                   'Solo Business Systems ([hf0U17FyA58 @ 00:04:20])'],
                                  ['Set a per-visit minimum that covers the drive and setup',
                                   'Apply a $65 per-visit floor even when the hourly math says $44',
                                   'Gas, setup, hauling equipment, and washing towels eat tiny accounts '
                                   'alive',
                                   'Channel Zero Marketing ([Ey7iPjW1uZQ @ 00:12:38])'],
                                  ['Expense every hidden operating cost into each proposal',
                                   'Include payroll taxes, insurance, overhead, inspectors, trainers, '
                                   'turnover, and phones',
                                   'Two unbudgeted turnovers a year drain $80 monthly straight from cash '
                                   'flow',
                                   'Clean Proposals ([0OZkOVSBE1c @ 00:02:03])']]}},
              {'heading': 'Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['Time estimates come from production rates, and these operators publish '
                              "theirs. Commercial Cleaning CEO's calculator infers minutes from what the "
                              'walkthrough counts. It allows 0.75 minutes per desk and about 3 minutes per '
                              'toilet, and counts glass faces per side of each entry or reception pane. '
                              'Floors are priced separately at about 7,000 square feet an hour for carpet, '
                              'and slower for hard floor that must be swept and then mopped [IMbK5m7qbY0 @ '
                              '00:10:33]. Matt also shaves 10 to 20% off the wall-to-wall measurement for '
                              'walls and fixed furniture, turning 10,000 measured feet into 8,500 '
                              'cleanable feet. Matt blames chronic overbidding on skipping that cut. The '
                              'office range on the CEO chart runs 3,000 to 4,000 square feet an hour, '
                              'fastest when density and traffic are low [598Td1ks52Y @ 00:02:46]. Channel '
                              'Zero Marketing works from ISSA production rates: a blended 2,500 to 3,000 '
                              'square feet an hour for general office work, and 2.5 to 5 minutes per '
                              'restroom fixture. Tile pushes the rate down toward 2,500, because the floor '
                              'gets touched twice, once to dust mop and again to wet mop [Ey7iPjW1uZQ @ '
                              '00:06:17]. AJ Simmons defaults to 3,000 when the floor type is unknown, '
                              'about 4,000 for all carpet, and 2,000 to 2,500 for all hard floor '
                              '[cWVLz5abUAg @ 00:01:24].',
                              'Margin selection is where Commercial Cleaning CEO breaks from '
                              "flat-percentage shops. Matt's chart ties margin to weekly hours. An account "
                              'clocking 19.72 weekly hours falls in the 14-to-33-hour band and gets quoted '
                              'at 45% [IMbK5m7qbY0 @ 00:14:51]. Accounts above 66 weekly hours drop to '
                              '35%, because a $10,000 monthly account does not take twenty times the '
                              'management of a $500 one. The conversion is true hourly cost divided by one '
                              'minus margin: $16.32 divided by 0.65 equals $25.11 an hour to bill '
                              '[598Td1ks52Y @ 00:08:41]. For a fast quote straight off the walkthrough, '
                              'Matt skips the line items and multiplies $32.20 an hour by five nightly '
                              'hours, five nights, and 4.33 weeks, giving $3,485 a month [IMbK5m7qbY0 @ '
                              '00:18:52]. Supplies are set at 2 to 3% of the final price. Matt treats the '
                              'calculator output as a ballpark, then adjusts it using similar buildings '
                              'already quoted, such as one running 34 cents a square foot. True Trade '
                              "Cost's $49.95 spreadsheet works from the other end. It rolls insurance, "
                              'bonding, storage, phone, cleaners, and owner pay into a $36.15 rate that '
                              'every building hour must clear before profit. It then flags forgotten items '
                              'like keys, alarm codes, restock checks, and inspections in red [8lFhFbsEuDc '
                              '@ 00:01:49].',
                              "The cheapest tools on the street are free and fast. Janibid's janitorial "
                              'calculator takes hours, wage, frequency, supplies, and taxes and insurance, '
                              'then accepts profit as either dollars or a percentage. A two-hour job with '
                              '$250 of profit shows $300 of labor and $550 to the customer, labeled 83% '
                              'profit [9FeuDZZNdKI @ 00:01:15]. In the app version, a five-night job at '
                              '$20 an hour, with $25 of chemicals and $50 of taxes and insurance, costs '
                              '$941 a month. The Janibid host would push profit to at least $350 for a '
                              '$1,291 price and round it to $1,298. Roughly 700 people used the app in its '
                              'launch month [Q0_kmHGx6FI @ 00:02:35]. AJ Simmons runs the Calculated '
                              'Cleaning app on a 30,000 square foot, three-story building. AJ estimates 36 '
                              'fixtures from two restrooms per floor, drops to $21 an hour for a five-day '
                              'schedule, and rounds the estimate to $5,165 a month before pasting it into '
                              "the app's proposal builder, all from a phone in under 30 minutes "
                              '[cWVLz5abUAg @ 00:03:26]. Bid & Profit Lab ends every bid with a stress '
                              'test. On their 20,000 square foot model, one extra worker hour per visit '
                              'cuts margin from 25% to about 13.4%, nearly halving the profit [T-l3Df3Iino '
                              '@ 00:04:10].'],
               'table': {'caption': 'Worked commercial bids with the exact inputs and outputs each '
                                    'practitioner showed',
                         'headers': ['Worked Bid Scenario',
                                     'Inputs Used by the Practitioner',
                                     'Resulting Price Logic',
                                     'Expert Source'],
                         'rows': [['2,400 square foot office cleaned three nights weekly',
                                   '2,800 square feet an hour gives 0.85 hours, times 3, times 52, divided '
                                   'by 12',
                                   'About 13 monthly hours billed at $25 equals $325 a month',
                                   'The Janitorial Store ([Cf4hKGN0mXg @ 00:01:30])'],
                                  ['3,500 square foot first account cleaned twice weekly',
                                   '3,000 square feet an hour plus six fixtures at 3 minutes equals 1.47 '
                                   'hours',
                                   '$44 visit raised to a $65 minimum, giving $563 monthly at 4.33',
                                   'Channel Zero Marketing ([Ey7iPjW1uZQ @ 00:12:38])'],
                                  ['5,000 square foot professional office cleaned three nights weekly',
                                   '2,500 square feet an hour, 26 monthly hours at $25 loaded, plus $150 '
                                   'in extras',
                                   '$800 cost marked up 25% to a $1,000 monthly contract',
                                   'Solo Business Systems ([hf0U17FyA58 @ 00:06:15])'],
                                  ['10,000 square foot office cleaned five nights weekly',
                                   'Four hours per visit, 86.6 hours at $22.50, plus supplies, equipment, '
                                   'and overhead',
                                   '$2,650 cost divided by 0.75, rounded to about $3,600 a month',
                                   'Janitorial Empire ([PmZvMyhPjCM @ 00:04:11])'],
                                  ['20,000 cleanable square feet with three visits weekly',
                                   '4,000 square feet per worker hour, 65 hours at $25, plus $475 in '
                                   'allowances',
                                   '$2,100 cost divided by 0.75 equals a $2,800 monthly price',
                                   'Bid & Profit Lab ([T-l3Df3Iino @ 00:02:38])'],
                                  ['30,000 square foot three-story office cleaned five days weekly',
                                   '3,000 square feet an hour blended, 36 estimated fixtures, $21 hourly '
                                   'rate',
                                   'Calculated Cleaning app estimate rounded up to $5,165 per month',
                                   'AJ SIMMONS ([cWVLz5abUAg @ 00:03:26])'],
                                  ['6,000 square foot office cleaned three nights weekly',
                                   'Task minutes for trash, restrooms, and dusting against a $36.15 '
                                   'break-even hour',
                                   '$124.47 a night and $1,618.15 a month after markup and cushion',
                                   'True Trade Cost ([8lFhFbsEuDc @ 00:01:26])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Small moves the bid-builders use to stay accurate and win',
                           'body': 'These are the field habits the operators rely on when turning a '
                                   'walkthrough into a number that wins and still pays.',
                           'items': ['Count toilets and urinals as units, never bathrooms; one restroom '
                                     'can hold one stall or twenty, and the units are what take time '
                                     '[Commercial Cleaning CEO — IMbK5m7qbY0 @ 00:07:02].',
                                     'When you lose a bid, call and ask why as a new owner seeking '
                                     'feedback. Landing 40% below two closer bids scares buyers as much as '
                                     'pricing three times higher [Channel Zero Marketing — Ey7iPjW1uZQ @ '
                                     '00:20:31].',
                                     'Price the initial deep clean as a separate one-off line, and write '
                                     'in a clause that reopens the price when the client adds space or '
                                     'staff, because scope creep is the silent margin killer [Solo '
                                     'Business Systems — hf0U17FyA58 @ 00:08:15].',
                                     'Benchmark starting pay on Indeed or buy a PayScale market report for '
                                     'about $100 before setting the base wage in your formula [Commercial '
                                     'Cleaning CEO — 598Td1ks52Y @ 00:04:22].']},
               'sop_steps': [{'step': 1,
                              'title': 'Walk and measure the building',
                              'action': 'Measure cleanable square footage, count restroom fixtures, log '
                                        'floor types, and confirm access and consumables.',
                              'detail': 'Use the nine-point walkthrough and cost restrooms at roughly 3 '
                                        'minutes per fixture [Solo Business Systems — hf0U17FyA58 @ '
                                        '00:04:37]. Subtract 10 to 20% from the wall-to-wall measurement '
                                        'for walls and fixed furniture [Commercial Cleaning CEO — '
                                        'IMbK5m7qbY0 @ 00:10:01].'},
                             {'step': 2,
                              'title': 'Convert footage and fixtures into labor hours',
                              'action': 'Divide square footage by the production rate, add fixture '
                                        'minutes, and multiply by nights per week and 4.33.',
                              'detail': 'Divide square feet by the production rate for hours, multiply '
                                        'fixtures by three to five minutes for restroom time, then '
                                        'multiply by nights per week, labor rate, and 4.33. Practice until '
                                        'you can run it on the back of a napkin [Channel Zero Marketing — '
                                        'Ey7iPjW1uZQ @ 00:14:20].'},
                             {'step': 3,
                              'title': 'Build the full monthly cost',
                              'action': 'Load wages with payroll burden, then add supplies, equipment '
                                        'wear, travel, supervision, and overhead.',
                              'detail': 'Add $100 supplies, $75 equipment, $100 travel, $100 supervision, '
                                        'and $100 overhead on top of the $1,625 loaded labor for a $2,100 '
                                        'modeled cost [Bid & Profit Lab — T-l3Df3Iino @ 00:02:19]. '
                                        'Allocate a slice for insurance, vehicles, software, accounting, '
                                        'and management time [Janitorial Empire — PmZvMyhPjCM @ '
                                        '00:03:08].'},
                             {'step': 4,
                              'title': 'Price on margin and stress test',
                              'action': 'Divide cost by one minus target margin, check it against your '
                                        'minimum, then rerun with one extra worker hour per visit.',
                              'detail': 'The repeatable workflow is scope, labor, full cost, target '
                                        'margin, then a stress test before the quote goes out [Bid & '
                                        'Profit Lab — T-l3Df3Iino @ 00:04:26].'}]},
              {'heading': 'Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The sharpest split is whether a square-foot number has any place in the '
                              'bid. Matt at Commercial Cleaning CEO refuses to quote off a flat 20 or 25 '
                              'cents a foot because markets pay different wages and buildings carry '
                              'different densities, calling square-foot pricing neither the safest nor the '
                              'most accurate route [IMbK5m7qbY0 @ 00:02:05]. Yet the same calculator still '
                              'reports price per square foot monthly, and Matt uses it to clone a known '
                              'winner: one building ran at 34 cents a foot, so a near-identical building '
                              'starts there and moves up or down [IMbK5m7qbY0 @ 00:17:40]. The Janitorial '
                              'Store draws a hard line instead: square-foot pricing only works on '
                              'buildings of 10,000 square feet or more cleaned five days a week, or once '
                              'you have tracked your own locations long enough to set your own per-foot '
                              'price points [Cf4hKGN0mXg @ 00:02:06]. Solo Business Systems goes furthest, '
                              'treating published 5-to-20-cents-per-visit figures as a comparison tool '
                              'only, because multiplied blindly they turn a 5,000-square-foot office into '
                              '$250 to $1,000 a visit, a fantasy number, while signed small-office '
                              'contracts cluster around $700 to $2,800 a month [hf0U17FyA58 @ 00:06:53]. '
                              'The operator takeaway: build from hours, then use per-foot data only as a '
                              'sanity check against your own past bids.',
                              'Production rates swing just as hard, and each operator defends a different '
                              'default. Commercial Cleaning CEO runs an office band of 3,000 to 4,000 '
                              'square feet per hour, reserving the fast end for low density and low '
                              'traffic, and gauges traffic by counting parking spaces on site or on Google '
                              'Maps [598Td1ks52Y @ 00:02:46]. AJ Simmons blends 3,000 when the '
                              'carpet-to-hard-floor split is unknown, moving to about 4,000 for all carpet '
                              'and 2,500 down to 2,000 for all hard floor [cWVLz5abUAg @ 00:01:24]. '
                              'Channel Zero Marketing works 2,500 to 3,000 on a small office and drops '
                              'toward 2,500 when it is mostly tile, because tile gets hit twice, dust mop '
                              'then wet mop, while a backpack vacuum passes carpet once [Ey7iPjW1uZQ @ '
                              '00:06:01]. Solo Business Systems tells a solo operator also doing restrooms '
                              'and detail work to plan at the careful end, 2,500 [hf0U17FyA58 @ 00:05:36]. '
                              'Billing rates split the same way: Channel Zero calls $28 to $30 an hour '
                              'middle-ground aggressive in their Midwest market, with mom-and-pop shops '
                              'bidding $25 and others stretching to $35 to $40 [Ey7iPjW1uZQ @ 00:09:04], '
                              'while AJ Simmons cuts to $21 an hour on five-day work to stay competitive '
                              'and goes higher on once-a-week stops [cWVLz5abUAg @ 00:02:56].',
                              'Margin is where the playbooks diverge most. Commercial Cleaning CEO uses a '
                              'sliding chart keyed to weekly hours where bigger accounts carry lower '
                              'margins, so an account above 66 hours a week sits at 35 percent '
                              '[598Td1ks52Y @ 00:08:23]; the logic is that a $10,000-a-month account does '
                              'not take 20 times the management of a $500 one, and bidding a large '
                              'facility at a small-facility margin rarely wins [598Td1ks52Y @ 00:07:07]. '
                              'Clean Proposals sets a 30 percent minimum, admits a million-square-foot '
                              'building may not bear it, and pulls 60 to 80 percent on a 1,000-square-foot '
                              'facility [0OZkOVSBE1c @ 00:01:28]. Janitorial Empire targets a flat 25 '
                              'percent by dividing a $2,650 cost by 0.75, landing about $3,530 and '
                              'rounding to $3,500 to $3,600 depending on scope, competition and contract '
                              'requirements [PmZvMyhPjCM @ 00:03:49]. Solo Business Systems reports '
                              'operators building 15 to 35 percent on top of cost; at 25 percent an $800 '
                              'cost becomes the $1,000-a-month price for its 5,000-square-foot office '
                              '[hf0U17FyA58 @ 00:06:15]. Supplies split the camps too: Matt treats '
                              'supplies as running 2 to 3 percent, usually absorbed inside the margin '
                              '[598Td1ks52Y @ 00:10:07], while Janitorial Empire budgets a separate $225 '
                              'for supplies and $125 for equipment wear on its 10,000-square-foot job '
                              '[PmZvMyhPjCM @ 00:02:30].'],
               'table': {'caption': 'Competing bid playbooks taught by practitioners, side by side',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Whether square-foot pricing belongs in a commercial bid',
                                   'Never quote a flat 20 or 25 cents a foot; build price from labor hours',
                                   'Per-foot pricing works only at 10,000+ square feet cleaned five days a '
                                   'week',
                                   'Commercial Cleaning CEO ([IMbK5m7qbY0 @ 00:02:05]); The Janitorial '
                                   'Store ([Cf4hKGN0mXg @ 00:02:06])'],
                                  ['Default production rate when details are thin',
                                   'Blend 3,000 square feet per hour when the floor mix is unknown',
                                   'Solo operator doing restrooms and detail plans at the careful end of '
                                   '2,500',
                                   'AJ SIMMONS ([cWVLz5abUAg @ 00:01:24]); Solo Business Systems '
                                   '([hf0U17FyA58 @ 00:05:36])'],
                                  ['Margin target as account size changes',
                                   'Sliding chart puts 14 to 33 weekly hours at a 45 percent margin',
                                   'Flat 25 percent margin by dividing total monthly cost by 0.75',
                                   'Commercial Cleaning CEO ([IMbK5m7qbY0 @ 00:14:51]); Janitorial Empire '
                                   '([PmZvMyhPjCM @ 00:03:49])'],
                                  ['How profit gets entered into the calculator',
                                   'Type a fixed dollar profit, such as $250 on a $300 labor job',
                                   'Set a 30 percent target margin and let the sheet recommend price',
                                   'Janibid ([9FeuDZZNdKI @ 00:01:15]); BizAlmighty ([f0CmEkWm_a0 @ '
                                   '00:02:34])'],
                                  ['Minimum charge logic for tiny or fast jobs',
                                   'Minimum price in the 300-to-400 range, plus a $65 per-visit floor '
                                   'twice weekly',
                                   'A $120 minimum job price kicks in when cost-based price falls near $75',
                                   'Channel Zero Marketing ([Ey7iPjW1uZQ @ 00:10:52]); Cleaning Business '
                                   'Tools ([skflEiwVHxw @ 00:04:16])'],
                                  ['Whether the owner-operator bids their own labor',
                                   'Bid like the company you want to be, with payroll, insurance and '
                                   'overhead loaded',
                                   'Brand-new solo cleaner can accept roughly $44 an hour topline to land '
                                   'first accounts',
                                   'Clean Proposals ([0OZkOVSBE1c @ 00:00:15]); Channel Zero Marketing '
                                   '([Ey7iPjW1uZQ @ 00:15:04])'],
                                  ['Fast quote shortcut without a full takeoff',
                                   'Bill $32.20 an hour times 5 hours, 5 nights, 4.33 weeks for $3,485 '
                                   'monthly',
                                   'Bill $25 an hour against 13 monthly hours for $325 a month',
                                   'Commercial Cleaning CEO ([IMbK5m7qbY0 @ 00:18:52]); The Janitorial '
                                   'Store ([Cf4hKGN0mXg @ 00:01:30])']]}},
              {'heading': 'Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The most expensive failure is a wrong labor-hour estimate, because every '
                              'downstream number multiplies it. Bid & Profit Lab stress-tested its own '
                              '20,000-square-foot bid: at five worker hours a visit the $2,800 price holds '
                              'a 25 percent margin, but six hours a visit pushes monthly labor from $1,625 '
                              'to $1,950, total cost to $2,425, and margin to about 13.4 percent '
                              '[T-l3Df3Iino @ 00:03:51]. Their verdict is blunt: one extra worker hour per '
                              'visit nearly halves the modeled profit, and a spreadsheet cannot make an '
                              'unrealistic time estimate accurate [T-l3Df3Iino @ 00:04:10]. Commercial '
                              'Cleaning CEO sees the mirror error, chronic over-bidding from measuring '
                              'wall to wall; Matt subtracts 10 to 20 percent of measured footage for walls '
                              'and fixed furniture, turning a 10,000-square-foot measurement into 8,500 '
                              'cleanable feet [IMbK5m7qbY0 @ 00:10:01]. Solo Business Systems names the '
                              'restroom blind spot as a core mistake, since fixtures, not floor area, eat '
                              'the clock and the restroom is the room the client inspects [hf0U17FyA58 @ '
                              '00:09:58]. Channel Zero Marketing prices that blind spot separately at '
                              'about 3 minutes a fixture, adding roughly 18 minutes for six fixtures on '
                              'top of a 70-minute general clean [Ey7iPjW1uZQ @ 00:08:13].',
                              'The second trap is a cost stack that stops at the wage. Janitorial Empire '
                              'calls it the first major mistake: an $18-an-hour employee does not cost '
                              '$18, and with a 25 percent burden the true rate is about $22.50 before '
                              'supplies, equipment and $350 of overhead push a 10,000-square-foot job to '
                              '$2,650 in monthly cost [PmZvMyhPjCM @ 00:01:49]. Matt at Commercial '
                              'Cleaning CEO deliberately sets the default payroll-liability line high, so '
                              'expected cost runs above reality rather than below it [IMbK5m7qbY0 @ '
                              '00:03:32]. True Trade Cost builds its calculator around the small items '
                              'cleaning companies forget to charge for, keys, alarm codes, lock-up, the '
                              'restock check and quality inspections, which show red until priced, because '
                              'those little things quietly eat profit [8lFhFbsEuDc @ 00:01:49]. Commercial '
                              'Cleaning CEO also loads setup, close-out, per-cleaning travel and task '
                              'transitions, warning that with five employees in one facility transitions '
                              'alone produce real cost [IMbK5m7qbY0 @ 00:12:02]. Clean Proposals puts a '
                              'number on a missed line: leave training out and two turnovers a year cost '
                              'about $80 a month straight out of cash flow, and that gross figure still '
                              'has to buy the van, the special equipment and the bonuses [0OZkOVSBE1c @ '
                              '00:02:03].',
                              'The last cluster of traps hits new owners hardest. Channel Zero Marketing '
                              'warns that a beginner cleaning three small accounts a night maxes out at '
                              'five or six nights a week with no time to sell or run operations, so every '
                              'bid needs enough margin to hand the work to an employee and still profit '
                              '[Ey7iPjW1uZQ @ 00:15:52]. The same practitioner shows that pricing a '
                              '$65-a-visit, twice-weekly account on four weeks instead of 4.33 drops it '
                              'from $563 to $520 a month and gives away $516 a year, practically a free '
                              'month [Ey7iPjW1uZQ @ 00:13:44]. Bid & Profit Lab adds that an owner who '
                              'leaves their own working time out of the cost makes the job look more '
                              'profitable than it is [T-l3Df3Iino @ 00:02:38]. Solo Business Systems '
                              'documents the cash gap that surprises every residential convert: on net 30, '
                              "a contract started on the first and invoiced at month's end pays around day "
                              "60 while costs leave weekly, so bank one month of that account's costs "
                              'before chasing account number two [hf0U17FyA58 @ 00:08:49]. And when a bid '
                              'loses, Channel Zero says call and ask why, because landing more than 10 to '
                              '20 percent off the other bids, even 40 percent low, scares buyers as much '
                              'as being three times high [Ey7iPjW1uZQ @ 00:20:31].'],
               'table': {'caption': 'Firsthand pricing failures and the economics behind each one',
                         'headers': ['Failure Mode',
                                     'What Happened Firsthand',
                                     'Economics Check',
                                     'Expert Source'],
                         'rows': [['Labor estimate off by one hour per visit',
                                   'Five worker hours became six per visit on a 20,000-square-foot bid',
                                   'Margin fell from 25 percent to about 13.4 percent at the same price',
                                   'Bid & Profit Lab ([T-l3Df3Iino @ 00:04:10])'],
                                  ['Markup confused with margin on the final price',
                                   'Adding 25 percent to a $2,100 cost priced the job at $2,625',
                                   'Real margin landed at 20 percent instead of the intended 25 percent',
                                   'Bid & Profit Lab ([T-l3Df3Iino @ 00:03:15])'],
                                  ['Four-week month used in the monthly formula',
                                   'Twice-weekly $65 visits billed on four weeks instead of 4.33 weeks',
                                   'Monthly price drops from $563 to $520, about $516 a year lost',
                                   'Channel Zero Marketing ([Ey7iPjW1uZQ @ 00:13:44])'],
                                  ['Recurring discount taken straight from margin',
                                   'Ten percent biweekly discount applied to a $161.12 cleaning price',
                                   'Profit fell to $15.73, so discounts must stay small or be pre-built',
                                   'Cleaning Business Tools ([skflEiwVHxw @ 00:03:35])'],
                                  ['Training and turnover left out of proposal expenses',
                                   'Two cleaner turnovers a year were never expensed into the account',
                                   'About $80 a month comes straight out of account cash flow',
                                   'Clean Proposals ([0OZkOVSBE1c @ 00:02:03])'],
                                  ['Net 30 payment gap on a new contract',
                                   'Service starts on the first and the invoice goes out at month end',
                                   'Payment arrives around day 60 while labor costs leave weekly',
                                   'Solo Business Systems ([hf0U17FyA58 @ 00:08:49])'],
                                  ['Crowd-sourced pricing from online cleaning groups',
                                   'Forty-nine answers to one 3,500-square-foot office post swung wildly',
                                   'Same building quoted anywhere from $750 to $3,000 a month',
                                   'Channel Zero Marketing ([Ey7iPjW1uZQ @ 00:01:33])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Four Checks Before Any Bid Leaves Your Hands',
                           'body': 'Every one of these gates comes from a practitioner who watched a bid '
                                   'bleed margin, overprice itself out, or starve cash flow. Clear all '
                                   'four before the number goes to the client.',
                           'items': ['Stress-test the bid at one extra worker hour per visit; scope, '
                                     'labor, full cost, target margin, then a stress test is the '
                                     'repeatable workflow [Bid & Profit Lab — T-l3Df3Iino @ 00:04:26].',
                                     'Subtract 10 to 20 percent of measured square footage for walls and '
                                     'fixed furniture before applying production rates, or you will keep '
                                     'over-bidding [Commercial Cleaning CEO — IMbK5m7qbY0 @ 00:10:01].',
                                     'Price every forgotten site task, including keys, alarm codes, '
                                     'lock-up, restock checks and quality inspections, before the quote '
                                     'goes out [True Trade Cost — 8lFhFbsEuDc @ 00:01:49].',
                                     "Bank one month of the new account's costs before chasing account "
                                     'number two, because net 30 money lands around day 60 [Solo Business '
                                     'Systems — hf0U17FyA58 @ 00:09:25].']}}],
 'pull_quote': '"You always want to bid like the company you want to be, never bid like the company you '
               'are." Attributed to Clean Proposals (0OZkOVSBE1c @ 00:00:15).',
 'diagram_id': 'diag-05',
 'action_checklist': ['Walk every building yourself, measure the cleanable square footage, and count '
                      'restroom fixtures rather than restrooms before writing a number [Solo Business '
                      'Systems — hf0U17FyA58 @ 00:04:20].',
                      'Build true hourly labor cost as average market starting pay plus 10 percent, then '
                      'add payroll liabilities, the way $14.30 became $16.32 [Commercial Cleaning CEO — '
                      '598Td1ks52Y @ 00:05:24].',
                      'Convert per-visit price to monthly using 4.33 weeks, never four, so the two '
                      'five-week months are not given away [Channel Zero Marketing — Ey7iPjW1uZQ @ '
                      '00:13:11].',
                      'Divide total monthly cost by one minus the target margin, since adding 25 percent '
                      'to cost does not produce a 25 percent margin [Janitorial Empire — PmZvMyhPjCM @ '
                      '00:03:30].',
                      'Call every lost bid, say you are new, and ask what made them choose the other '
                      'company so you learn whether price or presentation lost it [Channel Zero Marketing '
                      '— Ey7iPjW1uZQ @ 00:19:45].',
                      'Log actual hours on every job and adjust your time standards after five to ten '
                      'cleans [Cleaning Business Tools — skflEiwVHxw @ 00:05:04].'],
 'statutory_citations': [{'title': 'Commercial Cleaning CEO — How To Profitably Bid Commercial Cleaning '
                                   'Jobs | CALCULATOR [00:10:01]',
                          'url': 'https://www.youtube.com/watch?v=IMbK5m7qbY0&t=601s',
                          'relevance': 'Primary practitioner testimony on cleanable square footage '
                                       'deductions, task-time inference and the weekly-hours margin '
                                       'chart.'},
                         {'title': 'Commercial Cleaning CEO — Price Commercial Cleaning RIGHT | Cleaning '
                                   'Bid Calculator [00:08:23]',
                          'url': 'https://www.youtube.com/watch?v=598Td1ks52Y&t=503s',
                          'relevance': 'Primary practitioner testimony on true hourly labor cost, '
                                       'economies-of-scale margins and the final monthly bid formula.'},
                         {'title': 'Bid & Profit Lab — How to Bid a Commercial Cleaning Contract: 20,000 '
                                   'Sq Ft Example. [00:03:51]',
                          'url': 'https://www.youtube.com/watch?v=T-l3Df3Iino&t=231s',
                          'relevance': 'Primary practitioner testimony on margin versus markup and '
                                       'stress-testing a bid against one extra worker hour.'},
                         {'title': 'Channel Zero Marketing — How to Price Your First Commercial Cleaning '
                                   'Contract (Real Example) [00:13:44]',
                          'url': 'https://www.youtube.com/watch?v=Ey7iPjW1uZQ&t=824s',
                          'relevance': 'Primary practitioner testimony on blended production rates, '
                                       'fixture timing, minimums and the 4.33-week formula.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'IMbK5m7qbY0',
                       'title': 'How To Profitably Bid Commercial Cleaning Jobs | CALCULATOR',
                       'channel': 'Commercial Cleaning CEO',
                       'author': 'Commercial Cleaning CEO',
                       'text': 'By default, we typically subtract anywhere from 10 to 20% of the square '
                               'footage that we measure from that number.',
                       'tip': 'By default, we typically subtract anywhere from 10 to 20% of the square '
                              'footage that we measure from that number.',
                       'timestamp': 601,
                       'timestamp_seconds': 601,
                       'timestamp_label': '[00:10:01]',
                       'url': 'https://www.youtube.com/watch?v=IMbK5m7qbY0&t=601s',
                       'markdown': '[00:10:01](https://www.youtube.com/watch?v=IMbK5m7qbY0&t=601s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Ey7iPjW1uZQ',
                       'title': 'How to Price Your First Commercial Cleaning Contract (Real Example)',
                       'channel': 'Channel Zero Marketing',
                       'author': 'Channel Zero Marketing',
                       'text': "If you do it at 4.33 it's 563 a month, so you're talking about $516 a year "
                               "you're missing.",
                       'tip': "If you do it at 4.33 it's 563 a month, so you're talking about $516 a year "
                              "you're missing.",
                       'timestamp': 824,
                       'timestamp_seconds': 824,
                       'timestamp_label': '[00:13:44]',
                       'url': 'https://www.youtube.com/watch?v=Ey7iPjW1uZQ&t=824s',
                       'markdown': '[00:13:44](https://www.youtube.com/watch?v=Ey7iPjW1uZQ&t=824s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Ey7iPjW1uZQ',
                       'title': 'How to Price Your First Commercial Cleaning Contract (Real Example)',
                       'channel': 'Channel Zero Marketing',
                       'author': 'Channel Zero Marketing',
                       'text': "Remember to price it like you'll be hiring someone to work it someday.",
                       'tip': "Remember to price it like you'll be hiring someone to work it someday.",
                       'timestamp': 1356,
                       'timestamp_seconds': 1356,
                       'timestamp_label': '[00:22:36]',
                       'url': 'https://www.youtube.com/watch?v=Ey7iPjW1uZQ&t=1356s',
                       'markdown': '[00:22:36](https://www.youtube.com/watch?v=Ey7iPjW1uZQ&t=1356s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '9FeuDZZNdKI',
                       'title': 'How to Bid Commercial Cleaning Services? Free Commercial Cleaning '
                                'Calculator',
                       'channel': 'Janibid',
                       'author': 'Janibid',
                       'text': 'You typically know what an office is going to take; 2,000 square feet is '
                               'usually around two hours.',
                       'tip': 'You typically know what an office is going to take; 2,000 square feet is '
                              'usually around two hours.',
                       'timestamp': 23,
                       'timestamp_seconds': 23,
                       'timestamp_label': '[00:00:23]',
                       'url': 'https://www.youtube.com/watch?v=9FeuDZZNdKI&t=23s',
                       'markdown': '[00:00:23](https://www.youtube.com/watch?v=9FeuDZZNdKI&t=23s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Cf4hKGN0mXg',
                       'title': 'How to price a 2,400 square foot office space: How to price cleaning '
                                'offices',
                       'channel': 'The Janitorial Store',
                       'author': 'The Janitorial Store',
                       'text': "Whenever you have an office space that you're only cleaning three days per "
                               "week, you don't want to price it by the square foot because the "
                               "calculations just don't work properly.",
                       'tip': "Whenever you have an office space that you're only cleaning three days per "
                              "week, you don't want to price it by the square foot because the "
                              "calculations just don't work properly.",
                       'timestamp': 126,
                       'timestamp_seconds': 126,
                       'timestamp_label': '[00:02:06]',
                       'url': 'https://www.youtube.com/watch?v=Cf4hKGN0mXg&t=126s',
                       'markdown': '[00:02:06](https://www.youtube.com/watch?v=Cf4hKGN0mXg&t=126s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'T-l3Df3Iino',
                       'title': 'How to Bid a Commercial Cleaning Contract: 20,000 Sq Ft Example.',
                       'channel': 'Bid & Profit Lab',
                       'author': 'Bid & Profit Lab',
                       'text': 'One extra worker hour per visit nearly halves the modeled profit.',
                       'tip': 'A spreadsheet can calculate the result, but it cannot make an unrealistic '
                              'time estimate accurate.',
                       'timestamp': 250,
                       'timestamp_seconds': 250,
                       'timestamp_label': '[00:04:10]',
                       'url': 'https://www.youtube.com/watch?v=T-l3Df3Iino&t=250s',
                       'markdown': '[00:04:10](https://www.youtube.com/watch?v=T-l3Df3Iino&t=250s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Q0_kmHGx6FI',
                       'title': 'Free Commercial Calculator App - How to price commercial cleaning?',
                       'channel': 'Janibid',
                       'author': 'Janibid',
                       'text': "If I'm going to have a labor cost and expense cost of 900, I'm probably "
                               'going to want to make at least like 350 on it.',
                       'tip': "If I'm going to have a labor cost and expense cost of 900, I'm probably "
                              'going to want to make at least like 350 on it.',
                       'timestamp': 155,
                       'timestamp_seconds': 155,
                       'timestamp_label': '[00:02:35]',
                       'url': 'https://www.youtube.com/watch?v=Q0_kmHGx6FI&t=155s',
                       'markdown': '[00:02:35](https://www.youtube.com/watch?v=Q0_kmHGx6FI&t=155s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'f0CmEkWm_a0',
                       'title': 'Cleaning Business Calculator   Basic   Walkthrough',
                       'channel': 'BizAlmighty',
                       'author': 'BizAlmighty',
                       'text': "Some jobs are more difficult than others, and you're able to account for "
                               'that by defining your multipliers for easy, normal, hard, or very hard '
                               'jobs.',
                       'tip': "Some jobs are more difficult than others, and you're able to account for "
                              'that by defining your multipliers for easy, normal, hard, or very hard '
                              'jobs.',
                       'timestamp': 116,
                       'timestamp_seconds': 116,
                       'timestamp_label': '[00:01:56]',
                       'url': 'https://www.youtube.com/watch?v=f0CmEkWm_a0&t=116s',
                       'markdown': '[00:01:56](https://www.youtube.com/watch?v=f0CmEkWm_a0&t=116s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'AdyzLEzXsAQ',
                       'title': 'Cleaning Business Quote Calculator in Google Sheets (Easy Tutorial)',
                       'channel': 'Little Wonders',
                       'author': 'Little Wonders',
                       'text': 'A margin is a percentage of the selling price, not a markup percentage '
                               'added to cost.',
                       'tip': 'A margin is a percentage of the selling price, not a markup percentage '
                              'added to cost.',
                       'timestamp': 134,
                       'timestamp_seconds': 134,
                       'timestamp_label': '[00:02:14]',
                       'url': 'https://www.youtube.com/watch?v=AdyzLEzXsAQ&t=134s',
                       'markdown': '[00:02:14](https://www.youtube.com/watch?v=AdyzLEzXsAQ&t=134s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '8lFhFbsEuDc',
                       'title': 'How Much to Charge for Commercial Cleaning | Commercial Cleaning Pricing '
                                'Calculator Walkthrough',
                       'channel': 'True Trade Cost',
                       'author': 'True Trade Cost',
                       'text': 'For this company, every hour in a building has to bring in $36.15 before a '
                               'dime of profit.',
                       'tip': 'For this company, every hour in a building has to bring in $36.15 before a '
                              'dime of profit.',
                       'timestamp': 41,
                       'timestamp_seconds': 41,
                       'timestamp_label': '[00:00:41]',
                       'url': 'https://www.youtube.com/watch?v=8lFhFbsEuDc&t=41s',
                       'markdown': '[00:00:41](https://www.youtube.com/watch?v=8lFhFbsEuDc&t=41s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '598Td1ks52Y',
                       'title': 'Price Commercial Cleaning RIGHT | Cleaning Bid Calculator',
                       'channel': 'Commercial Cleaning CEO',
                       'author': 'Commercial Cleaning CEO',
                       'text': 'If you go into a large facility and bid it at a profit margin of a small '
                               'facility, the odds of you winning it are going to be very low.',
                       'tip': 'If you go into a large facility and bid it at a profit margin of a small '
                              'facility, the odds of you winning it are going to be very low.',
                       'timestamp': 461,
                       'timestamp_seconds': 461,
                       'timestamp_label': '[00:07:41]',
                       'url': 'https://www.youtube.com/watch?v=598Td1ks52Y&t=461s',
                       'markdown': '[00:07:41](https://www.youtube.com/watch?v=598Td1ks52Y&t=461s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'skflEiwVHxw',
                       'title': 'How to Price a House Cleaning Job (Real Math, Step by Step)',
                       'channel': 'Cleaning Business Tools',
                       'author': 'Cleaning Business Tools',
                       'text': 'A minimum protects your time, because driving, setup and scheduling cost '
                               'you the same on a small job.',
                       'tip': 'A minimum protects your time, because driving, setup and scheduling cost '
                              'you the same on a small job.',
                       'timestamp': 280,
                       'timestamp_seconds': 280,
                       'timestamp_label': '[00:04:40]',
                       'url': 'https://www.youtube.com/watch?v=skflEiwVHxw&t=280s',
                       'markdown': '[00:04:40](https://www.youtube.com/watch?v=skflEiwVHxw&t=280s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'cWVLz5abUAg',
                       'title': 'How to bid on 30,000 square foot office building for cleaning | '
                                'Calculated Cleaning | Cleaning Cost',
                       'channel': 'AJ SIMMONS',
                       'author': 'AJ SIMMONS',
                       'text': 'If you live in an area where you can still get away with paying somebody '
                               'ten bucks an hour, then maybe you might lower this to twenty-one dollars '
                               'an hour.',
                       'tip': 'If you live in an area where you can still get away with paying somebody '
                              'ten bucks an hour, then maybe you might lower this to twenty-one dollars an '
                              'hour.',
                       'timestamp': 176,
                       'timestamp_seconds': 176,
                       'timestamp_label': '[00:02:56]',
                       'url': 'https://www.youtube.com/watch?v=cWVLz5abUAg&t=176s',
                       'markdown': '[00:02:56](https://www.youtube.com/watch?v=cWVLz5abUAg&t=176s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'hf0U17FyA58',
                       'title': 'Commercial Cleaning: How to Win Your First Office Contract (Walkthrough + '
                                'Bid Worksheet)',
                       'channel': 'Solo Business Systems',
                       'author': 'Solo Business Systems',
                       'text': 'A per square foot figure is a comparison tool, nothing more.',
                       'tip': "The moment it becomes your pricing method, you're bidding somebody else's "
                              "building, somebody else's costs, somebody else's margin.",
                       'timestamp': 448,
                       'timestamp_seconds': 448,
                       'timestamp_label': '[00:07:28]',
                       'url': 'https://www.youtube.com/watch?v=hf0U17FyA58&t=448s',
                       'markdown': '[00:07:28](https://www.youtube.com/watch?v=hf0U17FyA58&t=448s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'PmZvMyhPjCM',
                       'title': 'How to Price a Commercial Cleaning Contract (10,000 Sq Ft Example)',
                       'channel': 'Janitorial Empire',
                       'author': 'Janitorial Empire',
                       'text': 'Adding 25% to your cost does not give you a 25% profit margin; if you want '
                               'a 25% margin, divide your cost by 0.75.',
                       'tip': 'Adding 25% to your cost does not give you a 25% profit margin; if you want '
                              'a 25% margin, divide your cost by 0.75.',
                       'timestamp': 210,
                       'timestamp_seconds': 210,
                       'timestamp_label': '[00:03:30]',
                       'url': 'https://www.youtube.com/watch?v=PmZvMyhPjCM&t=210s',
                       'markdown': '[00:03:30](https://www.youtube.com/watch?v=PmZvMyhPjCM&t=210s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'UugCweTgBhY',
                       'title': 'CleanFirst Tutorial | Cleaning Business Pricing Calculator & Quote '
                                'Template',
                       'channel': 'Jeff Jones | Digital Creator',
                       'author': 'Jeff Jones | Digital Creator',
                       'text': 'It gives you a suggested price of 136, the modeled gross contribution is '
                               '$34 and the modeled gross margin is 25%.',
                       'tip': 'It gives you a suggested price of 136, the modeled gross contribution is '
                              '$34 and the modeled gross margin is 25%.',
                       'timestamp': 235,
                       'timestamp_seconds': 235,
                       'timestamp_label': '[00:03:55]',
                       'url': 'https://www.youtube.com/watch?v=UugCweTgBhY&t=235s',
                       'markdown': '[00:03:55](https://www.youtube.com/watch?v=UugCweTgBhY&t=235s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '0OZkOVSBE1c',
                       'title': 'Understanding Cash Flow and Profit Margins for your Commercial Janitorial '
                                'Cleaning Business',
                       'channel': 'Clean Proposals',
                       'author': 'Clean Proposals',
                       'text': 'You always want to bid like the company you want to be, never bid like the '
                               'company you are.',
                       'tip': 'You always want to bid like the company you want to be, never bid like the '
                              'company you are.',
                       'timestamp': 15,
                       'timestamp_seconds': 15,
                       'timestamp_label': '[00:00:15]',
                       'url': 'https://www.youtube.com/watch?v=0OZkOVSBE1c&t=15s',
                       'markdown': '[00:00:15](https://www.youtube.com/watch?v=0OZkOVSBE1c&t=15s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'}]}
