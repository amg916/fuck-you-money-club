from __future__ import annotations

CHAPTER_3 = {'id': 'Q3',
 'chapter_id': 'Q3',
 'chapter_number': 3,
 'question_number': 3,
 'slug': 'large-load-interconnection-pjm-ercot',
 'question_prompt': 'How do large loads such as data centers get interconnected in PJM and ERCOT, and what '
                    'reliability rules and cost allocation fights come with it?',
 'kicker': 'Q3 / THE BIG MONEY PLAYBOOKS',
 'title': 'Large-Load Interconnection in PJM and ERCOT',
 'subtitle': 'PJM CIFP Stage 4 rules, ERCOT large load working group and Batch Zero workshops, the 3,800 '
             "MW ride-through event, NERC compliance for large loads, who pays when data centers can't "
             'connect, ratepayer bill impacts, and ERCOT–PJM leadership perspectives',
 'layout_template': 'financial_analysis',
 'reading_time_minutes': 15,
 'executive_summary': 'Practitioners across PJM and ERCOT agree the large-load queue is mostly paper: '
                      "ERCOT's queue hit 438,000 MW of load requests through 2032, its forecasters cut 218 "
                      'GW of letters, contracts and third-party forecasts to 148 GW by about 2032, and '
                      "Dominion's zone shows 70 GW of requests against a 24 GW peak. The street mechanics "
                      'run on cash and lock-in. ERCOT Batch Zero demands site control, duplicate-request '
                      'disclosure and $50,000/MW security, then freezes megawatts at a single 30-day '
                      "commitment window; PJM's Expedited Interconnection Track wants more than 250 MW of "
                      'UCAP and a $10,000-$20,000/MW non-refundable deposit. High-voltage breaker lead '
                      'times stretched from 77 to 125 weeks. The fights center on the 3-month refinement '
                      "back end, the six-year 2033 allocation 'blank check' and a six-month look-back one "
                      'stakeholder called draconian.',
 'key_metrics': [{'label': 'ERCOT Batch Zero Entry Security',
                  'metric': 'ERCOT Batch Zero Entry Security',
                  'value': '$50,000/MW posted with TDSP submission by July 10',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Entry kit for loads above 75 MW alongside site control, duplicate-request '
                             'disclosure, and regulatory-approval and engineering documents.',
                  'source': 'WhyPKD ([EvpNriZrrME @ 00:02:47])'},
                 {'label': 'PJM Expedited Interconnection Track Deposit',
                  'metric': 'PJM Expedited Interconnection Track Deposit',
                  'value': '$10,000-$20,000/MW non-refundable; more than 250 MW UCAP; 10 projects per year',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'EIT launches mid-2026 targeting 10 months to an agreement, with no changes '
                             'to site, fuel or MW after filing.',
                  'source': 'Keentel Engineering ([C9tZQM-x_Ho @ 00:02:58])'},
                 {'label': 'ERCOT Adjusted Large-Load Forecast',
                  'metric': 'ERCOT Adjusted Large-Load Forecast',
                  'value': '218 GW submitted, adjusted to 148 GW by about 2032',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'TSP letters, contracts and third-party forecasts haircut using historical '
                             'energization delays, as of July 2025.',
                  'source': 'Data Centers Technical Info ([S8vmSHwFrvE @ 00:04:08])'},
                 {'label': 'High-Voltage Breaker Lead Time',
                  'metric': 'High-Voltage Breaker Lead Time',
                  'value': '77 weeks in 2023 to 125 weeks',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Wood Mackenzie figures cited alongside generator step-up transformers '
                             'exceeding 160 weeks, up from 143 in 2024.',
                  'source': 'Profound Studies ([dMPUECoTe2M @ 00:01:40])'}],
 'sections': [{'heading': 'The Practitioner Consensus: The Queue Is Paper, and Capital Plus Hardware '
                          'Decide Who Connects',
               'paragraphs': ['Every operator who touched the numbers says the same thing first: the queue '
                              'is not the load. WhyPKD opens on 438,000 MW of loads seeking ERCOT '
                              "interconnection through 2032 and says such numbers 'live in what I call "
                              "stupid land,' with much of it speculative and a supply chain nowhere near "
                              'able to build it [EvpNriZrrME @ 00:00:02]. The ERCOT-side presenter on Data '
                              'Centers Technical Info walked through the haircut: TSP letters, signed '
                              'contracts and third-party forecasts summed to 218 GW, and ERCOT filed an '
                              'adjusted forecast of 148 GW for around 2032 by applying historical '
                              "energization delays [S8vmSHwFrvE @ 00:04:08]. On the PJM side, Virginia's "
                              "Chief Energy Officer on Texas Energy & Power put Dominion's zone at 70 GW "
                              'of large-load requests against a 24 GW peak, agreed with the market '
                              "monitor's 'fantasy' label, and blamed 'phantom load' on PJM not vetting "
                              'utility supplemental forecasts, adding that building 45 GW is impossible '
                              "[nzC-XREeuz4 @ 00:11:32]. Sarthak compresses it into two lines: 'A queue is "
                              "not a forecast' and 'Proposed is not connected,' because speculative and "
                              'duplicate requests stack up while real loads ramp in gradually [u0kuoKQbHTs '
                              '@ 00:01:39]. The read for a site optioner is blunt: a queue position or a '
                              'utility letter is a claim, not headroom, and both grid operators now '
                              'discount it before it ever reaches a planning case.',
                              'The second point of agreement is that capital and paperwork now gate the '
                              "line. Under ERCOT's Batch Zero, WhyPKD lists the entry kit for loads above "
                              '75 MW: submit to the TDSP by July 10, show site control by lease or '
                              'ownership, disclose every other interconnection request to kill double '
                              'counting, hand over regulatory-approval and engineering documents, and post '
                              '$50,000/MW of security [EvpNriZrrME @ 00:02:47]. At the interconnection '
                              'agreement a non-refundable $50,000/MW of peak demand is due and 100% of '
                              'direct CIAC is paid at signing, with no utility allowance, no rate-base '
                              "recovery and no upgrade work until CIAC lands, so 'only truly capitalized "
                              "projects can move forward' [EvpNriZrrME @ 00:05:03]. Keentel Engineering's "
                              'PJM breakdown mirrors it: the Expedited Interconnection Track wants more '
                              "than 250 MW of UCAP, 'not nameplate,' a non-refundable $10,000-$20,000/MW "
                              'deposit, a cap of 10 projects per year, and no changes to site, fuel or MW '
                              'after filing, with duplicate-request disclosure and milestone criteria '
                              'already on the board [C9tZQM-x_Ho @ 00:02:58]. Beyound The Signal frames '
                              'the principle both markets are converging on: the customer that causes the '
                              "upgrade should pay for the generation and wires built for it, and 'a "
                              "connection offer should not be a free option on the public network' "
                              '[Lh1aLCJikCo @ 00:07:04]. Cash at risk is the new proof of realness.',
                              "Third, every speaker agrees the binding constraint is physical time. PJM's "
                              'Manu Asthana put it as 18 months to build a data center against 5-7 years '
                              'for a combined cycle, with 30 of the 32 GW of PJM peak growth expected by '
                              '2030 coming from data centers [a34rwkck9IA @ 00:07:09]. Profound Studies, '
                              'citing Wood Mackenzie, reports generator step-up transformers past 160 '
                              'weeks and high-voltage breakers jumping from 77 weeks in 2023 to 125 weeks, '
                              "adding that 'equipment is getting slower and more expensive at the same "
                              "time' [dMPUECoTe2M @ 00:01:40]. Ben Watkins of ARM Group on The Clean "
                              'Energy Edge Podcast says equipment is now chosen on timeline rather than '
                              'optimality: if gear A takes 5 years and gear B arrives within a year, you '
                              "take B, or the project 'is going in the trash' [kHFYcexB2dU @ 00:09:25]. "
                              "Keentel's load-event breakdown adds the behavioral layer every planner now "
                              'watches: in Northern Virginia a 230 kV fault cleared in 50-80 ms still sent '
                              '3,800 MW to backup generation, because upstream protection, ATS and UPS '
                              'logic made the disconnect call even though the IT equipment could have '
                              'tolerated the sag [WN6PtJ3kQDQ @ 00:02:11]. The baseline is therefore '
                              'twofold: lock long-lead gear on delivery weeks, and prove how the campus '
                              'behaves under faults before the grid operator has to guess.'],
               'table': {'caption': 'Where PJM and ERCOT practitioners agree on large-load interconnection',
                         'headers': ['Consensus Point',
                                     'What the Practitioner Reported',
                                     'Operator Implication',
                                     'Expert Source'],
                         'rows': [['Queue volume is mostly speculative paper load',
                                   '438,000 MW of loads seek ERCOT interconnection through 2032, much of '
                                   'it speculative',
                                   'Treat queue totals as noise and never as available substation headroom',
                                   'WhyPKD ([EvpNriZrrME @ 00:00:02])'],
                                  ['Grid operators haircut load forecasts using delay history',
                                   'ERCOT cut 218 GW of letters, contracts and forecasts to 148 GW by '
                                   'about 2032',
                                   'Expect contracted megawatts to be discounted before any planning case '
                                   'counts them',
                                   'Data Centers Technical Info ([S8vmSHwFrvE @ 00:04:08])'],
                                  ['A signed utility contract does not equal counted megawatts',
                                   'PJM counts 100% in earliest years, about 40% in middle years, about '
                                   '33% later',
                                   'Override the discount with milestones, ramp data, utilization evidence '
                                   'and duplication disclosure',
                                   'Keentel Engineering ([C9tZQM-x_Ho @ 00:04:05])'],
                                  ['Site control and duplicate disclosure are the entry ticket',
                                   'Batch Zero requires lease or ownership proof and disclosure of all '
                                   'other interconnection requests',
                                   'Lock land control and clean up parallel requests before the TDSP '
                                   'filing date',
                                   'WhyPKD ([EvpNriZrrME @ 00:02:47])'],
                                  ['The customer causing the upgrade pays for the wires',
                                   'A connection offer should not be a free option on the public network',
                                   'Budget full upgrade exposure instead of assuming ratepayers absorb the '
                                   'wires',
                                   'Beyound The Signal ([Lh1aLCJikCo @ 00:07:04])'],
                                  ['Long-lead equipment sets the real energization calendar',
                                   'High-voltage breakers moved from 77 weeks in 2023 to 125 weeks last '
                                   'year',
                                   'Plan site timelines around transformer and breaker delivery weeks, not '
                                   'study dates',
                                   'Profound Studies ([dMPUECoTe2M @ 00:01:40])'],
                                  ['Data centers build far faster than grid supply arrives',
                                   'A data center takes 18 months while a combined cycle takes 5-7 years',
                                   'Expect grid supply, not building construction, to define your '
                                   'energization date',
                                   'ERCOTISO ([a34rwkck9IA @ 00:07:09])']]}},
              {'heading': 'Exact Street Mechanics, Tools & Numbers: Batch Clocks, Look-Backs, Deposits and '
                          'Ride-Through',
               'paragraphs': ["ERCOT's Batch Zero runs on a hard calendar, and the clock is the product. "
                              'AG Springer of ERCOT laid out the batch at the February 26, 2026 workshop: '
                              'a six-month cadence, an initial steady-state study of roughly 4.5 months '
                              'plus stability screening, a 30-day commitment window, a roughly 3-month '
                              'refinement study, a three-week RPG comment period, then TAC and Board, for '
                              '9-10 months end to end [9zpO8wwsfXc @ 00:18:27]. The study grid covers '
                              '2028-2032 with three cases per year (summer peak, peak net load as the '
                              'no-solar case, and fall peak), generation added per PGRR 127, and any '
                              'megawatts that cannot be served pushed into a 2033 allocation [9zpO8wwsfXc '
                              '@ 00:20:54]. The commitment point is a one-way door: megawatts and '
                              'financial commitment lock there, with no second decision point, '
                              "specifically to avoid an 'infinite restudy loop' [9zpO8wwsfXc @ 00:55:06]. "
                              'WhyPKD gives the downstream sequence from the PGRR 145 proposal: ERCOT '
                              'delivers results by January 29 with annual allocations through 2032, '
                              'required upgrades and CIAC costs, ILLEs accept on March 1, a refinement '
                              'study follows in June, and projects that miss milestones lose capacity '
                              '[EvpNriZrrME @ 00:03:20]. Size the request at the commitment window as if '
                              'it were the final number, because under this design it is, and the only '
                              'variable still moving in the refinement window is the transmission.',
                              "The gating flowchart ERCOT's Jeff Bilow presented decides whether an "
                              'existing position is treated as baseload or thrown back into the pot. Loads '
                              'energizing by the end of 2027 must prove development activity; those that '
                              'cannot get their studies invalidated, their energization date '
                              'administratively set to 01/01/2028, and their megawatts reallocated '
                              '[9zpO8wwsfXc @ 02:18:48]. Development activity means inclusion in the '
                              '05/01/2026 QSA, or site preparation or construction plus purchase of the '
                              "high-voltage transformers and breakers, and ERCOT warned that 'clever "
                              "people' are already trying to slip into the QSA without meeting the other "
                              'requirements [9zpO8wwsfXc @ 02:34:36]. Operating loads face a six-month '
                              'look-back, a June 1 snapshot reaching back to December 1, where a 500 MW '
                              'load observed at 300 MW frees 200 MW for reallocation; an updated ramp '
                              "schedule keeps the 500 MW as a one-time true-up that ERCOT staff called 'a "
                              "free option to update your ramp schedule' [9zpO8wwsfXc @ 04:51:39]. A study "
                              'only counts as valid with a complete dynamic model plus the DWG large load '
                              'survey, and the Data Centers Technical Info presenter notes ERCOT approvals '
                              'come back zero, partial or full across steady-state, short-circuit and '
                              'dynamics work [S8vmSHwFrvE @ 00:08:36]. Model quality is now a gating '
                              'asset.',
                              'On the PJM side, Keentel Engineering breaks the CIFP large-load rules into '
                              'three paths: bring your own generation matched on UCAP, demand response, or '
                              'non-capacity-backed load that serves only as a bridge during supply '
                              'shortfall with no capacity charges. The paths are not mutually exclusive, '
                              'so the play is to enter on path 3 and migrate to path 1 [C9tZQM-x_Ho @ '
                              '00:02:08]. Because UCAP derates by outage history, the same channel says '
                              'you need more nameplate than peak load, and co-location is not required '
                              "since ownership or a PPA works [C9tZQM-x_Ho @ 00:06:52]. PJM's Jason "
                              'Connell says the FERC show-cause response combines generation '
                              "interconnection and large-load transmission service into 'one single "
                              "cluster,' targeting an efficient transmission plan in under 12 months with "
                              "a November filing [DU-7TmjHp7c @ 00:00:47]. Inside the fence, Keentel's "
                              '3,800 MW event breakdown gives the engineering fix: start the generators '
                              'but delay transfer until the ride-through window expires, stagger campus '
                              'timing, verify the loaded settings, add power-quality recording at the '
                              'point of service, include sags in IST and retest after changes, because '
                              "'ride through is cheapest to engineer before equipment is purchased and "
                              "installed' [WN6PtJ3kQDQ @ 00:13:03]. Path choice and transfer logic are "
                              'both decided early or paid for later.'],
               'table': {'caption': 'Exact large-load interconnection numbers operators are working '
                                    'against in ERCOT and PJM',
                         'headers': ['Mechanic',
                                     'Exact Number or Rule',
                                     'How Operators Use It',
                                     'Expert Source'],
                         'rows': [['ERCOT Batch Zero entry security posting',
                                   '$50,000/MW posted with TDSP submission by July 10 for loads above 75 '
                                   'MW',
                                   'Fund security before filing because it screens out uncapitalized '
                                   'competing requests',
                                   'WhyPKD ([EvpNriZrrME @ 00:02:47])'],
                                  ['ERCOT interconnection agreement fee and CIAC',
                                   'Non-refundable $50,000/MW of peak demand plus 100% of direct CIAC at '
                                   'signing',
                                   'Hold CIAC cash at signing since no upgrade work starts until paid',
                                   'WhyPKD ([EvpNriZrrME @ 00:04:11])'],
                                  ['PJM Expedited Interconnection Track deposit and cap',
                                   '$10,000-$20,000/MW non-refundable, more than 250 MW UCAP, 10 projects '
                                   'per year',
                                   'Freeze site, fuel and MW before filing because changes are barred '
                                   'afterward',
                                   'Keentel Engineering ([C9tZQM-x_Ho @ 00:02:58])'],
                                  ['ERCOT batch cycle timing and commitment window',
                                   '30-day commitment window, about 3-month refinement, 9-10 months total '
                                   'per batch',
                                   'Decide final megawatts inside thirty days because no second decision '
                                   'point exists',
                                   'James Dickey ([9zpO8wwsfXc @ 00:18:27])'],
                                  ['ERCOT six-month look-back on operating loads',
                                   'A 500 MW load observed at 300 MW frees 200 MW for reallocation',
                                   'File an updated ramp schedule as a one-time true-up to keep megawatts',
                                   'James Dickey ([9zpO8wwsfXc @ 02:23:27])'],
                                  ['ERCOT development activity proof for 2027 energization',
                                   '05/01/2026 QSA inclusion, or site prep plus purchased high-voltage '
                                   'transformers and breakers',
                                   'Buy high-voltage gear early to avoid the administrative 01/01/2028 '
                                   'reset',
                                   'James Dickey ([9zpO8wwsfXc @ 02:34:36])'],
                                  ['NERC Category 2 registration threshold for added capacity',
                                   '20 MVA and 60 kV; 18 MVA plus a 4 MVA battery equals 22 MVA',
                                   'Check registration status before bolting on storage because status '
                                   'changes overnight',
                                   'Keentel Engineering ([f1C-d4m7OHg @ 00:03:20])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Insider Pro-Tips from the Interconnection Floor',
                           'body': 'The edge goes to operators who sequence paths, defend their counted '
                                   'megawatts, and buy equipment on delivery timelines rather than '
                                   'spec-sheet preference.',
                           'items': ['Sequence PJM paths instead of picking one: enter as '
                                     'non-capacity-backed load that accepts pre-emergency curtailment, '
                                     "then migrate to bring-your-own-generation, because 'Strategy is "
                                     "about sequencing, not just selecting.' [Keentel Engineering — "
                                     'C9tZQM-x_Ho @ 00:05:42]',
                                     "Beat PJM's forecast discount of about 40% in middle years and about "
                                     '33% in later years by filing milestones, ramp data, utilization '
                                     'evidence and duplication disclosure, since a signed utility contract '
                                     'does not mean the MW are counted. [Keentel Engineering — C9tZQM-x_Ho '
                                     '@ 00:04:21]',
                                     "If ERCOT's six-month look-back is about to haircut an operating "
                                     'load, file an updated ramp schedule: the 500 MW promise survives as '
                                     "a one-time true-up, described at the workshop as 'a free option to "
                                     "update your ramp schedule.' [James Dickey — 9zpO8wwsfXc @ 04:51:39]",
                                     'Pick equipment on delivery timeline, not optimality: if gear A is 5 '
                                     'years out and gear B lands within a year, take B, and bring the '
                                     'engineer in as soon as possible for site feasibility, critical-issue '
                                     'studies and desktop reviews. [The Clean Energy Edge Podcast — '
                                     'kHFYcexB2dU @ 00:09:25]']},
               'sop_steps': [{'step': 1,
                              'title': 'Lock Land and Clean the Request Stack',
                              'action': 'Secure lease or ownership site control and disclose every '
                                        'parallel interconnection request before the TDSP filing.',
                              'detail': 'Batch Zero entry requires site control by lease or ownership, '
                                        'disclosure of other interconnection requests to avoid double '
                                        'counting, regulatory-approval and engineering documents, and '
                                        '$50,000/MW security submitted to the TDSP by July 10 [WhyPKD — '
                                        'EvpNriZrrME @ 00:02:47]; in PJM, duplication disclosure is one of '
                                        'the levers that overrides forecast discounting [Keentel '
                                        'Engineering — C9tZQM-x_Ho @ 00:04:21].'},
                             {'step': 2,
                              'title': 'Prove Development Activity Before the Cutoff',
                              'action': 'Get into the 05/01/2026 QSA or show site preparation plus '
                                        'purchased high-voltage transformers and breakers.',
                              'detail': 'Loads energizing by end of 2027 that cannot show development '
                                        'activity get studies invalidated, energization set to 01/01/2028 '
                                        'and megawatts reallocated [James Dickey — 9zpO8wwsfXc @ '
                                        '02:18:48]; qualifying activity is QSA inclusion or site '
                                        'preparation or construction plus purchase of high-voltage '
                                        'transformers and breakers [James Dickey — 9zpO8wwsfXc @ '
                                        '02:34:36].'},
                             {'step': 3,
                              'title': 'Size the Commitment as Final',
                              'action': 'Fix your megawatts and line up funding inside the 30-day '
                                        'commitment window.',
                              'detail': 'Megawatts and financial commitment lock at the commitment point '
                                        'with no second decision point [James Dickey — 9zpO8wwsfXc @ '
                                        '00:55:06]; at the agreement, $50,000/MW of peak demand is '
                                        'non-refundable and 100% of direct CIAC is due at signing, with no '
                                        'upgrade work until CIAC is paid [WhyPKD — EvpNriZrrME @ '
                                        '00:04:11].'},
                             {'step': 4,
                              'title': 'Engineer Models and Ride-Through Up Front',
                              'action': 'Deliver a complete dynamic model and DWG survey, and design '
                                        'transfer logic that rides through faults.',
                              'detail': 'A valid ERCOT study requires a complete dynamic model plus the '
                                        'DWG large load survey [James Dickey — 9zpO8wwsfXc @ 02:32:00]; on '
                                        'the campus side, start generators but delay transfer until the '
                                        'ride-through window expires, add point-of-service power-quality '
                                        'recording, include sags in IST and retest after changes [Keentel '
                                        'Engineering — WN6PtJ3kQDQ @ 00:17:19].'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ["ERCOT's Batch Zero design locks megawatts and financial commitment at one "
                              "commitment point, and ERCOT's AG Springer defends the single lock as the "
                              "only exit from an 'infinite restudy loop' [9zpO8wwsfXc @ 00:55:06]. "
                              "Google's Chris Mattis and Skybox back that single decision point. NRG's "
                              "Bill Barnes calls the three-month back end a 'fatal flaw': a breaker with a "
                              'three-year lead time can leave only 150 of 1,000 MW flowing until the '
                              'upgrade lands, and when Barnes pressed on who pays for megawatts pushed '
                              "into the 2033 bucket, ERCOT replied 'I don't have an answer' [9zpO8wwsfXc @ "
                              "00:44:13]. Lancium's Evan Neal labels the year-six allocation a 'six year "
                              "blank check,' and Sam Brandon of Agentek warns that tying security to the "
                              "refinement study breeds cluster 'doom loops.' Oxy's Jamil Pueblos calls the "
                              '30-day commitment window tight, and Matt Marinis answers that 60 days would '
                              'shift the whole timeline by about a month. WhyPKD treats the hard entry bar '
                              'as the feature: site control, disclosure of every other interconnection '
                              "request, $50,000/MW security and 100% of direct CIAC at signing mean 'only "
                              'truly capitalized projects can move forward and other rate payers are '
                              "protected' [EvpNriZrrME @ 00:05:03]. The same narrator still says utilities "
                              "have been 'making this up as they go along' [EvpNriZrrME @ 00:06:06], and "
                              'ERCOT staff concede they are building the plane while flying it.',
                              'In PJM, the split is over whether a large load should ride the network or '
                              'route around it. Keentel Engineering says PJM prefers full network-load '
                              'integration, counted in the forecast and RPM and curtailed only in '
                              'emergencies, while islanded options stay invisible to planning, need '
                              'complex relays and get weaker curtailment protection; their play is to '
                              'treat the three paths as sequencing tools, entering as non-capacity-backed '
                              'load and migrating to bring-your-own generation [C9tZQM-x_Ho @ 00:02:41]. '
                              "Profound Studies reports FERC largely rejected PJM's "
                              'bring-your-own-new-capacity and curtailable plan on October 9 as intruding '
                              'on states and discriminating, while approving the large-load definition and '
                              "registry [dMPUECoTe2M @ 00:02:30]. Virginia's Chief Energy Officer, on "
                              "Texas Energy & Power, reads PJM's white-paper options harshly: bilateral "
                              'contracts are risk-shifting, differential reliability means Virginia loads '
                              'get curtailed more, and an ERCOT-like structure favors solar and storage '
                              '[nzC-XREeuz4 @ 00:19:14]. ERCOT draws its own BYOG line: AG Springer says '
                              'unsynchronized backup generation is not BYOG, a battery-plus-load CLR is a '
                              "'much heavier lift,' and no CLR planning credit flows until the operational "
                              "gaps close [9zpO8wwsfXc @ 03:59:09]. NRG's Bill Barnes still pushes ERCOT "
                              'to prioritize BYOG Scenario 3, while Matt Marinis floats NPRR 1206 '
                              'self-limiting logic for co-located sites.',
                              "Load flexibility is the sharpest philosophical split. PJM's Manu Asthana "
                              'wants demand response to grow from the roughly 8 GW in the control room '
                              'today to 20 GW, and names data-center backup diesels as one market-based '
                              'source [a34rwkck9IA @ 00:17:00]. Sarthak pushes back on the hype: Ember '
                              'puts only about 3% of modeled 2030 capacity as shiftable, inference demands '
                              "an instant answer while training can move, and flexibility 'is certainly "
                              "not a magic substitute for building actual grid capacity' [u0kuoKQbHTs @ "
                              '00:05:06]. Ben Watkins of ARM Group, on The Clean Energy Edge Podcast, '
                              'describes training loads swinging from 20% to 80% of peak within about 50 '
                              'milliseconds, with 30-40 MW jumping to 150 MW; inference use does '
                              'stabilize, per Watkins, and the host argues batteries respond '
                              'instantaneously [kHFYcexB2dU @ 00:02:11]. The ERCOT presenter on Data '
                              'Centers Technical Info adds a cost the flexibility camp skips: rapid '
                              "fluctuation can wear out the load's own equipment, so on-site storage "
                              'becomes the alternative [S8vmSHwFrvE @ 00:15:14]. Keentel Engineering notes '
                              "data centers are only about 3% of PJM's demand-response capacity today, and "
                              'on the ERCOT side Sam Brandon warns that unmitigated CLRs bidding $5,000 '
                              'around the clock could push SCED into violating limits, so Brandon proposes '
                              'reusing NPRR 1255 just-in-time mitigation.'],
               'table': {'caption': 'Contested playbooks for large-load interconnection in ERCOT and PJM',
                         'headers': ['Fault Line', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Batch Zero single commitment point versus restudy flexibility',
                                   'ERCOT, Google and Skybox lock megawatts and money at commitment to '
                                   'avoid an infinite restudy loop',
                                   'Bill Barnes calls the three-month back end a fatal flaw when breakers '
                                   'take three years',
                                   'James Dickey ([9zpO8wwsfXc @ 00:55:06]); James Dickey ([9zpO8wwsfXc @ '
                                   '00:44:13])'],
                                  ['Length of the Batch Zero commitment window for loads',
                                   'A 30-day commitment window keeps the nine-to-ten month batch clock '
                                   'intact',
                                   "Oxy's Jamil Pueblos calls 30 days tight; Marinis says 60 days shifts "
                                   'the timeline about a month',
                                   'James Dickey ([9zpO8wwsfXc @ 01:54:36])'],
                                  ['How much money goes at risk before study results arrive',
                                   'Eric Goff, for three hyperscalers, accepts the $100k/MW fee with a '
                                   'per-site cap and increasingly nonrefundable collateral',
                                   'Prashanth of Black Mountain wants the $100k/MW moved post-study and an '
                                   '$8-10k/MW filing fee instead',
                                   'James Dickey ([9zpO8wwsfXc @ 02:44:27]); James Dickey ([9zpO8wwsfXc @ '
                                   '04:16:38])'],
                                  ['PJM network load versus islanded behind-the-meter configuration',
                                   'Be a full network load counted in the forecast and RPM, curtailed only '
                                   'in emergencies',
                                   'Islanded options are invisible to planning, need complex relays and '
                                   'get weaker curtailment protection',
                                   'Keentel Engineering ([C9tZQM-x_Ho @ 00:01:23])'],
                                  ['Bring your own capacity as the PJM entry ticket',
                                   'UCAP-matched own generation earns residential-like treatment; enter '
                                   'non-capacity-backed and migrate later',
                                   "FERC largely rejected PJM's bring-your-own-new-capacity and "
                                   'curtailable plan as intruding on states and discriminating',
                                   'Keentel Engineering ([C9tZQM-x_Ho @ 00:02:08]); Profound Studies '
                                   '([dMPUECoTe2M @ 00:02:30])'],
                                  ['Six-month look-back reallocation of unused megawatts',
                                   'A 500 MW load observed at 300 MW frees 200 MW; updating the ramp is a '
                                   'free one-time option',
                                   'Haynes Trader calls the look-back draconian; designed 100 MW sites '
                                   'observe only 70-80 MW',
                                   'James Dickey ([9zpO8wwsfXc @ 02:23:27]); James Dickey ([9zpO8wwsfXc @ '
                                   '04:21:16])'],
                                  ['Data-center flexibility as a substitute for new grid capacity',
                                   'Asthana grows demand response from 8 GW to 20 GW, with data-center '
                                   'backup diesels as a source',
                                   'Sarthak says about 3% is shiftable, inference is inflexible, and '
                                   'flexibility is no magic substitute',
                                   'ERCOTISO ([a34rwkck9IA @ 00:16:17]); Sarthak ([u0kuoKQbHTs @ '
                                   '00:04:11])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The most expensive failure on record is a ride-through failure, not a '
                              'capacity shortfall. Keentel Engineering walks through the July 22, 2026 '
                              'Northern Virginia event: a 230 kV fault cleared in 50-80 ms, the 3-5 cycle '
                              'sag sat inside IT equipment tolerance, yet upstream devices pulled 3,800 MW '
                              'onto backup generation in two waves, 2,970 MW on undervoltage and then '
                              '1,099 MW on the overvoltage that followed [WN6PtJ3kQDQ @ 00:05:02]. Their '
                              'fix is blunt: start generators but delay transfer until the ride-through '
                              'window expires, stagger campus timing, verify the settings actually loaded, '
                              'and retest after every change [WN6PtJ3kQDQ @ 00:13:03]. The ERCOT presenter '
                              'on Data Centers Technical Info reports over a dozen events in a single year '
                              'where hundreds of megawatts unexpectedly left the grid, and warns that a '
                              'UPS switchover reads as ride-through to the facility operator even though '
                              "the load has left the grid [S8vmSHwFrvE @ 00:21:27]. PJM's Manu Asthana "
                              'cites a NERC report on roughly 1,500 MW tripping on a small frequency '
                              'disturbance and says operators now need tail room, not just headroom '
                              '[a34rwkck9IA @ 00:23:47]. Keentel adds that cooling VFD DC-bus trips break '
                              'thermal ride-through and that restart inrush can exceed six times full-load '
                              'current, and compares the situation to IBR settings in the 2010s, when '
                              'retrofits after commissioning proved costly.',
                              'Equipment lead time is where batch clocks and real projects collide. '
                              'Profound Studies, citing Wood Mackenzie, puts generator step-up '
                              'transformers past 160 weeks, up from 143 in 2024, and high-voltage breakers '
                              'at 125 weeks versus 77 in 2023, with prices expected up another 4-10% '
                              '[dMPUECoTe2M @ 00:01:40]. Ben Watkins says equipment is now chosen on '
                              'timeline rather than optimality: if equipment A takes five years and B '
                              'ships within a year, teams take B, and if neither is available the project '
                              "'is going in the trash' [kHFYcexB2dU @ 00:09:25]. ERCOT turns that into a "
                              "gate. Jeff Bilow's flowchart says loads energizing by end of 2027 that "
                              'cannot show development activity get their studies invalidated, their '
                              'energization date administratively set to 01/01/2028, and their megawatts '
                              'reallocated [9zpO8wwsfXc @ 02:18:48]; development activity means site prep '
                              'or construction plus purchased high-voltage transformers and breakers, and '
                              'ERCOT says clever people have already tried to get into the QSA without '
                              'meeting the other requirements. Prashanth of Black Mountain puts a number '
                              "on the exposure under the 9.5 process: 'we are exposed to fifty, sixty "
                              "million depending on the location of the project' [9zpO8wwsfXc @ 04:15:36], "
                              'which is why that developer wants the $100k/MW moved post-study.',
                              "The paperwork traps are quieter but just as costly. Keentel Engineering's "
                              'NERC team warns that a modest capacity addition changes regulatory status '
                              'overnight: an 18 MVA site plus a 4 MVA battery hits 22 MVA, crossing the 20 '
                              'MVA and 60 kV Category 2 registration line [f1C-d4m7OHg @ 00:03:20]. They '
                              'add that a 4-second SCADA historian misses a 200 ms dip while PRC-030 '
                              'triggers at 20 MW and 10% within 4 seconds, and that most audit findings '
                              'are evidence failures, not engineering failures [f1C-d4m7OHg @ 00:08:11]. '
                              'On the PJM forecast side, a signed utility contract does not mean the '
                              'megawatts are counted; discounting falls to about 40% in middle years and '
                              'about 33% later, and UCAP derates by outage history, so nameplate has to '
                              "exceed peak load [C9tZQM-x_Ho @ 00:04:05]. Virginia's Chief Energy Officer "
                              'flags a cost trap that survives self-supply: large loads pay 60% of minimum '
                              'generation for 14 years even if they acquire their own capacity, '
                              'effectively around 160% [nzC-XREeuz4 @ 00:16:43]. The same guest backs the '
                              "market monitor calling Dominion's 70 GW of large-load requests against a 24 "
                              "GW peak 'fantasy,' the phantom load that slips through because PJM does not "
                              'vet utility supplemental forecasts.'],
               'table': {'caption': 'Firsthand traps and the economics checks practitioners attach to them',
                         'headers': ['Trap',
                                     'What Happened Or Was Measured',
                                     'Economics Check',
                                     'Expert Source'],
                         'rows': [['Upstream protection devices disconnecting a load that never lost power',
                                   'A 230 kV fault cleared in 50-80 ms, yet 3,800 MW transferred to backup '
                                   'generation',
                                   'Ride-through is cheapest to engineer before equipment is purchased and '
                                   'installed; retrofits cost more',
                                   'Keentel Engineering ([WN6PtJ3kQDQ @ 00:16:26])'],
                                  ['Cooling plant dropping out during a voltage sag',
                                   'VFD DC-bus trips break thermal ride-through on the cooling system',
                                   'Restart inrush on cooling equipment can exceed six times full-load '
                                   'current',
                                   'Keentel Engineering ([WN6PtJ3kQDQ @ 00:09:13])'],
                                  ['Treating a signed utility contract as counted PJM megawatts',
                                   'A signed contract does not mean PJM counts the load in its forecast',
                                   'Discount runs about 40% in middle years and 33% later unless '
                                   'milestones and ramp data override it',
                                   'Keentel Engineering ([C9tZQM-x_Ho @ 00:04:21])'],
                                  ['Capacity-cost exposure in a short PJM auction',
                                   'The 2028 auction cleared at the $325/MW-day cap, 6.8 GW short, with '
                                   'only 525 MW new supply',
                                   'PJM put the capped bill at $16.4 billion against $29.7 billion '
                                   'uncapped',
                                   'Profound Studies ([dMPUECoTe2M @ 00:01:20])'],
                                  ['Assuming the public network absorbs the cost of connection',
                                   'The PJM market monitor ties $29.4B of capacity charges, about 46.2%, '
                                   'to data centers',
                                   "Ofgem's proposed fee runs 237,500 to 712,500 pounds per MW, or "
                                   '23.8-71.3 million pounds for 100 MW',
                                   'Beyound The Signal ([Lh1aLCJikCo @ 00:04:44])'],
                                  ['Capacity price passing straight into household bills',
                                   'The PJM capacity price went from $28.92/MW-day in 2024-25 to $329.17 '
                                   'in 2026-27',
                                   'Data centers caused about $6.5B, roughly 40% of a $16.4B increase in '
                                   '2026-27',
                                   'Techdamentals ([u6jr6SB0bD4 @ 00:05:26])'],
                                  ['Mistaking a queue position for an energized power supply',
                                   'Projects from 2018-2023 took a median five years and only 19% were '
                                   'built by late 2023',
                                   'Data centers build in one to two years, so plants and wires lag the '
                                   'load they serve',
                                   'Techdamentals ([u6jr6SB0bD4 @ 00:03:30])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Four gates practitioners say kill or strand a large-load project',
                           'body': 'Each gate below comes from a failure, reallocation, or cost shock '
                                   'practitioners reported on the record. Clear all four before committing '
                                   'capital to an ERCOT batch or a PJM expedited filing.',
                           'items': ['Program backup generators to start but delay transfer until the '
                                     'ride-through window expires, then verify loaded settings, record '
                                     'power quality at the point of service, and include sags in IST '
                                     '[Keentel Engineering — WN6PtJ3kQDQ @ 00:13:03].',
                                     'Buy the high-voltage transformers and breakers and begin site prep, '
                                     'or ERCOT invalidates the study, resets energization to 01/01/2028, '
                                     'and reallocates the megawatts [James Dickey — 9zpO8wwsfXc @ '
                                     '02:34:36].',
                                     'Recount registration before adding a battery: 18 MVA plus 4 MVA '
                                     'equals 22 MVA and crosses the 20 MVA and 60 kV Category 2 threshold '
                                     '[Keentel Engineering — f1C-d4m7OHg @ 00:03:20].',
                                     'Size the PJM expedited filing in UCAP, not nameplate: more than 250 '
                                     'MW UCAP, a $10,000-$20,000/MW non-refundable deposit, and no site, '
                                     'fuel, or MW changes after filing [Keentel Engineering — C9tZQM-x_Ho '
                                     '@ 00:02:58].']}}],
 'pull_quote': "'Ride through is cheapest to engineer before equipment is purchased and installed.' — "
               'Keentel Engineering (WN6PtJ3kQDQ @ 00:16:26).',
 'diagram_id': 'diag-03',
 'action_checklist': ['Submit to the TDSP with site control, disclosure of every other interconnection '
                      'request, regulatory and engineering documents, and $50,000/MW security [WhyPKD — '
                      'EvpNriZrrME @ 00:02:47].',
                      'Deliver a complete dynamic model plus the DWG large load survey so the study counts '
                      'as valid for Batch Zero [James Dickey — 9zpO8wwsfXc @ 02:32:00].',
                      'Treat the PJM forecast as a deliverable and override discounting with milestones, '
                      'ramp data, utilization evidence, and duplication disclosure [Keentel Engineering — '
                      'C9tZQM-x_Ho @ 00:04:21].',
                      'Bring the engineer in as soon as possible for site feasibility, critical-issue '
                      'studies, and desktop reviews to avoid redesigns [The Clean Energy Edge Podcast — '
                      'kHFYcexB2dU @ 00:12:18].',
                      'Verify the loaded protection settings, add power-quality recording at the point of '
                      'service, include sags in IST, and retest after changes [Keentel Engineering — '
                      'WN6PtJ3kQDQ @ 00:17:19].',
                      'Replace 4-second SCADA historian data with sub-second monitoring, since PRC-030 '
                      'triggers at 20 MW and 10% within 4 seconds [Keentel Engineering — f1C-d4m7OHg @ '
                      '00:08:11].'],
 'statutory_citations': [{'title': 'James Dickey — Batch Zero 9-Month Clock Starts: ERCOT Large Load '
                                   'Interconnection Workshop 3 — Feb 26, 2026 [00:18:27]',
                          'url': 'https://www.youtube.com/watch?v=9zpO8wwsfXc&t=1107s',
                          'relevance': 'Primary practitioner testimony on ERCOT Batch Zero cadence, '
                                       'commitment lock, and stakeholder dissent.'},
                         {'title': 'Keentel Engineering — PJM Interconnection Explained: How Data Centers '
                                   'Connect to the Power Grid [00:02:58]',
                          'url': 'https://www.youtube.com/watch?v=C9tZQM-x_Ho&t=178s',
                          'relevance': 'Primary practitioner testimony on the PJM Expedited '
                                       'Interconnection Track, UCAP sizing, and deposits.'},
                         {'title': 'WhyPKD — Ending the "Stupid Land" Queue: ERCOT\'s New Rules for '
                                   'Massive Power Loads [00:02:47]',
                          'url': 'https://www.youtube.com/watch?v=EvpNriZrrME&t=167s',
                          'relevance': 'Primary practitioner testimony on ERCOT batch entry requirements, '
                                       'security, and CIAC payment.'},
                         {'title': 'Keentel Engineering — 3,800 MW Data Center Load Event Explained | PJM '
                                   'Grid, Ride-Through & Reliability Lessons [00:00:00]',
                          'url': 'https://www.youtube.com/watch?v=WN6PtJ3kQDQ&t=0s',
                          'relevance': 'Primary practitioner testimony on the 3,800 MW load-loss event and '
                                       'ride-through engineering fixes.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'C9tZQM-x_Ho',
                       'title': 'PJM Interconnection Explained: How Data Centers Connect to the Power Grid',
                       'channel': 'Keentel Engineering',
                       'author': 'Keentel Engineering',
                       'text': 'PJM applies forecast discounting based on when your project is scheduled '
                               'to come online.',
                       'tip': 'PJM applies forecast discounting based on when your project is scheduled to '
                              'come online.',
                       'timestamp': 245,
                       'timestamp_seconds': 245,
                       'timestamp_label': '[00:04:05]',
                       'url': 'https://www.youtube.com/watch?v=C9tZQM-x_Ho&t=245s',
                       'markdown': '[00:04:05](https://www.youtube.com/watch?v=C9tZQM-x_Ho&t=245s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'C9tZQM-x_Ho',
                       'title': 'PJM Interconnection Explained: How Data Centers Connect to the Power Grid',
                       'channel': 'Keentel Engineering',
                       'author': 'Keentel Engineering',
                       'text': 'Strategy is about sequencing, not just selecting.',
                       'tip': 'Strategy is about sequencing, not just selecting.',
                       'timestamp': 342,
                       'timestamp_seconds': 342,
                       'timestamp_label': '[00:05:42]',
                       'url': 'https://www.youtube.com/watch?v=C9tZQM-x_Ho&t=342s',
                       'markdown': '[00:05:42](https://www.youtube.com/watch?v=C9tZQM-x_Ho&t=342s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'EvpNriZrrME',
                       'title': 'Ending the "Stupid Land" Queue: ERCOT\'s New Rules for Massive Power '
                                'Loads',
                       'channel': 'WhyPKD',
                       'author': 'WhyPKD',
                       'text': 'So, only truly capitalized projects can move forward and other rate payers '
                               'are protected.',
                       'tip': 'So, only truly capitalized projects can move forward and other rate payers '
                              'are protected.',
                       'timestamp': 303,
                       'timestamp_seconds': 303,
                       'timestamp_label': '[00:05:03]',
                       'url': 'https://www.youtube.com/watch?v=EvpNriZrrME&t=303s',
                       'markdown': '[00:05:03](https://www.youtube.com/watch?v=EvpNriZrrME&t=303s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'R1HunYyjous',
                       'title': 'Understanding PJM Interconnection: Powering the Grid Efficiently',
                       'channel': 'Edgecom Energy',
                       'author': 'Edgecom Energy',
                       'text': 'It also decides who pays for transmission upgrades, which can impact costs '
                               'in different states.',
                       'tip': 'It also decides who pays for transmission upgrades, which can impact costs '
                              'in different states.',
                       'timestamp': 94,
                       'timestamp_seconds': 94,
                       'timestamp_label': '[00:01:34]',
                       'url': 'https://www.youtube.com/watch?v=R1HunYyjous&t=94s',
                       'markdown': '[00:01:34](https://www.youtube.com/watch?v=R1HunYyjous&t=94s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '9zpO8wwsfXc',
                       'title': 'Batch Zero 9-Month Clock Starts: ERCOT Large Load Interconnection '
                                'Workshop 3 — Feb 26, 2026',
                       'channel': 'James Dickey',
                       'author': 'James Dickey',
                       'text': "And then in that three month window, the only variable that you're then "
                               'moving is the transmission.',
                       'tip': "And then in that three month window, the only variable that you're then "
                              'moving is the transmission.',
                       'timestamp': 3820,
                       'timestamp_seconds': 3820,
                       'timestamp_label': '[01:03:40]',
                       'url': 'https://www.youtube.com/watch?v=9zpO8wwsfXc&t=3820s',
                       'markdown': '[01:03:40](https://www.youtube.com/watch?v=9zpO8wwsfXc&t=3820s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '9zpO8wwsfXc',
                       'title': 'Batch Zero 9-Month Clock Starts: ERCOT Large Load Interconnection '
                                'Workshop 3 — Feb 26, 2026',
                       'channel': 'James Dickey',
                       'author': 'James Dickey',
                       'text': 'And so we are going to administratively set your energization date to '
                               '01/01/2028.',
                       'tip': 'And so we are going to administratively set your energization date to '
                              '01/01/2028.',
                       'timestamp': 8346,
                       'timestamp_seconds': 8346,
                       'timestamp_label': '[02:19:06]',
                       'url': 'https://www.youtube.com/watch?v=9zpO8wwsfXc&t=8346s',
                       'markdown': '[02:19:06](https://www.youtube.com/watch?v=9zpO8wwsfXc&t=8346s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '9zpO8wwsfXc',
                       'title': 'Batch Zero 9-Month Clock Starts: ERCOT Large Load Interconnection '
                                'Workshop 3 — Feb 26, 2026',
                       'channel': 'James Dickey',
                       'author': 'James Dickey',
                       'text': 'We are exposed to fifty, sixty million depending on the location of the '
                               'project.',
                       'tip': 'We are exposed to fifty, sixty million depending on the location of the '
                              'project.',
                       'timestamp': 15336,
                       'timestamp_seconds': 15336,
                       'timestamp_label': '[04:15:36]',
                       'url': 'https://www.youtube.com/watch?v=9zpO8wwsfXc&t=15336s',
                       'markdown': '[04:15:36](https://www.youtube.com/watch?v=9zpO8wwsfXc&t=15336s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'S8vmSHwFrvE',
                       'title': 'Large Load Interconnection to ERCOT',
                       'channel': 'Data Centers Technical Info',
                       'author': 'Data Centers Technical Info',
                       'text': "In ERCOT, we've seen over a dozen plus events in the last year where "
                               'hundreds of megawatts have unexpectedly left the grid that nobody '
                               'expected, nobody planned for.',
                       'tip': "In ERCOT, we've seen over a dozen plus events in the last year where "
                              'hundreds of megawatts have unexpectedly left the grid that nobody expected, '
                              'nobody planned for.',
                       'timestamp': 1287,
                       'timestamp_seconds': 1287,
                       'timestamp_label': '[00:21:27]',
                       'url': 'https://www.youtube.com/watch?v=S8vmSHwFrvE&t=1287s',
                       'markdown': '[00:21:27](https://www.youtube.com/watch?v=S8vmSHwFrvE&t=1287s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'dMPUECoTe2M',
                       'title': 'Should Data Centers Bring Their Own Power or Wait in Line?',
                       'channel': 'Profound Studies',
                       'author': 'Profound Studies',
                       'text': 'High voltage circuit breakers went from 77 weeks in 2023 to 125 weeks last '
                               'year.',
                       'tip': 'High voltage circuit breakers went from 77 weeks in 2023 to 125 weeks last '
                              'year.',
                       'timestamp': 100,
                       'timestamp_seconds': 100,
                       'timestamp_label': '[00:01:40]',
                       'url': 'https://www.youtube.com/watch?v=dMPUECoTe2M&t=100s',
                       'markdown': '[00:01:40](https://www.youtube.com/watch?v=dMPUECoTe2M&t=100s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'WN6PtJ3kQDQ',
                       'title': '3,800 MW Data Center Load Event Explained | PJM Grid, Ride-Through & '
                                'Reliability Lessons',
                       'channel': 'Keentel Engineering',
                       'author': 'Keentel Engineering',
                       'text': 'Ride through is cheapest to engineer before equipment is purchased and '
                               'installed.',
                       'tip': 'Ride through is cheapest to engineer before equipment is purchased and '
                              'installed.',
                       'timestamp': 986,
                       'timestamp_seconds': 986,
                       'timestamp_label': '[00:16:26]',
                       'url': 'https://www.youtube.com/watch?v=WN6PtJ3kQDQ&t=986s',
                       'markdown': '[00:16:26](https://www.youtube.com/watch?v=WN6PtJ3kQDQ&t=986s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Lh1aLCJikCo',
                       'title': 'Who Pays When an AI Data Centre Cannot Connect?',
                       'channel': 'Beyound The Signal',
                       'author': 'Beyound The Signal',
                       'text': 'But a connection offer should not be a free option on the public network.',
                       'tip': 'But a connection offer should not be a free option on the public network.',
                       'timestamp': 424,
                       'timestamp_seconds': 424,
                       'timestamp_label': '[00:07:04]',
                       'url': 'https://www.youtube.com/watch?v=Lh1aLCJikCo&t=424s',
                       'markdown': '[00:07:04](https://www.youtube.com/watch?v=Lh1aLCJikCo&t=424s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'u0kuoKQbHTs',
                       'title': 'AI’s Grid Queue: Who Pays to Connect the Data-Centre Boom?',
                       'channel': 'Sarthak',
                       'author': 'Sarthak',
                       'text': "Flexibility is not universal, and it's certainly not a magic substitute "
                               'for building actual grid capacity.',
                       'tip': "Flexibility is not universal, and it's certainly not a magic substitute for "
                              'building actual grid capacity.',
                       'timestamp': 306,
                       'timestamp_seconds': 306,
                       'timestamp_label': '[00:05:06]',
                       'url': 'https://www.youtube.com/watch?v=u0kuoKQbHTs&t=306s',
                       'markdown': '[00:05:06](https://www.youtube.com/watch?v=u0kuoKQbHTs&t=306s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'f1C-d4m7OHg',
                       'title': 'NERC Compliance Engineering: Reliability Standards, IBR Requirements & '
                                'Power System Compliance',
                       'channel': 'Keentel Engineering',
                       'author': 'Keentel Engineering',
                       'text': 'A modest capacity addition changes your regulatory status overnight.',
                       'tip': 'A modest capacity addition changes your regulatory status overnight.',
                       'timestamp': 239,
                       'timestamp_seconds': 239,
                       'timestamp_label': '[00:03:59]',
                       'url': 'https://www.youtube.com/watch?v=f1C-d4m7OHg&t=239s',
                       'markdown': '[00:03:59](https://www.youtube.com/watch?v=f1C-d4m7OHg&t=239s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'u6jr6SB0bD4',
                       'title': 'Why Is My Electric Bill So High? Live Close to Data Centers & AI Power? '
                                'Explained',
                       'channel': 'Techdamentals',
                       'author': 'Techdamentals',
                       'text': 'That auction price is called a capacity price and it gets passed into '
                               "everyone's bill.",
                       'tip': 'That auction price is called a capacity price and it gets passed into '
                              "everyone's bill.",
                       'timestamp': 71,
                       'timestamp_seconds': 71,
                       'timestamp_label': '[00:01:11]',
                       'url': 'https://www.youtube.com/watch?v=u6jr6SB0bD4&t=71s',
                       'markdown': '[00:01:11](https://www.youtube.com/watch?v=u6jr6SB0bD4&t=71s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'kHFYcexB2dU',
                       'title': 'Why AI Data Centers Are Overwhelming the Grid (It’s Not Just Generation)',
                       'channel': 'The Clean Energy Edge Podcast',
                       'author': 'The Clean Energy Edge Podcast',
                       'text': 'And so, that is a pretty stressful impact on the grid.',
                       'tip': 'And so, that is a pretty stressful impact on the grid.',
                       'timestamp': 251,
                       'timestamp_seconds': 251,
                       'timestamp_label': '[00:04:11]',
                       'url': 'https://www.youtube.com/watch?v=kHFYcexB2dU&t=251s',
                       'markdown': '[00:04:11](https://www.youtube.com/watch?v=kHFYcexB2dU&t=251s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'a34rwkck9IA',
                       'title': 'Energy Insights: A Conversation between ERCOT and PJM leaders',
                       'channel': 'ERCOTISO',
                       'author': 'ERCOTISO',
                       'text': 'We have about 8 gigawatts of DR available in the control room today.',
                       'tip': 'We have about 8 gigawatts of DR available in the control room today.',
                       'timestamp': 1020,
                       'timestamp_seconds': 1020,
                       'timestamp_label': '[00:17:00]',
                       'url': 'https://www.youtube.com/watch?v=a34rwkck9IA&t=1020s',
                       'markdown': '[00:17:00](https://www.youtube.com/watch?v=a34rwkck9IA&t=1020s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'nzC-XREeuz4',
                       'title': 'Why PJM is looking at the Texas grid',
                       'channel': 'Texas Energy & Power',
                       'author': 'Texas Energy & Power',
                       'text': 'That applies even if you go out as a large load customer and acquire your '
                               "own capacity to match what you're bringing online.",
                       'tip': 'That applies even if you go out as a large load customer and acquire your '
                              "own capacity to match what you're bringing online.",
                       'timestamp': 1003,
                       'timestamp_seconds': 1003,
                       'timestamp_label': '[00:16:43]',
                       'url': 'https://www.youtube.com/watch?v=nzC-XREeuz4&t=1003s',
                       'markdown': '[00:16:43](https://www.youtube.com/watch?v=nzC-XREeuz4&t=1003s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'DU-7TmjHp7c',
                       'title': 'Planning the Grid for Large Loads, Jason Connell, PJM Interconnection | '
                                'EP 2026',
                       'channel': 'POWERmagvideos',
                       'author': 'POWERmagvideos',
                       'text': 'We do have a partnership with Google Tapestry that we are working with '
                               'them on trying to streamline a lot of our application review, particularly '
                               'around site control, and their tools have been very helpful for us.',
                       'tip': 'We do have a partnership with Google Tapestry that we are working with them '
                              'on trying to streamline a lot of our application review, particularly '
                              'around site control, and their tools have been very helpful for us.',
                       'timestamp': 141,
                       'timestamp_seconds': 141,
                       'timestamp_label': '[00:02:21]',
                       'url': 'https://www.youtube.com/watch?v=DU-7TmjHp7c&t=141s',
                       'markdown': '[00:02:21](https://www.youtube.com/watch?v=DU-7TmjHp7c&t=141s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'}]}
