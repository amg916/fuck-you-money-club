from __future__ import annotations

CHAPTER_3 = {'id': 'Q3',
 'chapter_id': 'Q3',
 'chapter_number': 3,
 'question_number': 3,
 'slug': 'inside-the-pro-prediction-market-desk',
 'question_prompt': 'What separates winning prediction-market traders and trading teams from the losing '
                    'majority, and how do they run their operation?',
 'kicker': 'Q3 / THE BIG MONEY PLAYBOOKS',
 'title': 'Inside the Pro Prediction-Market Desk',
 'subtitle': 'Microstructure of wealth transfer across 72M Kalshi trades, three years of Polymarket data, '
             '$286-to-$1M and $100-to-$1M case studies, quant and fully manual strategies, building '
             'trading teams and tech, political/Iran market analysis, Gen Z trading firms, and '
             'sports-betting tax treatment for pros',
 'layout_template': 'financial_analysis',
 'reading_time_minutes': 15,
 'executive_summary': 'Pro prediction-market desks agree the edge is structural: retail buys emotional YES '
                      "longshots, makers harvest them, and exchanges do not limit winners. Becker's "
                      '72M-trade Kalshi dataset shows 5-cent contracts winning 4.18% of the time and '
                      'makers earning about +2.5% per trade, while only 22% of markets resolve YES. Street '
                      "mechanics run from Clay's fully manual first-touchdown quoting at about $3K per "
                      "primetime game and roughly 10% ROI on $60M volume, to Steven's RFQ combo desk where "
                      '40-plus NFL makers make five milliseconds decisive. InGenius by Veritasium finds '
                      'market makers averaging $11,831 versus $3,243 for skilled winners. Disagreements '
                      'center on taking versus making, with Steven still earning 7-8% taking against 2-3% '
                      'making, on whether copying RFQ quotes works, and on whether competition has flipped '
                      'the edge toward YES.',
 'key_metrics': [{'label': 'Five-Cent Longshot Win Rate',
                  'metric': 'Five-Cent Longshot Win Rate',
                  'value': '4.18%',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "How often 5-cent Kalshi contracts actually win across Jonathan Becker's 72 "
                             'million trade dataset; NO bought at 94 cents wins 95% of the time.',
                  'source': 'Part Time Larry ([vT0qMNgOkxo @ 00:04:34])'},
                 {'label': 'Maker Excess Return Per Trade',
                  'metric': 'Maker Excess Return Per Trade',
                  'value': 'About +2.5% for makers, about -2.5% for takers',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Maker versus taker excess return on Kalshi, with Reichenbach and Walther '
                             '(2025) finding the same pattern on Polymarket.',
                  'source': 'Part Time Larry ([vT0qMNgOkxo @ 00:05:36])'},
                 {'label': 'Manual Trader Volume and ROI',
                  'metric': 'Manual Trader Volume and ROI',
                  'value': 'About $60M volume at roughly 10% ROI',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Clay's self-reported lifetime volume and ROI from a fully manual, 80-85% "
                             "maker style; the leaderboard's 27M figure is called wrong.",
                  'source': 'Inside Prediction Markets ([tM5MKtoBoZ0 @ 00:19:59])'},
                 {'label': 'Market Maker vs Skilled Winner Profit',
                  'metric': 'Market Maker vs Skilled Winner Profit',
                  'value': '$11,831 average for market makers vs $3,243 for skilled winners',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Average profit over two years of Polymarket data; the top 0.1% of accounts '
                             'act as makers about half the time.',
                  'source': 'InGenius by Veritasium ([CTUqmUHvd2Y @ 00:22:13])'}],
 'sections': [{'section': 1,
               'heading': 'The Practitioner Consensus',
               'paragraphs': ['The loudest point of agreement across the desk is that retail order flow '
                              'carries a structural YES and longshot bias that pros harvest. Jonathan '
                              "Becker's dataset of 72 million Kalshi trades, walked through by Part Time "
                              'Larry, shows 5-cent contracts actually winning only 4.18% of the time, '
                              'while NO bought at 94 cents wins 95% of the time [vT0qMNgOkxo @ 00:04:34]. '
                              "Larry's own Rockets YES bought at 7% sank to 4%, turning $43 into $24, and "
                              'the summary is blunt: usually the boring outcome wins, nothing ever happens '
                              '[vT0qMNgOkxo @ 00:16:37]. Larry calls late cheap YES buying pouring money '
                              "into a dead bet. Three Markets lands in the same place: fabiano.soul's "
                              'count shows only 22% of markets resolve YES, and the play is buying NO '
                              'early in a 90/10 market because it tends to drift to 95/5 [DvHXWcq2iWc @ '
                              '00:02:17]. Semi, profiled with P&L over $1M from a $286 deposit in June '
                              '2024, calls the approach reverse stupidity: fading sensationalism bias. '
                              "InGenius by Veritasium's three-year Polymarket study adds that the skilled "
                              'winners, roughly 3% of accounts, avoid overpriced longshots and favour '
                              'favourites [CTUqmUHvd2Y @ 00:20:52]. The shared rule: treat emotional YES '
                              'buying as the flow you trade against.',
                              "Second consensus point: live on the maker side of the book. Becker's data "
                              'shows makers earning about +2.5% excess return per trade while takers lose '
                              'about the same, and Reichenbach and Walther (2025) found the identical '
                              "split on Polymarket [vT0qMNgOkxo @ 00:05:36]. Becker's own custom NBA "
                              'script found roughly $7M in taker losses. InGenius by Veritasium measured '
                              'skilled directional winners averaging $3,243 of profit over two years '
                              'against $11,831 for market makers, with the top 0.1% of accounts acting as '
                              'makers about half the time [CTUqmUHvd2Y @ 00:22:13]. The working pros on '
                              'Inside Prediction Markets back it with their own books. Clay, the fully '
                              'manual trader out of Princeton, New Jersey, runs 80-85% maker and calls the '
                              'process completely manual [tM5MKtoBoZ0 @ 00:12:30]. Steven, the part-time '
                              'market maker who crossed $1M in P&L, flipped from 95% taking in January to '
                              'roughly 20% taking and 80% making, mostly RFQs on combos plus niche markets '
                              'such as NASCAR. The nuance the pros add is that making is the volume '
                              'engine, not automatically the fattest margin: Steven still books about 7-8% '
                              'ROI taking against 2-3% making, and the taking P&L still leads the account '
                              '[ieRL4BXtMGA @ 00:06:55]. Making buys scale; selective taking still pays '
                              'the bills.',
                              'The third pillar is venue logic: sharps migrated because prediction markets '
                              'take their action instead of cutting them off. Troy Cooks of OddsJam, a pro '
                              'for two to three years who made over $250K in 2025, puts it simply: '
                              'sportsbooks hate winners, while peer-to-peer exchanges like Novig charge '
                              'fees and could care less how much you profit [zMU9NWt0gdE @ 00:02:38]. '
                              'Cooks also pitches these as the newest and least efficient markets, with '
                              'insider flow visible because every portfolio is public, and reports about '
                              '$20K in 30 days from arbitrage, +EV and the tool. Steven adds that offshore '
                              'books are in a slow death of limits, slow pay and 15-second timers '
                              '[ieRL4BXtMGA @ 00:12:00]. NBC News frames the structural driver: CFTC '
                              'federal oversight lets users in even where sports gambling is illegal, '
                              'while sportsbooks carry large capital reserves and tight regulation, and '
                              "the segment's critic warns the regulatory gate is completely down "
                              "[APN3zwcwPdQ @ 00:01:52]. Where to hunt is also agreed: Becker's data flags "
                              'entertainment, crypto and sports as inefficient and finance as efficient '
                              '[vT0qMNgOkxo @ 00:12:34]. The baseline prerequisite is cultural as much as '
                              'technical: think like the casino, diversify across a large number of bets, '
                              'and accept that longshots sometimes hit.'],
               'table': {'caption': 'Where the pro desk agrees: structural edges and baseline '
                                    'prerequisites',
                         'headers': ['Consensus Point',
                                     'What the Practitioner Reported',
                                     'Desk Application',
                                     'Expert Source'],
                         'rows': [['Fade emotional YES longshots on Kalshi',
                                   'Five-cent Kalshi contracts win only 4.18% of the time across 72M '
                                   'trades',
                                   'Buy NO on 5-10 cent emotional longshots using maker limit orders',
                                   'Part Time Larry ([vT0qMNgOkxo @ 00:04:34])'],
                                  ['Most markets resolve NO over time',
                                   'Only 22% of markets resolve YES; 90/10 markets tend to drift to 95/5',
                                   'Enter NO early in lopsided markets before the drift completes',
                                   'Three Markets – The Prediction Market Podcast ([DvHXWcq2iWc @ '
                                   '00:02:17])'],
                                  ['Makers beat takers on every venue',
                                   'Makers earn about +2.5% excess return per trade while takers lose '
                                   'similar',
                                   'Rest limit orders instead of crossing the spread on every entry',
                                   'Part Time Larry ([vT0qMNgOkxo @ 00:05:36])'],
                                  ['Market makers out-earn skilled directional winners',
                                   'Market makers average $11,831 versus $3,243 for skilled winners over '
                                   'two years',
                                   'Build a quoting operation rather than relying on directional calls '
                                   'alone',
                                   'InGenius by Veritasium ([CTUqmUHvd2Y @ 00:22:13])'],
                                  ['Exchanges do not limit winning accounts',
                                   'Sportsbooks hate winners; peer-to-peer exchanges charge fees and do '
                                   'not limit',
                                   'Route sharp volume to exchanges once sportsbook accounts get limited',
                                   'OddsJam: Sports Betting Strategy & Education ([zMU9NWt0gdE @ '
                                   '00:02:38])'],
                                  ['Selective taking still carries the margin',
                                   'Taking returns about 7-8% ROI versus 2-3% making, and taking P&L leads',
                                   'Run making for volume but keep selective taking for margin',
                                   'Inside Prediction Markets ([ieRL4BXtMGA @ 00:06:55])'],
                                  ['Hunt inefficient emotional categories, skip finance',
                                   'Entertainment, crypto and sports are inefficient while finance markets '
                                   'are efficient',
                                   'Concentrate hunting in emotional categories and skip finance contracts '
                                   'entirely',
                                   'Part Time Larry ([vT0qMNgOkxo @ 00:12:34])']]}},
              {'section': 2,
               'heading': 'Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ["Clay's first-touchdown playbook is the most granular manual workflow on the "
                              'desk. Quote the top 10 players, price the team without the ball at the '
                              'pregame line minus about 4 cents for roughly 5% ROI per player, refill in '
                              '900-contract lots, and before each snap drop the team with the ball to 1 '
                              'cent before repricing after the play [tM5MKtoBoZ0 @ 00:14:55]. The take '
                              'runs about $3K per primetime game, net negative in only two or three games '
                              'a year, but Clay got courtsided at 4,000 contracts and 95 cents and now '
                              'says that edge is dead [tM5MKtoBoZ0 @ 00:18:24]. The live focus has shifted '
                              'to end-of-game football, the highest-ROI window because people have no idea '
                              "what they're doing, plus hockey, tennis, soccer and Chinese basketball. "
                              'Clay listens to referee audio rather than trusting sportsbook data feeds. '
                              'Liquidity has transformed underneath all of it: early Kalshi college '
                              'football spreads were 3-4 cents wide, and now roughly $70K sits at a 1-cent '
                              'spread [tM5MKtoBoZ0 @ 00:10:42]. Novig goes further, with Henry and Chris '
                              'pointing to 300-500K-contract walls quoted a penny wide with no fees '
                              '[ZmMVHubZpns @ 00:06:04]. Clay pegs fair margins at 2-4% live and 1-2% '
                              'pregame, and says landing in a 5% range is quite profitable.',
                              "Steven's RFQ operation shows how fast quoting edges compress. RFQ started "
                              'at the end of May, the World Cup made June and July easy, and from August '
                              'competitors began offering 0.1% hold, pushing the focus to latency and '
                              'combo quoting [ieRL4BXtMGA @ 00:08:22]. Pricing is about 80% top down, and '
                              'some NFL markets carry 40-plus makers, so being five milliseconds behind '
                              'means getting nothing [ieRL4BXtMGA @ 00:22:05]. Steven expects proprietary '
                              'pricing to matter within three to four months, because low-hold SGP quotes '
                              'suggest rivals originate their own numbers. The build is one developer '
                              "working with Steven for nine months, because Steven's own builds were "
                              'garbage, with developers originally sourced through coaching calls. Michael '
                              'Hoffman, head of engineering on the Inside Prediction Markets trading team, '
                              'came from StoneX FIX connectivity into about 100 exchanges, hires for '
                              'distributed systems and messaging-bus skills, and discounts big-tech '
                              'candidates [4UVkZUKEmPI @ 00:35:53]. Clay runs the opposite stack: no '
                              'models, intuition only, and no appetite for troubleshooting, which makes '
                              'tooling cost a real line item. Multi-venue order-book software runs about '
                              "$0.02 per contract, tiered, which on Clay's roughly $5M a month of volume "
                              'would cost more than $10K [tM5MKtoBoZ0 @ 00:25:32]. Hoffman stays black '
                              'boxed from pricing entirely, walling engineering off from the trading book.',
                              'The contract math is simple. Event contracts pay $1 or $0, so YES at 67 '
                              "cents plus NO at 33 cents equals a dollar, and InGenius by Veritasium's "
                              'spread-capture template is to model 67% fair value, bid YES at 65 cents and '
                              'NO at 31 cents, pay 96 cents and lock 4 cents, with the risk that only one '
                              'side fills [CTUqmUHvd2Y @ 00:23:49]. The same team flags multi-outcome '
                              'arbitrage, buying all YES for under $1 or all NO for under $2 in a '
                              'three-outcome market, and notes the top 0.1% average more than 2,300 trades '
                              'a day against a median of 78. On the taker side, Troy Cooks prices a '
                              "60-cent contract as returning 40 cents of profit and says OddsJam's "
                              'Prediction Traders Tool, running the Sniper 2.0 model at a $250 average bet '
                              'and about 10 bets a day, is pitched at +$5,000 over 30 days via copy '
                              'trading [zMU9NWt0gdE @ 00:04:45]. For vetting traders, the Inside '
                              'Prediction Markets team uses a distribution-based CLV band, checks sizing '
                              'against optimal Kelly, and demands live results inside their own system '
                              'rather than backtests [xM4qzY2FKFw @ 00:29:10]. Tax mechanics matter too: '
                              "SharpMoney's Gary Conler notes Kalshi's terms call its contracts 1256 "
                              'contracts, which would make profits capital gains outside the 90% loss rule '
                              '[O3v0_n4fZLQ @ 00:22:29].'],
               'table': {'caption': 'Street mechanics, tools and unit economics as taught by the desk',
                         'headers': ['Mechanic',
                                     'Exact Numbers Stated',
                                     'Execution Detail',
                                     'Expert Source'],
                         'rows': [['First-touchdown scorer quoting on live football',
                                   'Pregame line minus about 4 cents for roughly 5% ROI per player',
                                   'Quote the top 10 players and refill in 900-contract lots',
                                   'Inside Prediction Markets ([tM5MKtoBoZ0 @ 00:14:55])'],
                                  ['Pre-snap repricing of the team in possession',
                                   'Team with the ball set to 1 cent before every snap',
                                   'Reprice the full ladder immediately after each play finishes',
                                   'Inside Prediction Markets ([tM5MKtoBoZ0 @ 00:15:46])'],
                                  ['RFQ combo quoting against crowded maker fields',
                                   'Competitors offering 0.1% hold from August with 40-plus NFL makers',
                                   'Compete on latency because five milliseconds behind means getting '
                                   'nothing',
                                   'Inside Prediction Markets ([ieRL4BXtMGA @ 00:22:05])'],
                                  ['Two-sided spread capture around a modeled fair',
                                   'Bid YES at 65 cents and NO at 31 cents against 67% fair',
                                   'Pay 96 cents total to lock 4 cents, risking one-sided fills',
                                   'InGenius by Veritasium ([CTUqmUHvd2Y @ 00:23:49])'],
                                  ['Multi-venue order-book software subscription cost',
                                   'About $0.02 per contract tiered, over $10K on $5M monthly volume',
                                   'Weigh vendor cost against monthly volume before buying multi-venue '
                                   'tooling',
                                   'Inside Prediction Markets ([tM5MKtoBoZ0 @ 00:25:32])'],
                                  ['Copy-trading signal tool for taker entries',
                                   '$250 average bet, about 10 bets daily, +$5,000 over 30 days',
                                   'OddsJam Prediction Traders Tool running the Sniper 2.0 model for '
                                   'signals',
                                   'OddsJam: Sports Betting Strategy & Education ([zMU9NWt0gdE @ '
                                   '00:04:45])'],
                                  ['Trader vetting before allocating team capital',
                                   'Distribution-based CLV band around a Pinnacle -105/-105 close',
                                   'Check sizing against optimal Kelly and require live in-system results',
                                   'Inside Prediction Markets ([xM4qzY2FKFw @ 00:29:10])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Where the desk actually finds and keeps its edge',
                           'body': 'Four moves the practitioners single out: go where liquidity is thin, '
                                   'trade the minutes when recreational flow is most confused, hire people '
                                   'already beating your venue, and flatten book balances before the '
                                   'calendar closes.',
                           'items': ['Run a market-making strategy in the most illiquid markets available; '
                                     "InGenius by Veritasium's interviewed expert says they would 100% do "
                                     'exactly that [InGenius by Veritasium — CTUqmUHvd2Y @ 00:26:55].',
                                     'Concentrate on end-of-game football, which Clay calls very good '
                                     "because people have no idea what they're doing [Inside Prediction "
                                     'Markets — tM5MKtoBoZ0 @ 00:34:37].',
                                     'Recruit traders who already win on your own platform, which the team '
                                     'calls a really good hiring strategy [Inside Prediction Markets — '
                                     'xM4qzY2FKFw @ 00:30:55].',
                                     'Under Bonaparte-style yearly sessions per site, hedge books toward '
                                     'zero at year-end; up $100K on FanDuel and down $20K on DraftKings '
                                     'may take 5-10 bets to flatten [SharpMoney — O3v0_n4fZLQ @ '
                                     '00:42:05].']},
               'sop_steps': [{'step': 1,
                              'title': "Map the bias with Becker's dataset",
                              'action': 'Clone the open-source repo, build the parquet files, and run the '
                                        'win-by-price analysis.',
                              'detail': "Becker's Python repo builds parquet files and runs DuckDB "
                                        'queries; the command make analyze win by price surfaces actual '
                                        'win rates against contract price [Part Time Larry — vT0qMNgOkxo @ '
                                        '00:01:09].'},
                             {'step': 2,
                              'title': 'Select nothing-ever-happens targets',
                              'action': 'Filter to emotional categories and 5-10 cent longshots, then buy '
                                        'NO as a maker and diversify.',
                              'detail': "Larry's playbook: use emotional categories, target 5-10 cent "
                                        'longshots, buy NO, place limit orders as a maker, and diversify '
                                        'over a large number of bets [Part Time Larry — vT0qMNgOkxo @ '
                                        '00:15:33].'},
                             {'step': 3,
                              'title': 'Quote live props manually',
                              'action': 'Ladder the top 10 first-touchdown players off the pregame line '
                                        'and reprice around every snap.',
                              'detail': 'Price the team without the ball at pregame minus about 4 cents '
                                        'for roughly 5% ROI per player, refill in 900-contract lots, and '
                                        'drop the team with the ball to 1 cent before each snap [Inside '
                                        'Prediction Markets — tM5MKtoBoZ0 @ 00:14:55].'},
                             {'step': 4,
                              'title': 'Vet and scale traders live',
                              'action': 'Grade every new trader on CLV bands and Kelly sizing, then '
                                        'require live proof in-system.',
                              'detail': 'Backtests are not enough; a trader must prove results live in the '
                                        "team's own system after passing a distribution-based CLV band and "
                                        'Kelly sizing check [Inside Prediction Markets — xM4qzY2FKFw @ '
                                        '00:32:21].'}]},
              {'number': 3,
               'heading': 'Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ["The loudest split on the desk is whether 'just bet NO' is still an edge or "
                              "already a crowded trade. Part Time Larry runs the 'nothing ever happens' "
                              'playbook straight off 72 million Kalshi fills: pick emotional categories, '
                              'target 5 to 10 cent longshots, buy the NO side as a resting maker limit, '
                              'and spread the book across many bets [vT0qMNgOkxo @ 00:15:33]. Three '
                              "Markets backs the bias with Fabiano.soul's stat that only 22% of markets "
                              'resolve YES, and Andrew Lonardi wants to buy the entire index of NOs, yet '
                              'the same hosts float the counterpoint that degens hammering the 10 cent '
                              'side may already offset the YES lean [DvHXWcq2iWc @ 00:04:39]. Clay, who '
                              'has pushed roughly $60M in manual volume, goes further and says competition '
                              'has flipped the edge toward YES on the sports ladders they trade '
                              '[tM5MKtoBoZ0 @ 00:29:30]. InGenius splits the difference: its '
                              'skilled-winner cohort avoids overpriced longshots and leans toward '
                              'favourites rather than blanket-shorting every headline [CTUqmUHvd2Y @ '
                              '00:20:52]. The operator read is that the NO tilt is real in emotional, '
                              'entertainment, crypto and sports categories but needs to be re-measured per '
                              'venue and per season, because the practitioners who live in liquid sports '
                              'ladders already see the premium being competed away by other makers.',
                              'Making versus taking is the second fault line, and the numbers do not line '
                              "up neatly. Part Time Larry's Kalshi data shows makers earning roughly 2.5% "
                              'excess return per trade while takers bleed about the same, a pattern '
                              'Reichenbach and Walther also found on Polymarket [vT0qMNgOkxo @ 00:05:36]. '
                              'InGenius lands on the same side: market makers in its sample averaged '
                              '$11,831 versus $3,243 for other skilled winners, and the top 0.1% are '
                              'makers about half the time [CTUqmUHvd2Y @ 00:22:13]. Clay runs 80 to 85% '
                              'maker flow and does it completely by hand, quoting ladders on intuition '
                              'rather than a model [tM5MKtoBoZ0 @ 00:12:30]. Steven complicates the story: '
                              'their book has swung from 95% taking in January to about 80% making, mostly '
                              'RFQs on combos and niche markets like NASCAR, yet taking still prints the '
                              'bigger PnL at a 7 to 8% ROI against only 2 to 3% on the making side '
                              '[ieRL4BXtMGA @ 00:06:55]. The practical split: making supplies steady, '
                              'thinner margin while live taking is where Steven still books the fat edges, '
                              'and they run both rather than picking one. Anyone copying maker returns '
                              'from aggregate studies should expect thinner per-trade margins once forty '
                              'competing quoters show up.',
                              'The remaining arguments are about desk structure and where the big money '
                              'sits. On the Novig episode, Chris argues the true end bosses stay offshore '
                              'out of tax and habit [ZmMVHubZpns @ 00:23:41], while Henry counters that it '
                              'is really stranded offshore and crypto balances keeping them there, and '
                              'adds that prediction markets let multiple millions go down quietly '
                              '[ZmMVHubZpns @ 00:27:08]. On building the team, Larry wants a named head '
                              'for each sport for accountability, topped up with generalists and part-time '
                              'specialists for Grand Slams and F1, whereas Joe prefers a quant-firm stack '
                              'of generalist traders, developers and researchers [xM4qzY2FKFw @ 00:19:36]. '
                              'Politics produces the sharpest live trade dispute: Gavin says pundits '
                              'underplay tails like a 55 to 56 seat Democratic Senate and wants to buy '
                              'tail Democrats such as Turek in Iowa rather than Talarico at 76, while a '
                              'host pushes back that with Democrats at 75% for the Senate, 55 to 56 seats '
                              'cannot be the likely outcome [4UVkZUKEmPI @ 00:16:43]. Gavin narrows the '
                              'claim to the underdog Democrats being slightly underpriced, not the '
                              'favourite. Gavin also warns that market makers should fear correlation in '
                              'political parlays, and few political RFQ trades get done at all.'],
               'table': {'caption': 'Side-by-side playbooks where prediction-market practitioners split',
                         'headers': ['Fault Line', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Directional bias on longshot and headline markets',
                                   'Buy NO on 5 to 10 cent emotional longshots as a resting maker, '
                                   'diversified across many bets',
                                   'Competition has already flipped the sports-ladder edge toward YES, so '
                                   'blanket NO is no longer free',
                                   'Part Time Larry ([vT0qMNgOkxo @ 00:15:33]); Inside Prediction Markets '
                                   '([tM5MKtoBoZ0 @ 00:29:30])'],
                                  ['Whether degen flow cancels the YES lean',
                                   'Only 22% of markets resolve YES, so buy NO early at 90/10 and ride the '
                                   'drift to 95/5',
                                   'Degens buying the 10 cent side may already offset acquiescence bias, '
                                   'so count them over time first',
                                   'Three Markets – The Prediction Market Podcast ([DvHXWcq2iWc @ '
                                   '00:02:17])'],
                                  ['Making versus taking as the core revenue engine',
                                   'Makers earn about 2.5% excess per trade and averaged $11,831 versus '
                                   '$3,243 for skilled winners',
                                   "Steven's taking still leads PnL at 7 to 8% ROI against 2 to 3% on "
                                   'making',
                                   'Inside Prediction Markets ([ieRL4BXtMGA @ 00:06:55]); InGenius by '
                                   'Veritasium ([CTUqmUHvd2Y @ 00:22:13])'],
                                  ['Manual judgment versus engineered latency on crowded books',
                                   'Clay quotes 80 to 85% maker flow completely by hand on intuition, with '
                                   'no model',
                                   'Steven says being five milliseconds behind 40-plus NFL makers means '
                                   'getting nothing, so latency and combo quoting win',
                                   'Inside Prediction Markets ([tM5MKtoBoZ0 @ 00:12:30]); Inside '
                                   'Prediction Markets ([ieRL4BXtMGA @ 00:22:05])'],
                                  ["Copying other traders' positions and quotes",
                                   'Troy Cooks pitches copy trading at $250 times about 10 bets a day for '
                                   '+$5,000 in 30 days',
                                   'Steven says copying the best RFQ quote loses to fake-outs, '
                                   'hedge-driven quotes and adverse selection',
                                   'OddsJam: Sports Betting Strategy & Education ([zMU9NWt0gdE @ '
                                   '00:04:45]); Inside Prediction Markets ([ieRL4BXtMGA @ 00:26:47])'],
                                  ['Why the biggest bettors still sit with offshore books',
                                   'Chris says end bosses stay offshore for taxes and habit, and some '
                                   'still move lines without edge',
                                   'Henry says stranded offshore and crypto funds keep them there, while '
                                   'PMs absorb millions quietly',
                                   'Inside Prediction Markets ([ZmMVHubZpns @ 00:23:41]); Inside '
                                   'Prediction Markets ([ZmMVHubZpns @ 00:27:08])'],
                                  ['How to organize a growing trading desk org chart',
                                   'Larry wants a head per sport for accountability plus generalists and '
                                   'part-time Grand Slam and F1 specialists',
                                   'Joe prefers a quant-firm stack of generalist traders, developers and '
                                   'researchers working across sports',
                                   'Inside Prediction Markets ([xM4qzY2FKFw @ 00:18:13]); Inside '
                                   'Prediction Markets ([xM4qzY2FKFw @ 00:19:36])']]}},
              {'number': 4,
               'heading': 'Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The most expensive mistakes on this desk come from contract wording, not '
                              'pricing. Steven misread the weather resolution rule on a NASCAR '
                              'pole-position market and lost about $35K, calling it the single most '
                              'expensive mistake of their career [ieRL4BXtMGA @ 00:38:21]. Clay took a '
                              'similar hit on cricket after misreading a 19.5 versus 18.5 line on a player '
                              'who went on to score about 100 [tM5MKtoBoZ0 @ 00:36:20]. Venue rules '
                              'diverge even on the same event: on the Bermuda Open, Novig voided bets '
                              'while Kalshi let them stand, which turns an identical position into a live '
                              'bet on one screen and a void on another [tM5MKtoBoZ0 @ 00:06:02]. The '
                              'Inside Prediction Markets team flags this as a structural staffing cost, '
                              'because trading Novig, Kalshi and Polymarket at once means handling '
                              'different rules on each, and every new league added, from F1 to NASCAR, '
                              'needs more people watching it [xM4qzY2FKFw @ 00:15:52]. The check before '
                              'any size goes on: read the resolution source, the void conditions and the '
                              'exact line on every venue in the hedge, and do not trade a market whose '
                              'rules you cannot explain in one sentence.',
                              "Edges on this desk decay fast, and the practitioners name the dates. Clay's "
                              'first-touchdown ladder, quoting the top ten players at the pregame line '
                              'minus about 4 cents for roughly 5% ROI each, earned about $3K per primetime '
                              'game until they got courtsided at 4,000 contracts at 95 cents; they now say '
                              'that edge is dead [tM5MKtoBoZ0 @ 00:18:24]. Clay also dropped 61K in a '
                              'single week betting against the Knicks, a reminder that a 10% lifetime ROI '
                              'on about $60M of volume still carries ugly weeks [tM5MKtoBoZ0 @ 00:20:35]. '
                              "Steven's RFQ book coasted through the World Cup in June and July, then from "
                              'August competitors started quoting a 0.1% hold, compressing edges and '
                              'forcing the shift into latency and combo quoting [ieRL4BXtMGA @ 00:08:22]. '
                              'Chris ran the defensive answer, quoting only at a 10%-plus margin early and '
                              'absorbing late flow, and still lost the McGregor versus Holloway example '
                              'running it [ZmMVHubZpns @ 00:35:23]. The economics check is to log ROI per '
                              'strategy per month, because each of these traders found out the edge had '
                              'closed only after a costly fill, and the next liquidity crunch on island '
                              'and playoff games is already expected.',
                              'The back office is where profitable traders quietly bleed. Gary Conler '
                              'stresses that the 90% rule cuts losses, not winnings, so $1M won against '
                              '$1.1M lost still leaves taxable income, and they watched a client report '
                              '$1.2M of W2Gs while IRS records showed $3.7M [O3v0_n4fZLQ @ 00:13:56]. '
                              'Andrew McMillan of REH CPA adds the recreational trap: losses only count if '
                              'you itemize, capped at winnings, and you cannot net wins against losses at '
                              'all [rN19s1QAAYo @ 00:01:24]. Custody is the second leak: after the '
                              'Polymarket international front-end hack and the Binance compromise rumor, '
                              'the Inside Prediction Markets hosts concluded never to keep money on an '
                              'exchange, while admitting hot wallets are needed to trade [4UVkZUKEmPI @ '
                              '00:09:20]. Automation is no shortcut either: InGenius built a weather '
                              'market-making bot with $103 and finished six days down $21.50, warning that '
                              'professional firms have better infrastructure and network connections '
                              '[CTUqmUHvd2Y @ 00:29:19]. The reconciliation check is to tie every return '
                              'to the IRS wage and income totals, keep session records both ways until '
                              'attorneys sign off, and hedge each book toward zero at year end.'],
               'table': {'caption': 'Firsthand losses and the economics check each practitioner drew from '
                                    'them',
                         'headers': ['Failure Mode', 'What Happened', 'Economics Check', 'Expert Source'],
                         'rows': [['Misreading a resolution rule on a niche market',
                                   'Steven misread the weather resolution rule on a NASCAR pole market and '
                                   'lost about $35K',
                                   'Read the resolution source and void conditions on every venue before '
                                   'sizing',
                                   'Inside Prediction Markets ([ieRL4BXtMGA @ 00:38:21])'],
                                  ['Getting courtsided on a manually quoted ladder',
                                   'Clay was hit at 4,000 contracts at 95 cents and declared the first-TD '
                                   'edge dead',
                                   'Refill in 900-contract lots and set the team with the ball to 1 cent '
                                   'each snap',
                                   'Inside Prediction Markets ([tM5MKtoBoZ0 @ 00:18:24])'],
                                  ['Paying the longshot and default-YES tax as a taker',
                                   "Part Time Larry's Rockets YES bought at 7% fell to 4%, turning $43 "
                                   'into $24',
                                   '5 cent contracts win only 4.18% of the time, so price longshots like '
                                   'the casino',
                                   'Part Time Larry ([vT0qMNgOkxo @ 00:04:34])'],
                                  ['Reporting gambling income short of IRS records',
                                   'A client reported $1.2M of W2Gs while their IRS records showed $3.7M',
                                   'Tie every return to W2G and 1099 totals; extending does not stop '
                                   'penalties and interest',
                                   'SharpMoney ([O3v0_n4fZLQ @ 00:13:56])'],
                                  ['Netting wins against losses as a recreational filer',
                                   '$10,000 won and $30,000 lost still means reporting $10k income and '
                                   'deducting only $10k',
                                   'Without itemizing there is no loss deduction, and some states disallow '
                                   'it entirely',
                                   'REH CPA ([rN19s1QAAYo @ 00:01:10])'],
                                  ['Leaving idle capital parked on an exchange',
                                   'A Polymarket international front-end hack required KYC for repayment, '
                                   'and a Binance compromise rumor circulated',
                                   'Never keep idle money on an exchange, but hold enough hot wallet '
                                   'balance to trade',
                                   'Inside Prediction Markets ([4UVkZUKEmPI @ 00:09:20])'],
                                  ['Deploying an untested automated bot strategy',
                                   'A $103 weather market-making bot posted +13 and +22, then four losing '
                                   'days for net minus $21.50',
                                   'A bot is only as smart as its buy and sell signals, and pros have '
                                   'better infrastructure',
                                   'InGenius by Veritasium ([CTUqmUHvd2Y @ 00:29:19])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Four Checks Before Scaling Size',
                           'body': 'Every one of these gates comes from a loss a working trader or CPA '
                                   'took or watched a client take. Clear all four before adding contracts.',
                           'items': ["Rules read on every venue: Steven's $35K NASCAR pole loss came from "
                                     'resolution wording, and Clay lost on a misread cricket line [Inside '
                                     'Prediction Markets — ieRL4BXtMGA @ 00:38:21].',
                                     'Live proof over backtests: Joe hit data leakage in an MLB backtest '
                                     'and had a big downswing, so new traders must prove results live in '
                                     "the desk's own system [Inside Prediction Markets — xM4qzY2FKFw @ "
                                     '00:33:14].',
                                     'Tax tie-out: reconcile against IRS wage and income totals before '
                                     'filing, because extending does not stop penalties and interest '
                                     '[SharpMoney — O3v0_n4fZLQ @ 00:13:25].',
                                     'Fee load check: multi-venue order-book software at about $0.02 per '
                                     'contract would cost Clay over $10K a month on roughly $5M of volume '
                                     '[Inside Prediction Markets — tM5MKtoBoZ0 @ 00:25:32].']}}],
 'pull_quote': '"Unless you have a proven strategy, you are going to be a fish who feeds a shark." — '
               'InGenius by Veritasium (CTUqmUHvd2Y @ 00:36:13).',
 'diagram_id': 'diag-03',
 'action_checklist': ["Clone Jonathan Becker's open-source repo, build the parquet files, and run `make "
                      'analyze win by price` in DuckDB to measure longshot bias in your category before '
                      'fading it [Part Time Larry — vT0qMNgOkxo @ 00:01:09].',
                      'Post NO-side limit orders as a maker on 5 to 10 cent longshots in emotional '
                      'categories, and diversify across a large number of bets [Part Time Larry — '
                      'vT0qMNgOkxo @ 00:15:33].',
                      'Quote first-TD ladders on the top 10 players at the pregame line minus about 4 '
                      'cents, refill in 900-contract lots, and set the team with the ball to 1 cent before '
                      'each snap [Inside Prediction Markets — tM5MKtoBoZ0 @ 00:14:55].',
                      'Vet new traders with a distribution-based CLV band and a Kelly sizing check, and '
                      'recruit people already winning on your platform [Inside Prediction Markets — '
                      'xM4qzY2FKFw @ 00:29:10].',
                      'Log daily sessions Shollenberger-style: column A the date, column B winning days, '
                      'column C losing days, netting wins and losses within each day [SharpMoney — '
                      'O3v0_n4fZLQ @ 00:37:14].',
                      'Hedge each book toward zero at year end under a per-site Bonaparte session, which '
                      'may take 5 to 10 bets on a book up $100K [SharpMoney — O3v0_n4fZLQ @ 00:42:05].'],
 'statutory_citations': [{'title': 'Inside Prediction Markets — Turning $100 to $1M on Prediction Markets: '
                                   'How to Build a Winning Operation [00:06:55]',
                          'url': 'https://www.youtube.com/watch?v=ieRL4BXtMGA&t=415s',
                          'relevance': 'Primary practitioner testimony on taking versus making ROI, RFQ '
                                       'edge compression, and the $35K NASCAR rules loss.'},
                         {'title': 'Inside Prediction Markets — Inside a Fully Manual Prediction Market '
                                   'Strategy: Where Human Judgment Finds an Edge [00:12:30]',
                          'url': 'https://www.youtube.com/watch?v=tM5MKtoBoZ0&t=750s',
                          'relevance': 'Primary practitioner testimony on fully manual maker flow, the '
                                       'dead first-TD edge, and the shift toward YES.'},
                         {'title': 'SharpMoney — Sports Betting Taxes in 2025 + 2026: CPA Explains Why the '
                                   '90% Rule Isn’t the End for Pros [00:08:41]',
                          'url': 'https://www.youtube.com/watch?v=O3v0_n4fZLQ&t=521s',
                          'relevance': 'Primary practitioner testimony on the 90% loss rule, W2G '
                                       'reconciliation, and session netting methods.'},
                         {'title': 'Part Time Larry — Why Kalshi Bettors Lose (72 Million Trades Analyzed) '
                                   '[00:05:36]',
                          'url': 'https://www.youtube.com/watch?v=vT0qMNgOkxo&t=336s',
                          'relevance': 'Primary practitioner testimony on maker excess returns, taker '
                                       'losses, and the longshot bias.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'vT0qMNgOkxo',
                       'title': 'Why Kalshi Bettors Lose (72 Million Trades Analyzed)',
                       'channel': 'Part Time Larry',
                       'author': 'Part Time Larry',
                       'text': 'Usually, the boring outcome wins.',
                       'tip': 'Usually, the boring outcome wins.',
                       'timestamp': 997,
                       'timestamp_seconds': 997,
                       'timestamp_label': '[00:16:37]',
                       'url': 'https://www.youtube.com/watch?v=vT0qMNgOkxo&t=997s',
                       'markdown': '[00:16:37](https://www.youtube.com/watch?v=vT0qMNgOkxo&t=997s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'vT0qMNgOkxo',
                       'title': 'Why Kalshi Bettors Lose (72 Million Trades Analyzed)',
                       'channel': 'Part Time Larry',
                       'author': 'Part Time Larry',
                       'text': "It's a diversifying over a large number of bets.",
                       'tip': "It's a diversifying over a large number of bets.",
                       'timestamp': 843,
                       'timestamp_seconds': 843,
                       'timestamp_label': '[00:14:03]',
                       'url': 'https://www.youtube.com/watch?v=vT0qMNgOkxo&t=843s',
                       'markdown': '[00:14:03](https://www.youtube.com/watch?v=vT0qMNgOkxo&t=843s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'akeWaTjtmIA',
                       'title': 'Iran War Prediction Markets — Polymarket Analysis 2026-11-06 | Political '
                                'Betting Odds & News Update',
                       'channel': 'Polymarket Plays & Analysis',
                       'author': 'Polymarket Plays & Analysis',
                       'text': "It's important to remember that prediction markets reflect collective "
                               'sentiment.',
                       'tip': "It's important to remember that prediction markets reflect collective "
                              'sentiment.',
                       'timestamp': 297,
                       'timestamp_seconds': 297,
                       'timestamp_label': '[00:04:57]',
                       'url': 'https://www.youtube.com/watch?v=akeWaTjtmIA&t=297s',
                       'markdown': '[00:04:57](https://www.youtube.com/watch?v=akeWaTjtmIA&t=297s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'zeZHFQujNTg',
                       'title': 'Iran War Prediction Markets — Polymarket Analysis 2026-11-06 | Political '
                                'Betting Odds & News Update',
                       'channel': 'Polymarket Plays & Analysis',
                       'author': 'Polymarket Plays & Analysis',
                       'text': 'Whether this represents a genuine diplomatic opening or political '
                               'posturing remains uncertain.',
                       'tip': 'Whether this represents a genuine diplomatic opening or political posturing '
                              'remains uncertain.',
                       'timestamp': 508,
                       'timestamp_seconds': 508,
                       'timestamp_label': '[00:08:28]',
                       'url': 'https://www.youtube.com/watch?v=zeZHFQujNTg&t=508s',
                       'markdown': '[00:08:28](https://www.youtube.com/watch?v=zeZHFQujNTg&t=508s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'zMU9NWt0gdE',
                       'title': 'Why Everyone Is Suddenly Betting on Prediction Markets',
                       'channel': 'OddsJam: Sports Betting Strategy & Education',
                       'author': 'OddsJam: Sports Betting Strategy & Education',
                       'text': 'The short answer is because sports books hate winners.',
                       'tip': 'The short answer is because sports books hate winners.',
                       'timestamp': 79,
                       'timestamp_seconds': 79,
                       'timestamp_label': '[00:01:19]',
                       'url': 'https://www.youtube.com/watch?v=zMU9NWt0gdE&t=79s',
                       'markdown': '[00:01:19](https://www.youtube.com/watch?v=zMU9NWt0gdE&t=79s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'DvHXWcq2iWc',
                       'title': "Prediction Market Trader's Strategy That Turned $286 To $1M",
                       'channel': 'Three Markets – The Prediction Market Podcast',
                       'author': 'Three Markets – The Prediction Market Podcast',
                       'text': 'Fading retail sentiment, especially when odds get skewed by emotion, can '
                               'give you an edge.',
                       'tip': 'Fading retail sentiment, especially when odds get skewed by emotion, can '
                              'give you an edge.',
                       'timestamp': 137,
                       'timestamp_seconds': 137,
                       'timestamp_label': '[00:02:17]',
                       'url': 'https://www.youtube.com/watch?v=DvHXWcq2iWc&t=137s',
                       'markdown': '[00:02:17](https://www.youtube.com/watch?v=DvHXWcq2iWc&t=137s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'APN3zwcwPdQ',
                       'title': 'How prediction markets are spawning an entire trading industry',
                       'channel': 'NBC News',
                       'author': 'NBC News',
                       'text': 'The regulatory gate is completely down, the vault is open, and people are '
                               'rushing in to grab what money they can at the time being before the vault '
                               'shuts back up.',
                       'tip': 'The regulatory gate is completely down, the vault is open, and people are '
                              'rushing in to grab what money they can at the time being before the vault '
                              'shuts back up.',
                       'timestamp': 95,
                       'timestamp_seconds': 95,
                       'timestamp_label': '[00:01:35]',
                       'url': 'https://www.youtube.com/watch?v=APN3zwcwPdQ&t=95s',
                       'markdown': '[00:01:35](https://www.youtube.com/watch?v=APN3zwcwPdQ&t=95s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'cwYnvWKtsYo',
                       'title': 'How Quants Trade Prediction Markets',
                       'channel': 'Three Markets – The Prediction Market Podcast',
                       'author': 'Three Markets – The Prediction Market Podcast',
                       'text': 'The model was great, far beyond anything the others produced.',
                       'tip': 'The model was great, far beyond anything the others produced.',
                       'timestamp': 168,
                       'timestamp_seconds': 168,
                       'timestamp_label': '[00:02:48]',
                       'url': 'https://www.youtube.com/watch?v=cwYnvWKtsYo&t=168s',
                       'markdown': '[00:02:48](https://www.youtube.com/watch?v=cwYnvWKtsYo&t=168s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'tM5MKtoBoZ0',
                       'title': 'Inside a Fully Manual Prediction Market Strategy: Where Human Judgment '
                                'Finds an Edge',
                       'channel': 'Inside Prediction Markets',
                       'author': 'Inside Prediction Markets',
                       'text': 'That edge is dead.',
                       'tip': 'That edge is dead.',
                       'timestamp': 1121,
                       'timestamp_seconds': 1121,
                       'timestamp_label': '[00:18:41]',
                       'url': 'https://www.youtube.com/watch?v=tM5MKtoBoZ0&t=1121s',
                       'markdown': '[00:18:41](https://www.youtube.com/watch?v=tM5MKtoBoZ0&t=1121s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'tM5MKtoBoZ0',
                       'title': 'Inside a Fully Manual Prediction Market Strategy: Where Human Judgment '
                                'Finds an Edge',
                       'channel': 'Inside Prediction Markets',
                       'author': 'Inside Prediction Markets',
                       'text': "And that's kind of where that's like why end of game is very good because "
                               "people have no idea what they're doing.",
                       'tip': "And that's kind of where that's like why end of game is very good because "
                              "people have no idea what they're doing.",
                       'timestamp': 2077,
                       'timestamp_seconds': 2077,
                       'timestamp_label': '[00:34:37]',
                       'url': 'https://www.youtube.com/watch?v=tM5MKtoBoZ0&t=2077s',
                       'markdown': '[00:34:37](https://www.youtube.com/watch?v=tM5MKtoBoZ0&t=2077s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ieRL4BXtMGA',
                       'title': 'Turning $100 to $1M on Prediction Markets: How to Build a Winning '
                                'Operation',
                       'channel': 'Inside Prediction Markets',
                       'author': 'Inside Prediction Markets',
                       'text': 'I did not read very well and lost about 35 K on that trade, and that was '
                               "probably the single most expensive mistake I've made.",
                       'tip': 'I did not read very well and lost about 35 K on that trade, and that was '
                              "probably the single most expensive mistake I've made.",
                       'timestamp': 2301,
                       'timestamp_seconds': 2301,
                       'timestamp_label': '[00:38:21]',
                       'url': 'https://www.youtube.com/watch?v=ieRL4BXtMGA&t=2301s',
                       'markdown': '[00:38:21](https://www.youtube.com/watch?v=ieRL4BXtMGA&t=2301s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ieRL4BXtMGA',
                       'title': 'Turning $100 to $1M on Prediction Markets: How to Build a Winning '
                                'Operation',
                       'channel': 'Inside Prediction Markets',
                       'author': 'Inside Prediction Markets',
                       'text': 'I think my taking PnL is like 7, 8% ROI and maybe my making PnL is like 2 '
                               'to 3% ROI.',
                       'tip': 'I think my taking PnL is like 7, 8% ROI and maybe my making PnL is like 2 '
                              'to 3% ROI.',
                       'timestamp': 415,
                       'timestamp_seconds': 415,
                       'timestamp_label': '[00:06:55]',
                       'url': 'https://www.youtube.com/watch?v=ieRL4BXtMGA&t=415s',
                       'markdown': '[00:06:55](https://www.youtube.com/watch?v=ieRL4BXtMGA&t=415s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '4UVkZUKEmPI',
                       'title': 'Perspectives From Our Trading Team: Building Tech & Trading Politics',
                       'channel': 'Inside Prediction Markets',
                       'author': 'Inside Prediction Markets',
                       'text': 'One is never keep money in an exchange because it could be hacked at any '
                               'time.',
                       'tip': 'One is never keep money in an exchange because it could be hacked at any '
                              'time.',
                       'timestamp': 560,
                       'timestamp_seconds': 560,
                       'timestamp_label': '[00:09:20]',
                       'url': 'https://www.youtube.com/watch?v=4UVkZUKEmPI&t=560s',
                       'markdown': '[00:09:20](https://www.youtube.com/watch?v=4UVkZUKEmPI&t=560s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ZmMVHubZpns',
                       'title': 'Novig Climbs to #1 in Sports: What’s Behind the Downloads?',
                       'channel': 'Inside Prediction Markets',
                       'author': 'Inside Prediction Markets',
                       'text': "It's not that difficult to get 100 million down if you're just willing to "
                               'sell it like market midpoint.',
                       'tip': "It's not that difficult to get 100 million down if you're just willing to "
                              'sell it like market midpoint.',
                       'timestamp': 1315,
                       'timestamp_seconds': 1315,
                       'timestamp_label': '[00:21:55]',
                       'url': 'https://www.youtube.com/watch?v=ZmMVHubZpns&t=1315s',
                       'markdown': '[00:21:55](https://www.youtube.com/watch?v=ZmMVHubZpns&t=1315s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'O3v0_n4fZLQ',
                       'title': 'Sports Betting Taxes in 2025 + 2026: CPA Explains Why the 90% Rule Isn’t '
                                'the End for Pros',
                       'channel': 'SharpMoney',
                       'author': 'SharpMoney',
                       'text': "So that is the first thing that people really need to understand that it's "
                               "off the losses, it's not off the winnings, which is where some people got "
                               'it wrong in the beginning.',
                       'tip': "So that is the first thing that people really need to understand that it's "
                              "off the losses, it's not off the winnings, which is where some people got "
                              'it wrong in the beginning.',
                       'timestamp': 537,
                       'timestamp_seconds': 537,
                       'timestamp_label': '[00:08:57]',
                       'url': 'https://www.youtube.com/watch?v=O3v0_n4fZLQ&t=537s',
                       'markdown': '[00:08:57](https://www.youtube.com/watch?v=O3v0_n4fZLQ&t=537s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'rN19s1QAAYo',
                       'title': "Online Sports Betting Taxes - Don't Make This Mistake...",
                       'channel': 'REH CPA',
                       'author': 'REH CPA',
                       'text': "They're considered an itemized tax deduction so you have to itemize your "
                               'tax return and you can only use losses to the extent that you had gambling '
                               'winnings.',
                       'tip': "They're considered an itemized tax deduction so you have to itemize your "
                              'tax return and you can only use losses to the extent that you had gambling '
                              'winnings.',
                       'timestamp': 70,
                       'timestamp_seconds': 70,
                       'timestamp_label': '[00:01:10]',
                       'url': 'https://www.youtube.com/watch?v=rN19s1QAAYo&t=70s',
                       'markdown': '[00:01:10](https://www.youtube.com/watch?v=rN19s1QAAYo&t=70s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'xM4qzY2FKFw',
                       'title': 'Building a Winning Prediction Market Trading Team',
                       'channel': 'Inside Prediction Markets',
                       'author': 'Inside Prediction Markets',
                       'text': 'And as you have more things that need to be covered, you need more people '
                               'to monitor them.',
                       'tip': 'And as you have more things that need to be covered, you need more people '
                              'to monitor them.',
                       'timestamp': 924,
                       'timestamp_seconds': 924,
                       'timestamp_label': '[00:15:24]',
                       'url': 'https://www.youtube.com/watch?v=xM4qzY2FKFw&t=924s',
                       'markdown': '[00:15:24](https://www.youtube.com/watch?v=xM4qzY2FKFw&t=924s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'CTUqmUHvd2Y',
                       'title': "We analysed 3 years worth of Polymarket trades. Here's what we found.",
                       'channel': 'InGenius by Veritasium',
                       'author': 'InGenius by Veritasium',
                       'text': 'Unless you have a proven strategy, you are going to be a fish who feeds a '
                               'shark.',
                       'tip': 'Unless you have a proven strategy, you are going to be a fish who feeds a '
                              'shark.',
                       'timestamp': 2173,
                       'timestamp_seconds': 2173,
                       'timestamp_label': '[00:36:13]',
                       'url': 'https://www.youtube.com/watch?v=CTUqmUHvd2Y&t=2173s',
                       'markdown': '[00:36:13](https://www.youtube.com/watch?v=CTUqmUHvd2Y&t=2173s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'}]}
