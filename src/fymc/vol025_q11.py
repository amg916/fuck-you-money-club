from __future__ import annotations

CHAPTER_11 = {'id': 'Q11',
 'chapter_id': 'Q11',
 'chapter_number': 11,
 'question_number': 11,
 'slug': 'double-brokering-and-freight-fraud-defense',
 'question_prompt': 'How do I spot and prevent double brokering and carrier identity fraud before a load '
                    'goes missing?',
 'kicker': 'Q11 / THE BIG MONEY PLAYBOOKS',
 'title': 'Double Brokering and Freight Fraud Defense',
 'subtitle': 'How double brokering evolved, warning signs, carrier vetting with Highway, RMIS and '
             'Truckstop MFA, Carrier411 policy changes, attorney-led prevention, and new federal rules '
             'targeting fraudulent brokers',
 'layout_template': 'chapter_opener',
 'reading_time_minutes': 15,
 'executive_summary': "Practitioners from Double Broker Bounty Hunter, Freight 360, Highway, Overdrive's "
                      'Hank Seaton and ThinkFreight converge on one thesis: double brokering is now an '
                      'identity-theft game, run through phished load board logins, look-alike email '
                      'domains, dark-web DOT PINs and bought MC numbers, usually by one operator posing as '
                      'both carrier and broker. Defense mechanics are concrete: Highway-style association '
                      'insights that expose shared addresses, phones and equipment; a 20% off-market rate '
                      'trigger; corporate-office callbacks on load number and lane; withheld PO numbers '
                      'released only after geofenced photo checks; and carrier names on the bill of '
                      'lading. Numbers frame the stakes: $2 to $3 billion in 2024 losses, a $75,000 bond '
                      'that paid Convoy carriers under 10 cents on the dollar, and a 7-day bond '
                      'replenishment rule enforced from January 16, 2026. Speakers split on rebrokering '
                      'chain depth and Carrier411 reporting.',
 'key_metrics': [{'label': 'Annual Double Brokering Cost (2024 Estimate)',
                  'metric': 'Annual Double Brokering Cost (2024 Estimate)',
                  'value': '$2 to $3 billion per year',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'John Cana cites 2024 estimates of economic damage from double brokering '
                             'alone, up from a half billion dollars in 2023 per FreightWaves and Triumph '
                             'Pay, excluding stolen or ransomed cargo.',
                  'source': 'Double Broker Bounty Hunter ([J96nZa6x_Ek @ 00:10:19])'},
                 {'label': 'Off-Market Rate Trigger',
                  'metric': 'Off-Market Rate Trigger',
                  'value': '20% above or below market triggers digging; 30% above is most likely a scam',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Cana's personal rate rule for deciding when to investigate the broker behind "
                             'a posted load, regardless of which brokerage name appears on it.',
                  'source': 'Double Broker Bounty Hunter ([3dI5z6SHDPc @ 00:14:19])'},
                 {'label': 'Shipments Picked Up Without Carrier Name',
                  'metric': 'Shipments Picked Up Without Carrier Name',
                  'value': 'Two-thirds to three-quarters of truckload shipments',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Hank Seaton's estimate of truckload shipments picked up and delivered "
                             'without the name of the pickup or delivery carrier on the paperwork, the gap '
                             'his bill of lading protocol targets.',
                  'source': 'Overdrive ([jnoJihiGSEA @ 00:25:28])'},
                 {'label': 'Broker Bond Replenishment Window',
                  'metric': 'Broker Bond Replenishment Window',
                  'value': '7 calendar days to restore $75,000 or face immediate suspension',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'ThinkFreight reports that from January 16, 2026, FMCSA can immediately '
                             'suspend a broker or freight forwarder whose bond or trust drops below '
                             '$75,000 and is not replenished within seven calendar days.',
                  'source': 'ThinkFreight ([s-qzw5ZxjmU @ 00:01:41])'}],
 'sections': [{'heading': 'Section 1: The Practitioner Consensus',
               'paragraphs': ['John Cana, who runs the Double Broker Bounty Hunter channel, calls double '
                              'brokering the root of every other freight crime, from cargo theft to '
                              'ransomed cargo to nonpayment [3WxrmhqpsyY @ 00:02:15]. The playbook starts '
                              'with a carrier identity. Scammers either file their own authority using a '
                              'scrapyard VIN and a pencil-whipped DOT inspection from a bribed mechanic, '
                              "phish a real carrier's setup packet by posting a fake load and sitting on "
                              'those documents for as long as the insurance stays valid, or buy aged MC '
                              'numbers that exiting carriers advertise on Facebook and X [J96nZa6x_Ek @ '
                              '00:12:13]. The broker side mirrors it: forged rate confirmations doctored '
                              'in Adobe, look-alike domains such as ship-abc swapped in for abclogistics, '
                              'and fake DAT authentication emails that harvest load board credentials. '
                              'Cana insists the chain is short, not a game of telephone: the same person '
                              'who books from the real broker while posing as a carrier is usually the one '
                              'posing as a broker to the real carrier, keeping a smoke screen in the '
                              'middle [3WxrmhqpsyY @ 00:19:58]. Keep Loadings describes the street result '
                              'in plain terms, with scammers buying old clean MC numbers and cloning '
                              'legitimate carrier names to book high-value cargo and steal the entire '
                              'trailer [FbcZES6peVA @ 00:01:42].',
                              'The vetting consensus centers on identity data that does not line up. Nate '
                              'Cross of Freight 360 lists five red flags: no inspection history or '
                              'unverifiable equipment, rates that sound too good to be true, email or '
                              'phone details that do not match the FMCSA registration, PO box or '
                              'residential addresses on a carrier offering to move multiple loads, and '
                              'community reports from Highway, the TIA Watchdog list, or the Excel lists '
                              "brokers pass between each other [gnxgKnnz6Jw @ 00:02:35]. Highway's demos "
                              'show the same pattern in data form. One carrier with active authority and a '
                              'recent inspection still carried eight insights: a residential address '
                              'within a quarter mile of a carrier holding broker authority, a claim of 10 '
                              'or more trucks, an inspection-to-truck ratio in the bottom 10 of its peer '
                              'group, and shared phones, emails, contacts, an address and even a vehicle '
                              'with a second carrier, which Highway calls two carriers sharing identities '
                              '[b-vDBH9GpuA @ 00:01:33]. A second Highway walkthrough flagged a carrier '
                              'self-reporting 16 trucks with zero inspections in 24 months and contact '
                              'details reused across three active MC numbers [sKKld4Wdyqg @ 00:01:17]. '
                              'Hank Seaton tells Overdrive listeners to start any fraud screen by looking '
                              'for common addresses and common names [jnoJihiGSEA @ 00:42:57].',
                              'Everyone agrees the losses are large and the federal backstop is thin. Cana '
                              'cites FreightWaves and Triumph Pay putting 2023 double brokering damage at '
                              'a half billion dollars, with 2024 estimates of $2 to $3 billion before '
                              'stolen or ransomed cargo is counted [J96nZa6x_Ek @ 00:10:19]. Bridge '
                              "Logistics relays Carrier411 CEO Darren Brewer's figure of more than $100 "
                              'million a year and warns that defrauded carriers chase shippers for payment '
                              'while honest brokers end up paying the same load twice [uT4ymtB7YcA @ '
                              '00:01:49]. The $75,000 broker bond is treated as a floor, not protection: '
                              'Cana notes some mega brokerages run bonds above $10 million, but when '
                              'Convoy shut down with about $34 million in loads chasing a $75,000 bond, '
                              'carriers collected less than 10 cents on the dollar [3WxrmhqpsyY @ '
                              '00:08:37]. ThinkFreight reports that since January 16, 2026, FMCSA can '
                              'suspend a broker whose bond or trust falls below $75,000 and is not '
                              'replenished within seven calendar days. Shortfalls can come from unpaid '
                              'claims, a broker consenting to a drawdown, ignoring valid claim notices, or '
                              'a claim turned into a federal court judgment, though the host, coming from '
                              'a broker background, still wants bonds sized to freight volume [s-qzw5ZxjmU '
                              '@ 00:01:41].'],
               'table': {'caption': 'Where the practitioners agree on how double brokering works and what '
                                    'to screen first',
                         'headers': ['Consensus Point',
                                     'What Practitioners Report',
                                     'Operator Takeaway',
                                     'Expert Source'],
                         'rows': [['Identity theft is now the main attack vector',
                                   'Scammers phish carrier setup packets, hijack DOT PINs, and buy aged MC '
                                   'numbers',
                                   'Treat every new carrier identity as unverified until data matches '
                                   'FMCSA records',
                                   'Double Broker Bounty Hunter ([J96nZa6x_Ek @ 00:12:13])'],
                                  ['DOT PINs issued before March 2023 are compromised',
                                   'The March 2023 DOT breach put active PINs up for sale on the dark web',
                                   'Carriers holding pre-March 2023 PINs should get a new PIN from FMCSA '
                                   'immediately',
                                   'Double Broker Bounty Hunter ([3dI5z6SHDPc @ 00:16:13])'],
                                  ['Shared identity data exposes linked shell carriers',
                                   'Shared phones, emails, addresses, and vehicles tie separate MC and DOT '
                                   'numbers together',
                                   'Run association checks before tendering, not after a load goes missing',
                                   'Highway ([b-vDBH9GpuA @ 00:03:01])'],
                                  ['Zero inspections against a large reported fleet is a warning',
                                   'A carrier claiming 16 trucks with no inspections in 24 months '
                                   'triggered review',
                                   'Compare inspection count against the fleet size the carrier '
                                   'self-reports on file',
                                   'Highway ([sKKld4Wdyqg @ 00:01:17])'],
                                  ['Contact details must match the FMCSA registration data',
                                   'Mismatched email domains or phone numbers point to a stolen identity '
                                   'or a dispatcher',
                                   'Call the number on the FMCSA record, not the number in the email',
                                   'Freight 360 ([gnxgKnnz6Jw @ 00:02:35])'],
                                  ['Look-alike email domains drive broker impersonation',
                                   'Fraudsters add or drop a single letter to clone a household-name '
                                   'broker domain',
                                   'Read every letter of the sender domain before signing any rate '
                                   'confirmation',
                                   'Overdrive ([jnoJihiGSEA @ 00:21:30])'],
                                  ['The $75,000 bond rarely makes unpaid carriers whole',
                                   'Convoy carriers recovered under 10 cents on the dollar against roughly '
                                   '$34 million in loads',
                                   'Do not treat a bond claim as the recovery plan for nonpayment',
                                   'Double Broker Bounty Hunter ([3WxrmhqpsyY @ 00:09:00])']]}},
              {'heading': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ["Cana's rate-confirmation forensics are the sharpest street mechanics on "
                              'offer. The pricing test is a 20% rule: any load posted 20% above or below '
                              'market gets heavy digging, 30% above market is most likely a scam no matter '
                              'which broker is named, and a Minneapolis to Elk River post paying $2,500 '
                              'for 32 miles was an instant scam call [3dI5z6SHDPc @ 00:14:19]. On paper, '
                              'Cana checks whether the pro number font differs from the rest of the '
                              'header, whether the email domain matches the real brokerage, and whether '
                              'shipper and receiver codes are four-character alphanumerics, which signal '
                              'an Amazon load that is a scam if it is not moving through the Relay app '
                              '[3dI5z6SHDPc @ 00:24:56]. A Gmail address triggers questions every time; '
                              'Cana has verified only two legitimate brokers using Gmail out of roughly '
                              '60,000. Behavioral tells include one-line rate cons with no fine print, a '
                              'broker demanding the bill of lading at pickup, check-in instructions under '
                              "another carrier's name, and status demands at arrival, check-in, loading, "
                              "and paperwork. Freight 360's Nate Cross adds that a too-good rate usually "
                              'means the carrier plans to rebroker, take quick pay, and vanish, leaving '
                              'the broker to pay the second carrier again [gnxgKnnz6Jw @ 00:02:20].',
                              'For brokers, the working stack layers vetting software over physical proof. '
                              'Nate Cross runs Highway at the Freight 360 brokerage for inspection '
                              'history, registered equipment, community reports, and an ELD-fed map of '
                              'equipment locations, then makes GPS tracking mandatory for the full load '
                              'when fraud is suspected; most fraudsters quit once challenged for tracking '
                              'or an ELD download before payment [uGu6NcZkt28 @ 00:01:57]. Cross also '
                              "demands photos or video at the shipper showing equipment, the driver's "
                              "face, registration, driver's license, and the MC on the truck door, zooming "
                              'in for doctored images, and withholds the PO or pickup number until '
                              'identity and location are confirmed. QuickScope automates that gate: the '
                              'driver gets a text, takes a one-time photo inside a 2m geofence, and '
                              'character recognition checks the company name, MC, and DOT before pickup '
                              'details release automatically [uGu6NcZkt28 @ 00:03:45]. Hank Seaton '
                              'estimates two-thirds to three-quarters of truckload shipments move without '
                              "the carrier's name on the paperwork [jnoJihiGSEA @ 00:25:28]. His protocol: "
                              "put the authorized carrier's name on the bill of lading, send that name to "
                              'the consignor at booking, show the contracting broker as the '
                              'send-freight-bill-to party, and require the driver to present credentials, '
                              "including a driver's license, satisfactory to the consignor [jnoJihiGSEA @ "
                              '00:26:07].',
                              'Carriers get their own checklist. Cana tells them to call the corporate '
                              'office of any medium or large brokerage, found through the DAT directory, '
                              'to confirm the load number, the lane, and that they are listed as carrier '
                              'of record; with small shops, ask the shipper which broker it uses, but '
                              'never talk money, because that edges into back solicitation [3dI5z6SHDPc @ '
                              '00:29:21]. Cana also recommends drivers sign over a colored rubber stamp '
                              'carrying the MC number, carrier name, and driver name, so a scammer cannot '
                              'hide the real carrier or forge a clean receiver signature [3dI5z6SHDPc @ '
                              '00:11:25]. On onboarding, Cana walks dispatchers through the Truckstop MFA '
                              'layered onto RMIS setups since January 2024: the owner completes a one-time '
                              "ID check with a driver's license scan and selfie, then each setup needs an "
                              'SMS, biometric, or authenticator code plus the usual emailed verification '
                              'code, adding about 30 seconds once configured; delete cookies between '
                              'setups or the flow hangs [aSSPaOdn5ZI @ 00:12:31]. Seaton adds a pressure '
                              'valve: a carrier who suspects fraud mid-haul can insist on payment for '
                              'delivery of the shipment, which Seaton frames as a possessory lien rooted '
                              'in old commerce law [jnoJihiGSEA @ 00:38:00].'],
               'table': {'caption': 'Street-level tools, thresholds, and workflows practitioners run '
                                    'against double brokers',
                         'headers': ['Tactic or Tool',
                                     'Exact Mechanic or Number',
                                     'How Operators Use It',
                                     'Expert Source'],
                         'rows': [['20% market-rate rule for posted loads',
                                   'Loads 20% above or below market get extra digging; 30% above is likely '
                                   'a scam',
                                   'Benchmark every posted rate before calling the broker back',
                                   'Double Broker Bounty Hunter ([3dI5z6SHDPc @ 00:14:19])'],
                                  ['QuickScope geofenced photo verification',
                                   'Driver takes a one-time photo within a 2m geofence; character '
                                   'recognition reads name, MC, DOT',
                                   'Release pickup details automatically only after the photo passes '
                                   'verification',
                                   'Freight 360 ([uGu6NcZkt28 @ 00:04:02])'],
                                  ['Truckstop MFA layered on RMIS setups',
                                   "Owner completes driver's license scan plus selfie; each setup then "
                                   'needs two codes',
                                   'Use SMS for speed and clear browser cookies between every carrier '
                                   'setup',
                                   'Double Broker Bounty Hunter ([aSSPaOdn5ZI @ 00:07:40])'],
                                  ['Highway multi-point identity checks',
                                   'Authority, insurance, ELD activity, and physical location '
                                   'cross-checked in real time',
                                   "Flags a login using a carrier's MC number from a different state "
                                   'instantly',
                                   'Keep Loadings ([FbcZES6peVA @ 00:02:38])'],
                                  ['Bill of lading carrier-name protocol',
                                   'Authorized carrier named on the bill and transmitted to the consignor '
                                   'at booking',
                                   'Attach it as a contract appendix so would-be double brokers '
                                   'self-select out',
                                   'Overdrive ([jnoJihiGSEA @ 00:36:35])'],
                                  ['Home-office document verification',
                                   'Match load board contact against the FMCSA address and area code on '
                                   'file',
                                   'Send anything the carrier must sign to the home office listed with '
                                   'FMCSA',
                                   'Overdrive ([jnoJihiGSEA @ 00:31:11])'],
                                  ['Centralized visibility followed by tracking',
                                   'Three steps: centralize data, identify high-risk lanes, then deploy '
                                   'tracking technology',
                                   'Tracking data proves to insurers you never possessed a double-brokered '
                                   'load',
                                   'Commercial Carrier Journal ([u2IgQ87ZELQ @ 00:10:22])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'What the fraud hunters do that most desks skip',
                           'body': 'Tactics practitioners run daily to cut off double brokers before the '
                                   'load moves or the money leaves.',
                           'items': ['Replace any DOT PIN issued before March 2023; Cana says the minute '
                                     'you discover a hijack, it has been live at least 24 hours with at '
                                     'least 100 loads double brokered in your name [Double Broker Bounty '
                                     'Hunter — 3dI5z6SHDPc @ 00:17:23]',
                                     'Never authenticate load board credentials from an email link; DAT '
                                     'does not verify accounts by email, and a phished login starts a very '
                                     'long nightmare for the broker [Double Broker Bounty Hunter — '
                                     'J96nZa6x_Ek @ 00:17:44]',
                                     'Stack your pickup proof requests and zoom in on every photo for '
                                     'doctoring; the more you ask for, the harder it is to scam you '
                                     '[Freight 360 — uGu6NcZkt28 @ 00:02:58]',
                                     'Treat a party pushing you to send paperwork immediately as a red '
                                     'flag; scammers track the load closely to beat the money to factoring '
                                     'before you invoice [Truck Driver Nation — 5dP6IV7sJW0 @ 00:05:30]']},
               'sop_steps': [{'step': 1,
                              'title': 'Screen the carrier identity',
                              'action': 'Pull location, operation, and association insights before '
                                        'tendering any load.',
                              'detail': 'Look for shared phones, emails, addresses, and vehicles across '
                                        'different MC and DOT numbers, which Highway reads as carriers '
                                        'sharing identities and flags for review [Highway — b-vDBH9GpuA @ '
                                        '00:02:25]'},
                             {'step': 2,
                              'title': 'Forensically check the rate confirmation',
                              'action': 'Compare the rate to market and inspect fonts, domains, and '
                                        'shipper codes.',
                              'detail': 'A pro number font that differs from the header and a domain that '
                                        'does not match the real brokerage marked one rate con as a '
                                        'guaranteed scam [Double Broker Bounty Hunter — 3dI5z6SHDPc @ '
                                        '00:24:37]'},
                             {'step': 3,
                              'title': 'Lock the carrier name into the paperwork',
                              'action': 'Write the authorized carrier onto the bill of lading and notify '
                                        'the consignor at booking.',
                              'detail': "Seaton's protocol has brokers and shippers contract that the bill "
                                        'of lading reflects the authorized carrier and that the consignor '
                                        'knows who to expect [Overdrive — jnoJihiGSEA @ 00:25:46]'},
                             {'step': 4,
                              'title': 'Gate the pickup information',
                              'action': 'Withhold the PO or pickup number until identity and location are '
                                        'verified on site.',
                              'detail': 'Release pickup details only to the verified carrier, and have the '
                                        "customer confirm the truck's identity at pickup once the "
                                        'information is released [Freight 360 — uGu6NcZkt28 @ 00:03:12]'}]},
              {'heading': 'Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The $75,000 broker bond is the loudest fault line. ThinkFreight, speaking '
                              'from a broker background, calls the new FMCSA rule a slight step forward: a '
                              'broker whose bond or trust drops below $75,000 and is not replenished '
                              'within seven calendar days can be suspended, but the speaker argues the '
                              'bond should scale with brokerage size, get reviewed every year, and that '
                              'anyone moving a billion dollars in freight should carry far more than a '
                              'replenishing minimum [s-qzw5ZxjmU @ 00:04:52]. John Cana of Double Broker '
                              'Bounty Hunter pushes the same direction with harder numbers: some mega '
                              'brokerages already run bonds upwards of $10 million while others still sit '
                              'at $75,000, and when big brokers like Convoy shut down, carriers chasing '
                              'roughly $34 million in loads against a $75,000 bond collected less than 10 '
                              'cents on the dollar [3WxrmhqpsyY @ 00:08:37]. Attorney Hank Seaton, on '
                              'Overdrive, describes a case where an operator ran up $1.9 million in '
                              'carrier receivables, filed bankruptcy, and left 273 carriers with maybe '
                              'four percent [jnoJihiGSEA @ 00:20:28]. The split is about remedy, not '
                              'diagnosis. ThinkFreight banks the seven-day replenishment trigger as '
                              'progress, while Cana wants the bond itself sized to the freight a broker '
                              'has on the road at any given time [3WxrmhqpsyY @ 00:09:20].',
                              'Practitioners also split on whether the federal government will fix this. '
                              'The Commercial Carrier Journal guest argues the Household Goods Shipping '
                              'Consumer Protection Act would give the government teeth and funding to fine '
                              'and even shut down fraudulent businesses, but insists it is just another '
                              'tool in the tool belt that should not stop carriers from deploying '
                              'technology and getting close with partners [u2IgQ87ZELQ @ 00:01:19]. Seaton '
                              'goes the other way: the statute already lets the government charge a '
                              'fraudster up to ten thousand dollars per violation, yet FMCSA has no '
                              'appetite for it, complaints can wait as much as a year for a response, and '
                              'the real fix is self-help, an agreement among brokers and carriers large '
                              'and small to quit the sloppy procedures [jnoJihiGSEA @ 00:17:45]. Cana '
                              'lands in the middle. FMCSA believes court challenges blocked its civil '
                              'penalty power, Cana disagrees with that interpretation, and private outfits '
                              'like the bounty hunter program and the freight fraud task force are '
                              'stepping in to help the agencies do their job [3WxrmhqpsyY @ 00:15:57]. '
                              'ThinkFreight still calls enforcement of the financial responsibility rule a '
                              'step forward, noting the rule took effect in January 2024 but enforcement '
                              'was delayed until January 2026, with the broker transparency rulemaking '
                              'expected next [s-qzw5ZxjmU @ 00:04:06].',
                              "Watchlists split the same camp. Freight 360's Nate Cross tells brokers that "
                              'community reports on Highway or the TIA Watchdog list, plus Excel lists of '
                              'internal double brokering reports passed from broker to broker, are a '
                              'strong indicator to avoid a carrier [gnxgKnnz6Jw @ 00:04:01]. Cana is more '
                              'skeptical, estimating at least 10 percent of Carrier411 reports are false '
                              'or exaggerated, while co-host Jimmy argues a bad experience earns an '
                              'internal do-not-use flag, not a Freight Guard that tells the world to drop '
                              "Joe's Trucking [3dI5z6SHDPc @ 00:17:59]. Cana later blasted Carrier411 for "
                              'making deleted Freight Guard reports permanent, growing from 12 to 26 '
                              'report categories, and allowing reports against carriers who file on a '
                              "broker's bond or threaten legal action, calling it a weapon brokers use to "
                              'intimidate and extort carriers [o7UDt2VXwwU @ 00:01:28]. Quick pay draws '
                              'the same kind of split. Cana tells brokers that a carrier demanding quick '
                              'pay from a well-established broker, one every factor already covers, is a '
                              'warning sign, but Jimmy counters that most brokers run quick pay cheaper '
                              'than the five to three percent a factor charges, and that it helps new '
                              'carriers factors will not take on, calling it a gamble but the price of '
                              'doing business [3dI5z6SHDPc @ 00:20:11].'],
               'table': {'caption': 'Contested playbooks on bonds, bills of lading, dock access, '
                                    'onboarding speed, rates, and mid-haul response',
                         'headers': ['Contested Question',
                                     'One Playbook',
                                     'Competing Playbook',
                                     'Expert Source'],
                         'rows': [['How big the broker bond should really be',
                                   'Treat seven-day replenishment of the $75,000 bond as a slight step '
                                   'forward',
                                   'Scale the bond to freight volume, like megas running bonds upwards of '
                                   '$10 million',
                                   'ThinkFreight ([s-qzw5ZxjmU @ 00:05:06]); Double Broker Bounty Hunter '
                                   '([3WxrmhqpsyY @ 00:07:57])'],
                                  ['Whose name belongs on the bill of lading',
                                   'Broker listing itself as carrier is usually okay; checking in as XYZ '
                                   'Trucking is the red flag',
                                   "Contract that the authorized carrier's name appears on the bill and is "
                                   'sent to the consignor',
                                   'Double Broker Bounty Hunter ([3dI5z6SHDPc @ 00:07:42]); Overdrive '
                                   '([jnoJihiGSEA @ 00:26:07])'],
                                  ['How many hands touch a double-brokered load',
                                   'Loads get rebrokered two, three, four or more times in Chicago, Los '
                                   'Angeles, and Atlanta',
                                   'Triple or quadruple claims are BS; usually one person plays both fake '
                                   'carrier and fake broker',
                                   'Bridge Logistics ([uT4ymtB7YcA @ 00:00:51]); Double Broker Bounty '
                                   'Hunter ([3WxrmhqpsyY @ 00:19:24])'],
                                  ['How to gate access at the pickup dock',
                                   'Withhold PO and pickup numbers until identity and location verify, '
                                   'released through QuickScope photo checks',
                                   'Send the authorized carrier name to the consignor and require driver '
                                   'credentials satisfactory to the consignor',
                                   'Freight 360 ([uGu6NcZkt28 @ 00:03:12]); Overdrive ([jnoJihiGSEA @ '
                                   '00:31:33])'],
                                  ['Whether automated carrier onboarding helps or hurts',
                                   'Automate with RMIS to reduce fraud, streamline operations, and '
                                   'minimize human error',
                                   'Thirty-minute decisions and a quickly signed RMIS contract breed the '
                                   'sloppy spot market failures',
                                   'Truckstop . com ([9d907d-1DzE @ 00:01:17]); Overdrive ([jnoJihiGSEA @ '
                                   '00:13:48])'],
                                  ['What rate spread signals a likely scam',
                                   'Any rate that sounds too good to be true suggests the carrier plans to '
                                   'double broker it',
                                   'Thirty percent above market is most likely a scam; dig harder at 20 '
                                   'percent above or below',
                                   'Freight 360 ([gnxgKnnz6Jw @ 00:02:20]); Double Broker Bounty Hunter '
                                   '([3dI5z6SHDPc @ 00:14:19])'],
                                  ['What a carrier does mid-haul once fraud surfaces',
                                   'Insist on payment before delivery and hold the freight up under a '
                                   'possessory lien',
                                   'Prove with tracking data on every asset that someone else actually '
                                   'possesses the freight',
                                   'Overdrive ([jnoJihiGSEA @ 00:38:00]); Commercial Carrier Journal '
                                   '([u2IgQ87ZELQ @ 00:10:22])']]}},
              {'heading': 'Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The most expensive failures Seaton walked through started with nobody '
                              'checking who actually backed into the dock. In one case, two reputable '
                              'broker-carriers tendered loads to a fraudster posing as a broker, the bills '
                              "of lading at pickup never showed the actual carrier's name, and roughly "
                              'three weeks later the parties realized the loads were copper wire in a scam '
                              'of over $2.6 million; all seven loads had been reconsigned to an empty '
                              'warehouse, and six months on nobody, including the FBI, FMCSA, and state '
                              'police, could find the freight [jnoJihiGSEA @ 00:22:34]. In another, over '
                              'two dozen victims were scammed by an outfit FMCSA showed running only '
                              '60,000 miles, freight was claimed broken down at a Montana truck stop, '
                              'seals came back broken and resealed, and the home office was a McMansion in '
                              'Ohio [jnoJihiGSEA @ 00:32:16]. Bridge Logistics describes the same endgame: '
                              'the real carrier is sent to an unknown location and the product is '
                              'transloaded onto another victimized carrier with a new bill of lading '
                              "[uT4ymtB7YcA @ 00:02:31]. Cana's tell is silence. When dispatch goes dark "
                              'after booking or tracking fails, the cargo is gone, and getting law '
                              'enforcement to take cargo theft seriously remains the problem [3dI5z6SHDPc '
                              '@ 00:18:48].',
                              'The economics of a single double-brokered load hit everyone twice. Nate '
                              'Cross warns that when the fraudster collects and never pays the hauling '
                              'carrier, the broker typically ends up paying for the same load twice, once '
                              'to the fraudster and again to the carrier that actually moved it '
                              '[gnxgKnnz6Jw @ 00:01:27]. Bridge Logistics adds that defrauded carriers go '
                              'after shippers for payment when they cannot track down the fake broker, '
                              'that legitimate brokers are commonly on the hook for multiple payments, and '
                              'that the rates promised to double-brokered carriers run much higher than '
                              'what the legitimate broker negotiated [uT4ymtB7YcA @ 00:01:09]. Seaton '
                              'describes collection agencies that find a hoodwinked small carrier, take an '
                              'assignment for 50 percent of whatever they collect, and hammer upstream, so '
                              'the honest broker catches heat from the customer over a $3,000 demand on a '
                              'load the broker never knew was double brokered [jnoJihiGSEA @ 00:15:35]. '
                              "George of Truck Driver Nation frames the carrier's side: that money is fuel "
                              'money, the only path back in most scenarios is to back source the load all '
                              'the way to the original direct shipper and bill them, and speed matters '
                              'because the fraudster is racing to collect first [5dP6IV7sJW0 @ 00:02:47].',
                              'Identity hijacks are the trap that compounds fastest. Cana warns that DOT '
                              'PIN numbers compromised in the March 2023 data breach are for sale on the '
                              'dark web, and that the minute a carrier discovers its information was '
                              'pirated, the problem has existed for at least 24 hours with at least 100 '
                              'loads double brokered in its name [3dI5z6SHDPc @ 00:17:23]. Scammers also '
                              'post a fake load, award it to a real carrier, harvest the setup documents, '
                              'and sit on them for as long as the insurance stays good, up to three '
                              'months, before booking freight under that identity, while brokers get '
                              'phished by fake DAT emails asking them to authenticate their accounts '
                              '[J96nZa6x_Ek @ 00:12:35]. Forged rate confirmations look clean at first '
                              'glance: Cana caught a mismatched font on the pro number, lookalike domains '
                              'such as brockb.net and logisticsdynamicsinc.com, and four-character '
                              'alphanumeric shipper and receiver codes marking Amazon loads that only the '
                              'relay app user gets paid on [3dI5z6SHDPc @ 00:27:54]. The Commercial '
                              'Carrier Journal guest expects the curve to get worse, since very advanced '
                              'AI lets fraudsters scrape large amounts of data, fabricate details like '
                              'physical location, and hide their actions much more effectively '
                              '[u2IgQ87ZELQ @ 00:04:31].'],
               'table': {'caption': 'Firsthand losses, traps, and the economics practitioners reported '
                                    'behind each',
                         'headers': ['Failure Mode',
                                     'What Practitioners Saw Firsthand',
                                     'Damage Or Economics Check',
                                     'Expert Source'],
                         'rows': [['Undersized bond when a large broker collapses',
                                   'Carriers on loads for brokers that shut down could only collect from a '
                                   '$75,000 bond',
                                   'Roughly $34 million in loads paid out at less than 10 cents on the '
                                   'dollar',
                                   'Double Broker Bounty Hunter ([3WxrmhqpsyY @ 00:08:37])'],
                                  ['Factored receivable turns out to be fake',
                                   'The factor buys the receivable with recourse, then deducts it once the '
                                   'fraud surfaces',
                                   'One transcontinental load deduction can put a small carrier upside '
                                   'down',
                                   'Overdrive ([jnoJihiGSEA @ 00:34:18])'],
                                  ['Broker clicks a fake DAT authentication email',
                                   'Phishing emails ask brokers to authenticate load board accounts by '
                                   'clicking a link',
                                   'Cana calls a phished login the start of a very long nightmare',
                                   'Double Broker Bounty Hunter ([J96nZa6x_Ek @ 00:17:44])'],
                                  ['Ghost fleet passes the surface safety check',
                                   'Active authority and insurance, but 16 self-reported trucks with zero '
                                   'inspections in 24 months',
                                   'Residential address holds both carrier and broker MC, with contacts '
                                   'reused across three active MCs',
                                   'Highway ([sKKld4Wdyqg @ 00:01:17])'],
                                  ['Shared identity hiding behind two separate MC numbers',
                                   'Carrier claims 10 or more trucks from a residential address near a '
                                   'broker authority',
                                   'Inspection-to-truck count sits in the bottom 10 of similar fleets, '
                                   'with equipment shared',
                                   'Highway ([b-vDBH9GpuA @ 00:01:49])'],
                                  ['Truckstop MFA hangs during an RMIS carrier setup',
                                   'The blue check mark appears but the session will not advance back into '
                                   'RMIS',
                                   'Fix is clearing cookies; ID verification failed once in three runs, '
                                   'then passed',
                                   'Double Broker Bounty Hunter ([aSSPaOdn5ZI @ 00:12:31])'],
                                  ['Paying a service to scrub a Carrier411 Freight Guard',
                                   'A cottage industry charged carriers to get Freight Guard reports '
                                   'deleted from the platform',
                                   'Between $2,000 and $55,000 per report, and deleted reports now persist '
                                   'as reclassified',
                                   'Double Broker Bounty Hunter ([o7UDt2VXwwU @ 00:01:03])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Stop Before The Load Moves',
                           'body': 'Each check below comes straight from a loss or near-loss the '
                                   'practitioners reported; clear all four before releasing pickup details '
                                   'or cutting a carrier payment.',
                           'items': ["Confirm the carrier's DOT PIN has been reset since the March 2023 "
                                     'breach, because a compromised PIN lets a scammer file a fake MCS-150 '
                                     'and change all the SAFER contact information in a couple of minutes '
                                     '[Double Broker Bounty Hunter — J96nZa6x_Ek @ 00:13:35].',
                                     'Never authenticate a load board account from an emailed link; DAT '
                                     'does not do that by email, and a phished login is the start of a '
                                     'very long nightmare [Double Broker Bounty Hunter — J96nZa6x_Ek @ '
                                     '00:17:44].',
                                     "Require the authorized carrier's name on the bill of lading, because "
                                     'in the copper wire scam the bills at pickup never showed who was '
                                     'actually hauling [Overdrive — jnoJihiGSEA @ 00:25:46].',
                                     'Treat a carrier that goes dark after booking, or a tracking feed '
                                     'that fails, as a stolen load and escalate at once, because once they '
                                     'go dark the cargo is gone [Double Broker Bounty Hunter — 3dI5z6SHDPc '
                                     '@ 00:18:48].']}}],
 'pull_quote': '"The minute you find out you\'ve had a problem, that problem\'s been there for at least 24 '
               'hours and you have at least a 100 loads double brokered in your name." — attributed to '
               'Double Broker Bounty Hunter (3dI5z6SHDPc @ 00:17:23).',
 'diagram_id': 'diag-06',
 'action_checklist': ['Open the Highway location, operation, and association insights on every new carrier '
                      'and flag residential addresses near a broker authority, low inspection-to-truck '
                      'counts, and shared phones, emails, or vehicles [Highway — b-vDBH9GpuA @ 00:01:33].',
                      'Make GPS tracking mandatory for the full load when fraud is suspected, start it '
                      'before the truck heads to pickup, and demand an ELD download proving location '
                      'before paying [Freight 360 — uGu6NcZkt28 @ 00:02:15].',
                      'Withhold the PO or pickup number until identity and location are verified, using '
                      'QuickScope to text the driver for a one-time geofenced photo checked by character '
                      'recognition for company name, MC, and DOT [Freight 360 — uGu6NcZkt28 @ 00:03:45].',
                      'Carriers: after receiving a rate confirmation from a medium or large broker, call '
                      'the corporate number from the DAT directory to verify the load number, the lane, '
                      'and that you are carrier of record [Double Broker Bounty Hunter — 3dI5z6SHDPc @ '
                      '00:29:05].',
                      'Write into broker and shipper contracts that the bill of lading shows the '
                      'authorized carrier and the broker as send freight bill to, and transmit that '
                      "carrier's name to the consignor at booking [Overdrive — jnoJihiGSEA @ 00:26:07].",
                      'Issue drivers a color rubber stamp carrying the carrier MC number, carrier name, '
                      'and driver name for every bill of lading signature so a scammer cannot hide who the '
                      'real carrier is [Double Broker Bounty Hunter — 3dI5z6SHDPc @ 00:11:25].'],
 'statutory_citations': [{'title': 'Overdrive — Fighting double-brokering fraud: Attorney Hank Seaton on '
                                   'prevention, ways to elevate the issue [00:25:46]',
                          'url': 'https://www.youtube.com/watch?v=jnoJihiGSEA&t=1546s',
                          'relevance': 'Primary practitioner testimony on the supply chain protocol '
                                       "requiring the authorized carrier's name on the bill of lading and "
                                       'the copper wire reconsignment loss.'},
                         {'title': "Double Broker Bounty Hunter — DBBH's Fraud Prevention Series 2.0 - "
                                   'Part 3 - Warning Signs Double Brokers [00:14:19]',
                          'url': 'https://www.youtube.com/watch?v=3dI5z6SHDPc&t=859s',
                          'relevance': 'Primary practitioner testimony on the 20 percent rate rule, forged '
                                       'rate confirmation tells, Carrier411 report reliability, and quick '
                                       'pay disagreements.'},
                         {'title': 'Double Broker Bounty Hunter — Transportation Fraud Prevention Series '
                                   '2.0 - Part 1 - Basics of Double Brokering [00:08:37]',
                          'url': 'https://www.youtube.com/watch?v=3WxrmhqpsyY&t=517s',
                          'relevance': 'Primary practitioner testimony on bond recovery at pennies on the '
                                       'dollar, the one-person-in-the-middle scam structure, and stalled '
                                       'federal enforcement.'},
                         {'title': 'ThinkFreight — FINALLY: FMCSA Targets Freight Brokers With New Rule '
                                   '[00:01:41]',
                          'url': 'https://www.youtube.com/watch?v=s-qzw5ZxjmU&t=101s',
                          'relevance': 'Primary practitioner testimony on the seven-day bond replenishment '
                                       'suspension trigger and the argument for scaling bonds to brokerage '
                                       'size.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 's-qzw5ZxjmU',
                       'title': 'FINALLY: FMCSA Targets Freight Brokers With New Rule',
                       'channel': 'ThinkFreight',
                       'author': 'ThinkFreight',
                       'text': 'Under the new rule, the FMCSA can immediately suspend a broker or a '
                               "freight forwarder's operating authority if their bond or trust drops below "
                               'that threshold and is not replenished within seven calendar days.',
                       'tip': 'Under the new rule, the FMCSA can immediately suspend a broker or a freight '
                              "forwarder's operating authority if their bond or trust drops below that "
                              'threshold and is not replenished within seven calendar days.',
                       'timestamp': 101,
                       'timestamp_seconds': 101,
                       'timestamp_label': '[00:01:41]',
                       'url': 'https://www.youtube.com/watch?v=s-qzw5ZxjmU&t=101s',
                       'markdown': '[00:01:41](https://www.youtube.com/watch?v=s-qzw5ZxjmU&t=101s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'b-vDBH9GpuA',
                       'title': 'Detecting Double Brokering with Highway',
                       'channel': 'Highway',
                       'author': 'Highway',
                       'text': "The carrier's physical address is located within a quarter mile of another "
                               'carrier with broker authority, and they claim to have 10 or more trucks '
                               "yet they're located in a residential area.",
                       'tip': "The carrier's physical address is located within a quarter mile of another "
                              'carrier with broker authority, and they claim to have 10 or more trucks yet '
                              "they're located in a residential area.",
                       'timestamp': 93,
                       'timestamp_seconds': 93,
                       'timestamp_label': '[00:01:33]',
                       'url': 'https://www.youtube.com/watch?v=b-vDBH9GpuA&t=93s',
                       'markdown': '[00:01:33](https://www.youtube.com/watch?v=b-vDBH9GpuA&t=93s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'J96nZa6x_Ek',
                       'title': 'Fraud Prevention   Part 1   Double Brokering Evolution',
                       'channel': 'Double Broker Bounty Hunter',
                       'author': 'Double Broker Bounty Hunter',
                       'text': "Another way is by obtaining the broker's load board credentials through "
                               'phishing scams, with brokers getting emails from what appears to be DAT '
                               "asking them to authenticate their account, and DAT doesn't do that, "
                               'certainly not by email.',
                       'tip': "Another way is by obtaining the broker's load board credentials through "
                              'phishing scams, with brokers getting emails from what appears to be DAT '
                              "asking them to authenticate their account, and DAT doesn't do that, "
                              'certainly not by email.',
                       'timestamp': 1041,
                       'timestamp_seconds': 1041,
                       'timestamp_label': '[00:17:21]',
                       'url': 'https://www.youtube.com/watch?v=J96nZa6x_Ek&t=1041s',
                       'markdown': '[00:17:21](https://www.youtube.com/watch?v=J96nZa6x_Ek&t=1041s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'gnxgKnnz6Jw',
                       'title': "How to Identify Double Broker's | Freight 360",
                       'channel': 'Freight 360',
                       'author': 'Freight 360',
                       'text': 'It gets really bad when they get paid by you and never pay the carrier '
                               'they double brokered the load to, which typically results in you paying '
                               'for the same load twice.',
                       'tip': 'It gets really bad when they get paid by you and never pay the carrier they '
                              'double brokered the load to, which typically results in you paying for the '
                              'same load twice.',
                       'timestamp': 87,
                       'timestamp_seconds': 87,
                       'timestamp_label': '[00:01:27]',
                       'url': 'https://www.youtube.com/watch?v=gnxgKnnz6Jw&t=87s',
                       'markdown': '[00:01:27](https://www.youtube.com/watch?v=gnxgKnnz6Jw&t=87s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'aSSPaOdn5ZI',
                       'title': 'DBBH Fraud Prevention   Truckstop MFA and RMIS Setups',
                       'channel': 'Double Broker Bounty Hunter',
                       'author': 'Double Broker Bounty Hunter',
                       'text': "If it gets hung up and won't advance you back into RMIS, close your "
                               'browser, delete your cookies, and then go back into the setup process '
                               'again.',
                       'tip': "If it gets hung up and won't advance you back into RMIS, close your "
                              'browser, delete your cookies, and then go back into the setup process '
                              'again.',
                       'timestamp': 751,
                       'timestamp_seconds': 751,
                       'timestamp_label': '[00:12:31]',
                       'url': 'https://www.youtube.com/watch?v=aSSPaOdn5ZI&t=751s',
                       'markdown': '[00:12:31](https://www.youtube.com/watch?v=aSSPaOdn5ZI&t=751s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '3WxrmhqpsyY',
                       'title': 'Transportation Fraud Prevention Series 2.0 - Part 1 - Basics of Double '
                                'Brokering',
                       'channel': 'Double Broker Bounty Hunter',
                       'author': 'Double Broker Bounty Hunter',
                       'text': 'When you have $34 million worth of loads trying to collect on a $75,000 '
                               "bond, you're talking pennies on the dollar, less than 10 cents on the "
                               'dollar.',
                       'tip': 'When you have $34 million worth of loads trying to collect on a $75,000 '
                              "bond, you're talking pennies on the dollar, less than 10 cents on the "
                              'dollar.',
                       'timestamp': 517,
                       'timestamp_seconds': 517,
                       'timestamp_label': '[00:08:37]',
                       'url': 'https://www.youtube.com/watch?v=3WxrmhqpsyY&t=517s',
                       'markdown': '[00:08:37](https://www.youtube.com/watch?v=3WxrmhqpsyY&t=517s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'sKKld4Wdyqg',
                       'title': 'Detecting double brokering and fraud',
                       'channel': 'Highway',
                       'author': 'Highway',
                       'text': 'This carrier has self-reported 16 trucks with no inspections in the last '
                               "24 months, and that's a red flag.",
                       'tip': 'This carrier has self-reported 16 trucks with no inspections in the last 24 '
                              "months, and that's a red flag.",
                       'timestamp': 77,
                       'timestamp_seconds': 77,
                       'timestamp_label': '[00:01:17]',
                       'url': 'https://www.youtube.com/watch?v=sKKld4Wdyqg&t=77s',
                       'markdown': '[00:01:17](https://www.youtube.com/watch?v=sKKld4Wdyqg&t=77s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'u2IgQ87ZELQ',
                       'title': 'Double brokering & freight fraud: How new laws will protect carriers',
                       'channel': 'Commercial Carrier Journal',
                       'author': 'Commercial Carrier Journal',
                       'text': 'Utilizing very advanced AI capabilities is going to make double brokering '
                               'much harder to detect.',
                       'tip': 'Utilizing very advanced AI capabilities is going to make double brokering '
                              'much harder to detect.',
                       'timestamp': 252,
                       'timestamp_seconds': 252,
                       'timestamp_label': '[00:04:12]',
                       'url': 'https://www.youtube.com/watch?v=u2IgQ87ZELQ&t=252s',
                       'markdown': '[00:04:12](https://www.youtube.com/watch?v=u2IgQ87ZELQ&t=252s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '3dI5z6SHDPc',
                       'title': "DBBH's Fraud Prevention Series 2.0 - Part 3 - Warning Signs Double "
                                'Brokers',
                       'channel': 'Double Broker Bounty Hunter',
                       'author': 'Double Broker Bounty Hunter',
                       'text': 'If you see 30% above market rate on a load, it is most likely a scam, so I '
                               "use a 20% rule and do a lot more digging if it's 20% above or below market "
                               'rate.',
                       'tip': 'If you see 30% above market rate on a load, it is most likely a scam, so I '
                              "use a 20% rule and do a lot more digging if it's 20% above or below market "
                              'rate.',
                       'timestamp': 859,
                       'timestamp_seconds': 859,
                       'timestamp_label': '[00:14:19]',
                       'url': 'https://www.youtube.com/watch?v=3dI5z6SHDPc&t=859s',
                       'markdown': '[00:14:19](https://www.youtube.com/watch?v=3dI5z6SHDPc&t=859s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'uGu6NcZkt28',
                       'title': 'Secure Your Freight: Strategies to Prevent Double Brokering Scams',
                       'channel': 'Freight 360',
                       'author': 'Freight 360',
                       'text': 'A clever tactic to protect your loads is to withhold pickup information '
                               "like a PO number or a pickup number until you've actually verified the "
                               "carrier's identity and their location.",
                       'tip': 'A clever tactic to protect your loads is to withhold pickup information '
                              "like a PO number or a pickup number until you've actually verified the "
                              "carrier's identity and their location.",
                       'timestamp': 192,
                       'timestamp_seconds': 192,
                       'timestamp_label': '[00:03:12]',
                       'url': 'https://www.youtube.com/watch?v=uGu6NcZkt28&t=192s',
                       'markdown': '[00:03:12](https://www.youtube.com/watch?v=uGu6NcZkt28&t=192s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'FbcZES6peVA',
                       'title': 'How Highway is Fighting Double Brokerage & Cargo Theft in Trucking (2026 '
                                'Update)',
                       'channel': 'Keep Loadings',
                       'author': 'Keep Loadings',
                       'text': 'If a scammer tries to log in using your MC number from a different state, '
                               'Highway flags it instantly.',
                       'tip': 'If a scammer tries to log in using your MC number from a different state, '
                              'Highway flags it instantly.',
                       'timestamp': 158,
                       'timestamp_seconds': 158,
                       'timestamp_label': '[00:02:38]',
                       'url': 'https://www.youtube.com/watch?v=FbcZES6peVA&t=158s',
                       'markdown': '[00:02:38](https://www.youtube.com/watch?v=FbcZES6peVA&t=158s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'jnoJihiGSEA',
                       'title': 'Fighting double-brokering fraud: Attorney Hank Seaton on prevention, ways '
                                'to elevate the issue',
                       'channel': 'Overdrive',
                       'author': 'Overdrive',
                       'text': 'When you get somebody on the phone who says they are a household name '
                               'broker and sends you an email, look at every letter of the email because '
                               'they can change the domain by adding or subtracting an s.',
                       'tip': 'When you get somebody on the phone who says they are a household name '
                              'broker and sends you an email, look at every letter of the email because '
                              'they can change the domain by adding or subtracting an s.',
                       'timestamp': 1290,
                       'timestamp_seconds': 1290,
                       'timestamp_label': '[00:21:30]',
                       'url': 'https://www.youtube.com/watch?v=jnoJihiGSEA&t=1290s',
                       'markdown': '[00:21:30](https://www.youtube.com/watch?v=jnoJihiGSEA&t=1290s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'jnoJihiGSEA',
                       'title': 'Fighting double-brokering fraud: Attorney Hank Seaton on prevention, ways '
                                'to elevate the issue',
                       'channel': 'Overdrive',
                       'author': 'Overdrive',
                       'text': 'The first thing in the supply chain protocol is that brokers and shippers '
                               'put in their contract that the bill of lading will reflect the name of the '
                               'authorized carrier.',
                       'tip': 'The first thing in the supply chain protocol is that brokers and shippers '
                              'put in their contract that the bill of lading will reflect the name of the '
                              'authorized carrier.',
                       'timestamp': 1546,
                       'timestamp_seconds': 1546,
                       'timestamp_label': '[00:25:46]',
                       'url': 'https://www.youtube.com/watch?v=jnoJihiGSEA&t=1546s',
                       'markdown': '[00:25:46](https://www.youtube.com/watch?v=jnoJihiGSEA&t=1546s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '9d907d-1DzE',
                       'title': '5 Ways to Avoid Double-Brokering Scams: Fraud Prevention Friday | '
                                'Truckstop',
                       'channel': 'Truckstop . com',
                       'author': 'Truckstop . com',
                       'text': "Trust your instincts, and if something feels off, don't hesitate to "
                               'question, research, and take precautions.',
                       'tip': "Trust your instincts, and if something feels off, don't hesitate to "
                              'question, research, and take precautions.',
                       'timestamp': 97,
                       'timestamp_seconds': 97,
                       'timestamp_label': '[00:01:37]',
                       'url': 'https://www.youtube.com/watch?v=9d907d-1DzE&t=97s',
                       'markdown': '[00:01:37](https://www.youtube.com/watch?v=9d907d-1DzE&t=97s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'uT4ymtB7YcA',
                       'title': 'Identifying Double Brokering! (Fraudulent Activities Awareness for '
                                'Brokers, Carriers & Shippers)',
                       'channel': 'Bridge Logistics',
                       'author': 'Bridge Logistics',
                       'text': 'It is not uncommon for one load to be rebrokered two, three, four or even '
                               'more times before reaching its final destination, especially in markets '
                               'with heavy freight flows such as Chicago, Los Angeles and Atlanta.',
                       'tip': 'It is not uncommon for one load to be rebrokered two, three, four or even '
                              'more times before reaching its final destination, especially in markets '
                              'with heavy freight flows such as Chicago, Los Angeles and Atlanta.',
                       'timestamp': 51,
                       'timestamp_seconds': 51,
                       'timestamp_label': '[00:00:51]',
                       'url': 'https://www.youtube.com/watch?v=uT4ymtB7YcA&t=51s',
                       'markdown': '[00:00:51](https://www.youtube.com/watch?v=uT4ymtB7YcA&t=51s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '5dP6IV7sJW0',
                       'title': 'Trucking Scams & Fraud Prevention How to Avoid Double Brokering Pitfalls',
                       'channel': 'Truck Driver Nation',
                       'author': 'Truck Driver Nation',
                       'text': 'The biggest thing is you want to recover the money as quick as possible, '
                               "because for a driver and owner operator it's fuel money and the majority "
                               'of that money is going to go to fuel.',
                       'tip': 'The biggest thing is you want to recover the money as quick as possible, '
                              "because for a driver and owner operator it's fuel money and the majority of "
                              'that money is going to go to fuel.',
                       'timestamp': 195,
                       'timestamp_seconds': 195,
                       'timestamp_label': '[00:03:15]',
                       'url': 'https://www.youtube.com/watch?v=5dP6IV7sJW0&t=195s',
                       'markdown': '[00:03:15](https://www.youtube.com/watch?v=5dP6IV7sJW0&t=195s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'o7UDt2VXwwU',
                       'title': 'Carrier411’s Overreach: Stripping Carriers of Defense and Due Process',
                       'channel': 'Double Broker Bounty Hunter',
                       'author': 'Double Broker Bounty Hunter',
                       'text': 'Freight Guards can now be applied against carriers for exercising their '
                               "statutory rights, such as filing on a broker's bond when a broker fails to "
                               'pay the carrier.',
                       'tip': 'Freight Guards can now be applied against carriers for exercising their '
                              "statutory rights, such as filing on a broker's bond when a broker fails to "
                              'pay the carrier.',
                       'timestamp': 112,
                       'timestamp_seconds': 112,
                       'timestamp_label': '[00:01:52]',
                       'url': 'https://www.youtube.com/watch?v=o7UDt2VXwwU&t=112s',
                       'markdown': '[00:01:52](https://www.youtube.com/watch?v=o7UDt2VXwwU&t=112s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '3dI5z6SHDPc',
                       'title': "DBBH's Fraud Prevention Series 2.0 - Part 3 - Warning Signs Double "
                                'Brokers',
                       'channel': 'Double Broker Bounty Hunter',
                       'author': 'Double Broker Bounty Hunter',
                       'text': 'One of the things I always recommend to every carrier is to have a color '
                               "rubber stamp for your drivers to sign on, with the carrier's MC number, "
                               "the carrier name, and the driver's name on it.",
                       'tip': 'One of the things I always recommend to every carrier is to have a color '
                              "rubber stamp for your drivers to sign on, with the carrier's MC number, the "
                              "carrier name, and the driver's name on it.",
                       'timestamp': 685,
                       'timestamp_seconds': 685,
                       'timestamp_label': '[00:11:25]',
                       'url': 'https://www.youtube.com/watch?v=3dI5z6SHDPc&t=685s',
                       'markdown': '[00:11:25](https://www.youtube.com/watch?v=3dI5z6SHDPc&t=685s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'}]}
