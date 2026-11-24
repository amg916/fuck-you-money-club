from __future__ import annotations

CHAPTER_11 = {'id': 'Q11',
 'chapter_id': 'Q11',
 'chapter_number': 11,
 'question_number': 11,
 'slug': 'google-shopping-feeds-merchant-center',
 'question_prompt': 'How do I set up and optimize my Google Merchant Center product feed so Shopping and '
                    'Performance Max ads, plus free listings, actually perform?',
 'kicker': 'Q11 / THE BIG MONEY PLAYBOOKS',
 'title': 'Google Shopping Feeds and Merchant Center',
 'subtitle': 'Merchant Center setup for Shopify, titles and product categories, attribute rules, custom '
             'labels with Google Sheets, Merchant Center promotions, feed fixes for Performance Max ROAS, '
             'organic free listings, and high-ticket SEO niches',
 'layout_template': 'chapter_opener',
 'reading_time_minutes': 15,
 'executive_summary': 'Operators from Grow My Ads, Ecom Chris, KeyCommerce, Max Crakanthorp and Abdul Rauf '
                      'Ali converge on one rule: in Shopping and Performance Max, the feed is the '
                      'targeting, and price is the lever that rules all. They front-load titles with the '
                      'converting search term, use most of the 150 characters, pick the deepest product '
                      'category, keep price, sale price and availability identical to the site, and never '
                      'change product IDs. Street numbers include a 10x click-and-impression jump from a '
                      'Home Reserve sofa retitle, a 2-3x CTR lift from lifestyle imagery, 20-30% more '
                      'sales from one winter-jacket retitle, and CPCs 2-3x higher on poorly optimized '
                      'feeds. Custom labels built through attribute rules, Google Sheets or supplemental '
                      'feeds segment by margin, price bucket and season. Practitioners split on '
                      "brand-first versus keyword-first titles, description effort, Google's generative "
                      'image tools and whether GTINs are essential.',
 'key_metrics': [{'label': 'Home Reserve Title Rewrite Lift',
                  'metric': 'Home Reserve Title Rewrite Lift',
                  'value': '10x jump in clicks and impressions',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Retitling an 'Alley sofa' listing to 'kid and pet friendly sectional sofa... "
                             "washable' produced a 10x jump in clicks and impressions, and sales rose.",
                  'source': 'Grow My Ads ([hY8ZBC3A4uQ @ 00:10:45])'},
                 {'label': 'Lifestyle Image CTR Lift',
                  'metric': 'Lifestyle Image CTR Lift',
                  'value': '2-3x CTR lift',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Lifestyle images versus plain product shots in Shopping listings; the '
                             'white-background main image is kept and lifestyle shots added as additional '
                             'images.',
                  'source': 'Grow My Ads ([hY8ZBC3A4uQ @ 00:13:00])'},
                 {'label': 'Converting Search Term Retitle',
                  'metric': 'Converting Search Term Retitle',
                  'value': '20-30% more sales in about a week at the same ROAS',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'A winter jacket title was rewritten to match the search term that was '
                             'already converting.',
                  'source': 'Ecom Chris ([d9kULGtUBD4 @ 00:12:01])'},
                 {'label': 'Poorly Optimized Feed CPC Penalty',
                  'metric': 'Poorly Optimized Feed CPC Penalty',
                  'value': 'CPC 2-3x higher',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Tracked alongside CTR, bounce rate, CVR and ROAS; poorly optimized feeds pay '
                             'two to three times the CPC.',
                  'source': 'Ecom Chris ([XQTEnn-3t0E @ 00:23:16])'}],
 'sections': [{'title': 'Section 1: The Practitioner Consensus',
               'paragraphs': ['Every operator in this group starts from the same premise: in Shopping and '
                              'Performance Max, the product feed is the targeting. Ecom Chris opens '
                              'bluntly, saying that if Shopping or PMax feels random, it is usually not '
                              'the bidding, it is the product data, and argues that money leaks out of the '
                              'foundation rather than out of campaign structure, tROAS settings or hacks; '
                              'poor input data brings low CTR and ROAS, inflated CPCs and '
                              'misrepresentation suspensions [XQTEnn-3t0E @ 00:00:00]. Casey Gill, '
                              'teaching inside the Jyll Saskin Gales course, says feed data replaces '
                              'keyword research for Shopping and PMax, and works titles, then product '
                              "types, then categories as separate passes, calling each fix a '1% factor' "
                              '[Q-KrwvAVhR4 @ 00:01:25]. KeyCommerce adds pressure from the next channel: '
                              'AI shopping assistants bypass the website and read feed data directly, so '
                              'incomplete feeds simply get skipped [S1NhYxaPnic @ 00:00:28]. Abdul Rauf '
                              'Ali, showing an account with $7.19M in conversion value at a 3.93 ROAS on '
                              'roughly $1.8M spend, runs diagnostics in a fixed order of understand, '
                              'match, click and close, and reads the search terms report before touching '
                              'anything else [V0LAr3jchLs @ 00:01:25]. The shared conclusion is simple: '
                              'fix the data first, then argue about bids.',
                              'Titles and price are the two levers ranked highest across the group. Austin '
                              'of Grow My Ads says the first 30 to 70 characters of a title are most '
                              'critical, yet sellers should use as much of the 150-character limit as '
                              'possible, because Google may reorder words already in the title but does '
                              'not add new ones; well-known brands such as Nike, Apple or Samsung go '
                              'first, while unknown brands go at the end [hY8ZBC3A4uQ @ 00:04:15]. On '
                              "price, Austin is unequivocal that 'price will rule all': a competitor 20% "
                              'cheaper beats the best-built feed, and price baiting, checkout hacks or '
                              'fake sale prices can get the account suspended [hY8ZBC3A4uQ @ 00:02:10]. '
                              'Kai Cromwell reports that below-average prices lift impressions and CTR, '
                              'recommends cheaper entry products with an upsell later, and warns that '
                              'stale sale prices hurt visibility [W6w0BjjlBs4 @ 00:06:44]. Ecom Chris '
                              'lands in the same place, calling Google a price comparison platform, '
                              'flagging that shoppers hold back mid-month and at month end, and pricing '
                              'within 5 to 10% of the average while insisting it is not a race to the '
                              'bottom [XQTEnn-3t0E @ 00:15:41]. Titles earn the match; price decides the '
                              'click.',
                              'The third point of agreement is strict consistency between the feed, the '
                              "store and the business behind it. KeyCommerce's Sam tells operators to "
                              'change price, availability and sale fields at the source, such as Shopify, '
                              'because Google checks daily and a discrepancy brings quick disapproval; Sam '
                              'also warns never to overwrite a product ID, since doing so creates a new '
                              'product, loses its history, and the team has watched catalog-wide ID '
                              'changes make performance plummet [UcU7Ishu1lY @ 00:04:52]. Max Crakanthorp '
                              'always recommends adding a sale price because the green sale price boosts '
                              'clicks, but a mismatch between feed and website gets the product suspended '
                              '[H4yH9xs030Q @ 00:13:20]. In the setup course, Max adds that business '
                              'information which does not match the website leads to misrepresentation '
                              "bans, and that only an 'exceptional' rating earns the top quality store "
                              'badge [FZOo2bNTrzo @ 00:08:23]. Wixpa closes the loop with a line operators '
                              'should tape to the monitor: a perfect product feed does not by itself get '
                              'products approved, because contact, refund, shipping, privacy and terms '
                              'pages plus visible business details still have to exist on the site, and '
                              'suspensions remain possible even after a clean app-based sync [RHJvGN_6sf0 '
                              '@ 00:04:47].'],
               'table': {'caption': 'Consensus Baselines Across Practitioners',
                         'headers': ['Consensus Principle',
                                     'What Practitioners Actually Do',
                                     'Reported Payoff or Risk',
                                     'Expert Source'],
                         'rows': [['Feed data is the real targeting layer',
                                   'Fix titles, product types and categories before touching bids or '
                                   'campaign structure',
                                   'Poor input data brings low CTR, high CPC and misrepresentation '
                                   'suspensions',
                                   'Ecom Chris ([XQTEnn-3t0E @ 00:01:38])'],
                                  ['Front-load the title with the searched product term',
                                   'Put the product keyword first and use most of the 150 characters',
                                   'Only about 70 characters show, so the opening words do the selling',
                                   'Kai Cromwell - eCommerce SEO ([W6w0BjjlBs4 @ 00:03:01])'],
                                  ['Price outranks every other feed optimization lever',
                                   'Benchmark competitors and stay close to the average market price',
                                   'A competitor 20% cheaper beats even the best-built product feed',
                                   'Grow My Ads ([hY8ZBC3A4uQ @ 00:02:10])'],
                                  ['Feed price, sale price and availability must match the site',
                                   'Change these fields at the source store because Google checks daily',
                                   'Any discrepancy triggers fast disapproval or outright product '
                                   'suspension',
                                   'KeyCommerce ([UcU7Ishu1lY @ 00:04:19])'],
                                  ['Never overwrite or change existing product IDs',
                                   'Keep the previous ID format when migrating to a new feed app',
                                   'A changed ID creates a new product and wipes learned history',
                                   'Wixpa Google Shopping Feed ([RHJvGN_6sf0 @ 00:02:18])'],
                                  ['Use the deepest accurate Google product category',
                                   'Move vague paths into specific ones, like Clothing & Closet Storage',
                                   'Casey Gill calls the corrected path a much better optimization',
                                   'Jyll Saskin Gales | Google Ads Coach ([Q-KrwvAVhR4 @ 00:00:41])'],
                                  ['Business details must mirror the live website exactly',
                                   'Keep Merchant Center business info identical to what the store shows',
                                   'Mismatched business information leads directly to misrepresentation '
                                   'bans',
                                   'Max Crakanthorp ([FZOo2bNTrzo @ 00:08:23])']]}},
              {'title': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['Title work is where the hard numbers live. Ecom Chris says this is not SEO: '
                              "build a 2 to 3 word primary keyword such as 'running shoe' plus secondary "
                              'modifiers, and source terms in strict priority order, with Google Ads '
                              'search terms first, then Merchant Center queries, autocomplete, competitor '
                              'listings, and keyword tools last [d9kULGtUBD4 @ 00:10:53]. The payoff '
                              'anecdote: retitling a winter jacket to match its converting search term '
                              'produced 20 to 30% more sales in about a week at the same ROAS [d9kULGtUBD4 '
                              '@ 00:12:01]. Austin at Grow My Ads reports the Home Reserve case, where '
                              "renaming an 'Alley sofa' to a 'kid and pet friendly sectional sofa' with "
                              "'washable' in the title produced a 10x jump in clicks and impressions, and "
                              'sales rose with it [hY8ZBC3A4uQ @ 00:10:45]. Grow My Ads then rolls that '
                              'pattern across hundreds of SKUs without touching the store: an attribute '
                              "rule prepends 'kid and pet friendly washable' and appends the Home Reserve "
                              "brand, turning 'tuck standard sectional in malti soda' into a keyword-led "
                              'title, which the team says drove very significant increases in performance '
                              "[-w0GraOv2B0 @ 00:06:16]. Chris's filter for every modifier: if removing it "
                              'would attract the wrong buyer, keep it, because search volume barely '
                              'matters.',
                              'Custom labels are the segmentation engine, and every practitioner who '
                              'covers them works the same five slots, labels 0 through 4. Tim Sutton shows '
                              "a PMax client bucketed by price from 100 up to 10,000, with a '2,000+' "
                              'label carrying its own tROAS and products with 100+ clicks and low ROAS '
                              'excluded outright; Tim also warns manual edits do not scale to thousands of '
                              'SKUs, so the labels live in a supplemental sheet filled down [APb0cOGKROE @ '
                              '00:05:06]. Grow My Ads builds labels with zero third-party tooling: in '
                              'Merchant Center Next, go to data sources, the Content API source, attribute '
                              "rules, add a rule on custom_label_3, and set it to 'Christmas' when the "
                              'title contains Christmas, Santa or holiday; the preview shows the active '
                              'value empty against the draft value, and the change goes live on the next '
                              "fetch [-w0GraOv2B0 @ 00:03:09]. PPC Incubator's Ian maps a Google Sheet of "
                              'brand tiers (top, high, mid, low) through feed rules, then splits listing '
                              'groups first by 25% margin and then by low brand [79VrN9FhpT8 @ 00:01:21]. '
                              'Abdul Rauf Ali tags top performers using a hygiene filter of ROAS above the '
                              '1.9 breakeven, at least 50 clicks, over a 6 to 12 month window [V0LAr3jchLs '
                              '@ 00:08:40].',
                              'Promotions, images and tooling round out the mechanics. KeyCommerce sets '
                              'promotions up through Settings, Add-ons, Promotions, Add; the promo code '
                              'must already exist in the store, and because Google ends promos at midnight '
                              'the day before, the end time goes in as 11:59 p.m.; review takes 1 to 24 '
                              'hours, longer around Black Friday, and free shipping is the recommended '
                              'first promotion [jmjy6G9akyM @ 00:01:32]. Max Crakanthorp runs a 10 to 20% '
                              'test promo and notes first-order promotions are available with new-customer '
                              'bidding [FZOo2bNTrzo @ 00:19:26]. On images, Austin reports lifestyle shots '
                              'deliver a 2 to 3x CTR lift, uses Product Studio to remove backgrounds, '
                              'raise resolution and generate scenes, got a good lifestyle image from a '
                              'single Nano Banana Pro prompt, and keeps the white-background main image '
                              'with lifestyle shots added as extras [hY8ZBC3A4uQ @ 00:13:00]. For feed '
                              'software, Austin ranks Channable first, puts Feedonomics in the enterprise, '
                              'hands-on tier for spend from a couple hundred thousand a year into the '
                              'millions, and positions DataFeedWatch as the cheaper, more DIY option '
                              '[hY8ZBC3A4uQ @ 00:29:24]. Whatever tool runs the catalog, edits belong '
                              'inside that tool.'],
               'table': {'caption': 'Street Mechanics: Specs, Rules and Numbers',
                         'headers': ['Mechanic',
                                     'Exact Spec or Number',
                                     'How Practitioners Execute It',
                                     'Expert Source'],
                         'rows': [['Title length and attribute order',
                                   'Run titles at 110 to 130 of the 150 allowed characters',
                                   'Frontload the keyword, then size, color, material and gender, no '
                                   'stuffing',
                                   'Ecom Chris ([XQTEnn-3t0E @ 00:02:11])'],
                                  ['Image minimums and framing rules',
                                   '100x100 non-apparel, 250x250 apparel, product filling 75-90% of frame',
                                   'White, gray or light background, maximum 64 MP or 16 MB',
                                   'Kai Cromwell - eCommerce SEO ([W6w0BjjlBs4 @ 00:01:55])'],
                                  ['Lifestyle imagery as additional images',
                                   'Lifestyle images deliver a reported 2-3x CTR lift',
                                   'Keep the white-background main image and add lifestyle shots as extras',
                                   'Grow My Ads ([hY8ZBC3A4uQ @ 00:13:00])'],
                                  ['Price-bucket custom labels for PMax',
                                   'Buckets from 100 to 10,000 with a separate 2,000+ label',
                                   'Give the 2,000+ bucket its own tROAS and exclude 100+ click low-ROAS '
                                   'products',
                                   'Tim Sutton | Google Ads | Launchpresso ([APb0cOGKROE @ 00:05:06])'],
                                  ['Hygiene filter for top performers',
                                   'ROAS above 1.9 breakeven, at least 50 clicks, 6-12 months',
                                   'Tag winners with a custom label pushed through a supplemental feed',
                                   'Abdul Rauf Ali ([V0LAr3jchLs @ 00:08:40])'],
                                  ['Promotion end-time setting in Merchant Center',
                                   'Set the end time to 11:59 p.m. on the final day',
                                   'Google otherwise ends the promotion at midnight the day before',
                                   'KeyCommerce ([jmjy6G9akyM @ 00:01:32])'],
                                  ['Title testing cadence and budget floor',
                                   'One change per SKU, run for 1-2 weeks',
                                   'At $40-50 per day there is not enough data to read results',
                                   'Ecom Chris ([d9kULGtUBD4 @ 00:28:56])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Operator Edges From the Practitioners',
                           'body': 'Four small moves the speakers lean on that most stores skip.',
                           'items': ['Retitle to the term that already converts: a winter jacket renamed '
                                     'to match its converting search term produced 20-30% more sales in '
                                     'about a week at the same ROAS [Ecom Chris — d9kULGtUBD4 @ 00:12:01]',
                                     'Always add a sale price, because the green sale price boosts clicks, '
                                     'but keep it identical to the website or the product gets suspended '
                                     '[Max Crakanthorp — H4yH9xs030Q @ 00:13:20]',
                                     'No GTIN? Create a unique MPN so Google keeps learning about the '
                                     'product instead of leaving the identifier blank [KeyCommerce — '
                                     'UcU7Ishu1lY @ 00:05:11]',
                                     'If a feed app such as Semrush or DataFeedWatch runs the catalog, '
                                     'edit inside the app, because manual Merchant Center edits get '
                                     'overridden on the next sync [KeyCommerce — S1NhYxaPnic @ 00:02:16]']},
               'sop_steps': [{'step': 1,
                              'title': 'Audit diagnostics and segment the catalog',
                              'action': 'Open Needs attention, resync if disapprovals look like a sync '
                                        'issue, then bucket products by performance.',
                              'detail': 'Check diagnostics first; a disapproval rate of about 0.3% is '
                                        'usually a sync issue, so resync, then sort products into top '
                                        'sellers, wasters, high-click/low-CVR and high-impression/low-CTR, '
                                        'leaving top sellers for last [Ecom Chris — d9kULGtUBD4 @ '
                                        '00:02:53]'},
                             {'step': 2,
                              'title': 'Rewrite titles for the top SKUs via supplemental feed',
                              'action': 'Sort by conversions, batch the top 30-50 SKUs, and push new '
                                        'titles through a supplemental feed.',
                              'detail': 'Use Brand + model + type or type + attribute + use case + brand, '
                                        'with no caps, symbols or promo text, and batch the top 30-50 SKUs '
                                        'sorted by conversions through a supplemental feed [Abdul Rauf Ali '
                                        '— V0LAr3jchLs @ 00:04:26]'},
                             {'step': 3,
                              'title': 'Build custom labels with attribute rules',
                              'action': 'Create a rule on an unused custom label, preview, save as draft, '
                                        'apply, and segment in Google Ads.',
                              'detail': 'Data sources > Content API > Attribute rules > Add rule on '
                                        'custom_label_3; if title contains Christmas OR Santa OR holiday '
                                        "set 'Christmas', check the draft value in preview, apply, and it "
                                        'goes live on the next fetch [Grow My Ads — -w0GraOv2B0 @ '
                                        '00:03:09]'},
                             {'step': 4,
                              'title': 'Launch a test promotion and lock the review cadence',
                              'action': 'Run a 10-20% test promo with an 11:59 p.m. end time, then review '
                                        'diagnostics weekly and store quality monthly.',
                              'detail': 'Set up via Settings > Add-ons > Promotions with the code already '
                                        'live in the store and the end time at 11:59 p.m. [KeyCommerce — '
                                        'jmjy6G9akyM @ 00:01:32]; run a 10-20% test promo, check '
                                        'diagnostics weekly and store quality monthly [Max Crakanthorp — '
                                        'FZOo2bNTrzo @ 00:22:03]'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The sharpest split is over what leads the title. Austin at Grow My Ads puts '
                              'household-name brands such as Nike, Apple and Samsung at the front and '
                              'pushes unknown brands to the end. He argues the first 30 to 70 characters '
                              'carry the weight, and Google may reorder words already in the title but '
                              "never adds any [hY8ZBC3A4uQ @ 00:06:04]. His Home Reserve retitle to 'kid "
                              "and pet friendly sectional sofa... washable' is the proof he points to for "
                              'the benefit-led formula: a 10x jump in clicks and impressions, with sales '
                              "rising. Kai Cromwell goes keyword-first, putting a phrase like 'leather "
                              "office chair' ahead of the brand because only about 70 of the 150 "
                              'characters are visible [W6w0BjjlBs4 @ 00:03:26]. Ecom Chris lands in the '
                              'middle. He puts the brand first only when it is strong like Nike, and '
                              'otherwise frontloads the main keyword. He also stacks attributes through '
                              'the feed rather than hardcoding them, and never stacks synonyms '
                              '[d9kULGtUBD4 @ 00:21:41]. Abdul Rauf Ali runs two templates depending on '
                              'the catalog: brand plus model plus type, or type plus attribute plus use '
                              'case plus brand. He sorts by conversions and only rewrites that slice first '
                              '[V0LAr3jchLs @ 00:02:25]. The operator call: pick the template that matches '
                              'your brand equity, then fill the visible zone with real search-term '
                              'language.',
                              'Description depth splits the room just as hard. Max Crakanthorp treats the '
                              "description as copy written 'for Google' and filled roughly 4,700 of 5,000 "
                              'characters in his live build. He drafts with an AI prompt and then strips '
                              'out irrelevant keywords [H4yH9xs030Q @ 00:06:23]. Ecom Chris says the '
                              'description matters less than the title. He wants 200 to 500 characters, '
                              'written for humans and leading with value, and warns that AI slop risks '
                              'disapproval or higher CPC [XQTEnn-3t0E @ 00:07:28]. Austin at Grow My Ads '
                              'applies an 80/20 rule: fix titles first and only write descriptions for top '
                              'products [hY8ZBC3A4uQ @ 00:22:25]. The same fault line runs through image '
                              'generation. Austin got a usable lifestyle scene from a single Nano Banana '
                              'Pro prompt and uses Product Studio for background removal, upscaling and '
                              "scene generation. KeyCommerce, by contrast, reports that Google's own "
                              "generative image tool 'hasn't been that useful' [S1NhYxaPnic @ 00:05:00]. "
                              "Both camps hold the same red line. Austin calls altering the product's look "
                              "'unethical', and he keeps the white-background main image while adding "
                              'lifestyle shots as additional images. Testing method differs too: Max '
                              'split-tests lifestyle versus plain images, either month versus month or '
                              'across products.',
                              'Tooling is the last big fork. Austin ranks Channable as the number one '
                              'pick. He positions Feedonomics as the enterprise, hands-on option for '
                              "accounts spending a 'couple hundred thousand a year to millions', and calls "
                              'DataFeedWatch the cheaper DIY route [hY8ZBC3A4uQ @ 00:29:24]. Yet in a '
                              'separate Grow My Ads tutorial, the same agency runs a Content API client '
                              'with no feed tool at all. It writes Merchant Center Next attribute rules '
                              'that tag any title containing Christmas, Santa or holiday into '
                              'custom_label_3, and rewrites sofa titles across hundreds of SKUs '
                              '[-w0GraOv2B0 @ 00:01:38]. Tim Sutton says manual label edits do not scale '
                              'to thousands of SKUs and pushes a supplemental sheet with fill-down instead '
                              '[APb0cOGKROE @ 00:02:48]. His PMax client example used price buckets from '
                              "100 to 10,000, with a '2,000+' label carrying its own tROAS. Ian at PPC "
                              'Incubator lays out three ways to populate labels side by side [79VrN9FhpT8 '
                              '@ 00:00:41]:\n'
                              '- a Google Sheet of brand tiers mapped through feed rules;\n'
                              "- a supplemental feed keyed on ID, carrying labels like 'best price + low "
                              "click + high AOV';\n"
                              "- a developer-pushed main feed carrying 'margin 25/30%'.\n"
                              'The choice is economic, not ideological. Spend level decides whether a paid '
                              'platform earns its fee. Whatever you choose, the system holding the source '
                              'of truth must be the only place edits happen.'],
               'table': {'caption': 'Competing playbooks on titles, descriptions, identifiers, imagery, '
                                    'tooling and price',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Brand position inside the Shopping product title',
                                   'Austin puts well-known brands like Nike, Apple and Samsung first and '
                                   'moves unknown brands to the end',
                                   'Kai Cromwell leads with the keyword, such as leather office chair, '
                                   'ahead of the brand name',
                                   'Grow My Ads ([hY8ZBC3A4uQ @ 00:06:04]); Kai Cromwell - eCommerce SEO '
                                   '([W6w0BjjlBs4 @ 00:03:26])'],
                                  ['How much of the 150-character title limit to use',
                                   'Max Crakanthorp filled 134 of 150 characters using product, '
                                   'description, features and benefits',
                                   'Ecom Chris runs 110 to 130 characters and says 30-character titles '
                                   'waste 120 characters',
                                   'Max Crakanthorp ([H4yH9xs030Q @ 00:06:10]); Ecom Chris ([XQTEnn-3t0E @ '
                                   '00:05:04])'],
                                  ['Description length and how much effort it deserves',
                                   'Max Crakanthorp writes the description for Google, using roughly 4,700 '
                                   'of 5,000 characters',
                                   'Ecom Chris targets 200 to 500 human-first characters and warns AI slop '
                                   'risks disapproval',
                                   'Max Crakanthorp ([H4yH9xs030Q @ 00:06:23]); Ecom Chris ([XQTEnn-3t0E @ '
                                   '00:07:28])'],
                                  ['Handling products that have no GTIN available',
                                   'Max Crakanthorp says a GTIN helps but leaving the field blank is OK',
                                   'KeyCommerce makes up a unique MPN so Google keeps learning; Abdul Rauf '
                                   'Ali never invents GTINs',
                                   'Max Crakanthorp ([H4yH9xs030Q @ 00:14:26]); KeyCommerce ([S1NhYxaPnic '
                                   '@ 00:07:44]); Abdul Rauf Ali ([V0LAr3jchLs @ 00:06:12])'],
                                  ['Generative AI tools for lifestyle product imagery',
                                   'Austin got a good lifestyle image from a single Nano Banana Pro prompt',
                                   "KeyCommerce says Google's own generative image tool hasn't been wildly "
                                   'useful in practice',
                                   'Grow My Ads ([hY8ZBC3A4uQ @ 00:16:51]); KeyCommerce ([UcU7Ishu1lY @ '
                                   '00:03:48])'],
                                  ['Feed management tooling matched to spend level',
                                   'Austin ranks Channable first, Feedonomics for big spenders and '
                                   'DataFeedWatch as cheaper DIY',
                                   'A Grow My Ads tutorial uses only Merchant Center Next attribute rules '
                                   'on a Content API feed',
                                   'Grow My Ads ([hY8ZBC3A4uQ @ 00:29:24]); Grow My Ads ([-w0GraOv2B0 @ '
                                   '00:00:00])'],
                                  ['Price positioning against competing Shopping listings',
                                   'Kai Cromwell pushes below-average prices and cheaper entry products, '
                                   'then upsells later',
                                   'Ecom Chris prices within 5 to 10 percent of the average and rejects a '
                                   'race to the bottom',
                                   'Kai Cromwell - eCommerce SEO ([W6w0BjjlBs4 @ 00:06:44]); Ecom Chris '
                                   '([XQTEnn-3t0E @ 00:15:41])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The fastest way to lose a feed is a mismatch between what Merchant Center '
                              'says and what the store shows. Max Crakanthorp always adds a sale price '
                              'because the green sale price boosts clicks. But a sale price that does not '
                              'match the website gets the product suspended [H4yH9xs030Q @ 00:13:46]. '
                              "KeyCommerce's Sam says price and availability must be changed at the "
                              'source, such as Shopify, because Google checks daily and a discrepancy '
                              'brings quick disapproval [UcU7Ishu1lY @ 00:04:19]. Austin at Grow My Ads '
                              'names the aggressive versions of the same play as suspension triggers: '
                              'price baiting, checkout hacks and fake sale prices [hY8ZBC3A4uQ @ '
                              '00:03:19]. His alternative to faking a discount is honest price '
                              'positioning, because in his words price will rule all, and a competitor 20% '
                              'cheaper beats the best feed. Wixpa adds the trap that catches new Shopify '
                              'stores: a perfect product feed does not guarantee product approval. '
                              'Contact, refund, shipping, privacy and terms pages are still required, '
                              'along with visible business details, and suspensions remain possible even '
                              'after a clean app setup [RHJvGN_6sf0 @ 00:04:47]. The rule across all four '
                              'is simple. Edit prices only where the store gets them, mirror them exactly, '
                              'and treat every sale price as a live claim that Google checks daily.',
                              'History destruction is the quiet killer. KeyCommerce warns never to change '
                              'an ID or SKU, because doing so would create a new product for Google. They '
                              'report performance dropping after IDs were changed [S1NhYxaPnic @ '
                              '00:06:21]. The same video flags a second trap. If a feed app such as '
                              'Semrush or DataFeedWatch runs the catalog, manual Merchant Center edits get '
                              'overridden on the next sync, so all work belongs in the app. Wixpa calls '
                              'the product ID format the migration trap. A new account keeps the default '
                              'format, but a store switching apps must keep its previous format or lose '
                              'its history [RHJvGN_6sf0 @ 00:02:18]. Wixpa also notes that inventory sync '
                              "runs automatically once the app is connected and that a 'Pending' status is "
                              'normal. Sync failures also masquerade as feed problems. Ecom Chris checks '
                              'diagnostics first and reads a disapproval rate around 0.3% as usually a '
                              'sync issue, fixed by a resync rather than a rewrite [d9kULGtUBD4 @ '
                              '00:02:53]. Max Crakanthorp hit the shipping version of the same bottleneck. '
                              'He tells operators to turn off the Shopify shipping sync when disapprovals '
                              'occur, then work through issues sorted by click potential, checking '
                              'diagnostics weekly and store quality monthly [FZOo2bNTrzo @ 00:11:04].',
                              'The economics checks come down to data volume and waste. Ecom Chris tests '
                              'one change per SKU and runs it for one to two weeks. He says that at $40 to '
                              '$50 a day there is not enough data, because you need a lot of budget and a '
                              'lot of data to test properly. His read on results: CTR rising while CVR '
                              'falls means the title went too broad [d9kULGtUBD4 @ 00:30:17]. In the '
                              'companion video he prices the downside of skipping the work. Poorly '
                              'optimized feeds pay CPC two to three times higher, which he tracks '
                              'alongside CTR, bounce rate, CVR and ROAS [XQTEnn-3t0E @ 00:23:16]. Abdul '
                              'Rauf Ali runs a hygiene filter over six to twelve months: ROAS above 1.9, '
                              'his breakeven, with at least 50 clicks. He gives the top performers a '
                              "custom label [V0LAr3jchLs @ 00:08:40]. Tim Sutton's PMax client goes "
                              'further on the cut side, excluding products with 100+ clicks and low ROAS '
                              "[APb0cOGKROE @ 00:05:22]. Ecom Chris also warns of 'death by "
                              "overoptimization', applying 80/20 with supplemental feeds for overrides. "
                              'The operator takeaway for small budgets: batch only proven winners, cut '
                              'proven losers on a click threshold, and resist rewriting the whole catalog '
                              'at once.'],
               'table': {'caption': 'Firsthand traps, what practitioners saw happen, and the fix or '
                                    'economics check',
                         'headers': ['Failure Mode',
                                     'What Practitioners Saw',
                                     'Fix or Economics Check',
                                     'Expert Source'],
                         'rows': [['Sale price in the feed not matching the website',
                                   'A green sale price boosts clicks, but a mismatch with the website gets '
                                   'the product suspended',
                                   'Keep the feed sale price identical to the live website price at all '
                                   'times',
                                   'Max Crakanthorp ([H4yH9xs030Q @ 00:13:46])'],
                                  ['Catalog-wide ID or SKU change during cleanup or migration',
                                   'KeyCommerce saw catalog-wide ID changes create new products and make '
                                   'performance plummet',
                                   'Never overwrite IDs; stores migrating apps keep the previous ID format '
                                   'to retain history',
                                   'KeyCommerce ([UcU7Ishu1lY @ 00:04:52]); Wixpa Google Shopping Feed '
                                   '([RHJvGN_6sf0 @ 00:02:18])'],
                                  ['Manual Merchant Center edits wiped by the feed app',
                                   'Manual edits get overridden on the next Semrush or DataFeedWatch sync',
                                   'Make every title and attribute edit inside the feed app itself',
                                   'KeyCommerce ([S1NhYxaPnic @ 00:02:16])'],
                                  ['Promotional copy stuffed into product descriptions',
                                   'Free shipping or BOGO copy inside descriptions breaks Merchant Center '
                                   'policy',
                                   'Keep descriptions to practical features and run offers through '
                                   'Merchant Center Promotions instead',
                                   'KeyCommerce ([UcU7Ishu1lY @ 00:03:31]); KeyCommerce ([jmjy6G9akyM @ '
                                   '00:00:13])'],
                                  ['Promotion ending a full day earlier than planned',
                                   'Google ends promotions at midnight the day before the chosen end date',
                                   'Set the end time to 11:59 p.m. and allow 1 to 24 hours review, longer '
                                   'near Black Friday',
                                   'KeyCommerce ([jmjy6G9akyM @ 00:01:32])'],
                                  ['Reading title tests on an underfunded daily budget',
                                   'At $40 to $50 per day there is not enough data to read a test',
                                   'Make one change per SKU for one to two weeks; CTR up with CVR down '
                                   'means too broad',
                                   'Ecom Chris ([d9kULGtUBD4 @ 00:28:56])'],
                                  ['Business identity that does not match the website',
                                   'Kai Cromwell advises a fake GMB as part of his high-ticket niche '
                                   'playbook',
                                   'Max Crakanthorp reports business info mismatches with the website lead '
                                   'to misrepresentation bans',
                                   'Kai Cromwell - eCommerce SEO ([61mBGqDsSo4 @ 00:06:46]); Max '
                                   'Crakanthorp ([FZOo2bNTrzo @ 00:08:23])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Four checks before you push a feed change live',
                           'body': 'Each check maps to a suspension, a loss of product history, or wasted '
                                   'spend that practitioners hit firsthand.',
                           'items': ['Audit every sale price against the live site before it syncs, '
                                     'because a mismatch with the website gets the product suspended [Max '
                                     'Crakanthorp — H4yH9xs030Q @ 00:13:46].',
                                     'Lock product IDs before any cleanup or app migration, because a '
                                     'changed ID creates a new product for Google and performance drops '
                                     '[KeyCommerce — S1NhYxaPnic @ 00:06:21].',
                                     'Confirm the contact, refund, shipping, privacy and terms pages are '
                                     'live and business details are visible, because a perfect feed does '
                                     'not guarantee approval [Wixpa Google Shopping Feed — RHJvGN_6sf0 @ '
                                     '00:04:47].',
                                     'Do not read a title test without enough budget: make one change per '
                                     'SKU for one to two weeks, and know that $40 to $50 a day is not '
                                     'enough data [Ecom Chris — d9kULGtUBD4 @ 00:28:56].']}}],
 'pull_quote': '"If your shopping or performance max feels random, it\'s usually not your bidding, it\'s '
               'your product data." — Ecom Chris (XQTEnn-3t0E @ 00:00:00).',
 'diagram_id': 'diag-06',
 'action_checklist': ['Open Diagnostics first and treat a disapproval rate around 0.3% as a sync issue to '
                      'fix with a resync, not a rewrite [Ecom Chris — d9kULGtUBD4 @ 00:02:53].',
                      'Sort products by conversions and push retitles for the top 30 to 50 SKUs through a '
                      'supplemental feed [Abdul Rauf Ali — V0LAr3jchLs @ 00:04:26].',
                      'Mine the Google Ads search terms report first for title modifiers, before '
                      'autocomplete, competitor listings or tools [Ecom Chris — d9kULGtUBD4 @ 00:10:53].',
                      'Move each product into the most specific fitting Google product category path, as '
                      'with garment shields to Clothing & Closet Storage [Jyll Saskin Gales | Google Ads '
                      'Coach — Q-KrwvAVhR4 @ 00:01:00].',
                      'Build a seasonal custom label with an attribute rule, such as title contains '
                      'Christmas, Santa or holiday set to Christmas, then preview before applying [Grow My '
                      'Ads — -w0GraOv2B0 @ 00:03:09].',
                      'Launch a free shipping promotion as the starting point, matching the selected speed '
                      'to your shipping settings and setting the end time to 11:59 p.m. [KeyCommerce — '
                      'jmjy6G9akyM @ 00:03:44].'],
 'statutory_citations': [{'title': 'Grow My Ads — Google Shopping Feed Optimizations for 10X Growth (2026 '
                                   'Updated) [00:02:10]',
                          'url': 'https://www.youtube.com/watch?v=hY8ZBC3A4uQ&t=130s',
                          'relevance': 'Primary practitioner testimony on price as the top lever, '
                                       'suspension risk from fake sale prices, and title retitling that '
                                       'drove a 10x click lift.'},
                         {'title': 'Ecom Chris — Ultimate Guide to Google Shopping Feed Optimization: '
                                   'Increase CTR, Conversions & ROAS [00:28:56]',
                          'url': 'https://www.youtube.com/watch?v=d9kULGtUBD4&t=1736s',
                          'relevance': 'Primary practitioner testimony on single-variable title testing, '
                                       'minimum budget for valid data, and overoptimization risk.'},
                         {'title': 'KeyCommerce — How To Optimize Your Product Feed & Data In Google '
                                   'Merchant Center [00:06:21]',
                          'url': 'https://www.youtube.com/watch?v=S1NhYxaPnic&t=381s',
                          'relevance': 'Primary practitioner testimony on ID changes destroying product '
                                       'history and feed app syncs overriding manual edits.'},
                         {'title': 'Max Crakanthorp — Set Up Google Merchant Center The Right Way (Full '
                                   'Course) [00:08:23]',
                          'url': 'https://www.youtube.com/watch?v=FZOo2bNTrzo&t=503s',
                          'relevance': 'Primary practitioner testimony on misrepresentation bans from '
                                       'business info mismatches and Shopify shipping sync disapprovals.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'hY8ZBC3A4uQ',
                       'title': 'Google Shopping Feed Optimizations for 10X Growth (2026 Updated)',
                       'channel': 'Grow My Ads',
                       'author': 'Grow My Ads',
                       'text': 'Retitling the Alley sofa to a kid and pet friendly washable sectional sofa '
                               'produced a 10x jump in clicks and impressions, and sales rose.',
                       'tip': 'Retitling the Alley sofa to a kid and pet friendly washable sectional sofa '
                              'produced a 10x jump in clicks and impressions, and sales rose.',
                       'timestamp': 645,
                       'timestamp_seconds': 645,
                       'timestamp_label': '[00:10:45]',
                       'url': 'https://www.youtube.com/watch?v=hY8ZBC3A4uQ&t=645s',
                       'markdown': '[00:10:45](https://www.youtube.com/watch?v=hY8ZBC3A4uQ&t=645s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'hY8ZBC3A4uQ',
                       'title': 'Google Shopping Feed Optimizations for 10X Growth (2026 Updated)',
                       'channel': 'Grow My Ads',
                       'author': 'Grow My Ads',
                       'text': 'Price baiting, checkout hacks and fake sale prices can get you suspended.',
                       'tip': 'Price baiting, checkout hacks and fake sale prices can get you suspended.',
                       'timestamp': 199,
                       'timestamp_seconds': 199,
                       'timestamp_label': '[00:03:19]',
                       'url': 'https://www.youtube.com/watch?v=hY8ZBC3A4uQ&t=199s',
                       'markdown': '[00:03:19](https://www.youtube.com/watch?v=hY8ZBC3A4uQ&t=199s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'jmjy6G9akyM',
                       'title': 'How to Run Promotions in Merchant Center for Google Shopping',
                       'channel': 'KeyCommerce',
                       'author': 'KeyCommerce',
                       'text': 'Google ends promotions at midnight the day before, so set the end time to '
                               '11:59 p.m.',
                       'tip': 'Google ends promotions at midnight the day before, so set the end time to '
                              '11:59 p.m.',
                       'timestamp': 92,
                       'timestamp_seconds': 92,
                       'timestamp_label': '[00:01:32]',
                       'url': 'https://www.youtube.com/watch?v=jmjy6G9akyM&t=92s',
                       'markdown': '[00:01:32](https://www.youtube.com/watch?v=jmjy6G9akyM&t=92s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'S1NhYxaPnic',
                       'title': 'How To Optimize Your Product Feed & Data In Google Merchant Center',
                       'channel': 'KeyCommerce',
                       'author': 'KeyCommerce',
                       'text': 'Doing so would create a new product for Google.',
                       'tip': 'Doing so would create a new product for Google.',
                       'timestamp': 381,
                       'timestamp_seconds': 381,
                       'timestamp_label': '[00:06:21]',
                       'url': 'https://www.youtube.com/watch?v=S1NhYxaPnic&t=381s',
                       'markdown': '[00:06:21](https://www.youtube.com/watch?v=S1NhYxaPnic&t=381s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'W6w0BjjlBs4',
                       'title': 'How to Increase Organic Revenue with Google Merchant Center Optimization '
                                '(Full Guide)',
                       'channel': 'Kai Cromwell - eCommerce SEO',
                       'author': 'Kai Cromwell - eCommerce SEO',
                       'text': 'The average e-commerce CPA is $45.2, and free listings can take it to '
                               'zero.',
                       'tip': 'The average e-commerce CPA is $45.2, and free listings can take it to zero.',
                       'timestamp': 14,
                       'timestamp_seconds': 14,
                       'timestamp_label': '[00:00:14]',
                       'url': 'https://www.youtube.com/watch?v=W6w0BjjlBs4&t=14s',
                       'markdown': '[00:00:14](https://www.youtube.com/watch?v=W6w0BjjlBs4&t=14s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'H4yH9xs030Q',
                       'title': 'Live Optimizing A Product In Google Merchant Center (A - Z Guide)',
                       'channel': 'Max Crakanthorp',
                       'author': 'Max Crakanthorp',
                       'text': 'I always recommend adding sale price.',
                       'tip': 'I always recommend adding sale price.',
                       'timestamp': 800,
                       'timestamp_seconds': 800,
                       'timestamp_label': '[00:13:20]',
                       'url': 'https://www.youtube.com/watch?v=H4yH9xs030Q&t=800s',
                       'markdown': '[00:13:20](https://www.youtube.com/watch?v=H4yH9xs030Q&t=800s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Q-KrwvAVhR4',
                       'title': 'How to Optimize Product Category in Google Merchant Center | Inside '
                                'Google Ads course | Casey Gill',
                       'channel': 'Jyll Saskin Gales | Google Ads Coach',
                       'author': 'Jyll Saskin Gales | Google Ads Coach',
                       'text': "So that's going to be a much better way of optimizing that product "
                               'category.',
                       'tip': "So that's going to be a much better way of optimizing that product "
                              'category.',
                       'timestamp': 60,
                       'timestamp_seconds': 60,
                       'timestamp_label': '[00:01:00]',
                       'url': 'https://www.youtube.com/watch?v=Q-KrwvAVhR4&t=60s',
                       'markdown': '[00:01:00](https://www.youtube.com/watch?v=Q-KrwvAVhR4&t=60s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'APb0cOGKROE',
                       'title': 'How to Master Google Merchant Center Custom Labels in 5 Minutes!',
                       'channel': 'Tim Sutton | Google Ads | Launchpresso',
                       'author': 'Tim Sutton | Google Ads | Launchpresso',
                       'text': 'Price buckets run from 100 to 10,000, with a 2,000+ label carrying its own '
                               'tROAS.',
                       'tip': 'Price buckets run from 100 to 10,000, with a 2,000+ label carrying its own '
                              'tROAS.',
                       'timestamp': 306,
                       'timestamp_seconds': 306,
                       'timestamp_label': '[00:05:06]',
                       'url': 'https://www.youtube.com/watch?v=APb0cOGKROE&t=306s',
                       'markdown': '[00:05:06](https://www.youtube.com/watch?v=APb0cOGKROE&t=306s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'FZOo2bNTrzo',
                       'title': 'Set Up Google Merchant Center The Right Way (Full Course)',
                       'channel': 'Max Crakanthorp',
                       'author': 'Max Crakanthorp',
                       'text': 'Business information that does not match the website leads to '
                               'misrepresentation bans.',
                       'tip': 'Business information that does not match the website leads to '
                              'misrepresentation bans.',
                       'timestamp': 503,
                       'timestamp_seconds': 503,
                       'timestamp_label': '[00:08:23]',
                       'url': 'https://www.youtube.com/watch?v=FZOo2bNTrzo&t=503s',
                       'markdown': '[00:08:23](https://www.youtube.com/watch?v=FZOo2bNTrzo&t=503s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'XQTEnn-3t0E',
                       'title': 'Your Google Merchant Center Feed Is Losing You Sales!',
                       'channel': 'Ecom Chris',
                       'author': 'Ecom Chris',
                       'text': "If your shopping or performance max feels random, it's usually not your "
                               "bidding, it's your product data.",
                       'tip': "If your shopping or performance max feels random, it's usually not your "
                              "bidding, it's your product data.",
                       'timestamp': 0,
                       'timestamp_seconds': 0,
                       'timestamp_label': '[00:00:00]',
                       'url': 'https://www.youtube.com/watch?v=XQTEnn-3t0E&t=0s',
                       'markdown': '[00:00:00](https://www.youtube.com/watch?v=XQTEnn-3t0E&t=0s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'XQTEnn-3t0E',
                       'title': 'Your Google Merchant Center Feed Is Losing You Sales!',
                       'channel': 'Ecom Chris',
                       'author': 'Ecom Chris',
                       'text': 'What that means for you is research your competitor pricing.',
                       'tip': 'What that means for you is research your competitor pricing.',
                       'timestamp': 927,
                       'timestamp_seconds': 927,
                       'timestamp_label': '[00:15:27]',
                       'url': 'https://www.youtube.com/watch?v=XQTEnn-3t0E&t=927s',
                       'markdown': '[00:15:27](https://www.youtube.com/watch?v=XQTEnn-3t0E&t=927s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'UcU7Ishu1lY',
                       'title': 'How To Optimize Your Product Feed & Data In Google Merchant Center',
                       'channel': 'KeyCommerce',
                       'author': 'KeyCommerce',
                       'text': 'Never overwrite the ID, because that creates a new product and loses its '
                               'history.',
                       'tip': 'Never overwrite the ID, because that creates a new product and loses its '
                              'history.',
                       'timestamp': 292,
                       'timestamp_seconds': 292,
                       'timestamp_label': '[00:04:52]',
                       'url': 'https://www.youtube.com/watch?v=UcU7Ishu1lY&t=292s',
                       'markdown': '[00:04:52](https://www.youtube.com/watch?v=UcU7Ishu1lY&t=292s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '-w0GraOv2B0',
                       'title': 'How to Optimize Google Ads Shopping Feeds with Feed Attribute Rules '
                                '[Step-by-Step Tutorial]',
                       'channel': 'Grow My Ads',
                       'author': 'Grow My Ads',
                       'text': 'If the title contains Christmas, Santa or holiday, set custom label 3 to '
                               'Christmas.',
                       'tip': 'If the title contains Christmas, Santa or holiday, set custom label 3 to '
                              'Christmas.',
                       'timestamp': 189,
                       'timestamp_seconds': 189,
                       'timestamp_label': '[00:03:09]',
                       'url': 'https://www.youtube.com/watch?v=-w0GraOv2B0&t=189s',
                       'markdown': '[00:03:09](https://www.youtube.com/watch?v=-w0GraOv2B0&t=189s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'RHJvGN_6sf0',
                       'title': 'Shopify Google Merchant Center Product Feed Setup (2026) | Complete '
                                'Beginner Guide #shopify #google',
                       'channel': 'Wixpa Google Shopping Feed',
                       'author': 'Wixpa Google Shopping Feed',
                       'text': 'A perfect product feed does not guarantee product approval.',
                       'tip': 'A perfect product feed does not guarantee product approval.',
                       'timestamp': 287,
                       'timestamp_seconds': 287,
                       'timestamp_label': '[00:04:47]',
                       'url': 'https://www.youtube.com/watch?v=RHJvGN_6sf0&t=287s',
                       'markdown': '[00:04:47](https://www.youtube.com/watch?v=RHJvGN_6sf0&t=287s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'd9kULGtUBD4',
                       'title': 'Ultimate Guide to Google Shopping Feed Optimization: Increase CTR, '
                                'Conversions & ROAS',
                       'channel': 'Ecom Chris',
                       'author': 'Ecom Chris',
                       'text': 'You need a lot of budget, a lot of data to also test this properly.',
                       'tip': 'You need a lot of budget, a lot of data to also test this properly.',
                       'timestamp': 1817,
                       'timestamp_seconds': 1817,
                       'timestamp_label': '[00:30:17]',
                       'url': 'https://www.youtube.com/watch?v=d9kULGtUBD4&t=1817s',
                       'markdown': '[00:30:17](https://www.youtube.com/watch?v=d9kULGtUBD4&t=1817s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '61mBGqDsSo4',
                       'title': '5 Best High Ticket SEO Dropshipping Niches for 2025',
                       'channel': 'Kai Cromwell - eCommerce SEO',
                       'author': 'Kai Cromwell - eCommerce SEO',
                       'text': "High ticket we're defining as $1,000 or more.",
                       'tip': "High ticket we're defining as $1,000 or more.",
                       'timestamp': 25,
                       'timestamp_seconds': 25,
                       'timestamp_label': '[00:00:25]',
                       'url': 'https://www.youtube.com/watch?v=61mBGqDsSo4&t=25s',
                       'markdown': '[00:00:25](https://www.youtube.com/watch?v=61mBGqDsSo4&t=25s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'V0LAr3jchLs',
                       'title': 'Google Shopping Feed Optimization for Performance Max, 3 Fixes to improve '
                                'ROAS & Merchant centre',
                       'channel': 'Abdul Rauf Ali',
                       'author': 'Abdul Rauf Ali',
                       'text': 'Filter for ROAS above 1.9, which is breakeven, with at least 50 clicks '
                               'over six to twelve months.',
                       'tip': 'Filter for ROAS above 1.9, which is breakeven, with at least 50 clicks over '
                              'six to twelve months.',
                       'timestamp': 520,
                       'timestamp_seconds': 520,
                       'timestamp_label': '[00:08:40]',
                       'url': 'https://www.youtube.com/watch?v=V0LAr3jchLs&t=520s',
                       'markdown': '[00:08:40](https://www.youtube.com/watch?v=V0LAr3jchLs&t=520s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '79VrN9FhpT8',
                       'title': 'Google Merchant Center - Optimizing Your Feed: Custom Labels with Google '
                                'Sheets & Attribute Rules',
                       'channel': 'PPC Incubator',
                       'author': 'PPC Incubator',
                       'text': 'Custom labels can be populated from a Google Sheet, a supplemental feed, '
                               'or a developer-pushed main feed.',
                       'tip': 'Custom labels can be populated from a Google Sheet, a supplemental feed, or '
                              'a developer-pushed main feed.',
                       'timestamp': 41,
                       'timestamp_seconds': 41,
                       'timestamp_label': '[00:00:41]',
                       'url': 'https://www.youtube.com/watch?v=79VrN9FhpT8&t=41s',
                       'markdown': '[00:00:41](https://www.youtube.com/watch?v=79VrN9FhpT8&t=41s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'}]}
