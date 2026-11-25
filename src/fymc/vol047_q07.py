from __future__ import annotations

CHAPTER_7 = {'id': 'Q7',
 'chapter_id': 'Q7',
 'chapter_number': 7,
 'question_number': 7,
 'slug': 'q07-substations-transformers-data-center-power-chain',
 'question_prompt': 'What do substations, transformers, and the utility-to-rack power chain involve, and '
                    'why do they gate data center energization?',
 'kicker': 'Q7 / THE BIG MONEY PLAYBOOKS',
 'title': 'Substations, Transformers and the Data Center Power Chain',
 'subtitle': 'How substations work, 138 kV walkthroughs and 60-minute design, radial, tapped and LILO '
             'layouts, 30-60-90-IFC design milestones, fast-track substation builds, transformer lead '
             'times, solid-state transformers and MVDC, transmission line parameters, and the grid-to-rack '
             'power path',
 'layout_template': 'thirty_day_roadmap',
 'reading_time_minutes': 15,
 'executive_summary': 'Practitioners agree the large power transformer is the gating item for AI data '
                      'center power. DOE-cited lead times run 3 to 4 years, Ryne Ogren quotes 2 to 3 '
                      "years, and APG's Dan Girard quotes 122 weeks. The consensus mechanics are owned "
                      'substations, interconnected or 2N redundant paths instead of radial single-source '
                      'feeds, and early utility engagement. In the field, Keentel Engineering gates design '
                      'at 30-60-90-IFC and puts the risk window between 30% and 60%. Keentel also warns '
                      'that ERCOT SB6 loads above 75 MW must deliver PSCAD models, ride-through curves and '
                      'harmonic data. APG compresses schedules with prebuilt control houses, reserved '
                      'queue spots, roughly 40-week breakers and 345 kV designs built on 230 kV products. '
                      'The practitioners split on three points: Ogren says substation proximity "has never '
                      'affected us," Critical Systems warns that premature orders create costly problems, '
                      'and TechTrainerNJ trades dual-utility feeds for diesel backup.',
 'key_metrics': [{'label': 'Large Transformer Lead Time (EPC Quote)',
                  'metric': 'Large Transformer Lead Time (EPC Quote)',
                  'value': '122 weeks',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "APG CEO Dan Girard's current transformer lead time, given after first "
                             'misspeaking it as 60 months',
                  'source': 'REsource Labs ([lFIWqD0EAkM @ 00:09:23])'},
                 {'label': 'Fast-Track Substation Build',
                  'metric': 'Fast-Track Substation Build',
                  'value': 'Under 6 months vs. 1.5 to 2 years',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "APG's Kansas substation build compared with what a large firm would take",
                  'source': 'REsource Labs ([lFIWqD0EAkM @ 00:03:28])'},
                 {'label': 'ERCOT SB6 Large-Load Threshold',
                  'metric': 'ERCOT SB6 Large-Load Threshold',
                  'value': 'Above 75 MW',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Loads above 75 MW must deliver PSCAD and positive-sequence models, '
                             'ride-through curves, harmonic data and fault contributions',
                  'source': 'Keentel Engineering ([u_aIABsRd0A @ 00:02:11])'},
                 {'label': 'Weak-Grid Short-Circuit Ratio After Line Trip',
                  'metric': 'Weak-Grid Short-Circuit Ratio After Line Trip',
                  'value': 'About 3.9; controllers unstable below 3',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'A 1,000 MW campus on a 345 kV bus loses strength after one line trip, close '
                             'to the controller instability floor',
                  'source': 'Keentel Engineering ([u_aIABsRd0A @ 00:03:52])'}],
 'sections': [{'heading': '1. The Practitioner Consensus',
               'paragraphs': ['Ryne Ogren kills the most common misconception first: substations do not '
                              '"hold power" [6_osryMHPf4 @ 00:05:43]. Practical Engineering breaks the job '
                              'into five functions, switching, protection, voltage transformation, '
                              'monitoring and safety [7Q-aVBv7PWM @ 00:02:24], and flags switching as the '
                              'dangerous one: "At high voltages, even air can act like a conductor, which '
                              'means even if you create a break in a line, electricity can continue '
                              'flowing in a phenomenon known as an arc" [7Q-aVBv7PWM @ 00:03:31]. Breakers '
                              'kill that arc with vacuum at lower voltages and oil or gas dielectric at '
                              'higher voltages, while fuses are one-time devices [7Q-aVBv7PWM @ 00:05:06]. '
                              'For site work, Ogren sorts substations into three buckets: transmission '
                              'stations stepping power down for long-distance transport at around 500 kV '
                              'or 230/345 kV, distribution substations, the type most common on data '
                              'center sites, and collector substations serving wind and solar, which are '
                              '"not relevant" for data centers [6_osryMHPf4 @ 00:02:41]. Gokce Capital '
                              'adds the ownership baseline: a substation usually belongs to a utility, but '
                              'a large industrial or commercial customer sometimes owns one [zeoe1qgsv2c @ '
                              '00:00:54], and an existing station must not exceed 100% of its rated '
                              'capacity [zeoe1qgsv2c @ 00:02:25].',
                              'Every practitioner who touches procurement lands on the same bottleneck: '
                              'the big transformer. Critical Systems Explained cites DOE lead times of 3 '
                              'to 4 years for large units [uEz7S-WjHG0 @ 00:01:12]. Ryne Ogren puts it at '
                              '"a two to three year lead time on these puppies right now" for units '
                              'weighing 50 to 100-plus tons, and warns that breakers are also very long '
                              'lead [6_osryMHPf4 @ 00:04:32]. Dan Girard of APG quotes 122 weeks after '
                              'first misspeaking "60 months" [lFIWqD0EAkM @ 00:09:23]. The cause is '
                              'physical, not paperwork. Each unit needs a grain-oriented steel core, '
                              'copper windings, drying, an oil-filled tank and bushings [uEz7S-WjHG0 @ '
                              '00:03:36], and a manufacturer "cannot simply double its output by adding a '
                              'night shift" because factory slots, skilled labor and materials are all '
                              'limited [uEz7S-WjHG0 @ 00:05:26]. Factory testing and oversize transport '
                              'stack more time on top [uEz7S-WjHG0 @ 00:06:19]. Critical Systems also '
                              'separates two clocks: the IEA reports grid queues as their own delay, so a '
                              'transformer delivered early cannot fix missing grid capacity [uEz7S-WjHG0 @ '
                              '00:07:29]. Girard frames the whole substation cycle as "lumpy," roughly 2.5 '
                              'years, which is why APG diversified into microgrids, solar and BESS '
                              '[lFIWqD0EAkM @ 00:04:32].',
                              'On reliability, the speakers agree that single-path supply is the enemy and '
                              'that true redundancy costs real money. TechTrainerNJ says the best case for '
                              'a Tier 4 site is two feeds from separate utilities or substations, but '
                              'because that is "very expensive" the usual answer is diesel generator '
                              'backup [QtOyye8fYNk @ 00:00:22]. Base Config ranks the levels: N is '
                              'unacceptable, N+1 often still shares a single path, and 2N is the Tier 4 '
                              'gold standard at about double the cost, because "this eliminates the path '
                              'failure point" [giNYYY0DnJw @ 00:02:09]. Kognito Key reaches the same '
                              'conclusion from the grid side. Radial and tapped layouts hang off a single '
                              'source, typical of rural areas, and a source failure means a "total '
                              'blackout" [u8ABTJm2_XQ @ 00:01:28]. LILO is more secure but "quite '
                              'expensive," and the interconnected layout is the "undisputed industry '
                              'standard" [u8ABTJm2_XQ @ 00:03:15]. Ownership is the other consensus lever. '
                              'Ryne Ogren says data centers target 99.999% uptime and that owning the '
                              'substation gets delivery faster than sharing one [6_osryMHPf4 @ 00:05:27]. '
                              'Base Config notes that hyperscalers target PUE below 1.2, sometimes 1.05, '
                              'and build their own substations [giNYYY0DnJw @ 00:06:55].'],
               'table': {'caption': 'Practitioner consensus on the data center substation and power chain',
                         'headers': ['Consensus Point',
                                     'What Practitioners Report',
                                     'Numbers Stated',
                                     'Expert Source'],
                         'rows': [['Substations switch, protect and transform power but never store it',
                                   'Five roles: switching, protection, voltage transformation, monitoring '
                                   'and safety; arcs make switching dangerous',
                                   'Breakers use vacuum at lower voltage and oil or gas dielectric at '
                                   'higher voltage',
                                   'Practical Engineering ([7Q-aVBv7PWM @ 00:02:24])'],
                                  ['Distribution substations are the type that matters on data center '
                                   'sites',
                                   'Collector substations serving wind and solar are called not relevant '
                                   'for data centers',
                                   'Transmission stations sit around 500 kV or 230/345 kV for '
                                   'long-distance transport',
                                   'Ryne Ogren ([6_osryMHPf4 @ 00:02:41])'],
                                  ['Large transformers are the longest pole in the build schedule',
                                   'Limited factory slots, skilled labor and materials; a night shift '
                                   'cannot double output',
                                   'DOE-cited lead times of 3 to 4 years for large transformer units',
                                   'Critical Systems Explained ([uEz7S-WjHG0 @ 00:01:12])'],
                                  ['A working EPC confirms transformer and breaker lead times are brutal',
                                   'APG quotes transformer and breaker lead times from its active '
                                   'substation builds',
                                   'Transformers at 122 weeks; HV breakers normally at 80-plus weeks',
                                   'REsource Labs ([lFIWqD0EAkM @ 00:09:23])'],
                                  ['Redundant paths beat single-path supply for uptime',
                                   'N is unacceptable, N+1 often shares one path, 2N is the Tier 4 gold '
                                   'standard',
                                   '2N redundancy runs about double the cost of a single path',
                                   'Base Config ([giNYYY0DnJw @ 00:01:27])'],
                                  ['Radial and tapped layouts expose the site to total blackout',
                                   'Single-source radial feeds are typical of rural areas; LILO is secure '
                                   'but quite expensive',
                                   'The interconnected layout is called the undisputed industry standard',
                                   'Kognito Key ([u8ABTJm2_XQ @ 00:03:15])'],
                                  ['Owning the substation speeds delivery compared with sharing one',
                                   'Data centers chase five-nines uptime and own their stations for faster '
                                   'delivery',
                                   '99.999% uptime target cited for data center operations',
                                   'Ryne Ogren ([6_osryMHPf4 @ 00:05:27])']]}},
              {'heading': '2. Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['Keentel Engineering runs substation design through four hard checkpoints. '
                              'The 30% package carries the single-line diagram, the design criteria '
                              'document and preliminary fault duty, which is flagged for validation by the '
                              'system impact study. Grounding and foundations are deliberately left open '
                              '[GAM0L1fXtiA @ 00:01:22]. At 60% the package supports a Class 2 cost '
                              'estimate and a 3D clash review, and grounding and duct-bank collisions are '
                              'the most common rework [GAM0L1fXtiA @ 00:02:15]. "The 90% package is fully '
                              'checked and essentially ready for final issue" [GAM0L1fXtiA @ 00:02:50], '
                              'and the discipline rule is that "nothing appears at IFC that has not '
                              'already been seen and reviewed" [GAM0L1fXtiA @ 00:03:48]. Sealing happens '
                              'at IFC under a state license and responsible charge [GAM0L1fXtiA @ '
                              '00:05:45], and Keentel places the real risk window between 30% and 60% '
                              '[GAM0L1fXtiA @ 00:15:03]. primtech solutions demos the tooling behind a '
                              '60-minute 138 kV design: an AutoCAD front end on a SQL database that '
                              'produces a digital twin [2FBThdUqgRg @ 00:00:19]. The model is built from '
                              'symbols, assemblies, bays, modules and part stations, and reusable modules '
                              'change everywhere once edited, so "you only make bays one time" '
                              '[2FBThdUqgRg @ 00:03:33]. Red BOM balloons flag unspecified items before a '
                              '30% handoff [2FBThdUqgRg @ 00:43:02].',
                              'For large loads, the interconnection package is now a modeling job. Keentel '
                              'Engineering ties the shift to July 2024, when 1,500 MW of data center load '
                              'dropped in 82 seconds after six faults [u_aIABsRd0A @ 00:00:54], and says '
                              '"NERC, ERCOT, and utilities are rewriting the rules for computational '
                              'loads" [u_aIABsRd0A @ 00:01:15]. Under ERCOT SB6, loads above 75 MW must '
                              'deliver PSCAD and positive-sequence models, ride-through curves, harmonic '
                              'data and fault contributions [u_aIABsRd0A @ 00:02:11]. The working rule: '
                              '"behavior is assumed unless it is specified" [u_aIABsRd0A @ 00:03:14]. '
                              "Keentel's weak-grid example is a 1,000 MW campus on a 345 kV bus where one "
                              'line trip drops the short-circuit ratio to about 3.9, and controllers go '
                              'unstable below 3. That is why "early EMT screening prevents late-stage '
                              'redesigns" [u_aIABsRd0A @ 00:04:13]. On the hardware list, Ryne Ogren says '
                              'some Chinese transformers are not approved by transmission operators, and '
                              '"they\'ll give you an approved manufacturer list on these transformers" '
                              '[6_osryMHPf4 @ 00:04:19]. SpeedFreakLS1 adds the contractual edge: the '
                              'utility can curtail a 150 MW farm to 20 or 50 MW within minutes, which is '
                              '"money out the door," and can curtail it directly if the owner does not '
                              'comply [-RBp8jOUA1U @ 00:02:45].',
                              "Dan Girard's APG attacks the calendar directly. The firm built a Kansas "
                              'substation in under 6 months, against "a year and a half to two years" at a '
                              'large firm [lFIWqD0EAkM @ 00:03:28]. HV breakers that normally take 80-plus '
                              'weeks arrive in about 40 through a relationship with a new manufacturer '
                              '[lFIWqD0EAkM @ 00:10:20]. At 35 kV, APG uses prebuilt control houses, '
                              'factory FAT testing and reserved queue spots [lFIWqD0EAkM @ 00:09:39]. The '
                              'team also designs to the 345 kV standard while using 230 kV products to '
                              'speed the build [lFIWqD0EAkM @ 00:12:41]. Critical Systems Explained adds '
                              'the owner-side moves: involve the utility early, identify long-lead '
                              'equipment early, standardize specifications, and use phased energization or '
                              "alternative sites [uEz7S-WjHG0 @ 00:09:15]. SpeedFreakLS1's 138 kV walk "
                              'supplies the field specs. The transformer is a 138/34.5 kV, 183 MVA '
                              'ONAN/ONAF unit with taps 1 through 33 at plus or minus 10% [-RBp8jOUA1U @ '
                              '00:11:54]. A roughly $50k neutral grounding reactor saves "hundreds of '
                              'thousands" in copper [-RBp8jOUA1U @ 00:17:46], but the factory ground strap '
                              'bypasses the reactor and must be removed [-RBp8jOUA1U @ 00:19:13]. PTs need '
                              '5 A fuses or they "melt" in 3 seconds [-RBp8jOUA1U @ 00:21:43].'],
               'table': {'caption': 'Street mechanics, tools and numbers for substation design, '
                                    'interconnection and build',
                         'headers': ['Mechanic',
                                     'Exact Numbers or Tool',
                                     'How Practitioners Use It',
                                     'Expert Source'],
                         'rows': [['30% design package scope and deliberate open items',
                                   'Single-line diagram, design criteria document and preliminary fault '
                                   'duty',
                                   'Fault duty flagged for system impact study validation; grounding and '
                                   'foundations left open',
                                   'Keentel Engineering ([GAM0L1fXtiA @ 00:01:22])'],
                                  ['60% design package with full 3D clash review',
                                   'Class 2 cost estimate plus a 3D clash review of the yard',
                                   'Catches grounding and duct-bank collisions, the most common rework on '
                                   'substation jobs',
                                   'Keentel Engineering ([GAM0L1fXtiA @ 00:02:15])'],
                                  ['Model-driven substation layout on a digital twin',
                                   'AutoCAD on SQL; 8 ft phase spacing; 954 cable; 5 in tube with damping '
                                   'cable',
                                   'Reusable modules update everywhere when edited, and bays are '
                                   'duplicated by drag-copy',
                                   'primtech solutions ([2FBThdUqgRg @ 00:10:56])'],
                                  ['Large-load interconnection deliverables under ERCOT SB6',
                                   'Loads above 75 MW; PSCAD and positive-sequence models plus '
                                   'ride-through curves',
                                   'Harmonic data and fault contributions are submitted alongside the '
                                   'model package',
                                   'Keentel Engineering ([u_aIABsRd0A @ 00:02:11])'],
                                  ['Weak-grid stability screen before any equipment order',
                                   '1,000 MW campus on a 345 kV bus; SCR drops to about 3.9',
                                   'Controllers go unstable below SCR 3, so stability is resolved before '
                                   'ordering equipment',
                                   'Keentel Engineering ([u_aIABsRd0A @ 00:03:52])'],
                                  ['Breaker lead-time compression through supplier relationships',
                                   'HV breakers in about 40 weeks versus 80-plus weeks normally',
                                   'Relationship with a new manufacturer, plus prebuilt control houses and '
                                   'reserved queue spots',
                                   'REsource Labs ([lFIWqD0EAkM @ 00:10:20])'],
                                  ['Grounding cost tradeoff on the transformer low side',
                                   'Neutral grounding reactor about $50k, saving hundreds of thousands in '
                                   'copper',
                                   'Remove the factory ground strap, which otherwise bypasses the reactor '
                                   'entirely',
                                   'SpeedFreakLS1 ([-RBp8jOUA1U @ 00:17:46])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Schedule and Spec Moves From the Field',
                           'body': 'Moves the speakers use to cut months off substation delivery and to '
                                   'stop rework before it reaches IFC.',
                           'items': ['Design the substation to the 345 kV standard but use 230 kV products '
                                     'to speed the build [REsource Labs — lFIWqD0EAkM @ 00:12:41]',
                                     "Get the transmission operator's approved-manufacturer list before "
                                     'quoting transformers, because some Chinese units are not approved '
                                     '[Ryne Ogren — 6_osryMHPf4 @ 00:04:19]',
                                     'On hyperscale jobs, procure the main power transformer separately at '
                                     'the 60% stage instead of waiting for IFC [Keentel Engineering — '
                                     'GAM0L1fXtiA @ 00:09:23]',
                                     'Use BOM balloons to flag unspecified items in red before handing off a '
                                     '30% design, and to catch stray objects parked at the origin '
                                     '[primtech solutions — 2FBThdUqgRg @ 00:43:02]']},
               'sop_steps': [{'step': 1,
                              'title': 'Lock the Utility and Hardware Lists',
                              'action': 'Engage the utility early and pull the approved-manufacturer list '
                                        'before any transformer quote.',
                              'detail': 'Critical Systems Explained says to involve the utility early '
                                        '[Critical Systems Explained — uEz7S-WjHG0 @ 00:08:39]. Ryne Ogren '
                                        'says the transmission operator will hand over an approved '
                                        'manufacturer list for transformers [Ryne Ogren — 6_osryMHPf4 @ '
                                        '00:04:19].'},
                             {'step': 2,
                              'title': 'Screen the Load Before Ordering',
                              'action': 'Run EMT and short-circuit-ratio screening and assemble the SB6 '
                                        'model package for loads above 75 MW.',
                              'detail': 'Keentel Engineering says "early EMT screening prevents late-stage '
                                        'redesigns" [Keentel Engineering — u_aIABsRd0A @ 00:04:13]. On its '
                                        '600 MW Texas campus, the stability issue was resolved before '
                                        'equipment was ordered [Keentel Engineering — u_aIABsRd0A @ '
                                        '00:11:23].'},
                             {'step': 3,
                              'title': 'Drive the 30-60-90-IFC Checkpoints',
                              'action': 'Freeze the single-line at 30%, clash-check at 60%, fully check at '
                                        '90%, and seal at IFC.',
                              'detail': 'Keentel Engineering places the risk window between 30% and 60% '
                                        '[Keentel Engineering — GAM0L1fXtiA @ 00:15:03]. primtech '
                                        'solutions runs phase-phase, phase-earth, fence and vehicle '
                                        'drive-path clearance checks inside the model [primtech solutions '
                                        '— 2FBThdUqgRg @ 00:37:23].'},
                             {'step': 4,
                              'title': 'Compress Procurement and Close the Punch List',
                              'action': 'Reserve factory queue spots, prebuild control houses, then '
                                        'punch-list the yard before energization.',
                              'detail': 'APG uses prebuilt control houses, factory FAT testing and '
                                        'reserved queue spots at 35 kV [REsource Labs — lFIWqD0EAkM @ '
                                        "00:09:39]. SpeedFreakLS1's punch list calls for supporting "
                                        'liquid-tight flex within 12 or 18 in and adding duct seal '
                                        '[SpeedFreakLS1 — -RBp8jOUA1U @ 00:03:53].'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The lead-time number every powered-land operator underwrites against is not '
                              'settled, and the spread rewrites the whole procurement calendar. Critical '
                              'Systems Explained anchors on DOE figures of 3-4 years for large power '
                              'transformers and treats that wait as the single biggest bottleneck in '
                              'getting an AI campus energized [uEz7S-WjHG0 @ 00:01:12]. Ryne Ogren, a '
                              'private equity investor in data centers and energy, quotes a tighter '
                              'two-to-three-year window on units weighing 50 to 100+ tons, and flags '
                              'high-voltage breakers as very long lead in their own right [6_osryMHPf4 @ '
                              '00:04:32]. The sharper split is on when to pull the trigger. Keentel '
                              "Engineering's hyperscale case procured the main power transformer "
                              'separately at the 60% design stage, long before the IFC seal, so the '
                              'longest pole in the tent started its clock early [GAM0L1fXtiA @ 00:09:23]. '
                              'Critical Systems Explained pushes back that ordering sooner can help, but '
                              'premature orders can create costly problems if final specifications change, '
                              'and pairs any early order with standardized specifications wherever '
                              'possible so a revised design does not strand a custom unit [uEz7S-WjHG0 @ '
                              '00:08:58]. The operator bet is on spec stability: freeze the electrical '
                              'design hard enough to survive an early order, or sit in the factory queue.',
                              'Practitioners also split on whether a powered-land play should chase an '
                              'existing substation at all. Ryne Ogren is blunt that proximity to an '
                              'existing substation has never affected their deals [6_osryMHPf4 @ '
                              '00:06:24]. The lever Ogren pushes instead is ownership: with data centers '
                              'targeting 99.999% uptime, owning the substation delivers faster than '
                              'sharing one [6_osryMHPf4 @ 00:05:27]. Gokce Capital runs the opposite '
                              'checklist, listing proximity to transmission, a central location, room for '
                              'clearances, heavy-equipment access, room for expansion, zoning and security '
                              'as siting criteria, and warning that an existing substation must not be '
                              'pushed past 100% of its rated capacity [zeoe1qgsv2c @ 00:01:13]. Gokce '
                              'Capital also notes the owner is usually a utility but sometimes a large '
                              'industrial or commercial customer, which is exactly the slot a campus '
                              "developer steps into. On who builds the yard, APG's Dan Girard sells raw "
                              'speed against the majors, claiming a Kansas substation finished in under '
                              'six months where a large firm would take a year and a half to two years '
                              "[lFIWqD0EAkM @ 00:03:28]. Ogren's playbook is to own the yard outright; "
                              "Girard's is to hire a fast EPC; Gokce's is to site against transmission and "
                              'respect the 100% rating on anything tapped.',
                              'Redundancy architecture is where the cost arguments get loud. TechTrainerNJ '
                              'says the best case for a Tier 4 site is two feeds from separate utilities '
                              'or substations, but because that is very expensive the usual approach is '
                              'diesel generator backup [QtOyye8fYNk @ 00:00:22]. Kognito Key grades the '
                              'substation layouts the same way: radial and tapped arrangements hang on a '
                              'single source, typical of rural areas, where a source failure means a total '
                              'blackout, while LILO is more secure but quite expensive, and the '
                              'interconnected layout is called the undisputed industry standard '
                              '[u8ABTJm2_XQ @ 00:02:45]. Base Config calls N unacceptable, warns that N+1 '
                              'often still shares a single path, and crowns 2N as the Tier 4 gold standard '
                              'at roughly double the cost because it eliminates the path failure point '
                              '[giNYYY0DnJw @ 00:01:27]. InfraEnergy Academy argues the legacy chain '
                              'itself is the problem, pitching block-redundant UPS in place of '
                              'distributed-redundant designs so active lines can run at full throttle, fed '
                              'by a solid-state transformer that converts medium-voltage AC to 800 V DC in '
                              'one step [YSqciE_dMbY @ 00:03:42]. One camp buys redundancy with duplicate '
                              'feeds and generators; the other redesigns the conversion chain so less '
                              'copper and fewer stages carry the load.'],
               'table': {'caption': 'Competing playbooks on transformer timing, breakers, build speed, '
                                    'siting and redundancy',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Large power transformer lead time to underwrite',
                                   'DOE-cited lead times of 3-4 years for large transformers set the '
                                   'conservative planning case',
                                   'Ogren quotes a two-to-three-year lead time; Girard quotes 122 weeks '
                                   'after correcting 60 months',
                                   'Critical Systems Explained ([uEz7S-WjHG0 @ 00:01:12]); Ryne Ogren '
                                   '([6_osryMHPf4 @ 00:04:32]); REsource Labs ([lFIWqD0EAkM @ 00:09:23])'],
                                  ['When to order the main power transformer',
                                   'Procure the main power transformer separately at the 60% design stage '
                                   'on hyperscale work',
                                   'Order sooner only with standardized, stable specs because premature '
                                   'orders get costly if specs change',
                                   'Keentel Engineering ([GAM0L1fXtiA @ 00:09:23]); Critical Systems '
                                   'Explained ([uEz7S-WjHG0 @ 00:08:58])'],
                                  ['High-voltage breaker procurement path',
                                   'Accept normal HV breaker lead times that run 80-plus weeks from '
                                   'established suppliers',
                                   'Cut breaker delivery to about 40 weeks through a relationship with a '
                                   'new manufacturer',
                                   'REsource Labs ([lFIWqD0EAkM @ 00:10:20]); REsource Labs ([lFIWqD0EAkM '
                                   '@ 00:10:36])'],
                                  ['Substation build speed and equipment class',
                                   'A large firm takes a year and a half to two years to deliver a '
                                   'substation',
                                   'APG built Kansas in under six months, designing to 345 kV standard '
                                   'with 230 kV products',
                                   'REsource Labs ([lFIWqD0EAkM @ 00:03:28]); REsource Labs ([lFIWqD0EAkM '
                                   '@ 00:12:41])'],
                                  ['Proximity to an existing substation',
                                   'Site near transmission and never load an existing substation past 100% '
                                   'of rating',
                                   "Proximity to an existing substation has never affected Ogren's deals; "
                                   'owning the substation delivers faster',
                                   'Gokce Capital ([zeoe1qgsv2c @ 00:01:13]); Ryne Ogren ([6_osryMHPf4 @ '
                                   '00:06:24])'],
                                  ['Equipment race versus grid capacity',
                                   'Hyperscalers build their own substations and target PUE below 1.2, '
                                   'sometimes reaching 1.05',
                                   'Grid queues are a separate delay; an early transformer cannot fix '
                                   'missing grid capacity, so consider alternative sites',
                                   'Base Config ([giNYYY0DnJw @ 00:06:55]); Critical Systems Explained '
                                   '([uEz7S-WjHG0 @ 00:07:29])'],
                                  ['How to buy feed redundancy',
                                   'Two feeds from separate utilities or substations is the Tier 4 best '
                                   'case but very expensive',
                                   'Usual approach is diesel generator backup; 2N runs about double the '
                                   'cost but eliminates path failure',
                                   'TechTrainerNJ ([QtOyye8fYNk @ 00:00:22]); Base Config ([giNYYY0DnJw @ '
                                   '00:01:27])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The SpeedFreakLS1 walk of a 138 kV to 34.5 kV yard is a catalog of traps '
                              'that only surface at commissioning. The biggest: the factory ground strap '
                              'on the neutral grounding reactor bypasses the reactor and must be removed, '
                              'which matters because that roughly $50k reactor is what saves hundreds of '
                              'thousands in copper [-RBp8jOUA1U @ 00:19:13]. Station service runs 100 kVA '
                              'at 19.9 kV, and the PTs need 5 A fuses or they melt in 3 seconds '
                              '[-RBp8jOUA1U @ 00:21:43]. Smaller misses pile up on the high-side punch '
                              'list: liquid-tight flex conduit that has to be supported within 12 or 18 '
                              'inches and finished with duct seal, plus missing torque marks on the '
                              'grounds [-RBp8jOUA1U @ 00:03:53]. Practical Engineering explains why '
                              'switching mistakes are dangerous rather than cosmetic: at high voltages '
                              'even air can act like a conductor, so a break in a line can keep carrying '
                              'current as an arc, which is why breakers lean on vacuum at lower voltage '
                              'and oil or gas dielectric at higher voltage [7Q-aVBv7PWM @ 00:03:31]. The '
                              'lesson from the walk is that a yard can be energized-ready on paper and '
                              'still carry a strap, a fuse or a conduit run that defeats the protection '
                              'design.',
                              'On the design side, the failures cluster in a predictable window. Keentel '
                              'Engineering places the risk between the 30% and 60% packages [GAM0L1fXtiA @ '
                              '00:15:03], and names grounding and duct-bank collisions as the most common '
                              'rework caught in the 60% 3D clash review that also supports a Class 2 cost '
                              'estimate [GAM0L1fXtiA @ 00:02:15]. Their 30% package carries preliminary '
                              'fault duty flagged for validation by the system impact study, with '
                              'grounding and foundations deliberately left unfinished, so anyone pricing '
                              'land or headroom off a 30% set is pricing a moving number. primtech '
                              'solutions attacks the same problem in software: BOM balloons flag unspecified '
                              'items in red before a 30% design is handed off, and the same check catches '
                              'stray objects sitting at the origin, while reusable modules propagate '
                              'changes everywhere when edited, so one bad module repeats everywhere it is '
                              'reused [2FBThdUqgRg @ 00:43:02]. For AI loads with solid-state '
                              "transformers, Keentel Engineering's rule of thumb is that behavior is "
                              'assumed unless it is specified, and early EMT screening prevents late-stage '
                              'redesigns [u_aIABsRd0A @ 00:04:13]. Skip the early model and the redesign '
                              'lands after the money is committed.',
                              'The economics traps sit at the grid interface. Keentel Engineering opens '
                              'with the trigger event: in July 2024, 1,500 MW of data center load dropped '
                              'in 82 seconds after 6 faults, which has NERC, ERCOT and utilities rewriting '
                              'the rules for computational loads [u_aIABsRd0A @ 00:00:54]. SpeedFreakLS1 '
                              'spells out the contractual bite on the generation side: a 150 MW farm can '
                              'be curtailed to 20 or 50 MW within minutes, which is money out the door, '
                              'and if the operator does not comply the utility can curtail the farm itself '
                              '[-RBp8jOUA1U @ 00:02:45]. Ryne Ogren warns that some Chinese transformers '
                              'are not approved by transmission operators, so the fix is to get the '
                              "operator's approved-manufacturer list before committing to a unit "
                              '[6_osryMHPf4 @ 00:03:36]. Gokce Capital adds the zoning trap: PNM bought '
                              "four lots in North Albuquerque Acres in 2020, a resident's home sat 120 ft "
                              'away, and the county unanimously denied the special use permit in 2021 '
                              '[zeoe1qgsv2c @ 00:04:32]. Each one strands capital that was already spent '
                              'before the blocker surfaced. For a powered-land buyer, those are diligence '
                              'items, not afterthoughts.'],
               'table': {'caption': 'Firsthand failure modes from yard walks, design reviews, grid events '
                                    'and permitting fights',
                         'headers': ['Failure Mode',
                                     'What Practitioners Reported',
                                     'Operator Check',
                                     'Expert Source'],
                         'rows': [['Factory ground strap left on the neutral grounding reactor',
                                   'The strap bypasses the roughly $50k reactor that saves hundreds of '
                                   'thousands in copper',
                                   'Remove the factory ground strap before energizing the transformer '
                                   'neutral path',
                                   'SpeedFreakLS1 ([-RBp8jOUA1U @ 00:19:13]); SpeedFreakLS1 ([-RBp8jOUA1U '
                                   '@ 00:17:46])'],
                                  ['Wrong PT fusing on station service',
                                   'PTs on 100 kVA, 19.9 kV station service melt in 3 seconds without '
                                   'proper fuses',
                                   'Verify 5 A fuses are installed on every PT before closing in',
                                   'SpeedFreakLS1 ([-RBp8jOUA1U @ 00:21:43])'],
                                  ['Bird guards and oil handling that may not perform',
                                   'Bird guards with only a 1 in gap are doubted; the Oil Minder ejects '
                                   'water but not oil',
                                   'Inspect guard gaps and confirm oil-pump behavior during the final yard '
                                   'walk',
                                   'SpeedFreakLS1 ([-RBp8jOUA1U @ 00:24:00]); SpeedFreakLS1 ([-RBp8jOUA1U '
                                   '@ 00:32:34])'],
                                  ['Rework landing between the 30% and 60% packages',
                                   'Grounding and duct-bank collisions are the most common rework found at '
                                   'the 60% clash review',
                                   'Run the 3D clash review and treat 30% fault duty as unvalidated until '
                                   'the impact study',
                                   'Keentel Engineering ([GAM0L1fXtiA @ 00:02:15]); Keentel Engineering '
                                   '([GAM0L1fXtiA @ 00:15:03])'],
                                  ['Weak-grid controller instability on a large campus',
                                   'On a 1,000 MW campus at 345 kV, a line trip drops SCR near 3.9; '
                                   'controllers go unstable below 3',
                                   'Screen stability early; the 600 MW Texas campus resolved it before '
                                   'ordering equipment',
                                   'Keentel Engineering ([u_aIABsRd0A @ 00:03:52]); Keentel Engineering '
                                   '([u_aIABsRd0A @ 00:11:23])'],
                                  ['DC arc flash and stored energy without a standard method',
                                   'IEEE 1584 does not cover DC; 20 converters at 2 mF store 720 kJ at 6 '
                                   'kV',
                                   'Use NFPA 70E alternative methods and choose solid-state, hybrid or '
                                   'converter-blocking protection',
                                   'Keentel Engineering ([u_aIABsRd0A @ 00:08:09]); Keentel Engineering '
                                   '([u_aIABsRd0A @ 00:04:33])'],
                                  ['Ordering a transformer the transmission operator will not accept',
                                   'Some Chinese transformers are not approved by transmission operators '
                                   'for interconnection',
                                   "Get the transmission operator's approved-manufacturer list before "
                                   'placing any transformer order',
                                   'Ryne Ogren ([6_osryMHPf4 @ 00:03:36]); Ryne Ogren ([6_osryMHPf4 @ '
                                   '00:04:19])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Hold capital until these four practitioner-reported traps are cleared',
                           'body': 'Each gate below comes from a loss, near-miss or warning the '
                                   'practitioners reported firsthand. Clear them before releasing '
                                   'transformer deposits, land closings or energization dates.',
                           'items': ["Pull the transmission operator's approved-manufacturer list before "
                                     'any transformer order, because some Chinese units are not approved '
                                     '[Ryne Ogren — 6_osryMHPf4 @ 00:04:19].',
                                     'Confirm the factory ground strap is off the neutral grounding '
                                     'reactor and every PT carries a 5 A fuse before energizing '
                                     '[SpeedFreakLS1 — -RBp8jOUA1U @ 00:19:13].',
                                     'For ERCOT loads above 75 MW, deliver PSCAD and positive-sequence '
                                     'models, ride-through curves, harmonic data and fault contributions '
                                     'before ordering, since behavior is assumed unless specified [Keentel '
                                     'Engineering — u_aIABsRd0A @ 00:02:11].',
                                     'Treat grid queue position as separate from transformer delivery, '
                                     'because a transformer delivered early cannot fix missing grid '
                                     'capacity [Critical Systems Explained — uEz7S-WjHG0 @ 00:07:29].']}}],
 'pull_quote': '"Ordering sooner can help, but premature orders can create costly problems if final '
               'specifications change." — Critical Systems Explained (uEz7S-WjHG0 @ 00:08:58).',
 'diagram_id': 'diag-01',
 'action_checklist': ['Involve the utility early and identify long-lead equipment early, then standardize '
                      'specifications so an early order survives design changes [Critical Systems '
                      'Explained — uEz7S-WjHG0 @ 00:08:39].',
                      "Request the transmission operator's approved-manufacturer list for transformers "
                      'before soliciting bids [Ryne Ogren — 6_osryMHPf4 @ 00:04:19].',
                      'Run the 30-60-90-IFC sequence with a 60% 3D clash review aimed at grounding and '
                      'duct-bank collisions [Keentel Engineering — GAM0L1fXtiA @ 00:02:15].',
                      'Package PSCAD and positive-sequence models, ride-through curves, harmonic data and '
                      'fault contributions for ERCOT SB6 loads above 75 MW [Keentel Engineering — '
                      'u_aIABsRd0A @ 00:02:11].',
                      'Run phase-phase, phase-earth, fence and vehicle drive-path clearance checks before '
                      'handing off a 30% design [primtech solutions — 2FBThdUqgRg @ 00:37:23].',
                      'Walk the yard punch list for torque marks on grounds, conduit support, duct seal '
                      'and switch open/close indicators before energization [SpeedFreakLS1 — -RBp8jOUA1U @ '
                      '00:04:25].'],
 'statutory_citations': [{'title': 'Critical Systems Explained — Why AI Data Centers Can Wait Years for '
                                   'One Transformer [00:08:58]',
                          'url': 'https://www.youtube.com/watch?v=uEz7S-WjHG0&t=538s',
                          'relevance': 'Primary practitioner testimony on transformer lead times, '
                                       'premature-order risk and grid queue delays.'},
                         {'title': 'Keentel Engineering — Substation Design | 30–60–90–IFC | Keentel '
                                   'Engineering [00:15:03]',
                          'url': 'https://www.youtube.com/watch?v=GAM0L1fXtiA&t=903s',
                          'relevance': 'Primary practitioner testimony on the 30%-to-60% design risk '
                                       'window and common rework.'},
                         {'title': 'Keentel Engineering — Solid-State Transformers & MVDC: Revolutionizing '
                                   'AI Data Center Power Systems | Keentel Engineering [00:00:54]',
                          'url': 'https://www.youtube.com/watch?v=u_aIABsRd0A&t=54s',
                          'relevance': 'Primary practitioner testimony on load-loss events, weak-grid '
                                       'stability and DC protection for AI campuses.'},
                         {'title': 'SpeedFreakLS1 — 138 kV High Voltage Substation Walk [00:19:13]',
                          'url': 'https://www.youtube.com/watch?v=-RBp8jOUA1U&t=1153s',
                          'relevance': 'Primary practitioner testimony on commissioning punch-list traps '
                                       'in a 138 kV yard.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': '-RBp8jOUA1U',
                       'title': '138 kV High Voltage Substation Walk',
                       'channel': 'SpeedFreakLS1',
                       'author': 'SpeedFreakLS1',
                       'text': 'A 150 MW farm can be curtailed down to 20 or 50 MW within minutes, and '
                               'that is money out the door.',
                       'tip': 'A 150 MW farm can be curtailed down to 20 or 50 MW within minutes, and that '
                              'is money out the door.',
                       'timestamp': 165,
                       'timestamp_seconds': 165,
                       'timestamp_label': '[00:02:45]',
                       'url': 'https://www.youtube.com/watch?v=-RBp8jOUA1U&t=165s',
                       'markdown': '[00:02:45](https://www.youtube.com/watch?v=-RBp8jOUA1U&t=165s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '-RBp8jOUA1U',
                       'title': '138 kV High Voltage Substation Walk',
                       'channel': 'SpeedFreakLS1',
                       'author': 'SpeedFreakLS1',
                       'text': 'The factory ground strap bypasses the neutral grounding reactor, so it has '
                               'to be removed.',
                       'tip': 'The factory ground strap bypasses the neutral grounding reactor, so it has '
                              'to be removed.',
                       'timestamp': 1153,
                       'timestamp_seconds': 1153,
                       'timestamp_label': '[00:19:13]',
                       'url': 'https://www.youtube.com/watch?v=-RBp8jOUA1U&t=1153s',
                       'markdown': '[00:19:13](https://www.youtube.com/watch?v=-RBp8jOUA1U&t=1153s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '2FBThdUqgRg',
                       'title': 'Design a complete 138 kV Substation in only 60 minutes - Live '
                                'Presentation @SDSIC 2025 Spring Event',
                       'channel': 'primtech solutions',
                       'author': 'primtech solutions',
                       'text': 'So you only make bays one time.',
                       'tip': 'So you only make bays one time.',
                       'timestamp': 213,
                       'timestamp_seconds': 213,
                       'timestamp_label': '[00:03:33]',
                       'url': 'https://www.youtube.com/watch?v=2FBThdUqgRg&t=213s',
                       'markdown': '[00:03:33](https://www.youtube.com/watch?v=2FBThdUqgRg&t=213s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'u_aIABsRd0A',
                       'title': 'Solid-State Transformers & MVDC: Revolutionizing AI Data Center Power '
                                'Systems | Keentel Engineering',
                       'channel': 'Keentel Engineering',
                       'author': 'Keentel Engineering',
                       'text': 'Early EMT screening prevents late-stage redesigns.',
                       'tip': 'Early EMT screening prevents late-stage redesigns.',
                       'timestamp': 253,
                       'timestamp_seconds': 253,
                       'timestamp_label': '[00:04:13]',
                       'url': 'https://www.youtube.com/watch?v=u_aIABsRd0A&t=253s',
                       'markdown': '[00:04:13](https://www.youtube.com/watch?v=u_aIABsRd0A&t=253s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'QtOyye8fYNk',
                       'title': 'Data Center Power Chain - Animation',
                       'channel': 'TechTrainerNJ',
                       'author': 'TechTrainerNJ',
                       'text': 'The best case for a Tier 4 site is two feeds from separate utilities or '
                               'substations, but that is very expensive, so the usual approach is diesel '
                               'generator backup.',
                       'tip': 'The best case for a Tier 4 site is two feeds from separate utilities or '
                              'substations, but that is very expensive, so the usual approach is diesel '
                              'generator backup.',
                       'timestamp': 22,
                       'timestamp_seconds': 22,
                       'timestamp_label': '[00:00:22]',
                       'url': 'https://www.youtube.com/watch?v=QtOyye8fYNk&t=22s',
                       'markdown': '[00:00:22](https://www.youtube.com/watch?v=QtOyye8fYNk&t=22s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'YSqciE_dMbY',
                       'title': 'How Data Center Power Works: From Grid Substation to AI Racks',
                       'channel': 'InfraEnergy Academy',
                       'author': 'InfraEnergy Academy',
                       'text': 'Double the voltage, half the current.',
                       'tip': 'Double the voltage, half the current.',
                       'timestamp': 272,
                       'timestamp_seconds': 272,
                       'timestamp_label': '[00:04:32]',
                       'url': 'https://www.youtube.com/watch?v=YSqciE_dMbY&t=272s',
                       'markdown': '[00:04:32](https://www.youtube.com/watch?v=YSqciE_dMbY&t=272s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'giNYYY0DnJw',
                       'title': "Data Center Power Explained (It's simpler than you think)",
                       'channel': 'Base Config',
                       'author': 'Base Config',
                       'text': 'This eliminates the path failure point.',
                       'tip': 'This eliminates the path failure point.',
                       'timestamp': 129,
                       'timestamp_seconds': 129,
                       'timestamp_label': '[00:02:09]',
                       'url': 'https://www.youtube.com/watch?v=giNYYY0DnJw&t=129s',
                       'markdown': '[00:02:09](https://www.youtube.com/watch?v=giNYYY0DnJw&t=129s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'uEz7S-WjHG0',
                       'title': 'Why AI Data Centers Can Wait Years for One Transformer',
                       'channel': 'Critical Systems Explained',
                       'author': 'Critical Systems Explained',
                       'text': 'Ordering sooner can help, but premature orders can create costly problems '
                               'if final specifications change.',
                       'tip': 'Ordering sooner can help, but premature orders can create costly problems '
                              'if final specifications change.',
                       'timestamp': 538,
                       'timestamp_seconds': 538,
                       'timestamp_label': '[00:08:58]',
                       'url': 'https://www.youtube.com/watch?v=uEz7S-WjHG0&t=538s',
                       'markdown': '[00:08:58](https://www.youtube.com/watch?v=uEz7S-WjHG0&t=538s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'uEz7S-WjHG0',
                       'title': 'Why AI Data Centers Can Wait Years for One Transformer',
                       'channel': 'Critical Systems Explained',
                       'author': 'Critical Systems Explained',
                       'text': 'A manufacturer cannot simply double its output by adding a night shift.',
                       'tip': 'A manufacturer cannot simply double its output by adding a night shift.',
                       'timestamp': 326,
                       'timestamp_seconds': 326,
                       'timestamp_label': '[00:05:26]',
                       'url': 'https://www.youtube.com/watch?v=uEz7S-WjHG0&t=326s',
                       'markdown': '[00:05:26](https://www.youtube.com/watch?v=uEz7S-WjHG0&t=326s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'lFIWqD0EAkM',
                       'title': 'Why Data Centers Are Choosing This Company For Substations | Dan Girard '
                                'at Midwest Solar Expo 2024',
                       'channel': 'REsource Labs',
                       'author': 'REsource Labs',
                       'text': 'We built a substation in Kansas in under six months, where a large firm '
                               'would take a year and a half to two years.',
                       'tip': 'We built a substation in Kansas in under six months, where a large firm '
                              'would take a year and a half to two years.',
                       'timestamp': 208,
                       'timestamp_seconds': 208,
                       'timestamp_label': '[00:03:28]',
                       'url': 'https://www.youtube.com/watch?v=lFIWqD0EAkM&t=208s',
                       'markdown': '[00:03:28](https://www.youtube.com/watch?v=lFIWqD0EAkM&t=208s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'lFIWqD0EAkM',
                       'title': 'Why Data Centers Are Choosing This Company For Substations | Dan Girard '
                                'at Midwest Solar Expo 2024',
                       'channel': 'REsource Labs',
                       'author': 'REsource Labs',
                       'text': 'Design the substation to the 345 kV standard but use 230 kV products, and '
                               'that speeds up the build.',
                       'tip': 'Design the substation to the 345 kV standard but use 230 kV products, and '
                              'that speeds up the build.',
                       'timestamp': 761,
                       'timestamp_seconds': 761,
                       'timestamp_label': '[00:12:41]',
                       'url': 'https://www.youtube.com/watch?v=lFIWqD0EAkM&t=761s',
                       'markdown': '[00:12:41](https://www.youtube.com/watch?v=lFIWqD0EAkM&t=761s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '6_osryMHPf4',
                       'title': 'What is a substation and why is it important for data centers?',
                       'channel': 'Ryne Ogren',
                       'author': 'Ryne Ogren',
                       'text': "They'll give you an approved manufacturer list on these transformers.",
                       'tip': "They'll give you an approved manufacturer list on these transformers.",
                       'timestamp': 259,
                       'timestamp_seconds': 259,
                       'timestamp_label': '[00:04:19]',
                       'url': 'https://www.youtube.com/watch?v=6_osryMHPf4&t=259s',
                       'markdown': '[00:04:19](https://www.youtube.com/watch?v=6_osryMHPf4&t=259s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '7Q-aVBv7PWM',
                       'title': 'How Do Substations Work?',
                       'channel': 'Practical Engineering',
                       'author': 'Practical Engineering',
                       'text': 'At high voltages, even air can act like a conductor, which means even if '
                               'you create a break in a line, electricity can continue flowing in a '
                               'phenomenon known as an arc.',
                       'tip': 'At high voltages, even air can act like a conductor, which means even if '
                              'you create a break in a line, electricity can continue flowing in a '
                              'phenomenon known as an arc.',
                       'timestamp': 211,
                       'timestamp_seconds': 211,
                       'timestamp_label': '[00:03:31]',
                       'url': 'https://www.youtube.com/watch?v=7Q-aVBv7PWM&t=211s',
                       'markdown': '[00:03:31](https://www.youtube.com/watch?v=7Q-aVBv7PWM&t=211s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'u8ABTJm2_XQ',
                       'title': 'Electrical Substation Layout Configurations | Radial, Tapped, LILO & '
                                'Interconnected',
                       'channel': 'Kognito Key',
                       'author': 'Kognito Key',
                       'text': 'The LILO configuration is more secure, but it is quite expensive.',
                       'tip': 'The LILO configuration is more secure, but it is quite expensive.',
                       'timestamp': 165,
                       'timestamp_seconds': 165,
                       'timestamp_label': '[00:02:45]',
                       'url': 'https://www.youtube.com/watch?v=u8ABTJm2_XQ&t=165s',
                       'markdown': '[00:02:45](https://www.youtube.com/watch?v=u8ABTJm2_XQ&t=165s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'zeoe1qgsv2c',
                       'title': 'Substation: 6 Things You Ought To Know',
                       'channel': 'Gokce Capital',
                       'author': 'Gokce Capital',
                       'text': 'In 2020, PNM bought four lots in North Albuquerque Acres, and in 2021 the '
                               'county unanimously denied the special use permit.',
                       'tip': 'In 2020, PNM bought four lots in North Albuquerque Acres, and in 2021 the '
                              'county unanimously denied the special use permit.',
                       'timestamp': 272,
                       'timestamp_seconds': 272,
                       'timestamp_label': '[00:04:32]',
                       'url': 'https://www.youtube.com/watch?v=zeoe1qgsv2c&t=272s',
                       'markdown': '[00:04:32](https://www.youtube.com/watch?v=zeoe1qgsv2c&t=272s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'GAM0L1fXtiA',
                       'title': 'Substation Design | 30–60–90–IFC | Keentel Engineering',
                       'channel': 'Keentel Engineering',
                       'author': 'Keentel Engineering',
                       'text': 'Nothing appears at IFC that has not already been seen and reviewed.',
                       'tip': 'Nothing appears at IFC that has not already been seen and reviewed.',
                       'timestamp': 228,
                       'timestamp_seconds': 228,
                       'timestamp_label': '[00:03:48]',
                       'url': 'https://www.youtube.com/watch?v=GAM0L1fXtiA&t=228s',
                       'markdown': '[00:03:48](https://www.youtube.com/watch?v=GAM0L1fXtiA&t=228s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Kq3m6y4jjFM',
                       'title': 'ECE421 - Lec 13: Transmission Line Parameters; Resistance; Inductance',
                       'channel': 'Kai Sun',
                       'author': 'Kai Sun',
                       'text': 'Underground cables are under 1% of high-voltage transmission, and their '
                               'higher capacitance raises high-voltage concerns.',
                       'tip': 'Underground cables are under 1% of high-voltage transmission, and their '
                              'higher capacitance raises high-voltage concerns.',
                       'timestamp': 131,
                       'timestamp_seconds': 131,
                       'timestamp_label': '[00:02:11]',
                       'url': 'https://www.youtube.com/watch?v=Kq3m6y4jjFM&t=131s',
                       'markdown': '[00:02:11](https://www.youtube.com/watch?v=Kq3m6y4jjFM&t=131s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'}]}
