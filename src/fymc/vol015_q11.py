from __future__ import annotations

CHAPTER_11 = {'id': 'Q11',
 'chapter_id': 'Q11',
 'chapter_number': 11,
 'question_number': 11,
 'slug': 'fdcpa-regulation-f-compliance-risk',
 'question_prompt': 'What do the FDCPA and Regulation F prohibit, and how do collectors get sued for '
                    'violating them?',
 'kicker': 'Q11 / THE BIG MONEY PLAYBOOKS',
 'title': 'FDCPA and Regulation F Compliance Risk',
 'subtitle': 'Who counts as a debt collector (Barbato v. Crown Asset), Sections 1692e and 1692f, '
             'Regulation F rules, consumer rights, anatomy of an FDCPA lawsuit, eviction-related '
             'liability, credit-dispute case studies, deposing a collection attorney, and proposed '
             'legislation affecting collection litigation',
 'layout_template': 'chapter_opener',
 'reading_time_minutes': 15,
 'executive_summary': 'Consumer attorneys and collection-side insiders agree the FDCPA hits third-party '
                      'collectors and debt buyers on consumer debt, and that Regulation F turned contact '
                      'limits into countable violations: seven call attempts per seven days per account, '
                      'no calls outside 8:00 a.m. to 9:00 p.m., opt-outs on every text, and a validation '
                      'notice within five days. Fee-shifting is the engine. Statutory damages run up to '
                      "$1,000, and Aaron Swift's bronze file turned two technical violations into a "
                      'roughly $4,000 debt wipe, a deleted tradeline, and about $4,500 in fees. Street '
                      'mechanics center on Reg F restriction letters, certified mail, itemization audits, '
                      'and contract-fee checks. Practitioners split on whether seven-in-seven is a hard '
                      'cap or a presumption, whether payment restarts the limitations clock in almost '
                      'every state or only some, and how much validation letters actually demand.',
 'key_metrics': [{'label': 'Reg F call-attempt ceiling per account',
                  'metric': 'Reg F call-attempt ceiling per account',
                  'value': '7 call attempts per 7 days per account; 5 accounts means up to 35 calls',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Attorney Kaiser Jansen's description of the 7-in-7 rule, with only one "
                             'contact per seven-day period after a connection',
                  'source': 'SeniorLiving.Org ([9RtU4rpS3pw @ 00:05:51])'},
                 {'label': 'FDCPA damages exposure',
                  'metric': 'FDCPA damages exposure',
                  'value': 'Actual damages plus up to $1,000 additional; class actions capped at the '
                           'lesser of $500,000 or 1% of net worth, plus costs and fees',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "LawShelf's breakdown of the remedies available against a collector that "
                             'violates the Act',
                  'source': 'LawShelf ([i6PAssklgJg @ 00:05:05])'},
                 {'label': 'Bronze-tier case payout',
                  'metric': 'Bronze-tier case payout',
                  'value': 'About $4,000 debt forgiven, tradeline deleted, $1,000 statutory damages, about '
                           '$4,500 attorney fees, about $450 to affiliate',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Aaron Swift's amalgam of a small case built on two technical violations: "
                             'continued texting and an unmarked disputed tradeline',
                  'source': 'Consumer Law 101 by Attorney Aaron Swift ([owpVxkqEbEk @ 00:05:22])'},
                 {'label': 'Collection law firm filing volume',
                  'metric': 'Collection law firm filing volume',
                  'value': 'About 50 lawsuits a week, roughly 10 a day',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Collection attorney Bradley Johnson's admission under deposition by Brian "
                             "Parker about his firm's suit volume",
                  'source': 'KillDebt & ParkerGPT: The New Way To Law ([RwXTJhX-rxo @ 00:21:52])'}],
 'sections': [{'heading': 'Section 1: The Practitioner Consensus',
               'paragraphs': ['Every practitioner draws the same perimeter first: the FDCPA bites '
                              'third-party collectors chasing consumer debt, not original creditors and '
                              'not commercial paper. Simple Explain frames it as third-party collectors '
                              'only [njrU1ZwxRCY @ 00:00:57], and LawShelf limits coverage to personal, '
                              'family, or household debts such as cars, credit cards, and some student '
                              'loans, with commercial debt excluded and attorneys who regularly collect '
                              'pulled inside [i6PAssklgJg @ 00:01:24]. Jeff Loman of Guardian Litigation '
                              'Group sharpens the edge for street use: banks, payday lenders, '
                              'rent-a-centers, and tolls sit outside, and business debt never qualifies '
                              '[n3SZjPQDSHc @ 00:04:20]. The perimeter is wider than debt buyers want it '
                              'to be. John Watts walks through Barbato v. Crown Asset, where the buyer '
                              'argued it merely purchased charged-off receivables and farmed collection '
                              'out; the court held that an entity meeting the principal-purpose definition '
                              'cannot dodge the Act by hiring a third party to do its collecting '
                              '[fPw38bPWFtw @ 00:02:40]. Watts frames the economics that make buyers fight '
                              'so hard: Crown buys a thousand-dollar debt for fifty bucks and the consumer '
                              'may settle for $700. For an operator, the first screening question is '
                              'therefore who is actually collecting, what kind of debt it is, and whose '
                              'business model depends on the payment.',
                              'The contact rules form the second layer of agreement. Attorney Kaiser '
                              'Jansen, on SeniorLiving.Org, states the Reg F line bluntly: collectors can '
                              'only attempt to call seven times in seven days, and after a connection only '
                              'one contact per seven-day period, counted per account, so five accounts can '
                              'mean up to 35 calls [9RtU4rpS3pw @ 00:05:51]. Jansen also warns that saying '
                              "'okay' to a callback counts as consent. WealthCurve adds the clock window "
                              'shared by nearly every speaker: no calls before 8:00 a.m. or after 9:00 '
                              'p.m., plus bans on threats, impersonation, and unauthorized fees '
                              '[cKYmFnf_o2Q @ 00:03:43]. Workplace contact runs on notice. Loman says '
                              'calls at work are allowed until the consumer tells the collector personal '
                              'calls cannot be received there, and any call after that is a violation '
                              '[n3SZjPQDSHc @ 00:20:44]. Digital channels carry their own trap for '
                              'collectors. Night Ferry notes texts and emails are not counted toward the '
                              'call cap but cannot harass, and each must offer a simple opt-out '
                              '[7HVra7o-cZg @ 00:04:04]; Jansen adds that contact continuing after a '
                              "'stop' reply is actionable. The operating consensus is simple: every "
                              'channel restriction becomes enforceable the moment the consumer puts it on '
                              'the record, and every post-notice contact becomes a countable, documentable '
                              'violation.',
                              'The third consensus pillar is the paper trail and the money behind it. '
                              'Jansen describes the 5-in-5 rule: a validation notice within five days, '
                              'with a tear-off dispute sheet, the original creditor, account number, and '
                              'an itemization, illustrated with a balance that climbed from $200 to 1,396 '
                              '[9RtU4rpS3pw @ 00:10:42]. WealthCurve says a written dispute sent inside '
                              'the 30-day window forces the collector to stop all collection activity, and '
                              'warns against mailing it on day 29 [cKYmFnf_o2Q @ 00:03:01]. On remedies, '
                              'LawShelf lists actual damages, additional damages up to $1,000, the lesser '
                              'of $500,000 or 1% of net worth in a class action, plus costs and fees, and '
                              'states that in many cases the potential for attorneys fees drives FDCPA '
                              'litigation [i6PAssklgJg @ 00:05:23]. Aaron Swift turns that into a business '
                              'thesis: two technical violations erased roughly $4,000 of debt and still '
                              'produced $1,000 statutory damages, and his lesson is that no case is too '
                              'small [owpVxkqEbEk @ 00:06:30]. Jansen notes FDCPA firms typically take a '
                              'third on contingency. Loman puts it plainly: under fee shifting, the '
                              'attorney is paid by the other side. Across the board, the speakers treat '
                              'fee-shifting as the engine that makes even small, technical violations '
                              'worth filing.'],
               'table': {'caption': 'Where the practitioners line up: coverage, contact limits, disputes, '
                                    'and remedies',
                         'headers': ['Consensus Point',
                                     'What Practitioners Report',
                                     'Operator Implication',
                                     'Expert Source'],
                         'rows': [['Third-party collectors are the core target',
                                   'FDCPA applies to third-party collectors, not original creditors '
                                   'handling their own accounts',
                                   'Screen every account first for who is actually doing the collecting',
                                   'Simple Explain ([njrU1ZwxRCY @ 00:00:57])'],
                                  ['Consumer debt only, commercial debt excluded',
                                   'Personal, family, household debts like cars, credit cards, and some '
                                   'student loans are covered',
                                   'Filter commercial and business debts out early because the Act never '
                                   'reaches them',
                                   'LawShelf ([i6PAssklgJg @ 00:01:24])'],
                                  ['Debt buyers cannot outsource their liability',
                                   'A principal-purpose entity cannot avoid the Act by hiring a third '
                                   'party to collect',
                                   'Passive debt buyer defenses fail when collection is the core business '
                                   'model',
                                   'Alabama Consumer Protection Lawyers ([fPw38bPWFtw @ 00:02:40])'],
                                  ['Seven-in-seven call attempt limit per account',
                                   'Seven call attempts in seven days, counted per account, one contact '
                                   'after a connection',
                                   'Log every call per account to build a countable frequency record',
                                   'SeniorLiving.Org ([9RtU4rpS3pw @ 00:05:51])'],
                                  ['Calling hours and workplace calls run on notice',
                                   'Work calls are allowed until the consumer says personal calls cannot '
                                   'be received there',
                                   'Put workplace and time restrictions on record so later calls become '
                                   'violations',
                                   'Solo – Resolve Your Debt ([n3SZjPQDSHc @ 00:20:44])'],
                                  ['Written dispute inside the thirty-day window',
                                   'A written dispute within the window forces the collector to stop all '
                                   'collection activity',
                                   'Mail the dispute early with proof and never wait until day twenty-nine',
                                   'WealthCurve ([cKYmFnf_o2Q @ 00:03:01])'],
                                  ['Fee-shifting drives the litigation economics',
                                   'Damages up to $1,000 plus attorney fees and costs, which often drive '
                                   'FDCPA suits',
                                   'Even small technical violations can pay for counsel through fee awards',
                                   'LawShelf ([i6PAssklgJg @ 00:05:23])']]}},
              {'heading': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ["Aaron Swift's bronze-tier case is the cleanest street workflow on record, "
                              "the 'blocking and tackling' files that keep the lights on. Intake filters "
                              'each consumer into litigation, disputes, or a credit-repair affiliate '
                              'partner, then the firm sends third-party collectors a letter by fax or '
                              'email [owpVxkqEbEk @ 00:03:10]. Swift stresses it is not a validation '
                              'letter, which only matters inside the first 30 days; it is built on Reg F, '
                              'restricts contact channels and times such as 5:00 to 8:00 p.m., and '
                              'disputes the debt. The trap then springs on its own. The collector kept '
                              'texting, and the credit reports never marked the account disputed. Loman '
                              'confirms the second hook: when a collector tradeline such as LVNV or '
                              'Portfolio Recovery is disputed, it must be marked disputed [n3SZjPQDSHc @ '
                              "00:14:16]. Swift's payout on those two technical violations: about $4,000 "
                              'of debt forgiven, the tradeline deleted, $1,000 in statutory damages, '
                              'roughly $4,500 in attorney fees, and about $450 to the affiliate as '
                              'contract paralegal [owpVxkqEbEk @ 00:05:22]. Swift calls the result a debt '
                              'almost completely erased like it never existed. The unit economics are the '
                              'point. A low-dollar file with a fax letter and two missed obligations funds '
                              'the attorney, the affiliate, and a near-total debt wipe for the client.',
                              'Once a file goes to suit, John Watts lays out the procedural rhythm. He '
                              'files in state court 99.9 percent of the time because of Spokeo standing '
                              'arguments, and defendants, who get 30 days to answer or remove, remove 99.9 '
                              'percent of the time [Ce0D7z4zJFo @ 00:00:30]. Motions to dismiss are often '
                              "baseless because 'it makes the lawyers money,' so he usually amends the "
                              'complaint as of right instead. Discovery then runs through interrogatories, '
                              'document requests, requests for admission, and depositions, followed by '
                              'summary judgment with damages usually left to the jury [Ce0D7z4zJFo @ '
                              "00:03:32]. At trial he calls the collector's own witnesses, and the "
                              "collector's motion for judgment as a matter of law has always been denied "
                              'in his trials. Swift tempers the trial math: the vast majority, 99 percent '
                              'or more, never reach trial [owpVxkqEbEk @ 00:01:14]. Brian Parker shows '
                              'what discovery can surface on the other side. Deposing collection attorney '
                              'Bradley Johnson, he extracted that the firm files about 50 suits a week, '
                              'roughly 10 a day, off a form complaint with an auto-generated summons, '
                              'scrubbing through LexisNexis for deceased, new addresses, bankruptcy, and '
                              'active military [RwXTJhX-rxo @ 00:21:52]. Volume filing on templates is '
                              'exactly what deposition questioning is built to expose.',
                              "The balance itself is the next attack surface. Loman's hospital-debt "
                              'workflow starts with a HIPAA request for medical records including billing, '
                              "because the collector is not required to itemize under 'G' of the FDCPA, "
                              'then pulls an insurance accounting of what was paid; he routinely finds '
                              'double billing and code changes [n3SZjPQDSHc @ 00:41:14]. Host Hannah '
                              'Locklear was charged $16 for one ibuprofen pill and got the debt lowered '
                              'after demanding an itemized statement, and Loman has a client billed $6,000 '
                              'for a $300 IV. Brian Parker hunts the same inflation through §1692f: every '
                              'charge must sit inside the four corners of the contract, and an '
                              'unauthorized 25% collection fee is a violation [YYdsx06msa0 @ 00:03:38]. He '
                              'also stacks claims, since false credit reporting under §1692e8 supports an '
                              "FCRA claim too, so 'you can hit them twice' [YYdsx06msa0 @ 00:01:13]. "
                              'Parker frames these as strict-liability violations. None of this works '
                              'without proof of delivery. Jermaine, drawing on his time working in debt '
                              'collections, insists on copying every letter and sending it certified, not '
                              'regular mail or email, for a 16-digit tracking number, because otherwise it '
                              "is your word against the collector's [XSfDS_s1URg @ 00:06:09]. Many "
                              'collectors, he warns, never fix errors after being called out, so the '
                              'documented file is the weapon.'],
               'table': {'caption': 'Street mechanics, tools, and hard numbers practitioners actually use',
                         'headers': ['Mechanic',
                                     'Exact Number or Tool',
                                     'How Operators Use It',
                                     'Expert Source'],
                         'rows': [['Reg F contact restriction and dispute letter',
                                   'Fax or email letter restricting channels and times such as 5:00 to '
                                   '8:00 p.m.',
                                   'Sets up countable violations when the collector keeps texting or '
                                   'ignores the dispute',
                                   'Consumer Law 101 by Attorney Aaron Swift ([owpVxkqEbEk @ 00:03:45])'],
                                  ['Bronze-tier case unit economics',
                                   'About $4,000 forgiven, $1,000 statutory, roughly $4,500 fees, about '
                                   '$450 to affiliate',
                                   'Shows small technical files can fund attorney, affiliate, and client '
                                   'debt relief together',
                                   'Consumer Law 101 by Attorney Aaron Swift ([owpVxkqEbEk @ 00:05:22])'],
                                  ['Per-account call attempt math',
                                   'Seven attempts per seven days per account, so five accounts means 35 '
                                   'calls',
                                   'Track call attempts separately for each account the collector is '
                                   'working',
                                   'SeniorLiving.Org ([9RtU4rpS3pw @ 00:05:51])'],
                                  ['Venue choice and removal pattern',
                                   'State court filing 99.9 percent of the time; defendants remove 99.9 '
                                   'percent',
                                   'Expect federal removal and plan to amend the complaint as of right',
                                   'Alabama Consumer Protection Lawyers ([Ce0D7z4zJFo @ 00:00:30])'],
                                  ['Medical billing audit before any payment',
                                   'HIPAA records request plus insurance accounting; $16 ibuprofen, $6,000 '
                                   'billed for $300 IV',
                                   'Expose double billing and code changes before negotiating any claimed '
                                   'balance',
                                   'Solo – Resolve Your Debt ([n3SZjPQDSHc @ 00:41:14])'],
                                  ['Unauthorized collection fee screen',
                                   "A 25% collection fee outside the contract's four corners violates "
                                   '§1692f',
                                   'Compare every itemized charge against the signed contract terms line '
                                   'by line',
                                   'KillDebt & ParkerGPT: The New Way To Law ([YYdsx06msa0 @ 00:03:38])'],
                                  ['Certified mail as proof of delivery',
                                   'Certified mail yields a 16-digit tracking number showing the actual '
                                   'delivery date',
                                   'Defeats the word-against-word problem that regular mail and email '
                                   'create',
                                   'Meet Jermaine (Clear &Strategic) ([XSfDS_s1URg @ 00:06:09])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Small Moves That Turn Contact Into Claims',
                           'body': 'The practitioners repeatedly show that the claim is built in the small '
                                   'moments: what the consumer says on the phone, what gets preserved, and '
                                   'what the collector leaves in a voicemail.',
                           'items': ["Never say 'okay' to a collector's offer to call back; Jansen says "
                                     'that reply counts as consent to further contact [SeniorLiving.Org — '
                                     '9RtU4rpS3pw @ 00:06:29]',
                                     'Screenshot and preserve every collector text, because contact '
                                     "continuing after a 'stop' reply is actionable [SeniorLiving.Org — "
                                     '9RtU4rpS3pw @ 00:08:21]',
                                     'Scrutinize limited-content voicemails: Watts says phrases like '
                                     "'pre-litigation department' are barred from those messages [Alabama "
                                     'Consumer Protection Lawyers — qTSer3pu6io @ 00:39:31]',
                                     'Check whether the debt was already paid; Loman says collecting paid '
                                     'debt resold in bulk spreadsheet sales is the most common violation '
                                     'he sees now [Solo – Resolve Your Debt — n3SZjPQDSHc @ 00:13:41]']},
               'sop_steps': [{'step': 1,
                              'title': 'Screen the collector and the debt',
                              'action': 'Confirm a third-party collector or debt buyer is chasing a '
                                        'personal, family, or household debt.',
                              'detail': 'LawShelf limits coverage to consumer debts and excludes '
                                        'commercial debt [LawShelf — i6PAssklgJg @ 00:01:24]; Watts notes '
                                        'a buyer cannot escape by hiring a third party to collect [Alabama '
                                        'Consumer Protection Lawyers — fPw38bPWFtw @ 00:02:40].'},
                             {'step': 2,
                              'title': 'Send the Reg F restriction and dispute letter',
                              'action': 'Restrict contact channels and times, dispute the debt, and send '
                                        'with provable delivery.',
                              'detail': "Swift's firm sends a Reg F letter by fax or email restricting "
                                        'times such as 5:00 to 8:00 p.m. [Consumer Law 101 by Attorney '
                                        'Aaron Swift — owpVxkqEbEk @ 00:03:45]; Jermaine adds certified '
                                        'mail for a 16-digit tracking number [Meet Jermaine (Clear '
                                        '&Strategic) — XSfDS_s1URg @ 00:06:09].'},
                             {'step': 3,
                              'title': 'Log every contact and every tradeline',
                              'action': 'Count call attempts per account, save texts, and pull credit '
                                        'reports to check dispute marking.',
                              'detail': "Jansen's seven-in-seven count runs per account [SeniorLiving.Org "
                                        '— 9RtU4rpS3pw @ 00:05:51]; Loman says a disputed collector '
                                        'tradeline must be marked disputed [Solo – Resolve Your Debt — '
                                        'n3SZjPQDSHc @ 00:14:16].'},
                             {'step': 4,
                              'title': 'Audit the balance and plan the filing',
                              'action': 'Match every charge to the contract, then file expecting removal '
                                        'and a motion to dismiss.',
                              'detail': 'Parker treats an unauthorized 25% collection fee as a §1692f '
                                        'violation [KillDebt & ParkerGPT: The New Way To Law — YYdsx06msa0 '
                                        '@ 00:03:38]; Watts files in state court and expects removal 99.9 '
                                        'percent of the time [Alabama Consumer Protection Lawyers — '
                                        'Ce0D7z4zJFo @ 00:00:30].'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The sharpest split on call frequency is whether seven attempts in seven '
                              'days is a wall or a tripwire. Kaiser Jansen, appearing on SeniorLiving.Org, '
                              'frames it as absolute: "now debt collectors can only attempt to call you '
                              'seven times in seven days that\'s it," and adds that the count runs per '
                              'account, so a consumer carrying five accounts can absorb up to 35 calls in '
                              'a week [9RtU4rpS3pw @ 00:05:51]. Night Ferry reads the same rule as a '
                              'presumption of violation rather than a hard cap, and notes that texts and '
                              'emails are not counted toward it, though each must still offer a simple '
                              'opt-out [7HVra7o-cZg @ 00:03:24]. Jeff Loman of Guardian Litigation Group '
                              'pushes the frequency fight further, citing case law where 18 calls in a '
                              'single day were not treated as harassing unless the collector actually '
                              'spoke with the consumer [n3SZjPQDSHc @ 00:08:09]. Michael Stillman, past '
                              'president of the NCBA, attacks the rule from the collection-bar side: after '
                              'a right-party contact, no further contact is allowed within seven days '
                              'without consent, which collides head-on with judges who order a hallway '
                              'call, prompting the attorney to ask the bench, "are you also going to '
                              'indemnify me" [9VNthZZ6JNk @ 00:08:37].',
                              'Practitioners also split on how dangerous a single payment is on old paper. '
                              'Jansen tells SeniorLiving.Org viewers that a payment resets the statute of '
                              'limitations in "almost every state," naming Texas as the exception, and '
                              'pairs that with the ban on threatening suit over time-barred debt '
                              '[9RtU4rpS3pw @ 00:17:58]. WealthCurve opens with a narrower warning that '
                              'paying can restart the clock only "in some states," puts typical limitation '
                              'periods at three to six years, and points to a 2023 CFPB advisory barring '
                              'suit threats on time-barred debt [cKYmFnf_o2Q @ 00:04:42]. Loman widens the '
                              'trigger list beyond money: a payment, a payment plan, or even an admission '
                              'can reset the clock, and the statute only limits lawsuits, so collection '
                              'can continue "forever" while credit reporting runs seven years [n3SZjPQDSHc '
                              '@ 00:29:22]. Brian Parker of KillDebt takes the most aggressive posture on '
                              'threatened suits under section 1692e5, telling consumers to "wait it out" '
                              'when a collector threatens litigation, and stressing that nobody can be '
                              'garnished without a judgment [YYdsx06msa0 @ 00:07:04]. The playbook choice '
                              'is stark: Jansen and Loman treat any engagement on stale debt as a reset '
                              'risk, while Parker treats an empty threat of suit as a strict-liability '
                              'violation in its own right.',
                              'The paperwork camp splits hardest on how much to demand from a collector. '
                              'Meet Jermaine, drawing on time spent working in debt collections, hands out '
                              'a free four-letter bundle covering pay to delete, goodwill, cease and '
                              'desist, and debt validation [XSfDS_s1URg @ 00:00:19]. Loman flatly rejects '
                              'the 28-item validation demands circulating online: "That is absolutely not '
                              'the law," explaining that only three items are required, and warning that a '
                              'written pay-for-delete can get an attorney classed as a credit repair '
                              'organization, so the safer route is getting deletion by email or informally '
                              '[n3SZjPQDSHc @ 00:34:56]. Attorney Aaron Swift runs a third playbook, '
                              'sending third-party collectors a letter by fax or email that is explicitly '
                              'not a validation letter, because validation only matters inside the first '
                              '30 days; it is built on Reg F, restricts contact channels and times such as '
                              '5:00 to 8:00 p.m., and disputes the debt [owpVxkqEbEk @ 00:03:29]. Jermaine '
                              'insists every letter go by certified mail for a 16-digit tracking number, '
                              'because with regular mail it is "your word against" the collector\'s, while '
                              'Swift reports that his letter, followed by two technical violations, wiped '
                              'roughly $4,000 of debt for a bronze-tier client.'],
               'table': {'caption': 'Head-to-head practitioner splits on FDCPA and Regulation F tactics',
                         'headers': ['Dispute Point', 'Position A', 'Position B', 'Expert Source'],
                         'rows': [['Seven calls in seven days limit',
                                   'Jansen calls it a hard cap counted per account, so five accounts means '
                                   '35 calls',
                                   'Night Ferry calls more than seven calls a presumption of violation, '
                                   'not a cap',
                                   'SeniorLiving.Org ([9RtU4rpS3pw @ 00:05:51]); Night Ferry ([7HVra7o-cZg '
                                   '@ 00:03:24])'],
                                  ['Payment restarting the statute of limitations',
                                   'Jansen says payment resets the clock in almost every state except '
                                   'Texas',
                                   'WealthCurve says paying can restart the clock only in some states',
                                   'SeniorLiving.Org ([9RtU4rpS3pw @ 00:17:58]); WealthCurve ([cKYmFnf_o2Q '
                                   '@ 00:00:00])'],
                                  ['Year the FDCPA was enacted',
                                   'SeniorLiving.Org and LawShelf date the law to 1978, LawShelf saying '
                                   'March 1978',
                                   'WealthCurve and ExamPrepAI say 1977; Stillman says introduced 1977, '
                                   'effective 1978',
                                   'WealthCurve ([cKYmFnf_o2Q @ 00:01:01]); Receivables Info | Debt '
                                   'Collection News ([9VNthZZ6JNk @ 00:03:37])'],
                                  ['How much validation to demand from collectors',
                                   'Jermaine promotes a four-letter bundle including pay to delete and '
                                   'debt validation',
                                   'Loman says 28-item demands are not the law and only three items are '
                                   'required',
                                   'Meet Jermaine (Clear &Strategic) ([XSfDS_s1URg @ 00:00:19]); Solo – '
                                   'Resolve Your Debt ([n3SZjPQDSHc @ 00:34:56])'],
                                  ['Whether collection lawyers belong under the FDCPA',
                                   'Stillman says lawyers should not be governed by two masters once they '
                                   'litigate',
                                   'Watts says eviction lawyers count as debt collectors and owe written '
                                   'CDC notice',
                                   'Receivables Info | Debt Collection News ([9VNthZZ6JNk @ 00:02:52]); '
                                   'Alabama Consumer Protection Lawyers ([z04uhB8lcJU @ 00:04:45])'],
                                  ['Whether a passive debt buyer is a debt collector',
                                   'Crown argued its purpose is acquisition and it only hires others to '
                                   'collect',
                                   'Court held hiring a third party cannot dodge the principal purpose '
                                   'definition',
                                   'Alabama Consumer Protection Lawyers ([fPw38bPWFtw @ 00:00:17]); '
                                   'Alabama Consumer Protection Lawyers ([fPw38bPWFtw @ 00:02:40])'],
                                  ['Whether original creditors face the same conduct rules',
                                   'Simple Explain and Loman say the FDCPA reaches third-party collectors '
                                   'only, not banks',
                                   'ExamPrepAI says a hospital collecting its own debt still cannot bang '
                                   'on doors at 3:00 a.m.',
                                   'Simple Explain ([njrU1ZwxRCY @ 00:00:57]); ExamPrepAI CPA Review '
                                   '([uGQHaP-BNy0 @ 00:05:46])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The cheapest losses are self-inflicted on the phone and at the mailbox. '
                              'Jansen warns that simply saying "okay" when a collector asks to call back '
                              'counts as consent, which quietly unlocks contact the seven-in-seven rule '
                              'would otherwise block [9RtU4rpS3pw @ 00:06:29]. WealthCurve flags two '
                              'timing traps: the dispute must be in writing and should not be mailed on '
                              'day 29 of the 30-day window, and the one-year limit to sue runs from the '
                              'violation, not from when the consumer discovers it [cKYmFnf_o2Q @ '
                              '00:07:18]. Night Ferry puts the scale of the biggest trap on the table, '
                              'citing Pew 2020 data that more than 70% of collection suits end in default '
                              'judgments, and noting garnishment is capped at 25% with weekly income of '
                              '$217.50 or less exempt [7HVra7o-cZg @ 00:06:18]. Loman is blunt about '
                              'ignoring a lawsuit: never do it, because bank accounts can be levied and '
                              'frozen years later, defenses are gone once judgment is entered, and there '
                              'is no statute of limitations on a stipulated judgment; vacating one is a '
                              'state-court fight that would need a $5,000 to $10,000 retainer [n3SZjPQDSHc '
                              '@ 00:32:24]. Loman also reports that Arizona judgments last ten years, are '
                              'renewable, and can reach four times the original amount.',
                              'Consumers who do sue hit their own walls. Meet Jermaine walks through a '
                              'Southern District of Ohio case against Portfolio Recovery Associates where '
                              'the plaintiff alleged inaccurate disputed-status reporting and collection '
                              'without verification, and the court granted summary judgment for PRA '
                              'because it followed reasonable procedures and the errors were unintentional '
                              '[XSfDS_s1URg @ 00:02:59]. LawShelf identifies that same bona fide error '
                              'defense, along with good-faith reliance on an FTC advisory opinion, as the '
                              'main escape hatches for collectors [i6PAssklgJg @ 00:06:40]. Watts adds a '
                              'structural trap that catches debtors who think a violation erases the '
                              'balance: a section 1692g violation is not a defense against the debt, only '
                              'a claim against the collector [qTSer3pu6io @ 01:01:14]. Loman tempers '
                              'damages expectations, putting statutory damages at $100 to $1,000 and '
                              'reporting that some clients have received $1, while warning that '
                              'non-lump-sum settlements get filed with the court, so a single missed '
                              'payment produces an immediate judgment, and roughly 30% of litigated files '
                              'fail to update to Metro 2 code 64 with a zero balance afterward '
                              '[n3SZjPQDSHc @ 00:25:48]. The lesson from Jermaine is operational: copy '
                              'every letter and keep documentation, because many collectors do not fix '
                              'errors even after being called out.',
                              'On the other side of the table, the economics run on volume, and volume '
                              "breaks. Brian Parker's deposition of collection attorney Bradley Johnson "
                              'extracted the admission "we do about 50 a week so 10 a day," with the '
                              'complaint built from a form, the summons auto-generated, and address '
                              'scrubbing outsourced to LexisNexis with no state-ID search [RwXTJhX-rxo @ '
                              '00:21:52]. The same deposition exposed a December 2022 affidavit that '
                              'called Security Credit Services "plaintiff" before any suit existed, never '
                              'attached its Exhibit A, and carried no penalty-of-perjury clause, prompting '
                              'Parker\'s line that "an affidavit is not an affidavit unless it\'s signed '
                              'under penalty of perjury"; Colin Ward still paid $2,500 in settlement '
                              "[RwXTJhX-rxo @ 01:53:36]. Swift's silver case shows stubbornness turning "
                              'into losses: Discover lost one suit, then sued again seven years later '
                              'through a new collector using the same lawyers, and the consumer '
                              'counterclaimed for over $50,000 [owpVxkqEbEk @ 00:08:31]. Watts lays out '
                              'why buyers keep pushing: Crown "buys a thousand dollar debt for fifty '
                              'bucks" and a consumer may settle for $700, yet the court held that hiring a '
                              'third party to collect does not let a principal-purpose buyer escape the '
                              'FDCPA [fPw38bPWFtw @ 00:03:48].'],
               'table': {'caption': 'Firsthand failure modes and their reported consequences',
                         'headers': ['Failure Mode',
                                     'What Happened Firsthand',
                                     'Economic or Legal Consequence',
                                     'Expert Source'],
                         'rows': [['Saying okay to a collector callback request',
                                   'Jansen warns the casual yes is treated as consent to further contact',
                                   'Unlocks calls the seven-in-seven contact limit would otherwise block',
                                   'SeniorLiving.Org ([9RtU4rpS3pw @ 00:06:29])'],
                                  ['Ignoring a filed collection lawsuit entirely',
                                   'More than 70% of collection suits end in default judgments per Pew '
                                   '2020',
                                   'Garnishment up to 25% of wages above the $217.50 weekly exemption',
                                   'Night Ferry ([7HVra7o-cZg @ 00:06:18])'],
                                  ['Suing on reporting errors without strong evidence',
                                   'PRA won summary judgment because it followed reasonable procedures',
                                   'Bona fide error defense reaffirmed and plaintiffs need substantial '
                                   'evidence',
                                   'Meet Jermaine (Clear &Strategic) ([XSfDS_s1URg @ 00:02:59])'],
                                  ['Missing a payment on a court-filed settlement',
                                   'Non-lump-sum settlements are filed with the court by the collector',
                                   'A single missed payment leads to an immediate judgment against the '
                                   'consumer',
                                   'Solo – Resolve Your Debt ([n3SZjPQDSHc @ 00:39:47])'],
                                  ['Tradeline not updating after a paid settlement',
                                   'Loman reports about 30% of litigated files do not update correctly',
                                   'Must dispute by letter with the settlement, judgment, and payment '
                                   'proof',
                                   'Solo – Resolve Your Debt ([n3SZjPQDSHc @ 00:50:22])'],
                                  ['Collector suing on templated affidavits at volume',
                                   'Affidavit named a plaintiff before suit, lacked Exhibit A and perjury '
                                   'clause',
                                   "Exposed in deposition; firm still says its biggest client's form will "
                                   'not change',
                                   'KillDebt & ParkerGPT: The New Way To Law ([RwXTJhX-rxo @ 01:53:36])'],
                                  ['Collectors chasing debt that was already paid',
                                   'Loman calls it the most common violation, driven by bulk spreadsheet '
                                   'resales',
                                   'Paid accounts resurface with new collectors and trigger fresh FDCPA '
                                   'claims',
                                   'Solo – Resolve Your Debt ([n3SZjPQDSHc @ 00:13:41])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Four checks before engaging any collector',
                           'body': 'Each check is drawn from losses, reversals, or traps the practitioners '
                                   'reported firsthand.',
                           'items': ['Send the written dispute early by certified mail with return '
                                     'receipt; never mail it on day 29 of the 30-day window [WealthCurve — '
                                     'cKYmFnf_o2Q @ 00:03:01].',
                                     "Do not answer okay to a collector's request to call back unless "
                                     'further contact is intended, because it counts as consent '
                                     '[SeniorLiving.Org — 9RtU4rpS3pw @ 00:06:29].',
                                     'Never ignore a filed collection suit; once judgment is entered the '
                                     'defenses are gone and accounts can be levied years later [Solo – '
                                     'Resolve Your Debt — n3SZjPQDSHc @ 00:32:24].',
                                     'Build the evidence file before suing: a copy of every letter and its '
                                     '16-digit certified tracking number, since PRA beat a reporting claim '
                                     'on bona fide error [Meet Jermaine (Clear &Strategic) — XSfDS_s1URg @ '
                                     '00:06:09].']}}],
 'pull_quote': '"So the lesson is no case is too small." — Consumer Law 101 by Attorney Aaron Swift '
               '(owpVxkqEbEk @ 00:06:30).',
 'diagram_id': 'diag-06',
 'action_checklist': ['Screenshot and preserve every collector text, reply stop to the opt-out, and treat '
                      'any contact after that as actionable (SeniorLiving.Org, 9RtU4rpS3pw @ 00:08:21).',
                      'Send the written dispute by certified mail with return receipt inside the 30-day '
                      'window (WealthCurve, cKYmFnf_o2Q @ 00:05:45).',
                      'Tell the collector you cannot receive personal calls at work; any call after that '
                      'is a violation (Solo – Resolve Your Debt, n3SZjPQDSHc @ 00:20:44).',
                      'On medical debt, request your records including billing under HIPAA plus an '
                      'insurance accounting to catch double billing and code changes (Solo – Resolve Your '
                      'Debt, n3SZjPQDSHc @ 00:41:14).',
                      'Audit every charge against the four corners of the contract; an unauthorized 25% '
                      'collection fee violates section 1692f (KillDebt & ParkerGPT: The New Way To Law, '
                      'YYdsx06msa0 @ 00:03:38).',
                      'File FDCPA suits in state court to blunt Spokeo standing fights, and amend the '
                      'complaint as of right rather than litigating baseless motions to dismiss (Alabama '
                      'Consumer Protection Lawyers, Ce0D7z4zJFo @ 00:00:30).'],
 'statutory_citations': [{'title': 'SeniorLiving.Org — Regulation F: New Debt Collection Laws You Need to '
                                   "Know Even if You're not in Debt [00:05:51]",
                          'url': 'https://www.youtube.com/watch?v=9RtU4rpS3pw&t=351s',
                          'relevance': 'Primary practitioner testimony on the seven-in-seven call rule '
                                       'counted per account under Regulation F.'},
                         {'title': 'Alabama Consumer Protection Lawyers — New FDCPA Rules (Regulation F) '
                                   '-- Part One [00:32:18]',
                          'url': 'https://www.youtube.com/watch?v=qTSer3pu6io&t=1938s',
                          'relevance': 'Primary practitioner testimony on limited-content message '
                                       'requirements and barred phrases under Regulation F.'},
                         {'title': 'Solo – Resolve Your Debt — The Fair Debt Collection Practices Act '
                                   'Explained by an Attorney [00:34:56]',
                          'url': 'https://www.youtube.com/watch?v=n3SZjPQDSHc&t=2096s',
                          'relevance': 'Primary practitioner testimony on validation scope, pay-for-delete '
                                       'risk, and post-settlement reporting.'},
                         {'title': 'KillDebt & ParkerGPT: The New Way To Law — How To Take a Deposition of '
                                   'a Collection Attorney in a Debt Collection Case - Part 1 [01:53:36]',
                          'url': 'https://www.youtube.com/watch?v=RwXTJhX-rxo&t=6816s',
                          'relevance': 'Primary practitioner testimony on collection-attorney volume '
                                       'filing, scrubbing, and defective affidavits.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': '9RtU4rpS3pw',
                       'title': "Regulation F: New Debt Collection Laws You Need to Know Even if You're "
                                'not in Debt',
                       'channel': 'SeniorLiving.Org',
                       'author': 'SeniorLiving.Org',
                       'text': 'now debt collectors can only attempt to call you seven times in seven days '
                               "that's it.",
                       'tip': 'now debt collectors can only attempt to call you seven times in seven days '
                              "that's it.",
                       'timestamp': 351,
                       'timestamp_seconds': 351,
                       'timestamp_label': '[00:05:51]',
                       'url': 'https://www.youtube.com/watch?v=9RtU4rpS3pw&t=351s',
                       'markdown': '[00:05:51](https://www.youtube.com/watch?v=9RtU4rpS3pw&t=351s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Ce0D7z4zJFo',
                       'title': 'Overview of a typical FDCPA lawsuit against an abusive debt collector',
                       'channel': 'Alabama Consumer Protection Lawyers',
                       'author': 'Alabama Consumer Protection Lawyers',
                       'text': "the defendant the debt collector we've sued they either will answer the "
                               'case or they will move to dismiss the case.',
                       'tip': "the defendant the debt collector we've sued they either will answer the "
                              'case or they will move to dismiss the case.',
                       'timestamp': 86,
                       'timestamp_seconds': 86,
                       'timestamp_label': '[00:01:26]',
                       'url': 'https://www.youtube.com/watch?v=Ce0D7z4zJFo&t=86s',
                       'markdown': '[00:01:26](https://www.youtube.com/watch?v=Ce0D7z4zJFo&t=86s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'cKYmFnf_o2Q',
                       'title': 'Debt Collectors: Know Your Rights Before You Pay a Dollar 🛡️',
                       'channel': 'WealthCurve',
                       'author': 'WealthCurve',
                       'text': 'If you send a written dispute within that window, the collector must stop '
                               'all collection activity.',
                       'tip': 'If you send a written dispute within that window, the collector must stop '
                              'all collection activity.',
                       'timestamp': 181,
                       'timestamp_seconds': 181,
                       'timestamp_label': '[00:03:01]',
                       'url': 'https://www.youtube.com/watch?v=cKYmFnf_o2Q&t=181s',
                       'markdown': '[00:03:01](https://www.youtube.com/watch?v=cKYmFnf_o2Q&t=181s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'z04uhB8lcJU',
                       'title': 'Breaking news! FDCPA liability in evictions (CDC Order)',
                       'channel': 'Alabama Consumer Protection Lawyers',
                       'author': 'Alabama Consumer Protection Lawyers',
                       'text': 'Eviction lawyers count as debt collectors and must give clear and '
                               'conspicuous written notice of CDC moratorium eligibility with the eviction '
                               'notice.',
                       'tip': 'Eviction lawyers count as debt collectors and must give clear and '
                              'conspicuous written notice of CDC moratorium eligibility with the eviction '
                              'notice.',
                       'timestamp': 285,
                       'timestamp_seconds': 285,
                       'timestamp_label': '[00:04:45]',
                       'url': 'https://www.youtube.com/watch?v=z04uhB8lcJU&t=285s',
                       'markdown': '[00:04:45](https://www.youtube.com/watch?v=z04uhB8lcJU&t=285s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'YYdsx06msa0',
                       'title': 'The Power of the FDCPA 1692e and 1692f Against Debt Collectors',
                       'channel': 'KillDebt & ParkerGPT: The New Way To Law',
                       'author': 'KillDebt & ParkerGPT: The New Way To Law',
                       'text': 'It is impossible to garnish anybody without a judgment.',
                       'tip': 'It is impossible to garnish anybody without a judgment.',
                       'timestamp': 500,
                       'timestamp_seconds': 500,
                       'timestamp_label': '[00:08:20]',
                       'url': 'https://www.youtube.com/watch?v=YYdsx06msa0&t=500s',
                       'markdown': '[00:08:20](https://www.youtube.com/watch?v=YYdsx06msa0&t=500s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'njrU1ZwxRCY',
                       'title': 'Fair Debt Collection Practices Act (FDCPA): Definition and Rules',
                       'channel': 'Simple Explain',
                       'author': 'Simple Explain',
                       'text': 'they may not call more than seven times in a 7-Day period.',
                       'tip': 'they may not call more than seven times in a 7-Day period.',
                       'timestamp': 129,
                       'timestamp_seconds': 129,
                       'timestamp_label': '[00:02:09]',
                       'url': 'https://www.youtube.com/watch?v=njrU1ZwxRCY&t=129s',
                       'markdown': '[00:02:09](https://www.youtube.com/watch?v=njrU1ZwxRCY&t=129s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'qTSer3pu6io',
                       'title': 'New FDCPA Rules (Regulation F) -- Part One',
                       'channel': 'Alabama Consumer Protection Lawyers',
                       'author': 'Alabama Consumer Protection Lawyers',
                       'text': 'a consumer is a natural person obligated or allegedly obligated to pay any '
                               'debt.',
                       'tip': 'a consumer is a natural person obligated or allegedly obligated to pay any '
                              'debt.',
                       'timestamp': 1333,
                       'timestamp_seconds': 1333,
                       'timestamp_label': '[00:22:13]',
                       'url': 'https://www.youtube.com/watch?v=qTSer3pu6io&t=1333s',
                       'markdown': '[00:22:13](https://www.youtube.com/watch?v=qTSer3pu6io&t=1333s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '7HVra7o-cZg',
                       'title': "Debt Collector Rights: What They Can and Can't Do",
                       'channel': 'Night Ferry',
                       'author': 'Night Ferry',
                       'text': "Texts and emails aren't counted, but can't harass either, and each must "
                               'offer a simple opt-out.',
                       'tip': "Texts and emails aren't counted, but can't harass either, and each must "
                              'offer a simple opt-out.',
                       'timestamp': 244,
                       'timestamp_seconds': 244,
                       'timestamp_label': '[00:04:04]',
                       'url': 'https://www.youtube.com/watch?v=7HVra7o-cZg&t=244s',
                       'markdown': '[00:04:04](https://www.youtube.com/watch?v=7HVra7o-cZg&t=244s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'fPw38bPWFtw',
                       'title': 'Case Decision FDCPA Definition of Debt Collector of Debt Buyer --  '
                                'Barbato v Crown Asset',
                       'channel': 'Alabama Consumer Protection Lawyers',
                       'author': 'Alabama Consumer Protection Lawyers',
                       'text': 'an entity that otherwise meets the principal purpose definition cannot '
                               'avoid the dictates of the FDCPA merely by hiring a third party to do its '
                               'collecting.',
                       'tip': 'an entity that otherwise meets the principal purpose definition cannot '
                              'avoid the dictates of the FDCPA merely by hiring a third party to do its '
                              'collecting.',
                       'timestamp': 160,
                       'timestamp_seconds': 160,
                       'timestamp_label': '[00:02:40]',
                       'url': 'https://www.youtube.com/watch?v=fPw38bPWFtw&t=160s',
                       'markdown': '[00:02:40](https://www.youtube.com/watch?v=fPw38bPWFtw&t=160s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '9VNthZZ6JNk',
                       'title': 'What a New Bill in Congress Means for Collection Attorney Litigation | '
                                'Ep. 271',
                       'channel': 'Receivables Info | Debt Collection News',
                       'author': 'Receivables Info | Debt Collection News',
                       'text': "We shouldn't have to be governed by two masters and that's pretty much the "
                               'big picture.',
                       'tip': "We shouldn't have to be governed by two masters and that's pretty much the "
                              'big picture.',
                       'timestamp': 172,
                       'timestamp_seconds': 172,
                       'timestamp_label': '[00:02:52]',
                       'url': 'https://www.youtube.com/watch?v=9VNthZZ6JNk&t=172s',
                       'markdown': '[00:02:52](https://www.youtube.com/watch?v=9VNthZZ6JNk&t=172s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'owpVxkqEbEk',
                       'title': 'Debt Collector Lawsuits (FDCPA): Examples and Outcomes by Attorney Aaron '
                                'Swift',
                       'channel': 'Consumer Law 101 by Attorney Aaron Swift',
                       'author': 'Consumer Law 101 by Attorney Aaron Swift',
                       'text': 'so two technical violations led to a debt almost completely erased like it '
                               'never existed.',
                       'tip': 'so two technical violations led to a debt almost completely erased like it '
                              'never existed.',
                       'timestamp': 356,
                       'timestamp_seconds': 356,
                       'timestamp_label': '[00:05:56]',
                       'url': 'https://www.youtube.com/watch?v=owpVxkqEbEk&t=356s',
                       'markdown': '[00:05:56](https://www.youtube.com/watch?v=owpVxkqEbEk&t=356s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'i6PAssklgJg',
                       'title': 'Fair Debt Collection Practices Act',
                       'channel': 'LawShelf',
                       'author': 'LawShelf',
                       'text': 'in many cases the potential that attorneys fees may be imposed drives '
                               'FDCPA litigation.',
                       'tip': 'in many cases the potential that attorneys fees may be imposed drives FDCPA '
                              'litigation.',
                       'timestamp': 323,
                       'timestamp_seconds': 323,
                       'timestamp_label': '[00:05:23]',
                       'url': 'https://www.youtube.com/watch?v=i6PAssklgJg&t=323s',
                       'markdown': '[00:05:23](https://www.youtube.com/watch?v=i6PAssklgJg&t=323s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'uGQHaP-BNy0',
                       'title': 'The Fair Debt Collection Practices Act (FDCPA) [CPA Prep]',
                       'channel': 'ExamPrepAI CPA Review',
                       'author': 'ExamPrepAI CPA Review',
                       'text': "just because someone says you owe money doesn't mean you actually owe it.",
                       'tip': "just because someone says you owe money doesn't mean you actually owe it.",
                       'timestamp': 262,
                       'timestamp_seconds': 262,
                       'timestamp_label': '[00:04:22]',
                       'url': 'https://www.youtube.com/watch?v=uGQHaP-BNy0&t=262s',
                       'markdown': '[00:04:22](https://www.youtube.com/watch?v=uGQHaP-BNy0&t=262s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'n3SZjPQDSHc',
                       'title': 'The Fair Debt Collection Practices Act Explained by an Attorney',
                       'channel': 'Solo – Resolve Your Debt',
                       'author': 'Solo – Resolve Your Debt',
                       'text': 'That is absolutely not the law.',
                       'tip': 'That is absolutely not the law.',
                       'timestamp': 2096,
                       'timestamp_seconds': 2096,
                       'timestamp_label': '[00:34:56]',
                       'url': 'https://www.youtube.com/watch?v=n3SZjPQDSHc&t=2096s',
                       'markdown': '[00:34:56](https://www.youtube.com/watch?v=n3SZjPQDSHc&t=2096s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'n3SZjPQDSHc',
                       'title': 'The Fair Debt Collection Practices Act Explained by an Attorney',
                       'channel': 'Solo – Resolve Your Debt',
                       'author': 'Solo – Resolve Your Debt',
                       'text': "Now, going back to what you were saying, statute of limitations, there's "
                               'no statute of limitations on a stipulated judgment.',
                       'tip': "Now, going back to what you were saying, statute of limitations, there's no "
                              'statute of limitations on a stipulated judgment.',
                       'timestamp': 3518,
                       'timestamp_seconds': 3518,
                       'timestamp_label': '[00:58:38]',
                       'url': 'https://www.youtube.com/watch?v=n3SZjPQDSHc&t=3518s',
                       'markdown': '[00:58:38](https://www.youtube.com/watch?v=n3SZjPQDSHc&t=3518s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'XSfDS_s1URg',
                       'title': 'Avoid This Credit Dispute Mistake! #FDCPA Law Suit Case Study '
                                '#askadebtcollector #advice #law',
                       'channel': 'Meet Jermaine (Clear &Strategic)',
                       'author': 'Meet Jermaine (Clear &Strategic)',
                       'text': "that's why it's important that you certify mail it then you get a 16-digit "
                               'tracking number as a receipt and you can check when that document was '
                               'actually delivered to the company.',
                       'tip': "that's why it's important that you certify mail it then you get a 16-digit "
                              'tracking number as a receipt and you can check when that document was '
                              'actually delivered to the company.',
                       'timestamp': 369,
                       'timestamp_seconds': 369,
                       'timestamp_label': '[00:06:09]',
                       'url': 'https://www.youtube.com/watch?v=XSfDS_s1URg&t=369s',
                       'markdown': '[00:06:09](https://www.youtube.com/watch?v=XSfDS_s1URg&t=369s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'RwXTJhX-rxo',
                       'title': 'How To Take a Deposition of a Collection Attorney in a Debt Collection '
                                'Case - Part 1',
                       'channel': 'KillDebt & ParkerGPT: The New Way To Law',
                       'author': 'KillDebt & ParkerGPT: The New Way To Law',
                       'text': "do you understand that an affidavit is not an affidavit unless it's signed "
                               'under penalty of perjury.',
                       'tip': "do you understand that an affidavit is not an affidavit unless it's signed "
                              'under penalty of perjury.',
                       'timestamp': 6816,
                       'timestamp_seconds': 6816,
                       'timestamp_label': '[01:53:36]',
                       'url': 'https://www.youtube.com/watch?v=RwXTJhX-rxo&t=6816s',
                       'markdown': '[01:53:36](https://www.youtube.com/watch?v=RwXTJhX-rxo&t=6816s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'}]}
