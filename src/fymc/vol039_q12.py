from __future__ import annotations

CHAPTER_12 = {'id': 'Q12',
 'chapter_id': 'Q12',
 'chapter_number': 12,
 'question_number': 12,
 'slug': 'pay-per-call-unit-economics-call-quality-scaling-case-studies',
 'question_prompt': 'What makes a call billable, how do payouts, margins and quality control work, and '
                    'what do real scaling case studies show?',
 'kicker': 'Q12 / THE BIG MONEY PLAYBOOKS',
 'title': 'Unit Economics, Call Quality, and Scaling Case Studies',
 'subtitle': 'Economics of a call, billing, payouts and margins, net terms with publishers, reading '
             'campaign rules, billable call criteria, quality assurance, fraud control, call center lead '
             'verification, optimization reporting, and debt settlement and million-dollar case studies',
 'layout_template': 'action_worksheet_summary',
 'reading_time_minutes': 15,
 'executive_summary': 'Practitioners from TrackDrive, Ringba, ExclusiveLiveCall, Marketcall, John Ventura, '
                      'Yoder, ceohec and DigitalTriggers agree on one rule: the payout rate alone never '
                      'proves a deal is profitable. Margin lives in the spread between buyer price and '
                      'publisher payout. Rejected calls, duplicates, callback fraud, telecom costs and '
                      'buyer credit risk then eat into it. Street numbers cluster around $35 publisher '
                      "payouts against $50+ buyer prices and 90-second billable thresholds. Marketcall's "
                      'debt-settlement funnel converts 25-35% of calls to billable. Operators demand '
                      'upfront buyer deposits, align net terms so wires clear before publishers are paid, '
                      'and run QA as a profit center. They disagree on duration-based versus '
                      'conversation-based billing and on network versus direct-to-business selling. They '
                      'also split on whether to chase cheap calls or pricier calls that close one in three '
                      'or four.',
 'key_metrics': [{'label': 'Affiliate-to-Buyer Spread Per Call',
                  'metric': 'Affiliate-to-Buyer Spread Per Call',
                  'value': '$35 affiliate payout vs $50+ buyer price = $15 spread; 500 calls/day = '
                           '$7,500/day',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "John Ventura's core middleman math, scaled to '$225,000 every single month' "
                             'at 500 calls per day',
                  'source': 'John Ventura ([KeC4mKXnzs4 @ 00:03:05])'},
                 {'label': 'Margin Collapse When Paying On All Calls',
                  'metric': 'Margin Collapse When Paying On All Calls',
                  'value': '30% margin ($1,200) falls to 12.5% ($500)',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "TrackDrive's illustrative 100-call example where the publisher is paid on "
                             'all 100 calls instead of the 80 that qualify',
                  'source': 'TrackDrive ([yYZ5s6jFzQs @ 00:02:04])'},
                 {'label': 'Call-to-Billable Conversion Rate',
                  'metric': 'Call-to-Billable Conversion Rate',
                  'value': '25-35% of calls go billable (>90s); 8-13% of billable calls enroll',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Marketcall's debt settlement Facebook funnel benchmarks from an 8-month case "
                             'run',
                  'source': 'Marketcall ([Dq9KUpYUWsE @ 00:09:49])'},
                 {'label': 'Minimum Billable Rate Before Scaling',
                  'metric': 'Minimum Billable Rate Before Scaling',
                  'value': '50% or higher billable rate, plus positive post-reconciliation margin and '
                           'clean QA',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "John Ventura's fifth step: scale only past this bar and never add 10 "
                             'affiliates at once',
                  'source': 'John Ventura ([KeC4mKXnzs4 @ 00:09:37])'}],
 'sections': [{'section_number': 1,
               'title': 'The Practitioner Consensus',
               'paragraphs': ['Every operator who breaks down a call starts from the same place. The '
                              'payout headline means nothing until it is set against the buyer price, the '
                              'qualification rules and the hidden costs underneath. TrackDrive frames its '
                              'numbers as illustrative rather than benchmarks, then walks 100 calls '
                              'through the machine. Eighty qualify, and the buyer pays $50 on each for '
                              '$4,000. The publisher earns $35 on each for $2,800, and the operator keeps '
                              '$1,200, a 30% margin [yYZ5s6jFzQs @ 00:01:20]. ExclusiveLiveCall runs the '
                              'same logic at a higher price point. A $200 buyer and a $150 publisher leave '
                              'a $50 gross spread, or $5,000 on 100 calls. Telecom, AI, processing, '
                              'chargebacks and bad debt still come out of that spread, and $2 saved across '
                              '10,000 transactions is $20,000 [b7P50zcQzTs @ 00:02:32]. John Ventura '
                              'describes the model as pure middleman arbitrage, likening it to Amazon, '
                              'Uber and Airbnb. Affiliates accept $35 and buyers pay $50 or more, so the '
                              '$15 spread on 500 calls a day becomes $7,500 daily, or $225,000 a month '
                              '[KeC4mKXnzs4 @ 00:03:05]. TrackDrive states the consensus line directly: '
                              'the rate alone never tells you if a deal is profitable, so know your margin '
                              'before you negotiate a payout [yYZ5s6jFzQs @ 00:02:27].',
                              'The second point of agreement is that the billable event defines the money. '
                              'TrackDrive shows what happens when an operator pays the publisher on all '
                              '100 calls instead of the 80 that qualify. Payout jumps to $3,500 and margin '
                              'collapses from 30% to $500, or 12.5%, because rejected calls come straight '
                              'out of margin [yYZ5s6jFzQs @ 00:02:04]. Nate of Money Printer Marketing, '
                              'interviewed on Yoder, works off a 90-second billable duration, and the '
                              'warning is blunt: hang the phone up before 90 seconds or the call gets '
                              "charged [-GEw-hz8tiY @ 00:06:29]. Marketcall's debt settlement offer prices "
                              'the same way. English calls over 90 seconds pay $55-60 and Spanish calls '
                              'pay $50-55. A private offer pays $20-25 for calls over just 10 seconds, and '
                              'every state except Oregon is accepted, Monday to Friday, 9am to 7pm ET '
                              '[Dq9KUpYUWsE @ 00:03:03]. ExclusiveLiveCall pushes operators to read every '
                              'payout alongside its trigger, because a $150 qualified-call campaign cannot '
                              'be compared head-to-head with an $800 acquisition campaign [scPdPdSnQWY @ '
                              '00:01:55]. Geography, hours, caps and duplicate windows also decide whether '
                              'a call ever pays. A Dallas caller is simply wasted on a South-Florida-only '
                              'buyer. The shared rule is never to choose a campaign based only on the '
                              'payout.',
                              'The baseline prerequisites are just as uniform. Collect cash before you '
                              'route, track every call yourself, and treat quality as a business line. '
                              'ceohec takes buyer payment upfront on every deal, because buyers whose '
                              'calls do not close have no incentive to pay, and they have been stiffed '
                              'before. The only exception is a massive deal backed by invoice insurance '
                              '[SkS03nygdoY @ 00:01:48]. ExclusiveLiveCall calls post-paid net 7, 15 or 30 '
                              'terms what they really are: extended credit. They start new buyers on '
                              'smaller limits and repeat that revenue on a dashboard is not the same as '
                              'cash in the bank [b7P50zcQzTs @ 00:04:31]. John Ventura says the beginner '
                              'with one affiliate, one buyer and a spreadsheet breaks within about three '
                              'days. The usual break is a fight where the buyer counts 40 qualified calls '
                              'and the affiliate claims 60. Their own AdSync operation still spent six '
                              'figures a year managing Ringba and Retreaver [KeC4mKXnzs4 @ 00:09:02]. '
                              "Ringba's QA masterclass argues that everyone in the chain should run QA, "
                              'because it keeps everyone honest and can become a profit center. It also '
                              'calls affiliates who skip their own call tracking a major mistake, since '
                              'networks are under-resourced and will not catch everything [JxU9bgFTUUs @ '
                              '00:05:01].'],
               'table': {'caption': 'Core consensus rules practitioners apply before sending a single call',
                         'headers': ['Consensus Principle',
                                     'What Operators Actually Do',
                                     'Number or Rule Stated',
                                     'Expert Source'],
                         'rows': [['The payout rate alone never proves a deal is profitable',
                                   'Price every deal on qualified calls instead of raw volume sent',
                                   '80 of 100 calls qualify, leaving $1,200 or a 30% margin',
                                   'TrackDrive ([yYZ5s6jFzQs @ 00:01:43])'],
                                  ['Pay publishers on qualified calls, never on every call sent',
                                   'Confirm the publisher payout trigger before negotiating any rate at '
                                   'all',
                                   'Paying all 100 calls drops margin to $500, or 12.5%',
                                   'TrackDrive ([yYZ5s6jFzQs @ 00:02:04])'],
                                  ['The spread between buyer price and payout is the business',
                                   'Recruit affiliates at a lower rate and resell their calls to buyers',
                                   '$35 affiliate payout against a $50-plus buyer price, a $15 spread',
                                   'John Ventura ([KeC4mKXnzs4 @ 00:02:36])'],
                                  ['Hidden costs quietly erode the gross spread on every call',
                                   'Audit telecom, AI, processing, chargebacks and bad debt line by line',
                                   '$2 saved across 10,000 transactions adds $20,000 to profit',
                                   'ExclusiveLiveCall ([b7P50zcQzTs @ 00:02:32])'],
                                  ['Buyer cash must arrive before any calls are routed to them',
                                   'Take deposits upfront unless a massive deal carries invoice insurance',
                                   'Agent Calls requires $250 minimum; recommended deposit is $500 to '
                                   '1,000',
                                   'ceohec ([SkS03nygdoY @ 00:08:10])'],
                                  ['Own call tracking is mandatory because spreadsheets break almost '
                                   'immediately',
                                   'Install dedicated tracking, routing, recording and QA instead of '
                                   'manual logs',
                                   'Spreadsheet tracking fails within roughly three days; disputes run 40 '
                                   'versus 60',
                                   'John Ventura ([KeC4mKXnzs4 @ 00:09:02])'],
                                  ['QA is a profit center that keeps everyone in the chain honest',
                                   'Put QA clauses at the top of every IO and review them live',
                                   'No one reads terms and conditions, so walk partners through by voice',
                                   'Ringba ([JxU9bgFTUUs @ 00:07:05])']]}},
              {'section_number': 2,
               'title': 'Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ["Marketcall's Alex, VP of Ops, lays out the most complete media playbook on "
                              'the debt settlement offer. It targets adults 30-55 with low but nonzero '
                              'income and over $10K of unsecured debt. Campaigns use a lifetime budget to '
                              'unlock ad scheduling, a 1-10-1 CBO structure, the special credit category '
                              'for cheaper CPMs, and broad targeting. News-style, B-roll voiceover and '
                              'Arcads UGC creatives feed into advertorial quiz pages or chatbots, and UGC '
                              'is currently winning [Dq9KUpYUWsE @ 00:05:12]. The funnel benchmarks are '
                              'explicit. Seven to 10% of clicks hit the call button, and 60-90% of those '
                              'actually dial. Then 25-35% of calls go billable past 90 seconds, and 8-13% '
                              'of billable calls enroll [Dq9KUpYUWsE @ 00:09:49]. Testing budgets run '
                              'about $20-30 per ad set to buy one raw call and $100-150 per billable call. '
                              'Losers are paused after two to three days [Dq9KUpYUWsE @ 00:11:35]. Nate, '
                              "on Yoder, works the same equation from the buyer's side. The pre-dial "
                              'filter is targeting, a qualifying landing-page flow and an urgency CTA. The '
                              'sales pitch is closing math, positioned against $5-20K monthly retainers: a '
                              '$200 CPA goal at $50 per call means one in four calls must close '
                              '[-GEw-hz8tiY @ 00:08:33].',
                              'Cash mechanics are where operators get specific. ceohec usually runs '
                              'publishers on weekly net 7, and some deals run monthly net 3. Terms are '
                              'aligned so wires clear first. A buyer on net 7 means the publisher goes on '
                              'net 10, while a publisher on net 7 against a buyer on net 3 leaves a '
                              'four-day buffer [SkS03nygdoY @ 00:05:31]. Their worked example is $40 times '
                              '10 billable calls for $400, invoiced on Sunday, with funds taking one to '
                              'two days to land in the bank [SkS03nygdoY @ 00:03:51]. ExclusiveLiveCall '
                              'builds prepaid billing as a $1,000 deposit with auto-recharge at a $200 '
                              'balance, tied directly to routing. They warn that a buyer on net 30, while '
                              'publishers are paid every seven days, means you are financing that '
                              'difference [b7P50zcQzTs @ 00:05:41]. Inside Ringba, payouts live under '
                              'Campaigns, Edit, Default Payout Settings, Add. A payout is either a fixed '
                              'amount or a rev-share percentage with limits. A fixed payout can trigger on '
                              'call length, connected, inbound or converted. Operators can optionally pay '
                              'for duplicates within a time limit and set payout hours. Caps cover call '
                              'count and concurrency at global, monthly, daily and hourly levels. Payouts '
                              'are ordered top to bottom for priority, with per-publisher overrides '
                              'available [YWJrO94X-f4 @ 00:00:37].',
                              'Optimization runs on a fixed weekly cadence rather than gut feel. '
                              'TrackDrive reviews four numbers by publisher and sub ID: qualified rate, '
                              'billable rate, revenue per call and margin. Revenue per call is the best '
                              'single figure for comparing sources. Any drop is diagnosed in a fixed order '
                              'of traffic, routing, buyer and pricing, changing one thing at a time. '
                              'Operators raise caps on performers, tighten or pause the rest, and log '
                              "every change [8O9Q1wVmurU @ 00:02:18]. Ringba's QA method for callback "
                              "fraud is mechanical. In this scheme an agent says 'let me call you back' "
                              'and bypasses tracking. The fix is to filter non-converted calls and sort '
                              'under-threshold calls by duration, highest to lowest. Group them by buyer '
                              'and ignore 5-8 second calls. Then hand the network the recording and caller '
                              'ID, and demand a QA addendum carrying a 50% penalty per CPA [JxU9bgFTUUs @ '
                              '00:17:55]. The same session benchmarks automated IVR selection at about '
                              '40%. It treats 50-60% as fine and flags roughly 100% as fraud [JxU9bgFTUUs '
                              '@ 00:40:16]. DigitalTriggers keeps review cheap with a VA who manually '
                              'checks calls averaging about three minutes. The VA skips through at the 30, '
                              '60 and 90 second marks to confirm the caller is in market and in territory '
                              '[1agI5uDKUlQ @ 00:14:33].'],
               'table': {'caption': 'Exact settings, benchmarks and tools operators run in live campaigns',
                         'headers': ['Mechanic',
                                     'Exact Setting or Number',
                                     'How Operators Use It',
                                     'Expert Source'],
                         'rows': [['Debt settlement payout grid by language and duration',
                                   '$55-60 English and $50-55 Spanish over 90s; private offer $20-25 over '
                                   '10s',
                                   'Price media against billable duration across all states except Oregon',
                                   'Marketcall ([Dq9KUpYUWsE @ 00:03:03])'],
                                  ['Facebook ad cost benchmarks for the debt settlement vertical',
                                   'CPM $20-30 Spanish, $40-60 English; CPC under $1.3-1.5; CTR 1.5-2.5%',
                                   'Benchmark every new ad set against these ranges before scaling spend',
                                   'Marketcall ([Dq9KUpYUWsE @ 00:10:33])'],
                                  ['Pixel event mapping for deeper Facebook optimization signals',
                                   'Call click as AddToCart, raw call as Lead, billable call as Contact '
                                   'via CAPI',
                                   'Feed the algorithm billable and enrollment events instead of page '
                                   'views',
                                   'Marketcall ([Dq9KUpYUWsE @ 00:09:10])'],
                                  ['Bidding war between competing buyers on the same call flow',
                                   'Bids climb from 45 to 50 to 55 to 60 dollars per call',
                                   'Play buyers against each other to lift revenue by 20-40% more',
                                   'Yoder ([-GEw-hz8tiY @ 00:13:26])'],
                                  ['Duplicate routing and conditional number display inside the router',
                                   'Repeat callers route to the same buyer; JavaScript shows the number '
                                   'only when a buyer is available',
                                   'Stop wasted calls by hiding the number when no buyer is eligible',
                                   'boberdoo.com ([gOc6yQYGV4s @ 00:01:26])'],
                                  ['AI voice recovery for calls that no buyer will take',
                                   'No upfront fee; $5 charged only per booked appointment synced to '
                                   'Google Calendar',
                                   'Monetize missed and unsold calls instead of letting them die unpaid',
                                   'ExclusiveLiveCall ([b7P50zcQzTs @ 00:09:22])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Street-Level Edges That Widen the Spread',
                           'body': 'These are the small operator moves practitioners credit with finding '
                                   'buyers, closing deals and squeezing extra revenue out of traffic '
                                   'already paid for.',
                           'items': ['Listen to call greetings to identify who the real end buyer is, then '
                                     'pitch that buyer directly [John Ventura — x3UYaJjRdx0 @ 00:05:57].',
                                     'Sell buyers a $2-5k test that reads out within 24-48 hours, set '
                                     'against a $15k/month agency retainer locked for 90 days [John '
                                     'Ventura — x3UYaJjRdx0 @ 00:01:26].',
                                     'Build exit pages for disqualified traffic, which add 5-10% revenue '
                                     'on clicks you already paid for [Marketcall — Dq9KUpYUWsE @ '
                                     '00:14:48].',
                                     "Open disputes with dated specifics such as 'between the third and "
                                     "the seventh...' rather than 'your traffic is bad' [TrackDrive — "
                                     'y8V08rKKNWY @ 00:04:31].']},
               'sop_steps': [{'step': 1,
                              'title': 'Lock the Vertical, Buyers and Billable Event',
                              'action': 'Pick one vertical that can justify about $50 per call, sign '
                                        'buyers before recruiting traffic, and write down the exact '
                                        'billable trigger.',
                              'detail': 'Choose buyers first and only enter verticals that justify '
                                        '$50/call [John Ventura — KeC4mKXnzs4 @ 00:09:37]; read every '
                                        'payout alongside its billable event so a $150 qualified call is '
                                        'never confused with an $800 acquisition [ExclusiveLiveCall — '
                                        'scPdPdSnQWY @ 00:01:55].'},
                             {'step': 2,
                              'title': 'Collect Deposits and Align Net Terms',
                              'action': 'Take buyer money upfront, then set publisher terms longer than '
                                        'buyer terms so wires clear before payouts go out.',
                              'detail': 'Put the publisher on net 10 when the buyer is on net 7, or run '
                                        'publisher net 7 against buyer net 3 for a four-day buffer [ceohec '
                                        '— SkS03nygdoY @ 00:05:31]; use a $1,000 prepaid deposit with '
                                        'auto-recharge at $200 tied to routing [ExclusiveLiveCall — '
                                        'b7P50zcQzTs @ 00:03:15].'},
                             {'step': 3,
                              'title': 'Configure Payouts, Caps and Routing in the Tracker',
                              'action': 'Build payout rules, duplicate handling, hours and caps inside the '
                                        'call platform instead of a spreadsheet.',
                              'detail': 'Set fixed or rev-share payouts, payout hours, and global, '
                                        'monthly, daily and hourly caps on count and concurrency, ordered '
                                        'top to bottom for priority [Ringba — YWJrO94X-f4 @ 00:01:05]; '
                                        'overflow to buyers B and C once a 20/day cap on buyer A fills '
                                        '[ExclusiveLiveCall — scPdPdSnQWY @ 00:06:58].'},
                             {'step': 4,
                              'title': 'Start Small, Review Weekly, Scale on Proof',
                              'action': 'Launch with limited traffic, review the four core metrics weekly, '
                                        'and only raise caps once the numbers hold.',
                              'detail': 'Review qualified rate, billable rate, revenue per call and margin '
                                        'by publisher and sub ID, then raise caps on performers and pause '
                                        'the rest [TrackDrive — 8O9Q1wVmurU @ 00:02:57]; scale only at a '
                                        '50%-plus billable rate with positive post-reconciliation margin '
                                        'and clean QA [John Ventura — KeC4mKXnzs4 @ 00:11:09].'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The sharpest split is over what a billable call even is. Nate on Yoder runs '
                              'a 90-second threshold and tells buyers to hang up before 90 seconds or get '
                              'charged, adding that some buyers need 120 seconds instead [-GEw-hz8tiY @ '
                              '00:06:29]. DigitalTriggers attacks that network model head-on: networks pay '
                              'only on calls past 90 seconds, after treating callers through IVRs where '
                              'each keypress loses about 20% of callers, and only for in-network zips, and '
                              'leading a pitch with duration creates an adversarial conversation with '
                              'local businesses [1agI5uDKUlQ @ 00:01:58]. The DigitalTriggers direct-sale '
                              'criteria run in strict order: the caller is in market with no '
                              'cherry-picking, in territory by county as verified by listening, over 30 '
                              'seconds, and voicemail is billable because home services miss 20 to 30% of '
                              'calls and some clients miss 10 to 15 per day worth $90 to $400 each '
                              '[1agI5uDKUlQ @ 00:11:57]. ExclusiveLiveCall lands between the camps, '
                              'arguing duration is imperfect because a 70-second call can be legitimate '
                              'while a 4-minute call is not, and routing that judgment to AI Verdict, '
                              'which scores calls on conversation content instead of the clock '
                              '[scPdPdSnQWY @ 00:06:04]. Pick the definition in writing before you pick '
                              'the buyer.',
                              'The second fight is rate versus quality, and the practitioners who buy '
                              'calls refuse to buy on price. Nate argues a $10-per-call vendor that needs '
                              '20 calls to produce one sale angers agents, while a $50-per-call vendor '
                              'converting 1 in 3 or 4 is the better buy; the math is that a $200 CPA at '
                              '$50 per call means 1 in 4 calls must close [-GEw-hz8tiY @ 00:10:00]. '
                              'TrackDrive frames the same trap from the seller side: a great rate with '
                              'strict rules can earn less than a modest rate with fair ones, so the rate '
                              'alone never tells you whether a deal is profitable [yYZ5s6jFzQs @ '
                              '00:03:06]. ExclusiveLiveCall agrees and pushes it further, telling '
                              'operators never to choose a campaign based only on the payout and to read '
                              'every payout alongside its billable event, because a $150 qualified-call '
                              'campaign cannot be compared directly with an $800 acquisition campaign '
                              '[scPdPdSnQWY @ 00:01:55]. John Ventura is the counterweight, running a pure '
                              'spread model where affiliates accept $35 and buyers pay $50 or more for a '
                              '$15 margin, scaling that to $7,500 a day at 500 calls and pitching it as '
                              'straight profit on every single call [KeC4mKXnzs4 @ 00:02:36]. Spread '
                              'operators chase volume; quality buyers chase close rate.',
                              'Cash terms and buyer sourcing split the room again. ceohec runs weekly net '
                              '7 with some monthly net 3 deals and insists on taking buyer payment '
                              "upfront, because buyers who don't close aren't incentivized to pay; the "
                              'only exception is a massive deal backed by invoice insurance [SkS03nygdoY @ '
                              '00:01:48]. ExclusiveLiveCall accepts post-paid net 7, 15, or 30 terms but '
                              'calls them extending credit, starts new buyers on smaller limits, and '
                              'models prepaid as a $1,000 deposit that auto-recharges at a $200 balance '
                              'tied to routing [b7P50zcQzTs @ 00:04:31]. On sourcing, John Ventura says '
                              'finding buyers was the hardest part of the first 3 to 6 months, so '
                              'beginners should start with a network or aggregator, then listen to call '
                              'greetings to identify end buyers and pitch them directly [x3UYaJjRdx0 @ '
                              '00:05:57]. DigitalTriggers flips the hierarchy and sells to networks only '
                              'when no direct buyer exists, since a network might pay $12 where a direct '
                              'sale gets $90, roughly 6 to 15 times more per call; direct buyers get won '
                              'with a PPC ad-spend test or a 30-day test instead of a duration debate '
                              '[1agI5uDKUlQ @ 00:13:51]. Network loyalists stay put for reliable pay; '
                              'direct sellers chase the multiple.'],
               'table': {'caption': 'Competing playbooks on billability, pricing, cash terms, sourcing, '
                                    'and QA posture',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Where the billable line sits on duration',
                                   'Network-style 90-second threshold, with some buyers demanding 120 '
                                   'seconds before billing',
                                   'Direct-sale criteria: in market, in territory, over 30 seconds, '
                                   'voicemail billable',
                                   'Yoder ([-GEw-hz8tiY @ 00:09:36]); DigitalTriggers ([1agI5uDKUlQ @ '
                                   '00:11:11])'],
                                  ['How call quality gets judged and billed',
                                   'Billable once the call passes the buffer time of 90, 120, 10, or 25 '
                                   'seconds',
                                   'AI Verdict judges conversation content because a 70-second call can be '
                                   'legitimate',
                                   'ceohec ([SkS03nygdoY @ 00:03:31]); ExclusiveLiveCall ([scPdPdSnQWY @ '
                                   '00:06:04])'],
                                  ['Choosing an offer by its payout headline',
                                   'Chasing headline payouts like roofing at $300 or water damage at '
                                   '$1,000',
                                   'A modest rate with fair rules can out-earn a great rate with strict '
                                   'ones',
                                   'ExclusiveLiveCall ([scPdPdSnQWY @ 00:00:00]); TrackDrive ([yYZ5s6jFzQs '
                                   '@ 00:03:06])'],
                                  ['How buyers pay for the calls they take',
                                   'Always collect buyer payment upfront, with invoice insurance only for '
                                   'massive deals',
                                   'Post-paid net 7, 15, or 30 treated as credit with small starting '
                                   'limits',
                                   'ceohec ([SkS03nygdoY @ 00:02:14]); ExclusiveLiveCall ([b7P50zcQzTs @ '
                                   '00:04:31])'],
                                  ['Where a new operator sources call buyers',
                                   'Start with a network or aggregator, then pitch end buyers heard in '
                                   'call greetings',
                                   'Sell direct first and route to networks only when no direct buyer '
                                   'exists',
                                   'John Ventura ([x3UYaJjRdx0 @ 00:05:45]); DigitalTriggers ([1agI5uDKUlQ '
                                   '@ 00:13:51])'],
                                  ['Default posture when bad calls show up',
                                   'Assume stupidity, not malice, because call centers hire the cheapest '
                                   'labor available',
                                   'Classify each dispute as honest mistake, careless practice, or '
                                   'deliberate violation, then document',
                                   'Ringba ([JxU9bgFTUUs @ 00:03:18]); TrackDrive ([y8V08rKKNWY @ '
                                   '00:03:16])'],
                                  ['What to do with calls nobody answers',
                                   'Bill voicemail because home services miss 20 to 30% of their calls',
                                   'Recover unclaimed calls with AI voice at $5 only per booked '
                                   'appointment',
                                   'DigitalTriggers ([1agI5uDKUlQ @ 00:11:57]); ExclusiveLiveCall '
                                   '([b7P50zcQzTs @ 00:09:22])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The most expensive failures are paper failures. TrackDrive shows the math: '
                              'send 100 calls, qualify 80, bill the buyer $50 and pay the publisher $35, '
                              'and margin is $1,200 or 30%; pay the publisher on all 100 calls instead and '
                              'payout jumps to $3,500 while margin collapses to $500, or 12.5%, which is '
                              'why rejected calls come straight out of margin and you price on 80, not '
                              '100, even though TrackDrive warns its example numbers are totally made up '
                              '[yYZ5s6jFzQs @ 00:02:04]. Nate reports losing hundreds of thousands of '
                              'dollars to agreements that were unsigned or misread [-GEw-hz8tiY @ '
                              '00:22:43]. ceohec has been stiffed by buyers who never closed and therefore '
                              'felt no incentive to pay, hence the upfront payment rule, the $500 to '
                              '$1,000 minimum deposit advice, and publishers on net 10 whenever the buyer '
                              'sits on net 7 so wires clear first [SkS03nygdoY @ 00:05:31]. '
                              'ExclusiveLiveCall names the same working-capital gap: a buyer on net 30 '
                              'while publishers get paid every 7 days means you are financing that '
                              'difference, and revenue on a dashboard is not the same as cash in the bank '
                              '[b7P50zcQzTs @ 00:05:41]. Collectible revenue, not booked revenue, is the '
                              'only scoreboard that pays rent.',
                              'Fraud shows up as patterns, and the Ringba masterclass maps the ugliest '
                              'one: callback fraud, where the agent says let me call you back and the '
                              'conversion escapes tracking entirely. The real example was a braces caller '
                              'on a 40-second call with about 35 seconds of talk time against a 1:30 '
                              'conversion threshold, and smaller buyers running 10 to 30 agents are '
                              'likelier to pull it [JxU9bgFTUUs @ 00:14:42]. Detection is mechanical: '
                              'filter non-converted calls, sort by duration highest to lowest under the '
                              'threshold, group by buyer, ignore 5-to-8-second calls, then hand the '
                              'network the recording and caller ID and demand a QA addendum carrying a 50% '
                              'penalty per CPA [JxU9bgFTUUs @ 00:20:34]. The same speaker flags automated '
                              'IVR selection: around 40% is the benchmark, 50 to 60% is fine, and roughly '
                              "100% is fraud [JxU9bgFTUUs @ 00:40:16]. TrackDrive's warning list covers "
                              'the traffic side: the same number calling 20 times a day, many calls ending '
                              'at 58 or 59 seconds against a 60-second minimum, out-of-state or off-hours '
                              'calls, a sudden spike from one sub ID, and pre-recorded audio, with the '
                              'rule that a pattern proves a problem while a single sign does not '
                              '[y8V08rKKNWY @ 00:01:21]. Read the pattern, then pull the recording.',
                              'Scaling breaks operators who skip infrastructure. John Ventura says most '
                              'beginners find one affiliate and one buyer, track everything in a '
                              'spreadsheet, and watch it fail within about three days, ending in the '
                              'classic dispute where the buyer counts 40 qualified calls and the affiliate '
                              'claims 60; even at scale, AdSync spent six figures a year just managing '
                              'Ringba and Retreaver [KeC4mKXnzs4 @ 00:09:02]. The Ventura scaling gate is '
                              'a billable rate of at least 50%, positive post-reconciliation margins, and '
                              'clean QA, with an explicit warning against adding 10 affiliates at once '
                              '[KeC4mKXnzs4 @ 00:11:09]. Andy on Beginner to 1K a Day Journey blames dips '
                              'on Google Ads updates and reports that legal tests on Facebook, Instagram, '
                              'and Google spent more than they earned, while Market Call has no legal '
                              'vertical at all [Cea6GBkjsgg @ 00:03:33]. Buyer capacity is the hidden '
                              'ceiling: ExclusiveLiveCall warns a buyer taking 50 calls a day may have '
                              'only 2 agents, so concurrency limits matter as much as daily caps, and the '
                              'fix is routing to buyers B and C once buyer A fills a 20-per-day cap '
                              '[scPdPdSnQWY @ 00:07:33]. Start small, reconcile weekly, and add affiliates '
                              'one at a time until the numbers hold.'],
               'table': {'caption': 'Firsthand losses, fraud patterns, and the checks practitioners run '
                                    'against them',
                         'headers': ['Failure Mode',
                                     'What Happened Or Was Measured',
                                     'Operator Check',
                                     'Expert Source'],
                         'rows': [['Paying publishers on every call sent',
                                   'Margin fell from $1,200 at 30% to $500 at 12.5% on 100 calls',
                                   'Confirm payout triggers on qualified calls only and price on 80, not '
                                   '100',
                                   'TrackDrive ([yYZ5s6jFzQs @ 00:02:27])'],
                                  ['Unsigned or misread buyer and publisher agreements',
                                   'Hundreds of thousands of dollars lost to unsigned or misread '
                                   'agreements',
                                   'Put QA clauses at the top of IOs and review them by voice or chat',
                                   'Yoder ([-GEw-hz8tiY @ 00:22:43]); Ringba ([JxU9bgFTUUs @ 00:07:05])'],
                                  ['Buyers who stop paying after weak closes',
                                   'Stiffed by buyers who did not close and had no incentive to pay',
                                   'Take payment upfront and require a $500 to $1,000 minimum deposit',
                                   'ceohec ([SkS03nygdoY @ 00:01:48]); ceohec ([SkS03nygdoY @ 00:08:10])'],
                                  ['Mismatched buyer and publisher payment terms',
                                   'Buyer on net 30 while publishers get paid every 7 days creates a '
                                   'financing gap',
                                   'Put publishers on net 10 when the buyer is on net 7 so wires clear',
                                   'ExclusiveLiveCall ([b7P50zcQzTs @ 00:05:41]); ceohec ([SkS03nygdoY @ '
                                   '00:05:31])'],
                                  ['Callback fraud by smaller buyer call centers',
                                   'A 40-second braces call with about 35 seconds of talk against a 1:30 '
                                   'conversion',
                                   'Sort non-converted calls by duration under threshold, group by buyer, '
                                   'enforce 50% penalty',
                                   'Ringba ([JxU9bgFTUUs @ 00:14:42])'],
                                  ['Manual spreadsheet tracking between one affiliate and one buyer',
                                   'Breaks within about three days; buyer counts 40 qualified while the '
                                   'affiliate claims 60',
                                   'Set up tracking, routing, recording, and QA before adding any second '
                                   'affiliate',
                                   'John Ventura ([KeC4mKXnzs4 @ 00:09:02])'],
                                  ['Buyer agents cherry-picking the calls they keep',
                                   'Agent hang-ups running 30% above the rate seen at other buyers',
                                   'No penalty on first offense, then $500, and $100 per call for removed '
                                   'agents',
                                   'Ringba ([JxU9bgFTUUs @ 01:02:54]); Ringba ([JxU9bgFTUUs @ '
                                   '01:05:06])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Do Not Scale Until These Four Clear',
                           'body': 'Each gate below traces back to a loss, a dispute, or a fraud pattern a '
                                   'practitioner reported firsthand. Clear all four before raising caps or '
                                   'onboarding more affiliates.',
                           'items': ['Billable rate at or above 50%, positive post-reconciliation margins, '
                                     'and clean QA before adding affiliates, and never 10 at once [John '
                                     'Ventura — KeC4mKXnzs4 @ 00:11:09].',
                                     'Buyer payment collected upfront with a $500 to $1,000 minimum '
                                     'deposit, with invoice insurance reserved for massive deals [ceohec — '
                                     'SkS03nygdoY @ 00:08:10].',
                                     'QA addendum signed with a 50% penalty per CPA for callback fraud, '
                                     'plus a signed affiliate one-pager [Ringba — JxU9bgFTUUs @ 00:20:34].',
                                     'When 15 of 100 calls are disputed, find out why, because a buyer '
                                     'failing to close is not an invalid call [ExclusiveLiveCall — '
                                     'b7P50zcQzTs @ 00:07:01].']}}],
 'pull_quote': '"The rate alone never tells you if a deal is profitable." — TrackDrive (yYZ5s6jFzQs @ '
               '00:02:27)',
 'diagram_id': 'diag-08',
 'action_checklist': ['Review qualified rate, billable rate, revenue per call, and margin weekly by '
                      'publisher and sub ID, raise caps on performers, tighten or pause the rest, and log '
                      'every change [TrackDrive — 8O9Q1wVmurU @ 00:02:57].',
                      'Diagnose any drop in fixed order of traffic, routing, buyer, then pricing, and '
                      'change one thing at a time [TrackDrive — 8O9Q1wVmurU @ 00:02:18].',
                      'Map pixel events so call click fires AddToCart, raw call fires Lead, billable call '
                      'over 90 seconds fires Contact via CAPI, and enrollment fires Purchase [Marketcall — '
                      'Dq9KUpYUWsE @ 00:09:10].',
                      'Add exit pages for disqualified traffic to pick up 5 to 10% more revenue '
                      '[Marketcall — Dq9KUpYUWsE @ 00:14:48].',
                      'Build Ringba payouts as fixed or rev-share with triggers, caps, and duplicate '
                      'windows, then order them top-to-bottom for priority and add per-publisher overrides '
                      '[Ringba — YWJrO94X-f4 @ 00:02:00].',
                      'Switch on per-partner call center verification in boberdoo, select it in the '
                      'partner filter set, and approve or decline pending leads with the green headset '
                      'icon [boberdoo.com — gUYjvbnA54I @ 00:00:56].'],
 'statutory_citations': [{'title': 'Ringba — Pay Per Call Masterclass - Quality Assurance [00:20:34]',
                          'url': 'https://www.youtube.com/watch?v=JxU9bgFTUUs&t=1234s',
                          'relevance': 'Primary practitioner testimony on callback fraud detection, QA '
                                       'addendums, and the 50% penalty per CPA.'},
                         {'title': 'ExclusiveLiveCall — How the Money Works in Pay Per Call | Billing, '
                                   'Payouts, Margins & Profit- Pay Per Call University #8 [00:05:41]',
                          'url': 'https://www.youtube.com/watch?v=b7P50zcQzTs&t=341s',
                          'relevance': 'Primary practitioner testimony on post-paid credit risk and the '
                                       'net 30 versus 7-day working-capital gap.'},
                         {'title': 'TrackDrive — The Economics of a Call | Pay-Per-Call Masterclass '
                                   '[00:02:04]',
                          'url': 'https://www.youtube.com/watch?v=yYZ5s6jFzQs&t=124s',
                          'relevance': 'Primary practitioner testimony on margin collapse when publishers '
                                       'are paid on all calls instead of qualified calls.'},
                         {'title': 'John Ventura — My Pay Per Call Biz is Boring, But it Makes Me '
                                   '$10M/year [00:09:02]',
                          'url': 'https://www.youtube.com/watch?v=KeC4mKXnzs4&t=542s',
                          'relevance': 'Primary practitioner testimony on spreadsheet tracking failure, '
                                       'reconciliation disputes, and scaling gates.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'yYZ5s6jFzQs',
                       'title': 'The Economics of a Call | Pay-Per-Call Masterclass',
                       'channel': 'TrackDrive',
                       'author': 'TrackDrive',
                       'text': 'The rate alone never tells you if a deal is profitable.',
                       'tip': 'The rate alone never tells you if a deal is profitable.',
                       'timestamp': 147,
                       'timestamp_seconds': 147,
                       'timestamp_label': '[00:02:27]',
                       'url': 'https://www.youtube.com/watch?v=yYZ5s6jFzQs&t=147s',
                       'markdown': '[00:02:27](https://www.youtube.com/watch?v=yYZ5s6jFzQs&t=147s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'yYZ5s6jFzQs',
                       'title': 'The Economics of a Call | Pay-Per-Call Masterclass',
                       'channel': 'TrackDrive',
                       'author': 'TrackDrive',
                       'text': 'Know your margin before you negotiate a payout.',
                       'tip': 'Know your margin before you negotiate a payout.',
                       'timestamp': 20,
                       'timestamp_seconds': 20,
                       'timestamp_label': '[00:00:20]',
                       'url': 'https://www.youtube.com/watch?v=yYZ5s6jFzQs&t=20s',
                       'markdown': '[00:00:20](https://www.youtube.com/watch?v=yYZ5s6jFzQs&t=20s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '8O9Q1wVmurU',
                       'title': 'Optimizing and Reporting | Pay-Per-Call Masterclass',
                       'channel': 'TrackDrive',
                       'author': 'TrackDrive',
                       'text': "It's tempting to jump to conclusions, so I suggest checking in a fixed "
                               'order.',
                       'tip': "It's tempting to jump to conclusions, so I suggest checking in a fixed "
                              'order.',
                       'timestamp': 138,
                       'timestamp_seconds': 138,
                       'timestamp_label': '[00:02:18]',
                       'url': 'https://www.youtube.com/watch?v=8O9Q1wVmurU&t=138s',
                       'markdown': '[00:02:18](https://www.youtube.com/watch?v=8O9Q1wVmurU&t=138s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'y8V08rKKNWY',
                       'title': 'Call Quality and Fraud Control | Pay-Per-Call Masterclass',
                       'channel': 'TrackDrive',
                       'author': 'TrackDrive',
                       'text': 'A genuine customer might call back once or twice.',
                       'tip': 'A genuine customer might call back once or twice.',
                       'timestamp': 60,
                       'timestamp_seconds': 60,
                       'timestamp_label': '[00:01:00]',
                       'url': 'https://www.youtube.com/watch?v=y8V08rKKNWY&t=60s',
                       'markdown': '[00:01:00](https://www.youtube.com/watch?v=y8V08rKKNWY&t=60s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '-GEw-hz8tiY',
                       'title': 'This 26 Year Old Marketer Generated Over $15,000,000 Selling Phonecalls - '
                                '30 Min Pay Per Call Guide',
                       'channel': 'Yoder',
                       'author': 'Yoder',
                       'text': 'Hang the damn phone up before 90 seconds, or you get charged for the call.',
                       'tip': 'Hang the damn phone up before 90 seconds, or you get charged for the call.',
                       'timestamp': 389,
                       'timestamp_seconds': 389,
                       'timestamp_label': '[00:06:29]',
                       'url': 'https://www.youtube.com/watch?v=-GEw-hz8tiY&t=389s',
                       'markdown': '[00:06:29](https://www.youtube.com/watch?v=-GEw-hz8tiY&t=389s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Cea6GBkjsgg',
                       'title': 'I Built a $1,000/Day Pay Per Call Business — Here’s What’s Next',
                       'channel': 'Beginner to 1K a Day Journey',
                       'author': 'Beginner to 1K a Day Journey',
                       'text': 'My account manager offered to raise my cap from 26 to 30 calls if I '
                               'consistently deliver 30 qualified calls a day.',
                       'tip': 'My account manager offered to raise my cap from 26 to 30 calls if I '
                              'consistently deliver 30 qualified calls a day.',
                       'timestamp': 41,
                       'timestamp_seconds': 41,
                       'timestamp_label': '[00:00:41]',
                       'url': 'https://www.youtube.com/watch?v=Cea6GBkjsgg&t=41s',
                       'markdown': '[00:00:41](https://www.youtube.com/watch?v=Cea6GBkjsgg&t=41s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Dq9KUpYUWsE',
                       'title': 'Debt Settlement $400k Pay Per Call Case Study 2025',
                       'channel': 'Marketcall',
                       'author': 'Marketcall',
                       'text': 'So using a call tracker is a must when running pay per call campaigns.',
                       'tip': 'So using a call tracker is a must when running pay per call campaigns.',
                       'timestamp': 794,
                       'timestamp_seconds': 794,
                       'timestamp_label': '[00:13:14]',
                       'url': 'https://www.youtube.com/watch?v=Dq9KUpYUWsE&t=794s',
                       'markdown': '[00:13:14](https://www.youtube.com/watch?v=Dq9KUpYUWsE&t=794s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'SkS03nygdoY',
                       'title': 'How I Pay Publishers in Pay Per Call (net terms)',
                       'channel': 'ceohec',
                       'author': 'ceohec',
                       'text': 'And so, always get your payments up front.',
                       'tip': 'And so, always get your payments up front.',
                       'timestamp': 91,
                       'timestamp_seconds': 91,
                       'timestamp_label': '[00:01:31]',
                       'url': 'https://www.youtube.com/watch?v=SkS03nygdoY&t=91s',
                       'markdown': '[00:01:31](https://www.youtube.com/watch?v=SkS03nygdoY&t=91s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'scPdPdSnQWY',
                       'title': 'How to Read a Pay Per Call Campaign Before You Send Traffic | Pay Per '
                                'Call University #6',
                       'channel': 'ExclusiveLiveCall',
                       'author': 'ExclusiveLiveCall',
                       'text': 'Never choose a campaign based only on the payout.',
                       'tip': 'Never choose a campaign based only on the payout.',
                       'timestamp': 734,
                       'timestamp_seconds': 734,
                       'timestamp_label': '[00:12:14]',
                       'url': 'https://www.youtube.com/watch?v=scPdPdSnQWY&t=734s',
                       'markdown': '[00:12:14](https://www.youtube.com/watch?v=scPdPdSnQWY&t=734s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'YWJrO94X-f4',
                       'title': 'Payouts | Ringba Platform Training',
                       'channel': 'Ringba',
                       'author': 'Ringba',
                       'text': 'Fixed payouts can trigger on call length, connected, inbound, or converted '
                               'calls.',
                       'tip': 'Fixed payouts can trigger on call length, connected, inbound, or converted '
                              'calls.',
                       'timestamp': 37,
                       'timestamp_seconds': 37,
                       'timestamp_label': '[00:00:37]',
                       'url': 'https://www.youtube.com/watch?v=YWJrO94X-f4&t=37s',
                       'markdown': '[00:00:37](https://www.youtube.com/watch?v=YWJrO94X-f4&t=37s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'JxU9bgFTUUs',
                       'title': 'Pay Per Call Masterclass - Quality Assurance',
                       'channel': 'Ringba',
                       'author': 'Ringba',
                       'text': 'You should do it in a hundred percent of the cases and then escalate if it '
                               'continues.',
                       'tip': 'You should do it in a hundred percent of the cases and then escalate if it '
                              'continues.',
                       'timestamp': 1288,
                       'timestamp_seconds': 1288,
                       'timestamp_label': '[00:21:28]',
                       'url': 'https://www.youtube.com/watch?v=JxU9bgFTUUs&t=1288s',
                       'markdown': '[00:21:28](https://www.youtube.com/watch?v=JxU9bgFTUUs&t=1288s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'KeC4mKXnzs4',
                       'title': 'My Pay Per Call Biz is Boring, But it Makes Me $10M/year',
                       'channel': 'John Ventura',
                       'author': 'John Ventura',
                       'text': 'They find one affiliate, they find one buyer, and they try to manually '
                               'track everything in a spreadsheet.',
                       'tip': 'They find one affiliate, they find one buyer, and they try to manually '
                              'track everything in a spreadsheet.',
                       'timestamp': 542,
                       'timestamp_seconds': 542,
                       'timestamp_label': '[00:09:02]',
                       'url': 'https://www.youtube.com/watch?v=KeC4mKXnzs4&t=542s',
                       'markdown': '[00:09:02](https://www.youtube.com/watch?v=KeC4mKXnzs4&t=542s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'x3UYaJjRdx0',
                       'title': 'I make $1M/mo with Pay Per Call (just copy me)',
                       'channel': 'John Ventura',
                       'author': 'John Ventura',
                       'text': 'Listen to the call greetings to identify the end buyers, then pitch them '
                               'directly.',
                       'tip': 'Listen to the call greetings to identify the end buyers, then pitch them '
                              'directly.',
                       'timestamp': 357,
                       'timestamp_seconds': 357,
                       'timestamp_label': '[00:05:57]',
                       'url': 'https://www.youtube.com/watch?v=x3UYaJjRdx0&t=357s',
                       'markdown': '[00:05:57](https://www.youtube.com/watch?v=x3UYaJjRdx0&t=357s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'gOc6yQYGV4s',
                       'title': 'Call Routing Solutions | boberdoo Call/Phone Routing System',
                       'channel': 'boberdoo.com',
                       'author': 'boberdoo.com',
                       'text': 'The JavaScript number display shows the number only when a buyer is '
                               'available.',
                       'tip': 'The JavaScript number display shows the number only when a buyer is '
                              'available.',
                       'timestamp': 86,
                       'timestamp_seconds': 86,
                       'timestamp_label': '[00:01:26]',
                       'url': 'https://www.youtube.com/watch?v=gOc6yQYGV4s&t=86s',
                       'markdown': '[00:01:26](https://www.youtube.com/watch?v=gOc6yQYGV4s&t=86s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'b7P50zcQzTs',
                       'title': 'How the Money Works in Pay Per Call | Billing, Payouts, Margins & Profit- '
                                'Pay Per Call University #8',
                       'channel': 'ExclusiveLiveCall',
                       'author': 'ExclusiveLiveCall',
                       'text': 'Revenue is not profit.',
                       'tip': 'Revenue is not profit.',
                       'timestamp': 70,
                       'timestamp_seconds': 70,
                       'timestamp_label': '[00:01:10]',
                       'url': 'https://www.youtube.com/watch?v=b7P50zcQzTs&t=70s',
                       'markdown': '[00:01:10](https://www.youtube.com/watch?v=b7P50zcQzTs&t=70s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'b7P50zcQzTs',
                       'title': 'How the Money Works in Pay Per Call | Billing, Payouts, Margins & Profit- '
                                'Pay Per Call University #8',
                       'channel': 'ExclusiveLiveCall',
                       'author': 'ExclusiveLiveCall',
                       'text': 'Profitable, collectible revenue is the goal.',
                       'tip': 'Profitable, collectible revenue is the goal.',
                       'timestamp': 771,
                       'timestamp_seconds': 771,
                       'timestamp_label': '[00:12:51]',
                       'url': 'https://www.youtube.com/watch?v=b7P50zcQzTs&t=771s',
                       'markdown': '[00:12:51](https://www.youtube.com/watch?v=b7P50zcQzTs&t=771s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '1agI5uDKUlQ',
                       'title': 'With Pay Per Call What Makes a Call Billable?',
                       'channel': 'DigitalTriggers',
                       'author': 'DigitalTriggers',
                       'text': 'Each IVR keypress loses about 20% of callers.',
                       'tip': 'Each IVR keypress loses about 20% of callers.',
                       'timestamp': 118,
                       'timestamp_seconds': 118,
                       'timestamp_label': '[00:01:58]',
                       'url': 'https://www.youtube.com/watch?v=1agI5uDKUlQ&t=118s',
                       'markdown': '[00:01:58](https://www.youtube.com/watch?v=1agI5uDKUlQ&t=118s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'gUYjvbnA54I',
                       'title': 'Enable Call Center Lead Verification | boberdoo Call Routing Software',
                       'channel': 'boberdoo.com',
                       'author': 'boberdoo.com',
                       'text': 'Pending leads show a red check mark, and you click the green headset icon '
                               'to approve or decline.',
                       'tip': 'Pending leads show a red check mark, and you click the green headset icon '
                              'to approve or decline.',
                       'timestamp': 56,
                       'timestamp_seconds': 56,
                       'timestamp_label': '[00:00:56]',
                       'url': 'https://www.youtube.com/watch?v=gUYjvbnA54I&t=56s',
                       'markdown': '[00:00:56](https://www.youtube.com/watch?v=gUYjvbnA54I&t=56s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'}]}
