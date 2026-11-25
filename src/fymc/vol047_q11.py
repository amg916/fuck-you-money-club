from __future__ import annotations

CHAPTER_11 = {'id': 'Q11',
 'chapter_id': 'Q11',
 'chapter_number': 11,
 'question_number': 11,
 'slug': 'bess-data-center-power-quality-safety-integration',
 'question_prompt': 'How should batteries be co-located with data centers for power quality and spiky AI '
                    'loads, and what fire, civil, and integration risks must be engineered out?',
 'kicker': 'Q11 / THE BIG MONEY PLAYBOOKS',
 'title': 'BESS at the Data Center: Power Quality, Safety and Integration',
 'subtitle': 'Co-locating batteries with data centers, grid-forming BESS for AI load swings, harmonics and '
             'stability, unlocking grid capacity, microgrid-enabled storage, UL fire testing, design-build '
             'fire protection, civil design, SCADA integration lessons, simulation of integration risk, '
             'and grid vulnerabilities',
 'layout_template': 'chapter_opener',
 'reading_time_minutes': 15,
 'executive_summary': 'Practitioners across utility, fire-code, EPC and simulation work converge on one '
                      'read: AI training loads that jump 30-60% in milliseconds and mass-trip on voltage '
                      'dips make a grid-forming BESS the price of interconnection, not an add-on. ABB '
                      'sizes genset-delay systems at 1-2 h and targets breaker-limited islanding under '
                      'half a second behind a 20 ms battery pickup. Lyten reports its mobile system '
                      'flattening up to 99.5% of load-step volatility in controlled tests. Keentel insists '
                      'compliance lives in TDD at the PCC, with validated models before the purchase order '
                      "and EMT studies on weak grids. On safety, UL's 9540A 6th edition forces fully "
                      'populated installation-level burns, while Orange County fire officials refuse '
                      'approval to unlisted systems. The splits: software smoothing versus hardware, '
                      "supplementing versus replacing diesel, and 'let it burn' fire marshals versus "
                      'active suppression.',
 'key_metrics': [{'label': 'BESS Islanding Pickup Time',
                  'metric': 'BESS Islanding Pickup Time',
                  'value': '20 ms at full load; system target under 0.5 s including upstream breaker '
                           'opening',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "ABB's BESS has no bypass and picks up full load in 20 ms, so the upstream "
                             'breaker opening time sets the real islanding limit.',
                  'source': 'Digital Infrastructure Network ([U2apRbTTZuE @ 00:08:45])'},
                 {'label': 'Load-Step Volatility Flattened',
                  'metric': 'Load-Step Volatility Flattened',
                  'value': 'Up to 99.5% of load-step volatility; grid-side variation cut up to 94.5%',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Lyten's VMS controlled test results. It was actively charging or discharging "
                             '98% of the time and held voltage within +/-0.4%.',
                  'source': 'Volta Foundation ([7h6DABJ_xgs @ 00:18:08])'},
                 {'label': 'Large-Scale Fire Test Trigger',
                  'metric': 'Large-Scale Fire Test Trigger',
                  'value': 'Baseline 50 kWh at 3 ft; 100 kWh at 2 ft triggers the NFPA 855 Chapter 9 test',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "UL's threshold for when installation-level fire testing kicks in. About one "
                             'day of testing takes about two weeks of preparation.',
                  'source': 'UL Solutions ([TtbHyJ6xzNg @ 00:15:29])'},
                 {'label': 'Exhaust Reingestion Runaway Loop',
                  'metric': 'Exhaust Reingestion Runaway Loop',
                  'value': '45C intake to 55C exhaust; at 50% reingestion, 50C intake and 60C exhaust',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Rand Simulation's CFD loop for dense container yards, running from derate to "
                             'thermal runaway and fire. The intake threshold is 54C.',
                  'source': 'Rand Simulation ([LBt7MoTnFFQ @ 00:21:35])'}],
 'sections': [{'heading': 'Section 1: The Practitioner Consensus',
               'paragraphs': ["Every power-side speaker names the load as the problem. Lyten's JP lays out "
                              'the mass-trip mechanic: PSUs and UPSs disconnect at the first voltage dip, '
                              'so a single fault can drop roughly 1,500 MW and spike frequency. NERC '
                              'issued a Level 3 alert in May 2026 covering events since 2022 that each '
                              "topped 1,000 MW. JP's line: 'protection that makes sense inside the "
                              "building can create a risk for everyone outside of it' [7h6DABJ_xgs @ "
                              "00:05:51]. Generac's Brad Ritter independently describes AI loads spiking "
                              '50% at millisecond scale and sites tripping offline during faults, with '
                              'spikiness severe enough to crack turbines [Ic-Cuo3Xdfo @ 00:01:48]. FlexGen '
                              'reaches the same place from the utility side. Step loads outrun what '
                              'spinning-inertia plants can follow, and utilities demand studies. The '
                              'battery becomes a shock absorber that makes the campus look like a '
                              "'smaller, stabilized load,' potentially pulling approvals forward by years "
                              '[LhqvSN3OdlI @ 00:02:44]. Ritter states the commercial consequence flatly: '
                              "BESS is now 'table stakes' for interconnect agreements, and utilities layer "
                              'bring-your-own-generation and behavior constraints on top [Ic-Cuo3Xdfo @ '
                              "00:12:53]. Across these speakers, the battery's first job is making the "
                              'load acceptable to the grid operator.',
                              'The second point of agreement is that the inverter must be grid-forming. '
                              "Keentel's Sandeep Sunny Patel opens with 'a BESS is fundamentally a power "
                              "electronic converter with a battery attached' and states that grid-forming "
                              'inverters are required for islanding and black start [BTkszCEW7nY @ '
                              "00:02:57]. ABB's Donald Turk and Carlos Nieto build their genset-delay "
                              'architecture on that. The BESS runs in parallel with grid and genset. '
                              'During an outage, the UPS carries IT load while the BESS goes grid-forming. '
                              'Gensets start in parallel only once state of charge falls below an '
                              'operator-set threshold, and the battery supplies spinning reserve so the '
                              'engines run at optimal speed [U2apRbTTZuE @ 00:06:32]. Ritter describes the '
                              'same pattern at campus scale: parallel grid-forming inverters black start '
                              'the site and call generators after about 30 minutes. That matters when a '
                              "200 MW site can need 'hundreds of generators' [Ic-Cuo3Xdfo @ 00:15:12]. The "
                              'ABB pair frame the economics against diesel. A genset stands idle 99% of '
                              'the time, while the BESS can provide additional services to the grid, '
                              'earning from time-of-use, fast frequency response, peak demand management '
                              'and capacity aggregation [U2apRbTTZuE @ 00:05:09]. ABB adds that islanding '
                              'and resync run automatically, with black start available.',
                              'The safety and permitting side agrees just as firmly that listing and '
                              'large-scale fire data come first. UL principal engineer LaTanya Schwab '
                              'explains that NFPA 855 (2026) Chapter 9 requires UL 9540A testing plus a '
                              "large-scale fire test that 'involves the intentional ignition of gases that "
                              "are vented from lithium-ion batteries during a thermal runaway event' "
                              "[TtbHyJ6xzNg @ 00:02:58]. Orange County Fire Authority's Robert treats a "
                              'missing UL 9540 listing or full-scale fire test as a showstopper, as are '
                              'manufacturers that bar indoor installation, such as Megapacks. Approval '
                              'waits until the system is listed. Entitlement comes first, then fire plan '
                              "review, which Robert's authority turns in 2-3 weeks [-B0ACVnCSu0 @ "
                              '00:18:02]. The BESS Book co-authors Drew Lebowitz and Swetha Sundaram call '
                              'NFPA 855 the umbrella standard that pulls in NFPA 68, 69 and 72, and they '
                              'push early engagement with AHJs and volunteer fire departments [eynQ4qifTao '
                              '@ 00:43:13]. Beneath all of it sits dirt. The Australian civil engineering '
                              "walkthrough warns that 'if water gathers beneath high voltage equipment, "
                              "the facility fails.' So the site is graded at 0.5-1.0%, platforms sit above "
                              'the 1% AEP flood level plus 300-500 mm freeboard, a windrow berm diverts '
                              "overland flow, and neighbors' flood depth and velocity cannot worsen "
                              '[935Rt3dBZso @ 00:03:10].'],
               'table': {'caption': 'Where the practitioners line up: the baseline case for BESS at an AI '
                                    'data center',
                         'headers': ['Consensus Point',
                                     'What Practitioners Report',
                                     'Operator Implication',
                                     'Expert Source'],
                         'rows': [['AI load swings are violent and fast',
                                   'Training load jumps 30-60% within milliseconds, and 0.2-3 Hz swings '
                                   'drive torsional and subsynchronous resonance',
                                   'Gas turbine makers say turbines may not last 1-2 years under these '
                                   'swings without buffering',
                                   'Volta Foundation ([7h6DABJ_xgs @ 00:06:11])'],
                                  ['In-building protection creates outside grid risk',
                                   'PSUs and UPSs disconnect at the first voltage dip, so one fault drops '
                                   'about 1,500 MW',
                                   'Grid operators respond by accepting the risk, capping or curtailing '
                                   'the load, or demanding grid-safe loads',
                                   'Volta Foundation ([7h6DABJ_xgs @ 00:03:40])'],
                                  ['BESS is now an interconnection requirement',
                                   "BESS is 'table stakes' for interconnect agreements, and utilities "
                                   'require bring-your-own generation',
                                   'Budget the battery as part of the grid deal itself, not as an optional '
                                   'backup upgrade',
                                   'The POWER Podcast ([Ic-Cuo3Xdfo @ 00:12:53])'],
                                  ['The battery acts as a shock absorber',
                                   'Co-located storage makes the site look like a smaller, stabilized load '
                                   'at a single interconnection point',
                                   'This could bring approvals years earlier and bypass decade-long grid '
                                   'queue waits for the campus',
                                   'FlexGen ([LhqvSN3OdlI @ 00:02:44])'],
                                  ['Grid-forming inverters are mandatory for islanding',
                                   'Grid-forming inverters are required for islanding and black start; '
                                   'grid-following PLLs fail on weak grids',
                                   'Specify grid-forming capability and validated models before issuing '
                                   'the purchase order to any vendor',
                                   'Keentel Engineering ([BTkszCEW7nY @ 00:02:57])'],
                                  ['No listing means no approval',
                                   'A missing UL 9540 listing or full-scale fire test is a fire authority '
                                   'showstopper',
                                   'Secure entitlement and listing first; fire plan review then runs about '
                                   '2-4 weeks',
                                   'ALL4 Environmental Consultants ([-B0ACVnCSu0 @ 00:18:02])'],
                                  ['Civil works decide whether the battery survives',
                                   'Water gathering beneath high voltage equipment fails the facility, so '
                                   'platforms sit above flood level plus freeboard',
                                   'Design grading, drainage, firewater retention and construction-phase '
                                   'pavement before electrical layout is frozen',
                                   'Civil and Structural Engineer ([935Rt3dBZso @ 00:03:10])']]}},
              {'heading': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ["ABB's Turk and Nieto supply the cleanest sizing math. In the genset-delay "
                              'case, the system is 1 MW and 2 MWh, sized for 1-2 h and modeled on two '
                              'one-hour outages per year, saving 26.1 t CO2 per MW [U2apRbTTZuE @ '
                              '00:06:32]. The genset-replace case needs 2-8 h of storage and saves 180 t '
                              'over a 15-year life, because the engines no longer run even for '
                              'maintenance. When state of charge runs low, IT load must transfer to '
                              'another server. A parallel fuel cell cuts the battery back to 1-2 h, with '
                              'the BESS setting voltage and frequency while the fuel cell injects current, '
                              'on fuels from methanol to ammonia cracked on site [U2apRbTTZuE @ 00:09:22]. '
                              'The UPS line shrinks too. At 1 MW, five minutes of UPS takes six battery '
                              'blocks, but behind a BESS 30 seconds is enough, covered by three '
                              'ultracapacitor racks [U2apRbTTZuE @ 00:12:21]. Islanding speed is set by '
                              'hardware outside the battery. The BESS has no bypass and picks up full load '
                              "within 20 ms, so upstream breaker opening time is the limit, and ABB's "
                              "target is under half a second. For land, RavenVolt's Daniel Hudson says a "
                              '10 MW system at 2 h or 4 h (20 or 40 MWh) needs about a quarter acre, and '
                              '20 MW about half an acre [biJIJcXR5mE @ 00:05:52].',
                              "Power quality is where Keentel's Patel sees projects get blindsided. The "
                              'trap is that teams chase THD, but compliance is measured as TDD at the '
                              "point of common coupling, and 'a blindly placed filter might just push the "
                              "resonance to a worse frequency' [BTkszCEW7nY @ 00:01:14]. On weak, low-SCR "
                              'grids the PLL can lose stability, so EMT modeling is required. Because '
                              'fault current is software-limited, overcurrent protection fails, and '
                              "directional or differential protection is needed. Patel's mitigation ladder "
                              'runs tier 1 software, tier 2 design, tier 3 filters and tier 4 STATCOMs, '
                              "the 'heavy iron' reserved as an absolute last resort. Skipping studies just "
                              "'deferred risk without pricing it' [BTkszCEW7nY @ 00:03:16]. On controls, "
                              'FlexGen warns that without orchestration, assets compete for inverter '
                              'capacity. Its hybrid OS honors a 50 MW grid cap by throttling generation '
                              "while the battery bridges, keeping the data center 'at 100% capacity "
                              "without ever violating the grid's cap' [LhqvSN3OdlI @ 00:03:38]. Lyten's JP "
                              'pitches the reactive end of the range. When servers drop off, VMS draws an '
                              'equivalent load within one grid cycle (1/60 s) and needs no prior '
                              'configuration. In controlled tests it was charging or discharging 98% of '
                              'the time and held voltage within +/-0.4%, up to 22x tighter than the '
                              'standard limit [7h6DABJ_xgs @ 00:17:01].',
                              "The 6th edition of UL 9540A, published in March, drops the old 'exit ramps' "
                              'that let testing stop early. The sequence now runs cell, module, optional '
                              "unit, then installation level; as Schwab puts it, 'the unit level test is "
                              "now optional' [TtbHyJ6xzNg @ 00:06:54]. The installation test uses a fully "
                              'populated enclosure of live cells, often hundreds, placed at the real '
                              'separation distance, such as 3 ft. The thermal runaway prevention system is '
                              'switched off in the enclosure of origin [TtbHyJ6xzNg @ 00:09:13]. Budget '
                              'the calendar: about one day of burn takes about two weeks of prep, and '
                              'moving from the 50 kWh at 3 ft baseline to 100 kWh at 2 ft triggers the '
                              "Chapter 9 test [TtbHyJ6xzNg @ 00:15:29]. Rand Simulation's Chris Smith adds "
                              'the thermal layer that suppliers miss by designing equipment in isolation. '
                              'A 45C intake yields 55C exhaust, and at 50% reingestion the intake climbs '
                              'to 50C and the exhaust to 60C, a loop running from derate to thermal '
                              'runaway and fire. Smith evaluates at 30% and 60% design. On a synthetic '
                              'Fort Stockton, Texas site of about 320 containers, a 7 mph southeast wind '
                              'derated about half the units. Fitting 70-degree louvers on the HVAC '
                              'exhausts then held aisles at 51-53C against a 54C intake threshold '
                              '[LBt7MoTnFFQ @ 00:21:35].'],
               'table': {'caption': 'Street mechanics: the exact sizing, power-quality, fire-test and '
                                    'thermal numbers practitioners use',
                         'headers': ['Mechanic', 'Exact Number or Spec', 'Execution Note', 'Expert Source'],
                         'rows': [['Genset-delay BESS sizing',
                                   '1 MW, 2 MWh, 1-2 h duration, two one-hour outages per year, 26.1 t CO2 '
                                   'saved per MW',
                                   'Gensets start in parallel only below an operator-set state of charge '
                                   'threshold',
                                   'Digital Infrastructure Network ([U2apRbTTZuE @ 00:06:32])'],
                                  ['Genset-replace BESS sizing',
                                   '2-8 h of storage saves 180 t over 15 years; a parallel fuel cell cuts '
                                   'it to 1-2 h',
                                   'The BESS sets voltage and frequency while the fuel cell injects '
                                   'current into the bus',
                                   'Digital Infrastructure Network ([U2apRbTTZuE @ 00:09:22])'],
                                  ['UPS shrink behind a BESS',
                                   'At 1 MW, 5 minutes needs 6 battery blocks; 30 seconds needs only 3 '
                                   'ultracapacitor racks',
                                   'Cuts UPS backup time and gray-space footprint once the BESS carries '
                                   'the bridge',
                                   'Digital Infrastructure Network ([U2apRbTTZuE @ 00:12:21])'],
                                  ['Reactive load compensation',
                                   'Equivalent load drawn within one grid cycle (1/60 s); voltage held '
                                   'within +/-0.4%',
                                   'Lyten states these are controlled tests; deeper validation data '
                                   'requires an NDA',
                                   'Volta Foundation ([7h6DABJ_xgs @ 00:17:01])'],
                                  ['Harmonic compliance at the interconnection',
                                   'Compliance is measured as TDD at the PCC, not THD at the equipment '
                                   'terminals',
                                   'Placing a filter blindly can push the resonance to a worse frequency; '
                                   'STATCOMs come last',
                                   'Keentel Engineering ([BTkszCEW7nY @ 00:01:14])'],
                                  ['Large-scale fire test trigger and effort',
                                   'Baseline 50 kWh at 3 ft; 100 kWh at 2 ft triggers the Chapter 9 test',
                                   'One day of testing takes about two weeks of preparation, with heat '
                                   'flux gauges',
                                   'UL Solutions ([TtbHyJ6xzNg @ 00:15:29])'],
                                  ['Container yard reingestion fix',
                                   '70-degree exhaust louvers held aisles at 51-53C against a 54C intake '
                                   'threshold',
                                   'Check fan pressure margin; a 7 mph wind derated about 50% of 320 units',
                                   'Rand Simulation ([LBt7MoTnFFQ @ 00:27:17])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'What the operators lock in before the PO is signed',
                           'body': 'These moves cost little early in the project. Practitioners report '
                                   'that they become expensive to retrofit once the equipment is ordered '
                                   'and the interconnection study clock is running.',
                           'items': ['Buy switchgear with digital components from the start so the site '
                                     'can be monitored and controlled remotely through the storage OS and '
                                     'BMS link [Digital Infrastructure Network — U2apRbTTZuE @ 00:16:29]',
                                     'Demand validated vendor models before the purchase order, because a '
                                     'BESS is fundamentally a power electronic converter with a battery '
                                     'attached [Keentel Engineering — BTkszCEW7nY @ 00:00:17]',
                                     'Spec SCADA for high data volume and retention, and test AEMO DNP3 '
                                     'event transmission for buffer overflow before connection [Australian '
                                     'Control Engineering | Smart Utilities — 8eadjA6Pqyo @ 00:00:20]',
                                     'Size bridge power so it can transition into permanent service '
                                     'without being ripped out later [The POWER Podcast — Ic-Cuo3Xdfo @ '
                                     '00:25:16]']},
               'sop_steps': [{'step': 1,
                              'title': 'Clear zoning and entitlement first',
                              'action': 'Confirm zoning, then scale, then file for fire plan review with a '
                                        'listed system.',
                              'detail': 'Check zoning before scale. A conditional use permit adds months: '
                                        'small projects take 3-6 months, larger ones more than a year, and '
                                        'utility approval can add a year or more [ALL4 Environmental '
                                        'Consultants — -B0ACVnCSu0 @ 00:16:24]'},
                             {'step': 2,
                              'title': 'Run interconnection power-quality studies',
                              'action': 'Model TDD at the PCC, run EMT on weak grids, and set protection '
                                        'to directional or differential.',
                              'detail': 'Low-SCR grids can destabilize the PLL, so EMT modeling is '
                                        'required, and utilities require model submissions for approval '
                                        '[Keentel Engineering — BTkszCEW7nY @ 00:02:38]'},
                             {'step': 3,
                              'title': 'Specify grid-forming islanding performance',
                              'action': 'Require 20 ms full-load pickup, an operator-set SOC genset start, '
                                        'and breaker opening under 0.5 s.',
                              'detail': 'The BESS picks up load within 20 ms at full load. Upstream '
                                        'breaker opening time is the limit, so the target is staying below '
                                        'half a second [Digital Infrastructure Network — U2apRbTTZuE @ '
                                        '00:08:45]'},
                             {'step': 4,
                              'title': 'Validate fire spread and thermal layout',
                              'action': 'Commission a fully populated UL 9540A installation-level test, '
                                        'then run yard CFD at 30% and 60% design.',
                              'detail': 'Use live cells at the real separation distance, with the '
                                        'prevention system off in the enclosure of origin [UL Solutions — '
                                        'TtbHyJ6xzNg @ 00:09:13]. Evaluate reingestion at 30% and 60% '
                                        'design [Rand Simulation — LBt7MoTnFFQ @ 00:14:15]'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ["ABB's Turk and Nieto pitch two distinct playbooks on the Digital "
                              'Infrastructure Network stage. The conservative one runs a 1-2 hour BESS in '
                              'parallel with grid and gensets and starts the engines only below an '
                              'operator-set state of charge. The aggressive one deletes the gensets '
                              'outright, which requires 2-8 hours of storage, or a fuel cell in parallel '
                              'that cuts the battery back to 1-2 hours [U2apRbTTZuE @ 00:09:22]. The ABB '
                              'case leans on the genset standing idle 99% of the time while a BESS can '
                              "sell services to the grid [U2apRbTTZuE @ 00:05:09]. ALL4's Sharon Sadler "
                              'reports the field differently: BESS is supplementing diesel, not yet '
                              'replacing it, and one facility committed to a grid-stability program '
                              'pivoted to BESS only after a permitting pause hit it [-B0ACVnCSu0 @ '
                              "00:13:28]. Generac's Brad Ritter lands between the camps on The POWER "
                              'Podcast. Ritter calls BESS table stakes for interconnect agreements, yet '
                              'the Generac architecture still uses parallel grid-forming inverters to '
                              'black start the site and call generators after about 30 minutes, on '
                              'campuses where 200 MW can need hundreds of generators [Ic-Cuo3Xdfo @ '
                              '00:15:12]. The operator read: genset deletion is a design option ABB sells, '
                              'while the market Sadler and Ritter describe still keeps iron behind the '
                              'batteries.',
                              "On power quality, Lyten's JP treats software and rack-level fixes as "
                              'half-measures. GPU power-capping at about 90% of rated power still leaves '
                              'about 20% of the swing and burns 10% more energy. Rack ultracapacitors or '
                              "UPS can't flatten sustained swings and do nothing for cooling, which can be "
                              "up to a third of demand. JP's conclusion is that these problems can only be "
                              'solved at the grid interconnection [7h6DABJ_xgs @ 00:21:07]. ABB works the '
                              'opposite end inside the white space. At 1 MW, the BESS shrinks UPS autonomy '
                              'from five minutes on six battery blocks to 30 seconds on three '
                              "ultracapacitor racks [U2apRbTTZuE @ 00:12:21]. Keentel's Sandeep Sunny "
                              'Patel runs a third playbook, a tiered escalation that starts with software, '
                              'moves to design, then filters, and holds heavy-iron STATCOMs as the '
                              'absolute last resort, because a blindly placed filter can push the '
                              'resonance to a worse frequency [BTkszCEW7nY @ 00:04:35]. FlexGen frames the '
                              'answer as orchestration. Its hybrid OS throttles generation while the '
                              'battery bridges, so a co-located site stays at full capacity without '
                              'violating a 50 MW grid cap [LhqvSN3OdlI @ 00:03:38]. The split: Lyten puts '
                              'the fix at the point of interconnection, Patel escalates from the cheapest '
                              'tier, and ABB and FlexGen lean on the control layer.',
                              'Fire posture is where practitioners split hardest. Orange County Fire '
                              "Authority's Robert, on the ALL4 panel, says plume modeling points toward "
                              'shelter in place rather than evacuation and that a battery fire burns like '
                              'a big-box store fire, with the team sampling the air by drone. On that '
                              'account, Otay Mesa and Moss Landing hurt few people even as public fear '
                              'runs high [-B0ACVnCSu0 @ 00:29:02]. Nancy White of the Secure the Grid '
                              "Coalition, appearing on Chris Heasley's channel, paints the opposite "
                              'picture: evacuation radii up to 5-6 miles and lockdowns out to 10-15 miles, '
                              'figures delivered with a self-hedge [oHZCEiu2Vc8 @ 00:14:04]. Robert also '
                              'splits indoor from outdoor risk. Outdoors, typically only one unit burns. '
                              'The indoor Otay Mesa fire consumed 12 million gallons of water and burned '
                              'up to a firewall as a total loss [-B0ACVnCSu0 @ 00:40:20]. The SunCast '
                              'Media BESS Book co-authors take the long view, citing EPRI data that '
                              'incidents fell about 97% over 6-7 years [eynQ4qifTao @ 00:44:39]. For a '
                              'data-center campus that must keep IT load online, the contrast is stark. '
                              "Robert's measured data argues for containment, separation and shelter in "
                              "place, White's numbers argue for distance from people, and the local fire "
                              'authority decides which story governs the permit.'],
               'table': {'caption': 'Contested Playbooks for BESS at the AI Data Center',
                         'headers': ['Decision Point',
                                     'Playbook A (Who / What)',
                                     'Playbook B (Who / What)',
                                     'Expert Source'],
                         'rows': [['Fate of diesel gensets on the data center campus',
                                   'ABB deletes gensets using 2-8 h BESS, or a fuel cell plus a 1-2 h '
                                   'battery',
                                   'Sadler reports BESS supplementing diesel in the field, not yet '
                                   'replacing it',
                                   'Digital Infrastructure Network ([U2apRbTTZuE @ 00:09:22]); ALL4 '
                                   'Environmental Consultants ([-B0ACVnCSu0 @ 00:13:28])'],
                                  ['Where AI training load swings get flattened',
                                   'Lyten says swings can only be solved at the grid interconnection',
                                   'ABB shrinks UPS autonomy to 30 seconds on three ultracapacitor racks '
                                   'per MW',
                                   'Volta Foundation ([7h6DABJ_xgs @ 00:21:07]); Digital Infrastructure '
                                   'Network ([U2apRbTTZuE @ 00:12:21])'],
                                  ['Order of power-quality mitigation spending on site',
                                   'Keentel escalates through software, design and filters, with STATCOMs '
                                   'as the last resort',
                                   'Lyten rejects software capping because about 20% of the swing remains, '
                                   'at 10% more energy',
                                   'Keentel Engineering ([BTkszCEW7nY @ 00:04:35]); Volta Foundation '
                                   '([7h6DABJ_xgs @ 00:20:00])'],
                                  ['Outage ride-through and black start sequence',
                                   'ABB BESS islands with no bypass, picking up full load within 20 '
                                   'milliseconds',
                                   'Generac black starts on grid-forming inverters and calls generators '
                                   'after about 30 minutes',
                                   'Digital Infrastructure Network ([U2apRbTTZuE @ 00:08:45]); The POWER '
                                   'Podcast ([Ic-Cuo3Xdfo @ 00:15:12])'],
                                  ['Public safety posture during an active BESS fire',
                                   "Robert's plume modeling and drone air sampling point toward shelter in "
                                   'place',
                                   'Nancy White warns of 5-6 mile evacuation and 10-15 mile lockdown radii',
                                   'ALL4 Environmental Consultants ([-B0ACVnCSu0 @ 00:29:02]); Chris '
                                   'Heasley ([oHZCEiu2Vc8 @ 00:14:04])'],
                                  ['Jurisdiction stance toward battery projects and burning units',
                                   'Some jurisdictions embrace BESS, and the BESS Book authors push early '
                                   'AHJ and volunteer fire department engagement',
                                   'Some fire marshals choose let it burn, and one permit south of Houston '
                                   'was denied over setbacks',
                                   'SunCast Media ([eynQ4qifTao @ 00:43:13]); Fire Protection Engineering '
                                   'Podcast ([biJIJcXR5mE @ 00:29:27])'],
                                  ['Chemistry bet for the next build cycle',
                                   'Robert expects LFP to dominate for a long time among about 20 listed '
                                   'types',
                                   'BESS Book co-authors say lithium will not be king forever, with '
                                   'sodium-ion coming',
                                   'ALL4 Environmental Consultants ([-B0ACVnCSu0 @ 00:59:59]); SunCast '
                                   'Media ([eynQ4qifTao @ 00:25:31])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ["Rand Simulation's Chris Smith documents the thermal failure that equipment "
                              'suppliers never see, because each supplier designs in isolation while '
                              '100-400 grouped units behave differently. The runaway loop is mechanical: a '
                              '45°C intake yields 55°C exhaust, and at 50% reingestion the intake climbs '
                              'to 50°C and the exhaust to 60°C, driving derate, then thermal runaway and '
                              'fire [LBt7MoTnFFQ @ 00:21:35]. In the Fort Stockton case of about 320 '
                              'containers, the worst condition was not calm air but a 7 mph southeast wind '
                              'that left about 50% of units derated, while winds of 12-20 mph refreshed '
                              'the aisles. Smith treats anything above a couple of percentage points '
                              'derated as adverse [LBt7MoTnFFQ @ 00:24:43]. The fix was 70° louvers on the '
                              'HVAC exhausts, with a check on fan pressure margin. It pulled aisles to '
                              '51-53°C against a 54°C intake threshold and shifted the temperature '
                              'histogram left, with less compressor wear [LBt7MoTnFFQ @ 00:27:17]. The '
                              'Civil and Structural Engineer channel reports the dirt-level version of the '
                              'same trap: ponding after minimal rain, and roads fracturing before the '
                              'battery is even connected, because the maximum structural stress on the '
                              'ground lands during the temporary construction phase [935Rt3dBZso @ '
                              "00:09:43]. The channel's blunt rule: if water gathers beneath high voltage "
                              'equipment, the facility fails.',
                              "Keentel's Sandeep Sunny Patel names the protection trap. BESS fault current "
                              'is software-limited, so conventional overcurrent protection fails and '
                              'directional or differential schemes are required [BTkszCEW7nY @ 00:03:16]. '
                              "Patel's verdict on teams that skip the studies is that they deferred risk "
                              'without pricing it. On weak, low-SCR grids the PLL itself can lose '
                              'stability, which is why EMT modeling is required [BTkszCEW7nY @ 00:03:55]. '
                              "Lyten's JP shows the grid-side bill. PSUs and UPSs disconnect at the first "
                              'voltage dip, one fault drops about 1,500 MW, and NERC issued a Level 3 '
                              'alert covering events above 1,000 MW, because protection that makes sense '
                              'inside the building can create a risk for everyone outside of it '
                              '[7h6DABJ_xgs @ 00:05:51]. Australian Control Engineering reports the '
                              'integration failures that surface late on real sites: overseas suppliers '
                              'misaligned with Australian standards, SCADA limits on data volume and '
                              'retention, AEMO DNP3 event-transmission problems with buffer overflow, and '
                              "distributed SCADA complexity [8eadjA6Pqyo @ 00:00:20]. Patel's "
                              'countermeasure is to secure validated models before the purchase order and '
                              'run a physical test loop of baseline, full envelope, statistics and repeat. '
                              'FlexGen adds that without orchestration, co-located assets compete for '
                              'inverter capacity.',
                              'The post-fire phase is where budgets break. The ALL4 panel reports that '
                              'without a post-incident plan, costs have gone from thousands to millions of '
                              'dollars. The fire department will not release a site until a cleanup lead '
                              'and a safety person are on site, sometimes with a firewatch carrying a '
                              'temperature gun [-B0ACVnCSu0 @ 00:44:14]. Stranded energy drives '
                              "reignition, so the panel's guidance is to pack damaged cells in steel drums "
                              "and let them sit before transport [-B0ACVnCSu0 @ 00:44:47]. RavenVolt's "
                              'Daniel Hudson adds the electrocution trap: burning systems still hold '
                              'stranded energy, water-soaked breakers stop isolating, Hudson knows of no '
                              'automatic discharge method, and the smoke is very toxic [biJIJcXR5mE @ '
                              "00:33:29]. UL Solutions' LaTanya Schwab sets the price of proving a design "
                              'before any of that happens. The installation-level test now requires a '
                              'fully populated enclosure of live cells, often hundreds, at the real '
                              'separation distance, with the thermal runaway prevention system deactivated '
                              'in the enclosure of origin. About one day of testing takes about two weeks '
                              "of preparation [TtbHyJ6xzNg @ 00:14:05]. Orange County Fire Authority's "
                              'Robert closes the loop from the permit desk. Without a UL 9540 listing or '
                              'full-scale fire test there is no approval, and a manufacturer that bans '
                              'indoor installation is a showstopper.'],
               'table': {'caption': 'Firsthand Failure Modes and Economics Checks for Data Center BESS',
                         'headers': ['Failure Mode',
                                     'Mechanism Reported',
                                     'Economic or Operational Hit',
                                     'Expert Source'],
                         'rows': [['Exhaust reingestion across container aisles',
                                   'A 45°C intake becomes 55°C exhaust, climbing to 60°C at 50% '
                                   'reingestion',
                                   'About 50% of roughly 320 units derated in a 7 mph southeast wind',
                                   'Rand Simulation ([LBt7MoTnFFQ @ 00:21:35])'],
                                  ['Equipment designed in isolation by suppliers',
                                   'Inverters sit 3-8 ft apart and 10 ft from containers, in groups of '
                                   '100-400',
                                   'Remediation can cost millions, take months, and lose money for 5-10 '
                                   'years',
                                   'Rand Simulation ([LBt7MoTnFFQ @ 00:11:59])'],
                                  ['Underdesigned civil drainage and pavement',
                                   'Ponding after minimal rain, with construction-phase loads exceeding '
                                   'pavement design',
                                   'Roads fracture before the battery is even connected to the grid',
                                   'Civil and Structural Engineer ([935Rt3dBZso @ 00:09:43])'],
                                  ['Protection blind to software-limited fault current',
                                   'Overcurrent relays fail because the inverter limits its own fault '
                                   'current in software',
                                   'Directional or differential protection is required, and skipped '
                                   'studies defer unpriced risk',
                                   'Keentel Engineering ([BTkszCEW7nY @ 00:03:16])'],
                                  ['Mass ride-through trip of data center load',
                                   'PSUs and UPSs disconnect at the first voltage dip, dropping about '
                                   '1,500 MW',
                                   'NERC Level 3 alert covering events above 1,000 MW since 2022',
                                   'Volta Foundation ([7h6DABJ_xgs @ 00:05:51])'],
                                  ['SCADA and telemetry integration breakdown',
                                   'Overseas suppliers misaligned with Australian standards, plus AEMO '
                                   'DNP3 buffer overflow',
                                   'Late rework on data volume, retention and distributed SCADA complexity',
                                   'Australian Control Engineering | Smart Utilities ([8eadjA6Pqyo @ '
                                   '00:00:20])'],
                                  ['No post-incident plan after a battery fire',
                                   'Stranded energy reignites cells, and the site is held until a cleanup '
                                   'lead and safety person arrive',
                                   'Costs escalate from thousands to millions of dollars per incident',
                                   'ALL4 Environmental Consultants ([-B0ACVnCSu0 @ 00:44:14])'],
                                  ['Transformer procurement delay on BESS builds',
                                   'Transformers are the chronic delay, and suppliers demand pay me now',
                                   'Owners carry delivery risk from contract negotiation onward',
                                   'Fire Protection Engineering Podcast ([biJIJcXR5mE @ 00:19:16])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Pre-Energization Kill Switches',
                           'body': 'Practitioners lost money, permits or whole sites on each of these. '
                                   'Clear all four before committing capital to a BESS-backed data center '
                                   'build.',
                           'items': ['Run full-site airflow simulation at 30% and 60% design, and test the '
                                     'worst-case moderate wind rather than calm air, before freezing the '
                                     'container layout [Rand Simulation — LBt7MoTnFFQ @ 00:14:15].',
                                     'Confirm the UL 9540 listing and full-scale fire test data exist, and '
                                     'that the manufacturer allows the planned indoor or outdoor '
                                     'installation [ALL4 Environmental Consultants — -B0ACVnCSu0 @ '
                                     '00:18:02].',
                                     'Obtain validated inverter models and run EMT and harmonic studies, '
                                     'with compliance measured as TDD at the PCC, before the purchase '
                                     'order [Keentel Engineering — BTkszCEW7nY @ 00:00:17].',
                                     'Write the post-incident plan before energization, naming a cleanup '
                                     'lead and safety person and covering steel-drum handling of cells '
                                     'holding stranded energy [ALL4 Environmental Consultants — '
                                     '-B0ACVnCSu0 @ 00:44:47].']}}],
 'pull_quote': '"So the key idea is that protection that makes sense inside the building can create a risk '
               'for everyone outside of it." — Volta Foundation (7h6DABJ_xgs @ 00:05:51).',
 'diagram_id': 'diag-06',
 'action_checklist': ['Screen zoning first, then scale. Budget months for a conditional use permit and a '
                      'year or more for utility approval [ALL4 Environmental Consultants — -B0ACVnCSu0 @ '
                      '00:20:16].',
                      'Size bridge power so it transitions into permanent service without being ripped out '
                      'later, and stop buying the cheapest [The POWER Podcast — Ic-Cuo3Xdfo @ 00:25:16].',
                      'Target upstream breaker opening times below half a second so the grid-forming BESS '
                      'can pick up full load within 20 milliseconds [Digital Infrastructure Network — '
                      'U2apRbTTZuE @ 00:09:02].',
                      'Route firewater through a smart valve to a retention pond sized for the full '
                      'firewater tank volume plus 0.3 m freeboard [Civil and Structural Engineer — '
                      '935Rt3dBZso @ 00:05:32].',
                      'Buy switchgear with digital components from the start, and link the storage OS to '
                      'the building management system with cybersecurity [Digital Infrastructure Network — '
                      'U2apRbTTZuE @ 00:16:29].',
                      'Run the battery as a shock absorber so the utility sees a smaller, stabilized load, '
                      'which could bring approvals years earlier [FlexGen — LhqvSN3OdlI @ 00:02:44].'],
 'statutory_citations': [{'title': 'Volta Foundation — Battery Forum: Grid-Forming BESS Architectures for '
                                   'AI Data Center Power Quality with Lyten [00:05:51]',
                          'url': 'https://www.youtube.com/watch?v=7h6DABJ_xgs&t=351s',
                          'relevance': 'Primary practitioner testimony on mass ride-through trips of data '
                                       'center load and on grid-forming BESS smoothing at the '
                                       'interconnection.'},
                         {'title': 'UL Solutions — Understanding BESS Fire Testing for Data Centers | TCA '
                                   '18 [00:09:13]',
                          'url': 'https://www.youtube.com/watch?v=TtbHyJ6xzNg&t=553s',
                          'relevance': 'Primary practitioner testimony on UL 9540A 6th edition '
                                       'installation-level testing with fully populated live-cell '
                                       'enclosures.'},
                         {'title': 'ALL4 Environmental Consultants — Battery Energy Storage Systems BESS '
                                   'Considerations for Data Centers [00:44:14]',
                          'url': 'https://www.youtube.com/watch?v=-B0ACVnCSu0&t=2654s',
                          'relevance': 'Primary practitioner testimony on post-incident costs, '
                                       'stranded-energy reignition and fire authority release conditions.'},
                         {'title': 'Rand Simulation — Leveraging Simulation for BESS & Data Center Sites '
                                   '[00:21:35]',
                          'url': 'https://www.youtube.com/watch?v=LBt7MoTnFFQ&t=1295s',
                          'relevance': 'Primary practitioner testimony on exhaust reingestion, derating '
                                       'and the thermal runaway loop across BESS container fields.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'U2apRbTTZuE',
                       'title': 'Sustainable Data Centers: microgrid-enabled and battery energy storage '
                                'powered systems',
                       'channel': 'Digital Infrastructure Network',
                       'author': 'Digital Infrastructure Network',
                       'text': 'One of the key values of the BESS is that, opposite to a genset which '
                               'stands idle 99% of the time, the BESS can provide additional services for '
                               'the grid.',
                       'tip': 'One of the key values of the BESS is that, opposite to a genset which '
                              'stands idle 99% of the time, the BESS can provide additional services for '
                              'the grid.',
                       'timestamp': 309,
                       'timestamp_seconds': 309,
                       'timestamp_label': '[00:05:09]',
                       'url': 'https://www.youtube.com/watch?v=U2apRbTTZuE&t=309s',
                       'markdown': '[00:05:09](https://www.youtube.com/watch?v=U2apRbTTZuE&t=309s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'U2apRbTTZuE',
                       'title': 'Sustainable Data Centers: microgrid-enabled and battery energy storage '
                                'powered systems',
                       'channel': 'Digital Infrastructure Network',
                       'author': 'Digital Infrastructure Network',
                       'text': 'So the energy storage can pick up a load within 20 milliseconds at full '
                               'load.',
                       'tip': 'So the energy storage can pick up a load within 20 milliseconds at full '
                              'load.',
                       'timestamp': 525,
                       'timestamp_seconds': 525,
                       'timestamp_label': '[00:08:45]',
                       'url': 'https://www.youtube.com/watch?v=U2apRbTTZuE&t=525s',
                       'markdown': '[00:08:45](https://www.youtube.com/watch?v=U2apRbTTZuE&t=525s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '7h6DABJ_xgs',
                       'title': 'Battery Forum: Grid-Forming BESS Architectures for AI Data Center Power '
                                'Quality with Lyten',
                       'channel': 'Volta Foundation',
                       'author': 'Volta Foundation',
                       'text': 'So the key idea is that protection that makes sense inside the building '
                               'can create a risk for everyone outside of it.',
                       'tip': 'So the key idea is that protection that makes sense inside the building can '
                              'create a risk for everyone outside of it.',
                       'timestamp': 351,
                       'timestamp_seconds': 351,
                       'timestamp_label': '[00:05:51]',
                       'url': 'https://www.youtube.com/watch?v=7h6DABJ_xgs&t=351s',
                       'markdown': '[00:05:51](https://www.youtube.com/watch?v=7h6DABJ_xgs&t=351s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '7h6DABJ_xgs',
                       'title': 'Battery Forum: Grid-Forming BESS Architectures for AI Data Center Power '
                                'Quality with Lyten',
                       'channel': 'Volta Foundation',
                       'author': 'Volta Foundation',
                       'text': 'So they can only be solved at the grid interconnection.',
                       'tip': 'So they can only be solved at the grid interconnection.',
                       'timestamp': 1267,
                       'timestamp_seconds': 1267,
                       'timestamp_label': '[00:21:07]',
                       'url': 'https://www.youtube.com/watch?v=7h6DABJ_xgs&t=1267s',
                       'markdown': '[00:21:07](https://www.youtube.com/watch?v=7h6DABJ_xgs&t=1267s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'TtbHyJ6xzNg',
                       'title': 'Understanding BESS Fire Testing for Data Centers | TCA 18',
                       'channel': 'UL Solutions',
                       'author': 'UL Solutions',
                       'text': 'And the large-scale fire test involves the intentional ignition of gases '
                               'that are vented from lithium-ion batteries during a thermal runaway event.',
                       'tip': 'And the large-scale fire test involves the intentional ignition of gases '
                              'that are vented from lithium-ion batteries during a thermal runaway event.',
                       'timestamp': 178,
                       'timestamp_seconds': 178,
                       'timestamp_label': '[00:02:58]',
                       'url': 'https://www.youtube.com/watch?v=TtbHyJ6xzNg&t=178s',
                       'markdown': '[00:02:58](https://www.youtube.com/watch?v=TtbHyJ6xzNg&t=178s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'TtbHyJ6xzNg',
                       'title': 'Understanding BESS Fire Testing for Data Centers | TCA 18',
                       'channel': 'UL Solutions',
                       'author': 'UL Solutions',
                       'text': 'All of your safeguards have failed and there is a fire that is happening '
                               'in the BESS.',
                       'tip': 'All of your safeguards have failed and there is a fire that is happening in '
                              'the BESS.',
                       'timestamp': 737,
                       'timestamp_seconds': 737,
                       'timestamp_label': '[00:12:17]',
                       'url': 'https://www.youtube.com/watch?v=TtbHyJ6xzNg&t=737s',
                       'markdown': '[00:12:17](https://www.youtube.com/watch?v=TtbHyJ6xzNg&t=737s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '-B0ACVnCSu0',
                       'title': 'Battery Energy Storage Systems BESS Considerations for Data Centers',
                       'channel': 'ALL4 Environmental Consultants',
                       'author': 'ALL4 Environmental Consultants',
                       'text': 'But firefighters are not going to go into a burning building to save a '
                               'BESS unit.',
                       'tip': 'But firefighters are not going to go into a burning building to save a BESS '
                              'unit.',
                       'timestamp': 2440,
                       'timestamp_seconds': 2440,
                       'timestamp_label': '[00:40:40]',
                       'url': 'https://www.youtube.com/watch?v=-B0ACVnCSu0&t=2440s',
                       'markdown': '[00:40:40](https://www.youtube.com/watch?v=-B0ACVnCSu0&t=2440s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '935Rt3dBZso',
                       'title': 'Civil Engineering Design for Battery Energy Storage Systems (BESS) in '
                                'Australia',
                       'channel': 'Civil and Structural Engineer',
                       'author': 'Civil and Structural Engineer',
                       'text': 'If water gathers beneath high voltage equipment, the facility fails.',
                       'tip': 'If water gathers beneath high voltage equipment, the facility fails.',
                       'timestamp': 190,
                       'timestamp_seconds': 190,
                       'timestamp_label': '[00:03:10]',
                       'url': 'https://www.youtube.com/watch?v=935Rt3dBZso&t=190s',
                       'markdown': '[00:03:10](https://www.youtube.com/watch?v=935Rt3dBZso&t=190s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '935Rt3dBZso',
                       'title': 'Civil Engineering Design for Battery Energy Storage Systems (BESS) in '
                                'Australia',
                       'channel': 'Civil and Structural Engineer',
                       'author': 'Civil and Structural Engineer',
                       'text': 'The absolute maximum structural stress inflicted on the ground occurs '
                               'during the temporary construction phase.',
                       'tip': 'The absolute maximum structural stress inflicted on the ground occurs '
                              'during the temporary construction phase.',
                       'timestamp': 464,
                       'timestamp_seconds': 464,
                       'timestamp_label': '[00:07:44]',
                       'url': 'https://www.youtube.com/watch?v=935Rt3dBZso&t=464s',
                       'markdown': '[00:07:44](https://www.youtube.com/watch?v=935Rt3dBZso&t=464s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'LBt7MoTnFFQ',
                       'title': 'Leveraging Simulation for BESS & Data Center Sites',
                       'channel': 'Rand Simulation',
                       'author': 'Rand Simulation',
                       'text': 'A 45 degree intake produces 55 degree exhaust, and at 50% reingestion the '
                               'intake reaches 50 and the exhaust 60, which leads to derate, then thermal '
                               'runaway and fire.',
                       'tip': 'A 45 degree intake produces 55 degree exhaust, and at 50% reingestion the '
                              'intake reaches 50 and the exhaust 60, which leads to derate, then thermal '
                              'runaway and fire.',
                       'timestamp': 1295,
                       'timestamp_seconds': 1295,
                       'timestamp_label': '[00:21:35]',
                       'url': 'https://www.youtube.com/watch?v=LBt7MoTnFFQ&t=1295s',
                       'markdown': '[00:21:35](https://www.youtube.com/watch?v=LBt7MoTnFFQ&t=1295s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '8eadjA6Pqyo',
                       'title': 'BESS Site Visit: SCADA Integration & Delivery Lessons',
                       'channel': 'Australian Control Engineering | Smart Utilities',
                       'author': 'Australian Control Engineering | Smart Utilities',
                       'text': 'Consult early to eliminate risks early.',
                       'tip': 'Consult early to eliminate risks early.',
                       'timestamp': 70,
                       'timestamp_seconds': 70,
                       'timestamp_label': '[00:01:10]',
                       'url': 'https://www.youtube.com/watch?v=8eadjA6Pqyo&t=70s',
                       'markdown': '[00:01:10](https://www.youtube.com/watch?v=8eadjA6Pqyo&t=70s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'WnjqDbowqy0',
                       'title': 'Phinergy and Rosendin Unlock New Grid Capacity for Data Centers',
                       'channel': 'IVY Press Room',
                       'author': 'IVY Press Room',
                       'text': 'If data centers reduced grid demand for just 1% of annual hours, the grid '
                               'could add up to 70 GW without a single grid upgrade.',
                       'tip': 'If data centers reduced grid demand for just 1% of annual hours, the grid '
                              'could add up to 70 GW without a single grid upgrade.',
                       'timestamp': 36,
                       'timestamp_seconds': 36,
                       'timestamp_label': '[00:00:36]',
                       'url': 'https://www.youtube.com/watch?v=WnjqDbowqy0&t=36s',
                       'markdown': '[00:00:36](https://www.youtube.com/watch?v=WnjqDbowqy0&t=36s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'LhqvSN3OdlI',
                       'title': 'Powering the AI Boom: Co-locating Batteries with Data Centers',
                       'channel': 'FlexGen',
                       'author': 'FlexGen',
                       'text': 'These are power demands that spike from zero to 100% and back again in '
                               'milliseconds.',
                       'tip': 'These are power demands that spike from zero to 100% and back again in '
                              'milliseconds.',
                       'timestamp': 92,
                       'timestamp_seconds': 92,
                       'timestamp_label': '[00:01:32]',
                       'url': 'https://www.youtube.com/watch?v=LhqvSN3OdlI&t=92s',
                       'markdown': '[00:01:32](https://www.youtube.com/watch?v=LhqvSN3OdlI&t=92s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'BTkszCEW7nY',
                       'title': 'BESS for Data Centers: Power Quality, Harmonics & Grid Stability '
                                'Explained | Keentel Engineering',
                       'channel': 'Keentel Engineering',
                       'author': 'Keentel Engineering',
                       'text': 'A blindly placed filter might just push the resonance to a worse '
                               'frequency.',
                       'tip': 'A blindly placed filter might just push the resonance to a worse frequency.',
                       'timestamp': 137,
                       'timestamp_seconds': 137,
                       'timestamp_label': '[00:02:17]',
                       'url': 'https://www.youtube.com/watch?v=BTkszCEW7nY&t=137s',
                       'markdown': '[00:02:17](https://www.youtube.com/watch?v=BTkszCEW7nY&t=137s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Ic-Cuo3Xdfo',
                       'title': '219. Spiky AI Loads Are Forcing a Rethink of Data Center Power',
                       'channel': 'The POWER Podcast',
                       'author': 'The POWER Podcast',
                       'text': 'Stop buying the cheapest.',
                       'tip': 'Stop buying the cheapest.',
                       'timestamp': 1517,
                       'timestamp_seconds': 1517,
                       'timestamp_label': '[00:25:17]',
                       'url': 'https://www.youtube.com/watch?v=Ic-Cuo3Xdfo&t=1517s',
                       'markdown': '[00:25:17](https://www.youtube.com/watch?v=Ic-Cuo3Xdfo&t=1517s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'oHZCEiu2Vc8',
                       'title': 'B E S S  Battery Energy Storage Systems and the Grid',
                       'channel': 'Chris Heasley',
                       'author': 'Chris Heasley',
                       'text': 'Seventy-two percent of failures occur at interconnection.',
                       'tip': 'Seventy-two percent of failures occur at interconnection.',
                       'timestamp': 1732,
                       'timestamp_seconds': 1732,
                       'timestamp_label': '[00:28:52]',
                       'url': 'https://www.youtube.com/watch?v=oHZCEiu2Vc8&t=1732s',
                       'markdown': '[00:28:52](https://www.youtube.com/watch?v=oHZCEiu2Vc8&t=1732s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'eynQ4qifTao',
                       'title': 'Required Reading For Battery Technology? The BESS Book: Utility-Scale '
                                'Battery Energy Storage Systems',
                       'channel': 'SunCast Media',
                       'author': 'SunCast Media',
                       'text': "We've broken the $100 kilowatt hour at the cell level.",
                       'tip': "We've broken the $100 kilowatt hour at the cell level.",
                       'timestamp': 3378,
                       'timestamp_seconds': 3378,
                       'timestamp_label': '[00:56:18]',
                       'url': 'https://www.youtube.com/watch?v=eynQ4qifTao&t=3378s',
                       'markdown': '[00:56:18](https://www.youtube.com/watch?v=eynQ4qifTao&t=3378s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'biJIJcXR5mE',
                       'title': 'BESS Design-Build Best Practices with Daniel Hudson',
                       'channel': 'Fire Protection Engineering Podcast',
                       'author': 'Fire Protection Engineering Podcast',
                       'text': 'I mean, the smoke is very toxic.',
                       'tip': 'I mean, the smoke is very toxic.',
                       'timestamp': 2240,
                       'timestamp_seconds': 2240,
                       'timestamp_label': '[00:37:20]',
                       'url': 'https://www.youtube.com/watch?v=biJIJcXR5mE&t=2240s',
                       'markdown': '[00:37:20](https://www.youtube.com/watch?v=biJIJcXR5mE&t=2240s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'}]}
