from __future__ import annotations

CHAPTER_5 = {'id': 'Q5',
 'chapter_id': 'Q5',
 'chapter_number': 5,
 'question_number': 5,
 'slug': 'working-the-ace-portal-reports-corrections-ach-refunds',
 'question_prompt': 'How do I set up and use the ACE portal to pull duty reports, file corrections, and '
                    'receive refunds by ACH?',
 'kicker': 'Q5 / THE BIG MONEY PLAYBOOKS',
 'title': 'Working the ACE Portal: Reports, Corrections and ACH Refunds',
 'subtitle': 'ACE Secure Data Portal account setup and approval timelines, ES-001/ES-003 and IEEPA duty '
             'reports, splitting duty bills by product from entry summaries, post summary corrections in '
             'ACE, eManifest, the February 6, 2026 ACH-only refund deadline, and the CAPE refund portal '
             'launch',
 'layout_template': 'case_study',
 'reading_time_minutes': 15,
 'executive_summary': 'Practitioners working the ACE portal converge on one hard rule: since February 6, '
                      '2026, CBP refunds only move by ACH to bank details registered in the portal, and '
                      'paying duty by ACH or periodic monthly statement does not register you. Scarbrough '
                      'Global, TEU Global and Ask The Customs Manager walk the setup: apply with company '
                      'and IOR data, unlock the account with the shared secret, then add routing and '
                      'account numbers or route funds through a 4811 or notify party. The street mechanics '
                      'center on Web Intelligence queries plus ES-001 and ES-003 line-tariff pulls '
                      'covering 2025 forward, which flag IEEPA lines and liquidation dates against the '
                      '180-day protest clock. Speakers split on refund speed (about 3 business days versus '
                      '60-90 days under CAPE) and on tariff scale ($200B+ versus $166B).',
 'key_metrics': [{'label': 'Electronic-only refund start date',
                  'metric': 'Electronic-only refund start date',
                  'value': 'February 6, 2026',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Date CBP stopped paper refund checks for all refund types; waivers described '
                             'as rare.',
                  'source': 'Ask The Customs Manager ([NRCd8c6t8rY @ 00:00:00])'},
                 {'label': 'CF28 response window',
                  'metric': 'CF28 response window',
                  'value': '30 days, as little as 5 left after a 3-week mail delay',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Misrouted CF28 letters burn the window; non-response leads to a CF29 rate '
                             'advance.',
                  'source': 'Scarbrough Global ([P1YIRCE3BPQ @ 00:05:32])'},
                 {'label': 'Forgotten credit authorization penalty',
                  'metric': 'Forgotten credit authorization penalty',
                  'value': '$1,000 per entry',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Importers paying CBP direct by credit forget to authorize; about a dozen are '
                             'penalized yearly.',
                  'source': 'Scarbrough Global ([P1YIRCE3BPQ @ 00:28:53])'},
                 {'label': 'Protest deadline tracked from liquidation date',
                  'metric': 'Protest deadline tracked from liquidation date',
                  'value': '180 days',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Liquidation date column in the IEEPA report is used to track the protest '
                             'deadline.',
                  'source': 'BGI Worldwide Logistics, Inc. ([zVrENO4RtLw @ 00:02:26])'}],
 'sections': [{'number': 1,
               'heading': 'The Practitioner Consensus',
               'paragraphs': ['Every Scarbrough Global speaker treats an ACE portal account as table '
                              'stakes, not an upgrade. The firm\'s explainer says it will "always '
                              'encourage" signup regardless of company size, because the portal acts as a '
                              'central hub across every broker you use and stores an electronic 7501 for '
                              'each entry [GuV2m_XHyd0 @ 00:04:08]. In the Wichita transition session the '
                              'pitch was blunter: "Why wouldn\'t you want the same information that '
                              'customs has," with setup described as a five-minute job involving roughly '
                              'three-quarters of a page of real input [ZzvKR65Oyuw @ 00:04:45]. That same '
                              'session found only 7 of about 50 attendees already held accounts, and the '
                              'recommended order is import application first, exporter second, with no '
                              'officer required on the file [ZzvKR65Oyuw @ 00:02:04]. Turnaround is fast '
                              'when the paperwork is clean: the most recent application Scarbrough pushed '
                              'through came back from CBP in less than a week, followed by an emailed '
                              'username and a password-retrieval link [LqV0KsoyRVw @ 00:00:00]. The '
                              'operator takeaway is that portal access costs almost nothing in time, while '
                              "running blind means relying entirely on each broker's version of your "
                              'import history, entry counts, and liquidation dates when refunds, rate '
                              'advances, or CF28 requests eventually land on your desk.',
                              'The second point of full agreement is that refunds now move by ACH or not '
                              'at all. Ask The Customs Manager pegs February 6, 2026 as the date CBP went '
                              'electronic-only for every refund type, warning that waivers are "rare" '
                              "[NRCd8c6t8rY @ 00:00:00]. Scarbrough Global's Adam Hill puts it in plainer "
                              'money terms: "If you are not set up on the ACE portal with your bank '
                              'information set up to receive that via AC, you won\'t get your money," and '
                              'the panel confirms PSC and protest refunds now land only in '
                              'portal-registered bank accounts [P1YIRCE3BPQ @ 00:01:03]. The same panel '
                              'calls the belief that paying duty through ACH or a periodic monthly '
                              'statement already registers you for refunds the "biggest myth" in the '
                              'market; payment-side enrollment and refund-side bank details are separate '
                              'setups [P1YIRCE3BPQ @ 00:10:34]. Ask The Customs Manager reduces the job to '
                              'three steps: enroll, verify the bank information, and confirm the broker is '
                              'ACH-ready, adding that the importer carries the full accuracy risk because '
                              'CBP "won\'t chase you down" [2H7zdtUvSDA @ 00:01:41]. Across all three '
                              'sources the operating baseline is identical: the portal account comes '
                              'first, the bank record second, and the broker readiness check third.',
                              'Practitioners also agree the portal is a surveillance tool you point at '
                              'yourself. In the Shapiro workshop, Patricia frames ACE reports as part of a '
                              'compliance routine, noting the data refreshes nightly and can expose '
                              'unauthorized filers, with the AM100 courtesy notice of liquidation and the '
                              "CF28/29 reports run weekly [605kfE-oUPM @ 00:12:23]. Scarbrough Global's "
                              'panel makes the same case from the brokerage side: watch for forgotten '
                              'powers of attorney and fraud under your EIN, and reconcile your own entry '
                              'counts against what CBP shows, down to a figure like 297 entries, so any '
                              'mismatch with broker records surfaces early [P1YIRCE3BPQ @ 00:07:14]. Adam '
                              'Hill\'s cadence is "I think you should be in weekly," running liquidation '
                              'reports on each visit and logging in at least monthly, because roughly 30 '
                              'days of inactivity forces a password reset that is best handled by phoning '
                              'the help desk rather than emailing it [P1YIRCE3BPQ @ 00:09:15]. Both camps '
                              "push CF28 and CF29 traffic into the portal as well: Shapiro's walkthrough "
                              'shows the mode of communication defaulting to mail and needing a manual '
                              'switch to portal, with full access required to respond [605kfE-oUPM @ '
                              '00:31:38]. The consensus is cadence over cleverness: weekly pulls, portal '
                              'delivery, and relentless self-reconciliation.'],
               'table': {'caption': 'Where the ACE portal practitioners line up',
                         'headers': ['Consensus Point',
                                     'What Practitioners Agree On',
                                     'Operator Implication',
                                     'Expert Source'],
                         'rows': [['Portal signup regardless of company size',
                                   'Central hub across all brokers that holds an electronic 7501 per entry',
                                   'Open the account before refunds or CF28 letters start arriving',
                                   'Scarbrough Global ([GuV2m_XHyd0 @ 00:04:08])'],
                                  ['Application turnaround is short when clean',
                                   'Most recent application came back from CBP in less than a week',
                                   'Apply now because the emailed password link expires if ignored',
                                   'Scarbrough Global ([LqV0KsoyRVw @ 00:00:00])'],
                                  ['Refunds are electronic-only from February 6, 2026',
                                   'Every refund type moved to ACH with waivers described as rare',
                                   'Missing portal bank data means the refund simply does not arrive',
                                   'Ask The Customs Manager ([NRCd8c6t8rY @ 00:00:00])'],
                                  ['Paying by ACH is not refund registration',
                                   'ACH or periodic monthly statement payment does not register refund '
                                   'bank details',
                                   'Add refund bank info separately even if already paying CBP '
                                   'electronically',
                                   'Scarbrough Global ([P1YIRCE3BPQ @ 00:10:34])'],
                                  ['Three-step ACH readiness routine for importers',
                                   'Enroll, verify bank information, then confirm the broker is ACH-ready',
                                   "A wrong account number is the importer's problem, not CBP's",
                                   'Ask The Customs Manager ([2H7zdtUvSDA @ 00:01:41])'],
                                  ['Weekly report cadence as a compliance habit',
                                   'Run AM100 liquidation notices and CF28/29 reports weekly on '
                                   'nightly-refreshed data',
                                   'Unauthorized filers and liquidations surface before deadlines quietly '
                                   'pass',
                                   'Shapiro ([605kfE-oUPM @ 00:12:23])'],
                                  ['CF28 and CF29 delivery switched to portal',
                                   'Mode of communication defaults to mail and must be changed manually',
                                   'Portal delivery protects the 30-day response window from mail delays',
                                   'Shapiro ([605kfE-oUPM @ 00:31:38])']]}},
              {'number': 2,
               'heading': 'Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['The account build is mechanical once you know where first-timers stall. The '
                              'Shapiro workshop walks the full application: Section A covers company, '
                              'fiscal year end, officer, date of birth and activity type, with a primary '
                              'activity chosen if you tick several; Section B names the account owner, '
                              'split between individuals and legal entities; Section C sets the point of '
                              'contact; Section D collects e-signatures [605kfE-oUPM @ 00:00:41]. Approval '
                              'triggers two emails, a temporary-password link and a shared secret, and '
                              'Scarbrough Global names the snag that stops most operators cold: "the very '
                              'first time your shared secret is your user id," meaning the username '
                              'customs emailed, and that link expires, so sitting on it means starting '
                              'over [LqV0KsoyRVw @ 00:00:58]. Passwords need at least 12 characters mixing '
                              'upper case, lower case, numeric and special characters, and they expire '
                              'every 45 days [605kfE-oUPM @ 00:03:52]. Three failed attempts lock the '
                              'account; a locked-out TAO calls the ACE helpdesk with the shared secret, '
                              'and only a TAO or proxy TAO can create users, whose IDs belong to '
                              'individuals rather than the company, with read-only or full access set per '
                              'function [605kfE-oUPM @ 00:05:23]. Give whoever answers CF28s full access, '
                              'because responding requires it.',
                              "The bank step is short but unforgiving. TEU Global's sequence inside the "
                              'portal is Get Info/Refresh on the account screen, then Add ACH info with '
                              'routing and account numbers, then submit, all done after a signup that '
                              'pulls company data from the 5106 already on file with CBP [lKk16DmiedE @ '
                              '00:01:52]. Importers without a US bank account add a notify party instead, '
                              'picking "one of the type 10, 20, 23, and 34" and entering that party\'s IR '
                              'number, a setup TEU offers as a service [lKk16DmiedE @ 00:02:28]. '
                              'Scarbrough Global reaches the same destination through a different form: a '
                              '4811 routes refunds to a third party, and because foreign bank accounts '
                              'cannot receive the deposit, the 4811 is the standard fix for overseas '
                              'importers of record who still want their money [P1YIRCE3BPQ @ 00:21:48]. '
                              'Precision matters because nobody downstream will rescue a typo. Ask The '
                              'Customs Manager warns that a wrong account number sends the refund "into '
                              'the void" for months before anyone untangles it [NRCd8c6t8rY @ 00:02:13]. '
                              'Treat routing and account entry as a two-person check, and re-verify the '
                              'record before any large PSC or protest refund comes due, since the importer '
                              'alone owns that error under the new regime.',
                              'The refund hunt runs on reports. BGI Worldwide Logistics builds a custom '
                              'pull in three minutes: Accounts, Importer, the account name, then Reports '
                              'to open the BI Launchpad, Web Intelligence with defaults, the Entry Summary '
                              'universe, Entry Summary Date filtered greater than January 1, 2025, plus '
                              'HTS Number Full, Liquidation Status and Liquidation Date, then Run and '
                              'export to Excel; the HTS column flags IEEPA lines and the liquidation date '
                              'drives the 180-day protest deadline [zVrENO4RtLw @ 00:01:42]. Harry F. '
                              'Long, Inc. skips the query builder and uses public reports under Reports, '
                              'Folders, Public, ACE, Trade, Importer, Entry Summary: ES001 with a February '
                              '1, 2025 begin date and a February 23, 2026 end date, when the IEEPA tariffs '
                              'ended, then ES003 line tariff on the same parameters for full HTS at line '
                              'level [bD2cV_iBUpU @ 00:00:52]. SKUio accepts a single 7501 PDF or an ACE '
                              'ES-003 report for bulk import, processed as a background job that takes '
                              "seconds [WLDwLas6IOI @ 00:01:00]. Scarbrough Global's brokers take the same "
                              'ES-003 file and return a dashboard of spend by IEEPA, 232 and 301 tariffs, '
                              'so the client sees exactly where the tariff dollars went before deciding '
                              'which entries to chase with a PSC or protest [P1YIRCE3BPQ @ 00:08:20].'],
               'table': {'caption': 'ACE portal paths, reports and settings practitioners actually click',
                         'headers': ['Tool or Report',
                                     'Exact Path or Setting',
                                     'Numbers and Outputs',
                                     'Expert Source'],
                         'rows': [['BI Launchpad Web Intelligence custom IEEPA query',
                                   'Accounts, Importer, account name, Reports, Entry Summary universe',
                                   'Entry Summary Date filtered after January 1, 2025, exported to Excel',
                                   'BGI Worldwide Logistics, Inc. ([zVrENO4RtLw @ 00:01:19])'],
                                  ['ES001 entry summary public report',
                                   'Reports, Folders, Public, ACE, Trade, Importer, Entry Summary',
                                   'Begin February 1, 2025, end February 23, 2026, IOR optional',
                                   'Harry F. Long, Inc. - U.S. Customs Brokers ([bD2cV_iBUpU @ 00:00:52])'],
                                  ['ES003 line tariff report for IEEPA lines',
                                   'Same parameters as ES001, run, then export to Excel',
                                   'Line-level full HTS identifies entries hit by IEEPA duties',
                                   'Harry F. Long, Inc. - U.S. Customs Brokers ([bD2cV_iBUpU @ 00:02:24])'],
                                  ['SKUio customs entries import and duty split',
                                   'Settings, Purchasing, Duty Rates, then the Customs entries tab',
                                   'Single 7501 PDF or bulk ES-003 report, job finishes in seconds',
                                   'SKUio ([WLDwLas6IOI @ 00:00:02])'],
                                  ['Scheduled ACE report delivery by email',
                                   'Save As to Favorites before modifying, then set the schedule',
                                   'Weekly or monthly, Excel or PDF, unlimited email recipients allowed',
                                   'Shapiro ([605kfE-oUPM @ 00:22:48])'],
                                  ['ACH refund bank record inside the portal',
                                   'Get Info/Refresh, then Add ACH info, then submit',
                                   'Routing and account numbers; no US bank uses a notify party',
                                   'TEU Global ([lKk16DmiedE @ 00:01:52])'],
                                  ['AD/CVD non-reimbursement statement filing',
                                   'Accounts, Importer, Declarations, Create, then attach and submit',
                                   'Up to 50 HTS numbers; confirmation number issued on submission',
                                   'Shapiro ([605kfE-oUPM @ 00:09:14])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Moves the Brokers Actually Use',
                           'body': 'Small portal settings decide whether a refund, a CF28 answer, or a '
                                   'report lands on time. These are the shortcuts the brokers and software '
                                   'vendors lean on.',
                           'items': ['Use Save As to park a standard report in Favorites before editing '
                                     'it, then drag in the PSC indicator so post-summary corrections show '
                                     'up in the same pull [Shapiro — 605kfE-oUPM @ 00:20:16].',
                                     'When AES filing gets clunky after migration, look up an old ITN and '
                                     'save it as a template instead of rekeying every filing [Scarbrough '
                                     'Global — ZzvKR65Oyuw @ 00:09:17].',
                                     'Select portal plus mail delivery for CF28s; a three-week mail delay '
                                     'leaves only five days of the 30-day window to answer [Scarbrough '
                                     'Global — P1YIRCE3BPQ @ 00:05:32].',
                                     'Read the SKUio Checks card before applying anything: a customs value '
                                     'below PO value is a cue to verify with the broker, and code '
                                     'mismatches stay unticked until Apply selected [SKUio — WLDwLas6IOI @ '
                                     '00:01:38].']},
               'sop_steps': [{'step': 1,
                              'title': 'Open and unlock the portal account',
                              'action': 'Submit the importer application first, then the exporter '
                                        'application if needed.',
                              'detail': 'On first login enter the user ID customs emailed as the shared '
                                        'secret, and act before the emailed password link expires '
                                        '[Scarbrough Global — LqV0KsoyRVw @ 00:00:58].'},
                             {'step': 2,
                              'title': 'Register refund bank data',
                              'action': 'Run Get Info/Refresh, add ACH routing and account numbers, then '
                                        'submit.',
                              'detail': 'Importers with no US bank add a notify party of type 10, 20, 23 '
                                        "or 34 with that party's IR number [TEU Global — lKk16DmiedE @ "
                                        '00:02:28].'},
                             {'step': 3,
                              'title': 'Pull the IEEPA exposure report',
                              'action': 'Build the Entry Summary query with HTS Number Full, Liquidation '
                                        'Status and Liquidation Date.',
                              'detail': 'Filter Entry Summary Date after January 1, 2025, export to Excel, '
                                        'and use the liquidation date to track the 180-day protest '
                                        'deadline [BGI Worldwide Logistics, Inc. — zVrENO4RtLw @ '
                                        '00:02:26].'},
                             {'step': 4,
                              'title': 'Lock in the weekly monitoring loop',
                              'action': 'Schedule AM100 and CF28/29 reports and switch CF28/29 delivery to '
                                        'portal.',
                              'detail': 'Schedule reports weekly or monthly in Excel or PDF to unlimited '
                                        'email recipients so liquidations and RFIs never slip [Shapiro — '
                                        '605kfE-oUPM @ 00:22:48].'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['Refund velocity is where the loudest numbers collide. Ask The Customs '
                              'Manager tells importers that once ACH enrollment is live, funds land in '
                              'roughly three business days, that waivers back to paper are rare, and that '
                              'the February 6, 2026 electronic-only cutover covers every refund type '
                              '[NRCd8c6t8rY @ 00:01:27]. NextGen CPA runs a far slower clock on the IEEPA '
                              'side: CAPE, launched April 20, 2026, is the sole route for those refunds, '
                              'pays by ACH only, and the operator budgets 60 to 90 days to payment, with a '
                              'missed 7501 forcing a brand-new declaration that drops the claim to the '
                              "back of the queue [sMBX0ZlgJRY @ 00:01:10]. CBC News reported the agency's "
                              'own build timeline, a refund system due in about 45 days around mid-April, '
                              'after the trade court ordered refunds with interest and then suspended that '
                              'order, with an appeal still possible [qVk8ygNZbS8 @ 00:01:03]. Even the '
                              'size of the pot splits: Ask The Customs Manager cites more than $200 '
                              'billion in tariffs collected since January 2025, while the CBP figure '
                              'quoted by CBC is $166 billion across 330,000-plus importers, requiring 4.4 '
                              'million man-hours to process [qVk8ygNZbS8 @ 00:00:45]. The working read is '
                              'that three days describes deposit speed once a refund is released, while 60 '
                              'to 90 days describes the CAPE queue itself.',
                              'The correction-versus-protest split is the sharpest tactical fork. '
                              "Scarbrough Global's brokerage team argues that the post summary correction, "
                              'which replaced the paper post-entry amendment, still drags because CBP '
                              'carries no regulatory burden to answer it; if Customs does nothing, the '
                              'entry simply liquidates on schedule, whereas a protest by law has to be '
                              'answered [FcsTuxrd4SM @ 00:00:19]. Their counterweight is proof of receipt: '
                              'in the PEA world, half the time they could not even prove CBP had the '
                              'filing, while a PSC at least shows it landed, even though staff turnover '
                              "means constant follow-up and replies like 'we'll get to it when we get to "
                              "it.' NextGen CPA's playbook is blunter: file PSCs or protests on every "
                              'entry, watch the Section 122 150-day expiry on July 24, expect a Section '
                              "301 'wave three' in August, and budget a 10 to 15 percent duty buffer "
                              '[sMBX0ZlgJRY @ 00:02:24]. BGI Worldwide Logistics builds the protest path '
                              'around the clock, pulling liquidation date into every IEEPA report '
                              'specifically to track the 180-day protest deadline [zVrENO4RtLw @ '
                              "00:02:26]. Access splits the field too: Scarbrough's ACE forum stresses "
                              'that an importer cannot file a PSC without an ABI connection, though the '
                              'PSC filer does not have to be the same party that filed the entry '
                              '[52Q7Sv1KF4Q @ 00:14:18].',
                              'Four shops pull the same refund data four different ways. Harry F. Long '
                              'walks the canned route: Reports, Folders, Public, ACE, Trade, Importer, '
                              'Entry Summary, then ES001 for header-level liquidation status and date, '
                              'followed by ES003 for line-level full HTS, run on a February 1, 2025 to '
                              'February 23, 2026 window because the IEEPA tariffs ended on February 23, '
                              '2026 [bD2cV_iBUpU @ 00:02:24]. BGI Worldwide Logistics skips the canned '
                              'folders entirely and builds a custom Web Intelligence query in the BI '
                              'Launchpad on the Entry Summary universe, filtered to entry summary dates '
                              'after January 1, 2025, adding HTS Number Full, Liquidation Status and '
                              'Liquidation Date, then saving it to Personal Folders for reuse [zVrENO4RtLw '
                              '@ 00:01:19]. SKUio pushes either a single 7501 PDF or a bulk ES-003 export '
                              'into its software as a background job, where a blue banner totals possibly '
                              'refundable IEEPA duty and an export worksheet feeds the refund claim line '
                              "by line [WLDwLas6IOI @ 00:01:00]. Scarbrough Global's model hands the "
                              'ES-003 straight to the broker, who returns a dashboard of spend by tariff '
                              'across IEEPA, 232 and 301 [P1YIRCE3BPQ @ 00:08:20]. The tradeoff is control '
                              'versus speed: the canned ES reports need only a trade account ID and two '
                              'dates, while the custom query lets the operator choose exactly which '
                              'columns land in Excel.'],
               'table': {'caption': 'Competing ACE refund and correction playbooks, side by side',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['How fast refund money actually reaches the importer',
                                   'ACH deposits arrive in about three business days once enrolled',
                                   'CAPE IEEPA refunds pay by ACH only in 60 to 90 days',
                                   'Ask The Customs Manager ([NRCd8c6t8rY @ 00:01:27]); NextGen CPA '
                                   '([sMBX0ZlgJRY @ 00:01:10])'],
                                  ['How big the tariff refund pot really is',
                                   'More than $200 billion in tariffs collected since January 2025',
                                   'CBP cites $166 billion across more than 330,000 importers',
                                   'Ask The Customs Manager ([NRCd8c6t8rY @ 00:02:55]); CBC News '
                                   '([qVk8ygNZbS8 @ 00:00:45])'],
                                  ['Which correction vehicle to lean on for recovery',
                                   'PSC proves receipt, but CBP has no duty to answer it',
                                   'File PSCs or protests on every single entry before deadlines hit',
                                   'Scarbrough Global ([FcsTuxrd4SM @ 00:00:37]); NextGen CPA '
                                   '([sMBX0ZlgJRY @ 00:02:24])'],
                                  ['How to pull IEEPA entry data out of ACE',
                                   'Run canned ES001 and ES003 from Public ACE Trade folders',
                                   'Build a custom Web Intelligence query on the Entry Summary universe',
                                   'Harry F. Long, Inc. - U.S. Customs Brokers ([bD2cV_iBUpU @ 00:00:24]); '
                                   'BGI Worldwide Logistics, Inc. ([zVrENO4RtLw @ 00:01:19])'],
                                  ['Who turns the ES-003 export into usable analysis',
                                   'Import ES-003 into SKU.io and prorate duty bills by product',
                                   'Hand ES-003 to the broker for a spend-by-tariff dashboard',
                                   'SKUio ([WLDwLas6IOI @ 00:01:00]); Scarbrough Global ([P1YIRCE3BPQ @ '
                                   '00:08:20])'],
                                  ['Routing refunds when the importer has no US bank',
                                   'Add a notify party type 10, 20, 23 or 34 with IR number',
                                   'File a 4811 so refunds route to a designated third party',
                                   'TEU Global ([lKk16DmiedE @ 00:02:28]); Scarbrough Global ([P1YIRCE3BPQ '
                                   '@ 00:21:48])'],
                                  ['How long getting an ACE portal account really takes',
                                   'Setup takes five minutes with about three-quarters of a page of input',
                                   'Applications get human review, so apply early before a backlog builds',
                                   'Scarbrough Global ([ZzvKR65Oyuw @ 00:02:24]); Scarbrough Global '
                                   '([52Q7Sv1KF4Q @ 00:12:28])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The most expensive trap is assuming money flows back the same way it flows '
                              'out. Scarbrough Global calls it the biggest myth: paying duty by ACH or '
                              'periodic monthly statement does not register an importer to receive '
                              'refunds, which now go only to bank information loaded in the ACE portal, '
                              'and the team watched a refund check north of $2 million get mailed to a '
                              'single client under the old paper regime [P1YIRCE3BPQ @ 00:10:34]. Ask The '
                              'Customs Manager warns that a mistyped account number sends the refund into '
                              "the void for months [NRCd8c6t8rY @ 00:02:13], and the same channel's "
                              'companion briefing is blunter about liability: the importer owns accuracy, '
                              "CBP won't chase you down, and if you put the wrong bank account, that's on "
                              'you [2H7zdtUvSDA @ 00:02:33]. Foreign-banked importers hit a separate wall '
                              'because foreign accounts cannot receive deposits at all. Scarbrough routes '
                              "those refunds to a third party through a 4811, while TEU Global's fix is "
                              "adding a notify party of type 10, 20, 23 or 34 with that party's IR number, "
                              'a service TEU sells directly [lKk16DmiedE @ 00:02:28]. There is an '
                              'asymmetry to budget for as well: refunds deposit electronically, but '
                              'additional duties owed on a PSC still arrive as paper bills, so the inbound '
                              'and outbound cash paths do not mirror each other.',
                              'Mail-routed requests for information quietly destroy landed cost. '
                              "Scarbrough Global's brokerage team reports CF28 letters getting misrouted "
                              'in the mail; the response window is 30 days, so a letter that spends three '
                              'weeks in transit leaves roughly five days to answer, and silence triggers a '
                              "CF29 rate advance [P1YIRCE3BPQ @ 00:05:32]. Shapiro's workshop confirms "
                              'that the mode of communication defaults to mail and shows the toggle to '
                              'portal, with the catch that responding requires full access rather than '
                              'read-only, and status moves from sent to closed [605kfE-oUPM @ 00:31:38]. '
                              'The Section 232 derivative wave raised the stakes further: CF28s now demand '
                              'smelt-and-cast proof behind claimed steel content, such as a 30 percent '
                              'claim, with one request carrying 12 separate data points and others asking '
                              'for bills of materials and proprietary data [P1YIRCE3BPQ @ 00:13:25]. The '
                              'firsthand lesson is to over-provide on the first 28s, because a CF29 '
                              'landing three months later breaks the landed cost the importer has been '
                              "running on. Scarbrough's portal-transition session adds that decentralized "
                              'firms in particular should push CF28 and CF29 traffic into the portal so '
                              'the request reaches whoever actually owns the entry instead of sitting in a '
                              'mailroom [ZzvKR65Oyuw @ 00:05:53].',
                              "Credential decay and payment terms are the slow bleeds. Shapiro's workshop "
                              'lays out the rules: passwords of at least 12 characters mixing upper, '
                              'lower, numeric and special characters, expiring every 45 days, with three '
                              'failed attempts locking the account, after which a locked-out TAO calls the '
                              'ACE helpdesk armed with the shared secret [605kfE-oUPM @ 00:05:23]. '
                              'Scarbrough Global flags the first-login sticking point: the very first '
                              'time, the shared secret is the user ID Customs emailed, and the password '
                              'link expires, possibly in about a week, so waiting means repeating the '
                              "whole process [LqV0KsoyRVw @ 00:00:58]. On cash, Scarbrough's panel reports "
                              "client duty runs about ten times the broker's revenue, pushing broker "
                              'credit exposure from $70 to $90,000 per customer and shrinking terms to '
                              'roughly five days, while PMS pays on the 15th business day of the following '
                              'month, giving float stretching from the 20s into the 50s of days '
                              '[P1YIRCE3BPQ @ 00:24:13]. Importers paying CBP direct should choose debit, '
                              "not credit: credit users forget to authorize, it's a $1,000 per entry "
                              'penalty, about a dozen credit importers get hit every year, and a duty-only '
                              'bank account is the clean workaround [P1YIRCE3BPQ @ 00:27:55]. The same '
                              'panel predicts mandatory direct payment within five years.'],
               'table': {'caption': 'Firsthand ACE refund and correction traps with operator fixes',
                         'headers': ['Trap', 'Firsthand Mechanism', 'Operator Fix', 'Expert Source'],
                         'rows': [['Assuming ACH duty payment already enrolls refund deposits',
                                   'Paying by ACH or PMS never registers bank info for refunds',
                                   'Sign up, then add bank information in the portal as step two',
                                   'Scarbrough Global ([P1YIRCE3BPQ @ 00:10:34]); Scarbrough Global '
                                   '([P1YIRCE3BPQ @ 00:30:28])'],
                                  ['Typing the wrong routing or account number into ACE',
                                   'Refund disappears into the void for months and the importer owns it',
                                   'Enroll, verify bank information, then confirm the broker is ACH-ready',
                                   'Ask The Customs Manager ([NRCd8c6t8rY @ 00:02:13]); Ask The Customs '
                                   'Manager ([2H7zdtUvSDA @ 00:01:41])'],
                                  ['Leaving CF28 delivery on the default mail setting',
                                   'Three weeks in the mail leaves five days of a 30-day window',
                                   'Switch mode of communication to portal, ideally portal plus mail',
                                   'Scarbrough Global ([P1YIRCE3BPQ @ 00:04:24]); Shapiro ([605kfE-oUPM @ '
                                   '00:31:38])'],
                                  ['Paying CBP direct on credit and forgetting to authorize',
                                   'A $1,000 per entry penalty hits about a dozen importers yearly',
                                   'Choose debit over credit and consider a duty-only bank account',
                                   'Scarbrough Global ([P1YIRCE3BPQ @ 00:28:53])'],
                                  ['Missing a 7501 when declaring in CAPE',
                                   'No amendments allowed, so a new declaration goes to the back',
                                   'Pull ES003 line-level HTS for the full IEEPA window before declaring',
                                   'NextGen CPA ([sMBX0ZlgJRY @ 00:01:10]); Harry F. Long, Inc. - U.S. '
                                   'Customs Brokers ([bD2cV_iBUpU @ 00:03:28])'],
                                  ['Letting the ACE login go stale between sessions',
                                   'About 30 days idle forces a reset; three failed attempts lock you out',
                                   'Log in weekly, run liquidation reports, and phone the help desk',
                                   'Scarbrough Global ([P1YIRCE3BPQ @ 00:09:15]); Shapiro ([605kfE-oUPM @ '
                                   '00:05:23])'],
                                  ['Ignoring entries filed by other parties under your numbers',
                                   'Forgotten POAs and fraud under your EIN go unnoticed in the data',
                                   'Add importer numbers first and reconcile entry counts against records',
                                   'SKUio ([WLDwLas6IOI @ 00:00:43]); Scarbrough Global ([P1YIRCE3BPQ @ '
                                   '00:07:14])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Four checks before counting on an ACE refund',
                           'body': 'Every item below is a failure practitioners watched happen to real '
                                   'importers; clear all four before treating any refund as cash in hand.',
                           'items': ['Bank information is loaded in the ACE portal itself, not merely '
                                     'implied by paying duty via ACH or periodic monthly statement '
                                     '[Scarbrough Global — P1YIRCE3BPQ @ 00:10:34].',
                                     'Routing and account numbers are double-checked, because a wrong '
                                     "account sends the refund into the void for months and CBP won't "
                                     'chase you down [Ask The Customs Manager — NRCd8c6t8rY @ 00:02:13].',
                                     'CF28 and CF29 delivery is switched from mail to portal so a 30-day '
                                     'window is not burned in transit [Scarbrough Global — P1YIRCE3BPQ @ '
                                     '00:05:32].',
                                     'Every IEEPA-hit 7501 is captured before declaring in CAPE, since a '
                                     'missed entry means a new declaration at the back of the queue '
                                     '[NextGen CPA — sMBX0ZlgJRY @ 00:01:10].']}}],
 'pull_quote': '"If you are not set up on the ACE portal with your bank information set up to receive that '
               'via AC, you won\'t get your money." — Scarbrough Global (P1YIRCE3BPQ @ 00:01:03).',
 'diagram_id': 'diag-05',
 'action_checklist': ['Apply for the ACE portal account now, filing the import application first and the '
                      'exporter application second, because applications get human review and a backlog '
                      'builds [Scarbrough Global — ZzvKR65Oyuw @ 00:02:42].',
                      'On first login, enter your emailed user ID as the shared secret and activate before '
                      'the password link expires [Scarbrough Global — LqV0KsoyRVw @ 00:00:58].',
                      'Load refund banking via Get Info/Refresh, then Add ACH info with routing and '
                      'account numbers, then submit [TEU Global — lKk16DmiedE @ 00:01:52].',
                      'Run the three-step ACH routine: enroll, verify bank information, and confirm your '
                      'broker is ACH-ready [Ask The Customs Manager — 2H7zdtUvSDA @ 00:01:41].',
                      'Pull ES001 and ES003 for February 1, 2025 through February 23, 2026, export to '
                      'Excel, and flag liquidation dates against the 180-day protest deadline [Harry F. '
                      'Long, Inc. - U.S. Customs Brokers — bD2cV_iBUpU @ 00:00:52].',
                      'Switch CF28/CF29 delivery to portal and schedule the AM100 courtesy notice of '
                      'liquidation to run weekly [Shapiro — 605kfE-oUPM @ 00:16:06].'],
 'statutory_citations': [{'title': "Scarbrough Global — Freight Expectations: CBP's ACE Portal [00:01:03]",
                          'url': 'https://www.youtube.com/watch?v=P1YIRCE3BPQ&t=63s',
                          'relevance': 'Primary practitioner testimony on portal-only ACH refunds, the '
                                       'ACH-payment enrollment myth, CF28 mail risk and credit-payment '
                                       'penalties.'},
                         {'title': 'Scarbrough Global — Post Summary Correction in ACE [00:00:19]',
                          'url': 'https://www.youtube.com/watch?v=FcsTuxrd4SM&t=19s',
                          'relevance': 'Primary practitioner testimony on why PSCs stall while protests '
                                       'require a CBP response.'},
                         {'title': 'BGI Worldwide Logistics, Inc. — Unlock Duty Refunds: ACE IEEPA Report '
                                   'in 3 Minutes! [00:02:26]',
                          'url': 'https://www.youtube.com/watch?v=zVrENO4RtLw&t=146s',
                          'relevance': 'Primary practitioner testimony on building the IEEPA refund report '
                                       'and tracking the 180-day protest deadline.'},
                         {'title': 'Ask The Customs Manager — CBP ACH Refund Deadline 2026: Importers Must '
                                   'Enroll by February 6 or Lose Tariff Refunds [00:00:00]',
                          'url': 'https://www.youtube.com/watch?v=NRCd8c6t8rY&t=0s',
                          'relevance': 'Primary practitioner testimony on the electronic-only refund '
                                       'cutover, deposit speed and wrong-account losses.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'GuV2m_XHyd0',
                       'title': 'What is CBP ACE Automated Commercial Environment?',
                       'channel': 'Scarbrough Global',
                       'author': 'Scarbrough Global',
                       'text': 'We always encourage signing up for the ACE portal regardless of size, '
                               'because it is a central hub across all brokers that holds an electronic '
                               '7501.',
                       'tip': 'We always encourage signing up for the ACE portal regardless of size, '
                              'because it is a central hub across all brokers that holds an electronic '
                              '7501.',
                       'timestamp': 248,
                       'timestamp_seconds': 248,
                       'timestamp_label': '[00:04:08]',
                       'url': 'https://www.youtube.com/watch?v=GuV2m_XHyd0&t=248s',
                       'markdown': '[00:04:08](https://www.youtube.com/watch?v=GuV2m_XHyd0&t=248s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'WLDwLas6IOI',
                       'title': 'Split a Customs Duty Bill by Product with CBP 7501 Entry Summaries | '
                                'SKU.io',
                       'channel': 'SKUio',
                       'author': 'SKUio',
                       'text': 'The blue banner totals the IEEPA duty you paid, which may be refundable.',
                       'tip': 'The blue banner totals the IEEPA duty you paid, which may be refundable.',
                       'timestamp': 23,
                       'timestamp_seconds': 23,
                       'timestamp_label': '[00:00:23]',
                       'url': 'https://www.youtube.com/watch?v=WLDwLas6IOI&t=23s',
                       'markdown': '[00:00:23](https://www.youtube.com/watch?v=WLDwLas6IOI&t=23s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '605kfE-oUPM',
                       'title': 'Automated Commercial Environment ACE Import Workshop',
                       'channel': 'Shapiro',
                       'author': 'Shapiro',
                       'text': 'Three failed attempts lock the account, and a locked-out TAO calls the ACE '
                               'helpdesk with the shared secret.',
                       'tip': 'Three failed attempts lock the account, and a locked-out TAO calls the ACE '
                              'helpdesk with the shared secret.',
                       'timestamp': 323,
                       'timestamp_seconds': 323,
                       'timestamp_label': '[00:05:23]',
                       'url': 'https://www.youtube.com/watch?v=605kfE-oUPM&t=323s',
                       'markdown': '[00:05:23](https://www.youtube.com/watch?v=605kfE-oUPM&t=323s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '52Q7Sv1KF4Q',
                       'title': 'ACE Question/Answer Forum: Session One Introduction',
                       'channel': 'Scarbrough Global',
                       'author': 'Scarbrough Global',
                       'text': 'Importers cannot file a post summary correction without an ABI connection, '
                               'and the PSC filer does not have to be the entry filer.',
                       'tip': 'Importers cannot file a post summary correction without an ABI connection, '
                              'and the PSC filer does not have to be the entry filer.',
                       'timestamp': 858,
                       'timestamp_seconds': 858,
                       'timestamp_label': '[00:14:18]',
                       'url': 'https://www.youtube.com/watch?v=52Q7Sv1KF4Q&t=858s',
                       'markdown': '[00:14:18](https://www.youtube.com/watch?v=52Q7Sv1KF4Q&t=858s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'bD2cV_iBUpU',
                       'title': 'ACE ES 001 and ES 003 Report',
                       'channel': 'Harry F. Long, Inc. - U.S. Customs Brokers',
                       'author': 'Harry F. Long, Inc. - U.S. Customs Brokers',
                       'text': 'The IEEPA tariffs ended on February 23rd, 2026.',
                       'tip': 'The IEEPA tariffs ended on February 23rd, 2026.',
                       'timestamp': 75,
                       'timestamp_seconds': 75,
                       'timestamp_label': '[00:01:15]',
                       'url': 'https://www.youtube.com/watch?v=bD2cV_iBUpU&t=75s',
                       'markdown': '[00:01:15](https://www.youtube.com/watch?v=bD2cV_iBUpU&t=75s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ZzvKR65Oyuw',
                       'title': 'ACE Portal Transition',
                       'channel': 'Scarbrough Global',
                       'author': 'Scarbrough Global',
                       'text': "Why wouldn't you want the same information that customs has.",
                       'tip': "Why wouldn't you want the same information that customs has.",
                       'timestamp': 285,
                       'timestamp_seconds': 285,
                       'timestamp_label': '[00:04:45]',
                       'url': 'https://www.youtube.com/watch?v=ZzvKR65Oyuw&t=285s',
                       'markdown': '[00:04:45](https://www.youtube.com/watch?v=ZzvKR65Oyuw&t=285s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'lKk16DmiedE',
                       'title': 'How to Set Up the CBP ACE Secure Data Portal & ACH Refunds | Step-by-Step '
                                'Guide for Importers',
                       'channel': 'TEU Global',
                       'author': 'TEU Global',
                       'text': 'You can choose one of the type 10, 20, 23, and 34.',
                       'tip': 'You can choose one of the type 10, 20, 23, and 34.',
                       'timestamp': 148,
                       'timestamp_seconds': 148,
                       'timestamp_label': '[00:02:28]',
                       'url': 'https://www.youtube.com/watch?v=lKk16DmiedE&t=148s',
                       'markdown': '[00:02:28](https://www.youtube.com/watch?v=lKk16DmiedE&t=148s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'NRCd8c6t8rY',
                       'title': 'CBP ACH Refund Deadline 2026: Importers Must Enroll by February 6 or Lose '
                                'Tariff Refunds',
                       'channel': 'Ask The Customs Manager',
                       'author': 'Ask The Customs Manager',
                       'text': 'A wrong account number means the refund goes into the void for months.',
                       'tip': 'A wrong account number means the refund goes into the void for months.',
                       'timestamp': 133,
                       'timestamp_seconds': 133,
                       'timestamp_label': '[00:02:13]',
                       'url': 'https://www.youtube.com/watch?v=NRCd8c6t8rY&t=133s',
                       'markdown': '[00:02:13](https://www.youtube.com/watch?v=NRCd8c6t8rY&t=133s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'sMBX0ZlgJRY',
                       'title': 'CBP Refund Portal is LIVE - Claim Your 2025 Tariff Money Now!',
                       'channel': 'NextGen CPA',
                       'author': 'NextGen CPA',
                       'text': 'If you miss a 7501 form, you have to start a new declaration, which can '
                               'push you to the back of the queue.',
                       'tip': 'If you miss a 7501 form, you have to start a new declaration, which can '
                              'push you to the back of the queue.',
                       'timestamp': 70,
                       'timestamp_seconds': 70,
                       'timestamp_label': '[00:01:10]',
                       'url': 'https://www.youtube.com/watch?v=sMBX0ZlgJRY&t=70s',
                       'markdown': '[00:01:10](https://www.youtube.com/watch?v=sMBX0ZlgJRY&t=70s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'qVk8ygNZbS8',
                       'title': 'Tariff refund system will be ready in 45 days, U.S. customs agency says',
                       'channel': 'CBC News',
                       'author': 'CBC News',
                       'text': 'CBP cites more than 330,000 importers and $166 billion in refunds, with '
                               'processing that would take 4.4 million man-hours.',
                       'tip': 'CBP cites more than 330,000 importers and $166 billion in refunds, with '
                              'processing that would take 4.4 million man-hours.',
                       'timestamp': 45,
                       'timestamp_seconds': 45,
                       'timestamp_label': '[00:00:45]',
                       'url': 'https://www.youtube.com/watch?v=qVk8ygNZbS8&t=45s',
                       'markdown': '[00:00:45](https://www.youtube.com/watch?v=qVk8ygNZbS8&t=45s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '2H7zdtUvSDA',
                       'title': 'CBP Ends Paper Checks February 6 – Enroll in ACH for Refunds NOW',
                       'channel': 'Ask The Customs Manager',
                       'author': 'Ask The Customs Manager',
                       'text': "If you put the wrong bank account, that's on you.",
                       'tip': "If you put the wrong bank account, that's on you.",
                       'timestamp': 153,
                       'timestamp_seconds': 153,
                       'timestamp_label': '[00:02:33]',
                       'url': 'https://www.youtube.com/watch?v=2H7zdtUvSDA&t=153s',
                       'markdown': '[00:02:33](https://www.youtube.com/watch?v=2H7zdtUvSDA&t=153s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'P1YIRCE3BPQ',
                       'title': "Freight Expectations: CBP's ACE Portal",
                       'channel': 'Scarbrough Global',
                       'author': 'Scarbrough Global',
                       'text': 'If you are not set up on the ACE portal with your bank information set up '
                               "to receive that via AC, you won't get your money.",
                       'tip': 'If you are not set up on the ACE portal with your bank information set up '
                              "to receive that via AC, you won't get your money.",
                       'timestamp': 63,
                       'timestamp_seconds': 63,
                       'timestamp_label': '[00:01:03]',
                       'url': 'https://www.youtube.com/watch?v=P1YIRCE3BPQ&t=63s',
                       'markdown': '[00:01:03](https://www.youtube.com/watch?v=P1YIRCE3BPQ&t=63s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'P1YIRCE3BPQ',
                       'title': "Freight Expectations: CBP's ACE Portal",
                       'channel': 'Scarbrough Global',
                       'author': 'Scarbrough Global',
                       'text': "It's a $1,000 per entry that you forget.",
                       'tip': "It's a $1,000 per entry that you forget.",
                       'timestamp': 1733,
                       'timestamp_seconds': 1733,
                       'timestamp_label': '[00:28:53]',
                       'url': 'https://www.youtube.com/watch?v=P1YIRCE3BPQ&t=1733s',
                       'markdown': '[00:28:53](https://www.youtube.com/watch?v=P1YIRCE3BPQ&t=1733s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'zVrENO4RtLw',
                       'title': 'Unlock Duty Refunds: ACE IEEPA Report in 3 Minutes!',
                       'channel': 'BGI Worldwide Logistics, Inc.',
                       'author': 'BGI Worldwide Logistics, Inc.',
                       'text': 'Review the HTS column to identify IEEPA duties, plus liquidation status '
                               'and liquidation date to track the 180-day protest deadline.',
                       'tip': 'Review the HTS column to identify IEEPA duties, plus liquidation status and '
                              'liquidation date to track the 180-day protest deadline.',
                       'timestamp': 146,
                       'timestamp_seconds': 146,
                       'timestamp_label': '[00:02:26]',
                       'url': 'https://www.youtube.com/watch?v=zVrENO4RtLw&t=146s',
                       'markdown': '[00:02:26](https://www.youtube.com/watch?v=zVrENO4RtLw&t=146s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'FcsTuxrd4SM',
                       'title': 'Post Summary Correction in ACE',
                       'channel': 'Scarbrough Global',
                       'author': 'Scarbrough Global',
                       'text': 'Whereas a protest by law they have to respond to.',
                       'tip': 'Whereas a protest by law they have to respond to.',
                       'timestamp': 37,
                       'timestamp_seconds': 37,
                       'timestamp_label': '[00:00:37]',
                       'url': 'https://www.youtube.com/watch?v=FcsTuxrd4SM&t=37s',
                       'markdown': '[00:00:37](https://www.youtube.com/watch?v=FcsTuxrd4SM&t=37s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'LqV0KsoyRVw',
                       'title': 'How long will it take for CBP to complete my ACE application?',
                       'channel': 'Scarbrough Global',
                       'author': 'Scarbrough Global',
                       'text': 'The very first time your shared secret is your user ID.',
                       'tip': 'The very first time your shared secret is your user ID.',
                       'timestamp': 58,
                       'timestamp_seconds': 58,
                       'timestamp_label': '[00:00:58]',
                       'url': 'https://www.youtube.com/watch?v=LqV0KsoyRVw&t=58s',
                       'markdown': '[00:00:58](https://www.youtube.com/watch?v=LqV0KsoyRVw&t=58s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'o__9Gebfyq4',
                       'title': 'BorderConnect Virtual Workshop - ACE eManifest',
                       'channel': 'BorderConnect',
                       'author': 'BorderConnect',
                       'text': 'Unfortunately, failure to do so could result in a monetary penalty issued '
                               'by CBP.',
                       'tip': 'Unfortunately, failure to do so could result in a monetary penalty issued '
                              'by CBP.',
                       'timestamp': 64,
                       'timestamp_seconds': 64,
                       'timestamp_label': '[00:01:04]',
                       'url': 'https://www.youtube.com/watch?v=o__9Gebfyq4&t=64s',
                       'markdown': '[00:01:04](https://www.youtube.com/watch?v=o__9Gebfyq4&t=64s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'}]}
