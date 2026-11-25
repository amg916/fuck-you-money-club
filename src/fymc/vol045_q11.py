from __future__ import annotations

CHAPTER_11 = {'id': 'Q11',
 'chapter_id': 'Q11',
 'chapter_number': 11,
 'question_number': 11,
 'slug': 'vol045-q11-decoding-claims-remittances-carc-rarc',
 'question_prompt': 'How do billers read claims and remittances—CMS-1500, UB-04, 837, 835/ERA, EOB, '
                    'CARC/RARC—to spot the payment variances that feed OON disputes?',
 'kicker': 'Q11 / THE BIG MONEY PLAYBOOKS',
 'title': 'Decoding Claims and Remittances: CMS-1500, 837, 835 ERAs, EOBs, and CARC/RARC Codes',
 'subtitle': 'CMS-1500 and UB-04 field architecture, EHR-to-837 claim drop, line-by-line 835 reading, EOB '
             'vs. ERA, CARC and RARC adjustment and denial codes, rejection vs. denial, remittances and '
             'payer portals, and payment posting and reconciliation to bank deposit',
 'layout_template': 'chapter_opener',
 'reading_time_minutes': 15,
 'executive_summary': 'Billers, EDI vendors and RCM consultants converge on one operating rule: the '
                      'remittance explains every dollar, and the operator who reads group codes, CARCs and '
                      "RARCs controls cash. CO is the provider's write-off, PR is what the patient may "
                      'owe, and CO45 is the normal contractual adjustment, while 16, 29 and 197 are action '
                      'items. On the mechanics side, an 835 is a plain tilde-and-asterisk text file whose '
                      'CLP, SVC, CAS, TRN and PLB segments must balance: charged minus adjustments equals '
                      'paid, and the TRN trace number ties the ERA to the EFT deposit. The Claim Game '
                      'reports a 60-day remittance audit that cut accounts receivable 30 to 40 percent. '
                      'Practitioners split on autoposting trust, whether CO45 signals a write-off or a '
                      'non-covered service, and whether RARCs only appear on denials.',
 'key_metrics': [{'label': 'Accounts receivable reduction from a remittance-versus-contract audit',
                  'metric': 'Accounts receivable reduction from a remittance-versus-contract audit',
                  'value': '30 to 40 percent drop in accounts receivable over a project of about 60 days',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Jeremy Zug's team matched remittances and EOBs against a large agency's fee "
                             'schedules, proved a payer had been underpaying, recovered the difference, '
                             'then installed a contract-check posting process.',
                  'source': 'The Claim Game X Practice Solutions ([FE6Ns41GFH0 @ 00:15:33])'},
                 {'label': 'Per-claim underpayment found in the practice health check',
                  'metric': 'Per-claim underpayment found in the practice health check',
                  'value': '75 cents to $1 per claim',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Underpayment surfaced by matching several remittances to the agency's fee "
                             'schedules; described as a giant difference at volume.',
                  'source': 'The Claim Game X Practice Solutions ([FE6Ns41GFH0 @ 00:13:50])'},
                 {'label': 'Line-level balancing example on a $200 claim',
                  'metric': 'Line-level balancing example on a $200 claim',
                  'value': '$200 billed - $80 CO45 - $100 PR1 = $20 paid',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Contract allowed $120, the $80 difference is written off, $100 goes to the '
                             'unmet deductible, and the payer paid $20; if the math does not balance, '
                             'investigate before posting.',
                  'source': 'Health Weave RCM LLC ([bPFE9F4Y_Y4 @ 00:05:52])'},
                 {'label': 'Timely filing window flagged by CARC 29',
                  'metric': 'Timely filing window flagged by CARC 29',
                  'value': 'Often 90 to 180 days from the date of service',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'A claim submitted even one day late is denied with CARC 29, and those '
                             'services often become write-offs for the provider.',
                  'source': 'AarkNine Healthcare ([3HP5mg0UdCw @ 00:09:24])'}],
 'sections': [{'section_number': 1,
               'heading': 'The Practitioner Consensus: The Remittance Explains Every Dollar',
               'paragraphs': ['Every practitioner starts from the same premise: the remittance is the '
                              'scorecard, and cash without it is blind money. Health Weave RCM frames it '
                              'as a $200 claim paid at $20, where only the remittance explains where the '
                              'other $180 went. The same instructor separates four terms people confuse: '
                              'the EOB explains how a claim was processed, the ERA is the electronic '
                              'version sent to the provider, the 835 is the standard file format carrying '
                              'the ERA, and the EFT is the money itself, often traveling separately and '
                              'linked by a trace number [bPFE9F4Y_Y4 @ 00:01:12]. Tamika at Medical '
                              'Billing Maven draws the same line from the posting desk: the patient EOB '
                              'usually shows a generic word like lab or surgery, while the provider RA or '
                              'ERA can cover several patients and shows the exact codes billed '
                              '[GhRz1M9lxtc @ 00:05:45]. Jeremy Zug of The Claim Game adds that the '
                              "payer's claim ID on the remittance often differs from the claim ID your EHR "
                              'generates, so mapping the two is mandatory [FE6Ns41GFH0 @ 00:05:07]. EMS '
                              'Healthcare Informatics confirms the 835 rides with the check or EFT but '
                              'sometimes arrives separated, and either way it tells you what was paid, '
                              'what was not, and why [JfPjIRaIz-o @ 00:00:38].',
                              'The group code is where the money gets assigned to a pocket, and every '
                              'instructor treats CO versus PR as the line you never cross. Health Weave '
                              'RCM spells out the five groups: CO is contractual obligation and a '
                              'write-off you cannot bill the patient for, PR is patient responsibility '
                              'covering deductible, coinsurance, copay and sometimes non-covered services, '
                              'OA is other adjustment, PI is a payer-initiated reduction that generally is '
                              'not billable to the patient, and CR is correction and reversal [bPFE9F4Y_Y4 '
                              '@ 00:02:43]. PKR Vibes puts it bluntly: if a CO prefix sits on a denied EOB '
                              'and you bill the patient, that is a mistake, while PR1, PR2 and PR3 map to '
                              'deductible, coinsurance and copay [72PuS1BX6_s @ 00:05:37]. Jeremy Zug '
                              'quantifies the stakes: confuse the two and you either bill patients for '
                              'money they do not owe or write off money you should have collected, the '
                              'small five-millimeter adjustments that make a practice unsustainable '
                              '[FE6Ns41GFH0 @ 00:06:33]. Jasmine at Inlera University shows the posting '
                              'consequence: a zero-paid line carrying PR1 with the full allowed amount in '
                              'the deductible column is not a denial, so the patient is held responsible '
                              'while the CO45 difference is written off [-zx82Gn2h04 @ 00:07:30].',
                              'On reason codes the consensus is a two-layer read, never one code in '
                              'isolation. Health Weave RCM calls the CARC the headline and the RARC the '
                              'paragraph underneath, and says read both before deciding: CARCs are '
                              'numbers, there are hundreds, nobody memorizes them all, and RARCs usually '
                              'start with M, A or N, as in M0130 for incomplete or invalid information '
                              "riding with CARC 16 [bPFE9F4Y_Y4 @ 00:05:13]. AarkNine Healthcare's "
                              'walkthrough adds the hierarchy: CARCs are always assigned by the payer, are '
                              'required in the ERA whenever there is an adjustment, and are needed to file '
                              'appeals and resubmissions, while RARCs are alphanumeric, technically '
                              'optional, and act as the instructional memo that turns a vague no into a '
                              'clear do this [3HP5mg0UdCw @ 00:27:24]. AarkNine also places both code sets '
                              'under X12 and CMS management, which is why one vocabulary spans Medicare, '
                              'Medicaid and commercial payers [3HP5mg0UdCw @ 00:29:17]. PKR Vibes ranks '
                              'the remark code as the priority read because it exposes the exact potential '
                              'cause and the corrective action, such as resubmitting with the missing '
                              'referral form, and says an analyst who is good at reading reason and remark '
                              'codes can sometimes close a claim without calling the insurance at all '
                              '[72PuS1BX6_s @ 00:23:49].'],
               'table': {'caption': 'Consensus rules every practitioner applies before posting a '
                                    'remittance',
                         'headers': ['Consensus Point',
                                     'What Practitioners Agree On',
                                     'Operator Implication',
                                     'Expert Source'],
                         'rows': [['CO versus PR group code split on every adjustment line',
                                   'CO is a contractual write-off the patient cannot be billed; PR is '
                                   'deductible, coinsurance, copay or non-covered',
                                   'Never move a CO dollar to the patient ledger; only PR amounts reach '
                                   'the patient balance',
                                   'Health Weave RCM LLC ([bPFE9F4Y_Y4 @ 00:02:43])'],
                                  ['CO45 is the routine contractual adjustment on paid claims',
                                   'CO45 appears on paid claims 99.99 percent of the time as the leftover '
                                   'contractual amount',
                                   'Write off the leftover above the allowed amount instead of chasing it '
                                   'as a denial',
                                   'PKR Vibes Career & Growth ([72PuS1BX6_s @ 00:12:52])'],
                                  ['CARC gives the what, RARC gives the why or next step',
                                   'CARC 27 says coverage terminated; RARC N130 says consult plan benefit '
                                   'documents for dates',
                                   'Read the remark code to find exactly where to look before calling or '
                                   'appealing',
                                   'AarkNine Healthcare ([3HP5mg0UdCw @ 00:23:14])'],
                                  ['Every claim must balance before a single dollar is posted',
                                   'Billed charge minus contractual adjustment minus patient '
                                   'responsibility should equal the payment',
                                   'If the numbers do not balance, do not force them; investigate first',
                                   'Health Weave RCM LLC ([bPFE9F4Y_Y4 @ 00:06:33])'],
                                  ['The TRN trace number links remittance to bank deposit',
                                   'TRN carries the check or EFT number that matches the ERA to the '
                                   'deposit',
                                   'Reconcile by trace number so no remittance sits without its matching '
                                   'money',
                                   'Michael Roberts ([HolIPG8-TV8 @ 00:00:55])'],
                                  ['A zero paid amount is not automatically a denial',
                                   'Zero-paid lines carrying PR1 are being applied to the patient '
                                   'deductible, not denied',
                                   'Bill the patient the deductible amount and write off only the CO45 '
                                   'portion',
                                   'Inlera University ([-zx82Gn2h04 @ 00:00:19])'],
                                  ['Contract and fee schedule outrank the remittance as truth',
                                   'The remittance is a source of truth, but the contract and fee schedule '
                                   'are the ultimate truth',
                                   'Match every remittance against the contract to catch payer '
                                   'underpayments early',
                                   'The Claim Game X Practice Solutions ([FE6Ns41GFH0 @ 00:15:52])']]}},
              {'section_number': 2,
               'heading': 'Exact Street Mechanics, Tools & Numbers: Reading the 835 and Posting to the '
                          'Penny',
               'paragraphs': ['Start with the raw file, because EMS Healthcare Informatics insists anyone '
                              'can open it. An 835 is a plain, unencrypted text file with no mandatory '
                              'naming convention, so a .txt or .dat opens in Notepad or WordPad, but never '
                              'edit it in a Word-style editor because its formatting breaks a file that '
                              'must stay pure [JfPjIRaIz-o @ 00:01:53]. It arrives as one continuous '
                              'string, built from hierarchical loops, segments of related fields, and '
                              'elements that hold the actual data, split by delimiters: the asterisk is '
                              'the most common element separator and the tilde the most common segment '
                              'separator. The trick: in a text editor with global search-and-replace, key '
                              'off the tilde and insert a carriage return so each segment lands on its own '
                              'line [JfPjIRaIz-o @ 00:05:25]. The decoder is the implementation guide, the '
                              'Bible bought from Washington Publishing and described as quite expensive. '
                              'Walk the CLP line with it: CLP01 is your patient control number, CLP02 '
                              'status where 2 means processed as secondary, CLP03 total charge, CLP04 '
                              'total paid, CLP05 patient responsibility, CLP06 filing indicator such as '
                              'HM, and CLP07 the payer claim control number [JfPjIRaIz-o @ 00:07:45]. '
                              'Michael Roberts, teaching as Professor Remit, adds that status 1 means '
                              'processed as primary [HolIPG8-TV8 @ 00:00:55].',
                              'Michael Roberts then walks a full sample ERA top to bottom, promising you '
                              'will know exactly where your money went. ISA, GS and ST are the envelope '
                              'you can mostly wave past; BPR is the payment line, here $1,250 sent by ACH '
                              'on November 5th; TRN is the check or EFT trace number used to match the '
                              'deposit; N1 PR is the payer and N1 PE is the practice with its NPI '
                              '[HolIPG8-TV8 @ 00:00:33]. The claim: CLP charges $200, pays $120, patient '
                              'owes $20; SVC 99213 office visit; CAS CO45 for $60 written off and PR2 for '
                              '$20 coinsurance; AMT B6 allowed of $140. His balance check is $200 minus '
                              '$60 equals $140 allowed, and $120 paid plus $20 patient equals $140 '
                              '[HolIPG8-TV8 @ 00:01:39]. Then the trap segment: PLB near the end pulls '
                              'money from the whole payment, his sample being a $25 overpayment recovery, '
                              'which is why a check can be smaller than its claims [HolIPG8-TV8 @ '
                              '00:02:04]. Jeremy Zug describes the same hole from the posting floor: bill '
                              '$100, the payer pays $80, the check says $70, and the missing $10 is buried '
                              'in a PLB recoupment for an error from three months ago, which on volume '
                              'makes a huge difference [FE6Ns41GFH0 @ 00:08:18].',
                              'Posting is where the decoding becomes cash control, and the speakers want '
                              'proof before a dollar counts. InfiMed Health runs it as six software agents '
                              'under an orchestrator: an 835 parser, ERA matching to claim and account, '
                              'contract variance detection, patient balance allocation using the '
                              'adjustment codes, bank deposit matching by trace number, and exception '
                              'routing, with two rules, posted means proven and people own write-offs, '
                              'refunds and underpayment disputes [uO7nW5fy5Y4 @ 00:01:25]. Health Weave '
                              "RCM's manual version: match the deposit total to the remittance before "
                              'closing the batch, post contractual, patient and payment amounts to '
                              'separate buckets, check the math on every claim, and watch for '
                              'provider-level recoupments [bPFE9F4Y_Y4 @ 00:09:19]. When a deposit lands '
                              "with no ERA, Jeremy Zug's move is the payer portal, Availity, Optum or "
                              'payer sites like Navanet, to download a PDF remittance and match it to the '
                              'cash before posting, instead of 45 minutes of hold music; portals also take '
                              'online corrections that process in days instead of 30 [FE6Ns41GFH0 @ '
                              "00:11:31]. For bulk triage, EMS's EDI Power Reader, a desktop application "
                              'that opens files like a spreadsheet, collapses the hierarchy into claim and '
                              'detail grids, filters to denied claims sorted by descending dollars, and '
                              'exports everything to Excel [JfPjIRaIz-o @ 00:16:10].'],
               'table': {'caption': '835 segments, claim-form boxes and tools operators work with, with '
                                    'the exact numbers taught',
                         'headers': ['Segment or Tool',
                                     'What It Carries or Does',
                                     'Exact Numbers Taught',
                                     'Expert Source'],
                         'rows': [['BPR payment segment near the top of the 835',
                                   'Carries the total of the whole check or EFT for the file',
                                   'Sample shows $1,250 sent by ACH on November 5th',
                                   'Michael Roberts ([HolIPG8-TV8 @ 00:00:33])'],
                                  ['TRN trace number segment following the payment line',
                                   'Holds the check or EFT number used to match the ERA to the deposit',
                                   'One trace number ties each remittance to its bank deposit',
                                   'Michael Roberts ([HolIPG8-TV8 @ 00:00:55])'],
                                  ['CAS adjustment segments on each service line',
                                   'Group code plus reason code plus amount explaining every unpaid dollar',
                                   'CO45 $60 written off and PR2 $20 coinsurance on a $200 charge',
                                   'Michael Roberts ([HolIPG8-TV8 @ 00:01:39])'],
                                  ['PLB provider-level adjustment at the bottom of the ERA',
                                   'Recoupments taken from the whole payment rather than from one claim',
                                   '$100 billed, $80 paid, $70 check, with the missing $10 buried in PLB',
                                   'The Claim Game X Practice Solutions ([FE6Ns41GFH0 @ 00:08:18])'],
                                  ['REF healthcare policy identification segment in Loop 2110',
                                   'REF01 qualifier plus REF02 identifier for each paid service line',
                                   'F8 qualifier pairs with patient control number 123456789 in the sample',
                                   'Vikash Learning ([MWf66u11yb8 @ 00:05:04])'],
                                  ['EDI Power Reader desktop application from EMS',
                                   'Collapses loops into linear claim and detail grids with sorting, '
                                   'filters and export',
                                   'Demo claim for Mitch Miller broke out into five procedure lines',
                                   'EDI PowerTools by EMS Healthcare Informatics ([JfPjIRaIz-o @ '
                                   '00:15:52])'],
                                  ['CMS-1500 denial map for professional claims',
                                   'Box 23 for authorization, box 21 and 24E for diagnosis, 24D for CPT or '
                                   'modifier, box 33 billing provider',
                                   'Form has 33 numbered boxes; read only those tied to the denial',
                                   'JobRath ([I__wJbnhlTw @ 00:05:59])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Posting-Desk Moves That Stop Money Leaking',
                           'body': 'Street-level reads the speakers use to separate routine adjustments '
                                   'from recoverable dollars before anything hits the ledger.',
                           'items': ['Never read a zero paid amount as a denial: if the allowed amount '
                                     'equals the deductible column and the line carries PR1, post it to '
                                     'the patient [Inlera University — -zx82Gn2h04 @ 00:04:18]',
                                     'Read the allowed amount, not just the paid amount; if the '
                                     'contractual adjustment is off, either your fee schedule is wrong or '
                                     'the payer is underpaying you [The Claim Game X Practice Solutions — '
                                     'FE6Ns41GFH0 @ 00:05:40]',
                                     'Track which reason codes recur; when the same one keeps showing up, '
                                     'the fix is the upstream cause, not more resubmitting [Health Weave '
                                     'RCM LLC — bPFE9F4Y_Y4 @ 00:09:51]',
                                     'Check professional and facility claims together: an inpatient POS on '
                                     'a CMS-1500 without the matching UB-04 gets both claims denied '
                                     'instantly [RCMOpsPro — Y-cwIjpRq9w @ 00:01:10]']},
               'sop_steps': [{'step': 1,
                              'title': 'Make the raw 835 readable',
                              'action': 'Open the 835 in a plain text editor and break it into one segment '
                                        'per line.',
                              'detail': 'Key off the tilde segment separator with a global '
                                        'search-and-replace and insert a carriage return, then read each '
                                        'two- or three-character segment ID against the implementation '
                                        'guide; never edit the file in a Word-style editor [EDI PowerTools '
                                        'by EMS Healthcare Informatics — JfPjIRaIz-o @ 00:05:25]'},
                             {'step': 2,
                              'title': 'Balance every claim before posting',
                              'action': 'Run the charge-minus-adjustments check on each claim and service '
                                        'line.',
                              'detail': 'Billed charge minus the contractual adjustment minus patient '
                                        'responsibility must equal the payment, as in $200 - $80 - $100 = '
                                        '$20; if it does not balance, investigate before posting [Health '
                                        'Weave RCM LLC — bPFE9F4Y_Y4 @ 00:06:33]'},
                             {'step': 3,
                              'title': 'Reconcile the ERA to the bank deposit',
                              'action': 'Match the TRN trace number to the EFT and hunt down any PLB gap.',
                              'detail': 'Use TRN to tie the ERA to the deposit, then check PLB near the '
                                        'end for recoupments such as a $25 overpayment recovery that make '
                                        'the check smaller than its claims [Michael Roberts — HolIPG8-TV8 '
                                        '@ 00:02:04]'},
                             {'step': 4,
                              'title': 'Route every adjustment to the right bucket',
                              'action': 'Write off CO, hold PR for the secondary, and fix-and-resubmit '
                                        'data denials.',
                              'detail': "Send the primary's payment and adjustments to the secondary payer "
                                        'and bill the patient only after both payers process, or you may '
                                        'collect money the secondary would have paid and have to refund it '
                                        '[Health Weave RCM LLC — bPFE9F4Y_Y4 @ 00:08:25]'}]},
              {'heading': 'Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The sharpest split on the remit floor is what a single code actually means. '
                              'Health Weave RCM LLC teaches CO45 as the normal contractual write-off: the '
                              'charge exceeded the contracted amount, the provider absorbs the difference, '
                              'and the patient is never billed for it [bPFE9F4Y_Y4 @ 00:03:54]. Vikash '
                              'Learning runs a partial-rejection scenario where the same CO45, paired with '
                              "remark code M15, signifies the procedure is not covered by the patient's "
                              'policy and is grouped with another service, so separate payment is not '
                              'allowed; that reading pushes the provider to notify the patient of the '
                              'non-covered service and possibly contest the denial [MWf66u11yb8 @ '
                              '00:02:00]. Remark code MA18 splits the room the same way. PKR Vibes Career '
                              '& Growth says Medicare drops MA18 alongside CO45 on a paid claim to signal '
                              "the claim crossed over to the patient's supplementary insurance, and "
                              'stresses it is not a denial [72PuS1BX6_s @ 00:21:45]. AarkNine Healthcare '
                              'reads MA18 as a claim adjustment because of late filing, riding next to '
                              'CARC 29 to underline a timely filing denial [3HP5mg0UdCw @ 00:19:55]. The '
                              'operator takeaway is to read the pairing rather than any code in isolation, '
                              "and to confirm the payer's own definition before posting a write-off, a "
                              'patient balance, or a crossover expectation.',
                              'How much weight the remark code deserves is the second fault line. PKR '
                              'Vibes Career & Growth ranks the remark code above the denial code, arguing '
                              'the RARC is where you find the exact potential cause of the claim, and adds '
                              'that RARCs show up on denied EOBs while paid claims carry CARCs like CO45 '
                              'without one [72PuS1BX6_s @ 00:16:03]. The same channel later describes MA18 '
                              'riding with CO45 on a Medicare paid claim, so even inside one playbook the '
                              'no-remark-on-paid rule bends. AarkNine Healthcare flips the hierarchy: '
                              'CARCs are required in the electronic remittance advice whenever there is an '
                              'adjustment, while RARCs are technically optional, so an absent remark does '
                              'not mean the claim is unexplained [3HP5mg0UdCw @ 00:27:24]. Health Weave '
                              'RCM LLC splits the difference with a newsroom model, calling the CARC the '
                              'headline and the RARC the paragraph underneath, ordering billers to read '
                              'both before deciding what to do, and flagging M0130 riding with CARC 16 as '
                              'the classic unprocessable-data pairing [bPFE9F4Y_Y4 @ 00:05:13]. On the '
                              'floor the playbooks converge: the CARC routes the work queue, and the '
                              'remark, when present, tells the follow-up desk which document, field, or '
                              'plan rule to chase before anyone picks up a phone or resubmits.',
                              'The third split is human judgment versus machine throughput, and who to '
                              'call when a remit makes no sense. RCMOpsPro draws a hard line: a basic data '
                              'entry clerk relies on the software to catch errors, while an elite RCM '
                              'analyst spots a formatting failure on a raw claim before it ever reaches '
                              'the clearinghouse [Y-cwIjpRq9w @ 00:01:10]. InfiMed Health goes the other '
                              'way on labor, running payment posting as one workflow with six specialist '
                              'software agents under an orchestrator, but it fences the cash with two '
                              'rules: posted means proven, and write-offs, refunds and underpayment '
                              'disputes stay with the finance team [uO7nW5fy5Y4 @ 00:02:06]. On '
                              'escalation, Medical Billing Maven still picks up the phone, reporting that '
                              'remittance advice from smaller insurers the speaker rarely works with is '
                              'hard to read and requires a representative to explain the figures, while '
                              'Cigna, Blue Cross Blue Shield, UnitedHealthcare and Medicare usually read '
                              'clean [GhRz1M9lxtc @ 00:10:03]. The Claim Game X Practice Solutions calls '
                              'that habit billing in hard mode for anything routine, pushing Availity, '
                              'Optum and payer sites like Navanet as a direct line into the payer database '
                              'instead of 45 minutes of distorted hold music [b2mkUKtTWnE @ 00:10:28]. Run '
                              'portals first, and keep the phone for the oddball payer whose layout '
                              'defeats the team.'],
               'table': {'caption': 'Competing readings and playbooks on codes, escalation and tooling',
                         'headers': ['Disagreement', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['What CO45 actually signals on a remittance line',
                                   'Normal contractual write-off where the charge exceeded the contracted '
                                   'amount',
                                   'Paired with M15, signals a non-covered service bundled into another '
                                   'service',
                                   'Health Weave RCM LLC ([bPFE9F4Y_Y4 @ 00:03:54]); Vikash Learning '
                                   '([MWf66u11yb8 @ 00:02:00])'],
                                  ['What remark code MA18 means when it appears',
                                   'Medicare crossover to supplementary insurance on a paid CO45 claim, '
                                   'not a denial',
                                   'Late filing adjustment that underlines a CARC 29 timely filing denial',
                                   'PKR Vibes Career & Growth ([72PuS1BX6_s @ 00:21:45]); AarkNine '
                                   'Healthcare ([3HP5mg0UdCw @ 00:19:55])'],
                                  ['Which group prefix carries a timely filing denial',
                                   'Some insurers send the timely filing denial under the CO prefix',
                                   'Other insurers send the same timely filing denial under a PI prefix',
                                   'PKR Vibes Career & Growth ([72PuS1BX6_s @ 00:07:46])'],
                                  ['Whether the CARC or the RARC drives the work',
                                   'Remark code is the priority because it shows the exact potential cause',
                                   'CARC is mandatory on every adjustment while the RARC is technically '
                                   'optional',
                                   'PKR Vibes Career & Growth ([72PuS1BX6_s @ 00:16:03]); AarkNine '
                                   'Healthcare ([3HP5mg0UdCw @ 00:27:24])'],
                                  ['Who catches formatting and posting errors before they cost money',
                                   'Elite analyst spots formatting failures on the raw claim before the '
                                   'clearinghouse',
                                   'Six software agents run posting while finance owns write-offs, refunds '
                                   'and disputes',
                                   'RCMOpsPro ([Y-cwIjpRq9w @ 00:01:10]); InfiMed Health ([uO7nW5fy5Y4 @ '
                                   '00:02:06])'],
                                  ['How to resolve a confusing remittance from a payer',
                                   'Call a representative for smaller insurers whose remittance layouts '
                                   'are hard to read',
                                   'Skip routine calls and use Availity, Optum or Navanet portals instead',
                                   'Medical Billing Maven ([GhRz1M9lxtc @ 00:10:03]); The Claim Game X '
                                   'Practice Solutions ([b2mkUKtTWnE @ 00:10:28])'],
                                  ['How deep an operator must go into raw 835 structure',
                                   'Insert carriage returns at each tilde in a text editor and parse by '
                                   'spec',
                                   'Skip memorizing loop 2100 and work from printed EOB and ERA component '
                                   'guides',
                                   'EDI PowerTools by EMS Healthcare Informatics ([JfPjIRaIz-o @ '
                                   '00:05:09]); The Claim Game X Practice Solutions ([b2mkUKtTWnE @ '
                                   '00:16:11])']]}},
              {'heading': 'Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The costliest trap is the check that does not match its claims. Michael '
                              'Roberts, speaking as Professor Remit, flags the PLB segment near the end of '
                              'the 835 that takes money from the whole payment, using a $25 overpayment '
                              'recovery, and warns it is easy to miss and is why a check can be smaller '
                              'than its claims [HolIPG8-TV8 @ 00:02:04]. The Claim Game X Practice '
                              'Solutions puts numbers on the same leak: you billed $100, they paid 80, but '
                              'the check was only $70, and the missing $10 is buried in a provider level '
                              'adjustment, often a recoupment for an error from three months earlier, '
                              'which is why autoposting cannot be set and forgotten [FE6Ns41GFH0 @ '
                              '00:08:18]. Health Weave RCM LLC adds that if you overlook these provider '
                              'level adjustments, your deposit and your postings will never reconcile '
                              '[bPFE9F4Y_Y4 @ 00:09:51]. InfiMed Health lists the failure shapes that hide '
                              'in plain sight: a remittance with no matching deposit, one deposit covering '
                              'hundreds of claims, a payment lower than the contract says with nobody '
                              'noticing, and an adjustment billed to the patient by mistake [uO7nW5fy5Y4 @ '
                              '00:00:43]. Each one leaves the books wrong or the clinic underpaid.',
                              'The second cluster of losses lands on the patient ledger. Health Weave RCM '
                              'LLC says that if you remember one thing, remember CO versus PR, because '
                              'confusing the two is how patients end up billed for write-offs [bPFE9F4Y_Y4 '
                              '@ 00:03:18]. The same channel adds a sequencing trap: bill the patient '
                              "before the secondary payer has processed the primary's leftover deductible, "
                              'coinsurance or copay, and you may collect money the secondary would have '
                              'paid and then have to refund it [bPFE9F4Y_Y4 @ 00:08:25]. The Claim Game X '
                              'Practice Solutions frames the CO and PR confusion as a two-way bleed: you '
                              'bill the patient for money they do not owe, or you write off money you '
                              'should have collected, the small adjustments that chip away until the '
                              'practice is unsustainable [FE6Ns41GFH0 @ 00:06:33]. Inlera University '
                              'catches the mirror-image mistake, where a paid amount of zero gets assumed '
                              'to be a denial even though the PR1 code and a deductible column equal to '
                              'the full allowed amount show the claim was applied to the deductible and '
                              'the patient owes it, while the CO45 gap between billed and allowed gets '
                              'written off [-zx82Gn2h04 @ 00:04:18]. Posting the wrong bucket in either '
                              'direction either strands collectible cash or sends a write-off to a '
                              'patient.',
                              'Upstream, the failures are structural and the economics compound. RCMOpsPro '
                              "reports that if the hospital software fails to map a patient's secondary "
                              'insurance data into the specific loop and segment the 837 requires, the '
                              'claim instantly crashes, which is why the file must clear aggressive '
                              'internal edit checks before leaving the network [0ElxFXefBcA @ 00:01:03]. '
                              'JobRath shows how a claim for a correctly performed service still gets '
                              'rejected or denied when the CPT is right but the diagnosis pointer in box '
                              '24E is wrong or the rendering provider NPI is missing or invalid '
                              '[I__wJbnhlTw @ 00:02:24]. AarkNine Healthcare puts a price on timing: '
                              'deadlines often run 90 to 180 days from the date of service, one day late '
                              'triggers CARC 29, and a batch delayed a week by a software glitch or '
                              'staffing shortage can wipe out a substantial chunk of monthly revenue as '
                              'write-offs [3HP5mg0UdCw @ 00:09:40]. The Claim Game X Practice Solutions '
                              'found a large agency being underpaid 75 cents to a dollar per claim, small '
                              'per line but a giant difference on volume; after documenting the case the '
                              'payer paid the difference, and the 60-day project dropped accounts '
                              'receivable 30 to 40 percent, speed that only existed because every payment '
                              'had moved to ERAs [b2mkUKtTWnE @ 00:13:53].'],
               'table': {'caption': 'Firsthand failure modes, what broke, and the economic hit or fix',
                         'headers': ['Failure Mode',
                                     'What Went Wrong',
                                     'Economic Hit Or Fix',
                                     'Expert Source'],
                         'rows': [['PLB provider level adjustment missed at the bottom of the 835',
                                   'Check came in smaller than its claims because a $25 overpayment '
                                   'recovery came off the top',
                                   'Deposit and postings never reconcile until every provider level '
                                   'adjustment is worked',
                                   'Michael Roberts ([HolIPG8-TV8 @ 00:02:04]); Health Weave RCM LLC '
                                   '([bPFE9F4Y_Y4 @ 00:09:51])'],
                                  ['Autoposting set and forgotten on incoming ERA files',
                                   'Billed $100, paid 80, but the check was $70 with $10 buried in PLB',
                                   'Mishandled recoupments leave billing ledgers a total mess by the end '
                                   'of the year',
                                   'The Claim Game X Practice Solutions ([FE6Ns41GFH0 @ 00:08:18])'],
                                  ['Contractual write-off billed straight to the patient',
                                   'CO confused with PR so a provider write-off lands on the patient '
                                   'statement',
                                   'Bill only PR amounts and never bill a patient for a contractual '
                                   'write-off',
                                   'Health Weave RCM LLC ([bPFE9F4Y_Y4 @ 00:03:18])'],
                                  ['Patient billed before the secondary payer finishes processing',
                                   'Primary leftover deductible, coinsurance or copay billed to the '
                                   'patient too early',
                                   'Practice collects money the secondary would have paid and then must '
                                   'refund it',
                                   'Health Weave RCM LLC ([bPFE9F4Y_Y4 @ 00:08:25])'],
                                  ['Secondary insurance mapped wrong into the outgoing 837 file',
                                   'EHR mapping fails to place secondary insurance in the required loop '
                                   'and segment',
                                   'Claim instantly crashes unless aggressive internal edit checks catch '
                                   'it first',
                                   'RCMOpsPro ([0ElxFXefBcA @ 00:01:03])'],
                                  ['Professional and facility claims billed out of sync',
                                   'CMS-1500 billed with an inpatient POS code but matching UB-04 never '
                                   'billed',
                                   'Payer flags the mismatch and denies both claims instantly with no '
                                   'partial payment',
                                   'RCMOpsPro ([Y-cwIjpRq9w @ 00:01:10])'],
                                  ['Claim batch filed past the payer timely filing deadline',
                                   'Software glitch or staffing shortage pushes claims a week late into '
                                   'CARC 29',
                                   'Substantial chunk of monthly revenue becomes write-offs the clinic '
                                   'cannot collect',
                                   'AarkNine Healthcare ([3HP5mg0UdCw @ 00:09:40])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'No Batch Closes Until The Money Proves Out',
                           'body': 'Do not close a payment batch or post a single dollar to a patient '
                                   'balance until these four checks clear on every remittance.',
                           'items': ['Match the total deposited to the total on the remittance and work '
                                     'every PLB recoupment line before closing the batch [Health Weave RCM '
                                     'LLC — bPFE9F4Y_Y4 @ 00:09:19].',
                                     'Run the balance check on each claim: charged minus contractual '
                                     'equals allowed, and paid plus patient share equals allowed, or stop '
                                     'and investigate [Michael Roberts — HolIPG8-TV8 @ 00:01:39].',
                                     'Never post an EFT that arrived without its remittance; pull the PDF '
                                     'remittance from the payer portal and match it to the cash first [The '
                                     'Claim Game X Practice Solutions — FE6Ns41GFH0 @ 00:11:04].',
                                     'Never edit a raw 835 in a Word-type document editor, because the '
                                     'formatting corrupts a file that has to be kept pure [EDI PowerTools '
                                     'by EMS Healthcare Informatics — JfPjIRaIz-o @ 00:01:53].']}}],
 'pull_quote': '"First: posted means proven. A payment only counts as reconciled once the remittance, the '
               'account and the deposit agree." InfiMed Health (uO7nW5fy5Y4 @ 00:02:06).',
 'diagram_id': 'diag-06',
 'action_checklist': ['Enroll for ERA and EFT as one of the first setup steps with every new payer so '
                      'payments and explanations arrive electronically instead of as paper checks [Health '
                      'Weave RCM LLC — bPFE9F4Y_Y4 @ 00:09:02].',
                      'Use the TRN trace number on each 835 to match the ERA to the exact check or EFT '
                      'deposit in the bank [Michael Roberts — HolIPG8-TV8 @ 00:00:33].',
                      'Sort every adjustment into normal codes like 45 versus action items like 16 and 197 '
                      'before deciding to write off, fix, or resubmit [Health Weave RCM LLC — bPFE9F4Y_Y4 '
                      '@ 00:04:53].',
                      'Track CARC volume by payer and procedure to spot trends such as a spike in CARC 45 '
                      'that signals a pricing or contract renegotiation problem [AarkNine Healthcare — '
                      '3HP5mg0UdCw @ 00:32:52].',
                      'Map the payer claim ID on the remittance to the EHR claim ID and compare the '
                      'allowed amount against the fee schedule to catch underpayments [The Claim Game X '
                      'Practice Solutions — b2mkUKtTWnE @ 00:05:07].',
                      'Work each denial from the matching CMS-1500 box: 1 to 11 for eligibility, 23 for '
                      'authorization, 21 and 24E for diagnosis, 24J for rendering and 33 for billing '
                      'provider [JobRath — I__wJbnhlTw @ 00:05:59].'],
 'statutory_citations': [{'title': 'Health Weave RCM LLC — EOB vs ERA CARC RARC Codes Explained | Medical '
                                   'Billing Class 4 [00:03:18]',
                          'url': 'https://www.youtube.com/watch?v=bPFE9F4Y_Y4&t=198s',
                          'relevance': 'Primary practitioner testimony on CO versus PR group codes, the '
                                       'balancing math, and the secondary billing refund trap.'},
                         {'title': 'Michael Roberts — 835 ERA Line by Line    and introducing Professor '
                                   'Remit [00:02:04]',
                          'url': 'https://www.youtube.com/watch?v=HolIPG8-TV8&t=124s',
                          'relevance': 'Primary practitioner testimony on reading 835 segments line by '
                                       'line and catching PLB recoveries that shrink the check.'},
                         {'title': 'The Claim Game X Practice Solutions — Episode 29: Revenue Cycle '
                                   'Management Explained: Remittances, ERAs, and Portals [00:08:18]',
                          'url': 'https://www.youtube.com/watch?v=FE6Ns41GFH0&t=498s',
                          'relevance': 'Primary practitioner testimony on autoposting risk, provider level '
                                       'adjustments, portals, and a recovered underpayment case.'},
                         {'title': 'InfiMed Health — Payment Posting and Reconciliation Explained: From '
                                   '835 to Bank Deposit [00:02:06]',
                          'url': 'https://www.youtube.com/watch?v=uO7nW5fy5Y4&t=126s',
                          'relevance': 'Primary practitioner testimony on the six-step remittance to '
                                       'deposit reconciliation workflow and human ownership of money '
                                       'decisions.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'JfPjIRaIz-o',
                       'title': 'How to read an 835 Electronic Remittance File',
                       'channel': 'EDI PowerTools by EMS Healthcare Informatics',
                       'author': 'EDI PowerTools by EMS Healthcare Informatics',
                       'text': "Because it's a text file you can open them with any text editor, but do "
                               'not try to edit using a Microsoft Word type document editor because they '
                               'are formatters as well and these need to be kept pure.',
                       'tip': "Because it's a text file you can open them with any text editor, but do not "
                              'try to edit using a Microsoft Word type document editor because they are '
                              'formatters as well and these need to be kept pure.',
                       'timestamp': 113,
                       'timestamp_seconds': 113,
                       'timestamp_label': '[00:01:53]',
                       'url': 'https://www.youtube.com/watch?v=JfPjIRaIz-o&t=113s',
                       'markdown': '[00:01:53](https://www.youtube.com/watch?v=JfPjIRaIz-o&t=113s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '72PuS1BX6_s',
                       'title': '#DENIALCODE AND REMARK CODE IN MEDICAL BILLING #ushealthcare #REMARKCODES '
                                '#CARC #RARC #denialcodes',
                       'channel': 'PKR Vibes Career & Growth',
                       'author': 'PKR Vibes Career & Growth',
                       'text': 'Remark code is a priority; by seeing the remark code we can find out the '
                               'exact potential cause of the claim.',
                       'tip': 'Remark code is a priority; by seeing the remark code we can find out the '
                              'exact potential cause of the claim.',
                       'timestamp': 963,
                       'timestamp_seconds': 963,
                       'timestamp_label': '[00:16:03]',
                       'url': 'https://www.youtube.com/watch?v=72PuS1BX6_s&t=963s',
                       'markdown': '[00:16:03](https://www.youtube.com/watch?v=72PuS1BX6_s&t=963s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'MWf66u11yb8',
                       'title': 'What is CARC, RARC, & 835 Healthcare Policy Identification Segment?',
                       'channel': 'Vikash Learning',
                       'author': 'Vikash Learning',
                       'text': 'CARC code CO45, RARC code M15: the CO45 code signifies that the procedure '
                               "is not covered by the patient's insurance policy.",
                       'tip': 'CARC code CO45, RARC code M15: the CO45 code signifies that the procedure '
                              "is not covered by the patient's insurance policy.",
                       'timestamp': 120,
                       'timestamp_seconds': 120,
                       'timestamp_label': '[00:02:00]',
                       'url': 'https://www.youtube.com/watch?v=MWf66u11yb8&t=120s',
                       'markdown': '[00:02:00](https://www.youtube.com/watch?v=MWf66u11yb8&t=120s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'bPFE9F4Y_Y4',
                       'title': 'EOB vs ERA CARC RARC Codes Explained | Medical Billing Class 4',
                       'channel': 'Health Weave RCM LLC',
                       'author': 'Health Weave RCM LLC',
                       'text': 'If you remember only one thing from this section, remember CO versus PR; '
                               'getting those two confused is how patients end up billed for write-offs.',
                       'tip': 'If you remember only one thing from this section, remember CO versus PR; '
                              'getting those two confused is how patients end up billed for write-offs.',
                       'timestamp': 198,
                       'timestamp_seconds': 198,
                       'timestamp_label': '[00:03:18]',
                       'url': 'https://www.youtube.com/watch?v=bPFE9F4Y_Y4&t=198s',
                       'markdown': '[00:03:18](https://www.youtube.com/watch?v=bPFE9F4Y_Y4&t=198s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'bPFE9F4Y_Y4',
                       'title': 'EOB vs ERA CARC RARC Codes Explained | Medical Billing Class 4',
                       'channel': 'Health Weave RCM LLC',
                       'author': 'Health Weave RCM LLC',
                       'text': 'If you bill the patient too early, you may collect money that the '
                               'secondary insurance would have paid, and then have to refund it.',
                       'tip': 'If you bill the patient too early, you may collect money that the secondary '
                              'insurance would have paid, and then have to refund it.',
                       'timestamp': 505,
                       'timestamp_seconds': 505,
                       'timestamp_label': '[00:08:25]',
                       'url': 'https://www.youtube.com/watch?v=bPFE9F4Y_Y4&t=505s',
                       'markdown': '[00:08:25](https://www.youtube.com/watch?v=bPFE9F4Y_Y4&t=505s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '3HP5mg0UdCw',
                       'title': 'CARC & RARC Adjustment and Denial codes ll Medical claim denial & '
                                'management ll adjustment #rcm',
                       'channel': 'AarkNine Healthcare',
                       'author': 'AarkNine Healthcare',
                       'text': 'If a claim is submitted even one day after that deadline, the payer will '
                               'deny it, and CARC 29 is the flag for that denial.',
                       'tip': 'If a claim is submitted even one day after that deadline, the payer will '
                              'deny it, and CARC 29 is the flag for that denial.',
                       'timestamp': 564,
                       'timestamp_seconds': 564,
                       'timestamp_label': '[00:09:24]',
                       'url': 'https://www.youtube.com/watch?v=3HP5mg0UdCw&t=564s',
                       'markdown': '[00:09:24](https://www.youtube.com/watch?v=3HP5mg0UdCw&t=564s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '-zx82Gn2h04',
                       'title': 'How to Read an Explanation of Benefits (EOB) & Electronic Remittance '
                                'Advice (ERA) in US Healthcare',
                       'channel': 'Inlera University',
                       'author': 'Inlera University',
                       'text': 'Very often when we see the paid amount of zero we make the assumption that '
                               "the claim has been denied, but in today's examples these claims are "
                               "actually applying towards the patient's deductibles.",
                       'tip': 'Very often when we see the paid amount of zero we make the assumption that '
                              "the claim has been denied, but in today's examples these claims are "
                              "actually applying towards the patient's deductibles.",
                       'timestamp': 241,
                       'timestamp_seconds': 241,
                       'timestamp_label': '[00:04:01]',
                       'url': 'https://www.youtube.com/watch?v=-zx82Gn2h04&t=241s',
                       'markdown': '[00:04:01](https://www.youtube.com/watch?v=-zx82Gn2h04&t=241s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'I__wJbnhlTw',
                       'title': 'What Is CMS-1500 Form in Medical Billing? How to Read It for Denial '
                                'Handling? #medicalbilling #rcm',
                       'channel': 'JobRath',
                       'author': 'JobRath',
                       'text': 'Imagine the CPT code is correct, but the diagnosis pointer is incorrect, '
                               'or the rendering provider NPI is missing or invalid.',
                       'tip': 'Imagine the CPT code is correct, but the diagnosis pointer is incorrect, or '
                              'the rendering provider NPI is missing or invalid.',
                       'timestamp': 144,
                       'timestamp_seconds': 144,
                       'timestamp_label': '[00:02:24]',
                       'url': 'https://www.youtube.com/watch?v=I__wJbnhlTw&t=144s',
                       'markdown': '[00:02:24](https://www.youtube.com/watch?v=I__wJbnhlTw&t=144s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'uO7nW5fy5Y4',
                       'title': 'Payment Posting and Reconciliation Explained: From 835 to Bank Deposit',
                       'channel': 'InfiMed Health',
                       'author': 'InfiMed Health',
                       'text': 'First: posted means proven. A payment only counts as reconciled once the '
                               'remittance, the account and the deposit agree.',
                       'tip': 'First: posted means proven. A payment only counts as reconciled once the '
                              'remittance, the account and the deposit agree.',
                       'timestamp': 126,
                       'timestamp_seconds': 126,
                       'timestamp_label': '[00:02:06]',
                       'url': 'https://www.youtube.com/watch?v=uO7nW5fy5Y4&t=126s',
                       'markdown': '[00:02:06](https://www.youtube.com/watch?v=uO7nW5fy5Y4&t=126s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'JpGm6Pmzrk8',
                       'title': 'Medical Billing Jobs Interview Q&A | Rejection vs Copay vs Deductible '
                                'Explained (2026 Guide)',
                       'channel': 'MediBill Pro',
                       'author': 'MediBill Pro',
                       'text': 'Claim not accepted due to errors, this is basically a rejection.',
                       'tip': 'Claim not accepted due to errors, this is basically a rejection.',
                       'timestamp': 52,
                       'timestamp_seconds': 52,
                       'timestamp_label': '[00:00:52]',
                       'url': 'https://www.youtube.com/watch?v=JpGm6Pmzrk8&t=52s',
                       'markdown': '[00:00:52](https://www.youtube.com/watch?v=JpGm6Pmzrk8&t=52s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'GhRz1M9lxtc',
                       'title': 'ELECTRONIC REMITTANCE ADVICE IN MEDICAL BILLING |WHAT ARE EOBs, RAs AND '
                                'ERAs | BACK TO BASICS PART 3',
                       'channel': 'Medical Billing Maven',
                       'author': 'Medical Billing Maven',
                       'text': 'When I get those remittance advice that are kind of off from these smaller '
                               "insurance companies, sometimes it's hard to read and I have to call a "
                               "representative for them to explain to me what's going on.",
                       'tip': 'When I get those remittance advice that are kind of off from these smaller '
                              "insurance companies, sometimes it's hard to read and I have to call a "
                              "representative for them to explain to me what's going on.",
                       'timestamp': 622,
                       'timestamp_seconds': 622,
                       'timestamp_label': '[00:10:22]',
                       'url': 'https://www.youtube.com/watch?v=GhRz1M9lxtc&t=622s',
                       'markdown': '[00:10:22](https://www.youtube.com/watch?v=GhRz1M9lxtc&t=622s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'HolIPG8-TV8',
                       'title': '835 ERA Line by Line    and introducing Professor Remit',
                       'channel': 'Michael Roberts',
                       'author': 'Michael Roberts',
                       'text': 'Watch for PLB near the end; it takes money from the whole payment, like '
                               'this $25 overpayment recovery, and it is easy to miss and it is why a '
                               'check can be smaller than its claims.',
                       'tip': 'Watch for PLB near the end; it takes money from the whole payment, like '
                              'this $25 overpayment recovery, and it is easy to miss and it is why a check '
                              'can be smaller than its claims.',
                       'timestamp': 124,
                       'timestamp_seconds': 124,
                       'timestamp_label': '[00:02:04]',
                       'url': 'https://www.youtube.com/watch?v=HolIPG8-TV8&t=124s',
                       'markdown': '[00:02:04](https://www.youtube.com/watch?v=HolIPG8-TV8&t=124s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Y-cwIjpRq9w',
                       'title': 'CMS-1500 vs. UB-04 Explained: Mastering the Architecture of Billing | '
                                'Created by Diego Samson',
                       'channel': 'RCMOpsPro',
                       'author': 'RCMOpsPro',
                       'text': 'If a doctor bills a CMS 1500 with an inpatient POS code, but the hospital '
                               'forgets to bill the matching UB-04, the payer will flag the mismatch and '
                               'deny both claims instantly.',
                       'tip': 'If a doctor bills a CMS 1500 with an inpatient POS code, but the hospital '
                              'forgets to bill the matching UB-04, the payer will flag the mismatch and '
                              'deny both claims instantly.',
                       'timestamp': 70,
                       'timestamp_seconds': 70,
                       'timestamp_label': '[00:01:10]',
                       'url': 'https://www.youtube.com/watch?v=Y-cwIjpRq9w&t=70s',
                       'markdown': '[00:01:10](https://www.youtube.com/watch?v=Y-cwIjpRq9w&t=70s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '6Lc5iQMx35E',
                       'title': 'CMS-1500 Claim Form Explained | Complete Guide to Medical Billing | '
                                'RCMPRO',
                       'channel': 'RCMPRO',
                       'author': 'RCMPRO',
                       'text': 'Field 21 lists the diagnoses, field 24D lists the procedures, and field '
                               '24E connects them; getting this connection right is critical for clean '
                               'claims.',
                       'tip': 'Field 21 lists the diagnoses, field 24D lists the procedures, and field 24E '
                              'connects them; getting this connection right is critical for clean claims.',
                       'timestamp': 512,
                       'timestamp_seconds': 512,
                       'timestamp_label': '[00:08:32]',
                       'url': 'https://www.youtube.com/watch?v=6Lc5iQMx35E&t=512s',
                       'markdown': '[00:08:32](https://www.youtube.com/watch?v=6Lc5iQMx35E&t=512s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'FE6Ns41GFH0',
                       'title': 'Episode 29: Revenue Cycle Management Explained: Remittances, ERAs, and '
                                'Portals',
                       'channel': 'The Claim Game X Practice Solutions',
                       'author': 'The Claim Game X Practice Solutions',
                       'text': "That missing $10 is usually buried in something called a PLB segment; it's "
                               'a provider level adjustment at the bottom of the ERA.',
                       'tip': "That missing $10 is usually buried in something called a PLB segment; it's "
                              'a provider level adjustment at the bottom of the ERA.',
                       'timestamp': 498,
                       'timestamp_seconds': 498,
                       'timestamp_label': '[00:08:18]',
                       'url': 'https://www.youtube.com/watch?v=FE6Ns41GFH0&t=498s',
                       'markdown': '[00:08:18](https://www.youtube.com/watch?v=FE6Ns41GFH0&t=498s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'b2mkUKtTWnE',
                       'title': 'Revenue Cycle Management Explained: Remittances, ERAs, and Portals',
                       'channel': 'The Claim Game X Practice Solutions',
                       'author': 'The Claim Game X Practice Solutions',
                       'text': "When you're dealing with the kind of volume that some of you are doing, 75 "
                               'cents or a dollar makes a giant difference.',
                       'tip': "When you're dealing with the kind of volume that some of you are doing, 75 "
                              'cents or a dollar makes a giant difference.',
                       'timestamp': 833,
                       'timestamp_seconds': 833,
                       'timestamp_label': '[00:13:53]',
                       'url': 'https://www.youtube.com/watch?v=b2mkUKtTWnE&t=833s',
                       'markdown': '[00:13:53](https://www.youtube.com/watch?v=b2mkUKtTWnE&t=833s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '0ElxFXefBcA',
                       'title': 'The Claim Drop: Translating the EHR to the 837 Claim File | Created by '
                                'Diego Samson',
                       'channel': 'RCMOpsPro',
                       'author': 'RCMOpsPro',
                       'text': 'If the system mapping is not perfectly configured, clean clinical data '
                               'instantly turns into garbage electronic data.',
                       'tip': 'If the system mapping is not perfectly configured, clean clinical data '
                              'instantly turns into garbage electronic data.',
                       'timestamp': 63,
                       'timestamp_seconds': 63,
                       'timestamp_label': '[00:01:03]',
                       'url': 'https://www.youtube.com/watch?v=0ElxFXefBcA&t=63s',
                       'markdown': '[00:01:03](https://www.youtube.com/watch?v=0ElxFXefBcA&t=63s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'}]}
