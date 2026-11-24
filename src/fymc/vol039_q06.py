from __future__ import annotations

CHAPTER_6 = {'id': 'Q6',
 'chapter_id': 'Q6',
 'chapter_number': 6,
 'question_number': 6,
 'slug': 'tcpa-one-to-one-consent-lead-gen-compliance',
 'question_prompt': 'How do I capture and document compliant consent for calls and leads under the '
                    'FCC/TCPA rules?',
 'kicker': 'Q6 / THE BIG MONEY PLAYBOOKS',
 'title': 'TCPA One-to-One Consent and Lead-Gen Compliance',
 'subtitle': 'FCC one-to-one consent rules and the third-party affiliate loophole, consent capture in '
             'forms, consent tracking checklists, TCPA-compliant texting, DNC and opt-in lead rules, TPMO '
             'disclaimers, compliant lead capture with AI scoring, and compliance essentials',
 'layout_template': 'step_by_step_blueprint',
 'reading_time_minutes': 15,
 'executive_summary': "Pay-per-call and ping-post operators agree the 'our partners' blanket is dead. "
                      "Consent must name one business per unchecked box, match the ad's context, list "
                      'every regulated technology, and live in a timestamped record that both buyer and '
                      'seller can produce. The buyer carries the burden of proof. Street mechanics range '
                      "from Calldrive's token-plus-IP-plus-video capture, 50,000-transaction AI scoring "
                      "and $20 to $1,000 RTB call bids, to LeadCaptureIO's dynamic buyer insertion, "
                      'Gravity Forms-to-Airtable consent logs, $150-a-month DNC scrubbing, and SMS kept '
                      'under 320 characters. Eric Troutman estimates only two of 10 circulating one-to-one '
                      'forms pass. The disagreements are sharp. Quoted fines run from $100 to $2,000 per '
                      'violation. Eli Rivera treats B2B as exposed while Mike Fitzpatrick says it is not '
                      'covered. Agent CRM reports the rule thrown out entirely, while Troutman treats '
                      'January 27 as live.',
 'key_metrics': [{'label': 'Per-Violation Fine Exposure',
                  'metric': 'Per-Violation Fine Exposure',
                  'value': '$500 to $2,000 per text or call violation',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Amy Chan's fine range for contacting leads without one-to-one consent ahead "
                             'of the January 27 deadline, counted per text or call.',
                  'source': 'Seasalt AI ([KBFaRW7QmVQ @ 00:14:15])'},
                 {'label': 'Circulating One-to-One Forms That Pass',
                  'metric': 'Circulating One-to-One Forms That Pass',
                  'value': 'Probably only 2 of 10',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Eric Troutman's read on one-to-one forms in circulation. Lead sellers create "
                             'the risk, but buyers bear it, with indemnity flowing back.',
                  'source': 'Seasalt AI ([KBFaRW7QmVQ @ 00:33:10])'},
                 {'label': 'RTB Pay-Per-Call Bid Range',
                  'metric': 'RTB Pay-Per-Call Bid Range',
                  'value': '$20 to $1,000 per call',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Calldrive buyers bid with no fixed cost per call. Calls route to the highest '
                             'earnings per call, and lower bids mean fewer calls.',
                  'source': 'Calldrive ([jHMaZ1k0rpY @ 00:06:16])'},
                 {'label': 'Industry Readiness Poll',
                  'metric': 'Industry Readiness Poll',
                  'value': '20% ready, 50% testing, 22% have an idea, 7% not started',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'ActiveProspect and boberdoo webinar poll of lead-gen operators, taken 111 '
                             'days before January 27 enforcement.',
                  'source': 'ActiveProspect, Inc. ([uXTg2yB_ZTM @ 00:08:03])'}],
 'sections': [{'section': 1,
               'title': 'The Practitioner Consensus: One Seller, One Checkbox, One Record',
               'paragraphs': ['Every operator who addresses the rule lands on the same core shift. Consent '
                              "now attaches to one named business, and the 'our partners' blanket is "
                              'finished. Evocalize sets the bar as a box the consumer physically checks '
                              'that names the exact downstream contact (loan officer, agent or provider), '
                              "presented 'clear and conspicuous.' Evocalize adds that the caller must "
                              "'take physical possession of the consent record before making the outbound "
                              "call' [h8PlsMHs16k @ 00:01:27]. Mike Fitzpatrick describes a mandatory "
                              "per-company checkbox plus a contact-method box. He says the '72 other "
                              "companies' style of batch consent that powered the old lead-gen loophole is "
                              "out [N9n3qM6ZlfI @ 00:13:04]. ActiveProspect's Benjamin Nafarro confirms "
                              'link-out partner lists are no longer allowed. Exclusive sellers now '
                              'dynamically insert a single company, and shared sellers move to individual '
                              'checkboxes that bring more post-rejects [uXTg2yB_ZTM @ 00:14:07]. '
                              "StreetText's Jonathan gives the street version: the recipient must see the "
                              'business receiving consent, and handing that consent to a second or third '
                              'business is no longer legal. In his telling, the change ends consumers '
                              "being 'round robin' by businesses chasing the same lead, which is exactly "
                              'the reseller loophole the rule targets [5wE-LfVEhgk @ 00:02:09]. For anyone '
                              'running ping-post or aged-lead resale, the shared conclusion is blunt: the '
                              'old multi-buyer consent asset no longer carries forward.',
                              'The baseline form mechanics are just as uniform across speakers. '
                              "TechMarketer's build uses a single select for each item, 'no select all,' "
                              "and 'no pre-check,' which he calls 'a big one.' Interest is tied to a "
                              'specific product, the partner-communications option is removable, and a '
                              'final confirmation step closes the flow [B9lfPgUUls0 @ 00:00:43]. Pitchit '
                              'says consent requires affirmative action through an unchecked box and '
                              "cannot be implied from inactivity or browsing. Its framing: 'you can't just "
                              'assume anything it needs to be Express written consent for very specific '
                              "use cases' [k6g6hxICGH4 @ 00:04:03]. Seasalt AI's Amy Chan says each "
                              'regulated technology must be named explicitly in the consent language: '
                              'automated SMS, recorded voice, IVR, voice drop and AI voice calls. She also '
                              'rules out pre-checked boxes and consent hidden behind a privacy hyperlink '
                              '[KBFaRW7QmVQ @ 00:18:57]. TrackDrive reduces the record standard to one '
                              "line operators repeat on every vertical: 'If you can't show who agreed, "
                              "when, and to what, assume you can't prove it.' It pairs that with a warning "
                              "that 'vague wording like our partners can be a real problem' for outbound "
                              'follow-up [sFVqp8Vluy8 @ 00:03:34]. The working standard that emerges is a '
                              'named business, an unchecked box, every channel spelled out, and a record '
                              'that captures who, when and what.',
                              'Practitioners also agree on who carries the risk, and it is the buyer. '
                              'Pitchit says the buyer bears the burden of verifying prior express written '
                              'consent and must document when, how and where it was obtained. Pitchit '
                              'tells buyers to request the full consent paragraph for their legal team and '
                              'to add contractual indemnification [k6g6hxICGH4 @ 00:00:35]. Eric Troutman '
                              'says lead sellers create the risk but buyers bear it, with indemnity '
                              "flowing back up the chain. He puts it plainly: 'remember if you're a lead "
                              "buyer the risk is on you' [KBFaRW7QmVQ @ 00:33:39]. Fitzpatrick agrees the "
                              'buyer still bears the burden of proof, and he predicts lead cost will '
                              "'extremely increase' as the batch-consent supply dries up [N9n3qM6ZlfI @ "
                              "00:18:12]. Socius's Brian brought the home-service vertical to Socius in "
                              '2008 and works with over half the top 500 remodelers. He expects higher '
                              'cost per lead from aggregators but better quality. In his view, big brands '
                              'gain while small and mid-sized companies are disadvantaged, and bulk-list '
                              'buyers face the heaviest disruption [2YZuiPP4QWc @ 00:08:13]. The consensus '
                              "economics are pricier, cleaner inventory, with the buyer's own "
                              'documentation as the final line of defense when a consumer, plaintiff or '
                              'regulator challenges a contact.'],
               'table': {'caption': 'Consensus Rules Every Speaker Treats as Baseline for One-to-One Lead '
                                    'Buying',
                         'headers': ['Consensus Rule',
                                     'What Practitioners Require',
                                     'Operator Implication',
                                     'Expert Source'],
                         'rows': [['One named business per consent checkbox',
                                   'Consumer physically checks a box naming the exact downstream contact, '
                                   'presented clear and conspicuous',
                                   'Shared partner lists and link-out pages stop working as consent '
                                   'vehicles',
                                   'Evocalize ([h8PlsMHs16k @ 00:00:00])'],
                                  ['No pre-checked or select-all boxes on forms',
                                   'Single select per item, no select all, no pre-check, plus a final '
                                   'confirmation step',
                                   'Form builds must be rebuilt so each consent is a separate deliberate '
                                   'action',
                                   'TechMarketer ([B9lfPgUUls0 @ 00:00:43])'],
                                  ['Ad content and context must match the buyer',
                                   'A mortgage ad means only mortgage providers can receive that '
                                   "consumer's consent",
                                   'Cross-vertical resale of a lead to unrelated buyers is off the table',
                                   'Evocalize ([h8PlsMHs16k @ 00:00:52])'],
                                  ['Consent does not transfer between buyers or resellers',
                                   'Consent does not transfer over, and buyers need one-to-one consent as '
                                   'well',
                                   'Every downstream buyer must be named at capture, not added after the '
                                   'fact',
                                   'ActiveProspect, Inc. ([uXTg2yB_ZTM @ 00:47:12])'],
                                  ['Every regulated technology named explicitly in consent language',
                                   'Automated SMS, recorded voice, IVR, voice drop and AI voice calls each '
                                   'named',
                                   'Unlisted channels cannot be switched on later without fresh consent '
                                   'from the consumer',
                                   'Seasalt AI ([KBFaRW7QmVQ @ 00:18:57])'],
                                  ['Buyer carries the burden of proving consent',
                                   'Document when, how and where consent was obtained, plus the full '
                                   'consent paragraph',
                                   "Contracts need indemnification, and the buyer's own records decide any "
                                   'dispute',
                                   'Pitchit ([k6g6hxICGH4 @ 00:00:35])'],
                                  ['Both buyer and seller retain consent records',
                                   'Disclosures name the organization, and TrustedForm certificates are '
                                   'stored in CRM and data warehouse',
                                   'Consent proof becomes a permanent data asset rather than a vendor-held '
                                   'artifact',
                                   'ActiveProspect, Inc. ([2YZuiPP4QWc @ 00:06:34])']]}},
              {'section': 2,
               'title': 'Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['Calldrive CEO Zach Ramirez runs the most complete end-to-end pay-per-call '
                              'machine described. He sources form fills from about 22 to 23 publishers, '
                              'each owning one to 200 sites, across debt relief, business loans, roofing '
                              "and solar. He buys real-time or 'slightly aged' leads, but only with 'a "
                              "trusted form or a Jayiah token' as third-party proof of consent. He stacks "
                              "more proof on top: 'Not only do we have our Janiah token, but we have your "
                              "IP address and we have a video of you filling out the form' [jHMaZ1k0rpY @ "
                              '00:02:28]. His AI scoring model was trained on around 50,000 closed '
                              'transactions and about 150 data points, including gender, age, children, '
                              'homeowner status and credit score. It ranks a million-record list into who '
                              'to market to and who to skip [jHMaZ1k0rpY @ 00:02:45]. Pricing carries no '
                              'fixed cost per call. Buyers bid $20 to $1,000 in a CallHub RTB auction, '
                              'calls route to the highest earnings per call, and $200 in credits at $20 '
                              "per call buys 10 calls: 'once you get those 10 calls, your credits are "
                              "done' [jHMaZ1k0rpY @ 00:10:14]. TrackDrive draws the key compliance line "
                              'for this model. Inbound pay-per-call differs from outbound follow-up, which '
                              'needs documented consent naming the specific business [sFVqp8Vluy8 @ '
                              '00:01:18].',
                              'On the capture side, LeadCaptureIO places consent wherever the form has a '
                              'phone field, which in its demo is the contact step after pre-qualification. '
                              'Its templates run from one company up to 10, 20 or more checkboxes, or use '
                              'a single-company toggle with the name inserted manually [FQR1fK6va5I @ '
                              '00:00:38]. In dynamic mode, the form pings LeadByte, LeadsPedia, Lead '
                              "Prosper or a custom tool and inserts buyer names by state or zip in 'a "
                              "fraction of a second.' It runs on Leadpages, GoHighLevel, Unbounce, "
                              'Instapage, WordPress and Webflow, and a TCPA webhook field passes '
                              'per-company consent with an IP address and a confirmed or unconfirmed tag '
                              "[FQR1fK6va5I @ 00:04:31]. TechMarketer's low-cost version pipes Gravity "
                              'Forms into Airtable. Its fields cover opt-in, consent date and timestamp, '
                              'the single seller name, contact topic, method of consent, topical-relevance '
                              "notes, and an opt-out date used for 'reply stop' on SMS and MMS "
                              "[B9lfPgUUls0 @ 00:01:25]. Eli Rivera's variant uses Zapier to push each "
                              'form into a Google Doc shared with the client. He assumes A2P plus DMARC, '
                              "DKIM and SPF are already in place and pays about '$150 a month' for a DNC "
                              'scrubbing service, recommending double opt-in on top [OwaZv3PLkqg @ '
                              '00:10:05].',
                              "For SMS follow-up, Hatch's Kristen McCormack says 10DLC is registered "
                              'through a campaign service provider while the carrier manually vets your '
                              'site. The form must carry the company name, an SMS mention, the purpose, '
                              "message frequency, 'message and data rates apply,' 'consent is not a "
                              "condition of purchase,' and links to SMS terms and the privacy policy "
                              '[2YZuiPP4QWc @ 00:23:39]. Her deliverability numbers are specific. Stay '
                              'under 320 characters and aim for about 150. Never mention other phone '
                              'numbers, and never blast leads that are 180 to 200 days old, because high '
                              'opt-out rates can get 33 to 66 percent of messages blocked [2YZuiPP4QWc @ '
                              '00:39:10]. On lead structure, ActiveProspect and boberdoo split the market '
                              'in two. Exclusive models dynamically insert a single company and fit legal, '
                              'health and Medicare. Shared checkbox models suit home improvement and auto. '
                              "Nafarro calls the choice 'very vertical specific' [uXTg2yB_ZTM @ 00:19:45]. "
                              'Agent CRM adds the sender-reputation mechanic that raises the stakes on '
                              'every text. A2P is now tied to the EIN, so spam flags follow the sender '
                              'across platforms rather than staying with one texting vendor [TFi09QYEol8 @ '
                              '00:03:31]. Opt-out rate, delivery rate and volume become the core dashboard '
                              'metrics.'],
               'table': {'caption': 'Street-Level Tools, Settings and Unit Economics Quoted by Operators',
                         'headers': ['Mechanic or Tool',
                                     'Exact Setup or Number',
                                     'How Operators Use It',
                                     'Expert Source'],
                         'rows': [['Calldrive RTB call auction on CallHub',
                                   'Buyers bid $20 to $1,000 per call with no fixed cost per call',
                                   'Calls route to the highest earnings per call, so lower bids get fewer '
                                   'calls',
                                   'Calldrive ([jHMaZ1k0rpY @ 00:06:16])'],
                                  ['Prepaid call credit math for buyers',
                                   '$200 in credits at $20 per call buys exactly 10 calls',
                                   'No minimums, contracts or fees, with caps, concurrency and state '
                                   'exclusions set by the buyer',
                                   'Calldrive ([jHMaZ1k0rpY @ 00:10:14])'],
                                  ['AI lead scoring before nurture spend',
                                   'Trained on around 50,000 closed transactions and about 150 data points',
                                   'Ranks a million-record list into who to market to and who to skip',
                                   'Calldrive ([jHMaZ1k0rpY @ 00:02:45])'],
                                  ['Dynamic buyer-name insertion on lead forms',
                                   'Pings LeadByte, LeadsPedia or Lead Prosper and inserts buyers by state '
                                   'or zip',
                                   'Names change per visitor in a fraction of a second, with consent '
                                   'passed by webhook',
                                   'LeadCaptureIO ([FQR1fK6va5I @ 00:04:31])'],
                                  ['DNC scrubbing subscription for outbound lists',
                                   'Scrubbing service runs about $150 a month for his campaigns',
                                   'Paired with double opt-in before any automated text, email or '
                                   'voicemail blast',
                                   'Eli Rivera | The AI Growth Operator ([OwaZv3PLkqg @ 00:10:05])'],
                                  ['SMS length and list-age deliverability limits',
                                   'Under 320 characters, aim near 150, and skip leads 180 to 200 days old',
                                   'High opt-out rates can get 33 to 66 percent of messages blocked',
                                   'ActiveProspect, Inc. ([2YZuiPP4QWc @ 00:35:32])'],
                                  ['Opt-out honoring window and documentation',
                                   'Honor opt-outs within 10 business days, then screenshot and upload '
                                   'them',
                                   'Every revocation lives in the CRM as evidence alongside the original '
                                   'consent',
                                   'Mike Fitzpatrick ([N9n3qM6ZlfI @ 00:15:58])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Conversion and Monetization Edges Operators Shared',
                           'body': 'These are small structural choices that practitioners say protect '
                                   'yield after the consent change.',
                           'items': ['Bid per company, not per whole lead. ActiveProspect and boberdoo say '
                                     "'we advocate an individual bid scenario,' and with 15 buyers the "
                                     'form shows 15 checkboxes [ActiveProspect, Inc. — uXTg2yB_ZTM @ '
                                     '00:44:12].',
                                     "Watch the call to action on shared forms. A 'select the best' prompt "
                                     "produced single picks, and switching the wording to 'compare' fixed "
                                     'it [ActiveProspect, Inc. — uXTg2yB_ZTM @ 00:22:42].',
                                     'Re-engage existing leads by email or SMS that sends them to a '
                                     'landing page capturing fresh one-to-one consent, and get consent '
                                     'covering every technology you might later use [Seasalt AI — '
                                     'KBFaRW7QmVQ @ 00:46:10].',
                                     "Facebook ads already display the advertiser's business, which aligns "
                                     'self-generated leads with the requirement that the recipient sees '
                                     'who is receiving consent [StreetText — 5wE-LfVEhgk @ 00:02:53].']},
               'sop_steps': [{'step': 1,
                              'title': 'Rebuild the Consent Form Per Seller',
                              'action': 'Put a separate unchecked box for each named seller and each '
                                        'regulated technology wherever a phone field appears.',
                              'detail': 'Use single select per item, no select all and no pre-check, tied '
                                        'to a specific product interest, with a final confirmation step '
                                        '[TechMarketer — B9lfPgUUls0 @ 00:00:43]. Name automated SMS, '
                                        'recorded voice, IVR, voice drop and AI voice calls explicitly '
                                        '[Seasalt AI — KBFaRW7QmVQ @ 00:18:57].'},
                             {'step': 2,
                              'title': 'Capture and Store the Proof Stack',
                              'action': 'Attach a third-party certificate, IP address and timestamp to '
                                        'every lead and push them into your own systems.',
                              'detail': "Calldrive requires a 'trusted form or a Jayiah token' and adds IP "
                                        'address, digital signature and video of the form fill [Calldrive '
                                        '— jHMaZ1k0rpY @ 00:02:08]. Store TrustedForm certificates in the '
                                        'CRM and data warehouse so both buyer and seller retain the record '
                                        '[ActiveProspect, Inc. — 2YZuiPP4QWc @ 00:06:34].'},
                             {'step': 3,
                              'title': 'Scrub, Suppress and Log Opt-Outs',
                              'action': 'Run national, state and internal DNC checks before outbound '
                                        'contact, and log every opt-out with its date and action.',
                              'detail': 'Check national, state and internal lists and honor opt-outs '
                                        'quickly [TrackDrive — sFVqp8Vluy8 @ 00:02:15]. Budget about $150 '
                                        'a month for scrubbing and add double opt-in [Eli Rivera | The AI '
                                        'Growth Operator — OwaZv3PLkqg @ 00:10:05]. Honor opt-outs within '
                                        '10 business days and screenshot them into the CRM [Mike '
                                        'Fitzpatrick — N9n3qM6ZlfI @ 00:15:58].'},
                             {'step': 4,
                              'title': 'Route Calls Through Buyer-Controlled RTB',
                              'action': 'Sell inbound calls by auction with buyer-set schedules, caps, '
                                        'concurrency, state exclusions and budgets.',
                              'detail': 'Calldrive buyers control schedule, concurrency, caps, state '
                                        'exclusions and hourly, daily or weekly budget, with no minimums, '
                                        'contracts or fees [Calldrive — jHMaZ1k0rpY @ 00:08:34]. Calls '
                                        'route to the highest earnings per call from bids between $20 and '
                                        '$1,000 [Calldrive — jHMaZ1k0rpY @ 00:06:16].'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The first fault line is whether one-to-one consent is live law at all. Alex '
                              'Branning and Will Winter of Agent CRM say the requirement was paused and '
                              "then they 'threw the whole thing out entirely,' yet they still tell agents "
                              "to 'act as if this is in play,' honor STOP, track consent, and favor fresh "
                              'exclusive leads [TFi09QYEol8 @ 00:00:36]. Eric Troutman of TCPAWorld, on '
                              'the Seasalt AI session, ran the opposite read: the Insurance Marketing '
                              "Coalition's Hobbs Act challenge drew three skeptical 11th Circuit judges "
                              'but no stay, the executive order only asks agencies to consider a 60-day '
                              'stay, the commission sits split 2-2, and the REACH emergency petition is no '
                              'sure thing, so treat January 27 as live [KBFaRW7QmVQ @ 00:30:23]. B2B '
                              'splits the room the same way. Eli Rivera calls B2B status unclear and errs '
                              'on caution even for commercial real estate outreach, while declaring the '
                              'lead-gen loophole closed [OwaZv3PLkqg @ 00:06:41]. Mike Fitzpatrick relays '
                              "that attorneys told him B2B is 'not covered' and expects the rule to choke "
                              'mortgage trigger leads and batch-consent plays like Zillow, realtor.com, '
                              'CarGurus and Bankrate [N9n3qM6ZlfI @ 00:16:46]. The operator takeaway both '
                              'camps land on: build the consent stack regardless of which read wins.',
                              "Form architecture is the second split. TechMarketer's build bans 'select "
                              "all' and pre-checked boxes outright, uses a single select per item, keeps "
                              'the partner-communications option removable, and ends on a final '
                              'confirmation step [B9lfPgUUls0 @ 00:00:43]. LeadCaptureIO pushes the other '
                              "way for conversion: a real person's photo, oversized checkboxes, "
                              'multi-company templates scaling from 1 to 10, 20 or more buyers, and a '
                              "'select all' link, with buyer names pinged from LeadByte, LeadsPedia or "
                              "Lead Prosper and injected by state or zip in 'a fraction of a second' "
                              '[FQR1fK6va5I @ 00:00:13]. The ActiveProspect and boberdoo panel frames it '
                              'as exclusive versus shared: exclusive dynamically inserts one company and '
                              'fits legal, health and Medicare, while shared runs checkboxes, fits home '
                              'improvement and auto, and eats more post-rejects; their attendee poll '
                              'landed at 38% exclusive, 8% shared and 37% mix, and they call the choice '
                              "'very vertical specific' [uXTg2yB_ZTM @ 00:19:45]. Monetization splits too. "
                              "That panel advocates 'an individual bid scenario,' pricing each company "
                              "rather than the whole lead, while Calldrive's Zach Ramirez runs one RTB "
                              'auction where buyers bid $20 to $1,000 and calls route to the highest '
                              "earnings per call, 'just like Google pay-per-click or Meta pay-per-click' "
                              '[jHMaZ1k0rpY @ 00:07:27].',
                              'Consent lifespan and scrubbing draw the sharpest contradictions. Michael '
                              'Ponto of ActiveProspect warns that if your legal team allows contact up to '
                              '90 days after submission, providers must switch 90 days early [2YZuiPP4QWc '
                              "@ 00:07:36]. Eli Rivera's workflow banks a 12-month permission off an "
                              'opt-in text and email blast, routes replies into an inbound Twilio number '
                              "answered by a voice AI agent, then fires a 'yes' text as a second consent "
                              'layer [OwaZv3PLkqg @ 00:12:41]. Eric Troutman counters that properly '
                              "captured one-to-one written consent 'doesn't expire in 90 days or 18 "
                              "months,' and that with proper one-to-one consent no DNC scrub is needed, "
                              "even as Rivera pays '$150 a month' for a scrubbing service [KBFaRW7QmVQ @ "
                              '00:45:32]. On opt-out language, Kristen McCormack of Hatch reports lawyers '
                              'differ on repeating it after the first text, while Troutman says the first '
                              'message suffices legally even though CTIA and carriers impose more. Manual '
                              "dialing is the last split: StreetText's Jonathan says anyone hand dialing "
                              "or hand delivering a message 'can still do business as normal' [5wE-LfVEhgk "
                              '@ 00:00:34], but Troutman says ATDS status turns on system capacity, '
                              "preview dialers are 'probably' an ATDS, and whether it is 'fingers on the "
                              "keypad' is 'actually irrelevant.'"],
               'table': {'caption': 'Side-by-side practitioner fault lines on one-to-one consent, form '
                                    'design, and lead monetization',
                         'headers': ['Fault Line', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Whether one-to-one consent is enforceable law right now',
                                   'Agent CRM says one-to-one consent was paused, then thrown out '
                                   'entirely, but agents should act as if it is in play',
                                   'Eric Troutman says no stay was entered, the commission sits split 2-2, '
                                   'so treat January 27 as live',
                                   'Agent CRM ([TFi09QYEol8 @ 00:00:36]) vs Seasalt AI ([KBFaRW7QmVQ @ '
                                   '00:30:23])'],
                                  ['Whether B2B outreach falls inside the new consent rule',
                                   'Eli Rivera calls B2B status unclear and errs on the side of caution '
                                   'for commercial real estate campaigns',
                                   'Mike Fitzpatrick relays that attorneys told him B2B outreach is not '
                                   'covered by the rule at all',
                                   'Eli Rivera | The AI Growth Operator ([OwaZv3PLkqg @ 00:06:41]) vs Mike '
                                   'Fitzpatrick ([N9n3qM6ZlfI @ 00:16:46])'],
                                  ['Dollar exposure quoted per text, call, or violation',
                                   'Eli Rivera quotes $500 to $1,500 per incident while Amy Chan quotes '
                                   '$500 to $2,000 per text or call',
                                   'Mike Fitzpatrick quotes $100 per violation but warns that class '
                                   'actions can reach into the millions',
                                   'Eli Rivera | The AI Growth Operator ([OwaZv3PLkqg @ 00:07:15]); '
                                   'Seasalt AI ([KBFaRW7QmVQ @ 00:14:15]) vs Mike Fitzpatrick '
                                   '([N9n3qM6ZlfI @ 00:22:25])'],
                                  ['Checkbox user experience on the consent step of the form',
                                   'TechMarketer runs single select per item with no select all and no '
                                   'pre-checked boxes anywhere',
                                   'LeadCaptureIO runs large checkboxes, up to 20 or more companies, plus '
                                   'a select all link for conversion',
                                   'TechMarketer ([B9lfPgUUls0 @ 00:00:43]) vs LeadCaptureIO ([FQR1fK6va5I '
                                   '@ 00:00:13])'],
                                  ['Exclusive single-company lead model versus shared multi-buyer lead '
                                   'model',
                                   'Exclusive dynamically inserts one company and fits legal, health and '
                                   'Medicare verticals best',
                                   'Shared shows a checkbox per buyer, fits home improvement and auto, but '
                                   'brings more post-rejects',
                                   'ActiveProspect, Inc. ([uXTg2yB_ZTM @ 00:19:45])'],
                                  ['Whether DNC scrubbing is still required on consented leads',
                                   'Eli Rivera recommends double opt-in plus a DNC scrubbing service '
                                   'costing $150 a month',
                                   'Eric Troutman says proper one-to-one consent means no DNC scrub is '
                                   'needed on those contacts',
                                   'Eli Rivera | The AI Growth Operator ([OwaZv3PLkqg @ 00:10:05]) vs '
                                   'Seasalt AI ([KBFaRW7QmVQ @ 00:54:46])'],
                                  ['How long a captured consent can be worked before it goes stale',
                                   'Michael Ponto says if legal allows 90 days post-submission, providers '
                                   'must switch 90 days early',
                                   'Eric Troutman says complete one-to-one written consent does not expire '
                                   'in 90 days or 18 months',
                                   'ActiveProspect, Inc. ([2YZuiPP4QWc @ 00:07:36]) vs Seasalt AI '
                                   '([KBFaRW7QmVQ @ 00:45:32])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The most expensive failure is a consent record that collapses under '
                              'scrutiny. Eric Troutman says courts already found a bills.com lead-gen web '
                              "flow unenforceable, and of 10 circulating one-to-one forms 'probably only "
                              "two' pass; lead sellers create the risk, buyers bear it, and indemnity "
                              'flows back [KBFaRW7QmVQ @ 00:33:10]. ActiveProspect confirms link-out '
                              "partner lists are dead and logged a live testing trap: a 'select the best' "
                              'call to action pushed consumers into single picks, starving shared buyers, '
                              "until the copy was swapped to 'compare' [uXTg2yB_ZTM @ 00:22:42]. "
                              "TrackDrive flags vague wording like 'our partners' as 'a real problem' and "
                              "sets the proof bar bluntly: 'If you can't show who agreed, when, and to "
                              "what, assume you can't prove it' [sFVqp8Vluy8 @ 00:03:34]. Calldrive's "
                              'answer is redundancy, stacking a TrustedForm or Janiah token with IP '
                              "address, digital signature and video of the form fill: 'Not only do we have "
                              'our Janiah token, but we have your IP address and we have a video of you '
                              "filling out the form' [jHMaZ1k0rpY @ 00:02:28]. Build that evidence stack "
                              'before the first dial, because the buyer is the party left holding the '
                              'proof burden when a plaintiff comes calling.',
                              'Legacy inventory is the second trap. Amy Chan of Seasalt AI warns that '
                              "existing CRM contacts, her example being '2,000,' lose consent under the "
                              'rule, and one lead-gen company told her it is closing because of it '
                              "[KBFaRW7QmVQ @ 00:15:20]. ActiveProspect states flatly that consent 'does "
                              "not transfer over,' so 'the buyers need to have one-to-one consent as "
                              "well,' and with 15 buyers the form shows 15 checkboxes [uXTg2yB_ZTM @ "
                              "00:47:12]. TechMarketer pegs the damage at '99%' of leads, customers and "
                              'prospects needing consent redone [B9lfPgUUls0 @ 00:00:00]. Texting old '
                              'lists compounds it: Kristen McCormack says blasting 180 to 200 day old '
                              'leads spikes opt-outs, and high opt-out rates can get 33% to 66% of '
                              'messages blocked; keep messages under 320 characters, aim near 150, skip '
                              'other phone numbers, and never try to evade filters [2YZuiPP4QWc @ '
                              "00:39:10]. Troutman's salvage route is to re-engage existing leads by email "
                              'or SMS that sends them to a landing page with one-to-one consent, and to '
                              'manual-dial valid existing written-consent leads while auto-dialers, AI '
                              'voice, prerecorded IVR and ringless voicemail stay parked until fresh '
                              'consent lands.',
                              'Economics checks cut both ways. Mike Fitzpatrick predicts lead cost will '
                              "'extremely increase' while the buyer still carries the burden of proof, and "
                              'expects batch-consent sources to lose their edge [N9n3qM6ZlfI @ 00:18:12]. '
                              'Eli Rivera reports a 15% drop in PPC clicks from AI summaries, yet one '
                              'commercial real estate push of 8,514 texts, emails and ringless voicemails '
                              'produced 29 deals and 60+ calls, run on top of A2P registration plus DMARC, '
                              'DKIM and SPF [OwaZv3PLkqg @ 00:01:35]. Calldrive prices pay-per-call with '
                              'no fixed cost, no minimums, no contracts and no fees: $200 in credits at '
                              "$20 per call buys 10 calls, 'then, once you get those 10 calls, your "
                              "credits are done,' and lower bids simply mean fewer calls [jHMaZ1k0rpY @ "
                              '00:10:14]. Medicare operators carry an extra script tax. Benjamin of Senior '
                              'Marketing Specialists says the TPMO disclaimer must land within the first '
                              '60 seconds of a sales call, which begins when the beneficiary asks about '
                              'products, and must also run in email, chat, texting, print and TV, with '
                              'organization and product counts pulled from the CMS landscape Excel file at '
                              'the state level [ecCFdANLCZc @ 00:02:29].'],
               'table': {'caption': 'Firsthand failure modes, mechanisms, and the operator fixes or unit '
                                    'economics practitioners reported',
                         'headers': ['Failure Mode',
                                     'What Went Wrong',
                                     'Operator Fix or Economics',
                                     'Expert Source'],
                         'rows': [['One-to-one form copy that fails legal scrutiny',
                                   'Of 10 circulating one-to-one forms probably only two pass, and a '
                                   'bills.com flow was found unenforceable',
                                   'Use the free Troutman Amin 15 template as the touchstone because the '
                                   'lead buyer carries the risk',
                                   'Seasalt AI ([KBFaRW7QmVQ @ 00:33:10])'],
                                  ['Call-to-action copy that starves shared lead buyers',
                                   "A 'select the best' prompt pushed consumers into picking a single "
                                   'company on the consent step',
                                   "Switching the call-to-action wording to 'compare' fixed the "
                                   'single-pick behavior in testing',
                                   'ActiveProspect, Inc. ([uXTg2yB_ZTM @ 00:22:42])'],
                                  ['Blasting aged leads by text after months of silence',
                                   'Texting 180 to 200 day old leads drives high opt-out rates that '
                                   'trigger carrier blocking',
                                   'High opt-outs can get 33% to 66% of messages blocked; keep texts near '
                                   '150 characters',
                                   'ActiveProspect, Inc. ([2YZuiPP4QWc @ 00:39:10])'],
                                  ['Spam flags that follow the sender everywhere',
                                   'A2P registration is now tied to the EIN, so spam flags follow the '
                                   'business across platforms',
                                   'Honor STOP, track consent, and prefer fresh exclusive leads over '
                                   'recycled shared inventory',
                                   'Agent CRM ([TFi09QYEol8 @ 00:03:31])'],
                                  ['Auditing lead vendors too rarely to catch problems',
                                   "Semiannual, annual, or no audits are 'definitely not a good idea' for "
                                   'third-party lead buyers',
                                   'Audit monthly or quarterly and keep point-in-time snapshots so audits '
                                   'can be compared',
                                   'Pitchit ([k6g6hxICGH4 @ 00:04:20])'],
                                  ['Recording calls and using vague partner consent wording',
                                   "Some states require all parties to consent to recording, and 'our "
                                   "partners' wording is a real problem",
                                   'Play a short recording disclosure and name the specific business in '
                                   'outbound consent language',
                                   'TrackDrive ([sFVqp8Vluy8 @ 00:01:55])'],
                                  ['Working saved data lists long after purchase',
                                   'Saved lists can be re-accessed without re-buying, but numbers may '
                                   'change on an eight-month-old list',
                                   'Filter out records with no mobile number first; that step removed '
                                   'about a thousand people',
                                   'DatatoLeads - B2B and B2C Wholesale Data and Leads ([1zvwOs0qmmg @ '
                                   '00:00:43])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Kill-Switch Checks Before Any Outbound Touch',
                           'body': 'Every item below is a stop point practitioners reported hitting '
                                   'firsthand. If any check fails, the dial, text, or AI voice campaign '
                                   'does not launch.',
                           'items': ['No outbound voice AI goes live until AI and robo-dialer consent '
                                     'language sits in your privacy policy and terms [Agent CRM — '
                                     'TFi09QYEol8 @ 00:07:30].',
                                     'The caller must take physical possession of the consent record '
                                     'before making the outbound call, with the consumer having checked a '
                                     'box naming that exact company [Evocalize — h8PlsMHs16k @ 00:01:27].',
                                     'Treat any new vertical or new state as a reason to stop and check '
                                     'calling hours, licensing, and advertising claims, especially in '
                                     'insurance, lending, and health [TrackDrive — sFVqp8Vluy8 @ '
                                     '00:02:36].',
                                     'Reject any lead source showing vague or blanket consent, missing '
                                     'documentation, or high volume with minimal verification [Pitchit — '
                                     'k6g6hxICGH4 @ 00:07:03].']}}],
 'pull_quote': '"If you can\'t show who agreed, when, and to what, assume you can\'t prove it." — '
               'TrackDrive (sFVqp8Vluy8 @ 00:03:34).',
 'diagram_id': 'diag-02',
 'action_checklist': ['Put an unchecked, clear and conspicuous checkbox naming each exact downstream '
                      'company on the form, and keep content matched to context so a mortgage ad only '
                      'feeds mortgage providers [Evocalize — h8PlsMHs16k @ 00:00:52].',
                      'Log every submission into a consent table with client name, email, opt-in status, '
                      'consent date and timestamp, single seller name, contact topic, method of consent, '
                      'and opt-out date [TechMarketer — B9lfPgUUls0 @ 00:01:25].',
                      'Pass consent per company through a TCPA webhook field into tools like '
                      'ActiveCampaign, LeadByte, or LeadsPedia, capturing IP address and tagging each '
                      'record confirmed or unconfirmed [LeadCaptureIO — FQR1fK6va5I @ 00:04:18].',
                      'Store TrustedForm certificates in both the CRM and the data warehouse, because '
                      'buyer and seller must each retain consent records [ActiveProspect, Inc. — '
                      '2YZuiPP4QWc @ 00:06:34].',
                      'Write proof and retention of consent, a right to audit, and indemnification clauses '
                      'into every lead contract, then audit sellers monthly or quarterly [Pitchit — '
                      'k6g6hxICGH4 @ 00:05:09].',
                      'Honor opt-outs within 10 business days, screenshot and upload them to the CRM, and '
                      'run double opt-in on new contacts [Mike Fitzpatrick — N9n3qM6ZlfI @ 00:15:58].'],
 'statutory_citations': [{'title': 'Seasalt AI — (UPDATE 1/21/2025) New One-to-One Consent Rules: TCPA '
                                   'Compliance w/ TCPAWorld Troutman & Seasalt.ai [00:25:06]',
                          'url': 'https://www.youtube.com/watch?v=KBFaRW7QmVQ&t=1506s',
                          'relevance': 'Primary practitioner testimony on the individual company-selection '
                                       'requirement, form pass rates, regulated technologies, and stay '
                                       'status.'},
                         {'title': 'ActiveProspect, Inc. — FCC SERIES: EPISODE 17 | Lead-Gen 2.0: A '
                                   'detailed compliance checklist for 1:1 consent management [00:14:07]',
                          'url': 'https://www.youtube.com/watch?v=uXTg2yB_ZTM&t=847s',
                          'relevance': 'Primary practitioner testimony on the end of link-out partner '
                                       'lists and exclusive versus shared consent models.'},
                         {'title': 'Pitchit — Summary of the New TCPA Rules Regarding Third Party '
                                   'Affiliate Leads Effective January 27, 2025 [00:00:35]',
                          'url': 'https://www.youtube.com/watch?v=k6g6hxICGH4&t=35s',
                          'relevance': 'Primary practitioner testimony on buyer burden of proof, contract '
                                       'clauses, audit cadence, and vendor red flags.'},
                         {'title': 'TrackDrive — Compliance Essentials | Pay-Per-Call Masterclass '
                                   '[00:03:34]',
                          'url': 'https://www.youtube.com/watch?v=sFVqp8Vluy8&t=214s',
                          'relevance': 'Primary practitioner testimony on pay-per-call consent proof, '
                                       'recording disclosure, and DNC suppression.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'B9lfPgUUls0',
                       'title': 'TCPA Compliance Made Easy: 1:1 Consent Tracking Guide',
                       'channel': 'TechMarketer',
                       'author': 'TechMarketer',
                       'text': 'Single select for each item, no select all, and no pre-check, which is a '
                               'big one.',
                       'tip': 'Single select for each item, no select all, and no pre-check, which is a '
                              'big one.',
                       'timestamp': 43,
                       'timestamp_seconds': 43,
                       'timestamp_label': '[00:00:43]',
                       'url': 'https://www.youtube.com/watch?v=B9lfPgUUls0&t=43s',
                       'markdown': '[00:00:43](https://www.youtube.com/watch?v=B9lfPgUUls0&t=43s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'jHMaZ1k0rpY',
                       'title': 'Calldrive\'s "Pay-Per-Call" Process Explained: Compliant Lead Capture, AI '
                                'Scoring & Real-Time Routing',
                       'channel': 'Calldrive',
                       'author': 'Calldrive',
                       'text': 'Not only do we have our Janiah token, but we have your IP address and we '
                               'have a video of you filling out the form.',
                       'tip': 'Not only do we have our Janiah token, but we have your IP address and we '
                              'have a video of you filling out the form.',
                       'timestamp': 148,
                       'timestamp_seconds': 148,
                       'timestamp_label': '[00:02:28]',
                       'url': 'https://www.youtube.com/watch?v=jHMaZ1k0rpY&t=148s',
                       'markdown': '[00:02:28](https://www.youtube.com/watch?v=jHMaZ1k0rpY&t=148s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'jHMaZ1k0rpY',
                       'title': 'Calldrive\'s "Pay-Per-Call" Process Explained: Compliant Lead Capture, AI '
                                'Scoring & Real-Time Routing',
                       'channel': 'Calldrive',
                       'author': 'Calldrive',
                       'text': 'Then, once you get those 10 calls, your credits are done.',
                       'tip': 'Then, once you get those 10 calls, your credits are done.',
                       'timestamp': 614,
                       'timestamp_seconds': 614,
                       'timestamp_label': '[00:10:14]',
                       'url': 'https://www.youtube.com/watch?v=jHMaZ1k0rpY&t=614s',
                       'markdown': '[00:10:14](https://www.youtube.com/watch?v=jHMaZ1k0rpY&t=614s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ecCFdANLCZc',
                       'title': 'TPMO Disclaimer Breakdown',
                       'channel': 'Senior Marketing Specialists',
                       'author': 'Senior Marketing Specialists',
                       'text': 'The disclaimer must be said within the first 60 seconds of a sales call, '
                               'and a sales call begins when the beneficiary asks about products or '
                               'details.',
                       'tip': 'The disclaimer must be said within the first 60 seconds of a sales call, '
                              'and a sales call begins when the beneficiary asks about products or '
                              'details.',
                       'timestamp': 149,
                       'timestamp_seconds': 149,
                       'timestamp_label': '[00:02:29]',
                       'url': 'https://www.youtube.com/watch?v=ecCFdANLCZc&t=149s',
                       'markdown': '[00:02:29](https://www.youtube.com/watch?v=ecCFdANLCZc&t=149s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'OwaZv3PLkqg',
                       'title': 'New FCC TCPA Compliance Rules 2025: Avoid $1,500 Fines',
                       'channel': 'Eli Rivera | The AI Growth Operator',
                       'author': 'Eli Rivera | The AI Growth Operator',
                       'text': 'Fines run $500 to $1,500 per incident.',
                       'tip': 'Fines run $500 to $1,500 per incident.',
                       'timestamp': 435,
                       'timestamp_seconds': 435,
                       'timestamp_label': '[00:07:15]',
                       'url': 'https://www.youtube.com/watch?v=OwaZv3PLkqg&t=435s',
                       'markdown': '[00:07:15](https://www.youtube.com/watch?v=OwaZv3PLkqg&t=435s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'h8PlsMHs16k',
                       'title': 'Understand the New FCC Rules for Lead Generation',
                       'channel': 'Evocalize',
                       'author': 'Evocalize',
                       'text': 'The caller must take physical possession of the consent record before '
                               'making the outbound call.',
                       'tip': 'The caller must take physical possession of the consent record before '
                              'making the outbound call.',
                       'timestamp': 87,
                       'timestamp_seconds': 87,
                       'timestamp_label': '[00:01:27]',
                       'url': 'https://www.youtube.com/watch?v=h8PlsMHs16k&t=87s',
                       'markdown': '[00:01:27](https://www.youtube.com/watch?v=h8PlsMHs16k&t=87s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'uXTg2yB_ZTM',
                       'title': 'FCC SERIES: EPISODE 17 | Lead-Gen 2.0: A detailed compliance checklist '
                                'for 1:1 consent management',
                       'channel': 'ActiveProspect, Inc.',
                       'author': 'ActiveProspect, Inc.',
                       'text': 'So we advocate an individual bid scenario.',
                       'tip': 'So we advocate an individual bid scenario.',
                       'timestamp': 2652,
                       'timestamp_seconds': 2652,
                       'timestamp_label': '[00:44:12]',
                       'url': 'https://www.youtube.com/watch?v=uXTg2yB_ZTM&t=2652s',
                       'markdown': '[00:44:12](https://www.youtube.com/watch?v=uXTg2yB_ZTM&t=2652s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'uXTg2yB_ZTM',
                       'title': 'FCC SERIES: EPISODE 17 | Lead-Gen 2.0: A detailed compliance checklist '
                                'for 1:1 consent management',
                       'channel': 'ActiveProspect, Inc.',
                       'author': 'ActiveProspect, Inc.',
                       'text': 'So, the buyers need to have one-to-one consent as well.',
                       'tip': 'So, the buyers need to have one-to-one consent as well.',
                       'timestamp': 2851,
                       'timestamp_seconds': 2851,
                       'timestamp_label': '[00:47:31]',
                       'url': 'https://www.youtube.com/watch?v=uXTg2yB_ZTM&t=2851s',
                       'markdown': '[00:47:31](https://www.youtube.com/watch?v=uXTg2yB_ZTM&t=2851s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'N9n3qM6ZlfI',
                       'title': '2024 TCPA Updates & Lead Generation Compliance',
                       'channel': 'Mike Fitzpatrick',
                       'author': 'Mike Fitzpatrick',
                       'text': 'Honor opt-outs within 10 business days, then screenshot them and upload '
                               'them to the CRM.',
                       'tip': 'Honor opt-outs within 10 business days, then screenshot them and upload '
                              'them to the CRM.',
                       'timestamp': 958,
                       'timestamp_seconds': 958,
                       'timestamp_label': '[00:15:58]',
                       'url': 'https://www.youtube.com/watch?v=N9n3qM6ZlfI&t=958s',
                       'markdown': '[00:15:58](https://www.youtube.com/watch?v=N9n3qM6ZlfI&t=958s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'TFi09QYEol8',
                       'title': 'FCC / TCPA Regulation Updates',
                       'channel': 'Agent CRM',
                       'author': 'Agent CRM',
                       'text': 'Act as if this is in play, honor STOP, track consent, and prefer fresh '
                               'exclusive leads.',
                       'tip': 'Act as if this is in play, honor STOP, track consent, and prefer fresh '
                              'exclusive leads.',
                       'timestamp': 320,
                       'timestamp_seconds': 320,
                       'timestamp_label': '[00:05:20]',
                       'url': 'https://www.youtube.com/watch?v=TFi09QYEol8&t=320s',
                       'markdown': '[00:05:20](https://www.youtube.com/watch?v=TFi09QYEol8&t=320s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '2YZuiPP4QWc',
                       'title': 'FCC SERIES: EPISODE 11 - Actionable strategies for TCPA-compliant texting '
                                'and lead gen',
                       'channel': 'ActiveProspect, Inc.',
                       'author': 'ActiveProspect, Inc.',
                       'text': 'So we always encourage you to go for the response and not the sell.',
                       'tip': 'So we always encourage you to go for the response and not the sell.',
                       'timestamp': 2083,
                       'timestamp_seconds': 2083,
                       'timestamp_label': '[00:34:43]',
                       'url': 'https://www.youtube.com/watch?v=2YZuiPP4QWc&t=2083s',
                       'markdown': '[00:34:43](https://www.youtube.com/watch?v=2YZuiPP4QWc&t=2083s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'j_cByFoLuqk',
                       'title': 'FCC SERIES: EPISODE 11 - Actionable strategies for TCPA-compliant texting '
                                'and lead gen',
                       'channel': 'ActiveProspect, Inc.',
                       'author': 'ActiveProspect, Inc.',
                       'text': 'The carriers, T-Mobile, AT&T and Verizon, manually vet your site when you '
                               'register 10DLC.',
                       'tip': 'The carriers, T-Mobile, AT&T and Verizon, manually vet your site when you '
                              'register 10DLC.',
                       'timestamp': 1861,
                       'timestamp_seconds': 1861,
                       'timestamp_label': '[00:31:01]',
                       'url': 'https://www.youtube.com/watch?v=j_cByFoLuqk&t=1861s',
                       'markdown': '[00:31:01](https://www.youtube.com/watch?v=j_cByFoLuqk&t=1861s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'k6g6hxICGH4',
                       'title': 'Summary of the New TCPA Rules Regarding Third Party Affiliate Leads '
                                'Effective January 27, 2025',
                       'channel': 'Pitchit',
                       'author': 'Pitchit',
                       'text': "You can't just assume anything, it needs to be express written consent for "
                               'very specific use cases.',
                       'tip': "You can't just assume anything, it needs to be express written consent for "
                              'very specific use cases.',
                       'timestamp': 243,
                       'timestamp_seconds': 243,
                       'timestamp_label': '[00:04:03]',
                       'url': 'https://www.youtube.com/watch?v=k6g6hxICGH4&t=243s',
                       'markdown': '[00:04:03](https://www.youtube.com/watch?v=k6g6hxICGH4&t=243s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '5wE-LfVEhgk',
                       'title': 'FCC/TCPA Compliance 2025: New Rules for Lead Generation & Automated '
                                'Messages Simplified',
                       'channel': 'StreetText',
                       'author': 'StreetText',
                       'text': "The good news is that if you're hand dialing or hand delivering a message "
                               'you can still do business as normal.',
                       'tip': "The good news is that if you're hand dialing or hand delivering a message "
                              'you can still do business as normal.',
                       'timestamp': 34,
                       'timestamp_seconds': 34,
                       'timestamp_label': '[00:00:34]',
                       'url': 'https://www.youtube.com/watch?v=5wE-LfVEhgk&t=34s',
                       'markdown': '[00:00:34](https://www.youtube.com/watch?v=5wE-LfVEhgk&t=34s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'sFVqp8Vluy8',
                       'title': 'Compliance Essentials | Pay-Per-Call Masterclass',
                       'channel': 'TrackDrive',
                       'author': 'TrackDrive',
                       'text': "If you can't show who agreed, when, and to what, assume you can't prove "
                               'it.',
                       'tip': "If you can't show who agreed, when, and to what, assume you can't prove it.",
                       'timestamp': 214,
                       'timestamp_seconds': 214,
                       'timestamp_label': '[00:03:34]',
                       'url': 'https://www.youtube.com/watch?v=sFVqp8Vluy8&t=214s',
                       'markdown': '[00:03:34](https://www.youtube.com/watch?v=sFVqp8Vluy8&t=214s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'FQR1fK6va5I',
                       'title': 'How to capture TCPA one-to-one consent in your lead capture forms',
                       'channel': 'LeadCaptureIO',
                       'author': 'LeadCaptureIO',
                       'text': 'Dynamic consent pings LeadByte, LeadsPedia, Lead Prosper or a custom tool '
                               'and inserts buyer names by state or zip in a fraction of a second.',
                       'tip': 'Dynamic consent pings LeadByte, LeadsPedia, Lead Prosper or a custom tool '
                              'and inserts buyer names by state or zip in a fraction of a second.',
                       'timestamp': 271,
                       'timestamp_seconds': 271,
                       'timestamp_label': '[00:04:31]',
                       'url': 'https://www.youtube.com/watch?v=FQR1fK6va5I&t=271s',
                       'markdown': '[00:04:31](https://www.youtube.com/watch?v=FQR1fK6va5I&t=271s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'KBFaRW7QmVQ',
                       'title': '(UPDATE 1/21/2025) New One-to-One Consent Rules: TCPA Compliance w/ '
                                'TCPAWorld Troutman & Seasalt.ai',
                       'channel': 'Seasalt AI',
                       'author': 'Seasalt AI',
                       'text': "The Troutman Amin 15 should be your touchstone, remember if you're a lead "
                               'buyer the risk is on you.',
                       'tip': "The Troutman Amin 15 should be your touchstone, remember if you're a lead "
                              'buyer the risk is on you.',
                       'timestamp': 2019,
                       'timestamp_seconds': 2019,
                       'timestamp_label': '[00:33:39]',
                       'url': 'https://www.youtube.com/watch?v=KBFaRW7QmVQ&t=2019s',
                       'markdown': '[00:33:39](https://www.youtube.com/watch?v=KBFaRW7QmVQ&t=2019s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '1zvwOs0qmmg',
                       'title': 'What is a Lead? TCPA Consent Guide to Opt in Leads - FCC Telemarketing '
                                'Laws & Do Not Call List Rule',
                       'channel': 'DatatoLeads - B2B and B2C Wholesale Data and Leads',
                       'author': 'DatatoLeads - B2B and B2C Wholesale Data and Leads',
                       'text': "Risk management, that's really what it comes down to.",
                       'tip': "Risk management, that's really what it comes down to.",
                       'timestamp': 121,
                       'timestamp_seconds': 121,
                       'timestamp_label': '[00:02:01]',
                       'url': 'https://www.youtube.com/watch?v=1zvwOs0qmmg&t=121s',
                       'markdown': '[00:02:01](https://www.youtube.com/watch?v=1zvwOs0qmmg&t=121s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'}]}
