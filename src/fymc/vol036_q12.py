from __future__ import annotations

CHAPTER_12 = {'id': 'Q12',
 'chapter_id': 'Q12',
 'chapter_number': 12,
 'question_number': 12,
 'slug': 'carrier-compliance-telecom-business-models',
 'question_prompt': 'What regulatory obligations and business models govern running a voice carrier, MVNO, '
                    'or eSIM operation?',
 'kicker': 'Q12 / THE BIG MONEY PLAYBOOKS',
 'title': 'Carrier Compliance and Telecom Business Models',
 'subtitle': 'STIR/SHAKEN and the squeeze on small VoIP carriers, Robocall Mitigation Database filings, '
             'FCC Form 499, USF contributions and the court ruling, state USF assessments, telecom company '
             'economics, launching and scaling an MVNO, IoT eSIM, travel eSIM roaming, and eSIM resale '
             'platforms',
 'layout_template': 'action_worksheet_summary',
 'reading_time_minutes': 15,
 'executive_summary': 'Compliance now decides who survives in voice resale. Crosstalk, Sangoma, Bandwidth, '
                      'and Techmode agree on the A/B/C attestation ladder, and Crosstalk reports C '
                      "signings drive most T-Mobile spam flags, while ZCorum's Rick reports that every "
                      'provider, including infrastructure-free resellers, must file in the Robocall '
                      'Mitigation Database or face refused traffic from May 28, 2024. Tony Lewis of '
                      'ClearlyIP prices the iconectiv token and certificate at thousands a year each, '
                      'against a Crosstalk resale margin of only 15 to 20 percent. USF pass-through runs '
                      'four to five dollars a bill, with the contribution factor at 25 to 33 percent. The '
                      'split: Sangoma says resellers need not implement and ZCorum notes they may file '
                      'without a STIR/SHAKEN obligation, yet Crosstalk was told it was covered and found '
                      'neither adviser correct.',
 'key_metrics': [{'label': 'Voice Resale Net Margin',
                  'metric': 'Voice Resale Net Margin',
                  'value': '15 to 20 percent profit margin per month',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Crosstalk's SIP resale side business, roughly 60 to 70 customers on VoIP "
                             'Innovations upstream, after FCC and state registration, tax engine, and '
                             'billing costs once it turned a profit',
                  'source': 'Crosstalk Solutions ([ycGPHG_ANrE @ 00:07:43])'},
                 {'label': 'USF Contribution Factor',
                  'metric': 'USF Contribution Factor',
                  'value': '25 to 33 percent, up from low single digits',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Ariel Roth's framing of the factor assessed on interstate and international "
                             'voice revenues and passed to consumers as a line item',
                  'source': 'The Federalist Society ([EL34vsXYuGQ @ 00:03:00])'},
                 {'label': 'RMD Traffic Refusal Date',
                  'metric': 'RMD Traffic Refusal Date',
                  'value': 'May 28, 2024',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Date from which voice service providers and intermediate providers must '
                             'refuse traffic from any provider not listed in the Robocall Mitigation '
                             'Database',
                  'source': 'ZCorum ([ZLzeR3N0mpc @ 00:05:20])'},
                 {'label': 'Kigen eSIM Revenue Share',
                  'metric': 'Kigen eSIM Revenue Share',
                  'value': "About 70 percent of last quarter's revenue, up from about 10 percent four "
                           'years ago',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Vincent Custany's disclosure of how much of Kigen's revenue is now "
                             'eSIM-based',
                  'source': 'The Things Industries ([u_m7kYjI4ow @ 00:14:14])'}],
 'sections': [{'heading': 'The Practitioner Consensus',
               'paragraphs': ['Every STIR/SHAKEN practitioner lands on the same three-grade ladder, and '
                              'the grade is a commercial weapon. Chris of Crosstalk and ClearlyIP CEO Tony '
                              'Lewis define A as a known customer on an owned number, B as a known '
                              'customer on an unverified number such as follow-me forwarding, and C as a '
                              'gateway call, the grade most likely to be marked spam [ycGPHG_ANrE @ '
                              '00:02:43]. Briana Sullivan of Bandwidth frames A around known right-to-use, '
                              'B as a known customer with an unknown number source, and C as originated '
                              'onto the network but unauthenticated, with the SIP Identity Header carrying '
                              'calling number, called number, timestamp, attestation level, and a unique '
                              'origination ID for traceback [G91y9mjo-pk @ 00:01:49]. Tim Lin of Sangoma '
                              'ties the grade directly to inventory: A means the DID was bought from '
                              'Sangoma, B a third-party DID, C an international gateway [3XJ9OkK8aFw @ '
                              '00:07:34]. Techmode, which sends every one of its numbers out with A '
                              'attestation, adds the operator reality check: STIR/SHAKEN does not itself '
                              'block calls or paint the spam-likely label, analytics companies do that, '
                              'and non-IP hops can strip the seal entirely [KjFy5hTaOcM @ 00:01:25]. '
                              "Crosstalk's standing rule follows from all of it: anything other than an A "
                              'on the checker number gets fixed.',
                              'The second point of agreement is that reselling does not buy anyone out of '
                              'the paperwork. Crosstalk ran a SIP resale side business for roughly 60 to '
                              '70 customers on VoIP Innovations upstream, and it still required FCC and '
                              'state registration, tax remittance, and billing [ycGPHG_ANrE @ 00:06:53]. '
                              'Rick at ZCorum reads the January 25 public notice the same way: every '
                              'provider must file certifications and plans in the Robocall Mitigation '
                              'Database, including intermediate providers and resellers that own no '
                              'infrastructure, with existing filers forced to update by February 26, 2024 '
                              '[ZLzeR3N0mpc @ 00:02:27]. Tim Lin lists the self-signing prerequisites as a '
                              '499-A filing, an OCN from NANPA, and direct SOMOS number access '
                              '[3XJ9OkK8aFw @ 00:19:14]. Legal Registration hammers the 499-A angle from '
                              'the filing side: every US telecom provider, VoIP included, needs a DC agent '
                              'secured through the form, it is filed every year before April 1st to report '
                              'USF revenue, and it grants no license on its own, so a separate license '
                              'application is still required [Lqlbag5CQMU @ 00:01:21]. The consensus '
                              'baseline for anyone selling voice minutes is therefore stacked: '
                              'registration, annual revenue reporting, an RMD listing with a mitigation '
                              "plan, and an FRN behind all of it, because the upstream carrier's "
                              "compliance does not carry the reseller's name.",
                              'Across voice, wireless, and IoT, practitioners agree that regulatory cost '
                              'flows straight into the unit economics and lands on the customer bill. Eric '
                              'Yuzi at ZCorum puts USF fees at about four or five dollars per bill, funded '
                              'by landline, mobile, and VoIP revenue on a shrinking base, and argues that '
                              "every fee passes to consumers anyway: there's no such thing as a free lunch "
                              "[QPBt987oumw @ 00:14:38]. Ariel Roth's Federalist Society framing confirms "
                              'the mechanism, with contributions assessed on interstate and international '
                              'voice revenue, passed through as a line item, and the contribution factor '
                              'climbing from low single digits to 25 to 33 percent [EL34vsXYuGQ @ '
                              '00:03:00]. On the wireless side, Brian Lachford of Atomic Mobile, who has '
                              'helped launch 100-plus MVNOs, warns that billing and tax surprises show up '
                              'with the first invoice and that state filings must be done before launch, '
                              'because after launch you are cleaning up a mess [Gye5g8KT7Oo @ 00:08:58]. '
                              'IoT (eSIM) Studio defines the structural split every model sits on: MNOs '
                              'own the network, MVNOs resell connectivity without owning the underlying '
                              'network patrimony, and aggregators contract with both, so the first '
                              'diligence question is always who you can switch to and at what cost '
                              '[GZtF-I2M1ZE @ 00:01:27].'],
               'table': {'caption': 'Where voice, wireless, and eSIM practitioners agree on baseline '
                                    'carrier obligations',
                         'headers': ['Consensus Point',
                                     'What Practitioners Report',
                                     'Operator Implication',
                                     'Expert Source'],
                         'rows': [['Attestation grade drives downstream call treatment',
                                   'A means known customer and owned number; C is the gateway grade most '
                                   'likely marked spam',
                                   'Fix anything other than A on the checker number before scaling '
                                   'outbound volume',
                                   'Crosstalk Solutions ([ycGPHG_ANrE @ 00:02:43])'],
                                  ['Attestation grade is tied to number inventory',
                                   'A when the DID was bought from Sangoma, B for third-party DIDs, C for '
                                   'international gateway',
                                   'Buy numbers from the signing carrier whenever A attestation matters '
                                   'commercially',
                                   'Sangoma ([3XJ9OkK8aFw @ 00:07:34])'],
                                  ['Signing does not equal blocking or labeling',
                                   'Analytics companies, not STIR/SHAKEN itself, block calls and apply the '
                                   'spam likely label',
                                   "Treat attestation as one signal inside the analytics engines' wider "
                                   'scoring of each call',
                                   'Techmode Business Phone Systems ([KjFy5hTaOcM @ 00:01:25])'],
                                  ['The identity header carries traceback data',
                                   'SIP Identity Header holds calling and called number, timestamp, '
                                   'attestation level, origination ID',
                                   'Every signed call can be traced back to the originating provider that '
                                   'attested it',
                                   'Bandwidth ([G91y9mjo-pk @ 00:02:09])'],
                                  ['Resellers must be listed in the RMD',
                                   'All providers, including intermediates and resellers without '
                                   'infrastructure, file certifications and plans',
                                   'Unlisted providers get their traffic refused by upstream carriers from '
                                   'May 28, 2024',
                                   'ZCorum ([ZLzeR3N0mpc @ 00:02:27])'],
                                  ['Annual 499-A filing and DC agent',
                                   'Filed every year before April 1st, used for USF revenue reporting, '
                                   'applies to VoIP providers',
                                   'Registration grants no license, so a separate license application is '
                                   'still needed',
                                   'Legal Registration ([Lqlbag5CQMU @ 00:01:21])'],
                                  ['Taxes and state filings are planned pre-launch',
                                   'Billing and tax surprises arrive with the first invoice; file in every '
                                   'state before launch',
                                   'Post-launch fixes mean cleaning up a mess instead of building the MVNO '
                                   'business',
                                   'The Boon of Wireless ([Gye5g8KT7Oo @ 00:08:58])']]}},
              {'heading': 'Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['Tony Lewis lays out the self-signing bill line by line. The iconectiv token '
                              'runs thousands a year, priced as a percentage of 499 revenue with a minimum '
                              'fee, getting it means clearing a multi-page sandbox test case, and the '
                              'certificate itself costs thousands a year against roughly $100 for SSL '
                              '[ycGPHG_ANrE @ 00:10:42]. Tim Lin confirms the governance chain behind '
                              'those invoices: ATIS is the governance authority, iconectiv is the policy '
                              'administrator that issues tokens and sets an annual fee based on FCC-filed '
                              'revenue, and multiple certificate authorities are listed by iconectiv '
                              '[3XJ9OkK8aFw @ 00:05:29]. The cheap path small operators reach for is '
                              'forking the call to a signing provider, which requires a PJSIP patch plus a '
                              'first and second trunk in FreePBX outbound routes, a setup Chris calls a '
                              'bubble gum and Band-Aid solution [ycGPHG_ANrE @ 00:12:53]. The proper path '
                              'Tony describes is a real SBC build with redundancy, geographic failover on '
                              'both coasts, DID, credential, and IP mapping, and 911 caller-ID logic. '
                              "Against that cost stack, Crosstalk's resale business peaked at 130,000 to "
                              '140,000 calls per month and netted only 15 to 20 percent margin every month '
                              'once profitable, while ClearlyIP handles tens of millions [ycGPHG_ANrE @ '
                              '00:07:43].',
                              'Rick at ZCorum turns the RMD rule into a repeatable know-your-customer '
                              'routine. Verify identity, address, years in business, and time at that '
                              'address, then ask what the service is actually for, because a pizza shop is '
                              'a different risk from a call center or telemarketer [ZLzeR3N0mpc @ '
                              '00:07:52]. Terms of service should allow immediate termination on reported '
                              'abuse, the filer certifies full, partial, or no STIR/SHAKEN implementation, '
                              'and the mitigation plan itself is usually just one page long. The sample '
                              'WOW plan Rick walks through commits to traceback cooperation, vets '
                              'businesses on name, physical and mailing address, tax ID, phone, email, and '
                              'PIN, and blocks unassigned numbers, with an FCC Registration Number '
                              'required to file [ZLzeR3N0mpc @ 00:13:22]. Tim Lin layers on the '
                              'carrier-side obligations: cooperate with the Industry Traceback Group and '
                              'law enforcement, and expect calls from providers without a certificate on '
                              "file to be refused from September 28, 2021 [3XJ9OkK8aFw @ 00:15:13]. Lin's "
                              'routing rule is blunt: sign your own calls if you are multi-vendor or an '
                              'outbound contact center, otherwise you face caller-ID-based routing. On the '
                              'foreign side, Chris and Tony Lewis say carriers handling foreign gateway '
                              'traffic face a binary choice, know your customer or block [ycGPHG_ANrE @ '
                              '00:25:56].',
                              'On the wireless and eSIM side the mechanics are platform-driven. Brian '
                              'Lachford says MVNOs otherwise juggle three to six vendors, launches that '
                              'once took six months with a one-week port now port in minutes, and Atomic '
                              'Mobile hands out a free 100-item launch checklist with no signup '
                              '[Gye5g8KT7Oo @ 00:13:33]. Lachford flags real-time usage as the margin '
                              'lever: lags of 3, 6, or 9 hours make usage plans risky, so Atomic hired '
                              'Amanda Herman, 22 years at AT&T, to fix it for margins, fraud, and spam '
                              'control [Gye5g8KT7Oo @ 00:14:59]. Vincent Custany of Kigen pitches the IoT '
                              'version: a starter kit with complimentary eSIMs and three months of '
                              'connectivity across 9 to 12 MVNOs, and Kigen Pulse with API parity to the '
                              'UI so an operator can run a campaign switch, such as moving all of Germany '
                              'from MNO A to MNO B, without a truck roll [u_m7kYjI4ow @ 00:12:19]. The Top '
                              'New Code demo shows the retail reseller stack: upload profiles from any '
                              'carrier, build global, regional, and country plans with custom pricing, '
                              'deliver by QR with top-ups across 190-plus countries, and run unlimited '
                              'resellers and sub-resellers with commissions, balance limits, KYC, and no '
                              'monthly fees [e8R4z-ISWAo @ 00:01:45].'],
               'table': {'caption': 'Exact costs, tools, and filing mechanics quoted by working operators',
                         'headers': ['Mechanic',
                                     'Exact Number or Tool',
                                     'How Operators Use It',
                                     'Expert Source'],
                         'rows': [['iconectiv SPC token for self-signing',
                                   'Thousands a year, a percentage of 499 revenue with a minimum fee',
                                   'Budget it before choosing to self-sign instead of buying upstream '
                                   'signing',
                                   'Crosstalk Solutions ([ycGPHG_ANrE @ 00:10:42])'],
                                  ['STIR/SHAKEN signing certificate',
                                   'Thousands a year versus roughly $100 for a standard SSL certificate',
                                   'Weigh recurring certificate cost against a thin 15 to 20 percent '
                                   'resale margin',
                                   'Crosstalk Solutions ([ycGPHG_ANrE @ 00:11:48])'],
                                  ['Fork-to-signer workaround for FreePBX',
                                   'PJSIP patch plus a first and second trunk in FreePBX outbound routes',
                                   'Stopgap signing for small shops, which Chris calls bubble gum and '
                                   'Band-Aid',
                                   'Crosstalk Solutions ([ycGPHG_ANrE @ 00:12:53])'],
                                  ['Robocall Mitigation Database plan',
                                   'Usually one page, FRN required, certifying full, partial, or no '
                                   'STIR/SHAKEN',
                                   'File before May or upstream partners may refuse your traffic outright',
                                   'ZCorum ([ZLzeR3N0mpc @ 00:10:29])'],
                                  ['Sangoma fraud scoring on inbound callers',
                                   'Fraud score from 0 to 100, tagging robo spam or fraudulent caller',
                                   'Pull it via API or take it included with CNAM lookups',
                                   'Sangoma ([3XJ9OkK8aFw @ 00:21:03])'],
                                  ['Wisconsin AQS Section 3 uncollectibles entry',
                                   'Example 2024 write-offs of 52,000 and change, entered as positive '
                                   'numbers',
                                   'The system subtracts uncollectibles from gross revenues itself, so '
                                   'never enter negatives',
                                   'Public Service Commission of Wisconsin ([vH9VQq2V9Qw @ 00:05:41])'],
                                  ['Kigen Pulse campaign switching for IoT fleets',
                                   'API parity with the UI, moving all of Germany from MNO A to MNO B',
                                   'Switch carriers per country without a truck roll on 10 to 15 year '
                                   'devices',
                                   'The Things Industries ([u_m7kYjI4ow @ 00:12:19])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Attestation, Spend, and Switching Levers Operators Actually Pull',
                           'body': 'Small moves practitioners use to lift attestation, cap exposure, and '
                                   'keep carrier leverage.',
                           'items': ['Buy DIDs from the carrier that signs your calls: Tim Lin says A '
                                     'attestation means the DID was bought from Sangoma, while third-party '
                                     'DIDs drop to B [Sangoma — 3XJ9OkK8aFw @ 00:07:34].',
                                     'Follow-me forwarding signs B today; ClearlyIP is building header '
                                     'hairpinning to sign it A because the right to use standard is what '
                                     'matters [Crosstalk Solutions — ycGPHG_ANrE @ 00:28:28].',
                                     "Cap exposure on outbound termination: Sangoma's A-Z termination "
                                     'ships with daily spend and per-minute caps [Sangoma — 3XJ9OkK8aFw @ '
                                     '00:21:59].',
                                     'Run the switching test before signing an IoT connectivity deal: who '
                                     'can I switch to today and how much will it cost, because if you '
                                     'cannot switch you are locked by technology [IoT (eSIM) Studio — '
                                     'GZtF-I2M1ZE @ 00:02:51].']},
               'sop_steps': [{'step': 1,
                              'title': 'Register and file the 499-A',
                              'action': 'Secure a DC agent through Form 499-A and calendar the annual '
                                        'filing before April 1st.',
                              'detail': 'Legal Registration says every US telecom and VoIP provider needs '
                                        'a DC agent via the form or faces massive fines, and the filing '
                                        'repeats every year [Legal Registration — Lqlbag5CQMU @ '
                                        '00:00:21].'},
                             {'step': 2,
                              'title': 'Build the know-your-customer intake',
                              'action': 'Verify identity, address, years in business, time at address, and '
                                        'the intended use of the service.',
                              'detail': 'Rick separates a pizza shop from a call center or telemarketer '
                                        'and wants terms of service that allow immediate termination on '
                                        'reported abuse [ZCorum — ZLzeR3N0mpc @ 00:07:39].'},
                             {'step': 3,
                              'title': 'File the RMD certification and plan',
                              'action': 'Submit the one-page mitigation plan with an FRN and certify full, '
                                        'partial, or no STIR/SHAKEN.',
                              'detail': 'From May 28, 2024 providers cannot accept traffic from unlisted '
                                        'non-gateway intermediates, so an unlisted reseller loses its '
                                        'upstream [ZCorum — ZLzeR3N0mpc @ 00:04:49].'},
                             {'step': 4,
                              'title': 'Pick a signing path and verify the grade',
                              'action': 'Choose fork-to-signer or a proper SBC build, then call the '
                                        'checker number to confirm attestation.',
                              'detail': 'Chris checks the live number against 920-66-1392 and treats '
                                        'anything other than A as a problem to fix [Crosstalk Solutions — '
                                        'ycGPHG_ANrE @ 00:04:31].'}]},
              {'section': 3,
               'title': 'Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The sharpest split in the reseller trench is whether a shop riding someone '
                              "else's switch owes its own signing. Tim Lin of Sangoma told VoIP "
                              'Innovations resellers they were not required to implement STIR/SHAKEN '
                              "themselves, while still telling them to get a regulatory expert's read on "
                              'their specific setup [3XJ9OkK8aFw @ 00:16:48]. Chris of Crosstalk Solutions '
                              'lived the other side of that answer. VoIP Innovations and a telecom lawyer '
                              'both told Chris the business was covered, and "neither of them were '
                              'correct," after FCC legal had already mailed what Chris called "pretty '
                              'threatening" letters [ycGPHG_ANrE @ 00:20:06]. Tony Lewis of ClearlyIP drew '
                              'the line in one sentence: whoever is charging the end user is the '
                              'originating service provider under the spec, no matter whose network '
                              'carries the minutes [ycGPHG_ANrE @ 00:20:52]. Rick at ZCorum sits between '
                              'the camps. Resellers can select the "without a STIR/SHAKEN obligation" box '
                              'in the Robocall Mitigation Database, yet Rick sees many tick "complete" '
                              'simply because their upstream is compliant, and he tells them to run that '
                              'choice past an attorney before filing [ZLzeR3N0mpc @ 00:16:08]. The '
                              "operator takeaway is blunt: the vendor's assurance and the regulator's "
                              'reading diverged, and the reseller who trusted the vendor is the one who '
                              'received the letter.',
                              'On how to actually get calls signed, three playbooks compete. Tony Lewis '
                              'priced the do-it-yourself route: the iconectiv token runs "thousands a '
                              'year," pegged as a percentage of 499 revenue with a minimum fee, and the '
                              'certificate is another "thousands a year" against roughly $100 for an '
                              'ordinary SSL cert [ycGPHG_ANrE @ 00:10:42]. The cheap alternative is '
                              'forking each call to a signing provider, which needs a PJSIP patch plus a '
                              'first and second trunk in the FreePBX outbound routes; Chris dismissed it '
                              'as a "bubble gum and Band-Aid" fix rather than real infrastructure '
                              '[ycGPHG_ANrE @ 00:12:53]. Tim Lin of Sangoma argues self-signing pays when '
                              'you are multi-vendor or running an outbound contact center, because '
                              'otherwise you are stuck with caller-ID-based routing, and the entry ticket '
                              'is a 499-A filing, an OCN from NANPA, and direct SOMOS number access '
                              '[3XJ9OkK8aFw @ 00:17:44]. Rick at ZCorum pitched a third lane through Voice '
                              'Select, where the reseller keeps only the customer premises equipment and '
                              'the know-your-customer work while the platform carries everything else '
                              '[ZLzeR3N0mpc @ 00:19:17]. The choice comes down to vendor count, outbound '
                              'volume, and whether you can afford to own certificates, tokens, and test '
                              'cases yourself every year.',
                              'MVNO builders split on speed and on whether to own the stack. Brian '
                              'Lachford of Atomic Mobile says launches that once took six months with '
                              'week-long ports now port in minutes, while host John Horvitz pushed back '
                              'that going direct to a carrier took a full year [Gye5g8KT7Oo @ 00:10:05]. '
                              'Lachford insists there is "not really a window of capitalizing on '
                              'developing your own software," adding that designing a platform is easy and '
                              'that AI-built MVNE platforms routinely ship without the billing logic that '
                              'actually runs the business [Gye5g8KT7Oo @ 00:17:36]. Top New Code sells the '
                              'opposite instinct: a white-label eSIM storefront with multi-vendor mode, '
                              'unlimited resellers, commissions, KYC, payment gateways, currency and '
                              'branding controls, pitched as "modular and customizable" with no monthly '
                              'fees [e8R4z-ISWAo @ 00:02:02]. On the IoT and connectivity side, IoT (eSIM) '
                              'Studio tells buyers to pressure-test any MNO, MVNO, or aggregator with one '
                              'question: which provider can I switch to today, and what will it cost? If '
                              'you cannot switch, you are locked by technology and the lack of service; if '
                              'switching costs unreasonably, you are locked commercially [GZtF-I2M1ZE @ '
                              "00:02:51]. Lachford's camp buys speed and billing maturity from a "
                              'specialist, while the storefront camp bets that packaged software plus '
                              'reseller tiers is enough to start selling data.'],
               'table': {'caption': 'Practitioner fault lines on carrier compliance, signing, MVNO builds, '
                                    'and USF funding',
                         'headers': ['Fault Line', 'Position A', 'Position B', 'Expert Source'],
                         'rows': [['Whether VoIP resellers must sign their own calls',
                                   'Sangoma said VI resellers were not required to implement STIR/SHAKEN '
                                   'themselves',
                                   'Chris says the upstream and a telecom lawyer were both wrong once FCC '
                                   'letters arrived',
                                   'Sangoma ([3XJ9OkK8aFw @ 00:16:48]); Crosstalk Solutions ([ycGPHG_ANrE '
                                   '@ 00:20:06])'],
                                  ['How resellers should certify inside the Robocall Mitigation Database',
                                   'Rick says resellers may select without a STIR/SHAKEN obligation, '
                                   'though many check complete',
                                   'Tony says whoever charges the end user is the originating service '
                                   'provider under the spec',
                                   'ZCorum ([ZLzeR3N0mpc @ 00:16:08]); Crosstalk Solutions ([ycGPHG_ANrE @ '
                                   '00:20:52])'],
                                  ['Which signing architecture a small carrier should actually deploy',
                                   'Fork calls to a signing provider using a PJSIP patch and two FreePBX '
                                   'trunks',
                                   'Run proper SBCs with redundancy, failover on both coasts, DID mapping, '
                                   'and 911 logic',
                                   'Crosstalk Solutions ([ycGPHG_ANrE @ 00:12:53]); Crosstalk Solutions '
                                   '([ycGPHG_ANrE @ 00:15:25])'],
                                  ['How fast a new MVNO can realistically reach the market',
                                   'Lachford says six-month launches and week-long ports have collapsed to '
                                   'ports in minutes',
                                   'Host John Horvitz countered that going direct to a carrier took a full '
                                   'year',
                                   'The Boon of Wireless ([Gye5g8KT7Oo @ 00:09:29]); The Boon of Wireless '
                                   '([Gye5g8KT7Oo @ 00:10:05])'],
                                  ['Build your own platform or buy packaged eSIM and MVNE software',
                                   'Lachford sees no window for capitalizing on your own software and '
                                   'warns about missing billing logic',
                                   'Top New Code sells a modular multi-vendor eSIM platform with reseller '
                                   'tiers and no monthly fees',
                                   'The Boon of Wireless ([Gye5g8KT7Oo @ 00:17:36]); Top New Code '
                                   '([e8R4z-ISWAo @ 00:02:02])'],
                                  ['Who should pay into the Universal Service Fund going forward',
                                   'Carr, Simington, and USTelecom favor assessing edge providers rather '
                                   'than broadband ISPs',
                                   'The FCC report warns ISP assessment hurts affordability; Yuzi argues '
                                   'every fee hits consumers anyway',
                                   'ZCorum ([QPBt987oumw @ 00:17:48]); ZCorum ([QPBt987oumw @ 00:14:07])'],
                                  ['Whether the USF contribution charge is a tax or a fee',
                                   'Furchtgott-Roth calls it a tax and calls the USAC structure lawless '
                                   'and deeply troubling',
                                   'Romano notes the DC Circuit and Fifth Circuit both called USF a fee',
                                   'The Federalist Society ([EL34vsXYuGQ @ 00:39:03]); The Federalist '
                                   'Society ([EL34vsXYuGQ @ 00:30:17])']]}},
              {'section': 4,
               'title': 'Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The resale math broke first. Chris ran the Crosstalk SIP side business on '
                              'VoIP Innovations for 60 to 70 customers while carrying FCC and state '
                              'registration, tax remittance through a paid third-party tax engine, and '
                              'billing, and once it finally turned a profit it cleared only "15 to 20 '
                              'percent profit margin every month" [ycGPHG_ANrE @ 00:07:43]. That margin '
                              'leaves no room for the next layer of cost. Tony Lewis says Inteliquent will '
                              'only sign C attestation when the customer has no certificate of their own, '
                              'which means the reseller pays for carriage and still ships the worst grade '
                              'available [ycGPHG_ANrE @ 00:21:20]. The penalty shows up at the handset: '
                              'Tony traces T-Mobile "likely spam" flags back to a C signing "nine times '
                              'out of ten," and SS7 hops along the route can strip the identity header '
                              'entirely [ycGPHG_ANrE @ 00:23:01]. Techmode adds the uncomfortable detail '
                              'that a clean signature does not settle the matter either. Non-IP hops can '
                              'strip the seal, STIR/SHAKEN itself never applies the "spam likely" label '
                              'because analytics companies do, and even all-A traffic is only one signal '
                              'among several that the terminating side weighs [KjFy5hTaOcM @ 00:01:25]. '
                              'Thin margin plus a fixed signing bill plus downgraded attestation is how '
                              'small VoIP carriers get squeezed out.',
                              'The 2024 Robocall Mitigation Database order turned paperwork into a kill '
                              'switch. Rick at ZCorum read it plainly: as of May 28, 2024, voice and '
                              'intermediate providers "must refuse to carry traffic from any provider '
                              'that\'s not listed," and he warned resellers to file before May or watch '
                              'their upstream partner refuse their traffic, even if fines for the February '
                              'deadline never land [ZLzeR3N0mpc @ 00:05:20]. The plan itself is where '
                              "operators get caught. Rick's know-your-customer bar asks what the service "
                              'is actually for, because a pizza shop is a different risk than a call '
                              'center or telemarketer, and the terms of service should allow immediate '
                              'termination on reported abuse [ZLzeR3N0mpc @ 00:07:52]. Tony Lewis applies '
                              'the same logic to foreign gateways: know the customer or block the traffic, '
                              'because that inbound flood is exactly what traceback lands on [ycGPHG_ANrE '
                              '@ 00:25:56]. Underneath sits the annual filing treadmill. Legal '
                              'Registration stresses that the 499-A is not a one-time event; it must be '
                              'filed every year before April 1, VoIP providers included, a provider '
                              'without a DC agent faces massive fines and penalties, and the filing itself '
                              'grants no license [Lqlbag5CQMU @ 00:01:21]. Miss any layer and the network, '
                              'not the regulator, is what cuts you off first.',
                              'MVNO founders bleed in places they never modeled. Brian Lachford says '
                              'billing and tax surprises arrive with the first invoice, and that filing in '
                              'every state is something you "plan before you launch, not after you launch, '
                              'cuz after you launch, you\'re essentially cleaning up a mess" [Gye5g8KT7Oo '
                              '@ 00:08:58]. Usage feeds that lag three, six, or nine hours make '
                              'usage-based plans risky, which is why Atomic hired Amanda Herman, a 22-year '
                              'AT&T veteran, to chase real-time data for margins, fraud, and spam control '
                              "[Gye5g8KT7Oo @ 00:14:59]. Lachford's fastest tell of a doomed brand is a "
                              'founder chasing Mint-level pricing, visible within five to ten minutes of '
                              'the first conversation, alongside founders who keep changing their minds '
                              'about the plan [Gye5g8KT7Oo @ 00:18:30]. B2B roaming carries its own '
                              'exposure. A Virtuser panelist described a wealthy, travel-heavy firm that '
                              'banned roaming outright because costs escalate fast beyond the 30 to 40 big '
                              'countries into zones two through six, and staff needed line-manager '
                              'sign-off proving a time-sensitive deal just to switch roaming on '
                              '[6sIXgGXsu3E @ 00:00:29]. Airport and hotel Wi-Fi does not rescue that '
                              'traveler either; the same panelist called it untrusted, maxed out, slow, '
                              'and patchy between the room and the lobby.'],
               'table': {'caption': 'Firsthand traps, losses, and economics checks reported by carrier and '
                                    'MVNO practitioners',
                         'headers': ['Failure Mode',
                                     'What Practitioners Reported',
                                     'Operator Check',
                                     'Expert Source'],
                         'rows': [['Trusting the upstream carrier and a lawyer on reseller coverage',
                                   'Both told Chris the business was covered, and neither of them were '
                                   'correct',
                                   'Verify your own RMD listing and obligations rather than relying on '
                                   'vendor assurances',
                                   'Crosstalk Solutions ([ycGPHG_ANrE @ 00:20:06])'],
                                  ['Shipping C attestation because you hold no certificate of your own',
                                   'Inteliquent signs only C without a customer certificate, and C drives '
                                   'T-Mobile spam flags',
                                   'Run the checker number and treat anything other than A as a fix',
                                   'Crosstalk Solutions ([ycGPHG_ANrE @ 00:21:20])'],
                                  ['Staying unlisted in the Robocall Mitigation Database past the cutoff',
                                   'From May 28, 2024, providers must refuse traffic from any unlisted '
                                   'provider',
                                   'File the certification and plan early, and update any existing filing '
                                   'on time',
                                   'ZCorum ([ZLzeR3N0mpc @ 00:05:20])'],
                                  ['Launching an MVNO before modeling billing and state tax exposure',
                                   'Billing and tax surprises arrive with the very first invoice after '
                                   'launch',
                                   'File in every state and build tax handling before the launch date',
                                   'The Boon of Wireless ([Gye5g8KT7Oo @ 00:08:11])'],
                                  ['Selling usage plans on top of lagging usage data feeds',
                                   'Usage lags of three, six, or nine hours make usage plans risky',
                                   'Get real-time usage visibility before selling plans that meter '
                                   'consumption',
                                   'The Boon of Wireless ([Gye5g8KT7Oo @ 00:14:59])'],
                                  ['Entering uncollectibles as negative numbers on the Wisconsin '
                                   'questionnaire',
                                   'The system already subtracts uncollectibles from gross revenues on its '
                                   'own',
                                   'Enter uncollectible revenue as a positive number and explain any '
                                   'nonzero other offsets',
                                   'Public Service Commission of Wisconsin ([vH9VQq2V9Qw @ 00:05:41])'],
                                  ['Assuming the USAC collection machinery is permanently settled law',
                                   'The Fifth Circuit held the FCC overstepped in building its USAC '
                                   'collection mechanism',
                                   'Watch for an FCC appeal or stay and any legislative fix from Congress',
                                   'LATEST NEWS UPDATE ([yh-FMlChr9U @ 00:01:45])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Clear These Four Before Moving Another Minute or Activating Another '
                                    'Line',
                           'body': 'Every item below comes from an operator who got burned, nearly got '
                                   'burned, or watched clients get burned on carrier compliance and MVNO '
                                   'launches.',
                           'items': ['Confirm your own Robocall Mitigation Database listing and '
                                     'certification instead of trusting your upstream carrier or lawyer, '
                                     'because both were wrong for Chris [Crosstalk Solutions — ycGPHG_ANrE '
                                     '@ 00:20:06].',
                                     'Call the attestation checker number 920-66-1392 from your own trunk '
                                     'and fix anything that comes back other than A [Crosstalk Solutions — '
                                     'ycGPHG_ANrE @ 00:04:31].',
                                     'File in every state and model billing and tax before launch, since '
                                     'cleaning it up after launch means cleaning up a mess [The Boon of '
                                     'Wireless — Gye5g8KT7Oo @ 00:08:58].',
                                     'On state assessment filings, enter uncollectibles as positive '
                                     'numbers because the system subtracts them itself [Public Service '
                                     'Commission of Wisconsin — vH9VQq2V9Qw @ 00:05:41].']}}],
 'pull_quote': '"Once we started turning a profit with our crosstalk sip side business we were only making '
               'about 15 to 20 percent profit margin every month." Attributed to Crosstalk Solutions '
               '(ycGPHG_ANrE @ 00:07:43).',
 'diagram_id': 'diag-08',
 'action_checklist': ['Dial the attestation checker 920-66-1392 from every outbound trunk and fix any '
                      'result other than A [Crosstalk Solutions — ycGPHG_ANrE @ 00:04:31].',
                      'File your certification and usually one-page robocall mitigation plan in the RMD, '
                      'with an FRN in hand [ZCorum — ZLzeR3N0mpc @ 00:10:29].',
                      'Vet every new customer for identity, address, years in business, time at address, '
                      'and what the service is for [ZCorum — ZLzeR3N0mpc @ 00:07:39].',
                      'If you are multi-vendor or an outbound contact center, line up a 499-A, an OCN from '
                      'NANPA, and direct SOMOS access to sign your own calls [Sangoma — 3XJ9OkK8aFw @ '
                      '00:19:14].',
                      'File FCC Form 499-A every year before April 1 and keep a DC agent on record [Legal '
                      'Registration — Lqlbag5CQMU @ 00:01:21].',
                      'Before signing with any MNO, MVNO, or aggregator, ask who you can switch to today '
                      'and what switching will cost [IoT (eSIM) Studio — GZtF-I2M1ZE @ 00:02:51].'],
 'statutory_citations': [{'title': 'Crosstalk Solutions — STIR/SHAKEN and the Death of the Small VoIP '
                                   'Carrier [00:20:06]',
                          'url': 'https://www.youtube.com/watch?v=ycGPHG_ANrE&t=1206s',
                          'relevance': 'Primary practitioner testimony on a VoIP reseller told by its '
                                       'upstream and a telecom lawyer that it was covered, then hit with '
                                       'FCC letters.'},
                         {'title': 'ZCorum — All Voice Service Providers are Now Required to File in the '
                                   'Robocall Mitigation Database [00:05:20]',
                          'url': 'https://www.youtube.com/watch?v=ZLzeR3N0mpc&t=320s',
                          'relevance': 'Primary practitioner testimony on the May 28, 2024 rule forcing '
                                       'providers to refuse traffic from unlisted providers.'},
                         {'title': "The Federalist Society — Consumers' Research v. FCC and the Legality "
                                   'of the Universal Service Fund Contribution Regime [00:39:03]',
                          'url': 'https://www.youtube.com/watch?v=EL34vsXYuGQ&t=2343s',
                          'relevance': 'Primary practitioner testimony on the USAC structure, its budget, '
                                       'and the tax-versus-fee fight over USF contributions.'},
                         {'title': 'LATEST NEWS UPDATE — Appeals court voids 9 billion dollar FCC telecom '
                                   'fund [00:01:02]',
                          'url': 'https://www.youtube.com/watch?v=yh-FMlChr9U&t=62s',
                          'relevance': 'Primary practitioner testimony on the Fifth Circuit ruling against '
                                       "the FCC's USAC collection mechanism."}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'ycGPHG_ANrE',
                       'title': 'STIR/SHAKEN and the Death of the Small VoIP Carrier',
                       'channel': 'Crosstalk Solutions',
                       'author': 'Crosstalk Solutions',
                       'text': 'All of this combined means that once we started turning a profit with our '
                               'crosstalk sip side business we were only making about 15 to 20 percent '
                               'profit margin every month.',
                       'tip': 'All of this combined means that once we started turning a profit with our '
                              'crosstalk sip side business we were only making about 15 to 20 percent '
                              'profit margin every month.',
                       'timestamp': 463,
                       'timestamp_seconds': 463,
                       'timestamp_label': '[00:07:43]',
                       'url': 'https://www.youtube.com/watch?v=ycGPHG_ANrE&t=463s',
                       'markdown': '[00:07:43](https://www.youtube.com/watch?v=ycGPHG_ANrE&t=463s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ycGPHG_ANrE',
                       'title': 'STIR/SHAKEN and the Death of the Small VoIP Carrier',
                       'channel': 'Crosstalk Solutions',
                       'author': 'Crosstalk Solutions',
                       'text': "Whoever's charging the end user you're the originating service provider as "
                               'per the Edith spec.',
                       'tip': "Whoever's charging the end user you're the originating service provider as "
                              'per the Edith spec.',
                       'timestamp': 1252,
                       'timestamp_seconds': 1252,
                       'timestamp_label': '[00:20:52]',
                       'url': 'https://www.youtube.com/watch?v=ycGPHG_ANrE&t=1252s',
                       'markdown': '[00:20:52](https://www.youtube.com/watch?v=ycGPHG_ANrE&t=1252s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '3XJ9OkK8aFw',
                       'title': 'Everything You Need to Know About STIR SHAKEN Compliance',
                       'channel': 'Sangoma',
                       'author': 'Sangoma',
                       'text': 'This service uses a fraud score between zero and 100 based off of '
                               'behavioral analytics and caller id authentication and verification.',
                       'tip': 'This service uses a fraud score between zero and 100 based off of '
                              'behavioral analytics and caller id authentication and verification.',
                       'timestamp': 1263,
                       'timestamp_seconds': 1263,
                       'timestamp_label': '[00:21:03]',
                       'url': 'https://www.youtube.com/watch?v=3XJ9OkK8aFw&t=1263s',
                       'markdown': '[00:21:03](https://www.youtube.com/watch?v=3XJ9OkK8aFw&t=1263s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ZLzeR3N0mpc',
                       'title': 'All Voice Service Providers are Now Required to File in the Robocall '
                                'Mitigation Database',
                       'channel': 'ZCorum',
                       'author': 'ZCorum',
                       'text': 'Voice service providers and intermediate providers must refuse to carry '
                               "traffic from any provider that's not listed in the robocall mitigation "
                               'database as of May 28th 2024.',
                       'tip': 'Voice service providers and intermediate providers must refuse to carry '
                              "traffic from any provider that's not listed in the robocall mitigation "
                              'database as of May 28th 2024.',
                       'timestamp': 320,
                       'timestamp_seconds': 320,
                       'timestamp_label': '[00:05:20]',
                       'url': 'https://www.youtube.com/watch?v=ZLzeR3N0mpc&t=320s',
                       'markdown': '[00:05:20](https://www.youtube.com/watch?v=ZLzeR3N0mpc&t=320s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'G91y9mjo-pk',
                       'title': 'Understanding STIR/SHAKEN',
                       'channel': 'Bandwidth',
                       'author': 'Bandwidth',
                       'text': "There are between 4 and 5 billion robocalls made each month, and it's "
                               'estimated that around 40% of those are fraudulent.',
                       'tip': "There are between 4 and 5 billion robocalls made each month, and it's "
                              'estimated that around 40% of those are fraudulent.',
                       'timestamp': 0,
                       'timestamp_seconds': 0,
                       'timestamp_label': '[00:00:00]',
                       'url': 'https://www.youtube.com/watch?v=G91y9mjo-pk&t=0s',
                       'markdown': '[00:00:00](https://www.youtube.com/watch?v=G91y9mjo-pk&t=0s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'KjFy5hTaOcM',
                       'title': 'Telecom in Under 2-  What is STIR/SHAKEN?',
                       'channel': 'Techmode Business Phone Systems',
                       'author': 'Techmode Business Phone Systems',
                       'text': 'The FCC began requiring STIR/SHAKEN on internet-based phone networks in '
                               '2021, with extra time for smaller providers.',
                       'tip': 'The FCC began requiring STIR/SHAKEN on internet-based phone networks in '
                              '2021, with extra time for smaller providers.',
                       'timestamp': 66,
                       'timestamp_seconds': 66,
                       'timestamp_label': '[00:01:06]',
                       'url': 'https://www.youtube.com/watch?v=KjFy5hTaOcM&t=66s',
                       'markdown': '[00:01:06](https://www.youtube.com/watch?v=KjFy5hTaOcM&t=66s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Z1cWYFBLpTA',
                       'title': 'The Economics of Owning a Telecom Company',
                       'channel': 'Cost Anatomy',
                       'author': 'Cost Anatomy',
                       'text': 'T-Mobile alone spends roughly $10 billion a year on capital expenditure, '
                               'not to grow, just to stay in the fight.',
                       'tip': 'T-Mobile alone spends roughly $10 billion a year on capital expenditure, '
                              'not to grow, just to stay in the fight.',
                       'timestamp': 275,
                       'timestamp_seconds': 275,
                       'timestamp_label': '[00:04:35]',
                       'url': 'https://www.youtube.com/watch?v=Z1cWYFBLpTA&t=275s',
                       'markdown': '[00:04:35](https://www.youtube.com/watch?v=Z1cWYFBLpTA&t=275s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Gye5g8KT7Oo',
                       'title': 'How to Launch & Scale an MVNO Successfully?',
                       'channel': 'The Boon of Wireless',
                       'author': 'The Boon of Wireless',
                       'text': 'And these are things that you have to plan before you launch, not after '
                               "you launch, cuz after you launch, you're essentially cleaning up a mess.",
                       'tip': 'And these are things that you have to plan before you launch, not after you '
                              "launch, cuz after you launch, you're essentially cleaning up a mess.",
                       'timestamp': 538,
                       'timestamp_seconds': 538,
                       'timestamp_label': '[00:08:58]',
                       'url': 'https://www.youtube.com/watch?v=Gye5g8KT7Oo&t=538s',
                       'markdown': '[00:08:58](https://www.youtube.com/watch?v=Gye5g8KT7Oo&t=538s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Gye5g8KT7Oo',
                       'title': 'How to Launch & Scale an MVNO Successfully?',
                       'channel': 'The Boon of Wireless',
                       'author': 'The Boon of Wireless',
                       'text': "There's not really a window of capitalizing on developing your own "
                               'software.',
                       'tip': "There's not really a window of capitalizing on developing your own "
                              'software.',
                       'timestamp': 1056,
                       'timestamp_seconds': 1056,
                       'timestamp_label': '[00:17:36]',
                       'url': 'https://www.youtube.com/watch?v=Gye5g8KT7Oo&t=1056s',
                       'markdown': '[00:17:36](https://www.youtube.com/watch?v=Gye5g8KT7Oo&t=1056s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'u_m7kYjI4ow',
                       'title': 'eSIM for IoT: Changing Connectivity Without a Truck Roll — Kigen',
                       'channel': 'The Things Industries',
                       'author': 'The Things Industries',
                       'text': 'If you want to change operators, you have to do a truck roll.',
                       'tip': 'If you want to change operators, you have to do a truck roll.',
                       'timestamp': 68,
                       'timestamp_seconds': 68,
                       'timestamp_label': '[00:01:08]',
                       'url': 'https://www.youtube.com/watch?v=u_m7kYjI4ow&t=68s',
                       'markdown': '[00:01:08](https://www.youtube.com/watch?v=u_m7kYjI4ow&t=68s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '6sIXgGXsu3E',
                       'title': 'Travel eSIMs for B2B Roaming and MVNO Roaming with integrated optional '
                                'Wi-Fi',
                       'channel': 'Virtuser - Connectivity Mobilised',
                       'author': 'Virtuser - Connectivity Mobilised',
                       'text': "You needed to get your line manager to sign off that you're working on a "
                               'deal that is time sensitive in order to get roaming turned on.',
                       'tip': "You needed to get your line manager to sign off that you're working on a "
                              'deal that is time sensitive in order to get roaming turned on.',
                       'timestamp': 55,
                       'timestamp_seconds': 55,
                       'timestamp_label': '[00:00:55]',
                       'url': 'https://www.youtube.com/watch?v=6sIXgGXsu3E&t=55s',
                       'markdown': '[00:00:55](https://www.youtube.com/watch?v=6sIXgGXsu3E&t=55s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'e8R4z-ISWAo',
                       'title': 'eSIM International Platform – Buy & Sell Global Data | Full Admin + User '
                                'Panel Demo',
                       'channel': 'Top New Code',
                       'author': 'Top New Code',
                       'text': "The built-in QR delivery system means you don't need to manually send "
                               'anything.',
                       'tip': "The built-in QR delivery system means you don't need to manually send "
                              'anything.',
                       'timestamp': 289,
                       'timestamp_seconds': 289,
                       'timestamp_label': '[00:04:49]',
                       'url': 'https://www.youtube.com/watch?v=e8R4z-ISWAo&t=289s',
                       'markdown': '[00:04:49](https://www.youtube.com/watch?v=e8R4z-ISWAo&t=289s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'GZtF-I2M1ZE',
                       'title': 'BEST MNO, MVNO for cellular data connectivity with eSIM (eUICC) SIM card',
                       'channel': 'IoT (eSIM) Studio',
                       'author': 'IoT (eSIM) Studio',
                       'text': "If you can't switch today you are locked by technology and the lack of "
                               'service.',
                       'tip': "If you can't switch today you are locked by technology and the lack of "
                              'service.',
                       'timestamp': 171,
                       'timestamp_seconds': 171,
                       'timestamp_label': '[00:02:51]',
                       'url': 'https://www.youtube.com/watch?v=GZtF-I2M1ZE&t=171s',
                       'markdown': '[00:02:51](https://www.youtube.com/watch?v=GZtF-I2M1ZE&t=171s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Lqlbag5CQMU',
                       'title': 'FCC 499 Filing is for Telecommunications Companies & Telecom and VoIP '
                                'Providers Information',
                       'channel': 'Legal Registration',
                       'author': 'Legal Registration',
                       'text': 'If you try operating a telecommunications company without a DC agent your '
                               'company can receive massive fines and penalties from the government.',
                       'tip': 'If you try operating a telecommunications company without a DC agent your '
                              'company can receive massive fines and penalties from the government.',
                       'timestamp': 21,
                       'timestamp_seconds': 21,
                       'timestamp_label': '[00:00:21]',
                       'url': 'https://www.youtube.com/watch?v=Lqlbag5CQMU&t=21s',
                       'markdown': '[00:00:21](https://www.youtube.com/watch?v=Lqlbag5CQMU&t=21s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'QPBt987oumw',
                       'title': 'FCC Releases Report on the Future of the Universal Service Fund',
                       'channel': 'ZCorum',
                       'author': 'ZCorum',
                       'text': "It's like four or five dollars now i think for usf fees.",
                       'tip': "It's like four or five dollars now i think for usf fees.",
                       'timestamp': 163,
                       'timestamp_seconds': 163,
                       'timestamp_label': '[00:02:43]',
                       'url': 'https://www.youtube.com/watch?v=QPBt987oumw&t=163s',
                       'markdown': '[00:02:43](https://www.youtube.com/watch?v=QPBt987oumw&t=163s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'EL34vsXYuGQ',
                       'title': "Consumers' Research v. FCC and the Legality of the Universal Service Fund "
                                'Contribution Regime',
                       'channel': 'The Federalist Society',
                       'author': 'The Federalist Society',
                       'text': 'This whole structure of usac is so lawless that it is it i find it deeply '
                               'troubling.',
                       'tip': 'This whole structure of usac is so lawless that it is it i find it deeply '
                              'troubling.',
                       'timestamp': 2343,
                       'timestamp_seconds': 2343,
                       'timestamp_label': '[00:39:03]',
                       'url': 'https://www.youtube.com/watch?v=EL34vsXYuGQ&t=2343s',
                       'markdown': '[00:39:03](https://www.youtube.com/watch?v=EL34vsXYuGQ&t=2343s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'yh-FMlChr9U',
                       'title': 'Appeals court voids 9 billion dollar FCC telecom fund',
                       'channel': 'LATEST NEWS UPDATE',
                       'author': 'LATEST NEWS UPDATE',
                       'text': 'In plain English, the court says the FCC built a corporate middleman it '
                               'had no legal right to build.',
                       'tip': 'In plain English, the court says the FCC built a corporate middleman it had '
                              'no legal right to build.',
                       'timestamp': 62,
                       'timestamp_seconds': 62,
                       'timestamp_label': '[00:01:02]',
                       'url': 'https://www.youtube.com/watch?v=yh-FMlChr9U&t=62s',
                       'markdown': '[00:01:02](https://www.youtube.com/watch?v=yh-FMlChr9U&t=62s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'vH9VQq2V9Qw',
                       'title': 'WI Telecom AQS Section 3 Non USF and USF Assessments',
                       'channel': 'Public Service Commission of Wisconsin',
                       'author': 'Public Service Commission of Wisconsin',
                       'text': 'Point out that the system subtracts uncollectibles from your gross '
                               "revenues so don't enter a negative number enter a positive number the "
                               'amount of revenues that were uncollectible.',
                       'tip': 'Point out that the system subtracts uncollectibles from your gross revenues '
                              "so don't enter a negative number enter a positive number the amount of "
                              'revenues that were uncollectible.',
                       'timestamp': 341,
                       'timestamp_seconds': 341,
                       'timestamp_label': '[00:05:41]',
                       'url': 'https://www.youtube.com/watch?v=vH9VQq2V9Qw&t=341s',
                       'markdown': '[00:05:41](https://www.youtube.com/watch?v=vH9VQq2V9Qw&t=341s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'}]}
