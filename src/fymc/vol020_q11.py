from __future__ import annotations

CHAPTER_11 = {'id': 'Q11',
 'chapter_id': 'Q11',
 'chapter_number': 11,
 'question_number': 11,
 'slug': 'brokering-dla-parts-through-dibbs',
 'question_prompt': 'How do I find, source, quote and batch-bid DLA parts solicitations on DIBBS?',
 'kicker': 'Q11 / THE BIG MONEY PLAYBOOKS',
 'title': 'Brokering DLA Parts Through DIBBS',
 'subtitle': 'Finding RFQs by FSC, NSN and due date, extracting key RFQ data, finding the right supplier, '
             'urgent-need and no-bid lists, AMSC manufacturing RFQs, live solicitation review and bidding, '
             'batch quote files and the DLA BUS, and Intertek/SAI tools',
 'layout_template': 'chapter_opener',
 'reading_time_minutes': 15,
 'executive_summary': 'DLA brokers on DIBBS agree the game is volume inside a narrow lane: register on SAM '
                      'and DIBBS, pick three to five FSCs, screen each RFQ for approved-source '
                      'restrictions, and quote every day, because roughly 99% of awards go to the cheapest '
                      'bid and bid count tracks award count. Street mechanics are precise: read '
                      'solicitations only to page 10, anchor price to procurement history, target 10 to '
                      '15% margin, take Net 30 since the government pays in 23 to 25 days, and call '
                      "suppliers instead of emailing. Tooling splits the field, from FedOpp's "
                      "browser-built batch files to DVN's DLA BUS catalog uploads and Gov Scraper at $100 "
                      'a month. Practitioners clash over chasing RFQs older than 60 days, whether batch '
                      'bidding needs thousands of NSNs, and how fast a bidding catalog can realistically '
                      'be built.',
 'key_metrics': [{'label': 'Daily DLA solicitation volume',
                  'metric': 'Daily DLA solicitation volume',
                  'value': '2,000-3,000 solicitations per day',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Ki Hendris of National Material Supply reports DLA posts 2,000 to 3,000 '
                             'solicitations a day and often cancels and reissues them.',
                  'source': 'The DLA Vendor Network (DVN) ([jjX9klCZFKI @ 00:32:59])'},
                 {'label': 'Target bid margin',
                  'metric': 'Target bid margin',
                  'value': '10-15%',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Tristan Thomas calls 10 to 15% the real sweet spot and says asking 20 to 30% '
                             'gets a bidder underbid.',
                  'source': 'Secureframe ([v7nJCLRc0uo @ 00:38:03])'},
                 {'label': 'Average government payment time',
                  'metric': 'Average government payment time',
                  'value': '23-25 days',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Tris10 picks Net 30 over a 10-day term that costs a 2% haircut, because the '
                             'government pays within 23 to 25 days on average.',
                  'source': 'Tris10 @ MeND ([v4ulUMKE5xA @ 00:05:57])'},
                 {'label': 'Active DIBBS vendor count',
                  'metric': 'Active DIBBS vendor count',
                  'value': 'About 8,500 vendors, down from about 15,000 pre-pandemic',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'DVN reports the active DIBBS vendor pool shrank to about 8,500 from roughly '
                             '15,000 before the pandemic.',
                  'source': 'The DLA Vendor Network (DVN) ([MyfmHjDF9HI @ 00:33:25])'}],
 'sections': [{'section_number': 1,
               'heading': 'The Practitioner Consensus',
               'paragraphs': ['Every practitioner opens at the same front door: register on SAM to pull a '
                              'UEI and CAGE code, then complete a separate DIBBS registration before a '
                              'single quote goes in [wxZNfwOuung @ 00:02:38]. The prize behind that '
                              'paperwork is enormous and tilted toward small shops. Ki Hendris of National '
                              "Material Supply puts last year's DLA spend at $51.4 billion, with about 80% "
                              'of awards going to small businesses [jjX9klCZFKI @ 00:10:46]. Tristan '
                              'Thomas of Mend Sourcing and Gov Scraper counts $52.6 billion in 2024 '
                              'obligations and $47 billion in revenue, with over 40% flowing to small '
                              'business against a 5% SDVOSB goal [v7nJCLRc0uo @ 00:12:06]. DVN frames the '
                              'daily firehose: about 10,000 awards a day, more than 100,000 open '
                              'solicitations, 5 to 8 million NSNs, and roughly $50 billion a year '
                              '[MyfmHjDF9HI @ 00:12:48]. The percentages differ by speaker, but the '
                              'direction is identical: this is a small-business market moving thousands of '
                              'buys every day, and the operators who win are the ones who treat it as a '
                              'daily volume game rather than a lottery ticket. None of these operators '
                              'sells it as fast money; the work is registration, a narrow lane, and '
                              'relentless quoting.',
                              'The second agreement is the lane, and the lane is the Federal Supply Class. '
                              'Thomas says about 95% of searches run by the four-digit FSC, and filtering '
                              '5306, 5305 and 5310 to small business and SDVOSB set-asides returned 876 '
                              'RFQs in a single pull [v7nJCLRc0uo @ 00:18:41]. myContractScout tells '
                              'newcomers to start with three to five FSCs, aim for a first $100,000, and '
                              "stay disciplined about scope: don't go try to sell tires on day one "
                              '[SeWe_WAhyVg @ 00:08:07]. The third agreement is that approved-source '
                              'restrictions decide whether a broker can even play the buy. Tris10 tells '
                              'beginners to look for items whose PID is blank with no approved sources, '
                              'which any supplier can fill, and to pair those with local manufacturers '
                              '[JE_OOJ3NAVk @ 00:09:49]. FedOpp warns flatly that the codes limiting a buy '
                              'to approved sources can knock you out, and puts an AMSC filter directly on '
                              'its bid-board search for exactly that reason [bTlxn6BVHJ0 @ 00:02:02]. The '
                              'operator logic stacks cleanly: keep a short FSC list, screen every RFQ for '
                              'who is allowed to supply the part, and spend sourcing hours only where the '
                              'door is open or where a distributor can reach the named manufacturer.',
                              'The final consensus is that awards follow volume, price, and voice. Tris10 '
                              'states there is a direct correlation between the amount of bids you put '
                              'into the system and the amount of awards you win, and pushes operators to '
                              'keep quoting even when they suspect they are priced out [v4ulUMKE5xA @ '
                              '00:15:55]. Humam Finding Sam estimates about 99% of awards go to the '
                              'cheapest bid, which makes the cheapest landed cost the entire contest '
                              "[wxZNfwOuung @ 00:06:24]. Thomas ranks DLA's priorities in order: price "
                              'first, then delivery time, then credibility through the SPRS score '
                              '[v7nJCLRc0uo @ 00:30:17]. On the supplier side the agreement is just as '
                              'firm. Tris10 says phone beats email and in person beats phone, because it '
                              'is much harder for someone to say no to you over the phone than it is via '
                              'email [JE_OOJ3NAVk @ 00:11:07]. That makes the daily rhythm obvious for a '
                              'broker: a short FSC list, aggressive price-first quoting every day, '
                              'delivery treated as a secondary lever, and suppliers worked by voice '
                              'instead of by inbox. Price is the contest, and volume is how an operator '
                              'gets enough at-bats to win it.'],
               'table': {'caption': 'Baseline consensus every DIBBS broker operates on',
                         'headers': ['Consensus Point',
                                     'What Operators Actually Do',
                                     'Practitioner Number or Warning',
                                     'Expert Source'],
                         'rows': [['Register on SAM and DIBBS before quoting anything',
                                   'Pull UEI and CAGE through SAM, then complete the separate DIBBS '
                                   'registration',
                                   'DIBBS registration is free and DLA verifies your business address by '
                                   'postcard',
                                   'Secureframe ([v7nJCLRc0uo @ 00:16:04])'],
                                  ['DLA spending is heavily tilted toward small businesses',
                                   "Position the shop as a small business competing for a giant buyer's "
                                   'daily needs',
                                   '$51.4 billion spent last year with about 80% of awards to small '
                                   'businesses',
                                   'The DLA Vendor Network (DVN) ([jjX9klCZFKI @ 00:10:46])'],
                                  ['Stay inside a narrow Federal Supply Class lane',
                                   'Start with three to five FSCs and search only those classes every day',
                                   "Aim for a first $100,000 before expanding; don't go try to sell tires",
                                   'myContractScout ([SeWe_WAhyVg @ 00:08:07])'],
                                  ['Screen approved-source restrictions before spending any sourcing time',
                                   'Beginners hunt blank-PID items with no approved sources and work with '
                                   'local manufacturers',
                                   'A blank PID means any supplier can fill the requirement on that RFQ',
                                   'Tris10 @ MeND ([JE_OOJ3NAVk @ 00:09:49])'],
                                  ['Isolate manufacturing RFQs that list zero approved sources',
                                   'Add a filter where Approved Sources is null and hit apply on the view',
                                   'Leaves only RFQs open to small manufacturers instead of named '
                                   'approved-source buys',
                                   'Loocey DLA & GovCon ([LzmJyrGyMBw @ 00:00:34])'],
                                  ['The cheapest bid takes almost every single award',
                                   'Build a cost expectation from past award prices before requesting any '
                                   'vendor quote',
                                   'About 99% of awards go to the cheapest bid on the solicitation',
                                   'Humam Finding Sam ([wxZNfwOuung @ 00:06:24])'],
                                  ['Bid volume directly drives the number of awards won',
                                   'Submit quotes daily, including ones where you suspect you are already '
                                   'priced out',
                                   'Direct correlation between bids put into the system and awards you win',
                                   'Tris10 @ MeND ([v4ulUMKE5xA @ 00:15:55])']]}},
              {'section_number': 2,
               'heading': 'Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['Execution starts with the pull. On raw DIBBS, myContractScout runs FSC '
                              '6510, gets 452 records, and copies the whole list into Google Sheets to '
                              "work it outside the portal [SeWe_WAhyVg @ 00:06:21]. FedOpp's morning "
                              'routine is tighter: filter Parts to Quote down to open RFQs only, then sort '
                              'by last award unit price before building any quote [bTs2wy13K1c @ '
                              '00:03:21]. Reading the solicitation is where most hours disappear, and '
                              'Thomas cuts it hard. They read only through page 10 of a 24-page RFQ, up to '
                              'the asterisks, and extract the solicitation number, PR number, procurement '
                              'history, NSN, CMMC level, approved sources, CLIN quantity, delivery days, '
                              'FOB terms, and ASTM packaging; their worked example carried 831 units at '
                              '108 delivery days with FOB origin, meaning the government pays shipping '
                              '[v7nJCLRc0uo @ 00:23:27]. Tris10 treats procurement history as the price '
                              'compass. One shear bolt history showed 1,966 pieces at $556 in 2022 and 46 '
                              'pieces at $49.90 in 2021, which gives a broker the price band before '
                              'calling a single supplier [Z9MLGFqFXtM @ 00:02:17]. The extraction sheet '
                              'becomes the template for every vendor request, so the same dozen fields get '
                              'captured the same way on every RFQ.',
                              'Pricing is built backward from the last award, not forward from a supplier '
                              'list. Humam Finding Sam pulls past awards of $33 on February 25, 2026, $35 '
                              'on January 28, and $27 on August 4, 2025, so they enter the vendor request '
                              "already knowing what the item should cost [wxZNfwOuung @ 00:06:38]. DVN's "
                              'live wiper-blade bid shows the markup math in plain dollars: a 10% markup '
                              'came to about $2 per unit and $642 of total profit, with ASTM D3951 '
                              'packaging and MIL-STD-129 labels priced in [MyfmHjDF9HI @ 00:31:22]. Thomas '
                              'puts the sweet spot at 10 to 15% margin, warns that asking 20 to 30% gets '
                              'you underbid, and walks a worked build: 250 units at $185 for $46,250, plus '
                              'a $350 packaging minimum, plus a 250 DCMA inspection line, plus $7,035 of '
                              'margin, all divided by 250 for the unit bid [v7nJCLRc0uo @ 00:38:03]. Terms '
                              'move cash too. Tris10 picks Net 30 over a 10-day term because the shorter '
                              'term is a 2% haircut that turns $100,000 into $98,000, and the government '
                              'pays within 23 to 25 days on average anyway [v4ulUMKE5xA @ 00:05:57]. The '
                              'pattern across all four is identical: anchor on history, stack every landed '
                              'cost, add a thin margin, and protect it through payment terms.',
                              "The bid form is where volume is won or lost. Tris10's rule on the DIBBS web "
                              'quote is to keep filling until no section is still yellow [v4ulUMKE5xA @ '
                              '00:02:32]. Hendris lays out the three quoting methods: the web form at '
                              'about two pages and time-consuming, EDI through a value-added network that '
                              'is antiquated, expensive, and not recommended for small businesses, and '
                              'batch quoting as a one-click upload locked to active vendors [jjX9klCZFKI @ '
                              '00:11:21]. Batch is where the serious distributors live, and the tooling '
                              "filters dead lines before they waste an upload. DVN's DLA BUS demo pushed "
                              '20 solicitations through and returned 11 green passes and 9 red failures '
                              'that were already awarded, cancelled, or closed [YlwuuaCoHzQ @ 00:12:25]. '
                              "FedOpp's batch builder runs a Check Line pass that flags every error in red "
                              'with a running count of items left to fix, covering item description code, '
                              'quality, trade and Buy American answers, packaging, and manufacturer or '
                              'dealer fields [iTxJkLPYuqc @ 00:02:56]. The street logic is simple: a web '
                              'form handles a few quotes a day, but an operator chasing real volume moves '
                              "the prep into spreadsheets or a catalog, validates every line against DLA's "
                              'format, and uploads the whole stack at once instead of retyping CAGE codes '
                              'and prices one solicitation at a time.'],
               'table': {'caption': 'Street-level DIBBS mechanics, tools and unit economics',
                         'headers': ['Mechanic or Tool',
                                     'Exact Setting or Number',
                                     'How Operators Use It',
                                     'Expert Source'],
                         'rows': [['Raw DIBBS search button on the RFQ tab',
                                   'Set category to Federal Supply Class, then click Search because Enter '
                                   'does nothing',
                                   'Avoids dead searches on a portal that ignores keyboard submission '
                                   'entirely',
                                   'myContractScout ([SeWe_WAhyVg @ 00:05:23])'],
                                  ['FedOpp No Bid list of failed solicitations',
                                   'Solicitations that got no acceptable quote while DLA still needs the '
                                   'parts',
                                   'Check DIBBS for a newly opened solicitation before quoting the part '
                                   'again',
                                   'FedOpp ([qmdunkO7mts @ 00:02:01])'],
                                  ['FedOpp Urgent Need list for in-stock inventory',
                                   'Email DLA button opens the available-material inbox; Export CSV '
                                   'downloads the list',
                                   'Check the exported list against your own inventory to quote parts '
                                   'already held',
                                   'FedOpp ([qmdunkO7mts @ 00:01:38])'],
                                  ['Payment terms field on the DIBBS quote',
                                   'Net 30 instead of a 10-day term that costs a 2% haircut',
                                   'Government pays within 23 to 25 days on average, so the discount is '
                                   'wasted',
                                   'Tris10 @ MeND ([v4ulUMKE5xA @ 00:05:57])'],
                                  ['Military packaging standards and packaging partner quotes',
                                   'ASTM D3951, MIL-STD-2073 and MIL-STD-129 decoded by govpacking.com',
                                   'Packaging quotes come back within 24 hours, typically in about two '
                                   'hours',
                                   'Secureframe ([v7nJCLRc0uo @ 00:40:51])'],
                                  ['Gov Scraper RFQ review and tracking software',
                                   '$100 per month, 100+ users, one user won 52 awards in 6 months',
                                   'Cuts RFQ review time from 8 to 10 minutes down to 30 seconds',
                                   'Secureframe ([v7nJCLRc0uo @ 00:50:16])'],
                                  ['DLA BUS batch bidding software from DVN',
                                   '14-day free trial; requires at least 1 award and at least 50 bids',
                                   'Not built for entry-level vendors; beta opened 50 seats with 40 still '
                                   'open',
                                   'The DLA Vendor Network (DVN) ([jjX9klCZFKI @ 00:45:04])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Edges the Volume Bidders Actually Use',
                           'body': 'Four moves the practitioners use to quote faster, source cleaner, and '
                                   'stay in the running on more buys.',
                           'items': ['Map every NSN to the manufacturer part number before you call, '
                                     'because suppliers often have no idea what an NSN is; Tris10 uses the '
                                     'nsn-now public search to do it [Tris10 @ MeND — JE_OOJ3NAVk @ '
                                     '00:04:05].',
                                     'Quote your real lead time instead of the requested one: Thomas won '
                                     'with 300 days against 25 requested, because DLA ranks price ahead of '
                                     'delivery [Secureframe — v7nJCLRc0uo @ 00:30:17].',
                                     'Build a manufacturing view by adding a filter where Approved Sources '
                                     'is null and hitting apply, so only RFQs open to small manufacturers '
                                     'remain [Loocey DLA & GovCon — LzmJyrGyMBw @ 00:00:34].',
                                     'You do not need thousands of NSNs to batch bid: every NSN you bid, '
                                     'won or lost, joins your catalog, per Hendris [The DLA Vendor Network '
                                     '(DVN) — jjX9klCZFKI @ 00:20:13].']},
               'sop_steps': [{'step': 1,
                              'title': 'Lock the FSC lane on the bid board',
                              'action': 'Filter open DLA RFQs to your handful of FSCs, then layer the '
                                        'set-aside filter.',
                              'detail': 'FedOpp calls the FSC filter the fastest one because most shops '
                                        'quote a handful of classes, and pairs it with set-aside filters '
                                        'for small business, HUBZone and SDVOSB [FedOpp — bTlxn6BVHJ0 @ '
                                        '00:01:38].'},
                             {'step': 2,
                              'title': 'Extract the approved manufacturer and part number',
                              'action': 'Pull the named approved manufacturer and its part number from the '
                                        'RFQ before sourcing.',
                              'detail': 'Tris10 pulls the single approved manufacturer, SPS Technologies, '
                                        'and its part number, noting they can only go to SPS Technologies '
                                        'or find a company that can supply the part from SPS Technologies '
                                        '[Tris10 @ MeND — Z9MLGFqFXtM @ 00:03:37].'},
                             {'step': 3,
                              'title': 'Send an all-inclusive vendor request',
                              'action': 'Email the supplier the NSN, part number, drawings and delivery '
                                        'date, then follow up by phone.',
                              'detail': 'Humam Finding Sam requests all-inclusive pricing including '
                                        'surcharges [Humam Finding Sam — wxZNfwOuung @ 00:08:06], and '
                                        "Tris10's template also asks for lead time, stock, certs, country "
                                        'of origin, cert fees and traceability [Tris10 @ MeND — '
                                        'JE_OOJ3NAVk @ 00:14:37].'},
                             {'step': 4,
                              'title': 'Fill the dealer fields and submit, then revise',
                              'action': "Enter the manufacturer's CAGE in the dealer field, submit, and "
                                        'circle back to revise while the RFQ is open.',
                              'detail': "Tris10 enters the manufacturer's CAGE in the dealer field [Tris10 "
                                        '@ MeND — v4ulUMKE5xA @ 00:11:39], and DVN says to bid and bid '
                                        'often because you can always circle back and revise after '
                                        'submitting [The DLA Vendor Network (DVN) — MyfmHjDF9HI @ '
                                        '00:35:56].'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The sharpest split is over how old an RFQ can be before it becomes dead '
                              'money. Tris10 @ MeND treats the return date loosely, using a no-bid as a '
                              'placeholder and often bidding after expiration because DIBBS is more '
                              'lenient than SAM, yet draws a hard line against touching anything older '
                              'than 60 days and works the newest RFQs because a contracting officer just '
                              'put them into the system [v4ulUMKE5xA @ 00:05:07]. Tristan Thomas of Mend '
                              'Sourcing and Gov Scraper, speaking on Secureframe, lands in the same camp '
                              'and calls the popular go-back-60-to-90-days advice false, arguing that '
                              'stale RFQs are leftovers from DLA staff reassignment rather than proof that '
                              'nobody bid, and sorts every search by newest issued [v7nJCLRc0uo @ '
                              '00:20:44]. The DLA Vendor Network runs a looser play in its live '
                              'walkthrough: a wiper-blade solicitation whose September 28 deadline had '
                              'passed was still open on October 4, and they quoted it anyway [MyfmHjDF9HI '
                              '@ 00:25:44]. Their logic is bid and bid often, because a submitted bid can '
                              'always be revised later [MyfmHjDF9HI @ 00:35:56]. The usable synthesis is '
                              'that a passed return date alone does not kill a buy, but the age of the RFQ '
                              'separates live demand from abandoned records.',
                              'Delivery promises and margin targets split the camp just as hard. On the '
                              'wiper blades, The DLA Vendor Network faced a 284-day required delivery and '
                              'bid 90 days, landing at $23.31 per unit after a 10% markup worth about $2 '
                              'per unit and $642 in total profit [MyfmHjDF9HI @ 00:35:09]. Tristan Thomas '
                              'argues the reverse on delivery: quote your real lead time, because they won '
                              'with 300 days against 25 requested, and DLA ranks price first, then '
                              'delivery, then credibility through the SPRS score [v7nJCLRc0uo @ 00:30:17]. '
                              'Tris10 @ MeND backs the price-first ranking from a different angle, pricing '
                              '103 pieces at 120 delivery days and stating that the government does not '
                              'have delivery days as the number one priority [v4ulUMKE5xA @ 00:09:28]. On '
                              'margin, Tristan Thomas puts the sweet spot at 10 to 15%, warns that asking '
                              '20 to 30% gets you underbid, and reports that judging the profit dollar '
                              'amount instead of the percentage brought more awards [v7nJCLRc0uo @ '
                              '00:38:03]. The DVN markup sits at the bottom of that band, so the live '
                              'argument is whether to anchor on percentage or on dollars per award, and '
                              'whether a short delivery promise is worth the risk of missing it.',
                              'Tooling and catalog strategy form the third fault line. Ki Hendris of '
                              'National Material Supply, presenting for The DLA Vendor Network, flatly '
                              'rejects the idea that you need thousands of NSNs to batch bid, because '
                              'every NSN you bid, won or lost, joins your catalog [jjX9klCZFKI @ '
                              '00:20:13]. FedOpp takes the opposite design stance from the DVN catalog '
                              'generator: the batch TXT is built line by line in the browser, checked '
                              "against DLA's format rules, and uploaded by the user, and FedOpp never "
                              'submits bids [iTxJkLPYuqc @ 00:00:04]. Even what to read before quoting is '
                              'contested. Tris10 @ MeND tells bidders that flow-downs can be ignored until '
                              'an award lands, arguing you do not need all the information at the '
                              'beginning just to submit a bid [Z9MLGFqFXtM @ 00:05:42]. Tristan Thomas '
                              'lists missing flowdowns among the five mistakes that sink vendors, next to '
                              'not reading to the asterisks, trusting one quote, promising unachievable '
                              'delivery and ignoring SPRS [v7nJCLRc0uo @ 00:45:05]. Both still read the '
                              'front of the RFQ hard: Tris10 pulls solicitation and PR numbers, '
                              'procurement history, NSN, approved manufacturer and CLIN quantities, and '
                              'Tristan stops at page 10 of 24, so the real dispute is only whether '
                              'flowdown review happens before the bid or after the award.'],
               'table': {'caption': 'Competing DIBBS brokering playbooks, side by side',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['How old an RFQ is still worth quoting',
                                   'Tris10 and Tristan Thomas work only the newest RFQs and reject 60 to '
                                   '90 day lookbacks',
                                   'DVN quoted a wiper-blade solicitation still open after its September '
                                   '28 deadline had passed',
                                   'Tris10 @ MeND ([v4ulUMKE5xA @ 00:04:14]); Secureframe ([v7nJCLRc0uo @ '
                                   '00:20:44]); The DLA Vendor Network (DVN) ([MyfmHjDF9HI @ 00:25:44])'],
                                  ['Delivery days entered against the required date',
                                   'DVN bid 90 days against a 284-day requirement, noting bids can be '
                                   'revised later',
                                   'Tristan Thomas quotes real lead time and won at 300 days versus 25 '
                                   'requested',
                                   'The DLA Vendor Network (DVN) ([MyfmHjDF9HI @ 00:35:09]); Secureframe '
                                   '([v7nJCLRc0uo @ 00:30:17])'],
                                  ['How to set the markup on a sourced part',
                                   'DVN applied a 10% markup worth about $2 per unit and $642 total profit',
                                   'Tristan Thomas targets 10 to 15% and switched to judging profit '
                                   'dollars for more awards',
                                   'The DLA Vendor Network (DVN) ([MyfmHjDF9HI @ 00:31:22]); Secureframe '
                                   '([v7nJCLRc0uo @ 00:39:17])'],
                                  ['Which approved-source status a newcomer should chase first',
                                   'Tris10 and Loocey target blank-PID or null approved-source items for '
                                   'beginners and manufacturers',
                                   'Humam Finding Sam priced a demo item carrying 3 approved sources off '
                                   'past award history',
                                   'Tris10 @ MeND ([JE_OOJ3NAVk @ 00:09:49]); Loocey DLA & GovCon '
                                   '([LzmJyrGyMBw @ 00:00:34]); Humam Finding Sam ([wxZNfwOuung @ '
                                   '00:05:43])'],
                                  ['How the DIBBS batch quote file gets built',
                                   "DVN's DLA BUS parses solicitation PDFs against a stored catalog behind "
                                   'a paid demo',
                                   'FedOpp builds and checks each line in the browser and never submits '
                                   'any bids',
                                   'The DLA Vendor Network (DVN) ([YlwuuaCoHzQ @ 00:18:15]); FedOpp '
                                   '([iTxJkLPYuqc @ 00:00:04])'],
                                  ['How big a catalog you need before batch bidding',
                                   'Attendee Elizabeth predicted that building the catalog would take '
                                   'about 10 years of work',
                                   'The DVN host answered it takes a day for 14, and every bid NSN joins '
                                   'the catalog',
                                   'The DLA Vendor Network (DVN) ([YlwuuaCoHzQ @ 00:17:26]); The DLA '
                                   'Vendor Network (DVN) ([jjX9klCZFKI @ 00:20:13])'],
                                  ['Which code should drive the daily opportunity search',
                                   'Attendee Bogdan reported working a single NAICS code to find DLA '
                                   'opportunities',
                                   'The DVN host searched FSC 6220 and found 88 active solicitations, 26 '
                                   'open under AMSC G',
                                   'The DLA Vendor Network (DVN) ([YlwuuaCoHzQ @ 00:25:08]); The DLA '
                                   'Vendor Network (DVN) ([YlwuuaCoHzQ @ 00:30:01])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The most common bleed happens before a bid is ever typed. Tris10 @ MeND '
                              'opens on suppliers who no-bid, never respond, or quote far above the '
                              'eventual award, then admits they came to find out suppliers had no idea '
                              'what an NSN number is, which is why each NSN now gets mapped to the '
                              'supplier part number through the nsn-now public search [JE_OOJ3NAVk @ '
                              '00:03:52]. When a supplier still declines, they phone to ask why it was a '
                              'no-bid instead of moving on blind [JE_OOJ3NAVk @ 00:15:51]. Humam Finding '
                              'Sam flags the vendor-side margin killer: surcharges left out of a quote are '
                              'either going to eat your profit margin or end the bid with a loss, so the '
                              'request has to carry NSN, part number, drawings and delivery date and '
                              'demand all-inclusive pricing [wxZNfwOuung @ 00:08:30]. Tristan Thomas '
                              'closes the same loop from the other side: always follow an email with a '
                              'call, including after a no-bid, because it is harder to say no to a person '
                              'when you hear their voice [v7nJCLRc0uo @ 00:54:07]. The economic check is '
                              'simple: no line goes into DIBBS on a single unverified number while lead '
                              'time, certs, country of origin, cert fees and traceability are still '
                              'unanswered.',
                              'DIBBS itself punishes sloppy operators. myContractScout warns that you '
                              'cannot hit the Enter button to run a search, that a soldier-hand error '
                              'means refresh and redo, and that the browser back button times the session '
                              "out [SeWe_WAhyVg @ 00:05:23]. The DLA Vendor Network's demo upload of 20 "
                              'solicitations passed only 11, with the other nine flagged red as already '
                              'awarded, cancelled or closed, and the same session warns that DLA will tell '
                              'you when you did not win but not when a buy was cancelled [YlwuuaCoHzQ @ '
                              '00:12:25]. Ki Hendris adds that DLA posts 2,000 to 3,000 solicitations a '
                              'day and often cancels and reissues them, so a dead solicitation number is '
                              'routine rather than a glitch [jjX9klCZFKI @ 00:32:59]. Manual entry, per '
                              'the same DVN camp, compounds the damage, burning three to five minutes per '
                              "bid with errors such as the wrong CAGE code or the wrong price. FedOpp's "
                              'answer is a check-line pass that flags errors in red with a running count '
                              'of items left to fix, and an exporter that only exports files that pass '
                              "DLA's format rules [iTxJkLPYuqc @ 00:04:03]. The operator lesson: expect "
                              'part of every batch to bounce, and recheck status before blaming your '
                              'price.',
                              'Eligibility traps cost the most because they surface after the sourcing '
                              'work is done. Tris10 @ MeND warns that parts from a non-qualifying country '
                              "such as China or Afghanistan disqualify the quote, and states flatly, 'in "
                              "our case, we only buy American' [v4ulUMKE5xA @ 00:12:48]. They also caution "
                              'that a procurement-history line only shows that someone won the award; a '
                              'cancellation or protest may have followed, so the past price is a guide '
                              'rather than a lock [Z9MLGFqFXtM @ 00:02:03]. Ki Hendris answers a question '
                              "about passing JCP tech data to an uncertified shop with 'No, it is not "
                              "legal,' unless the manufacturer is also certified, a hard stop for brokers "
                              'who want to hand C-folder drawings to an outside manufacturer [jjX9klCZFKI '
                              '@ 00:34:01]. The DLA Vendor Network frames the volume side just as soberly: '
                              'GovCon is not a sprint, no company has a 100% hit ratio, and the target of '
                              'ten bids a day comes with traceability requests you should expect '
                              '[MyfmHjDF9HI @ 00:40:33]. Run every quote past those three checks, origin, '
                              'tech-data rights and documentation, before the price ever gets entered.'],
               'table': {'caption': 'Firsthand traps reported by DIBBS practitioners and the fixes they '
                                    'use',
                         'headers': ['Trap',
                                     'What The Practitioner Hit',
                                     'Operator Fix Taught',
                                     'Expert Source'],
                         'rows': [['Suppliers blind to NSN numbers',
                                   'Suppliers had no idea what an NSN number is and no-bid or ignored RFQs',
                                   'Map each NSN to the supplier part number via nsn-now public search, '
                                   'then call',
                                   'Tris10 @ MeND ([JE_OOJ3NAVk @ 00:03:52])'],
                                  ['Hidden surcharges in vendor quotes',
                                   'Surcharges outside the vendor quote eat the margin or turn the bid '
                                   'into a loss',
                                   'Send NSN, part number, drawings and delivery date and demand '
                                   'all-inclusive pricing',
                                   'Humam Finding Sam ([wxZNfwOuung @ 00:08:30])'],
                                  ['DIBBS session timeouts and lockouts',
                                   'DIBBS times out after three idle minutes and locks you out for 15 '
                                   'minutes',
                                   'Never use the browser back button, and click Search instead of hitting '
                                   'Enter',
                                   'The DLA Vendor Network (DVN) ([YlwuuaCoHzQ @ 00:13:28]); '
                                   'myContractScout ([SeWe_WAhyVg @ 00:07:04])'],
                                  ['Silent solicitation cancellations',
                                   '9 of 20 uploaded solicitations failed as already awarded, cancelled or '
                                   'closed',
                                   'Recheck status before bidding because DLA will not tell you a buy was '
                                   'cancelled',
                                   'The DLA Vendor Network (DVN) ([YlwuuaCoHzQ @ 00:10:29])'],
                                  ['Approved-source knockouts',
                                   'AMSC codes that limit a buy to approved sources can knock you out '
                                   'entirely',
                                   'Run the AMSC filter and confirm the approved-source CAGE before any '
                                   'sourcing work',
                                   'FedOpp ([bTlxn6BVHJ0 @ 00:02:02]); Tris10 @ MeND ([JE_OOJ3NAVk @ '
                                   '00:08:55])'],
                                  ['Margin overreach on the quote',
                                   'Asking for a 20 to 30% margin gets you underbid on the award',
                                   'Hold the 10 to 15% band and judge the profit dollar amount per award',
                                   'Secureframe ([v7nJCLRc0uo @ 00:38:03])'],
                                  ['Quoting stale No Bid list items',
                                   'No Bid list solicitations got no acceptable quote but DLA still needs '
                                   'the parts',
                                   'Check whether a new solicitation is open on DIBBS before you quote the '
                                   'part',
                                   'FedOpp ([qmdunkO7mts @ 00:02:01])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Four Stops Before The Price Field',
                           'body': 'Every DIBBS quote clears these four checks before a unit price gets '
                                   'entered, each drawn from a practitioner warning.',
                           'items': ['Origin check: confirm the part does not come from a non-qualifying '
                                     'country such as China or Afghanistan, because that disqualifies the '
                                     'quote [Tris10 @ MeND — v4ulUMKE5xA @ 00:12:48].',
                                     'Tech-data check: never pass JCP technical data to a manufacturer '
                                     'that is not also certified, which Ki Hendris calls not legal [The '
                                     'DLA Vendor Network (DVN) — jjX9klCZFKI @ 00:34:01].',
                                     'Source check: an approved-source CAGE in the PID is mandatory, '
                                     'though you may buy that part through a distributor [Tris10 @ MeND — '
                                     'JE_OOJ3NAVk @ 00:08:55].',
                                     'Document check: always read the full solicitation on DIBBS before '
                                     'you quote [FedOpp — bTs2wy13K1c @ 00:02:49].']}}],
 'pull_quote': '"There is a direct correlation between the amount of bids that you put into the system and '
               'the amount of awards that you win." Tris10 @ MeND (v4ulUMKE5xA @ 00:15:55).',
 'diagram_id': 'diag-06',
 'action_checklist': ['Pick 3 to 5 FSCs in your lane, search DIBBS by Federal Supply Class, click Search '
                      'instead of Enter, and log results in Google Sheets [myContractScout — SeWe_WAhyVg @ '
                      '00:08:07].',
                      "Build a saved 'MFG items' view filtered where Approved Sources is null, then "
                      'confirm via the NSN pop-up and the DIBBS NSN page [Loocey DLA & GovCon — '
                      'LzmJyrGyMBw @ 00:00:34].',
                      'Anchor your price on procurement history and past awards before calling vendors, '
                      'since about 99% of awards go to the cheapest bid [Humam Finding Sam — wxZNfwOuung @ '
                      '00:06:24].',
                      'Send the RFQ email asking lead time, stock, certs, country of origin, cert fees and '
                      'traceability, then follow up by phone [Tris10 @ MeND — JE_OOJ3NAVk @ 00:14:37].',
                      'Price at a 10 to 15% margin and judge the profit dollar amount rather than the '
                      'percentage alone [Secureframe — v7nJCLRc0uo @ 00:38:03].',
                      'Clear every yellow field, choose Net 30, set quote validity at 30 to 45 days, and '
                      'keep bid volume high [Tris10 @ MeND — v4ulUMKE5xA @ 00:02:32].'],
 'statutory_citations': [{'title': 'Tris10 @ MeND — How to Bid on DLA / DIBBS and Win in 2025 - Government '
                                   'Contracting [00:04:14]',
                          'url': 'https://www.youtube.com/watch?v=v4ulUMKE5xA&t=254s',
                          'relevance': 'Primary practitioner testimony on the 60-day RFQ age cutoff and '
                                       'bidding after expiration.'},
                         {'title': 'Secureframe — Defense Logistics Agency Contracts: How to Bid '
                                   'Effectively with the DLA [00:38:03]',
                          'url': 'https://www.youtube.com/watch?v=v7nJCLRc0uo&t=2283s',
                          'relevance': 'Primary practitioner testimony on the 10 to 15% margin sweet spot '
                                       'and underbid risk.'},
                         {'title': 'The DLA Vendor Network (DVN) — TOP DLA Vendors Use DIBBS Batch Bidding '
                                   'to Win Big!🤯 [00:34:01]',
                          'url': 'https://www.youtube.com/watch?v=jjX9klCZFKI&t=2041s',
                          'relevance': 'Primary practitioner testimony on JCP tech data sharing limits for '
                                       'brokers.'},
                         {'title': 'The DLA Vendor Network (DVN) — How to Automate DLA Bidding: The DLA '
                                   'BUS (DIBBS Batch Bidding)🚀 [00:10:29]',
                          'url': 'https://www.youtube.com/watch?v=YlwuuaCoHzQ&t=629s',
                          'relevance': 'Primary practitioner testimony on silent solicitation '
                                       'cancellations and batch upload failures.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'JE_OOJ3NAVk',
                       'title': 'Find the Right Supplier - DLA / DIBBS Government Contracting',
                       'channel': 'Tris10 @ MeND',
                       'author': 'Tris10 @ MeND',
                       'text': "It's much harder for someone to say no to you over the phone than it is "
                               'via email.',
                       'tip': "It's much harder for someone to say no to you over the phone than it is via "
                              'email.',
                       'timestamp': 667,
                       'timestamp_seconds': 667,
                       'timestamp_label': '[00:11:07]',
                       'url': 'https://www.youtube.com/watch?v=JE_OOJ3NAVk&t=667s',
                       'markdown': '[00:11:07](https://www.youtube.com/watch?v=JE_OOJ3NAVk&t=667s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'wxZNfwOuung',
                       'title': 'How to Win DIBBS Contracts (Step-by-Step Beginner Guide)',
                       'channel': 'Humam Finding Sam',
                       'author': 'Humam Finding Sam',
                       'text': 'So that is either going to eat your profit margin or even end the bid with '
                               'a loss.',
                       'tip': 'So that is either going to eat your profit margin or even end the bid with '
                              'a loss.',
                       'timestamp': 510,
                       'timestamp_seconds': 510,
                       'timestamp_label': '[00:08:30]',
                       'url': 'https://www.youtube.com/watch?v=wxZNfwOuung&t=510s',
                       'markdown': '[00:08:30](https://www.youtube.com/watch?v=wxZNfwOuung&t=510s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'qmdunkO7mts',
                       'title': 'DLA Urgent Need and DIBBS No Bid List: In-Stock Parts | FedOpp',
                       'channel': 'FedOpp',
                       'author': 'FedOpp',
                       'text': 'DLA still needs these parts, so check whether a new solicitation is open '
                               'on DIBBS before you quote.',
                       'tip': 'DLA still needs these parts, so check whether a new solicitation is open on '
                              'DIBBS before you quote.',
                       'timestamp': 121,
                       'timestamp_seconds': 121,
                       'timestamp_label': '[00:02:01]',
                       'url': 'https://www.youtube.com/watch?v=qmdunkO7mts&t=121s',
                       'markdown': '[00:02:01](https://www.youtube.com/watch?v=qmdunkO7mts&t=121s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'SeWe_WAhyVg',
                       'title': 'How to Find 400+ Government Contracts on DLA DIBBS',
                       'channel': 'myContractScout',
                       'author': 'myContractScout',
                       'text': 'You cannot hit the enter button.',
                       'tip': 'You cannot hit the enter button.',
                       'timestamp': 323,
                       'timestamp_seconds': 323,
                       'timestamp_label': '[00:05:23]',
                       'url': 'https://www.youtube.com/watch?v=SeWe_WAhyVg&t=323s',
                       'markdown': '[00:05:23](https://www.youtube.com/watch?v=SeWe_WAhyVg&t=323s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Z9MLGFqFXtM',
                       'title': 'What Information to Extract in a DLA / DIBBS RFQs',
                       'channel': 'Tris10 @ MeND',
                       'author': 'Tris10 @ MeND',
                       'text': "It just shows that they won the award, maybe there's a cancellation later "
                               'on, maybe there was some protest, whatever might be.',
                       'tip': "It just shows that they won the award, maybe there's a cancellation later "
                              'on, maybe there was some protest, whatever might be.',
                       'timestamp': 123,
                       'timestamp_seconds': 123,
                       'timestamp_label': '[00:02:03]',
                       'url': 'https://www.youtube.com/watch?v=Z9MLGFqFXtM&t=123s',
                       'markdown': '[00:02:03](https://www.youtube.com/watch?v=Z9MLGFqFXtM&t=123s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'MyfmHjDF9HI',
                       'title': 'How to Win DLA Contracts: Live DIBBS Solicitation Review & Bid',
                       'channel': 'The DLA Vendor Network (DVN)',
                       'author': 'The DLA Vendor Network (DVN)',
                       'text': 'Bid and bid often because you can always circle back and revise your bid '
                               "after you've submitted your bid.",
                       'tip': 'Bid and bid often because you can always circle back and revise your bid '
                              "after you've submitted your bid.",
                       'timestamp': 2156,
                       'timestamp_seconds': 2156,
                       'timestamp_label': '[00:35:56]',
                       'url': 'https://www.youtube.com/watch?v=MyfmHjDF9HI&t=2156s',
                       'markdown': '[00:35:56](https://www.youtube.com/watch?v=MyfmHjDF9HI&t=2156s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'v4ulUMKE5xA',
                       'title': 'How to Bid on DLA / DIBBS and Win in 2025 - Government Contracting',
                       'channel': 'Tris10 @ MeND',
                       'author': 'Tris10 @ MeND',
                       'text': 'And also what we want to do is look at the ones that are the newest '
                               'because we know that a contracting officer has put that into the system.',
                       'tip': 'And also what we want to do is look at the ones that are the newest because '
                              'we know that a contracting officer has put that into the system.',
                       'timestamp': 307,
                       'timestamp_seconds': 307,
                       'timestamp_label': '[00:05:07]',
                       'url': 'https://www.youtube.com/watch?v=v4ulUMKE5xA&t=307s',
                       'markdown': '[00:05:07](https://www.youtube.com/watch?v=v4ulUMKE5xA&t=307s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'v4ulUMKE5xA',
                       'title': 'How to Bid on DLA / DIBBS and Win in 2025 - Government Contracting',
                       'channel': 'Tris10 @ MeND',
                       'author': 'Tris10 @ MeND',
                       'text': 'There is a direct correlation between the amount of bids that you put into '
                               'the system and the amount of awards that you win.',
                       'tip': 'There is a direct correlation between the amount of bids that you put into '
                              'the system and the amount of awards that you win.',
                       'timestamp': 955,
                       'timestamp_seconds': 955,
                       'timestamp_label': '[00:15:55]',
                       'url': 'https://www.youtube.com/watch?v=v4ulUMKE5xA&t=955s',
                       'markdown': '[00:15:55](https://www.youtube.com/watch?v=v4ulUMKE5xA&t=955s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'LzmJyrGyMBw',
                       'title': 'How To Find DLA RFQs For Manufacturing / AMSC (RFQs With No Approved '
                                'Sources) – DLA/DIBBS',
                       'channel': 'Loocey DLA & GovCon',
                       'author': 'Loocey DLA & GovCon',
                       'text': 'Then select approved sources for the column and condition is null and hit '
                               'apply.',
                       'tip': 'Then select approved sources for the column and condition is null and hit '
                              'apply.',
                       'timestamp': 34,
                       'timestamp_seconds': 34,
                       'timestamp_label': '[00:00:34]',
                       'url': 'https://www.youtube.com/watch?v=LzmJyrGyMBw&t=34s',
                       'markdown': '[00:00:34](https://www.youtube.com/watch?v=LzmJyrGyMBw&t=34s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'OiMCYKFBggE',
                       'title': 'Increase your DLA | DIBBS | Government Contracting Success with Intertek '
                                '/ SAI Global Online Tools!',
                       'channel': 'The DLA Vendor Network (DVN)',
                       'author': 'The DLA Vendor Network (DVN)',
                       'text': 'We are excited to introduce our partner SAI Global as a multinational '
                               'software and services company.',
                       'tip': 'We are excited to introduce our partner SAI Global as a multinational '
                              'software and services company.',
                       'timestamp': 41,
                       'timestamp_seconds': 41,
                       'timestamp_label': '[00:00:41]',
                       'url': 'https://www.youtube.com/watch?v=OiMCYKFBggE&t=41s',
                       'markdown': '[00:00:41](https://www.youtube.com/watch?v=OiMCYKFBggE&t=41s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'YNtu76ny5MI',
                       'title': '🎓How To Sell to the DLA | DIBBS 🏆The DLA Need to Know Guide',
                       'channel': 'The DLA Vendor Network (DVN)',
                       'author': 'The DLA Vendor Network (DVN)',
                       'text': 'Evaluation criteria may include price, technical capability, past '
                               'performance and other factors.',
                       'tip': 'Evaluation criteria may include price, technical capability, past '
                              'performance and other factors.',
                       'timestamp': 160,
                       'timestamp_seconds': 160,
                       'timestamp_label': '[00:02:40]',
                       'url': 'https://www.youtube.com/watch?v=YNtu76ny5MI&t=160s',
                       'markdown': '[00:02:40](https://www.youtube.com/watch?v=YNtu76ny5MI&t=160s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'jjX9klCZFKI',
                       'title': 'TOP DLA Vendors Use DIBBS Batch Bidding to Win Big!🤯',
                       'channel': 'The DLA Vendor Network (DVN)',
                       'author': 'The DLA Vendor Network (DVN)',
                       'text': 'No, it is not legal.',
                       'tip': 'No, it is not legal.',
                       'timestamp': 2041,
                       'timestamp_seconds': 2041,
                       'timestamp_label': '[00:34:01]',
                       'url': 'https://www.youtube.com/watch?v=jjX9klCZFKI&t=2041s',
                       'markdown': '[00:34:01](https://www.youtube.com/watch?v=jjX9klCZFKI&t=2041s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'bTs2wy13K1c',
                       'title': 'Find DLA Parts to Quote by FSC Code: Open DIBBS RFQs in FedOpp',
                       'channel': 'FedOpp',
                       'author': 'FedOpp',
                       'text': 'Fewer sources can mean less competition, so these are worth a closer look.',
                       'tip': 'Fewer sources can mean less competition, so these are worth a closer look.',
                       'timestamp': 120,
                       'timestamp_seconds': 120,
                       'timestamp_label': '[00:02:00]',
                       'url': 'https://www.youtube.com/watch?v=bTs2wy13K1c&t=120s',
                       'markdown': '[00:02:00](https://www.youtube.com/watch?v=bTs2wy13K1c&t=120s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'v7nJCLRc0uo',
                       'title': 'Defense Logistics Agency Contracts: How to Bid Effectively with the DLA',
                       'channel': 'Secureframe',
                       'author': 'Secureframe',
                       'text': 'The real sweet spot there is anywhere between 10 and 15%.',
                       'tip': 'The real sweet spot there is anywhere between 10 and 15%.',
                       'timestamp': 2283,
                       'timestamp_seconds': 2283,
                       'timestamp_label': '[00:38:03]',
                       'url': 'https://www.youtube.com/watch?v=v7nJCLRc0uo&t=2283s',
                       'markdown': '[00:38:03](https://www.youtube.com/watch?v=v7nJCLRc0uo&t=2283s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'v7nJCLRc0uo',
                       'title': 'Defense Logistics Agency Contracts: How to Bid Effectively with the DLA',
                       'channel': 'Secureframe',
                       'author': 'Secureframe',
                       'text': "And it's harder to say no to a person, you know, when you hear their voice "
                               "that they're actually a human being, not just an email that's there.",
                       'tip': "And it's harder to say no to a person, you know, when you hear their voice "
                              "that they're actually a human being, not just an email that's there.",
                       'timestamp': 3247,
                       'timestamp_seconds': 3247,
                       'timestamp_label': '[00:54:07]',
                       'url': 'https://www.youtube.com/watch?v=v7nJCLRc0uo&t=3247s',
                       'markdown': '[00:54:07](https://www.youtube.com/watch?v=v7nJCLRc0uo&t=3247s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'YlwuuaCoHzQ',
                       'title': 'How to Automate DLA Bidding: The DLA BUS (DIBBS Batch Bidding)🚀',
                       'channel': 'The DLA Vendor Network (DVN)',
                       'author': 'The DLA Vendor Network (DVN)',
                       'text': "Now they will tell you when you didn't win, but they won't tell you when "
                               'it was cancelled.',
                       'tip': "Now they will tell you when you didn't win, but they won't tell you when it "
                              'was cancelled.',
                       'timestamp': 629,
                       'timestamp_seconds': 629,
                       'timestamp_label': '[00:10:29]',
                       'url': 'https://www.youtube.com/watch?v=YlwuuaCoHzQ&t=629s',
                       'markdown': '[00:10:29](https://www.youtube.com/watch?v=YlwuuaCoHzQ&t=629s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'iTxJkLPYuqc',
                       'title': 'FedOpp DIBBS Batch Quote File: Build It, Check It, Upload It on DIBBS',
                       'channel': 'FedOpp',
                       'author': 'FedOpp',
                       'text': "It only exports files that pass DLA's format rules.",
                       'tip': "It only exports files that pass DLA's format rules.",
                       'timestamp': 243,
                       'timestamp_seconds': 243,
                       'timestamp_label': '[00:04:03]',
                       'url': 'https://www.youtube.com/watch?v=iTxJkLPYuqc&t=243s',
                       'markdown': '[00:04:03](https://www.youtube.com/watch?v=iTxJkLPYuqc&t=243s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'bTlxn6BVHJ0',
                       'title': 'How to Find DIBBS RFQs on the DLA Bid Board by FSC, NSN and Due Date',
                       'channel': 'FedOpp',
                       'author': 'FedOpp',
                       'text': 'The codes that limit a buy to approved sources can knock you out.',
                       'tip': 'The codes that limit a buy to approved sources can knock you out.',
                       'timestamp': 122,
                       'timestamp_seconds': 122,
                       'timestamp_label': '[00:02:02]',
                       'url': 'https://www.youtube.com/watch?v=bTlxn6BVHJ0&t=122s',
                       'markdown': '[00:02:02](https://www.youtube.com/watch?v=bTlxn6BVHJ0&t=122s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'}]}
