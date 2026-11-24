from __future__ import annotations

CHAPTER_11 = {'id': 'Q11',
 'chapter_id': 'Q11',
 'chapter_number': 11,
 'question_number': 11,
 'slug': 'a2p-10dlc-registering-vetting-delivering-business-sms',
 'question_prompt': 'How do I get A2P 10DLC brands and campaigns approved so business SMS traffic actually '
                    'delivers?',
 'kicker': 'Q11 / THE BIG MONEY PLAYBOOKS',
 'title': 'A2P 10DLC: Registering, Vetting, and Delivering Business SMS',
 'subtitle': 'TCR brand and campaign registration, Twilio, Commio, and Bandwidth portal walkthroughs, '
             'rejection error codes and fixes, first-time-approval submissions, opt-in and opt-out flows, '
             'carrier vetting Q&A, MSP checklists, carrier throttling, and bulk SMS sending',
 'layout_template': 'chapter_opener',
 'reading_time_minutes': 15,
 'executive_summary': "Sixteen practitioners, including carrier-side vendors, Twilio's developer team, "
                      'MSPs, and agency operators, agree on one reality: unregistered 10DLC traffic is '
                      'getting squeezed out, and registration lives or dies on the opt-in call to action. '
                      'Every number needs a brand (legal name and EIN matched to IRS records) and a '
                      'campaign (use case, samples, consent flow). Operators report brand fees of $4, $40 '
                      'secondary vetting, $15 per DCA vetting attempt, and package costs of $20-$60. '
                      'Default tiers sit near 2,000 segments/day on T-Mobile and 75 TPM on AT&T. A vetting '
                      'score of 80-100 unlocks 4,500 TPM and 200,000/day. The disagreements center on '
                      'three questions: whether resubmissions cost money, whether CPaaS platforms throttle '
                      'below carrier limits, and whether TCR has reduced spam at all.',
 'key_metrics': [{'label': 'External Vetting Fee',
                  'metric': 'External Vetting Fee',
                  'value': '$40 one-time',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'One-time external vetting fee paid through WMC Global, Aegis, or '
                             'campaignverify.org to earn a vetting score that sets throughput tier.',
                  'source': 'Telgorithm ([dgkKW0cbz1E @ 00:23:54])'},
                 {'label': 'Top-Tier Throughput After Vetting',
                  'metric': 'Top-Tier Throughput After Vetting',
                  'value': '4,500 TPM and 200,000 segments/day at a vetting score of 80-100',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Throughput unlocked once a brand scores 80-100 in external vetting, versus '
                             'the default 2,000/day T-Mobile and 75 TPM AT&T tier.',
                  'source': 'Telgorithm ([dgkKW0cbz1E @ 00:24:25])'},
                 {'label': 'DCA Vetting Cost Per Attempt',
                  'metric': 'DCA Vetting Cost Per Attempt',
                  'value': '$15 per attempt ($45 after three rejections)',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Per-submission DCA campaign vetting charge that compounds with every '
                             'rejected resubmission.',
                  'source': 'Telgorithm ([dgkKW0cbz1E @ 00:28:46])'},
                 {'label': 'Attempts Before Campaign Approval',
                  'metric': 'Attempts Before Campaign Approval',
                  'value': 'About 15 attempts',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'A Midwest MSP resubmitted roughly 15 times after repeated call-to-action '
                             'rejections before the campaign cleared.',
                  'source': 'Paradigm Escape ([wpj7_7cz4Kk @ 00:03:14])'}],
 'sections': [{'section': 1,
               'heading': 'The Practitioner Consensus',
               'paragraphs': ['Registry insiders and aggregators frame registration as a closing door '
                              'rather than a hard wall. The Campaign Registry, interviewed by Telgorithm, '
                              "concedes 'there's nothing preventing you from running unregistered,' yet "
                              'the avenues keep narrowing. Many direct connect aggregators now refuse '
                              'unregistered traffic outright because they see it as a liability to their '
                              'carrier connection [IQ19nUV4NVA @ 00:01:17]. The same interview warns that '
                              "pushing huge unregistered volumes can get your provider's carrier "
                              'connection questioned, and that more blocks and more algorithms are coming '
                              "for unregistered senders. Telgorithm's own Q&A lists the enforcement levers "
                              'carriers pull: pass-through fees of one cent per unregistered message from '
                              'June 1, filtering, and outright cutoffs [dgkKW0cbz1E @ 00:14:16]. '
                              'BuzzerBeep gives MSPs the same verdict in plain terms. Unregistered 10DLC '
                              "traffic carries additional carrier fees, and a filtered message 'doesn't "
                              "bounce like an email,' so the sender never sees the failure [9W2MLkN5lf4 @ "
                              '00:01:48]. Empire Telecom supplies the hard operational stop: a provider '
                              'cannot enable SMS on new numbers until registration is complete. Once '
                              'registered, the business should see better delivery rates because carriers '
                              'know and trust it [whbUkc2imdY @ 00:01:07]. The consensus position is that '
                              "registration is the carriers' sanctioned path for true business traffic, "
                              'and the unregistered lane keeps shrinking.',
                              'Every practitioner breaks registration into the same two objects. Bandwidth '
                              'explains that The Campaign Registry registers brands and campaigns, assigns '
                              'trust scores, and hands them to carriers. The brand file needs legal name, '
                              'contact, and industry, while the campaign needs a use case, description, '
                              'and sample messages [vrVUZ1rSJO0 @ 00:01:56]. RingLogix compresses it '
                              'further: TCR needs only who is texting and what type of message. On the '
                              "brand side, the rule is identical across vendors. Commio's walkthrough "
                              'stresses that legal name and address must match IRS or Secretary of State '
                              'records [WOoSDFU7S3k @ 00:00:54]. TwilioDevs ties this to error code 3903. '
                              'The legal name must match the IRS CP 575 or 147C letter, never the DBA or '
                              'W-9, and sole proprietor is reserved for US or Canada registrants without '
                              'an EIN [7pXYEARPIwU @ 00:02:53]. RingLogix shows the price of getting it '
                              'wrong. One brand sat unverified for a month, and once the correct name and '
                              'EIN went in, it verified the same day. Another failed purely for a missing '
                              'DUNS number [gmCqaG2hBKQ @ 00:38:26]. Commio adds the structural rule for '
                              'agencies and resellers: register the client as the brand and list yourself '
                              'as reseller, because the consumer thinks Nike is sending the message, not '
                              'your company.',
                              'Where the consensus gets loudest is the call to action. TwilioDevs names '
                              'four keys to a clean submission: consent, privacy policy, brand '
                              "consistency, and the ideal submission. Consent, they say, is where 'the "
                              "majority of rejections happen' [IUXJbMD7Qz4 @ 00:03:04]. RingLogix "
                              'independently reports that the call-to-action and message-flow field trips '
                              'people up most [gmCqaG2hBKQ @ 00:26:23]. Austin Marland splits approval '
                              'into three hurdles (business registration, brand and website compliance, '
                              "and use case) and flags the website piece as where 'most people fail' "
                              '[ttmM4fmBHDU @ 00:00:39]. Paradigm Escape, a Midwest MSP, lived it. They '
                              "were told 'over and over and over again' that their call to action was "
                              "wrong, and learned you cannot just claim 'text only.' The reviewer has to "
                              'see the opt-in method on your website [wpj7_7cz4Kk @ 00:01:47]. Their fix, '
                              'after roughly 15 attempts, was a Google Drive screenshot link showing the '
                              'website form with name, phone, consent, and submit. The TwilioDevs line '
                              "that sums up the consensus: 'If the reviewer can't see the process, they "
                              "can't approve the campaign.' The same channel adds that missing even one "
                              "opt-in flow is 'a one-way ticket to an immediate rejection.' The rules "
                              'apply equally to internal employees, so every collection point needs '
                              'documented proof.'],
               'table': {'caption': 'Where the practitioners agree: the baseline every 10DLC sender must '
                                    'clear',
                         'headers': ['Consensus Point',
                                     'What Practitioners Require',
                                     'Operator Consequence',
                                     'Expert Source'],
                         'rows': [['Unregistered traffic is a shrinking and increasingly risky lane',
                                   'Many DCAs refuse unregistered traffic as a liability to their carrier '
                                   'connection',
                                   'Expect more blocks and more algorithms targeting unregistered senders '
                                   'over time',
                                   'Telgorithm ([IQ19nUV4NVA @ 00:01:38])'],
                                  ['Every 10DLC sender needs a registered brand plus campaign',
                                   'Brand legal name, contact, industry; campaign use case, description, '
                                   'and sample messages',
                                   'Campaign ID generates immediately and must be associated with your '
                                   'numbers',
                                   'Bandwidth ([vrVUZ1rSJO0 @ 00:01:56])'],
                                  ['Brand legal name must match tax records exactly',
                                   'Use the name on IRS CP 575 or 147C, never the DBA or W-9',
                                   'A mismatch triggers error 3903 and a rejected brand registration',
                                   'TwilioDevs ([7pXYEARPIwU @ 00:02:53])'],
                                  ['The call to action is the single most common failure point',
                                   'Call-to-action and message-flow description trips registrants up more '
                                   'than anything else',
                                   'Build and verify the opt-in proof before touching any other field',
                                   'RingLogix ([gmCqaG2hBKQ @ 00:26:23])'],
                                  ['Opt-in proof must be visible to the reviewer, not just claimed',
                                   'Show the website opt-in form; claiming text-only opt-in gets the '
                                   'campaign rejected',
                                   'Paradigm Escape needed roughly 15 attempts before the call to action '
                                   'passed',
                                   'Paradigm Escape ([wpj7_7cz4Kk @ 00:01:47])'],
                                  ['Consent is non-transferable and every opt-in must be logged',
                                   'Record time, method, wording shown, and phone number for each '
                                   'individual opt-in',
                                   "A client's HR phone list cannot be repurposed as an SMS opt-in list",
                                   'BuzzerBeep ([9W2MLkN5lf4 @ 00:02:25])'],
                                  ['Agencies and resellers register the client as brand, not themselves',
                                   'Client goes into the brand slot while the agency is added as reseller',
                                   'The consumer believes the client brand, such as Nike, is sending the '
                                   'message',
                                   'Commio ([WOoSDFU7S3k @ 00:04:37])']]}},
              {'section': 2,
               'heading': 'Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['Each fee is small, but they stack fast on rejections. TwilioDevs puts brand '
                              'registration at $4, plus $40 for secondary vetting, and says resubmissions '
                              'add fees. Monthly campaign cost runs $2 for sole proprietor brands '
                              '[KWvbRToRnGg @ 00:13:45]. Telgorithm confirms the $40 as a one-time '
                              'external vetting fee through WMC Global, Aegis, or campaignverify.org. It '
                              'then itemizes the newer DCA vetting charge: $15 per attempt, so three '
                              'rejections cost $45. That layer began after cannabis traffic slipped '
                              "through back when approvals 'literally took seconds' [dgkKW0cbz1E @ "
                              '00:28:46]. Telgorithm also quotes low-volume campaigns at $1.50 per month '
                              'against $10 per month otherwise. Austin Marland prices the packages buyers '
                              'actually see at about $20 for low volume (under 2,000 segments a day at 160 '
                              'characters each) and about $60 for standard at 2,000 and up [ttmM4fmBHDU @ '
                              '00:07:18]. Marland clocked one approval at 3 days, with extreme cases '
                              'stretching to 2 weeks. Paradigm Escape saw a $10 to $15 charge right before '
                              'approval landed after roughly 15 attempts [wpj7_7cz4Kk @ 00:03:50]. Segment '
                              'math matters too. TwilioDevs counts roughly 160 characters per segment and '
                              'watched a single emoji turn a 2-segment message into 4, doubling the '
                              'segment count.',
                              'Throughput is the product you are buying. Telgorithm says outright that you '
                              'are purchasing throughput capabilities. The default tier sits at 2,000 '
                              'segments a day on T-Mobile and 75 TPM on AT&T [dgkKW0cbz1E @ 00:21:26]. The '
                              'units differ by carrier: T-Mobile counts per brand per day, AT&T per '
                              'campaign per minute, and Verizon and US Cellular per number per minute. '
                              'Send 2,001 messages against a 2,000 cap and the 2,001st drops. A vetting '
                              'score of 80 to 100 unlocks 4,500 TPM and 200,000 a day, and Russell 3000 '
                              'brands land in the top tier automatically. RingLogix steers most customers '
                              'to Low Volume Mix: 2 to 5 sub-use cases at 2,000 a day and 75 a minute, '
                              'with no extra vetting. It caps each campaign at 50 DIDs and each brand at '
                              "50 campaigns [gmCqaG2hBKQ @ 00:55:21]. Commio's marketing campaign showed "
                              '60 TPM and roughly 3,000 a day on T-Mobile. Pooling more than 49 numbers is '
                              "flagged as a special business case [WOoSDFU7S3k @ 00:03:19]. Signal House's "
                              'Will Craig stacks the math. Standard limits of 240 SMS segments a minute on '
                              'AT&T apply per campaign, so 10 campaigns yield 2,400 a minute, unless a '
                              'platform API cap of one call per second holds you to 60 [sVsWkczKncU @ '
                              '00:02:11].',
                              'The submission build is a checklist practitioners run line by line. Austin '
                              "Marland's opt-in page carries first name, phone, email, an unchecked "
                              'consent checkbox, opt-out language, Terms and Privacy Policy links, and a '
                              'frequency disclosure. Their sample messages follow name plus business name '
                              "plus 'stop to end,' with two or sometimes three samples [ttmM4fmBHDU @ "
                              '00:03:25]. They build policies in Termly in about 5 minutes. The free plan '
                              'allows one policy, and their workaround is a second account on a different '
                              'Google login. TwilioDevs maps the rejection codes to fixes. Host the opt-in '
                              'at a public link and check it in an incognito tab before resubmitting. Keep '
                              'the SMS checkbox unchecked and separate from the terms checkbox, and add '
                              "'message frequency varies' [7pXYEARPIwU @ 00:00:33]. The privacy policy "
                              "needs the exact clause 'No mobile information will be shared with third "
                              "parties or affiliates for marketing or promotional purposes.' Sharing data "
                              'with a CRM or support platform is fine [IUXJbMD7Qz4 @ 00:07:10]. TwilioDevs '
                              'adds that a 404 page means immediate rejection. On the Commio special with '
                              'Tim McLain, URL shorteners are banned outright in favor of a short owned '
                              'domain whose WHOIS matches the brand, and PO boxes trigger extra vetting '
                              '[SRizDef5BbE @ 00:10:34].'],
               'table': {'caption': 'Fee stack, throughput tiers, and hard limits as quoted by '
                                    'practitioners',
                         'headers': ['Line Item',
                                     'Exact Figure Stated',
                                     'How It Hits the Operator',
                                     'Expert Source'],
                         'rows': [['Brand registration and secondary vetting fees',
                                   '$4 per brand plus $40 for secondary vetting',
                                   'Resubmissions add further fees on top of the base registration cost',
                                   'TwilioDevs ([KWvbRToRnGg @ 00:13:45])'],
                                  ['DCA campaign vetting charged on every attempt',
                                   '$15 per attempt, so three rejections total $45',
                                   'Sloppy submissions compound cost with every rejected round of vetting',
                                   'Telgorithm ([dgkKW0cbz1E @ 00:28:46])'],
                                  ['External vetting score and the top throughput tier',
                                   'Score of 80 to 100 unlocks 4,500 TPM and 200,000 per day',
                                   'Paid once through WMC Global, Aegis, or campaignverify.org at $40',
                                   'Telgorithm ([dgkKW0cbz1E @ 00:24:25])'],
                                  ['Low volume versus standard package pricing for buyers',
                                   'About $20 under 2,000 segments a day; about $60 for 2,000 plus',
                                   'Choose the package by daily segment count at 160 characters each',
                                   'Austin Marland ([ttmM4fmBHDU @ 00:07:18])'],
                                  ['Low Volume Mix campaign limits and sub-use cases',
                                   '2,000 per day and 75 per minute across 2 to 5 sub-use cases',
                                   'Easier approval, no extra vetting, and lower cost for most customers',
                                   'RingLogix ([gmCqaG2hBKQ @ 00:17:53])'],
                                  ['Standard campaign carrier limits applied per campaign',
                                   '240 SMS segments per minute on AT&T; 2,000 segments per day on '
                                   'T-Mobile',
                                   'Ten campaigns stack to 2,400 per minute when the platform does not '
                                   'throttle',
                                   'Signal House ([sVsWkczKncU @ 00:01:28])'],
                                  ['Number and campaign ceilings inside a single brand',
                                   '50 DIDs per campaign and 50 campaigns per brand',
                                   'Number pools beyond 50 DIDs must be split across additional campaigns',
                                   'RingLogix ([gmCqaG2hBKQ @ 00:55:21])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Shortcuts operators used to clear review and protect throughput',
                           'body': 'These are the moves practitioners credit with getting campaigns '
                                   'approved faster and keeping sends at full carrier speed.',
                           'items': ['Screenshot the website opt-in form (name, phone, consent, submit) '
                                     'into a Google Drive link and paste it into the call to action. This '
                                     "is what finally ended Paradigm Escape's string of rejections "
                                     '[Paradigm Escape — wpj7_7cz4Kk @ 00:01:10].',
                                     'Write samples from the messages you will actually send, put the '
                                     'brand name in every one, and wrap dynamic data in square brackets '
                                     '[TwilioDevs — KWvbRToRnGg @ 00:15:45].',
                                     "Ask your platform point-blank: 'Is that the carrier rate limit or "
                                     "your internal rate limit?' Internal API caps can hold a sender to 60 "
                                     'messages per minute [Signal House — sVsWkczKncU @ 00:04:08].',
                                     'Open the opt-in URL in an incognito tab before every resubmission to '
                                     'confirm a reviewer can actually see it [TwilioDevs — 7pXYEARPIwU @ '
                                     '00:00:33].']},
               'sop_steps': [{'step': 1,
                              'title': 'Lock the brand identity',
                              'action': 'Register the brand with a legal name, EIN, and address that match '
                                        'IRS records exactly.',
                              'detail': 'Copy the legal name from the tax filing. A corrected name and EIN '
                                        'turned a month-long stall into same-day verification, and a '
                                        'missing DUNS number left another brand unverified [RingLogix — '
                                        'gmCqaG2hBKQ @ 00:38:26].'},
                             {'step': 2,
                              'title': 'Publish the public opt-in page and policies',
                              'action': 'Publish a form with an unchecked SMS consent box and full '
                                        'disclosures, plus matching Terms and Privacy Policy pages.',
                              'detail': 'Include first name, phone, email, an unchecked consent checkbox, '
                                        'opt-out text, a frequency disclosure, and ToS and Privacy Policy '
                                        'links. Termly-generated policies take about 5 minutes [Austin '
                                        'Marland — ttmM4fmBHDU @ 00:04:27].'},
                             {'step': 3,
                              'title': 'Write the campaign file to match reality',
                              'action': 'Align use case, description, samples, and call to action with '
                                        'what customers actually see.',
                              'detail': 'Samples carry the brand tag plus HELP and STOP language and must '
                                        'match the use case, so promos are not 2FA. Mixed campaigns need '
                                        'separate consent and samples for both message types [TwilioDevs — '
                                        'IUXJbMD7Qz4 @ 00:10:28].'},
                             {'step': 4,
                              'title': 'Attach numbers and go live',
                              'action': 'Link the approved campaign to your numbers inside the Messaging '
                                        'Service, then send using the service SID.',
                              'detail': 'After approval, link the accounts and wait [Paradigm Escape — '
                                        'wpj7_7cz4Kk @ 00:04:08]. Next, add the number to the Messaging '
                                        'Service [TwilioDevs — KWvbRToRnGg @ 00:19:33]. For bulk sends, '
                                        "put the Messaging Service SID in the 'from' field [Nexustech — "
                                        '6TMF0UdjIVU @ 00:02:41].'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The sharpest split on the money side is what a rejection actually costs. '
                              'Austin Marland tells operators that resubmitting carries no repeat fee, '
                              'that one approval cleared in 3 days, and that extreme cases stretch to 2 '
                              'weeks [ttmM4fmBHDU @ 00:08:00]. TwilioDevs flatly contradicts the '
                              'free-retry framing: registering a brand is $4, secondary vetting is $40, '
                              'and resubmission adds fees on top of that [KWvbRToRnGg @ 00:13:45]. '
                              'Telgorithm puts a hard number on the downside. DCA vetting costs $15 per '
                              'attempt, so three rejections burn $45. The vetting layer only appeared '
                              'after cannabis traffic slipped through, back when campaign approvals '
                              'literally took seconds. DCA queues were running 6 to 8 weeks, while '
                              'Telgorithm claims 3 to 5 days [dgkKW0cbz1E @ 00:28:46]. Paradigm Escape '
                              'lived the messy middle, grinding through roughly 15 attempts on a call to '
                              'action that kept bouncing, with a $10 to $15 charge landing just before '
                              'approval finally came through [wpj7_7cz4Kk @ 00:03:14]. The operator read '
                              'is blunt. Budget the rejection loop as a real cost line instead of trusting '
                              'the free-resubmit story. Front-load the opt-in, policy, and sample work '
                              'before the first click, and treat every bounce as both a fee and a '
                              "multi-week delay on the client's go-live.",
                              'Throughput numbers are where vendors pitch against each other hardest. Will '
                              'Craig of Signal House quotes standard limits of 240 SMS segments per minute '
                              'and 150 MMS per minute on AT&T, and 2,000 segments per day on T-Mobile. '
                              'Those scale to 4,500 SMS per minute, 2,400 MMS per minute, and 200,000 per '
                              'day. Craig argues that legacy CPaaS providers cap API calls, around 1 per '
                              'second, which works out to 60 messages per minute [sVsWkczKncU @ 00:02:27]. '
                              'The Signal House tactic is to ask whether a cap is the carrier rate limit '
                              "or the provider's internal rate limit. Craig also warns that resellers "
                              'share one API limit across every customer, which kills speed-to-lead. '
                              'Telgorithm frames the default tier as 2,000 per day on T-Mobile and 75 TPM '
                              'on AT&T, with external vetting scores of 80 to 100 unlocking 4,500 TPM and '
                              "200,000 per day [dgkKW0cbz1E @ 00:24:25]. Commio's dashboard showed a "
                              'marketing campaign at 60 texts per minute and roughly 3,000 per day on '
                              'T-Mobile, with paid vetting sold as the lever to raise it [WOoSDFU7S3k @ '
                              '00:03:19]. RingLogix pushes most customers toward Low Volume Mix instead: 2 '
                              'to 5 sub-use cases, 2,000 per day, 75 per minute, easier approval, no extra '
                              'vetting, and lower cost [gmCqaG2hBKQ @ 00:17:53]. The real choice is to pay '
                              'for vetting and fight for headroom, or accept the low-volume ceiling and '
                              'ship.',
                              'The deepest fight is over whether the registry, and the consent standard '
                              "behind it, actually earns its keep. Telgorithm's registry interview "
                              'concedes there is nothing preventing you from running unregistered. Some '
                              'senders may see acceptable termination for another year, with a few '
                              'messages blocked or dropped. The registry also warns that the avenues keep '
                              'shrinking and that many DCAs now refuse unregistered traffic as a liability '
                              'to their carrier connection [IQ19nUV4NVA @ 00:01:17]. The host of the '
                              'Telecom Application Development Summit session with Tim McLain goes the '
                              'other way entirely. The host claims spam has risen 520-fold since TCR began '
                              "and that the system doesn't work, and notes that Commio gets no campaign "
                              'discount [SRizDef5BbE @ 00:25:13]. On consent itself, Clerk AI treats an '
                              'inbound text from a customer as consent and auto-sends a STOP notice to '
                              'never-contacted numbers. Clerk AI admits a compliance team may still set a '
                              'stricter standard [CiI0Bewk8SU @ 00:01:43]. BuzzerBeep pulls hard the other '
                              "way for MSPs. Per CTIA, opt-in is non-transferable, and a client's HR phone "
                              'list is not your opt-in list. Every opt-in needs its time, method, wording '
                              "shown, and number recorded. BuzzerBeep's checklist reduces it to who is "
                              'sending, what you will send, how people agree, and who runs it [9W2MLkN5lf4 '
                              '@ 00:02:25].'],
               'table': {'caption': 'Competing practitioner playbooks on cost, throughput, pooling, '
                                    'registration, and consent',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Cost of a rejected submission and resubmission',
                                   'Austin Marland says resubmitting carries no repeat fee, and approvals '
                                   'run 3 days up to 2 weeks',
                                   'TwilioDevs says brand registration is $4, secondary vetting is $40, '
                                   'and resubmission adds fees',
                                   'Austin Marland ([ttmM4fmBHDU @ 00:08:00]); TwilioDevs ([KWvbRToRnGg @ '
                                   '00:13:58])'],
                                  ['Where the low-volume tier ceiling actually sits',
                                   'RingLogix Low Volume Mix allows 2 to 5 sub-use cases at 2,000 per day '
                                   'and 75 per minute',
                                   'TwilioDevs lists Low Volume Standard at 6,000 segments per day, with '
                                   'sole proprietor under 3,000',
                                   'RingLogix ([gmCqaG2hBKQ @ 00:17:53]); TwilioDevs ([KWvbRToRnGg @ '
                                   '00:13:10])'],
                                  ['What really limits sending speed in production',
                                   'Signal House says legacy CPaaS caps API calls near 1 per second, equal '
                                   'to 60 per minute',
                                   'Telgorithm says carriers measure differently: T-Mobile per brand per '
                                   'day, AT&T per campaign per minute',
                                   'Signal House ([sVsWkczKncU @ 00:02:27]); Telgorithm ([dgkKW0cbz1E @ '
                                   '00:52:47])'],
                                  ['Using a pool of many sender numbers',
                                   'Nexustech builds a Messaging Service sender pool and claims it helps '
                                   'bypass carrier filters',
                                   'Commio says pooling over 49 numbers is a T-Mobile special business '
                                   'case, with a hefty fee coming',
                                   'Nexustech ([6TMF0UdjIVU @ 00:01:10]); Commio ([WOoSDFU7S3k @ '
                                   '00:03:50])'],
                                  ['Running unregistered traffic versus registering now',
                                   "Telgorithm's registry guest says nothing prevents it, and termination "
                                   'may hold for another year',
                                   'Empire Telecom says providers cannot enable SMS on new numbers until '
                                   'registration is done',
                                   'Telgorithm ([IQ19nUV4NVA @ 00:02:15]); Empire Telecom ([whbUkc2imdY @ '
                                   '00:01:07])'],
                                  ['What counts as valid consent to text',
                                   'Clerk AI treats an inbound text from the customer as consent, then '
                                   'sends a STOP notice',
                                   "BuzzerBeep says opt-in is non-transferable, and a client's HR phone "
                                   'list is not an opt-in list',
                                   'Clerk AI ([CiI0Bewk8SU @ 00:01:43]); BuzzerBeep ([9W2MLkN5lf4 @ '
                                   '00:02:06])'],
                                  ['Whether the registry system itself is working',
                                   "Telgorithm's registry guest says registering takes away some of the "
                                   'unknown in termination',
                                   'The summit host claims spam rose 520-fold since TCR began and says it '
                                   "doesn't work",
                                   'Telgorithm ([IQ19nUV4NVA @ 00:00:57]); Telecom Application Development '
                                   'Summit ([SRizDef5BbE @ 00:25:13])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['Call to action is where campaigns die first, and every practitioner who has '
                              'fought it says so. Paradigm Escape, a Midwest MSP, was told over and over '
                              "that their call to action wasn't correct and burned through roughly 15 "
                              "attempts. They learned you can't just claim text-only without showing the "
                              'opt-in method on the site. They only broke through by submitting a Google '
                              'Drive screenshot link of the website form with name, phone, consent, and '
                              'submit [wpj7_7cz4Kk @ 00:01:10]. TwilioDevs maps the exact codes under '
                              "30909. Error 30543 means the opt-in isn't hosted at a public link. Error "
                              '3925 means the SMS checkbox is pre-checked or bundled with the terms '
                              'checkbox. Error 3545 means the form is missing message frequency varies '
                              'language [7pXYEARPIwU @ 00:00:15]. The second TwilioDevs walkthrough says '
                              "consent is where the majority of rejections happen. If the reviewer can't "
                              "see the process, they can't approve the campaign, and missing even one "
                              'opt-in flow is a one-way ticket to an immediate rejection [IUXJbMD7Qz4 @ '
                              '00:02:44]. RingLogix confirms that call-to-action and message flow trip '
                              'people up most. It adds that a campaign approved before it is rejected '
                              'seems easier to get through than one approved after a rejection '
                              '[gmCqaG2hBKQ @ 00:26:23].',
                              'Identity mismatches are the slow killer. RingLogix watched one brand sit '
                              'unverified for a month until the fix, the correct legal name and EIN, got '
                              'it verified the same day. Another brand stayed unverified because a DUNS '
                              'number was missing. The campaign stays blocked the whole time because it '
                              'cannot proceed until the brand is verified [gmCqaG2hBKQ @ 00:38:26]. '
                              'TwilioDevs pins error 3903 on brand type. Sole proprietor is only for US or '
                              'Canada registrants without an EIN, and the legal name must match the IRS CP '
                              '575 or 147C, not the DBA or the W-9 [7pXYEARPIwU @ 00:02:53]. The Tim '
                              'McLain session stacks more tripwires. Agencies should never register '
                              'themselves as the brand. PO boxes trigger extra vetting against a KYC '
                              'checklist of about 45 items, including DUNS. Each brand needs a unique EIN. '
                              'URL shorteners are out in favor of a short owned domain whose WHOIS matches '
                              "the brand. Sample messages that don't match the website pause the campaign "
                              '[SRizDef5BbE @ 00:12:45]. TwilioDevs adds that a mismatched domain or a '
                              'Gmail contact address raises suspicion, and a 404 page means immediate '
                              "rejection. ISVs must keep each client's brand front and center in its own "
                              'campaign, with no bundling [IUXJbMD7Qz4 @ 00:08:20].',
                              'The last layer of pain shows up in the invoice and the delivery log. '
                              'Telgorithm lists the enforcement levers as pass-through fees of 1 cent per '
                              'unregistered message from June 1, filtering, and cutoffs. It then warns '
                              'that if you send 2,001 messages against the T-Mobile 2,000 daily cap, that '
                              '2,001st message will drop. A DLR is not an HDLR, because no network '
                              'operator in existence today guarantees HDLRs [dgkKW0cbz1E @ 00:53:48]. '
                              'Signal House says traffic above carrier limits is dropped but can still be '
                              'charged. Resellers stuck behind one shared API limit watch speed-to-lead '
                              'suffer across every customer [sVsWkczKncU @ 00:03:05]. TwilioDevs flags the '
                              'quiet segment trap. A segment is about 160 characters, and a single emoji '
                              'turned a 2-segment message into 4, doubling the segment count on every send '
                              '[KWvbRToRnGg @ 00:10:06]. The Tim McLain session puts the penalty math on '
                              'the table. An escalated spam review costs $500, rising to $1,000 beyond 5 '
                              'campaigns, and T-Mobile fines reach the tens of thousands. Every STOP must '
                              'get a reply, and the defensive move is setting spend caps on the account '
                              '[SRizDef5BbE @ 00:18:45].'],
               'table': {'caption': 'Firsthand failures, what triggered them, and the practitioner fix or '
                                    'economics check',
                         'headers': ['Failure Mode',
                                     'What Happened Firsthand',
                                     'Fix or Economics Check',
                                     'Expert Source'],
                         'rows': [['Call to action rejected again and again',
                                   'Told over and over the call to action was wrong, across roughly 15 '
                                   'attempts',
                                   'Submit a Google Drive screenshot of the website form showing name, '
                                   'phone, consent, submit',
                                   'Paradigm Escape ([wpj7_7cz4Kk @ 00:01:10])'],
                                  ['Brand stuck unverified for weeks on end',
                                   'One brand took a month to verify, and another lacked a DUNS number',
                                   'Correct the legal name and EIN to match tax filing, and it verified '
                                   'the same day',
                                   'RingLogix ([gmCqaG2hBKQ @ 00:38:26])'],
                                  ['Privacy policy rejection under error 3908',
                                   'Missing the will-not-be-shared clause, a dead URL, conflicting '
                                   'policies, or a dropdown',
                                   'Place the clause visibly under an SMS terms or mobile information '
                                   'heading',
                                   'TwilioDevs ([7pXYEARPIwU @ 00:01:42])'],
                                  ['Emoji silently inflating segment counts',
                                   'A single emoji turned a 2-segment message into a 4-segment message',
                                   'Count roughly 160 characters per segment before writing campaign copy '
                                   'and samples',
                                   'TwilioDevs ([KWvbRToRnGg @ 00:10:06])'],
                                  ['Daily cap overflow on T-Mobile traffic',
                                   'Sending 2,001 messages on a 2,000 cap means the 2,001st message drops',
                                   'Track T-Mobile limits per brand per day, and AT&T limits per campaign '
                                   'per minute',
                                   'Telgorithm ([dgkKW0cbz1E @ 00:53:48])'],
                                  ['Paying for traffic that never delivered',
                                   'Traffic above carrier limits gets dropped but can still be charged to '
                                   'you',
                                   'Ask the provider whether a cap is the carrier rate limit or their '
                                   'internal one',
                                   'Signal House ([sVsWkczKncU @ 00:03:05])'],
                                  ['Spam escalation and carrier fine exposure',
                                   'Escalated spam review costs $500, rising to $1,000 beyond 5 campaigns',
                                   'Set spend caps, reply to every STOP, and expect T-Mobile fines in tens '
                                   'of thousands',
                                   'Telecom Application Development Summit ([SRizDef5BbE @ 00:18:45])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Pre-Submit and Pre-Send Kill Switch',
                           'body': 'Practitioners who lost weeks and money to rejections, unverified '
                                   'brands, dropped messages, and carrier penalties all point to the same '
                                   'four checks before you hit submit or scale sends.',
                           'items': ['Open the public opt-in link in an incognito tab before you resubmit, '
                                     'and confirm the SMS checkbox is unchecked and separate from the '
                                     'terms box [TwilioDevs — 7pXYEARPIwU @ 00:00:33].',
                                     "Match the brand's legal name and EIN exactly to the tax filing and "
                                     'confirm a DUNS number is on file. A one-month verification stall '
                                     'cleared the same day once this was fixed [RingLogix — gmCqaG2hBKQ @ '
                                     '00:38:26].',
                                     'Confirm every STOP gets a reply and that spend caps are set before '
                                     'scaling, because escalated spam reviews start at $500 [Telecom '
                                     'Application Development Summit — SRizDef5BbE @ 00:15:53].',
                                     'Keep daily sends under the T-Mobile per-brand cap, because the '
                                     '2,001st message on a 2,000 cap drops [Telgorithm — dgkKW0cbz1E @ '
                                     '00:53:48].']}}],
 'pull_quote': '"If the reviewer can\'t see the process, they can\'t approve the campaign." — TwilioDevs '
               '(IUXJbMD7Qz4 @ 00:02:44).',
 'diagram_id': 'diag-06',
 'action_checklist': ['Build an opt-in page with first name, phone, email, an unchecked consent checkbox, '
                      'opt-out text, Terms of Service and Privacy Policy links, and a frequency disclosure '
                      '[Austin Marland — ttmM4fmBHDU @ 00:03:25].',
                      "Add the clause 'No mobile information will be shared with third parties or "
                      "affiliates for marketing or promotional purposes' to the privacy policy [TwilioDevs "
                      '— IUXJbMD7Qz4 @ 00:07:10].',
                      'Write sample messages from your actual messages, with the brand name included and '
                      'dynamic data in brackets [TwilioDevs — KWvbRToRnGg @ 00:15:45].',
                      'Register the brand with a legal company name and address that match IRS or '
                      'Secretary of State records [Commio — WOoSDFU7S3k @ 00:00:54].',
                      'Choose Low Volume Mix with 2 to 5 sub-use cases when traffic fits under 2,000 per '
                      'day and 75 per minute [RingLogix — gmCqaG2hBKQ @ 00:17:53].',
                      'Associate the generated campaign ID with your numbers so traffic routes as '
                      'registered [Bandwidth — vrVUZ1rSJO0 @ 00:02:17].'],
 'statutory_citations': [{'title': 'TwilioDevs — Understanding US A2P 10DLC Registration [00:13:45]',
                          'url': 'https://www.youtube.com/watch?v=KWvbRToRnGg&t=825s',
                          'relevance': 'Primary practitioner testimony on brand fees, secondary vetting '
                                       'cost, resubmission fees, and throughput tiers.'},
                         {'title': 'Telgorithm — A2P 10DLC Messaging: TCR Registration & Campaign Vetting '
                                   'Q&A [00:28:46]',
                          'url': 'https://www.youtube.com/watch?v=dgkKW0cbz1E&t=1726s',
                          'relevance': 'Primary practitioner testimony on DCA vetting cost per attempt, '
                                       'vetting delays, and carrier throughput units.'},
                         {'title': 'RingLogix — Master 10DLC Texting Requirements [00:57:02]',
                          'url': 'https://www.youtube.com/watch?v=gmCqaG2hBKQ&t=3422s',
                          'relevance': 'Primary practitioner testimony on first-submission approval odds, '
                                       'brand verification stalls, and Low Volume Mix.'},
                         {'title': 'Telecom Application Development Summit — How to Register Your 10DLC '
                                   'Brands & Campaigns with TCE: Commio Special w/Tim McLain [00:18:45]',
                          'url': 'https://www.youtube.com/watch?v=SRizDef5BbE&t=1125s',
                          'relevance': 'Primary practitioner testimony on spam review penalties, carrier '
                                       'fines, and spend caps.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'wpj7_7cz4Kk',
                       'title': 'How to Get Your A2P 10DLC SMS Campaign Approved | Works with Twilio, '
                                'Plivo, Telnyx, and More',
                       'channel': 'Paradigm Escape',
                       'author': 'Paradigm Escape',
                       'text': 'Because I kept being told over and over and over again that my call to '
                               "action wasn't correct.",
                       'tip': 'Because I kept being told over and over and over again that my call to '
                              "action wasn't correct.",
                       'timestamp': 70,
                       'timestamp_seconds': 70,
                       'timestamp_label': '[00:01:10]',
                       'url': 'https://www.youtube.com/watch?v=wpj7_7cz4Kk&t=70s',
                       'markdown': '[00:01:10](https://www.youtube.com/watch?v=wpj7_7cz4Kk&t=70s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'sVsWkczKncU',
                       'title': 'Is Bandwidth, Twilio, and Telnyx Killing your 10DLC A2P Business '
                                'Messaging?!',
                       'channel': 'Signal House',
                       'author': 'Signal House',
                       'text': 'Now this means that you can send a total of 60 messages per minute.',
                       'tip': 'Now this means that you can send a total of 60 messages per minute.',
                       'timestamp': 166,
                       'timestamp_seconds': 166,
                       'timestamp_label': '[00:02:46]',
                       'url': 'https://www.youtube.com/watch?v=sVsWkczKncU&t=166s',
                       'markdown': '[00:02:46](https://www.youtube.com/watch?v=sVsWkczKncU&t=166s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '6TMF0UdjIVU',
                       'title': 'How To Send Bulk SMS In Twilio [2026 GUIDE]',
                       'channel': 'Nexustech',
                       'author': 'Nexustech',
                       'text': 'Put your Messaging Service SID in the from field when you send through the '
                               'Programmable SMS API.',
                       'tip': 'Put your Messaging Service SID in the from field when you send through the '
                              'Programmable SMS API.',
                       'timestamp': 161,
                       'timestamp_seconds': 161,
                       'timestamp_label': '[00:02:41]',
                       'url': 'https://www.youtube.com/watch?v=6TMF0UdjIVU&t=161s',
                       'markdown': '[00:02:41](https://www.youtube.com/watch?v=6TMF0UdjIVU&t=161s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'vrVUZ1rSJO0',
                       'title': 'The Messaging 411: 10DLC Campaign Registration',
                       'channel': 'Bandwidth',
                       'author': 'Bandwidth',
                       'text': 'If you want to send from a local number, then you do have to do this.',
                       'tip': 'If you want to send from a local number, then you do have to do this.',
                       'timestamp': 154,
                       'timestamp_seconds': 154,
                       'timestamp_label': '[00:02:34]',
                       'url': 'https://www.youtube.com/watch?v=vrVUZ1rSJO0&t=154s',
                       'markdown': '[00:02:34](https://www.youtube.com/watch?v=vrVUZ1rSJO0&t=154s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ttmM4fmBHDU',
                       'title': 'How to pass A2P 10DLC registration FAST (full 2025 tutorial for ANY '
                                'software)',
                       'channel': 'Austin Marland',
                       'author': 'Austin Marland',
                       'text': 'One approval took 3 days, resubmitting does not charge a repeat fee, and '
                               'extreme cases can take up to 2 weeks.',
                       'tip': 'One approval took 3 days, resubmitting does not charge a repeat fee, and '
                              'extreme cases can take up to 2 weeks.',
                       'timestamp': 480,
                       'timestamp_seconds': 480,
                       'timestamp_label': '[00:08:00]',
                       'url': 'https://www.youtube.com/watch?v=ttmM4fmBHDU&t=480s',
                       'markdown': '[00:08:00](https://www.youtube.com/watch?v=ttmM4fmBHDU&t=480s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '7pXYEARPIwU',
                       'title': 'Twilio A2P 10DLC Rejected? Fix These Error Codes',
                       'channel': 'TwilioDevs',
                       'author': 'TwilioDevs',
                       'text': 'Use an incognito tab to check that you can see it before you resubmit.',
                       'tip': 'Use an incognito tab to check that you can see it before you resubmit.',
                       'timestamp': 33,
                       'timestamp_seconds': 33,
                       'timestamp_label': '[00:00:33]',
                       'url': 'https://www.youtube.com/watch?v=7pXYEARPIwU&t=33s',
                       'markdown': '[00:00:33](https://www.youtube.com/watch?v=7pXYEARPIwU&t=33s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'KWvbRToRnGg',
                       'title': 'Understanding US A2P 10DLC Registration',
                       'channel': 'TwilioDevs',
                       'author': 'TwilioDevs',
                       'text': "Now to register a brand, it's $4.",
                       'tip': "Now to register a brand, it's $4.",
                       'timestamp': 825,
                       'timestamp_seconds': 825,
                       'timestamp_label': '[00:13:45]',
                       'url': 'https://www.youtube.com/watch?v=KWvbRToRnGg&t=825s',
                       'markdown': '[00:13:45](https://www.youtube.com/watch?v=KWvbRToRnGg&t=825s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'SRizDef5BbE',
                       'title': 'How to Register Your 10DLC Brands & Campaigns with TCE: Commio Special '
                                'w/Tim McLain',
                       'channel': 'Telecom Application Development Summit',
                       'author': 'Telecom Application Development Summit',
                       'text': 'If you are an agency, never register yourself as the brand.',
                       'tip': 'If you are an agency, never register yourself as the brand.',
                       'timestamp': 765,
                       'timestamp_seconds': 765,
                       'timestamp_label': '[00:12:45]',
                       'url': 'https://www.youtube.com/watch?v=SRizDef5BbE&t=765s',
                       'markdown': '[00:12:45](https://www.youtube.com/watch?v=SRizDef5BbE&t=765s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'gmCqaG2hBKQ',
                       'title': 'Master 10DLC Texting Requirements',
                       'channel': 'RingLogix',
                       'author': 'RingLogix',
                       'text': 'A campaign getting approved before it gets rejected seems to be easier '
                               "than getting a campaign approved after it's been rejected.",
                       'tip': 'A campaign getting approved before it gets rejected seems to be easier than '
                              "getting a campaign approved after it's been rejected.",
                       'timestamp': 3422,
                       'timestamp_seconds': 3422,
                       'timestamp_label': '[00:57:02]',
                       'url': 'https://www.youtube.com/watch?v=gmCqaG2hBKQ&t=3422s',
                       'markdown': '[00:57:02](https://www.youtube.com/watch?v=gmCqaG2hBKQ&t=3422s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'WOoSDFU7S3k',
                       'title': 'How to Register Brands & Campaigns | Commio | 10DLC Text Messaging',
                       'channel': 'Commio',
                       'author': 'Commio',
                       'text': "If you're doing campaigns have more than 49 numbers that affects you when "
                               'it comes to T-Mobile.',
                       'tip': "If you're doing campaigns have more than 49 numbers that affects you when "
                              'it comes to T-Mobile.',
                       'timestamp': 230,
                       'timestamp_seconds': 230,
                       'timestamp_label': '[00:03:50]',
                       'url': 'https://www.youtube.com/watch?v=WOoSDFU7S3k&t=230s',
                       'markdown': '[00:03:50](https://www.youtube.com/watch?v=WOoSDFU7S3k&t=230s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'CiI0Bewk8SU',
                       'title': '🔔10DLC Opt-In and Opt-Out Flows for SMS Texting (Outbound)🔔',
                       'channel': 'Clerk AI',
                       'author': 'Clerk AI',
                       'text': "It's really making sure that it's for the first time only.",
                       'tip': "It's really making sure that it's for the first time only.",
                       'timestamp': 69,
                       'timestamp_seconds': 69,
                       'timestamp_label': '[00:01:09]',
                       'url': 'https://www.youtube.com/watch?v=CiI0Bewk8SU&t=69s',
                       'markdown': '[00:01:09](https://www.youtube.com/watch?v=CiI0Bewk8SU&t=69s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'dgkKW0cbz1E',
                       'title': 'A2P 10DLC Messaging: TCR Registration & Campaign Vetting Q&A | Telgorithm',
                       'channel': 'Telgorithm',
                       'author': 'Telgorithm',
                       'text': 'If you send 2001 messages that 2000 first message will drop.',
                       'tip': 'If you send 2001 messages that 2000 first message will drop.',
                       'timestamp': 3228,
                       'timestamp_seconds': 3228,
                       'timestamp_label': '[00:53:48]',
                       'url': 'https://www.youtube.com/watch?v=dgkKW0cbz1E&t=3228s',
                       'markdown': '[00:53:48](https://www.youtube.com/watch?v=dgkKW0cbz1E&t=3228s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'dgkKW0cbz1E',
                       'title': 'A2P 10DLC Messaging: TCR Registration & Campaign Vetting Q&A | Telgorithm',
                       'channel': 'Telgorithm',
                       'author': 'Telgorithm',
                       'text': 'There is no network operator in existence today that guarantees HDLRs.',
                       'tip': 'There is no network operator in existence today that guarantees HDLRs.',
                       'timestamp': 2916,
                       'timestamp_seconds': 2916,
                       'timestamp_label': '[00:48:36]',
                       'url': 'https://www.youtube.com/watch?v=dgkKW0cbz1E&t=2916s',
                       'markdown': '[00:48:36](https://www.youtube.com/watch?v=dgkKW0cbz1E&t=2916s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '9W2MLkN5lf4',
                       'title': '10DLC Explained: What Is 10DLC? A Plain-English Guide for MSPs',
                       'channel': 'BuzzerBeep',
                       'author': 'BuzzerBeep',
                       'text': "A client's HR phone list is not your opt-in list.",
                       'tip': "A client's HR phone list is not your opt-in list.",
                       'timestamp': 126,
                       'timestamp_seconds': 126,
                       'timestamp_label': '[00:02:06]',
                       'url': 'https://www.youtube.com/watch?v=9W2MLkN5lf4&t=126s',
                       'markdown': '[00:02:06](https://www.youtube.com/watch?v=9W2MLkN5lf4&t=126s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'whbUkc2imdY',
                       'title': 'What is TCR Registration for 10DLC',
                       'channel': 'Empire Telecom',
                       'author': 'Empire Telecom',
                       'text': 'The good news is that once you are registered you should see even better '
                               'delivery rates for your messages as your business will be known and '
                               'trusted by the carriers.',
                       'tip': 'The good news is that once you are registered you should see even better '
                              'delivery rates for your messages as your business will be known and trusted '
                              'by the carriers.',
                       'timestamp': 122,
                       'timestamp_seconds': 122,
                       'timestamp_label': '[00:02:02]',
                       'url': 'https://www.youtube.com/watch?v=whbUkc2imdY&t=122s',
                       'markdown': '[00:02:02](https://www.youtube.com/watch?v=whbUkc2imdY&t=122s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'IQ19nUV4NVA',
                       'title': 'Why Register? The Campaign Registry Answers | A2P 10DLC Messaging',
                       'channel': 'Telgorithm',
                       'author': 'Telgorithm',
                       'text': "There's nothing preventing you from running unregistered.",
                       'tip': "There's nothing preventing you from running unregistered.",
                       'timestamp': 77,
                       'timestamp_seconds': 77,
                       'timestamp_label': '[00:01:17]',
                       'url': 'https://www.youtube.com/watch?v=IQ19nUV4NVA&t=77s',
                       'markdown': '[00:01:17](https://www.youtube.com/watch?v=IQ19nUV4NVA&t=77s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'IUXJbMD7Qz4',
                       'title': 'A2P 10DLC Campaign with Twilio - First Time Success',
                       'channel': 'TwilioDevs',
                       'author': 'TwilioDevs',
                       'text': "If the reviewer can't see the process, they can't approve the campaign.",
                       'tip': "If the reviewer can't see the process, they can't approve the campaign.",
                       'timestamp': 164,
                       'timestamp_seconds': 164,
                       'timestamp_label': '[00:02:44]',
                       'url': 'https://www.youtube.com/watch?v=IUXJbMD7Qz4&t=164s',
                       'markdown': '[00:02:44](https://www.youtube.com/watch?v=IUXJbMD7Qz4&t=164s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'}]}
