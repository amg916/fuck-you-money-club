from __future__ import annotations

CHAPTER_12 = {'id': 'Q12',
 'chapter_id': 'Q12',
 'chapter_number': 12,
 'question_number': 12,
 'slug': 'under-the-lease-cell-site-technology-and-battery-storage-sites',
 'question_prompt': 'How do cell site hardware and battery storage sites actually work, and what makes a '
                    'parcel qualify for a BESS lease?',
 'kicker': 'Q12 / THE BIG MONEY PLAYBOOKS',
 'title': 'Under the Lease: Cell Site Technology and Battery Storage Sites',
 'subtitle': 'Antennas and 5G MIMO, how a call travels through a tower, Starlink micro cell towers, BESS '
             'components (PCS, EMS, BMS), land requirements for battery storage, free land screening '
             'tools, project selection, and BESS financial modeling',
 'layout_template': 'action_worksheet_summary',
 'reading_time_minutes': 15,
 'executive_summary': 'Practitioners agree a battery storage lease is a grid-proximity play: LandGate '
                      'wants 2 to 15 acres next to a substation or under half a mile away, Land Owl '
                      'screens for 5 to 20 acres, power next door, a flat pad and access, and Gore Street '
                      'Capital weighs land, planning, grid cost and lease length before buying '
                      'ready-to-build projects. Leases run 20 to 30 years with upgrade rights. Street '
                      "tools are cheap: Doxy's free site check allows 10 screenings a day and a $9.99 map, "
                      "while Land Owl's map work exposes a listing asking 7.7 times its 2020 sale price. "
                      'Modelers plan for 1.5 to 3.5% annual battery fade and a 20% reserve. On the tower '
                      "side, SpaceX's reported push for 80,000 cell sites collides with a BNP Paribas $100 "
                      'billion build estimate and critics dismissing rooftop microcells.',
 'key_metrics': [{'label': 'Battery Storage Parcel Size',
                  'metric': 'Battery Storage Parcel Size',
                  'value': '2 to 15 acres',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Acreage range LandGate says battery storage developers look for, quite small '
                             'compared to solar farms',
                  'source': 'LandApp by LandGate ([Yes7DTfUfJs @ 00:00:17])'},
                 {'label': 'Maximum Distance to Substation',
                  'metric': 'Maximum Distance to Substation',
                  'value': 'Next to a substation or less than half a mile away',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'LandGate names proximity to substations and transmission lines as one of the '
                             'most important factors for battery storage developers',
                  'source': 'LandApp by LandGate ([Yes7DTfUfJs @ 00:00:33])'},
                 {'label': 'Battery Storage Lease Term',
                  'metric': 'Battery Storage Lease Term',
                  'value': '20 to 30 years',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "LandGate's stated lease length, with the lease needing to allow periodic "
                             'facility upgrades as technology changes',
                  'source': 'LandApp by LandGate ([Yes7DTfUfJs @ 00:01:44])'},
                 {'label': 'SpaceX Cell-Site Access Target',
                  'metric': 'SpaceX Cell-Site Access Target',
                  'value': 'At least 80,000 cell sites',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Bloomberg-reported SpaceX talks naming Crown Castle, which would put SpaceX '
                             'in the same ballpark as AT&T and Verizon at roughly 65,000 to 75,000 towers '
                             'each',
                  'source': 'The Space Flight ([0P3b6pUkElk @ 00:06:48])'}],
 'sections': [{'heading': 'Section 1: The Practitioner Consensus',
               'paragraphs': ['Every land-side operator lands on the same first filter: the wire, not the '
                              "dirt. LandGate's LandApp team tells owners battery storage needs only 2 to "
                              '15 acres, a fraction of a solar farm, and that the pad should sit next to a '
                              'substation or less than half a mile away [Yes7DTfUfJs @ 00:00:17]. Mickey '
                              'at Land Owl runs a tighter rubric of four boxes, the right size at about 5 '
                              'to 20 acres, power next door, a flat pad, and access, then measures a '
                              'Yadkin County, North Carolina listing at 0.35 and 0.47 miles from an '
                              'in-service Duke Energy substation carrying four 100 kV lines [yVhfvSQwGRQ @ '
                              "00:00:19]. Gore Street Capital's investment team scores the same variables "
                              "from the buyer's chair: the cost of the grid connection, the distance to "
                              'substation, the length of the land lease, and the availability of land to '
                              'expand in the future all feed its investment decision [9jXkiEU8op0 @ '
                              '00:01:06]. The Power Hub goes further for UK farm and industrial owners, '
                              'pitching that land with a substation already installed within it can host a '
                              'self-contained battery system built in close proximity, and that the owner '
                              'is handsomely rewarded for facilitating it [zXV1Vy_XECY @ 00:05:15]. '
                              'Acreage is the easy part; proximity is the asset everyone is pricing.',
                              'Every engineer who walks a battery site describes the same hardware on the '
                              'pad. BESS Engineer frames the business as flattening the duck curve, '
                              'charging in the midday belly when solar floods the grid and discharging up '
                              'the neck into the evening peak, then traces the power path from battery '
                              'containers storing DC, to a skid with an inverter and transformer, to '
                              'combiner switchgear, a main step-up transformer, a high-voltage switchyard, '
                              'and the gantry where the utility meters every megawatt in and out '
                              '[Pd5iB85hCLU @ 00:01:37]. Circuit Masterclass lists the same stack of '
                              'storage battery, PCS, EMS, transformer, BMS, fire protection, and cooling, '
                              'and notes lithium-ion only performs efficiently between 20 and 40 degrees C '
                              '[YhDIp_Bjk-I @ 00:05:05]. IndiGrid puts dimensions on it: each container is '
                              'about 20 ft long, 8 ft wide, 9.5 ft high, and weighs 43 tons [x9hN7fa_OOI @ '
                              '00:08:07], and 84 battery units across a 10-acre area form one power asset '
                              'that can supply the entire evening peak of a mid-sized Indian city '
                              "[x9hN7fa_OOI @ 00:23:08]. BESS Engineer's scaling rule matters for anyone "
                              'holding ground under one of these plants: to make the plant bigger, you do '
                              'not build a bigger machine, you repeat the station.',
                              'On paper, LandGate says battery storage leases run 20 to 30 years, the '
                              'developer begins building once the lease is signed, the owner keeps access '
                              'to the rest of the property because the footprint is small, and the '
                              'contract has to allow periodic facility upgrades as technology changes '
                              '[Yes7DTfUfJs @ 00:01:44]. Under a tower lease, the operators agree on an '
                              'equally standard build. Telecom Training explains that instead of one '
                              'antenna covering 360 degrees, the tower divides coverage into three sectors '
                              'of 120 degrees each, which lets millions of phones share the network '
                              'efficiently [tqz39K230_w @ 00:01:27]. Buildrightacademy walks the compound '
                              'from the dirt up: a buried ring of bare copper with ground rods often 8 '
                              'feet long and a common target of 5 ohms or less, then a walk-in shelter or '
                              'slab of outdoor cabinets holding rectifiers that turn utility AC into '
                              '48-volt DC, a battery rack that carries the site for hours rather than '
                              'days, the BBU, and on many sites a generator started by a transfer switch '
                              '[kHmq6jr22Ms @ 00:03:06]. The same instructor says small cells, boxes about '
                              'the size of a backpack hung on street poles or buildings close to the '
                              'street and covering a block or two, are now nearly 40% of all US cell sites '
                              '[kHmq6jr22Ms @ 00:15:04].'],
               'table': {'caption': 'Where the land, investor, and engineering practitioners line up',
                         'headers': ['Consensus Point',
                                     'What Practitioners Say',
                                     'Operator Takeaway',
                                     'Expert Source'],
                         'rows': [['Substation proximity decides whether a parcel qualifies',
                                   'Battery storage should be next to a substation or less than half a '
                                   'mile away',
                                   'Screen distance to the nearest substation before looking at acreage or '
                                   'price',
                                   'LandApp by LandGate ([Yes7DTfUfJs @ 00:00:33])'],
                                  ['Battery storage needs a small footprint compared to solar',
                                   'LandGate cites 2 to 15 acres while Land Owl looks for about 5 to 20 '
                                   'acres',
                                   'Combine adjacent small parcels when one alone sits under the 5-acre '
                                   'bar',
                                   'Land Owl ([yVhfvSQwGRQ @ 00:00:19])'],
                                  ['Being close to a substation is not the same as capacity',
                                   'Only the utility can tell you whether that substation has room for '
                                   'your project',
                                   "Call the utility about capacity before trusting any listing's "
                                   'substation claim',
                                   'Land Owl ([yVhfvSQwGRQ @ 00:01:23])'],
                                  ['Investors buy ready-to-build projects with key rights already secured',
                                   'Ready to build means the land, the planning, and the grid connection '
                                   'are secured',
                                   'Each secured milestone reduces uncertainty and changes what the '
                                   'project is worth',
                                   'Gore Street Capital ([9jXkiEU8op0 @ 00:00:53])'],
                                  ['The duck curve is the core reason batteries get built',
                                   'A BESS charges in the midday belly and discharges up the neck at the '
                                   'evening peak',
                                   'Sites serving grids with heavy midday solar and sharp evening demand '
                                   'fit the model',
                                   'BESS Engineer ([Pd5iB85hCLU @ 00:00:22])'],
                                  ['Battery storage leases are long and must allow technology upgrades',
                                   'Leases vary between 20 to 30 years and need periodic facility upgrade '
                                   'rights',
                                   'Expect the developer to build right after signing while you keep '
                                   'property access',
                                   'LandApp by LandGate ([Yes7DTfUfJs @ 00:01:44])'],
                                  ['Cell towers follow a standard three-sector antenna layout',
                                   'Each antenna is aimed at one 120 degree slice, three slices make 360',
                                   'One tower serves three groups of phones from three antenna directions',
                                   'Buildrightacademy ([kHmq6jr22Ms @ 00:07:07])']]}},
              {'heading': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['Screening starts on a screen, not in a truck. Land Intel walks through '
                              'sitedata.doxy.com, which tracks active 20-acre listings pre-screened for '
                              'power substation and fiber proximity, then runs its free renewable energy '
                              'site check under the I am a landowner investor tab, which allows 10 free '
                              'screenings and two free submissions per day [P_Nhj8ZzbYw @ 00:00:54]. The '
                              'operator enters acreage, in this case a 69-acre property bought after '
                              'running this exact check, drops coordinates, an address, or a pin, and gets '
                              'ratings for power line, substation, and fiber proximity; the $9.99 '
                              'interactive map then layers parcel boundaries, FEMA flood zones, nearest '
                              'substations, transmission line paths, and fiber lines [P_Nhj8ZzbYw @ '
                              '00:02:28]. Land Owl does the same work inside Land id by switching on '
                              'energy, then electric, then substations and transmission lines, clicking '
                              'the substation to confirm it is in service, and reading line voltages and '
                              'utility ownership straight off the map [yVhfvSQwGRQ @ 00:01:00]. LandGate '
                              'adds a battery storage value index score inside its property report and a '
                              'free marketplace where owners list for sale or lease across solar, wind, '
                              'oil and gas, mining, and EV charging with their contact details attached, '
                              'so developers call directly with no middleman [Yes7DTfUfJs @ 00:01:27].',
                              "Mickey's Yadkin County teardown is the cleanest worked example of parcel "
                              'math. The listing is just shy of 13 acres for $350,000, split across a '
                              '3.86-acre parcel and a 9.12-acre parcel, so only the combination clears the '
                              '5-acre bar [yVhfvSQwGRQ @ 00:00:19]. Contours turn up 11 lines from 975 to '
                              '1,025 feet, a 50-foot fall, and the soil survey shows over 95% Clifford '
                              "sandy clay loam at 6 to 10% slopes; Mickey's call is that slope is a cost, "
                              'not necessarily a no, so the operator prices grading, cut, fill, and maybe '
                              'a retaining wall for the flat battery pad [yVhfvSQwGRQ @ 00:01:46]. Then '
                              'the money: the smaller parcel last sold for $17,500 in July 2020 and now '
                              'asks $135,450, about 7.7 times, and the pair last sold for just short of '
                              '$70,000 combined against the $350,000 ask, about five times, while the '
                              'listing claims TZ zoning and the map shows R20 residential and M1 '
                              'industrial [yVhfvSQwGRQ @ 00:02:33]. The Power Hub runs the operator-side '
                              'math for UK businesses: a five-day week leaves potentially 29% of weekly '
                              'usage going to waste, and buying power back costs very likely 5 to 10 times '
                              'what it sold for [zXV1Vy_XECY @ 00:04:18].',
                              'Revenue modeling is where a developer decides what a site is worth. '
                              'eFinancial Models builds price arbitrage directly into its Excel template: '
                              'charge when the grid price is low, including midday hours when solar '
                              'oversupply drives prices down and sometimes negative, discharge when the '
                              'evening price is high, and set battery availability at 95% of days with 5% '
                              'offline [8xq5_kt3OY0 @ 00:14:31]. The same template keeps a 20% minimum '
                              'load that is never discharged because battery suppliers recommend it to '
                              'prolong lifetime, models annual capacity fade of 1.5 to 3.5%, and warns '
                              'that running two cycles per day adds wear that forces a recheck of expected '
                              'lifetime cycles [8xq5_kt3OY0 @ 00:18:30]. IndiGrid confirms that two-cycle '
                              "regime at utility scale, describing India's choice of drawing 2-hour worth "
                              'of energy two times a day as rare worldwide, lowering total cost of '
                              'ownership while stretching the chemistry to its maximum physical limits '
                              '[x9hN7fa_OOI @ 00:21:02]. Policy can rewrite the math: Learn Solar & BESS '
                              "reports Rajasthan's 2025 green open access rules require any renewable "
                              'project over 5 megawatt to include battery storage of at least 5% capacity '
                              'for a minimum of 2 hours, offset by 75 to 100% exemptions on transmission '
                              'charges [i_OH8wyz41M @ 00:02:20].'],
               'table': {'caption': 'Street tools, settings, and numbers practitioners actually use',
                         'headers': ['Mechanic or Tool',
                                     'Exact Number or Setting',
                                     'How Operators Use It',
                                     'Expert Source'],
                         'rows': [['Doxy free renewable energy site check for landowners',
                                   'Up to 10 free screenings and two free submissions per day',
                                   'Rate power line, substation, and fiber proximity before buying or '
                                   'listing',
                                   'Land Intel - Land Investing ([P_Nhj8ZzbYw @ 00:00:54])'],
                                  ['Doxy interactive infrastructure map for a single site',
                                   'Unlocked for $9.99 per site with street and satellite views',
                                   'See parcel boundaries, FEMA flood zones, substations, transmission '
                                   'paths, and fiber',
                                   'Land Intel - Land Investing ([P_Nhj8ZzbYw @ 00:02:28])'],
                                  ['Land id contour lines and soil survey layers',
                                   '50 feet of fall with over 95% at 6 to 10% slopes',
                                   'Price grading, cut, fill, and maybe a retaining wall for the pad',
                                   'Land Owl ([yVhfvSQwGRQ @ 00:01:46])'],
                                  ['Last-sale versus asking-price markup check on listings',
                                   '$17,500 in July 2020 against a $135,450 ask, about 7.7 times',
                                   'Expose listings priced on a battery storage story instead of the map',
                                   'Land Owl ([yVhfvSQwGRQ @ 00:02:06])'],
                                  ['Battery capacity fade assumption in the financial model',
                                   '1.5 to 3.5% per year depending on source, gradual or accelerating',
                                   'Plan battery replacement as capex or refurbishment as opex in the '
                                   'forecast',
                                   'eFinancial Models ([8xq5_kt3OY0 @ 00:14:53])'],
                                  ['Minimum load reserve kept inside the battery at all times',
                                   '20% of installed capacity is never discharged during cycling',
                                   'Follow supplier guidance to prolong lifetime and optionally sell the '
                                   'reserve',
                                   'eFinancial Models ([8xq5_kt3OY0 @ 00:18:30])'],
                                  ['Tower structural analysis before adding heavier 5G panels',
                                   'ANSI/TIA-222 check answers yes or reinforce the pole first',
                                   'Heavier panels add wind load, so the check comes before the climb',
                                   'Buildrightacademy ([kHmq6jr22Ms @ 00:15:43])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'What the operators do before anyone signs',
                           'body': 'Four moves the practitioners use to protect price and position on a '
                                   'battery or tower site.',
                           'items': ['Trust the map over the listing: the listing tells you what you want '
                                     'to hear and the map shows you what you need to see, so confirm '
                                     'substation capacity with the utility and zoning with the county '
                                     '[Land Owl — yVhfvSQwGRQ @ 00:02:53].',
                                     "Learn your state's renewable energy incentives before talking to a "
                                     'developer; few owners know them and understanding them gives a leg '
                                     'up during negotiations [LandApp by LandGate — Yes7DTfUfJs @ '
                                     '00:00:51].',
                                     'Start small and learn the curve: IndiGrid ran a 250 kWh pilot at one '
                                     'of its existing substations before bidding standalone utility-scale '
                                     'projects and grew to 2.5 GW [IndiGrid Infrastructure Trust — '
                                     'x9hN7fa_OOI @ 00:06:50].',
                                     'Timing is the price: invest too early and you carry planning, land, '
                                     'and grid risk, too late and someone else captured the value; Gore '
                                     'Street uses in-house construction expertise to enter earlier at more '
                                     'attractive pricing [Gore Street Capital — 9jXkiEU8op0 @ 00:05:40].']},
               'sop_steps': [{'step': 1,
                              'title': 'Run the free remote screen',
                              'action': "Enter acreage and location into Doxy's free site check and read "
                                        'the power line, substation, and fiber ratings.',
                              'detail': 'Enter acreage, then coordinates, a street address, a dropped pin, '
                                        'or your current location, click analyze site, and the system '
                                        'checks power infrastructure and site proximity in real time; the '
                                        '$9.99 map adds flood zones and fiber lines [Land Intel - Land '
                                        'Investing — P_Nhj8ZzbYw @ 00:01:42].'},
                             {'step': 2,
                              'title': 'Measure substation distance, then ask about capacity',
                              'action': 'Confirm the nearest substation is in service and inside half a '
                                        'mile, then call the utility.',
                              'detail': 'LandGate wants the site next to a substation or less than half a '
                                        'mile away [LandApp by LandGate — Yes7DTfUfJs @ 00:00:33]; Land '
                                        'Owl warns close is not capacity and only the utility can say if '
                                        'the substation has room [Land Owl — yVhfvSQwGRQ @ 00:01:23].'},
                             {'step': 3,
                              'title': 'Price the pad and the zoning',
                              'action': 'Turn on contours and soils, price the earthwork, and verify which '
                                        'zoning actually applies.',
                              'detail': 'Count contour lines and slope classes and price grading, cut, '
                                        'fill, and retaining walls [Land Owl — yVhfvSQwGRQ @ 00:01:46]; '
                                        'when a listing says TZ and the map shows R20 and M1, ask the '
                                        'county which applies [Land Owl — yVhfvSQwGRQ @ 00:02:33].'},
                             {'step': 4,
                              'title': 'Put the site in front of developers',
                              'action': 'List the property free on a marketplace or submit the screened '
                                        'site for developer introductions.',
                              'detail': 'LandGate lists for sale or lease free with your contact details '
                                        'so developers contact you directly with no middleman [LandApp by '
                                        'LandGate — Yes7DTfUfJs @ 00:02:15]; Doxel introduces qualifying '
                                        'land to solar, BESS, and data center developers [Land Intel - '
                                        'Land Investing — P_Nhj8ZzbYw @ 00:02:12].'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The land-side players do not agree on the size of the box or on who should '
                              'stand between the owner and the developer. LandGate pegs battery storage '
                              'sites at 2 to 15 acres and wants the parcel next to a substation or less '
                              'than half a mile away [Yes7DTfUfJs @ 00:00:17]. Mickey at Land Owl runs a '
                              'wider band of about 5 to 20 acres, stacks two parcels of 3.86 and 9.12 '
                              "acres to clear the bar, then warns that close isn't the same as capacity "
                              'and only the utility can tell you if that substation has room for you '
                              '[yVhfvSQwGRQ @ 00:00:19]. Land Intel goes bigger again, pulling 20-acre '
                              'listings pre-screened for substations and fiber and running a 69-acre '
                              'purchase through the Doxel site check before buying [P_Nhj8ZzbYw @ '
                              '00:01:11]. The route to the developer splits three ways. LandGate offers a '
                              'free marketplace listing with your contact information exposed, no '
                              'middleman, and no obligation to accept any offer. Doxel screens the '
                              'submission and introduces qualifying land to solar, BESS and data center '
                              'developers. The Power Hub pitches the opposite of direct dealing: you bring '
                              'the land, they bring the investors, the planning knowledge and the '
                              'energy-supplier relationships, and they manage the whole process from start '
                              'to finish [zXV1Vy_XECY @ 00:05:50].',
                              'On the capital side, the split is about when to step in and how hard to run '
                              "the asset. Gore Street Capital's baseline is acquiring projects ready to "
                              'build, with land, planning and grid connection secured, because investing '
                              'too early means unnecessary planning, land and grid risk while investing '
                              'too late means someone else already captured much of the value [9jXkiEU8op0 '
                              '@ 00:02:33]. Yet the same desk says in-house construction and technical '
                              'expertise lets it invest earlier than many other investors, at more '
                              'attractive pricing, and calls that early entry the repeatable source of its '
                              'outsized returns [9jXkiEU8op0 @ 00:05:28]. IndiGrid took a slower ladder: a '
                              '250 kWh pilot at one of its existing substations to learn the nuances, then '
                              'standalone utility-scale bids, and now 2.5 GW scale [x9hN7fa_OOI @ '
                              '00:06:50]. Dispatch strategy splits the same way. The eFinancial Models '
                              'template lets an operator charge only from excess solar, from all solar, or '
                              'buy from the grid for price arbitrage; the modeler pushes arbitrage to '
                              'fully utilize the battery while flagging that two cycles a day means more '
                              'wear and tear [8xq5_kt3OY0 @ 00:25:21]. Switch to solar-only and the model '
                              'drops to one charge-discharge cycle, leaving the morning uncovered unless '
                              'the battery is very big.',
                              'Under the cell-site lease, the fight is whether the big tower keeps its '
                              'rent or gets carved into rooftops. The Space Flight reports SpaceX in talks '
                              'to access at least 80,000 US cell sites, with Crown Castle named and its '
                              "CEO saying you can assume we're talking to all parties; Crown's stock "
                              'jumped while AT&T and T-Mobile each fell nearly 8% [0P3b6pUkElk @ '
                              '00:06:48]. Musk then pitched a microcell you could put on your roof like a '
                              'Starlink dish, scattered through densely populated areas instead of big '
                              'cell towers all over the place [0P3b6pUkElk @ 00:09:54]. The skeptics hit '
                              'back hard: femtocells usually cover only the area around a single building, '
                              'New Street Research called the earlier femtocell plan not feasible, '
                              "T-Mobile's outgoing CFO called it laughable, and Qualcomm's own executive "
                              "said we're not doing small cells over here [0P3b6pUkElk @ 00:13:36]. "
                              'Buildright Academy counters that small cells, backpack-sized boxes on '
                              'street poles covering a block or two, are already nearly 40% of all US cell '
                              'sites, while one tower covers miles [kHmq6jr22Ms @ 00:15:04]. Musk also '
                              'said AT&T, Verizon and others will not go out of business, expecting '
                              'bandwidth demand from AI and robots to be tremendous.'],
               'table': {'caption': 'Battery storage land and cell-site playbooks practitioners run '
                                    'against each other',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Target parcel size for a battery storage lease site',
                                   'LandGate targets 2 to 15 acres, small compared to solar farms',
                                   'Land Owl targets about 5 to 20 acres, stacking adjacent parcels to '
                                   'clear the bar',
                                   'LandGate ([Yes7DTfUfJs @ 00:00:17]); Land Owl ([yVhfvSQwGRQ @ '
                                   '00:00:19])'],
                                  ['How close the substation must be to the parcel',
                                   'Next to a substation or less than half a mile away',
                                   '0.35 and 0.47 miles pass on the map, but only the utility confirms '
                                   'capacity',
                                   'LandApp by LandGate ([Yes7DTfUfJs @ 00:00:33]); Land Owl ([yVhfvSQwGRQ '
                                   '@ 00:01:00])'],
                                  ['How the landowner reaches the battery storage developer',
                                   'Free marketplace listing, contact details exposed, no middleman, no '
                                   'obligation to accept',
                                   'Hand the land to a firm that organizes investors, planning and '
                                   'suppliers start to finish',
                                   'LandApp by LandGate ([Yes7DTfUfJs @ 00:02:15]); The Power Hub '
                                   '([zXV1Vy_XECY @ 00:05:50])'],
                                  ['Which screening tool runs the first pass on land',
                                   'Doxel free site check with 10 screenings and two submissions per day',
                                   'Land id map layers for contours, soils, zoning, substations and last '
                                   'sale price',
                                   'Land Intel - Land Investing ([P_Nhj8ZzbYw @ 00:00:54]); Land Owl '
                                   '([yVhfvSQwGRQ @ 00:01:23])'],
                                  ['When investor capital enters a battery storage project',
                                   'Acquire at ready-to-build once land, planning and grid connection are '
                                   'secured',
                                   'Enter earlier using in-house construction expertise to buy at more '
                                   'attractive pricing',
                                   'Gore Street Capital ([9jXkiEU8op0 @ 00:00:53]); Gore Street Capital '
                                   '([9jXkiEU8op0 @ 00:05:28])'],
                                  ['Where a multi-site corporate buyer places its batteries',
                                   'Consumer-end batteries at urban offices give instant backup and zero '
                                   'transmission loss at a premium',
                                   'Plant-end shared batteries at remote solar farms are cheaper per '
                                   'megawatt but a scheduling nightmare',
                                   'Learn Solar & BESS ([i_OH8wyz41M @ 00:05:46])'],
                                  ['How a new wireless entrant builds its cell network',
                                   'Lease roughly 80,000 tower sites fitted with Qualcomm 64 by 64 massive '
                                   'MIMO radios',
                                   'Rooftop microcell like a Starlink dish, which critics dismissed as '
                                   'laughable and not feasible',
                                   'The Space Flight ([0P3b6pUkElk @ 00:06:48]); The Space Flight '
                                   '([0P3b6pUkElk @ 00:13:36])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ["The first trap is the listing itself. Land Owl's Yadkin County, North "
                              'Carolina test case asks 350,000 for just shy of 13 acres and advertises a '
                              'Duke power substation a quarter mile away; the map puts it at 0.35 and 0.47 '
                              'miles from the two parcels, in service with four lines at 100 kV, but '
                              'nobody except the utility can confirm capacity [yVhfvSQwGRQ @ 00:01:00]. '
                              'The cleared site is not flat: 11 contour lines cross the parcel from 975 to '
                              '1,025 feet, 50 feet of fall on Clifford sandy clay loam at 6 to 10% slopes, '
                              'so grading, cut, fill and maybe a retaining wall go into the price '
                              '[yVhfvSQwGRQ @ 00:01:23]. Then the price and zoning: one parcel last sold '
                              'for $17,500 in July 2020 and now asks 135,450, about 7.7 times its last '
                              'sale, the pair last sold for just short of 70,000 combined and now asks '
                              'five times as much, and the listing claims TZ zoning while the map shows '
                              'R20 residential and M1 industrial [yVhfvSQwGRQ @ 00:02:06]. LandGate adds '
                              'the term trap: leases run 20 to 30 years and must allow periodic facility '
                              'upgrades as technology changes [Yes7DTfUfJs @ 00:01:44]. The Land Owl '
                              'verdict: the listing tells you what you want to hear.',
                              "Build-out is where the schedule breaks. IndiGrid's Sanand battery "
                              'containers run about 20 feet long, 8 feet wide, 9.5 feet high and 43 tons '
                              'each, and shock, vibration or temperature deviation can permanently damage '
                              'internal cell structure; the site team warns any damage can lead to an '
                              'explosion, and unloading one container took more than 3 hours just from '
                              'trailer to ground [x9hN7fa_OOI @ 00:08:07]. Laying the heavy cables needs '
                              'at least 15 to 20 people, and any damage to a cable means repeating the job '
                              '[x9hN7fa_OOI @ 00:15:28]. Then the EMS data layer slipped, producing tense '
                              'moments on site from a manager who was under the impression the gear was '
                              'fully ready, just power plug and the project is complete [x9hN7fa_OOI @ '
                              '00:16:07]. Gore Street Capital lists the same bleed points in sequence: '
                              'regulatory risk with tariffs imposed within a short duration, construction '
                              'delays that heavily impact the investment case, and revenue streams that '
                              "evolve so you may not have the same ones by the time you're operational "
                              "[9jXkiEU8op0 @ 00:04:32]. The desk's counter is aligning construction "
                              'programs with lawyers around likely regulatory changes and building a '
                              'system capable of adapting rather than one locked to day-one revenue.',
                              'The economics check starts with fade. eFinancial Models cites battery '
                              'capacity degradation of 1.5 to 3.5% per year depending on source, offers '
                              'fading curves that accelerate with age, and treats a refill or recycling '
                              'supplier bringing capacity back to 95% as a scenario only if such a '
                              'supplier can be found [8xq5_kt3OY0 @ 00:15:13]. The same template runs 95% '
                              'battery availability, holds 20% as a never-discharged minimum load per '
                              'supplier guidance, and warns battery lifetimes are much shorter than the '
                              'solar farm, triggering replacement capex or an opex refill line '
                              "[8xq5_kt3OY0 @ 00:08:00]. The modeler's fix is calibration: if lifetime "
                              'cycles climb too high under a two-cycle plan, adjust the expected lifetime '
                              'until the numbers make sense. Learn Solar & BESS names staggering upfront '
                              'capital, a dangerous reliance on imported lithium, no standardized '
                              'integration policies, and ambiguous rules on recovering costs as '
                              'compounding bottlenecks hitting developers all at once [i_OH8wyz41M @ '
                              '00:06:15]. On the tower side, the cost check is steel: a 5G panel is often '
                              'heavier with more wind load, so an engineer runs a structural analysis '
                              'against ANSI/TIA-222, and sometimes the answer is reinforce the pole first, '
                              'before anyone climbs [kHmq6jr22Ms @ 00:15:43].'],
               'table': {'caption': 'Failure modes practitioners hit on battery storage land and cell-site '
                                    'steel',
                         'headers': ['Failure Mode',
                                     'What Happened Firsthand',
                                     'Economics Check',
                                     'Expert Source'],
                         'rows': [['Listing advertises a substation a quarter mile away',
                                   'Map shows 0.35 and 0.47 miles to an in-service 100 kV substation',
                                   'Ask the utility about capacity before paying for proximity',
                                   'Land Owl ([yVhfvSQwGRQ @ 00:01:00])'],
                                  ['Cleared site mistaken for a flat battery pad',
                                   '50 feet of fall across 11 contour lines at 6 to 10% slopes',
                                   'Price grading, cut, fill and possibly a retaining wall into the deal',
                                   'Land Owl ([yVhfvSQwGRQ @ 00:01:23])'],
                                  ['Asking price inflated far past the last recorded sale',
                                   'One parcel asks about 7.7 times its $17,500 July 2020 sale',
                                   'Pull sale history and confirm zoning with the county before offering',
                                   'Land Owl ([yVhfvSQwGRQ @ 00:02:06])'],
                                  ['Battery container damaged in transport or unloading',
                                   '43-ton containers where shock or vibration can damage cells and risk '
                                   'explosion',
                                   'Plan port-to-site moves as precision operations taking hours per '
                                   'container',
                                   'IndiGrid Infrastructure Trust ([x9hN7fa_OOI @ 00:08:27])'],
                                  ['EMS data connectivity lags behind the power equipment',
                                   'Site leadership assumed plug-and-play readiness and hit delays and '
                                   'tense moments',
                                   'Budget integration and pre-commissioning tests before promising '
                                   'energization dates',
                                   'IndiGrid Infrastructure Trust ([x9hN7fa_OOI @ 00:16:07])'],
                                  ['Battery capacity fades faster than the pro forma assumed',
                                   'Degradation of 1.5 to 3.5% yearly plus extra wear from two daily '
                                   'cycles',
                                   'Recheck lifetime cycles and model replacement as capex or opex refill',
                                   'eFinancial Models ([8xq5_kt3OY0 @ 00:15:13])'],
                                  ['Heavier 5G panel overloads existing tower steel',
                                   'New panels add weight and wind load beyond original ANSI/TIA-222 '
                                   'design',
                                   'Run structural analysis and reinforce the pole before the climb',
                                   'Buildrightacademy ([kHmq6jr22Ms @ 00:15:43])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Four checks before you sign, buy or climb',
                           'body': 'Every item below comes from a trap practitioners hit or flagged on '
                                   'live land listings, battery sites and tower upgrades. Clear all four '
                                   'before money moves.',
                           'items': ['Get substation capacity from the utility, not the listing: the '
                                     'substation can be real and in service yet still have no room for you '
                                     '[Land Owl — yVhfvSQwGRQ @ 00:02:53].',
                                     "Turn on contour lines and the soil survey before trusting 'cleared': "
                                     '50 feet of fall on 6 to 10% slopes turns into grading, cut and fill '
                                     'costs [Land Owl — yVhfvSQwGRQ @ 00:01:23].',
                                     'Confirm EMS data cabling and integration are on schedule, not just '
                                     'power gear, before setting a commissioning date [IndiGrid '
                                     'Infrastructure Trust — x9hN7fa_OOI @ 00:16:07].',
                                     'Run a structural analysis on the tower before any heavier 5G panel '
                                     'goes up; sometimes the answer is reinforce the pole first '
                                     '[Buildrightacademy — kHmq6jr22Ms @ 00:15:43].']}}],
 'pull_quote': '"The listing tells you what you want to hear. The map shows you what you need to see." '
               'Land Owl (yVhfvSQwGRQ @ 00:02:53).',
 'diagram_id': 'diag-08',
 'action_checklist': ['Run the free Doxel site check with acreage and a dropped pin, using up to 10 '
                      'screenings and two submissions per day, and only submit sites rating well on power '
                      'line, substation and fiber proximity [Land Intel - Land Investing — P_Nhj8ZzbYw @ '
                      '00:00:54].',
                      'Map substations and transmission lines around the parcel and target 2 to 15 acres '
                      'sitting next to a substation or under half a mile away [LandApp by LandGate — '
                      'Yes7DTfUfJs @ 00:00:33].',
                      'Score every parcel on the four Land Owl tests: right size of about 5 to 20 acres, '
                      'power next door, a flat pad, and road access with frontage [Land Owl — yVhfvSQwGRQ '
                      '@ 00:00:19].',
                      "Compare the listing's zoning claim against the map and ask the county which zoning "
                      'applies before making an offer [Land Owl — yVhfvSQwGRQ @ 00:02:33].',
                      'Before pitching investors, lock land, planning and grid connection, and document '
                      'grid connection cost, substation distance, land lease length and room to expand '
                      '[Gore Street Capital — 9jXkiEU8op0 @ 00:01:06].',
                      'Model the battery with 95% availability, a 20% minimum load reserve and annual fade '
                      'before trusting any arbitrage return [eFinancial Models — 8xq5_kt3OY0 @ 00:14:31].'],
 'statutory_citations': [{'title': 'Land Owl — What Makes Land Good For A Battery Storage Project '
                                   '[00:00:19]',
                          'url': 'https://www.youtube.com/watch?v=yVhfvSQwGRQ&t=19s',
                          'relevance': 'Primary practitioner testimony on the four-part battery storage '
                                       'land test and the listing-versus-map due diligence traps.'},
                         {'title': 'Gore Street Capital — How We Choose Battery Storage Projects: The '
                                   'Investment Case for BESS [00:02:33]',
                          'url': 'https://www.youtube.com/watch?v=9jXkiEU8op0&t=153s',
                          'relevance': 'Primary practitioner testimony on investment timing, '
                                       'ready-to-build criteria and regulatory, construction and revenue '
                                       'risk.'},
                         {'title': "IndiGrid Infrastructure Trust — Inside India's Biggest Utility-Scale "
                                   'BESS | The Energy Storage | IndiGrid × National Geographic [00:08:07]',
                          'url': 'https://www.youtube.com/watch?v=x9hN7fa_OOI&t=487s',
                          'relevance': 'Primary practitioner testimony on utility-scale battery site '
                                       'construction, container logistics and EMS integration delays.'},
                         {'title': 'Buildrightacademy — How a Cell Tower Actually Works: A Phone Call, '
                                   'Ground to Sky [00:15:43]',
                          'url': 'https://www.youtube.com/watch?v=kHmq6jr22Ms&t=943s',
                          'relevance': 'Primary practitioner testimony on cell-site structural loading, 5G '
                                       'upgrades and small cell share of US sites.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'tqz39K230_w',
                       'title': 'What’s Inside a Cell Tower Antenna? | Cellular Antennas Explained',
                       'channel': 'Telecom Training',
                       'author': 'Telecom Training',
                       'text': 'Instead of there being one antenna on the base station covering every '
                               'direction equally, the tower usually divides coverage into three sectors, '
                               'with each sector having antennas covering 120 degrees.',
                       'tip': 'Instead of there being one antenna on the base station covering every '
                              'direction equally, the tower usually divides coverage into three sectors, '
                              'with each sector having antennas covering 120 degrees.',
                       'timestamp': 87,
                       'timestamp_seconds': 87,
                       'timestamp_label': '[00:01:27]',
                       'url': 'https://www.youtube.com/watch?v=tqz39K230_w&t=87s',
                       'markdown': '[00:01:27](https://www.youtube.com/watch?v=tqz39K230_w&t=87s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Yes7DTfUfJs',
                       'title': 'Does My Land Qualify for Battery Storage?',
                       'channel': 'LandApp by LandGate',
                       'author': 'LandApp by LandGate',
                       'text': 'Battery storage should be next to a substation or less than half a mile '
                               'away.',
                       'tip': 'Battery storage should be next to a substation or less than half a mile '
                              'away.',
                       'timestamp': 33,
                       'timestamp_seconds': 33,
                       'timestamp_label': '[00:00:33]',
                       'url': 'https://www.youtube.com/watch?v=Yes7DTfUfJs&t=33s',
                       'markdown': '[00:00:33](https://www.youtube.com/watch?v=Yes7DTfUfJs&t=33s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Yes7DTfUfJs',
                       'title': 'Does My Land Qualify for Battery Storage?',
                       'channel': 'LandApp by LandGate',
                       'author': 'LandApp by LandGate',
                       'text': 'The length of these leases can vary between 20 to 30 years and will need '
                               'to allow periodic facility upgrades throughout the years depending on '
                               'technology updates.',
                       'tip': 'The length of these leases can vary between 20 to 30 years and will need to '
                              'allow periodic facility upgrades throughout the years depending on '
                              'technology updates.',
                       'timestamp': 104,
                       'timestamp_seconds': 104,
                       'timestamp_label': '[00:01:44]',
                       'url': 'https://www.youtube.com/watch?v=Yes7DTfUfJs&t=104s',
                       'markdown': '[00:01:44](https://www.youtube.com/watch?v=Yes7DTfUfJs&t=104s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'zXV1Vy_XECY',
                       'title': 'Battery Energy Storage Systems (BESS)',
                       'channel': 'The Power Hub',
                       'author': 'The Power Hub',
                       'text': 'If your land, be it a farm or industrial land, happens to have a '
                               "substation installed within it, there's a real possibility that a "
                               'self-contained battery energy storage system could be built in close '
                               'proximity to it to help facilitate the grid.',
                       'tip': 'If your land, be it a farm or industrial land, happens to have a substation '
                              "installed within it, there's a real possibility that a self-contained "
                              'battery energy storage system could be built in close proximity to it to '
                              'help facilitate the grid.',
                       'timestamp': 315,
                       'timestamp_seconds': 315,
                       'timestamp_label': '[00:05:15]',
                       'url': 'https://www.youtube.com/watch?v=zXV1Vy_XECY&t=315s',
                       'markdown': '[00:05:15](https://www.youtube.com/watch?v=zXV1Vy_XECY&t=315s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Pd5iB85hCLU',
                       'title': 'How a BESS Site Works: Batteries to Grid | BESS Decoded Ep. 1',
                       'channel': 'BESS Engineer',
                       'author': 'BESS Engineer',
                       'text': "Batteries plus one skid make an energy station. That's the building block. "
                               "To make the plant bigger, you don't build a bigger machine. You repeat the "
                               'station.',
                       'tip': "Batteries plus one skid make an energy station. That's the building block. "
                              "To make the plant bigger, you don't build a bigger machine. You repeat the "
                              'station.',
                       'timestamp': 79,
                       'timestamp_seconds': 79,
                       'timestamp_label': '[00:01:19]',
                       'url': 'https://www.youtube.com/watch?v=Pd5iB85hCLU&t=79s',
                       'markdown': '[00:01:19](https://www.youtube.com/watch?v=Pd5iB85hCLU&t=79s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'x9hN7fa_OOI',
                       'title': "Inside India's Biggest Utility-Scale BESS | The Energy Storage | IndiGrid "
                                '× National Geographic',
                       'channel': 'IndiGrid Infrastructure Trust',
                       'author': 'IndiGrid Infrastructure Trust',
                       'text': 'The complete operation has taken us more than 3 hours just to take it from '
                               'the trailer and put it on the ground.',
                       'tip': 'The complete operation has taken us more than 3 hours just to take it from '
                              'the trailer and put it on the ground.',
                       'timestamp': 614,
                       'timestamp_seconds': 614,
                       'timestamp_label': '[00:10:14]',
                       'url': 'https://www.youtube.com/watch?v=x9hN7fa_OOI&t=614s',
                       'markdown': '[00:10:14](https://www.youtube.com/watch?v=x9hN7fa_OOI&t=614s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'YhDIp_Bjk-I',
                       'title': 'Battery Energy Storage System (BESS) Explained | Layout, PCS, EMS, BMS & '
                                'Working Principle',
                       'channel': 'Circuit Masterclass',
                       'author': 'Circuit Masterclass',
                       'text': 'Lithium ion batteries perform efficiently only within a temperature range '
                               'of 20 degrees C to 40 degrees, therefore cooling systems are required to '
                               'maintain the battery temperature within this range.',
                       'tip': 'Lithium ion batteries perform efficiently only within a temperature range '
                              'of 20 degrees C to 40 degrees, therefore cooling systems are required to '
                              'maintain the battery temperature within this range.',
                       'timestamp': 305,
                       'timestamp_seconds': 305,
                       'timestamp_label': '[00:05:05]',
                       'url': 'https://www.youtube.com/watch?v=YhDIp_Bjk-I&t=305s',
                       'markdown': '[00:05:05](https://www.youtube.com/watch?v=YhDIp_Bjk-I&t=305s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'yVhfvSQwGRQ',
                       'title': 'What Makes Land Good For A Battery Storage Project',
                       'channel': 'Land Owl',
                       'author': 'Land Owl',
                       'text': 'The substation is real and in service, but over a quarter of a mile away. '
                               'Ask the utility about capacity. The listing tells you what you want to '
                               'hear. The map shows you what you need to see.',
                       'tip': 'The substation is real and in service, but over a quarter of a mile away. '
                              'Ask the utility about capacity. The listing tells you what you want to '
                              'hear. The map shows you what you need to see.',
                       'timestamp': 173,
                       'timestamp_seconds': 173,
                       'timestamp_label': '[00:02:53]',
                       'url': 'https://www.youtube.com/watch?v=yVhfvSQwGRQ&t=173s',
                       'markdown': '[00:02:53](https://www.youtube.com/watch?v=yVhfvSQwGRQ&t=173s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'P_Nhj8ZzbYw',
                       'title': 'How to Check ANY Land for Solar, BESS & Data Center Potential for FREE',
                       'channel': 'Land Intel - Land Investing',
                       'author': 'Land Intel - Land Investing',
                       'text': 'Landowners and investors are free to use up to 10 free screenings per day '
                               'and two free submissions to Doxy per day.',
                       'tip': 'Landowners and investors are free to use up to 10 free screenings per day '
                              'and two free submissions to Doxy per day.',
                       'timestamp': 54,
                       'timestamp_seconds': 54,
                       'timestamp_label': '[00:00:54]',
                       'url': 'https://www.youtube.com/watch?v=P_Nhj8ZzbYw&t=54s',
                       'markdown': '[00:00:54](https://www.youtube.com/watch?v=P_Nhj8ZzbYw&t=54s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '8xq5_kt3OY0',
                       'title': 'Solar BESS Battery Energy Storage Systems Financial (Excel Template) '
                                'Walkthrough',
                       'channel': 'eFinancial Models',
                       'author': 'eFinancial Models',
                       'text': 'Batteries are subject to a degression in their capacity to store '
                               'electricity over time; depending on source, 1.5 to 3.5% per year, so this '
                               'is something material.',
                       'tip': 'Batteries are subject to a degression in their capacity to store '
                              'electricity over time; depending on source, 1.5 to 3.5% per year, so this '
                              'is something material.',
                       'timestamp': 913,
                       'timestamp_seconds': 913,
                       'timestamp_label': '[00:15:13]',
                       'url': 'https://www.youtube.com/watch?v=8xq5_kt3OY0&t=913s',
                       'markdown': '[00:15:13](https://www.youtube.com/watch?v=8xq5_kt3OY0&t=913s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'i_OH8wyz41M',
                       'title': 'Battery Energy Storage System - BESS | Explained |  #Learnsolar&bess '
                                '#BESS',
                       'channel': 'Learn Solar & BESS',
                       'author': 'Learn Solar & BESS',
                       'text': 'The upfront capital costs are just absolutely staggering right now, plus '
                               'we barely manufacture these things locally, meaning we have a dangerous '
                               'reliance on imported lithium.',
                       'tip': 'The upfront capital costs are just absolutely staggering right now, plus we '
                              'barely manufacture these things locally, meaning we have a dangerous '
                              'reliance on imported lithium.',
                       'timestamp': 393,
                       'timestamp_seconds': 393,
                       'timestamp_label': '[00:06:33]',
                       'url': 'https://www.youtube.com/watch?v=i_OH8wyz41M&t=393s',
                       'markdown': '[00:06:33](https://www.youtube.com/watch?v=i_OH8wyz41M&t=393s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '9jXkiEU8op0',
                       'title': 'How We Choose Battery Storage Projects: The Investment Case for BESS',
                       'channel': 'Gore Street Capital',
                       'author': 'Gore Street Capital',
                       'text': 'Invest too early and you take on unnecessary planning, land and grid risk. '
                               'Invest too late and someone else has already captured much of the value.',
                       'tip': 'Invest too early and you take on unnecessary planning, land and grid risk. '
                              'Invest too late and someone else has already captured much of the value.',
                       'timestamp': 153,
                       'timestamp_seconds': 153,
                       'timestamp_label': '[00:02:33]',
                       'url': 'https://www.youtube.com/watch?v=9jXkiEU8op0&t=153s',
                       'markdown': '[00:02:33](https://www.youtube.com/watch?v=9jXkiEU8op0&t=153s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '9jXkiEU8op0',
                       'title': 'How We Choose Battery Storage Projects: The Investment Case for BESS',
                       'channel': 'Gore Street Capital',
                       'author': 'Gore Street Capital',
                       'text': 'There are also site-specific considerations which can impact project '
                               'viability, such as the cost of the grid connection, the distance to '
                               'substation, the length of the land lease, and the availability of land to '
                               'expand in the future.',
                       'tip': 'There are also site-specific considerations which can impact project '
                              'viability, such as the cost of the grid connection, the distance to '
                              'substation, the length of the land lease, and the availability of land to '
                              'expand in the future.',
                       'timestamp': 66,
                       'timestamp_seconds': 66,
                       'timestamp_label': '[00:01:06]',
                       'url': 'https://www.youtube.com/watch?v=9jXkiEU8op0&t=66s',
                       'markdown': '[00:01:06](https://www.youtube.com/watch?v=9jXkiEU8op0&t=66s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '72KjPI3DpJ0',
                       'title': 'What Is BESS? Battery Energy Storage System Explained Simply',
                       'channel': 'Learn Solar & BESS',
                       'author': 'Learn Solar & BESS',
                       'text': 'Second is speed. They can dump power into the grid in milliseconds, way '
                               'faster than an old-school power plant can spin up.',
                       'tip': 'Second is speed. They can dump power into the grid in milliseconds, way '
                              'faster than an old-school power plant can spin up.',
                       'timestamp': 317,
                       'timestamp_seconds': 317,
                       'timestamp_label': '[00:05:17]',
                       'url': 'https://www.youtube.com/watch?v=72KjPI3DpJ0&t=317s',
                       'markdown': '[00:05:17](https://www.youtube.com/watch?v=72KjPI3DpJ0&t=317s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'zDZJfjUxezU',
                       'title': 'HOW 5G MIMO ANTENNAS WORK',
                       'channel': 'Telecom Training',
                       'author': 'Telecom Training',
                       'text': 'Anything larger than 4x4 is referred to as massive MIMO; they all refer to '
                               'as massive MIMO except for 4x4.',
                       'tip': 'Anything larger than 4x4 is referred to as massive MIMO; they all refer to '
                              'as massive MIMO except for 4x4.',
                       'timestamp': 110,
                       'timestamp_seconds': 110,
                       'timestamp_label': '[00:01:50]',
                       'url': 'https://www.youtube.com/watch?v=zDZJfjUxezU&t=110s',
                       'markdown': '[00:01:50](https://www.youtube.com/watch?v=zDZJfjUxezU&t=110s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '0P3b6pUkElk',
                       'title': 'Elon Musk Just Revealed Starlink Micro Cell Towers — And Big Wireless Is '
                                'In Trouble',
                       'channel': 'The Space Flight',
                       'author': 'The Space Flight',
                       'text': 'BNP Paribas estimates that SpaceX would need to spend at least $100 '
                               'billion to build a terrestrial network through tower leases, and that does '
                               'not include any additional spectrum.',
                       'tip': 'BNP Paribas estimates that SpaceX would need to spend at least $100 billion '
                              'to build a terrestrial network through tower leases, and that does not '
                              'include any additional spectrum.',
                       'timestamp': 856,
                       'timestamp_seconds': 856,
                       'timestamp_label': '[00:14:16]',
                       'url': 'https://www.youtube.com/watch?v=0P3b6pUkElk&t=856s',
                       'markdown': '[00:14:16](https://www.youtube.com/watch?v=0P3b6pUkElk&t=856s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'MT8oXJXtzq4',
                       'title': 'How Do Cell Towers Actually Work?',
                       'channel': 'History of Simple Things',
                       'author': 'History of Simple Things',
                       'text': 'Small cells are often mounted on utility poles or buildings, providing '
                               'more localized coverage in high-traffic areas like downtowns, stadiums, or '
                               'airports.',
                       'tip': 'Small cells are often mounted on utility poles or buildings, providing more '
                              'localized coverage in high-traffic areas like downtowns, stadiums, or '
                              'airports.',
                       'timestamp': 359,
                       'timestamp_seconds': 359,
                       'timestamp_label': '[00:05:59]',
                       'url': 'https://www.youtube.com/watch?v=MT8oXJXtzq4&t=359s',
                       'markdown': '[00:05:59](https://www.youtube.com/watch?v=MT8oXJXtzq4&t=359s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'kHmq6jr22Ms',
                       'title': 'How a Cell Tower Actually Works: A Phone Call, Ground to Sky',
                       'channel': 'Buildrightacademy',
                       'author': 'Buildrightacademy',
                       'text': 'So a 5G upgrade is also a structural job. Someone has to check the steel '
                               'before the new panel goes up, and sometimes the answer is reinforce the '
                               'pole first.',
                       'tip': 'So a 5G upgrade is also a structural job. Someone has to check the steel '
                              'before the new panel goes up, and sometimes the answer is reinforce the '
                              'pole first.',
                       'timestamp': 943,
                       'timestamp_seconds': 943,
                       'timestamp_label': '[00:15:43]',
                       'url': 'https://www.youtube.com/watch?v=kHmq6jr22Ms&t=943s',
                       'markdown': '[00:15:43](https://www.youtube.com/watch?v=kHmq6jr22Ms&t=943s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'}]}
