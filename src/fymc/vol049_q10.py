from __future__ import annotations

CHAPTER_10 = {'id': 'Q10',
 'chapter_id': 'Q10',
 'chapter_number': 10,
 'question_number': 10,
 'slug': 'plus-ev-workflow-oddsjam-sharp-books-player-props',
 'question_prompt': 'How do sharp bettors use OddsJam and sharp books to find positive-EV bets, and what '
                    'do betting communities offer?',
 'kicker': 'Q10 / THE BIG MONEY PLAYBOOKS',
 'title': 'The +EV Workflow: OddsJam, Sharp Books & Player Props',
 'subtitle': 'Positive-EV fundamentals and top-down betting, sharp sportsbooks as the market, OddsJam '
             'filters, parlay builder, Momentum, Sharp Money and Traders tools, NBA and player-prop '
             'strategies, +EV vs arbitrage results, and betting Discord communities',
 'layout_template': 'expert_commentary',
 'reading_time_minutes': 15,
 'executive_summary': 'Every OddsJam-aligned operator here runs the same top-down play: treat Pinnacle, '
                      'Circa, Bookmaker, and the Novig/ProphetX exchanges as the source of truth, then bet '
                      'the soft book that has not caught up. Main lines get devigged to Pinnacle with the '
                      'worst-case method; player props lean on FanDuel and Props Builder as the sharp '
                      'reference. The numbers are concrete: a $6,748 month on props at a 13% ROI, 10.6% '
                      'returns on $84,222 of April arbitrage versus 8.5% on roughly $32,000 of +EV, and '
                      "Sharp Money entries only when exchange size clears the sharp book's limit by 3x. "
                      'Disagreements are real: worst-case versus power devig, tight odds bands versus '
                      "long-shot volume, arbitrage-first bankrolls under $3,000, and whether OddsJam's "
                      'parlay builder generates real edge or herd signals books can fingerprint.',
 'key_metrics': [{'label': 'Player-Prop Month Profit',
                  'metric': 'Player-Prop Month Profit',
                  'value': '$6,748 in 30 days at a 13% ROI',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'September player-prop results, with a large share credited to attacking '
                             "OddsJam's Sharp Money tool",
                  'source': 'OddsJam: Sports Betting Strategy & Education ([J3KQ5FaneSs @ 00:00:00])'},
                 {'label': 'April Arbitrage Return',
                  'metric': 'April Arbitrage Return',
                  'value': '10.6% on $84,222 staked over 12 days (almost $9,000 profit)',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'First half of April, mostly live arbitrage, roughly 17 arbitrage bets per '
                             'day at about $7,000 wagered daily',
                  'source': 'OddsJam: Sports Betting Strategy & Education ([uxFJJTsfAhc @ 00:01:40])'},
                 {'label': 'April +EV Return',
                  'metric': 'April +EV Return',
                  'value': 'About 8.5% on almost $32,000 over 13 days (almost $2,700 profit)',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Second half of April, pre-match one-sided +EV wagers only, 224 bets at '
                             'roughly 17 per day',
                  'source': 'OddsJam: Sports Betting Strategy & Education ([uxFJJTsfAhc @ 00:02:41])'},
                 {'label': 'Sharp Money Entry Multiplier',
                  'metric': 'Sharp Money Entry Multiplier',
                  'value': "At least 3x the sharp book's limit (Sanchez example ran 162x)",
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Posted Novig/ProphetX size versus Pinnacle, Circa, or BetOnline limit before '
                             'tailing a player prop',
                  'source': 'OddsJam: Sports Betting Strategy & Education ([J3KQ5FaneSs @ 00:01:43])'}],
 'sections': [{'title': 'The Practitioner Consensus',
               'paragraphs': ['The baseline every OddsJam-side operator works from is top-down betting: '
                              'the sharp market already knows more than you do, and the job is finding '
                              'spots where the market disagrees with itself, not predicting games '
                              "[ob0DiySE-UI @ 00:00:12]. OddsJam's beginner guide splits bettors into "
                              'three camps: recreational gut-feel players who fund the books, originators '
                              'who build proprietary single-sport models, and top-down bettors who treat '
                              'sharp books as the fair-price reference and hunt the books that have not '
                              'caught up. Top-down gets called the best entry point because it needs far '
                              'less sports knowledge [ob0DiySE-UI @ 00:04:02]. The gap exists because '
                              'there is no centralized price the way Apple stock shows one price across '
                              'every platform. Pinnacle, Circa, Bookmaker, and BetOnline make the market '
                              'and take sharp action first, recreational books copy late, and BetRivers, '
                              'Bally Bet, and Desert Diamond outsource odds to a third party called Cami '
                              'and post identical prices [ob0DiySE-UI @ 00:05:50]. Alex at OddsJam Edge '
                              'frames it identically: Pinnacle typically takes $100,000 on an NFL spread, '
                              'so its line is pure information for exploiting soft books like FanDuel, '
                              'BetMGM, and Hard Rock. Ravens at -200 on Circa and Pinnacle against -120 on '
                              'DraftKings is, in that example, almost certainly a good bet [V7_y5HtPs8c @ '
                              '00:03:03].',
                              'Which book counts as sharp depends on the market. For NFL, NBA, and MLB '
                              'main lines such as moneylines and totals, Juiced Bets names Pinnacle, '
                              'Circa, and Bookmaker as the comparison set, but player props have no single '
                              'sharpest book, so FanDuel gets at least 50% of the weight, cross-checked '
                              'against Novig, DraftKings, BetOnline, Pinnacle, and Circa where they hang '
                              'props [andSdRbPQ4E @ 00:03:15]. Prop Geek Zeke, who has bet +EV for seven '
                              'years and publishes five years of tracked Discord plays, is blunter: '
                              "DraftKings is one of the worst books for sharpness, 'ran by absolute "
                              "idiots,' Onyx and Courtside copy it, and Underdog piles on so much vig that "
                              'devigging it is pointless. FanDuel, by contrast, is a pretty good indicator '
                              'of a sharp NBA prop, with Builder alongside it [iWi1gqgw35Y @ 00:07:05]. '
                              'OddsJam Edge backs the FanDuel read from the limit side: FanDuel takes some '
                              'of the highest player-prop limits in the industry, so -170 there against '
                              '-115 at BetMGM on a Drake Baldwin single is a pricing gift [r_G17vayq6A @ '
                              '00:05:33]. The US peer-to-peer exchanges, Novig and ProphetX, complete the '
                              'list because their liquidity comes from trading firms, syndicates, and '
                              'betting hedge funds, and they run no limits and almost no juice '
                              '[V7_y5HtPs8c @ 00:07:30].',
                              'Every OddsJam-side speaker treats the edge as a long-run grind. OddsJam '
                              "Edge's line is that you do not need to be right all the time, you need good "
                              'numbers repeated over hundreds and thousands of bets, and that 95% of '
                              'sports bettors lose long-term precisely because they study stats, watch '
                              "games, and think they know ball [r_G17vayq6A @ 00:09:28]. Luke Parlay's "
                              'under-five-minute routine proves the point at small scale: sort by EV '
                              'percentage, skip books without an account, take Fred VanVleet under 1.5 '
                              'steals at 1.8 against a 1.7 average, and expect roughly a 6.99% return over '
                              'the long term, because one bet will not make anyone rich [I88FWcNIr_0 @ '
                              "00:03:01]. On OddsJam's tool breakdown, volume is called your best friend "
                              'for both Momentum and Sharp Money, the way to cut variance and grow the '
                              'bankroll [Gl7DgicTVxk @ 00:02:31]. The endgame of winning is agreed too. '
                              'Recreational books cut winners from $100 to $50 or even $5, which is their '
                              'business model rather than a bug; that cut is a badge that the process '
                              'works, and the move is pushing the same top-down method onto Novig, '
                              'ProphetX, Kalshi, and Polymarket, which take a small rake and never profile '
                              'bettors. Consistently beating closing line value is the cleanest proof '
                              '[ob0DiySE-UI @ 00:13:41].'],
               'table': {'caption': 'Where the operators line up on the top-down +EV baseline',
                         'headers': ['Consensus Principle', 'How Practitioners Apply It', 'Expert Source'],
                         'rows': [['Sharp market makers set the reference price',
                                   'Pinnacle, Circa, Bookmaker and BetOnline price first while '
                                   'recreational books copy and trail them',
                                   'OddsJam: Sports Betting Strategy & Education ([ob0DiySE-UI @ '
                                   '00:05:22])'],
                                  ['Read the sharp book but never bet into it',
                                   'Alex checks Pinnacle lines before every single bet yet has never '
                                   'placed a wager on any sharp book',
                                   'OddsJam Edge ([V7_y5HtPs8c @ 00:03:56])'],
                                  ['Soft books are where the real money goes down',
                                   'Stakes go on Hard Rock, Fanatics, PrizePicks and Underdog Fantasy '
                                   'because their lines are exploitable',
                                   'OddsJam Edge ([V7_y5HtPs8c @ 00:04:29])'],
                                  ['Price matters more than knowing the player or team',
                                   'Took a Goodwin receiving yards under at 33.5 knowing nothing because '
                                   'sharp books hung 24.5',
                                   'OddsJam Edge ([V7_y5HtPs8c @ 00:05:07])'],
                                  ['Liquid exchanges count as sharp data points',
                                   'Novig and ProphetX lines come from trading firms and syndicates, but '
                                   'thin week-out markets get ignored',
                                   'OddsJam Edge ([V7_y5HtPs8c @ 00:09:27])'],
                                  ['Volume over hundreds of bets lets the math play out',
                                   'A +1,000 Moreno homer at BetMGM carried a 10.97% edge that only pays '
                                   'across many repeated bets',
                                   'OddsJam Edge ([r_G17vayq6A @ 00:03:24])'],
                                  ['Getting limited proves the process is working',
                                   'Rec books cut $100 bettors to $50 or $5, so volume shifts to Novig, '
                                   'ProphetX, Kalshi and Polymarket',
                                   'OddsJam: Sports Betting Strategy & Education ([ob0DiySE-UI @ '
                                   '00:13:41])']]}},
              {'title': 'Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['The +EV tool setup is specific. For NBA main lines, Prop Geek Zeke bets '
                              'day-of, mostly 5 p.m. onward once injury news and lineups settle, devigs to '
                              'Pinnacle on power or worst case, and wants Pinnacle limits above $5K before '
                              'looking; FanDuel at 2.65% against a well-limited Pinnacle fair line is a '
                              'bet. Worst case is the default because it takes the least favorable of the '
                              'three devig outputs: if power says 57 cents and another method says 55, a '
                              "56-cent bet is not actually +EV, so whatever survives 'is 1,000% positive "
                              "EV' [iWi1gqgw35Y @ 00:05:31]. Juiced Bets strips the recommended filters, "
                              'caps odds at +200, and sets maximum market width at 50, ideally closer to '
                              '25, because a wide spread across books means no consensus on the true '
                              'price; the same-game, conflicting, and already-placed toggles stay on so '
                              "five units never stack on one player [andSdRbPQ4E @ 00:05:53]. OddsJam's "
                              'April test ran pre-match +EV at -175 to +125 with a 3% minimum edge, '
                              'Pinnacle as sharp book, worst-case devig, main markets plus player props, '
                              "and today only [uxFJJTsfAhc @ 00:08:24]. OddsJam's player-prop strategist "
                              'runs tighter at -150 through +140, slightly better or worse than a coin '
                              'flip [wTrqHdI32FA @ 00:03:43].',
                              'Sharp Money is the prop workhorse. The tool tracks big posted orders on '
                              'Novig and ProphetX; on a Christopher Sanchez strikeouts prop, someone '
                              'posted over $160,000 offering the over at +135, meaning they wanted the '
                              'under near -135, while Pinnacle only took $1,000, a 162x multiplier, and '
                              'the under cashed at six strikeouts [J3KQ5FaneSs @ 00:01:43]. The rules: at '
                              "least 3x the sharp book's limit, two hours or less before start, no more "
                              "than 5 cents past the sharp bettor's price, and 1-3% units. Sonny Gray at "
                              '12x got a $250 ticket at FanDuel -130, Max Fried at 2.7x was a maybe, and '
                              "Trent Grisham, with $1,100 posted against Pinnacle's $7,500 limit, was a "
                              'pass [J3KQ5FaneSs @ 00:07:20]. Alex calls crossed-market EV his main '
                              'strategy: when a soft book is arbed against a liquid sharp exchange, bet '
                              'only the soft side, as with Kareem Hunt to score a touchdown at +250 on '
                              "FanDuel against ProphetX's -242 on no touchdown with over $7,000 liquid and "
                              "Pinnacle near +200 [V7_y5HtPs8c @ 00:12:43]. OddsJam's prop strategist "
                              'layers in 0% low-hold spots and sharp line movement, such as FanDuel '
                              'dropping a Grant rebounds-and-assists under from +102 to -125 in 45 '
                              "minutes, making Hard Rock's under the bet; the rec book gets bet every time "
                              '[wTrqHdI32FA @ 00:04:42].',
                              "Sizing is where the money gets protected. OddsJam's beginner guide calls "
                              'flat betting a mistake: a 5.27% edge deserves more than a 3.29% edge, so '
                              'the Kelly multiplier sits at quarter Kelly, 0.3 for slightly more '
                              'aggression, half Kelly at most, and the baked-in recommendation, $250 to '
                              '$300-plus on top edges and $120 to $190 on thin ones, gets followed rather '
                              'than overridden [ob0DiySE-UI @ 00:12:00]. OddsJam Edge shows the same '
                              'engine recommending only $5 on a +1,050 long shot versus $50 at -150 '
                              '[r_G17vayq6A @ 00:07:53]. On the arbitrage half of the April test, '
                              "OddsJam's tester staked $84,222 over 12 days, about $7,000 a day across "
                              'roughly 17 arbs daily, mostly live in two-to-three-hour night sessions; '
                              'pre-match filters leave the minimum return blank, cap the maximum at 10%, '
                              'stick to main markets and props, and stake $200 to $500 per wager, with a '
                              'sample split of $100 and $80 locking $6.28 [uxFJJTsfAhc @ 00:07:13]. For '
                              'the time-starved, the Traders tool tails profitable Kalshi, Polymarket, '
                              'Novig, and ProphetX traders, one showing almost a 7% NHL moneyline ROI, in '
                              '10 to 15 minutes a day, on mainline markets that revive limited rec '
                              'accounts still taking $50 to $100 [Gl7DgicTVxk @ 00:07:22].'],
               'table': {'caption': 'Exact settings, thresholds and payouts the operators run',
                         'headers': ['Tool or Setting', 'Exact Numbers Taught', 'Expert Source'],
                         'rows': [['+EV tool for NBA main lines',
                                   'Devig to Pinnacle on worst case or power and skip anything under a $5K '
                                   'Pinnacle limit',
                                   'OddsJam: Sports Betting Strategy & Education ([iWi1gqgw35Y @ '
                                   '00:04:32])'],
                                  ['+EV pre-match filter stack',
                                   'Odds from -175 to +125, 3% minimum edge, main markets plus player '
                                   'props, today only',
                                   'OddsJam: Sports Betting Strategy & Education ([uxFJJTsfAhc @ '
                                   '00:08:08])'],
                                  ['Market width and odds caps',
                                   'Maximum width 50, ideally near 25, with odds capped at +200 after '
                                   'removing recommended filters',
                                   'Juiced Bets ([andSdRbPQ4E @ 00:05:34])'],
                                  ['Sharp Money entry rules',
                                   '3x the sharp limit, two hours or less pre-game, 5 cents past sharp '
                                   'price, 1-3% units',
                                   'OddsJam: Sports Betting Strategy & Education ([J3KQ5FaneSs @ '
                                   '00:07:45])'],
                                  ['Kelly multiplier in bankroll settings',
                                   'Quarter Kelly as the default, 0.3 slightly more aggressive, 0.5 half '
                                   'Kelly as the ceiling',
                                   'OddsJam: Sports Betting Strategy & Education ([ob0DiySE-UI @ '
                                   '00:12:00])'],
                                  ['Pre-match arbitrage filters',
                                   'Minimum return left blank, maximum 10%, $200 to $500 per wager on '
                                   'liquid main markets and props',
                                   'OddsJam: Sports Betting Strategy & Education ([uxFJJTsfAhc @ '
                                   '00:07:13])'],
                                  ['Parlay builder price shopping',
                                   'Two-leg slip at FanDuel +652 paid $752 on $100 versus +527 for the '
                                   'same legs at DraftKings',
                                   'Billy Collins ([AcW1ucJmvQc @ 00:07:36])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Camouflage, Signal Hygiene and Fake-Edge Filters',
                           'body': 'Small habits the operators use to keep soft-book accounts alive longer '
                                   'and to throw out EV numbers that are not backed by a real sharp price '
                                   '[Billy Collins — AcW1ucJmvQc @ 00:04:29].',
                           'items': ['When opening new Fanatics, Bet365, or BetRivers accounts, fire '
                                     'main-market parlays from the parlay tool first so the book reads you '
                                     'as a casual Degen rather than a sharp hitting unders and arbs, which '
                                     'can get you limited within three bets [Billy Collins — AcW1ucJmvQc @ '
                                     '00:04:29].',
                                     'Place bets from the mobile app; books prefer casuals on their phones '
                                     'and tend to figure out that laptop bettors might be sharper [Billy '
                                     'Collins — AcW1ucJmvQc @ 00:11:41].',
                                     'Ignore EV percentages on markets no sharp book prices, such as MLB '
                                     'player singles where there is no Pinnacle or Circa line, and stick '
                                     'to main-line props like receiving yards and strikeouts near main '
                                     'odds [Billy Collins — AcW1ucJmvQc @ 00:08:24].',
                                     'In Sharp Money, the side being offered is the side the trader does '
                                     'not want, and check whether that trader is just trying to set up '
                                     'their own arbitrage before tailing [OddsJam: Sports Betting Strategy '
                                     '& Education — Gl7DgicTVxk @ 00:06:00].']},
               'sop_steps': [{'step': 1,
                              'title': 'Load Your Books and Odds Band',
                              'action': 'Select only the sportsbooks you hold accounts with, then set '
                                        'minimum and maximum odds.',
                              'detail': 'Input the books you can access so only bettable plays show, then '
                                        'set -200 to +200 (or -150 to +150) to strip out the high-variance '
                                        'plus-1,000 and minus-1,000 plays while starting out [OddsJam Edge '
                                        '— r_G17vayq6A @ 00:04:09].'},
                             {'step': 2,
                              'title': 'Set the Devig Book by Market',
                              'action': 'Run main lines and player props as separate filters with '
                                        'different sharp books.',
                              'detail': 'For main lines select main markets only and devig to Pinnacle, '
                                        'Bookmaker, or Circa on worst case; for player props select props '
                                        'only, switch the devig book to FanDuel, and show results [Juiced '
                                        'Bets — andSdRbPQ4E @ 00:06:47].'},
                             {'step': 3,
                              'title': 'Confirm the Sharp Signal',
                              'action': 'Open line history on FanDuel, Bookmaker, or Pinnacle for every '
                                        'prop before betting.',
                              'detail': 'Bet the rec book when the sharp book has dropped significantly in '
                                        '60 minutes or less, and avoid plays where two books simply hold '
                                        'different projections with no movement [OddsJam: Sports Betting '
                                        'Strategy & Education — wTrqHdI32FA @ 00:06:25].'},
                             {'step': 4,
                              'title': 'Size, Place, Track, Audit CLV',
                              'action': 'Bet the recommended quarter-Kelly size, log it, and check closing '
                                        'line value.',
                              'detail': "Log the book, price, and stake in OddsJam's free bet tracker "
                                        '[OddsJam: Sports Betting Strategy & Education — J3KQ5FaneSs @ '
                                        '00:07:32], then compare your price to the price right before '
                                        'start on the dashboard to confirm you are consistently beating '
                                        'the close [OddsJam: Sports Betting Strategy & Education — '
                                        'ob0DiySE-UI @ 00:15:08].'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The sharpest split on the desk is which book gets crowned the source of '
                              'truth for player props. Juiced Bets sets FanDuel as the DVIG book for props '
                              'on worst case, weighting it at least 50%, then cross-checks Novig and '
                              'DraftKings before firing, and reserves Pinnacle, Circa, and Bookmaker for '
                              'main lines only [andSdRbPQ4E @ 00:03:15]. Prop Geek Zeke skips a single '
                              'anchor on NBA props, running OddsJam recommended book weights on worst '
                              'case, rating FanDuel as a pretty good indicator of a sharp NBA prop while '
                              'calling DraftKings one of the worst books in terms of sharpness and '
                              'dismissing Onyx and Courtside as copies [iWi1gqgw35Y @ 00:05:16]. The '
                              'player-prop strategist on the OddsJam channel runs Pinnacle as the sharp '
                              'book on worst case with a tight minus 150 to plus 140 window, and only '
                              'swaps to FanDuel when Pinnacle does not hang the market, such as player '
                              'rebounds and assists [wTrqHdI32FA @ 00:03:43]. The April '
                              'arbitrage-versus-EV tester also anchors to Pinnacle on worst case but '
                              'widens the window to minus 175 through plus 125 and demands a 3% edge or '
                              'higher [uxFJJTsfAhc @ 00:08:08]. Same tool, four different truth settings, '
                              'and each operator defends theirs with live examples rather than theory.',
                              'The operators also split on whether you ever put money into a sharp venue. '
                              'Alex at OddsJam Edge checks Pinnacle before every bet yet says they have '
                              'never placed a bet on any sharp book and never will, steering all action to '
                              'soft books like Hard Rock, Fanatics, PrizePicks, and Underdog [V7_y5HtPs8c '
                              '@ 00:03:56]. The sharp-money grinder flatly says they will bet into the '
                              'sharp books if the price is right, ignoring Pinnacle and Circa pricing on '
                              'props because those books carry lower limits there, and lists No Vig among '
                              'the places to grab the Sonny Gray under [J3KQ5FaneSs @ 00:04:44]. Prop Geek '
                              'Zeke lands in the middle: they pass on betting into No Vig on thin edges '
                              'like a 0.9-cent Rangers money line, but will fire there at 5% to Pinnacle '
                              'or when Kalshi and Pinnacle both say the No Vig price is wrong [iWi1gqgw35Y '
                              '@ 00:02:24]. The deeper strategic fork is arbitrage versus one-sided EV. '
                              'The April test returned 10.6% on $84,222 staked across 12 arbitrage days '
                              'against 8.5% on almost $32,000 across 13 EV days, and that tester tells '
                              'anyone at $3,000 or less to arbitrage only until the roll clears that line '
                              '[uxFJJTsfAhc @ 00:05:36].',
                              'Workflow and clock management splits the room again. The OddsJam tool '
                              'breakdown ranks Momentum as the best tool to attack player props, Sharp '
                              'Money second, the Traders tool as the fit for someone with only 10 to 15 '
                              'minutes a day, and the plus EV tool as the one with the most utility '
                              'through its custom EV formula, while warning that props on the plus EV tool '
                              'force you to dig through line history on every single play [Gl7DgicTVxk @ '
                              '00:12:05]. Timing doctrine diverges hard. Prop Geek Zeke bets NBA day of, '
                              'mostly 5:00 p.m. and later, because players get ruled out 30 minutes before '
                              'the game and lineups change constantly [iWi1gqgw35Y @ 00:00:41]. The '
                              'sharp-money grinder only attacks plays 2 hours or less before start, '
                              'reasoning that heavy liquidity posted 45 minutes before first pitch carries '
                              'more conviction than the same order seen at 8:00 a.m. for a 7:00 p.m. game '
                              '[J3KQ5FaneSs @ 00:02:45]. Sports Bet University pushes to the opposite end '
                              'entirely, calling the live positive EV page the Cadillac because it flags '
                              'stoppages, giving you the half second needed to log in and get the bet down '
                              'on a busy college football Saturday while markets fail to keep up '
                              '[6VVxJaQPyPc @ 00:07:45].'],
               'table': {'caption': 'Side-by-side playbook splits between named +EV practitioners',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Which book anchors the player prop de-vig',
                                   'FanDuel as DVIG book on worst case, weighted at least 50%, then verify '
                                   'Novig and DraftKings agree',
                                   'Pinnacle on worst case, switching to FanDuel only when Pinnacle does '
                                   'not offer the prop market',
                                   'Juiced Bets ([andSdRbPQ4E @ 00:03:15]); OddsJam: Sports Betting '
                                   'Strategy & Education ([wTrqHdI32FA @ 00:04:13])'],
                                  ['Whether to ever bet into sharp venues',
                                   'Never place a bet on Pinnacle, Circa, or any sharp book; use their '
                                   'lines purely as information',
                                   'Bet into sharp books and No Vig on props whenever the price sits '
                                   'within the allowed range',
                                   'OddsJam Edge ([V7_y5HtPs8c @ 00:03:56]); OddsJam: Sports Betting '
                                   'Strategy & Education ([J3KQ5FaneSs @ 00:04:44])'],
                                  ['Arbitrage grind versus one-sided positive EV',
                                   'Arbitrage returned 10.6% on $84,222 staked, about 17 arbs per day, '
                                   'mostly live in the evening',
                                   'Positive EV returned 8.5% on almost $32,000 staked, pre-match only, '
                                   'with some losing days mixed in',
                                   'OddsJam: Sports Betting Strategy & Education ([uxFJJTsfAhc @ '
                                   '00:03:01])'],
                                  ['How to play a crossed market',
                                   'Bet only the soft-book side when a liquid exchange like ProphetX is '
                                   'crossed against it',
                                   'Bet the rec book every time, or hunt 0% low holds against Pinnacle on '
                                   'the low holds tool',
                                   'OddsJam Edge ([V7_y5HtPs8c @ 00:12:24]); OddsJam: Sports Betting '
                                   'Strategy & Education ([wTrqHdI32FA @ 00:01:31])'],
                                  ['Odds window and confidence filters for new bettors',
                                   'Start at minus 200 to plus 200, or plus 110 to minus 150, then add '
                                   'long shots after stacking wins',
                                   'Drop recommended filters, set min max odds at plus 200, and cap market '
                                   'width at 50',
                                   'OddsJam Edge ([r_G17vayq6A @ 00:07:09]); Juiced Bets ([andSdRbPQ4E @ '
                                   '00:05:34])'],
                                  ['Which OddsJam tool fits a busy schedule',
                                   'Traders tool for 10 to 15 minutes a day, all mainline markets that '
                                   'revive limited accounts',
                                   'Momentum and Sharp Money for props, where grabbing volume is your best '
                                   'friend against variance',
                                   'OddsJam: Sports Betting Strategy & Education ([Gl7DgicTVxk @ '
                                   '00:07:09])'],
                                  ['Parlays versus straight single wagers',
                                   'Parlay builder sorted by EV as camouflage so new soft-book accounts '
                                   'read you as a degen casual',
                                   'Straight positive EV singles sized by quarter Kelly directly from the '
                                   'plus EV tool recommendations',
                                   'Billy Collins ([AcW1ucJmvQc @ 00:04:29]); OddsJam: Sports Betting '
                                   'Strategy & Education ([ob0DiySE-UI @ 00:12:30])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The most expensive trap is a fake edge. Billy Collins shows how negative-EV '
                              'legs compound rather than add, so stringing three to five bad prices, like '
                              'Kansas plus 7.5 at minus 172 on FanDuel instead of BetRivers, turns a '
                              'parlay into the sucker bet its reputation promises [AcW1ucJmvQc @ '
                              '00:01:30]. They also call out a 1.95% EV parlay leg on Cal Raleigh singles '
                              'as no real edge at all, because no sharp book like Pinnacle or Circa prices '
                              'player singles, likening it to a group project where everyone got a C-minus '
                              '[AcW1ucJmvQc @ 00:08:24]. Prop Geek Zeke flags the same rot in de-vig '
                              'sources: a prop flashing 8% can be pure illusion when the only two-sided '
                              'markets come from DraftKings, Onyx, and Courtside copying each other, or '
                              'Underdog throwing a ridiculous amount of vig on props [iWi1gqgw35Y @ '
                              '00:06:30]. Juiced Bets flags the DFS version, where a League of Legends '
                              'first-map-kills over looked great on PrizePicks only because Underdog sat '
                              'half a point higher, so they strip esports out of the fantasy optimizer '
                              'entirely and set minimum data points at two or three [andSdRbPQ4E @ '
                              '00:08:45]. The economics check is identical across all four: no sharp '
                              'reference, no edge.',
                              'Account death is the second failure mode, and everyone treats it as '
                              'inevitable. The OddsJam beginner breakdown states plainly that sports books '
                              "don't like winners: show consistent profit and a $100 bettor can get cut to "
                              '$50 or even $5, with prediction markets like Novig, ProphetX, Kalshi, and '
                              'Polymarket as the exit since they only take a small fee, and getting '
                              'limited read as a sense of pride [ob0DiySE-UI @ 00:13:25]. Billy Collins '
                              'warns that firing arbitrage, super sharp straight EV, or player-prop unders '
                              'on Fanatics is how you get limited within your first three bets, so they '
                              'open new accounts with parlays on main lines and bet from the mobile app '
                              'because books read laptop users as sharper [AcW1ucJmvQc @ 00:04:42]. They '
                              'add that a crowd of OddsJam users hitting identical generated parlays sends '
                              'one loud signal to the books [AcW1ucJmvQc @ 00:13:02]. The tool breakdown '
                              'concedes Momentum is weak for anyone limited to pennies at recreational '
                              'books, though limited accounts can come back to life on the Traders tool '
                              'because most rec books still allow 50 to 100 dollars on main lines '
                              '[Gl7DgicTVxk @ 00:08:05].',
                              'Sizing and signal-reading errors quietly bleed rolls. The OddsJam beginner '
                              'breakdown calls flat betting a half-right mistake: bettors find good plays, '
                              'then ignore the recommended stake, when a 5.27% edge deserves more than a '
                              '3.29% edge, which is why they run quarter Kelly and warn that reckless '
                              'sizing can turn a profitable strategy negative [ob0DiySE-UI @ 00:12:56]. '
                              'Sharp Money carries its own traps: a $9,500 order that fails to clear '
                              "Pinnacle's $20,000 limit at only 7 cents off is not a clean signal, and a "
                              'big poster may simply be completing an arbitrage after grabbing the other '
                              'side cheaper [Gl7DgicTVxk @ 00:06:00]. The sharp-money grinder passes on '
                              'plays with no sharp limit shown, and on a Trent Grisham home run prop where '
                              'Pinnacle took almost $7,500 against only $1,100 posted, and caps every play '
                              'at 1 to 3% of bankroll [J3KQ5FaneSs @ 00:06:15]. Paid picks bring a '
                              'different letdown. Pick Scouts found one-star reviewers who joined '
                              'CookTheBooks expecting to hit the pinned $100-to-10K ladder on day one, '
                              "then watched it miss five times in a row, even while praising the group's "
                              'research depth, its $25 per two weeks price, and its estimated value bots '
                              'that size a pick at 2% of bankroll [lmzuGHKUTnE @ 00:04:06].'],
               'table': {'caption': 'Firsthand traps reported by practitioners with the economics check '
                                    'each one teaches',
                         'headers': ['Failure Mode',
                                     'What Happened Or Was Warned',
                                     'Economics Check',
                                     'Expert Source'],
                         'rows': [['Compounding negative-EV parlay legs',
                                   'Bettors pick the play instead of the price and stack legs like minus '
                                   '172 at the wrong book',
                                   'Every individual leg must carry positive expected value before it '
                                   'joins the slip',
                                   'Billy Collins ([AcW1ucJmvQc @ 00:01:44])'],
                                  ['Fake EV where no sharp book prices the market',
                                   'A 1.95% edge on Cal Raleigh singles with no Pinnacle or Circa line '
                                   'behind it',
                                   'Favor main line props like receiving yards and strikeouts priced near '
                                   'the main odds',
                                   'Billy Collins ([AcW1ucJmvQc @ 00:08:42])'],
                                  ['De-vigging to soft copycat books',
                                   'An 8% prop built off DraftKings, Onyx, and Courtside lines that just '
                                   'copy each other',
                                   'Use FanDuel, Builder, and liquid exchanges as the sharp player prop '
                                   'reference instead',
                                   'OddsJam: Sports Betting Strategy & Education ([iWi1gqgw35Y @ '
                                   '00:07:05])'],
                                  ['Thin liquidity several days before tip',
                                   'A Tyler Herro prop three days out had no Pinnacle, ProphetX, Kalshi, '
                                   'or Polymarket data',
                                   'Less data means a less confident de-vig, so wait for game-day exchange '
                                   'liquidity',
                                   'OddsJam: Sports Betting Strategy & Education ([iWi1gqgw35Y @ '
                                   '00:10:29])'],
                                  ['Same-game and conflicting exposure',
                                   'Five units on one game and one player can cost 5% of bankroll in a '
                                   'single result',
                                   'Toggle on same-game, conflicting bet, and already-placed bet warnings '
                                   'inside OddsJam filters',
                                   'Juiced Bets ([andSdRbPQ4E @ 00:07:34])'],
                                  ['Recreational book limits after consistent wins',
                                   'A bettor used to $100 stakes gets cut to $50, or $5 at some books',
                                   'Move volume to Novig, ProphetX, Kalshi, and Polymarket, which take a '
                                   'fee and do not limit',
                                   'OddsJam: Sports Betting Strategy & Education ([ob0DiySE-UI @ '
                                   '00:13:41])'],
                                  ['Expecting the full card from a free capper Discord',
                                   'Paid cappers post only limited plays there, like a unit play or a yolo',
                                   'The full paid card stays on Patreon, so free-room members chat and '
                                   'test only',
                                   'Top Sports Debate ([2zKRyFshFvw @ 00:00:59])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Four Kill Switches Before Money Moves',
                           'body': 'Every play clears all four checks or it does not get placed, straight '
                                   'from the losses and passes these operators reported.',
                           'items': ['Kill any leg or single where no sharp book prices the market; a '
                                     '1.95% edge on Cal Raleigh singles is not a real edge [Billy Collins '
                                     '— AcW1ucJmvQc @ 00:08:24].',
                                     'Only tail a Sharp Money order that clears the sharp book limit by at '
                                     'least 3x, inside 2 hours of start, and never pay more than 5 cents '
                                     "above the sharp bettor's price [OddsJam: Sports Betting Strategy & "
                                     'Education — J3KQ5FaneSs @ 00:07:45].',
                                     'Before treating a big exchange order as conviction, check whether '
                                     'the poster is just finishing an arbitrage after grabbing the other '
                                     'side cheaper [OddsJam: Sports Betting Strategy & Education — '
                                     'Gl7DgicTVxk @ 00:06:00].',
                                     'Hold off on one-sided positive EV until the bankroll clears $3,000, '
                                     'because a small roll has no cushion to absorb losing days [OddsJam: '
                                     'Sports Betting Strategy & Education — uxFJJTsfAhc @ 00:05:53].']}}],
 'pull_quote': '"Price dictates everything when it comes to profitable sports betting." — OddsJam: Sports '
               'Betting Strategy & Education (ob0DiySE-UI @ 00:10:26).',
 'diagram_id': 'diag-02',
 'action_checklist': ['For main lines, de-vig to Pinnacle on worst case or power and skip NBA sides where '
                      'Pinnacle shows less than a 5K limit (OddsJam: Sports Betting Strategy & Education, '
                      'iWi1gqgw35Y @ 00:04:47).',
                      'Cap market width at 50, ideally closer to 25, so you only bet markets where books '
                      'share a consensus price (Juiced Bets, andSdRbPQ4E @ 00:06:28).',
                      'On every prop, open line history for FanDuel, Bookmaker, or Pinnacle and bet the '
                      'rec book when the sharp line dropped significantly in 60 minutes or less (OddsJam: '
                      'Sports Betting Strategy & Education, wTrqHdI32FA @ 00:06:25).',
                      'Run Sharp Money with a 3x minimum over the sharp book limit, a 5-cent price '
                      'ceiling, and a 2-hour-or-less window before start (OddsJam: Sports Betting Strategy '
                      '& Education, J3KQ5FaneSs @ 00:07:45).',
                      'Set the OddsJam bankroll Kelly multiplier to quarter Kelly, going no higher than '
                      'half Kelly, and stake the recommended amount on every play (OddsJam: Sports Betting '
                      'Strategy & Education, ob0DiySE-UI @ 00:12:00).',
                      'Scan for arbitrage between a soft book like FanDuel and a liquid sharp exchange '
                      'like ProphetX, then bet only the soft-book side (OddsJam Edge, V7_y5HtPs8c @ '
                      '00:12:43).'],
 'statutory_citations': [{'title': 'OddsJam: Sports Betting Strategy & Education — I made $6,748 betting '
                                   'on player props in 30 days using one strategy [00:01:43]',
                          'url': 'https://www.youtube.com/watch?v=J3KQ5FaneSs&t=103s',
                          'relevance': 'Primary practitioner testimony on the Sharp Money 3x limit '
                                       'multiplier, 5-cent price ceiling, and 2-hour timing rules.'},
                         {'title': 'OddsJam: Sports Betting Strategy & Education — I Put Arbitrage and +EV '
                                   'Betting to the Test — The Results SHOCKED Me [00:03:01]',
                          'url': 'https://www.youtube.com/watch?v=uxFJJTsfAhc&t=181s',
                          'relevance': 'Primary practitioner testimony on a month-long arbitrage versus '
                                       'positive EV return comparison and the $3,000 bankroll threshold.'},
                         {'title': 'OddsJam Edge — How I Use Sharp Sportsbooks to Find +EV Bets [00:12:24]',
                          'url': 'https://www.youtube.com/watch?v=V7_y5HtPs8c&t=744s',
                          'relevance': 'Primary practitioner testimony on crossed-market EV betting '
                                       'against liquid exchanges like ProphetX.'},
                         {'title': "Billy Collins — I Tested OddsJam's NEW Parlay Tool (Here's What "
                                   'Happened) [00:00:56]',
                          'url': 'https://www.youtube.com/watch?v=AcW1ucJmvQc&t=56s',
                          'relevance': 'Primary practitioner testimony on compounding parlay edges, fake '
                                       'EV legs, and account camouflage tactics.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'AcW1ucJmvQc',
                       'title': "I Tested OddsJam's NEW Parlay Tool (Here's What Happened)",
                       'channel': 'Billy Collins',
                       'author': 'Billy Collins',
                       'text': 'Each leg of that parlay carries its own edge, positive or negative, and '
                               "when you add multiple legs to your parlay, that edge doesn't just add up, "
                               'it compounds.',
                       'tip': 'Each leg of that parlay carries its own edge, positive or negative, and '
                              "when you add multiple legs to your parlay, that edge doesn't just add up, "
                              'it compounds.',
                       'timestamp': 56,
                       'timestamp_seconds': 56,
                       'timestamp_label': '[00:00:56]',
                       'url': 'https://www.youtube.com/watch?v=AcW1ucJmvQc&t=56s',
                       'markdown': '[00:00:56](https://www.youtube.com/watch?v=AcW1ucJmvQc&t=56s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'AcW1ucJmvQc',
                       'title': "I Tested OddsJam's NEW Parlay Tool (Here's What Happened)",
                       'channel': 'Billy Collins',
                       'author': 'Billy Collins',
                       'text': "Most sports books, when they're trying to figure out if you're a sharp "
                               'bettor or a degen, they prefer that you use the mobile app.',
                       'tip': "Most sports books, when they're trying to figure out if you're a sharp "
                              'bettor or a degen, they prefer that you use the mobile app.',
                       'timestamp': 701,
                       'timestamp_seconds': 701,
                       'timestamp_label': '[00:11:41]',
                       'url': 'https://www.youtube.com/watch?v=AcW1ucJmvQc&t=701s',
                       'markdown': '[00:11:41](https://www.youtube.com/watch?v=AcW1ucJmvQc&t=701s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'iWi1gqgw35Y',
                       'title': 'NBA Betting Course, Part 2: How to Find Positive EV Bets',
                       'channel': 'OddsJam: Sports Betting Strategy & Education',
                       'author': 'OddsJam: Sports Betting Strategy & Education',
                       'text': "Worst case, I'm always going to use worst case.",
                       'tip': "Worst case, I'm always going to use worst case.",
                       'timestamp': 316,
                       'timestamp_seconds': 316,
                       'timestamp_label': '[00:05:16]',
                       'url': 'https://www.youtube.com/watch?v=iWi1gqgw35Y&t=316s',
                       'markdown': '[00:05:16](https://www.youtube.com/watch?v=iWi1gqgw35Y&t=316s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'iWi1gqgw35Y',
                       'title': 'NBA Betting Course, Part 2: How to Find Positive EV Bets',
                       'channel': 'OddsJam: Sports Betting Strategy & Education',
                       'author': 'OddsJam: Sports Betting Strategy & Education',
                       'text': 'In general, when betting player props, you want to bet in the soft books '
                               'with sharp books as your D Vig.',
                       'tip': 'In general, when betting player props, you want to bet in the soft books '
                              'with sharp books as your D Vig.',
                       'timestamp': 592,
                       'timestamp_seconds': 592,
                       'timestamp_label': '[00:09:52]',
                       'url': 'https://www.youtube.com/watch?v=iWi1gqgw35Y&t=592s',
                       'markdown': '[00:09:52](https://www.youtube.com/watch?v=iWi1gqgw35Y&t=592s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '6VVxJaQPyPc',
                       'title': 'Advanced OddsJam Tutorial 🔥 How Sharps Find Positive EV Bets & Beat the '
                                'Sportsbooks',
                       'channel': 'Sports Bet University | Sports Betting Education',
                       'author': 'Sports Bet University | Sports Betting Education',
                       'text': "So, the live betting tool, positive EV, odds jam, it's the Cadillac.",
                       'tip': "So, the live betting tool, positive EV, odds jam, it's the Cadillac.",
                       'timestamp': 465,
                       'timestamp_seconds': 465,
                       'timestamp_label': '[00:07:45]',
                       'url': 'https://www.youtube.com/watch?v=6VVxJaQPyPc&t=465s',
                       'markdown': '[00:07:45](https://www.youtube.com/watch?v=6VVxJaQPyPc&t=465s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'andSdRbPQ4E',
                       'title': 'How to Use OddsJam in 2025: +EV Filters, Strategy, Tools, Tutorial',
                       'channel': 'Juiced Bets',
                       'author': 'Juiced Bets',
                       'text': "That means that that market is not very sharp because there's no consensus "
                               'on what the correct price should be.',
                       'tip': "That means that that market is not very sharp because there's no consensus "
                              'on what the correct price should be.',
                       'timestamp': 372,
                       'timestamp_seconds': 372,
                       'timestamp_label': '[00:06:12]',
                       'url': 'https://www.youtube.com/watch?v=andSdRbPQ4E&t=372s',
                       'markdown': '[00:06:12](https://www.youtube.com/watch?v=andSdRbPQ4E&t=372s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'r_G17vayq6A',
                       'title': 'How to Find +EV Bets Before the Sportsbooks Fix Them',
                       'channel': 'OddsJam Edge',
                       'author': 'OddsJam Edge',
                       'text': "You don't need to be a sports expert to win. You just need to consistently "
                               'get good value against the market.',
                       'tip': "You don't need to be a sports expert to win. You just need to consistently "
                              'get good value against the market.',
                       'timestamp': 539,
                       'timestamp_seconds': 539,
                       'timestamp_label': '[00:08:59]',
                       'url': 'https://www.youtube.com/watch?v=r_G17vayq6A&t=539s',
                       'markdown': '[00:08:59](https://www.youtube.com/watch?v=r_G17vayq6A&t=539s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'V7_y5HtPs8c',
                       'title': 'How I Use Sharp Sportsbooks to Find +EV Bets',
                       'channel': 'OddsJam Edge',
                       'author': 'OddsJam Edge',
                       'text': 'Crossed market EV betting is the main strategy I use nowadays.',
                       'tip': 'Crossed market EV betting is the main strategy I use nowadays.',
                       'timestamp': 744,
                       'timestamp_seconds': 744,
                       'timestamp_label': '[00:12:24]',
                       'url': 'https://www.youtube.com/watch?v=V7_y5HtPs8c&t=744s',
                       'markdown': '[00:12:24](https://www.youtube.com/watch?v=V7_y5HtPs8c&t=744s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'V7_y5HtPs8c',
                       'title': 'How I Use Sharp Sportsbooks to Find +EV Bets',
                       'channel': 'OddsJam Edge',
                       'author': 'OddsJam Edge',
                       'text': 'Peer-to-peer does not mean your counterparty is an idiot.',
                       'tip': 'Peer-to-peer does not mean your counterparty is an idiot.',
                       'timestamp': 465,
                       'timestamp_seconds': 465,
                       'timestamp_label': '[00:07:45]',
                       'url': 'https://www.youtube.com/watch?v=V7_y5HtPs8c&t=465s',
                       'markdown': '[00:07:45](https://www.youtube.com/watch?v=V7_y5HtPs8c&t=465s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Gl7DgicTVxk',
                       'title': 'Which OddsJam Tool Fits You? Momentum vs Sharp Money vs Traders vs +EV',
                       'channel': 'OddsJam: Sports Betting Strategy & Education',
                       'author': 'OddsJam: Sports Betting Strategy & Education',
                       'text': "Something else that doesn't get talked about enough with sharp money is "
                               'you have to understand, is this individual trader trying to set up an '
                               'arbitrage play.',
                       'tip': "Something else that doesn't get talked about enough with sharp money is you "
                              'have to understand, is this individual trader trying to set up an arbitrage '
                              'play.',
                       'timestamp': 343,
                       'timestamp_seconds': 343,
                       'timestamp_label': '[00:05:43]',
                       'url': 'https://www.youtube.com/watch?v=Gl7DgicTVxk&t=343s',
                       'markdown': '[00:05:43](https://www.youtube.com/watch?v=Gl7DgicTVxk&t=343s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Gl7DgicTVxk',
                       'title': 'Which OddsJam Tool Fits You? Momentum vs Sharp Money vs Traders vs +EV',
                       'channel': 'OddsJam: Sports Betting Strategy & Education',
                       'author': 'OddsJam: Sports Betting Strategy & Education',
                       'text': 'On the plus EV tool, you have to dig through each play, which takes time, '
                               'which reduces your speed, which could easily eat into your profits.',
                       'tip': 'On the plus EV tool, you have to dig through each play, which takes time, '
                              'which reduces your speed, which could easily eat into your profits.',
                       'timestamp': 738,
                       'timestamp_seconds': 738,
                       'timestamp_label': '[00:12:18]',
                       'url': 'https://www.youtube.com/watch?v=Gl7DgicTVxk&t=738s',
                       'markdown': '[00:12:18](https://www.youtube.com/watch?v=Gl7DgicTVxk&t=738s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'I88FWcNIr_0',
                       'title': 'How I Use OddsJam to Find Winning Bets in 4 Minutes',
                       'channel': 'Luke Parlay',
                       'author': 'Luke Parlay',
                       'text': "The key here is consistency because one bet won't make you rich, but over "
                               "hundreds of these, that's where the edge compounds.",
                       'tip': "The key here is consistency because one bet won't make you rich, but over "
                              "hundreds of these, that's where the edge compounds.",
                       'timestamp': 202,
                       'timestamp_seconds': 202,
                       'timestamp_label': '[00:03:22]',
                       'url': 'https://www.youtube.com/watch?v=I88FWcNIr_0&t=202s',
                       'markdown': '[00:03:22](https://www.youtube.com/watch?v=I88FWcNIr_0&t=202s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'J3KQ5FaneSs',
                       'title': 'I made $6,748 betting on player props in 30 days using one strategy',
                       'channel': 'OddsJam: Sports Betting Strategy & Education',
                       'author': 'OddsJam: Sports Betting Strategy & Education',
                       'text': "Rule number one of the sharp money tool, we want to know what's the sharp "
                               "book's limit, and then we want at least a 3x multiplier or higher.",
                       'tip': "Rule number one of the sharp money tool, we want to know what's the sharp "
                              "book's limit, and then we want at least a 3x multiplier or higher.",
                       'timestamp': 103,
                       'timestamp_seconds': 103,
                       'timestamp_label': '[00:01:43]',
                       'url': 'https://www.youtube.com/watch?v=J3KQ5FaneSs&t=103s',
                       'markdown': '[00:01:43](https://www.youtube.com/watch?v=J3KQ5FaneSs&t=103s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'wTrqHdI32FA',
                       'title': 'The SECRET to Winning Player Prop Bets (2 Strategies That Work)',
                       'channel': 'OddsJam: Sports Betting Strategy & Education',
                       'author': 'OddsJam: Sports Betting Strategy & Education',
                       'text': "When a sharp sports book's odds are moving in one specific direction, it's "
                               'because of information and money, and we want to bet the recreational '
                               'books every single time.',
                       'tip': "When a sharp sports book's odds are moving in one specific direction, it's "
                              'because of information and money, and we want to bet the recreational books '
                              'every single time.',
                       'timestamp': 176,
                       'timestamp_seconds': 176,
                       'timestamp_label': '[00:02:56]',
                       'url': 'https://www.youtube.com/watch?v=wTrqHdI32FA&t=176s',
                       'markdown': '[00:02:56](https://www.youtube.com/watch?v=wTrqHdI32FA&t=176s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'uxFJJTsfAhc',
                       'title': 'I Put Arbitrage and +EV Betting to the Test — The Results SHOCKED Me',
                       'channel': 'OddsJam: Sports Betting Strategy & Education',
                       'author': 'OddsJam: Sports Betting Strategy & Education',
                       'text': 'I would highly advise that you only arbitrage bet if your bankroll is '
                               '$3,000 or less.',
                       'tip': 'I would highly advise that you only arbitrage bet if your bankroll is '
                              '$3,000 or less.',
                       'timestamp': 336,
                       'timestamp_seconds': 336,
                       'timestamp_label': '[00:05:36]',
                       'url': 'https://www.youtube.com/watch?v=uxFJJTsfAhc&t=336s',
                       'markdown': '[00:05:36](https://www.youtube.com/watch?v=uxFJJTsfAhc&t=336s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ob0DiySE-UI',
                       'title': 'The Complete Guide to +EV Sports Betting (For Beginners)',
                       'channel': 'OddsJam: Sports Betting Strategy & Education',
                       'author': 'OddsJam: Sports Betting Strategy & Education',
                       'text': 'Showing consistent profits on recreational sports books will eventually '
                               'get your limits cut.',
                       'tip': 'Showing consistent profits on recreational sports books will eventually get '
                              'your limits cut.',
                       'timestamp': 805,
                       'timestamp_seconds': 805,
                       'timestamp_label': '[00:13:25]',
                       'url': 'https://www.youtube.com/watch?v=ob0DiySE-UI&t=805s',
                       'markdown': '[00:13:25](https://www.youtube.com/watch?v=ob0DiySE-UI&t=805s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'lmzuGHKUTnE',
                       'title': 'I Joined CookTheBooks Sports Betting Discord. Here are my thoughts',
                       'channel': 'Pick Scouts',
                       'author': 'Pick Scouts',
                       'text': "It is highlighted there, it's pinned, but you're not going to hit that "
                               'every day.',
                       'tip': "It is highlighted there, it's pinned, but you're not going to hit that "
                              'every day.',
                       'timestamp': 246,
                       'timestamp_seconds': 246,
                       'timestamp_label': '[00:04:06]',
                       'url': 'https://www.youtube.com/watch?v=lmzuGHKUTnE&t=246s',
                       'markdown': '[00:04:06](https://www.youtube.com/watch?v=lmzuGHKUTnE&t=246s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '2zKRyFshFvw',
                       'title': 'I CREATED A FREE DISCORD SERVER FOR THE SPORTS BETTING COMMUNITY | '
                                'FANDUEL | DRAFTKINGS',
                       'channel': 'Top Sports Debate',
                       'author': 'Top Sports Debate',
                       'text': 'My cappers that get paid will only be doing limited plays over there.',
                       'tip': 'My cappers that get paid will only be doing limited plays over there.',
                       'timestamp': 36,
                       'timestamp_seconds': 36,
                       'timestamp_label': '[00:00:36]',
                       'url': 'https://www.youtube.com/watch?v=2zKRyFshFvw&t=36s',
                       'markdown': '[00:00:36](https://www.youtube.com/watch?v=2zKRyFshFvw&t=36s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'}]}
