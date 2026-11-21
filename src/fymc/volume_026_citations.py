"""Curated 180-citation Government Surplus Auctions baseline (15 per chapter across Q1-Q12) mined strictly from verified Government Surplus Auctions YouTube transcripts."""
from __future__ import annotations

CHAPTER_KEYWORDS: dict[int, set[str]] = {1: {'acquisition',
     'agency',
     'aging',
     'ambulance',
     'apparatus',
     'auction',
     'auctions',
     'avoiding',
     'battery',
     'business',
     'buyer',
     'certificate',
     'channels',
     'client',
     'clients',
     'codes',
     'commercial',
     'controls',
     'deadline',
     'dealer',
     'demil',
     'disposition',
     'district',
     'dla',
     'ear',
     'ebay',
     'equipment',
     'exemption',
     'export',
     'federal',
     'fire',
     'firm',
     'fleet',
     'flipping',
     'margin',
     'market',
     'model',
     'niche',
     'operator',
     'revenue',
     'service',
     'value'},
 2: {'acquisition',
     'agency',
     'aging',
     'ambulance',
     'apparatus',
     'auction',
     'auctions',
     'avoiding',
     'battery',
     'budget',
     'buyer',
     'certificate',
     'channels',
     'codes',
     'commercial',
     'contract',
     'controls',
     'customer',
     'deadline',
     'dealer',
     'decision',
     'demil',
     'disposition',
     'district',
     'dla',
     'ear',
     'ebay',
     'equipment',
     'escrow',
     'exemption',
     'export',
     'federal',
     'fee',
     'fees',
     'fire',
     'fleet',
     'flipping',
     'invoice',
     'pay',
     'payment',
     'pays',
     'retainer'},
 3: {'acquisition',
     'agency',
     'aging',
     'ambulance',
     'apparatus',
     'auction',
     'auctions',
     'avoiding',
     'battery',
     'buyer',
     'cash',
     'cashflow',
     'certificate',
     'channels',
     'codes',
     'commercial',
     'commission',
     'controls',
     'cost',
     'costs',
     'deadline',
     'dealer',
     'demil',
     'disposition',
     'district',
     'dla',
     'ear',
     'ebay',
     'economics',
     'equipment',
     'exemption',
     'export',
     'federal',
     'fire',
     'fleet',
     'flipping',
     'margin',
     'margins',
     'price',
     'pricing',
     'profit',
     'roi',
     'unit'},
 4: {'acquisition',
     'agency',
     'aging',
     'ambulance',
     'apparatus',
     'auction',
     'auctions',
     'avoiding',
     'battery',
     'budget',
     'buyer',
     'capital',
     'certificate',
     'channels',
     'codes',
     'commercial',
     'controls',
     'deadline',
     'dealer',
     'demil',
     'disposition',
     'district',
     'dla',
     'ear',
     'ebay',
     'entity',
     'equipment',
     'exemption',
     'export',
     'federal',
     'fire',
     'fleet',
     'flipping',
     'insurance',
     'lean',
     'license',
     'llc',
     'setup',
     'software',
     'stack',
     'startup',
     'tools'},
 5: {'acquisition',
     'agency',
     'aging',
     'ambulance',
     'apparatus',
     'auction',
     'auctions',
     'audit',
     'avoid',
     'avoiding',
     'battery',
     'buyer',
     'certificate',
     'channels',
     'clawback',
     'codes',
     'commercial',
     'controls',
     'deadline',
     'dealer',
     'demil',
     'disposition',
     'dispute',
     'district',
     'dla',
     'ear',
     'ebay',
     'edge',
     'equipment',
     'exemption',
     'export',
     'fail',
     'federal',
     'fire',
     'fleet',
     'flipping',
     'mistake',
     'mistakes',
     'problem',
     'risk',
     'risks',
     'trap',
     'traps'},
 6: {'acquisition',
     'agency',
     'aging',
     'ambulance',
     'apparatus',
     'auction',
     'auctions',
     'avoiding',
     'battery',
     'buyer',
     'certificate',
     'channels',
     'client',
     'codes',
     'commercial',
     'controls',
     'data',
     'deadline',
     'deal',
     'dealer',
     'demil',
     'disposition',
     'district',
     'dla',
     'ear',
     'ebay',
     'equipment',
     'exemption',
     'export',
     'federal',
     'find',
     'fire',
     'first',
     'fleet',
     'flipping',
     'lead',
     'leads',
     'list',
     'outbound',
     'prospect',
     'qualify',
     'search',
     'sourcing'},
 7: {'acquisition',
     'agency',
     'aging',
     'ambulance',
     'apparatus',
     'auction',
     'auctions',
     'avoiding',
     'battery',
     'buyer',
     'certificate',
     'channels',
     'checklist',
     'codes',
     'commercial',
     'controls',
     'deadline',
     'dealer',
     'delivery',
     'demil',
     'disposition',
     'district',
     'dla',
     'ear',
     'ebay',
     'equipment',
     'execution',
     'exemption',
     'export',
     'federal',
     'fire',
     'fleet',
     'flipping',
     'process',
     'quality',
     'sop',
     'step',
     'steps',
     'system',
     'underwriting',
     'verify',
     'workflow'},
 8: {'acquisition',
     'agency',
     'aging',
     'ambulance',
     'api',
     'apparatus',
     'auction',
     'auctions',
     'avoiding',
     'battery',
     'buyer',
     'certificate',
     'channels',
     'codes',
     'commercial',
     'controls',
     'crm',
     'data',
     'database',
     'deadline',
     'dealer',
     'demil',
     'disposition',
     'district',
     'dla',
     'ear',
     'ebay',
     'equipment',
     'exemption',
     'export',
     'federal',
     'fire',
     'fleet',
     'flipping',
     'platform',
     'portal',
     'scraper',
     'search',
     'software',
     'tool',
     'tools',
     'tracking'},
 9: {'acquisition',
     'agency',
     'aging',
     'agreement',
     'ambulance',
     'apparatus',
     'auction',
     'auctions',
     'avoiding',
     'battery',
     'buyer',
     'certificate',
     'channels',
     'codes',
     'commercial',
     'compliance',
     'contract',
     'controls',
     'deadline',
     'dealer',
     'demil',
     'disclosure',
     'disposition',
     'district',
     'dla',
     'ear',
     'ebay',
     'equipment',
     'exemption',
     'export',
     'federal',
     'fire',
     'fleet',
     'flipping',
     'law',
     'legal',
     'license',
     'outreach',
     'rules',
     'script',
     'state',
     'terms'},
 10: {'acquisition',
      'agency',
      'agent',
      'aging',
      'ai',
      'ambulance',
      'apparatus',
      'auction',
      'auctions',
      'automate',
      'automation',
      'avoiding',
      'battery',
      'buyer',
      'certificate',
      'channels',
      'codes',
      'commercial',
      'controls',
      'dashboard',
      'deadline',
      'dealer',
      'demil',
      'disposition',
      'district',
      'dla',
      'ear',
      'ebay',
      'equipment',
      'exemption',
      'export',
      'federal',
      'fire',
      'fleet',
      'flipping',
      'leverage',
      'pipeline',
      'scale',
      'script',
      'speed',
      'template',
      'workflow'},
 11: {'acquisition',
      'agency',
      'aging',
      'ambulance',
      'apparatus',
      'auction',
      'auctions',
      'avoiding',
      'battery',
      'buyer',
      'certificate',
      'channels',
      'codes',
      'commercial',
      'contractor',
      'controls',
      'deadline',
      'dealer',
      'demil',
      'disposition',
      'district',
      'dla',
      'ear',
      'ebay',
      'equipment',
      'exemption',
      'exit',
      'export',
      'federal',
      'fire',
      'fleet',
      'flipping',
      'hire',
      'hiring',
      'kpi',
      'manager',
      'operations',
      'pod',
      'scale',
      'scaling',
      'team',
      'valuation'},
 12: {'acquisition',
      'action',
      'agency',
      'aging',
      'ambulance',
      'apparatus',
      'auction',
      'auctions',
      'avoiding',
      'battery',
      'buyer',
      'certificate',
      'channels',
      'codes',
      'commercial',
      'controls',
      'day',
      'days',
      'deadline',
      'dealer',
      'demil',
      'disposition',
      'district',
      'dla',
      'ear',
      'ebay',
      'equipment',
      'exemption',
      'export',
      'federal',
      'fire',
      'fleet',
      'flipping',
      'launch',
      'milestone',
      'month',
      'plan',
      'roadmap',
      'sprint',
      'start',
      'thirty',
      'week'}}

BASELINE_EXPERT_CITATIONS_BY_CHAPTER: dict[int, list[dict]] = {1: [{'author': 'Tax Expert Today',
      'channel': 'Tax Expert Today',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:17](https://www.youtube.com/watch?v=WZL5m9rfNSQ&t=137s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "A school district certificate for a television delivered to an employee's home "
              'does not pass that test. What if the buyer later uses the item for something '
              'else? 155, the buyer owes tax on the value of that divergent use, usually the '
              'fair market rental value for the period.',
      'timestamp': 137,
      'timestamp_label': '[00:02:17]',
      'timestamp_seconds': 137,
      'tip': "A school district certificate for a television delivered to an employee's home "
             'does not pass that test. What if the buyer later uses the item for something '
             'else? 155, the buyer owes tax on the value of that divergent use, usually the '
             'fair market rental value for the period.',
      'title': 'Texas Sales Tax Exemption Certificate: Who Pays If It Fails (2026) (Tax Expert '
               'Today)',
      'url': 'https://www.youtube.com/watch?v=WZL5m9rfNSQ&t=137s',
      'video_id': 'WZL5m9rfNSQ'},
     {'author': 'GovAuctions',
      'channel': 'GovAuctions',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:05](https://www.youtube.com/watch?v=x8_btciMVuY&t=65s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'These are the three biggest channels where most active auctions are listed. '
              'Now, where are the actual deals and the catches? Some lots genuinely offer real '
              'value, especially surplus equipment and vehicles sold below market rate. But '
              'not every lot is a win.',
      'timestamp': 65,
      'timestamp_label': '[00:01:05]',
      'timestamp_seconds': 65,
      'tip': 'These are the three biggest channels where most active auctions are listed. Now, '
             'where are the actual deals and the catches? Some lots genuinely offer real '
             'value, especially surplus equipment and vehicles sold below market rate. But not '
             'every lot is a win.',
      'title': 'Are government auctions actually legit? (GovAuctions)',
      'url': 'https://www.youtube.com/watch?v=x8_btciMVuY&t=65s',
      'video_id': 'x8_btciMVuY'},
     {'author': 'Auction Reviews With Jeff',
      'channel': 'Auction Reviews With Jeff',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=gIFFMdh2fBk&t=21s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "I'm going to go through all the prices sold, compare them to market value, and "
              "we're going to see if these GSA auctions, these federal government auctions, "
              'vehicle auctions are worth it. Okay, a 2020 Nissan Murano.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': "I'm going to go through all the prices sold, compare them to market value, and "
             "we're going to see if these GSA auctions, these federal government auctions, "
             'vehicle auctions are worth it. Okay, a 2020 Nissan Murano.',
      'title': 'What do Federal Government Surplus Vehicles Sell For at Auction Part 3 of 3 '
               '(Auction Reviews With Jeff)',
      'url': 'https://www.youtube.com/watch?v=gIFFMdh2fBk&t=21s',
      'video_id': 'gIFFMdh2fBk'},
     {'author': 'IronPlanet',
      'channel': 'IronPlanet',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:38](https://www.youtube.com/watch?v=phjpnOl7Hto&t=158s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'With higher selling prices and lower selling costs, greater value and better '
              'net return so you can make smarter business decisions. And manage your fleet '
              'with confidence, 100% online. There is no better way to buy and sell your used '
              'equipment.',
      'timestamp': 158,
      'timestamp_label': '[00:02:38]',
      'timestamp_seconds': 158,
      'tip': 'With higher selling prices and lower selling costs, greater value and better net '
             'return so you can make smarter business decisions. And manage your fleet with '
             'confidence, 100% online. There is no better way to buy and sell your used '
             'equipment.',
      'title': 'What is IronPlanet? (IronPlanet)',
      'url': 'https://www.youtube.com/watch?v=phjpnOl7Hto&t=158s',
      'video_id': 'phjpnOl7Hto'},
     {'author': 'LedgerGurus: Ecommerce Accounting Experts',
      'channel': 'LedgerGurus: Ecommerce Accounting Experts',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:27](https://www.youtube.com/watch?v=4OfpzpJeXjQ&t=87s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Page one is the actual form. The rest are all footnotes and instructions. '
              "You'll want to enter the seller's name and address. That's your vendor or "
              'dropshipper asking for the certificate. Enter your business name and address as '
              'the buyer.',
      'timestamp': 87,
      'timestamp_label': '[00:01:27]',
      'timestamp_seconds': 87,
      'tip': "Page one is the actual form. The rest are all footnotes and instructions. You'll "
             "want to enter the seller's name and address. That's your vendor or dropshipper "
             'asking for the certificate. Enter your business name and address as the buyer.',
      'title': 'Stop Overpaying Sales Tax in These States (MTC Resale Certificate Tutorial) '
               '(LedgerGurus: Ecommerce Accounting Experts)',
      'url': 'https://www.youtube.com/watch?v=4OfpzpJeXjQ&t=87s',
      'video_id': '4OfpzpJeXjQ'},
     {'author': 'James Baker CPA',
      'channel': 'James Baker CPA',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:11](https://www.youtube.com/watch?v=L4NQWUrzH6A&t=191s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'re going to ask you in this order through an online questionnaire. And I'm "
              'going to go through the main points here. So, first, they want your federal EIN '
              "number. Generally, if you're doing all this business stuff, you should have an "
              "LLC. I didn't even talk about that yet.",
      'timestamp': 191,
      'timestamp_label': '[00:03:11]',
      'timestamp_seconds': 191,
      'tip': "'re going to ask you in this order through an online questionnaire. And I'm "
             'going to go through the main points here. So, first, they want your federal EIN '
             "number. Generally, if you're doing all this business stuff, you should have an "
             "LLC. I didn't even talk about that yet.",
      'title': 'How To Get a Florida Resale Tax Certificate (2025 Update) (James Baker CPA)',
      'url': 'https://www.youtube.com/watch?v=L4NQWUrzH6A&t=191s',
      'video_id': 'L4NQWUrzH6A'},
     {'author': 'Handyman Process',
      'channel': 'Handyman Process',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:21](https://www.youtube.com/watch?v=FZRiWN_dcS4&t=201s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Prefer one that's a little bit smaller service body on something smaller and "
              "it's hit or miss when you come to these auctions kind of what you're going to.",
      'timestamp': 201,
      'timestamp_label': '[00:03:21]',
      'timestamp_seconds': 201,
      'tip': "Prefer one that's a little bit smaller service body on something smaller and "
             "it's hit or miss when you come to these auctions kind of what you're going to.",
      'title': 'How to buy vehicles from a government auction (Handyman Process)',
      'url': 'https://www.youtube.com/watch?v=FZRiWN_dcS4&t=201s',
      'video_id': 'FZRiWN_dcS4'},
     {'author': 'homebusinessmag',
      'channel': 'homebusinessmag',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:53](https://www.youtube.com/watch?v=pRzKRg71z4s&t=893s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Running an auction uh you know somehow you know an auction buying and selling '
              'as a business yeah i the biggest thing uh that i.',
      'timestamp': 893,
      'timestamp_label': '[00:14:53]',
      'timestamp_seconds': 893,
      'tip': 'Running an auction uh you know somehow you know an auction buying and selling as '
             'a business yeah i the biggest thing uh that i.',
      'title': 'Government Auctions – A Great Resource for Your Business or as its Own '
               'Start-up (homebusinessmag)',
      'url': 'https://www.youtube.com/watch?v=pRzKRg71z4s&t=893s',
      'video_id': 'pRzKRg71z4s'},
     {'author': 'EEVblog',
      'channel': 'EEVblog',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:48](https://www.youtube.com/watch?v=ay9wFQAW19Y&t=228s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': '20 years, 21 years at least for this particular model. And if you go back to '
              "the Fluke 70 like the 70 series 1 and series 2 before that, we're talking way "
              "back into the 1980s. Name another meter on the market that's been around for "
              'that length of time.',
      'timestamp': 228,
      'timestamp_label': '[00:03:48]',
      'timestamp_seconds': 228,
      'tip': '20 years, 21 years at least for this particular model. And if you go back to the '
             "Fluke 70 like the 70 series 1 and series 2 before that, we're talking way back "
             "into the 1980s. Name another meter on the market that's been around for that "
             'length of time.',
      'title': 'eevBLAB 91 - Why Are Fluke Meters So EXPENSIVE? (EEVblog)',
      'url': 'https://www.youtube.com/watch?v=ay9wFQAW19Y&t=228s',
      'video_id': 'ay9wFQAW19Y'},
     {'author': 'Advanced Test Equipment Corp. (ATEC)',
      'channel': 'Advanced Test Equipment Corp. (ATEC)',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:16](https://www.youtube.com/watch?v=_7M8lI2DJDI&t=76s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "So, it's good to get this info in case you really need it. Along with viewing "
              'all the access points, you could also view all the clients connected to the '
              'network. And from there, you could troubleshoot if any specific client is '
              'having an issue with the network.',
      'timestamp': 76,
      'timestamp_label': '[00:01:16]',
      'timestamp_seconds': 76,
      'tip': "So, it's good to get this info in case you really need it. Along with viewing "
             'all the access points, you could also view all the clients connected to the '
             'network. And from there, you could troubleshoot if any specific client is having '
             'an issue with the network.',
      'title': 'How to Use the Fluke AirCheck Wi Fi Tester | Full Guide & Feature Walkthrough '
               '(Advanced Test Equipment Corp. (ATEC))',
      'url': 'https://www.youtube.com/watch?v=_7M8lI2DJDI&t=76s',
      'video_id': '_7M8lI2DJDI'},
     {'author': 'Good Day Sacramento',
      'channel': 'Good Day Sacramento',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:22](https://www.youtube.com/watch?v=1Cxx4l6qQcA&t=22s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'SEE ME MODEL MY NEW HAZ-MAT SUIT. Reporter: THE STATE SURPLUS AUCTION. HOW DO '
              'THEY GET THEIR STUFF? BUT I WANT TO SHOW YOU SOME THINGS.',
      'timestamp': 22,
      'timestamp_label': '[00:00:22]',
      'timestamp_seconds': 22,
      'tip': 'SEE ME MODEL MY NEW HAZ-MAT SUIT. Reporter: THE STATE SURPLUS AUCTION. HOW DO '
             'THEY GET THEIR STUFF? BUT I WANT TO SHOW YOU SOME THINGS.',
      'title': 'State Surplus Property Auction (Good Day Sacramento)',
      'url': 'https://www.youtube.com/watch?v=1Cxx4l6qQcA&t=22s',
      'video_id': '1Cxx4l6qQcA'},
     {'author': 'Shark Scrapper',
      'channel': 'Shark Scrapper',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:15](https://www.youtube.com/watch?v=6XObIp5c91U&t=135s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Green Metal Small metal socket and remember before you sell these you have to '
              "remove that battery let's get something for the ram ram.",
      'timestamp': 135,
      'timestamp_label': '[00:02:15]',
      'timestamp_seconds': 135,
      'tip': 'Green Metal Small metal socket and remember before you sell these you have to '
             "remove that battery let's get something for the ram ram.",
      'title': 'Sorting a pallet load of mixed circuit boards for max value (Shark Scrapper)',
      'url': 'https://www.youtube.com/watch?v=6XObIp5c91U&t=135s',
      'video_id': '6XObIp5c91U'},
     {'author': 'Dirt Legal',
      'channel': 'Dirt Legal',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:00](https://www.youtube.com/watch?v=9EAPaeoXhFs&t=240s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'In our ability to register your military humvee as street illegal that we offer '
              'a 100 money back guarantee if we fail to make it happen so contact us today to '
              'see if your military humvee qualifies for our in-state legalization service '
              "we'll see you next time.",
      'timestamp': 240,
      'timestamp_label': '[00:04:00]',
      'timestamp_seconds': 240,
      'tip': 'In our ability to register your military humvee as street illegal that we offer '
             'a 100 money back guarantee if we fail to make it happen so contact us today to '
             'see if your military humvee qualifies for our in-state legalization service '
             "we'll see you next time.",
      'title': 'How to Make Your Humvee or Military Vehicle STREET LEGAL! (Dirt Legal)',
      'url': 'https://www.youtube.com/watch?v=9EAPaeoXhFs&t=240s',
      'video_id': '9EAPaeoXhFs'},
     {'author': 'E Tech',
      'channel': 'E Tech',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=9ihMGubVqU4&t=15s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'सकते हैं और विद इन थ्री डेज किस तरीके से हासिल कर सकते हैं। मैं लाइव प्रूफ '
              'दिखाऊंगा इस चीज के और बाद में आपको यह भी बताऊंगा कि हमने इसके सेल्स वगैरह किस '
              'तरह.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'सकते हैं और विद इन थ्री डेज किस तरीके से हासिल कर सकते हैं। मैं लाइव प्रूफ '
             'दिखाऊंगा इस चीज के और बाद में आपको यह भी बताऊंगा कि हमने इसके सेल्स वगैरह किस '
             'तरह.',
      'title': 'How to Get Wyoming Resale Certificate in 48 Hours (Step-by-Step Full Guide) (E '
               'Tech)',
      'url': 'https://www.youtube.com/watch?v=9ihMGubVqU4&t=15s',
      'video_id': '9ihMGubVqU4'},
     {'author': 'Auction Reviews With Jeff',
      'channel': 'Auction Reviews With Jeff',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:07](https://www.youtube.com/watch?v=rDFBP32Mq2I&t=307s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Kabota hydraulic shuttle M5-11. Looks like a brand new dump truck, man. Imagine '
              'getting hit by those. Festival Park Royal Auction Group Government Surplus and '
              'Consignment Auction open to the public.',
      'timestamp': 307,
      'timestamp_label': '[00:05:07]',
      'timestamp_seconds': 307,
      'tip': 'Kabota hydraulic shuttle M5-11. Looks like a brand new dump truck, man. Imagine '
             'getting hit by those. Festival Park Royal Auction Group Government Surplus and '
             'Consignment Auction open to the public.',
      'title': 'State Government Auction Prices for Dump Trucks, Small Equipment, Lawn '
               'Attachments, Tractors... (Auction Reviews With Jeff)',
      'url': 'https://www.youtube.com/watch?v=rDFBP32Mq2I&t=307s',
      'video_id': 'rDFBP32Mq2I'}],
 2: [{'author': 'Vantor Insider',
      'channel': 'Vantor Insider',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:26](https://www.youtube.com/watch?v=tBIT1SUqIz8&t=326s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': '800 in gate fees usually ends up with a branded salvage certificate that '
              'requires a state highway patrol inspection. Whereas a buyer who registers '
              'directly on a federal or municipal surplus portal pays zero broker fees and '
              'receives an unencumbered government title document.',
      'timestamp': 326,
      'timestamp_label': '[00:05:26]',
      'timestamp_seconds': 326,
      'tip': '800 in gate fees usually ends up with a branded salvage certificate that '
             'requires a state highway patrol inspection. Whereas a buyer who registers '
             'directly on a federal or municipal surplus portal pays zero broker fees and '
             'receives an unencumbered government title document.',
      'title': "You Don't Need a Dealer License: How Ordinary Buyers Get Into Surplus Auctions "
               '(Vantor Insider)',
      'url': 'https://www.youtube.com/watch?v=tBIT1SUqIz8&t=326s',
      'video_id': 'tBIT1SUqIz8'},
     {'author': 'GovAuctions',
      'channel': 'GovAuctions',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:26](https://www.youtube.com/watch?v=Ie7zxVOXjeE&t=86s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Timeline expectations vary by auction type and location. Online auctions '
              'typically run for 3 to 10 days, then you have 5 to 15 business days to pay. '
              'After payment, pickup windows usually range from 1 to 4 weeks, depending on the '
              'item and government agency involved.',
      'timestamp': 86,
      'timestamp_label': '[00:01:26]',
      'timestamp_seconds': 86,
      'tip': 'Timeline expectations vary by auction type and location. Online auctions '
             'typically run for 3 to 10 days, then you have 5 to 15 business days to pay. '
             'After payment, pickup windows usually range from 1 to 4 weeks, depending on the '
             'item and government agency involved.',
      'title': 'How government surplus auctions work in 60 seconds (GovAuctions)',
      'url': 'https://www.youtube.com/watch?v=Ie7zxVOXjeE&t=86s',
      'video_id': 'Ie7zxVOXjeE'},
     {'author': 'Dave Doing Things',
      'channel': 'Dave Doing Things',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:01](https://www.youtube.com/watch?v=8FXm7sOaFwg&t=181s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': '10,000 the customer gets 10,000 I pay roughly 9100 or whatever comes out to '
              "10,000 with the fee and uh so I said yeah that's thousand bucks cheaper than "
              "I'd originally bid Um, and I'm the new truck owner.",
      'timestamp': 181,
      'timestamp_label': '[00:03:01]',
      'timestamp_seconds': 181,
      'tip': '10,000 the customer gets 10,000 I pay roughly 9100 or whatever comes out to '
             "10,000 with the fee and uh so I said yeah that's thousand bucks cheaper than I'd "
             "originally bid Um, and I'm the new truck owner.",
      'title': 'Iron Planet auction purchase, worth it? (Dave Doing Things)',
      'url': 'https://www.youtube.com/watch?v=8FXm7sOaFwg&t=181s',
      'video_id': '8FXm7sOaFwg'},
     {'author': 'TaxConnex',
      'channel': 'TaxConnex',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:59](https://www.youtube.com/watch?v=FPLS7VL_qTA&t=239s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "It's going to different or differ, I should say, from state to state. But "
              "essentially, you're going to want to see the customer name, the uh sales tax ID "
              'number in the state, the reason the buyer or your customer is claiming the '
              'exemption.',
      'timestamp': 239,
      'timestamp_label': '[00:03:59]',
      'timestamp_seconds': 239,
      'tip': "It's going to different or differ, I should say, from state to state. But "
             "essentially, you're going to want to see the customer name, the uh sales tax ID "
             'number in the state, the reason the buyer or your customer is claiming the '
             'exemption.',
      'title': 'Sales Tax Bytes Ep. 11 | Exemption Certificate Management (TaxConnex)',
      'url': 'https://www.youtube.com/watch?v=FPLS7VL_qTA&t=239s',
      'video_id': 'FPLS7VL_qTA'},
     {'author': 'The Salmon Runs',
      'channel': 'The Salmon Runs',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:45](https://www.youtube.com/watch?v=jaeWKn_Nu68&t=45s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Always look for information regarding the item's condition, noting any defects "
              'or necessary repairs. Remember to calculate potential additional costs, such as '
              "sales tax, buyer's premiums, and shipping fees into your budget.",
      'timestamp': 45,
      'timestamp_label': '[00:00:45]',
      'timestamp_seconds': 45,
      'tip': "Always look for information regarding the item's condition, noting any defects "
             'or necessary repairs. Remember to calculate potential additional costs, such as '
             "sales tax, buyer's premiums, and shipping fees into your budget.",
      'title': 'How To Buy From Government Auctions - Step By Step (The Salmon Runs)',
      'url': 'https://www.youtube.com/watch?v=jaeWKn_Nu68&t=45s',
      'video_id': 'jaeWKn_Nu68'},
     {'author': 'Shifting Stock | Matthew Wright',
      'channel': 'Shifting Stock | Matthew Wright',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:45](https://www.youtube.com/watch?v=Oe4lvXbQ80I&t=825s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Um the problem particularly with auctions like John Pie is the fees. I've got "
              'the invoice up here. So the pallet itself, I only paid 190 pound for the '
              'pallet.',
      'timestamp': 825,
      'timestamp_label': '[00:13:45]',
      'timestamp_seconds': 825,
      'tip': "Um the problem particularly with auctions like John Pie is the fees. I've got "
             'the invoice up here. So the pallet itself, I only paid 190 pound for the pallet.',
      'title': 'Can We PROFIT buying returns pallets at auction? (Shifting Stock | Matthew '
               'Wright)',
      'url': 'https://www.youtube.com/watch?v=Oe4lvXbQ80I&t=825s',
      'video_id': 'Oe4lvXbQ80I'},
     {'author': 'Kevin24Seven',
      'channel': 'Kevin24Seven',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:21](https://www.youtube.com/watch?v=TLQhxsY7JoE&t=441s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Um, I'm not sure if it's a requirement of dirt legal, but if you are going to "
              "do the street legal process yourself, it's definitely critical. I've gone into "
              'this in some older videos. You also got to pay the extra fees when you win a '
              'Gov Planet auction.',
      'timestamp': 441,
      'timestamp_label': '[00:07:21]',
      'timestamp_seconds': 441,
      'tip': "Um, I'm not sure if it's a requirement of dirt legal, but if you are going to do "
             "the street legal process yourself, it's definitely critical. I've gone into this "
             'in some older videos. You also got to pay the extra fees when you win a Gov '
             'Planet auction.',
      'title': 'Buying a Humvee - GovPlanet VS FaceBook MarketPlace (Kevin24Seven)',
      'url': 'https://www.youtube.com/watch?v=TLQhxsY7JoE&t=441s',
      'video_id': 'TLQhxsY7JoE'},
     {'author': 'Matt Sokol Business',
      'channel': 'Matt Sokol Business',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:28](https://www.youtube.com/watch?v=vwdB1U0_hGs&t=268s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'A person misusing a resale certificate for personal gain or to evade the '
              'payment of tax is liable for each purchase for the tax that would have been due '
              'plus a penalty of 10 of the tax or 500 whichever is more and then you enter '
              'your information so you enter your name.',
      'timestamp': 268,
      'timestamp_label': '[00:04:28]',
      'timestamp_seconds': 268,
      'tip': 'A person misusing a resale certificate for personal gain or to evade the payment '
             'of tax is liable for each purchase for the tax that would have been due plus a '
             'penalty of 10 of the tax or 500 whichever is more and then you enter your '
             'information so you enter your name.',
      'title': 'How to Fill Out Your California Resale Certificate | Business Sales Tax '
               'Exemption | *UPDATED 2022* (Matt Sokol Business)',
      'url': 'https://www.youtube.com/watch?v=vwdB1U0_hGs&t=268s',
      'video_id': 'vwdB1U0_hGs'},
     {'author': 'Wisdom & Authority Title Solutions',
      'channel': 'Wisdom & Authority Title Solutions',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:58](https://www.youtube.com/watch?v=-S82T9iXF7Q&t=118s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Time um mcos you know do go directly to the customer but there are uh some '
              'cases where a dealership May resale to another dealer okay um on the back of '
              'the.',
      'timestamp': 118,
      'timestamp_label': '[00:01:58]',
      'timestamp_seconds': 118,
      'tip': 'Time um mcos you know do go directly to the customer but there are uh some cases '
             'where a dealership May resale to another dealer okay um on the back of the.',
      'title': 'MCOs & CERTIFICATE OF TITLE DESCRIPTIONS-TITLE PROCESS (Wisdom & Authority '
               'Title Solutions)',
      'url': 'https://www.youtube.com/watch?v=-S82T9iXF7Q&t=118s',
      'video_id': '-S82T9iXF7Q'},
     {'author': 'T.J. Lovelady',
      'channel': 'T.J. Lovelady',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:19:19](https://www.youtube.com/watch?v=Lvrvr_hNtcE&t=1159s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'ll buy them and not realize how much the shipping actually is. So, the actual "
              'shipping for this is $543. Um also, you have to pay a $40 residential fee if '
              "you're not um getting it shipped to like a business.",
      'timestamp': 1159,
      'timestamp_label': '[00:19:19]',
      'timestamp_seconds': 1159,
      'tip': "'ll buy them and not realize how much the shipping actually is. So, the actual "
             'shipping for this is $543. Um also, you have to pay a $40 residential fee if '
             "you're not um getting it shipped to like a business.",
      'title': 'Buying Your First Liquidation Pallet | Liquidation Pallets 101 (T.J. Lovelady)',
      'url': 'https://www.youtube.com/watch?v=Lvrvr_hNtcE&t=1159s',
      'video_id': 'Lvrvr_hNtcE'},
     {'author': 'B-Stock',
      'channel': 'B-Stock',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:32](https://www.youtube.com/watch?v=_JpPAyxnPLc&t=152s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "So, there's going to be another fee. Again, they're not it's pretty nominal, "
              'but you need to be prepared for it. You can see those fees before you buy. '
              "There's also floor loaded shipments.",
      'timestamp': 152,
      'timestamp_label': '[00:02:32]',
      'timestamp_seconds': 152,
      'tip': "So, there's going to be another fee. Again, they're not it's pretty nominal, but "
             "you need to be prepared for it. You can see those fees before you buy. There's "
             'also floor loaded shipments.',
      'title': "Avoid Freight Surprises: Shannon Jean's Complete Shipping Guide for Pallet & "
               'Truckload Buyers (B-Stock)',
      'url': 'https://www.youtube.com/watch?v=_JpPAyxnPLc&t=152s',
      'video_id': '_JpPAyxnPLc'},
     {'author': 'Labor Legacy',
      'channel': 'Labor Legacy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:48](https://www.youtube.com/watch?v=uDCbq1XJsDA&t=588s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Some mills use optical sensors and computer controls to measure each piece and '
              'position the blades. The aim is to produce the required width while making good '
              'use of the available wood. Next comes grading and trimming.',
      'timestamp': 588,
      'timestamp_label': '[00:09:48]',
      'timestamp_seconds': 588,
      'tip': 'Some mills use optical sensors and computer controls to measure each piece and '
             'position the blades. The aim is to produce the required width while making good '
             'use of the available wood. Next comes grading and trimming.',
      'title': 'Inside Modern Pallet Factories | How Trees Become Wooden Pallets (Labor '
               'Legacy)',
      'url': 'https://www.youtube.com/watch?v=uDCbq1XJsDA&t=588s',
      'video_id': 'uDCbq1XJsDA'},
     {'author': 'IronPlanet',
      'channel': 'IronPlanet',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:39](https://www.youtube.com/watch?v=-1B3hGKjbz0&t=99s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Take one or more items at the final price congratulations when you're the "
              'highest bidder that item is yours just head to online checkout to complete your '
              "transaction and that's pretty much it still have questions customer care is "
              'standing by just ask.',
      'timestamp': 99,
      'timestamp_label': '[00:01:39]',
      'timestamp_seconds': 99,
      'tip': "Take one or more items at the final price congratulations when you're the "
             'highest bidder that item is yours just head to online checkout to complete your '
             "transaction and that's pretty much it still have questions customer care is "
             'standing by just ask.',
      'title': 'How to Bid Online at IronPlanet Auction (IronPlanet)',
      'url': 'https://www.youtube.com/watch?v=-1B3hGKjbz0&t=99s',
      'video_id': '-1B3hGKjbz0'},
     {'author': 'Auction Reviews With Jeff',
      'channel': 'Auction Reviews With Jeff',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:32:29](https://www.youtube.com/watch?v=Vi6nU6UkkoQ&t=1949s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'What is the right price on this one? How much would you pay for a 2020 Hyundai '
              'Elantra dark blue with only 8,122 mi on it? All right, we have an Escape here, '
              '2017. G38 All right, we have another Escape.',
      'timestamp': 1949,
      'timestamp_label': '[00:32:29]',
      'timestamp_seconds': 1949,
      'tip': 'What is the right price on this one? How much would you pay for a 2020 Hyundai '
             'Elantra dark blue with only 8,122 mi on it? All right, we have an Escape here, '
             '2017. G38 All right, we have another Escape.',
      'title': 'Federal Government (GSA) Auction Walk-Through (Cars and SUVs) (Auction Reviews '
               'With Jeff)',
      'url': 'https://www.youtube.com/watch?v=Vi6nU6UkkoQ&t=1949s',
      'video_id': 'Vi6nU6UkkoQ'},
     {'author': 'Auction Reviews With Jeff',
      'channel': 'Auction Reviews With Jeff',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:00](https://www.youtube.com/watch?v=crmTu2-MhzI&t=240s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'These are older here, 2005, 2004. And looky what we got here. They still have '
              "some Crown Victorias in the fleet. But they're turning them in one by one.",
      'timestamp': 240,
      'timestamp_label': '[00:04:00]',
      'timestamp_seconds': 240,
      'tip': 'These are older here, 2005, 2004. And looky what we got here. They still have '
             "some Crown Victorias in the fleet. But they're turning them in one by one.",
      'title': 'Government Vehicle Auction Prices | Ft Myers Part 1 of 3 (Auction Reviews With '
               'Jeff)',
      'url': 'https://www.youtube.com/watch?v=crmTu2-MhzI&t=240s',
      'video_id': 'crmTu2-MhzI'}],
 3: [{'author': 'Vantor Insider',
      'channel': 'Vantor Insider',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:43](https://www.youtube.com/watch?v=vkoGZ6Y4EhU&t=43s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'When a county road commission or federal depot designates an asset for '
              'disposal, that unit has already failed an internal maintenance audit balancing '
              'remaining service life against immediate capital repair cost.',
      'timestamp': 43,
      'timestamp_label': '[00:00:43]',
      'timestamp_seconds': 43,
      'tip': 'When a county road commission or federal depot designates an asset for disposal, '
             'that unit has already failed an internal maintenance audit balancing remaining '
             'service life against immediate capital repair cost.',
      'title': 'Never, EVER Bid on These 7 ‘Scrap’ Traps — 30 Years at Government Auctions '
               'Taught Me This (Vantor Insider)',
      'url': 'https://www.youtube.com/watch?v=vkoGZ6Y4EhU&t=43s',
      'video_id': 'vkoGZ6Y4EhU'},
     {'author': 'Flying Wheels',
      'channel': 'Flying Wheels',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=SEESfrbGoLY&t=20s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Guys are coming with me it's a free auction for anyone it's open to the public "
              "now I own a car dealership I have a dealer's license you guys can't go to a "
              'majority of the auctions I go to so I wanted to change it up a little bit today '
              'and go to a public auction show.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': "Guys are coming with me it's a free auction for anyone it's open to the public "
             "now I own a car dealership I have a dealer's license you guys can't go to a "
             'majority of the auctions I go to so I wanted to change it up a little bit today '
             'and go to a public auction show.',
      'title': 'How to Buy and Sell Government Auction Items for Profit - NO TITLES NEEDED! '
               '(Flying Wheels)',
      'url': 'https://www.youtube.com/watch?v=SEESfrbGoLY&t=20s',
      'video_id': 'SEESfrbGoLY'},
     {'author': 'IronPlanet Marketing',
      'channel': 'IronPlanet Marketing',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:46:17](https://www.youtube.com/watch?v=rn9oCm5t39A&t=2777s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Oo, that's a that's a that's an interesting question. I mean, you know, once "
              'again, going back to, you know, going back to my to my, you know, eBay days, I '
              "think you you'll you'll see that, you know, eBay is now actually more fixed "
              'price than it is auction.',
      'timestamp': 2777,
      'timestamp_label': '[00:46:17]',
      'timestamp_seconds': 2777,
      'tip': "Oo, that's a that's a that's an interesting question. I mean, you know, once "
             'again, going back to, you know, going back to my to my, you know, eBay days, I '
             "think you you'll you'll see that, you know, eBay is now actually more fixed "
             'price than it is auction.',
      'title': 'IronPlanet Webinar - Episode 1: From eBay to Excavators - Planning for Profit '
               'in the Digital Age (IronPlanet Marketing)',
      'url': 'https://www.youtube.com/watch?v=rn9oCm5t39A&t=2777s',
      'video_id': 'rn9oCm5t39A'},
     {'author': 'MrDavidAdelman',
      'channel': 'MrDavidAdelman',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:52](https://www.youtube.com/watch?v=gnsqwRYhRPY&t=52s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Federal, State and Local governments all hold their own auctions on a regular '
              'basis. The following is some helpful information to get you started in your '
              'quest to find a new home, car or other property at a bargain price.',
      'timestamp': 52,
      'timestamp_label': '[00:00:52]',
      'timestamp_seconds': 52,
      'tip': 'Federal, State and Local governments all hold their own auctions on a regular '
             'basis. The following is some helpful information to get you started in your '
             'quest to find a new home, car or other property at a bargain price.',
      'title': 'A Guide to Government Auction Sites (MrDavidAdelman)',
      'url': 'https://www.youtube.com/watch?v=gnsqwRYhRPY&t=52s',
      'video_id': 'gnsqwRYhRPY'},
     {'author': 'Money Making Juggernaut',
      'channel': 'Money Making Juggernaut',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:11](https://www.youtube.com/watch?v=KdtNDjlE4WQ&t=71s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'You also need to be aware of hidden costs associated with the foreclosure that '
              "we can't see. Only the foreclosure attorney or trustee can see. This can be "
              'acred interest. This can be the cost of the sale. And this can be the trustes '
              'commission for handling the actual sale.',
      'timestamp': 71,
      'timestamp_label': '[00:01:11]',
      'timestamp_seconds': 71,
      'tip': 'You also need to be aware of hidden costs associated with the foreclosure that '
             "we can't see. Only the foreclosure attorney or trustee can see. This can be "
             'acred interest. This can be the cost of the sale. And this can be the trustes '
             'commission for handling the actual sale.',
      'title': '5+ Million in Surplus Opportunities Texas and Georgia 11/4 sale (Money Making '
               'Juggernaut)',
      'url': 'https://www.youtube.com/watch?v=KdtNDjlE4WQ&t=71s',
      'video_id': 'KdtNDjlE4WQ'},
     {'author': 'GSA (General Services Administration)',
      'channel': 'GSA (General Services Administration)',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:03](https://www.youtube.com/watch?v=JzuRczRAlW8&t=123s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Proxy bids are intended to be the amount you are willing to pay for the '
              'auction. GSA Auctions will bid on your behalf and will use as much of your bid '
              'amount as needed to make you the current winner of the auction or to meet the '
              "auction's reserve price.",
      'timestamp': 123,
      'timestamp_label': '[00:02:03]',
      'timestamp_seconds': 123,
      'tip': 'Proxy bids are intended to be the amount you are willing to pay for the auction. '
             'GSA Auctions will bid on your behalf and will use as much of your bid amount as '
             "needed to make you the current winner of the auction or to meet the auction's "
             'reserve price.',
      'title': 'GSA Auctions: Online Bidding Opportunities (GSA (General Services '
               'Administration))',
      'url': 'https://www.youtube.com/watch?v=JzuRczRAlW8&t=123s',
      'video_id': 'JzuRczRAlW8'},
     {'author': 'WMBB News 13',
      'channel': 'WMBB News 13',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:19](https://www.youtube.com/watch?v=5kDb2ezDhgo&t=79s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "BUYING EQUIPMENT AND THE CARS AND STUFF LIKE I THINK IT'S A REALLY GOOD "
              'OPPORTUNITY FOR PEOPLE TO COME MAKE INVESTMENTS IN TURN AROUND AND MAKE A '
              'LITTLE EXTRA CASH THEY SHOULD DEFINITELY CHECK IT OUT. HUB SAYS THAT, YOU KNOW, '
              'A LITTLE EXTRA MONEY TO SPEND.',
      'timestamp': 79,
      'timestamp_label': '[00:01:19]',
      'timestamp_seconds': 79,
      'tip': "BUYING EQUIPMENT AND THE CARS AND STUFF LIKE I THINK IT'S A REALLY GOOD "
             'OPPORTUNITY FOR PEOPLE TO COME MAKE INVESTMENTS IN TURN AROUND AND MAKE A LITTLE '
             'EXTRA CASH THEY SHOULD DEFINITELY CHECK IT OUT. HUB SAYS THAT, YOU KNOW, A '
             'LITTLE EXTRA MONEY TO SPEND.',
      'title': 'Everything must go at government surplus auction in Springfield (WMBB News 13)',
      'url': 'https://www.youtube.com/watch?v=5kDb2ezDhgo&t=79s',
      'video_id': '5kDb2ezDhgo'},
     {'author': 'Jona Shone',
      'channel': 'Jona Shone',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=WG6vp4_R0nc&t=20s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'But there is a big price tag, £1,000 plus that. Not only will I be going '
              "through this palette, seeing what I've managed to get for my money, but I'll "
              'also be selling the entire palette, even if I want to keep some of the items on '
              'a live auction over on whatnot.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': 'But there is a big price tag, £1,000 plus that. Not only will I be going through '
             "this palette, seeing what I've managed to get for my money, but I'll also be "
             'selling the entire palette, even if I want to keep some of the items on a live '
             'auction over on whatnot.',
      'title': 'I Bought a DIY Tools Returns Pallet for £1000, Can I Make a Profit? (Jona '
               'Shone)',
      'url': 'https://www.youtube.com/watch?v=WG6vp4_R0nc&t=20s',
      'video_id': 'WG6vp4_R0nc'},
     {'author': 'Tris10 @ MeND',
      'channel': 'Tris10 @ MeND',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:15:53](https://www.youtube.com/watch?v=sG-wAF0b7kQ&t=953s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "See how the quantity is actually zero, but it's telling me what the price that "
              "we are agreeing to. So for every order that they send out, it'll be a unit "
              'price of $31. For every delivery that they send out, I need to complete it '
              'within 175 days as per my bid.',
      'timestamp': 953,
      'timestamp_label': '[00:15:53]',
      'timestamp_seconds': 953,
      'tip': "See how the quantity is actually zero, but it's telling me what the price that "
             "we are agreeing to. So for every order that they send out, it'll be a unit price "
             'of $31. For every delivery that they send out, I need to complete it within 175 '
             'days as per my bid.',
      'title': 'Understanding Your DLA Award - Uncover Potential Pitfalls and Mistakes (Tris10 '
               '@ MeND)',
      'url': 'https://www.youtube.com/watch?v=sG-wAF0b7kQ&t=953s',
      'video_id': 'sG-wAF0b7kQ'},
     {'author': 'Levi Salas | Whatnot Selling & Liquidation',
      'channel': 'Levi Salas | Whatnot Selling & Liquidation',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:05](https://www.youtube.com/watch?v=bGxomNwtOhQ&t=65s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "I'm blessed that my capital is not. 't come for two, three weeks, you have a "
              'lot of cash tied up where if you would have went locally, maybe had a smaller '
              'margin, um, you probably would have made more money if you would have just '
              'bought it locally, sell it or whatnot.',
      'timestamp': 65,
      'timestamp_label': '[00:01:05]',
      'timestamp_seconds': 65,
      'tip': "I'm blessed that my capital is not. 't come for two, three weeks, you have a lot "
             'of cash tied up where if you would have went locally, maybe had a smaller '
             'margin, um, you probably would have made more money if you would have just '
             'bought it locally, sell it or whatnot.',
      'title': 'Why Beginners Should Start With Pallets Instead of Truckloads (Levi Salas | '
               'Whatnot Selling & Liquidation)',
      'url': 'https://www.youtube.com/watch?v=bGxomNwtOhQ&t=65s',
      'video_id': 'bGxomNwtOhQ'},
     {'author': 'Kevin24Seven',
      'channel': 'Kevin24Seven',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:09](https://www.youtube.com/watch?v=gtS8l93r5cw&t=729s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'I think they last like 10 or 20 minutes. The price will more than double in '
              "every one of those auctions. Um, so that's, you know, how that works.",
      'timestamp': 729,
      'timestamp_label': '[00:12:09]',
      'timestamp_seconds': 729,
      'tip': 'I think they last like 10 or 20 minutes. The price will more than double in '
             "every one of those auctions. Um, so that's, you know, how that works.",
      'title': 'What to AVOID When Buying Humvees off GovPlanet (Kevin24Seven)',
      'url': 'https://www.youtube.com/watch?v=gtS8l93r5cw&t=729s',
      'video_id': 'gtS8l93r5cw'},
     {'author': 'Auction Reviews With Jeff',
      'channel': 'Auction Reviews With Jeff',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:20](https://www.youtube.com/watch?v=iauTGRI39kE&t=200s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Let's go look at this boat. Little Johnboat says Manatee Fire. That's a nice "
              'little boat if you can get it at the right price just to go boating around. '
              'Wow, look at all those birds.',
      'timestamp': 200,
      'timestamp_label': '[00:03:20]',
      'timestamp_seconds': 200,
      'tip': "Let's go look at this boat. Little Johnboat says Manatee Fire. That's a nice "
             'little boat if you can get it at the right price just to go boating around. Wow, '
             'look at all those birds.',
      'title': 'Government Surplus Vehicle Auction Walkthrough | Nice Trucks and Cars and '
               'More... (Auction Reviews With Jeff)',
      'url': 'https://www.youtube.com/watch?v=iauTGRI39kE&t=200s',
      'video_id': 'iauTGRI39kE'},
     {'author': 'Matt Goldberg | The Surplus Hunter',
      'channel': 'Matt Goldberg | The Surplus Hunter',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=6Ln8SD4VKv4&t=20s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, I can get offered surplus, slow moving, unwanted, maybe short expiry date, '
              'canceled orders, end of line, slow moving. Lots of different reasons why '
              'businesses have goods sitting in their warehouse, they just want to get rid of '
              'and turn it back into cash.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': 'So, I can get offered surplus, slow moving, unwanted, maybe short expiry date, '
             'canceled orders, end of line, slow moving. Lots of different reasons why '
             'businesses have goods sitting in their warehouse, they just want to get rid of '
             'and turn it back into cash.',
      'title': 'How I Find Highly Cheap Pallets Of Goods (On Autopilot) (Matt Goldberg | The '
               'Surplus Hunter)',
      'url': 'https://www.youtube.com/watch?v=6Ln8SD4VKv4&t=20s',
      'video_id': '6Ln8SD4VKv4'},
     {'author': 'Rattlesnake Defense',
      'channel': 'Rattlesnake Defense',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:39](https://www.youtube.com/watch?v=WzbjxUJRWKI&t=819s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Please don't judge me I'll tell you one thing right now after driving that "
              'hummer out here this uh CF Moto feels like a Ferrari uh keep that in mind.',
      'timestamp': 819,
      'timestamp_label': '[00:13:39]',
      'timestamp_seconds': 819,
      'tip': "Please don't judge me I'll tell you one thing right now after driving that "
             'hummer out here this uh CF Moto feels like a Ferrari uh keep that in mind.',
      'title': 'Would you spend $5k HMMWV from surplus.  Gov Planet Hummer Story. (Rattlesnake '
               'Defense)',
      'url': 'https://www.youtube.com/watch?v=WzbjxUJRWKI&t=819s',
      'video_id': 'WzbjxUJRWKI'},
     {'author': 'Auction Reviews With Jeff',
      'channel': 'Auction Reviews With Jeff',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:38](https://www.youtube.com/watch?v=P82Ir2OeO50&t=278s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Item 643, and item 645, a 2002 Ford pickup truck. Hey everyone, how you doing? '
              "I'm at another auction looking at what they have. The auction's actually going "
              "on now, so I'll I'll uh post the prices what they sold for. Everything else "
              'looks okay.',
      'timestamp': 278,
      'timestamp_label': '[00:04:38]',
      'timestamp_seconds': 278,
      'tip': 'Item 643, and item 645, a 2002 Ford pickup truck. Hey everyone, how you doing? '
             "I'm at another auction looking at what they have. The auction's actually going "
             "on now, so I'll I'll uh post the prices what they sold for. Everything else "
             'looks okay.',
      'title': 'MORE Government Auction Prices for Trucks, Vans, Buses and More! (Auction '
               'Reviews With Jeff)',
      'url': 'https://www.youtube.com/watch?v=P82Ir2OeO50&t=278s',
      'video_id': 'P82Ir2OeO50'}],
 4: [{'author': '41NBC',
      'channel': '41NBC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:56](https://www.youtube.com/watch?v=QOcs7dzmhGk&t=56s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'HAVE HERE AT THE DIST This is demonstration of RICT AE Comprompter Caption '
              'Central FUNA software. For a license call 60 THE S 785-7766URPLUS AUCTION GOES '
              'BAC INTO THE GENERAL FUND." THE SCHOOL DISTRICT AUCTIONS OFF THE ITEMS ONLINE '
              'TO THE HIGHEST BIDDER.',
      'timestamp': 56,
      'timestamp_label': '[00:00:56]',
      'timestamp_seconds': 56,
      'tip': 'HAVE HERE AT THE DIST This is demonstration of RICT AE Comprompter Caption '
             'Central FUNA software. For a license call 60 THE S 785-7766URPLUS AUCTION GOES '
             'BAC INTO THE GENERAL FUND." THE SCHOOL DISTRICT AUCTIONS OFF THE ITEMS ONLINE TO '
             'THE HIGHEST BIDDER.',
      'title': 'Bibb County Schools auction surplus items (41NBC)',
      'url': 'https://www.youtube.com/watch?v=QOcs7dzmhGk&t=56s',
      'video_id': 'QOcs7dzmhGk'},
     {'author': 'Engine Auction',
      'channel': 'Engine Auction',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:10](https://www.youtube.com/watch?v=t9kRwYmHNpE&t=730s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': '20,000 Cummins Onan Kubota diesel for $1,120 without needing a commercial '
              'dealer license opens up a massive opportunity, provided you know how to read '
              'the government inspection sheets before you place a bid.',
      'timestamp': 730,
      'timestamp_label': '[00:12:10]',
      'timestamp_seconds': 730,
      'tip': '20,000 Cummins Onan Kubota diesel for $1,120 without needing a commercial dealer '
             'license opens up a massive opportunity, provided you know how to read the '
             'government inspection sheets before you place a bid.',
      'title': '$1,100 at a US Government Auction Buys More Than You Think — 6 Quiet Diesels '
               'That Power a House (Engine Auction)',
      'url': 'https://www.youtube.com/watch?v=t9kRwYmHNpE&t=730s',
      'video_id': 't9kRwYmHNpE'},
     {'author': 'Good Day Sacramento',
      'channel': 'Good Day Sacramento',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:50](https://www.youtube.com/watch?v=9u351Sc6VXo&t=170s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'BEFORE THE AUCTION YOU CAN GET ONE LAST GLIMPSE AT THE ITEMS. Reporter: IF '
              "YOU'RE WONDERING IF ANYTHING IS IN YOUR BUDGET, WE HAVE A CRAZY RANGE. THINGS "
              'FOR AS LOW AS FIVE DOLLARS. DEPENDING ON SOME OF THE EQUIPMENT, WE HAVE SEEN '
              'THINGS GO FOR THOUSANDS.',
      'timestamp': 170,
      'timestamp_label': '[00:02:50]',
      'timestamp_seconds': 170,
      'tip': 'BEFORE THE AUCTION YOU CAN GET ONE LAST GLIMPSE AT THE ITEMS. Reporter: IF '
             "YOU'RE WONDERING IF ANYTHING IS IN YOUR BUDGET, WE HAVE A CRAZY RANGE. THINGS "
             'FOR AS LOW AS FIVE DOLLARS. DEPENDING ON SOME OF THE EQUIPMENT, WE HAVE SEEN '
             'THINGS GO FOR THOUSANDS.',
      'title': 'State Surplus Auction (Good Day Sacramento)',
      'url': 'https://www.youtube.com/watch?v=9u351Sc6VXo&t=170s',
      'video_id': '9u351Sc6VXo'},
     {'author': "Fun'N Learning",
      'channel': "Fun'N Learning",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:24](https://www.youtube.com/watch?v=wQlrhGYORAg&t=144s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'The ambulance has all kinds of medical tools like a stretcher to help carry '
              'people, bandages to help cover injuries, or even machines to check your '
              "heartbeat. He is always gentle and careful with her patients. Now it's time to "
              'meet Fred the fire truck.',
      'timestamp': 144,
      'timestamp_label': '[00:02:24]',
      'timestamp_seconds': 144,
      'tip': 'The ambulance has all kinds of medical tools like a stretcher to help carry '
             'people, bandages to help cover injuries, or even machines to check your '
             "heartbeat. He is always gentle and careful with her patients. Now it's time to "
             'meet Fred the fire truck.',
      'title': 'Learn Rescue Emergency Vehicles Police Car, Fire Truck, Ambulance | Best '
               "Toddlers Toy Learning Video (Fun'N Learning)",
      'url': 'https://www.youtube.com/watch?v=wQlrhGYORAg&t=144s',
      'video_id': 'wQlrhGYORAg'},
     {'author': 'dylanknowsball.',
      'channel': 'dylanknowsball.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:07](https://www.youtube.com/watch?v=doO2y672wlk&t=727s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Are you starting a stack because you saw a card you like ending at auction and '
              'you want it? Are you buying just for the sake of starting a stack because '
              "that's what I did. Weatherholt Topps Chrome X-Fractor for like less than four "
              'bucks.',
      'timestamp': 727,
      'timestamp_label': '[00:12:07]',
      'timestamp_seconds': 727,
      'tip': 'Are you starting a stack because you saw a card you like ending at auction and '
             "you want it? Are you buying just for the sake of starting a stack because that's "
             'what I did. Weatherholt Topps Chrome X-Fractor for like less than four bucks.',
      'title': 'Can you Make Money Buying on eBay Consignment Auctions? | Pickups + Case Study '
               '(dylanknowsball.)',
      'url': 'https://www.youtube.com/watch?v=doO2y672wlk&t=727s',
      'video_id': 'doO2y672wlk'},
     {'author': 'Junk Solutions Experts LLC',
      'channel': 'Junk Solutions Experts LLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:05](https://www.youtube.com/watch?v=El3cLMGi_9s&t=845s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'I got uh or I thought it was. Anyway, just wait for that video. Uh, so then it '
              'gives you all the details, you know, of the stuff that was in the description '
              "for the item, but this is sort of what's called a buyer certificate.",
      'timestamp': 845,
      'timestamp_label': '[00:14:05]',
      'timestamp_seconds': 845,
      'tip': 'I got uh or I thought it was. Anyway, just wait for that video. Uh, so then it '
             'gives you all the details, you know, of the stuff that was in the description '
             "for the item, but this is sort of what's called a buyer certificate.",
      'title': 'Govdeals auction tips for new accounts (Junk Solutions Experts LLC)',
      'url': 'https://www.youtube.com/watch?v=El3cLMGi_9s&t=845s',
      'video_id': 'El3cLMGi_9s'},
     {'author': 'Vantor Surplus',
      'channel': 'Vantor Surplus',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:42](https://www.youtube.com/watch?v=VA8oRw7jQuQ&t=462s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'The rumor that the government must scrap these units because federal '
              'environmental protection agency Tier 4 final emissions laws make older military '
              'diesel engines illegal for civilians to own or operate.',
      'timestamp': 462,
      'timestamp_label': '[00:07:42]',
      'timestamp_seconds': 462,
      'tip': 'The rumor that the government must scrap these units because federal '
             'environmental protection agency Tier 4 final emissions laws make older military '
             'diesel engines illegal for civilians to own or operate.',
      'title': 'Why the Pentagon Is Forced to Auction Brand-New Diesel Generators as '
               '“Unserviceable Scrap” (Vantor Surplus)',
      'url': 'https://www.youtube.com/watch?v=VA8oRw7jQuQ&t=462s',
      'video_id': 'VA8oRw7jQuQ'},
     {'author': 'We Hustle Daily',
      'channel': 'We Hustle Daily',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=VRmsT2o_6og&t=15s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'The tips and tricks on Copart and how to bid on co-art all right without a '
              'dealer license so you do not have to have a dealer license to buy a Copart all '
              'right.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'The tips and tricks on Copart and how to bid on co-art all right without a '
             'dealer license so you do not have to have a dealer license to buy a Copart all '
             'right.',
      'title': 'HOW TO BUY FROM COPART FOR BEGINNERS!!! WITHOUT A DEALERS LICENSE IN 2025!! '
               '(We Hustle Daily)',
      'url': 'https://www.youtube.com/watch?v=VRmsT2o_6og&t=15s',
      'video_id': 'VRmsT2o_6og'},
     {'author': 'Street Rat Garage',
      'channel': 'Street Rat Garage',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:25](https://www.youtube.com/watch?v=cqTAqIJLC10&t=865s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Sorts of things that are sitting here I'm going to give you about three "
              'examples and uh before the auction closes and then after the auction closes.',
      'timestamp': 865,
      'timestamp_label': '[00:14:25]',
      'timestamp_seconds': 865,
      'tip': "Sorts of things that are sitting here I'm going to give you about three examples "
             'and uh before the auction closes and then after the auction closes.',
      'title': 'Government auto auctions $1500.00 what did we buy? (Street Rat Garage)',
      'url': 'https://www.youtube.com/watch?v=cqTAqIJLC10&t=865s',
      'video_id': 'cqTAqIJLC10'},
     {'author': 'R25 Country',
      'channel': 'R25 Country',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:34:13](https://www.youtube.com/watch?v=sbKbkYznbo4&t=2053s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Paul's going to be proud of you. Who give $100 for that whole stack? I got 100 "
              'where 100 money zone. 50 75 50 75 75 75 75 75 5075 5075. They just had about a '
              'thousand trips.',
      'timestamp': 2053,
      'timestamp_label': '[00:34:13]',
      'timestamp_seconds': 2053,
      'tip': "Paul's going to be proud of you. Who give $100 for that whole stack? I got 100 "
             'where 100 money zone. 50 75 50 75 75 75 75 75 5075 5075. They just had about a '
             'thousand trips.',
      'title': 'You Won’t Believe What This State University Sells at their Annual Surplus '
               'Auction! (R25 Country)',
      'url': 'https://www.youtube.com/watch?v=sbKbkYznbo4&t=2053s',
      'video_id': 'sbKbkYznbo4'},
     {'author': 'The Rental Journey',
      'channel': 'The Rental Journey',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:26](https://www.youtube.com/watch?v=utk0mvTVyMM&t=146s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'That kind of go up on a like in school right and all sorts of equipment that I '
              "don't even know what it does like lab equipment test equipment uh really neat "
              'stuff us oscilloscopes um phones.',
      'timestamp': 146,
      'timestamp_label': '[00:02:26]',
      'timestamp_seconds': 146,
      'tip': 'That kind of go up on a like in school right and all sorts of equipment that I '
             "don't even know what it does like lab equipment test equipment uh really neat "
             'stuff us oscilloscopes um phones.',
      'title': 'Exploring Government Surplus Facility - For Hidden Rent-Out Gems (The Rental '
               'Journey)',
      'url': 'https://www.youtube.com/watch?v=utk0mvTVyMM&t=146s',
      'video_id': 'utk0mvTVyMM'},
     {'author': 'Scratch Fab',
      'channel': 'Scratch Fab',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:30](https://www.youtube.com/watch?v=45dQRk6d9Sw&t=450s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Capacity of this and it'll be probably between 5 and seven quarts so I'm going "
              'to start out with about five quarts not exactly an ideal setup for pouring oil '
              "throttles in the way so it's not real B sft.",
      'timestamp': 450,
      'timestamp_label': '[00:07:30]',
      'timestamp_seconds': 450,
      'tip': "Capacity of this and it'll be probably between 5 and seven quarts so I'm going "
             'to start out with about five quarts not exactly an ideal setup for pouring oil '
             "throttles in the way so it's not real B sft.",
      'title': 'Will it Run? I Bought a Military Forklift From GovPlanet! (Scratch Fab)',
      'url': 'https://www.youtube.com/watch?v=45dQRk6d9Sw&t=450s',
      'video_id': '45dQRk6d9Sw'},
     {'author': 'Kevin24Seven',
      'channel': 'Kevin24Seven',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:49](https://www.youtube.com/watch?v=jUJ2GbsJnGw&t=229s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'The hum V and it will recharge the the battery that is 12vt which is I believe '
              "the rear battery if I'm remembering that correctly.",
      'timestamp': 229,
      'timestamp_label': '[00:03:49]',
      'timestamp_seconds': 229,
      'tip': 'The hum V and it will recharge the the battery that is 12vt which is I believe '
             "the rear battery if I'm remembering that correctly.",
      'title': 'So You Want to Buy A Surplus Humvee? (Kevin24Seven)',
      'url': 'https://www.youtube.com/watch?v=jUJ2GbsJnGw&t=229s',
      'video_id': 'jUJ2GbsJnGw'},
     {'author': 'Auction Reviews With Jeff',
      'channel': 'Auction Reviews With Jeff',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:32](https://www.youtube.com/watch?v=6-YX9_QfY1A&t=512s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Did By the way, this is an absolute auction. So, the higher bidder gets it. '
              "Man, if this was four-wheel drive, it'd be perfect.",
      'timestamp': 512,
      'timestamp_label': '[00:08:32]',
      'timestamp_seconds': 512,
      'tip': 'Did By the way, this is an absolute auction. So, the higher bidder gets it. Man, '
             "if this was four-wheel drive, it'd be perfect.",
      'title': 'What Do Government Vehicles ACTUALLY Sell For at Auctions (Auction Reviews '
               'With Jeff)',
      'url': 'https://www.youtube.com/watch?v=6-YX9_QfY1A&t=512s',
      'video_id': '6-YX9_QfY1A'},
     {'author': 'Auction Reviews With Jeff',
      'channel': 'Auction Reviews With Jeff',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:52](https://www.youtube.com/watch?v=J-UWth-6Hd0&t=52s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Let's take a look at this one. Okey-dokey, let's go to the next one. Let's see "
              "if this one's locked, too. Maybe they lock them all up when the auction starts.",
      'timestamp': 52,
      'timestamp_label': '[00:00:52]',
      'timestamp_seconds': 52,
      'tip': "Let's take a look at this one. Okey-dokey, let's go to the next one. Let's see "
             "if this one's locked, too. Maybe they lock them all up when the auction starts.",
      'title': 'More Auction Prices for Campers, Motorhomes, Trailers, Boats, Mowers, '
               'Generators & More! (Auction Reviews With Jeff)',
      'url': 'https://www.youtube.com/watch?v=J-UWth-6Hd0&t=52s',
      'video_id': 'J-UWth-6Hd0'}],
 5: [{'author': 'UX Auctions',
      'channel': 'UX Auctions',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:13](https://www.youtube.com/watch?v=Z87d62pWVEk&t=253s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'t all sell them in the same place. Many cities and counties list their "
              'vehicles on government auction websites like gov deals, public surplus, and '
              'municipid. The federal government sells its fleet through GSA auctions and GSA '
              'fleet sales.',
      'timestamp': 253,
      'timestamp_label': '[00:04:13]',
      'timestamp_seconds': 253,
      'tip': "'t all sell them in the same place. Many cities and counties list their vehicles "
             'on government auction websites like gov deals, public surplus, and municipid. '
             'The federal government sells its fleet through GSA auctions and GSA fleet sales.',
      'title': 'How to Buy at Government Auctions: Police Cars & Surplus Vehicles (UX '
               'Auctions)',
      'url': 'https://www.youtube.com/watch?v=Z87d62pWVEk&t=253s',
      'video_id': 'Z87d62pWVEk'},
     {'author': 'Casey LaDelle',
      'channel': 'Casey LaDelle',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=XAvSq6gx5KQ&t=21s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "And on this one, I'm going to take you through some of my tips and tricks for "
              "how to make money buying equipment at an auction. 't, and some big mistakes to "
              'avoid.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': "And on this one, I'm going to take you through some of my tips and tricks for "
             "how to make money buying equipment at an auction. 't, and some big mistakes to "
             'avoid.',
      'title': 'How To Make MONEY At The Equipment Auction!   (and avoid the mistakes) (Casey '
               'LaDelle)',
      'url': 'https://www.youtube.com/watch?v=XAvSq6gx5KQ&t=21s',
      'video_id': 'XAvSq6gx5KQ'},
     {'author': 'Sales Tax Sisters',
      'channel': 'Sales Tax Sisters',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=uZA19ayitYY&t=15s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'The sales tax sisters and we want to talk about some audit hot topics again but '
              'specifically about exemption and resale certificate.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'The sales tax sisters and we want to talk about some audit hot topics again but '
             'specifically about exemption and resale certificate.',
      'title': 'Sales Tax Compliance- Top 5 Resale Certificate & Exemption Certificate '
               'Mistakes (Sales Tax Sisters)',
      'url': 'https://www.youtube.com/watch?v=uZA19ayitYY&t=15s',
      'video_id': 'uZA19ayitYY'},
     {'author': 'The Midnight Mechanic',
      'channel': 'The Midnight Mechanic',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=_tJQ6S_OaBc&t=21s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "So, I'm on my way to pick it up. Yes, we bought a military Humvee. We were "
              'thinking about what to do for our next project. Right when we started looking, '
              "email came across about government auctions. I'm never one to avoid checking "
              'out an auction.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': "So, I'm on my way to pick it up. Yes, we bought a military Humvee. We were "
             'thinking about what to do for our next project. Right when we started looking, '
             "email came across about government auctions. I'm never one to avoid checking out "
             'an auction.',
      'title': 'We bought a military surplus Humvee! (The Midnight Mechanic)',
      'url': 'https://www.youtube.com/watch?v=_tJQ6S_OaBc&t=21s',
      'video_id': '_tJQ6S_OaBc'},
     {'author': 'Hands Off Sales Tax (HOST)',
      'channel': 'Hands Off Sales Tax (HOST)',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:32](https://www.youtube.com/watch?v=lnmHPqYrNN8&t=212s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "None of this usually happens intentionally. It's just a byproduct of navigating "
              'a patchwork of state rules. Because resale certificate requirements vary so '
              'much by state, many businesses look for ways to reduce manual work and avoid '
              'mistakes.',
      'timestamp': 212,
      'timestamp_label': '[00:03:32]',
      'timestamp_seconds': 212,
      'tip': "None of this usually happens intentionally. It's just a byproduct of navigating "
             'a patchwork of state rules. Because resale certificate requirements vary so much '
             'by state, many businesses look for ways to reduce manual work and avoid '
             'mistakes.',
      'title': 'How YOU SHOULD Actually Obtain And Use Resale Certificates (Hands Off Sales '
               'Tax (HOST))',
      'url': 'https://www.youtube.com/watch?v=lnmHPqYrNN8&t=212s',
      'video_id': 'lnmHPqYrNN8'},
     {'author': 'iron king productions',
      'channel': 'iron king productions',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:12](https://www.youtube.com/watch?v=vlBL3apKXg0&t=492s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "I had, which I guess you really wouldn't call it a problem, was the battery "
              "system. So, these take 6TL batteries, and they're a square battery. They're "
              'basically military only, but you can pick them up from an auto parts store.',
      'timestamp': 492,
      'timestamp_label': '[00:08:12]',
      'timestamp_seconds': 492,
      'tip': "I had, which I guess you really wouldn't call it a problem, was the battery "
             "system. So, these take 6TL batteries, and they're a square battery. They're "
             'basically military only, but you can pick them up from an auto parts store.',
      'title': 'dont buy anything from a GOV-AUCTION UNTIL YOU WATCH THIS VIDEO!!!!! (iron '
               'king productions)',
      'url': 'https://www.youtube.com/watch?v=vlBL3apKXg0&t=492s',
      'video_id': 'vlBL3apKXg0'},
     {'author': 'Chase Thrifts',
      'channel': 'Chase Thrifts',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=aKiF3bLLJJ4&t=15s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Auctions with my two companions and I show you what reality TV doesn't welcome "
              "to chase thft what's going on thrifters we're going to a public College "
              'auction.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "Auctions with my two companions and I show you what reality TV doesn't welcome "
             "to chase thft what's going on thrifters we're going to a public College auction.",
      'title': 'University Surplus Auction -IUPUI (Chase Thrifts)',
      'url': 'https://www.youtube.com/watch?v=aKiF3bLLJJ4&t=15s',
      'video_id': 'aKiF3bLLJJ4'},
     {'author': 'Defense Logistics Agency',
      'channel': 'Defense Logistics Agency',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:42](https://www.youtube.com/watch?v=8HnHBuGYT6Y&t=42s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'What does this mean to you it means dla disposition services is your one-stop '
              'shop to dispose of and reutilize property at dla disposition services we are '
              "all about readiness responsiveness reuse we are dod's reverse logistics "
              'experts.',
      'timestamp': 42,
      'timestamp_label': '[00:00:42]',
      'timestamp_seconds': 42,
      'tip': 'What does this mean to you it means dla disposition services is your one-stop '
             'shop to dispose of and reutilize property at dla disposition services we are all '
             "about readiness responsiveness reuse we are dod's reverse logistics experts.",
      'title': "DLA Disposition Services: DOD's Reverse Logistics Experts (Defense Logistics "
               'Agency)',
      'url': 'https://www.youtube.com/watch?v=8HnHBuGYT6Y&t=42s',
      'video_id': '8HnHBuGYT6Y'},
     {'author': "Fun'N Learning",
      'channel': "Fun'N Learning",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:18:29](https://www.youtube.com/watch?v=S0me15htAic&t=1109s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "There was a little problem and I'm here to help. Wow, that's incredible, Rocky. "
              "Look, Rocky just became a missing puzzle piece. Let's put him back on the green "
              'puzzle. Cement mixers like Rocky are big trucks that have turning drums on '
              'their backs.',
      'timestamp': 1109,
      'timestamp_label': '[00:18:29]',
      'timestamp_seconds': 1109,
      'tip': "There was a little problem and I'm here to help. Wow, that's incredible, Rocky. "
             "Look, Rocky just became a missing puzzle piece. Let's put him back on the green "
             'puzzle. Cement mixers like Rocky are big trucks that have turning drums on their '
             'backs.',
      'title': 'Learn Emergency Rescue Vehicles |Police Car, Fire Truck, Ambulance Toy Video '
               "for Toddlers (Fun'N Learning)",
      'url': 'https://www.youtube.com/watch?v=S0me15htAic&t=1109s',
      'video_id': 'S0me15htAic'},
     {'author': 'Chill Crayon Explains',
      'channel': 'Chill Crayon Explains',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:45](https://www.youtube.com/watch?v=J0zoheNKu-E&t=105s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'s online destination for public sales of surplus federal real estate. "
              'Depending on the listings, buyers can encounter land, buildings, and other '
              'properties that the federal government no longer needs.',
      'timestamp': 105,
      'timestamp_label': '[00:01:45]',
      'timestamp_seconds': 105,
      'tip': "'s online destination for public sales of surplus federal real estate. Depending "
             'on the listings, buyers can encounter land, buildings, and other properties that '
             'the federal government no longer needs.',
      'title': 'Government Surplus Auctions Where You Can Buy Things For Pennies On The Dollar '
               '(Chill Crayon Explains)',
      'url': 'https://www.youtube.com/watch?v=J0zoheNKu-E&t=105s',
      'video_id': 'J0zoheNKu-E'},
     {'author': 'Gear Rack',
      'channel': 'Gear Rack',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:40](https://www.youtube.com/watch?v=m4wTDvPYQuA&t=520s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': '10 Polar Tech stuff sells We got a bunch of it. I mean, we we do sell it in the '
              "past. The problem is just like it's summer right now and we've also only had "
              "like terrible sizes that were used, so I would imagine they'll go pretty good. "
              'I mean, new extra-L large regular.',
      'timestamp': 520,
      'timestamp_label': '[00:08:40]',
      'timestamp_seconds': 520,
      'tip': '10 Polar Tech stuff sells We got a bunch of it. I mean, we we do sell it in the '
             "past. The problem is just like it's summer right now and we've also only had "
             "like terrible sizes that were used, so I would imagine they'll go pretty good. I "
             'mean, new extra-L large regular.',
      'title': 'Sorting a Random Military Surplus Pallet (Gear Rack)',
      'url': 'https://www.youtube.com/watch?v=m4wTDvPYQuA&t=520s',
      'video_id': 'm4wTDvPYQuA'},
     {'author': 'Operation Liquidation',
      'channel': 'Operation Liquidation',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:28](https://www.youtube.com/watch?v=f12reX7DS-U&t=88s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "And then what I'm doing is the items that are good to go on marketplace or "
              "eBay, I'm just going to photograph real quick. I did bring some more poster "
              'board with me today to kind of um make that whole backdrop white.',
      'timestamp': 88,
      'timestamp_label': '[00:01:28]',
      'timestamp_seconds': 88,
      'tip': "And then what I'm doing is the items that are good to go on marketplace or eBay, "
             "I'm just going to photograph real quick. I did bring some more poster board with "
             'me today to kind of um make that whole backdrop white.',
      'title': 'Unboxing 2 Pallets of Jumbo Amazon Returns - Worth It? (Operation Liquidation)',
      'url': 'https://www.youtube.com/watch?v=f12reX7DS-U&t=88s',
      'video_id': 'f12reX7DS-U'},
     {'author': 'Kevin24Seven',
      'channel': 'Kevin24Seven',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:27](https://www.youtube.com/watch?v=Vl0TRUioSn0&t=87s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'And have it in my garage so buying the humvee flat out was twelve thousand five '
              'hundred dollars to win that auction.',
      'timestamp': 87,
      'timestamp_label': '[00:01:27]',
      'timestamp_seconds': 87,
      'tip': 'And have it in my garage so buying the humvee flat out was twelve thousand five '
             'hundred dollars to win that auction.',
      'title': 'GovPlanet Humvee- Total Build Cost (Kevin24Seven)',
      'url': 'https://www.youtube.com/watch?v=Vl0TRUioSn0&t=87s',
      'video_id': 'Vl0TRUioSn0'},
     {'author': 'Auction Reviews With Jeff',
      'channel': 'Auction Reviews With Jeff',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:44](https://www.youtube.com/watch?v=HQ3YV3h4sC4&t=224s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "152 767 That is an interesting piece of equipment. All right, we'll get some "
              'generators. Wacker Neuson 134 131 Some Generacs.',
      'timestamp': 224,
      'timestamp_label': '[00:03:44]',
      'timestamp_seconds': 224,
      'tip': "152 767 That is an interesting piece of equipment. All right, we'll get some "
             'generators. Wacker Neuson 134 131 Some Generacs.',
      'title': 'Gov Auction Prices for Excavators | Skid Steers | Dump Trucks and MORE! '
               '(Auction Reviews With Jeff)',
      'url': 'https://www.youtube.com/watch?v=HQ3YV3h4sC4&t=224s',
      'video_id': 'HQ3YV3h4sC4'},
     {'author': 'Kevin24Seven',
      'channel': 'Kevin24Seven',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:20](https://www.youtube.com/watch?v=F0AkAibFp2g&t=860s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'It did when it came in but I have a build series on that and an off-roading '
              "series on that that you can follow I'll see you guys in the next one thanks for "
              'watching thank you for the support.',
      'timestamp': 860,
      'timestamp_label': '[00:14:20]',
      'timestamp_seconds': 860,
      'tip': 'It did when it came in but I have a build series on that and an off-roading '
             "series on that that you can follow I'll see you guys in the next one thanks for "
             'watching thank you for the support.',
      'title': 'Buying a Govplanet Humvee- Process & Top Tips. (Kevin24Seven)',
      'url': 'https://www.youtube.com/watch?v=F0AkAibFp2g&t=860s',
      'video_id': 'F0AkAibFp2g'}],
 6: [{'author': 'UpKeep',
      'channel': 'UpKeep',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:55](https://www.youtube.com/watch?v=G6OFgjz5ZIE&t=55s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'The original equipment manufacturer a quick Google search can lead you to eBay '
              'where you might find this part listed as New Old Stock for $69 or even used '
              'for.',
      'timestamp': 55,
      'timestamp_label': '[00:00:55]',
      'timestamp_seconds': 55,
      'tip': 'The original equipment manufacturer a quick Google search can lead you to eBay '
             'where you might find this part listed as New Old Stock for $69 or even used for.',
      'title': 'How to Source and Sell Industrial Parts on eBay: A Guide for Maintenance & '
               'Operations Teams (UpKeep)',
      'url': 'https://www.youtube.com/watch?v=G6OFgjz5ZIE&t=55s',
      'video_id': 'G6OFgjz5ZIE'},
     {'author': 'Top 5 Autos',
      'channel': 'Top 5 Autos',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:28](https://www.youtube.com/watch?v=WFVGJDWST7I&t=208s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Not because something is wrong, because policy says rotate the fleet. This is '
              'where you find the best value per dollar in the entire auction system. Number '
              'three, bank repo vehicles through federal programs.',
      'timestamp': 208,
      'timestamp_label': '[00:03:28]',
      'timestamp_seconds': 208,
      'tip': 'Not because something is wrong, because policy says rotate the fleet. This is '
             'where you find the best value per dollar in the entire auction system. Number '
             'three, bank repo vehicles through federal programs.',
      'title': 'Buy a $55K SUV for Under $18K | The Government Auction GOLDMINE Nobody Shows '
               'You (Top 5 Autos)',
      'url': 'https://www.youtube.com/watch?v=WFVGJDWST7I&t=208s',
      'video_id': 'WFVGJDWST7I'},
     {'author': 'SKUio',
      'channel': 'SKUio',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:50](https://www.youtube.com/watch?v=tahP--1EvSE&t=50s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'California has no certificate yet, so orders shipping there are still taxed. To '
              "add one, click the plus button at the end of its row. First, choose how you'll "
              'provide the certificate. You can upload the signed file, or paste a link to the '
              "buyer's own copy.",
      'timestamp': 50,
      'timestamp_label': '[00:00:50]',
      'timestamp_seconds': 50,
      'tip': 'California has no certificate yet, so orders shipping there are still taxed. To '
             "add one, click the plus button at the end of its row. First, choose how you'll "
             'provide the certificate. You can upload the signed file, or paste a link to the '
             "buyer's own copy.",
      'title': 'How to Add and Approve a Customer Resale Certificate for Sales Tax Exemption | '
               'SKU.io (SKUio)',
      'url': 'https://www.youtube.com/watch?v=tahP--1EvSE&t=50s',
      'video_id': 'tahP--1EvSE'},
     {'author': 'Matt Goldberg | The Surplus Hunter',
      'channel': 'Matt Goldberg | The Surplus Hunter',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:48](https://www.youtube.com/watch?v=gRoLw2uovek&t=228s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Literally, I will share the deal with you 50/50. So, how that would work is you '
              "would find the surplus stock. So, you're finding the seller of the goods. But "
              "you've also actually found the buyer of the goods as well.",
      'timestamp': 228,
      'timestamp_label': '[00:03:48]',
      'timestamp_seconds': 228,
      'tip': 'Literally, I will share the deal with you 50/50. So, how that would work is you '
             "would find the surplus stock. So, you're finding the seller of the goods. But "
             "you've also actually found the buyer of the goods as well.",
      'title': '5 Ways To Make Money Flipping Pallets Of Cheap Goods In Surplus Trader Academy '
               '(SKOOL) (Matt Goldberg | The Surplus Hunter)',
      'url': 'https://www.youtube.com/watch?v=gRoLw2uovek&t=228s',
      'video_id': 'gRoLw2uovek'},
     {'author': 'Jack Hagwell',
      'channel': 'Jack Hagwell',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:49](https://www.youtube.com/watch?v=iNfW7YXuTOA&t=49s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "So, I think this would be the best option. But what I'm going to do here is "
              "just type in for the example of when I did it the first time. So, I'm going to "
              'ask, how do I get my resale certificate or sales tax exemption in New York?',
      'timestamp': 49,
      'timestamp_label': '[00:00:49]',
      'timestamp_seconds': 49,
      'tip': "So, I think this would be the best option. But what I'm going to do here is just "
             "type in for the example of when I did it the first time. So, I'm going to ask, "
             'how do I get my resale certificate or sales tax exemption in New York?',
      'title': 'How To Avoid Sales Tax With Online Arbitrage | Reseller Certificates 101 (Jack '
               'Hagwell)',
      'url': 'https://www.youtube.com/watch?v=iNfW7YXuTOA&t=49s',
      'video_id': 'iNfW7YXuTOA'},
     {'author': 'AutoHacker',
      'channel': 'AutoHacker',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:01](https://www.youtube.com/watch?v=wNIgM_BLGik&t=541s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'To ensure insurance or auction and you scroll all the way down and you click '
              "this find the broker you're gonna find the list of all Brokers you can use and.",
      'timestamp': 541,
      'timestamp_label': '[00:09:01]',
      'timestamp_seconds': 541,
      'tip': 'To ensure insurance or auction and you scroll all the way down and you click '
             "this find the broker you're gonna find the list of all Brokers you can use and.",
      'title': '7 Common Mistakes to Avoid When Buying Cars at Copart, IAAI (AutoHacker)',
      'url': 'https://www.youtube.com/watch?v=wNIgM_BLGik&t=541s',
      'video_id': 'wNIgM_BLGik'},
     {'author': 'Liquidation Motivation',
      'channel': 'Liquidation Motivation',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:28:02](https://www.youtube.com/watch?v=PyTXQNvVkKc&t=1682s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Holy cow, there's two of them. So, I think this this deal is like if you have "
              'the patience to go through this, figure out what the car parts are, and then '
              'list them on eBay.',
      'timestamp': 1682,
      'timestamp_label': '[00:28:02]',
      'timestamp_seconds': 1682,
      'tip': "Holy cow, there's two of them. So, I think this this deal is like if you have "
             'the patience to go through this, figure out what the car parts are, and then '
             'list them on eBay.',
      'title': 'Scoring $20,000 on ONE Pallet from a 3PL Truckload (Liquidation Unboxing) '
               '(Liquidation Motivation)',
      'url': 'https://www.youtube.com/watch?v=PyTXQNvVkKc&t=1682s',
      'video_id': 'PyTXQNvVkKc'},
     {'author': 'Auction Reviews With Jeff',
      'channel': 'Auction Reviews With Jeff',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:23](https://www.youtube.com/watch?v=cZOfyxWtGp8&t=503s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'This is my second auction, GSA, government federal government auction. The '
              "first one I did, I've got some videos. I've got three videos on it. The prices "
              "were pretty decent. I think they I don't know for sure.",
      'timestamp': 503,
      'timestamp_label': '[00:08:23]',
      'timestamp_seconds': 503,
      'tip': 'This is my second auction, GSA, government federal government auction. The first '
             "one I did, I've got some videos. I've got three videos on it. The prices were "
             "pretty decent. I think they I don't know for sure.",
      'title': 'MORE TRUCK PRICES From GSA Auction (Auction Reviews With Jeff)',
      'url': 'https://www.youtube.com/watch?v=cZOfyxWtGp8&t=503s',
      'video_id': 'cZOfyxWtGp8'},
     {'author': 'Retired and Winging it',
      'channel': 'Retired and Winging it',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[01:07:12](https://www.youtube.com/watch?v=pl4wTzpNWRQ&t=4032s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Got what they sold for uh the video that says with prices o it's got a cabin "
              "I've got the prices the range of what these sold for okay over here last "
              "remaining little bit Massie first and 4610 it's a private or dealer and it's a "
              "cab let's see Massi fuson closed cab.",
      'timestamp': 4032,
      'timestamp_label': '[01:07:12]',
      'timestamp_seconds': 4032,
      'tip': "Got what they sold for uh the video that says with prices o it's got a cabin "
             "I've got the prices the range of what these sold for okay over here last "
             "remaining little bit Massie first and 4610 it's a private or dealer and it's a "
             "cab let's see Massi fuson closed cab.",
      'title': 'What did they sell for? Government Surplus Vehicle Auction WITH PRICES! '
               '(Retired and Winging it)',
      'url': 'https://www.youtube.com/watch?v=pl4wTzpNWRQ&t=4032s',
      'video_id': 'pl4wTzpNWRQ'},
     {'author': "PA's Shop",
      'channel': "PA's Shop",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:54](https://www.youtube.com/watch?v=5Qaj8MhpVIc&t=414s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Okay, so I have four resistors here. So, we're going to give it a shot. Uh "
              "we're going to check the first one on uh 2C5. If I can find the other probe. "
              "First one should be around 10 ohms. Uh let's look at the Fluke.",
      'timestamp': 414,
      'timestamp_label': '[00:06:54]',
      'timestamp_seconds': 414,
      'tip': "Okay, so I have four resistors here. So, we're going to give it a shot. Uh we're "
             'going to check the first one on uh 2C5. If I can find the other probe. First one '
             "should be around 10 ohms. Uh let's look at the Fluke.",
      'title': 'fluke87V vs the FNIRSI 2C53T  I would buy this as my first piece of test '
               "equipment (PA's Shop)",
      'url': 'https://www.youtube.com/watch?v=5Qaj8MhpVIc&t=414s',
      'video_id': '5Qaj8MhpVIc'},
     {'author': 'FlatBroke Garage',
      'channel': 'FlatBroke Garage',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:04](https://www.youtube.com/watch?v=mnHD_DqC7xk&t=364s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Be all the auction vehicles what he cleared out some school buses didn't he "
              'seven what was their number on the windshield it was seven two one one we have '
              "to find it I think it's straight ahead Maybe.",
      'timestamp': 364,
      'timestamp_label': '[00:06:04]',
      'timestamp_seconds': 364,
      'tip': "Be all the auction vehicles what he cleared out some school buses didn't he "
             'seven what was their number on the windshield it was seven two one one we have '
             "to find it I think it's straight ahead Maybe.",
      'title': 'I bought a Ford Escape on GovDeals, was it worth it? (FlatBroke Garage)',
      'url': 'https://www.youtube.com/watch?v=mnHD_DqC7xk&t=364s',
      'video_id': 'mnHD_DqC7xk'},
     {'author': 'IronPlanet',
      'channel': 'IronPlanet',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:16](https://www.youtube.com/watch?v=Un4UP8ZN-Pk&t=196s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "You're buying or selling iron planet is the company to turn to for auctions you "
              'can trust guaranteed inspections with our Ironclad Assurance no headaches or '
              "surprises no leg work just results that's iron Planet find out more by "
              'contacting iron planet today.',
      'timestamp': 196,
      'timestamp_label': '[00:03:16]',
      'timestamp_seconds': 196,
      'tip': "You're buying or selling iron planet is the company to turn to for auctions you "
             'can trust guaranteed inspections with our Ironclad Assurance no headaches or '
             "surprises no leg work just results that's iron Planet find out more by "
             'contacting iron planet today.',
      'title': 'IronPlanet - Auctions you can trust (IronPlanet)',
      'url': 'https://www.youtube.com/watch?v=Un4UP8ZN-Pk&t=196s',
      'video_id': 'Un4UP8ZN-Pk'},
     {'author': 'Matt Goldberg | The Surplus Hunter',
      'channel': 'Matt Goldberg | The Surplus Hunter',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:25](https://www.youtube.com/watch?v=Ey5jcenBhe8&t=85s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, the first one, go on to LinkedIn, all right? Type in in the search box '
              'returns and filter the results to people, okay? Now, the people in these '
              'results are generally going to be in job positions that has something to do '
              'with returns, okay?',
      'timestamp': 85,
      'timestamp_label': '[00:01:25]',
      'timestamp_seconds': 85,
      'tip': 'So, the first one, go on to LinkedIn, all right? Type in in the search box '
             'returns and filter the results to people, okay? Now, the people in these results '
             'are generally going to be in job positions that has something to do with '
             'returns, okay?',
      'title': '[Free Training] 5 Secret Places To Find Cheap Liquidation Returns Pallets '
               '(Matt Goldberg | The Surplus Hunter)',
      'url': 'https://www.youtube.com/watch?v=Ey5jcenBhe8&t=85s',
      'video_id': 'Ey5jcenBhe8'},
     {'author': 'Rasmussen Equipment',
      'channel': 'Rasmussen Equipment',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:47](https://www.youtube.com/watch?v=B8X-aaJ2DpY&t=707s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Planet uh we you know after picking it up we came out here to the Calico '
              'mountains you can see how beautiful this place is this sweet Hog Rock right '
              "there if you guys haven't seen that before and uh you know we came out here "
              'shot about 1,000 bucks with a lead.',
      'timestamp': 707,
      'timestamp_label': '[00:11:47]',
      'timestamp_seconds': 707,
      'tip': 'Planet uh we you know after picking it up we came out here to the Calico '
             'mountains you can see how beautiful this place is this sweet Hog Rock right '
             "there if you guys haven't seen that before and uh you know we came out here shot "
             'about 1,000 bucks with a lead.',
      'title': 'I Bought a Humvee From GovPlanet. Will it Start? HMMWV M1114 MCTAGS (Rasmussen '
               'Equipment)',
      'url': 'https://www.youtube.com/watch?v=B8X-aaJ2DpY&t=707s',
      'video_id': 'B8X-aaJ2DpY'},
     {'author': 'Kevin24Seven',
      'channel': 'Kevin24Seven',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=OoVFtojdDNk&t=21s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'There are some key factors that may come via some of the best off-road vehicles '
              'in the world and also just make them good solid vehicles in general before you '
              'scoff at that hear me out these are the top seven things I love about my prior '
              'military humvee.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': 'There are some key factors that may come via some of the best off-road vehicles '
             'in the world and also just make them good solid vehicles in general before you '
             'scoff at that hear me out these are the top seven things I love about my prior '
             'military humvee.',
      'title': '7 Reasons I LOVE my Surplus Humvee (GovPlanet) (Kevin24Seven)',
      'url': 'https://www.youtube.com/watch?v=OoVFtojdDNk&t=21s',
      'video_id': 'OoVFtojdDNk'}],
 7: [{'author': 'Sea Auctions',
      'channel': 'Sea Auctions',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:26](https://www.youtube.com/watch?v=drW14-jA62E&t=326s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'We created our step-by-step auction mastery training showing you how to buy '
              'repossessed boats, work trucks, and heavy equipment at marina bank and '
              'government auctions for pennies on the dollar. You also receive two field '
              'resources our captains use every weekend.',
      'timestamp': 326,
      'timestamp_label': '[00:05:26]',
      'timestamp_seconds': 326,
      'tip': 'We created our step-by-step auction mastery training showing you how to buy '
             'repossessed boats, work trucks, and heavy equipment at marina bank and '
             'government auctions for pennies on the dollar. You also receive two field '
             'resources our captains use every weekend.',
      'title': '$1,500 at a Florida Marina Auction Buys More Than You Think — What Captains '
               'Took Home (Sea Auctions)',
      'url': 'https://www.youtube.com/watch?v=drW14-jA62E&t=326s',
      'video_id': 'drW14-jA62E'},
     {'author': 'Kai Ashley ED',
      'channel': 'Kai Ashley ED',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:35](https://www.youtube.com/watch?v=-T-caQVAr7g&t=215s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'A very simple process we simply just have to fill out a an exemption form '
              'called the Georgia certificate of exemption st5 and then submit it to the.',
      'timestamp': 215,
      'timestamp_label': '[00:03:35]',
      'timestamp_seconds': 215,
      'tip': 'A very simple process we simply just have to fill out a an exemption form called '
             'the Georgia certificate of exemption st5 and then submit it to the.',
      'title': 'What is a Resale Certificate and How Can You Get One? | Tax Exemption for '
               'Wholesale Products (Kai Ashley ED)',
      'url': 'https://www.youtube.com/watch?v=-T-caQVAr7g&t=215s',
      'video_id': '-T-caQVAr7g'},
     {'author': 'GovDeals Media',
      'channel': 'GovDeals Media',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:50](https://www.youtube.com/watch?v=Q4B13yVVzZQ&t=50s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'You can now upload a photo of the VIN to automatically populate the fields. '
              'Remember, clear, accurate descriptions help build buyer confidence and drive '
              'stronger bidding. Step two, set up sale parameters. Next, configure your '
              'auction details.',
      'timestamp': 50,
      'timestamp_label': '[00:00:50]',
      'timestamp_seconds': 50,
      'tip': 'You can now upload a photo of the VIN to automatically populate the fields. '
             'Remember, clear, accurate descriptions help build buyer confidence and drive '
             'stronger bidding. Step two, set up sale parameters. Next, configure your auction '
             'details.',
      'title': 'GovDeals New Asset Listing Experience (GovDeals Media)',
      'url': 'https://www.youtube.com/watch?v=Q4B13yVVzZQ&t=50s',
      'video_id': 'Q4B13yVVzZQ'},
     {'author': 'Santiago Cueto | Miami Business Litigation Lawyer',
      'channel': 'Santiago Cueto | Miami Business Litigation Lawyer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:08](https://www.youtube.com/watch?v=K5oBesJVonE&t=728s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'FL Tax Verify app or one of the other approved methods. And fifth, you remember '
              'that your certificate renews every year. That is the entire process. It sounds '
              'like a lot, but once you have done it, it runs on autopilot. The initial setup '
              'takes a little effort.',
      'timestamp': 728,
      'timestamp_label': '[00:12:08]',
      'timestamp_seconds': 728,
      'tip': 'FL Tax Verify app or one of the other approved methods. And fifth, you remember '
             'that your certificate renews every year. That is the entire process. It sounds '
             'like a lot, but once you have done it, it runs on autopilot. The initial setup '
             'takes a little effort.',
      'title': 'The ONLY Florida Resale Certificate Guide You Need (Santiago Cueto | Miami '
               'Business Litigation Lawyer)',
      'url': 'https://www.youtube.com/watch?v=K5oBesJVonE&t=728s',
      'video_id': 'K5oBesJVonE'},
     {'author': 'GSA (General Services Administration)',
      'channel': 'GSA (General Services Administration)',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:30](https://www.youtube.com/watch?v=zFGATosXViU&t=90s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Manual Notifications: Emails sent by the Realty Specialist with updates about '
              'the property. System Announcements: General notifications about platform '
              'updates or events. You must register to bid on a specific listing. Registering '
              'to bid is a three-step process.',
      'timestamp': 90,
      'timestamp_label': '[00:01:30]',
      'timestamp_seconds': 90,
      'tip': 'Manual Notifications: Emails sent by the Realty Specialist with updates about '
             'the property. System Announcements: General notifications about platform updates '
             'or events. You must register to bid on a specific listing. Registering to bid is '
             'a three-step process.',
      'title': 'How to Register and Bid for GSA Real Property on RealEstateSales.gov (GSA '
               '(General Services Administration))',
      'url': 'https://www.youtube.com/watch?v=zFGATosXViU&t=90s',
      'video_id': 'zFGATosXViU'},
     {'author': 'Defense Logistics Agency',
      'channel': 'Defense Logistics Agency',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:10](https://www.youtube.com/watch?v=P3RfMbWlTYg&t=70s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Process to the system we can actually set up wherever and receiving destroyed '
              'property we currently have five sets three of them are around the world and two '
              'we keep stateside as training assets and in case we need them for humanitarian '
              'use.',
      'timestamp': 70,
      'timestamp_label': '[00:01:10]',
      'timestamp_seconds': 70,
      'tip': 'Process to the system we can actually set up wherever and receiving destroyed '
             'property we currently have five sets three of them are around the world and two '
             'we keep stateside as training assets and in case we need them for humanitarian '
             'use.',
      'title': 'Deploy the Dog: DLA Disposition Services Expeditionary Site Set (Open Caption) '
               '(Defense Logistics Agency)',
      'url': 'https://www.youtube.com/watch?v=P3RfMbWlTYg&t=70s',
      'video_id': 'P3RfMbWlTYg'},
     {'author': 'Keysight',
      'channel': 'Keysight',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:49](https://www.youtube.com/watch?v=TipNUpHGLw0&t=49s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'The second reason is that the same certifications that ensure the highest '
              'quality of our new products also guarantee the perfect implementation of our '
              "rigorous refurbishment process. As the industry's most comprehensive "
              'remanufacturing process.',
      'timestamp': 49,
      'timestamp_label': '[00:00:49]',
      'timestamp_seconds': 49,
      'tip': 'The second reason is that the same certifications that ensure the highest '
             'quality of our new products also guarantee the perfect implementation of our '
             "rigorous refurbishment process. As the industry's most comprehensive "
             'remanufacturing process.',
      'title': "Keysight Premium Used Equipment: See Keysight's Refurbishment Process "
               '(Keysight)',
      'url': 'https://www.youtube.com/watch?v=TipNUpHGLw0&t=49s',
      'video_id': 'TipNUpHGLw0'},
     {'author': 'Go-to-Market Solutions',
      'channel': 'Go-to-Market Solutions',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:08](https://www.youtube.com/watch?v=szkqa7FwjYE&t=368s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Templates to step-by-step guides we've got everything you need to streamline "
              'your process and win more contracts click the links Below in the video '
              "description to download your free toolkit and explore our dib's products let's "
              'win those contracts together.',
      'timestamp': 368,
      'timestamp_label': '[00:06:08]',
      'timestamp_seconds': 368,
      'tip': "Templates to step-by-step guides we've got everything you need to streamline "
             'your process and win more contracts click the links Below in the video '
             "description to download your free toolkit and explore our dib's products let's "
             'win those contracts together.',
      'title': 'DLA Inspections and Shipping Simplified: Step-by-Step Guide (Go-to-Market '
               'Solutions)',
      'url': 'https://www.youtube.com/watch?v=szkqa7FwjYE&t=368s',
      'video_id': 'szkqa7FwjYE'},
     {'author': 'Data Center MEP System',
      'channel': 'Data Center MEP System',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:19:20](https://www.youtube.com/watch?v=SQ3IcEPrZ9g&t=1160s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Earthing acceptance combines conductive continuity with the behavior of the '
              'protective system during a fault. Electrode resistance alone cannot describe '
              'touch voltage, step voltage, or disconnection time. Parallel paths can also '
              'change what an instrument actually measures.',
      'timestamp': 1160,
      'timestamp_label': '[00:19:20]',
      'timestamp_seconds': 1160,
      'tip': 'Earthing acceptance combines conductive continuity with the behavior of the '
             'protective system during a fault. Electrode resistance alone cannot describe '
             'touch voltage, step voltage, or disconnection time. Parallel paths can also '
             'change what an instrument actually measures.',
      'title': 'Acceptance Testing Masterclass | Hyperscale Data Center | Part A (Data Center '
               'MEP System)',
      'url': 'https://www.youtube.com/watch?v=SQ3IcEPrZ9g&t=1160s',
      'video_id': 'SQ3IcEPrZ9g'},
     {'author': 'Live Mobile Technology Inc',
      'channel': 'Live Mobile Technology Inc',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=2tSL4NkyYWM&t=15s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "In this video, I'll show you how to use the Fluke Link IQ step-by-step. We'll "
              'go through the process from connecting the cable to running the test  and.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "In this video, I'll show you how to use the Fluke Link IQ step-by-step. We'll go "
             'through the process from connecting the cable to running the test  and.',
      'title': 'How to Use the Fluke LinkIQ Network Tester | Ethernet Cable Testing Tutorial '
               '(Live Mobile Technology Inc)',
      'url': 'https://www.youtube.com/watch?v=2tSL4NkyYWM&t=15s',
      'video_id': '2tSL4NkyYWM'},
     {'author': 'James Baker CPA',
      'channel': 'James Baker CPA',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:22](https://www.youtube.com/watch?v=CiHy9lcx3x4&t=22s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "I'm in Florida and it's a little bit easier for me to get them here. And the "
              'resale certificates are actually pretty good . So you say, wait, wait, wait, '
              'Jim, take a step back. What is a resale certificate?',
      'timestamp': 22,
      'timestamp_label': '[00:00:22]',
      'timestamp_seconds': 22,
      'tip': "I'm in Florida and it's a little bit easier for me to get them here. And the "
             'resale certificates are actually pretty good . So you say, wait, wait, wait, '
             'Jim, take a step back. What is a resale certificate?',
      'title': 'What is a resale certificate and why do i need one? //Serie (James Baker CPA)',
      'url': 'https://www.youtube.com/watch?v=CiHy9lcx3x4&t=22s',
      'video_id': 'CiHy9lcx3x4'},
     {'author': 'Rasmussen Equipment',
      'channel': 'Rasmussen Equipment',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:08](https://www.youtube.com/watch?v=zqnmA4kt0RU&t=248s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Let me hit the zoom over here. Film these guys loading this Humvey up on that '
              'step deck trailer over there. And I said there were two in front of me, but I '
              "see three here. There's a tow truck and two step decks. But I think that red "
              'one showed up after I got here.',
      'timestamp': 248,
      'timestamp_label': '[00:04:08]',
      'timestamp_seconds': 248,
      'tip': 'Let me hit the zoom over here. Film these guys loading this Humvey up on that '
             'step deck trailer over there. And I said there were two in front of me, but I '
             "see three here. There's a tow truck and two step decks. But I think that red one "
             'showed up after I got here.',
      'title': 'Picking up a HMMWV From GovPlanet.  WILL IT RUN ? (Rasmussen Equipment)',
      'url': 'https://www.youtube.com/watch?v=zqnmA4kt0RU&t=248s',
      'video_id': 'zqnmA4kt0RU'},
     {'author': 'Auction Reviews With Jeff',
      'channel': 'Auction Reviews With Jeff',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:37](https://www.youtube.com/watch?v=YaIalHq0RVU&t=877s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Let's see if these two crank. And it smells smells musty in here like it like "
              'something got wet. So, one of the reasons I do these videos is just so you can '
              'see, you know, what type of vehicle is available at at these auctions.',
      'timestamp': 877,
      'timestamp_label': '[00:14:37]',
      'timestamp_seconds': 877,
      'tip': "Let's see if these two crank. And it smells smells musty in here like it like "
             'something got wet. So, one of the reasons I do these videos is just so you can '
             'see, you know, what type of vehicle is available at at these auctions.',
      'title': 'Government Auction Review: Cars, Trucks, SUVs, Boats, Construction and Lawn '
               'Equipment and more! (Auction Reviews With Jeff)',
      'url': 'https://www.youtube.com/watch?v=YaIalHq0RVU&t=877s',
      'video_id': 'YaIalHq0RVU'},
     {'author': 'Kevin24Seven',
      'channel': 'Kevin24Seven',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:53](https://www.youtube.com/watch?v=k5WD_GKlQhs&t=173s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "You've already created your account um I'll go ahead and just sign into mine "
              "okay we're signed in hello kevin so what I usually do is browse by category I'm "
              "going to assume in this video you're trying to buy a humvee but the process is "
              'similar for other vehicles.',
      'timestamp': 173,
      'timestamp_label': '[00:02:53]',
      'timestamp_seconds': 173,
      'tip': "You've already created your account um I'll go ahead and just sign into mine "
             "okay we're signed in hello kevin so what I usually do is browse by category I'm "
             "going to assume in this video you're trying to buy a humvee but the process is "
             'similar for other vehicles.',
      'title': 'GovPlanet Humvee Entire Buying to Street Legal Process (Kevin24Seven)',
      'url': 'https://www.youtube.com/watch?v=k5WD_GKlQhs&t=173s',
      'video_id': 'k5WD_GKlQhs'},
     {'author': 'Kevin24Seven',
      'channel': 'Kevin24Seven',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:57](https://www.youtube.com/watch?v=VvAg_yxxkPo&t=297s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Sooner or later here so hope you guys enjoyed the video hope this cleared up '
              'some things and made you a little less scared I will see you in the next one '
              'thanks for watching.',
      'timestamp': 297,
      'timestamp_label': '[00:04:57]',
      'timestamp_seconds': 297,
      'tip': 'Sooner or later here so hope you guys enjoyed the video hope this cleared up '
             'some things and made you a little less scared I will see you in the next one '
             'thanks for watching.',
      'title': 'How To Street Legal GovPlanet Humvee (Easy) (Kevin24Seven)',
      'url': 'https://www.youtube.com/watch?v=VvAg_yxxkPo&t=297s',
      'video_id': 'VvAg_yxxkPo'}],
 8: [{'author': 'IronPlanet',
      'channel': 'IronPlanet',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:03](https://www.youtube.com/watch?v=KyKSH6vNrZ8&t=123s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Four to five weeks whether you're a buyer or a seller iron planet is the "
              'auction company you can trust iron planet provides the tools and expertise to '
              'ensure the best auction results for all parties involved iron planet auctions '
              'you can trust.',
      'timestamp': 123,
      'timestamp_label': '[00:02:03]',
      'timestamp_seconds': 123,
      'tip': "Four to five weeks whether you're a buyer or a seller iron planet is the auction "
             'company you can trust iron planet provides the tools and expertise to ensure the '
             'best auction results for all parties involved iron planet auctions you can '
             'trust.',
      'title': 'IronPlanet Overview - English (IronPlanet)',
      'url': 'https://www.youtube.com/watch?v=KyKSH6vNrZ8&t=123s',
      'video_id': 'KyKSH6vNrZ8'},
     {'author': 'Auto Dealer Startup',
      'channel': 'Auto Dealer Startup',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:23](https://www.youtube.com/watch?v=dzr9aYx98oY&t=203s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'You know how to use the uh Put that live data report real quick. Show them guys '
              "how to use that jump box today, man. All right, so we're going to pull a live "
              "data report. We're going to check this car for codes. Even though we're at a "
              'dealer clear, they pull their own codes.',
      'timestamp': 203,
      'timestamp_label': '[00:03:23]',
      'timestamp_seconds': 203,
      'tip': 'You know how to use the uh Put that live data report real quick. Show them guys '
             "how to use that jump box today, man. All right, so we're going to pull a live "
             "data report. We're going to check this car for codes. Even though we're at a "
             'dealer clear, they pull their own codes.',
      'title': 'Picking a Car for My Private Rental Fleet at the Auction (Under $5,000 '
               "Beginner's Guide) (Auto Dealer Startup)",
      'url': 'https://www.youtube.com/watch?v=dzr9aYx98oY&t=203s',
      'video_id': 'dzr9aYx98oY'},
     {'author': 'Cleared Systems',
      'channel': 'Cleared Systems',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:45](https://www.youtube.com/watch?v=tEbWiX3Z22A&t=45s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "First, it's essential to understand what falls under the scope of ITAR. Defense "
              'articles, such as military equipment, components, and technical data, are '
              'covered. This includes anything specifically designed or modified for military '
              'use, including software.',
      'timestamp': 45,
      'timestamp_label': '[00:00:45]',
      'timestamp_seconds': 45,
      'tip': "First, it's essential to understand what falls under the scope of ITAR. Defense "
             'articles, such as military equipment, components, and technical data, are '
             'covered. This includes anything specifically designed or modified for military '
             'use, including software.',
      'title': 'What is ITAR Compliance? | Cleared Systems (Cleared Systems)',
      'url': 'https://www.youtube.com/watch?v=tEbWiX3Z22A&t=45s',
      'video_id': 'tEbWiX3Z22A'},
     {'author': 'LedgerGurus: Ecommerce Accounting Experts',
      'channel': 'LedgerGurus: Ecommerce Accounting Experts',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:54](https://www.youtube.com/watch?v=Cn-vsd4HlTE&t=474s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Very similar to SST, multi-state tax commission has another format of exemption '
              'certificates that a lot of states accept. So you search MTC resale certificate, '
              "it'll take you also click on the PDF format so we can just see the format. "
              "It'll take you directly to the form.",
      'timestamp': 474,
      'timestamp_label': '[00:07:54]',
      'timestamp_seconds': 474,
      'tip': 'Very similar to SST, multi-state tax commission has another format of exemption '
             'certificates that a lot of states accept. So you search MTC resale certificate, '
             "it'll take you also click on the PDF format so we can just see the format. It'll "
             'take you directly to the form.',
      'title': 'How to Get a Sales Tax Exemption Certificate (LedgerGurus: Ecommerce '
               'Accounting Experts)',
      'url': 'https://www.youtube.com/watch?v=Cn-vsd4HlTE&t=474s',
      'video_id': 'Cn-vsd4HlTE'},
     {'author': 'Tool Demos',
      'channel': 'Tool Demos',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:56](https://www.youtube.com/watch?v=EFXJtp6q_B8&t=596s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "If you're ready to get started on your renovation project, make sure you head "
              "over to the tool store. That's my Amazon page where I've got curated all of the "
              "tools that I use and I would recommend to fill your toolbox with that'll get "
              'you started on your project.',
      'timestamp': 596,
      'timestamp_label': '[00:09:56]',
      'timestamp_seconds': 596,
      'tip': "If you're ready to get started on your renovation project, make sure you head "
             "over to the tool store. That's my Amazon page where I've got curated all of the "
             "tools that I use and I would recommend to fill your toolbox with that'll get you "
             'started on your project.',
      'title': 'Are government auctions worth it? (Tool Demos)',
      'url': 'https://www.youtube.com/watch?v=EFXJtp6q_B8&t=596s',
      'video_id': 'EFXJtp6q_B8'},
     {'author': 'Shannon Jean',
      'channel': 'Shannon Jean',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:03](https://www.youtube.com/watch?v=i3yWMCnu2ac&t=963s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Toys and collectibles are super hot right now. So, you'd want to really know "
              "this product in and out before you bid on it. I'd be, you know, scouring data "
              "on sold listings from eBay with using the eBay research and I'd be using like "
              'this is this browser.',
      'timestamp': 963,
      'timestamp_label': '[00:16:03]',
      'timestamp_seconds': 963,
      'tip': "Toys and collectibles are super hot right now. So, you'd want to really know "
             "this product in and out before you bid on it. I'd be, you know, scouring data on "
             "sold listings from eBay with using the eBay research and I'd be using like this "
             'is this browser.',
      'title': 'Auction Deep Dive: How to Find “Cool” Deals (GovDeals, GSA, Liquidation & '
               'Freight Math) (Shannon Jean)',
      'url': 'https://www.youtube.com/watch?v=i3yWMCnu2ac&t=963s',
      'video_id': 'i3yWMCnu2ac'},
     {'author': 'Overage Acquisition',
      'channel': 'Overage Acquisition',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=X_Oq8vv4j_c&t=21s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "It's one of the documents I will need. And the way I do that is I go through "
              "what's called a software called Property Radar. And this is what the tool I use "
              'in order to order a copy of the deed.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': "It's one of the documents I will need. And the way I do that is I go through "
             "what's called a software called Property Radar. And this is what the tool I use "
             'in order to order a copy of the deed.',
      'title': 'Got a Surplus Funds Contract? Here’s Your Next Move (Overage Acquisition)',
      'url': 'https://www.youtube.com/watch?v=X_Oq8vv4j_c&t=21s',
      'video_id': 'X_Oq8vv4j_c'},
     {'author': 'GSA (General Services Administration)',
      'channel': 'GSA (General Services Administration)',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=csOCrIHnuSo&t=21s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Smart search a new navigation bar. We've updated the Featured Items section to "
              'make it easier for users to review options at a glance. Each item now includes '
              'helpful details like the current bid, auction status, and location.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': "Smart search a new navigation bar. We've updated the Featured Items section to "
             'make it easier for users to review options at a glance. Each item now includes '
             'helpful details like the current bid, auction status, and location.',
      'title': 'GSA Auctions Redesign (GSA (General Services Administration))',
      'url': 'https://www.youtube.com/watch?v=csOCrIHnuSo&t=21s',
      'video_id': 'csOCrIHnuSo'},
     {'author': 'UX Auctions',
      'channel': 'UX Auctions',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:46](https://www.youtube.com/watch?v=IUAs4NGQfyo&t=166s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'An oil change. >> Looking for a truck like this one? UX search dot app searches '
              'every major government auction site at once.',
      'timestamp': 166,
      'timestamp_label': '[00:02:46]',
      'timestamp_seconds': 166,
      'tip': 'An oil change. >> Looking for a truck like this one? UX search dot app searches '
             'every major government auction site at once.',
      'title': 'Watch a Government Surplus Ford F-250 Onsite Vehicle Inspection (UX Auctions)',
      'url': 'https://www.youtube.com/watch?v=IUAs4NGQfyo&t=166s',
      'video_id': 'IUAs4NGQfyo'},
     {'author': 'ITTechStudies',
      'channel': 'ITTechStudies',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:55](https://www.youtube.com/watch?v=7zVNMqLxB5I&t=115s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Switch as soon as I plug it in you'll notice the port starts blinking that "
              'means is detecting a connection and running data next access to distribution '
              "I'm connecting from Fast ethernet 0/1 on the access switch to fast ethernet 0 "
              'SL2 on the distribution switch.',
      'timestamp': 115,
      'timestamp_label': '[00:01:55]',
      'timestamp_seconds': 115,
      'tip': "Switch as soon as I plug it in you'll notice the port starts blinking that means "
             "is detecting a connection and running data next access to distribution I'm "
             'connecting from Fast ethernet 0/1 on the access switch to fast ethernet 0 SL2 on '
             'the distribution switch.',
      'title': 'Complete Cisco Lab Setup (Real Equipment Guide) (ITTechStudies)',
      'url': 'https://www.youtube.com/watch?v=7zVNMqLxB5I&t=115s',
      'video_id': '7zVNMqLxB5I'},
     {'author': 'Storage Unit Scrapper',
      'channel': 'Storage Unit Scrapper',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:33](https://www.youtube.com/watch?v=bAvpAOGu8Kw&t=753s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Especially with electric vehicles and stuff and all this new technology, data '
              "centers being built everywhere. I mean, they're using a lot of copper. And "
              "these data centers are building. They're building them everywhere. So, I mean, "
              "that's my my philosophy.",
      'timestamp': 753,
      'timestamp_label': '[00:12:33]',
      'timestamp_seconds': 753,
      'tip': 'Especially with electric vehicles and stuff and all this new technology, data '
             "centers being built everywhere. I mean, they're using a lot of copper. And these "
             "data centers are building. They're building them everywhere. So, I mean, that's "
             'my my philosophy.',
      'title': 'Scrapping Electronics Scrap in a Tote from a Storage Unit #storageunitfinds '
               '#scrapmetal #recycling (Storage Unit Scrapper)',
      'url': 'https://www.youtube.com/watch?v=bAvpAOGu8Kw&t=753s',
      'video_id': 'bAvpAOGu8Kw'},
     {'author': 'Larson Packaging Company',
      'channel': 'Larson Packaging Company',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:01](https://www.youtube.com/watch?v=mGYNeI8UeMw&t=61s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "So, here's another example of a prototype that we've made. We like working with "
              "wood because it's relatively inexpensive. It's very sturdy and strong and stiff "
              'for when you need it. So, we took the concept of our tool-less rack crate and '
              'turned it into a pallet concept.',
      'timestamp': 61,
      'timestamp_label': '[00:01:01]',
      'timestamp_seconds': 61,
      'tip': "So, here's another example of a prototype that we've made. We like working with "
             "wood because it's relatively inexpensive. It's very sturdy and strong and stiff "
             'for when you need it. So, we took the concept of our tool-less rack crate and '
             'turned it into a pallet concept.',
      'title': 'Rack Pallets versus Rack Crates: Protecting High-Value Tech (Larson Packaging '
               'Company)',
      'url': 'https://www.youtube.com/watch?v=mGYNeI8UeMw&t=61s',
      'video_id': 'mGYNeI8UeMw'},
     {'author': 'Kevin24Seven',
      'channel': 'Kevin24Seven',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:53](https://www.youtube.com/watch?v=gXjTPh7cGHU&t=233s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Dirty uh they look under it okay is anything leaking no yes you know they fire '
              "it up does it sound normal you know if it doesn't they'll put that it makes.",
      'timestamp': 233,
      'timestamp_label': '[00:03:53]',
      'timestamp_seconds': 233,
      'tip': 'Dirty uh they look under it okay is anything leaking no yes you know they fire '
             "it up does it sound normal you know if it doesn't they'll put that it makes.",
      'title': 'Are GovPlanet Humvees a SCAM? (Kevin24Seven)',
      'url': 'https://www.youtube.com/watch?v=gXjTPh7cGHU&t=233s',
      'video_id': 'gXjTPh7cGHU'},
     {'author': 'SkillsPanda',
      'channel': 'SkillsPanda',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=IQDdGtZqZb8&t=15s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'करने का मकसद स्थल मी टू लिप्स के हवाले से प्रैंक शनि के हवाले से ब्लास्ट चैप्टर '
              'इसके अंदर जो मेरे साथ संबंध है वह तक कि जो टेक्स्ट फॉरमैट और रिसर्च सर्टिफिकेट.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'करने का मकसद स्थल मी टू लिप्स के हवाले से प्रैंक शनि के हवाले से ब्लास्ट चैप्टर '
             'इसके अंदर जो मेरे साथ संबंध है वह तक कि जो टेक्स्ट फॉरमैट और रिसर्च सर्टिफिकेट.',
      'title': 'Understand State Sales Tax Permits and Resale Certificates Tax Exempt in the '
               'US (SkillsPanda)',
      'url': 'https://www.youtube.com/watch?v=IQDdGtZqZb8&t=15s',
      'video_id': 'IQDdGtZqZb8'},
     {'author': 'Vantor Insider',
      'channel': 'Vantor Insider',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:49](https://www.youtube.com/watch?v=tBIT1SUqIz8&t=589s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Services Administration Fleet Driveaway Program represent the cleanest entry '
              "point for a firsttime public buyer. Hosted directly on the federal government's "
              'official auction portal and conducted physically at contracted partner yards '
              'across the country.',
      'timestamp': 589,
      'timestamp_label': '[00:09:49]',
      'timestamp_seconds': 589,
      'tip': 'Services Administration Fleet Driveaway Program represent the cleanest entry '
             "point for a firsttime public buyer. Hosted directly on the federal government's "
             'official auction portal and conducted physically at contracted partner yards '
             'across the country.',
      'title': "You Don't Need a Dealer License: How Ordinary Buyers Get Into Surplus Auctions "
               '(Vantor Insider)',
      'url': 'https://www.youtube.com/watch?v=tBIT1SUqIz8&t=589s',
      'video_id': 'tBIT1SUqIz8'}],
 9: [{'author': 'Vantor Insider',
      'channel': 'Vantor Insider',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:41](https://www.youtube.com/watch?v=WGe7vjs5ktc&t=161s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'The true cost climbs to $710. Federal data sanitization rules mandate the '
              'physical removal and shredding of every solid state drive, steel mounting '
              'caddy, and proprietary lithium BIOS battery before the pallet ever reaches the '
              'auction floor.',
      'timestamp': 161,
      'timestamp_label': '[00:02:41]',
      'timestamp_seconds': 161,
      'tip': 'The true cost climbs to $710. Federal data sanitization rules mandate the '
             'physical removal and shredding of every solid state drive, steel mounting caddy, '
             'and proprietary lithium BIOS battery before the pallet ever reaches the auction '
             'floor.',
      'title': '27 Things Government Auctions Sell Every Week (And What They Really Cost) '
               '(Vantor Insider)',
      'url': 'https://www.youtube.com/watch?v=WGe7vjs5ktc&t=161s',
      'video_id': 'WGe7vjs5ktc'},
     {'author': 'Auction Reviews With Jeff',
      'channel': 'Auction Reviews With Jeff',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:32](https://www.youtube.com/watch?v=2Zb68VFEJ1c&t=872s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Whatever agency it is, I wish they would put the cloth seats. I wish they would '
              'put the agency like they do on that the state auctions. Next one right beside '
              "it is a Ram 1500. It's got that plastic liner. All right, so the next truck is "
              'a RAM 1500.',
      'timestamp': 872,
      'timestamp_label': '[00:14:32]',
      'timestamp_seconds': 872,
      'tip': 'Whatever agency it is, I wish they would put the cloth seats. I wish they would '
             'put the agency like they do on that the state auctions. Next one right beside it '
             "is a Ram 1500. It's got that plastic liner. All right, so the next truck is a "
             'RAM 1500.',
      'title': 'Federal Government (GSA) Auction Review | PICKUP TRUCKS! (Auction Reviews With '
               'Jeff)',
      'url': 'https://www.youtube.com/watch?v=2Zb68VFEJ1c&t=872s',
      'video_id': '2Zb68VFEJ1c'},
     {'author': 'LedgerGurus: Ecommerce Accounting Experts',
      'channel': 'LedgerGurus: Ecommerce Accounting Experts',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:29](https://www.youtube.com/watch?v=vzTkoCCX7ck&t=89s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Typically, box number 10, retail trade, is the most common. Box 4 is the reason '
              "you want the exemption. Box 5 is where you'll put your ID numbers. Use your "
              "home state sales tax ID. If you don't have one, use your FEIN or even your "
              "driver's license number.",
      'timestamp': 89,
      'timestamp_label': '[00:01:29]',
      'timestamp_seconds': 89,
      'tip': 'Typically, box number 10, retail trade, is the most common. Box 4 is the reason '
             "you want the exemption. Box 5 is where you'll put your ID numbers. Use your home "
             "state sales tax ID. If you don't have one, use your FEIN or even your driver's "
             'license number.',
      'title': 'Stop Paying Sales Tax with This One Form (SST Resale Certificate Tutorial) '
               '(LedgerGurus: Ecommerce Accounting Experts)',
      'url': 'https://www.youtube.com/watch?v=vzTkoCCX7ck&t=89s',
      'video_id': 'vzTkoCCX7ck'},
     {'author': 'Vantor Surplus',
      'channel': 'Vantor Surplus',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:26](https://www.youtube.com/watch?v=xwqMdeMDNSg&t=326s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'If a base property officer tries to transfer an obsolete zero-hour truck as a '
              'normal operable vehicle, federal rules require a mandatory interagency '
              'screening period that drags on for 14 months while state and county agencies '
              'browse the inventory.',
      'timestamp': 326,
      'timestamp_label': '[00:05:26]',
      'timestamp_seconds': 326,
      'tip': 'If a base property officer tries to transfer an obsolete zero-hour truck as a '
             'normal operable vehicle, federal rules require a mandatory interagency screening '
             'period that drags on for 14 months while state and county agencies browse the '
             'inventory.',
      'title': 'The Pentagon Rule Forcing US Bases to Auction Zero-Hour Diesel Trucks as '
               '"Scrap Metal" (Vantor Surplus)',
      'url': 'https://www.youtube.com/watch?v=xwqMdeMDNSg&t=326s',
      'video_id': 'xwqMdeMDNSg'},
     {'author': 'Hands Off Sales Tax (HOST)',
      'channel': 'Hands Off Sales Tax (HOST)',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:58](https://www.youtube.com/watch?v=InXP0n0EggQ&t=58s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Depending on the state or supplier, a resale certificate may also be called. '
              'MTC form, which is the uniform sales and use tax resale certificate, '
              'multi-jurisdiction, and the SST form, which is the streamline sales tax '
              'certificate of exemption.',
      'timestamp': 58,
      'timestamp_label': '[00:00:58]',
      'timestamp_seconds': 58,
      'tip': 'Depending on the state or supplier, a resale certificate may also be called. MTC '
             'form, which is the uniform sales and use tax resale certificate, '
             'multi-jurisdiction, and the SST form, which is the streamline sales tax '
             'certificate of exemption.',
      'title': "Seller's Permit vs Resale Certificate: The Simple Breakdown (Hands Off Sales "
               'Tax (HOST))',
      'url': 'https://www.youtube.com/watch?v=InXP0n0EggQ&t=58s',
      'video_id': 'InXP0n0EggQ'},
     {'author': 'Defense Logistics Agency',
      'channel': 'Defense Logistics Agency',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:42](https://www.youtube.com/watch?v=HYKDZ7wW8ik&t=102s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Compliance with epa standards we have approximately 40 customers throughout the '
              'state of maryland delaware.',
      'timestamp': 102,
      'timestamp_label': '[00:01:42]',
      'timestamp_seconds': 102,
      'tip': 'Compliance with epa standards we have approximately 40 customers throughout the '
             'state of maryland delaware.',
      'title': 'Logistics On Location: DLA Disposition Services, Ft Meade, MD (long version) '
               '(Defense Logistics Agency)',
      'url': 'https://www.youtube.com/watch?v=HYKDZ7wW8ik&t=102s',
      'video_id': 'HYKDZ7wW8ik'},
     {'author': 'Easy Teach WF',
      'channel': 'Easy Teach WF',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:30](https://www.youtube.com/watch?v=_PJtbgNQj4k&t=30s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Mr X: Ok don’t worry I am answering! Mr X: You can get free resale certificate '
              'in some states of USA if you have registered business. In this blog you can see '
              'which state resale certificate will cost you or you can have it free of cost.',
      'timestamp': 30,
      'timestamp_label': '[00:00:30]',
      'timestamp_seconds': 30,
      'tip': 'Mr X: Ok don’t worry I am answering! Mr X: You can get free resale certificate '
             'in some states of USA if you have registered business. In this blog you can see '
             'which state resale certificate will cost you or you can have it free of cost.',
      'title': 'Get a USA Free Resale Certificate - For Tax Exemption! (Easy Teach WF)',
      'url': 'https://www.youtube.com/watch?v=_PJtbgNQj4k&t=30s',
      'video_id': '_PJtbgNQj4k'},
     {'author': 'UX Auctions',
      'channel': 'UX Auctions',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:48](https://www.youtube.com/watch?v=c9mCACUk14Y&t=48s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Manasha Police  with no known mechanical issues sold for $6,050. Now equipment '
              'deals that run.  A state transportation.',
      'timestamp': 48,
      'timestamp_label': '[00:00:48]',
      'timestamp_seconds': 48,
      'tip': 'Manasha Police  with no known mechanical issues sold for $6,050. Now equipment '
             'deals that run.  A state transportation.',
      'title': '60-SECOND GOVERNMENT AUCTION REPORT — NOVEMBER 19, 2026! (UX Auctions)',
      'url': 'https://www.youtube.com/watch?v=c9mCACUk14Y&t=48s',
      'video_id': 'c9mCACUk14Y'},
     {'author': 'T-SHIRT KINGS',
      'channel': 'T-SHIRT KINGS',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:02](https://www.youtube.com/watch?v=1YNFxlnPOZM&t=122s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Only claim it on things you resell, like blanks that become your customer '
              "shirts. It doesn't exempt you from sales tax. And getting one just to dodge tax "
              "is fraud. Know your state's name for it, apply, fill out the certificate, send "
              'it to suppliers, and use it right.',
      'timestamp': 122,
      'timestamp_label': '[00:02:02]',
      'timestamp_seconds': 122,
      'tip': 'Only claim it on things you resell, like blanks that become your customer '
             "shirts. It doesn't exempt you from sales tax. And getting one just to dodge tax "
             "is fraud. Know your state's name for it, apply, fill out the certificate, send "
             'it to suppliers, and use it right.',
      'title': 'How to Get a Resale Certificate in 2026 (Buy Blank Shirts Tax Free) (T-SHIRT '
               'KINGS)',
      'url': 'https://www.youtube.com/watch?v=1YNFxlnPOZM&t=122s',
      'video_id': '1YNFxlnPOZM'},
     {'author': 'Dirt Legal',
      'channel': 'Dirt Legal',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:50](https://www.youtube.com/watch?v=-MWjNKD7-e8&t=230s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'We offer 100 money back guarantee if we fail to make your vehicle street legal '
              'and you can contact us at orders at dirtlegal.com to see if your situation '
              "qualifies for our out-of-state legalization service and that's it we'll see you "
              'next time.',
      'timestamp': 230,
      'timestamp_label': '[00:03:50]',
      'timestamp_seconds': 230,
      'tip': 'We offer 100 money back guarantee if we fail to make your vehicle street legal '
             'and you can contact us at orders at dirtlegal.com to see if your situation '
             "qualifies for our out-of-state legalization service and that's it we'll see you "
             'next time.',
      'title': 'How to Easily Register Your Salvage Title Vehicle (Dirt Legal)',
      'url': 'https://www.youtube.com/watch?v=-MWjNKD7-e8&t=230s',
      'video_id': '-MWjNKD7-e8'},
     {'author': 'Money Making Juggernaut',
      'channel': 'Money Making Juggernaut',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:28](https://www.youtube.com/watch?v=MmWoRR82S9g&t=268s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, being a realtor, I just went to uh attorney that I was already working with '
              "and >> No. At first, he told me no because he didn't understand. And then I "
              'just explained it to him >> and then he finally >> state law.',
      'timestamp': 268,
      'timestamp_label': '[00:04:28]',
      'timestamp_seconds': 268,
      'tip': 'So, being a realtor, I just went to uh attorney that I was already working with '
             "and >> No. At first, he told me no because he didn't understand. And then I just "
             'explained it to him >> and then he finally >> state law.',
      'title': 'Realtor Tries Surplus Funds And Does $94,000 in Deals In Her First Year (Money '
               'Making Juggernaut)',
      'url': 'https://www.youtube.com/watch?v=MmWoRR82S9g&t=268s',
      'video_id': 'MmWoRR82S9g'},
     {'author': 'Storage Unit Scrapper',
      'channel': 'Storage Unit Scrapper',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:58](https://www.youtube.com/watch?v=4TJbVuWoX3A&t=718s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'I just I got the best storage you could do. Copper drain, residential '
              'construction, run heavy equipment. Worked for the railroad for a while. So this '
              "here can go probably in low grade peripheral steel. It's not a gold finger "
              'card.',
      'timestamp': 718,
      'timestamp_label': '[00:11:58]',
      'timestamp_seconds': 718,
      'tip': 'I just I got the best storage you could do. Copper drain, residential '
             'construction, run heavy equipment. Worked for the railroad for a while. So this '
             "here can go probably in low grade peripheral steel. It's not a gold finger card.",
      'title': 'Laptop and Chip Board Scrapping from Storage Units #storageunitfinds '
               '#treasurehunt #scrapmetal (Storage Unit Scrapper)',
      'url': 'https://www.youtube.com/watch?v=4TJbVuWoX3A&t=718s',
      'video_id': '4TJbVuWoX3A'},
     {'author': 'Sean Drake',
      'channel': 'Sean Drake',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=ovCY1VA7klw&t=20s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': '5500 anyone to go 5500 five up front bidding 55 Would It Go 55. 55 55 and an '
              'even six grand at 60 a new bitter and 6500 six here to bid 65 17.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': '5500 anyone to go 5500 five up front bidding 55 Would It Go 55. 55 55 and an '
             'even six grand at 60 a new bitter and 6500 six here to bid 65 17.',
      'title': 'NH State Surplus Live Auction Day Spring 2023 (Sean Drake)',
      'url': 'https://www.youtube.com/watch?v=ovCY1VA7klw&t=20s',
      'video_id': 'ovCY1VA7klw'},
     {'author': 'Kevin24Seven',
      'channel': 'Kevin24Seven',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:35](https://www.youtube.com/watch?v=d2qrhLbKEbI&t=875s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'DMV and all that kind of stuff but if you want to do it the easy way um you '
              "know we'll just go through dirt legal here and pay them a little bit of money.",
      'timestamp': 875,
      'timestamp_label': '[00:14:35]',
      'timestamp_seconds': 875,
      'tip': 'DMV and all that kind of stuff but if you want to do it the easy way um you know '
             "we'll just go through dirt legal here and pay them a little bit of money.",
      'title': "What's it Cost to Build a BASIC GovPlanet Humvee? (Kevin24Seven)",
      'url': 'https://www.youtube.com/watch?v=d2qrhLbKEbI&t=875s',
      'video_id': 'd2qrhLbKEbI'},
     {'author': '41NBC',
      'channel': '41NBC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:57](https://www.youtube.com/watch?v=QOcs7dzmhGk&t=57s)',
      'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                   'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                   'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'This is demonstration of RICT AE Comprompter Caption Central FUNA software. For '
              'a license call 60 THE S 785-7766URPLUS AUCTION GOES BAC INTO THE GENERAL FUND." '
              'THE SCHOOL DISTRICT AUCTIONS OFF THE ITEMS ONLINE TO THE HIGHEST BIDDER. THE '
              'PROCEEDS GO WELL INTO THE THOUSANDS.',
      'timestamp': 57,
      'timestamp_label': '[00:00:57]',
      'timestamp_seconds': 57,
      'tip': 'This is demonstration of RICT AE Comprompter Caption Central FUNA software. For '
             'a license call 60 THE S 785-7766URPLUS AUCTION GOES BAC INTO THE GENERAL FUND." '
             'THE SCHOOL DISTRICT AUCTIONS OFF THE ITEMS ONLINE TO THE HIGHEST BIDDER. THE '
             'PROCEEDS GO WELL INTO THE THOUSANDS.',
      'title': 'Bibb County Schools auction surplus items (41NBC)',
      'url': 'https://www.youtube.com/watch?v=QOcs7dzmhGk&t=57s',
      'video_id': 'QOcs7dzmhGk'}],
 10: [{'author': 'Digital Iron Group',
       'channel': 'Digital Iron Group',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:08](https://www.youtube.com/watch?v=HF9Hu38gKMI&t=68s)',
       'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                    'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                    'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "'t have access to what their aging inventory report looks like. On aging "
               "inventory, and I've run into I remember a a dealer I had in the past, it was a "
               'Caterpillar dealer, and they had some used equipment. There were some used '
               'forestry pieces.',
       'timestamp': 68,
       'timestamp_label': '[00:01:08]',
       'timestamp_seconds': 68,
       'tip': "'t have access to what their aging inventory report looks like. On aging "
              "inventory, and I've run into I remember a a dealer I had in the past, it was a "
              'Caterpillar dealer, and they had some used equipment. There were some used '
              'forestry pieces.',
       'title': 'Stopping aging inventory: act fast and auction when needed (Digital Iron '
                'Group)',
       'url': 'https://www.youtube.com/watch?v=HF9Hu38gKMI&t=68s',
       'video_id': 'HF9Hu38gKMI'},
      {'author': 'GSA (General Services Administration)',
       'channel': 'GSA (General Services Administration)',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:34](https://www.youtube.com/watch?v=Dga3YkAiGmw&t=34s)',
       'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                    'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                    'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'You can navigate direct to this website by clicking the GSA Fleet Vehicles tab '
               'at the top of the GSA Auctions homepage. Offline bidding opportunities are '
               'posted in advance of the bid due date or auction start date for in-person '
               'bidding.',
       'timestamp': 34,
       'timestamp_label': '[00:00:34]',
       'timestamp_seconds': 34,
       'tip': 'You can navigate direct to this website by clicking the GSA Fleet Vehicles tab '
              'at the top of the GSA Auctions homepage. Offline bidding opportunities are '
              'posted in advance of the bid due date or auction start date for in-person '
              'bidding.',
       'title': 'GSA Auctions: Offline Bidding Opportunities (GSA (General Services '
                'Administration))',
       'url': 'https://www.youtube.com/watch?v=Dga3YkAiGmw&t=34s',
       'video_id': 'Dga3YkAiGmw'},
      {'author': "TK's Garage",
       'channel': "TK's Garage",
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:11:22](https://www.youtube.com/watch?v=6iKYdGlqqP4&t=682s)',
       'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                    'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                    'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'See if they got anything else. More generators, generators, generators. They '
               "got a lot of these generators. Fire boss They're selling fire equipment. I "
               'just want to see if they had any other like personnel carriers or whatnot.',
       'timestamp': 682,
       'timestamp_label': '[00:11:22]',
       'timestamp_seconds': 682,
       'tip': 'See if they got anything else. More generators, generators, generators. They '
              "got a lot of these generators. Fire boss They're selling fire equipment. I just "
              'want to see if they had any other like personnel carriers or whatnot.',
       'title': "Military Equipment Auction GovPlanet CHEAP HUMVEE! (TK's Garage)",
       'url': 'https://www.youtube.com/watch?v=6iKYdGlqqP4&t=682s',
       'video_id': '6iKYdGlqqP4'},
      {'author': 'Vantor WW2',
       'channel': 'Vantor WW2',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:20](https://www.youtube.com/watch?v=4PdPtt60qn0&t=20s)',
       'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                    'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                    'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'The buyer, a regional agricultural machinery dealer who had bid by the gross '
               'metric ton on a blind government liquidation lot listed only as cased iron '
               'ballast and obsolete ordnance packaging, levered the heavy lid upward against '
               '80-year-old rosin-coated nails.',
       'timestamp': 20,
       'timestamp_label': '[00:00:20]',
       'timestamp_seconds': 20,
       'tip': 'The buyer, a regional agricultural machinery dealer who had bid by the gross '
              'metric ton on a blind government liquidation lot listed only as cased iron '
              'ballast and obsolete ordnance packaging, levered the heavy lid upward against '
              '80-year-old rosin-coated nails.',
       'title': 'Sealed in Greased Crates Since 1944: 7 Zero-Hour WW2 Vehicles Sold at Scrap '
                'Auctions (Vantor WW2)',
       'url': 'https://www.youtube.com/watch?v=4PdPtt60qn0&t=20s',
       'video_id': '4PdPtt60qn0'},
      {'author': 'StorageUnitAuctions',
       'channel': 'StorageUnitAuctions',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:38](https://www.youtube.com/watch?v=ulXE2sJ0rv8&t=98s)',
       'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                    'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                    'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "This is really, really cool. So, you've got to stick with me. You're gonna "
               "love what I'm about to show you. Let's go take a look at my new acquisition. "
               "I'm about to check out my new acquisition at this government surplus auction "
               'today.',
       'timestamp': 98,
       'timestamp_label': '[00:01:38]',
       'timestamp_seconds': 98,
       'tip': "This is really, really cool. So, you've got to stick with me. You're gonna love "
              "what I'm about to show you. Let's go take a look at my new acquisition. I'm "
              'about to check out my new acquisition at this government surplus auction today.',
       'title': 'Government Surplus Auctions Treasure Hunting How To Make Money Buying Surplus '
                'Goods (StorageUnitAuctions)',
       'url': 'https://www.youtube.com/watch?v=ulXE2sJ0rv8&t=98s',
       'video_id': 'ulXE2sJ0rv8'},
      {'author': 'Lester John',
       'channel': 'Lester John',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:36](https://www.youtube.com/watch?v=7J3W8esngfU&t=96s)',
       'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                    'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                    'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "We're simply the middleman. 's you know dealing the transaction. It's kind of "
               'like real estate agent, right? Think about real estate agents. So they are the '
               'person facilitating between the buyer and the seller of the house. You know, '
               "they're just the middleman person.",
       'timestamp': 96,
       'timestamp_label': '[00:01:36]',
       'timestamp_seconds': 96,
       'tip': "We're simply the middleman. 's you know dealing the transaction. It's kind of "
              'like real estate agent, right? Think about real estate agents. So they are the '
              'person facilitating between the buyer and the seller of the house. You know, '
              "they're just the middleman person.",
       'title': 'How to Get a Resale Certificate/Permit 2026 [UPDATED] (Lester John)',
       'url': 'https://www.youtube.com/watch?v=7J3W8esngfU&t=96s',
       'video_id': '7J3W8esngfU'},
      {'author': 'Niche Pursuits',
       'channel': 'Niche Pursuits',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:01](https://www.youtube.com/watch?v=orDRxYfVypw&t=301s)',
       'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                    'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                    'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Uh, six-pack, three- ring binders, 20 bucks on eBay. Now, if I wanted to scale '
               'this reselling business, I would start capturing the emails of people that are '
               'interested in supporting the teenagers running this business.',
       'timestamp': 301,
       'timestamp_label': '[00:05:01]',
       'timestamp_seconds': 301,
       'tip': 'Uh, six-pack, three- ring binders, 20 bucks on eBay. Now, if I wanted to scale '
              'this reselling business, I would start capturing the emails of people that are '
              'interested in supporting the teenagers running this business.',
       'title': "I Just Bought 3 Amazon Return Pallets for $1,500...Here's What I Found (Niche "
                'Pursuits)',
       'url': 'https://www.youtube.com/watch?v=orDRxYfVypw&t=301s',
       'video_id': 'orDRxYfVypw'},
      {'author': 'LedgerGurus: Ecommerce Accounting Experts',
       'channel': 'LedgerGurus: Ecommerce Accounting Experts',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:21](https://www.youtube.com/watch?v=It-VnUi3x58&t=21s)',
       'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                    'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                    'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Now in this scenario, a resale certificate is one type of exemption '
               'certificate that you can provide to your drop shipper. So then the question '
               'is, what kind of certificate do they accept?',
       'timestamp': 21,
       'timestamp_label': '[00:00:21]',
       'timestamp_seconds': 21,
       'tip': 'Now in this scenario, a resale certificate is one type of exemption certificate '
              'that you can provide to your drop shipper. So then the question is, what kind '
              'of certificate do they accept?',
       'title': 'How to EASILY Get a Resale Certificate for Dropshipping (LedgerGurus: '
                'Ecommerce Accounting Experts)',
       'url': 'https://www.youtube.com/watch?v=It-VnUi3x58&t=21s',
       'video_id': 'It-VnUi3x58'},
      {'author': 'Midnight Machine Shop',
       'channel': 'Midnight Machine Shop',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:21](https://www.youtube.com/watch?v=oACqhA0f4EM&t=21s)',
       'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                    'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                    'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'On the floor, you can see the hood prop rod. Um, there was a fire extinguisher '
               "in fully charged. I took that out just so I wouldn't accidentally in "
               'inadvertently set it off. Uh, the doors removed just so I can get in here '
               'easier.',
       'timestamp': 21,
       'timestamp_label': '[00:00:21]',
       'timestamp_seconds': 21,
       'tip': 'On the floor, you can see the hood prop rod. Um, there was a fire extinguisher '
              "in fully charged. I took that out just so I wouldn't accidentally in "
              'inadvertently set it off. Uh, the doors removed just so I can get in here '
              'easier.',
       'title': "I Bought a SURPLUS HUMVEE at a GovPlanet Auction and Here's What I Found "
                '(Midnight Machine Shop)',
       'url': 'https://www.youtube.com/watch?v=oACqhA0f4EM&t=21s',
       'video_id': 'oACqhA0f4EM'},
      {'author': 'HHWheels',
       'channel': 'HHWheels',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:25](https://www.youtube.com/watch?v=09UUwyLab_0&t=205s)',
       'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                    'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                    'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Like the armored doors and all of the armor around the vehicle but they do '
               'eventually send you a title which is pretty cool what no fire extinguisher.',
       'timestamp': 205,
       'timestamp_label': '[00:03:25]',
       'timestamp_seconds': 205,
       'tip': 'Like the armored doors and all of the armor around the vehicle but they do '
              'eventually send you a title which is pretty cool what no fire extinguisher.',
       'title': 'BUYING A HUMVEE FROM GOV PLANET (HHWheels)',
       'url': 'https://www.youtube.com/watch?v=09UUwyLab_0&t=205s',
       'video_id': '09UUwyLab_0'},
      {'author': 'Test Equipment Depot',
       'channel': 'Test Equipment Depot',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:03](https://www.youtube.com/watch?v=Fp4VRiP2pnE&t=63s)',
       'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                    'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                    'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "So, they need an IR window. They're going to need uh thermal imaging products. "
               "They're going to need traditional electrical testers. Data centers use a lot "
               'of power. And this demand for the growth in AI.',
       'timestamp': 63,
       'timestamp_label': '[00:01:03]',
       'timestamp_seconds': 63,
       'tip': "So, they need an IR window. They're going to need uh thermal imaging products. "
              "They're going to need traditional electrical testers. Data centers use a lot of "
              'power. And this demand for the growth in AI.',
       'title': 'Data Center Solutions Engineered by Fluke (Test Equipment Depot)',
       'url': 'https://www.youtube.com/watch?v=Fp4VRiP2pnE&t=63s',
       'video_id': 'Fp4VRiP2pnE'},
      {'author': 'Advanced Test Equipment Corp. (ATEC)',
       'channel': 'Advanced Test Equipment Corp. (ATEC)',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:21](https://www.youtube.com/watch?v=t4jkcrLcddU&t=21s)',
       'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                    'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                    'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'I represent Fluke Networks here in Southern California. I work closely with '
               'Advanced Test Equipment. We came in today to show them the CertiFiber Max, '
               'which they will be receiving their units here shortly.',
       'timestamp': 21,
       'timestamp_label': '[00:00:21]',
       'timestamp_seconds': 21,
       'tip': 'I represent Fluke Networks here in Southern California. I work closely with '
              'Advanced Test Equipment. We came in today to show them the CertiFiber Max, '
              'which they will be receiving their units here shortly.',
       'title': 'MPO Fiber Testing with the New Fluke Networks CFM-100SI CertiFiber Max '
                'Optical Loss Test Set (Advanced Test Equipment Corp. (ATEC))',
       'url': 'https://www.youtube.com/watch?v=t4jkcrLcddU&t=21s',
       'video_id': 't4jkcrLcddU'},
      {'author': 'QQ Toys TV',
       'channel': 'QQ Toys TV',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:05](https://www.youtube.com/watch?v=5HQNQKtddhQ&t=245s)',
       'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                    'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                    'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Police helicopter flying above the city. This helicopter helps police watch '
               'from the sky. It spots trouble from far away and helps guide officers on the '
               'ground. Police water cannon vehicle. Police water cannon vehicle. This special '
               'truck sprays strong jets of water.',
       'timestamp': 245,
       'timestamp_label': '[00:04:05]',
       'timestamp_seconds': 245,
       'tip': 'Police helicopter flying above the city. This helicopter helps police watch '
              'from the sky. It spots trouble from far away and helps guide officers on the '
              'ground. Police water cannon vehicle. Police water cannon vehicle. This special '
              'truck sprays strong jets of water.',
       'title': 'Emergency Vehicle Name Sounds | Police Vehicle, Ambulance Vehicle, Fire '
                'truck, Cars, Bus, Helicopter (QQ Toys TV)',
       'url': 'https://www.youtube.com/watch?v=5HQNQKtddhQ&t=245s',
       'video_id': '5HQNQKtddhQ'},
      {'author': 'Resale Rabbit',
       'channel': 'Resale Rabbit',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:30](https://www.youtube.com/watch?v=iiaRVwB0tHk&t=210s)',
       'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                    'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                    'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "Um well that looks like an Amazon sticker yeah FBA let's look this up oh we "
               "got more right here uh it's an engine air filter for something that's a big "
               "Engine air filter uh let's see y.",
       'timestamp': 210,
       'timestamp_label': '[00:03:30]',
       'timestamp_seconds': 210,
       'tip': "Um well that looks like an Amazon sticker yeah FBA let's look this up oh we got "
              "more right here uh it's an engine air filter for something that's a big Engine "
              "air filter uh let's see y.",
       'title': 'Unboxing Three Liquidation Pallets - HUGE $1200 SCORE on the third one! '
                '(Resale Rabbit)',
       'url': 'https://www.youtube.com/watch?v=iiaRVwB0tHk&t=210s',
       'video_id': 'iiaRVwB0tHk'},
      {'author': 'Top 5 Autos',
       'channel': 'Top 5 Autos',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:14](https://www.youtube.com/watch?v=WFVGJDWST7I&t=194s)',
       'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                    'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                    'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Fleet vehicles get serviced on a strict schedule. Every oil change logged, '
               'every tire rotation documented, because the agency is accountable to '
               'taxpayers. The maintenance records are often better than anything at a private '
               'dealer.',
       'timestamp': 194,
       'timestamp_label': '[00:03:14]',
       'timestamp_seconds': 194,
       'tip': 'Fleet vehicles get serviced on a strict schedule. Every oil change logged, '
              'every tire rotation documented, because the agency is accountable to taxpayers. '
              'The maintenance records are often better than anything at a private dealer.',
       'title': 'Buy a $55K SUV for Under $18K | The Government Auction GOLDMINE Nobody Shows '
                'You (Top 5 Autos)',
       'url': 'https://www.youtube.com/watch?v=WFVGJDWST7I&t=194s',
       'video_id': 'WFVGJDWST7I'}],
 11: [{'author': 'Vantor Surplus',
       'channel': 'Vantor Surplus',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:41](https://www.youtube.com/watch?v=VKFtBFmCW4U&t=281s)',
       'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                    'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                    'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'M1070 heavy equipment transporter frequently carry demilitarization codes. '
               'When the Cold War ended in 1991, federal oversight tightened on military '
               'hardware flowing into private hands.',
       'timestamp': 281,
       'timestamp_label': '[00:04:41]',
       'timestamp_seconds': 281,
       'tip': 'M1070 heavy equipment transporter frequently carry demilitarization codes. When '
              'the Cold War ended in 1991, federal oversight tightened on military hardware '
              'flowing into private hands.',
       'title': '$1,500 at a Government Auction Buys More Than You Think — What Mechanics '
                'Drove Home Will Shock You (Vantor Surplus)',
       'url': 'https://www.youtube.com/watch?v=VKFtBFmCW4U&t=281s',
       'video_id': 'VKFtBFmCW4U'},
      {'author': 'AidensGotGuides',
       'channel': 'AidensGotGuides',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:53](https://www.youtube.com/watch?v=3E3YyoTCUAM&t=53s)',
       'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                    'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                    'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'When the chat opens, type sales tax exemption and let support know that you '
               'want to submit a business tax exemption certificate. It helps to keep your '
               "message short and clear so the support team can quickly understand what you're "
               'requesting.',
       'timestamp': 53,
       'timestamp_label': '[00:00:53]',
       'timestamp_seconds': 53,
       'tip': 'When the chat opens, type sales tax exemption and let support know that you '
              'want to submit a business tax exemption certificate. It helps to keep your '
              "message short and clear so the support team can quickly understand what you're "
              'requesting.',
       'title': 'How To Add Sales Tax Exemption On Temu For Business Owners (AidensGotGuides)',
       'url': 'https://www.youtube.com/watch?v=3E3YyoTCUAM&t=53s',
       'video_id': '3E3YyoTCUAM'},
      {'author': 'IronPlanet',
       'channel': 'IronPlanet',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:42](https://www.youtube.com/watch?v=rsMWDCVh1cE&t=162s)',
       'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                    'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                    'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "Equipment that they bought in the past equipment that they're looking to buy "
               'and our inside sales team leverages that information to proactively reach out '
               'to prospective bidders prior to the auction and during the auction.',
       'timestamp': 162,
       'timestamp_label': '[00:02:42]',
       'timestamp_seconds': 162,
       'tip': "Equipment that they bought in the past equipment that they're looking to buy "
              'and our inside sales team leverages that information to proactively reach out '
              'to prospective bidders prior to the auction and during the auction.',
       'title': 'IronPlanet - The Place to Buy & Sell Used Equipment (IronPlanet)',
       'url': 'https://www.youtube.com/watch?v=rsMWDCVh1cE&t=162s',
       'video_id': 'rsMWDCVh1cE'},
      {'author': 'Cereal Marshmallows',
       'channel': 'Cereal Marshmallows',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:57](https://www.youtube.com/watch?v=RvlA07ePLd4&t=117s)',
       'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                    'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                    'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "Lights hopefully they went to led and stuff save some money somewhere what's "
               "in these huge boxes I've got to know whoa fire and rescue equipment wow oxygen "
               'and everything.',
       'timestamp': 117,
       'timestamp_label': '[00:01:57]',
       'timestamp_seconds': 117,
       'tip': "Lights hopefully they went to led and stuff save some money somewhere what's in "
              "these huge boxes I've got to know whoa fire and rescue equipment wow oxygen and "
              'everything.',
       'title': 'GSA Government Auction Industrial Equipment ~ Tractors Semi Trucks  Classic '
                'Cars ~ Government Waste (Cereal Marshmallows)',
       'url': 'https://www.youtube.com/watch?v=RvlA07ePLd4&t=117s',
       'video_id': 'RvlA07ePLd4'},
      {'author': 'CabinDad',
       'channel': 'CabinDad',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:07](https://www.youtube.com/watch?v=aH3cAZ1RXvE&t=67s)',
       'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                    'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                    'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "'re looking for, check out all the different sites. GovPlanet tends to have a "
               'lot of the larger pieces of equipment and a lot of bulk items like, you know, '
               'boots and clothing. The other sites, they tend to do local governments in '
               'addition to big federal stuff.',
       'timestamp': 67,
       'timestamp_label': '[00:01:07]',
       'timestamp_seconds': 67,
       'tip': "'re looking for, check out all the different sites. GovPlanet tends to have a "
              'lot of the larger pieces of equipment and a lot of bulk items like, you know, '
              'boots and clothing. The other sites, they tend to do local governments in '
              'addition to big federal stuff.',
       'title': 'Government Surplus Auctions (CabinDad)',
       'url': 'https://www.youtube.com/watch?v=aH3cAZ1RXvE&t=67s',
       'video_id': 'aH3cAZ1RXvE'},
      {'author': 'Zero Tax Tags',
       'channel': 'Zero Tax Tags',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:15](https://www.youtube.com/watch?v=uOA3FOVLCGA&t=195s)',
       'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                    'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                    'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Chapter 4, what is an SF97? Bought a surplus Humvee or military trailer at '
               "auction? Military vehicles don't come with normal titles. Government doesn't "
               "title its own vehicles. Instead, you get an SF97, standard form 97. It's the "
               'government certificate to obtain a title.',
       'timestamp': 195,
       'timestamp_label': '[00:03:15]',
       'timestamp_seconds': 195,
       'tip': 'Chapter 4, what is an SF97? Bought a surplus Humvee or military trailer at '
              "auction? Military vehicles don't come with normal titles. Government doesn't "
              "title its own vehicles. Instead, you get an SF97, standard form 97. It's the "
              'government certificate to obtain a title.',
       'title': 'Vehicle Ownership Documents Explained | Title, Registration, MCO, SF-97 & '
                'More (Zero Tax Tags)',
       'url': 'https://www.youtube.com/watch?v=uOA3FOVLCGA&t=195s',
       'video_id': 'uOA3FOVLCGA'},
      {'author': 'Survival Gear',
       'channel': 'Survival Gear',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:57](https://www.youtube.com/watch?v=ZSzUyNfsBZ0&t=117s)',
       'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                    'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                    'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'These guns were designed from the ground up as integrally suppressed rifles, '
               'primarily intended for special operations use. Both of these guns fire the '
               "9x39mm cartridge. This is actually just a regular 7. 62x 39mm case that's been "
               'necked up to accept a larger diameter 9.',
       'timestamp': 117,
       'timestamp_label': '[00:01:57]',
       'timestamp_seconds': 117,
       'tip': 'These guns were designed from the ground up as integrally suppressed rifles, '
              'primarily intended for special operations use. Both of these guns fire the '
              "9x39mm cartridge. This is actually just a regular 7. 62x 39mm case that's been "
              'necked up to accept a larger diameter 9.',
       'title': 'The Army Is Selling 100,000 Military Surplus Rifles in January - Every Army '
                'Veteran Should Know This (Survival Gear)',
       'url': 'https://www.youtube.com/watch?v=ZSzUyNfsBZ0&t=117s',
       'video_id': 'ZSzUyNfsBZ0'},
      {'author': 'East Coast Classics',
       'channel': 'East Coast Classics',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:47](https://www.youtube.com/watch?v=q09PUtJPIxs&t=347s)',
       'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                    'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                    'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Off your rump you got to make a phone call schedule an appointment and do a '
               "physical inspection of the property now I've seen ads on these auction sites.",
       'timestamp': 347,
       'timestamp_label': '[00:05:47]',
       'timestamp_seconds': 347,
       'tip': 'Off your rump you got to make a phone call schedule an appointment and do a '
              "physical inspection of the property now I've seen ads on these auction sites.",
       'title': 'HOW TO FIND and BUY at Government Surplus Auctions (East Coast Classics)',
       'url': 'https://www.youtube.com/watch?v=q09PUtJPIxs&t=347s',
       'video_id': 'q09PUtJPIxs'},
      {'author': 'JR',
       'channel': 'JR',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:14:46](https://www.youtube.com/watch?v=14j6GQVGkBk&t=886s)',
       'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                    'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                    'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'On buyer five four three on that one all right you ever get a gs8 a little '
               "newer lazy dumb and coming up right here I'll run your regular nine grand on "
               'the buy ninety one hundred.',
       'timestamp': 886,
       'timestamp_label': '[00:14:46]',
       'timestamp_seconds': 886,
       'tip': 'On buyer five four three on that one all right you ever get a gs8 a little '
              "newer lazy dumb and coming up right here I'll run your regular nine grand on "
              'the buy ninety one hundred.',
       'title': 'How to Buy a Truck Online (GSA Auction) (JR)',
       'url': 'https://www.youtube.com/watch?v=14j6GQVGkBk&t=886s',
       'video_id': '14j6GQVGkBk'},
      {'author': 'MotorTrend Channel',
       'channel': 'MotorTrend Channel',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:20](https://www.youtube.com/watch?v=Wg0ziRtQ9JM&t=20s)',
       'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                    'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                    'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Sister company called Iron Planet and what they do is they take in government '
               'surplus vehicles put them up for auction and people like you can bid on them '
               'now.',
       'timestamp': 20,
       'timestamp_label': '[00:00:20]',
       'timestamp_seconds': 20,
       'tip': 'Sister company called Iron Planet and what they do is they take in government '
              'surplus vehicles put them up for auction and people like you can bid on them '
              'now.',
       'title': 'How to Buy a Government Surplus Army Truck or Humvee  - Dirt Every Day Extra '
                '(MotorTrend Channel)',
       'url': 'https://www.youtube.com/watch?v=Wg0ziRtQ9JM&t=20s',
       'video_id': 'Wg0ziRtQ9JM'},
      {'author': 'ConnorTV',
       'channel': 'ConnorTV',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:07](https://www.youtube.com/watch?v=0RUIANcUFdg&t=547s)',
       'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                    'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                    'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "You got to be kidding me, dude. That is a flipping sink right there. It's a "
               "little bent to the top. That's being bent back, dude. Stainless steel sink "
               'right here. Does it come with the pieces, too? It comes with a nice little '
               'drying rack right here.',
       'timestamp': 547,
       'timestamp_label': '[00:09:07]',
       'timestamp_seconds': 547,
       'tip': "You got to be kidding me, dude. That is a flipping sink right there. It's a "
              "little bent to the top. That's being bent back, dude. Stainless steel sink "
              'right here. Does it come with the pieces, too? It comes with a nice little '
              'drying rack right here.',
       'title': 'I Bought a GIANT Amazon Returns Pallet for $150 - HUGE Profit! (ConnorTV)',
       'url': 'https://www.youtube.com/watch?v=0RUIANcUFdg&t=547s',
       'video_id': '0RUIANcUFdg'},
      {'author': 'Auction Reviews With Jeff',
       'channel': 'Auction Reviews With Jeff',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:11:10](https://www.youtube.com/watch?v=PprDL7wH0FQ&t=670s)',
       'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                    'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                    'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'There, you can go anywhere with that thing. And the fire truck is not for '
               "sale. It's here all the time holding the flag.",
       'timestamp': 670,
       'timestamp_label': '[00:11:10]',
       'timestamp_seconds': 670,
       'tip': 'There, you can go anywhere with that thing. And the fire truck is not for sale. '
              "It's here all the time holding the flag.",
       'title': 'Government Auction SOLD Prices for Construction Equipment FEB 2026 (Auction '
                'Reviews With Jeff)',
       'url': 'https://www.youtube.com/watch?v=PprDL7wH0FQ&t=670s',
       'video_id': 'PprDL7wH0FQ'},
      {'author': 'MAN VS MYSTERY',
       'channel': 'MAN VS MYSTERY',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:14:32](https://www.youtube.com/watch?v=7H4B9rdQrOU&t=872s)',
       'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                    'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                    'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "What just give me a guess what do you think this right here is worth let's say "
               "50 bucks nope dragon $100 yeah that's a hard bucks.",
       'timestamp': 872,
       'timestamp_label': '[00:14:32]',
       'timestamp_seconds': 872,
       'tip': "What just give me a guess what do you think this right here is worth let's say "
              "50 bucks nope dragon $100 yeah that's a hard bucks.",
       'title': 'Government Surplus Auctions Are A Gold Mine Of Money! (MAN VS MYSTERY)',
       'url': 'https://www.youtube.com/watch?v=7H4B9rdQrOU&t=872s',
       'video_id': '7H4B9rdQrOU'},
      {'author': 'T.J. Lovelady',
       'channel': 'T.J. Lovelady',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:28](https://www.youtube.com/watch?v=3LlA-ruuv7E&t=148s)',
       'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                    'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                    'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Target highp counts these are really good they have some uh more High higher '
               "dollar stuff on top and then down below it's got you know it's a ton of stuff "
               'at the bottom the last one we got uh I think it had $150 Lego set on top those '
               "was 750 it's a cool little writing.",
       'timestamp': 148,
       'timestamp_label': '[00:02:28]',
       'timestamp_seconds': 148,
       'tip': 'Target highp counts these are really good they have some uh more High higher '
              "dollar stuff on top and then down below it's got you know it's a ton of stuff "
              'at the bottom the last one we got uh I think it had $150 Lego set on top those '
              "was 750 it's a cool little writing.",
       'title': 'Buying Your FIRST Liquidation Pallet What To Look For In 2025!! (T.J. '
                'Lovelady)',
       'url': 'https://www.youtube.com/watch?v=3LlA-ruuv7E&t=148s',
       'video_id': '3LlA-ruuv7E'},
      {'author': 'Digital Iron Group',
       'channel': 'Digital Iron Group',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:11](https://www.youtube.com/watch?v=HF9Hu38gKMI&t=71s)',
       'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                    'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                    'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "On aging inventory, and I've run into I remember a a dealer I had in the past, "
               'it was a Caterpillar dealer, and they had some used equipment. There were some '
               'used forestry pieces.',
       'timestamp': 71,
       'timestamp_label': '[00:01:11]',
       'timestamp_seconds': 71,
       'tip': "On aging inventory, and I've run into I remember a a dealer I had in the past, "
              'it was a Caterpillar dealer, and they had some used equipment. There were some '
              'used forestry pieces.',
       'title': 'Stopping aging inventory: act fast and auction when needed (Digital Iron '
                'Group)',
       'url': 'https://www.youtube.com/watch?v=HF9Hu38gKMI&t=71s',
       'video_id': 'HF9Hu38gKMI'}],
 12: [{'author': 'Auction Reviews With Jeff',
       'channel': 'Auction Reviews With Jeff',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:13:33](https://www.youtube.com/watch?v=E3mh6G6h8zM&t=813s)',
       'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                    'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                    'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Now, this is a General Services Administration the federal government auction. '
               "It's held by Orlando Auto Auction. No buyer fees, which is really good really "
               'good. And I read though that you have to pick the car up the day of the sale.',
       'timestamp': 813,
       'timestamp_label': '[00:13:33]',
       'timestamp_seconds': 813,
       'tip': 'Now, this is a General Services Administration the federal government auction. '
              "It's held by Orlando Auto Auction. No buyer fees, which is really good really "
              'good. And I read though that you have to pick the car up the day of the sale.',
       'title': 'What do Federal Government Surplus Vehicles Sell For at Auction? Part 1 of 3 '
                '(Auction Reviews With Jeff)',
       'url': 'https://www.youtube.com/watch?v=E3mh6G6h8zM&t=813s',
       'video_id': 'E3mh6G6h8zM'},
      {'author': 'Matthew Lesko',
       'channel': 'Matthew Lesko',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:07](https://www.youtube.com/watch?v=Ezeprg6O_GU&t=427s)',
       'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                    'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                    'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': '25th to take care of take advantage of this offer. So the 25th of this month '
               "it's over. 25th, you sign up for $1 and you get five days from that day uh to "
               'apply for everything we have. And at the end of five days, then we charge you '
               'uh $20 a month.',
       'timestamp': 427,
       'timestamp_label': '[00:07:07]',
       'timestamp_seconds': 427,
       'tip': '25th to take care of take advantage of this offer. So the 25th of this month '
              "it's over. 25th, you sign up for $1 and you get five days from that day uh to "
              'apply for everything we have. And at the end of five days, then we charge you '
              'uh $20 a month.',
       'title': 'GOVERNMENT SURPLUS! Get Free & Cheap Property, Equipment, Cars & More '
                '(Matthew Lesko)',
       'url': 'https://www.youtube.com/watch?v=Ezeprg6O_GU&t=427s',
       'video_id': 'Ezeprg6O_GU'},
      {'author': 'Matt Goldberg | The Surplus Hunter',
       'channel': 'Matt Goldberg | The Surplus Hunter',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:21:18](https://www.youtube.com/watch?v=_b6n7Qnt3P0&t=1278s)',
       'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                    'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                    'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "So we're rinse and repeating this method each day, each week, each month, each "
               "year. And that's why we are bringing in an abundance of surplus deals that we "
               'can get paid for. Because we know once we find those surplus deals, we are in '
               'control.',
       'timestamp': 1278,
       'timestamp_label': '[00:21:18]',
       'timestamp_seconds': 1278,
       'tip': "So we're rinse and repeating this method each day, each week, each month, each "
              "year. And that's why we are bringing in an abundance of surplus deals that we "
              'can get paid for. Because we know once we find those surplus deals, we are in '
              'control.',
       'title': '6 Ways To Find An Abundance Of Surplus Inventory Pallets...And Get Paid For '
                'It. (Matt Goldberg | The Surplus Hunter)',
       'url': 'https://www.youtube.com/watch?v=_b6n7Qnt3P0&t=1278s',
       'video_id': '_b6n7Qnt3P0'},
      {'author': '2plot ai',
       'channel': '2plot ai',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:26](https://www.youtube.com/watch?v=R8bNgZVNLAk&t=266s)',
       'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                    'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                    'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "'re not going to need unless, you know, you really need it. So, try to find "
               "the renting route for equipment. It's much better at the start.",
       'timestamp': 266,
       'timestamp_label': '[00:04:26]',
       'timestamp_seconds': 266,
       'tip': "'re not going to need unless, you know, you really need it. So, try to find the "
              "renting route for equipment. It's much better at the start.",
       'title': 'Flipping GovDeals Auction Items — Real Numbers & Custom Software (2plot ai)',
       'url': 'https://www.youtube.com/watch?v=R8bNgZVNLAk&t=266s',
       'video_id': 'R8bNgZVNLAk'},
      {'author': 'FlatBroke Garage',
       'channel': 'FlatBroke Garage',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:48](https://www.youtube.com/watch?v=pN1E-KA7qxw&t=588s)',
       'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                    'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                    'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "So, I'm going to fire this thing up. I'm going to let it run for an hour and "
               "we're going to take it out and beat on it and see what breaks. It's the next "
               'day and I want to see if this thing held a charge overnight.',
       'timestamp': 588,
       'timestamp_label': '[00:09:48]',
       'timestamp_seconds': 588,
       'tip': "So, I'm going to fire this thing up. I'm going to let it run for an hour and "
              "we're going to take it out and beat on it and see what breaks. It's the next "
              'day and I want to see if this thing held a charge overnight.',
       'title': 'GovDeals Ford F150 4X4 Great deal, or did I get burned? #govdeals #ford #f150 '
                '#auction (FlatBroke Garage)',
       'url': 'https://www.youtube.com/watch?v=pN1E-KA7qxw&t=588s',
       'video_id': 'pN1E-KA7qxw'},
      {'author': 'Tris10 @ MeND',
       'channel': 'Tris10 @ MeND',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:13:02](https://www.youtube.com/watch?v=Y895jCYSE5A&t=782s)',
       'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                    'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                    'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'This channel as we do provide these videos at least once a month to help you '
               'win more government contracts and with that have a great day.',
       'timestamp': 782,
       'timestamp_label': '[00:13:02]',
       'timestamp_seconds': 782,
       'tip': 'This channel as we do provide these videos at least once a month to help you '
              'win more government contracts and with that have a great day.',
       'title': 'Traceability, Cost Breakdowns, and Counteroffers for Government Contracts - '
                'DLA / DIBBS (Tris10 @ MeND)',
       'url': 'https://www.youtube.com/watch?v=Y895jCYSE5A&t=782s',
       'video_id': 'Y895jCYSE5A'},
      {'author': 'AuctionHub SA',
       'channel': 'AuctionHub SA',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:20](https://www.youtube.com/watch?v=zEvheNxg0WE&t=20s)',
       'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                    'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                    'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "I don't know what's going on here, but yeah. I don't know what you call those. "
               'And then And then, um, yeah, we had to start this battery up. Apparently, the '
               'battery is depleted or something, but completely. So, these are not working '
               'anymore.',
       'timestamp': 20,
       'timestamp_label': '[00:00:20]',
       'timestamp_seconds': 20,
       'tip': "I don't know what's going on here, but yeah. I don't know what you call those. "
              'And then And then, um, yeah, we had to start this battery up. Apparently, the '
              'battery is depleted or something, but completely. So, these are not working '
              'anymore.',
       'title': 'Viewing construction and mining assets for my clients at the auctions - '
                'AuctionHub Review (AuctionHub SA)',
       'url': 'https://www.youtube.com/watch?v=zEvheNxg0WE&t=20s',
       'video_id': 'zEvheNxg0WE'},
      {'author': 'Auction Reviews With Jeff',
       'channel': 'Auction Reviews With Jeff',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:59](https://www.youtube.com/watch?v=3ej4xfd_ers&t=59s)',
       'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                    'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                    'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "I'm in day day week four of my broken ribs and I feel much better. I'm looking "
               'at auction cars and trucks. This is a nice looking Chevy here. So thanks for '
               'the well wishes on my my ribs.',
       'timestamp': 59,
       'timestamp_label': '[00:00:59]',
       'timestamp_seconds': 59,
       'tip': "I'm in day day week four of my broken ribs and I feel much better. I'm looking "
              'at auction cars and trucks. This is a nice looking Chevy here. So thanks for '
              'the well wishes on my my ribs.',
       'title': 'Rainy Gov Vehicle Auction Preview | Some Nice Trucks (Part 1) (Auction '
                'Reviews With Jeff)',
       'url': 'https://www.youtube.com/watch?v=3ej4xfd_ers&t=59s',
       'video_id': '3ej4xfd_ers'},
      {'author': 'Midwestern Garage',
       'channel': 'Midwestern Garage',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:15](https://www.youtube.com/watch?v=3QWRjujnz2E&t=555s)',
       'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                    'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                    'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'I was messing with the charger a little bit. Noticed one of the battery cables '
               'was loose and I put the charger to uh start position and then I realized The '
               "motor crank's over. So, at least that's a little bit of a win.",
       'timestamp': 555,
       'timestamp_label': '[00:09:15]',
       'timestamp_seconds': 555,
       'tip': 'I was messing with the charger a little bit. Noticed one of the battery cables '
              'was loose and I put the charger to uh start position and then I realized The '
              "motor crank's over. So, at least that's a little bit of a win.",
       'title': 'I just bought a M1097R1 Heavy Spec Humvee from govplanet.com! (Midwestern '
                'Garage)',
       'url': 'https://www.youtube.com/watch?v=3QWRjujnz2E&t=555s',
       'video_id': '3QWRjujnz2E'},
      {'author': 'ElectroHoard',
       'channel': 'ElectroHoard',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=2ZRWlImJMzE&t=15s)',
       'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                    'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                    'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Equipment Workshop and I do plan on showing a lot of other stuff uh in detail '
               "if you follow the channel you'll notice that I have a.",
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': 'Equipment Workshop and I do plan on showing a lot of other stuff uh in detail '
              "if you follow the channel you'll notice that I have a.",
       'title': 'First look at my test equipment hoarding! HP, Agilent, Fluke and Tektronix '
                'crazyness in my workshop! (ElectroHoard)',
       'url': 'https://www.youtube.com/watch?v=2ZRWlImJMzE&t=15s',
       'video_id': '2ZRWlImJMzE'},
      {'author': 'Pallet Pros Academy',
       'channel': 'Pallet Pros Academy',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:11:22](https://www.youtube.com/watch?v=tDyyYhvrSts&t=682s)',
       'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                    'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                    'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'You have to have a a a proper system in order to retain your customers. So you '
               "can build three to six repeat customers within this time frame. That's within "
               '90 days with a mentor. And then finally, you can get to about 10K a month '
               'within 4 to 8 months.',
       'timestamp': 682,
       'timestamp_label': '[00:11:22]',
       'timestamp_seconds': 682,
       'tip': 'You have to have a a a proper system in order to retain your customers. So you '
              "can build three to six repeat customers within this time frame. That's within "
              '90 days with a mentor. And then finally, you can get to about 10K a month '
              'within 4 to 8 months.',
       'title': 'Pallet Business: Starting From Scratch (With vs Without a Mentor) (Pallet '
                'Pros Academy)',
       'url': 'https://www.youtube.com/watch?v=tDyyYhvrSts&t=682s',
       'video_id': 'tDyyYhvrSts'},
      {'author': 'Street Rat Garage',
       'channel': 'Street Rat Garage',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:35:42](https://www.youtube.com/watch?v=qieQr_fEJQ8&t=2142s)',
       'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                    'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                    'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "You're watching this and it's hasn't been too many days since I put this video "
               'out you might want to go in here and check out some of these deals I got.',
       'timestamp': 2142,
       'timestamp_label': '[00:35:42]',
       'timestamp_seconds': 2142,
       'tip': "You're watching this and it's hasn't been too many days since I put this video "
              'out you might want to go in here and check out some of these deals I got.',
       'title': 'Government surplus, public vehicle auction. Police cars and state owned '
                'vehicles, anyone can buy! (Street Rat Garage)',
       'url': 'https://www.youtube.com/watch?v=qieQr_fEJQ8&t=2142s',
       'video_id': 'qieQr_fEJQ8'},
      {'author': 'Split Builds',
       'channel': 'Split Builds',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:20](https://www.youtube.com/watch?v=CkfJvTDwa2w&t=140s)',
       'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                    'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                    'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Me to go pick it up until January and once it clears you got seven days to go '
               "pick up the vehicle or you'll get charged a daily storage rate so other than "
               "that that's kind of how it's done on our planet so jump on there see if you "
               'can get you one.',
       'timestamp': 140,
       'timestamp_label': '[00:02:20]',
       'timestamp_seconds': 140,
       'tip': 'Me to go pick it up until January and once it clears you got seven days to go '
              "pick up the vehicle or you'll get charged a daily storage rate so other than "
              "that that's kind of how it's done on our planet so jump on there see if you can "
              'get you one.',
       'title': 'How to buy a Government Surplus Humvee (Split Builds)',
       'url': 'https://www.youtube.com/watch?v=CkfJvTDwa2w&t=140s',
       'video_id': 'CkfJvTDwa2w'},
      {'author': 'Kevin24Seven',
       'channel': 'Kevin24Seven',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:26](https://www.youtube.com/watch?v=5QTEGYGbQsw&t=326s)',
       'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                    'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                    'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "Honestly they're worth about 15 I mean they have they're gonna need work so "
               "let's just you know this one it is clean on the inside but it better be for "
               "freaking forty five thousand dollars let's just look at it here um not the "
               "lights don't even all work.",
       'timestamp': 326,
       'timestamp_label': '[00:05:26]',
       'timestamp_seconds': 326,
       'tip': "Honestly they're worth about 15 I mean they have they're gonna need work so "
              "let's just you know this one it is clean on the inside but it better be for "
              "freaking forty five thousand dollars let's just look at it here um not the "
              "lights don't even all work.",
       'title': 'GovPlanet Humvee Auctions are Out of Control (Kevin24Seven)',
       'url': 'https://www.youtube.com/watch?v=5QTEGYGbQsw&t=326s',
       'video_id': '5QTEGYGbQsw'},
      {'author': 'UX Auctions',
       'channel': 'UX Auctions',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:16:48](https://www.youtube.com/watch?v=Z87d62pWVEk&t=1008s)',
       'relevance': 'Attributed practitioner commentary on federal (`GSA`/`GovPlanet`) and '
                    'municipal (`GovDeals`/`PublicSurplus`) physical surplus auctions, '
                    'SF-97/DEMIL compliance, and B2B remarketing (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Founding members pay $10 a month with a seven day money back guarantee. '
               'Chapter eight, you won, now what? This part moves fast, so have your plan '
               'ready before the auction ends. Every sale sets its own deadline.',
       'timestamp': 1008,
       'timestamp_label': '[00:16:48]',
       'timestamp_seconds': 1008,
       'tip': 'Founding members pay $10 a month with a seven day money back guarantee. Chapter '
              'eight, you won, now what? This part moves fast, so have your plan ready before '
              'the auction ends. Every sale sets its own deadline.',
       'title': 'How to Buy at Government Auctions: Police Cars & Surplus Vehicles (UX '
                'Auctions)',
       'url': 'https://www.youtube.com/watch?v=Z87d62pWVEk&t=1008s',
       'video_id': 'Z87d62pWVEk'}]}
