from __future__ import annotations

CHAPTER_1 = {'id': 'Q1',
 'chapter_id': 'Q1',
 'chapter_number': 1,
 'question_number': 1,
 'slug': 'powered-land-site-qualification-data-center-land-deals',
 'question_prompt': 'What makes a parcel qualify as powered land for an AI data center, and how are those '
                    'land deals structured, optioned, and valued?',
 'kicker': 'Q1 / THE BIG MONEY PLAYBOOKS',
 'title': 'Powered Land: Site Qualification and Data Center Land Deals',
 'subtitle': 'Buildable acreage minimums, powered vs. unpowered land, CBRE and Thor site-selection '
             "criteria, land option contracts and site control, Stargate's $1 land option, powered shells, "
             'and West Texas powered-land plays',
 'layout_template': 'opportunity_overview',
 'reading_time_minutes': 15,
 'executive_summary': 'Practitioners from Thor Equities, datacenterHawk, CBRE, LandBridge, Foley & Lardner '
                      'and Zego converge on one rule: power is the site, and acreage follows. Site hunts '
                      'now start from available megawatts and work backward to land, fiber, water and gas. '
                      'The street numbers are blunt: 1MW per acre with a 100-acre floor, power run-outs at '
                      '$20M per mile and fiber at $2M, $30-100k non-refundable utility studies, about '
                      '$500k to rezone, and $22M posted upfront to lock power on one deal. Powered land '
                      'trades at 4-5x unpowered, and NoVA ground has hit $3-4M per acre. Developers '
                      "control dirt through option contracts, from 2-3 year solar options to Stargate's $1 "
                      'option. The split: LandBridge says go behind-the-meter on cheap Permian gas, while '
                      'Zego treats grid interconnection privilege itself as the asset.',
 'key_metrics': [{'label': 'Powered vs Unpowered Land Price Gap',
                  'metric': 'Powered vs Unpowered Land Price Gap',
                  'value': 'About 4x to 5x',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "datacenterHawk's reported price difference between unpowered land and "
                             'powered land in current data center deals.',
                  'source': 'datacenterHawk ([dTHn2ejpXvM @ 00:18:51])'},
                 {'label': 'AI Data Center Acreage Rule',
                  'metric': 'AI Data Center Acreage Rule',
                  'value': '1MW per acre, 100-acre minimum',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Franklin Andrew Cruz's qualification floor: below 100 acres, AI data center "
                             'buyers will not look at the site.',
                  'source': 'Franklin Andrew Cruz ([YrpzmGX0-YM @ 00:00:47])'},
                 {'label': 'Power and Fiber Run-Out Cost',
                  'metric': 'Power and Fiber Run-Out Cost',
                  'value': '$20M per mile (power), $2M per mile (fiber)',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Mike Embry's cost to extend power once you pull off an existing line, and to "
                             'extend fiber to a site.',
                  'source': 'Advanta IRA ([3rM3iGzRRUA @ 00:08:27])'},
                 {'label': 'Permian Data Center Ground Lease',
                  'metric': 'Permian Data Center Ground Lease',
                  'value': 'About $4,000 per acre plus 5% of net power margin',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "LandBridge's first data center lease, long term, with a 5% override on net "
                             'power-generation margin layered on top.',
                  'source': 'Cool Vector ([rab11GilV3g @ 00:08:20])'}],
 'sections': [{'heading': '1. The Practitioner Consensus: Power Is the Site',
               'paragraphs': ['Every serious operator in this group now starts with electrons, not dirt. '
                              "Foley & Lardner's Faris and Conrad report that about two-thirds of "
                              'respondents name power as the top obstacle, and that the old sequence is '
                              'reversed: start from available megawatts and work backward to the parcel, '
                              'because those attributes matter more than raw acreage or even land price '
                              "[wOKA9jWA8fw @ 00:02:26]. Thor Equities' panel ranks the criteria the same "
                              'way: power first, then proximity to lines and substations, then contiguous '
                              'acreage for a secure perimeter, water and sewer, zoning buffers and tax '
                              "exemptions [yg9V2befNR0 @ 00:18:34]. datacenterHawk calls powered land 'the "
                              "new supply' and puts the price gap between unpowered and powered land at "
                              'four to five times [dTHn2ejpXvM @ 00:18:51]. Kenny Schoolcraft at Zego '
                              "defines the asset as land bundled with 'grid privilege': a parcel near an "
                              'existing substation, an advanced queue position, or transmission with '
                              'headroom, and frames the payoff as one to two years to connect versus three '
                              'to five [2ORDbZvOirU @ 00:08:13]. The blunt summary from Foley: securing '
                              'land without power is increasingly a speculative exercise, and being '
                              'further along in the queue can decide whether a project builds or gets '
                              'shelved for years.',
                              'The baseline physical checklist repeats almost word for word across '
                              'channels. Franklin Andrew Cruz, marketing an owned 130-acre site that could '
                              'be assembled to 288, works from a hard rule: an AI data center takes 1MW '
                              'per acre, and without a 100-acre minimum the buyers will not look '
                              "[YrpzmGX0-YM @ 00:00:47]. LandGate's team lists buildable acreage after "
                              'topography, elevation and risk indices, then off-take capacity, which they '
                              'define as how much power you can actually pull from a substation, then '
                              'regional versus long-haul fiber, water proximity and a redundancy source '
                              'such as a gas or coal plant, because downtime is so expensive [0_owMAznas0 '
                              "@ 00:01:15]. Very large parcels can get 'wiggle room' on a missing "
                              'criterion, LandGate adds. Mike Embry, the horizontal entitlement developer '
                              'on Advanta IRA, boils it to power, fiber, water and sewer, and prices the '
                              'penalty for being far from them: $20M per mile to run power off a line and '
                              '$2M per mile for fiber [3rM3iGzRRUA @ 00:08:27]. Brandt Burnett at CBRE '
                              'notes the scale jump behind all of this: hyperscalers now take 200MW on 100 '
                              'to 300 acres, versus 20-acre, 20MW sites a decade ago, and crypto buyers '
                              'want a path to 500MW at roughly 3-cent power [9IIIRj5ao20 @ 00:18:36].',
                              "Control comes before ownership in every deal here. US Energy Weekly's "
                              'site-control explainer states that developers almost never buy outright: '
                              'they sign two-to-three-year options, run environmental, permitting, '
                              'interconnection and title work, then convert to a lease, and one missing '
                              'parcel breaks the whole block [JwCWz91cMQc @ 00:00:40]. Farming continues '
                              'on optioned ground meanwhile. Maclarens Lawyers frames the option the same '
                              'way from the legal side: a right, not an obligation, with a stipulated '
                              'exercise price and period, that lets a developer secure land through '
                              'research and approvals without locking in the purchase, and that simply '
                              'lapses if not exercised in time [q09nIjF9s5c @ 00:01:49]. The extreme '
                              'version sits in the Stargate Abilene filings, where Systems Leverage found '
                              'a $1 land option exercisable from May 31, 2039, sitting behind a ground '
                              'lease of at least $200,000 a month and a $35M amendment tied to keeping '
                              'power available [nx4eX4emlwE @ 00:00:21]. The other half of the consensus '
                              "is that utilities now demand commitment back: Thor's panel reports "
                              'utilities mandating long-term contracts and minimum usage, deposits used to '
                              'filter out speculators, and Texas load requests tripling in 12 months, '
                              "against a backdrop where the city of Calgary's entire load is about 1.5GW "
                              '[yg9V2befNR0 @ 00:35:37].'],
               'table': {'caption': 'Where the practitioners agree on powered land qualification',
                         'headers': ['Consensus Point',
                                     'What the Practitioners Report',
                                     'Operator Takeaway',
                                     'Expert Source'],
                         'rows': [['Power-first sequencing replaces the old land-first site hunt',
                                   'Start from available megawatts and work backward, since power '
                                   'attributes outweigh raw acreage or pricing',
                                   'Open every parcel review with a deliverable megawatt question before '
                                   'discussing land price',
                                   'Environment+Energy Leader ([wOKA9jWA8fw @ 00:02:26])'],
                                  ['Powered land commands a steep premium over raw dirt',
                                   'Unpowered versus powered land now trades at roughly a four to five '
                                   'times price gap',
                                   'Value the interconnection position itself as the main asset being '
                                   'bought or sold',
                                   'datacenterHawk ([dTHn2ejpXvM @ 00:18:51])'],
                                  ['Hyperscale AI buyers apply a hard acreage and density floor',
                                   'One megawatt per acre and a 100-acre minimum, or buyers will not look '
                                   'at all',
                                   'Assemble neighboring parcels, as Cruz did taking 130 acres toward 288, '
                                   'to clear the floor',
                                   'Franklin Andrew Cruz ([YrpzmGX0-YM @ 00:00:47])'],
                                  ['Substation off-take capacity decides whether nearby power is real',
                                   'Off-take is how much power you can actually pull, and not every '
                                   'substation has enough electrons',
                                   'Verify substation headroom, not just distance to the nearest '
                                   'substation on a map',
                                   'LandApp by LandGate ([0_owMAznas0 @ 00:04:40])'],
                                  ['Grid privilege compresses the connection timeline dramatically for '
                                   'powered land',
                                   'Substation proximity, advanced queue position or transmission headroom '
                                   'bundled with the land itself',
                                   'Expect one to two years to connect versus three to five on raw ground',
                                   'Schneider Electric ([2ORDbZvOirU @ 00:02:25])'],
                                  ['Site control comes through options rather than outright land purchases',
                                   'Two to three year options, then environmental, permitting, '
                                   'interconnection and title work before converting',
                                   'Tie up every parcel in the block, because one missing parcel breaks it',
                                   'US Energy Weekly ([JwCWz91cMQc @ 00:00:40])'],
                                  ['Hyperscale campuses cluster for redundancy instead of standing alone',
                                   'Availability zones get built in threes, generally within 50 kilometers '
                                   'of each other',
                                   'Thor treats isolated remote training sites as high-risk and steers '
                                   'away from them',
                                   'Southern Economic Development Council ([yg9V2befNR0 @ 00:25:19])']]}},
              {'heading': '2. Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ["The utility conversation is step one, and it costs money. Cruz's script is "
                              'simple: call the utility, ask whether it can support 100MW or more, and '
                              'expect to be routed to the team that handles 50MW-plus loads; then confirm '
                              'a permanent natural gas supply for the 80 to 100 generators an AI site '
                              'runs. Cruz also notes Nvidia systems carry their own batteries [YrpzmGX0-YM '
                              "@ 00:02:30]. Embry's sequence on Advanta IRA is more expensive: find a line "
                              'such as a 230, submit a concept plan, then pay a non-refundable preliminary '
                              "study of $30k to $100k that exists 'to cover the overhead for their "
                              "engineering department,' with total spend of $60k to $140k just to learn "
                              'whether the deal works, and the answer usually comes back with required '
                              'grid upgrades [3rM3iGzRRUA @ 00:15:17]. datacenterHawk confirms utilities '
                              "now charge for studies, that CyrusOne's roughly 30MW will-serve letter with "
                              "no expiry would 'no way' be granted today, and that one utility saw a "
                              'single 400MW requirement shopped by four or five developers land as 2GW of '
                              "requests [dTHn2ejpXvM @ 00:15:10]. That phantom demand is why Thor's panel "
                              'reports deposits being used to filter out speculators, with Texas load '
                              'requests tripling in 12 months [yg9V2befNR0 @ 00:35:37].',
                              'Entitlement is where the land developer earns the spread. Embry runs '
                              'geotech, Phase I, environmental and sound studies, rezones at roughly $500k '
                              'out of pocket, and sells near permitting; on one deal $22M had to be posted '
                              'upfront to secure power after zoning cleared [3rM3iGzRRUA @ 00:47:42]. '
                              'Power arrives in phases, for example 2027 then 2032, and the exit pays '
                              'about three times a residential exit while closing faster, yet Embry always '
                              'keeps a Plan B such as multifamily or a Kroger commercial deal in the '
                              'drawer. Embry uses two standard footprints. Foley & Lardner lists the deal '
                              'structures now in play: power-conditioned options, phased closings and '
                              'joint development [wOKA9jWA8fw @ 00:04:24]. Up the value chain, '
                              'datacenterHawk prices turnkey at roughly $12M to $13M per megawatt against '
                              '$4M to $8M for powered shell, with turnkey leased per kW per month whether '
                              'used or not and powered shell per square foot per year, and on a 500MW deal '
                              'might split 200 turnkey and 300 powered shell [pt4hMec2LbM @ 00:13:43]. '
                              "CBRE's Burnett stacks the per-square-foot cost at $250 for core and shell, "
                              'about $1,000 more for fit-out, $2,000 for IT and $5,000 for software, '
                              'roughly ten times other asset classes [9IIIRj5ao20 @ 00:10:16].',
                              "On the landowner side, the numbers are just as specific. LandBridge's "
                              'Capobianco signed the first data center lease at about $4,000 per acre for '
                              '30 to 40 years and layers a 5% cut of net power-generation margin on top; '
                              'with $3 gas producing power at about 2 cents per kWh against a 7 to 9 cent '
                              'sale, a gigawatt could throw off $20M to $30M a year to the landlord '
                              '[rab11GilV3g @ 00:08:20]. LandBridge bought 46,000 acres at about $5,000 '
                              'per acre that now trade above $20,000 in the public market. US Energy '
                              "Weekly's benchmarks for optioned solar land: a signing bonus, an annual "
                              'option fee that often escalates, at least $1,000 to $2,000 a year, then '
                              'rent of $250 to $2,000 per acre, higher in Texas, with escalators of 1.5% '
                              'to 3%, and the standing rule is never to let a developer tie up land for '
                              'years without paying [JwCWz91cMQc @ 00:02:41]. For screening, LandGate '
                              'precomputes energy cost, source and interconnection queue for every single '
                              'US parcel [0_owMAznas0 @ 00:04:06], while CBRE replaced the old '
                              'orange-flag, spray-paint and manhole-stamp fiber tracing with Fiber '
                              'Locator, which it acquired. Substations, Burnett adds, now take two years '
                              'instead of one [9IIIRj5ao20 @ 00:14:21].'],
               'table': {'caption': 'Street-level numbers and tools for powered land deals',
                         'headers': ['Mechanic',
                                     'Exact Number or Tool',
                                     'How It Gets Used',
                                     'Expert Source'],
                         'rows': [['Utility preliminary feasibility study on a specific transmission line',
                                   'Non-refundable $30k to $100k, with $60k to $140k spent to learn if it '
                                   'works',
                                   'Submit a concept plan on a line such as a 230 first',
                                   'Advanta IRA ([3rM3iGzRRUA @ 00:15:17])'],
                                  ['Power and fiber run-out from the nearest existing line',
                                   '$20M per mile for power and $2M per mile for fiber',
                                   'Price the distance penalty before tying up land far from existing '
                                   'lines',
                                   'Advanta IRA ([3rM3iGzRRUA @ 00:08:27])'],
                                  ['Substation build time and cost inflation since the pandemic',
                                   'Substations now take two years instead of one, at roughly 150% of '
                                   'prior cost',
                                   'Push owners toward land banking and powered-site packaging ahead of '
                                   'demand',
                                   'datacenterHawk ([9IIIRj5ao20 @ 00:23:54])'],
                                  ['Turnkey versus powered shell capital cost per megawatt delivered',
                                   'Turnkey $12M to $13M per MW, powered shell $4M to $8M per MW',
                                   'Split big deals, for example 200MW turnkey plus 300MW powered shell',
                                   'datacenterHawk ([pt4hMec2LbM @ 00:13:43])'],
                                  ['Surface owner lease plus power-margin override in the Permian',
                                   'About $4,000 per acre for 30 to 40 years plus 5% of net margin',
                                   'Stack recurring power-margin income on top of the base ground rent',
                                   'Cool Vector ([rab11GilV3g @ 00:08:20])'],
                                  ['Option and rent payments on optioned solar ground',
                                   'Option fee at least $1,000 to $2,000 yearly, rent $250 to $2,000 per '
                                   'acre',
                                   'Escalate payments 1.5% to 3% and demand pay for every year tied up',
                                   'US Energy Weekly ([JwCWz91cMQc @ 00:02:41])'],
                                  ['Parcel-level energy screening software for data center suitability',
                                   'LandGate precomputes energy cost, source and interconnection queue for '
                                   'every US parcel',
                                   'Run parcel screens before calling the utility or walking the fiber '
                                   'route',
                                   'LandApp by LandGate ([0_owMAznas0 @ 00:04:06])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'How the operators actually work the deal',
                           'body': 'Four moves the practitioners use to find, lock and verify powered land '
                                   'before money goes hard.',
                           'items': ['Call the utility and ask directly whether it can support 100MW or '
                                     'more; you get routed to the department that handles 50MW-plus loads, '
                                     'which is the desk that matters [Franklin Andrew Cruz — YrpzmGX0-YM @ '
                                     '00:01:04].',
                                     'Never entitle a data center site without a Plan B such as '
                                     'multifamily or a Kroger commercial deal in case the power answer '
                                     'comes back wrong [Advanta IRA — 3rM3iGzRRUA @ 00:17:30].',
                                     'Landowners: compare at least two or three offers side by side before '
                                     'signing, and never let a developer tie up land for years without '
                                     'paying for it [US Energy Weekly — JwCWz91cMQc @ 00:05:01].',
                                     'Follow the contract, match the names, and check the date on the '
                                     "page; that is how Systems Leverage traced Stargate's $1 option to a "
                                     'ground lease of at least $200,000 a month and a JPMorgan collateral '
                                     'assignment [Systems Leverage — nx4eX4emlwE @ 00:10:36].']},
               'sop_steps': [{'step': 1,
                              'title': 'Screen parcels for megawatts, not acres',
                              'action': 'Pull parcel-level energy data and test the acreage floor before '
                                        'any outreach.',
                              'detail': "Use LandGate's precomputed energy cost, source and "
                                        'interconnection queue for the parcel, confirm substation off-take '
                                        'headroom, and check the site clears 1MW per acre with at least '
                                        '100 acres [LandApp by LandGate — 0_owMAznas0 @ 00:04:06] '
                                        '[Franklin Andrew Cruz — YrpzmGX0-YM @ 00:00:47].'},
                             {'step': 2,
                              'title': 'Fund the utility answer',
                              'action': 'Find a line, submit a concept plan, and pay for the preliminary '
                                        'study.',
                              'detail': 'Target a line such as a 230, submit a concept plan, pay the '
                                        'non-refundable $30k to $100k preliminary study, and expect the '
                                        'result to require grid upgrades [Advanta IRA — 3rM3iGzRRUA @ '
                                        '00:12:13].'},
                             {'step': 3,
                              'title': 'Lock site control with an option',
                              'action': 'Tie up every parcel in the block with a time-limited option '
                                        'rather than buying outright.',
                              'detail': 'Set a stipulated exercise price and option period so the right '
                                        'lapses cleanly if unexercised, and run environmental, permitting, '
                                        'interconnection and title work during the two-to-three-year '
                                        'window [Maclarens Lawyers — q09nIjF9s5c @ 00:01:49] [US Energy '
                                        'Weekly — JwCWz91cMQc @ 00:00:40].'},
                             {'step': 4,
                              'title': 'Entitle, phase power, and exit near permitting',
                              'action': 'Complete studies and rezoning, lock phased power, then sell to '
                                        'the end user.',
                              'detail': 'Run geotech, Phase I, environmental and sound studies, rezone at '
                                        'roughly $500k, phase power deliveries such as 2027 then 2032, and '
                                        'sell near permitting for an exit Embry puts at about three times '
                                        'residential [Advanta IRA — 3rM3iGzRRUA @ 00:23:02].'}]},
              {'heading': 'Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The sharpest split is over where the electrons come from. Kenny Schoolcraft '
                              'of Zego defines powered land as land bundled with grid privilege: a parcel '
                              'near an existing substation, holding an advanced interconnection queue '
                              'position, or tied to transmission with headroom. He argues that privilege '
                              'is a fungible asset worth shorter timelines, lower execution risk and '
                              'sometimes higher exit valuations [2ORDbZvOirU @ 00:02:25]. David Capobianco '
                              'of LandBridge plays the opposite hand in the Permian. He warns that very '
                              'few grids or municipal water systems can supply a data center, so the load '
                              'needs its own behind-the-meter power, fed by gas that has averaged about '
                              'minus 60 cents per mcf over nine months [rab11GilV3g @ 00:03:17]. Mike '
                              'Embry lands in the middle on his entitlement deals, running gas turbines as '
                              'primary power and keeping the grid as backup [3rM3iGzRRUA @ 00:09:36]. The '
                              'Foley & Lardner team flags the cost of leaving the grid: behind-the-meter '
                              'gas, storage-paired renewables and hybrids each raise permitting and '
                              'fuel-contract issues [wOKA9jWA8fw @ 00:04:59]. The operator read is that '
                              'both camps sell speed and firm 24/7 capacity. One monetizes a queue '
                              'position a buyer can plug straight into. The other monetizes cheap gas and '
                              'brackish water sitting next to the site, and sidesteps the utility almost '
                              'entirely.',
                              'Practitioners also disagree on how much dirt even qualifies. Franklin '
                              'Andrew Cruz, shopping his own 130-acre tract that can be assembled to 288 '
                              'acres, works off a rule of 1 megawatt per acre. He says buyers will not '
                              'look at anything under a 100-acre minimum [YrpzmGX0-YM @ 00:00:47]. '
                              "LandGate's team sets a much lower bar. It puts buildable acreage at an "
                              'average of around 40 acres, scored alongside off-take capacity near a '
                              'substation, fiber optic lines and environmental impact on the land '
                              '[2mYrH35TasY @ 00:00:00]. The same LandGate crew concedes that very large '
                              'parcels may carry wiggle room on criteria they are missing, so sheer size '
                              'can offset a gap elsewhere in the score [0_owMAznas0 @ 00:07:57]. Brandt '
                              'Burnett of CBRE describes the target moving up fast. Hyperscalers now take '
                              '200MW on 100 to 300 acres, against the 20-acre, 20MW sites that passed a '
                              'decade ago [9IIIRj5ao20 @ 00:18:36]. For an operator, the gap bites at the '
                              'pitch stage. A 40-acre parcel can score well inside a parcel index and '
                              "still never get a call from a hyperscale buyer running Cruz's "
                              'megawatt-per-acre math with a 100-acre floor. The parcel index tells you '
                              "proximity; the buyer's acreage floor tells you whether anyone shows up to "
                              'the table.',
                              "Location and fuel mix split the room as well. Thor Equities' team treats "
                              'clustering as the safe play, building availability zones in threes and '
                              'steering away from remote training sites, which it labels high-risk '
                              '[yg9V2befNR0 @ 00:27:30]. Capobianco runs the opposite thesis from the '
                              'Delaware sub-basin, a region with no large population centers. He argues '
                              'that it is a lot easier to move bytes than it is to move energy, so '
                              'builders should go to the place with the cheapest gas, with fiber already '
                              'running along I-10 and I-20 [rab11GilV3g @ 00:23:59]. On fuel, Mike Embry '
                              'says flatly that solar will not work as data center power and builds his '
                              'sites around gas turbines with closed-loop cooling on treated gray water '
                              '[3rM3iGzRRUA @ 00:10:26]. Kenny Schoolcraft goes further, saying powered '
                              'land may have nothing to do with renewables at all, because some owners '
                              'simply do not care about the renewable piece and the value sits in the '
                              'interconnection [2ORDbZvOirU @ 00:16:12]. Operators pitching a remote gas '
                              'site and a clustered metro grid site are therefore selling two different '
                              'risk profiles. One promises the cheapest molecules and behind-the-meter '
                              'control; the other promises latency, spillover between sister facilities '
                              'and a labor market already in place.'],
               'table': {'caption': 'Competing playbooks for qualifying, controlling and delivering '
                                    'powered land',
                         'headers': ['Decision Point',
                                     'Playbook A',
                                     'Playbook B / Counterpoint',
                                     'Expert Source'],
                         'rows': [['Where the power comes from',
                                   'Grid privilege near a substation with advanced queue position and '
                                   'transmission headroom',
                                   'Behind-the-meter gas because very few grids or water systems can '
                                   'supply the load',
                                   'Schneider Electric ([2ORDbZvOirU @ 00:02:25]); Cool Vector '
                                   '([rab11GilV3g @ 00:03:17])'],
                                  ['Minimum acreage to get looked at',
                                   'One megawatt per acre with a hard 100-acre floor for AI buyers',
                                   'Buildable acreage averaging around 40 acres, scored with substation, '
                                   'fiber and environmental factors',
                                   'Franklin Andrew Cruz ([YrpzmGX0-YM @ 00:00:47]); LandApp by LandGate '
                                   '([2mYrH35TasY @ 00:00:00])'],
                                  ['Role of renewables on the site',
                                   'Solar will not work; a 250MW solar farm averages about 25MW across a '
                                   'year',
                                   'Renewables proximity is a qualification, with Apple building its own '
                                   'solar',
                                   'Advanta IRA ([3rM3iGzRRUA @ 00:10:26]); Cool Vector ([rab11GilV3g @ '
                                   '00:06:28]); LandApp by LandGate ([0_owMAznas0 @ 00:09:13])'],
                                  ['Remote versus clustered siting',
                                   'Build availability zones in threes within about 50 kilometers and '
                                   'avoid remote training sites',
                                   'Move bytes rather than energy and go wherever the gas is cheapest',
                                   'Southern Economic Development Council ([yg9V2befNR0 @ 00:25:19]); Cool '
                                   'Vector ([rab11GilV3g @ 00:23:59])'],
                                  ['Do data centers raise power rates',
                                   'Some truth to rate increases, though a gigawatt of added load cuts '
                                   'rates about 1%',
                                   'Data centers pay bills like anyone else; compare five-year-old bills '
                                   'to see utility excuses',
                                   'Southern Economic Development Council ([yg9V2befNR0 @ 00:31:46]); '
                                   'Franklin Andrew Cruz ([YrpzmGX0-YM @ 00:01:45])'],
                                  ['How to control the land',
                                   'Developers almost never buy outright; they run a two-to-three-year '
                                   'option then convert to lease',
                                   'Buy at about $5,000 per acre, lease at about $4,000 per acre plus 5% '
                                   'of power margin',
                                   'US Energy Weekly ([JwCWz91cMQc @ 00:00:40]); Cool Vector ([rab11GilV3g '
                                   '@ 00:22:41])'],
                                  ['What product to deliver on the land',
                                   'Turnkey runs roughly $12 to $13 million per megawatt and takes five '
                                   'years to reach',
                                   'Powered shell runs $4 to $8 million per megawatt; a 500MW deal might '
                                   'split 200 turnkey and 300 shell',
                                   'datacenterHawk ([pt4hMec2LbM @ 00:13:43]); datacenterHawk '
                                   '([pt4hMec2LbM @ 00:20:49])']]}},
              {'heading': 'Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The most consistent firsthand pain is money spent before a single shovel '
                              'moves. Mike Embry pays a non-refundable preliminary study fee of $30,000 to '
                              '$100,000 after submitting a concept plan on a line, explaining that it '
                              "exists to cover the overhead of the power company's engineering department. "
                              'He warns you could be spending 60 to 140 thousand dollars just to find out '
                              'whether the deal works [3rM3iGzRRUA @ 00:15:17]. After clearing zoning, '
                              'which he puts at roughly $500,000 out of pocket, one deal required $22 '
                              'million up front to secure the power [3rM3iGzRRUA @ 00:47:42]. The '
                              'datacenterHawk hosts confirm utilities now charge for studies, and say '
                              "CyrusOne's roughly 30MW will-serve letter with no expiry is the kind of "
                              'commitment there is no way a utility grants today [dTHn2ejpXvM @ 00:13:48]. '
                              "Thor Equities' panel adds the back-end squeeze: utilities mandate long-term "
                              'contracts and minimum usage to recover costs, and water upgrade costs are '
                              'fully borne by the developer [yg9V2befNR0 @ 00:53:09]. The economics check '
                              'is simple. Every utility gate converts optionality into cash at risk, and a '
                              'horizontal developer carries that cash long before any end user signs. '
                              "Embry's answer is to always hold a fallback use for the dirt if the power "
                              'answer comes back wrong.',
                              'The second trap is believing the demand and grid numbers on the surface. '
                              'The datacenterHawk hosts describe one utility that saw a single 400MW '
                              'requirement shopped by four to five developers, which landed on its desk as '
                              '2GW of requests. They also estimate that of roughly 6GW of planned power in '
                              'Dallas, 2 to 3GW will likely not be built by whoever announced it '
                              '[dTHn2ejpXvM @ 00:15:10]. Embry lost a site outright on redundancy. TVA '
                              'areas lack it, so his Decatur, Alabama site failed, and his verdict on '
                              "another location was short: can't put a data center there [3rM3iGzRRUA @ "
                              '00:30:40]. Brandt Burnett reports that a substation that used to take a '
                              'year now takes two and costs about 150% of what it did, while land prices '
                              'have literally quadrupled since the pandemic [9IIIRj5ao20 @ 00:23:54]. He '
                              'also shows how textbook screens collapse in practice. Apply a five-mile '
                              'airport buffer and there are no Dallas sites left, so TIA-942 checklists '
                              'hold only until another factor trumps them, and his defense is building an '
                              'auditable roadmap [9IIIRj5ao20 @ 00:33:38]. The pattern across all three is '
                              'that the queue, the substation schedule and the redundancy picture each '
                              'look healthier on announcement than they do at diligence.',
                              'Paper and people produce the slowest-burning losses. Maclarens Lawyers call '
                              'option legislation rigid and unforgiving. A residential option cannot be '
                              'exercised in its first 42 days, and in 2021 a 66ZF certificate attached to '
                              'the call did not waive cooling-off on the put, so a buyer walked from 13 '
                              'contracts because no 66W was in place. They say such fights can take up '
                              "many years of everyone's lives [q09nIjF9s5c @ 00:04:31]. On assembly, US "
                              'Energy Weekly warns that big projects sign options with dozens of '
                              'landowners and that one missing parcel breaks the whole block, while '
                              'telling owners never to let a developer tie up land for years without '
                              'paying [JwCWz91cMQc @ 00:01:22]. Sellers have caught on. The datacenterHawk '
                              'hosts saw a 200-acre offer come in six times below market, a sign that '
                              'landowners are smarter than they were, and part of why buying unpowered '
                              'land, powering it and flipping it is getting harder [dTHn2ejpXvM @ '
                              "00:08:17]. Systems Leverage's dig into Stargate's Abilene site shows the "
                              'community bill: residents report destroyed roads, and university '
                              'recruitment fell from 40 to 12 with apartments at $2,600, while the '
                              'announced financing leaves $5.6 billion unexplained [nx4eX4emlwE @ '
                              '00:07:02].'],
               'table': {'caption': 'Firsthand failure modes and the economics behind them',
                         'headers': ['Failure Mode',
                                     'What Happened Firsthand',
                                     'Economics Check',
                                     'Expert Source'],
                         'rows': [['Paying for a utility study blind',
                                   'Non-refundable preliminary study covers the power company engineering '
                                   'department overhead',
                                   '$30,000 to $100,000 per study, or 60 to 140 thousand to learn if it '
                                   'works',
                                   'Advanta IRA ([3rM3iGzRRUA @ 00:15:17])'],
                                  ['Power security deposit after zoning',
                                   'One deal needed cash posted to the utility after zoning was already '
                                   'done',
                                   '$22 million up front on top of roughly $500,000 out-of-pocket rezoning',
                                   'Advanta IRA ([3rM3iGzRRUA @ 00:47:42])'],
                                  ['Phantom demand inflating the queue',
                                   'A single 400MW requirement shopped by four to five developers hit one '
                                   'utility',
                                   'Showed up as 2GW of requests; 2 to 3GW of Dallas plans likely not '
                                   'built by announcer',
                                   'datacenterHawk ([dTHn2ejpXvM @ 00:15:10]); datacenterHawk '
                                   '([dTHn2ejpXvM @ 00:22:04])'],
                                  ['No redundancy source on the grid',
                                   'Decatur, Alabama site in TVA territory failed because the area lacks '
                                   'redundancy',
                                   'Downtime cost is very high, so buyers walk from sites without a '
                                   'redundancy source',
                                   'Advanta IRA ([3rM3iGzRRUA @ 00:30:40]); LandApp by LandGate '
                                   '([0_owMAznas0 @ 00:08:54])'],
                                  ['Substation schedule and cost slippage',
                                   'Substation builds that took about a year now take about two years',
                                   'Substations now cost about 150% of before, with prices quadrupled '
                                   'since the pandemic',
                                   'datacenterHawk ([9IIIRj5ao20 @ 00:23:54]); datacenterHawk '
                                   '([9IIIRj5ao20 @ 00:26:39])'],
                                  ['Defective option paperwork on put and call',
                                   'Call-side 66ZF certificate did not waive cooling-off on the put side '
                                   'in 2021',
                                   'Buyer exited 13 contracts; either party can pull out of defective '
                                   'documents',
                                   'Maclarens Lawyers ([q09nIjF9s5c @ 00:04:50]); Maclarens Lawyers '
                                   '([q09nIjF9s5c @ 00:03:57])'],
                                  ['Thin buyer pool for the finished product',
                                   'Alt-energy sites have few buyers, and turnkey entrants must win over '
                                   'skeptical users',
                                   'Only 10 to 15 buyers exist; 15 to 20 users do not want to be your test '
                                   'case',
                                   'datacenterHawk ([dTHn2ejpXvM @ 00:11:24]); datacenterHawk '
                                   '([pt4hMec2LbM @ 00:15:00])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Four kill-switches before cash goes to the utility',
                           'body': 'Each gate below comes from a site, deposit or contract that '
                                   'practitioners watched fail. Clear all four before writing the study '
                                   'check, posting a power deposit or signing an option package.',
                           'items': ['Pin the concept plan to a specific line such as a 230 and have a '
                                     'Plan B like multifamily or a Kroger commercial deal ready before '
                                     'paying the study fee [Advanta IRA — 3rM3iGzRRUA @ 00:17:30].',
                                     'Name the redundancy source, such as a gas or coal plant, before '
                                     "advancing; Embry's Decatur, Alabama site died for lack of it in TVA "
                                     'territory [Advanta IRA — 3rM3iGzRRUA @ 00:30:40].',
                                     'Discount announced load and queue totals; one 400MW requirement '
                                     'shopped by four to five developers showed up as 2GW of requests '
                                     '[datacenterHawk — dTHn2ejpXvM @ 00:15:10].',
                                     'Paper each leg of a put and call on its own; a 66ZF certificate on '
                                     'the call did not cover the put and let a buyer exit 13 contracts '
                                     '[Maclarens Lawyers — q09nIjF9s5c @ 00:04:50].']}}],
 'pull_quote': '"It\'s really hard to make a quick buck in the data center space, maybe that\'s what I\'ll '
               'say." Attributed to datacenterHawk (dTHn2ejpXvM @ 00:08:34).',
 'diagram_id': 'diag-01',
 'action_checklist': ['Call the utility and ask whether it can support 100MW or more so you get routed to '
                      'its 50MW-plus team before marketing the parcel [Franklin Andrew Cruz — YrpzmGX0-YM '
                      '@ 00:02:30].',
                      'Click your parcel in LandApp and read the data center index for combined proximity '
                      'to substation, fiber and other factors [LandApp by LandGate — 2mYrH35TasY @ '
                      '00:01:35].',
                      'Submit a concept plan on a line such as a 230 and budget a non-refundable $30,000 '
                      'to $100,000 preliminary study [Advanta IRA — 3rM3iGzRRUA @ 00:12:13].',
                      'Confirm a redundancy source such as a nearby gas or coal plant because the cost of '
                      'downtime is very high [LandApp by LandGate — 0_owMAznas0 @ 00:08:54].',
                      'On the landowner side, demand paid option money of at least $1,000 to $2,000 per '
                      'year and compare two or three offers side by side [US Energy Weekly — JwCWz91cMQc @ '
                      '00:05:01].',
                      'Trace every announced deal through recorded instruments: follow the contract, match '
                      'the names, and check the date on the page [Systems Leverage — nx4eX4emlwE @ '
                      '00:10:36].'],
 'statutory_citations': [{'title': 'datacenterHawk — Land Battle: Powered vs Unpowered in Data Center '
                                   'Development [00:18:51]',
                          'url': 'https://www.youtube.com/watch?v=dTHn2ejpXvM&t=1131s',
                          'relevance': 'Primary practitioner testimony on the four-to-five-times price gap '
                                       'between unpowered and powered land and the shrinking flip margin.'},
                         {'title': 'Advanta IRA — The Real Estate Behind AI: Data Center Land Deals '
                                   'Explained - Episode 193 [00:47:42]',
                          'url': 'https://www.youtube.com/watch?v=3rM3iGzRRUA&t=2862s',
                          'relevance': 'Primary practitioner testimony on utility study fees, rezoning '
                                       'costs and the $22 million power deposit after zoning.'},
                         {'title': 'Cool Vector — West Texas Land is Perfect for Data Centers, Says '
                                   'LandBridge Founder [00:03:17]',
                          'url': 'https://www.youtube.com/watch?v=rab11GilV3g&t=197s',
                          'relevance': 'Primary practitioner testimony on behind-the-meter gas power as '
                                       'the alternative to grid-dependent powered land.'},
                         {'title': 'Schneider Electric — Powered Land Explained: The Race for Energy '
                                   'Infrastructure [00:02:25]',
                          'url': 'https://www.youtube.com/watch?v=2ORDbZvOirU&t=145s',
                          'relevance': 'Primary practitioner testimony on grid privilege and '
                                       'interconnection queue position as the core powered land asset.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'yg9V2befNR0',
                       'title': 'Data Center Site Selection and Navigating Power Procurement',
                       'channel': 'Southern Economic Development Council',
                       'author': 'Southern Economic Development Council',
                       'text': 'So if you build one, you want to have two more within a proximity of '
                               'generally less than 50 kilometers so that if one fails, you can spill over '
                               'into the next with nominal latency effects.',
                       'tip': 'So if you build one, you want to have two more within a proximity of '
                              'generally less than 50 kilometers so that if one fails, you can spill over '
                              'into the next with nominal latency effects.',
                       'timestamp': 1519,
                       'timestamp_seconds': 1519,
                       'timestamp_label': '[00:25:19]',
                       'url': 'https://www.youtube.com/watch?v=yg9V2befNR0&t=1519s',
                       'markdown': '[00:25:19](https://www.youtube.com/watch?v=yg9V2befNR0&t=1519s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'yg9V2befNR0',
                       'title': 'Data Center Site Selection and Navigating Power Procurement',
                       'channel': 'Southern Economic Development Council',
                       'author': 'Southern Economic Development Council',
                       'text': 'So as that denominator goes up the cost goes down, and about a gigawatt '
                               'extra of load essentially reduces rates by about 1%.',
                       'tip': 'So as that denominator goes up the cost goes down, and about a gigawatt '
                              'extra of load essentially reduces rates by about 1%.',
                       'timestamp': 3172,
                       'timestamp_seconds': 3172,
                       'timestamp_label': '[00:52:52]',
                       'url': 'https://www.youtube.com/watch?v=yg9V2befNR0&t=3172s',
                       'markdown': '[00:52:52](https://www.youtube.com/watch?v=yg9V2befNR0&t=3172s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'YrpzmGX0-YM',
                       'title': 'The Truth About AI Data Center Land (Most Sites Don’t Qualify)',
                       'channel': 'Franklin Andrew Cruz',
                       'author': 'Franklin Andrew Cruz',
                       'text': "So, if you do not have a minimum of 100 acres, then they're not going to "
                               'look.',
                       'tip': "So, if you do not have a minimum of 100 acres, then they're not going to "
                              'look.',
                       'timestamp': 47,
                       'timestamp_seconds': 47,
                       'timestamp_label': '[00:00:47]',
                       'url': 'https://www.youtube.com/watch?v=YrpzmGX0-YM&t=47s',
                       'markdown': '[00:00:47](https://www.youtube.com/watch?v=YrpzmGX0-YM&t=47s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '0_owMAznas0',
                       'title': 'Understanding Property Qualifications for Data Centers',
                       'channel': 'LandApp by LandGate',
                       'author': 'LandApp by LandGate',
                       'text': 'Your redundancy source is essential because the cost of downtime, the cost '
                               'of not running the data center, is very high.',
                       'tip': 'Your redundancy source is essential because the cost of downtime, the cost '
                              'of not running the data center, is very high.',
                       'timestamp': 534,
                       'timestamp_seconds': 534,
                       'timestamp_label': '[00:08:54]',
                       'url': 'https://www.youtube.com/watch?v=0_owMAznas0&t=534s',
                       'markdown': '[00:08:54](https://www.youtube.com/watch?v=0_owMAznas0&t=534s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '2mYrH35TasY',
                       'title': 'Data Centers Are Paying Top Dollar- Is Your Property a Match?',
                       'channel': 'LandApp by LandGate',
                       'author': 'LandApp by LandGate',
                       'text': 'I think an average hyperscale data center can use around the equivalent of '
                               '50,000 homes worth of electricity.',
                       'tip': 'I think an average hyperscale data center can use around the equivalent of '
                              '50,000 homes worth of electricity.',
                       'timestamp': 19,
                       'timestamp_seconds': 19,
                       'timestamp_label': '[00:00:19]',
                       'url': 'https://www.youtube.com/watch?v=2mYrH35TasY&t=19s',
                       'markdown': '[00:00:19](https://www.youtube.com/watch?v=2mYrH35TasY&t=19s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '3rM3iGzRRUA',
                       'title': 'The Real Estate Behind AI: Data Center Land Deals Explained - Episode 193',
                       'channel': 'Advanta IRA',
                       'author': 'Advanta IRA',
                       'text': 'So you could be spending 60 to 130, $140,000 to find out from the power '
                               "company it's going to be a deal that worked.",
                       'tip': 'So you could be spending 60 to 130, $140,000 to find out from the power '
                              "company it's going to be a deal that worked.",
                       'timestamp': 917,
                       'timestamp_seconds': 917,
                       'timestamp_label': '[00:15:17]',
                       'url': 'https://www.youtube.com/watch?v=3rM3iGzRRUA&t=917s',
                       'markdown': '[00:15:17](https://www.youtube.com/watch?v=3rM3iGzRRUA&t=917s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '3rM3iGzRRUA',
                       'title': 'The Real Estate Behind AI: Data Center Land Deals Explained - Episode 193',
                       'channel': 'Advanta IRA',
                       'author': 'Advanta IRA',
                       'text': 'There was $22 million had to be put up front to secure the power after we '
                               'got through zoning and all that kind of stuff.',
                       'tip': 'There was $22 million had to be put up front to secure the power after we '
                              'got through zoning and all that kind of stuff.',
                       'timestamp': 2862,
                       'timestamp_seconds': 2862,
                       'timestamp_label': '[00:47:42]',
                       'url': 'https://www.youtube.com/watch?v=3rM3iGzRRUA&t=2862s',
                       'markdown': '[00:47:42](https://www.youtube.com/watch?v=3rM3iGzRRUA&t=2862s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'wOKA9jWA8fw',
                       'title': 'Industry Voice: How Powered Land Is Changing Data Center Site Selection',
                       'channel': 'Environment+Energy Leader',
                       'author': 'Environment+Energy Leader',
                       'text': 'Securing land without power is increasingly a speculative exercise.',
                       'tip': 'Securing land without power is increasingly a speculative exercise.',
                       'timestamp': 490,
                       'timestamp_seconds': 490,
                       'timestamp_label': '[00:08:10]',
                       'url': 'https://www.youtube.com/watch?v=wOKA9jWA8fw&t=490s',
                       'markdown': '[00:08:10](https://www.youtube.com/watch?v=wOKA9jWA8fw&t=490s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'q09nIjF9s5c',
                       'title': 'Property Insights:  Land Option Contracts',
                       'channel': 'Maclarens Lawyers',
                       'author': 'Maclarens Lawyers',
                       'text': 'If the documents fail to recognize this the documents will be defective '
                               'and either party can pull out.',
                       'tip': 'If the documents fail to recognize this the documents will be defective and '
                              'either party can pull out.',
                       'timestamp': 237,
                       'timestamp_seconds': 237,
                       'timestamp_label': '[00:03:57]',
                       'url': 'https://www.youtube.com/watch?v=q09nIjF9s5c&t=237s',
                       'markdown': '[00:03:57](https://www.youtube.com/watch?v=q09nIjF9s5c&t=237s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'dTHn2ejpXvM',
                       'title': 'Land Battle: Powered vs Unpowered in Data Center Development',
                       'channel': 'datacenterHawk',
                       'author': 'datacenterHawk',
                       'text': "You're buying unpowered land, getting the power and trying to sell it for "
                               "a profit, sure, it's getting harder to do.",
                       'tip': "You're buying unpowered land, getting the power and trying to sell it for a "
                              "profit, sure, it's getting harder to do.",
                       'timestamp': 879,
                       'timestamp_seconds': 879,
                       'timestamp_label': '[00:14:39]',
                       'url': 'https://www.youtube.com/watch?v=dTHn2ejpXvM&t=879s',
                       'markdown': '[00:14:39](https://www.youtube.com/watch?v=dTHn2ejpXvM&t=879s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'dTHn2ejpXvM',
                       'title': 'Land Battle: Powered vs Unpowered in Data Center Development',
                       'channel': 'datacenterHawk',
                       'author': 'datacenterHawk',
                       'text': "The difference between unpowered land and powered land, we're seeing about "
                               'a four to 5x difference in price.',
                       'tip': "The difference between unpowered land and powered land, we're seeing about "
                              'a four to 5x difference in price.',
                       'timestamp': 1131,
                       'timestamp_seconds': 1131,
                       'timestamp_label': '[00:18:51]',
                       'url': 'https://www.youtube.com/watch?v=dTHn2ejpXvM&t=1131s',
                       'markdown': '[00:18:51](https://www.youtube.com/watch?v=dTHn2ejpXvM&t=1131s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '9IIIRj5ao20',
                       'title': 'Big Topics: Data Center Site Selection with CBRE',
                       'channel': 'datacenterHawk',
                       'author': 'datacenterHawk',
                       'text': "We build a substation and what used to take, let's just call it a year, "
                               "that's taken two years now.",
                       'tip': "We build a substation and what used to take, let's just call it a year, "
                              "that's taken two years now.",
                       'timestamp': 1434,
                       'timestamp_seconds': 1434,
                       'timestamp_label': '[00:23:54]',
                       'url': 'https://www.youtube.com/watch?v=9IIIRj5ao20&t=1434s',
                       'markdown': '[00:23:54](https://www.youtube.com/watch?v=9IIIRj5ao20&t=1434s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'JwCWz91cMQc',
                       'title': 'No Land, No Project? Site Control Explained | US Energy ESSENTIALS',
                       'channel': 'US Energy Weekly',
                       'author': 'US Energy Weekly',
                       'text': 'Never sign a deal that lets a developer tie up your land for years without '
                               'paying for it.',
                       'tip': 'Never sign a deal that lets a developer tie up your land for years without '
                              'paying for it.',
                       'timestamp': 161,
                       'timestamp_seconds': 161,
                       'timestamp_label': '[00:02:41]',
                       'url': 'https://www.youtube.com/watch?v=JwCWz91cMQc&t=161s',
                       'markdown': '[00:02:41](https://www.youtube.com/watch?v=JwCWz91cMQc&t=161s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'eTK7c4pacdY',
                       'title': 'How to Identify Renewable Energy Potential for Land & CRE',
                       'channel': 'LandApp by LandGate',
                       'author': 'LandApp by LandGate',
                       'text': "We provide them the data, sorry, we don't advise them, we provide them the "
                               'data.',
                       'tip': "We provide them the data, sorry, we don't advise them, we provide them the "
                              'data.',
                       'timestamp': 38,
                       'timestamp_seconds': 38,
                       'timestamp_label': '[00:00:38]',
                       'url': 'https://www.youtube.com/watch?v=eTK7c4pacdY&t=38s',
                       'markdown': '[00:00:38](https://www.youtube.com/watch?v=eTK7c4pacdY&t=38s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'nx4eX4emlwE',
                       'title': 'Stargate’s $1 Land Option: Who Pays for the $15 Billion Build?',
                       'channel': 'Systems Leverage',
                       'author': 'Systems Leverage',
                       'text': 'Follow the contract, match the names, and check the date on the page.',
                       'tip': 'Follow the contract, match the names, and check the date on the page.',
                       'timestamp': 636,
                       'timestamp_seconds': 636,
                       'timestamp_label': '[00:10:36]',
                       'url': 'https://www.youtube.com/watch?v=nx4eX4emlwE&t=636s',
                       'markdown': '[00:10:36](https://www.youtube.com/watch?v=nx4eX4emlwE&t=636s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'pt4hMec2LbM',
                       'title': 'Understanding Powered Shell Data Centers',
                       'channel': 'datacenterHawk',
                       'author': 'datacenterHawk',
                       'text': 'TurnKey is kind of maybe in the 12 to 13 million bucks a megawatt versus '
                               'powered shell could be maybe as low as four to five, maybe up to seven or '
                               'eight.',
                       'tip': 'TurnKey is kind of maybe in the 12 to 13 million bucks a megawatt versus '
                              'powered shell could be maybe as low as four to five, maybe up to seven or '
                              'eight.',
                       'timestamp': 823,
                       'timestamp_seconds': 823,
                       'timestamp_label': '[00:13:43]',
                       'url': 'https://www.youtube.com/watch?v=pt4hMec2LbM&t=823s',
                       'markdown': '[00:13:43](https://www.youtube.com/watch?v=pt4hMec2LbM&t=823s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'rab11GilV3g',
                       'title': 'West Texas Land is Perfect for Data Centers, Says LandBridge Founder',
                       'channel': 'Cool Vector',
                       'author': 'Cool Vector',
                       'text': "It's a lot easier to move bytes than it is to move energy, you want to go "
                               "to the place that's the cheapest gas.",
                       'tip': "It's a lot easier to move bytes than it is to move energy, you want to go "
                              "to the place that's the cheapest gas.",
                       'timestamp': 1439,
                       'timestamp_seconds': 1439,
                       'timestamp_label': '[00:23:59]',
                       'url': 'https://www.youtube.com/watch?v=rab11GilV3g&t=1439s',
                       'markdown': '[00:23:59](https://www.youtube.com/watch?v=rab11GilV3g&t=1439s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '2ORDbZvOirU',
                       'title': 'Powered Land Explained: The Race for Energy Infrastructure',
                       'channel': 'Schneider Electric',
                       'author': 'Schneider Electric',
                       'text': 'It tends to be gas-fired generation more so than others at this point '
                               "because that's what's going to give you the stability 24/7 as opposed to "
                               'the renewables.',
                       'tip': 'It tends to be gas-fired generation more so than others at this point '
                              "because that's what's going to give you the stability 24/7 as opposed to "
                              'the renewables.',
                       'timestamp': 1226,
                       'timestamp_seconds': 1226,
                       'timestamp_label': '[00:20:26]',
                       'url': 'https://www.youtube.com/watch?v=2ORDbZvOirU&t=1226s',
                       'markdown': '[00:20:26](https://www.youtube.com/watch?v=2ORDbZvOirU&t=1226s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'}]}
