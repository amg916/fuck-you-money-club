from __future__ import annotations

CHAPTER_3 = {'id': 'Q3',
 'chapter_id': 'Q3',
 'chapter_number': 3,
 'question_number': 3,
 'slug': 'ivr-design-call-flows-pre-qualify-callers',
 'question_prompt': 'How do I build IVRs and call flows that pre-qualify callers before they reach a '
                    'buyer?',
 'kicker': 'Q3 / THE BIG MONEY PLAYBOOKS',
 'title': 'IVR Design and Call Flows That Pre-Qualify Callers',
 'subtitle': 'How IVR works, Ringba IVR, Dial IVR and call flows, profitable call-flow builds, quiz-funnel '
             'pre-qualification, visual flow builders (SignalWire, WildJar, RingCentral, Autocia), IVR '
             'best practices, Retell AI inbound webhooks, and GoHighLevel inbound routing',
 'layout_template': 'financial_analysis',
 'reading_time_minutes': 15,
 'executive_summary': 'Practitioners from Ringba, Landerlab, SignalWire, WildJar, GetVoIP and independent '
                      'operators agree on one rule: the IVR is a qualification gate that sorts callers on '
                      "the attribute that decides payout before any buyer phone rings. Ringba's debt "
                      'example forwards only callers with more than $10,000 in unsecured credit card debt. '
                      "Carlos Corona's ACA flow routes uninsured callers into RTB and re-asks anyone who "
                      'claims coverage, because many callers press the wrong key the first time. Corona '
                      'does not monetize non-qualified Medicare and Medicaid callers as calls. He converts '
                      'them into an IVR SMS opt-in, and the opt-in webhook carries the call UUID, the '
                      'E.164 number, the campaign and the state. Landerlab pushes quiz answers such as '
                      'carrier into Ringba URL parameters so router filters can use them. Practitioners '
                      'disagree on two points. The first is whether to route mismatched callers to '
                      'adjacent buyers, which Corona says breeds complaints. The second is whether to use '
                      'audible menus or silent background IVR functions.',
 'key_metrics': [{'label': 'Debt Campaign IVR Qualification Threshold',
                  'metric': 'Debt Campaign IVR Qualification Threshold',
                  'value': 'More than $10,000 in unsecured credit card debt (press 1 = qualified, press 2 '
                           '= not qualified)',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Jordan Soto's example of an IVR call flow where only the press-1 caller is "
                             'forwarded to the buyer and the affiliate earns credit.',
                  'source': 'Ringba ([4dnXkZ7u6zw @ 00:00:51])'},
                 {'label': 'Inbound Call Webhook Timeout and Retries',
                  'metric': 'Inbound Call Webhook Timeout and Retries',
                  'value': '10-second timeout, retried up to 3 times, then falls back to the default agent',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Henryk Brzozowski's test of the Retell AI inbound webhook. When make.com "
                             'returns nothing, the call uses the agent already set on the number.',
                  'source': 'Henryk Brzozowski ([p7WavoW_6to @ 00:04:24])'},
                 {'label': 'Gather Failure Disconnect Rule',
                  'metric': 'Gather Failure Disconnect Rule',
                  'value': 'Disconnect after 2 failed attempts (timeout or unknown input)',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Nicholas at SignalWire increments an attempt variable on each gather '
                             'failure. The flow loops the caller back once with an audio cue, then hangs '
                             'up.',
                  'source': 'SignalWire ([VByuomL6T0s @ 00:05:14])'},
                 {'label': 'Maximum Options Per IVR Menu',
                  'metric': 'Maximum Options Per IVR Menu',
                  'value': 'Limit each menu to 5 options, most common items listed first',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Nate at GetVoIP gives this as a best practice so inbound callers can '
                             'identify their path instantly and select the DTMF option.',
                  'source': 'GetVoIP - Simplify your search ([7vsOEhARsdU @ 00:02:23])'}],
 'sections': [{'title': 'The Practitioner Consensus: Qualify Before the Buyer Ever Rings',
               'paragraphs': ['Every builder in this chapter treats the IVR as a qualification gate, not a '
                              'greeting. Ringba defines interactive voice response as an automated system '
                              'for qualifying callers with prompts and routing them to a destination based '
                              'on their responses. It splits campaign routing into two modes. Standard '
                              'routing sends calls to targets by priority and weight. IVR routing pushes '
                              'callers into a node tree that hands off to a routing plan at the IVR level '
                              '[Vd_ZoE2BRqQ @ 00:00:01] [Vd_ZoE2BRqQ @ 00:00:19]. Jordan Soto lays out the '
                              'pay-per-call version plainly with a debt campaign. The caller is asked '
                              'whether they carry more than ten thousand dollars in unsecured credit card '
                              'debt. Pressing one means qualified, and the call is forwarded to the buyer. '
                              'Pressing two means not qualified. Only the qualified leg earns the '
                              'affiliate the commission [4dnXkZ7u6zw @ 00:00:51]. Carlos Corona runs the '
                              'same logic on ACA traffic. A coverage question plays up front, and callers '
                              'without Medicaid, Medicare, or employer coverage go straight into the RTB '
                              'process against the buyers on that routing plan [tf4AieS7Mhc @ 00:00:45]. '
                              "The shared premise is that a buyer's phone should ring only after the "
                              'caller has already sorted themselves on the one or two attributes that '
                              'decide payout. Any call that reaches a buyer without that sort is a call '
                              'the publisher is gambling on rather than selling.',
                              'Pre-qualification does not have to start at the keypad. Landerlab says '
                              'anyone running pay-per-call to big auto insurance brands such as Allstate '
                              'or Geico has to pre-qualify visitors before sending them to a buyer. Its '
                              "build is a quiz funnel that asks for the visitor's current carrier and "
                              'homeowner status. Those answers are then pushed into Ringba, where the call '
                              'flow routes on them and filters exclusive buyers on homeowner or insured '
                              'status [DMS29IlU8pE @ 00:00:01]. CallCentreHelper describes the silent side '
                              'of an IVR. Some contact centers never want callers to hear a traditional '
                              'menu at all. They still run background modules that connect into back-end '
                              'systems and identify the caller from the number they display [8f7qA0z-AgQ @ '
                              '00:01:31]. Calilio and GetVoIP both stress the payoff of collecting context '
                              'before the transfer. The agent who answers already knows what the caller '
                              'needs instead of going in blind [KT-Jaz-hayQ @ 00:00:21] [U9IWvkKvtWE @ '
                              '00:01:08]. For an arbitrage operator the translation is direct. The '
                              'qualifying data can come from a landing-page quiz, a keypad press, or a '
                              'caller-ID lookup. Either way, it has to land on the call record before the '
                              'routing decision is made. That is the only way to filter buyers on carrier, '
                              'homeowner, or insured status instead of handing them whoever happens to '
                              'dial in.',
                              "The builders also agree on construction order and flow hygiene. Ringba's "
                              'training says that before you can create a call flow, you need a routing '
                              'plan configured. The dial node at the end of the tree needs a destination '
                              "to hand callers to [Ua5XxaPrhRs @ 00:01:05]. Ringba's IVR builder then "
                              'refuses to save a tree missing a validation node. The error is outlined in '
                              'red until a hang-up node catches calls that fail to connect to the routing '
                              "plan [Vd_ZoE2BRqQ @ 00:02:22]. WildJar's James hits the same wall in his "
                              'demo. Saving fails, and red lines appear around any transfer that has no '
                              'target number configured. The flow stays broken until every branch has a '
                              "place to dial [5z0mahGmR40 @ 00:01:53]. GetVoIP's Nate pushes menu "
                              'discipline on top of that structure. His rules are to use a drag-and-drop '
                              'builder, keep the phrasing concise, cap each menu at five options, and list '
                              'the most common items first so most callers recognize their path '
                              'immediately [7vsOEhARsdU @ 00:02:23]. Put together, the consensus template '
                              'has four parts: a short qualifying question asked up front, a hard '
                              'qualified branch to the buyer, a defined branch for non-qualified callers, '
                              'and no dangling node anywhere. Every vendor demo, from Ringba to WildJar, '
                              'blocks publishing on an open end. That block is the cheapest quality '
                              'control an operator gets.'],
               'table': {'caption': 'Where the practitioners line up on IVR pre-qualification for inbound '
                                    'call traffic',
                         'headers': ['Consensus Point',
                                     'What Practitioners Actually Do',
                                     'Why It Matters for Call Buyers',
                                     'Expert Source'],
                         'rows': [['The IVR acts as a caller qualification gate',
                                   'Prompts collect caller responses and route each caller to a '
                                   'destination based on what they answered',
                                   'Unqualified callers are filtered out before any buyer target ever '
                                   'rings',
                                   'Ringba ([Vd_ZoE2BRqQ @ 00:00:01])'],
                                  ['Ask one binary question on the payout attribute',
                                   'The caller presses one if they have more than ten thousand dollars of '
                                   'unsecured debt and two if they do not',
                                   'Only press-one calls are forwarded, and only those calls earn the '
                                   'affiliate commission',
                                   'Ringba ([4dnXkZ7u6zw @ 00:00:51])'],
                                  ["Gather the caller's context before the transfer",
                                   'The automated menu captures what the caller needs before they reach a '
                                   'live agent',
                                   'The answering agent already holds the context required to handle the '
                                   'caller',
                                   'Calilio ([KT-Jaz-hayQ @ 00:00:21])'],
                                  ['Pre-qualify on the landing page with a quiz',
                                   'The quiz captures carrier and homeowner status and pushes both into '
                                   'the call software',
                                   'Exclusive auto insurance buyers can then be filtered on those stated '
                                   'conditions',
                                   'Landerlab ([DMS29IlU8pE @ 00:16:17])'],
                                  ['Configure the routing plan before building the flow',
                                   'Create the routing plan first so the dial node has a destination for '
                                   'callers',
                                   'Without a routing plan, the call flow cannot send any qualified '
                                   'traffic onward',
                                   'Ringba ([Ua5XxaPrhRs @ 00:01:05])'],
                                  ['Never leave an unconfigured transfer node in the flow',
                                   'Saving fails, with red outlines, until every transfer has a target '
                                   'number',
                                   'Broken branches are caught before live paid traffic hits a dead end',
                                   'WildJar Call Intelligence ([5z0mahGmR40 @ 00:01:53])'],
                                  ['Keep each menu short with common options first',
                                   'Limit each menu to five options, with concise phrasing and the most '
                                   'common items leading',
                                   'Most callers pick the right DTMF option on their very first listen',
                                   'GetVoIP - Simplify your search ([7vsOEhARsdU @ 00:02:23])']]}},
              {'title': 'Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ["Carlos Corona's ACA flow is the most complete pay-per-call build in this "
                              'chapter, and it runs on two keypad prompts. The opening message reads: We '
                              'are one step closer to getting you approved for help with gas, groceries, '
                              'and rent. Please press two if you do not have Medicare, Medicaid, or '
                              'employer coverage. Please press one if you do have it. A press of two '
                              'qualifies the caller and kicks off the RTB process to the buyers on the '
                              'routing plan [tf4AieS7Mhc @ 00:01:22]. A press of one does not end the '
                              'call. Corona replays a longer version that opens with: please listen '
                              'carefully as our menu has changed. The replay splits into one for Medicaid, '
                              'two for Medicare, and three for no government health benefits, and a press '
                              'of three routes back to the buyers [tf4AieS7Mhc @ 00:01:55]. His reason '
                              'comes straight from live traffic. A lot of people press something that was '
                              'not the correct answer, and the second pass gives them another chance to '
                              "make the right choice [tf4AieS7Mhc @ 00:02:30]. SignalWire's Nicholas "
                              'builds the same safety net generically. An attempt variable increments each '
                              'time the gather times out or receives unknown input. A short audio cue '
                              'plays before the caller loops back to the prompt. After two failed '
                              'attempts, the flow disconnects the call [VByuomL6T0s @ 00:05:14].',
                              'Corona treats callers who confirm Medicaid or Medicare as no-value calls. '
                              'Instead of hanging up on them, he converts them into an SMS opt-in. He '
                              'builds a gather that accepts only a press of one. He lists the elements an '
                              'IVR consent has to carry: the brand name, how to opt out, where to see the '
                              'terms, and that message rates apply [tf4AieS7Mhc @ 00:05:10]. His live '
                              'script reads: Thank you for calling Medicare benefits. All agents are busy. '
                              'Press one to complete your request via text. By pressing one, you agree to '
                              'automated texts. To opt out, reply stop. Message rates apply. For terms, '
                              'visit medicarebenefits.net/terms [tf4AieS7Mhc @ 00:06:06]. A press of one '
                              'fires a webhook with four fields: the inbound call UUID for reference if '
                              'issues come up, the phone number in E.164 format for later texting, a '
                              'campaign tag, and the state for time zones. The flow then dials a '
                              'confirmation routing plan whose target only plays a message-sent prompt, '
                              'and every dial records the entire call [tf4AieS7Mhc @ 00:08:44]. Henryk '
                              "Brzozowski's Retell AI setup shows the webhook limits operators must design "
                              'around. The timeout is 10 seconds, with up to three retries before a silent '
                              'fallback to the default agent. He also whitelists IPs so only Retell can '
                              'reach his make.com endpoint [p7WavoW_6to @ 00:04:24].',
                              "Ringba's node set is the toolkit most of these pay-per-call builds run on. "
                              'The dial node routes to a target, and the menu node decides on the key '
                              'pressed. The router node decides on filters, and the gather node collects '
                              'numerical input. The hours node routes on hours of operation, and the pixel '
                              'node fires pixels from inside the call flow. The JS node runs custom '
                              'JavaScript once the team activates it, and the profile node pulls enriched '
                              'caller data [Ua5XxaPrhRs @ 00:03:42]. The robocall verification template '
                              'asks every caller to press one to continue and automatically terminates '
                              'anything that cannot, so spam robocallers never reach targets [Ua5XxaPrhRs '
                              '@ 00:04:54]. On the buyer side, Shane Hitchcock explains Dial IVR. The '
                              "operator times how long a buyer's own IVR takes to ask for a keypress and "
                              'enters that timing. Ringba then sends the DTMF digit, or a dynamic tag such '
                              'as a zip code, without the caller hearing it [VQKxVnPn5zE @ 00:01:15]. '
                              "Landerlab's carrier routing connects the page to the flow in three steps. "
                              'First, create a URL parameter named carrier, with carrier as the report '
                              'name. Next, add a router whose filters read carrier equal to Allstate or '
                              'Geico, with a routing plan behind each one. Finally, place a live test call '
                              'and confirm the carrier tag shows up on the call log [DMS29IlU8pE @ '
                              '00:12:40].'],
               'table': {'caption': 'Exact IVR build settings, scripts, and numbers taught by the '
                                    'operators',
                         'headers': ['Build Element',
                                     'Exact Setting or Number',
                                     'How Operators Use It',
                                     'Expert Source'],
                         'rows': [['Second-chance re-ask menu for coverage',
                                   'The prompt opens with please listen carefully as our menu has changed, '
                                   'then offers three numbered options',
                                   'Callers who pressed the wrong key get a second chance, which recovers '
                                   'qualified calls',
                                   'Carlos Corona ([tf4AieS7Mhc @ 00:01:55])'],
                                  ['IVR SMS consent gather for no-value callers',
                                   'The script states the brand name, opt-out by replying stop, that '
                                   'message rates apply, and the terms URL, then asks for one',
                                   'No-value Medicare and Medicaid callers become textable opt-ins instead '
                                   'of hang-ups',
                                   'Carlos Corona ([tf4AieS7Mhc @ 00:05:10])'],
                                  ['Opt-in webhook payload fields sent onward',
                                   'Inbound call UUID, phone number in E.164 format, campaign tag, and '
                                   'caller state',
                                   'Supports dispute lookups, later text sends, campaign attribution, and '
                                   'time zone handling',
                                   'Carlos Corona ([tf4AieS7Mhc @ 00:08:27])'],
                                  ['Inbound call webhook reliability limits',
                                   'Ten-second timeout, up to three retries, then fallback to the default '
                                   'agent',
                                   'Keep the backend fast, or callers silently land on the default agent',
                                   'Henryk Brzozowski ([p7WavoW_6to @ 00:04:24])'],
                                  ['Gather error loop driven by an attempt variable',
                                   'The attempt variable increments on each timeout or unknown input, and '
                                   'the call disconnects after two failures',
                                   'Confused callers are looped back once while dead air is cut off '
                                   'cleanly',
                                   'SignalWire ([VByuomL6T0s @ 00:04:54])'],
                                  ["Dial IVR that bypasses the buyer's own IVR",
                                   'A timed delay, then a DTMF digit or a dynamic tag such as a zip code',
                                   "Callers reach the buyer's live agent faster without ever hearing the "
                                   'menu',
                                   'Ringba ([VQKxVnPn5zE @ 00:01:15])'],
                                  ['Quiz funnel pre-qualifier before the call',
                                   'A three-second loading screen, then a you qualify for 40% off call-now '
                                   'button with a countdown',
                                   'Builds urgency while carrier and homeowner answers flow into Ringba '
                                   'for routing',
                                   'Landerlab ([DMS29IlU8pE @ 00:04:21])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Small IVR tweaks the operators swear by',
                           'body': 'These come from live builds and test calls, not from vendor feature '
                                   'lists.',
                           'items': ['Mix different voices across IVR prompts. Corona found that people '
                                     'pay more attention when the voice changes, while a single voice lets '
                                     'them tune out [Carlos Corona — tf4AieS7Mhc @ 00:07:06].',
                                     'Treat buyer IVRs as conversion killers. Use Dial IVR to send DTMF '
                                     'tones in the background so callers skip menus they never needed to '
                                     'hear [Ringba — VQKxVnPn5zE @ 00:00:15].',
                                     'Preview the landing page and confirm the base number has been '
                                     'swapped. If the number is replaced, the Ringba number pool script is '
                                     'loading correctly [Landerlab — DMS29IlU8pE @ 00:10:33].',
                                     'Dynamic variable names must match exactly between the webhook '
                                     "response and the agent prompt, or the caller's name will not "
                                     'populate [Henryk Brzozowski — p7WavoW_6to @ 00:07:13].']},
               'sop_steps': [{'step': 1,
                              'title': 'Stand up the routing plan first',
                              'action': 'Create the routing plan and choose priority routing or RPC '
                                        'routing before building any call flow.',
                              'detail': 'Priority routing sends calls by priority and weight. RPC routing '
                                        "sends calls by a target's revenue and historical performance. "
                                        'Then set how each target counts conversions, its revenue amount, '
                                        'and how duplicate conversions are handled [Ringba — Ua5XxaPrhRs @ '
                                        '00:01:24].'},
                             {'step': 2,
                              'title': 'Front-load the payout qualifier with a re-ask',
                              'action': 'Open the flow with a coverage or eligibility gather, send '
                                        'qualified presses to RTB, and replay a longer menu to callers who '
                                        'answer the other way.',
                              'detail': "Corona's longer replay starts with please listen carefully as our "
                                        'menu has changed. It splits Medicaid, Medicare, and no coverage '
                                        'onto separate keys, so callers who pressed the wrong key get a '
                                        'second chance [Carlos Corona — tf4AieS7Mhc @ 00:01:55].'},
                             {'step': 3,
                              'title': 'Add an error loop and close every node',
                              'action': 'Increment an attempt variable on timeouts and unknown input, loop '
                                        'back once with an audio cue, and end in hang-up or voicemail.',
                              'detail': 'Nicholas disconnects after two failed attempts. He ties off the '
                                        'remaining error paths with stop recording, an apology played '
                                        'through TTS, a voicemail recording, and a hang-up [SignalWire — '
                                        'VByuomL6T0s @ 00:05:14].'},
                             {'step': 4,
                              'title': 'Convert no-value callers into SMS opt-ins',
                              'action': 'Route non-qualified callers to a press-one consent gather, fire a '
                                        'webhook, and dial a recorded confirmation routing plan.',
                              'detail': 'The webhook passes the inbound call UUID, the E.164 phone number, '
                                        'the campaign tag, and the state. Every dial should record the '
                                        'entire call for later reference [Carlos Corona — tf4AieS7Mhc @ '
                                        '00:08:27].'}]},
              {'heading': 'Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The sharpest split is whether the caller should ever hear a qualifying '
                              'menu. Carlos Corona builds the ACA flow around one: the inbound call plays '
                              'a message asking whether the caller has Medicaid, Medicare, employer '
                              'coverage or no insurance, and only the no-insurance press triggers the RTB '
                              'hunt across the buyers under that routing plan [tf4AieS7Mhc @ 00:00:30]. '
                              "Ringba's own walkthrough of the three core flows frames the audible IVR the "
                              'same way, using a debt example where callers with more than ten thousand '
                              'dollars in unsecured credit card debt press one and everyone else presses '
                              'two and falls out [4dnXkZ7u6zw @ 00:00:51]. Shane Hitchcock at Ringba '
                              'argues the opposite side of the wire: IVRs can be conversion killers for '
                              "any call campaign, so Ringba's Dial IVR uses software and DTMF tones to "
                              "bypass a buyer's unnecessary menus without the customer ever hearing it, "
                              'timing how long the prompt takes and injecting a press one or even a zip '
                              'code tag [VQKxVnPn5zE @ 00:00:15]. CallCentreHelper adds that some contact '
                              'centers refuse a traditional audible IVR entirely yet still run its silent '
                              'functions, connecting to back-end systems and identifying the caller from '
                              'the displayed telephone number [8f7qA0z-AgQ @ 00:01:31]. The operator '
                              "choice is screening friction on your side versus raw speed into the buyer's "
                              'live agent.',
                              'A second fork is where qualification data gets captured in the first place. '
                              'Landerlab skips the keypad and qualifies on the landing page: a quiz asks '
                              'the current insurance carrier and homeowner status, injects the Ringba '
                              'number pool script, pushes the carrier value into a URL parameter, and a '
                              'router node with filters sends Allstate and Geico callers to separate '
                              "routing plans [DMS29IlU8pE @ 00:12:18]. Ringba's warm transfer model puts a "
                              'human in that seat instead, where a qualifying call center agent asks a '
                              'list of questions before handing off, and the conversion event typically '
                              'lands on the transfer [4dnXkZ7u6zw @ 00:01:24]. Henryk Brzozowski routes '
                              'before any agent speaks, using a Retell AI inbound webhook to make.com that '
                              'checks the current time and the caller number, then returns a day agent '
                              'armed with a transfer tool or a night agent stripped of it [p7WavoW_6to @ '
                              '00:01:31]. On the voice-versus-keypad question, Calilio pitches NLP systems '
                              'that open with how can I help you today and route on full sentences rather '
                              'than press one prompts, a direct challenge to the DTMF menus every '
                              'pay-per-call builder here still relies on [KT-Jaz-hayQ @ 00:02:02]. Each '
                              'choice moves the filter to a different layer of the stack, with different '
                              'costs.',
                              'Practitioners also split hard on what to do with callers who fail the '
                              'screen. Carlos Corona notes some publishers push Medicare callers to '
                              'Medicare buyers, and strongly discourages it because the ad angle is ACA, '
                              'the caller references that ad once on the phone with the agent, and the '
                              'mismatch breeds complaints; the alternative playbook is an IVR SMS consent '
                              'gather that names the brand, the opt-out, the terms page and message rates, '
                              'then fires a webhook so the caller can be monetized by text with another '
                              'offer [tf4AieS7Mhc @ 00:03:55]. Routing logic splits too: Ringba offers '
                              "priority routing by priority and weight, or RPC routing by a target's "
                              'revenue and historical performance [Ua5XxaPrhRs @ 00:01:24]. For the '
                              'call-back side, the GoHighLevel for Commercial Real Estate operator calls '
                              'it personal preference with no right or wrong answer, weighing direct '
                              'connect to a cell phone, which gives a real-time call back but zero prep '
                              'time, against an IVR offering press one to book an appointment or press two '
                              'for a call back [7GRJx9A5y5c @ 00:00:33]. GetVoIP pushes a different menu '
                              'philosophy entirely: limit each menu to five options and let callers reach '
                              'an agent at any time [7vsOEhARsdU @ 00:02:07]. Pick the policy that matches '
                              'whether you sell every call or only the clean ones.'],
               'table': {'caption': 'Competing IVR and call flow playbooks for pre-qualifying pay-per-call '
                                    'traffic',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Audible screen versus buyer IVR bypass',
                                   'Play a coverage question and route only the no-insurance press to '
                                   'buyers',
                                   'Use Dial IVR DTMF tones to skip buyer menus unheard by the caller',
                                   'Carlos Corona ([tf4AieS7Mhc @ 00:00:30]); Ringba ([VQKxVnPn5zE @ '
                                   '00:00:15])'],
                                  ['Where to capture the qualifying data',
                                   'Quiz funnel pushes carrier and homeowner answers into Ringba URL '
                                   'parameters',
                                   'Warm transfer qualifying call center asks a question list before '
                                   'handoff',
                                   'Landerlab ([DMS29IlU8pE @ 00:11:28]); Ringba ([4dnXkZ7u6zw @ '
                                   '00:01:24])'],
                                  ['Keypad input versus natural language input',
                                   'DTMF keypad presses mapped to each menu option by tone frequency',
                                   'NLP IVR asks how can I help you today and routes on sentences',
                                   'CallCentreHelper ([8f7qA0z-AgQ @ 00:00:19]); Calilio ([KT-Jaz-hayQ @ '
                                   '00:02:02])'],
                                  ['Handling callers who fail the screen',
                                   'Send Medicare callers to Medicare buyers, which Corona says draws '
                                   'complaints',
                                   'Gather SMS consent and monetize the caller later with a text offer',
                                   'Carlos Corona ([tf4AieS7Mhc @ 00:03:08])'],
                                  ['Routing plan logic for buyer targets',
                                   'Priority routing distributes calls by assigned priority and weight per '
                                   'target',
                                   'RPC routing picks targets by revenue and historical performance data',
                                   'Ringba ([Ua5XxaPrhRs @ 00:01:24])'],
                                  ['Time-of-day handling for inbound calls',
                                   'Make.com webhook checks the time and swaps day and night AI agents',
                                   'Assign different IVR flows Monday to Saturday versus after office '
                                   'hours',
                                   'Henryk Brzozowski ([p7WavoW_6to @ 00:01:31]); Autocia Technologies '
                                   '([tdZ944Oycuo @ 00:03:53])'],
                                  ['Ring strategy when transferring to a group',
                                   'Sequential, parallel, round robin, or sticky agent policies inside one '
                                   'group',
                                   'Forward to mixed PSTN numbers and SIP endpoints sequentially or '
                                   'simultaneously',
                                   'Autocia Technologies ([tdZ944Oycuo @ 00:10:35]); SignalWire '
                                   '([VByuomL6T0s @ 00:03:47])']]}},
              {'heading': 'Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The most expensive trap Carlos Corona reports is trusting the first '
                              'keypress. Testing showed a lot of callers press something that is not the '
                              'correct answer, so a press one for coverage triggers a second, longer menu '
                              'that opens with please listen carefully as our menu has changed and splits '
                              'Medicaid, Medicare and no government benefits into separate keys before a '
                              'call is written off [tf4AieS7Mhc @ 00:02:13]. Corona also found callers '
                              'tune out a single voice, and swapping voices across prompts keeps them '
                              'alert, a finding credited to plain testing [tf4AieS7Mhc @ 00:07:06]. Spam '
                              "is the other leak: Ringba's robocall verification template plays a "
                              'text-to-speech press one to continue, and any robocaller unable to complete '
                              'it has the call automatically terminated before it ever reaches a target '
                              "[Ua5XxaPrhRs @ 00:04:54]. SignalWire's Nicholas handles callers who time "
                              'out or hit an unknown input with a set variables module that increments an '
                              'attempt counter, plays an audio file confirming something went awry, loops '
                              'back to the gather, and disconnects after two failed attempts [VByuomL6T0s '
                              '@ 00:04:54]. Without that loop, confused callers either get dumped or route '
                              'blind, and both outcomes burn paid traffic.',
                              "Build errors stall launches more often than strategy does. Ringba's IVR "
                              'builder refuses to save a tree that lacks a hang-up node for calls that '
                              'fail to connect to the routing plan, marking the error in red on the node '
                              "[Vd_ZoE2BRqQ @ 00:02:22]. WildJar's James hit the same wall live: the save "
                              'failed with red lines around both transfers because no target number had '
                              "been configured for sales or support [5z0mahGmR40 @ 00:01:53]. Landerlab's "
                              'call flow threw publish errors until each router branch had a routing plan '
                              'selected, and the team verified the number pool script by checking that the '
                              'base number on the page was replaced by a Ringba pool number before running '
                              'a live mobile test and reading the carrier tag in the call log [DMS29IlU8pE '
                              '@ 00:10:33]. Webhook routing carries its own failure state: Henryk '
                              'Brzozowski found the Retell inbound webhook has a ten-second timeout, '
                              'retries up to three times, and then defaults to the agent already set on '
                              'the number, so a slow make.com scenario lands callers on that fallback '
                              'agent; the dynamic variable name must also match exactly, and the webhook '
                              'was locked down by whitelisting the Retell IP [p7WavoW_6to @ 00:04:24]. '
                              'Test every branch end to end before buying traffic.',
                              'Economics leaks show up after the build, not during it. Autocia '
                              "Technologies' Sanya warns that channels cap concurrent calls: five channels "
                              'means five people can call together without anyone getting a busy tone, and '
                              'the dashboard tracks answered, not answered and canceled calls plus answer '
                              'rate per number [tdZ944Oycuo @ 00:02:28]. Missed calls need a recovery '
                              'path, so WildJar routes unanswered transfers to voicemail with an instant '
                              'missed-lead email and SMS alert to the sales team [5z0mahGmR40 @ 00:03:32]. '
                              'The GoHighLevel for Commercial Real Estate operator sets the system to '
                              'notify the agent whenever a caller hangs up without booking or requesting a '
                              'call back, and calls direct connect a lost opportunity when the phone rings '
                              'mid-tour or at a closing with zero prep time [7GRJx9A5y5c @ 00:03:15]. '
                              "Carlos Corona's opt-in webhook passes the inbound call UUID, the E.164 "
                              'phone number, the campaign tag and the state, so any issue can be traced '
                              'back to how the caller opted in; the flow then dials a confirmation routing '
                              'plan that plays a your message has been sent message, and every dial '
                              'records the entire call [tf4AieS7Mhc @ 00:08:27]. Skip any of these and '
                              'paid calls die unbilled or untraceable.'],
               'table': {'caption': 'Firsthand IVR failure modes and the fixes practitioners deployed',
                         'headers': ['Failure Mode',
                                     'What Happened',
                                     'Fix Practitioners Used',
                                     'Expert Source'],
                         'rows': [['Wrong first keypress from real callers',
                                   'Callers pressed an answer that was not correct for their coverage',
                                   'Replay a longer please listen carefully menu with three distinct keys',
                                   'Carlos Corona ([tf4AieS7Mhc @ 00:02:13])'],
                                  ['Mismatched buyer routing for failed screens',
                                   'Medicare callers sent to Medicare buyers referenced the ACA ad and '
                                   'complained',
                                   'Capture SMS consent and monetize later with a matching text offer',
                                   'Carlos Corona ([tf4AieS7Mhc @ 00:03:36])'],
                                  ['Robocall spam reaching paying targets',
                                   'Automated robocallers would otherwise route straight through to buyer '
                                   'targets',
                                   'Robocall verification template terminates callers who cannot press one',
                                   'Ringba ([Ua5XxaPrhRs @ 00:04:54])'],
                                  ['Missing validation node in the tree',
                                   'IVR tree could not save and the node was outlined in red',
                                   'Add a hang-up node for calls that fail to connect',
                                   'Ringba ([Vd_ZoE2BRqQ @ 00:02:22])'],
                                  ['Unconfigured transfer destinations in the flow',
                                   'Call flow save failed with red lines around both transfer nodes',
                                   'Enter target numbers for sales and support, then save again',
                                   'WildJar Call Intelligence ([5z0mahGmR40 @ 00:01:53])'],
                                  ['Inbound webhook timeout on AI routing',
                                   'Retell webhook times out after ten seconds and retries three times',
                                   'Fallback agent on the number answers, so keep the scenario fast',
                                   'Henryk Brzozowski ([p7WavoW_6to @ 00:04:24])'],
                                  ['Endless invalid input inside the gather',
                                   'Callers time out or press unknown keys inside the gather menu',
                                   'Increment an attempt variable and disconnect after two failed attempts',
                                   'SignalWire ([VByuomL6T0s @ 00:05:14])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Four checks before a single paid call hits the flow',
                           'body': 'Every item below is a pitfall a practitioner hit or warned about '
                                   'firsthand while building pre-qualifying IVRs and call flows.',
                           'items': ['Do not dump failed-screen Medicare callers on Medicare buyers off an '
                                     'ACA ad; Corona says it works for days or weeks before complaints '
                                     'arrive [Carlos Corona — tf4AieS7Mhc @ 00:03:55].',
                                     'Confirm the Ringba number pool replaced the base number on the '
                                     'landing page, then place a live mobile test and check the carrier '
                                     'tag in the call log [Landerlab — DMS29IlU8pE @ 00:10:33].',
                                     'Every IVR tree needs a hang-up node on the failed-connection path or '
                                     'it will not validate and save [Ringba — Vd_ZoE2BRqQ @ 00:02:22].',
                                     'Webhook routers must answer inside ten seconds or Retell retries and '
                                     'then falls back to the default agent on the number [Henryk '
                                     'Brzozowski — p7WavoW_6to @ 00:04:24].']}}],
 'pull_quote': '"IVRs can be conversion killers for any call campaign." — Ringba (VQKxVnPn5zE @ 00:00:15)',
 'diagram_id': 'diag-03',
 'action_checklist': ['Create the routing plan before the call flow, choosing priority routing by priority '
                      'and weight or RPC routing by target revenue and historical performance [Ringba — '
                      'Ua5XxaPrhRs @ 00:01:24].',
                      'Open the flow with a coverage qualifier and send only the qualified keypress into '
                      'the buyer routing plan to start the RTB process [Carlos Corona — tf4AieS7Mhc @ '
                      '00:00:45].',
                      'Replay a longer please listen carefully menu to callers who press a non-qualifying '
                      'key, giving them a second chance to answer correctly [Carlos Corona — tf4AieS7Mhc @ '
                      '00:01:55].',
                      'Layer the robocall verification template so callers who cannot press a key to '
                      'continue are terminated before reaching targets [Ringba — Ua5XxaPrhRs @ 00:04:54].',
                      'Push quiz funnel answers such as carrier into a Ringba URL parameter and route with '
                      'router node filters to buyer-specific routing plans [Landerlab — DMS29IlU8pE @ '
                      '00:12:18].',
                      'Time how long the buyer IVR takes to ask for a press and enter it in Dial IVR, '
                      'swapping in tags like zip codes where needed [Ringba — VQKxVnPn5zE @ 00:01:15].'],
 'statutory_citations': [{'title': 'Carlos Corona — How to set up a profitable Ringba call flow that '
                                   'converts [00:02:30]',
                          'url': 'https://www.youtube.com/watch?v=tf4AieS7Mhc&t=150s',
                          'relevance': 'Primary practitioner testimony on re-asking misfiring callers, '
                                       'avoiding mismatched buyer routing, and IVR SMS opt-in '
                                       'monetization.'},
                         {'title': 'Ringba — Ringba Product Training: Dial IVR [00:00:15]',
                          'url': 'https://www.youtube.com/watch?v=VQKxVnPn5zE&t=15s',
                          'relevance': 'Primary practitioner testimony on bypassing buyer IVRs with DTMF '
                                       'tones to protect conversion rates.'},
                         {'title': 'Landerlab — We Built a Pay Per Call Quiz Funnel That Drives Quality '
                                   'Calls (Watch This Ringba Setup!) [00:12:18]',
                          'url': 'https://www.youtube.com/watch?v=DMS29IlU8pE&t=738s',
                          'relevance': 'Primary practitioner testimony on pre-qualifying on the landing '
                                       'page and routing by carrier with Ringba router filters.'},
                         {'title': 'Ringba — Using Call Flows | Ringba Platform Training [00:04:54]',
                          'url': 'https://www.youtube.com/watch?v=Ua5XxaPrhRs&t=294s',
                          'relevance': 'Primary practitioner testimony on call flow nodes, routing types, '
                                       'and robocall verification filtering.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'DMS29IlU8pE',
                       'title': 'We Built a Pay Per Call Quiz Funnel That Drives Quality Calls (Watch This '
                                'Ringba Setup!)',
                       'channel': 'Landerlab',
                       'author': 'Landerlab',
                       'text': 'This comes in handy when you are doing auto insurance pay per calls and '
                               'you have more than one exclusive buyer and you want them to be filtered '
                               'out based on some conditions such as if the visitor is a home owner or '
                               'not.',
                       'tip': 'This comes in handy when you are doing auto insurance pay per calls and you '
                              'have more than one exclusive buyer and you want them to be filtered out '
                              'based on some conditions such as if the visitor is a home owner or not.',
                       'timestamp': 977,
                       'timestamp_seconds': 977,
                       'timestamp_label': '[00:16:17]',
                       'url': 'https://www.youtube.com/watch?v=DMS29IlU8pE&t=977s',
                       'markdown': '[00:16:17](https://www.youtube.com/watch?v=DMS29IlU8pE&t=977s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Vd_ZoE2BRqQ',
                       'title': 'Interactive Voice Response | Ringba Call Tracking & Analytics',
                       'channel': 'Ringba',
                       'author': 'Ringba',
                       'text': 'An IVR or interactive voice response is an automated system for qualifying '
                               'callers with prompts and routing them to a destination based on their '
                               'responses.',
                       'tip': 'An IVR or interactive voice response is an automated system for qualifying '
                              'callers with prompts and routing them to a destination based on their '
                              'responses.',
                       'timestamp': 1,
                       'timestamp_seconds': 1,
                       'timestamp_label': '[00:00:01]',
                       'url': 'https://www.youtube.com/watch?v=Vd_ZoE2BRqQ&t=1s',
                       'markdown': '[00:00:01](https://www.youtube.com/watch?v=Vd_ZoE2BRqQ&t=1s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Ua5XxaPrhRs',
                       'title': 'Using Call Flows | Ringba Platform Training',
                       'channel': 'Ringba',
                       'author': 'Ringba',
                       'text': 'The robocall verification template contains a simple menu that asks the '
                               'caller to press a key in order to continue, and a robocaller unable to '
                               'complete this verification will have the call automatically terminated.',
                       'tip': 'The robocall verification template contains a simple menu that asks the '
                              'caller to press a key in order to continue, and a robocaller unable to '
                              'complete this verification will have the call automatically terminated.',
                       'timestamp': 294,
                       'timestamp_seconds': 294,
                       'timestamp_label': '[00:04:54]',
                       'url': 'https://www.youtube.com/watch?v=Ua5XxaPrhRs&t=294s',
                       'markdown': '[00:04:54](https://www.youtube.com/watch?v=Ua5XxaPrhRs&t=294s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'KT-Jaz-hayQ',
                       'title': 'What is an IVR System | Interactive Voice Response and How Does It Work?',
                       'channel': 'Calilio',
                       'author': 'Calilio',
                       'text': 'Instead of telling callers to press a number, a smart IVR can ask how can '
                               'I help you today and then direct the call based on what the caller says.',
                       'tip': 'Instead of telling callers to press a number, a smart IVR can ask how can I '
                              'help you today and then direct the call based on what the caller says.',
                       'timestamp': 122,
                       'timestamp_seconds': 122,
                       'timestamp_label': '[00:02:02]',
                       'url': 'https://www.youtube.com/watch?v=KT-Jaz-hayQ&t=122s',
                       'markdown': '[00:02:02](https://www.youtube.com/watch?v=KT-Jaz-hayQ&t=122s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'VByuomL6T0s',
                       'title': 'Building an IVR - Call Flow Builder | SignalWire in Seconds Ep. 12',
                       'channel': 'SignalWire',
                       'author': 'SignalWire',
                       'text': "Using the conditions module, I'll tell my flow to disconnect the call "
                               'following two failed attempts.',
                       'tip': "Using the conditions module, I'll tell my flow to disconnect the call "
                              'following two failed attempts.',
                       'timestamp': 294,
                       'timestamp_seconds': 294,
                       'timestamp_label': '[00:04:54]',
                       'url': 'https://www.youtube.com/watch?v=VByuomL6T0s&t=294s',
                       'markdown': '[00:04:54](https://www.youtube.com/watch?v=VByuomL6T0s&t=294s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'VQKxVnPn5zE',
                       'title': 'Ringba Product Training: Dial IVR',
                       'channel': 'Ringba',
                       'author': 'Ringba',
                       'text': 'IVRs can be conversion killers for any call campaign, so at Ringba we use '
                               'software and DTMF tones to bypass unnecessary IVRs without the customer '
                               'ever hearing us do so.',
                       'tip': 'IVRs can be conversion killers for any call campaign, so at Ringba we use '
                              'software and DTMF tones to bypass unnecessary IVRs without the customer '
                              'ever hearing us do so.',
                       'timestamp': 15,
                       'timestamp_seconds': 15,
                       'timestamp_label': '[00:00:15]',
                       'url': 'https://www.youtube.com/watch?v=VQKxVnPn5zE&t=15s',
                       'markdown': '[00:00:15](https://www.youtube.com/watch?v=VQKxVnPn5zE&t=15s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '4dnXkZ7u6zw',
                       'title': '3 Call Flows You Need to Know',
                       'channel': 'Ringba',
                       'author': 'Ringba',
                       'text': "If it's a debt call and we're asking if the caller has more than ten "
                               'thousand dollars in unsecured credit card debt, if they have that they '
                               "press one, which means they're qualified.",
                       'tip': "If it's a debt call and we're asking if the caller has more than ten "
                              'thousand dollars in unsecured credit card debt, if they have that they '
                              "press one, which means they're qualified.",
                       'timestamp': 51,
                       'timestamp_seconds': 51,
                       'timestamp_label': '[00:00:51]',
                       'url': 'https://www.youtube.com/watch?v=4dnXkZ7u6zw&t=51s',
                       'markdown': '[00:00:51](https://www.youtube.com/watch?v=4dnXkZ7u6zw&t=51s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '8f7qA0z-AgQ',
                       'title': 'How Does an IVR Work?',
                       'channel': 'CallCentreHelper',
                       'author': 'CallCentreHelper',
                       'text': "For some types of contact centers they don't actually want the caller to "
                               'ever have what they consider to be a traditional IVR, but they may still '
                               'want some of the silent functions of an IVR.',
                       'tip': "For some types of contact centers they don't actually want the caller to "
                              'ever have what they consider to be a traditional IVR, but they may still '
                              'want some of the silent functions of an IVR.',
                       'timestamp': 91,
                       'timestamp_seconds': 91,
                       'timestamp_label': '[00:01:31]',
                       'url': 'https://www.youtube.com/watch?v=8f7qA0z-AgQ&t=91s',
                       'markdown': '[00:01:31](https://www.youtube.com/watch?v=8f7qA0z-AgQ&t=91s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'U9IWvkKvtWE',
                       'title': 'What is an IVR system & How it Works | Interactive Voice Response Systems '
                                'Explained',
                       'channel': 'GetVoIP - Simplify your search',
                       'author': 'GetVoIP - Simplify your search',
                       'text': 'IVRs can also collect information on the customer and their inquiry before '
                               "transferring the call so that the representative picking up isn't going in "
                               'blind.',
                       'tip': 'IVRs can also collect information on the customer and their inquiry before '
                              "transferring the call so that the representative picking up isn't going in "
                              'blind.',
                       'timestamp': 68,
                       'timestamp_seconds': 68,
                       'timestamp_label': '[00:01:08]',
                       'url': 'https://www.youtube.com/watch?v=U9IWvkKvtWE&t=68s',
                       'markdown': '[00:01:08](https://www.youtube.com/watch?v=U9IWvkKvtWE&t=68s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '5z0mahGmR40',
                       'title': 'Call Flow Builder - IVR routing',
                       'channel': 'WildJar Call Intelligence',
                       'author': 'WildJar Call Intelligence',
                       'text': "If I hit the save button at the top we get failed, and it's because we "
                               "haven't configured where we want this number to then dial.",
                       'tip': "If I hit the save button at the top we get failed, and it's because we "
                              "haven't configured where we want this number to then dial.",
                       'timestamp': 113,
                       'timestamp_seconds': 113,
                       'timestamp_label': '[00:01:53]',
                       'url': 'https://www.youtube.com/watch?v=5z0mahGmR40&t=113s',
                       'markdown': '[00:01:53](https://www.youtube.com/watch?v=5z0mahGmR40&t=113s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'tdZ944Oycuo',
                       'title': 'Autocia IVR Demo | Complete IVR Software & Call Flow Setup | Business '
                                'Automation',
                       'channel': 'Autocia Technologies',
                       'author': 'Autocia Technologies',
                       'text': 'Channel simply means how many calls this number can handle at the same '
                               'time, and if you have five channels then five people can call together and '
                               'nobody gets a busy tone.',
                       'tip': 'Channel simply means how many calls this number can handle at the same '
                              'time, and if you have five channels then five people can call together and '
                              'nobody gets a busy tone.',
                       'timestamp': 148,
                       'timestamp_seconds': 148,
                       'timestamp_label': '[00:02:28]',
                       'url': 'https://www.youtube.com/watch?v=tdZ944Oycuo&t=148s',
                       'markdown': '[00:02:28](https://www.youtube.com/watch?v=tdZ944Oycuo&t=148s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'tf4AieS7Mhc',
                       'title': 'How to set up a profitable Ringba call flow that converts',
                       'channel': 'Carlos Corona',
                       'author': 'Carlos Corona',
                       'text': 'The reason why we do this is because we found out that a lot of people '
                               "will press something and it wasn't necessarily the correct answer.",
                       'tip': 'The reason why we do this is because we found out that a lot of people will '
                              "press something and it wasn't necessarily the correct answer.",
                       'timestamp': 133,
                       'timestamp_seconds': 133,
                       'timestamp_label': '[00:02:13]',
                       'url': 'https://www.youtube.com/watch?v=tf4AieS7Mhc&t=133s',
                       'markdown': '[00:02:13](https://www.youtube.com/watch?v=tf4AieS7Mhc&t=133s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'tf4AieS7Mhc',
                       'title': 'How to set up a profitable Ringba call flow that converts',
                       'channel': 'Carlos Corona',
                       'author': 'Carlos Corona',
                       'text': "It might work for a few days, for a few weeks, and eventually you're going "
                               'to start hearing complaints about your calls.',
                       'tip': "It might work for a few days, for a few weeks, and eventually you're going "
                              'to start hearing complaints about your calls.',
                       'timestamp': 235,
                       'timestamp_seconds': 235,
                       'timestamp_label': '[00:03:55]',
                       'url': 'https://www.youtube.com/watch?v=tf4AieS7Mhc&t=235s',
                       'markdown': '[00:03:55](https://www.youtube.com/watch?v=tf4AieS7Mhc&t=235s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '7vsOEhARsdU',
                       'title': 'IVR Call Flow - What it is, Benefits & Best Practices',
                       'channel': 'GetVoIP - Simplify your search',
                       'author': 'GetVoIP - Simplify your search',
                       'text': 'Keep the menu simple and the phrasing concise, and try to limit each menu '
                               'to five options.',
                       'tip': 'Keep the menu simple and the phrasing concise, and try to limit each menu '
                              'to five options.',
                       'timestamp': 127,
                       'timestamp_seconds': 127,
                       'timestamp_label': '[00:02:07]',
                       'url': 'https://www.youtube.com/watch?v=7vsOEhARsdU&t=127s',
                       'markdown': '[00:02:07](https://www.youtube.com/watch?v=7vsOEhARsdU&t=127s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'UPUMLukglNc',
                       'title': 'Creating an IVR Menu | RingCentral Office Demo',
                       'channel': 'RingCentral UK',
                       'author': 'RingCentral UK',
                       'text': 'If I click on the plus icon here I can see what routing options are '
                               'available, and I could route to another menu, an external transfer, a '
                               'directory, a voicemail, or an extension.',
                       'tip': 'If I click on the plus icon here I can see what routing options are '
                              'available, and I could route to another menu, an external transfer, a '
                              'directory, a voicemail, or an extension.',
                       'timestamp': 65,
                       'timestamp_seconds': 65,
                       'timestamp_label': '[00:01:05]',
                       'url': 'https://www.youtube.com/watch?v=UPUMLukglNc&t=65s',
                       'markdown': '[00:01:05](https://www.youtube.com/watch?v=UPUMLukglNc&t=65s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'p7WavoW_6to',
                       'title': 'Tutorial - How to Use the Inbound Call Webhook & Dynamic Variables in '
                                'Retell AI!',
                       'channel': 'Henryk Brzozowski',
                       'author': 'Henryk Brzozowski',
                       'text': "The webhook has a time out of 10 seconds, and within 10 seconds if there's "
                               'no success the webhook will be retried up to three times.',
                       'tip': "The webhook has a time out of 10 seconds, and within 10 seconds if there's "
                              'no success the webhook will be retried up to three times.',
                       'timestamp': 264,
                       'timestamp_seconds': 264,
                       'timestamp_label': '[00:04:24]',
                       'url': 'https://www.youtube.com/watch?v=p7WavoW_6to&t=264s',
                       'markdown': '[00:04:24](https://www.youtube.com/watch?v=p7WavoW_6to&t=264s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '7GRJx9A5y5c',
                       'title': 'Call Routing | How to Automate Inbound Calls | Workflow 2',
                       'channel': 'GoHighLevel for Commercial Real Estate',
                       'author': 'GoHighLevel for Commercial Real Estate',
                       'text': 'The pros of that are obviously you get a real-time call back, and the cons '
                               'are you have zero prep time for that.',
                       'tip': 'The pros of that are obviously you get a real-time call back, and the cons '
                              'are you have zero prep time for that.',
                       'timestamp': 33,
                       'timestamp_seconds': 33,
                       'timestamp_label': '[00:00:33]',
                       'url': 'https://www.youtube.com/watch?v=7GRJx9A5y5c&t=33s',
                       'markdown': '[00:00:33](https://www.youtube.com/watch?v=7GRJx9A5y5c&t=33s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'}]}
