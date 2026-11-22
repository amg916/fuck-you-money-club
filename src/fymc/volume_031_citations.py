"""Curated 180-citation Uber & Commercial Fleet Arbitrage baseline (15 per chapter across Q1-Q12) mined strictly from verified Uber & Commercial Fleet Arbitrage YouTube transcripts."""
from __future__ import annotations

CHAPTER_KEYWORDS: dict[int, set[str]] = {1: {'179',
     '30106',
     'abi',
     'accidents',
     'ach',
     'adesa',
     'agreement',
     'airport',
     'alternative',
     'amazon',
     'amendment',
     'anywhere',
     'app',
     'arbitrage',
     'auction',
     'auto',
     'automated',
     'automation',
     'bankrupt',
     'before',
     'billing',
     'black',
     'bonus',
     'booking',
     'bouncie',
     'box',
     'brakes',
     'business',
     'buying',
     'california',
     'client',
     'clients',
     'firm',
     'margin',
     'market',
     'model',
     'niche',
     'operator',
     'revenue',
     'service',
     'value'},
 2: {'179',
     '30106',
     'abi',
     'accidents',
     'ach',
     'adesa',
     'agreement',
     'airport',
     'alternative',
     'amazon',
     'amendment',
     'anywhere',
     'app',
     'arbitrage',
     'auction',
     'auto',
     'automated',
     'automation',
     'bankrupt',
     'before',
     'billing',
     'black',
     'bonus',
     'booking',
     'bouncie',
     'box',
     'brakes',
     'budget',
     'business',
     'buyer',
     'buying',
     'california',
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
 3: {'179',
     '30106',
     'abi',
     'accidents',
     'ach',
     'adesa',
     'agreement',
     'airport',
     'alternative',
     'amazon',
     'amendment',
     'anywhere',
     'app',
     'arbitrage',
     'auction',
     'auto',
     'automated',
     'automation',
     'bankrupt',
     'before',
     'billing',
     'black',
     'bonus',
     'booking',
     'bouncie',
     'box',
     'brakes',
     'business',
     'buying',
     'california',
     'cash',
     'cashflow',
     'commission',
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
 4: {'179',
     '30106',
     'abi',
     'accidents',
     'ach',
     'adesa',
     'agreement',
     'airport',
     'alternative',
     'amazon',
     'amendment',
     'anywhere',
     'app',
     'arbitrage',
     'auction',
     'auto',
     'automated',
     'automation',
     'bankrupt',
     'before',
     'billing',
     'black',
     'bonus',
     'booking',
     'bouncie',
     'box',
     'brakes',
     'budget',
     'business',
     'buying',
     'california',
     'capital',
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
 5: {'179',
     '30106',
     'abi',
     'accidents',
     'ach',
     'adesa',
     'agreement',
     'airport',
     'alternative',
     'amazon',
     'amendment',
     'anywhere',
     'app',
     'arbitrage',
     'auction',
     'audit',
     'auto',
     'automated',
     'automation',
     'avoid',
     'bankrupt',
     'before',
     'billing',
     'black',
     'bonus',
     'booking',
     'bouncie',
     'box',
     'brakes',
     'business',
     'buying',
     'california',
     'clawback',
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
 6: {'179',
     '30106',
     'abi',
     'accidents',
     'ach',
     'adesa',
     'agreement',
     'airport',
     'alternative',
     'amazon',
     'amendment',
     'anywhere',
     'app',
     'arbitrage',
     'auction',
     'auto',
     'automated',
     'automation',
     'bankrupt',
     'before',
     'billing',
     'black',
     'bonus',
     'booking',
     'bouncie',
     'box',
     'brakes',
     'business',
     'buying',
     'california',
     'client',
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
 7: {'179',
     '30106',
     'abi',
     'accidents',
     'ach',
     'adesa',
     'agreement',
     'airport',
     'alternative',
     'amazon',
     'amendment',
     'anywhere',
     'app',
     'arbitrage',
     'auction',
     'auto',
     'automated',
     'automation',
     'bankrupt',
     'before',
     'billing',
     'black',
     'bonus',
     'booking',
     'bouncie',
     'box',
     'brakes',
     'business',
     'buying',
     'california',
     'checklist',
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
 8: {'179',
     '30106',
     'abi',
     'accidents',
     'ach',
     'adesa',
     'agreement',
     'airport',
     'alternative',
     'amazon',
     'amendment',
     'anywhere',
     'api',
     'app',
     'arbitrage',
     'auction',
     'auto',
     'automated',
     'automation',
     'bankrupt',
     'before',
     'billing',
     'black',
     'bonus',
     'booking',
     'bouncie',
     'box',
     'brakes',
     'business',
     'buying',
     'california',
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
 9: {'179',
     '30106',
     'abi',
     'accidents',
     'ach',
     'adesa',
     'agreement',
     'airport',
     'alternative',
     'amazon',
     'amendment',
     'anywhere',
     'app',
     'arbitrage',
     'auction',
     'auto',
     'automated',
     'automation',
     'bankrupt',
     'before',
     'billing',
     'black',
     'bonus',
     'booking',
     'bouncie',
     'box',
     'brakes',
     'business',
     'buying',
     'california',
     'compliance',
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
 10: {'179',
      '30106',
      'abi',
      'accidents',
      'ach',
      'adesa',
      'agent',
      'agreement',
      'ai',
      'airport',
      'alternative',
      'amazon',
      'amendment',
      'anywhere',
      'app',
      'arbitrage',
      'auction',
      'auto',
      'automate',
      'automated',
      'automation',
      'bankrupt',
      'before',
      'billing',
      'black',
      'bonus',
      'booking',
      'bouncie',
      'box',
      'brakes',
      'business',
      'buying',
      'california',
      'dashboard',
      'leverage',
      'pipeline',
      'scale',
      'script',
      'speed',
      'template',
      'workflow'},
 11: {'179',
      '30106',
      'abi',
      'accidents',
      'ach',
      'adesa',
      'agreement',
      'airport',
      'alternative',
      'amazon',
      'amendment',
      'anywhere',
      'app',
      'arbitrage',
      'auction',
      'auto',
      'automated',
      'automation',
      'bankrupt',
      'before',
      'billing',
      'black',
      'bonus',
      'booking',
      'bouncie',
      'box',
      'brakes',
      'business',
      'buying',
      'california',
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
 12: {'179',
      '30106',
      'abi',
      'accidents',
      'ach',
      'action',
      'adesa',
      'agreement',
      'airport',
      'alternative',
      'amazon',
      'amendment',
      'anywhere',
      'app',
      'arbitrage',
      'auction',
      'auto',
      'automated',
      'automation',
      'bankrupt',
      'before',
      'billing',
      'black',
      'bonus',
      'booking',
      'bouncie',
      'box',
      'brakes',
      'business',
      'buying',
      'california',
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

BASELINE_EXPERT_CITATIONS_BY_CHAPTER: dict[int, list[dict]] = {1: [{'author': 'Black Truck Mick',
      'channel': 'Black Truck Mick',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:20:59](https://www.youtube.com/watch?v=uODRGjORQF4&t=1259s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "So that's why I built this. It's a course in community black truck system by "
              'Onyx Elite, my company. And you basically can learn how to start a wildly '
              'profitable six-figure luxury SUV service business and get your first high value '
              'client in 30 days.',
      'timestamp': 1259,
      'timestamp_label': '[00:20:59]',
      'timestamp_seconds': 1259,
      'tip': "So that's why I built this. It's a course in community black truck system by "
             'Onyx Elite, my company. And you basically can learn how to start a wildly '
             'profitable six-figure luxury SUV service business and get your first high value '
             'client in 30 days.',
      'title': 'CHAUFFEUR: How I Made $15,000 My First Month with 1 Luxury SUV (And I Didn’t '
               'Even Own It) (Black Truck Mick)',
      'url': 'https://www.youtube.com/watch?v=uODRGjORQF4&t=1259s',
      'video_id': 'uODRGjORQF4'},
     {'author': 'Camber Hazard',
      'channel': 'Camber Hazard',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:18](https://www.youtube.com/watch?v=Z973kfjFqdY&t=78s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Determining this figure accurately allows business owners to calculate total '
              'cost of ownership before buying a single key. If a vehicle retains a higher '
              'percentage of its value after 5 years of service, your actual monthly operating '
              'cost drops significantly.',
      'timestamp': 78,
      'timestamp_label': '[00:01:18]',
      'timestamp_seconds': 78,
      'tip': 'Determining this figure accurately allows business owners to calculate total '
             'cost of ownership before buying a single key. If a vehicle retains a higher '
             'percentage of its value after 5 years of service, your actual monthly operating '
             'cost drops significantly.',
      'title': 'Fleet Vehicle Depreciation & Tax Write-Off Strategy in United States 2026 '
               '(Camber Hazard)',
      'url': 'https://www.youtube.com/watch?v=Z973kfjFqdY&t=78s',
      'video_id': 'Z973kfjFqdY'},
     {'author': 'Alex Auto',
      'channel': 'Alex Auto',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:28:07](https://www.youtube.com/watch?v=RSpmJqhFEIw&t=1687s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Starting a private car rental business is the best way to do it. You can find '
              "me on Alex O Auto and I can help you do that. It's nice nice nice having you "
              'on, man. Um learned a bit about, you know, basically what your clients want. I '
              'like I like the model a lot.',
      'timestamp': 1687,
      'timestamp_label': '[00:28:07]',
      'timestamp_seconds': 1687,
      'tip': 'Starting a private car rental business is the best way to do it. You can find me '
             "on Alex O Auto and I can help you do that. It's nice nice nice having you on, "
             'man. Um learned a bit about, you know, basically what your clients want. I like '
             'I like the model a lot.',
      'title': 'How I Scaled to 50 Rental Cars (And How You Can Too) (Alex Auto)',
      'url': 'https://www.youtube.com/watch?v=RSpmJqhFEIw&t=1687s',
      'video_id': 'RSpmJqhFEIw'},
     {'author': 'AutoMarketplace',
      'channel': 'AutoMarketplace',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:39:50](https://www.youtube.com/watch?v=DiLCf_drK0E&t=2390s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'TLC plates are, what the TLC plate rental business are. I think a lot of '
              'drivers are shifting to this model. They prefer owning their own car for '
              "various reasons like we spoke about before. Is there anything we're missing? "
              "There's any other things that you wanted to add?",
      'timestamp': 2390,
      'timestamp_label': '[00:39:50]',
      'timestamp_seconds': 2390,
      'tip': 'TLC plates are, what the TLC plate rental business are. I think a lot of drivers '
             'are shifting to this model. They prefer owning their own car for various reasons '
             "like we spoke about before. Is there anything we're missing? There's any other "
             'things that you wanted to add?',
      'title': 'Fast Track Mobility Enters NYC’s TLC Plate Rental Market as Drivers Seek '
               'Flexible Ownership Options (AutoMarketplace)',
      'url': 'https://www.youtube.com/watch?v=DiLCf_drK0E&t=2390s',
      'video_id': 'DiLCf_drK0E'},
     {'author': 'rideXserve',
      'channel': 'rideXserve',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:19:47](https://www.youtube.com/watch?v=pOWoMXyVapQ&t=1187s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Never forget, buying a brand new car for rideshare industry is doing charity '
              'work. The Tesla might eventually give you autonomous upside and appreciate in '
              'value. The Sienna Hybrid unlocks Uber XL and is great for airport trips.',
      'timestamp': 1187,
      'timestamp_label': '[00:19:47]',
      'timestamp_seconds': 1187,
      'tip': 'Never forget, buying a brand new car for rideshare industry is doing charity '
             'work. The Tesla might eventually give you autonomous upside and appreciate in '
             'value. The Sienna Hybrid unlocks Uber XL and is great for airport trips.',
      'title': 'Top 7 Cars for Uber & Lyft Driving in 2026 (Ranked) (rideXserve)',
      'url': 'https://www.youtube.com/watch?v=pOWoMXyVapQ&t=1187s',
      'video_id': 'pOWoMXyVapQ'},
     {'author': 'TJackk',
      'channel': 'TJackk',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:42](https://www.youtube.com/watch?v=UTnHLaPqh1s&t=462s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'s a lot of people that come in this business uh speaking from like a driver's "
              "standpoint where they want to come test the market to see if it's worth buying "
              'their own SUV.',
      'timestamp': 462,
      'timestamp_label': '[00:07:42]',
      'timestamp_seconds': 462,
      'tip': "'s a lot of people that come in this business uh speaking from like a driver's "
             "standpoint where they want to come test the market to see if it's worth buying "
             'their own SUV.',
      'title': 'Don’t Start an Uber Black Fleet Until You Know THIS (TJackk)',
      'url': 'https://www.youtube.com/watch?v=UTnHLaPqh1s&t=462s',
      'video_id': 'UTnHLaPqh1s'},
     {'author': 'My Chauffeur Life',
      'channel': 'My Chauffeur Life',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:28](https://www.youtube.com/watch?v=Y-1AudoR8JA&t=148s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "And here's something that took me years to learn. You have to read the people. "
              'Some clients want to chat and they just want connection, but others they value '
              'silence.',
      'timestamp': 148,
      'timestamp_label': '[00:02:28]',
      'timestamp_seconds': 148,
      'tip': "And here's something that took me years to learn. You have to read the people. "
             'Some clients want to chat and they just want connection, but others they value '
             'silence.',
      'title': '5 Things I WISH I KNEW before starting my Chauffeur Business (My Chauffeur '
               'Life)',
      'url': 'https://www.youtube.com/watch?v=Y-1AudoR8JA&t=148s',
      'video_id': 'Y-1AudoR8JA'},
     {'author': 'Delano Green',
      'channel': 'Delano Green',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:04](https://www.youtube.com/watch?v=PSopHdn3T8M&t=124s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': '400 dollars a day in this market. And then we just basically rent them. We make '
              "like a year's worth of revenue in probably like 3 months. And then we just like "
              'send them back to a different market.',
      'timestamp': 124,
      'timestamp_label': '[00:02:04]',
      'timestamp_seconds': 124,
      'tip': '400 dollars a day in this market. And then we just basically rent them. We make '
             "like a year's worth of revenue in probably like 3 months. And then we just like "
             'send them back to a different market.',
      'title': 'How I Added More Rental Cars Without Buying Them | Turo Cohosting (Delano '
               'Green)',
      'url': 'https://www.youtube.com/watch?v=PSopHdn3T8M&t=124s',
      'video_id': 'PSopHdn3T8M'},
     {'author': 'CAMTHECEO',
      'channel': 'CAMTHECEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:52](https://www.youtube.com/watch?v=grHcYj2iy-c&t=1012s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'all live in bigger cities than me. So just imagine what's possible where you "
              "live in this business, man. Like I've been doing it for years and I still "
              'become speechless when it comes to like the demand with this business model.',
      'timestamp': 1012,
      'timestamp_label': '[00:16:52]',
      'timestamp_seconds': 1012,
      'tip': "'all live in bigger cities than me. So just imagine what's possible where you "
             "live in this business, man. Like I've been doing it for years and I still become "
             'speechless when it comes to like the demand with this business model.',
      'title': 'How I Rent Cars to Uber Drivers at 23 (No Turo) (CAMTHECEO)',
      'url': 'https://www.youtube.com/watch?v=grHcYj2iy-c&t=1012s',
      'video_id': 'grHcYj2iy-c'},
     {'author': 'Owners Risk',
      'channel': 'Owners Risk',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:46](https://www.youtube.com/watch?v=oDmpBy9CTek&t=286s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'In a standard market like Texas, Florida, or California, fleet operators pay '
              'somewhere between $1,800 and $2,500 per vehicle per year in commercial '
              'coverage.',
      'timestamp': 286,
      'timestamp_label': '[00:04:46]',
      'timestamp_seconds': 286,
      'tip': 'In a standard market like Texas, Florida, or California, fleet operators pay '
             'somewhere between $1,800 and $2,500 per vehicle per year in commercial coverage.',
      'title': 'The Economics of Running an Uber Fleet (Owners Risk)',
      'url': 'https://www.youtube.com/watch?v=oDmpBy9CTek&t=286s',
      'video_id': 'oDmpBy9CTek'},
     {'author': 'Etienne Elsaesser',
      'channel': 'Etienne Elsaesser',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:29](https://www.youtube.com/watch?v=ILKICEKUl_A&t=629s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'The lifestyle asset is gone. Scenario three is the car is on consignment with a '
              'professional operator. The average daily rate on that McLaren is probably going '
              'to be anywhere from $800 to $1,100 per day.',
      'timestamp': 629,
      'timestamp_label': '[00:10:29]',
      'timestamp_seconds': 629,
      'tip': 'The lifestyle asset is gone. Scenario three is the car is on consignment with a '
             'professional operator. The average daily rate on that McLaren is probably going '
             'to be anywhere from $800 to $1,100 per day.',
      'title': 'How To Start A Car Rental Business in 2026 WITHOUT Cars | On Consignment '
               '(Etienne Elsaesser)',
      'url': 'https://www.youtube.com/watch?v=ILKICEKUl_A&t=629s',
      'video_id': 'ILKICEKUl_A'},
     {'author': 'Mike_Thebusinessman',
      'channel': 'Mike_Thebusinessman',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:40](https://www.youtube.com/watch?v=1Va2FwAMf2A&t=340s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Said these guys are catering it's more mass Market they want people that just "
              "getting into the business or intermediaries maybe you don't have the.",
      'timestamp': 340,
      'timestamp_label': '[00:05:40]',
      'timestamp_seconds': 340,
      'tip': "Said these guys are catering it's more mass Market they want people that just "
             "getting into the business or intermediaries maybe you don't have the.",
      'title': 'Best Car Rental Software 2024 (easy to use, all in one) (Mike_Thebusinessman)',
      'url': 'https://www.youtube.com/watch?v=1Va2FwAMf2A&t=340s',
      'video_id': '1Va2FwAMf2A'},
     {'author': 'Rideshare Professor',
      'channel': 'Rideshare Professor',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:43](https://www.youtube.com/watch?v=4Y5_eWf85tM&t=883s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Your business model so go check it out sign up right now at um the link below '
              "and I will throw in a code h-e-l-p-20 help20 you'll see that's another 20 off "
              'take care have fun make money.',
      'timestamp': 883,
      'timestamp_label': '[00:14:43]',
      'timestamp_seconds': 883,
      'tip': 'Your business model so go check it out sign up right now at um the link below '
             "and I will throw in a code h-e-l-p-20 help20 you'll see that's another 20 off "
             'take care have fun make money.',
      'title': 'One of my most successful businesses involves the Uber Fleet program. Learn '
               'how to make the Big $$$ (Rideshare Professor)',
      'url': 'https://www.youtube.com/watch?v=4Y5_eWf85tM&t=883s',
      'video_id': '4Y5_eWf85tM'},
     {'author': 'Shuttle The Payment Layer',
      'channel': 'Shuttle The Payment Layer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:09](https://www.youtube.com/watch?v=i4xmeCN8hsg&t=189s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Not here to follow along with the market we're looking to expand on ideas that "
              "we have and we're looking to bring dreams into reality so Innovation is for us "
              'I think the number one key in this awesome thank you Sam Co over HQ rental '
              "you're welcome.",
      'timestamp': 189,
      'timestamp_label': '[00:03:09]',
      'timestamp_seconds': 189,
      'tip': "Not here to follow along with the market we're looking to expand on ideas that "
             "we have and we're looking to bring dreams into reality so Innovation is for us I "
             "think the number one key in this awesome thank you Sam Co over HQ rental you're "
             'welcome.',
      'title': 'HQ Rental Explained in 5 Minutes: A Game-Changer in Rental Management (Shuttle '
               'The Payment Layer)',
      'url': 'https://www.youtube.com/watch?v=i4xmeCN8hsg&t=189s',
      'video_id': 'i4xmeCN8hsg'},
     {'author': 'Ariel Ortiz vlogs',
      'channel': 'Ariel Ortiz vlogs',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:57](https://www.youtube.com/watch?v=mz7qEsvja6E&t=117s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Que te rente la placa o una persona particular ambas partes el proceso puede '
              'ser igual todo va a depender una sola cosa es que si consigues una persona '
              'particular va a depender de cómo él vaya a hacer el proceso pero la '
              'corporaciones mayoría se manejan similar o.',
      'timestamp': 117,
      'timestamp_label': '[00:01:57]',
      'timestamp_seconds': 117,
      'tip': 'Que te rente la placa o una persona particular ambas partes el proceso puede ser '
             'igual todo va a depender una sola cosa es que si consigues una persona '
             'particular va a depender de cómo él vaya a hacer el proceso pero la '
             'corporaciones mayoría se manejan similar o.',
      'title': 'TLC: El Requisito Oculto Para Rentar Placas!! en NYC (Ariel Ortiz vlogs)',
      'url': 'https://www.youtube.com/watch?v=mz7qEsvja6E&t=117s',
      'video_id': 'mz7qEsvja6E'}],
 2: [{'author': 'FOX 2 Detroit',
      'channel': 'FOX 2 Detroit',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:59](https://www.youtube.com/watch?v=rvid3s_9KZA&t=119s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "AND THEY AND THEY DON'T PAY US MUCH. IN THE MEANTIME, A WAITING GAME FOR UBER "
              'BLACK DRIVERS, HOPING THE AIRPORT AND UBER CAN COME TO AN AGREEMENT FAST. I '
              'WILL HANDLE MY PRIVATE BUSINESS THAT, YOU KNOW, I BUILT UP MY OWN CLIENTELE '
              'OVER TIME NOW.',
      'timestamp': 119,
      'timestamp_label': '[00:01:59]',
      'timestamp_seconds': 119,
      'tip': "AND THEY AND THEY DON'T PAY US MUCH. IN THE MEANTIME, A WAITING GAME FOR UBER "
             'BLACK DRIVERS, HOPING THE AIRPORT AND UBER CAN COME TO AN AGREEMENT FAST. I WILL '
             'HANDLE MY PRIVATE BUSINESS THAT, YOU KNOW, I BUILT UP MY OWN CLIENTELE OVER TIME '
             'NOW.',
      'title': 'Uber Black drivers stopped from picking up customers at Metro Airport. (FOX 2 '
               'Detroit)',
      'url': 'https://www.youtube.com/watch?v=rvid3s_9KZA&t=119s',
      'video_id': 'rvid3s_9KZA'},
     {'author': 'RENTALL',
      'channel': 'RENTALL',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:59](https://www.youtube.com/watch?v=hPnlMkTp3JI&t=719s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Agreement and hit next and verify the billing details and hit the save invoice '
              'button to create the invoice you can either print the hard copy of the invoice '
              'or email the invoice to the customer.',
      'timestamp': 719,
      'timestamp_label': '[00:11:59]',
      'timestamp_seconds': 719,
      'tip': 'Agreement and hit next and verify the billing details and hit the save invoice '
             'button to create the invoice you can either print the hard copy of the invoice '
             'or email the invoice to the customer.',
      'title': 'Car Rental Software - Live Demonstration (RENTALL)',
      'url': 'https://www.youtube.com/watch?v=hPnlMkTp3JI&t=719s',
      'video_id': 'hPnlMkTp3JI'},
     {'author': 'Russ Unlocked',
      'channel': 'Russ Unlocked',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:30](https://www.youtube.com/watch?v=y_X4A98Zuec&t=150s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'So basically when you buy cars from the auction, you got to pay via either like '
              "wire, ACH, or a cashier's check. Cashier's check is always the quickest because "
              'they take it and scan it and they basically mark it as paid right away.',
      'timestamp': 150,
      'timestamp_label': '[00:02:30]',
      'timestamp_seconds': 150,
      'tip': 'So basically when you buy cars from the auction, you got to pay via either like '
             "wire, ACH, or a cashier's check. Cashier's check is always the quickest because "
             'they take it and scan it and they basically mark it as paid right away.',
      'title': 'What It Really Takes to Run a Million-Dollar Car Rental Business (Russ '
               'Unlocked)',
      'url': 'https://www.youtube.com/watch?v=y_X4A98Zuec&t=150s',
      'video_id': 'y_X4A98Zuec'},
     {'author': 'ESCAPE THE MATRIX',
      'channel': 'ESCAPE THE MATRIX',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:55](https://www.youtube.com/watch?v=fPh6slkW9Tk&t=295s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Whenever I overthink about a decision, I end up not taking action. So, I ended '
              'up not overthinking it and I just ended up taking action. So, I did end up '
              'getting the car, put no dollars down payment. I did not pay anything towards '
              'the taxes.',
      'timestamp': 295,
      'timestamp_label': '[00:04:55]',
      'timestamp_seconds': 295,
      'tip': 'Whenever I overthink about a decision, I end up not taking action. So, I ended '
             'up not overthinking it and I just ended up taking action. So, I did end up '
             'getting the car, put no dollars down payment. I did not pay anything towards the '
             'taxes.',
      'title': 'I Bought a $125,000 SUV To Drive Uber. Everyone Said I Was Crazy. (ESCAPE THE '
               'MATRIX)',
      'url': 'https://www.youtube.com/watch?v=fPh6slkW9Tk&t=295s',
      'video_id': 'fPh6slkW9Tk'},
     {'author': 'AutoMarketplace',
      'channel': 'AutoMarketplace',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:18](https://www.youtube.com/watch?v=8QnFsW_-2_0&t=618s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Need to renew your fhv license you will also need to pay $625 using the tlcr '
              'system but that will be a separate transaction to pay the $125 transfer fee go '
              'to the TLC Lars and click the menu item fees and return payments then select '
              'existing TLC.',
      'timestamp': 618,
      'timestamp_label': '[00:10:18]',
      'timestamp_seconds': 618,
      'tip': 'Need to renew your fhv license you will also need to pay $625 using the tlcr '
             'system but that will be a separate transaction to pay the $125 transfer fee go '
             'to the TLC Lars and click the menu item fees and return payments then select '
             'existing TLC.',
      'title': '🔐🚖 NYC TLC Plate (FHV License) Storage: Step-by-Step Guide for Drivers & '
               'Fleets (AutoMarketplace)',
      'url': 'https://www.youtube.com/watch?v=8QnFsW_-2_0&t=618s',
      'video_id': '8QnFsW_-2_0'},
     {'author': 'Alex Auto',
      'channel': 'Alex Auto',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:43](https://www.youtube.com/watch?v=G-0j82EXJlk&t=343s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'These drivers are willing to pay a premium for these cars. The reason why is '
              'because they make anywhere from a thousand to two thousand dollars every single '
              'week. Full-time Uber drivers, full-time Lyft drivers, people that drive a '
              'combination of DoorDash and Amazon Flex.',
      'timestamp': 343,
      'timestamp_label': '[00:05:43]',
      'timestamp_seconds': 343,
      'tip': 'These drivers are willing to pay a premium for these cars. The reason why is '
             'because they make anywhere from a thousand to two thousand dollars every single '
             'week. Full-time Uber drivers, full-time Lyft drivers, people that drive a '
             'combination of DoorDash and Amazon Flex.',
      'title': 'How I built a 6 figure PRIVATE car rental business in 2 years (copy me) (Alex '
               'Auto)',
      'url': 'https://www.youtube.com/watch?v=G-0j82EXJlk&t=343s',
      'video_id': 'G-0j82EXJlk'},
     {'author': 'THE GENWEALTH SHOW',
      'channel': 'THE GENWEALTH SHOW',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:02](https://www.youtube.com/watch?v=_Z_UpLE5fM0&t=62s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Uber supplying you with the drivers if you can supply them with the vehicles. '
              "So, he was telling me he owns about five or six black trucks, GMC's, the big "
              'bodies, of course, and Uber will get him on contract with certain drivers.',
      'timestamp': 62,
      'timestamp_label': '[00:01:02]',
      'timestamp_seconds': 62,
      'tip': 'Uber supplying you with the drivers if you can supply them with the vehicles. '
             "So, he was telling me he owns about five or six black trucks, GMC's, the big "
             'bodies, of course, and Uber will get him on contract with certain drivers.',
      'title': '$100,000 A Year Uber Fleet Business (THE GENWEALTH SHOW)',
      'url': 'https://www.youtube.com/watch?v=_Z_UpLE5fM0&t=62s',
      'video_id': '_Z_UpLE5fM0'},
     {'author': 'Critical Reviews',
      'channel': 'Critical Reviews',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:22](https://www.youtube.com/watch?v=BbAy6S7Oz1I&t=22s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Tag of $89 seems reasonable don't forget about the $9 monthly service fee over "
              "time that adds up so if you're looking for a budget-friendly option this might.",
      'timestamp': 22,
      'timestamp_label': '[00:00:22]',
      'timestamp_seconds': 22,
      'tip': "Tag of $89 seems reasonable don't forget about the $9 monthly service fee over "
             "time that adds up so if you're looking for a budget-friendly option this might.",
      'title': 'Bouncie GPS Car Tracker | 5 Shocking Reasons NOT to Buy! 📉🚗 (Critical Reviews)',
      'url': 'https://www.youtube.com/watch?v=BbAy6S7Oz1I&t=22s',
      'video_id': 'BbAy6S7Oz1I'},
     {'author': 'Khushnud Numonov',
      'channel': 'Khushnud Numonov',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:23:52](https://www.youtube.com/watch?v=uhkmLcXXwMk&t=1432s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Uber and they only have lift so they have opoi they have black Lane so you gota '
              "like when you're in this business like you can't be just in one company.",
      'timestamp': 1432,
      'timestamp_label': '[00:23:52]',
      'timestamp_seconds': 1432,
      'tip': 'Uber and they only have lift so they have opoi they have black Lane so you gota '
             "like when you're in this business like you can't be just in one company.",
      'title': 'Uber Black vs Opoli vs Blacklane: Which Pays More? (Khushnud Numonov)',
      'url': 'https://www.youtube.com/watch?v=uhkmLcXXwMk&t=1432s',
      'video_id': 'uhkmLcXXwMk'},
     {'author': 'Soniclove21',
      'channel': 'Soniclove21',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:32](https://www.youtube.com/watch?v=TwvZcpkzAxo&t=272s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "The fee that's approximately 425 450 for the fees at DMV so make sure you have "
              "that ready make sure you have all her money ready because if you don't have "
              'that money all the money ready to get everything done it makes some sense.',
      'timestamp': 272,
      'timestamp_label': '[00:04:32]',
      'timestamp_seconds': 272,
      'tip': "The fee that's approximately 425 450 for the fees at DMV so make sure you have "
             "that ready make sure you have all her money ready because if you don't have that "
             'money all the money ready to get everything done it makes some sense.',
      'title': 'TLC Plates NYC (Soniclove21)',
      'url': 'https://www.youtube.com/watch?v=TwvZcpkzAxo&t=272s',
      'video_id': 'TwvZcpkzAxo'},
     {'author': 'DylanIsMayor',
      'channel': 'DylanIsMayor',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:27](https://www.youtube.com/watch?v=ZU8uokic3ws&t=327s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Charge his ass oh we got customers we got customer bro I'm actually surprised "
              "how well this is working he said hi ma' want a rental we're actually doing "
              "business this is amazing I love this so much Who's.",
      'timestamp': 327,
      'timestamp_label': '[00:05:27]',
      'timestamp_seconds': 327,
      'tip': "Charge his ass oh we got customers we got customer bro I'm actually surprised "
             "how well this is working he said hi ma' want a rental we're actually doing "
             "business this is amazing I love this so much Who's.",
      'title': 'I started a CAR RENTAL business in Greenville (DylanIsMayor)',
      'url': 'https://www.youtube.com/watch?v=ZU8uokic3ws&t=327s',
      'video_id': 'ZU8uokic3ws'},
     {'author': 'Limo Anywhere: Livery Software & Training',
      'channel': 'Limo Anywhere: Livery Software & Training',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:49](https://www.youtube.com/watch?v=8ejH3mv4ka8&t=49s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Status now let's go over how to receive a credit card payment if the credit "
              'card information was captured at the time of the booking all we will need to do '
              'is.',
      'timestamp': 49,
      'timestamp_label': '[00:00:49]',
      'timestamp_seconds': 49,
      'tip': "Status now let's go over how to receive a credit card payment if the credit card "
             'information was captured at the time of the booking all we will need to do is.',
      'title': 'Processing Payments (Limo Anywhere: Livery Software & Training)',
      'url': 'https://www.youtube.com/watch?v=8ejH3mv4ka8&t=49s',
      'video_id': '8ejH3mv4ka8'},
     {'author': 'Delano Green',
      'channel': 'Delano Green',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:39](https://www.youtube.com/watch?v=SPoQzQlFhXg&t=39s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Where I live, I actually got banned from the airport. The airport banned me '
              'from being there. They told me, "Listen, if we see any more of your cars here '
              "anymore, we're we're going to tow them. And you're just going to have to pay to "
              'get it out, all right?".',
      'timestamp': 39,
      'timestamp_label': '[00:00:39]',
      'timestamp_seconds': 39,
      'tip': 'Where I live, I actually got banned from the airport. The airport banned me from '
             'being there. They told me, "Listen, if we see any more of your cars here '
             "anymore, we're we're going to tow them. And you're just going to have to pay to "
             'get it out, all right?".',
      'title': 'The Systems It Takes to Manage 99 Rental Cars on Turo, Full Scale Turo '
               'Management Service (Delano Green)',
      'url': 'https://www.youtube.com/watch?v=SPoQzQlFhXg&t=39s',
      'video_id': 'SPoQzQlFhXg'},
     {'author': 'quartytypo',
      'channel': 'quartytypo',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:25](https://www.youtube.com/watch?v=1-02Nj4vD78&t=145s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "That you won't have to pay I don't want to take that kind of chance because the "
              'accident could be my fault not intentionally but just some Minor error puts you '
              'at fault and the highway patrol writes you a ticket for being at fault now you '
              'have no insurance coverage.',
      'timestamp': 145,
      'timestamp_label': '[00:02:25]',
      'timestamp_seconds': 145,
      'tip': "That you won't have to pay I don't want to take that kind of chance because the "
             'accident could be my fault not intentionally but just some Minor error puts you '
             'at fault and the highway patrol writes you a ticket for being at fault now you '
             'have no insurance coverage.',
      'title': 'supplemental liability insurance on car rental problem (quartytypo)',
      'url': 'https://www.youtube.com/watch?v=1-02Nj4vD78&t=145s',
      'video_id': '1-02Nj4vD78'},
     {'author': 'Khushnud Numonov',
      'channel': 'Khushnud Numonov',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:14](https://www.youtube.com/watch?v=IqvMzwtwzrI&t=554s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Additional three hundred and forty dollars they'll have to pay and it is plus "
              '8161 dollars with the total premium that I have to pay a year so overall it '
              'would be eight thousand five hundred dollars eight thousand five hundred '
              'dollars we multiply it by two percent.',
      'timestamp': 554,
      'timestamp_label': '[00:09:14]',
      'timestamp_seconds': 554,
      'tip': "Additional three hundred and forty dollars they'll have to pay and it is plus "
             '8161 dollars with the total premium that I have to pay a year so overall it '
             'would be eight thousand five hundred dollars eight thousand five hundred dollars '
             'we multiply it by two percent.',
      'title': 'How To Get The BEST Commercial Insurance | Uber Black Commercial Insurance '
               '(Khushnud Numonov)',
      'url': 'https://www.youtube.com/watch?v=IqvMzwtwzrI&t=554s',
      'video_id': 'IqvMzwtwzrI'}],
 3: [{'author': 'Money Prism',
      'channel': 'Money Prism',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:24:13](https://www.youtube.com/watch?v=tNUrWA8I5bI&t=1453s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Extras at $14 because you cut them to protect the rate. Your costs do not drop '
              'with it. Depreciation is fixed the day you signed the purchase agreement. The '
              'mag at the airport is fixed. Your staff is mostly fixed. And then the auction '
              'comes in 9% below books.',
      'timestamp': 1453,
      'timestamp_label': '[00:24:13]',
      'timestamp_seconds': 1453,
      'tip': 'Extras at $14 because you cut them to protect the rate. Your costs do not drop '
             'with it. Depreciation is fixed the day you signed the purchase agreement. The '
             'mag at the airport is fixed. Your staff is mostly fixed. And then the auction '
             'comes in 9% below books.',
      'title': 'The Economics of Owning a Car Rental Fleet (Money Prism)',
      'url': 'https://www.youtube.com/watch?v=tNUrWA8I5bI&t=1453s',
      'video_id': 'tNUrWA8I5bI'},
     {'author': 'Rideshare Professor',
      'channel': 'Rideshare Professor',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:00](https://www.youtube.com/watch?v=MTc0vheuAy8&t=120s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'California Public Utilities Commission uh that allows you to have people in '
              'your vehicle for hire where you charge them a fee. Um the whole PUC process uh '
              'to to get a TCP takes anywhere between 5 and 7 weeks right now. And the license '
              'itself costs $1,000.',
      'timestamp': 120,
      'timestamp_label': '[00:02:00]',
      'timestamp_seconds': 120,
      'tip': 'California Public Utilities Commission uh that allows you to have people in your '
             'vehicle for hire where you charge them a fee. Um the whole PUC process uh to to '
             'get a TCP takes anywhere between 5 and 7 weeks right now. And the license itself '
             'costs $1,000.',
      'title': 'Businessrocket.com founder and Rideshare Professor discussing TCP and Fleets '
               '(Rideshare Professor)',
      'url': 'https://www.youtube.com/watch?v=MTc0vheuAy8&t=120s',
      'video_id': 'MTc0vheuAy8'},
     {'author': 'darius benders',
      'channel': 'darius benders',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:43](https://www.youtube.com/watch?v=NFLtPz5bUp4&t=1003s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "I know you talk about cash cars. Is it like Facebook market? Is it uh what's "
              'the other one? Craigslist or how do we source these cash cars? What price point '
              'should they be looking for? Like as far as me advertising or buying?',
      'timestamp': 1003,
      'timestamp_label': '[00:16:43]',
      'timestamp_seconds': 1003,
      'tip': "I know you talk about cash cars. Is it like Facebook market? Is it uh what's the "
             'other one? Craigslist or how do we source these cash cars? What price point '
             'should they be looking for? Like as far as me advertising or buying?',
      'title': 'Earning $400 WEEK Renting Cars to Uber Drivers (darius benders)',
      'url': 'https://www.youtube.com/watch?v=NFLtPz5bUp4&t=1003s',
      'video_id': 'NFLtPz5bUp4'},
     {'author': 'Merchant Maverick',
      'channel': 'Merchant Maverick',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:45](https://www.youtube.com/watch?v=1Nm_1fEmKUk&t=225s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'And that covers our countdown of the five best commercial auto insurance '
              "providers. Whether you're looking for nationwide coverage, fleet management "
              "solutions, competitive pricing, or comprehensive protection, there's an option "
              'tailored to your business needs.',
      'timestamp': 225,
      'timestamp_label': '[00:03:45]',
      'timestamp_seconds': 225,
      'tip': 'And that covers our countdown of the five best commercial auto insurance '
             "providers. Whether you're looking for nationwide coverage, fleet management "
             "solutions, competitive pricing, or comprehensive protection, there's an option "
             'tailored to your business needs.',
      'title': 'Best Commercial Auto Insurance (Merchant Maverick)',
      'url': 'https://www.youtube.com/watch?v=1Nm_1fEmKUk&t=225s',
      'video_id': '1Nm_1fEmKUk'},
     {'author': 'AutoMarketplace',
      'channel': 'AutoMarketplace',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:54:47](https://www.youtube.com/watch?v=kuB7bxLZKa0&t=3287s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Sure of course no zero speculation uh like purchasing any business of course '
              "you you're hoping to make your money back and hold it for years. Uh but this is "
              "a such thin profit margin business for one car you're making nothing.",
      'timestamp': 3287,
      'timestamp_label': '[00:54:47]',
      'timestamp_seconds': 3287,
      'tip': 'Sure of course no zero speculation uh like purchasing any business of course you '
             "you're hoping to make your money back and hold it for years. Uh but this is a "
             "such thin profit margin business for one car you're making nothing.",
      'title': '🤔🐆🎙️ NYC TLC Leasing: "Predatory" Business Model (?), Plates, EVs & More '
               '(AutoMarketplace)',
      'url': 'https://www.youtube.com/watch?v=kuB7bxLZKa0&t=3287s',
      'video_id': 'kuB7bxLZKa0'},
     {'author': 'How Master',
      'channel': 'How Master',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:52](https://www.youtube.com/watch?v=gmU1WdF-DCo&t=52s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Sometimes the location data lags or shows a delay when your car moves. It's not "
              'a huge issue, but worth noting if you need realtime precision. The app also '
              'requires a paid subscription, so even though the device itself is affordable, '
              "you'll have ongoing monthly costs.",
      'timestamp': 52,
      'timestamp_label': '[00:00:52]',
      'timestamp_seconds': 52,
      'tip': "Sometimes the location data lags or shows a delay when your car moves. It's not "
             'a huge issue, but worth noting if you need realtime precision. The app also '
             'requires a paid subscription, so even though the device itself is affordable, '
             "you'll have ongoing monthly costs.",
      'title': 'Bouncie Review — My Honest Experience Using This Smart GPS Car Tracker (How '
               'Master)',
      'url': 'https://www.youtube.com/watch?v=gmU1WdF-DCo&t=52s',
      'video_id': 'gmU1WdF-DCo'},
     {'author': 'Khushnud Numonov',
      'channel': 'Khushnud Numonov',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:35](https://www.youtube.com/watch?v=eXUCLdNVhYc&t=635s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Buying a used vehicle for cash and register registering it to your company is '
              'the easiest way to go and will save you a lot of headaches moving forward in '
              "the process I don't think people who are trying to be a limo drivers have that "
              'much of cash.',
      'timestamp': 635,
      'timestamp_label': '[00:10:35]',
      'timestamp_seconds': 635,
      'tip': 'Buying a used vehicle for cash and register registering it to your company is '
             'the easiest way to go and will save you a lot of headaches moving forward in the '
             "process I don't think people who are trying to be a limo drivers have that much "
             'of cash.',
      'title': 'How To Get PUC/TCP PERMIT For Uber Black & Limo Company (Khushnud Numonov)',
      'url': 'https://www.youtube.com/watch?v=eXUCLdNVhYc&t=635s',
      'video_id': 'eXUCLdNVhYc'},
     {'author': "Freelancer's Wealth Blueprint",
      'channel': "Freelancer's Wealth Blueprint",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:22](https://www.youtube.com/watch?v=Hxl9pLAo8c0&t=142s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'A full commercial auto policy covers everything, costs several thousand dollars '
              'a year, and is genuine overkill for a part-time driver. For most drivers, the '
              'endorsement is the right answer, and it also happens to be the piece with the '
              'cleanest tax story.',
      'timestamp': 142,
      'timestamp_label': '[00:02:22]',
      'timestamp_seconds': 142,
      'tip': 'A full commercial auto policy covers everything, costs several thousand dollars '
             'a year, and is genuine overkill for a part-time driver. For most drivers, the '
             'endorsement is the right answer, and it also happens to be the piece with the '
             'cleanest tax story.',
      'title': 'Uber Driver Taxes 2026: Your Car Insurance Split Between Two Uses '
               "(Freelancer's Wealth Blueprint)",
      'url': 'https://www.youtube.com/watch?v=Hxl9pLAo8c0&t=142s',
      'video_id': 'Hxl9pLAo8c0'},
     {'author': 'FleetPilot',
      'channel': 'FleetPilot',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:33:55](https://www.youtube.com/watch?v=W_GJwoORfVw&t=2035s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'re trying to look at, this is what it should bring on a return. This is what "
              'your operating cost should be. We called it the baseline and the benchmark. So, '
              'we want to be able to cover the cost as well as try and be able to make, you '
              'know, a sizable profit.',
      'timestamp': 2035,
      'timestamp_label': '[00:33:55]',
      'timestamp_seconds': 2035,
      'tip': "'re trying to look at, this is what it should bring on a return. This is what "
             'your operating cost should be. We called it the baseline and the benchmark. So, '
             'we want to be able to cover the cost as well as try and be able to make, you '
             'know, a sizable profit.',
      'title': 'The B2B Rental Strategy Behind His 277-Vehicle Fleet (FleetPilot)',
      'url': 'https://www.youtube.com/watch?v=W_GJwoORfVw&t=2035s',
      'video_id': 'W_GJwoORfVw'},
     {'author': 'Etienne Elsaesser',
      'channel': 'Etienne Elsaesser',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:43](https://www.youtube.com/watch?v=amfsF8yd5hg&t=103s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'s why this is spreading like wildfire. There's low barrier to entry. 5,000 is "
              "realistic for a lot of people, and there's more gig workers in the economy than "
              'ever before, and people are looking for an easier alternative to Turo or '
              'finance fleets.',
      'timestamp': 103,
      'timestamp_label': '[00:01:43]',
      'timestamp_seconds': 103,
      'tip': "'s why this is spreading like wildfire. There's low barrier to entry. 5,000 is "
             "realistic for a lot of people, and there's more gig workers in the economy than "
             'ever before, and people are looking for an easier alternative to Turo or finance '
             'fleets.',
      'title': 'The Reality of Renting Cars to Gig Workers (Etienne Elsaesser)',
      'url': 'https://www.youtube.com/watch?v=amfsF8yd5hg&t=103s',
      'video_id': 'amfsF8yd5hg'},
     {'author': 'TJackk',
      'channel': 'TJackk',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:15](https://www.youtube.com/watch?v=9mwQox6xtqw&t=255s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': '"Oh, it\'s a scam or it costs too much money." No, everything in life is pretty '
              'much management. How good or how well are you at managing different things? And '
              'being an Uber fleet business, you have to be very good at managing if you want '
              'to stay in this business.',
      'timestamp': 255,
      'timestamp_label': '[00:04:15]',
      'timestamp_seconds': 255,
      'tip': '"Oh, it\'s a scam or it costs too much money." No, everything in life is pretty '
             'much management. How good or how well are you at managing different things? And '
             'being an Uber fleet business, you have to be very good at managing if you want '
             'to stay in this business.',
      'title': 'I Ran an Uber Black Fleet for 8 Months — Here’s the Truth (TJackk)',
      'url': 'https://www.youtube.com/watch?v=9mwQox6xtqw&t=255s',
      'video_id': '9mwQox6xtqw'},
     {'author': 'The Startup Hub',
      'channel': 'The Startup Hub',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:05](https://www.youtube.com/watch?v=aykNFM9361U&t=185s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Thousand dollars depending on your area and how long they are if you're doing "
              "uh airport ride and it's like an 80 mile ride you can expect it you know rake "
              'in a few hundred dollars in that single ride.',
      'timestamp': 185,
      'timestamp_label': '[00:03:05]',
      'timestamp_seconds': 185,
      'tip': "Thousand dollars depending on your area and how long they are if you're doing uh "
             "airport ride and it's like an 80 mile ride you can expect it you know rake in a "
             'few hundred dollars in that single ride.',
      'title': 'How Much Can You Make Driving Uber Black in 2024? (Uber XL, Comfort, Select, '
               'Black SUV, Green, WAV) (The Startup Hub)',
      'url': 'https://www.youtube.com/watch?v=aykNFM9361U&t=185s',
      'video_id': 'aykNFM9361U'},
     {'author': 'Wires747',
      'channel': 'Wires747',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:23](https://www.youtube.com/watch?v=YbO6R8RKS_8&t=323s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "So this is it's this is what's nice about this unit. There's another relay that "
              'comes with it. And then you have to connect the relay to this mess over here, '
              'the ignition, the starter and everything. And then the other wire from the '
              'relay come back to these wires over here.',
      'timestamp': 323,
      'timestamp_label': '[00:05:23]',
      'timestamp_seconds': 323,
      'tip': "So this is it's this is what's nice about this unit. There's another relay that "
             'comes with it. And then you have to connect the relay to this mess over here, '
             'the ignition, the starter and everything. And then the other wire from the relay '
             'come back to these wires over here.',
      'title': 'How To Install Moovetrax GPS Tracker With Kill Switch Kia Optima or Huyndai '
               '(Wires747)',
      'url': 'https://www.youtube.com/watch?v=YbO6R8RKS_8&t=323s',
      'video_id': 'YbO6R8RKS_8'},
     {'author': 'King of Rentals',
      'channel': 'King of Rentals',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:21:27](https://www.youtube.com/watch?v=qwQ8yQbhunw&t=1287s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': '400 a week, averages out to 13 or $1,700 a month and $20,000 over 52 weeks. '
              "Obviously, you have to subtract out your costs. A lot of times it's vehicle "
              'payment. If you own cars in cash, which the best model is cheap economy like '
              'Priuses, super reliable.',
      'timestamp': 1287,
      'timestamp_label': '[00:21:27]',
      'timestamp_seconds': 1287,
      'tip': '400 a week, averages out to 13 or $1,700 a month and $20,000 over 52 weeks. '
             "Obviously, you have to subtract out your costs. A lot of times it's vehicle "
             'payment. If you own cars in cash, which the best model is cheap economy like '
             'Priuses, super reliable.',
      'title': 'The ULTIMATE Rideshare Webinar (MUST WATCH!!) (King of Rentals)',
      'url': 'https://www.youtube.com/watch?v=qwQ8yQbhunw&t=1287s',
      'video_id': 'qwQ8yQbhunw'},
     {'author': 'Mr SharK',
      'channel': 'Mr SharK',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:34](https://www.youtube.com/watch?v=V5kch9SIAjI&t=694s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'About 20 minutes so with that drop I will be on around 50 maybe 160 pounds and '
              "that's like uh halfway to the shift I think it's not bad.",
      'timestamp': 694,
      'timestamp_label': '[00:11:34]',
      'timestamp_seconds': 694,
      'tip': 'About 20 minutes so with that drop I will be on around 50 maybe 160 pounds and '
             "that's like uh halfway to the shift I think it's not bad.",
      'title': 'Private Chauffeur vs. Uber Exec – 10 Hours Shift: Who Earns More? (Mr SharK)',
      'url': 'https://www.youtube.com/watch?v=V5kch9SIAjI&t=694s',
      'video_id': 'V5kch9SIAjI'}],
 4: [{'author': 'Fin Saint',
      'channel': 'Fin Saint',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:38](https://www.youtube.com/watch?v=kyXtImFfyxA&t=278s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': '" If the form doesn\'t ask about ride-share work, contact the insurer before '
              'buying. Ask for the endorsement name and written confirmation. Finally, check '
              'the current insurance certificate in your Uber or Lyft driver app and compare '
              'it with your personal policy.',
      'timestamp': 278,
      'timestamp_label': '[00:04:38]',
      'timestamp_seconds': 278,
      'tip': '" If the form doesn\'t ask about ride-share work, contact the insurer before '
             'buying. Ask for the endorsement name and written confirmation. Finally, check '
             'the current insurance certificate in your Uber or Lyft driver app and compare it '
             'with your personal policy.',
      'title': '𝗨𝗯𝗲𝗿 & 𝗟𝘆𝗳𝘁 𝗗𝗿𝗶𝘃𝗲𝗿𝘀: How to Compare Rideshare Insurance on Credit Karma (Fin '
               'Saint)',
      'url': 'https://www.youtube.com/watch?v=kyXtImFfyxA&t=278s',
      'video_id': 'kyXtImFfyxA'},
     {'author': 'TJackk',
      'channel': 'TJackk',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:37](https://www.youtube.com/watch?v=Yr0mmM9YyTc&t=217s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "That's why I tell people, hey, know what you want out of this business before "
              'you actually spend money to get started because getting started with Uber Black '
              'is not cheap. You got to pay for commercial insurance. You got to pay for all '
              'the limousine licenses and permits.',
      'timestamp': 217,
      'timestamp_label': '[00:03:37]',
      'timestamp_seconds': 217,
      'tip': "That's why I tell people, hey, know what you want out of this business before "
             'you actually spend money to get started because getting started with Uber Black '
             'is not cheap. You got to pay for commercial insurance. You got to pay for all '
             'the limousine licenses and permits.',
      'title': 'The Truth About Uber Black vs Chauffeur Services (TJackk)',
      'url': 'https://www.youtube.com/watch?v=Yr0mmM9YyTc&t=217s',
      'video_id': 'Yr0mmM9YyTc'},
     {'author': 'Alex Auto',
      'channel': 'Alex Auto',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:23](https://www.youtube.com/watch?v=k3tFtA9SWv4&t=383s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Uh, they have different types of commercial auto policies. They have one for '
              'the car rental business specifically. Um, they have limousine insurance for '
              'limousine transportation companies, and they have Uber black insurance for '
              'people that rent out Uber Black cars.',
      'timestamp': 383,
      'timestamp_label': '[00:06:23]',
      'timestamp_seconds': 383,
      'tip': 'Uh, they have different types of commercial auto policies. They have one for the '
             'car rental business specifically. Um, they have limousine insurance for '
             'limousine transportation companies, and they have Uber black insurance for '
             'people that rent out Uber Black cars.',
      'title': 'The Best Commercial Insurance For Car Rental Business | TURO & Private (Alex '
               'Auto)',
      'url': 'https://www.youtube.com/watch?v=k3tFtA9SWv4&t=383s',
      'video_id': 'k3tFtA9SWv4'},
     {'author': 'Mike_Thebusinessman',
      'channel': 'Mike_Thebusinessman',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:17:05](https://www.youtube.com/watch?v=pXYcnDt9ASA&t=1025s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "You don't need over complicated software. Everything is already automated in "
              "the software. You don't need months of setup. I just proved to you guys that "
              'you can set this up live in under 20 minutes. But what you do need is to get '
              'you the right car.',
      'timestamp': 1025,
      'timestamp_label': '[00:17:05]',
      'timestamp_seconds': 1025,
      'tip': "You don't need over complicated software. Everything is already automated in the "
             "software. You don't need months of setup. I just proved to you guys that you can "
             'set this up live in under 20 minutes. But what you do need is to get you the '
             'right car.',
      'title': 'This Is the Easiest Way To Start A Private Car Rental Business (Without Turo) '
               '(Mike_Thebusinessman)',
      'url': 'https://www.youtube.com/watch?v=pXYcnDt9ASA&t=1025s',
      'video_id': 'pXYcnDt9ASA'},
     {'author': 'King of Rentals',
      'channel': 'King of Rentals',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:34](https://www.youtube.com/watch?v=NQzlTWjz8a0&t=214s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Rent directly to customers, collect payment, have them sign a contract with '
              "template for it, verify driver's license, sell insurance if you need to. "
              "Literally there's a laundry list of things that are in the software. It's only "
              '$99 a month and that software is called iFleet.',
      'timestamp': 214,
      'timestamp_label': '[00:03:34]',
      'timestamp_seconds': 214,
      'tip': 'Rent directly to customers, collect payment, have them sign a contract with '
             "template for it, verify driver's license, sell insurance if you need to. "
             "Literally there's a laundry list of things that are in the software. It's only "
             '$99 a month and that software is called iFleet.',
      'title': 'How One Rental Car Turned Into a Full-Time Business... (King of Rentals)',
      'url': 'https://www.youtube.com/watch?v=NQzlTWjz8a0&t=214s',
      'video_id': 'NQzlTWjz8a0'},
     {'author': 'Web Development Experts',
      'channel': 'Web Development Experts',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:29](https://www.youtube.com/watch?v=uwU6N7flfU8&t=29s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'And you get your own booking website. Every rental business on Weekly Car '
              'Rental Software >>.',
      'timestamp': 29,
      'timestamp_label': '[00:00:29]',
      'timestamp_seconds': 29,
      'tip': 'And you get your own booking website. Every rental business on Weekly Car Rental '
             'Software >>.',
      'title': 'Car Rental Software Demo - WCR Austarlia (Web Development Experts)',
      'url': 'https://www.youtube.com/watch?v=uwU6N7flfU8&t=29s',
      'video_id': 'uwU6N7flfU8'},
     {'author': 'Bluebird Auto Rental Systems',
      'channel': 'Bluebird Auto Rental Systems',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:39](https://www.youtube.com/watch?v=1Bh5Wvanfss&t=39s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Afternoon, gone. Caught before it  ever happens. At the counter, a guided flow '
              'walks you from customer to car.  License, rates, add-ons.',
      'timestamp': 39,
      'timestamp_label': '[00:00:39]',
      'timestamp_seconds': 39,
      'tip': 'Afternoon, gone. Caught before it  ever happens. At the counter, a guided flow '
             'walks you from customer to car.  License, rates, add-ons.',
      'title': 'Introducing RentWorks Plus | Cloud Car Rental Management Software (Bluebird '
               'Auto Rental Systems)',
      'url': 'https://www.youtube.com/watch?v=1Bh5Wvanfss&t=39s',
      'video_id': '1Bh5Wvanfss'},
     {'author': 'FleetBold',
      'channel': 'FleetBold',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:35](https://www.youtube.com/watch?v=fNmLkHa3FiA&t=95s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, instead of juggling multiple tools, everything starts coming together '
              "inside of one system. And then, there's something most hosts have never really "
              'had before, and that is a real website, okay?',
      'timestamp': 95,
      'timestamp_label': '[00:01:35]',
      'timestamp_seconds': 95,
      'tip': 'So, instead of juggling multiple tools, everything starts coming together inside '
             "of one system. And then, there's something most hosts have never really had "
             'before, and that is a real website, okay?',
      'title': 'FleetBold Car Rental Software  | Build Your Own Rental Website, Take Bookings '
               '& Manage Your Fleet (FleetBold)',
      'url': 'https://www.youtube.com/watch?v=fNmLkHa3FiA&t=95s',
      'video_id': 'fNmLkHa3FiA'},
     {'author': 'Yusuf Benallal',
      'channel': 'Yusuf Benallal',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:26](https://www.youtube.com/watch?v=xrJ-xGav6Xo&t=206s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "You're going to be paying $2,993. 81 just on the on the actual car note. That "
              "doesn't, you know, the insurance. So, you might be you're going to be at $3,500 "
              'a month for this 2025 Calc Escalade in order for you to use this for Uber '
              'Black.',
      'timestamp': 206,
      'timestamp_label': '[00:03:26]',
      'timestamp_seconds': 206,
      'tip': "You're going to be paying $2,993. 81 just on the on the actual car note. That "
             "doesn't, you know, the insurance. So, you might be you're going to be at $3,500 "
             'a month for this 2025 Calc Escalade in order for you to use this for Uber Black.',
      'title': 'NYC Uber Driver SHOCKED his new Cadillac Escalade will be $3,500 a month! 😱🙃 '
               'Expensive SUV to drive😩 (Yusuf Benallal)',
      'url': 'https://www.youtube.com/watch?v=xrJ-xGav6Xo&t=206s',
      'video_id': 'xrJ-xGav6Xo'},
     {'author': 'The Rideshare Guy',
      'channel': 'The Rideshare Guy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:32](https://www.youtube.com/watch?v=F6U-c7e7avY&t=152s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Of policy so with a commercial insurance policy you can have multiple drivers '
              'on that vehicle you can do rides off the app so you could just go and give a '
              'ride.',
      'timestamp': 152,
      'timestamp_label': '[00:02:32]',
      'timestamp_seconds': 152,
      'tip': 'Of policy so with a commercial insurance policy you can have multiple drivers on '
             'that vehicle you can do rides off the app so you could just go and give a ride.',
      'title': 'What’s the difference between rideshare insurance and commercial insurance? '
               '(The Rideshare Guy)',
      'url': 'https://www.youtube.com/watch?v=F6U-c7e7avY&t=152s',
      'video_id': 'F6U-c7e7avY'},
     {'author': 'Conrad Layn',
      'channel': 'Conrad Layn',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:07](https://www.youtube.com/watch?v=ePOpmhuk-EQ&t=487s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'For proof one two three sata drive for uber lyft amazon flex grab pub instacart '
              "they're driving to make money that's when they usually get insurance that.",
      'timestamp': 487,
      'timestamp_label': '[00:08:07]',
      'timestamp_seconds': 487,
      'tip': 'For proof one two three sata drive for uber lyft amazon flex grab pub instacart '
             "they're driving to make money that's when they usually get insurance that.",
      'title': 'How To Get Commercial PERIOD X HyreCar Insurance 💡 (Conrad Layn)',
      'url': 'https://www.youtube.com/watch?v=ePOpmhuk-EQ&t=487s',
      'video_id': 'ePOpmhuk-EQ'},
     {'author': 'Demario Mccowan',
      'channel': 'Demario Mccowan',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:53:11](https://www.youtube.com/watch?v=-HtlfCgxxtg&t=3191s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "There's that, too, for the people that want to play it safe. So, we do we "
              'require insurance or we have Uber and Lift drivers that need to have insurance. '
              'And we actually worked on developing an app that sends you. So, basically, say '
              "that you have you're the renter.",
      'timestamp': 3191,
      'timestamp_label': '[00:53:11]',
      'timestamp_seconds': 3191,
      'tip': "There's that, too, for the people that want to play it safe. So, we do we "
             'require insurance or we have Uber and Lift drivers that need to have insurance. '
             'And we actually worked on developing an app that sends you. So, basically, say '
             "that you have you're the renter.",
      'title': 'How I Left Turo and Built a 500-Car Private Rental Empire (No Platform Needed) '
               '(Demario Mccowan)',
      'url': 'https://www.youtube.com/watch?v=-HtlfCgxxtg&t=3191s',
      'video_id': '-HtlfCgxxtg'},
     {'author': 'King of Rentals',
      'channel': 'King of Rentals',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:11](https://www.youtube.com/watch?v=OBbGsDAi0xA&t=611s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'You need a booking software, which means you need driver verification. Driver '
              'verification is like a background check. You need the ability sell insurance to '
              "the drivers in case they don't have any. So, you need insurance plus insurance "
              'check.',
      'timestamp': 611,
      'timestamp_label': '[00:10:11]',
      'timestamp_seconds': 611,
      'tip': 'You need a booking software, which means you need driver verification. Driver '
             'verification is like a background check. You need the ability sell insurance to '
             "the drivers in case they don't have any. So, you need insurance plus insurance "
             'check.',
      'title': 'How to build car rental fleet (STEP BY STEP)!! (King of Rentals)',
      'url': 'https://www.youtube.com/watch?v=OBbGsDAi0xA&t=611s',
      'video_id': 'OBbGsDAi0xA'},
     {'author': 'ESCAPE THE MATRIX',
      'channel': 'ESCAPE THE MATRIX',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:25](https://www.youtube.com/watch?v=Y8ppyxLqw9E&t=25s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Secret way to get tlc plates so make sure you follow along till the end of the '
              'video alright so first of all before you do get tlc plates you gotta ask.',
      'timestamp': 25,
      'timestamp_label': '[00:00:25]',
      'timestamp_seconds': 25,
      'tip': 'Secret way to get tlc plates so make sure you follow along till the end of the '
             'video alright so first of all before you do get tlc plates you gotta ask.',
      'title': 'How to get TLC plates in NYC 2022 (ESCAPE THE MATRIX)',
      'url': 'https://www.youtube.com/watch?v=Y8ppyxLqw9E&t=25s',
      'video_id': 'Y8ppyxLqw9E'},
     {'author': 'Car Sharing Jho',
      'channel': 'Car Sharing Jho',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:42](https://www.youtube.com/watch?v=1_yscjNU-oM&t=102s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Sometimes there um there is screws down here so you just gotta be careful not '
              "to pry it off completely without checking for screws and we're gonna take this "
              'off be sure to keep all your screws together like a little magnetic.',
      'timestamp': 102,
      'timestamp_label': '[00:01:42]',
      'timestamp_seconds': 102,
      'tip': 'Sometimes there um there is screws down here so you just gotta be careful not to '
             "pry it off completely without checking for screws and we're gonna take this off "
             'be sure to keep all your screws together like a little magnetic.',
      'title': 'How To Install TrackMateGPS Tracker and Kill Switch for Turo Cars (Car Sharing '
               'Jho)',
      'url': 'https://www.youtube.com/watch?v=1_yscjNU-oM&t=102s',
      'video_id': '1_yscjNU-oM'}],
 5: [{'author': 'TJackk',
      'channel': 'TJackk',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:26](https://www.youtube.com/watch?v=E0a86uKzcuk&t=146s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Infiniti QX80 because I wanted her to come join the business. I was making way '
              'more money than she was working or making at her job. So, I\'m like, "Hey, you '
              'come make this money, too." I\'m like, "No, we not making that same mistake of '
              'buying a mediumsiz SUV.',
      'timestamp': 146,
      'timestamp_label': '[00:02:26]',
      'timestamp_seconds': 146,
      'tip': 'Infiniti QX80 because I wanted her to come join the business. I was making way '
             'more money than she was working or making at her job. So, I\'m like, "Hey, you '
             'come make this money, too." I\'m like, "No, we not making that same mistake of '
             'buying a mediumsiz SUV.',
      'title': 'After Owning Multiple Uber Black SUVs — Here’s What Works Best (TJackk)',
      'url': 'https://www.youtube.com/watch?v=E0a86uKzcuk&t=146s',
      'video_id': 'E0a86uKzcuk'},
     {'author': 'Etienne Elsaesser',
      'channel': 'Etienne Elsaesser',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:24](https://www.youtube.com/watch?v=l8b3Oi2g48I&t=624s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'re driving DoorDash or when they're driving the cars for personal use. Graves "
              'Amendment, and having those embedded into your rental agreement properly, as '
              'well as the whole structure surrounding this business model.',
      'timestamp': 624,
      'timestamp_label': '[00:10:24]',
      'timestamp_seconds': 624,
      'tip': "'re driving DoorDash or when they're driving the cars for personal use. Graves "
             'Amendment, and having those embedded into your rental agreement properly, as '
             'well as the whole structure surrounding this business model.',
      'title': 'Why Gig Drivers Pay More Than Turo Guests (Etienne Elsaesser)',
      'url': 'https://www.youtube.com/watch?v=l8b3Oi2g48I&t=624s',
      'video_id': 'l8b3Oi2g48I'},
     {'author': 'Demario Mccowan',
      'channel': 'Demario Mccowan',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:16](https://www.youtube.com/watch?v=b4HG8nxaQlU&t=76s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Turo and we're getting burned out or not making enough money. So, by the end of "
              "the session, you'll know how to start earning with zero inventory and avoid "
              'some of these major mistakes and potentially turn this into a six-figure '
              'business.',
      'timestamp': 76,
      'timestamp_label': '[00:01:16]',
      'timestamp_seconds': 76,
      'tip': "Turo and we're getting burned out or not making enough money. So, by the end of "
             "the session, you'll know how to start earning with zero inventory and avoid some "
             'of these major mistakes and potentially turn this into a six-figure business.',
      'title': 'How to Start a Car Rental Business with ZERO Cars | Turo Co-Hosting '
               'Masterclass (Demario Mccowan)',
      'url': 'https://www.youtube.com/watch?v=b4HG8nxaQlU&t=76s',
      'video_id': 'b4HG8nxaQlU'},
     {'author': 'NutriVera',
      'channel': 'NutriVera',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:06](https://www.youtube.com/watch?v=vSUUOYMrXjw&t=186s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Airport coverage  they publicize is narrower though. Now a few quick tips so '
              'you avoid surprise charges. First, compare an all-in black car quote.',
      'timestamp': 186,
      'timestamp_label': '[00:03:06]',
      'timestamp_seconds': 186,
      'tip': 'Airport coverage  they publicize is narrower though. Now a few quick tips so you '
             'avoid surprise charges. First, compare an all-in black car quote.',
      'title': 'Black Car Service vs Uber Black in NYC 2026: Price, Surge, Reliability '
               '(NutriVera)',
      'url': 'https://www.youtube.com/watch?v=vSUUOYMrXjw&t=186s',
      'video_id': 'vSUUOYMrXjw'},
     {'author': 'Fares and Frustrations',
      'channel': 'Fares and Frustrations',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:30](https://www.youtube.com/watch?v=_UpXw8QDal8&t=150s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Not just that fake overnight social media version of growth. The real growth '
              'can be slow. It can be one booking, then another booking, then learning from a '
              'mistake, then putting your money back into the business.',
      'timestamp': 150,
      'timestamp_label': '[00:02:30]',
      'timestamp_seconds': 150,
      'tip': 'Not just that fake overnight social media version of growth. The real growth can '
             'be slow. It can be one booking, then another booking, then learning from a '
             'mistake, then putting your money back into the business.',
      'title': 'Uber Black to Private: Why the Uber-Only Mindset Is Dying (Fares and '
               'Frustrations)',
      'url': 'https://www.youtube.com/watch?v=_UpXw8QDal8&t=150s',
      'video_id': '_UpXw8QDal8'},
     {'author': 'King of Rentals',
      'channel': 'King of Rentals',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:38](https://www.youtube.com/watch?v=zIGomHkXMms&t=698s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Best part about this is if you're making sure you're buying the right car, all "
              "you're doing is collecting the money and then reinvesting it back into the "
              "business to crazy rapidly expand. The biggest mistakes I've seen by far that "
              'people make are insurance.',
      'timestamp': 698,
      'timestamp_label': '[00:11:38]',
      'timestamp_seconds': 698,
      'tip': "Best part about this is if you're making sure you're buying the right car, all "
             "you're doing is collecting the money and then reinvesting it back into the "
             "business to crazy rapidly expand. The biggest mistakes I've seen by far that "
             'people make are insurance.',
      'title': 'The #1 Car Rental Strategy Right Now (Rideshare Rentals)! (King of Rentals)',
      'url': 'https://www.youtube.com/watch?v=zIGomHkXMms&t=698s',
      'video_id': 'zIGomHkXMms'},
     {'author': 'Florida Trust, Real Estate, Probate, & Foreclosure',
      'channel': 'Florida Trust, Real Estate, Probate, & Foreclosure',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:35](https://www.youtube.com/watch?v=28RNMngtROc&t=575s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'They do not define the terms business or trade and in fact Apple lease site to '
              'a different definition of that term than we do. I think inherently that creates '
              'a dispute of fact, but they site to the internal revenue code.',
      'timestamp': 575,
      'timestamp_label': '[00:09:35]',
      'timestamp_seconds': 575,
      'tip': 'They do not define the terms business or trade and in fact Apple lease site to a '
             'different definition of that term than we do. I think inherently that creates a '
             'dispute of fact, but they site to the internal revenue code.',
      'title': '🔍 Turo Peer-to-Peer Car Sharing Graves Amendment Liability | Case No. 24-0266 '
               '| FL Appellate (Florida Trust, Real Estate, Probate, & Foreclosure)',
      'url': 'https://www.youtube.com/watch?v=28RNMngtROc&t=575s',
      'video_id': '28RNMngtROc'},
     {'author': 'GigCalifornia',
      'channel': 'GigCalifornia',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:25](https://www.youtube.com/watch?v=OMCcnT_Aer8&t=205s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "And I don't want to even like decline the ride because I want to improve my "
              'acceptance rate. How to know like what what what would be the pickup time? The '
              'airport is full of black cars.',
      'timestamp': 205,
      'timestamp_label': '[00:03:25]',
      'timestamp_seconds': 205,
      'tip': "And I don't want to even like decline the ride because I want to improve my "
             'acceptance rate. How to know like what what what would be the pickup time? The '
             'airport is full of black cars.',
      'title': '🚘 Uber & Lyft Black SUV | 15-Hour Shift in San Francisco | Real Driver '
               'Experience (GigCalifornia)',
      'url': 'https://www.youtube.com/watch?v=OMCcnT_Aer8&t=205s',
      'video_id': 'OMCcnT_Aer8'},
     {'author': 'Brandon Ascari',
      'channel': 'Brandon Ascari',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:16](https://www.youtube.com/watch?v=whkUEOIjybM&t=556s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'We bought it because we knew that it had the engine recall and the person who '
              'was selling it had just done it literally the day before he sold it to us. So, '
              'it had a brand new engine in it, which we thought was going to be no problem at '
              'all.',
      'timestamp': 556,
      'timestamp_label': '[00:09:16]',
      'timestamp_seconds': 556,
      'tip': 'We bought it because we knew that it had the engine recall and the person who '
             'was selling it had just done it literally the day before he sold it to us. So, '
             'it had a brand new engine in it, which we thought was going to be no problem at '
             'all.',
      'title': 'How I Scaled My Turo Fleet to 15 Cars (The Remote CEO Blueprint) (Brandon '
               'Ascari)',
      'url': 'https://www.youtube.com/watch?v=whkUEOIjybM&t=556s',
      'video_id': 'whkUEOIjybM'},
     {'author': 'DGOTEXOTICS',
      'channel': 'DGOTEXOTICS',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:05](https://www.youtube.com/watch?v=7d0XER3HAlQ&t=425s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "You think you're worried about buying more cars, when in reality you should be "
              'worried about secur- ing more cars. How do I make sure that these vehicles are '
              'covered or what is my risk?',
      'timestamp': 425,
      'timestamp_label': '[00:07:05]',
      'timestamp_seconds': 425,
      'tip': "You think you're worried about buying more cars, when in reality you should be "
             'worried about secur- ing more cars. How do I make sure that these vehicles are '
             'covered or what is my risk?',
      'title': 'How To Insure Your Rental Car Fleet 🚘📈 (DGOTEXOTICS)',
      'url': 'https://www.youtube.com/watch?v=7d0XER3HAlQ&t=425s',
      'video_id': '7d0XER3HAlQ'},
     {'author': 'Delano Green',
      'channel': 'Delano Green',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:01](https://www.youtube.com/watch?v=ziuX0-egB7Y&t=601s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "So, if you're basically knowing the the the stress you can deal with, you have "
              'to learn how to solve it. And like this is the last problem I actually dealt '
              "with. This is like a bonus one cuz I'm about to end this video right now.",
      'timestamp': 601,
      'timestamp_label': '[00:10:01]',
      'timestamp_seconds': 601,
      'tip': "So, if you're basically knowing the the the stress you can deal with, you have "
             'to learn how to solve it. And like this is the last problem I actually dealt '
             "with. This is like a bonus one cuz I'm about to end this video right now.",
      'title': 'How to Cohost 99 Rental Cars on Turo (The Systems I Used to Scale) (Delano '
               'Green)',
      'url': 'https://www.youtube.com/watch?v=ziuX0-egB7Y&t=601s',
      'video_id': 'ziuX0-egB7Y'},
     {'author': 'BusinessRocket',
      'channel': 'BusinessRocket',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:46](https://www.youtube.com/watch?v=s51s14MY4hI&t=106s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Credit and being able to have flexibility to sell the business as an asset in '
              'the future hopefully this information was helpful please leave your comments '
              "below we'll love to address all of them and we'll make sure we can help you any "
              'way we can till next time.',
      'timestamp': 106,
      'timestamp_label': '[00:01:46]',
      'timestamp_seconds': 106,
      'tip': 'Credit and being able to have flexibility to sell the business as an asset in '
             'the future hopefully this information was helpful please leave your comments '
             "below we'll love to address all of them and we'll make sure we can help you any "
             'way we can till next time.',
      'title': 'TCP License: Avoid These 3 Pitfalls for a Successful TCP License | Essential '
               'Tips for new TCP Permit (BusinessRocket)',
      'url': 'https://www.youtube.com/watch?v=s51s14MY4hI&t=106s',
      'video_id': 's51s14MY4hI'},
     {'author': 'Mr. RTB',
      'channel': 'Mr. RTB',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:28](https://www.youtube.com/watch?v=JJrV3_EbmeE&t=328s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'That is absolutely not not going to happen you have to be looking to play the '
              'long game in this Logistics business so keep running to the bag or rtb like '
              "share and comment and let's get this money.",
      'timestamp': 328,
      'timestamp_label': '[00:05:28]',
      'timestamp_seconds': 328,
      'tip': 'That is absolutely not not going to happen you have to be looking to play the '
             'long game in this Logistics business so keep running to the bag or rtb like '
             "share and comment and let's get this money.",
      'title': 'The TRUTH about the Cargo van business! (Mr. RTB)',
      'url': 'https://www.youtube.com/watch?v=JJrV3_EbmeE&t=328s',
      'video_id': 'JJrV3_EbmeE'},
     {'author': 'TJackk',
      'channel': 'TJackk',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:51](https://www.youtube.com/watch?v=YIgqF31H2Nc&t=291s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "And not only that, y'all, you able to learn from all of this, which that goes "
              'into my next lesson, which is the business side that it taught me. You know, '
              'this business taught me patience, leadership, communication, trust, problem '
              'solving.',
      'timestamp': 291,
      'timestamp_label': '[00:04:51]',
      'timestamp_seconds': 291,
      'tip': "And not only that, y'all, you able to learn from all of this, which that goes "
             'into my next lesson, which is the business side that it taught me. You know, '
             'this business taught me patience, leadership, communication, trust, problem '
             'solving.',
      'title': 'I Wish I Started My Uber Black Fleet Sooner (TJackk)',
      'url': 'https://www.youtube.com/watch?v=YIgqF31H2Nc&t=291s',
      'video_id': 'YIgqF31H2Nc'},
     {'author': 'Mike_Thebusinessman',
      'channel': 'Mike_Thebusinessman',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:17:04](https://www.youtube.com/watch?v=XGJGK0LyMno&t=1024s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Make these videos for you guys okay so um appreciate you guys thank you very '
              "much and I'll see you guys on the other side of success.",
      'timestamp': 1024,
      'timestamp_label': '[00:17:04]',
      'timestamp_seconds': 1024,
      'tip': 'Make these videos for you guys okay so um appreciate you guys thank you very '
             "much and I'll see you guys on the other side of success.",
      'title': 'How To Get Commercial Fleet  Insurance For Car Rental Business '
               '(Mike_Thebusinessman)',
      'url': 'https://www.youtube.com/watch?v=XGJGK0LyMno&t=1024s',
      'video_id': 'XGJGK0LyMno'}],
 6: [{'author': 'Paydirt',
      'channel': 'Paydirt',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:08](https://www.youtube.com/watch?v=BCGe4sRsiVE&t=128s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'TLC rental companies in the city. Many new drivers rent at first to test the '
              "waters before buying. Step seven, pass Uber's background screening, upload your "
              'documents, and go online. Here are three tips tailored to New York City. First, '
              'learn the airport game.',
      'timestamp': 128,
      'timestamp_label': '[00:02:08]',
      'timestamp_seconds': 128,
      'tip': 'TLC rental companies in the city. Many new drivers rent at first to test the '
             "waters before buying. Step seven, pass Uber's background screening, upload your "
             'documents, and go online. Here are three tips tailored to New York City. First, '
             'learn the airport game.',
      'title': '$37.44/Hour: How to Become an Uber Driver in New York City (2026) (Paydirt)',
      'url': 'https://www.youtube.com/watch?v=BCGe4sRsiVE&t=128s',
      'video_id': 'BCGe4sRsiVE'},
     {'author': 'The Rideshare CEO',
      'channel': 'The Rideshare CEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:45](https://www.youtube.com/watch?v=Ap3NIbDoDDg&t=45s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Because it covers the most jobs. Comfort, cargo, and airport runs all in one '
              'car. Every figure in this video comes from the research we have already '
              "published. And the same rule applies at the end. Check your city's list in the "
              'driver app before you buy.',
      'timestamp': 45,
      'timestamp_label': '[00:00:45]',
      'timestamp_seconds': 45,
      'tip': 'Because it covers the most jobs. Comfort, cargo, and airport runs all in one '
             'car. Every figure in this video comes from the research we have already '
             "published. And the same rule applies at the end. Check your city's list in the "
             'driver app before you buy.',
      'title': 'Best Cars for Rideshare Drivers: Hybrid Edition (The Rideshare CEO)',
      'url': 'https://www.youtube.com/watch?v=Ap3NIbDoDDg&t=45s',
      'video_id': 'Ap3NIbDoDDg'},
     {'author': 'TJackk',
      'channel': 'TJackk',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:18:14](https://www.youtube.com/watch?v=GBM9d0WqM-0&t=1094s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "I don't recommend you go with uh Progressive. So, what I'll do, let me see. And "
              "then it'll be like a a a bunch of list or a list of of different ones. Like I "
              'think Geico is now offering commercial auto insurance for black car. They '
              "wasn't whenever I first started.",
      'timestamp': 1094,
      'timestamp_label': '[00:18:14]',
      'timestamp_seconds': 1094,
      'tip': "I don't recommend you go with uh Progressive. So, what I'll do, let me see. And "
             "then it'll be like a a a bunch of list or a list of of different ones. Like I "
             "think Geico is now offering commercial auto insurance for black car. They wasn't "
             'whenever I first started.',
      'title': 'How To Start an Uber Black Fleet in 2026 (TJackk)',
      'url': 'https://www.youtube.com/watch?v=GBM9d0WqM-0&t=1094s',
      'video_id': 'GBM9d0WqM-0'},
     {'author': 'DOUBLE DOWN Podcast',
      'channel': 'DOUBLE DOWN Podcast',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:54:12](https://www.youtube.com/watch?v=UCJIebqFEj0&t=3252s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "So, it's basically what's called a business in a box. Um somebody would give me "
              "120,000 and I'm sourcing all the vehicles for them. I'm putting all of these "
              "paying renters in the car. Um I'm building out the whole back end of the "
              'business.',
      'timestamp': 3252,
      'timestamp_label': '[00:54:12]',
      'timestamp_seconds': 3252,
      'tip': "So, it's basically what's called a business in a box. Um somebody would give me "
             "120,000 and I'm sourcing all the vehicles for them. I'm putting all of these "
             "paying renters in the car. Um I'm building out the whole back end of the "
             'business.',
      'title': 'How He Built a 70+ Car  Rental Fleet Making $105K/Month (Rental Car King) '
               '(DOUBLE DOWN Podcast)',
      'url': 'https://www.youtube.com/watch?v=UCJIebqFEj0&t=3252s',
      'video_id': 'UCJIebqFEj0'},
     {'author': 'Delano Green',
      'channel': 'Delano Green',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=iN4oOhcGHDg&t=21s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "I have them on my notes here, so what I'll basically do is I'll just give you "
              "the points first and then I'll elaborate on all of them. So the first one is "
              'the buying cars before building a demand.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': "I have them on my notes here, so what I'll basically do is I'll just give you "
             "the points first and then I'll elaborate on all of them. So the first one is the "
             'buying cars before building a demand.',
      'title': '3 Mistakes that kill Most Car rental/Turo Businesses Before They Start (Delano '
               'Green)',
      'url': 'https://www.youtube.com/watch?v=iN4oOhcGHDg&t=21s',
      'video_id': 'iN4oOhcGHDg'},
     {'author': 'Kel King',
      'channel': 'Kel King',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:48](https://www.youtube.com/watch?v=swveqE_MJY0&t=468s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'So if a renter stops paying or goes quiet, you can find it and disable it. '
              "That's not paranoia, that's being a real business owner. So screen your renters "
              'and get it in writing. A signed agreement, a deposit, a real conversation.',
      'timestamp': 468,
      'timestamp_label': '[00:07:48]',
      'timestamp_seconds': 468,
      'tip': 'So if a renter stops paying or goes quiet, you can find it and disable it. '
             "That's not paranoia, that's being a real business owner. So screen your renters "
             'and get it in writing. A signed agreement, a deposit, a real conversation.',
      'title': "I Bought a $5K Car for My Rental Car Business- Here's What It Made (Kel King)",
      'url': 'https://www.youtube.com/watch?v=swveqE_MJY0&t=468s',
      'video_id': 'swveqE_MJY0'},
     {'author': 'ESCAPE THE MATRIX',
      'channel': 'ESCAPE THE MATRIX',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:28](https://www.youtube.com/watch?v=IjuFeAo7KGE&t=28s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Out my other video on what cars is qualify for Uber black let me start off in '
              "Reverse alphabetical order so the first car that we're going to start off.",
      'timestamp': 28,
      'timestamp_label': '[00:00:28]',
      'timestamp_seconds': 28,
      'tip': 'Out my other video on what cars is qualify for Uber black let me start off in '
             "Reverse alphabetical order so the first car that we're going to start off.",
      'title': 'what vehicles qualify for UBER BLACK SUV? (ESCAPE THE MATRIX)',
      'url': 'https://www.youtube.com/watch?v=IjuFeAo7KGE&t=28s',
      'video_id': 'IjuFeAo7KGE'},
     {'author': 'TJackk',
      'channel': 'TJackk',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:18](https://www.youtube.com/watch?v=iCdSnX4vLHI&t=318s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'all don't just sit around waiting on blacks cuz sometimes a comfort would "
              'direct you or lead you to a black. So, my first ride was like 34, 35 bucks to '
              'the airport. I took tolls, so it was kind of fast.',
      'timestamp': 318,
      'timestamp_label': '[00:05:18]',
      'timestamp_seconds': 318,
      'tip': "'all don't just sit around waiting on blacks cuz sometimes a comfort would "
             'direct you or lead you to a black. So, my first ride was like 34, 35 bucks to '
             'the airport. I took tolls, so it was kind of fast.',
      'title': 'You Can STILL Make $300-$500 a Day Driving Uber Black (TJackk)',
      'url': 'https://www.youtube.com/watch?v=iCdSnX4vLHI&t=318s',
      'video_id': 'iCdSnX4vLHI'},
     {'author': 'Peak Auto Academy',
      'channel': 'Peak Auto Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:03](https://www.youtube.com/watch?v=3kqux9OEEfY&t=183s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "They put in 44,680 to start. On an annualized basis, if you're doing your math, "
              "that's a 23% return on your money. Find me another place that you can do that. "
              "So, if you're interested in listing your vehicle at Peak Auto, head over to "
              'peakautorentals.',
      'timestamp': 183,
      'timestamp_label': '[00:03:03]',
      'timestamp_seconds': 183,
      'tip': "They put in 44,680 to start. On an annualized basis, if you're doing your math, "
             "that's a 23% return on your money. Find me another place that you can do that. "
             "So, if you're interested in listing your vehicle at Peak Auto, head over to "
             'peakautorentals.',
      'title': 'How Turo Hosts Make Money Doing No Work (Peak Auto Academy)',
      'url': 'https://www.youtube.com/watch?v=3kqux9OEEfY&t=183s',
      'video_id': '3kqux9OEEfY'},
     {'author': 'Pitstop to Profits',
      'channel': 'Pitstop to Profits',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:44](https://www.youtube.com/watch?v=x4wy8hXqVbk&t=404s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "So our first wire is off our tracker. It's going to be our red wire, right? "
              "This is our inline fuse just so that pops before so you don't burn something "
              "down or tear something up. We'll get this one out the way. That's connected to "
              'this pink wire here.',
      'timestamp': 404,
      'timestamp_label': '[00:06:44]',
      'timestamp_seconds': 404,
      'tip': "So our first wire is off our tracker. It's going to be our red wire, right? This "
             "is our inline fuse just so that pops before so you don't burn something down or "
             "tear something up. We'll get this one out the way. That's connected to this pink "
             'wire here.',
      'title': 'How I Installed a Goldstar GPS Tracker and Kill Switch In My Rental Car Fleet '
               '(Pitstop to Profits)',
      'url': 'https://www.youtube.com/watch?v=x4wy8hXqVbk&t=404s',
      'video_id': 'x4wy8hXqVbk'},
     {'author': 'Trackhawk GPS',
      'channel': 'Trackhawk GPS',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:41](https://www.youtube.com/watch?v=cLo7rU35m3U&t=41s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Things first uh let's remove the uh fuse box this is a 2024 Challenger Dodge "
              "Challenger jailbreak so uh what we're going to do here is that we're going to "
              'catch the signal for the starter under the fuse box so we remove the fuse box '
              'at this point.',
      'timestamp': 41,
      'timestamp_label': '[00:00:41]',
      'timestamp_seconds': 41,
      'tip': "Things first uh let's remove the uh fuse box this is a 2024 Challenger Dodge "
             "Challenger jailbreak so uh what we're going to do here is that we're going to "
             'catch the signal for the starter under the fuse box so we remove the fuse box at '
             'this point.',
      'title': 'Trackhawk GPS Kill Switch Installation - Best Turo and Car Rental GPS Tracker '
               '(Trackhawk GPS)',
      'url': 'https://www.youtube.com/watch?v=cLo7rU35m3U&t=41s',
      'video_id': 'cLo7rU35m3U'},
     {'author': 'Luxury Transportation Academy / Podcast',
      'channel': 'Luxury Transportation Academy / Podcast',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:19](https://www.youtube.com/watch?v=yg-RtCxYcG8&t=499s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'It could be a It could be just essentially an email list. But the reality is as '
              "you scale and grow your company with the right tools, it'll help you maintain "
              'it, but also grow it and see the growth based off the data, right?',
      'timestamp': 499,
      'timestamp_label': '[00:08:19]',
      'timestamp_seconds': 499,
      'tip': 'It could be a It could be just essentially an email list. But the reality is as '
             "you scale and grow your company with the right tools, it'll help you maintain "
             'it, but also grow it and see the growth based off the data, right?',
      'title': 'Chauffeur to CEO: The Blueprint to $250K/Year in Luxury Transportation (Luxury '
               'Transportation Academy / Podcast)',
      'url': 'https://www.youtube.com/watch?v=yg-RtCxYcG8&t=499s',
      'video_id': 'yg-RtCxYcG8'},
     {'author': 'ESCAPE THE MATRIX',
      'channel': 'ESCAPE THE MATRIX',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:49](https://www.youtube.com/watch?v=l1oXFuye_F0&t=109s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Mercedes-Benz and Mercedes-Benz has the GLS, which is a car actually I would '
              'also not recommend because just like the BMW X7, this is a car that I have a '
              'feeling in the future it will no longer qualify as a black SUV.',
      'timestamp': 109,
      'timestamp_label': '[00:01:49]',
      'timestamp_seconds': 109,
      'tip': 'Mercedes-Benz and Mercedes-Benz has the GLS, which is a car actually I would '
             'also not recommend because just like the BMW X7, this is a car that I have a '
             'feeling in the future it will no longer qualify as a black SUV.',
      'title': "Best Uber Black SUV Cars in NYC (2026) | What I'd Actually Buy (ESCAPE THE "
               'MATRIX)',
      'url': 'https://www.youtube.com/watch?v=l1oXFuye_F0&t=109s',
      'video_id': 'l1oXFuye_F0'},
     {'author': 'Brandon Duff',
      'channel': 'Brandon Duff',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:41](https://www.youtube.com/watch?v=c8x4Whu0UNg&t=161s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Toyota Prius 2018 white I just like to put a description here to kind of make '
              'it a lot easier to pick from the list if I only had this when I pull it later '
              "it's going to be very hard to figure out which one is which so 2018 Toyota.",
      'timestamp': 161,
      'timestamp_label': '[00:02:41]',
      'timestamp_seconds': 161,
      'tip': 'Toyota Prius 2018 white I just like to put a description here to kind of make it '
             "a lot easier to pick from the list if I only had this when I pull it later it's "
             'going to be very hard to figure out which one is which so 2018 Toyota.',
      'title': 'The Best Fleet Management Software - Walkthrough of Fleetwire (Brandon Duff)',
      'url': 'https://www.youtube.com/watch?v=c8x4Whu0UNg&t=161s',
      'video_id': 'c8x4Whu0UNg'},
     {'author': 'King of Rentals',
      'channel': 'King of Rentals',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:01](https://www.youtube.com/watch?v=QpyPtquGmrk&t=241s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Completely get then don't put a tracker in it and let the insurance companies "
              "deal with it but I think it's still a good solution for a lot of people so "
              'thanks you for watching and this is the little device may just save your life.',
      'timestamp': 241,
      'timestamp_label': '[00:04:01]',
      'timestamp_seconds': 241,
      'tip': "Completely get then don't put a tracker in it and let the insurance companies "
             "deal with it but I think it's still a good solution for a lot of people so "
             'thanks you for watching and this is the little device may just save your life.',
      'title': 'The Best Car Tracking Device: Bouncie GPS!!! (King of Rentals)',
      'url': 'https://www.youtube.com/watch?v=QpyPtquGmrk&t=241s',
      'video_id': 'QpyPtquGmrk'}],
 7: [{'author': 'Fares and Frustrations',
      'channel': 'Fares and Frustrations',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:06](https://www.youtube.com/watch?v=BgQ493l7UuE&t=546s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Tuesday comes around, I show up. And the system already told me whether his '
              "flight is on time, early, or delayed, and before I even left the house. That's "
              'the difference between running an actual chauffeur business and running a side '
              'hustle.',
      'timestamp': 546,
      'timestamp_label': '[00:09:06]',
      'timestamp_seconds': 546,
      'tip': 'Tuesday comes around, I show up. And the system already told me whether his '
             "flight is on time, early, or delayed, and before I even left the house. That's "
             'the difference between running an actual chauffeur business and running a side '
             'hustle.',
      'title': 'Limo Anywhere: The Software That Could Change Your Black Car Business (Fares '
               'and Frustrations)',
      'url': 'https://www.youtube.com/watch?v=BgQ493l7UuE&t=546s',
      'video_id': 'BgQ493l7UuE'},
     {'author': 'Elite Executive Limos',
      'channel': 'Elite Executive Limos',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:16](https://www.youtube.com/watch?v=nftoRdt_OUY&t=16s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Is bigger than most people realize. Let's break it down. With Uber Black, "
              "you're booking  through an app. The driver accepts your request or.",
      'timestamp': 16,
      'timestamp_label': '[00:00:16]',
      'timestamp_seconds': 16,
      'tip': "Is bigger than most people realize. Let's break it down. With Uber Black, you're "
             'booking  through an app. The driver accepts your request or.',
      'title': "Uber Black vs Private Chauffeur – What's the Real Difference? (South Florida) "
               '(Elite Executive Limos)',
      'url': 'https://www.youtube.com/watch?v=nftoRdt_OUY&t=16s',
      'video_id': 'nftoRdt_OUY'},
     {'author': 'How To Mr',
      'channel': 'How To Mr',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:17](https://www.youtube.com/watch?v=reD8ApAoQBQ&t=77s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'The platform is also cloud-based, so you and your team can access it anywhere, '
              "whether you're in the office or on the go. For customers, the online booking "
              'process feels smooth and professional, which can boost trust and conversion '
              'rates. But there are some downsides.',
      'timestamp': 77,
      'timestamp_label': '[00:01:17]',
      'timestamp_seconds': 77,
      'tip': 'The platform is also cloud-based, so you and your team can access it anywhere, '
             "whether you're in the office or on the go. For customers, the online booking "
             'process feels smooth and professional, which can boost trust and conversion '
             'rates. But there are some downsides.',
      'title': 'HQ Rental Software | Honest Review (ALL YOU NEED TO KNOW) (How To Mr)',
      'url': 'https://www.youtube.com/watch?v=reD8ApAoQBQ&t=77s',
      'video_id': 'reD8ApAoQBQ'},
     {'author': 'King of Rentals',
      'channel': 'King of Rentals',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:11](https://www.youtube.com/watch?v=706e4cdleYQ&t=491s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Has booking, payment collection process, insurance verification, you can sell '
              'insurance through it. You can do background checks, you can text directly to '
              'the customer, email directly to them. So like full email system and '
              'communication system built out, comm system.',
      'timestamp': 491,
      'timestamp_label': '[00:08:11]',
      'timestamp_seconds': 491,
      'tip': 'Has booking, payment collection process, insurance verification, you can sell '
             'insurance through it. You can do background checks, you can text directly to the '
             'customer, email directly to them. So like full email system and communication '
             'system built out, comm system.',
      'title': 'How I Actually Scaled a Rental Fleet Past 100 Cars.. (King of Rentals)',
      'url': 'https://www.youtube.com/watch?v=706e4cdleYQ&t=491s',
      'video_id': '706e4cdleYQ'},
     {'author': 'Trend Trader Clark',
      'channel': 'Trend Trader Clark',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:55](https://www.youtube.com/watch?v=laJpf5HhA8s&t=115s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "The color of our vehicle which is black all right next you're gonna use That "
              "Bouncy device that you took out the box and you're gonna enter the last six "
              'digits in this barcode the last six digits off of the little black plug that we '
              'got out of the blue bouncy box.',
      'timestamp': 115,
      'timestamp_label': '[00:01:55]',
      'timestamp_seconds': 115,
      'tip': "The color of our vehicle which is black all right next you're gonna use That "
             "Bouncy device that you took out the box and you're gonna enter the last six "
             'digits in this barcode the last six digits off of the little black plug that we '
             'got out of the blue bouncy box.',
      'title': 'DiY: HOW TO INSTALL A BOUNCIE CAR TRACKER DEVICE | STEP BY STEP (Trend Trader '
               'Clark)',
      'url': 'https://www.youtube.com/watch?v=laJpf5HhA8s&t=115s',
      'video_id': 'laJpf5HhA8s'},
     {'author': 'Limo Anywhere',
      'channel': 'Limo Anywhere',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:16](https://www.youtube.com/watch?v=zKmvS3lxgQc&t=196s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'All of this it knows because he has an account with us. We have done business '
              'with this person before. So now all we have to do is enter a pickup date and a '
              'pickup time. And by the way, it does military time. And uh over here, this is '
              'part of our FAA interaction.',
      'timestamp': 196,
      'timestamp_label': '[00:03:16]',
      'timestamp_seconds': 196,
      'tip': 'All of this it knows because he has an account with us. We have done business '
             'with this person before. So now all we have to do is enter a pickup date and a '
             'pickup time. And by the way, it does military time. And uh over here, this is '
             'part of our FAA interaction.',
      'title': 'Limo Anywhere Reservation & Dispatch System Demonstration (Limo Anywhere)',
      'url': 'https://www.youtube.com/watch?v=zKmvS3lxgQc&t=196s',
      'video_id': 'zKmvS3lxgQc'},
     {'author': 'maxxito',
      'channel': 'maxxito',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:51](https://www.youtube.com/watch?v=GsXJ5ED0hT8&t=231s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "All right, let's go pick up this ladies. It's about 40 minutes to get to that "
              'airport. Okay, we got another black trip down by Canal Street. That was about '
              "maybe $30, I'm guessing.",
      'timestamp': 231,
      'timestamp_label': '[00:03:51]',
      'timestamp_seconds': 231,
      'tip': "All right, let's go pick up this ladies. It's about 40 minutes to get to that "
             'airport. Okay, we got another black trip down by Canal Street. That was about '
             "maybe $30, I'm guessing.",
      'title': 'UBER BLACK NYC : What a Slow Day Really Looks Like. (maxxito)',
      'url': 'https://www.youtube.com/watch?v=GsXJ5ED0hT8&t=231s',
      'video_id': 'GsXJ5ED0hT8'},
     {'author': 'Driver Study Guides',
      'channel': 'Driver Study Guides',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:31](https://www.youtube.com/watch?v=I6r7SzCicUo&t=151s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'B. Any street hail. C. At any taxi stand.  D. Anywhere at the airport curb.',
      'timestamp': 151,
      'timestamp_label': '[00:02:31]',
      'timestamp_seconds': 151,
      'tip': 'B. Any street hail. C. At any taxi stand.  D. Anywhere at the airport curb.',
      'title': 'TLC Exam Questions and Answers #1 | NYC Taxi & Uber Drivers (EN + UZ) (Driver '
               'Study Guides)',
      'url': 'https://www.youtube.com/watch?v=I6r7SzCicUo&t=151s',
      'video_id': 'I6r7SzCicUo'},
     {'author': 'Web4U',
      'channel': 'Web4U',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:44](https://www.youtube.com/watch?v=aSeLmSHmhns&t=464s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "TLC inspection preparing your vehicle according to the TLC's requirements is an "
              "important step in the process meeting these standards ensures that you're "
              'operating a safe and reliable.',
      'timestamp': 464,
      'timestamp_label': '[00:07:44]',
      'timestamp_seconds': 464,
      'tip': "TLC inspection preparing your vehicle according to the TLC's requirements is an "
             "important step in the process meeting these standards ensures that you're "
             'operating a safe and reliable.',
      'title': 'How to Get a TLC License 2026 | Drive Uber & Lyft in NYC - Complete '
               'Step-by-Step Guide (Web4U)',
      'url': 'https://www.youtube.com/watch?v=aSeLmSHmhns&t=464s',
      'video_id': 'aSeLmSHmhns'},
     {'author': 'Fleet Brothers',
      'channel': 'Fleet Brothers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:31](https://www.youtube.com/watch?v=VCL-xD3r5VU&t=151s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Your your thought process because that's the first thing that came to mind for "
              "me yeah I think they've they've been working on automation messages I've.",
      'timestamp': 151,
      'timestamp_label': '[00:02:31]',
      'timestamp_seconds': 151,
      'tip': "Your your thought process because that's the first thing that came to mind for "
             "me yeah I think they've they've been working on automation messages I've.",
      'title': 'BREAKING: Turo Restricts Access to CarSync and Fleetwire (Fleet Brothers)',
      'url': 'https://www.youtube.com/watch?v=VCL-xD3r5VU&t=151s',
      'video_id': 'VCL-xD3r5VU'},
     {'author': 'Car Rental Coach',
      'channel': 'Car Rental Coach',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:37](https://www.youtube.com/watch?v=cp3QlVZWrog&t=157s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'ve built out and the quality that you are making sure that all of your guests "
              "have. So, we have a lot of people that come to Car Rental Coach. 're interested "
              'in starting a business.',
      'timestamp': 157,
      'timestamp_label': '[00:02:37]',
      'timestamp_seconds': 157,
      'tip': "'ve built out and the quality that you are making sure that all of your guests "
             "have. So, we have a lot of people that come to Car Rental Coach. 're interested "
             'in starting a business.',
      'title': 'How He Used Co-Hosting to Scale His Turo Business (Car Rental Coach)',
      'url': 'https://www.youtube.com/watch?v=cp3QlVZWrog&t=157s',
      'video_id': 'cp3QlVZWrog'},
     {'author': 'Delano Green',
      'channel': 'Delano Green',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:23](https://www.youtube.com/watch?v=C5WI_82-JuI&t=143s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "So those are basically the two main documents that I deal with whenever I'm "
              "doing this business model or whenever I'm just like taking shipment or taking "
              'delivery or even sending off vehicles.',
      'timestamp': 143,
      'timestamp_label': '[00:02:23]',
      'timestamp_seconds': 143,
      'tip': "So those are basically the two main documents that I deal with whenever I'm "
             "doing this business model or whenever I'm just like taking shipment or taking "
             'delivery or even sending off vehicles.',
      'title': 'How Turo Cohosting Works: Getting Partner Cars Shipped to Me (Delano Green)',
      'url': 'https://www.youtube.com/watch?v=C5WI_82-JuI&t=143s',
      'video_id': 'C5WI_82-JuI'},
     {'author': 'DigiTree - Official',
      'channel': 'DigiTree - Official',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:58](https://www.youtube.com/watch?v=9tsE8zvyMoY&t=538s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Sorry I was about to leave you guys before I told you guys about that so let's "
              "just go to we're gonna go to a vehicle right it's probably an easier way to do "
              "this right but I'm just gonna go to open.",
      'timestamp': 538,
      'timestamp_label': '[00:08:58]',
      'timestamp_seconds': 538,
      'tip': "Sorry I was about to leave you guys before I told you guys about that so let's "
             "just go to we're gonna go to a vehicle right it's probably an easier way to do "
             "this right but I'm just gonna go to open.",
      'title': 'How To Make A Car Rental Website (2025) - Fleetwire.io (DigiTree - Official)',
      'url': 'https://www.youtube.com/watch?v=9tsE8zvyMoY&t=538s',
      'video_id': '9tsE8zvyMoY'},
     {'author': 'TJackk',
      'channel': 'TJackk',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:04](https://www.youtube.com/watch?v=4NPuQA-V4ZA&t=724s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'I are like the only people in this operation. So like we lean on each other '
              'like heavily like you know like we bounce off ideas, we vent to each other, we '
              'you know make changes as needed. So having that support system is very '
              "important. But I think that's with any business.",
      'timestamp': 724,
      'timestamp_label': '[00:12:04]',
      'timestamp_seconds': 724,
      'tip': 'I are like the only people in this operation. So like we lean on each other like '
             'heavily like you know like we bounce off ideas, we vent to each other, we you '
             'know make changes as needed. So having that support system is very important. '
             "But I think that's with any business.",
      'title': 'Uber Fleet Owners: Don’t Hire Drivers Until You Watch This (TJackk)',
      'url': 'https://www.youtube.com/watch?v=4NPuQA-V4ZA&t=724s',
      'video_id': '4NPuQA-V4ZA'},
     {'author': 'ESCAPE THE MATRIX',
      'channel': 'ESCAPE THE MATRIX',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:05](https://www.youtube.com/watch?v=NtZcNRbIgUo&t=245s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "The gas station so I'll leave those links in the description for you make sure "
              'you guys use those if you guys do sign up until next time enjoy your journey '
              'Escaping The Matrix.',
      'timestamp': 245,
      'timestamp_label': '[00:04:05]',
      'timestamp_seconds': 245,
      'tip': "The gas station so I'll leave those links in the description for you make sure "
             'you guys use those if you guys do sign up until next time enjoy your journey '
             'Escaping The Matrix.',
      'title': 'How to Rent Out Your FHV/TLC License Plates (ESCAPE THE MATRIX)',
      'url': 'https://www.youtube.com/watch?v=NtZcNRbIgUo&t=245s',
      'video_id': 'NtZcNRbIgUo'}],
 8: [{'author': 'King of Rentals',
      'channel': 'King of Rentals',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:04](https://www.youtube.com/watch?v=0qz2jiKB21I&t=64s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'s not built for management. And so we partnered with a company essentially to "
              'give us those tools. The third thing that we had when we were on Turo, or '
              'tracking systems, is we had a Tesla app, which is common, and we had Bouncie '
              'for our gas cars.',
      'timestamp': 64,
      'timestamp_label': '[00:01:04]',
      'timestamp_seconds': 64,
      'tip': "'s not built for management. And so we partnered with a company essentially to "
             'give us those tools. The third thing that we had when we were on Turo, or '
             'tracking systems, is we had a Tesla app, which is common, and we had Bouncie for '
             'our gas cars.',
      'title': 'Best Software Tools to Grow Your Car Rental Fleet (Turo & Private) (King of '
               'Rentals)',
      'url': 'https://www.youtube.com/watch?v=0qz2jiKB21I&t=64s',
      'video_id': '0qz2jiKB21I'},
     {'author': 'Arthur Fandunyan',
      'channel': 'Arthur Fandunyan',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:12](https://www.youtube.com/watch?v=d5fglf-rFOc&t=612s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Q&A's, and keep up with blog posts. I promise you guys they do positively "
              "affect your SEO, so make sure you're doing weekly blog posts on your business "
              "profile as well. Now, you're going to want a booking portal software.",
      'timestamp': 612,
      'timestamp_label': '[00:10:12]',
      'timestamp_seconds': 612,
      'tip': "Q&A's, and keep up with blog posts. I promise you guys they do positively affect "
             "your SEO, so make sure you're doing weekly blog posts on your business profile "
             "as well. Now, you're going to want a booking portal software.",
      'title': 'How To Start Private Car Rentals in 2026 (Full Roadmap) (Arthur Fandunyan)',
      'url': 'https://www.youtube.com/watch?v=d5fglf-rFOc&t=612s',
      'video_id': 'd5fglf-rFOc'},
     {'author': 'Limo Anywhere',
      'channel': 'Limo Anywhere',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:21:31](https://www.youtube.com/watch?v=2s7phAWCEE4&t=1291s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "So, let's go over to this PowerPoint that's showing an example of uh of this "
              'portal. So, if you do airport pickups, this is a convenient tool to help '
              'simplify the pickup process for both the passenger and the driver and the '
              "dispatcher if they're also involved.",
      'timestamp': 1291,
      'timestamp_label': '[00:21:31]',
      'timestamp_seconds': 1291,
      'tip': "So, let's go over to this PowerPoint that's showing an example of uh of this "
             'portal. So, if you do airport pickups, this is a convenient tool to help '
             'simplify the pickup process for both the passenger and the driver and the '
             "dispatcher if they're also involved.",
      'title': 'Limo Anywhere Plus & Black Webinar Replay | Run Smarter. Scale Further. (Limo '
               'Anywhere)',
      'url': 'https://www.youtube.com/watch?v=2s7phAWCEE4&t=1291s',
      'video_id': '2s7phAWCEE4'},
     {'author': 'AOneDriver Recruiting',
      'channel': 'AOneDriver Recruiting',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=Yp0LDXpCQnU&t=20s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "And as drivers, you know, we love the right direction. So, if you're thinking "
              "about starting or leveling up your Amazon relay business, let's talk about one "
              'of your most important tools, the cargo van.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': "And as drivers, you know, we love the right direction. So, if you're thinking "
             "about starting or leveling up your Amazon relay business, let's talk about one "
             'of your most important tools, the cargo van.',
      'title': 'Which Cargo Van Is Best For Amazon Relay In 2025? (AOneDriver Recruiting)',
      'url': 'https://www.youtube.com/watch?v=Yp0LDXpCQnU&t=20s',
      'video_id': 'Yp0LDXpCQnU'},
     {'author': 'Alex Auto',
      'channel': 'Alex Auto',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=6_-L6DOOZog&t=20s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'re going to talk about all the tools you need to run your car rental business. "
              "So, I'm breaking down everything on the operational side that will get you "
              'started from nothing, right? From nothing or from Toro all the way to your '
              'private rental booking, right?',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': "'re going to talk about all the tools you need to run your car rental business. "
             "So, I'm breaking down everything on the operational side that will get you "
             'started from nothing, right? From nothing or from Toro all the way to your '
             'private rental booking, right?',
      'title': 'The Car Rental Toolkit: Software, Trackers, & Automation (Alex Auto)',
      'url': 'https://www.youtube.com/watch?v=6_-L6DOOZog&t=20s',
      'video_id': '6_-L6DOOZog'},
     {'author': 'Etienne Elsaesser',
      'channel': 'Etienne Elsaesser',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:02](https://www.youtube.com/watch?v=3dvvSrh_cus&t=122s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'s license, there is two different methods, and we're going to go kind of go "
              'over that in this uh bottom section here as well. But essentially, you can have '
              'it sent via text, email, you can have it submitted online through a portal if '
              'you have a software or a CRM.',
      'timestamp': 122,
      'timestamp_label': '[00:02:02]',
      'timestamp_seconds': 122,
      'tip': "'s license, there is two different methods, and we're going to go kind of go "
             'over that in this uh bottom section here as well. But essentially, you can have '
             'it sent via text, email, you can have it submitted online through a portal if '
             'you have a software or a CRM.',
      'title': 'How I Built a $150k/Mo “Hands-Off” Car Rental Team (Copy This) (Etienne '
               'Elsaesser)',
      'url': 'https://www.youtube.com/watch?v=3dvvSrh_cus&t=122s',
      'video_id': '3dvvSrh_cus'},
     {'author': 'Rideshare Professor',
      'channel': 'Rideshare Professor',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:12](https://www.youtube.com/watch?v=tKKCFcEvdl4&t=252s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Um you go to the supplier portal, access your dashboard to list the vehicles '
              "you own. Approval, each car must pass Uber's vehicle inspection, important, and "
              'meet local model year and condition requirements before it can be driven on the '
              'platform.',
      'timestamp': 252,
      'timestamp_label': '[00:04:12]',
      'timestamp_seconds': 252,
      'tip': 'Um you go to the supplier portal, access your dashboard to list the vehicles you '
             "own. Approval, each car must pass Uber's vehicle inspection, important, and meet "
             'local model year and condition requirements before it can be driven on the '
             'platform.',
      'title': 'Building an Uber Fleet. The best product they have by far. How to make real '
               'money. (Rideshare Professor)',
      'url': 'https://www.youtube.com/watch?v=tKKCFcEvdl4&t=252s',
      'video_id': 'tKKCFcEvdl4'},
     {'author': 'Limo Anywhere',
      'channel': 'Limo Anywhere',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:04](https://www.youtube.com/watch?v=m8BC7Cdy5a8&t=304s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "And I have created this custom portal that's now available on my driver app. "
              "It's called driver self-dispatch. And as a driver, I'm going to go in here and "
              "just create a booking. I'm based in Colorado, so I'll do local locations.",
      'timestamp': 304,
      'timestamp_label': '[00:05:04]',
      'timestamp_seconds': 304,
      'tip': "And I have created this custom portal that's now available on my driver app. "
             "It's called driver self-dispatch. And as a driver, I'm going to go in here and "
             "just create a booking. I'm based in Colorado, so I'll do local locations.",
      'title': 'From Dispatch to Drop-Off | Limo Anywhere Webinar Replay (Limo Anywhere)',
      'url': 'https://www.youtube.com/watch?v=m8BC7Cdy5a8&t=304s',
      'video_id': 'm8BC7Cdy5a8'},
     {'author': '6amTech',
      'channel': '6amTech',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:27](https://www.youtube.com/watch?v=g1Kpatk95Dc&t=27s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Inside the 6 a.m. Mart app they already use. No separate platform,  nothing new '
              'to learn. It all starts with a dedicated rental.',
      'timestamp': 27,
      'timestamp_label': '[00:00:27]',
      'timestamp_seconds': 27,
      'tip': 'Inside the 6 a.m. Mart app they already use. No separate platform,  nothing new '
             'to learn. It all starts with a dedicated rental.',
      'title': '6amMart Car Rental Module – Car Rental Software for Your Marketplace | '
               'Official Promo Video (6amTech)',
      'url': 'https://www.youtube.com/watch?v=g1Kpatk95Dc&t=27s',
      'video_id': 'g1Kpatk95Dc'},
     {'author': 'King of Rentals',
      'channel': 'King of Rentals',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:37](https://www.youtube.com/watch?v=294HBi50ud8&t=337s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'re really good and I put a lot of value on tracking devices, which we do, we "
              "put a lot of value on telematics. We're collecting a lot of data and tracking, "
              'making sure we know where the cars are. We use this software that we have, '
              'Standard Fleet, every day.',
      'timestamp': 337,
      'timestamp_label': '[00:05:37]',
      'timestamp_seconds': 337,
      'tip': "'re really good and I put a lot of value on tracking devices, which we do, we "
             "put a lot of value on telematics. We're collecting a lot of data and tracking, "
             'making sure we know where the cars are. We use this software that we have, '
             'Standard Fleet, every day.',
      'title': 'How to Choose the Right GPS Tracker for Your Rental Cars! (King of Rentals)',
      'url': 'https://www.youtube.com/watch?v=294HBi50ud8&t=337s',
      'video_id': '294HBi50ud8'},
     {'author': 'Alex Auto',
      'channel': 'Alex Auto',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:44](https://www.youtube.com/watch?v=0Q8BZGkkigM&t=404s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "That's your list of rental softwares that you can use to start your business. "
              "Now this last one is an honorable mention. GoHigh Level isn't specifically a "
              "rental system. GoHigh Level is actually a CRM platform. It's a customer "
              'relation relationship management platform.',
      'timestamp': 404,
      'timestamp_label': '[00:06:44]',
      'timestamp_seconds': 404,
      'tip': "That's your list of rental softwares that you can use to start your business. "
             "Now this last one is an honorable mention. GoHigh Level isn't specifically a "
             "rental system. GoHigh Level is actually a CRM platform. It's a customer relation "
             'relationship management platform.',
      'title': 'How To Run Your Own Car Rental Software Without Turo! (Alex Auto)',
      'url': 'https://www.youtube.com/watch?v=0Q8BZGkkigM&t=404s',
      'video_id': '0Q8BZGkkigM'},
     {'author': 'Limo Anywhere: Livery Software & Training',
      'channel': 'Limo Anywhere: Livery Software & Training',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:30](https://www.youtube.com/watch?v=i-JktDdUTEs&t=30s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Flight aware or flight view or you can do it automatically via flight stats '
              "integration with limo anywhere now first I'm going to go over has you set up "
              'automatic flight tracking with flight stats so first on a reservation.',
      'timestamp': 30,
      'timestamp_label': '[00:00:30]',
      'timestamp_seconds': 30,
      'tip': 'Flight aware or flight view or you can do it automatically via flight stats '
             "integration with limo anywhere now first I'm going to go over has you set up "
             'automatic flight tracking with flight stats so first on a reservation.',
      'title': 'Real-Time Flight Tracking (Limo Anywhere: Livery Software & Training)',
      'url': 'https://www.youtube.com/watch?v=i-JktDdUTEs&t=30s',
      'video_id': 'i-JktDdUTEs'},
     {'author': 'Khushnud Numonov',
      'channel': 'Khushnud Numonov',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:28](https://www.youtube.com/watch?v=67saVKNzHxc&t=568s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Continue and I think that after clicking continue There it actually opens you '
              'an account one TCP and the CP portal that account actually looks like right '
              'right this and when this account opens up for you what you have to do is uh '
              'click apply.',
      'timestamp': 568,
      'timestamp_label': '[00:09:28]',
      'timestamp_seconds': 568,
      'tip': 'Continue and I think that after clicking continue There it actually opens you an '
             'account one TCP and the CP portal that account actually looks like right right '
             'this and when this account opens up for you what you have to do is uh click '
             'apply.',
      'title': 'How To Apply For TCP PERMIT Online For FREE Step By Step | Uber Black/Limo '
               'Business (Khushnud Numonov)',
      'url': 'https://www.youtube.com/watch?v=67saVKNzHxc&t=568s',
      'video_id': '67saVKNzHxc'},
     {'author': 'Conrad Layn',
      'channel': 'Conrad Layn',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=9A9ySyt-LZQ&t=15s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Easier this is what you might not be aware of what you might be aware of even '
              'if you rent your car on the touro platform yes it will be covered by true.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Easier this is what you might not be aware of what you might be aware of even if '
             'you rent your car on the touro platform yes it will be covered by true.',
      'title': 'Period X & Personal Insurance For Turo Biz 🤔 (Conrad Layn)',
      'url': 'https://www.youtube.com/watch?v=9A9ySyt-LZQ&t=15s',
      'video_id': '9A9ySyt-LZQ'},
     {'author': 'TJackk',
      'channel': 'TJackk',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:16](https://www.youtube.com/watch?v=-QE8dzRh7To&t=256s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'It helped maximize my profits when it came to just strictly doing Uber black '
              "but let's check it out enough talking let's check it out so this is it right.",
      'timestamp': 256,
      'timestamp_label': '[00:04:16]',
      'timestamp_seconds': 256,
      'tip': 'It helped maximize my profits when it came to just strictly doing Uber black but '
             "let's check it out enough talking let's check it out so this is it right.",
      'title': 'My Fleet: 2 Luxury SUVs For Uber Black & Chauffeur Business (TJackk)',
      'url': 'https://www.youtube.com/watch?v=-QE8dzRh7To&t=256s',
      'video_id': '-QE8dzRh7To'}],
 9: [{'author': 'Business with Mide',
      'channel': 'Business with Mide',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:58](https://www.youtube.com/watch?v=4TzKcRuyrHY&t=58s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Passengers business rocket helps with getting a TCP license in California they '
              'know a lot about the rules and make the process easier they.',
      'timestamp': 58,
      'timestamp_label': '[00:00:58]',
      'timestamp_seconds': 58,
      'tip': 'Passengers business rocket helps with getting a TCP license in California they '
             'know a lot about the rules and make the process easier they.',
      'title': 'TCP License In California for BEGINNERS (Business with Mide)',
      'url': 'https://www.youtube.com/watch?v=4TzKcRuyrHY&t=58s',
      'video_id': '4TzKcRuyrHY'},
     {'author': 'TJackk',
      'channel': 'TJackk',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:32](https://www.youtube.com/watch?v=CB9UNWu4LMM&t=32s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Yeah, we're not going to tell y'all. But, uh, [laughter] >> you can't scam. So, "
              "just look for a car black on black. Let's just be law abiding people and follow "
              "the rules and get a black SUV that's black on the inside and black on the "
              'outside.',
      'timestamp': 32,
      'timestamp_label': '[00:00:32]',
      'timestamp_seconds': 32,
      'tip': "Yeah, we're not going to tell y'all. But, uh, [laughter] >> you can't scam. So, "
             "just look for a car black on black. Let's just be law abiding people and follow "
             "the rules and get a black SUV that's black on the inside and black on the "
             'outside.',
      'title': 'Before You Buy an SUV for Uber Black — Watch This (TJackk)',
      'url': 'https://www.youtube.com/watch?v=CB9UNWu4LMM&t=32s',
      'video_id': 'CB9UNWu4LMM'},
     {'author': 'The Finance Blueprint',
      'channel': 'The Finance Blueprint',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:51](https://www.youtube.com/watch?v=_J5NloENKR8&t=591s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Progressive is one of the few companies that actually has a streamlined online '
              'portal specifically for small business commercial auto, meaning you can often '
              'get a price in 10 minutes. In conclusion, the world of the side hustle is '
              "exciting, but it's also a legal minefield.",
      'timestamp': 591,
      'timestamp_label': '[00:09:51]',
      'timestamp_seconds': 591,
      'tip': 'Progressive is one of the few companies that actually has a streamlined online '
             'portal specifically for small business commercial auto, meaning you can often '
             'get a price in 10 minutes. In conclusion, the world of the side hustle is '
             "exciting, but it's also a legal minefield.",
      'title': 'Commercial Auto Insurance for Side Hustles (LLCs & Uber) (The Finance '
               'Blueprint)',
      'url': 'https://www.youtube.com/watch?v=_J5NloENKR8&t=591s',
      'video_id': '_J5NloENKR8'},
     {'author': 'BusinessRocket',
      'channel': 'BusinessRocket',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:34](https://www.youtube.com/watch?v=yv_URA4bMDw&t=34s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Their top tier platforms such as the Uber black Uber SUV platforms so before we '
              'get going we want to know what is a TCP license why does it exist well the.',
      'timestamp': 34,
      'timestamp_label': '[00:00:34]',
      'timestamp_seconds': 34,
      'tip': 'Their top tier platforms such as the Uber black Uber SUV platforms so before we '
             'get going we want to know what is a TCP license why does it exist well the.',
      'title': 'TCP License: A Complete Guide - How to create a TCP License. Important '
               'Information about TCP License (BusinessRocket)',
      'url': 'https://www.youtube.com/watch?v=yv_URA4bMDw&t=34s',
      'video_id': 'yv_URA4bMDw'},
     {'author': 'Your Solvent Uncle',
      'channel': 'Your Solvent Uncle',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:19:54](https://www.youtube.com/watch?v=S5qZoSWOz8w&t=1194s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Your vehicle in terms of your amazon relay business they'll take care of you "
              'for that they actually can also wash your vehicle for you it all depends on '
              'your needs you just gotta let them know up front.',
      'timestamp': 1194,
      'timestamp_label': '[00:19:54]',
      'timestamp_seconds': 1194,
      'tip': "Your vehicle in terms of your amazon relay business they'll take care of you for "
             'that they actually can also wash your vehicle for you it all depends on your '
             'needs you just gotta let them know up front.',
      'title': 'Amazon Relay Cargo Van Sprinter Van Expedited Van 2026: Leasing Programs I '
               'Tested, Why You Need This (Your Solvent Uncle)',
      'url': 'https://www.youtube.com/watch?v=S5qZoSWOz8w&t=1194s',
      'video_id': 'S5qZoSWOz8w'},
     {'author': 'Rideshare Professor',
      'channel': 'Rideshare Professor',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:04](https://www.youtube.com/watch?v=Y9-zVxm18W0&t=244s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "The message here is shop around even if you have to go to another state I'm in "
              'California I have a New York brokerage taking care of my business here so very '
              'very important shop around thank you have a great day.',
      'timestamp': 244,
      'timestamp_label': '[00:04:04]',
      'timestamp_seconds': 244,
      'tip': "The message here is shop around even if you have to go to another state I'm in "
             'California I have a New York brokerage taking care of my business here so very '
             'very important shop around thank you have a great day.',
      'title': "Let's talk about commercial insurance for your rideshare vehicles, Uber and "
               'Lyft (Rideshare Professor)',
      'url': 'https://www.youtube.com/watch?v=Y9-zVxm18W0&t=244s',
      'video_id': 'Y9-zVxm18W0'},
     {'author': 'Norman Tutorials',
      'channel': 'Norman Tutorials',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:29](https://www.youtube.com/watch?v=70EXcECzC70&t=89s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'You will also need to submit your tax information. Be sure to enter this '
              'carefully and double-check it before continuing, since tax details are '
              'especially important for compliance, reporting, and payment-related functions '
              'within the platform.',
      'timestamp': 89,
      'timestamp_label': '[00:01:29]',
      'timestamp_seconds': 89,
      'tip': 'You will also need to submit your tax information. Be sure to enter this '
             'carefully and double-check it before continuing, since tax details are '
             'especially important for compliance, reporting, and payment-related functions '
             'within the platform.',
      'title': 'How To Open Uber Fleet Account (Norman Tutorials)',
      'url': 'https://www.youtube.com/watch?v=70EXcECzC70&t=89s',
      'video_id': '70EXcECzC70'},
     {'author': 'RevHostHQ',
      'channel': 'RevHostHQ',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:04](https://www.youtube.com/watch?v=3jfvZ2LM8zM&t=124s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Rent to drivers only through the front door. Read Uber's and Lyft's rental "
              'rules for your city, and ask your insurer about the app-off gap. Running Turo '
              'and Direct side by side without breaking a single rule.',
      'timestamp': 124,
      'timestamp_label': '[00:02:04]',
      'timestamp_seconds': 124,
      'tip': "Rent to drivers only through the front door. Read Uber's and Lyft's rental rules "
             'for your city, and ask your insurer about the app-off gap. Running Turo and '
             'Direct side by side without breaking a single rule.',
      'title': 'Renting Cars to Uber and Lyft Drivers: The Real Math and the Rules (RevHostHQ)',
      'url': 'https://www.youtube.com/watch?v=3jfvZ2LM8zM&t=124s',
      'video_id': '3jfvZ2LM8zM'},
     {'author': 'Private Keys',
      'channel': 'Private Keys',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:47](https://www.youtube.com/watch?v=LI8272h_0Ns&t=227s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'I was going to college, I was buying these cars and selling cars, kind of '
              'building my own brand, kind of getting known by the community, kind of build my '
              'name. Um so, it which kind of led to me kind of being able to obtain a '
              'dealership license.',
      'timestamp': 227,
      'timestamp_label': '[00:03:47]',
      'timestamp_seconds': 227,
      'tip': 'I was going to college, I was buying these cars and selling cars, kind of '
             'building my own brand, kind of getting known by the community, kind of build my '
             'name. Um so, it which kind of led to me kind of being able to obtain a '
             'dealership license.',
      'title': 'How I Built A 50+ Exotic Rental Fleet Across 3 Cities (Nobody Teaches This) '
               '(Private Keys)',
      'url': 'https://www.youtube.com/watch?v=LI8272h_0Ns&t=227s',
      'video_id': 'LI8272h_0Ns'},
     {'author': 'Capterra',
      'channel': 'Capterra',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:03](https://www.youtube.com/watch?v=1Zq5flVE29o&t=123s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Like our car rental then I would say um it's a great solution there are some "
              "limitations in terms of the customization but again if you're a small business "
              "that's probably not something that you worry about to the same extent as if "
              "you're like a global brand.",
      'timestamp': 123,
      'timestamp_label': '[00:02:03]',
      'timestamp_seconds': 123,
      'tip': "Like our car rental then I would say um it's a great solution there are some "
             "limitations in terms of the customization but again if you're a small business "
             "that's probably not something that you worry about to the same extent as if "
             "you're like a global brand.",
      'title': 'HQ Rental Software Review: HQ Rental Software is a Great fit for Car Rentals! '
               '(Capterra)',
      'url': 'https://www.youtube.com/watch?v=1Zq5flVE29o&t=123s',
      'video_id': '1Zq5flVE29o'},
     {'author': 'King of Rentals',
      'channel': 'King of Rentals',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:43](https://www.youtube.com/watch?v=7IyNOkXwrsg&t=463s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Uh then the rest of our contract is like um more legal stuff like making sure '
              'that.',
      'timestamp': 463,
      'timestamp_label': '[00:07:43]',
      'timestamp_seconds': 463,
      'tip': 'Uh then the rest of our contract is like um more legal stuff like making sure '
             'that.',
      'title': 'Co-hosting 101 | Everything You Need To Know About Co-hosting On Turo (King of '
               'Rentals)',
      'url': 'https://www.youtube.com/watch?v=7IyNOkXwrsg&t=463s',
      'video_id': '7IyNOkXwrsg'},
     {'author': 'Alex Auto',
      'channel': 'Alex Auto',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:43](https://www.youtube.com/watch?v=bHUp-OA4bH8&t=643s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Now, you want to make sure you set up your rental agreement. This will protect '
              'you in the case of any liability, any lawsuits. That way, you and your business '
              "are covered properly. Now, that's the basic structure of setting up ride-share "
              'rentals.',
      'timestamp': 643,
      'timestamp_label': '[00:10:43]',
      'timestamp_seconds': 643,
      'tip': 'Now, you want to make sure you set up your rental agreement. This will protect '
             'you in the case of any liability, any lawsuits. That way, you and your business '
             "are covered properly. Now, that's the basic structure of setting up ride-share "
             'rentals.',
      'title': 'Rideshare Rentals! The #1 Car Rental Strategy Right Now (Alex Auto)',
      'url': 'https://www.youtube.com/watch?v=bHUp-OA4bH8&t=643s',
      'video_id': 'bHUp-OA4bH8'},
     {'author': 'Aubrey Janik',
      'channel': 'Aubrey Janik',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:18:42](https://www.youtube.com/watch?v=qSzMy86MT7I&t=1122s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'QuickBooks but also my wife works on the accounting side of the business so she '
              "has spreadsheets that she's created for OPC so for everyone's car that's at it.",
      'timestamp': 1122,
      'timestamp_label': '[00:18:42]',
      'timestamp_seconds': 1122,
      'tip': 'QuickBooks but also my wife works on the accounting side of the business so she '
             "has spreadsheets that she's created for OPC so for everyone's car that's at it.",
      'title': 'How to Grow a Turo Fleet Using Other Peoples Cars (Aubrey Janik)',
      'url': 'https://www.youtube.com/watch?v=qSzMy86MT7I&t=1122s',
      'video_id': 'qSzMy86MT7I'},
     {'author': 'Ryde VIP',
      'channel': 'Ryde VIP',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:06](https://www.youtube.com/watch?v=z-YFFXEIrY8&t=306s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Folds out so that's pretty good also it has a lot of luggage space so that's "
              'pretty cool so I really like the front the front looks actually really cool so '
              "let's open up the door and sit inside.",
      'timestamp': 306,
      'timestamp_label': '[00:05:06]',
      'timestamp_seconds': 306,
      'tip': "Folds out so that's pretty good also it has a lot of luggage space so that's "
             'pretty cool so I really like the front the front looks actually really cool so '
             "let's open up the door and sit inside.",
      'title': 'Uber Driver Test driving a black Chevrolet suburban SUV for Uber black SUV '
               'service (Ryde VIP)',
      'url': 'https://www.youtube.com/watch?v=z-YFFXEIrY8&t=306s',
      'video_id': 'z-YFFXEIrY8'},
     {'author': 'TJackk',
      'channel': 'TJackk',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:23](https://www.youtube.com/watch?v=o8EUtCEWMzY&t=263s)',
      'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                   'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                   'zero-owned-metal investor vehicle co-hosting (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Daily every day on Tik Tok I'll put it in this video my Tik Tok name is real TJ "
              "but that'll be it for this video video I will catch y'all next video.",
      'timestamp': 263,
      'timestamp_label': '[00:04:23]',
      'timestamp_seconds': 263,
      'tip': "Daily every day on Tik Tok I'll put it in this video my Tik Tok name is real TJ "
             "but that'll be it for this video video I will catch y'all next video.",
      'title': 'What Made Me Get Into Uber Black/Chauffeur Business (TJackk)',
      'url': 'https://www.youtube.com/watch?v=o8EUtCEWMzY&t=263s',
      'video_id': 'o8EUtCEWMzY'}],
 10: [{'author': 'Alex Auto',
       'channel': 'Alex Auto',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:32](https://www.youtube.com/watch?v=UJnOivSethI&t=32s)',
       'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                    'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                    'zero-owned-metal investor vehicle co-hosting (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "Hey, how do I get them to do this and that? So, I'm just going to make one "
               'video and then you guys can watch it. When it comes to the Uber drivers, '
               "right, before I get started, right, I'm Alex Auto. I help car rental "
               'entrepreneurs start and scale their business.',
       'timestamp': 32,
       'timestamp_label': '[00:00:32]',
       'timestamp_seconds': 32,
       'tip': "Hey, how do I get them to do this and that? So, I'm just going to make one "
              'video and then you guys can watch it. When it comes to the Uber drivers, right, '
              "before I get started, right, I'm Alex Auto. I help car rental entrepreneurs "
              'start and scale their business.',
       'title': 'Renting to Uber Drivers, The System That Actually Works (Alex Auto)',
       'url': 'https://www.youtube.com/watch?v=UJnOivSethI&t=32s',
       'video_id': 'UJnOivSethI'},
      {'author': '3doglife4real',
       'channel': '3doglife4real',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:31](https://www.youtube.com/watch?v=YkcJvhapCds&t=31s)',
       'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                    'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                    'zero-owned-metal investor vehicle co-hosting (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "Um, and again, you'll connect this um, in your vehicle. Again, it's usually "
               "under the dashboard. Anyway, so once you're set, the app lets you see the "
               "vehicle's real-time location and route history. Um, it also lets you set up "
               'speed monitoring and geoence.',
       'timestamp': 31,
       'timestamp_label': '[00:00:31]',
       'timestamp_seconds': 31,
       'tip': "Um, and again, you'll connect this um, in your vehicle. Again, it's usually "
              "under the dashboard. Anyway, so once you're set, the app lets you see the "
              "vehicle's real-time location and route history. Um, it also lets you set up "
              'speed monitoring and geoence.',
       'title': 'Good Option for Parents with Teens? Bouncie GPS Tracker for Vehicles '
                '(3doglife4real)',
       'url': 'https://www.youtube.com/watch?v=YkcJvhapCds&t=31s',
       'video_id': 'YkcJvhapCds'},
      {'author': 'Kel King',
       'channel': 'Kel King',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:16:33](https://www.youtube.com/watch?v=BD6Xfj5F-Fk&t=993s)',
       'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                    'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                    'zero-owned-metal investor vehicle co-hosting (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "Facebook Marketplace that's completely free. And finally, step number four, "
               'you want to automate and scale. Um, honestly, you can run this business by '
               'yourself because the renters take the cars for 6 months, 9 months, 12 months '
               'at a time.',
       'timestamp': 993,
       'timestamp_label': '[00:16:33]',
       'timestamp_seconds': 993,
       'tip': "Facebook Marketplace that's completely free. And finally, step number four, you "
              'want to automate and scale. Um, honestly, you can run this business by yourself '
              'because the renters take the cars for 6 months, 9 months, 12 months at a time.',
       'title': 'Ditch Turo: Build Your Private Car Rental Empire (Kel King)',
       'url': 'https://www.youtube.com/watch?v=BD6Xfj5F-Fk&t=993s',
       'video_id': 'BD6Xfj5F-Fk'},
      {'author': 'Car Sharing Jho',
       'channel': 'Car Sharing Jho',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:10:05](https://www.youtube.com/watch?v=uOTjoNGAa7w&t=605s)',
       'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                    'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                    'zero-owned-metal investor vehicle co-hosting (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "Before that's why I do not like doing it it has to be on my account because I "
               "have control on who's booking or not I've had nightmares before where.",
       'timestamp': 605,
       'timestamp_label': '[00:10:05]',
       'timestamp_seconds': 605,
       'tip': "Before that's why I do not like doing it it has to be on my account because I "
              "have control on who's booking or not I've had nightmares before where.",
       'title': 'TURO TALK #5 | Turo Car Rental Business Co-Hosting Host with 100+ Cars | How '
                'To Co-Host On Turo Tips (Car Sharing Jho)',
       'url': 'https://www.youtube.com/watch?v=uOTjoNGAa7w&t=605s',
       'video_id': 'uOTjoNGAa7w'},
      {'author': 'Cactus Crossfire',
       'channel': 'Cactus Crossfire',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:14](https://www.youtube.com/watch?v=oPWng_p3MLE&t=314s)',
       'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                    'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                    'zero-owned-metal investor vehicle co-hosting (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Now, in regards to auto accidents, all those other things, like I said, I '
               "think that that still falls on on the driver. That's pretty clear in most "
               "instances. Um uh it is it's even clearer for the for the cab companies, right?",
       'timestamp': 314,
       'timestamp_label': '[00:05:14]',
       'timestamp_seconds': 314,
       'tip': 'Now, in regards to auto accidents, all those other things, like I said, I think '
              "that that still falls on on the driver. That's pretty clear in most instances. "
              "Um uh it is it's even clearer for the for the cab companies, right?",
       'title': '🌵❌🔥Uber, the Graves Amendment, and the Rideshare Liability Fight #nevada '
                '#policy #GRAVESAMENDMENT (Cactus Crossfire)',
       'url': 'https://www.youtube.com/watch?v=oPWng_p3MLE&t=314s',
       'video_id': 'oPWng_p3MLE'},
      {'author': 'Frankie',
       'channel': 'Frankie',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:11](https://www.youtube.com/watch?v=gMeI77Gf16I&t=71s)',
       'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                    'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                    'zero-owned-metal investor vehicle co-hosting (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "Looks like it's in Fair Park Dose Ekis Arena maybe or state fair. Just it's a "
               "black SUV ride. Um I honestly probably wouldn't take that ride. I would "
               'definitely be converting that into like a$125 ride maybe and then I would just '
               'speed back.',
       'timestamp': 71,
       'timestamp_label': '[00:01:11]',
       'timestamp_seconds': 71,
       'tip': "Looks like it's in Fair Park Dose Ekis Arena maybe or state fair. Just it's a "
              "black SUV ride. Um I honestly probably wouldn't take that ride. I would "
              'definitely be converting that into like a$125 ride maybe and then I would just '
              'speed back.',
       'title': 'Uber Black SUV pay is something else. (Frankie)',
       'url': 'https://www.youtube.com/watch?v=gMeI77Gf16I&t=71s',
       'video_id': 'gMeI77Gf16I'},
      {'author': 'RC Simon',
       'channel': 'RC Simon',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:40](https://www.youtube.com/watch?v=E1lFWd_WIy8&t=340s)',
       'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                    'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                    'zero-owned-metal investor vehicle co-hosting (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Continue to scale if you guys enjoy this tap in I just did a video on like '
               'getting my free templates my whole dashboard set up how we organize our fleet '
               "tap in check that out y'all have a blessed one I'll talk to you soon bye.",
       'timestamp': 340,
       'timestamp_label': '[00:05:40]',
       'timestamp_seconds': 340,
       'tip': 'Continue to scale if you guys enjoy this tap in I just did a video on like '
              'getting my free templates my whole dashboard set up how we organize our fleet '
              "tap in check that out y'all have a blessed one I'll talk to you soon bye.",
       'title': 'How We MANAGE Our 24+ Turo Fleet (RC Simon)',
       'url': 'https://www.youtube.com/watch?v=E1lFWd_WIy8&t=340s',
       'video_id': 'E1lFWd_WIy8'},
      {'author': 'Luxury Transportation Academy / Podcast',
       'channel': 'Luxury Transportation Academy / Podcast',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:02](https://www.youtube.com/watch?v=dGw1wHDoOUA&t=62s)',
       'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                    'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                    'zero-owned-metal investor vehicle co-hosting (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': '\'s a lot of uh people that are at his heels saying, "Hey, you need to get '
               'over with in in in in Uber Black. You need to get into Uber business. You need '
               'to get into Uber corporate.".',
       'timestamp': 62,
       'timestamp_label': '[00:01:02]',
       'timestamp_seconds': 62,
       'tip': '\'s a lot of uh people that are at his heels saying, "Hey, you need to get over '
              'with in in in in Uber Black. You need to get into Uber business. You need to '
              'get into Uber corporate.".',
       'title': 'Black Car vs. Uber: The REAL Difference Between Luxury Transportation & '
                'Rideshare (Luxury Transportation Academy / Podcast)',
       'url': 'https://www.youtube.com/watch?v=dGw1wHDoOUA&t=62s',
       'video_id': 'dGw1wHDoOUA'},
      {'author': 'Limo Anywhere: Livery Software & Training',
       'channel': 'Limo Anywhere: Livery Software & Training',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:38](https://www.youtube.com/watch?v=Ql6WZs_7w1U&t=158s)',
       'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                    'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                    'zero-owned-metal investor vehicle co-hosting (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "Status to offer for those jobs to offer to that driver and they're both been "
               'offered to them at the same time they should have both of those offers sitting '
               'in that driver anywhere mobile app at that time.',
       'timestamp': 158,
       'timestamp_label': '[00:02:38]',
       'timestamp_seconds': 158,
       'tip': "Status to offer for those jobs to offer to that driver and they're both been "
              'offered to them at the same time they should have both of those offers sitting '
              'in that driver anywhere mobile app at that time.',
       'title': 'How to Dispatch Jobs and How to Utilize the Batch Edit functionality in LA '
                'Mobile (Limo Anywhere: Livery Software & Training)',
       'url': 'https://www.youtube.com/watch?v=Ql6WZs_7w1U&t=158s',
       'video_id': 'Ql6WZs_7w1U'},
      {'author': 'Fares and Frustrations',
       'channel': 'Fares and Frustrations',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:56](https://www.youtube.com/watch?v=zcztAGWjcfQ&t=116s)',
       'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                    'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                    'zero-owned-metal investor vehicle co-hosting (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "I I do Uber Comfort but with Uber black when you're not the airport does it "
               'send you rides like it does me for Uber black or does it send you just '
               'whatever like.',
       'timestamp': 116,
       'timestamp_label': '[00:01:56]',
       'timestamp_seconds': 116,
       'tip': "I I do Uber Comfort but with Uber black when you're not the airport does it "
              'send you rides like it does me for Uber black or does it send you just whatever '
              'like.',
       'title': 'How Uber Black works: Expert advice from Uber black drivers (Fares and '
                'Frustrations)',
       'url': 'https://www.youtube.com/watch?v=zcztAGWjcfQ&t=116s',
       'video_id': 'zcztAGWjcfQ'},
      {'author': 'Rideshare Professor',
       'channel': 'Rideshare Professor',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:44](https://www.youtube.com/watch?v=sYJ0eQpgXks&t=524s)',
       'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                    'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                    'zero-owned-metal investor vehicle co-hosting (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Different um topics we talk about uh we also talk about business rocket the '
               'registration buying the right vehicle doing it in the right sequence Etc I '
               'put.',
       'timestamp': 524,
       'timestamp_label': '[00:08:44]',
       'timestamp_seconds': 524,
       'tip': 'Different um topics we talk about uh we also talk about business rocket the '
              'registration buying the right vehicle doing it in the right sequence Etc I put.',
       'title': 'TCP License. The Complete Guide+How to become a private driver operating '
                'Uber, Lyft+private clients (Rideshare Professor)',
       'url': 'https://www.youtube.com/watch?v=sYJ0eQpgXks&t=524s',
       'video_id': 'sYJ0eQpgXks'},
      {'author': 'CentraliaUS',
       'channel': 'CentraliaUS',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:11](https://www.youtube.com/watch?v=YflWar_YuYg&t=251s)',
       'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                    'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                    'zero-owned-metal investor vehicle co-hosting (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "'s going to tell me that this is the trip timeline. So, it tells you the "
               'distance, the time, the idle time, the efficiency. 7% efficiency, max speed '
               'was 43, habits, how many times I braked hard, how many times I break rapidly, '
               'accelerated rapidly, and idle.',
       'timestamp': 251,
       'timestamp_label': '[00:04:11]',
       'timestamp_seconds': 251,
       'tip': "'s going to tell me that this is the trip timeline. So, it tells you the "
              'distance, the time, the idle time, the efficiency. 7% efficiency, max speed was '
              '43, habits, how many times I braked hard, how many times I break rapidly, '
              'accelerated rapidly, and idle.',
       'title': 'STOP CAR THEFT! Installing the @Bouncie GPS Tracker Hidden in my 2015 Dodge '
                'Durango (CentraliaUS)',
       'url': 'https://www.youtube.com/watch?v=YflWar_YuYg&t=251s',
       'video_id': 'YflWar_YuYg'},
      {'author': 'TJackk',
       'channel': 'TJackk',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:10:53](https://www.youtube.com/watch?v=fIZp2tBd2tY&t=653s)',
       'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                    'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                    'zero-owned-metal investor vehicle co-hosting (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "'s other business ventures that we're trying to like leverage the funding for, "
               'if that makes sense. So, right now in our situation, it made most sense to '
               "keep it. But with the way that it's going, it may go bye-bye soon.",
       'timestamp': 653,
       'timestamp_label': '[00:10:53]',
       'timestamp_seconds': 653,
       'tip': "'s other business ventures that we're trying to like leverage the funding for, "
              'if that makes sense. So, right now in our situation, it made most sense to keep '
              "it. But with the way that it's going, it may go bye-bye soon.",
       'title': 'I’d Never Buy This SUV Again for Uber Black (TJackk)',
       'url': 'https://www.youtube.com/watch?v=fIZp2tBd2tY&t=653s',
       'video_id': 'fIZp2tBd2tY'},
      {'author': 'Khushnud Numonov',
       'channel': 'Khushnud Numonov',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:54](https://www.youtube.com/watch?v=i1B7HEM_kcM&t=174s)',
       'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                    'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                    'zero-owned-metal investor vehicle co-hosting (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'That when a driver is online you can see where your car is located but when it '
               'goes offline you can even see where the last time the driver was online where '
               'the last time the car was so no information at all so it is a good privacy for '
               'those drivers.',
       'timestamp': 174,
       'timestamp_label': '[00:02:54]',
       'timestamp_seconds': 174,
       'tip': 'That when a driver is online you can see where your car is located but when it '
              'goes offline you can even see where the last time the driver was online where '
              'the last time the car was so no information at all so it is a good privacy for '
              'those drivers.',
       'title': 'How To ADD a DRIVER To Your Uber FLEET | Uber Fleet App Review | Uber Black '
                '(Khushnud Numonov)',
       'url': 'https://www.youtube.com/watch?v=i1B7HEM_kcM&t=174s',
       'video_id': 'i1B7HEM_kcM'},
      {'author': 'King of Rentals',
       'channel': 'King of Rentals',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=xCgsQFz-kOM&t=15s)',
       'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                    'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                    'zero-owned-metal investor vehicle co-hosting (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Arizona he has a huge Fleet what are you up to now 173 173 okay and today '
               "we're going to talk about co-hosting which is I mean you're.",
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': "Arizona he has a huge Fleet what are you up to now 173 173 okay and today we're "
              "going to talk about co-hosting which is I mean you're.",
       'title': 'How it Co-Host | Turo Talk (King of Rentals)',
       'url': 'https://www.youtube.com/watch?v=xCgsQFz-kOM&t=15s',
       'video_id': 'xCgsQFz-kOM'}],
 11: [{'author': 'Rideshare Professor',
       'channel': 'Rideshare Professor',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:35](https://www.youtube.com/watch?v=vavDFZYcydE&t=95s)',
       'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                    'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                    'zero-owned-metal investor vehicle co-hosting (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "LAX, if I'm picking them up, I take a screenshot. I go on to the app on the "
               "other phone and I put in, okay, I know they're going to Westlake, so let me "
               'just check quickly before I exit the airport, what is this guy paying? And I '
               'have the numbers right there, real time.',
       'timestamp': 95,
       'timestamp_label': '[00:01:35]',
       'timestamp_seconds': 95,
       'tip': "LAX, if I'm picking them up, I take a screenshot. I go on to the app on the "
              "other phone and I put in, okay, I know they're going to Westlake, so let me "
              'just check quickly before I exit the airport, what is this guy paying? And I '
              'have the numbers right there, real time.',
       'title': 'Attention Uber Black SUV drivers. How to sell that $242 Uber trip for $180 '
                'and get a $20 tip =$200 (Rideshare Professor)',
       'url': 'https://www.youtube.com/watch?v=vavDFZYcydE&t=95s',
       'video_id': 'vavDFZYcydE'},
      {'author': 'Car Rental Coach',
       'channel': 'Car Rental Coach',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:28:57](https://www.youtube.com/watch?v=sP0LfwE7elc&t=1737s)',
       'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                    'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                    'zero-owned-metal investor vehicle co-hosting (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'And guys, as always, scaling and automation. You want to scale it like a real '
               "business. You can't manually message every guest. You can't wash all the cars "
               "yourself. And you don't want to track all your rentals on paper. You have a "
               'rental business.',
       'timestamp': 1737,
       'timestamp_label': '[00:28:57]',
       'timestamp_seconds': 1737,
       'tip': 'And guys, as always, scaling and automation. You want to scale it like a real '
              "business. You can't manually message every guest. You can't wash all the cars "
              "yourself. And you don't want to track all your rentals on paper. You have a "
              'rental business.',
       'title': 'How to Run a Private Car Rental Business (No Turo Needed) (Car Rental Coach)',
       'url': 'https://www.youtube.com/watch?v=sP0LfwE7elc&t=1737s',
       'video_id': 'sP0LfwE7elc'},
      {'author': 'Limo Anywhere: Livery Software & Training',
       'channel': 'Limo Anywhere: Livery Software & Training',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:14](https://www.youtube.com/watch?v=WYw2hH-qD54&t=74s)',
       'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                    'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                    'zero-owned-metal investor vehicle co-hosting (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Little easier for them to follow on my confirmation email after adding my '
               "instructions I'll click the Add button below to save them in the store pickup "
               "instructions box I'll show you how to activate another Airport and store some "
               'instructions before in this video.',
       'timestamp': 74,
       'timestamp_label': '[00:01:14]',
       'timestamp_seconds': 74,
       'tip': 'Little easier for them to follow on my confirmation email after adding my '
              "instructions I'll click the Add button below to save them in the store pickup "
              "instructions box I'll show you how to activate another Airport and store some "
              'instructions before in this video.',
       'title': 'Airports (Limo Anywhere: Livery Software & Training)',
       'url': 'https://www.youtube.com/watch?v=WYw2hH-qD54&t=74s',
       'video_id': 'WYw2hH-qD54'},
      {'author': 'TJackk',
       'channel': 'TJackk',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:11:57](https://www.youtube.com/watch?v=Bf1i8iZKK5M&t=717s)',
       'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                    'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                    'zero-owned-metal investor vehicle co-hosting (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'I want to make sure you a good candidate and I believe that you are '
               'responsible to take care of my car." It\'s just like a like I said, it\'s just '
               'like you applying for a job and a manager vetting you out before they actually '
               "hire you. But you this time you're the employer.",
       'timestamp': 717,
       'timestamp_label': '[00:11:57]',
       'timestamp_seconds': 717,
       'tip': 'I want to make sure you a good candidate and I believe that you are responsible '
              'to take care of my car." It\'s just like a like I said, it\'s just like you '
              'applying for a job and a manager vetting you out before they actually hire you. '
              "But you this time you're the employer.",
       'title': 'How to Rent Cars Through Uber Fleet Partner Program (Step-by-Step) (TJackk)',
       'url': 'https://www.youtube.com/watch?v=Bf1i8iZKK5M&t=717s',
       'video_id': 'Bf1i8iZKK5M'},
      {'author': 'Luxury Transportation Academy / Podcast',
       'channel': 'Luxury Transportation Academy / Podcast',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:02](https://www.youtube.com/watch?v=74VV4-E1p9k&t=362s)',
       'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                    'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                    'zero-owned-metal investor vehicle co-hosting (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Um how how are you traditionally handling that when that does happen? Do you '
               'have somebody within your operations team that handles that? Well, so that you '
               'know those are good questions.',
       'timestamp': 362,
       'timestamp_label': '[00:06:02]',
       'timestamp_seconds': 362,
       'tip': 'Um how how are you traditionally handling that when that does happen? Do you '
              'have somebody within your operations team that handles that? Well, so that you '
              'know those are good questions.',
       'title': 'Why Your Limo Business NEEDS Software to Scale (Stop Doing It the Old Way) '
                '(Luxury Transportation Academy / Podcast)',
       'url': 'https://www.youtube.com/watch?v=74VV4-E1p9k&t=362s',
       'video_id': '74VV4-E1p9k'},
      {'author': 'Philly Car Renting',
       'channel': 'Philly Car Renting',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:58](https://www.youtube.com/watch?v=1amDBwhhsY0&t=118s)',
       'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                    'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                    'zero-owned-metal investor vehicle co-hosting (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "There's was this business is very very tricky. You need to have everything in "
               'line. And so you were saying that what we did before Turo is we still do that '
               'also. We are still in real estate.',
       'timestamp': 118,
       'timestamp_label': '[00:01:58]',
       'timestamp_seconds': 118,
       'tip': "There's was this business is very very tricky. You need to have everything in "
              'line. And so you were saying that what we did before Turo is we still do that '
              'also. We are still in real estate.',
       'title': 'How We Built a 250+ Car Fleet on Turo — Partner Q&A (Philly Car Renting)',
       'url': 'https://www.youtube.com/watch?v=1amDBwhhsY0&t=118s',
       'video_id': '1amDBwhhsY0'},
      {'author': 'Fleeteer - TURO Co-Host',
       'channel': 'Fleeteer - TURO Co-Host',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:26](https://www.youtube.com/watch?v=NINtu6BJvFY&t=206s)',
       'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                    'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                    'zero-owned-metal investor vehicle co-hosting (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Turo rental car operations for just 15% of the rental earnings we generate on '
               "behalf of you. So if we don't earn you any profit, then we don't get paid "
               'anything at all. And here are two major reasons why you should consider Fleet '
               'Tier to co-host your Turo business.',
       'timestamp': 206,
       'timestamp_label': '[00:03:26]',
       'timestamp_seconds': 206,
       'tip': 'Turo rental car operations for just 15% of the rental earnings we generate on '
              "behalf of you. So if we don't earn you any profit, then we don't get paid "
              'anything at all. And here are two major reasons why you should consider Fleet '
              'Tier to co-host your Turo business.',
       'title': 'Passive earnings from TURO Co-Hosting! (Fleeteer - TURO Co-Host)',
       'url': 'https://www.youtube.com/watch?v=NINtu6BJvFY&t=206s',
       'video_id': 'NINtu6BJvFY'},
      {'author': 'CBS New York',
       'channel': 'CBS New York',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:07](https://www.youtube.com/watch?v=o74VMchARlA&t=127s)',
       'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                    'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                    'zero-owned-metal investor vehicle co-hosting (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Reporter: THE APP COMPANY WILL BE FINED $350 FOR EACH 100 MILES OVER THE '
               'CRUISING LIMIT LOGGED BY EACH CAR. OFFICIALS SAY THAT COULD ADD UP TO HUNDREDS '
               'OF THOUSANDS OF DOLLARS IN FINES. THE TLC ALSO EXTENDED THE TEMPORARY CAP ON '
               'NEW FOR HIRE VEHICLES FOR ANOTHER YEAR.',
       'timestamp': 127,
       'timestamp_label': '[00:02:07]',
       'timestamp_seconds': 127,
       'tip': 'Reporter: THE APP COMPANY WILL BE FINED $350 FOR EACH 100 MILES OVER THE '
              'CRUISING LIMIT LOGGED BY EACH CAR. OFFICIALS SAY THAT COULD ADD UP TO HUNDREDS '
              'OF THOUSANDS OF DOLLARS IN FINES. THE TLC ALSO EXTENDED THE TEMPORARY CAP ON '
              'NEW FOR HIRE VEHICLES FOR ANOTHER YEAR.',
       'title': 'For-Hire Vehicle Cap Approved In NYC (CBS New York)',
       'url': 'https://www.youtube.com/watch?v=o74VMchARlA&t=127s',
       'video_id': 'o74VMchARlA'},
      {'author': 'Bloomberg Tech',
       'channel': 'Bloomberg Tech',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:57](https://www.youtube.com/watch?v=PcjMNPxzLCw&t=177s)',
       'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                    'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                    'zero-owned-metal investor vehicle co-hosting (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'FOR EVERY BOOKING PLACED IN OUR SYSTEM DURING THOSE TIMES. I ALSO FIND IT '
               'INTERESTING, CAROLINE IS RIGHT. WHAT IS IT THAT YOU HAVE, BLACKLANE, '
               'TECHNOLOGICALLY SPEAKING, WHAT IS IT THAT IS UNIQUE THAT JUSTIFIES THIS ROUND, '
               'WHAT IS A 50% JUMP IN VALUATION?',
       'timestamp': 177,
       'timestamp_label': '[00:02:57]',
       'timestamp_seconds': 177,
       'tip': 'FOR EVERY BOOKING PLACED IN OUR SYSTEM DURING THOSE TIMES. I ALSO FIND IT '
              'INTERESTING, CAROLINE IS RIGHT. WHAT IS IT THAT YOU HAVE, BLACKLANE, '
              'TECHNOLOGICALLY SPEAKING, WHAT IS IT THAT IS UNIQUE THAT JUSTIFIES THIS ROUND, '
              'WHAT IS A 50% JUMP IN VALUATION?',
       'title': 'Blacklane CEO on What Makes It Different from Uber (Bloomberg Tech)',
       'url': 'https://www.youtube.com/watch?v=PcjMNPxzLCw&t=177s',
       'video_id': 'PcjMNPxzLCw'},
      {'author': 'Delano Green',
       'channel': 'Delano Green',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:57](https://www.youtube.com/watch?v=xTVl-1-TkSI&t=297s)',
       'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                    'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                    'zero-owned-metal investor vehicle co-hosting (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "You say >> Other people's cars. Other people's cars, exactly. So, instead of "
               'like buying cars or like getting a bunch of financed vehicles or buying cash '
               "cars, I've only been just getting more partners and building those "
               'relationships and just scaling that way.',
       'timestamp': 297,
       'timestamp_label': '[00:04:57]',
       'timestamp_seconds': 297,
       'tip': "You say >> Other people's cars. Other people's cars, exactly. So, instead of "
              'like buying cars or like getting a bunch of financed vehicles or buying cash '
              "cars, I've only been just getting more partners and building those "
              'relationships and just scaling that way.',
       'title': 'I Met Turo Hosts With 400+ Cars… Here’s What They Taught Me (Delano Green)',
       'url': 'https://www.youtube.com/watch?v=xTVl-1-TkSI&t=297s',
       'video_id': 'xTVl-1-TkSI'},
      {'author': 'King of Rentals',
       'channel': 'King of Rentals',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:54](https://www.youtube.com/watch?v=by_FGx_s0B0&t=474s)',
       'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                    'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                    'zero-owned-metal investor vehicle co-hosting (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "Click the link below and we'll help you scale your business. But I appreciate "
               "all the support in every video and I'll see you in the next one.",
       'timestamp': 474,
       'timestamp_label': '[00:07:54]',
       'timestamp_seconds': 474,
       'tip': "Click the link below and we'll help you scale your business. But I appreciate "
              "all the support in every video and I'll see you in the next one.",
       'title': 'This Might Be Holding You Back From Scaling Your Car Rental Company! (King of '
                'Rentals)',
       'url': 'https://www.youtube.com/watch?v=by_FGx_s0B0&t=474s',
       'video_id': 'by_FGx_s0B0'},
      {'author': 'Aubrey Janik',
       'channel': 'Aubrey Janik',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:37](https://www.youtube.com/watch?v=Yjwp4WMIjbc&t=337s)',
       'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                    'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                    'zero-owned-metal investor vehicle co-hosting (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "On the Facebook groups he's plugging his business often he's letting people "
               "know what he's doing often and he kind of is shamelessly promoting his "
               'business and I.',
       'timestamp': 337,
       'timestamp_label': '[00:05:37]',
       'timestamp_seconds': 337,
       'tip': "On the Facebook groups he's plugging his business often he's letting people "
              "know what he's doing often and he kind of is shamelessly promoting his business "
              'and I.',
       'title': 'How to Co-Host On Turo (From a Host With 200+ Cars) (Aubrey Janik)',
       'url': 'https://www.youtube.com/watch?v=Yjwp4WMIjbc&t=337s',
       'video_id': 'Yjwp4WMIjbc'},
      {'author': 'Khushnud Numonov',
       'channel': 'Khushnud Numonov',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:51](https://www.youtube.com/watch?v=-SDfxVQEXXs&t=351s)',
       'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                    'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                    'zero-owned-metal investor vehicle co-hosting (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': '18 trips one of them was comfort one of them was black suv and the rest of it '
               'was uber black regular uber black so this is interesting interesting thing '
               'because if you are planning to get your own car.',
       'timestamp': 351,
       'timestamp_label': '[00:05:51]',
       'timestamp_seconds': 351,
       'tip': '18 trips one of them was comfort one of them was black suv and the rest of it '
              'was uber black regular uber black so this is interesting interesting thing '
              'because if you are planning to get your own car.',
       'title': "Uber Black Day 1 | You Won't Believe How Much I Made (Khushnud Numonov)",
       'url': 'https://www.youtube.com/watch?v=-SDfxVQEXXs&t=351s',
       'video_id': '-SDfxVQEXXs'},
      {'author': 'King of Rentals',
       'channel': 'King of Rentals',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:21](https://www.youtube.com/watch?v=sCxmSbzhAjM&t=21s)',
       'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                    'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                    'zero-owned-metal investor vehicle co-hosting (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'I started my rental business about 6 years ago with my brother Zach. We scaled '
               'it all the way to 300 cars from one in the very beginning. We have two '
               "locations now, and we're scaling faster than ever.",
       'timestamp': 21,
       'timestamp_label': '[00:00:21]',
       'timestamp_seconds': 21,
       'tip': 'I started my rental business about 6 years ago with my brother Zach. We scaled '
              'it all the way to 300 cars from one in the very beginning. We have two '
              "locations now, and we're scaling faster than ever.",
       'title': 'The Fastest Way to Build a 10-Car Rental Fleet! (King of Rentals)',
       'url': 'https://www.youtube.com/watch?v=sCxmSbzhAjM&t=21s',
       'video_id': 'sCxmSbzhAjM'},
      {'author': 'Arthur Fandunyan',
       'channel': 'Arthur Fandunyan',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:21:51](https://www.youtube.com/watch?v=d5fglf-rFOc&t=1311s)',
       'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                    'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                    'zero-owned-metal investor vehicle co-hosting (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Somebody comes in to do mechanic work, they can rent a car from us. And every '
               'business kind of feeds each other. So, at this point, with an operations '
               'manager, you are fully stepped out of operations. The team is going to run the '
               'show, and you own a business, not a job.',
       'timestamp': 1311,
       'timestamp_label': '[00:21:51]',
       'timestamp_seconds': 1311,
       'tip': 'Somebody comes in to do mechanic work, they can rent a car from us. And every '
              'business kind of feeds each other. So, at this point, with an operations '
              'manager, you are fully stepped out of operations. The team is going to run the '
              'show, and you own a business, not a job.',
       'title': 'How To Start Private Car Rentals in 2026 (Full Roadmap) (Arthur Fandunyan)',
       'url': 'https://www.youtube.com/watch?v=d5fglf-rFOc&t=1311s',
       'video_id': 'd5fglf-rFOc'}],
 12: [{'author': 'Fares and Frustrations',
       'channel': 'Fares and Frustrations',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:45](https://www.youtube.com/watch?v=TxZA7z6wXLg&t=105s)',
       'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                    'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                    'zero-owned-metal investor vehicle co-hosting (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'But, with private clients, well, you could turn one airport ride into a repeat '
               'customer, weekly rides, and corporate accounts. So, instead of chasing you '
               'actually start building relationships. And one good client can be worth more '
               'than an entire day on the app.',
       'timestamp': 105,
       'timestamp_label': '[00:01:45]',
       'timestamp_seconds': 105,
       'tip': 'But, with private clients, well, you could turn one airport ride into a repeat '
              'customer, weekly rides, and corporate accounts. So, instead of chasing you '
              'actually start building relationships. And one good client can be worth more '
              'than an entire day on the app.',
       'title': 'How I Started My Private "Black Car" Service After Uber Black in '
                'Jacksonville, Florida (Fares and Frustrations)',
       'url': 'https://www.youtube.com/watch?v=TxZA7z6wXLg&t=105s',
       'video_id': 'TxZA7z6wXLg'},
      {'author': 'Alex Auto',
       'channel': 'Alex Auto',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:45](https://www.youtube.com/watch?v=Sukdr8-ecMM&t=165s)',
       'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                    'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                    'zero-owned-metal investor vehicle co-hosting (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'And believe it or not, many of these drivers make anywhere from $2 to $500 a '
               'day on these platforms. So if you do the math, they may be making anywhere '
               'from 145 to $2,500 every single month. Uh every single week, sorry.',
       'timestamp': 165,
       'timestamp_label': '[00:02:45]',
       'timestamp_seconds': 165,
       'tip': 'And believe it or not, many of these drivers make anywhere from $2 to $500 a '
              'day on these platforms. So if you do the math, they may be making anywhere from '
              '145 to $2,500 every single month. Uh every single week, sorry.',
       'title': 'Renting a Car to Uber Drivers: Good or Bad Idea? (Alex Auto)',
       'url': 'https://www.youtube.com/watch?v=Sukdr8-ecMM&t=165s',
       'video_id': 'Sukdr8-ecMM'},
      {'author': 'ESCAPE THE MATRIX',
       'channel': 'ESCAPE THE MATRIX',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:23](https://www.youtube.com/watch?v=q6qypIL66TM&t=23s)',
       'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                    'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                    'zero-owned-metal investor vehicle co-hosting (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Before we start day one, I got a couple things to do before I start up. As you '
               "guys can tell, I'm at the last place that I want to be at, but we are here and "
               "we're here to get some gas.",
       'timestamp': 23,
       'timestamp_label': '[00:00:23]',
       'timestamp_seconds': 23,
       'tip': 'Before we start day one, I got a couple things to do before I start up. As you '
              "guys can tell, I'm at the last place that I want to be at, but we are here and "
              "we're here to get some gas.",
       'title': 'FIRST DAY DRIVING UBER BLACK SUV IN 120K SUV (ESCAPE THE MATRIX)',
       'url': 'https://www.youtube.com/watch?v=q6qypIL66TM&t=23s',
       'video_id': 'q6qypIL66TM'},
      {'author': 'Kel King',
       'channel': 'Kel King',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:20](https://www.youtube.com/watch?v=EVlxhXnHHH8&t=80s)',
       'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                    'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                    'zero-owned-metal investor vehicle co-hosting (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "20 cars in 60 days wasn't more hours in my day. It was three systems running "
               'without me having to personally touch every single piece. Let me walk you '
               'through each one. The first system is sourcing, specifically auction access.',
       'timestamp': 80,
       'timestamp_label': '[00:01:20]',
       'timestamp_seconds': 80,
       'tip': "20 cars in 60 days wasn't more hours in my day. It was three systems running "
              'without me having to personally touch every single piece. Let me walk you '
              'through each one. The first system is sourcing, specifically auction access.',
       'title': 'How to Scale to 10 Rental Cars in 30 Days (No Turo) | $22,200/Month Explained '
                '(Kel King)',
       'url': 'https://www.youtube.com/watch?v=EVlxhXnHHH8&t=80s',
       'video_id': 'EVlxhXnHHH8'},
      {'author': 'Mr Jay Hill Network',
       'channel': 'Mr Jay Hill Network',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:28:33](https://www.youtube.com/watch?v=fqYaTfdZsQ8&t=1713s)',
       'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                    'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                    'zero-owned-metal investor vehicle co-hosting (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "All right, let's just say 90 days. All changes is about uh less than 100 a "
               'month and breaks is every couple months. So essentially, if I buy a car, I '
               'could make my money back for the car within the same year and then start '
               'making interest for as long as the car is driving.',
       'timestamp': 1713,
       'timestamp_label': '[00:28:33]',
       'timestamp_seconds': 1713,
       'tip': "All right, let's just say 90 days. All changes is about uh less than 100 a "
              'month and breaks is every couple months. So essentially, if I buy a car, I '
              'could make my money back for the car within the same year and then start making '
              'interest for as long as the car is driving.',
       'title': 'How She Turned Cheap Cars Into Weekly Income (Without Turo) (Mr Jay Hill '
                'Network)',
       'url': 'https://www.youtube.com/watch?v=fqYaTfdZsQ8&t=1713s',
       'video_id': 'fqYaTfdZsQ8'},
      {'author': 'Your Solvent Uncle',
       'channel': 'Your Solvent Uncle',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:45](https://www.youtube.com/watch?v=gI2NWnEw3Mo&t=165s)',
       'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                    'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                    'zero-owned-metal investor vehicle co-hosting (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Get into a franchise and so to actually start a chauffeur business think about '
               'the business plan legal structure licenses and permits standard office '
               'facility in a suitable location luxury cars employees and funding.',
       'timestamp': 165,
       'timestamp_label': '[00:02:45]',
       'timestamp_seconds': 165,
       'tip': 'Get into a franchise and so to actually start a chauffeur business think about '
              'the business plan legal structure licenses and permits standard office facility '
              'in a suitable location luxury cars employees and funding.',
       'title': 'How to Start a Chauffeur Business 2026: How My Luxury Driving Blueprint '
                'Worked, Moves You Need Today (Your Solvent Uncle)',
       'url': 'https://www.youtube.com/watch?v=gI2NWnEw3Mo&t=165s',
       'video_id': 'gI2NWnEw3Mo'},
      {'author': 'Alex Auto',
       'channel': 'Alex Auto',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:49](https://www.youtube.com/watch?v=Q9fRvJfTKk0&t=49s)',
       'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                    'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                    'zero-owned-metal investor vehicle co-hosting (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "Well, in this video, I'm going to talk about everything that I did in order to "
               'be able to start and launch my car rental business, acquire my first renter, '
               'and start getting paid. The very first thing you need to do before you do '
               'anything else is to have an LLC.',
       'timestamp': 49,
       'timestamp_label': '[00:00:49]',
       'timestamp_seconds': 49,
       'tip': "Well, in this video, I'm going to talk about everything that I did in order to "
              'be able to start and launch my car rental business, acquire my first renter, '
              'and start getting paid. The very first thing you need to do before you do '
              'anything else is to have an LLC.',
       'title': 'How to Start a Private Car Rental Business With Just 1 Car (Step-by-Step) '
                '(Alex Auto)',
       'url': 'https://www.youtube.com/watch?v=Q9fRvJfTKk0&t=49s',
       'video_id': 'Q9fRvJfTKk0'},
      {'author': 'King of Rentals',
       'channel': 'King of Rentals',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:59](https://www.youtube.com/watch?v=DOrgMXhPDXs&t=119s)',
       'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                    'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                    'zero-owned-metal investor vehicle co-hosting (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "Just for normal rideshare driver. Typically if they're paying weekly, they're "
               "going to pay anywhere from 350 to 450 per week. Daily's always more expensive. "
               "It's always 20% more expensive. So for example, if you have 350 a week, that "
               'means that this would be 50 per day.',
       'timestamp': 119,
       'timestamp_label': '[00:01:59]',
       'timestamp_seconds': 119,
       'tip': "Just for normal rideshare driver. Typically if they're paying weekly, they're "
              "going to pay anywhere from 350 to 450 per week. Daily's always more expensive. "
              "It's always 20% more expensive. So for example, if you have 350 a week, that "
              'means that this would be 50 per day.',
       'title': 'How we make $1,500+ per car monthly (WITHOUT Turo)!! (King of Rentals)',
       'url': 'https://www.youtube.com/watch?v=DOrgMXhPDXs&t=119s',
       'video_id': 'DOrgMXhPDXs'},
      {'author': 'Kel King',
       'channel': 'Kel King',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:41:33](https://www.youtube.com/watch?v=7l7A5buuie0&t=2493s)',
       'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                    'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                    'zero-owned-metal investor vehicle co-hosting (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Yeah, I think the biggest thing cuz you know you make your money back in 90 '
               "days. That's the golden rule for this business is a 90-day return on "
               'investment. So the most business credit card is what 12 months to 0% APR, '
               'right?',
       'timestamp': 2493,
       'timestamp_label': '[00:41:33]',
       'timestamp_seconds': 2493,
       'tip': 'Yeah, I think the biggest thing cuz you know you make your money back in 90 '
              "days. That's the golden rule for this business is a 90-day return on "
              'investment. So the most business credit card is what 12 months to 0% APR, '
              'right?',
       'title': 'How To Start A Car Rental Business in 2026 (Kel King)',
       'url': 'https://www.youtube.com/watch?v=7l7A5buuie0&t=2493s',
       'video_id': '7l7A5buuie0'},
      {'author': 'Demario Mccowan',
       'channel': 'Demario Mccowan',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:48:31](https://www.youtube.com/watch?v=taXFg2qEMew&t=2911s)',
       'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                    'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                    'zero-owned-metal investor vehicle co-hosting (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'I\'m like, "Yo, where is this car?" I thought he was supposed to be at the '
               'office. " He goes, "Okay, we\'ll figure it out." That was before when we\'re '
               "really understaffed, so we forgot about it cuz we're just doing everything. On "
               "the 11th day, I'm at home at night.",
       'timestamp': 2911,
       'timestamp_label': '[00:48:31]',
       'timestamp_seconds': 2911,
       'tip': 'I\'m like, "Yo, where is this car?" I thought he was supposed to be at the '
              'office. " He goes, "Okay, we\'ll figure it out." That was before when we\'re '
              "really understaffed, so we forgot about it cuz we're just doing everything. On "
              "the 11th day, I'm at home at night.",
       'title': 'How to Start a Car Rental Business in 2025 (Scale to 400+ Cars) (Demario '
                'Mccowan)',
       'url': 'https://www.youtube.com/watch?v=taXFg2qEMew&t=2911s',
       'video_id': 'taXFg2qEMew'},
      {'author': '41.22 Inc.',
       'channel': '41.22 Inc.',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:53](https://www.youtube.com/watch?v=87xqndlXO8o&t=53s)',
       'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                    'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                    'zero-owned-metal investor vehicle co-hosting (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "So no matter what thieves do they can't start the car because the starter "
               "motor won't activate it just clicks here's how easy it is to install so you "
               "access your fuse box you pull your vehicle's Factory starter relay out then "
               'you plug in the relay PP pass.',
       'timestamp': 53,
       'timestamp_label': '[00:00:53]',
       'timestamp_seconds': 53,
       'tip': "So no matter what thieves do they can't start the car because the starter motor "
              "won't activate it just clicks here's how easy it is to install so you access "
              "your fuse box you pull your vehicle's Factory starter relay out then you plug "
              'in the relay PP pass.',
       'title': 'The FIRST drop-in KILL SWITCH (anti-theft) (41.22 Inc.)',
       'url': 'https://www.youtube.com/watch?v=87xqndlXO8o&t=53s',
       'video_id': '87xqndlXO8o'},
      {'author': 'TJackk',
       'channel': 'TJackk',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:09](https://www.youtube.com/watch?v=IDj4RVhbWtE&t=189s)',
       'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                    'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                    'zero-owned-metal investor vehicle co-hosting (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "And that's if they hustling. And there've been times where I talked to some X "
               'drivers, and they barely seeing $300 to $500 per week. You have to hustle in '
               "this business. Versus a Uber Black driver, they don't have to hustle as hard "
               'as a X driver and still make more than him.',
       'timestamp': 189,
       'timestamp_label': '[00:03:09]',
       'timestamp_seconds': 189,
       'tip': "And that's if they hustling. And there've been times where I talked to some X "
              'drivers, and they barely seeing $300 to $500 per week. You have to hustle in '
              "this business. Versus a Uber Black driver, they don't have to hustle as hard as "
              'a X driver and still make more than him.',
       'title': 'This Is Why Uber Black Drivers Don’t Go Back To UberX (Part 1) (TJackk)',
       'url': 'https://www.youtube.com/watch?v=IDj4RVhbWtE&t=189s',
       'video_id': 'IDj4RVhbWtE'},
      {'author': 'Rideshare Professor',
       'channel': 'Rideshare Professor',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:32](https://www.youtube.com/watch?v=7e3yD_HEDec&t=512s)',
       'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                    'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                    'zero-owned-metal investor vehicle co-hosting (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "Still come back to me whether it's Christmas whether it's they check in with "
               "me they let me know how their business is going how it's growing and um I'm "
               "super proud of them it's great start your own business today start your flea "
               'today have a good one.',
       'timestamp': 512,
       'timestamp_label': '[00:08:32]',
       'timestamp_seconds': 512,
       'tip': "Still come back to me whether it's Christmas whether it's they check in with me "
              "they let me know how their business is going how it's growing and um I'm super "
              "proud of them it's great start your own business today start your flea today "
              'have a good one.',
       'title': 'Start your own Uber Fleet today. Great ROI (return on investment). Learn the '
                'formula. How 2 run it. (Rideshare Professor)',
       'url': 'https://www.youtube.com/watch?v=7e3yD_HEDec&t=512s',
       'video_id': '7e3yD_HEDec'},
      {'author': 'BusinessRocket',
       'channel': 'BusinessRocket',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:53](https://www.youtube.com/watch?v=JmrjPmk_Gpo&t=113s)',
       'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                    'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                    'zero-owned-metal investor vehicle co-hosting (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "This video is very helpful if you have any questions leave it below we'll get "
               'you answers right away and I look forward to speaking to you in the future '
               'have a great day.',
       'timestamp': 113,
       'timestamp_label': '[00:01:53]',
       'timestamp_seconds': 113,
       'tip': "This video is very helpful if you have any questions leave it below we'll get "
              'you answers right away and I look forward to speaking to you in the future have '
              'a great day.',
       'title': 'TCP License: Vehicle Requirements for the California TCP Limousine / Charter '
                'Party License (BusinessRocket)',
       'url': 'https://www.youtube.com/watch?v=JmrjPmk_Gpo&t=113s',
       'video_id': 'JmrjPmk_Gpo'},
      {'author': 'FOX 2 Detroit',
       'channel': 'FOX 2 Detroit',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:01](https://www.youtube.com/watch?v=rvid3s_9KZA&t=121s)',
       'relevance': 'Attributed practitioner commentary on Uber Fleet Partner top-of-waterfall '
                    'driver leases, commercial TLC/TCP Black SUV shift dispatch, and '
                    'zero-owned-metal investor vehicle co-hosting (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'IN THE MEANTIME, A WAITING GAME FOR UBER BLACK DRIVERS, HOPING THE AIRPORT AND '
               'UBER CAN COME TO AN AGREEMENT FAST. I WILL HANDLE MY PRIVATE BUSINESS THAT, '
               'YOU KNOW, I BUILT UP MY OWN CLIENTELE OVER TIME NOW.',
       'timestamp': 121,
       'timestamp_label': '[00:02:01]',
       'timestamp_seconds': 121,
       'tip': 'IN THE MEANTIME, A WAITING GAME FOR UBER BLACK DRIVERS, HOPING THE AIRPORT AND '
              'UBER CAN COME TO AN AGREEMENT FAST. I WILL HANDLE MY PRIVATE BUSINESS THAT, YOU '
              'KNOW, I BUILT UP MY OWN CLIENTELE OVER TIME NOW.',
       'title': 'Uber Black drivers stopped from picking up customers at Metro Airport. (FOX 2 '
                'Detroit)',
       'url': 'https://www.youtube.com/watch?v=rvid3s_9KZA&t=121s',
       'video_id': 'rvid3s_9KZA'}]}
