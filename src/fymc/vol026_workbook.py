from __future__ import annotations

def build_volume_026_workbook() -> dict:
    return {'workbook_id': 'wb-026-government-surplus-auctions',
 'volume_id': 'vol-026-government-surplus-auctions',
 'title': 'Government Surplus Auctions — Practitioner Testimony Operator Workbook',
 'subtitle': 'A field workbook for finding government surplus sales, reading real hammer prices, bidding '
             'on fleet vehicles, heavy iron, and GovPlanet Humvees, and turning SF-97s, titles, fees, and '
             'freight into a true all-in cost before the clock runs out',
 'worksheets': [{'worksheet_id': 'ws-01',
                 'number': 1,
                 'title': 'Sale Source Map and Fleet Vehicle Bid Sheet',
                 'purpose': 'Build a working map of every city, county, state, and federal sale channel '
                            "within reach, convert each platform's fees into a hard multiplier, and run "
                            'every fleet car, truck, or police unit through inspection, paperwork, pickup, '
                            'and ceiling checks before a single bid is placed.',
                 'chapter_ref': 'Q1-Q2',
                 'instructions': ['Start with the platform map and fee stack, because a lot that looks '
                                  'cheap on one site can cost far more than an identical unit on another '
                                  'once premiums and wire fees land.',
                                  'Pull archived sold prices before you look at the current bid, and '
                                  'separate keyed from keyless comps so the averages are not distorted by '
                                  'vehicles that cannot be driven away.',
                                  'Read the full terms of sale and confirm the removal window and legal '
                                  'exit method for every lot, since a missed deadline can cost both the '
                                  'vehicle and the account.',
                                  'Complete the inspection checklist in person or through an allowed '
                                  'outside inspector, and record every seller question and answer posted '
                                  'on the listing.',
                                  'Write the maximum bid in ink before the closing window opens, and treat '
                                  'any lot that passes that number as already gone, because another sale '
                                  'follows next week.'],
                 'fields': [{'name': 'platform_map',
                             'type': 'textarea',
                             'prompt': 'List every government sale channel within your pickup radius, '
                                       'including city, county, state, and federal sources, and note which '
                                       'platform each agency actually uses, because neighboring '
                                       'jurisdictions often sell through completely different sites and '
                                       'missing one platform means missing whole inventories.',
                             'example': 'Delaware, New Castle County, and Wilmington each sold through a '
                                        'different platform, and one county lot became a potential honey '
                                        'hole once a maintenance supervisor shared which cars were slated '
                                        'for upcoming auctions [East Coast Classics — q09PUtJPIxs @ '
                                        '00:11:03]. My map lists GSA Auctions, GovDeals, Public Surplus, '
                                        'and Municibid, each checked twice weekly.'},
                            {'name': 'fee_stack',
                             'type': 'textarea',
                             'prompt': "For each platform on your map, record the buyer's premium, "
                                       'registration fee, wire or card fees, and card limits, then '
                                       'calculate the true multiplier you will apply to any hammer price '
                                       'before you decide how high to bid on a lot.',
                             'example': 'GovDeals premiums run 5% to 12.5% depending on the municipality '
                                        '[East Coast Classics — q09PUtJPIxs @ 00:04:12]. US Gov Bid '
                                        'charges a one-time $100 registration plus a $60 wire fee, while '
                                        'Public Surplus holds part of any bid above $500 and caps card '
                                        'purchases at $4,000. My worst-case GovDeals multiplier is 1.125 '
                                        'on every hammer.'},
                            {'name': 'historical_price_research',
                             'type': 'textarea',
                             'prompt': 'Pull past sold prices for the exact make, model, and year you are '
                                       'targeting from archived auctions, and write down at least five '
                                       'comparable results with dates, so your maximum bid rests on actual '
                                       'hammer history rather than hopeful guesses.',
                             'example': 'Search US Gov Bid past auctions going back years to pull selling '
                                        'prices on everything sold before setting a max [East Coast '
                                        'Classics — q09PUtJPIxs @ 00:03:24]. In Norfolk, keyed vehicles '
                                        'carried a $1,300 middle price versus $550 without keys [UX '
                                        'Auctions — Z87d62pWVEk @ 00:08:33]. My note: filter comps by key '
                                        'status before averaging anything.'},
                            {'name': 'closing_window_watch',
                             'type': 'text',
                             'prompt': 'Record the scheduled end day and time for every lot you are '
                                       'watching, note whether soft-close extensions apply, and flag '
                                       'clusters of closings, since agencies stagger end times and you '
                                       'need to be present when your target lots actually close.',
                             'example': 'GovDeals tells agencies to run 7 to 10 days, end Monday through '
                                        'Thursday in the afternoon or evening, avoid weekends and '
                                        'holidays, and stagger end times at least 10 minutes apart '
                                        '[GovDeals Media — Q4B13yVVzZQ @ 00:01:11]. GSA color codes '
                                        'alerts: yellow at 1 to 2 hours remaining, red under one hour [GSA '
                                        '(General Services Administration) — csOCrIHnuSo @ 00:01:47].'},
                            {'name': 'terms_of_sale_check',
                             'type': 'textarea',
                             'prompt': 'Read the full terms of sale for each target lot and record the '
                                       "payment method and deadline, the buyer's premium, the pickup "
                                       'window, and whether you receive a title or only a bill of sale, '
                                       'before placing any bid at all.',
                             'example': 'Terms of sale are where people get burned, so payment method, '
                                        'deadline, premium, pickup window, and title versus bill of sale '
                                        'all get checked first [UX Auctions — Z87d62pWVEk @ 00:06:20]. '
                                        'Miss the payment deadline and you can lose the vehicle, and some '
                                        'sites block you from bidding again [UX Auctions — Z87d62pWVEk @ '
                                        '00:17:24]. Lot status: title confirmed.'},
                            {'name': 'removal_logistics',
                             'type': 'text',
                             'prompt': 'Document the removal window in days, the legal way the vehicle '
                                       'leaves the lot by temporary tag or tow, who is driving or hauling '
                                       'it, and the storage or account penalties that apply if you miss '
                                       'the scheduled weekday pickup.',
                             'example': 'Removal windows ran from seven days down to two, so confirm '
                                        'temporary tag or tow before bidding [East Coast Classics — '
                                        'q09PUtJPIxs @ 00:06:23]. Print the buyer certificate and confirm '
                                        'the weekday pickup window, because no-shows lock the account '
                                        'while storage accrues [Junk Solutions Experts LLC — El3cLMGi_9s @ '
                                        '00:05:01]. My plan: borrowed trailer reserved for Tuesday '
                                        'morning.'},
                            {'name': 'preview_inspection',
                             'type': 'textarea',
                             'prompt': 'Write your inspection checklist for preview day, covering tires, '
                                       'OBD codes, door stickers, frame rust, flood signs, and VIN match, '
                                       'and note whether the yard allows outside inspectors if you cannot '
                                       'attend the fixed preview window in person.',
                             'example': 'Walk away from frame rust you can poke through, a musty smell, '
                                        'damp carpet, a water line, or a VIN that does not match the '
                                        'listing [UX Auctions — Z87d62pWVEk @ 00:11:50]. Never check just '
                                        'one tire [UX Auctions — IUAs4NGQfyo @ 00:00:19]. Pull codes '
                                        'yourself and walk from any unit whose OBD port is dead [Auto '
                                        'Dealer Startup — dzr9aYx98oY @ 00:11:30].'},
                            {'name': 'vin_history_and_questions',
                             'type': 'textarea',
                             'prompt': 'Record the VIN for each target unit, the result of a paid vehicle '
                                       'history report, and every question you posted to the seller on the '
                                       'listing, along with the answers, so condition guesses from photos '
                                       'are replaced with documented facts.',
                             'example': 'Pay the $12 to $15 fee for the VIN history [Top 5 Autos — '
                                        'WFVGJDWST7I @ 00:04:44]. Ask the seller directly on the listing '
                                        'instead of guessing from photos [UX Auctions — IUAs4NGQfyo @ '
                                        '00:05:15]. A 2006 F-250 from the Southport fire department showed '
                                        '157,119 miles at onsite inspection. State employees list every '
                                        'tiny leak, so take it with a grain of salt.'},
                            {'name': 'max_bid_ceiling',
                             'type': 'text',
                             'prompt': 'Set a written maximum bid for each lot using KBB value minus '
                                       "repair costs, sales tax, buyer's premium, and shipping, then state "
                                       'exactly what you will do when bidding passes that number, '
                                       'including during soft-close extensions and last-minute bidding '
                                       'wars.',
                             'example': "Price in sales tax, buyer's premiums, and shipping, then set a "
                                        'firm maximum and stick to it [The Salmon Runs — jaeWKn_Nu68 @ '
                                        '00:00:52]. Take your number, write it down, and if bidding passes '
                                        "it, let it go, because there's another sale next week [UX "
                                        'Auctions — Z87d62pWVEk @ 00:13:51]. Bidding wars are how prices '
                                        'get out of control.'},
                            {'name': 'value_angle',
                             'type': 'textarea',
                             'prompt': 'Identify the specific angle that makes this lot underpriced, such '
                                       'as scary photos, an unpopular color, a missing key, or a cosmetic '
                                       'fault, and estimate the realistic spread between your all-in cost '
                                       'and a conservative resale or KBB figure.',
                             'example': 'A black Explorer brought $6,600 while identical white units sold '
                                        'around $5,000 [Street Rat Garage — 6chXsHCTJA4 @ 00:11:02]. A '
                                        'former fire-rescue Expedition bought for $900 over an engine '
                                        'noise landed near $2,000 cash in against a KBB of $5,000 to '
                                        '$5,500 [Tool Demos — EFXJtp6q_B8 @ 00:08:56]. My angle: terrible '
                                        'wheel-off photos that scare off other bidders.'}],
                 'completion_gate': 'Do not bid until every channel on the map has a recorded fee '
                                    'multiplier, the terms of sale confirm payment deadline, pickup '
                                    'window, and title type, the inspection checklist is filled in, and a '
                                    'written maximum bid sits beside the lot number with a plan for '
                                    'walking away.'},
                {'worksheet_id': 'ws-02',
                 'number': 2,
                 'title': 'Hammer Price Comp Log and Heavy Iron Inspection Sheet',
                 'purpose': 'Anchor every bid to what government pickups, SUVs, ex-police units, and heavy '
                            'equipment actually hammered for, separate fleet iron from consignment, and '
                            'price hidden defects, robbed parts, and freight at their worst case, because '
                            'the profit on iron is locked in at the hammer, not at resale.',
                 'chapter_ref': 'Q3-Q4',
                 'instructions': ['Log at least ten real hammer prices for the class you are targeting, '
                                  'recording sale type and seller agency, and never mix asking prices into '
                                  'the comp set.',
                                  'Separate government-titled fleet units from private consignment using '
                                  'concrete evidence such as tires, retirement reason, and listing source '
                                  'before trusting any condition claim.',
                                  'Record whether each sale is absolute, reserved, or no-reserve, along '
                                  'with fees and same-day pickup rules, because those terms change how '
                                  'hard you can afford to push.',
                                  'On heavy equipment and military trucks, crawl under, check the hour '
                                  'meter and valve cover, and run a missing-parts census priced with '
                                  'shipping included.',
                                  'Convert every unknown leak or defect into its worst-case repair cost, '
                                  'subtract the total from your ceiling, and log the actual hammer '
                                  'afterward to measure discipline.'],
                 'fields': [{'name': 'comp_log',
                             'type': 'textarea',
                             'prompt': 'Log at least ten real hammer prices from government sales for the '
                                       'vehicle class you are targeting, recording year, model, mileage '
                                       'where known, sale type, and seller agency, so your bid ceiling '
                                       'reflects what iron actually brought rather than asking prices.',
                             'example': 'At a Florida government sale, a 2018 Chevrolet Silverado hammered '
                                        'at $6,750, a 2014 Silverado at $3,200, and a 2012 Chevrolet at '
                                        '$3,200 [Auction Reviews With Jeff — P82Ir2OeO50 @ 00:01:43]. '
                                        'Ex-cop Chargers and Impalas landed between $3,000 and $4,000. My '
                                        'log groups every comp by year, mileage, and whether the seller '
                                        'was an agency.'},
                            {'name': 'government_vs_consignment',
                             'type': 'text',
                             'prompt': 'For each lot, note whether it is government-titled fleet iron or '
                                       'private consignment, and record the evidence you used, such as '
                                       'tire condition, listing source, or retirement reason, because '
                                       'fleet units usually retire on mileage or age with mandated '
                                       'maintenance.',
                             'example': "Agencies do not get rid of these because there's a problem; they "
                                        'retire them at a certain mileage or number of years [Auction '
                                        'Reviews With Jeff — cZOfyxWtGp8 @ 00:16:49]. Tires in really good '
                                        'shape usually mark a government vehicle, because agencies keep '
                                        'them replaced [Auction Reviews With Jeff — 3ej4xfd_ers @ '
                                        '00:04:48]. Lot verdict: government unit, new tires.'},
                            {'name': 'sale_type_and_fees',
                             'type': 'text',
                             'prompt': 'Record whether the sale is absolute, reserved, or no-reserve, the '
                                       'buyer fee percentage, and any same-day pickup rule, then note how '
                                       'each condition changes your willingness to bid, since absolute '
                                       'sales award the lot to the high bidder regardless.',
                             'example': 'One sale carried no buyer fees, but cars had to be picked up the '
                                        'day of the sale [Auction Reviews With Jeff — E3mh6G6h8zM @ '
                                        '00:13:44]. Another was an absolute auction where the higher '
                                        'bidder gets it no matter what [Auction Reviews With Jeff — '
                                        '6-YX9_QfY1A @ 00:08:57]. Fees ran from zero at the GSA Orlando '
                                        'sale to 2% on some agency lots.'},
                            {'name': 'live_day_discipline',
                             'type': 'textarea',
                             'prompt': 'Before a live auction day, write each target lot number with its '
                                       'ceiling beside it, then afterward record the actual hammer, '
                                       'whether you bid, and whether the room ran past your number, so you '
                                       'can measure discipline across multiple sales.',
                             'example': 'At the New Hampshire state surplus live auction day, a '
                                        'two-wheel-drive Ranger hammered at $2,750 against a personal '
                                        'ceiling just under $2,000 [Sean Drake — ovCY1VA7klw @ 00:02:13]. '
                                        'Bid only on what you need or can make money on, and do not go a '
                                        'little crazy [Sean Drake — ovCY1VA7klw @ 00:10:15]. Result: '
                                        'passed, ceiling held.'},
                            {'name': 'timing_and_damage_angle',
                             'type': 'text',
                             'prompt': 'Note the calendar month of each target sale and any cosmetic '
                                       'damage on otherwise identical units in the same row, then explain '
                                       'whether timing or visible dings give you a realistic chance of '
                                       "buying below the cluster's typical hammer price.",
                             'example': 'Prices tend to run a little lower at the end of the year, '
                                        'November and December and sometimes October, which flags a '
                                        'December sale as a buying window [Auction Reviews With Jeff — '
                                        'iauTGRI39kE @ 00:11:24]. A Tahoe with a little body damage should '
                                        'hammer lower than its clean siblings in the same row [Retired and '
                                        'Winging it — pl4wTzpNWRQ @ 00:19:47].'},
                            {'name': 'cab_check_and_codes',
                             'type': 'textarea',
                             'prompt': "List what you checked from the driver's seat and under the hood "
                                       'for each vehicle, including start behavior, scanner codes, ports, '
                                       "and the posted as-is buyer's guide, and mark any listed issue you "
                                       'are not equipped to repair yourself.',
                             'example': 'Crank it, sit in it, and pull the codes, which a scanner under '
                                        '$100 handles [Auction Reviews With Jeff — E3mh6G6h8zM @ '
                                        "00:21:53]. Read the as-is buyer's guide Florida law requires on "
                                        'each unit [Auction Reviews With Jeff — YaIalHq0RVU @ 00:40:41]. '
                                        'On ex-police Tahoes, USB ports were disconnected and reconnecting '
                                        'them still did not restore charging.'},
                            {'name': 'iron_inspection',
                             'type': 'textarea',
                             'prompt': 'For heavy equipment, record the hour meter against the sale bill, '
                                       'the condition of the unpainted underside, signs of fresh respray '
                                       'such as shiny DOT tape, spray-in bed liner, and what you found '
                                       'under the valve cover, since fresh paint up top proves nothing.',
                             'example': "Crawl under and check the unpainted underside for the 'Richie "
                                        "Brothers overhaul,' because fresh paint up top proves nothing "
                                        '[Casey LaDelle — XAvSq6gx5KQ @ 00:19:39]. Cross-check the hour '
                                        'meter against the sale bill and look under the valve cover; '
                                        'sludge means cheap or not at all [Welding and Wheeling — '
                                        'UpuweWTtiG4 @ 00:41:28]. Spray-in liner can hide festering rust.'},
                            {'name': 'worst_case_repair_math',
                             'type': 'textarea',
                             'prompt': 'For every unknown leak, missing part, or warning sign on the lot, '
                                       'write the worst-case repair cost rather than the cheapest fix, '
                                       'total those figures, and lower your bid cap by that full amount '
                                       'before the auction opens.',
                             'example': 'Price every unknown leak as a roughly $10,000 valve body rather '
                                        'than an O-ring, and lower the cap to match [Casey LaDelle — '
                                        'XAvSq6gx5KQ @ 00:13:36]. A projected $20,000 profit on a Landoll '
                                        'trailer shrank to about $280 once hidden defects surfaced [Casey '
                                        'LaDelle — XAvSq6gx5KQ @ 01:04:09]. My reserve: $10,000 per '
                                        'unexplained drip.'},
                            {'name': 'military_parts_census',
                             'type': 'textarea',
                             'prompt': 'For military trucks and equipment, list every robbed or missing '
                                       'component, including ECUs, doors, glass, and turret caps, with a '
                                       'sourcing note and price for each, then add shipping so the true '
                                       'landed cost appears before you bid.',
                             'example': 'ECUs, doors, glass, and turret caps get robbed, and the doors '
                                        'alone cost $6,000 [iron king productions — vlBL3apKXg0 @ '
                                        '00:20:30]. An LMTV M1087 won at $800 cost about $1,000 with fees '
                                        'plus $5,000 shipping from Hawaii [iron king productions — '
                                        'vlBL3apKXg0 @ 00:07:14]. Marketplace turned up a $4,000 CAT ECM '
                                        'for $600, so hunt discontinued parts there.'},
                            {'name': 'ironplanet_channel_choice',
                             'type': 'text',
                             'prompt': 'Compare the IronPlanet channels open to you, including no-reserve '
                                       'live bidding, inspected online listings, and Make Offer, and '
                                       'record how payment, release, and fees work for each, plus how you '
                                       'will respond if an offer haggle drags on.',
                             'example': 'In no-reserve live bidding the highest bidder wins no matter the '
                                        'price, with no time extensions [IronPlanet — -1B3hGKjbz0 @ '
                                        '00:01:05]. The buyer pays into a secure account and the seller '
                                        "releases to the buyer's transporter [IronPlanet — KyKSH6vNrZ8 @ "
                                        '00:01:46]. A 2015 Silverado listed at 14,500 closed near $9,100 '
                                        'after a multi-round Make Offer haggle.'}],
                 'completion_gate': 'Do not bid until the comp log holds at least ten real hammer prices, '
                                    'the lot is classified as fleet or consignment with evidence, sale '
                                    'type and fees are recorded, every unknown defect carries a worst-case '
                                    'cost, and the adjusted ceiling is written next to the lot number.'},
                {'worksheet_id': 'ws-03',
                 'number': 3,
                 'title': 'GovPlanet Humvee Buy, Title Path, and True Build Cost Ledger',
                 'purpose': 'Carry a GovPlanet Humvee from bidding approval through listing screening, '
                            'overtime discipline, invoice and transport, first start, and title paperwork, '
                            'then total every line from winning bid to fully built truck, so the real cost '
                            'of a street-legal unit is known before the auction ends.',
                 'chapter_ref': 'Q5-Q6',
                 'instructions': ['Confirm bidding approval and plan the calendar around end-use '
                                  'certificate clearance, pickup windows, and SF-97 timing before you '
                                  'watch a single closing.',
                                  'Screen every listing on engine type, start clip, blow-by, and wear, and '
                                  'filter sold results for configurations that draw fewer bidders and '
                                  'lower hammers.',
                                  'Write the walk-away number before the close and hold it through every '
                                  '30-second overtime extension, because the auction is not won when the '
                                  'clock first hits zero.',
                                  'Project the full invoice and transport quote, then plan the first start '
                                  'from slave cable to glow plugs before tearing into a listed non-runner.',
                                  'Verify the ownership document, DMV acceptance, and insurer coverage, '
                                  'then total the bare-bones and fully built cost with a dedicated repair '
                                  'reserve included.'],
                 'fields': [{'name': 'bidding_approval_status',
                             'type': 'text',
                             'prompt': 'Record your GovPlanet bidding approval status, the date you were '
                                       'approved, any documents requested, and the end-use certificate '
                                       'requirements, so you know how long you must wait between winning a '
                                       'truck and actually being cleared to remove it.',
                             'example': 'A Marine Corps Humvee bought in October did not clear its end-use '
                                        'certificate until January, using all 12 weeks [Split Builds — '
                                        'CkfJvTDwa2w @ 00:01:49]. Another buyer reported 3-5 months of EUC '
                                        'approval with no storage fees, then about 2 weeks to pick up '
                                        '[Kevin24Seven — k5WD_GKlQhs @ 00:25:16]. My calendar assumes the '
                                        'longest wait.'},
                            {'name': 'listing_screen',
                             'type': 'textarea',
                             'prompt': 'Screen each Humvee listing by engine type, start clip behavior, '
                                       'blow-by at the radiator cap or oil filler, and wear on pedals and '
                                       'switches, and write the specific reason each truck passes or fails '
                                       'your screen before you watch its auction.',
                             'example': 'Mist coming out of the radiator cap at idle means an engine '
                                        'issue, and a healthy truck costs no more at auction [Kevin24Seven '
                                        '— gtS8l93r5cw @ 00:04:18]. A healthy 6.5 fires on the first crank '
                                        'with a smooth idle; a hard start can mean glow plugs or a start '
                                        'control box near $1,000 [Kevin24Seven — gtS8l93r5cw @ 00:09:53]. '
                                        'Verdict: pass.'},
                            {'name': 'configuration_targeting',
                             'type': 'text',
                             'prompt': 'Filter sold listings for the body configuration you want, such as '
                                       'two-door, soft top, topless, or truck body, and record the model '
                                       'designations and price ranges you found, noting which '
                                       'configurations consistently draw fewer bidders and lower hammers.',
                             'example': 'Filter GovPlanet sold listings for two-door units with soft top '
                                        'and truck body, because two-doors go for far less, and target '
                                        'M1123s [Kevin24Seven — d2qrhLbKEbI @ 00:02:24]. Topless trucks go '
                                        'for a lot less once bidding starts, and brand-new tops in camo, '
                                        'black, white, or tan are on eBay [Kevin24Seven — F0AkAibFp2g @ '
                                        '00:02:37].'},
                            {'name': 'overtime_walkaway',
                             'type': 'text',
                             'prompt': 'Write your walk-away number for the truck before the auction '
                                       'closes, then describe how you will handle repeated 30-second '
                                       'overtime extensions and $100 priority bid steps without chasing '
                                       'the price past the ceiling you set while calm.',
                             'example': "When the clock ends you haven't actually won, because 30-second "
                                        'extensions run four or five times and people can outbid you '
                                        '[Kevin24Seven — F0AkAibFp2g @ 00:09:46]. That creep pushed one '
                                        'truck from about $9,500 to a final win at $12,500. My walk-away: '
                                        'written on paper, taped to the monitor, never raised '
                                        'mid-overtime.'},
                            {'name': 'invoice_and_transport',
                             'type': 'textarea',
                             'prompt': 'Project the full invoice on your target win, including transaction '
                                       'fees, SF-97 fee, and taxes, then add a broker or self-haul '
                                       'transport quote from the pickup site to your home, and record the '
                                       'total landed cost before any repairs.',
                             'example': 'A $10,200 win invoiced at $12,290.40, built from a $1,030 '
                                        'transaction fee and a $50 SF-97 fee, before shipping '
                                        '[Kevin24Seven — gXjTPh7cGHU @ 00:09:22]. A broker driver hauled a '
                                        'truck from Albany, Georgia to St. Louis, Missouri for about $850, '
                                        'with typical runs of $500 to $1,200 by distance [Kevin24Seven — '
                                        'F0AkAibFp2g @ 00:12:07].'},
                            {'name': 'first_start_plan',
                             'type': 'textarea',
                             'prompt': 'Describe your first-start procedure for a truck listed as a '
                                       'non-runner, including battery or slave-cable jumping, steering and '
                                       'brake checks, and the order in which you will chase hard-start '
                                       'causes, before you commit to tearing anything apart.',
                             'example': 'Jump a listed non-runner with a slave cable from another 24-volt '
                                        "truck first; a 'non-runner' M1097 R1 only needed batteries "
                                        '[Rasmussen Equipment — zqnmA4kt0RU @ 00:21:01]. If the brake '
                                        'pedal is equally hard running or off, it is a power steering '
                                        'issue, because the pump feeds the hydro-boost brakes [The '
                                        'Midnight Mechanic — _tJQ6S_OaBc @ 00:07:42]. Glow plugs get '
                                        'checked first.'},
                            {'name': 'title_path',
                             'type': 'textarea',
                             'prompt': 'Identify exactly which ownership document the lot ships with, '
                                       'whether SF-97, MCO, title, or bill of sale only, and record what '
                                       'your DMV will accept, whether an insurer will cover the serial, '
                                       'and the expected wait for paperwork.',
                             'example': 'You sign the end-user agreement, the bill of sale is $25, the '
                                        'SF-97 is $50, and the clean title arrives in up to eight weeks '
                                        '[Dirt Legal — 9EAPaeoXhFs @ 00:01:46]. A bill of sale does not '
                                        'transfer ownership by itself [Zero Tax Tags — uOA3FOVLCGA @ '
                                        '00:01:35]. Confirm the DMV and an insurer accept the six-digit '
                                        'serial.'},
                            {'name': 'title_red_flags',
                             'type': 'text',
                             'prompt': 'List every title or record red flag on the lot, including a '
                                       'missing MCO, a scrap bill of sale on a DLA lot, certificate of '
                                       'destruction, or non-repairable status, and state whether the plan '
                                       'is registration or parts only.',
                             'example': 'Without the MCO there is no title record nine times out of 10, '
                                        'and the DMV may have to generate a VIN [Wisdom & Authority Title '
                                        'Solutions — -S82T9iXF7Q @ 00:06:31]. Carfax does not cover '
                                        'salvage, so pull autostat or Vindoctor at $7.99, and skip '
                                        'certificate of destruction titles [AutoHacker — wNIgM_BLGik @ '
                                        '00:03:20]. Plan: registration only.'},
                            {'name': 'true_build_cost',
                             'type': 'textarea',
                             'prompt': 'Build a line-item total for the finished vehicle, covering winning '
                                       'bid, fees, shipping, registration, taxes, titling service, top or '
                                       'body kit, maintenance, and a dedicated repair reserve, then '
                                       'compare the bare-bones figure against your fully built target.',
                             'example': 'A $12,500 win reached $17,777 bare-bones after shipping, '
                                        'registration, taxes, and $2,977.30 in maintenance, and $35,547 '
                                        'fully built [Kevin24Seven — Vl0TRUioSn0 @ 00:08:43]. A basic '
                                        'four-man build penciled out at $21,335: $11,000 truck with fees, '
                                        '$4,500 soft-top kit, $800 Dirt Legal titling, and $2,500 repairs '
                                        '[Kevin24Seven — d2qrhLbKEbI @ 00:19:39]. Reserve $2,500 for start '
                                        'boxes and TCMs.'},
                            {'name': 'idle_hours_and_wear',
                             'type': 'text',
                             'prompt': 'Record the odometer and engine hours for the target unit, convert '
                                       'idle hours into equivalent miles, and note driveline rust or '
                                       'listing claims you could not verify, so the true wear level drives '
                                       'your bid instead of the odometer alone.',
                             'example': 'One idle hour equals about 33 miles of wear, so 55,000 miles with '
                                        '6,500 hours reads like about 214,000 miles, while 1,700 hours '
                                        'means an engine barely broken in [Vantor Insider — tBIT1SUqIz8 @ '
                                        '00:08:24]. A listing claiming only a weak brake pedal turned out '
                                        'to be incorrect [Kevin24Seven — Vl0TRUioSn0 @ 00:01:15]. The '
                                        "aluminum body won't rust, but the steel driveline can."}],
                 'completion_gate': 'Do not bid until bidding approval is confirmed, the listing passes '
                                    'the blow-by and start screen, the walk-away number is written down, '
                                    'the ownership document and DMV path are verified, and the line-item '
                                    'build total includes transport, titling, and a $2,500 repair '
                                    'reserve.'},
                {'worksheet_id': 'ws-04',
                 'number': 4,
                 'title': 'Military Disposition Screening and Local Lot Flip Plan',
                 'purpose': 'Screen DLA tactical trucks, generators, and condemned lots for paperwork '
                            'traps and hidden service costs, then plan local school, city, and agency '
                            'surplus flips with locked pickup, known exit prices, and a tax reserve before '
                            'a single bid goes in.',
                 'chapter_ref': 'Q7-Q8',
                 'instructions': ['Pull the lot page, terms of sale, and every rider before filling any '
                                  'field, and keep the open lot numbers beside you while you work.',
                                  'Treat condition codes as paperwork, not wear: record what the data '
                                  'plate, hour meter, and preservation tag actually show on the unit.',
                                  'Price every lot to landed cost, not hammer price, adding buyer premium, '
                                  'transport, parts, repairs, and any storage exposure you could face.',
                                  'Confirm trailer, pickup vehicle, and helpers inside the removal window '
                                  'before you mark any lot as ready to bid.',
                                  'For local lots, write the exit price and sold comps first; if the '
                                  'all-in cost lands above your ceiling, strike the lot from the list.'],
                 'fields': [{'name': 'demil_code_and_sf97_check',
                             'type': 'textarea',
                             'prompt': 'Record the demilitarization code and title paperwork listed for '
                                       'the tactical truck you are watching. Note whether the lot confirms '
                                       'an original standard form 97 issued at sale, or only a scrap bill '
                                       'of sale, and decide whether to keep bidding.',
                             'example': 'Lot screen: Vantor Insider says do not bid on any tactical truck '
                                        'until the lot confirms its demilitarization code and an original '
                                        'standard form 97 issued at the time of sale [Vantor Insider — '
                                        'vkoGZ6Y4EhU @ 00:03:00]. Codes D and F are flagged as traps. My '
                                        'lot lists its demil code and an SF97 option, so it stays on the '
                                        'watch list.'},
                            {'name': 'data_plate_and_hour_meter',
                             'type': 'text',
                             'prompt': 'Before placing an offer on any MEP generator, write down the data '
                                       'plate middle digit, the analog hour counter reading, and the '
                                       'preservation tag hours. State whether the plate confirms 60 Hz '
                                       'output and whether both hour figures match each other.',
                             'example': 'Vantor Surplus: always verify the middle digit on the data plate '
                                        'is a zero for 60-Hz output, and check the analog hour counter '
                                        'against the preservation tag [Vantor Surplus — VA8oRw7jQuQ @ '
                                        '00:20:09]. Condemned Tactical Quiet Generators sold under '
                                        'condition code H showed 0.8 to 2.4 hours, logged only during the '
                                        'factory acceptance load test.'},
                            {'name': 'landed_cost_gap',
                             'type': 'textarea',
                             'prompt': 'Calculate the full landed cost for your target lot by adding buyer '
                                       'premium, transport, parts, and repairs to the hammer price. '
                                       'Compare the result to the hammer figure and express the difference '
                                       'as a percentage before you set your ceiling.',
                             'example': 'Vantor Insider puts the average gap between the winning hammer '
                                        'price and what a buyer spends to put the asset into service at '
                                        '42% [Vantor Insider — WGe7vjs5ktc @ 00:00:00]. Engine Auction '
                                        'priced a surplus home backup install at $1,560 all-in, counting '
                                        'the winning bid, a 10% premium, interlock parts, and 6-gauge SOOW '
                                        'cord [Engine Auction — t9kRwYmHNpE @ 00:27:03].'},
                            {'name': 'preserved_engine_first_start',
                             'type': 'textarea',
                             'prompt': 'Write your step-by-step first-start plan for a long-parked or '
                                       'preserved tactical diesel. List how you will turn the engine by '
                                       'hand, prime the fuel system, and handle the fuel cell before '
                                       'anyone touches the key or starter.',
                             'example': 'Vantor Surplus: put a 3/4-inch breaker bar on the front '
                                        'crankshaft damper bolt for two full revolutions, then work the '
                                        'manual primer for 5 minutes, because pooled preservative oil can '
                                        'bend a forged rod [Vantor Surplus — xwqMdeMDNSg @ 00:16:01]. Skip '
                                        'aerosol starting fluid; drain the fuel cell and flush the lines '
                                        'first [Vantor Surplus — VKFtBFmCW4U @ 00:13:00].'},
                            {'name': 'environmental_rider_review',
                             'type': 'text',
                             'prompt': 'For any cheap transformer, communication shelter, or skid chiller '
                                       'you are watching, note whether the environmental rider mentions '
                                       'PCBs, asbestos, or hazmat removal. Describe who pays for removal '
                                       'and whether that obligation still leaves room for profit.',
                             'example': 'Vantor Insider warns not to bid on a $25 to $100 transformer, '
                                        'communication shelter, or skid chiller until the environmental '
                                        'rider on PCBs and asbestos is read [Vantor Insider — vkoGZ6Y4EhU '
                                        '@ 00:15:04]. The same channel adds: stop looking at how cheap the '
                                        'current bid is and start calculating why the fleet manager '
                                        'refused to fix it [Vantor Insider — vkoGZ6Y4EhU @ 00:15:42].'},
                            {'name': 'removal_window_logistics',
                             'type': 'text',
                             'prompt': 'Enter the removal window stated in the terms, the date your '
                                       'trailer and pickup vehicle are confirmed, and the daily storage '
                                       'penalty that applies afterward. Explain how you will finish '
                                       'loading inside the window if the first trip fails.',
                             'example': 'Vantor Surplus: do not bid until trailer and pickup are lined up '
                                        'inside the 10 working day removal window, because daily storage '
                                        'penalties erase the savings [Vantor Surplus — VKFtBFmCW4U @ '
                                        '00:04:13]. My plan: trailer booked for day three, backup rental '
                                        "trailer held for day seven, and the lot's storage rate written "
                                        'beside my maximum bid.'},
                            {'name': 'local_sale_source_log',
                             'type': 'textarea',
                             'prompt': 'List the school districts, cities, police departments, state '
                                       'agencies, and universities near you that sell surplus. For each, '
                                       'note the sale format, whether preview days exist, and typical '
                                       'starting prices, so you can plan which sales to attend.',
                             'example': 'Local sales run on GovDeals, live auctioneers, and preview-day '
                                        'formats, with starting prices from $5 to $100. One local seller '
                                        'starts items at $100 and watches them end in the thousands [41NBC '
                                        '— QOcs7dzmhGk @ 00:00:35]. At a sale where a box of knives went '
                                        'for six to $800, buyers planned to resell them [Good Day '
                                        'Sacramento — 1Cxx4l6qQcA @ 00:02:13].'},
                            {'name': 'exit_price_comps',
                             'type': 'textarea',
                             'prompt': 'Before bidding on any local lot, record at least three sold '
                                       'comparables and the exit price you expect. Then calculate your '
                                       'all-in cost as a percentage of retail and confirm it lands inside '
                                       'your target buy ceiling.',
                             'example': "Shannon Jean: 'I always tell you don't buy anything unless you "
                                        "know what you can sell it for' [Shannon Jean — u0nFlfog1Y0 @ "
                                        '00:11:46]. Their target is 20-25% of retail all-in, always below '
                                        '30%; a Costco patio lot with $10,990 retail sold for $2,000 and '
                                        'landed at 42%, well above the ceiling [Shannon Jean — i3yWMCnu2ac '
                                        '@ 00:12:13].'},
                            {'name': 'pickup_and_account_limits',
                             'type': 'text',
                             'prompt': 'Note your GovDeals account status, the number of items you can '
                                       'currently win, and the truck or rented trailer you will use. '
                                       'Confirm pickup is locked before bidding, since a missed pickup can '
                                       'end your ability to bid.',
                             'example': '2plot ai: new GovDeals accounts are limited to 3 items, and '
                                        'failing to pick up gets you banned, so confirm the truck or a '
                                        'rented U-Haul trailer first [2plot ai — R8bNgZVNLAk @ 00:02:40]. '
                                        'Their San Antonio ISD kitchen equipment netted about $1,500 on '
                                        '$1,400 spent after a 6-hour round trip and four months holding '
                                        '[2plot ai — R8bNgZVNLAk @ 00:09:01].'},
                            {'name': 'tax_reserve_and_testing',
                             'type': 'textarea',
                             'prompt': 'Describe your testing process for every item before it is listed '
                                       'and the percentage of sales you will set aside for taxes. Name '
                                       'where the tax reserve is held so it cannot be spent on trucks, '
                                       'tools, or new inventory.',
                             'example': 'Chase Thrifts got a PayPal 1099 on about $30,000 in sales, and '
                                        'the $2,500 tax bill wiped out a $2,000 truck fund [Chase Thrifts '
                                        '— aKiF3bLLJJ4 @ 00:04:03]. Liquidation Motivation adds that you '
                                        'need some sort of process for testing to make sure everything is '
                                        'good before returned parts hit a listing [Liquidation Motivation '
                                        '— PyTXQNvVkKc @ 00:31:03].'}],
                 'completion_gate': 'Every watched lot shows a confirmed demil code and SF97 status where '
                                    'applicable, a verified data plate and hour reading for generators, a '
                                    'landed cost with the percentage gap over hammer, a booked pickup '
                                    'inside the removal window, sold comps with an exit price, and a '
                                    'funded tax reserve.'},
                {'worksheet_id': 'ws-05',
                 'number': 5,
                 'title': 'Pallet Freight Math and Electronics Scrap Grading',
                 'purpose': 'Turn a liquidation pallet or electronics scrap lot into a priced decision by '
                            'quoting real freight, costing labor, vetting suppliers, and grading boards '
                            'before anything is bought, shipped, or weighed.',
                 'chapter_ref': 'Q9-Q10',
                 'instructions': ['Start with local pallets you can pick up yourself before committing '
                                  'cash to truckloads that carry heavy freight risk.',
                                  'Replace every listed minimum shipping figure with an actual freight '
                                  'quote that includes residential, no-dock, and liftgate charges.',
                                  'Cost your own hours and any helper wages as real expenses; a pallet '
                                  'that only covers wages is a wash.',
                                  'Open, sort, and test every item before listing, and check branded goods '
                                  'against known genuine details.',
                                  'Strip boards of batteries, heat sinks, tape, and metal trays, then '
                                  "confirm grades with the buyer's own tool before shipping."],
                 'fields': [{'name': 'sourcing_channel_choice',
                             'type': 'text',
                             'prompt': 'Name the pallet source you plan to use first, whether a local '
                                       'pallet seller or an online truckload channel. Record the expected '
                                       'turnaround from purchase to sale and explain why that channel fits '
                                       'your current cash and storage space.',
                             'example': 'Levi Salas: the difference between pallet buying and truckload '
                                        'buying is freight [Levi Salas | Whatnot Selling & Liquidation — '
                                        'bGxomNwtOhQ @ 00:00:00]. They push beginners toward local pallets '
                                        'that turn in two to three days instead of truckloads that took '
                                        'two weeks to arrive. My first source is a local warehouse within '
                                        "an hour's drive, picked up by my own trailer."},
                            {'name': 'real_freight_quote',
                             'type': 'textarea',
                             'prompt': 'Record the listed minimum shipping, the actual freight quote, and '
                                       'every added charge such as residential, no-dock, or liftgate fees. '
                                       'Add these to your current bid and write the true all-in total '
                                       'before raising your bid at all.',
                             'example': "T.J. Lovelady's $1,999 MSRP lot from Las Vegas advertised $100 "
                                        'minimum shipping, but the actual quote was $543.96, plus $40 '
                                        'residential and $40 no-dock fees, pushing a $280 current bid near '
                                        '$1,000 all-in [T.J. Lovelady — Lvrvr_hNtcE @ 00:19:19]. Shannon '
                                        'Jean unchecks the $50 liftgate on freighted lots [Shannon Jean — '
                                        'i3yWMCnu2ac @ 00:07:49].'},
                            {'name': 'delivery_site_access',
                             'type': 'text',
                             'prompt': 'State whether your delivery address is commercial or residential, '
                                       'and whether you have a dock, forklift, or other unloading '
                                       'equipment. Note the driver instructions you will send ahead, '
                                       'including a call request and a map to the drop point.',
                             'example': 'B-Stock: confirm commercial versus residential delivery and dock '
                                        'or forklift access before paying, or liftgate and residential '
                                        'fees attach [B-Stock — _JpPAyxnPLc @ 00:03:41]. Treat drivers '
                                        'well: tip them, buy them lunch, request a call 30 minutes before '
                                        'delivery, and text a map to the drop point [B-Stock — _JpPAyxnPLc '
                                        '@ 00:06:26]. My site: residential, no dock, pallet jack only.'},
                            {'name': 'buy_price_vs_retail',
                             'type': 'text',
                             'prompt': 'Enter the pallet price, the stated retail value, and the '
                                       'percentage of retail you are paying. Then write the share of '
                                       'retail you realistically expect back per item, and check the '
                                       'spread against your fixed costs and selling fees.',
                             'example': 'Operation Liquidation pays about 15% of retail on jumbo Amazon '
                                        'returns pallets at roughly $500 to $600 each and targets $50 to '
                                        '$60 back on each $100 retail item, noting the supplier screens '
                                        'out salvage but not with 100% accuracy [Operation Liquidation — '
                                        'f12reX7DS-U @ 00:01:01]. T.J. Lovelady pays roughly 10% of MSRP '
                                        'on lots.'},
                            {'name': 'labor_math',
                             'type': 'textarea',
                             'prompt': 'Estimate the hours needed to sort, test, photograph, and list '
                                       'everything on the pallet, and the wage cost of that labor. '
                                       'Subtract wages, pallet cost, and fees from projected revenue to '
                                       'confirm a real profit remains after every cost.',
                             'example': 'Niche Pursuits ran the quick math on three Amazon return pallets: '
                                        'revenue of $4,000 minus wages of $2,500 and minus pallet costs of '
                                        '$1,500 left exactly $0 in profit [Niche Pursuits — orDRxYfVypw @ '
                                        '00:12:16]. Jona Shone netted £385.47 on £1,592.50 gross after '
                                        "Whatnot's 13% fee, with two people working a full day [Jona Shone "
                                        '— WG6vp4_R0nc @ 00:42:34].'},
                            {'name': 'supplier_vetting',
                             'type': 'text',
                             'prompt': 'List the pallet suppliers you are considering and how you verified '
                                       'each one. Note where they advertise, any history you could '
                                       'confirm, and how you will spot counterfeit branded items once the '
                                       'pallet is opened and sorted.',
                             'example': "Jona Shone: Facebook 'Amazon pallet return' sellers are full of "
                                        'scams, so stick with known suppliers like Gem Wholesale and '
                                        'Stockport Pallet Warehouse [Jona Shone — WG6vp4_R0nc @ 00:43:10]. '
                                        'To verify branded tools, they check a NOCO booster: on a genuine '
                                        'unit the rubber molding runs into the screw hole [Jona Shone — '
                                        'WG6vp4_R0nc @ 00:15:04].'},
                            {'name': 'manifest_and_unboxing_checks',
                             'type': 'textarea',
                             'prompt': 'Describe how you will review the manifest before buying and '
                                       'inspect boxes after delivery. Include how you check listing '
                                       'availability for each item, how you identify likely unopened '
                                       'stock, and how you test items whose origin is unknown.',
                             'example': "T.J. Lovelady checks every ASIN: 'currently unavailable' on "
                                        'Amazon means you would be the only seller listing it [T.J. '
                                        'Lovelady — Lvrvr_hNtcE @ 00:13:51]. Operation Liquidation reads '
                                        'factory banding as a sign the box is likely unopened [Operation '
                                        "Liquidation — f12reX7DS-U @ 00:03:01]. You don't know where a "
                                        'pallet came from, so test them yourself [T.J. Lovelady — '
                                        '3LlA-ruuv7E @ 00:01:51].'},
                            {'name': 'board_prep_and_grading',
                             'type': 'textarea',
                             'prompt': 'List every removal step you will complete before a circuit board '
                                       'is weighed or shipped, such as batteries, heat sinks, brackets, '
                                       'tape, and metal trays. Then explain how you will grade borderline '
                                       'boards and confirm the grade.',
                             'example': 'Storage Unit Scrapper: batteries off, heat sinks off, and tape '
                                        'heat-gunned off before any board ships, or it cannot be sent or '
                                        'gets downgraded [Storage Unit Scrapper — 4TJbVuWoX3A @ 00:15:37]. '
                                        "AI grading called some boards high-grade that BoardSort's Fred "
                                        'tool graded low-grade, so run borderline boards through Fred, '
                                        'which allows 50 submissions a day [Storage Unit Scrapper — '
                                        '4TJbVuWoX3A @ 00:04:45].'},
                            {'name': 'scrap_price_ladder',
                             'type': 'textarea',
                             'prompt': 'Build your price ladder for electronics scrap by listing what each '
                                       'category pays at your local yard versus a specialty buyer. Include '
                                       'whole laptops, RAM, and IC chips, and note whether the extra labor '
                                       'justifies separating each category.',
                             'example': 'Storage Unit Scrapper reports whole laptops at 15 cents a pound '
                                        'at the local yard, down from 98 cents [Storage Unit Scrapper — '
                                        '4TJbVuWoX3A @ 00:00:19], RAM at about $54 a pound at BoardSort '
                                        '[Storage Unit Scrapper — 4TJbVuWoX3A @ 00:21:03], and IC chips at '
                                        'about $15 a pound, roughly 3 lb collected in 8 months [Storage '
                                        'Unit Scrapper — bAvpAOGu8Kw @ 00:09:15].'},
                            {'name': 'sorting_fee_and_blind_buys',
                             'type': 'text',
                             'prompt': 'Before buying any mixed pallet or gaylord of boards, record the '
                                       'asking price, whether you inspected the contents, and the sorting '
                                       'fee you would charge or pay. Explain how the price reflects '
                                       'dirties, metal plates, and grading risk.',
                             'example': 'Shark Scrapper: never buy a pallet or gaylord blind, and walk '
                                        'away unless the mixed-board price already reflects the risk of '
                                        'dirties, metal plates, and mis-graded fractions [Shark Scrapper — '
                                        "6XObIp5c91U @ 00:19:54]. Their going rate for sorting a client's "
                                        'mixed boards is about 10%, waived once for a new computer-repair '
                                        'client to build goodwill [Shark Scrapper — 6XObIp5c91U @ '
                                        '00:06:47].'}],
                 'completion_gate': 'The pallet or scrap lot shows a real freight quote, all-in cost as a '
                                    'share of retail, labor-adjusted profit above zero, a vetted supplier, '
                                    'a manifest and testing plan, prepped and buyer-graded boards, and a '
                                    'price that already reflects blind-lot risk.'},
                {'worksheet_id': 'ws-06',
                 'number': 6,
                 'title': "Seller's Permit, Resale Certificate, and Compliance File",
                 'purpose': 'Build the paperwork file that lets you buy surplus inventory tax-free, sell '
                            'to other resellers without audit exposure, bid DLA awards at a workable '
                            'margin, and close surplus-funds claims with every document ready.',
                 'chapter_ref': 'Q11-Q12',
                 'instructions': ['Separate the permit from the certificate: one authorizes collecting and '
                                  'remitting sales tax, the other covers inventory bought for resale.',
                                  'Record every registration, form number, and expiration date in one '
                                  'place, and set reminders well before December 31 rolls over.',
                                  'Use the SST form first, then the MTC form, and register directly in '
                                  'states where neither form is accepted.',
                                  'Keep certificates you accept complete, signed, dated, and plausible on '
                                  'their face, and retain them for at least four years where Texas rules '
                                  'apply.',
                                  'Answer DLA traceability requests and counteroffers in PDF on the '
                                  'original email thread, and walk away from any award whose math fails.'],
                 'fields': [{'name': 'permit_vs_certificate',
                             'type': 'textarea',
                             'prompt': "Explain in your own words the difference between your seller's "
                                       'permit and your resale certificate. Note which agency issued each, '
                                       'the registration number, and the purchases where you plan to '
                                       'present the certificate to avoid paying sales tax.',
                             'example': 'Kai Ashley ED: a reseller certificate certifies that you do not '
                                        'have to pay sales tax on goods purchased that you intend to '
                                        'resell [Kai Ashley ED — -T-caQVAr7g @ 00:00:47]. James Baker CPA '
                                        'puts the stakes plainly: buying a million dollars of mice means '
                                        '$70,000 in sales taxes you did not have to pay [James Baker CPA — '
                                        'CiHy9lcx3x4 @ 00:01:26].'},
                            {'name': 'state_registration_steps',
                             'type': 'textarea',
                             'prompt': 'List the state registration steps you completed or still need, '
                                       'including the application form, the identification you supplied, '
                                       'and any confirmation email you must forward. Record the date each '
                                       'step finished and any processing problem you encountered.',
                             'example': 'In Florida, the DR-1 online application covers registration. '
                                        'James Baker CPA: with no SSN or visa number, enter all ones in '
                                        'the SSN field, then forward the DR-1 confirmation email with a '
                                        'passport or ID photo to the account-creation mailbox, or the '
                                        'application is never processed [James Baker CPA — L4NQWUrzH6A @ '
                                        '00:08:30].'},
                            {'name': 'multistate_form_choice',
                             'type': 'textarea',
                             'prompt': 'For each vendor, write the ship-to state, whether it accepts the '
                                       'SST form, and whether you fell back to the MTC form. Flag any '
                                       'state that requires its own registration and note the footnotes '
                                       'you reviewed on the MTC form.',
                             'example': 'LedgerGurus: SST plus MTC covers 35 of 45 sales-tax states, while '
                                        'California, Illinois, and roughly 8 others require registration '
                                        '[LedgerGurus: Ecommerce Accounting Experts — It-VnUi3x58 @ '
                                        '00:01:49]. Their default is the SST form first, then the MTC form '
                                        '[LedgerGurus: Ecommerce Accounting Experts — Cn-vsd4HlTE @ '
                                        '00:10:22]. My vendor ships to Illinois, so registration is '
                                        'required.'},
                            {'name': 'certificate_expiration_calendar',
                             'type': 'text',
                             'prompt': "Record each certificate's issue date and expiration date, and list "
                                       'every vendor holding a copy. Note when you will send renewed '
                                       'certificates before the next buying cycle and where printed copies '
                                       'are kept for in-store purchases.',
                             'example': 'Check the certificate date against December 31st and push the new '
                                        'DR-13 to every vendor before the January buying cycle [Santiago '
                                        'Cueto | Miami Business Litigation Lawyer — K5oBesJVonE @ '
                                        '00:07:40]. Lester John prints about 50 copies a year and keeps '
                                        'them in the glove box and laptop bag [Lester John — 7J3W8esngfU @ '
                                        '00:03:28].'},
                            {'name': 'filing_calendar',
                             'type': 'text',
                             'prompt': 'List every state where you hold a registration, the filing '
                                       'frequency assigned to each, and the next due date. Confirm that '
                                       'zero-sales periods are still on your calendar, since a '
                                       'registration carries filing duties even without in-state sales.',
                             'example': 'James Baker CPA: verify a return is on the calendar for every '
                                        'registered state, including zero-sales periods, because Florida '
                                        'expects a quarterly filing even if you sell zero inside the state '
                                        '[James Baker CPA — L4NQWUrzH6A @ 00:09:25]. My calendar: Florida '
                                        'quarterly, next return due after the current quarter closes, zero '
                                        'sales reported if nothing sold in-state.'},
                            {'name': 'retailer_exemption_list',
                             'type': 'textarea',
                             'prompt': 'List the retailers where you plan to request a tax exemption, '
                                       'sorting them into yes, maybe, and definite no groups. Note how you '
                                       'will submit the exemption, such as online chat, and what you will '
                                       'do if a retailer refuses.',
                             'example': 'Jack Hagwell: confirm a retailer sits on the yes list and not '
                                        'with Target-style definite nos that ban resellers on sight [Jack '
                                        'Hagwell — iNfW7YXuTOA @ 00:12:50]. They use online chat for '
                                        'cart-level exemptions to avoid questions about unit counts [Jack '
                                        'Hagwell — iNfW7YXuTOA @ 00:09:14], and would rather pay the sales '
                                        'tax than get banned [Jack Hagwell — iNfW7YXuTOA @ 00:11:43].'},
                            {'name': 'certificate_misuse_guardrails',
                             'type': 'textarea',
                             'prompt': 'Describe which purchases qualify for your resale certificate and '
                                       'which do not. List the items you resell, the personal purchases '
                                       'you will always pay tax on, and the penalty exposure you face if '
                                       'the certificate is misused.',
                             'example': 'T-SHIRT KINGS: only claim it on things you resell, like blanks '
                                        'that become customer shirts; getting one just to dodge tax is '
                                        'fraud [T-SHIRT KINGS — 1YNFxlnPOZM @ 00:01:59]. In California, '
                                        'misuse brings the tax due plus a penalty of 10% of the tax or '
                                        '$500, whichever is more, per purchase [Matt Sokol Business — '
                                        'vwdB1U0_hGs @ 00:04:28].'},
                            {'name': 'buyer_certificate_file',
                             'type': 'textarea',
                             'prompt': 'When you sell tax-free to another reseller, record what is on '
                                       'file: a complete, signed, dated certificate, its stated reason, '
                                       'and any lookup you ran. Note the deadline for collecting missing '
                                       'certificates and how long you will retain them.',
                             'example': 'Hold a complete, signed, dated certificate whose stated reason '
                                        'matches what the customer buys [Tax Expert Today — WZL5m9rfNSQ @ '
                                        '00:03:37]. Texas gives 90 days after written Comptroller notice '
                                        'and expects certificates kept at least 4 years [Tax Expert Today '
                                        '— WZL5m9rfNSQ @ 00:03:20]. New York cuts off single-use '
                                        'certificates at 90 days [Sales Tax Sisters — uZA19ayitYY @ '
                                        '00:16:30].'},
                            {'name': 'dla_bid_and_award_review',
                             'type': 'textarea',
                             'prompt': 'For each DLA DIBBS quote, record vendor cost, packaging, '
                                       'inspection, and your target margin. Note the PR number type, the '
                                       'inspection boxes on the award, any IDC minimum, and whether you '
                                       'would accept or refuse a counteroffer.',
                             'example': 'Tristan Thomas targets a 10% to 15% margin, since 20% to 25% gets '
                                        'underbid [Secureframe — v7nJCLRc0uo @ 00:38:03]. A PR number of '
                                        '1-0-0 means an estimated IDC quantity, while 700 or 090 means a '
                                        'firm quantity [Tris10 @ MeND — sG-wAF0b7kQ @ 00:15:16]. MeND has '
                                        'refused counteroffers with an informal cost breakdown and still '
                                        'won [Tris10 @ MeND — Y895jCYSE5A @ 00:08:22].'},
                            {'name': 'surplus_funds_claim_file',
                             'type': 'textarea',
                             'prompt': 'For a surplus-funds claim, list the documents you ordered, the '
                                       'date the signed contract arrived, and the date the claim was '
                                       'filed. Record your due diligence on debts and liens, and compare '
                                       "any attorney fee against the claimant's share.",
                             'example': 'Overage Acquisition: once the signed contract arrives, order the '
                                        'grant deed, not the tax deed, at about $4 per copy via Property '
                                        'Radar [Overage Acquisition — X_Oq8vv4j_c @ 00:01:22]. Check for '
                                        'any additional debt or liens [Money Making Juggernaut — '
                                        'KdtNDjlE4WQ @ 00:01:03]. A $2,500 attorney fee on $19,000 failed; '
                                        '$1,250 contingency worked [Money Making Juggernaut — MmWoRR82S9g '
                                        '@ 00:04:46].'}],
                 'completion_gate': 'Your file holds the permit and certificate numbers, a completed '
                                    'registration log, a vendor-by-vendor SST or MTC record, a renewal '
                                    'calendar, a filing calendar including zero-sales periods, a retailer '
                                    'exemption list, misuse guardrails, a complete certificate file for '
                                    'tax-free sales, a priced DLA bid sheet, and a documented '
                                    'surplus-funds claim.'}]}
