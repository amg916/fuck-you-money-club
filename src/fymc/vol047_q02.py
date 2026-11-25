from __future__ import annotations

CHAPTER_2 = {'id': 'Q2',
 'chapter_id': 'Q2',
 'chapter_number': 2,
 'question_number': 2,
 'slug': 'hyperscale-ai-load-scale-build-economics-power-scarcity',
 'question_prompt': 'How big are AI hyperscale loads, why are facilities short on power, and what drives '
                    'their build economics, delays, and cancellations?',
 'kicker': 'Q2 / THE BIG MONEY PLAYBOOKS',
 'title': 'Hyperscale AI Load: Scale, Build Economics and Power Scarcity',
 'subtitle': 'City-sized campus loads, the rural shift, hyperscale fundamentals and design types, PUE '
             'overhead, long-lead gear and ground prep, modular manufacturing, occupancy economics, '
             'financing, team building, and project delays and cancellations',
 'layout_template': 'executive_summary',
 'reading_time_minutes': 15,
 'executive_summary': 'Practitioners converge on one thesis: power, not chips or buildings, is the scarce '
                      'input. AI racks have jumped from about 10 kW to 120-140 kW, single campuses draw '
                      '1-2 GW, and buildings that go up in 18 months to 3 years wait 4-5 years for grid '
                      'connection while large transformers sit at 3-4 year lead times. The street '
                      'mechanics follow: buy grid-connected or behind-the-meter sites, order long-lead '
                      'electrical gear immediately, price capacity per megawatt at $100-150/kW/month, '
                      'budget $7-12M/MW for the build before roughly $25M/MW of AI fit-out, and lock '
                      'take-or-pay leases of 10-15 years. Disagreements are sharp: queue sizes in Texas '
                      'range from 232 GW to over 400 GW, turbine waits from 2-3 years to more than 5, and '
                      'Economy Media reports over half of projects canceled or delayed while Hyper sees '
                      'years, if not decades, of pent-up demand.',
 'key_metrics': [{'label': 'AI rack power density',
                  'metric': 'AI rack power density',
                  'value': '120-140 kW per AI rack versus about 10 kW a decade ago (more than 10x)',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Rack-level draw jump that forces every link from power plant to rack to be '
                             'resized for day-one AI load.',
                  'source': 'The Power Engineer ([BWtk0CSPH6g @ 00:00:18])'},
                 {'label': 'Data center build cost per megawatt',
                  'metric': 'Data center build cost per megawatt',
                  'value': '$7-12M per MW; 10 MW over $100M; 100+ MW campus over $1B',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Baseline construction cost before 15-20% engineering fees and a 15-25% '
                             'contingency line.',
                  'source': 'Your Finance Uncle ([BXuRdYxfF2k @ 00:03:08])'},
                 {'label': 'Break-even utilization',
                  'metric': 'Break-even utilization',
                  'value': '60-65% utilization at about $150/kW/month plus 15% ancillary revenue',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Occupancy floor below which an owner-operator stops covering costs on a '
                             'roughly $200M build.',
                  'source': 'Your Finance Uncle ([BXuRdYxfF2k @ 00:09:33])'},
                 {'label': 'Annual cost of a 30 MW PUE gap',
                  'metric': 'Annual cost of a 30 MW PUE gap',
                  'value': 'About $26M per year at $0.10/kWh (PUE 1.5 versus PUE 1.2 on 100 MW of IT)',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Same 100 MW IT load drawing 150 MW at one site and 120 MW at another; '
                             'electricity is about half of opex.',
                  'source': 'BESS Engineer ([MnGAkKrZF_I @ 00:01:01])'}],
 'sections': [{'heading': '1. The Practitioner Consensus: Power Is the Product',
               'paragraphs': ['Every practitioner who touched the load question lands in the same place: '
                              'the bottleneck is power delivered to the right parcel on time, not chips '
                              'and not concrete. The Power Engineer frames the scale bluntly: one frontier '
                              'AI campus draws 1-2 GW, the output of one or two large power stations going '
                              'to a single customer at a single address, and an AI rack now pulls 120-140 '
                              'kW against about 10 kW a decade ago [BWtk0CSPH6g @ 00:00:00]. BUILT BENEATH '
                              "puts a name on it, citing Meta's roughly 1 GW Lebanon, Indiana site at "
                              'about 800,000 homes, running 24/7 rather than peaking like residential load '
                              '[7L7MfK9coTY @ 00:01:13]. Break Even reaches the same conclusion from the '
                              'money side, opening with the line that the most valuable thing inside a '
                              "data center isn't the servers and closing with 'own the power and you own "
                              "everything that runs on it' [gMNnJebMwzw @ 00:14:45]. Build Core's Josh "
                              'states the rural siting driver in one sentence: power availability is now '
                              'more important than location [tNNIXQhntOk @ 00:03:35]. The operator read is '
                              'simple. A hyperscale site is a power-delivery asset with a building wrapped '
                              'around it, and every downstream decision on land, gear, tenants and '
                              'financing hangs off how many megawatts can actually be energized and when.',
                              'The second point of agreement is the timing mismatch between the box and '
                              'the wire. The Power Engineer puts a data center at 1-3 years against 5-15 '
                              'years for a transmission line, notes that every link from plant to rack was '
                              'sized for loads that arrived slowly while an AI campus needs everything on '
                              'day one, and flags Texas sitting on more than 400 GW of large-load '
                              'requests, over 5x its record peak, most of which will never be built but '
                              'all of which must be studied [BWtk0CSPH6g @ 00:01:12]. BUILT BENEATH stacks '
                              'the numbers: IEA puts the build at 2-3 years, JLL puts the grid connection '
                              'wait in the largest markets at over 4 years, and DOE puts grid gear at 2+ '
                              "years and large transformers at 3-4 years, summed up as 'you can't download "
                              "another transformer' [7L7MfK9coTY @ 00:06:39]. Your Finance Uncle reports "
                              'Northern Virginia power waits pushing projects back 3-5 years and generator '
                              'lead times past 2 years [BXuRdYxfF2k @ 00:02:20]. The baseline prerequisite '
                              'follows directly: land and capital alone do not make a project. Mark Caskey '
                              'of Steel Nation sees developers with money in hand who still lack a '
                              'location, a client, natural gas and generator sets [ZcZ62ZBZTrA @ '
                              '00:00:19].',
                              'Practitioners also agree on what counts as hyperscale and what has to sit '
                              'on site before a megawatt earns revenue. Eaton sizes a typical data center '
                              'from about 1 MW, against 3-5 kW for a home, hosted customers at 5-10 kW, '
                              'and hyperscale sites at 50 to over 100 MW, with redundant utility feeds, '
                              'generators, UPS, BESS, cooling and network paths built in and most '
                              'hyperscale sites running Tier IV at 99.995%, under 30 minutes of downtime a '
                              'year [II6xdRkgivE @ 00:03:45]. datacenterHawk narrows the buyer pool to '
                              '5-20 cloud and SaaS/social companies operating as an oligopoly, contrasts a '
                              "bank's roughly 1 MW need with a cloud provider's roughly 36 MW, and relays "
                              "QTS's Tag Greason on what those buyers want: scale, speed and cost, in "
                              "leases of 10-75 MW [SVLPjGiZivc @ 00:15:31]. Build Core's Josh lists the "
                              'physical stack a developer has to deliver on a single campus: shell, GPU '
                              'data halls, transformers, switchgear and batteries, chillers, towers and '
                              'liquid cooling, diesel or gas backup, and the substation [tNNIXQhntOk @ '
                              '00:01:36]. The shared baseline: a hyperscale tenant buys energized, '
                              'redundant, cooled capacity tens of megawatts at a time, and the electrical '
                              'yard is the backbone of the product rather than an accessory to it.'],
               'table': {'caption': 'Where practitioners line up on hyperscale AI load, scale and power '
                                    'scarcity',
                         'headers': ['Consensus Point',
                                     'Practitioner Evidence',
                                     'Why It Matters On Site',
                                     'Expert Source'],
                         'rows': [['AI rack density has outrun legacy grid planning assumptions',
                                   'AI racks draw 120-140 kW versus about 10 kW a decade ago',
                                   'Every link from plant to rack must be resized for day-one load',
                                   'The Power Engineer ([BWtk0CSPH6g @ 00:00:18])'],
                                  ['Power availability now outranks location in site selection decisions',
                                   '67% of planned US data centers are rural; 39% sit in counties with '
                                   'none today',
                                   'Developers chase sites delivering 200+ MW inside 18-36 months',
                                   'Build Core ([tNNIXQhntOk @ 00:03:35])'],
                                  ['Transformers and grid gear set the hard schedule constraint',
                                   'DOE puts grid gear at 2+ years and large transformers at 3-4 years',
                                   "You can't download another transformer, so gear dictates the critical "
                                   'path',
                                   'BUILT BENEATH ([7L7MfK9coTY @ 00:06:39])'],
                                  ['Long-lead electrical, generator and cooling gear gets ordered at '
                                   'kickoff',
                                   'Procure gear, generators and cooling immediately; confirm substation '
                                   'readiness with the utility',
                                   'Order long lead items early to avoid schedule slippage',
                                   'MEP Engineer AJ ([lTK_pU1_uFc @ 00:06:19])'],
                                  ['Hyperscale demand is concentrated in a small buyer oligopoly',
                                   'Five to twenty cloud and SaaS/social companies drive all hyperscale '
                                   'demand',
                                   "One 50 MW lease equals 3-5% of Northern Virginia's 1,000-1,200 MW "
                                   'market',
                                   'datacenterHawk ([SVLPjGiZivc @ 00:03:52])'],
                                  ['Hyperscale sites run maximum redundancy and Tier IV uptime targets',
                                   'Most hyperscale sites are Tier IV at 99.995%, under 30 minutes '
                                   'downtime yearly',
                                   'Redundant feeds, generators, UPS, BESS and cooling paths are baseline '
                                   'scope',
                                   'Eaton ([II6xdRkgivE @ 00:05:53])'],
                                  ['Electricity dominates the ongoing cost of running any site',
                                   'Electricity is usually the largest ongoing cost, about half of opex '
                                   'per IDC',
                                   'Every PUE point converts directly into megawatts of capacity and '
                                   'dollars',
                                   'BESS Engineer ([MnGAkKrZF_I @ 00:01:21])']]}},
              {'heading': '2. Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['Build cost is now quoted per megawatt, and practitioners give hard ranges '
                              'for every layer of the stack. Your Finance Uncle prices construction at '
                              '$7-12M per MW, so a 10 MW site runs over $100M and a campus over 100 MW '
                              'runs over $1B, then layers engineering fees of 15-20% (about $30M on a '
                              '$200M build) and a 15-25% contingency on top [BXuRdYxfF2k @ 00:03:08]. '
                              "Break Even cites JLL's shell-and-core benchmark of $11.3M per MW, putting "
                              '50 MW past half a billion dollars, adds roughly $25M per MW for AI fit-out, '
                              'and pegs a 1 GW AI facility at $45-55B with Stargate projected at 1.2 GW '
                              'across more than 4M sq ft [gMNnJebMwzw @ 00:01:10]. Within the build '
                              'budget, electrical eats 40-45% and cooling 15-25%, and AI racks at 100+ kW '
                              'versus 5-10 kW traditionally force liquid cooling [gMNnJebMwzw @ 00:07:58]. '
                              'Economy Media frames component cost differently: electrical components run '
                              'under 10% of build cost, yet nothing runs without them, transformer prices '
                              'have doubled in just 4 years, and sourcing is concentrated in China, South '
                              'Korea and Mexico [e0Dlr07jfjA @ 00:07:34]. The operator takeaway: the '
                              'electrical line items, not the shell, decide whether the capital stack and '
                              'the schedule both hold.',
                              'Revenue mechanics run on the same per-megawatt unit. Break Even quotes '
                              'lease pricing at $100-150 per kW per month in primary US markets and points '
                              "to take-or-pay structures where tenants 'pay for what they reserved, "
                              "whether they use it or not,' citing Applied Digital's May 2026 deal: 300 "
                              'MW, a 15-year term, $7.5B base revenue and up to $18.2B with options '
                              '[gMNnJebMwzw @ 00:06:05]. Your Finance Uncle breaks the revenue stack into '
                              'space and power fees, cross-connects, metered power markup, remote hands '
                              'and managed services, with ancillary fees adding 10-15%, and runs the math: '
                              'at about $150/kW/month plus 15% ancillary, break-even sits at 60-65% '
                              'utilization [BXuRdYxfF2k @ 00:09:33]. The pricing rule that follows cuts '
                              'against instinct: when occupancy sags, hold price and lengthen terms rather '
                              'than cut the rate, because cutting price is often the worst move a '
                              'struggling operator can make [BXuRdYxfF2k @ 00:08:20]. On the opex side, '
                              'the BESS Engineer shows two sites with the same 100 MW of IT load drawing '
                              '150 MW and 120 MW; that 30 MW gap at $0.10/kWh is about $26M a year, and '
                              'under a 150 MW cap, PUE 1.2 supports 125 MW of IT, 25% more, provided '
                              'cooling holds at peak [MnGAkKrZF_I @ 00:01:01].',
                              'The speed-to-power playbook practitioners teach runs in three distinct '
                              'moves. First, buy power that already exists: BUILT BENEATH reports '
                              'developers targeting old steel mills and auto plants for their existing '
                              'power hookups, because the grid connection wait in the largest markets runs '
                              'over 4 years [7L7MfK9coTY @ 00:03:02]. Second, go behind the grid: Mark '
                              "Caskey's Steel Nation Microgrids, launched in November 2024, has six "
                              'behind-the-grid builds of 200-850 MW, mostly near Columbus, Ohio, where '
                              "permits clear in about 90 days versus '90 months' in Pennsylvania, and "
                              'redundant 28-40 inch gas lines put Ohio and Utah projects at power in 14-15 '
                              'months [ZcZ62ZBZTrA @ 00:16:36]. Caskey sizes 10-15 turbines for 200-300 '
                              'MW, notes recip engines top out around 5-6 MW, and says buying or leasing '
                              'naked turbines cuts 6-8 months off turbine waits of 2-3 years, running gas '
                              'as primary supply and BESS as backup [ZcZ62ZBZTrA @ 00:25:42]. Third, '
                              "compress the build once power is secured: Hyper's Matt Caldwell names power "
                              'and land as the true bottlenecks, then builds private manufacturing '
                              'capacity so clients never compete for slots on shared lines, arguing '
                              'repeatable factory QA beats one-off field commissioning and pulls time to '
                              'tenant revenue forward [oQVb9TRp6Og @ 00:01:25].'],
               'table': {'caption': 'Unit economics and execution numbers for hyperscale AI builds',
                         'headers': ['Mechanic or Number',
                                     'Exact Figure Stated',
                                     'How Operators Use It',
                                     'Expert Source'],
                         'rows': [['Hard build cost per megawatt of capacity',
                                   '$7-12M per MW; 10 MW over $100M; 100+ MW campus over $1B',
                                   'Baseline capex underwriting before engineering fees and contingency '
                                   'layers',
                                   'Your Finance Uncle ([BXuRdYxfF2k @ 00:03:08])'],
                                  ['Shell and core benchmark plus AI fit-out',
                                   'JLL benchmark of $11.3M per MW; 50 MW exceeds half a billion',
                                   'Add roughly $25M per MW of AI fit-out on top of the shell',
                                   'Break Even ([gMNnJebMwzw @ 00:01:10])'],
                                  ['Soft costs and contingency on a large build',
                                   'Engineering fees of 15-20%, about $30M on a $200M build',
                                   'Carry a separate 15-25% contingency line to absorb overruns',
                                   'Your Finance Uncle ([BXuRdYxfF2k @ 00:04:17])'],
                                  ['Primary-market lease pricing per kilowatt reserved',
                                   '$100-150 per kW per month in primary US markets',
                                   'Price reserved capacity under take-or-pay so tenants pay whether used '
                                   'or not',
                                   'Break Even ([gMNnJebMwzw @ 00:02:40])'],
                                  ['Break-even utilization for an owner-operator',
                                   '60-65% at about $150/kW/month plus 15% ancillary revenue',
                                   'Below this occupancy, hold price and lengthen lease terms instead of '
                                   'cutting',
                                   'Your Finance Uncle ([BXuRdYxfF2k @ 00:09:33])'],
                                  ['PUE efficiency gap on identical IT load',
                                   '30 MW gap at $0.10/kWh costs about $26M every year',
                                   'Under a 150 MW cap, PUE 1.2 supports 125 MW of IT load',
                                   'BESS Engineer ([MnGAkKrZF_I @ 00:01:01])'],
                                  ['Behind-the-grid gas turbine sizing and procurement',
                                   '10-15 turbines for 200-300 MW; recip engines top out at 5-6 MW',
                                   'Buy or lease naked turbines to cut 6-8 months off the wait',
                                   'Data Center Sales & Marketing Institute (DCSMI) ([ZcZ62ZBZTrA @ '
                                   '00:25:42])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Edges the operators actually use',
                           'body': 'Small moves practitioners use to win time, cut risk and stay bankable '
                                   'while everyone else waits on the grid.',
                           'items': ['Learn to read a load study and talk to a utility about connection '
                                     'timelines; those engineers are becoming some of the most valuable '
                                     'people in the industry because the bottleneck is no longer the chip '
                                     '[The Power Engineer — BWtk0CSPH6g @ 00:02:06].',
                                     'Bring the GC in during design for constructability reviews and value '
                                     'engineering, and lean on prefabricated modular components to speed '
                                     'the schedule and tighten quality control [MEP Engineer AJ — '
                                     'lTK_pU1_uFc @ 00:05:15].',
                                     "Ignore the 'site near railroads' advice for gas-fed builds: rail "
                                     'vibration harms pipelines, though rail corridors still suit fiber '
                                     '[Data Center Sales & Marketing Institute (DCSMI) — ZcZ62ZBZTrA @ '
                                     '00:19:27].',
                                     'On 1-2 GW sites carrying 4-5 electrical contractors, model full '
                                     'transparency with partners, down to shared access to accounting '
                                     'software [Beyond the Breaker Podcast — P6AUptGZBvI @ 00:09:37].']},
               'sop_steps': [{'step': 1,
                              'title': 'Lock speed-to-power before land',
                              'action': 'Screen only sites that can deliver more than 200 MW within 18-36 '
                                        'months.',
                              'detail': 'Build Core reports developers hunting sites with power inside '
                                        '18-36 months and more than 200 MW, with grid capacity booked '
                                        "through 2030; Hyper's Matt Caldwell names power and land as the "
                                        'two bottlenecks [Build Core — tNNIXQhntOk @ 00:04:36] [JSA TV: '
                                        'Tech & Telecom News — oQVb9TRp6Og @ 00:01:25].'},
                             {'step': 2,
                              'title': 'Order long-lead gear at kickoff',
                              'action': 'Place electrical gear, generator and cooling orders immediately '
                                        'and confirm substation readiness with the utility.',
                              'detail': 'MEP Engineer AJ says to procure electrical gear, generators and '
                                        'cooling immediately and coordinate directly with power providers '
                                        'on substation readiness; Your Finance Uncle flags generator lead '
                                        'times past 2 years [MEP Engineer AJ — lTK_pU1_uFc @ 00:06:19] '
                                        '[Your Finance Uncle — BXuRdYxfF2k @ 00:04:36].'},
                             {'step': 3,
                              'title': 'Underwrite cost per MW with every layer',
                              'action': 'Model $7-12M per MW, add 15-20% engineering fees and 15-25% '
                                        'contingency, then add AI fit-out separately.',
                              'detail': 'Your Finance Uncle sets the $7-12M per MW build range with fee '
                                        'and contingency layers; Break Even adds roughly $25M per MW for '
                                        'AI fit-out on top [Your Finance Uncle — BXuRdYxfF2k @ 00:03:08] '
                                        '[Break Even — gMNnJebMwzw @ 00:02:04].'},
                             {'step': 4,
                              'title': 'Price per kW, hold the rate, stretch the term',
                              'action': 'Quote $100-150/kW/month, target utilization above the 60-65% '
                                        'break-even, and trade rate cuts for longer terms.',
                              'detail': 'Break Even quotes $100-150/kW/month in primary markets; Your '
                                        'Finance Uncle says hold price and lengthen terms rather than cut; '
                                        'Travis Wofford of Baker Botts underwrites 10-15 year leases plus '
                                        'a 10-year renewal [Break Even — gMNnJebMwzw @ 00:02:40] [Your '
                                        'Finance Uncle — BXuRdYxfF2k @ 00:08:20] [Bloomberg Podcasts — '
                                        'cvNO9pZAhM0 @ 00:12:08].'}]},
              {'heading': 'Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['Every practitioner agrees the grid queue is the choke point, but the '
                              'numbers they quote for it do not line up, and that gap is itself the '
                              'signal. The Power Engineer puts Texas at more than 400 GW of large-load '
                              "requests, over five times the state's record peak, and says most will never "
                              'be built but all must still be studied [BWtk0CSPH6g @ 00:01:12]. BUILT '
                              'BENEATH reads the February 2026 ERCOT figure as 232,000 MW of proposed '
                              'large loads, 72% of it data centers, more than double the roughly 91 GW '
                              'record, with ERCOT answering through grouped studies and audits '
                              '[7L7MfK9coTY @ 00:05:28]. Travis Wofford of Baker Botts explains why the '
                              'totals swell: developers file five to ten duplicate applications, so the '
                              'queue overstates real demand, and Wofford recalls expecting 80% of it would '
                              'never be constructed [cvNO9pZAhM0 @ 00:44:06]. Timelines split the same '
                              'way. The Power Engineer quotes one to three years to build a data center '
                              'against five to fifteen for a transmission line, BUILT BENEATH cites two to '
                              'three years for the building, and Break Even compresses the contrast into '
                              'one line: building the box takes 18 months, getting the electricity can '
                              'take five years [gMNnJebMwzw @ 00:05:29]. Operators who underwrite on the '
                              'headline queue number are reading inflated paper.',
                              'The second split is how to get electrons at all. Mark Caskey of Steel '
                              'Nation runs a gas-first model: behind-the-grid builds of 200 to 850 MW, gas '
                              'as primary supply, BESS as backup, diesel frowned upon, and solar dismissed '
                              "as 'for show' at about 5 to 6% of supply [ZcZ62ZBZTrA @ 00:31:23]. Caskey "
                              'quotes turbine waits of two to three years and says buying or leasing naked '
                              'turbines cuts six to eight months, while BUILT BENEATH puts large gas '
                              'turbines at more than five years and lists modular behind-the-meter '
                              'turbines, batteries, solar or wind plus storage, and nuclear as parallel '
                              'workarounds [7L7MfK9coTY @ 00:07:52]. BUILT BENEATH also flags a brownfield '
                              'play, with developers targeting old steel mills and auto plants for their '
                              'existing power hookups. Wofford attacks the behind-the-meter thesis from '
                              'the financing side: if the data center leaves, the generation asset is '
                              'stranded [cvNO9pZAhM0 @ 00:42:32]. Siting advice splits too. Caskey rejects '
                              "the common 'site near railroads' rule because rail vibration harms gas "
                              'pipelines, while conceding rail corridors suit fiber [ZcZ62ZBZTrA @ '
                              '00:19:27]. The grid camp waits in the queue; the gas camp buys speed but '
                              'carries stranding and fuel-supply risk, and Caskey says roughly 99% of '
                              'developers asked Steel Nation to source the gas.',
                              'The sharpest divide is whether the build cycle is a bubble. Economy Media '
                              'opens with the claim that more than half of AI data center construction '
                              "projects worldwide are being canceled or delayed, sets Nvidia's roughly 10 "
                              "GW of GPUs shipped in 2025 against Goldman's count of only 7.7 GW of data "
                              "centers operating worldwide, and cites Heatmap's tally of 25 contracts "
                              'canceled in Q4 2025 and 99 of 770 planned sites contested [e0Dlr07jfjA @ '
                              "00:05:57]. Economy Media also reports Bloomberg's April 2026 story that "
                              "Oracle and OpenAI's flagship Texas data center postponed its expansion "
                              'plans. Matt Caldwell of Hyper rejects the bubble view outright, arguing '
                              "that moratoriums create pent-up demand worth 'years if not decades' "
                              '[oQVb9TRp6Og @ 00:04:02]. Break Even splits the difference with a timing '
                              'warning: inference is expected to overtake training around 2027, which '
                              'creates stranded-capacity risk [gMNnJebMwzw @ 00:10:04]. The financing desk '
                              'argues the same fight over tenants. Wofford walks through investment-grade '
                              'underwriting at 40 to 50% loan-to-value against 10 to 15 year leases plus a '
                              '10-year renewal, while Tracy Alloway doubts that tenant diversification is '
                              'real and flags a maturity mismatch [cvNO9pZAhM0 @ 00:45:16]. The bear case '
                              'counts cancellations and contested sites; the bull case reads moratoriums '
                              'as demand deferred rather than destroyed.'],
               'table': {'caption': 'Side-by-side practitioner conflicts on queue size, timelines, power '
                                    'stack, water and demand',
                         'headers': ['Contested Point', 'Position A', 'Position B', 'Expert Source'],
                         'rows': [['Size of the Texas large-load interconnection queue today',
                                   'More than 400 GW of requests, over five times record peak',
                                   '232,000 MW proposed in February 2026, 72% from data centers',
                                   'The Power Engineer ([BWtk0CSPH6g @ 00:01:12]) vs BUILT BENEATH '
                                   '([7L7MfK9coTY @ 00:05:28])'],
                                  ['How long the data center building itself takes',
                                   'One to three years against five to fifteen for transmission lines',
                                   'Building the box takes 18 months while electricity can take five years',
                                   'The Power Engineer ([BWtk0CSPH6g @ 00:01:12]) vs Break Even '
                                   '([gMNnJebMwzw @ 00:05:29])'],
                                  ['Lead time on gas turbines for behind-the-meter power',
                                   'Two to three years, and naked turbines cut six to eight months',
                                   'Large gas turbines take more than five years to arrive on site',
                                   'Data Center Sales & Marketing Institute (DCSMI) ([ZcZ62ZBZTrA @ '
                                   '00:12:16]) vs BUILT BENEATH ([7L7MfK9coTY @ 00:07:52])'],
                                  ['Water draw of a running hyperscale data center campus',
                                   'About 6,000 gallons per day per MW, with closed-loop losing little',
                                   "About two McDonald's stores a day, with the rest recycled on site",
                                   'Build Core ([tNNIXQhntOk @ 00:06:28]) vs Data Center Sales & Marketing '
                                   'Institute (DCSMI) ([ZcZ62ZBZTrA @ 00:44:07])'],
                                  ['Whether to site the campus near railroad corridors',
                                   'Common siting advice favors rail corridors, which also suit fiber '
                                   'routes',
                                   'Rail vibration harms gas pipelines, so Caskey rejects the rule '
                                   'outright',
                                   'Data Center Sales & Marketing Institute (DCSMI) ([ZcZ62ZBZTrA @ '
                                   '00:19:27]) disagreeing with common siting advice'],
                                  ['Role of solar and behind-the-meter generation in supply',
                                   'Solar is for show at 5-6%; run gas primary with BESS backup',
                                   'Behind-the-meter asset gets stranded if the data center tenant leaves',
                                   'Data Center Sales & Marketing Institute (DCSMI) ([ZcZ62ZBZTrA @ '
                                   '00:31:23]) vs Bloomberg Podcasts ([cvNO9pZAhM0 @ 00:42:32])'],
                                  ['Whether AI data center demand is a bubble now',
                                   'More than half of projects worldwide are canceled or delayed',
                                   'Moratoriums create pent-up demand worth years if not decades',
                                   'Economy Media ([e0Dlr07jfjA @ 00:00:00]) vs JSA TV: Tech & Telecom '
                                   'News ([oQVb9TRp6Og @ 00:04:02])']]}},
              {'heading': 'Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The failure that kills owners is utilization, not construction. Your '
                              'Finance Uncle runs the math at about $150 per kW per month plus 15% '
                              'ancillary revenue and lands break-even at 60 to 65% utilization '
                              '[BXuRdYxfF2k @ 00:09:33]. On a roughly $200M build, the optimistic case '
                              'reaches 75% utilization by year four and still pays back over more than a '
                              'decade; the realistic case loses one tenant, drops to 50% utilization, and '
                              'the site goes underwater [BXuRdYxfF2k @ 00:13:56]. The channel points to '
                              "Cyxtera's Chapter 11 filing in June 2023 as the live warning and names the "
                              'reflex that makes it worse: cutting price is often the worst move a '
                              'struggling operator can make, so hold the rate and lengthen terms instead '
                              '[BXuRdYxfF2k @ 00:08:20]. Break Even shows the hyperscale escape hatch, '
                              'take-or-pay leases where tenants pay for what they reserved whether they '
                              "use it or not, citing Applied Digital's 300 MW, 15-year deal at $7.5B base "
                              'revenue and up to $18.2B with options [gMNnJebMwzw @ 00:06:05]. Build cost '
                              'and contingency sit on top, per Your Finance Uncle: $7 to 12M per MW, '
                              'engineering fees of 15 to 20%, and 15 to 25% contingency. Ancillary fees '
                              'from cross-connects, metered power markup, remote hands and managed '
                              'services add only 10 to 15%.',
                              'Long-lead electrical gear is the second trap, and the speakers who touched '
                              'it converge: order early. MEP Engineer AJ warns to procure electrical gear, '
                              'generators and cooling immediately, coordinate directly with power '
                              'providers on substation readiness, and test soil and water early, because '
                              'long-lead items cause schedule slippage [lTK_pU1_uFc @ 00:06:19]. BUILT '
                              'BENEATH cites DOE lead times of two-plus years for grid gear and three to '
                              "four years for large transformers, summed up as 'you can't download another "
                              "transformer' [7L7MfK9coTY @ 00:06:39]. Economy Media adds the price side: "
                              'electrical components are under 10% of build cost but nothing runs without '
                              'them, transformer prices have doubled in four years, and sourcing runs '
                              'through China, South Korea and Mexico under tariff risk that includes a '
                              'threatened extra 100% on Chinese goods [e0Dlr07jfjA @ 00:07:34]. The result '
                              'is stockpiling, with companies buying cooling fans and power supply systems '
                              'just in case. Break Even reports transformers backordered for years and '
                              'nine of ten projects running late, while electrical alone eats 40 to 45% of '
                              'the build budget and cooling another 15 to 25% [gMNnJebMwzw @ 00:08:55]. '
                              "Your Finance Uncle puts generator lead times past two years. Hunt's Nathan "
                              'Heman lists the Suez Canal, the pandemic and Chinese New Year as recurring '
                              'lessons-learned surprises on hyperscale jobs.',
                              'The last traps live in the field and in the meter. Nathan Heman, project '
                              'executive at Hunt, prices waste at hyperscale: a 20-minute walk for 300 '
                              'workers costs about $30K a day, across six to seven days a week and two '
                              'shifts [P6AUptGZBvI @ 00:15:24]. Heman also warns that GMP contracts cap '
                              "the contractor's upside but not its losses, calling it 'a fine line', and "
                              'notes that on a 400-electrician site many foremen are running crews of six '
                              "to ten for the first time [P6AUptGZBvI @ 00:25:55]. Caskey's admitted "
                              "mistake at Steel Nation was chasing EPCMs and the 'Mag 8' instead of "
                              '20-year clients, and the lesson was to stay in your lane [ZcZ62ZBZTrA @ '
                              '00:39:17]. On the operating side, BESS Engineer shows the cost of a loose '
                              'PUE: with the same 100 MW of IT load, a site at PUE 1.5 draws 150 MW '
                              'against 120 MW at PUE 1.2, and that 30 MW gap at $0.10 per kWh runs about '
                              '$26M a year [MnGAkKrZF_I @ 00:01:01]. Under a 150 MW cap, PUE 1.2 supports '
                              '125 MW of IT, 25% more, if cooling holds at peak. Break Even adds that more '
                              'than 60% of outages trace to power, cooling or cabling, and missing the '
                              'Tier 4 standard of 99.995% triggers penalties.'],
               'table': {'caption': 'Firsthand failure modes with the numbers and countermoves '
                                    'practitioners reported',
                         'headers': ['Failure Mode',
                                     'Firsthand Number or Event',
                                     'Practitioner Countermove',
                                     'Expert Source'],
                         'rows': [['Utilization stalls below the break-even line for years',
                                   'Break-even at 60-65% utilization on $150/kW/month plus 15% ancillary',
                                   'Hold price and lengthen lease terms instead of cutting the rate',
                                   'Your Finance Uncle ([BXuRdYxfF2k @ 00:09:33])'],
                                  ['One tenant walks out of a roughly $200M build',
                                   'Utilization drops to 50% and the whole site goes underwater',
                                   'Underwrite the realistic case with 15-25% contingency built into '
                                   'budget',
                                   'Your Finance Uncle ([BXuRdYxfF2k @ 00:13:56])'],
                                  ['Transformers and grid gear ordered far too late',
                                   'Large transformers take three to four years; grid gear two-plus years',
                                   'Procure electrical gear, generators and cooling immediately after site '
                                   'selection',
                                   'BUILT BENEATH ([7L7MfK9coTY @ 00:06:39]) and MEP Engineer AJ '
                                   '([lTK_pU1_uFc @ 00:06:19])'],
                                  ['Imported electrical components hit by price and tariff shocks',
                                   'Transformer prices doubled in four years; extra 100% Chinese tariff '
                                   'threatened',
                                   'Companies stockpile cooling fans and power supply systems just in case',
                                   'Economy Media ([e0Dlr07jfjA @ 00:07:49])'],
                                  ['Field labor bleeding cash across a giant campus site',
                                   'A 20-minute walk for 300 workers costs about $30K per day',
                                   'Plan logistics early: warehouse lease, site vehicles, submittals and '
                                   'trailers',
                                   'Beyond the Breaker Podcast ([P6AUptGZBvI @ 00:15:24])'],
                                  ['Facility overhead eating power under a hard capacity cap',
                                   'A 30 MW PUE gap at $0.10/kWh costs about $26M per year',
                                   'Work airflow, cooling controls and conversion losses; track energy per '
                                   'task',
                                   'BESS Engineer ([MnGAkKrZF_I @ 00:01:01])'],
                                  ['Chasing the wrong customers in a hot power market',
                                   'Steel Nation chased EPCMs and the Mag 8 instead of 20-year clients',
                                   'Stay in your lane and serve gas owners on roughly 10-year deals',
                                   'Data Center Sales & Marketing Institute (DCSMI) ([ZcZ62ZBZTrA @ '
                                   '00:39:17])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Do Not Advance a Site Until These Four Checks Clear',
                           'body': 'Each check traces to a loss, delay or reversal a practitioner reported '
                                   'firsthand on hyperscale builds.',
                           'items': ['Model the one-tenant-exit case: on a roughly $200M build, losing a '
                                     'tenant drops utilization to 50% and puts the site underwater [Your '
                                     'Finance Uncle — BXuRdYxfF2k @ 00:13:56].',
                                     'Confirm long-lead orders are placed: large transformers take three '
                                     'to four years and grid gear two-plus years [BUILT BENEATH — '
                                     '7L7MfK9coTY @ 00:06:39].',
                                     'Price behind-the-meter stranding: if the data center leaves, the '
                                     'generation asset is stranded [Bloomberg Podcasts — cvNO9pZAhM0 @ '
                                     '00:42:32].',
                                     'Read the GMP terms before signing: GMP contracts cap upside but not '
                                     'losses [Beyond the Breaker Podcast — P6AUptGZBvI @ 00:25:55].']}}],
 'pull_quote': '"Own the power and you own everything that runs on it." — Break Even (gMNnJebMwzw @ '
               '00:14:45).',
 'diagram_id': 'diag-04',
 'action_checklist': ['Learn grid interconnection and load forecasting so you can read a load study and '
                      'talk to a utility about connection timelines [The Power Engineer — BWtk0CSPH6g @ '
                      '00:02:06].',
                      'Screen sites for high-capacity electrical feeds, multiple fiber backbones, '
                      'topography, flood risk and soil, then engage local authorities early on stormwater, '
                      'roads and interconnection permits [MEP Engineer AJ — lTK_pU1_uFc @ 00:03:01].',
                      'Target sites that can deliver more than 200 MW of power within 18 to 36 months, '
                      'including rural counties with room for substations and switchyards [Build Core — '
                      'tNNIXQhntOk @ 00:04:36].',
                      'If going behind the grid, plan 10 to 15 turbines for 200 to 300 MW and buy or lease '
                      'naked turbines to cut six to eight months [Data Center Sales & Marketing Institute '
                      '(DCSMI) — ZcZ62ZBZTrA @ 00:25:42].',
                      'Underwrite at about $150/kW/month plus 15% ancillary against a 60 to 65% '
                      'break-even, and hold price while lengthening terms [Your Finance Uncle — '
                      'BXuRdYxfF2k @ 00:09:33].',
                      'Sequence capital as development equity, then construction loan, then take-out, and '
                      'line up 10 to 15 year leases with a 10-year renewal [Bloomberg Podcasts — '
                      'cvNO9pZAhM0 @ 00:20:57].'],
 'statutory_citations': [{'title': 'The Power Engineer — AI Data Centre Load and Grid Impact — One Campus '
                                   "Uses a City's Power [00:01:12]",
                          'url': 'https://www.youtube.com/watch?v=BWtk0CSPH6g&t=72s',
                          'relevance': 'Primary practitioner testimony on transmission timing, the Texas '
                                       'large-load queue and data center cost impact on capacity '
                                       'auctions.'},
                         {'title': "Data Center Sales & Marketing Institute (DCSMI) — Why Big Tech Can't "
                                   'Build AI Data Centers Fast Enough [00:16:36]',
                          'url': 'https://www.youtube.com/watch?v=ZcZ62ZBZTrA&t=996s',
                          'relevance': 'Primary practitioner testimony on behind-the-grid gas builds of '
                                       '200-850 MW, Ohio 90-day permitting and 14-15 month time to power.'},
                         {'title': 'Bloomberg Podcasts — This Is What It Takes to Get a Data Center '
                                   'Financed | Odd Lots [00:18:41]',
                          'url': 'https://www.youtube.com/watch?v=cvNO9pZAhM0&t=1121s',
                          'relevance': 'Primary practitioner testimony on separate load and generation '
                                       'interconnection and five-year generation approval timelines.'},
                         {'title': 'Your Finance Uncle — The Economics of Owning a Data Center (Why 65% '
                                   'Full Means Bankrupt) [00:09:33]',
                          'url': 'https://www.youtube.com/watch?v=BXuRdYxfF2k&t=573s',
                          'relevance': 'Primary practitioner testimony on per-kW pricing, ancillary '
                                       'revenue and the 60-65% utilization break-even.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'BWtk0CSPH6g',
                       'title': "AI Data Centre Load and Grid Impact — One Campus Uses a City's Power",
                       'channel': 'The Power Engineer',
                       'author': 'The Power Engineer',
                       'text': 'The engineers who can read a load study and talk to a utility about '
                               'connection timelines are becoming some of the most valuable people in the '
                               'industry because the bottleneck is no longer the chip.',
                       'tip': 'The engineers who can read a load study and talk to a utility about '
                              'connection timelines are becoming some of the most valuable people in the '
                              'industry because the bottleneck is no longer the chip.',
                       'timestamp': 126,
                       'timestamp_seconds': 126,
                       'timestamp_label': '[00:02:06]',
                       'url': 'https://www.youtube.com/watch?v=BWtk0CSPH6g&t=126s',
                       'markdown': '[00:02:06](https://www.youtube.com/watch?v=BWtk0CSPH6g&t=126s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'lTK_pU1_uFc',
                       'title': 'Building Hyperscale Data Centers: Site Selection, Long-Lead Gear & Ground '
                                'Prep',
                       'channel': 'MEP Engineer AJ',
                       'author': 'MEP Engineer AJ',
                       'text': 'Order long lead items early to avoid schedule slippage.',
                       'tip': 'Order long lead items early to avoid schedule slippage.',
                       'timestamp': 379,
                       'timestamp_seconds': 379,
                       'timestamp_label': '[00:06:19]',
                       'url': 'https://www.youtube.com/watch?v=lTK_pU1_uFc&t=379s',
                       'markdown': '[00:06:19](https://www.youtube.com/watch?v=lTK_pU1_uFc&t=379s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'tNNIXQhntOk',
                       'title': 'Why AI Data Centers Are Heading to Rural America',
                       'channel': 'Build Core',
                       'author': 'Build Core',
                       'text': 'The first driver is that power availability is now more important than '
                               'location.',
                       'tip': 'The first driver is that power availability is now more important than '
                              'location.',
                       'timestamp': 215,
                       'timestamp_seconds': 215,
                       'timestamp_label': '[00:03:35]',
                       'url': 'https://www.youtube.com/watch?v=tNNIXQhntOk&t=215s',
                       'markdown': '[00:03:35](https://www.youtube.com/watch?v=tNNIXQhntOk&t=215s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '7L7MfK9coTY',
                       'title': 'Data Center Electricity: Why AI Facilities Are Short on Power',
                       'channel': 'BUILT BENEATH',
                       'author': 'BUILT BENEATH',
                       'text': "You can't download another transformer.",
                       'tip': "You can't download another transformer.",
                       'timestamp': 399,
                       'timestamp_seconds': 399,
                       'timestamp_label': '[00:06:39]',
                       'url': 'https://www.youtube.com/watch?v=7L7MfK9coTY&t=399s',
                       'markdown': '[00:06:39](https://www.youtube.com/watch?v=7L7MfK9coTY&t=399s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ZcZ62ZBZTrA',
                       'title': "Why Big Tech Can't Build AI Data Centers Fast Enough",
                       'channel': 'Data Center Sales & Marketing Institute (DCSMI)',
                       'author': 'Data Center Sales & Marketing Institute (DCSMI)',
                       'text': 'Getting natural gas into these locations is probably the hardest thing to '
                               'do.',
                       'tip': 'Getting natural gas into these locations is probably the hardest thing to '
                              'do.',
                       'timestamp': 713,
                       'timestamp_seconds': 713,
                       'timestamp_label': '[00:11:53]',
                       'url': 'https://www.youtube.com/watch?v=ZcZ62ZBZTrA&t=713s',
                       'markdown': '[00:11:53](https://www.youtube.com/watch?v=ZcZ62ZBZTrA&t=713s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ZcZ62ZBZTrA',
                       'title': "Why Big Tech Can't Build AI Data Centers Fast Enough",
                       'channel': 'Data Center Sales & Marketing Institute (DCSMI)',
                       'author': 'Data Center Sales & Marketing Institute (DCSMI)',
                       'text': 'The mistake was chasing EPCMs and the Mag 8 instead of 20-year clients, '
                               'and the lesson is to stay in your lane.',
                       'tip': 'The mistake was chasing EPCMs and the Mag 8 instead of 20-year clients, and '
                              'the lesson is to stay in your lane.',
                       'timestamp': 2357,
                       'timestamp_seconds': 2357,
                       'timestamp_label': '[00:39:17]',
                       'url': 'https://www.youtube.com/watch?v=ZcZ62ZBZTrA&t=2357s',
                       'markdown': '[00:39:17](https://www.youtube.com/watch?v=ZcZ62ZBZTrA&t=2357s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'II6xdRkgivE',
                       'title': 'Data center solutions: Types, design, and infrastructure explained | '
                                'Eaton PSEC',
                       'channel': 'Eaton',
                       'author': 'Eaton',
                       'text': 'Most hyperscale sites are Tier IV at 99.995%, which means under 30 minutes '
                               'of downtime a year.',
                       'tip': 'Most hyperscale sites are Tier IV at 99.995%, which means under 30 minutes '
                              'of downtime a year.',
                       'timestamp': 353,
                       'timestamp_seconds': 353,
                       'timestamp_label': '[00:05:53]',
                       'url': 'https://www.youtube.com/watch?v=II6xdRkgivE&t=353s',
                       'markdown': '[00:05:53](https://www.youtube.com/watch?v=II6xdRkgivE&t=353s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'BXuRdYxfF2k',
                       'title': 'The Economics of Owning a Data Center (Why 65% Full Means Bankrupt)',
                       'channel': 'Your Finance Uncle',
                       'author': 'Your Finance Uncle',
                       'text': 'This is why cutting price is often the worst move a struggling data center '
                               'operator can make.',
                       'tip': 'This is why cutting price is often the worst move a struggling data center '
                              'operator can make.',
                       'timestamp': 500,
                       'timestamp_seconds': 500,
                       'timestamp_label': '[00:08:20]',
                       'url': 'https://www.youtube.com/watch?v=BXuRdYxfF2k&t=500s',
                       'markdown': '[00:08:20](https://www.youtube.com/watch?v=BXuRdYxfF2k&t=500s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'MnGAkKrZF_I',
                       'title': 'Data Center PUE Explained: Same IT Load, 30 MW Less | AIDC Decoded Ep. 3',
                       'channel': 'BESS Engineer',
                       'author': 'BESS Engineer',
                       'text': 'That matters because electricity is usually the largest ongoing cost of '
                               'running a data center.',
                       'tip': 'That matters because electricity is usually the largest ongoing cost of '
                              'running a data center.',
                       'timestamp': 81,
                       'timestamp_seconds': 81,
                       'timestamp_label': '[00:01:21]',
                       'url': 'https://www.youtube.com/watch?v=MnGAkKrZF_I&t=81s',
                       'markdown': '[00:01:21](https://www.youtube.com/watch?v=MnGAkKrZF_I&t=81s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'oQVb9TRp6Og',
                       'title': 'How Modular Manufacturing Accelerates Data Center Deployment | Hyper',
                       'channel': 'JSA TV: Tech & Telecom News',
                       'author': 'JSA TV: Tech & Telecom News',
                       'text': 'Moratoriums create pent-up demand that could last years if not decades.',
                       'tip': 'Moratoriums create pent-up demand that could last years if not decades.',
                       'timestamp': 242,
                       'timestamp_seconds': 242,
                       'timestamp_label': '[00:04:02]',
                       'url': 'https://www.youtube.com/watch?v=oQVb9TRp6Og&t=242s',
                       'markdown': '[00:04:02](https://www.youtube.com/watch?v=oQVb9TRp6Og&t=242s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'SVLPjGiZivc',
                       'title': 'What is a Hyperscale Data Center? - Data Center Fundamentals - Data '
                                'Center Investing',
                       'channel': 'datacenterHawk',
                       'author': 'datacenterHawk',
                       'text': 'One hyperscale deal can absorb all of the available supply in a market.',
                       'tip': 'One hyperscale deal can absorb all of the available supply in a market.',
                       'timestamp': 1010,
                       'timestamp_seconds': 1010,
                       'timestamp_label': '[00:16:50]',
                       'url': 'https://www.youtube.com/watch?v=SVLPjGiZivc&t=1010s',
                       'markdown': '[00:16:50](https://www.youtube.com/watch?v=SVLPjGiZivc&t=1010s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Ayt6rLwGjYM',
                       'title': 'How Hyperscale Data Centers Work – The Factories Of The Digital World.',
                       'channel': 'Mini Leviathan',
                       'author': 'Mini Leviathan',
                       'text': 'Networking is a critical bottleneck inside a hyperscale data center.',
                       'tip': 'Networking is a critical bottleneck inside a hyperscale data center.',
                       'timestamp': 146,
                       'timestamp_seconds': 146,
                       'timestamp_label': '[00:02:26]',
                       'url': 'https://www.youtube.com/watch?v=Ayt6rLwGjYM&t=146s',
                       'markdown': '[00:02:26](https://www.youtube.com/watch?v=Ayt6rLwGjYM&t=146s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'gMNnJebMwzw',
                       'title': "The Real Product of a Data Center Isn't Data",
                       'channel': 'Break Even',
                       'author': 'Break Even',
                       'text': 'Own the power and you own everything that runs on it.',
                       'tip': 'Own the power and you own everything that runs on it.',
                       'timestamp': 885,
                       'timestamp_seconds': 885,
                       'timestamp_label': '[00:14:45]',
                       'url': 'https://www.youtube.com/watch?v=gMNnJebMwzw&t=885s',
                       'markdown': '[00:14:45](https://www.youtube.com/watch?v=gMNnJebMwzw&t=885s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'gMNnJebMwzw',
                       'title': "The Real Product of a Data Center Isn't Data",
                       'channel': 'Break Even',
                       'author': 'Break Even',
                       'text': 'They pay for what they reserved, whether they use it or not.',
                       'tip': 'They pay for what they reserved, whether they use it or not.',
                       'timestamp': 365,
                       'timestamp_seconds': 365,
                       'timestamp_label': '[00:06:05]',
                       'url': 'https://www.youtube.com/watch?v=gMNnJebMwzw&t=365s',
                       'markdown': '[00:06:05](https://www.youtube.com/watch?v=gMNnJebMwzw&t=365s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'e0Dlr07jfjA',
                       'title': 'Why Tech Companies Are Quietly Cancelling AI Data Centers',
                       'channel': 'Economy Media',
                       'author': 'Economy Media',
                       'text': 'Even if many of these companies do not currently need them, they buy them '
                               'just in case.',
                       'tip': 'Even if many of these companies do not currently need them, they buy them '
                              'just in case.',
                       'timestamp': 501,
                       'timestamp_seconds': 501,
                       'timestamp_label': '[00:08:21]',
                       'url': 'https://www.youtube.com/watch?v=e0Dlr07jfjA&t=501s',
                       'markdown': '[00:08:21](https://www.youtube.com/watch?v=e0Dlr07jfjA&t=501s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'P6AUptGZBvI',
                       'title': 'Building a Hyperscale Data Center Team',
                       'channel': 'Beyond the Breaker Podcast',
                       'author': 'Beyond the Breaker Podcast',
                       'text': 'What we do from a data center standpoint is not an individual sport.',
                       'tip': 'What we do from a data center standpoint is not an individual sport.',
                       'timestamp': 1008,
                       'timestamp_seconds': 1008,
                       'timestamp_label': '[00:16:48]',
                       'url': 'https://www.youtube.com/watch?v=P6AUptGZBvI&t=1008s',
                       'markdown': '[00:16:48](https://www.youtube.com/watch?v=P6AUptGZBvI&t=1008s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'cvNO9pZAhM0',
                       'title': 'This Is What It Takes to Get a Data Center Financed | Odd Lots',
                       'channel': 'Bloomberg Podcasts',
                       'author': 'Bloomberg Podcasts',
                       'text': 'And we were expecting 80% of that would never actually be constructed. '
                               'Only 20% of it would.',
                       'tip': 'And we were expecting 80% of that would never actually be constructed. Only '
                              '20% of it would.',
                       'timestamp': 0,
                       'timestamp_seconds': 0,
                       'timestamp_label': '[00:00:00]',
                       'url': 'https://www.youtube.com/watch?v=cvNO9pZAhM0&t=0s',
                       'markdown': '[00:00:00](https://www.youtube.com/watch?v=cvNO9pZAhM0&t=0s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'cvNO9pZAhM0',
                       'title': 'This Is What It Takes to Get a Data Center Financed | Odd Lots',
                       'channel': 'Bloomberg Podcasts',
                       'author': 'Bloomberg Podcasts',
                       'text': 'Behind-the-meter generation becomes a stranded asset if the data center '
                               'leaves.',
                       'tip': 'Behind-the-meter generation becomes a stranded asset if the data center '
                              'leaves.',
                       'timestamp': 2552,
                       'timestamp_seconds': 2552,
                       'timestamp_label': '[00:42:32]',
                       'url': 'https://www.youtube.com/watch?v=cvNO9pZAhM0&t=2552s',
                       'markdown': '[00:42:32](https://www.youtube.com/watch?v=cvNO9pZAhM0&t=2552s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'}]}
