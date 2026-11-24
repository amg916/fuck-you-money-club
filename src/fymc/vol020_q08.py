from __future__ import annotations

CHAPTER_8 = {'id': 'Q8',
 'chapter_id': 'Q8',
 'chapter_number': 8,
 'question_number': 8,
 'slug': 'teaming-subcontracting-prime-sub-relationships',
 'question_prompt': 'How do I find primes and subcontractors, and how should teaming agreements be '
                    "structured so I don't get burned?",
 'kicker': 'Q8 / THE BIG MONEY PLAYBOOKS',
 'title': 'Teaming, Subcontracting and Prime–Sub Relationships',
 'subtitle': 'Prime vs. sub paths for beginners, finding primes (SAIC) and handling ghosting subs, teaming '
             "agreements vs. subcontracts vs. JVs, negotiating from the sub's side, the financial "
             'trade-offs between prime and sub, and VA OSDBU and PCI teaming guidance',
 'layout_template': 'legal_compliance_callout',
 'reading_time_minutes': 15,
 'executive_summary': 'Sixteen GovCon practitioners converge on one rule: the prime is whoever the '
                      'contracting officer signs with, it carries full liability, and subs only get paid '
                      'what is locked in writing. Operators report teaming lifts win probability when it '
                      'fills a named gap, while handshake deals end in ghosting, six-month removals and a '
                      '$20,000 loss. Street mechanics include pulling price history from FPDS, mining '
                      'SAM.gov contract awards (2,000 help-desk hits filtered to 87 woman-owned targets), '
                      'setting 51-52% prime workshare, enforcing the 50% services limitation on '
                      'subcontracting, and funding roughly 14% of contract value upfront as prime versus '
                      '20% as sub. Practitioners split on whether rushing to team helps or damages small '
                      'firms, how much exclusivity matters, and whether written teaming agreements are '
                      'actually enforceable in court.',
 'key_metrics': [{'label': 'Proposal Cost Burn Without Teaming',
                  'metric': 'Proposal Cost Burn Without Teaming',
                  'value': '$30,000 per proposal; $300,000 across 10 proposals with nothing won',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Jackie Lopez's ROI case for teaming to share proposal cost and raise P-win "
                             'instead of bidding solo',
                  'source': 'VA OSDBU (On Demand) ([iLuva0z2cMA @ 00:14:31])'},
                 {'label': 'Prime Upfront Capital on a $2M/yr Set-Aside Task Order',
                  'metric': 'Prime Upfront Capital on a $2M/yr Set-Aside Task Order',
                  'value': '$275,000-$300,000 (about 14% of contract value) for the prime vs. about '
                           '$80,000 (about 20%) for a $400k sub slice',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Prime doing 55% runs about $80k/month, waits 70-80 days for payment, and '
                             'holds a roughly $175k payroll reserve',
                  'source': 'ELINT Capital ([EpUc9OVjb4g @ 00:13:32])'},
                 {'label': 'Limitation on Subcontracting Prime Share',
                  'metric': 'Limitation on Subcontracting Prime Share',
                  'value': 'Services 50%; general construction 15% (85% to subs); specialty trade 25% (75% '
                           'to subs)',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Shane's breakdown, measured per base and option period with no averaging",
                  'source': 'VA OSDBU (On Demand) ([iLuva0z2cMA @ 01:09:29])'},
                 {'label': 'SAM.gov Contract Award Target List Yield',
                  'metric': 'SAM.gov Contract Award Target List Yield',
                  'value': "About 2,000 'help desk' results -> 149 woman-owned -> 87 unique companies "
                           'after removing 62 duplicates',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Neil McDonnell's live SAM.gov Contract Awards search, deduplicated by "
                             'awardee UEI',
                  'source': 'Neil McDonnell ([zqg5q_pZvdc @ 00:24:05])'}],
 'sections': [{'heading': 'Section 1: The Practitioner Consensus',
               'paragraphs': ['Every practitioner starts from the same hard line: the prime is the company '
                              'the contracting officer signed with, and that is where all liability sits. '
                              'ASI Education explains that the prime holds privity of contract, the '
                              'government has no privity with subs, and FAR Part 44 bars the agency from '
                              'dictating which subs a prime uses; even a multi-company team still has one '
                              "accountable 'belly button' [jYYGaPkanFU @ 00:01:41]. Shane, the legal voice "
                              'on the VA OSDBU panel, puts it bluntly: the prime is 100% responsible to '
                              'the government, including when a sub goes bankrupt or trips Service '
                              'Contract Act problems [iLuva0z2cMA @ 00:57:00]. Federal Contracts Lab '
                              'frames prime and sub as responsibility levels rather than status levels. '
                              'The prime signs, manages, invoices and eats the performance risk, while '
                              'subs plug in as HVAC, janitorial, pest control, help desk or cyber '
                              'specialists [3eoJWm0WffU @ 00:03:19]. Neil McDonnell attacks the assumption '
                              "that 'prime' means 'large': a small service-disabled veteran-owned business "
                              'won a $175M prime with Booz Allen and Boeing working underneath it, and an '
                              'aircraft carrier runs on roughly a thousand subs [zqg5q_pZvdc @ 00:07:38]. '
                              'The operating takeaway is simple: whoever signs owns the risk, and everyone '
                              'else at the table is negotiating for a protected slice.',
                              'The second point of near-total agreement: if it is not written, it does not '
                              'exist. Stephanie of GovCon TechLab opens with the classic burn, a handshake '
                              'teaming deal where the sub does 80% of the work for 20% of the revenue or '
                              'gets ghosted after the partner wins, and dismisses a one-page letter of '
                              "intent as a 'hope document,' because after award the prime holds all the "
                              'leverage [JYbjE63rG-Y @ 00:04:26]. Dr. Mel lists exactly what happens '
                              'without a real teaming agreement: lost control of IP, exclusion from the '
                              'final deal, ownership disputes and proposal hours that never pay back, then '
                              "tells operators to stop running on 'handshakes and hope' [HKtAZzSL_GQ @ "
                              '00:01:23]. The VA OSDBU panel warns that any prime offering 49% of a '
                              'project but refusing to put it in writing deserves extreme caution '
                              '[iLuva0z2cMA @ 00:26:33]. Centurion Research Solutions sharpens the '
                              'drafting standard: the work percentage should name a specific percentage or '
                              "number of staff, because agreements that promise 'best efforts' or 'goals' "
                              'rarely pan out [L-BpgTTiESM @ 00:10:18]. Across all four practitioners, the '
                              'rule is identical: lock precise numbers on paper before the proposal ships, '
                              'never vague percentages, verbal assurances or friendly intentions.',
                              'Practitioners also agree that subcontracting is a legitimate entry and '
                              'growth lane, not a consolation prize. Humam Finding Sam points out that the '
                              'FAR mandates primes subcontract set percentages to small businesses, so '
                              'prime compliance goals create built-in demand, and a firm with zero '
                              'government past performance can get its foot in the door this way, adding '
                              'that primes need subs as much as subs need primes [T_HZxPdh7B8 @ 00:00:25]. '
                              'Federal Contracts Lab states flatly that subcontracting is not a downgrade, '
                              'pitching a hybrid of subcontracting plus selective small primes in the same '
                              'service and buyer type, and telling subs to document every engagement for '
                              'references [3eoJWm0WffU @ 00:08:57]. Akiesha Foster, who won as key '
                              'personnel in a tier-two sub slot, says teammates are typically considered '
                              'six to twelve months before the request for proposal is released, so '
                              'operators should stop waiting until the last minute and start building '
                              "relationships now [qnkHiXcQCHM @ 00:05:18]. ELINT Capital's panel adds the "
                              'money logic: subcontracting beats getting nothing, but the single most '
                              'important move is picking the prime carefully and keeping a good '
                              'relationship with it [EpUc9OVjb4g @ 00:18:07]. The shared sequence across '
                              'all four is sub first, collect documented proof, then prime selectively '
                              'when ready.'],
               'table': {'caption': 'Where the practitioners agree on prime-sub fundamentals',
                         'headers': ['Consensus Point',
                                     'What Practitioners Say',
                                     'Operator Implication',
                                     'Expert Source'],
                         'rows': [['Prime owns the entire government relationship',
                                   'Prime holds privity of contract; the government has no privity with '
                                   'subs',
                                   'Any performance problem lands on the prime, so subs gain access only '
                                   'through the prime',
                                   'ASI Education ([jYYGaPkanFU @ 00:01:41])'],
                                  ['Prime carries 100% liability to the government',
                                   'Prime answers to the government even for sub bankruptcy and Service '
                                   'Contract Act issues',
                                   'Primes vet subs hard, so subs should expect financial and reference '
                                   'checks up front',
                                   'VA OSDBU (On Demand) ([iLuva0z2cMA @ 00:57:00])'],
                                  ['Written workshare beats any handshake promise',
                                   'Handshake deals end with 80% of the work for 20% of revenue, or '
                                   'ghosting',
                                   'Lock specific percentages in writing before proposal submission, not '
                                   'after the award',
                                   'GovCon TechLab ([JYbjE63rG-Y @ 00:00:00])'],
                                  ['Team to win, not to stay comfortable',
                                   'Avoid teaming just because it is somebody you already know; team to '
                                   'win',
                                   'Pick partners on win contribution rather than on existing friendship '
                                   'or familiarity',
                                   'Centurion Research Solutions ([L-BpgTTiESM @ 00:08:57])'],
                                  ['Subcontracting is a real revenue and growth lane',
                                   'Builds revenue plus past performance, including experience with the '
                                   'specific target agency',
                                   'Use sub work to qualify for larger vehicles and set-asides you cannot '
                                   'prime yet',
                                   'Neil McDonnell ([zqg5q_pZvdc @ 00:12:51])'],
                                  ['Relationships start months before the RFP drops',
                                   'Teammates are typically considered six to twelve months before the RFP '
                                   'is released',
                                   'Start building prime relationships now instead of chasing posted '
                                   'solicitations at the deadline',
                                   'Akiesha Foster ([qnkHiXcQCHM @ 00:05:18])'],
                                  ["Sub price quotes anchor the prime's bid",
                                   'Core objective with subs is getting a price quote, even a best guess '
                                   'estimate',
                                   'Without sub pricing in hand, a prime cannot build a credible bid '
                                   'number',
                                   'Kizzy Parks ([F6Hwh89ornQ @ 00:01:32])']]}},
              {'heading': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ["The prospecting mechanics are concrete. Neil McDonnell's SAM.gov workflow: "
                              'log in, go to Search, then Contracting, then Contract Awards, and search '
                              "the exact phrase 'help desk' for about 2,000 results; filter to woman-owned "
                              'small businesses, certified or not, to get 149; download and strip '
                              'duplicates by awardee UEI, which removed 62 and left 87 companies to '
                              'approach [zqg5q_pZvdc @ 00:20:35]. He favors firms with $20 million and '
                              'above in awards and says the point is future relationships, not asking for '
                              'a cut of existing contracts. Akiesha Foster Googles the top 100 federal '
                              'contractors, builds a spreadsheet, uses usaspending.gov to pick a target '
                              'like SAIC, then maps its small business program, specialist contact, '
                              'supplier portal and teaming process [qnkHiXcQCHM @ 00:00:45]. Humam Finding '
                              "Sam runs the channel's own SAM Search tool with subcontracting-source "
                              "filters on names like Lockheed Martin or Deloitte, using a 'high' "
                              'confidence filter to surface FAR-required subcontracts, plus plain-English '
                              'queries and weekly saved-search alerts [T_HZxPdh7B8 @ 00:03:53]. Kizzy '
                              'Parks works the other direction as prime: call vendors the moment an '
                              'opportunity posts, before they are exhausted by the 107th caller, and find '
                              'who won similar work in the same location, then ask who they subbed to, '
                              'such as a gravel supplier [F6Hwh89ornQ @ 00:08:58].',
                              'Workshare math is where deals live or die. On the VA OSDBU panel, Shane '
                              'lays out the limitation on subcontracting: services 50%, general '
                              'construction 15% with 85% to subs, specialty trade 25% with 75% to subs, '
                              'measured separately for each base and option period with no averaging; on a '
                              '$1M woman-owned set-aside with $100k of airfare excluded, the prime must '
                              "perform $450k of the remaining $900k, and a similarly situated sub's $200k "
                              "stacks with the prime's $300k to reach $500k [iLuva0z2cMA @ 01:10:26]. "
                              'Jackie Lopez on the same panel sets a 51-52% floor whenever socioeconomics '
                              'are involved. Theodore Watson says the prime generally performs at least '
                              '51% of contract cost, less depending on the industry code, and that 31% of '
                              'companies using teaming agreements or JVs are not familiar with the '
                              'landmines competitors use in bid protests [NP_UB6qiZhw @ 00:00:31]. '
                              'Stephanie at GovCon TechLab turns this into a filter: a prime promising 60% '
                              'of the work on a services set-aside is offering a deal that is illegal on '
                              'its face [JYbjE63rG-Y @ 00:12:50]. The Centurion Research Solutions session '
                              'confirms small-business primes usually retain 51% of revenue [L-BpgTTiESM @ '
                              '00:04:04]. The operator rule: run the dollar math per period before signing '
                              'anything, because the limitation can cost the award itself.',
                              "The money mechanics are just as specific. ELINT Capital's worked example: a "
                              '$2M-per-year services task order on a set-aside, with the prime doing 55%, '
                              'burns about $80k a month and waits 70-80 days for payment; with a roughly '
                              '$175k payroll reserve, total upfront hits $275-300k, about 14% of contract '
                              'value, while a sub holding a $400k slice needs about $80k upfront, about '
                              '20% [EpUc9OVjb4g @ 00:13:32]. The same panel says subs now push '
                              'pay-when-paid clauses capped at about 60 days, because an improper invoice '
                              'restarts the 30-day clock, and should fund 2-2.5 months of payroll. On '
                              'pricing, Kizzy Parks tells primes to ask the agency what it paid before and '
                              'to check fpds.gov, warning that taking a sub quote and simply tacking a '
                              'profit percentage on top is not going to happen [F6Hwh89ornQ @ 00:04:37]. '
                              'Jackie Lopez builds price to win from FPDS or a Googled contract number, '
                              'adjusted for changes, noting most bidders come in 5-10% under, and insists '
                              'price to win and price to execute must be one and the same [iLuva0z2cMA @ '
                              '01:26:27]. ASI Education describes the squeeze in sole-source negotiations: '
                              'either the prime tells the contracting officer the sub cannot go any '
                              'cheaper, or everyone cuts about 10% [jYYGaPkanFU @ 00:07:17].'],
               'table': {'caption': 'Street mechanics, tools and hard numbers for prime-sub deals',
                         'headers': ['Mechanic',
                                     'Exact Number or Tool',
                                     'How Operators Use It',
                                     'Expert Source'],
                         'rows': [['SAM.gov contract award mining for teaming targets',
                                   "'Help desk' search: about 2,000 results, 149 woman-owned, 87 unique "
                                   'UEIs',
                                   'Build a target list of firms with $20M-plus in awards for future '
                                   'teaming',
                                   'Neil McDonnell ([zqg5q_pZvdc @ 00:24:05])'],
                                  ['Limitation on subcontracting by work type',
                                   'Prime share: services 50%, general construction 15%, specialty trade '
                                   '25%',
                                   'Check every base and option period separately because there is no '
                                   'averaging',
                                   'VA OSDBU (On Demand) ([iLuva0z2cMA @ 01:09:29])'],
                                  ['Prime upfront capital on a set-aside task order',
                                   '$275,000-$300,000, about 14% of a $2M annual contract value',
                                   'Line up the payroll reserve before priming, since payment takes 70-80 '
                                   'days',
                                   'ELINT Capital ([EpUc9OVjb4g @ 00:13:32])'],
                                  ['Price to win built from historical award data',
                                   'Most bidders come in 5-10% under the prior contract price',
                                   'Pull FPDS history or Google the contract number, then adjust for scope '
                                   'changes',
                                   'VA OSDBU (On Demand) ([iLuva0z2cMA @ 01:26:27])'],
                                  ['Workshare floor clause in the teaming agreement',
                                   "'No less than 30%' beats 'approximately' as the workshare language",
                                   'Write a hard minimum percentage instead of target or approximate '
                                   'wording',
                                   'GovCon TechLab ([JYbjE63rG-Y @ 00:14:55])'],
                                  ['Pricing-lock clause carried into the subcontract',
                                   'Pricing accepted before proposal submission is incorporated into the '
                                   'following subcontract',
                                   'Blocks post-award renegotiation, which Karen Long estimates happens '
                                   'about 50% of the time',
                                   'Streamline Government Contracts, LLC ([W-f5dCQEEkE @ 00:07:28])'],
                                  ['Termination and no-bid notice window for subs',
                                   "Written no-bid notice within about 2 business days of the prime's "
                                   'decision',
                                   'Bar termination of the teaming agreement while the proposal sits in '
                                   'source selection',
                                   'Streamline Government Contracts, LLC ([W-f5dCQEEkE @ 00:15:49])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Moves the operators actually run',
                           'body': 'Small clause choices and vetting habits that practitioners say decide '
                                   'whether a teaming slot turns into paid work.',
                           'items': ['Make exclusivity task-order-level, not IDIQ-level, and make sure '
                                     'exclusivity does not survive termination while confidentiality and '
                                     'employee non-solicitation do [Streamline Government Contracts, LLC — '
                                     'W-f5dCQEEkE @ 00:09:32].',
                                     'Get sub pricing in writing even by text or WhatsApp; one winner had '
                                     'to give a contract back because the sub contact had left the company '
                                     '[Kizzy Parks — F6Hwh89ornQ @ 00:07:00].',
                                     "Vet a partner's core values by checking the CEO's LinkedIn "
                                     'connections and calling trusted mutual contacts, then run FPDS EZ '
                                     'Search, USAspending, SBA Dynamic Small Business Search and SAM.gov '
                                     '[VA OSDBU (On Demand) — iLuva0z2cMA @ 00:24:25].',
                                     'Pull a D&B report on any small prime before signing; one prime on a '
                                     'team was declared financially unacceptable [Centurion Research '
                                     'Solutions — L-BpgTTiESM @ 00:10:56].']},
               'sop_steps': [{'step': 1,
                              'title': 'Build the target list',
                              'action': 'Mine SAM.gov Contract Awards for your exact service phrase, '
                                        'filter by socioeconomic status, and deduplicate by UEI.',
                              'detail': 'Search the exact phrase, filter to the set-aside category, '
                                        'download, remove duplicates by awardee UEI, and prioritize firms '
                                        'with $20 million and above in awards [Neil McDonnell — '
                                        'zqg5q_pZvdc @ 00:24:05].'},
                             {'step': 2,
                              'title': 'Name the gap and assess the partner',
                              'action': 'Answer the four Assess questions before any outreach or '
                                        'signature.',
                              'detail': 'Confirm what gap teaming fixes, reject duplicate capabilities '
                                        'like two WOSB cyber firms, check the workshare math, and verify '
                                        'the partner pays through references, factoring companies and '
                                        'protests [GovCon TechLab — JYbjE63rG-Y @ 00:11:24].'},
                             {'step': 3,
                              'title': 'Paper the deal before submission',
                              'action': 'Sign the NDA first, then the teaming agreement before the '
                                        'proposal goes in, using attorney-drafted templates.',
                              'detail': 'Sign an NDA before disclosing relationships and sign the teaming '
                                        'agreement before submission, with a 51-52% prime floor when '
                                        'socioeconomics are involved [VA OSDBU (On Demand) — iLuva0z2cMA @ '
                                        '00:43:38].'},
                             {'step': 4,
                              'title': 'Track the relationship post-award',
                              'action': 'Run a fixed cadence of check-ins and invoice reviews and put '
                                        'every rate change in writing.',
                              'detail': 'Hold weekly 15-minute check-ins, monthly invoice reviews and '
                                        'quarterly relationship reviews; on a FEMA option period, reduced '
                                        'rates were passed through to the sub in writing [GovCon TechLab — '
                                        'JYbjE63rG-Y @ 00:19:53].'}]},
              {'heading': 'Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['Kizzy Parks breaks hardest from the teaming chorus. She says SBA, SCORE and '
                              'similar outfits push the line that “government loves teams,” and she calls '
                              'rushing to team “one of the most damaging” practices; her rule is to define '
                              'the goal first, whether that is higher win odds, fatter margins, or a new '
                              'client type, and then ask why a stronger party needs you at all '
                              '[ol1KkwjDTqg @ 00:00:45]. Jackie Lopez reads the same market the opposite '
                              'way, crediting teaming principles with having “significantly increased our '
                              'Revenue” and pinning 50–60% of her growth on a reputation as a good teaming '
                              'partner [iLuva0z2cMA @ 00:14:52]. Stephanie of GovCon TechLab lands between '
                              "them with a one-line filter: “If you can't name the specific gap that "
                              "you're trying to fill, then you don't really need to team,” and two WOSB "
                              'cyber firms pairing up is a “hard pass” [JYbjE63rG-Y @ 00:12:00]. Mike Lore '
                              'adds the relationship trap, warning operators to “avoid teaming just '
                              "because it's somebody you already know” and to “team to win,” setting "
                              'selection criteria before picking anyone [L-BpgTTiESM @ 00:08:57]. The '
                              'practical split: Lopez teams early and often to lift P-win, while Parks '
                              'teams only when her chips are on the table.',
                              'The sequencing fight is just as sharp. Kizzy Parks teaches middleman '
                              'priming from day one: you win as prime, others deliver the service or '
                              'product, and she closes by saying you need no past performance and no '
                              'product to play [F6Hwh89ornQ @ 00:11:55]. Akiesha Foster runs the opposite '
                              'clock, holding Level 3 certification and 12+ years of experience yet '
                              'planning about 10 years as a tier-two sub before priming, because “start '
                              'off as a subcontractor and then that will position you better so you can '
                              'become a prime” [qnkHiXcQCHM @ 00:07:08]. Neil McDonnell rejects the ladder '
                              'framing altogether, arguing subcontracting is not just for small or new '
                              'firms and pushing three revenue streams in parallel: subbing under a small, '
                              'priming, and subbing under a large, with all three in play once traction '
                              'passes $3M [zqg5q_pZvdc @ 00:11:06]. Federal Contracts Lab treats prime and '
                              'sub as responsibility levels rather than status, insists “Subcontracting is '
                              'not a downgrade,” and prescribes a hybrid of subcontracting plus selective '
                              "small primes in the same service and buyer type, summed up as “It's about "
                              "sequence” [3eoJWm0WffU @ 00:14:25]. Foster's timing warning compounds the "
                              'choice: teammates are typically picked six to 12 months before the RFP, so '
                              "“don't wait to the last minute.”",
                              'Paperwork depth splits the field. Parks tells middleman primes no exclusive '
                              'agreement or NDA is needed with vendors, only “some type of written paper '
                              'trail of pricing,” even by text or WhatsApp [F6Hwh89ornQ @ 00:07:00]. '
                              'Stephanie demands the full seven-clause stack, including a mutual NDA, '
                              'proposal-cost terms, termination if not awarded, a workshare floor where '
                              '“no less than 30%” beats “approximately,” and mutual exclusivity per '
                              'opportunity only, never blanket [JYbjE63rG-Y @ 00:14:55]. David Gallagher '
                              'of Kutak Rock tempers both camps on enforceability: “The agreement to agree '
                              'interpretation of a teaming agreement is by far the most common,” the '
                              'enforceable EG&G v. Cube outcome “is rare,” and “Exclusivity is not '
                              'critical, but it helps” [NB57wtT4xfs @ 00:48:53]. Karen Long, negotiating '
                              "from the sub's seat, wants exclusivity at the task-order level rather than "
                              'the IDIQ level and no unilateral right for the prime to drop you, warning '
                              "that “if you're going to be exclusive you should understand what you are "
                              "giving up” [W-f5dCQEEkE @ 00:09:32]. Gallagher's own baseline is blunt: "
                              '“Never sign just a standard teaming agreement,” because no standard federal '
                              'or DOD form exists, so you start from a template and tailor it.'],
               'table': {'caption': 'Side-by-side playbooks where named practitioners split on teaming and '
                                    'subcontracting',
                         'headers': ['Fault Line', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Default workshare split for a small prime',
                                   'McDonnell calls a 51/49 split the normal arrangement for 20 years',
                                   'Lopez always goes more than 50/50 with socioeconomics, setting a '
                                   '51–52% minimum',
                                   'Neil McDonnell ([zqg5q_pZvdc @ 00:08:46]); VA OSDBU (On Demand) '
                                   '([iLuva0z2cMA @ 01:57:24])'],
                                  ['How much exclusivity to grant the prime',
                                   'Gallagher says exclusivity is not critical, but it helps the deal',
                                   'Long limits exclusivity to the task-order level and says it must not '
                                   'survive',
                                   'Public Contracting Institute (PCI) ([NB57wtT4xfs @ 00:48:53]); '
                                   'Streamline Government Contracts, LLC ([W-f5dCQEEkE @ 00:09:32])'],
                                  ['Which document is the prenup and which is the marriage',
                                   'Stephanie: the teaming agreement is the prenup, the subcontract is the '
                                   'marriage',
                                   'Sheenapreneur: the joint venture is the marriage with a prenup, a new '
                                   'SAM entity',
                                   'GovCon TechLab ([JYbjE63rG-Y @ 00:14:41]); Sheenapreneur ([JnxlzAHCjkY '
                                   '@ 00:01:47])'],
                                  ['NDA and paperwork with vendors before bidding',
                                   'Parks needs no NDA or exclusive deal, only a written pricing trail',
                                   'Lopez signs an NDA before disclosing relationships and the teaming '
                                   'agreement before submission',
                                   'Kizzy Parks ([F6Hwh89ornQ @ 00:06:44]); VA OSDBU (On Demand) '
                                   '([iLuva0z2cMA @ 00:47:03])'],
                                  ['Getting onto large prime radar screens',
                                   'Parks paid several thousand dollars for supplier directories and got '
                                   'zero calls',
                                   "Foster works each prime's small business program, specialist contact, "
                                   'supplier portal and teaming process',
                                   'Kizzy Parks ([ol1KkwjDTqg @ 00:04:14]); Akiesha Foster ([qnkHiXcQCHM @ '
                                   '00:03:34])'],
                                  ['Handling price pressure inside the team',
                                   'ASI saw primes tell the CO the sub cannot go cheaper, or everyone cuts '
                                   'about 10%',
                                   'Lopez prices from FPDS history, expects most bidders 5–10% under, and '
                                   'never splits price to win from price to execute',
                                   'ASI Education ([jYYGaPkanFU @ 00:07:03]); VA OSDBU (On Demand) '
                                   '([iLuva0z2cMA @ 01:26:27])'],
                                  ['Prime first or sub first for a newcomer',
                                   'Parks primes as a middleman with no past performance and no product',
                                   'Foster plans about 10 years as a tier-two sub before ever priming',
                                   'Kizzy Parks ([F6Hwh89ornQ @ 00:11:55]); Akiesha Foster ([qnkHiXcQCHM @ '
                                   '00:07:08])']]}},
              {'heading': 'Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The costliest losses came from deals that lived on trust. Jackie Lopez was '
                              'pushed off a five-year contract within six months by a greed-driven prime, '
                              "and her lawsuit recovered only part of the first year's profit; and her "
                              "warning is blunt: “if someone tells you that they're going to give you 49 "
                              "of a project but they're not willing to put it in writing I would be very "
                              "careful about that” [iLuva0z2cMA @ 00:25:31]. Kizzy Parks took a man's "
                              'promise of a monthly “bonus” for access to her existing client, collected 1 '
                              'of 12 payments, had no signed agreement, and ate roughly $20,000 '
                              '[ol1KkwjDTqg @ 00:06:22]. Mike Lore watched his team get “awarded eight of '
                              'these 11 but my company only received actual work on two,” and he warns: '
                              '“avoid agreements that promise best efforts or goals these rarely pan out,” '
                              'calling a poor teaming agreement “a shotgun wedding” [L-BpgTTiESM @ '
                              "00:12:41]. Stephanie's warning covers the same ground: a one-page letter of "
                              'intent is a “hope document,” after award the prime holds all the leverage, '
                              'and a handshake deal is how you end up “doing 80% of the work and getting '
                              'only 20% of the revenue” [JYbjE63rG-Y @ 00:03:34].',
                              'ELINT Capital says prime-or-sub is often dictated by capital, credit line '
                              'and cash position. Its worked example on a $2M-per-year set-aside services '
                              'task order has the prime doing 55% at roughly $80k a month, waiting 70–80 '
                              'days for payment, holding a payroll reserve near $175k, and fronting '
                              '$275–300k, about 14% of contract value, while a sub with a $400k slice '
                              'needs about $80k up front, about 20% [EpUc9OVjb4g @ 00:13:32]. The same '
                              'panel flags subs pushing pay-when-paid clauses capped near 60 days, '
                              'improper invoices restarting the 30-day clock, DOGE freezes holding '
                              'payments 3–4 months, and near-annual shutdowns; its advice is to fund 2–2.5 '
                              "months of payroll, and “it's better to subcontract than to get nothing” "
                              '[EpUc9OVjb4g @ 00:18:29]. Jackie Lopez prices the bid side of the burn: a '
                              '30k proposal cost across 10 proposals is 300k spent with nothing won '
                              '[iLuva0z2cMA @ 00:14:31]. ASI Education lived the LPTA version: as a sub it '
                              'refused to drop lower and lost, then watched the winner post low DC '
                              'salaries on LinkedIn; it calls LPTA “a race to the bottom” where lowballers '
                              'try to get “made well” through modifications [jYYGaPkanFU @ 00:23:25]. '
                              'Kizzy Parks adds the margin trap: taking a vendor quote and simply bolting '
                              "on a profit percentage, “it's not going to happen” [F6Hwh89ornQ @ "
                              '00:04:57].',
                              'Compliance landmines turn wins into forfeits. Theodore Watson says 31% of '
                              'firms using teaming agreements or JVs are “not quite familiar” with the '
                              'landmines competitors use to get an award revoked in a bid protest, '
                              'starting with limitations on subcontracting, where the prime generally '
                              'performs at least 51% of contract cost, and affiliation when a partner '
                              '“exercises too much control over the contract” [NP_UB6qiZhw @ 00:00:14]. '
                              'Stephanie makes it concrete: “if a prime is promising you 60% of the work '
                              'on a service contract set-aside, that deal is illegal on its face” '
                              "[JYbjE63rG-Y @ 00:12:50]. VA OSDBU's Shane adds that "
                              'limitation-on-subcontracting compliance is measured per base and option '
                              'period with no averaging, and the prime stays 100% responsible to the '
                              'government, including for sub bankruptcy and Service Contract Act issues '
                              '[iLuva0z2cMA @ 01:03:40]. On partner vetting, Mike Lore pulls a D&B report '
                              'on small primes, cites one prime that was declared financially '
                              "unacceptable, vets the prime's proposal capability, asks the client's view "
                              'of partners, verifies citations, and makes contingent hires [L-BpgTTiESM @ '
                              '00:11:13]. His exit rule for stalling partners: “in the case of reluctant '
                              'suitors the sooner you walk away the better.”'],
               'table': {'caption': 'Firsthand losses, traps and economics checks reported by named '
                                    'practitioners',
                         'headers': ['Failure Mode',
                                     'What Happened Firsthand',
                                     'Damage or Economics Check',
                                     'Expert Source'],
                         'rows': [['Prime pushes the sub off after award',
                                   'A greed-driven prime removed Jackie Lopez from a five-year contract '
                                   'within six months',
                                   "Her lawsuit recovered only part of the first year's profit",
                                   'VA OSDBU (On Demand) ([iLuva0z2cMA @ 00:45:31])'],
                                  ['Unsigned side deal for client access',
                                   'A man promised Kizzy Parks a monthly bonus for access to her existing '
                                   'client',
                                   'He paid 1 of 12 payments and she lost about $20,000 with nothing '
                                   'signed',
                                   'Kizzy Parks ([ol1KkwjDTqg @ 00:06:22])'],
                                  ['Team wins while the sub starves',
                                   'Mike Lore reports his team was awarded eight of these 11',
                                   'His own company only received actual work on two of them',
                                   'Centurion Research Solutions ([L-BpgTTiESM @ 00:12:41])'],
                                  ['Teaming agreement with no end date',
                                   'Karen Long saw one agreement drafted with no end date at all',
                                   'It locked a company up for about five years of exclusivity',
                                   'Streamline Government Contracts, LLC ([W-f5dCQEEkE @ 00:18:33])'],
                                  ['Sub contact disappears before performance',
                                   "A winner's sub contact had left the company after the bid went in",
                                   'The winner had to give the contract back to the agency',
                                   'Kizzy Parks ([F6Hwh89ornQ @ 00:07:00])'],
                                  ['Fronting payroll as a small prime',
                                   'ELINT Capital modeled a 55% prime on a $2M-per-year set-aside task '
                                   'order',
                                   'Roughly $275–300k up front, about 14% of contract value, before '
                                   'payment lands',
                                   'ELINT Capital ([EpUc9OVjb4g @ 00:13:32])'],
                                  ['Lock-down language traded away without leverage',
                                   "David Gallagher's 2020 census hardware client sought lock-down "
                                   'language on units and price',
                                   'The protective language was negotiated away for lack of leverage',
                                   'Public Contracting Institute (PCI) ([NB57wtT4xfs @ 00:17:15])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Four checks before you sign onto any team',
                           'body': 'Every gate below comes from a loss, lockout or forfeit a named '
                                   'practitioner reported. Clear all four before the proposal goes in.',
                           'items': ['Workshare is written as a floor, not a hope: “no less than 30%” '
                                     'beats “approximately,” and a 49% promise nobody will put in writing '
                                     'is a red flag [GovCon TechLab — JYbjE63rG-Y @ 00:14:55].',
                                     'Duration and survival are nailed down: the agreement has an end '
                                     'date, exclusivity does not survive, and it cannot terminate while '
                                     'the proposal is in source selection [Streamline Government '
                                     'Contracts, LLC — W-f5dCQEEkE @ 00:18:33].',
                                     'Limitation-on-subcontracting math is run per period: services 50%, '
                                     'general construction 15%/85%, specialty trade 25%/75%, measured per '
                                     'base and option period with no averaging [VA OSDBU (On Demand) — '
                                     'iLuva0z2cMA @ 01:09:29].',
                                     'Cash runway covers the payment lag: fund 2–2.5 months of payroll and '
                                     'consider invoice insurance when the prime is unfamiliar [ELINT '
                                     'Capital — EpUc9OVjb4g @ 00:53:13].']}}],
 'pull_quote': '“A handshake teaming deal is how you end up doing 80% of the work and getting only 20% of '
               'the revenue or even worse being ghosted when you found out your teaming partner has won a '
               'contract.” — GovCon TechLab (JYbjE63rG-Y @ 00:00:00).',
 'diagram_id': 'diag-04',
 'action_checklist': ['Name the specific capability gap a partner fills before you team, and pass on '
                      'partners who duplicate what you already have [GovCon TechLab — JYbjE63rG-Y @ '
                      '00:12:00].',
                      "Vet a partner's core values by checking the CEO's LinkedIn connections and calling "
                      'trusted mutual contacts, then pull award history from FPDS, USAspending, SBA '
                      'Dynamic Small Business Search and SAM.gov [VA OSDBU (On Demand) — iLuva0z2cMA @ '
                      '00:24:25].',
                      'Pull a D&B report on any small prime, vet its proposal capability, and discuss '
                      'pricing up front before committing [Centurion Research Solutions — L-BpgTTiESM @ '
                      '00:10:56].',
                      'Write workshare “for the duration of the contract including all option periods” and '
                      'add a pricing-lock clause so accepted pricing carries into the subcontract '
                      '[Streamline Government Contracts, LLC — W-f5dCQEEkE @ 00:06:00].',
                      'Run the limitation-on-subcontracting math on real numbers: a $1M WOSB contract '
                      'minus $100k airfare leaves $900k, so the prime must perform $450k [VA OSDBU (On '
                      'Demand) — iLuva0z2cMA @ 01:10:26].',
                      'Model the cash before choosing prime or sub, and fund 2–2.5 months of payroll to '
                      'survive payment lags [ELINT Capital — EpUc9OVjb4g @ 00:53:13].'],
 'statutory_citations': [{'title': 'VA OSDBU (On Demand) — Prime Sub, Teaming Agreements and Subcontracts '
                                   '[01:09:29]',
                          'url': 'https://www.youtube.com/watch?v=iLuva0z2cMA&t=4169s',
                          'relevance': 'Primary practitioner testimony on limitation-on-subcontracting '
                                       'percentages, workshare buffers, and a prime ejecting its sub after '
                                       'award.'},
                         {'title': 'Public Contracting Institute (PCI) — GovCon 101- Teaming [00:37:46]',
                          'url': 'https://www.youtube.com/watch?v=NB57wtT4xfs&t=2266s',
                          'relevance': 'Primary practitioner testimony on teaming agreement '
                                       'enforceability, exclusivity, and tailoring templates.'},
                         {'title': 'GovCon TechLab — How to Structure a Teaming Agreement in Government '
                                   'Contracting (So That You Don’t Get Burned) [00:14:41]',
                          'url': 'https://www.youtube.com/watch?v=JYbjE63rG-Y&t=881s',
                          'relevance': 'Primary practitioner testimony on the seven-clause teaming '
                                       'agreement and workshare floors.'},
                         {'title': 'ELINT Capital — Subcontracting & Teaming - Prime vs Sub: The Financial '
                                   'Trade-offs [00:13:32]',
                          'url': 'https://www.youtube.com/watch?v=EpUc9OVjb4g&t=812s',
                          'relevance': 'Primary practitioner testimony on prime versus sub cash '
                                       'requirements and payment risk.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'F6Hwh89ornQ',
                       'title': 'How to Master Subcontracting & Win Government Contracts in 2025 (Step by '
                                'Step)',
                       'channel': 'Kizzy Parks',
                       'author': 'Kizzy Parks',
                       'text': "You don't have to have an NDA with them, what's important is you do have "
                               'some type of written paper trail of pricing.',
                       'tip': "You don't have to have an NDA with them, what's important is you do have "
                              'some type of written paper trail of pricing.',
                       'timestamp': 420,
                       'timestamp_seconds': 420,
                       'timestamp_label': '[00:07:00]',
                       'url': 'https://www.youtube.com/watch?v=F6Hwh89ornQ&t=420s',
                       'markdown': '[00:07:00](https://www.youtube.com/watch?v=F6Hwh89ornQ&t=420s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'jYYGaPkanFU',
                       'title': 'Government Acquisition for Dummies - Prime Contractors & Subcontractors',
                       'channel': 'ASI Education',
                       'author': 'ASI Education',
                       'text': 'Greatest overall benefit does not mean cheapest.',
                       'tip': 'Greatest overall benefit does not mean cheapest.',
                       'timestamp': 746,
                       'timestamp_seconds': 746,
                       'timestamp_label': '[00:12:26]',
                       'url': 'https://www.youtube.com/watch?v=jYYGaPkanFU&t=746s',
                       'markdown': '[00:12:26](https://www.youtube.com/watch?v=jYYGaPkanFU&t=746s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'zqg5q_pZvdc',
                       'title': 'Subcontracting with Prime Government Contractors is a Must',
                       'channel': 'Neil McDonnell',
                       'author': 'Neil McDonnell',
                       'text': "The only definition of a prime contractor is they're the ones the "
                               'contracting officer signed a contract with.',
                       'tip': "The only definition of a prime contractor is they're the ones the "
                              'contracting officer signed a contract with.',
                       'timestamp': 513,
                       'timestamp_seconds': 513,
                       'timestamp_label': '[00:08:33]',
                       'url': 'https://www.youtube.com/watch?v=zqg5q_pZvdc&t=513s',
                       'markdown': '[00:08:33](https://www.youtube.com/watch?v=zqg5q_pZvdc&t=513s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'HKtAZzSL_GQ',
                       'title': 'BEST Teaming Agreement Strategies For 2025 Government Contracts',
                       'channel': 'Dr. Mel',
                       'author': 'Dr. Mel',
                       'text': "Vague or generic templates can't protect you in high stakes deals.",
                       'tip': "Vague or generic templates can't protect you in high stakes deals.",
                       'timestamp': 166,
                       'timestamp_seconds': 166,
                       'timestamp_label': '[00:02:46]',
                       'url': 'https://www.youtube.com/watch?v=HKtAZzSL_GQ&t=166s',
                       'markdown': '[00:02:46](https://www.youtube.com/watch?v=HKtAZzSL_GQ&t=166s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'iLuva0z2cMA',
                       'title': 'Prime Sub, Teaming Agreements and Subcontracts',
                       'channel': 'VA OSDBU (On Demand)',
                       'author': 'VA OSDBU (On Demand)',
                       'text': 'Never mix up the price to win and the price to execute, they have to be '
                               'one and the same.',
                       'tip': 'Never mix up the price to win and the price to execute, they have to be one '
                              'and the same.',
                       'timestamp': 5231,
                       'timestamp_seconds': 5231,
                       'timestamp_label': '[01:27:11]',
                       'url': 'https://www.youtube.com/watch?v=iLuva0z2cMA&t=5231s',
                       'markdown': '[01:27:11](https://www.youtube.com/watch?v=iLuva0z2cMA&t=5231s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'iLuva0z2cMA',
                       'title': 'Prime Sub, Teaming Agreements and Subcontracts',
                       'channel': 'VA OSDBU (On Demand)',
                       'author': 'VA OSDBU (On Demand)',
                       'text': "If someone tells you that they're going to give you 49 of a project but "
                               "they're not willing to put it in writing I would be very careful about "
                               'that.',
                       'tip': "If someone tells you that they're going to give you 49 of a project but "
                              "they're not willing to put it in writing I would be very careful about "
                              'that.',
                       'timestamp': 1593,
                       'timestamp_seconds': 1593,
                       'timestamp_label': '[00:26:33]',
                       'url': 'https://www.youtube.com/watch?v=iLuva0z2cMA&t=1593s',
                       'markdown': '[00:26:33](https://www.youtube.com/watch?v=iLuva0z2cMA&t=1593s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'JYbjE63rG-Y',
                       'title': 'How to Structure a Teaming Agreement in Government Contracting (So That '
                                'You Don’t Get Burned)',
                       'channel': 'GovCon TechLab',
                       'author': 'GovCon TechLab',
                       'text': "But hope isn't a contract and in the gov con business, what isn't in "
                               "writing doesn't exist.",
                       'tip': "But hope isn't a contract and in the gov con business, what isn't in "
                              "writing doesn't exist.",
                       'timestamp': 266,
                       'timestamp_seconds': 266,
                       'timestamp_label': '[00:04:26]',
                       'url': 'https://www.youtube.com/watch?v=JYbjE63rG-Y&t=266s',
                       'markdown': '[00:04:26](https://www.youtube.com/watch?v=JYbjE63rG-Y&t=266s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'T_HZxPdh7B8',
                       'title': 'How to Win GovCon Contracts (2025) with Subcontracting',
                       'channel': 'Humam Finding Sam',
                       'author': 'Humam Finding Sam',
                       'text': "Don't be afraid to cold outreach to these prime because again as much as "
                               'you need them, they need you.',
                       'tip': "Don't be afraid to cold outreach to these prime because again as much as "
                              'you need them, they need you.',
                       'timestamp': 366,
                       'timestamp_seconds': 366,
                       'timestamp_label': '[00:06:06]',
                       'url': 'https://www.youtube.com/watch?v=T_HZxPdh7B8&t=366s',
                       'markdown': '[00:06:06](https://www.youtube.com/watch?v=T_HZxPdh7B8&t=366s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'JnxlzAHCjkY',
                       'title': "What's the Difference Between JVs, Subcontracting & Teaming? | Government "
                                'Contracting',
                       'channel': 'Sheenapreneur',
                       'author': 'Sheenapreneur',
                       'text': 'So you may or may not need it, you should always have one.',
                       'tip': 'So you may or may not need it, you should always have one.',
                       'timestamp': 37,
                       'timestamp_seconds': 37,
                       'timestamp_label': '[00:00:37]',
                       'url': 'https://www.youtube.com/watch?v=JnxlzAHCjkY&t=37s',
                       'markdown': '[00:00:37](https://www.youtube.com/watch?v=JnxlzAHCjkY&t=37s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ol1KkwjDTqg',
                       'title': 'Teaming In Government Contracting | Government Contracts',
                       'channel': 'Kizzy Parks',
                       'author': 'Kizzy Parks',
                       'text': "That's the intent of teaming, you want to be stronger by coming together "
                               'not weaker.',
                       'tip': "That's the intent of teaming, you want to be stronger by coming together "
                              'not weaker.',
                       'timestamp': 486,
                       'timestamp_seconds': 486,
                       'timestamp_label': '[00:08:06]',
                       'url': 'https://www.youtube.com/watch?v=ol1KkwjDTqg&t=486s',
                       'markdown': '[00:08:06](https://www.youtube.com/watch?v=ol1KkwjDTqg&t=486s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'NP_UB6qiZhw',
                       'title': 'Contractor Teaming Agreements',
                       'channel': 'Theodore Watson',
                       'author': 'Theodore Watson',
                       'text': 'Generally the prime has to perform at least 51 percent of the contract '
                               'cost but depending on your industry classification code it could be less.',
                       'tip': 'Generally the prime has to perform at least 51 percent of the contract cost '
                              'but depending on your industry classification code it could be less.',
                       'timestamp': 50,
                       'timestamp_seconds': 50,
                       'timestamp_label': '[00:00:50]',
                       'url': 'https://www.youtube.com/watch?v=NP_UB6qiZhw&t=50s',
                       'markdown': '[00:00:50](https://www.youtube.com/watch?v=NP_UB6qiZhw&t=50s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'EpUc9OVjb4g',
                       'title': 'Subcontracting & Teaming - Prime vs Sub: The Financial Trade-offs',
                       'channel': 'ELINT Capital',
                       'author': 'ELINT Capital',
                       'text': 'So really the most important thing is to pick your prime contractor '
                               'carefully to have a good relationship with them.',
                       'tip': 'So really the most important thing is to pick your prime contractor '
                              'carefully to have a good relationship with them.',
                       'timestamp': 2038,
                       'timestamp_seconds': 2038,
                       'timestamp_label': '[00:33:58]',
                       'url': 'https://www.youtube.com/watch?v=EpUc9OVjb4g&t=2038s',
                       'markdown': '[00:33:58](https://www.youtube.com/watch?v=EpUc9OVjb4g&t=2038s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'NB57wtT4xfs',
                       'title': 'GovCon 101- Teaming',
                       'channel': 'Public Contracting Institute (PCI)',
                       'author': 'Public Contracting Institute (PCI)',
                       'text': 'Never sign just a standard teaming agreement.',
                       'tip': 'Never sign just a standard teaming agreement.',
                       'timestamp': 624,
                       'timestamp_seconds': 624,
                       'timestamp_label': '[00:10:24]',
                       'url': 'https://www.youtube.com/watch?v=NB57wtT4xfs&t=624s',
                       'markdown': '[00:10:24](https://www.youtube.com/watch?v=NB57wtT4xfs&t=624s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'W-f5dCQEEkE',
                       'title': "Tips of the Trade: Negotiating Teaming Agreements - Subcontractors' "
                                'Perspective',
                       'channel': 'Streamline Government Contracts, LLC',
                       'author': 'Streamline Government Contracts, LLC',
                       'text': 'Words such as Target or approximately are vague.',
                       'tip': 'Words such as Target or approximately are vague.',
                       'timestamp': 340,
                       'timestamp_seconds': 340,
                       'timestamp_label': '[00:05:40]',
                       'url': 'https://www.youtube.com/watch?v=W-f5dCQEEkE&t=340s',
                       'markdown': '[00:05:40](https://www.youtube.com/watch?v=W-f5dCQEEkE&t=340s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '3eoJWm0WffU',
                       'title': 'Prime vs Subcontractor: Which Path Should Beginners Choose in GovCon?',
                       'channel': 'Federal Contracts Lab',
                       'author': 'Federal Contracts Lab',
                       'text': 'Subcontracting is not a downgrade.',
                       'tip': 'Subcontracting is not a downgrade.',
                       'timestamp': 537,
                       'timestamp_seconds': 537,
                       'timestamp_label': '[00:08:57]',
                       'url': 'https://www.youtube.com/watch?v=3eoJWm0WffU&t=537s',
                       'markdown': '[00:08:57](https://www.youtube.com/watch?v=3eoJWm0WffU&t=537s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'L-BpgTTiESM',
                       'title': 'How to Successfully Navigate the World of Teaming and Subcontracting',
                       'channel': 'Centurion Research Solutions',
                       'author': 'Centurion Research Solutions',
                       'text': 'Our team was awarded eight of these 11 but my company only received actual '
                               'work on two.',
                       'tip': 'Our team was awarded eight of these 11 but my company only received actual '
                              'work on two.',
                       'timestamp': 761,
                       'timestamp_seconds': 761,
                       'timestamp_label': '[00:12:41]',
                       'url': 'https://www.youtube.com/watch?v=L-BpgTTiESM&t=761s',
                       'markdown': '[00:12:41](https://www.youtube.com/watch?v=L-BpgTTiESM&t=761s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'L-BpgTTiESM',
                       'title': 'How to Successfully Navigate the World of Teaming and Subcontracting',
                       'channel': 'Centurion Research Solutions',
                       'author': 'Centurion Research Solutions',
                       'text': 'My hard learned rule of thumb is that in the case of reluctant suitors the '
                               'sooner you walk away the better.',
                       'tip': 'My hard learned rule of thumb is that in the case of reluctant suitors the '
                              'sooner you walk away the better.',
                       'timestamp': 1148,
                       'timestamp_seconds': 1148,
                       'timestamp_label': '[00:19:08]',
                       'url': 'https://www.youtube.com/watch?v=L-BpgTTiESM&t=1148s',
                       'markdown': '[00:19:08](https://www.youtube.com/watch?v=L-BpgTTiESM&t=1148s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'qnkHiXcQCHM',
                       'title': '19 - How to Find Prime Contractors Looking for Subcontractors - SAIC',
                       'channel': 'Akiesha Foster',
                       'author': 'Akiesha Foster',
                       'text': 'See look, teammates are typically considered six to 12 months before the '
                               'release of the request for proposal, the RFP.',
                       'tip': 'See look, teammates are typically considered six to 12 months before the '
                              'release of the request for proposal, the RFP.',
                       'timestamp': 318,
                       'timestamp_seconds': 318,
                       'timestamp_label': '[00:05:18]',
                       'url': 'https://www.youtube.com/watch?v=qnkHiXcQCHM&t=318s',
                       'markdown': '[00:05:18](https://www.youtube.com/watch?v=qnkHiXcQCHM&t=318s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'}]}
