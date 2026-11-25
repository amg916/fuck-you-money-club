from __future__ import annotations

CHAPTER_4 = {'id': 'Q4',
 'chapter_id': 'Q4',
 'chapter_number': 4,
 'question_number': 4,
 'slug': 'venue-map-kalshi-forecastex-brokered-event-contracts',
 'question_prompt': 'Which regulated prediction-market venues exist, how do they differ from sportsbooks, '
                    'and how do brokers like Interactive Brokers deliver event contracts?',
 'kicker': 'Q4 / THE BIG MONEY PLAYBOOKS',
 'title': 'The Venue Map: Kalshi, ForecastEx & Brokered Event Contracts',
 'subtitle': 'Prediction markets vs sportsbooks, top 10 venues, Kalshi founders and COO on the business, '
             'Kalshi Pro, ForecastEx buy-only design and hedging economic and climate risk, trading '
             'Kalshi/CME/ForecastEx inside IBKR, geopolitics contracts, and the critique of prediction '
             'markets as gambling',
 'layout_template': 'comparison_matrix',
 'reading_time_minutes': 15,
 'executive_summary': 'Across Kalshi, ForecastEx and the IBKR brokered terminal, practitioners agree the '
                      'product is a binary contract priced between roughly 1 and 99 cents that reads '
                      'directly as probability and settles at $1 or $0, with prices set peer-to-peer '
                      'rather than by a house. The street mechanics are tight: ForecastEx pairs Yes and No '
                      'at $1.01 for a half-penny-per-side fee, Kalshi routed through IBKR costs $0.02 per '
                      'contract, early exits double the fee load, and ForecastEx pays a variable coupon '
                      'quoted at 3.14, 3.38, 4.3 and 4.33 percent. Venue routing splits macro (CPI, Fed) '
                      'toward ForecastEx or CME and sports, elections and culture toward Kalshi. '
                      "Disagreements are sharp: Kalshi's COO says there is no house, while The Young Turks "
                      "cite 79-84% losing accounts and Peterffy calls ForecastEx's US clearinghouse "
                      'probably safer.',
 'key_metrics': [{'label': 'ForecastEx Yes + No Pair Price',
                  'metric': 'ForecastEx Yes + No Pair Price',
                  'value': '$1.01 per pair (half a penny per side)',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'The extra penny is the only charge; no other exchange, clearing, data or '
                             'brokerage fees are added on ForecastEx.',
                  'source': 'Interactive Brokers ([ceR-weGZSXc @ 00:01:53])'},
                 {'label': 'Kalshi Fee Routed Through IBKR',
                  'metric': 'Kalshi Fee Routed Through IBKR',
                  'value': '$0.02 per contract ($0.01 IBKR + $0.01 exchange)',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Fee comparison inside the unified IBKR prediction-markets terminal; exiting '
                             'early doubles the fees paid.',
                  'source': 'TC Trading ([MREcV1sLqwc @ 00:11:23])'},
                 {'label': 'ForecastEx Incentive Coupon',
                  'metric': 'ForecastEx Incentive Coupon',
                  'value': '4.33% annualized',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Same rate IBKR pays on idle cash; accrues on the contract mark and adjusts '
                             'as the price moves.',
                  'source': 'Interactive Brokers ([rMm-V95moXc @ 00:03:15])'},
                 {'label': 'Kalshi Weekly Volume',
                  'metric': 'Kalshi Weekly Volume',
                  'value': 'Over $25B per week',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Reported by Kalshi's co-founder and COO alongside a $40B valuation, with "
                             'institutions only just onboarding.',
                  'source': 'Schwab Network ([ZW18j-a-TuY @ 00:06:38])'}],
 'sections': [{'heading': '1. The Practitioner Consensus',
               'paragraphs': ['The baseline every venue operator agrees on is simple: a prediction-market '
                              'contract is a Yes/No claim priced between roughly 1 and 99 cents that '
                              'settles at $1 if right and $0 if wrong, and that price reads directly as '
                              'probability. Trade Handle frames it with Yes at 60 cents and No near 40 '
                              'cents, settling at $1 or $0, with traders rather than an operator setting '
                              'the number peer-to-peer [LHwUBaFR_no @ 00:00:57]. Simple Betting Guides '
                              'makes the same point from the bettor side: sportsbook odds need converting '
                              'into implied probability, while a 0-to-$1 price already is one [zfqcFKWL2gA '
                              '@ 00:01:43]. closeuptrading drills it into position math: 10 contracts at '
                              '30 cents cost $3, a correct call pays $10 for a $7 gain, and the maximum '
                              "loss is exactly what was paid [4_swDdRFYJc @ 00:00:16]. Kalshi's CEO "
                              'describes the engine as working exactly like the NASDAQ, where a 60-cent '
                              'buyer collects $1 for a 40-cent profit and the counterparty posts that 40 '
                              'cents [rDeB10i9gCE @ 00:01:16]. The operator takeaway is that the contract '
                              'price, not odds, is the key number, and max risk on an unlevered position '
                              'is the premium paid, whether the ticket routes to Kalshi, ForecastEx or '
                              'CME.',
                              "The second point of agreement is structural: there is no house. Kalshi's "
                              'CEO argues a sportsbook sets the price, bans and limits winners, and '
                              'targets losers, while an open marketplace wants winners because winners are '
                              'the smart people; the test is the structure, not the topic, and the legal '
                              'base is the Commodity Exchange Act of 1974, where federal uniformity means '
                              "deeper liquidity and better prices [rDeB10i9gCE @ 00:03:00]. Kalshi's "
                              'co-founder and COO puts the revenue model bluntly on Schwab Network: '
                              'sportsbook revenue equals customer losses, whereas Kalshi does not make '
                              'money when users lose and simply takes a transaction fee [ZW18j-a-TuY @ '
                              '00:17:38]. The Interactive Brokers podcast desk echoes it for ForecastEx, '
                              'saying the venue is not doing a house-edge kind of thing and that the extra '
                              'penny on a $1.01 pair is the fee, half a penny per side [rMm-V95moXc @ '
                              '00:19:06]. Trade Handle adds the regulatory frame operators need before '
                              'routing anything: sportsbooks sit under gambling law, some prediction '
                              'markets sit under commodities regulation, and that line is still changing '
                              'quickly, so legality depends on where the trader lives [LHwUBaFR_no @ '
                              '00:03:14]. For a venue map, that means every ticket is a peer-to-peer '
                              "contract with a disclosed fee, not a wager against an operator's margin.",
                              'The third consensus is that venues are not interchangeable and the '
                              'prerequisites differ by route. TC Trading maps the IBKR terminal as three '
                              'venues behind one cash account: Kalshi is the consumer venue, CME is '
                              "institutional, and ForecastEx is IBKR's own exchange, with the desk focus "
                              'on macro [MREcV1sLqwc @ 00:01:23]. OngPredicts says the first decision is '
                              'residency: US traders get regulated, dollar-denominated venues with full '
                              'KYC, while global traders run crypto wallets and stablecoins, and picking '
                              'wrong means you cannot sign up, cannot trade what you want, or leave better '
                              'prices elsewhere [4SzgTKdaSHI @ 00:00:49]. On the brokered route, the '
                              'Interactive Brokers podcast says trading permissions take about a day to '
                              'switch on [rMm-V95moXc @ 00:15:48], and closeuptrading flags that '
                              'eligibility is 21+, alongside the thin-market spread risk [4_swDdRFYJc @ '
                              '00:02:16]. Stack those together and the baseline kit is a verified account '
                              'on the right side of the residency line, venue permissions approved before '
                              'the data print you want to trade, and a clear sense of whether the question '
                              'is a macro release or a sports, election or culture market, because TC '
                              'Trading routes CPI and Fed questions to ForecastEx or CME and elections, '
                              'culture and sports to Kalshi.'],
               'table': {'caption': 'Practitioner consensus on how regulated event-contract venues '
                                    'actually work',
                         'headers': ['Consensus Point',
                                     'What Practitioners Report',
                                     'Operator Implication',
                                     'Expert Source'],
                         'rows': [['Contract price reads directly as probability',
                                   'Yes at 60 cents implies about 60 percent and settles at $1 or $0',
                                   'Read the price itself instead of converting sportsbook odds into '
                                   'implied probability',
                                   'Simple Betting Guides ([zfqcFKWL2gA @ 00:00:54])'],
                                  ['Prices are set peer-to-peer, not by an operator',
                                   'Traders set prices through supply and demand, while sportsbooks bake a '
                                   'margin into their odds',
                                   'Treat the live price as a signal that can still be wrong, emotional or '
                                   'thin',
                                   'Trade Handle ([LHwUBaFR_no @ 00:01:29])'],
                                  ['Exchange revenue comes from fees, not customer losses',
                                   'Kalshi does not make money when users lose and takes a transaction fee '
                                   'instead',
                                   'Winning accounts are welcomed rather than limited or banned like at '
                                   'sportsbooks',
                                   'Schwab Network ([ZW18j-a-TuY @ 00:17:38])'],
                                  ['Maximum loss equals the premium paid on unlevered trades',
                                   'Ten contracts at 30 cents cost $3 and pay $10 if correct, a $7 gain',
                                   'Size positions knowing the full premium can go to zero at settlement',
                                   'closeuptrading ([4_swDdRFYJc @ 00:00:16])'],
                                  ['Venues split by user type and question category',
                                   'Kalshi serves consumers, CME serves institutions, and ForecastEx is '
                                   "IBKR's own macro-focused exchange",
                                   'Route CPI and Fed questions to ForecastEx or CME, elections and sports '
                                   'to Kalshi',
                                   'TC Trading ([MREcV1sLqwc @ 00:01:23])'],
                                  ['Residency decides which venues you can actually open',
                                   'US traders get regulated dollar venues with full KYC; global traders '
                                   'use crypto wallets and stablecoins',
                                   'Confirm eligibility before funding or you cannot sign up or trade '
                                   'target markets',
                                   'OngPredicts ([4SzgTKdaSHI @ 00:00:49])'],
                                  ['Regulatory status sits outside gambling law but keeps shifting',
                                   'Sportsbooks sit under gambling law; some prediction markets sit under '
                                   'commodities regulation that is changing quickly',
                                   'Check legality where you live before routing orders to any event venue',
                                   'Trade Handle ([LHwUBaFR_no @ 00:03:14])']]}},
              {'heading': '2. Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['The brokered workflow TC Trading walks through starts inside one IBKR cash '
                              'account that routes across Kalshi, CME and ForecastEx with smart order '
                              'routing to the best price; the path is Trade, then IBKR Prediction Markets '
                              '[MREcV1sLqwc @ 00:00:53]. Before sizing anything, the speaker clicks show '
                              'market rules, which links an 8-page full rules document, then places a '
                              'limit order: an initial bid at 38 cents, then a fill at 39 cents for 100 '
                              'contracts, with Day or IOC as the time-in-force choices [MREcV1sLqwc @ '
                              '00:05:39]. The fill immediately showed an average price of 41 cents because '
                              'of 2 cents in fees, so unrealized P&L opened at minus $2 on the fill itself '
                              '[MREcV1sLqwc @ 00:07:38]. closeuptrading explains why the limit order '
                              'matters: Yes at 65 cents plus No at 36 cents totals $1.01, the extra cent '
                              'is the spread, and in thin markets a market order pays a wide spread, so '
                              'limits are the default on every venue [4_swDdRFYJc @ 00:00:56]. The same '
                              'speaker reads exits differently by venue: on Kalshi you sell, on ForecastEx '
                              'you buy the opposite side, and trading the probability itself, buying at 30 '
                              'and selling at 45, captures 15 cents without waiting for settlement.',
                              "Fees are where the venues actually separate. Interactive Brokers' "
                              'ForecastEx explainer sets the pair at half a penny per side, so Yes plus No '
                              'bids total $1.01, with no other exchange, clearing, data or brokerage '
                              'charges, and pricing data is free [ceR-weGZSXc @ 00:01:53]. TC Trading '
                              'prices the brokered alternatives: ForecastEx at $0.01 built into the $1.01, '
                              'Kalshi at $0.02 split as one cent IBKR plus one cent exchange, and CME at a '
                              'cent plus pass-through fees on larger notional [MREcV1sLqwc @ 00:11:23]. '
                              'There are no settlement fees, but exiting early doubles the fee load: a '
                              '48-cent exit nets about 46 cents, roughly $5 on 100 contracts, which the '
                              'speaker says will definitely eat into profits, while warning the fee '
                              'numbers may change [MREcV1sLqwc @ 00:12:10]. On the other side of the '
                              'ledger, ForecastEx pays an incentive coupon on positions held overnight; '
                              'the Interactive Brokers podcast quotes it at 4.33% annualized, the same '
                              'rate IBKR pays on idle cash, and says it adjusts with the mark, so a CPI '
                              'contract moving from 52 cents toward 80 or 90 cents earns on the higher '
                              'value [rMm-V95moXc @ 00:03:15]. Per those numbers, holding to settlement '
                              'avoids the second fee leg; scalping the probability pays fees twice.',
                              "ForecastEx's buy-only design changes exit math, and three IBKR-side voices "
                              'run the numbers. The ForecastEx explainer shows the close-out: hold Yes at '
                              '26 cents, buy No at 31 cents, total cost 57 cents against a $1 netting, a '
                              '43-cent profit; the ugly version is No at 70 plus Yes at 86, $1.56 in for '
                              '$1 out, a 56-cent loss before coupons [ceR-weGZSXc @ 00:06:14]. ForecastEx '
                              'CEO Downey frames it as buying No at 31 being roughly equivalent to selling '
                              'Yes at 70, and any pair that nets below $1 pays out, with no novation '
                              'needed because Yes and No are separate contracts [Vix7rchq6b8 @ 00:11:37]. '
                              'Thomas Peterffy gives the simplest case: Yes at 40 plus No at 40 is 80 '
                              "cents for a $1 payout [GaBqUuuLjrQ @ 00:08:02]. For hedgers, Kalshi's CEO "
                              'supplies the template: an ice cream shop makes $100 on a sunny day and '
                              'loses $100 on a cold one, so buying 200 cold-weather contracts at 10 '
                              'percent costs $20 and locks in plus $80 whichever way the weather breaks '
                              '[rDeB10i9gCE @ 00:08:54]. The pattern is consistent across venues: size the '
                              'opposing contract count to the dollar exposure, pay the premium up front, '
                              'and the outcome range collapses to a known number.'],
               'table': {'caption': 'Venue fees, coupons and exit mechanics with the exact numbers '
                                    'practitioners quoted',
                         'headers': ['Mechanic',
                                     'Exact Number Quoted',
                                     'How Operators Use It',
                                     'Expert Source'],
                         'rows': [['ForecastEx pair pricing and exchange fee',
                                   'Yes plus No bids total $1.01, half a penny per side',
                                   'No other exchange, clearing, data or brokerage charges are stacked on '
                                   'top',
                                   'Interactive Brokers ([ceR-weGZSXc @ 00:01:53])'],
                                  ['Kalshi fee when routed through IBKR',
                                   '$0.02 per contract, split as $0.01 IBKR plus $0.01 exchange',
                                   'Budget double that cost when exiting before settlement instead of '
                                   'holding',
                                   'TC Trading ([MREcV1sLqwc @ 00:11:23])'],
                                  ['Early exit fee drag on a live position',
                                   'A 48-cent exit nets about 46 cents, roughly $5 on 100 contracts',
                                   'Hold to settlement where possible because settlement itself carries no '
                                   'fee',
                                   'TC Trading ([MREcV1sLqwc @ 00:12:10])'],
                                  ['ForecastEx incentive coupon on overnight positions',
                                   'Quoted at 3.38% per year and described as variable',
                                   'Treat the coupon as a moving yield, not a fixed rate, when sizing',
                                   'closeuptrading ([4_swDdRFYJc @ 00:01:33])'],
                                  ['Buy-only exit on ForecastEx contracts',
                                   'Yes at 26 cents plus No at 31 cents costs 57 cents, a 43-cent profit',
                                   'Close by buying the opposite side rather than selling the original '
                                   'contract',
                                   'Interactive Brokers ([ceR-weGZSXc @ 00:06:14])'],
                                  ['Data reliability threshold on Kalshi markets',
                                   'Roughly 10,000 / $40,000 in volume, depending on time to expiry',
                                   'Trust thin-market prices less; deeper volume makes the probability '
                                   'signal reliable',
                                   'Schwab Network ([ZW18j-a-TuY @ 00:11:36])'],
                                  ['Pre-trade resolution checklist before placing any order',
                                   'Confirm the exact question, the deadline and the resolver every time',
                                   'Two questions that sound the same can settle differently, so read '
                                   'rules first',
                                   'closeuptrading ([4_swDdRFYJc @ 00:01:56])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Edges the venue regulars actually use',
                           'body': 'Small execution habits that the practitioners say protect fills, fees '
                                   'and spreads across Kalshi, ForecastEx and CME.',
                           'items': ['Open show market rules and read the full 8-page rules document '
                                     'before the first order goes in. [TC Trading — MREcV1sLqwc @ '
                                     '00:04:45]',
                                     'Default to limit orders: in thin markets a market order pays the '
                                     'full wide spread on top of the $1.01 pairing. [closeuptrading — '
                                     '4_swDdRFYJc @ 00:00:56]',
                                     'Hunt cross-venue gaps: buy the cheap side on one platform and the '
                                     'opposite side where it is expensive to lock in the spread, which is '
                                     'why a second platform is worth opening. [OngPredicts — 4SzgTKdaSHI @ '
                                     '00:04:32]',
                                     'Watch fed funds futures against ForecastEx: Torres flagged futures '
                                     'pricing a more dovish 50bp versus 25bp on ForecastEx as an arbitrage '
                                     'window. [Interactive Brokers — Vix7rchq6b8 @ 00:13:20]']},
               'sop_steps': [{'step': 1,
                              'title': 'Pick the venue by residency and question type',
                              'action': 'Decide US-regulated versus global access, then match the question '
                                        'category to the venue that carries it.',
                              'detail': 'US traders run regulated dollar venues with full KYC; route CPI '
                                        'and Fed questions to ForecastEx or CME and elections, culture and '
                                        'sports to Kalshi. [OngPredicts — 4SzgTKdaSHI @ 00:00:49] [TC '
                                        'Trading — MREcV1sLqwc @ 00:13:05]'},
                             {'step': 2,
                              'title': 'Clear permissions and read the rules',
                              'action': 'Request prediction-market permissions early and confirm question, '
                                        'deadline and resolver.',
                              'detail': 'Trading permissions take about a day to approve, and the '
                                        'indicator releases hit at 8:30 AM, so request access before the '
                                        'print you want to trade. [Interactive Brokers — rMm-V95moXc @ '
                                        '00:15:48]'},
                             {'step': 3,
                              'title': 'Enter with a limit order',
                              'action': 'Bid below the ask, walk the price a cent if needed, and set Day '
                                        'or IOC time-in-force.',
                              'detail': 'The speaker bid 38 cents, then filled 100 contracts at 39 cents; '
                                        'the average showed 41 cents after 2 cents in fees, leaving '
                                        'unrealized P&L at minus $2. [TC Trading — MREcV1sLqwc @ '
                                        '00:05:39]'},
                             {'step': 4,
                              'title': 'Manage the exit with fees in mind',
                              'action': 'Sell on Kalshi, buy the opposite side on ForecastEx, and set stop '
                                        'levels up front.',
                              'detail': 'Exit by buying the opposite side and stop out at 25/20/15%, '
                                        'remembering that early exits double the fees paid on the '
                                        'position. [Interactive Brokers — rMm-V95moXc @ 00:14:48]'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The loudest split is whether this is a market or a casino with a federal '
                              'license. The Young Turks call it flatly: “it’s gambling,” just with less '
                              'regulation, sitting under the CFTC instead of state gambling law and live '
                              'in all 50 states [Y-ToFo3PvAw @ 00:00:35]. They back it with return data: '
                              'the median prediction-market return runs -8%, worse than -5% at sportsbooks '
                              'and -6.55% on slots [Y-ToFo3PvAw @ 00:06:37]. Kalshi’s CEO, speaking with '
                              'Natalie Fratto, draws the line somewhere else entirely: the test is open '
                              'marketplace versus the house, and “It’s a structure. It’s not the topic” '
                              '[rDeB10i9gCE @ 00:05:06]. Kalshi’s co-founder on Schwab Network makes the '
                              'incentive argument directly: a sportsbook’s revenue equals customer losses, '
                              'while Kalshi says “We don’t make money when users lose” and takes a '
                              'transaction fee instead [ZW18j-a-TuY @ 00:17:38]. Evan at centsorsense sits '
                              'between the camps, calling the product “kind of like a coin toss” and “akin '
                              'to gambling” unless the position is hedging a real exposure, the way flood '
                              'insurance offsets a house [qH8nQqkMNv8 @ 00:06:43]. The operator takeaway: '
                              'the same contract reads as a hedge or a wager depending on whether an '
                              'offsetting exposure exists outside the account.',
                              'Practitioners also split on which venue is structurally safer. CryptoCoins '
                              'host Daniel J. Glenn pitches Kalshi as the “first CFTC regulated” '
                              'prediction site, onshore, with protections comparable to a stock platform '
                              '[1v9Cq8L6jqg @ 00:05:52]. Thomas Peterffy, speaking to John Lothian News, '
                              'pushes back hard: Kalshi leans on a “foreign corporation” as guarantor, '
                              'while ForecastEx clears through a US clearinghouse and is, in Peterffy’s '
                              'words, “probably safer” [GaBqUuuLjrQ @ 00:02:35]. ForecastEx CEO Downey, on '
                              'the IBKR podcast, frames the design gap: Yes and No are separate contracts '
                              'that never share a price, paired at $1.01, making it “the first derivative '
                              'in the world that doesn’t go into a Clearing House requiring Novation” '
                              '[Vix7rchq6b8 @ 00:04:05]. The two designs force different exit playbooks. '
                              'closeuptrading spells it out: on Kalshi you simply sell; on ForecastEx you '
                              'exit by buying the opposite side, and trading the probability means buying '
                              'at 30¢ and getting out at 45¢ for a 15¢ gain [4_swDdRFYJc @ 00:01:16]. '
                              'Downey gives the ForecastEx translation: buying No at 31 is roughly the '
                              'same as selling Yes at 70 [Vix7rchq6b8 @ 00:11:37]. Operators running both '
                              'venues need two mental models: a two-sided book on Kalshi and a buy-only '
                              'pairing engine on ForecastEx.',
                              'Even the headline ForecastEx incentive coupon gets quoted differently '
                              'depending on who is talking and when. TC Trading reads the interest at 3.14 '
                              'APY on the IBKR ticket [MREcV1sLqwc @ 00:10:26], closeuptrading lists the '
                              'coupon at 3.38% per year and flags it as variable [4_swDdRFYJc @ 00:01:33], '
                              'Peterffy cites 4.3% paid on the daily closing price [GaBqUuuLjrQ @ '
                              '00:04:25], and the Cents of Security podcast puts it at 4.33% annualized, '
                              'matching what IBKR pays on idle cash [rMm-V95moXc @ 00:03:15]. The rate '
                              'floats, so any coupon number in a pitch is a snapshot. The coupon also '
                              'reshapes holding periods. Peterffy argues it makes long-dated questions '
                              'such as national debt above $66T by 2035 viable, and that interest on an '
                              'appreciated price can exceed the $1 win itself [GaBqUuuLjrQ @ 00:04:25]. '
                              'The podcast adds that the coupon adjusts with the mark, so a CPI contract '
                              'climbing from 52¢ to 80–90¢ earns more as it runs [rMm-V95moXc @ 00:13:29]. '
                              'TC Trading treats venue choice as a category call rather than a yield call: '
                              'CPI and Fed questions go to ForecastEx or CME, while elections, culture and '
                              'sports belong on Kalshi [MREcV1sLqwc @ 00:13:05].'],
               'table': {'caption': 'Venue Map Fault Lines: Who Argues What and How Operators Read It',
                         'headers': ['Fault Line',
                                     'Camp A Position',
                                     'Camp B Position',
                                     'Operator Read',
                                     'Expert Source'],
                         'rows': [['Gambling versus legitimate market structure debate',
                                   'Prediction markets are gambling with less regulation, live in all 50 '
                                   'states',
                                   'Open marketplace versus the house; it is a structure, not the topic',
                                   'Classify each position by whether a real outside exposure is being '
                                   'offset',
                                   'The Young Turks ([Y-ToFo3PvAw @ 00:00:35]); Natalie Fratto '
                                   '([rDeB10i9gCE @ 00:05:06])'],
                                  ['Kalshi counterparty and guarantor safety question',
                                   'Kalshi is the first CFTC regulated site, onshore, with stock-platform '
                                   'protections',
                                   'Kalshi relies on a foreign corporation guarantor; ForecastEx US '
                                   'clearinghouse is probably safer',
                                   'Know which guarantor stands behind each venue before parking real size '
                                   'there',
                                   'CryptoCoins ([1v9Cq8L6jqg @ 00:05:52]); John Lothian News (JLN) '
                                   '([GaBqUuuLjrQ @ 00:02:35])'],
                                  ['ForecastEx incentive coupon rate quoted by speakers',
                                   'TC Trading reads 3.14 APY; closeuptrading quotes 3.38% yearly and '
                                   'variable',
                                   'Peterffy cites 4.3%; Cents of Security podcast cites 4.33% annualized',
                                   'Treat the coupon as a floating rate and recheck it at every entry',
                                   'TC Trading ([MREcV1sLqwc @ 00:10:26]); Interactive Brokers '
                                   '([rMm-V95moXc @ 00:03:15])'],
                                  ['Early exit mechanics across the two venues',
                                   'On Kalshi you sell the contract back to exit before settlement',
                                   'On ForecastEx you buy the opposite side; No at 31 roughly equals '
                                   'selling at 70',
                                   'Run separate exit math for each venue before you enter the trade',
                                   'closeuptrading ([4_swDdRFYJc @ 00:01:16]); Interactive Brokers '
                                   '([Vix7rchq6b8 @ 00:11:37])'],
                                  ['Which topics deserve to be listed at all',
                                   'centsorsense backs the proposed CFTC ban on election, sports and '
                                   'awards contracts',
                                   'OngPredicts rates Kalshi strongest in sports and economic data markets',
                                   'Sports flow lives on Kalshi; ForecastEx lists only '
                                   'US-government-resolved questions',
                                   'centsorsense ([qH8nQqkMNv8 @ 00:09:06]); OngPredicts ([4SzgTKdaSHI @ '
                                   '00:02:16]); John Lothian News (JLN) ([GaBqUuuLjrQ @ 00:06:57])'],
                                  ['One unified venue versus many separate platforms',
                                   'TC Trading runs Kalshi, CME and ForecastEx from one IBKR cash account '
                                   'with smart routing',
                                   'OngPredicts says the best traders do not pick one and trade '
                                   'cross-platform gaps',
                                   'Unified routing finds the best price; a second platform unlocks '
                                   'locked-in spreads',
                                   'TC Trading ([MREcV1sLqwc @ 00:00:00]); OngPredicts ([4SzgTKdaSHI @ '
                                   '00:04:32])'],
                                  ['Forecast accuracy of live contract prices',
                                   "Kalshi's CEO says the market beat the polls on 2024 Trump and Mamdani",
                                   'Trade Handle warns prices can be wrong, emotional, or affected by low '
                                   'liquidity',
                                   'Trust deep, liquid markets and discount thin books on '
                                   'closed-information questions',
                                   'Natalie Fratto ([rDeB10i9gCE @ 00:06:40]); Trade Handle ([LHwUBaFR_no '
                                   '@ 00:02:00])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The first leak is fees, and it shows up on the ticket before the trade has '
                              'moved. TC Trading filled 100 ForecastEx contracts at 39¢, yet the position '
                              'displayed a 41¢ average price because of 2¢ in fees, opening at -$2 '
                              'unrealized [MREcV1sLqwc @ 00:07:38]. Settlement carries no fee, but exiting '
                              'early doubles the fee bill: a 48¢ exit nets about 46¢, roughly $5 shaved '
                              'off 100 contracts, and the speaker warns it “will definitely eat into your '
                              'profits” [MREcV1sLqwc @ 00:12:27]. Simple Betting Guides reminds traders '
                              'that the gap from 60¢ to $1 is profit only “before fees,” and that fees, '
                              'spreads, overpaying and following hype all drag results [zfqcFKWL2gA @ '
                              '00:02:21]. closeuptrading shows where the spread hides: Yes at 65¢ plus No '
                              'at 36¢ totals $1.01, and in thin markets a market order pays the full wide '
                              'spread, so limit orders are the default [4_swDdRFYJc @ 00:00:56]. Buy-only '
                              'exits add their own trap. The Interactive Brokers ForecastEx explainer '
                              'walks through a No bought at 70¢ that gets closed by buying Yes at 86¢: a '
                              '$1.56 total outlay against a $1 payout, a 56¢ loss before coupons '
                              '[ceR-weGZSXc @ 00:07:37].',
                              'Being right about the world is not the same as getting paid. Kalshi’s '
                              'co-founder traces the company’s origin to a failed hedge: shorting the S&P '
                              '500 against the 2016 election lost money even though the thesis was correct '
                              '[ZW18j-a-TuY @ 00:02:25]. Torres, the senior economist on the IBKR podcast, '
                              'makes the same point from the trading desk, warning that trading the right '
                              'data can still lose money and citing a gamma squeeze as the example '
                              '[Vix7rchq6b8 @ 00:16:39]. Price quality is the next trap. Trade Handle '
                              'cautions that the contract price is a live signal that can be “wrong, '
                              'emotional, or affected by low liquidity,” and that value can drop before '
                              'settlement [LHwUBaFR_no @ 00:02:00]. The Kalshi co-founder ties reliable '
                              'prices to volume and time to expiry, roughly 10,000 / $40,000 in volume '
                              '[ZW18j-a-TuY @ 00:11:36], and flags closed information systems as poorly '
                              'forecast: the Pope market sat at 1% [ZW18j-a-TuY @ 00:13:15]. Leverage '
                              'compounds every one of these errors. Daniel J. Glenn at CryptoCoins notes '
                              'Kalshi Pro offers long, short and leverage, but refuses leverage personally '
                              'because “you can actually lose more than you put in” [1v9Cq8L6jqg @ '
                              '00:02:58].',
                              'The aggregate scoreboard is brutal. The Young Turks, citing WSJ figures, '
                              'report that 79–84% of accounts lose and that 0.1% of Polymarket accounts '
                              'take 67% of the profits, with users down about $0.5B since Kalshi launched '
                              '[Y-ToFo3PvAw @ 00:04:59]. They also flag insider trading, with Santos '
                              'making $17,839 and Joshua Mitts estimating $143M on Polymarket, plus a '
                              'court map in flux: a federal appeals court let Ohio and Tennessee enforce '
                              'gambling law, Minnesota’s ban is blocked, and markets are limited in '
                              'Massachusetts, Washington, Nevada and Michigan, with the fight likely '
                              'headed to the Supreme Court [Y-ToFo3PvAw @ 00:10:02]. Trade Handle agrees '
                              'the legal status is “still changing quickly” and tells traders to check '
                              'legality where they live [LHwUBaFR_no @ 00:03:14]. Contract wording is its '
                              'own failure mode: closeuptrading warns that “two questions that sound the '
                              'same can settle differently,” so every trade starts with the exact '
                              'question, the deadline and the resolver [4_swDdRFYJc @ 00:01:56]. '
                              'Automation does not dodge accountability either. Kalshi runs AI flags, '
                              'compliance interviews, a disciplinary panel and CFTC referrals, and the '
                              'co-founder is blunt about bots: “You are responsible for all your agents '
                              'coming in” [ZW18j-a-TuY @ 00:30:35].'],
               'table': {'caption': 'Firsthand Leaks, Losses and Economics Checks on the Venue Map',
                         'headers': ['Failure Mode',
                                     'What Practitioners Reported',
                                     'Economics Check',
                                     'Expert Source'],
                         'rows': [['Entry fees hidden inside the average price',
                                   'A 39¢ fill on 100 contracts displayed a 41¢ average after 2¢ fees',
                                   'Position opens at -$2 unrealized before the market moves at all',
                                   'TC Trading ([MREcV1sLqwc @ 00:07:38])'],
                                  ['Early exit doubles the total fee bill',
                                   'A 48¢ exit nets about 46¢ after the second round of fees',
                                   'Roughly $5 lost on 100 contracts versus holding to fee-free settlement',
                                   'TC Trading ([MREcV1sLqwc @ 00:12:10])'],
                                  ['Buy-only exit at a bad opposite-side price',
                                   'No bought at 70¢ was closed by buying Yes at 86¢',
                                   'Total outlay $1.56 against a $1 payout, a 56¢ loss before coupons',
                                   'Interactive Brokers ([ceR-weGZSXc @ 00:07:37])'],
                                  ['Market orders sent into thin order books',
                                   'Yes 65¢ plus No 36¢ totals $1.01; thin markets widen the spread',
                                   'Market orders pay the full spread, so limit orders protect the edge',
                                   'closeuptrading ([4_swDdRFYJc @ 00:00:56])'],
                                  ['Right thesis expressed through the wrong instrument',
                                   'Shorting the S&P 500 to hedge the 2016 election lost money',
                                   'The election thesis was correct yet the hedge still produced a loss',
                                   'Schwab Network ([ZW18j-a-TuY @ 00:02:25])'],
                                  ['Leverage layered on top of event contracts',
                                   'Kalshi Pro offers long, short and leverage across its listed markets',
                                   'With leverage you can actually lose more than you put in',
                                   'CryptoCoins ([1v9Cq8L6jqg @ 00:02:58])'],
                                  ['Crowd-level losses and profit concentration at the top',
                                   '79–84% of accounts lose; 0.1% of Polymarket accounts take 67% of '
                                   'profits',
                                   'Median return -8% versus -5% for sportsbooks and -6.55% for slots',
                                   'The Young Turks ([Y-ToFo3PvAw @ 00:04:59]); The Young Turks '
                                   '([Y-ToFo3PvAw @ 00:06:37])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Four Checks Before Any Ticket Goes Live',
                           'body': 'Every check below traces to a leak, loss or reversal a practitioner '
                                   'reported on the ticket or in the market itself.',
                           'items': ['Open “show market rules” and read the full 8-page rules document, '
                                     'then confirm the exact question, deadline and resolver, because '
                                     'look-alike questions settle differently [TC Trading — MREcV1sLqwc @ '
                                     '00:04:45].',
                                     'Use limit orders only; Yes 65¢ plus No 36¢ already costs $1.01, and '
                                     'thin books make market orders pay the wide spread [closeuptrading — '
                                     '4_swDdRFYJc @ 00:00:56].',
                                     'Price the round trip before entry: settlement is fee-free, but an '
                                     'early exit doubles fees and turns a 48¢ exit into about 46¢ net [TC '
                                     'Trading — MREcV1sLqwc @ 00:10:54].',
                                     'Skip markets below roughly 10,000 / $40,000 in volume and '
                                     'closed-information questions, where the Pope market sat at 1% '
                                     '[Schwab Network — ZW18j-a-TuY @ 00:11:36].']}}],
 'pull_quote': '“We don’t make money when users lose. We take a transaction fee.” — Schwab Network '
               '(ZW18j-a-TuY @ 00:17:38).',
 'diagram_id': 'diag-07',
 'action_checklist': ['Identify the goal first: education, investing, speculating, or hedging, before '
                      'choosing a contract [Interactive Brokers — rMm-V95moXc @ 00:18:33].',
                      'Route by category: CPI and Fed questions to ForecastEx or CME, elections, culture '
                      'and sports to Kalshi [TC Trading — MREcV1sLqwc @ 00:13:05].',
                      'Check the exact question, the deadline and the resolver on every contract before '
                      'sizing it [closeuptrading — 4_swDdRFYJc @ 00:01:56].',
                      'Work a limit order below the ask, as TC Trading did by bidding 38¢ and filling 100 '
                      'contracts at 39¢ with Day or IOC time-in-force [TC Trading — MREcV1sLqwc @ '
                      '00:05:39].',
                      'Size hedges to lock the outcome: the ice cream shop buys 200 cold contracts at 10% '
                      'for $20 and locks in +$80 either way [Natalie Fratto — rDeB10i9gCE @ 00:08:54].',
                      'Open a second platform, start small, and buy the cheap side on one venue against '
                      'the expensive opposite side on another to lock the spread [OngPredicts — '
                      '4SzgTKdaSHI @ 00:05:15].'],
 'statutory_citations': [{'title': 'Schwab Network — Kalshi Co-Founder & COO on Future of Prediction '
                                   'Markets [00:17:38]',
                          'url': 'https://www.youtube.com/watch?v=ZW18j-a-TuY&t=1058s',
                          'relevance': "Primary practitioner testimony on Kalshi's fee-based model versus "
                                       'sportsbook revenue from customer losses.'},
                         {'title': 'John Lothian News (JLN) — Thomas Peterffy on ForecastEx: Building a '
                                   'Buy-Only Market to Transform Event Contracts Trading [00:02:35]',
                          'url': 'https://www.youtube.com/watch?v=GaBqUuuLjrQ&t=155s',
                          'relevance': "Primary practitioner testimony on Kalshi's foreign guarantor "
                                       "versus ForecastEx's US clearinghouse."},
                         {'title': 'TC Trading — How To Trade Prediction Markets On Interactive Brokers '
                                   '(Kalshi + CME + ForecastEx) [00:10:54]',
                          'url': 'https://www.youtube.com/watch?v=MREcV1sLqwc&t=654s',
                          'relevance': 'Primary practitioner testimony on per-venue fees and how early '
                                       'exits double the fee bill.'},
                         {'title': 'The Young Turks — How Prediction Markets Are TAKING OVER America '
                                   '[00:04:59]',
                          'url': 'https://www.youtube.com/watch?v=Y-ToFo3PvAw&t=299s',
                          'relevance': 'Primary practitioner testimony on account loss rates, sports share '
                                       'of Kalshi volume and profit concentration.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': '1v9Cq8L6jqg',
                       'title': 'Can You Predict the Future? Kalshi Pro & Prediction Markets Explained',
                       'channel': 'CryptoCoins',
                       'author': 'CryptoCoins',
                       'text': 'Long, short and leverage are available, but with leverage you can actually '
                               'lose more than you put in.',
                       'tip': 'Long, short and leverage are available, but with leverage you can actually '
                              'lose more than you put in.',
                       'timestamp': 178,
                       'timestamp_seconds': 178,
                       'timestamp_label': '[00:02:58]',
                       'url': 'https://www.youtube.com/watch?v=1v9Cq8L6jqg&t=178s',
                       'markdown': '[00:02:58](https://www.youtube.com/watch?v=1v9Cq8L6jqg&t=178s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'LHwUBaFR_no',
                       'title': 'Prediction Markets vs Sportsbooks: Key Differences Explained',
                       'channel': 'Trade Handle',
                       'author': 'Trade Handle',
                       'text': 'If you come from sports betting, you may be used to looking for odds, but '
                               'in prediction markets, the key number is the contract price.',
                       'tip': 'If you come from sports betting, you may be used to looking for odds, but '
                              'in prediction markets, the key number is the contract price.',
                       'timestamp': 266,
                       'timestamp_seconds': 266,
                       'timestamp_label': '[00:04:26]',
                       'url': 'https://www.youtube.com/watch?v=LHwUBaFR_no&t=266s',
                       'markdown': '[00:04:26](https://www.youtube.com/watch?v=LHwUBaFR_no&t=266s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'zfqcFKWL2gA',
                       'title': 'Prediction Markets vs Sports Betting: What is the difference?',
                       'channel': 'Simple Betting Guides',
                       'author': 'Simple Betting Guides',
                       'text': 'If you buy at 60 cents and it settles at $1, your profit is the difference '
                               'before fees.',
                       'tip': 'If you buy at 60 cents and it settles at $1, your profit is the difference '
                              'before fees.',
                       'timestamp': 141,
                       'timestamp_seconds': 141,
                       'timestamp_label': '[00:02:21]',
                       'url': 'https://www.youtube.com/watch?v=zfqcFKWL2gA&t=141s',
                       'markdown': '[00:02:21](https://www.youtube.com/watch?v=zfqcFKWL2gA&t=141s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ceR-weGZSXc',
                       'title': 'Using ForecastEx Economic Forecast Contracts to Hedge Economic and '
                                'Climate Risks',
                       'channel': 'Interactive Brokers',
                       'author': 'Interactive Brokers',
                       'text': 'The exchange collects 1 cent per pairing and pays out the remaining $1.',
                       'tip': 'The exchange collects 1 cent per pairing and pays out the remaining $1.',
                       'timestamp': 213,
                       'timestamp_seconds': 213,
                       'timestamp_label': '[00:03:33]',
                       'url': 'https://www.youtube.com/watch?v=ceR-weGZSXc&t=213s',
                       'markdown': '[00:03:33](https://www.youtube.com/watch?v=ceR-weGZSXc&t=213s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'MREcV1sLqwc',
                       'title': 'How To Trade Prediction Markets On Interactive Brokers (Kalshi + CME + '
                                'ForecastEx)',
                       'channel': 'TC Trading',
                       'author': 'TC Trading',
                       'text': 'This is a big thing to think about because it will definitely eat into '
                               'your profits.',
                       'tip': 'This is a big thing to think about because it will definitely eat into your '
                              'profits.',
                       'timestamp': 747,
                       'timestamp_seconds': 747,
                       'timestamp_label': '[00:12:27]',
                       'url': 'https://www.youtube.com/watch?v=MREcV1sLqwc&t=747s',
                       'markdown': '[00:12:27](https://www.youtube.com/watch?v=MREcV1sLqwc&t=747s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'qH8nQqkMNv8',
                       'title': 'FORECASTEX - A new prediction exchange from Interactive Brokers #trading '
                                '#binarytrading #newmarket',
                       'channel': 'centsorsense',
                       'author': 'centsorsense',
                       'text': 'You can lose a lot of money, and it is akin to gambling unless you are '
                               'hedging.',
                       'tip': 'You can lose a lot of money, and it is akin to gambling unless you are '
                              'hedging.',
                       'timestamp': 403,
                       'timestamp_seconds': 403,
                       'timestamp_label': '[00:06:43]',
                       'url': 'https://www.youtube.com/watch?v=qH8nQqkMNv8&t=403s',
                       'markdown': '[00:06:43](https://www.youtube.com/watch?v=qH8nQqkMNv8&t=403s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '4_swDdRFYJc',
                       'title': 'How to Trade Prediction Markets (Kalshi, ForecastEx, CME Inside '
                                'Interactive Brokers)',
                       'channel': 'closeuptrading',
                       'author': 'closeuptrading',
                       'text': 'Two questions that sound the same can settle differently.',
                       'tip': 'Two questions that sound the same can settle differently.',
                       'timestamp': 116,
                       'timestamp_seconds': 116,
                       'timestamp_label': '[00:01:56]',
                       'url': 'https://www.youtube.com/watch?v=4_swDdRFYJc&t=116s',
                       'markdown': '[00:01:56](https://www.youtube.com/watch?v=4_swDdRFYJc&t=116s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'GaBqUuuLjrQ',
                       'title': 'Thomas Peterffy on ForecastEx: Building a Buy-Only Market to Transform '
                                'Event Contracts Trading',
                       'channel': 'John Lothian News (JLN)',
                       'author': 'John Lothian News (JLN)',
                       'text': 'Kalshi uses a foreign corporation as guarantor, while ForecastEx has a US '
                               'clearinghouse and is probably safer.',
                       'tip': 'Kalshi uses a foreign corporation as guarantor, while ForecastEx has a US '
                              'clearinghouse and is probably safer.',
                       'timestamp': 155,
                       'timestamp_seconds': 155,
                       'timestamp_label': '[00:02:35]',
                       'url': 'https://www.youtube.com/watch?v=GaBqUuuLjrQ&t=155s',
                       'markdown': '[00:02:35](https://www.youtube.com/watch?v=GaBqUuuLjrQ&t=155s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Y-ToFo3PvAw',
                       'title': 'How Prediction Markets Are TAKING OVER America',
                       'channel': 'The Young Turks',
                       'author': 'The Young Turks',
                       'text': "About 70% of Kalshi's daily volume is sports, and 79 to 84% of accounts "
                               'lose.',
                       'tip': "About 70% of Kalshi's daily volume is sports, and 79 to 84% of accounts "
                              'lose.',
                       'timestamp': 299,
                       'timestamp_seconds': 299,
                       'timestamp_label': '[00:04:59]',
                       'url': 'https://www.youtube.com/watch?v=Y-ToFo3PvAw&t=299s',
                       'markdown': '[00:04:59](https://www.youtube.com/watch?v=Y-ToFo3PvAw&t=299s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'rDeB10i9gCE',
                       'title': 'Explaining Prediction Markets with the CEO of Kalshi',
                       'channel': 'Natalie Fratto',
                       'author': 'Natalie Fratto',
                       'text': 'So we want the winners because winners are the smart people.',
                       'tip': 'So we want the winners because winners are the smart people.',
                       'timestamp': 214,
                       'timestamp_seconds': 214,
                       'timestamp_label': '[00:03:34]',
                       'url': 'https://www.youtube.com/watch?v=rDeB10i9gCE&t=214s',
                       'markdown': '[00:03:34](https://www.youtube.com/watch?v=rDeB10i9gCE&t=214s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ZW18j-a-TuY',
                       'title': 'Kalshi Co-Founder & COO on Future of Prediction Markets',
                       'channel': 'Schwab Network',
                       'author': 'Schwab Network',
                       'text': "We don't make money when users lose. We take a transaction fee.",
                       'tip': "We don't make money when users lose. We take a transaction fee.",
                       'timestamp': 1058,
                       'timestamp_seconds': 1058,
                       'timestamp_label': '[00:17:38]',
                       'url': 'https://www.youtube.com/watch?v=ZW18j-a-TuY&t=1058s',
                       'markdown': '[00:17:38](https://www.youtube.com/watch?v=ZW18j-a-TuY&t=1058s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ZW18j-a-TuY',
                       'title': 'Kalshi Co-Founder & COO on Future of Prediction Markets',
                       'channel': 'Schwab Network',
                       'author': 'Schwab Network',
                       'text': 'You are responsible for all your agents coming in.',
                       'tip': 'You are responsible for all your agents coming in.',
                       'timestamp': 1835,
                       'timestamp_seconds': 1835,
                       'timestamp_label': '[00:30:35]',
                       'url': 'https://www.youtube.com/watch?v=ZW18j-a-TuY&t=1835s',
                       'markdown': '[00:30:35](https://www.youtube.com/watch?v=ZW18j-a-TuY&t=1835s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '4SzgTKdaSHI',
                       'title': 'Top 10 Prediction Markets 2026',
                       'channel': 'OngPredicts',
                       'author': 'OngPredicts',
                       'text': "The best traders don't pick one. Those gaps are tradeable.",
                       'tip': "The best traders don't pick one. Those gaps are tradeable.",
                       'timestamp': 272,
                       'timestamp_seconds': 272,
                       'timestamp_label': '[00:04:32]',
                       'url': 'https://www.youtube.com/watch?v=4SzgTKdaSHI&t=272s',
                       'markdown': '[00:04:32](https://www.youtube.com/watch?v=4SzgTKdaSHI&t=272s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'rMm-V95moXc',
                       'title': 'Forecast & Event Contracts Explained - Cents of Security Podcast Ep. 69',
                       'channel': 'Interactive Brokers',
                       'author': 'Interactive Brokers',
                       'text': 'Identify what the goal is first.',
                       'tip': 'Identify what the goal is first.',
                       'timestamp': 1113,
                       'timestamp_seconds': 1113,
                       'timestamp_label': '[00:18:33]',
                       'url': 'https://www.youtube.com/watch?v=rMm-V95moXc&t=1113s',
                       'markdown': '[00:18:33](https://www.youtube.com/watch?v=rMm-V95moXc&t=1113s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Vix7rchq6b8',
                       'title': 'A Behind the Scenes Look at ForecastEx Events Contracts- IBKR Podcast Ep. '
                                '181',
                       'channel': 'Interactive Brokers',
                       'author': 'Interactive Brokers',
                       'text': 'Critically the two parties are not counterparties to each other, they '
                               "don't trade the same contract, they never share the same price.",
                       'tip': "Critically the two parties are not counterparties to each other, they don't "
                              'trade the same contract, they never share the same price.',
                       'timestamp': 245,
                       'timestamp_seconds': 245,
                       'timestamp_label': '[00:04:05]',
                       'url': 'https://www.youtube.com/watch?v=Vix7rchq6b8&t=245s',
                       'markdown': '[00:04:05](https://www.youtube.com/watch?v=Vix7rchq6b8&t=245s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Vix7rchq6b8',
                       'title': 'A Behind the Scenes Look at ForecastEx Events Contracts- IBKR Podcast Ep. '
                                '181',
                       'channel': 'Interactive Brokers',
                       'author': 'Interactive Brokers',
                       'text': "I just got to get the economic data right and I think that's huge huge "
                               'huge in these kinds of markets.',
                       'tip': "I just got to get the economic data right and I think that's huge huge huge "
                              'in these kinds of markets.',
                       'timestamp': 1054,
                       'timestamp_seconds': 1054,
                       'timestamp_label': '[00:17:34]',
                       'url': 'https://www.youtube.com/watch?v=Vix7rchq6b8&t=1054s',
                       'markdown': '[00:17:34](https://www.youtube.com/watch?v=Vix7rchq6b8&t=1054s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'LiKm_5YWgPU',
                       'title': 'Geopolitics Meets Markets - Cents of Security Ep. 124',
                       'channel': 'Interactive Brokers',
                       'author': 'Interactive Brokers',
                       'text': 'I like to group the participants in those five buckets.',
                       'tip': 'I like to group the participants in those five buckets.',
                       'timestamp': 88,
                       'timestamp_seconds': 88,
                       'timestamp_label': '[00:01:28]',
                       'url': 'https://www.youtube.com/watch?v=LiKm_5YWgPU&t=88s',
                       'markdown': '[00:01:28](https://www.youtube.com/watch?v=LiKm_5YWgPU&t=88s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'LiKm_5YWgPU',
                       'title': 'Geopolitics Meets Markets - Cents of Security Ep. 124',
                       'channel': 'Interactive Brokers',
                       'author': 'Interactive Brokers',
                       'text': 'So, 72% of participants, generally speaking, believe that the shutdown '
                               'will end by November 21st.',
                       'tip': 'So, 72% of participants, generally speaking, believe that the shutdown will '
                              'end by November 21st.',
                       'timestamp': 643,
                       'timestamp_seconds': 643,
                       'timestamp_label': '[00:10:43]',
                       'url': 'https://www.youtube.com/watch?v=LiKm_5YWgPU&t=643s',
                       'markdown': '[00:10:43](https://www.youtube.com/watch?v=LiKm_5YWgPU&t=643s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'}]}
