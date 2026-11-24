from __future__ import annotations

CHAPTER_4 = {'id': 'Q4',
 'chapter_id': 'Q4',
 'chapter_number': 4,
 'question_number': 4,
 'slug': 'pay-per-call-routing-optimization-and-call-attribution',
 'question_prompt': 'How do I route calls to the highest-converting buyer and attribute every call to its '
                    'traffic source?',
 'kicker': 'Q4 / THE BIG MONEY PLAYBOOKS',
 'title': 'Routing Optimization and Call Attribution',
 'subtitle': 'Automated precision routing, tag routing filters, URL parameters as tags, SIP routing, '
             'routing methods explained, dynamic number pool tracking, and call tracking tools compared '
             '(Invoca, CallRail, CallPOP, CloudTalk)',
 'layout_template': 'comparison_matrix',
 'reading_time_minutes': 15,
 'executive_summary': "Pay-per-call operators teaching on Ringba's channel agree on one premise: whoever "
                      'owns the call tracking and routing layer owns the margin. Adam of Ringba argues '
                      'that affiliates running on network numbers lose control of busy-signal recovery, '
                      'ring-timeout rerouting, duplicate remonetization and geo-accurate routing, and that '
                      'duplicate routing alone typically pays for the platform, with duplicates running 5% '
                      'to 25% of call flow. Jordan Soto and Mattias Mesters translate that into '
                      'configuration: priority tiers, weight fractions, concurrency and dollar caps, hours '
                      'of operation with lunch breaks, tag routing filters fed by URL parameters, and SIP '
                      "delivery. Attribution vendors CallPOP, Invoca and Travis Wilkie's CallRail "
                      'walkthrough split between static source numbers and dynamic number pools, while '
                      'tool reviewers split on pricing: CallRail looks cheap until add-ons triple the '
                      'bill, Invoca is quote-only enterprise, Ringba targets pay-per-call.',
 'key_metrics': [{'label': 'Duplicate Call Share of Call Flow',
                  'metric': 'Duplicate Call Share of Call Flow',
                  'value': 'At least 5% on the low end, up to 25% on the high end',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Adam reports this range from Ringba platform statistics across hundreds of '
                             'verticals, calling monetized duplicates pure profit that networks pay only '
                             'once for',
                  'source': 'Ringba ([ojcbZuG798w @ 00:14:05])'},
                 {'label': 'Area Code Mismatch Rate',
                  'metric': 'Area Code Mismatch Rate',
                  'value': 'Approximately 35% of people',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Share of people whose area code differs from where they physically live, '
                             'which Adam says makes area-code geo routing burn licensed insurance and '
                             'mortgage call flow',
                  'source': 'Ringba ([ojcbZuG798w @ 00:22:10])'},
                 {'label': 'Zip-Level Mortgage Call Payout Lift',
                  'metric': 'Zip-Level Mortgage Call Payout Lift',
                  'value': 'From $10 per call to up to $250 per call',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'A Ringba mortgage client combined demographic and geographic routing on high '
                             'home-value California zip codes, selling premium calls to smarter buyers and '
                             'dumping the rest on networks',
                  'source': 'Ringba ([ojcbZuG798w @ 00:41:53])'},
                 {'label': 'New Buyer Financial Exposure Cap',
                  'metric': 'New Buyer Financial Exposure Cap',
                  'value': '$2,000 for the first 2 weeks',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Jordan Soto's example of capping a new buyer by dollar amount so they pay "
                             'before more calls are sent',
                  'source': 'Ringba ([yFkULiyenzk @ 00:01:44])'}],
 'sections': [{'section': 1,
               'title': 'The Practitioner Consensus',
               'paragraphs': ['The baseline every Ringba speaker repeats is that a publisher who runs on a '
                              "network's or broker's number has surrendered the call flow. Adam's "
                              'masterclass puts it bluntly: without your own call tracking you cannot '
                              'prioritize or weight buyers, and whoever handed you the number is the only '
                              'party that ever receives the call [ojcbZuG798w @ 00:02:05]. Jordan Soto '
                              'restates the same rule for rerouting, telling media buyers and publishers '
                              "who rely on a network's tracking that they are simply out of luck when a "
                              'buyer is busy or never answers [0QJvQjrUoX8 @ 00:00:57]. The pain compounds '
                              'with scale. Adam describes clients moving from a handful of calls to 20 or '
                              '50 a day, then to thousands and tens of thousands daily, which is called '
                              'completely normal in the space, and warns that operators lacking automated '
                              'rerouting will get absolutely murdered by their buyers [ojcbZuG798w @ '
                              '00:08:53]. Soto frames duplicate handling the same way: networks typically '
                              'refuse to pay for repeat callers, and only independent tracking lets the '
                              'publisher keep control and get paid [ytuZI-5RwoI @ 00:00:39]. The shared '
                              'prerequisite is an owned routing layer sitting between every tracking '
                              'number and every destination, even for affiliates who still sell through '
                              'networks.',
                              'Outside the pay-per-call bubble, attribution vendors land on the same '
                              'foundation: a distinct number for every source you want to measure. '
                              "CallPOP's walkthrough starts with buying local or toll-free numbers, "
                              'assigning each one a source label and a receiving number, and notes that '
                              'for publications, signs and billboards those two parameters are all you '
                              'need before calls start flowing [wr6G-Sojm50 @ 00:01:13]. For web traffic '
                              "the consensus shifts to dynamic pools. Invoca's website tag swaps static "
                              'numbers for dynamic ones unique to each visitor, treating each number as a '
                              'session identifier while capturing UTM source, medium, paid search keyword '
                              'and Google click ID [bJeLdEIwej8 @ 00:00:35]. Jordan Soto describes '
                              "Ringba's version as number swapping or DNI that locks a pool number to a "
                              'browser session until the visitor goes idle, closes the browser or leaves, '
                              'and tracks impressions whether or not the visitor ever calls [pNWCpdBjuPA @ '
                              '00:00:35]. Travis Wilkie, demonstrating CallRail, gives the street-level '
                              'reason: without call tracking it is next to impossible to tell where calls '
                              'come from, which is the old line about knowing half your marketing works '
                              'but not which half [eH4764v8-74 @ 00:01:44]. Every speaker treats '
                              'source-level numbers as table stakes before any routing decision means '
                              'anything.',
                              'The third point of agreement is that the operator has to do their own '
                              'quality assurance, because nobody else in the value chain will. Adam '
                              'reports having hosted the CEO of almost every pay-per-call network on the '
                              'Pay Per Caller show, and that 100% of them said to listen to call '
                              'recordings, ideally playing them in the background to catch weak back-end '
                              'buyers or duplicated IVR trees burning conversions [ojcbZuG798w @ '
                              '00:48:23]. Travis Wilkie lands in the same place from the local-business '
                              'side, saying that replaying sales recordings exposes things you thought you '
                              'were doing and were not, plus habits you never noticed [eH4764v8-74 @ '
                              "00:04:40]. Invoca's brand testimonial quantifies what conversation data "
                              'unlocked once calls were tied to revenue instead of clicks and impressions: '
                              'a 33 percent efficiency gain that let the team cut wasted ad spend, and 45% '
                              'of people likely to hit voicemail now scheduling appointments online '
                              '[IPh2uXrQS1A @ 00:00:57]. The consensus extends to buyer caps. Adam insists '
                              'new buyers capping you at ten calls a day while you push 300 is fair, '
                              'because a human must answer and vet each call, and once your quality is '
                              'proven those same caps keep competitors out of the campaign [ojcbZuG798w @ '
                              '00:34:44]. Pay-per-call, in that telling, is exclusionary rather than '
                              'inclusive.'],
               'table': {'caption': 'Where Pay-Per-Call and Attribution Practitioners Agree on Routing and '
                                    'Tracking Fundamentals',
                         'headers': ['Consensus Principle',
                                     'Practitioner Position',
                                     'Operator Implication',
                                     'Expert Source'],
                         'rows': [['Own the tracking and routing layer yourself',
                                   'Without your own platform you cannot prioritize, weight or control '
                                   'where calls land',
                                   'Run every network and broker number through your own routing platform '
                                   'first',
                                   'Ringba ([ojcbZuG798w @ 00:02:05])'],
                                  ['Reroute busy and unanswered calls automatically every time',
                                   'Ringba reroutes to another buyer as many times as it takes to connect',
                                   'Publishers relying on network tracking cannot recover these dropped '
                                   'calls in real time',
                                   'Ringba ([0QJvQjrUoX8 @ 00:00:57])'],
                                  ['Remonetize duplicate callers instead of eating the loss',
                                   'Networks pay once per caller while selling duplicates to multiple '
                                   'back-end parties',
                                   "Route repeat callers to fresh buyers and take back the network's "
                                   'hidden margin',
                                   'Ringba ([0QJvQjrUoX8 @ 00:02:33])'],
                                  ['Assign a unique tracking number per marketing source',
                                   'Each advertising channel gets its own number with a source label and '
                                   'receiving number',
                                   'Spin up new numbers whenever a new offline or online initiative '
                                   'launches',
                                   'CallPOP ([wr6G-Sojm50 @ 00:00:20])'],
                                  ['Use dynamic number pools for website visitor sessions',
                                   'A JavaScript tag swaps static numbers for session-unique numbers and '
                                   'captures UTM, keyword and click ID',
                                   'Tie every web-driven call back to the exact campaign, keyword and '
                                   'session',
                                   'Invoca ([bJeLdEIwej8 @ 00:00:35])'],
                                  ['Route by physical caller location, never by area code',
                                   'Roughly 35% of people carry an area code different from where they '
                                   'actually live',
                                   'Use number pool zip, city and state data to match licensed buyers '
                                   'precisely',
                                   'Ringba ([yFkULiyenzk @ 00:02:27])'],
                                  ['Listen to your own call recordings constantly in the background',
                                   'Every network CEO interviewed on the Pay Per Caller show said to '
                                   'listen to recordings',
                                   'Catch duplicated IVR trees and weak back-end buyers that quietly burn '
                                   'your return',
                                   'Ringba ([ojcbZuG798w @ 00:48:23])']]}},
              {'section': 2,
               'title': 'Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['Mattias Mesters walks through the core routing plan math in Ringba: '
                              'priority one targets are always tried first, priority two only when none of '
                              'them is available, and within a tier the weights become fractions, so '
                              'targets weighted 1, 6, 6 and 1 split traffic 1/14, 6/14, 6/14 and 1/14 '
                              '[0eCCbtHmCJE @ 00:02:34]. Error handling sits on top. Adam describes Ringba '
                              'detecting a busy signal within a few milliseconds and immediately dialing '
                              'buyer two, fast enough that no caller can notice, which neutralizes call '
                              'centers that oversell capacity to many publishers and then busy-signal '
                              'overflow so they never pay for it [ojcbZuG798w @ 00:05:07]. For buyers who '
                              'let calls ring 30 seconds instead of bouncing them, the fix is a ring '
                              'timeout configured at the buyer or target level, maybe five seconds, maybe '
                              'ten, after which the call is pulled and rerouted [ojcbZuG798w @ 00:08:15]. '
                              'Adam pairs that with a commercial term: if a ringing buyer imposes duration '
                              'requirements, bill on duration from the moment the call starts ringing '
                              'rather than from answer, because the buyer captured the option value of '
                              'picking up the whole time [ojcbZuG798w @ 00:06:38]. Adam actually prefers '
                              'busy-signal buyers, since the bounce arrives in real time.',
                              'Simultaneous dialing rings every eligible buyer at once, whether three or '
                              '600, and the first to answer wins the call, but Adam flags the trap: if '
                              'buyer one pays $10, buyer two $22 and buyer three $6, and buyer three '
                              'always answers fastest, sim-dial gets expensive, and mixed West Coast and '
                              'East Coast requirements break it too [ojcbZuG798w @ 00:11:41]. The ideal '
                              'setup is nationwide buyers paying roughly the same, such as $10, $10 and '
                              '$10.25, on raw calls with no duration requirement [ojcbZuG798w @ 00:12:36]. '
                              'Concurrency is the next lever. Adam recommends configuring buyer '
                              'concurrency hourly by day rather than flat, after asking each call center '
                              'when lunch costs them 20% of capacity, when the 2 p.m. shift change adds '
                              'seats and when half the agents leave at 7 p.m., and on big direct campaigns '
                              'having someone talk to buyer operations daily [ojcbZuG798w @ 00:57:17]. '
                              'Caps protect cash as well as capacity. Jordan Soto suggests capping a new '
                              'buyer at $2,000 for the first two weeks so they pay before more calls flow, '
                              'and stopping delivery once a daily, weekly or monthly cap is hit because '
                              'overage calls go unpaid [yFkULiyenzk @ 00:01:44].',
                              'The data layer is what turns routing into a margin weapon. Mattias Mesters '
                              'shows Ringba tag routing filters on each target: any stored tag, whether '
                              'passed by publishers, captured from a landing page via number pools or '
                              'appended through instant caller profiles, can gate eligibility using logic '
                              'such as begins with, contains, equals multiple values, exists, less than or '
                              'greater than, with bulk zip lists and AND/OR rules, for example Alabama, '
                              'Alaska, Arizona and Connecticut or listed zips, and only from test '
                              'publisher one [4MDNmxviCKk @ 00:02:20]. URL parameters feed the same '
                              "filters: declare the parameter under Integrations, keep the third party's "
                              "name such as SRC or rename it to source, then select it in the target's "
                              'filter dropdown [qr3oqapZvoo @ 00:01:08]. On the voice side, Jordan Soto '
                              "says Ringba can auto-dial the selections inside a buyer's IVR so the caller "
                              'never hears a second identical menu, lifting conversion [ETvzBEnleCs @ '
                              '00:02:03], and recommends SIP delivery to buyers who support it for faster '
                              'connects, better audio and data passed in the SIP header [0QJvQjrUoX8 @ '
                              "00:00:19]. Together these filters replace the area-code guesswork Ringba's "
                              'speakers blame for misrouting the roughly 35% of callers whose area code '
                              'does not match their location.'],
               'table': {'caption': 'Routing Settings, Attribution Mechanics and Unit Economics Taught by '
                                    'the Speakers',
                         'headers': ['Mechanic or Tool',
                                     'Exact Setting or Number',
                                     'How Operators Use It',
                                     'Expert Source'],
                         'rows': [['Priority tiers and weight distribution in Ringba',
                                   'Weights of 1, 6, 6 and 1 split calls 1/14, 6/14, 6/14 and 1/14',
                                   'Priority two targets only receive calls when every priority one target '
                                   'is unavailable',
                                   'Ringba ([0eCCbtHmCJE @ 00:02:34])'],
                                  ['Ring timeout rerouting on slow-answering buyers',
                                   'Configurable per buyer or target, for example five or ten seconds',
                                   'Pull the call from slow-ringing buyers and send it to an available one',
                                   'Ringba ([ojcbZuG798w @ 00:08:15])'],
                                  ['Simultaneous dial across all eligible buyers at once',
                                   'Best when nationwide buyers pay near-equal $10, $10 and $10.25 on raw '
                                   'calls',
                                   'Avoid when a $6 buyer always answers before the $10 and $22 buyers',
                                   'Ringba ([ojcbZuG798w @ 00:11:58])'],
                                  ['Duplicate call routing to buyers with no prior relationship',
                                   'At least 5% and up to 25% of calls are duplicates across hundreds of '
                                   'verticals',
                                   'Resell repeat callers to fresh buyers, sometimes monetizing one '
                                   'consumer five to nine times',
                                   'Ringba ([ojcbZuG798w @ 00:14:05])'],
                                  ['Zip-level demographic plus geographic routing for mortgage calls',
                                   'Calls once sold at $10 now sell for up to $250 in high home-value zips',
                                   'Send premium zips like 90210 to smarter buyers and dump low-quality '
                                   'calls on networks',
                                   'Ringba ([ojcbZuG798w @ 00:41:53])'],
                                  ['Dynamic number reuse through a custom attribution window',
                                   'Reuse an uncalled number after 30 minutes if customers usually call '
                                   'within that window',
                                   'Keeps one-to-one call tracking feasible while holding phone number '
                                   'costs down',
                                   'Invoca ([bJeLdEIwej8 @ 00:02:43])'],
                                  ['CallRail plan fees plus usage pricing for agencies',
                                   'Five numbers and 250 minutes per plan, extra numbers $3, minutes 6 '
                                   'cents, lead tracking from $55 monthly',
                                   'Budget plan fees plus usage before scaling local lead generation '
                                   'tracking numbers',
                                   'StackSense ([Kkuu-FgiGxg @ 00:00:17])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Routing Edges Most Affiliates Leave on the Table',
                           'body': 'Small configuration and negotiation moves that the Ringba speakers say '
                                   'separate operators who keep their margin from those who quietly hand '
                                   'it to buyers and networks.',
                           'items': ['Bill ringing buyers on duration measured from ring rather than from '
                                     'answer, because the buyer held the option to pick up the entire time '
                                     'callers sat waiting [Ringba — ojcbZuG798w @ 00:06:38].',
                                     'When a network refuses to remove its own IVR, have Ringba auto-dial '
                                     "the buyer's IVR selections so callers never hear the same qualifying "
                                     'questions twice [Ringba — ojcbZuG798w @ 00:47:46].',
                                     'Treat claims of unlimited concurrency as a red flag; ten extra CC '
                                     'from a network is reasonable, while 500 from one giant buyer is '
                                     'fishy [Ringba — ojcbZuG798w @ 00:55:36].',
                                     'Watch for hours-of-operation arbitrage: a network can quote 8 a.m. '
                                     'to 6 p.m. while buyers actually answer until 6:30 or 7 p.m., keeping '
                                     'the late payouts [Ringba — ojcbZuG798w @ 00:50:23].']},
               'sop_steps': [{'step': 1,
                              'title': 'Deploy Dynamic Number Pools',
                              'action': 'Copy the Ringba JavaScript snippet from your account and paste it '
                                        'into the header of every page you want tracked.',
                              'detail': 'Ringba selects an available pool number, locks it to the '
                                        "visitor's browser session and attributes the call to that session "
                                        'data, including impressions that never call [Ringba — pNWCpdBjuPA '
                                        '@ 00:01:28].'},
                             {'step': 2,
                              'title': 'Declare Data Tags and Target Filters',
                              'action': 'Create URL parameters under Integrations, then add tag routing '
                                        'filters on each target by state, zip list or publisher ID.',
                              'detail': 'Click create URL parameter, keep the third-party name or rename '
                                        "it, then select it in the target's tag routing filter dropdown "
                                        'with AND/OR logic [Ringba — qr3oqapZvoo @ 00:00:52].'},
                             {'step': 3,
                              'title': 'Build the Routing Plan and Buyer Limits',
                              'action': 'Set priority tiers and weights, load buyer hours of operation, '
                                        'and configure concurrency plus daily, weekly or monthly caps.',
                              'detail': 'Request hours of operation from every buyer and include lunch '
                                        'time and breaks, since calls sent to an empty desk drop or hit '
                                        'voicemail unpaid [Ringba — 0QJvQjrUoX8 @ 00:01:36].'},
                             {'step': 4,
                              'title': 'Arm the Rerouting Rules',
                              'action': 'Turn on busy-signal rerouting, a short ring timeout and duplicate '
                                        'routing for repeat callers.',
                              'detail': 'Ringba checks in milliseconds whether the person has called '
                                        'before and routes them to buyer two, which has no relationship '
                                        'with that caller and treats it as fresh [Ringba — ojcbZuG798w @ '
                                        '00:16:51].'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ["Ringba's masterclass host, Adam, refuses to treat simultaneous dialing as a "
                              'default. Sim-dial rings every eligible buyer at once, whether that is '
                              'three, twenty-five or six hundred, and the first one to pick up owns the '
                              'call, which maximizes answer rates [ojcbZuG798w @ 00:09:28]. The same '
                              'session flags the trap immediately: if buyer one pays $10, buyer two pays '
                              '$22 and buyer three pays $6, and buyer three always answers fastest, '
                              'sim-dial turns into a very expensive situation, and split geographic '
                              'requirements such as West Coast versus East Coast buyers break it outright '
                              '[ojcbZuG798w @ 00:11:41]. The verdict is narrow: run sim-dial only when '
                              'every buyer takes national traffic, payouts sit essentially level ($10, '
                              '$10, $10.25), and buyers pay on raw call with no duration requirement, '
                              'because then salesperson quality is irrelevant and speed to answer is the '
                              'whole game [ojcbZuG798w @ 00:12:55]. Everywhere else, Mattias Mesters '
                              'demonstrates the alternative playbook inside the routing plan: priority '
                              'tiers where priority one is always tried first and priority two only when '
                              'none of those targets are available, with weights acting as fractions, so '
                              'four targets weighted 1, 6, 6 and 1 split traffic in fourteenths '
                              '[0eCCbtHmCJE @ 00:02:15]. Waterfall control beats raw speed whenever '
                              'payouts or eligibility diverge.',
                              'Duplicate callers split operators into two camps. The aggressive camp '
                              'resells every repeat: Adam reports duplicate rates of at least 5% on the '
                              'low end and up to 25% on the high end across hundreds of verticals, while '
                              'networks refuse to pay for a duplicate roughly 98% of the time or more, so '
                              'monetizing any slice of that band is pure profit [ojcbZuG798w @ 00:14:05]. '
                              "Jordan Soto frames resale as stripping the network's margin: networks sell "
                              'duplicates to multiple parties on the back end yet pay the publisher only '
                              'once per caller, and your own tracking takes that margin away without them '
                              'having any idea [0QJvQjrUoX8 @ 00:02:33]. The conservative camp pins '
                              'repeats instead. On campaigns where consumers keep dialing back believing '
                              'the number is customer service, Ringba lets you force a repeat caller to '
                              'the same buyer over and over, and Adam stresses that the ability to resell '
                              'never obligates you to [ojcbZuG798w @ 00:19:26]. The identical tension runs '
                              'through buyer mix. Adam wants a deliberate blend of direct buyers, '
                              'aggregators, brokers and networks: networks usually take a pretty high '
                              'margin, yet a call answered at a loss through a network still beats letting '
                              'it die unanswered [ojcbZuG798w @ 01:00:30]. Resell or pin, direct or '
                              'network, the deciding variable is campaign type.',
                              "Attribution itself has rival playbooks. For geo-licensed verticals, Adam's "
                              "primary route is number pool JavaScript that reads the caller's physical "
                              'zip code, but the fallback when that is unavailable is brute structure: '
                              'subdivide ad campaigns by state, from Michigan to Texas to California to '
                              'every other state, then pass the region in the URL to the landing page or '
                              'run 50 different tracking numbers, and tell buyers you only send callers '
                              'physically in, say, Wisconsin regardless of area code [ojcbZuG798w @ '
                              '00:27:23]. On number assignment, Jordan Soto describes Ringba pools locking '
                              'a number to one browser session until the visitor goes idle, closes the '
                              'browser or leaves the page [pNWCpdBjuPA @ 00:00:35]. Invoca argues for '
                              'recycling instead: set an attribution window matching buying behavior, so '
                              'if customers typically call within 30 minutes, the uncalled number goes to '
                              'a new visitor after 30 minutes, which makes one-to-one tracking feasible '
                              'and keeps costs down [bJeLdEIwej8 @ 00:02:43]. CallPOP runs the leanest '
                              'version for offline media, assigning one unique tracking number per '
                              'marketing source or lead acquisition channel, pointed at a single receiving '
                              'number for publications, signs and billboards [wr6G-Sojm50 @ 00:00:20]. '
                              "Session-lock buys per-visitor certainty; Invoca's window reuse explicitly "
                              'buys lower cost.'],
               'table': {'caption': 'Contested routing and attribution decisions, side by side',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['How to dial multiple eligible buyers',
                                   'Simultaneous dial all buyers, first to answer wins, only with national '
                                   'traffic, level payouts, raw-call billing',
                                   'Priority tiers plus weights, for example 1, 6, 6 and 1 out of 14 calls',
                                   'Ringba ([ojcbZuG798w @ 00:12:55])'],
                                  ['What to do with repeat duplicate callers',
                                   'Reroute repeats to fresh buyers; some plans remonetize one consumer '
                                   'five to nine times',
                                   'Force repeat callers to the same buyer when consumers treat the number '
                                   'as customer service',
                                   'Ringba ([ojcbZuG798w @ 00:17:06])'],
                                  ['How to geo-route licensed insurance or mortgage calls',
                                   'Number pool JavaScript captures physical zip code, city, state, '
                                   'latitude and longitude',
                                   'Split ad campaigns per state and run up to 50 separate tracking '
                                   'numbers',
                                   'Ringba ([ojcbZuG798w @ 00:27:23])'],
                                  ['How long a dynamic number stays assigned',
                                   'Ringba locks a pool number to one browser session until idle, close or '
                                   'exit',
                                   'Invoca reuses an uncalled number after a 30-minute attribution window '
                                   'to keep costs down',
                                   'Invoca ([bJeLdEIwej8 @ 00:02:43])'],
                                  ['Which tracking platform fits the operator type',
                                   'Ringba ranked best for pay per call and lead gen agencies, local '
                                   'tracking 5.5 cents a minute',
                                   'CallRail ranked best for agencies running local lead generation across '
                                   'lots of small clients',
                                   'StackSense ([Kkuu-FgiGxg @ 00:01:34])'],
                                  ['Enterprise depth versus lean pay-for-outcome billing',
                                   'Invoca for massive healthcare or insurance operations with deep AI and '
                                   'request-a-quote pricing',
                                   'Nimbata pay-per-answered-call model, billed the same whether calls '
                                   'last two or twenty minutes',
                                   'CloudTalk ([qwPhoKG3HJM @ 00:02:20])'],
                                  ['Direct buyers versus networks in the buyer mix',
                                   'Direct buyers for real-time concurrency communication and properly '
                                   'load-balanced call flow',
                                   'Networks as overflow despite pretty high margin, since an answered '
                                   'loss beats a dead call',
                                   'Ringba ([ojcbZuG798w @ 01:00:30])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The costliest failures Adam describes are buyer-side games, not tech '
                              'glitches. Call centers tell publishers, brokers and networks they have more '
                              'capacity than they really do, keep every agent saturated, then flip on a '
                              'busy signal whenever no seat is free so they never pay for the overflow '
                              "call; publishers riding a network's number simply watch that call drop with "
                              'nowhere else to go [ojcbZuG798w @ 00:03:31]. Buyers without queues play a '
                              'quieter version, letting calls ring 30 seconds or more so an agent might '
                              'still grab them while consumers give up and hang up unpaid; the counter is '
                              'billing duration from the moment of ringing rather than from answer '
                              'whenever duration requirements apply [ojcbZuG798w @ 00:06:38]. Hours of '
                              'operation get arbitraged too: a network can quote 8 a.m. to 6 p.m. while '
                              'buyers really run until 6:30 or 7 p.m., collecting on remnant calls after '
                              'the cutoff while the publisher is told calls after 6 p.m. go unpaid '
                              '[ojcbZuG798w @ 00:50:23]. Jordan Soto adds the overlooked lunch-hour leak: '
                              'calls sent while agents eat get dropped or hit voicemail and will more than '
                              'likely go unpaid, which is why buyer targets need hours including lunch and '
                              'breaks [0QJvQjrUoX8 @ 00:01:36].',
                              'Geo and qualification mistakes bleed money quietly. Roughly 35% of people '
                              'carry an area code that does not match where they live, so area-code '
                              'routing means approximately 35% of the time a ready-to-buy caller may land '
                              'on an unlicensed buyer and never get paid [yFkULiyenzk @ 00:02:27]. Adam '
                              'walks the scenario live: a 248 Michigan number calling from Alaska gets '
                              'disqualified within 10 or 15 seconds, well short of the 60-second duration '
                              'billing typical in insurance, and networks shrug because the affiliate eats '
                              'the loss, while affiliates without their own recordings never even see it '
                              'happen [ojcbZuG798w @ 00:24:43]. Even correctly geo-routed traffic draws '
                              'chargeback attempts; expect a buyer report claiming fifteen percent of '
                              'callers were not in Wisconsin, sometimes on calls the buyer already sold '
                              '[ojcbZuG798w @ 00:28:43]. The IVR trap compounds it: a network that refuses '
                              'to strip its own IVR forces callers through the same questions twice, which '
                              'drastically removes conversion rates, and Adam has heard it on so many call '
                              'recordings it is ridiculous. The fix is letting Ringba auto-dial the '
                              "buyer's IVR selections so the consumer never hears the second tree "
                              '[ojcbZuG798w @ 00:47:12]. Every one of these leaks is invisible without '
                              'independent recordings.',
                              "Capacity lies and loose caps are the final economics check. Adam's rule is "
                              'blunt: anyone claiming they can take unlimited calls is not telling the '
                              'truth, because unlimited calls require unlimited humans sitting around paid '
                              'to wait, labor is the most expensive part of any call center, and the '
                              'number one thing any center wants fixed is call flow efficiency '
                              '[ojcbZuG798w @ 00:53:19]. Flat caps break on staffing swings. Ask buyers '
                              'how capacity moves through the day: a center may lose 20% of its capacity '
                              'at the noon lunch hour, gain seats at a 2 p.m. shift change, and keep '
                              'wanting calls until 11:00 after half the agents leave at 7 p.m.; most '
                              'publishers never ask, then eat no-answers, rings and busies [ojcbZuG798w @ '
                              '00:57:17]. Jordan Soto adds two hard stops: buyers will not pay for calls '
                              'sent after their cap is already hit, and a brand-new buyer should be capped '
                              'at $2,000 for the first two weeks to make sure they pay before any more '
                              'calls flow [yFkULiyenzk @ 00:01:23]. Tool cost is its own trap. CloudTalk '
                              'warns that a CallRail base plan around forty-five to fifty bucks can easily '
                              'triple once AI transcriptions, form tracking and premium integrations are '
                              'layered on [qwPhoKG3HJM @ 00:01:03].'],
               'table': {'caption': 'Firsthand failure modes and the economics check that fixes each',
                         'headers': ['Failure Mode', 'What Happened', 'Economic Check', 'Expert Source'],
                         'rows': [['Busy-signal capacity game by call centers',
                                   'Centers overstate capacity, then busy-signal overflow calls so they '
                                   'never pay for them',
                                   'Own routing detects the busy in milliseconds and dials buyer two '
                                   'immediately',
                                   'Ringba ([ojcbZuG798w @ 00:05:07])'],
                                  ['Ring-out buyers with no queue in place',
                                   'Calls ring 30 seconds or longer while consumers give up and hang up '
                                   'unpaid',
                                   'Set a per-target ring timeout of five or ten seconds, then reroute '
                                   'automatically',
                                   'Ringba ([ojcbZuG798w @ 00:08:15])'],
                                  ['Area-code based geographic routing',
                                   'About 35% of callers carry mismatched area codes and land on '
                                   'unlicensed buyers',
                                   'Route by physical zip code captured through number pool tracking '
                                   'technology instead',
                                   'Ringba ([yFkULiyenzk @ 00:02:47])'],
                                  ['Hours-of-operation and lunch-break blind spots',
                                   'Calls sent while agents eat lunch get dropped or go to voicemail '
                                   'unpaid',
                                   'Request buyer hours including lunch and breaks, then adjust routing '
                                   'plans and targets',
                                   'Ringba ([0QJvQjrUoX8 @ 00:01:57])'],
                                  ['Stacked duplicate IVR trees across the chain',
                                   'Network IVR repeats the same qualifying questions and drastically '
                                   'removes conversion rates',
                                   "Auto-dial the buyer's IVR selections so callers never hear the second "
                                   'tree',
                                   'Ringba ([ETvzBEnleCs @ 00:01:42])'],
                                  ['Unpaid duplicate calls through networks',
                                   'Networks decline payment on duplicates while reselling them on the '
                                   'back end',
                                   'Duplicate call routing alone pays for your own call tracking in almost '
                                   'every scenario',
                                   'Ringba ([ojcbZuG798w @ 00:17:43])'],
                                  ['Ad budget spent on calls with no sale potential',
                                   'A large percentage of budget was going toward calls with no potential '
                                   'for a sale',
                                   'Call attribution delivered a 33 percent efficiency gain and cut wasted '
                                   'ad spend',
                                   'Invoca ([IPh2uXrQS1A @ 00:00:57])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Four checks before you scale call flow to any buyer',
                           'body': 'Each gate below comes straight from losses and buyer games the '
                                   'practitioners reported. Clear all four before raising volume or '
                                   'concurrency on a buyer, network or routing plan.',
                           'items': ['Reject any buyer or network claiming unlimited concurrency, and '
                                     'treat 500 CC funneled into one giant buyer as fishy until they '
                                     'explain their buyer network [Ringba — ojcbZuG798w @ 00:55:36].',
                                     'Cap every new buyer at a hard dollar exposure, such as $2,000 for '
                                     'the first two weeks, until they pay [Ringba — yFkULiyenzk @ '
                                     '00:01:44].',
                                     'Never run simultaneous dial when payouts diverge like $10, $22 and '
                                     '$6 or when buyers split East Coast and West Coast geographies '
                                     '[Ringba — ojcbZuG798w @ 00:11:41].',
                                     'Listen to your call recordings to catch network back-end buyers with '
                                     'crappy agents or stupid IVRs burning your return on investment '
                                     '[Ringba — ojcbZuG798w @ 00:48:43].']}}],
 'pull_quote': '"If you just only use duplicate call routing in almost 100% of scenarios this alone will '
               'pay for your own call tracking, and then everything else you do with it is all just '
               'profit." Attributed to Ringba (ojcbZuG798w @ 00:17:43).',
 'diagram_id': 'diag-07',
 'action_checklist': ['Paste the Ringba JavaScript snippet into the header of every page you want to track '
                      'so pool numbers swap per visitor session [Ringba — pNWCpdBjuPA @ 00:01:28].',
                      'Declare incoming URL parameters under Integrations, for example SRC renamed to '
                      'source, then select them as target tag routing filters [Ringba — qr3oqapZvoo @ '
                      '00:00:52].',
                      'Build target-level tag routing filters with AND/OR logic, such as approved states '
                      'OR a bulk zip code list AND a specific publisher ID [Ringba — 4MDNmxviCKk @ '
                      '00:02:20].',
                      'Connect via SIP to any buyer whose contact center software accepts it for faster '
                      'connection times, better voice quality and data in the SIP header [Ringba — '
                      '0QJvQjrUoX8 @ 00:00:19].',
                      'Waterfall IVR-qualified debt callers: send over-$10,000 presses to the $25 buyer '
                      'capped at 10 a day, then overflow to the next payout tier [Ringba — ojcbZuG798w @ '
                      '00:33:24].',
                      'Feed source-level call conversions back to Google Ads through your tracking '
                      'platform so campaigns optimize for phone calls [Travis Wilkie — eH4764v8-74 @ '
                      '00:03:09].'],
 'statutory_citations': [{'title': 'Ringba — Pay Per Call Masterclass - Improving Conversions with '
                                   'Automated Routing [00:14:05]',
                          'url': 'https://www.youtube.com/watch?v=ojcbZuG798w&t=845s',
                          'relevance': 'Primary practitioner testimony on duplicate call rates, network '
                                       'payout behavior and remonetizing repeat callers.'},
                         {'title': 'Ringba — How To Optimize Your Pay Per Call Routing (Part 2) [00:02:27]',
                          'url': 'https://www.youtube.com/watch?v=yFkULiyenzk&t=147s',
                          'relevance': 'Primary practitioner testimony on the 35% area code mismatch and '
                                       'zip code based geographic routing.'},
                         {'title': 'Invoca — Track and attribute calls using dynamic phone numbers '
                                   '[00:02:43]',
                          'url': 'https://www.youtube.com/watch?v=bJeLdEIwej8&t=163s',
                          'relevance': 'Primary practitioner testimony on attribution windows and reusing '
                                       'uncalled dynamic numbers to keep costs down.'},
                         {'title': 'Ringba — Ringba Product Training: Automated Routing [00:02:15]',
                          'url': 'https://www.youtube.com/watch?v=0eCCbtHmCJE&t=135s',
                          'relevance': 'Primary practitioner testimony on priority tiers and weight-based '
                                       'call distribution inside routing plans.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'ojcbZuG798w',
                       'title': 'Pay Per Call Masterclass - Improving Conversions with Automated Routing',
                       'channel': 'Ringba',
                       'author': 'Ringba',
                       'text': 'Based on the statistics in our platform across hundreds of different '
                               'verticals and industries we typically see on the low end at least 5% '
                               'duplicate calls and on the high end sometimes up to 25% duplicate calls.',
                       'tip': 'Based on the statistics in our platform across hundreds of different '
                              'verticals and industries we typically see on the low end at least 5% '
                              'duplicate calls and on the high end sometimes up to 25% duplicate calls.',
                       'timestamp': 845,
                       'timestamp_seconds': 845,
                       'timestamp_label': '[00:14:05]',
                       'url': 'https://www.youtube.com/watch?v=ojcbZuG798w&t=845s',
                       'markdown': '[00:14:05](https://www.youtube.com/watch?v=ojcbZuG798w&t=845s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ojcbZuG798w',
                       'title': 'Pay Per Call Masterclass - Improving Conversions with Automated Routing',
                       'channel': 'Ringba',
                       'author': 'Ringba',
                       'text': 'Most call tracking platforms will only route by area code and this is a '
                               'flawed methodology.',
                       'tip': 'Most call tracking platforms will only route by area code and this is a '
                              'flawed methodology.',
                       'timestamp': 1296,
                       'timestamp_seconds': 1296,
                       'timestamp_label': '[00:21:36]',
                       'url': 'https://www.youtube.com/watch?v=ojcbZuG798w&t=1296s',
                       'markdown': '[00:21:36](https://www.youtube.com/watch?v=ojcbZuG798w&t=1296s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ojcbZuG798w',
                       'title': 'Pay Per Call Masterclass - Improving Conversions with Automated Routing',
                       'channel': 'Ringba',
                       'author': 'Ringba',
                       'text': 'They put that information into routing plans and now they sell phone calls '
                               'they used to get ten dollars for for up to two hundred and fifty dollars a '
                               'phone call.',
                       'tip': 'They put that information into routing plans and now they sell phone calls '
                              'they used to get ten dollars for for up to two hundred and fifty dollars a '
                              'phone call.',
                       'timestamp': 2513,
                       'timestamp_seconds': 2513,
                       'timestamp_label': '[00:41:53]',
                       'url': 'https://www.youtube.com/watch?v=ojcbZuG798w&t=2513s',
                       'markdown': '[00:41:53](https://www.youtube.com/watch?v=ojcbZuG798w&t=2513s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'pNWCpdBjuPA',
                       'title': 'What is Dynamic Number Pool Tracking (and How to Implement it)',
                       'channel': 'Ringba',
                       'author': 'Ringba',
                       'text': 'Ringba will select an available number from the pool and locks it to that '
                               "user's browser session for the set amount of time until they become idle, "
                               'close the browser or leave the page.',
                       'tip': 'Ringba will select an available number from the pool and locks it to that '
                              "user's browser session for the set amount of time until they become idle, "
                              'close the browser or leave the page.',
                       'timestamp': 35,
                       'timestamp_seconds': 35,
                       'timestamp_label': '[00:00:35]',
                       'url': 'https://www.youtube.com/watch?v=pNWCpdBjuPA&t=35s',
                       'markdown': '[00:00:35](https://www.youtube.com/watch?v=pNWCpdBjuPA&t=35s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'yFkULiyenzk',
                       'title': 'How To Optimize Your Pay Per Call Routing (Part 2)',
                       'channel': 'Ringba',
                       'author': 'Ringba',
                       'text': 'If you want to limit your financial exposure to a new buyer, you can cap '
                               'them at $2,000 for the first 2 weeks to make sure they pay before sending '
                               'them any more calls.',
                       'tip': 'If you want to limit your financial exposure to a new buyer, you can cap '
                              'them at $2,000 for the first 2 weeks to make sure they pay before sending '
                              'them any more calls.',
                       'timestamp': 104,
                       'timestamp_seconds': 104,
                       'timestamp_label': '[00:01:44]',
                       'url': 'https://www.youtube.com/watch?v=yFkULiyenzk&t=104s',
                       'markdown': '[00:01:44](https://www.youtube.com/watch?v=yFkULiyenzk&t=104s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '4MDNmxviCKk',
                       'title': 'Ringba Product Training: Tag Routing Filters',
                       'channel': 'Ringba',
                       'author': 'Ringba',
                       'text': 'These are filters that you can place on the individual target level that '
                               'indicate that the call has to meet certain conditions in order for that '
                               'target to be eligible to receive that call.',
                       'tip': 'These are filters that you can place on the individual target level that '
                              'indicate that the call has to meet certain conditions in order for that '
                              'target to be eligible to receive that call.',
                       'timestamp': 36,
                       'timestamp_seconds': 36,
                       'timestamp_label': '[00:00:36]',
                       'url': 'https://www.youtube.com/watch?v=4MDNmxviCKk&t=36s',
                       'markdown': '[00:00:36](https://www.youtube.com/watch?v=4MDNmxviCKk&t=36s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '0QJvQjrUoX8',
                       'title': 'How To Optimize Your Pay Per Call Routing (Part 1)',
                       'channel': 'Ringba',
                       'author': 'Ringba',
                       'text': 'This results in faster connection times, better voice quality, plus the '
                               'ability to seamlessly pass data in the SIP header, which all result in '
                               'better conversion rates for your calls.',
                       'tip': 'This results in faster connection times, better voice quality, plus the '
                              'ability to seamlessly pass data in the SIP header, which all result in '
                              'better conversion rates for your calls.',
                       'timestamp': 19,
                       'timestamp_seconds': 19,
                       'timestamp_label': '[00:00:19]',
                       'url': 'https://www.youtube.com/watch?v=0QJvQjrUoX8&t=19s',
                       'markdown': '[00:00:19](https://www.youtube.com/watch?v=0QJvQjrUoX8&t=19s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '0eCCbtHmCJE',
                       'title': 'Ringba Product Training: Automated Routing',
                       'channel': 'Ringba',
                       'author': 'Ringba',
                       'text': 'If none of those targets are available then we will try priority two, and '
                               'furthermore the distribution or the percentage of the calls that go to '
                               'certain targets are managed by the weight.',
                       'tip': 'If none of those targets are available then we will try priority two, and '
                              'furthermore the distribution or the percentage of the calls that go to '
                              'certain targets are managed by the weight.',
                       'timestamp': 135,
                       'timestamp_seconds': 135,
                       'timestamp_label': '[00:02:15]',
                       'url': 'https://www.youtube.com/watch?v=0eCCbtHmCJE&t=135s',
                       'markdown': '[00:02:15](https://www.youtube.com/watch?v=0eCCbtHmCJE&t=135s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ETvzBEnleCs',
                       'title': 'Pay Per Call Routing Explained (Part 1)',
                       'channel': 'Ringba',
                       'author': 'Ringba',
                       'text': "With Ringba you can also automatically dial the selections in your buyer's "
                               "IVR so the users won't hear them.",
                       'tip': "With Ringba you can also automatically dial the selections in your buyer's "
                              "IVR so the users won't hear them.",
                       'timestamp': 102,
                       'timestamp_seconds': 102,
                       'timestamp_label': '[00:01:42]',
                       'url': 'https://www.youtube.com/watch?v=ETvzBEnleCs&t=102s',
                       'markdown': '[00:01:42](https://www.youtube.com/watch?v=ETvzBEnleCs&t=102s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'qr3oqapZvoo',
                       'title': 'Using URL Parameters as Tag Routing Filters | Ringba Platform Training',
                       'channel': 'Ringba',
                       'author': 'Ringba',
                       'text': 'If the URL parameter you are receiving is SRC but you want it to be called '
                               'something else, you can declare the parameter to be represented in Ringba '
                               'however you want.',
                       'tip': 'If the URL parameter you are receiving is SRC but you want it to be called '
                              'something else, you can declare the parameter to be represented in Ringba '
                              'however you want.',
                       'timestamp': 83,
                       'timestamp_seconds': 83,
                       'timestamp_label': '[00:01:23]',
                       'url': 'https://www.youtube.com/watch?v=qr3oqapZvoo&t=83s',
                       'markdown': '[00:01:23](https://www.youtube.com/watch?v=qr3oqapZvoo&t=83s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '9m3WjFJdUnA',
                       'title': 'CallRail vs Invoca',
                       'channel': 'DiscoverMyBusiness',
                       'author': 'DiscoverMyBusiness',
                       'text': 'CallRail local phone numbers ninety percent, dynamic number insertion '
                               'ninety percent, ease of use ninety one percent.',
                       'tip': 'CallRail local phone numbers ninety percent, dynamic number insertion '
                              'ninety percent, ease of use ninety one percent.',
                       'timestamp': 35,
                       'timestamp_seconds': 35,
                       'timestamp_label': '[00:00:35]',
                       'url': 'https://www.youtube.com/watch?v=9m3WjFJdUnA&t=35s',
                       'markdown': '[00:00:35](https://www.youtube.com/watch?v=9m3WjFJdUnA&t=35s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Kkuu-FgiGxg',
                       'title': '5 Best Call Tracking Software for Marketing Agencies (2026)',
                       'channel': 'StackSense',
                       'author': 'StackSense',
                       'text': 'Number five, Ringba. Local tracking starts at 5 and 1/2 cents a minute.',
                       'tip': 'Number five, Ringba. Local tracking starts at 5 and 1/2 cents a minute.',
                       'timestamp': 74,
                       'timestamp_seconds': 74,
                       'timestamp_label': '[00:01:14]',
                       'url': 'https://www.youtube.com/watch?v=Kkuu-FgiGxg&t=74s',
                       'markdown': '[00:01:14](https://www.youtube.com/watch?v=Kkuu-FgiGxg&t=74s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'qwPhoKG3HJM',
                       'title': 'Best Call Tracking Software in 2026: Phone Calls Convert 15x Better',
                       'channel': 'CloudTalk',
                       'author': 'CloudTalk',
                       'text': "They've shaken things up with a pay-per-answered call model. They don't "
                               'care if the call lasts two minutes or twenty minutes, you pay for the '
                               'outcome, the answered call.',
                       'tip': "They've shaken things up with a pay-per-answered call model. They don't "
                              'care if the call lasts two minutes or twenty minutes, you pay for the '
                              'outcome, the answered call.',
                       'timestamp': 140,
                       'timestamp_seconds': 140,
                       'timestamp_label': '[00:02:20]',
                       'url': 'https://www.youtube.com/watch?v=qwPhoKG3HJM&t=140s',
                       'markdown': '[00:02:20](https://www.youtube.com/watch?v=qwPhoKG3HJM&t=140s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ytuZI-5RwoI',
                       'title': 'Pay Per Call Routing Explained (Part 2)',
                       'channel': 'Ringba',
                       'author': 'Ringba',
                       'text': "You need to be sure that there's an agent somewhere that's gonna answer "
                               'it.',
                       'tip': "You need to be sure that there's an agent somewhere that's gonna answer it.",
                       'timestamp': 60,
                       'timestamp_seconds': 60,
                       'timestamp_label': '[00:01:00]',
                       'url': 'https://www.youtube.com/watch?v=ytuZI-5RwoI&t=60s',
                       'markdown': '[00:01:00](https://www.youtube.com/watch?v=ytuZI-5RwoI&t=60s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'IPh2uXrQS1A',
                       'title': 'The Value of Call Tracking and Conversational Analytics | Invoca '
                                'Testimonials',
                       'channel': 'Invoca',
                       'author': 'Invoca',
                       'text': "Invoca has led us to a 33 percent gain in efficiency so we've been able to "
                               'cut a lot of wasted ad spend and put that money to work in better areas.',
                       'tip': "Invoca has led us to a 33 percent gain in efficiency so we've been able to "
                              'cut a lot of wasted ad spend and put that money to work in better areas.',
                       'timestamp': 57,
                       'timestamp_seconds': 57,
                       'timestamp_label': '[00:00:57]',
                       'url': 'https://www.youtube.com/watch?v=IPh2uXrQS1A&t=57s',
                       'markdown': '[00:00:57](https://www.youtube.com/watch?v=IPh2uXrQS1A&t=57s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'wr6G-Sojm50',
                       'title': 'Call Tracking Attribution with CallPOP',
                       'channel': 'CallPOP',
                       'author': 'CallPOP',
                       'text': 'We achieve that objective by providing a unique tracking number for each '
                               'different marketing source or lead acquisition channel that you want to '
                               'measure.',
                       'tip': 'We achieve that objective by providing a unique tracking number for each '
                              'different marketing source or lead acquisition channel that you want to '
                              'measure.',
                       'timestamp': 20,
                       'timestamp_seconds': 20,
                       'timestamp_label': '[00:00:20]',
                       'url': 'https://www.youtube.com/watch?v=wr6G-Sojm50&t=20s',
                       'markdown': '[00:00:20](https://www.youtube.com/watch?v=wr6G-Sojm50&t=20s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'bJeLdEIwej8',
                       'title': 'Track and attribute calls using dynamic phone numbers',
                       'channel': 'Invoca',
                       'author': 'Invoca',
                       'text': 'If you know that customers typically call within 30 minutes of visiting '
                               'your page, you can safely reuse that uncalled number after 30 minutes, '
                               'exposing it to a new site visitor.',
                       'tip': 'If you know that customers typically call within 30 minutes of visiting '
                              'your page, you can safely reuse that uncalled number after 30 minutes, '
                              'exposing it to a new site visitor.',
                       'timestamp': 163,
                       'timestamp_seconds': 163,
                       'timestamp_label': '[00:02:43]',
                       'url': 'https://www.youtube.com/watch?v=bJeLdEIwej8&t=163s',
                       'markdown': '[00:02:43](https://www.youtube.com/watch?v=bJeLdEIwej8&t=163s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'eH4764v8-74',
                       'title': 'How Does Call Tracking Work?',
                       'channel': 'Travis Wilkie',
                       'author': 'Travis Wilkie',
                       'text': "They're going to put a unique phone number on the landing page or the "
                               'website for each person who visits the website.',
                       'tip': "They're going to put a unique phone number on the landing page or the "
                              'website for each person who visits the website.',
                       'timestamp': 139,
                       'timestamp_seconds': 139,
                       'timestamp_label': '[00:02:19]',
                       'url': 'https://www.youtube.com/watch?v=eH4764v8-74&t=139s',
                       'markdown': '[00:02:19](https://www.youtube.com/watch?v=eH4764v8-74&t=139s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'}]}
