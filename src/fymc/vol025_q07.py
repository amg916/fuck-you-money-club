from __future__ import annotations

CHAPTER_7 = {'id': 'Q7',
 'chapter_id': 'Q7',
 'chapter_number': 7,
 'question_number': 7,
 'slug': 'quote-to-cash-pricing-load-operations-payment',
 'question_prompt': 'How do I price a load, run it through my TMS, invoice it, and make sure cash keeps '
                    'flowing to me and my carriers?',
 'kicker': 'Q7 / THE BIG MONEY PLAYBOOKS',
 'title': 'Quote to Cash: Pricing, Load Operations and Payment',
 'subtitle': 'The four key numbers for pricing a first load, DAT/Truckstop rate data, freight pricing AI, '
             'how brokers think on rate calls, TMS operations workflows, invoicing and margin, quick pay '
             'vs. factoring',
 'layout_template': 'thirty_day_roadmap',
 'reading_time_minutes': 15,
 'executive_summary': 'Brokers price from the truck up. They collect every load detail, pull DAT and '
                      'FreightWaves lane data from several sources, fix an expected buy rate, and only '
                      'then add margin. ShipLeague quotes about $1,850 on a lane where the truck should '
                      'take about $1,700 and calls 15% standard. FreightBrokers works four numbers ($1,300 '
                      'buy, $250 target, $1,550 sell, $1,350 ceiling) and books the truck at $1,325. Every '
                      'money-side speaker separates gross from net and profit from cash: a $300 gross '
                      'becomes $225 net, and 30-to-90-day terms force a choice. Quick pay costs 1-5% and '
                      "covers one broker's loads. Factoring costs roughly 3-5% and advances 80-90% inside "
                      '24 hours. Practitioners split on quick pay versus factoring, on which AscendTMS '
                      'perks are free, and on whether factoring rescues a thin operation or just helps it '
                      'lose money faster.',
 'key_metrics': [{'label': 'Standard Broker Margin on a Quoted Lane',
                  'metric': 'Standard Broker Margin on a Quoted Lane',
                  'value': '15% (about $1,850 quoted against about $1,700 expected truck pay)',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Margin applied on a 766-mile Atlanta, GA to Vineland, NJ van lane priced off '
                             'DAT RateView 30-day and 7-day data',
                  'source': 'ShipLeague ([rMpa5pbBWtI @ 00:04:10])'},
                 {'label': 'Net Profit Kept From a $300 Gross Margin',
                  'metric': 'Net Profit Kept From a $300 Gross Margin',
                  'value': '$225 net after about $75 of expenses',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'A $2,100 shipper rate and an $1,800 carrier rate, less load board, TMS, '
                             'insurance, bond, phones, accounting and factoring costs',
                  'source': 'FreightBrokers ([Lpq9AHrz7nQ @ 00:05:20])'},
                 {'label': 'Broker Quick Pay Fee and Speed',
                  'metric': 'Broker Quick Pay Fee and Speed',
                  'value': '1-5% fee for payment in 2-7 days',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Quick pay replaces standard 30-60 day terms but only applies to that one '
                             "broker's loads",
                  'source': 'Porter Capital ([iJE2rZFL57E @ 00:00:13])'},
                 {'label': 'Factoring Advance Rate and Funding Window',
                  'metric': 'Factoring Advance Rate and Funding Window',
                  'value': 'About 80-90% advanced, usually within 24 hours',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Factor advances most of the invoice, collects from the customer, deducts its '
                             'fee and remits the remainder',
                  'source': 'Porter Capital ([R4i90VgyHqk @ 00:00:00])'}],
 'sections': [{'title': 'The Practitioner Consensus',
               'paragraphs': ['Every pricing practitioner works backward from the truck. FreightBrokers '
                              'refuses to touch a number until the pickup and delivery details, '
                              'appointment times, commodity, weight, equipment, driver assist, extra stops '
                              'and special instructions are collected, because a firm 6:00 a.m. delivery '
                              'prices differently than "anytime Friday." The carrier figure (the truck or '
                              'buy rate) then gets built from lane data, load boards, past company pay and '
                              'direct carrier calls, never from one source alone [HTQaqqy_CPs @ 00:00:56]. '
                              'ShipLeague runs the same play with DAT RateView and FreightWaves. They set '
                              'granularity to "Market" 99% of the time and fix an expected truck pay '
                              'before a single dollar of margin goes on top [rMpa5pbBWtI @ 00:01:22]. '
                              "Tony's Topics treats DAT's Quick Rate Lookup as the reality check, pulling "
                              'all-in spot rates by equipment type and holding every offer against the '
                              'market [wOpAqd5AALo @ 00:02:58]. The second FreightBrokers lesson frames '
                              'the output: research the lane, the market and the carriers, then quote. The '
                              'result is two separate agreements, one with the shipper and one with the '
                              'carrier [Lpq9AHrz7nQ @ 00:01:55]. The order of operations never flips. '
                              'Shipper price equals buy rate plus a deliberate gross profit, and the '
                              "broker's spread lives between two contracts that are negotiated separately "
                              'and paid on separate clocks.',
                              "Gross margin is not take-home pay. FreightBrokers' worked load has the "
                              'shipper paying $2,100 and the carrier receiving $1,800. That $300 gross '
                              'margin is "not necessarily what you actually keep." After roughly $75 of '
                              'load board, TMS, insurance, bond, phone, accounting and factoring expenses, '
                              'net lands at $225. The same lesson warns that invoiced is not paid: owe ten '
                              'carriers and $18,000 leaves the building before the first shipper check '
                              'clears, because "you can have a load that\'s profitable on paper and still '
                              'have a cash flow problem" [Lpq9AHrz7nQ @ 00:05:20]. BLACK BEAR FREIGHT & '
                              'LOGISTICS makes the identical point from the carrier seat. Brokers and '
                              'shippers pay in 30, 45 or 60 days, while fuel, insurance, drivers, truck '
                              'payments and repairs do not wait. Profit measures sustainability; cash flow '
                              'measures the ability to pay bills [ZYkg1UepLL4 @ 00:01:47]. Porter Capital '
                              'puts standard terms at 30-60 days [iJE2rZFL57E @ 00:00:00]. Bumble Bee '
                              'Dispatch stretches that to 30-90 days and notes that startup costs drain '
                              'cash before the first payment ever lands [dTOcCujNdaw @ 00:00:50]. The '
                              'shared answer is to fund the float through working capital, a credit line, '
                              'quick pay or factoring, and to price every load knowing none of those '
                              'options is free money.',
                              'Paperwork is the trigger that turns a delivered load into money. '
                              'FreightBrokers ties both invoices to the proof of delivery. The POD '
                              'releases the $1,800 carrier invoice and the $2,100 shipper invoice, and any '
                              'detention, lumper or extra-stop charge needs its own documentation to get '
                              "paid [Lpq9AHrz7nQ @ 00:02:48]. In FreightWaves' Rose Rocket demo, Rob "
                              'Dougherty automates that hinge: same-day invoicing fires the moment the POD '
                              'is uploaded and syncs straight to accounting [MobEZyaIjV4 @ 00:04:37]. '
                              'AscendTMS teaches the same discipline from inside the software. Supporting '
                              'documents must be uploaded, typed and attached or they sit "unprocessed." '
                              'Factoring runs through partner companies with an NOA stamp, and a load paid '
                              'in full earns the "green rectangle of victory" [ICIyOtMiEqY @ 00:24:58]. '
                              "Steve's longer Ascend training adds that the ready-for-accounting tab is a "
                              'staging area for collecting paperwork, and that adding an income pay item '
                              '"is what trips ascend tms to generate an invoice document" [idL8PXMlKjQ @ '
                              '00:45:31]. Across a vendor demo, a free TMS and a broker training channel, '
                              'the operating baseline is identical. No POD means no invoice. No attached '
                              'document means no payment. The back office runs off load status and logged '
                              "documents rather than anyone's memory of what happened on the road."],
               'table': {'caption': 'Where the practitioners line up on quote-to-cash fundamentals',
                         'headers': ['Consensus Point',
                                     'What Practitioners Actually Do',
                                     'Number or Rule Stated',
                                     'Expert Source'],
                         'rows': [['Build every quote upward from the truck buy rate',
                                   'Collect all load details first, then estimate carrier pay from several '
                                   'sources',
                                   'Research range $1,250-$1,350 with a $1,300 working carrier figure',
                                   'FreightBrokers ([HTQaqqy_CPs @ 00:01:26])'],
                                  ['Check every offer against live market lane data',
                                   'Pull DAT Quick Rate Lookup by equipment type before quoting or '
                                   'accepting',
                                   'Los Angeles to Chicago van at $1.90 per mile over 2,025 miles',
                                   "Tony's Topics ([wOpAqd5AALo @ 00:01:50])"],
                                  ['Gross margin on a load is not what you keep',
                                   'Subtract load board, TMS, insurance, bond, phones, accounting and '
                                   'factoring costs',
                                   '$300 gross margin nets $225 after about $75 of expenses',
                                   'FreightBrokers ([Lpq9AHrz7nQ @ 00:05:20])'],
                                  ['Standard payment terms open a real cash gap',
                                   'Plan for brokers and shippers paying long after the truck delivers',
                                   'Standard terms run 30-60 days while quick pay lands in 2-7',
                                   'Porter Capital ([iJE2rZFL57E @ 00:00:00])'],
                                  ['Factoring is a cash-flow tool and never a rate fix',
                                   'Sell invoices for speed but never use factoring to cover bad rates',
                                   'Factoring may only help you lose money more efficiently, per the '
                                   'speaker',
                                   'BLACK BEAR FREIGHT & LOGISTICS ([ZYkg1UepLL4 @ 00:01:47])'],
                                  ['Proof of delivery triggers billing on both sides of the load',
                                   'Upload the POD to release carrier and shipper invoices the same day',
                                   'Same-day invoicing synced to accounting the moment the POD is uploaded',
                                   'FreightWaves ([MobEZyaIjV4 @ 00:04:37])'],
                                  ['Vet every carrier by MC number before booking any freight',
                                   "Search every caller's MC or DOT number for FMCSA data by habit",
                                   'Presenter avoids carriers showing thin FMCSA data on authority and '
                                   'inspections',
                                   'AscendTMS - The Free (and Best) TMS Software ([ICIyOtMiEqY @ '
                                   '00:15:42])']]}},
              {'title': 'Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ["ShipLeague's worked lane is a van from Atlanta, GA to Vineland, NJ, 766 "
                              'miles. June ran a $2,183 high and a $1,670 low. The 3-day pull showed a '
                              '$1,609 average, a $1,678 high and a $1,532 low, but they distrust that dip '
                              'because the 7-, 15- and 30-day figures sit within $8 of each other, so '
                              'expected truck pay is about $1,678 [rMpa5pbBWtI @ 00:02:17]. The market '
                              'read "+100 very tight" (red is tight, blue is loose). They ignore forecasts '
                              'and let the 30-day and 7-day data rule. Expecting roughly $1,700 to the '
                              'truck, they quote about $1,850 and call 15% margin "pretty standard" '
                              '[rMpa5pbBWtI @ 00:04:10]. FreightBrokers formalizes the math into four '
                              'numbers on a Buffalo, NY to Newark, NJ dry van carrying about 22,000 lb of '
                              'non-stackable furniture. A $1,300 estimated carrier rate plus a $250 target '
                              'gross profit equals a $1,550 customer rate. With a $200 profit floor, the '
                              'maximum carrier rate is $1,350 [HTQaqqy_CPs @ 00:04:26]. The quote goes out '
                              'as "$1,550" with no apology and no "10-minute song and dance." It states '
                              'what is included and holds through end of day. The carrier booked at $1,325 '
                              'for $225 gross [HTQaqqy_CPs @ 00:06:29], because knowing the ceiling lets '
                              'the broker negotiate with confidence.',
                              "Data access is tiered, and the tier decides what you can see. Tony's Topics "
                              "lays out DAT's ladder. DAT One Standard carries no lane rates, Enhanced "
                              'shows a 30-day average, and the other three tiers show 15-day data, so the '
                              'working minimum is DAT One Pro at $135 a month via Tools > Quick Rate '
                              'Lookup. Los Angeles to Chicago at 2,025 miles priced van at $1.90 per mile, '
                              'reefer at $2.21 and flatbed at $2.14, all-in spot [wOpAqd5AALo @ 00:02:14]. '
                              'ShipLeague\'s new-lane safety net is "make or break even": price in 150 '
                              'miles of deadhead so the worst case breaks even, and keep doing it until '
                              'the lane is learned [rMpa5pbBWtI @ 00:04:55]. Margin goes up for an '
                              'undesirable or loose destination, or for freight that is overweight, '
                              'oversized, tarp-damaging, needs ramps or load levelers, needs driver '
                              'assist, or loads slowly. Capacity comes from Lane Makers filtered to full '
                              'truckload, van, 30 days. A carrier that posted the lane nine times gets the '
                              '"three a month" pitch [rMpa5pbBWtI @ 00:07:16]. Freight Broker 911 sells '
                              'the automated version: instant quotes in about 10 seconds built from market '
                              'data, lane history, fuel and capacity. Pricing is $0 for the first 30 days '
                              'and stays $0 with an active shipper and at least one shipment per 30 days; '
                              'otherwise it is $149 a month [edDHTJiH5HM @ 00:00:34].',
                              "Inside the TMS, the numbers become documents and deductions. Steve's "
                              'AscendTMS build sets income at $2.30 per mile, then cuts it to $1.90 per '
                              'mile for $2,205.90 on 1,161 miles. The carrier gets a flat $1,800 with a '
                              '$75 extra-stop option, and a 4% quick-pay fee comes off the top: "four '
                              'percent of 1800 is 72," held back from the carrier\'s pay [idL8PXMlKjQ @ '
                              '00:48:51]. The 2024 Ascend walkthrough shows $3,000 flat income against a '
                              '$2,000 flat expense, with gross profit and percentage displayed. It '
                              'auto-generates the bill of lading, carrier confirmation, customer '
                              'confirmation and invoice. A driver document request texts a link, and the '
                              'upload attaches straight to the load [Eycc6Jod6t4 @ 00:16:17]. On the '
                              "payment side, quick pay is priced broker by broker. Trucking From Scratch's "
                              'David McGill describes 2-, 5- or 14-day tiers, each at a different '
                              'percentage, with payment instructions printed on the rate confirmation '
                              '[K9UPJJr_uzQ @ 00:00:17]. Brandon Manney puts broker quick pay at about '
                              '2-3% within roughly 7 days, against factoring at 3-5% within 24 hours, '
                              'which on a $1,000 invoice works out to "$50 plus whatever other fees" '
                              "[i6KVZJUOBqs @ 00:02:21]. The broker's spread and the carrier's cost of "
                              'speed get settled on the same invoice.'],
               'table': {'caption': 'Street mechanics with the exact figures practitioners used',
                         'headers': ['Mechanic', 'Exact Execution Step', 'Stated Numbers', 'Expert Source'],
                         'rows': [['Reading a lane before quoting the shipper',
                                   'Trust the 30-day and 7-day data, ignore forecasts and short dips',
                                   'About $1,700 expected truck pay, about $1,850 quoted at 15%',
                                   'ShipLeague ([rMpa5pbBWtI @ 00:04:10])'],
                                  ['Setting a hard ceiling on carrier pay',
                                   'Subtract the minimum acceptable profit from the customer rate before '
                                   'calling trucks',
                                   '$1,550 customer rate minus $200 floor equals $1,350 maximum',
                                   'FreightBrokers ([HTQaqqy_CPs @ 00:04:26])'],
                                  ['Unlocking DAT lane rates for spot quoting',
                                   'Upgrade past DAT One Standard and use Tools, then Quick Rate Lookup',
                                   'DAT One Pro at $135 a month shows 15-day lane rates',
                                   "Tony's Topics ([wOpAqd5AALo @ 00:00:49])"],
                                  ['Protecting a brand-new lane from a loss',
                                   'Price 150 miles of deadhead into the quote so worst case breaks even',
                                   '150 deadhead miles built in until the lane is fully learned',
                                   'ShipLeague ([rMpa5pbBWtI @ 00:04:55])'],
                                  ['Holding back a carrier quick-pay fee in the TMS',
                                   'Apply the quick-pay percentage to the flat carrier rate inside '
                                   'financials',
                                   '4% of an $1,800 carrier rate equals $72 held back',
                                   'AscendTMS - The Free (and Best) TMS Software ([idL8PXMlKjQ @ '
                                   '00:48:51])'],
                                  ['Counting the full cost of broker quick pay',
                                   'Add the transfer fee on top of the quick-pay percentage before '
                                   'accepting',
                                   '5% plus a $25-29 Comchek fee on the example load',
                                   'Bumble Bee Dispatch ([dTOcCujNdaw @ 00:04:20])'],
                                  ['Getting a factoring advance on a delivered load',
                                   'Sell the invoice, factor collects from the customer and remits '
                                   'remainder',
                                   'About 80-90% advanced, usually funded within 24 hours of submission',
                                   'Porter Capital ([R4i90VgyHqk @ 00:00:00])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Small habits that protect the margin and the money',
                           'body': 'Operator-level habits practitioners use to keep quotes honest, data '
                                   'clean and receivables moving.',
                           'items': ['Do not chase a 3-day rate dip: if the 7-, 15- and 30-day figures sit '
                                     'within $8 of each other, price to the higher read, about $1,678 on '
                                     'the Atlanta to Vineland lane [ShipLeague — rMpa5pbBWtI @ 00:02:17]',
                                     'Add every new location through the Google-powered lookup, because it '
                                     '"mostly eliminates human error" like transposed numbers or wrong '
                                     'states and gives the best address format for load boards [AscendTMS '
                                     '- The Free (and Best) TMS Software — Eycc6Jod6t4 @ 00:12:52]',
                                     'Export the AR/AP report and work it as a collection sheet, using the '
                                     'KPI summary of revenue, expenses, profit, per-mile figures and gross '
                                     'margin percentage to spot weak lanes [AscendTMS - The Free (and '
                                     'Best) TMS Software — ICIyOtMiEqY @ 00:21:04]',
                                     'Refresh load board postings on a schedule, because "it does get '
                                     'stale on the load boards" and stale posts stop pulling carrier calls '
                                     '[AscendTMS - The Free (and Best) TMS Software — idL8PXMlKjQ @ '
                                     '01:01:31]']},
               'sop_steps': [{'step': 1,
                              'title': 'Lock the load details',
                              'action': 'Capture pickup and delivery times, commodity, weight, equipment, '
                                        'driver assist, extra stops and special instructions before '
                                        'pricing.',
                              'detail': 'A firm 6:00 a.m. delivery prices differently than "anytime '
                                        'Friday," so never quote off origin and destination alone '
                                        '[FreightBrokers — HTQaqqy_CPs @ 00:00:56]'},
                             {'step': 2,
                              'title': 'Set the four numbers',
                              'action': 'Estimate the carrier rate from multiple sources, add target gross '
                                        'profit, set the customer rate, then derive the maximum carrier '
                                        'rate.',
                              'detail': '$1,300 carrier plus $250 profit equals $1,550; minus the $200 '
                                        'floor gives a $1,350 ceiling, and the load booked at $1,325 '
                                        '[FreightBrokers — HTQaqqy_CPs @ 00:04:26]'},
                             {'step': 3,
                              'title': 'Vet the carrier and build the load',
                              'action': "Run the caller's MC through universal search, then build the load "
                                        'with stops, miles and financials in the TMS.',
                              'detail': 'An MC search triggers FMCSA verification plus a fraud alert, and '
                                        'broker-authority MCs also get a Triumph Business Capital credit '
                                        'check [AscendTMS - The Free (and Best) TMS Software — idL8PXMlKjQ '
                                        '@ 00:11:15]'},
                             {'step': 4,
                              'title': 'Bill on POD and price the payment rail',
                              'action': 'Release carrier and shipper invoices off the POD, then choose '
                                        'quick pay or factoring with total cost in writing.',
                              'detail': 'Get a written total-cost example for payment at 15, 30, 45 and 60 '
                                        'days, since tiered fees can rise every 10, 15 or 30 days [BLACK '
                                        'BEAR FREIGHT & LOGISTICS — ZYkg1UepLL4 @ 00:04:11]'}]},
              {'heading': 'Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The loudest split in getting paid is quick pay versus factoring, and the '
                              'practitioners land on different sides depending on how many brokers a truck '
                              'hauls for. Porter Capital frames quick pay as a 2-to-7-day payout costing 1 '
                              "to 5 percent, good only for that one broker's loads, and says one broker "
                              'with solid quick pay may be all a carrier needs while multi-broker scaling '
                              'calls for factoring [iJE2rZFL57E @ 00:01:14]. David McGill of Trucking From '
                              'Scratch goes further and prefers factoring outright: twenty to fifty '
                              'brokers means twenty to fifty invoicing processes, while a factor is one '
                              'portal or one email, a standardized process that can be delegated to an '
                              'admin hire, and some brokers do not offer quick pay at all [K9UPJJr_uzQ @ '
                              '00:02:43]. Brandon Manney prices the trade-off in plain numbers, quick pay '
                              'at roughly 2 to 3 percent inside about seven days against factoring at 3 to '
                              '5 percent inside 24 hours [i6KVZJUOBqs @ 00:02:21]. Courtney at Bumble Bee '
                              'Dispatch counters that quick pay is not as cheap as it looks once a 5 '
                              'percent fee stacks with a $25 to $29 Comchek fee, and steers carriers '
                              'toward same-day or next-day factoring deposits [dTOcCujNdaw @ 00:04:20].',
                              'On pricing, the split is percentage margin versus fixed-dollar margin, and '
                              'how much data to trust. ShipLeague pulls DAT RateView at Market '
                              'granularity, ignores forecasts, leans on 30-day and 7-day figures, expects '
                              'about $1,700 to the truck on a 766-mile Atlanta to Vineland van lane and '
                              'quotes about $1,850, calling 15 percent margin pretty standard [rMpa5pbBWtI '
                              '@ 00:04:10]. FreightBrokers rejects any fixed rule, stating there is no '
                              'magic profit amount, and instead stacks a $250 gross profit on a $1,300 '
                              'carrier estimate to land a $1,550 customer rate, then works backward to a '
                              "$1,350 ceiling for the truck [HTQaqqy_CPs @ 00:04:11]. Tony's Topics takes "
                              'the subscription route, insisting lane rates need at least DAT One Pro at '
                              '$135 a month, and shrugs that there is not much difference between 45 and '
                              '135 [wOpAqd5AALo @ 00:03:16]. Freight Broker 911 skips manual research '
                              'altogether with an AI engine that returns instant quotes in about ten '
                              'seconds off market data, lane history, fuel and capacity, at $0 for the '
                              'first 30 days and $0 after that only with an active shipper moving at least '
                              'one shipment every 30 days, otherwise $149 a month [edDHTJiH5HM @ '
                              '00:00:34].',
                              'The playbooks also diverge on who owns the customer and the carrier '
                              'relationship. Mike Gray, appearing on Entre Mike, onboarded 14 direct '
                              'shippers in a single year and kept only 2 or 3 of them, warning that direct '
                              'shippers pay in 30 to 45 days and demand a system just to track invoices '
                              '[oytUZVvyF80 @ 00:24:33]. FreightBrokers offers the agent route as the '
                              'alternative to building all of that alone: a 60 percent split of a $300 '
                              "margin leaves the agent $180, traded for the host brokerage's authority, "
                              'systems, credit and carrier network, with a blunt instruction to read the '
                              'agreement first [Lpq9AHrz7nQ @ 00:06:52]. Dispatchers split the room '
                              'hardest. Gray says they bring negative sales skills and that a broker like '
                              'Gray would pay a confident carrier two or three hundred dollars more, while '
                              'the host adds a firsthand case of a dispatcher booking lower rates than the '
                              "host's fiancé did and says dispatcher contact info in the packet adds "
                              'friction [oytUZVvyF80 @ 00:10:19]. Yet the same conversation concedes that '
                              'a carrier who lacks sales skills should hire a dispatcher anyway, with the '
                              'host warning that the dispatcher then owns the broker relationship instead '
                              'of the carrier [oytUZVvyF80 @ 00:31:06].'],
               'table': {'caption': 'Quote-to-cash forks: where named operators pick opposite playbooks',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Getting paid with one broker versus many brokers',
                                   'Single-broker carrier with solid quick pay can skip factoring entirely',
                                   'Multi-broker scaling needs factoring; one portal replaces 20 to 50 '
                                   'invoicing processes',
                                   'Porter Capital ([iJE2rZFL57E @ 00:01:14]); Trucking From Scratch '
                                   '([K9UPJJr_uzQ @ 00:02:43])'],
                                  ['Price of speed when cashing a delivered load',
                                   'Broker quick pay runs about 2 to 3 percent inside roughly seven days',
                                   'Factoring runs 3 to 5 percent but funds the invoice inside 24 hours',
                                   'Brandon Manney The Mentor ([i6KVZJUOBqs @ 00:02:21])'],
                                  ['Margin rule applied on top of the truck rate',
                                   'Target about 15 percent over expected truck pay, called pretty '
                                   'standard',
                                   'No magic profit amount; set a $250 dollar target with a $200 floor',
                                   'ShipLeague ([rMpa5pbBWtI @ 00:04:10]); FreightBrokers ([HTQaqqy_CPs @ '
                                   '00:04:11])'],
                                  ['Where the lane rate number actually comes from',
                                   'DAT One Pro at $135 a month for 15-day lane rate averages',
                                   'AI engine returning instant quotes in about ten seconds, $0 with an '
                                   'active shipper',
                                   "Tony's Topics ([wOpAqd5AALo @ 00:03:16]); Freight Broker 911 "
                                   '([edDHTJiH5HM @ 00:00:34])'],
                                  ['Which integrated load boards come free inside AscendTMS',
                                   'Tour says 123LoadBoard, Trucker Path, NextLoad and C4 are free for '
                                   'being a customer',
                                   'Ops training scopes Trucker Path and the 123LoadBoard courtesy '
                                   'subscription to premium subscribers',
                                   'AscendTMS - The Free (and Best) TMS Software ([ICIyOtMiEqY @ '
                                   '00:06:29]); AscendTMS - The Free (and Best) TMS Software ([idL8PXMlKjQ '
                                   '@ 00:57:37])'],
                                  ['Giving the shipper self-serve visibility into the load',
                                   'Rose Rocket ships anonymous tracking links and a self-serve customer '
                                   'portal',
                                   'AscendTMS customer portal not yet available; roadmap item with managed '
                                   'services as workaround',
                                   'FreightWaves ([MobEZyaIjV4 @ 00:03:40]); AscendTMS - The Free (and '
                                   'Best) TMS Software ([idL8PXMlKjQ @ 01:06:39])'],
                                  ['Whether a carrier should book through a dispatcher',
                                   'Dispatchers have negative sales skills; a confident carrier gets two '
                                   'or three hundred more',
                                   'Lacking sales skills, hire one, but the dispatcher then owns the '
                                   'broker relationship',
                                   'Entre Mike ([oytUZVvyF80 @ 00:10:19]); Entre Mike ([oytUZVvyF80 @ '
                                   '00:31:06])']]}},
              {'heading': 'Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The first trap every practitioner hits is confusing invoiced with paid. '
                              'FreightBrokers walks a $2,100 shipper and $1,800 carrier load through '
                              'POD-triggered invoicing, then shows that owing ten carriers means $18,000 '
                              'out the door before a single shipper check lands, adding that a load can be '
                              'profitable on paper and still create a cash flow problem [Lpq9AHrz7nQ @ '
                              '00:03:21]. That same $300 gross shrinks to $225 net once roughly $75 of '
                              'load board, TMS, insurance, bond, phone, accounting and factoring expense '
                              'comes off, which is why the channel defines net profit as what remains '
                              'after the expenses of operating the business [Lpq9AHrz7nQ @ 00:04:47]. '
                              'BLACK BEAR FREIGHT & LOGISTICS hits the carrier mirror image: fuel, '
                              'insurance, drivers, truck payments and repairs do not wait for 30-, 45- or '
                              '60-day terms, and factoring will not fix low rates or high costs, since it '
                              'may only help a carrier lose money more efficiently [ZYkg1UepLL4 @ '
                              '00:01:47]. Courtney at Bumble Bee Dispatch adds the friction cost of '
                              'chasing pay without a single point of contact: five brokers in one week are '
                              'hard to track, mailed checks can take two to three weeks, and truck stops '
                              'charge to cash Comcheks [dTOcCujNdaw @ 00:05:00].',
                              'Pricing errors cut both ways. FreightBrokers opens with the stakes on a '
                              'first load: quote too high and the first customer walks, quote too low and '
                              '500 bucks evaporates, which is why the channel derives a maximum carrier '
                              'rate, $1,550 minus a $200 floor equals $1,350, and refuses to escalate '
                              'until the profit disappears; if every carrier on the board wants $1,500, '
                              'the move is to re-check the numbers or go back to the shipper [HTQaqqy_CPs '
                              '@ 00:04:26]. When a competitor quotes $1,450, the instruction is to compare '
                              'apples to apples and walk away if the margin does not work, because nobody '
                              'needs to win every quote; the worked load still booked at $1,325 for $225 '
                              'gross [HTQaqqy_CPs @ 00:05:55]. ShipLeague warns new brokers off starting '
                              'on a loss, contrasting $300 to $500 lost per load against $500 to $600 made '
                              'at peaks, and says to quote very high or pass on year-round pricing and to '
                              'ask for help before committing [rMpa5pbBWtI @ 00:11:45]. The same '
                              'ShipLeague walkthrough flags a street-level abuse: do not post loads you do '
                              'not have just to hear what carriers will haul for [rMpa5pbBWtI @ 00:09:04].',
                              'The ugliest firsthand failure is fraud. Gray recounts a hotshot that '
                              'deadheaded 400 miles near Billings, Montana for an 8:30 appointment and '
                              'rolled in at 11:00, with the driver caught taping a handwritten paper sign '
                              "over the truck's decal [oytUZVvyF80 @ 00:13:56]. The driver ran a new MC "
                              'while the booked MC was 14 months old, the dispatcher could only get loads '
                              'from TQL, and the fake trip lease meant the driver never got paid while '
                              'every party, the broker included, carried fraud liability [oytUZVvyF80 @ '
                              '00:16:34]. On the factoring side, BLACK BEAR FREIGHT & LOGISTICS lists the '
                              'contract traps that eat the advance: ACH and wire fees, same-day funding '
                              'charges, minimum volumes, processing and credit-check fees, reserves, early '
                              'termination penalties, auto-renewal and aging fees, with tiered rates '
                              'stepping up every 10, 15 or 30 days, so the carrier should demand a written '
                              'total-cost example at 15, 30, 45 and 60 days [ZYkg1UepLL4 @ 00:03:36]. '
                              'Non-recourse is narrower than it sounds, usually covering only insolvency '
                              'and excluding disputes, missing POD, claims, rate-confirmation mismatches '
                              'and refusals, so non-recourse does not necessarily mean a carrier can never '
                              'be charged back [ZYkg1UepLL4 @ 00:03:00].'],
               'table': {'caption': 'Firsthand failure modes and the economics check each practitioner '
                                    'applies',
                         'headers': ['Failure Mode',
                                     'What Happened or Was Measured',
                                     'Economics Check',
                                     'Expert Source'],
                         'rows': [['Cash gap between carrier payables and shipper receivables',
                                   'Owing ten carriers $1,800 each means $18,000 out before collecting',
                                   'Line up working capital, a credit line or factoring before adding '
                                   'volume',
                                   'FreightBrokers ([Lpq9AHrz7nQ @ 00:03:21])'],
                                  ['Accessorial charges billed without supporting paperwork',
                                   'Detention, lumper and extra stops all need documentation to bill',
                                   'Collect documentation for every detention, lumper and extra stop event',
                                   'FreightBrokers ([Lpq9AHrz7nQ @ 00:06:08])'],
                                  ['Chasing carriers upward until the margin is gone',
                                   'Buffalo to Newark load priced at $1,550 with a $200 minimum profit',
                                   'Cap carrier pay at $1,350 and re-check or return to the shipper',
                                   'FreightBrokers ([HTQaqqy_CPs @ 00:04:26])'],
                                  ['Starting a new broker book on losing loads',
                                   'Losing $300 to $500 per load versus $500 to $600 at peaks',
                                   'Quote very high or pass until the lane is actually learned',
                                   'ShipLeague ([rMpa5pbBWtI @ 00:11:45])'],
                                  ['Trip-lease fraud hiding behind a seasoned MC number',
                                   'Paper sign taped over the decal; new MC hauling under 14-month-old MC',
                                   "Search every caller's MC in the TMS and avoid carriers with thin FMCSA "
                                   'data',
                                   'Entre Mike ([oytUZVvyF80 @ 00:16:34]); AscendTMS - The Free (and Best) '
                                   'TMS Software ([ICIyOtMiEqY @ 00:15:42])'],
                                  ['Factoring contract fees eating the cash advance',
                                   'ACH, same-day, reserve, termination and aging fees plus tiered '
                                   'step-ups',
                                   'Demand a written total-cost example at 15, 30, 45 and 60 days',
                                   'BLACK BEAR FREIGHT & LOGISTICS ([ZYkg1UepLL4 @ 00:04:11])'],
                                  ['Unprocessed documents and stale load board postings',
                                   'Documents not uploaded, typed and attached stay unprocessed; postings '
                                   'go stale',
                                   'Attach every supporting document and refresh load board postings '
                                   'periodically',
                                   'AscendTMS - The Free (and Best) TMS Software ([ICIyOtMiEqY @ '
                                   '00:24:58]); AscendTMS - The Free (and Best) TMS Software ([idL8PXMlKjQ '
                                   '@ 01:01:31])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Stop Before Booking, Signing or Scaling',
                           'body': 'Each check below comes from a loss, a fraud case or a cash crunch a '
                                   'practitioner reported firsthand. Clear all four before the next load '
                                   'moves.',
                           'items': ['Never book a carrier above your maximum carrier rate; if every '
                                     'carrier wants more, re-check the numbers or go back to the shipper '
                                     '[FreightBrokers — HTQaqqy_CPs @ 00:04:26].',
                                     "Search every caller's MC or DOT number for FMCSA authority, "
                                     'out-of-service status, safety rating and insurance, and pass on '
                                     'carriers with thin data [AscendTMS - The Free (and Best) TMS '
                                     'Software — ICIyOtMiEqY @ 00:15:42].',
                                     'Never redirect payments after a notice of assignment, and know the '
                                     'scope of any UCC filing and how it gets released before signing '
                                     '[BLACK BEAR FREIGHT & LOGISTICS — ZYkg1UepLL4 @ 00:05:26].',
                                     'Fund the payables gap before adding loads: ten carriers at $1,800 is '
                                     '$18,000 out before a shipper pays [FreightBrokers — Lpq9AHrz7nQ @ '
                                     '00:03:21].']}}],
 'pull_quote': '"But remember, fast money is not free money." — BLACK BEAR FREIGHT & LOGISTICS '
               '(ZYkg1UepLL4 @ 00:07:11).',
 'diagram_id': 'diag-01',
 'action_checklist': ['Collect pickup and delivery details, appointment times, commodity, weight, '
                      'equipment, driver assist, extra stops and special instructions before pricing; a '
                      'firm 6:00 a.m. delivery differs from anytime Friday [FreightBrokers — HTQaqqy_CPs @ '
                      '00:00:56].',
                      'Pull DAT RateView at Market granularity, weigh 30-day and 7-day data over '
                      'forecasts, and price in 150 miles of deadhead as a make-or-break-even floor until '
                      'you learn the lane [ShipLeague — rMpa5pbBWtI @ 00:04:55].',
                      'Deliver the customer rate flatly with no apology, state what is included, hold it '
                      'through end of day, and confirm in writing before booking the carrier '
                      '[FreightBrokers — HTQaqqy_CPs @ 00:05:22].',
                      'Build the load with Google-powered location lookup and optimized stop order, '
                      'because badly ordered stops mean you are not going to make money [AscendTMS - The '
                      'Free (and Best) TMS Software — Eycc6Jod6t4 @ 00:14:31].',
                      'Invoice the same day the POD is uploaded and sync the invoice straight to '
                      'accounting [FreightWaves — MobEZyaIjV4 @ 00:04:37].',
                      'Run the KPI summary for revenue, expenses, profit, per-mile figures and gross '
                      'margin percentage, and export the AR/AP report as a collection sheet [AscendTMS - '
                      'The Free (and Best) TMS Software — ICIyOtMiEqY @ 00:21:04].'],
 'statutory_citations': [{'title': 'FreightBrokers — How to Price Your First Load As A Freight Broker or '
                                   'Freight Agent [4 Key Numbers Explained] [00:04:26]',
                          'url': 'https://www.youtube.com/watch?v=HTQaqqy_CPs&t=266s',
                          'relevance': 'Primary practitioner testimony on deriving the maximum carrier '
                                       'rate and protecting the minimum profit floor.'},
                         {'title': 'FreightBrokers — How Do Freight Brokers Get Paid? From Invoicing to '
                                   'Profit. 💰🔥 [00:03:47]',
                          'url': 'https://www.youtube.com/watch?v=Lpq9AHrz7nQ&t=227s',
                          'relevance': 'Primary practitioner testimony on the gap between invoiced and '
                                       'paid, carrier payables and net profit after expenses.'},
                         {'title': 'ShipLeague — How Freight Brokers Quote Shippers - Explained [00:04:10]',
                          'url': 'https://www.youtube.com/watch?v=rMpa5pbBWtI&t=250s',
                          'relevance': 'Primary practitioner testimony on DAT RateView lane research, 15 '
                                       'percent margin and deadhead break-even pricing.'},
                         {'title': 'BLACK BEAR FREIGHT & LOGISTICS — How Freight Factoring Helps Carriers '
                                   'Improve Cash Flow [00:03:36]',
                          'url': 'https://www.youtube.com/watch?v=ZYkg1UepLL4&t=216s',
                          'relevance': 'Primary practitioner testimony on factoring hidden fees, recourse '
                                       'exposure, notice of assignment and exit terms.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'oytUZVvyF80',
                       'title': 'Freight Broker Reveals How Truckers Can Make More Money in 2026',
                       'channel': 'Entre Mike',
                       'author': 'Entre Mike',
                       'text': 'You and 90% of the other people in this industry can do that exact same '
                               'thing.',
                       'tip': 'You and 90% of the other people in this industry can do that exact same '
                              'thing.',
                       'timestamp': 1743,
                       'timestamp_seconds': 1743,
                       'timestamp_label': '[00:29:03]',
                       'url': 'https://www.youtube.com/watch?v=oytUZVvyF80&t=1743s',
                       'markdown': '[00:29:03](https://www.youtube.com/watch?v=oytUZVvyF80&t=1743s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'oytUZVvyF80',
                       'title': 'Freight Broker Reveals How Truckers Can Make More Money in 2026',
                       'channel': 'Entre Mike',
                       'author': 'Entre Mike',
                       'text': 'And so only 10% have ever even been asked once in their entire career.',
                       'tip': 'And so only 10% have ever even been asked once in their entire career.',
                       'timestamp': 1218,
                       'timestamp_seconds': 1218,
                       'timestamp_label': '[00:20:18]',
                       'url': 'https://www.youtube.com/watch?v=oytUZVvyF80&t=1218s',
                       'markdown': '[00:20:18](https://www.youtube.com/watch?v=oytUZVvyF80&t=1218s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Lpq9AHrz7nQ',
                       'title': 'How Do Freight Brokers Get Paid? From Invoicing to Profit. 💰🔥',
                       'channel': 'FreightBrokers',
                       'author': 'FreightBrokers',
                       'text': "You can have a load that's profitable on paper and still have a cash flow "
                               'problem.',
                       'tip': "You can have a load that's profitable on paper and still have a cash flow "
                              'problem.',
                       'timestamp': 227,
                       'timestamp_seconds': 227,
                       'timestamp_label': '[00:03:47]',
                       'url': 'https://www.youtube.com/watch?v=Lpq9AHrz7nQ&t=227s',
                       'markdown': '[00:03:47](https://www.youtube.com/watch?v=Lpq9AHrz7nQ&t=227s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'rMpa5pbBWtI',
                       'title': 'How Freight Brokers Quote Shippers - Explained',
                       'channel': 'ShipLeague',
                       'author': 'ShipLeague',
                       'text': 'Expect about $1,700 to the truck and quote about $1,850, because a 15% '
                               'margin is pretty standard.',
                       'tip': 'Expect about $1,700 to the truck and quote about $1,850, because a 15% '
                              'margin is pretty standard.',
                       'timestamp': 250,
                       'timestamp_seconds': 250,
                       'timestamp_label': '[00:04:10]',
                       'url': 'https://www.youtube.com/watch?v=rMpa5pbBWtI&t=250s',
                       'markdown': '[00:04:10](https://www.youtube.com/watch?v=rMpa5pbBWtI&t=250s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'edDHTJiH5HM',
                       'title': 'Freight Pricing AI - Earn While You Learn & Build Your Freight Brokerage '
                                'Business',
                       'channel': 'Freight Broker 911',
                       'author': 'Freight Broker 911',
                       'text': 'The first 30 days are $0, and it stays $0 with an active shipper and at '
                               'least one shipment every 30 days, otherwise it is $149 a month.',
                       'tip': 'The first 30 days are $0, and it stays $0 with an active shipper and at '
                              'least one shipment every 30 days, otherwise it is $149 a month.',
                       'timestamp': 34,
                       'timestamp_seconds': 34,
                       'timestamp_label': '[00:00:34]',
                       'url': 'https://www.youtube.com/watch?v=edDHTJiH5HM&t=34s',
                       'markdown': '[00:00:34](https://www.youtube.com/watch?v=edDHTJiH5HM&t=34s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'wOpAqd5AALo',
                       'title': 'Mastering Trucking Lane Rates | DAT Load Board Tutorial for Maximum '
                                'Profit',
                       'channel': "Tony's Topics",
                       'author': "Tony's Topics",
                       'text': 'This is a great tool to use and again, you will need a DAT One Pro '
                               'account, $135 a month.',
                       'tip': 'This is a great tool to use and again, you will need a DAT One Pro account, '
                              '$135 a month.',
                       'timestamp': 178,
                       'timestamp_seconds': 178,
                       'timestamp_label': '[00:02:58]',
                       'url': 'https://www.youtube.com/watch?v=wOpAqd5AALo&t=178s',
                       'markdown': '[00:02:58](https://www.youtube.com/watch?v=wOpAqd5AALo&t=178s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'iJE2rZFL57E',
                       'title': 'Quick Pay vs Freight Factoring',
                       'channel': 'Porter Capital',
                       'author': 'Porter Capital',
                       'text': "In exchange, they charge a fee between 1 and 5% of the load's value.",
                       'tip': "In exchange, they charge a fee between 1 and 5% of the load's value.",
                       'timestamp': 13,
                       'timestamp_seconds': 13,
                       'timestamp_label': '[00:00:13]',
                       'url': 'https://www.youtube.com/watch?v=iJE2rZFL57E&t=13s',
                       'markdown': '[00:00:13](https://www.youtube.com/watch?v=iJE2rZFL57E&t=13s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'K9UPJJr_uzQ',
                       'title': 'Trucking: What’s the Difference Between QuickPay & Factoring',
                       'channel': 'Trucking From Scratch',
                       'author': 'Trucking From Scratch',
                       'text': 'Factoring is the preference because the standardized process can be '
                               "delegated to an admin hire, and some brokers don't offer quick pay at all.",
                       'tip': 'Factoring is the preference because the standardized process can be '
                              "delegated to an admin hire, and some brokers don't offer quick pay at all.",
                       'timestamp': 163,
                       'timestamp_seconds': 163,
                       'timestamp_label': '[00:02:43]',
                       'url': 'https://www.youtube.com/watch?v=K9UPJJr_uzQ&t=163s',
                       'markdown': '[00:02:43](https://www.youtube.com/watch?v=K9UPJJr_uzQ&t=163s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'dTOcCujNdaw',
                       'title': 'Freight Invoice Factoring vs Quickpay with Brokers',
                       'channel': 'Bumble Bee Dispatch',
                       'author': 'Bumble Bee Dispatch',
                       'text': 'Quick pay can cost 5% plus a $25 to $29 Comchek fee.',
                       'tip': 'Quick pay can cost 5% plus a $25 to $29 Comchek fee.',
                       'timestamp': 260,
                       'timestamp_seconds': 260,
                       'timestamp_label': '[00:04:20]',
                       'url': 'https://www.youtube.com/watch?v=dTOcCujNdaw&t=260s',
                       'markdown': '[00:04:20](https://www.youtube.com/watch?v=dTOcCujNdaw&t=260s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'R4i90VgyHqk',
                       'title': 'How Working With A Truck Factoring Company Gets You Paid Fast!',
                       'channel': 'Porter Capital',
                       'author': 'Porter Capital',
                       'text': "Truck factoring doesn't hurt your credit.",
                       'tip': "Truck factoring doesn't hurt your credit.",
                       'timestamp': 60,
                       'timestamp_seconds': 60,
                       'timestamp_label': '[00:01:00]',
                       'url': 'https://www.youtube.com/watch?v=R4i90VgyHqk&t=60s',
                       'markdown': '[00:01:00](https://www.youtube.com/watch?v=R4i90VgyHqk&t=60s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'i6KVZJUOBqs',
                       'title': 'TRUCKING BUSINESS: HOW TO GET PAID? FACTORING SERVICE, COD, QUICK PAY & '
                                'INVOICING THE BROKER!!!',
                       'channel': 'Brandon Manney The Mentor',
                       'author': 'Brandon Manney The Mentor',
                       'text': 'Broker quick pay is about 2 to 3% within about 7 days, while factoring is '
                               '3 to 5% within 24 hours.',
                       'tip': 'Broker quick pay is about 2 to 3% within about 7 days, while factoring is 3 '
                              'to 5% within 24 hours.',
                       'timestamp': 141,
                       'timestamp_seconds': 141,
                       'timestamp_label': '[00:02:21]',
                       'url': 'https://www.youtube.com/watch?v=i6KVZJUOBqs&t=141s',
                       'markdown': '[00:02:21](https://www.youtube.com/watch?v=i6KVZJUOBqs&t=141s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'MobEZyaIjV4',
                       'title': 'Rose Rocket - Transportation Management Software (TMS) - Demo',
                       'channel': 'FreightWaves',
                       'author': 'FreightWaves',
                       'text': 'Invoicing can go out the same day the POD is uploaded, synced to '
                               'accounting.',
                       'tip': 'Invoicing can go out the same day the POD is uploaded, synced to '
                              'accounting.',
                       'timestamp': 277,
                       'timestamp_seconds': 277,
                       'timestamp_label': '[00:04:37]',
                       'url': 'https://www.youtube.com/watch?v=MobEZyaIjV4&t=277s',
                       'markdown': '[00:04:37](https://www.youtube.com/watch?v=MobEZyaIjV4&t=277s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ICIyOtMiEqY',
                       'title': "A Full Tour of AscendTMS for 3PL's, Logistics Brokers and Shippers",
                       'channel': 'AscendTMS - The Free (and Best) TMS Software',
                       'author': 'AscendTMS - The Free (and Best) TMS Software',
                       'text': "Now before everybody gets too excited, this doesn't mean that you get DAT "
                               'and Truckstop for free; you still have to have accounts with these load '
                               'boards for this to be able to work.',
                       'tip': "Now before everybody gets too excited, this doesn't mean that you get DAT "
                              'and Truckstop for free; you still have to have accounts with these load '
                              'boards for this to be able to work.',
                       'timestamp': 419,
                       'timestamp_seconds': 419,
                       'timestamp_label': '[00:06:59]',
                       'url': 'https://www.youtube.com/watch?v=ICIyOtMiEqY&t=419s',
                       'markdown': '[00:06:59](https://www.youtube.com/watch?v=ICIyOtMiEqY&t=419s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'idL8PXMlKjQ',
                       'title': 'FULL AscendTMS Operations Training!',
                       'channel': 'AscendTMS - The Free (and Best) TMS Software',
                       'author': 'AscendTMS - The Free (and Best) TMS Software',
                       'text': 'So four percent of 1800 is 72; I will hold back 72 dollars from Melton '
                               "Truckline's pay.",
                       'tip': 'So four percent of 1800 is 72; I will hold back 72 dollars from Melton '
                              "Truckline's pay.",
                       'timestamp': 2931,
                       'timestamp_seconds': 2931,
                       'timestamp_label': '[00:48:51]',
                       'url': 'https://www.youtube.com/watch?v=idL8PXMlKjQ&t=2931s',
                       'markdown': '[00:48:51](https://www.youtube.com/watch?v=idL8PXMlKjQ&t=2931s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Eycc6Jod6t4',
                       'title': 'FULL AscendTMS Operations Training! (2024)',
                       'channel': 'AscendTMS - The Free (and Best) TMS Software',
                       'author': 'AscendTMS - The Free (and Best) TMS Software',
                       'text': 'You can copy loads up to 20 times, you can cancel loads.',
                       'tip': 'You can copy loads up to 20 times, you can cancel loads.',
                       'timestamp': 1372,
                       'timestamp_seconds': 1372,
                       'timestamp_label': '[00:22:52]',
                       'url': 'https://www.youtube.com/watch?v=Eycc6Jod6t4&t=1372s',
                       'markdown': '[00:22:52](https://www.youtube.com/watch?v=Eycc6Jod6t4&t=1372s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'HTQaqqy_CPs',
                       'title': 'How to Price Your First Load As A Freight Broker or Freight Agent [4 Key '
                                'Numbers Explained]',
                       'channel': 'FreightBrokers',
                       'author': 'FreightBrokers',
                       'text': 'Knowing your maximum rate helps you negotiate with confidence.',
                       'tip': 'Knowing your maximum rate helps you negotiate with confidence.',
                       'timestamp': 322,
                       'timestamp_seconds': 322,
                       'timestamp_label': '[00:05:22]',
                       'url': 'https://www.youtube.com/watch?v=HTQaqqy_CPs&t=322s',
                       'markdown': '[00:05:22](https://www.youtube.com/watch?v=HTQaqqy_CPs&t=322s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ZYkg1UepLL4',
                       'title': 'How Freight Factoring Helps Carriers Improve Cash Flow',
                       'channel': 'BLACK BEAR FREIGHT & LOGISTICS',
                       'author': 'BLACK BEAR FREIGHT & LOGISTICS',
                       'text': 'So non-recourse does not necessarily mean you can never be charged back.',
                       'tip': 'So non-recourse does not necessarily mean you can never be charged back.',
                       'timestamp': 197,
                       'timestamp_seconds': 197,
                       'timestamp_label': '[00:03:17]',
                       'url': 'https://www.youtube.com/watch?v=ZYkg1UepLL4&t=197s',
                       'markdown': '[00:03:17](https://www.youtube.com/watch?v=ZYkg1UepLL4&t=197s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'}]}
