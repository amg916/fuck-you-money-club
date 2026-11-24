from __future__ import annotations

CHAPTER_7 = {'id': 'Q7',
 'chapter_id': 'Q7',
 'chapter_number': 7,
 'question_number': 7,
 'slug': 'building-the-510k-submission',
 'question_prompt': 'How is a 510(k) submission actually prepared, reviewed, and kept valid after changes?',
 'kicker': 'Q7 / THE BIG MONEY PLAYBOOKS',
 'title': 'Building the 510(k) Submission',
 'subtitle': 'eSTAR preparation, predicate selection and split predicates, RFDs, design controls, material '
             'compatibility testing, workshops on FDA review, software updates that trigger a new 510(k), '
             'DHF remediation, and CSA risk-based assurance',
 'layout_template': 'thirty_day_roadmap',
 'reading_time_minutes': 15,
 'executive_summary': 'Practitioners converge on one spine for the 510(k): lock the predicate, copy its '
                      "indications for use word-for-word, mirror FDA's guidance headings exactly, and "
                      'treat performance testing as the critical path that drives cost and calendar. Rob '
                      'Packard pegs the RTA screen as the first kill zone, with more than half of '
                      'submissions bounced and the clock reset to zero, while Qualio reports 30% not '
                      'accepted for initial review and 15% failing on the wrong predicate. Street numbers '
                      'run from a $10,953 standard fee (Packard) to almost $20,000 in 2023 (Qualio), '
                      '$13,000 biocompatibility, $50-60k EMC, and consultants at $20K-$25K typical. '
                      'Disagreements center on predicate age, whether pre-subs always pay, whether '
                      'abbreviated or special 510(k)s save time, and how conservative FDA is on software '
                      'changes, as the O.N. Diagnostics warning letter showed.',
 'key_metrics': [{'label': 'RTA First-Pass Rejection Rate',
                  'metric': 'RTA First-Pass Rejection Rate',
                  'value': 'More than 50% of submissions rejected at RTA screening',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Packard reports that more than half of submissions are rejected during '
                             'refuse-to-accept screening, and a rejection resets the review clock to zero.',
                  'source': 'MedicalMarcom ([-ceDuiClggg @ 00:13:03])'},
                 {'label': 'FDA 510(k) User Fee',
                  'metric': 'FDA 510(k) User Fee',
                  'value': '$10,953 standard; $2,738 small business',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Packard's quoted FDA fees, with small-business status requiring "
                             'requalification every year.',
                  'source': 'MedicalMarcom ([-ceDuiClggg @ 00:08:36])'},
                 {'label': 'Wrong-Predicate Failure Rate',
                  'metric': 'Wrong-Predicate Failure Rate',
                  'value': '15% of submissions fail because of the wrong predicate',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Qualio's figure for submissions that fail on predicate selection alone; "
                             'about two-thirds of submissions also receive additional-information '
                             'requests.',
                  'source': 'Qualio ([1GKnWm8UYVk @ 00:59:39])'},
                 {'label': 'Realistic Total Review Time',
                  'metric': 'Realistic Total Review Time',
                  'value': '120-130 days',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Rob's realistic end-to-end clock: 15-day RTA screen, interactive-review "
                             'decision point at day 60, and about 30 days from interactive review to '
                             'decision.',
                  'source': 'MedicalMarcom ([gGje01O9B44 @ 00:11:34])'}],
 'sections': [{'title': "Section 1: The Practitioner Consensus - Predicate First, FDA's Exact Words, "
                        'Testing on the Critical Path',
               'paragraphs': ['Every practitioner who touched predicate selection treats it as the '
                              'load-bearing wall of the file. The Cleared channel opens bluntly: every '
                              '510(k) is built on one comparison, and pick the wrong one and the whole '
                              'comparison can fall apart [6WEZ6ovm-PE @ 00:00:00]. Qualio puts a number on '
                              'the damage, saying 15% of submissions fail because of the wrong predicate, '
                              'while about two-thirds of all files draw additional-information requests '
                              "anyway [1GKnWm8UYVk @ 00:59:39]. Rob Packard's screening rules are the "
                              'operator version: avoid predicates under a consent decree or warning '
                              'letter, and choose the broadest intended use available rather than the '
                              'closest-looking product [gGje01O9B44 @ 00:21:40]. The same agreement covers '
                              "the indications-for-use language. Qualio says copy the predicate's "
                              'indications for use word-for-word, and Packard says copy them and change '
                              'the name, while warning that a technology swap such as pneumatic versus '
                              'mechanical can raise new risks [-ceDuiClggg @ 00:16:52]. Split predicates '
                              'get no support from anyone: decision points one through four ride on a '
                              'single primary device, and any other device in the file is labeled a '
                              'reference, not a predicate. A cleared predicate that has gone off the '
                              'market is still usable, and the Part II workshop speaker reports filing on '
                              'discontinued predicates directly.',
                              'The second point of agreement is that the refuse-to-accept screen kills '
                              "files on form, not science, so the document must mirror FDA's own rule "
                              'book. In the Part I workshop, Packard reports RTA rejecting 56% of '
                              'submissions and tells operators to follow the guidance order with a nice '
                              'big bold heading that uses the exact same words FDA uses, down to copying '
                              "FDA's misspellings, because paraphrasing invites rejection [yIARvVKN5-s @ "
                              '00:13:17]. Medical Device Academy turns the same idea into a template '
                              'method: convert every guidance item into a heading and, where a section '
                              "does not apply, write 'This is not applicable because' rather than deleting "
                              "it [bEKT9pNj8Sg @ 00:15:11]. The workshop's warning example is a condom "
                              "submission rejected as 'patient contacting.' For project control, Packard "
                              'runs an Excel table of contents color-coded red, yellow, blue, and green so '
                              "every section's status is visible at a glance [gGje01O9B44 @ 00:43:41]. Dr. "
                              "David Lim's conference panel lists poor document naming and version control "
                              'as pitfall number five and prescribes an internal final-review checklist '
                              'plus verifying the eSTAR before upload [aZkxlipyWRs @ 00:06:12]. '
                              'Inconsistent device names in headers are a known RTA trigger on their own, '
                              'and Form 3881 should be re-downloaded right before submitting.',
                              'The third consensus is that testing, not writing, sets the calendar and the '
                              'budget. Packard calls performance testing the critical path item in the '
                              'project and estimates it costs about ten times as much as the rest of the '
                              'build [yIARvVKN5-s @ 00:19:37]. In the Joe Hage session the trigger is '
                              "design freeze: 'This is the point at which it gets expensive,' and the play "
                              'is to write in parallel with testing and submit the same day the last test '
                              'report lands [-ceDuiClggg @ 00:06:40]. Dave Saunders adds the scale of what '
                              'sits behind the file: a 510(k) runs 200 to 500 pages while the design '
                              'history file behind it may run about 10,000, and that DHF cannot be created '
                              'retroactively [6w27HXwMbmU @ 00:31:49]. Adam at Matrix One closes the loop '
                              'with the same warning in plainer words, telling teams not to underestimate '
                              'the time a 510(k) needs and to ensure full documentation traceability '
                              'before paying the fee [dd7dQRVr-mQ @ 00:06:17]. Qualio adds that the '
                              'quality system is never submitted and gets no pre-submission audit, yet it '
                              "is still critical, and CS Medical's Kendall Ash describes years of "
                              'traceability, risk documentation, clinical in-use testing, and human '
                              'factors work feeding a single clearance.'],
               'table': {'caption': 'Where the 510(k) practitioners agree: the baseline rules for building '
                                    'a file that survives RTA and review',
                         'headers': ['Consensus Point',
                                     'What Practitioners Report',
                                     'Operator Takeaway',
                                     'Expert Source'],
                         'rows': [['Predicate choice is the load-bearing decision of the file',
                                   '15% of submissions fail on the wrong predicate and two-thirds draw '
                                   'information requests',
                                   'Screen predicates hard before writing a single section of the '
                                   'submission',
                                   'Qualio ([1GKnWm8UYVk @ 00:59:39])'],
                                  ['Indications for use are copied straight from the predicate',
                                   "Copy the predicate's indications for use and change only the device "
                                   'name',
                                   'Flag technology differences like pneumatic versus mechanical as '
                                   'possible new risks',
                                   'MedicalMarcom ([-ceDuiClggg @ 00:16:52])'],
                                  ['Section headings mirror FDA guidance wording exactly',
                                   'RTA rejects 56% of submissions; use the exact same words FDA uses',
                                   'Do not paraphrase headings and follow the guidance order section by '
                                   'section',
                                   'MedicalMarcom ([yIARvVKN5-s @ 00:12:43])'],
                                  ['Inapplicable sections stay in with a written reason',
                                   'Turn every guidance item into a heading and state why it does not '
                                   'apply',
                                   "Write 'This is not applicable because' instead of deleting the section "
                                   'entirely',
                                   'Medical Device Academy ([bEKT9pNj8Sg @ 00:15:11])'],
                                  ['Performance testing is the critical path item in the project',
                                   'Performance testing sections 18-20 plus 7 and 8 cost about ten times '
                                   'more',
                                   'Start testing at design freeze and write the submission in parallel '
                                   'with it',
                                   'MedicalMarcom ([yIARvVKN5-s @ 00:19:37])'],
                                  ['Traceability must already exist inside the design history file',
                                   'Auditors pick a random component and trace it to a user need in under '
                                   '60 seconds',
                                   'Fill every traceability matrix cell because empty cells signal gaps to '
                                   'auditors',
                                   'Dave Saunders ([6w27HXwMbmU @ 00:12:57])'],
                                  ['Pre-submission meeting outlines FDA expectations before money is spent',
                                   'The pre-sub step is optional but really helpful in outlining what FDA '
                                   'expects',
                                   'Book it early because Packard reports 60-75 days waiting for a pre-sub '
                                   'meeting',
                                   'Matrix One ([dd7dQRVr-mQ @ 00:05:39])']]}},
              {'title': 'Section 2: Exact Street Mechanics, Tools & Numbers - Fees, Test Bills, the Review '
                        'Clock, and Build Order',
               'paragraphs': ['The money map starts with the FDA user fee, and the numbers move with the '
                              'year each practitioner quoted. In the Joe Hage session Packard cites '
                              '$10,953 standard and $2,738 for small business, and lays out the testing '
                              'bill that dwarfs it: about $13,000 for biocompatibility, $40k at the low '
                              'end and $50-60k typical for electrical safety and EMC, tens of thousands '
                              'for orthopedic cyclic testing, $100,000-plus for animal studies, and up to '
                              '$3M for a 500-600 patient clinical, with $1M-plus as the ballpark '
                              '[-ceDuiClggg @ 00:10:04]. Qualio puts the 2023 standard fee at almost '
                              '$20,000 and the small-business fee at about $5,000 for firms under $100M, '
                              'requiring Form 3602/3602A plus a tax return, two to six weeks to process, '
                              'and yearly renewal; wholly owned subsidiaries must demonstrate independence '
                              'to claim the discount [1GKnWm8UYVk @ 00:37:33]. In a second Joe Hage '
                              'session Rob quotes consultant fees from $10K to $150K, with most landing '
                              'between $20K and $25K, and prices the job out loud: about 100 hours at $250 '
                              'an hour is 25 grand [gGje01O9B44 @ 01:20:17]. Pre-sub prep runs about 10 '
                              'hours, roughly $2,500, and Packard says pre-sub feedback, while '
                              'non-binding, saves $10k-plus [-ceDuiClggg @ 01:20:57].',
                              'The review clock is the second set of numbers every operator has to run. '
                              'The Part II workshop lays it out by day: receipt by day 7, acceptance or '
                              'RTA by day 15 with a refusal resetting the clock to day 0, substantive '
                              'review ending in an additional-information hold or interactive review by '
                              "day 60, and a decision by day 90 [nUaPO0mfwKI @ 00:29:17]. Rob's realistic "
                              'total is 120 to 130 days, with interactive review running about 30 days to '
                              'decision and the e-copy accepted and assigned a K number within 24 to 48 '
                              'hours once fees are paid a few days early [gGje01O9B44 @ 00:11:34]. The '
                              'highest-leverage trick on this clock is annotating the RTA checklist with '
                              'the exact location of every item; the workshop speaker once got acceptance '
                              'on day 2 doing it, and Rob, who includes a completed checklist in Section 1 '
                              'or Section 21, reports the last two consultant-led files passed RTA on the '
                              "first try [nUaPO0mfwKI @ 00:31:54]. When RTA does bounce a file, Packard's "
                              'move is to phone the reviewer before resubmitting, since RTA can reject the '
                              'same submission multiple times [-ceDuiClggg @ 00:27:35]. Once a hold letter '
                              'lands, there are 180 days to answer, only one hold allowed, and an '
                              'extension available.',
                              'The build order is fixed across the MedicalMarcom sessions. Performance '
                              'testing goes first, then Section 4 indications for use, then device '
                              'description, substantial equivalence, the 510(k) summary, and the executive '
                              "summary dead last; 'Write it last,' as the workshop puts it [yIARvVKN5-s @ "
                              '00:20:07]. Rob names the five critical sections as 4, 5, 10, 11, and 12, '
                              'and the workshop treats sections 1, 3, and 6 as boilerplate while marketing '
                              "owns labeling and the IFU early. Predicate research runs through FDA's own "
                              'databases. Searching product code OSH returned 3 predicates in the '
                              'classification database but 90 in the 510(k) database, and a company '
                              'holding a 510(k) statement must supply a redacted copy within 30 days of '
                              "request [gGje01O9B44 @ 00:20:07]. Qualio's search for pregnancy tests "
                              'turned up 316 predicates and points operators to K-number summaries, the '
                              'three-letter product code, MAUDE, IFUs, and FOIA requests that can take '
                              'years [1GKnWm8UYVk @ 00:15:11]. Packard calls the TPLC database, with '
                              "recent 510(k)s, recalls, a Pareto by failure mode, and MDR links, 'Tens of "
                              "thousands of dollars worth of consulting' [yIARvVKN5-s @ 00:07:13]. "
                              'Registration & Listing confirms the predicate is legally marketed. Keyword '
                              "discipline matters too: 'adhesive' returns 42 results, and searching "
                              "'dental' beats 'implant.'"],
               'table': {'caption': '510(k) street numbers: fees, test bills, timelines, and response '
                                    'windows as the practitioners quote them',
                         'headers': ['Line Item', 'Figure Quoted', 'How Operators Use It', 'Expert Source'],
                         'rows': [['FDA user fee in the Joe Hage session',
                                   '$10,953 standard and $2,738 small business with yearly requalification',
                                   'Apply for small business status every year on August 1st with tax '
                                   'filing',
                                   'MedicalMarcom ([-ceDuiClggg @ 00:08:36])'],
                                  ['FDA user fee quoted for 2023',
                                   'Almost $20,000 standard; about $5,000 small business under $100M',
                                   'File Form 3602/3602A plus a tax return and allow two to six weeks',
                                   'Qualio ([1GKnWm8UYVk @ 00:37:33])'],
                                  ['Electrical safety and EMC test program cost',
                                   '$40k at the low end and $50-60k as the typical range',
                                   'Budget it as a major line next to $13,000 biocompatibility testing',
                                   'MedicalMarcom ([-ceDuiClggg @ 00:10:04])'],
                                  ['Verification and validation testing timelines',
                                   'Electrical 4-6 weeks, software V&V about 2 months, overall V&V 2-6 '
                                   'months',
                                   'Use ISO 17025 labs and expect biocompatibility and aging to take '
                                   'months',
                                   'Qualio ([1GKnWm8UYVk @ 00:30:55])'],
                                  ['Regulatory consultant fees for a full 510(k)',
                                   '$10K to $150K overall, with most landing between $20K and $25K',
                                   'Price the job at about 100 hours at $250 an hour',
                                   'MedicalMarcom ([gGje01O9B44 @ 01:20:17])'],
                                  ['Additional-information hold response window',
                                   '180 days to answer additional information questions after the hold '
                                   'letter',
                                   'Request an extension if the ceiling approaches and check spam folders '
                                   'for letters',
                                   'MedicalMarcom ([nUaPO0mfwKI @ 00:31:21])'],
                                  ['Pre-submission meeting scheduling and format',
                                   '60-75 days waiting for a meeting, with one hour on the call',
                                   'Prefer a teleconference and use email response as the alternative '
                                   'option',
                                   'MedicalMarcom ([-ceDuiClggg @ 00:04:48])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Four moves that shave weeks off the 510(k) clock',
                           'body': 'These are the specific, repeatable plays the practitioners use to '
                                   'clear RTA faster, cut fees, and keep confidential data out of the '
                                   'public record.',
                           'items': ['Annotate the RTA checklist with the location of every item and ship '
                                     'it inside the file; the Part II workshop speaker once got acceptance '
                                     'on day 2 this way [MedicalMarcom — nUaPO0mfwKI @ 00:31:54].',
                                     'Apply for small business qualification every year on August 1st with '
                                     'your tax filing; it takes about 15 minutes, and Packard has seen '
                                     "approval in 5 days against FDA's stated 60 [MedicalMarcom — "
                                     '-ceDuiClggg @ 00:39:20].',
                                     'Send sterilization parameters (SAL 10^-6), not the sterilization '
                                     'test reports, and expect rising scrutiny of cleaning validation '
                                     '[MedicalMarcom — nUaPO0mfwKI @ 00:34:38].',
                                     'In eSTAR, put anything confidential in an attachment, never the text '
                                     'box; the 510(k) summary is the only public attachment [Medical '
                                     'Device Academy — b1Ejw4mhVFU @ 00:27:42].']},
               'sop_steps': [{'step': 1,
                              'title': 'Lock the product code and primary predicate',
                              'action': 'Search the classification and 510(k) databases by three-letter '
                                        'product code, confirm the predicate is legally marketed, and '
                                        'screen out consent decrees and warning letters.',
                              'detail': 'Searching OSH returned 3 predicates in the classification '
                                        'database and 90 in the 510(k) database; choose the broadest '
                                        'intended use and avoid predicates under a consent decree or '
                                        'warning letter [MedicalMarcom — gGje01O9B44 @ 00:20:07].'},
                             {'step': 2,
                              'title': 'Build the test plan at design-input approval',
                              'action': 'Draft the test plan when design inputs are approved, pulling '
                                        'requirements from guidances, standards, 510(k) summaries, and '
                                        'FOIA copies.',
                              'detail': 'Packard builds the test plan at design-input approval and uses '
                                        'four sources because special-controls guidances are hard to find '
                                        'and FDA search is Boolean [MedicalMarcom — -ceDuiClggg @ '
                                        '00:22:55].'},
                             {'step': 3,
                              'title': 'Write sections in the fixed build order',
                              'action': 'Run performance testing first, then indications for use, device '
                                        'description, substantial equivalence, the 510(k) summary, and the '
                                        'executive summary last.',
                              'detail': 'The workshop order is performance, Section 4 IFU, device '
                                        'description, SE, summary, and executive summary written last, '
                                        'with consistent device names in every header [MedicalMarcom — '
                                        'yIARvVKN5-s @ 00:20:07].'},
                             {'step': 4,
                              'title': 'Pre-screen against RTA and submit when the data lands',
                              'action': 'Complete the RTA checklist inside the file, pay fees a few days '
                                        'early, and submit as soon as the final test report arrives.',
                              'detail': "Rob's rule is 'Just go ahead and submit it when you have the "
                                        "data,' with a completed RTA checklist in Section 1 or Section 21 "
                                        '[MedicalMarcom — gGje01O9B44 @ 00:13:09].'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['Rob Packard is the loudest pre-sub advocate on MedicalMarcom. Since the '
                              "2016 guidance changes he always recommends one, says 'it really pays to "
                              "have pre-sub meetings,' prefers a teleconference, and warns that the single "
                              'hour is the whole allotment, with an email response as the alternative '
                              '[-ceDuiClggg @ 00:24:56]. In Q&A he prices the payoff: the feedback is '
                              'non-binding, but it saves $10k or more [-ceDuiClggg @ 01:20:57]. Adam at '
                              "Matrix One lands softer, calling the step optional but 'really helpful in "
                              "outlining the FDA's expectations' [dd7dQRVr-mQ @ 00:05:39]. The "
                              'counter-playbook comes from the Part II workshop speaker, who sometimes '
                              "skips the pre-sub because clients arrive with 'kitchen sink' question "
                              'lists. When a meeting does happen, the move is to bring the physical device '
                              'and ask narrow, specific questions. For fast answers without a formal '
                              'Q-sub, that speaker routes clients to DICE, which takes free, anonymous '
                              'questions by phone [nUaPO0mfwKI @ 00:10:37]. The calendar cost is real: '
                              'Packard clocks 60 to 75 days just waiting for a pre-sub meeting, and his '
                              'longer MedicalMarcom session puts scheduling at 75 to 90 days. Pre-sub prep '
                              'itself runs about 10 hours at $250 an hour, roughly $2,500.',
                              'Predicate age splits the Qualio stage itself. Kelly Stanton treats a '
                              'predicate older than 10 years as a no-go and prefers one under 5, while '
                              "Kyle Rose counters that it is 'not like a 100% rule' [1GKnWm8UYVk @ "
                              '01:01:57]. Discontinued predicates expose an outright contradiction. Qualio '
                              'says a cleared predicate that is off the market is still usable, and the '
                              'Part II workshop speaker says flatly they have used discontinued predicates '
                              '[nUaPO0mfwKI @ 00:08:57]. The 20-year professional behind the Cleared '
                              'channel lists removal from the market alongside misbranding and '
                              'adulteration as disqualifiers [6WEZ6ovm-PE @ 00:01:27]. Stacking predicates '
                              'is the other fight. During the Invent Healthcare webinar, attendee LaVine '
                              "argued that picking the primary predicate is arbitrary, essentially 'flip a "
                              "coin,' and attendee Coombs disputed that different testing methods amount "
                              'to new questions. Marjorie Shulman of CDRH held that split predicates are '
                              "inconsistent with the 510(k) standard and that FDA is 'not insisting on "
                              "multiple predicates' [V3Fob6FXlCo @ 00:16:27]. Cleared lands on the same "
                              'side: decision points 1 through 4 run on one predicate, multiple predicates '
                              'must share an intended use, a primary gets named, and a reference device is '
                              'not a predicate. Its 2023 draft filters add MAUDE, MDR, and MedSun checks '
                              'and a written reason for the choice.',
                              'Adam at Matrix One tells operators to investigate the abbreviated and '
                              'special 510(k), but the practitioners who have filed them are skeptical. '
                              "Kelly Stanton at Qualio warns that the abbreviated option 'takes about "
                              'twice as long as the traditional process for the FDA to review and it '
                              "doesn't require any less work on your part' [1GKnWm8UYVk @ 00:13:07]. The "
                              'Part II workshop speaker agrees it is not faster and pegs abbreviated '
                              'filings at roughly 10% of submissions [nUaPO0mfwKI @ 00:05:40]. The special '
                              '510(k) carries real upside on paper. Rob at MedicalMarcom quotes a 30-day '
                              'review target against 90 days for a traditional, but only one functional '
                              "area of expertise can be involved, and his rule is blunt: 'if you're in "
                              "doubt, submit it as a traditional' [gGje01O9B44 @ 01:27:19]. The cautionary "
                              'file is a nano-metal-coated PEEK cage that ran through Flowchart C as a '
                              'materials change on a tissue-contacting implant. It went in as a special, '
                              "and FDA converted it to a traditional [nUaPO0mfwKI @ 00:06:12]. Packard's "
                              'alternative to shortcut pathways is speed through parallel work. He can '
                              'write a 510(k) in 72 hours, runs the writing alongside testing, and submits '
                              'the same day the last test report arrives, which is how his book promises a '
                              '510(k) in 100 days.'],
               'table': {'caption': 'Competing playbooks on pre-subs, predicates, pathways, and quality '
                                    'tooling',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Whether to hold a pre-submission meeting before testing',
                                   'Always run one since the 2016 changes; non-binding feedback saves $10k '
                                   'or more',
                                   'Sometimes skip it over kitchen-sink questions; use free anonymous DICE '
                                   'phone calls instead',
                                   'MedicalMarcom ([-ceDuiClggg @ 00:24:56]); MedicalMarcom ([nUaPO0mfwKI '
                                   '@ 00:10:37])'],
                                  ['Maximum acceptable age for a predicate device',
                                   'Kelly Stanton: over 10 years is a no-go, and under 5 years is '
                                   'preferred',
                                   "Kyle Rose: predicate age limits are 'not like a 100% rule' in practice",
                                   'Qualio ([1GKnWm8UYVk @ 01:01:57])'],
                                  ['How to choose the primary predicate device',
                                   'Attendee LaVine: choosing the primary predicate is arbitrary, '
                                   'essentially flip a coin',
                                   'FDA: label primary and reference devices; on a tie pick higher class '
                                   'or most similar',
                                   'Invent Healthcare ([V3Fob6FXlCo @ 00:16:27]); Invent Healthcare '
                                   '([V3Fob6FXlCo @ 00:28:25])'],
                                  ['Abbreviated 510(k) treated as a shortcut route',
                                   'Matrix One tells operators to investigate both the abbreviated and '
                                   'special 510(k) routes',
                                   'Qualio: about twice as long to review, with no less work on your part',
                                   'Matrix One ([dd7dQRVr-mQ @ 00:04:26]); Qualio ([1GKnWm8UYVk @ '
                                   '00:13:07])'],
                                  ['Special versus traditional 510(k) filing decision',
                                   'Special targets a 30-day review but allows only one functional area of '
                                   'expertise',
                                   'If in doubt, file traditional; a special PEEK cage was converted to '
                                   'traditional',
                                   'MedicalMarcom ([gGje01O9B44 @ 01:25:50]); MedicalMarcom ([nUaPO0mfwKI '
                                   '@ 00:06:12])'],
                                  ['Paper versus electronic quality and design records',
                                   'Dave Saunders: tiny organizations can start on paper and switch to '
                                   'electronic later',
                                   "Qualio: 'don't do this on paper' and use templates rather than a DIY "
                                   'QMS',
                                   'Dave Saunders ([6w27HXwMbmU @ 00:18:28]); Qualio ([1GKnWm8UYVk @ '
                                   '00:29:23])'],
                                  ['Retraining a cleared software model after clearance',
                                   "David: requiring a new submission for model improvement is 'very "
                                   "strange'",
                                   'Mary: early FDA advice allowed retraining that met original criteria, '
                                   'but it has tightened',
                                   'Innolitics ([UdQw2LB0EYc @ 00:18:42]); Innolitics ([UdQw2LB0EYc @ '
                                   '00:21:06])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The refuse-to-accept screen is where most first submissions die. Packard '
                              "says 'more than 50% of the submissions are rejected during that RTA "
                              "screening,' that the checklist runs 26 to 27 pages, and that a rejection "
                              'resets the review clock to zero [-ceDuiClggg @ 00:13:03]. His longer '
                              'MedicalMarcom session drills into the cause: 54% of rejections cite missing '
                              'shelf-life data. His countermeasure is to include a completed RTA checklist '
                              'in Section 1 or Section 21, and his last two consultant-led submissions '
                              "passed on the first try [gGje01O9B44 @ 00:13:09]. Qualio's numbers are "
                              'lower but still brutal, with 30% of submissions last year not even accepted '
                              'for initial review [1GKnWm8UYVk @ 00:54:07]. Inside eSTAR the failure '
                              "points shift but do not vanish. Packard sees 'so many RTAs just because "
                              "companies don't have a level of concern documentation in the package,' and "
                              'he flags missing wireless coexistence testing as another common trigger '
                              '[b1Ejw4mhVFU @ 00:15:58]. The small stuff bites too. In the Part I '
                              'workshop, an inconsistent device name across headers triggers RTA, a condom '
                              "was rejected over the 'patient contacting' field, and a wrong Rx/OTC "
                              'checkbox costs about $5k and another 90 days.',
                              'Dave Saunders describes a company that got 48 hours to produce a '
                              '40,000-page DHF, hand-delivered it, and still failed clearance. His '
                              'yardstick is that a 510(k) runs 200 to 500 pages sitting on a DHF of '
                              "roughly 10,000 [6w27HXwMbmU @ 00:32:12]. He warns 'you cannot create this "
                              "documentation retroactively,' and says a change log where every change is "
                              "approved 'suggests a rubber stamp process' [6w27HXwMbmU @ 00:36:12]. Sagar "
                              "Tipne's remediation interview supplies the field evidence. A Class 2 "
                              'orthopedic implant drew a 483 for missing input-to-verification '
                              'traceability and took months to fix, and a drug-delivery device had no FMEA '
                              'or hazard analysis, so the team rebuilt both under ISO 14971 [hJg3slOsTT8 @ '
                              '00:00:57]. Departed engineers force rationale to be reverse-engineered from '
                              'ECOs and interviews, as happened on a cardiac catheter. Software '
                              'classification is its own trap: Packard notes that IEC 62304 classes A, B, '
                              'and C do not map to FDA level of concern, and some firms lost a year on '
                              "that mismatch [-ceDuiClggg @ 00:45:40]. Saunders' audit drill exposes all "
                              'of it: an auditor picks a random component, asks you to trace it back to a '
                              'user need, and reads empty matrix cells as gaps.',
                              'The Innolitics panel dissected a live enforcement case. O.N. Diagnostics '
                              'cleared its VirtuOst VFA spine CT tool in 2017, then shipped version 3.0.0 '
                              'on June 11, 2024 with a better ML model, a desktop-to-web move, and a newer '
                              'platform, all without a new 510(k). FDA inspected in March 2026, issued the '
                              'warning letter September 1, and called the device adulterated and '
                              'misbranded [UdQw2LB0EYc @ 00:00:03]. David was surprised the web move '
                              'needed a submission, while Mary read the letter as a QMS failure, with '
                              'unaddressed CAPAs and a release from an uncontrolled system [UdQw2LB0EYc @ '
                              '00:13:44]. For GenAI products the timing math is ugly: LLM deprecation '
                              'windows run 2 weeks to 6 months against a roughly 6-month 510(k), so the '
                              'panel treats a PCCP as effectively required. Budget checks belong at the '
                              'same gate. Packard prices biocompatibility near $13,000, electrical safety '
                              'and EMC at $50,000 to $60,000 typical, animal studies at $100,000 or more, '
                              'and clinical work up to $3M for 500 to 600 patients [-ceDuiClggg @ '
                              "00:10:04]. Qualio adds the predicate tax: '15% submissions fail because of "
                              "the wrong predicate' [1GKnWm8UYVk @ 00:59:39]."],
               'table': {'caption': 'Firsthand failure modes and what each one cost the submitter',
                         'headers': ['Failure Mode', 'What Happened', 'Cost or Delay', 'Expert Source'],
                         'rows': [['Rejection at the refuse-to-accept screen',
                                   'More than 50% of submissions rejected at RTA against a 26-27 page '
                                   'checklist',
                                   'A rejection resets the FDA review clock back to zero days',
                                   'MedicalMarcom ([-ceDuiClggg @ 00:13:03])'],
                                  ['Missing shelf-life data in the package',
                                   '54% of RTA rejections cite missing shelf life data in the submission',
                                   'Another RTA cycle on top of a realistic 120 to 130 day total',
                                   'MedicalMarcom ([gGje01O9B44 @ 00:13:09])'],
                                  ['Wrong Rx or OTC checkbox on the forms',
                                   'A single wrong prescription versus over-the-counter box checked on the '
                                   'submission',
                                   'About $5k and another 90 days added to the review timeline',
                                   'MedicalMarcom ([yIARvVKN5-s @ 00:32:03])'],
                                  ['DHF demanded under a 48-hour deadline',
                                   'Company had 48 hours to deliver a 40,000-page DHF and hand-delivered '
                                   'it',
                                   'Still failed clearance despite physically delivering the entire DHF on '
                                   'time',
                                   'Dave Saunders ([6w27HXwMbmU @ 00:32:12])'],
                                  ['Assuming IEC 62304 classes equal level of concern',
                                   'Firms mapped software safety classes A, B, and C onto FDA level of '
                                   'concern',
                                   'Some firms lost a full year correcting the classification mismatch',
                                   'MedicalMarcom ([-ceDuiClggg @ 00:45:40])'],
                                  ['Software update shipped without a new 510(k)',
                                   'VirtuOst VFA 3.0.0 shipped with a new ML model and a web app',
                                   'Warning letter calling the device adulterated and misbranded; '
                                   'distribution of that version halted',
                                   'Innolitics ([UdQw2LB0EYc @ 00:00:03])'],
                                  ['Missing design traceability on an implant',
                                   'Class 2 orthopedic implant lacked input-to-verification traceability '
                                   'in its DHF',
                                   'FDA 483 observation followed by months of remediation work',
                                   'SAGAR TIPNE ([hJg3slOsTT8 @ 00:00:57])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Pre-Upload Kill Checks',
                           'body': 'Run these four checks before the eSTAR or eCopy leaves the building. '
                                   'Each one maps to a rejection, hold, or enforcement action that '
                                   'practitioners lived through.',
                           'items': ['Annotate the RTA checklist with the exact location of every item and '
                                     'include it in the package; this approach once produced acceptance on '
                                     'day 2 [MedicalMarcom — nUaPO0mfwKI @ 00:31:54].',
                                     'Confirm level of concern documentation and wireless coexistence '
                                     'testing are in the eSTAR, two of the most common RTA triggers '
                                     'Packard sees [Medical Device Academy — b1Ejw4mhVFU @ 00:15:58].',
                                     'Run the random-component drill: trace any output back to a user need '
                                     'in under 60 seconds, and treat every empty matrix cell as a gap '
                                     '[Dave Saunders — 6w27HXwMbmU @ 00:13:16].',
                                     'Before shipping any software change, ask whether a PCCP exists and '
                                     'why you are retraining; expanding inputs means a special 510(k) '
                                     '[Innolitics — UdQw2LB0EYc @ 00:25:57].']}}],
 'pull_quote': "'The bad news is that you cannot create this documentation retroactively.' Attributed to "
               'Dave Saunders (6w27HXwMbmU @ 00:36:12).',
 'diagram_id': 'diag-01',
 'action_checklist': ['Search the three-letter product code in the Classification database, confirm the '
                      'predicate is legally marketed in Registration & Listing, and pull TPLC recalls and '
                      'MDRs [MedicalMarcom — yIARvVKN5-s @ 00:05:38].',
                      "Copy the predicate's indications for use word-for-word into your Section 4 draft "
                      '[Qualio — 1GKnWm8UYVk @ 00:39:21].',
                      'Build the test plan at design-input approval, pulling from guidances, standards, '
                      '510(k) summaries, and FOIA copies [MedicalMarcom — -ceDuiClggg @ 00:22:55].',
                      'Run the submission from a color-coded Excel table of contents (red, yellow, blue, '
                      'green), writing Section 4 first and the executive summary last [MedicalMarcom — '
                      'gGje01O9B44 @ 00:43:41].',
                      'Apply for small business qualification every year on August 1 alongside your tax '
                      'filing [MedicalMarcom — -ceDuiClggg @ 00:39:20].',
                      'Check spam folders for hold letters, answer within 180 days, and request an '
                      'extension if you approach that ceiling [MedicalMarcom — nUaPO0mfwKI @ 00:38:03].'],
 'statutory_citations': [{'title': 'MedicalMarcom — How to Prepare a Medical Device 510k Submission for '
                                   'FDA | Rob Packard | Joe Hage [00:13:03]',
                          'url': 'https://www.youtube.com/watch?v=-ceDuiClggg&t=783s',
                          'relevance': 'Primary practitioner testimony on RTA rejection rates, testing '
                                       'costs, pre-sub economics, and IEC 62304 classification traps.'},
                         {'title': 'Qualio — Mastering your 510(k) submission process [00:13:07]',
                          'url': 'https://www.youtube.com/watch?v=1GKnWm8UYVk&t=787s',
                          'relevance': 'Primary practitioner testimony on abbreviated 510(k) delays, '
                                       'predicate age disputes, and wrong-predicate failure rates.'},
                         {'title': 'Dave Saunders — Medical Device Design Controls: Complete FDA 510(k) '
                                   'Guide with ISO 13485 Compliance [00:32:12]',
                          'url': 'https://www.youtube.com/watch?v=6w27HXwMbmU&t=1932s',
                          'relevance': 'Primary practitioner testimony on DHF scale, the 40,000-page '
                                       'delivery failure, and retroactive documentation.'},
                         {'title': 'Innolitics — Coffee and Q&A: When a Software Update Needs a New '
                                   "510(k), FDA's Warning Letter to O.N. Diagnostics [00:00:03]",
                          'url': 'https://www.youtube.com/watch?v=UdQw2LB0EYc&t=3s',
                          'relevance': 'Primary practitioner testimony on software changes shipped without '
                                       'a new 510(k) and the resulting warning letter.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'dd7dQRVr-mQ',
                       'title': 'How to Prepare a Medical Device 510k Submission for FDA',
                       'channel': 'Matrix One',
                       'author': 'Matrix One',
                       'text': "Don't underestimate the amount of time that is needed for your 510k "
                               'submission.',
                       'tip': "Don't underestimate the amount of time that is needed for your 510k "
                              'submission.',
                       'timestamp': 377,
                       'timestamp_seconds': 377,
                       'timestamp_label': '[00:06:17]',
                       'url': 'https://www.youtube.com/watch?v=dd7dQRVr-mQ&t=377s',
                       'markdown': '[00:06:17](https://www.youtube.com/watch?v=dd7dQRVr-mQ&t=377s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '1GKnWm8UYVk',
                       'title': 'Mastering your 510(k) submission process',
                       'channel': 'Qualio',
                       'author': 'Qualio',
                       'text': 'This option actually takes about twice as long as the traditional process '
                               "for the FDA to review and it doesn't require any less work on your part.",
                       'tip': 'This option actually takes about twice as long as the traditional process '
                              "for the FDA to review and it doesn't require any less work on your part.",
                       'timestamp': 787,
                       'timestamp_seconds': 787,
                       'timestamp_label': '[00:13:07]',
                       'url': 'https://www.youtube.com/watch?v=1GKnWm8UYVk&t=787s',
                       'markdown': '[00:13:07](https://www.youtube.com/watch?v=1GKnWm8UYVk&t=787s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '1GKnWm8UYVk',
                       'title': 'Mastering your 510(k) submission process',
                       'channel': 'Qualio',
                       'author': 'Qualio',
                       'text': 'Again, 15% submissions fail because of the wrong predicate.',
                       'tip': 'Again, 15% submissions fail because of the wrong predicate.',
                       'timestamp': 3579,
                       'timestamp_seconds': 3579,
                       'timestamp_label': '[00:59:39]',
                       'url': 'https://www.youtube.com/watch?v=1GKnWm8UYVk&t=3579s',
                       'markdown': '[00:59:39](https://www.youtube.com/watch?v=1GKnWm8UYVk&t=3579s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'b1Ejw4mhVFU',
                       'title': 'How to prepare an FDA eSTAR 510(k) submission',
                       'channel': 'Medical Device Academy',
                       'author': 'Medical Device Academy',
                       'text': "I see so many RTAs just because companies don't have a level of concern "
                               'documentation in the package.',
                       'tip': "I see so many RTAs just because companies don't have a level of concern "
                              'documentation in the package.',
                       'timestamp': 958,
                       'timestamp_seconds': 958,
                       'timestamp_label': '[00:15:58]',
                       'url': 'https://www.youtube.com/watch?v=b1Ejw4mhVFU&t=958s',
                       'markdown': '[00:15:58](https://www.youtube.com/watch?v=b1Ejw4mhVFU&t=958s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'bEKT9pNj8Sg',
                       'title': "What's an RFD and when do I need one for a FDA 510(k)?",
                       'channel': 'Medical Device Academy',
                       'author': 'Medical Device Academy',
                       'text': 'Now, the FDA gets a bit perturbed, irritated when you ask them silly '
                               "questions in a pre-RFD about something that's already clearly stated in "
                               'the guidance document.',
                       'tip': 'Now, the FDA gets a bit perturbed, irritated when you ask them silly '
                              "questions in a pre-RFD about something that's already clearly stated in the "
                              'guidance document.',
                       'timestamp': 789,
                       'timestamp_seconds': 789,
                       'timestamp_label': '[00:13:09]',
                       'url': 'https://www.youtube.com/watch?v=bEKT9pNj8Sg&t=789s',
                       'markdown': '[00:13:09](https://www.youtube.com/watch?v=bEKT9pNj8Sg&t=789s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '6w27HXwMbmU',
                       'title': 'Medical Device Design Controls: Complete FDA 510(k) Guide with ISO 13485 '
                                'Compliance',
                       'channel': 'Dave Saunders',
                       'author': 'Dave Saunders',
                       'text': 'The bad news is that you cannot create this documentation retroactively.',
                       'tip': 'The bad news is that you cannot create this documentation retroactively.',
                       'timestamp': 2172,
                       'timestamp_seconds': 2172,
                       'timestamp_label': '[00:36:12]',
                       'url': 'https://www.youtube.com/watch?v=6w27HXwMbmU&t=2172s',
                       'markdown': '[00:36:12](https://www.youtube.com/watch?v=6w27HXwMbmU&t=2172s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '-ceDuiClggg',
                       'title': 'How to Prepare a Medical Device 510k Submission for FDA | Rob Packard | '
                                'Joe Hage',
                       'channel': 'MedicalMarcom',
                       'author': 'MedicalMarcom',
                       'text': 'More than 50% of the submissions are rejected during that RTA screening.',
                       'tip': 'More than 50% of the submissions are rejected during that RTA screening.',
                       'timestamp': 783,
                       'timestamp_seconds': 783,
                       'timestamp_label': '[00:13:03]',
                       'url': 'https://www.youtube.com/watch?v=-ceDuiClggg&t=783s',
                       'markdown': '[00:13:03](https://www.youtube.com/watch?v=-ceDuiClggg&t=783s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '-ceDuiClggg',
                       'title': 'How to Prepare a Medical Device 510k Submission for FDA | Rob Packard | '
                                'Joe Hage',
                       'channel': 'MedicalMarcom',
                       'author': 'MedicalMarcom',
                       'text': 'Usually time is more valuable than money.',
                       'tip': 'Usually time is more valuable than money.',
                       'timestamp': 4407,
                       'timestamp_seconds': 4407,
                       'timestamp_label': '[01:13:27]',
                       'url': 'https://www.youtube.com/watch?v=-ceDuiClggg&t=4407s',
                       'markdown': '[01:13:27](https://www.youtube.com/watch?v=-ceDuiClggg&t=4407s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'yIARvVKN5-s',
                       'title': '510k Workshop: How to Prepare an FDA Submission (Part I)',
                       'channel': 'MedicalMarcom',
                       'author': 'MedicalMarcom',
                       'text': "But if this form is not the same, you're dead in the water right off the "
                               'bat.',
                       'tip': "But if this form is not the same, you're dead in the water right off the "
                              'bat.',
                       'timestamp': 2040,
                       'timestamp_seconds': 2040,
                       'timestamp_label': '[00:34:00]',
                       'url': 'https://www.youtube.com/watch?v=yIARvVKN5-s&t=2040s',
                       'markdown': '[00:34:00](https://www.youtube.com/watch?v=yIARvVKN5-s&t=2040s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'hJg3slOsTT8',
                       'title': 'Medical Device DHF Remediation Interview | ISO 13485 | FDA 21 CFR 820 | '
                                'Risk Management & Compliance',
                       'channel': 'SAGAR TIPNE',
                       'author': 'SAGAR TIPNE',
                       'text': 'If a regulator asks how do you know this requirement was met, there should '
                               'be a direct line of evidence in the DHF.',
                       'tip': 'If a regulator asks how do you know this requirement was met, there should '
                              'be a direct line of evidence in the DHF.',
                       'timestamp': 553,
                       'timestamp_seconds': 553,
                       'timestamp_label': '[00:09:13]',
                       'url': 'https://www.youtube.com/watch?v=hJg3slOsTT8&t=553s',
                       'markdown': '[00:09:13](https://www.youtube.com/watch?v=hJg3slOsTT8&t=553s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'aZkxlipyWRs',
                       'title': 'Mastering the FDA 510(k) Submission Process: A Practical Guide',
                       'channel': 'Conference Panel',
                       'author': 'Conference Panel',
                       'text': 'Pitfall number five, poor document naming and version control.',
                       'tip': 'Pitfall number five, poor document naming and version control.',
                       'timestamp': 372,
                       'timestamp_seconds': 372,
                       'timestamp_label': '[00:06:12]',
                       'url': 'https://www.youtube.com/watch?v=aZkxlipyWRs&t=372s',
                       'markdown': '[00:06:12](https://www.youtube.com/watch?v=aZkxlipyWRs&t=372s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '7hmnIP4pXbo',
                       'title': 'Behind the 510(k): The Science of Material Compatibility and FDA '
                                'Clearance Ft. CS Medical Staff',
                       'channel': 'CS Medical',
                       'author': 'CS Medical',
                       'text': "You can't accelerate those with the US FDA.",
                       'tip': "You can't accelerate those with the US FDA.",
                       'timestamp': 1105,
                       'timestamp_seconds': 1105,
                       'timestamp_label': '[00:18:25]',
                       'url': 'https://www.youtube.com/watch?v=7hmnIP4pXbo&t=1105s',
                       'markdown': '[00:18:25](https://www.youtube.com/watch?v=7hmnIP4pXbo&t=1105s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'V3Fob6FXlCo',
                       'title': 'FDA 510K Premarket Notification Webinar',
                       'channel': 'Invent Healthcare',
                       'author': 'Invent Healthcare',
                       'text': "That's the beauty of the 510k process, you don't have to be exactly like "
                               'your predicate.',
                       'tip': "That's the beauty of the 510k process, you don't have to be exactly like "
                              'your predicate.',
                       'timestamp': 1362,
                       'timestamp_seconds': 1362,
                       'timestamp_label': '[00:22:42]',
                       'url': 'https://www.youtube.com/watch?v=V3Fob6FXlCo&t=1362s',
                       'markdown': '[00:22:42](https://www.youtube.com/watch?v=V3Fob6FXlCo&t=1362s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'gGje01O9B44',
                       'title': 'How to prepare a 510k submission for FDA',
                       'channel': 'MedicalMarcom',
                       'author': 'MedicalMarcom',
                       'text': "So, if you're in doubt, submit it as a traditional.",
                       'tip': "So, if you're in doubt, submit it as a traditional.",
                       'timestamp': 5239,
                       'timestamp_seconds': 5239,
                       'timestamp_label': '[01:27:19]',
                       'url': 'https://www.youtube.com/watch?v=gGje01O9B44&t=5239s',
                       'markdown': '[01:27:19](https://www.youtube.com/watch?v=gGje01O9B44&t=5239s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'UdQw2LB0EYc',
                       'title': "Coffee and Q&A: When a Software Update Needs a New 510(k), FDA's Warning "
                                'Letter to O.N. Diagnostics',
                       'channel': 'Innolitics',
                       'author': 'Innolitics',
                       'text': "And also, a PCCP doesn't mean less work or less documentation.",
                       'tip': "And also, a PCCP doesn't mean less work or less documentation.",
                       'timestamp': 3126,
                       'timestamp_seconds': 3126,
                       'timestamp_label': '[00:52:06]',
                       'url': 'https://www.youtube.com/watch?v=UdQw2LB0EYc&t=3126s',
                       'markdown': '[00:52:06](https://www.youtube.com/watch?v=UdQw2LB0EYc&t=3126s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'nUaPO0mfwKI',
                       'title': '510k Workshop: How to Prepare an FDA Submission (Part II)',
                       'channel': 'MedicalMarcom',
                       'author': 'MedicalMarcom',
                       'text': 'So, you have 180 days to answer the hold letter.',
                       'tip': 'So, you have 180 days to answer the hold letter.',
                       'timestamp': 2253,
                       'timestamp_seconds': 2253,
                       'timestamp_label': '[00:37:33]',
                       'url': 'https://www.youtube.com/watch?v=nUaPO0mfwKI&t=2253s',
                       'markdown': '[00:37:33](https://www.youtube.com/watch?v=nUaPO0mfwKI&t=2253s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '6WEZ6ovm-PE',
                       'title': 'How to Pick a Predicate Device for Your 510(k): Intended Use, Split '
                                'Predicates & FDA Best Practices',
                       'channel': 'Cleared 인허가 노트',
                       'author': 'Cleared 인허가 노트',
                       'text': "So start by reading the predicate's indications for use statement.",
                       'tip': "So start by reading the predicate's indications for use statement.",
                       'timestamp': 148,
                       'timestamp_seconds': 148,
                       'timestamp_label': '[00:02:28]',
                       'url': 'https://www.youtube.com/watch?v=6WEZ6ovm-PE&t=148s',
                       'markdown': '[00:02:28](https://www.youtube.com/watch?v=6WEZ6ovm-PE&t=148s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'XOwMEZdq9q8',
                       'title': "Video 18 of 35 - FDA's 2026 CSA Guidance — Risk Assessment and Assurance "
                                'Activities |',
                       'channel': 'Pharma Best Practices',
                       'author': 'Pharma Best Practices',
                       'text': 'Your assurance effort should be a holistic reflection of the actual risk.',
                       'tip': 'Your assurance effort should be a holistic reflection of the actual risk.',
                       'timestamp': 520,
                       'timestamp_seconds': 520,
                       'timestamp_label': '[00:08:40]',
                       'url': 'https://www.youtube.com/watch?v=XOwMEZdq9q8&t=520s',
                       'markdown': '[00:08:40](https://www.youtube.com/watch?v=XOwMEZdq9q8&t=520s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'}]}
