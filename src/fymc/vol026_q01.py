from __future__ import annotations

CHAPTER_1 = {'id': 'Q1',
 'chapter_id': 'Q1',
 'chapter_number': 1,
 'question_number': 1,
 'slug': 'government-auction-platforms-and-bidding-mechanics',
 'question_prompt': 'Where do government surplus auctions actually happen, and how do I register, search, '
                    'and place bids on the main platforms?',
 'kicker': 'Q1 / THE BIG MONEY PLAYBOOKS',
 'title': 'Finding the Sales: Government Auction Platforms and How Bidding Works',
 'subtitle': 'GSAAuctions.gov online and offline bidding, GovDeals listings, Public Surplus, '
             'RealEstateSales.gov registration, UX Auctions search tools, and city, county, state, and '
             'federal sale sources',
 'layout_template': 'opportunity_overview',
 'reading_time_minutes': 15,
 'executive_summary': 'Practitioners agree the inventory is real, public, and fragmented: East Coast '
                      'Classics found Delaware, New Castle County, and Wilmington each selling through a '
                      'different platform, while UX Auctions and GovAuctions name GSA Auctions, GovDeals, '
                      'Public Surplus, and Municibid as the core channels, no dealer license required. The '
                      "street math is fee-driven: GovDeals buyer's premiums run 5% to 12.5%, US Gov Bid "
                      'charges a $100 one-time registration plus a $60 wire fee, and Public Surplus caps '
                      'card purchases at $4,000. UX Auctions logged 310 Florida running vehicles under '
                      '$3,000 and Norfolk keyed vehicles at a $1,300 middle price versus $550 without '
                      'keys. Winning hinges on proxy bids, soft-close extensions, reserves, and short '
                      'pickup windows. The split is over condition risk: Greg Berry sells $70-battery '
                      'upside on non-runners, while East Coast Classics passed on Crown Vics too rough to '
                      'export.',
 'key_metrics': [{'label': "GovDeals Buyer's Premium Range",
                  'metric': "GovDeals Buyer's Premium Range",
                  'value': '5% to 12.5% added to the final bid',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Premium is set by each selling municipality; registration on GovDeals itself '
                             'costs nothing.',
                  'source': 'East Coast Classics ([q09PUtJPIxs @ 00:04:12])'},
                 {'label': 'Keyed vs Keyless Vehicle Middle Price',
                  'metric': 'Keyed vs Keyless Vehicle Middle Price',
                  'value': '$1,300 with a key vs $550 without',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Middle sold price for vehicles at Norfolk, Virginia government auctions, '
                             'split by whether a key was present.',
                  'source': 'UX Auctions ([Z87d62pWVEk @ 00:08:33])'},
                 {'label': 'Public Surplus Card Rules',
                  'metric': 'Public Surplus Card Rules',
                  'value': 'Card hold once bidding passes $500; $4,000 credit card purchase cap',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Public Surplus places a hold for a portion of the bid above $500 and limits '
                             'card purchases to $4,000.',
                  'source': 'East Coast Classics ([q09PUtJPIxs @ 00:05:25])'},
                 {'label': 'Timed Auction Clock',
                  'metric': 'Timed Auction Clock',
                  'value': '3-10 day auctions; 5-15 business days to pay; 1-4 week pickup',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Typical online government surplus auction run time, payment window, and '
                             'removal window.',
                  'source': 'GovAuctions ([Ie7zxVOXjeE @ 00:01:21])'}],
 'sections': [{'heading': 'Section 1: The Practitioner Consensus',
               'paragraphs': ['The baseline every practitioner agrees on is that the sales are real and '
                              'open to anyone. GovAuctions frames it bluntly: agencies are legally '
                              'required to dispose of seized and surplus property, cannot hold it '
                              'indefinitely, and push it to the public through auctions, with most lots '
                              'needing no special license or dealer credentials [x8_btciMVuY @ 00:00:15]. '
                              'UX Auctions sets the bar at two conditions: if you are old enough to sign a '
                              'contract and you can pay, you can bid, no dealer license and no connections '
                              'required [Z87d62pWVEk @ 00:02:42]. Greg Berry, who founded Municibid in '
                              '2006 after watching a town council sell a police car worth $3,000 for $300 '
                              'or $400 to one or two interested people, says anyone in the United States '
                              'and Canada can bid, and roughly 80 percent of the bidder base is '
                              'businesses: landscapers buying dump trucks, snow removal outfits buying '
                              'plow trucks, construction firms buying heavy equipment [pRzKRg71z4s @ '
                              '00:09:43]. The supply is also not a trickle. Matthew Lesko pegs GSA '
                              'Auctions alone at $250 million a year in vehicles, furniture, electronics, '
                              'and machinery, with roughly 300 sales running at any time and an estimated '
                              'one and a half to two billion dollars in federal property moving annually '
                              '[Ezeprg6O_GU @ 00:00:02].',
                              'The second consensus point is that no single site holds the market, so '
                              'finding sales is legwork. East Coast Classics calls the search the hardest '
                              'part of the whole process, says Google is your best friend for queries like '
                              'public auctions or public surplus in your area, and reports that in '
                              'Delaware the state sells through US Gov Bid, New Castle County through '
                              'GovDeals, and the city of Wilmington through Public Surplus, all within '
                              'minutes of each other [q09PUtJPIxs @ 00:01:38]. MrDavidAdelman makes the '
                              'same complaint: there is no consolidated place listing everything, local, '
                              'state, and federal governments tend not to cooperate, and listings may only '
                              'mention some of the items being sold, so call the local or state office, '
                              'check the newspaper, and look at notices posted in city and county '
                              'buildings [gnsqwRYhRPY @ 00:01:51]. UX Auctions maps the channels: cities '
                              'and counties on GovDeals, Public Surplus, and Municibid, the federal fleet '
                              'through GSA Auctions and GSA Fleet sales, some agencies through hired local '
                              'auction companies, and impounded cars straight off city tow lots, with a '
                              'sale sometimes listed only a week or two [Z87d62pWVEk @ 00:04:23]. '
                              'GovAuctions adds that the biggest challenge across three platforms is '
                              'simply not missing lots [ubzNe62V_y4 @ 00:01:21].',
                              'Every speaker who touches condition lands on the same rule: government '
                              'property sells as is, and the bidder carries the risk. UX Auctions points '
                              'to fine print on a real Florida listing stating the description rests on a '
                              'limited 5 to 10 minute visual inspection, then reminds buyers there is no '
                              'warranty and no returns, so zoom in on tires, dash, body, and engine bay or '
                              'go see it [Z87d62pWVEk @ 00:08:55]. Greg Berry tells Municibid buyers to be '
                              'buyer beware, ask every question, and use the on-site viewing most selling '
                              'agencies allow to kick the tires before bidding, adding that pretty much '
                              'everything on Municibid sells as is and largely out of warranty '
                              '[pRzKRg71z4s @ 00:15:01]. East Coast Classics is the harshest on this '
                              'point: get off your rump, make the phone call, schedule an appointment, and '
                              'physically inspect, because one car that read and photographed well online '
                              'could be smelled before reaching the windows and turned out to be a former '
                              'K9 unit [q09PUtJPIxs @ 00:05:55]. GovAuctions closes the loop for '
                              'resellers: condition is often unknown, there are no returns, and shipping '
                              'can eat into your margin fast, so know what you are looking at before you '
                              'bid [x8_btciMVuY @ 00:01:05].'],
               'table': {'caption': 'Where the practitioners agree on access, platforms, and risk',
                         'headers': ['Consensus Point',
                                     'What Practitioners Report',
                                     'Operator Implication',
                                     'Expert Source'],
                         'rows': [['Sales are real and legally mandated',
                                   'Agencies must dispose of seized and surplus property and cannot hold '
                                   'it indefinitely',
                                   'Treat the inventory as a steady, recurring public pipeline rather than '
                                   'rumor',
                                   'GovAuctions ([x8_btciMVuY @ 00:00:15])'],
                                  ['No dealer license is needed to bid',
                                   'Anyone old enough to sign a contract who can pay is allowed to bid',
                                   'Regular buyers compete for the same lots professionals and fleet '
                                   'resellers chase',
                                   'UX Auctions ([Z87d62pWVEk @ 00:02:42])'],
                                  ['Platforms split by jurisdiction in one area',
                                   'Delaware state uses US Gov Bid, county uses GovDeals, Wilmington uses '
                                   'Public Surplus',
                                   'Map every city, county, and state seller in your area separately',
                                   'East Coast Classics ([q09PUtJPIxs @ 00:01:38])'],
                                  ['No single consolidated listing source exists',
                                   'Local, state, and federal governments advertise separately and rarely '
                                   'cooperate on listings',
                                   'Combine web searches, phone calls, newspapers, and posted notices at '
                                   'government buildings',
                                   'MrDavidAdelman ([gnsqwRYhRPY @ 00:01:51])'],
                                  ['Everything sells as is with no returns',
                                   'Listing descriptions rest on a limited 5 to 10 minute visual '
                                   'inspection',
                                   'Inspect in person or send someone before you commit a bid',
                                   'UX Auctions ([Z87d62pWVEk @ 00:08:55])'],
                                  ['Businesses dominate the bidder pool',
                                   'Landscapers, snow removal outfits, and construction firms buy '
                                   'repeatedly from government sellers',
                                   'Expect experienced, repeat business buyers bidding against you on work '
                                   'equipment',
                                   'homebusinessmag ([pRzKRg71z4s @ 00:09:43])'],
                                  ['Three core platforms carry most active lots',
                                   'GSA Auctions handles federal property; GovDeals and Public Surplus '
                                   'carry state and local',
                                   'Start scouting on these three before chasing smaller regional sellers',
                                   'GovAuctions ([x8_btciMVuY @ 00:00:48])']]}},
              {'heading': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['The fee stack changes by platform, and East Coast Classics has run the '
                              'numbers on all three Delaware channels. US Gov Bid now charges a one-time '
                              "$100 registration fee but carries no buyer's premium, which makes it "
                              'cheapest on higher-dollar buys; the catch is payment, either a wire with a '
                              '$60 processing fee that recently rose from $30, plus roughly $30 your own '
                              "bank charges, or an overnighted cashier's check, so a $10 pair of jack "
                              'stands can land near $100 all-in, while a $3,200 Chevy Tahoe came in at a '
                              'little under 3 percent in fees [q09PUtJPIxs @ 00:03:09]. GovDeals '
                              "registration costs nothing, but a buyer's premium set by each municipality "
                              'runs from 5 percent to 12.5 percent, offset by easy PayPal or credit card '
                              'payment and customer service seven days a week [q09PUtJPIxs @ 00:04:12]. '
                              'Public Surplus files vehicles under motor pools, places a hold on your card '
                              'for a portion of the bid once bidding passes $500, and caps credit card '
                              'purchases at $4,000 [q09PUtJPIxs @ 00:05:25]. UX Auctions tells new bidders '
                              'to check four terms before anything else: payment method and deadline, '
                              "buyer's premium, pickup window, and whether you get a title or a bill of "
                              'sale [Z87d62pWVEk @ 00:06:20].',
                              'The bidding engine runs on proxy logic. GSA explains that an English-style '
                              'online auction accepts a flat bid, which is the starting bid or current bid '
                              'plus the increment, or a proxy bid set at the most you will pay; the system '
                              'spends only enough to beat a competing proxy plus one increment, the '
                              'greater proxy always wins, an exact tie goes to whoever entered first, and '
                              'an inactivity period at the end means the sale closes only after a set '
                              'stretch with no bids [JzuRczRAlW8 @ 00:02:23]. UX Auctions tells bidders to '
                              'enter their number as the max and let the system work, because early prices '
                              'mean almost nothing: the Monday before a Florida sale, 103 Explorers sat at '
                              '$5 to $10, and Guilford County lots were stuck at $200 to $250 days before '
                              'close; many sites also add minutes when a late bid lands, so sniping the '
                              'last second is unreliable, and reserve lots do not sell if bidding stays '
                              "under the seller's floor [Z87d62pWVEk @ 00:15:10]. GSA's redesign flags "
                              'lots yellow at one to two hours left and red under one hour, and lists the '
                              'top four high bids under the place-bid button [csOCrIHnuSo @ 00:01:47].',
                              'Pricing your number comes from sold data, not dealer stickers. UX Auctions '
                              'says to pull the middle price of the same year and model, ideally in the '
                              'same state over recent months, then adjust down for high miles, no key, or '
                              "a branded title, and add bid, buyer's premium, fees, towing or shipping, "
                              'title and registration, and inspection-day repairs to get the real cost; '
                              'the keys gap alone is stark, with Norfolk keyed vehicles at a $1,300 middle '
                              "price against $550 without [Z87d62pWVEk @ 00:08:33]. The UX Network's "
                              'November 19, 2026 report gives fresh comps: a 2009 Crown Victoria with '
                              '106,000 miles at $2,405, a 2019 Tahoe at $6,651, a 2011 International '
                              'tandem dump truck at $5,200, and a 1987 Humvee diesel with 3,500 miles at '
                              '$7,506 [c9mCACUk14Y @ 00:01:26]. East Coast Classics watched Crown Vics '
                              "live: a 2003 captain's car with 108,000 miles stalled at $450, a "
                              '153,000-mile unit with 4,700 idle hours drew six bidders to $625 with hours '
                              'to go, and a clean 118,000-mile county car sold for $650 to a single bidder '
                              '[q09PUtJPIxs @ 00:11:03]. GovAuctions puts the clock at 3 to 10 day '
                              'auctions, 5 to 15 business days to pay, and 1 to 4 week pickups '
                              '[Ie7zxVOXjeE @ 00:01:21].'],
               'table': {'caption': 'Platform fees, bidding rules, and timelines operators plan around',
                         'headers': ['Mechanic',
                                     'Exact Number or Rule',
                                     'How Operators Use It',
                                     'Expert Source'],
                         'rows': [['US Gov Bid fee structure',
                                   "$100 one-time registration, no buyer's premium, $60 wire processing "
                                   'fee',
                                   'Favor it on higher-dollar purchases where percentage premiums '
                                   'elsewhere would bite',
                                   'East Coast Classics ([q09PUtJPIxs @ 00:02:22])'],
                                  ["GovDeals buyer's premium",
                                   'Set per municipality, seen from 5% up to 12.5% of the bid',
                                   "Fold the specific seller's premium into your maximum before bidding",
                                   'East Coast Classics ([q09PUtJPIxs @ 00:04:12])'],
                                  ['Public Surplus card rules',
                                   'Card hold once bidding passes $500; $4,000 credit card purchase cap',
                                   'Plan payment in advance for any lot likely to exceed the card cap',
                                   'East Coast Classics ([q09PUtJPIxs @ 00:05:25])'],
                                  ['GSA proxy bidding',
                                   'Greater proxy always wins; identical proxies go to the earlier bidder',
                                   'Enter your true maximum early rather than nibbling at increments',
                                   'GSA (General Services Administration) ([JzuRczRAlW8 @ 00:02:23])'],
                                  ['GSA Buy Now listings',
                                   'First bidder at the fixed price wins and goes straight to payment',
                                   'Keep a credit card on your profile to lock fixed-price lots instantly',
                                   'GSA (General Services Administration) ([JzuRczRAlW8 @ 00:02:46])'],
                                  ['Keyed versus keyless vehicles',
                                   'Norfolk middle price of $1,300 with a key versus $550 without',
                                   'Discount keyless units hard and budget a tow off the lot',
                                   'UX Auctions ([Z87d62pWVEk @ 00:08:33])'],
                                  ['Timed auction timeline',
                                   '3 to 10 day runs, 5 to 15 business days to pay, 1 to 4 week pickup',
                                   'Calendar every payment and pickup deadline the moment you win',
                                   'GovAuctions ([Ie7zxVOXjeE @ 00:01:21])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Edges the Regulars Use',
                           'body': 'Small habits that separate repeat buyers from first-timers chasing '
                                   'listing photos.',
                           'items': ['Search US Gov Bid past auctions going back years to pull historical '
                                     'selling prices on everything sold before you set a max [East Coast '
                                     'Classics — q09PUtJPIxs @ 00:03:24].',
                                     'Work the yard: a maintenance supervisor who openly shared what they '
                                     'knew about the fleet turned one county lot into a potential honey '
                                     'hole, with every car there slated for upcoming auctions [East Coast '
                                     'Classics — q09PUtJPIxs @ 00:11:03].',
                                     'Read the seller playbook: GovDeals tells agencies to run 7 to 10 '
                                     'days, end Monday through Thursday in the afternoon or evening, avoid '
                                     'weekends and holidays, and stagger end times at least 10 minutes '
                                     'apart, so watch those closing windows [GovDeals Media — Q4B13yVVzZQ '
                                     '@ 00:01:11].',
                                     'Cannot make inspection day? Hire a mobile inspection service with '
                                     'ASE certified mechanics to check the vehicle and send a photo report '
                                     'before you bid, provided the yard allows outside inspectors [UX '
                                     'Auctions — Z87d62pWVEk @ 00:10:18].']},
               'sop_steps': [{'step': 1,
                              'title': 'Map Every Local Seller',
                              'action': 'Search for the state, county, and city auction platforms in your '
                                        'area and register on each.',
                              'detail': 'Google public auctions or public surplus for your area and expect '
                                        'each level of government to use a different company, then '
                                        'register as a bidder on each [East Coast Classics — q09PUtJPIxs @ '
                                        '00:01:25]. Hunt the agency that would logically own the item, '
                                        'such as an agriculture agency for used tractors [MrDavidAdelman — '
                                        'gnsqwRYhRPY @ 00:03:09].'},
                             {'step': 2,
                              'title': 'Register and Read the Terms',
                              'action': 'Create accounts, keep a card on file where required, and read the '
                                        'four terms on every sale.',
                              'detail': 'Signup is free on most sites with name, address, phone, and '
                                        'email, some require a credit card on file, and the terms to check '
                                        "are payment method and deadline, buyer's premium, pickup window, "
                                        'and title or bill of sale [UX Auctions — Z87d62pWVEk @ 00:06:01]. '
                                        'For federal real estate, verify through Login.gov, submit the bid '
                                        'form and registration deposit, and register separately for each '
                                        'property [GSA (General Services Administration) — zFGATosXViU @ '
                                        '00:04:11].'},
                             {'step': 3,
                              'title': 'Inspect and Set Your Number',
                              'action': 'Go on inspection day with tools, then price off sold middle '
                                        'prices plus every added cost.',
                              'detail': 'Bring a flashlight, rag, gloves, phone, and an OBD2 scanner if '
                                        'allowed, and walk away from frame rust you can poke through, '
                                        'signs of a flood, or a VIN that does not match; everything else '
                                        'gets factored into the bid [UX Auctions — Z87d62pWVEk @ '
                                        '00:11:50].'},
                             {'step': 4,
                              'title': 'Bid Proxy, Pay Fast, Remove Legally',
                              'action': 'Enter your max as a proxy, pay inside the deadline, and have '
                                        'removal sorted before close.',
                              'detail': 'Set a firm maximum, expect payment deadlines as tight as two to '
                                        'three business days, and bring valid ID plus proof of payment at '
                                        'pickup [The Salmon Runs — jaeWKn_Nu68 @ 00:01:08]. Know how the '
                                        'vehicle leaves the lot: in Delaware a $20 temporary tag gives 60 '
                                        'days of legal driving, while other sellers require a tow [East '
                                        'Coast Classics — q09PUtJPIxs @ 00:06:23].'}]},
              {'title': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The first split is over where to hunt. East Coast Classics treats discovery '
                              'as a manual grind: Google public auctions or public surplus for your area '
                              'and keep digging, because in Delaware the state sells through US Gov Bid, '
                              'New Castle County through GovDeals, and the city of Wilmington through '
                              'Public Surplus [q09PUtJPIxs @ 00:01:25]. The channel calls GovDeals the big '
                              'dog with robust filtering that can still overwhelm an unfocused buyer, '
                              'ranks US Gov Bid as a small player, and slots Public Surplus in the middle. '
                              'UX Auctions runs the opposite playbook: one search box at uxsearch.app that '
                              'hits GovDeals, GSA, Public Surplus, Municibid and police auction sites at '
                              'once, plus a schedule page that maps every police and government sale it '
                              'finds [Z87d62pWVEk @ 00:00:20]. GovAuctions splits the difference, framing '
                              'GovDeals as the high-volume classroom for learning how prices settle and '
                              'Public Surplus as the place sleeper deals from schools and counties hide, '
                              'then telling buyers to work a fixed schedule with a short list of '
                              'categories and locations rather than checking every site by hand '
                              '[ubzNe62V_y4 @ 00:01:05]. MrDavidAdelman goes fully analog: no consolidated '
                              'list exists, so call or email local and state offices, read the local '
                              'paper, and scan postings at city and county buildings [gnsqwRYhRPY @ '
                              '00:02:23].',
                              'Cost structure is where the platforms diverge hardest, and East Coast '
                              'Classics has run the numbers on all three. US Gov Bid now charges a '
                              "one-time $100 registration fee but no buyer's premium, which makes it the "
                              'lowest-fee venue on higher-dollar buys; their $3,200 Chevy Tahoe landed at '
                              'a little less than 3% in fees [q09PUtJPIxs @ 00:03:24]. The catch is '
                              'payment: wire the money with a $60 processing fee, up from $30, plus '
                              "roughly $30 from your own bank, or overnight a cashier's check, so a $10 "
                              'pair of jack stands turns into a $100 purchase. GovDeals flips that model '
                              "with free registration, PayPal or credit card payment, and a buyer's "
                              'premium they have seen run from 5% to 12.5% depending on the municipality. '
                              'Public Surplus places a hold on your card once bidding passes $500 and caps '
                              'card purchases at $4,000. UX Auctions confirms the patchwork, warning that '
                              "some sales take credit cards while others accept only a cashier's check or "
                              "wire, and that the buyer's premium sits on top of the winning bid "
                              '[Z87d62pWVEk @ 00:06:37]. The payment clock itself is disputed: The Salmon '
                              'Runs says deadlines typically land within two to three business days '
                              '[jaeWKn_Nu68 @ 00:01:08], while GovAuctions quotes five to fifteen business '
                              'days [Ie7zxVOXjeE @ 00:01:21].',
                              'Not everyone bids in a timed online lot. Matthew Lesko pitches the free '
                              'route: Lesko says small businesses, including veteran-owned ones, plus '
                              'nonprofits, schools, clinics, child care centers and museums can get '
                              'surplus for free, citing a requirement of at least 51% ownership or control '
                              'by economically disadvantaged citizens and income under $400,000, and '
                              'recalling a nonprofit radio station that landed an ex Air Force base '
                              '[Ezeprg6O_GU @ 00:03:16]. GSA runs a parallel offline lane: sealed bids by '
                              'mail or email stay sealed until the date on the invitation for bid, term '
                              'contracts can demand recurring removals over a set period, and fixed-price '
                              'retail sales go first-come, first-served [Dga3YkAiGmw @ 00:01:04]. Greg '
                              'Berry of Municibid describes the resale playbook instead: buyers turning '
                              'fire hoses into wallets sold on Etsy, a car guy who accidentally bought 20 '
                              'or 30 traffic lights and built a side business reselling them, refinishers '
                              'flipping wood furniture, and bulk lots bought at a discount then sold off '
                              'individually [pRzKRg71z4s @ 00:10:19]. GovAuctions frames the format choice '
                              'as temperament: online timed auctions run over several days and let you '
                              'research at your own pace, while live events move faster with real-time '
                              'bidding [Ie7zxVOXjeE @ 00:00:48].'],
               'table': {'caption': 'Competing playbooks practitioners run on the same government surplus '
                                    'decisions',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['How to locate the right local sale platform',
                                   'Google public auctions per town, county and state because each '
                                   'jurisdiction may use a different platform',
                                   'Search GovDeals, GSA, Public Surplus and Municibid all at once through '
                                   'one aggregator search box',
                                   'East Coast Classics ([q09PUtJPIxs @ 00:01:25]); UX Auctions '
                                   '([Z87d62pWVEk @ 00:00:20])'],
                                  ['Which fee model hurts less on your buy',
                                   "US Gov Bid charges $100 once, no buyer's premium, but wire or "
                                   "cashier's check only",
                                   'GovDeals registers free and takes PayPal or card, but adds a 5% to '
                                   '12.5% premium',
                                   'East Coast Classics ([q09PUtJPIxs @ 00:02:39]); East Coast Classics '
                                   '([q09PUtJPIxs @ 00:04:12])'],
                                  ['How fast the winning invoice must be paid',
                                   'Payment deadlines are often strict, typically within two to three '
                                   'business days of winning',
                                   'Online auctions run 3 to 10 days, then buyers get 5 to 15 business '
                                   'days',
                                   'The Salmon Runs ([jaeWKn_Nu68 @ 00:01:08]); GovAuctions ([Ie7zxVOXjeE '
                                   '@ 00:01:21])'],
                                  ['How far to trust the online listing description',
                                   'GovDeals write-ups run thorough; one car inspected better than its own '
                                   'description suggested',
                                   'Great photos and a good description hid a former K9 car you could '
                                   'smell',
                                   'East Coast Classics ([q09PUtJPIxs @ 00:04:27]); East Coast Classics '
                                   '([q09PUtJPIxs @ 00:05:55])'],
                                  ['Whether to pay at all for the surplus',
                                   'Bid competitively against the general public in timed online or '
                                   'in-person live auctions',
                                   'Nonprofits, schools, clinics and qualifying small businesses get '
                                   'surplus property for free, per Lesko',
                                   'Matthew Lesko ([Ezeprg6O_GU @ 00:03:16]); GovAuctions ([Ie7zxVOXjeE @ '
                                   '00:00:48])'],
                                  ['How the bid itself gets placed and decided',
                                   'Enter a proxy maximum and let GSA bid only as much as needed to lead',
                                   'Sealed bids by mail or email stay closed until the invitation for bid '
                                   'date',
                                   'GSA (General Services Administration) ([JzuRczRAlW8 @ 00:02:03]); GSA '
                                   '(General Services Administration) ([Dga3YkAiGmw @ 00:00:46])'],
                                  ['Which big platform a beginner should work first',
                                   'GovDeals offers huge volume for learning how prices settle, but needs '
                                   'a sorting routine',
                                   'Public Surplus carries schools and counties, where sleeper deals get '
                                   'less bidder attention',
                                   'GovAuctions ([ubzNe62V_y4 @ 00:00:49]); GovAuctions ([ubzNe62V_y4 @ '
                                   '00:01:05])']]}},
              {'title': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['Condition is where buyers bleed. East Coast Classics went to Avalon, New '
                              "Jersey to vet Crown Victorias for a buddy named Frank: the 2003 captain's "
                              'car at 108,000 miles carried a long door scratch and fender rust, the Oreo '
                              'car had rust, sticker shadows and 4,700 idle hours, and two more on a '
                              'second lot would not start, one needing a fuel pump and one a starter, '
                              'leaving them parts cars bid in the high $300s [q09PUtJPIxs @ 00:09:22]. '
                              'Another car read good and looked good online, yet East Coast Classics '
                              'smelled it before reaching the windows and later learned it was a former K9 '
                              'car. UX Auctions points out that listing descriptions can rest on a limited '
                              '5 to 10 minute visual inspection and that government vehicles sell as is '
                              'with no warranty and no returns [Z87d62pWVEk @ 00:09:14]. Its walk-away '
                              'list is frame rust you can poke through, flood signs like a musty smell, '
                              'damp carpet or a water line, and a VIN that does not match the listing. '
                              'Keys move price too: in Norfolk, keyed vehicles sold at a middle price of '
                              "$1,300 versus $550 without [Z87d62pWVEk @ 00:08:33]. Greg Berry's "
                              'counterpoint is that a non-runner may only need a $70 battery [pRzKRg71z4s '
                              '@ 00:15:50].',
                              'The second trap is logistics after the hammer. East Coast Classics has seen '
                              'removal windows of seven days at some lots and two at others, and notes '
                              'Delaware sells a $20 temporary tag good for 60 days while other '
                              'jurisdictions force a tow [q09PUtJPIxs @ 00:06:23]. UX Auctions documents '
                              'the penalties: miss a payment deadline and you can lose the vehicle and get '
                              'blocked from bidding again; Guilford County gave a three-day pickup window, '
                              'Wednesday through Friday with no other times, and Montgomery County, '
                              'Maryland charges a daily storage fee before forfeiting the vehicle with no '
                              'refund [Z87d62pWVEk @ 00:17:24]. Montgomery County also requires a tow '
                              'truck, tow dolly, trailer, temporary plates or dealer plates to move it, '
                              'and its buyers must apply for a salvage title within 90 days, while Norfolk '
                              'buyers get a bill of sale and affidavit with 30 days to file at the '
                              'Virginia DMV. GovAuctions warns that condition is often unknown, there are '
                              'no returns, and shipping can eat into your margin fast [x8_btciMVuY @ '
                              '00:01:23]. MrDavidAdelman watched a pallet of computers go for less than '
                              'the cost of a single computer while in the right place at the right time, '
                              'but without a truck [gnsqwRYhRPY @ 00:05:28].',
                              "The last check is the bidder's own head. UX Auctions calls getting caught "
                              'up in the moment the biggest mistake new bidders make, and prescribes the '
                              'fix: price off real winning bids for the same year, model and state, use '
                              'the middle price rather than an average one crazy sale can distort, then '
                              "total bid plus buyer's premium, fees, towing or shipping, title, "
                              'registration and repairs [Z87d62pWVEk @ 00:12:10]. Early prices are noise; '
                              'on the Monday before the Florida sale, 103 Explorers still sat at $5 to '
                              '$10, sites extend the clock when late bids land, and a reserve can kill the '
                              'sale even if you are high bidder. The Salmon Runs adds sales tax to that '
                              'cost stack and says to set a firm maximum and stick to it [jaeWKn_Nu68 @ '
                              '00:00:52]. Chill Crayon Explains frames these as competitive auctions '
                              'rather than bargains handed out, where the real trick is calculating every '
                              'cost before placing a bid [J0zoheNKu-E @ 00:03:55]. MrDavidAdelman confirms '
                              '$100 cars exist but warns they will most likely not be in mint condition, '
                              'so kick the tires, test drive if allowed, and check the car is not a '
                              'salvage car [gnsqwRYhRPY @ 00:03:30].'],
               'table': {'caption': 'Firsthand losses, traps and the countermeasures practitioners teach',
                         'headers': ['Failure Mode',
                                     'What Happened or Was Measured',
                                     'Countermeasure Taught',
                                     'Expert Source'],
                         'rows': [['Fee stacking on a cheap US Gov Bid lot',
                                   'A $10 pair of jack stands became about $100 after wire processing and '
                                   'bank fees',
                                   'Save US Gov Bid for higher-dollar buys where total fees stayed under '
                                   '3%',
                                   'East Coast Classics ([q09PUtJPIxs @ 00:03:09])'],
                                  ['Trusting photos and description without seeing it',
                                   'A car that read good and looked good online turned out a smelly former '
                                   'K9 car',
                                   'Make the phone call, schedule an appointment and physically inspect '
                                   'before any bid',
                                   'East Coast Classics ([q09PUtJPIxs @ 00:05:55])'],
                                  ['Leaving a won vehicle past the pickup deadline',
                                   'Montgomery County charges a daily storage fee, then forfeits the '
                                   'vehicle with no refund',
                                   'Line up a tow truck or car shipper before the auction ever ends',
                                   'UX Auctions ([Z87d62pWVEk @ 00:17:42])'],
                                  ['Missing the payment deadline after winning the lot',
                                   'Late payers can lose the vehicle and some sites block them from '
                                   'bidding again',
                                   'Have money lined up and know the exact deadline before the auction '
                                   'closes',
                                   'UX Auctions ([Z87d62pWVEk @ 00:17:24])'],
                                  ['Shipping costs eating a below-market purchase',
                                   'Condition is often unknown, there are no returns, and shipping erodes '
                                   'margin fast',
                                   'Know exactly what you are looking at before you place any bid',
                                   'GovAuctions ([x8_btciMVuY @ 00:01:23])'],
                                  ['Showing up to a bargain with no transport',
                                   'A pallet of computers sold below the price of one computer, but no '
                                   'truck',
                                   'Do the research and prepare hauling ahead so the treasure can actually '
                                   'leave',
                                   'MrDavidAdelman ([gnsqwRYhRPY @ 00:05:28])'],
                                  ['Buying equipment attachments that do not fit',
                                   'Vehicle and heavy equipment attachments may not work with the machine '
                                   'you own',
                                   'Confirm the attachment works with the exact equipment you plan to '
                                   'install it on',
                                   'homebusinessmag ([pRzKRg71z4s @ 00:20:42])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Four Kill Switches Before You Place a Bid',
                           'body': 'Every item below comes from a loss, forfeiture or bad buy the '
                                   'practitioners reported. If any one fails, pass on the lot and wait for '
                                   'the next sale.',
                           'items': ["Read the terms of sale for payment method and deadline, buyer's "
                                     'premium, pickup window, and whether you get a title or a bill of '
                                     'sale, because this is where people get burned [UX Auctions — '
                                     'Z87d62pWVEk @ 00:06:20].',
                                     'Walk away from frame rust you can poke through, any flood sign such '
                                     'as a musty smell, damp carpet or water line, or a VIN that does not '
                                     'match the listing [UX Auctions — Z87d62pWVEk @ 00:11:50].',
                                     'Confirm the removal window, which ran from seven days down to two, '
                                     'and how the vehicle legally leaves the lot, temporary tag or tow, '
                                     'before bidding [East Coast Classics — q09PUtJPIxs @ 00:06:23].',
                                     "Price in sales tax, buyer's premiums and shipping fees, then set a "
                                     'firm maximum bid that fits the budget and stick to it [The Salmon '
                                     'Runs — jaeWKn_Nu68 @ 00:00:52].']}}],
 'pull_quote': '"Take your number, write it down and stick to it. If the bidding goes past it, let it go. '
               'There\'s another sale next week." — UX Auctions (Z87d62pWVEk @ 00:13:51).',
 'diagram_id': 'diag-01',
 'action_checklist': ['Search public auctions and public surplus separately for your city, county and '
                      'state, since each may sell through a different platform such as US Gov Bid, '
                      'GovDeals or Public Surplus [East Coast Classics — q09PUtJPIxs @ 00:01:25].',
                      'Register as a bidder on each platform you find, budgeting the $100 one-time US Gov '
                      'Bid fee and expecting free registration on GovDeals [East Coast Classics — '
                      'q09PUtJPIxs @ 00:02:09].',
                      'Pull real winning bids for the same year, model and state from recent months and '
                      'use the middle price, not the highest or lowest [UX Auctions — Z87d62pWVEk @ '
                      '00:13:14].',
                      'Inspect in person with a flashlight, rag, gloves, phone and an OBD2 scanner, or '
                      'hire a mobile ASE-certified inspection service if the yard allows outside '
                      'inspectors [UX Auctions — Z87d62pWVEk @ 00:10:36].',
                      'Enter a proxy bid at the maximum you are willing to pay so GSA Auctions bids on '
                      'your behalf only as much as needed to lead [GSA (General Services Administration) — '
                      'JzuRczRAlW8 @ 00:02:03].',
                      'After winning, confirm payment processed, bring valid ID and proof of payment to '
                      'pickup, and inspect the item on site against its description [The Salmon Runs — '
                      'jaeWKn_Nu68 @ 00:01:41].'],
 'statutory_citations': [{'title': 'East Coast Classics — HOW TO FIND and BUY at Government Surplus '
                                   'Auctions [00:02:39]',
                          'url': 'https://www.youtube.com/watch?v=q09PUtJPIxs&t=159s',
                          'relevance': 'Primary practitioner testimony on US Gov Bid, GovDeals and Public '
                                       'Surplus fees, payment limits and firsthand Crown Victoria '
                                       'inspections.'},
                         {'title': 'UX Auctions — How to Buy at Government Auctions: Police Cars & Surplus '
                                   'Vehicles [00:06:20]',
                          'url': 'https://www.youtube.com/watch?v=Z87d62pWVEk&t=380s',
                          'relevance': 'Primary practitioner testimony on terms of sale, inspection '
                                       'walk-away signals, middle-price valuation and post-win deadlines.'},
                         {'title': 'GSA (General Services Administration) — GSA Auctions: Online Bidding '
                                   'Opportunities [00:02:03]',
                          'url': 'https://www.youtube.com/watch?v=JzuRczRAlW8&t=123s',
                          'relevance': 'Primary practitioner testimony on proxy bidding, tie-break rules, '
                                       'inactivity periods and Buy Now mechanics.'},
                         {'title': 'homebusinessmag — Government Auctions – A Great Resource for Your '
                                   'Business or as its Own Start-up [00:15:01]',
                          'url': 'https://www.youtube.com/watch?v=pRzKRg71z4s&t=901s',
                          'relevance': 'Primary practitioner testimony on buyer-beware diligence, '
                                       "non-runner upside and resale flipping playbooks from Municibid's "
                                       'founder.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'q09PUtJPIxs',
                       'title': 'HOW TO FIND and BUY at Government Surplus Auctions',
                       'channel': 'East Coast Classics',
                       'author': 'East Coast Classics',
                       'text': 'Even though US Gov Bid started charging a one-time $100 registration fee, '
                               'they still seem to have the lowest auction fees out there, at least on the '
                               'higher dollar purchases.',
                       'tip': 'Even though US Gov Bid started charging a one-time $100 registration fee, '
                              'they still seem to have the lowest auction fees out there, at least on the '
                              'higher dollar purchases.',
                       'timestamp': 159,
                       'timestamp_seconds': 159,
                       'timestamp_label': '[00:02:39]',
                       'url': 'https://www.youtube.com/watch?v=q09PUtJPIxs&t=159s',
                       'markdown': '[00:02:39](https://www.youtube.com/watch?v=q09PUtJPIxs&t=159s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'q09PUtJPIxs',
                       'title': 'HOW TO FIND and BUY at Government Surplus Auctions',
                       'channel': 'East Coast Classics',
                       'author': 'East Coast Classics',
                       'text': "That premium is different for each municipality and I've seen the premium "
                               'as low as 5% and as high as twelve and a half percent, so be aware of that '
                               'when bidding.',
                       'tip': "That premium is different for each municipality and I've seen the premium "
                              'as low as 5% and as high as twelve and a half percent, so be aware of that '
                              'when bidding.',
                       'timestamp': 252,
                       'timestamp_seconds': 252,
                       'timestamp_label': '[00:04:12]',
                       'url': 'https://www.youtube.com/watch?v=q09PUtJPIxs&t=252s',
                       'markdown': '[00:04:12](https://www.youtube.com/watch?v=q09PUtJPIxs&t=252s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Z87d62pWVEk',
                       'title': 'How to Buy at Government Auctions: Police Cars & Surplus Vehicles',
                       'channel': 'UX Auctions',
                       'author': 'UX Auctions',
                       'text': 'Take your number, write it down and stick to it. If the bidding goes past '
                               "it, let it go. There's another sale next week.",
                       'tip': 'Take your number, write it down and stick to it. If the bidding goes past '
                              "it, let it go. There's another sale next week.",
                       'timestamp': 831,
                       'timestamp_seconds': 831,
                       'timestamp_label': '[00:13:51]',
                       'url': 'https://www.youtube.com/watch?v=Z87d62pWVEk&t=831s',
                       'markdown': '[00:13:51](https://www.youtube.com/watch?v=Z87d62pWVEk&t=831s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Z87d62pWVEk',
                       'title': 'How to Buy at Government Auctions: Police Cars & Surplus Vehicles',
                       'channel': 'UX Auctions',
                       'author': 'UX Auctions',
                       'text': 'Miss the deadline and you can lose the vehicle and some sites will block '
                               'you from bidding again.',
                       'tip': 'Miss the deadline and you can lose the vehicle and some sites will block '
                              'you from bidding again.',
                       'timestamp': 1044,
                       'timestamp_seconds': 1044,
                       'timestamp_label': '[00:17:24]',
                       'url': 'https://www.youtube.com/watch?v=Z87d62pWVEk&t=1044s',
                       'markdown': '[00:17:24](https://www.youtube.com/watch?v=Z87d62pWVEk&t=1044s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'x8_btciMVuY',
                       'title': 'Are government auctions actually legit?',
                       'channel': 'GovAuctions',
                       'author': 'GovAuctions',
                       'text': 'Condition is often unknown, there are no returns, and shipping can eat '
                               'into your margin fast.',
                       'tip': 'Condition is often unknown, there are no returns, and shipping can eat into '
                              'your margin fast.',
                       'timestamp': 83,
                       'timestamp_seconds': 83,
                       'timestamp_label': '[00:01:23]',
                       'url': 'https://www.youtube.com/watch?v=x8_btciMVuY&t=83s',
                       'markdown': '[00:01:23](https://www.youtube.com/watch?v=x8_btciMVuY&t=83s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Ezeprg6O_GU',
                       'title': 'GOVERNMENT SURPLUS! Get Free & Cheap Property, Equipment, Cars & More',
                       'channel': 'Matthew Lesko',
                       'author': 'Matthew Lesko',
                       'text': 'Health centers, clinics, child care centers, schools, colleges, you get '
                               'all this stuff for free.',
                       'tip': 'Health centers, clinics, child care centers, schools, colleges, you get all '
                              'this stuff for free.',
                       'timestamp': 256,
                       'timestamp_seconds': 256,
                       'timestamp_label': '[00:04:16]',
                       'url': 'https://www.youtube.com/watch?v=Ezeprg6O_GU&t=256s',
                       'markdown': '[00:04:16](https://www.youtube.com/watch?v=Ezeprg6O_GU&t=256s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'csOCrIHnuSo',
                       'title': 'GSA Auctions Redesign',
                       'channel': 'GSA (General Services Administration)',
                       'author': 'GSA (General Services Administration)',
                       'text': 'We have also made it easier to track active bids with improved photo '
                               'viewers and color coded alerts. Yellow, 1 to 2 hours remaining. Red, less '
                               'than one hour remaining.',
                       'tip': 'We have also made it easier to track active bids with improved photo '
                              'viewers and color coded alerts. Yellow, 1 to 2 hours remaining. Red, less '
                              'than one hour remaining.',
                       'timestamp': 107,
                       'timestamp_seconds': 107,
                       'timestamp_label': '[00:01:47]',
                       'url': 'https://www.youtube.com/watch?v=csOCrIHnuSo&t=107s',
                       'markdown': '[00:01:47](https://www.youtube.com/watch?v=csOCrIHnuSo&t=107s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Dga3YkAiGmw',
                       'title': 'GSA Auctions: Offline Bidding Opportunities',
                       'channel': 'GSA (General Services Administration)',
                       'author': 'GSA (General Services Administration)',
                       'text': 'Unlike a sealed bid auction that usually has a one-time removal of '
                               'property, a term contract may require recurring removals of property over '
                               'a specified period of time.',
                       'tip': 'Unlike a sealed bid auction that usually has a one-time removal of '
                              'property, a term contract may require recurring removals of property over a '
                              'specified period of time.',
                       'timestamp': 64,
                       'timestamp_seconds': 64,
                       'timestamp_label': '[00:01:04]',
                       'url': 'https://www.youtube.com/watch?v=Dga3YkAiGmw&t=64s',
                       'markdown': '[00:01:04](https://www.youtube.com/watch?v=Dga3YkAiGmw&t=64s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'JzuRczRAlW8',
                       'title': 'GSA Auctions: Online Bidding Opportunities',
                       'channel': 'GSA (General Services Administration)',
                       'author': 'GSA (General Services Administration)',
                       'text': 'When two proxy bids compete, the greater of the two proxy limits always '
                               'wins. When two proxy bids are the same, the bidder who placed the proxy '
                               'bid first wins.',
                       'tip': 'When two proxy bids compete, the greater of the two proxy limits always '
                              'wins. When two proxy bids are the same, the bidder who placed the proxy bid '
                              'first wins.',
                       'timestamp': 143,
                       'timestamp_seconds': 143,
                       'timestamp_label': '[00:02:23]',
                       'url': 'https://www.youtube.com/watch?v=JzuRczRAlW8&t=143s',
                       'markdown': '[00:02:23](https://www.youtube.com/watch?v=JzuRczRAlW8&t=143s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'c9mCACUk14Y',
                       'title': '60-SECOND GOVERNMENT AUCTION REPORT — NOVEMBER 19, 2026!',
                       'channel': 'UX Auctions',
                       'author': 'UX Auctions',
                       'text': 'A 2019 Chevy Tahoe from the Lawrence County Sheriff listed as runs and '
                               'drives sold for $6,651.',
                       'tip': 'A 2019 Chevy Tahoe from the Lawrence County Sheriff listed as runs and '
                              'drives sold for $6,651.',
                       'timestamp': 20,
                       'timestamp_seconds': 20,
                       'timestamp_label': '[00:00:20]',
                       'url': 'https://www.youtube.com/watch?v=c9mCACUk14Y&t=20s',
                       'markdown': '[00:00:20](https://www.youtube.com/watch?v=c9mCACUk14Y&t=20s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Q4B13yVVzZQ',
                       'title': 'GovDeals New Asset Listing Experience',
                       'channel': 'GovDeals Media',
                       'author': 'GovDeals Media',
                       'text': 'For best results, run auctions for 7 to 10 days. Schedule end times Monday '
                               'through Thursday. Avoid weekends and holidays.',
                       'tip': 'For best results, run auctions for 7 to 10 days. Schedule end times Monday '
                              'through Thursday. Avoid weekends and holidays.',
                       'timestamp': 71,
                       'timestamp_seconds': 71,
                       'timestamp_label': '[00:01:11]',
                       'url': 'https://www.youtube.com/watch?v=Q4B13yVVzZQ&t=71s',
                       'markdown': '[00:01:11](https://www.youtube.com/watch?v=Q4B13yVVzZQ&t=71s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'zFGATosXViU',
                       'title': 'How to Register and Bid for GSA Real Property on RealEstateSales.gov',
                       'channel': 'GSA (General Services Administration)',
                       'author': 'GSA (General Services Administration)',
                       'text': 'Only bonafide bidders are allowed to bid on GSA real estate online auction '
                               'sales. Each property has a unique invitation for bid contract and you must '
                               'register for each property you want to bid on.',
                       'tip': 'Only bonafide bidders are allowed to bid on GSA real estate online auction '
                              'sales. Each property has a unique invitation for bid contract and you must '
                              'register for each property you want to bid on.',
                       'timestamp': 251,
                       'timestamp_seconds': 251,
                       'timestamp_label': '[00:04:11]',
                       'url': 'https://www.youtube.com/watch?v=zFGATosXViU&t=251s',
                       'markdown': '[00:04:11](https://www.youtube.com/watch?v=zFGATosXViU&t=251s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Ie7zxVOXjeE',
                       'title': 'How government surplus auctions work in 60 seconds',
                       'channel': 'GovAuctions',
                       'author': 'GovAuctions',
                       'text': 'Online auctions typically run for 3 to 10 days, then you have 5 to 15 '
                               'business days to pay.',
                       'tip': 'Online auctions typically run for 3 to 10 days, then you have 5 to 15 '
                              'business days to pay.',
                       'timestamp': 81,
                       'timestamp_seconds': 81,
                       'timestamp_label': '[00:01:21]',
                       'url': 'https://www.youtube.com/watch?v=Ie7zxVOXjeE&t=81s',
                       'markdown': '[00:01:21](https://www.youtube.com/watch?v=Ie7zxVOXjeE&t=81s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'pRzKRg71z4s',
                       'title': 'Government Auctions – A Great Resource for Your Business or as its Own '
                                'Start-up',
                       'channel': 'homebusinessmag',
                       'author': 'homebusinessmag',
                       'text': 'It could just be a matter of a battery, a 70 dollar battery, now the car '
                               'runs.',
                       'tip': 'It could just be a matter of a battery, a 70 dollar battery, now the car '
                              'runs.',
                       'timestamp': 950,
                       'timestamp_seconds': 950,
                       'timestamp_label': '[00:15:50]',
                       'url': 'https://www.youtube.com/watch?v=pRzKRg71z4s&t=950s',
                       'markdown': '[00:15:50](https://www.youtube.com/watch?v=pRzKRg71z4s&t=950s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'jaeWKn_Nu68',
                       'title': 'How To Buy From Government Auctions - Step By Step',
                       'channel': 'The Salmon Runs',
                       'author': 'The Salmon Runs',
                       'text': 'If you win, pay close attention to the payment deadlines, which are often '
                               'strict, typically within two to three business days.',
                       'tip': 'If you win, pay close attention to the payment deadlines, which are often '
                              'strict, typically within two to three business days.',
                       'timestamp': 68,
                       'timestamp_seconds': 68,
                       'timestamp_label': '[00:01:08]',
                       'url': 'https://www.youtube.com/watch?v=jaeWKn_Nu68&t=68s',
                       'markdown': '[00:01:08](https://www.youtube.com/watch?v=jaeWKn_Nu68&t=68s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'J0zoheNKu-E',
                       'title': 'Government Surplus Auctions Where You Can Buy Things For Pennies On The '
                                'Dollar',
                       'channel': 'Chill Crayon Explains',
                       'author': 'Chill Crayon Explains',
                       'text': 'The real trick is finding legitimate government listings, researching the '
                               'items condition and market value, and calculating every cost before '
                               'placing a bid.',
                       'tip': 'The real trick is finding legitimate government listings, researching the '
                              'items condition and market value, and calculating every cost before placing '
                              'a bid.',
                       'timestamp': 235,
                       'timestamp_seconds': 235,
                       'timestamp_label': '[00:03:55]',
                       'url': 'https://www.youtube.com/watch?v=J0zoheNKu-E&t=235s',
                       'markdown': '[00:03:55](https://www.youtube.com/watch?v=J0zoheNKu-E&t=235s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'gnsqwRYhRPY',
                       'title': 'A Guide to Government Auction Sites',
                       'channel': 'MrDavidAdelman',
                       'author': 'MrDavidAdelman',
                       'text': 'I have seen a pallet of computers go for less than the cost of a single '
                               'computer, because I was in the right place at the right time, but without '
                               'a truck.',
                       'tip': 'I have seen a pallet of computers go for less than the cost of a single '
                              'computer, because I was in the right place at the right time, but without a '
                              'truck.',
                       'timestamp': 328,
                       'timestamp_seconds': 328,
                       'timestamp_label': '[00:05:28]',
                       'url': 'https://www.youtube.com/watch?v=gnsqwRYhRPY&t=328s',
                       'markdown': '[00:05:28](https://www.youtube.com/watch?v=gnsqwRYhRPY&t=328s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ubzNe62V_y4',
                       'title': 'Best Government Auction Sites: GSA vs GovDeals vs Public Surplus',
                       'channel': 'GovAuctions',
                       'author': 'GovAuctions',
                       'text': 'Rather than checking each site by hand every day, make a habit of setting '
                               'a regular schedule and keeping a short list of categories and locations '
                               'you care about.',
                       'tip': 'Rather than checking each site by hand every day, make a habit of setting a '
                              'regular schedule and keeping a short list of categories and locations you '
                              'care about.',
                       'timestamp': 81,
                       'timestamp_seconds': 81,
                       'timestamp_label': '[00:01:21]',
                       'url': 'https://www.youtube.com/watch?v=ubzNe62V_y4&t=81s',
                       'markdown': '[00:01:21](https://www.youtube.com/watch?v=ubzNe62V_y4&t=81s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'}]}
