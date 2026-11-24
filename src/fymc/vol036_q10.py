from __future__ import annotations

CHAPTER_10 = {'id': 'Q10',
 'chapter_id': 'Q10',
 'chapter_number': 10,
 'question_number': 10,
 'slug': 'sip-trunking-cpaas-carriers-voice-ai-telephony',
 'question_prompt': 'How do I source SIP trunks and CPaaS carriers, and wire them into PBXs and AI voice '
                    'agents at the lowest cost without getting defrauded?',
 'kicker': 'Q10 / THE BIG MONEY PLAYBOOKS',
 'title': 'SIP Trunking, CPaaS Carriers, and Voice-AI Telephony',
 'subtitle': 'Retail vs wholesale SIP trunking, SIP vs VoIP, carrier softswitch selection, Twilio vs Plivo '
             'vs Telnyx pricing, Twilio vs Telnyx for voice agents, BYO SIP for Vapi, Retell, and '
             'ElevenLabs, Telnyx with LiveKit, FreeSWITCH carrier routing, FreePBX inbound routes, and SIP '
             'toll-fraud prevention',
 'layout_template': 'expert_commentary',
 'reading_time_minutes': 15,
 'executive_summary': 'SIP trunk and CPaaS practitioners agree the trunk is a concurrent talk path priced '
                      'against minutes, the carrier is a margin decision, and an exposed trunk becomes a '
                      'fraud bill. Sangoma sells stackable 3,000-minute trunks from around $25 a month at '
                      'roughly 2.4 cents per minute, while its VoIP Innovations wholesale arm demands a '
                      '$250 monthly minimum. On CPaaS, Plivo undercuts Twilio by about 30% on SMS, and Tim '
                      "of Voice AI with Tim argues Telnyx's private backbone can shave 100-plus "
                      "milliseconds off voice-agent turn gaps at roughly half Twilio's cost. Builders wire "
                      'Vapi, ElevenLabs, Retell, and LiveKit through BYO trunks, IP whitelists, FQDN '
                      "connections, and dispatch rules. The splits: Twilio's ecosystem and 180-country "
                      "reach versus Plivo's price and simpler setup, and Telnyx's latency claims, which "
                      'Tim flags as vendor marketing to verify with 100 test calls.',
 'key_metrics': [{'label': 'SIPStation Minutes Per Trunk',
                  'metric': 'SIPStation Minutes Per Trunk',
                  'value': '3,000 minutes per trunk; one bi-directional concurrent call; stackable (5 '
                           'trunks = 15,000 minutes)',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Michael White of Sangoma explaining how SIPStation trunks stack capacity and '
                             'minutes for FreePBX and PBXact systems',
                  'source': 'Sangoma ([dTsrqOzzrOk @ 00:02:13])'},
                 {'label': 'Plivo Per-Unit API Pricing',
                  'metric': 'Plivo Per-Unit API Pricing',
                  'value': '$0.007 per SMS; $0.01 per voice minute',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Amir Tutorial reading Plivo's SMS, verify, and voice API pricing against "
                             "Twilio's long code, toll-free, short code, and $0.02 MMS rates",
                  'source': 'Amir Tutorial ([_2POs6qxMdo @ 00:01:48])'},
                 {'label': 'Telnyx Marketed Audio Round Trip',
                  'metric': 'Telnyx Marketed Audio Round Trip',
                  'value': 'Sub-200 milliseconds round trip; possible 100+ ms shaved off the turn gap '
                           'versus Twilio',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Tim reports Telnyx's own marketed benchmark for voice AI audio, explicitly "
                             'telling viewers to take it with a grain of salt',
                  'source': 'Voice AI with Tim ([kYOdE4uxQXQ @ 00:05:42])'},
                 {'label': 'VoIP Innovations Wholesale Minimum',
                  'metric': 'VoIP Innovations Wholesale Minimum',
                  'value': '$250 per month minimum service commitment, plus volume-based rate plans',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Sangoma's wholesale carrier tier sold to resellers, MSPs, ITSPs, carriers, "
                             'and bulk-buying enterprises',
                  'source': 'Sangoma ([dTsrqOzzrOk @ 00:25:51])'}],
 'sections': [{'heading': '1. The Practitioner Consensus',
               'paragraphs': ['Every practitioner who prices SIP trunking treats the trunk as a talk path '
                              'rather than a phone line. Michael White of Sangoma sells SIPStation in '
                              'stackable trunks where each trunk is one bi-directional concurrent call '
                              'carrying 3,000 minutes, so a five-trunk account runs 15,000 minutes and '
                              'five simultaneous calls [dTsrqOzzrOk @ 00:02:13]. The VoIP Report applies '
                              'the same capacity logic at enterprise scale: share SIP capacity across '
                              'every site through pooled concurrent call paths, collapse duplicate office '
                              'PBXs into one centralized system, and run voice and data on one circuit '
                              'with one bill and one provider [zSendtIzBt0 @ 00:01:22]. Nate at GetVoIP '
                              'adds the buyer-side read: most SIP trunk providers plug into the IP-PBX a '
                              'business already runs and sell monthly plans with unlimited North American '
                              "calling and metered international [SUPHe70LM7s @ 00:01:16]. Nate's filter "
                              'is equally direct: a business without an IP-PBX on site is better off with '
                              'a cloud-hosted voice provider that demands no hardware purchase, while a '
                              'shop already running one can bolt VoIP on through a SIP trunk [SUPHe70LM7s '
                              '@ 00:08:50]. The shared baseline is blunt: count peak concurrent calls '
                              'before minutes, confirm whether switching hardware already sits on site, '
                              'and only then shop the carrier.',
                              'On the CPaaS layer, the speakers converge on a three-way split between '
                              'convenience, price, and owned infrastructure. Calderon Bridger casts the '
                              'industry giant as a rented luxury vehicle: sign up, grab a number, and send '
                              'a message before the coffee gets cold, then watch a premium for that '
                              'convenience stack up as the user base grows [KrSK9_CmFMk @ 00:00:55]. The '
                              'houdztech breakdown puts numbers on the gap, quoting Twilio at around 0.79 '
                              'per US SMS against roughly 0.55 for Plivo, about 30% cheaper, with Twilio '
                              'also charging for inbound messages where Plivo does not on local numbers '
                              '[lB4f9k3khDg @ 00:00:49]. GigaBits, after comparing both throughout 2025, '
                              'lands on the same fork: Twilio for highly custom flows backed by developers '
                              'on hand, Plivo as the leaner, cost-effective pick for startups and midsize '
                              'teams that need dependable voice and SMS without enterprise bulk '
                              '[cKVz3FEdvPQ @ 00:01:14]. Tim of Voice AI with Tim, who has run the voice '
                              'AI agency ximus.io for about two years, pushes the third lane: Telnyx '
                              'controls its own private backbone and co-locates telephony with GPU '
                              'inference at its global points of presence instead of riding the public '
                              'internet [kYOdE4uxQXQ @ 00:05:20]. The working consensus is that carrier '
                              'choice is a margin decision first and a feature decision second.',
                              'The third point of agreement is that an exposed trunk is a liability that '
                              'bills the owner. Mitel Academy walks through how a SIP hacker lifts trunk '
                              'credentials, registers a rogue device with the provider, and runs '
                              'long-distance and international calls whose bill lands on the company even '
                              'though nobody inside made a single one of them [ijPHb8SEENo @ 00:02:41]. '
                              "Sangoma's carrier-side answer is FraudGuard, which caps maximum weekly "
                              'international spend, hard-stops further international calls once the limit '
                              'is reached, and emails a warning as the account closes in on the ceiling '
                              '[dTsrqOzzrOk @ 00:11:02]. VoiceBuy widens the threat list to SIM box fraud '
                              'and international revenue share fraud, then calls native STIR/SHAKEN '
                              'support, meaning SIP identity header verification and token signing, basic '
                              'survival for North American operators facing FCC mandates rather than an '
                              "optional feature [elbBH6g2MU8 @ 00:02:34]. Sangoma's wholesale arm, VoIP "
                              'Innovations, sells the shortcut: resellers not ready to spend the time, '
                              'money, and effort on full STIR/SHAKEN compliance can have their calls '
                              'signed by Sangoma as part of the service [dTsrqOzzrOk @ 00:22:42]. The '
                              'floor is identical across the trainers and vendors: lock credentials, cap '
                              'international exposure, and get attestation handled before traffic scales, '
                              'because these losses surface as an invoice rather than a warning.'],
               'table': {'caption': 'Where SIP, CPaaS, and voice AI practitioners agree on the baseline',
                         'headers': ['Consensus Point',
                                     'What the Practitioner Reported',
                                     'Operator Implication',
                                     'Expert Source'],
                         'rows': [['Trunks are priced as concurrent talk paths',
                                   'Each SIPStation trunk is one bi-directional call carrying 3,000 '
                                   'stackable minutes',
                                   'Size capacity by peak simultaneous calls first, then minutes',
                                   'Sangoma ([dTsrqOzzrOk @ 00:02:13])'],
                                  ['SIP trunks fit businesses already owning an IP-PBX',
                                   'Without an on-site IP-PBX, a cloud-hosted voice provider needing no '
                                   'hardware wins',
                                   'Pitch trunks into shops already running their own PBX hardware',
                                   'GetVoIP - Simplify your search ([SUPHe70LM7s @ 00:08:50])'],
                                  ['Pooled capacity eliminates duplicate multi-site PBX spend',
                                   'Pooled concurrent call paths and one centralized PBX replace '
                                   'per-office duplicate systems',
                                   'Consolidate multi-location customers onto one shared trunk pool and '
                                   'bill',
                                   'The VoIP Report ([zSendtIzBt0 @ 00:01:22])'],
                                  ['CPaaS carrier choice is fundamentally a margin decision',
                                   'The giant gives speed, the budget alternative gives scale, the '
                                   'infrastructure owner gives power',
                                   'Match the carrier tier to launch stage and real call volume',
                                   'Calderon Bridger ([KrSK9_CmFMk @ 00:03:03])'],
                                  ['The carrier network sits inside voice AI latency',
                                   'Phone network adds delay alongside speech-to-text, LLM generation, and '
                                   'text-to-speech stages',
                                   'Treat carrier selection as a direct voice-agent naturalness lever',
                                   'Voice AI with Tim ([kYOdE4uxQXQ @ 00:01:18])'],
                                  ['Toll fraud enters through stolen trunk credentials',
                                   'Hijacked trunk or remote phone credentials let outsiders bill '
                                   'international calls to you',
                                   'Lock credentials and restrict dial plans before any number goes live',
                                   'Mitel Academy ([ijPHb8SEENo @ 00:01:32])'],
                                  ['STIR/SHAKEN is mandatory for North American carriers',
                                   'Native SIP identity header verification and token signing called basic '
                                   'survival',
                                   'Pick switches or wholesalers that sign calls natively or on your '
                                   'behalf',
                                   'VoiceBuy | Cloud Telecom & VoIP ([elbBH6g2MU8 @ 00:02:14])']]}},
              {'heading': '2. Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ["Sangoma's retail and wholesale card carries the hardest numbers. SIPStation "
                              'month-to-month pricing starts around $25 with a 20% discount on a '
                              'three-year plan, standard DIDs at $1, toll-free DIDs at $1.50, metered '
                              'minutes around 2.4 cents, outbound SMS at a penny per message, and inbound '
                              'texts free on any SMS-capable DID [dTsrqOzzrOk @ 00:12:57]. Overflow runs '
                              'through soft-cap bursting billed per minute once the 3,000-minute-per-trunk '
                              'allotment is spent, concurrency bursting billed per minute for calls beyond '
                              'the subscribed trunk count, and a pre-funded top-up balance that keeps the '
                              'system up during unexpected call spikes and fires a low-balance alert '
                              '[dTsrqOzzrOk @ 00:09:49]. On the wholesale side, Michael White positions '
                              'VoIP Innovations for resellers, MSPs, ITSPs, carriers, and bulk-buying '
                              'enterprises, covering more than 8,500 US rate centers and over 60 countries '
                              'with time-based, percentage-based, and failover routing, behind a $250 '
                              'monthly minimum commitment with volume-based rate plans layered on top '
                              '[dTsrqOzzrOk @ 00:25:51]. VoiceBuy maps the switching layer underneath that '
                              'business: class 4 for high calls-per-second wholesale transit with least '
                              'cost routing, class 5 for UCaaS and hosted PBX, and Sippy Softswitch as the '
                              'benchmark for least cost routing and rate deck management that stays '
                              'dependable under massive traffic loads [elbBH6g2MU8 @ 00:03:24].',
                              'Voice AI builders wire carriers into agent platforms through '
                              'bring-your-own-trunk plumbing. Jonas Massie creates a Twilio Elastic SIP '
                              'Trunk, names a termination SIP URI, and whitelists Vapi through two IP '
                              'access control lists, 44.229.228.186 and 44.238.177.138, each set to /32, '
                              'before saving the trunk [_wo5wokt3dI @ 00:05:23]. Jonas then fires two '
                              'Postman requests: a POST to api.vapi.ai/credential with the termination SIP '
                              'URI as the gateway, which returns the credential ID, and a POST to the '
                              'phone-number endpoint binding the Twilio-hosted number to that credential, '
                              'with inbound finished by adding an origination URI built from the number at '
                              'sip.vapi.ai [_wo5wokt3dI @ 00:09:05]. Omid Mohajerani runs the outbound '
                              'direction through FreeSWITCH so Vapi traffic can exit through any carrier: '
                              'create a Vapi SIP trunk pointing at the FreeSWITCH public IP with a '
                              'username and password of at least 20 characters, assign any E.164 number as '
                              'the caller ID because FreeSWITCH can rewrite it, add a matching directory '
                              'user, and send the Vapi dial plan context out to the carrier [HkWcpuMrX7k @ '
                              '00:05:19]. Omid routes plus-one numbers through SignalWire with the '
                              'FreeSWITCH IP already allowed there, calling it cheaper than other carriers '
                              'and reliable [HkWcpuMrX7k @ 00:09:17].',
                              'On Telnyx, a verified paid account is required before buying numbers, which '
                              'Tim says takes maybe a day or two, and the API key, which can carry an '
                              'expiration date, must be copied immediately because it is never shown again '
                              '[omQUCQVG1lg @ 00:02:01]. Inside Vapi, Tim uses the native Telnyx import, '
                              'which needs only the number, the API key, and a label; outbound then '
                              'requires an outbound voice profile whose allowed destinations default to '
                              "North America and must be switched to the caller's region before the "
                              'profile is assigned to the voice API application [omQUCQVG1lg @ 00:07:02]. '
                              'For LiveKit, Tim runs Postman requests that create the voice profile with '
                              'ISO A2 country codes, an FQDN connection with its own username and '
                              'password, an FQDN pointing at the LiveKit SIP endpoint, and a patch binding '
                              'the phone number ID to the connection, then builds an inbound trunk, a '
                              'dispatch rule with a call- room prefix, and an outbound trunk to '
                              'sip.telnyx.com carrying the X-Telnyx-Username header [omQUCQVG1lg @ '
                              '00:27:01]. VisionNLP self-hosts the same stack on Azure: reserve a static '
                              'public IP, add a DNS-only A record for the sip subdomain, open port 5060 '
                              'plus the 10,000 to 20,000 RTP range, and run the SIP service on host '
                              'networking because SIP and RTP do not work behind Docker NAT [ZQWTIIR9Exs @ '
                              '00:09:30].'],
               'table': {'caption': 'Price points, settings, and tool specs practitioners quoted on camera',
                         'headers': ['Tool / Line Item',
                                     'Exact Number or Setting',
                                     'How Operators Use It',
                                     'Expert Source'],
                         'rows': [['SIPStation retail SIP trunk for FreePBX',
                                   'Around $25 month-to-month, 20% off three-year, 2.4 cents per minute',
                                   'Retail trunk entry point for FreePBX and PBXact shops',
                                   'Sangoma ([dTsrqOzzrOk @ 00:12:57])'],
                                  ['SIPStation free trial inside the PBX module',
                                   '21 days, one DID in chosen rate center, two trunks',
                                   'Test inbound and outbound calling before committing any spend',
                                   'Sangoma ([dTsrqOzzrOk @ 00:03:56])'],
                                  ['VoIP Innovations wholesale carrier account minimum',
                                   '$250 monthly minimum commitment with volume-based rate plans on top',
                                   'Bulk wholesale access for resellers, MSPs, ITSPs, and carriers',
                                   'Sangoma ([dTsrqOzzrOk @ 00:25:51])'],
                                  ['Plivo SMS and voice API unit pricing',
                                   '$0.007 per SMS and $0.01 per voice minute',
                                   'Budget lane for SMS-heavy and basic calling builds',
                                   'Amir Tutorial ([_2POs6qxMdo @ 00:01:48])'],
                                  ['Twilio versus Plivo US SMS price gap',
                                   'Around 0.79 versus about 0.55 per US SMS',
                                   'Plivo roughly 30% cheaper across high-volume messaging runs',
                                   'houdztech ([lB4f9k3khDg @ 00:00:49])'],
                                  ['Telnyx voice AI audio latency marketing claim',
                                   'Sub-200 ms marketed round trip for voice AI audio',
                                   'Possible 100+ ms trimmed off the turn gap versus Twilio',
                                   'Voice AI with Tim ([kYOdE4uxQXQ @ 00:05:42])'],
                                  ['Vapi BYO SIP trunk credentials into FreeSWITCH',
                                   'Username and password of at least 20 characters',
                                   'Authenticates Vapi into FreeSWITCH before the carrier hand-off',
                                   'Omid Mohajerani ([HkWcpuMrX7k @ 00:05:19])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Small settings that move latency, margin, and routing accuracy',
                           'body': 'Four moves practitioners used on live accounts that most first-time '
                                   'builders skip.',
                           'items': ['Pin Twilio numbers to the closest region via Explore Products, Super '
                                     'Network, Phone Numbers: default is United States, pick Australia if '
                                     'in Sydney or Ireland for the EU, so calls stop crossing half the '
                                     'globe [Voice AI with Tim — kYOdE4uxQXQ @ 00:03:24]',
                                     'Use VoIP Innovations off-net SMS to port only the text-messaging '
                                     'portion of a number into FreePBX or PBXact while the existing voice '
                                     'carrier keeps the calls [Sangoma — dTsrqOzzrOk @ 00:20:03]',
                                     "Plivo's API is intentionally similar to Twilio's, so a cost-driven "
                                     'migration off Twilio is simple once volume justifies it [houdztech — '
                                     'lB4f9k3khDg @ 00:01:08]',
                                     'Know the digit format the carrier sends: Crosstalk SIP delivers '
                                     '11-digit numbers, so a 10-digit inbound route match fails; build a '
                                     'blank catch-all default route as the route of last resort [Crosstalk '
                                     'Solutions — 7VDpPwV6kS0 @ 00:09:37]']},
               'sop_steps': [{'step': 1,
                              'title': 'Size the trunk and pick the carrier tier',
                              'action': 'Count peak concurrent calls, buy stackable trunks, and set burst '
                                        'and top-up limits.',
                              'detail': 'Each SIPStation trunk is one concurrent call with 3,000 minutes, '
                                        'and soft-cap plus concurrency bursting bill per minute past the '
                                        'subscribed allotment [Sangoma — dTsrqOzzrOk @ 00:02:13]; match '
                                        'Twilio, Plivo, or Telnyx to whether speed, scale, or control '
                                        'matters most [Calderon Bridger — KrSK9_CmFMk @ 00:03:03].'},
                             {'step': 2,
                              'title': 'Lock the edge before any traffic flows',
                              'action': 'Restrict SIP ports, whitelist known IPs, block international '
                                        'dialing, and kill wildcard dial plans.',
                              'detail': 'Open 5060 and 5061 only to the provider and remote-user IPs, deny '
                                        'any at the end of the allow list, geo-block, block SIPVicious '
                                        'with an IPS firewall, and spell out allowed dial patterns instead '
                                        'of wildcards [Mitel Academy — ijPHb8SEENo @ 00:12:45].'},
                             {'step': 3,
                              'title': 'Wire the carrier into the agent platform',
                              'action': 'Create the trunk, whitelist the agent platform, and bind the '
                                        'number by API.',
                              'detail': 'On Twilio, build an Elastic SIP Trunk with two Vapi IP ACLs, POST '
                                        'the credential with the termination URI as gateway, then POST the '
                                        'phone number with the credential ID [Jonas Massie — _wo5wokt3dI @ '
                                        '00:09:05]; for an existing business number, get the IP or domain, '
                                        'username, and password from the current provider and have them '
                                        'whitelist the URI [Mehmood Feroz — R74S6hUZ4fk @ 00:04:34].'},
                             {'step': 4,
                              'title': 'Route inbound calls and A/B test the carrier',
                              'action': 'Set a catch-all inbound route, then run identical agent stacks on '
                                        'two carriers.',
                              'detail': 'Build identical configs on Telnyx and Twilio with the same STT, '
                                        'TTS, thresholds, and LLM, pin Twilio to the nearest region, log '
                                        'every metric, and run at least 100 test calls before choosing '
                                        '[Voice AI with Tim — kYOdE4uxQXQ @ 00:07:31].'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['On the CPaaS layer, the Twilio-versus-Plivo split is less about quality '
                              'than about which number you trust. houdztech prices Twilio at around 0.79 '
                              'per US SMS against roughly 0.55 on Plivo, calls that a 30% gap, says a '
                              'million messages saves thousands, and adds that Twilio bills inbound '
                              'messages while Plivo does not on local numbers [lB4f9k3khDg @ 00:00:31]. '
                              'Amir Tutorial quotes Plivo at 0.007 per SMS, 0.01 per voice minute, and '
                              'flags Twilio MMS at $0.02, yet still crowns Twilio best overall for '
                              "multi-channel builds and warns that Plivo's past security breaches and "
                              'limited features hold it back [_2POs6qxMdo @ 00:01:48]. The support verdict '
                              'flips depending on who you ask: Amir Tutorial rates Plivo support higher '
                              "than Twilio's, while houdztech reports Plivo phased out phone support and "
                              'frustrated some enterprise clients [lB4f9k3khDg @ 00:01:41]. GigaBits lands '
                              'in the middle, calling Twilio the gold standard that becomes overwhelming '
                              'without developers on hand and Plivo the leaner pick with more transparent '
                              'pricing and more responsive support for smaller teams [cKVz3FEdvPQ @ '
                              '00:00:36]. The operator read: Plivo for SMS and voice at volume, Twilio '
                              'when video, AI, email, or omnichannel flows justify the premium, and run '
                              'the numbers on your own lanes before committing.',
                              "For voice AI, the carrier fight is Twilio's ecosystem against Telnyx's "
                              'private backbone. Voice AI with Tim says Twilio runs traffic through '
                              'regional edges, so an operator pins the number to the nearest region under '
                              'Super Network (Australia for Sydney, Ireland for the EU, US by default), '
                              'and notes Twilio has published no latency benchmarks [kYOdE4uxQXQ @ '
                              "00:02:39]. Telnyx, by Tim's account, co-locates telephony with GPU "
                              'inference on its own private backbone and markets a sub-200 millisecond '
                              "audio round trip, which Tim explicitly tags as Telnyx's own benchmark to "
                              'take with a grain of salt, while estimating a possible saving of a '
                              'hundred-plus milliseconds off the turn gap [kYOdE4uxQXQ @ 00:05:59]. In the '
                              'follow-up build, Tim restates the verdict: Twilio works and is fine, but '
                              'Telnyx is building infrastructure for voice AI, with better latency, region '
                              'pinning, and about half the cost at scale [omQUCQVG1lg @ 00:01:24]. '
                              'Calderon Bridger frames the same market as three archetypes: the industry '
                              'giant that sells speed at a convenience tax, the budget alternative built '
                              'for high-volume rates with a steeper learning curve, and the infrastructure '
                              'owner that cuts out the middleman but is not for beginners [KrSK9_CmFMk @ '
                              '00:03:03]. Both converge on a stage-dependent rule: launch speed versus '
                              'margin survival.',
                              'Wiring a number into an agent splits into four competing playbooks. The '
                              "no-code route is Tim's: Vapi now ships an Import Telnyx option that needs "
                              'only the phone number, the API key, and a label, and inbound works once an '
                              'assistant is selected [omQUCQVG1lg @ 00:04:42]. Jonas Massie instead builds '
                              'a Twilio Elastic SIP Trunk, whitelists two Vapi IP access control lists on '
                              'termination, then registers a BYO SIP credential and phone number through '
                              "Vapi's API in Postman, adding an origination URI for inbound [_wo5wokt3dI @ "
                              "00:05:01]. Omid Mohajerani refuses to be limited to Vapi's own numbers: "
                              'Vapi sends outbound calls to a FreeSWITCH box that authenticates the Vapi '
                              'user, drops it into a dedicated Vapi context, and routes plus-numbers to '
                              'SignalWire, which they call cheaper than other carriers and reliable, while '
                              'existing billing and telephony stay intact [HkWcpuMrX7k @ 00:09:17]. '
                              'VisionNLP goes furthest, self-hosting the LiveKit SIP service on an Azure '
                              'VM behind its own DNS A record, then pointing a Telnyx FQDN connection at '
                              'that endpoint with inbound and outbound trunks plus a dispatch rule '
                              '[ZQWTIIR9Exs @ 00:12:25]. The tradeoff runs one direction: each step down '
                              'this ladder buys carrier freedom and control at the cost of more '
                              'configuration surface to break.'],
               'table': {'caption': 'Competing Playbooks: CPaaS, Carrier, Trunk, and Softswitch Choices',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Per-message SMS cost at US volume',
                                   'Twilio at around 0.79 per US SMS and it also bills inbound messages',
                                   'Plivo at about 0.55 per SMS, roughly 30% cheaper, no inbound charge on '
                                   'local numbers',
                                   'houdztech ([lB4f9k3khDg @ 00:00:31])'],
                                  ['Which CPaaS wins the overall pick',
                                   'Twilio named best overall for robust features, global scalability, and '
                                   'multi-channel options',
                                   'Plivo named the smart leaner pick for startups and midsize teams '
                                   'needing dependable SMS and voice',
                                   'Amir Tutorial ([_2POs6qxMdo @ 00:02:42]); GigaBits ([cKVz3FEdvPQ @ '
                                   '00:01:29])'],
                                  ['Plivo support quality and API speed',
                                   "Plivo support rated higher than Twilio's, with faster API call speed "
                                   'reported by users',
                                   'Plivo phased out phone support, which frustrated some enterprise '
                                   'clients, per mixed reviews',
                                   'Amir Tutorial ([_2POs6qxMdo @ 00:01:15]); houdztech ([lB4f9k3khDg @ '
                                   '00:01:41])'],
                                  ['Voice AI carrier latency strategy',
                                   'Twilio: pin the number to the nearest region, no official latency '
                                   'benchmarks published',
                                   'Telnyx: private backbone with marketed sub-200 ms round trip, a '
                                   'self-reported benchmark to discount',
                                   'Voice AI with Tim ([kYOdE4uxQXQ @ 00:05:59])'],
                                  ['Retail trunk versus wholesale carrier account',
                                   'SIPStation retail starts around 25 dollars monthly, 3,000 minutes per '
                                   'trunk, 2.4 cents per minute',
                                   'VoIP Innovations wholesale for resellers, MSPs, ITSPs, and carriers '
                                   'with a 250-per-month minimum commitment',
                                   'Sangoma ([dTsrqOzzrOk @ 00:12:37]); Sangoma ([dTsrqOzzrOk @ '
                                   '00:25:28])'],
                                  ['Hosted VoIP versus SIP trunking for a business',
                                   'No IP-PBX on site means go cloud-hosted; dollar for dollar VoIP '
                                   'usually offers better value',
                                   'An existing on-site IP-PBX or UCaaS stack makes adding a SIP trunk the '
                                   'easy path',
                                   'GetVoIP - Simplify your search ([SUPHe70LM7s @ 00:08:32])'],
                                  ['Softswitch class for a carrier build',
                                   'Class 4 for massive throughput, wholesale transit, high calls per '
                                   'second, and least cost routing',
                                   'Class 5 for end-user UCaaS, hosted PBX, and high feature density with '
                                   'multi-tenant portals',
                                   'VoiceBuy | Cloud Telecom & VoIP ([elbBH6g2MU8 @ 00:01:22])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['Toll fraud is the loss that lands as a bill nobody in the company placed. '
                              'Mitel Academy walks the attack paths: stolen SIP trunk credentials '
                              "registered on a hacker's device, hijacked remote-worker phone credentials, "
                              'PBX admin logins sniffed or social-engineered to create a rogue extension, '
                              'voicemail or IVR menus that branch back out to the telco, and call '
                              'forwarding set to an external destination [ijPHb8SEENo @ 00:07:06]. Their '
                              'counter-stack is blunt: strip international and long-distance from the dial '
                              'plan if you never call abroad, ban wildcard patterns because attackers '
                              'spray random numbers to see which completes, demand PIN authorization codes '
                              'for outbound, lock ports 5060 and 5061 to the carrier and known remote IPs, '
                              'geo-block whole continents, block SIPVicious with an IPS firewall, enable '
                              'fail-to-ban style lockouts, and upgrade firmware on PBX and endpoints '
                              '[ijPHb8SEENo @ 00:10:37]. Sangoma bolts a carrier-side cap on top: Fraud '
                              'Guard sets a maximum weekly international spend, halts international calls '
                              'when the limit hits, and emails a warning as you approach it [dTsrqOzzrOk @ '
                              '00:11:02]. VoiceBuy pushes the same logic into the switch, telling buyers '
                              'to demand that the platform automatically kill active sessions on velocity '
                              'spikes, because thin wholesale margins cannot absorb SIM box and '
                              'international revenue share fraud [elbBH6g2MU8 @ 00:05:48].',
                              'On the voice-AI side, most breakage is configuration drift rather than '
                              'carrier failure. Voice AI with Tim says the whitelisted destinations on the '
                              'Telnyx outbound voice profile tripped them up in the past, warns that a '
                              'Telnyx API key is visible only once and stops working at whatever '
                              'expiration you set, and stresses that the agent name in agent.py must match '
                              'the dispatch rule exactly or the call has no agent to land on [omQUCQVG1lg '
                              '@ 00:24:55]. Jonas Massie reports builders get tricked on the Gateway IP '
                              'field of the Vapi credential request; they route around it by pasting the '
                              'Twilio termination SIP URI instead of IPv4 ranges because it is much faster '
                              'and easier [_wo5wokt3dI @ 00:08:47]. Mehmood Feroz names the human '
                              "bottleneck when bridging a client's existing business number: the incumbent "
                              'provider has to enable access and whitelist on their side, so you need '
                              'their support to finish [R74S6hUZ4fk @ 00:04:15]. Omid Mohajerani flags two '
                              'smaller gotchas: the Vapi trunk username and password should be long, at '
                              'least around 20 characters, and the new BYO trunk may not appear in the '
                              'dashboard until you refresh the whole page [HkWcpuMrX7k @ 00:06:53].',
                              'Self-hosted and on-prem stacks break at the network layer first. VisionNLP '
                              'warns that Azure assigns a dynamic public IP that can change while the '
                              'deployment is live and fail the SIP trunks, so the IP must be switched to '
                              'static before the SIP A record goes into Cloudflare with proxy status set '
                              'to DNS only [ZQWTIIR9Exs @ 00:05:12]. The same build has to run the SIP '
                              'service with host networking because SIP and RTP do not work behind '
                              "Docker's NAT, and even the finished demo carried roughly 400 to 500 "
                              'milliseconds of extra lag from a UAE caller dialing a US Telnyx number '
                              'served by a South India VM [ZQWTIIR9Exs @ 00:20:41]. GetVoIP reports that '
                              'moving voice onto SIP puts much higher bandwidth demand on the network and '
                              'router, especially with a live call center, which may force a second or '
                              'more powerful router, with QoS settings used to prioritize voice traffic '
                              '[SUPHe70LM7s @ 00:08:01]. Crosstalk Solutions catches a quieter miss: their '
                              'carrier sends 11-digit numbers by default, so a DID inbound route keyed on '
                              '10 digits will not match, and you have to know the format your carrier '
                              'sends before building routes [7VDpPwV6kS0 @ 00:09:37].'],
               'table': {'caption': 'Firsthand Failure Modes and the Practitioner Fix',
                         'headers': ['Failure Mode', 'What Breaks', 'Fix or Check', 'Expert Source'],
                         'rows': [['Stolen SIP trunk credentials',
                                   'A hacker registers your trunk credentials on their own device and the '
                                   'bill lands on the company',
                                   'Provider-side public IP check so correct credentials from an '
                                   'unexpected IP still fail',
                                   'Mitel Academy ([ijPHb8SEENo @ 00:03:04])'],
                                  ['Guessable remote-phone SIP IDs',
                                   'Dictionary attacks guess simple numeric SIP IDs like 2006 and register '
                                   'rogue devices',
                                   'Alphanumeric mixed-case SIP IDs and passwords, plus whitelisted home '
                                   'IPs ending in deny any',
                                   'Mitel Academy ([ijPHb8SEENo @ 00:17:12])'],
                                  ['Uncapped international calling exposure',
                                   'Unauthorized international calls run up significant losses once '
                                   'international dialing is enabled',
                                   'Fraud Guard maximum weekly international spend with an email alert '
                                   'near the limit',
                                   'Sangoma ([dTsrqOzzrOk @ 00:10:46])'],
                                  ['Unpriced bursting during call spikes',
                                   'Usage past 3,000 minutes per trunk or past trunk count is billed per '
                                   'minute',
                                   'Set a Top-Up spending limit and turn on the low balance notification '
                                   'for admins',
                                   'Sangoma ([dTsrqOzzrOk @ 00:10:06])'],
                                  ['LiveKit outbound trunk auth mismatch',
                                   'Outbound calls fail when trunk auth username and password differ from '
                                   'the FQDN connection',
                                   'Match credentials exactly and add the X-Telnyx-Username custom header '
                                   'with the same username',
                                   'Voice AI with Tim ([omQUCQVG1lg @ 00:27:01])'],
                                  ['Legacy number cannot reach the trunk',
                                   'Porting into Twilio is lengthy, needs ownership documentation, and '
                                   'some numbers are not portable',
                                   'Run the portability check first, then ask the carrier or use another '
                                   'supported provider',
                                   'Jonas Massie ([_wo5wokt3dI @ 00:13:10])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Clear These Breakpoints Before a Trunk Carries Live Traffic',
                           'body': 'Four practitioner-reported breakpoints that turn a working demo into a '
                                   'fraud bill, a dead route, or a silent agent.',
                           'items': ['Dial plan contains no international or long-distance patterns you do '
                                     'not use and zero wildcards, since attackers throw random numbers to '
                                     'see which completes [Mitel Academy — ijPHb8SEENo @ 00:10:37].',
                                     "Ports 5060 and 5061 are open only to the SIP provider's IP and known "
                                     'remote-user IPs, with PBX admin reachable only through VPN or '
                                     'another secure method [Mitel Academy — ijPHb8SEENo @ 00:13:08].',
                                     'Self-hosted SIP VM has a static public IP before any trunk points at '
                                     'it, because a changed dynamic IP fails the SIP trunks [VisionNLP — '
                                     'ZQWTIIR9Exs @ 00:05:12].',
                                     'LiveKit agent name in code matches the dispatch rule exactly, or the '
                                     "dispatch rule cannot point the agent to the caller's room [Voice AI "
                                     'with Tim — omQUCQVG1lg @ 00:24:55].']}}],
 'pull_quote': '"Are you optimizing for the speed of a launch or the survival of your margins?" — Calderon '
               'Bridger (KrSK9_CmFMk @ 00:02:47).',
 'diagram_id': 'diag-02',
 'action_checklist': ['Pin your Twilio phone number region under Super Network to the location nearest '
                      'you: United States by default, Australia for Sydney, Ireland for the EU [Voice AI '
                      'with Tim — kYOdE4uxQXQ @ 00:03:24].',
                      'A/B test carriers with two identical agent configurations using the same STT, TTS, '
                      'LLM, and thresholds, log all metrics, and run at least 100 test calls [Voice AI '
                      'with Tim — kYOdE4uxQXQ @ 00:07:05].',
                      'On a Twilio Elastic SIP Trunk, set up termination with two Vapi IP access control '
                      'lists at /32 before attaching a number [Jonas Massie — _wo5wokt3dI @ 00:05:01].',
                      "Run Twilio's portability check on every legacy PBX or local carrier number before "
                      'promising a client their existing line on an AI agent [Jonas Massie — _wo5wokt3dI @ '
                      '00:13:10].',
                      'Create a Telnyx outbound voice profile whose allowed destinations match where your '
                      'calls go, then assign it to the voice API application [Voice AI with Tim — '
                      'omQUCQVG1lg @ 00:07:02].',
                      'Configure Fraud Guard with a maximum weekly international spend so international '
                      'calling stops at the cap and alerts you before it [Sangoma — dTsrqOzzrOk @ '
                      '00:11:02].'],
 'statutory_citations': [{'title': 'Mitel Academy — SIP Fraud | How to Prevent Toll Fraud on SIP Trunks '
                                   'and Devices [00:08:34]',
                          'url': 'https://www.youtube.com/watch?v=ijPHb8SEENo&t=514s',
                          'relevance': 'Primary practitioner testimony on toll fraud attack paths and '
                                       'layered firewall and PBX mitigations.'},
                         {'title': 'Voice AI with Tim — Twilio vs Telnyx: The Carrier That Makes or Breaks '
                                   'Your Voice AI [00:05:20]',
                          'url': 'https://www.youtube.com/watch?v=kYOdE4uxQXQ&t=320s',
                          'relevance': 'Primary practitioner testimony on carrier latency, private '
                                       'backbone positioning, and Twilio versus Telnyx cost.'},
                         {'title': 'Sangoma — SIP Trunking: Retail and Wholesale [00:25:28]',
                          'url': 'https://www.youtube.com/watch?v=dTsrqOzzrOk&t=1528s',
                          'relevance': 'Primary practitioner testimony on retail trunk pricing versus '
                                       'wholesale carrier minimum commitments.'},
                         {'title': 'VisionNLP — LiveKit SIP Trunking with Telnyx | Self-Hosted Azure, FQDN '
                                   '& AI Phone Calls [00:04:52]',
                          'url': 'https://www.youtube.com/watch?v=ZQWTIIR9Exs&t=292s',
                          'relevance': 'Primary practitioner testimony on self-hosted SIP failure points '
                                       'including dynamic IPs, Docker NAT, and network lag.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'dTsrqOzzrOk',
                       'title': 'SIP Trunking: Retail and Wholesale',
                       'channel': 'Sangoma',
                       'author': 'Sangoma',
                       'text': 'From a pricing perspective VoIP Innovations offers flexible and '
                               'customizable pricing plans, and we do have a minimum service commitment of '
                               '250 per month.',
                       'tip': 'From a pricing perspective VoIP Innovations offers flexible and '
                              'customizable pricing plans, and we do have a minimum service commitment of '
                              '250 per month.',
                       'timestamp': 1528,
                       'timestamp_seconds': 1528,
                       'timestamp_label': '[00:25:28]',
                       'url': 'https://www.youtube.com/watch?v=dTsrqOzzrOk&t=1528s',
                       'markdown': '[00:25:28](https://www.youtube.com/watch?v=dTsrqOzzrOk&t=1528s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'elbBH6g2MU8',
                       'title': 'Top 5 Carrier SIP Softswitch Providers in 2026 (Complete Comparison)',
                       'channel': 'VoiceBuy | Cloud Telecom & VoIP',
                       'author': 'VoiceBuy | Cloud Telecom & VoIP',
                       'text': 'Demand to know if their platform can automatically kill active sessions if '
                               'velocity spikes are detected.',
                       'tip': 'Demand to know if their platform can automatically kill active sessions if '
                              'velocity spikes are detected.',
                       'timestamp': 348,
                       'timestamp_seconds': 348,
                       'timestamp_label': '[00:05:48]',
                       'url': 'https://www.youtube.com/watch?v=elbBH6g2MU8&t=348s',
                       'markdown': '[00:05:48](https://www.youtube.com/watch?v=elbBH6g2MU8&t=348s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'SUPHe70LM7s',
                       'title': 'SIP Trunking vs VoIP - Key Differences, Pros & Cons',
                       'channel': 'GetVoIP - Simplify your search',
                       'author': 'GetVoIP - Simplify your search',
                       'text': 'Compare dollar for dollar, VoIP phone systems usually offer better value '
                               'than SIP trunking plans.',
                       'tip': 'Compare dollar for dollar, VoIP phone systems usually offer better value '
                              'than SIP trunking plans.',
                       'timestamp': 512,
                       'timestamp_seconds': 512,
                       'timestamp_label': '[00:08:32]',
                       'url': 'https://www.youtube.com/watch?v=SUPHe70LM7s&t=512s',
                       'markdown': '[00:08:32](https://www.youtube.com/watch?v=SUPHe70LM7s&t=512s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'zSendtIzBt0',
                       'title': 'SIP Trunking 101 - The VoIP Report',
                       'channel': 'The VoIP Report',
                       'author': 'The VoIP Report',
                       'text': 'Do you make a lot of long distance calls? Then choose a service provider '
                               'that operates a Tier 1 network, which gives you access to most regions of '
                               'the world, at competitive rates.',
                       'tip': 'Do you make a lot of long distance calls? Then choose a service provider '
                              'that operates a Tier 1 network, which gives you access to most regions of '
                              'the world, at competitive rates.',
                       'timestamp': 46,
                       'timestamp_seconds': 46,
                       'timestamp_label': '[00:00:46]',
                       'url': 'https://www.youtube.com/watch?v=zSendtIzBt0&t=46s',
                       'markdown': '[00:00:46](https://www.youtube.com/watch?v=zSendtIzBt0&t=46s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'KrSK9_CmFMk',
                       'title': 'Twilio vs Plivo vs Telnyx Comparison Review 2026: CPaaS Platform Overview',
                       'channel': 'Calderon Bridger',
                       'author': 'Calderon Bridger',
                       'text': 'Are you optimizing for the speed of a launch or the survival of your '
                               'margins.',
                       'tip': 'Are you optimizing for the speed of a launch or the survival of your '
                              'margins.',
                       'timestamp': 167,
                       'timestamp_seconds': 167,
                       'timestamp_label': '[00:02:47]',
                       'url': 'https://www.youtube.com/watch?v=KrSK9_CmFMk&t=167s',
                       'markdown': '[00:02:47](https://www.youtube.com/watch?v=KrSK9_CmFMk&t=167s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'lB4f9k3khDg',
                       'title': 'Twilio vs Plivo – Which One is Better in 2026?',
                       'channel': 'houdztech',
                       'author': 'houdztech',
                       'text': 'Twilio charges around 0.79 per SMS in the US while Plivo is about 0.55, '
                               "that's 30% cheaper.",
                       'tip': 'Twilio charges around 0.79 per SMS in the US while Plivo is about 0.55, '
                              "that's 30% cheaper.",
                       'timestamp': 31,
                       'timestamp_seconds': 31,
                       'timestamp_label': '[00:00:31]',
                       'url': 'https://www.youtube.com/watch?v=lB4f9k3khDg&t=31s',
                       'markdown': '[00:00:31](https://www.youtube.com/watch?v=lB4f9k3khDg&t=31s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'kYOdE4uxQXQ',
                       'title': 'Twilio vs Telnyx: The Carrier That Makes or Breaks Your Voice AI',
                       'channel': 'Voice AI with Tim',
                       'author': 'Voice AI with Tim',
                       'text': 'But also, caveat, this is their benchmark, so take this with a grain of '
                               'salt.',
                       'tip': 'But also, caveat, this is their benchmark, so take this with a grain of '
                              'salt.',
                       'timestamp': 359,
                       'timestamp_seconds': 359,
                       'timestamp_label': '[00:05:59]',
                       'url': 'https://www.youtube.com/watch?v=kYOdE4uxQXQ&t=359s',
                       'markdown': '[00:05:59](https://www.youtube.com/watch?v=kYOdE4uxQXQ&t=359s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '_2POs6qxMdo',
                       'title': 'Twilio vs Plivo – Which One is Better in 2025?',
                       'channel': 'Amir Tutorial',
                       'author': 'Amir Tutorial',
                       'text': 'Twilio is the best overall for its robust features, global scalability, '
                               'and multi-channel options.',
                       'tip': 'Twilio is the best overall for its robust features, global scalability, and '
                              'multi-channel options.',
                       'timestamp': 145,
                       'timestamp_seconds': 145,
                       'timestamp_label': '[00:02:25]',
                       'url': 'https://www.youtube.com/watch?v=_2POs6qxMdo&t=145s',
                       'markdown': '[00:02:25](https://www.youtube.com/watch?v=_2POs6qxMdo&t=145s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'cKVz3FEdvPQ',
                       'title': 'Twilio Vs Plivo (2025) | Which One Is Better?',
                       'channel': 'GigaBits',
                       'author': 'GigaBits',
                       'text': "With power comes complexity; Twilio can be overwhelming if you don't have "
                               'developers on hand to manage it.',
                       'tip': "With power comes complexity; Twilio can be overwhelming if you don't have "
                              'developers on hand to manage it.',
                       'timestamp': 36,
                       'timestamp_seconds': 36,
                       'timestamp_label': '[00:00:36]',
                       'url': 'https://www.youtube.com/watch?v=cKVz3FEdvPQ&t=36s',
                       'markdown': '[00:00:36](https://www.youtube.com/watch?v=cKVz3FEdvPQ&t=36s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'HkWcpuMrX7k',
                       'title': 'Connect VAPI BYO SIP Trunk to FreeSWITCH (Route to Any Carrier)',
                       'channel': 'Omid Mohajerani',
                       'author': 'Omid Mohajerani',
                       'text': "I'm using SignalWire to send plus one numbers to the carrier; it's cheaper "
                               'than for example the other carriers and also I rely on them.',
                       'tip': "I'm using SignalWire to send plus one numbers to the carrier; it's cheaper "
                              'than for example the other carriers and also I rely on them.',
                       'timestamp': 557,
                       'timestamp_seconds': 557,
                       'timestamp_label': '[00:09:17]',
                       'url': 'https://www.youtube.com/watch?v=HkWcpuMrX7k&t=557s',
                       'markdown': '[00:09:17](https://www.youtube.com/watch?v=HkWcpuMrX7k&t=557s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ijPHb8SEENo',
                       'title': 'SIP Fraud | How to Prevent Toll Fraud on SIP Trunks and Devices',
                       'channel': 'Mitel Academy',
                       'author': 'Mitel Academy',
                       'text': 'We must avoid using wild cards because when we use wild cards, we are just '
                               'opening up the system for any number that gets called to be successful.',
                       'tip': 'We must avoid using wild cards because when we use wild cards, we are just '
                              'opening up the system for any number that gets called to be successful.',
                       'timestamp': 661,
                       'timestamp_seconds': 661,
                       'timestamp_label': '[00:11:01]',
                       'url': 'https://www.youtube.com/watch?v=ijPHb8SEENo&t=661s',
                       'markdown': '[00:11:01](https://www.youtube.com/watch?v=ijPHb8SEENo&t=661s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '7VDpPwV6kS0',
                       'title': '21 Inbound Routes - FreePBX 101 v15',
                       'channel': 'Crosstalk Solutions',
                       'author': 'Crosstalk Solutions',
                       'text': 'With Crosstalk SIP by default we are sending 11 digit caller IDs, so if '
                               "you tried to route with a 10 digit caller ID it's not going to match.",
                       'tip': 'With Crosstalk SIP by default we are sending 11 digit caller IDs, so if you '
                              "tried to route with a 10 digit caller ID it's not going to match.",
                       'timestamp': 577,
                       'timestamp_seconds': 577,
                       'timestamp_label': '[00:09:37]',
                       'url': 'https://www.youtube.com/watch?v=7VDpPwV6kS0&t=577s',
                       'markdown': '[00:09:37](https://www.youtube.com/watch?v=7VDpPwV6kS0&t=577s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '_wo5wokt3dI',
                       'title': 'The Ultimate SIP Trunking Guide for AI Voice Agents | Twilio + Vapi',
                       'channel': 'Jonas Massie',
                       'author': 'Jonas Massie',
                       'text': 'Really what we need to do is get our number within the Twilio ecosystem so '
                               'that we can assign this to our trunk.',
                       'tip': 'Really what we need to do is get our number within the Twilio ecosystem so '
                              'that we can assign this to our trunk.',
                       'timestamp': 751,
                       'timestamp_seconds': 751,
                       'timestamp_label': '[00:12:31]',
                       'url': 'https://www.youtube.com/watch?v=_wo5wokt3dI&t=751s',
                       'markdown': '[00:12:31](https://www.youtube.com/watch?v=_wo5wokt3dI&t=751s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'R74S6hUZ4fk',
                       'title': 'Connect Your Business Phone to AI Voice Agent | SIP TRUNK | VAPI | RETELL '
                                '| ELEVENLABS',
                       'channel': 'Mehmood Feroz',
                       'author': 'Mehmood Feroz',
                       'text': 'The provider has to enable the access from their side and the '
                               'whitelisting, so you have to have some conversation with them and '
                               'integrate along with their help.',
                       'tip': 'The provider has to enable the access from their side and the whitelisting, '
                              'so you have to have some conversation with them and integrate along with '
                              'their help.',
                       'timestamp': 255,
                       'timestamp_seconds': 255,
                       'timestamp_label': '[00:04:15]',
                       'url': 'https://www.youtube.com/watch?v=R74S6hUZ4fk&t=255s',
                       'markdown': '[00:04:15](https://www.youtube.com/watch?v=R74S6hUZ4fk&t=255s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'omQUCQVG1lg',
                       'title': 'How to connect a Telnyx number with Vapi and LiveKit (2026)',
                       'channel': 'Voice AI with Tim',
                       'author': 'Voice AI with Tim',
                       'text': "Without this name, the dispatch rule doesn't know which room to point this "
                               'agent to, and this needs to match exactly.',
                       'tip': "Without this name, the dispatch rule doesn't know which room to point this "
                              'agent to, and this needs to match exactly.',
                       'timestamp': 1495,
                       'timestamp_seconds': 1495,
                       'timestamp_label': '[00:24:55]',
                       'url': 'https://www.youtube.com/watch?v=omQUCQVG1lg&t=1495s',
                       'markdown': '[00:24:55](https://www.youtube.com/watch?v=omQUCQVG1lg&t=1495s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ZQWTIIR9Exs',
                       'title': 'LiveKit SIP Trunking with Telnyx | Self-Hosted Azure, FQDN & AI Phone '
                                'Calls',
                       'channel': 'VisionNLP',
                       'author': 'VisionNLP',
                       'text': 'Azure usually provides a dynamic public IP which can get changed while our '
                               'deployment is still there and that will fail our SIP trunks.',
                       'tip': 'Azure usually provides a dynamic public IP which can get changed while our '
                              'deployment is still there and that will fail our SIP trunks.',
                       'timestamp': 292,
                       'timestamp_seconds': 292,
                       'timestamp_label': '[00:04:52]',
                       'url': 'https://www.youtube.com/watch?v=ZQWTIIR9Exs&t=292s',
                       'markdown': '[00:04:52](https://www.youtube.com/watch?v=ZQWTIIR9Exs&t=292s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ZQWTIIR9Exs',
                       'title': 'LiveKit SIP Trunking with Telnyx | Self-Hosted Azure, FQDN & AI Phone '
                                'Calls',
                       'channel': 'VisionNLP',
                       'author': 'VisionNLP',
                       'text': 'There is a little bit of network lag because the Telnyx phone number is '
                               'from the US, the call is from a UAE number, and the VM is hosted in South '
                               'India, which added around 400 to 500 milliseconds.',
                       'tip': 'There is a little bit of network lag because the Telnyx phone number is '
                              'from the US, the call is from a UAE number, and the VM is hosted in South '
                              'India, which added around 400 to 500 milliseconds.',
                       'timestamp': 1241,
                       'timestamp_seconds': 1241,
                       'timestamp_label': '[00:20:41]',
                       'url': 'https://www.youtube.com/watch?v=ZQWTIIR9Exs&t=1241s',
                       'markdown': '[00:20:41](https://www.youtube.com/watch?v=ZQWTIIR9Exs&t=1241s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'}]}
