from __future__ import annotations

CHAPTER_4 = {'id': 'Q4',
 'chapter_id': 'Q4',
 'chapter_number': 4,
 'question_number': 4,
 'slug': 'vol018-q04-data-tools-and-list-building',
 'question_prompt': 'Where do I get landowner data, and how do I build and filter the right list before I '
                    'market?',
 'kicker': 'Q4 / THE BIG MONEY PLAYBOOKS',
 'title': 'Data Tools and List Building',
 'subtitle': 'DataTree, TitlePro, and RealQuest Pro compared, parcel tagging, PRYCD process flow, list '
             'upload, and out-of-county owner maps, PropStream for land, county GIS and parcel viewers, '
             'public-record data basics, SiteFact reports, and pulling tax-delinquent and off-market lists',
 'layout_template': 'comparison_matrix',
 'reading_time_minutes': 15,
 'executive_summary': 'Land and wholesale operators converge on one rule: build the list by stacking cheap '
                      'public-record filters until only unlisted, long-held, absentee owners remain, then '
                      'price and verify every parcel before a dollar goes to mail. DataTree, PropStream, '
                      'RealQuest, TitlePro, PRYCD and free county GIS all draw on the same county tax-roll '
                      'backbone keyed to the APN. The street mechanics are numeric. Setting improvement '
                      'value to zero isolates raw land. DataTree records run 10 cents each, and PRYCD '
                      'priced 300 records for $24. PropStream cut 82,328 Lehigh Acres lots to 1,250, and '
                      'vacant-land mail pulls 2-5% response at $0.79 a piece. Operators split on equity '
                      'filters (none to 99%), hold periods (2 to 10-plus years), RealQuest versus '
                      'DataTree, texting versus mail, and whether niche lists are too small to work.',
 'key_metrics': [{'label': 'Vacant Land Direct Mail Response Rate',
                  'metric': 'Vacant Land Direct Mail Response Rate',
                  'value': '2-5% for vacant land versus 0.5-1% for residential, commercial and multifamily',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Matt reports these response rates from hundreds of deals sourced through '
                             'direct mail alone, so 2,000 letters at 1% equals 20 owners.',
                  'source': 'MS Partners LLC ([hemWETr8VGg @ 00:00:34])'},
                 {'label': 'DataTree Per-Record Export Cost',
                  'metric': 'DataTree Per-Record Export Cost',
                  'value': '$0.10 per record with membership',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Ron pays this rate for Boulder County raw-land exports, and removing '
                             'duplicate owners lowers the charge.',
                  'source': 'Apke Brothers ([tZnXE47jWp4 @ 00:06:34])'},
                 {'label': 'PRYCD Priced-List Cost',
                  'metric': 'PRYCD Priced-List Cost',
                  'value': '300 records for $24',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Max Edson's analysis-page purchase includes the offer price at a 25% default "
                             'slider, with counter-offer increments from 5-95%.',
                  'source': 'PRYCD ([7jGQIvwqBwc @ 00:20:36])'},
                 {'label': 'Cold Call Lead-to-Deal KPI',
                  'metric': 'Cold Call Lead-to-Deal KPI',
                  'value': '1,000 calls = about 1 lead; 30 leads = about 1 deal',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Dier uses this ratio to justify pulling 10,000 records and calling each '
                             'three times on a 14-line dialer.',
                  'source': 'Maximilian Dier ([KmEcpx-t8YM @ 00:01:55])'}],
 'sections': [{'section_number': 1,
               'heading': 'The Practitioner Consensus',
               'paragraphs': ['Every paid list tool in this chapter is a front end on the same raw '
                              'material: the county tax roll. DataTree by First American lays out the '
                              'backbone. Each of 3,144 counties produces a tax roll, and the APN works '
                              'like a Social Security number for the parcel. It carries land use, zoning, '
                              'acreage, frontage and depth, utilities, ownership, vesting, five types of '
                              'value, and tax fields down to the delinquent year [EmWzMGDpkTY @ 00:01:13]. '
                              'Stephen Jack Butala and Jill DeWit of Land Academy, licensed on DataTree, '
                              'TitlePro and RealQuest Pro, say all three serve the same purpose and now '
                              'all deliver decades of deeds and mortgages [CbpqiGq5E5Y @ 00:09:33]. That '
                              'is why the free layer matters too. Luke Harris of The Farm Finders, '
                              'featured by Country Land Sellers, searches county GIS by tax account number '
                              "for tax history, balance and boundary coordinates. To find any county's "
                              'map, Harris Googles the county, state and GIS, then tries portal, tax lot '
                              'finder or zoning map [6qNh515jvww @ 00:06:16]. Joséphine Saffert works the '
                              "same way on Metro Nashville's parcel viewer. Saffert searches by address or "
                              'owner, then reads frontage, overlays, floodplain and contours before a deal '
                              'moves [_kxaCpUojPw @ 00:00:42]. The consensus is that paid tools buy speed, '
                              'bulk export and mapping, not a different underlying truth about the parcel '
                              'or its owner.',
                              'The second point of agreement is the target owner. Across land and house '
                              'lists, operators strip out anything listed, anything corporate and anyone '
                              "who bought recently, then lean into distance and tenure. Great Lands LLC's "
                              'PropStream walk-through insists on unlisted property. It then filters for '
                              'individual owners who have held at least 10 years, people who have owned '
                              'land a long time and are tired of it, followed by out-of-state absentee '
                              'owners [Mdkx15sX_XM @ 00:05:19]. Max Edson of PRYCD builds a whole '
                              'county-level map on the same theory. Out-of-county owner records are '
                              'divided by total county parcels, because distant owners sell more readily, '
                              'and the map is filtered to counties at 40% or higher [mhHvzO1O8To @ '
                              '00:00:52]. On the house side, Lauren Hardy of The Well Entrepreneur drops '
                              'owner-occupants because they ride it out. Hardy keeps individuals and '
                              'trusts only, the mom and pops, and cuts LLCs [p_LcZVcrC3U @ 00:04:31]. '
                              "Maximilian Dier's core Dallas pull is single-family, absentee, individual "
                              "owner, seven-plus years owned, 30% equity and built 2010 or earlier. Dier's "
                              'reasoning is that absentee owners are inherited, out-of-state or tired '
                              'landlords [KmEcpx-t8YM @ 00:00:41]. The filters differ in degree, but the '
                              'profile is the same: an owner who is far away, has held for years, and is '
                              'not already working with an agent or listing the parcel.',
                              'The third consensus is that list building is a numbers game backed by hard '
                              'verification. Matt of MS Partners LLC reports hundreds of deals from direct '
                              'mail alone. Matt puts residential, commercial and multifamily response at '
                              '0.5-1% and vacant land at 2-5%, so 2,000 letters at 1% yields 20 owners. '
                              'The secret is consistency: do not quit after 200 letters [hemWETr8VGg @ '
                              '00:01:14]. Maximilian Dier runs the same math on phones. Usually 1,000 '
                              'calls produce one lead and 30 leads produce one deal, so the play is to '
                              'pull 10,000 records, call each three times, and treat skip-trace quality as '
                              'critical [KmEcpx-t8YM @ 00:01:55]. Volume only pays if the parcel survives '
                              'scrutiny. Don Healy, speaking with Seth on the REtipster podcast, frames '
                              'land as a war of due diligence. Whatever the end buyer will find that could '
                              'trip the deal, the investor wants to know first [IS6mrT0hkGw @ 00:09:56]. '
                              "Healy's two always-check items are zoning for intended use and soils plus "
                              'slope. On zoning, Healy points to EFU land carrying an 80-acre minimum lot '
                              'size [IS6mrT0hkGw @ 00:34:49]. Healy adds that a confirmed no is almost as '
                              'valuable as a yes, because it kills a bad offer before money moves and '
                              'before a buyer discovers the problem [IS6mrT0hkGw @ 00:33:41].'],
               'table': {'caption': 'Where the list-building practitioners agree',
                         'headers': ['Consensus Point',
                                     'What Practitioners Actually Do',
                                     'Why It Matters To The Operator',
                                     'Expert Source'],
                         'rows': [['All list tools sit on county tax rolls',
                                   'Pull APN-keyed records covering land use, zoning, acreage, ownership '
                                   'and delinquent tax year',
                                   'Every paid platform resells the same 3,144-county public record '
                                   'backbone',
                                   'DataTree by First American ([EmWzMGDpkTY @ 00:01:13])'],
                                  ['DataTree, TitlePro and RealQuest serve one purpose',
                                   'Licensed providers use all three to pull deeds, mortgages and owner '
                                   'data',
                                   'Tool choice comes down to format and features, not unique data access',
                                   'Land Academy ([CbpqiGq5E5Y @ 00:09:33])'],
                                  ['Raw land means zero assessed improvement value',
                                   'Set assessed improvement value to zero after the acreage filter is '
                                   'applied',
                                   'The Boulder County 5-5.5 acre pull dropped from 714 results to 309',
                                   'Apke Brothers ([tZnXE47jWp4 @ 00:02:39])'],
                                  ['Target unlisted, long-held, out-of-state individual owners first',
                                   'Filter off-market, individual owners holding ten years, then '
                                   'out-of-state absentee owners',
                                   'Owners who have held land a long time are tired of it',
                                   'Great Lands LLC ([Mdkx15sX_XM @ 00:05:19])'],
                                  ['Owner distance from the parcel predicts willingness to sell',
                                   'Map out-of-county owners divided by total parcels and keep counties at '
                                   '40%+',
                                   'Darker counties on the map carry more absentee owners worth mailing',
                                   'PRYCD ([mhHvzO1O8To @ 00:00:52])'],
                                  ['Free county GIS verifies every parcel before an offer',
                                   'Search by tax account number, then check tax balance, boundaries, '
                                   'neighbors and road access',
                                   'One parcel that looked fine on paper lacked real road access on '
                                   'aerials',
                                   'Country Land Sellers ([6qNh515jvww @ 00:03:48])'],
                                  ['Consistency beats any single campaign result in direct mail',
                                   'Mail repeatedly to the same list and do not quit after 200 letters',
                                   'Vacant land mail returns 2-5% while residential returns only 0.5-1%',
                                   'MS Partners LLC ([hemWETr8VGg @ 00:00:34])']]}},
              {'section_number': 2,
               'heading': 'Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ["The Apke Brothers' DataTree demo runs Boulder County, Colorado. A lot "
                              'acreage filter of 5 to 5.5 returns 714 results, including houses. Setting '
                              'assessed improvement value to zero strips that to 309 raw-land parcels '
                              '[tZnXE47jWp4 @ 00:02:39]. Under 1,000 results, the set displays on the map '
                              'with parcel, terrain, owner-name and APN layers. MLS recently-sold and '
                              'for-sale neighbors also show, including one listed at $1.4 million '
                              '[tZnXE47jWp4 @ 00:03:18]. Records cost 10 cents each with membership. '
                              'Removing duplicate owners lowers the charge, though the deduped count is '
                              'not shown before you pay [tZnXE47jWp4 @ 00:07:14]. Land Academy credits '
                              'DataTree with mapping and book-and-page documents on top of the core record '
                              'pull [CbpqiGq5E5Y @ 00:10:39]. For narrow, hand-picked targets, Seth of '
                              'REtipster skips Advanced Search and uses parcel tagging. The sequence is '
                              'More Map, the pencil icon, Freehand, mark each parcel, then Apply, Less Map '
                              "and Export [oJpqcR4iFy8 @ 00:01:48]. Seth's example was 5-plus-acre "
                              'self-storage sites in Millington, Michigan. Seth is willing to offer high '
                              'there because the plan is to entitle or rezone. A small town produces 20 to '
                              '40 properties, which then get skip traced for texting or calling '
                              '[oJpqcR4iFy8 @ 00:03:29]. The same tagging works for lakes, mountainsides '
                              'or specific roads [oJpqcR4iFy8 @ 00:04:47].',
                              "PRYCD turns the pull into a priced offer file. Max Edson's process starts "
                              'on the research page, which holds 1M-plus comps from Zillow, LandWatch, '
                              'Lands of America and LandFlip. Counties are ranked by sold-to-for-sale '
                              'ratio and parcels-on-market. In Colorado, filtering to population under 20 '
                              'per square mile and parcels-on-market under .05 left six counties '
                              "[7jGQIvwqBwc @ 00:05:19]. On the search page, Costilla County's 39,785 "
                              'records get a 20-100 acre range, with the top typed as 100.01 to avoid '
                              'rounding to 99.99. Residential codes require improvement value of zero. '
                              'Corporate and do-not-mail owners are excluded, and flood codes and active '
                              'or pending listings are dropped. The result is 1,930 records [7jGQIvwqBwc @ '
                              '00:12:32]. The offer slider defaults to 25% and can be overridden manually, '
                              'and 300 records cost $24. The raw file carries 240-plus columns, and scrub '
                              'filters remove on average 0.5% churches and 4.4% government owners. Five '
                              'files then arrive, and the scrub file is the one that gets mailed '
                              '[7jGQIvwqBwc @ 00:20:36]. Outside lists plug in too. Edson uploaded 1,359 '
                              'records, smart-tagged county, state and acreage, and changed the default '
                              '30% discount to 25%. The output added five columns feeding a blind-offer '
                              'letter, plus a Google Earth KML of owners and comps [3kN1hBRUqVU @ '
                              '00:02:51].',
                              'PropStream is the house tool that land operators bend to fit. Great Lands '
                              'LLC ran a Lehigh Acres, Florida funnel in steps. Residential vacant land '
                              'returned 82,328 records, and not on market left about 80,000. Individual '
                              'owners holding 10-plus years left about 44,000, and out-of-state absentee '
                              'owners about 20,000. Assessed value at or under $5,000 cut it to 17,000, '
                              '99% equity to 16,000, and last sale at or under $5,000 to 1,250 '
                              '[Mdkx15sX_XM @ 00:10:07]. Comps get narrowed to a quarter mile with houses '
                              'removed. The offer rule is double your money: a lot bought for $3,000 in '
                              '2004 gets a $1,500 offer, $2,000 max, and deed documents cost $5 '
                              "[Mdkx15sX_XM @ 00:12:48]. Lauren Hardy cut Albuquerque's 12,000 "
                              "tax-delinquent records to a 565-record final list. Hardy's plan is 10,000 "
                              'records a month for $99, then export to BatchLeads [p_LcZVcrC3U @ '
                              '00:06:30]. Zach Ginn, with 1,000-plus wholesale deals, gets the '
                              'tax-delinquent list free from the county clerk, appraiser or assessor. Ginn '
                              'files a FOIA request if refused and asks for Excel to dodge page fees. '
                              'TruePeopleSearch is the free skip-trace option [3VKazhO11yk @ 00:04:37]. '
                              'For delivery, Matt pays Land of Enchantment Direct Mail $0.79 per piece, '
                              'including letter, envelope and postage [hemWETr8VGg @ 00:01:50].'],
               'table': {'caption': 'Exact filters, settings and costs reported on the street',
                         'headers': ['Tool Or Step',
                                     'Exact Setting Or Number',
                                     'Operator Result Reported',
                                     'Expert Source'],
                         'rows': [['DataTree raw-land acreage filter in Boulder County',
                                   'Lot acreage 5 to 5.5 plus improvement value set to zero',
                                   '714 mixed results cut to 309 raw-land parcels on the map',
                                   'Apke Brothers ([tZnXE47jWp4 @ 00:02:39])'],
                                  ['DataTree parcel tagging for hand-picked small-town lists',
                                   'More Map, pencil, Freehand, mark parcels, Apply, Less Map, Export',
                                   '20 to 40 properties per small town, then skip traced',
                                   'REtipster ([oJpqcR4iFy8 @ 00:04:00])'],
                                  ['PRYCD county search with acreage and exclusion filters',
                                   '20 to 100.01 acres with corporate, do-not-mail, flood and listed '
                                   'parcels excluded',
                                   "Costilla County's 39,785 records reduced to 1,930 mailable records",
                                   'PRYCD ([7jGQIvwqBwc @ 00:12:32])'],
                                  ['PRYCD analysis pricing and scrub before mailing the file',
                                   'Offer slider at 25 percent, with 300 records priced for $24',
                                   'Scrub removes roughly 0.5% churches and 4.4% government owners',
                                   'PRYCD ([7jGQIvwqBwc @ 00:23:01])'],
                                  ['PropStream vacant land funnel in Lehigh Acres, Florida',
                                   'Unlisted, individual, 10+ years, out-of-state, with assessed value and '
                                   'last sale under $5,000',
                                   '82,328 vacant lots narrowed to 1,250 targeted owner records',
                                   'Great Lands LLC ([Mdkx15sX_XM @ 00:10:07])'],
                                  ['Free county tax-delinquent list requested from county staff',
                                   'Private citizen research line, FOIA if refused, and an Excel copy '
                                   'requested',
                                   'Free digital list instead of paying per-page printing fees',
                                   'Zach Ginn ([3VKazhO11yk @ 00:04:37])'],
                                  ['Direct mail fulfillment cost per vacant land piece',
                                   '$0.79 including letter, envelope and postage via Land of Enchantment',
                                   'Vacant land mail pulls 2-5% response versus 0.5-1% for residential',
                                   'MS Partners LLC ([hemWETr8VGg @ 00:01:50])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Small settings that change list quality and cost',
                           'body': 'These are the keystroke-level moves practitioners use to keep records '
                                   'clean and spend down before the first letter drops.',
                           'items': ['Type 100.01 rather than 100 as the top of an acreage range so the '
                                     'filter does not round to 99.99 and drop parcels [PRYCD — 7jGQIvwqBwc '
                                     '@ 00:07:50].',
                                     'Dedupe owners on DataTree before buying to lower the per-record '
                                     'charge, knowing the deduped count is not shown in advance [Apke '
                                     'Brothers — tZnXE47jWp4 @ 00:07:14].',
                                     'When a county clerk resists, say you are a private tax-paying '
                                     'citizen doing private independent research, and request the file in '
                                     'Excel [Zach Ginn — 3VKazhO11yk @ 00:04:24].',
                                     "Skip PropStream's improvement-value and estimated-value filters on "
                                     'land pulls, because Great Lands found them poorly populated or '
                                     'broken [Great Lands LLC — Mdkx15sX_XM @ 00:08:52].']},
               'sop_steps': [{'step': 1,
                              'title': 'Pick the county',
                              'action': 'Screen counties by absentee ratio and market velocity before '
                                        'pulling a single record.',
                              'detail': 'Use the out-of-county owner ratio map and keep counties at 40% or '
                                        'higher [PRYCD — mhHvzO1O8To @ 00:00:52]. Then filter the research '
                                        'page to population under 20 per square mile and parcels-on-market '
                                        'under .05, which left six Colorado counties [PRYCD — 7jGQIvwqBwc '
                                        '@ 00:05:19].'},
                             {'step': 2,
                              'title': 'Pull raw land owners',
                              'action': 'Stack acreage, zero improvement value, unlisted status, tenure '
                                        'and absentee filters.',
                              'detail': 'Set acreage, then set improvement value to zero to isolate raw '
                                        'land, as Boulder County went from 714 to 309 [Apke Brothers — '
                                        'tZnXE47jWp4 @ 00:02:39]. Then require unlisted, individual owners '
                                        'holding 10+ years and out-of-state, as in Lehigh Acres going from '
                                        '82,328 to 1,250 [Great Lands LLC — Mdkx15sX_XM @ 00:10:07].'},
                             {'step': 3,
                              'title': 'Price the list',
                              'action': 'Upload the export, map county, state and acreage, and set the '
                                        'discount.',
                              'detail': 'Upload any DataTree, RealQuest Pro or assessor list and change '
                                        'the default 30% discount to 25%. This appends market price, '
                                        'market price per acre, offer price, offer price per acre and '
                                        'source columns for a blind-offer letter [PRYCD — 3kN1hBRUqVU @ '
                                        '00:01:50].'},
                             {'step': 4,
                              'title': 'Verify and mail',
                              'action': 'Check GIS access and tax balance, then mail consistently at a '
                                        'known per-piece cost.',
                              'detail': 'Confirm tax balance, boundaries and real road access on county '
                                        'GIS aerials and Street View [Country Land Sellers — 6qNh515jvww @ '
                                        '00:03:48]. Then mail at $0.79 per piece and keep mailing past the '
                                        'first 200 letters [MS Partners LLC — hemWETr8VGg @ 00:01:14].'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ["Land Academy's Jill DeWit and Stephen Jack Butala hold licenses for "
                              'DataTree, TitlePro, and RealQuest, and they still split on which one '
                              "belongs in a land operator's stack. Jack rarely touches RealQuest and calls "
                              'DataTree the 21st century answer to pulling land and house data and then '
                              'visually seeing it. Jill calls RealQuest best for land because its export '
                              'format stays consistent, while DataTree columns shift county by county and '
                              'break a multi-county mailer merge [CbpqiGq5E5Y @ 00:11:10]. The Apke '
                              "Brothers lean into DataTree's map side: once a raw-land search drops below "
                              '1,000 results, the whole list plots on the map with parcel, terrain, '
                              'owner-name, and APN layers stacked on top [tZnXE47jWp4 @ 00:03:18]. Great '
                              'Lands LLC runs land through PropStream instead, conceding the platform is '
                              'specialized in houses but arguing that the land data and built-in comps '
                              "carry the workflow [Mdkx15sX_XM @ 00:01:45]. PRYCD's Max Edson sidesteps "
                              'the platform fight entirely: pull a list from DataTree, RealQuest Pro, or a '
                              'county assessor file, then upload it so PRYCD appends market price, offer '
                              'price, and a campaign map regardless of where the records came from '
                              '[3kN1hBRUqVU @ 00:00:14]. The real split is format consistency versus '
                              'visual mapping versus pricing layered on top of any source.',
                              'Filter depth is where the list builders openly contradict each other. '
                              'Maximilian Dier stacks absentee, individual owner, seven-plus years owned, '
                              'and equity, calling 30% the magic number and reasoning that people sell '
                              'every 7 to 10 years [KmEcpx-t8YM @ 00:04:58]. Great Lands LLC goes far '
                              'harder on land in Lehigh Acres: individual owners holding at least 10 years '
                              'to reach people tired of the lot, then 99% equity, then last sale at or '
                              'under $5,000, shrinking 82,328 residential vacant parcels down to 1,250 '
                              '[Mdkx15sX_XM @ 00:10:07]. Lauren Hardy refuses the equity filter outright '
                              'because it is often wrong, sets ownership at four years, keeps individuals '
                              'and trusts only to reach the mom and pops, and warns that stacking vacant '
                              'on top of tax delinquent collapses Albuquerque to 269 records [p_LcZVcrC3U '
                              '@ 00:02:04]. Ryan Dossey runs the loosest version for agents: equity of '
                              'only 10 to 15% versus the 35 to 100% investors use, ownership of just two '
                              'years, and a trust-owned filter that landed 3,361 West Jordan homes before '
                              "trimming to roughly 300 actually mailed [1VVAkFWqVKE @ 00:02:42]. Hardy's "
                              'tiebreaker is blunt: when in doubt, a bigger list beats a smaller list, '
                              'because over-stacking makes the list tiny.',
                              'The outreach channel and list size arguments run in parallel. Zach Ginn '
                              'works tax-delinquent lists by call, text, and mail but gives texting a '
                              'slight edge over cold calling, and the script never mentions the taxes, '
                              'leading instead with the me-and-my-partner-are-buying-in-the-area line '
                              '[3VKazhO11yk @ 00:06:41]. Matt at MS Partners LLC built hundreds of deals '
                              'on direct mail alone, quoting 0.5 to 1% response on residential, '
                              'commercial, and multifamily versus 2 to 5% on vacant land, and pointing to '
                              'the physical piece that some owners hold onto and call about a year later '
                              '[hemWETr8VGg @ 00:00:34]. Dier pushes pure volume from the other direction: '
                              'niche lists like 11 zombie properties or 608 tax delinquent records are too '
                              'small to feed a dialer, so pull 10,000 records and call each one three '
                              "times [KmEcpx-t8YM @ 00:01:39]. REtipster's Seth runs the opposite play, "
                              'skipping Advanced Search and freehand-tagging 20 to 40 parcels in a small '
                              'Michigan town for 5-plus acre self-storage sites, willing to offer high '
                              'because the exit is entitlement or rezoning [oJpqcR4iFy8 @ 00:02:47]. '
                              'Volume callers need thousands of dials; hand-taggers need conviction on a '
                              'handful of parcels, then a skip trace to text or call each owner directly.'],
               'table': {'caption': 'Competing list-building playbooks reported by land and wholesale '
                                    'practitioners',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Which data platform should feed a multi-county land mailer',
                                   'Jill DeWit picks RealQuest because its export format stays consistent '
                                   'across counties',
                                   'DataTree adds mapping and book and page documents, but its columns '
                                   'vary by county',
                                   'Land Academy ([CbpqiGq5E5Y @ 00:11:10])'],
                                  ['How narrow the target box should be for niche exits',
                                   'Seth freehand-tags 20 to 40 parcels in one small town for self-storage '
                                   'sites',
                                   'Advanced Search filters pull broad county lists when the target box is '
                                   'not that narrow',
                                   'REtipster ([oJpqcR4iFy8 @ 00:00:23])'],
                                  ['Whether to stack an equity filter on the list at all',
                                   'Maximilian Dier requires at least 30% equity and calls it the magic '
                                   'number',
                                   'Lauren Hardy skips the equity filter entirely because the field is '
                                   'often wrong',
                                   'Maximilian Dier ([KmEcpx-t8YM @ 00:04:58])'],
                                  ['Minimum years of ownership before an owner gets marketed',
                                   'Great Lands LLC sets at least 10 years to reach owners tired of their '
                                   'land',
                                   'Ryan Dossey uses only two years owned on an agent listing mail '
                                   'campaign',
                                   'Great Lands LLC ([Mdkx15sX_XM @ 00:05:19])'],
                                  ['Primary outreach channel for a fresh distressed owner list',
                                   'Zach Ginn gives texting a slight edge over cold calling tax-delinquent '
                                   'owners',
                                   'Matt at MS Partners LLC reports 2 to 5% direct mail response on vacant '
                                   'land',
                                   'Zach Ginn ([3VKazhO11yk @ 00:06:41])'],
                                  ['How deep to discount the blind offer price on each parcel',
                                   'PRYCD analysis slider defaults to 25% with a manual override to exact '
                                   'figures',
                                   'Great Lands LLC doubles its money, offering $1,500 with a $2,000 '
                                   'maximum on a lot',
                                   'PRYCD ([7jGQIvwqBwc @ 00:17:40])'],
                                  ['Big volume list versus small niche list for the first campaign',
                                   'Lauren Hardy would rather have a bigger list than a smaller list when '
                                   'in doubt',
                                   'Dier calls niche lists too small yet still says pre-foreclosures are '
                                   'the way',
                                   'The Well Entrepreneur ([p_LcZVcrC3U @ 00:05:09])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The most common self-inflicted loss is trusting a data field that was never '
                              "populated correctly. Great Lands LLC tested PropStream's improvement-value "
                              'and estimated-value filters live and found them poorly populated or flatly '
                              'broken, so the raw-land screen had to lean on assessed value of $5,000 or '
                              'less and last sale price instead [Mdkx15sX_XM @ 00:08:52]. Lauren Hardy '
                              'calls the data tricky: MLS and pre-foreclosure filters come from '
                              'data-mining firms, East Coast records are error-prone, and equity gets '
                              'skipped because it is so often wrong, even though Hardy later calls the '
                              'remaining data super accurate [p_LcZVcrC3U @ 00:03:36]. Country Land '
                              'Sellers flags timing rot on the county side: GIS ownership lags roughly a '
                              'month, the Recorder is the most current source, and the Assessor updates '
                              'only afterward, so an owner name on the map may already be stale when the '
                              'letter prints [6qNh515jvww @ 00:04:53]. Don Healy sees the same problem at '
                              'scale, with CoreLogic and Regrid data packages dated enough that recent '
                              'partitions do not match the ground, and jurisdiction PDFs sometimes '
                              'contradicting the GIS layers they are supposed to back up [IS6mrT0hkGw @ '
                              '00:27:32]. Every field that drives a filter or a price needs a second '
                              'source behind it before money goes out the door.',
                              'The expensive failures arrive after the contract, when a lot that looked '
                              'clean turns out to be hobbled. Don Healy warns that a county saying '
                              'buildable may mean buildable only under a conditional use, that utilities '
                              'available can mean a 300-foot mainline extension, and that resource zones '
                              'once imposed 100-foot setbacks on three sides, leaving a lot darn near '
                              'unbuildable; Seth no longer calls listings buildable at all [IS6mrT0hkGw @ '
                              "00:15:38]. Healy's landslide case carried a clean seller disclosure, yet "
                              'the assessor code read unbuildable and a title note pointed to a slide, '
                              'forcing helical piles and a geotech review before anything could go up '
                              '[IS6mrT0hkGw @ 00:17:57]. Luke Harris used the aerial basemap and Street '
                              'View to catch a parcel that had no real road access, the kind of flaw that '
                              'never shows on a spreadsheet export [6qNh515jvww @ 00:03:48]. Joséphine '
                              'Saffert reads floodplain layers and contour lines on a Nashville lot, '
                              'tracking roughly a 10-foot drop from 524 to 502 and circling the low '
                              'drainage point before ever touring in person [_kxaCpUojPw @ 00:04:03]. '
                              "Healy's pricing rule follows directly: an 18-month, $40,000 approval "
                              "process has to come out of the offer, and a listing that says buyer's due "
                              'diligence is a red flag.',
                              'The unit economics punish anyone who quits early or misreads the bill. '
                              "Dier's cold-calling math runs 1,000 calls to one lead and 30 leads to one "
                              'deal, which is why Dier pulls 10,000 records, calls each three times, and '
                              'runs Enzo Dialer on 14 lines at about 2,000 calls a day [KmEcpx-t8YM @ '
                              '00:01:55]. Matt prices mail at $0.79 per piece through Land of Enchantment '
                              'Direct Mail, with letter, envelope, and postage included, and says the '
                              'secret is consistency because it is a numbers game: operators who quit '
                              'after 200 letters never see the response math play out [hemWETr8VGg @ '
                              '00:01:14]. The Apke Brothers flag a billing trap inside DataTree: records '
                              'cost 10 cents each with membership, and removing duplicate owners lowers '
                              'the charge, but the deduplicated count is not shown before purchase, so the '
                              "true bill stays hidden until checkout [tZnXE47jWp4 @ 00:07:14]. PRYCD's Max "
                              'Edson reminds operators that the analysis rank reflects pricing confidence, '
                              'not the best place to mail, that the scrub file strips church and '
                              'government owners at averages of 0.5% and 4.4%, and that 300 priced records '
                              'cost $24 before a single stamp is bought [7jGQIvwqBwc @ 00:13:45].'],
               'table': {'caption': 'Firsthand data, buildability, and cost traps with the practitioner '
                                    'fix',
                         'headers': ['Trap', 'What Went Wrong', 'Operator Check', 'Expert Source'],
                         'rows': [['PropStream improvement and estimated value filters returning bad '
                                   'counts',
                                   'Great Lands LLC found both fields poorly populated or broken '
                                   'mid-search',
                                   'Screen raw land with assessed value at or under $5,000 and last sale '
                                   'price',
                                   'Great Lands LLC ([Mdkx15sX_XM @ 00:08:52])'],
                                  ['County staff calling a parcel buildable over the phone',
                                   'Buildable meant buildable only under a conditional use on that parcel',
                                   'Send the county template questions because different staff give '
                                   'different answers',
                                   'REtipster ([IS6mrT0hkGw @ 00:15:38])'],
                                  ['Trusting county GIS owner names for a fresh mailing',
                                   'County GIS ownership updates lag roughly a month behind recorded deeds',
                                   'Check the Recorder first because the Assessor only updates afterward',
                                   'Country Land Sellers ([6qNh515jvww @ 00:01:47])'],
                                  ['Paying DataTree for duplicate owner records on an export',
                                   'The deduplicated owner count is not shown before the export charge '
                                   'posts',
                                   'Remove duplicate owners every time since it lowers the 10 cent per '
                                   'record charge',
                                   'Apke Brothers ([tZnXE47jWp4 @ 00:07:14])'],
                                  ['Over-stacking distress filters into a tiny unusable list',
                                   'Vacant plus tax delinquent shrank Albuquerque from 12,000 down to 269 '
                                   'records',
                                   'Target roughly 6,000 records and keep the 269 stacked list for '
                                   'door-knocking',
                                   'The Well Entrepreneur ([p_LcZVcrC3U @ 00:02:04])'],
                                  ['Title work stalling the closing calendar on land deals',
                                   'Closings stretched from 10 days to 15 to 20 days on title plant '
                                   'backlog',
                                   'Call twice a week, agree a date, repeat it in every email, and send '
                                   'treats',
                                   'Land Academy ([CbpqiGq5E5Y @ 00:01:55])'],
                                  ['Reading the PRYCD county rank as a mailing priority',
                                   'Rank reflects pricing confidence in the model, not the best place to '
                                   'mail',
                                   'Use rank only to gauge pricing confidence and apply city pricing '
                                   'explicitly',
                                   'PRYCD ([7jGQIvwqBwc @ 00:13:45])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Pre-Spend Data and Buildability Gate',
                           'body': 'Clear these four checks before paying for records, mailing a list, or '
                                   'signing a purchase contract on raw land.',
                           'items': ['Confirm the raw-land screen actually works on your platform: '
                                     'residential land-use codes need improvement value set to 0, and '
                                     "PropStream's improvement-value field may be poorly populated [PRYCD "
                                     '— 7jGQIvwqBwc @ 00:09:40].',
                                     'Verify zoning for the intended use plus soils and slope on every '
                                     'parcel, since EFU land carries an 80-acre minimum lot size '
                                     '[REtipster — IS6mrT0hkGw @ 00:34:49].',
                                     'Pull ownership from the Recorder rather than the Assessor or GIS '
                                     'layer, which update later and can be stale [Country Land Sellers — '
                                     '6qNh515jvww @ 00:04:53].',
                                     'Budget for volume before launching: 1,000 calls per lead and 30 '
                                     'leads per deal, with each record dialed three times [Maximilian Dier '
                                     '— KmEcpx-t8YM @ 00:01:55].']}}],
 'pull_quote': '"But a confirmed no is almost as valuable as a yes." — Don Healy on REtipster (IS6mrT0hkGw '
               '@ 00:33:41).',
 'diagram_id': 'diag-07',
 'action_checklist': ['Shortlist counties on the PRYCD research page by filtering population under 20 per '
                      'square mile, then parcels-on-market under .05 [PRYCD — 7jGQIvwqBwc @ 00:04:32].',
                      'Isolate raw land in DataTree by setting assessed improvement value to 0, then keep '
                      'the result under 1,000 so it plots on the map [Apke Brothers — tZnXE47jWp4 @ '
                      '00:02:39].',
                      'Exclude corporate and do-not-mail owners, filter flood codes, and drop active and '
                      'pending listings before pricing the list [PRYCD — 7jGQIvwqBwc @ 00:10:09].',
                      'Request the tax-delinquent list free from the county as a private citizen doing '
                      'independent research, file a FOIA if refused, and ask for Excel to avoid page fees '
                      '[Zach Ginn — 3VKazhO11yk @ 00:04:37].',
                      'Upload the list to PRYCD, map county, state, and acreage, and set the offer '
                      'discount, for example from the 30% default to 25% [PRYCD — 3kN1hBRUqVU @ 00:01:50].',
                      'Order the Site Facts report at the start of a 30-day due diligence period on lots '
                      'above roughly $50K, especially builder exits [REtipster — IS6mrT0hkGw @ 00:10:08].'],
 'statutory_citations': [{'title': 'REtipster — The Report That Gives Land Investors an Unfair Advantage '
                                   'w/ Don Healy | REtipster Podcast 258 [00:09:56]',
                          'url': 'https://www.youtube.com/watch?v=IS6mrT0hkGw&t=596s',
                          'relevance': 'Primary practitioner testimony on early-stage buildability due '
                                       'diligence and the deal-killing traps in county and listing data.'},
                         {'title': 'Land Academy — DataTree vs TitlePro vs RealQuest Pro (LA 1422) '
                                   '[00:11:10]',
                          'url': 'https://www.youtube.com/watch?v=CbpqiGq5E5Y&t=670s',
                          'relevance': 'Primary practitioner testimony on choosing between DataTree, '
                                       'TitlePro, and RealQuest for multi-county land mailers.'},
                         {'title': 'PRYCD — PRYCD Land Step-By-Step Process Flow [00:04:32]',
                          'url': 'https://www.youtube.com/watch?v=7jGQIvwqBwc&t=272s',
                          'relevance': 'Primary practitioner testimony on county selection, list '
                                       'filtering, offer pricing, and scrub files.'},
                         {'title': 'Great Lands LLC — Propstream for Land Investors [00:03:14]',
                          'url': 'https://www.youtube.com/watch?v=Mdkx15sX_XM&t=194s',
                          'relevance': 'Primary practitioner testimony on a PropStream vacant-land filter '
                                       'funnel, broken value fields, and comp-based offers.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'IS6mrT0hkGw',
                       'title': 'The Report That Gives Land Investors an Unfair Advantage w/ Don Healy | '
                                'REtipster Podcast 258',
                       'channel': 'REtipster',
                       'author': 'REtipster',
                       'text': 'But a confirmed no is almost as valuable as a yes, if that makes sense.',
                       'tip': 'But a confirmed no is almost as valuable as a yes, if that makes sense.',
                       'timestamp': 2021,
                       'timestamp_seconds': 2021,
                       'timestamp_label': '[00:33:41]',
                       'url': 'https://www.youtube.com/watch?v=IS6mrT0hkGw&t=2021s',
                       'markdown': '[00:33:41](https://www.youtube.com/watch?v=IS6mrT0hkGw&t=2021s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'IS6mrT0hkGw',
                       'title': 'The Report That Gives Land Investors an Unfair Advantage w/ Don Healy | '
                                'REtipster Podcast 258',
                       'channel': 'REtipster',
                       'author': 'REtipster',
                       'text': "You want to have the better due diligence to make sure that if there's "
                               "something that buyer is going to find that's going to trip your whole deal "
                               'up, you want to be aware of that before you get there.',
                       'tip': "You want to have the better due diligence to make sure that if there's "
                              "something that buyer is going to find that's going to trip your whole deal "
                              'up, you want to be aware of that before you get there.',
                       'timestamp': 596,
                       'timestamp_seconds': 596,
                       'timestamp_label': '[00:09:56]',
                       'url': 'https://www.youtube.com/watch?v=IS6mrT0hkGw&t=596s',
                       'markdown': '[00:09:56](https://www.youtube.com/watch?v=IS6mrT0hkGw&t=596s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'tZnXE47jWp4',
                       'title': 'Is Data Tree the Best Data Tool for Land Investing? (Review & Tutorial)',
                       'channel': 'Apke Brothers',
                       'author': 'Apke Brothers',
                       'text': "I'm gonna hit zero so that's basically saying there's no improvements to "
                               "the land, it's raw land.",
                       'tip': "I'm gonna hit zero so that's basically saying there's no improvements to "
                              "the land, it's raw land.",
                       'timestamp': 159,
                       'timestamp_seconds': 159,
                       'timestamp_label': '[00:02:39]',
                       'url': 'https://www.youtube.com/watch?v=tZnXE47jWp4&t=159s',
                       'markdown': '[00:02:39](https://www.youtube.com/watch?v=tZnXE47jWp4&t=159s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '6qNh515jvww',
                       'title': 'The Secret to researching land easily with County GIS!',
                       'channel': 'Country Land Sellers',
                       'author': 'Country Land Sellers',
                       'text': "So the ownership information like I said isn't always super accurate and "
                               'up to date on this system.',
                       'tip': "So the ownership information like I said isn't always super accurate and up "
                              'to date on this system.',
                       'timestamp': 314,
                       'timestamp_seconds': 314,
                       'timestamp_label': '[00:05:14]',
                       'url': 'https://www.youtube.com/watch?v=6qNh515jvww&t=314s',
                       'markdown': '[00:05:14](https://www.youtube.com/watch?v=6qNh515jvww&t=314s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'CbpqiGq5E5Y',
                       'title': 'DataTree vs TitlePro vs RealQuest Pro (LA 1422)',
                       'channel': 'Land Academy',
                       'author': 'Land Academy',
                       'text': 'Data tree is the 21st century answer to pulling land and house data, '
                               'really any type of real estate data, and then visually seeing it.',
                       'tip': 'Data tree is the 21st century answer to pulling land and house data, really '
                              'any type of real estate data, and then visually seeing it.',
                       'timestamp': 619,
                       'timestamp_seconds': 619,
                       'timestamp_label': '[00:10:19]',
                       'url': 'https://www.youtube.com/watch?v=CbpqiGq5E5Y&t=619s',
                       'markdown': '[00:10:19](https://www.youtube.com/watch?v=CbpqiGq5E5Y&t=619s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'oJpqcR4iFy8',
                       'title': 'How to Build a Hand-Picked List of Properties by “Parcel Tagging” on '
                                'DataTree',
                       'channel': 'REtipster',
                       'author': 'REtipster',
                       'text': 'Apply the tags, switch to Less Map, and export, which gives about 20 to 40 '
                               'properties for a small town.',
                       'tip': 'Apply the tags, switch to Less Map, and export, which gives about 20 to 40 '
                              'properties for a small town.',
                       'timestamp': 209,
                       'timestamp_seconds': 209,
                       'timestamp_label': '[00:03:29]',
                       'url': 'https://www.youtube.com/watch?v=oJpqcR4iFy8&t=209s',
                       'markdown': '[00:03:29](https://www.youtube.com/watch?v=oJpqcR4iFy8&t=209s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'mhHvzO1O8To',
                       'title': 'PRYCD Out of County Owner to Total Parcel Ratio Map Example',
                       'channel': 'PRYCD',
                       'author': 'PRYCD',
                       'text': 'Filter the map to counties where the out of county owner to total parcel '
                               'ratio is 40% or higher.',
                       'tip': 'Filter the map to counties where the out of county owner to total parcel '
                              'ratio is 40% or higher.',
                       'timestamp': 52,
                       'timestamp_seconds': 52,
                       'timestamp_label': '[00:00:52]',
                       'url': 'https://www.youtube.com/watch?v=mhHvzO1O8To&t=52s',
                       'markdown': '[00:00:52](https://www.youtube.com/watch?v=mhHvzO1O8To&t=52s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'EmWzMGDpkTY',
                       'title': 'Public Records Property Data: Data 101 Series | DataTree by First '
                                'American',
                       'channel': 'DataTree by First American',
                       'author': 'DataTree by First American',
                       'text': 'The APN works like a Social Security number for each parcel on the county '
                               'tax roll.',
                       'tip': 'The APN works like a Social Security number for each parcel on the county '
                              'tax roll.',
                       'timestamp': 73,
                       'timestamp_seconds': 73,
                       'timestamp_label': '[00:01:13]',
                       'url': 'https://www.youtube.com/watch?v=EmWzMGDpkTY&t=73s',
                       'markdown': '[00:01:13](https://www.youtube.com/watch?v=EmWzMGDpkTY&t=73s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '7jGQIvwqBwc',
                       'title': 'PRYCD Land Step-By-Step Process Flow',
                       'channel': 'PRYCD',
                       'author': 'PRYCD',
                       'text': 'The rank reflects confidence in the pricing, not the best place to mail.',
                       'tip': 'The rank reflects confidence in the pricing, not the best place to mail.',
                       'timestamp': 825,
                       'timestamp_seconds': 825,
                       'timestamp_label': '[00:13:45]',
                       'url': 'https://www.youtube.com/watch?v=7jGQIvwqBwc&t=825s',
                       'markdown': '[00:13:45](https://www.youtube.com/watch?v=7jGQIvwqBwc&t=825s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '7jGQIvwqBwc',
                       'title': 'PRYCD Land Step-By-Step Process Flow',
                       'channel': 'PRYCD',
                       'author': 'PRYCD',
                       'text': 'The scrub filters remove on average about 0.5% church owners and 4.4% '
                               'government owners.',
                       'tip': 'The scrub filters remove on average about 0.5% church owners and 4.4% '
                              'government owners.',
                       'timestamp': 1381,
                       'timestamp_seconds': 1381,
                       'timestamp_label': '[00:23:01]',
                       'url': 'https://www.youtube.com/watch?v=7jGQIvwqBwc&t=1381s',
                       'markdown': '[00:23:01](https://www.youtube.com/watch?v=7jGQIvwqBwc&t=1381s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '_kxaCpUojPw',
                       'title': 'Parcel Viewer Tutorial: How To Find Land Deals Fast',
                       'channel': 'Joséphine Saffert',
                       'author': 'Joséphine Saffert',
                       'text': 'Some tools are better than others. This one here is pretty good.',
                       'tip': 'Some tools are better than others. This one here is pretty good.',
                       'timestamp': 70,
                       'timestamp_seconds': 70,
                       'timestamp_label': '[00:01:10]',
                       'url': 'https://www.youtube.com/watch?v=_kxaCpUojPw&t=70s',
                       'markdown': '[00:01:10](https://www.youtube.com/watch?v=_kxaCpUojPw&t=70s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Mdkx15sX_XM',
                       'title': 'Propstream for Land Investors',
                       'channel': 'Great Lands LLC',
                       'author': 'Great Lands LLC',
                       'text': 'So it sounds like this part is not well populated.',
                       'tip': 'So it sounds like this part is not well populated.',
                       'timestamp': 532,
                       'timestamp_seconds': 532,
                       'timestamp_label': '[00:08:52]',
                       'url': 'https://www.youtube.com/watch?v=Mdkx15sX_XM&t=532s',
                       'markdown': '[00:08:52](https://www.youtube.com/watch?v=Mdkx15sX_XM&t=532s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '3kN1hBRUqVU',
                       'title': 'PRYCD List Upload Example Video',
                       'channel': 'PRYCD',
                       'author': 'PRYCD',
                       'text': "You can see that we've priced and mapped 1,359 out of 1,359, so this was a "
                               'good pull.',
                       'tip': "You can see that we've priced and mapped 1,359 out of 1,359, so this was a "
                              'good pull.',
                       'timestamp': 138,
                       'timestamp_seconds': 138,
                       'timestamp_label': '[00:02:18]',
                       'url': 'https://www.youtube.com/watch?v=3kN1hBRUqVU&t=138s',
                       'markdown': '[00:02:18](https://www.youtube.com/watch?v=3kN1hBRUqVU&t=138s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '1VVAkFWqVKE',
                       'title': 'How I Got 2 Listings from 1 Direct Mail Campaign (Step-by-Step Guide for '
                                'Realtors)',
                       'channel': 'Ryan Dossey',
                       'author': 'Ryan Dossey',
                       'text': "Now just setting proper expectations, it doesn't always happen that fast.",
                       'tip': "Now just setting proper expectations, it doesn't always happen that fast.",
                       'timestamp': 507,
                       'timestamp_seconds': 507,
                       'timestamp_label': '[00:08:27]',
                       'url': 'https://www.youtube.com/watch?v=1VVAkFWqVKE&t=507s',
                       'markdown': '[00:08:27](https://www.youtube.com/watch?v=1VVAkFWqVKE&t=507s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '3VKazhO11yk',
                       'title': 'Wholesaling Tax Delinquent Properties (Step by Step)',
                       'channel': 'Zach Ginn',
                       'author': 'Zach Ginn',
                       'text': 'You might get better results texting than cold calling, but just a slight.',
                       'tip': 'You might get better results texting than cold calling, but just a slight.',
                       'timestamp': 401,
                       'timestamp_seconds': 401,
                       'timestamp_label': '[00:06:41]',
                       'url': 'https://www.youtube.com/watch?v=3VKazhO11yk&t=401s',
                       'markdown': '[00:06:41](https://www.youtube.com/watch?v=3VKazhO11yk&t=401s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'p_LcZVcrC3U',
                       'title': 'How To Get A Cold Call List - Tax Delinquent List',
                       'channel': 'The Well Entrepreneur',
                       'author': 'The Well Entrepreneur',
                       'text': "So when in doubt I'd rather have a bigger list than a smaller list.",
                       'tip': "So when in doubt I'd rather have a bigger list than a smaller list.",
                       'timestamp': 309,
                       'timestamp_seconds': 309,
                       'timestamp_label': '[00:05:09]',
                       'url': 'https://www.youtube.com/watch?v=p_LcZVcrC3U&t=309s',
                       'markdown': '[00:05:09](https://www.youtube.com/watch?v=p_LcZVcrC3U&t=309s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'KmEcpx-t8YM',
                       'title': 'How to Pull The BEST Wholesale List For Cold Calling & Texting',
                       'channel': 'Maximilian Dier',
                       'author': 'Maximilian Dier',
                       'text': 'When cold calling, every 1,000 calls is usually one lead. And it takes on '
                               'average 30 leads to get one deal.',
                       'tip': 'When cold calling, every 1,000 calls is usually one lead. And it takes on '
                              'average 30 leads to get one deal.',
                       'timestamp': 115,
                       'timestamp_seconds': 115,
                       'timestamp_label': '[00:01:55]',
                       'url': 'https://www.youtube.com/watch?v=KmEcpx-t8YM&t=115s',
                       'markdown': '[00:01:55](https://www.youtube.com/watch?v=KmEcpx-t8YM&t=115s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'hemWETr8VGg',
                       'title': 'How to Find Off-Market Real Estate Deals Using Direct Mail | MS Partners '
                                'LLC',
                       'channel': 'MS Partners LLC',
                       'author': 'MS Partners LLC',
                       'text': "But here's the secret, consistency. As with any sales, it's a numbers "
                               'game.',
                       'tip': "But here's the secret, consistency. As with any sales, it's a numbers game.",
                       'timestamp': 74,
                       'timestamp_seconds': 74,
                       'timestamp_label': '[00:01:14]',
                       'url': 'https://www.youtube.com/watch?v=hemWETr8VGg&t=74s',
                       'markdown': '[00:01:14](https://www.youtube.com/watch?v=hemWETr8VGg&t=74s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'}]}
