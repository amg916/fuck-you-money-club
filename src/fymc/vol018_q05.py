from __future__ import annotations

CHAPTER_5 = {'id': 'Q5',
 'chapter_id': 'Q5',
 'chapter_number': 5,
 'question_number': 5,
 'slug': 'comping-and-pricing-vacant-land',
 'question_prompt': 'How do I figure out what a piece of vacant land is really worth before I make an '
                    'offer?',
 'kicker': 'Q5 / THE BIG MONEY PLAYBOOKS',
 'title': 'Comping and Pricing Vacant Land',
 'subtitle': 'Zillow, Redfin, and LandWatch comps, acreage price-per-acre adjustments, scraping LandWatch '
             'listings, pricing in non-disclosure states, why Zillow misleads on land values, avoiding '
             'overpaying, picking counties with Zillow data, and comping a subdivide',
 'layout_template': 'case_study',
 'reading_time_minutes': 15,
 'executive_summary': 'Land operators converge on one rule: value vacant land off sold, land-only comps in '
                      'a tight size band and a six-to-twelve-month window, then adjust for wetlands, '
                      'septic, and frontage. Seth of REtipster turns Redfin or LandWatch exports into a '
                      'price-per-acre average, and Price Boss and PRYCD automate the pull. Offer math is '
                      'blunt: Cool Wholesaling pegs Fairmont retail at $5,000 to $6,000 an acre and caps '
                      'an 8-acre buy at $35,000; Brent Bowers aims under 50 cents on the dollar. '
                      "Acrewell's Alex Reese says asking prices run two to four times market value. In "
                      'non-disclosure states, Sumner Advanced haircuts last list price by days on market, '
                      "while the Apke Brothers leaned on a realtor's opinion to justify a seven-parcel "
                      'subdivide. They split on tooling: Bowers calls PRYCD his easy button, while Seth '
                      'says Zillow often omits acreage.',
 'key_metrics': [{'label': 'Fairmont NC Retail Land Value and Max Buy',
                  'metric': 'Fairmont NC Retail Land Value and Max Buy',
                  'value': '$5,000-$6,000 per acre retail; 8 acres = $40,000 retail; target buy $30,000, '
                           '$35,000 max',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Zillow sold land comps (5 acres for $30,000, 9 acres for $50,000) used to '
                             'set wholesale offer on an 8-acre Lake View lot without viewing the parcel',
                  'source': 'Cool Wholesaling+ Land Deals-Real Estate Investing ([3x8J7AdyCEw @ '
                            '00:03:12])'},
                 {'label': 'Days-on-Market Discount to Last List Price',
                  'metric': 'Days-on-Market Discount to Last List Price',
                  'value': '0-15% at 1-90 days; about 20-30% at 3-6 months; 35% and up to 50% at 6-12 '
                           'months',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Haircut applied to last list price of sold comps and active listings in '
                             'non-disclosure states; listings older than one year excluded',
                  'source': 'Sumner Advanced ([8pB5HoHJ4Bk @ 00:04:05])'},
                 {'label': 'Asking Price Versus Market Value on Vacant Land',
                  'metric': 'Asking Price Versus Market Value on Vacant Land',
                  'value': 'Asking prices run 200-400% of market value; sellers accept offers 50-80%+ '
                           'below ask',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Alex Reese's read across hundreds of land tracts; a Middleburg FL lot fell "
                             'from $85,000 to a $20,000 sale after 2.5 years',
                  'source': 'Acrewell Land Company ([TbH_4hSsYHU @ 00:03:07])'},
                 {'label': 'Tate County MS Subdivide Comp Outcome',
                  'metric': 'Tate County MS Subdivide Comp Outcome',
                  'value': '70 acres bought for $135,000 plus ~$5,000 survey; 4 of 7 ten-acre parcels sold '
                           'at ~$62,000 average (~$240,000 back)',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Comps were thin in a non-disclosure state, so a trusted realtor's "
                             '$50,000-$70,000 per-parcel opinion set the $60,000 conservative model',
                  'source': 'Apke Brothers ([bIqgihxHoo8 @ 00:06:07])'}],
 'sections': [{'heading': 'Section 1: The Practitioner Consensus',
               'paragraphs': ['Every operator who runs land numbers starts in the same place: strip the '
                              'search down to vacant land and lean on what actually closed. Brent Bowers '
                              'clicks sold-only, deselects every home type, re-selects lots and land, and '
                              'keeps the window to six months, stretching to nine only when nothing shows, '
                              "because 'what someone is willing to pay for it is what the value actually "
                              "is' [JNufnuENoDM @ 00:01:05]. Seth of REtipster makes the identical cut on "
                              "Redfin, calling sold data 'almost always the better way to go' since it is "
                              "not some seller's or realtor's opinion, and warning that reaching back two "
                              'or three years makes the numbers less relevant [rYCHQ59jzhY @ 00:01:58]. '
                              'The Cool Wholesaling crew filters Fairmont, North Carolina by sold and home '
                              "type land, and reports that Jasper's team comps on Zillow almost "
                              "exclusively and doesn't even have PropStream [3x8J7AdyCEw @ 00:00:01]. "
                              'Damian of WE ARE LAND SPECIALISTS opens every Zillow pull with the price '
                              'filter switched off and a twelve-month sold window, then widens to 24 '
                              'months, or cross-checks county GIS last-sale data, when dirt barely trades '
                              'in the pocket [JRa_lwdSNjo @ 00:10:48]. The shared logic: the older or more '
                              "distant the sale, the less it tells you about today's buyer.",
                              'The second universal rule is apples to apples on size, because price per '
                              'acre collapses as parcels get bigger. Valuing an 8-acre lot in Fairmont, '
                              'the Cool Wholesaling crew set aside 37 acres at roughly 3,000 to 4,000 an '
                              "acre and 50 acres for 139,000, saying the per-acre price 'gets smaller as "
                              "you go up in size,' so those big tracts 'don't really apply' [3x8J7AdyCEw @ "
                              '00:01:22]. Seth of REtipster calls it a statistical constant: look at '
                              'thousands of vacant lots in one area and the smaller ones command more per '
                              'acre, so a five-acre subject comped off a 2.37-acre sale deserves a '
                              'discount on the per-acre figure [9cX2NuhnYro @ 00:09:39]. Brent Bowers '
                              'brackets hard, giving a 10-acre subject only 9-to-11-acre comps, and wants '
                              'them within a couple of miles, calling five miles out a stretch '
                              '[JNufnuENoDM @ 00:03:14]. Setting matters as much as acreage. Pricing a '
                              'rural lot between Antioch and Shannon near Red Springs, North Carolina, the '
                              'Cool Wholesaling team refused city comps, threw out subdivision lots as a '
                              'builder charging premium, dropped a 6,500 sale that looked landlocked '
                              'behind the main road, and landed on roughly 13,000 as max retail for a '
                              'rural parcel in a not-high-end area [t8XDRE0ZjFc @ 00:02:57].',
                              'The third point of agreement: raw per-acre math is only the skeleton, and '
                              'physical traits plus a local land agent finish the valuation. Once Upon a '
                              "Brick warns that 'not every two acres is the same': flat versus sloped, "
                              'wetland or not, road access, a pond, a skinny strip versus a rectangle with '
                              'road frontage, and how close electric and water run all move the price '
                              '[Tmf12E9Dg7A @ 00:06:15]. Alex Reese of Acrewell turns that into a six-step '
                              'check called ASSESS (access, soil, slope, environmental, street view, '
                              'satellite view) and shows a 3.3-acre lot with 2.8 acres outside mapped '
                              'wetlands behaving like a bigger property than a 4.58-acre lot with only 1.1 '
                              'acres outside [TbH_4hSsYHU @ 00:22:24]. Outliers get cut without apology: '
                              'Seth deletes any sale that does not line up with the rest, guessing it '
                              'carried some issue or was a deal between friends or family members '
                              '[rYCHQ59jzhY @ 00:06:17]. And almost everyone ends at the phone. Seth calls '
                              'two or three agents who list multiple vacant lots, asks what price moves a '
                              'five-acre parcel in 30 days, three months, or six months, and expects '
                              'different numbers from different agents, the same reason one comp is never '
                              'enough [9cX2NuhnYro @ 00:16:31].'],
               'table': {'caption': 'Where the land comping operators agree before any offer is calculated',
                         'headers': ['Consensus Rule',
                                     'How Operators Apply It',
                                     'Why It Matters',
                                     'Expert Source'],
                         'rows': [['Sold-only, land-only filter on every search',
                                   'Click sold, deselect all home types, then reselect only lots and land',
                                   'Closed sales show what buyers paid; asking prices are only seller '
                                   'hopes',
                                   'Brent Bowers ([JNufnuENoDM @ 00:01:21])'],
                                  ['Six to twelve month sold window',
                                   'Go back twelve months in steady markets, six months when values move '
                                   'fast',
                                   'Older sales lose relevance because land values can shift quickly year '
                                   'to year',
                                   'REtipster ([9cX2NuhnYro @ 00:02:10])'],
                                  ['Bracket the acreage around the subject parcel',
                                   'For a 2-acre subject, set Zillow lot size from 1 to 10 acres',
                                   'Then compare 2- and 3-acre sales and average five consistent sales',
                                   'Once Upon a Brick · The Land Investor ([Tmf12E9Dg7A @ 00:02:01])'],
                                  ['Asking price is not market value on land',
                                   "Ignore the ask and offer off sold comps and the property's real "
                                   'characteristics',
                                   'Land asking prices run two, three, even 400 percent of market value',
                                   'Acrewell Land Company ([TbH_4hSsYHU @ 00:03:07])'],
                                  ['Delete outliers before averaging per-acre prices',
                                   'Remove any sale far off the pattern, like $7,000 per acre among much '
                                   'higher numbers',
                                   'One odd sale from a problem parcel or family deal skews the whole '
                                   'average',
                                   'REtipster ([rYCHQ59jzhY @ 00:06:17])'],
                                  ['Physical traits adjust the comp-based number',
                                   'Run ASSESS: access, soil, slope, environmental, street view, and '
                                   'satellite view on each parcel',
                                   'Buildable area outside wetlands and septic-ready soil drive what '
                                   'buyers will pay',
                                   'Acrewell Land Company ([TbH_4hSsYHU @ 00:13:13])'],
                                  ['Land-specialist agents confirm the number by phone',
                                   'Pull agent names from active vacant-land listings and ask whether they '
                                   'list many lots',
                                   'Agents with ongoing land listings know local growth, schools, '
                                   'employers, and real demand',
                                   'REtipster ([9cX2NuhnYro @ 00:14:28])']]}},
              {'heading': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['The cleanest bulk method comes from Seth at REtipster, who credits Carl '
                              'James and Todd Millin from the REtipster community. Filter Redfin to land, '
                              'set a lot-size band, switch to sold, and hit the download button to pull '
                              'every comp into a spreadsheet [rYCHQ59jzhY @ 00:03:07]. Delete everything '
                              'except sale price and lot size, then add two columns: acres, calculated as '
                              'lot square feet divided by 43,560, and dollars per acre, calculated as '
                              'price divided by acres; drag both formulas down and finish with =AVERAGE '
                              'over the column [rYCHQ59jzhY @ 00:04:15]. Where Redfin hides the download '
                              'button, as in Costilla County, Colorado, Seth runs the free Chrome '
                              "extension Instant Data Scraper, points its locate-next button at Redfin's "
                              'page arrow so it crawls past the first 40 of 296 results, exports a CSV, '
                              'and uses find-and-replace to strip the word acres out of the size column, '
                              'which in one pass made 310 replacements [rYCHQ59jzhY @ 00:08:23]. Where '
                              'Redfin does not operate at all, like Tallapoosa County, Alabama, the same '
                              'scraper runs on LandWatch. Price Boss automates the LandWatch version: '
                              'advanced search by state and county, price 0 to 50,000, property type land, '
                              'sort by most recent so paid-to-the-top ads do not skew the pull, paste each '
                              'page into the yellow bar, and hit compute [FOpRZxfMs4I @ 00:01:32].',
                              'Once the per-acre number is set, operators move straight to offer math. The '
                              'Cool Wholesaling crew read Fairmont comps of 5 acres at 30,000 and 9 acres '
                              'at 50,000 as retail of 5,000 to 6,000 an acre, took the conservative 5,000 '
                              'because big parcels sell slower than single building lots, priced the '
                              '8-acre subject at 40,000 retail, and set the buy target at 30,000, 35,000 '
                              'max, without even pulling up the parcel [3x8J7AdyCEw @ 00:03:12]. Seth '
                              'reverse-engineers a single lot: 17,900 divided by 2.37 acres is $7,552 an '
                              'acre, then he knocks it to 7,000, 6,500, or 6,000 for a larger five-acre '
                              'subject [9cX2NuhnYro @ 00:09:00]. Brent Bowers caps comp research at 15 to '
                              '20 minutes per new area because land runs on averages and the offer is '
                              'ideally under 50 cents on the dollar, leaving room for error [JNufnuENoDM @ '
                              '00:10:39]. Alex Reese adjusts comps line by line: against a $20,000 sale in '
                              'the same Middleburg, Florida subdivision, an installed septic adds about '
                              '$10,000, a well about $15,000, and site prep at least $5,000, putting the '
                              'listed lot near $50,000, which is exactly what he would offer against a '
                              '$75,000 ask [TbH_4hSsYHU @ 00:07:34].',
                              'Non-disclosure states force operators to price off list data, and the '
                              'street method is a days-on-market haircut. Sumner Advanced reads the last '
                              'list price where a sold comp went under contract, never as the sale price: '
                              'same-day contingent likely closed at list, a 117-day listing gets maybe 10 '
                              'to 15 or 20 percent off, a 317-day listing 30 to 35 percent, and the '
                              'six-month-to-a-year band can run toward 50 percent, while active listings '
                              'older than a year are left out of the math [8pB5HoHJ4Bk @ 00:04:05]. The '
                              'Apke Brothers ran exactly this play in Tate County, Mississippi: a 9.4-acre '
                              'sale with a long listing history was guessed near $35,000, a 12-acre listed '
                              'at 125,000 that went pending after five months was pegged near $100,000, '
                              "and when comps still could not justify the price, a trusted local realtor's "
                              '50,000-to-70,000 opinion closed the gap [bIqgihxHoo8 @ 00:05:17]. When only '
                              'for-sale listings exist, Seth discounts them 20 to 30 percent [rYCHQ59jzhY '
                              '@ 00:02:42]. Jeff checks LandWatch descriptions for seller-finance terms, '
                              'where one ad showed 1,997 cash versus 297 down and 97 a month for 48 '
                              'months, and multiplies the monthly payment by the months to get the terms '
                              'price before treating it as a comp [mM0tCRujCDM @ 00:01:35].'],
               'table': {'caption': 'Tools, exact settings, and outputs the operators use to price vacant '
                                    'land',
                         'headers': ['Tool / Workflow',
                                     'Exact Settings & Numbers',
                                     'What It Produces',
                                     'Expert Source'],
                         'rows': [['Redfin sold-land spreadsheet export',
                                   'Land filter, lot band, sold; acres equals square feet divided by '
                                   '43,560; then =AVERAGE',
                                   'Average sold price per acre across every comp in the filtered area',
                                   'REtipster ([rYCHQ59jzhY @ 00:04:15])'],
                                  ['Instant Data Scraper Chrome extension',
                                   'Locate next button, start crawling, export CSV, strip acres text with '
                                   'find and replace',
                                   'Same per-acre spreadsheet where Redfin hides download or LandWatch is '
                                   'the only source',
                                   'REtipster ([rYCHQ59jzhY @ 00:07:41])'],
                                  ['Price Boss LandWatch scrape and compute',
                                   'Advanced search, county, price 0 to 50,000, land, newest first, paste '
                                   'pages, compute',
                                   '54 comps with price and acreage, subdivision write-ups highlighted '
                                   'green',
                                   'LandSpeed Price Boss ([FOpRZxfMs4I @ 00:05:08])'],
                                  ['PRYCD county valuation easy button',
                                   'Seven-day free trial, first 400 records free, offers from 5 to 95 '
                                   'cents on the dollar',
                                   'Values for 1-2, 3-5, buildable, and 10-acre parcels plus offer prices '
                                   'in Excel',
                                   'Brent Bowers ([JNufnuENoDM @ 00:11:58])'],
                                  ['Land Portal custom comp report',
                                   'Acreage 5 to 8, last 12 months, sold: about 104,000 per acre; 8 to 12 '
                                   'acres about 37,000',
                                   'Per-acre sold averages by band to price each lot in a planned split',
                                   'For Land and Country ([7FfLOUMhyyA @ 00:13:22])'],
                                  ['Zillow lot-size band for new county scouting',
                                   'Lot size 45,000 to 500,000 square feet, roughly 1 to 10 acres, sorted '
                                   'cheapest first',
                                   'Bottom-of-the-barrel list and sold range before committing to a new '
                                   'market',
                                   'REtipster ([E9KBudZB1Do @ 00:01:57])'],
                                  ['Assessed value plus last sale screen',
                                   'Start at assessed value, check last sale date and price; 57.5 assessed '
                                   'against 160,000 paid',
                                   'Kill-or-pursue call; leads that cannot get near their last sale get '
                                   'dropped',
                                   'WE ARE LAND SPECIALISTS ([JRa_lwdSNjo @ 00:06:25])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Shortcuts the Operators Actually Use',
                           'body': 'Small moves that sharpen a land number fast, taken straight from how '
                                   'these operators run their own deals.',
                           'items': ["Ask for the '30-day blowout price,' not the pie-in-the-sky number: "
                                     'Brent Bowers called a land realtor about a parcel he had at $285, '
                                     "heard about $10,000 within 45 days, then took the realtor's own "
                                     '$5,000 offer and closed four days later [Brent Bowers — JNufnuENoDM '
                                     '@ 00:07:30].',
                                     'Sort LandWatch by most recent before scraping so the pull is not '
                                     'stacked with only cheap ads, only expensive ads, or ads someone paid '
                                     "to push to the top; then use the green 'subdivision' highlight or "
                                     'the city to fill the subdivision column [LandSpeed Price Boss — '
                                     'FOpRZxfMs4I @ 00:01:32].',
                                     'Read demand off the listing page: most Cedar Springs lots sitting '
                                     'under 100 days and one lot pulling 498 views in 57 days signals '
                                     'decent land demand, while 10 or 20 views and no saves after months '
                                     'signals a dead market [REtipster — 9cX2NuhnYro @ 00:13:12].',
                                     'In non-disclosure counties, check land.com sold listings: sellers '
                                     'self-report the sold price there, and more times than not they '
                                     'report it accurately; LandFlip only shows actives [Sumner Advanced — '
                                     '8pB5HoHJ4Bk @ 00:05:17].']},
               'sop_steps': [{'step': 1,
                              'title': 'Lock the Search Box',
                              'action': 'Filter Zillow or Redfin to sold, lots and land only, a bracketed '
                                        'acreage band, and a six-month window.',
                              'detail': 'Bowers deselects every home type, reselects lots and land, '
                                        'matches HOA status to the subject, brackets a 10-acre parcel at 9 '
                                        'to 11 acres, and widens to nine months only when nothing appears '
                                        '[Brent Bowers — JNufnuENoDM @ 00:01:39].'},
                             {'step': 2,
                              'title': 'Build the Per-Acre Sheet',
                              'action': 'Export or scrape price and lot size, convert to acres, compute '
                                        'dollars per acre, and average it.',
                              'detail': 'Divide square feet by 43,560 for acres, divide sale price by '
                                        'acres, delete outliers that do not line up, and run =AVERAGE down '
                                        'the dollars-per-acre column [REtipster — rYCHQ59jzhY @ '
                                        '00:05:19].'},
                             {'step': 3,
                              'title': 'Haircut List Data and Adjust for Improvements',
                              'action': 'Discount list-price comps by days on market, then add or subtract '
                                        'for septic, well, site prep, and wetlands.',
                              'detail': 'Take up to 15 percent off inside 90 days, around 20 to 30 percent '
                                        'at three to six months, 35 percent or more past six months, and '
                                        'skip actives older than a year [Sumner Advanced — 8pB5HoHJ4Bk @ '
                                        '00:04:05]; credit installed septic, well, and site prep the way '
                                        'Alex Reese added about $30,000 over a raw comp [Acrewell Land '
                                        'Company — TbH_4hSsYHU @ 00:08:06].'},
                             {'step': 4,
                              'title': 'Verify by Phone, Then Set the Offer',
                              'action': 'Get a quick-sale number from a land-specialist agent and back the '
                                        'offer out of conservative retail.',
                              'detail': 'Find the land specialist on LandWatch and ask what the parcel '
                                        'sells for in 30 days [Brent Bowers — JNufnuENoDM @ 00:08:59], '
                                        'then work backward from conservative retail, as with 8 acres at '
                                        '$5,000 an acre for $40,000 retail and a $30,000 to $35,000 max '
                                        'buy [Cool Wholesaling+ Land Deals-Real Estate Investing — '
                                        '3x8J7AdyCEw @ 00:03:12].'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The first split is over which free portal deserves to be the primary comp '
                              'engine. Cool Wholesaling+ Land Deals argues Zillow now works really well '
                              "for comping and says Jasper's team runs almost exclusively on it without "
                              "even paying for PropStream [3x8J7AdyCEw @ 00:00:01]. REtipster's Seth backs "
                              'Zillow for scouting a new county because it serves the most markets and has '
                              'the best mapping and filtering functionality [E9KBudZB1Do @ 00:00:30], but '
                              'for hard per-acre math the order flips: Zillow is a poor fit because it '
                              'does not consistently put acreages in its listings, so the Redfin '
                              'spreadsheet download comes first, with LandWatch as the backup [rYCHQ59jzhY '
                              '@ 00:13:46]. LandSpeed Price Boss skips the house portals entirely, running '
                              'a LandWatch advanced search by county with a 0 to 50,000 price band and '
                              'land-only property type, sorting by most recent so the results are not '
                              'skewed toward the cheapest ads, the priciest ads or the sellers who paid to '
                              'float to the top of the page [FOpRZxfMs4I @ 00:01:32]. The real choice is '
                              'about data shape. Zillow suits map-based eyeballing in thick markets where '
                              'sold pins are plentiful. Redfin exports or scraped LandWatch pages suit '
                              'operators who want a clean column of prices divided by a column of acres '
                              'and averaged across dozens of rows.',
                              'Practitioners also disagree on how far back and how wide to cast the net. '
                              'DannyG Real Estate starts at six months sold, as tight as possible, and '
                              'only expands if nothing turns up, because starting narrow finds the best '
                              'possible comp [UqPvFZ6TGGo @ 00:00:46]. Brent Bowers also anchors on six '
                              'months because a lot can change in that window, stretching to nine months '
                              'only when land comps are scarce, and insists on a tight apples-to-apples '
                              'size band of 9 to 11 acres for a 10-acre subject [JNufnuENoDM @ 00:03:14]. '
                              'WE ARE LAND SPECIALISTS runs the opposite default: kill the price filter, '
                              'pull the last 12 months of lots and land, and if the pocket is thin, push '
                              'Zillow or the county GIS sales layer out to 24 months [JRa_lwdSNjo @ '
                              '00:10:48]. Once Upon a Brick sets a far looser size band, telling a buyer '
                              'comping a 2-acre parcel to search 1 to 10 acres and then average about five '
                              'similar sales rather than trusting any single one [Tmf12E9Dg7A @ 00:02:01]. '
                              'The tension is volume versus relevance. Narrow windows protect against '
                              'stale prices in markets that are moving, but when the sold pins run dry, '
                              'the tight operators end up expanding anyway, while the wide-net operators '
                              'accept noisier per-acre numbers and lean on averaging to smooth the spread.',
                              'The sharpest numeric disagreement is how hard to haircut asking prices. '
                              'REtipster applies a 20 to 30 percent discount when forced to use for-sale '
                              'listings in thin markets [rYCHQ59jzhY @ 00:02:42]. Sumner Advanced builds a '
                              'sliding scale off days on market in non-disclosure states: a listing that '
                              'went contingent within about 90 days gets 0 to 15 percent, three to six '
                              'months roughly 20 to 30 percent, six months to a year 35 percent or as much '
                              'as 50 percent, and anything active longer than a year gets thrown out of '
                              'the discount math entirely [8pB5HoHJ4Bk @ 00:04:05]. Acrewell Land Company '
                              'goes much further, calling asking prices made-up numbers that can run two, '
                              'three or 400 percent of market value, with sellers accepting offers 50 to '
                              '80 percent below ask, often without even countering [TbH_4hSsYHU @ '
                              '00:03:07]. Brent Bowers frames it as a national rule of thumb that people '
                              'ask a little more than they actually get, yet the example given has a '
                              '10,000 ask on five acres hopefully landing around 5,000 [JNufnuENoDM @ '
                              '00:04:31]. Which scale an operator adopts directly sets the retail anchor, '
                              'and every offer built downstream inherits that error in either direction.'],
               'table': {'caption': 'Competing comp playbooks for vacant land, side by side as '
                                    'practitioners run them',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Primary free portal for pulling vacant land comps',
                                   'Zillow sold filter on lots and land, used almost exclusively by '
                                   "Jasper's team without PropStream",
                                   'Redfin spreadsheet download first because Zillow listings often omit '
                                   'acreage, LandWatch kept as backup',
                                   'Cool Wholesaling+ Land Deals-Real Estate Investing ([3x8J7AdyCEw @ '
                                   '00:00:01]); REtipster ([rYCHQ59jzhY @ 00:13:46])'],
                                  ['How far back the sold lookback window should reach',
                                   'Start at six months sold and expand only if nothing nearby shows up',
                                   'Pull the last 12 months, then stretch Zillow or county GIS sales to 24 '
                                   'months',
                                   'DannyG Real Estate ([UqPvFZ6TGGo @ 00:00:46]); WE ARE LAND SPECIALISTS '
                                   '([JRa_lwdSNjo @ 00:10:48])'],
                                  ['How tight the acreage band around the subject should be',
                                   'Tight band of 9 to 11 acres when the subject parcel is 10 acres',
                                   'Loose band of 1 to 10 acres for a 2-acre subject, then average five '
                                   'sales',
                                   'Brent Bowers ([JNufnuENoDM @ 00:03:14]); Once Upon a Brick · The Land '
                                   'Investor ([Tmf12E9Dg7A @ 00:02:01])'],
                                  ['Haircut applied when only list prices are available to comp',
                                   'Flat 20 to 30 percent discount applied to for-sale listings in thin '
                                   'markets',
                                   'Days-on-market scale running from 0 to 15 percent up to as much as 50 '
                                   'percent',
                                   'REtipster ([rYCHQ59jzhY @ 00:02:42]); Sumner Advanced ([8pB5HoHJ4Bk @ '
                                   '00:04:05])'],
                                  ['Software valuation engine versus manual comp selection by hand',
                                   'PRYCD easy button returns comps and offer tiers from 5 to 95 cents in '
                                   'Excel',
                                   'Manual Zillow method is slowest, but with PRYCD you do not control '
                                   'what it pulls',
                                   'Brent Bowers ([JNufnuENoDM @ 00:11:09]); REtipster ([9cX2NuhnYro @ '
                                   '00:20:16])'],
                                  ['Fallback when a non-disclosure state hides the real sold prices',
                                   'Call local land realtors for price opinions when sold comps cannot '
                                   'justify the number',
                                   'Skip buying MLS access, mail offers and iterate pricing across about '
                                   'two campaigns',
                                   'Apke Brothers ([bIqgihxHoo8 @ 00:05:33]); Sumner Advanced '
                                   '([8pB5HoHJ4Bk @ 00:06:22])'],
                                  ['Screening sellers whose price expectations sit far above comps',
                                   'Kill the lead if the offer lands nowhere near their last sales price',
                                   'Ignore asking price completely and make the offer at market value '
                                   'anyway',
                                   'WE ARE LAND SPECIALISTS ([JRa_lwdSNjo @ 00:06:46]); Acrewell Land '
                                   'Company ([TbH_4hSsYHU @ 00:24:06])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ["Acrewell Land Company's Alex Reese documents how badly list prices mislead. "
                              'A 0.62-acre lot in Citrus Springs, Florida came to market at 75,000 and was '
                              'cut to 42,000 within three months, a 44 percent drop, while sitting at 119 '
                              'days on Zillow with 26 views, 18 saves and no buyer [TbH_4hSsYHU @ '
                              '00:01:13]. A Middleburg lot at 5309 Chickory Circle went from an 85,000 ask '
                              'to a 20,000 sale after two and a half years and three separate listings, '
                              'never drawing a buyer until the price fell below 28,000 [TbH_4hSsYHU @ '
                              '00:05:46]. The cause was physical: roughly 40 percent wetlands and flood '
                              'zone, with the remaining ground in Kinault peat, a very poorly drained soil '
                              'that may force an alternative septic system at much higher cost '
                              '[TbH_4hSsYHU @ 00:06:46]. For Land and Country hits the same wall on a '
                              '47.53-acre Lebanon, Tennessee listing, where the stream corridor is mapped '
                              'as floodway that cannot be built in at all, shrinking the usable building '
                              'envelope toward the road frontage and handing the buyer leverage to push '
                              'for a better price [7FfLOUMhyyA @ 00:04:11]. The trap is comping a lot by '
                              'acreage and address alone. Two parcels in the same subdivision at the same '
                              'size can sit tens of thousands apart once wet ground, drainage and '
                              'buildable area are measured.',
                              'Non-disclosure states are where comp math breaks first. Sumner Advanced '
                              'warns that the MLS in a state like Texas shows the last list price where a '
                              'sold property went under contract, not what it closed at, so reading a 149 '
                              'last list price as a 149 sale is the core mistake [8pB5HoHJ4Bk @ 00:00:52]. '
                              'Apke Brothers ran straight into this on a 70-acre Tate County, Mississippi '
                              'subdivide under contract at 135,000 plus a 5,000 survey: a nearby 9.4-acre '
                              'parcel listed in late 2023 probably closed around 35,000, which did not '
                              'make them feel good when they needed 40,000 to 50,000 per 10-acre lot to '
                              'double their money [bIqgihxHoo8 @ 00:04:41]. With too few comps to justify '
                              'the price, they called realtors and got a 50,000 to 70,000 opinion; eight '
                              'months in, four parcels averaged 62,000 for about 240,000 back on roughly '
                              '140,000, with three left listed at 50,000 to 65,000 to move fast '
                              '[bIqgihxHoo8 @ 00:06:27]. Sumner frames the cost of thin data as time: a '
                              'non-disclosure county might take two mail campaigns to get pricing right '
                              'versus one in a disclosure state, with offer feedback filling the gap '
                              '[8pB5HoHJ4Bk @ 00:06:22]. The economics check: when the only sold signal is '
                              'a guessed close below your per-parcel break-even, the deal rides on realtor '
                              'opinion until real sales land.',
                              'The rest of the firsthand mistakes are process errors. Brent Bowers locked '
                              'up a lot for 285 dollars with no idea how to comp it, got a 45-day estimate '
                              "of about 10,000 from a local realtor, then took that same realtor's 5,000 "
                              'offer and closed four days later, a fast win that still left roughly half '
                              "of the realtor's own retail estimate on the table [JNufnuENoDM @ 00:07:44]. "
                              'REtipster admits to scraping LandWatch without first restricting the search '
                              'to sold comps, which mixed asking prices into the output, and repeatedly '
                              'deletes outliers that would otherwise throw off the per-acre average '
                              '[rYCHQ59jzhY @ 00:13:34]. Cool Wholesaling+ Land Deals comped an 8-acre '
                              'Fairmont, North Carolina lot at 5,000 to 6,000 per acre, roughly 40,000 to '
                              '48,000 retail, and found the wholesale price at or above retail once ponds, '
                              'drainage and a zoning change back to residential were factored in, forcing '
                              'a 30,000 to 35,000 max [3x8J7AdyCEw @ 00:02:26]. WE ARE LAND SPECIALISTS '
                              'throws out a pocket comp because it was a waterfront lot with a boat slip, '
                              'a premium the subject cannot share [JRa_lwdSNjo @ 00:04:48]. Each error '
                              'points the same way: unscreened comps inflate retail, and inflated retail '
                              'erases the spread.'],
               'table': {'caption': 'Firsthand comp failures and the economics check each one forces',
                         'headers': ['Failure Mode', 'What Happened', 'Economics Check', 'Expert Source'],
                         'rows': [['Treating a vacant land asking price as market value',
                                   'Citrus Springs lot cut from 75,000 to 42,000 within its first three '
                                   'months',
                                   'Nearby sales at 45,000 and 49,000 showed the original ask was wishful '
                                   'thinking',
                                   'Acrewell Land Company ([TbH_4hSsYHU @ 00:01:13])'],
                                  ['Comping a wet, poorly drained lot as a clean building lot',
                                   'Chickory Circle lot fell from 85,000 to a 20,000 sale over two and a '
                                   'half years',
                                   'About 40 percent wetlands plus Kinault peat soil cut final price to '
                                   '23.5 percent of ask',
                                   'Acrewell Land Company ([TbH_4hSsYHU @ 00:06:46])'],
                                  ['Reading the last list price in a non-disclosure state as a sold price',
                                   'MLS shows the price where it went under contract, not the closing '
                                   'number',
                                   'Long days on market means a 149 last list price likely closed well '
                                   'below 149',
                                   'Sumner Advanced ([8pB5HoHJ4Bk @ 00:00:52])'],
                                  ['Underwriting a subdivide on thin non-disclosure Mississippi comps',
                                   'A 9.4-acre comp probably closed near 35,000 against a 40,000 to 50,000 '
                                   'per-lot target',
                                   'Realtor opinions of 50,000 to 70,000 carried the deal; four parcels '
                                   'averaged 62,000',
                                   'Apke Brothers ([bIqgihxHoo8 @ 00:04:41])'],
                                  ['Leaving landlocked and builder-premium lots in the comp sample',
                                   'A 6,500 landlocked sale and builder-priced subdivision lots at 175 '
                                   'were both thrown out',
                                   'Cleaned sample of rural lots put max retail on the subject around '
                                   '13,000',
                                   'Cool Wholesaling+ Land Deals-Real Estate Investing ([t8XDRE0ZjFc @ '
                                   '00:02:57])'],
                                  ['Mixing big tracts into small-parcel per-acre math',
                                   '37 acres for 144,000 and 50 acres for 139,000 ran only 3,000 to 4,000 '
                                   'per acre',
                                   'Price per acre shrinks as size grows, so those tracts cannot comp an '
                                   '8-acre lot',
                                   'Cool Wholesaling+ Land Deals-Real Estate Investing ([3x8J7AdyCEw @ '
                                   '00:01:22])'],
                                  ['Trusting a software per-acre figure over local sold comps',
                                   'Comp tool showed around 104,000 per acre for the five to eight acre '
                                   'range',
                                   'Actual sales ran 17,000 to 36,000 per acre, with local knowledge '
                                   'pointing near 50,000',
                                   'For Land and Country ([7FfLOUMhyyA @ 00:13:22])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Pre-Offer Comp Gate',
                           'body': 'Every item below comes from a deal where an operator either lost '
                                   'margin or nearly mispriced a parcel. Clear all four before a number '
                                   'goes into an offer letter or a purchase contract.',
                           'items': ['Pull wetlands, flood zone and soil layers before trusting any '
                                     'acreage comp; a lot about 40 percent wet with very poorly drained '
                                     'Kinault peat sold at 20,000 after an 85,000 ask [Acrewell Land '
                                     'Company — TbH_4hSsYHU @ 00:06:46].',
                                     'In non-disclosure states, discount last list prices by days on '
                                     'market and drop any listing that has been active longer than a year '
                                     'from the discount math [Sumner Advanced — 8pB5HoHJ4Bk @ 00:03:49].',
                                     'On any subdivide, call the county on minimum lot rules first; Tate '
                                     'County would only allow mobile homes on parcels of 10 acres or more '
                                     '[Apke Brothers — bIqgihxHoo8 @ 00:01:48].',
                                     'Delete outliers that do not line up with the rest of the sold list '
                                     'before averaging per-acre values, since one odd sale throws '
                                     'everything else off [REtipster — rYCHQ59jzhY @ 00:06:17].']}}],
 'pull_quote': '"Every successful land buyer has one thing in common, which is that they ignore asking '
               'price. They make their offer based on market value." Attributed to Acrewell Land Company '
               '(TbH_4hSsYHU @ 00:24:06).',
 'diagram_id': 'diag-05',
 'action_checklist': ['Filter Zillow to sold only, deselect every home type, reselect lots and land, and '
                      'match the HOA setting to the subject parcel [Brent Bowers — JNufnuENoDM @ '
                      '00:01:39].',
                      'Download Redfin sold land comps, divide lot square feet by 43,560 for acres, divide '
                      'price by acres, then run AVERAGE on the dollars-per-acre column [REtipster — '
                      'rYCHQ59jzhY @ 00:04:15].',
                      'Where Redfin shows no download button, install Instant Data Scraper, locate the '
                      'next button and crawl every results page into a CSV [REtipster — rYCHQ59jzhY @ '
                      '00:07:27].',
                      'Copy filtered LandWatch result pages into Price Boss, hit compute, and tag each '
                      'comp with its subdivision or city before analysis [LandSpeed Price Boss — '
                      'FOpRZxfMs4I @ 00:03:34].',
                      'Call the land specialist listed on LandWatch for the area and ask for the 30-day '
                      'blowout price, not the one-year number [Brent Bowers — JNufnuENoDM @ 00:09:15].',
                      'Check days on market, views and saves on active Zillow land listings to gauge '
                      'demand before committing to a county [REtipster — 9cX2NuhnYro @ 00:12:43].'],
 'statutory_citations': [{'title': 'Acrewell Land Company — Zillow Is Lying To You About Land Prices '
                                   '[00:03:07]',
                          'url': 'https://www.youtube.com/watch?v=TbH_4hSsYHU&t=187s',
                          'relevance': 'Primary practitioner testimony on asking prices running far above '
                                       'market value and sellers accepting deep discounts on vacant land.'},
                         {'title': 'REtipster — How to Use Redfin and LandWatch to Determine Land Values '
                                   '[00:04:15]',
                          'url': 'https://www.youtube.com/watch?v=rYCHQ59jzhY&t=255s',
                          'relevance': 'Primary practitioner testimony on converting Redfin sold exports '
                                       'into a dollars-per-acre average.'},
                         {'title': "Sumner Advanced — How I Price Land When Sold Prices Aren't Public "
                                   '[00:04:05]',
                          'url': 'https://www.youtube.com/watch?v=8pB5HoHJ4Bk&t=245s',
                          'relevance': 'Primary practitioner testimony on days-on-market discount rates '
                                       'for last list prices in non-disclosure states.'},
                         {'title': 'Apke Brothers — How To Make $250,000 in 2025 by Subdividing Land (Step '
                                   'by Step Guide) [00:06:07]',
                          'url': 'https://www.youtube.com/watch?v=bIqgihxHoo8&t=367s',
                          'relevance': 'Primary practitioner testimony on comping a 70-acre subdivide with '
                                       'thin non-disclosure data and realtor price opinions.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': '3x8J7AdyCEw',
                       'title': 'Zillow Land Comping: Master Acreage Pricing 🔑',
                       'channel': 'Cool Wholesaling+ Land Deals-Real Estate Investing',
                       'author': 'Cool Wholesaling+ Land Deals-Real Estate Investing',
                       'text': "We can't really compare 36 and 50 with 8 because the price per acre gets "
                               'smaller as you go up in size.',
                       'tip': "We can't really compare 36 and 50 with 8 because the price per acre gets "
                              'smaller as you go up in size.',
                       'timestamp': 82,
                       'timestamp_seconds': 82,
                       'timestamp_label': '[00:01:22]',
                       'url': 'https://www.youtube.com/watch?v=3x8J7AdyCEw&t=82s',
                       'markdown': '[00:01:22](https://www.youtube.com/watch?v=3x8J7AdyCEw&t=82s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'mM0tCRujCDM',
                       'title': 'Landwatch and Zillow Comps',
                       'channel': 'Jeff',
                       'author': 'Jeff',
                       'text': 'The terms price payment price is 297 down, 97 a month for 48 months, so '
                               'you multiply it out to find the actual terms price.',
                       'tip': 'The terms price payment price is 297 down, 97 a month for 48 months, so you '
                              'multiply it out to find the actual terms price.',
                       'timestamp': 112,
                       'timestamp_seconds': 112,
                       'timestamp_label': '[00:01:52]',
                       'url': 'https://www.youtube.com/watch?v=mM0tCRujCDM&t=112s',
                       'markdown': '[00:01:52](https://www.youtube.com/watch?v=mM0tCRujCDM&t=112s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'UqPvFZ6TGGo',
                       'title': 'How I Pull Comps on Zillow as Real Estate Investor (2025)',
                       'channel': 'DannyG Real Estate',
                       'author': 'DannyG Real Estate',
                       'text': 'Start as narrow as possible, only expand if you need to.',
                       'tip': 'Start as narrow as possible, only expand if you need to.',
                       'timestamp': 356,
                       'timestamp_seconds': 356,
                       'timestamp_label': '[00:05:56]',
                       'url': 'https://www.youtube.com/watch?v=UqPvFZ6TGGo&t=356s',
                       'markdown': '[00:05:56](https://www.youtube.com/watch?v=UqPvFZ6TGGo&t=356s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'FOpRZxfMs4I',
                       'title': 'Scraping LandWatch',
                       'channel': 'LandSpeed Price Boss',
                       'author': 'LandSpeed Price Boss',
                       'text': "If it's sold it's an actual comp; if it's for sale that means we might "
                               'want to make an adjustment when it does sell.',
                       'tip': "If it's sold it's an actual comp; if it's for sale that means we might want "
                              'to make an adjustment when it does sell.',
                       'timestamp': 214,
                       'timestamp_seconds': 214,
                       'timestamp_label': '[00:03:34]',
                       'url': 'https://www.youtube.com/watch?v=FOpRZxfMs4I&t=214s',
                       'markdown': '[00:03:34](https://www.youtube.com/watch?v=FOpRZxfMs4I&t=214s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 't8XDRE0ZjFc',
                       'title': 'How to use Zillow for comping vacant land ii- Determine the best price to '
                                'offer so you can profit',
                       'channel': 'Cool Wholesaling+ Land Deals-Real Estate Investing',
                       'author': 'Cool Wholesaling+ Land Deals-Real Estate Investing',
                       'text': "This one sold for 6,500 but it looks like it's landlocked behind the main "
                               "road, so that's probably not a good comp either.",
                       'tip': "This one sold for 6,500 but it looks like it's landlocked behind the main "
                              "road, so that's probably not a good comp either.",
                       'timestamp': 124,
                       'timestamp_seconds': 124,
                       'timestamp_label': '[00:02:04]',
                       'url': 'https://www.youtube.com/watch?v=t8XDRE0ZjFc&t=124s',
                       'markdown': '[00:02:04](https://www.youtube.com/watch?v=t8XDRE0ZjFc&t=124s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'JNufnuENoDM',
                       'title': 'How To Find Comps For Land',
                       'channel': 'Brent Bowers',
                       'author': 'Brent Bowers',
                       'text': "I'm wondering what the 30-day blowout price is; I want the get it done "
                               'number, not the pie in the sky one year from now number.',
                       'tip': "I'm wondering what the 30-day blowout price is; I want the get it done "
                              'number, not the pie in the sky one year from now number.',
                       'timestamp': 555,
                       'timestamp_seconds': 555,
                       'timestamp_label': '[00:09:15]',
                       'url': 'https://www.youtube.com/watch?v=JNufnuENoDM&t=555s',
                       'markdown': '[00:09:15](https://www.youtube.com/watch?v=JNufnuENoDM&t=555s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'JRa_lwdSNjo',
                       'title': 'HOW TO RUN VACANT LAND COMPS USING ZILLOW | LAND SPECIALIST',
                       'channel': 'WE ARE LAND SPECIALISTS',
                       'author': 'WE ARE LAND SPECIALISTS',
                       'text': 'Typically if I cannot get them nowhere near their last sales price I run; '
                               "it's a waste of time.",
                       'tip': 'Typically if I cannot get them nowhere near their last sales price I run; '
                              "it's a waste of time.",
                       'timestamp': 406,
                       'timestamp_seconds': 406,
                       'timestamp_label': '[00:06:46]',
                       'url': 'https://www.youtube.com/watch?v=JRa_lwdSNjo&t=406s',
                       'markdown': '[00:06:46](https://www.youtube.com/watch?v=JRa_lwdSNjo&t=406s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'QB6c4nBfXrs',
                       'title': 'How to Find Land Deals (LandWatch, LandSearch & Hidden Sources) '
                                '#realestate',
                       'channel': 'Once Upon a Brick · The Land Investor',
                       'author': 'Once Upon a Brick · The Land Investor',
                       'text': "This does not mean you can purchase the land for $200 for 20 acres; that's "
                               'most likely your monthly payment.',
                       'tip': "This does not mean you can purchase the land for $200 for 20 acres; that's "
                              'most likely your monthly payment.',
                       'timestamp': 419,
                       'timestamp_seconds': 419,
                       'timestamp_label': '[00:06:59]',
                       'url': 'https://www.youtube.com/watch?v=QB6c4nBfXrs&t=419s',
                       'markdown': '[00:06:59](https://www.youtube.com/watch?v=QB6c4nBfXrs&t=419s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'rYCHQ59jzhY',
                       'title': 'How to Use Redfin and LandWatch to Determine Land Values',
                       'channel': 'REtipster',
                       'author': 'REtipster',
                       'text': 'I would probably want to factor in some kind of discount by maybe 20% or '
                               "30%, because just because these are listed at these numbers doesn't mean "
                               "they're actually going to sell at these numbers.",
                       'tip': 'I would probably want to factor in some kind of discount by maybe 20% or '
                              "30%, because just because these are listed at these numbers doesn't mean "
                              "they're actually going to sell at these numbers.",
                       'timestamp': 162,
                       'timestamp_seconds': 162,
                       'timestamp_label': '[00:02:42]',
                       'url': 'https://www.youtube.com/watch?v=rYCHQ59jzhY&t=162s',
                       'markdown': '[00:02:42](https://www.youtube.com/watch?v=rYCHQ59jzhY&t=162s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '7FfLOUMhyyA',
                       'title': 'This Zillow Property Looks PERFECT for a Family Compound… But Is It?',
                       'channel': 'For Land and Country',
                       'author': 'For Land and Country',
                       'text': "If you click on it, it will say subtype floodway, which means you can't "
                               'build in it.',
                       'tip': "If you click on it, it will say subtype floodway, which means you can't "
                              'build in it.',
                       'timestamp': 251,
                       'timestamp_seconds': 251,
                       'timestamp_label': '[00:04:11]',
                       'url': 'https://www.youtube.com/watch?v=7FfLOUMhyyA&t=251s',
                       'markdown': '[00:04:11](https://www.youtube.com/watch?v=7FfLOUMhyyA&t=251s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Tmf12E9Dg7A',
                       'title': "The $10,000 Land Trap: Don't Overpay #landinvesting #realestate",
                       'channel': 'Once Upon a Brick · The Land Investor',
                       'author': 'Once Upon a Brick · The Land Investor',
                       'text': 'Not every two acres is the same; is your two acres flat or is it sloping, '
                               'is it in a wetland, how is the access.',
                       'tip': 'Not every two acres is the same; is your two acres flat or is it sloping, '
                              'is it in a wetland, how is the access.',
                       'timestamp': 375,
                       'timestamp_seconds': 375,
                       'timestamp_label': '[00:06:15]',
                       'url': 'https://www.youtube.com/watch?v=Tmf12E9Dg7A&t=375s',
                       'markdown': '[00:06:15](https://www.youtube.com/watch?v=Tmf12E9Dg7A&t=375s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '9cX2NuhnYro',
                       'title': 'How to Find Land Values and Market Insights with Zillow',
                       'channel': 'REtipster',
                       'author': 'REtipster',
                       'text': 'The smaller a property gets, the higher the price or the value or the sale '
                               'price is going to be on a per acre basis.',
                       'tip': 'The smaller a property gets, the higher the price or the value or the sale '
                              'price is going to be on a per acre basis.',
                       'timestamp': 579,
                       'timestamp_seconds': 579,
                       'timestamp_label': '[00:09:39]',
                       'url': 'https://www.youtube.com/watch?v=9cX2NuhnYro&t=579s',
                       'markdown': '[00:09:39](https://www.youtube.com/watch?v=9cX2NuhnYro&t=579s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'TbH_4hSsYHU',
                       'title': 'Zillow Is Lying To You About Land Prices',
                       'channel': 'Acrewell Land Company',
                       'author': 'Acrewell Land Company',
                       'text': 'For vacant land, asking price is not a reliable indicator of market value '
                               'at all.',
                       'tip': 'For vacant land, asking price is not a reliable indicator of market value '
                              'at all.',
                       'timestamp': 187,
                       'timestamp_seconds': 187,
                       'timestamp_label': '[00:03:07]',
                       'url': 'https://www.youtube.com/watch?v=TbH_4hSsYHU&t=187s',
                       'markdown': '[00:03:07](https://www.youtube.com/watch?v=TbH_4hSsYHU&t=187s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'TbH_4hSsYHU',
                       'title': 'Zillow Is Lying To You About Land Prices',
                       'channel': 'Acrewell Land Company',
                       'author': 'Acrewell Land Company',
                       'text': 'The wetlands maps, like the county soil maps, can be misleading and '
                               "inaccurate, so you want the soil scientist to do what's called a wetlands "
                               'delineation.',
                       'tip': 'The wetlands maps, like the county soil maps, can be misleading and '
                              "inaccurate, so you want the soil scientist to do what's called a wetlands "
                              'delineation.',
                       'timestamp': 1002,
                       'timestamp_seconds': 1002,
                       'timestamp_label': '[00:16:42]',
                       'url': 'https://www.youtube.com/watch?v=TbH_4hSsYHU&t=1002s',
                       'markdown': '[00:16:42](https://www.youtube.com/watch?v=TbH_4hSsYHU&t=1002s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '8pB5HoHJ4Bk',
                       'title': "How I Price Land When Sold Prices Aren't Public",
                       'channel': 'Sumner Advanced',
                       'author': 'Sumner Advanced',
                       'text': "It's going to show you the last list price where it actually went under "
                               "contract at, but that does not mean that's what it sold at.",
                       'tip': "It's going to show you the last list price where it actually went under "
                              "contract at, but that does not mean that's what it sold at.",
                       'timestamp': 52,
                       'timestamp_seconds': 52,
                       'timestamp_label': '[00:00:52]',
                       'url': 'https://www.youtube.com/watch?v=8pB5HoHJ4Bk&t=52s',
                       'markdown': '[00:00:52](https://www.youtube.com/watch?v=8pB5HoHJ4Bk&t=52s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'E9KBudZB1Do',
                       'title': 'How to Find the Best Counties for Land Investing with Zillow',
                       'channel': 'REtipster',
                       'author': 'REtipster',
                       'text': "That's typically what we want, a rural area that's within like a one to "
                               'two, maybe three hour drive from the nearest big city.',
                       'tip': "That's typically what we want, a rural area that's within like a one to "
                              'two, maybe three hour drive from the nearest big city.',
                       'timestamp': 241,
                       'timestamp_seconds': 241,
                       'timestamp_label': '[00:04:01]',
                       'url': 'https://www.youtube.com/watch?v=E9KBudZB1Do&t=241s',
                       'markdown': '[00:04:01](https://www.youtube.com/watch?v=E9KBudZB1Do&t=241s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'bIqgihxHoo8',
                       'title': 'How To Make $250,000 in 2025 by Subdividing Land (Step by Step Guide)',
                       'channel': 'Apke Brothers',
                       'author': 'Apke Brothers',
                       'text': 'You need to understand how to comp out land or you can lose money, and '
                               'there is a lot more risk involved in it.',
                       'tip': 'You need to understand how to comp out land or you can lose money, and '
                              'there is a lot more risk involved in it.',
                       'timestamp': 403,
                       'timestamp_seconds': 403,
                       'timestamp_label': '[00:06:43]',
                       'url': 'https://www.youtube.com/watch?v=bIqgihxHoo8&t=403s',
                       'markdown': '[00:06:43](https://www.youtube.com/watch?v=bIqgihxHoo8&t=403s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'}]}
