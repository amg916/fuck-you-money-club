from __future__ import annotations

CHAPTER_2 = {'id': 'Q2',
 'chapter_id': 'Q2',
 'chapter_number': 2,
 'question_number': 2,
 'slug': 'q02-merchant-pricing-models-statement-analysis',
 'question_prompt': 'How do interchange, tiered, flat-rate, interchange-plus, and subscription pricing '
                    'compare, and how do you read a merchant statement to find the real cost?',
 'kicker': 'Q2 / THE BIG MONEY PLAYBOOKS',
 'title': 'Merchant Pricing Models and Statement Analysis',
 'subtitle': 'Interchange basics; tiered vs. interchange-plus vs. flat-rate vs. subscription pricing; '
             'which structure pays the agent more; and reading tiered and cost-plus statements line by '
             'line to find hidden fees',
 'layout_template': 'executive_summary',
 'reading_time_minutes': 15,
 'executive_summary': 'Practitioners across BancardSales, CCSalesPro, Merchant Maverick, Helcim and '
                      'MerchantAccounts.ca agree that interchange is the fixed wholesale floor under every '
                      'pricing model, identical across processors and non-negotiable, so the only lever is '
                      'the processor markup and the card-acceptance habits that keep transactions in '
                      'cheaper categories. The street mechanics are statement math: total interchange '
                      'divided by volume should land near 1.7 percent, total fees minus interchange '
                      'exposes markup, and tier statements are judged by card mix before rates, with 60 to '
                      '70 percent qualified expected for storefronts. Agents price from Schedule A costs, '
                      'using per-item fees to survive small-ticket debit. The split comes on tiered '
                      'pricing: Merchant Maverick and Joe Wagner call it a buried-markup red flag, while '
                      'Bryan Manning and Paygent AI argue the right model is situational, with Manning '
                      'naming the effective rate as the only undisputed yardstick.',
 'key_metrics': [{'label': 'Average US Interchange Effective Rate',
                  'metric': 'Average US Interchange Effective Rate',
                  'value': '1.7 percent (1.6 to 1.8 percent is about right)',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Total interchange divided by total volume on an interchange plus statement, '
                             'stated as the US average in May 2019',
                  'source': 'CCSalesPro ([2Sn4XMqpW4I @ 00:01:46])'},
                 {'label': 'Interchange Share of Total Processing Cost',
                  'metric': 'Interchange Share of Total Processing Cost',
                  'value': 'Roughly 70 to 90 percent',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Portion of transaction processing costs that goes to interchange depending '
                             'on the rate plan, with the rest going to the processor and card association',
                  'source': 'Merchant Maverick ([dUz90pAXTm0 @ 00:02:30])'},
                 {'label': 'Uncompetitive Markup Threshold at Mid Volume',
                  'metric': 'Uncompetitive Markup Threshold at Mid Volume',
                  'value': 'More than about 0.7 percent markup at 20,000 to 40,000 dollars monthly volume',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Markup effective rate (total fees minus interchange, divided by volume) '
                             'above this level signals a savings opportunity',
                  'source': 'CCSalesPro ([2Sn4XMqpW4I @ 00:06:40])'},
                 {'label': 'Small-Ticket Flat Rate Loss Trap',
                  'metric': 'Small-Ticket Flat Rate Loss Trap',
                  'value': 'About 33 cents of per-item cost on a 2 dollar ticket, roughly 15 percent cost '
                           'against a 3.5 percent flat rate',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Agents who sold a coffee shop on 3.5 percent flat rate owed money back to '
                             'the processor on their first residual statement',
                  'source': 'CCSalesPro ([fb0PHmE8aCc @ 00:04:55])'}],
 'sections': [{'section': 1,
               'heading': 'The Practitioner Consensus',
               'paragraphs': ['Every practitioner starts from the same floor: interchange. Bryan Manning '
                              'of BancardSales frames it as the prime rate of payments, a published '
                              'schedule of hundreds of categories that is the same for every processing '
                              'company and acts as the base cost for credit and debit acceptance '
                              '[AseZioaNb5s @ 00:01:14]. Ahmad at Merchant Maverick calls it the wholesale '
                              'layer set by Visa and Mastercard, shared between the card associations and '
                              'issuing banks like Chase, Wells Fargo and Bank of America, and flatly '
                              'states those fees cannot be negotiated [h72ua8pD9cU @ 00:04:38]. David at '
                              'MerchantAccounts.ca makes the same point from the Canadian side: '
                              'interchange is set at a country level, so switching processors never '
                              'changes the underlying cost structure, and nearly all of it flows to the '
                              'card issuing bank with a roughly 0.1 percent card brand fee layered on top '
                              '[btemhvIers4 @ 00:00:47]. PaymentCloud closes the loop for the merchant '
                              'across the desk: because issuing banks assign interchange, there is no way '
                              'to lower it, but the discount rate the processor adds to each transaction '
                              'is open for negotiation [xfBalp9Zzio @ 00:06:31]. The practical consensus '
                              'is blunt. The only money in play is the markup, so every pitch, audit and '
                              'repricing targets that layer and nothing beneath it.',
                              'The practitioners also agree on what pushes a transaction into a cheap or '
                              'expensive category. Manning lists the business type and MCC code, '
                              'face-to-face versus internet acceptance, average ticket, consumer versus '
                              'business or corporate cards, interchange optimization technology and daily '
                              'settlement, noting each card lands in one and only one category and that '
                              'the brands publish changes twice a year, spring and fall [AseZioaNb5s @ '
                              '00:02:37]. Merchant Maverick puts a ratio on the card-type gap: credit '
                              'interchange runs roughly six times higher than debit, rewards cards cost '
                              'more, and interchange eats roughly 70 to 90 percent of total processing '
                              'cost depending on the rate plan [dUz90pAXTm0 @ 00:02:30]. James Shepherd of '
                              'CCSalesPro adds the industry layer most merchants miss, explaining that the '
                              'same card spending 100 dollars costs a grocery store less than a retail '
                              'store because grocers run on their own interchange table, while B2B cards '
                              'and rewards cards cost more and debit usually costs significantly less '
                              'except at tiny-ticket shops like coffee [bdumFSr4sA8 @ 00:04:25]. Manning '
                              'turns that into merchant-side habits: run AVS, key the three-digit code and '
                              'billing zip, settle daily, swipe or dip whenever the card is present, and '
                              'void instead of refunding, all to qualify more transactions into the lower '
                              'interchange category [AseZioaNb5s @ 00:04:57].',
                              "The third point of agreement is that the processor's underlying cost never "
                              'moves with the pricing label on the account. Shepherd tells a newly '
                              'independent agent that whether a 10,000 dollar pizza shop sits on '
                              'interchange plus, tiered, flat rate, surcharging or cash discounting, the '
                              'roughly 200 dollars of interchange plus dues, assessments and Schedule A '
                              'per-item costs stays identical, so revenue depends entirely on how the deal '
                              'is priced [fb0PHmE8aCc @ 00:01:07]. Shepherd reduces the choice to '
                              'simplicity versus transparency: larger accounts want interchange plus not '
                              'because it is cheaper but because the statement shows cost and markup line '
                              'by line, while smaller merchants are drifting from tiered to a single flat '
                              'rate because they do not want fifty lines on a statement [fb0PHmE8aCc @ '
                              '00:02:51]. David at MerchantAccounts.ca lands in the same place, saying '
                              'flat pricing can suit a small merchant who mostly wants easy '
                              'reconciliation, but every large merchant on the planet belongs on '
                              "interchange plus [btemhvIers4 @ 00:04:58]. Manning's tiebreaker is the "
                              'effective rate: every model collapses into one end-of-month number, and '
                              'that rate is the only undisputed figure for comparing any two providers '
                              '[5jk-0XxkiR0 @ 00:11:32]. In practice, operators read every model through '
                              'that single number before arguing about labels.'],
               'table': {'caption': 'Where the practitioners line up on interchange, cost floors and model '
                                    'choice',
                         'headers': ['Consensus Point',
                                     'What the Practitioner Reports',
                                     'Operator Implication',
                                     'Expert Source'],
                         'rows': [['Interchange is a fixed base cost for everyone',
                                   'Same schedule for every processor, compared to the prime rate in '
                                   'mortgage lending',
                                   'Stop shopping interchange and attack the processor markup layer '
                                   'instead',
                                   'BancardSales ([AseZioaNb5s @ 00:01:14])'],
                                  ['Published interchange cannot be discounted by a sales rep',
                                   'Be careful when a merchant account rep offers a discount on standard '
                                   'interchange',
                                   'Treat any promised interchange discount as a warning sign during '
                                   'competitive pitches',
                                   'Merchant Maverick ([dUz90pAXTm0 @ 00:03:58])'],
                                  ['Interchange dominates the total processing bill every month',
                                   'Roughly 70 to 90 percent of processing cost goes to interchange fees',
                                   'Markup is the remaining slice where processors earn money and compete '
                                   'for accounts',
                                   'Merchant Maverick ([dUz90pAXTm0 @ 00:02:30])'],
                                  ['Card type drives the category cost on every swipe',
                                   'Rewards and ultra premium cards cost more while debit costs far less '
                                   'than credit',
                                   'Read the card mix before judging any quoted rate on a statement',
                                   'MerchantAccounts.ca ([btemhvIers4 @ 00:01:02])'],
                                  ['Agent cost is identical across every pricing model',
                                   'Schedule A interchange, dues, assessments and per-item costs never '
                                   'change with the pricing label',
                                   'Agent revenue depends entirely on the markup level chosen for the deal',
                                   'CCSalesPro ([fb0PHmE8aCc @ 00:01:41])'],
                                  ['Effective rate is the universal comparison yardstick',
                                   'Every pricing model yields one single end-of-month rate for the '
                                   'merchant account',
                                   'Compare any two providers on effective rate before trusting '
                                   'transparency labels',
                                   'BancardSales ([5jk-0XxkiR0 @ 00:11:32])'],
                                  ['Growing merchants are rewarded on interchange plus pricing',
                                   'Volume milestones unlock lower markup because cost is separated from '
                                   'margin',
                                   'Pitch interchange plus to bigger accounts and flat rate to the '
                                   'smallest ones',
                                   'Helcim ([cZ2DaswdAqo @ 00:07:43])']]}},
              {'section': 2,
               'heading': 'Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['Statement work starts with identifying the pricing model in seconds, before '
                              "touching a single rate. Shepherd's rule for tiered statements is to scan "
                              'for qualified, mid-qualified and non-qualified, usually abbreviated as '
                              'qual, m-qual and n-qual, and the presence of those words alone confirms '
                              'tier pricing [RxgrRsVThx4 @ 00:00:00]. An interchange plus statement '
                              'instead carries a huge interchange table of incomprehensible abbreviations, '
                              'anywhere from ten to 200 lines, plus a total interchange figure; Shepherd '
                              'treats a supposed cost-plus statement with no total interchange amount as '
                              'suspicious on sight [2Sn4XMqpW4I @ 00:05:13]. The disguise to watch for is '
                              'tiered pricing dressed up as an interchange table: the category names are '
                              'real, but scanning down the rate column shows only three or four distinct '
                              'rates repeating across many lines, which means bucketed rates are being '
                              'displayed like pass-through [XEaaN73nJ6Q @ 00:06:39]. Subscription pricing '
                              'announces itself as one large monthly subscription or monthly fee around 40 '
                              'or 50 dollars, with everything else presented as Visa and Mastercard cost, '
                              'though Shepherd warns that small network-access fees often carry hidden '
                              'markup on top of the subscription, and that processors mostly offer it to '
                              'small merchants who would pay only about 30 dollars of markup on tiered '
                              'pricing, overpaying roughly 20 dollars a month [aZv0u_x9ipQ @ 00:00:42].',
                              'Once the model is known, the arithmetic is simple enough to run at a '
                              'counter. Shepherd divides total interchange by total volume and expects '
                              'roughly 1.7 percent, with 1.6 to 1.8 percent normal, small-ticket '
                              'debit-heavy shops near 2.5 to 2.7 percent, large-ticket rewards and B2B '
                              'merchants around 2.2 to 2.8 percent, and debit-heavy auto repair as low as '
                              '1 percent [2Sn4XMqpW4I @ 00:03:03]. Total fees minus total interchange is '
                              'the markup; divide that by volume and benchmark it against size: 1 to 1.5 '
                              'percent is unremarkable under 10,000 dollars a month, anything over about '
                              '0.7 percent at 20,000 to 40,000 is uncompetitive, and above 60,000 even 0.3 '
                              'percent probably has a better offer waiting [2Sn4XMqpW4I @ 00:06:22]. David '
                              'shows the per-card math in Canada: a basic Visa at 1.4 percent interchange '
                              'plus a 0.1 percent card brand fee is a 1.5 percent cost, so interchange '
                              'plus 0.5 percent bills the merchant 2 percent on that card [btemhvIers4 @ '
                              '00:02:07]. The markup ladder then steps down with size, with David quoting '
                              'around 0.25 over interchange at a million dollars a month for low-risk '
                              'product and about 0.15 at ten million [btemhvIers4 @ 00:03:42].',
                              "On tiered statements, Shepherd's first move is card mix, not rates: a "
                              'storefront retailer, restaurant or auto shop should show 60 to 70 percent '
                              'qualified with the rest split roughly evenly between mid and non-qualified, '
                              'and anything lower usually means savings are sitting on the table '
                              '[RxgrRsVThx4 @ 00:02:54]. The quickest rate win is converting a blended '
                              'qualified rate into four-tier pricing with a separate, cheaper debit and '
                              'check card qualified rate. On the agent side, the CCSalesPro coach dissects '
                              'a live deal priced at 1.45, 2.29 and 3.5 percent plus 10 and 15 cent item '
                              'fees: with regulated debit costing about 22 cents and five basis points, '
                              'that 25 cents covers the per-item cost and the qualified basis points on '
                              'debit are almost all profit [fb0PHmE8aCc @ 00:06:41]. For a 240 dollar '
                              'average ticket, the play is interchange plus 40 basis points and 10 cents '
                              'for a large account, or for one doing 20,000 dollars a month or less, a '
                              'simplified flat 2.15 percent and 25 cents, keeping a high per-item fee '
                              'because nothing else is passed through [fb0PHmE8aCc @ 00:08:16]. The '
                              "coach's final call was to simply match the existing tiered pricing, because "
                              'the mid and non-qualified bumps protect margin if next month brings rewards '
                              'and corporate cards instead of debit [fb0PHmE8aCc @ 00:10:06].'],
               'table': {'caption': 'Statement math, benchmarks and tools the practitioners actually run',
                         'headers': ['Mechanic or Tool',
                                     'Exact Numbers or Workflow',
                                     'How Operators Use It',
                                     'Expert Source'],
                         'rows': [['Interchange effective rate check on cost-plus statements',
                                   'Total interchange divided by total volume should land near 1.7 percent',
                                   'Flags padded or marked-up interchange when the figure looks '
                                   'dramatically off',
                                   'CCSalesPro ([2Sn4XMqpW4I @ 00:03:03])'],
                                  ['Markup extraction formula for any interchange plus statement',
                                   'Total fees minus total interchange, then divided by total monthly '
                                   'volume',
                                   'Benchmarks markup against monthly volume bands to locate savings',
                                   'CCSalesPro ([2Sn4XMqpW4I @ 00:05:31])'],
                                  ['Tiered card mix benchmark for physical locations',
                                   'Storefronts should show 60 to 70 percent qualified transactions each '
                                   'month',
                                   'A lower qualified share signals bucket games and an easy savings pitch',
                                   'CCSalesPro ([RxgrRsVThx4 @ 00:02:54])'],
                                  ['Canadian interchange plus per-card math',
                                   '1.4 percent interchange plus 0.1 brand fee plus 0.5 markup equals 2 '
                                   'percent',
                                   'Shows the merchant exactly what the processor keeps on each card',
                                   'MerchantAccounts.ca ([btemhvIers4 @ 00:02:29])'],
                                  ['Small-ticket regulated debit per-item floor',
                                   'Regulated debit runs about 22 cents plus five basis points per '
                                   'transaction',
                                   'Always load per-item fees into flat or tiered small-ticket deals',
                                   'CCSalesPro ([fb0PHmE8aCc @ 00:07:14])'],
                                  ['ISO Amp full-service statement analysis platform',
                                   'Uploads return categorized fees, about 87 percent back in 20 minutes '
                                   'or less',
                                   'Converts any statement into side-by-side proposals across every '
                                   'pricing model',
                                   'CCSalesPro ([bdumFSr4sA8 @ 00:01:49])'],
                                  ['Helcim free statement comparison calculator',
                                   'Three inputs: current cost, online versus in-person split, volume by '
                                   'card type',
                                   'Estimates merchant savings from moving onto an interchange plus model',
                                   'Helcim ([cZ2DaswdAqo @ 00:09:16])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Street-Level Pricing Edges From the Field',
                           'body': 'These are the moves practitioners use to protect margin on their own '
                                   "book and to find switch targets fast on someone else's statement.",
                           'items': ['Never price an average ticket under about 15 dollars on flat or '
                                     'tiered without a per-item fee; agents who sold a coffee shop at 3.5 '
                                     'percent flat owed the processor money on the first residual '
                                     '[CCSalesPro — fb0PHmE8aCc @ 00:05:24]',
                                     'A merchant still on tiered pricing likely has not had fees reviewed '
                                     'in years and is almost always overpaying, which makes the account a '
                                     'prime switch target [Joe Wagner | Merchant Services & Passive Income '
                                     '— XXH81AbZQcg @ 00:01:11]',
                                     'Before switching processors, ask the current one to move the account '
                                     'onto interchange plus, since the same processor may offer all three '
                                     'models and cut fees without a switch [Paygent AI — xTWy5shtdSk @ '
                                     '00:09:53]',
                                     'Larger merchants who have stayed with a processor can trade a longer '
                                     'contract term for a lower interchange markup [MerchantAccounts.ca — '
                                     'btemhvIers4 @ 00:05:27]']},
               'sop_steps': [{'step': 1,
                              'title': 'Identify the pricing model',
                              'action': 'Scan the statement for tier words, a full interchange table, or '
                                        'one large monthly subscription fee.',
                              'detail': 'Qual, m-qual and n-qual confirm tier pricing, while an '
                                        'interchange table showing only three or four repeating rates is '
                                        'tiered pricing displayed like pass-through [CCSalesPro — '
                                        'RxgrRsVThx4 @ 00:00:00] [CCSalesPro — XEaaN73nJ6Q @ 00:06:39]'},
                             {'step': 2,
                              'title': 'Compute the effective and interchange rates',
                              'action': 'Divide total fees by total volume, then total interchange by '
                                        'total volume.',
                              'detail': 'The interchange figure should sit near 1.7 percent, and the '
                                        'overall effective rate is the one number that compares any '
                                        'provider to any other [CCSalesPro — 2Sn4XMqpW4I @ 00:03:03] '
                                        '[BancardSales — 5jk-0XxkiR0 @ 00:11:32]'},
                             {'step': 3,
                              'title': 'Isolate and benchmark the markup',
                              'action': 'Subtract total interchange from total fees, divide by volume, and '
                                        'compare to the volume band.',
                              'detail': '1 to 1.5 percent is normal under 10,000 dollars a month, over 0.7 '
                                        'percent at 20,000 to 40,000 is uncompetitive, and even 0.3 '
                                        'percent above 60,000 can be beaten [CCSalesPro — 2Sn4XMqpW4I @ '
                                        '00:06:22]'},
                             {'step': 4,
                              'title': 'Price the proposal from Schedule A cost',
                              'action': 'Quote interchange plus to large accounts and a simplified flat '
                                        'rate with a strong per-item fee to smaller ones.',
                              'detail': 'Interchange plus 40 basis points and 10 cents for a big account, '
                                        'or a flat 2.15 percent and 25 cents for one doing 20,000 dollars '
                                        'a month or less [CCSalesPro — fb0PHmE8aCc @ 00:08:29]'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['Tiered pricing is the sharpest split on the street. Ahmad at Merchant '
                              'Maverick calls it the least transparent model and the worst one a merchant '
                              'can sit on. He tells owners to ask their processor whether they are on it '
                              'and to get off it immediately [h72ua8pD9cU @ 00:16:08]. Joe Wagner goes '
                              'further for agents prospecting accounts. To him tiered is old school and '
                              'intentionally vague, and a merchant still on it is a great sign, because '
                              'they likely have not had their fees reviewed in years and are almost always '
                              'overpaying [XXH81AbZQcg @ 00:01:11]. Bryan Manning at BancardSales pushes '
                              'back hard. He rejects the claim that tier-based and flat rate programs are '
                              'dishonest. He points out that Stripe and Square both boldly claim '
                              'transparent pricing on their own pricing pages while running tier-based '
                              'models, and concludes that true and transparent is just a subjective term '
                              'people use for whatever model they prefer [5jk-0XxkiR0 @ 00:10:17]. '
                              'CCSalesPro sits in between. When the host started fifteen years ago '
                              'everybody was on tiered. It faded, then came back in a resurgence. Today '
                              'the most common version is two-tier pricing, card present versus card not '
                              'present, the structure PayPal, Square and Stripe run [XEaaN73nJ6Q @ '
                              '00:04:26].',
                              'Interchange plus gets the loudest endorsements, but even its champions make '
                              'exceptions. David at MerchantAccounts.ca calls it the best model in the '
                              'industry with literally no downside. He would quote a low-risk merchant '
                              'doing a million dollars a month at 0.25 over interchange and a '
                              'ten-million-dollar account at 0.15. He still concedes it is not always best '
                              'for small merchants who just want something easy to reconcile, and flat '
                              'pricing may suit them better [btemhvIers4 @ 00:04:58]. Helcim pitches '
                              'scale: at 100K in monthly sales, an interchange plus merchant could see an '
                              'effective rate under 1.5%, compared with the 2.5% or 2.9% Square or Stripe '
                              'keep charging as volume grows [cZ2DaswdAqo @ 00:08:22]. Crystal Little at '
                              'Paygent AI flips the flat-rate argument. She says card-not-present '
                              'e-commerce shops benefit most from flat rate because their underlying '
                              'interchange is already the highest. She even recommends splitting volume '
                              'across two processors: interchange plus for in-person payments and a flat '
                              'rate processor online [xTWy5shtdSk @ 00:12:34]. Subscription pricing draws '
                              'the widest split. CCSalesPro flags that processors mostly hand it to small '
                              'merchants who would pay only thirty dollars of markup on tier pricing '
                              'instead of a fifty-dollar subscription, and that extra network-access fees '
                              'get marked up on top [aZv0u_x9ipQ @ 00:01:19].',
                              "On the agent side, CCSalesPro's coaching call reframes the whole debate "
                              "around the agent's own books. Schedule A costs (interchange, card brand "
                              'dues and assessments, per-item costs and BIN sponsorship) are identical '
                              'whether you sell interchange plus, tiered, flat rate, surcharging or cash '
                              'discounting. That leaves revenue as the only question, and revenue depends '
                              'entirely on the level you price at. Interchange plus 90 basis points and 25 '
                              'cents earns a lot, while interchange plus five basis points and three cents '
                              'earns almost nothing [fb0PHmE8aCc @ 00:01:57]. For a debit-heavy merchant '
                              'with a 240-dollar average ticket, the coach lays out two plays. Go in with '
                              'interchange plus 40 basis points and 10 cents if the account is big. '
                              'Simplify to a flat 2.15% and 25 cents across the board if they run 20,000 a '
                              'month or less [fb0PHmE8aCc @ 00:08:29]. Contract terms split practitioners '
                              'too. David at MerchantAccounts.ca wants young merchants on month-to-month '
                              'interchange plus, but tells larger established merchants to trade a longer '
                              'contract term for a lower interchange markup [btemhvIers4 @ 00:05:27]. '
                              'Ahmad at Merchant Maverick, by contrast, ranks the early termination fee '
                              'among the worst junk fees. It runs from a hundred dollars to thousands, and '
                              'he says good processors do not charge one [h72ua8pD9cU @ 00:11:00].'],
               'table': {'caption': 'Side-by-side practitioner splits on pricing models, merchant fit, and '
                                    'contract strategy',
                         'headers': ['Debate Point', 'Camp A Position', 'Camp B Position', 'Expert Source'],
                         'rows': [['Is tiered pricing dishonest or just a different model',
                                   'Merchant Maverick calls tiered the least transparent, worst model and '
                                   'says get off it immediately',
                                   'BancardSales says tier and flat rate are situational, noting Stripe '
                                   'and Square claim transparent pricing',
                                   'Merchant Maverick ([h72ua8pD9cU @ 00:16:08]); BancardSales '
                                   '([5jk-0XxkiR0 @ 00:09:16])'],
                                  ['Is interchange plus always the best model for everyone',
                                   'MerchantAccounts.ca says literally no downside and every large '
                                   'merchant on earth belongs on it',
                                   'CCSalesPro says smaller merchants want simplicity and prefer one flat '
                                   'rate over fifty statement lines',
                                   'MerchantAccounts.ca ([btemhvIers4 @ 00:04:00]); CCSalesPro '
                                   '([fb0PHmE8aCc @ 00:03:06])'],
                                  ['Which merchant actually benefits most from flat rate pricing',
                                   'Merchant Maverick says newer low-volume businesses, getting expensive '
                                   'once volume climbs past 10K monthly',
                                   'Paygent AI says card-not-present e-commerce shops benefit most because '
                                   'their interchange is already highest',
                                   'Merchant Maverick ([h72ua8pD9cU @ 00:18:45]); Paygent AI ([xTWy5shtdSk '
                                   '@ 00:04:22])'],
                                  ['Is subscription or membership pricing a good deal for merchants',
                                   'Merchant Maverick calls membership pricing a great model for a certain '
                                   'volume and sale amount',
                                   'CCSalesPro says processors offer it mostly to small merchants who '
                                   'overpay fifty dollars versus thirty',
                                   'Merchant Maverick ([h72ua8pD9cU @ 00:17:37]); CCSalesPro ([aZv0u_x9ipQ '
                                   '@ 00:01:19])'],
                                  ['Should a card-present retail store ever use flat rate',
                                   'BancardSales says skip the 2.6% flat minimum when merchant accounts '
                                   'run over a point lower',
                                   'BancardSales flip side: startups and seasonal companies may prefer '
                                   'pay-as-you-go with no monthly fees',
                                   'BancardSales ([5jk-0XxkiR0 @ 00:07:58]); BancardSales ([5jk-0XxkiR0 @ '
                                   '00:08:27])'],
                                  ['When does tiered pricing actually make sense for a merchant',
                                   'Paygent AI says tiered fits B2B sellers and law offices with '
                                   'predictable transaction flow',
                                   'Paygent AI warns that when consumers pick any card freely, tiered '
                                   'becomes a roll of the dice',
                                   'Paygent AI ([xTWy5shtdSk @ 00:08:43]); Paygent AI ([xTWy5shtdSk @ '
                                   '00:09:19])'],
                                  ['Switch processors or just switch the pricing model in place',
                                   'Paygent AI says call your current processor first because it may offer '
                                   'all three models',
                                   'Merchant Maverick says choosing the right processor is the difference '
                                   'between getting swindled or treated fairly',
                                   'Paygent AI ([xTWy5shtdSk @ 00:10:09]); Merchant Maverick ([h72ua8pD9cU '
                                   '@ 00:05:07])']]},
               'key_metrics': [{'label': 'Interchange plus markup for large low-risk merchants',
                                'metric': 'Interchange plus markup for large low-risk merchants',
                                'value': '0.25% over interchange at $1M/month; 0.15% at $10M/month',
                                'confidence': 'attributed_practitioner_claim',
                                'context': 'David at MerchantAccounts.ca quotes lower markups as volume '
                                           'rises because the account needs less margin to service.',
                                'source': 'MerchantAccounts.ca ([btemhvIers4 @ 00:03:42])'},
                               {'label': 'Square card-present flat rate versus tier merchant account',
                                'metric': 'Square card-present flat rate versus tier merchant account',
                                'value': '2.6% + $0.10 versus an average below 1.8% on tier-based swiped '
                                         'transactions',
                                'confidence': 'attributed_practitioner_claim',
                                'context': 'Bryan Manning notes the trade-off: merchant accounts usually '
                                           'carry $10 to $25 monthly fees that Square does not charge.',
                                'source': 'BancardSales ([5jk-0XxkiR0 @ 00:05:45])'},
                               {'label': 'Interchange plus effective rate at $100K monthly sales',
                                'metric': 'Interchange plus effective rate at $100K monthly sales',
                                'value': 'Under 1.5% versus 2.5% to 2.9% on Square or Stripe',
                                'confidence': 'attributed_practitioner_claim',
                                'context': 'Helcim attributes the drop to a more predictable card mix at '
                                           'scale plus volume discounts on markup.',
                                'source': 'Helcim ([cZ2DaswdAqo @ 00:08:22])'}]},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The most expensive agent mistake is pricing a small-ticket account on '
                              'percentage alone. CCSalesPro tells of agents who sold a coffee shop a flat '
                              '3.5% across the board, opened their first residual statement, and found '
                              'they had lost money and owed it back to the processor [fb0PHmE8aCc @ '
                              '00:04:39]. The math is brutal. Regulated debit under the Durbin amendment '
                              'carries 22 cents, card brand fees add a couple of cents, and a five-cent '
                              'transaction fee rides on top. That puts roughly 33 cents of fixed cost on a '
                              'customer spending two dollars, about 15% of the ticket against a 3.5% '
                              "charge [fb0PHmE8aCc @ 00:05:08]. The coach's rule is that once the average "
                              'ticket drops below 15 bucks, flat or tier pricing needs real per-item fees '
                              'built in, or it will eat your lunch in a hurry. The second trap is trusting '
                              'a single month. A debit-heavy account showing a 1.99 effective rate looks '
                              'safe to flat-price near two percent and 25 cents. But if that month was a '
                              'fluke and the merchant starts running rewards and corporate cards at two '
                              'and a half to three percent, the margin shrinks very quickly. The safer '
                              'play is matching the existing tier sheet so the mid-qualified and '
                              'non-qualified buckets protect the margin [fb0PHmE8aCc @ 00:09:50].',
                              'On the statement, the biggest error James Shepherd at CCSalesPro sees on '
                              'tier pricing is reading the rates instead of the card mix. No industry rule '
                              'says which transactions go into which bucket. Some processors post a really '
                              'good qualified rate, put very few transactions there, and push most of the '
                              'volume into non-qualified, the highest rate [RxgrRsVThx4 @ 00:02:40]. His '
                              'benchmark is that a retailer, restaurant or auto repair shop should show '
                              '60% to 70% qualified, with the rest split fairly evenly between '
                              "mid-qualified and non-qualified. A pizza shop's phone orders belong in "
                              'mid-qualified, but anything far outside that pattern points to savings '
                              '[RxgrRsVThx4 @ 00:02:54]. Interchange plus has its own trap. If the '
                              'statement never shows a total interchange amount, Shepherd calls it '
                              'suspicious. If total interchange divided by total volume sits far from the '
                              'roughly 1.7% national average, it may be what he calls interchange plus '
                              'plus: marked-up interchange with hidden costs buried in the table '
                              '[2Sn4XMqpW4I @ 00:04:13]. The markup check is total fees minus total '
                              'interchange, divided by volume. At 20,000 to 40,000 a month, a markup above '
                              'about 0.7% is most likely not competitive. Even 0.3% at 60,000 and up can '
                              'probably be beaten [2Sn4XMqpW4I @ 00:06:40].',
                              'Merchant-side traps cluster in the flat-fee lines. Ahmad at Merchant '
                              'Maverick calls a terminal lease an absolutely horrible deal that ends up '
                              'costing thousands of dollars for a 200 to 300 dollar piece of equipment. '
                              "His rule is simple: don't ever get a terminal lease [h72ua8pD9cU @ "
                              '00:09:20]. PaymentCloud warns that many processors implement annual rate '
                              'increases, usually announced by a notice on the statement two to three '
                              'months before they hit. It tells merchants to watch leasing and equipment '
                              'fees, compliance and regulatory fees, PCI fees and monthly access fees to '
                              'make sure they do not creep up [xfBalp9Zzio @ 00:04:53]. The same team '
                              'calls chargebacks financial gremlins that nibble away at profits and can '
                              'ultimately get the merchant account terminated. High-risk accounts can also '
                              'have a percentage of sales held in a separate non-interest-bearing reserve '
                              "account [xfBalp9Zzio @ 00:03:25]. Merchant Maverick's Maverick Minute adds "
                              'a red flag for sales pitches: be careful if a merchant account rep offers a '
                              'discount on the standard published interchange rates. The only way to '
                              'eliminate or reduce interchange is to pass it on to customers, which '
                              'Merchant Maverick calls a whole other can of worms [dUz90pAXTm0 @ '
                              '00:03:58].'],
               'table': {'caption': 'Firsthand failure modes, warning signs, and the unit economics behind '
                                    'each trap',
                         'headers': ['Failure Mode',
                                     'What Happened Or Warning Sign',
                                     'Economics Check',
                                     'Expert Source'],
                         'rows': [['Flat-rating a small-ticket coffee shop at 3.5% across the board',
                                   'Agents opened their first residual statement and owed money back to '
                                   'the processor',
                                   'About 33 cents of fixed cost on a two-dollar ticket equals roughly 15%',
                                   'CCSalesPro ([fb0PHmE8aCc @ 00:04:55])'],
                                  ['Pricing a flat rate off one fluke debit-heavy month',
                                   'Flat near two percent on a 1.99 effective account leaves no '
                                   'rewards-card cushion',
                                   'Rewards and corporate cards can cost two and a half to three percent '
                                   'quickly',
                                   'CCSalesPro ([fb0PHmE8aCc @ 00:09:50])'],
                                  ['Reading tier rates while ignoring the actual card mix',
                                   'Processor posts a great qualified rate but routes most volume into '
                                   'non-qualified',
                                   'Physical-location businesses should run 60% to 70% qualified '
                                   'transactions',
                                   'CCSalesPro ([RxgrRsVThx4 @ 00:02:54])'],
                                  ['Interchange plus plus hiding inside an interchange table',
                                   'Missing total interchange line, or interchange far off the national '
                                   'average',
                                   'Total interchange divided by volume should land near 1.6% to 1.8%',
                                   'CCSalesPro ([2Sn4XMqpW4I @ 00:02:41])'],
                                  ['Subscription pricing with marked-up network access fees stacked on top',
                                   'Merchant pays the fifty-dollar subscription plus extra markup without '
                                   'really knowing it',
                                   'The same small merchant might pay only thirty dollars of markup on '
                                   'tiers',
                                   'CCSalesPro ([aZv0u_x9ipQ @ 00:02:05])'],
                                  ['Leasing a credit card terminal instead of buying outright',
                                   'Lease ends up costing thousands of dollars for a cheap piece of '
                                   'equipment',
                                   'Buying outright typically runs about 150 to 350 dollars per terminal',
                                   'Merchant Maverick ([h72ua8pD9cU @ 00:09:20]); Merchant Maverick '
                                   '([h72ua8pD9cU @ 00:09:06])'],
                                  ["Missing the processor's annual rate increase notice on statements",
                                   'Processors announce yearly increases two to three months ahead on the '
                                   'statement',
                                   'Watch leasing, PCI, compliance and monthly access fees for quiet creep',
                                   'PaymentCloud ([xfBalp9Zzio @ 00:04:22])']]},
               'key_metrics': [{'label': 'Fixed cost on a two-dollar coffee shop ticket',
                                'metric': 'Fixed cost on a two-dollar coffee shop ticket',
                                'value': 'About $0.33 per transaction, roughly 15% of the sale',
                                'confidence': 'attributed_practitioner_claim',
                                'context': 'Regulated debit at 22 cents plus card brand fees plus a '
                                           'five-cent transaction fee wiped out a 3.5% flat rate.',
                                'source': 'CCSalesPro ([fb0PHmE8aCc @ 00:05:08])'},
                               {'label': 'Interchange share of total processing cost',
                                'metric': 'Interchange share of total processing cost',
                                'value': 'Roughly 70% to 90%',
                                'confidence': 'attributed_practitioner_claim',
                                'context': 'Merchant Maverick says interchange is the single largest '
                                           'expense, with the rest going to the processor and card '
                                           'association.',
                                'source': 'Merchant Maverick ([dUz90pAXTm0 @ 00:02:30])'},
                               {'label': 'Competitive markup benchmark by monthly volume',
                                'metric': 'Competitive markup benchmark by monthly volume',
                                'value': 'Above ~0.7% at $20K-$40K/month likely not competitive; ~0.3% at '
                                         '$60K+ may still be beaten',
                                'confidence': 'attributed_practitioner_claim',
                                'context': 'Markup is total fees minus total interchange, divided by total '
                                           'volume; 1% to 1.5% is not unusual under $10K/month.',
                                'source': 'CCSalesPro ([2Sn4XMqpW4I @ 00:06:40])'}],
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Pre-Quote Kill Checks',
                           'body': 'Run these four checks on every statement before you put a number in '
                                   'front of a merchant. Each one comes from a practitioner who watched an '
                                   'account or a margin blow up.',
                           'items': ['Never quote flat or tier pricing on an average ticket under 15 '
                                     'dollars without per-item fees that cover the 22-cent regulated debit '
                                     'cost [CCSalesPro — fb0PHmE8aCc @ 00:05:24].',
                                     'Check card mix before rates: a physical-location statement running '
                                     'well under 60% to 70% qualified means the buckets are stacked '
                                     'against the merchant [CCSalesPro — RxgrRsVThx4 @ 00:02:54].',
                                     'Treat any interchange plus statement without a total interchange '
                                     'figure as suspicious, then subtract interchange from total fees to '
                                     'expose the real markup [CCSalesPro — 2Sn4XMqpW4I @ 00:05:13].',
                                     'Walk away from any rep promising a discount on standard published '
                                     'interchange rates, since interchange only goes away by passing it to '
                                     'customers [Merchant Maverick — dUz90pAXTm0 @ 00:03:58].']}}],
 'pull_quote': '"You got to make sure you have some per item fees in there because if you don\'t that can '
               'really eat your lunch in a hurry." - CCSalesPro (fb0PHmE8aCc @ 00:05:39).',
 'diagram_id': 'diag-04',
 'action_checklist': ['Calculate the effective rate (total fees divided by total volume) on every '
                      'statement and use it as the single number to compare any two providers '
                      '[BancardSales — 5jk-0XxkiR0 @ 00:11:32].',
                      'Divide total interchange by total volume and compare it against the roughly 1.7% '
                      'average to catch marked-up interchange [CCSalesPro — 2Sn4XMqpW4I @ 00:03:03].',
                      'Subtract total interchange from total fees, divide by volume, and test that markup '
                      'against the volume benchmarks before quoting [CCSalesPro — 2Sn4XMqpW4I @ 00:06:22].',
                      'On tier statements, move the merchant from one blended qualified rate to split '
                      'debit and credit qualified rates on 4-tier pricing [CCSalesPro — RxgrRsVThx4 @ '
                      '00:06:55].',
                      'Strike junk fees: a statement fee charged on top of the monthly fee, online '
                      'reporting fees, debit network fees, and monthly minimums negotiated to zero '
                      '[Merchant Maverick — h72ua8pD9cU @ 00:11:27].',
                      'Push card acceptance best practices that qualify transactions for lower '
                      'interchange: AVS, CVV and zip entry, daily settlement, swiping or dipping, and '
                      'voids instead of refunds [BancardSales — AseZioaNb5s @ 00:05:14].'],
 'statutory_citations': [{'title': 'Merchant Maverick — Credit Card Processing Fees and Rates Explained '
                                   '[00:16:08]',
                          'url': 'https://www.youtube.com/watch?v=h72ua8pD9cU&t=968s',
                          'relevance': 'Primary practitioner testimony on why tiered pricing is the least '
                                       'transparent model and which junk fees to strip.'},
                         {'title': 'CCSalesPro — Choosing The Right Pricing Structure: Tiered Pricing VS. '
                                   'Interchange Plus [00:04:22]',
                          'url': 'https://www.youtube.com/watch?v=fb0PHmE8aCc&t=262s',
                          'relevance': 'Primary practitioner testimony on the coffee shop flat-rate '
                                       'residual loss and agent pricing plays.'},
                         {'title': 'BancardSales — Merchant Account Rates & Pricing - Interchange Plus, '
                                   'Tier Based & Flat Rate Comparison [00:09:16]',
                          'url': 'https://www.youtube.com/watch?v=5jk-0XxkiR0&t=556s',
                          'relevance': 'Primary practitioner testimony disputing that tier and flat rate '
                                       'pricing are dishonest and naming effective rate as the '
                                       'tiebreaker.'},
                         {'title': 'CCSalesPro — What is Interchange Plus or Cost Plus Pricing - Merchant '
                                   'Services [00:04:13]',
                          'url': 'https://www.youtube.com/watch?v=2Sn4XMqpW4I&t=253s',
                          'relevance': 'Primary practitioner testimony on detecting interchange plus plus '
                                       'and benchmarking markup by volume.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'AseZioaNb5s',
                       'title': 'Merchant Account Pricing -  What Is Interchange - Fees, Rates and Why '
                                "it's important to you!",
                       'channel': 'BancardSales',
                       'author': 'BancardSales',
                       'text': 'Interchange optimization is not available with aggregator payment services '
                               'like Stripe, PayPal or Square.',
                       'tip': 'Interchange optimization is not available with aggregator payment services '
                              'like Stripe, PayPal or Square.',
                       'timestamp': 347,
                       'timestamp_seconds': 347,
                       'timestamp_label': '[00:05:47]',
                       'url': 'https://www.youtube.com/watch?v=AseZioaNb5s&t=347s',
                       'markdown': '[00:05:47](https://www.youtube.com/watch?v=AseZioaNb5s&t=347s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '5jk-0XxkiR0',
                       'title': 'Merchant Account Rates & Pricing - Interchange Plus, Tier Based & Flat '
                                'Rate Comparison',
                       'channel': 'BancardSales',
                       'author': 'BancardSales',
                       'text': 'All of these pricing models will yield an effective rate, one single rate '
                               'at the end of the month, and this effective rate is the only undisputed '
                               'rate by which every single merchant account provider and rate program can '
                               'be compared.',
                       'tip': 'All of these pricing models will yield an effective rate, one single rate '
                              'at the end of the month, and this effective rate is the only undisputed '
                              'rate by which every single merchant account provider and rate program can '
                              'be compared.',
                       'timestamp': 692,
                       'timestamp_seconds': 692,
                       'timestamp_label': '[00:11:32]',
                       'url': 'https://www.youtube.com/watch?v=5jk-0XxkiR0&t=692s',
                       'markdown': '[00:11:32](https://www.youtube.com/watch?v=5jk-0XxkiR0&t=692s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'fb0PHmE8aCc',
                       'title': 'Choosing The Right Pricing Structure: Tiered Pricing VS. Interchange Plus',
                       'channel': 'CCSalesPro',
                       'author': 'CCSalesPro',
                       'text': 'I know agents that have sold a coffee shop on flat rate pricing at say '
                               '3.5, and they get their first residual statement and find out that they '
                               'owe money back to the processor.',
                       'tip': 'I know agents that have sold a coffee shop on flat rate pricing at say 3.5, '
                              'and they get their first residual statement and find out that they owe '
                              'money back to the processor.',
                       'timestamp': 262,
                       'timestamp_seconds': 262,
                       'timestamp_label': '[00:04:22]',
                       'url': 'https://www.youtube.com/watch?v=fb0PHmE8aCc&t=262s',
                       'markdown': '[00:04:22](https://www.youtube.com/watch?v=fb0PHmE8aCc&t=262s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'dUz90pAXTm0',
                       'title': 'Merchant Account Pricing: Interchange Fees Explained',
                       'channel': 'Merchant Maverick',
                       'author': 'Merchant Maverick',
                       'text': 'Be careful if a sales representative from a merchant account service '
                               'provider offers you a discount on the standard published interchange '
                               'rates.',
                       'tip': 'Be careful if a sales representative from a merchant account service '
                              'provider offers you a discount on the standard published interchange rates.',
                       'timestamp': 238,
                       'timestamp_seconds': 238,
                       'timestamp_label': '[00:03:58]',
                       'url': 'https://www.youtube.com/watch?v=dUz90pAXTm0&t=238s',
                       'markdown': '[00:03:58](https://www.youtube.com/watch?v=dUz90pAXTm0&t=238s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'h72ua8pD9cU',
                       'title': 'Credit Card Processing Fees and Rates Explained',
                       'channel': 'Merchant Maverick',
                       'author': 'Merchant Maverick',
                       'text': 'Tiered pricing is the least transparent pricing model, the worst one you '
                               'can be on, and by no means should you ever be on tiered pricing.',
                       'tip': 'Tiered pricing is the least transparent pricing model, the worst one you '
                              'can be on, and by no means should you ever be on tiered pricing.',
                       'timestamp': 968,
                       'timestamp_seconds': 968,
                       'timestamp_label': '[00:16:08]',
                       'url': 'https://www.youtube.com/watch?v=h72ua8pD9cU&t=968s',
                       'markdown': '[00:16:08](https://www.youtube.com/watch?v=h72ua8pD9cU&t=968s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'cZ2DaswdAqo',
                       'title': 'Interchange Plus: The "Secret" Pricing Model That Saves Your Business '
                                'Thousands',
                       'channel': 'Helcim',
                       'author': 'Helcim',
                       'text': "If you're processing 100K in monthly sales, you could see your effective "
                               'processing rate decrease to less than 1.5%, far better than continuing to '
                               'pay Square or Stripe that 2.5 or 2.9%.',
                       'tip': "If you're processing 100K in monthly sales, you could see your effective "
                              'processing rate decrease to less than 1.5%, far better than continuing to '
                              'pay Square or Stripe that 2.5 or 2.9%.',
                       'timestamp': 502,
                       'timestamp_seconds': 502,
                       'timestamp_label': '[00:08:22]',
                       'url': 'https://www.youtube.com/watch?v=cZ2DaswdAqo&t=502s',
                       'markdown': '[00:08:22](https://www.youtube.com/watch?v=cZ2DaswdAqo&t=502s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'RxgrRsVThx4',
                       'title': 'How to Read a Merchant Statement   Tier Pricing',
                       'channel': 'CCSalesPro',
                       'author': 'CCSalesPro',
                       'text': "If you're a physical location business, 60 to 70% of your transactions "
                               'should be qualified, and the others should be split fairly evenly between '
                               'non-qualified and mid-qualified.',
                       'tip': "If you're a physical location business, 60 to 70% of your transactions "
                              'should be qualified, and the others should be split fairly evenly between '
                              'non-qualified and mid-qualified.',
                       'timestamp': 174,
                       'timestamp_seconds': 174,
                       'timestamp_label': '[00:02:54]',
                       'url': 'https://www.youtube.com/watch?v=RxgrRsVThx4&t=174s',
                       'markdown': '[00:02:54](https://www.youtube.com/watch?v=RxgrRsVThx4&t=174s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '2Sn4XMqpW4I',
                       'title': 'What is Interchange Plus or Cost Plus Pricing - Merchant Services',
                       'channel': 'CCSalesPro',
                       'author': 'CCSalesPro',
                       'text': 'If the interchange amount is dramatically different than the interchange '
                               'amount on the statement, it might be interchange plus plus pricing, '
                               'meaning the interchange might be marked up a little bit.',
                       'tip': 'If the interchange amount is dramatically different than the interchange '
                              'amount on the statement, it might be interchange plus plus pricing, meaning '
                              'the interchange might be marked up a little bit.',
                       'timestamp': 253,
                       'timestamp_seconds': 253,
                       'timestamp_label': '[00:04:13]',
                       'url': 'https://www.youtube.com/watch?v=2Sn4XMqpW4I&t=253s',
                       'markdown': '[00:04:13](https://www.youtube.com/watch?v=2Sn4XMqpW4I&t=253s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'XXH81AbZQcg',
                       'title': 'What Is Tiered Pricing? Merchant Services Pricing Explained',
                       'channel': 'Joe Wagner | Merchant Services & Passive Income',
                       'author': 'Joe Wagner | Merchant Services & Passive Income',
                       'text': "If a merchant is still on tiered pricing, they likely haven't had their "
                               "fees reviewed in years, they're almost always overpaying, and you have a "
                               'huge opportunity to save them money.',
                       'tip': "If a merchant is still on tiered pricing, they likely haven't had their "
                              "fees reviewed in years, they're almost always overpaying, and you have a "
                              'huge opportunity to save them money.',
                       'timestamp': 71,
                       'timestamp_seconds': 71,
                       'timestamp_label': '[00:01:11]',
                       'url': 'https://www.youtube.com/watch?v=XXH81AbZQcg&t=71s',
                       'markdown': '[00:01:11](https://www.youtube.com/watch?v=XXH81AbZQcg&t=71s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'qBBgFNiTDYg',
                       'title': 'What is Interchange Plus Pricing? | Payments Insights',
                       'channel': 'CCSalesPro',
                       'author': 'CCSalesPro',
                       'text': 'Interchange plus pricing is almost always used with merchants who do more '
                               'than 100,000 a month in credit card processing volume.',
                       'tip': 'Interchange plus pricing is almost always used with merchants who do more '
                              'than 100,000 a month in credit card processing volume.',
                       'timestamp': 181,
                       'timestamp_seconds': 181,
                       'timestamp_label': '[00:03:01]',
                       'url': 'https://www.youtube.com/watch?v=qBBgFNiTDYg&t=181s',
                       'markdown': '[00:03:01](https://www.youtube.com/watch?v=qBBgFNiTDYg&t=181s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'XEaaN73nJ6Q',
                       'title': 'What is Tiered Pricing? | Payments Insights',
                       'channel': 'CCSalesPro',
                       'author': 'CCSalesPro',
                       'text': "If you're looking at an interchange table and there's only like three or "
                               "four rates on there, you're probably looking at tiered pricing that's "
                               'displayed like an interchange table.',
                       'tip': "If you're looking at an interchange table and there's only like three or "
                              "four rates on there, you're probably looking at tiered pricing that's "
                              'displayed like an interchange table.',
                       'timestamp': 399,
                       'timestamp_seconds': 399,
                       'timestamp_label': '[00:06:39]',
                       'url': 'https://www.youtube.com/watch?v=XEaaN73nJ6Q&t=399s',
                       'markdown': '[00:06:39](https://www.youtube.com/watch?v=XEaaN73nJ6Q&t=399s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'btemhvIers4',
                       'title': 'What is Interchange Plus Pricing?',
                       'channel': 'MerchantAccounts.ca',
                       'author': 'MerchantAccounts.ca',
                       'text': 'If a merchant was processing a million dollars per month for a low risk '
                               "product maybe I would quote them 0.25 over interchange, and if they're "
                               'doing 10 million dollars a month maybe 0.15 over interchange.',
                       'tip': 'If a merchant was processing a million dollars per month for a low risk '
                              "product maybe I would quote them 0.25 over interchange, and if they're "
                              'doing 10 million dollars a month maybe 0.15 over interchange.',
                       'timestamp': 222,
                       'timestamp_seconds': 222,
                       'timestamp_label': '[00:03:42]',
                       'url': 'https://www.youtube.com/watch?v=btemhvIers4&t=222s',
                       'markdown': '[00:03:42](https://www.youtube.com/watch?v=btemhvIers4&t=222s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'bdumFSr4sA8',
                       'title': 'Understanding Merchant Statements and Fees',
                       'channel': 'CCSalesPro',
                       'author': 'CCSalesPro',
                       'text': 'The card brands collect dues and assessments, generally 13 to 15 basis '
                               'points plus around 2 cents, and they have a bunch of other fees like a per '
                               'location fee and international assessments that can really stack up.',
                       'tip': 'The card brands collect dues and assessments, generally 13 to 15 basis '
                              'points plus around 2 cents, and they have a bunch of other fees like a per '
                              'location fee and international assessments that can really stack up.',
                       'timestamp': 291,
                       'timestamp_seconds': 291,
                       'timestamp_label': '[00:04:51]',
                       'url': 'https://www.youtube.com/watch?v=bdumFSr4sA8&t=291s',
                       'markdown': '[00:04:51](https://www.youtube.com/watch?v=bdumFSr4sA8&t=291s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'xfBalp9Zzio',
                       'title': 'Understanding Your Merchant Statement: Everything They Don’t Want You To '
                                'Know',
                       'channel': 'PaymentCloud',
                       'author': 'PaymentCloud',
                       'text': 'Many processors implement annual rate increases, and typically a notice '
                               'will be included on your statement 2 to 3 months before any increase '
                               'happens.',
                       'tip': 'Many processors implement annual rate increases, and typically a notice '
                              'will be included on your statement 2 to 3 months before any increase '
                              'happens.',
                       'timestamp': 262,
                       'timestamp_seconds': 262,
                       'timestamp_label': '[00:04:22]',
                       'url': 'https://www.youtube.com/watch?v=xfBalp9Zzio&t=262s',
                       'markdown': '[00:04:22](https://www.youtube.com/watch?v=xfBalp9Zzio&t=262s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'xTWy5shtdSk',
                       'title': 'Flat Rate vs Interchange Plus vs Tiered Pricing — What Merchants Need to '
                                'Know',
                       'channel': 'Paygent AI',
                       'author': 'Paygent AI',
                       'text': 'Maybe it makes sense for your business to have two processors, one that is '
                               'a certain pricing model for some of your transactions and another that is '
                               'a different one.',
                       'tip': 'Maybe it makes sense for your business to have two processors, one that is '
                              'a certain pricing model for some of your transactions and another that is a '
                              'different one.',
                       'timestamp': 737,
                       'timestamp_seconds': 737,
                       'timestamp_label': '[00:12:17]',
                       'url': 'https://www.youtube.com/watch?v=xTWy5shtdSk&t=737s',
                       'markdown': '[00:12:17](https://www.youtube.com/watch?v=xTWy5shtdSk&t=737s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'aZv0u_x9ipQ',
                       'title': 'Cost Structures - Subscription Rate Pricing - How to Sell Merchant '
                                'Services',
                       'channel': 'CCSalesPro',
                       'author': 'CCSalesPro',
                       'text': "There's two big problems with subscription rate pricing, and first of all "
                               "most processors only offer it to very small merchants who don't actually "
                               'pay that much in markup on a traditional cost structure.',
                       'tip': "There's two big problems with subscription rate pricing, and first of all "
                              "most processors only offer it to very small merchants who don't actually "
                              'pay that much in markup on a traditional cost structure.',
                       'timestamp': 61,
                       'timestamp_seconds': 61,
                       'timestamp_label': '[00:01:01]',
                       'url': 'https://www.youtube.com/watch?v=aZv0u_x9ipQ&t=61s',
                       'markdown': '[00:01:01](https://www.youtube.com/watch?v=aZv0u_x9ipQ&t=61s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'}]}
