from __future__ import annotations

CHAPTER_6 = {'id': 'Q6',
 'chapter_id': 'Q6',
 'chapter_number': 6,
 'question_number': 6,
 'slug': 'entries-entry-summaries-challenging-cbp-duty-decisions',
 'question_prompt': 'How does a U.S. customs entry work, and how do I correct, protest, or litigate a '
                    'wrong duty assessment?',
 'kicker': 'Q6 / THE BIG MONEY PLAYBOOKS',
 'title': "Entries, Entry Summaries and Challenging CBP's Duty Decisions",
 'subtitle': 'The import process and entry types, CBP Form 7501 block by block and 2026 changes, ISF 10+2, '
             'in-bond entry automation, post summary corrections, the CBP protest process, suing at the '
             'Court of International Trade, and 19 USC foundations',
 'layout_template': 'step_by_step_blueprint',
 'reading_time_minutes': 15,
 'executive_summary': "Brokers, exam coaches, a customs law office, and CBP's own protest team converge on "
                      "one rule: the 7501 is the shipment's tax return, every supporting document must "
                      'tell the same story, and the importer of record owns the numbers even when a broker '
                      'files. CBP reports protests jumping from about 28,000 a year to 93,000 in 2020, a '
                      '221 percent increase, so packaging matters: lead entry first in ACE, grouped '
                      'exclusions, 10-digit HTS plus Chapter 99 numbers, and a specific because statement '
                      'for further review. The challenge ladder runs 180 days to protest after '
                      'liquidation, 30 days to deemed denial under accelerated disposition, pay duties and '
                      'interest, then a CIT summons within 180 days. Practitioners split on whether a '
                      'revised 7501 is required with a protest and on when a continuous bond beats '
                      'single-transaction bonds.',
 'key_metrics': [{'label': 'Protest Volume Surge',
                  'metric': 'Protest Volume Surge',
                  'value': '221 percent increase: about 28,000 per year before 2019 to nearly 60,000 in '
                           '2019 and 93,000 in 2020',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "CBP's protest team reported annual protest filings and 106,505 open or "
                             'suspended protests as of Dec 1, 2020, driving its push for grouped, '
                             'well-documented protests.',
                  'source': 'U.S. Customs and Border Protection ([lGkujBtNI0A @ 00:01:41])'},
                 {'label': 'Protest Filing Window',
                  'metric': 'Protest Filing Window',
                  'value': '180 days after the date of liquidation',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Under Section 1514, CBP decisions become final unless protested within 180 '
                             'days via ACE or CBP Form 19; the liquidation date is the date notice is '
                             'posted.',
                  'source': 'FDAImports.com, LLC ([vv45EYjpwXM @ 00:02:22])'},
                 {'label': 'Accelerated Disposition Deemed Denial',
                  'metric': 'Accelerated Disposition Deemed Denial',
                  'value': 'Deemed denied after 30 days',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Request sent separately by registered or certified mail; all duties and '
                             'interest must be paid before filing a CIT summons, and court review is de '
                             'novo.',
                  'source': 'U.S. Customs and Border Protection ([lGkujBtNI0A @ 01:04:12])'},
                 {'label': '2026 Form 7501 Block Renumbering',
                  'metric': '2026 Form 7501 Block Renumbering',
                  'value': '23 of 43 block numbers moved; page one now 47 blocks in five zones',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'February 2026 revision added blocks 21-24 for steel and aluminum melt, '
                             'smelt, and cast countries on 232 articles, and moved duty and IR tax from '
                             'block 34 to 38.',
                  'source': 'CustomsPrep — Customs Broker License Exam ([qORXZ_TDyKg @ 00:00:20])'}],
 'sections': [{'title': 'Section 1: The Practitioner Consensus',
               'paragraphs': ['Across the brokers, lawyers, and exam coaches teaching entry work, the '
                              'entry summary is treated as the money document. VoraPrep frames CBP Form '
                              "7501 as 'the tax return for a shipment,' filed through ACE, with the "
                              '10-digit HTS driving the duty rate and origin meaning where goods were '
                              'manufactured, not where they shipped from [2rbdaN1Swhk @ 00:00:52]. The '
                              'Yuri Starikov law office lists four jobs for the same form: declaring the '
                              'entry, calculating duties, depositing duties, and identifying the liable '
                              "party, and adds that filling it out correctly is 'what most of the "
                              "importers pay money for' [1DFXItS5lCQ @ 00:02:08]. The supporting stack is "
                              'the same everywhere: commercial invoice, packing list, and bill of lading '
                              'or air waybill, plus FDA or textile certificates where they apply, and '
                              "VoraPrep's rule is that all of them 'have to tell the same story' "
                              '[2rbdaN1Swhk @ 00:03:22]. Freight & Trade lists the identical source '
                              'documents and names inconsistent paperwork, vague descriptions, and wrong '
                              'value, classification, or origin as the core mistakes, opening with a blunt '
                              "warning: 'don't assume that the customs broker is responsible for "
                              "everything' [wDQlwDFTfuE @ 00:04:38]. The practical consensus is that the "
                              'importer owns the numbers on the 7501, the broker is a preparer, and any '
                              'mismatch between documents is where duty disputes are born.',
                              'Once the summary is filed, the clock that matters is liquidation. '
                              'FDAImports.com lays out the spine: under Section 1514, CBP decisions are '
                              'final unless protested, liquidation is due in one year and extendable to '
                              'four, and the date of liquidation is the date the notice is posted '
                              "[vv45EYjpwXM @ 00:01:11]. The window is stated without hedging: 'Section "
                              "1514 gives you 180 days after the date of liquidation to file,' through ACE "
                              'or CBP Form 19, with one protest per entry and amendments allowed inside '
                              "the 180 days [vv45EYjpwXM @ 00:02:22]. CBP's own protest webinar cites 19 "
                              'USC 1514, 19 CFR 174, 1515, 1520(d), and 141.105, and stresses that a '
                              'protest cannot be adverse to the importer; if duties are owed, the play is '
                              'a voluntary deposit within 90 days of liquidation or a prior disclosure, '
                              'never a protest [lGkujBtNI0A @ 00:07:04]. Coach Toyin ties the front end to '
                              'that back end: file in ACE within 15 days of arrival, file the 7501 within '
                              '10 working days of release, and treat liquidation as the moment duty '
                              'becomes final, with five years of records kept behind it [595qylDVQzM @ '
                              '00:04:09]. The shared view: whatever the entry record says is the '
                              'ammunition the protest will have.',
                              "The baseline prerequisites repeat across brokers. Scarbrough Global's Kevin "
                              "and Allison Scher frame the Mod Act as 'shared responsibility' with "
                              'reasonable care as the goal, penalties scaling from negligence to gross '
                              'negligence to fraud, and five areas of most concern: valuation, '
                              'classification, quantity, country of origin, and recordkeeping; they cite a '
                              "penalty of '600,000 plus' for misclassified sugar [c50k-4phw2w @ 00:02:34]. "
                              'Caleb Hall at Scarbrough lists the entry kit as a POA, CF 5106, and a bond, '
                              'says a continuous bond pays off above four to five shipments a year, and '
                              'notes an ocean shipment on single bonds needs two, one for the ISF and one '
                              'for the entry [heA5dQMIcKY @ 00:27:48]. VoraPrep puts the reasonable-care '
                              'trap in exam terms: when invoice and packing list conflict, cotton versus '
                              "polyester, the filer must investigate before filing, and 'blindly relying' "
                              "on the importer is 'a major violation' [2rbdaN1Swhk @ 00:05:53]. The "
                              'Starikov office adds that a CBP Form 5106 must be on file before doing '
                              'business, with the IOR number taking the corporate number with an XX '
                              'suffix, an SSN for sole proprietors, or a CBP-assigned number for foreign '
                              'importers [1DFXItS5lCQ @ 03:08:54]. Five-year recordkeeping is the one '
                              'number nobody disputes, and it is the file every later correction or '
                              'protest will be built from.'],
               'table': {'caption': 'Where the practitioners agree on entries, summaries, and the right to '
                                    'challenge',
                         'headers': ['Consensus Point',
                                     'What Practitioners Say',
                                     'Operator Implication',
                                     'Expert Source'],
                         'rows': [["Form 7501 is the shipment's tax return",
                                   'Filed through ACE; the 10-digit HTS sets the duty rate and origin '
                                   'means place of manufacture',
                                   'Treat every data element as a taxable declaration you will defend '
                                   'later',
                                   'VoraPrep ([2rbdaN1Swhk @ 00:00:52])'],
                                  ['All entry documents must tell the same story',
                                   'Invoice, packing list, and B/L or AWB must agree, plus FDA or textile '
                                   'certificates',
                                   'Reconcile conflicts like cotton versus polyester before filing, never '
                                   'after release',
                                   'VoraPrep ([2rbdaN1Swhk @ 00:03:22])'],
                                  ['The importer of record stays on the hook',
                                   'The IOR often hires a licensed broker but remains responsible for '
                                   'accuracy and compliance',
                                   "Audit the broker's work instead of assuming the broker handles "
                                   'everything',
                                   'Freight & Trade ([wDQlwDFTfuE @ 00:01:22])'],
                                  ['CBP decisions become final unless protested',
                                   'Under Section 1514, protest within 180 days after liquidation via ACE '
                                   'or Form 19',
                                   'Calendar the posted liquidation date for every entry you might '
                                   'challenge',
                                   'FDAImports.com, LLC ([vv45EYjpwXM @ 00:02:22])'],
                                  ['ACE is the only electronic protest lane',
                                   'CBP refuses protests sent by email or fax; ACE is the single accepted '
                                   'electronic channel',
                                   'Build every protest packet inside ACE, not in an inbox or fax queue',
                                   'U.S. Customs and Border Protection ([lGkujBtNI0A @ 00:09:15])'],
                                  ['Five-year recordkeeping is universal across speakers',
                                   'Keep records for at least five years and ask your broker for entry '
                                   'packets',
                                   'Hold your own complete entry file so corrections and protests have '
                                   'evidence ready',
                                   'Scarbrough Global ([heA5dQMIcKY @ 00:55:53])'],
                                  ['Reasonable care governs penalty exposure on every entry',
                                   'Penalties scale from negligence to gross negligence to fraud under '
                                   'shared responsibility',
                                   'Document diligence across valuation, classification, quantity, origin, '
                                   'and recordkeeping',
                                   'Scarbrough Global ([c50k-4phw2w @ 00:02:34])']]}},
              {'title': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ["CBP's webinar is the most granular playbook on the protest itself. Enter "
                              'the lead entry first because it autofills other fields, upload extra '
                              'entries as a .txt file up to 1MB, and attach anything except TIF, TIFF, or '
                              'TXT up to 10MB; a refund sent care-of another party needs a CBP 4811 on '
                              'file [lGkujBtNI0A @ 00:10:25]. Amendments are allowed within 180 days of '
                              'liquidation while the protest is undecided, but documents that arrive late '
                              "go under 'provide supplemental information,' not an amendment [lGkujBtNI0A "
                              '@ 00:22:01]. FDAImports.com confirms each entry gets one protest and that '
                              'an application for further review is available [vv45EYjpwXM @ 00:03:36]. On '
                              "that further review, CBP's Grant wants a specific 'because statement' for "
                              'eligibility; one protested entry can carry the AFR while the other nine '
                              'entries stay suspended, decisions post on CROSS within 60 days, and a '
                              '1515(c) set-aside must be filed within 60 days, is reviewed only on the '
                              'record that was before the center, and counts as denied if still undecided '
                              "after 60 days [lGkujBtNI0A @ 00:30:50]. Sumby's fix for the backlog: group "
                              'like exclusions on one protest with the 10-digit HTS, the Chapter 99 '
                              "number, and product specifics, because sorting mixed exclusions 'is what "
                              "becomes time consuming.'",
                              'When the protest stalls, the escalation ladder is precise. FDAImports.com: '
                              'under Section 1515 CBP has two years to decide, but an '
                              'accelerated-disposition request makes the protest deemed denied at 30 days, '
                              "at the price of barring amendment [vv45EYjpwXM @ 00:03:59]. CBP's Smith "
                              'adds the delivery mechanics: the accelerated-disposition request goes '
                              'separately by registered or certified mail, all duties and interest must be '
                              'paid before a summons is filed, and the court reviews de novo [lGkujBtNI0A '
                              '@ 01:04:12]. FDAImports.com locates the forum: the CIT has exclusive '
                              'jurisdiction under 1581(a), the summons is due within 180 days under '
                              'Section 2636, the complaint within 24 months extendable to 48, and the '
                              'presumption of correctness applies even though the court decides on a de '
                              'novo record [vv45EYjpwXM @ 00:05:26]. For IEEPA tariffs, struck down in '
                              'February 2026, the same channel routes claims through 1581(i) on a two-year '
                              'deadline, points to CAPE refunds, warns that protests can complicate them, '
                              "and reports a class certified in October 2026. Upstream, CBP's Amder shows "
                              'how to avoid needing any of this: request an extension of liquidation while '
                              'a 232 or 301 exclusion is pending, send it straight to the center team, '
                              'then file a PSC once the exclusion is granted [lGkujBtNI0A @ 00:04:52].',
                              'On the front end, the mechanics that keep a refund claim clean start with '
                              'the form itself. The Starikov office breaks the entry number into 11 digits '
                              "in a 3-7-1 layout: a 3-character filer code that works 'like a social "
                              "security number,' a 7-digit broker-set number that must never be recycled, "
                              'and a check digit [1DFXItS5lCQ @ 00:04:32]. CustomsPrep flags the February '
                              '2026 rebuild: 23 of 43 block numbers moved, page one now runs 47 blocks in '
                              'five zones, new blocks 21 through 24 capture steel melt-and-pour and '
                              "aluminum smelt and cast countries for 232 articles 'whether or not the 232 "
                              "duty applies,' duty and IR tax moved from block 34 to 38, and the broker "
                              "file number from 43 to 47 [qORXZ_TDyKg @ 00:00:20]. Docxster's NetCHB demo "
                              'shows the automation lane for in-bond 7512 entries: documents land by alias '
                              'email, Gmail or Microsoft pickup, chat, or forms, OCR maps fields to NetCHB '
                              'values, and the workflow pauses until the broker approves, with drafts '
                              'never posted automatically [bsk4ScOMz_o @ 00:02:10]. When the receiving '
                              "report later disagrees with the 7501, Scarbrough Global's answer is a PSC, "
                              "a filing ACE 'made that easier,' after checking the roughly $20 de minimis "
                              'on duty changes and keeping records [Bse6lVDGA_U @ 00:00:00].'],
               'table': {'caption': 'Hard numbers and filing rules for entries, corrections, and duty '
                                    'challenges',
                         'headers': ['Mechanic',
                                     'Exact Number or Rule',
                                     'How Operators Use It',
                                     'Expert Source'],
                         'rows': [['Protest filing window after liquidation',
                                   '180 days after the posted liquidation date, one protest per entry',
                                   'Count from the posted notice date, not from entry or release',
                                   'FDAImports.com, LLC ([vv45EYjpwXM @ 00:02:42])'],
                                  ['ACE protest upload limits for entries',
                                   'Extra entries uploaded as a .txt file up to 1MB per upload',
                                   'Load the lead entry first, then bulk-upload remaining entries as text',
                                   'U.S. Customs and Border Protection ([lGkujBtNI0A @ 00:11:07])'],
                                  ['Void-denial request timing and clock effect',
                                   '90 days to request, and it does not toll the 180-day CIT clock',
                                   'File the CIT summons on schedule regardless of any pending void-denial '
                                   'request',
                                   'U.S. Customs and Border Protection ([lGkujBtNI0A @ 01:01:36])'],
                                  ['Accelerated disposition to force a decision',
                                   'Sent by registered or certified mail; deemed denied after 30 days',
                                   'Use it to reach the CIT fast, accepting that amendment is barred',
                                   'U.S. Customs and Border Protection ([lGkujBtNI0A @ 01:04:12])'],
                                  ['Informal versus formal entry value threshold',
                                   'Informal under 2,500; formal at 2,500 or more and requires a bond',
                                   'Size bond coverage before shipments cross the formal-entry line',
                                   'Quantum Leap with Coach Toyin ([595qylDVQzM @ 00:02:59])'],
                                  ['Assist added to dutiable transaction value',
                                   'A $50,000 invoice plus $5,000 of tooling equals $55,000 dutiable value',
                                   'Add tooling assists before filing so the declared 7501 value holds up',
                                   'VoraPrep ([2rbdaN1Swhk @ 00:06:42])'],
                                  ['Merchandise processing fee on formal entries',
                                   '0.3464% with about $26 minimum and about 517 maximum, flagged to '
                                   'double-check',
                                   'Budget MPF per formal entry and verify the cap before quoting clients',
                                   'Scarbrough Global ([heA5dQMIcKY @ 00:25:18])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Moves the practitioners use to protect refunds before and after '
                                    'liquidation',
                           'body': 'Small filing choices decide whether a duty challenge is clean, fast, '
                                   'and fully documented.',
                           'items': ['With a 232 or 301 exclusion pending, ask the center team for an '
                                     'extension of liquidation and file a PSC once it is granted, instead '
                                     'of fighting through a protest later [U.S. Customs and Border '
                                     'Protection — lGkujBtNI0A @ 00:04:52].',
                                     'Treat void-denial requests as a side bet: they run 90 days and do '
                                     'NOT toll the 180-day CIT clock, so the summons deadline keeps '
                                     'running [U.S. Customs and Border Protection — lGkujBtNI0A @ '
                                     '01:01:36].',
                                     'Strip duties out of DDP values before filing the entry summary, or '
                                     'you pay duty twice on the same goods [Law Office of Yuri Starikov, '
                                     'LLC — 1DFXItS5lCQ @ 04:00:13].',
                                     "Write your own line descriptions: the word 'guns' in an HTS "
                                     'description triggered exams on spray guns until the firm wrote its '
                                     'own [Law Office of Yuri Starikov, LLC — 1DFXItS5lCQ @ 03:41:25].']},
               'sop_steps': [{'step': 1,
                              'title': 'Build a defensible 7501 file',
                              'action': 'Reconcile invoice, packing list, and B/L or AWB before submitting '
                                        'the entry summary in ACE.',
                              'detail': "All documents 'have to tell the same story'; conflicts such as "
                                        'cotton versus polyester must be investigated before filing, and '
                                        'every document is kept for 5 years [VoraPrep — 2rbdaN1Swhk @ '
                                        '00:03:22].'},
                             {'step': 2,
                              'title': 'Correct before liquidation',
                              'action': 'File a PSC when the receiving report disagrees with the 7501, or '
                                        'request an extension of liquidation while an exclusion is '
                                        'pending.',
                              'detail': 'Check the roughly $20 de minimis on duty changes and keep the '
                                        'broker and receiving staff in contact [Scarbrough Global — '
                                        'Bse6lVDGA_U @ 00:00:00]; then file the PSC once the 232 or 301 '
                                        'exclusion is granted [U.S. Customs and Border Protection — '
                                        'lGkujBtNI0A @ 00:04:52].'},
                             {'step': 3,
                              'title': 'Protest inside 180 days through ACE',
                              'action': 'Enter the lead entry first, group like exclusions, and attach the '
                                        '10-digit HTS, Chapter 99 number, and product specifics.',
                              'detail': 'The protest window is 180 days after the posted liquidation date '
                                        '[FDAImports.com, LLC — vv45EYjpwXM @ 00:02:22]; the lead entry '
                                        'autofills other fields and extra entries go in a .txt upload up '
                                        'to 1MB [U.S. Customs and Border Protection — lGkujBtNI0A @ '
                                        '00:10:25].'},
                             {'step': 4,
                              'title': 'Escalate to the CIT',
                              'action': 'Request accelerated disposition by registered or certified mail, '
                                        'pay all duties and interest, then file the summons.',
                              'detail': 'Accelerated disposition is deemed denied after 30 days and review '
                                        'is de novo [U.S. Customs and Border Protection — lGkujBtNI0A @ '
                                        '01:04:12]; the CIT summons is due within 180 days and the '
                                        'complaint within 24 months, extendable to 48 [FDAImports.com, LLC '
                                        '— vv45EYjpwXM @ 00:05:26].'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The first split is whether a refund fight should ever reach the protest '
                              'stage. Amder, speaking on the U.S. Customs and Border Protection webinar, '
                              'pushes the avoidance route: while a 232 or 301 exclusion is pending, '
                              'request an extension of liquidation, then file a post summary correction '
                              'once the exclusion is granted, and send extension requests straight to the '
                              'center team [lGkujBtNI0A @ 00:04:52]. Scarbrough Global runs the same PSC '
                              'lane for ordinary mismatches: when the receiving report does not match the '
                              '7501, file a PSC, which ACE "made that easier," and watch the roughly $20 '
                              'de minimis on duty changes [Bse6lVDGA_U @ 00:00:00]. Once a protest is '
                              'unavoidable, the same CBP panel splits on paperwork. Sumby calls a revised '
                              '7501 the "gold standard" for supporting an exclusion protest, alongside '
                              'grouping like exclusions, the 10-digit HTS, the Chapter 99 number and '
                              'product specifics [lGkujBtNI0A @ 00:56:21]. Ernst answers that the revised '
                              '7501 is not required except for non-EDI entries [lGkujBtNI0A @ 01:16:25]. '
                              'Operator read: build the revised 7501 when the entry was filed outside EDI, '
                              'and treat it as optional supporting evidence on clean EDI entries where the '
                              'center already holds the data.',
                              'The second split is speed versus flexibility once a protest is on file. '
                              'Smith, on the CBP webinar, lays out the fast lane: separately send a '
                              'request for accelerated disposition by registered or certified mail, and '
                              'the protest is deemed denied after 30 days, opening the door to the Court '
                              'of International Trade [lGkujBtNI0A @ 01:04:12]. FDAImports.com, LLC flags '
                              'the price: under section 1515 CBP otherwise has two years to decide, and '
                              'accelerated disposition bars any later amendment to the protest '
                              '[vv45EYjpwXM @ 00:03:59]. The alternative is to stay inside CBP and use '
                              'further review. Grant explains that one protested entry can carry the AFR '
                              'while the other nine entries sit suspended, that eligibility needs a '
                              'specific "because statement," and that decisions publish on CROSS within 60 '
                              'days [lGkujBtNI0A @ 00:29:04]. On IEEPA duties the channels diverge again: '
                              'FDAImports.com says those tariffs, struck down in February 2026, run under '
                              'section 1581(i) with a two-year deadline, that CAPE refunds are the '
                              'vehicle, and that protests can complicate them [vv45EYjpwXM @ 00:08:22]. '
                              'Operator read: reserve accelerated disposition for a complete, final '
                              'record, since amendment rights die; use AFR for test-case entries that '
                              'carry a suspended batch.',
                              'The third split is who actually files and at what dollar line. Caleb Hall '
                              'of Scarbrough Global states flatly, "It is required that you hire a US '
                              'Customs broker in order to file entry" [heA5dQMIcKY @ 00:16:04]. Coach '
                              'Toyin teaches the opposite option: self-file as the owner or hire a broker '
                              'from the list on cbp.gov, then file in ACE within 15 days of arrival '
                              '[595qylDVQzM @ 00:02:04]. Kevin, also at Scarbrough, advises being the '
                              'importer of record yourself and buying FOB, but warns that multiple brokers '
                              'work only with a strong internal program [c50k-4phw2w @ 00:37:31]. '
                              'Thresholds also drift between speakers. The Starikov lecture says the '
                              'informal limit was tested at $2,000 and is now $2,500, with anything under '
                              '$200 handled as Section 321 with no duty and no HTS number; Caleb puts '
                              'Section 321 at about $800 and requires a formal entry above $2,500 or for '
                              'any Section 301 or 232 goods, and Coach Toyin also cites 800. Fee math '
                              'diverges as well: Starikov reads MPF as 25 to 485 per formal entry, while '
                              'Caleb quotes 0.3464 percent with a minimum near $26 and a maximum near 517 '
                              'that they said needed double-checking [heA5dQMIcKY @ 00:25:18].'],
               'table': {'caption': 'Competing playbooks for entry corrections, protests, filing roles, '
                                    'bonds and fees',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Whether a revised 7501 belongs in the exclusion protest file',
                                   'Sumby calls the revised 7501 the gold standard for exclusion protests',
                                   'Ernst says a revised 7501 is not required except for non-EDI entries',
                                   'U.S. Customs and Border Protection ([lGkujBtNI0A @ 00:56:21]); U.S. '
                                   'Customs and Border Protection ([lGkujBtNI0A @ 01:16:25])'],
                                  ['Pending 232 or 301 exclusion before the entry liquidates',
                                   'Amder requests a liquidation extension, then files a PSC once the '
                                   'exclusion is granted',
                                   'Protest within 180 days after the posted liquidation date via ACE or '
                                   'CBP Form 19',
                                   'U.S. Customs and Border Protection ([lGkujBtNI0A @ 00:04:52]); '
                                   'FDAImports.com, LLC ([vv45EYjpwXM @ 00:02:42])'],
                                  ['Forcing a fast protest decision to reach the trade court',
                                   'Smith mails an accelerated disposition request; protest is deemed '
                                   'denied after 30 days',
                                   'Waiting preserves amendment rights because CBP otherwise has two years '
                                   'under section 1515',
                                   'U.S. Customs and Border Protection ([lGkujBtNI0A @ 01:04:12]); '
                                   'FDAImports.com, LLC ([vv45EYjpwXM @ 00:03:59])'],
                                  ['Who files the entry and carries importer of record exposure',
                                   'Caleb Hall says hiring a US customs broker is required to file entry',
                                   'Coach Toyin allows self-filing as owner; Kevin says be the importer of '
                                   'record yourself',
                                   'Scarbrough Global ([heA5dQMIcKY @ 00:16:04]); Quantum Leap with Coach '
                                   'Toyin ([595qylDVQzM @ 00:02:04])'],
                                  ['Choosing a continuous bond versus single-transaction bonds',
                                   'Kevin says single-transaction suits a few imports yearly unless value '
                                   'is high or FDA applies',
                                   'Caleb says continuous wins above 4 to 5 shipments yearly and at '
                                   '$200,000 of imports',
                                   'Scarbrough Global ([c50k-4phw2w @ 00:07:17]); Scarbrough Global '
                                   '([heA5dQMIcKY @ 00:38:06])'],
                                  ['Section 321 and informal entry dollar thresholds in practice',
                                   'Starikov lecture puts informal at $2,500 and Section 321 under $200 '
                                   'with no duty',
                                   'Caleb Hall and Coach Toyin both put the Section 321 line at about $800',
                                   'Law Office of Yuri Starikov, LLC ([1DFXItS5lCQ @ 00:20:38]); '
                                   'Scarbrough Global ([heA5dQMIcKY @ 00:18:05])'],
                                  ['Merchandise processing fee figures used for landed cost math',
                                   'Starikov reads MPF as 25 to 485 per formal entry at a .25 rate',
                                   'Caleb quotes 0.3464 percent, minimum about $26, maximum about 517, '
                                   'flagged for double-checking',
                                   'Law Office of Yuri Starikov, LLC ([1DFXItS5lCQ @ 04:09:24]); '
                                   'Scarbrough Global ([heA5dQMIcKY @ 00:25:18])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The fatal mistakes in a duty fight are almost all clock mistakes. '
                              'FDAImports.com, LLC opens with the rule that frames everything: under '
                              'section 1514 a CBP decision is final unless protested, and you get 180 days '
                              "after the posted date of liquidation; miss one step and CBP's decision "
                              'becomes final [vv45EYjpwXM @ 00:02:42]. Sumby on the CBP webinar adds a '
                              'trap that burns experienced filers: a request to void a protest denial must '
                              'be filed within 90 days, and it does not toll the 180-day clock to reach '
                              'the Court of International Trade [lGkujBtNI0A @ 01:01:36]. Grant adds that '
                              'a set-aside under 1515(c) must be filed within 60 days, review is limited '
                              'to the record that was before the center, and silence after 60 days means '
                              'denied [lGkujBtNI0A @ 00:39:14]. Smith closes the loop: all duties and '
                              'interest must be paid before filing a summons [lGkujBtNI0A @ 01:09:33]. '
                              'Late documents are another self-inflicted wound: they go under "provide '
                              'supplemental information," not under an amendment, and amendments only work '
                              'within 180 days of liquidation while the protest is undecided. A protest '
                              'also cannot be adverse to the importer; owed duties go back by voluntary '
                              'deposit within 90 days or prior disclosure.',
                              'On the entry summary itself, the firsthand losses come from shortcuts. The '
                              'Starikov lecture tells of a computer-generated MID code that matched a '
                              "sanctioned party's code, and the freight was seized; the same lecture "
                              'insists on breaking out GRI 3B sets with X and V lines, because brokers who '
                              'skip it for "expediency" hide AD duties and differing origins [1DFXItS5lCQ '
                              '@ 03:44:48]. Value errors compound: strip duties out of DDP values or you '
                              'pay duty twice, and never fold freight into total entered value '
                              '[1DFXItS5lCQ @ 04:00:13]. VoraPrep frames the reasonable-care failure: when '
                              'the invoice says cotton and the packing list says polyester, investigate '
                              'before filing, because "blindly relying" on the importer is "a major '
                              'violation" [2rbdaN1Swhk @ 00:05:53]. The penalty scale is real. Kevin of '
                              'Scarbrough Global cites a penalty of "600,000 plus" for misclassifying '
                              'sugar, with penalties scaling by negligence, gross negligence and fraud '
                              '[c50k-4phw2w @ 00:03:37], and Caleb warns that switching tariff numbers to '
                              'dodge a 25 percent Section 301 layer on top of a 2 percent base duty is '
                              '"literally fraud." The Starikov firm also wrote its own descriptions after '
                              'the HTS word "guns" triggered exams on spray guns.',
                              'The economics checks start before the vessel sails. Caleb Hall of '
                              'Scarbrough Global puts the late-ISF penalty at $5,000 and stresses the ISF '
                              'is due 24 to 48 hours before the last foreign port, so a transship through '
                              'Kaohsiung moves the deadline [heA5dQMIcKY @ 00:02:50]. JSJ International '
                              'LCB adds that best-available data for manufacturer, ship-to, origin and HTS '
                              'must be updated before arrival, and cancelled shipments withdrawn, because '
                              'filing the ISF "correctly and on time is not optional" [2cuZPxRLr1E @ '
                              '00:04:58]. Once cargo lands, the Starikov lecture warns that goods not '
                              'declared within 15 days go to general order, a "punishment warehouse" with '
                              'extraordinary storage fees [1DFXItS5lCQ @ 03:07:20]. Bonding is where small '
                              'importers leak cash: Caleb notes that an ocean shipment on single bonds '
                              'needs two, one for the ISF and one for the entry, and that at $200,000 of '
                              'imports a continuous bond is cheaper; Kevin adds that FDA shipments need a '
                              "bond at three times the goods' value. Finally, budget for delay in any "
                              'protest: the CBP webinar counts 106,505 open or suspended protests as of '
                              'December 1, 2020, with volume rising from about 28,000 a year to 93,000 in '
                              '2020 [lGkujBtNI0A @ 00:01:41].'],
               'table': {'caption': 'Firsthand traps, losses and cost leaks on entries, protests and court '
                                    'filings',
                         'headers': ['Failure Mode',
                                     'What Happened Or Was Warned',
                                     'Economics Or Consequence',
                                     'Expert Source'],
                         'rows': [['Assuming a void-denial request pauses the court clock',
                                   'The 90-day void-denial request does not toll the 180-day CIT window',
                                   'Miss the summons window and the CBP denial stands as final',
                                   'U.S. Customs and Border Protection ([lGkujBtNI0A @ 01:01:36]); '
                                   'FDAImports.com, LLC ([vv45EYjpwXM @ 00:00:26])'],
                                  ['Filing a CIT summons before paying the assessed duties',
                                   'Smith requires all duties and interest paid before any summons is '
                                   'filed',
                                   'FDAImports.com reads the same pay-first rule from 28 USC 2637',
                                   'U.S. Customs and Border Protection ([lGkujBtNI0A @ 01:09:33]); '
                                   'FDAImports.com, LLC ([vv45EYjpwXM @ 00:05:05])'],
                                  ['Trusting a computer-generated MID code without manual verification',
                                   "The generated code matched a sanctioned party's MID code on file",
                                   'The freight was seized; textiles must name the actual manufacturer',
                                   'Law Office of Yuri Starikov, LLC ([1DFXItS5lCQ @ 02:13:42])'],
                                  ['Late or stale ISF data keyed to the wrong port',
                                   'The ISF deadline runs from the last foreign port, including transship '
                                   'hubs',
                                   'A $5,000 late-ISF penalty, and on-time correct filing is not optional',
                                   'Scarbrough Global ([heA5dQMIcKY @ 00:02:50]); JSJ INTERNATIONAL LCB '
                                   '([2cuZPxRLr1E @ 00:07:42])'],
                                  ['Leaving duty inside DDP values or freight inside entered value',
                                   'Duties left in a DDP price get duty charged on top of them',
                                   'The importer pays duty twice, and freight in entered value is a tested '
                                   'trap',
                                   'Law Office of Yuri Starikov, LLC ([1DFXItS5lCQ @ 04:00:13]); Law '
                                   'Office of Yuri Starikov, LLC ([1DFXItS5lCQ @ 04:03:55])'],
                                  ['Switching tariff numbers to escape Section 301 layers',
                                   'A 2 percent base duty plus 25 percent Section 301 equals 27 percent',
                                   'Caleb calls the switch literally fraud; a sugar misclassification drew '
                                   'a 600,000-plus penalty',
                                   'Scarbrough Global ([heA5dQMIcKY @ 00:42:35]); Scarbrough Global '
                                   '([c50k-4phw2w @ 00:03:37])'],
                                  ['Leaving arrived cargo undeclared for more than fifteen days',
                                   'Undeclared goods are moved to general order, a punishment warehouse',
                                   'Extraordinary storage fees accrue against the importer until the goods '
                                   'are entered',
                                   'Law Office of Yuri Starikov, LLC ([1DFXItS5lCQ @ 03:07:20])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Four checks before any protest, correction or court filing moves',
                           'body': 'Each gate below comes from a loss, reversal or warning reported by the '
                                   'practitioners. Clear all four before the filing goes out.',
                           'items': ['Calendar the 180-day CIT summons date from the denial and never '
                                     'count on a 90-day void-denial request to pause it [U.S. Customs and '
                                     'Border Protection — lGkujBtNI0A @ 01:01:36].',
                                     'Confirm every dollar of duties and interest is paid before the '
                                     'summons is filed, or the court route closes [U.S. Customs and Border '
                                     'Protection — lGkujBtNI0A @ 01:09:33].',
                                     'Hand-check every MID against the actual manufacturer; a '
                                     'computer-generated MID that matched a sanctioned party got freight '
                                     'seized [Law Office of Yuri Starikov, LLC — 1DFXItS5lCQ @ 02:13:42].',
                                     'Reconcile invoice and packing list conflicts, such as cotton versus '
                                     'polyester, before filing, because blindly relying on the importer is '
                                     'a major violation [VoraPrep — 2rbdaN1Swhk @ 00:05:53].']}}],
 'pull_quote': '"So your protest defines the fight." Attributed to FDAImports.com, LLC (vv45EYjpwXM @ '
               '00:07:22).',
 'diagram_id': 'diag-02',
 'action_checklist': ['While a 232 or 301 exclusion is pending, request an extension of liquidation '
                      'directly from the center team, then file a PSC once the exclusion is granted [U.S. '
                      'Customs and Border Protection — lGkujBtNI0A @ 00:04:52].',
                      'When the receiving report does not match the 7501, file a post summary correction '
                      'in ACE, check the roughly $20 de minimis and keep the records [Scarbrough Global — '
                      'Bse6lVDGA_U @ 00:00:00].',
                      'Group entries with similar exclusions on one protest and supply the 10-digit HTS, '
                      'the Chapter 99 number and product specifics [U.S. Customs and Border Protection — '
                      'lGkujBtNI0A @ 00:52:02].',
                      'File the protest in ACE or on CBP Form 19 within 180 days after the posted '
                      'liquidation date, one protest per entry [FDAImports.com, LLC — vv45EYjpwXM @ '
                      '00:02:42].',
                      'Send late documents under provide supplemental information rather than as an '
                      'amendment, and amend only within 180 days of liquidation while the protest is '
                      'undecided [U.S. Customs and Border Protection — lGkujBtNI0A @ 00:23:30].',
                      'If the protest is denied, pay first and file a summons at the Court of '
                      'International Trade within 180 days, then the complaint within 24 to 48 months '
                      '[FDAImports.com, LLC — vv45EYjpwXM @ 00:05:26].'],
 'statutory_citations': [{'title': 'U.S. Customs and Border Protection — CBP Protest Webinar [01:01:36]',
                          'url': 'https://www.youtube.com/watch?v=lGkujBtNI0A&t=3696s',
                          'relevance': 'Primary practitioner testimony on protest mechanics, AFR, '
                                       'set-aside and void-denial timing in ACE.'},
                         {'title': 'FDAImports.com, LLC — How To SUE Customs When They Overcharge Your '
                                   'Business! [00:02:42]',
                          'url': 'https://www.youtube.com/watch?v=vv45EYjpwXM&t=162s',
                          'relevance': 'Primary practitioner testimony on the 180-day protest window, '
                                       'accelerated disposition and CIT pay-first rules.'},
                         {'title': 'Scarbrough Global — Post Summary Corrections and 7501 [00:00:00]',
                          'url': 'https://www.youtube.com/watch?v=Bse6lVDGA_U&t=0s',
                          'relevance': 'Primary practitioner testimony on using PSCs to fix 7501 '
                                       'mismatches before liquidation.'},
                         {'title': 'Law Office of Yuri Starikov, LLC — CBP Form 7501 Discussion [03:44:48]',
                          'url': 'https://www.youtube.com/watch?v=1DFXItS5lCQ&t=13488s',
                          'relevance': 'Primary practitioner testimony on line-level 7501 errors that hide '
                                       'AD duties and inflate duty.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'lGkujBtNI0A',
                       'title': 'CBP Protest Webinar',
                       'channel': 'U.S. Customs and Border Protection',
                       'author': 'U.S. Customs and Border Protection',
                       'text': 'What is probably a best practice that we would like to put forth is that '
                               'you group entries that have similar exclusions.',
                       'tip': 'What is probably a best practice that we would like to put forth is that '
                              'you group entries that have similar exclusions.',
                       'timestamp': 3018,
                       'timestamp_seconds': 3018,
                       'timestamp_label': '[00:50:18]',
                       'url': 'https://www.youtube.com/watch?v=lGkujBtNI0A&t=3018s',
                       'markdown': '[00:50:18](https://www.youtube.com/watch?v=lGkujBtNI0A&t=3018s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'lGkujBtNI0A',
                       'title': 'CBP Protest Webinar',
                       'channel': 'U.S. Customs and Border Protection',
                       'author': 'U.S. Customs and Border Protection',
                       'text': 'You will need to separately file by registered or certified mail that '
                               'request for accelerated disposition.',
                       'tip': 'You will need to separately file by registered or certified mail that '
                              'request for accelerated disposition.',
                       'timestamp': 3949,
                       'timestamp_seconds': 3949,
                       'timestamp_label': '[01:05:49]',
                       'url': 'https://www.youtube.com/watch?v=lGkujBtNI0A&t=3949s',
                       'markdown': '[01:05:49](https://www.youtube.com/watch?v=lGkujBtNI0A&t=3949s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '2cuZPxRLr1E',
                       'title': 'ISF “10+2” Filing Explained | Importer Requirements under 19 CFR Part 149 '
                                '| CBP Compliance Guide',
                       'channel': 'JSJ INTERNATIONAL LCB',
                       'author': 'JSJ INTERNATIONAL LCB',
                       'text': 'Filing the ISF correctly and on time is not optional.',
                       'tip': 'Filing the ISF correctly and on time is not optional.',
                       'timestamp': 462,
                       'timestamp_seconds': 462,
                       'timestamp_label': '[00:07:42]',
                       'url': 'https://www.youtube.com/watch?v=2cuZPxRLr1E&t=462s',
                       'markdown': '[00:07:42](https://www.youtube.com/watch?v=2cuZPxRLr1E&t=462s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '2rbdaN1Swhk',
                       'title': '[CBLE] CBLE1: Entry Summary Documentation and Data Elements (CBP Form '
                                '7501)',
                       'channel': 'VoraPrep',
                       'author': 'VoraPrep',
                       'text': 'You have to keep a copy of every single one of these documents for 5 '
                               'years.',
                       'tip': 'You have to keep a copy of every single one of these documents for 5 years.',
                       'timestamp': 304,
                       'timestamp_seconds': 304,
                       'timestamp_label': '[00:05:04]',
                       'url': 'https://www.youtube.com/watch?v=2rbdaN1Swhk&t=304s',
                       'markdown': '[00:05:04](https://www.youtube.com/watch?v=2rbdaN1Swhk&t=304s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'aNG7o_BW3k8',
                       'title': 'U.S. Customs (CBP) Entry Summary: General Overview Webcast Preview',
                       'channel': 'Law Office of Yuri Starikov, LLC',
                       'author': 'Law Office of Yuri Starikov, LLC',
                       'text': 'Some of the fill in the blanks on this form are pretty much '
                               'self-explanatory, some of them require more deliberation, more thinking, '
                               'they require your knowledge of law, of regulation.',
                       'tip': 'Some of the fill in the blanks on this form are pretty much '
                              'self-explanatory, some of them require more deliberation, more thinking, '
                              'they require your knowledge of law, of regulation.',
                       'timestamp': 24,
                       'timestamp_seconds': 24,
                       'timestamp_label': '[00:00:24]',
                       'url': 'https://www.youtube.com/watch?v=aNG7o_BW3k8&t=24s',
                       'markdown': '[00:00:24](https://www.youtube.com/watch?v=aNG7o_BW3k8&t=24s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'bsk4ScOMz_o',
                       'title': 'How to Automate CBP Form 7512 Inbond Entries in NetCHB (Docxster Demo)',
                       'channel': 'Docxster | Document-First Automation',
                       'author': 'Docxster | Document-First Automation',
                       'text': "It's not going to get posted as is.",
                       'tip': "It's not going to get posted as is.",
                       'timestamp': 219,
                       'timestamp_seconds': 219,
                       'timestamp_label': '[00:03:39]',
                       'url': 'https://www.youtube.com/watch?v=bsk4ScOMz_o&t=219s',
                       'markdown': '[00:03:39](https://www.youtube.com/watch?v=bsk4ScOMz_o&t=219s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'qORXZ_TDyKg',
                       'title': 'CBP Form 7501 Entry Summary Explained, Block by Block — and What Changed '
                                'in 2026',
                       'channel': 'CustomsPrep — Customs Broker License Exam',
                       'author': 'CustomsPrep — Customs Broker License Exam',
                       'text': 'The April 2026 exam still printed the old layout.',
                       'tip': 'The April 2026 exam still printed the old layout.',
                       'timestamp': 103,
                       'timestamp_seconds': 103,
                       'timestamp_label': '[00:01:43]',
                       'url': 'https://www.youtube.com/watch?v=qORXZ_TDyKg&t=103s',
                       'markdown': '[00:01:43](https://www.youtube.com/watch?v=qORXZ_TDyKg&t=103s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '1DFXItS5lCQ',
                       'title': 'CBP Form 7501 Discussion',
                       'channel': 'Law Office of Yuri Starikov, LLC',
                       'author': 'Law Office of Yuri Starikov, LLC',
                       'text': 'Customs has been known to ask a lot of questions especially with the entry '
                               'type code, so keep that in mind.',
                       'tip': 'Customs has been known to ask a lot of questions especially with the entry '
                              'type code, so keep that in mind.',
                       'timestamp': 1214,
                       'timestamp_seconds': 1214,
                       'timestamp_label': '[00:20:14]',
                       'url': 'https://www.youtube.com/watch?v=1DFXItS5lCQ&t=1214s',
                       'markdown': '[00:20:14](https://www.youtube.com/watch?v=1DFXItS5lCQ&t=1214s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '1DFXItS5lCQ',
                       'title': 'CBP Form 7501 Discussion',
                       'channel': 'Law Office of Yuri Starikov, LLC',
                       'author': 'Law Office of Yuri Starikov, LLC',
                       'text': 'The actual country of origin shall be specified rather than a country of '
                               'invoice or exportation.',
                       'tip': 'The actual country of origin shall be specified rather than a country of '
                              'invoice or exportation.',
                       'timestamp': 6498,
                       'timestamp_seconds': 6498,
                       'timestamp_label': '[01:48:18]',
                       'url': 'https://www.youtube.com/watch?v=1DFXItS5lCQ&t=6498s',
                       'markdown': '[01:48:18](https://www.youtube.com/watch?v=1DFXItS5lCQ&t=6498s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'wDQlwDFTfuE',
                       'title': 'What Is a Customs Entry  A Beginner’s Guide to U S  Imports',
                       'channel': 'Freight & Trade',
                       'author': 'Freight & Trade',
                       'text': "First, don't assume that the customs broker is responsible for everything.",
                       'tip': "First, don't assume that the customs broker is responsible for everything.",
                       'timestamp': 278,
                       'timestamp_seconds': 278,
                       'timestamp_label': '[00:04:38]',
                       'url': 'https://www.youtube.com/watch?v=wDQlwDFTfuE&t=278s',
                       'markdown': '[00:04:38](https://www.youtube.com/watch?v=wDQlwDFTfuE&t=278s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'WyZnXlLGG-o',
                       'title': 'USA CBP Rules Explained! Import-Export Compliance Made Easy',
                       'channel': 'Vmani International',
                       'author': 'Vmani International',
                       'text': 'Common mistakes are a wrong HTS code, under- or overvaluing goods, missing '
                               'paperwork, safety non-compliance and late duty payments.',
                       'tip': 'Common mistakes are a wrong HTS code, under- or overvaluing goods, missing '
                              'paperwork, safety non-compliance and late duty payments.',
                       'timestamp': 163,
                       'timestamp_seconds': 163,
                       'timestamp_label': '[00:02:43]',
                       'url': 'https://www.youtube.com/watch?v=WyZnXlLGG-o&t=163s',
                       'markdown': '[00:02:43](https://www.youtube.com/watch?v=WyZnXlLGG-o&t=163s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'l9SdxEh635U',
                       'title': 'How to fulfill the CBP form',
                       'channel': 'Mandy Wu',
                       'author': 'Mandy Wu',
                       'text': 'Address lines are limited to 32 characters, so move any overflow to the '
                               'next line.',
                       'tip': 'Address lines are limited to 32 characters, so move any overflow to the '
                              'next line.',
                       'timestamp': 139,
                       'timestamp_seconds': 139,
                       'timestamp_label': '[00:02:19]',
                       'url': 'https://www.youtube.com/watch?v=l9SdxEh635U&t=139s',
                       'markdown': '[00:02:19](https://www.youtube.com/watch?v=l9SdxEh635U&t=139s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Bse6lVDGA_U',
                       'title': 'Post Summary Corrections and 7501',
                       'channel': 'Scarbrough Global',
                       'author': 'Scarbrough Global',
                       'text': 'If the receiving report does not match the 7501, file a post summary '
                               'correction, and ACE made that easier.',
                       'tip': 'If the receiving report does not match the 7501, file a post summary '
                              'correction, and ACE made that easier.',
                       'timestamp': 0,
                       'timestamp_seconds': 0,
                       'timestamp_label': '[00:00:00]',
                       'url': 'https://www.youtube.com/watch?v=Bse6lVDGA_U&t=0s',
                       'markdown': '[00:00:00](https://www.youtube.com/watch?v=Bse6lVDGA_U&t=0s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '595qylDVQzM',
                       'title': 'U.S. Import Process by Customs and Border Protection - CBP',
                       'channel': 'Quantum Leap with Coach Toyin',
                       'author': 'Quantum Leap with Coach Toyin',
                       'text': 'File the 7501 entry summary within 10 working days of release.',
                       'tip': 'File the 7501 entry summary within 10 working days of release.',
                       'timestamp': 249,
                       'timestamp_seconds': 249,
                       'timestamp_label': '[00:04:09]',
                       'url': 'https://www.youtube.com/watch?v=595qylDVQzM&t=249s',
                       'markdown': '[00:04:09](https://www.youtube.com/watch?v=595qylDVQzM&t=249s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'TDiFTjun7-4',
                       'title': 'What is 19 USC — The U.S. Customs Code Explained',
                       'channel': 'TestMyself',
                       'author': 'TestMyself',
                       'text': 'Add 1000 first, then look.',
                       'tip': 'Add 1000 first, then look.',
                       'timestamp': 370,
                       'timestamp_seconds': 370,
                       'timestamp_label': '[00:06:10]',
                       'url': 'https://www.youtube.com/watch?v=TDiFTjun7-4&t=370s',
                       'markdown': '[00:06:10](https://www.youtube.com/watch?v=TDiFTjun7-4&t=370s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'vv45EYjpwXM',
                       'title': 'How To SUE Customs When They Overcharge Your Business!',
                       'channel': 'FDAImports.com, LLC',
                       'author': 'FDAImports.com, LLC',
                       'text': 'So your protest defines the fight.',
                       'tip': 'So your protest defines the fight.',
                       'timestamp': 442,
                       'timestamp_seconds': 442,
                       'timestamp_label': '[00:07:22]',
                       'url': 'https://www.youtube.com/watch?v=vv45EYjpwXM&t=442s',
                       'markdown': '[00:07:22](https://www.youtube.com/watch?v=vv45EYjpwXM&t=442s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'c50k-4phw2w',
                       'title': 'U.S. Customs Brokerage and Classification - Full Version',
                       'channel': 'Scarbrough Global',
                       'author': 'Scarbrough Global',
                       'text': "If customs can't determine that then you're likely going to see a hold.",
                       'tip': "If customs can't determine that then you're likely going to see a hold.",
                       'timestamp': 3642,
                       'timestamp_seconds': 3642,
                       'timestamp_label': '[01:00:42]',
                       'url': 'https://www.youtube.com/watch?v=c50k-4phw2w&t=3642s',
                       'markdown': '[01:00:42](https://www.youtube.com/watch?v=c50k-4phw2w&t=3642s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'heA5dQMIcKY',
                       'title': 'US Customs Brokerage Training – Import Process',
                       'channel': 'Scarbrough Global',
                       'author': 'Scarbrough Global',
                       'text': "So, it's a better deal to just go ahead and get the continuous bond if "
                               'nothing else just to save money.',
                       'tip': "So, it's a better deal to just go ahead and get the continuous bond if "
                              'nothing else just to save money.',
                       'timestamp': 2286,
                       'timestamp_seconds': 2286,
                       'timestamp_label': '[00:38:06]',
                       'url': 'https://www.youtube.com/watch?v=heA5dQMIcKY&t=2286s',
                       'markdown': '[00:38:06](https://www.youtube.com/watch?v=heA5dQMIcKY&t=2286s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'}]}
