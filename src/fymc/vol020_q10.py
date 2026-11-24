from __future__ import annotations

CHAPTER_10 = {'id': 'Q10',
 'chapter_id': 'Q10',
 'chapter_number': 10,
 'question_number': 10,
 'slug': 'navigating-the-far-and-contract-administration',
 'question_prompt': 'Which parts of the FAR actually matter to a small contractor, and how is the FAR '
                    'overhaul changing them?',
 'kicker': 'Q10 / THE BIG MONEY PLAYBOOKS',
 'title': 'Navigating the FAR and Contract Administration',
 'subtitle': 'FAR structure and the parts that matter, Part 1 authority and unauthorized commitments, Part '
             '4 registration data and CAGE updates, Part 34 scope, schedule and cost, Part 52 clauses, '
             'Part 47 transportation and FOB terms, Part 33 protests vs. claims, and the Revolutionary FAR '
             'Overhaul',
 'layout_template': 'expert_commentary',
 'reading_time_minutes': 15,
 'executive_summary': 'Practitioners from PCI, GovSuccess, Contract Warrior, FedAccess, Neybor and GovCon '
                      'Empire converge on one operating rule: only the contracting officer binds the '
                      'government, and the clauses physically in your contract govern your money. Tim '
                      'Sullivan and Christopher Williams both treat CORs as having zero contracting '
                      'authority, and Williams describes a contractor filing a roughly $38k REA after a '
                      "COR-directed ductwork move. Street mechanics center on Ctrl-F for '52.2', checking "
                      'clause dates, flagging the 30-day change notice, the 60-day/75% limitation-of-cost '
                      'warning, and $100,000 claim certification. FAR overhaul operators report about 25% '
                      'of the text moved to companion guides and Part 12 awards in roughly 45 days versus '
                      '5+ months under Part 15. They split on how to read clause numbers, how many pages '
                      'the FAR runs, and whether to read it at all.',
 'key_metrics': [{'label': 'FAR Content Removed in the Overhaul',
                  'metric': 'FAR Content Removed in the Overhaul',
                  'value': 'About 25%',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Tim Sullivan reports roughly a quarter of the FAR was moved to companion '
                             'guides under the April executive order, and that moved material cannot '
                             'support protests.',
                  'source': 'Public Contracting Institute (PCI) ([Gisvrg813kY @ 00:18:42])'},
                 {'label': 'Part 12 vs Part 15 Award Speed',
                  'metric': 'Part 12 vs Part 15 Award Speed',
                  'value': 'About 45 days vs 5+ months',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Neybor Consulting contrasts commercial Part 12 awards with Part 15 '
                             'negotiated awards, alongside more than 60% of federal buys using commercial '
                             'authority and a $7.5M threshold ($15M in emergencies) under FAR 2.0.',
                  'source': 'Neybor Consulting ([TFl20T0yyig @ 00:02:10])'},
                 {'label': 'REA After a COR-Directed Change',
                  'metric': 'REA After a COR-Directed Change',
                  'value': 'About $38k',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Christopher Williams describes a COR ordering ductwork offset 6 ft north; '
                             'three weeks later the contractor filed an REA of about $38k even though the '
                             'COR had no warrant.',
                  'source': 'Contract Warrior ([pktnZU4AWIE @ 00:04:13])'},
                 {'label': 'Claim Certification Threshold',
                  'metric': 'Claim Certification Threshold',
                  'value': 'Over $100,000',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Former Air Force procurement litigators state claims over $100,000 must be '
                             'certified, which starts the disputes process; claims carry a 6-year limit '
                             'and earn CDA interest while REAs do not.',
                  'source': 'How To Sell To & Win Federal Government Contracts ([h1yszOmFw3w @ '
                            '01:01:54])'}],
 'sections': [{'heading': 'Section 1: The Practitioner Consensus',
               'paragraphs': ['The hardest consensus in this chapter is about who can spend the '
                              "government's money. GovSuccess opens FAR Part 1 with a customer asking for "
                              'extra work and says the first question is authority, not enthusiasm: '
                              'contracting officers bind the government only within delegated authority, '
                              'while a COR works under a written designation and cannot change price, '
                              'quantity, delivery or terms [x7xmTiXnwQ4 @ 00:00:17]. Tim Sullivan of PCI, '
                              'who logged two years as a contracting officer and decades as a contractor '
                              'lawyer, hammers the same line in plain terms: CORs have no contracting '
                              'authority, so loop every scope question back to the CO, in writing '
                              '[Gisvrg813kY @ 01:12:28]. Christopher Williams, a KO for 17 years, puts '
                              'teeth on it from the construction side: a COR carries no warrant and cannot '
                              'alter the scope of work [pktnZU4AWIE @ 00:04:31]. Sky and Michelle, former '
                              'Air Force procurement litigators, add why this bites so often: constructive '
                              'changes frequently happen orally in meetings, and the changes clause '
                              'expects the contractor to notify the CO, typically within 30 days, though '
                              'they tell operators to read the actual clause [h1yszOmFw3w @ 00:14:08]. '
                              'GovSuccess adds that job titles, relationships and urgency never create '
                              'authority, and that ratification is a conditional process, not a dependable '
                              'business plan.',
                              'The second point of agreement: the clauses inside your own contract are '
                              'what you actually live under, and they carry real legal weight. Sullivan '
                              'reports that courts hold the FAR has the force and effect of law, and that '
                              'a FAR violation that hurt a protester means the solicitation is probably '
                              'going down [Gisvrg813kY @ 00:13:10]. David Gallagher of Kutak Rock, with '
                              '20-plus years in the field, maps the stack: the FAR sits in 48 CFR Chapter '
                              '1, and agency supplements such as DFARS and HSAR usually add to it and '
                              'occasionally displace it, with data rights and country of origin as the '
                              'examples [UV6zJLRHfHw @ 00:09:38]. FedAccess frames the operator version '
                              "bluntly: the FAR runs about 2,000 pages, so don't read it, read your "
                              'clauses, because invoicing, progress payments and fast payment are set by '
                              'your contract rather than by generic FAR searching [T_cRpZF2IUo @ '
                              '00:00:00]. ASI Education lands in the same place from a study angle, noting '
                              'Part 52 is the only part addressed to the contractor and the longest, and '
                              'recommending one clause a day [MTy_zJd0RsY @ 00:02:41]. Gallagher counts '
                              'more than 600 clauses and splits them into instructional, certification, '
                              'prohibition and requirement buckets, with requirement-clause noncompliance '
                              'meaning breach or default.',
                              'The third consensus covers the FAR overhaul: buying is getting faster, but '
                              'the text you read online may not be the text your agency implemented. '
                              'Sullivan traces the April executive order, Restoring Common Sense to '
                              'Federal Procurement, which kept only content required by law or essential '
                              'to sound procurement, and reports about 25% of the FAR moved to companion '
                              'guides that cannot support protests [Gisvrg813kY @ 00:18:42]. Derrick '
                              'Green, an ex-CO at DoD, DHS, FEMA, VA and Houston, tells vendors to have '
                              'pricing, staffing, insurance, references and an operational story ready '
                              'because awards may now arrive in days, not months [k1EsNHPfqXY @ 00:09:13]. '
                              'GovSuccess runs the counterweight across multiple episodes: an overhaul '
                              'model is not automatically the text your agency implemented [z7tDxORX_pQ @ '
                              '00:01:42], and codified and overhaul section numbers differ, so the '
                              'operator has to verify which version actually applies [LgX6N2c9-S4 @ '
                              "00:00:33]. Fed Gov Today's guest Matthew Rose of Snowflake describes the "
                              'culture shift behind it: more commercial technology buying, Part 10 market '
                              'research, and agencies paying for outcomes rather than level of effort. '
                              "Green's line on the tempo is that faster does not mean reckless, it just "
                              'means smarter.'],
               'table': {'caption': 'Where the practitioners agree on authority, clauses and the overhaul',
                         'headers': ['Consensus Point',
                                     'What Practitioners Say',
                                     'Operator Implication',
                                     'Expert Source'],
                         'rows': [['Only the contracting officer binds the government',
                                   'CORs have no contracting authority; scope questions go back to the CO '
                                   'in writing',
                                   'Never start extra work on a COR instruction without written CO '
                                   'confirmation',
                                   'Public Contracting Institute (PCI) ([Gisvrg813kY @ 01:12:28])'],
                                  ['COR limits sit inside a written designation',
                                   'A COR monitors and administers but cannot change price, quantity, '
                                   'delivery, or terms',
                                   'Check every customer request against the written designation and the '
                                   'contract scope',
                                   'Win Government Contracts with GovSuccess ([x7xmTiXnwQ4 @ 00:00:17])'],
                                  ['No warrant means no scope change',
                                   'A COR-ordered ductwork offset of 6 ft north turned into an REA of '
                                   'about $38k',
                                   "Get the KO's confirmation before moving a single duct or crew",
                                   'Contract Warrior ([pktnZU4AWIE @ 00:04:13])'],
                                  ['The FAR carries the force of law',
                                   'Courts hold the FAR has the force and effect of law; violations sink '
                                   'solicitations',
                                   'A FAR violation that impacted your offer is real protest leverage',
                                   'Public Contracting Institute (PCI) ([Gisvrg813kY @ 00:13:10])'],
                                  ['Your contract clauses govern, not generic FAR searches',
                                   'The FAR runs about 2,000 pages; read the clauses in your own contract '
                                   'instead',
                                   'Pull your solicitation clause list before researching any FAR question '
                                   'at all',
                                   'FedAccess ([T_cRpZF2IUo @ 00:00:00])'],
                                  ['Agency supplements add to and sometimes displace the FAR',
                                   'DFARS and HSAR usually add requirements and occasionally displace FAR '
                                   'rules like data rights',
                                   'Read the agency supplement alongside the FAR on every single award',
                                   'Public Contracting Institute (PCI) ([UV6zJLRHfHw @ 00:09:38])'],
                                  ['Overhaul model text is not implemented text',
                                   'An overhaul model is not automatically the text your agency actually '
                                   'implemented',
                                   'Confirm the current FAR, agency deviation, and contract language '
                                   'before relying on it',
                                   'Win Government Contracts with GovSuccess ([z7tDxORX_pQ @ '
                                   '00:01:42])']]}},
              {'heading': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ["The clause-reading workflow starts with a keyword hunt. Gallagher's tactic "
                              "is to Ctrl-F the solicitation for '52.2' to surface every FAR clause, then "
                              'repeat for the supplement prefixes: DFARS clauses start with 252, GSA with '
                              '552 and VA with 852 [UV6zJLRHfHw @ 00:29:28]. Clauses show up in full text '
                              'or by reference in Sections H, I and K, and the date matters: 52.243-1 '
                              'dated April 1984 versus August 1987 is unchanged after 37 years, but Buy '
                              'American versions from February 2009 and October 2022 differ materially. An '
                              'undated clause most likely means the version in effect at signing, and '
                              'Gallagher calls the idea of a self-refreshing clause wrong, just as there '
                              'is no such thing as a self-deleting flow-down [UV6zJLRHfHw @ 00:38:30]. '
                              "FedAccess's shortcut for the unfamiliar ones is to Google the clause "
                              'together with its date [T_cRpZF2IUo @ 00:03:04]. Sullivan adds a tracing '
                              "step: every clause says 'as prescribed by' a section, so trace each clause "
                              'back to its prescription, and use the 52.3 matrix, which codes clauses R, A '
                              "or O [Gisvrg813kY @ 00:57:25]. On fill-ins, Gallagher's rule is short: "
                              'blank means blank, and the government cannot fill in a 52.244-2 blank six '
                              'months later.',
                              "Post-award money runs on hard clocks. Sky and Michelle's numbers: notify "
                              'the CO of a change typically within 30 days, recover the cost of the change '
                              'plus reasonable profit, and remember commercial contracts allow no '
                              'constructive change [h1yszOmFw3w @ 00:14:08]. Williams ties the same 30-day '
                              'notice to the changes clause and warns that late claims are scraping the '
                              'pan, because costs still have to be allowable, allocable and reasonable '
                              "[pktnZU4AWIE @ 00:05:12]. Sullivan's rule while a dispute runs is to keep "
                              'performing as directed and file a claim in parallel; the example is quoting '
                              '$2M while the agency offers $1M [Gisvrg813kY @ 00:39:41]. The KW partners '
                              'then stack the claim math: claims over $100,000 must be certified and start '
                              'the disputes process, the limit is six years, CDA interest runs on claims, '
                              'and REA preparation costs are recoverable but REAs earn no CDA interest '
                              '[h1yszOmFw3w @ 01:01:54]. Their other clocks include a limitation-of-cost '
                              'notice within 60 days of reaching 75%, a termination-for-convenience '
                              'settlement proposal within one year with an inventory schedule inside 120 '
                              'days, a 10-day cure notice for some default grounds, and 90 days to the '
                              'board or a year to the Court of Federal Claims to appeal a default.',
                              'On the front end, Neybor Consulting lays out the Part 12 economics: more '
                              'than 60% of federal buys use commercial authority, FAR 2.0 raises the '
                              'threshold to $7.5M or $15M in emergencies, and a Part 12 award takes about '
                              '45 days versus 5-plus months under Part 15 [TFl20T0yyig @ 00:02:10]. The '
                              'timeline Neybor teaches is a synopsis of about 15 days, evaluation in 1 to '
                              '4 weeks and award in 30 to 60 days, with the contractor signing block 30 '
                              'and the CO signing block 31; firm-fixed-price is the default, so price '
                              'accordingly, and cost-type is prohibited [TFl20T0yyig @ 00:15:50]. '
                              'FedAccess flags that SCA and Davis-Bacon wage determinations drive pricing '
                              'and that 52.219-14 limitations on subcontracting matters for middleman '
                              'strategies. GovSuccess pushes delivery math: compare FOB origin and '
                              'destination quotes on a total-delivered-cost basis covering freight, '
                              'packaging, appointments and unloading, because the lowest unit price may '
                              'not produce the lowest supported delivery cost [QvsXldnQyAg @ 00:02:31]. '
                              'Registration hygiene closes the loop. Federal Processing Registry says to '
                              'update a CAGE record within 30 days of an address, ownership or structure '
                              'change; DLA review takes 3 to 7 business days, and past 10 days you call '
                              'the DLA Customer Interaction Center [ifMU9O8Ydmg @ 00:01:23].'],
               'table': {'caption': 'Clocks, thresholds and tools operators run against the FAR',
                         'headers': ['Mechanic',
                                     'Exact Number or Tool',
                                     'How Operators Use It',
                                     'Expert Source'],
                         'rows': [['Clause discovery in the solicitation',
                                   "Ctrl-F '52.2', then 252 for DFARS, 552 for GSA, 852 for VA",
                                   'Surface every FAR and supplement clause buried in the solicitation '
                                   'package',
                                   'Public Contracting Institute (PCI) ([UV6zJLRHfHw @ 00:29:28])'],
                                  ['Change notice to the contracting officer',
                                   'Notify the CO typically within 30 days, but read your clause',
                                   'Log every oral meeting direction and send written notice fast',
                                   'How To Sell To & Win Federal Government Contracts ([h1yszOmFw3w @ '
                                   '00:14:08])'],
                                  ['Claim certification and disputes entry',
                                   'Claims over $100,000 must be certified to start the disputes process',
                                   'Convert stalled REAs into certified claims when CDA interest matters',
                                   'How To Sell To & Win Federal Government Contracts ([h1yszOmFw3w @ '
                                   '01:01:54])'],
                                  ['Limitation of cost or funds warning',
                                   'Notify within 60 days of reaching 75%; you may stop at the ceiling',
                                   'Stop work at the funding ceiling instead of performing unfunded effort',
                                   'How To Sell To & Win Federal Government Contracts ([h1yszOmFw3w @ '
                                   '00:55:17])'],
                                  ['Part 12 commercial award speed',
                                   'About 45 days versus 5-plus months under Part 15 negotiations',
                                   'Keep FFP pricing and past performance ready to respond in days',
                                   'Neybor Consulting ([TFl20T0yyig @ 00:02:10])'],
                                  ['CAGE record correction in SAM',
                                   'Update within 30 days of change; DLA review takes 3 to 7 business days',
                                   'Call the DLA Customer Interaction Center once review passes 10 days',
                                   'Federal Processing Registry ([ifMU9O8Ydmg @ 00:01:23])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Moves the veterans actually run',
                           'body': 'Small habits from former contracting officers and procurement '
                                   'litigators that protect bid money, flow-down exposure and pricing.',
                           'items': ['Never wait until the last minute: an electronic proposal sent before '
                                     '5:00 the prior day and delayed by government fault must be accepted, '
                                     'otherwise late is late, and even when you win, ask for a debriefing '
                                     '[Public Contracting Institute (PCI) — Gisvrg813kY @ 00:26:41].',
                                     'Treat local clauses as the dangerous ones: they skip public comment, '
                                     'which is why Sullivan calls them doozies [Public Contracting '
                                     'Institute (PCI) — Gisvrg813kY @ 01:01:45].',
                                     "Don't flow down all of 52.2 to subs; the mandatory lists live in "
                                     '52.244-6 and 52.212-5(e), and 244-7000 tells primes to limit '
                                     'flow-downs [Public Contracting Institute (PCI) — UV6zJLRHfHw @ '
                                     '00:56:54].',
                                     'Under TINA, exempt under $2M, you must disclose a cheaper vendor you '
                                     'know about when pricing [How To Sell To & Win Federal Government '
                                     'Contracts — h1yszOmFw3w @ 00:39:13].']},
               'sop_steps': [{'step': 1,
                              'title': 'Build the authority sheet',
                              'action': 'List the contracting officer, the designated technical '
                                        'representative, your authorized company signer and your internal '
                                        'escalation owner, and keep the award, modifications and '
                                        'delegations accessible.',
                              'detail': 'Drill staff on where to route scope requests so the team responds '
                                        'promptly without making commitments based on assumptions [Win '
                                        'Government Contracts with GovSuccess — x7xmTiXnwQ4 @ 00:01:24].'},
                             {'step': 2,
                              'title': 'Map every clause and its date',
                              'action': "Ctrl-F '52.2' and the supplement prefixes, note full-text versus "
                                        'by-reference clauses in Sections H, I and K, and record each '
                                        'clause date.',
                              'detail': 'Treat an undated clause as the version at signing, never assume '
                                        'self-refresh or self-deleting, and remember blank means blank '
                                        '[Public Contracting Institute (PCI) — UV6zJLRHfHw @ 00:29:28].'},
                             {'step': 3,
                              'title': 'Route and document every change',
                              'action': 'When a COR or field rep directs work outside scope, stop and get '
                                        "the KO's confirmation before performing.",
                              'detail': 'Send the 30-day changes-clause notice and keep costs allowable, '
                                        'allocable and reasonable, because late claims are scraping the '
                                        'pan [Contract Warrior — pktnZU4AWIE @ 00:06:55].'},
                             {'step': 4,
                              'title': 'Split protest files from claim files',
                              'action': 'Open a protest file (action, interest, forum, filing rules) '
                                        'separate from a claim file (contractual basis, relief, '
                                        'certification).',
                              'detail': 'Never import protest deadlines into a claim or confuse the '
                                        'submission period with the appeal period, and keep evidence of '
                                        'delivery and receipt [Win Government Contracts with GovSuccess — '
                                        '-smvR-8_v1M @ 00:00:55].'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The first split is how deep to go into the regulation itself. FedAccess '
                              'says the FAR runs 2,000 pages and flatly tells operators not to read it. '
                              'Instead, read the clauses in your own solicitation, then Google each clause '
                              'with its date [T_cRpZF2IUo @ 00:00:00]. ASI Education runs the opposite '
                              'drill: memorize all 53 parts with the "Colt 45" mnemonic, read Part 52 one '
                              'clause a day, and master Parts 15 and 13 [MTy_zJd0RsY @ 00:01:47]. ASI also '
                              'anchors its read on 1.102(d): "if it\'s not prohibited it\'s okay." Even '
                              'the clause numbering gets read two ways. FedAccess parses 52.219-14 as '
                              'subpart 2, section 219, and flags it as the limitations-on-subcontracting '
                              'clause that matters for middleman strategies [T_cRpZF2IUo @ 00:02:44]. '
                              'David Gallagher of Kutak Rock reads the digits after 52.2 as the FAR part '
                              'that prescribes the clause, and says the "numerology nomenclature" alone '
                              'tells you where a clause lives and why [UV6zJLRHfHw @ 00:30:26]. Gallagher '
                              'adds that supplements carry their own prefixes: DFARS 252, GSA 552 and VA '
                              '852. The page count splits too, with ASI Education saying 1,000 plus pages '
                              'and FedAccess saying 2,000. Pick one reading system, but trace every clause '
                              'back to its prescription and date before you price.',
                              'The FAR overhaul splits the room between operators sprinting for speed and '
                              'operators slowing down to verify the text. Derrick Green "Theo," an ex-CO '
                              'at DoD, DHS, FEMA, VA and Houston, says to stop wasting six months '
                              'pretending 200 vendors exist. Have pricing, staffing, insurance, references '
                              'and an operational story ready, because you may get "days, not months" '
                              '[k1EsNHPfqXY @ 00:09:13]. Neybor Consulting pushes the same tempo through '
                              'Part 12. More than 60 percent of federal buys use commercial authority, FAR '
                              '2.0 raises the threshold to $7.5M or $15M in emergencies, and a Part 12 '
                              'award lands in about 45 days versus 5+ months under Part 15 [TFl20T0yyig @ '
                              '00:02:10]. GovSuccess runs the counter-playbook. Its Part 34 breakdown '
                              'warns that an overhaul model is not automatically the text your agency '
                              'implemented. Its Part 47 breakdown adds that FAC 2026-01, effective March '
                              '13, 2026, still has to be checked against deviations [z7tDxORX_pQ @ '
                              '00:01:42]. Fed Gov Today guest Matthew Rose of Snowflake reports a pricing '
                              'split as well: buyers are moving from paying for level of effort to paying '
                              'for outcomes, yet utility-based pricing is still "not the norm" '
                              "[MM4DJrI2Od0 @ 00:02:16]. Neybor's hedge is blunt: expect FFP and price "
                              'accordingly.',
                              'When a fight starts, practitioners split on which lever to pull. Tim '
                              'Sullivan says a FAR violation that impacted the protester means the '
                              'solicitation is "probably going down." Yet in one sole-source dispute, '
                              'Sullivan skipped the protest and wrote to the competition advocate instead '
                              '[Gisvrg813kY @ 00:23:38]. Sullivan also warns that the overhaul moved about '
                              '25 percent of the FAR into companion guides, and that material cannot '
                              "support protests. On performance disputes, Sullivan's playbook is to keep "
                              'performing as directed and file a claim in parallel, using the case where '
                              'you quote $2M and the agency offers $1M [Gisvrg813kY @ 00:39:41]. Sky and '
                              'Michelle, former Air Force procurement litigators, agree that the disputes '
                              'clause demands continued performance. They add that a breach exists only '
                              'for a cardinal change, so get counsel before stopping, and that commercial '
                              'contracts allow no constructive change at all [h1yszOmFw3w @ 00:12:48]. '
                              'GovSuccess refuses to blend the two paths. A protest file tracks action, '
                              'interest, forum and filing rules. A claim file tracks contractual basis, '
                              'relief and certification. A clarification request, debriefing, REA and '
                              'claim are not interchangeable [-smvR-8_v1M @ 00:00:55]. Gallagher adds a '
                              'subcontract wrinkle: the majority view keeps the Christian doctrine off '
                              'subcontracts, and Chevron changes likely limit it further.'],
               'table': {'caption': 'Competing Playbooks on Reading, Speed, Pricing and Disputes',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['How much of the FAR an operator should actually read',
                                   'Skip the 2,000 pages and read only the clauses in your solicitation',
                                   'Memorize all 53 parts with Colt 45 and read one Part 52 clause daily',
                                   'FedAccess ([T_cRpZF2IUo @ 00:00:00]); ASI Education ([MTy_zJd0RsY @ '
                                   '00:01:47])'],
                                  ['Decoding a clause number like 52.219-14',
                                   'Read it as subpart 2, section 219, and treat it as the middleman '
                                   'limitations clause',
                                   'Read the digits after 52.2 as the FAR part that prescribes the clause',
                                   'FedAccess ([T_cRpZF2IUo @ 00:02:44]); Public Contracting Institute '
                                   '(PCI) ([UV6zJLRHfHw @ 00:30:26])'],
                                  ['Tempo under the FAR overhaul and faster award cycles',
                                   'Have pricing, staffing, insurance, references and an operational story '
                                   'ready for days-not-months turnarounds',
                                   'Check deviations first, because the overhaul model is not your '
                                   "agency's implemented text",
                                   'GovCon Empire with Derrick Green “Theo” ([k1EsNHPfqXY @ 00:09:13]); '
                                   'Win Government Contracts with GovSuccess ([z7tDxORX_pQ @ 00:01:42])'],
                                  ['Pricing model for commercial technology buys',
                                   'Expect firm-fixed-price as the Part 12 default and price accordingly',
                                   'Pitch paying for outcomes, knowing utility-based pricing is still not '
                                   'the norm',
                                   'Neybor Consulting ([TFl20T0yyig @ 00:09:21]); Fed Gov Today '
                                   '([MM4DJrI2Od0 @ 00:03:24])'],
                                  ['Challenging a sole-source buy you think is flawed',
                                   'Protest when a FAR violation impacted you, because the solicitation is '
                                   'probably going down',
                                   'Skip the protest and write directly to the agency competition advocate '
                                   'instead',
                                   'Public Contracting Institute (PCI) ([Gisvrg813kY @ 00:14:13]); Public '
                                   'Contracting Institute (PCI) ([Gisvrg813kY @ 00:23:38])'],
                                  ['Disputed government direction during contract performance',
                                   'Keep performing as directed and file a claim in parallel with the work',
                                   'Get counsel before stopping, since breach exists only for a cardinal '
                                   'change',
                                   'Public Contracting Institute (PCI) ([Gisvrg813kY @ 00:39:41]); How To '
                                   'Sell To & Win Federal Government Contracts ([h1yszOmFw3w @ 00:12:48])'],
                                  ['Undated clause sitting in a long-running contract',
                                   'Some contractors assume undated clauses self-refresh to the newest '
                                   'published version',
                                   'Gallagher says undated most likely means the version at signing, and '
                                   'self-refresh is wrong',
                                   'Public Contracting Institute (PCI) ([UV6zJLRHfHw @ 00:38:30])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ["The most expensive trap reported firsthand is working off a COR's say-so. "
                              'Christopher Williams of Contract Warrior, a KO for 17 years, walks through '
                              'a construction job where the COR ordered ductwork offset 6 feet north. '
                              'Three weeks later, the contractor filed an REA of about $38k [pktnZU4AWIE @ '
                              '00:04:13]. The COR had no warrant and could not alter the scope of work. '
                              'The 30-day notice under the changes clause was blown, and a late claim at '
                              'that point is "scraping the pan." Williams adds that costs still have to be '
                              'allowable, allocable and reasonable, and that the COR could end up paying '
                              '[pktnZU4AWIE @ 00:06:37]. Tim Sullivan hits the same wall from the lawyer '
                              'side: a COR has no contracting authority, so loop scope questions back to '
                              'the CO, in writing [Gisvrg813kY @ 01:12:28]. GovSuccess closes the escape '
                              'hatch contractors bank on. Ratification is a separate process with '
                              'conditions, and it is not a dependable business plan for work started '
                              'without proper authorization. Job titles, relationships and urgency do not '
                              'establish authority [x7xmTiXnwQ4 @ 00:00:50]. Sky and Michelle note that '
                              'constructive changes often happen orally in meetings, which is exactly '
                              'where unwritten direction gets lost.',
                              'The money leaks come from pricing assumptions, not just authority. '
                              'FedAccess reports a firm that lost money on Service Contract Act paid '
                              'vacation. The channel also warns that the government can terminate for '
                              'convenience and has done so shortly after award [T_cRpZF2IUo @ 00:05:54]. '
                              'Tim Sullivan, who says there is no three-offeror rule, describes a client '
                              'rated in the \'50s that spent "150 grand" chasing an award; the case '
                              'settled. Agencies can also award on initial proposals, so holding back for '
                              "best-and-finals is a gamble [Gisvrg813kY @ 00:30:24]. Sullivan's other "
                              'losses are procedural. A bid that took exception to the default clause was '
                              'rejected as nonresponsive. Late is late, unless an electronic submission '
                              "sent before 5:00 the prior day was delayed by the government's fault. "
                              'GovSuccess flags a hidden cost in schedules: a sensor program had a June '
                              'test slot with no priced retest, and money spent is not the same thing as '
                              'completed technical work [z7tDxORX_pQ @ 00:02:18]. On supply deals, the '
                              'same channel warns that the lowest unit price may not produce the lowest '
                              'supported delivery cost. Compare FOB origin and destination quotes on '
                              'freight, packaging, appointments and unloading [QvsXldnQyAg @ 00:02:49].',
                              'The quietest failures are missed clocks and dirty records. Sky and Michelle '
                              'lay out the deadlines that sink contractors: settlement proposals within 1 '
                              'year of a termination for convenience, and inventory schedules within 120 '
                              'days. A default can be appealed within 90 days to the board or within a '
                              'year to the Court of Federal Claims, and default records damage you in SAM '
                              '[h1yszOmFw3w @ 00:27:49]. Claims over $100,000 must be certified, and the '
                              'claim window runs 6 years. REA preparation costs are recoverable, but REAs '
                              'earn no CDA interest [h1yszOmFw3w @ 01:03:30]. GovSuccess warns operators '
                              'not to import protest deadlines into a claim, and not to confuse the '
                              'submission period with the appeal period. On registration, Federal '
                              'Processing Registry says to update your CAGE code within 30 days of an '
                              'address, ownership or structure change. DLA review takes 3 to 7 business '
                              'days, and past 10 days you call the DLA Customer Interaction Center. '
                              '"Entity not found" means you need to update IRS data [ifMU9O8Ydmg @ '
                              '00:01:23]. David Gallagher adds a drafting trap: if the 52.244-2 blank is '
                              'left empty, the government cannot fill it in 6 months later, because "blank '
                              'means blank" [UV6zJLRHfHw @ 00:44:39]. Unmarked data submissions, per Sky '
                              'and Michelle, put your rights at risk.'],
               'table': {'caption': 'Firsthand Traps and the Economics Behind Them',
                         'headers': ['Trap', 'What Went Wrong', 'Economics Check', 'Expert Source'],
                         'rows': [["Acting on a COR's verbal direction on site",
                                   'COR without a warrant ordered ductwork offset 6 feet north',
                                   'Contractor filed a roughly $38k REA three weeks later, past the notice '
                                   'window',
                                   'Contract Warrior ([pktnZU4AWIE @ 00:04:13])'],
                                  ['Banking on ratification after unauthorized extra work',
                                   'Ratification is a separate process with its own conditions attached',
                                   'Not a dependable business plan for work started without proper '
                                   'authorization',
                                   'Win Government Contracts with GovSuccess ([x7xmTiXnwQ4 @ 00:00:50])'],
                                  ['Mispricing Service Contract Act benefit obligations',
                                   'A firm missed SCA paid vacation costs in its pricing',
                                   'The firm lost money, since wage determinations drive the price',
                                   'FedAccess ([T_cRpZF2IUo @ 00:06:57])'],
                                  ['Chasing an award from deep in the competitive range',
                                   'Client rated in the fifties fought on despite no three-offeror rule',
                                   'Spent 150 grand chasing the award before the case settled',
                                   'Public Contracting Institute (PCI) ([Gisvrg813kY @ 00:29:18])'],
                                  ['Unpriced retest buried in a tight test schedule',
                                   'Sensor program booked a June test slot with no priced retest',
                                   'Money spent is not the same thing as completed technical work',
                                   'Win Government Contracts with GovSuccess ([z7tDxORX_pQ @ 00:02:18])'],
                                  ['Missing the limitation of cost or funds notice',
                                   'Contractor must notify within 60 days of reaching 75 percent',
                                   'Under the clause, the contractor may stop work at the ceiling',
                                   'How To Sell To & Win Federal Government Contracts ([h1yszOmFw3w @ '
                                   '00:55:17])'],
                                  ['Stale CAGE code and entity registration records',
                                   'Address, ownership or structure change not updated within 30 days',
                                   'Ten minutes of updating can safeguard millions, per the walkthrough',
                                   'Federal Processing Registry ([ifMU9O8Ydmg @ 00:00:33])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Authority, Notice, Pricing and File Discipline Gate',
                           'body': 'Before any extra work starts, before any bid goes out, and before any '
                                   'dispute gets a label, clear these four gates drawn from losses the '
                                   'practitioners saw firsthand.',
                           'items': ['No scope change moves until the KO confirms it; a COR has no warrant '
                                     'and cannot alter the scope of work [Contract Warrior — pktnZU4AWIE @ '
                                     '00:06:55].',
                                     'Notify the Contracting Officer of a change typically within 30 days, '
                                     'but read your clause for the exact window [How To Sell To & Win '
                                     'Federal Government Contracts — h1yszOmFw3w @ 00:14:08].',
                                     'Price every SCA paid vacation and wage determination line before '
                                     'submission, because a firm lost money missing it [FedAccess — '
                                     'T_cRpZF2IUo @ 00:06:57].',
                                     'Keep protest and claim files separate, and never import protest '
                                     'deadlines into a claim or confuse submission and appeal periods [Win '
                                     'Government Contracts with GovSuccess — -smvR-8_v1M @ 00:01:14].']}}],
 'pull_quote': '"Before anyone says yes, your first question should be about authority, not enthusiasm." — '
               'Win Government Contracts with GovSuccess (x7xmTiXnwQ4 @ 00:00:00).',
 'diagram_id': 'diag-02',
 'action_checklist': ['Build a contact and authority sheet naming the contracting officer, the designated '
                      'technical representative, your authorized company signer and your internal '
                      'escalation owner, and keep the award, modifications and delegations accessible [Win '
                      'Government Contracts with GovSuccess — x7xmTiXnwQ4 @ 00:01:24].',
                      'Ctrl-F "52.2" in every solicitation to pull every clause, then trace each one back '
                      'to the section that prescribes it [Public Contracting Institute (PCI) — UV6zJLRHfHw '
                      '@ 00:29:28].',
                      'Google each clause together with its date so you read the exact version in your '
                      'contract rather than a generic FAR search [FedAccess — T_cRpZF2IUo @ 00:03:04].',
                      'Have pricing, staffing, insurance, references and an operational story ready, '
                      'because the response window may be days, not months [GovCon Empire with Derrick '
                      'Green “Theo” — k1EsNHPfqXY @ 00:09:13].',
                      'Ask for a debriefing even when you win, and do not wait until the last minute to '
                      'submit proposals [Public Contracting Institute (PCI) — Gisvrg813kY @ 00:33:18].',
                      'Build a delivery worksheet comparing freight, packaging, appointments and unloading '
                      'on total delivered cost, with an owner and resolution date for each open item [Win '
                      'Government Contracts with GovSuccess — QvsXldnQyAg @ 00:03:58].'],
 'statutory_citations': [{'title': "Contract Warrior — Don't Work for Free: Unauthorized Commitments in "
                                   'Federal Construction [00:04:13]',
                          'url': 'https://www.youtube.com/watch?v=pktnZU4AWIE&t=253s',
                          'relevance': 'Primary practitioner testimony on a COR-directed ductwork change '
                                       'that produced a roughly $38k REA without warranted authority.'},
                         {'title': 'Public Contracting Institute (PCI) — GovCon 101   Federal Acquisition '
                                   'Regulation FAR [01:12:28]',
                          'url': 'https://www.youtube.com/watch?v=Gisvrg813kY&t=4348s',
                          'relevance': 'Primary practitioner testimony on CORs having no contracting '
                                       'authority and routing scope questions to the CO in writing.'},
                         {'title': 'How To Sell To & Win Federal Government Contracts — 2024 FAR Part 52 - '
                                   'Solicitation Provisions And Contract Clauses [00:10:56]',
                          'url': 'https://www.youtube.com/watch?v=h1yszOmFw3w&t=656s',
                          'relevance': 'Primary practitioner testimony on unilateral, bilateral and '
                                       'constructive changes, terminations, claims certification and '
                                       'notice windows.'},
                         {'title': 'Public Contracting Institute (PCI) — GovCon 101 - A Guide to '
                                   'Navigating FAR Part 52 [00:38:30]',
                          'url': 'https://www.youtube.com/watch?v=UV6zJLRHfHw&t=2310s',
                          'relevance': 'Primary practitioner testimony on undated clauses, alternates, '
                                       'fill-ins, flow-downs and the Christian doctrine.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'Gisvrg813kY',
                       'title': 'GovCon 101   Federal Acquisition Regulation FAR',
                       'channel': 'Public Contracting Institute (PCI)',
                       'author': 'Public Contracting Institute (PCI)',
                       'text': "That's how complicated this is, but the thing to remember is that CORs "
                               'have no contracting authority.',
                       'tip': "That's how complicated this is, but the thing to remember is that CORs have "
                              'no contracting authority.',
                       'timestamp': 4367,
                       'timestamp_seconds': 4367,
                       'timestamp_label': '[01:12:47]',
                       'url': 'https://www.youtube.com/watch?v=Gisvrg813kY&t=4367s',
                       'markdown': '[01:12:47](https://www.youtube.com/watch?v=Gisvrg813kY&t=4367s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Gisvrg813kY',
                       'title': 'GovCon 101   Federal Acquisition Regulation FAR',
                       'channel': 'Public Contracting Institute (PCI)',
                       'author': 'Public Contracting Institute (PCI)',
                       'text': 'And so do not wait till the last minute to submit these proposals.',
                       'tip': 'And so do not wait till the last minute to submit these proposals.',
                       'timestamp': 1638,
                       'timestamp_seconds': 1638,
                       'timestamp_label': '[00:27:18]',
                       'url': 'https://www.youtube.com/watch?v=Gisvrg813kY&t=1638s',
                       'markdown': '[00:27:18](https://www.youtube.com/watch?v=Gisvrg813kY&t=1638s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'x7xmTiXnwQ4',
                       'title': 'FAR PART 1 (Simplified) | Who Can Authorize the Work?',
                       'channel': 'Win Government Contracts with GovSuccess',
                       'author': 'Win Government Contracts with GovSuccess',
                       'text': 'Before anyone says yes, your first question should be about authority, not '
                               'enthusiasm.',
                       'tip': 'Before anyone says yes, your first question should be about authority, not '
                              'enthusiasm.',
                       'timestamp': 0,
                       'timestamp_seconds': 0,
                       'timestamp_label': '[00:00:00]',
                       'url': 'https://www.youtube.com/watch?v=x7xmTiXnwQ4&t=0s',
                       'markdown': '[00:00:00](https://www.youtube.com/watch?v=x7xmTiXnwQ4&t=0s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'UV6zJLRHfHw',
                       'title': 'GovCon 101 - A Guide to Navigating FAR Part 52',
                       'channel': 'Public Contracting Institute (PCI)',
                       'author': 'Public Contracting Institute (PCI)',
                       'text': 'Importantly, I want us all to know there is no such thing as '
                               'self-deleting.',
                       'tip': 'Importantly, I want us all to know there is no such thing as self-deleting.',
                       'timestamp': 3590,
                       'timestamp_seconds': 3590,
                       'timestamp_label': '[00:59:50]',
                       'url': 'https://www.youtube.com/watch?v=UV6zJLRHfHw&t=3590s',
                       'markdown': '[00:59:50](https://www.youtube.com/watch?v=UV6zJLRHfHw&t=3590s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'UV6zJLRHfHw',
                       'title': 'GovCon 101 - A Guide to Navigating FAR Part 52',
                       'channel': 'Public Contracting Institute (PCI)',
                       'author': 'Public Contracting Institute (PCI)',
                       'text': 'Blank means blank.',
                       'tip': 'Blank means blank.',
                       'timestamp': 2713,
                       'timestamp_seconds': 2713,
                       'timestamp_label': '[00:45:13]',
                       'url': 'https://www.youtube.com/watch?v=UV6zJLRHfHw&t=2713s',
                       'markdown': '[00:45:13](https://www.youtube.com/watch?v=UV6zJLRHfHw&t=2713s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'MTy_zJd0RsY',
                       'title': 'The Federal Acquisition Regulation (FAR) Explained in 5 Minutes',
                       'channel': 'ASI Education',
                       'author': 'ASI Education',
                       'text': "Under 1.102(d), if it's not prohibited it's okay.",
                       'tip': "Under 1.102(d), if it's not prohibited it's okay.",
                       'timestamp': 125,
                       'timestamp_seconds': 125,
                       'timestamp_label': '[00:02:05]',
                       'url': 'https://www.youtube.com/watch?v=MTy_zJd0RsY&t=125s',
                       'markdown': '[00:02:05](https://www.youtube.com/watch?v=MTy_zJd0RsY&t=125s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'T_cRpZF2IUo',
                       'title': 'TLDR  Which Parts of the Federal Acquisition Regulation Matter?',
                       'channel': 'FedAccess',
                       'author': 'FedAccess',
                       'text': "The FAR is 2,000 pages, so don't read it; read your clauses.",
                       'tip': "The FAR is 2,000 pages, so don't read it; read your clauses.",
                       'timestamp': 0,
                       'timestamp_seconds': 0,
                       'timestamp_label': '[00:00:00]',
                       'url': 'https://www.youtube.com/watch?v=T_cRpZF2IUo&t=0s',
                       'markdown': '[00:00:00](https://www.youtube.com/watch?v=T_cRpZF2IUo&t=0s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'MM4DJrI2Od0',
                       'title': 'The New Rules of Federal Buying: How the FAR Overhaul Is Changing '
                                'Everything',
                       'channel': 'Fed Gov Today',
                       'author': 'Fed Gov Today',
                       'text': "So, as opposed to paying for level of effort, what we're seeing is paying "
                               'for outcomes.',
                       'tip': "So, as opposed to paying for level of effort, what we're seeing is paying "
                              'for outcomes.',
                       'timestamp': 136,
                       'timestamp_seconds': 136,
                       'timestamp_label': '[00:02:16]',
                       'url': 'https://www.youtube.com/watch?v=MM4DJrI2Od0&t=136s',
                       'markdown': '[00:02:16](https://www.youtube.com/watch?v=MM4DJrI2Od0&t=136s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'k1EsNHPfqXY',
                       'title': 'Federal Contracts Moving Faster in 2026 - FAR Overhaul.',
                       'channel': 'GovCon Empire with Derrick Green “Theo”',
                       'author': 'GovCon Empire with Derrick Green “Theo”',
                       'text': 'Thankfully, finally, faster does not mean reckless, it just means smarter.',
                       'tip': 'Thankfully, finally, faster does not mean reckless, it just means smarter.',
                       'timestamp': 799,
                       'timestamp_seconds': 799,
                       'timestamp_label': '[00:13:19]',
                       'url': 'https://www.youtube.com/watch?v=k1EsNHPfqXY&t=799s',
                       'markdown': '[00:13:19](https://www.youtube.com/watch?v=k1EsNHPfqXY&t=799s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'z7tDxORX_pQ',
                       'title': 'FAR Part 34 (Simplified) | Connect Scope, Schedule, and Cost Before You '
                                'Commit',
                       'channel': 'Win Government Contracts with GovSuccess',
                       'author': 'Win Government Contracts with GovSuccess',
                       'text': 'In practical terms, money spent is not the same thing as completed '
                               'technical work, and an attractive schedule is not evidence that the '
                               'necessary resources will be available.',
                       'tip': 'In practical terms, money spent is not the same thing as completed '
                              'technical work, and an attractive schedule is not evidence that the '
                              'necessary resources will be available.',
                       'timestamp': 102,
                       'timestamp_seconds': 102,
                       'timestamp_label': '[00:01:42]',
                       'url': 'https://www.youtube.com/watch?v=z7tDxORX_pQ&t=102s',
                       'markdown': '[00:01:42](https://www.youtube.com/watch?v=z7tDxORX_pQ&t=102s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'LgX6N2c9-S4',
                       'title': 'FAR PART 4 (Simplified) | Treat Registration and Contract Data as '
                                'Operating Controls',
                       'channel': 'Win Government Contracts with GovSuccess',
                       'author': 'Win Government Contracts with GovSuccess',
                       'text': 'SAM registration has exceptions and does not prove readiness.',
                       'tip': 'SAM registration has exceptions and does not prove readiness.',
                       'timestamp': 15,
                       'timestamp_seconds': 15,
                       'timestamp_label': '[00:00:15]',
                       'url': 'https://www.youtube.com/watch?v=LgX6N2c9-S4&t=15s',
                       'markdown': '[00:00:15](https://www.youtube.com/watch?v=LgX6N2c9-S4&t=15s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'pktnZU4AWIE',
                       'title': "Don't Work for Free: Unauthorized Commitments in Federal Construction",
                       'channel': 'Contract Warrior',
                       'author': 'Contract Warrior',
                       'text': 'They cannot alter the scope of work.',
                       'tip': 'They cannot alter the scope of work.',
                       'timestamp': 271,
                       'timestamp_seconds': 271,
                       'timestamp_label': '[00:04:31]',
                       'url': 'https://www.youtube.com/watch?v=pktnZU4AWIE&t=271s',
                       'markdown': '[00:04:31](https://www.youtube.com/watch?v=pktnZU4AWIE&t=271s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ifMU9O8Ydmg',
                       'title': 'How to Correct or Update Your CAGE Code in SAM.gov | Visual Walkthrough',
                       'channel': 'Federal Processing Registry',
                       'author': 'Federal Processing Registry',
                       'text': 'Ten minutes can safeguard millions.',
                       'tip': 'Ten minutes can safeguard millions.',
                       'timestamp': 167,
                       'timestamp_seconds': 167,
                       'timestamp_label': '[00:02:47]',
                       'url': 'https://www.youtube.com/watch?v=ifMU9O8Ydmg&t=167s',
                       'markdown': '[00:02:47](https://www.youtube.com/watch?v=ifMU9O8Ydmg&t=167s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'h1yszOmFw3w',
                       'title': '2024 FAR Part 52 - Solicitation Provisions And Contract Clauses',
                       'channel': 'How To Sell To & Win Federal Government Contracts',
                       'author': 'How To Sell To & Win Federal Government Contracts',
                       'text': 'claims that are over $100,000 must be certified and that claim starts the '
                               'disputes process.',
                       'tip': 'claims that are over $100,000 must be certified and that claim starts the '
                              'disputes process.',
                       'timestamp': 3714,
                       'timestamp_seconds': 3714,
                       'timestamp_label': '[01:01:54]',
                       'url': 'https://www.youtube.com/watch?v=h1yszOmFw3w&t=3714s',
                       'markdown': '[01:01:54](https://www.youtube.com/watch?v=h1yszOmFw3w&t=3714s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'mZqOwnA0HbE',
                       'title': 'Title Transfer: FOB Shipping Point and FOB Destination - FAR Exam Prep',
                       'channel': 'ExamPrepAI CPA Review',
                       'author': 'ExamPrepAI CPA Review',
                       'text': 'Well, this means the title transfers of the goods at the shipping point.',
                       'tip': 'Well, this means the title transfers of the goods at the shipping point.',
                       'timestamp': 0,
                       'timestamp_seconds': 0,
                       'timestamp_label': '[00:00:00]',
                       'url': 'https://www.youtube.com/watch?v=mZqOwnA0HbE&t=0s',
                       'markdown': '[00:00:00](https://www.youtube.com/watch?v=mZqOwnA0HbE&t=0s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'QvsXldnQyAg',
                       'title': 'FAR Part 47 (Simplified) | Align Delivery, Freight, and Risk Before '
                                'Shipment',
                       'channel': 'Win Government Contracts with GovSuccess',
                       'author': 'Win Government Contracts with GovSuccess',
                       'text': 'The lowest unit price may not produce the lowest supported delivery cost.',
                       'tip': 'The lowest unit price may not produce the lowest supported delivery cost.',
                       'timestamp': 169,
                       'timestamp_seconds': 169,
                       'timestamp_label': '[00:02:49]',
                       'url': 'https://www.youtube.com/watch?v=QvsXldnQyAg&t=169s',
                       'markdown': '[00:02:49](https://www.youtube.com/watch?v=QvsXldnQyAg&t=169s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'TFl20T0yyig',
                       'title': 'Neybor FAR Part12',
                       'channel': 'Neybor Consulting',
                       'author': 'Neybor Consulting',
                       'text': 'Speed is the entire point of part 12.',
                       'tip': 'Speed is the entire point of part 12.',
                       'timestamp': 950,
                       'timestamp_seconds': 950,
                       'timestamp_label': '[00:15:50]',
                       'url': 'https://www.youtube.com/watch?v=TFl20T0yyig&t=950s',
                       'markdown': '[00:15:50](https://www.youtube.com/watch?v=TFl20T0yyig&t=950s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '-smvR-8_v1M',
                       'title': 'FAR Part 33 (Simplified) | Separate a Protest From a Contract Claim',
                       'channel': 'Win Government Contracts with GovSuccess',
                       'author': 'Win Government Contracts with GovSuccess',
                       'text': 'The label on an email does not settle which framework applies.',
                       'tip': 'The label on an email does not settle which framework applies.',
                       'timestamp': 37,
                       'timestamp_seconds': 37,
                       'timestamp_label': '[00:00:37]',
                       'url': 'https://www.youtube.com/watch?v=-smvR-8_v1M&t=37s',
                       'markdown': '[00:00:37](https://www.youtube.com/watch?v=-smvR-8_v1M&t=37s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'}]}
