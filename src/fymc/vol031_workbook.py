from __future__ import annotations

def build_volume_031_workbook() -> dict:
    return {'workbook_id': 'wb-031-uber-and-commercial-fleet-arbitrage',
 'volume_id': 'vol-031-uber-and-commercial-fleet-arbitrage',
 'title': 'Uber & Commercial Fleet Arbitrage — Practitioner Testimony Operator Workbook',
 'subtitle': 'A field workbook for launching an Uber Fleet, choosing the revenue vehicle, running Uber '
             'Black unit economics, licensing plates and permits, building private chauffeur clients, and '
             'renting cheap cars to gig drivers by the week',
 'worksheets': [{'worksheet_id': 'ws-01',
                 'number': 1,
                 'title': 'Fleet Launch and Revenue Vehicle Selection Plan',
                 'purpose': 'Turn the Uber Fleet Partner Program into a working back office and choose the '
                            'first revenue vehicle on hard numbers. Set up the account, fund a real '
                            'reserve, quote insurance off the VIN, price the weekly rate, vet renters, and '
                            'stack the full monthly cost before signing.',
                 'chapter_ref': 'Q1-Q2',
                 'instructions': ['Complete every field in order, because the cash reserve, insurance '
                                  'quote, and monthly cost stack decide whether the vehicle choice and '
                                  'rate card further down are even affordable.',
                                  'Use your own market numbers wherever possible, and set each figure '
                                  'beside the practitioner benchmark cited in the example so the gap '
                                  'between your plan and street reality is visible.',
                                  'Write dollar amounts per week and per month, not as ranges, so the '
                                  'payback horizon and weekly rate card can be checked with simple '
                                  'arithmetic later.',
                                  'Treat every operator gate as a hard stop: no limousine license, no full '
                                  'payment, no VIN insurance quote, or no funded reserve means the launch '
                                  'waits.',
                                  'Revisit this worksheet after your first eight weeks of operation and '
                                  'replace every estimate with actual dashboard earnings, insurance '
                                  'invoices, and fuel receipts.'],
                 'fields': [{'name': 'fleet_account_setup',
                             'type': 'textarea',
                             'prompt': 'List every step you still need to complete to open your Uber Fleet '
                                       'account and business setup, including tax information entry, '
                                       'dashboard access, and how weekly driver earnings will route into '
                                       'your account before you pay each driver their share.',
                             'example': 'Enter tax information carefully and double-check it before '
                                        'continuing, per Norman Tutorials [Norman Tutorials — 70EXcECzC70 '
                                        '@ 00:01:33]. Then mirror the Khushnud Numonov flow: earnings '
                                        'arrive weekly in the checking account, the owner keeps their part '
                                        'and sends the rest to the driver [Khushnud Numonov — i1B7HEM_kcM '
                                        '@ 00:01:21]. My checklist: tax ID entered, bank linked, Fleet app '
                                        'installed, driver invite drafted.'},
                            {'name': 'starting_capital_reserve',
                             'type': 'textarea',
                             'prompt': 'Write down your total launch cash, then split it between the '
                                       'vehicle price and a separate reserve for licensing, permits, '
                                       'insurance, and one surprise repair week. State plainly whether you '
                                       'are starting with exactly one vehicle and why.',
                             'example': 'TJackk is blunt: if the cash only covers the SUV, do not start, '
                                        'because the reserve must absorb licensing, permits, insurance, '
                                        'and a surprise repair week [TJackk — UTnHLaPqh1s @ 00:04:02]. '
                                        'Rideshare Professor adds that people buy five vehicles at once '
                                        'when they should start with one [Rideshare Professor — '
                                        'tKKCFcEvdl4 @ 00:05:29]. My plan: one SUV, reserve funded before '
                                        'purchase.'},
                            {'name': 'commercial_insurance_vin_quote',
                             'type': 'textarea',
                             'prompt': 'Record the exact VINs of every candidate vehicle you are '
                                       'considering and the commercial auto insurance quote for each one. '
                                       'Note who will hold the policy, you as fleet owner or the renter, '
                                       'and which candidate quotes cheapest.',
                             'example': 'Quote off the VIN before buying; TJackk found swapping a Tahoe '
                                        'VIN for an Infiniti could come back cheaper, and once the truck '
                                        'is bought you are stuck with it [TJackk — GBM9d0WqM-0 @ '
                                        '00:20:42]. Renters may not carry commercial auto because it is '
                                        'super expensive, so hold it yourself [TJackk — Bf1i8iZKK5M @ '
                                        '00:05:45]. Log: Tahoe VIN versus QX80 VIN quotes.'},
                            {'name': 'weekly_rate_card',
                             'type': 'textarea',
                             'prompt': 'Build your weekly rate card for each vehicle class you plan to '
                                       'place in the fleet, choosing a flat weekly rental or a 50/50 '
                                       'earnings split, and explain how your rate compares against '
                                       'competitors charging in your market.',
                             'example': 'Rideshare Professor leases Chevrolet Suburbans at $600 a week and '
                                        'still makes an insane return, takes $100 more for Cadillacs, and '
                                        'prices a Sienna at $450, while a competitor asks $800 for a '
                                        'Suburban [Rideshare Professor — 7e3yD_HEDec @ 00:01:28]. My card: '
                                        'Suburban $600 flat, Escalade $700 flat, Sienna $450 flat, with '
                                        '50/50 split offered only to proven drivers.'},
                            {'name': 'payback_horizon',
                             'type': 'textarea',
                             'prompt': 'Calculate the payback horizon for your first vehicle using '
                                       'purchase price, weekly rate, and realistic net per week after Uber '
                                       'commission and driver pay. State the month you expect the vehicle '
                                       'fully paid and profit to begin.',
                             'example': 'Rideshare Professor targets an auction vehicle fully paid within '
                                        '15 months, with really good money from month 16 onward [Rideshare '
                                        'Professor — 4Y5_eWf85tM @ 00:05:51]. Owners Risk models a tighter '
                                        'case: $1,500 gross weekly fares, 25% Uber commission, $900 kept '
                                        'by the driver, leaving $225 per car weekly [Owners Risk — '
                                        'oDmpBy9CTek @ 00:07:27]. My Suburban: payoff month 15.'},
                            {'name': 'renter_vetting_rules',
                             'type': 'textarea',
                             'prompt': 'Write the non-negotiable rules a renter must meet before you add '
                                       'them in the Fleet app, covering licensing, payment timing, '
                                       'hardship requests, and what you will do if Uber repeatedly flags '
                                       'their account with an action needed notice.',
                             'example': "TJackk's rule: no limousine license and no full payment up front "
                                        'means no car, with pay-you-later requests and hardship discounts '
                                        'off the table [TJackk — 4NPuQA-V4ZA @ 00:04:57]. The first renter '
                                        'TJackk and Camila onboarded ran a bought Uber Black account that '
                                        'Uber kept flagging [TJackk — 4NPuQA-V4ZA @ 00:02:52]. My rule: '
                                        'second flag, onboarding stops.'},
                            {'name': 'driver_monitoring_policy',
                             'type': 'textarea',
                             'prompt': 'Describe how you will monitor driving style and account activity '
                                       'once a renter is on the road, including the tracking app you use, '
                                       'the speed threshold that triggers a warning, and the exact point a '
                                       'driver is removed.',
                             'example': 'Rideshare Professor watches driving style with tracking apps: '
                                        'speeding over 80 earns one warning, and the second time the '
                                        'driver is out [Rideshare Professor — 4Y5_eWf85tM @ 00:13:13]. '
                                        'Drivers need only one Uber trip a month to keep the fleet account '
                                        'active, so private trips may run on the car otherwise [Rideshare '
                                        'Professor — 4Y5_eWf85tM @ 00:12:18]. My policy: written warning, '
                                        'then removal.'},
                            {'name': 'vehicle_class_choice',
                             'type': 'text',
                             'prompt': 'Choose the revenue vehicle class for your first unit, naming seat '
                                       'count, tier, and the ride types it unlocks. Explain why that class '
                                       'fits the job you plan to run rather than simply the vehicle you '
                                       'personally prefer.',
                             'example': 'TJackk warns against a five-seater SUV for chauffeur or Uber '
                                        'Black work and says get a seven-seater [TJackk — -QE8dzRh7To @ '
                                        '00:02:57]. Their Infiniti QX80 unlocked X, Comfort, XL, Black and '
                                        'Black SUV for about a $300 daily floor, and one Black SUV ride '
                                        'paid $150 for an hour [TJackk — E0a86uKzcuk @ 00:03:08]. My pick: '
                                        'seven-seat large SUV.'},
                            {'name': 'monthly_nut_stack',
                             'type': 'textarea',
                             'prompt': 'Stack your full monthly cost to run the chosen vehicle before '
                                       'signing anything: car note, commercial insurance, fuel at '
                                       'realistic miles per gallon, and maintenance. Then note any older '
                                       'car you can rent out to offset that total.',
                             'example': 'ESCAPE THE MATRIX financed 100% of a $125,000 Navigator at $1,733 '
                                        'a month; with $370 commercial liability and $900 to $1,200 gas at '
                                        'about 13 mpg, the nut ran $3,000 to $3,300 [ESCAPE THE MATRIX — '
                                        'fPh6slkW9Tk @ 00:06:08]. Renting out the former Tesla clears '
                                        'about $500 a month toward it [ESCAPE THE MATRIX — fPh6slkW9Tk @ '
                                        '00:09:45].'},
                            {'name': 'credit_and_model_year_check',
                             'type': 'textarea',
                             'prompt': "Confirm your market's model-year floor for Uber Black, your "
                                       'current credit score, and the mileage and Carfax standard you will '
                                       'accept on a used SUV. Write the maximum price you will pay and '
                                       'your private clientele plan.',
                             'example': 'Yusuf Benallal shows a 620 credit score turning a 2025 Escalade '
                                        'into about $3,500 a month with insurance, and the NYC call '
                                        'surfaces a 2024-and-newer floor [Yusuf Benallal — xrJ-xGav6Xo @ '
                                        '00:03:35]. TJackk will pay 40 for an SUV with 60 to 80k miles, '
                                        'but the Carfax better be clean [TJackk — CB9UNWu4LMM @ 00:08:05]. '
                                        'My cap: 40 with clean Carfax.'}],
                 'completion_gate': 'Do not move to Worksheet 2 until one vehicle is chosen, its VIN has a '
                                    'commercial insurance quote in hand, the reserve covers licensing, '
                                    'permits, insurance, and a surprise repair week, and the weekly rate '
                                    'card produces a written payback month.'},
                {'worksheet_id': 'ws-02',
                 'number': 2,
                 'title': 'Uber Black Shift Economics and Fleet Licensing Tracker',
                 'purpose': 'Measure what a premium shift actually earns after fixed daily burn, filter '
                            'requests by dollars per mile, plan days and airports around penalties, and '
                            'lock down the plates or permits the market demands so every dollar earned is '
                            'earned legally and kept.',
                 'chapter_ref': 'Q3-Q4',
                 'instructions': ['Start with the fixed daily burn, because every shift benchmark, rate '
                                  'comparison, and acceptance filter below only makes sense once you know '
                                  'how far negative you begin each morning.',
                                  'Log real shifts rather than hoped-for shifts, recording hours online, '
                                  'hours active, trip count, gross, tolls, and gas for at least three '
                                  'consecutive working days.',
                                  'Write airport rules, decline penalties, and pickup fees for every lot '
                                  'you plan to work, and update them whenever a practitioner warning or '
                                  'new charge appears.',
                                  'Complete only the licensing field that matches your market, New York '
                                  'City plates or California TCP permits, and mark every step with its '
                                  'cost, deadline, and current status.',
                                  'Treat any missing permit, commercial registration, or airport '
                                  'credential as a reason to park the vehicle, because fines, arrest, and '
                                  'impound erase weeks of shift earnings.'],
                 'fields': [{'name': 'daily_fixed_burn',
                             'type': 'textarea',
                             'prompt': 'Price your fixed daily burn before the first ride of a shift: '
                                       'inspection, gas, car wash, tolls, and your share of weekly rent or '
                                       'note. Write the dollar figure you are already down when you log '
                                       'online each morning.',
                             'example': 'maxxito sat on negative $91 before the first ride once '
                                        'inspection, gas, and wash hit one NYC shift [maxxito — '
                                        'GsXJ5ED0hT8 @ 00:00:03]. ESCAPE THE MATRIX spent over $200 before '
                                        'starting work, with one charge at 103 including tax [ESCAPE THE '
                                        'MATRIX — q6qypIL66TM @ 00:02:45]. My burn: $86 rent share, $45 '
                                        'gas, $15 wash.'},
                            {'name': 'rate_card_comparison',
                             'type': 'textarea',
                             'prompt': 'Write the per-mile, per-minute, and minimum fare for Uber Black '
                                       'and UberX in your market side by side. Calculate how many UberX '
                                       'trips equal one typical Black trip and whether that multiple '
                                       'justifies the premium vehicle cost.',
                             'example': 'The Startup Hub logs UberX at $0.80 a mile, $0.28 a minute, $6.50 '
                                        'minimum, against Black at $2.90 a mile, $0.71 a minute, $15.75 '
                                        'minimum [The Startup Hub — aykNFM9361U @ 00:02:11]. ESCAPE THE '
                                        'MATRIX trades 20 UberX rides for five to 10 Black rides at '
                                        'similar money [ESCAPE THE MATRIX — fPh6slkW9Tk @ 00:05:15]. My '
                                        'multiple: roughly 3.6 per mile.'},
                            {'name': 'shift_log_benchmark',
                             'type': 'textarea',
                             'prompt': 'Log your last three premium shifts with hours online, hours '
                                       'active, trip count, and gross. Compare each against a practitioner '
                                       'benchmark and write your earnings per online hour, earnings per '
                                       'active hour, and the gap to your target.',
                             'example': "Khushnud Numonov's first full Black shift in a rented 2016 "
                                        'Suburban: 12 hours online, six active, 18 trips, $544, about $45 '
                                        'an hour online and $90 active [Khushnud Numonov — -SDfxVQEXXs @ '
                                        '00:03:09]. GigCalifornia ran 15 hours in San Francisco for $550, '
                                        'about $36.67 an hour, against an $800 target [GigCalifornia — '
                                        'OMCcnT_Aer8 @ 00:06:30].'},
                            {'name': 'dollars_per_mile_filter',
                             'type': 'text',
                             'prompt': 'Set your dollars-per-mile acceptance threshold for premium '
                                       'requests and write three real request examples you would reject '
                                       'and three you would accept. Explain how the filter protects '
                                       'mileage, fuel, and wear on a high-cost vehicle every shift.',
                             'example': 'TJackk checks dollars per mile on every request: reject $8 for 17 '
                                        'miles and take $10 for 7 miles [TJackk — iCdSnX4vLHI @ 00:08:43]. '
                                        'Starting at 4am around River Oaks and Post Oak, a $34-35 Comfort '
                                        'airport run set up a $107 hotel Black pickup [TJackk — '
                                        'iCdSnX4vLHI @ 00:05:16]. My floor: $1.40 per mile.'},
                            {'name': 'calendar_and_zone_plan',
                             'type': 'textarea',
                             'prompt': 'Map your weekly schedule by day and zone, naming the days, start '
                                       'times, neighborhoods, and event loops you will work. Note which '
                                       'holidays or event nights you will prioritize and which slow days '
                                       'you will treat as rest.',
                             'example': 'Khushnud Numonov works Tuesdays, Wednesdays and holidays; one '
                                        'holiday paid $900 while the following day paid only $200 '
                                        '[Khushnud Numonov — uhkmLcXXwMk @ 00:30:17]. Frankie runs Fort '
                                        'Worth Stockyards-to-TCU loops after events for a $600-800 day '
                                        'with no traffic, noting people have money in Dallas [Frankie — '
                                        'gMeI77Gf16I @ 00:10:33]. My plan: Tuesday, Wednesday, event '
                                        'Saturdays.'},
                            {'name': 'airport_rules',
                             'type': 'textarea',
                             'prompt': 'List every airport you plan to serve and write its queue rules, '
                                       'decline penalties, pickup fees, and permit requirements. Identify '
                                       'any airport where an extra pickup charge or ban changes whether '
                                       'working that lot is worth the wait.',
                             'example': 'Mr SharK warns that declining two or three jobs in Heathrow '
                                        'Express waiting gets you kicked out, charged GBP 7.50 parking, '
                                        'and sent to the back of the queue [Mr SharK — V5kch9SIAjI @ '
                                        '00:03:40]. In Detroit, drivers paid $10 per pickup, essentially '
                                        'double paying since Uber also takes $10 [FOX 2 Detroit — '
                                        'rvid3s_9KZA @ 00:00:47]. My note: no declines.'},
                            {'name': 'fleet_owner_fare_transparency',
                             'type': 'textarea',
                             'prompt': 'If you drive for another fleet owner or platform, record the real '
                                       'fare a rider pays, the amount the owner quotes you, and the '
                                       'percentage taken. Write the written proof you will demand before '
                                       'accepting any assigned premium job.',
                             'example': 'Khushnud Numonov warns that some fleet owners quote $70 on a $90 '
                                        'Blacklane ride and still take 15 percent, so get the real fare in '
                                        'writing [Khushnud Numonov — uhkmLcXXwMk @ 00:17:34]. Their LA '
                                        'weekly floor across Uber, Lyft, private clients and other '
                                        'companies is at least $3,000 [Khushnud Numonov — uhkmLcXXwMk @ '
                                        '00:04:52]. My demand: screenshot of rider fare.'},
                            {'name': 'used_vehicle_inspection',
                             'type': 'textarea',
                             'prompt': 'For each used premium candidate, write the model year against your '
                                       "market's age limit, the mileage, transmission history, and the "
                                       'mechanic you will pay to inspect it. Flag any pending repair bill '
                                       'before you commit money.',
                             'example': 'The Startup Hub says pay a mechanic $50-100 to inspect any used '
                                        'Black candidate and treat transmissions past 100,000-120,000 '
                                        'miles as a pending bill [The Startup Hub — aykNFM9361U @ '
                                        '00:07:20]. Operators buy used vehicles under the seven-year age '
                                        'limit to stay eligible. My candidate: 2021 Suburban, 88,000 '
                                        'miles, inspection booked, transmission record requested from '
                                        'seller.'},
                            {'name': 'nyc_plate_strategy',
                             'type': 'textarea',
                             'prompt': 'If you operate in New York City, choose your plate path: plating '
                                       'your own car, renting a plate, or the WAV route. Write the '
                                       'application cost, DMV pickup deadline, weekly plate rate, deposit, '
                                       'and who appears on the registration.',
                             'example': 'Soniclove21 prices plating your own car at about $650 at TLC plus '
                                        '$425-$450 at the DMV within 20 days [Soniclove21 — TwvZcpkzAxo @ '
                                        '00:03:13]. FastTrack rents plate plus insurance at $289 a week '
                                        'for 56 weeks against a $1,000 deposit, and AutoMarketplace warns '
                                        'a title holder who is not the registrant cannot pull a car from '
                                        'impound [AutoMarketplace — DiLCf_drK0E @ 00:18:16].'},
                            {'name': 'tcp_permit_sequence',
                             'type': 'textarea',
                             'prompt': 'If you operate in California, write your TCP filing sequence in '
                                       'order: entity, DMV EPN, commercial registration, lienholder '
                                       'approval, permit class, pending TCP number, insurance binding, and '
                                       'airport permits. Mark each step with its cost and status.',
                             'example': 'Khushnud Numonov orders the DMV EPN on day one, about $15 and one '
                                        'to two weeks, then pays $1,000 for Class B or $1,500 for Class A '
                                        '[Khushnud Numonov — 67saVKNzHxc @ 00:10:24]. BusinessRocket says '
                                        'ask for commercial registration in those exact words and hold off '
                                        'binding insurance until the pending TCP number issues '
                                        '[BusinessRocket — s51s14MY4hI @ 00:00:42]. My status: LLC formed, '
                                        'EPN ordered.'}],
                 'completion_gate': 'Do not move to Worksheet 3 until three real shifts are logged against '
                                    'benchmarks, a written dollars-per-mile floor exists, every airport '
                                    'you serve has its penalties recorded, and your plate or TCP sequence '
                                    'shows every step either complete or dated.'},
                {'worksheet_id': 'ws-03',
                 'number': 3,
                 'title': 'Private Chauffeur Build-Out and Weekly Gig Rental Playbook',
                 'purpose': 'Convert app riders into private clients priced by the day, build referral '
                            'partners and a real dispatch system, then add a second income line by renting '
                            'cheap paid-off cars to gig drivers weekly, with honest net math, strict '
                            'screening, and tracker protection on every car.',
                 'chapter_ref': 'Q5-Q6',
                 'instructions': ['Work the private chauffeur fields first, because direct clients keep '
                                  'the full fare while the app takes a cut that practitioners report '
                                  'anywhere from 10 to 70 percent.',
                                  'Name real people and businesses in the referral field, not categories, '
                                  'and record the date you contacted each one alongside the follow-up you '
                                  'sent.',
                                  'Build the gig rental fields around one specific car you could buy this '
                                  'month, using its actual purchase price, insurance quote, and weekly '
                                  'rent rather than a generic fleet average.',
                                  'Write every screening and handoff rule as a yes-or-no check so a helper '
                                  'or virtual assistant could run the handoff without calling you for '
                                  'judgment.',
                                  'Recalculate the true net math every quarter using real insurance, '
                                  'maintenance, and loss figures, and raise or cut weekly rent based on '
                                  'that result, not on competitor posts.'],
                 'fields': [{'name': 'private_client_conversion',
                             'type': 'textarea',
                             'prompt': 'Describe the exact service standard you will deliver on every app '
                                       'ride to convert riders into direct clients: temperature, '
                                       'cleanliness, hospitality, and how you hand over contact details. '
                                       'Write the private rate you will quote returning riders.',
                             'example': 'TJackk treats every Uber Black ride as a free lead, using '
                                        'hospitality, the right AC temperature, and a clean car, because '
                                        'people come back off experience, not just a ride [TJackk — '
                                        'Yr0mmM9YyTc @ 00:05:08]. Rideshare Professor reminds operators '
                                        'that $180 is always $200 [Rideshare Professor — vavDFZYcydE @ '
                                        '00:05:04]. My quote: $200 airport transfer, cash or card.'},
                            {'name': 'day_rate_pricing',
                             'type': 'textarea',
                             'prompt': 'Calculate the daily revenue you must clear to cover your vehicle '
                                       'cost, then set your direct hourly rate, affiliate hourly rate, '
                                       'minimum booking length, and fees such as smoking. Explain why you '
                                       'price the day, not the ride.',
                             'example': 'Black Truck Mick needed $300 a day to cover a rented SUV and '
                                        'admits $40 for six riders was too little [Black Truck Mick — '
                                        'uODRGjORQF4 @ 00:10:28]. After raising prices from $75 an hour, '
                                        'they bill $100 direct, $80 to affiliates, and lifted the smoking '
                                        'fee from $100 to $150 [Black Truck Mick — uODRGjORQF4 @ '
                                        '00:14:11].'},
                            {'name': 'referral_partner_map',
                             'type': 'textarea',
                             'prompt': 'Name ten specific referral partners in your market, sorted into '
                                       'hotel concierges, event planners, and corporate assistants. For '
                                       'each, write how you will introduce yourself, what you will show '
                                       'them, and how you will thank them after referrals.',
                             'example': 'My Chauffeur Life says most of their best clients did not come '
                                        'from ads or social media, and works hotel concierges, event '
                                        'planners, and corporate assistants with a thank-you text after '
                                        'every referral [My Chauffeur Life — Y-1AudoR8JA @ 00:05:13]. Limo '
                                        'Anywhere suggests showing the hotel a branded portal and QR flyer '
                                        'to replace its Uber Black kiosk [Limo Anywhere — 2s7phAWCEE4 @ '
                                        '00:13:17].'},
                            {'name': 'dispatch_system',
                             'type': 'textarea',
                             'prompt': 'Describe the booking and dispatch system that will hold every '
                                       'reservation, replacing WhatsApp and text threads. List the '
                                       'features you need and who enters bookings, such as flight '
                                       'tracking, confirmation emails, pickup instructions, review '
                                       'surveys, and airport zone pricing.',
                             'example': 'Luxury Transportation Academy warns that reservations kept in '
                                        'WhatsApp and text threads get lost nine times out of 10, so move '
                                        'them into a CRM or booking system [Luxury Transportation Academy '
                                        '/ Podcast — yg-RtCxYcG8 @ 00:09:02]. Limo Anywhere stores airport '
                                        'pickup instructions with stars, such as meet at the bottom of the '
                                        'escalator [Limo Anywhere: Livery Software & Training — '
                                        'WYw2hH-qD54 @ 00:01:12].'},
                            {'name': 'permits_and_reserve',
                             'type': 'textarea',
                             'prompt': 'List every permit and airport credential required before your '
                                       'first private booking, then set the weekly dollar amount you will '
                                       'move into a repair reserve. Write how you will track every expense '
                                       'so one luxury repair cannot park the business.',
                             'example': 'Business with Mide states plainly that operating without the TCP '
                                        'is illegal [Business with Mide — 4TzKcRuyrHY @ 00:00:44]. Fares '
                                        'and Frustrations warns that the wrong airport permit or '
                                        'credential means lost bookings, and My Chauffeur Life funds a '
                                        'weekly reserve before a luxury repair costing thousands parks the '
                                        'car for weeks [My Chauffeur Life — Y-1AudoR8JA @ 00:04:09]. My '
                                        'reserve: $250 weekly.'},
                            {'name': 'rental_car_buy_box',
                             'type': 'textarea',
                             'prompt': 'Define your buy box for weekly gig rental cars: models, purchase '
                                       'price ceiling, paid-off versus financed, interior color, and '
                                       'features to avoid. Write where you will source cars and the '
                                       'inspection red flags that end a deal immediately.',
                             'example': 'Alex Auto calls financing the first car instead of buying it very '
                                        'cheap their very first mistake [Alex Auto — G-0j82EXJlk @ '
                                        '00:01:46]. Mr Jay Hill Network buys economy cars with a dark '
                                        'interior and skips sunroofs and leather because darker interiors '
                                        'hide stains [Mr Jay Hill Network — fqYaTfdZsQ8 @ 00:30:41]. My '
                                        'box: cash Corolla or Camry, $3,000 to $6,000.'},
                            {'name': 'weekly_rent_pricing',
                             'type': 'text',
                             'prompt': 'Set your weekly rent for each car in the fleet, your opening rate '
                                       'on older cars, and your daily-payer premium. Explain how you will '
                                       'adjust price if a car sits empty and how upfront payment is '
                                       'collected every week.',
                             'example': 'Etienne Elsaesser puts the market at $350 to $450 a week on a '
                                        'Corolla bought for $3,000 to $6,000 [Etienne Elsaesser — '
                                        'l8b3Oi2g48I @ 00:00:00]. King of Rentals opens older cars at $400 '
                                        'to $500 and cuts gradually, such as $500 down to $450, and '
                                        'charges daily payers a 20% premium [King of Rentals — zIGomHkXMms '
                                        '@ 00:04:27].'},
                            {'name': 'true_net_math',
                             'type': 'textarea',
                             'prompt': 'Strip the influencer math down to your real monthly net per car: '
                                       'gross rent minus insurance, maintenance, processing, cleaning, and '
                                       'a total-loss reserve. Then compute months to payback and compare '
                                       'it with a three-to-four-month target that other operators pitch.',
                             'example': 'Etienne Elsaesser takes $1,600 gross, subtracts $300-plus '
                                        'insurance, about $200 maintenance, processing and cleaning, and a '
                                        '$200 total-loss reserve, landing near $700 net per car monthly '
                                        '[Etienne Elsaesser — amfsF8yd5hg @ 00:06:15]. Alex Auto counts on '
                                        'rentals averaging about three and a half months [Alex Auto — '
                                        'Sukdr8-ecMM @ 00:05:14]. My Corolla: $4,200 cost, six-month '
                                        'payback.'},
                            {'name': 'renter_screening_handoff',
                             'type': 'textarea',
                             'prompt': 'Write your renter screening and handoff procedure step by step: '
                                       'background check, license verification, liability coverage in the '
                                       "renter's name, card ownership, deposit, and in-person pickup. Note "
                                       'what single failure cancels a handoff on the spot.',
                             'example': 'Etienne Elsaesser calls renter-side liability bound in the '
                                        "renter's own name non-negotiable [Etienne Elsaesser — amfsF8yd5hg "
                                        '@ 00:08:56]. King of Rentals takes payment only on a card in the '
                                        "renter's name, never a Zelle on their word [King of Rentals — "
                                        'qwQ8yQbhunw @ 01:09:58], and Alex Auto matches face to license in '
                                        'person [Alex Auto — Q9fRvJfTKk0 @ 00:06:22].'},
                            {'name': 'tracker_and_platform_approval',
                             'type': 'textarea',
                             'prompt': 'Specify the tracking hardware installed on every car before its '
                                       'first rental: number of trackers, kill switch, and remote cut-off. '
                                       'Then confirm each car is an approved rideshare option where you '
                                       'live, and record how you verified it.',
                             'example': 'Alex Auto warns that without trackers and kill switches you will '
                                        'lose your car [Alex Auto — bHUp-OA4bH8 @ 00:08:40]. darius '
                                        'benders runs two trackers per car, sometimes three, with a remote '
                                        'cut-off [darius benders — NFLtPz5bUp4 @ 00:13:20]. RevHostHQ says '
                                        'check that the car is an approved option where you live before a '
                                        'driver logs in [RevHostHQ — 3jfvZ2LM8zM @ 00:00:52].'}],
                 'completion_gate': 'This worksheet is complete only when a day-rate price sheet exists, '
                                    'ten named referral partners have been contacted, every reservation '
                                    'lives in one booking system, and each rental car shows a written net '
                                    'figure, tracker with kill switch, and platform approval check.'},
                {'worksheet_id': 'ws-04',
                 'number': 4,
                 'title': 'Off-Platform Rentals and Co-Hosting Arbitrage Planner',
                 'purpose': 'Turn cheap cash-bought economy cars into weekly gig-driver rentals that pay '
                            'back inside 90 days. Then decide whether, and on what written terms, you will '
                            "manage other owners' cars for a cut of gross revenue.",
                 'chapter_ref': 'Q7-Q8',
                 'instructions': ['Complete every field using real numbers from cars you own, are buying '
                                  'this month, or have priced on Facebook Marketplace.',
                                  'Run the 90-day payback test on each car before you list it, and drop '
                                  'any car that misses the target.',
                                  'Cite the practitioner benchmark beside each number you commit to so you '
                                  'can audit the logic later.',
                                  'Finish the private rental fields before touching the co-hosting fields, '
                                  'because owner cars come after your own operating record.',
                                  'Put every co-hosting term into a signed written agreement before an '
                                  'owner hands you keys.'],
                 'fields': [{'name': 'weekly_rate_band',
                             'type': 'text',
                             'prompt': 'Write the weekly rate you will charge on each cash-bought economy '
                                       'car in your private rental lineup, including the purchase price, '
                                       'the planned all-in cap, and the reason your number sits inside or '
                                       'outside the band that practitioners quote.',
                             'example': '2014 Corolla bought for $3,800 cash, all-in cap of $6,000 after '
                                        'tires and brakes, listed at $400 per week. Kel King prices '
                                        '$350-450 per week on $3K-4K cars [Kel King — BD6Xfj5F-Fk @ '
                                        '00:11:47], so $400 sits mid-band, leaving room to open higher on '
                                        'newer units and still undercut nearby rideshare rental lots.'},
                            {'name': 'payback_clock',
                             'type': 'text',
                             'prompt': 'Calculate how many days each car needs to return its full purchase '
                                       'price at your weekly rate, then mark whether it clears the 90-day '
                                       'rule, and name the specific car you would refuse to buy because it '
                                       'fails.',
                             'example': 'Corolla at $3,800 renting for $400 weekly returns its price in '
                                        'roughly 67 days, clearing the 90-day golden rule [Kel King — '
                                        '7l7A5buuie0 @ 00:41:31]. A financed $14,000 Camry at the same '
                                        'rate would need about 245 days, so it is rejected; Alex Auto '
                                        'names financing the first car as the very first mistake [Alex '
                                        'Auto — G-0j82EXJlk @ 00:01:46].'},
                            {'name': 'private_vs_turo_math',
                             'type': 'textarea',
                             'prompt': 'Lay out the monthly revenue, monthly costs, and net profit for one '
                                       "car rented privately to gig drivers, then set the same car's "
                                       'expected Turo net beside it and explain which channel you will '
                                       'build around and why.',
                             'example': 'Private channel: $1,500 monthly revenue minus about $500 in costs '
                                        'leaves $1,000 net per car, against roughly $500 on Turo [King of '
                                        'Rentals — DOrgMXhPDXs @ 00:07:36]. Rideshare renters hold cars '
                                        'about 60 days versus 3 days for Turo guests, cutting cleaning '
                                        'turns sharply [King of Rentals — DOrgMXhPDXs @ 00:04:23]. '
                                        'Decision: build around weekly private renters.'},
                            {'name': 'marketplace_lead_post',
                             'type': 'textarea',
                             'prompt': 'Draft the exact title and body of your free Facebook Marketplace '
                                       'listing, including the features you promise renters, the '
                                       'walkaround video you will attach, and the second lead channel you '
                                       'will run alongside it to keep inquiries steady.',
                             'example': "Title: 'cars for rideshare.' Body: unlimited miles, insurance "
                                        'included, maintenance included, plus a full walkaround video, '
                                        'with wording kept exactly as taught and never remixed [Kel King — '
                                        'UCJIebqFEj0 @ 00:13:53]. Second channel: a Google Business '
                                        'profile and a $10/day Messenger ad, with inquiries screened by a '
                                        '$3-5/hr overseas VA before any call is booked.'},
                            {'name': 'car_inspection_buy',
                             'type': 'textarea',
                             'prompt': 'Describe the inspection routine you will run on every used economy '
                                       'car before paying cash, including the fluids you check, the '
                                       'warning signs that end the deal, and how you will use needed '
                                       'repairs to negotiate the price down.',
                             'example': 'Pull the dipstick and oil cap on every Ford Fusion; creamy oil '
                                        'means a blown head gasket and an instant walk-away. On clean '
                                        'cars, itemize every needed repair to the seller line by line to '
                                        'drive the price down [Demario Mccowan — -HtlfCgxxtg @ 01:27:39]. '
                                        'Skip the auction lane entirely and source locally instead [Kel '
                                        'King — BD6Xfj5F-Fk @ 00:13:53].'},
                            {'name': 'deposit_payment_rules',
                             'type': 'textarea',
                             'prompt': 'Set your deposit amount, first-payment method, accepted payment '
                                       'rails, minimum renter age, and the rental agreement clauses you '
                                       'will enforce, noting where practitioners disagree on card payments '
                                       'and how your policy resolves that disagreement for every renter.',
                             'example': 'Flat $300 deposit plus the first week up front, renters 23 and '
                                        'older only [Demario Mccowan — taXFg2qEMew @ 00:35:57]. First '
                                        'payment by Zelle or ACH with a $1 hold on a card kept on file, '
                                        'since card disputes are a 50/50 [Car Rental Coach — sP0LfwE7elc @ '
                                        '00:27:50]. Agreement includes $250 smoking and $200 cleaning '
                                        'fees.'},
                            {'name': 'insurance_stance',
                             'type': 'textarea',
                             'prompt': 'State which insurance structure you will run on private rentals, '
                                       'personal policy with permissible-driver framing or commercial '
                                       'coverage, explain how you will keep your loss run report clean '
                                       'when a renter damages a car, and name the practitioner warning '
                                       'that settled your choice.',
                             'example': 'Commercial coverage that explicitly allows private rentals, bound '
                                        'before the first handoff. Mo got commercial insurance right off '
                                        'rip after a personal-policy rental totaled their car [Demario '
                                        'Mccowan — -HtlfCgxxtg @ 01:34:49]. Small damage gets paid out of '
                                        'pocket, and insurance only handles events outside my control, '
                                        'keeping the loss run clean [Demario Mccowan — -HtlfCgxxtg @ '
                                        '01:37:06].'},
                            {'name': 'cohost_split_terms',
                             'type': 'textarea',
                             'prompt': 'Write the co-hosting revenue split you will offer car owners, the '
                                       'base the percentage is calculated from, any monthly fee floor, and '
                                       'the document that will hold every term so nothing rests on a '
                                       'handshake with owners or partners.',
                             'example': '30% of gross or $400 per car per month, whichever is higher, '
                                        "mirroring Brandon Bartron's $398 per-car break-even [King of "
                                        'Rentals — xCgsQFz-kOM @ 00:02:46]. The cut comes off gross, never '
                                        'net, after net deals paid only $200-300 per car [Demario Mccowan '
                                        '— b4HG8nxaQlU @ 00:06:17]. Every fee lives in a signed written '
                                        'agreement.'},
                            {'name': 'owner_pitch_return',
                             'type': 'textarea',
                             'prompt': 'Build the owner-facing return example you will show a passive car '
                                       'investor, including vehicle cost, months on the platform, gross '
                                       'revenue, net, the owner share, and the annualized percentage, '
                                       'without promising future profit as guaranteed to that owner.',
                             'example': 'Reference case: a 2022 GMC Yukon grossed $14.5k over 8 months and '
                                        'netted $9,672; under a 70/30 split the owner received $6,770 on '
                                        '$44,680 invested, a 23% annualized return [Peak Auto Academy — '
                                        '3kqux9OEEfY @ 00:02:47]. My pitch shows this as a past result '
                                        'only, then walks the owner through deductibles, downtime, and '
                                        'claim timelines.'},
                            {'name': 'cohost_readiness_ops',
                             'type': 'textarea',
                             'prompt': "Confirm your readiness to run other people's cars by listing the "
                                       'cars you have personally operated, your weekly schedule '
                                       'flexibility, your partner-car shipping checklist, and your claim '
                                       'photo timing rule for every single returned trip on the platform.',
                             'example': 'Operated two of my own cars for six months first, since running '
                                        "someone else's car before that is irresponsible [Aubrey Janik — "
                                        'Yjwp4WMIjbc @ 00:03:51]. Shipping checklist: plates off and into '
                                        'the trunk to stop late toll tickets [Delano Green — C5WI_82-JuI @ '
                                        '00:03:51]. Photos uploaded within 24 hours, because 26-hour '
                                        'uploads are not covered [Delano Green — xTVl-1-TkSI @ '
                                        '00:13:38].'}],
                 'completion_gate': 'Every car on your list clears the 90-day payback test, has a written '
                                    'deposit and payment policy, and carries coverage that explicitly '
                                    'allows private rentals. No co-hosted car is accepted until you have '
                                    'operated your own cars and the owner has signed a gross-based written '
                                    'agreement.'},
                {'worksheet_id': 'ws-05',
                 'number': 5,
                 'title': 'Fleet Insurance and Asset Protection Audit',
                 'purpose': 'Close every coverage gap between personal, rideshare, rental, and commercial '
                            'policies before a claim exposes it, then lock each car down with a tracker '
                            'and kill switch setup matched to the renter risk it actually carries.',
                 'chapter_ref': 'Q9-Q10',
                 'instructions': ['Fill this worksheet with the actual quotes, declarations pages, and '
                                  'device invoices on your desk, not estimates.',
                                  "Run every candidate VIN past your insurer's underwriters before you pay "
                                  'a seller or dealer.',
                                  'Get each coverage confirmation in writing, with the endorsement or '
                                  "policy name, and file it with the car's records.",
                                  "Install and crank-test the tracker and kill switch before the car's "
                                  'first rental, never after.',
                                  'Revisit the insurance and tracker fields every renewal and every time a '
                                  'car changes renter profile.'],
                 'fields': [{'name': 'coverage_ladder_tier',
                             'type': 'text',
                             'prompt': 'Identify which rung of the coverage ladder each vehicle sits on '
                                       'today, from personal policy through rideshare endorsement, all-in '
                                       'rideshare insurance, and commercial, and write the monthly or '
                                       'yearly cost you were actually quoted for it.',
                             'example': 'Prius driven personally: rideshare endorsement in the $15 to $40 '
                                        'per month band, matching the example driver who paid an extra '
                                        "$340 a year on a $1,480 base premium [Freelancer's Wealth "
                                        'Blueprint — Hxl9pLAo8c0 @ 00:02:17]. Fleet cars: commercial, '
                                        'since a full-time operation is where $3 to $5,000 a year makes '
                                        'sense [The Rideshare Guy — F6U-c7e7avY @ 00:02:55].'},
                            {'name': 'premium_payment_plan',
                             'type': 'textarea',
                             'prompt': 'Record the full cash price of your commercial premium, the down '
                                       'payment the carrier requested, the APR and finance charges on any '
                                       'balance, and the method you will use to pay upfront instead of '
                                       'financing the policy.',
                             'example': 'Lancer quote for an Uber Black sedan: $8,161 cash price, $2,155 '
                                        'down, financed balance at 23.8 percent APR with $611 in finance '
                                        'charges [Khushnud Numonov — IqvMzwtwzrI @ 00:05:26]. Plan: pay '
                                        'upfront on a 0 percent APR card, absorbing a $340 card fee but '
                                        'earning $170 cash back, saving about $441 [Khushnud Numonov — '
                                        'IqvMzwtwzrI @ 00:10:07].'},
                            {'name': 'rental_fleet_policy',
                             'type': 'textarea',
                             'prompt': 'Choose the coverage model for your rental cars, Period X gap '
                                       'cover, a Lula fleet policy, or commercial liability with '
                                       'renter-paid damage waivers, and write the per-car monthly cost, '
                                       'the deductibles, and how renters will offset it.',
                             'example': 'Lula commercial fleet policy at about $130 per car per month at '
                                        'two cars, dropping under $100 at six to seven cars, with a $1,000 '
                                        'collision and $3,000 comprehensive deductible '
                                        '[Mike_Thebusinessman — XGJGK0LyMno @ 00:13:30]. Renters pay $30 '
                                        'per day for coverage, turning the premium into a profit line '
                                        '[Mike_Thebusinessman — XGJGK0LyMno @ 00:13:47].'},
                            {'name': 'underwriter_vin_check',
                             'type': 'text',
                             'prompt': 'Before buying the next fleet car, write the VIN you sent to the '
                                       "insurer's underwriters, the database they used to check title "
                                       'history, and the result, including whether the car was accepted, '
                                       'rejected, or flagged as salvage or rebuilt.',
                             'example': 'VIN sent to Lula underwriters, who ran it on their Black Book '
                                        'database rather than relying on Carfax or AutoCheck, which can '
                                        'miss salvage titles [Mike_Thebusinessman — XGJGK0LyMno @ '
                                        '00:15:12]. Result: rejected as salvage despite a clean dealer '
                                        'report, so the deal was canceled. For the Black SUV, the '
                                        'commercial quote also ran off the exact VIN first [TJackk — '
                                        'GBM9d0WqM-0 @ 00:20:42].'},
                            {'name': 'gap_and_dmv_check',
                             'type': 'textarea',
                             'prompt': 'List every coverage gap you have confirmed in writing, including '
                                       'Period 1 app-on waiting, contingent physical damage deductibles, '
                                       'coverage after a rental ends, and whether your policy reports '
                                       "insurance to the DMV to protect each car's registration status.",
                             'example': 'Platform contingent damage carries a $2,500 deductible and '
                                        'applies only if I hold comprehensive and collision [Fin Saint — '
                                        'kyXtImFfyxA @ 00:01:38]. Agent confirmed in writing, endorsement '
                                        'named, that app-on waiting and active trips are covered [Fin '
                                        'Saint — kyXtImFfyxA @ 00:04:36]. HyreCar coverage alone does not '
                                        'report to the DMV, so a separate policy is kept [Conrad Layn — '
                                        'ePOpmhuk-EQ @ 00:10:35].'},
                            {'name': 'claim_reserve_tax',
                             'type': 'textarea',
                             'prompt': 'Set the cash reserve you will hold for small accidents so the '
                                       'fleet never files an early claim, and explain how you will measure '
                                       'business-use percentage and handle the insurance deduction under '
                                       'your chosen mileage method.',
                             'example': 'Reserve of $3,000 held out of pocket so a thin fleet never files '
                                        'the early claim that gets it dropped [DGOTEXOTICS — 7d0XER3HAlQ @ '
                                        '00:08:33]. Odometer logged on January 1 and December 31, and the '
                                        "endorsement's dollar increase written down [Freelancer's Wealth "
                                        'Blueprint — Hxl9pLAo8c0 @ 00:07:03]. Standard mileage blocks any '
                                        'insurance deduction, so actual expenses are compared first.'},
                            {'name': 'tracker_choice',
                             'type': 'text',
                             'prompt': 'Name the tracker you will run in each car, plug-in Bouncie, '
                                       'hardwired Gold Star, or another unit, along with the device price, '
                                       'install cost, and monthly service fee, and justify the choice '
                                       "against that car's renter risk.",
                             'example': 'Rideshare rental Corollas: hardwired Gold Star with kill switch, '
                                        'about $600 for five units [Alex Auto — 6_-L6DOOZog @ 00:19:18], '
                                        'since an OBD plug-in alone can simply be unplugged [Alex Auto — '
                                        '6_-L6DOOZog @ 00:19:52]. Install budget $100 to $200 per device '
                                        'and service at $8 to $30 monthly [King of Rentals — 294HBi50ud8 @ '
                                        '00:06:17].'},
                            {'name': 'concealment_plan',
                             'type': 'textarea',
                             'prompt': 'Describe how you will conceal any plug-in tracker from renters, '
                                       'including the splitter or extension cable, the false-front port, '
                                       'and how you will secure the device so features like accident '
                                       'notification keep working reliably on every rental.',
                             'example': 'Backup Bouncie at $89 new or $60 to $70 used [King of Rentals — '
                                        'QpyPtquGmrk @ 00:00:11], hidden behind a $12 OBD2 splitter so '
                                        'renters reaching under the dash find a dead port. The device gets '
                                        'zip-tied firm at the end of the extension cable, because a loose '
                                        'unit may not send accident notifications [CentraliaUS — '
                                        'YflWar_YuYg @ 00:03:06].'},
                            {'name': 'hardwire_install_log',
                             'type': 'textarea',
                             'prompt': 'Log the hardwired install for each car, listing the constant 12V, '
                                       'ignition sense, and chassis ground sources, where the starter '
                                       'relay is spliced, how the trigger wire is protected, and the '
                                       'schematic source you checked before cutting.',
                             'example': 'Camry: constant 12V and ignition sense located with a multimeter, '
                                        'ignition lead pulled from the cigarette lighter since the radio '
                                        'harness was buried [Car Sharing Jho — 1_yscjNU-oM @ 00:08:58]. '
                                        "Wiring schematic confirmed through an O'Reilly commercial account "
                                        '[Pitstop to Profits — x4wy8hXqVbk @ 00:14:07]. Trigger wire '
                                        'crimped and heat-shrunk [Pitstop to Profits — x4wy8hXqVbk @ '
                                        '00:11:08].'},
                            {'name': 'kill_switch_test_policy',
                             'type': 'textarea',
                             'prompt': 'Write your kill switch testing routine and usage policy, covering '
                                       'the app crank test in both states before panels close, which '
                                       'renters and booking types require kill switch hardware, and '
                                       'whether keys stay in cars for verified renters.',
                             'example': 'Every install gets crank-tested from the app in both kill and '
                                        'unkill states before panels go back on [Wires747 — YbO6R8RKS_8 @ '
                                        '00:04:44]. Kill switches required on local rideshare renters and '
                                        'late-night airport bookings [King of Rentals — 294HBi50ud8 @ '
                                        '00:03:04]. Verified renters find keys inside, and the car is '
                                        'turned on remotely before pickup [Alex Auto — 6_-L6DOOZog @ '
                                        '00:21:41].'}],
                 'completion_gate': 'Every car has a written coverage confirmation naming the policy or '
                                    'endorsement, an underwriter-cleared VIN, a funded small-claim '
                                    'reserve, and a tracker that has passed a live kill and unkill crank '
                                    'test. Any car missing one of these stays parked.'},
                {'worksheet_id': 'ws-06',
                 'number': 6,
                 'title': 'Fleet Software Stack and Scaling Survival Blueprint',
                 'purpose': 'Own the booking pipe with software that cannot be switched off by a platform, '
                            'then prove your processes, team model, and unit economics can carry the next '
                            'block of cars before a single one is added.',
                 'chapter_ref': 'Q11-Q12',
                 'instructions': ['Answer each field with your current fleet numbers first, then the '
                                  'target you are building toward.',
                                  'Test your booking site end to end, from payment link to signed '
                                  'agreement, before you route renters to it.',
                                  'Write handover and verification steps as checklists a 1099 vendor could '
                                  'follow without calling you.',
                                  'Model profit at your next car-count milestone before buying, and name '
                                  'the assumption that breaks it.',
                                  'Freeze fleet growth until the broken process named in the final field '
                                  'is fixed and running clean.'],
                 'fields': [{'name': 'booking_platform_choice',
                             'type': 'text',
                             'prompt': 'Name the booking and rental management platform you will run off '
                                       'Turo, its monthly price at your current car count, any setup fee, '
                                       'and whether the plan caps vehicle count or staff accounts as you '
                                       'grow.',
                             'example': 'Fleetwire at about $20 a month for five cars, with two staff '
                                        'accounts and payment links, scaling to roughly $240-$250 at 150 '
                                        'cars [Alex Auto — 0Q8BZGkkigM @ 00:01:39]. HQ Rentals was ruled '
                                        'out over its $450 to $500 setup fee [Alex Auto — 0Q8BZGkkigM @ '
                                        '00:05:17] and the car cap that forced a migration '
                                        '[Mike_Thebusinessman — 1Va2FwAMf2A @ 00:06:27].'},
                            {'name': 'turo_dependency_exit',
                             'type': 'textarea',
                             'prompt': 'Describe how much of your booking flow still depends on Turo sync '
                                       'today, what breaks if Turo revokes access again, and the steps you '
                                       'will take to move guests and reviews onto your own direct booking '
                                       'site.',
                             'example': 'Calendar blocking and message automations ran through the '
                                        'unofficial API that Turo shut off for Fleetwire and CarSync '
                                        "[Fleet Brothers — VCL-xD3r5VU @ 00:01:08]. Fleetwire's owner "
                                        'sized about 25% of accounts as hybrid [Fleet Brothers — '
                                        'VCL-xD3r5VU @ 00:01:39]. Exit step: screenshot Turo testimonials '
                                        'and post them as images on the new booking site [DigiTree - '
                                        'Official — 9tsE8zvyMoY @ 00:02:33].'},
                            {'name': 'deposit_hold_rules',
                             'type': 'textarea',
                             'prompt': 'Write your deposit handling rules by rental length, stating when '
                                       'you hold a deposit on Stripe without charging it, when you capture '
                                       'it or take cash instead, and the merchant fee you avoid or accept '
                                       'in each case.',
                             'example': 'Rentals under seven days: deposit held on Stripe, not charged, '
                                        'dodging the 2.7 to 2.8 percent merchant fee [Mike_Thebusinessman '
                                        '— 1Va2FwAMf2A @ 00:16:47]. Rentals longer than seven days: '
                                        'deposit captured upfront or taken in cash, because the Stripe '
                                        'hold falls off on the seventh day [Mike_Thebusinessman — '
                                        '1Va2FwAMf2A @ 00:17:13].'},
                            {'name': 'handover_evidence',
                             'type': 'textarea',
                             'prompt': 'Define the evidence you capture at every handover and return, '
                                       'including odometer, fuel level, and condition photos, how the '
                                       'signed agreement reaches both parties, and the fluid checks done '
                                       'before a car goes back out to renters.',
                             'example': 'Odometer, fuel, and condition photos at every handover, with the '
                                        'signed agreement and photos sent to both parties [Web Development '
                                        'Experts — uwU6N7flfU8 @ 00:01:50]. Every returned car is opened '
                                        'for oil, coolant, washer fluid, and wipers before relisting [Car '
                                        'Rental Coach — lOTgf5qQVJ8 @ 00:02:35]. Listings include color '
                                        'and plate to separate identical models [Brandon Duff — '
                                        'c8x4Whu0UNg @ 00:05:36].'},
                            {'name': 'guest_insurance_verification',
                             'type': 'textarea',
                             'prompt': 'Write the guest verification script you will follow before '
                                       'releasing any car, covering payment before reservation, the '
                                       'separate coverage lines you verify, the questions you ask the '
                                       "guest's insurer directly, and the document you require on file.",
                             'example': 'No reservation without payment; liability, comprehensive, and '
                                        'collision verified separately, and the security deposit taken on '
                                        'rental day [Etienne Elsaesser — 3dvvSrh_cus @ 00:06:44]. Call the '
                                        "guest's insurer directly, confirm the policy is not brand new, "
                                        'ask about exclusions, and pull a binder before release [Etienne '
                                        'Elsaesser — VUKM00PHEmI @ 00:25:20]. No binder means the keys '
                                        'stay put.'},
                            {'name': 'utilization_target',
                             'type': 'text',
                             'prompt': 'Write your current fleet utilization, your target utilization, and '
                                       'the effective number of cars actually working, then name the '
                                       'channel shift or pricing change you will use to close the gap '
                                       'between the two utilization figures this quarter.',
                             'example': 'Current: 10 cars at 60% utilization, really only running six, '
                                        'just as a 50-car fleet at 60% is really only running 30 cars '
                                        '[Bluebird Auto Rental Systems — 1Bh5Wvanfss @ 00:01:34]. Target: '
                                        '84%, the average King of Rentals hit after shifting to roughly '
                                        '60-day rideshare rentals versus 65-70% on Turo [King of Rentals — '
                                        'NQzlTWjz8a0 @ 00:06:38].'},
                            {'name': 'vendor_team_model',
                             'type': 'textarea',
                             'prompt': 'Describe how cleaning, delivery, and repair work will get done '
                                       'without you, including whether you hire employees or pay 1099 '
                                       'vendors per job, what the operations manager may approve alone, '
                                       'and your weekly check-in hours as owner.',
                             'example': 'No employees; every cleaner, driver, and mechanic is a 1099 '
                                        'vendor paid per job [Etienne Elsaesser — 3dvvSrh_cus @ 00:20:01] '
                                        '[Etienne Elsaesser — 3dvvSrh_cus @ 00:09:28]. The operations '
                                        'manager can only approve things already approved before [Delano '
                                        'Green — ziuX0-egB7Y @ 00:06:33]. Owner reviews on Mondays, since '
                                        'the late shift otherwise runs till midnight [Russ Unlocked — '
                                        'y_X4A98Zuec @ 00:24:47].'},
                            {'name': 'scale_economics_model',
                             'type': 'textarea',
                             'prompt': 'Model your fleet at your next size milestone, listing car count, '
                                       'revenue, total costs, resale loss, operating profit, margin, and '
                                       'lot overhead per car, and mark which single assumption would wipe '
                                       'out the profit if wrong.',
                             'example': 'Benchmark: 100 cars at $28K, 80% financed at 6%, 75% utilization '
                                        'at $55/day plus $18/day extras, about $2M revenue and $240K '
                                        'operating profit at a 12% margin, with a $230K resale loss in the '
                                        'model [Money Prism — tNUrWA8I5bI @ 00:19:23]. Lot overhead runs '
                                        '$50 per car at 20 cars [King of Rentals — by_FGx_s0B0 @ '
                                        '00:04:58]. Fragile assumption: resale value.'},
                            {'name': 'turo_account_safety',
                             'type': 'textarea',
                             'prompt': 'List the platform settings and habits that protect your host '
                                       'account from a ban, including how you handle trips you cannot '
                                       'fulfill, your minimum discount settings, and how much revenue you '
                                       'still give a middleman each month.',
                             'example': 'Never cancel from the host side; two or three host cancellations '
                                        'can get the account banned, so Turo gets a phone call and cancels '
                                        'instead [Etienne Elsaesser — VUKM00PHEmI @ 00:07:36]. Minimum '
                                        'discount settings stay on. Middleman share currently sits near '
                                        'the 25 to 30% of revenue Private Keys reports giving away '
                                        '[Private Keys — LI8272h_0Ns @ 00:08:49].'},
                            {'name': 'process_before_scale',
                             'type': 'textarea',
                             'prompt': 'Name the broken process you must fix before adding another car, '
                                       'the evidence showing it is broken, the fix you will install, and '
                                       'the in-house repair or purchasing upgrade you will make once the '
                                       'fleet justifies it.',
                             'example': 'Broken process: returns sit unchecked for two days. Adding cars '
                                        'to a bad process just adds fuel to the fire [King of Rentals — '
                                        '706e4cdleYQ @ 00:00:22]. Later upgrade: a $10K pop-up building on '
                                        'a $10K cement pad with a lift and part-time mechanic, which saved '
                                        'over $60-70K in repairs [Car Rental Coach — lOTgf5qQVJ8 @ '
                                        '00:12:08].'}],
                 'completion_gate': 'Your booking site takes payment, issues signed agreements, and blocks '
                                    'double bookings without any Turo sync. Handover and guest '
                                    'verification checklists run without you, the next-milestone profit '
                                    'model survives a bad resale year, and the named broken process is '
                                    'fixed before another car is bought.'}]}
