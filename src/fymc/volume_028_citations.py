"""Curated 180-citation Commercial Cleaning Contracts baseline (15 per chapter across Q1-Q12) mined strictly from verified Commercial Cleaning Contracts YouTube transcripts."""
from __future__ import annotations

CHAPTER_KEYWORDS: dict[int, set[str]] = {1: {'1099',
     'account',
     'add',
     'app',
     'area',
     'arr',
     'avoiding',
     'b2b',
     'bank',
     'bid',
     'bidding',
     'bids',
     'bloodborne',
     'bond',
     'business',
     'calculator',
     'calling',
     'campion',
     'carpet',
     'checklist',
     'church',
     'clean',
     'cleaning',
     'client',
     'clients',
     'cold',
     'commercial',
     'comp',
     'company',
     'construction',
     'consumables',
     'contract',
     'firm',
     'margin',
     'market',
     'model',
     'niche',
     'operator',
     'revenue',
     'service',
     'value'},
 2: {'1099',
     'account',
     'add',
     'app',
     'area',
     'arr',
     'avoiding',
     'b2b',
     'bank',
     'bid',
     'bidding',
     'bids',
     'bloodborne',
     'bond',
     'budget',
     'business',
     'buyer',
     'calculator',
     'calling',
     'campion',
     'carpet',
     'checklist',
     'church',
     'clean',
     'cleaning',
     'cold',
     'commercial',
     'comp',
     'company',
     'construction',
     'consumables',
     'contract',
     'customer',
     'decision',
     'escrow',
     'fee',
     'fees',
     'invoice',
     'pay',
     'payment',
     'pays',
     'retainer'},
 3: {'1099',
     'account',
     'add',
     'app',
     'area',
     'arr',
     'avoiding',
     'b2b',
     'bank',
     'bid',
     'bidding',
     'bids',
     'bloodborne',
     'bond',
     'business',
     'calculator',
     'calling',
     'campion',
     'carpet',
     'cash',
     'cashflow',
     'checklist',
     'church',
     'clean',
     'cleaning',
     'cold',
     'commercial',
     'commission',
     'comp',
     'company',
     'construction',
     'consumables',
     'contract',
     'cost',
     'costs',
     'economics',
     'margin',
     'margins',
     'price',
     'pricing',
     'profit',
     'roi',
     'unit'},
 4: {'1099',
     'account',
     'add',
     'app',
     'area',
     'arr',
     'avoiding',
     'b2b',
     'bank',
     'bid',
     'bidding',
     'bids',
     'bloodborne',
     'bond',
     'budget',
     'business',
     'calculator',
     'calling',
     'campion',
     'capital',
     'carpet',
     'checklist',
     'church',
     'clean',
     'cleaning',
     'cold',
     'commercial',
     'comp',
     'company',
     'construction',
     'consumables',
     'contract',
     'entity',
     'insurance',
     'lean',
     'license',
     'llc',
     'setup',
     'software',
     'stack',
     'startup',
     'tools'},
 5: {'1099',
     'account',
     'add',
     'app',
     'area',
     'arr',
     'audit',
     'avoid',
     'avoiding',
     'b2b',
     'bank',
     'bid',
     'bidding',
     'bids',
     'bloodborne',
     'bond',
     'business',
     'calculator',
     'calling',
     'campion',
     'carpet',
     'checklist',
     'church',
     'clawback',
     'clean',
     'cleaning',
     'cold',
     'commercial',
     'comp',
     'company',
     'construction',
     'consumables',
     'contract',
     'dispute',
     'edge',
     'fail',
     'mistake',
     'mistakes',
     'problem',
     'risk',
     'risks',
     'trap',
     'traps'},
 6: {'1099',
     'account',
     'add',
     'app',
     'area',
     'arr',
     'avoiding',
     'b2b',
     'bank',
     'bid',
     'bidding',
     'bids',
     'bloodborne',
     'bond',
     'business',
     'calculator',
     'calling',
     'campion',
     'carpet',
     'checklist',
     'church',
     'clean',
     'cleaning',
     'client',
     'cold',
     'commercial',
     'comp',
     'company',
     'construction',
     'consumables',
     'contract',
     'data',
     'deal',
     'find',
     'first',
     'lead',
     'leads',
     'list',
     'outbound',
     'prospect',
     'qualify',
     'search',
     'sourcing'},
 7: {'1099',
     'account',
     'add',
     'app',
     'area',
     'arr',
     'avoiding',
     'b2b',
     'bank',
     'bid',
     'bidding',
     'bids',
     'bloodborne',
     'bond',
     'business',
     'calculator',
     'calling',
     'campion',
     'carpet',
     'checklist',
     'church',
     'clean',
     'cleaning',
     'cold',
     'commercial',
     'comp',
     'company',
     'construction',
     'consumables',
     'contract',
     'delivery',
     'execution',
     'process',
     'quality',
     'sop',
     'step',
     'steps',
     'system',
     'underwriting',
     'verify',
     'workflow'},
 8: {'1099',
     'account',
     'add',
     'api',
     'app',
     'area',
     'arr',
     'avoiding',
     'b2b',
     'bank',
     'bid',
     'bidding',
     'bids',
     'bloodborne',
     'bond',
     'business',
     'calculator',
     'calling',
     'campion',
     'carpet',
     'checklist',
     'church',
     'clean',
     'cleaning',
     'cold',
     'commercial',
     'comp',
     'company',
     'construction',
     'consumables',
     'contract',
     'crm',
     'data',
     'database',
     'platform',
     'portal',
     'scraper',
     'search',
     'software',
     'tool',
     'tools',
     'tracking'},
 9: {'1099',
     'account',
     'add',
     'agreement',
     'app',
     'area',
     'arr',
     'avoiding',
     'b2b',
     'bank',
     'bid',
     'bidding',
     'bids',
     'bloodborne',
     'bond',
     'business',
     'calculator',
     'calling',
     'campion',
     'carpet',
     'checklist',
     'church',
     'clean',
     'cleaning',
     'cold',
     'commercial',
     'comp',
     'company',
     'compliance',
     'construction',
     'consumables',
     'contract',
     'disclosure',
     'law',
     'legal',
     'license',
     'outreach',
     'rules',
     'script',
     'state',
     'terms'},
 10: {'1099',
      'account',
      'add',
      'agent',
      'ai',
      'app',
      'area',
      'arr',
      'automate',
      'automation',
      'avoiding',
      'b2b',
      'bank',
      'bid',
      'bidding',
      'bids',
      'bloodborne',
      'bond',
      'business',
      'calculator',
      'calling',
      'campion',
      'carpet',
      'checklist',
      'church',
      'clean',
      'cleaning',
      'cold',
      'commercial',
      'comp',
      'company',
      'construction',
      'consumables',
      'contract',
      'dashboard',
      'leverage',
      'pipeline',
      'scale',
      'script',
      'speed',
      'template',
      'workflow'},
 11: {'1099',
      'account',
      'add',
      'app',
      'area',
      'arr',
      'avoiding',
      'b2b',
      'bank',
      'bid',
      'bidding',
      'bids',
      'bloodborne',
      'bond',
      'business',
      'calculator',
      'calling',
      'campion',
      'carpet',
      'checklist',
      'church',
      'clean',
      'cleaning',
      'cold',
      'commercial',
      'comp',
      'company',
      'construction',
      'consumables',
      'contract',
      'contractor',
      'exit',
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
 12: {'1099',
      'account',
      'action',
      'add',
      'app',
      'area',
      'arr',
      'avoiding',
      'b2b',
      'bank',
      'bid',
      'bidding',
      'bids',
      'bloodborne',
      'bond',
      'business',
      'calculator',
      'calling',
      'campion',
      'carpet',
      'checklist',
      'church',
      'clean',
      'cleaning',
      'cold',
      'commercial',
      'comp',
      'company',
      'construction',
      'consumables',
      'contract',
      'day',
      'days',
      'launch',
      'milestone',
      'month',
      'plan',
      'roadmap',
      'sprint',
      'start',
      'thirty',
      'week'}}

BASELINE_EXPERT_CITATIONS_BY_CHAPTER: dict[int, list[dict]] = {1: [{'author': 'Bid & Profit Lab',
      'channel': 'Bid & Profit Lab',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:33](https://www.youtube.com/watch?v=T-l3Df3Iino&t=273s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'If you prefer a ready made spreadsheet for your bidding calculations, our '
              'Commercial Cleaning Bid and Margin System is linked in the description. Use '
              'your own job assumptions, review the result and check that every promised '
              'service is covered before you submit a bid.',
      'timestamp': 273,
      'timestamp_label': '[00:04:33]',
      'timestamp_seconds': 273,
      'tip': 'If you prefer a ready made spreadsheet for your bidding calculations, our '
             'Commercial Cleaning Bid and Margin System is linked in the description. Use your '
             'own job assumptions, review the result and check that every promised service is '
             'covered before you submit a bid.',
      'title': 'How to Bid a Commercial Cleaning Contract: 20,000 Sq Ft Example. (Bid & Profit '
               'Lab)',
      'url': 'https://www.youtube.com/watch?v=T-l3Df3Iino&t=273s',
      'video_id': 'T-l3Df3Iino'},
     {'author': 'Commercial Cleaning CEO',
      'channel': 'Commercial Cleaning CEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=HahI_OcnGVA&t=21s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So stay tuned to the end so that you know how to apply these services to your '
              'commercial cleaning company and your clients so that you can continue to add '
              "more and more revenue. And if you don't know who I am, my name is Matt.",
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': 'So stay tuned to the end so that you know how to apply these services to your '
             'commercial cleaning company and your clients so that you can continue to add '
             "more and more revenue. And if you don't know who I am, my name is Matt.",
      'title': 'How To Use Day Porter Services To Grow Your Cleaning Business (Commercial '
               'Cleaning CEO)',
      'url': 'https://www.youtube.com/watch?v=HahI_OcnGVA&t=21s',
      'video_id': 'HahI_OcnGVA'},
     {'author': 'Janitorial Manager',
      'channel': 'Janitorial Manager',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:11](https://www.youtube.com/watch?v=NDvJAHP1GQo&t=131s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Simply add your business logo onto each QR code and place them throughout the '
              'facilities you service, customers and the public can then scan your code to see '
              "if an area is clean and rate the level of cleanliness they've observed.",
      'timestamp': 131,
      'timestamp_label': '[00:02:11]',
      'timestamp_seconds': 131,
      'tip': 'Simply add your business logo onto each QR code and place them throughout the '
             'facilities you service, customers and the public can then scan your code to see '
             "if an area is clean and rate the level of cleanliness they've observed.",
      'title': 'Janitorial Manager QR Code Features and Benefits (Janitorial Manager)',
      'url': 'https://www.youtube.com/watch?v=NDvJAHP1GQo&t=131s',
      'video_id': 'NDvJAHP1GQo'},
     {'author': 'Commercial Cleaning CEO',
      'channel': 'Commercial Cleaning CEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:10](https://www.youtube.com/watch?v=-DEX3b-m000&t=130s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'It was not able to be hands-off for the client. The cleaning company that was '
              "fulfilling the contract was essentially just a staffing service. They weren't "
              'able to do much of the management. But, the thing is with that, how can you '
              'know when those problems are happening?',
      'timestamp': 130,
      'timestamp_label': '[00:02:10]',
      'timestamp_seconds': 130,
      'tip': 'It was not able to be hands-off for the client. The cleaning company that was '
             "fulfilling the contract was essentially just a staffing service. They weren't "
             'able to do much of the management. But, the thing is with that, how can you know '
             'when those problems are happening?',
      'title': 'Win $200K Commercial Cleaning Contracts With This Janitorial Software '
               '(Commercial Cleaning CEO)',
      'url': 'https://www.youtube.com/watch?v=-DEX3b-m000&t=130s',
      'video_id': '-DEX3b-m000'},
     {'author': 'Franchise Wizards',
      'channel': 'Franchise Wizards',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=eJ5s6HRr1HE&t=21s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'t think about when considering business ownership, commercial cleaning. And "
              "we're also exploring a very unique business model in the franchise industry, "
              "the master franchise model. Here's what makes this conversation interesting.",
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': "'t think about when considering business ownership, commercial cleaning. And "
             "we're also exploring a very unique business model in the franchise industry, the "
             "master franchise model. Here's what makes this conversation interesting.",
      'title': 'Own a Cleaning Franchise Without Cleaning? Stratus Clean Master Franchise '
               'Explained (Franchise Wizards)',
      'url': 'https://www.youtube.com/watch?v=eJ5s6HRr1HE&t=21s',
      'video_id': 'eJ5s6HRr1HE'},
     {'author': 'OctoClean Media',
      'channel': 'OctoClean Media',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:26](https://www.youtube.com/watch?v=OzSRs5osKKI&t=326s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Lowballing may help you secure a job initially, but it often creates long-term '
              'problems through poor margins, staffing issues, inconsistent service, and '
              'strained client relationships. A sustainable cleaning company cannot be built '
              'on desperation pricing.',
      'timestamp': 326,
      'timestamp_label': '[00:05:26]',
      'timestamp_seconds': 326,
      'tip': 'Lowballing may help you secure a job initially, but it often creates long-term '
             'problems through poor margins, staffing issues, inconsistent service, and '
             'strained client relationships. A sustainable cleaning company cannot be built on '
             'desperation pricing.',
      'title': 'How To Win Commercial Cleaning Contracts With Great Proposals! (Janitorial) '
               '(OctoClean Media)',
      'url': 'https://www.youtube.com/watch?v=OzSRs5osKKI&t=326s',
      'video_id': 'OzSRs5osKKI'},
     {'author': 'Cleaning Launch',
      'channel': 'Cleaning Launch',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=V84a_KWRYU4&t=15s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Belief of thinking that they have to be the cheapest in order to win a '
              "commercial cleaning contract and I'm here to tell you that clients are not.",
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Belief of thinking that they have to be the cheapest in order to win a '
             "commercial cleaning contract and I'm here to tell you that clients are not.",
      'title': 'Never Get Lowballed Commercial Cleaning Contracts Again With This Method '
               '(Cleaning Launch)',
      'url': 'https://www.youtube.com/watch?v=V84a_KWRYU4&t=15s',
      'video_id': 'V84a_KWRYU4'},
     {'author': 'Swept',
      'channel': 'Swept',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:07](https://www.youtube.com/watch?v=Tub9xxD1-7o&t=367s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And you know that may seem kind of counter-intuitive like well i'm i own a "
              "cleaning company i'm here to provide a cleaning service.",
      'timestamp': 367,
      'timestamp_label': '[00:06:07]',
      'timestamp_seconds': 367,
      'tip': "And you know that may seem kind of counter-intuitive like well i'm i own a "
             "cleaning company i'm here to provide a cleaning service.",
      'title': 'Selling with Swept: How to Win 80% of Your Commercial Cleaning Contracts '
               '(Swept)',
      'url': 'https://www.youtube.com/watch?v=Tub9xxD1-7o&t=367s',
      'video_id': 'Tub9xxD1-7o'},
     {'author': 'CleanTender',
      'channel': 'CleanTender',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:54](https://www.youtube.com/watch?v=M3p8970sZyg&t=54s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "For the devolved nations, you don't need to hunt down individual council sites. "
              'Just use Public Contracts Scotland, Sell 2 Wales, eSourcing NI. For the '
              'high-value cleaning contracts, everything must legally be posted on the Find a '
              'Tender service.',
      'timestamp': 54,
      'timestamp_label': '[00:00:54]',
      'timestamp_seconds': 54,
      'tip': "For the devolved nations, you don't need to hunt down individual council sites. "
             'Just use Public Contracts Scotland, Sell 2 Wales, eSourcing NI. For the '
             'high-value cleaning contracts, everything must legally be posted on the Find a '
             'Tender service.',
      'title': 'How to Find, Bid and Win UK Cleaning Contracts (2026 Walkthrough) '
               '(CleanTender)',
      'url': 'https://www.youtube.com/watch?v=M3p8970sZyg&t=54s',
      'video_id': 'M3p8970sZyg'},
     {'author': 'Clean Ops Guide',
      'channel': 'Clean Ops Guide',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:13](https://www.youtube.com/watch?v=XySWgKh0nEY&t=73s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Now, all three companies may know how to clean, but which one would you feel '
              'more comfortable giving access to your property? Clients are only evaluating '
              'your cleaning ability.',
      'timestamp': 73,
      'timestamp_label': '[00:01:13]',
      'timestamp_seconds': 73,
      'tip': 'Now, all three companies may know how to clean, but which one would you feel '
             'more comfortable giving access to your property? Clients are only evaluating '
             'your cleaning ability.',
      'title': 'How to Win Commercial Cleaning Contracts | Step-by-Step Guide (Clean Ops '
               'Guide)',
      'url': 'https://www.youtube.com/watch?v=XySWgKh0nEY&t=73s',
      'video_id': 'XySWgKh0nEY'},
     {'author': 'GovKidMethod',
      'channel': 'GovKidMethod',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:22:04](https://www.youtube.com/watch?v=ua_m84N0cwA&t=1324s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I mean, it could be under any services, but as long as it's a multiple option "
              "year contract. And for this, we're assuming it's a base plus one, two, three, "
              "four. So, it's a five-year contract. So, recurring service model base plus four "
              'option years, fiveyear contract.',
      'timestamp': 1324,
      'timestamp_label': '[00:22:04]',
      'timestamp_seconds': 1324,
      'tip': "I mean, it could be under any services, but as long as it's a multiple option "
             "year contract. And for this, we're assuming it's a base plus one, two, three, "
             "four. So, it's a five-year contract. So, recurring service model base plus four "
             'option years, fiveyear contract.',
      'title': 'The Lucrative Janitorial Services Government Contracts Industry! '
               '(GovKidMethod)',
      'url': 'https://www.youtube.com/watch?v=ua_m84N0cwA&t=1324s',
      'video_id': 'ua_m84N0cwA'},
     {'author': 'Commercial Cleaning CEO',
      'channel': 'Commercial Cleaning CEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:18:52](https://www.youtube.com/watch?v=yfZUE5PZgvk&t=1132s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Look, being small is not the problem. It's looking risky that's the problem. "
              'And when you do these 10 things inside of your commercial cleaning service, no '
              "matter what size you are at, you're going to look far less risky to large "
              'clients.',
      'timestamp': 1132,
      'timestamp_label': '[00:18:52]',
      'timestamp_seconds': 1132,
      'tip': "Look, being small is not the problem. It's looking risky that's the problem. And "
             'when you do these 10 things inside of your commercial cleaning service, no '
             "matter what size you are at, you're going to look far less risky to large "
             'clients.',
      'title': 'How Small Cleaning Companies Win BIG Contracts (Commercial Cleaning CEO)',
      'url': 'https://www.youtube.com/watch?v=yfZUE5PZgvk&t=1132s',
      'video_id': 'yfZUE5PZgvk'},
     {'author': 'Darian Jarrett',
      'channel': 'Darian Jarrett',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:50](https://www.youtube.com/watch?v=QlIScHN-MPE&t=410s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Really do this stuff email me at Daran Jared 9@gmail.com I'll be glad to get "
              'with you and help you out with that by the way if you got any value out of this '
              "video make sure you give me a like on this one I'll see you on the next video "
              'peace.',
      'timestamp': 410,
      'timestamp_label': '[00:06:50]',
      'timestamp_seconds': 410,
      'tip': "Really do this stuff email me at Daran Jared 9@gmail.com I'll be glad to get "
             'with you and help you out with that by the way if you got any value out of this '
             "video make sure you give me a like on this one I'll see you on the next video "
             'peace.',
      'title': 'Are You Bidding Right? Here’s How to Price Commercial Cleaning Jobs Like The '
               'Pros! (Darian Jarrett)',
      'url': 'https://www.youtube.com/watch?v=QlIScHN-MPE&t=410s',
      'video_id': 'QlIScHN-MPE'},
     {'author': 'AJ SIMMONS',
      'channel': 'AJ SIMMONS',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:30](https://www.youtube.com/watch?v=cWVLz5abUAg&t=510s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Service is all everything matches what you want your terms of services say also '
              'make sure that wherever it says your company name you that you delete these '
              'brackets and the words and actually put the name of your actual company okay so '
              'test company.',
      'timestamp': 510,
      'timestamp_label': '[00:08:30]',
      'timestamp_seconds': 510,
      'tip': 'Service is all everything matches what you want your terms of services say also '
             'make sure that wherever it says your company name you that you delete these '
             'brackets and the words and actually put the name of your actual company okay so '
             'test company.',
      'title': 'How to bid on 30,000 square foot office building for cleaning | Calculated '
               'Cleaning | Cleaning Cost (AJ SIMMONS)',
      'url': 'https://www.youtube.com/watch?v=cWVLz5abUAg&t=510s',
      'video_id': 'cWVLz5abUAg'},
     {'author': 'The Janitorial Store',
      'channel': 'The Janitorial Store',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:59](https://www.youtube.com/watch?v=U5pnasmmPuY&t=299s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Such tests may have to be done at intervals over a period of several months to '
              'make sure that your needle stick injury does not lead to HIV hepatitis B HB v '
              'hepatitis C HCV or any of approximately 20 other blood-borne diseases.',
      'timestamp': 299,
      'timestamp_label': '[00:04:59]',
      'timestamp_seconds': 299,
      'tip': 'Such tests may have to be done at intervals over a period of several months to '
             'make sure that your needle stick injury does not lead to HIV hepatitis B HB v '
             'hepatitis C HCV or any of approximately 20 other blood-borne diseases.',
      'title': 'Bloodborne Pathogens Training for Janitorial Employees (The Janitorial Store)',
      'url': 'https://www.youtube.com/watch?v=U5pnasmmPuY&t=299s',
      'video_id': 'U5pnasmmPuY'}],
 2: [{'author': 'Karen Denton KSC',
      'channel': 'Karen Denton KSC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:44](https://www.youtube.com/watch?v=xeZ8_Jlv0AI&t=104s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Because here's something I want you to understand. You might have to pay your "
              'employees before your customer even pays you. Now, imagine winning a large '
              'contract that requires 10 employees. Can your company afford that payroll while '
              "you're waiting for your first payment?",
      'timestamp': 104,
      'timestamp_label': '[00:01:44]',
      'timestamp_seconds': 104,
      'tip': "Because here's something I want you to understand. You might have to pay your "
             'employees before your customer even pays you. Now, imagine winning a large '
             'contract that requires 10 employees. Can your company afford that payroll while '
             "you're waiting for your first payment?",
      'title': 'Ready to Win Big Cleaning Contracts  Here’s What You Must Know First! (Karen '
               'Denton KSC)',
      'url': 'https://www.youtube.com/watch?v=xeZ8_Jlv0AI&t=104s',
      'video_id': 'xeZ8_Jlv0AI'},
     {'author': 'Clean Ops Guide',
      'channel': 'Clean Ops Guide',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:34](https://www.youtube.com/watch?v=IgZO8_dFaeU&t=214s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You may need multiple employees, more equipment, additional supervision, and '
              'enough money to cover payroll before the customer pays the invoice. If you '
              "haven't developed your pricing and operational systems, a larger contract may "
              'become overwhelming.',
      'timestamp': 214,
      'timestamp_label': '[00:03:34]',
      'timestamp_seconds': 214,
      'tip': 'You may need multiple employees, more equipment, additional supervision, and '
             'enough money to cover payroll before the customer pays the invoice. If you '
             "haven't developed your pricing and operational systems, a larger contract may "
             'become overwhelming.',
      'title': 'Starting a Commercial Cleaning Business? Understand This First (Clean Ops '
               'Guide)',
      'url': 'https://www.youtube.com/watch?v=IgZO8_dFaeU&t=214s',
      'video_id': 'IgZO8_dFaeU'},
     {'author': 'Logan Robison',
      'channel': 'Logan Robison',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:31:08](https://www.youtube.com/watch?v=mrd8LK8fcFM&t=1868s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'t care what you charge your guests to pay for this clean. If you want my "
              "company to clean this property, this is how much it's going to cost. Like, I "
              "don't care what the guest pays. You can charge the guest $0. You can charge the "
              'guest $500.',
      'timestamp': 1868,
      'timestamp_label': '[00:31:08]',
      'timestamp_seconds': 1868,
      'tip': "'t care what you charge your guests to pay for this clean. If you want my "
             "company to clean this property, this is how much it's going to cost. Like, I "
             "don't care what the guest pays. You can charge the guest $0. You can charge the "
             'guest $500.',
      'title': 'How I Built a $1M Airbnb Cleaning Business — Without Cleaning a Single Unit '
               '(Logan Robison)',
      'url': 'https://www.youtube.com/watch?v=mrd8LK8fcFM&t=1868s',
      'video_id': 'mrd8LK8fcFM'},
     {'author': 'Little Wonders',
      'channel': 'Little Wonders',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:36](https://www.youtube.com/watch?v=AdyzLEzXsAQ&t=96s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'In this example, the calculator includes labor, cleaning supplies, travel, and '
              "an allowance for overhead. Let's raise the supplies budget from 18 to quote "
              "increases from 180 to $195. That's why it's important to enter realistic costs "
              'before quoting a customer.',
      'timestamp': 96,
      'timestamp_label': '[00:01:36]',
      'timestamp_seconds': 96,
      'tip': 'In this example, the calculator includes labor, cleaning supplies, travel, and '
             "an allowance for overhead. Let's raise the supplies budget from 18 to quote "
             "increases from 180 to $195. That's why it's important to enter realistic costs "
             'before quoting a customer.',
      'title': 'Cleaning Business Quote Calculator in Google Sheets (Easy Tutorial) (Little '
               'Wonders)',
      'url': 'https://www.youtube.com/watch?v=AdyzLEzXsAQ&t=96s',
      'video_id': 'AdyzLEzXsAQ'},
     {'author': 'Daniel Linton',
      'channel': 'Daniel Linton',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:06](https://www.youtube.com/watch?v=B415KkGunUw&t=186s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Basically, the porter is on the cleaning company's insurance, cleaning "
              "company's benefits, the cleaning company's payroll, the cleaning company just "
              'charges the end customer a markup on their hourly rate.',
      'timestamp': 186,
      'timestamp_label': '[00:03:06]',
      'timestamp_seconds': 186,
      'tip': "Basically, the porter is on the cleaning company's insurance, cleaning company's "
             "benefits, the cleaning company's payroll, the cleaning company just charges the "
             'end customer a markup on their hourly rate.',
      'title': 'Cold Calling Guide for Janitorial Companies | Appointment Setting Training '
               '(Daniel Linton)',
      'url': 'https://www.youtube.com/watch?v=B415KkGunUw&t=186s',
      'video_id': 'B415KkGunUw'},
     {'author': 'Mike Mak',
      'channel': 'Mike Mak',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:56](https://www.youtube.com/watch?v=6MDrTK46_8g&t=356s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Perform a carpet job which typically did pay really well the only problem that '
              'those those fees existed even on those.',
      'timestamp': 356,
      'timestamp_label': '[00:05:56]',
      'timestamp_seconds': 356,
      'tip': 'Perform a carpet job which typically did pay really well the only problem that '
             'those those fees existed even on those.',
      'title': "The Dark Side of Buying a Cleaning Franchise - What They Don't Tell You (Mike "
               'Mak)',
      'url': 'https://www.youtube.com/watch?v=6MDrTK46_8g&t=356s',
      'video_id': '6MDrTK46_8g'},
     {'author': 'Commercial Cleaning CEO',
      'channel': 'Commercial Cleaning CEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:55](https://www.youtube.com/watch?v=f9f6YA_kX78&t=295s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'To increase profitability through something that I like to call Value training '
              'you see the Temptation that commercial cleaning business owners face.',
      'timestamp': 295,
      'timestamp_label': '[00:04:55]',
      'timestamp_seconds': 295,
      'tip': 'To increase profitability through something that I like to call Value training '
             'you see the Temptation that commercial cleaning business owners face.',
      'title': '3 PROVEN Cold Calling Tips That Get More Commercial Cleaning Contracts '
               '(Commercial Cleaning CEO)',
      'url': 'https://www.youtube.com/watch?v=f9f6YA_kX78&t=295s',
      'video_id': 'f9f6YA_kX78'},
     {'author': 'Janitorial Coaching Hub',
      'channel': 'Janitorial Coaching Hub',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:22](https://www.youtube.com/watch?v=GlA-D_TIYLg&t=22s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You're starting out cash flow sometimes is very difficult you don't have enough "
              'money to pay your staff every two weeks so um some contract some clients may.',
      'timestamp': 22,
      'timestamp_label': '[00:00:22]',
      'timestamp_seconds': 22,
      'tip': "You're starting out cash flow sometimes is very difficult you don't have enough "
             'money to pay your staff every two weeks so um some contract some clients may.',
      'title': 'Should You use W-2 or 1099 (Subcontracting) Model For Your Cleaning Team '
               '(Janitorial Coaching Hub)',
      'url': 'https://www.youtube.com/watch?v=GlA-D_TIYLg&t=22s',
      'video_id': 'GlA-D_TIYLg'},
     {'author': 'GovKidMethod',
      'channel': 'GovKidMethod',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:44:40](https://www.youtube.com/watch?v=dr59GJ2T5v4&t=2680s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "It's really good way to to put your yourself out of business if you don't pay "
              "this and you get caught. So, it's this number plus the 454 plus plus vacation "
              'and holidays.',
      'timestamp': 2680,
      'timestamp_label': '[00:44:40]',
      'timestamp_seconds': 2680,
      'tip': "It's really good way to to put your yourself out of business if you don't pay "
             "this and you get caught. So, it's this number plus the 454 plus plus vacation "
             'and holidays.',
      'title': 'Janitorial GovCon Bids (beta.sam.gov) | LIVE with GovKidMethod (GovKidMethod)',
      'url': 'https://www.youtube.com/watch?v=dr59GJ2T5v4&t=2680s',
      'video_id': 'dr59GJ2T5v4'},
     {'author': 'AJ SIMMONS',
      'channel': 'AJ SIMMONS',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:18](https://www.youtube.com/watch?v=QBuGc_Q36dg&t=558s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Calculated clean mobile app as well all right so that's what I got for y'all "
              'until you click another video and go watch man watch another video why not '
              'binge.',
      'timestamp': 558,
      'timestamp_label': '[00:09:18]',
      'timestamp_seconds': 558,
      'tip': "Calculated clean mobile app as well all right so that's what I got for y'all "
             'until you click another video and go watch man watch another video why not '
             'binge.',
      'title': 'How To Get Commercial Cleaning Customers - Million Dollar Cleaning Company '
               'Shares Secret!!! (AJ SIMMONS)',
      'url': 'https://www.youtube.com/watch?v=QBuGc_Q36dg&t=558s',
      'video_id': 'QBuGc_Q36dg'},
     {'author': 'OctoClean Media',
      'channel': 'OctoClean Media',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:54](https://www.youtube.com/watch?v=1tf8JMWxi98&t=54s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Decision and do they have budget now we're going to go through each one of "
              'those individually what is pain.',
      'timestamp': 54,
      'timestamp_label': '[00:00:54]',
      'timestamp_seconds': 54,
      'tip': "Decision and do they have budget now we're going to go through each one of those "
             'individually what is pain.',
      'title': 'Do THIS to Close a Commercial Cleaning Deal Every Time (OctoClean Media)',
      'url': 'https://www.youtube.com/watch?v=1tf8JMWxi98&t=54s',
      'video_id': '1tf8JMWxi98'},
     {'author': 'iCleaners Commercial Cleaning Services',
      'channel': 'iCleaners Commercial Cleaning Services',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:02](https://www.youtube.com/watch?v=iigVbHUUCBE&t=782s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Find out this information is sometimes not through me but through other people '
              'that actually do that facility okay guys so this is it hope everybody has '
              'downloaded the app.',
      'timestamp': 782,
      'timestamp_label': '[00:13:02]',
      'timestamp_seconds': 782,
      'tip': 'Find out this information is sometimes not through me but through other people '
             'that actually do that facility okay guys so this is it hope everybody has '
             'downloaded the app.',
      'title': 'Using the Swept App (iCleaners Commercial Cleaning Services)',
      'url': 'https://www.youtube.com/watch?v=iigVbHUUCBE&t=782s',
      'video_id': 'iigVbHUUCBE'},
     {'author': 'Commercial Cleaning CEO',
      'channel': 'Commercial Cleaning CEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:42](https://www.youtube.com/watch?v=huf7CKyeee4&t=42s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And if you want my help and the full seven-figure blueprint to build a '
              'seven-figure commercial cleaning company, check out the links down below. If '
              "you don't know who I am, my name is Matt. I'm a seven-figure commercial "
              'cleaning CEO.',
      'timestamp': 42,
      'timestamp_label': '[00:00:42]',
      'timestamp_seconds': 42,
      'tip': 'And if you want my help and the full seven-figure blueprint to build a '
             'seven-figure commercial cleaning company, check out the links down below. If you '
             "don't know who I am, my name is Matt. I'm a seven-figure commercial cleaning "
             'CEO.',
      'title': 'How to Get Commercial Cleaning Contracts as a Residential Cleaner (Commercial '
               'Cleaning CEO)',
      'url': 'https://www.youtube.com/watch?v=huf7CKyeee4&t=42s',
      'video_id': 'huf7CKyeee4'},
     {'author': 'The Janitorial Store',
      'channel': 'The Janitorial Store',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:54](https://www.youtube.com/watch?v=YC2NrvVJqlg&t=54s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "What you're what you want to do the last thing you want to do is have a an "
              "employee that you're going to label a subcontractor and give them a 10.99 at "
              'the end of the year and expect them to pay for their taxes and stuff.',
      'timestamp': 54,
      'timestamp_label': '[00:00:54]',
      'timestamp_seconds': 54,
      'tip': "What you're what you want to do the last thing you want to do is have a an "
             "employee that you're going to label a subcontractor and give them a 10.99 at the "
             'end of the year and expect them to pay for their taxes and stuff.',
      'title': 'What is a 1099 employee? | The Janitorial Store (The Janitorial Store)',
      'url': 'https://www.youtube.com/watch?v=YC2NrvVJqlg&t=54s',
      'video_id': 'YC2NrvVJqlg'},
     {'author': 'AJ SIMMONS',
      'channel': 'AJ SIMMONS',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:22:58](https://www.youtube.com/watch?v=NHWdv_WG2B8&t=1378s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I'm going up is that right okay uh let's see what we got here favorite and "
              "actually before we do that one best decision you've made in business so far "
              'hmm.',
      'timestamp': 1378,
      'timestamp_label': '[00:22:58]',
      'timestamp_seconds': 1378,
      'tip': "I'm going up is that right okay uh let's see what we got here favorite and "
             "actually before we do that one best decision you've made in business so far hmm.",
      'title': 'How To Start A Cleaning Business With NO MONEY, NO SUPPLIES, NO WEBSITE! (AJ '
               'SIMMONS)',
      'url': 'https://www.youtube.com/watch?v=NHWdv_WG2B8&t=1378s',
      'video_id': 'NHWdv_WG2B8'}],
 3: [{'author': 'Clean Ops Guide',
      'channel': 'Clean Ops Guide',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=9ojOIxznBUc&t=21s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You can win a contract and still lose money every month. Welcome to Clean Ops '
              "Guide. Today, we're going to look at why pricing matters, what actually "
              'determines the cost of cleaning a building, and how to approach your next bid '
              'with more confidence.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': 'You can win a contract and still lose money every month. Welcome to Clean Ops '
             "Guide. Today, we're going to look at why pricing matters, what actually "
             'determines the cost of cleaning a building, and how to approach your next bid '
             'with more confidence.',
      'title': 'How to Price Commercial Cleaning Jobs Without Losing Money (Clean Ops Guide)',
      'url': 'https://www.youtube.com/watch?v=9ojOIxznBUc&t=21s',
      'video_id': '9ojOIxznBUc'},
     {'author': 'Karen Denton KSC',
      'channel': 'Karen Denton KSC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:30](https://www.youtube.com/watch?v=h7lD-HNIQ_o&t=30s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Too many business owners are out here guessing, under bidding, or missing '
              "opportunities because they don't understand how to calculate true cost, factor "
              "in labor, supplies, and profit. 's bid like I used to do with the franchises.",
      'timestamp': 30,
      'timestamp_label': '[00:00:30]',
      'timestamp_seconds': 30,
      'tip': 'Too many business owners are out here guessing, under bidding, or missing '
             "opportunities because they don't understand how to calculate true cost, factor "
             "in labor, supplies, and profit. 's bid like I used to do with the franchises.",
      'title': 'How to Price Commercial Cleaning Services (The Right Way!) (Karen Denton KSC)',
      'url': 'https://www.youtube.com/watch?v=h7lD-HNIQ_o&t=30s',
      'video_id': 'h7lD-HNIQ_o'},
     {'author': 'Vetted Biz | Best Franchise Opportunities to Buy',
      'channel': 'Vetted Biz | Best Franchise Opportunities to Buy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:51](https://www.youtube.com/watch?v=rQxrqnty1Cs&t=171s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Looking at it that you understand if you're going to be more of a area "
              "developer master and really growing a large business or if you're looking more "
              'for a side game you might be a better fit for being a unit level franchisee for '
              'commercial cleaning.',
      'timestamp': 171,
      'timestamp_label': '[00:02:51]',
      'timestamp_seconds': 171,
      'tip': "Looking at it that you understand if you're going to be more of a area developer "
             "master and really growing a large business or if you're looking more for a side "
             'game you might be a better fit for being a unit level franchisee for commercial '
             'cleaning.',
      'title': 'The Secret to Massive Profits with Cleaning Franchises! 💰📈 (Vetted Biz | Best '
               'Franchise Opportunities to Buy)',
      'url': 'https://www.youtube.com/watch?v=rQxrqnty1Cs&t=171s',
      'video_id': 'rQxrqnty1Cs'},
     {'author': 'True Trade Cost',
      'channel': 'True Trade Cost',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:12](https://www.youtube.com/watch?v=8lFhFbsEuDc&t=132s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Then it builds a clean quote with every schedule priced, ready to send tonight. '
              'After the job, the job log shows which accounts actually made money. The '
              'commercial cleaning pricing calculator works in Excel or Google Sheets, $49.',
      'timestamp': 132,
      'timestamp_label': '[00:02:12]',
      'timestamp_seconds': 132,
      'tip': 'Then it builds a clean quote with every schedule priced, ready to send tonight. '
             'After the job, the job log shows which accounts actually made money. The '
             'commercial cleaning pricing calculator works in Excel or Google Sheets, $49.',
      'title': 'How Much to Charge for Commercial Cleaning | Commercial Cleaning Pricing '
               'Calculator Walkthrough (True Trade Cost)',
      'url': 'https://www.youtube.com/watch?v=8lFhFbsEuDc&t=132s',
      'video_id': '8lFhFbsEuDc'},
     {'author': 'Channel Zero Marketing',
      'channel': 'Channel Zero Marketing',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=Ey7iPjW1uZQ&t=21s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'How much should I charge cleaning twice a week? " And I\'m in these groups and '
              'I actually had Claude AI go and scrape several of these groups, 1,900 post and '
              'the most common question was about pricing, how to price commercial accounts. '
              'And this one got 49 comments.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': 'How much should I charge cleaning twice a week? " And I\'m in these groups and I '
             'actually had Claude AI go and scrape several of these groups, 1,900 post and the '
             'most common question was about pricing, how to price commercial accounts. And '
             'this one got 49 comments.',
      'title': 'How to Price Your First Commercial Cleaning Contract (Real Example) (Channel '
               'Zero Marketing)',
      'url': 'https://www.youtube.com/watch?v=Ey7iPjW1uZQ&t=21s',
      'video_id': 'Ey7iPjW1uZQ'},
     {'author': 'Cleaning Business Tools',
      'channel': 'Cleaning Business Tools',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:36](https://www.youtube.com/watch?v=skflEiwVHxw&t=36s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Then add any add-ons, take off any recurring discount, and round up. And the '
              'price never goes below your minimum job price. Everything starts on the '
              'Settings tab. Target labor cost is what one cleaner hour costs you. Your pay or '
              'wage, plus payroll.',
      'timestamp': 36,
      'timestamp_label': '[00:00:36]',
      'timestamp_seconds': 36,
      'tip': 'Then add any add-ons, take off any recurring discount, and round up. And the '
             'price never goes below your minimum job price. Everything starts on the Settings '
             'tab. Target labor cost is what one cleaner hour costs you. Your pay or wage, '
             'plus payroll.',
      'title': 'How to Price a House Cleaning Job (Real Math, Step by Step) (Cleaning Business '
               'Tools)',
      'url': 'https://www.youtube.com/watch?v=skflEiwVHxw&t=36s',
      'video_id': 'skflEiwVHxw'},
     {'author': 'Janibid',
      'channel': 'Janibid',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:38](https://www.youtube.com/watch?v=9FeuDZZNdKI&t=98s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Two hours go ahead and calculate it again it's going to punch out the every "
              'other week monthly cost so monthly total cost 186 monthly total profit 250 um '
              "monthly total price to the customer 436 added 83.33% profit and that's it "
              'pretty simple pretty easy to use.',
      'timestamp': 98,
      'timestamp_label': '[00:01:38]',
      'timestamp_seconds': 98,
      'tip': "Two hours go ahead and calculate it again it's going to punch out the every "
             'other week monthly cost so monthly total cost 186 monthly total profit 250 um '
             "monthly total price to the customer 436 added 83.33% profit and that's it pretty "
             'simple pretty easy to use.',
      'title': 'How to Bid Commercial Cleaning Services? Free Commercial Cleaning Calculator '
               '(Janibid)',
      'url': 'https://www.youtube.com/watch?v=9FeuDZZNdKI&t=98s',
      'video_id': '9FeuDZZNdKI'},
     {'author': 'Janibid',
      'channel': 'Janibid',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:54](https://www.youtube.com/watch?v=Q0_kmHGx6FI&t=114s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Um, and then you go ahead and calculate it. Once you hit calculate, it's going "
              "to give you the total monthly cost. It's going to tell you the monthly profit "
              'and the total price to the customer.',
      'timestamp': 114,
      'timestamp_label': '[00:01:54]',
      'timestamp_seconds': 114,
      'tip': "Um, and then you go ahead and calculate it. Once you hit calculate, it's going "
             "to give you the total monthly cost. It's going to tell you the monthly profit "
             'and the total price to the customer.',
      'title': 'Free Commercial Calculator App - How to price commercial cleaning? (Janibid)',
      'url': 'https://www.youtube.com/watch?v=Q0_kmHGx6FI&t=114s',
      'video_id': 'Q0_kmHGx6FI'},
     {'author': 'The Janitorial Store',
      'channel': 'The Janitorial Store',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:00](https://www.youtube.com/watch?v=RNflg846cs4&t=360s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "More it's gonna cost them so anyway so those are all things that you want to "
              "keep in mind when you're pricing post construction cleanup you know it's a.",
      'timestamp': 360,
      'timestamp_label': '[00:06:00]',
      'timestamp_seconds': 360,
      'tip': "More it's gonna cost them so anyway so those are all things that you want to "
             "keep in mind when you're pricing post construction cleanup you know it's a.",
      'title': 'How to price post construction cleaning (The Janitorial Store)',
      'url': 'https://www.youtube.com/watch?v=RNflg846cs4&t=360s',
      'video_id': 'RNflg846cs4'},
     {'author': 'UpFlip',
      'channel': 'UpFlip',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:55](https://www.youtube.com/watch?v=PUIZGbefocg&t=895s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You have thousands every month for a really low cost. But outside of that, you '
              'have to come and really see the place, right? Are profit margins higher here or '
              'about the same? The margins are about the same, actually.',
      'timestamp': 895,
      'timestamp_label': '[00:14:55]',
      'timestamp_seconds': 895,
      'tip': 'You have thousands every month for a really low cost. But outside of that, you '
             'have to come and really see the place, right? Are profit margins higher here or '
             'about the same? The margins are about the same, actually.',
      'title': 'How He Makes $250K/Year Cleaning Homes... From His Laptop?! (UpFlip)',
      'url': 'https://www.youtube.com/watch?v=PUIZGbefocg&t=895s',
      'video_id': 'PUIZGbefocg'},
     {'author': 'OctoClean Media',
      'channel': 'OctoClean Media',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:54](https://www.youtube.com/watch?v=j_wLBMK7Flk&t=114s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Takes to actually clean the facility how much your labor will cost your '
              'overhead and your profit you then must be able to demonstrate those estimations '
              'to a.',
      'timestamp': 114,
      'timestamp_label': '[00:01:54]',
      'timestamp_seconds': 114,
      'tip': 'Takes to actually clean the facility how much your labor will cost your overhead '
             'and your profit you then must be able to demonstrate those estimations to a.',
      'title': 'How to Create a Kickass Commercial Cleaning Proposal (OctoClean Media)',
      'url': 'https://www.youtube.com/watch?v=j_wLBMK7Flk&t=114s',
      'video_id': 'j_wLBMK7Flk'},
     {'author': 'Commercial Cleaning CEO',
      'channel': 'Commercial Cleaning CEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=TCaVkVk94bc&t=15s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Commercial cleaning company by working with property managers and how they '
              "differ from other types of clients within our company we've worked with.",
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Commercial cleaning company by working with property managers and how they '
             "differ from other types of clients within our company we've worked with.",
      'title': 'How To Win Big Cleaning Contracts With Property Managers (Commercial Cleaning '
               'CEO)',
      'url': 'https://www.youtube.com/watch?v=TCaVkVk94bc&t=15s',
      'video_id': 'TCaVkVk94bc'},
     {'author': 'AJ SIMMONS',
      'channel': 'AJ SIMMONS',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:56](https://www.youtube.com/watch?v=Bbay8f0-XFM&t=116s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Under bid their contracts right and when I say under bid I mean they price way '
              'too low I just did a video probably about two weeks ago on my channel uh.',
      'timestamp': 116,
      'timestamp_label': '[00:01:56]',
      'timestamp_seconds': 116,
      'tip': 'Under bid their contracts right and when I say under bid I mean they price way '
             'too low I just did a video probably about two weeks ago on my channel uh.',
      'title': 'Is A Cleaning Franchise Worth It? (AJ SIMMONS)',
      'url': 'https://www.youtube.com/watch?v=Bbay8f0-XFM&t=116s',
      'video_id': 'Bbay8f0-XFM'},
     {'author': 'Service On Command',
      'channel': 'Service On Command',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:23](https://www.youtube.com/watch?v=CXVWaxMTpV0&t=263s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Instructions on there if there's special hot spots that we for but this is the "
              'basic rundown and swept at if you have any questions please let us know.',
      'timestamp': 263,
      'timestamp_label': '[00:04:23]',
      'timestamp_seconds': 263,
      'tip': "Instructions on there if there's special hot spots that we for but this is the "
             'basic rundown and swept at if you have any questions please let us know.',
      'title': 'Training - Swept Mobile App (Service On Command)',
      'url': 'https://www.youtube.com/watch?v=CXVWaxMTpV0&t=263s',
      'video_id': 'CXVWaxMTpV0'},
     {'author': 'The Janitorial Store',
      'channel': 'The Janitorial Store',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:31](https://www.youtube.com/watch?v=1c9Ty46MQbg&t=271s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Uh share and if you haven't already go ahead and uh you know click on that bell "
              "notification so you can get any notifications for new videos that we're putting "
              "out so hopefully this did help and thanks for checking in today and we'll see "
              'you next time.',
      'timestamp': 271,
      'timestamp_label': '[00:04:31]',
      'timestamp_seconds': 271,
      'tip': "Uh share and if you haven't already go ahead and uh you know click on that bell "
             "notification so you can get any notifications for new videos that we're putting "
             "out so hopefully this did help and thanks for checking in today and we'll see "
             'you next time.',
      'title': 'Pricing Day Porter Service | The Janitorial Store (The Janitorial Store)',
      'url': 'https://www.youtube.com/watch?v=1c9Ty46MQbg&t=271s',
      'video_id': '1c9Ty46MQbg'}],
 4: [{'author': 'Small Business Bid School',
      'channel': 'Small Business Bid School',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:27](https://www.youtube.com/watch?v=uARedcLLS5c&t=87s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Let's budget $180 per month for cleaning products, trash liners, equipment "
              "wear, and other consumables. We'll estimate $120 per month. We also need to "
              'cover business overhead, such as administration, insurance, software, and other '
              'operating expenses.',
      'timestamp': 87,
      'timestamp_label': '[00:01:27]',
      'timestamp_seconds': 87,
      'tip': "Let's budget $180 per month for cleaning products, trash liners, equipment wear, "
             "and other consumables. We'll estimate $120 per month. We also need to cover "
             'business overhead, such as administration, insurance, software, and other '
             'operating expenses.',
      'title': 'How to Price a Government Cleaning Contract (Step-by-Step) (Small Business Bid '
               'School)',
      'url': 'https://www.youtube.com/watch?v=uARedcLLS5c&t=87s',
      'video_id': 'uARedcLLS5c'},
     {'author': 'Mark Etherton - The Millionaire Playbook',
      'channel': 'Mark Etherton - The Millionaire Playbook',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:46](https://www.youtube.com/watch?v=PG-8SEuPFQk&t=46s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "5 to 10 times more, but only if you know what you're doing. Step one, choose "
              "your service area. You don't need the whole state. Pick a 25 to 50 mile radius "
              'where construction is booming. Step two, set up your business with an LLC, '
              'insurance, website, simple email.',
      'timestamp': 46,
      'timestamp_label': '[00:00:46]',
      'timestamp_seconds': 46,
      'tip': "5 to 10 times more, but only if you know what you're doing. Step one, choose "
             "your service area. You don't need the whole state. Pick a 25 to 50 mile radius "
             'where construction is booming. Step two, set up your business with an LLC, '
             'insurance, website, simple email.',
      'title': 'How to Start a Construction Cleaning Company (What Most People Get Wrong) '
               '#constructioncleaning (Mark Etherton - The Millionaire Playbook)',
      'url': 'https://www.youtube.com/watch?v=PG-8SEuPFQk&t=46s',
      'video_id': 'PG-8SEuPFQk'},
     {'author': 'Owlsfield Financial Corp',
      'channel': 'Owlsfield Financial Corp',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:29](https://www.youtube.com/watch?v=LARqKW_L-QI&t=89s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Check the locations, hours, required experience, insurance, security rules, '
              'site visit questions, deadline, and submission dead A large contract useful if '
              'your company can perform it. Attend the site visit when the bid requires one.',
      'timestamp': 89,
      'timestamp_label': '[00:01:29]',
      'timestamp_seconds': 89,
      'tip': 'Check the locations, hours, required experience, insurance, security rules, site '
             'visit questions, deadline, and submission dead A large contract useful if your '
             'company can perform it. Attend the site visit when the bid requires one.',
      'title': 'Government Cleaning Contracts: How to Bid and Win More Business (Owlsfield '
               'Financial Corp)',
      'url': 'https://www.youtube.com/watch?v=LARqKW_L-QI&t=89s',
      'video_id': 'LARqKW_L-QI'},
     {'author': 'The Professional Cleaner',
      'channel': 'The Professional Cleaner',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:51](https://www.youtube.com/watch?v=DDLzG49aDvU&t=471s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Your cleaning business like an office and you want to ensure that computers and '
              'other equipment stored there and with commercial auto insurance you would.',
      'timestamp': 471,
      'timestamp_label': '[00:07:51]',
      'timestamp_seconds': 471,
      'tip': 'Your cleaning business like an office and you want to ensure that computers and '
             'other equipment stored there and with commercial auto insurance you would.',
      'title': 'Cleaning Business Insurance & Bonding… MUST KNOWS 🧼 💸 (The Professional '
               'Cleaner)',
      'url': 'https://www.youtube.com/watch?v=DDLzG49aDvU&t=471s',
      'video_id': 'DDLzG49aDvU'},
     {'author': 'OctoClean Media',
      'channel': 'OctoClean Media',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:19](https://www.youtube.com/watch?v=SXNq_81x8SY&t=319s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You and your area now you have your hourly rate you have your building '
              "inventory and you're able to figure out how much time it's going to take you to "
              "clean a facility every day so what's this equation on how to bid accounts it's "
              'pretty simple.',
      'timestamp': 319,
      'timestamp_label': '[00:05:19]',
      'timestamp_seconds': 319,
      'tip': 'You and your area now you have your hourly rate you have your building inventory '
             "and you're able to figure out how much time it's going to take you to clean a "
             "facility every day so what's this equation on how to bid accounts it's pretty "
             'simple.',
      'title': 'How to Bid Commercial Cleaning Jobs (FORMULA INCLUDED) (OctoClean Media)',
      'url': 'https://www.youtube.com/watch?v=SXNq_81x8SY&t=319s',
      'video_id': 'SXNq_81x8SY'},
     {'author': 'Jazmine Tates',
      'channel': 'Jazmine Tates',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:50](https://www.youtube.com/watch?v=g8OVdfYHogY&t=530s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '300 cleaning day program below. It will walk you through step-by-step pricing, '
              'structuring, positioning, scripts, back-end support, back-end setup, start the '
              "structure, not the stress. And remember, y'all, lean in a little bit, lean in. "
              'Experience cleaning is optional.',
      'timestamp': 530,
      'timestamp_label': '[00:08:50]',
      'timestamp_seconds': 530,
      'tip': '300 cleaning day program below. It will walk you through step-by-step pricing, '
             'structuring, positioning, scripts, back-end support, back-end setup, start the '
             "structure, not the stress. And remember, y'all, lean in a little bit, lean in. "
             'Experience cleaning is optional.',
      'title': 'How to Start a Cleaning Business With No Experience (2026 Beginner Guide) '
               '(Jazmine Tates)',
      'url': 'https://www.youtube.com/watch?v=g8OVdfYHogY&t=530s',
      'video_id': 'g8OVdfYHogY'},
     {'author': 'The Coyle Group - Business Insurance',
      'channel': 'The Coyle Group - Business Insurance',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:08](https://www.youtube.com/watch?v=HSh0vcHYmUI&t=188s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And fortunately, we at The Coile Group, we do all these things and more to help '
              'you make the best decisions when it comes to business insurance, not just '
              'workers comp for your janitorial business.',
      'timestamp': 188,
      'timestamp_label': '[00:03:08]',
      'timestamp_seconds': 188,
      'tip': 'And fortunately, we at The Coile Group, we do all these things and more to help '
             'you make the best decisions when it comes to business insurance, not just '
             'workers comp for your janitorial business.',
      'title': 'Workers Compensation for Janitorial Contractors in NY (The Coyle Group - '
               'Business Insurance)',
      'url': 'https://www.youtube.com/watch?v=HSh0vcHYmUI&t=188s',
      'video_id': 'HSh0vcHYmUI'},
     {'author': 'Commercial Cleaning CEO',
      'channel': 'Commercial Cleaning CEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:26](https://www.youtube.com/watch?v=9BXhBVRp_XU&t=266s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Going to cover how to do each of those in just a sec but real quick if you do '
              "own a commercial cleaning company and you're wanting to grow to seven figures.",
      'timestamp': 266,
      'timestamp_label': '[00:04:26]',
      'timestamp_seconds': 266,
      'tip': 'Going to cover how to do each of those in just a sec but real quick if you do '
             "own a commercial cleaning company and you're wanting to grow to seven figures.",
      'title': 'W2 Employees Or 1099 Contractors? Which To Pick For Your Cleaning Business '
               '(Commercial Cleaning CEO)',
      'url': 'https://www.youtube.com/watch?v=9BXhBVRp_XU&t=266s',
      'video_id': '9BXhBVRp_XU'},
     {'author': 'Medicine and Health Sciences at Bethel University',
      'channel': 'Medicine and Health Sciences at Bethel University',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:06](https://www.youtube.com/watch?v=jf-dh46niMw&t=306s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Let it you know wait for like five to ten minutes typically about a minute is '
              "the appropriate length of time to be able to disinfect everything so now we're "
              "just going to take your disposable towel make sure that you're wiping the "
              'entire surface up and cleaning the area.',
      'timestamp': 306,
      'timestamp_label': '[00:05:06]',
      'timestamp_seconds': 306,
      'tip': 'Let it you know wait for like five to ten minutes typically about a minute is '
             "the appropriate length of time to be able to disinfect everything so now we're "
             "just going to take your disposable towel make sure that you're wiping the entire "
             'surface up and cleaning the area.',
      'title': 'Cleaning and Decontaminating a Blood Borne Pathogen Spill Skills Video '
               '(Medicine and Health Sciences at Bethel University)',
      'url': 'https://www.youtube.com/watch?v=jf-dh46niMw&t=306s',
      'video_id': 'jf-dh46niMw'},
     {'author': 'Elite Business Insurance',
      'channel': 'Elite Business Insurance',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:34](https://www.youtube.com/watch?v=PGrPNqCYNvY&t=214s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You need so give us a call give us a chance we'll give you as many options as "
              "possible and we'll give you the best price possible 185 0 81 9 elite business "
              'insurance we are a Leeds.',
      'timestamp': 214,
      'timestamp_label': '[00:03:34]',
      'timestamp_seconds': 214,
      'tip': "You need so give us a call give us a chance we'll give you as many options as "
             "possible and we'll give you the best price possible 185 0 81 9 elite business "
             'insurance we are a Leeds.',
      'title': 'Janitorial Bonding Insurance - Janitorial Bonding Insurance Explained (Elite '
               'Business Insurance)',
      'url': 'https://www.youtube.com/watch?v=PGrPNqCYNvY&t=214s',
      'video_id': 'PGrPNqCYNvY'},
     {'author': 'AJ SIMMONS',
      'channel': 'AJ SIMMONS',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:18:47](https://www.youtube.com/watch?v=mOnf6pk37_c&t=1127s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So that'll be your daytime inspections. And then when you're doing daytime "
              "inspections, y'all didn't clean this network, use your app. If you got a "
              'tablet, it look even better.',
      'timestamp': 1127,
      'timestamp_label': '[00:18:47]',
      'timestamp_seconds': 1127,
      'tip': "So that'll be your daytime inspections. And then when you're doing daytime "
             "inspections, y'all didn't clean this network, use your app. If you got a tablet, "
             'it look even better.',
      'title': 'All Cleaners Need To Watch THIS! (Commercial Cleaning Training) (AJ SIMMONS)',
      'url': 'https://www.youtube.com/watch?v=mOnf6pk37_c&t=1127s',
      'video_id': 'mOnf6pk37_c'},
     {'author': 'Construction Clean Partners',
      'channel': 'Construction Clean Partners',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:24](https://www.youtube.com/watch?v=vx1fwmFh0zM&t=144s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Jobs are worth 10 20 $30,000 uh the estimated job amount we put it on the '
              "Facebook ad so you can decide there but if it's worth 20 or 30,000 bucks it "
              'might be worth getting the insurance for anyways uh hope to hear from you soon '
              'and bye-bye.',
      'timestamp': 144,
      'timestamp_label': '[00:02:24]',
      'timestamp_seconds': 144,
      'tip': 'Jobs are worth 10 20 $30,000 uh the estimated job amount we put it on the '
             "Facebook ad so you can decide there but if it's worth 20 or 30,000 bucks it "
             'might be worth getting the insurance for anyways uh hope to hear from you soon '
             'and bye-bye.',
      'title': 'How to win a post construction final cleanup job with Construction Clean '
               'Partners (Construction Clean Partners)',
      'url': 'https://www.youtube.com/watch?v=vx1fwmFh0zM&t=144s',
      'video_id': 'vx1fwmFh0zM'},
     {'author': 'Commercial Cleaning CEO',
      'channel': 'Commercial Cleaning CEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=-IxCGolievQ&t=15s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Commercial cleaning business or if you have a cleaning business already and '
              "you're wanting to know how do you get those $100,000 $200,000 $300,000 or even.",
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Commercial cleaning business or if you have a cleaning business already and '
             "you're wanting to know how do you get those $100,000 $200,000 $300,000 or even.",
      'title': 'How to Get BIG Commercial Cleaning Contracts (Commercial Cleaning CEO)',
      'url': 'https://www.youtube.com/watch?v=-IxCGolievQ&t=15s',
      'video_id': '-IxCGolievQ'},
     {'author': 'Stewart Facility Services',
      'channel': 'Stewart Facility Services',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:44](https://www.youtube.com/watch?v=7uKR0mnlF9Q&t=104s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Any issues that need to be resolved or any information that as I previously '
              'said is a blanket message for all Associates please do not reply to anything in '
              'this chat it is for incoming information only.',
      'timestamp': 104,
      'timestamp_label': '[00:01:44]',
      'timestamp_seconds': 104,
      'tip': 'Any issues that need to be resolved or any information that as I previously said '
             'is a blanket message for all Associates please do not reply to anything in this '
             'chat it is for incoming information only.',
      'title': 'Swept app cont. (Stewart Facility Services)',
      'url': 'https://www.youtube.com/watch?v=7uKR0mnlF9Q&t=104s',
      'video_id': '7uKR0mnlF9Q'},
     {'author': 'AJ SIMMONS',
      'channel': 'AJ SIMMONS',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:29](https://www.youtube.com/watch?v=7pVd69Als0I&t=149s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Stripped and waxed the floor two weeks ago I love strip of wax and floors it's "
              'the best before and after effect you could get but like just do you have to '
              'always be learning and always be involved.',
      'timestamp': 149,
      'timestamp_label': '[00:02:29]',
      'timestamp_seconds': 149,
      'tip': "Stripped and waxed the floor two weeks ago I love strip of wax and floors it's "
             'the best before and after effect you could get but like just do you have to '
             'always be learning and always be involved.',
      'title': "$15 Million Dollar Cleaning Company Owner's Advice To New Cleaning Business "
               'Owners (AJ SIMMONS)',
      'url': 'https://www.youtube.com/watch?v=7pVd69Als0I&t=149s',
      'video_id': '7pVd69Als0I'}],
 5: [{'author': 'Anton Pantio',
      'channel': 'Anton Pantio',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:45](https://www.youtube.com/watch?v=-1k_o5iWj8w&t=405s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'t even contract out cleaning. Can't find good leads if you don't know who "
              "you're looking for. For commercial cleaning, the best prospects to reach out by "
              'cold calling are facility managers or property managers, operation directors, '
              'business owners.',
      'timestamp': 405,
      'timestamp_label': '[00:06:45]',
      'timestamp_seconds': 405,
      'tip': "'t even contract out cleaning. Can't find good leads if you don't know who "
             "you're looking for. For commercial cleaning, the best prospects to reach out by "
             'cold calling are facility managers or property managers, operation directors, '
             'business owners.',
      'title': 'Cold Calling For Commercial Cleaning Companies (Script + Live Call) (Anton '
               'Pantio)',
      'url': 'https://www.youtube.com/watch?v=-1k_o5iWj8w&t=405s',
      'video_id': '-1k_o5iWj8w'},
     {'author': 'The Professional Cleaner',
      'channel': 'The Professional Cleaner',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:12](https://www.youtube.com/watch?v=jl4sDr8y-Ws&t=192s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "To do everything you'll be an expert of nothing so sometimes students will ask "
              "me how do you work carpet cleaning into your commercial bids I don't well what.",
      'timestamp': 192,
      'timestamp_label': '[00:03:12]',
      'timestamp_seconds': 192,
      'tip': "To do everything you'll be an expert of nothing so sometimes students will ask "
             "me how do you work carpet cleaning into your commercial bids I don't well what.",
      'title': '4 HIDDEN TRAPS that will KILL your cleaning business ☠️ (The Professional '
               'Cleaner)',
      'url': 'https://www.youtube.com/watch?v=jl4sDr8y-Ws&t=192s',
      'video_id': 'jl4sDr8y-Ws'},
     {'author': 'ISSA Media',
      'channel': 'ISSA Media',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=nBB03PNbUHI&t=21s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And to get into this, I'd like to welcome two industry pros who know the ins "
              "and the outs of bidding commercial cleaning jobs. So, I'm pleased to welcome "
              'two professionals from Octo Clean, Matthew and Greg.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': "And to get into this, I'd like to welcome two industry pros who know the ins and "
             "the outs of bidding commercial cleaning jobs. So, I'm pleased to welcome two "
             'professionals from Octo Clean, Matthew and Greg.',
      'title': 'How to Bid Commercial Cleaning Jobs Like a Pro (ISSA Media)',
      'url': 'https://www.youtube.com/watch?v=nBB03PNbUHI&t=21s',
      'video_id': 'nBB03PNbUHI'},
     {'author': 'OctoClean Media',
      'channel': 'OctoClean Media',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=9TymiXPWhyY&t=15s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Cleaning as a way to get into the contract after they occupy if you clean '
              'college dorm rooms after they move out you may be a good construction cleanup.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Cleaning as a way to get into the contract after they occupy if you clean '
             'college dorm rooms after they move out you may be a good construction cleanup.',
      'title': 'Construction Cleaning: Build Your Profits! | OctoClean Podcast Ep. 17 '
               '(OctoClean Media)',
      'url': 'https://www.youtube.com/watch?v=9TymiXPWhyY&t=15s',
      'video_id': '9TymiXPWhyY'},
     {'author': 'Surety Bonds Direct',
      'channel': 'Surety Bonds Direct',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:14](https://www.youtube.com/watch?v=uMW_ZJMW0ZU&t=134s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Amount number six if your business of services commercial properties typical '
              'bond amounts usually start at twenty five thousand dollars all the way up to.',
      'timestamp': 134,
      'timestamp_label': '[00:02:14]',
      'timestamp_seconds': 134,
      'tip': 'Amount number six if your business of services commercial properties typical '
             'bond amounts usually start at twenty five thousand dollars all the way up to.',
      'title': 'Janitorial Bond - Getting Bonded for a Cleaning Business (Surety Bonds Direct)',
      'url': 'https://www.youtube.com/watch?v=uMW_ZJMW0ZU&t=134s',
      'video_id': 'uMW_ZJMW0ZU'},
     {'author': 'Janitorial Manager',
      'channel': 'Janitorial Manager',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:52](https://www.youtube.com/watch?v=c9NTVgpJrx0&t=112s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'This feature provides greater trust in the health and safety of a facility. If '
              'an area is marked NOT Clean, the app helps look for other clean areas nearby, '
              'And allows them to request service for the dirty area.',
      'timestamp': 112,
      'timestamp_label': '[00:01:52]',
      'timestamp_seconds': 112,
      'tip': 'This feature provides greater trust in the health and safety of a facility. If '
             'an area is marked NOT Clean, the app helps look for other clean areas nearby, '
             'And allows them to request service for the dirty area.',
      'title': 'Enhance Your Value with Scan4Clean | QR Codes For Your Cleaning Operations '
               '(Janitorial Manager)',
      'url': 'https://www.youtube.com/watch?v=c9NTVgpJrx0&t=112s',
      'video_id': 'c9NTVgpJrx0'},
     {'author': 'Mike Mak',
      'channel': 'Mike Mak',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:35](https://www.youtube.com/watch?v=92cY7nLDqTI&t=35s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Hey, I'm Mike Mack, author of the Amazon bestseller Pickup Cash, Not Trash. And "
              'I have a dose of reality for you. People fail in this business because they '
              'chase the wrong customers. They clean houses or tiny offices for $300 a month.',
      'timestamp': 35,
      'timestamp_label': '[00:00:35]',
      'timestamp_seconds': 35,
      'tip': "Hey, I'm Mike Mack, author of the Amazon bestseller Pickup Cash, Not Trash. And "
             'I have a dose of reality for you. People fail in this business because they '
             'chase the wrong customers. They clean houses or tiny offices for $300 a month.',
      'title': "The Secret to Getting Big Office Cleaning Contracts (Even If You're Brand New) "
               '(Mike Mak)',
      'url': 'https://www.youtube.com/watch?v=92cY7nLDqTI&t=35s',
      'video_id': '92cY7nLDqTI'},
     {'author': 'Commercial Cleaning CEO',
      'channel': 'Commercial Cleaning CEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=598Td1ks52Y&t=15s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Cleaning contracts I have successfully used this exact formula to build my '
              'personal commercial cleaning company Beyond seven figures in less than 5.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Cleaning contracts I have successfully used this exact formula to build my '
             'personal commercial cleaning company Beyond seven figures in less than 5.',
      'title': 'Price Commercial Cleaning RIGHT | Cleaning Bid Calculator (Commercial Cleaning '
               'CEO)',
      'url': 'https://www.youtube.com/watch?v=598Td1ks52Y&t=15s',
      'video_id': '598Td1ks52Y'},
     {'author': 'Active Learning',
      'channel': 'Active Learning',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:39](https://www.youtube.com/watch?v=WPuiNvUKURw&t=219s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'For example, a needlestick injury has a small but real risk of HIV '
              'transmission, about 0. 3% for an exposure to blood. This means that for every '
              '1,000 accidental needlesticks, one person risks contracting HIV.',
      'timestamp': 219,
      'timestamp_label': '[00:03:39]',
      'timestamp_seconds': 219,
      'tip': 'For example, a needlestick injury has a small but real risk of HIV transmission, '
             'about 0. 3% for an exposure to blood. This means that for every 1,000 accidental '
             'needlesticks, one person risks contracting HIV.',
      'title': 'Bloodborne Pathogens Explained | OSHA BBP Standards & Safety for Healthcare '
               'Workers (Active Learning)',
      'url': 'https://www.youtube.com/watch?v=WPuiNvUKURw&t=219s',
      'video_id': 'WPuiNvUKURw'},
     {'author': 'Window Cleaning BluePrint',
      'channel': 'Window Cleaning BluePrint',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:46](https://www.youtube.com/watch?v=K4OAVqDBtgE&t=46s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And I jump like up on the booth and I open up these big blinds and I'm cleaning "
              'them all. And then he wants me to clean the blinds, the blinds. So, I got into '
              'blind cleaning. Then he\'s like, "What about the ceiling fans?".',
      'timestamp': 46,
      'timestamp_label': '[00:00:46]',
      'timestamp_seconds': 46,
      'tip': "And I jump like up on the booth and I open up these big blinds and I'm cleaning "
             'them all. And then he wants me to clean the blinds, the blinds. So, I got into '
             'blind cleaning. Then he\'s like, "What about the ceiling fans?".',
      'title': 'How To Sell Window Cleaning Jobs On The Spot #keithkalfas #windowcleaning '
               '#windowcleaningblueprint (Window Cleaning BluePrint)',
      'url': 'https://www.youtube.com/watch?v=K4OAVqDBtgE&t=46s',
      'video_id': 'K4OAVqDBtgE'},
     {'author': 'AJ SIMMONS',
      'channel': 'AJ SIMMONS',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:38](https://www.youtube.com/watch?v=BK0p3k8OpRo&t=578s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'It says as an entrepreneur is an individual who starts, organizes, and manages '
              'a business venture assuming the primary financial risk in exchange for '
              'potential rewards. The key part on that is primary financial risk.',
      'timestamp': 578,
      'timestamp_label': '[00:09:38]',
      'timestamp_seconds': 578,
      'tip': 'It says as an entrepreneur is an individual who starts, organizes, and manages a '
             'business venture assuming the primary financial risk in exchange for potential '
             'rewards. The key part on that is primary financial risk.',
      'title': 'COMMERCIAL CLEANING FRANCHISES ARE NOT SCAMS (AJ SIMMONS)',
      'url': 'https://www.youtube.com/watch?v=BK0p3k8OpRo&t=578s',
      'video_id': 'BK0p3k8OpRo'},
     {'author': 'Bloodborne Pathogen',
      'channel': 'Bloodborne Pathogen',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:54](https://www.youtube.com/watch?v=gLeTNOVfh8o&t=354s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The blood-borne pathogen standards this list shows examples of some of the '
              "professions at risk of occupational exposure to blood-borne pathogens let's "
              "take a quiz to review what you've learned.",
      'timestamp': 354,
      'timestamp_label': '[00:05:54]',
      'timestamp_seconds': 354,
      'tip': 'The blood-borne pathogen standards this list shows examples of some of the '
             "professions at risk of occupational exposure to blood-borne pathogens let's take "
             "a quiz to review what you've learned.",
      'title': 'OSHA Bloodborne Pathogen Training, Bloodborne Pathogen Video (Bloodborne '
               'Pathogen)',
      'url': 'https://www.youtube.com/watch?v=gLeTNOVfh8o&t=354s',
      'video_id': 'gLeTNOVfh8o'},
     {'author': 'OctoClean Media',
      'channel': 'OctoClean Media',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:24](https://www.youtube.com/watch?v=45JohGIULbI&t=24s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And I think I surprise a lot of folks when I get on to one-on-one coaching '
              'calls, and you know, they say, "Well, it\'s a 25,000 sq ft space." And I\'m '
              'like, "Okay, well, tell me more about the space. You know, what is the density '
              'of this area?".',
      'timestamp': 24,
      'timestamp_label': '[00:00:24]',
      'timestamp_seconds': 24,
      'tip': 'And I think I surprise a lot of folks when I get on to one-on-one coaching '
             'calls, and you know, they say, "Well, it\'s a 25,000 sq ft space." And I\'m '
             'like, "Okay, well, tell me more about the space. You know, what is the density '
             'of this area?".',
      'title': 'Commercial Cleaning Contracts: Beginner Pricing Mistakes to Avoid (OctoClean '
               'Media)',
      'url': 'https://www.youtube.com/watch?v=45JohGIULbI&t=24s',
      'video_id': '45JohGIULbI'},
     {'author': 'Commercial Cleaning CEO',
      'channel': 'Commercial Cleaning CEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=xqw9zag57Uk&t=15s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And you'll be able to decide what should you do about commercial cleaning "
              'franchises and which one is right for you or should you completely avoid them.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "And you'll be able to decide what should you do about commercial cleaning "
             'franchises and which one is right for you or should you completely avoid them.',
      'title': 'Commercial Cleaning Franchise Types | Choose Wisely! (Commercial Cleaning CEO)',
      'url': 'https://www.youtube.com/watch?v=xqw9zag57Uk&t=15s',
      'video_id': 'xqw9zag57Uk'},
     {'author': 'Commercial Cleaning CEO',
      'channel': 'Commercial Cleaning CEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=turpTn9YjJA&t=15s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'That you call or the people that you quote with the people that you want to '
              "earn the business from if you can't seem to get them to close the deal with "
              'you.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'That you call or the people that you quote with the people that you want to earn '
             "the business from if you can't seem to get them to close the deal with you.",
      'title': 'How To Get Commercial Cleaning Contracts With CTA Targeting (Commercial '
               'Cleaning CEO)',
      'url': 'https://www.youtube.com/watch?v=turpTn9YjJA&t=15s',
      'video_id': 'turpTn9YjJA'}],
 6: [{'author': 'Carolyn Arellano',
      'channel': 'Carolyn Arellano',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:58](https://www.youtube.com/watch?v=xJ6TUBTc4Qo&t=118s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You are positioning your company as a professional option for when they're "
              'ready to make that change. Think of cold calling as opening a door, not closing '
              "a deal. Now, let's talk about why cold calling matters so much in commercial "
              'cleaning.',
      'timestamp': 118,
      'timestamp_label': '[00:01:58]',
      'timestamp_seconds': 118,
      'tip': "You are positioning your company as a professional option for when they're ready "
             'to make that change. Think of cold calling as opening a door, not closing a '
             "deal. Now, let's talk about why cold calling matters so much in commercial "
             'cleaning.',
      'title': 'Cold Calling For Commercial Cleaning Companies (Carolyn Arellano)',
      'url': 'https://www.youtube.com/watch?v=xJ6TUBTc4Qo&t=118s',
      'video_id': 'xJ6TUBTc4Qo'},
     {'author': 'AJ SIMMONS',
      'channel': 'AJ SIMMONS',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:20](https://www.youtube.com/watch?v=Xvc-7yo1lng&t=740s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Commercial cleaning company you ready to start growing bigger go to www.clean '
              'Biz leads.com and you can buy leads there and then also you can get discount '
              'on.',
      'timestamp': 740,
      'timestamp_label': '[00:12:20]',
      'timestamp_seconds': 740,
      'tip': 'Commercial cleaning company you ready to start growing bigger go to www.clean '
             'Biz leads.com and you can buy leads there and then also you can get discount on.',
      'title': 'Cleaning Business Walkthrough Tips (AJ SIMMONS)',
      'url': 'https://www.youtube.com/watch?v=Xvc-7yo1lng&t=740s',
      'video_id': 'Xvc-7yo1lng'},
     {'author': 'DJ The Boss',
      'channel': 'DJ The Boss',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:20](https://www.youtube.com/watch?v=ZVDOV6jG8Dw&t=380s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The lead form and it was my first client the gymnastics facility that you guys '
              'have seen and a lot of videos we still clean it to this day.',
      'timestamp': 380,
      'timestamp_label': '[00:06:20]',
      'timestamp_seconds': 380,
      'tip': 'The lead form and it was my first client the gymnastics facility that you guys '
             'have seen and a lot of videos we still clean it to this day.',
      'title': 'How i got my First Commercial Cleaning contract: how to start a commercial '
               'cleaning business (DJ The Boss)',
      'url': 'https://www.youtube.com/watch?v=ZVDOV6jG8Dw&t=380s',
      'video_id': 'ZVDOV6jG8Dw'},
     {'author': 'SEO Growth Partners',
      'channel': 'SEO Growth Partners',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:47](https://www.youtube.com/watch?v=1A40YzhpJ5Q&t=47s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s about a month and a half. Commercial cleaning services, 4,800 square feet, "
              'commercial small office space, monthly office and showroom cleaning, first '
              'floor is 6,500 square feet. Uh weekly cleaning, retail shop, restaurant, office '
              'cleaning, one-time carpet cleaning.',
      'timestamp': 47,
      'timestamp_label': '[00:00:47]',
      'timestamp_seconds': 47,
      'tip': "'s about a month and a half. Commercial cleaning services, 4,800 square feet, "
             'commercial small office space, monthly office and showroom cleaning, first floor '
             'is 6,500 square feet. Uh weekly cleaning, retail shop, restaurant, office '
             'cleaning, one-time carpet cleaning.',
      'title': 'Commercial Cleaning & Janitorial Services SEO Case Study - From Business '
               'Launch to 10+ Leads/Mo (SEO Growth Partners)',
      'url': 'https://www.youtube.com/watch?v=1A40YzhpJ5Q&t=47s',
      'video_id': '1A40YzhpJ5Q'},
     {'author': 'Solo Business Systems',
      'channel': 'Solo Business Systems',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:55](https://www.youtube.com/watch?v=hf0U17FyA58&t=55s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Business,  an office manager whose job is not to find the cheapest cleaner. '
              "It's to never have to think about cleaning again.",
      'timestamp': 55,
      'timestamp_label': '[00:00:55]',
      'timestamp_seconds': 55,
      'tip': "Business,  an office manager whose job is not to find the cheapest cleaner. It's "
             'to never have to think about cleaning again.',
      'title': 'Commercial Cleaning: How to Win Your First Office Contract (Walkthrough + Bid '
               'Worksheet) (Solo Business Systems)',
      'url': 'https://www.youtube.com/watch?v=hf0U17FyA58&t=55s',
      'video_id': 'hf0U17FyA58'},
     {'author': 'Jeremy Dixon',
      'channel': 'Jeremy Dixon',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:15](https://www.youtube.com/watch?v=-LFfJivPXKw&t=435s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'We can take care of all of your lead generation needs for your code calling '
              'business I hope this video was helpful for you and I will see you in the next.',
      'timestamp': 435,
      'timestamp_label': '[00:07:15]',
      'timestamp_seconds': 435,
      'tip': 'We can take care of all of your lead generation needs for your code calling '
             'business I hope this video was helpful for you and I will see you in the next.',
      'title': 'Cold Calling For Commercial Cleaning Companies (Script + Live Calls) (Jeremy '
               'Dixon)',
      'url': 'https://www.youtube.com/watch?v=-LFfJivPXKw&t=435s',
      'video_id': '-LFfJivPXKw'},
     {'author': 'The Profitable Cleaner',
      'channel': 'The Profitable Cleaner',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:31:52](https://www.youtube.com/watch?v=u3njpVGKi3M&t=1912s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'CSV, what I go ahead and do, I go over to chat GPT cuz AI is freaking awesome. '
              'So, let me make sure you guys see my chat GPT here and I say clean up this lead '
              "list and remove duplicates. This is a cheap lead finder, guys, so there's going "
              'to be duplicates.',
      'timestamp': 1912,
      'timestamp_label': '[00:31:52]',
      'timestamp_seconds': 1912,
      'tip': 'CSV, what I go ahead and do, I go over to chat GPT cuz AI is freaking awesome. '
             'So, let me make sure you guys see my chat GPT here and I say clean up this lead '
             "list and remove duplicates. This is a cheap lead finder, guys, so there's going "
             'to be duplicates.',
      'title': 'How to Get Janitorial Contracts with Cold Calling, Email & Door-to-Door Sales '
               '| Ep 185 (The Profitable Cleaner)',
      'url': 'https://www.youtube.com/watch?v=u3njpVGKi3M&t=1912s',
      'video_id': 'u3njpVGKi3M'},
     {'author': 'AJ SIMMONS',
      'channel': 'AJ SIMMONS',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:21:45](https://www.youtube.com/watch?v=srB5UatlJlU&t=1305s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I know when I was cleaning um when I was cleaning myself like when I first '
              'pulled myself out cuz I knew like I was trying to take client calls and take '
              'lead calls while cleaning and like getting caught up and turning down bad job I '
              'mean know other jobs.',
      'timestamp': 1305,
      'timestamp_label': '[00:21:45]',
      'timestamp_seconds': 1305,
      'tip': 'I know when I was cleaning um when I was cleaning myself like when I first '
             'pulled myself out cuz I knew like I was trying to take client calls and take '
             'lead calls while cleaning and like getting caught up and turning down bad job I '
             'mean know other jobs.',
      'title': 'I Built a Million-Dollar Cleaning Brand — Here’s What It Really Takes | AJ '
               'Simmons x Jazmine Tates (AJ SIMMONS)',
      'url': 'https://www.youtube.com/watch?v=srB5UatlJlU&t=1305s',
      'video_id': 'srB5UatlJlU'},
     {'author': 'Commercial Cleaning CEO',
      'channel': 'Commercial Cleaning CEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=j4duUCt9Dlw&t=15s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Cleaning CEO and in this video we're going to unpack how do you find how do you "
              'bid how do you successfully submit and calculate the quotes for commercial.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "Cleaning CEO and in this video we're going to unpack how do you find how do you "
             'bid how do you successfully submit and calculate the quotes for commercial.',
      'title': 'How To Win Government Commercial Cleaning Contracts (Commercial Cleaning CEO)',
      'url': 'https://www.youtube.com/watch?v=j4duUCt9Dlw&t=15s',
      'video_id': 'j4duUCt9Dlw'},
     {'author': 'OctoClean Media',
      'channel': 'OctoClean Media',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:29:04](https://www.youtube.com/watch?v=52I2LNERY3E&t=1744s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "How are you you know somebody's not getting the right end of the deal here. "
              "It's either the client or the vendor. And usually it's the vendor who suffers. "
              "Um because they'll bully them into you can't get the business yourself.",
      'timestamp': 1744,
      'timestamp_label': '[00:29:04]',
      'timestamp_seconds': 1744,
      'tip': "How are you you know somebody's not getting the right end of the deal here. It's "
             "either the client or the vendor. And usually it's the vendor who suffers. Um "
             "because they'll bully them into you can't get the business yourself.",
      'title': 'What is a Day Porter?  Expectations vs Reality in Cleaning Businesses | Ep. 31 '
               '(OctoClean Media)',
      'url': 'https://www.youtube.com/watch?v=52I2LNERY3E&t=1744s',
      'video_id': '52I2LNERY3E'},
     {'author': 'MA Exec. Office of Labor and Workforce Development',
      'channel': 'MA Exec. Office of Labor and Workforce Development',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:38:19](https://www.youtube.com/watch?v=4xmWcKLIfmA&t=2299s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Sick first before the needle stick ever happened workers who are assigned to '
              "clean up these syringes must be offered the hepatitis B vaccine if you've.",
      'timestamp': 2299,
      'timestamp_label': '[00:38:19]',
      'timestamp_seconds': 2299,
      'tip': 'Sick first before the needle stick ever happened workers who are assigned to '
             "clean up these syringes must be offered the hepatitis B vaccine if you've.",
      'title': 'Bloodborne Pathogens Training Guide 11-23-15 (MA Exec. Office of Labor and '
               'Workforce Development)',
      'url': 'https://www.youtube.com/watch?v=4xmWcKLIfmA&t=2299s',
      'video_id': '4xmWcKLIfmA'},
     {'author': 'Mike Mak',
      'channel': 'Mike Mak',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=G2qoM4LqGdM&t=15s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I'm here to help stick with me to the end and I'm going to share proven "
              'strategies that you can use right now to land your first five office cleaning.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "I'm here to help stick with me to the end and I'm going to share proven "
             'strategies that you can use right now to land your first five office cleaning.',
      'title': 'How To Get Your First 5 Office Cleaning Contracts FAST? (Mike Mak)',
      'url': 'https://www.youtube.com/watch?v=G2qoM4LqGdM&t=15s',
      'video_id': 'G2qoM4LqGdM'},
     {'author': 'SafetyTrainingNetwork.com',
      'channel': 'SafetyTrainingNetwork.com',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:40](https://www.youtube.com/watch?v=Pr6reN7o5NI&t=160s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'This disease are slim hepatitis b however is far more prevalent it is a liver '
              'disease caused by the hepatitis b virus it ranges in severity from a mild '
              'illness lasting a few weeks to a serious long-term illness that can lead to '
              'liver disease or liver cancer.',
      'timestamp': 160,
      'timestamp_label': '[00:02:40]',
      'timestamp_seconds': 160,
      'tip': 'This disease are slim hepatitis b however is far more prevalent it is a liver '
             'disease caused by the hepatitis b virus it ranges in severity from a mild '
             'illness lasting a few weeks to a serious long-term illness that can lead to '
             'liver disease or liver cancer.',
      'title': 'Bloodborne Pathogens for Custodians (SafetyTrainingNetwork.com)',
      'url': 'https://www.youtube.com/watch?v=Pr6reN7o5NI&t=160s',
      'video_id': 'Pr6reN7o5NI'},
     {'author': 'S.N.M. Cleaning Service',
      'channel': 'S.N.M. Cleaning Service',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:00](https://www.youtube.com/watch?v=8s441oHT2b4&t=180s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'We spend a lot of time just in detail work edging taking care of corners a lot '
              "of the places that the machines can't get to spend a great deal of time just on "
              'a lot of those detail works.',
      'timestamp': 180,
      'timestamp_label': '[00:03:00]',
      'timestamp_seconds': 180,
      'tip': 'We spend a lot of time just in detail work edging taking care of corners a lot '
             "of the places that the machines can't get to spend a great deal of time just on "
             'a lot of those detail works.',
      'title': 'STRIP AND REFINISH 20,000 SQUARE FEET of VCT floor - strip & wax 2025 (S.N.M. '
               'Cleaning Service)',
      'url': 'https://www.youtube.com/watch?v=8s441oHT2b4&t=180s',
      'video_id': '8s441oHT2b4'},
     {'author': 'AJ SIMMONS',
      'channel': 'AJ SIMMONS',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:22](https://www.youtube.com/watch?v=7VHAkhs_HG4&t=502s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Sense if you got any other questions drop it down below under the video and '
              "I'll make sure I answer it soon thank y'all I'm aj simmons see y'all later.",
      'timestamp': 502,
      'timestamp_label': '[00:08:22]',
      'timestamp_seconds': 502,
      'tip': "Sense if you got any other questions drop it down below under the video and I'll "
             "make sure I answer it soon thank y'all I'm aj simmons see y'all later.",
      'title': 'How To Bid Cleaning Jobs Per Hour Or Per Sqft (AJ SIMMONS)',
      'url': 'https://www.youtube.com/watch?v=7VHAkhs_HG4&t=502s',
      'video_id': '7VHAkhs_HG4'}],
 7: [{'author': 'Janitorial Empire',
      'channel': 'Janitorial Empire',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:11](https://www.youtube.com/watch?v=8ireVJkHvoo&t=311s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'A surprising amount of business is won simply because one company followed up '
              "while another didn't. And finally, step eight, use the first contract to get "
              'the second. Once you win an account, perform the work extremely well.',
      'timestamp': 311,
      'timestamp_label': '[00:05:11]',
      'timestamp_seconds': 311,
      'tip': 'A surprising amount of business is won simply because one company followed up '
             "while another didn't. And finally, step eight, use the first contract to get the "
             'second. Once you win an account, perform the work extremely well.',
      'title': 'How to Get Your First Commercial Cleaning Contract (Step-by-Step) (Janitorial '
               'Empire)',
      'url': 'https://www.youtube.com/watch?v=8ireVJkHvoo&t=311s',
      'video_id': '8ireVJkHvoo'},
     {'author': 'OctoClean Media',
      'channel': 'OctoClean Media',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:38](https://www.youtube.com/watch?v=YE3spKAx9HI&t=158s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Else that's that three-step cleaning process yes and then you have punch so a "
              'punch list would be that the architect and the construction manager come.',
      'timestamp': 158,
      'timestamp_label': '[00:02:38]',
      'timestamp_seconds': 158,
      'tip': "Else that's that three-step cleaning process yes and then you have punch so a "
             'punch list would be that the architect and the construction manager come.',
      'title': 'Post Construction Cleaning Differences: Better Than Commercial Cleaning? '
               '(OctoClean Media)',
      'url': 'https://www.youtube.com/watch?v=YE3spKAx9HI&t=158s',
      'video_id': 'YE3spKAx9HI'},
     {'author': 'Mathew Rogers',
      'channel': 'Mathew Rogers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:35](https://www.youtube.com/watch?v=xzidtSceePw&t=755s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Use a commercial-grade vacuum with strong suction to lift as much dry soil as '
              'possible. Step number two, you want to get into the pre-spray application. This '
              'is where you prepare the carpet for deep cleaning.',
      'timestamp': 755,
      'timestamp_label': '[00:12:35]',
      'timestamp_seconds': 755,
      'tip': 'Use a commercial-grade vacuum with strong suction to lift as much dry soil as '
             'possible. Step number two, you want to get into the pre-spray application. This '
             'is where you prepare the carpet for deep cleaning.',
      'title': 'How To Start A $1000/Day Carpet Cleaning Business (Free Course) (Mathew '
               'Rogers)',
      'url': 'https://www.youtube.com/watch?v=xzidtSceePw&t=755s',
      'video_id': 'xzidtSceePw'},
     {'author': 'Commercial Cleaning CEO',
      'channel': 'Commercial Cleaning CEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:25:45](https://www.youtube.com/watch?v=esIqvQsbxco&t=1545s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "But when you have a referral partnership and you're going to give them "
              "business, they're going to give you business, then you're you grow "
              'exponentially faster. This has actually been the number one producing method '
              'historically in our commercial cleaning company.',
      'timestamp': 1545,
      'timestamp_label': '[00:25:45]',
      'timestamp_seconds': 1545,
      'tip': "But when you have a referral partnership and you're going to give them business, "
             "they're going to give you business, then you're you grow exponentially faster. "
             'This has actually been the number one producing method historically in our '
             'commercial cleaning company.',
      'title': '21 Ways To Get More Commercial Cleaning Contracts (Commercial Cleaning CEO)',
      'url': 'https://www.youtube.com/watch?v=esIqvQsbxco&t=1545s',
      'video_id': 'esIqvQsbxco'},
     {'author': 'AJ SIMMONS',
      'channel': 'AJ SIMMONS',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:53](https://www.youtube.com/watch?v=mp0PpDrOpYM&t=53s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I guess it All right, first things first, how would you do it? It's the same "
              'steps, all right? So, you still want to go follow that video how to start a '
              'cleaning business step-by-step or no BS guide or whatever. The the video I got '
              'is uh right on my homepage.',
      'timestamp': 53,
      'timestamp_label': '[00:00:53]',
      'timestamp_seconds': 53,
      'tip': "I guess it All right, first things first, how would you do it? It's the same "
             'steps, all right? So, you still want to go follow that video how to start a '
             'cleaning business step-by-step or no BS guide or whatever. The the video I got '
             'is uh right on my homepage.',
      'title': 'How To Start A Cleaning Business SOLO! (AJ SIMMONS)',
      'url': 'https://www.youtube.com/watch?v=mp0PpDrOpYM&t=53s',
      'video_id': 'mp0PpDrOpYM'},
     {'author': 'Training Videos',
      'channel': 'Training Videos',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:49](https://www.youtube.com/watch?v=AxPTARAhtdA&t=109s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'It is critical that you follow these exactly. Skipping any part of this process '
              'can compromise the safety of the entire facility. Steps one and two are to '
              'secure the area and suit up. Block off the spill site immediately and have a '
              'co-worker stand guard to prevent traffic.',
      'timestamp': 109,
      'timestamp_label': '[00:01:49]',
      'timestamp_seconds': 109,
      'tip': 'It is critical that you follow these exactly. Skipping any part of this process '
             'can compromise the safety of the entire facility. Steps one and two are to '
             'secure the area and suit up. Block off the spill site immediately and have a '
             'co-worker stand guard to prevent traffic.',
      'title': 'OSHA Bloodborne Pathogens Spill Cleanup Training (Training Videos)',
      'url': 'https://www.youtube.com/watch?v=AxPTARAhtdA&t=109s',
      'video_id': 'AxPTARAhtdA'},
     {'author': 'Imperial Brady',
      'channel': 'Imperial Brady',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:55](https://www.youtube.com/watch?v=4ynia2-e2hw&t=175s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Protective eyewear and a face mask to thoroughly clean and disinfect an '
              'inpatient area you should follow the following steps.',
      'timestamp': 175,
      'timestamp_label': '[00:02:55]',
      'timestamp_seconds': 175,
      'tip': 'Protective eyewear and a face mask to thoroughly clean and disinfect an '
             'inpatient area you should follow the following steps.',
      'title': 'Steps to Terminal Cleaning a Patient Room (Imperial Brady)',
      'url': 'https://www.youtube.com/watch?v=4ynia2-e2hw&t=175s',
      'video_id': '4ynia2-e2hw'},
     {'author': 'recruiterbackoffice',
      'channel': 'recruiterbackoffice',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:14](https://www.youtube.com/watch?v=VumHp7Ist1c&t=194s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Is there a contract are there benefits what's the duration of the assignment "
              "and then what's the normal business process involving the termination or any.",
      'timestamp': 194,
      'timestamp_label': '[00:03:14]',
      'timestamp_seconds': 194,
      'tip': "Is there a contract are there benefits what's the duration of the assignment and "
             "then what's the normal business process involving the termination or any.",
      'title': '1099 Independent Contractor vs. W-2 Employees (recruiterbackoffice)',
      'url': 'https://www.youtube.com/watch?v=VumHp7Ist1c&t=194s',
      'video_id': 'VumHp7Ist1c'},
     {'author': 'BuddSafety',
      'channel': 'BuddSafety',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:02](https://www.youtube.com/watch?v=eEnUgYz8rXU&t=362s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Let's go debrief back at your office, if that's all right. Speaker 2: That "
              "sounds great. Hey, anytime, the last step when you're cleaning up a blood "
              'spill, bloodborne pathogen spill, you got to wash your hands for 30 seconds, so '
              "I'll meet you in my office.",
      'timestamp': 362,
      'timestamp_label': '[00:06:02]',
      'timestamp_seconds': 362,
      'tip': "Let's go debrief back at your office, if that's all right. Speaker 2: That "
             "sounds great. Hey, anytime, the last step when you're cleaning up a blood spill, "
             "bloodborne pathogen spill, you got to wash your hands for 30 seconds, so I'll "
             'meet you in my office.',
      'title': 'Blood Borne Pathogens Safety - BBP Kit (BuddSafety)',
      'url': 'https://www.youtube.com/watch?v=eEnUgYz8rXU&t=362s',
      'video_id': 'eEnUgYz8rXU'},
     {'author': 'Imperial Brady',
      'channel': 'Imperial Brady',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:15](https://www.youtube.com/watch?v=tCz-yNw0WBo&t=255s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Fluid spill kit it's time for the second step after you have everything that "
              'you need ready step two is to commence the cleanup process disposable '
              'absorbent.',
      'timestamp': 255,
      'timestamp_label': '[00:04:15]',
      'timestamp_seconds': 255,
      'tip': "Fluid spill kit it's time for the second step after you have everything that you "
             'need ready step two is to commence the cleanup process disposable absorbent.',
      'title': 'How to Clean Up Bloodborne Pathogens: A Methodical Guide to Safety and '
               'Compliance (Imperial Brady)',
      'url': 'https://www.youtube.com/watch?v=tCz-yNw0WBo&t=255s',
      'video_id': 'tCz-yNw0WBo'},
     {'author': 'Austin Davis',
      'channel': 'Austin Davis',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:16](https://www.youtube.com/watch?v=M2j87yHQY10&t=16s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'This white dust white mortar typically you guys can see this whenever you guys '
              'are looking at brand new homes brand new uh communities commercial buildings '
              'you.',
      'timestamp': 16,
      'timestamp_label': '[00:00:16]',
      'timestamp_seconds': 16,
      'tip': 'This white dust white mortar typically you guys can see this whenever you guys '
             'are looking at brand new homes brand new uh communities commercial buildings '
             'you.',
      'title': 'Post Construction Cleaning | Construction Dust Solved With No Brushing (Austin '
               'Davis)',
      'url': 'https://www.youtube.com/watch?v=M2j87yHQY10&t=16s',
      'video_id': 'M2j87yHQY10'},
     {'author': 'Kizzy Parks',
      'channel': 'Kizzy Parks',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:24](https://www.youtube.com/watch?v=UVPaRFj3LDE&t=144s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'What also is helpful if you have it there are free options you will want to '
              'only submit the 1449. you just simply you go into organize Pages you can get a '
              'step-by-step online to extract these two pages very simple.',
      'timestamp': 144,
      'timestamp_label': '[00:02:24]',
      'timestamp_seconds': 144,
      'tip': 'What also is helpful if you have it there are free options you will want to only '
             'submit the 1449. you just simply you go into organize Pages you can get a '
             'step-by-step online to extract these two pages very simple.',
      'title': 'How to Write a Proposal to the Government (Strategy + Full Walkthrough) (Kizzy '
               'Parks)',
      'url': 'https://www.youtube.com/watch?v=UVPaRFj3LDE&t=144s',
      'video_id': 'UVPaRFj3LDE'},
     {'author': 'OctoClean Media',
      'channel': 'OctoClean Media',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:11](https://www.youtube.com/watch?v=X3MX2xOshA4&t=251s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Apply the stripper solution the other will be for your rinse bucket we are not '
              'going to get into the stripping process here but clean mops and neutralizing.',
      'timestamp': 251,
      'timestamp_label': '[00:04:11]',
      'timestamp_seconds': 251,
      'tip': 'Apply the stripper solution the other will be for your rinse bucket we are not '
             'going to get into the stripping process here but clean mops and neutralizing.',
      'title': 'How to Price Floor Care (VCT Strip and Finish Pricing) (OctoClean Media)',
      'url': 'https://www.youtube.com/watch?v=X3MX2xOshA4&t=251s',
      'video_id': 'X3MX2xOshA4'},
     {'author': 'Grow My Cleaning Company',
      'channel': 'Grow My Cleaning Company',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:45](https://www.youtube.com/watch?v=D9L_Gw-APSU&t=165s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Many employees you have run around there on any given day currently we've got "
              "about 138 540 that's we've got people that run from 8 to 10 so only having a to "
              "employee variance over 100 that's that's a you do it a good job Cynthia.",
      'timestamp': 165,
      'timestamp_label': '[00:02:45]',
      'timestamp_seconds': 165,
      'tip': "Many employees you have run around there on any given day currently we've got "
             "about 138 540 that's we've got people that run from 8 to 10 so only having a to "
             "employee variance over 100 that's that's a you do it a good job Cynthia.",
      'title': 'Everything You Need to Know Before Setting Up Your Own Janitorial Franchise '
               '(Grow My Cleaning Company)',
      'url': 'https://www.youtube.com/watch?v=D9L_Gw-APSU&t=165s',
      'video_id': 'D9L_Gw-APSU'},
     {'author': 'AJ SIMMONS',
      'channel': 'AJ SIMMONS',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:53](https://www.youtube.com/watch?v=IMsJ1NxKfUk&t=473s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Be looking at the pictures on Google if they got any pictures on Google looking '
              'at scoping out the building before you go stuff like this but put your all into '
              "it you know what I mean and go in all right y'all.",
      'timestamp': 473,
      'timestamp_label': '[00:07:53]',
      'timestamp_seconds': 473,
      'tip': 'Be looking at the pictures on Google if they got any pictures on Google looking '
             'at scoping out the building before you go stuff like this but put your all into '
             "it you know what I mean and go in all right y'all.",
      'title': 'I Started a Commercial Cleaning Service (My 1st Walkthrough) (AJ SIMMONS)',
      'url': 'https://www.youtube.com/watch?v=IMsJ1NxKfUk&t=473s',
      'video_id': 'IMsJ1NxKfUk'}],
 8: [{'author': 'ONLY MAIDS PODCAST',
      'channel': 'ONLY MAIDS PODCAST',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:25:04](https://www.youtube.com/watch?v=aQj7G__L-iE&t=1504s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Starting your commercial cleaning business and um keeping things organized '
              "awesome the win is a uh it's a software that that that includes a CRM and a uh "
              'bid advisor.',
      'timestamp': 1504,
      'timestamp_label': '[00:25:04]',
      'timestamp_seconds': 1504,
      'tip': 'Starting your commercial cleaning business and um keeping things organized '
             "awesome the win is a uh it's a software that that that includes a CRM and a uh "
             'bid advisor.',
      'title': 'Hot Seat | Commercial Cleaning Crash Course: Get the Walkthrough, Price the '
               'Job & Win the Account (ONLY MAIDS PODCAST)',
      'url': 'https://www.youtube.com/watch?v=aQj7G__L-iE&t=1504s',
      'video_id': 'aQj7G__L-iE'},
     {'author': 'The Janitorial Store',
      'channel': 'The Janitorial Store',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:29](https://www.youtube.com/watch?v=gTK5pzrNCqg&t=149s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Much easier is if you have a tool and on the janitorial store.com we actually '
              'have a post construction bidding calculator and it just makes the whole.',
      'timestamp': 149,
      'timestamp_label': '[00:02:29]',
      'timestamp_seconds': 149,
      'tip': 'Much easier is if you have a tool and on the janitorial store.com we actually '
             'have a post construction bidding calculator and it just makes the whole.',
      'title': 'How to price a post construction cleaning for a commercial building (The '
               'Janitorial Store)',
      'url': 'https://www.youtube.com/watch?v=gTK5pzrNCqg&t=149s',
      'video_id': 'gTK5pzrNCqg'},
     {'author': 'Cleaning Launch',
      'channel': 'Cleaning Launch',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:16](https://www.youtube.com/watch?v=vAsWtmVSISA&t=316s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Commercial contracts and that is using LinkedIn organic and you want to be '
              'using a software to add people message people and invite them to your company.',
      'timestamp': 316,
      'timestamp_label': '[00:05:16]',
      'timestamp_seconds': 316,
      'tip': 'Commercial contracts and that is using LinkedIn organic and you want to be using '
             'a software to add people message people and invite them to your company.',
      'title': '7 FREE Ways to get Commercial CLEANING Contracts (copy this strategy) '
               '(Cleaning Launch)',
      'url': 'https://www.youtube.com/watch?v=vAsWtmVSISA&t=316s',
      'video_id': 'vAsWtmVSISA'},
     {'author': 'victoria menifee',
      'channel': 'victoria menifee',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:48:43](https://www.youtube.com/watch?v=5htVyehKCRo&t=2923s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Now, this right here they're small disadvantaged business. They're they don't "
              "have anything else. You can see they're not veteran owned. We can look and see "
              'exactly what they are right in this area with their with their um economic '
              'data.',
      'timestamp': 2923,
      'timestamp_label': '[00:48:43]',
      'timestamp_seconds': 2923,
      'tip': "Now, this right here they're small disadvantaged business. They're they don't "
             "have anything else. You can see they're not veteran owned. We can look and see "
             'exactly what they are right in this area with their with their um economic data.',
      'title': 'SECRET SHORTCUT TO GOVERNMENT CLEANING CONTRACT TO WIN BIG (NO-BID METHOD) '
               '(victoria menifee)',
      'url': 'https://www.youtube.com/watch?v=5htVyehKCRo&t=2923s',
      'video_id': '5htVyehKCRo'},
     {'author': 'Contractor Plus',
      'channel': 'Contractor Plus',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:22](https://www.youtube.com/watch?v=9IJ1pi5IQ_E&t=22s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Built for commercial cleaning and facility contracts, not generic service '
              'businesses. If you run multi-location accounts, tools for night shifts, GPS '
              'check-ins, inspection score cards, and client-ready reporting. Before you '
              'shortlist, get clear on your operation.',
      'timestamp': 22,
      'timestamp_label': '[00:00:22]',
      'timestamp_seconds': 22,
      'tip': 'Built for commercial cleaning and facility contracts, not generic service '
             'businesses. If you run multi-location accounts, tools for night shifts, GPS '
             'check-ins, inspection score cards, and client-ready reporting. Before you '
             'shortlist, get clear on your operation.',
      'title': '9 BEST Janitorial Software Platforms in 2026 (Commercial Cleaning Ranked) '
               '(Contractor Plus)',
      'url': 'https://www.youtube.com/watch?v=9IJ1pi5IQ_E&t=22s',
      'video_id': '9IJ1pi5IQ_E'},
     {'author': 'Commercial Cleaning CEO',
      'channel': 'Commercial Cleaning CEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:37](https://www.youtube.com/watch?v=SU1OB2thaKo&t=157s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And when you say you're spending this time on it what are you doing currently? "
              "We we got the website up and running. Um of course I've been doing all the "
              'paperwork and the business account, checking account um set up. You know, '
              'stumbled across your platform.',
      'timestamp': 157,
      'timestamp_label': '[00:02:37]',
      'timestamp_seconds': 157,
      'tip': "And when you say you're spending this time on it what are you doing currently? "
             "We we got the website up and running. Um of course I've been doing all the "
             'paperwork and the business account, checking account um set up. You know, '
             'stumbled across your platform.',
      'title': 'Just Starting? How To Land Your First Commercial Cleaning Contract (Commercial '
               'Cleaning CEO)',
      'url': 'https://www.youtube.com/watch?v=SU1OB2thaKo&t=157s',
      'video_id': 'SU1OB2thaKo'},
     {'author': 'OctoClean Media',
      'channel': 'OctoClean Media',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:25](https://www.youtube.com/watch?v=KNxKwtNpe_s&t=205s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Changes to account for the medical cleaning times I'm about to give you some "
              'information that will transform your company so hang on tight medical.',
      'timestamp': 205,
      'timestamp_label': '[00:03:25]',
      'timestamp_seconds': 205,
      'tip': "Changes to account for the medical cleaning times I'm about to give you some "
             'information that will transform your company so hang on tight medical.',
      'title': 'How to Bid Medical Cleaning (Formula + Example) (OctoClean Media)',
      'url': 'https://www.youtube.com/watch?v=KNxKwtNpe_s&t=205s',
      'video_id': 'KNxKwtNpe_s'},
     {'author': 'XO Safety',
      'channel': 'XO Safety',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:51](https://www.youtube.com/watch?v=-8zP-by6RbU&t=411s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Work Practice Controls reduce the likelihood of exposure by altering the way a '
              'task is performed The most common Work Practice Control is frequent hand '
              'washing. Regular cleaning and decontamination of the work area is another Work '
              'Practice Control.',
      'timestamp': 411,
      'timestamp_label': '[00:06:51]',
      'timestamp_seconds': 411,
      'tip': 'Work Practice Controls reduce the likelihood of exposure by altering the way a '
             'task is performed The most common Work Practice Control is frequent hand '
             'washing. Regular cleaning and decontamination of the work area is another Work '
             'Practice Control.',
      'title': 'Bloodborne Pathogens Safety Training (XO Safety)',
      'url': 'https://www.youtube.com/watch?v=-8zP-by6RbU&t=411s',
      'video_id': '-8zP-by6RbU'},
     {'author': 'nurselyf',
      'channel': 'nurselyf',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:30](https://www.youtube.com/watch?v=Efj3Vo_qlBY&t=90s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Hazard communication standard. All chemicals and cleaning agents must be '
              'labeled and handled with training think material safety data sheets. Safe '
              'patient handling programs to reduce back injuries and muscularkeeletal '
              'disorders.',
      'timestamp': 90,
      'timestamp_label': '[00:01:30]',
      'timestamp_seconds': 90,
      'tip': 'Hazard communication standard. All chemicals and cleaning agents must be labeled '
             'and handled with training think material safety data sheets. Safe patient '
             'handling programs to reduce back injuries and muscularkeeletal disorders.',
      'title': 'OSHA in Healthcare: Key Safety Standards, Bloodborne Pathogens, PPE & '
               'Workplace Safety Explained (nurselyf)',
      'url': 'https://www.youtube.com/watch?v=Efj3Vo_qlBY&t=90s',
      'video_id': 'Efj3Vo_qlBY'},
     {'author': 'Swept',
      'channel': 'Swept',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:21:31](https://www.youtube.com/watch?v=lPuBkaocWL8&t=1291s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You'll make up an excuse and that's just the reality of it so going in knowing "
              'that you want software and why having that that intention will really help you '
              'be successful with it and it can completely transform your business.',
      'timestamp': 1291,
      'timestamp_label': '[00:21:31]',
      'timestamp_seconds': 1291,
      'tip': "You'll make up an excuse and that's just the reality of it so going in knowing "
             'that you want software and why having that that intention will really help you '
             'be successful with it and it can completely transform your business.',
      'title': 'Maximize the ROI of janitorial software (Swept)',
      'url': 'https://www.youtube.com/watch?v=lPuBkaocWL8&t=1291s',
      'video_id': 'lPuBkaocWL8'},
     {'author': 'AJ SIMMONS',
      'channel': 'AJ SIMMONS',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:30:04](https://www.youtube.com/watch?v=du4OAGZv9AE&t=1804s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re in the CBN network and you have a member if you're a member if you have "
              "access to the software, you'll be able to create a post on your CRM to where "
              'you can you can put them all out at one time. People tap in with me on on '
              'Facebook as well.',
      'timestamp': 1804,
      'timestamp_label': '[00:30:04]',
      'timestamp_seconds': 1804,
      'tip': "'re in the CBN network and you have a member if you're a member if you have "
             "access to the software, you'll be able to create a post on your CRM to where you "
             'can you can put them all out at one time. People tap in with me on on Facebook '
             'as well.',
      'title': 'How He Built A Million Dollar Cleaning Business! (AJ SIMMONS)',
      'url': 'https://www.youtube.com/watch?v=du4OAGZv9AE&t=1804s',
      'video_id': 'du4OAGZv9AE'},
     {'author': 'CleanGuru',
      'channel': 'CleanGuru',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:55](https://www.youtube.com/watch?v=nNPKmshBChQ&t=175s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "We're so excited that it's ready to go and we'd love for you to give it a try "
              "if you've never been a clean QC member before because it's brand-new just click "
              'on the link below and get your own free trial for 30 days starting now thanks.',
      'timestamp': 175,
      'timestamp_label': '[00:02:55]',
      'timestamp_seconds': 175,
      'tip': "We're so excited that it's ready to go and we'd love for you to give it a try if "
             "you've never been a clean QC member before because it's brand-new just click on "
             'the link below and get your own free trial for 30 days starting now thanks.',
      'title': 'CleanGuru - CleanQC Janitorial Inspection Software (CleanGuru)',
      'url': 'https://www.youtube.com/watch?v=nNPKmshBChQ&t=175s',
      'video_id': 'nNPKmshBChQ'},
     {'author': 'CSI Accounting',
      'channel': 'CSI Accounting',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:45](https://www.youtube.com/watch?v=kfUxzVfMpAk&t=225s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Questions about classifying workers or you're interested in our services check "
              'out our YouTube channel or go to our website and schedule a free consultation '
              'thanks so much for watching foreign.',
      'timestamp': 225,
      'timestamp_label': '[00:03:45]',
      'timestamp_seconds': 225,
      'tip': "Questions about classifying workers or you're interested in our services check "
             'out our YouTube channel or go to our website and schedule a free consultation '
             'thanks so much for watching foreign.',
      'title': '1099 Contractors vs W-2 Employees - How to Classify Your Workers (CSI '
               'Accounting)',
      'url': 'https://www.youtube.com/watch?v=kfUxzVfMpAk&t=225s',
      'video_id': 'kfUxzVfMpAk'},
     {'author': 'AJ SIMMONS',
      'channel': 'AJ SIMMONS',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:39](https://www.youtube.com/watch?v=vqE3IAR7B18&t=699s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Multiply the times four times in 4.33 times in a month so uh we'll do 601 time "
              "4.33 I don't have my calculator handy if you want to do that for me in the "
              "background right $61 hopefully y'all can see that that $61 time.",
      'timestamp': 699,
      'timestamp_label': '[00:11:39]',
      'timestamp_seconds': 699,
      'tip': "Multiply the times four times in 4.33 times in a month so uh we'll do 601 time "
             "4.33 I don't have my calculator handy if you want to do that for me in the "
             "background right $61 hopefully y'all can see that that $61 time.",
      'title': 'How To Bid Commercial and Residential Cleaning Jobs (Formula Included) (AJ '
               'SIMMONS)',
      'url': 'https://www.youtube.com/watch?v=vqE3IAR7B18&t=699s',
      'video_id': 'vqE3IAR7B18'},
     {'author': 'Modern Field Service',
      'channel': 'Modern Field Service',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:33](https://www.youtube.com/watch?v=Y00vfNH19Q4&t=33s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Tools like SendJim and Maidily are generally good at what they do, but what '
              'they do is houses. Booking a recurring home clean, reminding the customer, '
              'collecting payments. Commercial cleaning is a different business.',
      'timestamp': 33,
      'timestamp_label': '[00:00:33]',
      'timestamp_seconds': 33,
      'tip': 'Tools like SendJim and Maidily are generally good at what they do, but what they '
             'do is houses. Booking a recurring home clean, reminding the customer, collecting '
             'payments. Commercial cleaning is a different business.',
      'title': 'Best Janitorial & Commercial Cleaning Software 2026 (Modern Field Service)',
      'url': 'https://www.youtube.com/watch?v=Y00vfNH19Q4&t=33s',
      'video_id': 'Y00vfNH19Q4'}],
 9: [{'author': 'Business From Zero',
      'channel': 'Business From Zero',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:31](https://www.youtube.com/watch?v=fvJFWetfuFA&t=91s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'First, form your LLC, pull a free IRS EIN, and open a business checking account '
              'for $350. Second, put $650 down on a $1 million to $2 million commercial '
              'general liability policy plus a $10,000 janitorial surety bond. Here is the '
              'compliance trap.',
      'timestamp': 91,
      'timestamp_label': '[00:01:31]',
      'timestamp_seconds': 91,
      'tip': 'First, form your LLC, pull a free IRS EIN, and open a business checking account '
             'for $350. Second, put $650 down on a $1 million to $2 million commercial general '
             'liability policy plus a $10,000 janitorial surety bond. Here is the compliance '
             'trap.',
      'title': 'How to Start a Commercial Cleaning Business for $4,200 (Business From Zero)',
      'url': 'https://www.youtube.com/watch?v=fvJFWetfuFA&t=91s',
      'video_id': 'fvJFWetfuFA'},
     {'author': 'AJ SIMMONS',
      'channel': 'AJ SIMMONS',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:00](https://www.youtube.com/watch?v=pqTeTRcPhKg&t=300s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Every city and county does not require you to have a business license for a '
              'cleaning company. Now, some might require you to have a business license for a '
              'residential cleaning service but not a commercial cleaning service or vice '
              'versa.',
      'timestamp': 300,
      'timestamp_label': '[00:05:00]',
      'timestamp_seconds': 300,
      'tip': 'Every city and county does not require you to have a business license for a '
             'cleaning company. Now, some might require you to have a business license for a '
             'residential cleaning service but not a commercial cleaning service or vice '
             'versa.',
      'title': 'How To Start A Cleaning Business in 2026 (NO BS) Step By Step FREE FULL COURSE '
               '(AJ SIMMONS)',
      'url': 'https://www.youtube.com/watch?v=pqTeTRcPhKg&t=300s',
      'video_id': 'pqTeTRcPhKg'},
     {'author': 'Carolyn Arellano',
      'channel': 'Carolyn Arellano',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:05](https://www.youtube.com/watch?v=IJlyq2UAXqU&t=245s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Now there are different bidding apps that are available for you know commercial '
              'cleaning companies and then there is also the Issa clean times which.',
      'timestamp': 245,
      'timestamp_label': '[00:04:05]',
      'timestamp_seconds': 245,
      'tip': 'Now there are different bidding apps that are available for you know commercial '
             'cleaning companies and then there is also the Issa clean times which.',
      'title': 'How To Bid Commercial Cleaning Jobs (Formula Included) (Carolyn Arellano)',
      'url': 'https://www.youtube.com/watch?v=IJlyq2UAXqU&t=245s',
      'video_id': 'IJlyq2UAXqU'},
     {'author': 'Stronger Built',
      'channel': 'Stronger Built',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:50](https://www.youtube.com/watch?v=EoNW1HDL3PI&t=230s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'No matter how good your cleaning services are. Enforcing these rules like a '
              'hawk is the contract monitoring division or CMD. To prove your outreach to LBE '
              "firms, you've got to score a strict 50point minimum on their evaluation form.",
      'timestamp': 230,
      'timestamp_label': '[00:03:50]',
      'timestamp_seconds': 230,
      'tip': 'No matter how good your cleaning services are. Enforcing these rules like a hawk '
             'is the contract monitoring division or CMD. To prove your outreach to LBE firms, '
             "you've got to score a strict 50point minimum on their evaluation form.",
      'title': 'City and County of San Francisco Janitorial Services RFP (SFGOV-0000011743).- '
               'Stronger Built LLC (Stronger Built)',
      'url': 'https://www.youtube.com/watch?v=EoNW1HDL3PI&t=230s',
      'video_id': 'EoNW1HDL3PI'},
     {'author': 'DJ The Boss',
      'channel': 'DJ The Boss',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:15](https://www.youtube.com/watch?v=cShuZhOvvr4&t=135s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'A commercial cleaning company about eight years ago skilled that past seven '
              "figures I've documented the entire Journey here on YouTube which is pretty.",
      'timestamp': 135,
      'timestamp_label': '[00:02:15]',
      'timestamp_seconds': 135,
      'tip': 'A commercial cleaning company about eight years ago skilled that past seven '
             "figures I've documented the entire Journey here on YouTube which is pretty.",
      'title': 'W2 Employees vs 1099 Contractors for Cleaning Businesses (DJ The Boss)',
      'url': 'https://www.youtube.com/watch?v=cShuZhOvvr4&t=135s',
      'video_id': 'cShuZhOvvr4'},
     {'author': 'Darian Jarrett',
      'channel': 'Darian Jarrett',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:12](https://www.youtube.com/watch?v=_hqGinSApYg&t=372s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Construction cleaning and would love to partner with your company to ensure '
              "your projects are delivered in pristine condition I wanted to know if there's "
              'a.',
      'timestamp': 372,
      'timestamp_label': '[00:06:12]',
      'timestamp_seconds': 372,
      'tip': 'Construction cleaning and would love to partner with your company to ensure your '
             "projects are delivered in pristine condition I wanted to know if there's a.",
      'title': 'How to Get Construction Cleaning Contracts (This REALLY Worked) (Darian '
               'Jarrett)',
      'url': 'https://www.youtube.com/watch?v=_hqGinSApYg&t=372s',
      'video_id': '_hqGinSApYg'},
     {'author': 'Commercial Cleaning CEO',
      'channel': 'Commercial Cleaning CEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:10](https://www.youtube.com/watch?v=gqEvFieh5-k&t=670s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So that's going to look like real estate offices, legal offices, like you've "
              'got a real estate law office, you have general law offices, you have business '
              'law offices, you have all kinds of different lawyers and law groups and firms '
              'in most cities.',
      'timestamp': 670,
      'timestamp_label': '[00:11:10]',
      'timestamp_seconds': 670,
      'tip': "So that's going to look like real estate offices, legal offices, like you've got "
             'a real estate law office, you have general law offices, you have business law '
             'offices, you have all kinds of different lawyers and law groups and firms in '
             'most cities.',
      'title': 'Top 5 HIGH PROFIT Commercial Cleaning Clients (Commercial Cleaning CEO)',
      'url': 'https://www.youtube.com/watch?v=gqEvFieh5-k&t=670s',
      'video_id': 'gqEvFieh5-k'},
     {'author': 'Betco',
      'channel': 'Betco',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:19](https://www.youtube.com/watch?v=wjpbeqDKZnE&t=259s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Isn't exposed it is crucial to clean and disinfect the area with the "
              'appropriate disinfectant cleaner after a cleanup procedure always remove.',
      'timestamp': 259,
      'timestamp_label': '[00:04:19]',
      'timestamp_seconds': 259,
      'tip': "Isn't exposed it is crucial to clean and disinfect the area with the appropriate "
             'disinfectant cleaner after a cleanup procedure always remove.',
      'title': 'OSHA Bloodborne Pathogen (Betco)',
      'url': 'https://www.youtube.com/watch?v=wjpbeqDKZnE&t=259s',
      'video_id': 'wjpbeqDKZnE'},
     {'author': 'Squared Compass',
      'channel': 'Squared Compass',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:55](https://www.youtube.com/watch?v=Hoy7bWdKYOA&t=55s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'If your business sells it, builds it, supports it, or maintains it… there is '
              'probably a government agency that buys it. But because it’s taxpayer money, the '
              'process has structure—rules, competition, documentation, and oversight.',
      'timestamp': 55,
      'timestamp_label': '[00:00:55]',
      'timestamp_seconds': 55,
      'tip': 'If your business sells it, builds it, supports it, or maintains it… there is '
             'probably a government agency that buys it. But because it’s taxpayer money, the '
             'process has structure—rules, competition, documentation, and oversight.',
      'title': 'Government Contracting Decoded: From Basics to Bidding (Squared Compass)',
      'url': 'https://www.youtube.com/watch?v=Hoy7bWdKYOA&t=55s',
      'video_id': 'Hoy7bWdKYOA'},
     {'author': 'Commercial Cleaning Blueprint',
      'channel': 'Commercial Cleaning Blueprint',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:58](https://www.youtube.com/watch?v=rFUVTv2YEQU&t=418s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Daniel wow wow just kidding she probably hung up on accident they probably '
              "let's call her back let's do it thank you for calling Explorer if you are "
              "looking to schedule a visit or I don't like to sit on hold guys cuz I need to "
              'make my time.',
      'timestamp': 418,
      'timestamp_label': '[00:06:58]',
      'timestamp_seconds': 418,
      'tip': "Daniel wow wow just kidding she probably hung up on accident they probably let's "
             "call her back let's do it thank you for calling Explorer if you are looking to "
             "schedule a visit or I don't like to sit on hold guys cuz I need to make my time.",
      'title': 'LIVE COLD CALLS - COMMERCIAL CLEANING (Commercial Cleaning Blueprint)',
      'url': 'https://www.youtube.com/watch?v=rFUVTv2YEQU&t=418s',
      'video_id': 'rFUVTv2YEQU'},
     {'author': 'That Clinical Instructor',
      'channel': 'That Clinical Instructor',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:20:12](https://www.youtube.com/watch?v=CzGiV83CMyU&t=1212s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Your facility has personal protective equipment available for you in your work '
              'area. If you are unsure of the location of a particular item, ask your '
              'supervisor.',
      'timestamp': 1212,
      'timestamp_label': '[00:20:12]',
      'timestamp_seconds': 1212,
      'tip': 'Your facility has personal protective equipment available for you in your work '
             'area. If you are unsure of the location of a particular item, ask your '
             'supervisor.',
      'title': 'Bloodborne Pathogens in Healthcare Facilities Training Video (That Clinical '
               'Instructor)',
      'url': 'https://www.youtube.com/watch?v=CzGiV83CMyU&t=1212s',
      'video_id': 'CzGiV83CMyU'},
     {'author': 'The.Mad.Forensic.Scientist',
      'channel': 'The.Mad.Forensic.Scientist',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=PzH0BFleLzU&t=15s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Any other lectures and now enjoy this presentation budy I hope you're excited "
              'for a quick and dirty overview of Osha bloodborne.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "Any other lectures and now enjoy this presentation budy I hope you're excited "
             'for a quick and dirty overview of Osha bloodborne.',
      'title': 'OSHA Bloodborne Pathogens Training mini session (The.Mad.Forensic.Scientist)',
      'url': 'https://www.youtube.com/watch?v=PzH0BFleLzU&t=15s',
      'video_id': 'PzH0BFleLzU'},
     {'author': 'BICO Legal and Compliance Consulting, LLC',
      'channel': 'BICO Legal and Compliance Consulting, LLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:59](https://www.youtube.com/watch?v=xljn9o0tX_E&t=179s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Contractor status and finally consult with an employment lawyer if your '
              'employer is unwilling to address your concerns seek legal advice from an '
              'employment attorney who can assess your situation and advise on the best course '
              'of action.',
      'timestamp': 179,
      'timestamp_label': '[00:02:59]',
      'timestamp_seconds': 179,
      'tip': 'Contractor status and finally consult with an employment lawyer if your employer '
             'is unwilling to address your concerns seek legal advice from an employment '
             'attorney who can assess your situation and advise on the best course of action.',
      'title': 'Case Study: Misclassification of Employees as Independent Contractors (BICO '
               'Legal and Compliance Consulting, LLC)',
      'url': 'https://www.youtube.com/watch?v=xljn9o0tX_E&t=179s',
      'video_id': 'xljn9o0tX_E'},
     {'author': 'OctoClean Media',
      'channel': 'OctoClean Media',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:23:42](https://www.youtube.com/watch?v=zAGjNnpTUcY&t=1422s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "High as 75 in California we're doing that I me it depends on the state you're "
              'in expenses are different in different states cost for goods can be different '
              'in different states um but you know this is something that is at least a '
              'Baseline.',
      'timestamp': 1422,
      'timestamp_label': '[00:23:42]',
      'timestamp_seconds': 1422,
      'tip': "High as 75 in California we're doing that I me it depends on the state you're in "
             'expenses are different in different states cost for goods can be different in '
             'different states um but you know this is something that is at least a Baseline.',
      'title': 'How To Bid Commercial Cleaning Jobs Like A Pro: Live at ISSA 2024! '
               '@ISSAMediaTV (OctoClean Media)',
      'url': 'https://www.youtube.com/watch?v=zAGjNnpTUcY&t=1422s',
      'video_id': 'zAGjNnpTUcY'},
     {'author': 'ONLY MAIDS PODCAST',
      'channel': 'ONLY MAIDS PODCAST',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:24:18](https://www.youtube.com/watch?v=aQj7G__L-iE&t=1458s)',
      'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                   'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                   'and supervisor pods (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "That's my commercial cleaning company um I'm located in uh DC Maryland and "
              'Virginia area I also um have a Clean Ops guide which is a uh a a a I guess a '
              'commercial cleaning resource for uh for new and experienced uh commercial '
              'cleaning.',
      'timestamp': 1458,
      'timestamp_label': '[00:24:18]',
      'timestamp_seconds': 1458,
      'tip': "That's my commercial cleaning company um I'm located in uh DC Maryland and "
             'Virginia area I also um have a Clean Ops guide which is a uh a a a I guess a '
             'commercial cleaning resource for uh for new and experienced uh commercial '
             'cleaning.',
      'title': 'Hot Seat | Commercial Cleaning Crash Course: Get the Walkthrough, Price the '
               'Job & Win the Account (ONLY MAIDS PODCAST)',
      'url': 'https://www.youtube.com/watch?v=aQj7G__L-iE&t=1458s',
      'video_id': 'aQj7G__L-iE'}],
 10: [{'author': 'Win Driggins',
       'channel': 'Win Driggins',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:53](https://www.youtube.com/watch?v=83XHXw79m3E&t=413s)',
       'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                    'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                    'and supervisor pods (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'The hidden business is organizing higher-margin specialty services around the '
               'regular cleaning contract. This slide shows the commercial carpet cleaner '
               'replacing and servicing the business entry rugs.',
       'timestamp': 413,
       'timestamp_label': '[00:06:53]',
       'timestamp_seconds': 413,
       'tip': 'The hidden business is organizing higher-margin specialty services around the '
              'regular cleaning contract. This slide shows the commercial carpet cleaner '
              'replacing and servicing the business entry rugs.',
       'title': 'Commercial Cleaning Contracts, Janitorial Franchises Video Presentation With '
                'CC (Win Driggins)',
       'url': 'https://www.youtube.com/watch?v=83XHXw79m3E&t=413s',
       'video_id': '83XHXw79m3E'},
      {'author': 'Commercial Cleaning CEO',
       'channel': 'Commercial Cleaning CEO',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:10:41](https://www.youtube.com/watch?v=IMbK5m7qbY0&t=641s)',
       'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                    'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                    'and supervisor pods (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "So, this carpet cleaning speed right here, that's just what a good average is. "
               'You can clean about 7,000 square feet per hour just doing vacuuming and '
               'cleaning carpet, right? Uh hard floor, this is sweeping and mopping.',
       'timestamp': 641,
       'timestamp_label': '[00:10:41]',
       'timestamp_seconds': 641,
       'tip': "So, this carpet cleaning speed right here, that's just what a good average is. "
              'You can clean about 7,000 square feet per hour just doing vacuuming and '
              'cleaning carpet, right? Uh hard floor, this is sweeping and mopping.',
       'title': 'How To Profitably Bid Commercial Cleaning Jobs | CALCULATOR (Commercial '
                'Cleaning CEO)',
       'url': 'https://www.youtube.com/watch?v=IMbK5m7qbY0&t=641s',
       'video_id': 'IMbK5m7qbY0'},
      {'author': 'BizAlmighty',
       'channel': 'BizAlmighty',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:03](https://www.youtube.com/watch?v=f0CmEkWm_a0&t=303s)',
       'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                    'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                    'and supervisor pods (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "I'm going to hit this refresh dashboard. And that will give me the 2026 data "
               'all in these charts perfectly updated so that you can keep on top of your '
               'business performance. That wraps up the walkthrough of the um cleaning '
               'business calculator, the basic edition.',
       'timestamp': 303,
       'timestamp_label': '[00:05:03]',
       'timestamp_seconds': 303,
       'tip': "I'm going to hit this refresh dashboard. And that will give me the 2026 data "
              'all in these charts perfectly updated so that you can keep on top of your '
              'business performance. That wraps up the walkthrough of the um cleaning business '
              'calculator, the basic edition.',
       'title': 'Cleaning Business Calculator   Basic   Walkthrough (BizAlmighty)',
       'url': 'https://www.youtube.com/watch?v=f0CmEkWm_a0&t=303s',
       'video_id': 'f0CmEkWm_a0'},
      {'author': '7 Figure Cleaning',
       'channel': '7 Figure Cleaning',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:59](https://www.youtube.com/watch?v=1_z-Kgj0GYM&t=239s)',
       'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                    'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                    'and supervisor pods (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'re accurate every time, go to my website. I have a free bidding calculator on "
               'there and it breaks down everything that you need to know to keep you safe, '
               "keep you winning, and keep you profitable on every account. That's my gift to "
               'you guys.',
       'timestamp': 239,
       'timestamp_label': '[00:03:59]',
       'timestamp_seconds': 239,
       'tip': "'re accurate every time, go to my website. I have a free bidding calculator on "
              'there and it breaks down everything that you need to know to keep you safe, '
              "keep you winning, and keep you profitable on every account. That's my gift to "
              'you guys.',
       'title': 'How to Price Commercial Cleaning Contracts to Win and Profit (3 Ways) (7 '
                'Figure Cleaning)',
       'url': 'https://www.youtube.com/watch?v=1_z-Kgj0GYM&t=239s',
       'video_id': '1_z-Kgj0GYM'},
      {'author': 'Mike Mak',
       'channel': 'Mike Mak',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:27](https://www.youtube.com/watch?v=kbRmM3sctgA&t=447s)',
       'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                    'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                    'and supervisor pods (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "See, office cleaning gives you the ability to scale because it's built around "
               'seven $5,000 per month contracts, recurring contracts. And that is so much '
               "easier to automate. And isn't that the part that's crazy?",
       'timestamp': 447,
       'timestamp_label': '[00:07:27]',
       'timestamp_seconds': 447,
       'tip': "See, office cleaning gives you the ability to scale because it's built around "
              'seven $5,000 per month contracts, recurring contracts. And that is so much '
              "easier to automate. And isn't that the part that's crazy?",
       'title': 'Starting A "ReMOtE CleAnINg" Business Is BS. Do This Instead. (Mike Mak)',
       'url': 'https://www.youtube.com/watch?v=kbRmM3sctgA&t=447s',
       'video_id': 'kbRmM3sctgA'},
      {'author': 'AJ SIMMONS',
       'channel': 'AJ SIMMONS',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:16:25](https://www.youtube.com/watch?v=ZDdd0TDbbFo&t=985s)',
       'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                    'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                    'and supervisor pods (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'But do not get both because the in-house lead generation course is inside of '
               "the automation program. All right, so anyway, that's what I got for y'all. I'm "
               'AJ Simmons, founder of the Clean Business Network.',
       'timestamp': 985,
       'timestamp_label': '[00:16:25]',
       'timestamp_seconds': 985,
       'tip': 'But do not get both because the in-house lead generation course is inside of '
              "the automation program. All right, so anyway, that's what I got for y'all. I'm "
              'AJ Simmons, founder of the Clean Business Network.',
       'title': 'How To Get Commercial Cleaning Contracts (SIMPLE ANSWER) (AJ SIMMONS)',
       'url': 'https://www.youtube.com/watch?v=ZDdd0TDbbFo&t=985s',
       'video_id': 'ZDdd0TDbbFo'},
      {'author': 'GovKidMethod',
       'channel': 'GovKidMethod',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:45:39](https://www.youtube.com/watch?v=dOj6rxt15uE&t=2739s)',
       'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                    'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                    'and supervisor pods (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'You know, what you can do is just employee number one. Employee number one '
               'served performed for the LA Parks summer season cleaning job and will be '
               'working directly on this contract as proposed.',
       'timestamp': 2739,
       'timestamp_label': '[00:45:39]',
       'timestamp_seconds': 2739,
       'tip': 'You know, what you can do is just employee number one. Employee number one '
              'served performed for the LA Parks summer season cleaning job and will be '
              'working directly on this contract as proposed.',
       'title': 'Government Bid Proposal Training: Start a Cleaning Business (Janitorial) for '
                'the Government! (GovKidMethod)',
       'url': 'https://www.youtube.com/watch?v=dOj6rxt15uE&t=2739s',
       'video_id': 'dOj6rxt15uE'},
      {'author': 'Constantin Schröck',
       'channel': 'Constantin Schröck',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:42](https://www.youtube.com/watch?v=Q5K2zTuisJc&t=102s)',
       'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                    'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                    'and supervisor pods (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Noise complaints all while keeping the property clean for tenants and owners '
               "right we'll be back in the Baltimore area for some jobs soon mind if a drop.",
       'timestamp': 102,
       'timestamp_label': '[00:01:42]',
       'timestamp_seconds': 102,
       'tip': 'Noise complaints all while keeping the property clean for tenants and owners '
              "right we'll be back in the Baltimore area for some jobs soon mind if a drop.",
       'title': 'How To Get Jobs With Property Managers | Power Washing Lead generation | Cold '
                'Email Campaign (Constantin Schröck)',
       'url': 'https://www.youtube.com/watch?v=Q5K2zTuisJc&t=102s',
       'video_id': 'Q5K2zTuisJc'},
      {'author': 'Sheenapreneur',
       'channel': 'Sheenapreneur',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:19:47](https://www.youtube.com/watch?v=hyUO_-BE-qc&t=1187s)',
       'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                    'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                    'and supervisor pods (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Do you want you know document shredding removal like I said in one of my other '
               'videos like something like that where you can just add more to the cleaning.',
       'timestamp': 1187,
       'timestamp_label': '[00:19:47]',
       'timestamp_seconds': 1187,
       'tip': 'Do you want you know document shredding removal like I said in one of my other '
              'videos like something like that where you can just add more to the cleaning.',
       'title': 'TOP 10 things you need to get started in Janitorial! | Government Contracting '
                '(Sheenapreneur)',
       'url': 'https://www.youtube.com/watch?v=hyUO_-BE-qc&t=1187s',
       'video_id': 'hyUO_-BE-qc'},
      {'author': 'Janitorial Manager',
       'channel': 'Janitorial Manager',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:56](https://www.youtube.com/watch?v=D60Eb-ryFyc&t=176s)',
       'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                    'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                    'and supervisor pods (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Business and so you know we're providing solutions that allow you to to scale "
               'to keep customers to to to keep employees to making sure that you know all '
               'those.',
       'timestamp': 176,
       'timestamp_label': '[00:02:56]',
       'timestamp_seconds': 176,
       'tip': "Business and so you know we're providing solutions that allow you to to scale "
              'to keep customers to to to keep employees to making sure that you know all '
              'those.',
       'title': 'Finalist for the ISSA Innovation Award 2019: Janitorial Manager by Double A '
                'Solutions (Janitorial Manager)',
       'url': 'https://www.youtube.com/watch?v=D60Eb-ryFyc&t=176s',
       'video_id': 'D60Eb-ryFyc'},
      {'author': 'Dylan Marma',
       'channel': 'Dylan Marma',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:55](https://www.youtube.com/watch?v=uJmpWtXEuyg&t=115s)',
       'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                    'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                    'and supervisor pods (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Are set up we generally set up separate bank accounts for each property and '
               'actually we have multiple bank accounts for each property we have one for our.',
       'timestamp': 115,
       'timestamp_label': '[00:01:55]',
       'timestamp_seconds': 115,
       'tip': 'Are set up we generally set up separate bank accounts for each property and '
              'actually we have multiple bank accounts for each property we have one for our.',
       'title': 'The Ultimate 90-day Property Onboarding Checklist in 2023 | RV Parks | '
                'Requity, Dylan Marma (Dylan Marma)',
       'url': 'https://www.youtube.com/watch?v=uJmpWtXEuyg&t=115s',
       'video_id': 'uJmpWtXEuyg'},
      {'author': 'Commercial Cleaning CEO',
       'channel': 'Commercial Cleaning CEO',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:22:02](https://www.youtube.com/watch?v=o6xwPfuhTI4&t=1322s)',
       'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                    'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                    'and supervisor pods (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Click the link or continue watching this next video, and I hope to meet you '
               'soon and to help you get on the path to a seven-figure commercial cleaning '
               'business in five-hour weeks.',
       'timestamp': 1322,
       'timestamp_label': '[00:22:02]',
       'timestamp_seconds': 1322,
       'tip': 'Click the link or continue watching this next video, and I hope to meet you '
              'soon and to help you get on the path to a seven-figure commercial cleaning '
              'business in five-hour weeks.',
       'title': 'How to Get Commercial Cleaning Contracts Starting From Zero (Commercial '
                'Cleaning CEO)',
       'url': 'https://www.youtube.com/watch?v=o6xwPfuhTI4&t=1322s',
       'video_id': 'o6xwPfuhTI4'},
      {'author': 'victoria menifee',
       'channel': 'victoria menifee',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:02](https://www.youtube.com/watch?v=JJ1zFR0l3vE&t=302s)',
       'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                    'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                    'and supervisor pods (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Their spaces limited click in the description in order to sign up love to see '
               'you there until the next video be safe and take care bye bye.',
       'timestamp': 302,
       'timestamp_label': '[00:05:02]',
       'timestamp_seconds': 302,
       'tip': 'Their spaces limited click in the description in order to sign up love to see '
              'you there until the next video be safe and take care bye bye.',
       'title': 'HOW TO WIN COMMERCIAL CLEANING CONTRACTS WITH MAJOR BANKS (victoria menifee)',
       'url': 'https://www.youtube.com/watch?v=JJ1zFR0l3vE&t=302s',
       'video_id': 'JJ1zFR0l3vE'},
      {'author': 'OctoClean Media',
       'channel': 'OctoClean Media',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:46](https://www.youtube.com/watch?v=Z8hsIGjmi_c&t=166s)',
       'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                    'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                    'and supervisor pods (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "All right I'm going to take these gloves off because I don't want to grab the "
               "clean bottle with possible contamination on my hands so what I'm going to do "
               "from the inside clean thumb from the inside and I'm putting these in my bag "
               "I'll grab another set of gloves.",
       'timestamp': 166,
       'timestamp_label': '[00:02:46]',
       'timestamp_seconds': 166,
       'tip': "All right I'm going to take these gloves off because I don't want to grab the "
              "clean bottle with possible contamination on my hands so what I'm going to do "
              "from the inside clean thumb from the inside and I'm putting these in my bag "
              "I'll grab another set of gloves.",
       'title': 'Bloodborne Pathogen Cleanup and Decontamination | SAFELY Cleanup Blood! '
                '(OctoClean Media)',
       'url': 'https://www.youtube.com/watch?v=Z8hsIGjmi_c&t=166s',
       'video_id': 'Z8hsIGjmi_c'},
      {'author': 'Bid & Profit Lab',
       'channel': 'Bid & Profit Lab',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:26](https://www.youtube.com/watch?v=T-l3Df3Iino&t=266s)',
       'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                    'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                    'and supervisor pods (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'The repeatable workflow is scope, labor, full cost, target margin, then a '
               'stress test. If you prefer a ready made spreadsheet for your bidding '
               'calculations, our Commercial Cleaning Bid and Margin System is linked in the '
               'description.',
       'timestamp': 266,
       'timestamp_label': '[00:04:26]',
       'timestamp_seconds': 266,
       'tip': 'The repeatable workflow is scope, labor, full cost, target margin, then a '
              'stress test. If you prefer a ready made spreadsheet for your bidding '
              'calculations, our Commercial Cleaning Bid and Margin System is linked in the '
              'description.',
       'title': 'How to Bid a Commercial Cleaning Contract: 20,000 Sq Ft Example. (Bid & '
                'Profit Lab)',
       'url': 'https://www.youtube.com/watch?v=T-l3Df3Iino&t=266s',
       'video_id': 'T-l3Df3Iino'}],
 11: [{'author': 'Modern Field Service',
       'channel': 'Modern Field Service',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:37](https://www.youtube.com/watch?v=Y00vfNH19Q4&t=277s)',
       'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                    'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                    'and supervisor pods (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Connect Team and add a simple invoicing tool. Clients heavy janitorial with '
               "inspections at the center, Janitorial Manager, if you're okay with quote-based "
               'pricing. Established janitorial company that wants the industry standard, '
               'Swept is a safe, solid pick.',
       'timestamp': 277,
       'timestamp_label': '[00:04:37]',
       'timestamp_seconds': 277,
       'tip': 'Connect Team and add a simple invoicing tool. Clients heavy janitorial with '
              "inspections at the center, Janitorial Manager, if you're okay with quote-based "
              'pricing. Established janitorial company that wants the industry standard, Swept '
              'is a safe, solid pick.',
       'title': 'Best Janitorial & Commercial Cleaning Software 2026 (Modern Field Service)',
       'url': 'https://www.youtube.com/watch?v=Y00vfNH19Q4&t=277s',
       'video_id': 'Y00vfNH19Q4'},
      {'author': 'Jon Margalit',
       'channel': 'Jon Margalit',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:57](https://www.youtube.com/watch?v=8gbn-TCd4l4&t=297s)',
       'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                    'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                    'and supervisor pods (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "If you're trying to build a cleaning business and you're stuck on that W2 "
               "versus 1099 debate, here's the truth. There's a way to do it right. You don't "
               "need to hire W2 employees. You don't need to hand out vacuums and micromanage "
               'people.',
       'timestamp': 297,
       'timestamp_label': '[00:04:57]',
       'timestamp_seconds': 297,
       'tip': "If you're trying to build a cleaning business and you're stuck on that W2 "
              "versus 1099 debate, here's the truth. There's a way to do it right. You don't "
              "need to hire W2 employees. You don't need to hand out vacuums and micromanage "
              'people.',
       'title': 'W2 vs 1099: How I Built a Remote Cleaning Team Without Payroll Headaches (Jon '
                'Margalit)',
       'url': 'https://www.youtube.com/watch?v=8gbn-TCd4l4&t=297s',
       'video_id': '8gbn-TCd4l4'},
      {'author': 'Bryan Gutowsky | Michigan Insurance',
       'channel': 'Bryan Gutowsky | Michigan Insurance',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:13](https://www.youtube.com/watch?v=irbQWL_bLuA&t=73s)',
       'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                    'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                    'and supervisor pods (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'s property damage related to your work. If you're a contractor or a "
               "construction company, and you're doing work on a property, and maybe because "
               'of your operations, because of of the work you were doing, the neighboring '
               'property gets damaged.',
       'timestamp': 73,
       'timestamp_label': '[00:01:13]',
       'timestamp_seconds': 73,
       'tip': "'s property damage related to your work. If you're a contractor or a "
              "construction company, and you're doing work on a property, and maybe because of "
              'your operations, because of of the work you were doing, the neighboring '
              'property gets damaged.',
       'title': 'General Liability vs Workers Comp Insurance | What’s The Difference? (Bryan '
                'Gutowsky | Michigan Insurance)',
       'url': 'https://www.youtube.com/watch?v=irbQWL_bLuA&t=73s',
       'video_id': 'irbQWL_bLuA'},
      {'author': 'Commercial Cleaning CEO',
       'channel': 'Commercial Cleaning CEO',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:07](https://www.youtube.com/watch?v=z_tdT6I7K7U&t=307s)',
       'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                    'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                    'and supervisor pods (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'And I can say within our area where we typically operate is we look for head '
               "of school. So don't be calling these or reaching out to these or interacting "
               'with private schools and asking for a principal or a director of some kind. '
               'You want head of school or business manager.',
       'timestamp': 307,
       'timestamp_label': '[00:05:07]',
       'timestamp_seconds': 307,
       'tip': 'And I can say within our area where we typically operate is we look for head of '
              "school. So don't be calling these or reaching out to these or interacting with "
              'private schools and asking for a principal or a director of some kind. You want '
              'head of school or business manager.',
       'title': 'How to Win Commercial Cleaning Contracts With Schools (Commercial Cleaning '
                'CEO)',
       'url': 'https://www.youtube.com/watch?v=z_tdT6I7K7U&t=307s',
       'video_id': 'z_tdT6I7K7U'},
      {'author': 'UpFlip',
       'channel': 'UpFlip',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:19:07](https://www.youtube.com/watch?v=j3l2-xKJKb8&t=1147s)',
       'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                    'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                    'and supervisor pods (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "What's the most rewarding part of owning your own business? Well, leaving a "
               'legacy, right? So my son does work for me. So when I came back from pool '
               'school, he started cleaning pools. And right now he is the general manager of '
               'my area.',
       'timestamp': 1147,
       'timestamp_label': '[00:19:07]',
       'timestamp_seconds': 1147,
       'tip': "What's the most rewarding part of owning your own business? Well, leaving a "
              'legacy, right? So my son does work for me. So when I came back from pool '
              'school, he started cleaning pools. And right now he is the general manager of '
              'my area.',
       'title': 'Most Underrated Service Business?! (Makes $851K/Year) (UpFlip)',
       'url': 'https://www.youtube.com/watch?v=j3l2-xKJKb8&t=1147s',
       'video_id': 'j3l2-xKJKb8'},
      {'author': 'The Janitorial Store',
       'channel': 'The Janitorial Store',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:41](https://www.youtube.com/watch?v=EL4NN_-rX7o&t=161s)',
       'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                    'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                    'and supervisor pods (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'We got to know where those alarm codes are so we can tell our team uh when '
               "we're doing our initial training. So, that way we can go right to alarm, "
               'disarm it, and not worry about any false alarms. And the same thing is true as '
               "if you're cleaning a commercial building.",
       'timestamp': 161,
       'timestamp_label': '[00:02:41]',
       'timestamp_seconds': 161,
       'tip': 'We got to know where those alarm codes are so we can tell our team uh when '
              "we're doing our initial training. So, that way we can go right to alarm, disarm "
              'it, and not worry about any false alarms. And the same thing is true as if '
              "you're cleaning a commercial building.",
       'title': 'Commercial Cleaning Company Onboarding Checklist (The Janitorial Store)',
       'url': 'https://www.youtube.com/watch?v=EL4NN_-rX7o&t=161s',
       'video_id': 'EL4NN_-rX7o'},
      {'author': 'Janitorial Manager',
       'channel': 'Janitorial Manager',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:48](https://www.youtube.com/watch?v=qZwFYeU_0Qs&t=168s)',
       'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                    'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                    'and supervisor pods (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Cares steven also has a better idea advies inventory niet en zus business in '
               'crisis steven en de kroon niet langer hoop voor succes bij use the general '
               'manager or glory and bring to a en de consumable calculator bij het succes '
               '[Muziek].',
       'timestamp': 168,
       'timestamp_label': '[00:02:48]',
       'timestamp_seconds': 168,
       'tip': 'Cares steven also has a better idea advies inventory niet en zus business in '
              'crisis steven en de kroon niet langer hoop voor succes bij use the general '
              'manager or glory and bring to a en de consumable calculator bij het succes '
              '[Muziek].',
       'title': 'ISSA Work Loading & Bidding Tool and Consumable Calculator - Janitorial '
                'Manager (Janitorial Manager)',
       'url': 'https://www.youtube.com/watch?v=qZwFYeU_0Qs&t=168s',
       'video_id': 'qZwFYeU_0Qs'},
      {'author': 'Kadz Money',
       'channel': 'Kadz Money',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:39](https://www.youtube.com/watch?v=dEkotRT-f90&t=159s)',
       'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                    'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                    'and supervisor pods (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Cleaning businesses it's in demand customers will come to you very rarely you "
               "can advertise online and people will start calling you and you'll have enough.",
       'timestamp': 159,
       'timestamp_label': '[00:02:39]',
       'timestamp_seconds': 159,
       'tip': "Cleaning businesses it's in demand customers will come to you very rarely you "
              "can advertise online and people will start calling you and you'll have enough.",
       'title': 'How To Start A Cleaning Business In The UK For 2025 | Cleaning Business Plan '
                '(Kadz Money)',
       'url': 'https://www.youtube.com/watch?v=dEkotRT-f90&t=159s',
       'video_id': 'dEkotRT-f90'},
      {'author': 'Runjob Software',
       'channel': 'Runjob Software',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:03](https://www.youtube.com/watch?v=0pkOO_oVhN8&t=123s)',
       'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                    'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                    'and supervisor pods (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "A contractor on the project a lot of people don't understand the calculation "
               "of a bond but there's two basic types of bond that you're going to see in the.",
       'timestamp': 123,
       'timestamp_label': '[00:02:03]',
       'timestamp_seconds': 123,
       'tip': "A contractor on the project a lot of people don't understand the calculation of "
              "a bond but there's two basic types of bond that you're going to see in the.",
       'title': 'Calculation of Workers’ Compensation, General Liability (GL) & Bond in your '
                'Estimates (Runjob Software)',
       'url': 'https://www.youtube.com/watch?v=0pkOO_oVhN8&t=123s',
       'video_id': '0pkOO_oVhN8'},
      {'author': 'Darian Jarrett',
       'channel': 'Darian Jarrett',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:33](https://www.youtube.com/watch?v=6wtiLyP6-zU&t=93s)',
       'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                    'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                    'and supervisor pods (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Following me for any time you know I love Mr Clean uh any type of Mr Clean but '
               'the multi multi-surface this is a fabreeze fragrance right here we also.',
       'timestamp': 93,
       'timestamp_label': '[00:01:33]',
       'timestamp_seconds': 93,
       'tip': 'Following me for any time you know I love Mr Clean uh any type of Mr Clean but '
              'the multi multi-surface this is a fabreeze fragrance right here we also.',
       'title': 'Everything You NEED for Post-Construction Cleaning (Complete Supply '
                'Checklist) (Darian Jarrett)',
       'url': 'https://www.youtube.com/watch?v=6wtiLyP6-zU&t=93s',
       'video_id': '6wtiLyP6-zU'},
      {'author': 'The Profitable Cleaner',
       'channel': 'The Profitable Cleaner',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:42](https://www.youtube.com/watch?v=phVhAxusau8&t=102s)',
       'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                    'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                    'and supervisor pods (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Associations and other real estate and that starts building the relationship '
               'because if you care enough to understand our business we already know that you '
               "have some element of trust sure and that's huge.",
       'timestamp': 102,
       'timestamp_label': '[00:01:42]',
       'timestamp_seconds': 102,
       'tip': 'Associations and other real estate and that starts building the relationship '
              'because if you care enough to understand our business we already know that you '
              "have some element of trust sure and that's huge.",
       'title': 'Best Ways To Reach and Sell To A Property Manager? (The Profitable Cleaner)',
       'url': 'https://www.youtube.com/watch?v=phVhAxusau8&t=102s',
       'video_id': 'phVhAxusau8'},
      {'author': 'Janitorial Manager',
       'channel': 'Janitorial Manager',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:01](https://www.youtube.com/watch?v=LFXytjdaxWA&t=121s)',
       'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                    'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                    'and supervisor pods (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Management can approve guarantee precision and accountability in your payroll '
               'while establishing employees satisfaction in keeping your customers happy '
               'elevate your operations efficiency today with janitorial manager timekeeping '
               'feature.',
       'timestamp': 121,
       'timestamp_label': '[00:02:01]',
       'timestamp_seconds': 121,
       'tip': 'Management can approve guarantee precision and accountability in your payroll '
              'while establishing employees satisfaction in keeping your customers happy '
              'elevate your operations efficiency today with janitorial manager timekeeping '
              'feature.',
       'title': "Janitorial Manager's Timekeeping Feature (Janitorial Manager)",
       'url': 'https://www.youtube.com/watch?v=LFXytjdaxWA&t=121s',
       'video_id': 'LFXytjdaxWA'},
      {'author': 'AJ SIMMONS',
       'channel': 'AJ SIMMONS',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=mk-8avM72Ms&t=15s)',
       'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                    'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                    'and supervisor pods (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "And today I'm just going to share with you the equipment and supplies that "
               "you're going to need to start your cleaning company and as you can look.",
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': "And today I'm just going to share with you the equipment and supplies that "
              "you're going to need to start your cleaning company and as you can look.",
       'title': 'Cleaning Supplies Needed For Cleaning Business (AJ SIMMONS)',
       'url': 'https://www.youtube.com/watch?v=mk-8avM72Ms&t=15s',
       'video_id': 'mk-8avM72Ms'},
      {'author': 'Commercial Cleaning CEO',
       'channel': 'Commercial Cleaning CEO',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:20](https://www.youtube.com/watch?v=8jCIs_UmQ1Q&t=20s)',
       'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                    'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                    'and supervisor pods (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'t need to be intimidated if a large factory calls you or if you want to go "
               'pursue them to grow your business even faster. Because simply put, if you '
               "don't know how to quote these, then you're limited in how much your business "
               'can grow in the area that you operate.',
       'timestamp': 20,
       'timestamp_label': '[00:00:20]',
       'timestamp_seconds': 20,
       'tip': "'t need to be intimidated if a large factory calls you or if you want to go "
              "pursue them to grow your business even faster. Because simply put, if you don't "
              "know how to quote these, then you're limited in how much your business can grow "
              'in the area that you operate.',
       'title': 'How To Quote Industrial Cleaning Jobs (BIG Money Contracts!) (Commercial '
                'Cleaning CEO)',
       'url': 'https://www.youtube.com/watch?v=8jCIs_UmQ1Q&t=20s',
       'video_id': '8jCIs_UmQ1Q'},
      {'author': 'Business From Zero',
       'channel': 'Business From Zero',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:24](https://www.youtube.com/watch?v=fvJFWetfuFA&t=444s)',
       'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                    'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                    'and supervisor pods (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Part-time W-2 crew payroll and employer FICA taxes across three accounts, '
               "$1,130. Monthly commercial general liability, surety bond, and workers' comp "
               'insurance, $245. Wholesale commercial disinfectants, trash liners, and restock '
               'consumables, $380.',
       'timestamp': 444,
       'timestamp_label': '[00:07:24]',
       'timestamp_seconds': 444,
       'tip': 'Part-time W-2 crew payroll and employer FICA taxes across three accounts, '
              "$1,130. Monthly commercial general liability, surety bond, and workers' comp "
              'insurance, $245. Wholesale commercial disinfectants, trash liners, and restock '
              'consumables, $380.',
       'title': 'How to Start a Commercial Cleaning Business for $4,200 (Business From Zero)',
       'url': 'https://www.youtube.com/watch?v=fvJFWetfuFA&t=444s',
       'video_id': 'fvJFWetfuFA'}],
 12: [{'author': 'AJ SIMMONS',
       'channel': 'AJ SIMMONS',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:16:58](https://www.youtube.com/watch?v=VrlDbQP4iQI&t=1018s)',
       'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                    'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                    'and supervisor pods (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Are you looking to start your own cleaning company? Or maybe you started your '
               'cleaning company, but you just need a support group, some mentorship, some '
               "guidance, hell, a bidding calculator just to help you know if you're pricing "
               'the job correctly.',
       'timestamp': 1018,
       'timestamp_label': '[00:16:58]',
       'timestamp_seconds': 1018,
       'tip': 'Are you looking to start your own cleaning company? Or maybe you started your '
              'cleaning company, but you just need a support group, some mentorship, some '
              "guidance, hell, a bidding calculator just to help you know if you're pricing "
              'the job correctly.',
       'title': 'How To Start A Commercial Cleaning Business Today Under $1000 and Get '
                'Customers FAST! (AJ SIMMONS)',
       'url': 'https://www.youtube.com/watch?v=VrlDbQP4iQI&t=1018s',
       'video_id': 'VrlDbQP4iQI'},
      {'author': "Bea's Business",
       'channel': "Bea's Business",
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:52](https://www.youtube.com/watch?v=3vr4bkvaByo&t=52s)',
       'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                    'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                    'and supervisor pods (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'And as you can see here, someone already asked that question and it is 21. '
               'Now, I actually reached out to the director of this contract and he broke down '
               'what that 2158 a month entails. So that is one person working 5 days a week, 8 '
               'to 12 hours per day.',
       'timestamp': 52,
       'timestamp_label': '[00:00:52]',
       'timestamp_seconds': 52,
       'tip': 'And as you can see here, someone already asked that question and it is 21. Now, '
              'I actually reached out to the director of this contract and he broke down what '
              'that 2158 a month entails. So that is one person working 5 days a week, 8 to 12 '
              'hours per day.',
       'title': "Step-by-Step: Fill Out a Government Cleaning Contract with Me! (Bea's "
                'Business)',
       'url': 'https://www.youtube.com/watch?v=3vr4bkvaByo&t=52s',
       'video_id': '3vr4bkvaByo'},
      {'author': 'The Janitorial Store',
       'channel': 'The Janitorial Store',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:43](https://www.youtube.com/watch?v=rGpgBfBHKg0&t=43s)',
       'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                    'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                    'and supervisor pods (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'s say you have an account that is 12,500 ft and it takes 3. 25 hours to clean "
               'it your production rate is 38461 15 ft per hour if that account is cleaned 3 '
               'days per week you would have 20 4225 hours per month you would then multiply '
               '42.',
       'timestamp': 43,
       'timestamp_label': '[00:00:43]',
       'timestamp_seconds': 43,
       'tip': "'s say you have an account that is 12,500 ft and it takes 3. 25 hours to clean "
              'it your production rate is 38461 15 ft per hour if that account is cleaned 3 '
              'days per week you would have 20 4225 hours per month you would then multiply '
              '42.',
       'title': 'How to Price an Account Using The Production Rate Bidding Method (The '
                'Janitorial Store)',
       'url': 'https://www.youtube.com/watch?v=rGpgBfBHKg0&t=43s',
       'video_id': 'rGpgBfBHKg0'},
      {'author': 'Clean For A Dream',
       'channel': 'Clean For A Dream',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:36:12](https://www.youtube.com/watch?v=fs86ZhCBfJ8&t=2172s)',
       'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                    'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                    'and supervisor pods (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'People all at a time in order to have you know a multi-million dollar cleaning '
               'business you need to have at least 45 people working four hours a day seven '
               'days a week.',
       'timestamp': 2172,
       'timestamp_label': '[00:36:12]',
       'timestamp_seconds': 2172,
       'tip': 'People all at a time in order to have you know a multi-million dollar cleaning '
              'business you need to have at least 45 people working four hours a day seven '
              'days a week.',
       'title': 'The 5 Things You Must Know Before You Buy a Janitorial Franchise! (Clean For '
                'A Dream)',
       'url': 'https://www.youtube.com/watch?v=fs86ZhCBfJ8&t=2172s',
       'video_id': 'fs86ZhCBfJ8'},
      {'author': 'CleanGuru',
       'channel': 'CleanGuru',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:38](https://www.youtube.com/watch?v=UdGEmUdlNJs&t=98s)',
       'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                    'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                    'and supervisor pods (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Rooms lunchroom Lobby tra all the kind of things standard every day but then '
               'detail cleaning scheduled in there during the week or during the month but.',
       'timestamp': 98,
       'timestamp_label': '[00:01:38]',
       'timestamp_seconds': 98,
       'tip': 'Rooms lunchroom Lobby tra all the kind of things standard every day but then '
              'detail cleaning scheduled in there during the week or during the month but.',
       'title': 'What’s the Going Rate Per Sq. Ft. for Bidding Commercial Office Cleaning '
                'Jobs: Cleaning Business Tip (CleanGuru)',
       'url': 'https://www.youtube.com/watch?v=UdGEmUdlNJs&t=98s',
       'video_id': 'UdGEmUdlNJs'},
      {'author': 'UpFlip',
       'channel': 'UpFlip',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:23:28](https://www.youtube.com/watch?v=d4Iip7BHXwg&t=1408s)',
       'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                    'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                    'and supervisor pods (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Chris] Learning your numbers, learn how to delegate and start investing in '
               'marketing. If you had to start a new business in a different field, what would '
               'it be and why? Chris] I would say carpet cleaning.',
       'timestamp': 1408,
       'timestamp_label': '[00:23:28]',
       'timestamp_seconds': 1408,
       'tip': 'Chris] Learning your numbers, learn how to delegate and start investing in '
              'marketing. If you had to start a new business in a different field, what would '
              'it be and why? Chris] I would say carpet cleaning.',
       'title': 'Starting a $120K/Month Cleaning Business From Scratch (UpFlip)',
       'url': 'https://www.youtube.com/watch?v=d4Iip7BHXwg&t=1408s',
       'video_id': 'd4Iip7BHXwg'},
      {'author': 'Grow My Cleaning Company',
       'channel': 'Grow My Cleaning Company',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:40](https://www.youtube.com/watch?v=PcnIuILxXOw&t=340s)',
       'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                    'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                    'and supervisor pods (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'First and foremost, we the flow that we coach is weekly meetings, monthly '
               'parties, quarterly reviews. So, weekly meetings about an hour a week, about 2 '
               'hours a month, and half day to a day a quarter.',
       'timestamp': 340,
       'timestamp_label': '[00:05:40]',
       'timestamp_seconds': 340,
       'tip': 'First and foremost, we the flow that we coach is weekly meetings, monthly '
              'parties, quarterly reviews. So, weekly meetings about an hour a week, about 2 '
              'hours a month, and half day to a day a quarter.',
       'title': 'Getting Your Cleaning Company from $500K- $1M vs.  $1M- $5M (Grow My Cleaning '
                'Company)',
       'url': 'https://www.youtube.com/watch?v=PcnIuILxXOw&t=340s',
       'video_id': 'PcnIuILxXOw'},
      {'author': 'Clicks Geek',
       'channel': 'Clicks Geek',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:10](https://www.youtube.com/watch?v=EuwGlvViI4w&t=190s)',
       'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                    'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                    'and supervisor pods (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Cleaning it niche and when you start getting results like this just start '
               'pumping your budget incrementally to maybe 25 bucks a day something like that.',
       'timestamp': 190,
       'timestamp_label': '[00:03:10]',
       'timestamp_seconds': 190,
       'tip': 'Cleaning it niche and when you start getting results like this just start '
              'pumping your budget incrementally to maybe 25 bucks a day something like that.',
       'title': 'Janitorial Services Google Ads PPC Case Study (Clicks Geek)',
       'url': 'https://www.youtube.com/watch?v=EuwGlvViI4w&t=190s',
       'video_id': 'EuwGlvViI4w'},
      {'author': 'Commercial Cleaning CEO',
       'channel': 'Commercial Cleaning CEO',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:14:15](https://www.youtube.com/watch?v=wC3VDZWQwZk&t=855s)',
       'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                    'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                    'and supervisor pods (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'If you think it was, please share it with someone else who owns a commercial '
               'cleaning business that needs to start doing any one or all of these. Again, '
               'thanks so much for watching. Until next time, stay blessed.',
       'timestamp': 855,
       'timestamp_label': '[00:14:15]',
       'timestamp_seconds': 855,
       'tip': 'If you think it was, please share it with someone else who owns a commercial '
              'cleaning business that needs to start doing any one or all of these. Again, '
              'thanks so much for watching. Until next time, stay blessed.',
       'title': '8 Fast & Free Ways to Get Commercial Cleaning Contracts (Commercial Cleaning '
                'CEO)',
       'url': 'https://www.youtube.com/watch?v=wC3VDZWQwZk&t=855s',
       'video_id': 'wC3VDZWQwZk'},
      {'author': 'The Janitorial Store',
       'channel': 'The Janitorial Store',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:01](https://www.youtube.com/watch?v=Cf4hKGN0mXg&t=61s)',
       'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                    'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                    'and supervisor pods (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Determine what the total hours are per month so what we do is we take the '
               'point eight five times three days per week then times 52 weeks in a year '
               'divided by.',
       'timestamp': 61,
       'timestamp_label': '[00:01:01]',
       'timestamp_seconds': 61,
       'tip': 'Determine what the total hours are per month so what we do is we take the point '
              'eight five times three days per week then times 52 weeks in a year divided by.',
       'title': 'How to price a 2,400 square foot office space: How to price cleaning offices '
                '(The Janitorial Store)',
       'url': 'https://www.youtube.com/watch?v=Cf4hKGN0mXg&t=61s',
       'video_id': 'Cf4hKGN0mXg'},
      {'author': 'AJ SIMMONS',
       'channel': 'AJ SIMMONS',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:39](https://www.youtube.com/watch?v=VNrAGY4xXig&t=159s)',
       'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                    'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                    'and supervisor pods (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Just go to the next and actually back in my jam Pro days we used to clean for '
               "them anyway it wasn't this location but uh I believe I know they into "
               "Government Contracting in the day that's why they always stay locked down "
               "anyway all right let's go check out bunny pages.",
       'timestamp': 159,
       'timestamp_label': '[00:02:39]',
       'timestamp_seconds': 159,
       'tip': 'Just go to the next and actually back in my jam Pro days we used to clean for '
              "them anyway it wasn't this location but uh I believe I know they into "
              "Government Contracting in the day that's why they always stay locked down "
              "anyway all right let's go check out bunny pages.",
       'title': 'How To Get Commercial Cleaning Customers From Door To Doors Sales (AJ '
                'SIMMONS)',
       'url': 'https://www.youtube.com/watch?v=VNrAGY4xXig&t=159s',
       'video_id': 'VNrAGY4xXig'},
      {'author': 'Winter 🧊',
       'channel': 'Winter 🧊',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:30](https://www.youtube.com/watch?v=6Ee7M9O9djo&t=210s)',
       'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                    'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                    'and supervisor pods (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'So if you have any questions or concerns please please please comment below do '
               'not be shy I will definitely respond and depending on the response I have in '
               'accordance that I have I might even make a new video who knows have a good day '
               'bye.',
       'timestamp': 210,
       'timestamp_label': '[00:03:30]',
       'timestamp_seconds': 210,
       'tip': 'So if you have any questions or concerns please please please comment below do '
              'not be shy I will definitely respond and depending on the response I have in '
              'accordance that I have I might even make a new video who knows have a good day '
              'bye.',
       'title': 'Cleaning businesses Do NOT work through a franchise or management company!! '
                '(Winter 🧊)',
       'url': 'https://www.youtube.com/watch?v=6Ee7M9O9djo&t=210s',
       'video_id': '6Ee7M9O9djo'},
      {'author': 'Steam Boss inc',
       'channel': 'Steam Boss inc',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:54](https://www.youtube.com/watch?v=jt0SYjId62I&t=534s)',
       'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                    'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                    'and supervisor pods (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Couple more rinses before we can start laying some finish all right first coat '
               "on the bathrooms looking really good two more to go and we'll be in good shape "
               'the final product.',
       'timestamp': 534,
       'timestamp_label': '[00:08:54]',
       'timestamp_seconds': 534,
       'tip': 'Couple more rinses before we can start laying some finish all right first coat '
              "on the bathrooms looking really good two more to go and we'll be in good shape "
              'the final product.',
       'title': 'SUPER DIRTY GRIMY VCT Floor strip and wax transformation! #satisfying '
                '#cleaning (Steam Boss inc)',
       'url': 'https://www.youtube.com/watch?v=jt0SYjId62I&t=534s',
       'video_id': 'jt0SYjId62I'},
      {'author': 'The Janitorial Store',
       'channel': 'The Janitorial Store',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:16](https://www.youtube.com/watch?v=baQYWkWt7lQ&t=316s)',
       'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                    'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                    'and supervisor pods (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Rate our billable rate is the rate that we charge the per hour rate that we '
               "charge our clients it's not not our labor rate it's what we charge our clients "
               "per hour so in this case here you know let's say we're going to charge them "
               'thirty dollars per hour.',
       'timestamp': 316,
       'timestamp_label': '[00:05:16]',
       'timestamp_seconds': 316,
       'tip': 'Rate our billable rate is the rate that we charge the per hour rate that we '
              "charge our clients it's not not our labor rate it's what we charge our clients "
              "per hour so in this case here you know let's say we're going to charge them "
              'thirty dollars per hour.',
       'title': 'What are production rates and billable rates ? | The Janitorial Store (The '
                'Janitorial Store)',
       'url': 'https://www.youtube.com/watch?v=baQYWkWt7lQ&t=316s',
       'video_id': 'baQYWkWt7lQ'},
      {'author': 'Anton Pantio',
       'channel': 'Anton Pantio',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:10:10](https://www.youtube.com/watch?v=-1k_o5iWj8w&t=610s)',
       'relevance': 'Attributed practitioner commentary on recurring B2B commercial & medical '
                    'janitorial contracts, ISSA production-rate bidding, W-2/sub compliance, '
                    'and supervisor pods (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "And that's exactly what we do for our commercial cleaning clients. This is one "
               'of our cold calling clients. Generated him 15 solid walk-throughs in the past '
               'month.',
       'timestamp': 610,
       'timestamp_label': '[00:10:10]',
       'timestamp_seconds': 610,
       'tip': "And that's exactly what we do for our commercial cleaning clients. This is one "
              'of our cold calling clients. Generated him 15 solid walk-throughs in the past '
              'month.',
       'title': 'Cold Calling For Commercial Cleaning Companies (Script + Live Call) (Anton '
                'Pantio)',
       'url': 'https://www.youtube.com/watch?v=-1k_o5iWj8w&t=610s',
       'video_id': '-1k_o5iWj8w'}]}
