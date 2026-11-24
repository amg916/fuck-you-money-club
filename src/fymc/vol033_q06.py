from __future__ import annotations

CHAPTER_6 = {'id': 'Q6',
 'chapter_id': 'Q6',
 'chapter_number': 6,
 'question_number': 6,
 'slug': 'scaling-automating-stress-testing-arbitrage',
 'question_prompt': 'How do arbitrage operators automate and scale their portfolios, and where does the '
                    'master-lease model break down?',
 'kicker': 'Q6 / THE BIG MONEY PLAYBOOKS',
 'title': 'Scaling, Automating, and Stress-Testing Arbitrage',
 'subtitle': 'Scaling to 60, 76, and 300+ units, automation stacks, remote management, teams and org '
             'charts, a Mexico City case study, master-lease failure modes, and why some operators quit '
             'arbitrage for co-hosting',
 'layout_template': 'step_by_step_blueprint',
 'reading_time_minutes': 15,
 'executive_summary': 'Operators who scaled past 20, 60, even 450 doors agree on the same spine: pitch '
                      'landlords as corporate housing, underwrite at two to three times rent against 24 '
                      'months of AirDNA data, and hire a virtual assistant the day the lease is signed. '
                      'Richie Matthews went from 18 to 35 units in six months after delegating, running an '
                      '$80-a-month Hospitable-plus-pricing stack and 900 VA protocols. Colin Wright '
                      'refuses deals without free rent and negotiates one-to-two-month escape clauses. '
                      'Humza Zafar peaked at 450 units, cleared his 0% APR cards before they reset, and '
                      'moved to A-class because fixed costs are identical across classes. The fault lines: '
                      'Wright skips sublease addendums while Brian Fontenot refuses to do anything under '
                      'the radar, and Milan Sánchez Stiepovic and Jeremy Werden argue co-hosting carries '
                      'far lower risk than holding leases.',
 'key_metrics': [{'label': 'Delegated Scaling Run',
                  'metric': 'Delegated Scaling Run',
                  'value': '18 to 35 units in 6 months',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Unit growth after Matthews built his system in March 2021 and delegated '
                             'operations to VAs',
                  'source': 'Richie Matthews ([VtVf0h80q0w @ 00:04:01])'},
                 {'label': 'Minimum Net Per Property',
                  'metric': 'Minimum Net Per Property',
                  'value': '$2,000 to $2,500 per month',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Walk-away threshold; any deal netting less gets dropped or renegotiated, '
                             'with an average of 6 units per building',
                  'source': 'Richie Matthews ([VtVf0h80q0w @ 00:06:44])'},
                 {'label': 'Peak Portfolio Size',
                  'metric': 'Peak Portfolio Size',
                  'value': '450 units, cut back to 300',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Zafar trimmed after economy units died to competition and shifted to '
                             'A-class, where fixed costs leave more margin',
                  'source': 'Humza Zafar ([1D3J3ID1ZZM @ 00:06:25])'},
                 {'label': 'Automation Stack Cost',
                  'metric': 'Automation Stack Cost',
                  'value': '$80 per month (Hospitable $40 + dynamic pricing $40)',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Monthly software cost Matthews quotes for running messaging, calendar sync '
                             'and pricing per operation',
                  'source': 'Richie Matthews ([O4cBKKUBS64 @ 00:13:29])'}],
 'sections': [{'heading': 'Section 1: The Practitioner Consensus',
               'paragraphs': ['The operators who scaled fastest never walked into a leasing office asking '
                              'about Airbnb. Brian Fontenot built a list of buildings that already '
                              'accepted corporate housing, targeted large Class A complexes through a '
                              "realtor, and pitched himself to the leasing professional as a 'corporate "
                              "housing provider' until a corporate lease was verified [D63ppvOFpvk @ "
                              '00:10:26]. Richie Matthews runs the same filter on Class B stock 10 to 15 '
                              "years old: the first question is 'do you allow corporate leasing?' and "
                              'nothing else happens until the answer is yes [O4cBKKUBS64 @ 00:09:25]. In '
                              "Mexico City, Nathan Carillo says the words 'sublet' or 'Airbnb' get him "
                              "hung up on immediately, so he opens with 'corporate rental, short or long "
                              "term' and works 20 inquiries and three to four appointments a day "
                              "[z5rgPmF_Dm4 @ 00:13:35]. Farhan Abbasi says landlords 'didn't like "
                              "hearing' his other framing but 'loved hearing guaranteed,' and his best "
                              'target is an owner who has carried a unit vacant for more than a month, '
                              'because debt service on an empty unit hurts [Y2Nj2IYzw-Q @ 00:18:41]. The '
                              'baseline prerequisite across all four: a landlord who sees a guaranteed, '
                              'professional tenant that kills vacancy, not a side hustle trying to slip a '
                              'listing past the lease.',
                              'Every scaled operator underwrites the spread before touching furniture, and '
                              'they converge on a hard multiple. Richie Matthews targets markets where '
                              'gross revenue runs two to three times rent, checked in AirDNA against 24 to '
                              '36 months of history, citing a Nashville 2/2 that grosses $7,500 against '
                              '$2,500 rent [VtVf0h80q0w @ 00:07:50]. His absolute floor is a 2.0 multiple '
                              'verified on Rentometer, with rent at no more than half of revenue and '
                              'ideally a third; if 24 months of month-over-month data does not exist for '
                              'the market, he walks [O4cBKKUBS64 @ 00:03:08]. Quentin West works the math '
                              'backwards: a $2,000 minimum profit plus $2,000 rent, $600 utilities and '
                              '$500 cleaning means the unit must clear $5,100 a month, and AirDNA has to '
                              'show more than $60,000 a year before anyone checks Zillow [GFTAQzCp4aM @ '
                              '00:18:27]. Colin Wright runs AirDNA, BNB Calc and Zillow rents together but '
                              'warns the data is scraped and not 100% accurate; his own units outperform '
                              'it, and he tells operators to balance occupancy against rate rather than '
                              'chase a full calendar [NSyEBVGX02o @ 00:11:43]. The shared rule: the spread '
                              'clears a written floor before a lease ever reaches signature, and nobody '
                              'here signs on a hunch.',
                              'The third point of agreement is that scale comes from systems and people, '
                              'not from the founder answering messages. Matthews says step one is hiring a '
                              'virtual assistant the day the lease is signed, and after building his '
                              'system in March 2021 and delegating, he went from 18 to 35 units in six '
                              'months [VtVf0h80q0w @ 00:04:17]. Abbasi ran his early units off an Excel '
                              'and Google Sheets master file that produced date errors, and the business '
                              'only became scalable once he paired a channel manager with a VA '
                              '[Y2Nj2IYzw-Q @ 00:14:44]. Fontenot mapped the staffing curve by unit count: '
                              "Guesty's communication service covered four to five units but still left "
                              'him with 2 a.m. lockout calls, he hired an admin and communications person '
                              'at five to seven units, grew that team to three or four people at 10 to 15 '
                              'units, and added a property manager at 20 [D63ppvOFpvk @ 00:22:08]. Humza '
                              'Zafar, running hundreds of doors, now works about three hours a week '
                              'because a COO in Philadelphia runs operations and Philippines-based VAs '
                              "handle customer service six days a week [1D3J3ID1ZZM @ 00:18:39]. Abbasi's "
                              'minimum stack is calendar sync, dynamic pricing and outside help once a '
                              'portfolio passes four or five units.'],
               'table': {'caption': 'Where scaled arbitrage operators agree before the first lease is '
                                    'signed',
                         'headers': ['Consensus Point',
                                     'What Practitioners Do',
                                     'Why It Scales',
                                     'Expert Source'],
                         'rows': [['Pitch the unit as corporate housing, never as Airbnb',
                                   'Lead with corporate housing provider language to Class A leasing '
                                   'professionals',
                                   'Leasing teams verify a corporate lease instead of rejecting a '
                                   'short-term host',
                                   'Short Term Rental Secrets ([D63ppvOFpvk @ 00:10:26])'],
                                  ['Screen every landlord for corporate leasing approval first',
                                   'Ask whether the building allows corporate leasing before any tour or '
                                   'call',
                                   'Kills dead-end deals early and keeps acquisition running by automated '
                                   'message',
                                   'Richie Matthews ([O4cBKKUBS64 @ 00:09:25])'],
                                  ['Target owners already bleeding from vacancy at the unit level',
                                   'Approach owners who have carried a unit vacant for more than a month',
                                   'Debt service on an empty unit turns guaranteed rent into a win-win',
                                   'Short Term Sage - Airbnb, Vacation Rental Host ([Y2Nj2IYzw-Q @ '
                                   '00:18:41])'],
                                  ['Favor mom-and-pop owners over big complexes for longevity',
                                   'Work rent.com, apartments.com, networking events and '
                                   'investor-landlords for small owners',
                                   'Big complexes deny the model while small owners keep you in the '
                                   'building',
                                   'Alex Sabio ([52k99Zbi6fk @ 00:03:56])'],
                                  ['Underwrite every market to a two-to-three-times rent multiple',
                                   'Pull AirDNA with 24 to 36 months of revenue history per market',
                                   'A Nashville 2/2 grossing $7,500 against $2,500 rent is a 3x market',
                                   'Richie Matthews ([VtVf0h80q0w @ 00:07:50])'],
                                  ['Hire help before the portfolio breaks the founder',
                                   'Pair a channel manager with a VA once past four or five units',
                                   'Spreadsheet master files produced date errors until tech and help '
                                   'arrived',
                                   'Short Term Sage - Airbnb, Vacation Rental Host ([Y2Nj2IYzw-Q @ '
                                   '00:14:44])'],
                                  ['Move up to A-class where fixed costs stay identical',
                                   'Shift from $800 economy units to A-class apartments and 2BR-plus '
                                   'layouts',
                                   'Internet and cleaning cost the same, leaving more meat on the bone',
                                   'Humza Zafar ([1D3J3ID1ZZM @ 00:06:25])']]}},
              {'heading': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ["The unit math the practitioners publish is specific. Rafa Loza's 2BR "
                              'conversion cost a $1,000 deposit plus $2,950 rent, so $3,950 to get the '
                              'keys, then roughly $15,000 for beds, TVs, wallpaper and locks; he averages '
                              'at least $1,500 a month in profit over 12 months, swinging from $400 to '
                              '$4,000 or $5,000, and pays the unit back in year one [52k99Zbi6fk @ '
                              '00:02:28]. Colin Wright tells newcomers to start with a studio or '
                              'one-bedroom at $7,000 to $10,000 to furnish and $10,000 to $15,000 all-in, '
                              'netting $10,000 to $20,000 a year, while houses renting at $5,000 to '
                              '$10,000 can throw a negative month [NSyEBVGX02o @ 00:13:01]. Short Term '
                              "Dojo's monthly model runs $4,500 revenue against a $1,500 lease, $75 "
                              'supplies, $75 STR-specific insurance, a $50 tech stack plus utilities, '
                              'totaling $2,000 in costs and netting $2,500, versus roughly $500 as a '
                              'long-term rental [tfwUVSMpB2c @ 00:05:11]. At the top end, Humza Zafar '
                              'reports $2,600 to $2,800 rent producing $6,000 to $7,000 a month, $4,000 to '
                              '$5,000 rent producing $8,000 to $11,000, and an $8,000-rent mansion '
                              'furnished for $50,000 grossing $15,000 to $20,000 a month [1D3J3ID1ZZM @ '
                              "00:07:23]. Zafar's reasoning is that fixed costs like internet and cleaning "
                              'are identical across classes, so bigger units leave more margin per door.',
                              "The automation layer is nearly identical across operators. Rafael Loza's "
                              'top PMS is Hospitable, which syncs calendars across Airbnb, VRBO, '
                              'Booking.com and a direct site to stop same-day double bookings and feeds '
                              "PriceLabs; he tells hosts to stay away from Airbnb's native pricing tool "
                              "because it 'will underprice everything' [J8lQc66Jf6c @ 00:01:07]. Matthews "
                              'prices his stack at $40 for Hospitable plus $40 for dynamic pricing, $80 a '
                              'month, and lists every unit on 20 platforms the day it goes live, including '
                              'Booking, Expedia, Furnished Finder and ALE channels, while 70% of amateurs '
                              'use two or fewer [O4cBKKUBS64 @ 00:05:44]. Fontenot runs Guesty, Hey Market '
                              'for SMS, Zendesk and Slack, uses SiteMinder to reach Expedia, HomeAway, '
                              'corporate-housing and travel-nurse portals, and screens every guest through '
                              "Autohost; when COVID left Wheelhouse's event data stale, he switched to "
                              "PriceClaro's manual pricing service and saw a '20 to 30' revenue increase "
                              '[D63ppvOFpvk @ 00:24:02]. Colin Wright layers Ring doorbells, smart locks '
                              'with a unique code per guest and per cleaner, and Minut sensors that log '
                              'decibels, smoking and crowds as claim evidence, plus PriceLabs managed by a '
                              'revenue manager at $50 to $60 per listing [NSyEBVGX02o @ 00:30:24]. Wright '
                              'adds that setting the base price correctly is critical.',
                              'Financing and labor are where the scaled operators squeeze the most. Zafar '
                              'funded his run to roughly 100 units with 0% APR business credit cards for '
                              'furniture plus month-free rent concessions, then paused at 200 units for a '
                              'few months to clear the cards before the 15-month promotional window closed '
                              '[1D3J3ID1ZZM @ 00:03:45]. Wright says he gets free rent on every deal '
                              'because he will not take one without it, offers landlords package terms '
                              "like '10 units, here's my terms,' and negotiates an escape clause usually "
                              'costing one to two months of rent, which he offsets by asking the next '
                              'property for a two-month concession [NSyEBVGX02o @ 00:58:03]. Wright '
                              "sources his own VAs on onlinejobs.ph at $3 to $5 an hour. Matthews' first "
                              'unit in February 2020 cost $4,800 total, $4,500 of furniture and a $300 '
                              'deposit, with four weeks of free rent, and his VAs train for five days, run '
                              'autonomously on day six, and work from 900 protocols with a six-minute '
                              'maximum response time split-tested across 10,000 reservations; they never '
                              'touch refunds or safety [O4cBKKUBS64 @ 00:16:04]. Quentin West pushes '
                              'leverage further: one credit check across more than 45 signed leases, an '
                              'LLC, and ten hours of script practice before calling landlords [GFTAQzCp4aM '
                              '@ 00:41:26].'],
               'table': {'caption': 'Exact tools, costs and unit numbers the operators run on',
                         'headers': ['Mechanic',
                                     'Exact Number or Tool',
                                     'Operator Detail',
                                     'Expert Source'],
                         'rows': [['Startup cash required to open one arbitrage unit',
                                   '$1,000 deposit plus $2,950 rent, then about $15,000 furnishing',
                                   'Profit averages at least $1,500 monthly with payback inside year one',
                                   'Alex Sabio ([52k99Zbi6fk @ 00:02:28])'],
                                  ['PMS and calendar sync across every booking channel',
                                   'Hospitable syncing Airbnb, VRBO, Booking.com and a direct booking site',
                                   'Prevents same-day double bookings and feeds PriceLabs dynamic pricing '
                                   'daily',
                                   'Rafael Loza ([J8lQc66Jf6c @ 00:00:12])'],
                                  ['Monthly software cost for messaging and pricing automation',
                                   'Hospitable at $40 plus dynamic pricing at $40 equals $80',
                                   'One booking per month pays for a $700 to $800 monthly VA',
                                   'Richie Matthews ([O4cBKKUBS64 @ 00:13:29])'],
                                  ['Guest screening and corporate channel distribution at scale',
                                   'Autohost checks ID, sex-offender registry and watchlist within 12 '
                                   'hours',
                                   'Property managers get portal access while SiteMinder reaches '
                                   'travel-nurse portals',
                                   'Short Term Rental Secrets ([D63ppvOFpvk @ 00:15:01])'],
                                  ['Furniture rental instead of buying for faster launches',
                                   'Court Furniture Rent at $550 to $750 monthly with setup included',
                                   'Walk away from deals netting under $2,000 to $2,500 per property',
                                   'Richie Matthews ([VtVf0h80q0w @ 00:06:32])'],
                                  ['In-unit security hardware that doubles as claims evidence',
                                   'Ring doorbell, per-guest smart-lock codes and Minut noise and smoke '
                                   'sensors',
                                   'Decibel, smoking and crowd logs back up damage claims against guests',
                                   'Official Success Formula ([NSyEBVGX02o @ 00:30:24])'],
                                  ['Cleaning team structure that holds quality across units',
                                   'One lead manages about eight cleaners across about 22 units',
                                   'Cleaners are first contact reporting damage, smoking and excess pets',
                                   'Rafael Loza ([J8lQc66Jf6c @ 00:03:43])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Acquisition and Revenue Edges Scaled Operators Actually Use',
                           'body': 'Four moves the operators credit for landing doors and squeezing more '
                                   'revenue out of each one, pulled from their own deal flow and booking '
                                   'data.',
                           'items': ['Drive your neighborhood for buildings under construction and ask the '
                                     'contractors on site to connect you directly with the owner [Alex '
                                     'Sabio — 52k99Zbi6fk @ 00:07:06]',
                                     'Only accept VRBO or Booking.com reservations when they catch a '
                                     "premium over Airbnb, since Airbnb's host fee jumped from 3% to 15% "
                                     '[Official Success Formula — NSyEBVGX02o @ 00:38:14]',
                                     'Offer your units to the complex as guest suites and overnight model '
                                     'units for prospective long-term tenants to bond with the leasing '
                                     'office [Short Term Rental Secrets — D63ppvOFpvk @ 00:11:13]',
                                     "List during the landlord's two-week setup grace period: one Mexico "
                                     'City listing booked three stays within 30 minutes, at a cost of '
                                     'about $200 in photos [Short Term Sage - Airbnb, Vacation Rental Host '
                                     '— z5rgPmF_Dm4 @ 00:29:48]']},
               'sop_steps': [{'step': 1,
                              'title': 'Underwrite the Market',
                              'action': 'Pull 24 months of AirDNA data and confirm at least a 2x rent '
                                        'multiple',
                              'detail': 'Spend about 20 minutes each morning pulling month-over-month '
                                        'AirDNA data and Rentometer rents; walk if 24 months of data is '
                                        'missing or the multiple falls under 2.0, then verify legality for '
                                        'the market [Richie Matthews — O4cBKKUBS64 @ 00:10:19]'},
                             {'step': 2,
                              'title': 'Negotiate the Lease Terms',
                              'action': 'Demand free rent and an escape clause before signing',
                              'detail': 'Refuse deals without free rent, negotiate an escape clause of one '
                                        "to two months' rent, and push package terms of multiple units "
                                        'with lower or no security deposits [Official Success Formula — '
                                        'NSyEBVGX02o @ 00:58:03]'},
                             {'step': 3,
                              'title': 'Install the Stack and the VA',
                              'action': 'Hire a VA on lease day and load Hospitable, PriceLabs and canned '
                                        'messages',
                              'detail': 'Hire the VA the day the lease is signed at $4 to $4.50 an hour '
                                        'paid through Wise every other week, list on all platforms, and '
                                        'load roughly 900 canned messages into Hospitable with PriceLabs '
                                        'running pricing [Richie Matthews — VtVf0h80q0w @ 00:05:24]'},
                             {'step': 4,
                              'title': 'Furnish, Shoot and Launch',
                              'action': 'Run a floor-plan-to-install pipeline and book an STR-specific '
                                        'photographer',
                              'detail': 'Move from floor plan to vision board to storage locker to '
                                        'install, budget $8,000 to $10,000 turnkey, give every unit a '
                                        'desk, sleeper sofa and air mattress, and hire an STR-specific '
                                        'photographer shooting HDR brackets [Official Success Formula — '
                                        'NSyEBVGX02o @ 00:27:07]'}]},
              {'heading': 'Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The sharpest split is whether arbitrage should be the scaling engine at '
                              'all. Milan Sánchez Stiepovic runs Happy Host at 163 units and says 98% of '
                              "them now sit under management, calling co-hosting '100% superior' after "
                              'trying both models, yet he still tells beginners to do their first unit as '
                              'arbitrage [nPFkgk7QMfA @ 00:18:20]. Jeremy Werden quit arbitrage outright: '
                              'a $2,500-rent unit grossing $5,000 against $1,000 in costs nets $1,500, but '
                              'a slide to $3,000 revenue leaves the operator $500 short, while a co-host '
                              'earning 20% of that same $5,000 pockets $1,000 a month with minimal '
                              'overhead and no lease exposure [kXJgiO6RYaU @ 00:02:07]. Humza Zafar argues '
                              'the opposite for the US market, rejecting 80/20 revenue share because a '
                              'roughly $15K startup with rent concessions keeps the master lease worth '
                              'carrying; he concedes only that Dubai, with $40–50K paid upfront, changes '
                              'the math [1D3J3ID1ZZM @ 00:44:45]. John Bell refuses to pick a side at all. '
                              'At roughly 50 units split about evenly between arbitrage and co-hosting, '
                              'co-hosting income covers his leases through slow seasons and COVID, and his '
                              "rule is that 'it always bleeds into the next method so you're going to want "
                              "a good blend' [scmRAbKvEPk @ 00:06:14].",
                              'Pace is the second fault line. Richie Matthews teaches speed: he copied the '
                              'Sonder playbook, went to 18 properties in 12 months and 46 in two years, '
                              'and frames his VA-plus-protocol system as the thing that makes that pace '
                              "possible because 'you can't scale chaos' [O4cBKKUBS64 @ 00:07:11]. The "
                              'CoLiving Insider prescribes the brake pedal instead: hold every new house '
                              'at break-even for 90 days before opening the next, put each house in its '
                              "own LLC 'so one bad lease cannot take down the rest,' and never pay above "
                              'market just to win a deal, pointing to Quarters raising $300M and still '
                              'going bankrupt as a business that grew faster than its margins could '
                              'support [zj0PhRK1anA @ 00:07:57]. Humza Zafar sits between them. He scaled '
                              'from 5 to roughly 100 units on 0% APR cards and free-month concessions, but '
                              'deliberately paused at 200 units for a few months to clear the cards before '
                              'the 15-month promotional window closed [1D3J3ID1ZZM @ 00:13:20]. Rafa Loza '
                              'looks back and says he should have capped out at about $30K a month in cash '
                              'flow and bought property, after a $2.7–3M revenue year left him paying $86K '
                              'in taxes with nothing to depreciate [52k99Zbi6fk @ 00:07:31].',
                              'How openly to run the model, and whose name goes on the paper, splits the '
                              'room just as hard. Brian Fontenot refuses to sign leases in a personal '
                              'name, routes everything through a business entity, issues guests a '
                              'short-term occupancy permit so the arrangement is not a sublet, and insists '
                              "on doing nothing 'under the radar,' even giving property managers portal "
                              'access to his Autohost guest screening [D63ppvOFpvk @ 00:13:28]. Colin '
                              'Wright runs looser: he skips the sublease addendum, leans on verbal or '
                              'written permission, says an LLC is not required, keeps some leases in his '
                              'own name, and openly books the cost, roughly 15 units lost to new owners '
                              'over three years [NSyEBVGX02o @ 00:23:11]. Nathan Carillo in Mexico City '
                              "hides the model's name entirely, never saying 'sublet' or 'Airbnb' on a "
                              "first call because owners hang up, and pitches a 'corporate rental, "
                              "short/long term' backed by a professional video, landlord testimonials, a "
                              'presentation and a website [z5rgPmF_Dm4 @ 00:13:35]. Quentin West, on Beau '
                              "Eckstein's show, takes the entity route to its scaling conclusion: one "
                              'credit check across 45+ signed leases, an LLC, and ten hours of script '
                              'practice before working landlords [GFTAQzCp4aM @ 00:41:26].'],
               'table': {'caption': 'Side-by-side playbooks where scaled arbitrage operators split',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Arbitrage versus co-hosting as the core scaling engine',
                                   'Humza Zafar rejects US 80/20 revenue share because startup runs about '
                                   '$15K with concessions',
                                   'Milan keeps 98% of 163 units under management and calls co-hosting '
                                   'superior',
                                   'Humza Zafar ([1D3J3ID1ZZM @ 00:44:45]); Milan Sánchez Stiepovic '
                                   '([nPFkgk7QMfA @ 00:18:20])'],
                                  ['Single-family homes versus apartments and luxury houses',
                                   'Richie Matthews tells operators facing single family homes to simply '
                                   'run away',
                                   'Humza runs an $8K-rent mansion grossing $15–20K per month after a $50K '
                                   'furnish',
                                   'Richie Matthews ([O4cBKKUBS64 @ 00:01:28]); Humza Zafar ([1D3J3ID1ZZM '
                                   '@ 00:07:23])'],
                                  ['Starter unit class: small economy units versus A-class larger units',
                                   'Colin Wright says start with a studio or one-bedroom at $10–15K all-in',
                                   'Humza dropped $800 Dallas economy units for A-class after competition '
                                   'killed that tier',
                                   'Official Success Formula ([NSyEBVGX02o @ 00:13:01]); Humza Zafar '
                                   '([1D3J3ID1ZZM @ 00:04:57])'],
                                  ['Growth pace: speed-scaling versus one house at a time',
                                   'Richie Matthews copied Sonder and hit 18 properties in 12 months, 46 '
                                   'in two years',
                                   'Hold each new house 90 days at break-even before opening the next one',
                                   'Richie Matthews ([O4cBKKUBS64 @ 00:00:20]); The CoLiving Insider '
                                   '([zj0PhRK1anA @ 00:07:57])'],
                                  ['Lease paperwork: entity-signed transparency versus handshake '
                                   'permission',
                                   'Fontenot signs only through a business entity and does nothing under '
                                   'the radar',
                                   'Colin Wright skips the sublease addendum and lost about 15 units to '
                                   'new owners',
                                   'Short Term Rental Secrets ([D63ppvOFpvk @ 00:13:28]); Official Success '
                                   'Formula ([NSyEBVGX02o @ 00:23:11])'],
                                  ['Virtual assistant sourcing: offshore hourly versus local hire',
                                   'Richie Matthews scales on offshore VAs paid $4 to $4.50 an hour',
                                   'Quentin West prefers working with a local virtual assistant instead of '
                                   'offshore help',
                                   'Richie Matthews ([O4cBKKUBS64 @ 00:06:55]); Beau Eckstein, Business '
                                   'Ownership Coach ([GFTAQzCp4aM @ 00:17:20])'],
                                  ['What co-hosting actually pays per door if you switch models',
                                   "John Bell's segment puts the co-hosting fee at 15–20% of revenue",
                                   'Milan charges about 20% and up to 35%, calculated including the '
                                   'cleaning fee',
                                   'Short Term Sage - Airbnb, Vacation Rental Host ([scmRAbKvEPk @ '
                                   '00:04:49]); Milan Sánchez Stiepovic ([nPFkgk7QMfA @ 00:10:48])']]}},
              {'heading': 'Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The landlord exit is the failure every operator eventually meets. Rafa Loza '
                              "states it bluntly: 'you will only be a business as long as the landlord or "
                              "Property Management allows you to be in the building,' and he steers "
                              'operators toward mom-and-pop owners because big complexes deny you '
                              '[52k99Zbi6fk @ 00:03:34]. He lived it, growing from zero to 14 units in '
                              'nine months and reaching about 28, before COVID and a building sale cut him '
                              'back to three; it took another year and a half to rebuild to 76 '
                              '[52k99Zbi6fk @ 00:06:41]. The CoLiving Insider walks through an owner '
                              'selling nine months into payback on a $27K setup and an owner defaulting on '
                              'the mortgage, and puts every fix before signing: strike the sale clause, '
                              'add a buyout and a right of first refusal, pull county records, and get an '
                              'SNDA plus a notice clause [zj0PhRK1anA @ 00:00:48]. Farhan Abbasi prices '
                              'the wind-down when a market closes on you: storage at $350 a month for '
                              'three apartments over about eight months, furniture that cost $2–3K per '
                              "apartment with near-zero resale, and a final answer that 'the simplest one "
                              "was to unfortunately throw them away' [Y2Nj2IYzw-Q @ 01:00:07].",
                              'Scale itself eats margin, and the operators who ran the biggest portfolios '
                              "report it most precisely. Humza Zafar's Dallas economy units rented for "
                              '$800 and earned about $3,000 in 2021–22, furnished with $2,000 of IKEA, '
                              'until competition killed that tier and forced him into A-class only '
                              '[1D3J3ID1ZZM @ 00:04:57]. He also reports per-unit net shrinking as the '
                              'portfolio grows, from $1,500 down to $700–800 and from $800 down to $300. '
                              'His Detroit case is the cleanest warning on cannibalization: one building '
                              'went from 20 to 50 units, another 30 were added across the street, and net '
                              'per unit collapsed from $1,200–1,500 to about $500, a roughly $100K loss; '
                              'he now concentrates units only in Dubai or New York-type demand '
                              '[1D3J3ID1ZZM @ 00:33:19]. Jeremy Werden names the same trap from the '
                              "competitor's side, saturation and price wars whenever nearby operators "
                              'launch units, and pairs it with the seasonal mistake of failing to bank '
                              'summer profit to carry winter rent [kXJgiO6RYaU @ 00:04:29]. Colin Wright '
                              'frames the problem as markets saturated with bad hosts rather than with '
                              'hosts, adding that the $2K IKEA furniture package that used to win no '
                              'longer works [NSyEBVGX02o @ 00:15:17].',
                              'The operational failures are personal, expensive, and usually discovered by '
                              'the operators who scaled first. Jeremy Werden warns that roughly year-long '
                              '0% APR cards fund the furniture until the promo ends and the operator is '
                              'left sitting on six-figure debt, a spiral he wants viewers to steer clear '
                              'of entirely [kXJgiO6RYaU @ 00:05:02]. Richie Matthews self-furnished from '
                              'IKEA and Amazon and cleaned his own units for the first year while '
                              "acquiring 18 properties in 12 months; his summary of that stretch is 'my "
                              "first year was up all night' [VtVf0h80q0w @ 00:08:55]. Colin Wright names "
                              'his single biggest mistake as running with no SOPs at all, which meant '
                              'training every VA one-on-one as the team grew [NSyEBVGX02o @ 00:52:50]. '
                              "Brian Fontenot found that even with Guesty's communication service covering "
                              'support at 4–5 units he was still taking 2 a.m. lockout calls, which forced '
                              'an admin and communications hire at 5–7 units, growth of that team from one '
                              'person to three or four by 10–15 units, and a dedicated property manager '
                              'once he reached 20 units [D63ppvOFpvk @ 00:22:08].'],
               'table': {'caption': 'Failure modes operators hit firsthand and the fix each one now runs',
                         'headers': ['Failure Mode',
                                     'What Happened',
                                     'Practitioner Fix or Check',
                                     'Expert Source'],
                         'rows': [['Owner sells the building in the middle of payback',
                                   'A $27K setup was stranded nine months into payback when the owner sold',
                                   'Strike the sale clause and add a buyout plus right of first refusal',
                                   'The CoLiving Insider ([zj0PhRK1anA @ 00:00:48])'],
                                  ['Cannibalizing your own units in one building',
                                   'Detroit building went 20 to 50 units and net per unit fell to about '
                                   '$500',
                                   'Concentrate units only in Dubai or New York-type demand markets',
                                   'Humza Zafar ([1D3J3ID1ZZM @ 00:33:19])'],
                                  ['Landlord steals the business model mid-negotiation',
                                   'A Mexico City owner heard the projected income, cancelled, and started '
                                   'his own Airbnb',
                                   'Never lead with sublet or Airbnb; pitch a corporate rental, short or '
                                   'long term',
                                   'Short Term Sage - Airbnb, Vacation Rental Host ([z5rgPmF_Dm4 @ '
                                   '00:45:16])'],
                                  ['Stale dynamic pricing data during a demand shock',
                                   'Wheelhouse relied on events that COVID cancelled, so its rate data '
                                   'went stale',
                                   'Switched to PriceClaro manual pricing and saw a 20 to 30 revenue '
                                   'increase',
                                   'Short Term Rental Secrets ([D63ppvOFpvk @ 00:23:46])'],
                                  ['Card-funded furniture turning into a debt spiral',
                                   'Year-long 0% APR furniture cards can end in six-figure debt when '
                                   'promos expire',
                                   'Pause growth and clear the cards before the 15-month promo window ends',
                                   'Jeremy Werden ([kXJgiO6RYaU @ 00:05:02]); Humza Zafar ([1D3J3ID1ZZM @ '
                                   '00:13:20])'],
                                  ['Spotty internet breaking the smart-home stack',
                                   'Weak internet took down locks and devices, forcing monthly-rotated '
                                   'backup lock codes',
                                   'Switch to a better internet provider and treat it like electricity',
                                   'Rafael Loza ([J8lQc66Jf6c @ 00:02:38])'],
                                  ['Resident or guest non-payment wiping out monthly margin',
                                   "One $850 non-payment equals roughly half of that house's monthly "
                                   'profit',
                                   'Screen residents, follow fair housing, and keep three months of owner '
                                   'rent reserved',
                                   'The CoLiving Insider ([zj0PhRK1anA @ 00:03:38])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Kill Checks Before the Next Lease',
                           'body': 'Run these checks before signing or adding another unit; each one comes '
                                   'from an operator who paid for skipping it.',
                           'items': ['Walk away or renegotiate any deal that is not spitting out at least '
                                     '$2,000 to $2,500 net per month per property [Richie Matthews — '
                                     'VtVf0h80q0w @ 00:06:44].',
                                     'Hold each new house at break-even for 90 days and put it in its own '
                                     'LLC before opening the next one [The CoLiving Insider — zj0PhRK1anA '
                                     '@ 00:07:57].',
                                     'Do not stack units in one building or across the street outside '
                                     'Dubai or New York-type demand; Detroit cannibalization cost about '
                                     '$100K [Humza Zafar — 1D3J3ID1ZZM @ 00:53:42].',
                                     'Negotiate a one-to-two-month-rent escape clause before signing, and '
                                     'offset that exit cost with a two-month rent concession on the next '
                                     'property [Official Success Formula — NSyEBVGX02o @ 00:04:30].']}}],
 'pull_quote': '"And now you\'re able to scale because you can\'t scale chaos." — Richie Matthews '
               '(O4cBKKUBS64 @ 00:07:11).',
 'diagram_id': 'diag-02',
 'action_checklist': ['Screen every market for at least a 2x and ideally 3x revenue-to-rent multiple using '
                      '24 months of month-over-month data, and walk if the data is not there [Richie '
                      'Matthews — O4cBKKUBS64 @ 00:10:19].',
                      'Hire a virtual assistant the day you sign the lease, make sure they work for a '
                      'US-based operator, and pay them through Wise every other week [Richie Matthews — '
                      'VtVf0h80q0w @ 00:04:17].',
                      'Run Hospitable synced with PriceLabs for daily dynamic pricing and stay away from '
                      "Airbnb's native pricing tool [Rafael Loza — J8lQc66Jf6c @ 00:01:07].",
                      'Background-check every guest through Autohost for ID, sex-offender and watchlist '
                      'hits, and give property managers portal access to the reports [Short Term Rental '
                      'Secrets — D63ppvOFpvk @ 00:15:01].',
                      'Drive your neighborhood for buildings under construction and ask the contractors to '
                      'connect you with the owner [Alex Sabio — 52k99Zbi6fk @ 00:07:06].',
                      'Install Ring doorbells, smart locks with a unique code per guest and per cleaner, '
                      'and Minut sensors for decibels, smoking and crowds to back claims with evidence '
                      '[Official Success Formula — NSyEBVGX02o @ 00:30:09].'],
 'statutory_citations': [{'title': 'Humza Zafar — Humza Zafar on Scaling to $1M/mo with Airbnb Arbitrage & '
                                   'Why Most Hosts Fail | BNB Inside [00:33:19]',
                          'url': 'https://www.youtube.com/watch?v=1D3J3ID1ZZM&t=1999s',
                          'relevance': 'Primary practitioner testimony on per-unit margin compression and '
                                       'Detroit unit cannibalization at scale.'},
                         {'title': 'The CoLiving Insider — Rental Arbitrage Gone Wrong: 5 Ways a Master '
                                   'Lease Fails [00:07:57]',
                          'url': 'https://www.youtube.com/watch?v=zj0PhRK1anA&t=477s',
                          'relevance': 'Primary practitioner testimony on master lease failure modes, '
                                       'one-LLC-per-house and 90-day break-even growth rules.'},
                         {'title': 'Richie Matthews — Billion Dollar Blueprint For Apartment Arbitrage '
                                   '[00:16:04]',
                          'url': 'https://www.youtube.com/watch?v=O4cBKKUBS64&t=964s',
                          'relevance': 'Primary practitioner testimony on speed-scaling through 900 VA '
                                       'protocols and 20-platform distribution.'},
                         {'title': 'Jeremy Werden — 6 Brutal Reasons I Quit Airbnb Arbitrage And Switched '
                                   'to Co Hosting [00:05:02]',
                          'url': 'https://www.youtube.com/watch?v=kXJgiO6RYaU&t=302s',
                          'relevance': 'Primary practitioner testimony on 0% APR debt spirals, saturation '
                                       'price wars and the switch to co-hosting.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': '52k99Zbi6fk',
                       'title': 'Scaling to 76 Airbnb Arbitrage Units with Rafa Loza',
                       'channel': 'Alex Sabio',
                       'author': 'Alex Sabio',
                       'text': 'You will only be a business as long as the landlord or Property Management '
                               'allows you to be in the building.',
                       'tip': 'You will only be a business as long as the landlord or Property Management '
                              'allows you to be in the building.',
                       'timestamp': 214,
                       'timestamp_seconds': 214,
                       'timestamp_label': '[00:03:34]',
                       'url': 'https://www.youtube.com/watch?v=52k99Zbi6fk&t=214s',
                       'markdown': '[00:03:34](https://www.youtube.com/watch?v=52k99Zbi6fk&t=214s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'J8lQc66Jf6c',
                       'title': 'How to Automate your Airbnb Rental Arbitrage!',
                       'channel': 'Rafael Loza',
                       'author': 'Rafael Loza',
                       'text': "Please stay away from it, do not use it, it's terrible.",
                       'tip': "Please stay away from it, do not use it, it's terrible.",
                       'timestamp': 67,
                       'timestamp_seconds': 67,
                       'timestamp_label': '[00:01:07]',
                       'url': 'https://www.youtube.com/watch?v=J8lQc66Jf6c&t=67s',
                       'markdown': '[00:01:07](https://www.youtube.com/watch?v=J8lQc66Jf6c&t=67s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'VtVf0h80q0w',
                       'title': 'Rental Arbitrage Has Changed — Use This New System',
                       'channel': 'Richie Matthews',
                       'author': 'Richie Matthews',
                       'text': "And if you're not spitting out at least $2,000 to $2,500 per month per "
                               'property, walk away from the deal or better yet, negotiate it.',
                       'tip': "And if you're not spitting out at least $2,000 to $2,500 per month per "
                              'property, walk away from the deal or better yet, negotiate it.',
                       'timestamp': 404,
                       'timestamp_seconds': 404,
                       'timestamp_label': '[00:06:44]',
                       'url': 'https://www.youtube.com/watch?v=VtVf0h80q0w&t=404s',
                       'markdown': '[00:06:44](https://www.youtube.com/watch?v=VtVf0h80q0w&t=404s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Y2Nj2IYzw-Q',
                       'title': 'How to manage and build Rental Arbitrage properties remotely w/ Farhan '
                                'Abbasi',
                       'channel': 'Short Term Sage - Airbnb, Vacation Rental Host',
                       'author': 'Short Term Sage - Airbnb, Vacation Rental Host',
                       'text': "Don't fall into the hype, do your financial modeling very conservatively.",
                       'tip': "Don't fall into the hype, do your financial modeling very conservatively.",
                       'timestamp': 3939,
                       'timestamp_seconds': 3939,
                       'timestamp_label': '[01:05:39]',
                       'url': 'https://www.youtube.com/watch?v=Y2Nj2IYzw-Q&t=3939s',
                       'markdown': '[01:05:39](https://www.youtube.com/watch?v=Y2Nj2IYzw-Q&t=3939s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'D63ppvOFpvk',
                       'title': 'Scaling a Rental Arbitrage Business With Systems & Teams with Brian '
                                'Fontenot',
                       'channel': 'Short Term Rental Secrets',
                       'author': 'Short Term Rental Secrets',
                       'text': "What I recommend definitely is that you don't go the route of signing it "
                               'in a personal name.',
                       'tip': "What I recommend definitely is that you don't go the route of signing it in "
                              'a personal name.',
                       'timestamp': 808,
                       'timestamp_seconds': 808,
                       'timestamp_label': '[00:13:28]',
                       'url': 'https://www.youtube.com/watch?v=D63ppvOFpvk&t=808s',
                       'markdown': '[00:13:28](https://www.youtube.com/watch?v=D63ppvOFpvk&t=808s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'NSyEBVGX02o',
                       'title': 'He Makes $600K/Month Without Owning a Single Property | Airbnb Arbitrage '
                                'Secrets with Colin Wright',
                       'channel': 'Official Success Formula',
                       'author': 'Official Success Formula',
                       'text': "I'm getting free rent on all of my deals now because I don't take deals "
                               'without.',
                       'tip': "I'm getting free rent on all of my deals now because I don't take deals "
                              'without.',
                       'timestamp': 3483,
                       'timestamp_seconds': 3483,
                       'timestamp_label': '[00:58:03]',
                       'url': 'https://www.youtube.com/watch?v=NSyEBVGX02o&t=3483s',
                       'markdown': '[00:58:03](https://www.youtube.com/watch?v=NSyEBVGX02o&t=3483s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'z5rgPmF_Dm4',
                       'title': 'What its like scaling a Rental Arbitrage business in Mexico City w/ '
                                'Nathan & Raquel Carillo',
                       'channel': 'Short Term Sage - Airbnb, Vacation Rental Host',
                       'author': 'Short Term Sage - Airbnb, Vacation Rental Host',
                       'text': "It's the same amount of effort that I need to put and it's much more "
                               'profitable.',
                       'tip': "It's the same amount of effort that I need to put and it's much more "
                              'profitable.',
                       'timestamp': 1215,
                       'timestamp_seconds': 1215,
                       'timestamp_label': '[00:20:15]',
                       'url': 'https://www.youtube.com/watch?v=z5rgPmF_Dm4&t=1215s',
                       'markdown': '[00:20:15](https://www.youtube.com/watch?v=z5rgPmF_Dm4&t=1215s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'O4cBKKUBS64',
                       'title': 'Billion Dollar Blueprint For Apartment Arbitrage',
                       'channel': 'Richie Matthews',
                       'author': 'Richie Matthews',
                       'text': "And now you're able to scale because you can't scale chaos.",
                       'tip': "And now you're able to scale because you can't scale chaos.",
                       'timestamp': 431,
                       'timestamp_seconds': 431,
                       'timestamp_label': '[00:07:11]',
                       'url': 'https://www.youtube.com/watch?v=O4cBKKUBS64&t=431s',
                       'markdown': '[00:07:11](https://www.youtube.com/watch?v=O4cBKKUBS64&t=431s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'O4cBKKUBS64',
                       'title': 'Billion Dollar Blueprint For Apartment Arbitrage',
                       'channel': 'Richie Matthews',
                       'author': 'Richie Matthews',
                       'text': 'At 15% vacancy, trust me, the landlord is going to fly to town.',
                       'tip': 'At 15% vacancy, trust me, the landlord is going to fly to town.',
                       'timestamp': 527,
                       'timestamp_seconds': 527,
                       'timestamp_label': '[00:08:47]',
                       'url': 'https://www.youtube.com/watch?v=O4cBKKUBS64&t=527s',
                       'markdown': '[00:08:47](https://www.youtube.com/watch?v=O4cBKKUBS64&t=527s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'GFTAQzCp4aM',
                       'title': 'Maximizing Profits with Rental Arbitrage on Airbnb and VRBO',
                       'channel': 'Beau Eckstein, Business Ownership Coach',
                       'author': 'Beau Eckstein, Business Ownership Coach',
                       'text': "Build up our cash flow with Arbitrage because it's not long-term wealth, "
                               "it's cash flow, it's temporary.",
                       'tip': "Build up our cash flow with Arbitrage because it's not long-term wealth, "
                              "it's cash flow, it's temporary.",
                       'timestamp': 1424,
                       'timestamp_seconds': 1424,
                       'timestamp_label': '[00:23:44]',
                       'url': 'https://www.youtube.com/watch?v=GFTAQzCp4aM&t=1424s',
                       'markdown': '[00:23:44](https://www.youtube.com/watch?v=GFTAQzCp4aM&t=1424s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'roqaSiCOnsI',
                       'title': 'What is Rental Arbitrage vs Cohosting vs BRRRR vs Turnkey',
                       'channel': 'Short Term Sage - Airbnb, Vacation Rental Host',
                       'author': 'Short Term Sage - Airbnb, Vacation Rental Host',
                       'text': "If things go belly-up I'm out as soon as the lease ends.",
                       'tip': "If things go belly-up I'm out as soon as the lease ends.",
                       'timestamp': 203,
                       'timestamp_seconds': 203,
                       'timestamp_label': '[00:03:23]',
                       'url': 'https://www.youtube.com/watch?v=roqaSiCOnsI&t=203s',
                       'markdown': '[00:03:23](https://www.youtube.com/watch?v=roqaSiCOnsI&t=203s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'scmRAbKvEPk',
                       'title': 'Which is Harder to Start and Scale, Rental Arbitrage or Cohosting?',
                       'channel': 'Short Term Sage - Airbnb, Vacation Rental Host',
                       'author': 'Short Term Sage - Airbnb, Vacation Rental Host',
                       'text': "It always bleeds into the next method so you're going to want a good "
                               'blend.',
                       'tip': "It always bleeds into the next method so you're going to want a good blend.",
                       'timestamp': 374,
                       'timestamp_seconds': 374,
                       'timestamp_label': '[00:06:14]',
                       'url': 'https://www.youtube.com/watch?v=scmRAbKvEPk&t=374s',
                       'markdown': '[00:06:14](https://www.youtube.com/watch?v=scmRAbKvEPk&t=374s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'tfwUVSMpB2c',
                       'title': 'Running a Short Term Rental though the Master Lease (Arbitrage) model',
                       'channel': 'Short Term Dojo',
                       'author': 'Short Term Dojo',
                       'text': "If you don't have money and you want to build your unit count in your "
                               "portfolio, it's probably better off to go in the co-host route.",
                       'tip': "If you don't have money and you want to build your unit count in your "
                              "portfolio, it's probably better off to go in the co-host route.",
                       'timestamp': 777,
                       'timestamp_seconds': 777,
                       'timestamp_label': '[00:12:57]',
                       'url': 'https://www.youtube.com/watch?v=tfwUVSMpB2c&t=777s',
                       'markdown': '[00:12:57](https://www.youtube.com/watch?v=tfwUVSMpB2c&t=777s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'zj0PhRK1anA',
                       'title': 'Rental Arbitrage Gone Wrong: 5 Ways a Master Lease Fails',
                       'channel': 'The CoLiving Insider',
                       'author': 'The CoLiving Insider',
                       'text': 'Put each house in its own limited liability company or LLC, so one bad '
                               'lease cannot take down the rest.',
                       'tip': 'Put each house in its own limited liability company or LLC, so one bad '
                              'lease cannot take down the rest.',
                       'timestamp': 477,
                       'timestamp_seconds': 477,
                       'timestamp_label': '[00:07:57]',
                       'url': 'https://www.youtube.com/watch?v=zj0PhRK1anA&t=477s',
                       'markdown': '[00:07:57](https://www.youtube.com/watch?v=zj0PhRK1anA&t=477s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'zj0PhRK1anA',
                       'title': 'Rental Arbitrage Gone Wrong: 5 Ways a Master Lease Fails',
                       'channel': 'The CoLiving Insider',
                       'author': 'The CoLiving Insider',
                       'text': 'Almost every fix happens before you sign.',
                       'tip': 'Almost every fix happens before you sign.',
                       'timestamp': 554,
                       'timestamp_seconds': 554,
                       'timestamp_label': '[00:09:14]',
                       'url': 'https://www.youtube.com/watch?v=zj0PhRK1anA&t=554s',
                       'markdown': '[00:09:14](https://www.youtube.com/watch?v=zj0PhRK1anA&t=554s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '1D3J3ID1ZZM',
                       'title': 'Humza Zafar on Scaling to $1M/mo with Airbnb Arbitrage & Why Most Hosts '
                                'Fail | BNB Inside',
                       'channel': 'Humza Zafar',
                       'author': 'Humza Zafar',
                       'text': 'Location is the most important thing.',
                       'tip': 'Location is the most important thing.',
                       'timestamp': 3206,
                       'timestamp_seconds': 3206,
                       'timestamp_label': '[00:53:26]',
                       'url': 'https://www.youtube.com/watch?v=1D3J3ID1ZZM&t=3206s',
                       'markdown': '[00:53:26](https://www.youtube.com/watch?v=1D3J3ID1ZZM&t=3206s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'nPFkgk7QMfA',
                       'title': 'Whats better? Airbnb Arbitrage vs Airbnb Management (Co-hosting)',
                       'channel': 'Milan Sánchez Stiepovic',
                       'author': 'Milan Sánchez Stiepovic',
                       'text': "I've tried both models and this one for me it's 100% superior, management "
                               'or co-hosting.',
                       'tip': "I've tried both models and this one for me it's 100% superior, management "
                              'or co-hosting.',
                       'timestamp': 1100,
                       'timestamp_seconds': 1100,
                       'timestamp_label': '[00:18:20]',
                       'url': 'https://www.youtube.com/watch?v=nPFkgk7QMfA&t=1100s',
                       'markdown': '[00:18:20](https://www.youtube.com/watch?v=nPFkgk7QMfA&t=1100s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'kXJgiO6RYaU',
                       'title': '6 Brutal Reasons I Quit Airbnb Arbitrage And Switched to Co Hosting',
                       'channel': 'Jeremy Werden',
                       'author': 'Jeremy Werden',
                       'text': 'Benefit number four, and again I think this really is the biggest one, is '
                               'lower financial risk.',
                       'tip': 'Benefit number four, and again I think this really is the biggest one, is '
                              'lower financial risk.',
                       'timestamp': 442,
                       'timestamp_seconds': 442,
                       'timestamp_label': '[00:07:22]',
                       'url': 'https://www.youtube.com/watch?v=kXJgiO6RYaU&t=442s',
                       'markdown': '[00:07:22](https://www.youtube.com/watch?v=kXJgiO6RYaU&t=442s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'}]}
