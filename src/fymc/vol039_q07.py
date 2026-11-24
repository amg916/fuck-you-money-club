from __future__ import annotations

CHAPTER_7 = {'id': 'Q7',
 'chapter_id': 'Q7',
 'chapter_number': 7,
 'question_number': 7,
 'slug': 'generating-inbound-calls-google-meta-ads',
 'question_prompt': 'Which paid and owned traffic sources generate consumer-initiated inbound calls, and '
                    'how do I set them up?',
 'kicker': 'Q7 / THE BIG MONEY PLAYBOOKS',
 'title': 'Generating Inbound Calls with Google and Meta Ads',
 'subtitle': 'Google call-only campaigns and their 2026 phase-out, call assets, clicks-without-calls '
             'fixes, Google Ads best practices, local call-only industry selection, flight-booking '
             'campaigns, Facebook and quiz ads, health insurance on Facebook, low-budget Meta scaling, and '
             'paid/organic/owned traffic',
 'layout_template': 'thirty_day_roadmap',
 'reading_time_minutes': 15,
 'executive_summary': 'Pay-per-call operators running Google and Meta agree the scoreboard is the billable '
                      'call, not the click or the lead. Search intent drives the cleanest calls: long-tail '
                      'local keywords, exact and phrase match, aggressive negatives, and plain Search '
                      'campaigns over Performance Max and Smart. With new call-only ads blocked from '
                      'February 2026, Google builds now pair responsive search ads with call assets, '
                      'minus-100-percent desktop and tablet bids, and tap-to-call mobile pages, counting '
                      'calls over 15 seconds as conversions. On Meta, operators use call-now buttons, '
                      'Reach campaigns, or lead-to-call flows at $8 to $15 per call and $20 to $25 per '
                      'billable call. Answer speed decides revenue: 31 percent conversion inside 30 '
                      'seconds versus 4 percent after five minutes. Brokers live on $3 to $10 spreads. The '
                      'split is channel choice: Google for intent versus Meta for cheaper, riskier volume.',
 'key_metrics': [{'label': 'Cost Per Call By Channel',
                  'metric': 'Cost Per Call By Channel',
                  'value': 'Google $50-150; Facebook/Instagram $15-40; YouTube/TikTok/Outbrain $25-60',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Ventura's per-call cost ranges by traffic source, with Facebook and "
                             'Instagram creative refreshed every 2-3 weeks to hold the lower range.',
                  'source': 'John Ventura ([GV0ML_xytX8 @ 00:04:04])'},
                 {'label': 'Answer Speed Conversion Rate',
                  'metric': 'Answer Speed Conversion Rate',
                  'value': '31% when answered within 30 seconds; 4% after 5 minutes',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Research Ventura cites on inbound call pickup, alongside the claim that 80% '
                             'of callers will not leave a voicemail.',
                  'source': 'John Ventura ([GV0ML_xytX8 @ 00:07:43])'},
                 {'label': 'Facebook Health Insurance Cost Per Billable Call',
                  'metric': 'Facebook Health Insurance Cost Per Billable Call',
                  'value': '$8-15 per call; $20-25 per billable call; 40-70% billable rate',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Marketcall's benchmark for health insurance pay-per-call on Facebook, with "
                             'CPM about $10, CTR 1-1.5% and ROI of 20-50%.',
                  'source': 'Marketcall ([9msaK2zlGMI @ 00:29:13])'},
                 {'label': 'Brokering Margin At Scale',
                  'metric': 'Brokering Margin At Scale',
                  'value': '$10 margin x 2,000 calls/day = $20,000/day',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Ancelet's brokering math: 50 calls a day at $10 margin is $500 profit, "
                             'scaling to $20,000 at 2,000 calls, starting from a $3-5 margin.',
                  'source': 'Nate Ancelet ([q4tpqSo7KCE @ 00:10:09])'}],
 'sections': [{'section_number': 1,
               'title': 'The Practitioner Consensus',
               'paragraphs': ['Every serious operator on this roster measures the call that pays, not the '
                              'click or the raw ring. John Ventura frames the core metric as cost per '
                              'enrolled customer rather than cost per lead [GV0ML_xytX8 @ 00:00:31], and '
                              "flips the usual logic by calling a phone call 'perfect friction' for "
                              'high-intent buyers [GV0ML_xytX8 @ 00:02:02]. ExclusiveLiveCall makes the '
                              'same point in cash terms: the job is generating profitable billable calls, '
                              'not just calls [grygjesM2j8 @ 00:01:14]. Their worked example turns $1,000 '
                              'of spend into 50 calls, 30 of them billable at $60, for $1,800 in revenue '
                              "and $800 left before other expenses [grygjesM2j8 @ 00:01:48]. Marketcall's "
                              'health insurance webinar shows why the distinction matters: benchmark cost '
                              'per call runs $8 to $15, but cost per billable call lands at $20 to $25 '
                              'because only 40 to 70 percent of calls qualify [9msaK2zlGMI @ 00:29:13]. On '
                              'the brokering side, Nate Ancelet warns that quality is the one thing to '
                              'watch, because bad calls will kill relationships with buyers [q4tpqSo7KCE @ '
                              '00:10:26]. The shared baseline is blunt: know the payout and the '
                              "qualification rule before spending, as Marketcall's $33 on a 90-second "
                              'health call shows [9msaK2zlGMI @ 00:01:51], then price every traffic source '
                              'against billable volume rather than dials.',
                              'The second point of agreement is that search intent carries the economics. '
                              'Soares Junior moved pay-per-call work to Google after repeated Facebook '
                              'account disables, and values Google because it captures people actively '
                              'searching [mRb5vDti0sI @ 00:00:21] [mRb5vDti0sI @ 00:01:50]. Chris at '
                              "Downey Marketing pushes high-intent local terms such as 'pool service "
                              "Gilbert' over a bare 'pools,' running exact and phrase match only with "
                              'negative keywords layered on [_VG0M_8UuLs @ 00:04:08]. Jordan Sordo of '
                              'Ringba lands in the same place: long-tail variants with a city, state, or '
                              'zip code bolted to the front or back are cheaper than the main five to ten '
                              "keywords, and a negative keyword list is 'an absolute must' [YhBQnt2AHbI @ "
                              '00:00:00] [YhBQnt2AHbI @ 00:00:41]. ExclusiveLiveCall draws the same '
                              "contrast on Microsoft Ads, where 'AC repair near me' beats 'how does an air "
                              "conditioner work' because keyword intent decides whether a click turns into "
                              'a call [grygjesM2j8 @ 00:02:42]. Chris also steers budget away from '
                              'Performance Max and Smart campaigns toward plain Search, blaming the '
                              'automated types for spam and irrelevant calls [_VG0M_8UuLs @ 00:01:12], and '
                              "Soares Junior's own Smart campaign burned 41 clicks to produce 2 calls "
                              'before stopping [mRb5vDti0sI @ 00:06:09]. Consensus baseline: Search '
                              'campaigns, tight match types, local modifiers, and a growing negative list '
                              'fed by what the calls reveal.',
                              'The third consensus is that the call must hit a live human fast, and that '
                              'every source needs its own tracking. Ventura cites research showing a 31 '
                              'percent conversion rate when calls are answered within 30 seconds, dropping '
                              'to 4 percent after five minutes, and notes 80 percent of callers will not '
                              'leave a voicemail [GV0ML_xytX8 @ 00:07:43]. Marketcall reports that contact '
                              'within five minutes converts best on lead-to-call flows [9msaK2zlGMI @ '
                              '00:09:56], and Sabri Suby, working high-ticket Meta funnels, has every lead '
                              'called within 60 seconds [u57s5wmdl5s @ 00:02:11]. On tracking, '
                              'ExclusiveLiveCall assigns each source its own tracking number, source ID, '
                              'or sub-affiliate ID [grygjesM2j8 @ 00:02:08], and Ventura puts a dollar '
                              'figure on it: on $10,000 a month, attribution shows which $2,000 versus '
                              "which $8,000 is performing [GV0ML_xytX8 @ 00:10:16]. Ventura's routing "
                              'target is the full IVR, smart-match, and simul-ring sequence finished in '
                              'under 30 seconds, with failover after 10 to 15 seconds to an auto-SMS or a '
                              "callback inside five minutes [GV0ML_xytX8 @ 00:08:29]. Marketcall's bundle "
                              'routing follows the same logic, sending calls by state and hours to the '
                              'highest payout and rerouting after 15 seconds [9msaK2zlGMI @ 01:02:31]. The '
                              'operators agree that slow pickup and blind attribution waste the spend that '
                              'search intent earned.'],
               'table': {'caption': 'Where Google and Meta pay-per-call operators line up',
                         'headers': ['Consensus Point',
                                     'What The Practitioner Reported',
                                     'Operator Implication',
                                     'Expert Source'],
                         'rows': [['Optimize to the paying outcome, not raw leads',
                                   'Track cost per enrolled customer instead of cost per lead as the core '
                                   'metric',
                                   'Judge every channel by enrollments it produces, not by cheap lead '
                                   'volume',
                                   'John Ventura ([GV0ML_xytX8 @ 00:00:31])'],
                                  ['Billable calls are the only calls that count',
                                   '$1,000 spend produced 50 calls, 30 billable at $60, for $1,800 revenue',
                                   'Model profit on billable percentage, leaving $800 before other '
                                   'expenses in this example',
                                   'ExclusiveLiveCall ([grygjesM2j8 @ 00:01:48])'],
                                  ['Billable rate swings unit cost hard on Facebook health traffic',
                                   'Cost per call $8 to $15 versus cost per billable call $20 to $25',
                                   'Budget against a 40 to 70 percent billable rate on health calls',
                                   'Marketcall ([9msaK2zlGMI @ 00:29:13])'],
                                  ['Search intent outperforms interruption for inbound phone calls',
                                   'Moved from Facebook to Google because Google captures people actively '
                                   'searching',
                                   'Lead with search campaigns when Meta accounts keep getting disabled',
                                   'Soares Junior ([mRb5vDti0sI @ 00:01:50])'],
                                  ['Long-tail local keywords plus a mandatory negative keyword list',
                                   'Add city, state, or zip to keywords; negative list is an absolute must',
                                   'Cheaper clicks than the main five to ten head keywords in the niche',
                                   'Ringba ([YhBQnt2AHbI @ 00:00:41])'],
                                  ['Answer speed decides whether paid calls convert into revenue',
                                   'Answering within 30 seconds converts 31 percent; after five minutes '
                                   'only 4 percent',
                                   'Staff and route so the full routing flow completes in under 30 seconds',
                                   'John Ventura ([GV0ML_xytX8 @ 00:07:43])'],
                                  ['Avoid automated Google campaign types for local call generation',
                                   'Performance Max and Smart campaigns bring spam and irrelevant calls; '
                                   'run Search instead',
                                   'Build plain Search campaigns with exact and phrase match keywords only',
                                   'Downey Marketing ([_VG0M_8UuLs @ 00:01:12])']]}},
              {'section_number': 2,
               'title': 'Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['Google call campaigns are being rebuilt around one hard date that changes '
                              'every account. Downey Marketing reports that from February 2026 Google '
                              'removes the option to create new call-only ads, with existing ones getting '
                              'roughly one more year of impressions, likely declining gradually before the '
                              'cutoff [4jiwxMObZvQ @ 00:01:07] [4jiwxMObZvQ @ 00:01:38]. The replacement '
                              'build is a responsive search ad with 15 headlines and 4 descriptions, a '
                              'call asset whose number matches the landing page, computer and tablet bid '
                              'adjustments set to minus 100 percent, and a form-free, tap-to-call mobile '
                              'landing page [4jiwxMObZvQ @ 00:03:00] [4jiwxMObZvQ @ 00:04:46]. Hasib Ashad '
                              'builds the call asset under Assets then Call, enters the number in '
                              '888-555-1234 format, and raises the bid 5 to 10 percent [Y4oieZQ07T8 @ '
                              '00:01:27] [Y4oieZQ07T8 @ 00:01:59]. For tracking, Ashad sets category phone '
                              'call lead, source calls from ads, count one, and a 15-second minimum, '
                              'because a call lasting more than 15 seconds then counts as a conversion, '
                              'with campaign-specific goals layered on top [Y4oieZQ07T8 @ 00:03:06] '
                              "[Y4oieZQ07T8 @ 00:03:55]. Adshot Media's flight-booking build runs maximize "
                              'clicks with a $2 max CPC, switches off search partners, display network, '
                              'and broad match, and schedules 9pm to 6am IST [9FAM3f3MDl0 @ 00:05:43] '
                              '[9FAM3f3MDl0 @ 00:06:51]. Approval Google quoted at one to two days came '
                              'through in about 30 minutes [9FAM3f3MDl0 @ 00:13:03].',
                              'On Meta, the practitioners run calls through a few distinct builds. '
                              "Ringba's Jordan Soto walks through two: add a call now button to the Page, "
                              'click Promote, select get more calls, and fill in creative, targeting, and '
                              'budget; the second method uses the Reach objective with a website URL for '
                              'verification and a call now CTA [2pUXq9do_FU @ 00:00:55]. Soto adds that '
                              "Ringba's native Business Manager integration pushes calls back as offline "
                              "conversions [2pUXq9do_FU @ 00:02:29]. Marketcall's health insurance setup "
                              'is more granular: Conversions objective, interests in health insurance, '
                              'wellness, and family, exclusions for Spanish speakers, non-accepted states, '
                              'and low-income audiences, mobile only on Facebook and Instagram feeds, and '
                              'a bid cap of $5 to $8 per call click on a one-day conversion window '
                              '[9msaK2zlGMI @ 00:16:50] [9msaK2zlGMI @ 00:22:40]. Their lead-to-call '
                              'option runs TrackDrive: call immediately, SMS after five seconds, call '
                              'again after five minutes [9msaK2zlGMI @ 00:09:12]. Sabri Suby, selling '
                              '$2,500-plus offers, skips book-a-call funnels where calls cost about $250 '
                              'and instead runs a 12-page PDF opt-in at $10 to $25 a lead, then a '
                              "long-form page and a Loom-style VSL [u57s5wmdl5s @ 00:02:11]. Suby's "
                              'structure is ABO testing with broad targeting by gender and location only, '
                              'optimized for leads and left alone for seven days [u57s5wmdl5s @ 00:09:50].',
                              'The unit economics are where the operators show their arithmetic. Ryan '
                              "Moran's pre-launch math assumes 50 percent click-to-call and one in three "
                              'calls chargeable, which works out to about six clicks per sale, so cost per '
                              'sale is roughly CPC times six [yB7cDGVlP0k @ 00:05:59]. Moran also targets '
                              '60 percent-plus mobile share in the forecasting tool and tests with $40 to '
                              "$50 of spend [yB7cDGVlP0k @ 00:08:01]. Marketcall's Facebook health "
                              'benchmarks give the full funnel: CPM about $10, CTR 1 to 1.5 percent, CPC '
                              '$1 to $1.50, landing page conversion 5 to 10 percent, and ROI of 20 to 50 '
                              'percent, starting at $50 to $100 a day [9msaK2zlGMI @ 00:29:13]. Nate '
                              "Ancelet's brokering spread is buying a call at $40 and selling at $45 or "
                              '$50, starting with a $3 to $5 margin; at $10 margin, 50 calls a day is $500 '
                              'profit and 2,000 calls a day is $20,000 [q4tpqSo7KCE @ 00:01:24] '
                              "[q4tpqSo7KCE @ 00:10:09]. Sabri Suby's $1,000 test runs at $25 per lead for "
                              '40 leads, 15 percent booking for 6 calls, 60 percent show for 4, 2 offers, '
                              'and 1 close worth $2,500 in month one or $6,000 lifetime [u57s5wmdl5s @ '
                              '00:15:20]. Suby kills any ad running two times above the $15-per-lead KPI '
                              '[u57s5wmdl5s @ 00:13:57].'],
               'table': {'caption': 'Exact settings, thresholds and unit math the operators run',
                         'headers': ['Lever', 'Exact Setting Or Number', 'How It Is Used', 'Expert Source'],
                         'rows': [['Call asset bid adjustment and number format',
                                   'Number entered as 888-555-1234, bid raised 5 to 10 percent',
                                   'Adds tap-to-call to search ads and lowers friction for searchers',
                                   'Hasib Ashad - Google Ads ([Y4oieZQ07T8 @ 00:01:59])'],
                                  ['Call conversion threshold for Google Ads tracking',
                                   'Calls longer than 15 seconds count as one conversion',
                                   "Feeds Google's optimization with campaign-specific phone call lead "
                                   'goals',
                                   'Hasib Ashad - Google Ads ([Y4oieZQ07T8 @ 00:03:55])'],
                                  ['Post call-only replacement device targeting',
                                   'Computer and tablet bid adjustments set to minus 100 percent',
                                   'Forces responsive search ads with call assets onto mobile phones only',
                                   'Downey Marketing ([4jiwxMObZvQ @ 00:04:46])'],
                                  ['Flight-booking campaign bidding and network settings',
                                   'Maximize clicks, $2 max CPC, partners, display and broad off',
                                   'Keeps spend on search during a 9pm to 6am IST schedule',
                                   'Adshot Media | Google Ads Experts ([9FAM3f3MDl0 @ 00:05:43])'],
                                  ['Facebook health insurance bid cap and window',
                                   'Bid cap $5 to $8 per call click, one-day conversion window',
                                   'Runs mobile-only Facebook and Instagram feeds on a Conversions '
                                   'objective',
                                   'Marketcall ([9msaK2zlGMI @ 00:22:40])'],
                                  ['Pre-launch cost per sale estimate for local niches',
                                   '50 percent click-to-call, one third chargeable, about six clicks per '
                                   'sale',
                                   'Multiply forecast CPC by six to estimate cost per chargeable call '
                                   'before launch',
                                   'Ryan Moran ([yB7cDGVlP0k @ 00:05:59])'],
                                  ['Brokering spread and starting margin per call',
                                   'Buy at $40, sell at $45 to $50, start at $3 to $5',
                                   'Scale volume with a locked fixed rate once affiliates and buyers are '
                                   'secured',
                                   'Nate Ancelet ([q4tpqSo7KCE @ 00:08:24])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Small Moves The Operators Swear By',
                           'body': 'Four low-cost habits that tighten call quality, approval odds and '
                                   'creative fit before more budget goes in.',
                           'items': ['Listen to call recordings constantly and push every irrelevant '
                                     'request into the negative keyword list [Ringba — YhBQnt2AHbI @ '
                                     '00:00:59].',
                                     'Make the Google business name match the domain the ads point to '
                                     '[Marketcall — 9msaK2zlGMI @ 01:04:47].',
                                     "Mine Google autocomplete for 'emergency' searches to find urgent "
                                     'verticals, then sell a single service such as emergency dentist as '
                                     'the foot in the door [Ryan Moran — yB7cDGVlP0k @ 00:00:47].',
                                     "Run the phone script, then feed the callers' own wording back into "
                                     'the ad copy [Sabri Suby — u57s5wmdl5s @ 00:16:49].']},
               'sop_steps': [{'step': 1,
                              'title': 'Pick A Specific Vertical And Payout',
                              'action': 'Choose an urgent, narrow niche with a defined qualified-call rule '
                                        'instead of a crowded broad offer.',
                              'detail': 'vanel sylvestre skips flight booking and health insurance for '
                                        'gutters at $64 per call, qualified only for new installation or '
                                        'repair inside the service area, with no customer-service or '
                                        'billing calls [vanel sylvestre — B2slPImGPD8 @ 00:03:16].'},
                             {'step': 2,
                              'title': 'Build A Keyword-Matched Call Landing Page',
                              'action': 'Send each keyword group to its own customized page with dynamic '
                                        'keyword insertion and a working call button.',
                              'detail': "Route 'bed bug treatment near me' to a bed-bug page with inserted "
                                        "copy; a general landing page won't work, while the matched page "
                                        'lifts quality score, lowers CPC and raises conversions [Ringba — '
                                        'YhBQnt2AHbI @ 00:01:17].'},
                             {'step': 3,
                              'title': 'Launch Search With Full Conversion Tracking',
                              'action': 'Run Search campaigns split by service or location and track every '
                                        'call path from day one.',
                              'detail': 'At minimum track ad calls, form fills and landing-page calls so '
                                        "the account can be diagnosed and Google can optimize; Downey's "
                                        'proof campaign logged 57 conversions in 30 days from 15 ad calls, '
                                        '11 forms and 31 landing-page calls [Downey Marketing — '
                                        '_VG0M_8UuLs @ 00:02:41].'},
                             {'step': 4,
                              'title': 'Test On Controlled Spend Before Scaling',
                              'action': 'Run a capped test and read the full economics before moving '
                                        'budget toward $10,000.',
                              'detail': 'Track CPC, cost per call, billable percentage, revenue per call '
                                        'and ROI together, because quality and economics have to be '
                                        'measured together [ExclusiveLiveCall — grygjesM2j8 @ '
                                        '00:09:30].'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['Channel choice is the first fork, and the operators split hard. John '
                              'Ventura prices Facebook and Instagram calls at $15-40 against $50-150 on '
                              'Google, provided creative is refreshed every two to three weeks '
                              '[GV0ML_xytX8 @ 00:04:04]. Soares Junior went the opposite way. He abandoned '
                              'Facebook for Google because his ad accounts kept getting disabled, and '
                              'because search captures people who are already hunting for the service '
                              '[mRb5vDti0sI @ 00:00:21]. Even inside Meta, the call mechanics diverge. '
                              'Jordan Soto of Ringba teaches the direct route: a call-now Page button, '
                              "then Promote with 'get more calls,' or a Reach campaign with a call-now "
                              "CTA. Calls flow back as offline conversions through Ringba's native "
                              'Business Manager integration [2pUXq9do_FU @ 00:00:55]. Marketcall '
                              'explicitly does not recommend Facebook call-only ads for health insurance. '
                              'Instead it pushes landing pages with call buttons, forms routed into '
                              'lead-to-call callbacks, and Lead Ads, all optimized on the Conversions '
                              'objective with a $5-8 bid cap per call click [9msaK2zlGMI @ 00:12:34]. The '
                              'same team benchmarks that flow at $8-15 per raw call and $20-25 per '
                              "billable call. That sits inside Ventura's Facebook band and far under his "
                              'Google range, which is why the Meta-first camp keeps building forms and '
                              'callbacks instead of chasing a pure tap-to-call button.',
                              'On Google, the fight is over campaign type. Soares Junior opened his '
                              'pest-control test on a Smart campaign that burned 41 clicks for 2 calls '
                              'before stopping. He still recommends call-only ads after landing 2 '
                              'qualified Marketcall calls [mRb5vDti0sI @ 00:06:09]. Chris at Downey '
                              'Marketing bans Performance Max and Smart campaigns outright for local lead '
                              'gen, citing spam and irrelevant calls. He runs Search campaigns on exact '
                              'and phrase match only, with ad groups split by service or location '
                              '[_VG0M_8UuLs @ 00:01:12]. Call-only itself is on borrowed time. Downey '
                              'reports no new call-only ads from February 2026, with existing ads getting '
                              'roughly one more year of gradually declining impressions. He rebuilds the '
                              'format as a responsive search ad with 15 headlines and 4 descriptions, a '
                              'call asset matching the landing-page number, and -100% computer and tablet '
                              'bids [4jiwxMObZvQ @ 00:04:46]. Ryan Moran already runs that hybrid: '
                              'mobile-only text ads with call extensions and negative bids on tablets and '
                              'computers. He targets verticals where the forecasting tool shows 60%+ '
                              'mobile, though he lets urgency override mobile share for plumbing '
                              '[yB7cDGVlP0k @ 00:02:58]. The keyword split mirrors this. Downey chases '
                              "'pool service Gilbert' over 'pools,' while Adshot Media switches off broad "
                              'match, search partners, and the display network entirely on its '
                              'flight-booking build.',
                              'Vertical and model choices split the camp again. Vanel Sylvestre tells '
                              'beginners to skip broad offers like flight booking and health insurance '
                              'because the competition is too high. He promotes a $64-per-call gutters '
                              "offer instead, where 'gutter services' shows 1k-10k searches, low "
                              'competition, and a single advertiser [B2slPImGPD8 @ 00:02:11]. Marketcall '
                              'runs exactly that health vertical at $33 per 90-second call with no caps, '
                              'and Adshot Media builds a flight-booking call campaign anyway. Nate Ancelet '
                              'skips media buying altogether. He brokers calls bought at $40 and sold at '
                              '$45-50, and warns off seasonal pest control [q4tpqSo7KCE @ 00:02:56], a '
                              'vertical Soares Junior tested on Google anyway. Ryan Moran, by contrast, '
                              'treats visible competitors in a vertical as a good sign. Even the '
                              'definition of a converted call differs. Hasib Ashad counts any call past 15 '
                              'seconds as a conversion, while Adshot Media defaults to 60 seconds and will '
                              'stretch the threshold to 600 [Y4oieZQ07T8 @ 00:03:55]. ExclusiveLiveCall '
                              "frames the long game differently from all of them. Paid ads are 'renting "
                              "traffic,' while owned assets like SEO sites, maps listings, and communities "
                              'last longer. Every source gets its own tracking number, source ID, or '
                              'sub-affiliate ID so quality can be judged per lane [grygjesM2j8 @ '
                              '00:07:42].'],
               'table': {'caption': 'Competing playbooks for generating inbound calls on Google and Meta',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['How to generate phone calls inside Meta ads',
                                   "Call-now Page button plus Promote 'get more calls' or a Reach campaign "
                                   'with call-now CTA',
                                   'Landing page, form-to-callback, or Lead Ads; Facebook call-only ads '
                                   'not recommended for health',
                                   'Ringba ([2pUXq9do_FU @ 00:00:55]); Marketcall ([9msaK2zlGMI @ '
                                   '00:12:34])'],
                                  ['Which paid channel to lead with for calls',
                                   'Facebook and Instagram at $15-40 per call with creative refreshed '
                                   'every two to three weeks',
                                   'Google search after Facebook accounts kept getting disabled, capturing '
                                   'active searchers',
                                   'John Ventura ([GV0ML_xytX8 @ 00:04:04]); Soares Junior ([mRb5vDti0sI @ '
                                   '00:00:21])'],
                                  ['Which Google campaign type to run for calls',
                                   'Smart campaign tested first, then call-only ads recommended after two '
                                   'qualified calls',
                                   'Search campaigns only; avoid Performance Max and Smart because of spam '
                                   'and irrelevant calls',
                                   'Soares Junior ([mRb5vDti0sI @ 00:09:05]); Downey Marketing '
                                   '([_VG0M_8UuLs @ 00:01:12])'],
                                  ['How to replace or replicate call-only ads',
                                   'Responsive search ad with call asset matching landing page and -100% '
                                   'computer and tablet bids',
                                   'Mobile-only text ads with call extensions and negative bids on tablets '
                                   'and computers',
                                   'Downey Marketing ([4jiwxMObZvQ @ 00:04:46]); Ryan Moran ([yB7cDGVlP0k '
                                   '@ 00:02:58])'],
                                  ['Minimum call length that counts as a conversion',
                                   'Count any call lasting more than 15 seconds as a phone call lead '
                                   'conversion',
                                   'Default 60-second call length in Google, adjustable upward to 600 '
                                   'seconds for flight booking',
                                   'Hasib Ashad - Google Ads ([Y4oieZQ07T8 @ 00:03:55]); Adshot Media | '
                                   'Google Ads Experts ([9FAM3f3MDl0 @ 00:00:57])'],
                                  ['Which vertical and business model to enter first',
                                   'Skip health insurance and flight booking; run low-competition gutters '
                                   'at $64 per call',
                                   'Broker calls at a $5-10 spread in auto, injury, and senior health; '
                                   'avoid seasonal pest control',
                                   'vanel sylvestre ([B2slPImGPD8 @ 00:00:00]); Nate Ancelet ([q4tpqSo7KCE '
                                   '@ 00:02:56])'],
                                  ['How to capture and qualify Meta prospects before the call',
                                   'Hook ad into a 3-6 question quiz that filters out people who cannot '
                                   'afford you',
                                   '12-page PDF opt-in at $10-25 per lead, then call every lead within 60 '
                                   'seconds',
                                   'Elite Marketer ([yfrI3Ns-hqY @ 00:07:31]); Sabri Suby ([u57s5wmdl5s @ '
                                   '00:02:11])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['Account death is the most repeated firsthand loss. Soares Junior left '
                              'Facebook because his accounts kept getting disabled. Then his Google '
                              "account was suspended mid-test for 'detected suspicious payment' "
                              '[mRb5vDti0sI @ 00:05:22]. OnlineSyndrome builds its whole pitch on the same '
                              "wound: 'our accounts keeps on getting suspended,' with call-only ads "
                              'disappearing and policy shifts every two to three years. Its answer is '
                              'AI-assisted landing pages and suspension appeals [wybWVvxFiI0 @ 00:01:14]. '
                              'Marketcall flags two self-inflicted triggers on Meta. Uploading bought '
                              'lists as custom audiences can get the account suspended. Coronavirus-angle '
                              'health ads are risky enough that some advertisers resort to cloaking '
                              '[9msaK2zlGMI @ 00:24:34]. Network access is its own gate. Vanel Sylvestre '
                              'says networks detect applicants from Pakistan, Bangladesh, India, and '
                              'Haiti, which is why he routes through a $2 PureVPN. His pages also '
                              "geo-localize visitors and block non-US traffic with a 'Service available in "
                              "the United States only' notice [B2slPImGPD8 @ 00:15:10]. John Ventura puts "
                              'compliance first for the same reason, pointing to FTC and state crackdowns '
                              'and TCPA fines of $500-1,500 per violation. Across these operators, the ad '
                              'account, payment profile, and network approval all sit upstream of every '
                              'call-economics spreadsheet.',
                              'The second trap is paying for calls that never bill. ExclusiveLiveCall runs '
                              'the math: $1,000 buys 50 calls, but only 30 are billable at $60. That '
                              "$1,800 in revenue leaves $800 before other expenses, which is why 'quality "
                              "and economics have to be measured together' [grygjesM2j8 @ 00:01:48]. "
                              "Marketcall's Facebook health benchmarks put billable rates at 40-70%, "
                              'turning $8-15 raw calls into $20-25 billable calls at 20-50% ROI, and '
                              'callers must be able to afford $150 a month. Ryan Moran prices the leak up '
                              'front. Assume 50% click-to-call and one in three calls chargeable, so a '
                              'sale costs roughly six clicks, or CPC times six [yB7cDGVlP0k @ 00:05:59]. '
                              'Downey Marketing traces clicks without calls to Performance Max and Smart '
                              'spam, broad keywords, lumped ad groups, and homepage traffic. The fix is '
                              'Search Terms reviews, negatives, and focused mobile landing pages '
                              '[_VG0M_8UuLs @ 00:04:08]. Jordan Sordo of Ringba adds the feedback loop: '
                              'listen to call recordings and push every irrelevant request into the '
                              'negative list [YhBQnt2AHbI @ 00:00:59]. Sabri Suby enforces the same '
                              'discipline on lead ads, killing anything that runs two times above his $15 '
                              'lead KPI, and warns that instant forms deliver spam emails. For brokers the '
                              'stakes compound, because Nate Ancelet warns that bad calls kill buyer '
                              'relationships.',
                              'The last failure is operational: calls arrive and nobody answers, or the '
                              "buy side breaks. John Ventura says 80% of callers won't leave a voicemail. "
                              'Answering within 30 seconds converts at 31%, while waiting five minutes '
                              'drops it to 4%. His routing therefore fails over after 10-15 seconds to an '
                              'auto-SMS or a callback inside five minutes [GV0ML_xytX8 @ 00:07:43]. '
                              "Marketcall's TrackDrive sequence runs a call, an SMS after five seconds, "
                              'then a second call at five minutes. A call center converts best but costs '
                              'about $15 per agent hour, often with a $1,000 weekly minimum [9msaK2zlGMI @ '
                              '00:37:53]. Nate Ancelet lists the broker-side traps: promising 200 calls '
                              'and delivering 50, unvetted affiliates, and a single buyer as a single '
                              'point of failure [q4tpqSo7KCE @ 00:10:40]. ExclusiveLiveCall echoes the '
                              'concentration risk on the traffic side and insists on respecting each '
                              "buyer's allowed sources [grygjesM2j8 @ 00:10:37]. Ventura also flags DIY "
                              "stack sprawl, '10 different tools in 90 days,' and rising input costs, with "
                              'Facebook cost per lead climbing from $8 in 2020 to $25+ in 2024. Speed is '
                              'non-negotiable for Sabri Suby too, who calls every opt-in within 60 '
                              'seconds. Ryan Moran adds a sales-side miss of his own: urgent care '
                              'decision-makers were too hard to reach.'],
               'table': {'caption': 'Firsthand traps, the numbers behind them, and the countermeasures '
                                    'practitioners teach',
                         'headers': ['Trap',
                                     'Firsthand Number or Incident',
                                     'Countermeasure Taught',
                                     'Expert Source'],
                         'rows': [['Google ad account suspended in the middle of a test',
                                   "Account suspended for 'detected suspicious payment' during a "
                                   'pest-control call test',
                                   'Use AI-assisted suspension appeals because accounts in this industry '
                                   'keep getting suspended',
                                   'Soares Junior ([mRb5vDti0sI @ 00:05:22]); OnlineSyndrome | Marketing & '
                                   'Technology Firm ([wybWVvxFiI0 @ 00:00:58])'],
                                  ['Smart campaign burning clicks without producing calls',
                                   '41 clicks produced only 2 calls before the Smart campaign stopped',
                                   'Run Search campaigns on exact and phrase match with negatives and '
                                   'Search Terms review',
                                   'Soares Junior ([mRb5vDti0sI @ 00:06:09]); Downey Marketing '
                                   '([_VG0M_8UuLs @ 00:04:08])'],
                                  ['Counting raw calls instead of billable calls',
                                   '$1,000 spend bought 50 calls but only 30 billable at $60 each',
                                   'Track cost per call, billable percentage, revenue per call, and ROI '
                                   'for every source',
                                   'ExclusiveLiveCall ([grygjesM2j8 @ 00:01:48])'],
                                  ['Slow answer and unanswered inbound calls',
                                   '31% conversion inside 30 seconds collapses to 4% after five minutes',
                                   'Fail over after 10-15 seconds to auto-SMS or a callback within five '
                                   'minutes',
                                   'John Ventura ([GV0ML_xytX8 @ 00:07:43])'],
                                  ['Uploading bought lists as Facebook custom audiences',
                                   'Purchased lists uploaded to Facebook may get the ad account suspended',
                                   'Build custom audiences from 1,000+ real contacts and expand with '
                                   'lookalikes',
                                   'Marketcall ([9msaK2zlGMI @ 00:18:42])'],
                                  ['Broker over-promising volume to a single buyer',
                                   'Promising 200 calls a day and then delivering only 50',
                                   'Lock fixed rates, vet every affiliate, and never depend on one buyer',
                                   'Nate Ancelet ([q4tpqSo7KCE @ 00:10:40])'],
                                  ['Letting expensive lead ads keep running on Meta',
                                   'Ads sitting two times above the $15 per lead KPI',
                                   'Kill the ad, review on a 5-day window, keep CTR at 1% or higher',
                                   'Sabri Suby ([u57s5wmdl5s @ 00:13:57])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Four checks before adding budget to any call campaign',
                           'body': 'Each gate comes straight from a loss or bottleneck a practitioner hit '
                                   'firsthand. Clear all four before scaling spend.',
                           'items': ['Prove billable percentage, revenue per call, and ROI on a controlled '
                                     'spend before pushing toward $10,000, never judging on raw call count '
                                     '[ExclusiveLiveCall — grygjesM2j8 @ 00:09:30].',
                                     'Confirm an answer path under 30 seconds with a 10-15 second failover '
                                     "to auto-SMS or a five-minute callback, because 80% of callers won't "
                                     'leave a voicemail [John Ventura — GV0ML_xytX8 @ 00:07:43].',
                                     'Keep Google traffic on Search campaigns, avoiding Performance Max '
                                     'and Smart, with ad calls, form fills, and landing-page calls all '
                                     'tracked before reading results [Downey Marketing — _VG0M_8UuLs @ '
                                     '00:02:41].',
                                     'Line up more than one buyer and never promise volume you cannot '
                                     'deliver, since a single buyer is a single point of failure [Nate '
                                     'Ancelet — q4tpqSo7KCE @ 00:10:40].']}}],
 'pull_quote': '"The only thing you have to watch out for is quality because bad calls will kill your '
               'relationships." — Nate Ancelet (q4tpqSo7KCE @ 00:10:26).',
 'diagram_id': 'diag-01',
 'action_checklist': ["Create a Google Ads call conversion with category 'phone call lead,' source 'calls "
                      "from ads,' count set to one, and a 15-second minimum call length, using "
                      'campaign-specific goals [Hasib Ashad - Google Ads — Y4oieZQ07T8 @ 00:03:06].',
                      'Rebuild call-only campaigns as responsive search ads with 15 headlines, 4 '
                      'descriptions, a call asset matching the landing-page number, and -100% computer and '
                      'tablet bid adjustments [Downey Marketing — 4jiwxMObZvQ @ 00:03:00].',
                      'Build long-tail keywords with a city, state, or zip code added, attach a negative '
                      'keyword list, and keep feeding it from call recordings [Ringba — YhBQnt2AHbI @ '
                      '00:00:00].',
                      "On Facebook, add a call-now Page button, then click Promote, select 'get more "
                      "calls,' set creative, targeting, and budget, and track calls as offline conversions "
                      '[Ringba — 2pUXq9do_FU @ 00:00:55].',
                      'Launch Facebook health call campaigns on mobile only in Facebook and Instagram '
                      'feeds with a $5-8 bid cap per call click and a 1-day conversion window, starting at '
                      '$50-100 a day [Marketcall — 9msaK2zlGMI @ 00:22:40].',
                      'Before pitching a vertical, estimate cost per sale as CPC times six, based on 50% '
                      'click-to-call and one in three calls chargeable, then validate with a $40-50 test '
                      '[Ryan Moran — yB7cDGVlP0k @ 00:05:59].'],
 'statutory_citations': [{'title': 'John Ventura — The $100M Pay Per Call Generation System (Step-By-Step) '
                                   '[00:07:43]',
                          'url': 'https://www.youtube.com/watch?v=GV0ML_xytX8&t=463s',
                          'relevance': 'Primary practitioner testimony on speed-to-answer conversion '
                                       'rates, failover routing, and cost per call by channel.'},
                         {'title': 'Marketcall — Webinar: How to run Health Insurance Pay Per Call offers '
                                   'on Facebook ads [00:22:40]',
                          'url': 'https://www.youtube.com/watch?v=9msaK2zlGMI&t=1360s',
                          'relevance': 'Primary practitioner testimony on Facebook health call campaign '
                                       'settings, bid caps, and billable-call benchmarks.'},
                         {'title': "Downey Marketing — Google Ads Is Getting Rid Of Call Only Ads - Here's "
                                   'How To Adjust [00:01:07]',
                          'url': 'https://www.youtube.com/watch?v=4jiwxMObZvQ&t=67s',
                          'relevance': 'Primary practitioner testimony on the February 2026 call-only ad '
                                       'removal and the responsive search ad replacement build.'},
                         {'title': 'ExclusiveLiveCall — How to Generate Pay Per Call Traffic That Converts '
                                   '| Paid, Organic & Owned Traffic | Episode 13 [00:01:48]',
                          'url': 'https://www.youtube.com/watch?v=grygjesM2j8&t=108s',
                          'relevance': 'Primary practitioner testimony on billable-call economics, '
                                       'per-source tracking, and concentration risk.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'GV0ML_xytX8',
                       'title': 'The $100M Pay Per Call Generation System (Step-By-Step)',
                       'channel': 'John Ventura',
                       'author': 'John Ventura',
                       'text': 'Compare that to cold outreach where industry average is 2 to 3%.',
                       'tip': 'Compare that to cold outreach where industry average is 2 to 3%.',
                       'timestamp': 382,
                       'timestamp_seconds': 382,
                       'timestamp_label': '[00:06:22]',
                       'url': 'https://www.youtube.com/watch?v=GV0ML_xytX8&t=382s',
                       'markdown': '[00:06:22](https://www.youtube.com/watch?v=GV0ML_xytX8&t=382s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'GV0ML_xytX8',
                       'title': 'The $100M Pay Per Call Generation System (Step-By-Step)',
                       'channel': 'John Ventura',
                       'author': 'John Ventura',
                       'text': "Research shows if you answer within 30 seconds, you've got a 31% "
                               'conversion rate.',
                       'tip': "Research shows if you answer within 30 seconds, you've got a 31% conversion "
                              'rate.',
                       'timestamp': 463,
                       'timestamp_seconds': 463,
                       'timestamp_label': '[00:07:43]',
                       'url': 'https://www.youtube.com/watch?v=GV0ML_xytX8&t=463s',
                       'markdown': '[00:07:43](https://www.youtube.com/watch?v=GV0ML_xytX8&t=463s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '9msaK2zlGMI',
                       'title': 'Webinar: How to run Health Insurance Pay Per Call offers on Facebook ads',
                       'channel': 'Marketcall',
                       'author': 'Marketcall',
                       'text': 'Set a bid cap of five to eight dollars per call click and use a one day '
                               'conversion window.',
                       'tip': 'Set a bid cap of five to eight dollars per call click and use a one day '
                              'conversion window.',
                       'timestamp': 1360,
                       'timestamp_seconds': 1360,
                       'timestamp_label': '[00:22:40]',
                       'url': 'https://www.youtube.com/watch?v=9msaK2zlGMI&t=1360s',
                       'markdown': '[00:22:40](https://www.youtube.com/watch?v=9msaK2zlGMI&t=1360s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'q4tpqSo7KCE',
                       'title': 'How to make $20,344/day with Pay Per Call',
                       'channel': 'Nate Ancelet',
                       'author': 'Nate Ancelet',
                       'text': "If you're doing 50 calls a day at $10 per call margin, that's $500 profit "
                               'per day.',
                       'tip': "If you're doing 50 calls a day at $10 per call margin, that's $500 profit "
                              'per day.',
                       'timestamp': 609,
                       'timestamp_seconds': 609,
                       'timestamp_label': '[00:10:09]',
                       'url': 'https://www.youtube.com/watch?v=q4tpqSo7KCE&t=609s',
                       'markdown': '[00:10:09](https://www.youtube.com/watch?v=q4tpqSo7KCE&t=609s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'q4tpqSo7KCE',
                       'title': 'How to make $20,344/day with Pay Per Call',
                       'channel': 'Nate Ancelet',
                       'author': 'Nate Ancelet',
                       'text': 'The only thing you have to watch out for is quality because bad calls will '
                               'kill your relationships.',
                       'tip': 'The only thing you have to watch out for is quality because bad calls will '
                              'kill your relationships.',
                       'timestamp': 626,
                       'timestamp_seconds': 626,
                       'timestamp_label': '[00:10:26]',
                       'url': 'https://www.youtube.com/watch?v=q4tpqSo7KCE&t=626s',
                       'markdown': '[00:10:26](https://www.youtube.com/watch?v=q4tpqSo7KCE&t=626s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'mRb5vDti0sI',
                       'title': 'Inside my Google Ads campaign for Pay Per Call Affiliate Marketing Offer '
                                '| Pay Per Call',
                       'channel': 'Soares Junior',
                       'author': 'Soares Junior',
                       'text': 'I moved from Facebook to Google because my accounts kept getting disabled.',
                       'tip': 'I moved from Facebook to Google because my accounts kept getting disabled.',
                       'timestamp': 21,
                       'timestamp_seconds': 21,
                       'timestamp_label': '[00:00:21]',
                       'url': 'https://www.youtube.com/watch?v=mRb5vDti0sI&t=21s',
                       'markdown': '[00:00:21](https://www.youtube.com/watch?v=mRb5vDti0sI&t=21s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '4jiwxMObZvQ',
                       'title': "Google Ads Is Getting Rid Of Call Only Ads - Here's How To Adjust",
                       'channel': 'Downey Marketing',
                       'author': 'Downey Marketing',
                       'text': "But from right here you can see in February 2026 they're going to pretty "
                               'much remove the option to create new call only ads.',
                       'tip': "But from right here you can see in February 2026 they're going to pretty "
                              'much remove the option to create new call only ads.',
                       'timestamp': 67,
                       'timestamp_seconds': 67,
                       'timestamp_label': '[00:01:07]',
                       'url': 'https://www.youtube.com/watch?v=4jiwxMObZvQ&t=67s',
                       'markdown': '[00:01:07](https://www.youtube.com/watch?v=4jiwxMObZvQ&t=67s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Y4oieZQ07T8',
                       'title': 'Google Ads Call Assets FULL TUTORIAL - Get More Phone Calls',
                       'channel': 'Hasib Ashad - Google Ads',
                       'author': 'Hasib Ashad - Google Ads',
                       'text': "So, if the call lasts more than 15 seconds, that's counted as a "
                               'conversion.',
                       'tip': "So, if the call lasts more than 15 seconds, that's counted as a conversion.",
                       'timestamp': 235,
                       'timestamp_seconds': 235,
                       'timestamp_label': '[00:03:55]',
                       'url': 'https://www.youtube.com/watch?v=Y4oieZQ07T8&t=235s',
                       'markdown': '[00:03:55](https://www.youtube.com/watch?v=Y4oieZQ07T8&t=235s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'wybWVvxFiI0',
                       'title': 'World’s No. 1 Pay Per Call Course 2026 | Beginner To Advanced Google Ads '
                                'Call Campaign Training',
                       'channel': 'OnlineSyndrome | Marketing & Technology Firm',
                       'author': 'OnlineSyndrome | Marketing & Technology Firm',
                       'text': 'Because this industry, our accounts keeps on getting suspended.',
                       'tip': 'Because this industry, our accounts keeps on getting suspended.',
                       'timestamp': 74,
                       'timestamp_seconds': 74,
                       'timestamp_label': '[00:01:14]',
                       'url': 'https://www.youtube.com/watch?v=wybWVvxFiI0&t=74s',
                       'markdown': '[00:01:14](https://www.youtube.com/watch?v=wybWVvxFiI0&t=74s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'yB7cDGVlP0k',
                       'title': 'Finding Pay Per Call Industries: Local Lead Generation Services with '
                                'Call-Only Ads (Google Adwords)',
                       'channel': 'Ryan Moran',
                       'author': 'Ryan Moran',
                       'text': 'Assume 50% of clicks call and one third of calls are chargeable, so it '
                               'takes about six clicks per sale and your cost is roughly CPC times six.',
                       'tip': 'Assume 50% of clicks call and one third of calls are chargeable, so it '
                              'takes about six clicks per sale and your cost is roughly CPC times six.',
                       'timestamp': 359,
                       'timestamp_seconds': 359,
                       'timestamp_label': '[00:05:59]',
                       'url': 'https://www.youtube.com/watch?v=yB7cDGVlP0k&t=359s',
                       'markdown': '[00:05:59](https://www.youtube.com/watch?v=yB7cDGVlP0k&t=359s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '9FAM3f3MDl0',
                       'title': 'How To Setup Pay Per Call Campaign Google Ads | Flight Booking | Google '
                                'Ads Tutorial | AdShot Media',
                       'channel': 'Adshot Media | Google Ads Experts',
                       'author': 'Adshot Media | Google Ads Experts',
                       'text': 'Google says approval can take one to two days, but in practice the ads '
                               'were approved in about 30 minutes.',
                       'tip': 'Google says approval can take one to two days, but in practice the ads were '
                              'approved in about 30 minutes.',
                       'timestamp': 783,
                       'timestamp_seconds': 783,
                       'timestamp_label': '[00:13:03]',
                       'url': 'https://www.youtube.com/watch?v=9FAM3f3MDl0&t=783s',
                       'markdown': '[00:13:03](https://www.youtube.com/watch?v=9FAM3f3MDl0&t=783s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'yfrI3Ns-hqY',
                       'title': 'EP 359: Master Facebook Quiz Ads & Unlock Endless Possibilities',
                       'channel': 'Elite Marketer',
                       'author': 'Elite Marketer',
                       'text': 'Make sure your pixel is on all of those pages on your website including '
                               'the quiz page.',
                       'tip': 'Make sure your pixel is on all of those pages on your website including the '
                              'quiz page.',
                       'timestamp': 338,
                       'timestamp_seconds': 338,
                       'timestamp_label': '[00:05:38]',
                       'url': 'https://www.youtube.com/watch?v=yfrI3Ns-hqY&t=338s',
                       'markdown': '[00:05:38](https://www.youtube.com/watch?v=yfrI3Ns-hqY&t=338s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'u57s5wmdl5s',
                       'title': 'How to Scale Meta Ads on a Low Budget (Post-Andromeda)',
                       'channel': 'Sabri Suby',
                       'author': 'Sabri Suby',
                       'text': 'Anything that sits two times above KPI of the $15 a lead, we kill that ad.',
                       'tip': 'Anything that sits two times above KPI of the $15 a lead, we kill that ad.',
                       'timestamp': 837,
                       'timestamp_seconds': 837,
                       'timestamp_label': '[00:13:57]',
                       'url': 'https://www.youtube.com/watch?v=u57s5wmdl5s&t=837s',
                       'markdown': '[00:13:57](https://www.youtube.com/watch?v=u57s5wmdl5s&t=837s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '2pUXq9do_FU',
                       'title': 'Generating Inbound Calls with Facebook Ads',
                       'channel': 'Ringba',
                       'author': 'Ringba',
                       'text': 'Go to your facebook page and click promote select get more calls and fill '
                               'in your ad details including creative targeting and budget.',
                       'tip': 'Go to your facebook page and click promote select get more calls and fill '
                              'in your ad details including creative targeting and budget.',
                       'timestamp': 72,
                       'timestamp_seconds': 72,
                       'timestamp_label': '[00:01:12]',
                       'url': 'https://www.youtube.com/watch?v=2pUXq9do_FU&t=72s',
                       'markdown': '[00:01:12](https://www.youtube.com/watch?v=2pUXq9do_FU&t=72s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'grygjesM2j8',
                       'title': 'How to Generate Pay Per Call Traffic That Converts | Paid, Organic & '
                                'Owned Traffic | Episode 13',
                       'channel': 'ExclusiveLiveCall',
                       'author': 'ExclusiveLiveCall',
                       'text': 'Quality and economics have to be measured together.',
                       'tip': 'Quality and economics have to be measured together.',
                       'timestamp': 604,
                       'timestamp_seconds': 604,
                       'timestamp_label': '[00:10:04]',
                       'url': 'https://www.youtube.com/watch?v=grygjesM2j8&t=604s',
                       'markdown': '[00:10:04](https://www.youtube.com/watch?v=grygjesM2j8&t=604s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'B2slPImGPD8',
                       'title': "I Made $11,429+ With Pay Per Call Affiliate Marketing (Here's How!)",
                       'channel': 'vanel sylvestre',
                       'author': 'vanel sylvestre',
                       'text': "So if you keep promoting these you won't make any phone calls and the "
                               'competition is very high.',
                       'tip': "So if you keep promoting these you won't make any phone calls and the "
                              'competition is very high.',
                       'timestamp': 22,
                       'timestamp_seconds': 22,
                       'timestamp_label': '[00:00:22]',
                       'url': 'https://www.youtube.com/watch?v=B2slPImGPD8&t=22s',
                       'markdown': '[00:00:22](https://www.youtube.com/watch?v=B2slPImGPD8&t=22s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '_VG0M_8UuLs',
                       'title': 'Why Your Google Ads Are Getting Clicks But No Calls (And What To Do About '
                                'It)',
                       'channel': 'Downey Marketing',
                       'author': 'Downey Marketing',
                       'text': 'So, Performance Max is usually not good for local lead generation.',
                       'tip': 'So, Performance Max is usually not good for local lead generation.',
                       'timestamp': 109,
                       'timestamp_seconds': 109,
                       'timestamp_label': '[00:01:49]',
                       'url': 'https://www.youtube.com/watch?v=_VG0M_8UuLs&t=109s',
                       'markdown': '[00:01:49](https://www.youtube.com/watch?v=_VG0M_8UuLs&t=109s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'YhBQnt2AHbI',
                       'title': 'Best Practices for Pay Per Call Campaigns on Google Ads: Part 1',
                       'channel': 'Ringba',
                       'author': 'Ringba',
                       'text': 'Implement a negative keywords list. Using a negative keyword list is an '
                               'absolute must.',
                       'tip': 'Implement a negative keywords list. Using a negative keyword list is an '
                              'absolute must.',
                       'timestamp': 41,
                       'timestamp_seconds': 41,
                       'timestamp_label': '[00:00:41]',
                       'url': 'https://www.youtube.com/watch?v=YhBQnt2AHbI&t=41s',
                       'markdown': '[00:00:41](https://www.youtube.com/watch?v=YhBQnt2AHbI&t=41s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'}]}
