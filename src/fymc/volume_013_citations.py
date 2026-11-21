"""Curated 180-citation Intellectual Property Licensing baseline (15 per chapter across Q1-Q12) mined strictly from verified Intellectual Property Licensing YouTube transcripts."""
from __future__ import annotations

CHAPTER_KEYWORDS: dict[int, set[str]] = {1: {'act',
     'advance',
     'against',
     'agency',
     'agent',
     'algorithm',
     'annual',
     'assignment',
     'audit',
     'brand',
     'broker',
     'brokerage',
     'building',
     'business',
     'cad',
     'catalog',
     'character',
     'clause',
     'client',
     'clients',
     'commercial',
     'commercialization',
     'compliance',
     'contract',
     'control',
     'copyright',
     'corporate',
     'database',
     'dataset',
     'deal',
     'deals',
     'deductions',
     'firm',
     'margin',
     'market',
     'model',
     'niche',
     'operator',
     'revenue',
     'service',
     'value'},
 2: {'act',
     'advance',
     'against',
     'agency',
     'agent',
     'algorithm',
     'annual',
     'assignment',
     'audit',
     'brand',
     'broker',
     'brokerage',
     'budget',
     'building',
     'business',
     'buyer',
     'cad',
     'catalog',
     'character',
     'clause',
     'commercial',
     'commercialization',
     'compliance',
     'contract',
     'control',
     'copyright',
     'corporate',
     'customer',
     'database',
     'dataset',
     'deal',
     'deals',
     'decision',
     'deductions',
     'escrow',
     'fee',
     'fees',
     'invoice',
     'pay',
     'payment',
     'pays',
     'retainer'},
 3: {'act',
     'advance',
     'against',
     'agency',
     'agent',
     'algorithm',
     'annual',
     'assignment',
     'audit',
     'brand',
     'broker',
     'brokerage',
     'building',
     'business',
     'cad',
     'cash',
     'cashflow',
     'catalog',
     'character',
     'clause',
     'commercial',
     'commercialization',
     'commission',
     'compliance',
     'contract',
     'control',
     'copyright',
     'corporate',
     'cost',
     'costs',
     'database',
     'dataset',
     'deal',
     'deals',
     'deductions',
     'economics',
     'margin',
     'margins',
     'price',
     'pricing',
     'profit',
     'roi',
     'unit'},
 4: {'act',
     'advance',
     'against',
     'agency',
     'agent',
     'algorithm',
     'annual',
     'assignment',
     'audit',
     'brand',
     'broker',
     'brokerage',
     'budget',
     'building',
     'business',
     'cad',
     'capital',
     'catalog',
     'character',
     'clause',
     'commercial',
     'commercialization',
     'compliance',
     'contract',
     'control',
     'copyright',
     'corporate',
     'database',
     'dataset',
     'deal',
     'deals',
     'deductions',
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
 5: {'act',
     'advance',
     'against',
     'agency',
     'agent',
     'algorithm',
     'annual',
     'assignment',
     'audit',
     'avoid',
     'brand',
     'broker',
     'brokerage',
     'building',
     'business',
     'cad',
     'catalog',
     'character',
     'clause',
     'clawback',
     'commercial',
     'commercialization',
     'compliance',
     'contract',
     'control',
     'copyright',
     'corporate',
     'database',
     'dataset',
     'deal',
     'deals',
     'deductions',
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
 6: {'act',
     'advance',
     'against',
     'agency',
     'agent',
     'algorithm',
     'annual',
     'assignment',
     'audit',
     'brand',
     'broker',
     'brokerage',
     'building',
     'business',
     'cad',
     'catalog',
     'character',
     'clause',
     'client',
     'commercial',
     'commercialization',
     'compliance',
     'contract',
     'control',
     'copyright',
     'corporate',
     'data',
     'database',
     'dataset',
     'deal',
     'deals',
     'deductions',
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
 7: {'act',
     'advance',
     'against',
     'agency',
     'agent',
     'algorithm',
     'annual',
     'assignment',
     'audit',
     'brand',
     'broker',
     'brokerage',
     'building',
     'business',
     'cad',
     'catalog',
     'character',
     'checklist',
     'clause',
     'commercial',
     'commercialization',
     'compliance',
     'contract',
     'control',
     'copyright',
     'corporate',
     'database',
     'dataset',
     'deal',
     'deals',
     'deductions',
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
 8: {'act',
     'advance',
     'against',
     'agency',
     'agent',
     'algorithm',
     'annual',
     'api',
     'assignment',
     'audit',
     'brand',
     'broker',
     'brokerage',
     'building',
     'business',
     'cad',
     'catalog',
     'character',
     'clause',
     'commercial',
     'commercialization',
     'compliance',
     'contract',
     'control',
     'copyright',
     'corporate',
     'crm',
     'data',
     'database',
     'dataset',
     'deal',
     'deals',
     'deductions',
     'platform',
     'portal',
     'scraper',
     'search',
     'software',
     'tool',
     'tools',
     'tracking'},
 9: {'act',
     'advance',
     'against',
     'agency',
     'agent',
     'agreement',
     'algorithm',
     'annual',
     'assignment',
     'audit',
     'brand',
     'broker',
     'brokerage',
     'building',
     'business',
     'cad',
     'catalog',
     'character',
     'clause',
     'commercial',
     'commercialization',
     'compliance',
     'contract',
     'control',
     'copyright',
     'corporate',
     'database',
     'dataset',
     'deal',
     'deals',
     'deductions',
     'disclosure',
     'law',
     'legal',
     'license',
     'outreach',
     'rules',
     'script',
     'state',
     'terms'},
 10: {'act',
      'advance',
      'against',
      'agency',
      'agent',
      'ai',
      'algorithm',
      'annual',
      'assignment',
      'audit',
      'automate',
      'automation',
      'brand',
      'broker',
      'brokerage',
      'building',
      'business',
      'cad',
      'catalog',
      'character',
      'clause',
      'commercial',
      'commercialization',
      'compliance',
      'contract',
      'control',
      'copyright',
      'corporate',
      'dashboard',
      'database',
      'dataset',
      'deal',
      'deals',
      'deductions',
      'leverage',
      'pipeline',
      'scale',
      'script',
      'speed',
      'template',
      'workflow'},
 11: {'act',
      'advance',
      'against',
      'agency',
      'agent',
      'algorithm',
      'annual',
      'assignment',
      'audit',
      'brand',
      'broker',
      'brokerage',
      'building',
      'business',
      'cad',
      'catalog',
      'character',
      'clause',
      'commercial',
      'commercialization',
      'compliance',
      'contract',
      'contractor',
      'control',
      'copyright',
      'corporate',
      'database',
      'dataset',
      'deal',
      'deals',
      'deductions',
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
 12: {'act',
      'action',
      'advance',
      'against',
      'agency',
      'agent',
      'algorithm',
      'annual',
      'assignment',
      'audit',
      'brand',
      'broker',
      'brokerage',
      'building',
      'business',
      'cad',
      'catalog',
      'character',
      'clause',
      'commercial',
      'commercialization',
      'compliance',
      'contract',
      'control',
      'copyright',
      'corporate',
      'database',
      'dataset',
      'day',
      'days',
      'deal',
      'deals',
      'deductions',
      'launch',
      'milestone',
      'month',
      'plan',
      'roadmap',
      'sprint',
      'start',
      'thirty',
      'week'}}

BASELINE_EXPERT_CITATIONS_BY_CHAPTER: dict[int, list[dict]] = {1: [{'author': 'Bao Tran, Esq. | Patent Attorney',
      'channel': 'Bao Tran, Esq. | Patent Attorney',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:26](https://www.youtube.com/watch?v=SkIAUEkenak&t=326s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Let's talk about understanding the licensee's business model. The licensee "
              "needs to consider the value of the product or the service. What is a licensee's "
              "view of the market and the competition? What is a licensee's business model? "
              'How would they finance the business?',
      'timestamp': 326,
      'timestamp_label': '[00:05:26]',
      'timestamp_seconds': 326,
      'tip': "Let's talk about understanding the licensee's business model. The licensee needs "
             "to consider the value of the product or the service. What is a licensee's view "
             "of the market and the competition? What is a licensee's business model? How "
             'would they finance the business?',
      'title': 'Patent Licensing Strategy: Royalties, Equity & Exclusive Rights Explained (Bao '
               'Tran, Esq. | Patent Attorney)',
      'url': 'https://www.youtube.com/watch?v=SkIAUEkenak&t=326s',
      'video_id': 'SkIAUEkenak'},
     {'author': 'Sync Warehouse',
      'channel': 'Sync Warehouse',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:52](https://www.youtube.com/watch?v=M7AeOQ9cxtQ&t=412s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'For composers, they provide another way to monetize a catalog through upfront '
              "payments, revenue sharing, or download-based compensation. It's a different "
              "business model than traditional sync, but it's become an important part of "
              "today's licensing landscape.",
      'timestamp': 412,
      'timestamp_label': '[00:06:52]',
      'timestamp_seconds': 412,
      'tip': 'For composers, they provide another way to monetize a catalog through upfront '
             "payments, revenue sharing, or download-based compensation. It's a different "
             "business model than traditional sync, but it's become an important part of "
             "today's licensing landscape.",
      'title': 'What Is Sync Licensing? (And How It Actually Works) (Sync Warehouse)',
      'url': 'https://www.youtube.com/watch?v=M7AeOQ9cxtQ&t=412s',
      'video_id': 'M7AeOQ9cxtQ'},
     {'author': 'Patent pc',
      'channel': 'Patent pc',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:59](https://www.youtube.com/watch?v=Tv_OWgYldPw&t=299s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'IP filing patents in the emerging field, such as ai, robotics, to future proof '
              'the business. When you have a deal structure, you can be flexible. You can use '
              'a hybrid payment model where you combine upfront payment with back end revenue '
              'sharing to align the incentives.',
      'timestamp': 299,
      'timestamp_label': '[00:04:59]',
      'timestamp_seconds': 299,
      'tip': 'IP filing patents in the emerging field, such as ai, robotics, to future proof '
             'the business. When you have a deal structure, you can be flexible. You can use a '
             'hybrid payment model where you combine upfront payment with back end revenue '
             'sharing to align the incentives.',
      'title': 'How to Monetize Unused Intellectual Property and Patents (Patent pc)',
      'url': 'https://www.youtube.com/watch?v=Tv_OWgYldPw&t=299s',
      'video_id': 'Tv_OWgYldPw'},
     {'author': 'Dr. Lauryn B',
      'channel': 'Dr. Lauryn B',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:45](https://www.youtube.com/watch?v=QRv3A_DETg4&t=405s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'t have time to go through a course in a lot of cases that it's better to um "
              "invest in the money just to have it done because it's a faster way to deliver "
              'better client care or patient care. It increases the value of the service '
              "you're providing instantly.",
      'timestamp': 405,
      'timestamp_label': '[00:06:45]',
      'timestamp_seconds': 405,
      'tip': "'t have time to go through a course in a lot of cases that it's better to um "
             "invest in the money just to have it done because it's a faster way to deliver "
             "better client care or patient care. It increases the value of the service you're "
             'providing instantly.',
      'title': 'What Is Licensing? The Business Model That Turns Your Knowledge Into Scalable '
               'Revenue (Dr. Lauryn B)',
      'url': 'https://www.youtube.com/watch?v=QRv3A_DETg4&t=405s',
      'video_id': 'QRv3A_DETg4'},
     {'author': 'TrademarkLawyer',
      'channel': 'TrademarkLawyer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:50](https://www.youtube.com/watch?v=K6BFUviYg0Q&t=50s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Players that we might see in the market as you guys know i have another '
              'business or another brand and it is called stowy joey here is the link if '
              "you're.",
      'timestamp': 50,
      'timestamp_label': '[00:00:50]',
      'timestamp_seconds': 50,
      'tip': 'Players that we might see in the market as you guys know i have another business '
             "or another brand and it is called stowy joey here is the link if you're.",
      'title': 'Licensing Your Trademarks (Intellectual Property) Without A Lawyer! PASSIVE '
               'INCOME Deals (TrademarkLawyer)',
      'url': 'https://www.youtube.com/watch?v=K6BFUviYg0Q&t=50s',
      'video_id': 'K6BFUviYg0Q'},
     {'author': 'Licensing Consulting Group',
      'channel': 'Licensing Consulting Group',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:12](https://www.youtube.com/watch?v=0MpPL7OXNr4&t=72s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Haven't thought of and looking at their business model in different matters I "
              'really love the way the presentation was given I loved the atmosphere and it '
              'was.',
      'timestamp': 72,
      'timestamp_label': '[00:01:12]',
      'timestamp_seconds': 72,
      'tip': "Haven't thought of and looking at their business model in different matters I "
             'really love the way the presentation was given I loved the atmosphere and it '
             'was.',
      'title': 'Turn Intellectual Property Into Revenue | Licensing & Commercialization '
               'Strategy (Licensing Consulting Group)',
      'url': 'https://www.youtube.com/watch?v=0MpPL7OXNr4&t=72s',
      'video_id': '0MpPL7OXNr4'},
     {'author': 'CNBC International Live',
      'channel': 'CNBC International Live',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:07](https://www.youtube.com/watch?v=KpR6WOaw0vM&t=67s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Smart business model because you're concentrating on your core business so for "
              'example if if you were you know Scots which is a lawn and garden company.',
      'timestamp': 67,
      'timestamp_label': '[00:01:07]',
      'timestamp_seconds': 67,
      'tip': "Smart business model because you're concentrating on your core business so for "
             'example if if you were you know Scots which is a lawn and garden company.',
      'title': 'Brand Licensing Europe: LIMA President upbeat on licensing business | '
               'Marketing Media Money (CNBC International Live)',
      'url': 'https://www.youtube.com/watch?v=KpR6WOaw0vM&t=67s',
      'video_id': 'KpR6WOaw0vM'},
     {'author': 'CAM Logic, Inc.',
      'channel': 'CAM Logic, Inc.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:34](https://www.youtube.com/watch?v=jv3KcPKvwZs&t=994s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Generative design algorithm it will generate and optimize the design so that '
              "you have a you know very efficient model when you're done.",
      'timestamp': 994,
      'timestamp_label': '[00:16:34]',
      'timestamp_seconds': 994,
      'tip': 'Generative design algorithm it will generate and optimize the design so that you '
             "have a you know very efficient model when you're done.",
      'title': 'Leveraging Value Based Licensing within NX & Solid Edge Webinar (CAM Logic, '
               'Inc.)',
      'url': 'https://www.youtube.com/watch?v=jv3KcPKvwZs&t=994s',
      'video_id': 'jv3KcPKvwZs'},
     {'author': 'NVIDIA Developer',
      'channel': 'NVIDIA Developer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:18:23](https://www.youtube.com/watch?v=7NRKyXl9j6U&t=1103s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Quick LS just to make sure that that client configuration token is in the right '
              'place and it is so now all we need to do is we need to restart the grid D '
              'service to pick up that token.',
      'timestamp': 1103,
      'timestamp_label': '[00:18:23]',
      'timestamp_seconds': 1103,
      'tip': 'Quick LS just to make sure that that client configuration token is in the right '
             'place and it is so now all we need to do is we need to restart the grid D '
             'service to pick up that token.',
      'title': 'Creating a License Service for NVIDIA AI Enterprise or Virtual GPU (NVIDIA '
               'Developer)',
      'url': 'https://www.youtube.com/watch?v=7NRKyXl9j6U&t=1103s',
      'video_id': '7NRKyXl9j6U'},
     {'author': 'Chartered Institute of Patent Attorneys',
      'channel': 'Chartered Institute of Patent Attorneys',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:11](https://www.youtube.com/watch?v=uTreJGUMqMs&t=71s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'We patented worldwide means that we get about 10 more seats in the equivalent '
              'amount of space in the business class cabin and so for them to be able to get '
              "10 more revenue from the same space in the aircraft is everything really it's a "
              'massive revolution.',
      'timestamp': 71,
      'timestamp_label': '[00:01:11]',
      'timestamp_seconds': 71,
      'tip': 'We patented worldwide means that we get about 10 more seats in the equivalent '
             'amount of space in the business class cabin and so for them to be able to get 10 '
             "more revenue from the same space in the aircraft is everything really it's a "
             'massive revolution.',
      'title': 'Turning ideas into profits - licensing your patents (Chartered Institute of '
               'Patent Attorneys)',
      'url': 'https://www.youtube.com/watch?v=uTreJGUMqMs&t=71s',
      'video_id': 'uTreJGUMqMs'},
     {'author': 'J.D. Houvener / Bold Patents Law Firm',
      'channel': 'J.D. Houvener / Bold Patents Law Firm',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:25](https://www.youtube.com/watch?v=Vi4MIcyHOFE&t=385s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Established yourself in the market and you see some new entrants that are kind '
              'of creeping getting close to and in your mind confusingly similar with some of '
              'your clients sure what actions can you take can you be the good guy.',
      'timestamp': 385,
      'timestamp_label': '[00:06:25]',
      'timestamp_seconds': 385,
      'tip': 'Established yourself in the market and you see some new entrants that are kind '
             'of creeping getting close to and in your mind confusingly similar with some of '
             'your clients sure what actions can you take can you be the good guy.',
      'title': 'Patent and Trademark Monetization through Licensing and Selling (J.D. Houvener '
               '/ Bold Patents Law Firm)',
      'url': 'https://www.youtube.com/watch?v=Vi4MIcyHOFE&t=385s',
      'video_id': 'Vi4MIcyHOFE'},
     {'author': 'Patent pc',
      'channel': 'Patent pc',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:23](https://www.youtube.com/watch?v=TYb3i3iIHEQ&t=83s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Uh you can sell the patents to aggregators uh to companies who compete against '
              'each other or to startups for a lump sum amount of money. Um the easiest way uh '
              'to do this is to work with brokers to maximize your value uh because they know '
              'a lot of potential prospects.',
      'timestamp': 83,
      'timestamp_label': '[00:01:23]',
      'timestamp_seconds': 83,
      'tip': 'Uh you can sell the patents to aggregators uh to companies who compete against '
             'each other or to startups for a lump sum amount of money. Um the easiest way uh '
             'to do this is to work with brokers to maximize your value uh because they know a '
             'lot of potential prospects.',
      'title': "5 Patent Monetization Strategies Inventors Don't Know About (Patent pc)",
      'url': 'https://www.youtube.com/watch?v=TYb3i3iIHEQ&t=83s',
      'video_id': 'TYb3i3iIHEQ'},
     {'author': 'inventRightTV',
      'channel': 'inventRightTV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:51](https://www.youtube.com/watch?v=ykqpNKDKFEE&t=51s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The business model that is being taught at the University level is to start a '
              'business but not everybody wants to start a business not every product.',
      'timestamp': 51,
      'timestamp_label': '[00:00:51]',
      'timestamp_seconds': 51,
      'tip': 'The business model that is being taught at the University level is to start a '
             'business but not everybody wants to start a business not every product.',
      'title': 'Who is Stephen Key? (inventRightTV)',
      'url': 'https://www.youtube.com/watch?v=ykqpNKDKFEE&t=51s',
      'video_id': 'ykqpNKDKFEE'},
     {'author': 'SeltzerLicensingGrp',
      'channel': 'SeltzerLicensingGrp',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:04](https://www.youtube.com/watch?v=qx___lyJ5yQ&t=124s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Cents on this transaction 10% of the $5 but what's interesting is that they "
              "probably have very little overhead for that transaction so that's that's a nice "
              'margin that they enjoy probably the highest margin.',
      'timestamp': 124,
      'timestamp_label': '[00:02:04]',
      'timestamp_seconds': 124,
      'tip': "Cents on this transaction 10% of the $5 but what's interesting is that they "
             "probably have very little overhead for that transaction so that's that's a nice "
             'margin that they enjoy probably the highest margin.',
      'title': 'Licensing Basics: The Royalty Rate and Minimum Guarantee [Part 7/10] '
               '(SeltzerLicensingGrp)',
      'url': 'https://www.youtube.com/watch?v=qx___lyJ5yQ&t=124s',
      'video_id': 'qx___lyJ5yQ'},
     {'author': 'inventRightTV',
      'channel': 'inventRightTV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:46](https://www.youtube.com/watch?v=5pNsi_2H-J4&t=46s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Mistakes and before when we say students we call our clients students because '
              'we teach and coach and Mentor we people asking that like I I I want to become '
              'a.',
      'timestamp': 46,
      'timestamp_label': '[00:00:46]',
      'timestamp_seconds': 46,
      'tip': 'Mistakes and before when we say students we call our clients students because we '
             'teach and coach and Mentor we people asking that like I I I want to become a.',
      'title': 'How Much Money Will You Make Licensing? (Royalties) (inventRightTV)',
      'url': 'https://www.youtube.com/watch?v=5pNsi_2H-J4&t=46s',
      'video_id': '5pNsi_2H-J4'}],
 2: [{'author': 'Simple Explain',
      'channel': 'Simple Explain',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:22](https://www.youtube.com/watch?v=2-_h0sI3YQI&t=202s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'For example, individuals or businesses must often pay licensing fees to a '
              'government agency in order to practice a certain profession or engage in a '
              'particular line of business.',
      'timestamp': 202,
      'timestamp_label': '[00:03:22]',
      'timestamp_seconds': 202,
      'tip': 'For example, individuals or businesses must often pay licensing fees to a '
             'government agency in order to practice a certain profession or engage in a '
             'particular line of business.',
      'title': 'Licensing Fee: Definition, How It Works vs. Royalty, and Examples (Simple '
               'Explain)',
      'url': 'https://www.youtube.com/watch?v=2-_h0sI3YQI&t=202s',
      'video_id': '2-_h0sI3YQI'},
     {'author': 'Useless Money',
      'channel': 'Useless Money',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:43](https://www.youtube.com/watch?v=xkXjle5Spjw&t=223s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The second model is a fixed license fee. A customer pays an agreed amount for '
              'permission to use specified rights over a defined period or under defined '
              'conditions. The third is an upfront payment combined with future royalties.',
      'timestamp': 223,
      'timestamp_label': '[00:03:43]',
      'timestamp_seconds': 223,
      'tip': 'The second model is a fixed license fee. A customer pays an agreed amount for '
             'permission to use specified rights over a defined period or under defined '
             'conditions. The third is an upfront payment combined with future royalties.',
      'title': 'The Economics of Owning an IP Holding Company (Useless Money)',
      'url': 'https://www.youtube.com/watch?v=xkXjle5Spjw&t=223s',
      'video_id': 'xkXjle5Spjw'},
     {'author': 'OneHourProfessor',
      'channel': 'OneHourProfessor',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:42](https://www.youtube.com/watch?v=SU66nYi95IY&t=402s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Then clarify what the buyer approves and actually pays for. Now, a commercial '
              'agreement, it needs to connect payment with a clear contribution. So, does '
              'payment cover one set of records, updates, or new employee work?',
      'timestamp': 402,
      'timestamp_label': '[00:06:42]',
      'timestamp_seconds': 402,
      'tip': 'Then clarify what the buyer approves and actually pays for. Now, a commercial '
             'agreement, it needs to connect payment with a clear contribution. So, does '
             'payment cover one set of records, updates, or new employee work?',
      'title': 'How to License Your Data to AI Companies & Get Paid (OneHourProfessor)',
      'url': 'https://www.youtube.com/watch?v=SU66nYi95IY&t=402s',
      'video_id': 'SU66nYi95IY'},
     {'author': 'Accountancy Students Hub',
      'channel': 'Accountancy Students Hub',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:43](https://www.youtube.com/watch?v=o0riJRlxTsY&t=343s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You have to evaluate if the renewal or extension triggers the accounting for a '
              'contract modification or if it constitutes a brand new agreement altogether. '
              'And what about when a franchisee pays a huge non-refundable upfront fee just to '
              'open a restaurant?',
      'timestamp': 343,
      'timestamp_label': '[00:05:43]',
      'timestamp_seconds': 343,
      'tip': 'You have to evaluate if the renewal or extension triggers the accounting for a '
             'contract modification or if it constitutes a brand new agreement altogether. And '
             'what about when a franchisee pays a huge non-refundable upfront fee just to open '
             'a restaurant?',
      'title': 'AFAR Revenue 06: PFRS 15 Licensing – Right to Access vs. Right to Use; '
               'Usage-Based Royalties (Accountancy Students Hub)',
      'url': 'https://www.youtube.com/watch?v=o0riJRlxTsY&t=343s',
      'video_id': 'o0riJRlxTsY'},
     {'author': 'Bao Tran, Esq. | Patent Attorney',
      'channel': 'Bao Tran, Esq. | Patent Attorney',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:06](https://www.youtube.com/watch?v=k9Sb2smIIjM&t=186s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Worse yet, if you let the patent lapse because you just forgot to pay, your '
              'licensing agreement essentially evaporates. Always audit the USPTO Patent '
              'Center to verify your fees are paid up before making deals.',
      'timestamp': 186,
      'timestamp_label': '[00:03:06]',
      'timestamp_seconds': 186,
      'tip': 'Worse yet, if you let the patent lapse because you just forgot to pay, your '
             'licensing agreement essentially evaporates. Always audit the USPTO Patent Center '
             'to verify your fees are paid up before making deals.',
      'title': 'Patent Licensing: Why You’re Losing Royalties (and How to Fix It) (Bao Tran, '
               'Esq. | Patent Attorney)',
      'url': 'https://www.youtube.com/watch?v=k9Sb2smIIjM&t=186s',
      'video_id': 'k9Sb2smIIjM'},
     {'author': 'Majeston',
      'channel': 'Majeston',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:12](https://www.youtube.com/watch?v=7t871xx-ysc&t=312s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, the sync fee is like, "Yo, I\'m a music supervisor. I want to use your '
              "track for this film. I'm going to pay you $5,000 up front to license this, "
              'right?" That\'s the upfront payment you get. And then there\'s the back-end as '
              'well.',
      'timestamp': 312,
      'timestamp_label': '[00:05:12]',
      'timestamp_seconds': 312,
      'tip': 'So, the sync fee is like, "Yo, I\'m a music supervisor. I want to use your track '
             'for this film. I\'m going to pay you $5,000 up front to license this, right?" '
             "That's the upfront payment you get. And then there's the back-end as well.",
      'title': 'sync licensing basics + libraries you should submit to - MORNING CHOPS '
               '(Majeston)',
      'url': 'https://www.youtube.com/watch?v=7t871xx-ysc&t=312s',
      'video_id': '7t871xx-ysc'},
     {'author': 'Barbara “Financial Tidbitter” Aboagye',
      'channel': 'Barbara “Financial Tidbitter” Aboagye',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:52](https://www.youtube.com/watch?v=SK5CqQ61CYI&t=172s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Then you choose your currency and this is where they will give you the fee. '
              "Sometimes it's free, sometimes you have to pay for it. Sometimes it's a special "
              "case. I've already requested for this. I've already requested um for this in "
              'Okay.',
      'timestamp': 172,
      'timestamp_label': '[00:02:52]',
      'timestamp_seconds': 172,
      'tip': 'Then you choose your currency and this is where they will give you the fee. '
             "Sometimes it's free, sometimes you have to pay for it. Sometimes it's a special "
             "case. I've already requested for this. I've already requested um for this in "
             'Okay.',
      'title': 'How to Request Copyright Permission to Reuse an Image | Can You Use Images '
               'From Research Papers? (Barbara “Financial Tidbitter” Aboagye)',
      'url': 'https://www.youtube.com/watch?v=SK5CqQ61CYI&t=172s',
      'video_id': 'SK5CqQ61CYI'},
     {'author': 'Brian Fried - The Inventor Coach',
      'channel': 'Brian Fried - The Inventor Coach',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:40](https://www.youtube.com/watch?v=UnGdjQb467o&t=40s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I will make a prototype, I'm going to do 3-D CAD drawing with an engineer or an "
              "industrial designer, and I'm going to get it to a point where I can make a "
              'decision of having these options of licensing versus manufacturing.',
      'timestamp': 40,
      'timestamp_label': '[00:00:40]',
      'timestamp_seconds': 40,
      'tip': "I will make a prototype, I'm going to do 3-D CAD drawing with an engineer or an "
             "industrial designer, and I'm going to get it to a point where I can make a "
             'decision of having these options of licensing versus manufacturing.',
      'title': 'Licensing to Earn royalties Vs  Manufacturing Your Invention Idea (Brian Fried '
               '- The Inventor Coach)',
      'url': 'https://www.youtube.com/watch?v=UnGdjQb467o&t=40s',
      'video_id': 'UnGdjQb467o'},
     {'author': 'Idea2PatentAI',
      'channel': 'Idea2PatentAI',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:19](https://www.youtube.com/watch?v=ixENhsfAdEA&t=319s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'One important point, you must pay your filing fees on the same day that you '
              'submit your provisional application. The US Patent Office operates on Eastern '
              'time, so avoid filing your application until just before midnight if possible.',
      'timestamp': 319,
      'timestamp_label': '[00:05:19]',
      'timestamp_seconds': 319,
      'tip': 'One important point, you must pay your filing fees on the same day that you '
             'submit your provisional application. The US Patent Office operates on Eastern '
             'time, so avoid filing your application until just before midnight if possible.',
      'title': 'How to File a Provisional Patent Application with the USPTO (Step-by-Step) '
               '(Idea2PatentAI)',
      'url': 'https://www.youtube.com/watch?v=ixENhsfAdEA&t=319s',
      'video_id': 'ixENhsfAdEA'},
     {'author': 'Randy McGravey Music',
      'channel': 'Randy McGravey Music',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:22](https://www.youtube.com/watch?v=iF_Z6ikfzMo&t=382s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Pretty good ones the syn fees won't be as good probably as APM or Universal but "
              'you know if you have a good enough catalog then you probably will get some.',
      'timestamp': 382,
      'timestamp_label': '[00:06:22]',
      'timestamp_seconds': 382,
      'tip': "Pretty good ones the syn fees won't be as good probably as APM or Universal but "
             'you know if you have a good enough catalog then you probably will get some.',
      'title': 'Ranking The Top 5 Major Sub-Publishers (Sync Licensing) (Randy McGravey Music)',
      'url': 'https://www.youtube.com/watch?v=iF_Z6ikfzMo&t=382s',
      'video_id': 'iF_Z6ikfzMo'},
     {'author': "It's Julisa",
      'channel': "It's Julisa",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:57](https://www.youtube.com/watch?v=hoMi3ZhgFlc&t=117s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Now, sync agency, depending on what agency you signed up for, most of them take '
              'between 25 and 50% of your sync licensing fee. They do not touch your backend '
              "royalties or anything like that. So, you'll still register your song.",
      'timestamp': 117,
      'timestamp_label': '[00:01:57]',
      'timestamp_seconds': 117,
      'tip': 'Now, sync agency, depending on what agency you signed up for, most of them take '
             'between 25 and 50% of your sync licensing fee. They do not touch your backend '
             "royalties or anything like that. So, you'll still register your song.",
      'title': "How Much Can You Make From Sync Licensing? (Real Numbers Explained) (It's "
               'Julisa)',
      'url': 'https://www.youtube.com/watch?v=hoMi3ZhgFlc&t=117s',
      'video_id': 'hoMi3ZhgFlc'},
     {'author': 'Brand Licensing by Informa',
      'channel': 'Brand Licensing by Informa',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:55](https://www.youtube.com/watch?v=6dKNY_VUEIs&t=55s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The brand to stopped by the foot traffic here has been phenomenal the attendee '
              'pool here is exactly who we want to meet with vice presidents director level '
              'people decision makers on the retail level people that are trying to drive '
              'retail.',
      'timestamp': 55,
      'timestamp_label': '[00:00:55]',
      'timestamp_seconds': 55,
      'tip': 'The brand to stopped by the foot traffic here has been phenomenal the attendee '
             'pool here is exactly who we want to meet with vice presidents director level '
             'people decision makers on the retail level people that are trying to drive '
             'retail.',
      'title': 'What can licensing do for your brand? (Brand Licensing by Informa)',
      'url': 'https://www.youtube.com/watch?v=6dKNY_VUEIs&t=55s',
      'video_id': '6dKNY_VUEIs'},
     {'author': 'UpCounsel',
      'channel': 'UpCounsel',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:57](https://www.youtube.com/watch?v=mtxmo_OkhSw&t=57s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'When it comes to licensing a patent, inventors have two main options for '
              'structuring royalty payments. They can opt for a flat fee royalty, which is a '
              'one-time or periodic lumpsum payment.',
      'timestamp': 57,
      'timestamp_label': '[00:00:57]',
      'timestamp_seconds': 57,
      'tip': 'When it comes to licensing a patent, inventors have two main options for '
             'structuring royalty payments. They can opt for a flat fee royalty, which is a '
             'one-time or periodic lumpsum payment.',
      'title': 'Patent Royalties  How Much Can Inventors Really Earn (UpCounsel)',
      'url': 'https://www.youtube.com/watch?v=mtxmo_OkhSw&t=57s',
      'video_id': 'mtxmo_OkhSw'},
     {'author': 'inventRightTV',
      'channel': 'inventRightTV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:13](https://www.youtube.com/watch?v=fyUYT-gfzfU&t=193s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Patent application which is really expensive or when you cut the deal with the '
              "company you're licensing it to you can negotiate so they pay for the.",
      'timestamp': 193,
      'timestamp_label': '[00:03:13]',
      'timestamp_seconds': 193,
      'tip': 'Patent application which is really expensive or when you cut the deal with the '
             "company you're licensing it to you can negotiate so they pay for the.",
      'title': 'What You “NEED” To License Your Idea For Royalties! (inventRightTV)',
      'url': 'https://www.youtube.com/watch?v=fyUYT-gfzfU&t=193s',
      'video_id': 'fyUYT-gfzfU'},
     {'author': 'inventRightTV',
      'channel': 'inventRightTV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:49](https://www.youtube.com/watch?v=CS31715RNQk&t=349s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Or four months you're going to know gauge if there's interest we show our "
              "students how to get the company to pay for the patent yeah so you don't have "
              'to.',
      'timestamp': 349,
      'timestamp_label': '[00:05:49]',
      'timestamp_seconds': 349,
      'tip': "Or four months you're going to know gauge if there's interest we show our "
             "students how to get the company to pay for the patent yeah so you don't have to.",
      'title': 'How to License Your Product Ideas Without a Patent (inventRightTV)',
      'url': 'https://www.youtube.com/watch?v=CS31715RNQk&t=349s',
      'video_id': 'CS31715RNQk'}],
 3: [{'author': 'UpCounsel',
      'channel': 'UpCounsel',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:00](https://www.youtube.com/watch?v=xRRc9i7j5A8&t=240s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Request sample packages from past deals to evaluate their work quality. Inquire '
              'about their commission structure, how costs are covered, and whether they '
              'charge upfront fees. Most brokers work on commission, typically ranging from 10 '
              'to 30% of the sale price.',
      'timestamp': 240,
      'timestamp_label': '[00:04:00]',
      'timestamp_seconds': 240,
      'tip': 'Request sample packages from past deals to evaluate their work quality. Inquire '
             'about their commission structure, how costs are covered, and whether they charge '
             'upfront fees. Most brokers work on commission, typically ranging from 10 to 30% '
             'of the sale price.',
      'title': 'How Patent Brokers Help You Turn Intellectual Property Into Profit (UpCounsel)',
      'url': 'https://www.youtube.com/watch?v=xRRc9i7j5A8&t=240s',
      'video_id': 'xRRc9i7j5A8'},
     {'author': 'EarthTab Business School',
      'channel': 'EarthTab Business School',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:36](https://www.youtube.com/watch?v=_AP6Fd6Lwwg&t=336s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Alternatively, work with art licensing agents who pitch and manage deals for a '
              'commission, typically 30 to 50%. Eight, legal protections for licensing. '
              'Register your copyright before signing any licensing deal. Use watermarked '
              'previews and pitches.',
      'timestamp': 336,
      'timestamp_label': '[00:05:36]',
      'timestamp_seconds': 336,
      'tip': 'Alternatively, work with art licensing agents who pitch and manage deals for a '
             'commission, typically 30 to 50%. Eight, legal protections for licensing. '
             'Register your copyright before signing any licensing deal. Use watermarked '
             'previews and pitches.',
      'title': 'Passive Income Streams for Artists Module 6  Art Licensing and Royalty '
               'Agreements (EarthTab Business School)',
      'url': 'https://www.youtube.com/watch?v=_AP6Fd6Lwwg&t=336s',
      'video_id': '_AP6Fd6Lwwg'},
     {'author': 'Campus Fund',
      'channel': 'Campus Fund',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:22](https://www.youtube.com/watch?v=rbNcenaCppU&t=82s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Similarly, there's a clause around expenses. This allocates who bears the legal "
              'and transaction costs of that deal.',
      'timestamp': 82,
      'timestamp_label': '[00:01:22]',
      'timestamp_seconds': 82,
      'tip': "Similarly, there's a clause around expenses. This allocates who bears the legal "
             'and transaction costs of that deal.',
      'title': 'Binding vs Non-Binding Clauses in a Term Sheet | Startup Legal Basics '
               'Explained (Campus Fund)',
      'url': 'https://www.youtube.com/watch?v=rbNcenaCppU&t=82s',
      'video_id': 'rbNcenaCppU'},
     {'author': 'Kauffman FoundersSchool',
      'channel': 'Kauffman FoundersSchool',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:36](https://www.youtube.com/watch?v=q5uDRlH_eFo&t=96s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'In my experience, all the other terms of the deal impact the price. So until '
              "you have those negotiated, you really don't have comfort that you know what the "
              "price ought to be. It's a business question really at the end of the day.",
      'timestamp': 96,
      'timestamp_label': '[00:01:36]',
      'timestamp_seconds': 96,
      'tip': 'In my experience, all the other terms of the deal impact the price. So until you '
             "have those negotiated, you really don't have comfort that you know what the "
             "price ought to be. It's a business question really at the end of the day.",
      'title': 'Intellectual Property: Licensing (Kauffman FoundersSchool)',
      'url': 'https://www.youtube.com/watch?v=q5uDRlH_eFo&t=96s',
      'video_id': 'q5uDRlH_eFo'},
     {'author': 'EUIPO',
      'channel': 'EUIPO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:45](https://www.youtube.com/watch?v=IZLXSII8AZ8&t=645s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'RHM, which made the deal turn for GFW and prompted an immediate withdrawal of '
              'the hostile takeover bid. Eventually, the brands were taken over by another '
              'company called Tomkins, but this company paid a price that also covered the '
              'brand value.',
      'timestamp': 645,
      'timestamp_label': '[00:10:45]',
      'timestamp_seconds': 645,
      'tip': 'RHM, which made the deal turn for GFW and prompted an immediate withdrawal of '
             'the hostile takeover bid. Eventually, the brands were taken over by another '
             'company called Tomkins, but this company paid a price that also covered the '
             'brand value.',
      'title': 'IP valuation – The art of making money with your Intellectual Property (EUIPO)',
      'url': 'https://www.youtube.com/watch?v=IZLXSII8AZ8&t=645s',
      'video_id': 'IZLXSII8AZ8'},
     {'author': 'Jason Varner',
      'channel': 'Jason Varner',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:38](https://www.youtube.com/watch?v=XDzwbT8LWMQ&t=458s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s do it because, you You maybe maybe you can spend up to X dollars on "
              'outsourcing inventory at a higher price. So, whatever your whatever the cost is '
              "that's higher than your current cost per unit, maybe you have a budget of say "
              'an extra $200.',
      'timestamp': 458,
      'timestamp_label': '[00:07:38]',
      'timestamp_seconds': 458,
      'tip': "'s do it because, you You maybe maybe you can spend up to X dollars on "
             'outsourcing inventory at a higher price. So, whatever your whatever the cost is '
             "that's higher than your current cost per unit, maybe you have a budget of say an "
             'extra $200.',
      'title': 'Types of Valuable Data for AI Training (Jason Varner)',
      'url': 'https://www.youtube.com/watch?v=XDzwbT8LWMQ&t=458s',
      'video_id': 'XDzwbT8LWMQ'},
     {'author': 'IPWatchdog, Inc.',
      'channel': 'IPWatchdog, Inc.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:17:17](https://www.youtube.com/watch?v=pyi_x9MFGjs&t=1037s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s very common a lot of companies that I deal with have patents they just don't "
              "want to get involved D in the litigation and it's a business uh consideration.",
      'timestamp': 1037,
      'timestamp_label': '[00:17:17]',
      'timestamp_seconds': 1037,
      'tip': "'s very common a lot of companies that I deal with have patents they just don't "
             "want to get involved D in the litigation and it's a business uh consideration.",
      'title': 'Patent Monetization Economics: What It Costs to Turn Patents into Revenue '
               '(IPWatchdog, Inc.)',
      'url': 'https://www.youtube.com/watch?v=pyi_x9MFGjs&t=1037s',
      'video_id': 'pyi_x9MFGjs'},
     {'author': 'Matthew Anderson',
      'channel': 'Matthew Anderson',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:13](https://www.youtube.com/watch?v=-267ABEXf8o&t=373s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'It could cost the company big time and I mean big if you have a spare 10 '
              'seconds just google the phrase willful copyright infringement fine you might '
              "realize it's a lot easier and a lot less costly to just do things the right "
              'way.',
      'timestamp': 373,
      'timestamp_label': '[00:06:13]',
      'timestamp_seconds': 373,
      'tip': 'It could cost the company big time and I mean big if you have a spare 10 seconds '
             'just google the phrase willful copyright infringement fine you might realize '
             "it's a lot easier and a lot less costly to just do things the right way.",
      'title': 'Do You Own the Photos? - Photography Copyright/Licensing Simplified & '
               'Explained! (Matthew Anderson)',
      'url': 'https://www.youtube.com/watch?v=-267ABEXf8o&t=373s',
      'video_id': '-267ABEXf8o'},
     {'author': 'inventRightTV',
      'channel': 'inventRightTV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:36](https://www.youtube.com/watch?v=gxeuCPaGeHY&t=36s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "It was called, here's a plastic arrow suction cup. It's sold during "
              "Valentine's, very limited distribution, very seasonal, about $10,000. What did "
              'it cost for me to get this deal done? I sent them a one-line description.',
      'timestamp': 36,
      'timestamp_label': '[00:00:36]',
      'timestamp_seconds': 36,
      'tip': "It was called, here's a plastic arrow suction cup. It's sold during Valentine's, "
             'very limited distribution, very seasonal, about $10,000. What did it cost for me '
             'to get this deal done? I sent them a one-line description.',
      'title': 'How Much Money Stephen Key Made Licensing His Ideas (inventRightTV)',
      'url': 'https://www.youtube.com/watch?v=gxeuCPaGeHY&t=36s',
      'video_id': 'gxeuCPaGeHY'},
     {'author': 'IP Europe',
      'channel': 'IP Europe',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:12](https://www.youtube.com/watch?v=fAwWxzitmUk&t=192s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'IPRED study by the European Commission addresses a very important point, which '
              'is enforcing patents in Europe, but the focus should be in a different place.',
      'timestamp': 192,
      'timestamp_label': '[00:03:12]',
      'timestamp_seconds': 192,
      'tip': 'IPRED study by the European Commission addresses a very important point, which '
             'is enforcing patents in Europe, but the focus should be in a different place.',
      'title': 'Patents and patent licensing as a business model? Fractus co-founder Dr. '
               'Carles Puente explains how (IP Europe)',
      'url': 'https://www.youtube.com/watch?v=fAwWxzitmUk&t=192s',
      'video_id': 'fAwWxzitmUk'},
     {'author': 'SeltzerLicensingGrp',
      'channel': 'SeltzerLicensingGrp',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:50](https://www.youtube.com/watch?v=MGH55iIT-A0&t=290s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Three-year agreement then your guarantee instead of being $60,000 might be '
              'three times that amount so that is h a quick overview to to answer your '
              'question how much this is going to cost me and we wish you luck and my name is '
              'Stu Seltzer and thanks for watching.',
      'timestamp': 290,
      'timestamp_label': '[00:04:50]',
      'timestamp_seconds': 290,
      'tip': 'Three-year agreement then your guarantee instead of being $60,000 might be three '
             'times that amount so that is h a quick overview to to answer your question how '
             'much this is going to cost me and we wish you luck and my name is Stu Seltzer '
             'and thanks for watching.',
      'title': 'What Are The Financial Terms in a Licensing Deal? (SeltzerLicensingGrp)',
      'url': 'https://www.youtube.com/watch?v=MGH55iIT-A0&t=290s',
      'video_id': 'MGH55iIT-A0'},
     {'author': 'Patents Demystified',
      'channel': 'Patents Demystified',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=zel57Kej5nY&t=15s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Assignment from Elon reev Musk which is uh the Elon Musk that you know right so '
              'he assigned his rights in this invention to Tesla Motors Inc so here you got '
              'Bill.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Assignment from Elon reev Musk which is uh the Elon Musk that you know right so '
             'he assigned his rights in this invention to Tesla Motors Inc so here you got '
             'Bill.',
      'title': 'How to Access HIDDEN Patent Assignment Records & Ownership History (Patents '
               'Demystified)',
      'url': 'https://www.youtube.com/watch?v=zel57Kej5nY&t=15s',
      'video_id': 'zel57Kej5nY'},
     {'author': 'Patent pc',
      'channel': 'Patent pc',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:27](https://www.youtube.com/watch?v=A7xn_DzjKzE&t=147s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You then create a professional representation about how your patent works and '
              'then perhaps you might include information such as manufacturing cost and of '
              'course the benefits provided by the the products embodying the invention.',
      'timestamp': 147,
      'timestamp_label': '[00:02:27]',
      'timestamp_seconds': 147,
      'tip': 'You then create a professional representation about how your patent works and '
             'then perhaps you might include information such as manufacturing cost and of '
             'course the benefits provided by the the products embodying the invention.',
      'title': 'Got a Patent? Here’s How You Actually Make Money (Patent pc)',
      'url': 'https://www.youtube.com/watch?v=A7xn_DzjKzE&t=147s',
      'video_id': 'A7xn_DzjKzE'},
     {'author': 'LawShelf',
      'channel': 'LawShelf',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:45](https://www.youtube.com/watch?v=WtxlYb996kI&t=705s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Could be liable for contributory infringement of a patent claiming a mobile '
              'phone with these chips but the manufacturer of a double-a battery would not be '
              'liable for contributory infringement of a patent claim requiring a battery.',
      'timestamp': 705,
      'timestamp_label': '[00:11:45]',
      'timestamp_seconds': 705,
      'tip': 'Could be liable for contributory infringement of a patent claiming a mobile '
             'phone with these chips but the manufacturer of a double-a battery would not be '
             'liable for contributory infringement of a patent claim requiring a battery.',
      'title': 'Patent Infringement Litigation: Module 5 of 5 (LawShelf)',
      'url': 'https://www.youtube.com/watch?v=WtxlYb996kI&t=705s',
      'video_id': 'WtxlYb996kI'},
     {'author': 'inventRightTV',
      'channel': 'inventRightTV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:42:54](https://www.youtube.com/watch?v=G2JXLQrTZXI&t=2574s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '100% curbside if you go to Fishbone decom you see it there that technology to '
              'test it to get someone interested was going to be about a million.',
      'timestamp': 2574,
      'timestamp_label': '[00:42:54]',
      'timestamp_seconds': 2574,
      'tip': '100% curbside if you go to Fishbone decom you see it there that technology to '
             'test it to get someone interested was going to be about a million.',
      'title': '7 strategies to get a great licensing deal! (inventRightTV)',
      'url': 'https://www.youtube.com/watch?v=G2JXLQrTZXI&t=2574s',
      'video_id': 'G2JXLQrTZXI'}],
 4: [{'author': 'Uncover Fraud',
      'channel': 'Uncover Fraud',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:15:04](https://www.youtube.com/watch?v=9Fku-QlhyHc&t=904s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'This is typically accomplished through the use of various software tools, '
              'databases, and programming languages. A royalty audit is a contract compliance '
              'investigation that requires special forensic investigation and in-depth '
              'auditing skills.',
      'timestamp': 904,
      'timestamp_label': '[00:15:04]',
      'timestamp_seconds': 904,
      'tip': 'This is typically accomplished through the use of various software tools, '
             'databases, and programming languages. A royalty audit is a contract compliance '
             'investigation that requires special forensic investigation and in-depth auditing '
             'skills.',
      'title': 'Royalty Audit: Why Every Licensor & Artist Needs a Forensic Accountant on '
               'Their Side | Uncover Fraud (Uncover Fraud)',
      'url': 'https://www.youtube.com/watch?v=9Fku-QlhyHc&t=904s',
      'video_id': '9Fku-QlhyHc'},
     {'author': 'Jobank CPA',
      'channel': 'Jobank CPA',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:01](https://www.youtube.com/watch?v=eoUe3NebB3E&t=301s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '360,000 brand license relies entirely on your ongoing brand activity to hold '
              'its value. Recognizing those brand rights up front, treating them like a simple '
              'isolated on-premises software key, is an immediate catastrophic audit finding.',
      'timestamp': 301,
      'timestamp_label': '[00:05:01]',
      'timestamp_seconds': 301,
      'tip': '360,000 brand license relies entirely on your ongoing brand activity to hold its '
             'value. Recognizing those brand rights up front, treating them like a simple '
             'isolated on-premises software key, is an immediate catastrophic audit finding.',
      'title': 'Episode 7 ASC 606 Licensing: Functional vs. Symbolic Intellectual Property '
               '(Jobank CPA)',
      'url': 'https://www.youtube.com/watch?v=eoUe3NebB3E&t=301s',
      'video_id': 'eoUe3NebB3E'},
     {'author': 'Daymond John',
      'channel': 'Daymond John',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:06](https://www.youtube.com/watch?v=knoob7eUS6Y&t=126s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '" A LOT OF TIMES, THE LICENSE IS THREE YEARS OR FIVE YEARS, THERE ARE SOME '
              "BUSINESS DEALS WHERE THE LICENSE IS IN PERPETUITY, THAT'S A DIFFERENT TYPE OF "
              "LICENSE WE'RE TALKING ABOUT. NOW, WHAT IS MY OBLIGATION?",
      'timestamp': 126,
      'timestamp_label': '[00:02:06]',
      'timestamp_seconds': 126,
      'tip': '" A LOT OF TIMES, THE LICENSE IS THREE YEARS OR FIVE YEARS, THERE ARE SOME '
             "BUSINESS DEALS WHERE THE LICENSE IS IN PERPETUITY, THAT'S A DIFFERENT TYPE OF "
             "LICENSE WE'RE TALKING ABOUT. NOW, WHAT IS MY OBLIGATION?",
      'title': "Licensing Basics You NEED To Know In Business | Shark Tank's Daymond John "
               '(Daymond John)',
      'url': 'https://www.youtube.com/watch?v=knoob7eUS6Y&t=126s',
      'video_id': 'knoob7eUS6Y'},
     {'author': 'Ayers Law TV ~ Andrew M. Ayers, Esq.',
      'channel': 'Ayers Law TV ~ Andrew M. Ayers, Esq.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:16](https://www.youtube.com/watch?v=lVFYoVaNnrs&t=196s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Non-exclusive license then the other company can contract with you as well so '
              'that you can sell your software to variety of different companies and have.',
      'timestamp': 196,
      'timestamp_label': '[00:03:16]',
      'timestamp_seconds': 196,
      'tip': 'Non-exclusive license then the other company can contract with you as well so '
             'that you can sell your software to variety of different companies and have.',
      'title': 'Exclusive vs Non Exclusive License l What’s the difference? (Ayers Law TV ~ '
               'Andrew M. Ayers, Esq.)',
      'url': 'https://www.youtube.com/watch?v=lVFYoVaNnrs&t=196s',
      'video_id': 'lVFYoVaNnrs'},
     {'author': 'xJ-Will',
      'channel': 'xJ-Will',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:00](https://www.youtube.com/watch?v=SEliWc2Tz3k&t=180s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'As well more on this later what a sync agent is is basically either an agent of '
              'that library or a third-party entity that actually has a catalog of artists.',
      'timestamp': 180,
      'timestamp_label': '[00:03:00]',
      'timestamp_seconds': 180,
      'tip': 'As well more on this later what a sync agent is is basically either an agent of '
             'that library or a third-party entity that actually has a catalog of artists.',
      'title': 'Sync Licensing: How it works for Indie Artists and Music Producers in 2025 '
               '(xJ-Will)',
      'url': 'https://www.youtube.com/watch?v=SEliWc2Tz3k&t=180s',
      'video_id': 'SEliWc2Tz3k'},
     {'author': 'Make Music Income',
      'channel': 'Make Music Income',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:57](https://www.youtube.com/watch?v=hQRVouviU-w&t=657s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And they work with television directors and producers and all the personalities '
              'they have to deal with to work with them to find the right song for the right '
              'thing. And then they have to make sure it fits the budget and they have to make '
              'sure all the rights are cleared.',
      'timestamp': 657,
      'timestamp_label': '[00:10:57]',
      'timestamp_seconds': 657,
      'tip': 'And they work with television directors and producers and all the personalities '
             'they have to deal with to work with them to find the right song for the right '
             'thing. And then they have to make sure it fits the budget and they have to make '
             'sure all the rights are cleared.',
      'title': 'How to Do Sync in 2026 | Sync Library vs. Sync Agent vs. Direct to Music '
               'Supervisor (Make Music Income)',
      'url': 'https://www.youtube.com/watch?v=hQRVouviU-w&t=657s',
      'video_id': 'hQRVouviU-w'},
     {'author': 'J.D. Houvener / Bold Patents Law Firm',
      'channel': 'J.D. Houvener / Bold Patents Law Firm',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:56](https://www.youtube.com/watch?v=-VhDIVEwvzI&t=56s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Make sure there's a performance Clause that if they decide to Shelf this and "
              "not make it you're going to be able to get out of the contract and just watch.",
      'timestamp': 56,
      'timestamp_label': '[00:00:56]',
      'timestamp_seconds': 56,
      'tip': "Make sure there's a performance Clause that if they decide to Shelf this and not "
             "make it you're going to be able to get out of the contract and just watch.",
      'title': "Exclusive vs. Non-Exclusive Patent and Trademark License Agreements: What's "
               'the Difference? (J.D. Houvener / Bold Patents Law Firm)',
      'url': 'https://www.youtube.com/watch?v=-VhDIVEwvzI&t=56s',
      'video_id': '-VhDIVEwvzI'},
     {'author': 'Jeff Schell',
      'channel': 'Jeff Schell',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:37](https://www.youtube.com/watch?v=cfPpWt8cw64&t=217s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Specifically in negotiating patent license deals you always want to keep in '
              'mind that successful negotiations not only maximize shortterm profits or.',
      'timestamp': 217,
      'timestamp_label': '[00:03:37]',
      'timestamp_seconds': 217,
      'tip': 'Specifically in negotiating patent license deals you always want to keep in mind '
             'that successful negotiations not only maximize shortterm profits or.',
      'title': 'Patent Licensing 101 - Learn What Goes Into Monetizing Your Patented Ideas '
               '(Jeff Schell)',
      'url': 'https://www.youtube.com/watch?v=cfPpWt8cw64&t=217s',
      'video_id': 'cfPpWt8cw64'},
     {'author': 'Matthew Anderson',
      'channel': 'Matthew Anderson',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:42](https://www.youtube.com/watch?v=manKMR61ho0&t=582s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Completely different kind of license keep in mind too if that ceo's company "
              "even pays thousands of dollars for that song in a commercial they still don't.",
      'timestamp': 582,
      'timestamp_label': '[00:09:42]',
      'timestamp_seconds': 582,
      'tip': "Completely different kind of license keep in mind too if that ceo's company even "
             "pays thousands of dollars for that song in a commercial they still don't.",
      'title': 'Photo Licensing 101 - The Basics Explained (Matthew Anderson)',
      'url': 'https://www.youtube.com/watch?v=manKMR61ho0&t=582s',
      'video_id': 'manKMR61ho0'},
     {'author': 'TrademarkLawyer',
      'channel': 'TrademarkLawyer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:16](https://www.youtube.com/watch?v=ASLTB9jyYII&t=196s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Example because it is extremely powerful Bethany Frankel who sold the skinny '
              'girl brand was able to license her brand but keep the intellectual property in '
              'other.',
      'timestamp': 196,
      'timestamp_label': '[00:03:16]',
      'timestamp_seconds': 196,
      'tip': 'Example because it is extremely powerful Bethany Frankel who sold the skinny '
             'girl brand was able to license her brand but keep the intellectual property in '
             'other.',
      'title': 'PASSIVE INCOME LICENSING MODEL: Beginner’s Guide from a Trademark Lawyer ✅✅✅ '
               '(TrademarkLawyer)',
      'url': 'https://www.youtube.com/watch?v=ASLTB9jyYII&t=196s',
      'video_id': 'ASLTB9jyYII'},
     {'author': 'inventRightTV',
      'channel': 'inventRightTV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:18](https://www.youtube.com/watch?v=mljygoL-peE&t=18s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Mean that means building a list of the companies that you're going to reach out "
              "to and submit your idea too right it's your It's called Your Potential license.",
      'timestamp': 18,
      'timestamp_label': '[00:00:18]',
      'timestamp_seconds': 18,
      'tip': "Mean that means building a list of the companies that you're going to reach out "
             "to and submit your idea too right it's your It's called Your Potential license.",
      'title': 'Making Your Hit List of Potential Licensees (inventRightTV)',
      'url': 'https://www.youtube.com/watch?v=mljygoL-peE&t=18s',
      'video_id': 'mljygoL-peE'},
     {'author': 'Davie Fogarty',
      'channel': 'Davie Fogarty',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:37](https://www.youtube.com/watch?v=7U8vYps8fMk&t=97s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'AUD into our first license launch still living with my parents at time I '
              'remember launching it and we did over $500,000 in just a few weeks completely.',
      'timestamp': 97,
      'timestamp_label': '[00:01:37]',
      'timestamp_seconds': 97,
      'tip': 'AUD into our first license launch still living with my parents at time I '
             'remember launching it and we did over $500,000 in just a few weeks completely.',
      'title': 'How Licensing Really Works (And How to Land One for Your Brand) (Davie '
               'Fogarty)',
      'url': 'https://www.youtube.com/watch?v=7U8vYps8fMk&t=97s',
      'video_id': '7U8vYps8fMk'},
     {'author': 'Circular Venture Lab',
      'channel': 'Circular Venture Lab',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:09](https://www.youtube.com/watch?v=ThAHgFsvejI&t=69s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I've kept this really basic. I've just typed in food as that term will have a "
              'lot of technologies associated with it. Some of these may be really relevant to '
              "your startup and you can start to explore those. Now I'll search for corn as "
              "that's more focused than food.",
      'timestamp': 69,
      'timestamp_label': '[00:01:09]',
      'timestamp_seconds': 69,
      'tip': "I've kept this really basic. I've just typed in food as that term will have a "
             'lot of technologies associated with it. Some of these may be really relevant to '
             "your startup and you can start to explore those. Now I'll search for corn as "
             "that's more focused than food.",
      'title': 'IMPACTT - Purdue Technology Transfer Office (Circular Venture Lab)',
      'url': 'https://www.youtube.com/watch?v=ThAHgFsvejI&t=69s',
      'video_id': 'ThAHgFsvejI'},
     {'author': 'Michigan Engineering',
      'channel': 'Michigan Engineering',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:37](https://www.youtube.com/watch?v=EPj0ydCGdiU&t=277s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Benefiting them the way they anticipated these are just some of the '
              'considerations you want to take into account when granting a patent license to '
              'someone else and that very generally is the concept of patent licensing.',
      'timestamp': 277,
      'timestamp_label': '[00:04:37]',
      'timestamp_seconds': 277,
      'tip': 'Benefiting them the way they anticipated these are just some of the '
             'considerations you want to take into account when granting a patent license to '
             'someone else and that very generally is the concept of patent licensing.',
      'title': 'Patent Licensing | IP series (25 of 62) (Michigan Engineering)',
      'url': 'https://www.youtube.com/watch?v=EPj0ydCGdiU&t=277s',
      'video_id': 'EPj0ydCGdiU'},
     {'author': 'inventRightTV',
      'channel': 'inventRightTV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=Se-TzTVqhfY&t=15s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Information with everybody that could benefit from it stepen key Andrew Krauss '
              'and vent Wright trying to help you license your creativity to companies and.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Information with everybody that could benefit from it stepen key Andrew Krauss '
             'and vent Wright trying to help you license your creativity to companies and.',
      'title': 'From Ideas To Income : The Truth About Earning Royalties (inventRightTV)',
      'url': 'https://www.youtube.com/watch?v=Se-TzTVqhfY&t=15s',
      'video_id': 'Se-TzTVqhfY'}],
 5: [{'author': 'Secrets of the music industry',
      'channel': 'Secrets of the music industry',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:11](https://www.youtube.com/watch?v=DfuXhSrezTU&t=311s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "It's an act of independence. It's you, the artist, taking control of your own "
              "business and your own career. And so, we'll just leave you with this question. "
              'A question for every artist out there. Your contract contains a hidden power.',
      'timestamp': 311,
      'timestamp_label': '[00:05:11]',
      'timestamp_seconds': 311,
      'tip': "It's an act of independence. It's you, the artist, taking control of your own "
             "business and your own career. And so, we'll just leave you with this question. A "
             'question for every artist out there. Your contract contains a hidden power.',
      'title': 'Your Right to AUDIT: How to Catch Your Label Stealing Your Royalties 🕵️ '
               '(Secrets of the music industry)',
      'url': 'https://www.youtube.com/watch?v=DfuXhSrezTU&t=311s',
      'video_id': 'DfuXhSrezTU'},
     {'author': 'Trenner Law Firm - Patents & Trademarks',
      'channel': 'Trenner Law Firm - Patents & Trademarks',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:33](https://www.youtube.com/watch?v=dSzZD5CnwK8&t=213s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Describe why the recipient should care. Show them how it solves a concrete '
              'business problem. Frame your patent as a way for them to gain a competitive '
              'advantage or capture a new segment of the market. And lastly, step five, '
              'structure the deal for risk and reward.',
      'timestamp': 213,
      'timestamp_label': '[00:03:33]',
      'timestamp_seconds': 213,
      'tip': 'Describe why the recipient should care. Show them how it solves a concrete '
             'business problem. Frame your patent as a way for them to gain a competitive '
             'advantage or capture a new segment of the market. And lastly, step five, '
             'structure the deal for risk and reward.',
      'title': 'From Idea to Income: How to License Your Patent for Royalties (Trenner Law '
               'Firm - Patents & Trademarks)',
      'url': 'https://www.youtube.com/watch?v=dSzZD5CnwK8&t=213s',
      'video_id': 'dSzZD5CnwK8'},
     {'author': 'IN(C) TALK | Everything Has A Business Model',
      'channel': 'IN(C) TALK | Everything Has A Business Model',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:17](https://www.youtube.com/watch?v=TYLVikvshaE&t=197s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, it's not enough to know your song is streaming. You need to know which "
              'rights you control, who administers them, and whether the registrations are in '
              'place. Now, the part that confuses a lot of people, the advance. An artist '
              'signs a deal and gets money up front.',
      'timestamp': 197,
      'timestamp_label': '[00:03:17]',
      'timestamp_seconds': 197,
      'tip': "So, it's not enough to know your song is streaming. You need to know which "
             'rights you control, who administers them, and whether the registrations are in '
             'place. Now, the part that confuses a lot of people, the advance. An artist signs '
             'a deal and gets money up front.',
      'title': 'The Music Industry Is Broken: Why Your Rights Are Worth Less Than You Think | '
               'IN(C) TALK (IN(C) TALK | Everything Has A Business Model)',
      'url': 'https://www.youtube.com/watch?v=TYLVikvshaE&t=197s',
      'video_id': 'TYLVikvshaE'},
     {'author': 'Brands On Brands Podcast',
      'channel': 'Brands On Brands Podcast',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:30:00](https://www.youtube.com/watch?v=3tCB_MAOXkA&t=1800s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s some inventory risk, some brand risk potentially if you're a brand owner and "
              'you just need to know and and uh really analyze and understand all those risks '
              "as you're entering the industry.",
      'timestamp': 1800,
      'timestamp_label': '[00:30:00]',
      'timestamp_seconds': 1800,
      'tip': "'s some inventory risk, some brand risk potentially if you're a brand owner and "
             'you just need to know and and uh really analyze and understand all those risks '
             "as you're entering the industry.",
      'title': 'Brand Licensing 101 - Stu Seltzer Interview (Brands On Brands Podcast)',
      'url': 'https://www.youtube.com/watch?v=3tCB_MAOXkA&t=1800s',
      'video_id': '3tCB_MAOXkA'},
     {'author': 'Kingacademic UK',
      'channel': 'Kingacademic UK',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:03](https://www.youtube.com/watch?v=aRUsXPICxpY&t=63s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Designs or a portfolio.  That access can shorten development and reduce '
              'technical risk. Some agreements include annual.',
      'timestamp': 63,
      'timestamp_label': '[00:01:03]',
      'timestamp_seconds': 63,
      'tip': 'Designs or a portfolio.  That access can shorten development and reduce '
             'technical risk. Some agreements include annual.',
      'title': "Arm's Licensing & Royalty Business Model Explained (Kingacademic UK)",
      'url': 'https://www.youtube.com/watch?v=aRUsXPICxpY&t=63s',
      'video_id': 'aRUsXPICxpY'},
     {'author': 'John Ferrell, Esq.',
      'channel': 'John Ferrell, Esq.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=Te8GX-Xx4mo&t=15s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Nobody should get a patent without having a business reason for doing so but '
              'when licensing your invention there are seven really dumb mistakes that come.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Nobody should get a patent without having a business reason for doing so but '
             'when licensing your invention there are seven really dumb mistakes that come.',
      'title': 'Errors You Can’t Afford to Make When Licensing Your Invention (John Ferrell, '
               'Esq.)',
      'url': 'https://www.youtube.com/watch?v=Te8GX-Xx4mo&t=15s',
      'video_id': 'Te8GX-Xx4mo'},
     {'author': 'Ask a VC',
      'channel': 'Ask a VC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:46](https://www.youtube.com/watch?v=f7jKIsIKO1c&t=466s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'t maintain control of the board indefinitely. So at some point it's likely "
              "that you're not going to control the board and that, you know, there is a risk "
              "that maybe, you know, you wouldn't be CEO going forward.",
      'timestamp': 466,
      'timestamp_label': '[00:07:46]',
      'timestamp_seconds': 466,
      'tip': "'t maintain control of the board indefinitely. So at some point it's likely that "
             "you're not going to control the board and that, you know, there is a risk that "
             "maybe, you know, you wouldn't be CEO going forward.",
      'title': 'AskAVC #12 - How to negotiate a term sheet (Ask a VC)',
      'url': 'https://www.youtube.com/watch?v=f7jKIsIKO1c&t=466s',
      'video_id': 'f7jKIsIKO1c'},
     {'author': 'USPTOvideo',
      'channel': 'USPTOvideo',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:31](https://www.youtube.com/watch?v=binARAl4AK8&t=751s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'For more information, I encourage you to visit copyright. The US Copyright '
              'Office is the federal agency responsible for registering US copyrights. US '
              'Copyright Office is a part of the Library of Congress, so a separate agency '
              'from the US Patent and Trademark Office.',
      'timestamp': 751,
      'timestamp_label': '[00:12:31]',
      'timestamp_seconds': 751,
      'tip': 'For more information, I encourage you to visit copyright. The US Copyright '
             'Office is the federal agency responsible for registering US copyrights. US '
             'Copyright Office is a part of the Library of Congress, so a separate agency from '
             'the US Patent and Trademark Office.',
      'title': 'Path to a Patent, Part I - Intellectual property basics (USPTOvideo)',
      'url': 'https://www.youtube.com/watch?v=binARAl4AK8&t=751s',
      'video_id': 'binARAl4AK8'},
     {'author': 'IPWatchdog, Inc.',
      'channel': 'IPWatchdog, Inc.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:32:39](https://www.youtube.com/watch?v=1UEOTCZ_qYA&t=1959s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'MOSFET rule, but it forces you to to talk to the business people and say, '
              '"Okay, is this design going to change?" Because if it is, then we have we have '
              "a might have a a problem. They're another safety tip.",
      'timestamp': 1959,
      'timestamp_label': '[00:32:39]',
      'timestamp_seconds': 1959,
      'tip': 'MOSFET rule, but it forces you to to talk to the business people and say, "Okay, '
             'is this design going to change?" Because if it is, then we have we have a might '
             "have a a problem. They're another safety tip.",
      'title': 'Is Your Patent Portfolio Ready to Make Money? Patent Monetization Reality '
               'Check (IPWatchdog, Inc.)',
      'url': 'https://www.youtube.com/watch?v=1UEOTCZ_qYA&t=1959s',
      'video_id': '1UEOTCZ_qYA'},
     {'author': 'UpCounsel',
      'channel': 'UpCounsel',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:23](https://www.youtube.com/watch?v=cURFfKlt_Ek&t=83s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'When negotiating royalty rates, research comparable deals using databases like '
              'KT Mine and Royalty Source. Consider the lences profitability as higher margins '
              'may justify higher rates. A hybrid model combining upfront fees with ongoing '
              'royalties can balance risk and reward.',
      'timestamp': 83,
      'timestamp_label': '[00:01:23]',
      'timestamp_seconds': 83,
      'tip': 'When negotiating royalty rates, research comparable deals using databases like '
             'KT Mine and Royalty Source. Consider the lences profitability as higher margins '
             'may justify higher rates. A hybrid model combining upfront fees with ongoing '
             'royalties can balance risk and reward.',
      'title': 'Patent Licensing  How to Set Fair Royalty Rates (UpCounsel)',
      'url': 'https://www.youtube.com/watch?v=cURFfKlt_Ek&t=83s',
      'video_id': 'cURFfKlt_Ek'},
     {'author': 'inventRightTV',
      'channel': 'inventRightTV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:17:22](https://www.youtube.com/watch?v=hM7gpPqIDoQ&t=1042s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "They know firsthand that they want someone that knows what they're doing. I "
              "know that because at Gateway we save them time, we save them money. So, that's "
              "the problem today. It's not building prototypes. I can do an AI prototype, "
              "doesn't cost me a thing.",
      'timestamp': 1042,
      'timestamp_label': '[00:17:22]',
      'timestamp_seconds': 1042,
      'tip': "They know firsthand that they want someone that knows what they're doing. I know "
             "that because at Gateway we save them time, we save them money. So, that's the "
             "problem today. It's not building prototypes. I can do an AI prototype, doesn't "
             'cost me a thing.',
      'title': 'I Licensed My Ideas — Here’s How Much I Made! (inventRightTV)',
      'url': 'https://www.youtube.com/watch?v=hM7gpPqIDoQ&t=1042s',
      'video_id': 'hM7gpPqIDoQ'},
     {'author': 'Patent Insanity',
      'channel': 'Patent Insanity',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:22](https://www.youtube.com/watch?v=Jwz-iMwUtCU&t=442s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Different way so that you can avoid both literal infringement and doctrine of '
              'equivalence analysis if you can then you have successfully designed around the '
              "patent claims and you can roll out your product without worrying that you're "
              'infringing that particular patent.',
      'timestamp': 442,
      'timestamp_label': '[00:07:22]',
      'timestamp_seconds': 442,
      'tip': 'Different way so that you can avoid both literal infringement and doctrine of '
             'equivalence analysis if you can then you have successfully designed around the '
             "patent claims and you can roll out your product without worrying that you're "
             'infringing that particular patent.',
      'title': 'Designing Around Patents - How to avoid patent infringement (Patent Insanity)',
      'url': 'https://www.youtube.com/watch?v=Jwz-iMwUtCU&t=442s',
      'video_id': 'Jwz-iMwUtCU'},
     {'author': 'Technology Licensing Office (TLO)',
      'channel': 'Technology Licensing Office (TLO)',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:20:44](https://www.youtube.com/watch?v=BtnDins-U4g&t=1244s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Repeated ear infections knowing the distress and anxiety that that causes but '
              'being able to see the actual problem in real time and discuss the possible '
              'solutions can help empower.',
      'timestamp': 1244,
      'timestamp_label': '[00:20:44]',
      'timestamp_seconds': 1244,
      'tip': 'Repeated ear infections knowing the distress and anxiety that that causes but '
             'being able to see the actual problem in real time and discuss the possible '
             'solutions can help empower.',
      'title': 'Lesley Millar-Nicholson: The Role of Technology Transfer (Technology Licensing '
               'Office (TLO))',
      'url': 'https://www.youtube.com/watch?v=BtnDins-U4g&t=1244s',
      'video_id': 'BtnDins-U4g'},
     {'author': 'CIONCA IP',
      'channel': 'CIONCA IP',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:56](https://www.youtube.com/watch?v=kRlS4inO95k&t=236s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Know um uh a bearing and this could be a gear um so you know because not all '
              'the elements of the patented claim are found in the ACC accused product this '
              'claim is not infringed by this product what about the second.',
      'timestamp': 236,
      'timestamp_label': '[00:03:56]',
      'timestamp_seconds': 236,
      'tip': 'Know um uh a bearing and this could be a gear um so you know because not all the '
             'elements of the patented claim are found in the ACC accused product this claim '
             'is not infringed by this product what about the second.',
      'title': 'Patent Infringement - Visually and Simply Explained (CIONCA IP)',
      'url': 'https://www.youtube.com/watch?v=kRlS4inO95k&t=236s',
      'video_id': 'kRlS4inO95k'},
     {'author': 'inventRightTV',
      'channel': 'inventRightTV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:23](https://www.youtube.com/watch?v=MvycxV2ib_8&t=83s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Complaints do a little homework and if they've got complaints they have a lot "
              'of lawsuits maybe you should go to the next company no problem if you reach '
              'out.',
      'timestamp': 83,
      'timestamp_label': '[00:01:23]',
      'timestamp_seconds': 83,
      'tip': "Complaints do a little homework and if they've got complaints they have a lot of "
             'lawsuits maybe you should go to the next company no problem if you reach out.',
      'title': 'Finding Companies That Embrace Open Innovation and Inventors (inventRightTV)',
      'url': 'https://www.youtube.com/watch?v=MvycxV2ib_8&t=83s',
      'video_id': 'MvycxV2ib_8'}],
 6: [{'author': 'Gait Gain',
      'channel': 'Gait Gain',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:58](https://www.youtube.com/watch?v=lvsa9U4qZJA&t=718s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Proactive outbound marketing and direct business-to-business pitching represent '
              'the fastest ways to secure lucrative licensing deals with high-value commercial '
              'brands.',
      'timestamp': 718,
      'timestamp_label': '[00:11:58]',
      'timestamp_seconds': 718,
      'tip': 'Proactive outbound marketing and direct business-to-business pitching represent '
             'the fastest ways to secure lucrative licensing deals with high-value commercial '
             'brands.',
      'title': 'Digital IP Licensing for Business Revenue in United State 2026 (Gait Gain)',
      'url': 'https://www.youtube.com/watch?v=lvsa9U4qZJA&t=718s',
      'video_id': 'lvsa9U4qZJA'},
     {'author': 'Patents and IP with Adam Diament',
      'channel': 'Patents and IP with Adam Diament',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:18](https://www.youtube.com/watch?v=k0S01jxvk6M&t=78s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So where do you find this thing? Just Google USPTO patent assignment search and '
              "it should pop up. You don't even need an account. The site is officially called "
              'the USPTO assignment search or sometimes the patent assignment query system.',
      'timestamp': 78,
      'timestamp_label': '[00:01:18]',
      'timestamp_seconds': 78,
      'tip': 'So where do you find this thing? Just Google USPTO patent assignment search and '
             "it should pop up. You don't even need an account. The site is officially called "
             'the USPTO assignment search or sometimes the patent assignment query system.',
      'title': 'How to Use the Patent Office Patent Assignment Database Like a Pro. Ep. 167 '
               '(Patents and IP with Adam Diament)',
      'url': 'https://www.youtube.com/watch?v=k0S01jxvk6M&t=78s',
      'video_id': 'k0S01jxvk6M'},
     {'author': 'Archive Trove',
      'channel': 'Archive Trove',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:55](https://www.youtube.com/watch?v=y5YpFZxHpYE&t=295s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Nothing resolves itself automatically. Every outcome traces back to what is '
              'written down. What happens to copies, derived data, and trained models is a '
              'matter of contract terms. Retention, deletion, and post-termination rights all '
              'need to be decided in advance.',
      'timestamp': 295,
      'timestamp_label': '[00:04:55]',
      'timestamp_seconds': 295,
      'tip': 'Nothing resolves itself automatically. Every outcome traces back to what is '
             'written down. What happens to copies, derived data, and trained models is a '
             'matter of contract terms. Retention, deletion, and post-termination rights all '
             'need to be decided in advance.',
      'title': 'Do You Lose Your Files When You License Data for AI Training? (Archive Trove)',
      'url': 'https://www.youtube.com/watch?v=y5YpFZxHpYE&t=295s',
      'video_id': 'y5YpFZxHpYE'},
     {'author': 'micro1',
      'channel': 'micro1',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:28](https://www.youtube.com/watch?v=Sya3mBgQK7Q&t=628s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And so, this is kind of the perfect opportunity to be able to use AI to '
              "monetize your business's data to a company like Micro 1. So, what are the major "
              'hesitations or objections that you hear when you first present this program to '
              'a business owner?',
      'timestamp': 628,
      'timestamp_label': '[00:10:28]',
      'timestamp_seconds': 628,
      'tip': 'And so, this is kind of the perfect opportunity to be able to use AI to monetize '
             "your business's data to a company like Micro 1. So, what are the major "
             'hesitations or objections that you hear when you first present this program to a '
             'business owner?',
      'title': 'What every business owner should know abut AI data licensing (micro1)',
      'url': 'https://www.youtube.com/watch?v=Sya3mBgQK7Q&t=628s',
      'video_id': 'Sya3mBgQK7Q'},
     {'author': 'ipMAGNET USPTO Patent Search',
      'channel': 'ipMAGNET USPTO Patent Search',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:04](https://www.youtube.com/watch?v=K33V82uvPfc&t=304s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'On your search results here you can find if a patent is issued for these '
              'publications in your list with just a single click the detailed tutorial is '
              'available from the patent status screen.',
      'timestamp': 304,
      'timestamp_label': '[00:05:04]',
      'timestamp_seconds': 304,
      'tip': 'On your search results here you can find if a patent is issued for these '
             'publications in your list with just a single click the detailed tutorial is '
             'available from the patent status screen.',
      'title': 'How to Search and Download USPTO Patents (ipMAGNET USPTO Patent Search)',
      'url': 'https://www.youtube.com/watch?v=K33V82uvPfc&t=304s',
      'video_id': 'K33V82uvPfc'},
     {'author': 'Intellectual Property Ontario',
      'channel': 'Intellectual Property Ontario',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:26](https://www.youtube.com/watch?v=2L5qDLM_EkY&t=26s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Usbto is exclusively for searching us patents and has recently revamped its '
              'search database you can access it by clicking on the link provided in the '
              'description below once you are on the landing page you will find two search '
              'options basic search and advanced search.',
      'timestamp': 26,
      'timestamp_label': '[00:00:26]',
      'timestamp_seconds': 26,
      'tip': 'Usbto is exclusively for searching us patents and has recently revamped its '
             'search database you can access it by clicking on the link provided in the '
             'description below once you are on the landing page you will find two search '
             'options basic search and advanced search.',
      'title': 'How Can I Conduct Effective Patent Searches on the USPTO Database? '
               '(Intellectual Property Ontario)',
      'url': 'https://www.youtube.com/watch?v=2L5qDLM_EkY&t=26s',
      'video_id': '2L5qDLM_EkY'},
     {'author': 'Boardgame Publisher',
      'channel': 'Boardgame Publisher',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:49](https://www.youtube.com/watch?v=SOV77fL52Dw&t=349s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s only the company that you are selling it's not the the catalog of games that "
              "you have. 's a good thing to have that kind of event planned into your contract "
              "from the get go so that if it happens you don't find yourself in a delicate "
              'situation.',
      'timestamp': 349,
      'timestamp_label': '[00:05:49]',
      'timestamp_seconds': 349,
      'tip': "'s only the company that you are selling it's not the the catalog of games that "
             "you have. 's a good thing to have that kind of event planned into your contract "
             "from the get go so that if it happens you don't find yourself in a delicate "
             'situation.',
      'title': 'Boardgame licensing rights duration, reversion and sublicensing (Boardgame '
               'Publisher)',
      'url': 'https://www.youtube.com/watch?v=SOV77fL52Dw&t=349s',
      'video_id': 'SOV77fL52Dw'},
     {'author': 'Patent Attorney Worldwide',
      'channel': 'Patent Attorney Worldwide',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:11](https://www.youtube.com/watch?v=D-Am1gpuzaw&t=251s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re being accused of infringing is actually invalid and shouldn't have been "
              "granted in the first place. Your legal team goes on a hunt. They conduct what's "
              'called a validity search to find something called prior art.',
      'timestamp': 251,
      'timestamp_label': '[00:04:11]',
      'timestamp_seconds': 251,
      'tip': "'re being accused of infringing is actually invalid and shouldn't have been "
             "granted in the first place. Your legal team goes on a hunt. They conduct what's "
             'called a validity search to find something called prior art.',
      'title': 'Patent Infringement Explained: Types, Lawsuits & Legal Remedies (Complete '
               'Guide) (Patent Attorney Worldwide)',
      'url': 'https://www.youtube.com/watch?v=D-Am1gpuzaw&t=251s',
      'video_id': 'D-Am1gpuzaw'},
     {'author': 'USPTOvideo',
      'channel': 'USPTOvideo',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:44:40](https://www.youtube.com/watch?v=np8RKbVMSLg&t=2680s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So to do so, you'll first take note of the document that you want to view in "
              "this case, D947805. And we will open up and go back again to the USPTO. 'll "
              'navigate here to find fast. And The Patent Center is listed under Patent Public '
              'Search right here.',
      'timestamp': 2680,
      'timestamp_label': '[00:44:40]',
      'timestamp_seconds': 2680,
      'tip': "So to do so, you'll first take note of the document that you want to view in "
             "this case, D947805. And we will open up and go back again to the USPTO. 'll "
             'navigate here to find fast. And The Patent Center is listed under Patent Public '
             'Search right here.',
      'title': 'Using Patent Public Search Advanced to Search Designs (USPTOvideo)',
      'url': 'https://www.youtube.com/watch?v=np8RKbVMSLg&t=2680s',
      'video_id': 'np8RKbVMSLg'},
     {'author': 'The Linux Foundation',
      'channel': 'The Linux Foundation',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:46](https://www.youtube.com/watch?v=bii4_gwgoBY&t=886s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The first thing I want to start starting guys off slow first scary part is '
              'about 107 of those data sets use custom licenses which means that identifying '
              "the rights and obligations properly would need legal expertise it's not like we "
              'already know.',
      'timestamp': 886,
      'timestamp_label': '[00:14:46]',
      'timestamp_seconds': 886,
      'tip': 'The first thing I want to start starting guys off slow first scary part is about '
             '107 of those data sets use custom licenses which means that identifying the '
             "rights and obligations properly would need legal expertise it's not like we "
             'already know.',
      'title': 'OpenDataology - A Call to Arms for Fixing the Dataset Licensing Landscape - '
               'Gopi Krishnan Rajbahadur (The Linux Foundation)',
      'url': 'https://www.youtube.com/watch?v=bii4_gwgoBY&t=886s',
      'video_id': 'bii4_gwgoBY'},
     {'author': 'Edel Patents',
      'channel': 'Edel Patents',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=SDXhhmDKGJo&t=15s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I'm going to show you a basic search structure that you can use over and over "
              'again as a template for your searches first.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "I'm going to show you a basic search structure that you can use over and over "
             'again as a template for your searches first.',
      'title': 'Beginner Tips for USPTO Search - [Operators & Fields] (Edel Patents)',
      'url': 'https://www.youtube.com/watch?v=SDXhhmDKGJo&t=15s',
      'video_id': 'SDXhhmDKGJo'},
     {'author': 'inventRightTV',
      'channel': 'inventRightTV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:31](https://www.youtube.com/watch?v=aFZpyTUvtlY&t=91s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, that's the first thing you need to do. Second thing you need to do, I would "
              "I'd make a list of all the companies you want to reach out to and I would "
              'connect with them if you can, but also I would comment on their posts.',
      'timestamp': 91,
      'timestamp_label': '[00:01:31]',
      'timestamp_seconds': 91,
      'tip': "So, that's the first thing you need to do. Second thing you need to do, I would "
             "I'd make a list of all the companies you want to reach out to and I would "
             'connect with them if you can, but also I would comment on their posts.',
      'title': 'How to Pitch Your Product to Companies For a Licensing Deal (inventRightTV)',
      'url': 'https://www.youtube.com/watch?v=aFZpyTUvtlY&t=91s',
      'video_id': 'aFZpyTUvtlY'},
     {'author': 'Alliance for Patient Access',
      'channel': 'Alliance for Patient Access',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:47](https://www.youtube.com/watch?v=5RtieTL1OqM&t=47s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The patent expires quick cheap drugs sound appealing but there are real '
              'consequences to compulsory licensing first medicine copies made.',
      'timestamp': 47,
      'timestamp_label': '[00:00:47]',
      'timestamp_seconds': 47,
      'tip': 'The patent expires quick cheap drugs sound appealing but there are real '
             'consequences to compulsory licensing first medicine copies made.',
      'title': 'Understanding Compulsory Licensing (Alliance for Patient Access)',
      'url': 'https://www.youtube.com/watch?v=5RtieTL1OqM&t=47s',
      'video_id': '5RtieTL1OqM'},
     {'author': 'Visme',
      'channel': 'Visme',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:50](https://www.youtube.com/watch?v=ShCyD9TYhLY&t=410s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Appreciate your support and want to keep helping people just like you for years '
              'to come check out our channel to see what other questions that we can answer '
              "for you until then I'm Mike ploger with vimme helping you make information.",
      'timestamp': 410,
      'timestamp_label': '[00:06:50]',
      'timestamp_seconds': 410,
      'tip': 'Appreciate your support and want to keep helping people just like you for years '
             'to come check out our channel to see what other questions that we can answer for '
             "you until then I'm Mike ploger with vimme helping you make information.",
      'title': 'How to LEGALLY Use a Copyrighted Photo (Visme)',
      'url': 'https://www.youtube.com/watch?v=ShCyD9TYhLY&t=410s',
      'video_id': 'ShCyD9TYhLY'},
     {'author': 'inventRightTV',
      'channel': 'inventRightTV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:15:35](https://www.youtube.com/watch?v=biVTpLl2T5U&t=935s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Me ah stephen key here and be ready for the next video because I'm going to "
              "talk about licensing agreements there's a great idea in each of us but it's "
              'truly magical to see it come to life.',
      'timestamp': 935,
      'timestamp_label': '[00:15:35]',
      'timestamp_seconds': 935,
      'tip': "Me ah stephen key here and be ready for the next video because I'm going to talk "
             "about licensing agreements there's a great idea in each of us but it's truly "
             'magical to see it come to life.',
      'title': 'How to Land the Licensing Deal of Your Dreams (inventRightTV)',
      'url': 'https://www.youtube.com/watch?v=biVTpLl2T5U&t=935s',
      'video_id': 'biVTpLl2T5U'}],
 7: [{'author': 'Cashix',
      'channel': 'Cashix',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:40](https://www.youtube.com/watch?v=2dvDoXcllAw&t=220s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Under the Lanham Act, a trademark acts as a guarantee of consistent quality. If '
              'a brand owner licenses their name to a third-party, but fails to exercise '
              'strict active quality control over the resulting products, they commit what is '
              'known as naked licensing.',
      'timestamp': 220,
      'timestamp_label': '[00:03:40]',
      'timestamp_seconds': 220,
      'tip': 'Under the Lanham Act, a trademark acts as a guarantee of consistent quality. If '
             'a brand owner licenses their name to a third-party, but fails to exercise strict '
             'active quality control over the resulting products, they commit what is known as '
             'naked licensing.',
      'title': 'The Hidden Business of Licensing: How Brands Make Billions Without Making '
               'Products (Cashix)',
      'url': 'https://www.youtube.com/watch?v=2dvDoXcllAw&t=220s',
      'video_id': '2dvDoXcllAw'},
     {'author': 'Flowhaven',
      'channel': 'Flowhaven',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:09](https://www.youtube.com/watch?v=M69XC4rxxQc&t=69s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'When those five steps live in one system, nobody has to chase anybody. '
              'Tidewhale, an ocean lifestyle brand, is signing Kelpline Apparel to make '
              "hoodies for the Nordic market, sold wholesale and online. We'll follow that one "
              'deal through all five steps.',
      'timestamp': 69,
      'timestamp_label': '[00:01:09]',
      'timestamp_seconds': 69,
      'tip': 'When those five steps live in one system, nobody has to chase anybody. '
             'Tidewhale, an ocean lifestyle brand, is signing Kelpline Apparel to make hoodies '
             "for the Nordic market, sold wholesale and online. We'll follow that one deal "
             'through all five steps.',
      'title': 'How licensing teams run agreements, approvals and royalties in one place '
               '(Flowhaven)',
      'url': 'https://www.youtube.com/watch?v=M69XC4rxxQc&t=69s',
      'video_id': 'M69XC4rxxQc'},
     {'author': 'Mayer Brown',
      'channel': 'Mayer Brown',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:52](https://www.youtube.com/watch?v=yRNAVrfCNIE&t=592s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "In the process it's important to be organized and intentional so in the end you "
              "have a deal that works for the business and that's legally sound.",
      'timestamp': 592,
      'timestamp_label': '[00:09:52]',
      'timestamp_seconds': 592,
      'tip': "In the process it's important to be organized and intentional so in the end you "
             "have a deal that works for the business and that's legally sound.",
      'title': 'Navigating the Brand Licensing Life Cycle (Mayer Brown)',
      'url': 'https://www.youtube.com/watch?v=yRNAVrfCNIE&t=592s',
      'video_id': 'yRNAVrfCNIE'},
     {'author': 'Jason Varner',
      'channel': 'Jason Varner',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:19](https://www.youtube.com/watch?v=nKuxu_x-s6o&t=319s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'That will kind of get you prepared. I also have a business data checklist where '
              "you can select your category of business and it'll give you all the different "
              'things that uh might be valuable that can help you in building out your data '
              'manifest.',
      'timestamp': 319,
      'timestamp_label': '[00:05:19]',
      'timestamp_seconds': 319,
      'tip': 'That will kind of get you prepared. I also have a business data checklist where '
             "you can select your category of business and it'll give you all the different "
             'things that uh might be valuable that can help you in building out your data '
             'manifest.',
      'title': 'Explaining the Data Licensing Opportunity for Your Company (Jason Varner)',
      'url': 'https://www.youtube.com/watch?v=nKuxu_x-s6o&t=319s',
      'video_id': 'nKuxu_x-s6o'},
     {'author': 'Brand Licensing by Informa',
      'channel': 'Brand Licensing by Informa',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=TwdLXgIhXJA&t=15s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Licensing may be right for you what is licensing licensing is the process of '
              'leasing a legally protected entity such as a character name logo or.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Licensing may be right for you what is licensing licensing is the process of '
             'leasing a legally protected entity such as a character name logo or.',
      'title': 'What is Brand Licensing? (Brand Licensing by Informa)',
      'url': 'https://www.youtube.com/watch?v=TwdLXgIhXJA&t=15s',
      'video_id': 'TwdLXgIhXJA'},
     {'author': 'CPDPConferences',
      'channel': 'CPDPConferences',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:17:05](https://www.youtube.com/watch?v=k3ktLc3BIZc&t=1025s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Since there is no uh, an individual um, um, no individual aspect of any of the '
              'works in the database is preserved by the system because you extract standards '
              "and concept out of it. Then you don't have uh the individual component of a "
              'protected work.',
      'timestamp': 1025,
      'timestamp_label': '[00:17:05]',
      'timestamp_seconds': 1025,
      'tip': 'Since there is no uh, an individual um, um, no individual aspect of any of the '
             'works in the database is preserved by the system because you extract standards '
             "and concept out of it. Then you don't have uh the individual component of a "
             'protected work.',
      'title': 'Copyright Law and Generative AI Training CPDP 2026 (CPDPConferences)',
      'url': 'https://www.youtube.com/watch?v=k3ktLc3BIZc&t=1025s',
      'video_id': 'k3ktLc3BIZc'},
     {'author': 'Columbia TechVentures',
      'channel': 'Columbia TechVentures',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:57:39](https://www.youtube.com/watch?v=ZzczaFujs3A&t=3459s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Um they're just wondering about the whole process I have a general sense of the "
              'process but just how your office would work with like a pharmacy and like like '
              'the stage before where the contract has now been established sure.',
      'timestamp': 3459,
      'timestamp_label': '[00:57:39]',
      'timestamp_seconds': 3459,
      'tip': "Um they're just wondering about the whole process I have a general sense of the "
             'process but just how your office would work with like a pharmacy and like like '
             'the stage before where the contract has now been established sure.',
      'title': 'Patenting & Licensing of Early-Stage University Technology (Columbia '
               'TechVentures)',
      'url': 'https://www.youtube.com/watch?v=ZzczaFujs3A&t=3459s',
      'video_id': 'ZzczaFujs3A'},
     {'author': 'Edel Patents',
      'channel': 'Edel Patents',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=oOln2IDvhqE&t=15s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'First patent application number searching is not hard but there are more steps '
              'and problems with the process than you might.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'First patent application number searching is not hard but there are more steps '
             'and problems with the process than you might.',
      'title': 'Patent Application Number Search - Avoid the traps (Edel Patents)',
      'url': 'https://www.youtube.com/watch?v=oOln2IDvhqE&t=15s',
      'video_id': 'oOln2IDvhqE'},
     {'author': 'Patents Demystified',
      'channel': 'Patents Demystified',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:51](https://www.youtube.com/watch?v=9hTMXJtONtM&t=171s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Non-provisional patent application okay so to step back for a second so the way '
              'you start the patent one way you start the patent process is by filing a.',
      'timestamp': 171,
      'timestamp_label': '[00:02:51]',
      'timestamp_seconds': 171,
      'tip': 'Non-provisional patent application okay so to step back for a second so the way '
             'you start the patent one way you start the patent process is by filing a.',
      'title': 'Mastering Patentability And Infringement Concepts Made EASY (Patents '
               'Demystified)',
      'url': 'https://www.youtube.com/watch?v=9hTMXJtONtM&t=171s',
      'video_id': '9hTMXJtONtM'},
     {'author': 'inventRightTV',
      'channel': 'inventRightTV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:43](https://www.youtube.com/watch?v=hbfKyomYp6U&t=163s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'It took a while like I said but I did figure it out and along with my partner '
              'Andrew Kraus we created a tendon step system we call it invent right that '
              "teaches you how to license your ideas and it's fairly straightforward and now.",
      'timestamp': 163,
      'timestamp_label': '[00:02:43]',
      'timestamp_seconds': 163,
      'tip': 'It took a while like I said but I did figure it out and along with my partner '
             'Andrew Kraus we created a tendon step system we call it invent right that '
             "teaches you how to license your ideas and it's fairly straightforward and now.",
      'title': 'The Licensing Lifestyle with Stephen Key (inventRightTV)',
      'url': 'https://www.youtube.com/watch?v=hbfKyomYp6U&t=163s',
      'video_id': 'hbfKyomYp6U'},
     {'author': 'Commercialisation Talks',
      'channel': 'Commercialisation Talks',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=2_OclNjs2Hg&t=21s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Um tell you you're one of the rare ones in the world that you do "
              'commercialization and technology transfer [clears throat] and at the same time '
              'you did your PhD in technology transfer.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': "Um tell you you're one of the rare ones in the world that you do "
             'commercialization and technology transfer [clears throat] and at the same time '
             'you did your PhD in technology transfer.',
      'title': 'Why do so many university patents remain on the shelf? (Commercialisation '
               'Talks)',
      'url': 'https://www.youtube.com/watch?v=2_OclNjs2Hg&t=21s',
      'video_id': '2_OclNjs2Hg'},
     {'author': '3HTi',
      'channel': '3HTi',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:17:40](https://www.youtube.com/watch?v=UPnBwRHoelM&t=1060s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Geometry from any other system and ultimately go and change it and always the '
              'pain in the behind was with parametric modeling was you got to the.',
      'timestamp': 1060,
      'timestamp_label': '[00:17:40]',
      'timestamp_seconds': 1060,
      'tip': 'Geometry from any other system and ultimately go and change it and always the '
             'pain in the behind was with parametric modeling was you got to the.',
      'title': "What's in a Creo License (3HTi)",
      'url': 'https://www.youtube.com/watch?v=UPnBwRHoelM&t=1060s',
      'video_id': 'UPnBwRHoelM'},
     {'author': 'UpCounsel',
      'channel': 'UpCounsel',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:46](https://www.youtube.com/watch?v=wiI7fBL42Vg&t=346s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'By understanding the options available and taking appropriate steps to protect '
              'and market your invention, you can maximize the potential return on your '
              'innovative ideas.',
      'timestamp': 346,
      'timestamp_label': '[00:05:46]',
      'timestamp_seconds': 346,
      'tip': 'By understanding the options available and taking appropriate steps to protect '
             'and market your invention, you can maximize the potential return on your '
             'innovative ideas.',
      'title': 'How to Profit from Your Patent  Selling, Licensing, and Protecting Your '
               'Invention (UpCounsel)',
      'url': 'https://www.youtube.com/watch?v=wiI7fBL42Vg&t=346s',
      'video_id': 'wiI7fBL42Vg'},
     {'author': 'Patents Demystified',
      'channel': 'Patents Demystified',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:20](https://www.youtube.com/watch?v=GOd61uYqq-8&t=200s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You want to see more clips from this podcast you can see the full playlist '
              "right here and we've got the full podcast right here and please like the video "
              'on your way out so we can it seen by more people thanks.',
      'timestamp': 200,
      'timestamp_label': '[00:03:20]',
      'timestamp_seconds': 200,
      'tip': 'You want to see more clips from this podcast you can see the full playlist right '
             "here and we've got the full podcast right here and please like the video on your "
             'way out so we can it seen by more people thanks.',
      'title': 'How To Practice Patent Law WITHOUT Being An Attorney [Insider Secrets] '
               '(Patents Demystified)',
      'url': 'https://www.youtube.com/watch?v=GOd61uYqq-8&t=200s',
      'video_id': 'GOd61uYqq-8'},
     {'author': 'inventRightTV',
      'channel': 'inventRightTV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:57](https://www.youtube.com/watch?v=zdIFauqdSt8&t=417s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You want to be pleasant you want to you have a good time you want them to like '
              "you you don't want them to run by doing some things that maybe you shouldn't be "
              "doing I'll talk about those things too so let's go to next.",
      'timestamp': 417,
      'timestamp_label': '[00:06:57]',
      'timestamp_seconds': 417,
      'tip': 'You want to be pleasant you want to you have a good time you want them to like '
             "you you don't want them to run by doing some things that maybe you shouldn't be "
             "doing I'll talk about those things too so let's go to next.",
      'title': 'Pitching an Idea? Learn the RIGHT Way to Land a Licensing Deal! '
               '(inventRightTV)',
      'url': 'https://www.youtube.com/watch?v=zdIFauqdSt8&t=417s',
      'video_id': 'zdIFauqdSt8'}],
 8: [{'author': '514Blog',
      'channel': '514Blog',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:00](https://www.youtube.com/watch?v=ApLNF2BQAt8&t=240s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'CAD to a working interactive 3D parts catalog without building the entire '
              'system internally, Ventana is our top choice for 2026. Of course, the right '
              'platform will depend on your existing systems, your product complexity, and how '
              'you plan to use your 3D content.',
      'timestamp': 240,
      'timestamp_label': '[00:04:00]',
      'timestamp_seconds': 240,
      'tip': 'CAD to a working interactive 3D parts catalog without building the entire system '
             'internally, Ventana is our top choice for 2026. Of course, the right platform '
             'will depend on your existing systems, your product complexity, and how you plan '
             'to use your 3D content.',
      'title': 'Best 3D Parts Catalog Software in 2026 (5 Tools Compared) (514Blog)',
      'url': 'https://www.youtube.com/watch?v=ApLNF2BQAt8&t=240s',
      'video_id': 'ApLNF2BQAt8'},
     {'author': 'UpCounsel',
      'channel': 'UpCounsel',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:48](https://www.youtube.com/watch?v=QaABLYw6maY&t=108s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s laws will govern the agreement, addressing potential tax implications, and "
              'ensuring compliance with local regulations. Licensing agreements can be '
              'powerful tools for generating revenue, expanding brand reach, and accessing new '
              'markets.',
      'timestamp': 108,
      'timestamp_label': '[00:01:48]',
      'timestamp_seconds': 108,
      'tip': "'s laws will govern the agreement, addressing potential tax implications, and "
             'ensuring compliance with local regulations. Licensing agreements can be powerful '
             'tools for generating revenue, expanding brand reach, and accessing new markets.',
      'title': 'Licensing Agreements  Key Elements and Business Benefits (UpCounsel)',
      'url': 'https://www.youtube.com/watch?v=QaABLYw6maY&t=108s',
      'video_id': 'QaABLYw6maY'},
     {'author': 'Torys LLP',
      'channel': 'Torys LLP',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:32](https://www.youtube.com/watch?v=ijF0IyvjXXg&t=332s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Okay, well, this sounds much more promising. So, if a trademark holder sees '
              'this occurring, can they assert infringement against the platform or do they '
              'still to search for the true seller?',
      'timestamp': 332,
      'timestamp_label': '[00:05:32]',
      'timestamp_seconds': 332,
      'tip': 'Okay, well, this sounds much more promising. So, if a trademark holder sees this '
             'occurring, can they assert infringement against the platform or do they still to '
             'search for the true seller?',
      'title': 'Ask an IP litigator: #5 - How do I stop an unauthorized seller? (Torys LLP)',
      'url': 'https://www.youtube.com/watch?v=ijF0IyvjXXg&t=332s',
      'video_id': 'ijF0IyvjXXg'},
     {'author': 'MillionPodcasts',
      'channel': 'MillionPodcasts',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:23](https://www.youtube.com/watch?v=s8iH8wFk-Hc&t=503s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Keeping track of music rights across your podcast catalog doesn't have to be "
              'complicated. A few simple tools can help you avoid missed clearances and '
              'expired licenses. Start with a music rights tracking spreadsheet.',
      'timestamp': 503,
      'timestamp_label': '[00:08:23]',
      'timestamp_seconds': 503,
      'tip': "Keeping track of music rights across your podcast catalog doesn't have to be "
             'complicated. A few simple tools can help you avoid missed clearances and expired '
             'licenses. Start with a music rights tracking spreadsheet.',
      'title': 'The Complete Guide to Podcast Music Rights & Licensing 2026 (MillionPodcasts)',
      'url': 'https://www.youtube.com/watch?v=s8iH8wFk-Hc&t=503s',
      'video_id': 's8iH8wFk-Hc'},
     {'author': 'DesignLab UW-Madison',
      'channel': 'DesignLab UW-Madison',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:15](https://www.youtube.com/watch?v=mGWJAAFhtRk&t=75s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'This is because the creator has waived all rights to their creative work. This '
              'means you can copy, modify, distribute, and perform the work even for '
              "commercial purposes all without asking the creator's permission. One useful "
              'image search engine is the CCSearch.',
      'timestamp': 75,
      'timestamp_label': '[00:01:15]',
      'timestamp_seconds': 75,
      'tip': 'This is because the creator has waived all rights to their creative work. This '
             'means you can copy, modify, distribute, and perform the work even for commercial '
             "purposes all without asking the creator's permission. One useful image search "
             'engine is the CCSearch.',
      'title': 'Copyright and Fair Use for Images, Videos, and Audio - Basics (DesignLab '
               'UW-Madison)',
      'url': 'https://www.youtube.com/watch?v=mGWJAAFhtRk&t=75s',
      'video_id': 'mGWJAAFhtRk'},
     {'author': 'Lynn D. Jung',
      'channel': 'Lynn D. Jung',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:49](https://www.youtube.com/watch?v=cEP_oNaMQcw&t=289s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, when you actually finalize and sign your contract, you're going to get your "
              "first chunk of change. So, let's say you have a $100,000 advance, you'll get "
              '25K upon signing. And then your next chunk of change is going to come when you '
              'deliver your book and it is accepted.',
      'timestamp': 289,
      'timestamp_label': '[00:04:49]',
      'timestamp_seconds': 289,
      'tip': "So, when you actually finalize and sign your contract, you're going to get your "
             "first chunk of change. So, let's say you have a $100,000 advance, you'll get 25K "
             'upon signing. And then your next chunk of change is going to come when you '
             'deliver your book and it is accepted.',
      'title': '💸 a guide to author finances // advances, royalties, taxes, & what worked for '
               'me (Lynn D. Jung)',
      'url': 'https://www.youtube.com/watch?v=cEP_oNaMQcw&t=289s',
      'video_id': 'cEP_oNaMQcw'},
     {'author': 'Ideas on Fire',
      'channel': 'Ideas on Fire',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:33](https://www.youtube.com/watch?v=QHV5OSGnAMg&t=393s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Yeah, I could just add on to to what I said earlier. I did want to clarify that '
              'when I use the language of advanced contract, all that means is that the '
              'contract is being offered in advance of a final approved manuscript, peer '
              'review, all of that kind of stuff.',
      'timestamp': 393,
      'timestamp_label': '[00:06:33]',
      'timestamp_seconds': 393,
      'tip': 'Yeah, I could just add on to to what I said earlier. I did want to clarify that '
             'when I use the language of advanced contract, all that means is that the '
             'contract is being offered in advance of a final approved manuscript, peer '
             'review, all of that kind of stuff.',
      'title': 'Understanding Contracts, Royalties, and Rights - Academic Publishing Series '
               '(Ideas on Fire)',
      'url': 'https://www.youtube.com/watch?v=QHV5OSGnAMg&t=393s',
      'video_id': 'QHV5OSGnAMg'},
     {'author': 'freeCodeCamp Concepts',
      'channel': 'freeCodeCamp Concepts',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:35](https://www.youtube.com/watch?v=grui-CD6Uck&t=95s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Domain most search engines will allow you to filter image results by a license '
              'there are also sites like pixabay and unsplash which offer free to ous images '
              'always be mindful of the copyright and Licensing when you use an image in your '
              'website.',
      'timestamp': 95,
      'timestamp_label': '[00:01:35]',
      'timestamp_seconds': 95,
      'tip': 'Domain most search engines will allow you to filter image results by a license '
             'there are also sites like pixabay and unsplash which offer free to ous images '
             'always be mindful of the copyright and Licensing when you use an image in your '
             'website.',
      'title': 'What are the different types of image licenses and how do they work? '
               '(freeCodeCamp Concepts)',
      'url': 'https://www.youtube.com/watch?v=grui-CD6Uck&t=95s',
      'video_id': 'grui-CD6Uck'},
     {'author': 'Mayer Brown',
      'channel': 'Mayer Brown',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:47](https://www.youtube.com/watch?v=5gxaM62YYFk&t=707s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Is constantly evolving and changing the training is continuous there may be '
              'continuous updates and tweaks going on to the AI tool the production data is.',
      'timestamp': 707,
      'timestamp_label': '[00:11:47]',
      'timestamp_seconds': 707,
      'tip': 'Is constantly evolving and changing the training is continuous there may be '
             'continuous updates and tweaks going on to the AI tool the production data is.',
      'title': "Mayer Brown's Tech Talks: Smart Licensing of AI (Mayer Brown)",
      'url': 'https://www.youtube.com/watch?v=5gxaM62YYFk&t=707s',
      'video_id': '5gxaM62YYFk'},
     {'author': 'universityofontario',
      'channel': 'universityofontario',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:19](https://www.youtube.com/watch?v=O2Cp8235kvg&t=199s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So it really depends on on a lot of factors and you have to look at you know '
              "really what you're trying to do and probably get some external advice as to the "
              'right ways to protect intellectual property and software products.',
      'timestamp': 199,
      'timestamp_label': '[00:03:19]',
      'timestamp_seconds': 199,
      'tip': 'So it really depends on on a lot of factors and you have to look at you know '
             "really what you're trying to do and probably get some external advice as to the "
             'right ways to protect intellectual property and software products.',
      'title': 'UOIT Office of Technology Transfer and Commercialization - How do I protect my '
               'Copyright? (universityofontario)',
      'url': 'https://www.youtube.com/watch?v=O2Cp8235kvg&t=199s',
      'video_id': 'O2Cp8235kvg'},
     {'author': 'Erinnae Baker',
      'channel': 'Erinnae Baker',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:17](https://www.youtube.com/watch?v=Awpsichbouw&t=257s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'It looks and operates just the same as the patent search so you should have no '
              "problem with that and that's how to use the united states patent and trademark "
              "office's patent search.",
      'timestamp': 257,
      'timestamp_label': '[00:04:17]',
      'timestamp_seconds': 257,
      'tip': 'It looks and operates just the same as the patent search so you should have no '
             "problem with that and that's how to use the united states patent and trademark "
             "office's patent search.",
      'title': 'USPTO Patent Database Tutorial (Erinnae Baker)',
      'url': 'https://www.youtube.com/watch?v=Awpsichbouw&t=257s',
      'video_id': 'Awpsichbouw'},
     {'author': 'IP Author',
      'channel': 'IP Author',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:19](https://www.youtube.com/watch?v=IJ_WZiM4dKk&t=799s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Now, you're not trying to draft a patent application or conduct a search, but "
              "you're saying, you know what, I want to build a patent application or I want to "
              'build up my portfolio in a particular topic area.',
      'timestamp': 799,
      'timestamp_label': '[00:13:19]',
      'timestamp_seconds': 799,
      'tip': "Now, you're not trying to draft a patent application or conduct a search, but "
             "you're saying, you know what, I want to build a patent application or I want to "
             'build up my portfolio in a particular topic area.',
      'title': 'AI Agents Are Transforming Patent Practice: From Patent Tools to AI Agents (IP '
               'Author)',
      'url': 'https://www.youtube.com/watch?v=IJ_WZiM4dKk&t=799s',
      'video_id': 'IJ_WZiM4dKk'},
     {'author': 'The Patent Professor',
      'channel': 'The Patent Professor',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:21](https://www.youtube.com/watch?v=bO09tLv7ysM&t=201s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "This because you didn't do this I'm like okay that's fine I'm walking away or "
              "we're negotiating so it's not it's like yeah those are those are good "
              'ammunition to have but your true the true power is the decision of you what '
              'what you want to do with your idea.',
      'timestamp': 201,
      'timestamp_label': '[00:03:21]',
      'timestamp_seconds': 201,
      'tip': "This because you didn't do this I'm like okay that's fine I'm walking away or "
             "we're negotiating so it's not it's like yeah those are those are good ammunition "
             'to have but your true the true power is the decision of you what what you want '
             'to do with your idea.',
      'title': 'Licensing Your Product Idea: How to Negotiate Your Royalty Percentage with Sef '
               'Chang (The Patent Professor)',
      'url': 'https://www.youtube.com/watch?v=bO09tLv7ysM&t=201s',
      'video_id': 'bO09tLv7ysM'},
     {'author': 'inventRightTV',
      'channel': 'inventRightTV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:16](https://www.youtube.com/watch?v=LWNWc2dynPI&t=976s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "We love our ideas, we're enthusiastic, we want to show it to you. They're not "
              "really they don't really understand the business here. So, you're just "
              "overloading these companies. If you can get to them, and they're like, you're "
              "driving us crazy. So, they're not responding.",
      'timestamp': 976,
      'timestamp_label': '[00:16:16]',
      'timestamp_seconds': 976,
      'tip': "We love our ideas, we're enthusiastic, we want to show it to you. They're not "
             "really they don't really understand the business here. So, you're just "
             "overloading these companies. If you can get to them, and they're like, you're "
             "driving us crazy. So, they're not responding.",
      'title': 'How I License an Invention From Start to Finish (inventRightTV)',
      'url': 'https://www.youtube.com/watch?v=LWNWc2dynPI&t=976s',
      'video_id': 'LWNWc2dynPI'},
     {'author': 'inventRightTV',
      'channel': 'inventRightTV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:55:03](https://www.youtube.com/watch?v=1w_iTE7ZNso&t=3303s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "This great idea that's not going to work and I the other day uh a company flat "
              "out told us one group that we're working with we're not ever going to sign in n "
              "da I don't know what half the company's.",
      'timestamp': 3303,
      'timestamp_label': '[00:55:03]',
      'timestamp_seconds': 3303,
      'tip': "This great idea that's not going to work and I the other day uh a company flat "
             "out told us one group that we're working with we're not ever going to sign in n "
             "da I don't know what half the company's.",
      'title': '12 Tips for Successful Product Licensing! (inventRightTV)',
      'url': 'https://www.youtube.com/watch?v=1w_iTE7ZNso&t=3303s',
      'video_id': '1w_iTE7ZNso'}],
 9: [{'author': 'J.D. Houvener / Bold Patents Law Firm',
      'channel': 'J.D. Houvener / Bold Patents Law Firm',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:14](https://www.youtube.com/watch?v=ZbJhX8I0koA&t=194s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Grant Clause I don't take a quick break here then yeah a license agreement is "
              'not just as simple as literally signing the patent over this is a legal '
              "contract that you're creating with the other party.",
      'timestamp': 194,
      'timestamp_label': '[00:03:14]',
      'timestamp_seconds': 194,
      'tip': "Grant Clause I don't take a quick break here then yeah a license agreement is "
             'not just as simple as literally signing the patent over this is a legal contract '
             "that you're creating with the other party.",
      'title': 'How to License a Patent (J.D. Houvener / Bold Patents Law Firm)',
      'url': 'https://www.youtube.com/watch?v=ZbJhX8I0koA&t=194s',
      'video_id': 'ZbJhX8I0koA'},
     {'author': 'Patent Question',
      'channel': 'Patent Question',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:13](https://www.youtube.com/watch?v=E7nUaZBoVeI&t=253s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'An exclusive license is very different from a non-exclusive license. You also '
              'need to make sure that the agreement addresses reporting. These details can '
              'make a big difference and need to be addressed when you make a deal. '
              'Manufacturing is a business model.',
      'timestamp': 253,
      'timestamp_label': '[00:04:13]',
      'timestamp_seconds': 253,
      'tip': 'An exclusive license is very different from a non-exclusive license. You also '
             'need to make sure that the agreement addresses reporting. These details can make '
             'a big difference and need to be addressed when you make a deal. Manufacturing is '
             'a business model.',
      'title': 'How Inventors Make Money Without Manufacturing Anything: Licensing, Royalties, '
               'and Selling Explained (Patent Question)',
      'url': 'https://www.youtube.com/watch?v=E7nUaZBoVeI&t=253s',
      'video_id': 'E7nUaZBoVeI'},
     {'author': 'BaxterIPAttorneys',
      'channel': 'BaxterIPAttorneys',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=NU_eh8zb6Uk&t=15s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Talking about joint developments and other legal terms within a license '
              'agreement under certain circumstances joint developments can also be planned.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Talking about joint developments and other legal terms within a license '
             'agreement under certain circumstances joint developments can also be planned.',
      'title': 'Term Sheet in Patent Licensing (extended) Part 3- John Baxter '
               '(BaxterIPAttorneys)',
      'url': 'https://www.youtube.com/watch?v=NU_eh8zb6Uk&t=15s',
      'video_id': 'NU_eh8zb6Uk'},
     {'author': 'Berkeley Center for Law & Technology (BCLT)',
      'channel': 'Berkeley Center for Law & Technology (BCLT)',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:28:44](https://www.youtube.com/watch?v=xhIufRgP0ME&t=1724s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s given me a law license, and I'm a patent agent at the same time? The tone of "
              'my voice tells you what my my thoughts on the answer are, that the law degree '
              "qualifies you for nothing. But I'll let the two of you answer.",
      'timestamp': 1724,
      'timestamp_label': '[00:28:44]',
      'timestamp_seconds': 1724,
      'tip': "'s given me a law license, and I'm a patent agent at the same time? The tone of "
             'my voice tells you what my my thoughts on the answer are, that the law degree '
             "qualifies you for nothing. But I'll let the two of you answer.",
      'title': 'Patent Agents, Patent Lawyers, and Unique Career Paths (Berkeley Center for '
               'Law & Technology (BCLT))',
      'url': 'https://www.youtube.com/watch?v=xhIufRgP0ME&t=1724s',
      'video_id': 'xhIufRgP0ME'},
     {'author': 'Book Industry Study Group',
      'channel': 'Book Industry Study Group',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:44:48](https://www.youtube.com/watch?v=Xy0iIdZDIHk&t=2688s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Uh, the idea of of uh a license and a lency sharing um contract numbers or deal '
              'number uh as a way of matching is a really interesting thing.',
      'timestamp': 2688,
      'timestamp_label': '[00:44:48]',
      'timestamp_seconds': 2688,
      'tip': 'Uh, the idea of of uh a license and a lency sharing um contract numbers or deal '
             'number uh as a way of matching is a really interesting thing.',
      'title': 'Rights Royalty Statement Standards: The Details Make the Difference (Book '
               'Industry Study Group)',
      'url': 'https://www.youtube.com/watch?v=Xy0iIdZDIHk&t=2688s',
      'video_id': 'Xy0iIdZDIHk'},
     {'author': 'Mark Reyland',
      'channel': 'Mark Reyland',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:28:51](https://www.youtube.com/watch?v=71FE9YR_9no&t=1731s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "That's like taking your dog to your dentist with all difference to my good "
              "friends in the patent attorney business they're not contract attorneys contract "
              "law is different than patent law I wouldn't take my my patent needs to my "
              'contract attorney.',
      'timestamp': 1731,
      'timestamp_label': '[00:28:51]',
      'timestamp_seconds': 1731,
      'tip': "That's like taking your dog to your dentist with all difference to my good "
             "friends in the patent attorney business they're not contract attorneys contract "
             "law is different than patent law I wouldn't take my my patent needs to my "
             'contract attorney.',
      'title': 'Licensing A Retail Product by Mark Reyland (Mark Reyland)',
      'url': 'https://www.youtube.com/watch?v=71FE9YR_9no&t=1731s',
      'video_id': '71FE9YR_9no'},
     {'author': 'UpCounsel',
      'channel': 'UpCounsel',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:53](https://www.youtube.com/watch?v=AaEw4SGbkk0&t=173s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'A strong licensing agreement  should include several key terms. The scope of '
              'license defines exactly  what rights are granted. The term and.',
      'timestamp': 173,
      'timestamp_label': '[00:02:53]',
      'timestamp_seconds': 173,
      'tip': 'A strong licensing agreement  should include several key terms. The scope of '
             'license defines exactly  what rights are granted. The term and.',
      'title': 'How to Profit from Your Patent Through Licensing (UpCounsel)',
      'url': 'https://www.youtube.com/watch?v=AaEw4SGbkk0&t=173s',
      'video_id': 'AaEw4SGbkk0'},
     {'author': 'Sinorbit Academy',
      'channel': 'Sinorbit Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=-uT7bPngmNc&t=20s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "They're making it, using it, selling it without your permission. That feeling, "
              "yeah, that's the real world impact of patent infringement. It's the moment the "
              'abstract legal right granted by the patent uh collides with actual commercial '
              'activity.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': "They're making it, using it, selling it without your permission. That feeling, "
             "yeah, that's the real world impact of patent infringement. It's the moment the "
             'abstract legal right granted by the patent uh collides with actual commercial '
             'activity.',
      'title': 'TOPIC 18    Patent Infringement and Defences - Intellectual Property Law - UoL '
               '(Sinorbit Academy)',
      'url': 'https://www.youtube.com/watch?v=-uT7bPngmNc&t=20s',
      'video_id': '-uT7bPngmNc'},
     {'author': 'The Good Old Brands',
      'channel': 'The Good Old Brands',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=SemEIJ61Mb0&t=15s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Success begins in the year 1929 when Walt Disney himself signed the first ever '
              'character licensing agreement allowing a company to put Mickey Mouse.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Success begins in the year 1929 when Walt Disney himself signed the first ever '
             'character licensing agreement allowing a company to put Mickey Mouse.',
      'title': "Disney's Licensing Magic  A Global Success Story (The Good Old Brands)",
      'url': 'https://www.youtube.com/watch?v=SemEIJ61Mb0&t=15s',
      'video_id': 'SemEIJ61Mb0'},
     {'author': 'Jim Selbach',
      'channel': 'Jim Selbach',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:28](https://www.youtube.com/watch?v=0r9cstgrqZM&t=208s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Not admitted that's that's obviously the practice of law but what about "
              'advising somebody what if your client is in another state and they ask you for '
              'some advice.',
      'timestamp': 208,
      'timestamp_label': '[00:03:28]',
      'timestamp_seconds': 208,
      'tip': "Not admitted that's that's obviously the practice of law but what about advising "
             'somebody what if your client is in another state and they ask you for some '
             'advice.',
      'title': 'What Is Unauthorized Practice Of Law || Best Advice For Young Lawyers (Jim '
               'Selbach)',
      'url': 'https://www.youtube.com/watch?v=0r9cstgrqZM&t=208s',
      'video_id': '0r9cstgrqZM'},
     {'author': 'Derek Fahey, Esq.',
      'channel': 'Derek Fahey, Esq.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:18](https://www.youtube.com/watch?v=nLSthuXQCL4&t=18s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Fact that wallpaper the different wallpaper designs can actually be protected '
              'both via copyright and also by design patent law.',
      'timestamp': 18,
      'timestamp_label': '[00:00:18]',
      'timestamp_seconds': 18,
      'tip': 'Fact that wallpaper the different wallpaper designs can actually be protected '
             'both via copyright and also by design patent law.',
      'title': 'What is the difference between design patent infringement and Copyright '
               'infringement? (Derek Fahey, Esq.)',
      'url': 'https://www.youtube.com/watch?v=nLSthuXQCL4&t=18s',
      'video_id': 'nLSthuXQCL4'},
     {'author': 'BaxterIPAttorneys',
      'channel': 'BaxterIPAttorneys',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:16](https://www.youtube.com/watch?v=yl8L7tuwNuI&t=316s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Indexation of this royalty come back next week where I'm going to talk about "
              'the IP revisions of a license agreement and how we Define the term of a license '
              'agreement.',
      'timestamp': 316,
      'timestamp_label': '[00:05:16]',
      'timestamp_seconds': 316,
      'tip': "Indexation of this royalty come back next week where I'm going to talk about the "
             'IP revisions of a license agreement and how we Define the term of a license '
             'agreement.',
      'title': 'Term Sheet in Patent Licensing (extended) Part 1- John Baxter '
               '(BaxterIPAttorneys)',
      'url': 'https://www.youtube.com/watch?v=yl8L7tuwNuI&t=316s',
      'video_id': 'yl8L7tuwNuI'},
     {'author': 'docstocTV',
      'channel': 'docstocTV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:52](https://www.youtube.com/watch?v=HbM8XU4hPCc&t=172s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Purpose is to prevent a party from pursuing another transaction while '
              'negotiations are ongoing so these are the key terms to consider when reviewing '
              "any term sheet if you understand these key points you're well on your way to "
              'understanding and negotiating a term sheet.',
      'timestamp': 172,
      'timestamp_label': '[00:02:52]',
      'timestamp_seconds': 172,
      'tip': 'Purpose is to prevent a party from pursuing another transaction while '
             'negotiations are ongoing so these are the key terms to consider when reviewing '
             "any term sheet if you understand these key points you're well on your way to "
             'understanding and negotiating a term sheet.',
      'title': 'Key Terms In All Term Sheets (docstocTV)',
      'url': 'https://www.youtube.com/watch?v=HbM8XU4hPCc&t=172s',
      'video_id': 'HbM8XU4hPCc'},
     {'author': 'inventRightTV',
      'channel': 'inventRightTV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:04](https://www.youtube.com/watch?v=WMcwXYcUD5c&t=184s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'That I was like you gotta be kidding me so he said hey let me look it up and '
              'see if we have given that license to any other guitar pick manufacturer and he '
              "looked up he said no we don't it's open would you like to become a Disney "
              'license.',
      'timestamp': 184,
      'timestamp_label': '[00:03:04]',
      'timestamp_seconds': 184,
      'tip': 'That I was like you gotta be kidding me so he said hey let me look it up and see '
             'if we have given that license to any other guitar pick manufacturer and he '
             "looked up he said no we don't it's open would you like to become a Disney "
             'license.',
      'title': 'What is Brand Licensing? (inventRightTV)',
      'url': 'https://www.youtube.com/watch?v=WMcwXYcUD5c&t=184s',
      'video_id': 'WMcwXYcUD5c'},
     {'author': 'inventRightTV',
      'channel': 'inventRightTV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:08](https://www.youtube.com/watch?v=IMLF0c7wOQI&t=968s)',
      'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                   'intellectual-property licensing, minimum guarantees, and royalty auditing '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I'm meeting companies that's how you work a show but I asked someone the other "
              "day that's kind of a big believer in these trade shows for inventors and I said "
              'all right okay fair enough show me a success.',
      'timestamp': 968,
      'timestamp_label': '[00:16:08]',
      'timestamp_seconds': 968,
      'tip': "I'm meeting companies that's how you work a show but I asked someone the other "
             "day that's kind of a big believer in these trade shows for inventors and I said "
             'all right okay fair enough show me a success.',
      'title': 'How to license your product ideas (inventRightTV)',
      'url': 'https://www.youtube.com/watch?v=IMLF0c7wOQI&t=968s',
      'video_id': 'IMLF0c7wOQI'}],
 10: [{'author': 'Artist Rights Institute',
       'channel': 'Artist Rights Institute',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:27](https://www.youtube.com/watch?v=cirxW12BS2k&t=147s)',
       'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                    'intellectual-property licensing, minimum guarantees, and royalty auditing '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Um but if you have a publishing deal or a label deal, you will have an audit '
               'right uh that would include publishing administrators, um co-publishing deals, '
               'um whatever form it takes.',
       'timestamp': 147,
       'timestamp_label': '[00:02:27]',
       'timestamp_seconds': 147,
       'tip': 'Um but if you have a publishing deal or a label deal, you will have an audit '
              'right uh that would include publishing administrators, um co-publishing deals, '
              'um whatever form it takes.',
       'title': 'Royalty audits, steps and strategies. (Artist Rights Institute)',
       'url': 'https://www.youtube.com/watch?v=cirxW12BS2k&t=147s',
       'video_id': 'cirxW12BS2k'},
      {'author': 'ClintMusic',
       'channel': 'ClintMusic',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:53](https://www.youtube.com/watch?v=2DYtoU6JVRA&t=113s)',
       'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                    'intellectual-property licensing, minimum guarantees, and royalty auditing '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'The old way was waiting for a deal. The new way is building your own catalog '
               "and pitching it directly. But here's where most producers still mess up. They "
               'treat sync licensing like a dumping ground.',
       'timestamp': 113,
       'timestamp_label': '[00:01:53]',
       'timestamp_seconds': 113,
       'tip': 'The old way was waiting for a deal. The new way is building your own catalog '
              "and pitching it directly. But here's where most producers still mess up. They "
              'treat sync licensing like a dumping ground.',
       'title': 'Why The Old Sync Licensing Rules No Longer Apply (ClintMusic)',
       'url': 'https://www.youtube.com/watch?v=2DYtoU6JVRA&t=113s',
       'video_id': '2DYtoU6JVRA'},
      {'author': 'Producer Royalty',
       'channel': 'Producer Royalty',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:28](https://www.youtube.com/watch?v=gN8CTjqp8lA&t=388s)',
       'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                    'intellectual-property licensing, minimum guarantees, and royalty auditing '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "There's plenty of companies, you know, that offer these standard template "
               "deals where it's just a split with no advance money. You can do it, but if you "
               "want to negotiate and ask for money, it's it's possible.",
       'timestamp': 388,
       'timestamp_label': '[00:06:28]',
       'timestamp_seconds': 388,
       'tip': "There's plenty of companies, you know, that offer these standard template deals "
              "where it's just a split with no advance money. You can do it, but if you want "
              "to negotiate and ask for money, it's it's possible.",
       'title': 'Producer Publishing Deals in 2026 (Music Attorneys Explain) (Producer '
                'Royalty)',
       'url': 'https://www.youtube.com/watch?v=gN8CTjqp8lA&t=388s',
       'video_id': 'gN8CTjqp8lA'},
      {'author': 'macProVideoDotCom',
       'channel': 'macProVideoDotCom',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:50](https://www.youtube.com/watch?v=tk2j8egQtvo&t=50s)',
       'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                    'intellectual-property licensing, minimum guarantees, and royalty auditing '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Performance not included, aka non-performance income. 's 50% deal, as is your "
               '50% and logged into their financial books as going towards your recoupment, '
               'they keep all $5,000 or 100% of the income this time because your advance has '
               'not been fully recouped.',
       'timestamp': 50,
       'timestamp_label': '[00:00:50]',
       'timestamp_seconds': 50,
       'tip': "Performance not included, aka non-performance income. 's 50% deal, as is your "
              '50% and logged into their financial books as going towards your recoupment, '
              'they keep all $5,000 or 100% of the income this time because your advance has '
              'not been fully recouped.',
       'title': 'Music Business 102: Mechanical Royalties and Licensing - 18. Recoupment at '
                '50-50 (macProVideoDotCom)',
       'url': 'https://www.youtube.com/watch?v=tk2j8egQtvo&t=50s',
       'video_id': 'tk2j8egQtvo'},
      {'author': 'Alex G. Lee',
       'channel': 'Alex G. Lee',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:41](https://www.youtube.com/watch?v=Yg9nVJp45oo&t=461s)',
       'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                    'intellectual-property licensing, minimum guarantees, and royalty auditing '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'AI and then I just do uh I I just prove it in a conceptual level is working '
               'and then I I want to share with you and then I I want to have some opportunity '
               'to have a further collaboration to develop this as a commercial product in in '
               'the later stage.',
       'timestamp': 461,
       'timestamp_label': '[00:07:41]',
       'timestamp_seconds': 461,
       'tip': 'AI and then I just do uh I I just prove it in a conceptual level is working and '
              'then I I want to share with you and then I I want to have some opportunity to '
              'have a further collaboration to develop this as a commercial product in in the '
              'later stage.',
       'title': 'AI Agent-Powered Autonomous Patent Management & Monetization Webinar (Alex G. '
                'Lee)',
       'url': 'https://www.youtube.com/watch?v=Yg9nVJp45oo&t=461s',
       'video_id': 'Yg9nVJp45oo'},
      {'author': 'inventRightTV',
       'channel': 'inventRightTV',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:06](https://www.youtube.com/watch?v=KOR6yXD1nTQ&t=186s)',
       'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                    'intellectual-property licensing, minimum guarantees, and royalty auditing '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Stephen, let's get going, man. Well, first of all, first question, everyone "
               "raise your hand if you're building cell sheets or using AI now. Raise your "
               "hand if you're using it now. If you're not, all right, this is going to be a "
               'good good class for you tonight.',
       'timestamp': 186,
       'timestamp_label': '[00:03:06]',
       'timestamp_seconds': 186,
       'tip': "Stephen, let's get going, man. Well, first of all, first question, everyone "
              "raise your hand if you're building cell sheets or using AI now. Raise your hand "
              "if you're using it now. If you're not, all right, this is going to be a good "
              'good class for you tonight.',
       'title': 'How AI Can Help You Get a Licensing Deal (inventRightTV)',
       'url': 'https://www.youtube.com/watch?v=KOR6yXD1nTQ&t=186s',
       'video_id': 'KOR6yXD1nTQ'},
      {'author': 'Agi Entertainment | The Star Maker',
       'channel': 'Agi Entertainment | The Star Maker',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:28](https://www.youtube.com/watch?v=yC0aLTouh44&t=88s)',
       'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                    'intellectual-property licensing, minimum guarantees, and royalty auditing '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Take time to review every single clause. You know, certain words that you '
               'might think mean a particular thing could mean something slightly different as '
               'it relates to the entertainment business, right?',
       'timestamp': 88,
       'timestamp_label': '[00:01:28]',
       'timestamp_seconds': 88,
       'tip': 'Take time to review every single clause. You know, certain words that you might '
              'think mean a particular thing could mean something slightly different as it '
              'relates to the entertainment business, right?',
       'title': 'What Every Artist Must Know About Music Contracts and Royalties (Agi '
                'Entertainment | The Star Maker)',
       'url': 'https://www.youtube.com/watch?v=yC0aLTouh44&t=88s',
       'video_id': 'yC0aLTouh44'},
      {'author': 'Schwegman Lundberg & Woessner, P.A.',
       'channel': 'Schwegman Lundberg & Woessner, P.A.',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:13:42](https://www.youtube.com/watch?v=YwEyzgLoOrA&t=822s)',
       'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                    'intellectual-property licensing, minimum guarantees, and royalty auditing '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'s starting to grow more and more. So we're at 20 15 20% of the deals are now "
               "AI related and we're seeing machine learning growing and we're seeing a "
               "combination of both growing. Other part of this that's interesting, they don't "
               'sell as well.',
       'timestamp': 822,
       'timestamp_label': '[00:13:42]',
       'timestamp_seconds': 822,
       'tip': "'s starting to grow more and more. So we're at 20 15 20% of the deals are now "
              "AI related and we're seeing machine learning growing and we're seeing a "
              "combination of both growing. Other part of this that's interesting, they don't "
              'sell as well.',
       'title': 'Patent Monetization (Schwegman Lundberg & Woessner, P.A.)',
       'url': 'https://www.youtube.com/watch?v=YwEyzgLoOrA&t=822s',
       'video_id': 'YwEyzgLoOrA'},
      {'author': 'UC Riverside Innovation & Entrepreneurship',
       'channel': 'UC Riverside Innovation & Entrepreneurship',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:21](https://www.youtube.com/watch?v=DsnLgDwQddQ&t=21s)',
       'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                    'intellectual-property licensing, minimum guarantees, and royalty auditing '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Translates University Research and discoveries to the private sector and '
               'contributes to building a solid entrepreneurial ecosystem in our region.',
       'timestamp': 21,
       'timestamp_label': '[00:00:21]',
       'timestamp_seconds': 21,
       'tip': 'Translates University Research and discoveries to the private sector and '
              'contributes to building a solid entrepreneurial ecosystem in our region.',
       'title': 'Intro to Technology Commercialization (UC Riverside Innovation & '
                'Entrepreneurship)',
       'url': 'https://www.youtube.com/watch?v=DsnLgDwQddQ&t=21s',
       'video_id': 'DsnLgDwQddQ'},
      {'author': 'Legal Tips for Smart Entrepreneurs',
       'channel': 'Legal Tips for Smart Entrepreneurs',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:27](https://www.youtube.com/watch?v=GLaoDfT8SDA&t=147s)',
       'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                    'intellectual-property licensing, minimum guarantees, and royalty auditing '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Product but you should still go into these types of deals with you know a full '
               'set of eyes and some advice on how to structure them so this is attorney Dan '
               "x-wind coming at you with some information about licensing deals and I'll talk "
               'to you later.',
       'timestamp': 147,
       'timestamp_label': '[00:02:27]',
       'timestamp_seconds': 147,
       'tip': 'Product but you should still go into these types of deals with you know a full '
              'set of eyes and some advice on how to structure them so this is attorney Dan '
              "x-wind coming at you with some information about licensing deals and I'll talk "
              'to you later.',
       'title': 'Negotiate Like a Pro: Secure Your Royalties with This Licensing Fee Secret '
                '(Legal Tips for Smart Entrepreneurs)',
       'url': 'https://www.youtube.com/watch?v=GLaoDfT8SDA&t=147s',
       'video_id': 'GLaoDfT8SDA'},
      {'author': 'UIA TV',
       'channel': 'UIA TV',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:58:40](https://www.youtube.com/watch?v=3N-s4ptr2VU&t=3520s)',
       'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                    'intellectual-property licensing, minimum guarantees, and royalty auditing '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Titan things right loketten en and analyze and cheat wrappers vond en alright '
               "shacho item ziet er ai laik inzoomen om les marques killer items' soort "
               'curcumin en kwik hangen get it dit word about a cutting for liesbeth yahoo '
               'mail.',
       'timestamp': 3520,
       'timestamp_label': '[00:58:40]',
       'timestamp_seconds': 3520,
       'tip': 'Titan things right loketten en and analyze and cheat wrappers vond en alright '
              "shacho item ziet er ai laik inzoomen om les marques killer items' soort "
              'curcumin en kwik hangen get it dit word about a cutting for liesbeth yahoo '
              'mail.',
       'title': 'Manufacturing & Licensing: How To License Your Product (UIA TV)',
       'url': 'https://www.youtube.com/watch?v=3N-s4ptr2VU&t=3520s',
       'video_id': '3N-s4ptr2VU'},
      {'author': 'Licensing Basics',
       'channel': 'Licensing Basics',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:47](https://www.youtube.com/watch?v=uBnJLlSWMLk&t=167s)',
       'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                    'intellectual-property licensing, minimum guarantees, and royalty auditing '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Learn more about the licensing industry please check out my free webinar you '
               "can go to licensing basics comm and get registered today you're going to learn "
               "a lot of valuable information again my name is Ryan Stewart I'm the licensing "
               'expert thanks.',
       'timestamp': 167,
       'timestamp_label': '[00:02:47]',
       'timestamp_seconds': 167,
       'tip': 'Learn more about the licensing industry please check out my free webinar you '
              "can go to licensing basics comm and get registered today you're going to learn "
              "a lot of valuable information again my name is Ryan Stewart I'm the licensing "
              'expert thanks.',
       'title': "What's more important than your royalty rate in a licensing deal? (Licensing "
                'Basics)',
       'url': 'https://www.youtube.com/watch?v=uBnJLlSWMLk&t=167s',
       'video_id': 'uBnJLlSWMLk'},
      {'author': 'Salk Institute',
       'channel': 'Salk Institute',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:58:04](https://www.youtube.com/watch?v=3iEjObMZnZo&t=3484s)',
       'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                    'intellectual-property licensing, minimum guarantees, and royalty auditing '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Interesting Supreme Court case that just uh was decided in the last week or so '
               'uh dealing with University invention so uh come on back thanks.',
       'timestamp': 3484,
       'timestamp_label': '[00:58:04]',
       'timestamp_seconds': 3484,
       'tip': 'Interesting Supreme Court case that just uh was decided in the last week or so '
              'uh dealing with University invention so uh come on back thanks.',
       'title': 'Intellectual Property and Technology Transfer - Why is Academia Suddenly So '
                'Interested in Patents? (Salk Institute)',
       'url': 'https://www.youtube.com/watch?v=3iEjObMZnZo&t=3484s',
       'video_id': '3iEjObMZnZo'},
      {'author': 'UpCounsel',
       'channel': 'UpCounsel',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:40](https://www.youtube.com/watch?v=Lpv4Uq-cOLA&t=160s)',
       'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                    'intellectual-property licensing, minimum guarantees, and royalty auditing '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'By understanding the basics of patent licensing and avoiding common pitfalls, '
               'you can maximize the value of your intellectual property and contribute to '
               'technological progress.',
       'timestamp': 160,
       'timestamp_label': '[00:02:40]',
       'timestamp_seconds': 160,
       'tip': 'By understanding the basics of patent licensing and avoiding common pitfalls, '
              'you can maximize the value of your intellectual property and contribute to '
              'technological progress.',
       'title': 'Patent Licensing  How It Works and What You Need to Know (UpCounsel)',
       'url': 'https://www.youtube.com/watch?v=Lpv4Uq-cOLA&t=160s',
       'video_id': 'Lpv4Uq-cOLA'},
      {'author': 'inventRightTV',
       'channel': 'inventRightTV',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:14:30](https://www.youtube.com/watch?v=INuH7fr5H40&t=870s)',
       'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                    'intellectual-property licensing, minimum guarantees, and royalty auditing '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Information from people that have done it repeatedly so thank you for watching '
               'this video until next time this is stephen key.',
       'timestamp': 870,
       'timestamp_label': '[00:14:30]',
       'timestamp_seconds': 870,
       'tip': 'Information from people that have done it repeatedly so thank you for watching '
              'this video until next time this is stephen key.',
       'title': 'How to License Your Ideas and Make Money (Your Honest Guide to Profitable '
                'Inventing) (inventRightTV)',
       'url': 'https://www.youtube.com/watch?v=INuH7fr5H40&t=870s',
       'video_id': 'INuH7fr5H40'}],
 11: [{'author': 'Flowhaven',
       'channel': 'Flowhaven',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:05](https://www.youtube.com/watch?v=HkDV-RELNXc&t=185s)',
       'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                    'intellectual-property licensing, minimum guarantees, and royalty auditing '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Flowhaven checks every line against the agreement. Sales in a territory that '
               "was never granted. A product that was never approved. And a rate that doesn't "
               'match the contract. Your team sends those lines back to the partner, accepts '
               'the rest, and raises the invoice request.',
       'timestamp': 185,
       'timestamp_label': '[00:03:05]',
       'timestamp_seconds': 185,
       'tip': 'Flowhaven checks every line against the agreement. Sales in a territory that '
              "was never granted. A product that was never approved. And a rate that doesn't "
              'match the contract. Your team sends those lines back to the partner, accepts '
              'the rest, and raises the invoice request.',
       'title': 'How brand licensing teams run agreements, approvals and royalties in one '
                'place (Flowhaven)',
       'url': 'https://www.youtube.com/watch?v=HkDV-RELNXc&t=185s',
       'video_id': 'HkDV-RELNXc'},
      {'author': 'INDIAN MARKETS DECODED',
       'channel': 'INDIAN MARKETS DECODED',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:40](https://www.youtube.com/watch?v=3P0vRsEmqtY&t=40s)',
       'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                    'intellectual-property licensing, minimum guarantees, and royalty auditing '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'s streaming a song, playing it in a coffee shop, or licensing it from massive "
               'brand campaign. There is absolutely zero distraction from unrelated '
               'operations. The entire business is built around one single thing, acquiring '
               'and renting out intellectual property.',
       'timestamp': 40,
       'timestamp_label': '[00:00:40]',
       'timestamp_seconds': 40,
       'tip': "'s streaming a song, playing it in a coffee shop, or licensing it from massive "
              'brand campaign. There is absolutely zero distraction from unrelated operations. '
              'The entire business is built around one single thing, acquiring and renting out '
              'intellectual property.',
       'title': 'Decoding Pure-Play Licensing Model: High Margin Royalty Cash Flows | Industry '
                'Terms (INDIAN MARKETS DECODED)',
       'url': 'https://www.youtube.com/watch?v=3P0vRsEmqtY&t=40s',
       'video_id': '3P0vRsEmqtY'},
      {'author': 'Technology Licensing Office (TLO)',
       'channel': 'Technology Licensing Office (TLO)',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:53:52](https://www.youtube.com/watch?v=2ADE7tP4bYM&t=3232s)',
       'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                    'intellectual-property licensing, minimum guarantees, and royalty auditing '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'MIT, we require that the company provide us a business plan that explains to '
               'us how they intend to commercialize the MIT Technology with what resources, '
               'with what team.',
       'timestamp': 3232,
       'timestamp_label': '[00:53:52]',
       'timestamp_seconds': 3232,
       'tip': 'MIT, we require that the company provide us a business plan that explains to us '
              'how they intend to commercialize the MIT Technology with what resources, with '
              'what team.',
       'title': 'Commercialization of MIT Technology (Technology Licensing Office (TLO))',
       'url': 'https://www.youtube.com/watch?v=2ADE7tP4bYM&t=3232s',
       'video_id': '2ADE7tP4bYM'},
      {'author': 'USPTOvideo',
       'channel': 'USPTOvideo',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:31:21](https://www.youtube.com/watch?v=hwcNfSr-ia0&t=1881s)',
       'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                    'intellectual-property licensing, minimum guarantees, and royalty auditing '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Yeah, I agree wholeheartedly with Laura and especially thinking through you '
               "can't have a single person who's gonna understand all the different parts of "
               'business, marketing, finance, operations, legal, regulatory. I mean, I can '
               'even just give you an example.',
       'timestamp': 1881,
       'timestamp_label': '[00:31:21]',
       'timestamp_seconds': 1881,
       'tip': 'Yeah, I agree wholeheartedly with Laura and especially thinking through you '
              "can't have a single person who's gonna understand all the different parts of "
              'business, marketing, finance, operations, legal, regulatory. I mean, I can even '
              'just give you an example.',
       'title': 'Tech Transfer and Commercialization (USPTOvideo)',
       'url': 'https://www.youtube.com/watch?v=hwcNfSr-ia0&t=1881s',
       'video_id': 'hwcNfSr-ia0'},
      {'author': 'inventRightTV',
       'channel': 'inventRightTV',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:03](https://www.youtube.com/watch?v=p3ODWhpvt3E&t=183s)',
       'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                    'intellectual-property licensing, minimum guarantees, and royalty auditing '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "We know what they're going to be asking and we know why they they sign "
               "licensing deals. And there's certain things that they need to see in order for "
               'you to get the deal.',
       'timestamp': 183,
       'timestamp_label': '[00:03:03]',
       'timestamp_seconds': 183,
       'tip': "We know what they're going to be asking and we know why they they sign "
              "licensing deals. And there's certain things that they need to see in order for "
              'you to get the deal.',
       'title': 'The #1 Thing Companies Want Before Buying Your Idea (inventRightTV)',
       'url': 'https://www.youtube.com/watch?v=p3ODWhpvt3E&t=183s',
       'video_id': 'p3ODWhpvt3E'},
      {'author': 'OSU Center for Clinical and Translational Science',
       'channel': 'OSU Center for Clinical and Translational Science',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:16:50](https://www.youtube.com/watch?v=HKAvhkDKxNQ&t=1010s)',
       'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                    'intellectual-property licensing, minimum guarantees, and royalty auditing '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Commercial scale clearly the the research that is being done and as you saw '
               "the numbers you know if it's if it's getting 150 plus products in the market.",
       'timestamp': 1010,
       'timestamp_label': '[00:16:50]',
       'timestamp_seconds': 1010,
       'tip': 'Commercial scale clearly the the research that is being done and as you saw the '
              "numbers you know if it's if it's getting 150 plus products in the market.",
       'title': 'Technology Transfer and Intellectual Property (OSU Center for Clinical and '
                'Translational Science)',
       'url': 'https://www.youtube.com/watch?v=HKAvhkDKxNQ&t=1010s',
       'video_id': 'HKAvhkDKxNQ'},
      {'author': 'Patent Question',
       'channel': 'Patent Question',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:40](https://www.youtube.com/watch?v=dlTT-hWgkB8&t=100s)',
       'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                    'intellectual-property licensing, minimum guarantees, and royalty auditing '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'You can also use your invention as a foundation for your own company. This '
               'path gives you the highest potential upside, but also is going to take the '
               "most effort. You'll need to handle product development, marketing, operations, "
               'and sales. But the advantage is control.',
       'timestamp': 100,
       'timestamp_label': '[00:01:40]',
       'timestamp_seconds': 100,
       'tip': 'You can also use your invention as a foundation for your own company. This path '
              'gives you the highest potential upside, but also is going to take the most '
              "effort. You'll need to handle product development, marketing, operations, and "
              'sales. But the advantage is control.',
       'title': 'Patents Explained – How to Make Money from a Patent | Rich Goldstein (Patent '
                'Question)',
       'url': 'https://www.youtube.com/watch?v=dlTT-hWgkB8&t=100s',
       'video_id': 'dlTT-hWgkB8'},
      {'author': 'MIT Bootcamps',
       'channel': 'MIT Bootcamps',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:45](https://www.youtube.com/watch?v=SPgUdIOB0IM&t=465s)',
       'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                    'intellectual-property licensing, minimum guarantees, and royalty auditing '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Under 18 and it's a long time since I've been there they can't enforce it "
               "there's also they said you know this apply non-competes against unpaid interns "
               'is.',
       'timestamp': 465,
       'timestamp_label': '[00:07:45]',
       'timestamp_seconds': 465,
       'tip': "Under 18 and it's a long time since I've been there they can't enforce it "
              "there's also they said you know this apply non-competes against unpaid interns "
              'is.',
       'title': 'How IP can strategically advance your business goals (MIT Bootcamps)',
       'url': 'https://www.youtube.com/watch?v=SPgUdIOB0IM&t=465s',
       'video_id': 'SPgUdIOB0IM'},
      {'author': 'Eric Hanscom (ICIP)',
       'channel': 'Eric Hanscom (ICIP)',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:43](https://www.youtube.com/watch?v=yUPS-UISPnQ&t=283s)',
       'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                    'intellectual-property licensing, minimum guarantees, and royalty auditing '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Complete control they get to keep all the money that's left over however it's "
               'going to become more than a full-time job for one person so the second route.',
       'timestamp': 283,
       'timestamp_label': '[00:04:43]',
       'timestamp_seconds': 283,
       'tip': "Complete control they get to keep all the money that's left over however it's "
              'going to become more than a full-time job for one person so the second route.',
       'title': 'ICIP presents:  Intellectual Property Licensing - Three Main Ways To Make '
                'Money on Your Invention (Eric Hanscom (ICIP))',
       'url': 'https://www.youtube.com/watch?v=yUPS-UISPnQ&t=283s',
       'video_id': 'yUPS-UISPnQ'},
      {'author': 'Informa Connect Life Sciences',
       'channel': 'Informa Connect Life Sciences',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:40](https://www.youtube.com/watch?v=Dd9V4RSqNuk&t=220s)',
       'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                    'intellectual-property licensing, minimum guarantees, and royalty auditing '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Time out of the hundreds in the US are making money and it's not always the "
               "same ones so from a business point of view it's more like a lottery but from.",
       'timestamp': 220,
       'timestamp_label': '[00:03:40]',
       'timestamp_seconds': 220,
       'tip': "Time out of the hundreds in the US are making money and it's not always the "
              "same ones so from a business point of view it's more like a lottery but from.",
       'title': 'BWB TV: Commercializing university research with Lita Nelsen, MIT (Informa '
                'Connect Life Sciences)',
       'url': 'https://www.youtube.com/watch?v=Dd9V4RSqNuk&t=220s',
       'video_id': 'Dd9V4RSqNuk'},
      {'author': 'Innovent Law',
       'channel': 'Innovent Law',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:40](https://www.youtube.com/watch?v=boXHxU-4qd8&t=100s)',
       'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                    'intellectual-property licensing, minimum guarantees, and royalty auditing '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Uh money you've decided on the second one licensing that's something that you "
               'have a little bit more control and flexibility over in a sense where you.',
       'timestamp': 100,
       'timestamp_label': '[00:01:40]',
       'timestamp_seconds': 100,
       'tip': "Uh money you've decided on the second one licensing that's something that you "
              'have a little bit more control and flexibility over in a sense where you.',
       'title': 'Patent Monetizing Strategies Every Entrepreneur Should Know (Innovent Law)',
       'url': 'https://www.youtube.com/watch?v=boXHxU-4qd8&t=100s',
       'video_id': 'boXHxU-4qd8'},
      {'author': 'B&H Photo Video Pro Audio',
       'channel': 'B&H Photo Video Pro Audio',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[01:31:05](https://www.youtube.com/watch?v=74bQUodJbWY&t=5465s)',
       'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                    'intellectual-property licensing, minimum guarantees, and royalty auditing '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'You guys outside thanks for more information please visit us online give us a '
               'call or stop by our New York City Superstore you can also connect with us on '
               'the web.',
       'timestamp': 5465,
       'timestamp_label': '[01:31:05]',
       'timestamp_seconds': 5465,
       'tip': 'You guys outside thanks for more information please visit us online give us a '
              'call or stop by our New York City Superstore you can also connect with us on '
              'the web.',
       'title': 'Registration Counts: How to Copyright Your Images (B&H Photo Video Pro Audio)',
       'url': 'https://www.youtube.com/watch?v=74bQUodJbWY&t=5465s',
       'video_id': '74bQUodJbWY'},
      {'author': 'Osage University Partners',
       'channel': 'Osage University Partners',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[01:13:12](https://www.youtube.com/watch?v=Q3YzwCiT2M4&t=4392s)',
       'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                    'intellectual-property licensing, minimum guarantees, and royalty auditing '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "It's it's meant to really reflect what the company's anticipated minimum "
               'royalty is going to be for that year so the the goal is that they would '
               'essentially never pay this amount because their projected royalties are always '
               'going to be higher than this set minimum.',
       'timestamp': 4392,
       'timestamp_label': '[01:13:12]',
       'timestamp_seconds': 4392,
       'tip': "It's it's meant to really reflect what the company's anticipated minimum "
              'royalty is going to be for that year so the the goal is that they would '
              'essentially never pay this amount because their projected royalties are always '
              'going to be higher than this set minimum.',
       'title': 'Startup Licensing 101: Term Sheets & Financials (Osage University Partners)',
       'url': 'https://www.youtube.com/watch?v=Q3YzwCiT2M4&t=4392s',
       'video_id': 'Q3YzwCiT2M4'},
      {'author': 'inventRightTV',
       'channel': 'inventRightTV',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:22](https://www.youtube.com/watch?v=_aiJZ1WKmfc&t=82s)',
       'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                    'intellectual-property licensing, minimum guarantees, and royalty auditing '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Being taught that the university level is to start a business but not '
               'everybody wants to start a business not every.',
       'timestamp': 82,
       'timestamp_label': '[00:01:22]',
       'timestamp_seconds': 82,
       'tip': 'Being taught that the university level is to start a business but not everybody '
              'wants to start a business not every.',
       'title': 'The Game-Changing Power of Open Innovation (inventRightTV)',
       'url': 'https://www.youtube.com/watch?v=_aiJZ1WKmfc&t=82s',
       'video_id': '_aiJZ1WKmfc'},
      {'author': 'Uncover Fraud',
       'channel': 'Uncover Fraud',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:45](https://www.youtube.com/watch?v=9Fku-QlhyHc&t=45s)',
       'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                    'intellectual-property licensing, minimum guarantees, and royalty auditing '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "In this video, I'm going to explain reasons for contract non-compliance, "
               'benefits of royalty audits, how to conduct a royalty audit, and the benefits '
               'of a forensic royalty audit. What you learn in this video, you will be able to '
               'use straight away in your business.',
       'timestamp': 45,
       'timestamp_label': '[00:00:45]',
       'timestamp_seconds': 45,
       'tip': "In this video, I'm going to explain reasons for contract non-compliance, "
              'benefits of royalty audits, how to conduct a royalty audit, and the benefits of '
              'a forensic royalty audit. What you learn in this video, you will be able to use '
              'straight away in your business.',
       'title': 'Royalty Audit: Why Every Licensor & Artist Needs a Forensic Accountant on '
                'Their Side | Uncover Fraud (Uncover Fraud)',
       'url': 'https://www.youtube.com/watch?v=9Fku-QlhyHc&t=45s',
       'video_id': '9Fku-QlhyHc'}],
 12: [{'author': 'PKF Texas',
       'channel': 'PKF Texas',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:04](https://www.youtube.com/watch?v=Z-vXnFsa6zY&t=124s)',
       'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                    'intellectual-property licensing, minimum guarantees, and royalty auditing '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'But we can help both licensors if they want to audit licensees and help '
               "licensees if they are ever getting audited. All right, well, we'll get you "
               'back to talk a little bit more about contract compliance. For more information '
               'about this topic, visit PKFTexas.',
       'timestamp': 124,
       'timestamp_label': '[00:02:04]',
       'timestamp_seconds': 124,
       'tip': 'But we can help both licensors if they want to audit licensees and help '
              "licensees if they are ever getting audited. All right, well, we'll get you back "
              'to talk a little bit more about contract compliance. For more information about '
              'this topic, visit PKFTexas.',
       'title': "Red Flags in Licensing and Royalty Audits | PKF Texas - The Entrepreneur's "
                'Playbook (PKF Texas)',
       'url': 'https://www.youtube.com/watch?v=Z-vXnFsa6zY&t=124s',
       'video_id': 'Z-vXnFsa6zY'},
      {'author': 'Jason Varner',
       'channel': 'Jason Varner',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:49](https://www.youtube.com/watch?v=0ZCFBJ3aOOA&t=589s)',
       'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                    'intellectual-property licensing, minimum guarantees, and royalty auditing '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "So there's a lot of options. You don't got to rush into it. Um you can email "
               "me, jason@datahasvalue. Um I'm researching this stuff every day. Um on the "
               'site you also see I put a deal tracker in yesterday that has um recent data '
               'licensing deals.',
       'timestamp': 589,
       'timestamp_label': '[00:09:49]',
       'timestamp_seconds': 589,
       'tip': "So there's a lot of options. You don't got to rush into it. Um you can email "
              "me, jason@datahasvalue. Um I'm researching this stuff every day. Um on the site "
              'you also see I put a deal tracker in yesterday that has um recent data '
              'licensing deals.',
       'title': "Should You License Your Advisory Firm's Data for AI Training? (Jason Varner)",
       'url': 'https://www.youtube.com/watch?v=0ZCFBJ3aOOA&t=589s',
       'video_id': '0ZCFBJ3aOOA'},
      {'author': 'Elite Music Coaching',
       'channel': 'Elite Music Coaching',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:11:59](https://www.youtube.com/watch?v=D6XhETdysBM&t=719s)',
       'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                    'intellectual-property licensing, minimum guarantees, and royalty auditing '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'It could be the thing that finally gives you the freedom to create music '
               "full-time. But only if you build it with intention. Look, I'll be honest with "
               'you, building a catalog that generates income every day is not about getting '
               'lucky with one massive placement.',
       'timestamp': 719,
       'timestamp_label': '[00:11:59]',
       'timestamp_seconds': 719,
       'tip': 'It could be the thing that finally gives you the freedom to create music '
              "full-time. But only if you build it with intention. Look, I'll be honest with "
              'you, building a catalog that generates income every day is not about getting '
              'lucky with one massive placement.',
       'title': 'How to Build a Music Catalog That Pays You for Years (Sync Licensing '
                'Strategy) (Elite Music Coaching)',
       'url': 'https://www.youtube.com/watch?v=D6XhETdysBM&t=719s',
       'video_id': 'D6XhETdysBM'},
      {'author': 'Go:lofty - The Official Channel',
       'channel': 'Go:lofty - The Official Channel',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:25](https://www.youtube.com/watch?v=A4bw9yuaOVo&t=25s)',
       'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                    'intellectual-property licensing, minimum guarantees, and royalty auditing '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "So, let's start with the basics. What exactly is an IP strategy? Your IP "
               'strategy is your game plan for how you protect, manage, and monetize your '
               "business's unique ideas, inventions, designs, and innovations. It's not just "
               'about legal protection.',
       'timestamp': 25,
       'timestamp_label': '[00:00:25]',
       'timestamp_seconds': 25,
       'tip': "So, let's start with the basics. What exactly is an IP strategy? Your IP "
              'strategy is your game plan for how you protect, manage, and monetize your '
              "business's unique ideas, inventions, designs, and innovations. It's not just "
              'about legal protection.',
       'title': 'Intellectual Property Strategy – Protect, Lead, and Monetize Innovation '
                '(Go:lofty - The Official Channel)',
       'url': 'https://www.youtube.com/watch?v=A4bw9yuaOVo&t=25s',
       'video_id': 'A4bw9yuaOVo'},
      {'author': 'Sabarwal Law',
       'channel': 'Sabarwal Law',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:12](https://www.youtube.com/watch?v=4ZKPBotNzQw&t=192s)',
       'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                    'intellectual-property licensing, minimum guarantees, and royalty auditing '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'The contract and things like that or there are more formal audits where we '
               'give audit notice to a counterparty and um everything is more official usually '
               "there's attorneys involved.",
       'timestamp': 192,
       'timestamp_label': '[00:03:12]',
       'timestamp_seconds': 192,
       'tip': 'The contract and things like that or there are more formal audits where we give '
              'audit notice to a counterparty and um everything is more official usually '
              "there's attorneys involved.",
       'title': '22.5. What is a Royalty Audit (Sabarwal Law)',
       'url': 'https://www.youtube.com/watch?v=4ZKPBotNzQw&t=192s',
       'video_id': '4ZKPBotNzQw'},
      {'author': 'American Physiological Society',
       'channel': 'American Physiological Society',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:42:04](https://www.youtube.com/watch?v=jxdKIK4n-Dk&t=2524s)',
       'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                    'intellectual-property licensing, minimum guarantees, and royalty auditing '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Um at NYU we have our own startup manager and like her job is just to really '
               'really help researchers and students you know define a clear um '
               'commercialization plan. Um we also have different resources for filed members '
               'to um fundra.',
       'timestamp': 2524,
       'timestamp_label': '[00:42:04]',
       'timestamp_seconds': 2524,
       'tip': 'Um at NYU we have our own startup manager and like her job is just to really '
              'really help researchers and students you know define a clear um '
              'commercialization plan. Um we also have different resources for filed members '
              'to um fundra.',
       'title': 'Engaging Your Technology Transfer Office to Translate Research into Patents '
                '(American Physiological Society)',
       'url': 'https://www.youtube.com/watch?v=jxdKIK4n-Dk&t=2524s',
       'video_id': 'jxdKIK4n-Dk'},
      {'author': 'Authors Guild',
       'channel': 'Authors Guild',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:51:51](https://www.youtube.com/watch?v=NrMiKZwGTD4&t=3111s)',
       'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                    'intellectual-property licensing, minimum guarantees, and royalty auditing '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'And if so, um what terms did you try especially hard to get that are not '
               "normally granted to authors? So, again, um I think in the in I don't want to "
               'say in the old days, but um 15 to 20 years ago, audit clauses were in um a lot '
               'of contracts and they were very general.',
       'timestamp': 3111,
       'timestamp_label': '[00:51:51]',
       'timestamp_seconds': 3111,
       'tip': 'And if so, um what terms did you try especially hard to get that are not '
              "normally granted to authors? So, again, um I think in the in I don't want to "
              'say in the old days, but um 15 to 20 years ago, audit clauses were in um a lot '
              'of contracts and they were very general.',
       'title': 'Understanding Your Royalty Statements and Learning What Questions to Ask Your '
                'Publisher (Authors Guild)',
       'url': 'https://www.youtube.com/watch?v=NrMiKZwGTD4&t=3111s',
       'video_id': 'NrMiKZwGTD4'},
      {'author': 'Alexa Donne',
       'channel': 'Alexa Donne',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:22:44](https://www.youtube.com/watch?v=yAYeomyyeP8&t=1364s)',
       'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                    'intellectual-property licensing, minimum guarantees, and royalty auditing '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Your advance and you start earning royalties you were steadily selling copies '
               "and so you'll get payments every six months they will vary widely how.",
       'timestamp': 1364,
       'timestamp_label': '[00:22:44]',
       'timestamp_seconds': 1364,
       'tip': 'Your advance and you start earning royalties you were steadily selling copies '
              "and so you'll get payments every six months they will vary widely how.",
       'title': 'How Book Advances and Royalties Work (Alexa Donne)',
       'url': 'https://www.youtube.com/watch?v=yAYeomyyeP8&t=1364s',
       'video_id': 'yAYeomyyeP8'},
      {'author': 'inventRightTV',
       'channel': 'inventRightTV',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:38](https://www.youtube.com/watch?v=WEVVJ111b8o&t=278s)',
       'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                    'intellectual-property licensing, minimum guarantees, and royalty auditing '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'A third of which went to my agent so okay but and it still does it sells today '
               "but you know it's not nearly like I remember in the early days I get a.",
       'timestamp': 278,
       'timestamp_label': '[00:04:38]',
       'timestamp_seconds': 278,
       'tip': 'A third of which went to my agent so okay but and it still does it sells today '
              "but you know it's not nearly like I remember in the early days I get a.",
       'title': 'How This Inventor Earned $10 Million In Royalties! (inventRightTV)',
       'url': 'https://www.youtube.com/watch?v=WEVVJ111b8o&t=278s',
       'video_id': 'WEVVJ111b8o'},
      {'author': 'SeltzerLicensingGrp',
       'channel': 'SeltzerLicensingGrp',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:34](https://www.youtube.com/watch?v=7LHR9Jso37I&t=214s)',
       'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                    'intellectual-property licensing, minimum guarantees, and royalty auditing '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Items the license or has to approve the product but is it going to be ten days '
               "and what if they don't respond in ten days so the key thing it's all about "
               'negotiating and you know the two sides and just remember key rule to '
               "negotiating is that everything's negotiable.",
       'timestamp': 214,
       'timestamp_label': '[00:03:34]',
       'timestamp_seconds': 214,
       'tip': 'Items the license or has to approve the product but is it going to be ten days '
              "and what if they don't respond in ten days so the key thing it's all about "
              'negotiating and you know the two sides and just remember key rule to '
              "negotiating is that everything's negotiable.",
       'title': 'Licensing Basics: Key Legal Terms In  Brand Licensing [Part 10/10] '
                '(SeltzerLicensingGrp)',
       'url': 'https://www.youtube.com/watch?v=7LHR9Jso37I&t=214s',
       'video_id': '7LHR9Jso37I'},
      {'author': 'University of Minnesota',
       'channel': 'University of Minnesota',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:58](https://www.youtube.com/watch?v=Yqfdzambgbs&t=178s)',
       'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                    'intellectual-property licensing, minimum guarantees, and royalty auditing '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Entirely useless if it that has nothing to develop everyone has to get along '
               'and the OTC serves as that intermediary to try to make sure it happens so '
               'bring your creativity and match it with theirs and amazing things will happen '
               'at the end of the day.',
       'timestamp': 178,
       'timestamp_label': '[00:02:58]',
       'timestamp_seconds': 178,
       'tip': 'Entirely useless if it that has nothing to develop everyone has to get along '
              'and the OTC serves as that intermediary to try to make sure it happens so bring '
              'your creativity and match it with theirs and amazing things will happen at the '
              'end of the day.',
       'title': 'Inside the Office for Technology Commercialization (University of Minnesota)',
       'url': 'https://www.youtube.com/watch?v=Yqfdzambgbs&t=178s',
       'video_id': 'Yqfdzambgbs'},
      {'author': 'IPWatchdog, Inc.',
       'channel': 'IPWatchdog, Inc.',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=qZqv5lEPPQc&t=15s)',
       'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                    'intellectual-property licensing, minimum guarantees, and royalty auditing '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Catch everybody up what what what are you doing these days because I know that '
               "recently you've had sort of a shift in.",
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': 'Catch everybody up what what what are you doing these days because I know that '
              "recently you've had sort of a shift in.",
       'title': 'Patent Monetization: Doing Business as an NPE (IPWatchdog, Inc.)',
       'url': 'https://www.youtube.com/watch?v=qZqv5lEPPQc&t=15s',
       'video_id': 'qZqv5lEPPQc'},
      {'author': 'inventRightTV',
       'channel': 'inventRightTV',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:25:08](https://www.youtube.com/watch?v=LO-vI8icz70&t=1508s)',
       'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                    'intellectual-property licensing, minimum guarantees, and royalty auditing '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "I don't do any of those um other platforms. The Gators seem to be pretty "
               'motivated reaching out. You guys do it every single day. You almost have a '
               'thousand companies in your database.',
       'timestamp': 1508,
       'timestamp_label': '[00:25:08]',
       'timestamp_seconds': 1508,
       'tip': "I don't do any of those um other platforms. The Gators seem to be pretty "
              'motivated reaching out. You guys do it every single day. You almost have a '
              'thousand companies in your database.',
       'title': 'How to Get Open Innovation Companies to Respond (Licensing Playbook) '
                '(inventRightTV)',
       'url': 'https://www.youtube.com/watch?v=LO-vI8icz70&t=1508s',
       'video_id': 'LO-vI8icz70'},
      {'author': 'inventRightTV',
       'channel': 'inventRightTV',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:07](https://www.youtube.com/watch?v=E5dH32uMqOY&t=247s)',
       'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                    'intellectual-property licensing, minimum guarantees, and royalty auditing '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Realize when you start your own business you can't to sell your own product "
               'you could do a little half-ass like micro business or something sell an eBay '
               'and.',
       'timestamp': 247,
       'timestamp_label': '[00:04:07]',
       'timestamp_seconds': 247,
       'tip': "Realize when you start your own business you can't to sell your own product you "
              'could do a little half-ass like micro business or something sell an eBay and.',
       'title': 'Licensing for Royalties (Passive Income) vs. Selling an Idea Yourself '
                '(inventRightTV)',
       'url': 'https://www.youtube.com/watch?v=E5dH32uMqOY&t=247s',
       'video_id': 'E5dH32uMqOY'},
      {'author': 'Secrets of the music industry',
       'channel': 'Secrets of the music industry',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:05](https://www.youtube.com/watch?v=DfuXhSrezTU&t=305s)',
       'relevance': 'Attributed practitioner commentary on patent, brand, catalog, and dataset '
                    'intellectual-property licensing, minimum guarantees, and royalty auditing '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "See, conducting an audit isn't an aggressive act. It's not about starting a "
               "fight. It's an act of self-reliance. It's an act of independence. It's you, "
               'the artist, taking control of your own business and your own career. And so, '
               "we'll just leave you with this question.",
       'timestamp': 305,
       'timestamp_label': '[00:05:05]',
       'timestamp_seconds': 305,
       'tip': "See, conducting an audit isn't an aggressive act. It's not about starting a "
              "fight. It's an act of self-reliance. It's an act of independence. It's you, the "
              "artist, taking control of your own business and your own career. And so, we'll "
              'just leave you with this question.',
       'title': 'Your Right to AUDIT: How to Catch Your Label Stealing Your Royalties 🕵️ '
                '(Secrets of the music industry)',
       'url': 'https://www.youtube.com/watch?v=DfuXhSrezTU&t=305s',
       'video_id': 'DfuXhSrezTU'}]}
