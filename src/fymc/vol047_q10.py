from __future__ import annotations

CHAPTER_10 = {'id': 'Q10',
 'chapter_id': 'Q10',
 'chapter_number': 10,
 'question_number': 10,
 'slug': 'bess-sizing-revenue-stacking-greenfield-development',
 'question_prompt': 'How do you size, finance, and develop a BESS project from greenfield site and land '
                    'lease through COD?',
 'kicker': 'Q10 / THE BIG MONEY PLAYBOOKS',
 'title': 'BESS Sizing, Revenue Stacking and Greenfield Development',
 'subtitle': 'Sizing for payback and microgrids, chemistry and revenue stacking, grid-scale battery '
             'economics, the six stages from site to COD, landman and lease considerations, UK land values '
             'per acre, 2 GW operating lessons, scaling a BESS business, logistics, and Poland and EU '
             'capital flows',
 'layout_template': 'expert_commentary',
 'reading_time_minutes': 15,
 'executive_summary': 'Storage operators across the UK, ERCOT, Australia and Poland agree that grid '
                      'distance decides the deal. Harmony Energy only chases sites within about 1 km of '
                      'the connection point, and UK landowner advisers call anything beyond 5 km dead. The '
                      'revenue stack is arbitrage, ancillary services and capacity. In the UK, frequency '
                      'response carries 50 to 60 percent of revenue, and location sets the price spread '
                      'everywhere. The street numbers are concrete: £10,000 to £40,000 per acre per year '
                      'in UK battery rent, densities up to 100 MWh per acre, and ERCOT interconnection of '
                      'around 3 years against up to 7 in CAISO. EMS fees can eat 20 to 30 percent of '
                      'arbitrage revenue. Operators split on merchant versus contracted revenue, crowded '
                      'metro nodes versus overlooked ones, and outright land purchase versus leasing. They '
                      'also disagree on how hard to cycle an asset before degradation erases trading '
                      'gains.',
 'key_metrics': [{'label': 'UK Battery Land Rent Per Acre',
                  'metric': 'UK Battery Land Rent Per Acre',
                  'value': '£10,000 to £40,000 per acre per year, versus £850 to £1,200 per acre for solar',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'UK landowner lease rates for battery storage sites, typically set at 2 to 5 '
                             'percent of gross site revenue',
                  'source': 'Solar Grid Check ([9mZg--94z1I @ 00:00:00])'},
                 {'label': 'Harmony Energy Siting Radius',
                  'metric': 'Harmony Energy Siting Radius',
                  'value': 'Within about 1 km of the point of connection, with cabling costs of up to £10m '
                           'per km',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Harmony's development director says the rule is why every project Harmony "
                             'consented was built',
                  'source': 'Regen ([Zmu3gs7y51A @ 00:34:31])'},
                 {'label': 'Maximum Energy Density Per Acre',
                  'metric': 'Maximum Energy Density Per Acre',
                  'value': 'Up to 100 MWh per acre, with 50 MWh per acre called the lower side',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Acacia Energy's 850 MW / roughly 1.7 GWh project near Sydney uses about 32 "
                             'acres',
                  'source': 'The Land Department Podcast ([bWbMkkvRPWI @ 00:08:20])'},
                 {'label': 'EMS Fee Drag On Arbitrage',
                  'metric': 'EMS Fee Drag On Arbitrage',
                  'value': '20 to 30 percent of arbitrage revenue',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Hidden contract cost flagged alongside SCADA that can cost as much as the '
                             'battery container',
                  'source': 'Jerzy Kuzminski ([fDBjJyTGWDQ @ 00:22:19])'}],
 'sections': [{'heading': 'Section 1: The Practitioner Consensus',
               'paragraphs': ['Every developer who has actually built storage starts from the same place: '
                              'distance to the point of connection decides the deal before anything else '
                              'does. Francis Nicholson of Harmony Energy runs a hard rule of only chasing '
                              'sites within roughly 1 km of the connection point. He says that discipline '
                              'is why every project Harmony consented got built [Zmu3gs7y51A @ 00:34:31]. '
                              "The economics behind the rule are stark: on Harmony's 200 MW, 4-hour, 400 "
                              'kV Burton scheme, cabling runs up to £10m per kilometre against roughly '
                              '£200m of total capex. Solar Grid Check puts it bluntly for UK landowners. A '
                              'substation at 33 kV or above is required; under 1 km is ideal, 1 to 2 miles '
                              'is workable, and beyond 5 km the site is dead. The channel calls grid '
                              'distance effectively the only factor [9mZg--94z1I @ 00:03:12]. Sean Daly of '
                              'Acacia Energy applies the same logic in the US and Australia. Daly prefers '
                              'parcels beside substations with open bays and falls back to a line tap with '
                              'a short gen-tie, because every extra length of gen-tie adds cost and '
                              'failure risk [bWbMkkvRPWI @ 00:18:30]. Ravi Sharma at Deriva adds the '
                              'competitive reality: a good site has usually been looked at by five '
                              'competitors already, so speed on grid screening matters as much as the '
                              'screen itself [LhT4VVDW7CI @ 00:15:45].',
                              'On revenue, the speakers converge on a three-legged stack. STG Nations '
                              'Energy names arbitrage, ancillary services and capacity, and insists the '
                              'value lives in the model rather than the data sheet [AVf_DgVRB3w @ '
                              '00:03:18]. Modo Energy lists the same three streams and describes the daily '
                              "pattern of charging overnight and discharging in the afternoon. In Modo's "
                              'words, location is everything for how batteries make money [AtMNJWhrmXE @ '
                              '00:01:46]. Solar Grid Check gives the UK weighting: frequency response at '
                              '50 to 60 percent of revenue, arbitrage at 20 to 30 percent, and capacity '
                              'market plus other ancillary services filling the rest. On that mix, a 50 MW '
                              'site grosses £4 million to £7.5 million a year [9mZg--94z1I @ 00:01:26]. '
                              'Andy Willis of Kona Energy ties revenue directly to siting, arguing that '
                              'location is key to determining revenues for storage. Kona is pointed at '
                              'Central West Texas and the panhandle, where 2 to 3 pm prices hit zero or '
                              'about $1 per MWh, instead of the metro nodes around Houston, Austin, San '
                              'Antonio and Dallas-Fort Worth where early batteries clustered [UI-9nmVEA9U '
                              "@ 00:05:08]. Sizing follows the revenue target. STG's line is to size the "
                              'power-to-energy ratio for the revenue: 50 MW with 100 MWh runs 2 hours, and '
                              'half the power on the same energy runs 4.',
                              'The third point of agreement is that development is a de-risking business '
                              'and bankability is the finish line. BESS Engineer lays out six stages: '
                              'idea, technical feasibility, risk reduction, bankability, financing and '
                              'construction. The killers are listed plainly: no fire-safety approval, a '
                              'grid connection that is too expensive, or no long-term service plan. Any '
                              'one of them cancels the project [r852ohYdDhc @ 00:01:48]. Ravi Sharma '
                              "frames the developer's whole job as de-risking, which is where value gets "
                              'created. Sharma warns that network-upgrade allocations of tens to hundreds '
                              'of millions of dollars can kill a project outright [LhT4VVDW7CI @ '
                              '00:14:10]. Everyone who models degradation treats it as a hard cost. '
                              'Académie Énergie shows that accounting for it cuts over 22 percent of '
                              'annual net profit on a 1 MWh system and over 12 percent at 2 MWh '
                              '[V57-D23t6Lo @ 00:03:44]. Zami of Clearspot warns that running 200 cycles a '
                              'year instead of 100 can cut asset life from 20 years to 16 [tFP2z1s7IrM @ '
                              '00:34:55]. Stefan Müller of Enerparc closes the loop for capital: a project '
                              'is only a project if you find a bank who finance it. That makes fire '
                              'approval, grid cost and service planning bankability items to settle early, '
                              'well before financial close.'],
               'table': {'caption': 'Where BESS practitioners agree: siting, revenue, sizing and '
                                    'bankability baselines',
                         'headers': ['Consensus Point',
                                     'What Practitioners Report',
                                     'Operator Implication',
                                     'Expert Source'],
                         'rows': [['Grid proximity is the first filter',
                                   'Harmony pursues only sites within about 1 km of the point of '
                                   'connection',
                                   'Every project Harmony consented under this rule was actually built',
                                   'Regen ([Zmu3gs7y51A @ 00:34:31])'],
                                  ['Grid distance thresholds for landowners',
                                   'Under 1 km is ideal, 1 to 2 miles workable, beyond 5 km dead',
                                   'Screen parcels by substation distance at 33 kV or above first',
                                   'Solar Grid Check ([9mZg--94z1I @ 00:03:12])'],
                                  ['Three-legged revenue stack',
                                   'Arbitrage, ancillary services and capacity form the core revenue legs',
                                   'Value lives in the financial model, not in the hardware data sheet',
                                   'STG Nations Energy ([AVf_DgVRB3w @ 00:03:18])'],
                                  ['Location drives battery revenue',
                                   'Markets, prices and grid need vary sharply from region to region',
                                   'Pick nodes for price spread and service need, not for convenience',
                                   'Modo Energy ([AtMNJWhrmXE @ 00:01:46])'],
                                  ['De-risking is how developers create value',
                                   'Early, mid and late development stages each strip risk out of the '
                                   'project',
                                   'Upgrade allocations of tens to hundreds of millions of dollars kill '
                                   'projects',
                                   'Modo Energy ([LhT4VVDW7CI @ 00:14:10])'],
                                  ['Degradation is a real cost line',
                                   'Accounting for degradation cuts over 22 percent of annual net profit '
                                   'at 1 MWh',
                                   'Model degradation explicitly or the payback case will be overstated',
                                   'Académie Énergie — Efficacité & Électricité ([V57-D23t6Lo @ '
                                   '00:03:44])'],
                                  ['Bankability gaps cancel projects outright',
                                   'No fire approval, a costly grid connection, or no long-term service '
                                   'plan',
                                   'Each missing item leads directly to cancellation before construction '
                                   'starts',
                                   'BESS Engineer ([r852ohYdDhc @ 00:01:48])']]}},
              {'heading': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ["The land math is tight and specific. Sean Daly's 850 MW / roughly 1.7 GWh "
                              'Acacia project near Sydney sits on about 32 acres, around 50 MWh per acre, '
                              'which Daly calls the lower side. Density can reach 100 MWh per acre, and '
                              'typical sites run 15 to 20 acres [bWbMkkvRPWI @ 00:08:20]. Daly also tracks '
                              'hardware compression. A 20 ft container has gone from about 2 MWh to 6 or '
                              'even 7 MWh, and round-trip efficiency has climbed from 70 to 80 percent to '
                              'upwards of 90. If the parcel is not beside an existing substation, add a '
                              'utility substation of up to a few acres. On the UK lease side, Solar Grid '
                              'Check quotes £10,000 to £40,000 per acre per year against £850 to £1,200 '
                              'for solar. Rent is typically 2 to 5 percent of gross, viable footprints are '
                              '0.5 to 2 acres, and leases run 25 to 40 years with the developer paying all '
                              'costs [9mZg--94z1I @ 00:00:00]. Options pay £1,000 to £5,000 per acre '
                              'upfront; the landowner keeps that money if planning fails, and first full '
                              'rent lands 18 to 30 months later [9mZg--94z1I @ 00:04:18]. The Land '
                              'Department Podcast crew prefers outright purchase, because owning the land '
                              'lets you partner, sell off and expand [bWbMkkvRPWI @ 00:34:33].',
                              'Interconnection and long-lead equipment set the calendar. The Land '
                              'Department Podcast guests put transformer and breaker lead times at 2 to 4 '
                              'years. On their numbers, ERCOT interconnection takes about 3 years (2 if '
                              'lucky), CAISO up to 7, and Australia about 1. They add that the May 2024 '
                              'FERC order raised fees and cancellation costs, so you have to be ready to '
                              'pay to play [bWbMkkvRPWI @ 00:26:57]. Jerzy Kuzminski reports Polish grid '
                              "connection waits of usually 18 months. In Kuzminski's view, there is not "
                              'much to do except plan for it and build buffer into timelines [fDBjJyTGWDQ '
                              "@ 00:28:31]. Harmony's Francis Nicholson asks councils for 5-year-plus "
                              'implementation windows because of NESO delays. Emma of Field recommends a '
                              'Rochdale envelope approach after watching one scheme go from 200 MW to 300 '
                              'MW in the same footprint inside six months [Zmu3gs7y51A @ 00:25:44]. '
                              'Delivery logistics are a bottleneck of their own. Marcus at Fluence says '
                              'denser, heavier units have moved from high-cube containers to break-bulk '
                              'vessels and flatbed trailers. Greenfield sites are found by GPS over gravel '
                              'roads and need road surveys, and the next choke point is ADR-licensed '
                              'drivers and low-bed trailers [fzdDu4tWnGQ @ 00:06:58].',
                              'The modeling stack is what separates operators from tourists. Zami of '
                              'Clearspot simulates hourly over 20 years, noting that MILP optimisation is '
                              'linear while degradation and auxiliary load are not. Zami also flags that '
                              'augmentation in year 7 versus year 8 changes the outcome, and rejects '
                              'shortcuts like top-2 minus bottom-2 times 365 or a $50 average times 300 '
                              "days [tFP2z1s7IrM @ 00:21:13]. Académie Énergie's method runs in three "
                              'steps: define the services, model revenue, opex and degradation, then '
                              'maximise NPV over a 15 to 20 year life [V57-D23t6Lo @ 00:04:49]. Kuzminski '
                              'lists the hidden line items that break those models. EMS fees can take 20 '
                              'to 30 percent of arbitrage revenue, and SCADA can cost as much as the '
                              'container. A quoted 92 percent round-trip efficiency slides to 85 to 87 '
                              'percent after three years, and warranties multiply, so three 98 percent '
                              "guarantees stack to about 94 percent [fDBjJyTGWDQ @ 00:22:19]. Zami's "
                              'auxiliary-load example is 10 MW / 40 MWh with a 200 kW peak at $15 per '
                              'kW-month. That comes to $3,000 a month, $36,000 a year, or roughly 2 '
                              'percent of revenue, self-flagged as rough math [tFP2z1s7IrM @ 00:40:28]. '
                              'Kuzminski adds that banks want a DSCR of about 1.5.'],
               'table': {'caption': 'Street-level BESS numbers, timelines and tools quoted by operators',
                         'headers': ['Mechanic', 'Number or Tool', 'How Operators Use It', 'Expert Source'],
                         'rows': [['Energy density per acre',
                                   '50 MWh per acre on the lower side, up to 100 MWh per acre',
                                   'Typical utility sites run 15 to 20 acres plus a substation',
                                   'The Land Department Podcast ([bWbMkkvRPWI @ 00:08:20])'],
                                  ['UK battery lease rent',
                                   '£10,000 to £40,000 per acre per year, set at 2 to 5 percent of gross',
                                   'Benchmark against £850 to £1,200 per acre paid for solar',
                                   'Solar Grid Check ([9mZg--94z1I @ 00:00:00])'],
                                  ['Option payment to landowner',
                                   '£1,000 to £5,000 per acre upfront, kept if planning fails',
                                   'First full rent arrives roughly 18 to 30 months after signing',
                                   'Solar Grid Check ([9mZg--94z1I @ 00:04:18])'],
                                  ['Interconnection queue timeline',
                                   'ERCOT about 3 years, CAISO up to 7 years, Australia about 1',
                                   'Transformer and breaker lead times separately run 2 to 4 years',
                                   'The Land Department Podcast ([bWbMkkvRPWI @ 00:26:57])'],
                                  ['Revenue and degradation modeling',
                                   'Hourly simulation over 20 years using MILP optimisation',
                                   'Handle degradation and auxiliary load as nonlinear inputs, not '
                                   'averages',
                                   'Clearspot ([tFP2z1s7IrM @ 00:17:11])'],
                                  ['Hidden operating cost drag',
                                   'EMS fees take 20 to 30 percent of arbitrage revenue',
                                   'Budget SCADA at up to the cost of a battery container',
                                   'Jerzy Kuzminski ([fDBjJyTGWDQ @ 00:22:19])'],
                                  ['Microgrid sizing software workflow',
                                   'Storlytics Battery Profile Creator feeding the Microgrid Demand app',
                                   'Set the charge threshold to the net demand curve for self-sufficiency',
                                   'Storlytics Energy Storage ([pk02pXrBqWI @ 00:01:34])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Moves operators use that do not show up on a data sheet',
                           'body': 'Cheap, specific levers that working developers, engineers and advisers '
                                   'use to protect returns before steel goes in the ground.',
                           'items': ['Buy 10 to 20 extra acres for noise setback instead of paying for a '
                                     'sound wall that can run about $2 million [The Land Department '
                                     'Podcast — bWbMkkvRPWI @ 00:17:16]',
                                     'If three other developers are targeting the best node, evaluate the '
                                     'second- and third-best nodes instead [Clearspot — tFP2z1s7IrM @ '
                                     '00:06:15]',
                                     'Make the technical specification an annex to the supply contract, '
                                     'not a separate marketing document [Jerzy Kuzminski — fDBjJyTGWDQ @ '
                                     '00:23:17]',
                                     'Bring insurers in before design and supplier choice, and vet battery '
                                     'and transformer suppliers for bankability [Lockton Europe — '
                                     'UI-9nmVEA9U @ 00:08:38]']},
               'sop_steps': [{'step': 1,
                              'title': 'Screen grid distance first',
                              'action': 'Map substations at 33 kV or above and discard parcels beyond the '
                                        'viable connection radius.',
                              'detail': 'Target under 1 km to the substation and treat anything past 5 km '
                                        "as dead, mirroring Harmony's rule of staying within about 1 km of "
                                        'the point of connection [Solar Grid Check — 9mZg--94z1I @ '
                                        '00:03:12] [Regen — Zmu3gs7y51A @ 00:34:31]'},
                             {'step': 2,
                              'title': 'Lock the land on clean terms',
                              'action': 'Sign an option at £1,000 to £5,000 per acre and check indexation, '
                                        'bond and exit clauses.',
                              'detail': 'Confirm whether the RPI uplift is capped, insist that '
                                        'decommissioning is a bond or escrow account rather than a '
                                        'promise, and review the break rights that favour the developer '
                                        '[Solar Grid Check — 9mZg--94z1I @ 00:05:01]'},
                             {'step': 3,
                              'title': 'Size the ratio for the revenue',
                              'action': 'Set the MW-to-MWh ratio to match the target revenue stack and '
                                        'default to LFP chemistry.',
                              'detail': 'A 50 MW / 100 MWh system runs 2 hours, and half the power on the '
                                        "same energy runs 4. Do not let a supplier's inventory choose the "
                                        'chemistry [STG Nations Energy — AVf_DgVRB3w @ 00:01:26]'},
                             {'step': 4,
                              'title': 'Model, then contract for debt',
                              'action': 'Run an hourly 20-year model and secure floors or tolls to unlock '
                                        'lender appetite.',
                              'detail': 'Floors and tolls over 10 to 15 years unlock debt, while banks '
                                        'look for a DSCR of about 1.5 [Lockton Europe — UI-9nmVEA9U @ '
                                        '00:14:39] [Jerzy Kuzminski — fDBjJyTGWDQ @ 00:25:21]'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The sharpest split is where to plant the battery. Francis Nicholson of '
                              'Harmony Energy runs a hard proximity rule: Harmony only pursues sites '
                              'within about 1 km of the point of connection, cabling on the 400 kV Burton '
                              'site runs up to £10m per kilometre, and Nicholson credits that discipline '
                              'for every consented Harmony project getting built [Zmu3gs7y51A @ 00:34:31]. '
                              'Andy Willis of Kona Energy plays the opposite hand in ERCOT. Early Texas '
                              'batteries clustered around Houston, Austin, San Antonio and Dallas–Fort '
                              'Worth; Kona instead targets Central West Texas and the panhandle, where '
                              '2–3pm prices print at zero or roughly $1 per megawatt hour, so the charging '
                              'side of the spread is close to free [UI-9nmVEA9U @ 00:05:08]. Zami, who '
                              "scaled Pivot's storage business past 2 GW, frames the choice as game "
                              'theory: if three other developers are already chasing the best node, run '
                              'the numbers on the second- and third-best nodes instead of joining the '
                              'pile-on [tFP2z1s7IrM @ 00:06:15]. The Land Department Podcast crew show why '
                              'that matters on the ground: Houston saw a 12–18 month substation land grab, '
                              'and of 20 substations clients sent over, 10 had already been worked '
                              '[bWbMkkvRPWI @ 00:23:46]. Proximity buys certainty; contrarian nodes buy '
                              'spread.',
                              'Practitioners also split on how much merchant exposure a battery should '
                              'carry. On The smarter E panel, Stefan Müller of Enerparc describes traders '
                              'hitting the market about 25 times a day under what Enerparc calls '
                              'asset-backed trading, and the panel puts the open question bluntly: for how '
                              'long merchant can work is the crystal ball [-6QrZ_r6oJs @ 00:26:08]. Andy '
                              'Willis of Kona Energy goes the other way on debt: floors and tolls running '
                              '10–15 years are what unlock lending [UI-9nmVEA9U @ 00:14:39]. The Land '
                              'Department Podcast lays out a middle path, splitting 20–25 year contracted '
                              'revenue against merchant revenue, with 50/50 given as an example structure '
                              '[bWbMkkvRPWI @ 00:42:31]. Jerzy Kuzminski warns against leaning on capacity '
                              'payments in Poland: the capacity market derating fell from 60% to 13%, '
                              'leaving that stream practically unprofitable, optimiser and owner interests '
                              'conflict, and banks prefer hybrids [fDBjJyTGWDQ @ 00:13:22]. The live '
                              'argument is therefore not merchant versus contracted in the abstract. It is '
                              'how large the contracted slice must be before a lender signs, how long the '
                              'merchant tail can keep paying, and how much upside the owner is willing to '
                              'hand to an optimiser whose incentives do not match the long-term health of '
                              'the asset.',
                              'Footprint and land tenure are the third fault line. On The Land Department '
                              "Podcast, Sean Daly cites Acacia's 850 MW / ~1.7 GWh project near Sydney on "
                              'about 32 acres, roughly 50 MWh per acre and on the lower side, notes '
                              'density can reach 100 MWh per acre, puts typical sites at 15–20 acres, and '
                              'argues that buying 10–20 extra acres beats paying for a $2M sound wall '
                              '[bWbMkkvRPWI @ 00:17:16]. Solar Grid Check pitches a far tighter box to UK '
                              'landowners: viable sites run 0.5–2 acres, a 50 MW site takes 2–4 acres, two '
                              'acres at the top of the range out-earn 100 arable acres, and the deal is a '
                              '25–40 year lease rather than a sale, with the developer paying all costs '
                              '[9mZg--94z1I @ 00:03:57]. The Land Department guests instead prefer '
                              'outright purchase, because owned land can be partnered, sold off or '
                              'expanded [bWbMkkvRPWI @ 00:34:14]. Duration splits the same way. Zami warns '
                              "that ERCOT's 10 MW / 20 MWh arbitrage design fails in NYISO, ISO-NE or "
                              'MISO, which need longer duration, with capital recovery taking 10+ years '
                              '[tFP2z1s7IrM @ 00:12:51]. Pick footprint and duration for the market being '
                              'entered, not the one the team came from.'],
               'table': {'caption': 'Competing BESS playbooks: siting, revenue, tenure and duration',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['How close the site must sit to the point of connection',
                                   'Harmony only pursues sites within about 1 km of the point of '
                                   'connection',
                                   'Zami models the 2nd and 3rd-best nodes when three rivals crowd the '
                                   'best one',
                                   'Regen ([Zmu3gs7y51A @ 00:34:31]); Clearspot ([tFP2z1s7IrM @ '
                                   '00:06:15])'],
                                  ['Which part of the ERCOT map to target for charging spreads',
                                   'Early Texas batteries sat near Houston, Austin, San Antonio and '
                                   'Dallas–Fort Worth load centres',
                                   'Kona targets Central West Texas and the panhandle where 2–3pm prices '
                                   'hit zero or about $1',
                                   'Lockton Europe ([UI-9nmVEA9U @ 00:04:21]); Lockton Europe '
                                   '([UI-9nmVEA9U @ 00:05:08])'],
                                  ['How much revenue certainty to lock before raising debt',
                                   'Floors and tolls running 10–15 years are what unlock debt for the '
                                   'project',
                                   'Enerparc runs asset-backed trading with traders in the market about 25 '
                                   'times a day',
                                   'Lockton Europe ([UI-9nmVEA9U @ 00:14:39]); The smarter E ([-6QrZ_r6oJs '
                                   '@ 00:25:23])'],
                                  ['How heavily to lean on frequency services in the revenue stack',
                                   'Solar Grid Check puts frequency response at 50–60% of UK battery site '
                                   'revenue',
                                   'Zami reports ERCOT frequency regulation saturated, with earlier gains '
                                   'driven by rare events',
                                   'Solar Grid Check ([9mZg--94z1I @ 00:01:03]); Clearspot ([tFP2z1s7IrM @ '
                                   '00:10:12])'],
                                  ['Whether to lease the land or buy it outright',
                                   'Lease not sale on 25–40 year terms, annual rent review, developer pays '
                                   'all costs',
                                   'Outright purchase preferred so land can be partnered, sold off or '
                                   'expanded later',
                                   'Solar Grid Check ([9mZg--94z1I @ 00:03:57]); The Land Department '
                                   'Podcast ([bWbMkkvRPWI @ 00:34:14])'],
                                  ['What duration to build for the target market',
                                   'ERCOT-style 10 MW / 20 MWh arbitrage builds with short two-hour '
                                   'duration',
                                   'NYISO, ISO-NE and MISO need longer duration; UK cap-and-floor targets '
                                   '8 hours or more',
                                   'Clearspot ([tFP2z1s7IrM @ 00:12:51]); Regen ([Zmu3gs7y51A @ '
                                   '00:08:45])'],
                                  ['Whether capacity payments belong in the base case',
                                   'Capacity is sized as load forecast plus reserve margin and needs '
                                   'firmer interconnection',
                                   "Poland's capacity derating fell from 60% to 13%, making it practically "
                                   'unprofitable',
                                   'Modo Energy ([LhT4VVDW7CI @ 00:21:12]); Jerzy Kuzminski ([fDBjJyTGWDQ '
                                   '@ 00:13:22])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The most expensive mistake practitioners report is running the asset into '
                              'the ground. Zami of Clearspot uses a car redline analogy: warranties often '
                              'assume 365 cycles a year, LFP should stay within 5–95%, and running 200 '
                              'cycles instead of 100 could cut life from 20 to 16 years [tFP2z1s7IrM @ '
                              '00:34:55]. Zami also names the incentive problem: traders on quarterly '
                              'bonuses chase revenue, and gaining 5% revenue at the cost of 20% of asset '
                              'life is a bad trade [tFP2z1s7IrM @ 00:36:10]. Académie Énergie puts a '
                              'number on ignoring wear: accounting for degradation cuts over 22% of annual '
                              'net profit at 1 MWh and over 12% at 2 MWh, and the two mistakes flagged are '
                              'ignoring degradation and oversizing [V57-D23t6Lo @ 00:03:44]. Jerzy '
                              'Kuzminski adds the contract sting: daily cycle caps can void warranties, so '
                              'aggressive dispatch can cost the owner warranty cover outright [fDBjJyTGWDQ '
                              "@ 00:18:25]. Zami's charging advice points the same way, since fast "
                              "charging leaves cells unbalanced and spreading a 4-hour battery's charge "
                              'over 5–6 hours is better. The economics check is simple: every extra cycle '
                              'has to earn more than the life it burns, and the trader dispatching it '
                              'rarely carries that cost.',
                              'Contract and supplier traps come next. Jerzy Kuzminski reports a supplier '
                              'that shipped a container plus cells only, notes that warranties are '
                              'multiplicative so three stacked 98% guarantees land at about 94%, and warns '
                              'that EMS fees can take 20–30% of arbitrage revenue while SCADA can cost as '
                              "much as the container [fDBjJyTGWDQ @ 00:22:19]. Kuzminski's rule is that "
                              'technical specifications must be an annex to the contract, not a separate '
                              'marketing document, because a quoted 92% round-trip efficiency becomes '
                              '85–87% after three years [fDBjJyTGWDQ @ 00:23:17]. STG Nations Energy '
                              'points out that neither the supplier nor the EPC checks degradation, '
                              'thermal runaway and grid-connection risk end to end, which is the gap it '
                              'pitches an independent engineer with zero supplier commissions to fill '
                              '[AVf_DgVRB3w @ 00:05:25]. Andy Willis of Kona Energy says developers leave '
                              'insurance too late; insurers belong in the room before design and supplier '
                              'choice, so battery and transformer suppliers get vetted for bankability '
                              '[UI-9nmVEA9U @ 00:08:38]. Kuzminski also flags the integrator spread: 20–30 '
                              'cell makers but hundreds of integrators, often using the same cells and '
                              'quoting X versus X plus 20%. Every one of these costs lands on the owner '
                              'after signature, which is why the paperwork gets fought before it does.',
                              'The project-killers often sit outside the battery itself. Ravi Sharma of '
                              'Deriva warns that network-upgrade allocations of tens to hundreds of '
                              'millions of dollars can kill a project [LhT4VVDW7CI @ 00:14:10]. BESS '
                              'Engineer lists the cancellation triggers: no fire-safety approval, a grid '
                              'connection that is too expensive, or no long-term service plan [r852ohYdDhc '
                              '@ 00:01:48]. Logistics is the next squeeze. Marcus at Fluence says denser, '
                              'heavier units no longer fit a high cube container and now need break-bulk '
                              'and flatbed trailers instead of curtain-siders, ocean carriers resist the '
                              'cargo, Fluence competes with the wind industry for deck space, vessel '
                              'schedules are unreliable, and the coming bottleneck is ADR-licensed drivers '
                              "and low-bed trailers [fzdDu4tWnGQ @ 00:06:58]. Field's Emma shows how "
                              'design drifts under a live consent: a project started at 200 MW in '
                              'September 2023, was 300 MW in the same footprint six months later, and got '
                              'a new layout in December 2024, so Emma recommends a Rochdale envelope '
                              'approach and expects non-material amendments or s73 applications for '
                              'changes as small as 20 cm of height or ±20 units [Zmu3gs7y51A @ 00:25:44]. '
                              'Gate every site on grid cost, fire approval and haul route before spending '
                              'on design.'],
               'table': {'caption': 'Firsthand BESS failure modes and the economics check each one demands',
                         'headers': ['Failure Mode',
                                     'What Happened or Was Measured',
                                     'Economics Check',
                                     'Expert Source'],
                         'rows': [['Traders cycling the battery past its redline for revenue',
                                   'Running 200 cycles instead of 100 could cut asset life from 20 to 16 '
                                   'years',
                                   'Gaining 5% revenue at the cost of 20% of asset life is a bad trade',
                                   'Clearspot ([tFP2z1s7IrM @ 00:34:55])'],
                                  ['Leaving degradation out of the sizing model entirely',
                                   'Accounting for degradation cuts over 22% of annual net profit at 1 MWh',
                                   'Over 12% of profit lost at 2 MWh; model degradation before maximising '
                                   'NPV',
                                   'Académie Énergie — Efficacité & Électricité ([V57-D23t6Lo @ '
                                   '00:03:44])'],
                                  ['Supplier delivering less than the full system that was expected',
                                   'A supplier shipped a container plus cells only to the buyer',
                                   'Make technical specifications a contract annex, not a separate '
                                   'marketing document',
                                   'Jerzy Kuzminski ([fDBjJyTGWDQ @ 00:16:17])'],
                                  ['Hidden opex and efficiency loss eating the arbitrage margin',
                                   'EMS fees take 20–30% of arbitrage revenue and SCADA can cost as much '
                                   'as the container',
                                   'A quoted 92% round-trip efficiency becomes 85–87% after three years of '
                                   'operation',
                                   'Jerzy Kuzminski ([fDBjJyTGWDQ @ 00:22:19])'],
                                  ['HVAC faults, coolant leaks and sensor failures during peak season',
                                   'A 2-day outage in a Texas July can wipe out key revenue for the year',
                                   'Check whether revenue was concentrated, for example $1M earned in only '
                                   '2 days',
                                   'Clearspot ([tFP2z1s7IrM @ 00:24:18])'],
                                  ['Network-upgrade allocation or grid cost blowing up the project',
                                   'Upgrade allocations of tens to hundreds of millions of dollars can '
                                   'kill a project',
                                   'A grid connection that is too expensive leads straight to cancellation',
                                   'Modo Energy ([LhT4VVDW7CI @ 00:14:10]); BESS Engineer ([r852ohYdDhc @ '
                                   '00:01:48])'],
                                  ['Ocean carriers and haulage capacity choking delivery to site',
                                   'Carriers do not want the cargo and Fluence competes with wind for '
                                   'break-bulk deck space',
                                   'The coming bottleneck is ADR-licensed drivers and low-bed trailers for '
                                   'heavy units',
                                   'Project Cargo Professionals ([fzdDu4tWnGQ @ 00:05:08])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Four kill-switches before capital goes in',
                           'body': 'Each gate comes straight from a loss, cancellation or contract trap '
                                   'the practitioners lived through. Fail one and the project stops or '
                                   'gets re-priced.',
                           'items': ['Kill or re-price any site where network-upgrade allocations reach '
                                     'tens to hundreds of millions of dollars before paying for mid-stage '
                                     'engineering [Modo Energy — LhT4VVDW7CI @ 00:14:10].',
                                     'Hold dispatch inside warranty terms, keeping LFP between 5% and 95% '
                                     'and below the cycle assumptions the warranty is written on '
                                     '[Clearspot — tFP2z1s7IrM @ 00:32:43].',
                                     'Attach the technical specification as a contract annex and price EMS '
                                     'fees, SCADA and real round-trip efficiency before signing [Jerzy '
                                     'Kuzminski — fDBjJyTGWDQ @ 00:23:17].',
                                     'Bring insurers in before design and supplier choice so battery and '
                                     'transformer suppliers are vetted for bankability [Lockton Europe — '
                                     'UI-9nmVEA9U @ 00:08:38].']}}],
 'pull_quote': '"The only projects that get built are the ones where all risks are understood and managed '
               'at every stage." — BESS Engineer (r852ohYdDhc @ 00:02:32).',
 'diagram_id': 'diag-02',
 'action_checklist': ['Screen every candidate site on grid distance first: under 1 km is ideal, 1–2 miles '
                      'is workable, and beyond 5 km the site is dead [Solar Grid Check — 9mZg--94z1I @ '
                      '00:03:12].',
                      'Simulate revenue hourly over 20 years with degradation and auxiliary load included, '
                      'and reject top-2 minus bottom-2 times 365 shortcuts [Clearspot — tFP2z1s7IrM @ '
                      '00:21:13].',
                      'Lock floors or tolls running 10–15 years on the slice of revenue that has to '
                      'service debt [Lockton Energy — UI-9nmVEA9U @ 00:14:39].',
                      'Build buffer into the timeline because grid connection waits usually run 18 months '
                      'and administration plus investor over-optimism add delay [Jerzy Kuzminski — '
                      'fDBjJyTGWDQ @ 00:28:31].',
                      'On the landowner side, insist the decommissioning obligation sits in a bond or '
                      'escrow account, not a promise [Solar Grid Check — 9mZg--94z1I @ 00:05:01].',
                      'On any acquired portfolio, compare past operation against OEM parameters, check '
                      'whether revenue was concentrated in a few days, and set up data monitoring '
                      '[Clearspot — tFP2z1s7IrM @ 01:10:35].'],
 'statutory_citations': [{'title': 'Clearspot — 2GW BESS Lessons Every Asset Owner Needs [00:34:55]',
                          'url': 'https://www.youtube.com/watch?v=tFP2z1s7IrM&t=2095s',
                          'relevance': 'Primary practitioner testimony on cycling abuse, degradation, '
                                       'trader incentives and asset-life economics.'},
                         {'title': 'Jerzy Kuzminski — 01 What is BESS and Why Poland [00:22:19]',
                          'url': 'https://www.youtube.com/watch?v=fDBjJyTGWDQ&t=1339s',
                          'relevance': 'Primary practitioner testimony on hidden EMS and SCADA costs, '
                                       'warranty traps and supplier contract failures.'},
                         {'title': 'Modo Energy — Developing BESS - from greenfield to grid with Ravi '
                                   'Sharma - Transmission [00:14:10]',
                          'url': 'https://www.youtube.com/watch?v=LhT4VVDW7CI&t=850s',
                          'relevance': 'Primary practitioner testimony on network-upgrade allocations '
                                       'killing greenfield BESS projects.'},
                         {'title': 'Lockton Europe — Lockton Energy And Power Podcast | Scaling Success: '
                                   'Expanding A BESS Business [00:14:39]',
                          'url': 'https://www.youtube.com/watch?v=UI-9nmVEA9U&t=879s',
                          'relevance': 'Primary practitioner testimony on floors and tolls unlocking debt '
                                       'and ERCOT siting strategy.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'Zmu3gs7y51A',
                       'title': 'Planning for clean Energy - Assessing battery energy storage system '
                                '(BESS) applications',
                       'channel': 'Regen',
                       'author': 'Regen',
                       'text': 'Harmony only pursues sites within about 1 km of the point of connection, '
                               'and as a result every project they consented was built.',
                       'tip': 'Harmony only pursues sites within about 1 km of the point of connection, '
                              'and as a result every project they consented was built.',
                       'timestamp': 2071,
                       'timestamp_seconds': 2071,
                       'timestamp_label': '[00:34:31]',
                       'url': 'https://www.youtube.com/watch?v=Zmu3gs7y51A&t=2071s',
                       'markdown': '[00:34:31](https://www.youtube.com/watch?v=Zmu3gs7y51A&t=2071s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Zmu3gs7y51A',
                       'title': 'Planning for clean Energy - Assessing battery energy storage system '
                                '(BESS) applications',
                       'channel': 'Regen',
                       'author': 'Regen',
                       'text': 'The project started at 200 MW in September 2023 and six months later it '
                               'was 300 MW in the same footprint.',
                       'tip': 'The project started at 200 MW in September 2023 and six months later it was '
                              '300 MW in the same footprint.',
                       'timestamp': 1544,
                       'timestamp_seconds': 1544,
                       'timestamp_label': '[00:25:44]',
                       'url': 'https://www.youtube.com/watch?v=Zmu3gs7y51A&t=1544s',
                       'markdown': '[00:25:44](https://www.youtube.com/watch?v=Zmu3gs7y51A&t=1544s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'AVf_DgVRB3w',
                       'title': 'BESS 101 for developers: sizing, chemistry, revenue stacking',
                       'channel': 'STG Nations Energy',
                       'author': 'STG Nations Energy',
                       'text': 'Size the ratio for the revenue.',
                       'tip': 'Size the ratio for the revenue.',
                       'timestamp': 86,
                       'timestamp_seconds': 86,
                       'timestamp_label': '[00:01:26]',
                       'url': 'https://www.youtube.com/watch?v=AVf_DgVRB3w&t=86s',
                       'markdown': '[00:01:26](https://www.youtube.com/watch?v=AVf_DgVRB3w&t=86s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'AtMNJWhrmXE',
                       'title': 'The Economics of Grid-Scale Batteries Explained',
                       'channel': 'Modo Energy',
                       'author': 'Modo Energy',
                       'text': 'Location is everything for how batteries can make money.',
                       'tip': 'Location is everything for how batteries can make money.',
                       'timestamp': 106,
                       'timestamp_seconds': 106,
                       'timestamp_label': '[00:01:46]',
                       'url': 'https://www.youtube.com/watch?v=AtMNJWhrmXE&t=106s',
                       'markdown': '[00:01:46](https://www.youtube.com/watch?v=AtMNJWhrmXE&t=106s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'V57-D23t6Lo',
                       'title': 'BESS sizing: how to design a battery system that actually pays back',
                       'channel': 'Académie Énergie — Efficacité & Électricité',
                       'author': 'Académie Énergie — Efficacité & Électricité',
                       'text': 'Pushing a battery harder wears it out quicker.',
                       'tip': 'Pushing a battery harder wears it out quicker.',
                       'timestamp': 164,
                       'timestamp_seconds': 164,
                       'timestamp_label': '[00:02:44]',
                       'url': 'https://www.youtube.com/watch?v=V57-D23t6Lo&t=164s',
                       'markdown': '[00:02:44](https://www.youtube.com/watch?v=V57-D23t6Lo&t=164s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'r852ohYdDhc',
                       'title': 'From Site to COD: The 6 Stages of a BESS Project',
                       'channel': 'BESS Engineer',
                       'author': 'BESS Engineer',
                       'text': 'The only projects that get built are the ones where all risks are '
                               'understood and managed at every stage.',
                       'tip': 'The only projects that get built are the ones where all risks are '
                              'understood and managed at every stage.',
                       'timestamp': 152,
                       'timestamp_seconds': 152,
                       'timestamp_label': '[00:02:32]',
                       'url': 'https://www.youtube.com/watch?v=r852ohYdDhc&t=152s',
                       'markdown': '[00:02:32](https://www.youtube.com/watch?v=r852ohYdDhc&t=152s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'pk02pXrBqWI',
                       'title': 'How to Size BESS for Microgrid Applications',
                       'channel': 'Storlytics Energy Storage',
                       'author': 'Storlytics Energy Storage',
                       'text': 'So, the blue one here is negative, showing that this is generation.',
                       'tip': 'So, the blue one here is negative, showing that this is generation.',
                       'timestamp': 58,
                       'timestamp_seconds': 58,
                       'timestamp_label': '[00:00:58]',
                       'url': 'https://www.youtube.com/watch?v=pk02pXrBqWI&t=58s',
                       'markdown': '[00:00:58](https://www.youtube.com/watch?v=pk02pXrBqWI&t=58s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'LhT4VVDW7CI',
                       'title': 'Developing BESS - from greenfield to grid with Ravi Sharma - Transmission',
                       'channel': 'Modo Energy',
                       'author': 'Modo Energy',
                       'text': 'Network-upgrade allocations of tens to hundreds of millions of dollars can '
                               'kill a project.',
                       'tip': 'Network-upgrade allocations of tens to hundreds of millions of dollars can '
                              'kill a project.',
                       'timestamp': 850,
                       'timestamp_seconds': 850,
                       'timestamp_label': '[00:14:10]',
                       'url': 'https://www.youtube.com/watch?v=LhT4VVDW7CI&t=850s',
                       'markdown': '[00:14:10](https://www.youtube.com/watch?v=LhT4VVDW7CI&t=850s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'bWbMkkvRPWI',
                       'title': 'The Ultimate Guide to BESS with Drew Lebowitz and Sean Daly | TLD 032',
                       'channel': 'The Land Department Podcast',
                       'author': 'The Land Department Podcast',
                       'text': 'You got to really be ready to pay to play.',
                       'tip': 'You got to really be ready to pay to play.',
                       'timestamp': 1736,
                       'timestamp_seconds': 1736,
                       'timestamp_label': '[00:28:56]',
                       'url': 'https://www.youtube.com/watch?v=bWbMkkvRPWI&t=1736s',
                       'markdown': '[00:28:56](https://www.youtube.com/watch?v=bWbMkkvRPWI&t=1736s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'bWbMkkvRPWI',
                       'title': 'The Ultimate Guide to BESS with Drew Lebowitz and Sean Daly | TLD 032',
                       'channel': 'The Land Department Podcast',
                       'author': 'The Land Department Podcast',
                       'text': 'If you own that land outright you can partner with other groups you can '
                               'sell off you can have future development you can expand your operations.',
                       'tip': 'If you own that land outright you can partner with other groups you can '
                              'sell off you can have future development you can expand your operations.',
                       'timestamp': 2073,
                       'timestamp_seconds': 2073,
                       'timestamp_label': '[00:34:33]',
                       'url': 'https://www.youtube.com/watch?v=bWbMkkvRPWI&t=2073s',
                       'markdown': '[00:34:33](https://www.youtube.com/watch?v=bWbMkkvRPWI&t=2073s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '9mZg--94z1I',
                       'title': 'Leasing Land for Battery Storage: What Your Land Is Actually Worth (UK, '
                                '2026)',
                       'channel': 'Solar Grid Check',
                       'author': 'Solar Grid Check',
                       'text': 'And the cable to get there is brutally expensive.',
                       'tip': 'And the cable to get there is brutally expensive.',
                       'timestamp': 192,
                       'timestamp_seconds': 192,
                       'timestamp_label': '[00:03:12]',
                       'url': 'https://www.youtube.com/watch?v=9mZg--94z1I&t=192s',
                       'markdown': '[00:03:12](https://www.youtube.com/watch?v=9mZg--94z1I&t=192s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '9mZg--94z1I',
                       'title': 'Leasing Land for Battery Storage: What Your Land Is Actually Worth (UK, '
                                '2026)',
                       'channel': 'Solar Grid Check',
                       'author': 'Solar Grid Check',
                       'text': 'It should be a bond or escrow account, not a promise.',
                       'tip': 'It should be a bond or escrow account, not a promise.',
                       'timestamp': 301,
                       'timestamp_seconds': 301,
                       'timestamp_label': '[00:05:01]',
                       'url': 'https://www.youtube.com/watch?v=9mZg--94z1I&t=301s',
                       'markdown': '[00:05:01](https://www.youtube.com/watch?v=9mZg--94z1I&t=301s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'tFP2z1s7IrM',
                       'title': '2GW BESS Lessons Every Asset Owner Needs',
                       'channel': 'Clearspot',
                       'author': 'Clearspot',
                       'text': 'So you have to build your project based on where you see the future of the '
                               'market is.',
                       'tip': 'So you have to build your project based on where you see the future of the '
                              'market is.',
                       'timestamp': 592,
                       'timestamp_seconds': 592,
                       'timestamp_label': '[00:09:52]',
                       'url': 'https://www.youtube.com/watch?v=tFP2z1s7IrM&t=592s',
                       'markdown': '[00:09:52](https://www.youtube.com/watch?v=tFP2z1s7IrM&t=592s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'tFP2z1s7IrM',
                       'title': '2GW BESS Lessons Every Asset Owner Needs',
                       'channel': 'Clearspot',
                       'author': 'Clearspot',
                       'text': 'That needs to be done at strategy and procurement phase with the feedback '
                               'from operators.',
                       'tip': 'That needs to be done at strategy and procurement phase with the feedback '
                              'from operators.',
                       'timestamp': 3225,
                       'timestamp_seconds': 3225,
                       'timestamp_label': '[00:53:45]',
                       'url': 'https://www.youtube.com/watch?v=tFP2z1s7IrM&t=3225s',
                       'markdown': '[00:53:45](https://www.youtube.com/watch?v=tFP2z1s7IrM&t=3225s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'UI-9nmVEA9U',
                       'title': 'Lockton Energy And Power Podcast | Scaling Success: Expanding A BESS '
                                'Business',
                       'channel': 'Lockton Europe',
                       'author': 'Lockton Europe',
                       'text': "I'd say engage early is definitely rule number one.",
                       'tip': "I'd say engage early is definitely rule number one.",
                       'timestamp': 1596,
                       'timestamp_seconds': 1596,
                       'timestamp_label': '[00:26:36]',
                       'url': 'https://www.youtube.com/watch?v=UI-9nmVEA9U&t=1596s',
                       'markdown': '[00:26:36](https://www.youtube.com/watch?v=UI-9nmVEA9U&t=1596s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'fzdDu4tWnGQ',
                       'title': 'Fluence and the BESS Boom | The Future of Battery Storage Logistics',
                       'channel': 'Project Cargo Professionals',
                       'author': 'Project Cargo Professionals',
                       'text': 'Our biggest competitors are in the wind industry.',
                       'tip': 'Our biggest competitors are in the wind industry.',
                       'timestamp': 308,
                       'timestamp_seconds': 308,
                       'timestamp_label': '[00:05:08]',
                       'url': 'https://www.youtube.com/watch?v=fzdDu4tWnGQ&t=308s',
                       'markdown': '[00:05:08](https://www.youtube.com/watch?v=fzdDu4tWnGQ&t=308s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'fDBjJyTGWDQ',
                       'title': '01 What is BESS and Why Poland',
                       'channel': 'Jerzy Kuzminski',
                       'author': 'Jerzy Kuzminski',
                       'text': "That's why technical specifications must be an annex to the contract, not "
                               'a separate marketing document.',
                       'tip': "That's why technical specifications must be an annex to the contract, not a "
                              'separate marketing document.',
                       'timestamp': 1397,
                       'timestamp_seconds': 1397,
                       'timestamp_label': '[00:23:17]',
                       'url': 'https://www.youtube.com/watch?v=fDBjJyTGWDQ&t=1397s',
                       'markdown': '[00:23:17](https://www.youtube.com/watch?v=fDBjJyTGWDQ&t=1397s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '-6QrZ_r6oJs',
                       'title': 'From EVs to BESS: Why capital is flowing to batteries – with Laurent '
                                'Segalen and Stefan Mueller',
                       'channel': 'The smarter E',
                       'author': 'The smarter E',
                       'text': 'A project is only a project if you find a bank who finance it.',
                       'tip': 'A project is only a project if you find a bank who finance it.',
                       'timestamp': 2070,
                       'timestamp_seconds': 2070,
                       'timestamp_label': '[00:34:30]',
                       'url': 'https://www.youtube.com/watch?v=-6QrZ_r6oJs&t=2070s',
                       'markdown': '[00:34:30](https://www.youtube.com/watch?v=-6QrZ_r6oJs&t=2070s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'}]}
