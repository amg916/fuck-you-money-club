from __future__ import annotations

CHAPTER_12 = {'id': 'Q12',
 'chapter_id': 'Q12',
 'chapter_number': 12,
 'question_number': 12,
 'slug': 'q12-community-pushback-and-decentralized-alternatives',
 'question_prompt': 'Why are communities pushing back on AI data centers, and do smaller, decentralized or '
                    'edge alternatives reduce the land and power burden?',
 'kicker': 'Q12 / THE BIG MONEY PLAYBOOKS',
 'title': 'Community Pushback and Decentralized Alternatives',
 'subtitle': "Water use, Indigenous land and 'data colonialism', utility land-taking for power lines, "
             "Florida's Project Tango, secrecy and local resistance, county preparedness, and "
             'decentralized, edge and tiny data centers as alternatives to hyperscale',
 'layout_template': 'action_worksheet_summary',
 'reading_time_minutes': 15,
 'executive_summary': 'Opposition to hyperscale AI campuses is now organized and winning votes. Polls show '
                      '65% to 70% of residents against local sites. Palm Beach County killed Project '
                      'Tango’s expansion 5-1, Tulsa and the Seminole Nation passed moratoria, and 40 of 41 '
                      'Ohio county ballot initiatives ban sites above 25 MW. Organizers attack water use, '
                      '97 dB noise, 16-degree heat islands, doubled power bills, construction jobs that '
                      'shrink from 1,500 to three permanent roles, and land deals locked behind NDAs. The '
                      'decentralized camp answers with smaller footprints: Span’s 16-GPU node at a claimed '
                      '$3M per MW in six months, 20 MW sites paired with district heating to jump power '
                      'queues, and 10 kW air-cooled racks that fit brownfield halls. Speakers split on '
                      'whether closed-loop cooling exists at all, and on whether distributed loads '
                      'strengthen or strain distribution grids.',
 'key_metrics': [{'label': 'Proposed hyperscale sites on native lands',
                  'metric': 'Proposed hyperscale sites on native lands',
                  'value': '103 to 160 proposed hyperscale data centers',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Crystal Two Bulls counts these sites using a crowdsourced map built from '
                             'organizer networks; Tulsa passed a 9-month moratorium and the Seminole '
                             'Nation passed one unanimously.',
                  'source': 'Democracy Now! ([Ac0-fBK0LVQ @ 00:04:14])'},
                 {'label': 'Distributed node build cost versus 100 MW campus',
                  'metric': 'Distributed node build cost versus 100 MW campus',
                  'value': '$3M/MW and 6 months vs. $15M/MW and 3-5 years',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Span’s Xfra 16-GPU home node, compared on cost per MW and build time against '
                             'a 100 MW site.',
                  'source': 'Latitude Media ([D7D1CPOoub4 @ 00:20:50])'},
                 {'label': 'Local opposition and top grievances',
                  'metric': 'Local opposition and top grievances',
                  'value': '65% opposed; electricity 72%, water 64%, noise 41%',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'A Quinnipiac poll cited on PBS NewsHour, alongside a separate finding that '
                             'seven in 10 people oppose a local data center.',
                  'source': 'PBS NewsHour ([fkB8mt1DEVw @ 00:04:45])'},
                 {'label': 'Ohio county ballot initiatives banning large sites',
                  'metric': 'Ohio county ballot initiatives banning large sites',
                  'value': '40 of 41 ban data centers above 25 MW',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'County-level ballot measures reviewed during an election-season discussion '
                             'of distributed data centers.',
                  'source': 'Latitude Media ([D7D1CPOoub4 @ 00:50:40])'}],
 'sections': [{'title': 'Section 1: The Practitioner Consensus',
               'paragraphs': ['Wherever a hyperscale campus is proposed, opposition is now the default '
                              'response, and the numbers match across countries. On PBS NewsHour, Brangham '
                              'reported that seven in 10 people oppose a local data center. A Quinnipiac '
                              'poll put opposition at 65%: 72% of respondents cited electricity, 64% '
                              'water, and 41% noise [fkB8mt1DEVw @ 00:04:45]. CBC News found the same mood '
                              'in Canada, where 68% of Canadians would oppose a large data center near '
                              'their home. Olds, Alberta, a town of about 10,000, faces a proposed complex '
                              '10 times the size of Canada’s largest, and residents say they were never '
                              'consulted [Rj_icscgo_Q @ 00:03:14]. That sentiment is turning into votes. '
                              'In western Palm Beach County, Project Tango is a 600 MW, five-building '
                              'campus next to Florida’s largest power plant. Its zoning committee '
                              'recommended denial, and the County Commission then rejected the 1.5M sq ft '
                              'expansion 5-1. A national protest day of roughly 100 events, nine of them '
                              'in Florida, was already planned [iYCYPKhdqcY @ 00:05:09]. On Latitude '
                              'Media, the panel noted that 40 of 41 Ohio county ballot initiatives ban '
                              'data centers above 25 MW [D7D1CPOoub4 @ 00:50:40]. Every operator in this '
                              'chapter treats organized resistance as a standard site condition. The one '
                              'factor that reliably changes the response is the size of the footprint, '
                              'which runs through every section that follows.',
                              'Speakers repeat the same specific grievances. Crystal Two Bulls of Honor '
                              'the Earth and the No Data Center Coalition puts facility water use at '
                              '300,000 to 2.7 million gallons per year, “even 5 million.” Two Bulls says '
                              'corporate closed-loop and water-positive claims have been “dispelled,” and '
                              'puts noise at about 97 dB, compared with roughly 140 dB for an LRAD: “So, '
                              '97 to 140 is not a big jump” [Ac0-fBK0LVQ @ 00:08:43]. In a second cut of '
                              'that testimony, Two Bulls adds heat islands of up to 16 degrees and Montana '
                              'bills that have almost doubled. Two Bulls also describes how the jobs '
                              'disappear: up to 1,500 construction jobs, mostly not local, over as long as '
                              'two years, then as few as three full-time jobs, as in Rapid City, South '
                              'Dakota [OeYd0jErrF4 @ 00:01:42]. Asianometry estimates that a 15 MW IT '
                              'facility uses about 80 to 130 million gallons a year, “as much water as '
                              'three hospitals, or two 18-hole golf courses” [tJYSzc7YkY0 @ 00:00:02]. '
                              'Industrial hygienists Tammy Clark and Kristen Megan Kelly focus on noise '
                              'measurement. Tonal and ELF noise has to be measured in dBC or dBZ, not dBA. '
                              'Vendors quote “55 dB at the fence” against an 85 dBA occupational action '
                              'level that assumes 8-hour exposure, yet these sites run 24/7 [S_6FoEr75bs @ '
                              '00:11:30].',
                              'Speakers also agree on how deals get made: quietly, through intermediaries, '
                              'on land chosen because local rules are weak. Two Bulls says Microsoft, '
                              'Google, Apple, Meta and Amazon approach tribes through subsidiaries and '
                              'native-owned energy companies. The pitch opens with solar, NDAs get signed, '
                              'and only then does the conversation shift to a data center. The result is '
                              'tribal leadership that answers to corporations rather than to its own '
                              'people [Ac0-fBK0LVQ @ 00:03:27]. Clark and Kelly describe the same approach '
                              'on farmland: NDAs and leases pitched as “temporary” and “probably never '
                              'going to happen,” sites picked for weak zoning, $10M offers to farmers, and '
                              'one family that turned down $25M [S_6FoEr75bs @ 00:39:30]. On PBS NewsHour, '
                              'Michael Webber links the secrecy to unincorporated areas where jurisdiction '
                              'is unclear. Webber concedes that some of the stealth is about hiding from '
                              'competitors, but says companies are “very late” to engage communities, '
                              'repeating the mistake of the shale era [fkB8mt1DEVw @ 00:21:11]. The '
                              'decentralized camp turns these complaints into a sales pitch. Mark '
                              'Bjornsgaard says smaller sites surrounded by solar can run off-grid and put '
                              'less stress on the grid, and Joshua Feinberg adds that they also draw less '
                              'community pushback [W92xU-lo1Gc @ 00:01:55]. The pattern holds across '
                              'sources: secrecy, scale and grid load drive the backlash.'],
               'table': {'caption': 'Where practitioners agree on community pushback and footprint',
                         'headers': ['Consensus Point',
                                     'What Practitioners Report',
                                     'Operator Implication',
                                     'Expert Source'],
                         'rows': [['Opposition is the majority local position',
                                   'Quinnipiac found 65% opposed, citing electricity 72%, water 64%, noise '
                                   '41%',
                                   'Assume organized local resistance exists before securing land or '
                                   'announcing a site',
                                   'PBS NewsHour ([fkB8mt1DEVw @ 00:04:45])'],
                                  ['Elected bodies are voting hyperscale expansions down',
                                   'Project Tango expansion denied 5-1 after zoning committee recommended '
                                   'denial',
                                   'A staff recommendation to deny signals likely defeat at the final '
                                   'commission vote',
                                   'WPLG Local 10 ([iYCYPKhdqcY @ 00:05:09])'],
                                  ['Moratoria are spreading across tribal and municipal governments',
                                   'Tulsa passed a 9-month moratorium and the Seminole Nation passed one '
                                   'unanimously',
                                   'Track tribal council and city agendas as closely as county zoning '
                                   'dockets',
                                   'Democracy Now! ([Ac0-fBK0LVQ @ 00:04:14])'],
                                  ['Construction jobs do not turn into lasting local employment',
                                   'Up to 1,500 mostly non-local construction jobs, then as few as 3 in '
                                   'Rapid City',
                                   'Opponents will check jobs pitches against the permanent headcount '
                                   'after construction',
                                   'Democracy Now! ([OeYd0jErrF4 @ 00:01:42])'],
                                  ['Ratepayer bills are a leading grievance at hearings',
                                   'Montana bills almost doubled and one person in a trailer got a $900 '
                                   'bill',
                                   'Expect residents to blame utility cost increases on large new loads',
                                   'Democracy Now! ([Ac0-fBK0LVQ @ 00:11:38])'],
                                  ['Land is acquired through NDAs and soft-pitched leases',
                                   'Leases pitched as temporary and probably never going to happen, with '
                                   '$10M farm offers',
                                   'Once NDA terms surface, they become the opposition’s strongest '
                                   'argument',
                                   'Careers Over Beers Podcast ([S_6FoEr75bs @ 00:06:46])'],
                                  ['Smaller decentralized sites draw less community fire',
                                   'Smaller sites with surrounding solar can run off-grid, with less grid '
                                   'stress and less pushback',
                                   'Reducing site size is a way to lower political risk, not only a sizing '
                                   'decision',
                                   'DCSMI ([W92xU-lo1Gc @ 00:01:55])']]}},
              {'title': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['The distributed model depends on a gap in cost and build time. On Latitude '
                              'Media, Span’s Xfra is presented as a 16-GPU home node, claimed at $3M per '
                              'MW and six months to build, compared with $15M per MW and three to five '
                              'years for a 100 MW site [D7D1CPOoub4 @ 00:20:50]. In that discussion, '
                              '“distributed” means tens of MW or less, mostly for inference. One working '
                              'definition is distribution-connected sites of 25 MW or below: “So they’re '
                              'not connected at transmission voltage. They’re being connected at on '
                              'distribution” [D7D1CPOoub4 @ 00:27:04]. The unit economics come from the '
                              'same panel. Offtakes of three to five years are easy at 5 MW and above. A '
                              'residential install costs about $150K, and an estimated 10% of homeowners '
                              'would buy in. Shah describes 5,000 data centers of 250 kW at Crown Castle '
                              'towers selling merchant tokens, which is not a long-term fixed-price '
                              'offtake. Span is also offering free power to new-construction cul-de-sacs '
                              '[D7D1CPOoub4 @ 00:43:15]. Size labels are elastic. DCSMI’s Adam Gibson '
                              'notes that edge means 5 to 10 MW to a hyperscaler but 10 racks in a '
                              'regional location to others, and that a 50-rack site counts as very large '
                              'edge in Alaska. Providers define edge to suit their own focus [tWgTVIzYje8 '
                              '@ 00:00:15]. In practice, that elasticity gives a developer room to pitch '
                              'the same capacity as a set of small, quiet distribution-level nodes.',
                              'The second lever is power position. Mark Bjornsgaard calls it the race to '
                              'the electron. In the UK and Europe, a 50 MW district-heating project gets '
                              'ahead of a 100 MW data center in the power queue, so Bjornsgaard’s firm '
                              'builds 20 MW data centers paired with district heating to move up in '
                              'allocation [W92xU-lo1Gc @ 00:02:43]. Bjornsgaard also cites 6.5 TWh of '
                              'curtailed UK wind, about 750 MW wasted, as the kind of stranded power that '
                              'smaller sites with on-site generation and storage can absorb. Michael '
                              'Webber says on-site, behind-the-meter generation solves speed-to-power when '
                              'utilities quote four to five years for a grid connection, and that it can '
                              'avoid August-afternoon peaks. Diesel generators, however, are outlawed in '
                              'California [fkB8mt1DEVw @ 00:08:04]. SambaNova’s Rodrigo Liang tackles the '
                              'problem at the rack. State-of-the-art racks draw 100 to 150 kW and are '
                              'heading to 500 kW with liquid cooling, while SambaNova racks run at 10 kW, '
                              'air-cooled, and fit into existing brownfield data centers [JvqqjgCu9mg @ '
                              '00:02:22]. Liang claims 10x throughput on the workload that covers 80% of '
                              'inference and payback in six months, compared with 18 to 24 months. Running '
                              'prefill on Nvidia and decode on SambaNova, Liang says, yields 3 to 4x '
                              'throughput for 10% more power [JvqqjgCu9mg @ 00:19:17]. Taken together, '
                              'low-power racks and queue-friendly pairings let compute get built without '
                              'the gigawatt footprint that triggers hearings.',
                              'Opponents use their own repeatable methods, and site teams that ignore them '
                              'lose. Two Bulls lists the field kit: town halls, tribal council meetings, '
                              'door knocking, petitions, and coalitions with agriculture, ranchers and '
                              'landowners. The results so far include Tulsa’s nine-month moratorium, a '
                              'unanimous Seminole Nation moratorium, and a Muscogee resolution that was '
                              'blocked [Ac0-fBK0LVQ @ 00:04:55]. Clark and Kelly go further. They advise '
                              'withholding tax subsidies, noting that a Google representative testified '
                              '“we’ll go somewhere else.” They also call for environmental impact studies, '
                              'which they say stopped a Michigan battery plant, and for recalling '
                              'officials who approve deals. They claim 50% of data center construction '
                              'slated for 2026 has been stopped [S_6FoEr75bs @ 00:23:26]. Their monitoring '
                              'routine is simple: check diesel-generator air-permit filings every month. '
                              '“So keep once a month, go on there and look” [S_6FoEr75bs @ 01:16:47]. Jeff '
                              'Pierson offers counties a way out of the binary trap of general zoning or a '
                              'total ban: a six-factor County Siting Posture Metric. Scores from 0 to 44 '
                              'point to a conditional use permit, 45 to 79 to overlay districts, and 80 to '
                              '100 to a ban. Pierson stresses that documentation, not the score itself, is '
                              'the legal shield [CmmE71lfGdw @ 00:05:01]. Developers who understand these '
                              'tools can predict which posture a county will take before filing.'],
               'table': {'caption': 'Street mechanics, tools and unit numbers for distributed and '
                                    'contested sites',
                         'headers': ['Mechanic',
                                     'Exact Numbers Stated',
                                     'How Operators Use It',
                                     'Expert Source'],
                         'rows': [['Distributed 16-GPU home node build',
                                   'Span Xfra claimed at $3M/MW and 6 months versus $15M/MW and 3-5 years',
                                   'Deploy inference capacity in months without a 100 MW campus fight',
                                   'Latitude Media ([D7D1CPOoub4 @ 00:20:50])'],
                                  ['District-heating pairing to jump the power queue',
                                   '20 MW data centers paired with heating; a 50 MW heat project beats a '
                                   '100 MW data center',
                                   'Pair compute with a heat customer to move up in UK and European grid '
                                   'allocation',
                                   'DCSMI ([W92xU-lo1Gc @ 00:02:43])'],
                                  ['Low-power racks that fit brownfield halls',
                                   '10 kW air-cooled racks versus 100-150 kW liquid-cooled racks heading '
                                   'to 500 kW',
                                   'Retrofit existing data centers instead of building new hyperscale '
                                   'shells',
                                   'Founders Explain The World ([JvqqjgCu9mg @ 00:02:22])'],
                                  ['Behind-the-meter power to beat interconnection waits',
                                   'Utilities quote 4-5 years for a grid connection; on-site power avoids '
                                   'August peaks',
                                   'Use on-site generation for speed-to-power where diesel is not outlawed',
                                   'PBS NewsHour ([fkB8mt1DEVw @ 00:08:04])'],
                                  ['Unused industrial interconnection headroom',
                                   'ProLogis customers run at 25% of their 5, 10 and 20 MW '
                                   'interconnections',
                                   'Look for stranded capacity already connected at existing industrial '
                                   'sites',
                                   'Latitude Media ([D7D1CPOoub4 @ 00:27:26])'],
                                  ['EV charging sites as compute hosts',
                                   'L3 chargers run at roughly 15-30% utilization; EV tariffs block added '
                                   'load',
                                   'Opt the site into a C&I tariff to add compute load at charger '
                                   'locations',
                                   'Latitude Media ([D7D1CPOoub4 @ 00:39:37])'],
                                  ['County Siting Posture Metric scoring bands',
                                   '0-44 conditional use permit, 45-79 overlay districts, 80-100 ban',
                                   'Predict a county’s regulatory posture and document every factor scored',
                                   'Jeff Pierson ([CmmE71lfGdw @ 00:05:01])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Field Tricks From the Distributed and Opposition Camps',
                           'body': 'Specific moves the speakers teach for building small, defending a '
                                   'site, or attacking one.',
                           'items': ['Spiky inference loads create power-quality, voltage and harmonics '
                                     'risk on distribution circuits, which the panel calls solvable, with '
                                     'storage as the fix [Latitude Media — D7D1CPOoub4 @ 00:26:26]',
                                     'Check diesel-generator air-permit filings every month to catch '
                                     'backup generation before it shows up at a hearing: “So keep once a '
                                     'month, go on there and look” [Careers Over Beers Podcast — '
                                     'S_6FoEr75bs @ 01:16:47]',
                                     'Ask whether a closed loop is filled once or uses water every day, '
                                     'because that answer determines the real water draw [PBS NewsHour — '
                                     'fkB8mt1DEVw @ 00:10:45]',
                                     'Run prefill on Nvidia and decode on SambaNova for a claimed 3 to 4x '
                                     'throughput at only 10% more power [Founders Explain The World — '
                                     'JvqqjgCu9mg @ 00:24:25]']},
               'sop_steps': [{'step': 1,
                              'title': 'Size below the ballot line',
                              'action': 'Design sites as distribution-connected nodes of 25 MW or less, '
                                        'mostly for inference.',
                              'detail': '40 of 41 Ohio county ballot initiatives ban data centers above 25 '
                                        'MW, which makes the sub-25 MW distribution tier the footprint '
                                        'least exposed to bans [Latitude Media — D7D1CPOoub4 @ 00:50:40]'},
                             {'step': 2,
                              'title': 'Score the county before filing',
                              'action': 'Run the six CSPM factors: infrastructure, agriculture, regulatory '
                                        'capacity, economics, community alignment and cumulative regional '
                                        'pressure.',
                              'detail': 'Pierson’s bands send 0-44 to a conditional use permit, 45-79 to '
                                        'overlays and 80-100 to a ban, and documentation, not the score, '
                                        'is the legal shield [Jeff Pierson — CmmE71lfGdw @ 00:06:08]'},
                             {'step': 3,
                              'title': 'Lock power ahead of the queue',
                              'action': 'Pair the site with district heating, on-site solar and storage to '
                                        'move up in power allocation and reduce grid stress.',
                              'detail': 'Bjornsgaard says smaller sites with surrounding solar can run '
                                        'off-grid, and his firm pairs 20 MW builds with district heating '
                                        'to get ahead in allocation [DCSMI — W92xU-lo1Gc @ 00:01:37]'},
                             {'step': 4,
                              'title': 'Engage before the vote, not after',
                              'action': 'Hold community engagement before the zoning committee hearing '
                                        'instead of relying on NDAs and stealth.',
                              'detail': 'Webber says companies are “very late” to engage communities, as '
                                        'in the shale era, and Olds residents report there was no '
                                        'consultation [PBS NewsHour — fkB8mt1DEVw @ 00:21:11]'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The sharpest split is over footprint. Mark Bjornsgaard argues that a $1T '
                              'ASI cluster would need 100 GW, about 20% of US electricity, and that the '
                              'way out is decentralization: smaller sites wrapped in on-site solar and '
                              "storage that can run off-grid and absorb waste power such as the UK's 6.5 "
                              "TWh of curtailed wind [W92xU-lo1Gc @ 00:00:32]. Bjornsgaard's firm builds "
                              '20 MW data centers paired with district heating because, in the UK and '
                              'Europe, a 50 MW district-heating project gets ahead of a 100 MW data center '
                              'in the power queue, and Joshua Feinberg adds that smaller sites draw less '
                              'community pushback [W92xU-lo1Gc @ 00:02:43]. Adam Gibson plays the opposite '
                              'hand: tier-1 greenfield is nearly impossible to get, so capital rotates '
                              'into tier-2 and tier-3 markets that still allow 100 MW greenfield builds or '
                              'easy brownfield retrofits, and with demand high and capacity scarce, Gibson '
                              'would put a few billion straight into new facilities [tWgTVIzYje8 @ '
                              "00:02:57]. The Latitude Media panel prices the gap: Span's 16-GPU Xfra node "
                              'is pitched at $3M/MW and six months to build versus $15M/MW and three to '
                              'five years for a 100 MW site, yet hyperscalers still prefer 50 MW behind '
                              '1-2 GW plants because it means one contract and protects the brand '
                              '[D7D1CPOoub4 @ 00:20:50].',
                              'On the regulatory weapon, organizers and planners pull in different '
                              'directions. Crystal Two Bulls counts moratoria as wins: Tulsa passed a '
                              'nine-month moratorium, the Seminole Nation passed one unanimously, and the '
                              'Muscogee blocked a resolution, all driven by town halls, tribal council '
                              'meetings, door knocking, petitions, and coalitions with agriculture, '
                              'ranchers and landowners [Ac0-fBK0LVQ @ 00:04:14]. Jeff Pierson calls the '
                              'reflex a binary trap: counties pick between general zoning and a total ban, '
                              'and the ban invites state preemption fights, takings claims and '
                              'equal-protection challenges, while potentially outlawing a future project '
                              "built by local farmers [CmmE71lfGdw @ 00:00:52]. Pierson's alternative is a "
                              'six-factor County Siting Posture Metric scoring infrastructure capacity, '
                              'agriculture, regulatory capacity, economic conditions, community alignment '
                              'and cumulative regional pressure; a score of 0-44 routes to a conditional '
                              'use permit, 45-79 to overlay districts, and only 80-100 to a ban, which '
                              'Pierson insists must be a last resort and never the first reaction '
                              '[CmmE71lfGdw @ 00:06:23]. Tammy Clark and Kristen Meghan run harder plays '
                              'instead: withhold tax subsidies even when a Google representative testifies '
                              "'we'll go somewhere else,' demand environmental impact studies, and recall "
                              'the officials who approve the deals [S_6FoEr75bs @ 00:25:34].',
                              "Cooling claims are the third fault line. Project Tango's developers "
                              'answered water, heat and noise objections with closed-loop cooling and '
                              'offsite water disposal, concrete buildings, a berm and trees, on a parcel '
                              'bordering the Arden community, an elementary school and sensitive '
                              'equestrian horses [iYCYPKhdqcY @ 00:02:48]. Kristen Meghan rejects the '
                              "label outright: 'There is no such thing as a closed loop system when it "
                              "comes to water use.' Glycol mixes are 50% water, the real alternatives, "
                              'dielectric fluid or mineral oil, cost more, and air cooling fails once '
                              'ambient air hits 100 degrees Fahrenheit [S_6FoEr75bs @ 00:43:31]. Michael '
                              'Webber applies a narrower test: the question is whether a closed loop is '
                              'filled once or draws water every day, and in Texas water is a more '
                              "sensitive issue than electricity; Webber still holds up Meta's "
                              "water-positive site near El Paso and Microsoft's air cooling near San "
                              'Antonio as working models [fkB8mt1DEVw @ 00:10:45]. Rodrigo Liang sidesteps '
                              'the argument in hardware: state-of-the-art racks draw 100-150 kW on the way '
                              'to 500 kW and need liquid cooling, while SambaNova racks run at 10 kW, '
                              'air-cooled, and drop into brownfield data centers that already exist '
                              'instead of new campuses [JvqqjgCu9mg @ 00:02:22].'],
               'table': {'caption': 'Competing playbooks on footprint, local control, cooling, ratepayers '
                                    'and rack design',
                         'headers': ['Fault Line', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Footprint strategy for winning scarce grid power',
                                   'Build 20 MW sites paired with district heating to jump ahead in the '
                                   'power queue',
                                   'Chase tier-2 and tier-3 markets that still allow 100 MW greenfield '
                                   'builds or brownfield retrofits',
                                   'Data Center Sales & Marketing Institute (DCSMI) ([W92xU-lo1Gc @ '
                                   '00:02:43]); Data Center Sales & Marketing Institute (DCSMI) '
                                   '([tWgTVIzYje8 @ 00:02:57])'],
                                  ['Distributed versus concentrated build cost and speed',
                                   'Span Xfra 16-GPU home nodes pitched at $3M/MW and six months to build',
                                   'Hyperscalers prefer 50 MW behind 1-2 GW plants for one contract and '
                                   'brand protection',
                                   'Latitude Media ([D7D1CPOoub4 @ 00:20:50]); Latitude Media '
                                   '([D7D1CPOoub4 @ 00:35:16])'],
                                  ['Local tool for stopping or shaping projects',
                                   'Moratoria and bans: Tulsa nine months, Seminole Nation unanimous, '
                                   'Muscogee resolution blocked',
                                   'CSPM score routes 0-44 to conditional use permits, 45-79 to overlays, '
                                   '80-100 to a ban',
                                   'Democracy Now! ([Ac0-fBK0LVQ @ 00:04:14]); Jeff Pierson ([CmmE71lfGdw '
                                   '@ 00:05:01])'],
                                  ['Whether closed-loop cooling claims hold up',
                                   'Project Tango pitches closed-loop cooling with offsite water disposal; '
                                   "eStruxture's 90 MW Calgary site runs closed loop",
                                   'Glycol is 50% water, so a closed loop for water use does not exist',
                                   'WPLG Local 10 ([iYCYPKhdqcY @ 00:02:48]); CBC News: The National '
                                   '([Rj_icscgo_Q @ 00:04:19]); Careers Over Beers Podcast ([S_6FoEr75bs @ '
                                   '00:43:31])'],
                                  ['How to test a water claim on site',
                                   'Ask whether the loop is filled once or draws water every single day',
                                   'Treat corporate closed-loop and water positivity claims as already '
                                   'dispelled by organizers',
                                   'PBS NewsHour ([fkB8mt1DEVw @ 00:10:45]); Democracy Now! ([Ac0-fBK0LVQ '
                                   '@ 00:09:00])'],
                                  ['Who pays for new generation and grid upgrades',
                                   'FPL says data center companies fund 100% of new generation under '
                                   'Senate Bill 484 protections',
                                   'Commissions approve upfront costs paid by ratepayers; Montana bills '
                                   'have almost doubled',
                                   'WPLG Local 10 ([iYCYPKhdqcY @ 00:03:36]); Democracy Now! ([Ac0-fBK0LVQ '
                                   '@ 00:11:07])'],
                                  ['Rack density and the need for new campuses',
                                   'State-of-the-art racks draw 100-150 kW heading toward 500 kW with '
                                   'liquid cooling',
                                   'SambaNova runs 10 kW air-cooled racks that fit existing brownfield '
                                   'data centers',
                                   'Founders Explain The World ([JvqqjgCu9mg @ 00:02:22])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The first trap fires at the kitchen table. Crystal Two Bulls reports that '
                              'Microsoft, Google, Apple, Meta and Amazon approach through subsidiaries and '
                              'native-owned energy companies with NDAs in hand, open with a solar pitch, '
                              'then pivot to a data center once the NDA is signed, leaving tribal '
                              'leadership accountable to the corporations instead of their own people '
                              '[Ac0-fBK0LVQ @ 00:03:27]. Tammy Clark and Kristen Meghan describe the same '
                              "script on farmland: leases pitched as 'temporary' and 'probably never going "
                              "to happen,' $10M offers to farmers, one family that refused $25M, and sites "
                              'picked specifically for weak zoning [S_6FoEr75bs @ 00:39:30]. The '
                              'transmission side is blunter. In Georgia, planned new lines jumped from 24 '
                              'miles in 2019 to 1,065 miles, roughly 80% of the added 10 GW is for data '
                              'centers, and Georgia Power offered Rachael Maszk $57,000 for half a '
                              'backyard while representatives raised eminent domain mid-negotiation; the '
                              "company's line is 'we use it less than 1 percent of the time' [e8QyJw6I-Bc "
                              '@ 00:03:50]. Doug Fergus lost a quarter of a backyard and roughly 400 trees '
                              'to a power line, held out for more than a year, then settled and paid down '
                              'half the mortgage with the proceeds [e8QyJw6I-Bc @ 00:04:16].',
                              'The second trap is believing the jobs-and-revenue story. Two Bulls puts '
                              'numbers on it: up to 1,500 construction jobs, mostly not local, over a '
                              'build phase of up to two years, then as few as three full-time jobs, as in '
                              'Rapid City, South Dakota, while Montana bills almost doubled and one person '
                              'living alone in a trailer received a $900 bill [Ac0-fBK0LVQ @ 00:11:53]. In '
                              'Alberta, residents of Olds, a town of about 10,000 facing a proposed '
                              "complex ten times Canada's largest, report no consultation at all, 68% of "
                              'Canadians would oppose a large data center near home, and no published '
                              'papers yet prove the economic benefits [Rj_icscgo_Q @ 00:03:14]. Michael '
                              "Webber names the timing problem directly: 'we feel the impacts today, the "
                              "benefits come later,' and companies are very late to engage communities, "
                              'repeating the shale era [fkB8mt1DEVw @ 00:17:16]. Project Tango shows what '
                              'that costs a developer: the zoning committee recommended denial, the '
                              'light-industrial argument failed, and the Palm Beach County Commission '
                              'killed the 1.5M sq ft expansion 5-1 even after FPL said data center '
                              'companies fund 100% of new generation, with a national protest day of '
                              'roughly 100 events already planned [iYCYPKhdqcY @ 00:05:09].',
                              'The third trap is physical and hits operators as hard as neighbors. The '
                              'Latitude Media panel warns that behind-the-meter builds can be invisible to '
                              'utilities, much like cannabis grow houses; an overload trips the building '
                              'rather than the feeder, and spiky inference loads create power-quality, '
                              'voltage and harmonics risk that the panel calls solvable, with storage as '
                              'the fix [D7D1CPOoub4 @ 00:24:22]. Utilization is the hidden economics '
                              'check: ProLogis customers run at 25% of their 5, 10 or 20 MW '
                              'interconnections, L3 chargers sit at roughly 15-30%, and EV tariffs block '
                              'added load unless the site opts into a C&I tariff, while office retrofits '
                              'stall on fire code, server weight, cooling and fiber [D7D1CPOoub4 @ '
                              '00:39:37]. Noise is where vendor specs break. Kristen Meghan says tonal and '
                              'low-frequency noise has to be measured in dBC or dBZ, not dBA; vendors '
                              "quote '55 dB at the fence' against an 85 dBA action level built on "
                              'eight-hour occupational exposure, while these sites run 24/7 [S_6FoEr75bs @ '
                              '00:11:30]. Two Bulls cites roughly 97 dB at sites and compares it with an '
                              "LRAD at about 140 dB: 'So, 97 to 140 is not a big jump' [Ac0-fBK0LVQ @ "
                              '00:09:45].'],
               'table': {'caption': 'Firsthand failure modes and the economics check practitioners '
                                    'attached to each',
                         'headers': ['Failure Mode',
                                     'What Practitioners Saw',
                                     'Economics Check',
                                     'Expert Source'],
                         'rows': [['NDA-first approach through subsidiaries and partners',
                                   'Solar pitch pivots to a hyperscale data center after the NDA is signed',
                                   'Leadership becomes accountable to corporations rather than to its own '
                                   'people',
                                   'Democracy Now! ([Ac0-fBK0LVQ @ 00:03:27])'],
                                  ['Eminent domain raised during easement negotiations',
                                   'Georgia Power offered $57,000 for half of a residential backyard',
                                   'Company says it uses eminent domain less than 1 percent of the time',
                                   'The New York Times ([e8QyJw6I-Bc @ 00:03:37])'],
                                  ['Jobs promise collapses after construction ends',
                                   'Up to 1,500 mostly non-local construction jobs over roughly two years',
                                   'As few as three permanent full-time jobs, as seen in Rapid City',
                                   'Democracy Now! ([OeYd0jErrF4 @ 00:01:42])'],
                                  ['Behind-the-meter load hidden from the local utility',
                                   'Builds can be invisible to utilities, much like cannabis grow houses',
                                   'Spiky inference loads risk voltage and harmonics problems; storage is '
                                   'the fix',
                                   'Latitude Media ([D7D1CPOoub4 @ 00:24:22])'],
                                  ['Interconnections sized far above actual usage',
                                   'ProLogis customers use about 25% of their 5, 10 or 20 MW '
                                   'interconnections',
                                   'L3 chargers sit at 15-30%; EV tariffs block load unless sites opt into '
                                   'C&I',
                                   'Latitude Media ([D7D1CPOoub4 @ 00:39:37])'],
                                  ['Fence-line noise specs measured on the wrong scale',
                                   'Vendors claim 55 dB at the fence using dBA weighting',
                                   'Tonal noise needs dBC or dBZ measurement; sites run 24/7, not eight '
                                   'hours',
                                   'Careers Over Beers Podcast ([S_6FoEr75bs @ 00:11:30])'],
                                  ['Layering AI onto legacy systems and stale data',
                                   'Bolting AI onto old systems and old data fails in production',
                                   'Make data and processes AI-ready first, then measure speed and cost '
                                   'per outcome',
                                   'Fierce Network TV ([ixyJ-cWKBEg @ 00:02:22])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Kill Switches Before Anyone Signs, Votes or Breaks Ground',
                           'body': 'Each gate below comes from a trap practitioners hit firsthand on land '
                                   'deals, noise specs, permits and county decisions.',
                           'items': ["Treat any NDA or 'temporary' lease offer as the opening move of a "
                                     'data-center deal, because organizers report solar pitches pivoting '
                                     'to hyperscale after signature [Democracy Now! — Ac0-fBK0LVQ @ '
                                     '00:03:27].',
                                     'Reject fence-line noise numbers quoted only in dBA and demand dBC or '
                                     'dBZ readings for continuous 24/7 operation [Careers Over Beers '
                                     'Podcast — S_6FoEr75bs @ 00:11:30].',
                                     'Pull diesel-generator air-permit filings once a month to catch '
                                     'projects before they surface publicly [Careers Over Beers Podcast — '
                                     'S_6FoEr75bs @ 01:16:47].',
                                     'Document every factor behind a siting posture, because '
                                     'documentation, not the score itself, is the legal shield [Jeff '
                                     'Pierson — CmmE71lfGdw @ 00:06:08].']}}],
 'pull_quote': "'A total ban is a legally valid civic tool, but it should strictly be deployed as a last "
               "resort when high standards fail, never as the first reaction.' Jeff Pierson (CmmE71lfGdw @ "
               '00:06:23).',
 'diagram_id': 'diag-08',
 'action_checklist': ['Score the county on the six CSPM factors (infrastructure, agriculture, regulatory '
                      'capacity, economics, community alignment, cumulative pressure) before choosing a '
                      'conditional use permit, overlay district or ban [Jeff Pierson — CmmE71lfGdw @ '
                      '00:01:39].',
                      'Organize through town halls, tribal council meetings, door knocking and petitions, '
                      'and build coalitions with agriculture, ranchers and landowners [Democracy Now! — '
                      'Ac0-fBK0LVQ @ 00:04:55].',
                      'Demand environmental impact studies and ask officials to send the documents '
                      'directly, the tactic credited with stopping a Michigan battery plant [Careers Over '
                      'Beers Podcast — S_6FoEr75bs @ 00:52:00].',
                      'Interrogate every cooling claim by asking whether the closed loop is filled once or '
                      'uses water daily [PBS NewsHour — fkB8mt1DEVw @ 00:10:45].',
                      'Pair sub-hyperscale sites of around 20 MW with district heating to move ahead of '
                      '100 MW data centers in the power queue [Data Center Sales & Marketing Institute '
                      '(DCSMI) — W92xU-lo1Gc @ 00:02:43].',
                      'Reduce exposure, choose regions deliberately, and keep data and applications '
                      'portable to avoid lock-in [Fierce Network TV — ixyJ-cWKBEg @ 00:04:03].'],
 'statutory_citations': [{'title': 'Democracy Now! — “Data Colonialism”: Native Communities Fight AI Data '
                                   'Centers on Indigenous Land [00:04:14]',
                          'url': 'https://www.youtube.com/watch?v=Ac0-fBK0LVQ&t=254s',
                          'relevance': 'Primary practitioner testimony on 103 to 160 proposed hyperscale '
                                       'sites on native lands, NDA-first approaches, and moratorium wins.'},
                         {'title': 'Jeff Pierson — Preparing your community for grid scale energy and '
                                   'hyperscale data centers [00:06:23]',
                          'url': 'https://www.youtube.com/watch?v=CmmE71lfGdw&t=383s',
                          'relevance': 'Primary practitioner testimony on the binary zoning trap, the CSPM '
                                       'score bands, and bans as a last resort.'},
                         {'title': 'Careers Over Beers Podcast — The AI Data Center Land Grab: Money, '
                                   'Secrecy, & Community Resistance | Kristen Meghan & Tammy Clark '
                                   '[00:43:31]',
                          'url': 'https://www.youtube.com/watch?v=S_6FoEr75bs&t=2611s',
                          'relevance': 'Primary practitioner testimony on closed-loop water claims, tonal '
                                       'noise measurement, and community counter-tactics.'},
                         {'title': 'Latitude Media — How Tiny Data Centers Could Solve AI’s Power Crunch '
                                   '[00:24:22]',
                          'url': 'https://www.youtube.com/watch?v=D7D1CPOoub4&t=1462s',
                          'relevance': 'Primary practitioner testimony on distributed data center '
                                       'economics, behind-the-meter visibility, and grid utilization.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'Ac0-fBK0LVQ',
                       'title': '“Data Colonialism”: Native Communities Fight AI Data Centers on '
                                'Indigenous Land',
                       'channel': 'Democracy Now!',
                       'author': 'Democracy Now!',
                       'text': "So, right now we're looking at about 103 to 160 proposed hyperscale data "
                               'centers on native lands.',
                       'tip': "So, right now we're looking at about 103 to 160 proposed hyperscale data "
                              'centers on native lands.',
                       'timestamp': 254,
                       'timestamp_seconds': 254,
                       'timestamp_label': '[00:04:14]',
                       'url': 'https://www.youtube.com/watch?v=Ac0-fBK0LVQ&t=254s',
                       'markdown': '[00:04:14](https://www.youtube.com/watch?v=Ac0-fBK0LVQ&t=254s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Ac0-fBK0LVQ',
                       'title': '“Data Colonialism”: Native Communities Fight AI Data Centers on '
                                'Indigenous Land',
                       'channel': 'Democracy Now!',
                       'author': 'Democracy Now!',
                       'text': 'So, 97 to 140 is not a big jump.',
                       'tip': 'So, 97 to 140 is not a big jump.',
                       'timestamp': 585,
                       'timestamp_seconds': 585,
                       'timestamp_label': '[00:09:45]',
                       'url': 'https://www.youtube.com/watch?v=Ac0-fBK0LVQ&t=585s',
                       'markdown': '[00:09:45](https://www.youtube.com/watch?v=Ac0-fBK0LVQ&t=585s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'tWgTVIzYje8',
                       'title': 'Decentralized Data Centers vs. Hyperscale vs. Edge',
                       'channel': 'Data Center Sales & Marketing Institute (DCSMI)',
                       'author': 'Data Center Sales & Marketing Institute (DCSMI)',
                       'text': 'Tier-2 markets still allow 100 MW greenfield builds or easy brownfield '
                               'retrofits that tier-1 markets cannot offer.',
                       'tip': 'Tier-2 markets still allow 100 MW greenfield builds or easy brownfield '
                              'retrofits that tier-1 markets cannot offer.',
                       'timestamp': 177,
                       'timestamp_seconds': 177,
                       'timestamp_label': '[00:02:57]',
                       'url': 'https://www.youtube.com/watch?v=tWgTVIzYje8&t=177s',
                       'markdown': '[00:02:57](https://www.youtube.com/watch?v=tWgTVIzYje8&t=177s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'W92xU-lo1Gc',
                       'title': 'Hyperscale vs. Decentralized Data Centers, Global Energy Capacity, and '
                                '$1T ASI Cluster',
                       'channel': 'Data Center Sales & Marketing Institute (DCSMI)',
                       'author': 'Data Center Sales & Marketing Institute (DCSMI)',
                       'text': 'We build 20 MW data centers paired with district heating so we get ahead '
                               'in power allocation.',
                       'tip': 'We build 20 MW data centers paired with district heating so we get ahead in '
                              'power allocation.',
                       'timestamp': 163,
                       'timestamp_seconds': 163,
                       'timestamp_label': '[00:02:43]',
                       'url': 'https://www.youtube.com/watch?v=W92xU-lo1Gc&t=163s',
                       'markdown': '[00:02:43](https://www.youtube.com/watch?v=W92xU-lo1Gc&t=163s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'iYCYPKhdqcY',
                       'title': 'Project Tango fuels debate over Florida’s first hyperscale AI data center',
                       'channel': 'WPLG Local 10',
                       'author': 'WPLG Local 10',
                       'text': "Project Tango's expansion master plan went before the Palm Beach County "
                               'Commission where it was just denied in a 5-1 vote.',
                       'tip': "Project Tango's expansion master plan went before the Palm Beach County "
                              'Commission where it was just denied in a 5-1 vote.',
                       'timestamp': 309,
                       'timestamp_seconds': 309,
                       'timestamp_label': '[00:05:09]',
                       'url': 'https://www.youtube.com/watch?v=iYCYPKhdqcY&t=309s',
                       'markdown': '[00:05:09](https://www.youtube.com/watch?v=iYCYPKhdqcY&t=309s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'tJYSzc7YkY0',
                       'title': 'The Big Data Center Water Problem',
                       'channel': 'Asianometry',
                       'author': 'Asianometry',
                       'text': 'Berkeley Lab estimates indirect water use from power generation at two to '
                               "three times a data center's direct water use.",
                       'tip': 'Berkeley Lab estimates indirect water use from power generation at two to '
                              "three times a data center's direct water use.",
                       'timestamp': 333,
                       'timestamp_seconds': 333,
                       'timestamp_label': '[00:05:33]',
                       'url': 'https://www.youtube.com/watch?v=tJYSzc7YkY0&t=333s',
                       'markdown': '[00:05:33](https://www.youtube.com/watch?v=tJYSzc7YkY0&t=333s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'OeYd0jErrF4',
                       'title': 'How huge AI data centers can harm local communities',
                       'channel': 'Democracy Now!',
                       'author': 'Democracy Now!',
                       'text': "In Montana, people's electricity bills have almost doubled.",
                       'tip': "In Montana, people's electricity bills have almost doubled.",
                       'timestamp': 88,
                       'timestamp_seconds': 88,
                       'timestamp_label': '[00:01:28]',
                       'url': 'https://www.youtube.com/watch?v=OeYd0jErrF4&t=88s',
                       'markdown': '[00:01:28](https://www.youtube.com/watch?v=OeYd0jErrF4&t=88s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'fkB8mt1DEVw',
                       'title': 'Why communities are revolting against data centers',
                       'channel': 'PBS NewsHour',
                       'author': 'PBS NewsHour',
                       'text': 'So we feel the impacts today, the benefits come later.',
                       'tip': 'So we feel the impacts today, the benefits come later.',
                       'timestamp': 1036,
                       'timestamp_seconds': 1036,
                       'timestamp_label': '[00:17:16]',
                       'url': 'https://www.youtube.com/watch?v=fkB8mt1DEVw&t=1036s',
                       'markdown': '[00:17:16](https://www.youtube.com/watch?v=fkB8mt1DEVw&t=1036s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'e8QyJw6I-Bc',
                       'title': 'When the Power Company Takes Your Land for a Data Center',
                       'channel': 'The New York Times',
                       'author': 'The New York Times',
                       'text': 'In fact, we use it less than 1 percent of the time.',
                       'tip': 'In fact, we use it less than 1 percent of the time.',
                       'timestamp': 230,
                       'timestamp_seconds': 230,
                       'timestamp_label': '[00:03:50]',
                       'url': 'https://www.youtube.com/watch?v=e8QyJw6I-Bc&t=230s',
                       'markdown': '[00:03:50](https://www.youtube.com/watch?v=e8QyJw6I-Bc&t=230s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'e8QyJw6I-Bc',
                       'title': 'When the Power Company Takes Your Land for a Data Center',
                       'channel': 'The New York Times',
                       'author': 'The New York Times',
                       'text': 'After more than a year, Doug Fergus settled and used the money to pay down '
                               'half the mortgage.',
                       'tip': 'After more than a year, Doug Fergus settled and used the money to pay down '
                              'half the mortgage.',
                       'timestamp': 256,
                       'timestamp_seconds': 256,
                       'timestamp_label': '[00:04:16]',
                       'url': 'https://www.youtube.com/watch?v=e8QyJw6I-Bc&t=256s',
                       'markdown': '[00:04:16](https://www.youtube.com/watch?v=e8QyJw6I-Bc&t=256s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'CmmE71lfGdw',
                       'title': 'Preparing your community for grid scale energy and hyperscale data '
                                'centers',
                       'channel': 'Jeff Pierson',
                       'author': 'Jeff Pierson',
                       'text': 'A total ban is a legally valid civic tool, but it should strictly be '
                               'deployed as a last resort when high standards fail, never as the first '
                               'reaction.',
                       'tip': 'A total ban is a legally valid civic tool, but it should strictly be '
                              'deployed as a last resort when high standards fail, never as the first '
                              'reaction.',
                       'timestamp': 383,
                       'timestamp_seconds': 383,
                       'timestamp_label': '[00:06:23]',
                       'url': 'https://www.youtube.com/watch?v=CmmE71lfGdw&t=383s',
                       'markdown': '[00:06:23](https://www.youtube.com/watch?v=CmmE71lfGdw&t=383s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'JvqqjgCu9mg',
                       'title': 'AI Without New Data Centers?',
                       'channel': 'Founders Explain The World',
                       'author': 'Founders Explain The World',
                       'text': 'SambaNova racks run at 10 kW, air-cooled, so they fit into existing '
                               'brownfield data centers.',
                       'tip': 'SambaNova racks run at 10 kW, air-cooled, so they fit into existing '
                              'brownfield data centers.',
                       'timestamp': 142,
                       'timestamp_seconds': 142,
                       'timestamp_label': '[00:02:22]',
                       'url': 'https://www.youtube.com/watch?v=JvqqjgCu9mg&t=142s',
                       'markdown': '[00:02:22](https://www.youtube.com/watch?v=JvqqjgCu9mg&t=142s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Rj_icscgo_Q',
                       'title': 'A hyperscale AI data centre boom is coming',
                       'channel': 'CBC News: The National',
                       'author': 'CBC News: The National',
                       'text': 'Residents of Olds say there was no consultation, and 68 percent of '
                               'Canadians would oppose a large data centre near their home.',
                       'tip': 'Residents of Olds say there was no consultation, and 68 percent of '
                              'Canadians would oppose a large data centre near their home.',
                       'timestamp': 194,
                       'timestamp_seconds': 194,
                       'timestamp_label': '[00:03:14]',
                       'url': 'https://www.youtube.com/watch?v=Rj_icscgo_Q&t=194s',
                       'markdown': '[00:03:14](https://www.youtube.com/watch?v=Rj_icscgo_Q&t=194s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'D7D1CPOoub4',
                       'title': 'How Tiny Data Centers Could Solve AI’s Power Crunch',
                       'channel': 'Latitude Media',
                       'author': 'Latitude Media',
                       'text': "So they're not connected at transmission voltage. They're being connected "
                               'on distribution.',
                       'tip': "So they're not connected at transmission voltage. They're being connected "
                              'on distribution.',
                       'timestamp': 1624,
                       'timestamp_seconds': 1624,
                       'timestamp_label': '[00:27:04]',
                       'url': 'https://www.youtube.com/watch?v=D7D1CPOoub4&t=1624s',
                       'markdown': '[00:27:04](https://www.youtube.com/watch?v=D7D1CPOoub4&t=1624s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'D7D1CPOoub4',
                       'title': 'How Tiny Data Centers Could Solve AI’s Power Crunch',
                       'channel': 'Latitude Media',
                       'author': 'Latitude Media',
                       'text': 'Behind-the-meter builds can be invisible to the utility, the same way '
                               'cannabis grow houses were.',
                       'tip': 'Behind-the-meter builds can be invisible to the utility, the same way '
                              'cannabis grow houses were.',
                       'timestamp': 1462,
                       'timestamp_seconds': 1462,
                       'timestamp_label': '[00:24:22]',
                       'url': 'https://www.youtube.com/watch?v=D7D1CPOoub4&t=1462s',
                       'markdown': '[00:24:22](https://www.youtube.com/watch?v=D7D1CPOoub4&t=1462s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ixyJ-cWKBEg',
                       'title': 'Akamai on Why AI Needs More Than Hyperscale Data Centers',
                       'channel': 'Fierce Network TV',
                       'author': 'Fierce Network TV',
                       'text': 'They need to make sure that their data is portable and that their '
                               "application's portable so they're not locked in and their data is freely "
                               'movable.',
                       'tip': 'They need to make sure that their data is portable and that their '
                              "application's portable so they're not locked in and their data is freely "
                              'movable.',
                       'timestamp': 258,
                       'timestamp_seconds': 258,
                       'timestamp_label': '[00:04:18]',
                       'url': 'https://www.youtube.com/watch?v=ixyJ-cWKBEg&t=258s',
                       'markdown': '[00:04:18](https://www.youtube.com/watch?v=ixyJ-cWKBEg&t=258s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'S_6FoEr75bs',
                       'title': 'The AI Data Center Land Grab: Money, Secrecy, & Community Resistance | '
                                'Kristen Meghan & Tammy Clark',
                       'channel': 'Careers Over Beers Podcast',
                       'author': 'Careers Over Beers Podcast',
                       'text': 'There is no such thing as a closed loop system when it comes to water use.',
                       'tip': 'There is no such thing as a closed loop system when it comes to water use.',
                       'timestamp': 2611,
                       'timestamp_seconds': 2611,
                       'timestamp_label': '[00:43:31]',
                       'url': 'https://www.youtube.com/watch?v=S_6FoEr75bs&t=2611s',
                       'markdown': '[00:43:31](https://www.youtube.com/watch?v=S_6FoEr75bs&t=2611s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'S_6FoEr75bs',
                       'title': 'The AI Data Center Land Grab: Money, Secrecy, & Community Resistance | '
                                'Kristen Meghan & Tammy Clark',
                       'channel': 'Careers Over Beers Podcast',
                       'author': 'Careers Over Beers Podcast',
                       'text': 'So keep once a month, go on there and look.',
                       'tip': 'So keep once a month, go on there and look.',
                       'timestamp': 4607,
                       'timestamp_seconds': 4607,
                       'timestamp_label': '[01:16:47]',
                       'url': 'https://www.youtube.com/watch?v=S_6FoEr75bs&t=4607s',
                       'markdown': '[01:16:47](https://www.youtube.com/watch?v=S_6FoEr75bs&t=4607s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'}]}
