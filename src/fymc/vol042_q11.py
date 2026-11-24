from __future__ import annotations

CHAPTER_11 = {'id': 'Q11',
 'chapter_id': 'Q11',
 'chapter_number': 11,
 'question_number': 11,
 'slug': 'ios-truck-parking-yard-build-and-operations',
 'question_prompt': 'How do I develop and operate an IOS or truck parking yard, and what does it actually '
                    'cost to make it work?',
 'kicker': 'Q11 / THE BIG MONEY PLAYBOOKS',
 'title': 'Building and Running IOS and Truck Parking Yards',
 'subtitle': 'Raw land to IOS in San Antonio, actual truck parking development costs, zoning hurdles, flex '
             'vs. IOS, contractor yards (Longyards), managed truck parking challenges, gate and access '
             'control systems, and Rig Hut yard-management lessons',
 'layout_template': 'chapter_opener',
 'reading_time_minutes': 15,
 'executive_summary': 'Operators building IOS and truck parking yards agree on a land-first, low-coverage '
                      'thesis: zoning that allows outdoor storage by right, sites under roughly 20-30% '
                      'building coverage, infill highway access, and a city that will actually sign off. '
                      'Ron Rohde pushed DFW stall rents from $100 to $215-225 on a 5.5-acre yard, and '
                      'models one acre at about 40 spaces at $175 per month. Build costs run $16 per '
                      'linear foot for chain link, about $30K for a cantilever gate, and $1,000 per light '
                      'pole, with self-management via Easy Storage, PDK text-to-gate, or Rig Hut app '
                      'access tied to payment. Practitioners split on pavement versus gravel, single '
                      'versus multi-tenant, padlocks versus automation, and daily versus monthly parkers, '
                      'while Truck Parking Club runs a 70/30 marketplace split for hosts monetizing spare '
                      'spaces.',
 'key_metrics': [{'label': 'Truck Stall Rent Lift',
                  'metric': 'Truck Stall Rent Lift',
                  'value': '$100 to $215-225 per stall per month',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Rohde's pro forma assumed a 50% bump to $150 per 75 ft x 12 ft stall on a "
                             '5.5-acre graveled yard; actual rents reached $215-225, but higher insurance '
                             'kept net income flat.',
                  'source': 'Ronald Rohde Law ([gcg4K6xqYaU @ 00:04:24])'},
                 {'label': 'One-Acre Truck Parking Gross and NOI',
                  'metric': 'One-Acre Truck Parking Gross and NOI',
                  'value': 'About 40 spaces x $175/mo = $7,000/mo gross; about $57K NOI',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Unit math run on the Tyler Cauble show with occupancy in the mid-to-upper '
                             '90s, after taxes, insurance, management, utilities, and software; the hosts '
                             'labeled it a 19% cap with no capex.',
                  'source': 'Tyler Cauble ([q7HQGiIiT_8 @ 00:19:30])'},
                 {'label': 'Marketplace Host Revenue Split',
                  'metric': 'Marketplace Host Revenue Split',
                  'value': '70/30 owner/platform starting rate',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Evan Shelley's Truck Parking Club split covers marketing, notifications, "
                             'payment processing, 24/7/365 support, and payouts, with lower rates for '
                             'operators running 5-10 lots.',
                  'source': 'REtipster ([Ombo8TjihMk @ 00:12:41])'},
                 {'label': 'Automatic Cantilever Gate Cost',
                  'metric': 'Automatic Cantilever Gate Cost',
                  'value': 'About $30K installed for a 30 ft cantilever; operator about $5K',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Rohde recommends an automatic gate even on Class B yards because manual '
                             'gates get left open; the cantilever needs a 30-40% counterbalance, so the '
                             'gate runs about 70 ft long.',
                  'source': 'Ronald Rohde Law ([rPXHwXgqWs8 @ 00:06:59])'}],
 'sections': [{'heading': '1. The Practitioner Consensus',
               'paragraphs': ['Every operator in this lane starts from the same rule Ron Rohde repeats: '
                              'land first, buildings second. Rohde frames IOS as low-coverage yards for '
                              'trucks, trailers, and equipment, with no roofs or major plumbing to fail '
                              'and no $50K air-conditioning surprises [-g_D6hbOPNE @ 00:00:16]. Rohde '
                              'tightens the definition to 20% or less site coverage by improvements, with '
                              'zoning that allows outdoor storage by right, and warns that flood zones and '
                              'geotech problems shrink what you can actually use [q7HQGiIiT_8 @ 00:02:49]. '
                              'Benji Miller of Negresco Property Group lands in the same place from the '
                              'SoCal institutional side: the ideal sites run 30% coverage or less with '
                              'by-right zoning, and once a site crosses that line rent tips to a '
                              'per-building basis, so 32.5% coverage with demolishable sheds is a '
                              'different game [7qT_5Pw0cTo @ 00:28:35]. When a Chicago residential '
                              'investor tried to define IOS by acreage and infill location, Rohde pushed '
                              'back, arguing size and infill do not belong in the definition and it falls '
                              'apart once building coverage passes 20-30% [tonuCLfZrYE @ 00:02:19]. The '
                              'operator takeaway: underwrite the dirt and the zoning entitlement first, '
                              'treat any building as a leasing accelerator, and walk from sites where '
                              'coverage pushes you into a different asset class.',
                              'The demand side is the one point nobody argues. Rohde pegs the gap at '
                              'roughly 3 million tractor-trailers chasing about 300,000 paid commercial '
                              'spaces while city regulation keeps eliminating truck parking, and says a '
                              'single site can earn $10-30K per month [rPXHwXgqWs8 @ 00:00:37]. On '
                              "Jonathan Hayek's show Rohde flagged the truck count as possibly misquoted "
                              'but held the thesis: San Antonio fines trucks parked more than two '
                              'consecutive days, one fine equals a month of parking, and the trucks being '
                              'protected cost $75-100K apiece [mPrS0VognEo @ 00:29:24]. The binding '
                              'constraint is entitled land, not tenants. The Truck N’ Hustle operator '
                              'calls finding land zoned for truck parking the toughest part of the '
                              'business and picked industrial zoning ringed by trash and '
                              "window-manufacturing neighbors who won't complain [uZVNo7EIaXA @ 00:00:03]. "
                              'Rohde hit the same wall on a 5.5-acre yard: the city was the number-one '
                              'issue across zoning, setbacks, fire lanes, sprinklers, sewer, and '
                              'utilities, and 50-75+ tours from national and credit groups produced no '
                              "lease without the city's green light [gcg4K6xqYaU @ 00:05:42]. The "
                              'consensus rule: confirm the jurisdiction is friendly before going under '
                              'contract, never after, because Rohde was still on regulatory work 24 months '
                              'after closing.',
                              'The baseline physical product is also settled: a secured, lit, fenced yard. '
                              "Rohde's Class B standard is gravel, full fencing, a gate, and lighting with "
                              'no frills, and the case for it is recession resilience, since $400 '
                              'paved-lot parkers trade down in a downturn [tonuCLfZrYE @ 00:19:05]. The '
                              "Massachusetts Truck N’ Hustle operator's build list ran new pavement, "
                              'striping with assigned numbered spots, about 33 perimeter light poles they '
                              'called a huge expense, and CCTV with posted signs that is actually '
                              'monitored [uZVNo7EIaXA @ 00:01:43]. Management is the other baseline. Rohde '
                              'says IOS rents will not justify paying a third-party manager a few hundred '
                              'to $1,000 a month, so owners self-manage, while multi-tenant flex can carry '
                              'a property manager [-g_D6hbOPNE @ 00:04:39]. The Rig Hut founders, who '
                              'handled roughly 1,000 vehicles a month around a South Florida port city, '
                              'add that monthly tenants paying $250-400 are the business: daily parking '
                              'pays more but carries the highest management intensity and the most gate '
                              "and damage incidents, so learn monthly tenants' names, equipment, and "
                              'anniversary billing dates [ulBXkeE5I_8 @ 00:03:11]. Those four pillars, '
                              'entitled dirt, perimeter security, self-management, and a monthly core, are '
                              'the floor every speaker builds on.'],
               'table': {'caption': 'Where IOS and truck parking operators line up on the fundamentals',
                         'headers': ['Consensus Point',
                                     'What Practitioners Do',
                                     'Why It Matters',
                                     'Expert Source'],
                         'rows': [['Low site coverage with by-right outdoor storage zoning',
                                   'Keep improvements at or under 20% site coverage with outdoor storage '
                                   'allowed by right',
                                   'Flood zones and geotech problems quietly cut the buildable and usable '
                                   'square footage',
                                   'Tyler Cauble ([q7HQGiIiT_8 @ 00:02:49])'],
                                  ['Hard coverage ceiling that institutional IOS buyers respect',
                                   'Buy sites at 30% coverage or less with by-right zoning in place',
                                   'Above that line rent tips to a per-building basis and changes the game',
                                   'Adding Value w/ Shy Assar | CRE & Industrial ([7qT_5Pw0cTo @ '
                                   '00:28:35])'],
                                  ['City approval cleared before signing the purchase contract',
                                   'Clear zoning, setbacks, fire lanes, sprinklers, sewer, and utility '
                                   'questions with the jurisdiction',
                                   "Rohde drew 50-75+ tours yet signed no lease without the city's green "
                                   'light',
                                   'Ronald Rohde Law ([gcg4K6xqYaU @ 00:05:42])'],
                                  ['Structural truck parking shortage drives the demand thesis',
                                   'Underwrite against roughly 3 million tractor-trailers versus 300,000 '
                                   'paid commercial spaces',
                                   'City regulation keeps eliminating truck parking, and one site can earn '
                                   '$10-30K monthly',
                                   'Ronald Rohde Law ([rPXHwXgqWs8 @ 00:00:37])'],
                                  ['Industrial neighbors who will never complain about trucks',
                                   'Pick industrial zoning next to trash haulers and window manufacturers',
                                   'Finding land zoned for truck parking is the toughest thing in the '
                                   'business',
                                   'Truck N’ Hustle ([uZVNo7EIaXA @ 00:00:03])'],
                                  ['Monthly tenants form the stable core of the yard',
                                   'Build around monthly tenants paying $250-400 and track their '
                                   'anniversary billing dates',
                                   'Daily parkers pay more but bring the most gate and damage incidents',
                                   'Truck Parking Media ([ulBXkeE5I_8 @ 00:02:56])'],
                                  ['Self-management is the norm for yard owners',
                                   'Owners run IOS and truck parking themselves rather than hire a '
                                   'third-party manager',
                                   'Yard rents will not justify a few hundred to $1,000 monthly for '
                                   'management',
                                   'Ronald Rohde Law ([-g_D6hbOPNE @ 00:04:39])']]}},
              {'heading': '2. Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['Sourcing starts off-market because brokers ignore the deal size. Rohde says '
                              'DFW infill runs $300-500K an acre, too small for brokers to give the time '
                              'of day, so the team built a list of 200-300 sites from Google Maps and '
                              'PropStream, scored each on highway proximity, lot shape, slope, zoning, and '
                              'owner or use, then hit the top 30-50 with texts, calls, flyers, and emails; '
                              "host Tyler Cauble's own cadence is 600 properties a quarter, 10 a day, "
                              'where a 1% response is good [q7HQGiIiT_8 @ 00:05:05]. The unit math is a '
                              '75-foot by 11-13-foot stall, about 900 square feet, which works out to '
                              '20-25 spaces per acre at roughly 50% coverage [tonuCLfZrYE @ 00:31:22]. On '
                              'the Cauble show the model ran about 40 spaces per acre at $175 a month for '
                              '$7,000 gross, then taxes near $6K, insurance $2K, management $12K, '
                              'utilities $6K, and software $1K, leaving about $57K of NOI the hosts '
                              'labeled a 19% cap with no capex [q7HQGiIiT_8 @ 00:22:20]. To set the rent, '
                              'Rohde tells operators to pull the Google Maps median, underwrite at or '
                              'slightly below it, and validate with a $30-50 Facebook ad before committing '
                              '[mPrS0VognEo @ 00:50:21].',
                              "Rohde's line-item truck parking budget is the closest thing to a price "
                              'sheet in this niche. Land at $50-100K an acre can cash flow while $1M an '
                              "acre likely won't; clearing runs $1-4K an acre plus dumpsters, grading "
                              'about $5K an acre in infill DFW off a topographic survey pulled during '
                              'diligence, and gravel is the single most expensive item [rPXHwXgqWs8 @ '
                              '00:01:28]. Fencing is $16 per linear foot for 6-foot chain link with top '
                              'and bottom rails and three strands of barbed wire, measured off Google Maps '
                              'or a boundary or ALTA survey, and the price doubles for R panel where a '
                              'city bans chain link and demands opaque fencing [rPXHwXgqWs8 @ 00:05:27]. '
                              'Rohde specs an automatic gate even at Class B because manual gates get left '
                              'open: about $5K for a LiftMaster operator, about $30K installed for a '
                              '30-foot cantilever, and since a cantilever needs a 30-40% counterbalance '
                              'the gate runs roughly 70 feet long, while rolling gates need concrete or '
                              'asphalt because rocks derail them [rPXHwXgqWs8 @ 00:06:59]. Chris Long of '
                              'Longyards, building modular fencing that slides into concrete, reported '
                              'Florida fence quotes at $55 a foot and 3-8 acre build-outs at $300-800K '
                              '[7n_O1KWl4EQ @ 00:35:36].',
                              'The operating stack is software plus remote access. Chris Long runs QR '
                              'onboarding, Easy Storage Solutions with PDK text-to-gate, grid-labeled '
                              'piles like B7, and view-only main-camera access for tenants with no audio '
                              'and a posted disclosure, a setup Rohde said he plans to adopt [7n_O1KWl4EQ '
                              '@ 00:24:21]. Jose of Rig Hut lays out the access ladder: padlock and chain '
                              'needs on-site staff, a keypad gate operator assigns and expires codes per '
                              'tenant or reservation as a strong middle ground, LPR logs in and out '
                              'timestamps for high-value yards but demands connectivity, quality cameras, '
                              'and subscriptions, and a mobile-app link opens the gate with no hardware '
                              '[GOXjR9kZ3BA @ 00:01:54]. One Rig Hut client went from Zelle, Venmo, '
                              'checks, cash, and inventory on a sheet of printer paper to phone-opened '
                              'gates with timestamps, and locks out past-due tenants on the 10th, which '
                              'generates calls [hjC6tiI5Kd4 @ 00:00:48]. Rohde sizes the labor: a minimum '
                              'viable yard is about 4 acres grossing $7-8K a month, run by an offshore VA '
                              'under $2K a month, and the VA tipping point sits at $8-10K gross, after '
                              'which one VA lets you triple in size [tonuCLfZrYE @ 00:27:03].'],
               'table': {'caption': 'Street-level build costs, layout specs, and platform economics',
                         'headers': ['Line Item', 'Number or Spec', 'Operator Note', 'Expert Source'],
                         'rows': [['Truck stall footprint and per-acre density',
                                   '75 ft by 11-13 ft stalls, about 900 sq ft each',
                                   'Yields 20-25 spaces per acre at roughly 50% coverage',
                                   'Ronald Rohde Law ([tonuCLfZrYE @ 00:31:22])'],
                                  ['Chain-link perimeter fencing with barbed wire',
                                   '$16 per linear foot for 6 ft chain link with rails',
                                   'Double the price for R panel where cities ban chain link',
                                   'Ronald Rohde Law ([rPXHwXgqWs8 @ 00:05:27])'],
                                  ['Automatic cantilever gate with LiftMaster operator',
                                   'About $30K installed for 30 ft; operator alone about $5K',
                                   'Cantilever needs 30-40% counterbalance, so the gate runs about 70 ft',
                                   'Ronald Rohde Law ([rPXHwXgqWs8 @ 00:06:59])'],
                                  ['Perimeter lighting on trenched electric service',
                                   '$1,000 per pole, with 16-20 poles covering 4 acres',
                                   'Add $20-30K for crews, permits, and utility tap fees',
                                   'Ronald Rohde Law ([rPXHwXgqWs8 @ 00:10:01])'],
                                  ['Solar SIM security cameras instead of Wi-Fi',
                                   'A $10-20 SIM covers 2 GB for about six months',
                                   'Cheapest item; deters opportunistic thieves and builds an insurance '
                                   'record',
                                   'Ronald Rohde Law ([rPXHwXgqWs8 @ 00:11:30])'],
                                  ['Truck Parking Club marketplace listing split',
                                   '70/30 owner to platform starting rate across the US',
                                   'Covers marketing, payments, and 24/7 support; lower rates at 5-10 lots',
                                   'REtipster ([Ombo8TjihMk @ 00:12:41])'],
                                  ['Longyards Ottawa contractor mini-yard site',
                                   '67 month-to-month yards of roughly 6-9K sq ft each',
                                   'Bought $470K plus $710K build, appraised $3.6M at two-thirds leased',
                                   'Garret Wong Podcast ([RPNJmiZNQdY @ 00:12:42])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Small Edges Yard Operators Actually Use',
                           'body': 'Four moves practitioners use to squeeze more revenue and fewer '
                                   'headaches out of the same dirt.',
                           'items': ['Answer first or lose the truck: inbound callers are dialing three '
                                     'yards at once, and a 20-minute callback lost bookings, so get the '
                                     'caller into the system immediately [Truck Parking Media — '
                                     'ulBXkeE5I_8 @ 00:02:30]',
                                     'Mark up vendor services on Class A yards: Rohde charges $225 for '
                                     'wash services the vendor prices at $200, alongside showers and a '
                                     '24-hour golf-cart patrol at about $5K a month [Ronald Rohde Law — '
                                     'tonuCLfZrYE @ 00:14:14]',
                                     'Skip commercial Wi-Fi: carriers see the address and quote a $150 '
                                     'monthly commercial minimum while SIM cards run about $10 each, and '
                                     'never mix the two technologies across one site [Ronald Rohde Law — '
                                     'tonuCLfZrYE @ 00:21:27]',
                                     'Work the underutilized-yard play: spot candidates on Google Earth, '
                                     'count dock trailers as a utilization proxy, have the tenant give '
                                     'back 1.5 acres to save $3,000 a month, and re-lease at $6,000 NNN to '
                                     'turn a 6.25 cap into an 8 [Jonathan Hayek — mPrS0VognEo @ '
                                     '00:22:53]']},
               'sop_steps': [{'step': 1,
                              'title': 'Build and Score the Off-Market List',
                              'action': 'Pull 200-300 candidate sites and rank them before any outreach.',
                              'detail': 'Use Google Maps and PropStream to build the list, score each site '
                                        'on highway proximity, lot shape, slope, zoning, and owner or use, '
                                        'then hit the top 30-50 with texts, calls, flyers, and emails '
                                        '[Tyler Cauble — q7HQGiIiT_8 @ 00:05:41]'},
                             {'step': 2,
                              'title': 'Test Demand and Price Before Closing',
                              'action': 'Run coming-soon ads and float daily, weekly, and monthly rates.',
                              'detail': 'Rohde runs coming-soon ads to test demand at $30 a night, $100 a '
                                        'week, or $300 a month, and pushes daily parking through Facebook, '
                                        'trucker apps and forums, and signage [Ronald Rohde Law — '
                                        'tonuCLfZrYE @ 00:26:18]'},
                             {'step': 3,
                              'title': 'Clear the City and the Dirt in Diligence',
                              'action': 'Confirm zoning, approvals, and environmental condition before '
                                        'going hard.',
                              'detail': 'Tyler Cauble says always get a Phase I even in cash deals after a '
                                        "tenant swapped clean fill for debris on Rohde's site, and Benji "
                                        'Miller brought in a land-use attorney before contract because of '
                                        'zoning landmines [Tyler Cauble — q7HQGiIiT_8 @ 00:14:06] [Adding '
                                        'Value w/ Shy Assar | CRE & Industrial — 7qT_5Pw0cTo @ 00:08:56]'},
                             {'step': 4,
                              'title': 'Tie Gate Access to Payment',
                              'action': 'Install code- or app-based access that shuts off when rent is '
                                        'late.',
                              'detail': "Rig Hut's rule is that if someone owes they should not be able to "
                                        'get in, because leaked codes mean 50 trucks parked when you think '
                                        "40 are paying and 3 haven't paid in 2 months [Truck Parking Media "
                                        '— ulBXkeE5I_8 @ 00:02:13]'}]},
              {'section_number': 3,
               'title': 'Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The first fight is over what an IOS site even is, and the definition '
                              'dictates what you buy. Ron Rohde, sitting with Tyler Cauble, draws the line '
                              'at 20% or less site coverage by improvements, with outdoor storage allowed '
                              'by right [q7HQGiIiT_8 @ 00:02:49]. Benji Miller of Negresco Property Group '
                              'runs a looser box: 30% coverage or less with by-right zoning is ideal, and '
                              'past that the rent tips toward a per-building basis, with 32.5% coverage '
                              'and demolishable sheds being a different game [7qT_5Pw0cTo @ 00:28:35]. '
                              'When a Chicago residential investor pitched IOS as 3 to 10 acre urban '
                              'parcels near highways with outdoor-storage zoning, Ron pushed back, saying '
                              "size and infill don't belong in the definition and that it falls apart "
                              'above 20 to 30% building coverage [tonuCLfZrYE @ 00:02:19]. The sharper '
                              'split is building versus bare dirt. Ron told Jonathan Hayek flatly that a '
                              'pure yard is off the menu in 2024, because a site without a building gets '
                              'fewer accessory uses by right [mPrS0VognEo @ 00:08:57]. Benji lands in the '
                              'same place from the leasing side: bare paved yards only make sense for '
                              'drayage or trucking near the port, and sites with buildings lease better. '
                              'The pure-yard operator lives or dies on port-adjacent drayage demand.',
                              'Surface and gate spend split the operators into two camps. The Truck N’ '
                              'Hustle operator, running roughly 100 spots in Massachusetts at about $500 '
                              'per spot per month, puts pavement at the top of the build list: number one '
                              'is you want pavement, not crush gravel, followed by striping, numbered '
                              'spots, around 33 perimeter light poles and CCTV that is actually monitored '
                              '[uZVNo7EIaXA @ 00:01:43]. Ron Rohde runs the opposite playbook in DFW. '
                              "Ron's pick is Class B: gravel, full fencing, a gate and lighting with no "
                              'frills, which Ron calls recession-resilient because $400 paved-lot parkers '
                              'trade down when the market tightens [tonuCLfZrYE @ 00:19:05]. On gates, Ron '
                              'still tells builders to install an automatic gate even at Class B, because '
                              'manual gates get left open, and prices a 30 ft cantilever gate with install '
                              'at about $30K [rPXHwXgqWs8 @ 00:06:59]. Jose at Rig Hut takes the staged '
                              'route: test the market under a lease with manual gates before investing in '
                              'automation, then move to an automatic system once you want 24/7 access, '
                              'multiple tenants and expansion beyond one location [Fc82YDH9IrI @ '
                              '00:06:10]. Jose concedes that five-acre gravel lots in tight markets get '
                              'away with padlocks purely because demand is high.',
                              'Tenant concentration and rental term are the third fault line. Ron Rohde '
                              'argues single tenant is a benefit: underwrite heavily and bet once, because '
                              'in a building of 20 to 30 flex tenants at least 5 are financially shaky '
                              '[-g_D6hbOPNE @ 00:02:17]. Ron frames the choice as a temperament call: with '
                              'sweat equity, choose multi-tenant; if time-constrained, choose single '
                              'tenant. The Truck N’ Hustle operator leans on the opposite logic and treats '
                              "many tenants as a shield: with 50 tenants, losing 2 doesn't hurt, though "
                              'they concede a single tenant is simpler to run and eventually leased the '
                              "first lot to one tenant [uZVNo7EIaXA @ 00:04:16]. On term, Ron's math "
                              'favors transient parking: $30 a night is about $900 a month per space '
                              'against $225 to $300 from a monthly tenant, and even at 80% occupancy a '
                              'daily space yields about $630, but it demands heavy marketing through '
                              'Facebook, trucker apps, forums and signage [tonuCLfZrYE @ 00:10:32]. Rig '
                              'Hut, having handled about 1,000 vehicles a month at peak around a South '
                              'Florida port city, lands on the other side: daily and transient pays more '
                              'but brings the highest management intensity and more gate and damage '
                              'incidents, so monthly tenants paying $250 to $400 are the business '
                              '[ulBXkeE5I_8 @ 00:02:56].'],
               'table': {'caption': 'Side-by-side playbooks where IOS and truck parking operators split',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Maximum site coverage that still counts as IOS',
                                   'Ron Rohde: 20% or less coverage by improvements, with outdoor storage '
                                   'allowed by right',
                                   'Benji Miller: 30% or less with by-right zoning; 32.5% with '
                                   'demolishable sheds is a different game',
                                   'Tyler Cauble ([q7HQGiIiT_8 @ 00:02:49]); Adding Value w/ Shy Assar | '
                                   'CRE & Industrial ([7qT_5Pw0cTo @ 00:28:35])'],
                                  ['Building on site versus a pure yard',
                                   'Ron Rohde will not buy pure yard in 2024 because fewer accessory uses '
                                   'are allowed by right',
                                   'Benji Miller buys bare paved yards only for drayage or trucking near '
                                   'the port; buildings lease better',
                                   'Jonathan Hayek ([mPrS0VognEo @ 00:08:57]); Adding Value w/ Shy Assar | '
                                   'CRE & Industrial ([7qT_5Pw0cTo @ 00:29:49])'],
                                  ['Yard surface for a truck parking build',
                                   'Truck N’ Hustle: pavement not crush gravel, plus striping, numbered '
                                   'spots and about 33 light poles',
                                   'Ron Rohde: Class B gravel, fencing, gate and lighting with no frills, '
                                   'resilient when paved parkers trade down',
                                   'Truck N’ Hustle ([uZVNo7EIaXA @ 00:01:43]); Ronald Rohde Law '
                                   '([tonuCLfZrYE @ 00:19:05])'],
                                  ['When to spend on an automatic gate',
                                   'Ron Rohde: automatic gate even at Class B because manual gates get '
                                   'left open; about $30K installed',
                                   'Jose at Rig Hut: test the market under a lease with manual gates, '
                                   'automate when scaling to 24/7',
                                   'Ronald Rohde Law ([rPXHwXgqWs8 @ 00:06:59]); Truck Parking Media '
                                   '([Fc82YDH9IrI @ 00:06:10])'],
                                  ['One tenant versus many tenants on the lot',
                                   'Ron Rohde: single tenant is a benefit, so underwrite heavily and bet '
                                   'once',
                                   "Truck N’ Hustle: 50 tenants act as a shield, so losing 2 doesn't hurt "
                                   'the lot',
                                   'Ronald Rohde Law ([-g_D6hbOPNE @ 00:02:17]); Truck N’ Hustle '
                                   '([uZVNo7EIaXA @ 00:04:16])'],
                                  ['Daily transient parking versus monthly tenants',
                                   'Ron Rohde: $30 per night is about $900 per month per space, still '
                                   'about $630 at 80% occupancy',
                                   'Rig Hut: monthly tenants at $250 to $400 are the business; daily '
                                   'brings the most gate and damage incidents',
                                   'Ronald Rohde Law ([tonuCLfZrYE @ 00:10:32]); Truck Parking Media '
                                   '([ulBXkeE5I_8 @ 00:02:56])'],
                                  ['Target acreage for an acquisition or build',
                                   'Benji Miller: 1 to 2 acres lease fastest; avoids vacant 7 to 10+ acre '
                                   'white whales',
                                   'Ron Rohde buys infill DFW over 4 acres; Chris Long screens for 3+ '
                                   'acres in towns over 50k population',
                                   'Adding Value w/ Shy Assar | CRE & Industrial ([7qT_5Pw0cTo @ '
                                   '00:05:49]); Jonathan Hayek ([mPrS0VognEo @ 00:06:44]); Garret Wong '
                                   'Podcast ([RPNJmiZNQdY @ 00:36:06])']]}},
              {'section_number': 4,
               'title': 'Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The city kills more IOS deals than the market does. Ron Rohde, reviewing a '
                              '5.5-acre graveled truck-parking site 24 months after closing, names the '
                              'city the number one issue: zoning, setbacks, fire lanes, sprinklers, sewer '
                              'and utility questions, with the fix being confirmation that the '
                              'jurisdiction is friendly before going under contract [gcg4K6xqYaU @ '
                              '00:05:42]. The site drew 50 to 75-plus tours, including national and credit '
                              "groups, and still could not sign a lease without the city's green light. "
                              "Ron's next steps there are regulatory work and landing a compatible use. "
                              'Benji Miller avoids that trap by front-loading the work, running heavy '
                              'diligence before contract on the Fontana deal, including land-use attorney '
                              'Alan Mackins, because of zoning landmines [7qT_5Pw0cTo @ 00:08:56]. Chris '
                              'Long of Longyards paid for the same lesson in a different currency: 12 '
                              'easements on one site caused a 2-year loss and raised costs by a third '
                              '[RPNJmiZNQdY @ 00:39:23]. Chris also flags that some Texas cities limit '
                              'unbuilt sites to 5 years and that in DFW a structure was required for full '
                              'occupancy; the DFW location fell through, and Tier 1 land with existing '
                              'heavy-industrial use is where Longyards now concentrates [7n_O1KWl4EQ @ '
                              '00:04:15].',
                              'Thin NOI plus the wrong debt is the second killer. On that same site, rents '
                              'climbed from $100 per stall to $215 to $225 against a pro forma of $150, '
                              'yet insurance rose several thousand dollars and net income stayed flat '
                              '[gcg4K6xqYaU @ 00:04:45]. A 5-year fixed note at about 5.5% saved their '
                              'bacon; Ron says variable debt plus a thin NOI would have meant pain, and '
                              'calls the lender a very powerful ally but a heavy sword. Benji Miller flags '
                              'the same exposure at portfolio scale: 2022 and 2023 vintage portfolios on '
                              '3-year loans face liquidity events, so expect recaps and new debt '
                              'facilities [7qT_5Pw0cTo @ 00:35:08]. Evan Shelley of Truck Parking Club '
                              'says a lot of underwriting in the last couple of years just made no sense, '
                              'and that the lots that failed were too far out or over-leased; buying '
                              'property in the middle of Kentucky or Tennessee, not close to anything, on '
                              'the assumption you will fill it is not a wise decision [Ombo8TjihMk @ '
                              "00:29:46]. Expense lines are stickier than first-timers expect: AT&T's "
                              'commercial minimum is $250 a month and an electric hookup alone runs $100 a '
                              "month, because, as Ron puts it, you can't do anything cheaply in commercial "
                              '[q7HQGiIiT_8 @ 00:29:31].',
                              'The daily grind leaks money through access, collections and tenants who '
                              "abuse the yard. Rig Hut's founders, who managed a multi-yard portfolio "
                              'around a South Florida port city, warn that your gate code is not a gate: '
                              'codes get shared with cousins, dispatchers and buddies until you think 40 '
                              "trucks are paying while 50 are parked and 3 haven't paid in 2 months, and "
                              'the fix is tying access control to payment [ulBXkeE5I_8 @ 00:01:59]. One '
                              'Rig Hut operator came off Zelle, Venmo, checks, cash and a single sheet of '
                              'printer paper; now drivers open the gate from their phones and past-due '
                              'tenants get locked out on the 10th, which generates calls [hjC6tiI5Kd4 @ '
                              "00:00:48]. Chris Long's early equity-for-management deal failed and the "
                              'managers were fired; Chris now insists on a strong lease, because abandoned '
                              'cars can take 3 to 6 months to remove, and on separation of duties so '
                              "people can't get crooked [RPNJmiZNQdY @ 00:42:02]. Ron Rohde had a tenant "
                              'swap clean fill for debris, brought in Terracon, and now watches for truck '
                              'oil changes with boots on the ground, cameras and a check of all four '
                              "corners [q7HQGiIiT_8 @ 00:12:03]. Tyler Cauble's add-on: always get a Phase "
                              'I, even in cash deals.'],
               'table': {'caption': 'Firsthand losses, leaks and the economics check each operator now '
                                    'runs',
                         'headers': ['Failure Mode',
                                     'What Went Wrong',
                                     'Economics Check Or Fix',
                                     'Expert Source'],
                         'rows': [['City blocks the lease on a demanded site',
                                   '50 to 75+ tours including national and credit groups, but no lease '
                                   "without the city's green light",
                                   'Confirm the jurisdiction is friendly on zoning, setbacks, fire lanes, '
                                   'sprinklers and sewer before contract',
                                   'Ronald Rohde Law ([gcg4K6xqYaU @ 00:06:51])'],
                                  ['Insurance swallows the rent increase',
                                   'Stall rents rose from $100 to $215 to $225 against a $150 pro forma',
                                   'Insurance rose several thousand dollars and net income stayed flat; '
                                   'fixed 5-year debt at about 5.5% saved the deal',
                                   'Ronald Rohde Law ([gcg4K6xqYaU @ 00:04:45])'],
                                  ['Easements buried in the site',
                                   'Twelve easements on one Longyards site caused a 2-year loss',
                                   'Costs rose by a third; Longyards now focuses on Tier 1 ready-to-go '
                                   'land only',
                                   'Garret Wong Podcast ([RPNJmiZNQdY @ 00:39:23])'],
                                  ['Overpaying for land relative to parking rent',
                                   "At $1M per acre a truck parking site likely won't cash flow",
                                   'Land at $50,000 to $100,000 per acre is viable; higher land price must '
                                   'be supported by higher rent',
                                   'Ronald Rohde Law ([rPXHwXgqWs8 @ 00:01:28])'],
                                  ['Remote or over-leased lots that never fill',
                                   'Failed lots on the platform were too far out or over-leased',
                                   "Don't buy in the middle of Kentucky or Tennessee assuming it fills; "
                                   'bookings track interstate distance',
                                   'REtipster ([Ombo8TjihMk @ 00:29:46])'],
                                  ['Gate code leakage and silent non-payers',
                                   "Operator thinks 40 trucks pay while 50 park and 3 haven't paid in 2 "
                                   'months',
                                   'Tie access control to payment so anyone who owes cannot get in',
                                   'Truck Parking Media ([ulBXkeE5I_8 @ 00:01:59])'],
                                  ['Tenant contaminates or degrades the yard',
                                   'A tenant swapped clean fill for debris and Ron had to engage Terracon',
                                   'Boots on the ground, cameras, all four corners checked, and a Phase I '
                                   'even in cash deals',
                                   'Tyler Cauble ([q7HQGiIiT_8 @ 00:12:03])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Four Kill Checks Before You Wire Money',
                           'body': 'Each check below comes from an operator who paid for the lesson in '
                                   'lost tours, lost years, or leaked rent.',
                           'items': ["Confirm the city is friendly before going under contract; Ron's "
                                     '5.5-acre site drew 50 to 75+ tours and still could not lease without '
                                     "the city's green light [Ronald Rohde Law — gcg4K6xqYaU @ 00:06:51].",
                                     'Learn the certificate-of-occupancy process before buying, the one '
                                     'step Ron says they wish they had mastered first [Tyler Cauble — '
                                     'q7HQGiIiT_8 @ 00:32:22].',
                                     'Pull every easement before closing; Chris Long lost 2 years and saw '
                                     'costs rise by a third on a site carrying 12 easements [Garret Wong '
                                     'Podcast — RPNJmiZNQdY @ 00:39:23].',
                                     'Tie gate access to payment and know average revenue per space net of '
                                     'bad debt, vacancy and late payments [Truck Parking Media — '
                                     'ulBXkeE5I_8 @ 00:02:13].']}}],
 'pull_quote': '“Number two, speaking of leakage, your gate code is not a gate.” — Truck Parking Media '
               '(ulBXkeE5I_8 @ 00:01:44).',
 'diagram_id': 'diag-06',
 'action_checklist': ['Build an off-market list of 200 to 300 sites with Google Maps and PropStream, score '
                      'each on highway proximity, lot shape, slope, zoning and owner/use, then hit the top '
                      '30 to 50 with texts, calls, flyers and emails [Tyler Cauble — q7HQGiIiT_8 @ '
                      '00:05:05].',
                      'Order a topographic survey during due diligence so the site plan can show drainage '
                      'and gravel compaction depth, budgeting about $5K per acre for grading in infill DFW '
                      '[Ronald Rohde Law — rPXHwXgqWs8 @ 00:02:53].',
                      'Run coming-soon ads before opening and float $30 per night, $100 per week, or $300 '
                      'per month to test demand [Ronald Rohde Law — tonuCLfZrYE @ 00:26:18].',
                      'Underwrite rent at or slightly below the Google Maps median for nearby yards, '
                      'validated with a $30 to $50 Facebook ad [Jonathan Hayek — mPrS0VognEo @ 00:50:21].',
                      'Get every inbound caller into the system immediately, because callers ring 3 yards '
                      'at once and a 20-minute callback lost bookings [Truck Parking Media — ulBXkeE5I_8 @ '
                      '00:02:44].',
                      'Install solar SIM cameras at $10 to $20 per SIM for 2 GB over about 6 months '
                      'instead of Wi-Fi, creating a deterrent and an insurance record [Ronald Rohde Law — '
                      'rPXHwXgqWs8 @ 00:11:30].'],
 'statutory_citations': [{'title': 'Ronald Rohde Law — Challenges I Faced On My Industrial Investment IOS '
                                   '[00:05:42]',
                          'url': 'https://www.youtube.com/watch?v=gcg4K6xqYaU&t=342s',
                          'relevance': 'Primary practitioner testimony on the city as the number one '
                                       'obstacle, insurance creep, and fixed debt protecting a thin NOI.'},
                         {'title': 'Garret Wong Podcast — How to Invest in Industrial Outdoor Storage '
                                   '[00:39:23]',
                          'url': 'https://www.youtube.com/watch?v=RPNJmiZNQdY&t=2363s',
                          'relevance': 'Primary practitioner testimony on 12 easements causing a 2-year '
                                       'loss and a one-third cost overrun.'},
                         {'title': 'Truck Parking Media — What I Wish I Knew Before Managing My First '
                                   'Truck Parking Yard [00:01:59]',
                          'url': 'https://www.youtube.com/watch?v=ulBXkeE5I_8&t=119s',
                          'relevance': 'Primary practitioner testimony on gate code leakage, non-payment '
                                       'excuses, and speed to lead.'},
                         {'title': 'REtipster — Truck Yeah! How Evan Shelley Makes Bank on Truck Parking '
                                   'Lots | REtipster 194 [00:29:46]',
                          'url': 'https://www.youtube.com/watch?v=Ombo8TjihMk&t=1786s',
                          'relevance': 'Primary practitioner testimony on failed lots that were too far '
                                       'out or over-leased and broken underwriting.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'gcg4K6xqYaU',
                       'title': 'Challenges I Faced On My Industrial Investment IOS',
                       'channel': 'Ronald Rohde Law',
                       'author': 'Ronald Rohde Law',
                       'text': 'Fixed debt saved our bacon, and the lender is a very powerful ally but a '
                               'heavy sword.',
                       'tip': 'Fixed debt saved our bacon, and the lender is a very powerful ally but a '
                              'heavy sword.',
                       'timestamp': 440,
                       'timestamp_seconds': 440,
                       'timestamp_label': '[00:07:20]',
                       'url': 'https://www.youtube.com/watch?v=gcg4K6xqYaU&t=440s',
                       'markdown': '[00:07:20](https://www.youtube.com/watch?v=gcg4K6xqYaU&t=440s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'gcg4K6xqYaU',
                       'title': 'Challenges I Faced On My Industrial Investment IOS',
                       'channel': 'Ronald Rohde Law',
                       'author': 'Ronald Rohde Law',
                       'text': 'The city is the number one issue, so confirm the jurisdiction is friendly '
                               'before going under contract.',
                       'tip': 'The city is the number one issue, so confirm the jurisdiction is friendly '
                              'before going under contract.',
                       'timestamp': 342,
                       'timestamp_seconds': 342,
                       'timestamp_label': '[00:05:42]',
                       'url': 'https://www.youtube.com/watch?v=gcg4K6xqYaU&t=342s',
                       'markdown': '[00:05:42](https://www.youtube.com/watch?v=gcg4K6xqYaU&t=342s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'aMpeVcjGM3c',
                       'title': 'I Bought 7.5 Acres to Build This IOS Deal',
                       'channel': 'Ronald Rohde Law',
                       'author': 'Ronald Rohde Law',
                       'text': 'And so we are targeting about 5 to 7,000 per acre triple net in terms of '
                               'the rent.',
                       'tip': 'And so we are targeting about 5 to 7,000 per acre triple net in terms of '
                              'the rent.',
                       'timestamp': 344,
                       'timestamp_seconds': 344,
                       'timestamp_label': '[00:05:44]',
                       'url': 'https://www.youtube.com/watch?v=aMpeVcjGM3c&t=344s',
                       'markdown': '[00:05:44](https://www.youtube.com/watch?v=aMpeVcjGM3c&t=344s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '7qT_5Pw0cTo',
                       'title': 'Inside a $4.8M Industrial Outdoor Storage (IOS) Deal in Fontana | Benji '
                                'Miller',
                       'channel': 'Adding Value w/ Shy Assar | CRE & Industrial',
                       'author': 'Adding Value w/ Shy Assar | CRE & Industrial',
                       'text': 'So, generally what we view as like the most ideal IOS sites are 30% '
                               'coverage or less with by right zoning.',
                       'tip': 'So, generally what we view as like the most ideal IOS sites are 30% '
                              'coverage or less with by right zoning.',
                       'timestamp': 1715,
                       'timestamp_seconds': 1715,
                       'timestamp_label': '[00:28:35]',
                       'url': 'https://www.youtube.com/watch?v=7qT_5Pw0cTo&t=1715s',
                       'markdown': '[00:28:35](https://www.youtube.com/watch?v=7qT_5Pw0cTo&t=1715s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'rPXHwXgqWs8',
                       'title': 'Actual Costs of Developing Truck Parking',
                       'channel': 'Ronald Rohde Law',
                       'author': 'Ronald Rohde Law',
                       'text': "At $1M per acre the site likely won't cash flow, while $50,000 to $100,000 "
                               'per acre is viable.',
                       'tip': "At $1M per acre the site likely won't cash flow, while $50,000 to $100,000 "
                              'per acre is viable.',
                       'timestamp': 88,
                       'timestamp_seconds': 88,
                       'timestamp_label': '[00:01:28]',
                       'url': 'https://www.youtube.com/watch?v=rPXHwXgqWs8&t=88s',
                       'markdown': '[00:01:28](https://www.youtube.com/watch?v=rPXHwXgqWs8&t=88s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Ombo8TjihMk',
                       'title': 'Truck Yeah! How Evan Shelley Makes Bank on Truck Parking Lots | REtipster '
                                '194',
                       'channel': 'REtipster',
                       'author': 'REtipster',
                       'text': "I don't think it's a wise decision to go out and buy property that's in "
                               'the middle of Kentucky or Tennessee not close to anything with the '
                               "assumption that you're going to fill it up.",
                       'tip': "I don't think it's a wise decision to go out and buy property that's in the "
                              'middle of Kentucky or Tennessee not close to anything with the assumption '
                              "that you're going to fill it up.",
                       'timestamp': 1929,
                       'timestamp_seconds': 1929,
                       'timestamp_label': '[00:32:09]',
                       'url': 'https://www.youtube.com/watch?v=Ombo8TjihMk&t=1929s',
                       'markdown': '[00:32:09](https://www.youtube.com/watch?v=Ombo8TjihMk&t=1929s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'uZVNo7EIaXA',
                       'title': 'Pros And Cons; Building The “Truck Parking Lot Business!”',
                       'channel': 'Truck N’ Hustle',
                       'author': 'Truck N’ Hustle',
                       'text': "The toughest thing is finding land that's zoned for truck parking.",
                       'tip': "The toughest thing is finding land that's zoned for truck parking.",
                       'timestamp': 3,
                       'timestamp_seconds': 3,
                       'timestamp_label': '[00:00:03]',
                       'url': 'https://www.youtube.com/watch?v=uZVNo7EIaXA&t=3s',
                       'markdown': '[00:00:03](https://www.youtube.com/watch?v=uZVNo7EIaXA&t=3s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'GOXjR9kZ3BA',
                       'title': 'Truck Yard Access Control: 4 Systems That Can Make or Break Your Lot’s '
                                'Success',
                       'channel': 'Truck Parking Media',
                       'author': 'Truck Parking Media',
                       'text': 'Each system has a time and place, but what matters is knowing what your '
                               'yard actually needs today and what will break as you grow.',
                       'tip': 'Each system has a time and place, but what matters is knowing what your '
                              'yard actually needs today and what will break as you grow.',
                       'timestamp': 307,
                       'timestamp_seconds': 307,
                       'timestamp_label': '[00:05:07]',
                       'url': 'https://www.youtube.com/watch?v=GOXjR9kZ3BA&t=307s',
                       'markdown': '[00:05:07](https://www.youtube.com/watch?v=GOXjR9kZ3BA&t=307s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Fc82YDH9IrI',
                       'title': 'Manual vs Automatic Gates: Which Is Best for Your Truck Parking Yard?',
                       'channel': 'Truck Parking Media',
                       'author': 'Truck Parking Media',
                       'text': 'Again, no one wants those calls at night.',
                       'tip': 'Again, no one wants those calls at night.',
                       'timestamp': 252,
                       'timestamp_seconds': 252,
                       'timestamp_label': '[00:04:12]',
                       'url': 'https://www.youtube.com/watch?v=Fc82YDH9IrI&t=252s',
                       'markdown': '[00:04:12](https://www.youtube.com/watch?v=Fc82YDH9IrI&t=252s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'hjC6tiI5Kd4',
                       'title': 'Truck Parking Technology That Fills Yards Faster | Rig Hut',
                       'channel': 'Truck Parking Media',
                       'author': 'Truck Parking Media',
                       'text': 'So, all these drivers can open the gate from their phone.',
                       'tip': 'So, all these drivers can open the gate from their phone.',
                       'timestamp': 48,
                       'timestamp_seconds': 48,
                       'timestamp_label': '[00:00:48]',
                       'url': 'https://www.youtube.com/watch?v=hjC6tiI5Kd4&t=48s',
                       'markdown': '[00:00:48](https://www.youtube.com/watch?v=hjC6tiI5Kd4&t=48s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'q7HQGiIiT_8',
                       'title': 'How to Invest in Industrial Outdoor Storage with Ron Rohde',
                       'channel': 'Tyler Cauble',
                       'author': 'Tyler Cauble',
                       'text': "So that's my answer is why it's kind of expensive because can't do "
                               'anything cheaply in commercial and even IOS qualifies as commercial.',
                       'tip': "So that's my answer is why it's kind of expensive because can't do anything "
                              'cheaply in commercial and even IOS qualifies as commercial.',
                       'timestamp': 1803,
                       'timestamp_seconds': 1803,
                       'timestamp_label': '[00:30:03]',
                       'url': 'https://www.youtube.com/watch?v=q7HQGiIiT_8&t=1803s',
                       'markdown': '[00:30:03](https://www.youtube.com/watch?v=q7HQGiIiT_8&t=1803s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '-g_D6hbOPNE',
                       'title': 'Flex vs Outdoor Storage (IOS) Which industrial investment is better?',
                       'channel': 'Ronald Rohde Law',
                       'author': 'Ronald Rohde Law',
                       'text': 'IOS on the other hand is essentially a covered land play.',
                       'tip': 'IOS on the other hand is essentially a covered land play.',
                       'timestamp': 346,
                       'timestamp_seconds': 346,
                       'timestamp_label': '[00:05:46]',
                       'url': 'https://www.youtube.com/watch?v=-g_D6hbOPNE&t=346s',
                       'markdown': '[00:05:46](https://www.youtube.com/watch?v=-g_D6hbOPNE&t=346s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'RPNJmiZNQdY',
                       'title': 'How to Invest in Industrial Outdoor Storage',
                       'channel': 'Garret Wong Podcast',
                       'author': 'Garret Wong Podcast',
                       'text': "You want to put bridges between that so people can't get crooked or do "
                               'deals.',
                       'tip': "You want to put bridges between that so people can't get crooked or do "
                              'deals.',
                       'timestamp': 2548,
                       'timestamp_seconds': 2548,
                       'timestamp_label': '[00:42:28]',
                       'url': 'https://www.youtube.com/watch?v=RPNJmiZNQdY&t=2548s',
                       'markdown': '[00:42:28](https://www.youtube.com/watch?v=RPNJmiZNQdY&t=2548s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'mPrS0VognEo',
                       'title': 'Net Lease Industrial, IOS, and Truck Parking with Ron Rohde',
                       'channel': 'Jonathan Hayek',
                       'author': 'Jonathan Hayek',
                       'text': 'Pick the median or slightly below the median for underwriting your '
                               "property, and you'll be conservative.",
                       'tip': 'Pick the median or slightly below the median for underwriting your '
                              "property, and you'll be conservative.",
                       'timestamp': 3021,
                       'timestamp_seconds': 3021,
                       'timestamp_label': '[00:50:21]',
                       'url': 'https://www.youtube.com/watch?v=mPrS0VognEo&t=3021s',
                       'markdown': '[00:50:21](https://www.youtube.com/watch?v=mPrS0VognEo&t=3021s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '7n_O1KWl4EQ',
                       'title': 'Massive Profit within IOS Industrial Contractor Yard with Chris Long and '
                                'Longyards',
                       'channel': 'Ronald Rohde Law',
                       'author': 'Ronald Rohde Law',
                       'text': 'You can have one employee manage to three of them.',
                       'tip': 'You can have one employee manage to three of them.',
                       'timestamp': 1096,
                       'timestamp_seconds': 1096,
                       'timestamp_label': '[00:18:16]',
                       'url': 'https://www.youtube.com/watch?v=7n_O1KWl4EQ&t=1096s',
                       'markdown': '[00:18:16](https://www.youtube.com/watch?v=7n_O1KWl4EQ&t=1096s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'tonuCLfZrYE',
                       'title': 'How to Invest Industrial Outdoor Storage (Truck Parking)',
                       'channel': 'Ronald Rohde Law',
                       'author': 'Ronald Rohde Law',
                       'text': 'And so all truck parking I would say is self-managed.',
                       'tip': 'And so all truck parking I would say is self-managed.',
                       'timestamp': 1680,
                       'timestamp_seconds': 1680,
                       'timestamp_label': '[00:28:00]',
                       'url': 'https://www.youtube.com/watch?v=tonuCLfZrYE&t=1680s',
                       'markdown': '[00:28:00](https://www.youtube.com/watch?v=tonuCLfZrYE&t=1680s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ulBXkeE5I_8',
                       'title': 'What I Wish I Knew Before Managing My First Truck Parking Yard',
                       'channel': 'Truck Parking Media',
                       'author': 'Truck Parking Media',
                       'text': "If someone owes, they shouldn't be able to get in.",
                       'tip': "If someone owes, they shouldn't be able to get in.",
                       'timestamp': 133,
                       'timestamp_seconds': 133,
                       'timestamp_label': '[00:02:13]',
                       'url': 'https://www.youtube.com/watch?v=ulBXkeE5I_8&t=133s',
                       'markdown': '[00:02:13](https://www.youtube.com/watch?v=ulBXkeE5I_8&t=133s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'}]}
