from __future__ import annotations

def build_volume_049_workbook() -> dict:
    return {'workbook_id': 'wb-049-prediction-market-terminals-and-igaming-affiliates',
 'volume_id': 'vol-049-prediction-market-terminals-and-igaming-affiliates',
 'title': 'Regulated Prediction-Market Terminals & Licensed iGaming Affiliates — Practitioner Testimony '
          'Operator Workbook',
 'subtitle': 'Terminal wiring, cross-venue arbitrage, pro-desk microstructure, venue routing, '
             'event-contract rules, and secure odds data pipes for operators who trade regulated '
             'prediction markets and build licensed iGaming data stacks',
 'worksheets': [{'worksheet_id': 'ws-01',
                 'number': 1,
                 'title': 'Terminal Wiring and Cross-Venue Arbitrage Control Sheet',
                 'purpose': 'Document how your prediction-market terminal connects to Kalshi and '
                            'Polymarket, how it caches, authenticates, and emulates order types, how any '
                            'LLM or bot is kept on a dry-run leash, and how every cross-venue pair is '
                            'verified for equivalence, depth, latency, and exit before capital moves.',
                 'chapter_ref': 'Q1-Q2',
                 'instructions': ['Complete every field using your live configuration, real stake sizes, '
                                  'and the exact venues you trade today, not the setup you plan to build '
                                  'later.',
                                  'Attach a log excerpt, screenshot, or code reference to each answer so a '
                                  'second operator could reproduce the check without asking you.',
                                  'Treat any scanner gap, model recommendation, or quoted spread as '
                                  'unverified until the equivalence, depth, and rules fields below are '
                                  'filled in.',
                                  'Record dollar figures, seconds, and cents as numbers, and note the date '
                                  'each figure was last measured so stale assumptions are easy to spot.',
                                  'Revisit this sheet whenever you add a venue, change a data feed, switch '
                                  'models, or raise your per-trade cap above its current level.'],
                 'fields': [{'name': 'venue_split_rationale',
                             'type': 'textarea',
                             'prompt': "Write down which venue holds your regulated, KYC'd, fiat-funded "
                                       'account and which venue supplies crypto-native volume, then '
                                       'explain how a normalization layer will reconcile the IDs, field '
                                       'names, and order-book shapes that the two venues do not share.',
                             'example': 'Kalshi holds the regulated US account with its free documented '
                                        'API, while Polymarket supplies volume Part Time Larry pegs at ten '
                                        "times Kalshi's. A mapping table joins both catalogs, and "
                                        'Predictify groups equivalent markets across venues so a single '
                                        'listing opens a wider view of the same question [OngPredicts — '
                                        'HtGMBJ7ynjs @ 00:04:37].'},
                            {'name': 'catalog_cache_policy',
                             'type': 'textarea',
                             'prompt': 'Describe how you page through the full event catalog, how many '
                                       'events each request returns, how long a cold load takes against a '
                                       'cached reload, and the invalidation rule that keeps stale odds '
                                       'from feeding your terminal decisions.',
                             'example': 'The assistant pages roughly 30,000 Kalshi events with nested '
                                        'markets at 200 per request. Cold load took 193 seconds; the '
                                        'Streamlit cache decorator cut reloads to 1.5 seconds. Because '
                                        'odds keep moving, the cache now expires on a fixed timer, and a '
                                        'forced refresh runs before any order is sent [Part Time Larry — '
                                        'Ib0BEFKAvn0 @ 00:16:21].'},
                            {'name': 'key_storage_and_auth',
                             'type': 'text',
                             'prompt': 'Document where your RSA private keys and API secrets live, how the '
                                       'code loads them without ever writing them inline, and how bearer '
                                       'tokens are attached to websocket sessions so credentials stay out '
                                       'of version control and screenshots.',
                             'example': 'Keys sit in a .env file outside the repository, loaded at '
                                        'startup, never pasted into scripts; as Robot Traders put it, the '
                                        'keys are separated in an exterior file [Robot Traders — '
                                        'yYjo1lzNoGI @ 00:11:35]. The websocket client attaches a bearer '
                                        'token on connect, and the .env file is listed in the ignore file '
                                        'before the first commit.'},
                            {'name': 'order_type_emulation',
                             'type': 'text',
                             'prompt': 'Explain how your terminal fills urgently on a venue that lacks '
                                       'true market orders, naming the order type, the aggressive price '
                                       'you set, and the maximum slippage you will tolerate before the '
                                       'order is cancelled rather than resting.',
                             'example': "On Kalshi market orders don't exist per se [Robot Traders — "
                                        'yYjo1lzNoGI @ 00:13:25], so the bot sends fill-or-kill with an '
                                        'aggressive yes price set above the best offer. If depth at that '
                                        'ceiling cannot absorb the full size, the order dies instead of '
                                        'resting, and the log records the attempted price and the reason '
                                        'for the kill.'},
                            {'name': 'llm_rule_reading_check',
                             'type': 'textarea',
                             'prompt': 'For every contract an assistant or bot recommends, record who read '
                                       'the resolution rules, which clause defines the outcome count or '
                                       'threshold, and how malformed structured output from the model is '
                                       'cleaned and validated before any order call.',
                             'example': 'A three-cut bet lost when the sequence counted as four, so the '
                                        'rules text is now fed to the model alongside each contract [Part '
                                        'Time Larry — Ib0BEFKAvn0 @ 00:13:45]. Perplexity Sonar output '
                                        'works about 90% of the time, sometimes dropping the contracts key '
                                        'or wrapping JSON in backticks, so a parser strips backticks and '
                                        'rejects missing keys.'},
                            {'name': 'dry_run_log_review',
                             'type': 'textarea',
                             'prompt': 'Set out the dry-run period for any LLM-driven or automated bot, '
                                       'the per-trade dollar cap you will hold, and the three log entries '
                                       'you will read on each decision before you allow the bot to send '
                                       'live orders.',
                             'example': 'The bot runs in dry-run mode with the $10 cap locked [OngPredicts '
                                        '— kDOrvOpgzjE @ 00:03:22]. Each cycle logs the market snapshot, '
                                        "the model's probability estimate, and the trade-or-skip reason. "
                                        'Three Markets watched AI portfolios bleed, so live trading stays '
                                        'off until a week of logs shows skip reasons that match the '
                                        'written rules.'},
                            {'name': 'equivalence_verdict_log',
                             'type': 'textarea',
                             'prompt': 'For each cross-venue pair your scanner surfaces, record the '
                                       'equivalence verdict, the resolution sources on both venues, the '
                                       'quoted gap in cents, and whether the venue with the most money '
                                       'traded confirms that price after you re-check it.',
                             'example': 'A 3-cent gap between markets judged not equivalent is logged as '
                                        'no trade [OngPredicts — OEhjqCpa1Uw @ 00:04:11]. Taf warns that '
                                        'same-titled markets can resolve totally differently. A 22-cent '
                                        'Dodgers gap on the scanner collapsed to about a third of a cent '
                                        'on the compare tab [OngPredicts — T6thRudYjsg @ 00:02:51], so '
                                        'every row is re-priced first.'},
                            {'name': 'depth_at_size',
                             'type': 'textarea',
                             'prompt': 'Walk the order book on both legs at your intended stake, then '
                                       'record the average fill price, total fees, net profit, and the '
                                       'stake level above which thinning depth starts shrinking the net '
                                       'return on the pair.',
                             'example': "Chen Trading's $100 Mark Kelly pair bought about 107.75 shares at "
                                        'a 92.8-cent average and netted an estimated $7.75 after roughly '
                                        "94 cents in fees [Chen Trading — lYFPEQllQOw @ 00:02:35]. Taf's "
                                        'AI-benchmark pair paid about $31 near $205 to $220 and shrank '
                                        'above that because the book was not deep enough [Taf — '
                                        'GLvhRHB7n2U @ 00:09:16].'},
                            {'name': 'feed_latency_audit',
                             'type': 'textarea',
                             'prompt': 'List every data feed driving live decisions, its measured delay '
                                       'against the venue, its monthly cost, and a written rule stating '
                                       'which feeds are barred from triggering latency trades because '
                                       'faster participants already move prices before your signal '
                                       'arrives.',
                             'example': 'ESPN Gamecast runs 5 to 15 seconds ahead of TV, yet the ESPN-fed '
                                        'Kalshi bot still lost money because Kalshi moved first [Part Time '
                                        'Larry — bA_NUrMJuw4 @ 00:05:01]. Pro feeds run near $5,000 a '
                                        'month, and Whale Slots puts consumer streams 7 to 30 seconds '
                                        'behind, so free feeds only inform pregame models.'},
                            {'name': 'crossover_exit_plan',
                             'type': 'text',
                             'prompt': 'Define when you exit a cross-venue position before resolution, how '
                                       'you detect the lines crossing over, how you size the hedge if only '
                                       'one leg fills, and how long you will tolerate capital being '
                                       'locked, measured in weeks.',
                             'example': 'The Taylor Swift top Spotify artist market crossed roughly every '
                                        '2 weeks, so both legs are cashed out at each crossover instead of '
                                        'waiting months [Juiced Bets — PaQjSUCZVb0 @ 00:08:30]. If '
                                        "Polymarket fills and the Kalshi side moves, the tool's calculated "
                                        'hedge size goes on Kalshi immediately so no single outcome '
                                        'carries exposure.'}],
                 'completion_gate': 'This worksheet is complete only when keys are confirmed outside the '
                                    'code, the catalog cache has a written invalidation rule, the bot has '
                                    'a logged dry run under the $10 cap, and every funded cross-venue pair '
                                    'shows an equivalence verdict, a compare-tab re-price, and a depth '
                                    'walk at actual size.'},
                {'worksheet_id': 'ws-02',
                 'number': 2,
                 'title': 'Pro Desk Microstructure and Venue Routing Ledger',
                 'purpose': 'Measure where your book sits relative to the structural edge that pro desks '
                            'harvest, decide your maker-versus-taker mix and niche, and route each '
                            'contract category to the venue whose rules, fees, clearing structure, coupon, '
                            'and liquidity actually fit the position you intend to hold.',
                 'chapter_ref': 'Q3-Q4',
                 'instructions': ['Pull your actual fill history before answering so the longshot, maker, '
                                  'and fee fields reflect real trades rather than memory or intention.',
                                  'Read the full rules document for every venue you route to and record '
                                  'the date, question wording, deadline, and resolver in the rules field.',
                                  'Price each position as a full round trip, writing out both the '
                                  'hold-to-settlement path and the early-exit path with doubled fees.',
                                  'Apply the volume floor and closed-information screen before price, so '
                                  'thin or unknowable markets are removed regardless of how cheap they '
                                  'look.',
                                  'Have a second desk member review the live-proof and fee-load fields '
                                  'before any new strategy or trader receives additional capital.'],
                 'fields': [{'name': 'longshot_exposure_audit',
                             'type': 'textarea',
                             'prompt': 'Tally how much of your book sits in cheap YES longshots, compare '
                                       'each price bucket against its realized win rate, and state whether '
                                       'you are the emotional buyer or the patient seller harvesting those '
                                       'contracts across many diversified positions.',
                             'example': "Across Becker's 72 million Kalshi trades, 5-cent contracts won "
                                        '4.18% of the time while NO bought at 94 cents won 95% [Part Time '
                                        'Larry — vT0qMNgOkxo @ 00:04:34]. Only 22% of markets resolve YES, '
                                        'so the book now favors the boring outcome, spread across a large '
                                        'number of small positions rather than a few loud bets.'},
                            {'name': 'maker_taker_mix',
                             'type': 'textarea',
                             'prompt': 'Record the share of your fills that rest as maker orders versus '
                                       'cross the spread as taker orders, the excess return you measure on '
                                       'each side, and the evidence that justifies keeping any taking '
                                       'activity in your plan.',
                             'example': 'Makers earn about +2.5% per trade and takers about -2.5% on '
                                        'Kalshi, with the same pattern on Polymarket [Part Time Larry — '
                                        'vT0qMNgOkxo @ 00:05:36]. InGenius by Veritasium puts market '
                                        'makers at $11,831 average profit versus $3,243 for skilled '
                                        'winners, yet Steven still earns 7-8% taking against 2-3% making, '
                                        'so taking stays only where measured.'},
                            {'name': 'niche_selection',
                             'type': 'text',
                             'prompt': 'Name the illiquid markets or game situations where you plan to '
                                       'quote, explain why other participants misprice them, and estimate '
                                       'the per-event profit and lifetime ROI that would justify the '
                                       'manual hours those markets demand from you.',
                             'example': 'Clay concentrates on end-of-game football because people have no '
                                        "idea what they're doing [Inside Prediction Markets — tM5MKtoBoZ0 "
                                        '@ 00:34:37], quoting first-touchdown markets for about $3K per '
                                        'primetime game on a fully manual, 80-85% maker style. Lifetime '
                                        'volume sits near $60M at roughly 10% ROI, which sets the '
                                        'benchmark for any new niche.'},
                            {'name': 'rules_reading_log',
                             'type': 'textarea',
                             'prompt': 'For every venue and contract you trade, log the date you read the '
                                       'full rules document, the exact question wording, the deadline, the '
                                       'resolver, and any look-alike contract elsewhere that settles on '
                                       'different terms despite a similar title.',
                             'example': "Steven's $35K NASCAR pole loss came from resolution wording, and "
                                        'Clay lost on a misread cricket line [Inside Prediction Markets — '
                                        'ieRL4BXtMGA @ 00:38:21]. Inside IBKR, show market rules opens the '
                                        'full 8-page document [TC Trading — MREcV1sLqwc @ 00:04:45], and '
                                        'closeuptrading warns two questions that sound the same can settle '
                                        'differently.'},
                            {'name': 'live_proof_record',
                             'type': 'textarea',
                             'prompt': 'Describe how a new strategy or new trader proves results live '
                                       'inside your own system before receiving capital, including the '
                                       'minimum live sample, the leakage checks applied to any backtest, '
                                       'and who signs off on promotion.',
                             'example': 'Joe hit data leakage in an MLB backtest and then took a big '
                                        'downswing, so the desk requires new traders to prove results live '
                                        'in its own system [Inside Prediction Markets — xM4qzY2FKFw @ '
                                        '00:33:14]. Recruiting starts with traders already winning on the '
                                        'platform, which the team calls a really good hiring strategy.'},
                            {'name': 'fee_load_model',
                             'type': 'textarea',
                             'prompt': 'Project your monthly contract volume, multiply it by every '
                                       'per-contract charge from exchanges, brokers, and multi-venue '
                                       'software, and state the volume level at which tooling fees would '
                                       'consume a meaningful share of the edge you expect.',
                             'example': 'Multi-venue order-book software at about $0.02 per contract would '
                                        'cost Clay over $10K a month on roughly $5M of volume [Inside '
                                        'Prediction Markets — tM5MKtoBoZ0 @ 00:25:32]. Kalshi routed '
                                        'through IBKR adds $0.02 per contract, split between IBKR and the '
                                        'exchange [TC Trading — MREcV1sLqwc @ 00:11:23], so both layers '
                                        'enter the monthly model.'},
                            {'name': 'round_trip_pricing',
                             'type': 'text',
                             'prompt': 'Before entry, price the full round trip for each position, '
                                       'comparing a hold-to-settlement path against an early exit, and '
                                       'record the net exit price after doubled fees so the trade still '
                                       'clears your minimum required margin.',
                             'example': 'Settlement is fee-free, but an early exit doubles fees and turns '
                                        'a 48-cent exit into about 46 cents net [TC Trading — MREcV1sLqwc '
                                        '@ 00:10:54]. TC Trading stresses this will definitely eat into '
                                        'profits, so each ticket lists both paths, and positions that only '
                                        'work on an early exit are sized down or skipped.'},
                            {'name': 'limit_order_discipline',
                             'type': 'text',
                             'prompt': 'State your default order type on thin event-contract books, the '
                                       'maximum spread you will cross, and how the paired price of a Yes '
                                       'and a No contract informs where you place each limit order and '
                                       'when you cancel it.',
                             'example': 'On ForecastEx, Yes at 65 cents plus No at 36 cents already costs '
                                        '$1.01, the half-penny-per-side pairing fee [closeuptrading — '
                                        '4_swDdRFYJc @ 00:00:56]. Thin books make a market order pay the '
                                        'full wide spread on top, so every entry rests as a limit order '
                                        'and is cancelled if unfilled after the set window.'},
                            {'name': 'venue_routing_map',
                             'type': 'textarea',
                             'prompt': 'Map each contract category you trade to its venue, covering macro '
                                       'releases, Fed decisions, sports, elections, and culture, and note '
                                       'the clearing structure, fee schedule, and any incentive coupon '
                                       'that tilts routing toward one venue over another.',
                             'example': 'CPI and Fed contracts route to ForecastEx or CME, while sports, '
                                        'elections, and culture go to Kalshi. ForecastEx pays a 4.33% '
                                        'annualized coupon on the contract mark [Interactive Brokers — '
                                        'rMm-V95moXc @ 00:03:15], and Peterffy calls its US clearinghouse '
                                        "probably safer than Kalshi's foreign guarantor [John Lothian News "
                                        '(JLN) — GaBqUuuLjrQ @ 00:02:35].'},
                            {'name': 'liquidity_floor_check',
                             'type': 'text',
                             'prompt': 'Set the minimum traded volume a market must show before you enter, '
                                       'list the question types where outcome information is closed to '
                                       'outsiders, and explain how either condition removes a market from '
                                       'your watchlist regardless of price.',
                             'example': 'Markets below roughly 10,000 / $40,000 in volume are skipped, and '
                                        'so are closed-information questions such as the Pope market that '
                                        "sat at 1% [Schwab Network — ZW18j-a-TuY @ 00:11:36]. Kalshi's COO "
                                        'reports over $25B per week in volume, so the screen redirects '
                                        'capital toward the deep markets carrying that flow.'}],
                 'completion_gate': 'This worksheet is complete only when your longshot and maker-taker '
                                    'figures come from real fills, every routed venue has a dated rules '
                                    'entry, each open position shows a priced round trip with doubled exit '
                                    'fees, and no market below the volume floor or with closed outcome '
                                    'information remains on the watchlist.'},
                {'worksheet_id': 'ws-03',
                 'number': 3,
                 'title': 'Event-Contract Rulebook and Secure Odds Pipeline Checklist',
                 'purpose': 'Screen every position and listing against insider, manipulation, '
                            'mention-contract, state-litigation, and conflicts exposure under the CFTC '
                            'framework, then prove that the odds feeds, API keys, and site-to-site tunnels '
                            'behind your operation are fresh, trimmed, secret, matched on both peers, and '
                            'verifiably passing traffic.',
                 'chapter_ref': 'Q5-Q6',
                 'instructions': ['Complete the conduct fields before the infrastructure fields, because a '
                                  'clean data pipe does not rescue a trade that is barred by insider or '
                                  'manipulation rules.',
                                  'List named employers, campaigns, and confidentiality agreements '
                                  'explicitly; vague categories cannot be enforced by a block list or '
                                  'reviewed later.',
                                  'For every odds source, write the refresh interval and cache duration as '
                                  'numbers in seconds, alongside the date you last confirmed them.',
                                  'Capture configuration values for both tunnel peers side by side, and '
                                  'paste the heartbeat, counter, and ping evidence rather than summarizing '
                                  'it.',
                                  'Re-run this sheet after any new listing, new state action, new data '
                                  'vendor, firewall change, or HA deployment touching your environment.'],
                 'fields': [{'name': 'insider_exposure_screen',
                             'type': 'textarea',
                             'prompt': 'List every contract whose outcome touches your job, your employer, '
                                       'your campaign, or any confidentiality agreement you have signed, '
                                       'and record the hard block that keeps your accounts and automated '
                                       'tools from ever trading those markets.',
                             'example': 'Miller says a signed confidentiality agreement turns such a trade '
                                        'into misappropriation and the CFTC will come after you '
                                        '[NEXTPredict — uh3GgMs9ha8 @ 00:14:13]. A former White House '
                                        "teleprompter operator's roughly 50 mention-market trades ended in "
                                        'a $65,000 penalty after disgorging about $100,000 to $107,000, so '
                                        'employer-linked tickers sit on a permanent block list.'},
                            {'name': 'manipulation_conduct_rule',
                             'type': 'textarea',
                             'prompt': 'Write the conduct rule that governs public statements, posts, and '
                                       'commentary about markets where you hold positions, and describe '
                                       'how you document cooperation and remediation steps should any '
                                       'trading activity ever draw an enforcement inquiry from regulators.',
                             'example': 'Even when trading your own information, Miller treats public '
                                        'misstatements pushed to move price as market manipulation '
                                        '[NEXTPredict — uh3GgMs9ha8 @ 00:09:44]. No position-holder posts '
                                        'about an open market. NEXTPredict notes that cooperating and '
                                        'remediating can earn up to a 25% discount absent extenuating '
                                        'circumstances, so a remediation file is kept current.'},
                            {'name': 'mention_contract_controls',
                             'type': 'textarea',
                             'prompt': 'Before listing or trading a mention or sports contract, identify '
                                       'who could control the outcome, which known insiders exist, and '
                                       'which position limits, accountability levels, reporting duties, '
                                       'and surveillance steps match the concentration of that control.',
                             'example': 'Potential controllers and known insiders are mapped first, then '
                                        'position limits, accountability, reporting, and surveillance are '
                                        'calibrated to them [🎓Profeissor.com🚀Digital Assets, AI & FinTech '
                                        '— YIkTrxNRVlc @ 00:05:20]. The CFTC staff advisory flags sports '
                                        'contracts because a small group of athletes can hold concentrated '
                                        'control over outcomes, so player-level contracts carry tighter '
                                        'limits.'},
                            {'name': 'state_litigation_exposure',
                             'type': 'textarea',
                             'prompt': 'Identify every state where your products or listings could face a '
                                       'direct state-court suit, explain the federal swap-definition and '
                                       'preemption argument you would rely on, and note how losing a '
                                       'first-filing option changes your response plan.',
                             'example': 'Nevada sued Polymarket and Massachusetts sued Kalshi directly in '
                                        'state court, skipping the cease-and-desist letter that once let '
                                        'operators file first federally [A Lawyer In Finance Explains  '
                                        '1.1M views — MHeX-gRNpCE @ 00:00:36]. Andrew Kim estimates swaps '
                                        'took roughly 65% of Third Circuit briefing and 90% of air time, '
                                        'so the response plan anchors on that definition.'},
                            {'name': 'conflicts_matrix',
                             'type': 'textarea',
                             'prompt': 'If you operate or partner with affiliated exchange, clearing, '
                                       'brokerage, or market-making entities, draft the conflicts matrix '
                                       'and describe how you document equal treatment of every member '
                                       'during incidents so rival complaints can be answered with records.',
                             'example': 'An affiliated DCM, FCM, DCO and market maker get a conflicts '
                                        'matrix, and every incident log shows each member treated equally, '
                                        'because complaints from rival FCMs go straight to the CFTC '
                                        '[PredictionNews — 9aHX4chc8YY @ 00:20:43]. Every registered DCM '
                                        'must also meet 23 core principles covering manipulation, position '
                                        'limits, governance, conflicts, and system safeguards.'},
                            {'name': 'odds_feed_refresh_audit',
                             'type': 'textarea',
                             'prompt': 'Record the refresh interval, uptime figure, and cache duration of '
                                       'every odds source feeding your models or dashboards, and state the '
                                       'maximum staleness you accept before a price is excluded from '
                                       'arbitrage or value calculations entirely.',
                             'example': 'OddsJam refreshes most markets every five seconds with 99.9 '
                                        'uptime and dismisses five-minute delayed feeds as useless when '
                                        'injury news moves lines [OddsJam: Sports Betting Strategy & '
                                        'Education — ZTKIge6SyQI @ 00:00:15]. SportsGameOdds caches '
                                        'responses for 30 seconds and refreshes its dashboard on the same '
                                        'cadence, so 30 seconds becomes the staleness ceiling.'},
                            {'name': 'api_request_trimming',
                             'type': 'text',
                             'prompt': 'Show how each odds request is narrowed to only the markets and '
                                       'bookmakers you actually use, which parameters you pass, and how '
                                       'you catch errors when a required region or bookmaker key is '
                                       'missing from the call.',
                             'example': 'Requests pass trimmed oddIDs and a single bookmakerID, the two '
                                        'levers the official docs name for lightning-fast responses '
                                        '[SportsGameOdds API — auctQZC3iOE @ 00:03:50]. The fetcher '
                                        'validates region and bookmaker parameters before sending, after '
                                        'Coding with Ado hit a missing regions or bookmakers key error '
                                        '[Coding with Ado — MkF4ThP7PRs @ 00:04:31].'},
                            {'name': 'secret_key_handling',
                             'type': 'text',
                             'prompt': 'Explain where odds API keys are stored, which server-side process '
                                       'attaches them to requests, which header carries them, and how you '
                                       'confirm that no key ever reaches the browser, a client bundle, or '
                                       'a shared spreadsheet.',
                             'example': 'Keys live in .env.local on the server so they never reach the '
                                        'browser, and a Next.js server route sends them in the X-API-Key '
                                        'header [SportsGameOdds API — JXdlRbDVFNY @ 00:01:21]. Before each '
                                        'deploy, the built client bundle is searched for the key string, '
                                        'and any match blocks the release.'},
                            {'name': 'vpn_tunnel_parameter_match',
                             'type': 'textarea',
                             'prompt': 'For each site-to-site tunnel protecting your odds infrastructure, '
                                       "list both peers' protected subnets, IKE version, IPsec lifetime, "
                                       'PFS setting, pre-shared key status, and NAT exemption, confirming '
                                       'every value matches before the configuration is deployed to the '
                                       'firewall.',
                             'example': "Silesio's tunnel stayed down until PFS was enabled on the FTD, so "
                                        'PFS, IPsec lifetime, IKEv2, and the pre-shared key are checked '
                                        'side by side on both peers [Silesio Carvalho — 1hYtt8kbt1g @ '
                                        '00:12:41]. Tunnel traffic is exempted from NAT, and pending '
                                        'changes are deployed before any HA pair forms, expecting the '
                                        'Snort restart.'},
                            {'name': 'tunnel_traffic_proof',
                             'type': 'textarea',
                             'prompt': 'Describe the evidence you require before declaring a tunnel live, '
                                       'covering heartbeat timing, the last disconnect reason, encrypted '
                                       'packet counters, and host-to-host pings, plus the firewall checks '
                                       'you run when the tunnel shows up but pings fail.',
                             'example': 'Registration completed only proves the tunnel was established in '
                                        'the past; heartbeat send time is compared against receive time '
                                        '[Hexward Labs | Cybersecurity Tools + AI — gsvmpPQY_ak @ '
                                        '00:03:57]. Show crypto IPsec SA must show encrypted counters '
                                        'climbing, and when pings fail, the tunnel access control setting '
                                        "and the test PC's Windows firewall are checked [NET Learners — "
                                        'gd0RJEsarik @ 00:23:54].'}],
                 'completion_gate': 'This worksheet is complete only when every employer-linked or '
                                    'campaign-linked contract sits on an enforced block list, each mention '
                                    'or sports listing has calibrated limits and surveillance, every odds '
                                    'source has a numeric staleness ceiling, API keys are proven absent '
                                    'from client code, and each tunnel shows matched parameters, live '
                                    'heartbeats, climbing counters, and passing host pings.'},
                {'worksheet_id': 'ws-04',
                 'number': 4,
                 'title': 'Affiliate Deal Math and Operator Partnership Ledger',
                 'purpose': 'Convert every commission headline into effective per-player value, then '
                            'pressure-test each operator relationship on GEO fit, payments, review '
                            'integrity and contract terms before a single additional FTD is sent.',
                 'chapter_ref': 'Q7-Q8',
                 'instructions': ['Pull the signed contract, not the pitch deck, for every operator you '
                                  'list before filling any field.',
                                  'Run each revshare offer through the GGR-to-NGR walkdown and each CPA '
                                  'through its qualification rule and cap.',
                                  'Cite the practitioner benchmark you compared against beside every '
                                  'figure, using the channel, ID and timestamp format.',
                                  'Mark any field you cannot complete with real numbers as open, and do '
                                  'not send scaled traffic to that operator.',
                                  'Revisit the ledger monthly, because carryover, EPC and GEO conversion '
                                  'shift without notice.'],
                 'fields': [{'name': 'ngr_definition_walkdown',
                             'type': 'textarea',
                             'prompt': 'Take one live revshare offer and walk its contract from a full '
                                       'month of GGR down to NGR. List every deduction the operator '
                                       'applies, including bonuses, tax and processing, then compute the '
                                       'effective percentage of gross you actually receive.',
                             'example': 'A $1,000 GGR month loses $150 to bonuses, $100 to tax and $50 to '
                                        'processing, leaving $700 NGR. At a 35% deal that pays $245, an '
                                        'effective 24.5% of gross, which is why a 30% deal can beat it '
                                        '[15M iGaming Media & Dealflow Platform — WaWQNIAchz0 @ 00:04:55]. '
                                        'Record each deduction line exactly as the contract names it.'},
                            {'name': 'cpa_qualification_math',
                             'type': 'textarea',
                             'prompt': 'For every CPA deal under review, write the headline payout, the '
                                       'qualifying deposit and wager rule, any cap, and the share of '
                                       'referred players who actually qualify. Divide through to the '
                                       'effective per-player value before you scale any traffic.',
                             'example': 'Headline CPA $400, requiring a $400 deposit and wager. Only 5% of '
                                        'referred players qualify, so the real value is $20 per player '
                                        '[iGaming Marketing Agency Tips by Christian Strutt — _puyhQJIomQ '
                                        '@ 00:06:35]. Benchmark against the Track360 tier-1 range of '
                                        '$150-$400 with a $250 median, which the 15M iGaming presenter '
                                        'flags as indicative rather than universal.'},
                            {'name': 'negative_carryover_terms',
                             'type': 'text',
                             'prompt': 'Quote the exact negative carryover clause from each contract and '
                                       'state whether balances reset monthly or roll forward indefinitely. '
                                       'Note which operators refused to change the clause and whether you '
                                       'walked away or accepted the risk in writing.',
                             'example': 'Operator B uses rolling negative carryover. The case of a player '
                                        'who won about 20,000 and later lost about 10,000 is why Strutt '
                                        'calls monthly resets a must [iGaming Marketing Agency Tips by '
                                        'Christian Strutt — 6jlPOcl5CnI @ 00:14:13]. Requested a monthly '
                                        'reset over Telegram after rejecting the first offer; the deal '
                                        'stays paused until the clause is rewritten.'},
                            {'name': 'cpa_hold_release_rule',
                             'type': 'text',
                             'prompt': 'Define the on-hold rule for CPA conversions in your tracking '
                                       'platform. State how long a conversion stays held, what post-bonus '
                                       'play you check, and the NGR condition that must be met before the '
                                       'payout is released to the affiliate.',
                             'example': 'Every CPA conversion lands on-hold. Release only after confirming '
                                        'the player kept playing past the bonus and generated positive NGR '
                                        '[Trackdesk — zjkFJJ0rAJ0 @ 00:05:40]. Trackdesk stresses the fix '
                                        'is not a fraud detection tool bolted on after the fact [Trackdesk '
                                        '— zjkFJJ0rAJ0 @ 00:04:28]. Hold window: set per operator '
                                        'contract, logged beside the deal.'},
                            {'name': 'rtp_and_withdrawal_check',
                             'type': 'textarea',
                             'prompt': 'Before promoting a project, record the RTP it actually runs on '
                                       'Pragmatic and Playing go titles, its withdrawal limits and payout '
                                       'speed, and any combined-wager bonus terms. Flag every number that '
                                       'diverges from what other projects show.',
                             'example': 'Inspecting network requests on a Playing go slot showed 91% RTP '
                                        'against 96% elsewhere, a short-term RTP play [Traffic Cardinal EN '
                                        '— Affiliate Press — GRpptuPlok4 @ 00:06:31]. Its welcome offer '
                                        'applies x40 to deposit plus bonus, effectively x80 and almost '
                                        'unplayable [Traffic Cardinal EN — Affiliate Press — GRpptuPlok4 @ '
                                        '00:11:00]. Verdict: do not promote until the operator fixes '
                                        'both.'},
                            {'name': 'tracking_link_map',
                             'type': 'text',
                             'prompt': 'Map one tracking link to each traffic channel you run, then record '
                                       'clicks, depositing players and click-to-deposit conversion per '
                                       'link. Mark which channel is scaling now and the signal that will '
                                       'tell you its gap has saturated.',
                             'example': 'Separate links for SEO pages, Telegram and a streamer partnership '
                                        'show Telegram producing most depositing players, so scale it '
                                        'while it works, because gaps saturate [iGaming Marketing Agency '
                                        'Tips by Christian Strutt — 3ZUgO2w5vfU @ 00:13:50]. Strutt treats '
                                        '1 to 5% click-to-depositor conversion as good [iGaming Marketing '
                                        'Agency Tips by Christian Strutt — 6jlPOcl5CnI @ 00:07:53]. Follow '
                                        'the money.'},
                            {'name': 'portfolio_model_split',
                             'type': 'textarea',
                             'prompt': 'Lay out your operator portfolio by commission model: how many '
                                       'brands sit on revshare, hybrid and CPA, the FTDs each group '
                                       'receives, and the modeled monthly commission per group. Explain '
                                       'why this split suits your cash needs.',
                             'example': 'Thirty FTDs a month on €6,000 of player deposits, split across '
                                        'revshare, hybrid and CPA groups of 10 casinos each, models €750, '
                                        '€900 and €800, or €2,450 per site [CASINOAFFMASTERY — JUjTzv8yGw4 '
                                        '@ 00:14:52]. CPA covers near-term liquidity while revshare builds '
                                        'lifetime upside; hybrids make up about 45% of new tier-1 deals, '
                                        'so test one hybrid first.'},
                            {'name': 'geo_segmentation_plan',
                             'type': 'textarea',
                             'prompt': 'Segment your traffic by GEO and list, for each, the operators you '
                                       'send it to, their top-converting GEOs, and the local payment '
                                       'methods available. Estimate what share of your earning potential '
                                       'leaks when segments are mixed. Name each GEO explicitly.',
                             'example': 'Morocco, US and LatAm traffic now route separately. Nikoghosyan '
                                        'warns that without GEO segmentation a 100K-a-month potential '
                                        'becomes 10K earned and 90K burned [Odys Podcast: The High Stakes '
                                        'Growth Show — ohEZ5-gHckQ @ 00:20:12]. Canada pages list only '
                                        'Interac-enabled licensed casinos after test deposits as a player '
                                        '[Ace Alliance — R-_FHgwDEFQ @ 00:12:03].'},
                            {'name': 'operator_vetting_gate',
                             'type': 'textarea',
                             'prompt': 'Run each new operator through your vetting gate: months live, '
                                       'payment confirmations from other affiliates, defined GEO focus, '
                                       'licensing status, and forum complaints about late payments. Record '
                                       'the pass or fail result and the evidence behind each line.',
                             'example': "Brand X is two months old and pitches 'we work worldwide' with no "
                                        'defined GEO. Fail: new brands can vanish, so wait until other '
                                        'affiliates confirm payment [Odys Podcast: The High Stakes Growth '
                                        'Show — ohEZ5-gHckQ @ 00:12:00], and worldwide pitches pay listing '
                                        'fees, fail to convert and get delisted [Peaky Ads – Marketing '
                                        'Podcasts & Interviews — JCr5X66vWg4 @ 00:15:02].'},
                            {'name': 'review_integrity_and_relationship',
                             'type': 'textarea',
                             'prompt': 'Document your review integrity and partner contact rules: how star '
                                       'ratings are set, how operator requests for higher scores are '
                                       'handled, how often you speak with each affiliate manager, and '
                                       'which backup traffic sources stay live alongside your main '
                                       'channel.',
                             'example': 'Stars come from user reviews only, negative reviews stay visible, '
                                        'and requests for a five-star score are refused [Ace Alliance — '
                                        'R-_FHgwDEFQ @ 00:23:35]. Weekly calls with each affiliate manager '
                                        'supply forward-looking offer information, and SEO, Telegram and '
                                        'paid social stay live as plan B and plan C [Revpanda Group — '
                                        'qOL8mMQPJyI @ 00:12:42].'}],
                 'completion_gate': 'Every active operator shows an effective commission figure, a monthly '
                                    'carryover reset or a written risk acceptance, a CPA hold rule, a '
                                    'verified RTP and withdrawal check, and a passed vetting gate; any '
                                    'operator missing one of these receives no new traffic.'},
                {'worksheet_id': 'ws-05',
                 'number': 5,
                 'title': 'Compliant Launch Stack and the +EV Betting Workflow',
                 'purpose': 'Document the license, payment, KYC, affiliate and advertising controls that '
                            'keep a launch inside the rules, then codify the sharp-reference, tailing, '
                            'bankroll and account-longevity rules behind every positive-EV wager.',
                 'chapter_ref': 'Q9-Q10',
                 'instructions': ["Treat the license holder as owner of every partner's behavior and write "
                                  'each answer from that position.',
                                  'Attach evidence for each compliance claim: provider contracts, '
                                  'processor approvals, geofence screenshots or dashboard screen-share '
                                  'notes.',
                                  'On the betting side, name the sharp book or exchange used as the source '
                                  'of truth for each market before recording any edge.',
                                  'Cite the practitioner benchmark beside each number in channel, ID and '
                                  'timestamp format.',
                                  'Any market with no sharp price, any unverified partner and any creative '
                                  'without a geofence is logged as blocked until fixed.'],
                 'fields': [{'name': 'launch_model_choice',
                             'type': 'textarea',
                             'prompt': 'Compare white-label and turnkey launch paths for your sportsbook '
                                       'or casino. Record the launch window, the NGR or GGR share the '
                                       'provider takes, whose license you operate under, and the exposure '
                                       'if a fellow sub-licensee goes rogue.',
                             'example': 'White label: live in 2-6 weeks for a 10-15% NGR share, versus '
                                        'turnkey builds needing their own licenses, payment contracts and '
                                        'servers [Metablock iGaming — 3O-jguNKEvw @ 00:06:26]. Risk noted: '
                                        'one rogue sub-licensee could get the master license pulled, '
                                        'taking all operators offline [Metablock iGaming — XyJxTxBFvuw @ '
                                        '00:16:06]. Provider pitch of zero GGR share flagged for '
                                        'clarification.'},
                            {'name': 'payment_processing_plan',
                             'type': 'textarea',
                             'prompt': 'Detail your high-risk card processing setup: the MCC you are '
                                       'classified under, expected rates, reserves and volume caps, the '
                                       'backup processor, the approval timeline, and what players see at a '
                                       'declined deposit. Include the verified payout rail.',
                             'example': 'Card processing runs on MCC 7995 with no 3-D Secure liability '
                                        'shift. Budgeted higher rates, reserves and volume caps, kept a '
                                        'backup processor, and planned for several weeks of approval '
                                        '[High-Risk Merchant Accounts | Adaptiv Payments — jerDG4rTmK8 @ '
                                        '00:03:15]. Declines show an alternative payment method on the '
                                        'spot, and payouts go only to verified players via Visa OCT or '
                                        'ACH.'},
                            {'name': 'kyc_and_license_file',
                             'type': 'textarea',
                             'prompt': 'List every document in your license and KYC file, from founder '
                                       'identity and criminal record checks to source-of-wealth proof, and '
                                       'describe player verification at signup. Note which markets demand '
                                       'stronger evidence than the one you hold today.',
                             'example': 'Player signup requires ID upload plus a roughly three-second live '
                                        'selfie face-match; Pennsylvania reports chargebacks down 50% over '
                                        '10 months after adding it [PA Gaming Control Board — gpGZLcIMERI '
                                        '@ 00:18:34]. Founder file holds passports and criminal records, '
                                        'but source-of-wealth documents accepted in one market may be '
                                        'insufficient in another [License Gentlemen — 4mTaeo1ds6g @ '
                                        '00:02:07].'},
                            {'name': 'affiliate_licensing_and_liability',
                             'type': 'textarea',
                             'prompt': 'For each market, record whether performance affiliates need their '
                                       'own license, the fee and withholding involved, the penalties for '
                                       'working unlicensed, and whether the operator is liable for partner '
                                       "advertising. State how you verify each partner's status.",
                             'example': 'Bulgaria: CPA, revshare and hybrid affiliates pay about €6,000 a '
                                        'year plus 10% of commission withheld for the state, and '
                                        'unlicensed work risks fines up to €20,000 [3SNET — XUPjmWHBPq4 @ '
                                        '00:01:32]. The regulator looks at the substance of the deal, not '
                                        'the label [3SNET — XUPjmWHBPq4 @ 00:01:51]. Brazil makes '
                                        'operators liable for partner ads.'},
                            {'name': 'affiliate_fraud_controls',
                             'type': 'textarea',
                             'prompt': 'Describe the controls that stop fake-account CPA farming: the '
                                       'minimum qualifying deposit, how you verify affiliate dashboards, '
                                       'which scammer lists you check, and the behavior that marks a '
                                       'partner as a red flag before any payout goes out.',
                             'example': 'A €30 CPA triggered by a €5 deposit lost €30,000 on 1,000 fake '
                                        'accounts [License Gentlemen — CmKMSqyx4r0 @ 00:03:54]. New rule: '
                                        'qualifying deposits raised, live screen-shares of affiliate '
                                        'dashboards instead of blurry screenshots, and Telegram scammer '
                                        'lists checked before payment [License Gentlemen — CmKMSqyx4r0 @ '
                                        '00:09:00]. Partners who chase aggressively are flagged, because '
                                        'good affiliates do not chase you.'},
                            {'name': 'advertising_geofence_log',
                             'type': 'text',
                             'prompt': 'Log the geofence for every live creative: the licensed region, the '
                                       'location settings checked on YouTube, Instagram and TV, the date '
                                       'checked, and any complaint received. Name the markets you rate as '
                                       'highest risk for player complaints.',
                             'example': 'Spring creative restricted to the licensed province; YouTube and '
                                        'Instagram location settings verified, TV buy confirmed regional. '
                                        'Ontario, Kahnawake and Alberta treated as riskiest, since sneaky '
                                        'players who know the law file complaints [Ace Alliance — '
                                        'ebby4L0y_P0 @ 00:02:28]. TikTok Lives capped at 60 to 90 minutes, '
                                        'recordings reviewed within the 30-day storage window [Capperway — '
                                        'uMAJwS6tPzw @ 00:18:58].'},
                            {'name': 'sharp_reference_selection',
                             'type': 'textarea',
                             'prompt': 'For each market type you bet, name the sharp book or exchange you '
                                       'treat as the source of truth, the devig method you apply, and the '
                                       'soft books you target. Mark any market where no sharp book posts a '
                                       'price.',
                             'example': 'Main lines devig to Pinnacle using worst case, always worst case '
                                        '[OddsJam: Sports Betting Strategy & Education — iWi1gqgw35Y @ '
                                        '00:05:16]. Player props: bet soft books with sharp books as the '
                                        'devig [OddsJam: Sports Betting Strategy & Education — iWi1gqgw35Y '
                                        '@ 00:09:52]. MLB player singles have no Pinnacle or Circa line, '
                                        'so a 1.95% Cal Raleigh edge is killed.'},
                            {'name': 'sharp_money_tail_rules',
                             'type': 'textarea',
                             'prompt': 'Write the rules you apply before tailing a large exchange order: '
                                       'minimum size relative to the sharp book limit, time window before '
                                       'start, maximum price premium over the sharp bettor, and the check '
                                       'for a hidden arbitrage.',
                             'example': 'Tail only when Novig or ProphetX size clears the Pinnacle, Circa '
                                        'or BetOnline limit by at least 3x, inside 2 hours of start, '
                                        'paying no more than 5 cents above the sharp price [OddsJam: '
                                        'Sports Betting Strategy & Education — J3KQ5FaneSs @ 00:07:45]. '
                                        'The offered side is the side the trader does not want, so check '
                                        'for a finishing arbitrage.'},
                            {'name': 'bankroll_strategy_split',
                             'type': 'textarea',
                             'prompt': 'State your current bankroll and whether it is committed to '
                                       'arbitrage, one-sided positive EV, or both. Record volume staked, '
                                       'bets per day and ROI for each strategy over your last full month, '
                                       'and the threshold for switching.',
                             'example': 'Bankroll $2,400, so arbitrage only until it clears $3,000, '
                                        'because a small roll cannot absorb losing days [OddsJam: Sports '
                                        'Betting Strategy & Education — uxFJJTsfAhc @ 00:05:53]. '
                                        'Benchmark: 10.6% on $84,222 of mostly live arbitrage over 12 days '
                                        'versus about 8.5% on almost $32,000 of pre-match +EV over 13 days '
                                        '[OddsJam: Sports Betting Strategy & Education — uxFJJTsfAhc @ '
                                        '00:02:41].'},
                            {'name': 'account_longevity_playbook',
                             'type': 'textarea',
                             'prompt': 'Describe how you protect new soft-book accounts from early limits: '
                                       'which bets you place first, which device you bet from, how you '
                                       'round stake sizes, and how many sharp-looking bets you allow '
                                       'before an account has aged.',
                             'example': 'New Fanatics and BetRivers accounts open with main-market parlays '
                                        'from the parlay tool, since unders and arbs can trigger limits '
                                        'within three bets [Billy Collins — AcW1ucJmvQc @ 00:04:29]. All '
                                        'bets go through the mobile app [Billy Collins — AcW1ucJmvQc @ '
                                        '00:11:41]. Stakes round to zeros and fives, never $50.40 '
                                        '[OddsJam: Sports Betting Strategy & Education — bKaCBMQuXgk @ '
                                        '00:06:52].'}],
                 'completion_gate': 'Launch proceeds only when the platform model, processor and backup, '
                                    'KYC file, affiliate licensing, fraud controls and geofence log are '
                                    'complete; betting proceeds only when every market has a sharp '
                                    'reference, tailing rules are written, and the bankroll threshold is '
                                    'met.'},
                {'worksheet_id': 'ws-06',
                 'number': 6,
                 'title': 'Traffic Acquisition Audit and CFTC Counterparty Controls',
                 'purpose': 'Audit the SEO, owned-audience and paid channels that bring depositing '
                            'players, then confirm that every broker, FCM, perpetual venue and automated '
                            'agent in the trading stack is registered, collateralized and controllable.',
                 'chapter_ref': 'Q11-Q12',
                 'instructions': ['Start with technical SEO and indexing status; no link or paid budget is '
                                  'approved until search engines see the content.',
                                  'Record every acquisition figure as an effective cost per FTD, not a '
                                  'headline CPA or a click count.',
                                  'Rate each authority-borrowing tactic on core-update risk and keep it '
                                  'away from the money site unless the register says otherwise.',
                                  'For every trading counterparty, confirm CFTC registration and NFA '
                                  'membership in NFA BASIC before any transfer.',
                                  'Cite the practitioner benchmark beside each figure in channel, ID and '
                                  'timestamp format, and re-audit after every core update or rule change.'],
                 'fields': [{'name': 'seo_foundation_check',
                             'type': 'text',
                             'prompt': 'Before buying any link, confirm that search engines actually see '
                                       'your content. Record the technical SEO audit result, the '
                                       'pre-rendering status, Bing Webmaster Tools setup, and the date '
                                       'each check passed on your main money pages. Note any page still '
                                       'failing.',
                             'example': 'Tech SEO and pre-rendering confirmed on all casino review pages '
                                        'before the first link purchase [Big Pond Digital — 0_KHkuMmtVQ @ '
                                        '00:19:11]. Bing Webmaster Tools set up because ChatGPT draws on '
                                        'Bing; the listicles AI answers cite are being reverse-engineered '
                                        '[Big Pond Digital — 0_KHkuMmtVQ @ 00:33:17]. Link budget stays '
                                        'frozen until both checks pass.'},
                            {'name': 'link_profile_maintenance',
                             'type': 'textarea',
                             'prompt': 'Describe how you build and maintain your link profile: the '
                                       'relevance signals each new link must satisfy, your anchor text '
                                       'baseline, the annual decay rate you measure, and the recovery '
                                       'process for links that drop out of the index.',
                             'example': 'Every link must hit at least two of domain, article content and '
                                        'anchor relevance, with brand or naked URL as baseline [Odys '
                                        'Podcast: The High Stakes Growth Show — ESj1bVRdO2s @ 00:28:24]. '
                                        'Expect about 7% loss per year; export from Majestic, sort by last '
                                        'seen, and submit to Giga Indexer, about 72 hours [Big Pond '
                                        'Digital — 0_KHkuMmtVQ @ 00:44:49].'},
                            {'name': 'black_hat_risk_register',
                             'type': 'textarea',
                             'prompt': 'List every tactic in your SEO plan that borrows authority, such as '
                                       'expired domains, canonical tricks or parasite pages. For each, '
                                       'record the expected ranking gain, the core-update risk, and '
                                       'whether the money site is exposed to any penalty.',
                             'example': 'An expired-domain play is ranking now, but Strutt reports black '
                                        'hat getting zeroed on core updates and EVERNET warns that '
                                        'authority-borrowing tricks tend to get caught. Decision: keep it '
                                        'off the money site. Any agency pitch is vetted for a dated FTD '
                                        'case study and rejected if it offers PBN packages or guaranteed '
                                        'first-page rankings [Linkee ai — PGdrtjIirPk @ 00:04:04].'},
                            {'name': 'owned_audience_funnel',
                             'type': 'textarea',
                             'prompt': 'Map how traffic converts into an owned audience: the capture '
                                       'channels you run, such as app, email or Telegram, the conversion '
                                       'event you optimize, and your current conversion rate measured '
                                       'against a target. Explain what counts as success.',
                             'example': 'Target is 20%-plus conversion into a banner click, subscription '
                                        'or add-to-bet-slip, against vanity traffic converting well under '
                                        '1% [Revpanda Group — OlzqNLFabLI @ 00:14:21]. Add-to-bet-slip is '
                                        'now the number one priority [Revpanda Group — OlzqNLFabLI @ '
                                        '00:54:43]. Telegram and email capture sit on every prediction '
                                        'page, reflecting a big belief in owning the audience [Revpanda '
                                        'Group — Xyf6JUN9RFg @ 00:00:13].'},
                            {'name': 'tournament_traffic_plan',
                             'type': 'textarea',
                             'prompt': 'Plan your World Cup 2026 content: the head terms you will skip, '
                                       'the team, match or player-level pages you will build instead, when '
                                       'the hubs must be indexed, and how you will handle paid cost spikes '
                                       'at peak moments.',
                             'example': 'Skipping the World Cup betting head term for local team and match '
                                        'pages plus player-level prediction markets [Revpanda Group — '
                                        'Xyf6JUN9RFg @ 00:01:34]. Ghana-style per-team hubs go live well '
                                        'before the 39-day traffic window [Revpanda Group — OlzqNLFabLI @ '
                                        '00:23:11]. Paid budget assumes CPC rising around 40 to 80% during '
                                        'peak moments [Revpanda Group — OlzqNLFabLI @ 00:22:00].'},
                            {'name': 'paid_acquisition_economics',
                             'type': 'textarea',
                             'prompt': 'For every paid or CPA-guaranteed deal, record the headline CPA, '
                                       'any click-to-FTD guarantee, the clicks actually needed per FTD, '
                                       'and the resulting effective cost. State whether campaigns optimize '
                                       'to FTDs or sign-ups and how bots are filtered.',
                             'example': 'German deal: €800-900 headline CPA with a 20% click-to-FTD '
                                        'guarantee; at 10 clicks per FTD the effective cost lands at '
                                        '€1,600 [Big Pond Digital — jWqa6ck6G3Y @ 00:21:00]. Campaigns '
                                        'optimize to FTDs, not sign-ups, with bots filtered, '
                                        'pre-conversion metrics tracked and no fast scaling [Revpanda '
                                        'Group — OlzqNLFabLI @ 00:27:01]. PPC waits for a converting '
                                        'brand.'},
                            {'name': 'tracking_balance_audit',
                             'type': 'text',
                             'prompt': 'Audit every tracking link and program balance this month. Record '
                                       'any balance that dropped to zero, links the program invalidated, '
                                       'and dead brands still receiving traffic, plus the lifetime value '
                                       'you expect per referred revshare player. Date each finding.',
                             'example': 'Two program balances dropped to zero and one invalidated link '
                                        'still pointed at a dead brand; all three were rerouted after the '
                                        'audit [Olga Zarr SEO — j9LMpZesI1o @ 00:06:19]. Revshare at '
                                        '25-50% is valued at $500-$2,000 per player, with one signup '
                                        'reported paying $11,000 a month [Powerhouse Affiliate — '
                                        'pihR_hy7xRU @ 00:00:15].'},
                            {'name': 'broker_registration_check',
                             'type': 'text',
                             'prompt': 'Before wiring funds to any broker, FCM or introducing broker, '
                                       'record the CFTC registration, NFA membership, the NFA BASIC lookup '
                                       'date, any enforcement history, and the leverage limits and capital '
                                       'floor that apply to the account type.',
                             'example': 'Retail forex dealer confirmed in NFA BASIC with both CFTC '
                                        'registration and NFA membership; if either were missing, walk '
                                        'away [Brokerchampion — CIinXD9tbVo @ 00:06:10]. Leverage capped '
                                        'at 50:1 on seven majors and 20:1 elsewhere, and the RFED must '
                                        'hold at least $20 million in capital [Brokerchampion — '
                                        'CIinXD9tbVo @ 00:02:46]. Enforcement records reviewed: none.'},
                            {'name': 'collateral_and_perpetual_risk',
                             'type': 'textarea',
                             'prompt': 'Describe the collateral and funding risk on any leveraged or '
                                       'perpetual position: how your FCM is vetted, how customer funds are '
                                       "held, the venue's premium math and observation periods, and the "
                                       'worst-case funding cost per day you have modeled.',
                             'example': 'FCM vetted with the Vanguard checklist: capital levels, '
                                        'investments limited to top-tier 1.25 securities, audit and '
                                        'seg-compliance history, custodian rigor [CFTC — yUqRhv7w9Vs @ '
                                        '02:17:28]. Perpetual funding pays every 8 hours, capped near 2% '
                                        'per period and up to 6% per 24 hours, so the position is sized to '
                                        'survive maximum funding [CFTC — ZEPjpgVSavY @ 00:08:07].'},
                            {'name': 'agent_controls_and_reporting',
                             'type': 'textarea',
                             'prompt': 'Document controls for any automated or AI agent that trades on '
                                       'your behalf: where risk limits and audit logs run, how the kill '
                                       'switch is tested, who answers for agent misbehavior, and which '
                                       'compliance report format your firm files.',
                             'example': 'Risk controls and audit logs run outside the agent harness, '
                                        'backed by hard limits and a kill switch that turns agents off '
                                        '[CFTC — Ckw1w5mSMIQ @ 01:04:27]. The deploying firm is named as '
                                        'accountable. CCO filing is either the unredacted home-regulator '
                                        'report or a full Reg 3.3 report, never a hybrid [A Lawyer In '
                                        'Finance Explains  1.1M views — BO0iMB23sU4 @ 00:04:39].'}],
                 'completion_gate': 'Close the worksheet only when indexing is verified, effective FTD '
                                    'cost is known for every paid deal, tracking balances are reconciled, '
                                    'every counterparty passes NFA BASIC, perpetual funding is modeled at '
                                    'the cap, and agent controls run outside the harness with a tested '
                                    'kill switch.'}]}
